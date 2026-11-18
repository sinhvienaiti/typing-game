import json
from pathlib import Path
import subprocess
import sys

phase, label, *command = sys.argv[1:]
folder = Path('docs/codex-queue/214') / phase
folder.mkdir(parents=True, exist_ok=True)
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
(folder / f'{label}.log').write_text('$ ' + ' '.join(command) + '\n' + result.stdout)
(folder / f'{label}.json').write_text(json.dumps({'command': command, 'exit_code': result.returncode}, indent=2) + '\n')
if label.startswith('build') and result.returncode == 0:
    assets = {str(p): p.stat().st_size for pattern in ('index-*.js', 'index-*.css')
              for p in sorted(Path('portal/dist/assets').glob(pattern))}
    (folder / 'bundle-bytes.json').write_text(json.dumps(assets, indent=2) + '\n')
print(f'{phase}/{label}: exit {result.returncode}')
print('\n'.join(result.stdout.splitlines()[-12:]))
