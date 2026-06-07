# Database Auto-Pruning Implementation Plan

> **Historical status: Implemented.**
>
> Unchecked boxes are stale plan metadata, not incomplete runtime work. The
> phase number is local to memory optimization. See
> [`docs/BASELINE.md`](../../BASELINE.md).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement automatic pruning of short-term memory messages per user based on configured limit.

**Architecture:** Retrieve config settings `auto_prune_enabled` and `auto_prune_limit` during `SqliteStore` initialization. In `add_message`, after inserting a new message, if pruning is enabled, run a SQL query to delete messages for the user that exceed the limit. The existing SQLite trigger will automatically keep the FTS5 index synchronized.

**Tech Stack:** Python, SQLite, aiosqlite, pytest

---

### Task 1: Update SqliteStore Initialization and Configuration Reading

**Files:**
- Modify: `idolhub/memory/sqlite_store.py`

- [ ] **Step 1: Read config options in `SqliteStore.__init__`**

Modify `idolhub/memory/sqlite_store.py` to store `auto_prune_enabled` and `auto_prune_limit` from the config object.

```python
    def __init__(self, cfg: AppConfig):
        self.db_path = cfg.memory.short_term.path
        self.max_messages = cfg.memory.short_term.max_messages
        self.fts_context_window = cfg.memory.short_term.fts_context_window
        self.auto_prune_enabled = getattr(cfg.memory.short_term, "auto_prune_enabled", True)
        self.auto_prune_limit = getattr(cfg.memory.short_term, "auto_prune_limit", 1000)
        self.db = None
```

- [ ] **Step 2: Commit initial config parsing changes**

Run:
```bash
git add idolhub/memory/sqlite_store.py
git commit -m "feat: read auto_prune_enabled and auto_prune_limit from configuration"
```

---

### Task 2: Implement Auto-Pruning in add_message

**Files:**
- Modify: `idolhub/memory/sqlite_store.py`

- [ ] **Step 1: Implement pruning logic**

Modify `add_message` in `idolhub/memory/sqlite_store.py` to prune messages when `auto_prune_enabled` is True and the limit is exceeded.

```python
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
```

- [ ] **Step 2: Commit pruning implementation**

Run:
```bash
git add idolhub/memory/sqlite_store.py
git commit -m "feat: implement sqlite database auto-pruning in add_message"
```

---

### Task 3: Write and Run Unit Tests for Auto-Pruning

**Files:**
- Modify: `idolhub/tests/test_memory.py`

- [ ] **Step 1: Add auto-pruning tests**

Append unit tests in `idolhub/tests/test_memory.py` to verify:
1. Pruning limit is enforced and old messages are deleted.
2. FTS5 indexes are synchronized with deleted messages.
3. Pruning is not executed when disabled.

```python
@pytest.mark.asyncio
async def test_memory_auto_prune_enforced(tmp_path):
    # Setup config with auto_prune_limit = 3
    db_path = str(tmp_path / "test_prune.db")
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {
            "short_term": {
                "backend": "sqlite",
                "path": db_path,
                "max_messages": 10,
                "fts_context_window": 1,
                "auto_prune_enabled": True,
                "auto_prune_limit": 3
            },
            "long_term": {"backend": "none", "path": ""}
        },
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    store = SqliteStore(cfg)
    await store.initialize()
    
    user_id = "user_prune"
    # Insert 5 messages
    await store.add_message(user_id, "user", "Message apple")
    await store.add_message(user_id, "assistant", "Message banana")
    await store.add_message(user_id, "user", "Message cherry")
    await store.add_message(user_id, "assistant", "Message date")
    await store.add_message(user_id, "user", "Message elderberry")
    
    # Check that only the newest 3 messages remain in database
    async with store.db.execute("SELECT content FROM messages WHERE user_id = ? ORDER BY id ASC", (user_id,)) as cursor:
        rows = await cursor.fetchall()
    contents = [r[0] for r in rows]
    assert contents == ["Message cherry", "Message date", "Message elderberry"]
    
    # Verify FTS5 matches the pruned state
    # Searching for "apple" should return nothing since it is pruned
    fts_results_apple = await store.search_history_fts(user_id, "apple")
    assert len(fts_results_apple) == 0
    
    # Searching for "elderberry" should return the match
    fts_results_elderberry = await store.search_history_fts(user_id, "elderberry")
    assert len(fts_results_elderberry) > 0
    
    await store.close()


@pytest.mark.asyncio
async def test_memory_auto_prune_disabled(tmp_path):
    # Setup config with auto_prune_enabled = False and limit = 3
    db_path = str(tmp_path / "test_prune_disabled.db")
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {
            "short_term": {
                "backend": "sqlite",
                "path": db_path,
                "max_messages": 10,
                "fts_context_window": 1,
                "auto_prune_enabled": False,
                "auto_prune_limit": 3
            },
            "long_term": {"backend": "none", "path": ""}
        },
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    store = SqliteStore(cfg)
    await store.initialize()
    
    user_id = "user_prune"
    # Insert 5 messages
    await store.add_message(user_id, "user", "Message apple")
    await store.add_message(user_id, "assistant", "Message banana")
    await store.add_message(user_id, "user", "Message cherry")
    await store.add_message(user_id, "assistant", "Message date")
    await store.add_message(user_id, "user", "Message elderberry")
    
    # Check that all 5 messages remain in database
    async with store.db.execute("SELECT content FROM messages WHERE user_id = ? ORDER BY id ASC", (user_id,)) as cursor:
        rows = await cursor.fetchall()
    contents = [r[0] for r in rows]
    assert len(contents) == 5
    assert contents == ["Message apple", "Message banana", "Message cherry", "Message date", "Message elderberry"]
    
    await store.close()
```

- [ ] **Step 2: Run all unit tests**

Run:
```bash
.venv/bin/pytest tests/test_memory.py -v
```
Expected: All tests pass.

- [ ] **Step 3: Commit unit tests**

Run:
```bash
git add idolhub/tests/test_memory.py
git commit -m "test: add unit tests for database auto-pruning"
```

---

### Task 4: Complete Verification and Cleanup

**Files:**
- Modify: None

- [ ] **Step 1: Run complete test suite**

Run:
```bash
.venv/bin/pytest
```
Expected: All 59+ tests pass.

- [ ] **Step 2: Audit changed files**
Verify zero dead code, clean imports, and no unused variables in `idolhub/memory/sqlite_store.py` and `idolhub/tests/test_memory.py`.
