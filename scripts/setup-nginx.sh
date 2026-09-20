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

HOSTS=(
  "typing-game.local"
  "monkeytype.typing-game.local"
  "shooter.typing-game.local"
  "recall.typing-game.local"
  "karaoke.typing-game.local"
)

ensure_hosts() {
  local host
  for host in "${HOSTS[@]}"; do
    if ! grep -qE "(^|[[:space:]])${host//./\\.}([[:space:]]|$)" /etc/hosts; then
      echo "Adding $host to /etc/hosts..."
      echo "127.0.0.1 $host" | sudo tee -a /etc/hosts >/dev/null
    fi
  done
}

certificate_has_all_hosts() {
  [[ -f "$CERT" ]] || return 1

  local certificate_text
  certificate_text="$(openssl x509 -in "$CERT" -noout -text 2>/dev/null)" || return 1

  local host
  for host in "${HOSTS[@]}"; do
    if ! grep -q "DNS:$host" <<<"$certificate_text"; then
      return 1
    fi
  done
}

create_certificate() {
  if ! command -v mkcert >/dev/null 2>&1; then
    echo "mkcert is not installed or not in PATH."
    exit 1
  fi

  echo "Ensuring the local mkcert CA is installed..."
  mkcert -install

  echo "Creating local TLS certificate for all typing-game hosts..."
  local temp_dir
  temp_dir="$(mktemp -d)"

  mkcert \
    -cert-file "$temp_dir/typing-game.local.pem" \
    -key-file "$temp_dir/typing-game.local-key.pem" \
    "${HOSTS[@]}"

  sudo mkdir -p "$SSL_DIR"
  sudo cp "$temp_dir/typing-game.local.pem" "$CERT"
  sudo cp "$temp_dir/typing-game.local-key.pem" "$KEY"
  rm -rf "$temp_dir"
}

ensure_hosts

if [[ ! -f "$KEY" ]] || ! certificate_has_all_hosts; then
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
