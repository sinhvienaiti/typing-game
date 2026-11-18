"""Hậu kỳ phiếu 225; chỉ ghi đường dẫn được giao, không ghi đè ảnh."""
from pathlib import Path
import sys, os, importlib.util, subprocess, json
sys.dont_write_bytecode = True
sys.path.insert(0,str(Path('tools/art-normalize').resolve()))
os.environ['ART_MAGICK']='/opt/homebrew/bin/magick'
game,name,attempt=sys.argv[1:4]
revision=sys.argv[4] if len(sys.argv)>4 else ''
tag=f'{name}.try{attempt}'+(f'.{revision}' if revision else '')
assert game in ['dragon-hold','typing-defense','typing-survival']
assert name in ['slider-track','slider-thumb']
base=Path(f'games/{game}/art-src/ui/quick-settings/sliders')
tmp=Path(f'games/{game}/tmp/codex-225');tmp.mkdir(parents=True,exist_ok=True)
spec=importlib.util.spec_from_file_location('normalize225','tools/art-normalize/normalize.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
n.WORK=tmp.resolve()
src=base/f'{name}.try{attempt}.png';alpha=tmp/f'{tag}.alpha.png'
if not alpha.exists():n.key(src,alpha,bg='#FF00FF',keep_alpha=game=='typing-survival',mode='global',despill='protect-interior',no_key_hue=bool(revision) and game!='typing-survival')
im=lambda args:subprocess.check_output(['/opt/homebrew/bin/magick',*map(str,args)])
w,h=map(int,im(['identify','-format','%w %h',alpha]).split())
b=im([alpha,'-depth','8','rgba:-']);xs=[];ys=[]
for y in range(h):
 for x in range(w):
  if b[(y*w+x)*4+3]>16:xs.append(x);ys.append(y)
bbox=[min(xs),min(ys),max(xs)-min(xs)+1,max(ys)-min(ys)+1]
crop=tmp/f'{tag}.crop.png'
if not crop.exists():im([alpha,'-crop',f'{bbox[2]}x{bbox[3]}+{bbox[0]}+{bbox[1]}','+repage','-define','png:color-type=6',crop])
target=tmp/f'{tag}.processed.png'
args=[crop,'-filter','Lanczos','-resize','1024x64!' if name=='slider-track' else '716x716']
if name=='slider-thumb':args+=['-gravity','center','-background','none','-extent','1024x1024']
if not target.exists():im(args+(['-channel','A','-level','1%,99%','+channel'] if revision else [])+['-depth','8','-define','png:color-type=6',target])
record={'game':game,'name':name,'tryNumber':int(attempt),'sourceSize':[w,h],'bboxAlphaGT16':bbox,'bboxRatio':bbox[2]/bbox[3],'ratioDeviationFrom16':abs(bbox[2]/bbox[3]/16-1) if name=='slider-track' else None,'scaleXY':[1024/bbox[2],64/bbox[3]] if name=='slider-track' else [716/max(bbox[2:])]*2,'processed':str(target),'operations':args}
p=Path(f'docs/codex-queue/225/postprocess-{game}-{tag}.json');assert not p.exists();p.write_text(json.dumps(record,ensure_ascii=False,indent=2,default=str)+'\n')
print(json.dumps(record,ensure_ascii=False,default=str))
