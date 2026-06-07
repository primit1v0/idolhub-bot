import importlib.util
import logging
import os
import sys

from core.event_bus import EventBus

logger = logging.getLogger("idolhub.plugins")

EVENTS = ["before_message", "after_message", "before_reply", "after_reply", "on_error", "on_tool_call"]

def register_plugin_to_bus(plugin_instance, event_bus: EventBus):
    for event_name in EVENTS:
        method = getattr(plugin_instance, event_name, None)
        if method and callable(method):
            event_bus.subscribe(event_name, method)
            logger.info(f"Subscribed method '{method.__name__}' of {type(plugin_instance).__name__} to '{event_name}'")

def load_plugins(plugins_dir: str, event_bus: EventBus):
    if not os.path.exists(plugins_dir):
        logger.warning(f"Plugins directory {plugins_dir} does not exist.")
        return
        
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py" and filename != "loader.py":
            module_name = f"plugins.{filename[:-3]}"
            file_path = os.path.join(plugins_dir, filename)
            
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[module_name] = module
                    spec.loader.exec_module(module)
                    
                    for attr_name in dir(module):
                          attr = getattr(module, attr_name)
                          if isinstance(attr, type) and attr.__module__ == module_name:
                              plugin_instance = attr()
                              register_plugin_to_bus(plugin_instance, event_bus)
                              logger.info(f"Loaded plugin class {attr_name} from {filename}")
            except Exception as e:
                logger.error(f"Failed to load plugin {filename}: {e}", exc_info=True)
