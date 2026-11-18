#!/usr/bin/env bash
set -euo pipefail
ART_NORMALIZE_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -n "${ART_MAGICK:-}" ]]; then
  [[ -x "$ART_MAGICK" ]] || { printf '%s\n' 'ART_MAGICK phải trỏ đến ImageMagick 7 có thể chạy.' >&2; exit 1; }
elif command -v magick >/dev/null 2>&1; then
  ART_MAGICK="$(command -v magick)"
elif [[ -x "$HOME/.local/bin/magick" ]]; then
  ART_MAGICK="$HOME/.local/bin/magick"
else
  printf '%s\n' 'Cần ImageMagick 7: magick trong PATH hoặc ~/.local/bin/magick.' >&2
  exit 1
fi
export ART_MAGICK
export PYTHONDONTWRITEBYTECODE=1
command -v python3 >/dev/null 2>&1 || { printf '%s\n' 'Cần Python 3.' >&2; exit 1; }
