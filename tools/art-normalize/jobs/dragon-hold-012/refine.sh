#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' 'Hồ sơ 012 đã khóa; dùng rebuild-012d.sh.' >&2
exit 1
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
art_dir="$ART_NORMALIZE_DIR/../../games/dragon-hold/art-src"
mkdir -p "$ART_NORMALIZE_DIR/.tmp"
work_dir="$(mktemp -d "$ART_NORMALIZE_DIR/.tmp/refine-XXXXXX")"
case "$(realpath -- "$work_dir")" in
  "$ART_NORMALIZE_DIR"/.tmp/refine-*) ;;
  *) printf '%s\n' 'Thư mục tạm nằm ngoài phạm vi cho phép.' >&2; exit 1 ;;
esac
trap 'rm -r -- "$work_dir"' EXIT
bash "$ART_NORMALIZE_DIR/seamless.sh" "$art_dir/backdrops/pine-river-far.png" "$art_dir/backdrops/pine-river-far.soft.seamless.png" --axis x --blend 12%
bash "$ART_NORMALIZE_DIR/seam-check.sh" "$art_dir/backdrops/pine-river-far.soft.seamless.png" "$art_dir/_review/pine-river-far.soft.seam.png" --axis x
for name in flower-clusters forest-litter; do
  bash "$ART_NORMALIZE_DIR/key-alpha.sh" "$art_dir/decals/pine-river/$name.png" "$work_dir/$name.png" --fuzz 20%
  bash "$ART_NORMALIZE_DIR/pad-margin.sh" "$work_dir/$name.png" "$art_dir/decals/pine-river/$name.clean.alpha.png" --size 1024 --margin 9.375% --grid 2x2
done
bash "$ART_NORMALIZE_DIR/sheet.sh" "$art_dir/_review/decals-clean.dark.png" "$art_dir/decals/pine-river/flower-clusters.clean.alpha.png" "$art_dir/decals/pine-river/forest-litter.clean.alpha.png" --bg dark --tile 512
