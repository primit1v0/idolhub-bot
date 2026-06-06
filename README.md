# idolhub

> Personal assistant berbasis [PocketFlow](https://github.com/The-Pocket/PocketFlow) — Telegram Bot + REST API + MCP Server

[![Private](https://img.shields.io/badge/repo-private-red)](https://github.com/primit1v0/idolhub-bot)

## Features

- 🤖 **Telegram Bot** — chat natural, search web, jalankan tools
- 🧠 **Dual Memory** — short-term (SQLite) + long-term (ChromaDB vector)
- 🔌 **Plugin-First** — skill, tool, plugin bisa di-inject tanpa ubah core
- 📡 **REST API** — FastAPI endpoint untuk integrasi eksternal
- 🔁 **MCP Server** — compatible dengan Claude Desktop, Cursor, dll
- 🔐 **Secrets aman** — tidak pernah ada di folder project, inject via systemd

## Quick Start

```bash
# 1. Clone dan setup
git clone https://github.com/primit1v0/idolhub-bot.git
cd idolhub-bot

# 2. Install uv (jika belum ada)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Setup environment dan dependencies
sudo bash scripts/setup.sh

# 4. Edit secrets
sudo nano /etc/idolhub/secrets.env

# 5. Jalankan (development)
uv run python main.py

# 6. Jalankan (production via systemd)
sudo systemctl enable --now idolhub
```

## Structure

```
idolhub/
├── core/          # Engine (bot, agent, memory, llm, config, event_bus)
├── providers/     # LLM providers (openai, codex, copilot)
├── skills/        # OpenClaw/Hermes-compatible skill definitions (.md)
├── tools/         # Tool implementations (auto-discovered)
├── plugins/       # Hook/plugin system (auto-loaded)
├── memory/        # SQLite + ChromaDB backends
├── api/           # FastAPI REST endpoints
├── mcp/           # MCP server
├── systemd/       # systemd service template
└── scripts/       # Setup helpers
```

## Configuration

Config via `config.json` dengan `$VAR` interpolation dari environment:

```json
{
  "llm": {
    "provider": "openai",
    "api_key": "$OPENAI_API_KEY"
  }
}
```

Secrets di-inject via systemd `EnvironmentFile=/etc/idolhub/secrets.env` — **tidak pernah ada `.env` di dalam project**.

## Inject Skill Baru

Drop file `.md` ke folder `skills/`:

```markdown
---
name: my_skill
description: What this skill does
parameters:
  input:
    type: string
    required: true
---
## Instructions
...
```

## Inject Tool Baru

Drop file `.py` ke folder `tools/`:

```python
from tools.registry import tool

@tool(name="my_tool", description="Does something useful")
def my_tool(input: str) -> str:
    return f"Result: {input}"
```

## Inject Plugin/Hook

Drop file `.py` ke folder `plugins/`:

```python
class MyPlugin:
    def before_message(self, ctx): ...
    def after_reply(self, ctx): ...
```

## Design Spec

Lihat [docs/superpowers/specs/2026-06-06-idolhub-design.md](docs/superpowers/specs/2026-06-06-idolhub-design.md)

## License

Private — All rights reserved
