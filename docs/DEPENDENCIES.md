# Dependency Decisions — idolhub

> Setiap dependency harus terjustifikasi. Dokumen ini adalah catatan keputusan.

---

## Core Dependencies (Phase 1)

### `pocketflow`
- **Alasan**: Core framework, 100 baris, zero external dependencies
- **Alternatif yang ditolak**: LangChain (+166MB), CrewAI (+173MB), LangGraph (+51MB)

### `python-telegram-bot`
- **Alasan**: Async handler Telegram yang stabil, widely used, maintained
- **Alternatif yang dipertimbangkan**: `aiogram` (lebih ringan tapi less stable), raw `httpx` calls (lebih banyak boilerplate)
- **Catatan**: Gunakan tanpa extras `[all]`

### `openai`
- **Alasan**: OpenAI-compatible SDK — support custom `base_url` untuk semua provider
- **Alternatif**: `httpx` langsung — bisa, tapi SDK handle retry, streaming, error parsing
- **Catatan**: Satu SDK untuk OpenAI, Codex, Copilot, Ollama, LM Studio

### `httpx`
- **Alasan**: Async HTTP client modern, dipakai oleh openai + python-telegram-bot sebagai transitive dep
- **Alternatif yang ditolak**: `requests` (sync only), `aiohttp` (sudah punya httpx)

### `fastapi`
- **Alasan**: Lightweight, type-safe, auto-docs, minimal overhead
- **Alternatif yang ditolak**: Flask (sync), Django (overkill), Starlette (terlalu low-level)

### `uvicorn`
- **Alasan**: ASGI server minimal untuk FastAPI
- **Catatan**: Plain `uvicorn`, bukan `uvicorn[standard]` — tidak butuh websockets/httptools/watchfiles

### `mcp`
- **Alasan**: Official MCP SDK — required untuk MCP protocol compliance
- **Catatan**: Pulls `pydantic-settings` sebagai transitive dep (kita tidak import langsung)

### `aiosqlite`
- **Alasan**: Async wrapper SQLite untuk short-term memory
- **Ukuran**: ~100KB, zero C++ deps
- **Alternatif yang ditolak**: `databases` (overkill), raw `sqlite3` (sync only)

### `pydantic`
- **Alasan**: Type validation untuk config dan data models
- **Catatan**: Dipakai juga oleh fastapi dan mcp sebagai transitive dep

### `pyyaml`
- **Alasan**: Parse YAML frontmatter di skill definitions (`.md` files)
- **Alternatif**: `python-frontmatter` (adds another dep), manual regex (error-prone)

---

## Optional Dependencies

### `sqlite-vec` *(extras: vector)*
- **Alasan**: SQLite extension untuk vector similarity search — ringan vs chromadb
- **Kapan diinstall**: Phase 2, saat long-term memory diaktifkan
- **Alternatif yang ditolak**: `chromadb` (200MB+, C++ deps, onnxruntime), `faiss-cpu` (C++ heavy)
- **Install**: `uv sync --extra vector`

### `duckduckgo-search` *(extras: search)*
- **Alasan**: Web search tool untuk agent
- **Catatan**: Bisa diganti dengan `httpx` langsung ke DDG Lite JSON endpoint
- **Install**: `uv sync --extra search`

---

## Dependencies yang Ditolak

| Package | Ukuran | Alasan Ditolak |
|---|---|---|
| `chromadb` | ~200MB+ | C++ deps, onnxruntime, numpy — jauh lebih berat dari `sqlite-vec` |
| `pydantic-settings` | ~1MB | Overkill — kita pakai `os.environ` + custom `$VAR` resolver |
| `uvicorn[standard]` | +extras | Tambah websockets, httptools, watchfiles yang tidak diperlukan |
| `langchain` | ~100MB+ | Framework alternatif — tidak dipakai, sudah ada PocketFlow |
| `crewai` | ~173MB | Framework alternatif — tidak dipakai |
| `requests` | ~300KB | Sync-only, sudah ada `httpx` |
| `aiohttp` | ~2MB | Redundant dengan `httpx` |
| `python-dotenv` | ~50KB | Kita tidak pakai `.env` file di project |

---

## Transitive Dependencies Penting

Dependencies berikut tidak kita tambah langsung tapi terinstall karena dibutuhkan dep lain:

| Package | Ditarik oleh | Catatan |
|---|---|---|
| `pydantic-settings` | `mcp` | Tidak kita import langsung |
| `python-dotenv` | `pydantic-settings` via `mcp` | Tidak kita import langsung |
| `starlette` | `fastapi`, `mcp` | FastAPI foundation |
| `anyio` | `httpx`, `mcp`, `openai` | Async primitives |
| `cryptography` | `pyjwt` via `mcp` | JWT support |

---

## Aturan Review Dependency

Sebelum merge PR yang menambah dependency:

- [ ] Justifikasi ada di dokumen ini
- [ ] Ukuran install terdokumentasi
- [ ] Alternatif yang lebih ringan sudah dipertimbangkan
- [ ] Jika heavy (>10MB): masuk ke `[optional-dependencies]`
- [ ] Tidak ada dependency duplikat dengan yang sudah ada
