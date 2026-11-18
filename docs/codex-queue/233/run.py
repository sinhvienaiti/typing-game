#!/usr/bin/env python3
"""Chạy kiểm ngoại tuyến trong bản chép, lưu lệnh và đầu ra."""
from pathlib import Path
import json, os, re, subprocess, time, sys

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'docs/codex-queue/233'
PARENT_COPY = ROOT / 'tmp/codex-233-portal'
TD_COPY = ROOT / 'games/typing-defense/tmp/codex-233/tree'

def run(name, argv, cwd, portal=None, timeout=180):
    env = os.environ.copy()
    env.pop('VITE_PORTAL_URL', None)
    if portal is not None:
        env['VITE_PORTAL_URL'] = portal
    env['pnpm_config_verify_deps_before_run'] = 'false'
    env['TMPDIR'] = str((TD_COPY.parent / 'tmpdir') if cwd == TD_COPY else PARENT_COPY / 'tmp')
    start = time.monotonic()
    result = subprocess.run(argv, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=timeout)
    log = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout)
    (OUT / (name + '.log')).write_text('\n'.join(line.rstrip() for line in log.splitlines()) + '\n')
    row = {'name': name, 'argv': argv, 'cwd': str(cwd), 'portal_url': portal,
           'exit': result.returncode, 'seconds': round(time.monotonic() - start, 3)}
    for key in ['tests', 'pass', 'fail', 'skipped']:
        hits = re.findall(r'^[#ℹ]?\s*' + key + r' (\d+)\s*$', log, re.M)
        if hits: row[key] = int(hits[-1])
    for key, pattern in [('test_files', r'Test Files\s+([^\n]+)'), ('vitest_tests', r'Tests\s+([^\n]+)')]:
        found = re.findall(pattern, log)
        if found: row[key] = found[-1].strip()
    (OUT / (name + '.json')).write_text(json.dumps(row, indent=2) + '\n')
    print(json.dumps(row), flush=True)
    return row

if __name__ == '__main__':
    kind, name, *argv = sys.argv[1:]
    row = run(name, argv, {'parent': ROOT, 'portal': PARENT_COPY, 'td': TD_COPY}[kind])
    sys.exit(row['exit'])
