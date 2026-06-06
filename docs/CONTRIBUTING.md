# Contributing to idolhub

> Baca filosofi di README.md terlebih dahulu sebelum berkontribusi.

---

## Prinsip Utama

### Zero Bloatware
- Setiap dependency wajib punya justifikasi di komentar `pyproject.toml`
- Heavy deps (ML libs, vector DB, dll) masuk `[optional-dependencies]`
- Gunakan `uv add X` bukan `pip install X`

### Zero Dead Code
- Tidak ada fungsi/class/import yang tidak dipakai
- Tidak ada commented-out code yang di-commit
- Tidak ada `TODO` tanpa issue reference

### Pure & Minimal Code
- Satu fungsi → satu tujuan
- Panjang file maksimal ~150 baris — pecah jika lebih
- Type hints wajib di semua public API
- Docstring hanya jika nama + type hints tidak cukup jelas

---

## Menambah Dependency Baru

Jawab semua pertanyaan ini sebelum `uv add X`:

1. Apakah bisa pakai stdlib Python? (`json`, `re`, `sqlite3`, `asyncio`, ...)
2. Apakah `httpx` atau dep yang sudah ada bisa handle ini?
3. Berapa ukuran install package + transitive deps? (`pip show X` / PyPI)
4. Apakah benar-benar dibutuhkan sekarang, atau bisa defer ke phase berikutnya?

**Jika tidak lulus minimal 2 pertanyaan → jangan tambah.**

---

## Workflow

```bash
# Setup
uv sync --dev

# Lint
uv run ruff check .
uv run ruff format --check .

# Test
uv run pytest

# Run
uv run python main.py bot
```

---

## Struktur Commit

```
type: deskripsi singkat

- detail perubahan
- alasan perubahan
```

Types: `feat`, `fix`, `refactor`, `docs`, `chore`, `test`

---

## Inject Fitur Baru

| Jenis | Cara | Auto-loaded? |
|---|---|---|
| Skill | Drop `.md` ke `skills/` | ✅ Ya |
| Tool | Drop `.py` ke `tools/` | ✅ Ya |
| Plugin/Hook | Drop `.py` ke `plugins/` | ✅ Ya |
| LLM Provider | Tambah provider baru di core/llm.py | ❌ Daftarkan credentials di config.py & config.json |

Tidak perlu ubah core untuk menambah skill, tool, atau plugin.
