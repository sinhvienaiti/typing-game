"""Kiểm hiện vật, phạm vi Git và số đo; chạy sau khi chép đủ raw."""
from pathlib import Path
import json, hashlib, subprocess, re, datetime, sys
root=Path(__file__).resolve().parents[4]
r=root/'docs/codex-queue/220'; wt=root/'games/.wt-ts-codex'; tmp=wt/'tmp/codex-220'
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
cmd=lambda args,cwd=root: subprocess.run(args,cwd=cwd,text=True,capture_output=True)
specs=json.loads((r/'variants.json').read_text()); summary=json.loads((r/'summary.json').read_text())
variants=[k for k in specs if re.fullmatch(r'f[1-6]',k)]
files=[]
for p in sorted((tmp/'runs').iterdir()):
 q=r/'runs'/p.name
 files.append({'name':p.name,'sha256':sha(p),'copySha256':sha(q),'match':sha(p)==sha(q)})
waves=[json.loads(p.read_text()) for p in sorted((r/'evidence').glob('wave-*.json'))]
jobs=[j for w in waves for j in w['jobs']]
raw=[]
for p in sorted((r/'runs').glob('*.json')):
 cells=json.loads(p.read_text()); stages=sorted({c['stage'] for c in cells}); stem=p.stem
 md=p.with_suffix('.md').read_text(); err=p.with_suffix('.err').read_text()
 raw.append({'id':stem,'stages':stages,'cells':len(cells),'cellCounts':{s:sum(c['stage']==s for c in cells) for s in stages},'allRuns100':all(c['summary']['runs']==100 for c in cells),'g3cPairs':sum(1 for line in md.splitlines() if line.startswith('| ') and len(line.split('|'))==7 and re.match(r'^\| [^|]+ \| [\d,]+ ?%',line)),'niceDenied': 'setpriority: Operation not permitted' in err,'unexpectedStderr':[x for x in err.splitlines() if x and not x.startswith('--set: ') and x!='nice: setpriority: Operation not permitted'],'seconds':int(re.search(r'cả lệnh (\d+) s',md)[1])})
checks={}
checks['beforeCheckExit']=int((r/'logs/check-before.exit').read_text());checks['afterCheckExit']=int((r/'logs/check-after.exit').read_text())
checks['testsBefore']='296 passed (296)' in (r/'logs/check-before.txt').read_text();checks['testsAfter']='317 passed (317)' in (r/'logs/check-after.txt').read_text()
checks['goldenBefore']=(r/'evidence/golden-before.txt').read_text().split()[0];checks['goldenAfter']=(r/'evidence/golden-after.txt').read_text().split()[0]
checks['chapterLinesBefore']=len((r/'chapter-before.txt').read_text().splitlines());checks['chapterLinesAfter']=len((r/'chapter-after.txt').read_text().splitlines());checks['chapterMatch']=(r/'chapter-before.txt').read_bytes()==(r/'chapter-after.txt').read_bytes()
checks['variantCount']=len(variants);checks['singleReports']=sum(len(x['stages'])==1 for x in raw);checks['fourStageReports']=sum(len(x['stages'])==4 for x in raw);checks['rawFilesMatch']=all(f['match'] for f in files);checks['allExit0']=all(j['exit']==0 for j in jobs)
checks['waveStartLimits']=all(w['peak']<= (2 if w['load']>10 else 4) for w in waves)
checks['loadRoseAbove10With4Reports']=True
checks['liveLimitDuringRiseGuaranteed']=False
checks['summaryOverridesValid']=all(x['checks']['overridesValid'] for x in summary['runs'])
checks['worktreeHead']=cmd(['git','rev-parse','HEAD'],wt).stdout.strip()
allowed={'src/content/guns.ts','src/sim/weapons.ts','src/sim/words.ts','src/sim/pace.ts','src/sim/world.ts','tests/survival/typist-bot.ts','tests/full-bay.test.ts','docs/changelog/2026-10-30-full-bay-knobs.md'}
status=cmd(['git','status','--short','-uall'],wt).stdout;(r/'evidence/worktree-status-after.txt').write_text(status)
checks['onlyAllowedWorktreePaths']=all(line[3:] in allowed for line in status.splitlines())
for name,args in {'protectedDiff':['diff','--quiet','--','src/view','src/app','src/kit','src/audio','tests/golden','scripts'],'diffCheck':['diff','--check'],'contentDiff':['diff','--name-only','--','src/content'],'worldNumstat':['diff','--numstat','--','src/sim/world.ts']}.items():
 x=cmd(['git',*args],wt);checks[name]={'exit':x.returncode,'stdout':x.stdout,'stderr':x.stderr}
(r/'evidence/parent-status-after.txt').write_text(cmd(['git','status','--short','-uall']).stdout)
before=set((r/'evidence/parent-status-before.txt').read_text().splitlines());after=set((r/'evidence/parent-status-after.txt').read_text().splitlines())
parent={'added':sorted(after-before),'removed':sorted(before-after)};(r/'evidence/parent-status-changes.json').write_text(json.dumps(parent,ensure_ascii=False,indent=2)+'\n')
checks['tmpdirRemoved']=not (tmp/'tmpdir').exists();checks['tmpRunsRemain']=(tmp/'runs').is_dir()
seconds=sum(x['seconds'] for x in raw)
result={'timeUtc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'raw':raw,'copies':files,'waves':waves,'machineSeconds':seconds,'machineHours':seconds/3600,'processWallSeconds':sum(j['wallSeconds'] for j in jobs),'measurementSpanSeconds':(datetime.datetime.fromisoformat(max(w['end'] for w in waves).replace('Z','+00:00'))-datetime.datetime.fromisoformat(min(w['start'] for w in waves).replace('Z','+00:00'))).total_seconds(),'parentChanges':parent,'taskStartUtc':datetime.datetime.fromtimestamp((r/'start.txt').stat().st_birthtime,datetime.timezone.utc).isoformat(),'taskSpanSeconds':datetime.datetime.now().timestamp()-(r/'start.txt').stat().st_birthtime}
(r/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':checks,'rawReports':len(raw),'rawFiles':len(files),'machineSeconds':seconds,'measurementSpanSeconds':result['measurementSpanSeconds']},ensure_ascii=False,indent=2))

errors=[]
for key in ['testsBefore','testsAfter','chapterMatch','rawFilesMatch','allExit0','waveStartLimits','summaryOverridesValid','onlyAllowedWorktreePaths','tmpRunsRemain']:
 if not checks[key]:errors.append(key)
if checks['beforeCheckExit'] or checks['afterCheckExit']:errors.append('pnpm check exit')
if checks['goldenBefore']!=checks['goldenAfter'] or checks['goldenBefore']!='42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea':errors.append('golden')
if checks['chapterLinesBefore']!=152 or checks['chapterLinesAfter']!=152:errors.append('chapter count')
if checks['singleReports']!=2+2*len(variants) or checks['fourStageReports']!=6 or len(variants)>6:errors.append('report budget')
if checks['worktreeHead']!='ba6d70e9d6978eb4b430d119c409f3d47f9a364e':errors.append('HEAD')
if checks['protectedDiff']['exit'] or checks['diffCheck']['exit']:errors.append('protected paths/diff check')
if checks['contentDiff']['stdout']!='src/content/guns.ts\n' or checks['worldNumstat']['stdout']!='1\t1\tsrc/sim/world.ts\n':errors.append('restricted content/world')
if not checks['tmpdirRemoved'] and '--before-cleanup' not in sys.argv:errors.append('tmpdir still exists')
for x in raw:
 if x['cells']!=36*len(x['stages']) or not all(n==36 for n in x['cellCounts'].values()) or not x['allRuns100'] or x['g3cPairs']!=10*len(x['stages']) or x['unexpectedStderr']:errors.append(x['id'])
for name in ['v6-repro.json','four-stage-repro.json']:
 comparisons=json.loads((r/'evidence'/name).read_text())
 if any(x['changedCells'] or x['diffs'] or x['actualCells']!=36 for x in comparisons):errors.append(name)
result['artifactErrors']=errors
result['resourceCaveat']='Tải giữa đợt C tăng >10; sandbox từ chối SIGSTOP. Chỉ xác nhận trần theo tải đầu đợt, xem load-rise.json.'
(r/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if errors: print('ERRORS:',errors)
sys.exit(1 if errors else 0)
