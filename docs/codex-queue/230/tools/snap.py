#!/usr/bin/env python3
"""Ticket 230: read-only snapshot of the two Last Line worktrees.

Usage (from the parent repo root): python3 -I docs/codex-queue/230/tools/snap.py <out.json>
Records HEAD, branch, status, and size + SHA-256 of every file Git sees
(ls-files -co --exclude-standard) plus everything under public/, the top
level of node_modules (name, kind, mtime) and the mtime of Vitest results.
"""
import hashlib, json, os, subprocess, sys

ROOT = os.getcwd()
TREES = ["games/.wt-ts-art", "games/.wt-ts-codex"]


def git(wt, *args):
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    return subprocess.run(["git", "-C", wt, "--no-optional-locks", *args], capture_output=True, env=env, check=True).stdout


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def tree(wt):
    files = set(p for p in git(wt, "ls-files", "-co", "--exclude-standard", "-z").decode().split("\0") if p)
    pub = os.path.join(wt, "public")
    for d, _, fs in os.walk(pub):
        for f in fs:
            files.add(os.path.relpath(os.path.join(d, f), wt))
    out = {}
    for p in sorted(files):
        full = os.path.join(wt, p)
        if os.path.islink(full):
            out[p] = {"link": os.readlink(full)}
        elif os.path.isfile(full):
            out[p] = {"bytes": os.path.getsize(full), "sha256": sha(full)}
        else:
            out[p] = {"missing": True}
    nm = os.path.join(wt, "node_modules")
    top = []
    for e in sorted(os.listdir(nm)):
        full = os.path.join(nm, e)
        st = os.lstat(full)
        kind = "link" if os.path.islink(full) else ("dir" if os.path.isdir(full) else "file")
        top.append({"name": e, "kind": kind, "mtime": st.st_mtime})
    results = []
    vroot = os.path.join(nm, ".vite", "vitest")
    if os.path.isdir(vroot):
        for d, _, fs in os.walk(vroot):
            for f in fs:
                if f == "results.json":
                    full = os.path.join(d, f)
                    results.append({"path": os.path.relpath(full, wt), "mtime": os.stat(full).st_mtime, "sha256": sha(full)})
    return {
        "branch": git(wt, "branch", "--show-current").decode().strip(),
        "head": git(wt, "rev-parse", "HEAD").decode().strip(),
        "status": git(wt, "status", "--short", "-uall").decode().splitlines(),
        "fileCount": len(out),
        "files": out,
        "nodeModulesTop": top,
        "vitestResults": results,
    }


snap = {wt: tree(wt) for wt in TREES}
with open(sys.argv[1], "w") as f:
    json.dump(snap, f, indent=1, sort_keys=True)
    f.write("\n")
print({wt: {"files": s["fileCount"], "head": s["head"][:9], "status": len(s["status"])} for wt, s in snap.items()})
