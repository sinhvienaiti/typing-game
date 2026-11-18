#!/usr/bin/env python3
"""Phiếu 224: chạy từ gốc repo cha; chỉ ghi bằng chứng và bản chép của phiếu."""
from pathlib import Path
import argparse, collections, hashlib, json, os, re, shutil, subprocess, time

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'docs/codex-queue/224'
WT = ROOT / 'games/.wt-td-codex'
C = ROOT / 'games/typing-defense/tmp/codex-224'
HEAD = 'f9abfd09987dadd519233c2f38692758d35cefca'

def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def git(*args):
    return subprocess.check_output(['git', '-C', str(WT), *args])

def sha(data):
    return hashlib.sha256(data).hexdigest()

def entry(base, path):
    data = (base / path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': sha(data)}

def source_paths():
    tracked = [p.decode() for p in git('ls-files', '-co', '--exclude-standard', '-z').split(b'\0') if p]
    public = [p.relative_to(WT).as_posix() for p in (WT / 'public').rglob('*') if p.is_file()]
    return tracked, sorted(set(tracked + public))

def modules():
    items = []
    for p in sorted((WT / 'node_modules').iterdir()):
        st = p.lstat()
        items.append({'name': p.name, 'type': 'symlink' if p.is_symlink() else 'directory' if p.is_dir() else 'file', 'mtime_ns': st.st_mtime_ns})
    results = [{'path': p.relative_to(WT).as_posix(), 'mtime_ns': p.stat().st_mtime_ns} for p in sorted((WT / 'node_modules/.vite/vitest').glob('*/results.json'))]
    return {'items': items, 'vitest_results': results}

def snapshot(name):
    tracked, paths = source_paths()
    protected = json.loads((OUT.parent / '208/after.json').read_text())['sha256']
    hashes = {p: sha((WT / p).read_bytes()) for p in protected}
    data = {'branch': git('branch', '--show-current').decode().strip(), 'head': git('rev-parse', 'HEAD').decode().strip(),
            'status': git('--no-optional-locks', 'status', '--short', '-uall').decode(),
            'ls_files_count': len(tracked), 'file_count': len(paths), 'entries': [entry(WT, p) for p in paths],
            'protected_sha256': hashes, 'protected_match_208': sum(hashes[p] == protected[p] for p in hashes),
            'node_modules': modules(), 'main_tmp': sorted(p.name for p in (ROOT / 'games/typing-defense/tmp').iterdir())}
    save(name, data)
    return data

def copy():
    assert not C.exists(), 'Thư mục tạm đã tồn tại'
    before = snapshot('before.json')
    assert before['head'] == HEAD and before['status'] == (OUT.parent / '208/status-final.txt').read_text()
    assert before['file_count'] == 329 and before['protected_match_208'] == 37
    for d in ['tree', 'tree-170', 'tmpdir']:
        (C / d).mkdir(parents=True)
    (C / 'marker').touch()
    paths = git('ls-files', '-co', '--exclude-standard', '-z')
    report = {}
    for d in ['tree', 'tree-170']:
        base = C / d
        subprocess.run(['/usr/bin/rsync', '-a', '--from0', '--files-from=-', str(WT) + '/', str(base) + '/'], input=paths, check=True)
        subprocess.run(['/usr/bin/rsync', '-a', str(WT / 'public') + '/', str(base / 'public') + '/'], check=True)
        nm = base / 'node_modules'; nm.mkdir()
        for p in sorted((WT / 'node_modules').iterdir()):
            if p.name not in ['.vite', '.vite-temp', '.pnpm-workspace-state-v1.json']:
                (nm / p.name).symlink_to(p)
        inv = inventory(base, excludes={'node_modules'})
        report[d] = {**inv, 'comparison': compare(inv['entries'], before['entries']),
                     'node_modules_real_directory': not nm.is_symlink(),
                     'symlinks': [{'name': p.name, 'target': str(p.readlink())} for p in sorted(nm.iterdir())]}
    save('copy.json', report)
    print(json.dumps({k: {'file_count': v['file_count'], 'comparison': v['comparison'], 'symlinks': len(v['symlinks'])} for k,v in report.items()}, ensure_ascii=False))

def inventory(base, excludes=set()):
    paths = []
    for here, dirs, files in os.walk(base, followlinks=False):
        if Path(here) == base: dirs[:] = [d for d in dirs if d not in excludes]
        paths.extend((Path(here) / f).relative_to(base).as_posix() for f in files)
    entries = [entry(base, p) for p in sorted(paths)]
    return {'file_count': len(entries), 'bytes': sum(e['bytes'] for e in entries), 'entries': entries}

def compare(actual, expected):
    a, b = ({e['path']: e for e in seq} for seq in [actual, expected])
    same = [p for p in a.keys() & b.keys() if a[p]['sha256'] == b[p]['sha256']]
    return {'same_sha256': len(same), 'changed': [{'path': p, 'actual_bytes': a[p]['bytes'], 'expected_bytes': b[p]['bytes']} for p in sorted(a.keys() & b.keys()) if a[p]['sha256'] != b[p]['sha256']], 'added': sorted(a.keys()-b.keys()), 'missing': sorted(b.keys()-a.keys())}

def run(name, args, tree='tree', portal=None, json_output=False, timeout=240):
    env = os.environ.copy(); env.pop('VITE_PORTAL_URL', None)
    if portal is not None: env['VITE_PORTAL_URL'] = portal
    env['pnpm_config_verify_deps_before_run'] = 'false'
    env['TMPDIR'] = str(C / 'tmpdir')
    start = time.monotonic()
    p = subprocess.run(args, cwd=C / tree, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    duration = time.monotonic() - start
    (OUT / (name + ('.json' if json_output else '.log'))).write_bytes(p.stdout if json_output else p.stdout + p.stderr)
    if json_output and p.stderr: (OUT / (name + '.stderr.log')).write_bytes(p.stderr)
    result = {'command': args, 'cwd': str((C / tree).relative_to(ROOT)), 'env': {'VITE_PORTAL_URL': portal if portal is not None else '(absent)', 'pnpm_config_verify_deps_before_run': 'false', 'TMPDIR': str(C / 'tmpdir')}, 'exit': p.returncode, 'seconds': round(duration, 4)}
    save(name + '-run.json', result)
    print(name, p.returncode, result['seconds'], flush=True)
    return p

def split():
    patch = (OUT.parent / '208/208-only.patch').read_bytes()
    p = subprocess.run(['/usr/bin/patch', '-R', '-p1', '-E', '-d', str(C / 'tree-170')], input=patch, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (OUT / 'split.log').write_bytes(b'$ /usr/bin/patch -R -p1 -E -d games/typing-defense/tmp/codex-224/tree-170 < docs/codex-queue/208/208-only.patch\n' + p.stdout + f'\nexit={p.returncode}\n'.encode())
    base = C / 'tree-170'
    new208 = ['src/app/portal.ts','deploy-models.json','scripts/deploy/prune.mjs','tests/portal.test.ts','tests/portal-build.test.ts','tests/deploy-prune.test.ts','docs/changelog/2026-10-30-deploy-pack.md']
    common = ['package.json','README.md','tests/deploy-pack.test.ts']
    allpaths = [e['path'] for e in inventory(base, {'node_modules'})['entries'] if e['path'] != 'public/assets/typing-defense/ui/title-dusk.webp']
    changed = []
    headpaths = set(p.decode() for p in git('ls-files', '-z').split(b'\0') if p)
    for path in sorted(set(allpaths) | headpaths):
        old = git('show', 'HEAD:' + path) if path in headpaths else b''
        file = base / path
        if not file.exists() or path not in headpaths or file.read_bytes() != old:
            changed.append({'path': path, 'type': 'modified' if path in headpaths else 'new'})
    report = {'exit': p.returncode, 'patched_files': len(re.findall(rb'^patching file ', p.stdout, re.M)),
              'patch_artifacts': [str(p.relative_to(base)) for pat in ['*.rej','*.orig'] for p in base.rglob(pat)],
              'deleted_new_208': {x: not (base / x).exists() for x in new208},
              'same_head': {x: (base / x).read_bytes() == git('show', 'HEAD:' + x) for x in ['src/app/learning.ts','vite.config.ts']},
              'same_before': {x: (base / x).read_bytes() == (OUT.parent / '208/before' / x).read_bytes() for x in common}, 'changed_170': changed}
    save('split.json', report)
    # Đếm dòng từng phiếu bằng diff trong bộ nhớ; không dùng git apply.
    import difflib
    before = json.loads((OUT / 'before.json').read_text())
    rows = []
    for line in before['status'].splitlines():
        path = line[3:]; final = (WT / path).read_bytes(); state170 = (base / path).read_bytes() if (base / path).is_file() else b''
        initial = git('show', 'HEAD:' + path) if path in headpaths else b''
        def delta(a,b):
            diff = list(difflib.unified_diff(a.decode().splitlines(),b.decode().splitlines()))[2:]
            return {'added': sum(s.startswith('+') for s in diff), 'removed': sum(s.startswith('-') for s in diff)}
        group = 'cả hai' if path in common else '170' if final == state170 else '208'
        rows.append({'path':path,'group':group,'170':delta(initial,state170),'208':delta(state170,final),'total':delta(initial,final)})
    save('paths.json', rows)
    print(json.dumps(report, ensure_ascii=False))

def scan(label):
    base = C / 'tree/dist'; inv = inventory(base)
    report = {'local_host': {}, 'asset_prefixes': collections.Counter(), 'model_extensions': {'.glb':0,'.gltf':0,'.bin':0}, 'has_vite': (base / '.vite').exists(), 'has_models': (base / 'assets/typing-defense/models').exists(), 'text_files': 0}
    for e in inv['entries']:
        path = e['path']; ext = Path(path).suffix.lower()
        if ext in ['.glb','.gltf','.bin']: report['model_extensions'][ext] = report['model_extensions'].get(ext,0)+1
        if ext not in ['.html','.js','.css','.json','.webmanifest','.txt']: continue
        report['text_files'] += 1
        text = (base / path).read_text()
        count = text.count('typing-game.local')
        report['local_host'][path] = count
        report['asset_prefixes'].update(re.findall(r'/assets/[^/\s"\'<>`]+/', text))
    report['asset_prefixes'] = dict(report['asset_prefixes'])
    scans = json.loads((OUT / 'scan.json').read_text()) if (OUT / 'scan.json').exists() else {}
    scans[label] = report; save('scan.json', scans)
    save('dist-' + label + '.json', inv)
    return inv

def builds():
    run('check-170',['pnpm','check'],tree='tree-170')
    run('deploy-170',['pnpm','deploy:pack'],tree='tree-170')
    run('pack-170',['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','typing-defense','--json'],tree='tree-170',json_output=True)
    run('pack-170-local',['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','typing-defense','--json','--allow-local-host'],tree='tree-170',json_output=True)
    inv=inventory(C/'tree-170/dist'); save('dist-170.json',inv)
    save('dist-170-comparison.json',compare(inv['entries'],json.loads((OUT.parent/'170/dist-inventory.json').read_text())['entries']))
    manifest=(C/'tree-170/dist/.vite/manifest.json').read_text()
    save('manifest-paths.json',{'node_modules_paths':re.findall(r'"([^"\n]*node_modules/[^"\n]*)"',manifest),'relative_prefix':os.path.relpath(WT,C/'tree-170')+'/'})
    run('check',['pnpm','check'])
    # Lưu số build thường trước bước deploy dọn .vite.
    save('build-only.json',inventory(C/'tree/dist'))
    run('golden',['pnpm','td:golden:check'])
    for label,portal,script in [('absent',None,'deploy:pack'),('empty','','deploy:pack'),('local','https://typing-game.local/','deploy:pack:local')]:
        run('deploy-'+label,['pnpm',script],portal=portal)
        args=['node','src/kit/tools/deploy/check-pack.mjs','dist','--game','typing-defense','--json']
        run('pack-'+label,args+(['--allow-local-host'] if label=='local' else []),portal=portal,json_output=True)
        if label=='local': run('pack-local-production',args,portal=portal,json_output=True)
        inv=scan(label)
        if label=='empty': save('dist-empty-comparison.json',compare(inv['entries'],json.loads((OUT.parent/'208/dist-final.json').read_text())['files']))

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('stage',choices=['copy','split','builds']);args=parser.parse_args()
    {'copy':copy,'split':split,'builds':builds}[args.stage]()
