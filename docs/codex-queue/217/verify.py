"""Ghi kiểm phạm vi và so sánh số test; chỉ ghi hồ sơ của phiếu 217."""
import json
import re
import subprocess
from pathlib import Path

repo = Path(__file__).resolve().parents[3]
folder = repo / 'docs/codex-queue/217'
for name in ('scope.json', 'test-summary.json', 'status-after.txt'):
    path = folder / name
    if not path.exists():
        path.write_text('{}\n' if path.suffix == '.json' else '', encoding='utf-8')


def write(name, data):
    (folder / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def counts(name):
    text = (folder / name).read_text()
    result = {'passed': 0, 'failed': 0, 'errors': 0, 'skipped': 0}
    for n, key in re.findall(r'(\d+) (passed|failed|errors?|skipped)\b', text.splitlines()[-1]):
        result['errors' if key.startswith('error') else key] = int(n)
    result['failures'] = [line.split(' - ')[0] for line in text.splitlines() if line.startswith(('FAILED ', 'ERROR '))]
    return result

before, after = counts('tests-before.txt'), counts('tests-after.txt')
new = counts('tests-new.txt')
summary = {'before': before, 'after': after, 'new': new,
           'sameFailingTests': before['failures'] == after['failures'],
           'passCountDelta': after['passed'] - before['passed'],
           'existingContextKeys': counts('tests-existing-context-keys.txt'),
           'licenceDefaultUnchanged': (folder / 'licence-before.txt').read_bytes() == (folder / 'licence-after.txt').read_bytes()}
assert summary['sameFailingTests'] and summary['passCountDelta'] == new['passed'] == 20
assert summary['licenceDefaultUnchanged']
write('test-summary.json', summary)
report = repo / 'docs/codex-queue/217-report.md'
text = report.read_text().replace('| Audio Lab sau sửa, theo `pytest.ini` | Đang ghi kết quả cuối | — | — | — |',
                                  '| Audio Lab sau sửa, theo `pytest.ini` | 539 | 6 | 10 | 6 |')
fixed = ['tools/audio-lab/build/policy.py', 'tools/audio-lab/build/licence_check.py',
         'tools/audio-lab/build/tests/test_build_firefly_licence.py', 'tools/audio-lab/common/launch.py',
         'tools/audio-lab/pytest.ini', 'docs/changelog/2026-10-30-audio-lab-firefly-ingest.md',
         'docs/codex-queue/217-report.md']
owned = sorted(set(fixed + [str(p.relative_to(repo)) for base in (folder, repo / 'tools/audio-lab/firefly')
                           for p in base.rglob('*') if p.is_file() and p.suffix in ('.py', '.txt', '.json', '.md')]))
assert not [p for base in (folder, repo / 'tools/audio-lab/firefly') for p in base.rglob('*')
            if p.is_file() and p.suffix.lower() in ('.wav', '.ogg', '.mp3', '.png', '.jpg')]
text = text.split('<!-- PATHS -->')[0] + '<!-- PATHS -->\n\n' + '\n'.join('- `' + p + '`' for p in owned) + '\n'
report.write_text(text, encoding='utf-8')
status = subprocess.check_output(['git', 'status', '--short', '-uall'], cwd=repo, text=True)
(folder / 'status-after.txt').write_text(status, encoding='utf-8')
old = set((folder / 'status-before.txt').read_text().splitlines())
current = set(status.splitlines())
added, removed = sorted(current - old), sorted(old - current)
concurrent = [line for line in added if line[3:] not in owned]
write('scope.json', {'branch': subprocess.check_output(['git', 'branch', '--show-current'], cwd=repo, text=True).strip(),
                    'ownedPaths': owned, 'ownedPathCount': len(owned),
                    'concurrentStatusAdded': concurrent, 'statusRemoved': removed,
                    'note': 'Chỉ ghi các đường ownedPaths; giữ nguyên việc đồng thời của làn khác.',
                    'temporaryData': 'tmp/firefly-ingest/** (Git bỏ qua)',
                    'noAudioOrImagesInTicketPaths': True})
print(json.dumps({'ownedPaths': len(owned), 'concurrentStatusLines': len(concurrent),
                  'tests': {k: v for k,v in after.items() if k != 'failures'},
                  'newTests': new['passed'], 'sameFailures': summary['sameFailingTests']}, ensure_ascii=False))
