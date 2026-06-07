# Audit Record

**Audit date:** June 7, 2026
**Scope:** current idolhub runtime and memory baseline

## Verification Summary

| Check | Result |
|---|---|
| Full pytest suite | 67 passed, 13 warnings |
| Semgrep community rules | 0 findings across 22 tracked runtime files |
| pip-audit | 0 known dependency vulnerabilities |
| Ruff full-repo `F,I` checks | Passed |
| Bandit runtime scan | 0 high, 1 medium, 2 low |

## Commands

```bash
.venv/bin/pytest -q
.venv/bin/ruff check . --select F,I
.audit-tools/bin/bandit -r core memory tools api mcp_server -q
HOME=.audit-tools/home .audit-tools/bin/semgrep \
  --config auto --error core memory tools api mcp_server
.audit-tools/bin/pip-audit -r requirements.txt
```

## Accepted Bandit Findings

No Bandit finding is in the sqlite-vector memory changes.

| Location | Severity | Rationale |
|---|---|---|
| `tools/sandbox.py` tmpfs `/tmp` | Medium | Intentional ephemeral mount inside bubblewrap command construction |
| `tools/registry.py` subprocess import | Low | Required for bubblewrap execution; command uses `shell=False` |
| `tools/heartbeat.py` best-effort exception fallback | Low | Health metric falls back to zero |

These are accepted observations, not a statement that all future uses of these
patterns are safe.

## Runtime Coverage

The test suite covers:

- configuration resolution and provider credentials;
- Telegram, REST API, and MCP dispatch;
- skills, plugins, and tool filtering;
- sandbox boundaries and web search;
- prompt-injection filtering and memory-write gating;
- SQLite history, facts, preferences, FTS5 threading, and pruning;
- sqlite-vec initialization, ingestion, search, failure fallback, and optional
  dependency behavior;
- RRF fusion including semantic memory.

## Known Warnings

- PocketFlow emits a flow-end warning in agent tests.
- FastAPI TestClient emits a Starlette/httpx deprecation warning.
- `ruff format --check .` reports 31 legacy files requiring a dedicated
  formatting-only change.

Neither warning caused a test failure in this baseline. They remain maintenance
items and must not be represented as fixed.

## Configuration Security

`config.json` is local-only and ignored. `config.example.json` is the only
tracked template. Git history is rewritten as part of this documentation
baseline so no reachable repository commit contains `config.json`.
