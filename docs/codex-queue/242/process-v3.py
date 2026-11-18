#!/usr/bin/env python3
"""Phiếu 242: hậu kỳ/kiểm ảnh bằng ImageMagick 7, chỉ tạo file mới.
Chạy: python3 docs/codex-queue/242/process.py <thư-mục-mới> [selection.json]
Không cần Pillow, numpy, mạng hoặc runtime game.
"""
import json, subprocess, sys, math, colorsys, random
from pathlib import Path
MAG='/opt/homebrew/bin/magick'; FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
ROOT=Path(__file__).resolve().parents[3]; ICON=ROOT/'games/typing-survival/art-src/ui/icons'; FRAME=ICON.parent/'frames-epic'
DATA=json.loads((Path(__file__).parent/'assets.json').read_text())
OUT=Path(sys.argv[1]); OUT.mkdir(exist_ok=False,parents=True)
SEL=json.loads(Path(sys.argv[2]).read_text()) if len(sys.argv)>2 else {}
def run(args):return subprocess.check_output([MAG,*map(str,args)])
def make(args,p):
 assert not Path(p).exists(),p
 run([*args,'-define','png:color-type=6',p]);return Path(p)
def dim(p):return tuple(map(int,run(['identify','-format','%w %h',p]).split()))
def rgba(p,size=None):
 args=[p]
 if size:args+=['-filter','Lanczos','-resize',f'{size}x{size}']
 return run([*args,'-alpha','on','-depth','8','rgba:-'])
def mask(p,n,t=128):
 b=rgba(p,n);return {(i%n,i//n) for i,a in enumerate(b[3::4]) if a>t}
def bounds(S):
 xs=[x for x,y in S];ys=[y for x,y in S];return min(xs),min(ys),max(xs)+1,max(ys)+1
def clean_alpha(src,dst):
 b=bytearray(rgba(src));w,h=dim(src)
 edge50=run([src,'-alpha','extract','-threshold','50%','-morphology','Edge','Disk:3','-depth','8','gray:-'])
 edge16=run([src,'-alpha','extract','-threshold',str(16/255*100)+'%','-morphology','Edge','Disk:3','-depth','8','gray:-'])
 count=0;maximum=0
 for i,a in enumerate(b[3::4]):
  if (edge50[i]!=0 and edge16[i]!=0) or a in (0,255):continue
  target=0 if a<128 else 255
  if abs(target-a)<=16:
   b[i*4+3]=target;count+=1;maximum=max(maximum,abs(target-a))
 assert not Path(dst).exists()
 subprocess.run([MAG,'-size',f'{w}x{h}','-depth','8','rgba:-','-colorspace','sRGB','-define','png:color-type=6',str(dst)],input=bytes(b),check=True)
 return dict(pixels_changed=count,max_alpha_delta=maximum,rgb_pixels_changed=0)
# Mép Euclid r=3: IM Disk kernel. Lưu hai định nghĩa đường bao >16 và >=128.
def alpha_metrics(p):
 b=rgba(p);a=b[3::4]; w,h=dim(p); partial={i for i,v in enumerate(a) if 0<v<255};result={}
 for threshold in [16,127]:
  edge=run([p,'-alpha','extract','-threshold',f'{threshold/255*100:.9f}%','-morphology','Edge','Disk:3','-depth','8','gray:-'])
  result[str(threshold)]=sum(edge[i]==0 for i in partial)
 color=0;nonzero=0
 for i in range(0,len(b),4):
  if not b[i+3]:continue
  nonzero+=1
  h0,s,v=colorsys.rgb_to_hsv(*(x/255 for x in b[i:i+3])); hue=h0*360
  color+=int(285<=hue<=315 and s>.5)
 return dict(partial_outside_3px=result,key_magenta_pct=100*color/max(1,nonzero))
def opening(S):
 E={(x,y) for x,y in S if all((x+dx,y+dy) in S for dx,dy in [(0,0),(1,0),(0,1),(1,1)])}
 return {(x+dx,y+dy) for x,y in E for dx,dy in [(0,0),(1,0),(0,1),(1,1)]}
def luma(b):return .2126*b[0]/255+.7152*b[1]/255+.0722*b[2]/255
# Vùng cắt nguyên pixel từ lòng khung thật; không tô lại nền.
BG={}
for tag,src,geom in [('button',FRAME/'button.png','260x64+220+160'),('panel',FRAME/'panel-large.png','260x64+230+230')]:
 BG[tag]=make([src,'-crop',geom,'+repage','-colorspace','sRGB'],OUT/(tag+'-crop.png'))

def tile(p,size,label,tag,path):
 ps=max(1,round(size*.83)) # Arial cap-height xấp xỉ 0,72 em → 0,60 icon.
 args=[BG[tag],'(',p,'-filter','Lanczos','-resize',f'{size}x{size}',')','-gravity','NorthWest','-geometry',f'+8+{(64-size)//2}','-compose','Over','-composite']
 if label:args+=['-font',FONT,'-pointsize',ps,'-fill','#eef4f8','-gravity','West','-annotate',f'+{size+14}+0',label]
 return make(args,path)
metrics={};candidates={};SMALL=[]
for a in DATA:
 name=a['name'];base=a['base'];n=SEL.get(name,1);stem=base+('-try' if name!='stat-words' else '.try')+str(n);src=ICON/(stem+'.png')
 b=rgba(src);w,h=dim(src);S={(i%w,i//w) for i,v in enumerate(b[3::4]) if v>16};x0,y0,x1,y1=bounds(S)
 # Cắt khoảng alpha thấp ở mép; không sửa RGB, không threshold alpha trong vật.
 pre=make([src,'-crop',f'{x1-x0}x{y1-y0}+{x0}+{y0}','+repage','-filter','Lanczos','-resize','717x717','-background','none','-gravity','center','-extent','1024x1024','-colorspace','sRGB','-depth','8'],OUT/(base+'-pre-matte.png'))
 p=OUT/(base+'.png'); cleanup=clean_alpha(pre,p)
 candidates[name]=p
 sizes={1024:p}
 for size in [256,128,64]:sizes[size]=make([p,'-filter','Lanczos','-resize',f'{size}x{size}','-colorspace','sRGB','-depth','8'],OUT/(base+f'.{size}.png'))
 S=mask(p,1024,16);x0,y0,x1,y1=bounds(S)
 m=dict(matte=cleanup,source=str(src.relative_to(ROOT)),bbox=[x0,y0,x1,y1],extent_pct=max(x1-x0,y1-y0)/1024*100,centre_offset_pct=max(abs((x0+x1)/2-512),abs((y0+y1)/2-512))/1024*100,alpha={})
 for size,f in sizes.items():m['alpha'][size]=alpha_metrics(f)
 S=mask(p,a['s720']);x0,y0,x1,y1=bounds(S)
 m['opening_pct']=100*len(opening(S))/len(S);m['coverage_pct']=100*len(S)/((x1-x0)*(y1-y0));m['contrast']={}
 for res in ['720','1080']:
  size=a['s'+res]
  for tag in BG:
   t=tile(p,size,a['label'],tag,OUT/(name+'-'+res+'-'+tag+'.png'))
   if res=='720' and tag=='panel':SMALL.append((name,t))
   if res=='720':make([t,'-filter','point','-resize','400%'],OUT/(name+'-'+res+'-'+tag+'-4x.png'))
   fg=rgba(p,size);bg=rgba(BG[tag]);ws=0;diff=0
   for y in range(size):
    for x in range(size):
     i=(y*size+x)*4;alpha=fg[i+3]/255;j=(((64-size)//2+y)*260+8+x)*4
     ws+=alpha;diff+=alpha*(luma(fg[i:i+3])-luma(bg[j:j+3]))
   m['contrast'][res+'-'+tag]=abs(diff/max(ws,1))
 # Bản sinh | hậu kỳ: hai ô 512²; chỉ fit, không méo.
 make(['-size','1024x556','xc:#14181f','(',src,'-resize','512x512','-background','none','-gravity','center','-extent','512x512',')','-gravity','NorthWest','-geometry','+0+32','-composite','(',p,'-resize','512x512',')','-geometry','+512+32','-composite','-font',FONT,'-pointsize','18','-fill','white','-gravity','NorthWest','-annotate','+12+8','Generated','-annotate','+524+8','Postprocessed'],OUT/(name+'-before-after.png'))
 metrics[name]=m
# IoU với đúng các tên ở bảng, cả hai ngưỡng để không chọn cách đo có lợi.
for a in DATA:
 m=metrics[a['name']];m['iou']={}
 for other in a['compare']:
  othername=other.replace('.r2','')
  q=candidates.get(othername) if '.r2' in other or othername=='stat-words' else None
  if q is None:q=ICON/(other+'.png')
  if not q.exists():m['iou'][other]={'missing':str(q)};continue
  scores={}
  for t in [16,128]:
   A=mask(candidates[a['name']],32,t);B=mask(q,32,t);scores[str(t)]=len(A&B)/max(1,len(A|B))
  m['iou'][other]=scores
# Tờ đọc cỡ thật bỏ nhãn, xáo thứ tự. Không đọc mapping trước khi viết nhận xét.
order=list(DATA);random.Random(242).shuffle(order)
args=['-size',f'260x{len(order)*48}','xc:#10151d']
for i,a in enumerate(order):
 args+=['(',BG['panel'], '-crop','260x48+0+8','+repage','(',candidates[a['name']],'-filter','Lanczos','-resize',f"{a['s720']}x{a['s720']}",')','-gravity','NorthWest','-geometry',f"+8+{(48-a['s720'])//2}",'-composite',')','-gravity','NorthWest','-geometry',f'+0+{i*48}','-composite','-font',FONT,'-pointsize','14','-fill','white','-annotate',f'+64+{i*48+16}',str(i+1)]
make(args,OUT/'blind-1x.png')
(OUT/'blind-mapping.json').write_text(json.dumps([a['name'] for a in order],indent=2))
(OUT/'metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2))
for name,m in metrics.items():print(name,'opening',round(m['opening_pct'],2),'coverage',round(m['coverage_pct'],2),'contrast',round(m['contrast']['720-panel'],3),'IoU',m['iou'])
