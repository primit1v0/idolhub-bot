# Config Reference — idolhub

> **`config.json` adalah satu-satunya pintu konfigurasi seluruh sistem idolhub.**
>
> Tidak ada file konfigurasi lain. Tidak ada ENV yang di-hardcode di code. Tidak ada file persona eksternal.

---

## Prinsip

- **Satu file** — semua konfigurasi ada di `config.json`
- **Zero duplikat** — credentials LLM hanya di `providers[name]`, bukan juga di `llm`
- **Zero secrets** — semua `$VAR` di-resolve dari environment (inject via systemd)
- **Zero file persona** — system prompt ada di `agent.system_prompt`, bukan SOUL.md/AGENTS.md

---

## Alur Resolve Config

```
config.json ($VAR references)
      ↓
/etc/idolhub/secrets.env  (injected by systemd EnvironmentFile)
      ↓
core/config.py  (load JSON + resolve $VAR dari os.environ)
      ↓
Semua modul (core/, providers/, api/, mcp/, dll)
```

---

## Schema Lengkap

### `app` — Konfigurasi Aplikasi

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `app.name` | string | `"idolhub"` | Nama aplikasi (dipakai di logging) |
| `app.mode` | string | `"bot"` | Mode startup: `bot` \| `api` \| `mcp` |
| `app.debug` | bool | `false` | Aktifkan debug logging |
| `app.timezone` | string | `"Asia/Jakarta"` | Timezone untuk timestamp |

---

### `agent` — Konfigurasi Agent PocketFlow

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `agent.system_prompt` | string | *(lihat contoh)* | System prompt yang diinjeksi ke setiap LLM call |
| `agent.max_iterations` | int | `10` | Batas loop agent (cegah infinite loop) |
| `agent.tools_enabled` | bool | `true` | Aktifkan tool calling |
| `agent.memory_enabled` | bool | `true` | Aktifkan memory retrieval |

> **Catatan**: `agent.system_prompt` adalah satu-satunya tempat persona/instruksi agent.
> Tidak ada SOUL.md, AGENTS.md, atau file persona eksternal.

---

### `telegram` — Konfigurasi Bot Telegram

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `telegram.token` | string | `"$TELEGRAM_BOT_TOKEN"` | Bot token dari @BotFather |
| `telegram.allowed_users` | int[] | `[]` | Whitelist user ID. Kosong = semua boleh |
| `telegram.parse_mode` | string | `"Markdown"` | Format pesan: `Markdown` \| `MarkdownV2` \| `HTML` |

---

### `llm` — Parameter LLM (bukan credentials)

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `llm.provider` | string | `"openai"` | Provider aktif: `openai` \| `openai_codex` \| `github_copilot` |
| `llm.model` | string | `"gpt-4o"` | Nama model yang dipakai |
| `llm.temperature` | float | `0.7` | Kreativitas output (0.0 = deterministik) |
| `llm.max_tokens` | int | `4096` | Batas token per response |
| `llm.timeout` | int | `30` | Timeout HTTP request (detik) |

> **Penting**: Credentials (api_key, base_url, token) ada di `providers`, **bukan** di sini.
> `llm.provider` adalah selector — sistem akan baca `providers[llm.provider]` untuk credentials.

---

### `providers` — Credentials Per Provider

Hanya provider yang dipilih di `llm.provider` yang aktif. Sisanya diabaikan.

#### `providers.openai`

| Key | Type | Keterangan |
|---|---|---|
| `base_url` | string | Endpoint API. Bisa custom untuk Ollama, LM Studio, dll |
| `api_key` | string | API key (`$OPENAI_API_KEY`) |

#### `providers.openai_codex`

| Key | Type | Keterangan |
|---|---|---|
| `base_url` | string | `https://api.openai.com/v1` |
| `oauth_token` | string | OpenAI Codex OAuth token (`$OPENAI_CODEX_TOKEN`) |

#### `providers.github_copilot`

| Key | Type | Keterangan |
|---|---|---|
| `base_url` | string | `https://api.githubcopilot.com` |
| `cli_token` | string | Token dari `gh auth token` atau OAuth (`$GITHUB_COPILOT_TOKEN`) |

---

### `memory` — Konfigurasi Memory

#### `memory.short_term`

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `backend` | string | `"sqlite"` | Backend: `sqlite` |
| `path` | string | `"./data/memory.db"` | Path file SQLite |
| `max_messages` | int | `50` | Max pesan yang dimuat untuk konteks aktif percakapan |
| `fts_context_window` | int | `2` | Jumlah pesan sebelum/sesudah pesan FTS5 yang ikut diambil sebagai utas konteks |
| `auto_prune_enabled` | bool | `true` | Mengaktifkan pembersihan otomatis (auto-pruning) untuk histori lama |
| `auto_prune_limit` | int | `1000` | Batas maksimum jumlah pesan yang disimpan di DB sebelum dipotong |

#### `memory.long_term`

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `backend` | string | `"none"` | Backend: `none` \| `sqlite_vec` *(Phase 2)* |
| `path` | string | `"./data/vectors.db"` | Path file vector DB |
| `embedding_model` | string | `"text-embedding-3-small"` | Model embedding OpenAI-compatible untuk semantic search |

> **Phase 1**: `long_term.backend = "none"` — tidak ada vector memory.
> **Phase 2**: Ganti ke `"sqlite_vec"` + `uv sync --extra vector`. Vector memory menggunakan ekstensi SQLite `sqlite-vec` yang ringan untuk pemrosesan semantik lokal di dalam file database yang sama atau terpisah.

---

### `skills` — Skill System

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `skills.dir` | string | `"./skills"` | Folder skill definitions (`.md` files) |
| `skills.enabled` | string[] | `[]` | Kosong = semua aktif. Isi untuk whitelist |

---

### `tools` — Tool Registry

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `tools.dir` | string | `"./tools"` | Folder tool implementations (`.py` files) |
| `tools.enabled` | string[] | `[]` | Kosong = semua aktif. Isi untuk whitelist |

---

### `plugins` — Plugin/Hook System

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `plugins.dir` | string | `"./plugins"` | Folder plugin files (`.py` files) |
| `plugins.enabled` | string[] | `[]` | Kosong = semua aktif. Isi untuk whitelist |

---

### `api` — FastAPI REST Server

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `api.enabled` | bool | `true` | Aktifkan REST API |
| `api.host` | string | `"127.0.0.1"` | Bind host |
| `api.port` | int | `8000` | Port |
| `api.cors_origins` | string[] | `[]` | Allowed origins. Kosong = tidak ada CORS |

---

### `mcp` — MCP Protocol Server

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `mcp.enabled` | bool | `true` | Aktifkan MCP server |
| `mcp.port` | int | `8001` | Port MCP server |

---

### `logging` — Logging

| Key | Type | Default | Keterangan |
|---|---|---|---|
| `logging.level` | string | `"INFO"` | Level: `DEBUG` \| `INFO` \| `WARNING` \| `ERROR` |
| `logging.format` | string | `"text"` | Format: `text` \| `json` |

> Output ke stdout — ditangkap `journald` saat production via systemd.

---

## Contoh Konfigurasi

### Ganti provider ke Ollama (local)

```json
{
  "llm": {
    "provider": "openai",
    "model": "llama3.2"
  },
  "providers": {
    "openai": {
      "base_url": "http://localhost:11434/v1",
      "api_key": "ollama"
    }
  }
}
```

### Aktifkan whitelist user Telegram

```json
{
  "telegram": {
    "allowed_users": [123456789, 987654321]
  }
}
```

### Aktifkan long-term memory (Phase 2)

```json
{
  "memory": {
    "long_term": {
      "backend": "sqlite_vec",
      "path": "./data/vectors.db"
    }
  }
}
```

### Hanya aktifkan skill tertentu

```json
{
  "skills": {
    "enabled": ["web_search", "summarize"]
  }
}
```

---

## Cara `core/config.py` Bekerja

```python
# Pseudocode — implementasi ada di core/config.py
import json, os, re

def resolve_env(value):
    """Resolve $VAR_NAME dari os.environ"""
    return re.sub(r'\$([A-Z_][A-Z0-9_]*)',
                  lambda m: os.environ[m.group(1)], str(value))

# Load config.json
# Resolve semua $VAR secara rekursif
# Return typed Config object (Pydantic model)
```

Tidak ada `load_dotenv()`. Tidak ada `.env` file. Murni dari environment yang sudah di-inject systemd.
