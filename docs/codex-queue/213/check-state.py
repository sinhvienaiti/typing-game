from pathlib import Path
import subprocess,json,os

root=Path(__file__).resolve().parents[3]
out=root/'docs/codex-queue/213'
env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'}
def git(*args):return subprocess.check_output(['git',*args],cwd=root,text=True,env=env)
# Create report before this snapshot so its untracked entry is included.
report=root/'docs/codex-queue/213-report.md'
if not report.exists():report.write_text('# Phiếu 213\n\nĐang lập báo cáo kiểm.\n')
(out/'state-check.json').touch(exist_ok=True)
(out/'status-after.txt').touch(exist_ok=True)
(out/'game-after.txt').write_text(git('-C','games/dragon-hold','status','--short'))
(out/'status-after.txt').write_text(git('status','--short','-uall'))
before=set((out/'status-before.txt').read_text().splitlines())
after=set((out/'status-after.txt').read_text().splitlines())
def allowed(line):
    p=line[3:]
    return p in ['docs/games/audio/firefly/dragon-hold.md','docs/games/audio/firefly/dragon-hold.json','docs/codex-queue/213-report.md'] or p.startswith('docs/codex-queue/213/')
added=sorted(after-before);removed=sorted(before-after)
state=dict(addedStatusLines=added,removedStatusLines=removed,outsideAdded=[x for x in added if not allowed(x)],outsideRemoved=[x for x in removed if not allowed(x)],gameStatusIdentical=(out/'game-before.txt').read_bytes()==(out/'game-after.txt').read_bytes(),gameBranchAfter=git('-C','games/dragon-hold','branch','--show-current').strip())
state['parentOnlyAllowedChanges']=not state['outsideAdded'] and not state['outsideRemoved']
(out/'state-check.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in state.items() if k not in ['addedStatusLines','removedStatusLines']},ensure_ascii=False,indent=2))
