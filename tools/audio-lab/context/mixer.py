"""A small offline mixer that behaves like a game's Web Audio graph (BATCH1_BRIEF §3.5, plan §6.1).

Numbers per game come from its audio code (read only). Rồng Giữ Ải (games/dragon-hold/src/audio):
  - mix.ts LEVELS: the pronunciation dip of each bus (world -6, enemies -6, traps -6, ambience -4,
    stingers -2, dragon -3 dB), DUCKS.pronunciation down 80 ms, up 400 ms (setTargetAtTime, tau = ramp / 3);
  - mixer.ts: one forest reverb made in code (0.9 s, the same LCG as forestImpulse), sends per bus
    (world 0.12, enemies 0.14, traps 0.12, stingers 0.16, dragon 0.10, ambience 0), return 0.4;
    master limiter (DynamicsCompressorNode -3 dB, ratio 20, knee 0, attack 2 ms, release 120 ms) and the
    soft clip guard (linear to 0.8, tanh knee to 0.96).
Approximations (said in every report): the compressor is a peak detector with attack/release smoothing and
Chromium's automatic make-up gain, without its 6 ms look-ahead and adaptive release; the convolver uses
Chromium's normalisation of the impulse (RMS power, 0.00125 calibration).

Levels: an event is placed at its card's mix target (`loudness.mix_target`, plan §4.3.3, middle of the range)
before the duck, so every candidate of an id sits at the same level and only the sound differs. The spoken
word (speechSynthesis) is outside the game's graph: it is added after the master, never ducked or limited.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from scipy import signal

SR = 48000
EPS = 1e-12


def db_to_gain(db: float) -> float:
    return float(10 ** (db / 20.0))


# ---------------------------------------------------------------- game profiles

DRAGON_HOLD = {
    "game": "dragon-hold",
    "source": "games/dragon-hold/src/audio/mix.ts, mixer.ts (read 24/10/2026)",
    "buses": {
        "world": {"duck_db": -6.0, "send": 0.12},
        "enemies": {"duck_db": -6.0, "send": 0.14},
        "traps": {"duck_db": -6.0, "send": 0.12},
        "ambience": {"duck_db": -4.0, "send": 0.0},
        "stingers": {"duck_db": -2.0, "send": 0.16},
        "dragon": {"duck_db": -3.0, "send": 0.10},
        "music": {"duck_db": -4.0, "send": 0.18},
    },
    "duck": {"down_s": 0.08, "up_s": 0.4},
    "reverb": {"seconds": 0.9, "return": 0.4},
    "limiter": {"threshold_db": -3.0, "ratio": 20.0, "knee_db": 0.0, "attack_s": 0.002, "release_s": 0.12},
    "guard": {"knee": 0.8, "ceiling": 0.96},
}
PROFILES = {"dragon-hold": DRAGON_HOLD}


# ---------------------------------------------------------------- building blocks

def stereo(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = x[:, None]
    if x.shape[1] == 1:
        return np.repeat(x, 2, axis=1)
    return x[:, :2]


def pan(x: np.ndarray, p: float) -> np.ndarray:
    """Web Audio StereoPannerNode (equal power), for mono and stereo inputs."""
    x = np.asarray(x, dtype=np.float64)
    p = float(np.clip(p, -1.0, 1.0))
    if x.ndim == 1 or x.shape[1] == 1:
        m = x.reshape(-1)
        a = (p + 1.0) / 2.0 * np.pi / 2.0
        return np.stack([m * np.cos(a), m * np.sin(a)], axis=1)
    L, R = x[:, 0], x[:, 1]
    if p <= 0:
        a = (p + 1.0) * np.pi / 2.0
        return np.stack([L + R * np.cos(a), R * np.sin(a)], axis=1)
    a = p * np.pi / 2.0
    return np.stack([L * np.cos(a), R + L * np.sin(a)], axis=1)


def varispeed(x: np.ndarray, cents: float) -> np.ndarray:
    """playbackRate = 2^(cents/1200): pitch and length change together, like the games."""
    if abs(cents) < 0.05:
        return x
    import soxr
    rate = 2 ** (cents / 1200.0)
    y = soxr.resample(np.ascontiguousarray(x, dtype=np.float64), SR * rate, SR, quality="VHQ")
    return y


def forest_impulse(seconds: float = 0.9, sr: int = SR) -> np.ndarray:
    """mixer.ts forestImpulse: the same LCG (seed 7), stereo, darker as it fades, -60 dB at the end."""
    n = int(np.floor(seconds * sr))
    out = np.zeros((n, 2))
    seed = 7
    for ch in range(2):
        low = 0.0
        for i in range(n):
            seed = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
            r = seed / 4294967296.0
            t = i / n
            low += (0.9 - 0.75 * t) * (r * 2 - 1 - low)
            out[i, ch] = low * np.exp(-6.9 * t) * (i / 64.0 if i < 64 else 1.0)
    return out


_IMPULSE: dict[tuple, np.ndarray] = {}


def convolver(x: np.ndarray, seconds: float) -> np.ndarray:
    """ConvolverNode with normalize=true (Chromium CalculateNormalizationScale)."""
    key = (seconds, SR)
    if key not in _IMPULSE:
        _IMPULSE[key] = forest_impulse(seconds, SR)
    ir = _IMPULSE[key]
    power = np.sqrt(np.sum(ir ** 2) / ir.size)
    scale = (1.0 / max(power, 0.000125)) * 0.00125 * (44100.0 / SR)
    y = np.stack([signal.fftconvolve(x[:, c], ir[:, c])[: x.shape[0]] for c in range(2)], axis=1)
    return y * scale


def target_curve(n: int, changes: list[tuple[float, float, float]], start: float = 1.0) -> np.ndarray:
    """AudioParam.setTargetAtTime: from each change time, approach its value with tau (s)."""
    out = np.empty(n)
    v = start
    changes = sorted(changes)
    idx = [int(round(t * SR)) for t, _, _ in changes] + [n]
    out[: max(0, min(n, idx[0]))] = start
    for k, (t, val, tau) in enumerate(changes):
        a, b = max(0, idx[k]), min(n, idx[k + 1])
        if b <= a:
            continue
        tt = np.arange(b - a) / SR
        seg = val + (v - val) * np.exp(-tt / max(tau, 1e-4))
        out[a:b] = seg
        v = seg[-1]
    return out


def _smooth_py(gr: np.ndarray, a_att: float, a_rel: float) -> np.ndarray:
    sm = np.empty_like(gr)
    g = 0.0
    for i in range(gr.size):          # gr <= 0: more negative means more reduction
        c = gr[i]
        g = a_att * g + (1 - a_att) * c if c < g else a_rel * g + (1 - a_rel) * c
        sm[i] = g
    return sm


try:                                   # numba is in the shared venv (librosa); plain Python otherwise
    import numba
    _smooth = numba.njit(cache=False)(_smooth_py)
except Exception:                      # noqa: BLE001
    _smooth = _smooth_py


def compressor(x: np.ndarray, threshold_db: float, ratio: float, attack_s: float, release_s: float,
               knee_db: float = 0.0, makeup: bool = True) -> tuple[np.ndarray, np.ndarray]:
    """(output, gain reduction dB per sample): peak detector, static curve, attack/release smoothing."""
    det = np.max(np.abs(x), axis=1)
    lvl = 20 * np.log10(np.maximum(det, EPS))
    over = lvl - threshold_db
    if knee_db > 0:
        gr = np.where(over <= -knee_db / 2, 0.0,
                      np.where(over >= knee_db / 2, over * (1 / ratio - 1),
                               (1 / ratio - 1) * (over + knee_db / 2) ** 2 / (2 * knee_db)))
    else:
        gr = np.where(over > 0, over * (1 / ratio - 1), 0.0)
    sm = _smooth(np.ascontiguousarray(gr, dtype=np.float64), float(np.exp(-1.0 / (attack_s * SR))),
                 float(np.exp(-1.0 / (release_s * SR))))
    gain = 10 ** (sm / 20.0)
    if makeup:   # Chromium DynamicsCompressorKernel: full-range make-up gain ^0.6
        full = threshold_db + (0.0 - threshold_db) / ratio if threshold_db < 0 else 0.0
        gain = gain * (1.0 / db_to_gain(full)) ** 0.6
    return x * gain[:, None], sm


def guard(x: np.ndarray, knee: float = 0.8, ceiling: float = 0.96) -> np.ndarray:
    a = np.abs(x)
    room = ceiling - knee
    y = np.where(a <= knee, a, knee + room * np.tanh((a - knee) / room))
    return np.sign(x) * y


# ---------------------------------------------------------------- the mix

@dataclass
class Event:
    t: float                    # start (s)
    audio: np.ndarray           # (n,) or (n, 2) at 48 kHz, already at its mix level
    bus: str
    pan: float = 0.0
    label: str = ""
    slot: str = ""
    loop_end: float | None = None   # beds: tile the audio until this time
    fade_in_s: float = 0.0
    fade_out_s: float = 0.0
    level_curve: list[tuple[float, float, float]] = field(default_factory=list)   # bed level ramps (t, gain, tau)


@dataclass
class Voice:
    t_request: float            # the game asks for the word (word complete)
    t_start: float              # the voice starts
    audio: np.ndarray
    word: str = ""
    voice: str = ""


def render(events: list[Event], voices: list[Voice], duration_s: float, profile: dict = DRAGON_HOLD,
           duck_from: str = "request", voice_gain_db: float = 0.0) -> dict:
    """Mix events through buses, duck, reverb, master limiter and guard; add the spoken words after.

    duck_from: "request" (proposed, plan §6.2 step 4: dip from the request) or "voice" (current: when the
    voice starts). Returns the master mix, the game mix without voice, per-bus stems and the GR curve."""
    n = int(round(duration_s * SR))
    buses: dict[str, np.ndarray] = {}
    for ev in events:
        y = stereo(ev.audio) if ev.audio.ndim == 2 and ev.audio.shape[1] == 2 else pan(ev.audio, ev.pan)
        a = int(round(ev.t * SR))
        if a >= n:
            continue
        if ev.loop_end is not None:
            b = min(n, int(round(ev.loop_end * SR)))
            reps = int(np.ceil((b - a) / y.shape[0])) + 1
            y = np.tile(y, (reps, 1))[: b - a]
        y = y[: n - a].copy()
        if ev.fade_in_s > 0:
            k = min(y.shape[0], int(ev.fade_in_s * SR))
            y[:k] *= np.linspace(0, 1, k)[:, None]
        if ev.fade_out_s > 0:
            k = min(y.shape[0], int(ev.fade_out_s * SR))
            y[-k:] *= np.linspace(1, 0, k)[:, None]
        if ev.level_curve:
            curve = target_curve(y.shape[0], [(t - ev.t, v, tau) for t, v, tau in ev.level_curve], start=0.0)
            y *= curve[:, None]
        buf = buses.setdefault(ev.bus, np.zeros((n, 2)))
        buf[a:a + y.shape[0]] += y
    # pronunciation dip per bus
    d = profile["duck"]
    duck_curves: dict[str, np.ndarray] = {}
    for bus, x in buses.items():
        depth = db_to_gain(profile["buses"].get(bus, {}).get("duck_db", 0.0))
        if depth >= 1.0 or not voices:
            duck_curves[bus] = np.ones(n)
            continue
        ch = []
        for v in voices:
            t0 = v.t_request if duck_from == "request" else v.t_start
            t1 = v.t_start + v.audio.shape[0] / SR
            ch += [(t0, depth, d["down_s"] / 3.0), (t1, 1.0, d["up_s"] / 3.0)]
        duck_curves[bus] = target_curve(n, ch, start=1.0)
    stems = {bus: x * duck_curves[bus][:, None] for bus, x in buses.items()}
    dry = sum(stems.values()) if stems else np.zeros((n, 2))
    send = sum(x * profile["buses"].get(bus, {}).get("send", 0.0) for bus, x in stems.items()) if stems else np.zeros((n, 2))
    wet = convolver(send, profile["reverb"]["seconds"]) * profile["reverb"]["return"] if np.any(send) else np.zeros((n, 2))
    lim = profile["limiter"]
    game, gr = compressor(dry + wet, lim["threshold_db"], lim["ratio"], lim["attack_s"], lim["release_s"], lim["knee_db"])
    game = guard(game, profile["guard"]["knee"], profile["guard"]["ceiling"])
    voice = np.zeros((n, 2))
    for v in voices:
        a = int(round(v.t_start * SR))
        if a >= n:
            continue
        y = pan(v.audio, 0.0) * db_to_gain(voice_gain_db)
        y = y[: n - a]
        voice[a:a + y.shape[0]] += y
    return {"mix": game + voice, "game": game, "voice": voice, "stems": stems, "gr_db": gr, "duck": duck_curves,
            "wet": wet}
