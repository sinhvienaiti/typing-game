from pathlib import Path
import hashlib,json,subprocess,sys,re,platform
from run import WT,OUT
before=json.loads((OUT/'before.json').read_text())
status=subprocess.check_output(['git','status','--short','-uall'],cwd=WT).decode()
(OUT/'status-after.txt').write_text(status)
paths=set(subprocess.check_output(['git','ls-files','-z'],cwd=WT).decode().split('\0'))|{line[3:] for line in status.splitlines()}
paths.discard('')
after={p:hashlib.sha256((WT/p).read_bytes()).hexdigest() for p in sorted(paths) if (WT/p).is_file()}
changed=[p for p,h in before['paths'].items() if after.get(p)!=h]
added=sorted(set(after)-set(before['paths']))
allowed=['vite.config.ts','scripts/deploy/prune.mjs','tests/deploy-prune.test.ts','tests/portal.test.ts','tests/portal-id.test.ts','docs/changelog/2026-10-30-fix-224-findings.md']
assert set(changed+added)==set(allowed),(changed,added)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=WT).decode().strip()
assert head==before['head']
protected=[p for p in before['paths'] if p.startswith('src/kit/') or p.startswith('tests/golden/') or p=='public/assets/typing-defense/models/manifest.json']
assert len(protected)==37,len(protected)
assert all(after[p]==before['paths'][p] for p in protected)
diff=subprocess.run(['git','diff','--check'],cwd=WT,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(OUT/'diff-check.txt').write_bytes(diff.stdout);assert diff.returncode==0
for name in ['production','local','final']:
    result=json.loads((OUT/('pack-'+name+'.log')).read_text())
    assert result['ok'] and not result['problems']
    (OUT/('pack-'+name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
cross=json.loads((OUT/'pack-local-production.log').read_text())
assert len(cross['problems'])==1 and cross['problems'][0]['code']=='local-host'
(OUT/'pack-local-production.json').write_text(json.dumps(cross,indent=2)+'\n')
fixture_leftovers=[p.name for p in (WT/'tmp').iterdir() if p.name.startswith(('portal-id-','deploy-prune-'))]
assert not fixture_leftovers,fixture_leftovers
summary={'head':head,'branch':subprocess.check_output(['git','branch','--show-current'],cwd=WT).decode().strip(),'changed':changed,'added':added,'allowed':allowed,'protected_unchanged':len(protected),'protected_paths':protected,'before_paths':len(before['paths']),'after_paths':len(after),'status_before_lines':len(before['status'].splitlines()),'status_after_lines':len(status.splitlines()),'diff_check_exit':diff.returncode,'fixture_leftovers':fixture_leftovers,'platform':platform.platform(),'versions':{cmd:subprocess.check_output([cmd,'--version']).decode().strip() for cmd in ['node','pnpm']},'source_sha256':{p:after[p] for p in allowed}}
for key in ['before','after']:
    log=(OUT/('check-'+key+'.log')).read_text()
    summary['check_'+key]={'files':re.search(r'Test Files\s+(\d+) passed',log).group(1),'tests':re.search(r'\n\s*Tests\s+(\d+) passed',log).group(1),'kit':33,'exit':json.loads((OUT/('check-'+key+'-run.json')).read_text())['exit']}
(OUT/'verification.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'after.json').write_text(json.dumps({'head':head,'paths':after,'status':status},indent=2)+'\n')
print(json.dumps(summary,indent=2))
