"""Print §10.6 licences.jsonl lines for library files used by a render.

  run.sh gen.licence_lines ~/AudioLab/work/_sampler/renders/word-hit.json      # a sampler report
  run.sh gen.licence_lines "vcsl/Chordophones/Zithers/Dan Tranh/Normal/B4_ff_1.wav" --out lines.jsonl

Inputs: sampler report JSON files (their `sources`), or paths relative to ~/AudioLab/libraries
(or absolute). One JSON line per distinct file, ready to append to art-src/audio/licences.jsonl;
copy each `licence_copy_source` to art-src/audio/<licence_copy> with it.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from common import env
from gen import libraries as L


def files_from(arg: str, root: Path) -> list[Path]:
    p = Path(arg).expanduser()
    if p.suffix == ".json" and p.is_file():
        rep = json.loads(p.read_text())
        return [root / s["file"] if not Path(s["file"]).is_absolute() else Path(s["file"])
                for s in rep.get("sources", [])]
    return [p if p.is_absolute() else root / p]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="gen.licence_lines", description=__doc__.split("\n")[0])
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", help="ghi ra file JSONL thay vì stdout")
    ap.add_argument("--root", default=str(L.ROOT), help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    env.apply()
    root = Path(a.root)
    ledger = L.read_ledger(root)
    seen, lines, missing = set(), [], []
    for arg in a.inputs:
        for f in files_from(arg, root):
            if f in seen:
                continue
            seen.add(f)
            try:
                lines.append(L.licence_line(f, root, ledger))
            except (LookupError, ValueError, OSError):   # not a library file: needs its own ledger row
                missing.append(str(f))
    for m in missing:
        print(f"KHÔNG có trong sổ thư viện (cần dòng nguồn riêng): {m}", file=sys.stderr)
    text = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in lines)
    if a.out:
        Path(a.out).write_text(text)
        print(f"{len(lines)} dòng -> {a.out}")
    else:
        sys.stdout.write(text)
    return 2 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
