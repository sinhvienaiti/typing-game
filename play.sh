#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

case "${1:-}" in
  "")
    ;;
  -h|--help|help)
    echo "Usage: ./play.sh"
    echo
    echo "Play mode does not pull Git, update submodules, or install dependencies."
    echo "It only refreshes stale static builds, switches nginx to static Play mode,"
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

echo "[1/4] Stopping typing-game development servers..."
bash scripts/cleanup-dev-ports.sh --project-only 3000 3001 3002 3003 3004 3100

echo "[2/4] Checking static builds..."
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
  "shared/learning"

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
  "games/space-typing/index.html" \
  "games/space-typing/package.json" \
  "games/space-typing/tsconfig.json" \
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

echo "[3/4] Switching nginx to static Play mode..."
PLAY_NGINX_SOURCE="$ROOT_DIR/infra/nginx/typing-game.local.play.conf"
NGINX_TARGET="/usr/local/etc/nginx/servers/typing-game.local.conf"

if [[ -f "$NGINX_TARGET" ]] && cmp -s "$PLAY_NGINX_SOURCE" "$NGINX_TARGET"; then
  brew services start nginx >/dev/null 2>&1 || true
  echo "nginx is already in Play mode."
else
  bash scripts/setup-nginx.sh play
fi

echo "[4/4] Opening typing games..."
bash scripts/play.sh
