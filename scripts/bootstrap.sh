#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

case "$TARGET" in
  all|monkeytype|shooter|recall|karaoke)
    ;;
  *)
    echo "Usage: $0 [all|monkeytype|shooter|recall|karaoke]"
    exit 1
    ;;
esac

cd "$ROOT_DIR"

git submodule sync --recursive

case "$TARGET" in
  all)
    git submodule update --init --recursive
    ;;
  monkeytype)
    git submodule update --init --recursive games/monkeytype
    ;;
  shooter)
    git submodule update --init --recursive games/vocab-shooter
    ;;
  recall)
    git submodule update --init --recursive games/recall-typing
    ;;
  karaoke)
    git submodule update --init --recursive games/karaoke-typing
    ;;
esac

echo "Installing platform tools..."
pnpm install

echo "Installing portal..."
pnpm --dir portal install

install_shooter() {
  echo "Installing Vocabulary Shooter..."
  pnpm --dir games/vocab-shooter install
}

install_recall() {
  echo "Installing Recall Typing..."
  pnpm --dir games/recall-typing install
}

install_karaoke() {
  echo "Installing Karaoke Typing..."
  pnpm --dir games/karaoke-typing install
}

install_monkeytype() {
  echo "Installing Monkeytype..."
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
}

case "$TARGET" in
  all)
    install_shooter
    install_recall
    install_karaoke
    install_monkeytype
    ;;
  monkeytype)
    install_monkeytype
    ;;
  shooter)
    install_shooter
    ;;
  recall)
    install_recall
    ;;
  karaoke)
    install_karaoke
    ;;
esac

echo "Bootstrap complete for: $TARGET"
