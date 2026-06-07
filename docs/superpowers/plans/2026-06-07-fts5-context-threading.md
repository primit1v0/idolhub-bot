# FTS5 Context Threading Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement FTS5 Context Threading to retrieve search matches along with their adjacent conversation messages formatted as a thread.

**Architecture:** Update `SqliteStore.search_history_fts` to query messages within a context window of size `fts_context_window` around matching search row IDs, bound by `user_id`. Format retrieved messages chronologically as `[role]: content` thread strings. Update `IdolhubAgent` to filter using the matched content.

**Tech Stack:** Python, SQLite FTS5, aiosqlite, pytest

---

### Task 1: Update SqliteStore for FTS5 Context Threading

**Files:**
- Modify: `memory/sqlite_store.py`
- Test: `tests/test_memory.py`

- [ ] **Step 1: Write a failing unit test in `tests/test_memory.py`**
  Add `test_fts5_context_threading` to verify that `search_history_fts` returns the context window messages formatted as a single string thread.

  ```python
  @pytest.mark.asyncio
  async def test_fts5_context_threading(tmp_path):
      from memory.sqlite_store import SqliteStore
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "test", "max_iterations": 3},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {
              "short_term": {
                  "backend": "sqlite", 
                  "path": str(tmp_path / "test.fts_thread.db"),
                  "fts_context_window": 1
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
      
      # Add chronological messages
      await store.add_message("user_fts", "user", "Message 1")
      await store.add_message("user_fts", "assistant", "Message 2")
      await store.add_message("user_fts", "user", "Message 3 (match me)")
      await store.add_message("user_fts", "assistant", "Message 4")
      
      # Search FTS5
      matches = await store.search_history_fts("user_fts", "match")
      assert len(matches) == 1
      assert matches[0]["role"] == "user"
      assert matches[0]["matched_content"] == "Message 3 (match me)"
      # Window is 1, so it should fetch Message 2 (id = 2), Message 3 (id = 3), Message 4 (id = 4)
      expected_thread = "[assistant]: Message 2\n[user]: Message 3 (match me)\n[assistant]: Message 4"
      assert matches[0]["content"] == expected_thread
      
      await store.close()
  ```

- [ ] **Step 2: Run pytest to verify the new test fails**
  Run: `.venv/bin/pytest tests/test_memory.py::test_fts5_context_threading -v`
  Expected: Fail with `KeyError` or missing `matched_content` or incorrect content format.

- [ ] **Step 3: Update `SqliteStore.__init__` and `SqliteStore.search_history_fts` in `memory/sqlite_store.py`**
  Modify `SqliteStore.__init__` to store `self.fts_context_window` from config.
  Rewrite `search_history_fts` to use a CTE query that fetches the matched rowid and queries adjacent messages within the window for the same `user_id`, grouping and formatting them.

  Code changes:
  ```python
  # memory/sqlite_store.py:25
  def __init__(self, cfg: AppConfig):
      self.db_path = cfg.memory.short_term.path
      self.max_messages = cfg.memory.short_term.max_messages
      self.fts_context_window = cfg.memory.short_term.fts_context_window
      self.db = None
  ```

  ```python
  # memory/sqlite_store.py:207
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
          return []
  ```

- [ ] **Step 4: Run test to verify it passes**
  Run: `.venv/bin/pytest tests/test_memory.py::test_fts5_context_threading -v`
  Expected: PASS

- [ ] **Step 5: Run all test_memory.py tests to ensure no regressions**
  Run: `.venv/bin/pytest tests/test_memory.py -v`
  Expected: PASS

- [ ] **Step 6: Commit changes for Task 1**
  Run: `git add memory/sqlite_store.py tests/test_memory.py && git commit -m "feat: implement FTS5 Context Threading in SqliteStore"`

---

### Task 2: Update Agent Query Logic for Matched Content Deduplication

**Files:**
- Modify: `core/agent.py`
- Test: `tests/test_agent.py`

- [ ] **Step 1: Write an integration test in `tests/test_agent.py`**
  Add a test `test_agent_fts_threading_integration` that adds older messages to memory, then queries the agent. It checks that the agent uses the context thread of the matched messages.

- [ ] **Step 2: Update query deduplication filter in `core/agent.py`**
  Update line 197 in `core/agent.py` to use `m.get("matched_content", m["content"])` instead of `m["content"]` when filtering out already recent contents.

  ```python
  # core/agent.py:197
  unique_fts = [m for m in fts_messages if m.get("matched_content", m["content"]) not in recent_contents]
  ```

- [ ] **Step 3: Run the integration tests**
  Run: `.venv/bin/pytest tests/test_agent.py -v`
  Expected: PASS

- [ ] **Step 4: Commit changes for Task 2**
  Run: `git add core/agent.py && git commit -m "feat: update agent deduplication to use matched_content"`

---

### Task 3: Audit, Clean Up and Verify Everything

**Files:**
- Audit: All modified files
- Verify: Run full pytest test suite

- [ ] **Step 1: Audit code for zero dead code, clean imports, no unused variables**
- [ ] **Step 2: Run the full test suite**
  Run: `.venv/bin/pytest`
  Expected: 55+ tests pass.
- [ ] **Step 3: Commit all remaining files and report back**
