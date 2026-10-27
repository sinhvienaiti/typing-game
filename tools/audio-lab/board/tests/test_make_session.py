"""`board make-session` (alias of from-critic) writes a session from a critic run, with --anchors."""
import json

import numpy as np
import soundfile as sf

from board import loudness, session
from board.__main__ import main


def test_make_session_alias_and_anchors(tmp_path):
    out = tmp_path / "critic-run"
    out.mkdir()
    files, names = [], []
    t = np.arange(4800) / 48000
    for j in range(3):
        w = tmp_path / f"gun.xung-v{j + 1}.wav"
        sf.write(str(w), 0.3 * np.sin(2 * np.pi * (200 + 50 * j) * t) * np.exp(-t / 0.03), 48000)
        doc = {"file": {"path": str(w), "name": w.name, "sha256": loudness.sha256_file(w)},
               "spec": {"id": "gun.xung", "family": "ban", "group": "shot_gun", "rate_hz": 5.0, "loop": False}}
        (out / f"{w.stem}.json").write_text(json.dumps(doc), "utf-8")
        files.append({"name": w.name, "json": f"{w.stem}.json"})
        names.append(w.name)
    listen = {"id:gun.xung": {"top": names[0], "distinct": names[2], "probe": names[1]}}
    (out / "_batch.json").write_text(json.dumps({"listen": listen, "files": files}), "utf-8")
    review = tmp_path / "review"
    rc = main(["make-session", str(out), "--game", "_test", "--batch", "0a", "--session", "s1",
               "--review-root", str(review), "--anchors", "0"])
    assert rc == 0
    path = review / "_test" / "sessions" / "s1.json"
    raw = json.loads(path.read_text("utf-8"))
    assert raw["anchors"] == 0 and raw["batch"] == "0a"
    s = session.load(path)
    assert [c.role for c in s.items[0].candidates] == ["top", "distinct", "probe"]
    assert s.items[0].probe and s.items[0].loop["interval_ms"] == 200


def test_candidate_note_is_shown_but_role_and_path_are_not(tmp_path):
    """A labelled contrast (batch 0b: the mõ-risk call-chop, rule-blocked howls) shows its note only."""
    t = np.arange(4800) / 48000
    files = []
    for j in range(2):
        w = tmp_path / f"call-chop__{'AB'[j]}__s1.wav"
        sf.write(str(w), 0.3 * np.sin(2 * np.pi * (300 + 200 * j) * t) * np.exp(-t / 0.03), 48000)
        files.append(w)
    raw = {"schema": "audiolab.board.session/1", "session": "s", "game": "_test", "batch": "0b", "seed": 3,
           "items": [{"id": "call-chop", "candidates": [
               {"file": str(files[0]), "role": "top"},
               {"file": str(files[1]), "role": "contrast-mo-risk", "note": "Đối chứng có chủ ý: tiếng tốc rỗng"}]}]}
    p = tmp_path / "s.json"
    p.write_text(json.dumps(raw, ensure_ascii=False), "utf-8")
    s = session.load(p)
    view = session.item_view(s.items[0])
    notes = {c["label"]: c.get("note") for c in view["candidates"]}
    assert sorted(v for v in notes.values() if v) == ["Đối chứng có chủ ý: tiếng tốc rỗng"]
    text = json.dumps(view, ensure_ascii=False)
    assert "contrast-mo-risk" not in text and "call-chop__B" not in text and "top" not in text
    raw["items"][0]["candidates"][1]["note"] = "x" * 81
    p.write_text(json.dumps(raw), "utf-8")
    try:
        session.load(p)
    except session.SessionError as exc:
        assert "note" in str(exc)
    else:
        raise AssertionError("a note over 80 characters must be refused")
