# Current Baseline

**Baseline date:** June 7, 2026  
**Runtime:** Python 3.11+, PocketFlow, Telegram, FastAPI, MCP stdio  
**Verification:** 67 tests passed

This document is the canonical status reference. Historical phase numbers in
`docs/superpowers/` describe the order of past work only.

The proposed next phase is tracked in
[`docs/NEXT_PHASE.md`](NEXT_PHASE.md). Active project specifications are stored
under `docs/specs/` and apply to every model and contributor.

## Implemented

- Telegram bot with PocketFlow async agent flow.
- OpenAI-compatible LLM client supporting `openai`, `gemini`,
  `openai_codex`, and `github_copilot` credential layouts.
- REST API with chat, health, and local configuration endpoints.
- MCP stdio server exposing the sandboxed shell tool.
- Skill discovery from Markdown frontmatter.
- Plugin lifecycle hooks.
- Built-in web search, sandbox shell, fact, and preference tools.
- SQLite conversation history with Jaccard deduplication.
- EAV facts and preferences.
- FTS5 context threading.
- Automatic per-user history pruning.
- Prompt-injection filtering and explicit-consent memory writes.
- Optional sqlite-vec semantic memory.
- RRF fusion across facts, FTS5 threads, and semantic matches.

## Configuration Contract

- `config.example.json` is the only tracked configuration template.
- `config.json` is required at runtime, local-only, and ignored by Git.
- Copy the example before running:

  ```bash
  cp config.example.json config.json
  ```

- Secrets are referenced as `$VARIABLE` and resolved from the process
  environment.
- Every `$VARIABLE` present in local `config.json` must exist, even under an
  inactive provider. Keep only provider blocks that are actually configured.
- `config.json`, `.env`, databases, logs, and workspace contents must never be
  committed.

## Implemented Configuration Controls

- `app.mode`
- `agent.max_iterations`
- `agent.tools_enabled`
- `agent.filter_enabled`
- `agent.gating_enabled`
- `telegram.token`, `telegram.allowed_users`, `telegram.parse_mode`
- all `llm` request settings
- selected `providers[llm.provider]`
- all short-term and long-term memory settings
- `skills.dir`, `skills.enabled`
- `tools.enabled`
- `plugins.dir`
- `api.host`, `api.port`, `api.cors_origins`
- `logging.level`, `logging.format`

## Accepted But Not Enforced Yet

These keys are accepted by the schema but do not currently control runtime
behavior:

- `app.debug`
- `app.timezone`
- `agent.memory_enabled`
- `tools.dir`
- `plugins.enabled`
- `api.enabled`
- `mcp.enabled`
- `mcp.port` (the MCP server currently uses stdio)

They must not be described as active toggles until implementation and tests
exist.

## Deferred

- Dashboard WebUI. The directory is a placeholder only.

## Proposed Next Phase

- Foundation hardening is listed as 39 work titles in
  [`docs/specs/2026-06-07-baseline-foundation-hardening.md`](specs/2026-06-07-baseline-foundation-hardening.md).
- No implementation schema or task plan has been approved yet.
- Start future sessions from [`docs/NEXT_PHASE.md`](NEXT_PHASE.md).

## Not Scheduled

- Voice interface.
- Multi-agent orchestration.
- Additional RAG backends.

No implementation work should start from these items without an approved
design and implementation plan.
