import json
from pathlib import Path
import subprocess

folder = Path('docs/codex-queue/214')
new_ids = {'dragon-hold', 'typing-defense', 'typing-survival'}
sources = [
    'portal/public/games.json', 'portal/src/main.ts', 'portal/src/styles.css',
    'portal/src/game-card.ts', 'portal/tests/game-card.test.mjs',
    'portal/tests/fixtures/legacy-games.json', 'scripts/game-dir.sh',
    'scripts/bootstrap.sh', 'docs/changelog/2026-10-30-portal-english-names.md',
    'docs/codex-queue/214-report.md',
]


def git(*args):
    return subprocess.check_output(['git', *args], text=True)


def matches(path, terms):
    return [f'{path}:{i}: {line}'
            for i, line in enumerate(Path(path).read_text().splitlines(), 1)
            if any(term in line for term in terms)]


baseline = json.loads(git('show', 'HEAD:portal/public/games.json'))['games']
current = json.loads(Path('portal/public/games.json').read_text())['games']
legacy = json.loads(Path('portal/tests/fixtures/legacy-games.json').read_text())
assert legacy == [g for g in baseline if g['id'] not in new_ids]
assert legacy == [g for g in current if g['id'] not in new_ids]
assert [g['id'] for g in baseline] == [g['id'] for g in current]
changed = {}
for old, new in zip(baseline, current):
    fields = sorted(k for k in old.keys() | new.keys() if old.get(k) != new.get(k))
    if fields:
        assert new['id'] in new_ids
        assert fields == ['art', 'description', 'icon', 'name']
        changed[new['id']] = fields
assert set(changed) == new_ids

old_names = ['Rồng Giữ Ải', 'Lời Gọi', 'Tuyến Cuối']
scripts = ['scripts/game-dir.sh', 'scripts/bootstrap.sh']
remaining = [line for path in scripts for line in matches(path, old_names)]
assert remaining == []
tu_tien = [line for path in scripts for line in matches(path, ['Tu Tiên'])]
for path in scripts:
    old_lines = [line for line in git('show', 'HEAD:' + path).splitlines() if 'Tu Tiên' in line]
    new_lines = [line for line in Path(path).read_text().splitlines() if 'Tu Tiên' in line]
    assert old_lines == new_lines

emoji = subprocess.check_output(['node', '--input-type=module', '-e', '''
import { readFileSync } from 'node:fs';
const lines = [];
for (const file of ['portal/public/games.json', 'portal/src/main.ts']) {
  readFileSync(file, 'utf8').split(/\\r?\\n/).forEach((line, i) => {
    if (/\\p{Extended_Pictographic}/u.test(line)) lines.push(`${file}:${i + 1}: ${line}`);
  });
}
console.log(lines.join('\\n'));
'''], text=True)
(folder / 'emoji-remaining.txt').write_text(emoji)
(folder / 'old-names-out-of-scope.txt').write_text('\n'.join(
    line for path in ['play.sh', 'dev.sh'] for line in matches(path, old_names)) + '\n')
(folder / 'games-json.diff').write_text(git('diff', '--', 'portal/public/games.json'))

all_paths = sorted(sources + [str(p) for p in folder.rglob('*') if p.is_file()]
                   + [str(folder / 'files.txt'), str(folder / 'verification.json'),
                      str(folder / 'status-after.txt'), str(folder / 'status-delta.json'),
                      str(folder / 'diff-check.txt')])
all_paths = sorted(set(all_paths))
(folder / 'files.txt').write_text('\n'.join(all_paths) + '\n')
diff = subprocess.run(['git', 'diff', '--check', '--', *sources, str(folder)],
                      capture_output=True, text=True)
assert diff.returncode == 0, diff.stdout + diff.stderr
untracked_checks = []
for path in all_paths:
    if not Path(path).exists():
        continue
    if git('status', '--short', '--', path).startswith('??'):
        result = subprocess.run(['git', 'diff', '--no-index', '--check', '/dev/null', path],
                                capture_output=True, text=True)
        assert not result.stdout and not result.stderr, path + result.stdout + result.stderr
        # No-index returns 1 for a new file even without whitespace diagnostics.
        assert result.returncode in (0, 1), (path, result.returncode)
        untracked_checks.append({'path': path, 'exit_code': result.returncode})
(folder / 'diff-check.txt').write_text(
    'git diff --check -- <scoped paths>: exit 0\n'
    + '\n'.join(f"git diff --no-index --check /dev/null {p['path']}: exit {p['exit_code']}; no whitespace diagnostics"
                for p in untracked_checks) + '\n')

status = git('status', '--short', '-uall')
(folder / 'status-after.txt').write_text(status)
allowed = set(sources)


def scoped(line):
    path = line[3:]
    return path in allowed or path.startswith(str(folder) + '/')


delta = {}
after_lines = set(status.splitlines())
for label in ['before', 'resume']:
    before_lines = set((folder / f'status-{label}.txt').read_text().splitlines())
    added, removed = sorted(after_lines - before_lines), sorted(before_lines - after_lines)
    delta[label] = {'added': added, 'removed': removed,
                    'outside_scope': [line for line in added + removed if not scoped(line)]}
(folder / 'status-delta.json').write_text(json.dumps(delta, ensure_ascii=False, indent=2) + '\n')
(folder / 'verification.json').write_text(json.dumps({
    'head': git('rev-parse', 'HEAD').strip(),
    'branch': git('branch', '--show-current').strip(),
    'legacy_entries_unchanged': len(legacy), 'changed_registry_fields': changed,
    'descriptions': {g['id']: {'text': g['description'], 'characters': len(g['description'])}
                     for g in current if g['id'] in new_ids},
    'old_names_in_scripts': len(remaining), 'tu_tien_labels_unchanged': tu_tien,
    'last_line_asset_directory_exists': Path('games/typing-survival/public/assets/typing-survival').is_dir(),
    'tracked_whitespace_exit_code': diff.returncode,
    'untracked_whitespace_checks': len(untracked_checks),
    'outside_scope_since_resume': delta['resume']['outside_scope'],
    'outside_scope_since_original_baseline': delta['before']['outside_scope'],
}, ensure_ascii=False, indent=2) + '\n')
print('Registry, script labels and whitespace checks passed; scope differences recorded.')
print('Outside original baseline:', delta['before']['outside_scope'])
print('Outside resume baseline:', delta['resume']['outside_scope'])
