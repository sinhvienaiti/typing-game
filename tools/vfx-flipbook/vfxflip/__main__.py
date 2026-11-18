"""CLI for flipbook ingestion, probing and full-resolution video export."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import atlas_ktx2, ktx2, media, pipeline, upgrade, video_export

USAGE = """vfx-flipbook: Firefly Video clip -> game flipbook
  run.sh ingest <game> <id> [vN]   one id (every version when vN is left out)
  run.sh all <game>                every clip in $VFXLAB_HOME/inbox/firefly/<game>/
  run.sh probe <clip.mp4>          ffprobe summary
  run.sh ktx2 <manifest directory> [--only id,id] [--force]
  run.sh upgrade --like <manifest.json>:<id> --out <directory> --cell WxH --fps N
                 [--frames 64] [--look cool|neutral] [--no-mv] [--ktx2 uastc,etc1s|none]
                 [--videos crf23,720p] [--uastc-level 2] [--etc1s-quality 150]
                 [--max-atlas 4096] [--game immortality-cultivation] [--repo-root <dir>]
  run.sh export-video --manifest <manifest.json> [--ids a,b,...] [--jobs 3]
                      [--force] [--dry-run] [--repo-root <directory>]
  run.sh test [-q]                 synthetic-clip tests"""


def _positive_int(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("phải lớn hơn 0")
    return number


def _ktx2(args: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="vfxflip ktx2")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--only", help="các id cần nén, phân cách bằng dấu phẩy")
    parser.add_argument("--force", action="store_true")
    opts = parser.parse_args(args)
    only = {cid.strip() for cid in opts.only.split(",") if cid.strip()} if opts.only is not None else None
    atlas_ktx2.run(opts.folder, only=only, force=opts.force)
    return 0


def _export_video(args: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="vfxflip export-video")
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--ids", help="các id cần xuất, phân cách bằng dấu phẩy")
    parser.add_argument("--jobs", type=_positive_int, default=3)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    opts = parser.parse_args(args)
    ids = {cid.strip() for cid in opts.ids.split(",") if cid.strip()} if opts.ids is not None else None
    video_export.export_manifest(opts.manifest, repo_root=opts.repo_root, ids=ids,
                                 jobs=opts.jobs, force=opts.force, dry_run=opts.dry_run)
    return 0


def _upgrade(args: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="vfxflip upgrade")
    parser.add_argument("--like", required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--cell", required=True)
    parser.add_argument("--fps", type=float, required=True)
    parser.add_argument("--frames", type=int, default=64)
    parser.add_argument("--look")
    parser.add_argument("--no-mv", action="store_true")
    parser.add_argument("--ktx2", dest="ktx2_codecs", default="uastc,etc1s")
    parser.add_argument("--videos", default="")
    parser.add_argument("--uastc-level", type=int, default=2)
    parser.add_argument("--etc1s-quality", type=int, default=150)
    parser.add_argument("--max-atlas", type=int, default=4096)
    parser.add_argument("--game", default="immortality-cultivation")
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    opts = vars(parser.parse_args(args))
    try:
        opts["cell"] = tuple(int(s) for s in opts["cell"].lower().split("x"))
    except ValueError as exc:
        raise media.MediaError("cell cần WxH, ví dụ 768x432") from exc
    upgrade.run(**opts)
    return 0


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
        if cmd == "ktx2":
            return _ktx2(args)
        if cmd == "upgrade":
            return _upgrade(args)
        if cmd == "export-video":
            return _export_video(args)
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
    except (FileNotFoundError, media.MediaError, video_export.VideoExportError, ktx2.Ktx2Error) as e:
        print(f"vfx-flipbook: {e}", file=sys.stderr)
        return 3
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
