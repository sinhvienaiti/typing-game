#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"
git submodule update --init --recursive
echo "[1/4] Installing platform tools..."
pnpm install
echo "[2/4] Installing portal..."
pnpm --dir portal install
echo "[3/4] Installing Vocabulary Shooter..."
pnpm --dir games/vocab-shooter install
echo "[4/4] Installing Monkeytype..."
(cd games/monkeytype && pnpm install)
echo "Bootstrap complete."
