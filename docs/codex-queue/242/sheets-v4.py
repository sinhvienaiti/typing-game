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
P=D/'proofs-v3'
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
 args+=['(',P/(name+'-720-panel.png'),'-crop',f'{size+8}x64+0+0','+repage','-filter','point','-resize','400%',')','-geometry',f'+{x+(W-4*(size+8))//2}+{rows[3]}','-composite']
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
run([*args,'-quality','94'],V/'242-sheet-v4.jpg')
# Trang nhỏ để xem 100% thuận tiện, không phóng nội dung các ô 1×.
for idx,(start,count) in enumerate([(0,4),(4,4),(8,3)]):
 run([V/'242-sheet-v4.jpg','-crop',f'{W*count}x{H}+{W*start}+0','+repage','-quality','95'],V/f'242-sheet-v4-page-{idx+1}.jpg')
print("Final v4 sheets saved.")
