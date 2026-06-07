# Current Baseline

**Baseline date:** June 7, 2026  
**Runtime:** Python 3.11+, PocketFlow, Telegram, FastAPI, MCP stdio  
**Verification:** 113 tests passed (100% pass rate)  
**Current Phase:** Phase 1 Complete ✅

This document is the canonical status reference. Historical specifications in `docs/superpowers/` describe past work only.

The next phase is tracked in [`docs/NEXT_PHASE.md`](NEXT_PHASE.md). Active project specifications are stored under `docs/specs/` and apply to every model and contributor.

## Phase 1: Configuration Hardening ✅ COMPLETE

**Status:** 113/113 tests passing  
**Completed:** June 7, 2026  
**Documentation:** [PHASE1_COMPLETION.md](../PHASE1_COMPLETION.md)

### Implemented Features

- ✅ Pydantic-based configuration validation
- ✅ Environment variable resolution (`$VAR` syntax)
- ✅ Telegram token format validation (bot_id:token)
- ✅ Provider URL validation (HTTPS required)
- ✅ System prompt validation (min 10 chars)
- ✅ Memory path validation (non-empty)
- ✅ Auto-prune limits (min 100 messages)
- ✅ Secret masking in API responses
- ✅ Hot-reload capability with validation
- ✅ Secrets overwrite protection

### Key Files

- `core/config_schema.py` - Pydantic models
- `core/config_validator.py` - Validation logic
- `core/config_reloader.py` - Hot-reload capability
- `tests/conftest.py` - Centralized test fixtures

## Core Features (Pre-Phase 1)

- Telegram bot with PocketFlow async agent flow
- OpenAI-compatible LLM client supporting `openai`, `gemini`, `openai_codex`, and `github_copilot` credential layouts
- REST API with chat, health, and local configuration endpoints
- MCP stdio server exposing the sandboxed shell tool
- Skill discovery from Markdown frontmatter
- Plugin lifecycle hooks
- Built-in web search, sandbox shell, fact, and preference tools
- SQLite conversation history with Jaccard deduplication
- EAV facts and preferences
- FTS5 context threading
- Automatic per-user history pruning
- Prompt-injection filtering and explicit-consent memory writes
- Optional sqlite-vec semantic memory
- RRF fusion across facts, FTS5 threads, and semantic matches

## Configuration Contract

- `config.example.json` is the only tracked configuration template
- `config.json` is required at runtime, local-only, and ignored by Git
- Copy the example before running:

  ```bash
  cp config.example.json config.json
  ```

- Secrets are referenced as `$VARIABLE` and resolved from the process environment
- Every `$VARIABLE` present in local `config.json` must exist in the environment
- **Never commit:** `config.json`, `.env`, databases, logs, workspace contents

## Implemented Configuration Controls

### Fully Functional
- `app.mode` - Runtime mode (bot/api/mcp)
- `agent.max_iterations` - Max agent loop iterations
- `agent.tools_enabled` - Enable/disable tools
- `agent.filter_enabled` - Enable/disable prompt injection filter
- `agent.gating_enabled` - Enable/disable memory write gating
- `telegram.token` - Bot token (validated format)
- `telegram.allowed_users` - User allowlist
- `telegram.parse_mode` - Message parsing mode
- All `llm` request settings (temperature, max_tokens, etc.)
- Selected `providers[llm.provider]` - Active provider config
- All short-term and long-term memory settings
- `skills.dir` - Skills directory path
- `skills.enabled` - Enable/disable skills
- `tools.enabled` - Enable/disable tools
- `plugins.dir` - Plugins directory path
- `api.host` - API server host
- `api.port` - API server port
- `api.cors_origins` - CORS allowed origins
- `logging.level` - Log level
- `logging.format` - Log format

### Accepted But Not Enforced Yet

These keys are accepted by the schema but do not currently control runtime behavior:

- `app.debug` - Debug mode flag
- `app.timezone` - Application timezone
- `agent.memory_enabled` - Memory enable/disable toggle
- `tools.dir` - Tools directory (not auto-discovered yet)
- `plugins.enabled` - Plugin enable/disable toggle
- `api.enabled` - API enable/disable toggle
- `mcp.enabled` - MCP enable/disable toggle
- `mcp.port` - MCP server port (currently uses stdio only)

They must not be described as active toggles until implementation and tests exist.

## Proposed Next Phase

**Phase 2: Secrets Management** 📋 Planned

- Complete technical design: [`docs/specs/phase2-secrets-management-design.md`](specs/phase2-secrets-management-design.md)
- Objectives: Remove secrets from config.json, implement secure backend (Vault/AWS), add rotation
- Estimated: 3 weeks, 15+ new tests (128 total expected)
- Start future sessions from [`docs/NEXT_PHASE.md`](NEXT_PHASE.md)

## Deferred

- Dashboard WebUI (directory is placeholder only)

## Not Scheduled

- Voice interface
- Multi-agent orchestration
- Additional RAG backends

No implementation work should start from these items without an approved design and implementation plan.

## Documentation Structure

### Active Documentation
- [`AGENT_GUIDE.md`](AGENT_GUIDE.md) - Guide for AI agents
- [`BASELINE.md`](BASELINE.md) - This file (current status)
- [`NEXT_PHASE.md`](NEXT_PHASE.md) - Next phase handoff
- [`CONFIG.md`](CONFIG.md) - Configuration reference
- [`EXECUTION_PROTOCOL.md`](EXECUTION_PROTOCOL.md) - Development guidelines
- [`specs/phase1-config-validation-design.md`](specs/phase1-config-validation-design.md) - Phase 1 design
- [`specs/phase2-secrets-management-design.md`](specs/phase2-secrets-management-design.md) - Phase 2 design

### Historical Documentation
- [`superpowers/`](superpowers/) - Historical specifications and plans
- [`superpowers/specs/`](superpowers/specs/) - Old design documents

## Test Coverage

```
113 tests passing (100%)
- Configuration: 15 tests
- Agent: 12 tests
- Memory: 20 tests
- API: 7 tests
- LLM: 5 tests
- Tools: 8 tests
- Plugins: 6 tests
- Skills: 5 tests
- MCP: 4 tests
- Integration: 31 tests
```

## Security Standards

- ✅ OWASP Top 10 (2021) - Configuration Security
- ✅ CWE-20 - Input Validation
- ✅ CWE-798 - Hard-coded Credentials (removed)
- ✅ CWE-522 - Insufficiently Protected Credentials
- ✅ Principle of Least Privilege
- ✅ Defense in Depth
- ✅ Fail Securely
- ✅ Secure by Default

---

**Last Updated:** 2026-06-07  
**Maintained By:** Project Team  
**For Questions:** See [AGENT_GUIDE.md](AGENT_GUIDE.md)