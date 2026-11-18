import json, os, re, subprocess, sys, time
from pathlib import Path
ROOT = Path.cwd()
OUT = ROOT / 'docs/codex-queue/228'
name, *argv = sys.argv[1:]
env = {**os.environ, 'GIT_OPTIONAL_LOCKS': '0', 'pnpm_config_verify_deps_before_run': 'false', 'NO_COLOR': '1'}
start = time.time()
result = subprocess.run(argv, cwd=ROOT, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
log = '$ ' + ' '.join(argv) + '\ncwd: ' + str(ROOT) + '\n\n' + output + '\nexit: ' + str(result.returncode) + '\n'
(OUT / (name + '.txt')).write_text('\n'.join(line.rstrip() for line in log.splitlines()) + '\n')
summary = {'argv': argv, 'cwd': str(ROOT), 'exit': result.returncode, 'seconds': round(time.time()-start, 3)}
for label in ['tests', 'pass', 'fail', 'skipped', 'suites']:
 match = re.search(r'^(?:# |ℹ )?'+label+r' (\d+)$', output, re.M)
 if match: summary[label] = int(match[1])
(OUT / (name + '.json')).write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary))
print('\n'.join(output.splitlines()[-12:]))
