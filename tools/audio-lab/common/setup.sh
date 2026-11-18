#!/usr/bin/env bash
# (Re)create ~/AudioLab/.venv from requirements.lock.txt with the private uv.
# Needs: ~/AudioLab/bin/uv and ~/AudioLab/python/cpython-3.12.* (see README). No brew, no sudo.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/env.sh"
mkdir -p "$AUDIOLAB_MODELS" "$AUDIOLAB_LIBRARIES" "$AUDIOLAB_WORK" "$AUDIOLAB_REVIEW" \
  "$AUDIOLAB_BIN" "$AUDIOLAB_CACHE" "$HF_HOME"
[ -x "$AUDIOLAB_UV" ] || { echo "thiếu $AUDIOLAB_UV" >&2; exit 2; }
[ -x "$AUDIOLAB_PY" ] || "$AUDIOLAB_UV" venv --python 3.12 "$AUDIOLAB_VENV"
"$AUDIOLAB_UV" pip sync --python "$AUDIOLAB_PY" --require-hashes "$AUDIOLAB_LAB/requirements.lock.txt"
"$AUDIOLAB_PY" -I -c 'import sys; print(sys.version.split()[0])'
