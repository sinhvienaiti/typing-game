#!/usr/bin/env python3
"""Giao bản chọn phiếu 245, chỉ tạo file mới và xác minh KA1.
python3 docs/codex-queue/245/deliver.py <candidate> <proofs>
"""
import json,sys,hashlib,subprocess,difflib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];BASE=Path(__file__).parent
SRC=Path(sys.argv[1]);PROOF=Path(sys.argv[2]);MAG='/opt/homebrew/bin/magick'
M=json.loads((SRC/'metrics.json').read_text());A=json.loads((PROOF/'audit.json').read_text());R=json.loads((SRC/'records.json').read_text())
def newcopy(src,dst):
 src=Path(src);dst=Path(dst);assert not dst.exists(),dst
 with dst.open('xb') as f:f.write(src.read_bytes())
 return dict(path=str(dst.relative_to(ROOT)),md5=hashlib.md5(dst.read_bytes()).hexdigest())
def meanval(x):return x['mean_subject_minus_bg']
assert max(x['iou'] for x in M['foe_pairs_24'])<=.70
assert max(x['iou'] for x in A['foe_pairs_32'])<=.80
for tag in ['dh','ww']:assert A[tag+'-list-exact']['iou_1536x256']>=.95
files=[];planned=[]
for r in R:
 key=r['tag']+'-'+r['name'];m=M[key];a=A[key];folder=ROOT/r['folder'];name=r['name']
 assert m['partial_outside_3px']==0 and m['alpha_min']==0 and m['alpha_max']==255,key
 assert a['components_alpha_gt16']['islands_under_20']==0,key
 suffixes=['.png','.prompt.txt']
 if r['kind']=='row':
  assert m['slice_pct']<=25 and m['rail_luma_stdev_max']<=.05 and m['text_wcag']>=7,key
  suffixes+=['.json']
 else:
  assert 68<=m['longside_pct']<=72 and max(map(abs,m['centre_offset_pct']))<=2,key
  assert m['opening_pct']>=80 and m['coverage_pct']>=30,key
  assert meanval(m['contrast_720'])>=.25 and meanval(m['contrast_1080'])>=.25,key
  for n,v in a['sizes'].items():assert v['partial_outside_3px']==0,(key,n,v)
  for n in [256,128,64]:suffixes += [f'.{n}.png',f'.{n}.prompt.txt']
 for suffix in suffixes:
  source=SRC/(key+suffix);target=folder/(name+suffix)
  assert source.exists() and not target.exists(),(source,target)
  planned.append((source,target))

for source,target in planned:files.append(newcopy(source,target))

for tag,game in [('dh','dragon-hold'),('ww','typing-defense'),('ll','typing-survival')]:
 folder=ROOT/'games'/game/'art-src/_review';folder.mkdir(exist_ok=True)
 # Tờ sáu hàng của icon; hàng danh sách có tờ riêng và bản 1× nguyên pixel.
 files.append(newcopy(PROOF/(tag+'-sheet.jpg'),folder/'245-sheet.jpg'))
 for label in ['720','1080']:
  for scale in ['', '-4x']:
   name=tag+'-close-'+label+scale+'.png';files.append(newcopy(SRC/name,folder/('245-close-'+label+scale+'.png')))
 if tag!='ll':
  for label in ['720','1080']:
   for scale in ['', '-4x']:
    name=tag+'-list-'+label+scale+'.png';files.append(newcopy(SRC/name,folder/('245-list-'+label+scale+'.png')))
 else:
  for label in ['720','1080']:
   for scale in ['1x','4x']:
    files.append(newcopy(SRC/('foes-'+label+'-'+scale+'.png'),folder/('245-foes-'+label+'-'+scale+'.png')))
 raws=[SRC/(r['tag']+'-'+r['name']+'-raw-vs-final.png') for r in R if r['tag']==tag]
 dest=folder/'245-raw-vs-final.jpg';assert not dest.exists()
 subprocess.check_call([MAG,'montage',*map(str,raws),'-background','#20242b','-geometry','+8+8','-tile','1x'+str(len(raws)),'-quality','92',str(dest)])
 files.append(dict(path=str(dest.relative_to(ROOT)),md5=hashlib.md5(dest.read_bytes()).hexdigest()))

folders=[ROOT/'games/dragon-hold/art-src/ui/frames',ROOT/'games/typing-defense/art-src/ui/frames-epic',ROOT/'games/typing-survival/art-src/ui/frames-epic',ROOT/'games/typing-survival/art-src/ui/foes']
paths=sorted(x for p in folders for x in p.rglob('*') if x.is_file())
after=subprocess.check_output(['md5','-r',*(str(p.relative_to(ROOT)) for p in paths)],cwd=ROOT).decode()
assert not (BASE/'md5-after.txt').exists();(BASE/'md5-after.txt').write_text(after)
before=(BASE/'md5-before.txt').read_text()
def mapping(s):return {line.split(' ',1)[1]:line.split(' ',1)[0] for line in s.splitlines()}
b=mapping(before);a=mapping(after);changed=[p for p,h in b.items() if a.get(p)!=h]
diff=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after'))
(BASE/'md5-diff.txt').write_text(diff)
result=dict(existing_files=len(b),after_files=len(a),added=len(a.keys()-b.keys()),changed=changed,removed=sorted(b.keys()-a.keys()),files=files)
(BASE/'delivered.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
assert not changed and not result['removed'],result
print('delivered',len(files),'files; KA1',result['added'],'added, 0 changed, 0 removed')
