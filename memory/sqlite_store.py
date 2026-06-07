import os
import re
from typing import Dict, List

import aiosqlite
import sqlite_vec

from core.config import AppConfig


def calculate_jaccard(text1: str, text2: str) -> float:
    words1 = set(re.findall(r'[a-zA-Z0-9]+', text1.lower()))
    words2 = set(re.findall(r'[a-zA-Z0-9]+', text2.lower()))
    if not words1 and not words2:
        return 1.0
    if not words1 or not words2:
        return 0.0
    return len(words1.intersection(words2)) / len(words1.union(words2))


class SqliteStore:
    """
    Short-term memory implementation using async SQLite.
    Menyimpan history obrolan berdasarkan user_id secara persisten tapi cepat.
    """
    def __init__(self, cfg: AppConfig):
        self.cfg = cfg
        self.db_path = cfg.memory.short_term.path
        self.max_messages = cfg.memory.short_term.max_messages
        self.fts_context_window = cfg.memory.short_term.fts_context_window
        self.auto_prune_enabled = getattr(cfg.memory.short_term, "auto_prune_enabled", True)
        self.auto_prune_limit = getattr(cfg.memory.short_term, "auto_prune_limit", 1000)
        self.long_term_backend = cfg.memory.long_term.backend
        self.long_term_path = cfg.memory.long_term.path
        self.embedding_model = cfg.memory.long_term.embedding_model
        self.db = None
        self.vec_db = None

    async def initialize(self):
        """Membuat tabel jika belum ada."""
        # Pastikan direktori ada sebelum bikin DB
        if self.db_path != ":memory:":
            os.makedirs(os.path.dirname(os.path.abspath(self.db_path)), exist_ok=True)
            
        self.db = await aiosqlite.connect(self.db_path)
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        await self.db.execute('CREATE INDEX IF NOT EXISTS idx_user_id ON messages(user_id)')
        
        # Tabel Fakta (Deterministic LTM)
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS fakta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                entity TEXT NOT NULL,
                nilai TEXT NOT NULL,
                confidence REAL DEFAULT 0.9,
                source TEXT DEFAULT 'auto',
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, entity, nilai)
            )
        ''')
        
        # Tabel Preferensi
        await self.db.execute('''
            CREATE TABLE IF NOT EXISTS preferensi (
                user_id TEXT NOT NULL,
                kunci TEXT NOT NULL,
                nilai TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, kunci)
            )
        ''')
        # FTS5 Virtual Table & Triggers
        await self.db.execute('''
            CREATE VIRTUAL TABLE IF NOT EXISTS messages_fts USING fts5(
                user_id,
                role,
                content,
                content='messages',
                content_rowid='id'
            )
        ''')
        
        # Triggers to keep FTS5 synchronized
        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS messages_ai AFTER INSERT ON messages BEGIN
                INSERT INTO messages_fts(rowid, user_id, role, content) VALUES (new.id, new.user_id, new.role, new.content);
            END;
        ''')
        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS messages_ad AFTER DELETE ON messages BEGIN
                INSERT INTO messages_fts(messages_fts, rowid, user_id, role, content) 
                VALUES('delete', old.id, old.user_id, old.role, old.content);
            END;
        ''')
        await self.db.execute('''
            CREATE TRIGGER IF NOT EXISTS messages_au AFTER UPDATE ON messages BEGIN
                INSERT INTO messages_fts(messages_fts, rowid, user_id, role, content) 
                VALUES('delete', old.id, old.user_id, old.role, old.content);
                INSERT INTO messages_fts(rowid, user_id, role, content) VALUES (new.id, new.user_id, new.role, new.content);
            END;
        ''')
        await self.db.commit()

        if self.long_term_backend == "sqlite_vec":
            if self.long_term_path != ":memory:":
                os.makedirs(os.path.dirname(os.path.abspath(self.long_term_path)), exist_ok=True)
            self.vec_db = await aiosqlite.connect(self.long_term_path)
            await self.vec_db.enable_load_extension(True)
            await self.vec_db.load_extension(sqlite_vec.loadable_path())
            await self.vec_db.execute('''
                CREATE TABLE IF NOT EXISTS semantic_messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            await self.vec_db.execute('''
                CREATE VIRTUAL TABLE IF NOT EXISTS vec_messages USING vec0(
                    rowid INTEGER PRIMARY KEY,
                    embedding float[1536]
                )
            ''')
            await self.vec_db.commit()

    async def add_message(self, user_id: str, role: str, content: str):
        """Menambah pesan ke database untuk user tertentu dengan deduplikasi."""
        # Cek pesan terakhir dari user & role yang sama
        query = '''
            SELECT content FROM messages 
            WHERE user_id = ? AND role = ?
            ORDER BY timestamp DESC, id DESC LIMIT 1
        '''
        async with self.db.execute(query, (str(user_id), role)) as cursor:
            row = await cursor.fetchone()
            
        if row:
            last_content = row[0]
            if calculate_jaccard(content, last_content) > 0.8:
                # Lewati insert jika sangat mirip
                return

        await self.db.execute(
            'INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)',
            (str(user_id), role, content)
        )
        
        if self.auto_prune_enabled:
            # Delete messages exceeding the auto_prune_limit
            prune_query = '''
                DELETE FROM messages
                WHERE user_id = ?
                  AND id NOT IN (
                      SELECT id FROM messages
                      WHERE user_id = ?
                      ORDER BY id DESC
                      LIMIT ?
                  )
            '''
            await self.db.execute(prune_query, (str(user_id), str(user_id), self.auto_prune_limit))

        await self.db.commit()

    async def get_history(self, user_id: str) -> List[Dict[str, str]]:
        """Mengambil X pesan terakhir untuk konteks (sesuai max_messages di config)."""
        # Ambil dengan limit, diurutkan DESC untuk dapat yang terbaru, lalu reverse ke urutan asli
        query = '''
            SELECT role, content FROM messages 
            WHERE user_id = ? AND role IN ('user', 'assistant')
            ORDER BY timestamp DESC, id DESC 
            LIMIT ?
        '''
        async with self.db.execute(query, (str(user_id), self.max_messages)) as cursor:
            rows = await cursor.fetchall()
            
        # Reverse agar kronologis (lama -> baru)
        history = [{"role": row[0], "content": row[1]} for row in reversed(rows)]
        return history

    async def save_fakta(self, user_id: str, entity: str, nilai: str, confidence: float = 0.9, source: str = "auto") -> int:
        """Menyimpan atau memperbarui fakta pengguna (EAV facts)."""
        try:
            cursor = await self.db.execute(
                '''INSERT INTO fakta (user_id, entity, nilai, confidence, source) 
                   VALUES (?, ?, ?, ?, ?)''',
                (str(user_id), entity, nilai, confidence, source)
            )
            await self.db.commit()
            return cursor.lastrowid
        except aiosqlite.IntegrityError:
            cursor = await self.db.execute(
                '''UPDATE fakta SET confidence = ?, source = ? 
                   WHERE user_id = ? AND entity = ? AND nilai = ?''',
                (confidence, source, str(user_id), entity, nilai)
            )
            await self.db.commit()
            return cursor.rowcount

    async def get_fakta(self, user_id: str, entity: str | None = None, limit: int = 10) -> List[Dict]:
        """Mengambil daftar fakta pengguna."""
        if entity:
            query = '''SELECT entity, nilai, confidence, source FROM fakta 
                       WHERE user_id = ? AND entity = ? ORDER BY timestamp DESC LIMIT ?'''
            async with self.db.execute(query, (str(user_id), entity, limit)) as cursor:
                rows = await cursor.fetchall()
        else:
            query = '''SELECT entity, nilai, confidence, source FROM fakta 
                       WHERE user_id = ? ORDER BY timestamp DESC LIMIT ?'''
            async with self.db.execute(query, (str(user_id), limit)) as cursor:
                rows = await cursor.fetchall()
        return [{"entity": r[0], "nilai": r[1], "confidence": r[2], "source": r[3]} for r in rows]

    async def delete_fakta(self, user_id: str, entity: str, nilai: str | None = None) -> int:
        """Menghapus fakta pengguna."""
        if nilai:
            cursor = await self.db.execute(
                'DELETE FROM fakta WHERE user_id = ? AND entity = ? AND nilai = ?',
                (str(user_id), entity, nilai)
            )
        else:
            cursor = await self.db.execute(
                'DELETE FROM fakta WHERE user_id = ? AND entity = ?',
                (str(user_id), entity)
            )
        await self.db.commit()
        return cursor.rowcount

    async def set_preferensi(self, user_id: str, kunci: str, nilai: str):
        """Menyimpan atau memperbarui preferensi pengguna."""
        await self.db.execute(
            '''INSERT OR REPLACE INTO preferensi (user_id, kunci, nilai) 
               VALUES (?, ?, ?)''',
            (str(user_id), kunci, nilai)
        )
        await self.db.commit()

    async def get_preferensi(self, user_id: str, kunci: str, default: str = "") -> str:
        """Mengambil nilai preferensi pengguna."""
        query = 'SELECT nilai FROM preferensi WHERE user_id = ? AND kunci = ?'
        async with self.db.execute(query, (str(user_id), kunci)) as cursor:
            row = await cursor.fetchone()
        return row[0] if row else default

    async def search_history_fts(self, user_id: str, query: str, limit: int = 3) -> List[Dict]:
        """Mencari riwayat pesan lama menggunakan FTS5."""
        cleaned_query = re.sub(r'[^a-zA-Z0-9\s]', ' ', query).strip()
        if not cleaned_query:
            return []
        words = [w for w in cleaned_query.split() if len(w) > 2]
        if not words:
            return []
        match_expr = " OR ".join(words)
        
        sql = '''
            WITH matches AS (
                SELECT rowid AS match_id, role AS match_role, content AS match_content
                FROM messages_fts
                WHERE user_id = ? AND messages_fts MATCH ?
                LIMIT ?
            )
            SELECT 
                m.id, 
                m.role, 
                m.content,
                matches.match_id,
                matches.match_role,
                matches.match_content
            FROM messages m
            JOIN matches ON m.user_id = ? AND m.id BETWEEN (matches.match_id - ?) AND (matches.match_id + ?)
            ORDER BY matches.match_id ASC, m.id ASC
        '''
        try:
            async with self.db.execute(sql, (str(user_id), match_expr, limit, str(user_id), self.fts_context_window, self.fts_context_window)) as cursor:
                rows = await cursor.fetchall()
                
            from collections import defaultdict
            grouped = defaultdict(list)
            metadata = {}
            for r in rows:
                msg_id, role, content, match_id, m_role, m_content = r
                grouped[match_id].append((role, content))
                metadata[match_id] = (m_role, m_content)
                
            results = []
            for match_id in sorted(grouped.keys()):
                thread_msgs = grouped[match_id]
                m_role, m_content = metadata[match_id]
                formatted_lines = [f"[{role}]: {content}" for role, content in thread_msgs]
                results.append({
                    "role": m_role,
                    "content": "\n".join(formatted_lines),
                    "matched_content": m_content
                })
            return results
        except aiosqlite.OperationalError:
            # Fallback jika FTS5 query format bermasalah
            return []

    async def close(self):
        """Tutup koneksi database."""
        if self.db:
            await self.db.close()
        if hasattr(self, "vec_db") and self.vec_db:
            await self.vec_db.close()
