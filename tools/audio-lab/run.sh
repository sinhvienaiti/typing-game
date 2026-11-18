#!/usr/bin/env bash
# Run an Audio Lab module in the shared venv with the safe environment.
# Usage: tools/audio-lab/run.sh <alias|module|script.py|script.mjs> [args...]
#   tools/audio-lab/run.sh critic --help
#   tools/audio-lab/run.sh critic.analyze file.wav --out ~/AudioLab/work/x
#   tools/audio-lab/run.sh test -q
set -euo pipefail
LAB="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common/env.sh
source "$LAB/common/env.sh"
if [ ! -x "$AUDIOLAB_PY" ]; then
  echo "audio-lab: chưa có venv ở $AUDIOLAB_VENV; chạy: bash tools/audio-lab/common/setup.sh" >&2
  exit 2
fi
exec "$AUDIOLAB_PY" -I "$LAB/common/launch.py" "$@"
