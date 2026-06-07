# SQLite Vector Memory (sqlite-vec) Implementation Plan

> **Historical status: Implemented.**
>
> Unchecked boxes are stale plan metadata, not incomplete runtime work.
> References to modifying or committing `config.json` are obsolete because
> that file is local-only. The phase number is local to memory optimization.
> See [`docs/BASELINE.md`](../../BASELINE.md).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement Phase 3 of the memory optimizations by adding local SQLite-based vector memory using the `sqlite-vec` extension and fusing results in the agent RRF merger.

**Architecture:** Modifying `SqliteStore` to handle a separate SQLite database connection at `long_term.path` when `long_term.backend == "sqlite_vec"`. The store will load `sqlite-vec` extension dynamically, manage tables `semantic_messages` and virtual `vec_messages`, generate embeddings using the LLM client, and expose `search_history_semantic`. Finally, update the agent flow to run semantic searches and fuse results using a reciprocal rank dictionary.

**Tech Stack:** Python 3.11, SQLite (aiosqlite), sqlite-vec, OpenAI (async SDK), Pydantic, Pytest.

---

### Task 1: Configuration Updates

**Files:**
- Modify: `core/config.py`
- Modify: `config.json`
- Modify: `config.example.json`
- Modify: `docs/CONFIG.md`
- Test: `tests/test_config.py`

- [ ] **Step 1: Write the failing test**
  Add a test in `tests/test_config.py` verifying that `embedding_model` is read from `long_term` config.
  ```python
  def test_long_term_config_embedding_model():
      from core.config import load_config
      import tempfile
      import json
      
      data = {
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "sys"},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": "x"},
              "long_term": {"backend": "sqlite_vec", "path": "y", "embedding_model": "text-embedding-3-small"}
          },
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      }
      with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
          json.dump(data, f)
          f.flush()
          
      cfg = load_config(f.name)
      assert cfg.memory.long_term.embedding_model == "text-embedding-3-small"
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_config.py -v`
  Expected: FAIL (missing `embedding_model` attribute in LongTermMemory schema)

- [ ] **Step 3: Implement config changes**
  Modify `core/config.py` to add `embedding_model` to `LongTermMemory` class:
  ```python
  class LongTermMemory(BaseModel):
      backend: Literal["none", "sqlite_vec"] = "none"
      path: str = "./data/vectors.db"
      embedding_model: str = "text-embedding-3-small"
  ```
  Add `"embedding_model": "text-embedding-3-small"` to `"long_term"` in `config.json` and `config.example.json`.
  Update `docs/CONFIG.md` to document the new `embedding_model` field under `memory.long_term`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_config.py -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add core/config.py config.json config.example.json docs/CONFIG.md tests/test_config.py
  git commit -m "feat: add embedding_model to long-term memory configuration"
  ```

---

### Task 2: SqliteStore Initialization & sqlite-vec Dynamic Extension Loading

**Files:**
- Modify: `memory/sqlite_store.py`
- Test: `tests/test_memory.py`

- [ ] **Step 1: Write the failing test**
  Add a test `test_sqlite_store_vector_init` in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_sqlite_store_vector_init(tmp_path):
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "sys"},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": str(tmp_path / "short.db")},
              "long_term": {
                  "backend": "sqlite_vec",
                  "path": str(tmp_path / "long.db"),
                  "embedding_model": "text-embedding-3-small"
              }
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
      assert store.vec_db is not None
      # Verify tables exist
      async with store.vec_db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='semantic_messages'") as cursor:
          row = await cursor.fetchone()
          assert row is not None
      await store.close()
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_vector_init -v`
  Expected: FAIL (AttributeError/No attribute vec_db or similar)

- [ ] **Step 3: Implement connection, extension loading, and table creation in `SqliteStore`**
  Modify `memory/sqlite_store.py` to:
  - Import `sqlite_vec`.
  - Store configuration in `__init__`:
    ```python
    self.long_term_backend = cfg.memory.long_term.backend
    self.long_term_path = cfg.memory.long_term.path
    self.embedding_model = cfg.memory.long_term.embedding_model
    self.vec_db = None
    ```
  - In `initialize`:
    ```python
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
    ```
  - In `close`:
    ```python
    if hasattr(self, "vec_db") and self.vec_db:
        await self.vec_db.close()
    ```

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_vector_init -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add memory/sqlite_store.py tests/test_memory.py
  git commit -m "feat: initialize sqlite-vec extension and long-term tables in SqliteStore"
  ```

---

### Task 3: Embedding API Helper in SqliteStore

**Files:**
- Modify: `memory/sqlite_store.py`
- Test: `tests/test_memory.py`

- [ ] **Step 1: Write the failing test**
  Add `test_sqlite_store_get_embedding` in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_sqlite_store_get_embedding(tmp_path, monkeypatch):
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "sys"},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": str(tmp_path / "short.db")},
              "long_term": {
                  "backend": "sqlite_vec",
                  "path": str(tmp_path / "long.db"),
                  "embedding_model": "text-embedding-3-small"
              }
          },
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })
      store = SqliteStore(cfg)
      
      # Mock the OpenAI embeddings.create API
      class MockData:
          embedding = [0.2] * 1536
      class MockResponse:
          data = [MockData()]
      
      async def mock_create(*args, **kwargs):
          return MockResponse()
          
      class MockClient:
          class MockEmbeddings:
              create = mock_create
          embeddings = MockEmbeddings()
          
      monkeypatch.setattr("core.llm.get_llm_client", lambda c: MockClient())
      
      emb = await store._get_embedding("test text")
      assert len(emb) == 1536
      assert emb[0] == 0.2
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_get_embedding -v`
  Expected: FAIL (AttributeError: 'SqliteStore' object has no attribute '_get_embedding')

- [ ] **Step 3: Implement embedding helper**
  Add helper method `_get_embedding` in `SqliteStore`:
  ```python
      async def _get_embedding(self, text: str) -> List[float]:
          from core.llm import get_llm_client
          client = get_llm_client(self.cfg)
          response = await client.embeddings.create(
              model=self.embedding_model,
              input=text
          )
          return response.data[0].embedding
  ```
  Also ensure `self.cfg` is stored in `self.cfg = cfg` in `__init__`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_get_embedding -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add memory/sqlite_store.py tests/test_memory.py
  git commit -m "feat: implement _get_embedding helper method in SqliteStore"
  ```

---

### Task 4: Message Ingestion (Saving embeddings in add_message)

**Files:**
- Modify: `memory/sqlite_store.py`
- Test: `tests/test_memory.py`

- [ ] **Step 1: Write the failing test**
  Add `test_sqlite_store_add_message_vector` in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_sqlite_store_add_message_vector(tmp_path, monkeypatch):
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "sys"},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": str(tmp_path / "short.db")},
              "long_term": {
                  "backend": "sqlite_vec",
                  "path": str(tmp_path / "long.db"),
                  "embedding_model": "text-embedding-3-small"
              }
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
      
      # Mock embedding generator
      async def mock_get_embedding(self, text):
          return [0.5] * 1536
      monkeypatch.setattr(SqliteStore, "_get_embedding", mock_get_embedding)
      
      await store.add_message("user_1", "user", "Hello semantic world")
      
      # Verify message stored in semantic_messages
      async with store.vec_db.execute("SELECT content FROM semantic_messages WHERE user_id='user_1'") as cursor:
          row = await cursor.fetchone()
          assert row is not None
          assert row[0] == "Hello semantic world"
          
      # Verify vector stored in vec_messages
      async with store.vec_db.execute("SELECT rowid FROM vec_messages") as cursor:
          row = await cursor.fetchone()
          assert row is not None
          assert row[0] == 1
          
      await store.close()
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_add_message_vector -v`
  Expected: FAIL (no entries in semantic_messages / vec_messages since we haven't implemented it in `add_message`)

- [ ] **Step 3: Update `add_message` in `SqliteStore`**
  Modify `add_message` in `memory/sqlite_store.py` to save semantic embeddings under try-except safety:
  ```python
          # (inside add_message, after the short-term insert commits)
          if self.long_term_backend == "sqlite_vec" and self.vec_db:
              try:
                  embedding = await self._get_embedding(content)
                  if embedding:
                      cursor = await self.vec_db.execute(
                          'INSERT INTO semantic_messages (user_id, role, content) VALUES (?, ?, ?)',
                          (str(user_id), role, content)
                      )
                      row_id = cursor.lastrowid
                      import sqlite_vec
                      serialized = sqlite_vec.serialize_float32(embedding)
                      await self.vec_db.execute(
                          'INSERT INTO vec_messages (rowid, embedding) VALUES (?, ?)',
                          (row_id, serialized)
                      )
                      await self.vec_db.commit()
              except Exception:
                  # Safe fallback to prevent crashes if offline or API key is invalid
                  pass
  ```
  Ensure we store `self.cfg = cfg` in `__init__`.

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_add_message_vector -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add memory/sqlite_store.py tests/test_memory.py
  git commit -m "feat: save semantic embeddings in add_message with try-except fallback"
  ```

---

### Task 5: Implement search_history_semantic

**Files:**
- Modify: `memory/sqlite_store.py`
- Test: `tests/test_memory.py`

- [ ] **Step 1: Write the failing test**
  Add `test_sqlite_store_search_semantic` in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_sqlite_store_search_semantic(tmp_path, monkeypatch):
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "sys"},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": str(tmp_path / "short.db")},
              "long_term": {
                  "backend": "sqlite_vec",
                  "path": str(tmp_path / "long.db"),
                  "embedding_model": "text-embedding-3-small"
              }
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
      
      # Mock embedding generator
      async def mock_get_embedding(self, text):
          # return unique vectors depending on text
          if "apple" in text:
              return [0.9] * 1536
          return [0.1] * 1536
      monkeypatch.setattr(SqliteStore, "_get_embedding", mock_get_embedding)
      
      await store.add_message("user_1", "user", "I want an apple")
      await store.add_message("user_1", "user", "Sky is blue")
      
      # Search for apple
      results = await store.search_history_semantic("user_1", "Show me apple", limit=1)
      assert len(results) == 1
      assert results[0]["content"] == "I want an apple"
      assert results[0]["role"] == "user"
      
      await store.close()
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_search_semantic -v`
  Expected: FAIL (AttributeError: 'SqliteStore' object has no attribute 'search_history_semantic')

- [ ] **Step 3: Implement search_history_semantic in `SqliteStore`**
  Modify `memory/sqlite_store.py` to add `search_history_semantic`:
  ```python
      async def search_history_semantic(self, user_id: str, query: str, limit: int = 3) -> List[Dict]:
          """Mencari riwayat pesan lama secara semantik menggunakan sqlite-vec MATCH."""
          if self.long_term_backend != "sqlite_vec" or not self.vec_db:
              return []
              
          try:
              embedding = await self._get_embedding(query)
              if not embedding:
                  return []
                  
              import sqlite_vec
              serialized = sqlite_vec.serialize_float32(embedding)
              
              sql = '''
                  SELECT sm.role, sm.content
                  FROM vec_messages v
                  JOIN semantic_messages sm ON v.rowid = sm.id
                  WHERE sm.user_id = ? AND v.embedding MATCH ? AND k = ?
              '''
              async with self.vec_db.execute(sql, (str(user_id), serialized, limit)) as cursor:
                  rows = await cursor.fetchall()
                  
              return [{"role": r[0], "content": r[1]} for r in rows]
          except Exception:
              return []
  ```

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_memory.py::test_sqlite_store_search_semantic -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add memory/sqlite_store.py tests/test_memory.py
  git commit -m "feat: implement search_history_semantic in SqliteStore"
  ```

---

### Task 6: Integrate Semantic search in Agent RRF Merger

**Files:**
- Modify: `core/agent.py`
- Test: `tests/test_agent.py`

- [ ] **Step 1: Write the failing test**
  Add a test `test_agent_semantic_rrf_integration` in `tests/test_agent.py`:
  ```python
  @pytest.mark.asyncio
  async def test_agent_semantic_rrf_integration(tmp_path, monkeypatch):
      from core.agent import IdolhubAgent
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "You are a helpful assistant", "max_iterations": 3, "tools_enabled": False, "memory_enabled": True, "filter_enabled": False, "gating_enabled": False},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {"backend": "sqlite", "path": str(tmp_path / "short.db"), "max_messages": 5, "fts_context_window": 1},
              "long_term": {
                  "backend": "sqlite_vec",
                  "path": str(tmp_path / "long.db"),
                  "embedding_model": "text-embedding-3-small"
              }
          },
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })
      
      # Mock embedding call
      async def mock_get_embedding(self, text):
          return [0.1] * 1536
      monkeypatch.setattr(SqliteStore, "_get_embedding", mock_get_embedding)
      
      # Mock the LLM call to just return text response
      async def mock_call_llm(cfg, messages, tools=None):
          return {"type": "text", "content": "I understand."}
      monkeypatch.setattr("core.agent.call_llm", mock_call_llm)
      
      agent = IdolhubAgent(cfg)
      await agent.initialize()
      
      # Add semantic history directly
      await agent.memory.add_message("user_1", "user", "Previous message about coding")
      
      # Run agent
      res = await agent.run("user_1", "Ask about coding")
      assert res == "I understand."
      
      await agent.close()
  ```

- [ ] **Step 2: Run test to verify it fails**
  Run: `uv run pytest tests/test_agent.py::test_agent_semantic_rrf_integration -v`
  Expected: FAIL or does not fuse semantic search since it's not yet implemented in `core/agent.py`.

- [ ] **Step 3: Update `IdolhubAgent.run` in `core/agent.py`**
  Modify `IdolhubAgent.run` to call semantic search and update the RRF merger to fuse facts, FTS5, and semantic search results using a reciprocal rank dictionary.
  Replace:
  ```python
        # 3. Reciprocal Rank Fusion (RRF) Merger
        # We assign rank score = 1 / (60 + rank)
        rrf_items = []
        for rank, (_, fact) in enumerate(scored_facts):
            score = 1.0 / (60.0 + rank)
            rrf_items.append((score, f"Fakta: {fact['entity']} -> {fact['nilai']}"))
        for rank, msg in enumerate(unique_fts):
            score = 1.0 / (60.0 + rank)
            rrf_items.append((score, f"Pesan lampau ({msg['role']}): {msg['content']}"))
            
        # Sort combined by RRF score DESC and limit to top 3
        rrf_items.sort(key=lambda x: x[0], reverse=True)
        top_rrf = [item[1] for item in rrf_items[:3]]
  ```
  With:
  ```python
        # 2b. Retrieve Semantic matching messages
        semantic_messages = []
        if self.cfg.memory.long_term.backend == "sqlite_vec":
            semantic_messages = await self.memory.search_history_semantic(user_id, user_input, limit=3)
        unique_semantic = [m for m in semantic_messages if m["content"] not in recent_contents]

        # 3. Reciprocal Rank Fusion (RRF) Merger
        # We assign rank score = 1 / (60 + rank)
        rrf_map = {}
        for rank, (_, fact) in enumerate(scored_facts):
            item_str = f"Fakta: {fact['entity']} -> {fact['nilai']}"
            rrf_map[item_str] = rrf_map.get(item_str, 0.0) + (1.0 / (60.0 + rank))
        for rank, msg in enumerate(unique_fts):
            item_str = f"Pesan lampau ({msg['role']}): {msg['content']}"
            rrf_map[item_str] = rrf_map.get(item_str, 0.0) + (1.0 / (60.0 + rank))
        for rank, msg in enumerate(unique_semantic):
            item_str = f"Pesan lampau ({msg['role']}): {msg['content']}"
            rrf_map[item_str] = rrf_map.get(item_str, 0.0) + (1.0 / (60.0 + rank))
            
        # Sort combined by RRF score DESC and limit to top 3
        rrf_items = [(score, item_str) for item_str, score in rrf_map.items()]
        rrf_items.sort(key=lambda x: x[0], reverse=True)
        top_rrf = [item[1] for item in rrf_items[:3]]
  ```

- [ ] **Step 4: Run test to verify it passes**
  Run: `uv run pytest tests/test_agent.py::test_agent_semantic_rrf_integration -v`
  Expected: PASS

- [ ] **Step 5: Commit**
  Run:
  ```bash
  git add core/agent.py tests/test_agent.py
  git commit -m "feat: fuse sqlite-vec semantic search results in agent RRF merger"
  ```
