"""Tuyến Cuối scenarios ("Liên thanh 3 s") on synthetic files: no voices recorded, no models, no library files."""
from __future__ import annotations

import numpy as np
import pytest
import soundfile as sf

from context import mixer, ts_scenes as T

SR = mixer.SR


def shot(path, tail_s: float, seed: int, level_db: float = -6.0):
    """A crack and a low body that decays to -60 dB over tail_s."""
    rng = np.random.default_rng(seed)
    n = int((tail_s + 0.01) * SR)
    t = np.arange(n) / SR
    crack = rng.standard_normal(n) * np.exp(-t / 0.004)
    body = np.sin(2 * np.pi * 220 * t) * np.exp(-6.9 * t / tail_s)
    x = (0.6 * crack + body) * 10 ** (level_db / 20)
    sf.write(str(path), x, SR, subtype="FLOAT")
    return path


@pytest.fixture(autouse=True)
def no_voices(monkeypatch):
    t = np.arange(int(0.4 * SR)) / SR
    word = np.sin(2 * np.pi * 1500 * t) * 0.05
    monkeypatch.setattr(T.voices, "load", lambda v, w: word)
    T._CACHE.clear()


def test_short_rounds_on_even_frames_leave_holes_and_long_tails_fill_them(tmp_path):
    short = [shot(tmp_path / f"s{k}.wav", 0.05, k) for k in range(2)]
    longs = {"A": [shot(tmp_path / f"a{k}.wav", 0.35, 10 + k) for k in range(3)],
             "B": [shot(tmp_path / f"b{k}.wav", 0.35, 20 + k, -11) for k in range(3)]}
    sc, dur = T.build("ts-xung-3s", {"gun.xung": short[:1]}, "current")
    cur = T.burst_numbers(T.render_mix(sc, dur), sc)
    sc2, _ = T.build("ts-xung-3s", {"gun.xung": longs}, "proposed")
    new = T.burst_numbers(T.render_mix(sc2, dur), sc2)
    assert len(sc.rounds) == 15 and len(sc2.rounds) == 30            # even rounds only vs every round
    assert cur["gap_time_pct"] > 50 > 10 > new["gap_time_pct"]
    assert new["onset_interval_ms"] == pytest.approx(100, abs=2)
    assert all(abs(t * 60 - round(t * 60)) < 1e-6 for t in sc.rounds)  # the current game starts sounds on frames


def test_proposed_playback_caps_gun_voices_and_never_repeats_a_take(tmp_path):
    sets = {"A": [shot(tmp_path / f"a{k}.wav", 0.9, k) for k in range(4)],
            "B": [shot(tmp_path / f"b{k}.wav", 0.9, 9 + k) for k in range(4)]}
    sc, _ = T.build("ts-xung-3s", {"gun.xung": sets}, "proposed")
    guns = sorted([e for e in sc.events if e.gun], key=lambda e: e.t)
    for e in guns:                    # once the stolen voice's 25 ms fade is over
        at = e.t + T.STEAL_FADE_S + 0.001
        playing = [g for g in guns if g.t <= at < g.t + g.audio.size / SR]
        assert len(playing) <= T.MAX_GUN_VOICES
    assert all(a != b for a, b in zip(sc.played, sc.played[1:]))
    labels = [m["id"] for m in sc.marks if m["id"].startswith("gun.xung.")]
    assert labels[:4] == ["gun.xung.A", "gun.xung.B", "gun.xung.A", "gun.xung.B"]


def test_bed_and_tail_only_in_the_proposed_playback(tmp_path):
    rng = np.random.default_rng(3)
    bed = tmp_path / "bed.wav"
    sf.write(str(bed), rng.standard_normal(int(2.5 * SR)) * 0.05, SR, subtype="FLOAT")
    tail = shot(tmp_path / "tail.wav", 0.6, 5)
    slots = {"gun.xung": {"A": [shot(tmp_path / "a.wav", 0.3, 1)], "B": [shot(tmp_path / "b.wav", 0.3, 2)]},
             "gun.xung.loop": [bed], "gun.xung.tail": [tail]}
    cur, _ = T.build("ts-xung-3s", slots, "current")
    new, _ = T.build("ts-xung-3s", slots, "proposed", bed_db=11.0)
    assert {e.slot for e in cur.events} == {"gun.xung"}
    assert {"gun.xung.loop", "gun.xung.tail"} <= {e.slot for e in new.events}
    tail_ev = next(e for e in new.events if e.slot == "gun.xung.tail")
    assert tail_ev.t == pytest.approx(3.05)


def test_ceasefire_cut_counts_only_above_minus_60_db(tmp_path):
    """A tail that ends in digital silence far under the firing level is not a cut; a hard stop at full level is."""
    sets = {"A": [shot(tmp_path / f"a{k}.wav", 0.35, k) for k in range(2)],
            "B": [shot(tmp_path / f"b{k}.wav", 0.35, 5 + k, -11) for k in range(2)]}
    soft = shot(tmp_path / "soft.wav", 0.7, 7)
    sc, dur = T.build("ts-xung-3s", {"gun.xung": sets, "gun.xung.tail": [soft]}, "proposed")
    ok = T.burst_numbers(T.render_mix(sc, dur), sc)
    assert ok["stop_max_drop_10ms_db"] <= 6.0 and ok["stop_pass"]
    rng = np.random.default_rng(1)
    hard = tmp_path / "hard.wav"
    sf.write(str(hard), rng.standard_normal(int(0.3 * SR)) * 0.3, SR, subtype="FLOAT")   # full level, then nothing
    sc2, _ = T.build("ts-xung-3s", {"gun.xung": sets, "gun.xung.tail": [hard]}, "proposed")
    cut = T.burst_numbers(T.render_mix(sc2, dur), sc2)
    assert cut["stop_max_drop_10ms_db"] > 20.0 and not cut["stop_pass"]
