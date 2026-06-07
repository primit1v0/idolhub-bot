"""
Configuration validator with whitelist checking and fail-fast validation.

This module provides:
- Configuration loading with environment variable substitution
- Provider whitelist validation
- Tool/plugin/skill capability validation
- Clear error messages for misconfigurations
- Fail-fast behavior at startup
"""

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Set

from core.config_schema import AppConfig


def resolve_env(value: str) -> str:
    """
    Resolve $VAR_NAME tokens in a string using os.environ.
    
    Raises:
        KeyError: If environment variable is not found
    """
    if not isinstance(value, str):
        return value
    
    # Matches $VAR_NAME (letters, numbers, underscores, must start with letter/underscore)
    pattern = re.compile(r'\$([A-Z_][A-Z0-9_]*)')
    
    def replacer(match: re.Match) -> str:
        var_name = match.group(1)
        try:
            return os.environ[var_name]
        except KeyError:
            raise KeyError(
                f"Environment variable ${var_name} not found. "
                f"Please set it before running the application."
            )
        
    return pattern.sub(replacer, value)


def _resolve_dict(data: Any) -> Any:
    """
    Recursively resolve $VAR_NAME in dictionaries and lists.
    
    Skips keys starting with underscore (comments).
    """
    if isinstance(data, dict):
        return {k: _resolve_dict(v) for k, v in data.items() if not k.startswith("_")}
    elif isinstance(data, list):
        return [_resolve_dict(item) for item in data]
    elif isinstance(data, str):
        return resolve_env(data)
    else:
        return data


def load_config(path: str = "config.json") -> AppConfig:
    """
    Load configuration from JSON file with validation.
    
    Steps:
    1. Load JSON file
    2. Resolve environment variables ($VAR_NAME)
    3. Validate against Pydantic schema
    4. Validate capability whitelists
    
    Args:
        path: Path to configuration file
        
    Returns:
        Validated AppConfig instance
        
    Raises:
        FileNotFoundError: If config file doesn't exist
        json.JSONDecodeError: If JSON is malformed
        KeyError: If required environment variable is missing
        ValueError: If configuration is invalid
    """
    # Check file exists
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Configuration file not found: {path}\n"
            f"Copy config.example.json to {path} and configure it."
        )
    
    # Load and parse JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON in configuration file {path}: {e}"
        )
    
    # Resolve environment variables
    try:
        resolved_data = _resolve_dict(raw_data)
    except KeyError as e:
        raise KeyError(
            f"Configuration error in {path}: {e}\n"
            f"Ensure all $VARIABLE references have corresponding environment variables set."
        )
    
    # Validate with Pydantic schema
    try:
        config = AppConfig(**resolved_data)
    except Exception as e:
        raise ValueError(
            f"Configuration validation failed for {path}:\n{e}"
        )
    
    # Additional whitelist validations
    validate_capability_whitelists(config)
    
    return config


def validate_capability_whitelists(config: AppConfig) -> None:
    """
    Validate that enabled capabilities exist and are accessible.
    
    Checks:
    - Skills directory exists if skills are enabled
    - Plugins directory exists if plugins are enabled
    - Tools directory exists (warning only, not enforced yet)
    
    Args:
        config: Validated AppConfig instance
        
    Raises:
        ValueError: If required directories don't exist
    """
    errors: List[str] = []
    warnings: List[str] = []
    
    # Validate skills directory
    if config.skills.enabled:
        skills_path = Path(config.skills.dir)
        if not skills_path.exists():
            errors.append(
                f"Skills directory not found: {config.skills.dir}\n"
                f"Create the directory or set skills.enabled to []"
            )
        elif not skills_path.is_dir():
            errors.append(
                f"Skills path is not a directory: {config.skills.dir}"
            )
    
    # Validate plugins directory
    if config.plugins.enabled:
        plugins_path = Path(config.plugins.dir)
        if not plugins_path.exists():
            errors.append(
                f"Plugins directory not found: {config.plugins.dir}\n"
                f"Create the directory or set plugins.enabled to []"
            )
        elif not plugins_path.is_dir():
            errors.append(
                f"Plugins path is not a directory: {config.plugins.dir}"
            )
    
    # Validate tools directory (warning only, not enforced yet)
    if config.tools.enabled:
        tools_path = Path(config.tools.dir)
        if not tools_path.exists():
            warnings.append(
                f"Tools directory not found: {config.tools.dir}\n"
                f"Note: Custom tools are not yet implemented, this is a placeholder."
            )
    
    # Print warnings
    for warning in warnings:
        print(f"WARNING: {warning}")
    
    # Raise errors if any
    if errors:
        raise ValueError(
            "Configuration validation failed:\n" + "\n".join(errors)
        )


def validate_provider_credentials(config: AppConfig) -> None:
    """
    Validate that selected provider has required credentials.
    
    This is already handled by Pydantic validators, but kept as
    a separate function for future enhancements (e.g., testing
    provider connectivity).
    
    Args:
        config: Validated AppConfig instance
    """
    # Provider existence is already validated by Pydantic
    # This function is a placeholder for future provider health checks
    pass


def get_available_providers(config: AppConfig) -> Set[str]:
    """
    Get set of available provider names.
    
    Args:
        config: Validated AppConfig instance
        
    Returns:
        Set of provider names
    """
    return set(config.providers.keys())


def get_enabled_capabilities(config: AppConfig) -> Dict[str, List[str]]:
    """
    Get dictionary of enabled capabilities.
    
    Returns:
        Dictionary with keys: 'skills', 'tools', 'plugins'
    """
    return {
        "skills": config.skills.enabled,
        "tools": config.tools.enabled,
        "plugins": config.plugins.enabled,
    }
