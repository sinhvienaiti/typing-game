#!/usr/bin/env python3
"""Kiểm giao, không ghi đè. python3 docs/codex-queue/242/audit.py <tên-lượt-mới>"""
import subprocess,json,sys,difflib
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;O=D/('audit-'+sys.argv[1]);O.mkdir(exist_ok=False)
M='/opt/homebrew/bin/magick'; I=R/'games/typing-survival/art-src/ui/icons';V=R/'games/typing-survival/art-src/_review'
files=sorted(str(p.relative_to(R)) for p in I.rglob('*') if p.is_file())
after=subprocess.check_output(['/sbin/md5','-r',*files],cwd=R,text=True)
(O/'md5-after-icons.txt').write_text(after);before=(D/'md5-before.txt').read_text()
def parse(s):return {line[33:].strip():line[:32] for line in s.splitlines()}
b=parse(before);a=parse(after);changed=[p for p in b if p in a and b[p]!=a[p]];missing=[p for p in b if p not in a];added=[p for p in a if p not in b]
(O/'md5-diff.txt').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
assert not changed and not missing,(changed,missing)
L=json.loads((D/'delivered.json').read_text());ident=[];resizes=[]
for rel in L:
 p=R/rel;ident.append(subprocess.check_output([M,'identify','-format','%f %wx%h %[channels] %[colorspace] %[depth]bit\n',str(p)],text=True))
 suffix=p.stem.split('.')[-1]; expected=int(suffix) if suffix in ('256','128','64') else 1024
 assert subprocess.check_output([M,'identify','-format','%w %h',str(p)],text=True).strip()==f'{expected} {expected}'
 assert p.with_suffix('.prompt.txt').exists()
 if expected!=1024:
  master=p.with_name(p.name.replace('.'+suffix+'.png','.png'))
  ref=subprocess.check_output([M,str(master),'-filter','Lanczos','-resize',f'{expected}x{expected}','-colorspace','sRGB','-depth','8','rgba:-'])
  actual=subprocess.check_output([M,str(p),'-depth','8','rgba:-']);assert ref==actual,p
  resizes.append(str(p.relative_to(R)))
(O/'identify.txt').write_text(''.join(ident))
allfiles=sorted({*files,*[str(p.relative_to(R)) for p in D.rglob('*') if p.is_file() and O not in p.parents],*[str(p.relative_to(R)) for p in V.glob('242*') if p.is_file()], 'docs/codex-queue/242-report.md'})
full=subprocess.check_output(['/sbin/md5','-r',*allfiles],cwd=R,text=True);(O/'md5-after-all-targets.txt').write_text(full)
summary=dict(before=len(b),after=len(a),added=len(added),changed=changed,missing=missing,delivered_png=len(L),direct_lanczos_match=len(resizes),all_targets_hashed=len(allfiles),note='Mốc đầu: ui/icons có 532 file; hồ sơ/242, report và _review/242* chưa có file. Manifest sau loại chính thư mục audit đang ghi để không tự băm đệ quy.')
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False))
