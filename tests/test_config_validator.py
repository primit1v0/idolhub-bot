"""
Tests for core/config_validator.py - Configuration validation and loading.
"""

import json
import os

import pytest

from core.config_schema import AppConfig
from core.config_validator import (
    get_available_providers,
    get_enabled_capabilities,
    load_config,
    resolve_env,
    validate_capability_whitelists,
)


class TestResolveEnv:
    def test_resolve_single_var(self):
        """Test resolving single environment variable."""
        os.environ["TEST_VAR"] = "test_value"
        result = resolve_env("$TEST_VAR")
        assert result == "test_value"
        del os.environ["TEST_VAR"]
    
    def test_resolve_multiple_vars(self):
        """Test resolving multiple environment variables."""
        os.environ["VAR1"] = "value1"
        os.environ["VAR2"] = "value2"
        result = resolve_env("$VAR1 and $VAR2")
        assert result == "value1 and value2"
        del os.environ["VAR1"]
        del os.environ["VAR2"]
    
    def test_missing_var_raises_error(self):
        """Test that missing environment variable raises KeyError."""
        with pytest.raises(KeyError) as exc_info:
            resolve_env("$NONEXISTENT_VAR")
        assert "NONEXISTENT_VAR" in str(exc_info.value)
    
    def test_non_string_passthrough(self):
        """Test that non-string values pass through unchanged."""
        assert resolve_env(123) == 123
        assert resolve_env(True) is True
        assert resolve_env(None) is None


class TestLoadConfig:
    def test_load_valid_config(self, tmp_path):
        """Test loading valid configuration file."""
        config_data = {
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
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        config = load_config(str(config_file))
        assert isinstance(config, AppConfig)
        assert config.app.name == "test"
    
    def test_load_config_with_env_vars(self, tmp_path):
        """Test loading config with environment variable substitution."""
        os.environ["TEST_API_KEY"] = "sk-test-key"
        
        config_data = {
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
                "openai": {"base_url": "https://api.openai.com/v1", "api_key": "$TEST_API_KEY"}
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
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        config = load_config(str(config_file))
        assert config.providers["openai"].api_key == "sk-test-key"
        
        del os.environ["TEST_API_KEY"]
    
    def test_load_config_missing_file(self):
        """Test loading non-existent config file."""
        with pytest.raises(FileNotFoundError) as exc_info:
            load_config("nonexistent.json")
        assert "not found" in str(exc_info.value)
    
    def test_load_config_invalid_json(self, tmp_path):
        """Test loading malformed JSON file."""
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            f.write("{invalid json")
        
        with pytest.raises(ValueError) as exc_info:
            load_config(str(config_file))
        assert "Invalid JSON" in str(exc_info.value)
    
    def test_load_config_missing_env_var(self, tmp_path):
        """Test loading config with missing environment variable."""
        config_data = {
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
                "openai": {"base_url": "https://api.openai.com/v1", "api_key": "$MISSING_VAR"}
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
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        with pytest.raises(KeyError) as exc_info:
            load_config(str(config_file))
        assert "MISSING_VAR" in str(exc_info.value)


class TestValidateCapabilityWhitelists:
    def test_validate_with_existing_dirs(self, tmp_path):
        """Test validation with existing directories."""
        skills_dir = tmp_path / "skills"
        plugins_dir = tmp_path / "plugins"
        skills_dir.mkdir()
        plugins_dir.mkdir()
        
        config_data = {
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
            "skills": {"dir": str(skills_dir), "enabled": ["test"]},
            "tools": {"dir": "./tools", "enabled": []},
            "plugins": {"dir": str(plugins_dir), "enabled": ["test"]},
            "api": {"enabled": True, "host": "127.0.0.1", "port": 8000, "cors_origins": []},
            "mcp": {"enabled": True, "port": 8001},
            "logging": {"level": "INFO", "format": "text"}
        }
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        config = load_config(str(config_file))
        # Should not raise
        validate_capability_whitelists(config)
    
    def test_validate_missing_skills_dir(self, tmp_path):
        """Test validation with missing skills directory."""
        config_data = {
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
            "skills": {"dir": "/nonexistent/skills", "enabled": ["test"]},
            "tools": {"dir": "./tools", "enabled": []},
            "plugins": {"dir": "./plugins", "enabled": []},
            "api": {"enabled": True, "host": "127.0.0.1", "port": 8000, "cors_origins": []},
            "mcp": {"enabled": True, "port": 8001},
            "logging": {"level": "INFO", "format": "text"}
        }
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        # load_config calls validate_capability_whitelists internally
        with pytest.raises(ValueError) as exc_info:
            load_config(str(config_file))
        assert "Skills directory not found" in str(exc_info.value)


class TestHelperFunctions:
    def test_get_available_providers(self, tmp_path):
        """Test getting available providers."""
        config_data = {
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
                "openai": {"base_url": "https://api.openai.com/v1", "api_key": "sk-test"},
                "gemini": {"base_url": "https://api.gemini.com/v1", "api_key": "gm-test"}
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
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        config = load_config(str(config_file))
        providers = get_available_providers(config)
        assert providers == {"openai", "gemini"}
    
    def test_get_enabled_capabilities(self, tmp_path):
        """Test getting enabled capabilities."""
        config_data = {
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
            "skills": {"dir": "./skills", "enabled": ["skill1", "skill2"]},
            "tools": {"dir": "./tools", "enabled": ["tool1"]},
            "plugins": {"dir": "./plugins", "enabled": []},
            "api": {"enabled": True, "host": "127.0.0.1", "port": 8000, "cors_origins": []},
            "mcp": {"enabled": True, "port": 8001},
            "logging": {"level": "INFO", "format": "text"}
        }
        
        config_file = tmp_path / "config.json"
        with open(config_file, "w") as f:
            json.dump(config_data, f)
        
        config = load_config(str(config_file))
        capabilities = get_enabled_capabilities(config)
        assert capabilities["skills"] == ["skill1", "skill2"]
        assert capabilities["tools"] == ["tool1"]
        assert capabilities["plugins"] == []
