#!/usr/bin/env python3
"""Chép bằng chứng sau khi 16 lệnh kết thúc; không xóa bản chép."""
from pathlib import Path
import subprocess,shutil,hashlib,json,re
ROOT=Path(__file__).resolve().parents[4];D=ROOT/'docs/codex-queue/226';TD=ROOT/'games/typing-defense';W=TD/'tmp/codex-226'
records=json.loads((W/'runs/commands.json').read_text())
assert len(records)==16 and all(r['exit']==0 and r['headers_valid'] for r in records)
assert all(r['threads']<=4 and (r['load1']<=10 or r['threads']<=2) for r in records)
assert all(records[i]['end']<=records[i+1]['start'] for i in range(len(records)-1))
assert all(r['command'][:6]==['nice','-n','15','node','--import','tsx'] for r in records)
header_checks=[]
for c in ['base','pkg']:
 for suffix,need in [('balance160',['seed 1–80','seed 81–160','## Gộp 2 bộ seed (160 ván mỗi ô)']),('g12x20',['seed 1–12','(20 seed, 4 đêm']),('pn-balanced',['seeds 25–48']),('pn-relax',['seeds 25–48']),('pn-challenge',['seeds 25–48']),('night1-40',['seeds 1–40']),('night1-160',['seeds 1–160'])]:
  p=W/'runs'/f'{c}-{suffix}.md';s=p.read_text();assert all(x in s for x in need)
  header_checks.append({'file':p.name,'need':need,'pass':True})
R=D/'runs';R.mkdir(exist_ok=True);hashes=[]
for src in sorted((W/'runs').iterdir())+[W/'refs.txt']:
 assert src.is_file()
 dst=R/src.name;shutil.copyfile(src,dst)
 a=hashlib.sha256(src.read_bytes()).hexdigest();b=hashlib.sha256(dst.read_bytes()).hexdigest();assert a==b
 hashes.append({'file':str(dst.relative_to(D)),'sha256':a,'source':str(src.relative_to(ROOT)),'source_sha256':b,'match':True})
(D/'runs.sha256').write_text('\n'.join(x['sha256']+'  '+x['file']+'  == '+x['source']+'  MATCH' for x in hashes)+'\n')
diff=subprocess.run(['diff','-ru','-x','node_modules','-x','probe','base','pkg'],cwd=W,capture_output=True,text=True);assert diff.returncode==1
(D/'base-pkg.diff').write_text(diff.stdout)
def lines(s):return sorted(l for l in s.splitlines() if l.startswith(('+','-')) and not l.startswith(('+++','---')))
a=lines(diff.stdout);b=lines((W/'a2-package-v2.patch').read_text());assert a==b
assert len([l for l in diff.stdout.splitlines() if l.startswith('@@')])==11
assert sum(l.startswith('+') for l in a)==45 and sum(l.startswith('-') for l in a)==15
with (D/'git-after.txt').open('w') as f:
 for cmd in [['git','-C',str(TD.relative_to(ROOT)),'status','--short'],['git','-C',str(TD.relative_to(ROOT)),'branch','--show-current']]:
  f.write('$ '+' '.join(cmd)+'\n');p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True);assert p.returncode==0;f.write(p.stdout+p.stderr)
status_equal=(D/'git-before.txt').read_bytes()==(D/'git-after.txt').read_bytes()
ls=subprocess.run(['find',str(W.relative_to(ROOT)),'-maxdepth','2'],cwd=ROOT,capture_output=True,text=True);assert ls.returncode==0
(D/'delete-list.txt').write_text('\n'.join(sorted(ls.stdout.splitlines()))+'\n')
noise=[r['tag'] for r in records if 'nice: setpriority: Operation not permitted' in (W/'runs'/(r['tag']+('.err' if r['command'][6]=='scripts/td/balance.ts' else '.md'))).read_text()]
checks={'commands':len(records),'measurements':14,'smokes':2,'exit0':sum(r['exit']==0 for r in records),'max_threads':max(r['threads'] for r in records),'load_gt10_commands':[{'tag':r['tag'],'threads':r['threads'],'load1':r['load1']} for r in records if r['load1']>10],'sequential':True,'header_checks':header_checks,'copied_files':len(hashes),'sha256_matched':sum(x['match'] for x in hashes),'game_status_and_branch_unchanged':status_equal,'sysctl_denied_count':sum(r['sysctl_exit']!=0 for r in records),'nice_denied_count':len(noise),'nice_denied_commands':noise,'diff_exit':diff.returncode,'diff_change_lines_match':a==b,'wall_seconds':round(sum(r['elapsed_seconds'] for r in records),3)}
(D/'execution-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(checks,ensure_ascii=False,indent=2))
