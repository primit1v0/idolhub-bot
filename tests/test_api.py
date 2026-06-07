# tests/test_api.py
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

from core.config import AppConfig


@pytest.fixture
def mock_cfg():
    return AppConfig.model_validate({
        "app": {"name": "test", "mode": "api"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": True, "cors_origins": ["*"]},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

@pytest.fixture
def client(mock_cfg, monkeypatch):
    monkeypatch.setattr("core.config.load_config", lambda *args, **kwargs: mock_cfg)
    monkeypatch.setattr("api.server.load_config", lambda *args, **kwargs: mock_cfg)
    from api.server import create_app
    
    # Mock the IdolhubAgent
    mock_agent_instance = MagicMock()
    async def mock_run(user_id: str, user_input: str):
        return f"Mock response for user {user_id}: {user_input}"
    async def mock_initialize():
        pass
    async def mock_close():
        pass
    mock_agent_instance.run = mock_run
    mock_agent_instance.initialize = mock_initialize
    mock_agent_instance.close = mock_close
    
    monkeypatch.setattr("api.server.IdolhubAgent", lambda cfg: mock_agent_instance)
    
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "idolhub"

    
def test_chat_endpoint(client):
    response = client.post("/chat", json={"message": "hello", "user_id": "123"})
    assert response.status_code == 200
    assert response.json() == {"response": "Mock response for user 123: hello"}
    
def test_get_config_masked(client):
    response = client.get("/config")
    assert response.status_code == 200
    data = response.json()
    assert "config" in data
    assert data["config"]["telegram"]["token"] == "********"

def test_update_config(client, monkeypatch, tmp_path):
    import json
    
    close_called = []
    init_called = []
    
    # Spy on the initial agent's close
    original_close = client.app.state.agent.close
    async def spy_close():
        close_called.append(True)
        await original_close()
    client.app.state.agent.close = spy_close
    
    # Mock the new agent creation
    mock_new_agent = MagicMock()
    async def mock_init():
        init_called.append(True)
    async def mock_new_close():
        pass
    mock_new_agent.initialize = mock_init
    mock_new_agent.close = mock_new_close
    
    monkeypatch.setattr("core.agent.IdolhubAgent", lambda cfg: mock_new_agent)

    # Create a temp config.json file
    temp_config = tmp_path / "config.json"
    temp_config.write_text(json.dumps({
        "app": {"name": "test", "mode": "api"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": True, "cors_origins": ["*"]},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    }))
    
    # Patch open inside api.routes.config to intercept "config.json"
    original_open = open
    def mock_open(file, *args, **kwargs):
        if file == "config.json":
            return original_open(temp_config, *args, **kwargs)
        return original_open(file, *args, **kwargs)
        
    monkeypatch.setattr("builtins.open", mock_open)
    
    # Patch load_config inside api.routes.config to load from temp_config using the unpatched core function
    from core.config import AppConfig
    
    def mock_load_config_func(*args, **kwargs):
        with open(temp_config, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        return AppConfig(**raw_data)
        
    monkeypatch.setattr("api.routes.config.load_config", mock_load_config_func)
    
    response = client.post("/config", json={"app": {"name": "new_name"}})
    assert response.status_code == 200
    data = response.json()
    assert data["config"]["app"]["name"] == "new_name"
    
    # Assertions for agent recreation and initialization
    assert len(close_called) == 1
    assert len(init_called) == 1
    assert client.app.state.agent == mock_new_agent

def test_update_config_invalid_fails(client, monkeypatch, tmp_path):
    import json
    
    temp_config = tmp_path / "config.json"
    temp_config.write_text(json.dumps({
        "app": {"name": "test", "mode": "api"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": True, "cors_origins": ["*"]},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    }))
    
    original_open = open
    def mock_open(file, *args, **kwargs):
        if file == "config.json":
            return original_open(temp_config, *args, **kwargs)
        return original_open(file, *args, **kwargs)
        
    monkeypatch.setattr("builtins.open", mock_open)
    
    from core.config import AppConfig
    def mock_load_config_func(*args, **kwargs):
        with open(temp_config, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        return AppConfig(**raw_data)
    monkeypatch.setattr("api.routes.config.load_config", mock_load_config_func)
    
    # Try sending invalid mode "invalid_mode" which violates AppSection's literal constraint
    response = client.post("/config", json={"app": {"mode": "invalid_mode"}})
    assert response.status_code == 400
    assert "validation failed" in response.json()["detail"].lower()

def test_update_config_secrets_overwrite_protection(client, monkeypatch, tmp_path):
    import json
    
    temp_config = tmp_path / "config.json"
    temp_config.write_text(json.dumps({
        "app": {"name": "test", "mode": "api"},
        "telegram": {"token": "my_original_secret_token"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": True, "cors_origins": ["*"]},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    }))
    
    original_open = open
    def mock_open(file, *args, **kwargs):
        if file == "config.json":
            return original_open(temp_config, *args, **kwargs)
        return original_open(file, *args, **kwargs)
        
    monkeypatch.setattr("builtins.open", mock_open)
    
    from core.config import AppConfig
    def mock_load_config_func(*args, **kwargs):
        with open(temp_config, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        return AppConfig(**raw_data)
    monkeypatch.setattr("api.routes.config.load_config", mock_load_config_func)
    
    # Update some other fields, but pass the masked value "********" for the telegram token
    response = client.post("/config", json={
        "app": {"name": "updated_app_name"},
        "telegram": {"token": "********"}
    })
    
    assert response.status_code == 200
    
    # Read the file content from disk to verify the original token wasn't overwritten by "********"
    with open(temp_config, "r", encoding="utf-8") as f:
        written_data = json.load(f)
    
    assert written_data["telegram"]["token"] == "my_original_secret_token"
    assert written_data["app"]["name"] == "updated_app_name"


def test_health_metrics(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert "system" in data
    assert "ram_available_mb" in data["system"]
    assert "disk" in data["system"]
    assert "cpu_load_avg" in data["system"]



