"""Thẻ spec âm thanh. Chạy: pnpm audio:specs <lệnh> (hoặc tools/audio-lab/run.sh specs <lệnh>).

  generate [--game G] [--check] [--prune]   sinh hoặc cập nhật thẻ, giữ phần sửa tay
  validate [--game G] [--strict] [file...]  kiểm thẻ theo schema/card.schema.json và luật riêng
  report   [--game G] [--json] [--out F]    số thẻ theo game và nhóm, các chỗ mã và danh sách âm lệch nhau
  list     [--game G] [--category C] [--status S] [--blocked B]
  export   [--game G] [--dry-run]           chép thẻ sang ~/AudioLab/review/staging/<game>/art-src/audio/specs/
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from common import env

from . import report, store, validate
from .generate import PLAN_PATH, run
from .readers import GAMES


def _root(args) -> Path:
    return Path(args.root).expanduser().resolve() if args.root else store.SPECS_DIR


def _games(args) -> list[str]:
    return args.game or list(GAMES)


def cmd_generate(args) -> int:
    results = run(_root(args), Path(args.games_root), Path(args.plan), _games(args), write=not args.check, prune=args.prune)
    changed = 0
    for r in results:
        st = r.status
        n = {k: sum(1 for v in st.values() if v == k) for k in ("created", "updated", "unchanged")}
        changed += n["created"] + n["updated"]
        kept = {i: k for i, k in r.kept.items() if k}
        print(f"{r.game}: {len(r.cards)} thẻ (mới {n['created']}, đổi {n['updated']}, giữ nguyên {n['unchanged']}), "
              f"giữ phần sửa tay ở {len(kept)} thẻ, {len(r.issues)} ghi nhận")
        for sid, paths in sorted(kept.items()):
            print(f"  giữ tay {sid}: {', '.join(paths)}")
        for p in r.orphans:
            print(f"  thẻ mồ côi (không còn id): {p.name}")
        for p in r.pruned:
            print(f"  đã xóa thẻ mồ côi: {p.name}")
        if args.check:
            for sid, s in sorted(st.items()):
                if s != "unchanged":
                    print(f"  cần sinh lại: {sid} ({'mới' if s == 'created' else 'đổi'})")
    if args.check:
        stale = changed + sum(len(r.orphans) for r in results)
        print("Thẻ khớp nguồn." if stale == 0 else f"{stale} thẻ cần sinh lại: chạy `pnpm audio:specs generate`.")
        return 1 if stale else 0
    paths = [p for g in _games(args) for p in store.card_files(_root(args), g)]
    problems, n = validate.check_files(paths)
    errors = [p for p in problems if p.level == validate.ERROR]
    for p in problems:
        print(p)
    print(f"Đã kiểm {n} thẻ: {len(errors)} lỗi, {len(problems) - len(errors)} cảnh báo. Xem chỗ lệch: pnpm audio:specs report")
    return 1 if errors else 0


def cmd_validate(args) -> int:
    paths = [Path(p).resolve() for p in args.files] or [p for g in _games(args) for p in store.card_files(_root(args), g)]
    if not paths:
        print("Không có thẻ nào để kiểm. Chạy trước: pnpm audio:specs generate", file=sys.stderr)
        return 2
    problems, n = validate.check_files(paths)
    errors = [p for p in problems if p.level == validate.ERROR]
    for p in problems:
        print(p)
    print(f"Đã kiểm {n} thẻ: {len(errors)} lỗi, {len(problems) - len(errors)} cảnh báo.")
    return 1 if errors or (args.strict and problems) else 0


def cmd_report(args) -> int:
    results = run(_root(args), Path(args.games_root), Path(args.plan), _games(args), write=False)
    text = json.dumps(report.as_json(results), ensure_ascii=False, indent=2) + "\n" if args.json else report.markdown(results)
    if args.out:
        out = Path(args.out).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"Đã ghi {out}")
    else:
        sys.stdout.write(text)
    return 0


def cmd_list(args) -> int:
    for path in [p for g in _games(args) for p in store.card_files(_root(args), g)]:
        c = store.load_file(path)
        if args.category and c.get("category") not in args.category:
            continue
        if args.status and c.get("status") not in args.status:
            continue
        if args.blocked and args.blocked not in (c.get("blocked_by") or []):
            continue
        d = (c.get("duration") or {}).get("target_ms")
        now = "+".join((c.get("source_plan") or {}).get("now") or [])
        print(f"{c['game']}\t{c['id']}\t{c.get('category')}\t{c.get('family')}\t{c.get('status')}\t{d if d is not None else '-'} ms\t{now}")
    return 0


def cmd_export(args) -> int:
    total = 0
    for game in _games(args):
        files = store.card_files(_root(args), game)
        dest = env.STAGING / game / "art-src" / "audio" / "specs"
        for f in files:
            if not args.dry_run:
                dest.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dest / f.name)
        total += len(files)
        print(f"{game}: {len(files)} thẻ -> {dest}{' (thử, chưa chép)' if args.dry_run else ''}")
    print(f"Tổng {total} thẻ. Người điều phối chép sang games/<game>/art-src/audio/specs/ khi games/** được mở (§11).")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="specs", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", help="thư mục chứa thẻ (mặc định tools/audio-lab/specs)")
    ap.add_argument("--games-root", default=str(env.GAMES), help="thư mục games/ (chỉ đọc)")
    ap.add_argument("--plan", default=str(PLAN_PATH), help="đường dẫn AUDIO_PIPELINE.md")
    sub = ap.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("generate", help="sinh hoặc cập nhật thẻ")
    g.add_argument("--game", action="append", choices=GAMES)
    g.add_argument("--check", action="store_true", help="không ghi; mã thoát 1 nếu thẻ cần sinh lại")
    g.add_argument("--prune", action="store_true", help="xóa thẻ mồ côi chưa sửa tay")
    g.set_defaults(func=cmd_generate)

    v = sub.add_parser("validate", help="kiểm thẻ")
    v.add_argument("--game", action="append", choices=GAMES)
    v.add_argument("--strict", action="store_true", help="cảnh báo cũng tính là lỗi")
    v.add_argument("files", nargs="*")
    v.set_defaults(func=cmd_validate)

    r = sub.add_parser("report", help="số thẻ và chỗ lệch")
    r.add_argument("--game", action="append", choices=GAMES)
    r.add_argument("--json", action="store_true")
    r.add_argument("--out")
    r.set_defaults(func=cmd_report)

    li = sub.add_parser("list", help="liệt kê thẻ")
    li.add_argument("--game", action="append", choices=GAMES)
    li.add_argument("--category", action="append")
    li.add_argument("--status", action="append")
    li.add_argument("--blocked")
    li.set_defaults(func=cmd_list)

    ex = sub.add_parser("export", help="chép thẻ sang thư mục staging của art-src")
    ex.add_argument("--game", action="append", choices=GAMES)
    ex.add_argument("--dry-run", action="store_true")
    ex.set_defaults(func=cmd_export)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
