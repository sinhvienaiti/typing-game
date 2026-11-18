#!/usr/bin/env python3
"""python3 docs/codex-queue/243/audit.py <thư-mục-kiểm-mới>"""
import subprocess,sys,json,difflib,math
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;O=D/sys.argv[1];O.mkdir(exist_ok=False)
M='/opt/homebrew/bin/magick';C=D/'candidates-final'
def run(args):return subprocess.check_output([M,*map(str,args)])
def rgba(p,n=None):return run([p,*(['-filter','Lanczos','-resize',f'{n}x{n}'] if n else []),'-depth','8','rgba:-'])
def mask(p,t):return {i for i,v in enumerate(rgba(p,32)[3::4]) if v>t}
roots=[R/'games/typing-survival/art-src/ui/icons',R/'games/typing-survival/art-src/ui/quick-settings']
files=sorted({str(p.relative_to(R)) for r in roots for p in r.rglob('*') if p.is_file()}|{str(p.relative_to(R)) for p in (R/'games/typing-survival/art-src/_review').glob('243*') if p.is_file()})
after=''
for k in range(0,len(files),100):after+=subprocess.check_output(['/sbin/md5','-r',*files[k:k+100]],cwd=R,text=True)
(O/'md5-after.txt').write_text(after);before=(D/'md5-before.txt').read_text()
def parse(s):return {s1[33:]:s1[:32] for s1 in s.splitlines()}
b=parse(before);aa=parse(after);changed=[p for p in b if p in aa and b[p]!=aa[p]];missing=[p for p in b if p not in aa]
(O/'md5-diff.txt').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
assert not changed and not missing,(changed,missing)
A=json.loads((D/'assets-check.json').read_text());L=json.loads((D/'delivered.json').read_text());identify=[];resizes=[];rgb=[]
for rel in L:
 p=R/rel;identify.append(run(['identify','-format','%f %wx%h %[channels] %[colorspace] %[depth]bit\n',p]).decode())
 suffix=p.stem.split('.')[-1];n=int(suffix) if suffix in ['256','128','64'] else 1024
 assert run(['identify','-format','%w %h',p]).decode()==f'{n} {n}'
 assert 'srgba' in identify[-1] and 'sRGB' in identify[-1]
 assert p.with_suffix('.prompt.txt').exists()
 if n!=1024:
  master=p.with_name(p.name.replace('.'+suffix+'.png','.png'))
  assert rgba(master,n)==rgba(p),p
  resizes.append(rel)
for a in A:
 base=Path(a['final']).name;x=rgba(C/(base+'.png'));y=rgba(C/(base+'.clean.png'))
 assert x[0::4]==y[0::4] and x[1::4]==y[1::4] and x[2::4]==y[2::4],base
 rgb.append(a['name'])
(O/'identify.txt').write_text(''.join(identify))
pairs=[]
for i,a in enumerate(A):
 for b0 in A[i+1:]:
  p=R/(a['final']+'.png');q=R/(b0['final']+'.png');scores={}
  for t in [16,128]:
   ma=mask(p,t);mb=mask(q,t);scores[str(t)]=len(ma&mb)/len(ma|mb)
  gear={a['name'],b0['name']}=={'menu-settings','hud-settings'}
  assert all(v>=.9 if gear else v<=.8 for v in scores.values()),(a['name'],b0['name'],scores)
  pairs.append(dict(a=a['name'],b=b0['name'],iou=scores,gear=gear))
(O/'all-pairs-32px.json').write_text(json.dumps(pairs,indent=2))
summary=dict(before_files=len(b),after_files=len(aa),added=len(aa)-len(b),changed=changed,missing=missing,masters=10,delivered_png=len(L),exact_direct_lanczos=len(resizes),rgb_unchanged_by_alpha_cleanup=rgb,pair_count=len(pairs),max_iou_non_gear=max(max(p['iou'].values()) for p in pairs if not p['gear']),gear_iou=next(p['iou'] for p in pairs if p['gear']))
(O/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False))
