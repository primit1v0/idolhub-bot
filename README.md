# idolhub

> **Lightweight personal assistant** — PocketFlow · Telegram · REST API · MCP
>
> Zero bloat. Pure code. Plugin-first.

[![Private](https://img.shields.io/badge/repo-private-red)](https://github.com/primit1v0/idolhub-bot)
[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://python.org)
[![uv](https://img.shields.io/badge/package--manager-uv-purple)](https://docs.astral.sh/uv/)
[![PocketFlow](https://img.shields.io/badge/framework-PocketFlow-orange)](https://github.com/The-Pocket/PocketFlow)

---

## Filosofi

> **Jika ada dua cara untuk menyelesaikan sesuatu, pilih yang lebih ringan.**

- **Zero bloatware** — setiap dependency harus terjustifikasi, heavy deps masuk `[optional]`
- **Zero dead code** — tidak ada import, fungsi, atau class yang tidak dipakai
- **Pure & minimal** — satu fungsi, satu tujuan. Max ~150 baris per file
- **No `.env` in project** — secrets di-inject via systemd `EnvironmentFile`

---

## Features

| | Fitur | Keterangan |
|---|---|---|
| 🤖 | **Telegram Bot** | Chat natural, search web, jalankan tools |
| 🧠 | **Dual Memory (RRF)** | SQLite history (Jaccard deduplicated) + EAV Facts & Preference Store, terintegrasi via Reciprocal Rank Fusion (RRF) |
| 🛡️ | **Gating & Security** | Prompt Injection Filter (RAG Filter) + Memory Gating (Safe Writes) untuk keamanan memori |
| 🔌 | **Plugin-First** | Skill/tool/plugin di-drop ke folder, auto-loaded tanpa ubah core |
| 📡 | **REST API** | FastAPI endpoint dengan integrasi dynamic resource heartbeat monitor |
| 🔁 | **MCP Server** | Compatible dengan Claude Desktop, Cursor, Windsurf |
| 🔐 | **Secrets Aman** | Tidak pernah ada di folder project — inject via systemd |
| ⚡ | **LLM Providers** | OpenAI-compatible, Gemini/Gemma, GitHub Codex OAuth, GitHub Copilot CLI |

---

## Tech Stack (Audited)

| Komponen | Library | Ukuran |
|---|---|---|
| Framework | `pocketflow` | ~56KB |
| Telegram | `python-telegram-bot` | ~1MB |
| LLM | `openai` SDK | ~1MB |
| HTTP | `httpx` | ~500KB |
| API | `fastapi` + `uvicorn` | ~500KB |
| MCP | `mcp` SDK | ~500KB |
| Memory | `aiosqlite` | ~100KB |
| Validation | `pydantic` | ~2MB |
| Skills parser | `pyyaml` | ~200KB |
| **Total core** | | **~30MB install** |

**Tidak ada**: `chromadb`, `langchain`, `crewai`, atau framework besar lainnya.

---

## Quick Start

### Prerequisites

```bash
# Install uv (jika belum ada)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Setup

```bash
# 1. Clone
git clone https://github.com/primit1v0/idolhub-bot.git
cd idolhub-bot

# 2. Setup: buat /etc/idolhub/secrets.env + install systemd service
sudo bash scripts/setup.sh

# 3. Isi secrets (WAJIB — tidak ada .env di project)
sudo nano /etc/idolhub/secrets.env

# 4. Install dependencies
uv sync

# 5. Jalankan (development)
uv run python main.py bot

# 6. Production via systemd
sudo systemctl enable --now idolhub
journalctl -u idolhub -f
```

### Mode Operasi

```bash
uv run python main.py bot    # Telegram bot (default)
uv run python main.py api    # FastAPI REST server (port 8000)
uv run python main.py mcp    # MCP server (port 8001)
```

---

## Project Structure

```
idolhub/
│
├── main.py                   # Entry point: bot | api | mcp
├── config.json               # $VAR references only — aman di git
├── config.example.json       # Template: copy + isi di secrets.env
├── pyproject.toml            # uv dependencies (audited, no bloat)
│
├── core/                     # Engine — stabil, jarang disentuh
│   ├── bot.py                # Telegram handler
│   ├── agent.py              # PocketFlow agent flow (RRF context injection)
│   ├── memory.py             # Memory manager (short + long term)
│   ├── llm.py                # LLM abstraction layer
│   ├── config.py             # $VAR resolver (stdlib os.environ)
│   ├── event_bus.py          # Hook/event lifecycle system
│   └── rag_filter.py         # Prompt injection filter (regex word boundaries)
│
├── providers/                # LLM provider adapters (swap via config)
│   ├── openai_provider.py    # OpenAI / OpenAI-compatible
│   ├── codex_provider.py     # GitHub Codex via OAuth
│   └── copilot_provider.py   # GitHub Copilot via CLI token
│
├── skills/                   # OpenClaw/Hermes-compatible (.md)
├── tools/                    # Tool implementations (.py, auto-discovered)
│   └── heartbeat.py          # Zero-dependency system resource monitor
│
├── plugins/                  # Hooks & plugins (.py, auto-loaded)
│
├── memory/
│   ├── sqlite_store.py       # SQLite store: conversation history & EAV facts
│   ├── memory_gate.py        # Memory gating validation (explicit consent)
│   └── vector_store.py       # Long-term: sqlite-vec [optional, Phase 2]
│
├── api/                      # FastAPI REST
│   └── routes/               # chat · health · config
│
├── mcp/                      # MCP protocol server
├── systemd/                  # Service template
├── scripts/                  # Setup helpers
└── dashboard/                # WebUI [Phase 3]
```

---

## Configuration

`config.json` hanya berisi referensi `$VAR` — **tidak ada nilai secret**:

```json
{
  "llm": {
    "provider": "openai",
    "base_url": "$OPENAI_BASE_URL",
    "api_key": "$OPENAI_API_KEY",
    "model": "gpt-4o"
  }
}
```

Semua `$VAR` di-resolve dari environment yang di-inject systemd:

```ini
# /etc/systemd/system/idolhub.service
EnvironmentFile=/etc/idolhub/secrets.env   # ← di luar project
```

Lihat [`config.example.json`](config.example.json) untuk daftar semua key yang dibutuhkan.

---

## Inject Skill Baru

Drop file `.md` ke `skills/` — auto-loaded saat startup:

```markdown
---
name: my_skill
description: Apa yang skill ini lakukan
parameters:
  query:
    type: string
    description: Input query
    required: true
---

## Instructions
Langkah-langkah yang harus dilakukan agent...
```

Format kompatibel dengan **OpenClaw / Hermes** skill definitions.

---

## Inject Tool Baru

Drop file `.py` ke `tools/` — auto-discovered via registry:

```python
from tools.registry import tool

@tool(name="my_tool", description="Does something useful")
def my_tool(query: str) -> str:
    return f"result: {query}"
```

---

## Inject Plugin / Hook

Drop file `.py` ke `plugins/` — auto-loaded, lifecycle hooks:

```python
class MyPlugin:
    def before_message(self, ctx: dict) -> None: ...
    def after_reply(self, ctx: dict) -> None: ...
    def on_error(self, ctx: dict) -> None: ...
```

Hook yang tersedia: `before_message`, `after_message`, `before_reply`, `after_reply`, `on_error`, `on_tool_call`

---

## Dependency Rules

Sebelum `uv add X`, jawab semua ini:

1. Apakah bisa pakai **stdlib Python**? (`json`, `re`, `sqlite3`, `asyncio`, ...)
2. Apakah **`httpx`** atau dep yang sudah ada bisa handle ini?
3. Berapa **ukuran install** package ini + transitive deps?
4. Apakah benar-benar dibutuhkan **sekarang**, atau bisa defer ke phase berikutnya?

Jika tidak lulus minimal 2 → jangan tambah.

---

## Roadmap

| Phase | Status | Scope |
|---|---|---|
| **Phase 1** | ✅ Completed | Core bot · agent · memory · providers · skill/tool/plugin system |
| **Phase 2** | ✅ Completed | FastAPI REST · MCP server · SQLite EAV memory (Jaccard, FTS5, RRF) · Heartbeat monitor & Security Gating |
| **Phase 3** | 📋 Planned | WebUI Dashboard (config + monitoring) |
| **Phase 4** | 💡 Future | Voice · advanced RAG · sqlite-vec long-term memory |

---

## Docs

- [Design Spec](docs/superpowers/specs/2026-06-06-idolhub-design.md)
- [Contributing](docs/CONTRIBUTING.md)
- [Dependencies](docs/DEPENDENCIES.md)

---

## License

Private — All rights reserved
