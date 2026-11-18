#!/usr/bin/env bash
set -euo pipefail
printf "%s\n" "Hồ sơ thử 012b đã khóa; dùng rebuild-012d.sh và inspect-pockets.sh." >&2
exit 1
source "$(dirname -- "${BASH_SOURCE[0]}")/../../common.sh"
export ART_NORMALIZE_DIR
python3 - <<'PY'
import os,sys
from pathlib import Path
root=Path(os.environ['ART_NORMALIZE_DIR']);sys.path.insert(0,str(root))
import normalize as n
sys.path.insert(0,str(root/'jobs/dragon-hold-012'))
from rebuild_012b import neutral_residue
for name in ('forest-litter.cut.png','forest-litter.png','flower-clusters.cut.png','flower-clusters.png'):
    w,h,p=n.rgba(root/'.tmp/probe-012b'/name)
    def bad(i):
        r,g,b,a=p[i:i+4]
        return a>0 and (g-max(r,b)>25 if name.startswith('forest') else b-max(r,g)>25)
    print(name,sum(bad(i) for i in range(0,len(p),4)),flush=True)
    if name=='forest-litter.png':
        n.im(root/'.tmp/probe-012b'/name,'-background','#FFFFFF','-alpha','remove','-crop','512x512+0+0','+repage',root/'.tmp/probe-012b/forest-white.png')
art=root.parent.parent/'games/dragon-hold/art-src'
w,h,p=n.rgba(art/'enemies/moss-archer.png')
background=n.background_color(w,h,p)
print('Archer pockets:',neutral_residue(root/'.tmp/probe-012b/archer.png',background),flush=True)
PY
