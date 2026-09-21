#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

for path in \
  "$ROOT_DIR/portal/dist/index.html" \
  "$ROOT_DIR/games/vocab-shooter/dist/index.html" \
  "$ROOT_DIR/games/recall-typing/dist/index.html" \
  "$ROOT_DIR/games/karaoke-typing/dist/index.html" \
  "$ROOT_DIR/games/space-typing/dist/index.html" \
  "$ROOT_DIR/games/monkeytype/frontend/dist/index.html"
do
  if [[ ! -f "$path" ]]; then
    echo "Static build is missing: $path"
    echo "Run: pnpm build:local"
    exit 1
  fi
done

brew services start nginx >/dev/null 2>&1 || true
open "https://typing-game.local"
