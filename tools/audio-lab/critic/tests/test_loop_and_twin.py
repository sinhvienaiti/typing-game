"""Batch 0b review additions: long-term loop spectrum, loop signature, decoder comb, near-mono beds,
loop-aware "most different" choice, and raw clip checks that read a generator's float copy."""
from __future__ import annotations

import json

import numpy as np
import soundfile as sf
import yaml

from critic import loopcheck, pipeline, score

SR = 48000


def bed(seconds: float = 6.0, seed: int = 0, stereo: bool = True) -> np.ndarray:
    from scipy import signal
    rng = np.random.default_rng(seed)
    n = int(seconds * SR)
    x = rng.standard_normal((n, 2 if stereo else 1)) * 0.1
    x = signal.sosfilt(signal.butter(1, 4000, "low", fs=SR, output="sos"), x, axis=0)
    if stereo:
        x[:, 1] = 0.6 * x[:, 0] + 0.8 * x[:, 1]
    return x


def test_clean_bed_has_no_signature_and_a_long_term_spectrum():
    x = bed()
    sig = loopcheck.signature(x, SR)
    assert sig["applies"] and sig["knocks"] == 0 and sig["chirps"] == 0
    m, ctx = loopcheck.summary(x, SR)
    assert 0 <= m["ltas_share_4k_10k"] <= 1 and m["ltas_tilt_db_oct"] is not None and len(m["third_octaves"]) > 20
    assert ctx["ltas"]["p10"].shape == ctx["ltas"]["psd"].shape


def test_knock_and_chirp_are_found_at_their_times():
    x = bed()
    k = int(2.0 * SR)
    x[k:k + int(0.012 * SR)] += 0.8 * np.random.default_rng(1).standard_normal((int(0.012 * SR), 1))
    c = int(4.0 * SR)
    t = np.arange(int(0.12 * SR)) / SR
    x[c:c + len(t)] += (0.25 * np.sin(2 * np.pi * (3500 + 2000 * t) * t) * np.hanning(len(t)))[:, None]
    sig = loopcheck.signature(x, SR)
    kinds = {(e["kind"], round(e["t"])) for e in sig["events"]}
    assert ("knock", 2) in kinds and ("chirp", 4) in kinds


def test_knock_at_the_seam_counts():
    x = bed()
    x[-int(0.006 * SR):] += 0.8
    x[:int(0.006 * SR)] += 0.8
    assert loopcheck.signature(x, SR, loop=True)["knocks"] >= 1


def test_comb_lines_are_measured():
    x = bed(4.0)
    t = np.arange(x.shape[0]) / SR
    noisy = x + sum(0.003 * np.sin(2 * np.pi * k * loopcheck.COMB_F0 * t + k) for k in range(60, 125))[:, None]
    from scipy import signal
    f, p = signal.welch(noisy.mean(axis=1), SR, nperseg=8192)
    f0, p0 = signal.welch(x.mean(axis=1), SR, nperseg=8192)
    assert loopcheck.comb(f, p)["median_prom_db"] >= 6
    assert loopcheck.comb(f0, p0)["median_prom_db"] < 3


def _card(tmp, sid="amb.test", stereo=True, loop=True):
    c = {"id": sid, "game": "dragon-hold", "critic": {"group": "ambience", "loop": loop, "stereo": stereo,
                                                      "head_max_ms": None, "attack_max_ms": None,
                                                      "duration_ms": {"target_ms": 6000, "tolerance_pct": 20}}}
    p = tmp / f"{sid}.yaml"
    p.write_text(yaml.safe_dump(c), "utf-8")
    return p


def test_bed_flags_and_card_panel(tmp_path):
    from build import dsp
    ind = tmp_path / "in"
    ind.mkdir()
    x = bed(6.5)
    k = int(3.0 * SR)
    x[k:k + int(0.01 * SR)] += 0.9
    loop = dsp.loop_crossfade(x, 500, SR)
    sf.write(str(ind / "amb.test__A__s1.wav"), loop, SR, subtype="PCM_24")
    sf.write(str(ind / "amb.test__B__s1.wav"), np.repeat(dsp.loop_crossfade(bed(6.5, 4), 500, SR)[:, :1], 2, axis=1),
             SR, subtype="PCM_24")
    out = tmp_path / "out"
    pipeline.run([str(ind)], spec_path=str(_card(tmp_path)), out_dir=out,
                 opts=pipeline.Options(layers=("L1", "L1b", "L2", "L6"), quiet=True))
    a = json.loads((out / "amb.test__A__s1.json").read_text())
    b = json.loads((out / "amb.test__B__s1.json").read_text())
    ids_a = {f["id"] for f in a["flags"]}
    ids_b = {f["id"] for f in b["flags"]}
    assert "loop_signature" in ids_a and "near_mono" not in ids_a
    assert "near_mono" in ids_b and "loop_signature" not in ids_b
    assert a["metrics"]["loop_spectrum"]["comb_median_prom_db"] is not None
    assert (out / a["card"]).is_file()


def test_most_different_loop_uses_loop_features():
    loop = {"spec": {"loop": True}, "metrics": {"centroid_hz": 900.0, "stereo_correlation": 0.4, "attack_ms": 2.0}}
    hit = {"spec": {"loop": False}, "metrics": {"centroid_hz": 900.0, "attack_ms": 2.0}}
    assert len(score._vec(loop)) == len(score.LOOP_DIST_FEATURES)
    assert len(score._vec(hit)) == len(score.DIST_FEATURES)


def test_raw_clip_checks_read_the_float_copy(tmp_path):
    ind = tmp_path / "raw"
    ind.mkdir()
    t = np.arange(SR) / SR
    x = 1.3 * np.sin(2 * np.pi * 300 * t) * np.exp(-t / 0.08)
    st = np.stack([x, x], axis=1)
    sf.write(str(ind / "hit.test__A__s1.wav"), np.clip(st, -1, 1), SR, subtype="PCM_16")
    sf.write(str(ind / "hit.test__A__s1.f32.wav"), st, SR, subtype="FLOAT")
    sf.write(str(ind / "hit.test__B__s1.wav"), np.clip(st, -1, 1), SR, subtype="PCM_16")   # no float copy
    out = tmp_path / "out"
    batch = pipeline.run([str(ind)], out_dir=out, opts=pipeline.Options(layers=("L1",), stage="raw", quiet=True))
    names = sorted(f["name"] for f in batch["files"])
    assert names == ["hit.test__A__s1.wav", "hit.test__B__s1.wav"]          # the twin is not scored on its own
    a = json.loads((out / "hit.test__A__s1.json").read_text())
    b = json.loads((out / "hit.test__B__s1.json").read_text())
    chk = {c["id"]: c for c in a["L1"]["checks"]}
    assert chk["clip_full_scale"]["ok"] and chk["clip_full_scale"]["measured_on"] == "raw-float"
    assert chk["writer_clip"]["value"] >= 1 and chk["writer_clip"]["ok"]
    assert a["L1"]["clip_source"]["file"] == "hit.test__A__s1.f32.wav"
    assert a["verdict"] != "BLOCK" and b["verdict"] == "BLOCK" and "clip_full_scale" in b["L1"]["blocking"]


def test_a_twin_with_other_audio_is_ignored(tmp_path):
    ind = tmp_path / "raw"
    ind.mkdir()
    t = np.arange(SR // 2) / SR
    x = 1.2 * np.sin(2 * np.pi * 300 * t)
    sf.write(str(ind / "z__A__s1.wav"), np.clip(x, -1, 1), SR, subtype="PCM_16")
    sf.write(str(ind / "z__A__s1.f32.wav"), 0.5 * np.sin(2 * np.pi * 500 * t), SR, subtype="FLOAT")
    out = tmp_path / "out"
    pipeline.run([str(ind / "z__A__s1.wav")], out_dir=out, opts=pipeline.Options(layers=("L1",), stage="raw", quiet=True))
    a = json.loads((out / "z__A__s1.json").read_text())
    assert a["verdict"] == "BLOCK" and "clip_source" not in a["L1"]


def test_low_thump_and_a_band_that_comes_and_goes_are_signatures():
    """Batch 0b r2: a wind-mic thump under 100 Hz and a 4.2 kHz hiss band that stops mid-loop."""
    from scipy import signal
    x = bed(seed=7)
    k = int(2.5 * SR)
    t = np.arange(int(0.05 * SR)) / SR
    x[k:k + len(t)] += (1.2 * np.sin(2 * np.pi * 60 * t) * np.hanning(len(t)))[:, None]   # low thump only
    sig = loopcheck.signature(x, SR)
    thumps = [e for e in sig["events"] if e["kind"] == "knock"]
    assert thumps and abs(thumps[0]["t"] - 2.5) < 0.06 and thumps[0]["band"] in ("full", "below-200")
    y = bed(seed=8)
    hiss = np.random.default_rng(9).standard_normal(y.shape[0])
    hiss = signal.sosfiltfilt(signal.butter(4, [4100, 4500], "bandpass", fs=SR, output="sos"), hiss)
    on = np.zeros(y.shape[0])
    on[: int(3.6 * SR)] = 1.0
    y += (0.4 * hiss * np.convolve(on, np.ones(2400) / 2400, "same"))[:, None]       # about -10 dB re the bed there
    sig = loopcheck.signature(y, SR)
    bands = [e for e in sig["events"] if e["kind"] == "band"]
    assert sig["bands"] == 1 and 3800 <= bands[0]["hz"] <= 4800 and bands[0]["t"] < 3.6
    assert loopcheck.signature(bed(seed=8), SR)["bands"] == 0


def test_a_quiet_low_thump_and_a_short_tone_mark_a_bright_bed():
    """Review 2 (amb.forest H s2001): a < 200 Hz thump 11 dB over its median, hidden in the full
    band by a bright bed, and a 3.93 kHz near-tone 13 dB over its neighbours: both mark the loop."""
    from scipy import signal
    rng = np.random.default_rng(21)
    n = 6 * SR
    hi = signal.sosfilt(signal.butter(2, 1000, "high", fs=SR, output="sos"), rng.standard_normal((n, 2)), axis=0)
    lo = signal.sosfilt(signal.butter(4, [30, 180], "bandpass", fs=SR, output="sos"), rng.standard_normal((n, 2)), axis=0)
    x = 0.2 * hi + 0.02 * lo
    assert loopcheck.signature(x, SR)["knocks"] == 0
    k = int(2.0 * SR)
    t = np.arange(int(0.08 * SR)) / SR
    y = x.copy()
    y[k:k + len(t)] += (0.12 * np.sin(2 * np.pi * 70 * t) * np.hanning(len(t)))[:, None]
    sig = loopcheck.signature(y, SR)
    low = [e for e in sig["events"] if e["kind"] == "knock" and e["band"] == "below-200"]
    assert low and abs(low[0]["t"] - 2.0) < 0.08
    z = x.copy()
    a = int(0.4 * SR)
    t = np.arange(int(0.2 * SR)) / SR
    z[a:a + len(t)] += (0.08 * np.sin(2 * np.pi * 3930 * t) * np.hanning(len(t)))[:, None]   # the 24 dB chirp test misses it
    tones = [e for e in loopcheck.signature(z, SR)["events"] if e.get("rule") == "tone"]
    assert tones and abs(tones[0]["hz"] - 3930) < 30 and abs(tones[0]["t"] - 0.5) < 0.12
    assert not loopcheck.tones(x.mean(axis=1), SR)
