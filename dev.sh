#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

TARGET="${1:-all}"

case "$TARGET" in
  -h|--help|help)
    echo "Usage: ./dev.sh [all|monkeytype|shooter|recall|karaoke|space]"
    echo
    echo "Default: all"
    exit 0
    ;;
  vocab-shooter)
    TARGET="shooter"
    ;;
  recall-typing)
    TARGET="recall"
    ;;
  karaoke-typing)
    TARGET="karaoke"
    ;;
  space-typing)
    TARGET="space"
    ;;
  all|monkeytype|shooter|recall|karaoke|space)
    ;;
  *)
    echo "Unknown target: $TARGET"
    echo "Usage: ./dev.sh [all|monkeytype|shooter|recall|karaoke|space]"
    exit 1
    ;;
esac

if [[ "${TYPING_GAME_DEV_AFTER_PULL:-0}" != "1" ]]; then
  echo "[1/4] Pulling latest platform code..."
  git pull --ff-only --recurse-submodules=no

  # Re-run the version of this script that exists after git pull.
  exec env TYPING_GAME_DEV_AFTER_PULL=1 bash "$ROOT_DIR/dev.sh" "$TARGET"
fi

echo "[2/4] Updating submodules and dependencies for: $TARGET"
bash scripts/bootstrap.sh "$TARGET"

echo "Indexing local background music..."
pnpm music:index

echo "[3/4] Switching nginx to development mode..."
pnpm setup:dev

echo "[4/4] Starting development services for: $TARGET"
case "$TARGET" in
  all)
    exec pnpm dev
    ;;
  monkeytype)
    exec pnpm dev:monkeytype
    ;;
  shooter)
    exec pnpm dev:shooter
    ;;
  recall)
    exec pnpm dev:recall
    ;;
  karaoke)
    exec pnpm dev:karaoke
    ;;
  space)
    exec pnpm dev:space
    ;;
esac
