"""Record ticket 187 commands, exit codes, timing and output."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--portal")
parser.add_argument("command", nargs=argparse.REMAINDER)
args = parser.parse_args()
command = args.command
if command[0] == "--":
    command = command[1:]
evidence = Path(__file__).resolve().parent
root = evidence.parents[2] / "games/.wt-dh-codex"
env = os.environ.copy()
env.pop("VITE_PORTAL_URL", None)
if args.portal is not None:
    env["VITE_PORTAL_URL"] = args.portal
started = time.monotonic()
result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
(evidence / f"{args.name}.log").write_text(result.stdout + result.stderr)
record = {"command": command, "cwd": str(root), "VITE_PORTAL_URL": args.portal,
          "exitCode": result.returncode, "seconds": round(time.monotonic() - started, 3)}
(evidence / f"{args.name}.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(record, ensure_ascii=False))
print((result.stdout + result.stderr)[-2500:])
