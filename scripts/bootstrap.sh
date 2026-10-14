#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"

case "$TARGET" in
  all|monkeytype|shooter|recall|karaoke|space)
    ;;
  *)
    echo "Usage: $0 [all|monkeytype|shooter|recall|karaoke|space]"
    exit 1
    ;;
esac

cd "$ROOT_DIR"

git submodule sync --recursive

update_submodule_branch() {
  local name="$1"
  local path="$2"
  local branch

  git submodule update --init --recursive "$path"

  branch="$(git config -f .gitmodules --get "submodule.$name.branch" || true)"
  if [[ -z "$branch" ]]; then
    echo "  ✓ $path is pinned to the platform gitlink."
    return
  fi

  echo "  → Updating $path from origin/$branch..."
  git -C "$path" fetch origin "$branch"

  if git -C "$path" show-ref --verify --quiet "refs/heads/$branch"; then
    git -C "$path" checkout "$branch"
  else
    git -C "$path" checkout -b "$branch" --track "origin/$branch"
  fi

  git -C "$path" pull --ff-only origin "$branch"
  git -C "$path" submodule update --init --recursive

  echo "  ✓ $path: $(git -C "$path" rev-parse --short HEAD) ($branch)"
}

update_submodule_pinned() {
  local path="$1"
  local pinned_sha
  local actual_sha

  pinned_sha="$(git rev-parse "HEAD:$path")"
  echo "  → Restoring $path to the platform-pinned gitlink ${pinned_sha:0:12}..."
  git submodule update --init --recursive "$path"
  actual_sha="$(git -C "$path" rev-parse HEAD)"

  if [[ "$actual_sha" != "$pinned_sha" ]]; then
    echo "ERROR: $path did not land on the platform gitlink." >&2
    echo "  expected: $pinned_sha" >&2
    echo "  actual:   $actual_sha" >&2
    exit 1
  fi

  echo "  ✓ $path: $(git -C "$path" rev-parse --short HEAD) (platform gitlink)"
}

update_space_submodule() {
  if [[ "${TYPING_GAME_SPACE_FOLLOW_BRANCH:-0}" == "1" ]]; then
    echo "  ! TYPING_GAME_SPACE_FOLLOW_BRANCH=1: explicitly following the Space Typing branch hint."
    update_submodule_branch "games/space-typing" "games/space-typing"
    return
  fi

  update_submodule_pinned "games/space-typing"
}

case "$TARGET" in
  all)
    update_submodule_branch "games/monkeytype" "games/monkeytype"
    update_submodule_branch "games/vocab-shooter" "games/vocab-shooter"
    update_submodule_branch "games/recall-typing" "games/recall-typing"
    update_submodule_branch "games/karaoke-typing" "games/karaoke-typing"
    update_space_submodule
    ;;
  monkeytype)
    update_submodule_branch "games/monkeytype" "games/monkeytype"
    ;;
  shooter)
    update_submodule_branch "games/vocab-shooter" "games/vocab-shooter"
    ;;
  recall)
    update_submodule_branch "games/recall-typing" "games/recall-typing"
    ;;
  karaoke)
    update_submodule_branch "games/karaoke-typing" "games/karaoke-typing"
    ;;
  space)
    update_space_submodule
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

install_space() {
  echo "Installing Space Typing..."
  pnpm --dir games/space-typing install
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
    install_space
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
  space)
    install_space
    ;;
esac

echo "Bootstrap complete for: $TARGET"
