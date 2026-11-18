#!/usr/bin/env python3
"""Preflight chỉ đọc, in ra stdout; không tự ghi/xóa hoặc tiếp tục khi sai."""
from pathlib import Path
import os, subprocess, sys
root=Path.cwd();wt=root/'games/.wt-td-codex';failures=[]
def command(args,expected=None,env=None):
    p=subprocess.run(args,cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    print('$ '+' '.join(args));print(p.stdout,end='');print(f'[exit {p.returncode}]')
    if p.returncode or (expected is not None and p.stdout.strip()!=expected):failures.append(args)
    return p.stdout
command(['git','-C',str(wt),'branch','--show-current'],'td-codex')
command(['git','-C',str(wt),'rev-parse','HEAD'],'f9abfd09987dadd519233c2f38692758d35cefca')
status=command(['git','-C',str(wt),'--no-optional-locks','status','--short','-uall'])
ref=root/'docs/codex-queue/208/status-final.txt'
p=subprocess.run(['diff','-',str(ref)],input=status,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
print('$ status | diff - docs/codex-queue/208/status-final.txt');print(p.stdout,end='');print(f'[exit {p.returncode}]')
if p.returncode:failures.append('status diff')
names=['208/208-only.patch','208/before/package.json','208/before/README.md','208/before/tests/deploy-pack.test.ts','208/dist-final.json','208/after.json','208/status-final.txt','208/run.py','170/dist-inventory.json','170-td-pack-and-kit.md','168-ts-pack-and-kit.md','208-td-deploy-pack.md','170-report.md']
for name in names:
    good=(root/'docs/codex-queue'/name).is_file();print(name,good)
    if not good:failures.append(name)
temp=root/'games/typing-defense/tmp/codex-224'
print('temp exists:',temp.exists())
if temp.exists():failures.append('temp tồn tại: cần xác minh sở hữu trước, không tự xóa')
node=command(['node','-v'])
try:
    if int(node.strip().lstrip('v').split('.')[0])<24:failures.append('node <24')
except ValueError:failures.append('node không đọc được')
env=os.environ.copy();env['pnpm_config_verify_deps_before_run']='false'
command(['pnpm','-v'],'11.21.0',env)
for path in ['/usr/bin/rsync','/usr/bin/patch']:
    good=Path(path).is_file() and os.access(path,os.X_OK);print(path,good)
    if not good:failures.append(path)
print('FAILURES:',failures)
sys.exit(1 if failures else 0)
