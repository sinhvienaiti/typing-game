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
    echo "If Git is available, dev.sh pulls and updates submodules first."
    echo "Without Git (for example the Mac mini ZIP workflow), it keeps the local"
    echo "source, installs only missing dependencies, refreshes Space Typing art,"
    echo "and starts development normally."
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

has_git_checkout() {
  command -v git >/dev/null 2>&1 &&
    git -C "$ROOT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1
}

require_dir() {
  local dir="$1"
  local label="$2"
  if [[ ! -d "$dir" ]]; then
    echo "$label source directory is missing: $dir"
    echo "Restore/copy the complete typing-game ZIP before running dev.sh."
    exit 1
  fi
}

install_if_missing() {
  local dir="$1"
  local label="$2"

  require_dir "$dir" "$label"
  if [[ -d "$dir/node_modules" ]]; then
    echo "  ✓ $label dependencies are present."
    return
  fi

  echo "  → Installing $label dependencies..."
  if [[ "$dir" == "$ROOT_DIR" ]]; then
    pnpm install
  else
    pnpm --dir "$dir" install
  fi
}

ensure_monkeytype_config() {
  local config="$ROOT_DIR/games/monkeytype/frontend/src/ts/constants/firebase-config.ts"
  local example="$ROOT_DIR/games/monkeytype/frontend/src/ts/constants/firebase-config-example.ts"
  if [[ ! -f "$config" && -f "$example" ]]; then
    cp "$example" "$config"
    echo "  ✓ Created local Monkeytype Firebase placeholder config."
  fi
}

prepare_without_git() {
  if ! command -v node >/dev/null 2>&1 || ! command -v pnpm >/dev/null 2>&1; then
    echo "Node and pnpm are required for local development."
    exit 1
  fi

  install_if_missing "$ROOT_DIR" "Platform"
  install_if_missing "$ROOT_DIR/portal" "Portal"

  case "$TARGET" in
    all)
      install_if_missing "$ROOT_DIR/games/vocab-shooter" "Vocabulary Shooter"
      install_if_missing "$ROOT_DIR/games/recall-typing" "Recall Typing"
      install_if_missing "$ROOT_DIR/games/karaoke-typing" "Karaoke Typing"
      install_if_missing "$ROOT_DIR/games/space-typing" "Space Typing"
      install_if_missing "$ROOT_DIR/games/monkeytype" "Monkeytype"
      ensure_monkeytype_config
      ;;
    monkeytype)
      install_if_missing "$ROOT_DIR/games/monkeytype" "Monkeytype"
      ensure_monkeytype_config
      ;;
    shooter)
      install_if_missing "$ROOT_DIR/games/vocab-shooter" "Vocabulary Shooter"
      ;;
    recall)
      install_if_missing "$ROOT_DIR/games/recall-typing" "Recall Typing"
      ;;
    karaoke)
      install_if_missing "$ROOT_DIR/games/karaoke-typing" "Karaoke Typing"
      ;;
    space)
      install_if_missing "$ROOT_DIR/games/space-typing" "Space Typing"
      ;;
  esac
}

prepare_space_art() {
  if [[ "$TARGET" != "all" && "$TARGET" != "space" ]]; then
    echo "  • Space Typing is not selected; art refresh skipped."
    return
  fi

  local package_file="$ROOT_DIR/games/space-typing/package.json"
  if [[ ! -f "$package_file" ]]; then
    echo "Space Typing package is missing: $package_file"
    exit 1
  fi
  if ! node -e '
    const p = require(process.argv[1]);
    process.exit(p.scripts?.["art:prepare"] ? 0 : 1);
  ' "$package_file"; then
    echo "Space Typing is too old: package.json has no art:prepare script."
    echo "Apply the latest Space Typing update before running dev.sh."
    exit 1
  fi

  pnpm --dir "$ROOT_DIR/games/space-typing" art:prepare
}

if has_git_checkout; then
  if [[ "${TYPING_GAME_DEV_AFTER_PULL:-0}" != "1" ]]; then
    echo "[1/5] Pulling latest platform code..."
    git pull --ff-only --recurse-submodules=no

    # Re-run the version of this script that exists after git pull.
    exec env TYPING_GAME_DEV_AFTER_PULL=1 bash "$ROOT_DIR/dev.sh" "$TARGET"
  fi
  echo "[1/5] Platform code already refreshed."
  echo "[2/5] Updating submodules and dependencies for: $TARGET"
  bash scripts/bootstrap.sh "$TARGET"
else
  echo "[1/5] Git checkout unavailable; keeping local ZIP/source as-is."
  echo "[2/5] Checking local dependencies for: $TARGET"
  prepare_without_git
fi

echo "[3/5] Refreshing local Space Typing art..."
prepare_space_art

echo "Indexing local background music..."
pnpm music:index

echo "[4/5] Switching nginx to development mode..."
pnpm setup:dev

echo "[5/5] Starting development services for: $TARGET"
if [[ "$TARGET" == "all" || "$TARGET" == "space" ]]; then
  node games/space-typing/scripts/local-duel.mjs start
fi
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
