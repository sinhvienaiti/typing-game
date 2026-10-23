"""Deterministic DSP helpers for layers and the final chain (numpy/scipy/soxr; float64)."""
from __future__ import annotations

import numpy as np
import soxr
from scipy import signal

from build import measure

SR = 48000


def ms_to_n(ms: float, sr: int = SR) -> int:
    return max(0, int(round(ms * sr / 1000.0)))


def db_to_gain(db: float) -> float:
    return float(10 ** (db / 20.0))


def as2d(x: np.ndarray) -> np.ndarray:
    return x[:, None] if x.ndim == 1 else x


def resample(x: np.ndarray, sr_in: float, sr_out: float) -> np.ndarray:
    if abs(sr_in - sr_out) < 1e-9:
        return x
    return soxr.resample(as2d(x), sr_in, sr_out, quality="VHQ")


def to_channels(x: np.ndarray, channels: int) -> tuple[np.ndarray, str]:
    """Mono rule of §5.1: mid if the fold-down loses <= 3 dB, else the stronger channel."""
    x = as2d(x)
    if x.shape[1] == channels:
        return x, "as-is"
    if channels == 2:
        return np.repeat(x[:, :1], 2, axis=1), "dual-mono"
    if x.shape[1] == 1:
        return x, "as-is"
    mid = x.mean(axis=1, keepdims=True)
    e_mid = float(np.sum(mid ** 2))
    e_lr = float(np.mean(np.sum(x ** 2, axis=0)))
    loss_db = 10 * np.log10(max(e_lr, 1e-20) / max(e_mid, 1e-20))
    if loss_db <= 3.0:
        return mid, "mid"
    best = int(np.argmax(np.sum(x ** 2, axis=0)))
    return x[:, best:best + 1], f"channel-{best}"


def pitch_varispeed(x: np.ndarray, semitones: float, sr: int = SR) -> np.ndarray:
    """Tape-style pitch change (length changes too), as WebAudio playbackRate does."""
    if abs(semitones) < 1e-9:
        return x
    rate = 2 ** (semitones / 12.0)
    return soxr.resample(as2d(x), sr, sr / rate, quality="VHQ")


def pitch_preserve(x: np.ndarray, semitones: float, sr: int = SR) -> np.ndarray:
    """Length-preserving pitch shift (pedalboard PitchShift, GPL, local only)."""
    if abs(semitones) < 1e-9:
        return x
    import pedalboard  # local import: GPL tool, only ever imported

    y = pedalboard.PitchShift(semitones=float(semitones))(as2d(x).T.astype(np.float32), sr)
    return y.T.astype(np.float64)


def fade(x: np.ndarray, in_ms: float = 0.0, out_ms: float = 0.0, sr: int = SR, curve: str = "cos") -> np.ndarray:
    x = as2d(x).copy()
    n = x.shape[0]
    for length, rising in ((ms_to_n(in_ms, sr), True), (ms_to_n(out_ms, sr), False)):
        length = min(length, n)
        if length <= 0:
            continue
        t = np.linspace(0.0, 1.0, length, endpoint=True)
        ramp = np.sin(0.5 * np.pi * t) ** 2 if curve == "cos" else t
        if rising:
            x[:length] *= ramp[:, None]
        else:
            x[n - length:] *= ramp[::-1][:, None]
    return x


def _sos(spec: dict, sr: int) -> np.ndarray:
    kind = spec["type"]
    order = int(spec.get("order", 2))
    nyq = sr / 2.0
    if kind in ("highpass", "lowpass"):
        hz = min(float(spec["hz"]), nyq * 0.98)
        return signal.butter(order, hz, btype=kind, fs=sr, output="sos")
    if kind == "bandpass":
        lo, hi = float(spec["lowHz"]), min(float(spec["highHz"]), nyq * 0.98)
        return signal.butter(order, [lo, hi], btype="bandpass", fs=sr, output="sos")
    # RBJ cookbook biquads.
    f0 = min(float(spec["hz"]), nyq * 0.98)
    gain = float(spec.get("gainDb", 0.0))
    q = float(spec.get("q", 0.7071))
    a = 10 ** (gain / 40.0)
    w0 = 2 * np.pi * f0 / sr
    cw, sw = np.cos(w0), np.sin(w0)
    alpha = sw / (2 * q)
    if kind == "peak":
        b = [1 + alpha * a, -2 * cw, 1 - alpha * a]
        den = [1 + alpha / a, -2 * cw, 1 - alpha / a]
    elif kind in ("lowshelf", "highshelf"):
        sq = 2 * np.sqrt(a) * alpha
        s = 1 if kind == "lowshelf" else -1
        b = [a * ((a + 1) - s * (a - 1) * cw + sq), s * 2 * a * ((a - 1) - s * (a + 1) * cw),
             a * ((a + 1) - s * (a - 1) * cw - sq)]
        den = [(a + 1) + s * (a - 1) * cw + sq, -s * 2 * ((a - 1) + s * (a + 1) * cw),
               (a + 1) + s * (a - 1) * cw - sq]
    else:
        raise ValueError(f"unknown filter type {kind!r}")
    b, den = np.asarray(b) / den[0], np.asarray(den) / den[0]
    return np.concatenate([b, den])[None, :]


def apply_filters(x: np.ndarray, filters: list[dict] | None, sr: int = SR) -> np.ndarray:
    """Causal IIR filters (no pre-ringing ahead of the attack)."""
    x = as2d(x)
    for spec in filters or ():
        x = signal.sosfilt(_sos(spec, sr), x, axis=0)
    return x


def trim(x: np.ndarray, start_ms: float = 0.0, end_ms: float | None = None, sr: int = SR) -> np.ndarray:
    x = as2d(x)
    a = ms_to_n(start_ms, sr)
    b = x.shape[0] if end_ms is None else min(x.shape[0], ms_to_n(end_ms, sr))
    return x[a:max(a, b)]


def place(mix: np.ndarray, layer: np.ndarray, offset: int) -> np.ndarray:
    """Add `layer` into `mix` at sample `offset` (grows mix; negative offset cuts the layer head)."""
    layer = as2d(layer)
    if offset < 0:
        layer, offset = layer[-offset:], 0
    end = offset + layer.shape[0]
    if end > mix.shape[0]:
        mix = np.vstack([mix, np.zeros((end - mix.shape[0], mix.shape[1]))])
    mix[offset:end] += layer
    return mix


def head_trim(x: np.ndarray, threshold_db: float, pre_roll_ms: float, sr: int = SR) -> tuple[np.ndarray, int]:
    """Cut silence before the onset, keep `pre_roll_ms`, fade that pre-roll in."""
    onset = measure.onset_index(x, threshold_db)
    pre = ms_to_n(pre_roll_ms, sr)
    cut = max(0, onset - pre)
    y = as2d(x)[cut:].copy()
    if onset - cut > 1:
        y = fade(y, in_ms=1000.0 * (onset - cut) / sr, sr=sr)
    return y, cut


def tail_trim(x: np.ndarray, floor_db: float, sr: int = SR, keep_ms: float = 5.0) -> np.ndarray:
    """Drop the tail once a 5 ms RMS envelope stays below `floor_db` relative to the peak."""
    x = as2d(x)
    mono = np.max(np.abs(x), axis=1)
    peak = float(mono.max()) if mono.size else 0.0
    if peak <= 0:
        return x
    win = max(1, ms_to_n(5.0, sr))
    env = np.sqrt(np.convolve(mono ** 2, np.ones(win) / win, mode="same"))
    above = np.flatnonzero(env >= peak * 10 ** (floor_db / 20.0))
    if not above.size:
        return x
    end = min(x.shape[0], int(above[-1]) + ms_to_n(keep_ms, sr))
    return x[:end]


def saturate(x: np.ndarray, drive_db: float, mix: float = 1.0) -> np.ndarray:
    """Gentle tanh saturation; output peak matches input peak before blending."""
    if drive_db <= 0 or mix <= 0:
        return x
    g = db_to_gain(drive_db)
    peak = float(np.max(np.abs(x))) or 1.0
    wet = np.tanh(x / peak * g) / np.tanh(g) * peak
    return (1 - mix) * x + mix * wet


def loop_crossfade(x: np.ndarray, xf_ms: float, sr: int = SR) -> np.ndarray:
    """Equal-power crossfade of the last `xf_ms` into the head; result loops seamlessly."""
    x = as2d(x)
    n = ms_to_n(xf_ms, sr)
    if n <= 0 or 2 * n >= x.shape[0]:
        return x
    t = np.linspace(0.0, 1.0, n, endpoint=False)[:, None]
    body = x[: x.shape[0] - n].copy()
    body[:n] = x[:n] * np.sin(0.5 * np.pi * t) + x[x.shape[0] - n:] * np.cos(0.5 * np.pi * t)
    return body
