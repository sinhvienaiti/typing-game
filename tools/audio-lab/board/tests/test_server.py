"""Listening Board: sessions, blind labels, loudness matching and the HTTP API."""
from __future__ import annotations

import json
import socket
import threading
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from board import config, loudness, session
from board.server import Board, make_server

SR = 48000


def tone(path: Path, freq=440.0, dur=0.3, peak_db=-12.0, decay=0.08) -> Path:
    t = np.arange(int(SR * dur)) / SR
    x = np.sin(2 * np.pi * freq * t) * np.exp(-t / decay)
    x *= 10 ** (peak_db / 20) / np.max(np.abs(x))
    sf.write(str(path), x, SR, subtype="PCM_16")
    return path


def write_session(root: Path, sid: str, items: list[dict], **extra) -> Path:
    p = root / "review" / "_test" / "sessions" / f"{sid}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"schema": config.SESSION_SCHEMA, "session": sid, "game": "_test", "batch": "t1",
                             "seed": 11, "items": items, **extra}, ensure_ascii=False), "utf-8")
    return p


@pytest.fixture()
def lab(tmp_path):
    a = tone(tmp_path / "hit-a.wav", 440, peak_db=-14)
    b = tone(tmp_path / "hit-b-loud.wav", 440, peak_db=-4)          # same sound, +10 dB
    c = tone(tmp_path / "hit-c.wav", 880, peak_db=-12)
    d = tone(tmp_path / "bell.wav", 660, dur=0.6, peak_db=-6, decay=0.2)
    v = [tone(tmp_path / f"coin-{i}.wav", 1500 + 60 * i, dur=0.2) for i in range(3)]
    items = [
        {"id": "hit", "family": "trung", "probe": True, "desc": "Trúng nhỏ",
         "candidates": [{"file": str(a), "role": "top"}, {"file": str(b), "role": "distinct"}, {"file": str(c), "role": "probe"}]},
        {"id": "bell", "family": "thuong", "candidates": [str(d)]},
        {"id": "coin", "family": "thuong", "mode": "variants", "candidates": [str(x) for x in v]},
    ]
    path = write_session(tmp_path, "s1", items)
    return {"root": tmp_path, "review": tmp_path / "review", "session": path, "files": {"a": a, "b": b, "c": c, "d": d}}


@pytest.fixture()
def server(lab):
    board = Board(lab["review"], cache_path=lab["root"] / "cache.json")
    httpd = make_server(board, "127.0.0.1", 0)
    th = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
    th.start()
    yield {"url": f"http://127.0.0.1:{board.port}", "board": board, "port": board.port, **lab}
    httpd.shutdown()
    httpd.server_close()


def call(srv, path, body=None, headers=None, method=None):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"} if body is not None else {}
    h.update(headers or {})
    req = urllib.request.Request(srv["url"] + path, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            raw = r.read()
            ctype = r.headers.get("Content-Type", "")
            return r.status, (json.loads(raw) if ctype.startswith("application/json") else raw)
    except urllib.error.HTTPError as e:
        raw = e.read()
        return e.code, json.loads(raw) if raw.startswith(b"{") else raw


def label_map(view_item, s: session.Session, key: str) -> dict[str, str]:
    """label -> file name (test side only; the page never sees this)."""
    it = s.item(key)
    return {c.label: c.files[0].name for c in it.candidates}


# ---------------------------------------------------------------- session + loudness
def test_labels_blind_and_fixed_by_seed(lab):
    s1 = session.load(lab["session"])
    s2 = session.load(lab["session"])
    assert [c.label for c in s1.items[0].candidates] == [c.label for c in s2.items[0].candidates]
    assert sorted(c.label for c in s1.items[0].candidates) == ["A", "B", "C"]
    view = json.dumps([session.item_view(i) for i in s1.items], ensure_ascii=False)
    for leak in ("hit-a", ".wav", "probe", "distinct", "top", str(lab["root"])):
        assert leak not in view
    raw = json.loads(lab["session"].read_text())
    orders = set()
    for seed in range(8):
        raw["seed"] = seed
        orders.add(tuple(c.label for c in session.build(raw, lab["session"], None).items[0].candidates))
    assert len(orders) > 1      # different seeds shuffle differently


def test_default_roles_and_contexts(lab):
    s = session.load(lab["session"])
    hit, bell, coin = s.items
    assert [c.role for c in hit.candidates] == ["top", "distinct", "probe"] and hit.probe
    assert hit.contexts[0] == "loop"            # dense family: loop first (§7)
    assert bell.candidates[0].role == "top"
    assert {c.role for c in coin.candidates} == {"variant"}
    assert hit.loop["interval_ms"] == 250 and hit.loop["count"] == 20


def test_loudness_matching_cancels_level(lab):
    s = session.load(lab["session"])
    by_name = {c.files[0].name: (c.gains[0], c.measures[0]) for c in s.items[0].candidates}
    ga, ma = by_name["hit-a.wav"]
    gb, mb = by_name["hit-b-loud.wav"]
    assert abs((ga - gb) - 10.0) < 0.05                       # louder file is turned down by exactly 10 dB
    assert abs((ma["lufs_m_max"] + ga) - (mb["lufs_m_max"] + gb)) < 0.01
    for c in s.items[0].candidates:                            # nothing goes over the ceiling
        assert c.measures[0]["true_peak_db"] + c.gains[0] <= loudness.CEILING_DBTP + 1e-6
    assert s.items[0].loudness_source == "board:lufs_m_max"


def test_quiet_file_still_matched():
    f = lambda lv, tp: {"measure": {"lufs_m_max": lv, "true_peak_db": tp}, "critic": None}  # noqa: E731
    src, g, short = loudness.item_gains([f(-58.32, -32.56), f(-14.39, -1.13), f(-6.23, 0.36)])
    played = [-58.32 + g[0], -14.39 + g[1], -6.23 + g[2]]
    assert short == 0 and max(played) - min(played) < 0.02               # the item plays quieter, all matched
    assert -32.56 + g[0] <= loudness.CEILING_DBTP + 1e-6
    src, g, short = loudness.item_gains([f(-90.0, -70.0), f(-14.0, -1.0)])   # near silence: floor, then short
    assert abs(-14.0 + g[1] - loudness.MIN_GOAL_LUFS) < 0.01 and g[0] == loudness.MAX_BOOST_DB and short > 20


def test_critic_loudness_used_only_when_complete(lab, tmp_path):
    a, b = lab["files"]["a"], lab["files"]["b"]
    (tmp_path / "hit-a.json").write_text(json.dumps({"lufs_momentary_max": -30.0}))
    p = write_session(tmp_path, "s2", [{"id": "x", "candidates": [str(a), str(b)]}])
    assert session.load(p).items[0].loudness_source == "board:lufs_m_max"   # b has no critic JSON
    (tmp_path / "hit-b-loud.json").write_text(json.dumps({"fixed": {"lufs_momentary_max": -20.0}}))
    it = session.load(p).items[0]
    assert it.loudness_source == "critic:lufs_momentary_max"
    g = {c.files[0].name: c.gains[0] for c in it.candidates}
    assert abs((g["hit-a.wav"] - g["hit-b-loud.wav"]) - 10.0) < 1e-6
    # a critic JSON for another file (sha256 mismatch) is ignored
    (tmp_path / "hit-b-loud.json").write_text(json.dumps({"sha256": "0" * 64, "lufs_momentary_max": -20.0}))
    assert session.load(p).items[0].loudness_source == "board:lufs_m_max"


def test_session_errors_are_vietnamese(tmp_path):
    p = write_session(tmp_path, "bad", [{"id": "x", "candidates": [str(tmp_path / "missing.wav")]}])
    with pytest.raises(session.SessionError, match="không thấy file"):
        session.load(p)
    p = write_session(tmp_path, "bad2", [{"id": "x", "contexts": ["mix2"], "candidates": []}])
    with pytest.raises(session.SessionError, match="ứng viên"):
        session.load(p)


# ---------------------------------------------------------------- HTTP API
def test_api_flow(server):
    st, cfg = call(server, "/api/config")
    assert st == 200 and len(cfg["tags"]) == 15 and cfg["tags"][0]["name"] == "hay"
    st, lst = call(server, "/api/sessions")
    assert st == 200 and lst["sessions"][0]["session"] == "s1" and lst["sessions"][0]["items"] == 3
    st, view = call(server, "/api/session/s1")
    assert st == 200 and view["resumeIndex"] == 0 and view["items"][0]["rating"] is None
    assert "hit-a" not in json.dumps(view)
    key = view["items"][0]["key"]
    s = server["board"].get("s1")
    names = label_map(view["items"][0], s, key)

    # audio by label only; bytes are the file's
    st, data = call(server, f"/api/audio/s1/{key}/A/0")
    assert st == 200 and data == (server["root"] / names["A"]).read_bytes()
    assert call(server, f"/api/audio/s1/{key}/Z/0")[0] == 404
    # nothing revealed before rating
    assert call(server, f"/api/reveal/s1/{key}")[0] == 403
    assert call(server, f"/api/card/s1/{key}/A")[0] == 403

    base = {"session": "s1", "item": key, "context": "loop", "device": "headphones"}
    st, err = call(server, "/api/rate", {**base, "stars": {"A": 4}})
    assert st == 400 and "còn thiếu sao" in err["error"]
    st, err = call(server, "/api/rate", {**base, "stars": {"A": 4, "B": 2, "C": 3}})
    assert st == 400 and "bản tốt nhất" in err["error"]
    st, err = call(server, "/api/rate", {**base, "stars": {"A": 4, "B": 2, "C": 3}, "pick": "A", "tags": {"B": ["không có"]}})
    assert st == 400
    st, err = call(server, "/api/rate", {**base, "stars": {"A": 4, "B": 9, "C": 3}, "pick": "A"})
    assert st == 400
    st, err = call(server, "/api/rate", {**base, "stars": {"A": 4, "B": 2, "C": 3}, "pick": "A", "device": "tv"})
    assert st == 400 and "thiết bị" in err["error"]
    body = {**base, "stars": {"A": 4, "B": 2, "C": 3}, "pick": "A", "pick_auto": True,
            "tags": {"B": ["yếu/mỏng", "chói"]}, "note": "A gọn", "listens": {"A": 2, "B": 1, "C": 1},
            "contexts_heard": ["alone", "loop"], "item_ms": 4200, "session_ms": 9000}
    st, res = call(server, "/api/rate", body)
    assert st == 200 and res["rev"] == 1 and len(res["reveal"]["candidates"]) == 3

    lines = (server["review"] / "_test" / "ratings.jsonl").read_text("utf-8").splitlines()
    assert len(lines) == 1
    ln = json.loads(lines[0])
    assert ln["schema"] == config.RATING_SCHEMA and ln["kind"] == "rating" and ln["id"] == "hit"
    assert ln["game"] == "_test" and ln["session"] == "s1" and ln["batch"] == "t1" and ln["device"] == "headphones"
    hash_of = dict(zip(ln["order"], ln["shown"]))
    assert ln["stars"] == {hash_of["A"]: 4, hash_of["B"]: 2, hash_of["C"]: 3}
    assert ln["pick"] == hash_of["A"] and ln["pick_auto"] is True and ln["none"] is False
    assert ln["tags"] == {hash_of["B"]: ["chói", "yếu/mỏng"]}             # fixed tag order
    assert sorted(ln["roles"].values()) == ["distinct", "probe", "top"] and ln["probe"] is True
    assert ln["roles"][ln["shown"][0]] == "top"                            # shown = session order
    assert ln["contexts_heard"] == ["alone", "loop"] and ln["context"] == "loop"
    assert ln["note"] == "A gọn" and ln["rev"] == 1 and ln["revealed_before"] is False
    assert all(len(h) == 64 for h in ln["shown"])
    assert ln["ts"][-6] in "+-"                                            # local time with offset
    files = {Path(v[0]).name for v in ln["files"].values()}
    assert files == {"hit-a.wav", "hit-b-loud.wav", "hit-c.wav"}

    assert call(server, f"/api/reveal/s1/{key}")[0] == 200
    st, view = call(server, "/api/session/s1")
    r = view["items"][0]["rating"]
    assert r["stars"] == {"A": 4, "B": 2, "C": 3} and r["pick"] == "A" and r["tags"] == {"B": ["chói", "yếu/mỏng"]}
    assert view["resumeIndex"] == 1 and view["rated"] == 1

    # re-rating appends a new line with rev 2
    st, res = call(server, "/api/rate", {**body, "pick": None, "none": True})
    assert st == 200 and res["rev"] == 2
    lines = (server["review"] / "_test" / "ratings.jsonl").read_text("utf-8").splitlines()
    assert len(lines) == 2 and json.loads(lines[1])["none"] is True and json.loads(lines[1])["revealed_before"] is True

    # single-candidate item: stars only; variants: drops without stars
    k2, k3 = view["items"][1]["key"], view["items"][2]["key"]
    assert call(server, "/api/rate", {**base, "item": k2, "context": "alone", "stars": {"A": 3}})[0] == 200
    st, res = call(server, "/api/rate", {**base, "item": k3, "dropped": ["B"]})
    assert st == 200
    last = json.loads((server["review"] / "_test" / "ratings.jsonl").read_text("utf-8").splitlines()[-1])
    assert last["mode"] == "variants" and last["dropped"] == [dict(zip(last["order"], last["shown"]))["B"]]

    # state: timer never goes back, device kept
    assert call(server, "/api/state", {"session": "s1", "elapsedMs": 50000, "device": "speakers", "index": 2})[0] == 200
    assert call(server, "/api/state", {"session": "s1", "elapsedMs": 1000})[0] == 200
    st, view = call(server, "/api/session/s1")
    assert view["state"]["elapsedMs"] == 50000 and view["state"]["device"] == "speakers"


def test_security_rules(server):
    assert call(server, "/api/health", headers={"Host": "evil.example:80"})[0] == 403
    assert call(server, "/api/state", {"session": "s1"}, headers={"Origin": "http://evil.example"})[0] == 403
    req = urllib.request.Request(server["url"] + "/api/state", data=b"session=s1", method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    with pytest.raises(urllib.error.HTTPError) as e:
        urllib.request.urlopen(req, timeout=5)
    assert e.value.code == 415
    for path in ("/static/../server.py", "/static/server.py", "/api/audio/s1/../../x/A/0", "/etc/passwd"):
        assert call(server, path)[0] in (403, 404)
    st, html = call(server, "/")
    assert st == 200 and b"/static/app.js" in html


def test_port_fallback_when_busy(lab):
    busy = socket.socket()
    busy.bind(("127.0.0.1", 0))
    busy.listen(1)
    free = socket.socket()
    free.bind(("127.0.0.1", 0))
    fallback = free.getsockname()[1]
    free.close()
    board = Board(lab["review"])
    try:
        httpd = make_server(board, "127.0.0.1", busy.getsockname()[1], fallback)
        assert httpd.used_fallback and board.port == fallback
        httpd.server_close()
    finally:
        busy.close()


def test_anchors_inserted_from_earlier_sessions(server):
    st, view = call(server, "/api/session/s1")
    key = view["items"][0]["key"]
    body = {"session": "s1", "item": key, "context": "alone", "device": "headphones",
            "stars": {"A": 5, "B": 1, "C": 3}, "pick": "A"}
    assert call(server, "/api/rate", body)[0] == 200
    root = server["root"]
    p2 = write_session(root, "s2", [{"id": "bell2", "candidates": [str(server["files"]["d"])]},
                                    {"id": "bell3", "candidates": [str(server["files"]["d"])]}], anchors=1)
    st, v2 = call(server, "/api/session/s2")
    assert st == 200, v2
    keys = [i["key"] for i in v2["items"]]
    assert "01-bell2" in keys and "02-bell3" in keys and len(keys) == 3          # regular keys unchanged
    anchor = next(i for i in v2["items"] if i["key"] not in ("01-bell2", "02-bell3"))
    akey = anchor["key"]
    assert anchor["id"] == "hit" and len(anchor["candidates"]) == 2 and anchor["mode"] == "hero"
    assert anchor["desc"] == "Trúng nhỏ"                                         # looks like any other item
    assert "anchor" not in json.dumps(anchor) and "mốc" not in json.dumps(anchor, ensure_ascii=False)
    s2 = server["board"].get("s2")
    names = sorted(c.files[0].name for c in s2.item(akey).candidates)
    s1 = server["board"].get("s1")
    lab_to_name = label_map(None, s1, key)
    assert names == sorted([lab_to_name["A"], lab_to_name["B"]])                # best and worst of the earlier rating
    state = json.loads((server["review"] / "_test" / "state" / "s2.json").read_text())
    assert state["anchors"][0]["item"]["anchor_of"]["session"] == "s1"
    st, res = call(server, "/api/rate", {"session": "s2", "item": akey, "context": "alone",
                                         "device": "headphones", "stars": {"A": 4, "B": 2}, "pick": "A"})
    assert st == 200
    last = json.loads((server["review"] / "_test" / "ratings.jsonl").read_text("utf-8").splitlines()[-1])
    assert last["anchor"] is True and last["anchor_of"]["item"] == key and last["mode"] == "hero"
    p2.touch()                                                                   # reload: same anchors
    st, v3 = call(server, "/api/session/s2")
    assert [i["key"] for i in v3["items"]] == keys


def test_calibration_sessions_build():
    from common import env
    from board import calib

    fx = env.FIXTURES / "poc40"
    if not (fx / "degraded").is_dir():
        pytest.skip("không có bộ âm thử poc40")
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        paths = calib.write_sessions(fx, Path(d), env.WORK)
        s1, s2 = (session.load(p) for p in paths)
        assert len(s1.items) == 8 and all(len(i.candidates) == 4 for i in s1.items)
        assert len(s2.items) == 8 and all(len(i.candidates) == 1 for i in s2.items)
        assert {c.role for i in s1.items for c in i.candidates} == {"good", "degraded:clipped", "degraded:muddy", "degraded:thin"}


def test_anchors_not_added_mid_session(server):
    """A session already rated without anchors never gets items inserted (resume point stays)."""
    st, view = call(server, "/api/session/s1")
    key = view["items"][0]["key"]
    assert call(server, "/api/rate", {"session": "s1", "item": key, "context": "alone", "device": "headphones",
                                      "stars": {"A": 5, "B": 1, "C": 3}, "pick": "A"})[0] == 200
    p2 = write_session(server["root"], "s2", [{"id": "bell2", "candidates": [str(server["files"]["d"])]}])
    s2 = server["board"].get("s2")                        # e.g. the server warm-up: no anchors chosen
    assert len(s2.items) == 1
    server["board"].store.append("_test", {"kind": "rating", "session": "s2", "item": "01-bell2", "mode": "hero"})
    st, v2 = call(server, "/api/session/s2")             # opened after it was rated: stays 1 item
    assert st == 200 and len(v2["items"]) == 1
    state = json.loads((server["review"] / "_test" / "state" / "s2.json").read_text())
    assert state["anchors"] == []
    p2.touch()
    assert len(call(server, "/api/session/s2")[1]["items"]) == 1


def test_critic_module_output(lab, tmp_path):
    """critic_dir + audiolab.critic.file/1 JSON: nested metrics, file.sha256, card name, flags, L1 checks."""
    a, b = lab["files"]["a"], lab["files"]["b"]
    out = tmp_path / "critic-out"
    out.mkdir()
    for f, lufs in ((a, -31.0), (b, -21.0)):
        (out / f"{f.stem}.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 32)
        doc = {"schema": "audiolab.critic.file/1", "file": {"name": f.name, "stem": f.stem, "sha256": loudness.sha256_file(f)},
               "verdict": "BLOCK", "score": {"total": 0.42},
               "metrics": {"duration_ms": 300.0, "lufs_m_max": lufs, "lufs_s_max": lufs - 8, "attack_ms": 1.5,
                           "crest_db": 9.1, "true_peak_dbtp": -3.0},
               "L1": {"checks": [{"id": "clip_full_scale", "label_vi": "Clip", "ok": False, "blocking": True},
                                 {"id": "tail", "label_vi": "Đuôi tắt hẳn", "ok": False, "blocking": False},
                                 {"id": "attack", "label_vi": "Thời gian lên", "ok": True}]},
               "flags": [{"layer": "L1b", "id": "hiss", "msg_vi": "có tiếng xì"}], "card": f"{f.stem}.png"}
        (out / f"{f.stem}.json").write_text(json.dumps(doc, ensure_ascii=False), "utf-8")
    p = write_session(tmp_path, "c1", [{"id": "x", "candidates": [str(a), str(b)]}], critic_dir=str(out))
    board = Board(tmp_path / "review", cache_path=tmp_path / "cache.json")
    it = board.get("c1").items[0]
    assert it.loudness_source == "critic:lufs_m_max"
    g = {c.files[0].name: c.gains[0] for c in it.candidates}
    assert abs((g["hit-a.wav"] - g["hit-b-loud.wav"]) - 10.0) < 1e-6
    assert all(c.cards[0] == out / f"{c.files[0].stem}.png" for c in it.candidates)
    board.store.append("_test", {"kind": "rating", "session": "c1", "item": it.key})
    rv = board.reveal("c1", it.key)
    rows = {m["label"]: m["value"] for m in rv["candidates"][0]["measures"]}
    assert rows["Lên"] == 1.5 and rows["Crest"] == 9.1 and rows["Dài"] == 300.0 and "Chỉnh" in rows
    flags = rv["candidates"][0]["flags"]
    assert flags == ["L1 chặn: Clip", "L1 sửa: Đuôi tắt hẳn"]          # no L1b/L4/L5 machine flags (§7)
    assert "0.42" not in json.dumps(rv) and "BLOCK" not in json.dumps(rv)       # no machine score or verdict
    # a stale critic JSON (another version of the file) is ignored, with its card
    doc = json.loads((out / "hit-a.json").read_text())
    doc["file"]["sha256"] = "0" * 64
    (out / "hit-a.json").write_text(json.dumps(doc))
    p.touch()
    it = board.get("c1").items[0]
    assert it.loudness_source == "board:lufs_m_max"
    stale = next(c for c in it.candidates if c.files[0].name == "hit-a.wav")
    assert stale.critics == [None] and stale.cards == [None]


def test_from_critic_listening_list(lab, tmp_path):
    """critic _batch.json "listen" -> session file: roles, critic JSON and card, gameplay rate, split by 10."""
    from board import from_critic

    out = tmp_path / "critic-run"
    out.mkdir()
    files, listen = [], {}
    for k in range(12):
        sid = f"hit{k:02d}"
        names = []
        for j in range(3):
            w = tone(tmp_path / f"{sid}-c{j}.wav", 300 + 40 * j + k, peak_db=-6 - 3 * j)
            png = out / f"{w.stem}.png"
            png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 16)
            doc = {"file": {"path": str(w), "name": w.name, "sha256": loudness.sha256_file(w)},
                   "spec": {"id": sid, "family": "trung", "group": "hit_heavy", "group_name_vi": "Trúng vừa, nặng",
                            "rate_hz": 2.0, "loop": False},
                   "metrics": {"lufs_m_max": -20.0 - 3 * j}, "card": png.name}
            (out / f"{w.stem}.json").write_text(json.dumps(doc, ensure_ascii=False), "utf-8")
            files.append({"name": w.name, "json": f"{w.stem}.json", "png": png.name})
            names.append(w.name)
        listen[f"id:{sid}"] = {"top": names[0], "distinct": names[1], "probe": names[2] if k % 3 == 0 else None}
    listen["id:blocked"] = {"top": None, "distinct": None, "probe": None}
    (out / "_batch.json").write_text(json.dumps({"listen": listen, "files": files}), "utf-8")
    review = tmp_path / "review"
    paths, skipped = from_critic.write_sessions([out], review, "_test", "b1", "s1")
    assert [p.name for p in paths] == ["s1-1.json", "s1-2.json"] and skipped == ["blocked: không bản nào qua cổng L1"]
    s = session.load(paths[0])
    assert len(s.items) == 10 and len(session.load(paths[1]).items) == 2
    it = s.items[0]
    assert it.id == "hit00" and it.probe and [c.role for c in it.candidates] == ["top", "distinct", "probe"]
    assert it.family == "trung" and it.desc == "Trúng vừa, nặng" and it.loudness_source == "critic:lufs_m_max"
    assert it.loop["interval_ms"] == 500 and it.loop["preset"] == "trung-nang" and not it.loop.get("seamless")
    assert all(c.cards[0] and c.cards[0].suffix == ".png" for c in it.candidates)
    assert not s.items[1].probe and len(s.items[1].candidates) == 2
    with pytest.raises(from_critic.FromCriticError, match="--force"):
        from_critic.write_sessions([out], review, "_test", "b1", "s1")
    assert from_critic.write_sessions([out], review, "_test", "b1", "s9", ids={"hit03"})[0][0].name == "s9.json"


def test_loop_presets_from_critic_groups():
    assert config.loop_params({"group": "key_ok"})["preset"] == "phim-dung"
    assert config.loop_params({"group": "hit_small"})["interval_ms"] == 250
    assert config.loop_params({"group": "unknown", "family": "ban"})["preset"] == "ban"
    assert config.loop_params({"group": "stinger", "family": "nen"})["cents"] == 0
