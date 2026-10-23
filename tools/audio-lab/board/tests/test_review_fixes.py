"""Board rules added after the batch-0 review: stems, reveal at the end, WAV only, 100 ms loudness,
quiet-id note, sparse loop count, neutral calibration ids."""
from __future__ import annotations

import json
import threading
import urllib.request
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from board import config, from_critic, loudness, session
from board.server import Board, make_server

SR = 48000


def _gong(path: Path, peak_db: float) -> Path:
    t = np.arange(int(1.2 * SR)) / SR
    x = np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.6) * np.minimum(t / 0.06, 1)    # slow, dark bloom
    sf.write(str(path), x * 10 ** (peak_db / 20) / np.max(np.abs(x)), SR, subtype="PCM_24")
    return path


def _clang(path: Path, peak_db: float, fmt: str = "WAV") -> Path:
    t = np.arange(int(1.2 * SR)) / SR
    x = np.sin(2 * np.pi * 2400 * t) * np.exp(-t / 0.05)                               # bright, instant
    sub = "VORBIS" if fmt == "OGG" else "PCM_24"
    sf.write(str(path), x * 10 ** (peak_db / 20) / np.max(np.abs(x)), SR, format=fmt, subtype=sub)
    return path


def _session(root: Path, sid: str, items: list[dict], **extra) -> Path:
    p = root / "review" / "_test" / "sessions" / f"{sid}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"schema": config.SESSION_SCHEMA, "session": sid, "game": "_test", "batch": "t",
                             "seed": 3, "anchors": 0, "items": items, **extra}, ensure_ascii=False), "utf-8")
    return p


def test_100ms_spread_is_matched_and_recorded(tmp_path):
    a, b = _gong(tmp_path / "gong.wav", -6), _clang(tmp_path / "clang.wav", -6)
    s = session.load(_session(tmp_path, "s", [{"id": "leak", "candidates": [str(a), str(b)]}]))
    it = s.items[0]
    assert it.loudness_source.endswith("+100ms")
    m = [c.measures[0] for c in it.candidates]
    before = loudness.item_gains([{"measure": x, "critic": None} for x in m])[1]
    spread_before = abs((m[0]["lufs_100ms_max"] + before[0]) - (m[1]["lufs_100ms_max"] + before[1]))
    assert spread_before > loudness.SPREAD_MAX_DB
    assert it.loudness_spread_100ms_db < spread_before


def test_quiet_item_gets_a_note_and_sparse_items_loop_8_times(tmp_path):
    loud = _clang(tmp_path / "c1.wav", 0)
    click = np.zeros(int(0.3 * SR))
    click[100:104] = [0.5, 0.9, -0.7, 0.3]                       # a tick: the true-peak cap keeps it quiet
    sf.write(str(tmp_path / "c2.wav"), click, SR, subtype="PCM_24")
    s = session.load(_session(tmp_path, "q", [
        {"id": "ui-move", "candidates": [str(tmp_path / "c2.wav")]},
        {"id": "word-hit", "group": "reward", "candidates": [str(loud)], "loop": {"interval_ms": 1500}},
        {"id": "gun", "group": "shot_gun", "candidates": [str(loud)]}]))
    assert s.items[0].quiet_db > loudness.QUIET_NOTE_DB
    assert "nhỏ hơn mức chung" in session.item_view(s.items[0])["desc"]
    assert s.items[2].quiet_db <= loudness.QUIET_NOTE_DB and "mức chung" not in session.item_view(s.items[2])["desc"]
    assert s.items[1].loop["count"] == config.SPARSE_LOOP_COUNT
    assert s.items[2].loop["count"] == config.LOOP_COUNT


@pytest.fixture()
def srv(tmp_path):
    a = _gong(tmp_path / "orig.wav", -6)
    b = _clang(tmp_path / "orig2.ogg", -6, fmt="OGG")
    c = _clang(tmp_path / "copy.wav", -8)
    for f in (a, b, c):
        (tmp_path / f"{f.stem}.png").write_bytes(b"\x89PNG\r\n\x1a\n" + b"0" * 16)
    _session(tmp_path, "cal", [
        {"id": "calib-1", "source_id": "kenney_impactBell_heavy_000", "candidates": [str(a), str(b)]},
        {"id": "calib-2", "source_id": "syn_punchy_impact", "candidates": [str(c)]}], reveal="end")
    board = Board(tmp_path / "review", cache_path=tmp_path / "cache.json")
    httpd = make_server(board, "127.0.0.1", 0)
    th = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
    th.start()
    yield {"url": f"http://127.0.0.1:{board.port}", "board": board, "root": tmp_path}
    httpd.shutdown()
    httpd.server_close()


def _get(srv, path):
    try:
        with urllib.request.urlopen(srv["url"] + path, timeout=10) as r:
            return r.status, r.headers.get("Content-Type"), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type"), e.read()


def _post(srv, path, body):
    req = urllib.request.Request(srv["url"] + path, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())


def test_calibration_session_hides_source_and_reveals_at_the_end(srv):
    st, _, raw = _get(srv, "/api/session/cal")
    view = json.loads(raw)
    assert view["revealAt"] == "end" and [i["id"] for i in view["items"]] == ["calib-1", "calib-2"]
    assert "kenney" not in raw.decode() and "syn_" not in raw.decode()
    k1, k2 = (i["key"] for i in view["items"])
    for lab in ("A", "B"):                                   # OGG original and WAV copy look the same
        st, ctype, body = _get(srv, f"/api/audio/cal/{k1}/{lab}/0")
        assert st == 200 and ctype == "audio/wav" and body[:4] == b"RIFF"
    r = _post(srv, "/api/rate", {"session": "cal", "item": k1, "context": "alone", "device": "speakers",
                                 "stars": {"A": 4, "B": 2}, "pick": "A"})
    assert r["reveal"] is None and r["revealAt"] == "end"
    assert _get(srv, f"/api/reveal/cal/{k1}")[0] == 403 and _get(srv, f"/api/card/cal/{k1}/A")[0] == 403
    r = _post(srv, "/api/rate", {"session": "cal", "item": k2, "context": "alone", "device": "speakers",
                                 "stars": {"A": 3}})
    assert r["reveal"] is not None                           # last id rated: everything opens
    assert _get(srv, f"/api/reveal/cal/{k1}")[0] == 200
    lines = [json.loads(x) for x in (srv["root"] / "review" / "_test" / "ratings.jsonl").read_text("utf-8").splitlines()]
    assert lines[0]["id"] == "calib-1" and lines[0]["source_id"] == "kenney_impactBell_heavy_000"
    assert lines[0]["reveal_at"] == "end" and "loudness_spread_100ms_db" in lines[0]


def test_listening_entries_resolve_by_stem_and_refuse_ambiguous_names(tmp_path):
    out = tmp_path / "run"
    out.mkdir()
    files = []
    for sub in ("r1", "r2"):
        w = _clang(tmp_path / sub / "gun.xung-v1.wav", -6) if (tmp_path / sub).mkdir() is None else None
        stem = "gun.xung-v1" if sub == "r1" else "gun.xung-v1__2"
        doc = {"file": {"path": str(w), "name": w.name, "stem": stem, "sha256": loudness.sha256_file(w)},
               "spec": {"id": "gun.xung", "family": "ban", "group": "shot_gun", "rate_hz": 5.0}}
        (out / f"{stem}.json").write_text(json.dumps(doc), "utf-8")
        files.append({"name": w.name, "stem": stem, "json": f"{stem}.json"})
    (out / "_batch.json").write_text(json.dumps({"listen": {"id:gun.xung": {"top": "gun.xung-v1__2",
                                                                              "distinct": "gun.xung-v1"}},
                                                 "files": files}), "utf-8")
    items, _ = from_critic.items_from_run(out)
    assert [c["file"].split("/")[-2] for c in items[0]["candidates"]] == ["r2", "r1"]
    (out / "_batch.json").write_text(json.dumps({"listen": {"id:gun.xung": {"top": "gun.xung-v1.wav"}},
                                                 "files": [{k: v for k, v in f.items() if k != "stem"} | {"json": None}
                                                           for f in files]}), "utf-8")
    with pytest.raises(from_critic.FromCriticError, match="trùng"):
        from_critic.items_from_run(out)
