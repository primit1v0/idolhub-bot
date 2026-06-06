import pytest
from unittest.mock import patch, MagicMock
from core.config import AppConfig

# Create a mock config to avoid reading config.json and resolving missing env variables
mock_cfg = AppConfig.model_validate({
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

# Patch load_config BEFORE importing the app or lifespan from api.server
with patch("core.config.load_config", return_value=mock_cfg):
    from api.server import app, lifespan

def test_app_instance():
    assert app is not None
    assert app.title == "idolhub API"

@pytest.mark.asyncio
async def test_app_lifespan(monkeypatch):
    from fastapi import FastAPI
    
    # Mock IdolhubAgent initialization and close
    mock_agent_instance = MagicMock()
    
    async def mock_initialize():
        pass
    
    async def mock_close():
        pass
        
    mock_agent_instance.initialize = mock_initialize
    mock_agent_instance.close = mock_close
    
    monkeypatch.setattr("api.server.IdolhubAgent", lambda cfg: mock_agent_instance)
    monkeypatch.setattr("api.server.load_config", lambda: mock_cfg)
    
    test_app = FastAPI(lifespan=lifespan)
    
    async with lifespan(test_app):
        assert test_app.state.agent == mock_agent_instance
        assert test_app.state.cfg == mock_cfg
