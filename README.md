# idolhub

Lightweight personal assistant built with PocketFlow, Telegram, FastAPI, and
MCP. The project favors small dependencies, explicit configuration, and local
SQLite storage.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://python.org)
[![uv](https://img.shields.io/badge/package%20manager-uv-purple)](https://docs.astral.sh/uv/)
[![PocketFlow](https://img.shields.io/badge/framework-PocketFlow-orange)](https://github.com/The-Pocket/PocketFlow)

## Current Status

The current baseline is implemented and covered by 67 tests:

- Telegram bot, REST API, and MCP stdio modes.
- OpenAI-compatible provider selection.
- Tool, skill, and plugin extension points.
- SQLite history, EAV facts/preferences, FTS5 threading, and pruning.
- Optional sqlite-vec semantic memory.
- RRF context fusion across facts, FTS5, and semantic results.
- Prompt-injection filtering, memory-write gating, and bubblewrap sandboxing.

See [Current Baseline](docs/BASELINE.md) for the authoritative feature and
configuration status. Start a new work session from
[Next Phase](docs/NEXT_PHASE.md).

## Configuration Policy

`config.example.json` is tracked. `config.json` is local-only and ignored by
Git.

```bash
cp config.example.json config.json
```

Edit local `config.json` to select one provider. Secrets remain outside the
repository and are supplied through environment variables. Every `$VARIABLE`
left in local `config.json` must exist in the environment.

Never commit:

- `config.json`
- `.env` or other secret files
- `data/` databases
- logs
- `workspace/` contents

## Quick Start

```bash
git clone https://github.com/primit1v0/idolhub-bot.git
cd idolhub-bot

cp config.example.json config.json
uv sync

export TELEGRAM_BOT_TOKEN="..."
export GEMINI_API_KEY="..."

uv run python main.py bot
```

Install the optional vector extension when local semantic memory is enabled:

```bash
uv sync --extra vector
```

Then set `memory.long_term.backend` to `sqlite_vec` in local `config.json`.

## Modes

```bash
uv run python main.py bot
uv run python main.py api
uv run python main.py mcp
```

CLI mode overrides `app.mode`. MCP currently uses stdio transport; `mcp.port`
is not used.

## Project Structure

```text
idolhub/
├── main.py
├── config.example.json
├── pyproject.toml
├── core/
│   ├── agent.py
│   ├── bot.py
│   ├── config.py
│   ├── event_bus.py
│   ├── llm.py
│   └── rag_filter.py
├── memory/
│   ├── memory_gate.py
│   └── sqlite_store.py
├── api/
│   ├── server.py
│   └── routes/
├── mcp_server/
│   └── server.py
├── skills/
│   └── loader.py
├── plugins/
│   └── loader.py
├── tools/
│   ├── heartbeat.py
│   ├── registry.py
│   └── sandbox.py
├── systemd/
├── tests/
├── docs/
└── dashboard/
```

## Extension Points

### Skills

Markdown files in `skills.dir` are discovered automatically. They require YAML
frontmatter containing `name`, `description`, and optional parameters.

### Plugins

Python classes in `plugins.dir` are instantiated automatically. Supported hook
methods are:

`before_message`, `after_message`, `before_reply`, `after_reply`, `on_error`,
and `on_tool_call`.

### Tools

Built-in tools are registered explicitly in `tools/registry.py`. Adding a tool
requires:

1. implementing the function;
2. adding its OpenAI-compatible schema to `TOOLS_SCHEMA`;
3. adding the function to `TOOLS_MAPPING`;
4. adding tests.

`tools.dir` is currently schema-only and is not auto-discovered.

## Production Notes

Systemd templates under `systemd/` use `@IDOLHUB_*@` placeholders.
`scripts/setup.sh` renders the bot service with the target user, repository
directory, and machine-local environment file. Secrets remain outside the
repository.

## Documentation

- [Current baseline](docs/BASELINE.md)
- [Next phase handoff](docs/NEXT_PHASE.md)
- [Active specifications](docs/specs/)
- [Configuration reference](docs/CONFIG.md)
- [Dependency decisions](docs/DEPENDENCIES.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Latest audit](hasilaudit.md)
- [Historical specs and plans](docs/superpowers/)

## Roadmap

| Status | Scope |
|---|---|
| Implemented | Core runtime, APIs, extension systems, security controls, and memory stack |
| Proposed | Foundation hardening listed in the active 39-point specification |
| Deferred | Dashboard WebUI |
| Not scheduled | Voice, multi-agent orchestration, additional RAG backends |

## License

All rights reserved.
