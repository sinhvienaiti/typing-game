"""Record the final, read-only scope and immutable-file checks."""
import difflib
import json
from pathlib import Path
import subprocess
from run import GAME, OUT, ROOT, git, save, snapshot

snapshot("after.json")
before = json.loads((OUT / "before.json").read_text())
after = json.loads((OUT / "after.json").read_text())
owned = ["README.md", "vite.config.ts", "src/app/portal.ts", "src/app/learning.ts",
         "tests/portal.test.ts", "tests/portal-build.test.ts", "docs/changelog/2026-10-30-portal-origin.md"]
initial_paths = {line[3:] for line in before["status"]}
final_paths = {line[3:] for line in after["status"]}
diff = subprocess.run(["git", "-C", str(GAME), "diff", "--check"], cwd=ROOT, capture_output=True, text=True)
(OUT / "diff-check.txt").write_text(diff.stdout + diff.stderr)
(OUT / "status-final.txt").write_text("\n".join(after["status"]) + "\n")
production = json.loads((OUT / "production-bundle.json").read_text())
final = json.loads((OUT / "dist-final.json").read_text())
kit_unchanged = before["protected"] == after["protected"]
models_section_unchanged = (OUT / "before/README.md").read_text().split("## Models\n", 1)[1] == (GAME / "README.md").read_text().split("## Models\n", 1)[1]
vite_before = (OUT / "before/vite.config.ts").read_text()
vite_after = (GAME / "vite.config.ts").read_text()
server_before = vite_before.split("server: {", 1)[1].split("build: {", 1)[0]
server_after = vite_after.split("server: {", 1)[1].split("build: {", 1)[0]
server_unchanged = "".join(server_before.split()) == "".join(server_after.split())
parent_status = subprocess.check_output(["git", "status", "--short", "-uall"], cwd=ROOT, text=True)
(OUT / "parent-status-after.txt").write_text(parent_status)
def external_lines(text):
    return {line for line in text.splitlines() if not line[3:].startswith("docs/codex-queue/207")}
parent_before = external_lines((OUT / "parent-status-before.txt").read_text())
parent_after = external_lines(parent_status)
result = {
    "headBefore": before["head"], "headAfter": after["head"], "branch": after["branch"],
    "initial205Paths": sorted(initial_paths), "owned207Paths": owned,
    "unexpectedPaths": sorted(final_paths - initial_paths - set(owned)),
    "missing205Paths": sorted(initial_paths - final_paths),
    "protectedFilesUnchanged": kit_unchanged,
    "protectedCounts": {folder: sum(k.startswith(folder + "/") for k in before["protected"])
                        for folder in ["src/kit", "src/sim", "src/content", "tests/golden"]},
    "contractSha256Before": before["protected"]["src/kit/learning/contract.ts"],
    "contractSha256After": after["protected"]["src/kit/learning/contract.ts"],
    "goldenSha256Before": before["protected"]["tests/golden/s0-trace.json"],
    "goldenSha256After": after["protected"]["tests/golden/s0-trace.json"],
    "readme205ModelsSectionUnchanged": models_section_unchanged,
    "vite205ServerSettingsUnchanged": server_unchanged,
    "vite205SharedPluginStillAbsent": "serveSharedFolders" not in vite_after and "spaceModels" not in vite_after,
    "productionFinalInventoryMatches": production == final,
    "remainingOwnFixtureDirectories": [str(p.relative_to(GAME)) for p in (GAME / "tmp").glob("portal-build-*")],
    "diffCheckExitCode": diff.returncode,
    "parentStatusDeltaOutside207": {"added": sorted(parent_after - parent_before), "removed": sorted(parent_before - parent_after)},
}
save("verification.json", result)

# A reviewable patch relative to the dirty 205 baseline, including the two shared files.
patch = []
for name in owned:
    if name in ["README.md", "vite.config.ts"]:
        old = (OUT / "before" / name).read_text()
    elif name == "src/app/learning.ts":
        old = git("show", "HEAD:" + name)
    else:
        old = ""
    patch.extend(difflib.unified_diff(old.splitlines(keepends=True), (GAME / name).read_text().splitlines(keepends=True),
                                      fromfile="a/" + name if old else "/dev/null", tofile="b/" + name))
(OUT / "207-only.patch").write_text("".join(patch))
assert after["branch"] == "ts-codex" and before["head"] == after["head"]
assert not result["unexpectedPaths"] and not result["missing205Paths"]
assert kit_unchanged and models_section_unchanged and server_unchanged and result["vite205SharedPluginStillAbsent"]
assert result["productionFinalInventoryMatches"] and not result["remainingOwnFixtureDirectories"] and diff.returncode == 0
print(json.dumps(result, ensure_ascii=False, indent=2))
