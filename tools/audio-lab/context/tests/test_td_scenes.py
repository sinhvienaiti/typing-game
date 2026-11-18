"""Lời Gọi scenarios on synthetic files: no voices recorded, no models, no library files."""
from __future__ import annotations

import json

import numpy as np
import pytest
import soundfile as sf

from context import mixer, td_scenes as T

SR = mixer.SR


def tone(path, f: float, dur: float, decay: float, level_db: float = -6.0, noise: float = 0.0, seed: int = 0):
    rng = np.random.default_rng(seed)
    t = np.arange(int(dur * SR)) / SR
    x = (np.sin(2 * np.pi * f * t) + noise * rng.standard_normal(t.size)) * np.exp(-t / decay) * 10 ** (level_db / 20)
    sf.write(str(path), x, SR, subtype="FLOAT")
    return path


@pytest.fixture(autouse=True)
def no_voices(monkeypatch):
    t = np.arange(int(0.4 * SR)) / SR
    word = np.sin(2 * np.pi * 1500 * t) * 0.05
    monkeypatch.setattr(T.voices, "load", lambda v, w: word)
    T._CACHE.clear()


def slots(tmp):
    notes = {n: tone(tmp / f"wh-{n}.wav", 220 * 2 ** (k / 5), 0.8, 0.12) for k, n in enumerate(T.SCALE)}
    return {"word-hit": notes, "word-hit-bell": tone(tmp / "bell.wav", 2093, 0.5, 0.08),
            "wordshot-fire": tone(tmp / "ws.wav", 900, 0.18, 0.04, noise=0.5, seed=1),
            "arrow-fire": tone(tmp / "ar.wav", 700, 0.09, 0.02, noise=0.3, seed=2),
            "ink-puff": tone(tmp / "ink.wav", 500, 0.15, 0.03, noise=1.0, seed=3),
            "blast": tone(tmp / "bl.wav", 90, 0.45, 0.12, noise=0.4, seed=4),
            "coin": tone(tmp / "coin.wav", 3136, 0.3, 0.05)}


def test_chain_plays_the_scale_in_order_with_words_shots_and_bells(tmp_path):
    sc, dur = T.build("td-wordhit-chain", slots(tmp_path))
    hits = [m["id"] for m in sc.marks if m["id"].startswith("word-hit ")]
    assert hits == [f"word-hit {n}" for n in T.SCALE[:-1]] + ["word-hit C5 (Chớp)"]
    assert len(sc.voices) == 7 and len(sc.played["wordshot-fire"]) == 7 and len(sc.played["word-hit-bell"]) == 2
    assert all(v.t_start - v.t_request == pytest.approx(0.15) for v in sc.voices)
    assert dur == pytest.approx(11.6)


def test_proposed_spacing_is_even_and_current_windows_drop_bursts(tmp_path):
    s = slots(tmp_path)
    cur, _ = T.build("td-wordhit-chain", s, "current")
    new, _ = T.build("td-wordhit-chain", s, "proposed")
    assert cur.asked["arrow-fire"] == new.asked["arrow-fire"]          # the same simulation for both
    for sid, gap in T.PROPOSED_GAP_S.items():
        if sid in new.played:
            t = sorted(new.played[sid])
            burst = T.PROPOSED_BURST.get(sid, 1)
            if burst == 1:
                d = np.diff(t)
                assert d.size == 0 or d.min() >= gap - 1e-6
            # a token bucket never lets more than burst + span / gap through in any span
            for i, a in enumerate(t):
                for j in range(i, len(t)):
                    assert j - i + 1 <= burst + (t[j] - a) / gap + 1e-6
    assert len(new.played["coin"]) <= len(new.asked["coin"])
    assert cur.asked["coin"] == new.asked["coin"]                      # coins drop by the simulation, not the sound
    for sid in ("ink-puff", "coin"):
        t = sorted(cur.played[sid])
        assert all(sum(1 for x in t if a - 1.0 < x <= a) <= T.CURRENT_CAPS[sid][0] for a in t)
    assert all(abs(t * 60 - round(t * 60)) < 1e-6 for t in cur.played["arrow-fire"])   # frames in the current game
    rep = T.caps_report("td-wordhit-chain", s, 0.15)
    assert rep["current"]["ink-puff"]["asked"] == rep["proposed"]["ink-puff"]["asked"]


def test_render_writes_files_and_the_same_candidate_gives_the_same_mix(tmp_path):
    s = slots(tmp_path)
    a = T.render("td-wordhit-chain", s, tmp_path / "a.wav", focus="word-hit", sweep=False, png=False)
    b = T.render("td-wordhit-chain", s, tmp_path / "b.wav", focus="word-hit", sweep=False, png=False)
    assert a["sha256"] == b["sha256"]
    m = a["metrics"]
    assert len(m["voice"]["per_word_db"]) == 7 and m["focus_plays"] == 7
    assert len(m["focus_band_decay"]["drop_db_at_100ms"]) == 7
    assert m["mix"]["true_peak_dbtp"] + T.SCENE_GAIN_DB < 0.0 and "caps" in m      # the written file does not clip
    doc = json.loads((tmp_path / "a.json").read_text("utf-8"))
    assert doc["scenario"] == "td-wordhit-chain" and doc["game"] == "typing-defense"


def test_night_leak_respects_its_gap_and_menu_has_no_voice(tmp_path):
    leak = tone(tmp_path / "leak.wav", 900, 1.2, 0.3)
    s = {**slots(tmp_path), "leak": leak, "call-chop": tone(tmp_path / "chop.wav", 180, 0.25, 0.05)}
    sc, _ = T.build("td-night", s)
    assert sc.played["leak"] == [3.4, 7.2] and len(sc.played["call-chop"]) == 2
    menu = {"ui-move": tone(tmp_path / "mv.wav", 1200, 0.04, 0.008), "ui-pick": tone(tmp_path / "pk.wav", 880, 0.6, 0.1)}
    doc = T.render("td-menu", menu, tmp_path / "m.wav", focus="ui-move", sweep=False, png=False)
    assert doc["metrics"]["focus_plays"] == 7 and "voice" not in doc["metrics"]


def test_flash_slide_bends_up_into_the_note():
    t = np.arange(int(0.3 * SR)) / SR
    x = np.sin(2 * np.pi * 1000 * t)
    y = T.slide_up(x)
    early = np.abs(np.fft.rfft(y[:2048] * np.hanning(2048)))
    late = np.abs(np.fft.rfft(y[-4096:] * np.hanning(4096)))
    f_early = np.argmax(early) * SR / 2048
    f_late = np.argmax(late) * SR / 4096
    assert f_early < 990 and abs(f_late - 1000) < 15
