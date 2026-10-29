"""Keyboard profiles: stroke slicing, phrase timing, family numbers, the kit's manifest reader (numpy audio only)."""
from __future__ import annotations

import numpy as np

from keys import family, phrases, pipeline, strokes

SR = 48000


def _hit(n_ms: float, f: float, level: float, decay_ms: float, seed: int) -> np.ndarray:
    n = int(n_ms / 1000 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    return level * np.exp(-t / (decay_ms / 1000)) * (0.6 * np.sin(2 * np.pi * f * t) + 0.4 * rng.standard_normal(n))


def _take(events: list[tuple[float, float]], seconds: float = 2.0) -> np.ndarray:
    """events: (time s, level) -> a mono take at 48 kHz with a press (level) and its release (-10 dB) 90 ms later."""
    x = np.zeros(int(seconds * SR))
    for k, (t, lv) in enumerate(events):
        for dt, g, f in ((0.0, lv, 900.0), (0.090, lv * 0.32, 1500.0)):
            h = _hit(60, f, g, 8, k * 7 + int(dt * 1000))
            a = int((t + dt) * SR)
            x[a:a + len(h)] += h
    return x


def test_press_and_release_make_one_stroke_and_a_crowded_key_is_skipped():
    x = _take([(0.20, 0.5), (0.80, 0.45), (1.30, 0.5), (1.36, 0.5)])
    st, skipped = strokes.find_strokes(x, "t", "key")
    assert [round(s.onset / SR, 2) for s in st] == [0.2, 0.8]
    assert all(s.kind == "press+release" for s in st)
    assert sum("không rõ nhả phím" in k["why"] for k in skipped) == 2


def test_render_starts_inside_2_ms_and_fits_the_cap():
    x = _take([(0.30, 0.5)])
    st, _ = strokes.find_strokes(x, "t", "key")
    y, info = strokes.render(x, st[0], "key")
    assert y is not None and info["pre_roll_ms"] <= 1.0
    assert len(y) <= strokes.CAP_MS["key"] / 1000 * SR
    head = np.flatnonzero(np.abs(y) > np.abs(y).max() * 10 ** (-40 / 20))[0] / SR * 1000
    assert head <= 2.0


def test_a_long_hold_is_shortened_in_its_silence():
    x = np.zeros(SR)
    for dt, g, f in ((0.0, 0.5, 900.0), (0.170, 0.16, 1500.0)):
        h = _hit(50, f, g, 6, int(dt * 1000))
        a = int((0.2 + dt) * SR)
        x[a:a + len(h)] += h
    st, _ = strokes.find_strokes(x, "t", "key")
    y, info = strokes.render(x, st[0], "key")
    assert y is not None and info["tightened_ms"] > 0 and len(y) <= 0.180 * SR


def test_picker_never_repeats_and_timing_follows_wpm():
    p = phrases.Picker(10, np.random.default_rng(1))
    seq = [p.next() for _ in range(200)]
    assert all(a != b for a, b in zip(seq, seq[1:]))
    assert sorted(seq[:10]) == list(range(10))
    ev = phrases.schedule("a" * 400, 60, seed=3)
    gaps = np.diff([t for t, _ in ev])
    assert abs(np.mean(gaps) - 0.2) < 0.02


def test_family_numbers_and_fit():
    y = _hit(120, 900, 0.5, 10, 1)
    f = family.features(y)
    assert f["t_main_ms"] < 5 and f["attack_ms"] < 5
    st = family.family_stats([f, f])
    assert st["mel_dist_mean"] == 0.0
    score, parts = family.fit_score(f, {"centroid_hz": {"good": [0, 1e5], "bad": [0, 1e5]}})
    assert score == 1.0 and parts["centroid_hz"] == 1.0
    assert family.trap(5, (10, 20), (0, 30)) == 0.5


def test_kit_reader_sees_only_the_runtime_files():
    man = {"files": [{"file": "key-02.ogg"}, {"file": "key-01.ogg"}, {"file": "space-01.ogg"}],
           "format": {"master": "WAV 48 kHz (_art-src/x/masters/<name>.wav)"},
           "other": ["../x/key-03.ogg", "/abs/key-04.ogg", "https://h/key-05.ogg"]}
    assert pipeline.kit_files(man) == {"key": ["key-01.ogg", "key-02.ogg"], "space": ["space-01.ogg"]}
