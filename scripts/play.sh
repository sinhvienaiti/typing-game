#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
URL="https://typing-game.local"

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

open_url() {
  if command -v open >/dev/null 2>&1; then
    open "$URL"
    return
  fi

  if command -v wslview >/dev/null 2>&1; then
    wslview "$URL"
    return
  fi

  if command -v cmd.exe >/dev/null 2>&1; then
    cmd.exe /C start "" "$URL" >/dev/null 2>&1 || true
    return
  fi

  if command -v powershell.exe >/dev/null 2>&1; then
    powershell.exe -NoProfile -Command "Start-Process '$URL'" >/dev/null 2>&1 || true
    return
  fi

  if command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$URL" >/dev/null 2>&1 || true
    return
  fi

  echo "Open this URL in your browser: $URL"
}

open_url
