#!/usr/bin/env bash
# Regenerate requirements.lock.txt (hashes) from requirements.txt. Existing pins are kept
# as preferences, so only new or changed top-level packages move. Then run setup.sh.
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HERE/env.sh"
cd "$AUDIOLAB_LAB"
"$AUDIOLAB_UV" pip compile requirements.txt --generate-hashes --no-annotate \
  --python "$AUDIOLAB_PY" --python-version 3.12 \
  --custom-compile-command "bash tools/audio-lab/common/lock.sh" \
  -o requirements.lock.txt "$@"
