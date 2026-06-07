"""
Atomic configuration reloader with rollback support.

This module provides:
- Atomic configuration reload without restart
- Validation before applying changes
- Automatic rollback on validation failure
- Event system for config change notifications
- Thread-safe config access
"""

import asyncio
import threading
from typing import Callable, List, Optional, Tuple

from core.config_schema import AppConfig
from core.config_validator import load_config

# Global state
_current_config: Optional[AppConfig] = None
_config_lock = threading.RLock()
_change_handlers: List[Callable[[AppConfig], None]] = []


def initialize_config(path: str = "config.json") -> AppConfig:
    """
    Initialize configuration at startup.
    
    This must be called once at application startup before any
    other config operations.
    
    Args:
        path: Path to configuration file
        
    Returns:
        Loaded and validated configuration
        
    Raises:
        ValueError: If configuration is invalid
    """
    global _current_config
    
    with _config_lock:
        config = load_config(path)
        _current_config = config
        return config


def get_current_config() -> AppConfig:
    """
    Get current active configuration.
    
    Returns:
        Current AppConfig instance
        
    Raises:
        RuntimeError: If config not initialized
    """
    with _config_lock:
        if _current_config is None:
            raise RuntimeError(
                "Configuration not initialized. "
                "Call initialize_config() at startup."
            )
        return _current_config


async def reload_config(path: str = "config.json") -> Tuple[bool, str]:
    """
    Reload configuration atomically.
    
    Steps:
    1. Load new config from file
    2. Validate fully (schema + whitelists)
    3. If valid, swap atomically
    4. Notify change handlers
    5. If invalid, rollback (keep current config)
    
    Args:
        path: Path to configuration file
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    global _current_config
    
    # Get current config for rollback
    with _config_lock:
        old_config = _current_config
    
    try:
        # Load and validate new config
        new_config = load_config(path)
        
        # Atomic swap
        with _config_lock:
            _current_config = new_config
        
        # Notify handlers (async)
        await _notify_change_handlers(new_config)
        
        return True, "Configuration reloaded successfully"
        
    except FileNotFoundError as e:
        return False, f"Configuration file not found: {e}"
        
    except ValueError as e:
        # Validation failed, rollback
        with _config_lock:
            _current_config = old_config
        return False, f"Configuration validation failed: {e}"
        
    except Exception as e:
        # Unexpected error, rollback
        with _config_lock:
            _current_config = old_config
        return False, f"Configuration reload failed: {e}"


def reload_config_sync(path: str = "config.json") -> Tuple[bool, str]:
    """
    Synchronous version of reload_config.
    
    Use this in non-async contexts (e.g., signal handlers).
    
    Args:
        path: Path to configuration file
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    global _current_config
    
    with _config_lock:
        old_config = _current_config
    
    try:
        new_config = load_config(path)
        
        with _config_lock:
            _current_config = new_config
        
        # Notify handlers synchronously
        _notify_change_handlers_sync(new_config)
        
        return True, "Configuration reloaded successfully"
        
    except FileNotFoundError as e:
        return False, f"Configuration file not found: {e}"
        
    except ValueError as e:
        with _config_lock:
            _current_config = old_config
        return False, f"Configuration validation failed: {e}"
        
    except Exception as e:
        with _config_lock:
            _current_config = old_config
        return False, f"Configuration reload failed: {e}"


def register_change_handler(handler: Callable[[AppConfig], None]) -> None:
    """
    Register a callback for configuration changes.
    
    Handler will be called with the new config after successful reload.
    Handlers should be fast and non-blocking.
    
    Args:
        handler: Callback function that takes AppConfig
    """
    with _config_lock:
        if handler not in _change_handlers:
            _change_handlers.append(handler)


def unregister_change_handler(handler: Callable[[AppConfig], None]) -> None:
    """
    Unregister a configuration change callback.
    
    Args:
        handler: Previously registered callback function
    """
    with _config_lock:
        if handler in _change_handlers:
            _change_handlers.remove(handler)


async def _notify_change_handlers(config: AppConfig) -> None:
    """
    Notify all registered handlers of config change (async).
    
    Handlers are called in order of registration.
    Exceptions in handlers are caught and logged but don't affect reload.
    """
    with _config_lock:
        handlers = _change_handlers.copy()
    
    for handler in handlers:
        try:
            # Check if handler is async
            if asyncio.iscoroutinefunction(handler):
                await handler(config)
            else:
                handler(config)
        except Exception as e:
            # Log error but continue with other handlers
            print(f"Error in config change handler {handler.__name__}: {e}")


def _notify_change_handlers_sync(config: AppConfig) -> None:
    """
    Notify all registered handlers of config change (sync).
    
    Used by reload_config_sync.
    """
    with _config_lock:
        handlers = _change_handlers.copy()
    
    for handler in handlers:
        try:
            handler(config)
        except Exception as e:
            print(f"Error in config change handler {handler.__name__}: {e}")


def clear_change_handlers() -> None:
    """
    Clear all registered change handlers.
    
    Useful for testing.
    """
    with _config_lock:
        _change_handlers.clear()
