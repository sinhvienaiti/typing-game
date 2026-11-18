"""Real-browser check of the Listening Board (Chrome over CDP, keyboard only).

Builds the demo session in a fresh folder under ~/AudioLab/work/_board-check/, starts the
board (127.0.0.1:3191, or 3192 when busy), runs tools/board-check.mjs through
tools/cdp-run.mjs, stops the server, then verifies ratings.jsonl line by line.
Screenshots: ~/AudioLab/work/_board-check/shots/*.png (outside the repo).
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from common import env

from . import config
from .demo import write_demo

HERE = Path(__file__).resolve().parent
TOOLS = HERE / "tools"


def _wait_url(proc: subprocess.Popen, timeout: float = 30.0) -> str:
    deadline = time.time() + timeout
    while time.time() < deadline:
        line = proc.stdout.readline()
        if not line:
            if proc.poll() is not None:
                break
            continue
        sys.stdout.write("  server: " + line)
        m = re.search(r"(http://127\.0\.0\.1:\d+/)", line)
        if m:
            return m.group(1)
    raise RuntimeError("Bảng Nghe không khởi động được")


def _json_tail(text: str) -> dict:
    start = text.find("{")
    if start < 0:
        raise ValueError("cdp-run không in JSON")
    return json.loads(text[start:])


def verify(ratings: Path) -> list[str]:
    """Return problems in the ratings written by the scenario (empty = all good)."""
    lines = [json.loads(x) for x in ratings.read_text("utf-8").splitlines() if x.strip()]
    problems = []
    by_item = {ln["item"]: ln for ln in lines}
    expect_items = ["01-demo.phim", "02-demo.chuong", "04-demo.xu"]
    if [ln["item"] for ln in lines] != expect_items:
        problems.append(f"thứ tự dòng: {[ln['item'] for ln in lines]} != {expect_items}")
    for ln in lines:
        if ln.get("schema") != config.RATING_SCHEMA or ln.get("kind") != "rating":
            problems.append(f"{ln.get('item')}: schema/kind sai")
        if ln.get("device") != "headphones" or ln.get("session") != "demo" or ln.get("game") != "_demo":
            problems.append(f"{ln.get('item')}: device/session/game sai")
        if sorted(ln["order"]) != sorted("ABCD"[: len(ln["shown"])]):
            problems.append(f"{ln.get('item')}: order sai")
    label = lambda ln, lb: ln["shown"][ln["order"].index(lb)]  # noqa: E731
    one = by_item.get("01-demo.phim")
    if one:
        want = {"A": 4, "B": 2, "C": 3}
        got = {lb: one["stars"].get(label(one, lb)) for lb in want}
        if got != want:
            problems.append(f"phim: sao {got} != {want}")
        if one["pick"] != label(one, "A") or not one["pick_auto"]:
            problems.append("phim: bản tốt nhất phải là A (tự chọn theo sao)")
        if one["tags"].get(label(one, "B")) != ["chói", "yếu/mỏng"]:
            problems.append(f"phim: nhãn của B {one['tags']}")
        if one["note"] != "A gọn, B mỏng":
            problems.append(f"phim: ghi chú {one['note']!r}")
        if sorted(one["roles"].values()) != ["distinct", "probe", "top"] or not one["probe"]:
            problems.append(f"phim: vai trò {one['roles']}")
        if not {"loop", "small"} <= set(one["contexts_heard"]):
            problems.append(f"phim: bối cảnh đã nghe {one['contexts_heard']}")
        if sum(one["listens"].values()) < 4:
            problems.append(f"phim: số lần nghe {one['listens']}")
        g = {Path(p[0]).name: one["gain_db"][h][0] for h, p in one["files"].items()}
        if abs((g["phim-sang.wav"] - g["phim-sang-to.wav"]) - 10.0) > 0.05:
            problems.append(f"phim: chỉnh độ to không bù đúng 10 dB: {g}")
    two = by_item.get("02-demo.chuong")
    if two:
        if two["pick"] != label(two, "B") or two["pick_auto"]:
            problems.append("chuong: bản tốt nhất phải là B (chọn tay)")
        if {lb: two["stars"].get(label(two, lb)) for lb in "AB"} != {"A": 3, "B": 5}:
            problems.append(f"chuong: sao {two['stars']}")
        if two["tags"].get(label(two, "B")) != ["hay", "hợp game"]:
            problems.append(f"chuong: nhãn {two['tags']}")
        if not two["loudness"].startswith("critic:"):
            problems.append(f"chuong: độ to phải lấy từ bộ phê bình, đang là {two['loudness']}")
    four = by_item.get("04-demo.xu")
    if four:
        if four["mode"] != "variants" or four.get("dropped") != [label(four, "C")]:
            problems.append(f"xu: dropped {four.get('dropped')}")
    return problems


def run(port: int | None = None, keep: bool = False) -> int:
    root = env.WORK / "_board-check"
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = root / f"run-{stamp}"
    shots = root / "shots"
    for old in root.glob("run-*"):
        shutil.rmtree(old, ignore_errors=True)
    shutil.rmtree(shots, ignore_errors=True)
    shots.mkdir(parents=True, exist_ok=True)
    review = run_dir / "review"
    session_file = write_demo(run_dir / "audio", review)
    launch = env.LAB / "common" / "launch.py"
    cmd = [sys.executable, "-I", str(launch), "board", "serve", "--review-root", str(review),
           "--session", str(session_file)]
    if port is not None:
        cmd += ["--port", str(port)]
    print(f"browser-check: {run_dir}")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=os.environ.copy())
    try:
        url = _wait_url(proc)
        res = subprocess.run(
            ["node", str(TOOLS / "cdp-run.mjs"), str(TOOLS / "board-check.mjs"), "--width=1280", "--height=720"],
            capture_output=True, text=True, timeout=240,
            env={**os.environ, "URL": url + "?s=demo", "OUT_DIR": str(shots)})
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
    if res.returncode != 0:
        print(res.stdout[-4000:], res.stderr[-4000:], sep="\n")
        return 1
    out = _json_tail(res.stdout)
    checks = out["result"]["checks"]
    print(json.dumps(checks, ensure_ascii=False, indent=1))
    problems = []
    if out.get("exceptions"):
        problems.append(f"lỗi JS trên trang: {out['exceptions']}")
    errors = [x for x in out.get("logs", []) if x.startswith("error")]
    if errors:
        problems.append(f"console error: {errors}")
    expect = {
        "phase": "item", "item1": "demo.phim", "ctxDefault1": "loop", "cardBefore": 403, "revealBefore": 403,
        "saved1": True, "item2": "demo.chuong", "cardAfter": 200, "lightbox": True, "item3": "demo.trung",
        "help": True, "resumeDevice": "headphones", "saved4": True,
    }
    for k, v in expect.items():
        if checks.get(k) != v:
            problems.append(f"{k}: {checks.get(k)!r} != {v!r}")
    if not (checks.get("loop") or {}).get("events") == 20:
        problems.append(f"loop: {checks.get('loop')}")
    if checks.get("blindBeforeRating") != {"domClean": True, "netClean": True}:
        problems.append(f"nghe mù bị lộ trước khi chấm: {checks.get('blindBeforeRating')}")
    if checks.get("blindEnd") != {"domClean": True, "netClean": True}:
        problems.append(f"nghe mù bị lộ: {checks.get('blindEnd')}")
    if not checks.get("thumbs") or not all(w and w > 0 for w in checks["thumbs"]):
        problems.append(f"thẻ ảnh không hiện: {checks.get('thumbs')}")
    if "Tiếp tục từ id 3" not in (checks.get("resumeButton") or ""):
        problems.append(f"resume: {checks.get('resumeButton')!r}")
    loop4 = checks.get("loop4") or {}
    if loop4.get("label") is not None or "C" in loop4.get("labels", ["C"]):
        problems.append(f"lượt biến thể vẫn phát bản đã bỏ: {loop4}")
    if "còn thiếu sao" not in (checks.get("tryEarlyEnter") or ""):
        problems.append(f"Enter khi chưa chấm phải báo thiếu: {checks.get('tryEarlyEnter')!r}")
    spill = {k: v for k, v in (checks.get("overflow") or {}).items() if isinstance(v, (int, float)) and v > 0}
    if spill:
        problems.append(f"trang tràn khỏi màn hình (px): {spill}")
    problems += verify(review / "_demo" / "ratings.jsonl")
    print("ảnh chụp:", *out["result"]["shots"], sep="\n  ")
    print("ratings:", review / "_demo" / "ratings.jsonl")
    if problems:
        print("TRƯỢT:", *problems, sep="\n  - ")
        return 1
    print("ĐẠT: Bảng Nghe chạy đúng trên Chrome thật (2 id chấm bằng phím, lượt biến thể, resume).")
    if not keep:
        shutil.rmtree(run_dir / "audio", ignore_errors=True)
    return 0


def main(argv: list[str]) -> int:
    port = None
    if "--port" in argv:
        port = int(argv[argv.index("--port") + 1])
    return run(port=port, keep="--keep" in argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
