"""Small loudness/peak meters used by the chain and its report.

The critic lane owns the full QA; these are the few numbers the build chain needs.
All functions take float arrays shaped (n,) or (n, ch).
"""
from __future__ import annotations

import numpy as np
import pyloudnorm as pyln
from scipy import signal

from critic.audio import dc_estimate

EPS = 1e-12


def as2d(x: np.ndarray) -> np.ndarray:
    return x[:, None] if x.ndim == 1 else x


def db(v: float) -> float:
    return float(20 * np.log10(max(abs(v), EPS)))


def sample_peak_db(x: np.ndarray) -> float:
    return db(np.max(np.abs(x))) if x.size else -240.0


def true_peak_db(x: np.ndarray, sr: int = 48000) -> float:
    """BS.1770-4 style true peak: 4x oversampling (8x below 96 kHz would be stricter)."""
    x2 = as2d(x)
    if not x2.size:
        return -240.0
    up = signal.resample_poly(x2, 4, 1, axis=0)
    return db(max(np.max(np.abs(up)), np.max(np.abs(x2))))


def _k_weighted(x: np.ndarray, sr: int) -> np.ndarray:
    z = as2d(x).astype(np.float64).copy()
    meter = pyln.Meter(sr)
    for stage in meter._filters.values():  # pyloudnorm's K-weighting (pinned 0.2.0)
        for ch in range(z.shape[1]):
            z[:, ch] = stage.apply_filter(z[:, ch])
    return z


def sliding_lufs(x: np.ndarray, sr: int, win_s: float, hop_s: float = 0.01) -> np.ndarray:
    """Loudness curve with a `win_s` window; the clip is padded with silence to fit one window."""
    z = _k_weighted(x, sr)
    win = int(round(win_s * sr))
    if z.shape[0] < win:
        z = np.vstack([z, np.zeros((win - z.shape[0], z.shape[1]))])
    hop = max(1, int(round(hop_s * sr)))
    csum = np.vstack([np.zeros((1, z.shape[1])), np.cumsum(z ** 2, axis=0)])
    starts = np.arange(0, z.shape[0] - win + 1, hop)
    ms = (csum[starts + win] - csum[starts]) / win
    power = ms.sum(axis=1)  # channel weights 1.0 (mono/stereo)
    return -0.691 + 10 * np.log10(np.maximum(power, EPS))


def lufs_m_max(x: np.ndarray, sr: int) -> float:
    """Max momentary loudness (400 ms), padded to 0.4 s (§4.3.3)."""
    return float(np.max(sliding_lufs(x, sr, 0.4)))


def lufs_s_max(x: np.ndarray, sr: int) -> float:
    """Max short-term loudness (3 s), padded to 3 s."""
    return float(np.max(sliding_lufs(x, sr, 3.0, 0.1)))


def lufs_i(x: np.ndarray, sr: int) -> float:
    x2 = as2d(x)
    if x2.shape[0] < int(0.4 * sr):
        x2 = np.vstack([x2, np.zeros((int(0.4 * sr) - x2.shape[0], x2.shape[1]))])
    v = pyln.Meter(sr).integrated_loudness(x2)
    return float(v) if np.isfinite(v) else -240.0


def loudness(x: np.ndarray, sr: int, mode: str) -> float:
    if mode == "lufs-m-max":
        return lufs_m_max(x, sr)
    if mode == "lufs-s-max":
        return lufs_s_max(x, sr)
    if mode == "lufs-i":
        return lufs_i(x, sr)
    if mode == "peak":
        return true_peak_db(x, sr)
    raise ValueError(f"unknown loudness mode {mode!r}")


def onset_index(x: np.ndarray, threshold_db: float = -40.0) -> int:
    """First sample whose |x| reaches peak + threshold_db (relative)."""
    a = np.max(np.abs(as2d(x)), axis=1)
    peak = float(a.max()) if a.size else 0.0
    if peak <= EPS:
        return 0
    idx = np.flatnonzero(a >= peak * 10 ** (threshold_db / 20))
    return int(idx[0]) if idx.size else 0


def head_ms(x: np.ndarray, sr: int, threshold_db: float = -40.0) -> float:
    return 1000.0 * onset_index(x, threshold_db) / sr


def summary(x: np.ndarray, sr: int) -> dict:
    """Numbers stored in render.json (raw mix and final file)."""
    x2 = as2d(x)
    mono = x2.mean(axis=1)
    n = x2.shape[0]
    tail = mono[-max(1, int(0.01 * sr)):]
    out = {
        "durationMs": round(1000.0 * n / sr, 2),
        "channels": int(x2.shape[1]),
        "samplePeakDb": round(sample_peak_db(x2), 2),
        "truePeakDbtp": round(true_peak_db(x2, sr), 2),
        "lufsMMax": round(lufs_m_max(x2, sr), 2),
        "lufsSMax": round(lufs_s_max(x2, sr), 2),
        "headMs": round(head_ms(x2, sr), 2),
        "dcPercent": round(100.0 * dc_estimate(x2, sr), 4),          # true DC (critic.audio, §4.3.1)
        "clippedSamples": int(np.sum(np.abs(x2) >= 0.999)),
        "tailDbfs": round(db(float(np.sqrt(np.mean(tail ** 2)))) if n else -240.0, 1),
    }
    if n >= int(0.4 * sr):
        out["lufsI"] = round(lufs_i(x2, sr), 2)
    return out
