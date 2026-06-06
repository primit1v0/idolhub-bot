#!/usr/bin/env bash
# =============================================================================
# idolhub setup.sh — Persiapan environment pertama kali
# Jalankan sebagai root: sudo bash scripts/setup.sh
# =============================================================================

set -euo pipefail

SECRETS_DIR="/etc/idolhub"
SECRETS_FILE="${SECRETS_DIR}/secrets.env"
SERVICE_SRC="$(dirname "$0")/../systemd/idolhub.service.template"
SERVICE_DEST="/etc/systemd/system/idolhub.service"
VENV_DIR="$(dirname "$0")/../.venv"
PROJECT_DIR="$(dirname "$0")/.."

echo "=== idolhub Setup ==="

# 1. Buat direktori secrets
if [ ! -d "$SECRETS_DIR" ]; then
    echo "[+] Membuat $SECRETS_DIR ..."
    mkdir -p "$SECRETS_DIR"
    chmod 700 "$SECRETS_DIR"
fi

# 2. Buat secrets.env template jika belum ada
if [ ! -f "$SECRETS_FILE" ]; then
    echo "[+] Membuat $SECRETS_FILE template ..."
    cat > "$SECRETS_FILE" << 'EOF'
# /etc/idolhub/secrets.env
# Isi dengan nilai yang sebenarnya, lalu: chmod 600 /etc/idolhub/secrets.env

TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
OPENAI_API_KEY=REPLACE_ME
OPENAI_BASE_URL=https://api.openai.com/v1
GITHUB_CODEX_TOKEN=your-github-codex-oauth-token
GITHUB_COPILOT_TOKEN=your-github-copilot-cli-token
EOF
    chmod 600 "$SECRETS_FILE"
    echo "[!] Edit $SECRETS_FILE dan isi dengan nilai yang benar sebelum menjalankan service"
fi

# 3. Install systemd service
if [ -f "$SERVICE_SRC" ]; then
    echo "[+] Install systemd service ..."
    cp "$SERVICE_SRC" "$SERVICE_DEST"
    systemctl daemon-reload
    echo "[+] Service installed: $SERVICE_DEST"
    echo "    Aktifkan dengan: sudo systemctl enable --now idolhub"
fi

# 4. Setup uv dan venv
if ! command -v uv &>/dev/null; then
    echo "[+] Install uv ..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

echo "[+] Membuat virtual environment dengan uv ..."
cd "$PROJECT_DIR"
uv venv .venv
uv sync

echo ""
echo "=== Setup selesai ==="
echo "Langkah berikutnya:"
echo "  1. Edit /etc/idolhub/secrets.env — isi semua token yang diperlukan"
echo "  2. sudo systemctl enable --now idolhub"
echo "  3. journalctl -u idolhub -f   # monitor log"
