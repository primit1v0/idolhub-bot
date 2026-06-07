# Design Spec: SQLite Vector Memory (sqlite-vec)

> **Historical status: Implemented.**
>
> The phase number below is local to the memory-optimization sequence, not the
> active project roadmap. Current behavior includes lazy optional dependency
> loading, logged embedding fallback, and semantic RRF integration. See
> [`docs/BASELINE.md`](../../BASELINE.md).

This document specifies the design for Phase 3 of the memory optimizations: implementing local semantic vector search using the `sqlite-vec` extension.

## 1. Context & Motivation

Currently, the agent uses two memory mechanisms:
1. **Facts (EAV)**: A deterministic list of facts extracted from user interactions.
2. **FTS5 (Full-Text Search)**: Keyword-based search over the chat history database.

While FTS5 is efficient for exact keyword matches, it fails to capture semantic similarity (e.g. searching for "automobile" when the user said "car"). Adding vector search using `sqlite-vec` provides a lightweight, local, file-based semantic memory without requiring heavy external database services.

## 2. Configuration Settings

We add configuration options under `LongTermMemory` in `core/config.py` and configuration files:

- `embedding_model`: A string specifying the OpenAI-compatible embedding model to use (default: `"text-embedding-3-small"`).

### Updated Config Classes (Pydantic)

```python
class LongTermMemory(BaseModel):
    backend: Literal["none", "sqlite_vec"] = "none"
    path: str = "./data/vectors.db"
    embedding_model: str = "text-embedding-3-small"
```

## 3. Database Schema & Architecture

When `long_term.backend` is set to `"sqlite_vec"`, `SqliteStore` will establish a separate connection to the database file at `long_term.path`.

### Extension Loading
During initialization of `SqliteStore`, the `sqlite-vec` extension is dynamically loaded:
```python
import sqlite_vec

await self.vec_db.enable_load_extension(True)
await self.vec_db.load_extension(sqlite_vec.loadable_path())
```

### Tables
1. **`semantic_messages`**: A regular table storing message metadata:
   - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `user_id`: TEXT NOT NULL
   - `role`: TEXT NOT NULL
   - `content`: TEXT NOT NULL
   - `timestamp`: DATETIME DEFAULT CURRENT_TIMESTAMP

2. **`vec_messages`**: A virtual table managed by the `vec0` module (from `sqlite-vec`) with 1536 float dimensions:
   - `rowid`: INTEGER PRIMARY KEY (maps to `semantic_messages.id`)
   - `embedding`: float[1536]

```sql
CREATE TABLE IF NOT EXISTS semantic_messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE VIRTUAL TABLE IF NOT EXISTS vec_messages USING vec0(
    rowid INTEGER PRIMARY KEY,
    embedding float[1536]
);
```

## 4. Workflows

### A. Message Ingestion (`add_message`)
When a message is added:
1. The message is stored in the short-term memory database.
2. If `long_term.backend == "sqlite_vec"`, an async task/helper is triggered to:
   - Generate embeddings using `client.embeddings.create` via `get_llm_client(self.cfg)`.
   - Save message details in `semantic_messages`.
   - Serialize the embedding list using `sqlite_vec.serialize_float32()`.
   - Save the serialized vector in `vec_messages` using the generated row ID.
3. The process is wrapped in a `try-except` block to ensure that API errors, invalid credentials, or network failures do not disrupt the chat execution flow.

### B. Semantic Search (`search_history_semantic`)
Performs K-Nearest Neighbors (KNN) search:
1. Generates query vector embedding from user query.
2. Serializes query vector.
3. Queries closest match:
   ```sql
   SELECT sm.role, sm.content
   FROM vec_messages v
   JOIN semantic_messages sm ON v.rowid = sm.id
   WHERE sm.user_id = ? AND v.embedding MATCH ? AND k = ?
   ```
4. Returns a list of dicts: `[{"role": role, "content": content}, ...]`

### C. Reciprocal Rank Fusion (RRF)
We update `IdolhubAgent.run` to call semantic search and fuse results.
To handle duplicate messages (e.g., if FTS5 and semantic search both retrieve the same historical message), we sum their reciprocal rank scores in a dictionary:

```python
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

rrf_items = [(score, item) for item, score in rrf_map.items()]
rrf_items.sort(key=lambda x: x[0], reverse=True)
top_rrf = [item[1] for item in rrf_items[:3]]
```

## 5. Testing & Verification

- **Mocking**: In unit tests, the embedding API client will be mocked to return a static 1536 float list.
- **Unit Tests (`tests/test_memory.py`)**:
  - Verify loading of `sqlite-vec` extension.
  - Verify initialization of tables.
  - Verify embedding retrieval and storage.
  - Verify KNN search retrieves closest match.
  - Verify fallback behavior when backend is `"none"`.
- **Integration Tests (`tests/test_agent.py`)**:
  - Verify that `IdolhubAgent` initializes `sqlite-vec` and runs semantic search as part of the flow when configured.
