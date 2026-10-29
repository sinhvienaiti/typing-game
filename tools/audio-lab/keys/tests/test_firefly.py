"""Firefly survey (keys/firefly.py): onsets, press/release grouping, windows and per-stroke numbers on
synthetic signals only (no source take is read)."""
from __future__ import annotations

import hashlib
import json
import struct

import numpy as np
import pytest
import soundfile as sf

from keys import firefly as ff
from keys import pipeline, strokes

SR = 48000


def _press(n_ms: float = 60.0, level: float = 0.5, seed: int = 0, low_hz: float = 120.0, decay_ms: float = 8.0,
           click: bool = True) -> np.ndarray:
    """A synthetic bottom-out: a broadband click (first 2 ms) over a decaying low body."""
    n = int(n_ms / 1000 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    body = np.sin(2 * np.pi * low_hz * t) * np.exp(-t / (decay_ms / 1000))
    y = 0.7 * body
    if click:
        c = rng.standard_normal(n) * np.exp(-t / 0.0008)
        y = y + 0.6 * c
    return level * y / np.abs(y).max()


def _release(level: float, seed: int = 1) -> np.ndarray:
    """An upstroke: a short bright tick with no low body."""
    n = int(0.020 * SR)
    t = np.arange(n) / SR
    rng = np.random.default_rng(seed)
    y = rng.standard_normal(n) * np.exp(-t / 0.0015)
    return level * y / np.abs(y).max()


def _take(events: list[tuple[float, float, bool]], seconds: float = 3.0, noise_db: float | None = None) -> np.ndarray:
    """events: (time s, press level, with a release 90 ms later at -30 dB)."""
    x = np.zeros(int(seconds * SR))
    for k, (t, lv, rel) in enumerate(events):
        h = _press(level=lv, seed=k)
        a = int(t * SR)
        x[a:a + len(h)] += h[:len(x) - a]
        if rel:
            r = _release(lv * 10 ** (-30 / 20), seed=100 + k)
            b = a + int(0.090 * SR)
            x[b:b + len(r)] += r[:max(0, len(x) - b)]
    if noise_db is not None:
        x += 10 ** (noise_db / 20) * np.random.default_rng(9).standard_normal(len(x))
    return x


# ---------------------------------------------------------------- detection

def test_quieter_fast_presses_are_presses_not_releases():
    # strokes.find_strokes would swallow the 120 ms follower (6 dB quieter) as a release; the survey must not
    x = _take([(0.30, 0.5, True), (1.00, 0.5, True), (1.12, 0.25, False), (1.80, 0.5, True)])
    presses, comps, G = ff.detect(x)
    onsets = [round(p["onset"] / SR, 2) for p in presses]
    assert onsets == [0.30, 1.00, 1.12, 1.80]
    # the -30 dB upstroke 90 ms after an isolated press is its release, not a press
    p0 = presses[0]
    assert p0["release"] is not None and abs((p0["release"] - p0["onset"]) / SR - 0.090) < 0.003
    assert p0["clean"] and p0["stroke"] is not None and p0["stroke"].kind == "press+release"
    # the follower lands on the first one's release: no quiet before it, so it is measured but not clean
    assert not presses[2]["clean"] and presses[2]["why"].startswith("no quiet before")
    assert presses[2]["stroke"] is None
    assert presses[3]["clean"]


def test_window_ends_before_the_next_press_and_starts_1_ms_early():
    x = _take([(0.30, 0.5, True), (1.00, 0.5, True)])
    presses, _, _ = ff.detect(x)
    for i, p in enumerate(presses):
        assert p["a"] == p["onset"] - SR // 1000
        if i + 1 < len(presses):
            assert p["b"] < presses[i + 1]["onset"]


def test_single_keystroke_take_keeps_a_loud_release_with_its_press():
    x = np.zeros(SR)                                   # a 1 s take: press, loud upstroke 65 ms later
    h = _press(level=0.5)
    x[int(0.2 * SR):int(0.2 * SR) + len(h)] += h
    r = _release(0.4)
    x[int(0.265 * SR):int(0.265 * SR) + len(r)] += r
    presses, _, _ = ff.detect(x)
    assert len(presses) == 1
    assert presses[0]["release"] is not None


def test_a_stroke_cut_by_the_end_of_the_take_is_not_clean():
    x = _take([(0.30, 0.5, True), (1.0 - 0.025, 0.5, False)], seconds=1.0 + 3.5)[:int(1.0 * SR)]
    x = np.concatenate([np.zeros(SR * 3), x])        # long enough not to be a single-keystroke take
    presses, _, _ = ff.detect(x)
    assert presses[-1]["why"] == "cut by the end of the take"


def test_prepare_accepts_48k_stereo():
    x = np.column_stack([_take([(0.3, 0.5, True)], 1.0)] * 2)
    m, info = strokes.prepare(x, SR)
    assert m.ndim == 1 and len(m) == len(x) and info["stereo_corr"] == pytest.approx(1.0)


# ---------------------------------------------------------------- per-stroke numbers

def _features(x: np.ndarray, lr: np.ndarray | None = None) -> list[dict]:
    presses, _, _ = ff.detect(x)
    lr = np.column_stack([x, x]) if lr is None else lr
    out, prev = [], None
    for p in presses:
        out.append(ff.stroke_features(x, lr, p, prev))
        prev = p["end"]
    return out


def test_stroke_numbers_on_a_known_stroke():
    x = _take([(0.30, 0.5, True)], seconds=1.5)
    f = _features(x)[0]
    assert f["main_ms"] <= 2.0 and f["attack_ms"] <= 3.0
    assert f["kind"] == "press+release" and abs(f["release_gap_ms"] - 90) < 3
    assert -40 < f["release_rel_db"] < -20
    assert f["bands_db"]["b80_150"] > f["bands_db"]["b4k_8k"]       # a 120 Hz body under a short click
    assert 40 < f["len40_ms"] < 140
    assert f["stereo"]["corr"] == pytest.approx(1.0) and abs(f["stereo"]["mono_loss_db"]) < 0.01
    # digital silence around it: the floor once mastered is far under the -70 dBFS gate
    assert f["floor_at_master_dbfs"] is None or f["floor_at_master_dbfs"] < -100


def test_hiss_ratio_and_tail_hiss_rise_with_a_hiss_bed():
    clean = _features(_take([(0.30, 0.5, False)], 1.5))[0]
    hissy = _features(_take([(0.30, 0.5, False)], 1.5, noise_db=-45))[0]
    assert hissy["hiss_db"] > clean["hiss_db"] + 6
    assert hissy["hiss_tail_db"] > clean["hiss_tail_db"] + 10
    assert hissy["floor_at_master_dbfs"] > -100


def test_tail_slope_matches_a_known_exponential_decay():
    # a 300 Hz tone decaying 0.5 dB/ms (T60 = 120 ms) after a click
    n = int(0.4 * SR)
    t = np.arange(n) / SR
    y = np.sin(2 * np.pi * 300 * t) * 10 ** (-0.5 * t * 1000 / 20)
    y[:48] += np.random.default_rng(3).standard_normal(48) * 0.5
    x = np.zeros(2 * SR)
    x[int(0.5 * SR):int(0.5 * SR) + n] = 0.5 * y
    tl = ff.tail(x, int(0.5 * SR), int(0.5 * SR) + n, 0.0)
    assert tl["t60_ms"] == pytest.approx(120, rel=0.15)
    assert tl["late_db"] < -15


def test_ring_finds_a_sustained_tone():
    rng = np.random.default_rng(5)
    noise = rng.standard_normal(int(0.08 * SR)) * np.exp(-np.arange(int(0.08 * SR)) / SR / 0.02)
    t = np.arange(len(noise)) / SR
    from scipy import signal
    f0, P0 = signal.welch(noise, SR, nperseg=2048, nfft=16384)
    f1, P1 = signal.welch(noise + 0.3 * np.sin(2 * np.pi * 1100 * t), SR, nperseg=2048, nfft=16384)
    r0, _ = ff.ring(f0, P0)
    r1, hz = ff.ring(f1, P1)
    assert r1 > 15 and abs(hz - 1100) < 10
    assert r0 < r1 - 8


def test_low_edge_sees_a_brick_wall_low_block():
    # a press whose sustain is noise low-passed hard at 450 Hz (the Firefly fingerprint) against a plain decay
    from scipy import signal
    rng = np.random.default_rng(8)
    n = int(0.15 * SR)
    sus = signal.sosfilt(signal.butter(12, 450, "low", fs=SR, output="sos"), rng.standard_normal(n)) * 0.05
    x = np.zeros(2 * SR)
    a = int(0.4 * SR)
    h = _press(n_ms=200.0, level=0.5, low_hz=600.0, decay_ms=40.0)   # long enough to measure a sustain
    x[a:a + len(h)] += h
    plain = x.copy()
    x[a:a + n] += sus
    fb = _features(x)[0]
    fp = _features(plain)[0]
    assert fb["low_edge_db"] > fp["low_edge_db"] + 10
    assert fb["low_sustain_db"] > fp["low_sustain_db"] + 5


def test_stereo_numbers():
    x = np.random.default_rng(2).standard_normal(4800)
    same = ff.stereo(np.column_stack([x, x]))
    flip = ff.stereo(np.column_stack([x, -0.9 * x]))
    assert same["corr"] == pytest.approx(1.0) and abs(same["mono_loss_db"]) < 0.01
    assert flip["corr"] < -0.9 and flip["mono_loss_db"] > 15


def test_spacebar_flag_picks_the_lower_longer_heavier_stroke():
    def f(cen, length, low, pk):
        return {"centroid_hz": cen, "len40_ms": length, "bands_db": {"b80_150": low, "b150_400": low - 3},
                "peak_dbfs": pk}
    feats = [f(900 + 20 * i, 90 + i, -12 + 0.2 * i, -6 - 0.1 * i) for i in range(9)] + [f(300, 150, -4, -3)]
    ff.space_flags(feats)
    assert [g["space_like"] for g in feats] == [False] * 9 + [True]


# ---------------------------------------------------------------- per-take numbers

def test_take_numbers_count_presses_rhythm_floor_and_hard_cuts():
    x = _take([(0.2 + 0.4 * k, 0.5, True) for k in range(6)], seconds=3.0, noise_db=-80)
    x[int(2.85 * SR):] = 0.0                          # an edit that drops the bed to digital zero
    presses, comps, G = ff.detect(x)
    feats = _features(x)
    tk = ff.take_numbers(x, presses, comps, G, feats)
    assert tk["presses"] == 6 and tk["clean"] == 6
    assert tk["rhythm"]["ioi_median_ms"] == pytest.approx(400, abs=2) and tk["rhythm"]["ioi_cv"] < 0.02
    assert -90 < tk["gap"]["floor_dbfs"] < -75
    assert tk["hard_cuts_to_digital_zero"] == 1


def test_cleanliness_penalises_a_noisy_floor_and_hiss():
    base = {"gap": {"floor_at_master_dbfs": -90.0, "activity": 0.0}, "clip_samples": 0, "stray_events": 0,
            "presses": 20, "clean": 10}
    ms = {"floor_at_master_dbfs": -85.0, "hiss_db": -12.0, "hiss_tail_db": -30.0, "t60_ms": 60.0, "late_db": -40.0,
          "mono_loss_db": 0.2}
    good, _ = ff.cleanliness(base, ms)
    bad, pen = ff.cleanliness({**base, "gap": {"floor_at_master_dbfs": -60.0, "activity": 0.5}},
                              {**ms, "hiss_tail_db": -10.0, "t60_ms": 200.0})
    assert good == 10.0 and bad < 4.0 and pen["floor"] == 2.0 and pen["hiss"] == 2.0


# ---------------------------------------------------------------- names, provenance, CLI

def test_slug_and_file_id():
    assert ff.slug("Adobe_2026-10-29 (8) (1)") == "adobe-2026-10-29-8-1"
    assert ff.file_id("An edited Foley sequence of isol 111746 jTN.wav") == "111746-jTN"


def _wav_with_xmp(path, x):
    sf.write(str(path), x, SR, subtype="PCM_16")
    b = bytearray(path.read_bytes())
    xmp = b'<x:xmpmeta><rdf:Description dcterms:provenance="https://cai-manifests.adobe.com/manifests/urn-test"/></x:xmpmeta>'
    chunk = b"XMP " + struct.pack("<I", len(xmp)) + xmp + (b"\0" if len(xmp) & 1 else b"")
    b += chunk
    b[4:8] = struct.pack("<I", len(b) - 8)
    path.write_bytes(bytes(b))


def test_provenance_reads_the_c2pa_link_and_hash(tmp_path):
    p = tmp_path / "An edited Foley sequence of isol 1 abc.wav"
    _wav_with_xmp(p, np.zeros((480, 2)))
    pv = ff.provenance(p)
    assert pv["c2pa_manifest"].endswith("urn-test")
    assert pv["sha256"] == hashlib.sha256(p.read_bytes()).hexdigest()
    assert pv["chunks"][:2] == ["fmt ", "data"] and "XMP " in pv["chunks"]


def test_cli_survey_end_to_end_on_a_synthetic_folder(tmp_path, monkeypatch):
    src = tmp_path / "src" / "Adobe_2026-10-29"
    src.mkdir(parents=True)
    for k in range(2):
        ev = [(0.2 + 0.45 * i, 0.5 - 0.02 * i, True) for i in range(8)] + [(4.0, 0.6, True)]
        x = _take(ev, seconds=5.0)
        _wav_with_xmp(src / f"An edited Foley sequence of isol {k} t{k}x.wav", np.column_stack([x, 0.98 * x]))
    before = {p: p.read_bytes() for p in src.iterdir()}
    monkeypatch.setattr(ff, "CODEX_SETS", tmp_path / "no-codex")
    monkeypatch.setattr(ff, "SA3_SETS", tmp_path / "no-sa3")
    out = tmp_path / "out"
    assert pipeline.main(["firefly", "survey", "--src", str(src.parent), "--out", str(out)]) == 0
    feats = json.loads((out / "features.json").read_text())
    summ = json.loads((out / "summary.json").read_text())
    assert len(feats["files"]) == 2 and all(t["presses"] == 9 for t in feats["files"])
    fo = summ["folders"][0]
    assert fo["slug"] == "adobe-2026-10-29" and fo["clean"] >= 14
    assert (out / "sheets" / "adobe-2026-10-29.png").stat().st_size > 10000
    assert (out / "sheets" / "spectra-overlay.png").exists()
    idx = json.loads((out / "strokes" / "adobe-2026-10-29" / "index.json").read_text())
    assert idx["strokes"] and all((out / "strokes" / "adobe-2026-10-29" / r["file"]).exists() for r in idx["strokes"])
    info = sf.info(str(out / "strokes" / "adobe-2026-10-29" / idx["strokes"][0]["file"]))
    assert info.samplerate == SR and info.channels == 1 and info.subtype == "PCM_24"
    assert {p: p.read_bytes() for p in src.iterdir()} == before          # the source stays untouched
