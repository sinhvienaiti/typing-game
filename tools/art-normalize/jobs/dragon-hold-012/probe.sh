#!/usr/bin/env bash
set -euo pipefail
printf "%s\n" "Hồ sơ thử 012b đã khóa; dùng rebuild-012d.sh và inspect-pockets.sh." >&2
exit 1
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
export ART_NORMALIZE_DIR
python3 - <<'PY'
import os
import sys
from pathlib import Path
root = Path(os.environ['ART_NORMALIZE_DIR'])
sys.path.insert(0, str(root))
import normalize as n
art = root.parent.parent / 'games/dragon-hold/art-src'
out = root / '.tmp/probe-012b'
out.mkdir(exist_ok=True)
for name in ('forest-litter', 'flower-clusters'):
    src = art / f'decals/pine-river/{name}.png'
    n.key(src, out / f'{name}.cut.png', mode='global', fuzz=.12)
    n.pad(out / f'{name}.cut.png', out / f'{name}.png', (1024,1024), .09375, '2x2', out)
    print('Xong', name, flush=True)
src = art / 'enemies/moss-archer.png'
n.key(src, out / 'archer.cut.png', fuzz=.06)
n.fit(out / 'archer.cut.png', out / 'archer.pad.png', (1024,1536), .08)
n.im(out / 'archer.pad.png', '-background', '#E6E6E6', '-alpha', 'remove', '-alpha', 'off', out / 'archer.png')
src = art / 'backdrops/pine-river-far.png'
n.seamless(src, out / 'seam.png', 'x', .12)
for label,p in (('before',src),('after',out/'seam.png')):
    w,h,data=n.rgba(p)
    print(label,n.seam_metrics(w,h,data)['x'],flush=True)
n.im(out/'seam.png',out/'seam.png','+append','-crop','500x600+1286+300','+repage',out/'seam-crop.png')
print('Xong mẫu kiểm tra',flush=True)
PY
