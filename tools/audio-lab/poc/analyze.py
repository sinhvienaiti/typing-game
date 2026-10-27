"""analyze.py - technical "AI ears" for game audio.

Input : WAV / OGG / FLAC / MP3 (via libsndfile >= 1.1, no ffmpeg needed)
Output: <out>/<name>.json  (metrics + rule-based QA flags for a sound profile)
        <out>/<name>.png   (waveform, mel spectrogram, loudness envelope, spectrum,
                            loop seam) for a multimodal reviewer to look at

Usage:
  python -I analyze.py FILE [FILE ...] --out OUT_DIR [--profile impact|ui|loop|ambience|music|auto]

All thresholds in PROFILES are heuristics for game SFX, not a standard.
"""
import argparse
import json
import os
import sys

import numpy as np
import soundfile as sf
from scipy import signal
import pyloudnorm as pyln
import librosa

EPS = 1e-12


def db(x):
    return 20 * np.log10(np.maximum(np.abs(x), EPS))


def pdb(x):  # power -> dB
    return 10 * np.log10(np.maximum(x, EPS))


def load(path):
    data, sr = sf.read(path, always_2d=True, dtype="float64")
    return data, sr


# ---------------------------------------------------------------- loudness
def k_weighted(data, sr):
    meter = pyln.Meter(sr)
    z = data.copy()
    for _, stage in meter._filters.items():  # same K-weighting as integrated_loudness
        for ch in range(z.shape[1]):
            z[:, ch] = stage.apply_filter(z[:, ch])
    return z


def sliding_loudness(data, sr, win_s, hop_s):
    """BS.1770 momentary (0.4 s) / short-term (3 s) loudness curve, LUFS."""
    z = k_weighted(data, sr)
    G = np.array([1.0, 1.0, 1.0, 1.41, 1.41])[: z.shape[1]]
    win = int(win_s * sr)
    hop = max(1, int(hop_s * sr))
    pad = np.zeros((win, z.shape[1]))
    zp = np.vstack([pad, z, pad])  # let the window slide fully across the clip
    csum = np.vstack([np.zeros((1, z.shape[1])), np.cumsum(zp ** 2, axis=0)])
    starts = np.arange(0, zp.shape[0] - win, hop)
    ms = (csum[starts + win] - csum[starts]) / win
    lufs = -0.691 + 10 * np.log10(np.maximum((ms * G).sum(axis=1), EPS))
    times = starts / sr  # padded index s+win (window end) == clip index s
    return times, lufs


def integrated_lufs(data, sr):
    padded = False
    x = data
    if data.shape[0] < int(0.4 * sr) + 1:
        x = np.vstack([data, np.zeros((int(0.41 * sr) - data.shape[0] + 1, data.shape[1]))])
        padded = True
    meter = pyln.Meter(sr)
    try:
        v = float(meter.integrated_loudness(x))
    except Exception:
        v = float("-inf")
    return v, padded


def true_peak_dbtp(mono_or_multi, sr):
    # 4x oversampled peak (BS.1770-4 annex 2 style estimate)
    up = signal.resample_poly(mono_or_multi, 4, 1, axis=0)
    return float(db(np.max(np.abs(up))))


# ---------------------------------------------------------------- envelope / dynamics
def frame_rms(x, sr, frame_ms=1.0, hop_ms=0.5):
    fl = max(1, int(sr * frame_ms / 1000))
    hop = max(1, int(sr * hop_ms / 1000))
    if len(x) < fl:
        x = np.pad(x, (0, fl - len(x)))
    fr = librosa.util.frame(np.ascontiguousarray(x), frame_length=fl, hop_length=hop)
    rms = np.sqrt(np.mean(fr ** 2, axis=0))
    t = (np.arange(rms.shape[0]) * hop + fl / 2) / sr
    return t, rms


def rms_db_window(x, sr, t0, t1):
    a, b = int(max(0, t0) * sr), int(max(0, t1) * sr)
    seg = x[a:b]
    if len(seg) == 0:
        return float("-inf")
    return float(pdb(np.mean(seg ** 2)))


def dynamics(x, sr):
    peak = float(np.max(np.abs(x)) + EPS)
    thr = 10 ** (-60 / 20)
    above = np.where(np.abs(x) > thr)[0]
    if len(above) == 0:
        return {"silent": True}
    head = above[0] / sr
    tail_sil = (len(x) - 1 - above[-1]) / sr

    t, env = frame_rms(x, sr, 1.0, 0.5)
    emax = env.max()
    i_pk = int(np.argmax(env))
    i10 = int(np.argmax(env >= 0.1 * emax))
    i90 = int(np.argmax(env >= 0.9 * emax))
    attack_ms = max(0.0, (t[i90] - t[i10]) * 1000)
    onset_t = t[i10]

    env_db = pdb(env ** 2)
    # fastest rise in dB over 1 ms (2 hops) during the first 50 ms after onset
    seg = env_db[i10: i10 + 100]
    rise = float(np.max(seg[2:] - seg[:-2])) if len(seg) > 3 else 0.0

    # tail: time from envelope peak until envelope stays below peak-60 dB (relative)
    rel = env_db - env_db[i_pk]
    above_rel = np.where(rel > -60)[0]
    last_rel = above_rel[-1]
    tail_ms_rel60 = (t[last_rel] - t[i_pk]) * 1000
    reached_rel60 = last_rel < len(env) - 3
    end_level_rel_db = float(np.max(rel[-10:])) if len(rel) >= 10 else float(rel[-1])

    # punch / transient layer
    early = rms_db_window(x, sr, onset_t, onset_t + 0.020)
    late = rms_db_window(x, sr, onset_t + 0.100, onset_t + 0.300)
    sos = signal.butter(4, 2000, btype="high", fs=sr, output="sos")
    xh = signal.sosfilt(sos, x)
    hf_early = rms_db_window(xh, sr, onset_t, onset_t + 0.015)
    hf_late = rms_db_window(xh, sr, onset_t + 0.030, onset_t + 0.130)
    full_early = rms_db_window(x, sr, onset_t, onset_t + 0.015)

    # crest factor on the active part (frames above peak-40 dB) so silence padding does not inflate it
    act = env_db > (env_db.max() - 40)
    active_rms = float(np.sqrt(np.mean(env[act] ** 2)))
    last5 = x[-max(1, int(0.005 * sr)):]

    return {
        "silent": False,
        "head_silence_ms": round(head * 1000, 2),
        "tail_silence_ms": round(tail_sil * 1000, 2),
        "attack_ms_10_90": round(attack_ms, 2),
        "onset_ms": round(onset_t * 1000, 2),
        "time_to_peak_ms": round((t[i_pk] - onset_t) * 1000, 2),
        "rise_rate_db_per_ms": round(rise, 2),
        "punch_db_early20_vs_100_300": None if not np.isfinite(late) else round(min(40.0, early - late), 2),
        "transient_hf_db_0_15_vs_30_130": None if not np.isfinite(hf_late) else round(min(40.0, hf_early - hf_late), 2),
        "transient_hf_share_db": round(hf_early - full_early, 2),
        "crest_factor_db": round(float(db(peak) - db(active_rms)), 2),
        "rms_dbfs_whole": round(float(pdb(np.mean(x ** 2))), 2),
        "rms_dbfs_active": round(float(db(active_rms)), 2),
        "tail_ms_to_minus60_rel": round(tail_ms_rel60, 1),
        "tail_reaches_minus60_rel": bool(reached_rel60),
        "end_level_rel_db": round(end_level_rel_db, 1),
        "last5ms_dbfs": round(float(pdb(np.mean(last5 ** 2))), 1),
        "_env": (t, env_db, onset_t, t[i_pk], t[i90]),
    }


# ---------------------------------------------------------------- spectrum
BANDS = [("sub_20_60", 20, 60), ("bass_60_250", 60, 250), ("lowmid_250_500", 250, 500),
         ("mid_500_2k", 500, 2000), ("highmid_2k_6k", 2000, 6000), ("air_6k_20k", 6000, 20000)]


def spectral(x, sr):
    n_fft = 2048 if len(x) >= 2048 else int(2 ** np.floor(np.log2(max(256, len(x)))))
    hop = n_fft // 8
    S = np.abs(librosa.stft(x, n_fft=n_fft, hop_length=hop, center=True)) ** 2
    fe = S.sum(axis=0)
    act = fe > fe.max() * 10 ** (-50 / 10)
    w = fe[act] / fe[act].sum()
    Sa = S[:, act]
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    cent = librosa.feature.spectral_centroid(S=np.sqrt(Sa), sr=sr, n_fft=n_fft)[0]
    roll = librosa.feature.spectral_rolloff(S=np.sqrt(Sa), sr=sr, n_fft=n_fft, roll_percent=0.85)[0]
    flat = librosa.feature.spectral_flatness(S=np.sqrt(Sa))[0]
    bw = librosa.feature.spectral_bandwidth(S=np.sqrt(Sa), sr=sr, n_fft=n_fft)[0]
    avg = (Sa * w).sum(axis=1)
    tot = avg[(freqs >= 20)].sum() + EPS
    bands = {}
    for name, lo, hi in BANDS:
        bands[name] = round(float(avg[(freqs >= lo) & (freqs < hi)].sum() / tot), 4)
    low = avg[(freqs >= 20) & (freqs < 250)].sum() / tot
    mid = avg[(freqs >= 250) & (freqs < 4000)].sum() / tot
    high = avg[freqs >= 4000].sum() / tot
    mud = avg[(freqs >= 200) & (freqs < 500)].sum() / tot
    return {
        "spectral_centroid_hz": round(float((cent * w).sum()), 1),
        "spectral_rolloff85_hz": round(float((roll * w).sum()), 1),
        "spectral_flatness": round(float((flat * w).sum()), 4),
        "spectral_bandwidth_hz": round(float((bw * w).sum()), 1),
        "band_share": bands,
        "low_mid_high_share": [round(float(low), 3), round(float(mid), 3), round(float(high), 3)],
        "mud_200_500_share": round(float(mud), 3),
        "_spec": (freqs, avg),
    }


# ---------------------------------------------------------------- loop seam
def loopability(x, sr):
    n = int(0.15 * sr)
    if len(x) < 4 * n:
        return {"loop_score": None}
    d = np.abs(np.diff(x))
    jump = abs(x[0] - x[-1])
    p95 = np.percentile(d, 95) + EPS
    r_jump = jump / p95
    s_jump = 1.0 if r_jump <= 1 else float(np.exp(-(r_jump - 1) / 2))
    m1 = librosa.feature.melspectrogram(y=x[-n:], sr=sr, n_mels=64).mean(axis=1)
    m2 = librosa.feature.melspectrogram(y=x[:n], sr=sr, n_mels=64).mean(axis=1)
    a, b = pdb(m1) + 100, pdb(m2) + 100
    cos = float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + EPS))
    s_spec = float(np.clip((cos - 0.9) / 0.1, 0, 1))
    lvl = abs(rms_db_window(x, sr, len(x) / sr - 0.15, len(x) / sr) - rms_db_window(x, sr, 0, 0.15))
    s_lvl = float(np.exp(-lvl / 3))
    # click at seam: >4 kHz energy in 4 ms around the seam vs median of the neighbourhood
    seam = np.concatenate([x[-n:], x[:n]])
    sos = signal.butter(4, 4000, btype="high", fs=sr, output="sos")
    h = signal.sosfiltfilt(sos, seam)
    t, e = frame_rms(h, sr, 2.0, 1.0)
    c = int(np.argmin(np.abs(t - n / sr)))
    around = e[max(0, c - 2): c + 3].max()
    click_db = float(db(around) - db(np.median(e) + EPS))
    s_click = float(np.exp(-max(0.0, click_db - 3) / 6))
    score = 0.25 * (s_jump + s_spec + s_lvl + s_click)
    return {
        "loop_score": round(score, 3),
        "loop_seam_jump_ratio": round(float(r_jump), 2),
        "loop_spectral_cosine": round(cos, 4),
        "loop_level_diff_db": round(float(lvl), 2),
        "loop_seam_click_db": round(click_db, 2),
        "_seam": seam,
    }


# ---------------------------------------------------------------- QA rules
PROFILES = {
    # target ranges are heuristics for short combat SFX (game-ready, pre-mix)
    "impact": {"dur": (0.05, 3.0), "head_ms": 5, "attack_ms": 10, "punch_db": 6, "crest_min": 9,
               "mud_max": 0.30, "mmax": (-20, -6), "tp_max": -1.0, "low_min": 0.08, "hf_min": 0.03},
    "ui": {"dur": (0.02, 0.6), "head_ms": 2, "attack_ms": 5, "punch_db": None, "crest_min": 6,
           "mud_max": 0.35, "mmax": (-30, -12), "tp_max": -1.0, "low_min": None, "hf_min": 0.02},
    "loop": {"dur": (0.5, 120), "head_ms": 1, "attack_ms": None, "punch_db": None, "crest_min": 3,
             "mud_max": 0.45, "mmax": (-35, -10), "tp_max": -1.0, "low_min": None, "hf_min": None,
             "loop_min": 0.8},
    "ambience": {"dur": (2, 600), "head_ms": 50, "attack_ms": None, "punch_db": None, "crest_min": 3,
                 "mud_max": 0.5, "mmax": (-40, -16), "tp_max": -1.0, "low_min": None, "hf_min": None},
    "whoosh": {"dur": (0.2, 4.0), "head_ms": 30, "attack_ms": None, "punch_db": None, "crest_min": 6,
               "mud_max": 0.35, "mmax": (-24, -8), "tp_max": -1.0, "low_min": None, "hf_min": 0.03},
}


def qa(m, profile):
    p = PROFILES[profile]
    flags = []

    def add(level, rule, msg):
        flags.append({"level": level, "rule": rule, "msg": msg})

    if m["clipped_samples"] > 0:
        add("FAIL", "clipping", f"{m['clipped_samples']} samples at |x|>=0.999 in {m['clip_runs']} runs")
    if m["true_peak_dbtp"] > 0:
        add("FAIL", "true_peak", f"true peak {m['true_peak_dbtp']} dBTP > 0 (inter-sample overs)")
    elif m["true_peak_dbtp"] > p["tp_max"]:
        add("WARN", "true_peak", f"true peak {m['true_peak_dbtp']} dBTP > {p['tp_max']}")
    if abs(m["dc_offset"]) > 0.002:
        add("WARN", "dc_offset", f"DC offset {m['dc_offset']}")
    lo, hi = p["dur"]
    if not lo <= m["duration_s"] <= hi:
        add("WARN", "duration", f"{m['duration_s']} s outside {lo}-{hi} s")
    if m.get("silent"):
        add("FAIL", "silent", "no sample above -60 dBFS")
        return flags
    if m["head_silence_ms"] > p["head_ms"]:
        add("WARN", "head_silence", f"{m['head_silence_ms']} ms before first sound (adds input latency)")
    if p["attack_ms"] is not None and m["attack_ms_10_90"] > p["attack_ms"]:
        add("WARN", "soft_attack", f"attack {m['attack_ms_10_90']} ms > {p['attack_ms']} ms (hit feels late/soft)")
    if p["punch_db"] is not None and (m["punch_db_early20_vs_100_300"] or 0) < p["punch_db"]:
        add("WARN", "weak_punch", f"early/late {m['punch_db_early20_vs_100_300']} dB < {p['punch_db']} dB")
    if m["crest_factor_db"] < p["crest_min"]:
        add("WARN", "over_compressed", f"crest {m['crest_factor_db']} dB < {p['crest_min']} dB")
    if m["mud_200_500_share"] > p["mud_max"]:
        add("WARN", "muddy", f"200-500 Hz holds {m['mud_200_500_share']*100:.0f}% of energy (> {p['mud_max']*100:.0f}%)")
    low, mid, high = m["low_mid_high_share"]
    if p["low_min"] is not None and low < p["low_min"]:
        add("WARN", "thin", f"only {low*100:.1f}% energy below 250 Hz (no weight)")
    hf = m["band_share"]["highmid_2k_6k"] + m["band_share"]["air_6k_20k"]
    if profile == "impact":
        if m["transient_hf_share_db"] < -30:
            add("WARN", "dull", f">2 kHz part of the first 15 ms is {m['transient_hf_share_db']} dB (no crack/bite at the hit)")
        if m["tail_ms_to_minus60_rel"] < 40:
            add("WARN", "no_body", f"decays to -60 dB in {m['tail_ms_to_minus60_rel']} ms (a click, no body)")
    elif p["hf_min"] is not None and hf < p["hf_min"]:
        add("WARN", "dull", f"only {hf*100:.1f}% energy above 2 kHz (no bite/definition)")
    if profile in ("impact", "ui", "whoosh") and m["laptop_speaker_loss_db"] > 6:
        add("WARN", "small_speaker", f"loses {m['laptop_speaker_loss_db']} dB through a 200 Hz high-pass (laptop speaker): weight will vanish")
    a, b = p["mmax"]
    if not a <= m["lufs_momentary_max"] <= b:
        add("WARN", "loudness", f"momentary max {m['lufs_momentary_max']} LUFS outside {a}..{b}")
    if profile in ("impact", "ui", "whoosh") and m["last5ms_dbfs"] > -50:
        add("WARN", "tail_cut", f"last 5 ms at {m['last5ms_dbfs']} dBFS: sound is cut off (click at end)")
    if profile == "loop":
        if m.get("loop_score") is not None and m["loop_score"] < p["loop_min"]:
            add("FAIL", "loop_seam", f"loop score {m['loop_score']} < {p['loop_min']} "
                f"(jump x{m['loop_seam_jump_ratio']}, level diff {m['loop_level_diff_db']} dB, click {m['loop_seam_click_db']} dB)")
        if (m["lufs_momentary_range_db"] or 0) > 4:
            add("WARN", "unstable_level", f"momentary loudness swings {m['lufs_momentary_range_db']} dB inside the loop")
    return flags


def verdict(flags):
    if any(f["level"] == "FAIL" for f in flags):
        return "FAIL"
    if len(flags) >= 2:
        return "WEAK"
    if flags:
        return "OK_WITH_NOTES"
    return "PASS"


# ---------------------------------------------------------------- main analysis
def analyze(path, profile="impact"):
    data, sr = load(path)
    mono = data.mean(axis=1)
    m = {
        "file": os.path.basename(path),
        "profile": profile,
        "sample_rate": sr,
        "channels": int(data.shape[1]),
        "duration_s": round(len(mono) / sr, 4),
        "peak_dbfs": round(float(db(np.max(np.abs(data)))), 2),
        "true_peak_dbtp": round(true_peak_dbtp(data, sr), 2),
        "dc_offset": round(float(np.mean(mono)), 5),
    }
    clip_mask = np.abs(data).max(axis=1) >= 0.999
    m["clipped_samples"] = int(clip_mask.sum())
    m["clip_runs"] = int(np.sum(np.diff(np.concatenate([[0], clip_mask.astype(int)])) == 1))
    lufs_i, padded = integrated_lufs(data, sr)
    m["lufs_integrated"] = round(lufs_i, 2) if np.isfinite(lufs_i) else None
    m["lufs_integrated_padded"] = padded
    tm, lm = sliding_loudness(data, sr, 0.4, 0.01)
    m["lufs_momentary_max"] = round(float(lm.max()), 2)
    ts, ls = sliding_loudness(data, sr, 3.0, 0.1)
    m["lufs_short_term_max"] = round(float(ls.max()), 2)
    dur = len(mono) / sr
    core = lm[(tm >= 0.4) & (tm <= dur)]  # momentary windows fully inside the clip
    m["lufs_momentary_range_db"] = round(float(np.ptp(core)), 2) if len(core) else None
    # small-speaker simulation: how much momentary loudness survives a laptop (HPF 200 Hz)
    # or phone (HPF 400 Hz) speaker. Heuristic cut-offs, 4th-order Butterworth.
    for name, fc in (("laptop", 200), ("phone", 400)):
        sos = signal.butter(4, fc, btype="high", fs=sr, output="sos")
        _, lh = sliding_loudness(signal.sosfilt(sos, data, axis=0), sr, 0.4, 0.01)
        m[f"{name}_speaker_loss_db"] = round(float(lm.max() - lh.max()), 2)
    if data.shape[1] == 2:
        L, R = data[:, 0], data[:, 1]
        m["stereo_correlation"] = round(float(np.corrcoef(L, R)[0, 1]), 3) if np.std(L) > 0 and np.std(R) > 0 else 1.0
        mid, side = (L + R) / 2, (L - R) / 2
        m["side_to_mid_db"] = round(float(pdb(np.mean(side ** 2)) - pdb(np.mean(mid ** 2))), 1)
    dyn = dynamics(mono, sr)
    spec = spectral(mono, sr)
    loop = loopability(mono, sr)
    env = dyn.pop("_env", None)
    spec_curve = spec.pop("_spec")
    seam = loop.pop("_seam", None)
    m.update(dyn)
    m.update(spec)
    m.update(loop)
    m["onset_strength_max"] = round(float(librosa.onset.onset_strength(y=mono, sr=sr).max()), 2)
    flags = qa(m, profile)
    m["qa_flags"] = flags
    m["qa_verdict"] = verdict(flags)
    return m, (data, sr, mono, env, spec_curve, seam, (tm, lm))


def plot(m, ctx, png):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import librosa.display
    data, sr, mono, env, (freqs, avg), seam, (tm, lm) = ctx
    if m["profile"] not in ("loop", "ambience"):
        seam = None
    rows = 5 if seam is not None else 4
    fig, ax = plt.subplots(rows, 1, figsize=(12, 2.6 * rows + 0.6),
                           gridspec_kw={"height_ratios": [1, 1.4, 1, 1] + ([0.8] if seam is not None else [])})
    t = np.arange(len(mono)) / sr
    # 1 waveform
    for ch in range(data.shape[1]):
        ax[0].plot(t, data[:, ch], lw=0.6, alpha=0.8, label=f"ch{ch}")
    clip = np.where(np.abs(data).max(axis=1) >= 0.999)[0]
    if len(clip):
        ax[0].plot(t[clip], np.sign(mono[clip]) * 1.0, "r|", ms=10, label=f"clipped ({len(clip)})")
    ax[0].axhline(1, color="r", lw=0.5, ls="--")
    ax[0].axhline(-1, color="r", lw=0.5, ls="--")
    ax[0].set_ylim(-1.1, 1.1)
    ax[0].set_xlim(0, t[-1])
    ax[0].set_ylabel("amplitude")
    ax[0].legend(loc="upper right", fontsize=7)
    ax[0].set_title("Waveform  |  peak %.1f dBFS, true peak %.1f dBTP, DC %.4f" %
                    (m["peak_dbfs"], m["true_peak_dbtp"], m["dc_offset"]), fontsize=9, loc="left")
    # 2 mel spectrogram
    n_fft = 2048 if len(mono) >= 2048 else 512
    M = librosa.feature.melspectrogram(y=mono, sr=sr, n_fft=n_fft, hop_length=n_fft // 8, n_mels=128, fmax=sr / 2)
    img = librosa.display.specshow(librosa.power_to_db(M, ref=np.max, top_db=80), sr=sr, hop_length=n_fft // 8,
                                   x_axis="time", y_axis="mel", fmax=sr / 2, ax=ax[1], cmap="magma")
    ax[1].set_title("Mel spectrogram (dB rel. max, 80 dB range)  |  centroid %.0f Hz, rolloff85 %.0f Hz, flatness %.3f" %
                    (m["spectral_centroid_hz"], m["spectral_rolloff85_hz"], m["spectral_flatness"]), fontsize=9, loc="left")
    fig.colorbar(img, ax=ax[1], format="%+2.0f dB", pad=0.01)
    ax[1].set_xlabel("")
    # 3 loudness envelope
    if env is not None:
        te, edb, onset, tpk, t90 = env
        ax[2].plot(te, edb, lw=0.8, label="RMS 1 ms (dBFS)")
        ax[2].axvline(onset, color="g", lw=0.8, ls="--", label="onset (10%)")
        ax[2].axvline(t90, color="orange", lw=0.8, ls="--", label=f"90% (attack {m['attack_ms_10_90']} ms)")
    ax[2].plot(tm, lm, lw=1.2, color="k", label="momentary LUFS (400 ms)")
    ax[2].axhline(m["peak_dbfs"] - 60 if env is None else edb.max() - 60, color="grey", lw=0.6, ls=":", label="peak-60 dB")
    ax[2].set_ylim(-100, 3)
    ax[2].set_xlim(0, t[-1])
    ax[2].set_ylabel("dB")
    ax[2].legend(loc="upper right", fontsize=7, ncol=2)
    ax[2].set_title("Loudness envelope  |  LUFS-M max %.1f, LUFS-I %s, crest %.1f dB, tail->-60rel %.0f ms, punch %s dB" %
                    (m["lufs_momentary_max"], m["lufs_integrated"], m["crest_factor_db"],
                     m["tail_ms_to_minus60_rel"], m["punch_db_early20_vs_100_300"]), fontsize=9, loc="left")
    # 4 average spectrum
    sel = freqs >= 20
    ax[3].semilogx(freqs[sel], pdb(avg[sel] / (avg[sel].max() + EPS)), lw=0.9)
    colors = ["#ddeeff", "#cce0ff", "#ffe0cc", "#e8ffe0", "#f5e0ff", "#f0f0f0"]
    for (name, lo, hi), c in zip(BANDS, colors):
        ax[3].axvspan(lo, min(hi, sr / 2), color=c, alpha=0.6, lw=0)
        ax[3].text(np.sqrt(lo * min(hi, sr / 2)), -5, f"{name.split('_')[0]}\n{m['band_share'][name]*100:.0f}%",
                   ha="center", va="top", fontsize=7)
    ax[3].set_xlim(20, sr / 2)
    ax[3].set_ylim(-90, 3)
    ax[3].set_ylabel("dB rel.")
    ax[3].set_xlabel("Hz")
    ax[3].set_title("Average spectrum (energy-weighted)  |  mud 200-500 Hz %.0f%%" % (m["mud_200_500_share"] * 100),
                    fontsize=9, loc="left")
    if seam is not None:
        n = len(seam) // 2
        w = int(0.02 * sr)
        ts = (np.arange(2 * w) - w) / sr * 1000
        ax[4].plot(ts, seam[n - w: n + w], lw=0.8)
        ax[4].axvline(0, color="r", lw=0.8, ls="--")
        ax[4].set_xlabel("ms around loop seam (end -> start)")
        ax[4].set_title("Loop seam  |  score %s, jump x%s, level diff %s dB, HF click %s dB" %
                        (m["loop_score"], m["loop_seam_jump_ratio"], m["loop_level_diff_db"], m["loop_seam_click_db"]),
                        fontsize=9, loc="left")
    flags = "; ".join(f"{f['level']} {f['rule']}" for f in m["qa_flags"]) or "no flags"
    import textwrap
    head = (f"{m['file']}  [{m['profile']}]  {m['duration_s']} s @ {m['sample_rate']} Hz x{m['channels']}  ->  "
            f"{m['qa_verdict']}: {flags}")
    fig.suptitle("\n".join(textwrap.wrap(head, 150)), fontsize=10, x=0.01, ha="left")
    fig.tight_layout()
    fig.savefig(png, dpi=100)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--profile", default="impact", choices=list(PROFILES))
    ap.add_argument("--profile-map", help="JSON {basename: profile} overriding --profile")
    ap.add_argument("--no-png", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    pmap = json.load(open(a.profile_map)) if a.profile_map else {}
    results = []
    for f in a.files:
        prof = pmap.get(os.path.basename(f), a.profile)
        m, ctx = analyze(f, prof)
        stem = os.path.splitext(os.path.basename(f))[0]
        with open(os.path.join(a.out, stem + ".json"), "w") as fh:
            json.dump(m, fh, indent=2)
        if not a.no_png:
            plot(m, ctx, os.path.join(a.out, stem + ".png"))
        results.append(m)
        print(f"{m['file']:40s} {prof:8s} {m['qa_verdict']:14s} " +
              "; ".join(f"{x['level']}:{x['rule']}" for x in m["qa_flags"]))
    with open(os.path.join(a.out, "_all_metrics.json"), "w") as fh:
        json.dump(results, fh, indent=2)


if __name__ == "__main__":
    main()
