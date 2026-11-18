#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re
from run import run, ROOT, OUT, TD_COPY as C, PARENT_COPY as P

def inventory(dist):
    entries = [{'path': str(p.relative_to(dist)), 'bytes': p.stat().st_size,
                'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
               for p in sorted(dist.rglob('*')) if p.is_file()]
    text = {str(p.relative_to(dist)): p.read_text(errors='replace') for p in dist.rglob('*')
            if p.is_file() and p.suffix in ['.html', '.js', '.css', '.json', '.txt', '.webmanifest']}
    return {'files': len(entries), 'bytes': sum(e['bytes'] for e in entries), 'entries': entries,
            'text_files': len(text), 'local_host': {p: s.count('typing-game.local') for p, s in text.items()},
            'prefixes': sorted({x for s in text.values() for x in re.findall(r'/assets/[a-z0-9-]+/', s)}),
            'model_files': [e['path'] for e in entries if Path(e['path']).suffix in ['.glb', '.gltf', '.bin']],
            'vite': (dist / '.vite').exists(), 'models': (dist / 'assets/typing-defense/models').exists()}

if __name__ == '__main__':
    checker = ['node', 'src/kit/tools/deploy/check-pack.mjs', 'dist', '--game', 'typing-defense', '--json']
    for name, script, url in [('production', 'deploy:pack', None), ('local', 'deploy:pack:local', 'https://typing-game.local/')]:
        assert run('deploy-' + name, ['pnpm', script], C, portal=url)['exit'] == 0
        argv = checker + (['--allow-local-host'] if name == 'local' else [])
        assert run('pack-' + name, argv, C, portal=url)['exit'] == 0
        data = inventory(C / 'dist')
        (OUT / ('dist-' + name + '.json')).write_text(json.dumps(data, indent=2) + '\n')
        (OUT / ('pack-' + name + '-result.json')).write_text((OUT / ('pack-' + name + '.log')).read_text())
        print(name, data['files'], data['bytes'], flush=True)
        assert not data['vite'] and not data['models'] and not data['model_files']
        if name == 'production': assert sum(data['local_host'].values()) == 0
        else: assert run('pack-local-production', checker, C)['exit'] == 1
    data = inventory(P / 'portal/dist')
    (OUT / 'portal-dist.json').write_text(json.dumps(data, indent=2) + '\n')
    js = [e for e in data['entries'] if e['path'].endswith('.js')]
    css = [e for e in data['entries'] if e['path'].endswith('.css')]
    print('portal', data['files'], 'JS', sum(e['bytes'] for e in js), 'CSS', sum(e['bytes'] for e in css))
