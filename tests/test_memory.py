
import pytest

from core.config import AppConfig
from memory.sqlite_store import SqliteStore


@pytest.fixture
async def memory_store(tmp_path):
    # Setup config dummy untuk path db di memory
    db_path = str(tmp_path / "test_memory.db")
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {
            "short_term": {"backend": "sqlite", "path": db_path, "max_messages": 3},
            "long_term": {"backend": "none", "path": ""}
        },
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    
    store = SqliteStore(cfg)
    await store.initialize()
    yield store
    await store.close()

@pytest.mark.asyncio
async def test_memory_add_and_get(memory_store):
    user_id = "user_123"
    
    # Simpan pesan
    await memory_store.add_message(user_id, "user", "Halo")
    await memory_store.add_message(user_id, "assistant", "Halo juga")
    
    # Ambil pesan
    history = await memory_store.get_history(user_id)
    
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Halo"
    assert history[1]["role"] == "assistant"
    assert history[1]["content"] == "Halo juga"

@pytest.mark.asyncio
async def test_memory_respects_max_messages(memory_store):
    user_id = "user_123"
    
    # config diset max_messages = 3, kita simpan 5 pesan
    await memory_store.add_message(user_id, "user", "Pesan 1")
    await memory_store.add_message(user_id, "assistant", "Pesan 2")
    await memory_store.add_message(user_id, "user", "Pesan 3")
    await memory_store.add_message(user_id, "assistant", "Pesan 4")
    await memory_store.add_message(user_id, "user", "Pesan 5")
    
    history = await memory_store.get_history(user_id)
    
    # Harus cuma ambil 3 pesan terakhir (Pesan 3, 4, 5)
    assert len(history) == 3
    assert history[0]["content"] == "Pesan 3"
    assert history[2]["content"] == "Pesan 5"

@pytest.mark.asyncio
async def test_memory_filters_out_invalid_roles(memory_store):
    user_id = "user_456"
    
    await memory_store.add_message(user_id, "user", "Pesan valid 1")
    await memory_store.add_message(user_id, "tool", "Hasil tool yang tidak valid")
    await memory_store.add_message(user_id, "assistant", "Pesan valid 2")
    
    history = await memory_store.get_history(user_id)
    
    # Hanya 'user' dan 'assistant' yang boleh masuk
    assert len(history) == 2
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Pesan valid 1"
    assert history[1]["role"] == "assistant"
    assert history[1]["content"] == "Pesan valid 2"

@pytest.mark.asyncio
async def test_memory_facts_eav(memory_store):
    user_id = "user_789"
    
    # Simpan fakta baru
    fact_id = await memory_store.save_fakta(user_id, "motor", "mioblack")
    assert fact_id > 0
    
    # Ambil fakta
    facts = await memory_store.get_fakta(user_id, "motor")
    assert len(facts) == 1
    assert facts[0]["entity"] == "motor"
    assert facts[0]["nilai"] == "mioblack"
    assert facts[0]["confidence"] == 0.9
    
    # Update fakta yang sama (IntegrityError trigger update)
    update_res = await memory_store.save_fakta(user_id, "motor", "mioblack", confidence=0.95, source="manual")
    assert update_res > 0
    
    facts = await memory_store.get_fakta(user_id, "motor")
    assert len(facts) == 1
    assert facts[0]["confidence"] == 0.95
    assert facts[0]["source"] == "manual"
    
    # Hapus fakta
    deleted = await memory_store.delete_fakta(user_id, "motor")
    assert deleted == 1
    
    facts = await memory_store.get_fakta(user_id, "motor")
    assert len(facts) == 0

@pytest.mark.asyncio
async def test_memory_preferences(memory_store):
    user_id = "user_789"
    
    # Set preferensi
    await memory_store.set_preferensi(user_id, "theme", "dark")
    
    # Get preferensi
    val = await memory_store.get_preferensi(user_id, "theme")
    assert val == "dark"
    
    # Get preferensi default jika tidak ada
    val_default = await memory_store.get_preferensi(user_id, "language", default="id")
    assert val_default == "id"


@pytest.mark.asyncio
async def test_jaccard_deduplication(tmp_path):
    from memory.sqlite_store import SqliteStore, calculate_jaccard
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "test", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": str(tmp_path / "test.db")}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    store = SqliteStore(cfg)
    await store.initialize()
    
    # Test Jaccard calculations
    assert calculate_jaccard("Saya naik motor hitam", "Saya naik motor hitam") == 1.0
    assert calculate_jaccard("Saya naik motor hitam", "Saya mengendarai motor hitam") > 0.5
    assert calculate_jaccard("Halo apa kabar", "Pagi dunia") == 0.0

    # Add first message
    await store.add_message("user_123", "user", "Saya ingin membeli sepeda baru")
    history1 = await store.get_history("user_123")
    assert len(history1) == 1
    
    # Add highly similar message
    await store.add_message("user_123", "user", "Saya ingin membeli sepeda baru!")
    history2 = await store.get_history("user_123")
    # Length should still be 1 because it is deduplicated
    assert len(history2) == 1
    await store.close()


@pytest.mark.asyncio
async def test_fts5_search(tmp_path):
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "test", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": str(tmp_path / "test.fts.db")}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    store = SqliteStore(cfg)
    await store.initialize()
    
    # Add messages
    await store.add_message("user_fts", "user", "Saya suka makan martabak keju")
    await store.add_message("user_fts", "assistant", "Martabak keju itu enak sekali!")
    await store.add_message("user_fts", "user", "Bagaimana cuaca hari ini?")
    
    # Search FTS5
    matches = await store.search_history_fts("user_fts", "martabak")
    assert len(matches) >= 1
    assert "martabak" in matches[0]["content"].lower()
    
    await store.close()


@pytest.mark.asyncio
async def test_fts5_context_threading(tmp_path):
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "test", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {
            "short_term": {
                "backend": "sqlite", 
                "path": str(tmp_path / "test.fts_thread.db"),
                "fts_context_window": 1
            }, 
            "long_term": {"backend": "none", "path": ""}
        },
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })
    store = SqliteStore(cfg)
    await store.initialize()
    
    # Add chronological messages
    await store.add_message("user_fts", "user", "Message 1")
    await store.add_message("user_fts", "assistant", "Message 2")
    await store.add_message("user_fts", "user", "Message 3 (match me)")
    await store.add_message("user_fts", "assistant", "Message 4")
    
    # Search FTS5
    matches = await store.search_history_fts("user_fts", "match")
    assert len(matches) == 1
    assert matches[0]["role"] == "user"
    assert matches[0]["matched_content"] == "Message 3 (match me)"
    # Window is 1, so it should fetch Message 2 (id = 2), Message 3 (id = 3), Message 4 (id = 4)
    expected_thread = "[assistant]: Message 2\n[user]: Message 3 (match me)\n[assistant]: Message 4"
    assert matches[0]["content"] == expected_thread
    
    await store.close()





