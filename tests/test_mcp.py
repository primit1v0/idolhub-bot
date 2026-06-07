# tests/test_mcp.py
import pytest
from mcp.server.fastmcp import FastMCP

from mcp_server.server import create_mcp_server


@pytest.mark.asyncio
async def test_mcp_server_tool_registry(monkeypatch, valid_test_config_data):
    from core.config import AppConfig
    
    mock_cfg = AppConfig.model_validate({
        "app": {"name": "test-mcp", "mode": "mcp"},
        "telegram": {"token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "https://api.openai.com/v1", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": "./data/vectors.db"}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "api": {"enabled": False, "cors_origins": ["*"]},
        "mcp": {"enabled": True, "port": 8001},
        "logging": {"level": "INFO"}
    })
    
    # Import mcp_server.server to patch load_config
    import mcp_server.server
    monkeypatch.setattr(mcp_server.server, "load_config", lambda *args, **kwargs: mock_cfg)
    
    server = create_mcp_server()
    assert isinstance(server, FastMCP)
    # Check execute_bash tool is present
    tools = await server.list_tools()
    assert any(t.name == "execute_bash" for t in tools)
