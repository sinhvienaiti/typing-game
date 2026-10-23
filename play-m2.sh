#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

export TYPING_GAME_MACHINE="mac-m2"
export TYPING_GAME_GIT_HOST="gitlab"

exec bash "$ROOT_DIR/play.sh" "$@"
