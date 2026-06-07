"""
Configuration loading and management.

This module provides backward-compatible configuration loading using
the enhanced validation system from config_validator and config_schema.

For new code, prefer using:
- config_validator.load_config() for loading
- config_reloader.get_current_config() for access
- config_reloader.reload_config() for reloading
"""

from core.config_schema import (
    AgentSection,
    ApiSection,
    AppConfig,
    AppSection,
    LlmSection,
    LoggingSection,
    LongTermMemory,
    McpSection,
    MemorySection,
    PluginsSection,
    ProviderCredentials,
    ShortTermMemory,
    SkillsSection,
    TelegramSection,
    ToolsSection,
)
from core.config_validator import (
    _resolve_dict,
    get_available_providers,
    get_enabled_capabilities,
    load_config,
    resolve_env,
    validate_capability_whitelists,
    validate_provider_credentials,
)

# Re-export for backward compatibility
__all__ = [
    # Main config class
    "AppConfig",
    # Section classes
    "AppSection",
    "AgentSection",
    "TelegramSection",
    "LlmSection",
    "ProviderCredentials",
    "ShortTermMemory",
    "LongTermMemory",
    "MemorySection",
    "SkillsSection",
    "ToolsSection",
    "PluginsSection",
    "ApiSection",
    "McpSection",
    "LoggingSection",
    # Functions
    "_resolve_dict",
    "load_config",
    "resolve_env",
    "validate_capability_whitelists",
    "validate_provider_credentials",
    "get_available_providers",
    "get_enabled_capabilities",
]