import subprocess,time,os,json,hashlib
from pathlib import Path
R=Path('/Users/toandx/htdocs/typing-game'); C=R/'games/dragon-hold/tmp/codex-222'; os.chdir(C/'tree')
records=[]
def run(name,args,env=None):
 start=time.monotonic()
 with (C/'logs'/name).open('w') as out:
  p=subprocess.run(args,stdout=out,stderr=subprocess.STDOUT,env=env)
 rec={'log':name,'command':args,'exitCode':p.returncode,'seconds':round(time.monotonic()-start,3)}; records.append(rec)
 (C/'logs/commands.json').write_text(json.dumps(records,indent=2)+'\n')
 print(json.dumps(rec),flush=True)
 return p.returncode
for name,args in [('kit.log',['node','src/kit/verify-kit.mjs']),('tests.log',['node_modules/.bin/vitest','run']),('tsc.log',['node_modules/.bin/tsc','--noEmit']),('build.log',['node_modules/.bin/vite','build'])]:
 run(name,args)
with (C/'logs/check-fallback.log').open('w') as out:
 for n in ['kit.log','tests.log','tsc.log','build.log']:
  out.write('\nCOMMAND LOG: '+n+'\n'+(C/'logs'/n).read_text())
run('golden.log',['node_modules/.bin/vitest','run','tests/golden/golden.test.ts'])
(C/'logs/golden-md5.txt').write_text(hashlib.md5(Path('tests/golden/m0.json').read_bytes()).hexdigest()+'\n')
run('english-ui.log',['node_modules/.bin/vitest','run','tests/english-ui.test.ts'])
run('prepare-check.log',['node','scripts/ui-art/prepare.mjs','--check','--art-src',str(R/'games/dragon-hold/art-src')])
local=os.environ.copy();local['VITE_PORTAL_URL']='https://typing-game.local/'
run('pack-local-build.log',['node_modules/.bin/tsc','--noEmit'],local)
run('pack-local-vite.log',['node_modules/.bin/vite','build'],local)
run('pack-local.json',['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','dragon-hold','--json','--allow-local-host'],local)
prod=os.environ.copy();prod.pop('VITE_PORTAL_URL',None)
run('pack-prod-tsc.log',['node_modules/.bin/tsc','--noEmit'],prod)
run('pack-prod-build.log',['node_modules/.bin/vite','build'],prod)
run('pack-prod.json',['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','dragon-hold','--json'],prod)
found=[str(f) for f in Path('dist').rglob('*') if f.is_file() and b'typing-game.local' in f.read_bytes()]
(C/'logs/prod-local-host-scan.json').write_text(json.dumps({'count':len(found),'files':found},indent=2)+'\n')
load=subprocess.run(['uptime'],capture_output=True,text=True);(C/'logs/uptime.txt').write_text(load.stdout+load.stderr)
try: load1=float(load.stdout.split('load averages:')[1].strip().split()[0])
except Exception: load1=os.getloadavg()[0]
jobs=2 if load1>10 else 4
balance=os.environ.copy();balance['TSX_DISABLE_CACHE']='1'
run('balance-b35.md',['node','--import=tsx','scripts/balance/run.ts','--seeds=20','--bots=b35',f'--jobs={jobs}',f'--json={C}/logs/balance-b35.json'],balance)
run('idle-estimate.json',['node','scripts/balance/idle-estimate.mjs',str(R/'games/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json')])
for p in ['lib/dh.mjs','dh-bench.mjs','dh-camera.mjs','dh-map-shots.mjs','dh-models.mjs','dh-pace.mjs','ui-preview.mjs']:
 run('syntax-'+Path(p).stem+'.log',['node','--check','scripts/visual/scenarios/'+p])
source=R/'games/dragon-hold/tmp/map1-audit/feel-35-1280/samples.json'
(C/'logs/samples-after.sha256').write_text(hashlib.sha256(source.read_bytes()).hexdigest()+'  '+str(source)+'\n')
print('SECTION 3 COMPLETE',flush=True)
