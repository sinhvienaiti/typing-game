"""Shared measurements (used by L1, L1b, L2 and the card) and the L2 ranking score.

Ported from the PoC analyze.py (dynamics, spectral, loudness, loopability), plus the
group-specific features of §4.3.3. Everything runs on the RAW file as stored.
"""
from __future__ import annotations

import math

import numpy as np

from . import audio as A
from . import groups as G
from .audio import EPS, db, fnum, pdb
from .spec import Spec
from .thresholds import L1, L1B, L2

PoC_BANDS = [("sub_20_60", 20, 60), ("bass_60_250", 60, 250), ("lowmid_250_500", 250, 500),
             ("mid_500_2k", 500, 2000), ("highmid_2k_6k", 2000, 6000), ("air_6k_20k", 6000, 20000)]

EXTRA_BANDS = {
    "share_below_120": (20, 120), "share_below_150": (20, 150), "share_below_300": (20, 300),
    "share_sub_40_90": (40, 90), "share_60_150": (60, 150), "share_150_600": (150, 600),
    "mud_share": (200, 500), "share_200_800": (200, 800), "share_1k_4k": (1000, 4000),
    "share_1k_5k": (1000, 5000), "share_4k_8k": (4000, 8000), "share_4k_10k": (4000, 10000),
    "share_150_800": (150, 800),
    "share_above_500": (500, 1e9), "share_above_3k": (3000, 1e9),
}


# ---------------------------------------------------------------- envelope and dynamics
def envelope(mono: np.ndarray, sr: int) -> dict:
    t, rms = A.frame_rms(mono, sr, 1.0, 0.5)
    env_db = pdb(rms ** 2)
    i_pk = int(np.argmax(rms))
    emax = rms[i_pk]
    # Attack to the first peak that reaches -3 dB of the loudest frame, so a layered sound
    # (click, then a louder body) is timed by its first loud moment.
    i_first = int(np.argmax(rms >= 0.708 * emax))
    p = i_first
    while p + 1 < len(rms) and rms[p + 1] >= rms[p]:
        p += 1
    ref = rms[p]
    i10 = int(np.argmax(rms >= 0.1 * ref))
    i90 = int(np.argmax(rms >= 0.9 * ref))
    return {"t": t, "rms": rms, "env_db": env_db, "i_pk": i_pk, "i_first_pk": p, "i10": i10, "i90": i90}


def dynamics(mono: np.ndarray, sr: int, env: dict) -> dict:
    t, rms, env_db = env["t"], env["rms"], env["env_db"]
    i_pk, i10, i90, p = env["i_pk"], env["i10"], env["i90"], env["i_first_pk"]
    onset = float(t[i10])
    early = A.rms_db(mono, sr, onset, onset + 0.020)
    late = A.rms_db(mono, sr, onset + 0.100, onset + 0.300)
    xh = A.band(mono, sr, 2000, None, zero_phase=False)
    hf_early = A.rms_db(xh, sr, onset, onset + 0.015)
    hf_late = A.rms_db(xh, sr, onset + 0.030, onset + 0.130)
    full_early = A.rms_db(mono, sr, onset, onset + 0.015)
    act = env_db > (env_db.max() - 40)
    active_rms = float(np.sqrt(np.mean(rms[act] ** 2)))
    rel = env_db - env_db[i_pk]
    above = np.where(rel > L1["tail_floor_db"])[0]
    last = int(above[-1]) if len(above) else i_pk
    seg = env_db[i10: i10 + 100]
    rise = float(np.max(seg[2:] - seg[:-2])) if len(seg) > 3 else 0.0
    return {
        "onset_ms": fnum(onset * 1000),
        "attack_ms": fnum(max(0.0, (t[i90] - t[i10]) * 1000)),
        "time_to_peak_ms": fnum((t[p] - onset) * 1000),
        "rise_rate_db_per_ms": fnum(rise),
        "punch_db": None if not np.isfinite(late) else fnum(min(40.0, early - late)),
        "transient_hf_db": None if not np.isfinite(hf_late) else fnum(min(40.0, hf_early - hf_late)),
        "transient_hf_share_db": fnum(max(-80.0, hf_early - full_early)),
        "crest_db": fnum(db(np.max(np.abs(mono))) - db(active_rms)),
        "rms_active_dbfs": fnum(db(active_rms)),
        "tail_ms": fnum((t[last] - t[i_pk]) * 1000, 1),
    }


def hf_attack(mono: np.ndarray, sr: int, env: dict) -> dict:
    """Smeared attack: rise time of the >= 2 kHz layer (crack) and its lag behind the full-band onset.

    A clean hit's crack reaches its peak in ~1 ms; a diffusion model often spreads it over 5-30 ms
    (§4.2 "đầu tiếng nhòe"). Only the attack is looked at: the 2 ms before the full-band onset to
    50 ms after it (ours), so a late high event (embers crackling at 85 ms, debris) is not taken
    for a slow crack. Same first-peak rule as the full-band attack (features.envelope)."""
    out = {"hf_attack_ms": None, "hf_onset_lag_ms": None}
    hi = min(L1B["smear_band"][1], sr / 2 * 0.95)
    y = A.band(mono, sr, L1B["smear_band"][0], hi, zero_phase=False)
    t, r = A.frame_rms(y, sr, 1.0, 0.25)
    if not len(r) or r.max() <= 0:
        return out
    on = float(env["t"][env["i10"]])
    win = (t >= on - L1B["smear_pre_ms"] / 1000) & (t <= on + L1B["smear_window_ms"] / 1000)
    if win.sum() < 4:
        return out
    idx = np.where(win)[0]
    rw = r[idx]
    full_pk = float(np.max(env["rms"]))
    if pdb(rw.max() ** 2) < pdb(full_pk ** 2) + L1B["smear_min_rel_db"]:
        return out                     # no HF layer in the attack: nothing to smear
    i_first = int(np.argmax(rw >= 0.708 * rw.max()))
    p = i_first
    while p + 1 < len(rw) and rw[p + 1] >= rw[p]:
        p += 1
    i10 = int(np.argmax(rw >= 0.1 * rw[p]))
    i90 = int(np.argmax(rw >= 0.9 * rw[p]))
    tw = t[idx]
    out["hf_attack_ms"] = fnum(max(0.0, (tw[i90] - tw[i10]) * 1000), 2)
    out["hf_onset_lag_ms"] = fnum((tw[i10] - on) * 1000, 2)
    return out


def hf_reonset(mono: np.ndarray, sr: int) -> dict:
    """Two onsets in one shot (ours, batch 0b review 2: gun.xung v3 sounded like two shots 25 ms apart).

    On the >= 2 kHz band (2 ms RMS, 0.5 ms hop): the first peak is the first frame within 6 dB of the
    band's loudest, climbed to its local top; the band's loudest frame 12-40 ms later is the second
    peak, the lowest frame between them the dip. Reported: delay, second peak re the first, rise
    over the dip, dip re the first; None when the band peaks more than 30 dB under the full band."""
    lo, hi = L1B["double_onset_after_ms"]
    out = {"hf_reonset_ms": None, "hf_reonset_db": None, "hf_reonset_rise_db": None, "hf_reonset_dip_db": None}
    y = A.band(mono, sr, 2000.0, min(16000.0, sr / 2 * 0.95), zero_phase=False)
    t, r = A.frame_rms(y, sr, 2.0, 0.5)
    _, rf = A.frame_rms(mono, sr, 2.0, 0.5)
    if not len(r) or r.max() <= 0:
        return out
    e = pdb(r ** 2)
    if float(e.max()) < float(pdb(rf.max() ** 2)) + L1B["double_onset_min_rel_db"]:
        return out
    i1 = int(np.argmax(e >= e.max() - 6.0))
    while i1 + 1 < len(e) and e[i1 + 1] >= e[i1]:
        i1 += 1
    sel = np.where((t >= t[i1] + lo / 1000) & (t <= t[i1] + hi / 1000))[0]
    if not sel.size:
        return out
    k = int(sel[int(np.argmax(e[sel]))])
    dip = float(e[i1:k + 1].min())
    out.update({"hf_reonset_ms": fnum((t[k] - t[i1]) * 1000, 1), "hf_reonset_db": fnum(e[k] - e[i1], 1),
                "hf_reonset_rise_db": fnum(e[k] - dip, 1), "hf_reonset_dip_db": fnum(dip - e[i1], 1)})
    return out


LR_BANDS = ((20.0, 150.0), (150.0, 1000.0), (1000.0, 4000.0), (4000.0, 16000.0))


def stereo_balance(L: np.ndarray, R: np.ndarray, sr: int) -> dict:
    """Channel balance (L re R, dB) broadband and in 4 bands, and the side level re the mid (ours,
    batch 0b review 2: a bed leaning 6 dB right; a 'stereo' bed whose side sat 11.8 dB under the mid)."""
    def bal(a, b):
        return float(pdb(np.mean(a ** 2)) - pdb(np.mean(b ** 2)))
    bands = []
    for lo, hi in LR_BANDS:
        if hi >= sr / 2:
            hi = sr / 2 * 0.95
        bands.append(fnum(bal(A.band(L, sr, lo, hi), A.band(R, sr, lo, hi)), 1))
    mid, side = (L + R) / 2, (L - R) / 2
    return {"lr_balance_db": fnum(bal(L, R), 2), "lr_balance_bands_db": bands,
            "side_mid_db": fnum(max(-120.0, float(pdb(np.mean(side ** 2)) - pdb(np.mean(mid ** 2)))), 1)}


def ending(mono: np.ndarray, sr: int, env: dict) -> dict:
    """Tail end: decayed to -60 dB re peak, or a fade of >= 5 ms (§4.3.1)."""
    peak_rms = float(env["rms"][env["i_pk"]]) + EPS
    n1 = max(1, int(0.001 * sr))
    n5 = int(L1["tail_fade_min_ms"] / 1000 * sr)
    end_rms = float(np.sqrt(np.mean(mono[-n1:] ** 2)))
    end_db = float(db(end_rms) - db(peak_rms))
    fade_drop = None
    if len(mono) >= n5 + n1:
        a_start = float(np.max(np.abs(mono[-(n5 + n1):-n5]))) + EPS
        a_end = float(np.max(np.abs(mono[-n1:]))) + EPS
        fade_drop = float(db(a_start) - db(a_end))
    last_abs = float(np.abs(mono[-1])) if len(mono) else 0.0
    return {
        "end_level_db_rel": fnum(max(-120.0, end_db), 1),
        "end_decayed": bool(end_db <= L1["tail_floor_db"]),
        "end_fade_drop_db": fnum(fade_drop, 1),
        "end_faded": bool(fade_drop is not None and fade_drop >= L1["tail_fade_drop_db"]),
        "last_sample_db_rel": fnum(max(-120.0, float(db(last_abs) - db(np.max(np.abs(mono)) + EPS))), 1),
    }


# ---------------------------------------------------------------- spectrum
def spectral(mono: np.ndarray, sr: int) -> tuple[dict, tuple]:
    import librosa
    x = mono.astype(np.float64)
    n_fft = 2048 if len(x) >= 2048 else int(2 ** np.floor(np.log2(max(256, len(x)))))
    if len(x) < n_fft:
        x = np.pad(x, (0, n_fft - len(x)))
    hop = n_fft // 8
    S = np.abs(librosa.stft(x, n_fft=n_fft, hop_length=hop, center=True)) ** 2
    fe = S.sum(axis=0)
    act = fe > fe.max() * 10 ** (-50 / 10)
    w = fe[act] / (fe[act].sum() + EPS)
    Sa = S[:, act]
    freqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft)
    mag = np.sqrt(Sa)
    cent = librosa.feature.spectral_centroid(S=mag, sr=sr, n_fft=n_fft)[0]
    roll = librosa.feature.spectral_rolloff(S=mag, sr=sr, n_fft=n_fft, roll_percent=0.85)[0]
    flat = librosa.feature.spectral_flatness(S=mag)[0]
    bw = librosa.feature.spectral_bandwidth(S=mag, sr=sr, n_fft=n_fft)[0]
    avg = (Sa * w).sum(axis=1)
    tot = avg[freqs >= 20].sum() + EPS

    def share(lo, hi):
        return float(avg[(freqs >= lo) & (freqs < hi)].sum() / tot)

    out = {
        "centroid_hz": fnum((cent * w).sum(), 1),
        "rolloff85_hz": fnum((roll * w).sum(), 1),
        "flatness": fnum((flat * w).sum(), 4),
        "bandwidth_hz": fnum((bw * w).sum(), 1),
        "band_share": {name: fnum(share(lo, hi), 4) for name, lo, hi in PoC_BANDS},
    }
    for k, (lo, hi) in EXTRA_BANDS.items():
        out[k] = fnum(share(lo, hi), 4)
    out["share_low300_hi4k10k"] = fnum(share(20, 300) + share(4000, 10000), 4)
    out["key_1k4k_vs_4k8k_db"] = fnum(10 * math.log10((share(1000, 4000) + EPS) / (share(4000, 8000) + EPS)), 1)
    out["above3k_vs_150_600_db"] = fnum(10 * math.log10((share(3000, 1e9) + EPS) / (share(150, 600) + EPS)), 1)
    return out, (freqs, avg)


def band_energy(x: np.ndarray, sr: int, lo, hi, t0: float, t1: float) -> float:
    a, b = int(max(0.0, t0) * sr), int(max(0.0, t1) * sr)
    if b <= a:
        return 0.0
    y = A.band(x[max(0, a - 512): b + 512], sr, lo, hi)   # margin for filter settling
    off = a - max(0, a - 512)
    return float(np.sum(y[off: off + (b - a)] ** 2))


def local_bands(mono: np.ndarray, sr: int, onset_s: float) -> dict:
    """Time-local band measures of §4.3.3 (crack, sub length, voice band)."""
    out: dict = {}
    tot15 = float(np.sum(mono[int(onset_s * sr): int((onset_s + 0.015) * sr)] ** 2)) + EPS
    tot30 = float(np.sum(mono[int(onset_s * sr): int((onset_s + 0.030) * sr)] ** 2)) + EPS
    out["onset_2k6k_share"] = fnum(band_energy(mono, sr, 2000, 6000, onset_s, onset_s + 0.015) / tot15, 4)
    out["crack_2k8k_share_30ms"] = fnum(band_energy(mono, sr, 2000, 8000, onset_s, onset_s + 0.030) / tot30, 4)

    def band_env(lo, hi, frame_ms=10.0):
        y = A.band(mono, sr, lo, hi)
        t, r = A.frame_rms(y, sr, frame_ms, frame_ms)
        return t, pdb(r ** 2)

    full_peak = float(pdb(np.max(A.frame_rms(mono, sr, 10, 10)[1]) ** 2))
    t, e = band_env(40, 90)
    if e.max() < full_peak - 40:
        out["sub_len_ms"] = None          # no sub layer: "sub too long" does not apply
    else:
        on = t >= onset_s
        idx = np.where(on & (e >= e.max() - 20))[0]
        out["sub_len_ms"] = fnum((t[idx[-1]] - onset_s) * 1000 + 10, 1) if len(idx) else 0.0
    t, e = band_env(1000, 4000)
    early = A.rms_db(A.band(mono, sr, 1000, 4000), sr, onset_s, onset_s + 0.020)
    late = A.rms_db(A.band(mono, sr, 1000, 4000), sr, onset_s + 0.100, onset_s + 0.130)
    out["voice_drop_db"] = fnum(min(60.0, early - late) if np.isfinite(late) else 60.0, 1)
    out["sustain_1k4k_ms"] = fnum(float(np.sum(e >= e.max() - 20)) * 10.0, 1) if e.max() > full_peak - 40 else 0.0
    return out


# ---------------------------------------------------------------- loudness
def loudness(data: np.ndarray, sr: int) -> tuple[dict, tuple]:
    z = A.k_weighted(data, sr)
    tm, lm = A.sliding_loudness(data, sr, 0.4, 0.01, z)
    ts, ls = A.sliding_loudness(data, sr, 3.0, 0.1, z)
    tb, lb = A.sliding_loudness(data, sr, 0.1, 0.005, z)
    dur = data.shape[0] / sr
    core = lm[(tm >= 0.4) & (tm <= dur)]
    out = {
        "lufs_m_max": fnum(lm.max()),
        "lufs_s_max": fnum(ls.max()),
        "lufs_100ms_max": fnum(lb.max()),
        "lufs_b100": fnum(A.integrated(data, sr, L2["lufs_block_short_s"])) if dur <= 3.0 else None,
        "lufs_i": fnum(A.integrated(data, sr, 0.4)) if dur >= 0.4 else None,
        "lufs_m_range_db": fnum(np.percentile(core, 95) - np.percentile(core, 5)) if len(core) > 4 else None,
    }
    for name, fc in (("speaker", L2["speaker_hpf_hz"]), ("phone", L2["phone_hpf_hz"])):
        hp = A.band(data, sr, fc, None, zero_phase=False)
        _, lh = A.sliding_loudness(hp, sr, 0.4, 0.01)
        out[f"{name}_loss_db"] = fnum(lm.max() - lh.max())
    return out, (tm, lm, tb, lb)


# ---------------------------------------------------------------- pitch
def pitch(mono: np.ndarray, sr: int, onset_s: float) -> tuple[dict, tuple | None]:
    import librosa
    a = int((onset_s + 0.03) * sr)
    seg = mono[a: a + int(2.0 * sr)]
    if len(seg) < int(0.08 * sr):
        return {"f0_hz": None, "pitch_off_cents": None, "voiced_ratio": 0.0}, None
    y = A.resample(seg, sr, 22050)
    f0, voiced, _ = librosa.pyin(y, fmin=65.0, fmax=2093.0, sr=22050, frame_length=2048, hop_length=256)
    times = onset_s + 0.03 + np.arange(len(f0)) * 256 / 22050
    ok = voiced & np.isfinite(f0)
    if ok.sum() < 3:
        return {"f0_hz": None, "pitch_off_cents": None, "voiced_ratio": fnum(ok.mean(), 3)}, None
    f = float(np.median(f0[ok]))
    midi = 69 + 12 * math.log2(f / 440.0)
    off = (midi - round(midi)) * 100
    return ({"f0_hz": fnum(f, 1), "pitch_off_cents": fnum(abs(off), 1), "voiced_ratio": fnum(ok.mean(), 3),
             "note_midi": int(round(midi))}, (times[ok], f0[ok]))


# ---------------------------------------------------------------- loop seam (shared by L1 and the card)
def seam(data: np.ndarray, sr: int) -> dict:
    n = int(L1["loop_window_ms"] / 1000 * sr)
    out: dict = {"applies": data.shape[0] >= 4 * n}
    if not out["applies"]:
        return out
    jumps, excess = [], []
    for ch in range(data.shape[1]):
        x = data[:, ch]
        j = abs(x[0] - x[-1])
        p95 = float(np.percentile(np.abs(np.diff(x)), 95))
        jumps.append(j)
        excess.append(max(0.0, j - p95))
    mono = data.mean(axis=1)
    head, tail = mono[:n], mono[-n:]
    lv = abs(float(pdb(np.mean(tail ** 2)) - pdb(np.mean(head ** 2))))

    def centroid(seg):
        f = np.fft.rfftfreq(len(seg), 1 / sr)
        p = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))) ** 2
        return float((f * p).sum() / (p.sum() + EPS))

    c1, c2 = centroid(tail), centroid(head)
    out.update({
        "jump_dbfs": fnum(db(max(jumps)), 1),
        "jump_excess_dbfs": fnum(max(-120.0, float(db(max(excess)))), 1),
        "rms_diff_db": fnum(lv),
        "centroid_end_hz": fnum(c1, 1), "centroid_start_hz": fnum(c2, 1),
        "centroid_diff_rel": fnum(abs(c1 - c2) / (0.5 * (c1 + c2) + EPS), 4),
    })
    return out


# ---------------------------------------------------------------- core analysis
def analyze(a: A.Audio, spec: Spec) -> tuple[dict, dict]:
    """All measurements of one file. Returns (metrics, context-for-card)."""
    data, sr = a.data, a.sr
    mono = a.mono
    peak = float(np.max(np.abs(data))) if data.size else 0.0
    m: dict = {
        "duration_s": fnum(a.duration, 4), "duration_ms": fnum(a.duration * 1000, 1),
        "sample_rate": sr, "channels": a.channels,
        "peak_dbfs": fnum(db(peak)), "true_peak_dbtp": fnum(A.true_peak_dbtp(data)),
        "dc_offset": fnum(A.dc_estimate(data, sr), 6),
        "mean_abs": fnum(float(np.max(np.abs(data.mean(axis=0)))), 6),   # plain mean, for reference only
        "silent": bool(peak < 10 ** (L1["silent_dbfs"] / 20)),
    }
    lvl = 10 ** (L1["head_level_dbfs"] / 20)
    above = np.where(np.abs(data).max(axis=1) >= lvl)[0]
    m["head_silence_ms"] = fnum(above[0] / sr * 1000) if len(above) else fnum(a.duration * 1000)
    ctx: dict = {"audio": a}
    if m["silent"]:
        return m, ctx
    env = envelope(mono, sr)
    ctx["env"] = env
    m.update(dynamics(mono, sr, env))
    if spec.group_obj.percussive:
        m.update(hf_attack(mono, sr, env))
        if not spec.loop:
            m.update(hf_reonset(mono, sr))
    m.update(ending(mono, sr, env))
    lo, curves = loudness(data, sr)
    m.update(lo)
    ctx["loudness"] = curves
    sp, spec_curve = spectral(mono, sr)
    m.update(sp)
    ctx["spectrum"] = spec_curve
    m.update(local_bands(mono, sr, m["onset_ms"] / 1000))
    import librosa
    y = mono.astype(np.float32)
    m["onset_strength_max"] = fnum(librosa.onset.onset_strength(y=np.pad(y, (0, max(0, 2048 - len(y)))), sr=sr).max())
    if spec.loop or spec.group_obj.loop:
        m["seam"] = seam(data, sr)
        if spec.group != "music":          # beds: long-term spectrum, decoder comb, loop signature
            from . import loopcheck
            m["loop_spectrum"], ctx["loop_spectrum"] = loopcheck.summary(data, sr)
            m["loop_signature"] = loopcheck.signature(data, sr, loop=True)
    if spec.pitched:
        pm, track = pitch(mono, sr, m["onset_ms"] / 1000)
        m.update(pm)
        ctx["f0"] = track
    if a.channels == 2:
        L, R = data[:, 0], data[:, 1]
        m["stereo_correlation"] = fnum(np.corrcoef(L, R)[0, 1], 3) if np.std(L) > 0 and np.std(R) > 0 else 1.0
        e_lr = (np.mean(L ** 2) + np.mean(R ** 2)) / 2
        m["mono_loss_db"] = fnum(pdb(e_lr) - pdb(np.mean(((L + R) / 2) ** 2)))
        m.update(stereo_balance(L, R, sr))
    return m, ctx


# ---------------------------------------------------------------- L2 score
REF_FEATURES = sorted({t.feature for g in G.GROUPS.values() for t in g.targets})


def targets_for(spec: Spec, ref_stats: dict | None = None, calibration=None) -> list[tuple[G.Target, str]]:
    """Group targets, then the owner calibration (critic/calibration.py), then the spec's own duration
    and attack limit, then approved refs (>= 5) replace good bands."""
    base = list(spec.group_obj.targets)
    changed: dict[str, str] = {}
    if calibration is not None:
        from .calibration import spec_keys
        base, changed = calibration.targets(base, **spec_keys(spec))
    out = []
    for t in base:
        src = f"calibration:{changed[t.feature]}" if t.feature in changed else "group"
        if t.feature == "duration_ms" and spec.duration_ms:
            # good = the spec's own tolerance (what L1 accepts), so a length inside the spec is never red
            lo, hi = spec.duration_ms
            tol = spec.duration_tol
            t = G.between("duration_ms", lo * (1 - tol), hi * (1 + tol), 0.2, t.weight, t.low_vi, t.high_vi)
            src = "spec"
        if (t.feature == "attack_ms" and t.feature not in changed and spec.attack_max_ms
                and spec.attack_max_ms != spec.group_obj.attack_max_ms):
            t = G.at_most("attack_ms", spec.attack_max_ms / 2, spec.attack_max_ms, t.weight, high_vi=t.high_vi)
            src = "spec"
        st = (ref_stats or {}).get(t.feature)
        if st and st.get("n", 0) >= L2["refs_min"]:
            p10, p90 = st["p10"], st["p90"]
            w = max(p90 - p10, abs(p90) * 0.05, 1e-6)
            t = G.Target(t.feature, (p10, p90), (p10 - w, p90 + w), t.weight, t.low_vi, t.high_vi)
            src = "refs"
        out.append((t, src))
    return out


def l2_score(m: dict, spec: Spec, ref_stats: dict | None = None, calibration=None) -> dict:
    rows, num, den, notes = [], 0.0, 0.0, []
    for t, src in targets_for(spec, ref_stats, calibration):
        v = m.get(t.feature)
        d = t.desirability(v)
        rows.append({"feature": t.feature, "value": v, "good": [_j(t.good[0]), _j(t.good[1])],
                     "bad": [_j(t.bad[0]), _j(t.bad[1])], "weight": t.weight, "d": fnum(d, 3), "source": src})
        if d is None:
            continue
        num += t.weight * d
        den += t.weight
        if d < 0.5:
            side = t.low_vi if (v is not None and v < t.good[0]) else t.high_vi
            if side:
                notes.append((d, f"{side} ({_fmt(t.feature, v)})"))
    notes.sort(key=lambda x: x[0])
    return {"score": fnum(num / den, 4) if den else None, "targets": rows, "notes_vi": [n for _, n in notes[:3]],
            "calibration": calibration.version if calibration is not None else None}


def _j(v):
    return None if v is None or not math.isfinite(v) else v


def _fmt(feature: str, v) -> str:
    if v is None:
        return "không đo được"
    if "share" in feature and not feature.endswith("_db"):
        return f"{v * 100:.0f} %".replace(".", ",")
    unit = "ms" if feature.endswith("_ms") else "dB" if feature.endswith("_db") else "cent" if "cents" in feature else ""
    return f"{v:.1f} {unit}".replace(".", ",").replace("-", "−").strip()


def ref_stats(metric_rows: list[dict]) -> dict:
    """P10/P90 of every ranking feature over a set of reference metrics."""
    out = {}
    for f in REF_FEATURES:
        vals = [r.get(f) for r in metric_rows if isinstance(r.get(f), (int, float))]
        if vals:
            out[f] = {"n": len(vals), "p10": float(np.percentile(vals, 10)), "p90": float(np.percentile(vals, 90))}
    return out
