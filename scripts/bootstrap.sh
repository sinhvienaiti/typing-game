#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

git submodule update --init --recursive

echo "[1/5] Installing platform tools..."
pnpm install

echo "[2/5] Installing portal..."
pnpm --dir portal install

echo "[3/5] Installing Vocabulary Shooter..."
pnpm --dir games/vocab-shooter install

echo "[4/5] Installing Recall Typing..."
pnpm --dir games/recall-typing install

echo "[5/5] Installing Monkeytype..."
(
  cd games/monkeytype
  pnpm install

  FIREBASE_CONFIG="frontend/src/ts/constants/firebase-config.ts"
  FIREBASE_EXAMPLE="frontend/src/ts/constants/firebase-config-example.ts"
  if [[ ! -f "$FIREBASE_CONFIG" && -f "$FIREBASE_EXAMPLE" ]]; then
    cp "$FIREBASE_EXAMPLE" "$FIREBASE_CONFIG"
    echo "Created local Firebase placeholder config."
  fi
)

echo "Bootstrap complete."
