# Memory Integration Implementation Plan

> **Historical status: Implemented.**
>
> This plan is retained for provenance. Current behavior and status are defined
> in [`docs/BASELINE.md`](../../BASELINE.md).

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Integrate EAV facts and preferences schema with FTS5 search into the IdolhubAgent workflow and expose memory management tools to the agent.

**Architecture:** 
- Add `save_fact` and `set_preference` to the tool schema and registry.
- Inject relevant facts queried using a lightweight keyword matching strategy from the SQLite database before running the LLM call.
- Add comprehensive integration tests in `tests/test_agent.py`.

**Tech Stack:** Python, aiosqlite, pocketflow, pytest

---

### Task 1: Add Memory Management Tools
**Files:**
- Modify: `tools/registry.py`
- Modify: `tests/test_agent.py`

- [x] **Step 1: Implement the tool functions**
  Add `save_fact(entity: str, nilai: str, confidence: float = 0.9, source: str = "auto")` and `set_preference(kunci: str, nilai: str)` to `tools/registry.py` and register them in `TOOLS_MAPPING` and `TOOLS_SCHEMA`. These tools will call the agent's memory store methods.
  *Note:* Since `tools/registry.py` functions are called dynamically without a direct `agent` context, we need access to the running `agent.memory` instance. We can modify the tool execution context in `core/agent.py` or retrieve the memory store. Let's make `execute_bash`, `save_fact` and `set_preference` accept an optional `agent_context` or access a shared instance, or pass it via argument mapping. In `core/agent.py:77-80`:
  ```python
  func_result = self.tools_mapping[func_name](**args)
  ```
  We can check if the tool function accepts `user_id` or similar parameters and pass them.
  Wait, let's inspect `tools/registry.py` to design how the tools can access the database.
  We can implement `save_fact(user_id: str, entity: str, nilai: str)` where `user_id` is passed automatically by the agent or manually.
  Let's define them in `tools/registry.py`:
  ```python
  def save_fact(entity: str, nilai: str, user_id: str = "default") -> str:
      # We need access to the database. We can initialize a local memory store or use a shared one.
      # Since we already have the cfg and SqliteStore, we can create a temporary or shared store.
      # Better: import config and agent instance, or initialize a quick connection to config's DB path.
      pass
  ```
- [x] **Step 2: Update tool schema in `tools/registry.py`**
  Add schemas for `save_fact` and `set_preference`.
- [x] **Step 3: Commit Task 1 changes**

### Task 2: Inject Relevant Facts into Agent Execution Context
**Files:**
- Modify: `core/agent.py`

- [x] **Step 4: Implement local factual recall**
  Add a query matching step in `IdolhubAgent.run` to call a new method `self.memory.recall_factual(query=user_input)` (or local keyword extraction from input) to retrieve facts related to words in the user query.
- [x] **Step 5: Inject context into system message**
  If any relevant facts are found, format them into a clean markdown block and prepend it to the conversation history as a system message.
- [x] **Step 6: Commit Task 2 changes**

### Task 3: Integration Testing & Verification
**Files:**
- Modify: `tests/test_agent.py`

- [x] **Step 7: Add integration tests**
  Write a test case where a user tells the agent their motor name. Verify that:
  - The agent calls `save_fact` tool.
  - The fact is saved in the database.
  - The next message query retrieve this fact and the agent correctly answers using the fact.
- [x] **Step 8: Run all unit tests and security audits**
  Verify with `pytest`, `semgrep`, and `bandit`.
- [x] **Step 9: Commit Task 3 changes**
