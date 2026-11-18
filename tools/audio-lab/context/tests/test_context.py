"""Context mixer and metrics on synthetic signals (no voices, no models, no files from the libraries)."""
from __future__ import annotations

import numpy as np

from context import metrics, mixer

SR = mixer.SR


def burst(dur=0.3, f=2000.0, level_db=-12.0, decay=0.05):
    t = np.arange(int(dur * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t / decay) * 10 ** (level_db / 20)


def test_pan_is_equal_power_like_web_audio():
    x = np.ones(100)
    c = mixer.pan(x, 0.0)
    assert np.allclose(c[:, 0], np.cos(np.pi / 4)) and np.allclose(c[:, 1], np.sin(np.pi / 4))
    hard = mixer.pan(x, 1.0)
    assert np.allclose(hard[:, 0], 0, atol=1e-12) and np.allclose(hard[:, 1], 1)
    st = mixer.pan(np.ones((10, 2)), 0.0)
    assert np.allclose(st, 1.0)                    # a centred stereo source passes unchanged


def test_target_curve_follows_set_target_at_time():
    n = SR
    c = mixer.target_curve(n, [(0.1, 0.5, 0.08 / 3)], start=1.0)
    assert c[int(0.09 * SR)] == 1.0
    assert abs(c[int((0.1 + 0.08) * SR)] - (0.5 + 0.5 * np.exp(-3))) < 1e-3


def test_compressor_holds_peaks_near_threshold():
    x = np.stack([burst(0.5, 200, 0.0, 0.3)] * 2, axis=1)       # 0 dBFS peaks
    y, gr = mixer.compressor(x, -3.0, 20.0, 0.002, 0.12, makeup=False)
    assert gr.min() < -2.0
    assert 20 * np.log10(np.abs(y[int(0.01 * SR):]).max()) < -1.5


def test_forest_impulse_matches_game_shape():
    ir = mixer.forest_impulse(0.9)
    assert ir.shape == (int(0.9 * SR), 2)
    head = np.abs(ir[: int(0.1 * SR)]).mean()
    tail = np.abs(ir[-int(0.1 * SR):]).mean()
    assert 20 * np.log10(tail / head) < -40


def test_duck_from_request_dips_earlier_than_from_voice():
    sfx = np.stack([burst(1.0, 2500, -10, 0.5)] * 2, axis=1)
    voice = burst(0.4, 1500, -10, 1.0)
    ev = [mixer.Event(t=0.0, audio=sfx, bus="world")]
    vs = [mixer.Voice(t_request=0.1, t_start=0.25, audio=voice)]
    a = mixer.render(ev, vs, 1.2, duck_from="request")
    b = mixer.render(ev, vs, 1.2, duck_from="voice")
    assert a["duck"]["world"][int(0.2 * SR)] < 0.8 < b["duck"]["world"][int(0.2 * SR)]
    va = metrics.voice_clarity(a["game"], a["voice"], [0.25])
    vb = metrics.voice_clarity(b["game"], b["voice"], [0.25])
    assert va["min_db"] > vb["min_db"]


def test_band_decay_rule():
    fast = burst(0.4, 2000, -6, 0.01)          # 1-4 kHz gone within 100 ms
    slow = burst(0.4, 2000, -6, 0.3)
    assert metrics.band_decay(fast)["pass_15db"] and not metrics.band_decay(slow)["pass_15db"]


def test_cast_chain_adds_impact_multi_only_when_its_slot_is_filled(tmp_path, monkeypatch):
    import soundfile as sf

    from context import scenes

    monkeypatch.setattr(scenes.voices, "load", lambda v, w: burst(0.4, 1500, -20, 1.0))
    scenes._CACHE.clear()
    files = {}
    for k, sid in enumerate(("fire.cast", "fire.impact.a", "fire.impact.b", "fire.impact.c", "impact.multi")):
        p = tmp_path / f"{sid}.wav"
        sf.write(str(p), burst(0.7, 300 + 100 * k, -12, 0.2), SR, subtype="FLOAT")
        files[sid] = p
    without = {k: v for k, v in files.items() if k != "impact.multi"}
    b0, _ = scenes.build("dh-cast-chain", without)
    b1, _ = scenes.build("dh-cast-chain", files)
    multi = [m for m in b1.marks if m["id"] == "impact.multi"]
    assert not [m for m in b0.marks if m["id"] == "impact.multi"]
    assert [m["t"] for m in multi] == [round(0.5 + 1.5 * 1 + 0.6, 3), round(0.5 + 1.5 * 4 + 0.6, 3)]
    # map-events.ts:175 gain for 3 and 4 foes, +-1 dB of level spread
    assert abs(multi[0]["db"] - scenes.multi_gain_db(3)) <= 1.0 and abs(multi[1]["db"] - scenes.multi_gain_db(4)) <= 1.0
    assert scenes.multi_gain_db(3) < scenes.multi_gain_db(4) < 0.0
    # the other sounds keep their times
    assert [(m["t"], m["id"]) for m in b0.marks] == [(m["t"], m["id"]) for m in b1.marks if m["id"] != "impact.multi"]
