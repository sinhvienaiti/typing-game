#!/usr/bin/env python3
"""Ticket 230: mutations of the 220 full-bay code, run in a throwaway copy.

Usage from the parent repo root: python3 -I docs/codex-queue/230/tools/mutate.py <out.json>
Each mutation replaces exactly one string in one file of
games/typing-survival/tmp/codex-230/art-mut, runs the named Vitest files,
restores the file from the worktree and checks its SHA-256.
"""
import hashlib, json, os, re, shutil, subprocess, sys, time

ROOT = os.getcwd()
WT = os.path.join(ROOT, "games/.wt-ts-art")
C = os.path.join(ROOT, "games/typing-survival/tmp/codex-230")
M = os.path.join(C, "art-mut")
FB = ["tests/ui-art.test.ts", "tests/english-ui.test.ts", "tests/small-labels.test.ts", "tests/theme.test.ts"]
ALL = []  # whole suite


MUTATIONS = [
    ("A1", "src/view/hud.ts", '      appendArt(root, artAttrs(gunRole(spec.key), "bay"));\n', "", "bay icon (LL-39) not attached", ALL),
    ("A2", "src/view/hud.ts", '          appendArt(this.fresh, artAttrs(foeRole(kind), "fresh"));\n', "", "new-foe card portrait (LL-35) not attached", ALL),
    ("A3", "src/view/hud.ts", "    watchArt(root);\n", "", "error listener never installed", ALL),
    ("A4", "src/app/main.ts", 'art: "stage-" + next.id, ', "", "results Next button loses its stage image (LL-53)", ALL),
    ("A5", "src/app/main.ts", 'stage: level.id === "s0" ? undefined : level.id, ', "stage: level.id, ", "trial intro asks for stage-s0 art", ALL),
    ("A6", "src/view/ui-art.ts", "at(box * 1.5)", "at(box)", "1x picks the box width, not box x 1.5", FB),
    ("A7", "src/view/survival.css", ".sv-art-briefing:not([hidden]) { display: block;", ".sv-art-briefing { display: block;", "briefing band display rule beats [hidden] (no :not)", ALL),
    ("A8", "src/view/ui-art.ts", "  img.hidden = true;\n", "", "failed image stays visible", FB),
]


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def vitest(files):
    env = dict(os.environ, TMPDIR=os.path.join(C, "tmpdir"), pnpm_config_verify_deps_before_run="false")
    start = time.time()
    r = subprocess.run(["node_modules/.bin/vitest", "run", *files], cwd=M, capture_output=True, text=True, env=env)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    tests = re.search(r"Tests\s+(.*)\((\d+)\)", out)
    failed = re.search(r"(\d+) failed", tests.group(1)) if tests else None
    passed = re.search(r"(\d+) passed", tests.group(1)) if tests else None
    names = sorted(set(re.findall(r"(?:FAIL|×)\s+(tests/[\w./-]+\.test\.ts)", out)))
    return {"exit": r.returncode, "failed": int(failed.group(1)) if failed else 0, "passed": int(passed.group(1)) if passed else 0,
            "total": int(tests.group(2)) if tests else None, "failingFiles": names, "seconds": round(time.time() - start, 2)}


results = []
for mid, rel, old, new, what, files in MUTATIONS:
    path = os.path.join(M, rel)
    text = open(path, encoding="utf8").read()
    count = text.count(old)
    if count != 1:
        results.append({"id": mid, "file": rel, "what": what, "error": f"pattern found {count} times"})
        continue
    open(path, "w", encoding="utf8").write(text.replace(old, new))
    mutated = vitest(files)
    shutil.copyfile(os.path.join(WT, rel), path)
    restored_sha = sha(path) == sha(os.path.join(WT, rel))
    restored = vitest(files)
    results.append({"id": mid, "file": rel, "what": what, "tests": files or "all", "mutated": mutated, "restored": restored, "restoredSha256Match": restored_sha})
    print(mid, what, "mutated", mutated["failed"], "/", mutated["total"], "restored", restored["failed"], "/", restored["total"], restored_sha, flush=True)

json.dump(results, open(sys.argv[1], "w"), indent=1)
