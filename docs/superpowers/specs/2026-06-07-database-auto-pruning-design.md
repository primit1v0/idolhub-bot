# Design Spec: Database Auto-Pruning

This document describes the design for Phase 2 of the memory optimizations: **Database Auto-Pruning**.

## 1. Problem Statement
The short-term memory database store (`SqliteStore`) currently inserts messages indefinitely. Over time, the SQLite database grows without bound, which can lead to memory bloat, increased disk usage, and degraded performance of search queries (especially FTS5 search queries).

## 2. Proposed Solution
Implement an auto-pruning feature in `SqliteStore` that runs within `add_message`. If enabled, it ensures that the number of stored messages for a specific user does not exceed a configurable limit, pruning older messages when this limit is exceeded.

To keep data integrity, the pruning must:
- Be scoped per `user_id` to prevent cross-user message deletions.
- Integrate with `AppConfig` settings `auto_prune_enabled` and `auto_prune_limit`.
- Be fully synchronized with the FTS5 virtual table (`messages_fts`) via existing database triggers (specifically the `messages_ad` delete trigger).

## 3. Design Details

### 3.1. Config Integration
The configuration settings are defined under `ShortTermMemory` in `idolhub/core/config.py`:
- `auto_prune_enabled`: Boolean flag governing whether pruning is executed (default: `True`).
- `auto_prune_limit`: Integer limit specifying the maximum number of messages to keep per user (default: `1000`).

In `SqliteStore.__init__`, we will read these settings:
```python
self.auto_prune_enabled = cfg.memory.short_term.auto_prune_enabled
self.auto_prune_limit = cfg.memory.short_term.auto_prune_limit
```

### 3.2. Pruning Query in `add_message`
When `add_message` inserts a new message, if `self.auto_prune_enabled` is `True`, it will execute a pruning query for the specified `user_id` to delete messages that fall outside the most recent `self.auto_prune_limit` entries.

The SQL statement to prune old messages for a user:
```sql
DELETE FROM messages
WHERE user_id = ?
  AND id NOT IN (
      SELECT id FROM messages
      WHERE user_id = ?
      ORDER BY id DESC
      LIMIT ?
  )
```

This query:
- Safely targets only messages belonging to the target `user_id`.
- Efficiently keeps only the newest `auto_prune_limit` rows (ordered by `id DESC` to ensure the most recent inserts are preserved).
- Works natively with SQLite's subquery support.

### 3.3. FTS5 Index Synchronization
The SQLite schema defines a trigger `messages_ad`:
```sql
CREATE TRIGGER IF NOT EXISTS messages_ad AFTER DELETE ON messages BEGIN
    INSERT INTO messages_fts(messages_fts, rowid, user_id, role, content) 
    VALUES('delete', old.id, old.user_id, old.role, old.content);
END;
```
Whenever a delete occurs on the `messages` table, this trigger fires automatically, removing the corresponding row from `messages_fts`. No manual FTS5 cleanup is needed in Python code.

## 4. Verification Plan

### 4.1. Unit Tests (`idolhub/tests/test_memory.py`)
1. **Pruning limit enforcement**: Add a test that sets the pruning limit to 3, inserts 5 messages, and asserts that only the newest 3 messages remain in both `get_history` and direct query.
2. **Pruning disabled**: Add a test that sets `auto_prune_enabled = False`, inserts messages beyond the limit, and asserts that nothing is deleted.
3. **FTS5 Synchronization**: Verify that after pruning, the FTS5 search index matches the pruned state (i.e. queries for words in pruned messages return no matches, whereas queries for words in preserved messages return matches).
