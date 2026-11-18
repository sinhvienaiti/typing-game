from pathlib import Path
import subprocess, hashlib, json, difflib
ROOT=Path(__file__).resolve().parents[3]
W=ROOT/'games/.wt-ts-codex'
OUT=ROOT/'docs/codex-queue/210'
def git(*args):
    r=subprocess.run(['git','-C',str(W),*args],cwd=ROOT,capture_output=True)
    return r
new=['src/app/guide.ts','tests/guide.test.ts','scripts/visual/scenarios/survival-s1-first-run.mjs','docs/changelog/2026-10-30-first-run-guide.md']
changed=['src/app/journey.ts','src/view/screens-journey.ts','src/view/hud.ts','src/view/survival.css','scripts/visual/scenarios/survival-s1-loadout.mjs']
status=git('status','--short','-uall').stdout.decode()
(OUT/'status-final.txt').write_text(status)
before_status=(OUT/'status-before.txt').read_text()
paths=lambda s:{line[3:] for line in s.splitlines()}
allowed=paths(before_status)|set(new+changed+['src/app/main.ts'])
sha=lambda b:hashlib.sha256(b).hexdigest()
golden=sha((W/'tests/golden/s0-trace.json').read_bytes())
(OUT/'golden-after.txt').write_text(golden+'\n')
diffcheck=git('diff','--check'); (OUT/'diff-check.txt').write_bytes(diffcheck.stdout+diffcheck.stderr)
numstat=git('diff','--numstat','--','src/app/main.ts').stdout.decode(); (OUT/'main-numstat.txt').write_text(numstat)
main_before=(OUT/'before/main.ts').read_text(); main_after=(W/'src/app/main.ts').read_text()
main_diff=''.join(difflib.unified_diff(main_before.splitlines(True),main_after.splitlines(True),fromfile='a/src/app/main.ts',tofile='b/src/app/main.ts'))
(OUT/'main-210.diff').write_text(main_diff); (OUT/'main-all.diff').write_bytes(git('diff','--','src/app/main.ts').stdout)
patch=git('diff','--',*changed).stdout.decode()+main_diff
for name in new:
    if (W/name).exists(): patch+=''.join(difflib.unified_diff([], (W/name).read_text().splitlines(True),fromfile='/dev/null',tofile='b/'+name))
(OUT/'210-only.patch').write_text(patch)
intro=lambda s:s[s.index('for (const type of ["pointerdown", "keydown"])'):s.index('installAutoPause(window')]
insert_only={p:not any(l.startswith('-') and not l.startswith('---') for l in git('diff','--',p).stdout.decode().splitlines()) for p in ['src/view/screens-journey.ts','src/view/survival.css']}
chapter=subprocess.run(['diff',str(OUT/'chapter-before.txt'),str(OUT/'chapter-after.txt')],capture_output=True)
(OUT/'chapter-diff.txt').write_bytes(chapter.stdout+chapter.stderr)
checks={
 'chapterDiffExit':chapter.returncode,
 'chapterLineCounts':[len((OUT/name).read_text().splitlines()) for name in ['chapter-before.txt','chapter-after.txt']],
 'branch':git('branch','--show-current').stdout.decode().strip(),
 'outsideAllowed':sorted(paths(status)-allowed),
 'preexisting205207':sorted(paths(before_status)),
 'new210':new+changed+['src/app/main.ts'],
 'goldenSha256':golden,
 'goldenUnchanged':golden==(OUT/'golden-before.txt').read_text().strip(),
 'mainNumstat':numstat.strip(),
 'mainAddedRemovedTotal':sum(map(int,numstat.split()[:2])),
 'mainVmSliceUnchanged':intro(main_before)==intro(main_after),
 'introTestUnchanged':git('diff','--','tests/intro-key.test.ts').stdout==b'',
 'insertionOnly':insert_only,
 'diffCheckExit':diffcheck.returncode,
}
nodechecks={}
for filename in ['survival-s1-loadout.mjs','survival-s1-first-run.mjs']:
 r=subprocess.run(['node','--check',f'scripts/visual/scenarios/{filename}'],cwd=W,capture_output=True)
 nodechecks[filename]=r.returncode
 (OUT/(filename+'.check.log')).write_bytes(r.stdout+r.stderr+f'node --check exit {r.returncode}\n'.encode())
checks['nodeChecks']=nodechecks
(OUT/'verification.json').write_text(json.dumps(checks,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(checks,indent=2,ensure_ascii=False))
assert checks['branch']=='ts-codex' and not checks['outsideAllowed']
assert checks['goldenUnchanged'] and checks['mainVmSliceUnchanged'] and checks['introTestUnchanged']
assert checks['mainAddedRemovedTotal']<=8 and all(insert_only.values()) and diffcheck.returncode==0
assert all(v==0 for v in nodechecks.values())
assert chapter.returncode==0 and checks['chapterLineCounts']==[152,152]
