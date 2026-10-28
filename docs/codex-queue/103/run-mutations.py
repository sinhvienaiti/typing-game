from pathlib import Path
import hashlib
import json
import subprocess

REPO = Path(__file__).resolve().parents[3]
WORKTREE = REPO / "games/.wt-td-codex"
OUT = Path(__file__).resolve().parent
CASES = [
    ("a6-mode", "src/ui/sheets.ts", 'w.mode === "learn" || w.knowledge > 0', 'w.knowledge > 0'),
    ("a6-unconditional", "src/ui/sheets.ts", '(w.mode === "learn" || w.knowledge > 0 ? row("Knowledge", w.knowledge) : "")', 'row("Knowledge", w.knowledge)'),
    ("a8-omit-mean", "src/view/words/cards.ts", '      (lanes.get(c) ?? lanes.set(c, []).get(c)!).push(card);\n    }\n    this.layout', '    }\n    this.layout'),
    ("a8-rise-cap", "src/view/words/lanes.ts", 'cards.map((_, k) => k * gap)', 'cards.map((_, k) => Math.min(COLUMN.max, k * gap))'),
]
results = []
for name, relative, old, new in CASES:
    path = WORKTREE / relative
    original = path.read_bytes()
    source = original.decode()
    assert source.count(old) == 1, (name, source.count(old))
    try:
        path.write_text(source.replace(old, new))
        run = subprocess.run(["pnpm", "vitest", "run", "tests/td-sheet-cards.test.ts"], cwd=WORKTREE, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (OUT / ("mutation-" + name + ".txt")).write_text(run.stdout)
    finally:
        path.write_bytes(original)
    result = {"name": name, "file": relative, "exitCode": run.returncode, "restored": path.read_bytes() == original, "sha256Restored": hashlib.sha256(original).hexdigest()}
    results.append(result)
    assert run.returncode == 1 and result["restored"], result
(OUT / "mutations.json").write_text(json.dumps(results, indent=2) + "\n")
print(json.dumps(results, indent=2))
