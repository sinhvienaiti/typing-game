from pathlib import Path
import re, sys, hashlib, json
root=Path(__file__).resolve().parents[1]
source=next((root/'source').iterdir())
files=sorted(f for f in source.glob('[0-9][0-9][0-9]_*.md') if f.name!='000_INDEX.md')
a,b=map(int,sys.argv[1:3]); seen={}; manifest=[]
for f in files:
 text=f.read_text(); n=int(f.name[:3]); chunks=[]; repeats=0
 for match in re.finditer(r'\S[\s\S]*?(?=\n\s*\n|\Z)',text):
  para=match.group(); line=text.count('\n',0,match.start())+1
  if para in seen: repeats+=1
  else:
   seen[para]=f'{f.name}:{line}'
   chunks.append(f'L{line}: {para}')
 if a<=n<=b:
  print(f'\n===== {f.name} (all novel paragraphs; {repeats} exact repeated paragraphs already read) =====\n'+'\n\n'.join(chunks))
 manifest.append({'id':n,'file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'lines':len(text.splitlines()),'novel_paragraphs':len(chunks),'exact_repeat_paragraphs':repeats})
(root/'READ_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
