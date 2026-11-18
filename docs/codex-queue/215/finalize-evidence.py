from pathlib import Path
import hashlib
import json
import subprocess

root = Path.cwd()
p = root / 'docs/codex-queue/215'
product = [
 'shared/learning/core.mjs', 'shared/learning/core.d.mts',
 'shared/learning/query.mjs', 'shared/learning/query.d.mts',
 'shared/learning/message-contract.mjs', 'shared/learning/message-contract.d.mts',
 'shared/learning/profile-backup.mjs', 'shared/learning/lookup.test.mjs',
 'shared/learning/README.md', 'portal/src/learning/bridge.ts',
 'portal/tests/learning-lookup.test.mjs',
 'docs/changelog/2026-10-30-portal-learning-lookup.md',
 'docs/codex-queue/215-report.md',
]
(p / 'logs').mkdir(exist_ok=True)
for log in p.glob('*.log'):
 (p / 'logs' / (log.stem + '.txt')).write_text('\n'.join(line.rstrip(' \t') for line in log.read_text().splitlines()) + '\n')
baseline = json.loads((p / 'baseline.json').read_text())
after_bytes = {kind:sum(f.stat().st_size for f in (root / 'portal/dist/assets').glob('*.' + kind)) for kind in ['js','css']}
(p / 'bundle-bytes.json').write_text(json.dumps({
 'before': baseline['bundleBytes'], 'after': after_bytes,
 'delta': {k:after_bytes[k] - baseline['bundleBytes'][k] for k in after_bytes},
 'includesWorkers': True,
}, indent=2) + '\n')
start = json.loads((p / 'start.json').read_text())
head = subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
(p / 'head-advance.txt').write_text(subprocess.check_output(['git','log','--oneline',start['head']+'..'+head],text=True) + subprocess.check_output(['git','diff','--stat',start['head'],head],text=True))
changed_sources = subprocess.check_output(['git','diff','--name-only',start['head'],head,'--','portal','shared/learning','package.json','pnpm-lock.yaml'],text=True).splitlines()
# Create evidence destinations before the final status snapshot.
for name in ['verification.json','files.txt','status-delta.json','diff-check.txt']:
 (p / name).touch(exist_ok=True)
files = sorted(set(product + [str(f.relative_to(root)) for f in p.rglob('*') if f.is_file() and f.suffix != '.log']))
(p / 'files.txt').write_text('\n'.join(files) + '\n')
check = subprocess.run(['git','diff','--check','--',*files],text=True,capture_output=True)
whitespace = []
for name in files:
 for line_number, line in enumerate((root / name).read_text().splitlines(),1):
  if line.rstrip(' \t') != line or line.startswith(('<<<<<<< ', '=======', '>>>>>>> ')):
   whitespace.append({'file':name,'line':line_number})
(p / 'diff-check.txt').write_text(check.stdout + check.stderr + f'git diff --check exit: {check.returncode}\n' + f'Whitespace/conflict findings: {len(whitespace)}\n')
status = subprocess.check_output(['git','status','--short','-uall'],text=True)
(p / 'status-after.txt').write_text(status)
before_lines = set((p / 'status-before.txt').read_text().splitlines())
after_lines = set(status.splitlines())
def owned(line):
 name = line[3:]
 return name in product or name.startswith('docs/codex-queue/215/')
added = sorted(after_lines - before_lines)
removed = sorted(before_lines - after_lines)
delta = {
 'addedOrChanged215': [line for line in added if owned(line)],
 'addedOrChangedOtherWorkers': [line for line in added if not owned(line)],
 'removed215': [line for line in removed if owned(line)],
 'removedOtherWorkers': [line for line in removed if not owned(line)],
}
(p / 'status-delta.json').write_text(json.dumps(delta,indent=2,ensure_ascii=False) + '\n')
verification = {
 'branch': subprocess.check_output(['git','branch','--show-current'],text=True).strip(),
 'headAtStart': start['head'], 'headAfter': head,
 'interveningSourceChanges': changed_sources,
 'buildBeforeExit': int((p / 'build-baseline.exit').read_text()),
 'buildAfterExit': int((p / 'build-after.exit').read_text()),
 'learningCheckExit': int((p / 'learning-check.exit').read_text()),
 'diffCheckExit': check.returncode, 'whitespaceFindings': whitespace,
 'coreSnapshotsIdentical': (p / 'core-before.json').read_bytes() == (p / 'core-after.json').read_bytes(),
 'globalStatus215Deltas': len(delta['addedOrChanged215']) + len(delta['removed215']),
 'globalStatusOtherWorkerAdditions': len(delta['addedOrChangedOtherWorkers']),
 'globalStatusOtherWorkerRemovals': len(delta['removedOtherWorkers']),
 'productHashes': {name:hashlib.sha256((root / name).read_bytes()).hexdigest() for name in product},
}
(p / 'verification.json').write_text(json.dumps(verification,indent=2,ensure_ascii=False) + '\n')
assert check.returncode == 0 and not whitespace
assert not changed_sources and verification['coreSnapshotsIdentical']
assert verification['buildBeforeExit'] == verification['buildAfterExit'] == verification['learningCheckExit'] == 0
print(json.dumps({key:value for key,value in verification.items() if key != 'productHashes'}, indent=2))
print(json.dumps(json.loads((p/'bundle-bytes.json').read_text()),indent=2))
print(json.dumps({key:value for key,value in delta.items() if 'OtherWorker' in key},indent=2,ensure_ascii=False))
