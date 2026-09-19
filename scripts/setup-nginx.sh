#!/usr/bin/env bash
set -euo pipefail
MODE="${1:-}"
if [[ "$MODE" != "dev" && "$MODE" != "play" ]]; then echo "Usage: $0 dev|play"; exit 1; fi
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT_DIR/infra/nginx/typing-game.local.$MODE.conf"
TARGET="/usr/local/etc/nginx/servers/typing-game.local.conf"
CERT="/usr/local/etc/nginx/ssl/typing-game.local/typing-game.local.pem"
KEY="/usr/local/etc/nginx/ssl/typing-game.local/typing-game.local-key.pem"
if [[ ! -f "$CERT" || ! -f "$KEY" ]]; then echo "TLS certificate not found. Create it with mkcert first."; exit 1; fi
sudo mkdir -p "$(dirname "$TARGET")"
sudo cp "$SOURCE" "$TARGET"
NGINX_BIN="$(command -v nginx || true)"
if [[ -z "$NGINX_BIN" ]]; then echo "nginx is not installed or not in PATH."; exit 1; fi
"$NGINX_BIN" -t
brew services restart nginx
echo "nginx switched to $MODE mode."
