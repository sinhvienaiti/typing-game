#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"
if [[ "$MODE" != "dev" && "$MODE" != "play" ]]; then
  echo "Usage: $0 dev|play"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
source "$ROOT_DIR/scripts/local-env.sh"
SOURCE="$ROOT_DIR/infra/nginx/typing-game.local.$MODE.conf"

case "$(uname -s)" in
  Darwin)
    PLATFORM="macos"
    BREW_PREFIX="$(brew --prefix)"
    NGINX_BIN="$BREW_PREFIX/bin/nginx"
    NGINX_BASE="$BREW_PREFIX/etc/nginx"
    TARGET="$NGINX_BASE/servers/typing-game.local.conf"
    SSL_DIR="$NGINX_BASE/ssl/typing-game.local"
    ;;
  Linux)
    PLATFORM="linux"
    NGINX_BASE="/etc/nginx"
    TARGET="$NGINX_BASE/conf.d/typing-game.local.conf"
    SSL_DIR="$NGINX_BASE/ssl/typing-game.local"
    ;;
  *)
    echo "Unsupported platform: $(uname -s)"
    exit 1
    ;;
esac

CERT="$SSL_DIR/typing-game.local.pem"
KEY="$SSL_DIR/typing-game.local-key.pem"

HOSTS=(
  "typing-game.local"
  "monkeytype.typing-game.local"
  "shooter.typing-game.local"
  "recall.typing-game.local"
  "karaoke.typing-game.local"
  "space.typing-game.local"
  "dragon.typing-game.local"
  "td.typing-game.local"
  "survival.typing-game.local"
  "tutien.typing-game.local"
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

migrate_legacy_linux_certificate() {
  [[ "$PLATFORM" == "linux" ]] || return 1

  local legacy_dir="/usr/local/etc/nginx/ssl/typing-game.local"
  local legacy_cert="$legacy_dir/typing-game.local.pem"
  local legacy_key="$legacy_dir/typing-game.local-key.pem"

  if ! sudo test -f "$legacy_cert" || ! sudo test -f "$legacy_key"; then
    return 1
  fi

  echo "Migrating existing typing-game TLS certificate into Linux nginx path..."
  sudo mkdir -p "$SSL_DIR"
  sudo cp "$legacy_cert" "$CERT"
  sudo cp "$legacy_key" "$KEY"
  sudo chown root:root "$CERT" "$KEY"
  sudo chmod 644 "$CERT"
  sudo chmod 600 "$KEY"
  return 0
}

create_certificate() {
  if ! command -v mkcert >/dev/null 2>&1; then
    echo "mkcert is not installed or not in PATH."
    echo "Install mkcert, then rerun ./play.sh."
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

  if [[ "$PLATFORM" == "linux" ]]; then
    sudo mkdir -p "$SSL_DIR"
    sudo cp "$temp_dir/typing-game.local.pem" "$CERT"
    sudo cp "$temp_dir/typing-game.local-key.pem" "$KEY"
    sudo chown root:root "$CERT" "$KEY"
    sudo chmod 644 "$CERT"
    sudo chmod 600 "$KEY"
  else
    mkdir -p "$SSL_DIR"
    cp "$temp_dir/typing-game.local.pem" "$CERT"
    cp "$temp_dir/typing-game.local-key.pem" "$KEY"
    chmod 644 "$CERT"
    chmod 600 "$KEY"
  fi

  rm -rf "$temp_dir"
}

render_config() {
  local destination="$1"
  sed \
    -e "s|__ROOT_DIR__|$ROOT_DIR|g" \
    -e "s|__SSL_CERT__|$CERT|g" \
    -e "s|__SSL_KEY__|$KEY|g" \
    "$SOURCE" > "$destination"
}

macos_nginx_running() {
  local pid_file="$BREW_PREFIX/var/run/nginx.pid"
  local nginx_pid=""
  [[ -r "$pid_file" ]] || return 1
  read -r nginx_pid < "$pid_file" || true
  [[ "$nginx_pid" =~ ^[0-9]+$ ]] || return 1
  local process
  process="$(ps -p "$nginx_pid" -o comm= 2>/dev/null)" || return 1
  [[ "$process" == *"nginx: master process "* || "$process" == */nginx ]]
}

restart_nginx() {
  if [[ "$PLATFORM" == "macos" ]]; then
    local state_dir="$ROOT_DIR/.local/nginx"
    local state_file="$state_dir/applied-config.sha256"
    local signature
    signature="$(shasum -a 256 "$TARGET" "$CERT" "$NGINX_BASE/nginx.conf" | shasum -a 256 | awk '{print $1}')"
    if [[ -r "$state_file" ]] && [[ "$(cat "$state_file")" == "$signature" ]] && macos_nginx_running; then
      return
    fi
    sudo "$NGINX_BIN" -t
    if macos_nginx_running; then
      sudo "$NGINX_BIN" -s reload
    else
      sudo "$NGINX_BIN"
    fi
    mkdir -p "$state_dir"
    printf '%s\n' "$signature" > "$state_file"
    return
  fi

  sudo nginx -t
  if command -v systemctl >/dev/null 2>&1; then
    sudo systemctl restart nginx 2>/dev/null || sudo service nginx restart
  else
    sudo service nginx restart
  fi
}

ensure_hosts

if [[ ! -f "$KEY" ]] || ! certificate_has_all_hosts; then
  if ! migrate_legacy_linux_certificate || ! certificate_has_all_hosts; then
    create_certificate
  fi
fi

temp_config="$(mktemp)"
trap 'rm -f "$temp_config"' EXIT
render_config "$temp_config"

if [[ "$PLATFORM" == "linux" ]]; then
  sudo mkdir -p "$(dirname "$TARGET")"
  if ! sudo test -f "$TARGET" || ! sudo cmp -s "$temp_config" "$TARGET"; then
    sudo cp "$temp_config" "$TARGET"
    restart_nginx
    echo "nginx switched to $MODE mode ($PLATFORM)."
  else
    sudo nginx -t >/dev/null
    sudo service nginx start >/dev/null 2>&1 || true
    echo "nginx is already in $MODE mode ($PLATFORM)."
  fi
else
  mkdir -p "$(dirname "$TARGET")"
  if [[ ! -f "$TARGET" ]] || ! cmp -s "$temp_config" "$TARGET"; then
    if [[ -f "$TARGET" ]]; then
      mkdir -p "$NGINX_BASE/backups"
      cp -p "$TARGET" "$NGINX_BASE/backups/$(basename "$TARGET").$(date +%Y%m%d-%H%M%S)"
    fi
    cp "$temp_config" "$TARGET"
    restart_nginx
    echo "nginx switched to $MODE mode ($PLATFORM)."
  else
    restart_nginx
    echo "nginx is already in $MODE mode ($PLATFORM)."
  fi
fi
