# mcp/server.py
import logging
import sys

from mcp.server.fastmcp import FastMCP

from core.config import load_config
from tools.registry import execute_bash

# Standard out must be kept clean for JSON-RPC messages. Log to stderr only.
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("idolhub.mcp")

def create_mcp_server() -> FastMCP:
    cfg = load_config()
    mcp = FastMCP(cfg.app.name)
    
    # Expose sandbox tool
    @mcp.tool(name="execute_bash")
    def mcp_execute_bash(command: str) -> str:
        """Menjalankan bash command di Linux host system (Ubuntu). Command berjalan secara aman di dalam Sandbox (Workspace directory)."""
        logger.info(f"MCP Tool call 'execute_bash' received: {command}")
        return execute_bash(command)
        
    return mcp

def run_mcp_server():
    logger.info("Starting idolhub MCP server over stdio transport...")
    server = create_mcp_server()
    server.run(transport="stdio")
