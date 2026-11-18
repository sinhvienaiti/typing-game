from pathlib import Path
import json,hashlib,subprocess,difflib
ROOT=Path(__file__).resolve().parents[3]
W=ROOT/'games/.wt-td-codex'; O=Path(__file__).resolve().parent
before=json.loads((O/'before.json').read_text())
sha={p:hashlib.sha256((W/p).read_bytes()).hexdigest() for p in before['sha256']}
(O/'after.json').write_text(json.dumps({'sha256':sha},indent=2)+'\n')
status=subprocess.check_output(['git','status','--short','-uall'],cwd=W,text=True)
(O/'status-final.txt').write_text(status)
initial=[line[3:] for line in before['status'].splitlines()]
owned=['README.md','package.json','tests/deploy-pack.test.ts','src/app/learning.ts','src/app/portal.ts','vite.config.ts','deploy-models.json','scripts/deploy/prune.mjs','tests/portal.test.ts','tests/portal-build.test.ts','tests/deploy-prune.test.ts','docs/changelog/2026-10-30-deploy-pack.md']
paths=[line[3:] for line in status.splitlines()]
unknown=sorted(set(paths)-set(initial)-set(owned))
diff=subprocess.run(['git','diff','--check'],cwd=W,capture_output=True,text=True)
(O/'diff-check.txt').write_text(diff.stdout+diff.stderr)
scan=[];count=0; scanned=0
for f in sorted((W/'dist').rglob('*')):
 if f.is_file() and f.suffix.lower() in ['.html','.js','.css','.json']:
  scanned+=1; data=f.read_text(); matches=data.count('typing-game.local');count+=matches
  if matches:scan.append({'path':str(f.relative_to(W/'dist')),'count':matches})
parent=json.loads((ROOT/'package.json').read_text())['scripts']
package=json.loads((W/'package.json').read_text())['scripts'];old=json.loads((O/'before/package.json').read_text())['scripts']
changes={k:{'before208':old[k],'after208':package[k]} for k in ['deploy:pack','deploy:pack:local']}
(O/'package-changes.json').write_text(json.dumps(changes,indent=2)+'\n')
patch=[]
for name in owned:
 if (O/'before'/name).is_file(): original=(O/'before'/name).read_text()
 else:
  r=subprocess.run(['git','show','HEAD:'+name],cwd=W,capture_output=True,text=True)
  original=r.stdout if r.returncode==0 else ''
 patch.extend(difflib.unified_diff(original.splitlines(True),(W/name).read_text().splitlines(True),fromfile='a/'+name,tofile='b/'+name))
(O/'208-only.patch').write_text(''.join(patch))
final=json.loads((O/'dist-final.json').read_text());after=json.loads((O/'dist-after.json').read_text())
checks={'headUnchanged':subprocess.check_output(['git','rev-parse','HEAD'],cwd=W,text=True).strip()==before['head'], 'sha256Match':sha==before['sha256'],'hashFileCount':len(sha),'kitFileCount':len([p for p in sha if p.startswith('src/kit/')]),'goldenFileCount':len([p for p in sha if p.startswith('tests/golden/')]),'unknownPaths':unknown,'missing170Paths':sorted(set(initial)-set(paths)),'files170':initial,'files208':owned,'sharedPaths':sorted(set(initial)&set(owned)),'worktreeChangedPaths':len(paths),'diffCheckExit':diff.returncode,'productionTextFilesScanned':scanned,'productionLocalStringCount':count,'productionLocalMatches':scan,'modelsAbsent':not (W/'dist/assets/typing-defense/models').exists(),'viteAbsent':not (W/'dist/.vite').exists(),'productionRebuildIdentical':final==after,'fixtureRemainders':[str(p.relative_to(W)) for prefix in ['portal-build-','deploy-prune-','deploy-pack-test-'] for p in (W/'tmp').glob(prefix+'*')],'parentCommandsReadOnly':{k:parent[k] for k in ['build:td','dev:td:app']}}
(O/'verification.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n');print(json.dumps(checks,ensure_ascii=False,indent=2))
assert checks['sha256Match'] and not unknown and not checks['missing170Paths'] and diff.returncode==0
assert not count and checks['modelsAbsent'] and checks['viteAbsent'] and checks['productionRebuildIdentical'] and not checks['fixtureRemainders']
