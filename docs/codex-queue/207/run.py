"""Local evidence recorder; run from the parent repository. No network or Git writes."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
GAME = ROOT / "games/.wt-ts-codex"
OUT = Path(__file__).resolve().parent


def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def git(*args):
    return subprocess.check_output(["git", "-C", str(GAME), *args], cwd=ROOT, text=True)


def run(name, command, portal=None, raw=False):
    env = os.environ.copy()
    env.pop("VITE_PORTAL_URL", None)
    if portal is not None:
        env["VITE_PORTAL_URL"] = portal
    started = time.monotonic()
    result = subprocess.run(command, cwd=GAME, env=env, capture_output=True, text=True)
    (OUT / (name + (".json" if raw else ".log"))).write_text(result.stdout if raw else result.stdout + result.stderr)
    if raw:
        json.loads(result.stdout)
    record = {"command": command, "cwd": str(GAME), "VITE_PORTAL_URL": portal,
              "exitCode": result.returncode, "seconds": round(time.monotonic() - started, 3)}
    save(name + ("-run.json" if raw else ".json"), record)
    print(json.dumps({"name": name, **record}))


def inventory(name):
    files = []
    matches = []
    for p in sorted((GAME / "dist").rglob("*")):
        if not p.is_file():
            continue
        data = p.read_bytes()
        rel = p.relative_to(GAME / "dist").as_posix()
        files.append({"file": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()})
        start = 0
        while (offset := data.find(b"typing-game.local", start)) != -1:
            matches.append({"file": rel, "offset": offset,
                            "context": data[max(0, offset - 100):offset + 116].decode("utf8", "replace")})
            start = offset + len(b"typing-game.local")
    value = {"fileCount": len(files), "bytes": sum(p["bytes"] for p in files), "files": files,
             "localHostCount": len(matches), "localHostMatches": matches,
             "scannedTextFiles": sum(Path(p["file"]).suffix in [".html", ".js", ".css", ".json"] for p in files)}
    save(name, value)
    return value


def snapshot(name):
    protected = {}
    for folder in ["src/kit", "src/sim", "src/content", "tests/golden"]:
        for p in sorted((GAME / folder).rglob("*")):
            if p.is_file():
                protected[p.relative_to(GAME).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    save(name, {"head": git("rev-parse", "HEAD").strip(), "branch": git("branch", "--show-current").strip(),
                "status": git("status", "--short", "-uall").splitlines(), "protected": protected})


if __name__ == "__main__":
    action = sys.argv[1]
    if action == "before":
        snapshot("before.json")
        (OUT / "parent-status-before.txt").write_text(subprocess.check_output(["git", "status", "--short", "-uall"], cwd=ROOT, text=True))
        run("deploy-pack-before", ["pnpm", "deploy:pack"])
        run("pack-before", ["node", "src/kit/tools/deploy/check-pack.mjs", "dist", "--game", "typing-survival", "--json"], raw=True)
        value = inventory("dist-before.json")
        save("local-host-before.json", value["localHostMatches"])
        print(json.dumps({k: value[k] for k in ["fileCount", "bytes", "localHostCount"]}))
    elif action in ["red", "red-literal", "green"]:
        run("tests-" + action, ["pnpm", "exec", "vitest", "run", "tests/portal.test.ts", "tests/portal-build.test.ts", "tests/learning.test.ts",
                               "--reporter=default", "--reporter=json", "--outputFile=" + str(OUT / ("tests-" + action + "-results.json"))])
    elif action == "check":
        run("check", ["pnpm", "check"])
    elif action in ["after", "local", "final"]:
        local = action == "local"
        run("deploy-pack-" + action, ["pnpm", "deploy:pack:local" if local else "deploy:pack"], portal="https://typing-game.local/" if local else None)
        run("pack-" + action, ["node", "src/kit/tools/deploy/check-pack.mjs", "dist", "--game", "typing-survival", "--json"] + (["--allow-local-host"] if local else []), raw=True)
        value = inventory("production-bundle.json" if action == "after" else "dist-" + action + ".json")
        print(json.dumps({k: value[k] for k in ["fileCount", "bytes", "localHostCount"]}))
    elif action == "snapshot":
        snapshot("after.json")
