# idolhub — Design Specification

**Date:** 2026-06-06  
**Repo:** https://github.com/primit1v0/idolhub-bot  
**Status:** Approved ✅

---

## 1. Overview

**idolhub** adalah personal assistant berbasis [PocketFlow](https://github.com/The-Pocket/PocketFlow) dengan:

- **Transport layer**: Telegram Bot (primary interface)
- **Backend API**: FastAPI REST (secondary interface)
- **Protocol**: MCP (Model Context Protocol) server
- **Architecture**: Plugin-first — skill, tool, plugin bisa di-inject tanpa ubah core
- **LLM**: OpenAI-compatible API, GitHub Codex OAuth, GitHub Copilot CLI token

---

## 2. Goals

- Personal assistant yang bisa chat, search web, dan jalankan tools via Telegram
- Memory persisten: short-term (SQLite) + long-term (ChromaDB vector)
- Skill system kompatibel dengan format OpenClaw/Hermes (markdown-based)
- Plugin/hook injection via event bus (before_message, after_reply, dll)
- Config via `config.json` dengan `$VAR` interpolation dari environment
- Secrets TIDAK pernah ada di dalam project folder — inject via systemd `EnvironmentFile`
- Dashboard WebUI (fase berikutnya)

---

## 3. Architecture

### 3.1 Plugin-First Architecture

```
idolhub/
├── main.py                     # Entry point (bot / api / mcp mode)
├── config.json                 # $VAR references only — aman di git
├── config.example.json         # Template lengkap semua key
├── pyproject.toml              # uv project config
├── uv.lock                     # Di-commit — reproducible builds
├── .gitignore
│
├── systemd/
│   └── idolhub.service.template  # systemd unit template
├── scripts/
│   └── setup.sh                  # Setup helper (buat /etc/idolhub/)
│
├── core/
│   ├── bot.py                  # Telegram handler (python-telegram-bot)
│   ├── agent.py                # PocketFlow agent flow
│   ├── memory.py               # Memory manager (short + long term)
│   ├── llm.py                  # LLM abstraction layer
│   ├── config.py               # $VAR resolver dari os.environ
│   └── event_bus.py            # Hook/event system
│
├── providers/
│   ├── openai_provider.py      # OpenAI / OpenAI-compatible
│   ├── codex_provider.py       # GitHub Codex via OAuth
│   └── copilot_provider.py     # GitHub Copilot via CLI auth token
│
├── skills/                     # OpenClaw/Hermes-compatible skills
│   ├── loader.py               # Auto-discover skills dari folder
│   ├── web_search.md
│   └── summarize.md
│
├── tools/
│   ├── registry.py             # Tool registry + auto-discover
│   ├── search.py               # DuckDuckGo / Serper
│   └── calculator.py
│
├── plugins/
│   ├── loader.py               # Plugin auto-loader
│   └── logger.py               # Log semua interaksi
│
├── memory/
│   ├── sqlite_store.py         # Short-term: conversation history
│   └── vector_store.py         # Long-term: ChromaDB semantic memory
│
├── api/
│   ├── server.py               # FastAPI app
│   └── routes/
│       ├── chat.py             # POST /chat
│       ├── health.py           # GET /health
│       └── config.py           # GET/POST /config
│
├── mcp/
│   ├── server.py               # MCP-compliant server
│   └── handlers.py             # Tool handlers via MCP protocol
│
└── dashboard/
    └── README.md               # Placeholder WebUI (fase berikutnya)
```

### 3.2 Data Flow

```
Telegram Message
      ↓
  core/bot.py ──→ event_bus.emit("before_message")
      ↓
  core/agent.py (PocketFlow Flow)
    ├── DecideAction Node  ──→ core/llm.py ──→ providers/[aktif]
    ├── UseTool Node       ──→ tools/registry.py ──→ tool.exec()
    ├── SearchMemory Node  ──→ memory/vector_store.py
    └── AnswerNode         ──→ event_bus.emit("before_reply")
      ↓
  Telegram Reply
      ↓
  memory/ (save conversation)
      ↓
  event_bus.emit("after_reply")

Paralel:
  api/    ←── HTTP clients (REST)
  mcp/    ←── MCP clients (Claude Desktop, Cursor, dll)
```

---

## 4. Configuration

### 4.1 `config.json` (aman di git — hanya $VAR)

```json
{
  "app": {
    "name": "idolhub",
    "mode": "bot"
  },
  "telegram": {
    "token": "$TELEGRAM_BOT_TOKEN"
  },
  "llm": {
    "provider": "openai",
    "base_url": "$OPENAI_BASE_URL",
    "api_key": "$OPENAI_API_KEY",
    "model": "gpt-4o",
    "temperature": 0.7,
    "max_tokens": 4096
  },
  "providers": {
    "codex": {
      "oauth_token": "$GITHUB_CODEX_TOKEN",
      "base_url": "https://api.githubcopilot.com"
    },
    "copilot": {
      "cli_token": "$GITHUB_COPILOT_TOKEN",
      "base_url": "https://api.githubcopilot.com"
    }
  },
  "memory": {
    "short_term": "sqlite",
    "long_term": "chroma",
    "sqlite_path": "./data/memory.db",
    "chroma_path": "./data/chroma",
    "max_history": 50
  },
  "api": {
    "enabled": true,
    "host": "0.0.0.0",
    "port": 8000
  },
  "mcp": {
    "enabled": true,
    "port": 8001
  },
  "skills_dir": "./skills",
  "tools_dir": "./tools",
  "plugins_dir": "./plugins"
}
```

### 4.2 Secrets — `/etc/idolhub/secrets.env`

```bash
# /etc/idolhub/secrets.env
# chmod 600 — TIDAK pernah masuk git
TELEGRAM_BOT_TOKEN=xxxxx
OPENAI_API_KEY=sk-xxxxx
OPENAI_BASE_URL=https://api.openai.com/v1
GITHUB_CODEX_TOKEN=xxxxx
GITHUB_COPILOT_TOKEN=xxxxx
```

---

## 5. LLM Providers

### 5.1 OpenAI-compatible (default)
- Standard OpenAI API format
- `base_url` configurable → bisa arahkan ke Ollama, LM Studio, dll
- `api_key` dari env

### 5.2 GitHub Codex (OAuth)
- Autentikasi via OAuth token
- Endpoint: `https://api.githubcopilot.com`
- Format response: OpenAI-compatible

### 5.3 GitHub Copilot (CLI token)
- Token dari `gh auth token` atau `~/.config/gh/hosts.yml`
- Endpoint sama dengan Codex
- Fallback jika Codex tidak tersedia

**Provider swap** via `config.json → llm.provider` tanpa ubah code.

---

## 6. Skill System (OpenClaw/Hermes-compatible)

Skill didefinisikan sebagai **markdown file** dengan YAML frontmatter:

```markdown
---
name: web_search
description: Search the web for current information
parameters:
  query:
    type: string
    description: Search query
    required: true
---

## Instructions
Search the web using the provided query and return relevant results...
```

`skills/loader.py` auto-discover semua `.md` file di `skills_dir`, parse frontmatter, dan register ke agent sebagai callable tool.

---

## 7. Plugin/Hook System

Event bus dengan lifecycle hooks:

| Event | Trigger |
|---|---|
| `before_message` | Sebelum pesan diproses agent |
| `after_message` | Setelah pesan diterima, sebelum LLM call |
| `before_reply` | Sebelum balasan dikirim ke Telegram |
| `after_reply` | Setelah balasan terkirim |
| `on_error` | Saat terjadi error di flow mana pun |
| `on_tool_call` | Setiap kali agent memanggil sebuah tool |

Plugin adalah Python class dengan method yang match nama event:

```python
class MyPlugin:
    def before_message(self, ctx): ...
    def after_reply(self, ctx): ...
```

Drop ke `plugins/` folder → auto-loaded saat startup.

---

## 8. Memory Architecture

### Short-term (SQLite)
- Conversation history per user
- Max N messages (configurable, default 50)
- Persistent across restarts

### Long-term (ChromaDB)
- Vector embedding dari conversation penting
- Semantic search: agent bisa recall info relevan dari history jauh
- Embedding model: text-embedding-3-small (OpenAI) atau lokal

---

## 9. API & MCP

### REST API (FastAPI)
| Endpoint | Method | Description |
|---|---|---|
| `/health` | GET | Status check |
| `/chat` | POST | Query agent via HTTP |
| `/config` | GET | Baca config aktif |
| `/config` | POST | Update config (runtime) |

### MCP Server
- Expose tools via MCP protocol
- Bisa dipakai oleh: Claude Desktop, Cursor, Windsurf, dll
- Tools yang di-expose: semua yang ada di `tools/registry.py`

---

## 10. Deployment (systemd)

```ini
# /etc/systemd/system/idolhub.service
[Unit]
Description=idolhub Personal Assistant
After=network.target

[Service]
Type=simple
User=sandi
WorkingDirectory=/opt/idolhub
EnvironmentFile=/etc/idolhub/secrets.env
ExecStart=/opt/idolhub/.venv/bin/python main.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

---

## 11. Phase Plan

| Phase | Scope |
|---|---|
| **Phase 1 (sekarang)** | Core bot, agent, memory, providers, skill loader, tool registry, plugin system |
| **Phase 2** | FastAPI REST + MCP server |
| **Phase 3** | WebUI Dashboard (config + monitoring) |
| **Phase 4** | Advanced: voice, RAG, multi-agent |

---

## 12. Tech Stack

| Komponen | Library |
|---|---|
| Framework | PocketFlow |
| Telegram | python-telegram-bot |
| LLM | openai (SDK) |
| API | FastAPI + uvicorn |
| MCP | mcp (official SDK) |
| Memory (short) | aiosqlite |
| Memory (long) | chromadb |
| Config | pydantic-settings |
| Package manager | uv |
| Deployment | systemd |
