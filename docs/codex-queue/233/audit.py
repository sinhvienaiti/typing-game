#!/usr/bin/env python3
"""Đối chiếu độc lập mốc sửa và phạm vi; mọi file trung gian ở bản chép."""
from pathlib import Path
import hashlib, json, re, shutil, subprocess
from run import ROOT as R, OUT as O, PARENT_COPY as P, TD_COPY as C, run

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name, obj): (O / name).write_text(json.dumps(obj, indent=2) + '\n')
queue = R / 'docs/codex-queue'
before = json.loads((queue / '228/hashes-before.json').read_text())
after = json.loads((queue / '228/hashes-after.json').read_text())
changed = sorted(p for p in before if after.get(p) != before[p])
assert len(changed) == 9
assert all(sha(R / p) == h for p, h in after.items())
patch = (queue / '228/task.diff').read_text()
patch_paths = re.findall(r'^\+\+\+ b/(.+)$', patch, re.M)
assert sorted(patch_paths) == changed
work = P / 'scope228'
work.mkdir(exist_ok=True)
for path in changed:
    dst = work / path
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(R / path, dst)
row = run('reverse-228-patch', ['/usr/bin/patch', '-R', '-p1', '-d', str(work), '-i', str(queue / '228/task.diff')], P)
assert row['exit'] == 0
bsd_matches = sum(sha(work / path) == before[path] for path in changed)
# BSD patch can move a zero-context deletion past an adjacent insertion.
# Apply the recorded new-file coordinates exactly, then verify the old hashes.
for section in patch.split('--- a/')[1:]:
    path = section.splitlines()[0]
    source = (R / path).read_text().splitlines(keepends=True)
    hunks = []
    current = None
    for line in section.splitlines(keepends=True)[2:]:
        match = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
        if match:
            a,ac,b,bc=match.groups()
            current={'start':int(b) - (1 if (int(bc) if bc is not None else 1) else 0),'old':[],'new':[]}
            hunks.append(current)
        elif current is not None:
            if line.startswith(('-', ' ')): current['old'].append(line[1:])
            if line.startswith(('+', ' ')): current['new'].append(line[1:])
    for hunk in reversed(hunks):
        at = hunk['start']; end = at + len(hunk['new'])
        assert source[at:end] == hunk['new'], (path,at)
        source[at:end] = hunk['old']
    (work / path).write_text(''.join(source))
assert all(sha(work / path) == before[path] for path in changed)
allowed_parent = lambda p: (p.startswith(('portal/src/', 'portal/tests/')) or p == 'portal/public/games.json'
    or p in ['infra/nginx/typing-game.local.play.conf','infra/nginx/typing-game.local.dev.conf',
             'scripts/validate-play-mode.mjs','scripts/validate-play-mode.test.mjs']
    or re.match(r'^shared/learning/(core|query|message-contract|profile-backup)\.(mjs|d\.mts|test\.mjs)$',p)
    or p == 'shared/learning/lookup.test.mjs')
assert all(allowed_parent(p) for p in changed)
td_before = json.loads((queue / '229/before.json').read_text())['paths']
td_after = json.loads((queue / '229/after.json').read_text())['paths']
td_changed = sorted(p for p in td_before if td_after.get(p) != td_before[p])
td_added = sorted(set(td_after) - set(td_before))
td_allowed = ['vite.config.ts','scripts/deploy/prune.mjs','tests/deploy-prune.test.ts','tests/portal.test.ts',
              'tests/portal-id.test.ts','docs/changelog/2026-10-30-fix-224-findings.md']
assert set(td_changed + td_added) == set(td_allowed)
assert all(sha(R / 'games/.wt-td-codex' / p) == h for p,h in td_after.items())
assert not (set(td_before) - set(td_after))
scope = {'228': {'baseline_files':len(before),'changed':changed,'unchanged':len(before)-len(changed),
    'task_patch_paths':patch_paths,'bsd_reverse_matches':bsd_matches,
    'coordinate_reverse_matches_before_hashes':9,'current_matches_after':len(after),
    'all_allowed':True,'changelog':'docs/changelog/2026-10-30-fix-227.md'},
    '229': {'baseline_files':len(td_before),'after_files':len(td_after),'changed':td_changed,'added':td_added,
            'current_matches_after':len(td_after),'all_allowed':True}}
for ticket in ['228','229']:
    a=set((queue / ticket / 'status-before.txt').read_text().splitlines())
    b=set((queue / ticket / 'status-after.txt').read_text().splitlines())
    scope[ticket]['historical_status_added']=sorted(b-a)
    scope[ticket]['historical_status_removed']=sorted(a-b)
save('scope-review.json',scope)
f7=R/'docs/codex-queue/216/tests-before.txt'
lines=[i for i,line in enumerate(f7.read_text().splitlines(),1) if re.search(r'[ \t]+$',line)]
assert len(lines)==15
save('f7.json',{'file':str(f7.relative_to(R)),'lines':lines,'count':len(lines),'sha256':sha(f7)})
run('f7-read-only',['git','--no-optional-locks','diff','--no-index','--check','/dev/null',str(f7)],R)
run('validate-play-mode',['node','scripts/validate-play-mode.mjs'],P)
old=json.loads((queue/'228/bundle-after-files.json').read_text())
new=json.loads((O/'portal-dist.json').read_text())['entries']
oldby={f['path']:f for f in old};newby={f['path']:f for f in new}
save('bundle-comparison.json',{'228':{'files':len(old),'bytes':sum(e['bytes'] for e in old),
    'js_bytes':sum(e['bytes'] for e in old if e['path'].endswith('.js'))},
    '233':{'files':len(new),'bytes':sum(e['bytes'] for e in new),
    'js_bytes':sum(e['bytes'] for e in new if e['path'].endswith('.js'))},
    'unchanged_entries':sum(oldby[p]==newby[p] for p in oldby.keys()&newby.keys()),
    'added_paths':sorted(set(newby)-set(oldby)),'removed_paths':sorted(set(oldby)-set(newby)),
    'changed_common_paths':[p for p in sorted(oldby.keys()&newby.keys()) if oldby[p]!=newby[p]]})
for name in ['production','local']:
    now=json.loads((O/('dist-'+name+'.json')).read_text())
    old=json.loads((queue/'229'/('dist-'+name+'.json')).read_text())
    assert now['entries']==old['entries']
save('pack-comparison.json',{'production':{'matching_entries':53,'same_bytes_and_hashes':True},
                             'local':{'matching_entries':53,'same_bytes_and_hashes':True}})
print(json.dumps({'scope_228':len(changed),'scope_229':len(td_changed+td_added),'F7':lines,
                  'pack_matches':'53/53 production + 53/53 local'},ensure_ascii=False))
