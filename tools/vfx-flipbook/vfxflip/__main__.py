"""CLI: run.sh ingest <game> <id> [vN] | run.sh all <game> | run.sh probe <clip.mp4>"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from . import media, pipeline

USAGE = """vfx-flipbook: Firefly Video clip -> game flipbook
  run.sh ingest <game> <id> [vN]   one id (every version when vN is left out)
  run.sh all <game>                every clip in $VFXLAB_HOME/inbox/firefly/<game>/
  run.sh probe <clip.mp4>          ffprobe summary
  run.sh test [-q]                 synthetic-clip tests"""


def _print(reports: list[dict]) -> None:
    for r in reports:
        print(r["summary"])
        for w in r["warnings"]:
            print(f"    note: {w}")


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(USAGE)
        return 0 if argv else 2
    cmd, args = argv[0], argv[1:]
    try:
        if cmd == "ingest" and len(args) in (2, 3):
            _print(pipeline.ingest(args[0], args[1], args[2] if len(args) == 3 else None))
            return 0
        if cmd == "all" and len(args) == 1:
            reports, errors = pipeline.ingest_all(args[0])
            _print(reports)
            flagged = sum(1 for r in reports if r["flags"])
            print(f"— {len(reports)} flipbook(s), {flagged} flagged, {len(errors)} error(s); "
                  f"summary: {pipeline.lab_home() / 'out' / args[0] / 'summary.json'}")
            for e in errors:
                print(f"ERROR {e}", file=sys.stderr)
            return 1 if errors else 0
        if cmd == "probe" and len(args) == 1:
            print(json.dumps(media.probe(Path(args[0])), indent=2))
            return 0
    except (FileNotFoundError, media.MediaError) as e:
        print(f"vfx-flipbook: {e}", file=sys.stderr)
        return 3
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
