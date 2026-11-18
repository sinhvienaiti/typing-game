#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' 'Hồ sơ 012 đã khóa; dùng rebuild-012d.sh.' >&2
exit 1
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
art_dir="$ART_NORMALIZE_DIR/../../games/dragon-hold/art-src"
for tile in 256 64 32; do
  source_size=64
  if [[ "$tile" == 256 ]]; then source_size=256; fi
  bash "$ART_NORMALIZE_DIR/sheet.sh" "$art_dir/_review/icons-$tile.labeled.checker.png" "$art_dir/icons/normalized/"*."$source_size".png --bg checker --tile "$tile"
done
