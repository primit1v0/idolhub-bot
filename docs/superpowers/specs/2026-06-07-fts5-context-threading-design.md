# Design Spec: FTS5 Context Threading

> **Historical status: Implemented.**
>
> The phase number below is local to the memory-optimization sequence. Current
> status is defined in [`docs/BASELINE.md`](../../BASELINE.md). References to a
> repository-tracked `config.json` are obsolete; runtime configuration is
> local-only.

This document describes the design for Phase 1 of the memory optimizations: **FTS5 Context Threading**.

## 1. Problem Statement
The current FTS5 search in `SqliteStore.search_history_fts` retrieves only the specific individual message that matches the FTS search query. However, an isolated message lacks conversational context (e.g., what was asked before, or how the assistant responded immediately after). This reduces the utility of the recalled memory when injected as context via RRF (Reciprocal Rank Fusion).

## 2. Proposed Solution
When an FTS match is found, instead of returning just the matched message, we fetch the "context thread" containing the matched message and its adjacent messages (a window of size `fts_context_window` before and after). 

For example, if `fts_context_window = 2` and a message at ID `10` matches the FTS search:
- We retrieve messages with IDs from `10 - 2` to `10 + 2` (IDs `8, 9, 10, 11, 12`).
- We restrict the retrieved context messages to the same `user_id` to prevent cross-user leakage.
- We format this sequence of messages chronologically as a single thread string.
- We return this thread as the memory match context.

## 3. Design Details

### 3.1. Config Integration
The context window size will be configured via `memory.short_term.fts_context_window` (default 2), which is already defined in the `AppConfig` schema (`ShortTermMemory` model) and standard `config.json`.

### 3.2. SQLite Query Implementation
To avoid N+1 queries (first querying `messages_fts` to find match IDs, then querying `messages` individually for each match ID), we can use a single SQL query with a CTE (Common Table Expression):

```sql
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
```

### 3.3. Formatting the Context Thread
We will group the returned messages by `match_id` (preserving chronologial order of messages within each group). For each match, we build the thread string:
```
[role1]: content1
[role2]: content2
```
For example:
```
[user]: Saya lapar sekali
[assistant]: Kamu mau makan apa?
[user]: Mau martabak manis keju dong
[assistant]: Martabak manis keju itu enak sekali!
[user]: Belinya di mana ya?
```

### 3.4. Updating search_history_fts Interface
The `search_history_fts` method will return:
```python
List[Dict[str, str]]
```
Where each dict represents a match:
```python
{
    "role": match_role,
    "content": formatted_thread_string,
    "matched_content": match_content
}
```
Adding `matched_content` ensures that `IdolhubAgent` can still deduplicate and check whether the matched message itself was already in the recent conversation (so we don't redundantly inject it).

In `core/agent.py`:
```python
# 2. Retrieve FTS5 matching messages
fts_messages = await self.memory.search_history_fts(user_id, user_input, limit=3)
recent_contents = [m["content"] for m in messages[-4:]] if len(messages) >= 4 else [m["content"] for m in messages]
unique_fts = [m for m in fts_messages if m.get("matched_content", m["content"]) not in recent_contents]
```

## 4. Verification Plan

### 4.1. Unit Tests (`tests/test_memory.py`)
- Test that `search_history_fts` correctly fetches the context window with the default window size (2).
- Test that it bounds context search to the same `user_id` (adjacent messages from other users are not included).
- Test that window size from config is respected (e.g. testing with window size 1 or 0).

### 4.2. Integration Tests (`tests/test_agent.py`)
- Test that the agent utilizes the threaded context from long-past conversations correctly to answer a query.
