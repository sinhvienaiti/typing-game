#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"
source "$ROOT_DIR/scripts/local-env.sh"
# Local Play keeps the private announcer/music files and the Admin QA Sandbox (Test Lab).
# Public builds leave both out: see "Build flags" in games/space-typing/README.md.
export SPACE_LOCAL_ASSETS=1 SPACE_TEST_LAB=1

case "${1:-}" in
  "")
    ;;
  -h|--help|help)
    echo "Usage: ./play.sh"
    echo
    echo "Play mode does not pull Git, update submodules, or install dependencies."
    echo "It automatically refreshes local Space Typing source art, prepares the"
    echo "verified offline Voice model when needed, refreshes stale static builds,"
    echo "starts the Admin runtime bridge, switches nginx to static Play mode,"
    echo "and opens https://typing-game.local."
    exit 0
    ;;
  *)
    echo "Unknown argument: $1"
    echo "Usage: ./play.sh"
    exit 1
    ;;
esac

needs_build() {
  local output="$1"
  shift

  if [[ ! -f "$output" ]]; then
    return 0
  fi

  local source
  for source in "$@"; do
    [[ -e "$source" ]] || continue

    if [[ -f "$source" ]]; then
      if [[ "$source" -nt "$output" ]]; then
        return 0
      fi
      continue
    fi

    while IFS= read -r -d '' file; do
      if [[ "$file" -nt "$output" ]]; then
        return 0
      fi
    done < <(
      find "$source" \
        \( -type d \( \
          -name node_modules -o \
          -name dist -o \
          -name .git -o \
          -name .turbo -o \
          -name coverage \
        \) -prune \) \
        -o -type f -print0
    )
  done

  return 1
}

build_if_needed() {
  local name="$1"
  local output="$2"
  local script="$3"
  shift 3

  if ! needs_build "$output" "$@"; then
    echo "  ✓ $name static build is current."
    return
  fi

  if ! command -v pnpm >/dev/null 2>&1; then
    echo "pnpm is required because the $name static build is missing or stale."
    echo "Run ./dev.sh once to prepare the development environment, then retry ./play.sh."
    exit 1
  fi

  echo "  → Building $name..."
  pnpm "$script"
}

prepare_space_art() {
  local game_dir="$ROOT_DIR/games/space-typing"
  local package_file="$game_dir/package.json"

  if [[ ! -f "$package_file" ]]; then
    echo "Space Typing package is missing: $package_file"
    exit 1
  fi
  if ! command -v node >/dev/null 2>&1 || ! command -v pnpm >/dev/null 2>&1; then
    echo "Node and pnpm are required to refresh local Space Typing art."
    exit 1
  fi
  if ! node -e '
    const p = require(process.argv[1]);
    process.exit(p.scripts?.["art:prepare"] ? 0 : 1);
  ' "$package_file"; then
    echo "Space Typing is too old: package.json has no art:prepare script."
    echo "Apply the latest Space Typing update before running ./play.sh."
    exit 1
  fi

  pnpm --dir "$game_dir" art:prepare
}

prepare_voice_assets() {
  if ! command -v node >/dev/null 2>&1 || ! command -v pnpm >/dev/null 2>&1; then
    echo "Node and pnpm are required to prepare the offline Voice model."
    exit 1
  fi
  if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is required to prepare the offline Voice model."
    echo "On Ubuntu/WSL run: sudo apt update && sudo apt install -y python3"
    exit 1
  fi
  if ! node -e 'require.resolve("vosk-browser")' >/dev/null 2>&1; then
    echo "The Portal Voice dependency vosk-browser is not installed yet."
    echo "After pulling this update, run once: pnpm install --frozen-lockfile"
    echo "Then retry ./play.sh."
    exit 1
  fi

  pnpm voice:prepare
}

print_admin_runtime_log() {
  local log_file="$1"
  if [[ -s "$log_file" ]]; then
    echo
    echo "--- Last 80 lines of $log_file ---"
    tail -n 80 "$log_file" || true
    echo "--- End Admin runtime log ---"
  else
    echo "Admin runtime log is empty: $log_file"
  fi
}

ensure_admin_runtime_service() {
  local endpoint="http://127.0.0.1:3199/api/runtime/space-typing/ships"
  local log_dir="$ROOT_DIR/.local/admin"
  local log_file="$log_dir/server.log"
  local pid_file="$log_dir/server.pid"
  local startup_attempts=80
  local startup_sleep=0.25

  mkdir -p "$log_dir"
  rm -f "$pid_file"

  # cleanup-dev-ports.sh intentionally leaves processes outside this repository alone.
  # Detect that case explicitly so Node does not fail later with a vague EADDRINUSE.
  local existing_pids
  existing_pids="$(lsof -tiTCP:3199 -sTCP:LISTEN 2>/dev/null || true)"
  if [[ -n "$existing_pids" ]]; then
    echo "Port 3199 is still occupied after project cleanup; refusing to replace an unrelated process."
    lsof -nP -iTCP:3199 -sTCP:LISTEN 2>/dev/null || true
    echo "Stop the process using port 3199, then run ./play.sh again."
    exit 1
  fi

  : >"$log_file"
  nohup node "$ROOT_DIR/admin/server.mjs" >"$log_file" 2>&1 &
  local server_pid="$!"
  echo "$server_pid" >"$pid_file"

  local attempt
  for ((attempt = 1; attempt <= startup_attempts; attempt++)); do
    sleep "$startup_sleep"

    if ! kill -0 "$server_pid" 2>/dev/null; then
      rm -f "$pid_file"
      echo "Space Typing Admin runtime bridge exited before becoming ready (PID $server_pid)."
      print_admin_runtime_log "$log_file"
      exit 1
    fi

    if curl -fsS --max-time 1 "$endpoint" >/dev/null 2>&1; then
      echo "  ✓ Admin runtime bridge started from current source (PID $server_pid)."
      return
    fi
  done

  rm -f "$pid_file"
  kill "$server_pid" 2>/dev/null || true
  echo "Timed out waiting for the Space Typing Admin runtime bridge on port 3199."
  echo "The startup probe waits about 20 seconds to accommodate slower filesystems such as WSL-mounted drives."
  print_admin_runtime_log "$log_file"
  exit 1
}

echo "[1/6] Stopping typing-game development servers..."
bash scripts/cleanup-dev-ports.sh --project-only 3000 3001 3002 3003 3004 3100 3199

echo "[2/6] Refreshing local Space Typing art..."
prepare_space_art

echo "[3/6] Preparing verified offline Voice assets..."
prepare_voice_assets

echo "[4/6] Checking static builds..."
node scripts/generate-music-index.mjs
build_if_needed \
  "Portal" \
  "portal/dist/index.html" \
  "build:portal" \
  "portal/src" \
  "portal/public" \
  "portal/index.html" \
  "portal/package.json" \
  "portal/tsconfig.json" \
  "portal/vite.config.ts" \
  "package.json" \
  "pnpm-lock.yaml" \
  "shared/learning" \
  "shared/voice" \
  "scripts/offline-vosk-plugin.mjs" \
  "scripts/voice-model-middleware.mjs"

build_if_needed \
  "Vocabulary Shooter" \
  "games/vocab-shooter/dist/index.html" \
  "build:shooter" \
  "games/vocab-shooter/src" \
  "games/vocab-shooter/index.html" \
  "games/vocab-shooter/package.json" \
  "games/vocab-shooter/tsconfig.json" \
  "games/vocab-shooter/vite.config.ts"

build_if_needed \
  "Recall Typing" \
  "games/recall-typing/dist/index.html" \
  "build:recall" \
  "games/recall-typing/src" \
  "games/recall-typing/index.html" \
  "games/recall-typing/package.json" \
  "games/recall-typing/tsconfig.json" \
  "games/recall-typing/vite.config.ts"

build_if_needed \
  "Karaoke Typing" \
  "games/karaoke-typing/dist/index.html" \
  "build:karaoke" \
  "games/karaoke-typing/src" \
  "games/karaoke-typing/index.html" \
  "games/karaoke-typing/package.json" \
  "games/karaoke-typing/tsconfig.json" \
  "games/karaoke-typing/vite.config.ts"

build_if_needed \
  "Space Typing" \
  "games/space-typing/dist/index.html" \
  "build:space" \
  "games/space-typing/src" \
  "games/space-typing/public" \
  "games/space-typing/art-src" \
  "games/space-typing/scripts" \
  "games/space-typing/index.html" \
  "games/space-typing/package.json" \
  "games/space-typing/tsconfig.json" \
  "games/space-typing/tsconfig.server.json" \
  "games/space-typing/vite.config.ts"

build_if_needed \
  "Monkeytype" \
  "games/monkeytype/frontend/dist/index.html" \
  "build:monkeytype" \
  "games/monkeytype/frontend/src" \
  "games/monkeytype/frontend/public" \
  "games/monkeytype/frontend/index.html" \
  "games/monkeytype/frontend/package.json" \
  "games/monkeytype/frontend/vite.config.ts" \
  "games/monkeytype/packages" \
  "games/monkeytype/package.json" \
  "games/monkeytype/pnpm-lock.yaml" \
  "games/monkeytype/turbo.json"

echo "[5/6] Starting runtime services and switching nginx to static Play mode..."
ensure_admin_runtime_service
bash scripts/setup-nginx.sh play
node games/space-typing/scripts/local-duel.mjs start
node games/space-typing/scripts/local-account.mjs start

echo "[6/6] Opening typing games..."
bash scripts/play.sh
