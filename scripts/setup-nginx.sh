#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"
if [[ "$MODE" != "dev" && "$MODE" != "play" ]]; then
  echo "Usage: $0 dev|play"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT_DIR/infra/nginx/typing-game.local.$MODE.conf"
TARGET="/usr/local/etc/nginx/servers/typing-game.local.conf"
SSL_DIR="/usr/local/etc/nginx/ssl/typing-game.local"
CERT="$SSL_DIR/typing-game.local.pem"
KEY="$SSL_DIR/typing-game.local-key.pem"

ensure_hosts() {
  if ! grep -qE '(^|[[:space:]])recall\.typing-game\.local([[:space:]]|$)' /etc/hosts; then
    echo "Adding recall.typing-game.local to /etc/hosts..."
    echo "127.0.0.1 recall.typing-game.local" | sudo tee -a /etc/hosts >/dev/null
  fi
}

certificate_has_recall_host() {
  [[ -f "$CERT" ]] &&
    openssl x509 -in "$CERT" -noout -text 2>/dev/null |
      grep -q "DNS:recall.typing-game.local"
}

create_certificate() {
  if ! command -v mkcert >/dev/null 2>&1; then
    echo "mkcert is not installed or not in PATH."
    exit 1
  fi

  echo "Creating local TLS certificate for all typing-game hosts..."
  local temp_dir
  temp_dir="$(mktemp -d)"

  mkcert \
    -cert-file "$temp_dir/typing-game.local.pem" \
    -key-file "$temp_dir/typing-game.local-key.pem" \
    typing-game.local \
    monkeytype.typing-game.local \
    shooter.typing-game.local \
    recall.typing-game.local

  sudo mkdir -p "$SSL_DIR"
  sudo cp "$temp_dir/typing-game.local.pem" "$CERT"
  sudo cp "$temp_dir/typing-game.local-key.pem" "$KEY"
  rm -rf "$temp_dir"
}

ensure_hosts
if [[ ! -f "$CERT" || ! -f "$KEY" ]] || ! certificate_has_recall_host; then
  create_certificate
fi

sudo mkdir -p "$(dirname "$TARGET")"
sudo cp "$SOURCE" "$TARGET"

NGINX_BIN="$(command -v nginx || true)"
if [[ -z "$NGINX_BIN" ]]; then
  echo "nginx is not installed or not in PATH."
  exit 1
fi

"$NGINX_BIN" -t
brew services restart nginx
echo "nginx switched to $MODE mode."
