import pytest
from core.llm import get_llm_client
from core.config import AppConfig

def test_get_openai_client():
    # Arrange: mock config
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot", "debug": False, "timezone": "UTC"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.0, "max_tokens": 100, "timeout": 30},
        "providers": {
            "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-123"}
        },
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO", "format": "text"}
    })

    # Act
    client = get_llm_client(cfg)

    # Assert
    assert client.api_key == "sk-123"
    assert str(client.base_url).rstrip("/") == "https://api.openai.com/v1"

def test_get_github_copilot_client():
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "github_copilot", "model": "gpt-4"},
        "providers": {
            "github_copilot": {"base_url": "https://api.githubcopilot.com", "cli_token": "gho_123"}
        },
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

    client = get_llm_client(cfg)
    assert client.api_key == "gho_123"
    assert str(client.base_url).rstrip("/") == "https://api.githubcopilot.com"

def test_get_openai_codex_client():
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai_codex", "model": "gpt-4"},
        "providers": {
            "openai_codex": {"base_url": "https://api.openai.com/v1", "oauth_token": "oauth_123"}
        },
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

    client = get_llm_client(cfg)
    assert client.api_key == "oauth_123"
    assert str(client.base_url).rstrip("/") == "https://api.openai.com/v1"

def test_invalid_provider_raises_error():
    cfg = AppConfig.model_validate({
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "unknown", "model": "gpt-4"},
        "providers": {},
        "memory": {"short_term": {"backend": "sqlite", "path": ":memory:"}, "long_term": {"backend": "none", "path": ""}},
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    })

    with pytest.raises(ValueError):
        get_llm_client(cfg)
