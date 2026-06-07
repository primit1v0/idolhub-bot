import pytest

from core.config import AppConfig, load_config, resolve_env


def test_resolve_env_success(monkeypatch):
    monkeypatch.setenv("DUMMY_TOKEN", "12345")
    assert resolve_env("$DUMMY_TOKEN") == "12345"

def test_resolve_env_embedded(monkeypatch):
    monkeypatch.setenv("API_URL", "https://api.example.com")
    assert resolve_env("URL: $API_URL/v1") == "URL: https://api.example.com/v1"

def test_resolve_env_missing_raises_error():
    with pytest.raises(KeyError):
        resolve_env("$MISSING_VAR")

def test_resolve_env_no_var():
    assert resolve_env("just string") == "just string"

def test_load_config_resolves_nested_dict(monkeypatch, tmp_path):
    monkeypatch.setenv("MY_KEY", "secret-key")
    
    config_file = tmp_path / "config.json"
    config_file.write_text('''
    {
      "app": {"name": "test", "mode": "bot", "debug": false, "timezone": "UTC"},
      "telegram": {"token": "$MY_KEY", "allowed_users": [], "parse_mode": "Markdown"},
      "llm": {"provider": "openai", "model": "test", "temperature": 0.0, "max_tokens": 100, "timeout": 10},
      "providers": {},
      "memory": {
          "short_term": {"backend": "sqlite", "path": ":memory:", "max_messages": 10},
          "long_term": {"backend": "none", "path": ":memory:"}
      },
      "skills": {"dir": "./skills", "enabled": []},
      "tools": {"dir": "./tools", "enabled": []},
      "plugins": {"dir": "./plugins", "enabled": []},
      "api": {"enabled": false, "host": "127.0.0.1", "port": 8000, "cors_origins": []},
      "mcp": {"enabled": false, "port": 8001},
      "logging": {"level": "INFO", "format": "text"},
      "agent": {"system_prompt": "test", "max_iterations": 1, "tools_enabled": true, "memory_enabled": false}
    }
    ''')
    
    cfg = load_config(str(config_file))
    
    assert isinstance(cfg, AppConfig)
    assert cfg.telegram.token == "secret-key"
    assert cfg.app.name == "test"


def test_long_term_config_embedding_model():
    from core.config import load_config
    import tempfile
    import json
    
    data = {
        "app": {"name": "test", "mode": "bot"},
        "telegram": {"token": "test"},
        "agent": {"system_prompt": "sys"},
        "llm": {"provider": "openai", "model": "gpt-4"},
        "providers": {"openai": {"base_url": "dummy", "api_key": "dummy"}},
        "memory": {
            "short_term": {"backend": "sqlite", "path": "x"},
            "long_term": {"backend": "sqlite_vec", "path": "y", "embedding_model": "text-embedding-3-small"}
        },
        "skills": {"dir": "./skills"},
        "tools": {"dir": "./tools"},
        "plugins": {"dir": "./plugins"},
        "api": {"enabled": False},
        "mcp": {"enabled": False},
        "logging": {"level": "INFO"}
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        f.flush()
        
    cfg = load_config(f.name)
    assert cfg.memory.long_term.embedding_model == "text-embedding-3-small"

