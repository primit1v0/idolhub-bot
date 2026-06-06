#!/usr/bin/env python3
"""
idolhub — Personal Assistant Entry Point
Usage:
  python main.py          # default: bot mode
  python main.py bot      # Telegram bot
  python main.py api      # FastAPI REST server
  python main.py mcp      # MCP server
"""

import sys
import asyncio
from core.config import load_config


def main():
    config = load_config()
    mode = sys.argv[1] if len(sys.argv) > 1 else config.app.mode

    if mode == "bot":
        from core.bot import start_bot
        asyncio.run(start_bot(config))
    elif mode == "api":
        from api.server import start_api
        start_api(config)
    elif mode == "mcp":
        from mcp.server import start_mcp
        asyncio.run(start_mcp(config))
    else:
        print(f"Unknown mode: {mode}. Use: bot | api | mcp")
        sys.exit(1)


if __name__ == "__main__":
    main()
