"""Đối chiếu TF2 và status, chỉ đọc Git; chứng cứ chỉ ghi trong thư mục phiếu 219."""
from pathlib import Path
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[3]
folder = root / 'docs/codex-queue/219'
protected = [
    'shared/game-kit/feedback/typing-fx/css.ts',
    'shared/game-kit/feedback/typing-fx/draw.ts',
    'shared/game-kit/ui/quick-settings/css.ts',
]
code = [
    'shared/game-kit/feedback/typing-fx/audio.ts',
    'shared/game-kit/feedback/typing-fx/index.ts',
    'shared/game-kit/feedback/typing-fx/audio-progressive.test.ts',
    'shared/game-kit/ui/quick-settings/keyboard-choices.ts',
    'shared/game-kit/ui/quick-settings/keyboard-sound.test.ts',
    'shared/game-kit/ui/quick-settings/keyboard-families.test.ts',
    'tools/typing-feedback-lab/README.md',
    'tools/typing-feedback-lab/vite.config.mjs',
    'tools/typing-feedback-lab/src/main.ts',
    'tools/typing-feedback-lab/src/profiles.ts',
]

def git(*args):
    return subprocess.check_output(['git', *args], cwd=root)

def own(line):
    path = line[3:]
    return path in code or path == 'docs/codex-queue/219-report.md' or path.startswith('docs/codex-queue/219/')

(folder / 'tf2-after.txt').write_bytes(git('diff', '--stat', '--', *protected))
after_hashes = {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in protected}
(folder / 'tf2-hashes-after.json').write_text(json.dumps(after_hashes, indent=2) + '\n')
(folder / 'implementation.diff').write_bytes(git('diff', '--', *code))
check = subprocess.run(['git', 'diff', '--check', '--', *code, 'docs/codex-queue/219-report.md'], cwd=root, capture_output=True)
(folder / 'diff-check.txt').write_bytes(check.stdout + check.stderr)
# Tạo file kết quả trước status để status sau cũng chứa chính chứng cứ này.
(folder / 'scope.json').touch()
(folder / 'status-after.txt').touch()
after = git('status', '--short', '-uall')
(folder / 'status-after.txt').write_bytes(after)
before_lines = set((folder / 'status-before.txt').read_text().splitlines())
after_lines = set(after.decode().splitlines())
new_lines = after_lines - before_lines
result = {
    'tf2StatIdentical': (folder / 'tf2-before.txt').read_bytes() == (folder / 'tf2-after.txt').read_bytes(),
    'tf2HashesIdentical': json.loads((folder / 'tf2-hashes-before.json').read_text()) == after_hashes,
    'diffCheckExitCode': check.returncode,
    'taskCodeFiles': code,
    'taskStatusRows': sorted(line for line in after_lines if own(line)),
    'preExistingStatusRowCount': len(before_lines),
    'wholeRepoContainsOnlyTask': all(own(line) for line in after_lines),
    'newRowsOutsideTaskSinceSnapshot': sorted(line for line in new_lines if not own(line)),
    'rowsRemovedOutsideTaskSinceSnapshot': sorted(line for line in before_lines - after_lines if not own(line)),
    'note': 'Status trước đã có thay đổi của tác vụ khác. Các dòng ngoài phiếu được giữ nguyên, không quy cho phiếu 219.',
}
(folder / 'scope.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in ['taskCodeFiles', 'taskStatusRows']}, ensure_ascii=False, indent=2))
assert result['tf2StatIdentical'] and result['tf2HashesIdentical']
assert check.returncode == 0
