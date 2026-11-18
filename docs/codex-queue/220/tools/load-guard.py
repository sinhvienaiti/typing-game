"""Giảm số báo cáo đang thực thi khi tải chung tăng giữa đợt, không mở lại báo cáo."""
import os, signal, subprocess, json, time, datetime
from pathlib import Path
r=Path(__file__).resolve().parents[1]; wave=r/'evidence/wave-C.json'; output=r/'evidence/load-guard.json'
paused=set(); events=[]
def record(kind,pid,uptime):
 events.append({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'action':kind,'pid':pid,'uptime':uptime})
 output.write_text(json.dumps({'events':events,'paused':sorted(paused)},indent=2)+'\n')
try:
 while True:
  data=json.loads(wave.read_text()); jobs=[j for j in data['jobs'] if 'end' not in j and 'pid' in j]
  uptime=subprocess.check_output(['uptime'],text=True).strip(); load=float(uptime.split('load averages:')[1].split()[0]); limit=2 if load>10 else 4
  live=[j['pid'] for j in jobs]; active=[pid for pid in live if pid not in paused]
  while len(active)>limit:
   pid=active.pop()
   os.kill(pid,signal.SIGSTOP);paused.add(pid);record('SIGSTOP',pid,uptime)
  for pid in list(paused):
   if pid not in live: paused.remove(pid)
   elif len(active)<limit:
    os.kill(pid,signal.SIGCONT);paused.remove(pid);active.append(pid);record('SIGCONT',pid,uptime)
  if data.get('end'):break
  time.sleep(2)
finally:
 for pid in list(paused):
  try:os.kill(pid,signal.SIGCONT)
  except ProcessLookupError:pass
  paused.remove(pid);record('SIGCONT-finally',pid,'')
