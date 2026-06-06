import aiosqlite
import os
from typing import List, Dict
from core.config import AppConfig

class SqliteStore:
    """
    Short-term memory implementation using async SQLite.
    Menyimpan history obrolan berdasarkan user_id secara persisten tapi cepat.
    """
    def __init__(self, cfg: AppConfig):
        self.db_path = cfg.memory.short_term.path
        self.max_messages = cfg.memory.short_term.max_messages
        self.db = None

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
        await self.db.commit()

    async def add_message(self, user_id: str, role: str, content: str):
        """Menambah pesan ke database untuk user tertentu."""
        await self.db.execute(
            'INSERT INTO messages (user_id, role, content) VALUES (?, ?, ?)',
            (str(user_id), role, content)
        )
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

    async def close(self):
        """Tutup koneksi database."""
        if self.db:
            await self.db.close()
