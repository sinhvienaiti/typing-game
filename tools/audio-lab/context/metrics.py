"""Numbers of a context render (BATCH1_BRIEF §3.5, plan §6.1 C, D, F and §6.2)."""
from __future__ import annotations

import numpy as np

from build import measure
from critic import audio as A

SR = 48000
EPS = 1e-12


def _mono(x: np.ndarray) -> np.ndarray:
    return x.mean(axis=1) if x.ndim == 2 else x


def band_db(x: np.ndarray, lo: float, hi: float, t0: float, t1: float) -> float:
    m = _mono(x)
    a, b = max(0, int(t0 * SR)), min(m.shape[0], int(t1 * SR))
    if b <= a:
        return -240.0
    y = A.band(m[max(0, a - 2400):min(m.shape[0], b + 2400)], SR, lo, hi)
    off = a - max(0, a - 2400)
    seg = y[off:off + (b - a)]
    return float(10 * np.log10(np.mean(seg ** 2) + EPS))


def voice_clarity(game: np.ndarray, voice: np.ndarray, starts: list[float], window_s: float = 0.3) -> dict:
    """Test C: the spoken word over the rest in 1-4 kHz, first 300 ms of each word (pass >= 10 dB)."""
    rows = []
    for t in starts:
        v = band_db(voice, 1000, 4000, t, t + window_s)
        g = band_db(game, 1000, 4000, t, t + window_s)
        rows.append(round(v - g, 1))
    return {"per_word_db": rows, "min_db": min(rows) if rows else None,
            "median_db": float(np.median(rows)) if rows else None, "pass_10db": bool(rows and min(rows) >= 10.0)}


def band_decay(x: np.ndarray, lo: float = 1000, hi: float = 4000, after_ms: float = 100.0) -> dict:
    """Plan §6.2: energy in 1-4 kHz falls >= 15 dB within 100 ms of the onset (word-complete sounds)."""
    m = _mono(x)
    y = A.band(m, SR, lo, hi)
    hop = int(0.005 * SR)
    win = int(0.010 * SR)
    fr = np.array([np.mean(y[i:i + win] ** 2) for i in range(0, max(1, y.shape[0] - win), hop)])
    db = 10 * np.log10(fr + EPS)
    env_all = 10 * np.log10(np.array([np.mean(m[i:i + win] ** 2) for i in range(0, max(1, m.shape[0] - win), hop)]) + EPS)
    on = int(np.argmax(env_all >= env_all.max() - 30))                 # onset frame of the whole sound
    pk = on + int(np.argmax(db[on:on + 10]))                             # band peak within 50 ms of it
    at = on + int(round(after_ms / 5.0))
    level = float(db[at]) if at < db.size else -240.0
    drop = float(db[pk] - level)
    return {"onset_ms": on * 5.0, "peak_ms": pk * 5.0, "drop_db_at_100ms": round(drop, 1), "pass_15db": drop >= 15.0}


def small_speaker_loss(stem: np.ndarray) -> float | None:
    """Plan §6.1 F: loudness lost through a 200 Hz high-pass (LUFS-M max)."""
    if not np.any(stem):
        return None
    from scipy import signal
    sos = signal.butter(2, 200, "highpass", fs=SR, output="sos")
    hp = signal.sosfilt(sos, stem, axis=0)
    return round(measure.lufs_m_max(stem, SR) - measure.lufs_m_max(hp, SR), 1)


def limiter_stats(gr_db: np.ndarray) -> dict:
    return {"max_gr_db": round(float(-gr_db.min()), 2) if gr_db.size else 0.0,
            "time_over_3db_pct": round(100.0 * float(np.mean(gr_db <= -3.0)), 2)}


def mix_numbers(mix: np.ndarray) -> dict:
    return {"true_peak_dbtp": round(measure.true_peak_db(mix, SR), 2), "lufs_i": round(measure.lufs_i(mix, SR), 2),
            "lufs_s_max": round(measure.lufs_s_max(mix, SR), 2), "lufs_m_max": round(measure.lufs_m_max(mix, SR), 2),
            "clipped": int(np.sum(np.abs(mix) >= 0.999))}


def slot_share(stems: dict, slot_stem: np.ndarray, lo: float, hi: float) -> float | None:
    """How much of a band the slot's own sound holds in the game mix (not used for pass/fail)."""
    total = sum(stems.values())
    if not np.any(total):
        return None
    a = band_db(slot_stem, lo, hi, 0, slot_stem.shape[0] / SR)
    b = band_db(total, lo, hi, 0, total.shape[0] / SR)
    return round(a - b, 1)
