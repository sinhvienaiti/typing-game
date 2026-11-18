#!/usr/bin/env python3
"""Ticket 230: mutations of the 220 full-bay code, run in a throwaway copy.

Usage from the parent repo root: python3 -I docs/codex-queue/230/tools/mutate.py <out.json>
Each mutation replaces exactly one string in one file of
games/typing-survival/tmp/codex-230/codex-mut, runs the named Vitest files,
restores the file from the worktree and checks its SHA-256.
"""
import hashlib, json, os, re, shutil, subprocess, sys, time

ROOT = os.getcwd()
WT = os.path.join(ROOT, "games/.wt-ts-codex")
C = os.path.join(ROOT, "games/typing-survival/tmp/codex-230")
M = os.path.join(C, "codex-mut")
FB = ["tests/full-bay.test.ts"]
ALL = []  # whole suite

MUTATIONS = [
    ("M1", "src/sim/weapons.ts", "(chapter > 0 ? Math.max(0, Math.floor(FULL_BAY.extra)) : 0)", "Math.max(0, Math.floor(FULL_BAY.extra))", "R1 drops the chapter-only condition", FB),
    ("M2", "src/sim/weapons.ts", "if (w.stage.chapter <= 0 || FULL_BAY.spill < 1", "if (FULL_BAY.spill < 1", "R2 drops the chapter-only condition", FB),
    ("M3", "src/sim/weapons.ts", "return w.stage.chapter > 0 && FULL_BAY.boost > 0", "return FULL_BAY.boost > 0", "R3 drops the chapter-only condition", FB),
    ("M4", "src/content/guns.ts", "{ extra: 0, spill: 0, boost: 0 }", "{ extra: 0, spill: 0, boost: 0.3 }", "R3 knob on by default (boost 0.3)", ALL),
    ("M5", "src/content/guns.ts", "{ extra: 0, spill: 0, boost: 0 }", "{ extra: 0, spill: 1, boost: 0 }", "R2 knob on by default (spill 1)", ALL),
    ("M6", "src/sim/weapons.ts", "    G.fullBay.boosted[i + k] = G.fullBay.boosted[i + k + 1]!;\n", "", "nextMagazine no longer shifts the boost mark", FB),
    ("M7", "src/sim/weapons.ts", "  G.fullBay.boosted[i] = 0;\n", "", "loadMagazine no longer clears the boost mark", FB),
    ("M8", "src/sim/weapons.ts", "  const target = spillTarget(w, bay);\n  if (target >= 0 && loadMagazine(w, target, clean, fast)) return target;\n  if (!canBoost(w, bay)) return -1;",
     "  if (!canBoost(w, bay)) { const target = spillTarget(w, bay); return target >= 0 && loadMagazine(w, target, clean, fast) ? target : -1; }", "R3 before R2 (precedence swapped)", FB),
    ("M9", "src/sim/weapons.ts", "G.mags[b]! < G.mags[target]!) target = b;", "G.mags[b]! <= G.mags[target]!) target = b;", "R2 tie goes to the higher bay", FB),
    ("M10", "src/sim/pace.ts", " || spillTarget(w, b) >= 0 || canBoost(w, b)", " || spillTarget(w, b) >= 0", "flowSnapshot ignores R3", FB),
    ("M11", "src/sim/weapons.ts", "return canBoost(w, bay) ? need[gun]! * FULL_BAY.boost : -1;", "return -1;", "bot value ignores R3", FB),
    ("M12", "src/sim/words.ts", "if (receiver >= 0) w.events.push", "if (receiver === slot) w.events.push", "R2 emits no EV.load for the receiver", FB),
    ("M13", "src/sim/world.ts", "createGuns(header.kit, stage.chapter)", "createGuns(header.kit)", "world.ts line 119 reverted (R1 never reaches a world)", FB),
    ("M14", "src/sim/weapons.ts", "    fullBay: { boosted: new Uint8Array(slots) },", "    fullBay: { boosted: new Uint8Array(slots) },\n    boostedTop: new Uint8Array(slots),", "a top-level typed array next to the nested mark (enters hashWorld)", ALL),
    ("M15", "src/sim/weapons.ts", "if (b === bay || G.gun[b]! < 0 || G.mags[b]! >= G.cap[b]!) continue;", "if (b === bay || G.mags[b]! >= G.cap[b]!) continue;", "R2 may pick an empty socket", FB),
    ("M16", "src/sim/weapons.ts", "w.guns.damage[i] = w.guns.damage[i]! * (1 + FULL_BAY.boost);", "w.guns.damage[i] = w.guns.damage[i]! * (1 + 2 * FULL_BAY.boost);", "R3 multiplies by 1 + 2 x boost", FB),
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
