import inspect
import logging

logger = logging.getLogger("idolhub.event_bus")

class EventBus:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event_name: str, callback):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(callback)

    async def emit(self, event_name: str, ctx: dict):
        if event_name not in self._listeners:
            return
        for callback in self._listeners[event_name]:
            try:
                if inspect.iscoroutinefunction(callback):
                    await callback(ctx)
                else:
                    callback(ctx)
            except Exception as e:
                logger.error(f"Error in listener for {event_name}: {e}", exc_info=True)
