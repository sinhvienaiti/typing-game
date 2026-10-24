#!/usr/bin/env bash
# Guard commands for games that may not be checked out yet.
#   game-dir.sh require <dir> [command ...]  fail with a hint when games/<dir> is missing
#   game-dir.sh skip <dir> command ...       run when present, else print a notice and exit 0
#   game-dir.sh idle <dir> command ...       run when present, else stay idle (keeps `concurrently -k` running)
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MODE="${1:-}"
DIR="${2:-}"

usage() {
  echo "Usage: $0 require|skip|idle <game-dir> [command ...]" >&2
  exit 2
}

[[ -n "$MODE" && -n "$DIR" && "$DIR" != */* ]] || usage
shift 2

case "$DIR" in
  dragon-hold) LABEL="Rồng Giữ Ải (dragon-hold)" ;;
  typing-defense) LABEL="Lời Gọi (typing-defense)" ;;
  typing-survival) LABEL="Tuyến Cuối (typing-survival)" ;;
  immortality-cultivation) LABEL="Tu Tiên Thủ Ải (immortality-cultivation)" ;;
  *) LABEL="$DIR" ;;
esac

present() {
  [[ -f "$ROOT_DIR/games/$DIR/package.json" ]]
}

case "$MODE" in
  require)
    if ! present; then
      echo "$LABEL is not checked out yet: games/$DIR/package.json is missing." >&2
      echo "Add the game under games/$DIR (see docs/games/SPLIT_PLAN.md), then run: pnpm bootstrap" >&2
      exit 1
    fi
    if [[ "$#" -gt 0 ]]; then
      exec "$@"
    fi
    ;;
  skip)
    [[ "$#" -gt 0 ]] || usage
    if present; then
      exec "$@"
    fi
    echo "  • $LABEL is not checked out yet (games/$DIR); skipped."
    ;;
  idle)
    [[ "$#" -gt 0 ]] || usage
    if present; then
      exec "$@"
    fi
    echo "$LABEL is not checked out yet (games/$DIR); its dev server is skipped."
    sleep_pid=""
    trap '[[ -n "$sleep_pid" ]] && kill "$sleep_pid" 2>/dev/null; exit 0' INT TERM HUP
    while :; do
      sleep 3600 &
      sleep_pid="$!"
      wait "$sleep_pid" || true
    done
    ;;
  *)
    usage
    ;;
esac
