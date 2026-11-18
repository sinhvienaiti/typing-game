#!/usr/bin/env python3
"""Phiếu 226: chỉ chạy các phép đo đã được chủ dự án chỉ định, tuần tự."""
from pathlib import Path
import subprocess, os, datetime, time, re, json, shutil
ROOT=Path(__file__).resolve().parents[4]
TD=ROOT/'games/typing-defense'; W=TD/'tmp/codex-226'; E=TD/'tmp/mac-2026-10-27/open/a2-days'
RUN=W/'runs'; records=[]
def now(): return datetime.datetime.now().astimezone().isoformat()
def log(s):
 with (RUN/'timeline.txt').open('a') as f:f.write(s+'\n');f.flush()
def run(tree,tag,entry,args,smoke=False):
 date=subprocess.run(['date','+%F %T'],capture_output=True,text=True)
 up=subprocess.run(['uptime'],capture_output=True,text=True)
 sy=subprocess.run(['sysctl','-n','vm.loadavg'],capture_output=True,text=True)
 source=sy.stdout if sy.returncode==0 else up.stdout
 nums=re.findall(r'\d+\.\d+',source)
 if not nums: raise RuntimeError('Không đọc được tải 1 phút')
 load=float(nums[0]); threads=2 if smoke or load>10 else 4
 is_balance=entry=='scripts/td/balance.ts'
 cmd=['nice','-n','15','node','--import','tsx',entry,*args]
 if is_balance:cmd.append('--threads='+str(threads))
 start=now();t=time.monotonic()
 rec=dict(tree=tree,tag=tag,start=start,load1=load,load_source='sysctl' if sy.returncode==0 else 'uptime (sysctl bị sandbox chặn)',threads=threads if is_balance else 1,command=cmd,cwd=str(W/tree),uptime=up.stdout.strip(),sysctl_exit=sy.returncode,sysctl_error=sy.stderr.strip())
 log('\nBEGIN '+tag+' '+start+'\n$ date \'+%F %T\'\n'+date.stdout+'$ uptime\n'+up.stdout+'$ sysctl -n vm.loadavg\n'+sy.stdout+sy.stderr+'sysctl_exit='+str(sy.returncode)+'\nload_source='+rec['load_source']+'; load1='+str(load)+'; threads='+str(rec['threads'])+'\n$ '+' '.join(cmd))
 print('BEGIN',tag,start,'load',load,'threads',rec['threads'],flush=True)
 env=os.environ.copy();env['TMPDIR']=str(W/'tmpdir')
 with (RUN/(tag+'.md')).open('w') as out:
  if is_balance:
   with (RUN/(tag+'.err')).open('w') as err:p=subprocess.run(cmd,cwd=W/tree,env=env,stdout=out,stderr=err)
  else:p=subprocess.run(cmd,cwd=W/tree,env=env,stdout=out,stderr=subprocess.STDOUT)
 rec.update(end=now(),elapsed_seconds=round(time.monotonic()-t,3),exit=p.returncode)
 text=(RUN/(tag+'.md')).read_text()
 if smoke: valid='seed 1–2' in text and '2 luồng' in text.splitlines()[-1]
 elif tag.endswith('balance160'):valid=all(s in text for s in ['seed 1–80','seed 81–160','## Gộp 2 bộ seed (160 ván mỗi ô)'])
 elif tag.endswith('g12x20'):valid='seed 1–12' in text and 'Cổng `BUILD_1A6.md` §12' in text
 elif '-pn-' in tag:valid='seeds 25–48' in text
 else:valid='seeds 1–'+tag.rsplit('-',1)[1] in text
 rec['headers_valid']=valid
 records.append(rec);(RUN/'commands.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
 log('END '+tag+' '+rec['end']+' exit='+str(p.returncode)+' elapsed_seconds='+str(rec['elapsed_seconds'])+' headers_valid='+str(valid))
 print('END',tag,'exit',p.returncode,'seconds',rec['elapsed_seconds'],'headers',valid,flush=True)
 if p.returncode or not valid:raise RuntimeError('Dừng: '+tag)
for c in ['base','pkg']:run(c,c+'-smoke','scripts/td/balance.ts',['--stage-seeds=2','--stage-sets=1','--quick'],True)
for c in ['base','pkg']:
 run(c,c+'-balance160','scripts/td/balance.ts',['--stage-seeds=80','--stage-sets=2'])
 run(c,c+'-g12x20','scripts/td/balance.ts',['--stage-seeds=12','--stage-sets=1','--seeds=20','--nights=4','--modes=balanced'])
 (W/c/'probe').mkdir()
 for name in ['pernight.ts','night1.ts']:shutil.copyfile(E/'probes'/name,W/c/'probe'/name)
 for m in ['balanced','relax','challenge']:run(c,c+'-pn-'+m,'probe/pernight.ts',['--from=24','--seeds=24','--modes='+m])
 for n in [40,160]:run(c,c+'-night1-'+str(n),'probe/night1.ts',['--seeds='+str(n)])
print('ALL_DONE',now(),flush=True)
