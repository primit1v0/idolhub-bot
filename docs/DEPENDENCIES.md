# Dependency Decisions

The authoritative dependency declarations are `pyproject.toml` and `uv.lock`.

## Core

| Package | Purpose | Decision |
|---|---|---|
| `pocketflow` | Async agent graph | Small framework aligned with project architecture |
| `python-telegram-bot` | Telegram transport | Maintained async client |
| `openai` | OpenAI-compatible chat and embeddings | One client for configured compatible endpoints |
| `httpx` | HTTP requests and web-search tool | Existing async-capable client |
| `fastapi` | REST API | Typed ASGI API |
| `uvicorn` | ASGI server | Installed without heavy optional extras |
| `mcp` | MCP protocol | Official SDK |
| `aiosqlite` | Async SQLite access | Lightweight persistence |
| `pydantic` | Configuration validation | Shared with API stack |
| `pyyaml` | Skill frontmatter | Avoids ad hoc YAML parsing |

## Optional Extras

### `vector`

Installs `sqlite-vec`. It is required only when
`memory.long_term.backend = "sqlite_vec"`.

```bash
uv sync --extra vector
```

The module is lazy-loaded. Core and short-term memory remain importable without
the extra.

### `search`

Installs `duckduckgo-search`, but the current built-in `search_web` tool uses
`httpx` directly and does not require this extra. Keep the extra only for
experimentation or a future approved implementation.

## Development

The `dev` extra installs pytest, pytest-asyncio, and Ruff.

## Rejected Heavy Alternatives

| Package | Reason |
|---|---|
| `chromadb` | Large dependency graph for a use case handled by sqlite-vec |
| `faiss-cpu` | Native-heavy dependency unnecessary for local personal memory |
| `langchain` | Overlaps PocketFlow and local orchestration |
| `crewai` | Overlaps current agent architecture |
| `uvicorn[standard]` | Adds components not required by the current server |
| `python-dotenv` as direct dependency | Runtime uses process environment directly |

## Review Checklist

- Justification is documented here.
- `pyproject.toml` and `uv.lock` agree.
- Optional functionality is isolated behind an extra.
- No existing dependency already covers the requirement.
- Full tests and pip-audit pass.
