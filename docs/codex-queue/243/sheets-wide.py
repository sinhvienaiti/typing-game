#!/usr/bin/env python3
"""Tờ kiểm phiếu 243; chỉ ghi vào thư mục mới và tên _review/243 mới."""
import json, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent
M='/opt/homebrew/bin/magick';F='/System/Library/Fonts/Supplemental/Arial.ttf'
C=R/sys.argv[1];O=D/sys.argv[2];O.mkdir(exist_ok=False)
A=json.loads((D/'assets-check.json').read_text())
def run(args):return subprocess.check_output([M,*map(str,args)])
def make(args,p):
 assert not p.exists(),p
 run([*args,'-define','png:color-type=6',p]);return p
def path(a):return C/(Path(a['final']).name+'.clean.png')
def annotation(x,y,s,size=20):return ['-font',F,'-pointsize',str(size),'-fill','#edf4fa','-gravity','NorthWest','-annotate',f'+{x}+{y}',s]
def paste(p,x,y,args=None):return ['(',p,*(args or []),')','-gravity','NorthWest','-geometry',f'+{x}+{y}','-compose','Over','-composite']
# Mảnh UI đủ rộng cho nhãn Pace ở cả hai cỡ; giữ nguyên pixel nguồn.
for tag,geom in [('button','560x64+220+160'),('panel','560x64+230+230')]:
 make([R/'games/typing-survival/art-src/ui/frames-epic'/(('button' if tag=='button' else 'panel-large')+'.png'),'-crop',geom,'+repage','-colorspace','sRGB'],O/(tag+'-crop.png'))
for a in A:
 for res in ['720','1080']:
  n=a['size'+res]
  for tag in ['button','panel']:
   args=[O/(tag+'-crop.png'),*paste(path(a),8,(64-n)//2,['-filter','Lanczos','-resize',f'{n}x{n}'])]
   if a['label']:args+=annotation(n+14,(64-round(n*.6))//2,a['label'],round(n*.83))
   tile=make(args,O/(a['name']+'-'+res+'-'+tag+'.png'))
   if res=='720' and tag=='panel':make([tile,'-filter','point','-resize','400%'],O/(a['name']+'-720-panel-4x.png'))
cols=[]
for a in A:
 name=a['name'];p=path(a);args=['-size','2240x1120','xc:#14181f']
 args+=annotation(12,8,name)+annotation(12,40,'1. Master 256 px',16)
 args+=paste(p,12,64,['-resize','256x256'])
 args+=annotation(12,328,'2. 1080p 1x / button + panel',16)
 for k,tag in enumerate(['button','panel']):args+=paste(O/(name+'-1080-'+tag+'.png'),12+k*580,352)
 args+=annotation(12,424,'3. 720p 1x / button + panel',16)
 for k,tag in enumerate(['button','panel']):args+=paste(O/(name+'-720-'+tag+'.png'),12+k*580,448)
 args+=annotation(12,520,'4. 720p panel x4 / nearest',16)
 args+=paste(O/(name+'-720-panel-4x.png'),0,544)
 args+=annotation(12,808,'5. Comparisons at 720p size',16)
 for k,other in enumerate(a['compare']):
  b=next((b for b in A if b['name']==other),None);q=path(b) if b else R/other
  args+=paste(C/'panel-crop.png',12+k*280,840)
  args+=paste(p,20+k*280,856,['-resize',f"{a['size720']}x{a['size720']}"])
  args+=paste(q,68+k*280,856,['-resize',f"{a['size720']}x{a['size720']}"])
  args+=annotation(16+k*280,910,Path(other).stem,14)
 args+=annotation(12,948,'6. Current | new at 720p size',16)
 if name in ['ship','letter-style','effect-strength','word-size']:
  args+=annotation(16,1004,'New asset',16)
 else:
  old=(R/Path(a['final']).parent/(name+'.png'))
  if name=='pace-director':old=R/'games/typing-survival/art-src/ui/icons/pace-director.v2.png'
  args+=paste(C/'panel-crop.png',12,984)
  args+=paste(old,20,1000,['-resize',f"{a['size720']}x{a['size720']}"])
  args+=paste(p,76,1000,['-resize',f"{a['size720']}x{a['size720']}"])
 col=make(args,O/(name+'-column.png'));cols.append(col)
sheet=R/'games/typing-survival/art-src/_review'/'243-sheet-v2.jpg'
assert not sheet.exists();run([*cols,'+append','-quality','92',sheet])
args=['-size','1160x640','xc:#14181f']
for k,a in enumerate(A):
 for j,tag in enumerate(['button','panel']):args+=paste(O/(a['name']+'-720-'+tag+'.png'),j*580,k*64)
make(args,O/'real-size-720-1x.png')
args=['-size','560x192','xc:#14181f']
for k,name in enumerate(['letter-style','word-size','effect-strength']):args+=paste(O/(name+'-720-panel.png'),0,k*64)
make(args,O/'letters-compare-28px.png')
print(sheet.relative_to(R))
