# idolhub — Async PocketFlow Agent Flow Design Spec

> **Historical status: Implemented.**
>
> This document records the original design. Current behavior and status are
> defined in [`docs/BASELINE.md`](../../BASELINE.md). Any phase numbering is
> local to this historical work item.

**Date:** 2026-06-06  
**Status:** Approved ✅

---

## 1. Overview

Spesifikasi ini mendefinisikan migrasi sistem agent `idolhub` ke alur eksekusi asinkron penuh menggunakan fitur asli `AsyncNode` dan `AsyncFlow` dari pustaka `pocketflow`. 

Langkah ini juga mengintegrasikan Event Bus (lifecycle hooks) dan Skill Loader untuk menyelesaikan Phase 1 sejalan dengan filosofi *lightweight* dan efisiensi memori.

---

## 2. PocketFlow Async Graph & Declarative Transitions

Kita akan mengubah implementasi agent di [`core/agent.py`](../../../core/agent.py) dari iterasi `while` imperatif menjadi graf asinkron deklaratif menggunakan operator transisi PocketFlow:

- **AnswerNode** (`AsyncNode`): Memanggil LLM secara asinkron. Mengembalikan aksi `"done"` jika berhasil membalas dengan teks, atau `"tool_call"` jika memerlukan pemanggilan tool.
- **ToolExecutionNode** (`AsyncNode`): Mengeksekusi tool-tool yang dipanggil secara sekuensial, menginjeksi hasilnya ke riwayat pesan, dan loop kembali ke `AnswerNode`.

### 2.1 Graf Alur Deklaratif

```python
self.answer_node = AnswerNode(self.cfg)
self.tool_node = ToolExecutionNode(self.cfg, self.tools_mapping)

# Graf Transisi PocketFlow:
# answer_node mengirim action "tool_call" ke tool_node
self.answer_node - "tool_call" >> self.tool_node

# tool_node kembali ke answer_node dengan action default
self.tool_node >> self.answer_node

self.flow = AsyncFlow(start=self.answer_node)
```

---

## 3. Asynchronous LLM Client

Kita akan mengubah berkas [`core/llm.py`](../../../core/llm.py) agar menggunakan `AsyncOpenAI` dari pustaka `openai` SDK:

- Fungsi `call_llm` diubah menjadi asinkron (`async def call_llm`).
- Panggilan API chat completions diubah menggunakan `await client.chat.completions.create(...)`.
- `get_llm_client` tetap dipertahankan sinkron dalam instansiasinya karena `AsyncOpenAI()` tidak memerlukan pemanggilan async untuk inisialisasi, menjaga kompatibilitas pengujian di `tests/test_llm.py`.

---

## 4. Hook Lifecycle & Event Bus (Plugins)

Menambahkan berkas [`core/event_bus.py`](../../../core/event_bus.py) untuk menyebarkan event asinkron ke plugin.

### 4.1 Daftar Event & Trigger Point
1. `before_message`: Di awal `agent.run`.
2. `after_message`: Setelah input diterima, sebelum graph berjalan.
3. `on_tool_call`: Sesaat sebelum mengeksekusi tool di `ToolExecutionNode`.
4. `before_reply`: Setelah graf selesai, sebelum respons akhir disimpan.
5. `after_reply`: Setelah respons disimpan ke memory.
6. `on_error`: Jika terjadi error di graf atau agent.

Pemuat plugin di [`plugins/loader.py`](../../../plugins/loader.py) memuat berkas `.py` dari direktori `plugins/` secara dinamis menggunakan `importlib` dan meregistrasikan fungsi yang memiliki nama yang sama dengan event ke Event Bus.

---

## 5. Skill Loader (Hermes/OpenClaw-Compatible)

Menambahkan berkas [`skills/loader.py`](../../../skills/loader.py) untuk memuat berkas `.md` dengan YAML frontmatter dari folder `skills/`:
- Memparse frontmatter YAML dengan `pyyaml`.
- Membuat skema OpenAI Tool secara otomatis.
- Membuat fungsi *runner* dinamis yang memicu LLM call terisolasi dengan instruksi markdown skill sebagai system prompt sementara.

---

## 6. Verification Plan

1. Buat unit test baru di [`tests/test_skills_plugins.py`](../../../tests/test_skills_plugins.py) untuk memverifikasi event bus, pemuatan plugin dinamis, dan pemuatan skill markdown.
2. Perbarui [`tests/test_agent.py`](../../../tests/test_agent.py) untuk menggunakan `async def mock_call_llm`.
3. Jalankan seluruh unit test suite dengan `uv run pytest` untuk memastikan status kelulusan 100%.
