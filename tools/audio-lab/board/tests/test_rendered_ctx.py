"""Rendered contexts (scene, burst): a file made beforehand for each candidate (BATCH1_BRIEF §3.5)."""
from __future__ import annotations

import json
import threading
import urllib.error
import urllib.request

import pytest

from board import config, session
from board.server import Board, make_server
from board.tests.test_server import tone, write_session


def _get(url):
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return r.status, r.read(), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return e.code, e.read(), ""


@pytest.fixture()
def srv(tmp_path):
    a, b = tone(tmp_path / "a.wav", 300), tone(tmp_path / "b.wav", 500)
    sa, sb = tone(tmp_path / "scene-a.wav", 300, dur=1.0), tone(tmp_path / "scene-b.wav", 500, dur=1.0)
    c = tone(tmp_path / "c.wav", 700)
    items = [
        {"id": "fire.cast", "family": "thuong", "contexts": ["scene", "loop", "alone"],
         "candidates": [{"file": str(a), "ctx": {"scene": str(sa)}}, {"file": str(b), "ctx": {"scene": str(sb)}}]},
        # one candidate without a render: the item may not offer the context
        {"id": "fire.impact.a", "family": "trung", "contexts": ["scene", "loop"],
         "candidates": [{"file": str(c), "ctx": {"scene": str(sa)}}, {"file": str(b)}]},
    ]
    path = write_session(tmp_path, "r1", items)
    board = Board(tmp_path / "review", cache_path=tmp_path / "cache.json")
    httpd = make_server(board, "127.0.0.1", 0)
    th = threading.Thread(target=httpd.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True)
    th.start()
    yield {"url": f"http://127.0.0.1:{board.port}", "board": board, "path": path}
    httpd.shutdown()
    httpd.server_close()


def test_rendered_context_needs_a_file_for_every_candidate(srv):
    s = session.load(srv["path"])
    first, second = s.items
    assert first.rendered == ["scene"] and first.contexts[0] == "scene"
    assert second.rendered == [] and "scene" not in second.contexts
    view = session.item_view(first)
    assert view["rendered"] == ["scene"]
    assert "ctx" not in json.dumps(view["candidates"])          # no path or role reaches the page


def test_ctx_route_serves_the_render_and_rejects_others(srv):
    s = session.load(srv["path"])
    it = s.items[0]
    lab = it.candidates[0].label
    st, body, ctype = _get(f"{srv['url']}/api/ctx/r1/{it.key}/{lab}/scene")
    assert st == 200 and ctype == "audio/wav" and body[:4] == b"RIFF"
    assert _get(f"{srv['url']}/api/ctx/r1/{it.key}/{lab}/burst")[0] == 404
    other = s.items[1]
    assert _get(f"{srv['url']}/api/ctx/r1/{other.key}/{other.candidates[0].label}/scene")[0] == 404


def test_bad_ctx_key_is_a_session_error(tmp_path):
    a = tone(tmp_path / "a.wav")
    p = write_session(tmp_path, "r2", [{"id": "x", "candidates": [{"file": str(a), "ctx": {"loop": str(a)}}]}])
    with pytest.raises(session.SessionError):
        session.load(p)


def test_rating_keeps_the_scene_context_and_its_files(srv):
    s = session.load(srv["path"])
    it = s.items[0]
    labels = sorted(c.label for c in it.candidates)
    body = {"session": "r1", "item": it.key, "stars": {labels[0]: 4, labels[1]: 2}, "pick": labels[0],
            "context": "scene", "contexts_heard": ["scene", "alone"], "device": "headphones"}
    req = urllib.request.Request(srv["url"] + "/api/rate", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        assert r.status == 200
    line = srv["board"].store.latest("_test", "r1")[it.key]
    assert line["context"] == "scene" and set(line["contexts_heard"]) == {"scene", "alone"}
    assert all("scene" in v for v in line["ctx_files"].values())
    assert "ngắt quãng" in config.TAG_NAMES
