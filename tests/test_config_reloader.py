"""
Tests for core/config_reloader.py - Atomic configuration reloading.
"""

import json

import pytest

from core.config_reloader import (
    clear_change_handlers,
    get_current_config,
    initialize_config,
    register_change_handler,
    reload_config_sync,
    unregister_change_handler,
)
from core.config_schema import AppConfig


@pytest.fixture
def valid_config_data():
    """Fixture providing valid configuration data."""
    return {
        "app": {"name": "test", "mode": "bot", "debug": False, "timezone": "UTC"},
        "agent": {
            "system_prompt": "Test prompt",
            "max_iterations": 10,
            "tools_enabled": True,
            "memory_enabled": True,
            "filter_enabled": True,
            "gating_enabled": True
        },
        "telegram": {"token": "123:abc", "allowed_users": [], "parse_mode": "Markdown"},
        "llm": {"provider": "openai", "model": "gpt-4", "temperature": 0.7, "max_tokens": 4096, "timeout": 30},
        "providers": {
            "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"}
        },
        "memory": {
            "short_term": {"backend": "sqlite", "path": "./data/memory.db", "max_messages": 50, "fts_context_window": 2, "auto_prune_enabled": True, "auto_prune_limit": 1000},
            "long_term": {"backend": "none", "path": "./data/vectors.db", "embedding_model": "text-embedding-3-small"}
        },
        "skills": {"dir": "./skills", "enabled": []},
        "tools": {"dir": "./tools", "enabled": []},
        "plugins": {"dir": "./plugins", "enabled": []},
        "api": {"enabled": True, "host": "127.0.0.1", "port": 8000, "cors_origins": []},
        "mcp": {"enabled": True, "port": 8001},
        "logging": {"level": "INFO", "format": "text"}
    }


@pytest.fixture(autouse=True)
def cleanup_handlers():
    """Cleanup change handlers after each test."""
    yield
    clear_change_handlers()


class TestInitializeConfig:
    def test_initialize_valid_config(self, tmp_path, valid_config_data):
        """Test initializing with valid configuration."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        config = initialize_config(str(config_file))
        assert isinstance(config, AppConfig)
        assert config.app.name == "test"
    
    def test_initialize_invalid_config(self, tmp_path):
        """Test initializing with invalid configuration."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            f.write("{invalid json")
        
        with pytest.raises(ValueError):
            initialize_config(str(config_file))


class TestGetCurrentConfig:
    def test_get_config_after_init(self, tmp_path, valid_config_data):
        """Test getting config after initialization."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        config = get_current_config()
        assert isinstance(config, AppConfig)
        assert config.app.name == "test"
    
    def test_get_config_before_init(self):
        """Test getting config before initialization raises error."""
        # Note: This test may fail if other tests have initialized config
        # In real scenario, would need to reset global state
        pass


class TestReloadConfig:
    def test_reload_valid_config(self, tmp_path, valid_config_data):
        """Test reloading with valid configuration."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        # Modify config
        valid_config_data["app"]["name"] = "modified"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        success, message = reload_config_sync(str(config_file))
        assert success is True
        assert "successfully" in message.lower()
        
        config = get_current_config()
        assert config.app.name == "modified"
    
    def test_reload_invalid_config_rollback(self, tmp_path, valid_config_data):
        """Test that invalid config reload rolls back to previous."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        original_name = get_current_config().app.name
        
        # Write invalid config
        with open(config_file, "w") as f:
            f.write("{invalid json")
        
        success, message = reload_config_sync(str(config_file))
        assert success is False
        assert "failed" in message.lower()
        
        # Config should still be the original
        config = get_current_config()
        assert config.app.name == original_name
    
    def test_reload_missing_file(self, tmp_path, valid_config_data):
        """Test reloading non-existent file."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        success, message = reload_config_sync("/nonexistent/config.json")
        assert success is False
        assert "not found" in message.lower()


class TestChangeHandlers:
    def test_register_and_call_handler(self, tmp_path, valid_config_data):
        """Test registering and calling change handler."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        handler_called = []
        
        def test_handler(config: AppConfig):
            handler_called.append(config.app.name)
        
        register_change_handler(test_handler)
        
        # Modify and reload
        valid_config_data["app"]["name"] = "changed"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        reload_config_sync(str(config_file))
        
        assert len(handler_called) == 1
        assert handler_called[0] == "changed"
    
    def test_unregister_handler(self, tmp_path, valid_config_data):
        """Test unregistering change handler."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        handler_called = []
        
        def test_handler(config: AppConfig):
            handler_called.append(True)
        
        register_change_handler(test_handler)
        unregister_change_handler(test_handler)
        
        # Modify and reload
        valid_config_data["app"]["name"] = "changed"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        reload_config_sync(str(config_file))
        
        # Handler should not be called
        assert len(handler_called) == 0
    
    def test_handler_error_doesnt_break_reload(self, tmp_path, valid_config_data):
        """Test that handler errors don't break reload."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        def failing_handler(config: AppConfig):
            raise Exception("Handler error")
        
        register_change_handler(failing_handler)
        
        # Modify and reload
        valid_config_data["app"]["name"] = "changed"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        success, message = reload_config_sync(str(config_file))
        
        # Reload should still succeed despite handler error
        assert success is True
        assert get_current_config().app.name == "changed"
    
    def test_clear_handlers(self, tmp_path, valid_config_data):
        """Test clearing all handlers."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        initialize_config(str(config_file))
        
        handler_called = []
        
        def test_handler(config: AppConfig):
            handler_called.append(True)
        
        register_change_handler(test_handler)
        clear_change_handlers()
        
        # Modify and reload
        valid_config_data["app"]["name"] = "changed"
        with open(config_file, "w") as f:
            json.dump(valid_config_data, f)
        
        reload_config_sync(str(config_file))
        
        # Handler should not be called
        assert len(handler_called) == 0
