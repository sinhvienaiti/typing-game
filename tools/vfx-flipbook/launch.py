"""Entry point used by tools/vfx-flipbook/run.sh (runs under `python -I`)."""
import os
import runpy
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Bytecode goes to $VFXLAB_HOME/cache/pycache, never into the repo (set before any local import).
sys.pycache_prefix = os.path.join(
    os.environ.get("VFXLAB_HOME") or os.path.expanduser("~/VFXLab"), "cache", "pycache")
sys.path.insert(0, str(HERE))


def main() -> None:
    args = sys.argv[1:]
    if args and args[0] == "test":
        os.chdir(HERE)  # testpaths apply only when pytest starts in its rootdir
        sys.argv = ["pytest", "-c", str(HERE / "pytest.ini"), "--rootdir", str(HERE), *args[1:]]
        runpy.run_module("pytest", run_name="__main__", alter_sys=True)
        return
    from vfxflip.__main__ import main as cli
    sys.exit(cli(args))


if __name__ == "__main__":
    main()
