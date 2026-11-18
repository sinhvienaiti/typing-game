#!/usr/bin/env python3
"""Chạy đúng các đột biến 228/229, chỉ sửa bản chép."""
from pathlib import Path
import hashlib, json, sys
from run import run, ROOT, OUT, PARENT_COPY, TD_COPY

def execute(name, target, mutate, argv, cwd):
    original = target.read_bytes()
    changed = mutate(original.decode())
    assert changed != original.decode(), name
    row = {'id': name, 'file': str(target.relative_to(cwd)),
           'sha256': hashlib.sha256(original).hexdigest()}
    try:
        target.write_text(changed)
        row['mutated'] = run(name + '-mutated', argv, cwd)
    finally:
        target.write_bytes(original)
        assert target.read_bytes() == original
    row['restored'] = run(name + '-restored', argv, cwd)
    row['restored_sha256'] = hashlib.sha256(target.read_bytes()).hexdigest()
    assert row['mutated']['exit'] == 1 and row['restored']['exit'] == 0, row
    return row

def once(s, old, new):
    assert s.count(old) == 1, repr(old)
    return s.replace(old, new, 1)

if sys.argv[1] == 'parent':
    # Read definitions only; never execute the old runner or its mutation loop.
    definitions = (ROOT / 'docs/codex-queue/228/mutate.py').read_text().split('results = []')[0]
    scope = {}
    exec(compile(definitions, '228-mutation-definitions', 'exec'), scope)
    rows = []
    for name, path, change, tests in scope['cases']:
        argv = ['node', '--test', '--test-name-pattern=' + name.upper(), *tests]
        rows.append(execute(name, PARENT_COPY / path, change, argv, PARENT_COPY))
        (OUT / 'parent-mutations.json').write_text(json.dumps(rows, indent=2) + '\n')
else:
    plans = [
        ('M5', 'scripts/deploy/prune.mjs', 'if (lstatSync(at).isSymbolicLink())',
         'if (false && lstatSync(at).isSymbolicLink())', 'tests/deploy-prune.test.ts', 'rejects a linked'),
        ('M6', 'src/app/learning.ts', 'let bridge: LearningBridge | null = null;',
         'let bridge: LearningBridge | null = createPortalBridge();', 'tests/portal.test.ts', 'creates one real bridge'),
        ('P1-01-query', 'vite.config.ts', 'const path = id.split("?")[0]!.replace(/\\\\/g, "/");',
         'const path = id.replace(/\\\\/g, "/");', 'tests/portal-id.test.ts', 'rewrites the real build through'),
        ('P1-01-realpath', 'vite.config.ts', 'return realpathSync(path);', 'return path;',
         'tests/portal-id.test.ts', 'rewrites the real build through'),
        ('P1-01-guard', 'vite.config.ts', 'if (!error && !transformed)', 'if (false && !error && !transformed)',
         'tests/portal-id.test.ts', 'never transforms'),
        ('P1-02', 'scripts/deploy/prune.mjs', 'return lstatSync(path, { throwIfNoEntry: false });',
         'return existsSync(path) ? lstatSync(path) : undefined;', 'tests/deploy-prune.test.ts', 'rejects dangling'),
    ]
    rows = []
    for name, path, old, new, test, pattern in plans:
        def change(s):
            s = once(s, old, new)
            if name == 'P1-02': s = once(s, 'import { lstatSync,', 'import { existsSync, lstatSync,')
            return s
        rows.append(execute(name, TD_COPY / path, change,
                    ['pnpm', 'exec', 'vitest', 'run', test, '-t', pattern], TD_COPY))
        (OUT / 'td-mutations.json').write_text(json.dumps(rows, indent=2) + '\n')
