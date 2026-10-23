#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

export TYPING_GAME_MACHINE="mac-m2"
export TYPING_GAME_GIT_HOST="gitlab"

# Force every Git process launched by dev.sh/bootstrap.sh (including Git inside
# already-initialized submodules) to resolve this project's GitHub URLs through
# the GitLab mirror. This is inherited by child Git processes and therefore also
# works when the checked-out parent branch still has an older bootstrap.sh.
export GIT_CONFIG_COUNT=1
export GIT_CONFIG_KEY_0="url.https://gitlab.com/sinhvienaiti/.insteadOf"
export GIT_CONFIG_VALUE_0="https://github.com/sinhvienaiti/"

echo "[M2] Machine profile: mac-m2"
echo "[M2] Git source: GitLab (GitHub URLs are transparently rewritten to GitLab)"
echo "[M2] Parent branch: $(git branch --show-current 2>/dev/null || echo unknown)"

exec env \
  TYPING_GAME_MACHINE="$TYPING_GAME_MACHINE" \
  TYPING_GAME_GIT_HOST="$TYPING_GAME_GIT_HOST" \
  GIT_CONFIG_COUNT="$GIT_CONFIG_COUNT" \
  GIT_CONFIG_KEY_0="$GIT_CONFIG_KEY_0" \
  GIT_CONFIG_VALUE_0="$GIT_CONFIG_VALUE_0" \
  bash "$ROOT_DIR/dev.sh" "$@"
