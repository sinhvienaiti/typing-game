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
