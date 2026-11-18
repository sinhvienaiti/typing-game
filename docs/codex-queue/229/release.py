from pathlib import Path
import hashlib,json
from run import run,WT,OUT

def inventory(name):
    dist=WT/'dist'
    files=[{'path':str(p.relative_to(dist)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(dist.rglob('*')) if p.is_file()]
    textfiles=[p for p in sorted(dist.rglob('*')) if p.is_file() and p.suffix in ['.html','.js','.css','.json']]
    data={'files':len(files),'bytes':sum(p['bytes'] for p in files),'entries':files,'text_files':len(textfiles),'local_host':[str(p.relative_to(dist)) for p in textfiles if 'typing-game.local' in p.read_text(errors='replace')], 'models':(dist/'assets/typing-defense/models').exists(), 'vite':(dist/'.vite').exists()}
    (OUT/('dist-'+name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
    print(name,data['files'],data['bytes'],'bytes',flush=True)
    assert not data['models'] and not data['vite']
    return data

checker=['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','typing-defense','--json']
assert run('golden',['pnpm','td:golden:check'])==0
assert run('deploy-production',['pnpm','deploy:pack'])==0
assert run('pack-production',checker)==0
prod=inventory('production');assert not prod['local_host']
assert run('deploy-local',['pnpm','deploy:pack:local'],portal='https://typing-game.local/')==0
assert run('pack-local',checker+['--allow-local-host'],portal='https://typing-game.local/')==0
local=inventory('local')
assert run('pack-local-production',checker)==1
assert run('deploy-final',['pnpm','deploy:pack'])==0
assert run('pack-final',checker)==0
final=inventory('final')
assert final==prod
