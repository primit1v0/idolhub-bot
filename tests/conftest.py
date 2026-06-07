"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def valid_test_config_data():
    """
    Provides a valid configuration dictionary for testing.
    
    This fixture returns a complete, valid configuration that passes
    Pydantic validation. Use this in tests instead of manually creating
    config dictionaries to ensure consistency and validity.
    
    Returns:
        dict: A valid configuration dictionary with all required fields.
    """
    return {
        "app": {
            "name": "idolhub-test",
            "mode": "bot",
            "debug": False,
            "timezone": "UTC"
        },
        "telegram": {
            "token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
            "allowed_users": [],
            "parse_mode": "Markdown"
        },
        "llm": {
            "provider": "openai",
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 4096,
            "timeout": 30
        },
        "providers": {
            "openai": {
                "base_url": "https://api.openai.com/v1",
                "api_key": "sk-test123"
            }
        },
        "memory": {
            "short_term": {
                "backend": "sqlite",
                "path": ":memory:",
                "max_messages": 50,
                "fts_context_window": 2,
                "auto_prune_enabled": True,
                "auto_prune_limit": 1000
            },
            "long_term": {
                "backend": "none",
                "path": "./data/vectors.db",
                "embedding_model": "text-embedding-3-small"
            }
        },
        "plugins": {
            "dir": "./plugins"
        },
        "api": {
            "enabled": False
        },
        "skills": {
            "dir": "./skills",
            "enabled": []
        },
        "tools": {
            "dir": "./tools",
            "enabled": []
        },
        "mcp": {
            "enabled": False,
            "port": 8001
        },
        "logging": {
            "level": "INFO",
            "format": "text"
        },
        "agent": {
            "system_prompt": "You are a helpful assistant.",
            "max_iterations": 10,
            "tools_enabled": True,
            "memory_enabled": True
        }
    }