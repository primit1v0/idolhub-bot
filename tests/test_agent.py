import pytest
from core.config import AppConfig
from core.agent import IdolhubAgent

def test_agent_simple_response(monkeypatch):
    # Arrange: Setup mock config
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "You are a test bot", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

    # Mock call_llm agar tidak request ke internet
    def mock_call_llm(config, messages):
        # Pastikan message user sampai ke LLM
        last_msg = messages[-1]["content"]
        return f"Mocked reply for: {last_msg}"

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    # Act
    agent = IdolhubAgent(cfg)
    response = agent.run("Hello idolhub!")

    # Assert
    assert response == "Mocked reply for: Hello idolhub!"
