#!/usr/bin/env bash
# VFX Flipbook: Adobe Firefly Video clip -> game flipbook (atlas PNG, JSON, sheet, preview, metrics).
# Usage (from the parent repo root):
#   tools/vfx-flipbook/run.sh ingest <game> <id> [vN]   # one id; every version when vN is left out
#   tools/vfx-flipbook/run.sh all <game>                # every clip present in the inbox
#   tools/vfx-flipbook/run.sh probe <clip.mp4>          # ffprobe summary
#   tools/vfx-flipbook/run.sh ktx2 <manifest directory> [--only id,id] [--force]
#   tools/vfx-flipbook/run.sh test [-q]                 # synthetic-clip tests (pytest)
# Input:  $VFXLAB_HOME/inbox/firefly/<game>/<id>/<id>__vN.mp4   (VFXLAB_HOME defaults to ~/VFXLab)
#         or <id>__vN.rgb.mp4 + <id>__vN.alpha.mp4 (Firefly transparent mode: colour + matte, "matte": "alpha-video")
# Output: $VFXLAB_HOME/out/<game>/<id>/<id>__vN.{atlas.png,json,sheet.jpg,preview.mp4,metrics.json}
# Python: needs numpy, scipy, Pillow, pytest; the Audio Lab venv has them (override with VFXFLIP_PY).
# Cài riêng cho công cụ (chỉ khi chưa có):
# uv venv --python ~/AudioLab/python/cpython-3.12-macos-aarch64-none/bin/python3.12 tools/vfx-flipbook/.venv
# uv pip install --python tools/vfx-flipbook/.venv/bin/python -r tools/vfx-flipbook/requirements.txt
# npm install --no-audit --no-fund --prefix tools/vfx-flipbook/ktx2
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export VFXLAB_HOME="${VFXLAB_HOME:-$HOME/VFXLab}"
PY="${VFXFLIP_PY:-}"
if [ -z "$PY" ]; then
  if [ -x "$HERE/.venv/bin/python" ]; then
    PY="$HERE/.venv/bin/python"
  else
    PY="$HOME/AudioLab/.venv/bin/python"
  fi
fi
if [ ! -x "$PY" ]; then
  echo "vfx-flipbook: không thấy Python có numpy/scipy/Pillow ở $PY; đặt VFXFLIP_PY" >&2
  exit 2
fi
if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  echo "vfx-flipbook: cần ffmpeg và ffprobe trong PATH" >&2
  exit 2
fi
exec "$PY" -I "$HERE/launch.py" "$@"
