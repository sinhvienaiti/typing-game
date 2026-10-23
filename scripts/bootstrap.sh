#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-all}"
GIT_HOST="${TYPING_GAME_GIT_HOST:-}"

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

submodule_url_for_host() {
  local path="$1"
  local repo="${path##*/}"

  case "$GIT_HOST" in
    "")
      return 1
      ;;
    gitlab)
      printf 'https://gitlab.com/sinhvienaiti/%s.git\n' "$repo"
      ;;
    github)
      printf 'https://github.com/sinhvienaiti/%s.git\n' "$repo"
      ;;
    *)
      echo "Unsupported TYPING_GAME_GIT_HOST: $GIT_HOST" >&2
      exit 1
      ;;
  esac
}

apply_submodule_host_override() {
  [[ -n "$GIT_HOST" ]] || return 0

  local name path url
  while IFS='|' read -r name path; do
    url="$(submodule_url_for_host "$path")"
    git config "submodule.$name.url" "$url"
    echo "  → $path source: $GIT_HOST"
  done <<'EOF'
games/monkeytype|games/monkeytype
games/vocab-shooter|games/vocab-shooter
games/recall-typing|games/recall-typing
games/karaoke-typing|games/karaoke-typing
games/space-typing|games/space-typing
EOF
}

apply_submodule_host_override

update_submodule_branch() {
  local name="$1"
  local path="$2"
  local branch
  local override_url=""

  if [[ -n "$GIT_HOST" ]]; then
    override_url="$(submodule_url_for_host "$path")"
  fi

  git submodule update --init --recursive "$path"

  if [[ -n "$override_url" ]]; then
    git -C "$path" remote set-url origin "$override_url"
  fi

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

case "$TARGET" in
  all)
    update_submodule_branch "games/monkeytype" "games/monkeytype"
    update_submodule_branch "games/vocab-shooter" "games/vocab-shooter"
    update_submodule_branch "games/recall-typing" "games/recall-typing"
    update_submodule_branch "games/karaoke-typing" "games/karaoke-typing"
    update_submodule_branch "games/space-typing" "games/space-typing"
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
    update_submodule_branch "games/space-typing" "games/space-typing"
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
