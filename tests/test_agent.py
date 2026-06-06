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
    async def mock_call_llm(config, messages, tools=None):
        # Pastikan message user dan history sampai ke LLM
        # history di-inject ke prompt atau ada di messages
        last_msg = messages[-1]["content"]
        return {"type": "text", "content": f"Mocked reply for: {last_msg}"}

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


@pytest.mark.asyncio
async def test_agent_memory_tools_execution(monkeypatch):
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

    call_count = 0
    async def mock_call_llm(config, messages, tools=None):
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            class MockFunction:
                def __init__(self, name, arguments):
                    self.name = name
                    self.arguments = arguments

            class MockToolCall:
                def __init__(self, id, name, arguments):
                    self.id = id
                    self.type = "function"
                    self.function = MockFunction(name, arguments)

            tool_calls = [
                MockToolCall("call_1", "save_fact", '{"entity": "hobi", "nilai": "coding"}'),
                MockToolCall("call_2", "set_preference", '{"kunci": "bahasa", "nilai": "id"}')
            ]
            return {
                "type": "tool_calls",
                "calls": tool_calls,
                "message_obj": {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {"name": "save_fact", "arguments": '{"entity": "hobi", "nilai": "coding"}'}
                        },
                        {
                            "id": "call_2",
                            "type": "function",
                            "function": {"name": "set_preference", "arguments": '{"kunci": "bahasa", "nilai": "id"}'}
                        }
                    ]
                }
            }
        else:
            return {"type": "text", "content": "Done processing memory tools!"}

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    # Act
    agent = IdolhubAgent(cfg)
    await agent.initialize()
    response = await agent.run(user_id="user_test", user_input="Remember my hobby is coding and language is Indonesian.")

    # Assert
    assert response == "Done processing memory tools!"

    # Assert database state
    facts = await agent.memory.get_fakta("user_test", "hobi")
    assert len(facts) == 1
    assert facts[0]["nilai"] == "coding"

    pref = await agent.memory.get_preferensi("user_test", "bahasa")
    assert pref == "id"

    await agent.close()


@pytest.mark.asyncio
async def test_agent_relevant_facts_injection(monkeypatch):
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

    captured_messages = []

    async def mock_call_llm(config, messages, tools=None):
        nonlocal captured_messages
        captured_messages = list(messages)
        return {"type": "text", "content": "Mock response"}

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    agent = IdolhubAgent(cfg)
    await agent.initialize()

    # Seed facts
    user_id = "user_fact_test"
    await agent.memory.save_fakta(user_id, "motor", "mioblack")
    await agent.memory.save_fakta(user_id, "hobi", "riding")
    await agent.memory.save_fakta(user_id, "makanan", "pizza")

    # Act 1: query matching 'motor'
    await agent.run(user_id=user_id, user_input="Ceritakan tentang motor saya")

    # Assert 1: system message injected at index 0
    assert len(captured_messages) > 0
    assert captured_messages[0]["role"] == "system"
    assert "Relevant facts:" in captured_messages[0]["content"]
    assert "- motor: mioblack" in captured_messages[0]["content"]
    assert "hobi" not in captured_messages[0]["content"]

    # Act 2: query matching multiple entities ('riding' -> matches 'hobi', 'pizza' -> matches 'makanan')
    captured_messages.clear()
    await agent.run(user_id=user_id, user_input="Apakah hobi riding makanan pizza?")

    # Assert 2: system message injected with both facts
    assert len(captured_messages) > 0
    assert captured_messages[0]["role"] == "system"
    assert "Relevant facts:" in captured_messages[0]["content"]
    assert "- hobi: riding" in captured_messages[0]["content"]
    assert "- makanan: pizza" in captured_messages[0]["content"]
    
    # Act 3: query with no matching entity
    captured_messages.clear()
    await agent.run(user_id=user_id, user_input="Halo apa kabar?")
    
    # Assert 3: no system message injected at index 0 starting with "Relevant facts:"
    assert len(captured_messages) > 0
    assert not any(msg["role"] == "system" and "Relevant facts:" in msg["content"] for msg in captured_messages)

    await agent.close()


@pytest.mark.asyncio
async def test_agent_fts_injection(monkeypatch):
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "test", "max_iterations": 3},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:", "max_messages": 2}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

    captured_messages = []
    async def mock_call_llm(config, messages, tools=None):
        nonlocal captured_messages
        captured_messages = list(messages)
        return {"type": "text", "content": "Mock response"}

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    agent = IdolhubAgent(cfg)
    await agent.initialize()

    user_id = "user_fts_agent"
    # Seed old messages directly
    await agent.memory.add_message(user_id, "user", "Saya punya kucing bernama Koko")
    await agent.memory.add_message(user_id, "assistant", "Kucing yang lucu!")
    await agent.memory.add_message(user_id, "user", "Bagaimana cuaca hari ini?") # Distractor
    
    # Act
    await agent.run(user_id=user_id, user_input="Siapa nama kucing saya?")
    
    # Assert FTS injection contains kucing Koko
    assert len(captured_messages) > 0
    assert any(msg["role"] == "system" and "Relevant past conversations:" in msg["content"] and "Koko" in msg["content"] for msg in captured_messages)

    await agent.close()


@pytest.mark.asyncio
async def test_agent_facts_scoring(monkeypatch):
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "test", "max_iterations": 3},
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

    captured_messages = []
    async def mock_call_llm(config, messages, tools=None):
        nonlocal captured_messages
        captured_messages = list(messages)
        return {"type": "text", "content": "Mock response"}

    monkeypatch.setattr("core.agent.call_llm", mock_call_llm)

    agent = IdolhubAgent(cfg)
    await agent.initialize()

    user_id = "user_score"
    # Seed facts with different criteria
    # 1. 'motor' - High similarity, low recency
    await agent.memory.save_fakta(user_id, "motor", "mioblack", confidence=0.8)
    # 2. 'hobi motor roda dua' - Partial similarity, newer
    await agent.memory.save_fakta(user_id, "hobi motor roda dua", "riding", confidence=0.9)
    # 3. 'motor sport' - High similarity, newest, lower confidence
    await agent.memory.save_fakta(user_id, "motor sport", "kawasaki", confidence=0.5)

    await agent.run(user_id=user_id, user_input="Ceritakan tentang motor saya")

    # Assert facts ranking in system prompt
    assert len(captured_messages) > 0
    sys_msg = [msg["content"] for msg in captured_messages if msg["role"] == "system" and "Relevant facts:" in msg["content"]][0]
    
    # Motor sport should be ranked high due to exact keyword intersection and newest recency, or motor
    assert "motor sport: kawasaki" in sys_msg
    assert "motor: mioblack" in sys_msg

    await agent.close()
