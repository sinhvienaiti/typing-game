#!/usr/bin/env python3
"""Kiểm bổ sung và tờ xem phiếu 245; chỉ ghi vào thư mục mới.
python3 docs/codex-queue/245/proofs.py <candidate-dir> <output-dir>
"""
import json,sys,subprocess,colorsys,statistics,random
from pathlib import Path
SRC=Path(sys.argv[1]);OUT=Path(sys.argv[2]);OUT.mkdir(parents=True,exist_ok=False)
ROOT=Path(__file__).resolve().parents[3];MAG='/opt/homebrew/bin/magick';FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
records=json.loads((SRC/'records.json').read_text());audit={}
def run(a):return subprocess.check_output([MAG,*map(str,a)])
def dim(p):return tuple(map(int,run(['identify','-format','%w %h',p]).split()))
def make(a,p):assert not p.exists(),p;run([*a,'-depth','8','-define','png:color-type=6',p]);return p
def rgba(p,n=None):return run([p,*(['-filter','Lanczos','-resize',f'{n}x{n}!'] if n else []),'-depth','8','rgba:-'])
def mask(p,n=None,t=128):
 b=rgba(p,n);return {i for i,a in enumerate(b[3::4]) if a>t}
def iou(a,b):return len(a&b)/max(1,len(a|b))
def caption(p,s,out):return make([p,'-background','#20242b','-gravity','south','-splice','0x24','-font',FONT,'-pointsize','12','-fill','#f3ead2','-annotate','+0+5',s],out)
def fixed(p,w,h,out):return make([p,'-filter','Lanczos','-resize',f'{w}x{h}','-background','#20242b','-alpha','remove','-alpha','off','-gravity','center','-extent',f'{w}x{h}'],out)
def montage(paths,p,tile):subprocess.check_call([MAG,'montage',*map(str,paths),'-background','#20242b','-geometry','+6+6','-tile',tile,str(p)])
def components(p):
 w,h=dim(p);S=mask(p,t=16);small=[];count=0
 while S:
  start=S.pop();stack=[start];n=1
  while stack:
   i=stack.pop();x=i%w
   for j,valid in [(i-1,x>0),(i+1,x<w-1),(i-w,i>=w),(i+w,i<w*(h-1))]:
    if valid and j in S:S.remove(j);stack.append(j);n+=1
  count+=1
  if n<20:small.append(n)
 return dict(component_count=count,islands_under_20=len(small),small_component_sizes=small)

blind=[]
for r in records:
 key=r['tag']+'-'+r['name'];p=SRC/(key+'.png');kind=r['kind'];info={}
 info['components_alpha_gt16']=components(p)
 if kind!='row':
  sizes={}
  for n in [1024,256,128,64]:
   q=p if n==1024 else SRC/(key+f'.{n}.png');b=rgba(q);alph=b[3::4];partial=[i for i,a in enumerate(alph) if 0<a<255]
   edge=run([q,'-alpha','extract','-bordercolor','black','-border','3','-threshold','50%','-morphology','Edge','Disk:3','-shave','3x3','-depth','8','gray:-'])
   pink=visible=opaque=0
   for i in range(0,len(b),4):
    if not b[i+3]:continue
    opaque+=1;h,s,v=colorsys.rgb_to_hsv(*(x/255 for x in b[i:i+3]))
    if 285<=h*360<=330 and s>.5:pink+=1;visible+=int(v>10/255)
   sizes[n]=dict(size=list(dim(q)),channels=run(['identify','-format','%[channels]',q]).decode(),alpha_min=min(alph),alpha_max=max(alph),partial_outside_3px=sum(not edge[i] for i in partial),strict_magenta_hue_pct=100*pink/max(1,opaque),magenta_hue_above_10_pct=100*visible/max(1,opaque),key_colour_applies=r['tag']!='ll')
  info['sizes']=sizes
  # Ô đọc không nhãn, số thứ tự chỉ thêm sau khi đảo thứ tự.
  if kind=='foe':
   bg=SRC/'word-720.png';ico=SRC/(key+'-720-icon.png');w,h=dim(bg)
   cell=make([bg,ico,'-geometry',f'+{(w-24)//2}+10','-composite'],OUT/(key+'-blind.png'))
  else:cell=SRC/(r['tag']+'-close-720.png')
  blind.append((key,cell))
 audit[key]=info

for tag in ['dh','ww']:
 a=SRC/(tag+'-list-row.png');b=SRC/(tag+'-list-row-active.png')
 audit[tag+'-list-exact']=dict(iou_1536x256=iou(mask(a),mask(b)),iou_300x34=iou(mask(SRC/(tag+'-720-row0.png')),mask(SRC/(tag+'-720-row1.png'))))
foes=[r for r in records if r['kind']=='foe'];audit['foe_pairs_32']=[]
for i,a in enumerate(foes):
 for b in foes[i+1:]:audit['foe_pairs_32'].append(dict(a=a['name'],b=b['name'],iou=iou(mask(SRC/('ll-'+a['name']+'.png'),32),mask(SRC/('ll-'+b['name']+'.png'),32))))

# Cỡ thật bổ sung trên mảnh button/panel thật, có nhãn tiếng Anh.
frame=ROOT/'games/typing-survival/art-src/ui/frames-epic'
for bgname,src,crop in [('button',frame/'button.alpha.png','250x64+250+224'),('panel',frame/'panel-large.alpha.png','250x64+240+240')]:
 bg=make([src,'-crop',crop,'+repage'],OUT/(bgname+'-crop.png'))
 cells720=[];cells1080=[]
 for r in foes:
  key='ll-'+r['name'];title=r['name'].split('.small')[0].replace('-',' ').title()
  for label,n in [('720',24),('1080',36)]:
   ico=SRC/(key+'-'+label+'-icon.png')
   cell=make([bg,ico,'-geometry',f'+8+{(64-n)//2}','-composite','-font',FONT,'-pointsize',str(round(n*.83)),'-fill','#f3ead2','-gravity','west','-annotate',f'+{n+16}+0',title],OUT/(key+'-'+label+'-'+bgname+'.png'))
   (cells720 if label=='720' else cells1080).append(cell)
   bb=rgba(bg);ib=rgba(ico);su=[];ba=[]
   for y in range(n):
    for x in range(n):
     j=4*(y*n+x);bi=4*((y+(64-n)//2)*250+x+8)
     if ib[j+3]>128:
      su.append(sum(ib[j+c]*v/255 for c,v in enumerate([.2126,.7152,.0722])))
      ba.append(sum(bb[bi+c]*v/255 for c,v in enumerate([.2126,.7152,.0722])))
   audit[key]['contrast_'+label+'_'+bgname]=statistics.mean(su)-statistics.mean(ba)
 montage(cells720,OUT/('foes-'+bgname+'-720.png'),'3x2');montage(cells1080,OUT/('foes-'+bgname+'-1080.png'),'3x2')

# Đảo thứ tự cố định; bảng ánh xạ chỉ mở sau khi ghi nhận đọc 1×.
random.Random(245).shuffle(blind);mapping={};tiles=[]
for i,(key,p) in enumerate(blind,1):
 mapping[str(i)]=key
 tile=make([p,'-background','#20242b','-gravity','center','-extent','180x90'],OUT/(f'blind-{i}.png'))
 tiles.append(caption(tile,str(i),OUT/(f'blind-{i}-number.png')))
montage(tiles,OUT/'blind-1x.png','3x3');(OUT/'blind-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')

# Tờ tổng hợp sáu hàng cho mỗi game. Không phóng các hàng cỡ thật.
for tag in ['dh','ww','ll']:
 rs=[r for r in records if r['tag']==tag and r['kind']!='row'];rowfiles=[]
 for row in range(6):
  tiles=[]
  for r in rs:
   key=tag+'-'+r['name'];kind=r['kind'];title=r['name'].replace('.small','')
   if row==0:q=SRC/(key+'.256.png');tile=fixed(q,280,280,OUT/(key+'-sheet0.png'))
   elif row in [1,2]:
    label='1080' if row==1 else '720';q=SRC/((tag+'-close-'+label+'.png') if kind=='icon' else (key+'-'+label+'.png'))
    tile=make([q,'-background','#20242b','-gravity','center','-extent','280x100'],OUT/(key+f'-sheet{row}.png'))
   elif row==3:
    q=SRC/((tag+'-close-720-4x.png') if kind=='icon' else 'foes-720-4x.png')
    if kind=='foe':
     q=make([SRC/(key+'-720.png'),'-filter','point','-resize','400%'],OUT/(key+'-cell4x.png'))
    tile=make([q,'-background','#20242b','-gravity','center','-extent','480x310'],OUT/(key+'-sheet3.png'))
   elif row==4:
    if kind=='foe':q=OUT/(key+'-720-button.png')
    else:
     # So sánh cùng cỡ với hai icon Settings/Sound thực của cùng game.
     folder=ROOT/r['folder'];iconroot=folder.parent/'quick-settings'
     if tag=='ww':iconroot=folder.parent/'quick-settings'
     siblings=[SRC/(key+'.png'),iconroot/'hud-settings.png',iconroot/'hud-sound.png'];small=[]
     for j,s in enumerate(siblings):
      small.append(make([s,'-filter','Lanczos','-resize','32x32'],OUT/(key+f'-compare-{j}.png')))
     q=make([*small,'+append'],OUT/(key+'-compare.png'))
    tile=make([q,'-background','#20242b','-gravity','center','-extent','280x100'],OUT/(key+'-sheet4.png'))
   else:
    if kind=='foe':
     old=ROOT/'games/typing-survival/art-src/ui/foes'/(title+'.v2.png');bg=SRC/'word-720.png'
     oldsmall=make([old,'-filter','Lanczos','-resize','24x24'],OUT/(key+'-old24.png'))
     before=make([bg,oldsmall,'-geometry','+44+10','-composite'],OUT/(key+'-before.png'))
     q=make([before,SRC/(key+'-720.png'),'+append'],OUT/(key+'-before-after.png'))
    else:
     bg=SRC/(tag+'-close-720.png')
     before=make([SRC/(tag+'-panel-720.png'),'-crop','120x76+240+0','+repage','-font',FONT,'-pointsize','14','-fill','#f3ead2','-gravity','center','-annotate','+0+8','Close'],OUT/(key+'-text-before.png'))
     q=make([before,bg,'+append'],OUT/(key+'-before-after.png'))
    tile=make([q,'-background','#20242b','-gravity','center','-extent','280x100'],OUT/(key+'-sheet5.png'))
   tiles.append(caption(tile,title,OUT/(key+f'-sheet{row}-caption.png')))
  rowfile=OUT/(tag+f'-row{row}.png');montage(tiles,rowfile,f'{len(tiles)}x1');rowfiles.append(rowfile)
 make([*rowfiles,'-background','#20242b','-gravity','center','-append'],OUT/(tag+'-sheet.png'))
 subprocess.check_call([MAG,str(OUT/(tag+'-sheet.png')),'-background','#20242b','-alpha','remove','-quality','92',str(OUT/(tag+'-sheet.jpg'))])
 if tag!='ll':
  montage([SRC/(tag+'-list-1080.png'),SRC/(tag+'-list-720.png')],OUT/(tag+'-list-sizes.png'),'2x1')
  make([SRC/(tag+'-list-720.png'),'-filter','point','-resize','400%'],OUT/(tag+'-list4x.png'))

(OUT/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print('done',OUT)
