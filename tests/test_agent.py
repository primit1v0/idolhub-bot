import pytest
import os
from core.config import AppConfig
from core.agent import IdolhubAgent

@pytest.mark.asyncio
async def test_agent_simple_response(monkeypatch):
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
        # Pastikan message user dan history sampai ke LLM
        # history di-inject ke prompt atau ada di messages
        last_msg = messages[-1]["content"]
        return f"Mocked reply for: {last_msg}"

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    # Act
    agent = IdolhubAgent(cfg)
    await agent.initialize()
    response = await agent.run(user_id="user_1", user_input="Hello idolhub!")

    # Assert
    assert response == "Mocked reply for: Hello idolhub!"
    
    # Check if history is saved
    history = await agent.memory.get_history("user_1")
    assert len(history) == 2
    assert history[0]["content"] == "Hello idolhub!"
    assert history[1]["content"] == "Mocked reply for: Hello idolhub!"
    
    await agent.close()
