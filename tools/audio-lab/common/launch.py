"""Entry point used by tools/audio-lab/run.sh (runs under `python -I`).

run.sh <target> [args...]
  target = alias (see ENTRYPOINTS) | dotted module | path/to/script.py | path/to/script.mjs
"""
import importlib.util
import os
import runpy
import sys
from pathlib import Path

LAB = Path(__file__).resolve().parent.parent
# Bytecode goes to ~/AudioLab/cache/pycache, never into the repo (set before any import below).
sys.pycache_prefix = os.path.join(
    os.environ.get("AUDIOLAB_HOME") or os.path.expanduser("~/AudioLab"), "cache", "pycache")
sys.path.insert(0, str(LAB))

from common import env  # noqa: E402

# One place to map pnpm script names to code. "node:" runs a Node script with the same env.
ENTRYPOINTS = {
    "critic": "critic",                       # critic/__main__.py
    "board": "board",                         # board/__main__.py (or "node:board/server.mjs")
    "specs": "specs",                         # specs/__main__.py
    "licence-check": "build.licence_check",   # build/licence_check.py
    "build": "build",                         # build/__main__.py (render, release, mark-ai, ledger)
    "sampler": "sampler",                     # sampler/__main__.py
    "libraries": "gen.fetch_libraries",       # CC0 libraries + SOURCES.jsonl
    "batch0": "common.batch0",                # common/batch0.py: end-to-end run of phase 0-1
    "batch0b": "common.batch0b",              # common/batch0b.py: batch 0b round 2 (Stable Audio 3)
    "sa3": "gen.sa3",                         # gen/sa3.py: Stable Audio 3 jobs from spec cards
    "process": "gen.process",                 # gen/process.py: model output -> review candidates
    "models": "common.fetch_models",          # critic weights in the HF cache (check / --download)
    "test": "pytest",
}


def _die(msg: str, code: int = 3) -> None:
    print(f"audio-lab: {msg}", file=sys.stderr)
    sys.exit(code)


def _run_node(script: Path, args: list[str]) -> None:
    if not script.is_file():
        _die(f"chưa có file {script.relative_to(LAB)}")
    os.execvp("node", ["node", str(script), *args])


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        print("Aliases: " + ", ".join(f"{k} -> {v}" for k, v in ENTRYPOINTS.items()))
        sys.exit(0 if len(sys.argv) >= 2 else 2)
    target, args = sys.argv[1], sys.argv[2:]
    env.apply()
    target = ENTRYPOINTS.get(target, target)

    if target.startswith("node:"):
        _run_node(LAB / target[5:], args)
    if target.endswith((".mjs", ".js")):
        _run_node((LAB / target) if not os.path.isabs(target) else Path(target), args)
    if target.endswith(".py") or "/" in target:
        path = Path(target) if os.path.isabs(target) else (Path.cwd() / target)
        if not path.is_file():
            path = LAB / target
        if not path.is_file():
            _die(f"không thấy script {target}")
        sys.argv = [str(path), *args]
        runpy.run_path(str(path), run_name="__main__")
        return

    if target == "pytest":
        sys.argv = ["pytest", "-c", str(LAB / "pytest.ini"), "--rootdir", str(LAB), *args]
        runpy.run_module("pytest", run_name="__main__", alter_sys=True)
        return

    try:
        spec = importlib.util.find_spec(target)
        main_spec = importlib.util.find_spec(target + ".__main__") if spec and spec.submodule_search_locations else spec
    except ModuleNotFoundError:
        spec = main_spec = None
    if spec is None or main_spec is None:
        _die(f"module '{target}' chưa có điểm vào (đang được làm?)")
    sys.argv = [target, *args]
    runpy.run_module(target, run_name="__main__", alter_sys=True)


if __name__ == "__main__":
    main()
