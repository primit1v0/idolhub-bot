import pytest
import os
from memory.sqlite_store import SqliteStore
from core.config import AppConfig

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
