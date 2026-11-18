#!/usr/bin/env python3
"""Chỉ tạo file mới. Chạy sau process-v3.py: python3 docs/codex-queue/242/deliver.py"""
import subprocess,json,shutil
from pathlib import Path
R=Path(__file__).resolve().parents[3];D=Path(__file__).parent;C=D/'final-delivery';I=R/'games/typing-survival/art-src/ui/icons';V=R/'games/typing-survival/art-src/_review';M='/opt/homebrew/bin/magick';F='/System/Library/Fonts/Supplemental/Arial.ttf'
A=json.loads((D/'assets.json').read_text());S=json.loads((D/'selection-delivery.json').read_text());LOG=[]
def run(args,p):
 assert not p.exists(),p
 subprocess.run([M,*map(str,args),str(p)],check=True)
def cp(src,dst):
 with src.open('rb') as a,dst.open('xb') as b:shutil.copyfileobj(a,b)
P=D/'proofs-v3';P.mkdir(exist_ok=False)
FRAME=I.parent/'frames-epic'
for tag,src,geom in [('button',FRAME/'button.png','320x64+220+160'),('panel',FRAME/'panel-large.png','320x64+230+230')]:
 run([src,'-crop',geom,'+repage','-colorspace','sRGB'],P/(tag+'-crop.png'))
for a in A:
 for res in ['720','1080']:
  size=a['s'+res]
  for tag in ['button','panel']:
   args=[P/(tag+'-crop.png'),'(',C/(a['base']+'.png'),'-filter','Lanczos','-resize',f'{size}x{size}',')','-gravity','NorthWest','-geometry',f'+8+{(64-size)//2}','-compose','Over','-composite']
   if a['label']:args+=['(','-background','none','-font',F,'-pointsize','64','-fill','#eef4f8','label:'+a['label'],'-trim','+repage','-resize','x'+str(round(size*.6)),')','-gravity','NorthWest','-geometry',f'+{size+14}+{(64-round(size*.6))//2}','-composite']
   t=P/(a['name']+'-'+res+'-'+tag+'.png');run(args,t)
   if res=='720':run([t,'-filter','point','-resize','400%'],P/(a['name']+'-'+res+'-'+tag+'-4x.png'))
# Tờ sáu hàng, ô 1× được chép pixel nguyên kích thước; hàng 4 chỉ phóng vùng icon.
W=340;H=1180;rows=[68,352,508,664,928,1064]
args=['-size',f'{W*len(A)}x{H}','xc:#111923','-font',F,'-fill','#f3f6fa','-pointsize','22','-gravity','NorthWest','-annotate','+14+8','242 · Last Line · 256 / 1080p 1x / 720p 1x / 720p icon crop 4x nearest / comparisons / old-new']
for col,a in enumerate(A):
 x=col*W;name=a['name'];base=a['base'];size=a['s720']
 args+=['-pointsize','17','-annotate',f'+{x+10}+42',name]
 args+=['(',C/(base+'.256.png'),')','-geometry',f'+{x+12}+{rows[0]}','-composite']
 for ri,res in [(1,'1080'),(2,'720')]:
  for j,tag in enumerate(['button','panel']):
   args+=['(',P/(name+'-'+res+'-'+tag+'.png'),')','-geometry',f'+{x+10}+{rows[ri]+j*66}','-composite']
 args+=['(',P/(name+'-720-panel.png'),'-crop','40x64+0+0','+repage','-filter','point','-resize','400%',')','-geometry',f'+{x+90}+{rows[3]}','-composite']
 # Со sánh cùng cỡ 720p, có đúng mọi icon cột So với.
 compare=[(name,C/(base+'.png'))]
 for k in a['compare']:
  other=next((b for b in A if b['name']==k.replace('.r2','')),None)
  q=C/(other['base']+'.png') if other and ('.r2' in k or k=='stat-words') else I/(k+'.png')
  compare.append((k,q))
 args+=['(',P/'panel-crop.png',')','-geometry',f'+{x+10}+{rows[4]}','-composite']
 for j,(label,q) in enumerate(compare):
  xx=x+16+j*64
  args+=['(',q,'-filter','Lanczos','-resize',f'{size}x{size}',')','-geometry',f'+{xx}+{rows[4]+10}','-composite','-pointsize','8','-annotate',f'+{xx}+{rows[4]+46}',label.replace('../parts/','')]
 # stat-words trước đây dùng keyboard, lấy đúng ảnh cũ đó.
 old=I/((name if name!='stat-words' else 'keyboard')+'.png')
 args+=['(',P/'panel-crop.png',')','-geometry',f'+{x+10}+{rows[5]}','-composite']
 for j,(label,q) in enumerate([('Old',old),('New',C/(base+'.png'))]):
  xx=x+28+j*126
  args+=['(',q,'-filter','Lanczos','-resize',f'{size}x{size}',')','-geometry',f'+{xx}+{rows[5]+8}','-composite','-pointsize','12','-annotate',f'+{xx+size+4}+{rows[5]+12}',label]
run([*args,'-quality','94'],V/'242-sheet-v3.jpg')
# Trang nhỏ để xem 100% thuận tiện, không phóng nội dung các ô 1×.
for idx,(start,count) in enumerate([(0,4),(4,4),(8,3)]):
 run([V/'242-sheet-v3.jpg','-crop',f'{W*count}x{H}+{W*start}+0','+repage','-quality','95'],V/f'242-sheet-v3-page-{idx+1}.jpg')
print("Revised proof sheets saved; assets unchanged.")
pair=['-size','640x256','xc:#111923','-gravity','NorthWest']
for j,tag in enumerate(['button','panel']):
 for row,res in enumerate(['720','1080']):
  for col,name in enumerate(['kills','stat-accuracy']):
   pair+=['(',P/(name+'-'+res+'-'+tag+'.png'),')','-geometry',f'+{col*320}+{(j*2+row)*64}','-composite']
run(pair,V/'242-kills-accuracy-v3-1x.png');run([V/'242-kills-accuracy-v3-1x.png','-filter','point','-resize','400%'],V/'242-kills-accuracy-v3-4x.png')
