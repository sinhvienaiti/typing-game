"""Kiểm bằng chứng/tài liệu phiếu 188, không chạy build hay test game."""
from pathlib import Path
import hashlib, json, subprocess, re
ROOT = Path.cwd()
OUT = ROOT / 'docs/codex-queue/188'
data = json.loads((OUT / 'inventory.json').read_text())
counts = json.loads((OUT / 'counts.json').read_text())
checks = {}
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
checks['manifestAndLockHashesStable'] = all(digest(ROOT / p) == h for a in data for p, h in a['hashes'].items())
checks['installedVersionsMatchLock'] = all(r['version'] == r['installedVersion'] for a in data for r in a['records'])
checks['noMissingRuntimePackagesOrNotices'] = all(not r.get('missing') and r.get('license') and r.get('notices') for a in data for r in a['records'] if r['kind'] != 'devDependency')
checks['localNoticesUnchanged'] = all(digest(ROOT / n['path']) == n['sha256'] and (ROOT / n['path']).read_text() == n['text'] for a in data for r in a['records'] for n in r.get('notices', []))
checks['dependencyClosuresComplete'] = all(all(any(r['name'] == dep and r['version'] == version.split('(')[0] for r in a['records']) for dep, version in a['lock']['snapshots'].get(r['name']+'@'+r['version'], {}).items()) for a in data for r in a['records'] if r['kind'] != 'devDependency')
checks['manifestDependencyNamesMatchLock'] = all(set(a['manifest'].get('dependencies', {})) == set(a['lock']['dependencies']) for a in data)
checks['noUnresolvedImports'] = all(not a['runtime']['unresolved'] and not a['vendorGraph']['unresolved'] for a in data)
old = (OUT / 'third-party-before.md').read_bytes()
third = (ROOT / 'docs/games/THIRD_PARTY.md').read_bytes()
checks['allOldThirdPartyBytesPreserved'] = third.startswith(old)
added = third[len(old):].decode()
rows = [l for l in added.splitlines() if l.startswith('| ') and not l.startswith('| Tên |')]
checks['exactly21NewRowsWith8Columns'] = len(rows) == 21 and all(len(l.split('|')) == 10 for l in rows)
checks['runtimeRecordsAllInLedger'] = all(f'`{r["name"]}` | {r["version"]}' in added for a in data for r in a['records'] if r['kind'] != 'devDependency')
checks['creditsContainExactLocalLicenseText'] = True
for a in data:
    game = a['base'].split('/')[-1]
    text = (OUT / f'credits-{game}.md').read_text()
    for r in a['records']:
        if r['kind'] == 'devDependency': continue
        for n in r['notices']:
            checks['creditsContainExactLocalLicenseText'] &= n['text'].rstrip() in text
unique = {(r['name'], r['version']): r['license'] for a in data for r in a['records'] if r['kind'] != 'devDependency'}
checks['uniqueNpmCountAndLicenses'] = len(unique) == counts['uniqueNpmRuntimePackagesIncludingKit'] == 8 and {lic: list(unique.values()).count(lic) for lic in set(unique.values())} == counts['uniqueNpmLicenses']
checks['fivePolicyFlags'] = sorted(n+'@'+v for (n,v),lic in unique.items() if lic not in ['MIT','BSD-2-Clause','BSD-3-Clause','ISC','Apache-2.0','MPL-2.0','CC0-1.0','CC-BY-4.0']) == sorted(counts['policyFlags']) and len(counts['policyFlags']) == 5
checks['declaredCountsPerComponent'] = all(sum(r['kind'] in ['dependency','transitive'] for r in a['records']) == counts['declaredDependencies'][a['base'].split('/')[-1]]['total'] for a in data)
checks['currentGameRuntimeCounts'] = True
for a in data[:3]:
    bare = set(s.split('/')[0] if not s.startswith('@') else '/'.join(s.split('/')[:2]) for s in (i['spec'] for i in a['runtime']['external']))
    vendor_names = {Path(f).name for f in a['vendorGraph']['files'] if '/libs/' in f}
    expected = len(bare) + len(vendor_names) + 1  # Vite có mã chèn vào bản chơi.
    checks['currentGameRuntimeCounts'] &= expected == counts['currentGameRuntimeIncludingEmbedded'][a['base'].split('/')[-1]]['total']
embedded = json.loads((OUT / 'embedded-evidence.json').read_text())
checks['embeddedAndViteHashesStable'] = all(digest(ROOT / x['path']) == x['sha256'] for x in embedded['vendored']) and all(digest(ROOT / x['source']) == x['sourceSha256'] and digest(ROOT / x['licensePath']) == x['licenseSha256'] for x in embedded['buildEmbedded'])
checks['threeGameHelperEvidence'] = len(embedded['buildEmbedded']) == 3 and all(x['modulepreload'] and x['preloadHelper'] for x in embedded['distExisting'])

# Tạo các file kết quả trước khi lấy status để bản chụp có đủ tên.
for name in ['verification.json', 'scope.json', 'status-final.txt']:
    (OUT / name).touch(exist_ok=True)
own_paths = sorted([str(p.relative_to(ROOT)) for p in OUT.rglob('*') if p.is_file() and p.name != 'status-before.txt'] + ['docs/games/THIRD_PARTY.md', 'docs/codex-queue/188-report.md'])
checks['allTaskWritesAllowed'] = all(p in ['docs/games/THIRD_PARTY.md', 'docs/codex-queue/188-report.md'] or p.startswith('docs/codex-queue/188/') for p in own_paths)
status = subprocess.check_output(['git','status','--short','-uall'], cwd=ROOT, text=True)
(OUT / 'status-final.txt').write_text(status)
before = set((OUT / 'status-start.txt').read_text().splitlines())
after = set(status.splitlines())
new = sorted(after - before)
scope = {'command': 'git status --short -uall', 'initialStatusLines': len(before), 'finalStatusLines': len(after), 'taskWritePaths': own_paths, 'newStatusLinesInTaskScope': [l for l in new if l[3:] in own_paths], 'otherConcurrentStatusAdditions': [l for l in new if l[3:] not in own_paths], 'initialStatusLinesNoLongerPresent': sorted(before - after), 'allTaskWritesAllowed': checks['allTaskWritesAllowed'], 'note': 'Không gán thay đổi của làn khác cho phiếu này; status toàn repo có sẵn thay đổi ngoài phạm vi. status-before.txt có trước lượt làm, giữ nguyên.'}
(OUT / 'scope.json').write_text(json.dumps(scope,ensure_ascii=False,indent=2)+'\n')
result = {'date': '2026-10-29', 'checks': checks, 'passed': all(checks.values()), 'testOrBuildExecuted': False, 'newLedgerRows': len(rows), 'taskWritePathCount': len(own_paths), 'concurrentStatusAdditions': len(scope['otherConcurrentStatusAdditions'])}
(OUT / 'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
if not result['passed']: raise SystemExit(1)
