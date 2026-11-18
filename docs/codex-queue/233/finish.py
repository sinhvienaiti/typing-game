#!/usr/bin/env python3
"""Kiểm bảo toàn trước khi xóa đúng hai cây tạm của phiếu 233."""
from pathlib import Path
import hashlib, json, os, re, shutil, subprocess
from run import ROOT as R, OUT as O, PARENT_COPY as P, TD_COPY as C

def git(w,*args):
    return subprocess.check_output(['git','--no-optional-locks','-C',str(w),*args],text=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):(O/name).write_text(json.dumps(obj,indent=2)+'\n')
before=json.loads((O/'before.json').read_text())
extra=C/'tests/codex-233-variants.test.ts'
if extra.exists():
    assert extra.read_bytes()==(O/'td-variants.test.ts').read_bytes()
    extra.unlink()
for name in ['integrity.json','cleanup.json','parent-diff-check.log','td-diff-check.log','td-status-after.txt']:
    if not (O/name).exists(): (O/name).write_text('')
integrity={}
for name,w,c in [('parent',R,P),('td',R/'games/.wt-td-codex',C)]:
    old=before[name]
    changed=[p for p,h in old['hashes'].items() if not (w/p).is_file() or sha(w/p)!=h]
    copy_changed=[p for p,h in old['hashes'].items() if not (c/p).is_file() or sha(c/p)!=h]
    status=git(w,'status','--short','-uall');(O/(name+'-status-after.txt')).write_text(status)
    start=set(old['status'].splitlines());end=set(status.splitlines())
    row={'branch':git(w,'branch','--show-current').strip(),'head':git(w,'rev-parse','HEAD').strip(),
         'hashed_files':len(old['hashes']),'changed_source':changed,'changed_copy':copy_changed,
         'status_before_lines':len(start),'status_after_lines':len(end),
         'status_added':sorted(end-start),'status_removed':sorted(start-end)}
    assert row['branch']==old['branch'] and row['head']==old['head']
    assert not changed and not copy_changed,row
    if name=='td':
        modules={p.name:{'symlink':p.is_symlink(),'mtime_ns':p.lstat().st_mtime_ns} for p in (w/'node_modules').iterdir()}
        results={str(p.relative_to(w)):p.stat().st_mtime_ns for p in (w/'node_modules/.vite').rglob('results.json')}
        row['node_modules_unchanged']=modules==old['node_modules']
        row['vitest_results_unchanged']=results==old['results']
        protected=[p for p in old['hashes'] if p.startswith(('src/kit/','tests/golden/')) or p=='public/assets/typing-defense/models/manifest.json']
        row['protected_unchanged']=len(protected)
        assert status==old['status'] and row['node_modules_unchanged'] and row['vitest_results_unchanged']
        newer=[]
        marker=(C.parent/'marker').stat().st_mtime_ns
        for base,dirs,files in os.walk(w,followlinks=False):
            dirs[:]=[d for d in dirs if d!='.git']
            for n in dirs+files:
                path=Path(base)/n
                if path.lstat().st_mtime_ns>marker:newer.append(str(path.relative_to(w)))
        row['worktree_newer_than_marker']=newer
        assert not newer,newer
    else:
        row['status_added_outside_233']=[s for s in end-start if not s[3:].startswith('docs/codex-queue/233/') and s[3:]!='docs/codex-queue/233-report.md']
        row['status_added_outside_233']=sorted(row['status_added_outside_233'])
        row['concurrent_status_paths_only']=all(s[3:].startswith(('docs/codex-queue/223/','docs/codex-queue/230/','docs/codex-queue/231/'))
            for s in row['status_added_outside_233']+row['status_removed'])
        assert row['concurrent_status_paths_only'],row
    integrity[name]=row
save('integrity.json',integrity)
# Save full final file lists as well as the scoped content hashes.
for name,w in [('parent',R),('td',R/'games/.wt-td-codex')]:
    result=subprocess.run(['git','--no-optional-locks','-C',str(w),'diff','--check'],capture_output=True,text=True)
    (O/(name+'-diff-check.log')).write_text('\n'.join(s.rstrip() for s in result.stdout.splitlines())+'\n')
    integrity[name]['diff_check_exit']=result.returncode
save('integrity.json',integrity)
cleanup={'removed':[]}
for path in [P,C.parent]:
    assert path in [R/'tmp/codex-233-portal',R/'games/typing-defense/tmp/codex-233']
    shutil.rmtree(path)
    cleanup['removed'].append({'path':str(path.relative_to(R)),'exists_after':path.exists()})
cleanup['tmp_before']=before['tmp_before']
cleanup['tmp_after']=[p.name for p in (R/'games/typing-defense/tmp').iterdir()]
cleanup['other_added']=sorted(set(cleanup['tmp_after'])-set(cleanup['tmp_before']))
cleanup['other_removed']=sorted(set(cleanup['tmp_before'])-set(cleanup['tmp_after']))
save('cleanup.json',cleanup)
print(json.dumps({'integrity':{k:{x:v for x,v in row.items() if x not in ['status_added','status_removed']} for k,row in integrity.items()},'cleanup':cleanup},indent=2))
