"""Bảng Nghe (Listening Board) CLI.

  run.sh board [serve] [--game G] [--batch B] [--session FILE ...] [--port N] [--open]
  run.sh board demo [--serve]          tạo phiên demo bằng âm tổng hợp
  run.sh board calib-0a [--critic-dir D]  tạo 2 phiên lô 0a từ 40 âm thử
  run.sh board from-critic OUT... --game G --batch B --session S   phiên từ danh sách nghe của bộ phê bình
  run.sh board make-session ...        tên khác của from-critic
  run.sh board check [phiên...]        kiểm file phiên
  run.sh board prepare [phiên...]      đo độ to, in mức chỉnh của từng file
  run.sh board summary --game G        tóm tắt ratings.jsonl
  run.sh board browser-check           thử bằng Chrome thật (CDP), chụp 1280x720 và 1920x1080
"""
from __future__ import annotations

import argparse
import os
import signal
import sys
import threading
from collections import Counter, defaultdict
from pathlib import Path

from common import env

from . import config, loudness, session
from .server import Board, make_server

COMMANDS = ("serve", "demo", "calib-0a", "from-critic", "make-session", "check", "prepare", "summary", "browser-check")


def _review_root(args) -> Path:
    return Path(args.review_root).expanduser() if args.review_root else env.REVIEW


def _cache_path(args) -> Path:
    if args.review_root:
        return _review_root(args) / ".board-cache" / "measure-v1.json"
    return env.CACHE / "board" / "measure-v1.json"


def _session_paths(args) -> list[Path]:
    if args.session:
        return [Path(p).expanduser() for p in args.session]
    root = _review_root(args)
    paths = sorted(root.glob(f"{args.game or '*'}/sessions/*.json"))
    if args.batch:
        paths = [p for p in paths if str(session.read_raw(p).get("batch") or "") == args.batch]
    return paths


def cmd_serve(args) -> int:
    board = Board(_review_root(args), sessions=_session_paths(args) if args.session else None,
                  game=args.game, batch=args.batch, cache_path=_cache_path(args))
    found = board.discover()
    for err in board.errors.values():
        print(f"board: bỏ qua phiên lỗi: {err}", file=sys.stderr)
    strict = args.port is not None
    port = args.port if strict else int(os.environ.get("AUDIOLAB_BOARD_PORT") or env.BOARD_PORT)
    try:
        httpd = make_server(board, env.BOARD_HOST, port, None if strict else env.BOARD_PORT_FALLBACK, args.verbose)
    except OSError as exc:
        print(f"board: không mở được cổng {port}: {exc}", file=sys.stderr)
        return 4
    url = f"http://{env.BOARD_HOST}:{board.port}/"
    if getattr(httpd, "used_fallback", False):
        print(f"board: CẢNH BÁO: cổng {port} đang bận, Bảng Nghe dùng cổng {board.port}.", file=sys.stderr)
    print(f"Bảng Nghe: {url}  ({len(found)} phiên; ghi điểm vào {_review_root(args)}/<game>/ratings.jsonl)")
    print("Ctrl+C để dừng.", flush=True)

    def warm():  # measure loudness now, so the first page open is quick
        for sid in list(found):
            try:
                board.get(sid)
            except Exception as exc:  # noqa: BLE001 - reported on the page as well
                print(f"board: phiên {sid}: {exc}", file=sys.stderr)

    threading.Thread(target=warm, daemon=True).start()

    def stop(*_):
        threading.Thread(target=httpd.shutdown, daemon=True).start()

    signal.signal(signal.SIGTERM, stop)
    if args.open:
        import webbrowser
        webbrowser.open(url)
    try:
        httpd.serve_forever(poll_interval=0.25)
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        board.cache.save()
    print("board: đã dừng.")
    return 0


def cmd_demo(args) -> int:
    from .demo import write_demo

    audio = Path(args.audio_dir).expanduser() if args.audio_dir else env.WORK / "_board-demo"
    path = write_demo(audio, _review_root(args))
    print(path)
    if args.serve:
        args.session = [str(path)]
        return cmd_serve(args)
    return 0


def cmd_calib(args) -> int:
    from .calib import write_sessions

    try:
        paths = write_sessions(env.FIXTURES / "poc40", _review_root(args), env.WORK, critic_dir=args.critic_dir,
                               batch=args.calib_batch, force=args.force)
    except FileExistsError as exc:
        print(f"board: {exc}", file=sys.stderr)
        return 1
    for p in paths:
        print(p)
    return 0


def cmd_from_critic(args) -> int:
    from .from_critic import FromCriticError, write_sessions

    try:
        paths, skipped = write_sessions(
            [Path(o) for o in args.out], _review_root(args), args.game, args.batch, args.session_id,
            title=args.title, seed=args.seed, ids=set(args.id) if args.id else None,
            max_items=args.max_items, force=args.force, anchors=args.anchors)
    except FromCriticError as exc:
        print(f"board: {exc}", file=sys.stderr)
        return 1
    for line in skipped:
        print(f"bỏ qua  {line}")
    for p in paths:
        print(p)
    return 0


def _load_all(args) -> list[tuple[Path, session.Session | Exception]]:
    cache = loudness.MeasureCache(_cache_path(args))
    out = []
    for p in _session_paths(args):
        try:
            out.append((p, session.load(p, cache)))
        except session.SessionError as exc:
            out.append((p, exc))
    return out


def cmd_check(args) -> int:
    bad = 0
    for p, s in _load_all(args):
        if isinstance(s, Exception):
            bad += 1
            print(f"LỖI  {p}: {s}")
        else:
            n = len(s.items)
            warn = f"  (quá {s.max_items} id/phiên)" if n > s.max_items else ""
            print(f"ĐẠT  {p}: {s.sid}, {n} id{warn}")
    return 1 if bad else 0


def cmd_prepare(args) -> int:
    for p, s in _load_all(args):
        if isinstance(s, Exception):
            print(f"LỖI  {p}: {s}")
            continue
        print(f"# {s.sid} ({s.game}) mục tiêu {s.target_lufs} LUFS-M")
        for it in s.items:
            short = f"  CẢNH BÁO: một bản vẫn nhỏ hơn {it.loudness_short_db} dB" if it.loudness_short_db > 0.5 else ""
            print(f"  {it.key}  [{it.loudness_source}]{short}")
            for c in it.displayed:
                for f, g, m in zip(c.files, c.gains, c.measures):
                    print(f"    {c.label} {g:+6.2f} dB  LUFS-M {m.get('lufs_m_max')}  TP {m.get('true_peak_db')}  {f.name}")
    return 0


def cmd_summary(args) -> int:
    from .store import Store

    store = Store(_review_root(args))
    games = [args.game] if args.game else sorted(p.name for p in _review_root(args).iterdir() if p.is_dir()) \
        if _review_root(args).is_dir() else []
    for g in games:
        lines = store.lines(g)
        if not lines:
            continue
        latest = {}
        for ln in lines:
            latest[(ln.get("session"), ln.get("item"))] = ln
        picks, stars = Counter(), defaultdict(list)
        for ln in latest.values():
            roles = ln.get("roles") or {}
            if ln.get("pick"):
                picks[roles.get(ln["pick"], "?")] += 1
            elif ln.get("none"):
                picks["(không bản nào)"] += 1
            for h, v in (ln.get("stars") or {}).items():
                stars[roles.get(h, "?")].append(v)
        print(f"# {g}: {len(lines)} dòng, {len(latest)} id đã chấm, {store.bad_lines(g)} dòng hỏng")
        print("  chọn theo vai trò: " + ", ".join(f"{k} {v}" for k, v in picks.most_common()))
        print("  sao trung bình:    " + ", ".join(f"{k} {sum(v) / len(v):.2f} (n={len(v)})" for k, v in sorted(stars.items())))
    return 0


def cmd_browser(args) -> int:
    from .browser_check import main as browser_main

    return browser_main(args.rest)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in COMMANDS + ("-h", "--help"):
        argv.insert(0, "serve")
    ap = argparse.ArgumentParser(prog="board", description="Bảng Nghe: nghe mù, đã cân độ to (AUDIO_PIPELINE.md §7).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, sessions=True):
        p.add_argument("--review-root", help="thư mục review (mặc định ~/AudioLab/review)")
        if sessions:
            p.add_argument("--game", help="lọc theo game (dragon-hold, typing-defense, ...)")
            p.add_argument("--batch", help="lọc theo lô")
            p.add_argument("--session", action="append", help="file phiên JSON (lặp lại được)")
        return p

    s = common(sub.add_parser("serve", help="mở Bảng Nghe"))
    s.add_argument("--port", type=int, help="cổng cố định (mặc định 3191, bận thì 3192)")
    s.add_argument("--open", action="store_true", help="mở trình duyệt")
    s.add_argument("--verbose", action="store_true")
    d = common(sub.add_parser("demo", help="tạo phiên demo"), sessions=False)
    d.add_argument("--audio-dir", help="nơi ghi âm demo (mặc định ~/AudioLab/work/_board-demo)")
    d.add_argument("--serve", action="store_true", help="mở Bảng Nghe với phiên demo")
    d.add_argument("--port", type=int)
    d.add_argument("--open", action="store_true")
    d.add_argument("--verbose", action="store_true")
    c0 = common(sub.add_parser("calib-0a", help="tạo phiên lô 0a"), sessions=False)
    c0.add_argument("--critic-dir", help="thư mục kết quả của bộ phê bình chạy trên 40 âm thử (mặc định: bản thử PoC)")
    c0.add_argument("--batch", dest="calib_batch", default="0a", help="nhãn lô của hai phiên (mặc định 0a)")
    c0.add_argument("--force", action="store_true", help="ghi đè file phiên đã có")
    fc = common(sub.add_parser("from-critic", aliases=["make-session"],
                              help="tạo phiên từ danh sách nghe của bộ phê bình"), sessions=False)
    fc.add_argument("out", nargs="+", help="thư mục kết quả của run.sh critic (có _batch.json)")
    fc.add_argument("--game", required=True)
    fc.add_argument("--batch", required=True)
    fc.add_argument("--session", dest="session_id", required=True, help="tên phiên, ví dụ s1")
    fc.add_argument("--title")
    fc.add_argument("--seed", type=int)
    fc.add_argument("--id", action="append", help="chỉ lấy id này (lặp lại được)")
    fc.add_argument("--max-items", type=int, default=10, help="tối đa id mỗi phiên (mặc định 10, mục 7)")
    fc.add_argument("--force", action="store_true", help="ghi đè file phiên đã có")
    fc.add_argument("--anchors", type=int, help="số cặp mốc mỗi phiên (mặc định 4, 0 để tắt; mục 4.6)")
    common(sub.add_parser("check", help="kiểm file phiên"))
    common(sub.add_parser("prepare", help="đo độ to và in mức chỉnh"))
    sm = common(sub.add_parser("summary", help="tóm tắt điểm đã chấm"), sessions=False)
    sm.add_argument("--game")
    b = sub.add_parser("browser-check", help="thử bằng Chrome thật")
    b.add_argument("rest", nargs=argparse.REMAINDER)
    args = ap.parse_args(argv)
    if args.cmd == "demo":
        args.game = args.batch = None
    return {"serve": cmd_serve, "demo": cmd_demo, "calib-0a": cmd_calib, "from-critic": cmd_from_critic, "make-session": cmd_from_critic,
            "check": cmd_check,
            "prepare": cmd_prepare, "summary": cmd_summary, "browser-check": cmd_browser}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
