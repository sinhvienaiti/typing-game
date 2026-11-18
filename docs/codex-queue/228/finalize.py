import hashlib, json, os, subprocess
from pathlib import Path
OUT=Path('docs/codex-queue/228')
ENV={**os.environ,'GIT_OPTIONAL_LOCKS':'0'}
def git(*args): return subprocess.check_output(['git',*args],text=True,env=ENV)
def allowed(p):
    return p.startswith(('portal/src/','portal/tests/','docs/codex-queue/228/')) or p in ['portal/public/games.json','docs/codex-queue/228-report.md','docs/changelog/2026-10-30-fix-227.md','scripts/validate-play-mode.mjs','scripts/validate-play-mode.test.mjs','infra/nginx/typing-game.local.play.conf','infra/nginx/typing-game.local.dev.conf'] or (p.startswith('shared/learning/') and (p.endswith('.test.mjs') or p.split('/')[-1] in [n+e for n in ['core','query','message-contract','profile-backup'] for e in ['.mjs','.d.mts']]))
(OUT/'whitespace.json').touch()
products=(OUT/'product-files.txt').read_text().splitlines()
new=[str(p) for p in sorted(OUT.rglob('*')) if p.is_file()]+['docs/changelog/2026-10-30-fix-227.md','docs/codex-queue/228-report.md']
checks=[]
for argv in [['git','diff','--check','--',*products]]+[['git','diff','--no-index','--check','/dev/null',f] for f in products+new]:
    result=subprocess.run(argv,env=ENV,text=True,capture_output=True)
    checks.append({'argv':argv,'exit':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    assert not result.stdout and not result.stderr, checks[-1]
    assert result.returncode in [0,1], checks[-1]
(OUT/'whitespace.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
pre=json.loads((OUT/'preflight.json').read_text())
hashes=json.loads((OUT/'hashes-before.json').read_text())
current={f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in hashes}
(OUT/'hashes-after.json').write_text(json.dumps(current,indent=2)+'\n')
status=git('status','--short','-uall');(OUT/'status-after.txt').write_text(status)
before=set((OUT/'status-before.txt').read_text().splitlines());after=set(status.splitlines())
added=sorted(after-before);removed=sorted(before-after)
changed=[f for f in hashes if hashes[f]!=current[f]]
scope={'branchBefore':pre['branch'],'branchAfter':git('branch','--show-current').strip(),'headBefore':pre['head'],'headAfter':git('rev-parse','HEAD').strip(),'statusBeforeLines':len(before),'statusAfterLines':len(after),'statusAdded':added,'statusRemoved':removed,'statusDeltaOutsideAllowed':[x for x in added+removed if not allowed(x[3:])],'changedScopedFiles':changed,'changedScopedOutsideAllowed':[f for f in changed if not allowed(f)],'scopedUnchangedCount':len(hashes)-len(changed),'buildFoldersRemoved':all(not (OUT/('build-'+p)).exists() for p in ['before','after']),'validatorFixturesRemoved':not Path('tmp/validate-play-mode-test').exists()}
assert not scope['changedScopedOutsideAllowed']
assert scope['branchBefore']==scope['branchAfter']
assert scope['headBefore']==scope['headAfter']
(OUT/'scope.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in scope.items() if k not in ['statusAdded','statusRemoved']},ensure_ascii=False,indent=2))
print('Whitespace checks:',len(checks),'with no diagnostics; new-file exit 1 means content differs from /dev/null.')
