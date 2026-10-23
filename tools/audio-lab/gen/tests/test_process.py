"""gen/process.py: true onsets (first window too), creature calls whole, exponential tail cap,
card channels, decoder comb notch, loop crossfade with seam check, SOURCES records."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from build import ledger
from gen import process as P

SR = P.SR


def plan(**over) -> P.Plan:
    p = dict(id="x", game="typing-survival", loop=False, channels=1, onset_class="impact", rise_max_ms=10,
             target_ms=80, min_ms=64, max_ms=96, norm_mode="peak", norm_target=-1.0)
    p.update(over)
    return P.Plan(**p)


def tone(dur, f=220.0, sr=SR):
    t = np.arange(int(dur * sr)) / sr
    return np.sin(2 * np.pi * f * t)


def test_first_window_never_cuts_into_a_running_sound():
    # a steady tone from 100 ms, a hit 6 dB louder at 300 ms: the old chooser started at the hit
    x = np.zeros(int(0.8 * SR))
    a, b = int(0.1 * SR), int(0.6 * SR)
    x[a:b] = 0.3 * tone((b - a) / SR)
    h = int(0.3 * SR)
    x[h:h + int(0.08 * SR)] += 0.6 * tone(0.08, 900) * np.exp(-np.arange(int(0.08 * SR)) / SR / 0.02)
    res = P.process_oneshot(x[:, None], SR, plan(max_ms=600, min_ms=100, target_ms=400))
    w = res["window"]
    assert res["onset_ok"] and w["true_onset"]
    assert abs(w["onset_s"] - 0.1) < 0.003, w
    assert w["pre_onset_db"] is not None and w["pre_onset_db"] <= -30


def test_a_start_inside_an_earlier_tail_is_a_cut_in():
    # A: loud tone stopping at 200 ms; 15 ms of silence; B: quieter tone. B's 28 ms before hold A's end
    x = np.zeros(int(0.5 * SR))
    x[:int(0.2 * SR)] = 0.9 * tone(0.2)
    s = int(0.215 * SR)
    x[s:s + int(0.15 * SR)] = 0.27 * tone(0.15, 330)
    events, _ = P.find_events(x, SR)
    assert [e.kind for e in events] == ["file-start", "cut-in"]
    res = P.process_oneshot(x[:, None], SR, plan(max_ms=400, min_ms=50, target_ms=200))
    assert res["window"]["onset_s"] < 0.001 and res["window"]["onset_kind"] == "file-start"


def test_creature_keeps_its_whole_natural_onset():
    # a howl-like swell: 300 ms rise from 50 ms, then 600 ms decay
    n = int(1.2 * SR)
    t = np.arange(n) / SR
    env = np.clip((t - 0.05) / 0.3, 0, 1) * np.where(t > 0.35, np.exp(-(t - 0.35) / 0.12), 1.0)
    x = 0.5 * env * np.sin(2 * np.pi * 400 * t)
    p = plan(onset_class="creature", rise_max_ms=30, target_ms=1100, min_ms=880, max_ms=1320, whole=True)
    res = P.process_oneshot(x[:, None], SR, p)
    w = res["window"]
    assert res["onset_ok"] and abs(w["onset_s"] - 0.05) < 0.02
    assert w["len_ms"] > 700                     # whole call, its decay kept
    assert w["critic_attack_ms"] > 30            # the slow swell stays (the rise rule will block: owner judges)


def test_burst_keeps_only_the_first_shot():
    x = np.zeros(int(0.6 * SR))
    shot = 0.8 * np.random.default_rng(1).standard_normal(int(0.06 * SR)) * np.exp(-np.arange(int(0.06 * SR)) / SR / 0.012)
    for k in range(3):
        a = int((0.01 + 0.09 * k) * SR)
        x[a:a + len(shot)] += shot
    res = P.process_oneshot(x[:, None], SR, plan(max_ms=144, min_ms=96, target_ms=120))
    w = res["window"]
    assert w["onset_s"] < 0.011 and w["window_s"][1] <= 0.1     # never reaches the second shot at 100 ms
    assert res["usable"]                         # the first shot decayed on its own: a short sound, kept
    # shots 50 ms apart whose tails overlap (one run): the window ends at the dip before the second
    x = np.zeros(int(0.6 * SR))
    shot = 0.8 * np.random.default_rng(2).standard_normal(int(0.2 * SR)) * np.exp(-np.arange(int(0.2 * SR)) / SR / 0.012)
    for k in range(3):
        a = int((0.01 + 0.05 * k) * SR)
        x[a:a + len(shot)] += shot
    res = P.process_oneshot(x[:, None], SR, plan(max_ms=144, min_ms=96, target_ms=120))
    w = res["window"]
    assert w["end_kind"] == "next-hit" and w["window_s"][1] <= 0.062, w
    # 52 ms before the next shot, card min 96 ms: not a usable one-shot (rejected, with the reason)
    assert not res["usable"] and "ngắn hơn mức tối thiểu 96 ms" in res["reason"]


def test_tail_cap_is_exponential_not_a_flat_cut():
    n = int(0.096 * SR)
    t = np.arange(n) / SR
    y = np.sin(2 * np.pi * 2500 * t) * np.exp(-t / 0.08)    # rings far past 96 ms (-5 dB at the end)
    out, info = P.cap_tail(y, SR, int(0.035 * SR), -60.0)
    st, e = P.envelope(out, SR, 2.0, 1.0)
    e = e - e.max()
    assert e[-3] < -45 and info["max_cut_db"] > 40
    k0 = np.searchsorted(st, int(0.04 * SR))
    k1 = np.searchsorted(st, int(0.088 * SR))
    seg = e[k0:k1]
    slope = np.diff(seg)
    assert np.all(slope < 0.6)                       # falls all the way (no flat stretch, no pumping)
    half = len(seg) // 2
    s1, s2 = (seg[half] - seg[0]) / half, (seg[-1] - seg[half]) / (len(seg) - 1 - half)
    assert abs(s1 - s2) < 0.35 * abs(s1)             # a straight line in dB: an exponential decay
    early = np.abs(out[: int(0.03 * SR)]).max() / np.abs(y[: int(0.03 * SR)]).max()
    assert early > 0.99                              # nothing touched before the knee


def test_channels_follow_the_card():
    rng = np.random.default_rng(3)
    L = rng.standard_normal(4800)
    st = np.stack([L, 0.5 * L + 0.5 * rng.standard_normal(4800)], axis=1)
    y, info = P.to_channels(st, 2)
    assert y.shape[1] == 2 and info["channels"] == "stereo" and 0 < info["stereo_corr"] < 0.99
    y, info = P.to_channels(np.stack([L, L], axis=1), 2)
    assert info["dual_mono"] and info["channels"] == "stereo-dual-mono"
    y, info = P.to_channels(st, 1)
    assert y.shape[1] == 1 and info["channels"] == "mid"


def test_comb_notch_removes_decoder_lines_only():
    rng = np.random.default_rng(5)
    n = 4 * SR
    t = np.arange(n) / SR
    noise = 0.05 * rng.standard_normal(n)
    lines = sum(0.004 * np.sin(2 * np.pi * k * P.COMB_F0 * t + k) for k in range(60, 125))
    x = (noise + lines)[:, None]
    before = P.comb_lines(x, SR)
    y, rep = P.notch_comb(x, SR)
    after = P.comb_lines(y, SR)
    assert before["median_prom_db"] >= 8 and rep["notched"] >= 50
    assert -2.5 <= after["median_prom_db"] <= 2      # level with the bed: no holes where the lines were
    from scipy import signal
    f, p0 = signal.welch(x[:, 0], SR, nperseg=8192)
    _, p1 = signal.welch(y[:, 0], SR, nperseg=8192)
    band = (f > 1000) & (f < 9000)
    assert abs(10 * np.log10(p1[band].sum() / p0[band].sum())) < 0.2   # below 10 kHz untouched


def test_loop_crossfade_passes_its_seam_check():
    rng = np.random.default_rng(9)
    n = 10 * SR
    t = np.arange(n) / SR
    bed = rng.standard_normal((n, 2)) * (0.2 + 0.05 * np.sin(2 * np.pi * 0.3 * t))[:, None]
    from scipy import signal
    bed = signal.sosfilt(signal.butter(2, 3000, "low", fs=SR, output="sos"), bed, axis=0)
    p = plan(loop=True, channels=2, onset_class="loop", rise_max_ms=None, target_ms=6000, min_ms=4800,
             max_ms=7200, norm_mode="lufs-i", norm_target=-26.0)
    res = P.process_loop(bed, SR, p)
    assert res["seam_ok"] and res["loop"]["seam_ok"]
    assert abs(res["audio"].shape[0] - 6 * SR) <= 1
    bad = {"applies": True, "jump_excess_dbfs": -20.0, "rms_diff_db": 0.2, "centroid_diff_rel": 0.01}
    assert not P.seam_ok(bad)


def write_candidate(root: Path, name: str, x: np.ndarray, sr: int = 44100) -> Path:
    raw = root / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    st = np.stack([x, x], axis=1)
    sf.write(str(raw / f"{name}.wav"), np.clip(st, -1, 1), sr, subtype="PCM_16")
    sf.write(str(raw / f"{name}.f32.wav"), st, sr, subtype="FLOAT")
    rec = {"schema": "audiolab.sa3.candidate/1", "id": "hit.test", "game": "typing-survival", "candidate": name,
           "variant": "A", "prompt": "a clank", "seed": 1, "steps": 8, "cfg": 1.0, "seconds": 1.0,
           "model": {"id": "stabilityai/stable-audio-3-optimized@" + "f" * 40,
                     "repo": "stabilityai/stable-audio-3-optimized", "revision": "f" * 40},
           "files": {"wav16": {"path": str(raw / f"{name}.wav"), "sha256": ledger.sha256_file(raw / f"{name}.wav")},
                     "f32": {"path": str(raw / f"{name}.f32.wav"), "sha256": ledger.sha256_file(raw / f"{name}.f32.wav")}},
           "licence": {"rows": [ledger.model_row("stabilityai/stable-audio-3-optimized", "f" * 40,
                                                 "LicenseRef-Stability-Community-2024",
                                                 "https://stability.ai/community-license-agreement", "1" * 64,
                                                 "generate", "2026-10-23")], "copies": {}}}
    p = raw / f"{name}.json"
    p.write_text(json.dumps(rec), "utf-8")
    return p


def test_process_many_writes_finals_records_and_raw_clip_from_the_float_copy(tmp_path):
    t = np.arange(44100) / 44100
    hit = 1.25 * np.sin(2 * np.pi * 700 * t) * np.exp(-t / 0.03)          # over 1.0: only the 16-bit copy clips
    rec = write_candidate(tmp_path, "hit.test__A__s1", hit)
    card = {"id": "hit.test", "game": "typing-survival", "_path": str(tmp_path / "card.yaml"),
            "playback": {"mode": "one-shot", "channels": "mono"}, "onset": {"class": "impact", "rise_max_ms": 10},
            "duration": {"target_ms": 80, "min_ms": 64, "max_ms": 96},
            "loudness": {"file": {"metric": "peak-dbtp", "target": -1}}}
    out = tmp_path / "processed"
    res = P.process_many([rec], card, out)
    assert res["kept"] == 1 and not res["rejected"]
    wav = out / "hit.test__A__s1.wav"
    info = sf.info(str(wav))
    assert info.samplerate == 48000 and info.channels == 1 and info.subtype == "PCM_24"
    pj = json.loads((out / "hit.test__A__s1.proc.json").read_text())
    assert pj["window"]["true_onset"] and pj["window"]["len_ms"] <= 96.0     # pre-roll included in the card max
    src = ledger.read_sources(out / "SOURCES.json")
    assert not ledger.schema_errors("sources", src)
    lay = src["hit.test__A__s1.wav"]["layers"][0]
    assert lay["kind"] == "gen" and lay["rawQa"]["verdict"] == "PASS"        # the float copy is not clipped
    assert lay["rawQa"]["files"][0]["subtype"] == "FLOAT"
    assert ledger.read_rows(out / "licences.rows.jsonl")[0]["kind"] == "model"
    again = P.process_many([rec], card, out)
    assert again["skipped"] == 1


def test_a_burst_too_short_to_use_is_rejected_and_never_left_in_the_finals(tmp_path):
    sr = 44100
    x = np.zeros(sr)
    shot = 0.8 * np.random.default_rng(3).standard_normal(int(0.2 * sr)) * np.exp(-np.arange(int(0.2 * sr)) / sr / 0.012)
    for k in range(3):                                   # three shots 50 ms apart, tails overlapping
        a = int((0.01 + 0.05 * k) * sr)
        x[a:a + len(shot)] += shot
    rec = write_candidate(tmp_path, "hit.test__B__s2", x)
    card = {"id": "hit.test", "game": "typing-survival", "_path": str(tmp_path / "card.yaml"),
            "playback": {"mode": "one-shot", "channels": "mono"}, "onset": {"class": "impact", "rise_max_ms": 10},
            "duration": {"target_ms": 120, "min_ms": 96, "max_ms": 144},
            "loudness": {"file": {"metric": "peak-dbtp", "target": -1}}}
    out = tmp_path / "processed"
    out.mkdir()
    (out / "hit.test__B__s2.wav").write_bytes(b"stale")             # left by an earlier run
    res = P.process_many([rec], card, out, force=True)
    assert res["kept"] == 0 and "ngắn hơn mức tối thiểu" in res["rejected"][0]["reason"]
    assert not (out / "hit.test__B__s2.wav").exists()
    pj = json.loads((tmp_path / "processed-rejected" / "hit.test__B__s2.proc.json").read_text())
    assert pj["true_onset"] and not pj["onset_ok"] and pj["window"]["end_kind"] == "next-hit"
    assert "hit.test__B__s2.wav" not in ledger.read_sources(out / "SOURCES.json")


def test_flutter_inside_one_whoosh_is_not_a_second_hit():
    """Fire whoomphs flutter: a dip of the 10 ms level that lasts only a few ms must not split one
    burst (batch 0b r2: 4 of 9 fire takes were cut at 50-230 ms by such dips)."""
    rng = np.random.default_rng(5)
    n = int(0.6 * SR)
    t = np.arange(n) / SR
    env = np.minimum(1.0, t / 0.004) * np.exp(-t / 0.5)
    gate = np.ones(n)
    a = int(0.080 * SR)
    gate[a:a + int(0.011 * SR)] = 0.02                      # 11 ms flutter: the 10 ms level dips > 12 dB briefly
    x = 0.6 * rng.standard_normal(n) * env * gate
    p = plan(max_ms=408, min_ms=272, target_ms=340)
    res = P.process_oneshot(x[:, None], SR, p)
    assert res["usable"] and res["window"]["end_kind"] != "next-hit" and res["window"]["len_ms"] >= 272


def test_a_flam_is_rejected_but_a_crack_then_boom_is_not():
    """call-chop B s1006 (batch 0b r2): a weak knock 40 ms before the main one ranked first."""
    def knock(n, f, tau):
        t = np.arange(n) / SR
        return np.sin(2 * np.pi * f * t) * np.exp(-t / tau)
    x = np.zeros(int(0.4 * SR))
    a, b = int(0.010 * SR), int(0.050 * SR)
    x[a:a + int(0.2 * SR)] += 0.25 * knock(int(0.2 * SR), 700, 0.040)       # weak first knock (-12 dB), rings on
    x[b:b + int(0.2 * SR)] += 1.0 * knock(int(0.2 * SR), 650, 0.030)        # the main knock 40 ms later
    p = plan(onset_class="other", rise_max_ms=None, target_ms=250, min_ms=200, max_ms=300)
    res = P.process_oneshot(x[:, None], SR, p)
    assert not res["usable"] and res["reason"].startswith("gõ hai lần") and res["pre_hit"]["main_ms"] >= 35
    # gun take: a crack, then the boom 15 ms later, is one shot
    y = np.zeros(int(0.4 * SR))
    y[a:a + int(0.2 * SR)] += 0.5 * np.random.default_rng(4).standard_normal(int(0.2 * SR)) * np.exp(-np.arange(int(0.2 * SR)) / SR / 0.003)
    c = a + int(0.015 * SR)
    y[c:c + int(0.2 * SR)] += knock(int(0.2 * SR), 80, 0.04)
    res = P.process_oneshot(y[:, None], SR, plan(max_ms=144, min_ms=96, target_ms=120))
    assert res["usable"] and res["pre_hit"] is None


def test_a_file_start_needs_evidence_of_a_real_start():
    """Review 2 (hit.t1 A s1005, B s1006): the first sample already rang at -18..-22 dB and the
    >= 2 kHz peak came 12-14 ms later; a hit that starts at the file start keeps its crack in 5 ms."""
    from scipy import signal
    rng = np.random.default_rng(11)
    n = int(0.2 * SR)
    t = np.arange(n) / SR
    crack = signal.sosfilt(signal.butter(4, 3000, "high", fs=SR, output="sos"), rng.standard_normal(n))
    ring = 0.15 * np.sin(2 * np.pi * 600 * t) * np.exp(-t / 0.08)             # rings from sample 0
    late = np.zeros(n)
    k = int(0.013 * SR)
    late[k:] = 0.8 * crack[:n - k] * np.exp(-t[:n - k] / 0.004)               # its crack 13 ms in
    events, _ = P.find_events(ring + late, SR)
    assert events[0].kind == "file-start" and not events[0].verified and events[0].hf_peak_ms > 5
    res = P.process_oneshot((ring + late)[:, None], SR, plan(max_ms=120, min_ms=64, target_ms=96))
    assert res["usable"] and not res["onset_verified"] and "chưa xác minh" in res["onset_note"]
    hit = 0.8 * crack * np.exp(-t / 0.004) + 0.3 * np.sin(2 * np.pi * 300 * t) * np.exp(-t / 0.03)
    ev = P.find_events(hit, SR)[0][0]
    assert ev.kind == "file-start" and ev.verified and ev.hf_peak_ms <= 5
    quiet = np.concatenate([np.zeros(int(0.02 * SR)), hit])
    ev = P.find_events(quiet, SR)[0][0]
    assert ev.kind == "quiet" and ev.verified


def test_stereo_bed_is_levelled_per_band():
    """Review 2 (amb.forest H s2004): right louder by 6.6 dB under 150 Hz but 2.7 dB at 4-16 kHz."""
    from scipy import signal
    rng = np.random.default_rng(12)
    n = 8 * SR
    a, b = rng.standard_normal(n), rng.standard_normal(n)
    lo = signal.butter(4, 300, "low", fs=SR, output="sos")
    hi = signal.butter(4, 3000, "high", fs=SR, output="sos")
    L = signal.sosfilt(lo, a) + 0.3 * signal.sosfilt(hi, b)
    R = 2.1 * signal.sosfilt(lo, a + 0.5 * b) + 0.41 * signal.sosfilt(hi, b + 0.5 * a)
    x = np.stack([L, R], axis=1) * 0.1
    before = P.lr_balance(x, SR)
    assert before["broadband_db"] < -4 and before["bands_db"][0] < -5
    y, rep = P.balance_stereo(x, SR)
    assert rep["applied"] and abs(rep["after"]["broadband_db"]) < 0.5
    assert max(abs(v) for v in rep["after"]["bands_db"]) < 1.0
    same, rep2 = P.balance_stereo(np.stack([L, L], axis=1), SR)
    assert not rep2["applied"]
