from pathlib import Path
import json,sys,shutil,datetime
out=Path('docs/codex-queue/244'); jobs=json.loads((out/'prompts.json').read_text()); i=int(sys.argv[1]); job=jobs[i]; dest=Path(job['output'])
if dest.exists(): raise SystemExit('Không ghi đè '+str(dest))
shutil.copyfile(sys.argv[2],dest); dest.with_suffix('.prompt.txt').write_text(job['prompt'])
p=out/'calls.json'; calls=json.loads(p.read_text()) if p.exists() else []; calls.append({'index':i,'game':job['game'],'name':job['name'],'attempt':job.get('attempt',1),'at':datetime.datetime.now().astimezone().isoformat(),'source':sys.argv[2],'output':str(dest),'status':'ok'}); p.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n'); print(dest)
