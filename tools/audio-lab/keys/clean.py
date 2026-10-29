"""Cleaning chain for real keyboard recordings (owner 29/10: "xào xạc quá lởm", no hiss, no room under the hits).

A recording (CC0 / CC-BY, owner-approved download) goes, before slicing, through:

1. high-pass (4th order, zero phase, default 60 Hz): desk and HVAC rumble;
2. spectral gate: the noise spectrum is the mean STFT magnitude of the quietest frames (between strokes);
   a bin under noise x 10^(threshold/20) is turned down by `reduction_db`, the mask is smoothed over time and
   frequency so the gate never chirps; the mask only attenuates (never boosts), so it cannot add pre-echo;
3. de-click, only for artefacts: an isolated spike (<= 3 samples, > `k` x the local MAD of the 2nd difference)
   more than 6 ms from any stroke onset is replaced by interpolation; stroke onsets are never touched;
4. tone EQ (RBJ biquads), per profile: a low-mid lift toward a solid thock (150-400 Hz) and a gentle cut of the
   4-8 kHz scratch band, never a boost up there.

After slicing, `stroke_gate` is a downward expander on each stroke (threshold re the stroke's peak), so no room
tone sits under or after the press and its release. Every step reports numbers (noise floor and 4-8 kHz hiss in
the quiet frames before and after, spikes repaired), written into the take's record.
"""
from __future__ import annotations

import numpy as np
from scipy import signal

DEFAULTS = {
    "hpf_hz": 60.0,
    "gate": {"threshold_db": 6.0, "reduction_db": 24.0, "n_fft": 1024, "hop": 256, "quiet_pct": 15.0,
             "smooth_t": 5, "smooth_f": 5},
    "declick": {"k": 12.0, "protect_ms": 6.0},
    "eq": [{"type": "peak", "hz": 250.0, "db": 2.0, "q": 0.8}, {"type": "peak", "hz": 6000.0, "db": -2.5, "q": 0.9}],
    "stroke_gate": {"threshold_db": -48.0, "range_db": 30.0, "attack_ms": 0.5, "release_ms": 25.0},
}


def highpass(x: np.ndarray, sr: int, hz: float, order: int = 4) -> np.ndarray:
    if not hz:
        return x
    return signal.sosfiltfilt(signal.butter(order, hz, "high", fs=sr, output="sos"), x)


def _frames_db(x: np.ndarray, n: int, hop: int) -> np.ndarray:
    nf = max(1, 1 + (len(x) - n) // hop)
    return np.array([10 * np.log10(np.mean(x[i * hop:i * hop + n] ** 2) + 1e-20) for i in range(nf)])


def spectral_gate(x: np.ndarray, sr: int, threshold_db: float = 6.0, reduction_db: float = 24.0, n_fft: int = 1024,
                  hop: int = 256, quiet_pct: float = 15.0, smooth_t: int = 5, smooth_f: int = 5) -> tuple[np.ndarray, dict]:
    f, t, Z = signal.stft(x, fs=sr, window="hann", nperseg=n_fft, noverlap=n_fft - hop, boundary="even", padded=True)
    mag = np.abs(Z)
    e = 10 * np.log10(np.mean(mag ** 2, axis=0) + 1e-20)
    quiet = e <= np.percentile(e, quiet_pct)
    noise = mag[:, quiet].mean(axis=1, keepdims=True) + 1e-12
    over = mag > noise * 10 ** (threshold_db / 20)
    floor = 10 ** (-reduction_db / 20)
    mask = np.where(over, 1.0, floor)
    k = np.ones((max(1, smooth_f), max(1, smooth_t))) / (max(1, smooth_f) * max(1, smooth_t))
    mask = np.clip(signal.convolve2d(mask, k, mode="same", boundary="symm"), floor, 1.0)
    _, y = signal.istft(Z * mask, fs=sr, window="hann", nperseg=n_fft, noverlap=n_fft - hop, boundary=True)
    y = y[:len(x)] if len(y) >= len(x) else np.pad(y, (0, len(x) - len(y)))
    return y, {"quiet_frames": int(quiet.sum()), "frames": int(len(e)), "threshold_db": threshold_db,
               "reduction_db": reduction_db}


def onsets(x: np.ndarray, sr: int, rise_db: float = 15.0) -> list[int]:
    """Sample positions where the 1 ms level jumps >= rise_db within 3 ms (stroke onsets; protected from de-click)."""
    w = max(1, int(0.001 * sr))
    lv = _frames_db(x, w, w)
    G = lv.max()
    out, last = [], -10 ** 9
    for i in range(3, len(lv)):
        # a stroke keeps sounding (2-6 ms later within 20 dB); a lone click is gone after 1 ms
        if (lv[i] > G - 45 and lv[i] - lv[i - 3] >= rise_db and i - last > 30
                and lv[i + 2:i + 7].max(initial=-200.0) >= lv[i] - 20):
            out.append(i * w)
            last = i
    return out


def declick(x: np.ndarray, sr: int, k: float = 12.0, protect_ms: float = 6.0, protect: list[int] | None = None) -> tuple[np.ndarray, dict]:
    y = x.copy()
    d2 = np.abs(np.diff(x, 2))
    win = int(0.010 * sr)
    pad = np.pad(d2, (win // 2, win - win // 2), mode="edge")
    # local median and MAD of the 2nd difference, by blocks (fast enough for minutes of audio)
    blk = max(1, win // 2)
    med = np.repeat([np.median(pad[i:i + win]) for i in range(0, len(d2), blk)], blk)[:len(d2)]
    mad = np.repeat([np.median(np.abs(pad[i:i + win] - np.median(pad[i:i + win]))) for i in range(0, len(d2), blk)], blk)[:len(d2)]
    hits = np.flatnonzero(d2 > med + k * (mad + 1e-9) * 1.4826)
    prot = np.zeros(len(x), bool)
    pm = int(protect_ms / 1000 * sr)
    for o in (protect if protect is not None else onsets(x, sr)):
        prot[max(0, o - pm):o + pm] = True
    fixed = 0
    i = 0
    while i < len(hits):
        j = i
        while j + 1 < len(hits) and hits[j + 1] - hits[j] <= 1:
            j += 1
        a, b = int(hits[i]) + 1, int(hits[j]) + 2       # spike samples (2nd difference is centred one sample on)
        if b - a <= 3 and not prot[a:b].any() and a > 2 and b + 2 < len(x):
            xs = np.r_[a - 2:a, b:b + 2]
            y[a:b] = np.interp(np.arange(a, b), xs, x[xs])
            fixed += 1
        i = j + 1
    return y, {"spikes_repaired": fixed, "candidates": int(len(hits))}


def _biquad(b: dict, sr: int) -> np.ndarray:
    A = 10 ** (b["db"] / 40)
    w0 = 2 * np.pi * b["hz"] / sr
    alpha = np.sin(w0) / (2 * b.get("q", 0.707))
    c = np.cos(w0)
    if b["type"] == "peak":
        num = [1 + alpha * A, -2 * c, 1 - alpha * A]
        den = [1 + alpha / A, -2 * c, 1 - alpha / A]
    elif b["type"] in ("lowshelf", "highshelf"):
        s = 1 if b["type"] == "lowshelf" else -1
        sq = 2 * np.sqrt(A) * alpha
        num = [A * ((A + 1) - s * (A - 1) * c + sq), s * 2 * A * ((A - 1) - s * (A + 1) * c), A * ((A + 1) - s * (A - 1) * c - sq)]
        den = [(A + 1) + s * (A - 1) * c + sq, -s * 2 * ((A - 1) + s * (A + 1) * c), (A + 1) + s * (A - 1) * c - sq]
    else:
        raise ValueError(f"EQ type {b['type']!r}")
    return signal.tf2sos(np.array(num) / den[0], np.array(den) / den[0])


def eq(x: np.ndarray, sr: int, bands: list[dict]) -> np.ndarray:
    for b in bands or []:
        if b["type"] == "peak" and b["hz"] >= 4000 and b["db"] > 0:
            raise ValueError("no boost in the 4-8 kHz scratch band (owner 29/10)")
        x = signal.sosfilt(_biquad(b, sr), x)
    return x


def quiet_stats(x: np.ndarray, sr: int, pct: float = 15.0) -> dict:
    """Noise floor and 4-8 kHz hiss in the quietest 20 ms frames, dB re the 1 ms peak."""
    n = int(0.020 * sr)
    lv = _frames_db(x, n, n)
    pk = 10 * np.log10(max(np.max(np.convolve(x ** 2, np.ones(int(0.001 * sr)) / int(0.001 * sr), "same")), 1e-20))
    q = np.flatnonzero(lv <= np.percentile(lv, pct))
    hs = signal.sosfilt(signal.butter(4, [4000, 8000], "band", fs=sr, output="sos"), x)
    hiss = [np.mean(hs[i * n:(i + 1) * n] ** 2) for i in q]
    return {"noise_floor_db": round(float(np.mean(lv[q]) - pk), 1),
            "hiss_4k8k_db": round(float(10 * np.log10(np.mean(hiss) + 1e-20) - pk), 1)}


def clean_take(x: np.ndarray, sr: int, params: dict | None = None) -> tuple[np.ndarray, dict]:
    p = {**DEFAULTS, **(params or {})}
    rep = {"before": quiet_stats(x, sr), "params": p}
    y = highpass(x, sr, p["hpf_hz"])
    y, rep["gate"] = spectral_gate(y, sr, **p["gate"])
    y, rep["declick"] = declick(y, sr, **p["declick"])
    y = eq(y, sr, p["eq"])
    rep["after"] = quiet_stats(y, sr)
    rep["chain"] = (f"hpf{p['hpf_hz']:g} zero-phase, spectral gate (noise from the quietest {p['gate']['quiet_pct']:g} % "
                    f"of frames, -{p['gate']['reduction_db']:g} dB), de-click {rep['declick']['spikes_repaired']} spikes "
                    f"(onsets protected), EQ " + ", ".join(f"{b['type']} {b['hz']:g} Hz {b['db']:+g} dB" for b in p["eq"]))
    return y, rep


def stroke_gate(y: np.ndarray, sr: int, threshold_db: float = -48.0, range_db: float = 30.0, attack_ms: float = 0.5,
                release_ms: float = 25.0) -> np.ndarray:
    """Downward expander on one stroke: below (stroke peak + threshold_db) the level falls by up to range_db."""
    env = np.abs(y)
    a = np.exp(-1.0 / (attack_ms / 1000 * sr))
    r = np.exp(-1.0 / (release_ms / 1000 * sr))
    e = np.empty_like(env)
    s = 0.0
    for i, v in enumerate(env):
        s = a * s + (1 - a) * v if v > s else r * s + (1 - r) * v
        e[i] = s
    pk = e.max() + 1e-12
    lvl = 20 * np.log10(e / pk + 1e-12)
    gdb = np.clip(lvl - threshold_db, -range_db, 0.0)      # 1:2 below the threshold, at most range_db
    return y * 10 ** (gdb / 20)
