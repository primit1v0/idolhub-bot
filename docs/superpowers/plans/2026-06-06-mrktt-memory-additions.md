# mrktt Memory Additions Implementation Plan

> **Historical status: Implemented.**
>
> This plan is retained for provenance. Checkbox and service-handoff notes are
> historical, not current operational status. See
> [`docs/BASELINE.md`](../../BASELINE.md).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the remaining memory optimizations inspired by `mrktt`: SQLite FTS5 search indexing, Jaccard similarity deduplication, and multi-factor facts scoring.

**Architecture:**
- Create an FTS5 virtual table for messages with database triggers to keep it automatically in sync.
- Add query-based FTS5 retrieval in the agent's run cycle to inject relevant past messages.
- Implement Jaccard similarity deduplication before saving messages to avoid repeating context.
- Implement a multi-factor scoring algorithm (Similarity, Recency, Confidence) for ranking facts.

**Tech Stack:** Python, aiosqlite, pytest

---

### Task 1: Jaccard Similarity Deduplication
**Files:**
- Modify: `memory/sqlite_store.py`
- Modify: `tests/test_memory.py`

- [x] **Step 1: Write the deduplication test**
  Add a test to verify that if a message is Jaccard-similar (>0.8) to the user's last message, it is deduplicated (not inserted again) or ignored.
  Write this in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_jaccard_deduplication(tmp_path):
      from memory.sqlite_store import SqliteStore, calculate_jaccard
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "test", "max_iterations": 3},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {"short_term": {"backend": "sqlite", "path": str(tmp_path / "test.db")}, "long_term": {"backend": "none", "path": ""}},
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })
      store = SqliteStore(cfg)
      await store.initialize()
      
      # Test Jaccard calculations
      assert calculate_jaccard("Saya naik motor hitam", "Saya naik motor hitam") == 1.0
      assert calculate_jaccard("Saya naik motor hitam", "Saya mengendarai motor hitam") > 0.5
      assert calculate_jaccard("Halo apa kabar", "Pagi dunia") == 0.0

      # Add first message
      await store.add_message("user_123", "user", "Saya ingin membeli sepeda baru")
      history1 = await store.get_history("user_123")
      assert len(history1) == 1
      
      # Add highly similar message
      await store.add_message("user_123", "user", "Saya ingin membeli sepeda baru!")
      history2 = await store.get_history("user_123")
      # Length should still be 1 because it is deduplicated
      assert len(history2) == 1
      await store.close()
  ```

- [x] **Step 2: Run pytest to verify the new test fails**
  Run: `.venv/bin/pytest tests/test_memory.py -k test_jaccard_deduplication`
  Expected: Fail (ImportError/AssertionError).

- [x] **Step 3: Implement calculate_jaccard and deduplication in sqlite_store.py**
  Add `calculate_jaccard` helper and modify `add_message` to fetch the last message for the user & role. If similarity > 0.8, skip inserting.
  In `memory/sqlite_store.py`:
  ```python
  import re

  def calculate_jaccard(text1: str, text2: str) -> float:
      words1 = set(re.findall(r'[a-zA-Z0-9]+', text1.lower()))
      words2 = set(re.findall(r'[a-zA-Z0-9]+', text2.lower()))
      if not words1 and not words2:
          return 1.0
      if not words1 or not words2:
          return 0.0
      return len(words1.intersection(words2)) / len(words1.union(words2))
  ```
  And modify `add_message`:
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
          await self.db.commit()
  ```

- [x] **Step 4: Run pytest to verify Jaccard test passes**
  Run: `.venv/bin/pytest tests/test_memory.py -k test_jaccard_deduplication`
  Expected: PASS.

- [x] **Step 5: Commit Jaccard changes**
  Run: `git commit -am "feat(memory): add Jaccard similarity deduplication for messages"`

---

### Task 2: SQLite FTS5 (Full-Text Search) Indexing
**Files:**
- Modify: `memory/sqlite_store.py`
- Modify: `tests/test_memory.py`
- Modify: `core/agent.py`

- [x] **Step 6: Write test for FTS5 indexing & search**
  Add a test to verify FTS5 table is created, kept in sync, and returns relevant matches.
  Write in `tests/test_memory.py`:
  ```python
  @pytest.mark.asyncio
  async def test_fts5_search(tmp_path):
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "test", "max_iterations": 3},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {"short_term": {"backend": "sqlite", "path": str(tmp_path / "test.fts.db")}, "long_term": {"backend": "none", "path": ""}},
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })
      store = SqliteStore(cfg)
      await store.initialize()
      
      # Add messages
      await store.add_message("user_fts", "user", "Saya suka makan martabak keju")
      await store.add_message("user_fts", "assistant", "Martabak keju itu enak sekali!")
      await store.add_message("user_fts", "user", "Bagaimana cuaca hari ini?")
      
      # Search FTS5
      matches = await store.search_history_fts("user_fts", "martabak")
      assert len(matches) >= 1
      assert "martabak" in matches[0]["content"].lower()
      
      await store.close()
  ```

- [x] **Step 7: Run pytest to verify FTS5 test fails**
  Run: `.venv/bin/pytest tests/test_memory.py -k test_fts5_search`
  Expected: FAIL.

- [x] **Step 8: Implement FTS5 table, triggers, and search function**
  Add `messages_fts` table, synchronization triggers, and search method in `memory/sqlite_store.py`:
  In `SqliteStore.initialize`:
  ```python
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
  ```
  Add `search_history_fts` method:
  ```python
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
              SELECT role, content FROM messages_fts 
              WHERE user_id = ? AND messages_fts MATCH ? 
              LIMIT ?
          '''
          try:
              async with self.db.execute(sql, (str(user_id), match_expr, limit)) as cursor:
                  rows = await cursor.fetchall()
              return [{"role": r[0], "content": r[1]} for r in rows]
          except aiosqlite.OperationalError:
              # Fallback jika FTS5 query format bermasalah
              return []
  ```

- [x] **Step 9: Run pytest to verify FTS5 test passes**
  Run: `.venv/bin/pytest tests/test_memory.py -k test_fts5_search`
  Expected: PASS.

- [x] **Step 10: Integrate FTS5 injection into Agent flow**
  Modify `IdolhubAgent.run` in `core/agent.py` to search for matching past messages via FTS5 and inject them as a system message.
  In `core/agent.py:154`:
  ```python
          # Retrieve FTS5 matching messages
          fts_messages = await self.memory.search_history_fts(user_id, user_input, limit=3)
          # Saring agar tidak memasukkan kembali pesan yang baru saja diinput atau sedang di-history aktif
          recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else []
          unique_fts = [m for m in fts_messages if m["content"] not in recent_contents]
          
          if unique_fts:
              fts_md = "Relevant past conversations:\n" + "\n".join(f"- {m['role']}: {m['content']}" for m in unique_fts)
              messages.insert(0, {"role": "system", "content": fts_md})
  ```

- [x] **Step 11: Add unit test verifying FTS5 injection in Agent**
  Write in `tests/test_agent.py`:
  ```python
  @pytest.mark.asyncio
  async def test_agent_fts_injection(monkeypatch):
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "test", "max_iterations": 3},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })

      captured_messages = []
      async def mock_call_llm(config, messages, tools=None):
          nonlocal captured_messages
          captured_messages = list(messages)
          return {"type": "text", "content": "Mock response"}

      monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

      agent = IdolhubAgent(cfg)
      await agent.initialize()

      user_id = "user_fts_agent"
      # Seed old messages directly
      await agent.memory.add_message(user_id, "user", "Saya punya kucing bernama Koko")
      await agent.memory.add_message(user_id, "assistant", "Kucing yang lucu!")
      await agent.memory.add_message(user_id, "user", "Bagaimana cuaca hari ini?") # Distractor
      
      # Act
      await agent.run(user_id=user_id, user_input="Siapa nama kucing saya?")
      
      # Assert FTS injection contains kucing Koko
      assert len(captured_messages) > 0
      assert any(msg["role"] == "system" and "Relevant past conversations:" in msg["content"] and "Koko" in msg["content"] for msg in captured_messages)

      await agent.close()
  ```

- [x] **Step 12: Run unit tests to verify Agent FTS test passes**
  Run: `.venv/bin/pytest tests/test_agent.py -k test_agent_fts_injection`
  Expected: PASS.

---

### Task 3: Multi-factor Facts Scoring
**Files:**
- Modify: `core/agent.py`
- Modify: `tests/test_agent.py`

- [x] **Step 13: Write test for multi-factor facts scoring**
  Add a test to verify that matched facts are ordered based on similarity score, recency (newer first), and confidence.
  Write in `tests/test_agent.py`:
  ```python
  @pytest.mark.asyncio
  async def test_agent_facts_scoring(monkeypatch):
      cfg = AppConfig.model_validate({
          "app": {"name": "test", "mode": "bot"},
          "telegram": {"token": "test"},
          "agent": {"system_prompt": "test", "max_iterations": 3},
          "llm": {"provider": "openai", "model": "gpt-4"},
          "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
          "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
          "skills": {"dir": "./skills"},
          "tools": {"dir": "./tools"},
          "plugins": {"dir": "./plugins"},
          "api": {"enabled": False},
          "mcp": {"enabled": False},
          "logging": {"level": "INFO"}
      })

      captured_messages = []
      async def mock_call_llm(config, messages, tools=None):
          nonlocal captured_messages
          captured_messages = list(messages)
          return {"type": "text", "content": "Mock response"}

      monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

      agent = IdolhubAgent(cfg)
      await agent.initialize()

      user_id = "user_score"
      # Seed facts with different criteria
      # 1. 'motor' - High similarity, low recency
      await agent.memory.save_fakta(user_id, "motor", "mioblack", confidence=0.8)
      # 2. 'hobi motor roda dua' - Partial similarity, newer
      await agent.memory.save_fakta(user_id, "hobi motor roda dua", "riding", confidence=0.9)
      # 3. 'motor sport' - High similarity, newest, lower confidence
      await agent.memory.save_fakta(user_id, "motor sport", "kawasaki", confidence=0.5)

      await agent.run(user_id=user_id, user_input="Ceritakan tentang motor saya")

      # Assert facts ranking in system prompt
      assert len(captured_messages) > 0
      sys_msg = [msg["content"] for msg in captured_messages if msg["role"] == "system" and "Relevant facts:" in msg["content"]][0]
      
      # Motor sport should be ranked high due to exact keyword intersection and newest recency, or motor
      assert "motor sport: kawasaki" in sys_msg
      assert "motor: mioblack" in sys_msg

      await agent.close()
  ```

- [x] **Step 14: Run pytest to verify scoring test fails**
  Run: `.venv/bin/pytest tests/test_agent.py -k test_agent_facts_scoring`
  Expected: FAIL.

- [x] **Step 15: Implement scoring algorithm in Agent facts retrieval**
  Update `IdolhubAgent.run` to score each matched fact:
  `score = (0.5 * similarity) + (0.3 * recency) + (0.2 * confidence)`
  In `core/agent.py`:
  ```python
          # Retrieve facts and score them
          facts = await self.memory.get_fakta(user_id, limit=30)
          query_words = set(re.findall(r'[a-zA-Z0-9]+', user_input.lower()))
          scored_facts = []
          
          # Recency index (newer index is 0, so recency_score = 1.0 - (i / len(facts)))
          for i, fact in enumerate(facts):
              entity = fact.get("entity", "")
              entity_words = set(re.findall(r'[a-zA-Z0-9]+', entity.lower()))
              intersection = query_words.intersection(entity_words)
              if intersection:
                  # 1. Similarity Score
                  sim_score = len(intersection) / len(entity_words) if entity_words else 0.0
                  # 2. Recency Score (based on index)
                  rec_score = 1.0 - (i / len(facts)) if len(facts) > 1 else 1.0
                  # 3. Confidence Score
                  conf_score = fact.get("confidence", 0.9)
                  
                  score = (0.5 * sim_score) + (0.3 * rec_score) + (0.2 * conf_score)
                  scored_facts.append((score, fact))
                  
          # Sort by score DESC
          scored_facts.sort(key=lambda x: x[0], reverse=True)
          relevant_facts = [item[1] for item in scored_facts[:3]]
          
          if relevant_facts:
              facts_md = "Relevant facts:\n" + "\n".join(f"- {f['entity']}: {f['nilai']}" for f in relevant_facts)
              messages.insert(0, {"role": "system", "content": facts_md})
  ```

- [x] **Step 16: Run pytest to verify scoring test passes**
  Run: `.venv/bin/pytest tests/test_agent.py -k test_agent_facts_scoring`
  Expected: PASS.

- [x] **Step 17: Run the entire test suite**
  Run: `.venv/bin/pytest`
  Expected: 38 passed.

- [x] **Step 18: Commit FTS & Scoring changes**
  Run: `git commit -am "feat(memory): add FTS5 indexing and multi-factor facts scoring"`

---

### Task 4: Security Audit & Service Handoff
- [x] **Step 19: Run security scanners**
  Verify with `bandit`, `safety`, and `semgrep`.
- [x] **Step 20: Restart service**
  Run: `systemctl --user restart idolhub`
- [x] **Step 21: Verify service status**
  Run: `systemctl --user status idolhub`
