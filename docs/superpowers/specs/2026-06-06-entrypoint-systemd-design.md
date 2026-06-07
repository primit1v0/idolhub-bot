# idolhub — Main Entrypoint & Systemd Service Integration Spec

> **Historical status: Implemented with later configuration-policy changes.**
>
> Current behavior and status are defined in
> [`docs/BASELINE.md`](../../BASELINE.md). References that treat `config.json`
> as a tracked repository file are obsolete: it is now local-only and ignored.
> Any phase numbering is local to this historical work item.

**Date:** 2026-06-06  
**Status:** Approved ✅

---

## 1. Overview

Spesifikasi ini mendefinisikan perubahan untuk menyelesaikan integrasi backend API dan server MCP ke dalam entrypoint utama (`main.py`) serta pembuatan template konfigurasi systemd untuk kedua mode tersebut.

---

## 2. CLI Argument Support & Lazy Imports

Untuk meminimalkan jejak memori (memory footprint) dan mendukung konfigurasi yang fleksibel, entrypoint utama (`main.py`) akan mendukung pemilihan mode melalui argumen command-line:

- `python main.py bot`
- `python main.py api`
- `python main.py mcp`

Jika argumen tidak diberikan, aplikasi akan fallback ke konfigurasi `app.mode` dari `config.json`.

Untuk mematuhi prinsip **Zero Bloat**, dependency untuk mode API (`uvicorn`, `api.server`) dan mode MCP (`mcp_server.server`) akan diimpor secara dinamis (lazy import) hanya saat mode tersebut diaktifkan.

---

## 3. Detail Perubahan Kode

### 3.1 `main.py`
```python
import sys
import logging
from core.config import load_config
from core.bot import TelegramBot

# ... setup_logging ...

def main():
    try:
        cfg = load_config("config.json")
    except KeyError as e:
        print(f"CRITICAL ERROR: Secret untuk {e} tidak ditemukan di environment!")
        sys.exit(1)
    except Exception as e:
        print(f"CRITICAL ERROR: Gagal memuat config: {e}")
        sys.exit(1)

    setup_logging(cfg.logging.level, cfg.logging.format)
    logger = logging.getLogger("idolhub")
    
    # Resolusi mode: CLI argument -> config.json
    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()
    else:
        mode = cfg.app.mode

    logger.info(f"Memulai idolhub dalam mode: {mode.upper()}")

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
```

---

## 4. Systemd Service Templates

Dua berkas template baru akan dibuat di direktori `systemd/`:

### 4.1 `systemd/idolhub-api.service.template`
```ini
[Unit]
Description=idolhub REST API Server
Documentation=https://github.com/primit1v0/idolhub-bot
After=network.target

[Service]
Type=simple
User=@IDOLHUB_USER@
WorkingDirectory=@IDOLHUB_DIR@
EnvironmentFile=@IDOLHUB_ENV_FILE@
ExecStart=@IDOLHUB_DIR@/.venv/bin/python main.py api
Restart=on-failure
RestartSec=5
StartLimitInterval=60
StartLimitBurst=3

StandardOutput=journal
StandardError=journal
SyslogIdentifier=idolhub-api

[Install]
WantedBy=default.target
```

### 4.2 `systemd/idolhub-mcp.service.template`
```ini
[Unit]
Description=idolhub MCP stdio Server
Documentation=https://github.com/primit1v0/idolhub-bot
After=network.target

[Service]
Type=simple
User=@IDOLHUB_USER@
WorkingDirectory=@IDOLHUB_DIR@
EnvironmentFile=@IDOLHUB_ENV_FILE@
ExecStart=@IDOLHUB_DIR@/.venv/bin/python main.py mcp
Restart=on-failure
RestartSec=5
StartLimitInterval=60
StartLimitBurst=3

StandardOutput=journal
StandardError=journal
SyslogIdentifier=idolhub-mcp

[Install]
WantedBy=default.target
```

---

## 5. Verification Plan

Untuk memverifikasi integrasi:
1. Jalankan unit test pytest untuk memastikan tidak ada pemecahan kompatibilitas.
2. Tambahkan unit test baru di `tests/test_config.py` atau file test baru untuk memverifikasi override mode via `sys.argv`.
