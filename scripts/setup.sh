#!/usr/bin/env bash
# =============================================================================
# idolhub setup.sh — Persiapan environment pertama kali
# Jalankan sebagai root: sudo bash scripts/setup.sh
# =============================================================================

set -euo pipefail

if [ "${EUID}" -ne 0 ]; then
    echo "Jalankan setup melalui sudo." >&2
    exit 1
fi

IDOLHUB_USER="${IDOLHUB_USER:-${SUDO_USER:-}}"
if [ -z "$IDOLHUB_USER" ] || [ "$IDOLHUB_USER" = "root" ]; then
    echo "Target user tidak terdeteksi. Jalankan dengan sudo atau set IDOLHUB_USER." >&2
    exit 1
fi

IDOLHUB_GROUP="$(id -gn "$IDOLHUB_USER")"
IDOLHUB_HOME="$(getent passwd "$IDOLHUB_USER" | cut -d: -f6)"
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SECRETS_DIR="${IDOLHUB_HOME}/.config/idolhub"
SECRETS_FILE="${SECRETS_DIR}/.env"
SERVICE_SRC="${PROJECT_DIR}/systemd/idolhub.service.template"
SERVICE_DEST="/etc/systemd/system/idolhub.service"
CONFIG_FILE="${PROJECT_DIR}/config.json"
CONFIG_EXAMPLE="${PROJECT_DIR}/config.example.json"

echo "=== idolhub Setup ==="

# 1. Buat direktori secrets
if [ ! -d "$SECRETS_DIR" ]; then
    echo "[+] Membuat $SECRETS_DIR ..."
    mkdir -p "$SECRETS_DIR"
    chmod 700 "$SECRETS_DIR"
    chown "$IDOLHUB_USER:$IDOLHUB_GROUP" "$SECRETS_DIR"
fi

# 2. Buat environment template jika belum ada
if [ ! -f "$SECRETS_FILE" ]; then
    echo "[+] Membuat $SECRETS_FILE template ..."
    cat > "$SECRETS_FILE" << EOF
# ${SECRETS_FILE}
# Isi dengan nilai sebenarnya. File ini tidak boleh masuk repository.

TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
GEMINI_API_KEY=your-gemini-api-key-here
OPENAI_API_KEY=REPLACE_ME
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_CODEX_TOKEN=your-openai-codex-oauth-token
GITHUB_COPILOT_TOKEN=your-github-copilot-cli-token
EOF
    chmod 600 "$SECRETS_FILE"
    chown "$IDOLHUB_USER:$IDOLHUB_GROUP" "$SECRETS_FILE"
    echo "[!] Edit $SECRETS_FILE dan isi dengan nilai yang benar sebelum menjalankan service"
fi

# 3. Buat config lokal dari template jika belum ada
if [ ! -f "$CONFIG_FILE" ]; then
    echo "[+] Membuat config.json lokal dari config.example.json ..."
    cp "$CONFIG_EXAMPLE" "$CONFIG_FILE"
    chown "$IDOLHUB_USER:$IDOLHUB_GROUP" "$CONFIG_FILE"
fi

# 4. Install systemd service
if [ -f "$SERVICE_SRC" ]; then
    echo "[+] Install systemd service ..."
    sed \
        -e "s|@IDOLHUB_USER@|${IDOLHUB_USER}|g" \
        -e "s|@IDOLHUB_GROUP@|${IDOLHUB_GROUP}|g" \
        -e "s|@IDOLHUB_DIR@|${PROJECT_DIR}|g" \
        -e "s|@IDOLHUB_ENV_FILE@|${SECRETS_FILE}|g" \
        "$SERVICE_SRC" > "$SERVICE_DEST"
    systemctl daemon-reload
    echo "[+] Service installed: $SERVICE_DEST"
    echo "    Aktifkan dengan: sudo systemctl enable --now idolhub"
fi

# 5. Setup uv dan venv
UV_BIN="$(command -v uv || true)"
if [ -z "$UV_BIN" ] && [ -x "${IDOLHUB_HOME}/.local/bin/uv" ]; then
    UV_BIN="${IDOLHUB_HOME}/.local/bin/uv"
fi

if [ -z "$UV_BIN" ]; then
    echo "[+] Install uv ..."
    sudo -u "$IDOLHUB_USER" env HOME="$IDOLHUB_HOME" \
        sh -c 'curl -LsSf https://astral.sh/uv/install.sh | sh'
    for candidate in \
        "${IDOLHUB_HOME}/.local/bin/uv" \
        "${IDOLHUB_HOME}/.cargo/bin/uv"
    do
        if [ -x "$candidate" ]; then
            UV_BIN="$candidate"
            break
        fi
    done
fi

if [ -z "$UV_BIN" ]; then
    echo "uv tidak ditemukan setelah instalasi." >&2
    exit 1
fi

echo "[+] Membuat virtual environment dengan uv ..."
cd "$PROJECT_DIR"
sudo -u "$IDOLHUB_USER" env HOME="$IDOLHUB_HOME" "$UV_BIN" venv .venv
sudo -u "$IDOLHUB_USER" env HOME="$IDOLHUB_HOME" "$UV_BIN" sync

echo ""
echo "=== Setup selesai ==="
echo "Langkah berikutnya:"
echo "  1. Edit $CONFIG_FILE — sisakan hanya provider yang digunakan"
echo "  2. Edit $SECRETS_FILE — isi variable yang dirujuk config.json"
echo "  3. sudo systemctl enable --now idolhub"
echo "  4. journalctl -u idolhub -f   # monitor log"
