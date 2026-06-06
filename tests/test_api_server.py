import pytest
from unittest.mock import patch, MagicMock
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
def mock_load_config(mock_cfg, monkeypatch):
    # Patch core.config.load_config so import-time creation of the default app gets mock_cfg
    with patch("core.config.load_config", return_value=mock_cfg):
        from api.server import load_config
        # Patch api.server.load_config for runtime create_app calls in other tests
        monkeypatch.setattr("api.server.load_config", lambda: mock_cfg)
        yield

def test_app_instance(mock_load_config):
    from api.server import create_app
    app = create_app()
    assert app is not None
    assert app.title == "idolhub API"

def test_app_lifespan(monkeypatch, mock_cfg, mock_load_config):
    from fastapi.testclient import TestClient
    
    mock_agent_instance = MagicMock()
    
    async def mock_initialize():
        pass
    
    async def mock_close():
        pass
        
    mock_agent_instance.initialize = mock_initialize
    mock_agent_instance.close = mock_close
    
    monkeypatch.setattr("api.server.IdolhubAgent", lambda cfg: mock_agent_instance)
    
    from api.server import create_app
    app = create_app()
    
    with TestClient(app) as client:
        assert client.app.state.agent == mock_agent_instance
        assert client.app.state.cfg == mock_cfg

def test_cors_allow_credentials_wildcard(mock_cfg, mock_load_config):
    from api.server import create_app
    app = create_app()
    
    cors_middleware = None
    for middleware in app.user_middleware:
        if middleware.cls.__name__ == "CORSMiddleware":
            cors_middleware = middleware
            break
            
    assert cors_middleware is not None
    assert cors_middleware.kwargs["allow_credentials"] is False

def test_cors_allow_credentials_specific(mock_cfg, mock_load_config, monkeypatch):
    mock_cfg.api.cors_origins = ["http://localhost:3000"]
    # Update the load_config mock return value for this test
    monkeypatch.setattr("api.server.load_config", lambda: mock_cfg)
    
    from api.server import create_app
    app = create_app()
    
    cors_middleware = None
    for middleware in app.user_middleware:
        if middleware.cls.__name__ == "CORSMiddleware":
            cors_middleware = middleware
            break
            
    assert cors_middleware is not None
    assert cors_middleware.kwargs["allow_credentials"] is True
