import logging
import sys

from core.bot import TelegramBot
from core.config_reloader import initialize_config


def setup_logging(level_str: str, format_str: str, debug: bool = False):
    """Setup logging with optional debug mode."""
    numeric_level = getattr(logging, level_str.upper(), logging.INFO)
    
    # Override to DEBUG if debug flag is set
    if debug:
        numeric_level = logging.DEBUG
    
    if format_str.lower() == "json":
        # Simplified JSON logging for systemd
        log_format = '{"time": "%(asctime)s", "level": "%(levelname)s", "msg": "%(message)s"}'
    else:
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logging.basicConfig(
        format=log_format,
        level=numeric_level
    )
    # Reduce noise from httpx
    logging.getLogger("httpx").setLevel(logging.WARNING)


def main():
    # 1. Load Config & Resolve Env (Fail-fast jika ada yang kurang)
    try:
        cfg = initialize_config("config.json")
    except KeyError as e:
        print(f"CRITICAL ERROR: Secret untuk {e} tidak ditemukan di environment!")
        print("Pastikan environment atau EnvironmentFile lokal sudah diisi.")
        sys.exit(1)
    except Exception as e:
        print(f"CRITICAL ERROR: Gagal memuat config: {e}")
        sys.exit(1)

    # 2. Setup Logging (with debug flag enforcement)
    setup_logging(cfg.logging.level, cfg.logging.format, cfg.app.debug)
    logger = logging.getLogger("idolhub")
    
    if cfg.app.debug:
        logger.debug("Debug mode enabled - verbose logging active")
    
    # 3. Determine Mode (CLI overrides config)
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        mode = cfg.app.mode
    
    # 4. Validate mode is enabled
    if mode == "api" and not cfg.api.enabled:
        logger.error("Cannot run in 'api' mode: api.enabled is False in config")
        logger.error("Set api.enabled to true or change mode to 'bot' or 'mcp'")
        sys.exit(1)
    
    if mode == "mcp" and not cfg.mcp.enabled:
        logger.error("Cannot run in 'mcp' mode: mcp.enabled is False in config")
        logger.error("Set mcp.enabled to true or change mode to 'bot' or 'api'")
        sys.exit(1)
        
    logger.info(f"Memulai idolhub dalam mode: {mode.upper()}")

    # 5. Dispatch Mode
    if mode == "bot":
        try:
            bot = TelegramBot(cfg)
            bot.run()
        except ValueError as e:
            logger.error(f"Setup Error: {e}")
            sys.exit(1)
    elif mode == "api":
        import uvicorn
        logger.info(f"Starting FastAPI server on {cfg.api.host}:{cfg.api.port}...")
        uvicorn.run("api.server:app", host=cfg.api.host, port=cfg.api.port, reload=False)
    elif mode == "mcp":
        from mcp_server.server import run_mcp_server
        logger.info("Starting MCP stdio server...")
        run_mcp_server()
    else:
        logger.error(f"Mode tidak dikenal: {mode}")
        logger.error("Mode yang valid: bot, api, mcp")
        sys.exit(1)


if __name__ == "__main__":
    main()