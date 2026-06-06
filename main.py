import sys
import logging
from core.config import load_config
from core.bot import TelegramBot

def setup_logging(level_str: str, format_str: str):
    numeric_level = getattr(logging, level_str.upper(), logging.INFO)
    
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
        cfg = load_config("config.json")
    except KeyError as e:
        print(f"CRITICAL ERROR: Secret untuk {e} tidak ditemukan di environment!")
        print("Pastikan /etc/idolhub/idolhub.env sudah diisi dan di-export.")
        sys.exit(1)
    except Exception as e:
        print(f"CRITICAL ERROR: Gagal memuat config: {e}")
        sys.exit(1)

    # 2. Setup Logging
    setup_logging(cfg.logging.level, cfg.logging.format)
    logger = logging.getLogger("idolhub")
    
    # 3. Determine Mode (CLI overrides config)
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        mode = cfg.app.mode
        
    logger.info(f"Memulai idolhub dalam mode: {mode.upper()}")

    # 4. Dispatch Mode
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
        sys.exit(1)

if __name__ == "__main__":
    main()
