"""Seeded synth generators for recipe layers. Each returns mono float64 with peak 1.0.

A generator gets (params, rng, sr). Same params + same seed -> identical samples.
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy import signal

SR = 48000
LN1000 = np.log(1000.0)  # exp decay reaching -60 dB at t60


def _n(ms: float, sr: int) -> int:
    return max(1, int(round(ms * sr / 1000.0)))


def envelope(n: int, sr: int, attack_ms: float, t60_ms: float | None, hold_ms: float = 0.0) -> np.ndarray:
    t = np.arange(n) / sr
    a = max(attack_ms, 0.0) / 1000.0
    h = max(hold_ms, 0.0) / 1000.0
    env = np.ones(n)
    if a > 0:
        rise = t < a
        env[rise] = np.sin(0.5 * np.pi * t[rise] / a) ** 2
    if t60_ms:
        after = t >= a + h
        env[after] *= np.exp(-LN1000 * (t[after] - a - h) / (t60_ms / 1000.0))
    return env


def _noise(color: str, n: int, rng: np.random.Generator) -> np.ndarray:
    w = rng.standard_normal(n)
    if color == "white":
        return w
    spec = np.fft.rfft(w)
    f = np.fft.rfftfreq(n)
    f[0] = f[1] if n > 1 else 1.0
    tilt = {"pink": 0.5, "brown": 1.0, "blue": -0.5}.get(color)
    if tilt is None:
        raise ValueError(f"unknown noise color {color!r}")
    return np.fft.irfft(spec / f ** tilt, n)


def _norm(x: np.ndarray) -> np.ndarray:
    p = float(np.max(np.abs(x))) if x.size else 0.0
    return x / p if p > 0 else x


def _band(x: np.ndarray, sr: int, hp: float | None, lp: float | None, order: int = 2) -> np.ndarray:
    nyq = sr / 2 * 0.98
    if hp:
        x = signal.sosfilt(signal.butter(order, min(hp, nyq), "highpass", fs=sr, output="sos"), x)
    if lp:
        x = signal.sosfilt(signal.butter(order, min(lp, nyq), "lowpass", fs=sr, output="sos"), x)
    return x


def noise_burst(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Shaped noise hit: attack, exponential decay, optional band limits."""
    dur = p.get("durMs", 120.0)
    n = _n(dur, sr)
    x = _noise(p.get("color", "white"), n, rng)
    x = _band(x, sr, p.get("hpHz"), p.get("lpHz"), int(p.get("order", 2)))
    x *= envelope(n, sr, p.get("attackMs", 1.0), p.get("decayMs", dur), p.get("holdMs", 0.0))
    return _norm(x)


def noise_sweep(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Noise through a band (or low-pass) whose centre glides fromHz -> toHz (whoosh, riser)."""
    dur = p.get("durMs", 600.0)
    n = _n(dur, sr)
    x = _noise(p.get("color", "pink"), n, rng)
    nper, hop = 1024, 256
    f, t, z = signal.stft(x, fs=sr, nperseg=nper, noverlap=nper - hop, boundary="even", padded=True)
    frac = np.clip(t / max(dur / 1000.0, 1e-6), 0.0, 1.0) ** p.get("curve", 1.0)
    f0, f1 = float(p.get("fromHz", 300.0)), float(p.get("toHz", 4000.0))
    fc = f0 * (f1 / f0) ** frac                                  # log glide
    ff = np.maximum(f, 1.0)[:, None]
    if p.get("mode", "bandpass") == "lowpass":
        mask = 1.0 / np.sqrt(1.0 + (ff / fc[None, :]) ** (2 * int(p.get("order", 2))))
    else:
        sigma = float(p.get("bwOct", 1.0)) / 2.355
        mask = np.exp(-0.5 * (np.log2(ff / fc[None, :]) / sigma) ** 2)
    _, y = signal.istft(z * mask, fs=sr, nperseg=nper, noverlap=nper - hop, boundary=True)
    y = y[:n] if y.size >= n else np.pad(y, (0, n - y.size))
    shape = p.get("shape", "swell")
    if shape == "swell":   # rise to peakAt, fall to the end
        peak_at = float(p.get("peakAt", 0.6))
        tt = np.arange(n) / n
        env = np.where(tt < peak_at, np.sin(0.5 * np.pi * tt / peak_at) ** 2,
                       np.cos(0.5 * np.pi * (tt - peak_at) / max(1 - peak_at, 1e-6)) ** 2)
    else:
        env = envelope(n, sr, p.get("attackMs", 5.0), p.get("decayMs", dur))
    return _norm(y * env)


def _phase(f_start: float, f_end: float | None, glide_ms: float, n: int, sr: int, curve: str = "exp") -> tuple:
    t = np.arange(n) / sr
    if f_end is None or f_end == f_start or glide_ms <= 0:
        freq = np.full(n, float(f_start))
    else:
        g = np.clip(t / (glide_ms / 1000.0), 0.0, 1.0)
        freq = f_start * (f_end / f_start) ** g if curve == "exp" else f_start + (f_end - f_start) * g
    return 2 * np.pi * np.cumsum(freq) / sr, freq


def _osc(wave: str, phase: np.ndarray, freq: np.ndarray, sr: int) -> np.ndarray:
    if wave == "sine":
        return np.sin(phase)
    # Band-limited additive square/saw/triangle: drop harmonics above 0.45 sr.
    out = np.zeros_like(phase)
    kmax = int(0.45 * sr / max(float(freq.min()), 1.0))
    for k in range(1, max(kmax, 1) + 1):
        if wave == "square" and k % 2 == 0:
            continue
        if wave == "triangle" and k % 2 == 0:
            continue
        amp = {"square": 1.0 / k, "saw": 1.0 / k, "triangle": ((-1) ** ((k - 1) // 2)) / k ** 2}[wave]
        live = (k * freq) < 0.45 * sr
        out += np.where(live, amp * np.sin(k * phase), 0.0)
    return out


def tone(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Sine/square/saw/triangle body with a pitch envelope (glide) and an amplitude envelope."""
    dur = p.get("durMs", 200.0)
    n = _n(dur, sr)
    wave = p.get("wave", "sine")
    if wave not in ("sine", "square", "saw", "triangle"):
        raise ValueError(f"unknown wave {wave!r}")
    ph, freq = _phase(p.get("freqHz", 220.0), p.get("endHz"), p.get("glideMs", 0.0), n, sr, p.get("glide", "exp"))
    ph = ph + rng.uniform(0, 2 * np.pi) * bool(p.get("randomPhase", False))
    x = _osc(wave, ph, freq, sr) * envelope(n, sr, p.get("attackMs", 2.0), p.get("decayMs", dur), p.get("holdMs", 0.0))
    return _norm(x)


def sub_thump(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Sine sub drop (e.g. 110 -> 45 Hz) with optional click and soft drive."""
    dur = p.get("durMs", 220.0)
    n = _n(dur, sr)
    ph, _ = _phase(p.get("startHz", 110.0), p.get("endHz", 45.0), p.get("glideMs", 60.0), n, sr)
    x = np.sin(ph) * envelope(n, sr, p.get("attackMs", 0.5), p.get("decayMs", dur))
    drive = float(p.get("driveDb", 0.0))
    if drive > 0:
        g = 10 ** (drive / 20)
        x = np.tanh(x * g) / np.tanh(g)
    click = float(p.get("click", 0.0))
    if click > 0:
        m = _n(2.0, sr)
        c = _band(rng.standard_normal(m), sr, 1500.0, None) * envelope(m, sr, 0.05, 2.0)
        x[:m] += click * _norm(c)
    return _norm(x)


def fm_ping(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Two-operator FM; an inharmonic ratio and a fast index decay give a metallic ping."""
    dur = p.get("durMs", 400.0)
    n = _n(dur, sr)
    t = np.arange(n) / sr
    fc = float(p.get("carrierHz", 1800.0))
    fm = fc * float(p.get("ratio", 1.41))
    idx_env = float(p.get("index", 4.0)) * np.exp(-LN1000 * t / (p.get("indexDecayMs", 60.0) / 1000.0))
    mod = idx_env * np.sin(2 * np.pi * fm * t + rng.uniform(0, 2 * np.pi) * bool(p.get("randomPhase", False)))
    x = np.sin(2 * np.pi * fc * t + mod)
    x *= envelope(n, sr, p.get("attackMs", 0.3), p.get("decayMs", dur))
    return _norm(_band(x, sr, p.get("hpHz"), p.get("lpHz")))


def click(p: dict, rng: np.random.Generator, sr: int = SR) -> np.ndarray:
    """Very short filtered noise tick (key/UI transient)."""
    dur = p.get("durMs", 5.0)
    n = _n(dur, sr)
    x = _band(rng.standard_normal(n), sr, p.get("hpHz", 2000.0), p.get("lpHz", 12000.0))
    return _norm(x * envelope(n, sr, p.get("attackMs", 0.1), p.get("decayMs", dur)))


GENERATORS: dict[str, Callable[[dict, np.random.Generator, int], np.ndarray]] = {
    "noise_burst": noise_burst,
    "noise_sweep": noise_sweep,
    "tone": tone,
    "sub_thump": sub_thump,
    "fm_ping": fm_ping,
    "click": click,
}


def generate(name: str, params: dict, seed: int, sr: int = SR) -> np.ndarray:
    if name not in GENERATORS:
        raise ValueError(f"unknown synth generator {name!r}; have {sorted(GENERATORS)}")
    rng = np.random.default_rng(np.random.SeedSequence(int(seed)))
    return GENERATORS[name](dict(params or {}), rng, sr)
