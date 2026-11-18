#!/usr/bin/env python3
"""Băm toàn bộ đường dẫn đích; không băm thư mục audit đang tự ghi."""
import subprocess,json,sys,difflib
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;O=D/sys.argv[1];O.mkdir(exist_ok=False)
roots=[R/'games/typing-survival/art-src/ui/icons',R/'games/typing-survival/art-src/ui/quick-settings',D]
files={str(p.relative_to(R)) for r in roots for p in r.rglob('*') if p.is_file() and O not in p.parents}
files|={str(p.relative_to(R)) for p in (R/'games/typing-survival/art-src/_review').glob('243*') if p.is_file()}
files.add('docs/codex-queue/243-report.md');files=sorted(files);after=''
for k in range(0,len(files),100):after+=subprocess.check_output(['/sbin/md5','-r',*files[k:k+100]],cwd=R,text=True)
before=(D/'md5-before.txt').read_text()
def parse(s):return {x[33:]:x[:32] for x in s.splitlines()}
b=parse(before);a=parse(after);changed=[p for p in b if p in a and b[p]!=a[p]];missing=[p for p in b if p not in a]
assert not changed and not missing,(changed,missing)
(O/'md5-after-all-targets.txt').write_text(after)
(O/'md5-diff.txt').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
summary=dict(before=len(b),after=len(a),added=len(a)-len(b),changed=changed,missing=missing,excluded_self=str(O.relative_to(R)))
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary,ensure_ascii=False))
