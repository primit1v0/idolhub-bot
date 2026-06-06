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
- **LLM**: OpenAI-compatible API, OpenAI Codex OAuth, GitHub Copilot CLI token

---

## 2. Lightweight Engineering Principles

> **Aturan utama: jika ada dua cara untuk menyelesaikan sesuatu, pilih yang lebih ringan.**

### 2.1 Zero Bloatware

- **Tidak ada dependency besar** tanpa alasan kuat yang terdokumentasi
- Setiap package di `pyproject.toml` wajib memiliki justifikasi di komentar
- Sebelum menambah package baru: cek apakah bisa pakai stdlib atau dependency yang sudah ada
- Semua heavy dependencies (vector DB, ML libs, dll) masuk `[optional-dependencies]` — tidak terinstall by default

### 2.2 Zero Dead Code

- Tidak ada fungsi/class/import yang tidak dipakai
- Tidak ada commented-out code yang di-commit
- Tidak ada `TODO` tanpa issue tracker reference
- Setiap file harus bisa dijustifikasi: hapus jika tidak ada yang memanggilnya

### 2.3 Pure & Minimal Code

- Setiap fungsi melakukan **satu hal** dengan jelas
- Tidak ada over-engineering atau abstraksi yang tidak diperlukan sekarang (YAGNI)
- Panjang file maksimal ~150 baris — jika lebih, pecah menjadi modul terpisah
- Type hints wajib di semua public API
- Docstring hanya untuk fungsi yang tidak self-explanatory dari nama + type hints

### 2.4 Dependency Audit (per Phase)

**Phase 1 — Core dependencies (total install ~30MB):**

| Package | Ukuran | Justifikasi |
|---|---|---|
| `pocketflow` | ~56KB | Core framework |
| `python-telegram-bot` | ~1MB | Telegram async handler |
| `openai` | ~1MB | OpenAI-compatible SDK |
| `httpx` | ~500KB | HTTP client untuk providers & tools |
| `fastapi` | ~300KB | REST API |
| `uvicorn` | ~200KB | ASGI server (plain, no extras) |
| `mcp` | ~500KB | MCP protocol SDK |
| `aiosqlite` | ~100KB | Async SQLite memory |
| `pydantic` | ~2MB | Data validation |
| `pyyaml` | ~200KB | Skill frontmatter parser |

**Dibuang / Optional:**

| Package | Alasan Dibuang | Alternatif |
|---|---|---|
| `chromadb` | 200MB+, C++ deps, onnxruntime | `sqlite-vec` (Phase 2, optional) |
| `pydantic-settings` | Overkill | Custom `$VAR` resolver (stdlib `os.environ`) |
| `uvicorn[standard]` | Tambah websockets, watchfiles, httptools | Plain `uvicorn` |
| `duckduckgo-search` | Bisa pakai `httpx` ke DDG JSON API langsung | Optional extra |

### 2.5 Aturan Menambah Dependency Baru

Sebelum `uv add X`, jawab semua pertanyaan ini:

1. Apakah bisa pakai stdlib Python? (`json`, `re`, `sqlite3`, `asyncio`, dll)
2. Apakah `httpx` atau dependency yang sudah ada bisa handle ini?
3. Berapa ukuran install package ini beserta transitive deps-nya?
4. Apakah ini benar-benar dibutuhkan sekarang, atau bisa defer ke phase berikutnya?

Jika tidak lulus minimal 2 pertanyaan → jangan tambah.

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
│   ├── idolhub.service.template      # systemd bot unit template
│   ├── idolhub-api.service.template  # systemd API unit template
│   └── idolhub-mcp.service.template  # systemd MCP unit template
├── scripts/
│   └── setup.sh                      # Setup helper (buat /etc/idolhub/)
│
├── core/
│   ├── bot.py                        # Telegram handler (python-telegram-bot)
│   ├── agent.py                      # PocketFlow agent flow (Async graph)
│   ├── llm.py                        # LLM abstraction layer (AsyncOpenAI client)
│   ├── config.py                     # $VAR resolver dari os.environ
│   └── event_bus.py                  # Hook/event bus system (Async/Sync)
│
├── providers/
│   └── __init__.py                   # Provider adapters resolved in core/llm.py
│
├── skills/                           # OpenClaw/Hermes-compatible skills
│   └── loader.py                     # Auto-discover and parse markdown skills
│
├── tools/
│   ├── registry.py                   # Tool registry + auto-discover
│   └── sandbox.py                    # Bubblewrap sandbox execution wrapper
│
├── plugins/
│   └── loader.py                     # Dynamic plugins auto-loader
│
├── memory/
│   └── sqlite_store.py               # Short-term: conversation history (SQLite)
│
├── api/
│   ├── server.py                     # FastAPI REST app
│   └── routes/
│       ├── chat.py                   # POST /chat
│       ├── health.py                 # GET /health
│       └── config.py                 # GET/POST /config
│
├── mcp_server/
│   └── server.py                     # FastMCP stdio server
│
└── dashboard/
    └── README.md                     # Placeholder WebUI (fase berikutnya)
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

### 3.3 Security & Sandboxing (bwrap)

`idolhub` memiliki kebijakan ketat terkait eksekusi *shell commands* yang dilakukan oleh agent, mengadopsi mekanisme *sandbox* dari [nanobot-ai](https://github.com/primit1v0/nanobot).

- **Default Workspace Only**: Agent hanya dapat bekerja, membaca, dan menulis di dalam folder `workspace` yang telah ditentukan. Agent tidak bisa keluar dari batasan ini.
- **Bubblewrap (bwrap) Enforcement**: Setiap perintah terminal yang dieksekusi oleh agent dibungkus ke dalam *ephemeral container* menggunakan `bwrap`.
- **Isolasi Konfigurasi**: `bwrap` akan melakukan *bind-mount* `tmpfs` kosong di atas direktori *parent* dari workspace. Artinya, meskipun agent mengeksekusi `ls ../`, mereka tidak akan melihat `config.json`, `/etc/idolhub/secrets.env`, atau konfigurasi bot lainnya.
- **Zero Configuration**: Fitur sandbox ini aktif secara default untuk semua eksekusi shell dan tidak bisa dimatikan via `config.json`.


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
    "openai_codex": {
      "oauth_token": "$OPENAI_CODEX_TOKEN",
      "base_url": "https://api.openai.com/v1"
    },
    "github_copilot": {
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
    "host": "127.0.0.1",
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

```env
# /etc/idolhub/idolhub.env
# chmod 600 — TIDAK pernah masuk git
TELEGRAM_BOT_TOKEN=xxxxx
OPENAI_API_KEY=sk-xxxxx
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_CODEX_TOKEN=xxxxx
GITHUB_COPILOT_TOKEN=xxxxx
```

---

## 5. LLM Providers

### 5.1 OpenAI-compatible (default)
- Standard OpenAI API format
- `base_url` configurable → bisa arahkan ke Ollama, LM Studio, dll
- `api_key` dari env

### 5.2 OpenAI Codex (OAuth)
- Autentikasi via OAuth token
- Endpoint: `https://api.openai.com/v1`
- Format response: OpenAI-compatible

### 5.3 GitHub Copilot (CLI token)
- Token dari `gh auth token` atau `~/.config/gh/hosts.yml`
- Endpoint: `https://api.githubcopilot.com`
- Format response: OpenAI-compatible

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

### Tambahan Perkembangan Memori (Deterministic Facts & FTS5)
Terinspirasi dari repositori `mrktt`, kami menambahkan arsitektur memori hibrida yang sangat ringan dan tanpa dependensi pihak ketiga:
- **Tabel Fakta (Deterministic EAV):** Menyimpan data faktual/preferensi pengguna dalam format `fakta(id, entity, nilai, confidence, source, created_at, updated_at)` dan `preferensi(kunci, nilai, updated_at)`.
- **FTS5 Indexing:** Menggunakan virtual table FTS5 bawaan SQLite untuk pencarian kata kunci pada memori jangka panjang tanpa memerlukan Vector DB.
- **Memory Gating & Safe Writes (`memory_gate.py`):** Menyaring penulisan fakta/preferensi ke memori agar terhindar dari *poisoning* dengan memeriksa kata kunci perintah berbahaya (`rm`, `execute`, `curl`, dll.) serta memicu penulisan memori hanya atas persetujuan atau instruksi eksplisit pengguna (misal: mengandung kata kunci `SIMPAN KE MEMORI`).
- **Prompt Injection & Input Gating (`rag_filter.py`):** Memvalidasi input pengguna sebelum dimasukkan ke dalam aliran pencarian memori guna mencegah serangan injeksi (seperti perintah `"ignore previous instructions"` atau `"lupakan semua instruksi"`).
- **Mini-RRF Rank Fusion Merger (`retriever.py`):** Algoritma perankingan dan penggabungan mini berbasis Reciprocal Rank Fusion (RRF) untuk menyatukan hasil pencarian memori kata kunci (FTS5) dan memori fakta (EAV) secara adil tanpa pustaka eksternal yang berat.

### Tambahan Fitur Heartbeat (Sistem Monitor)
Terinspirasi dari repositori `fortress-v2`, kami menambahkan utilitas monitoring server yang sangat ringan dan terintegrasi:
- **Zero-Dependency Monitor (`tools/heartbeat.py`):** Modul mandiri berbasis Python standar untuk mengumpulkan metrik sistem RAM (`/proc/meminfo`), CPU load (`/proc/loadavg`), dan penggunaan Disk (`os.statvfs`) secara lokal tanpa bergantung pada library eksternal `psutil`.
- **Integrasi Endpoint `/health`:** Memperluas API `/health` di [api/routes/health.py](file:///opt/idolhub/api/routes/health.py) untuk menyertakan metrik kesehatan sistem secara dinamis.

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

## 12. Tech Stack (Audited)

| Komponen | Library | Catatan |
|---|---|---|
| Framework | `pocketflow` | 100 lines, zero bloat |
| Telegram | `python-telegram-bot` | Async, standard |
| LLM | `openai` | OpenAI-compatible SDK |
| HTTP Client | `httpx` | Dipakai oleh providers & tools |
| API | `fastapi` + `uvicorn` | Plain uvicorn, no extras |
| MCP | `mcp` | Official SDK |
| Memory (short) | `aiosqlite` | Lightweight async SQLite |
| Memory (long) | `sqlite-vec` *(optional)* | Phase 2, ringan vs chromadb |
| Validation | `pydantic` | Minimal usage |
| Skills parser | `pyyaml` | Frontmatter only |
| Package manager | `uv` | 10-100x faster than pip |
| Deployment | `systemd` | Native, no Docker overhead |

> **Tidak ada**: chromadb, pydantic-settings, uvicorn[standard], atau paket besar lainnya di core install.
