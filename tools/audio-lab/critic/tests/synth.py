"""Synthetic test sounds made at test time (no audio files in Git). numpy/scipy only, seeded.

Clean ones go through the plan's fix chain basics (high-pass 35 Hz, fade, peak -3 dBFS) so they
pass L1; each broken one carries exactly one defect.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

SR = 48000


def _t(sec, sr=SR):
    return np.arange(int(sr * sec)) / sr


def norm_peak(x, dbfs):
    return x * (10 ** (dbfs / 20) / (np.max(np.abs(x)) + 1e-12))


def _band(x, lo, hi, sr=SR, order=4):
    if lo is None:
        sos = signal.butter(order, hi, btype="low", fs=sr, output="sos")
    elif hi is None:
        sos = signal.butter(order, lo, btype="high", fs=sr, output="sos")
    else:
        sos = signal.butter(order, [lo, hi], btype="band", fs=sr, output="sos")
    return signal.sosfilt(sos, x)


def fade_out(x, ms, sr=SR):
    n = int(sr * ms / 1000)
    y = x.copy()
    y[-n:] *= np.linspace(1, 0, n)
    return y


def fix_chain(x, fade_ms=30, peak=-3.0, sr=SR):
    y = _band(x, 35, None, sr, order=2)
    return norm_peak(fade_out(y, fade_ms, sr), peak)


def punchy(dur=0.45, seed=1):
    """Layered impact: noise crack + pitch-dropping sine body + mid crunch + short debris tail."""
    rng = np.random.default_rng(seed)
    t = _t(dur)
    crack = np.zeros_like(t)
    n = int(SR * 0.006)
    crack[:n] = _band(rng.standard_normal(n), 1500, 9000) * np.linspace(1, 0, n) ** 2
    f = 48 + (140 - 48) * np.exp(-t / 0.04)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.07)
    body[: int(SR * 0.002)] *= np.linspace(0, 1, int(SR * 0.002))
    crunch = _band(rng.standard_normal(len(t)), 300, 2500) * np.exp(-t / 0.03)
    tail = _band(rng.standard_normal(len(t)), None, 2500) * np.exp(-t / 0.08)
    mix = norm_peak(crack, -3) + norm_peak(body, -4) + norm_peak(crunch, -6) + norm_peak(tail, -16)
    return fix_chain(mix)


def smeared(smear_ms=15.0, dur=0.45, seed=1):
    """The punchy impact with its crack spread over `smear_ms` (diffusion-style smeared onset).

    The sub/body keeps its 2 ms attack, so L1 passes; only the >= 2 kHz layer rises slowly."""
    rng = np.random.default_rng(seed)
    t = _t(dur)
    n = int(SR * smear_ms / 1000)
    env = np.exp(-np.maximum(t - smear_ms / 1000, 0) / 0.008)
    env[:n] = 0.5 - 0.5 * np.cos(np.pi * np.arange(n) / n)
    crack = _band(rng.standard_normal(len(t)), 1500, 9000) * env
    f = 48 + (140 - 48) * np.exp(-t / 0.04)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.07)
    body[: int(SR * 0.002)] *= np.linspace(0, 1, int(SR * 0.002))
    tail = _band(rng.standard_normal(len(t)), None, 2500) * np.exp(-t / 0.08)
    return fix_chain(norm_peak(crack, -5) + norm_peak(body, -4) + norm_peak(tail, -16))


def weak_click():
    """Thin, quiet 3 ms blip in 150 ms: the placeholder sound."""
    x = np.zeros(int(SR * 0.15))
    n = int(SR * 0.003)
    x[:n] = np.sin(2 * np.pi * 3200 * _t(0.003)) * np.hanning(n)
    return norm_peak(x, -24)


def muddy(dur=0.6, seed=2):
    """Fast enough attack (hygiene-clean) but boomy: 70 Hz body, 200-500 Hz build-up, low-passed."""
    rng = np.random.default_rng(seed)
    t = _t(dur)
    f = 70 + 30 * np.exp(-t / 0.2)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.35)
    boom = _band(rng.standard_normal(len(t)), 200, 500) * np.exp(-t / 0.3)
    x = norm_peak(body, -6) + norm_peak(boom, -1)
    x *= np.minimum(1, t / 0.003)            # 3 ms ramp: no crack, but attack under 10 ms
    x = _band(x, None, 600)
    return fix_chain(x, fade_ms=40)


def clipped():
    """The punchy impact slammed +18 dB into a hard clip (written as PCM_16)."""
    return np.clip(punchy() * 8.0, -1.0, 1.0)


def head_silence():
    return np.concatenate([np.zeros(int(SR * 0.25)), punchy(0.3)])


def cut_tail():
    """Truncated at 120 ms with no fade: click at the end."""
    return punchy()[: int(SR * 0.12)]


def slow_attack():
    x = punchy().copy()
    n = int(SR * 0.045)
    x[:n] *= np.linspace(0, 1, n)
    return x


def with_dc():
    return punchy() * 0.9 + 0.01


def loop(seamless=True, dur=2.0, seed=3):
    """2 s drone. Seamless: whole cycles, cos LFO symmetric at the seam, circular noise."""
    rng = np.random.default_rng(seed)
    t = _t(dur)
    base = 55.0 if seamless else 55.37
    x = np.sin(2 * np.pi * base * t) + 0.5 * np.sin(2 * np.pi * base * 2 * t)
    x *= 0.8 + 0.2 * np.cos(2 * np.pi * (4.0 if seamless else 3.7) * t)
    spec = np.fft.rfft(rng.standard_normal(len(t)))
    fr = np.fft.rfftfreq(len(t), 1 / SR)
    spec *= (fr > 800) & (fr < 5000)
    noise = np.fft.irfft(spec, n=len(t))
    x = x + 0.15 * noise / (np.max(np.abs(noise)) + 1e-9)
    if not seamless:
        x *= np.linspace(1.0, 0.55, len(t))
    return norm_peak(x, -4)


def music_loop(bars=8, bpm=96, extra_ms=0.0, click=False):
    """Plucked notes on every beat; exact bar length (+extra_ms). Stereo. Tail decays before the seam."""
    beat = 60.0 / bpm
    n = int(round((bars * 4 * beat + extra_ms / 1000) * SR))
    x = np.zeros(n)
    for k in range(bars * 4):
        i = int(round(k * beat * SR))
        m = min(int(0.3 * SR), n - i)
        tt = np.arange(m) / SR
        x[i:i + m] += np.sin(2 * np.pi * (220 if k % 4 else 110) * tt) * np.exp(-tt / 0.06) * np.minimum(1, tt / 0.002)
    x = norm_peak(x, -6)
    if click:
        x[-200:] = np.linspace(0, 0.4, 200)       # ends high: a jump back to the first sample
    return np.stack([x, x * 0.9], axis=1)


def smooth_lf_crest_16bit():
    """A clean 12 Hz sine at -1 dBFS: its crests round to equal 16-bit values (not clipping)."""
    t = _t(1.0)
    return 0.89 * np.sin(2 * np.pi * 12 * t + 0.3)


def write(path: Path, x, sr=SR, subtype="PCM_24") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), np.asarray(x, dtype=np.float64), sr, subtype=subtype)
    return path


def resample_44k(x):
    return signal.resample_poly(x, 147, 160)


CARDS = """
- id: imp
  game: typing-survival
  group: hit_heavy
- id: loop
  group: ambience
"""


def make_set(root: Path) -> dict[str, Path]:
    """The test set: name -> path. Names start with the card id (imp_*, loop_*)."""
    d = root / "in"
    files = {
        "imp_weak": write(d / "imp_weak.wav", weak_click()),
        "imp_punchy": write(d / "imp_punchy.wav", punchy()),
        "imp_muddy": write(d / "imp_muddy.wav", muddy()),
        "imp_clipped": write(d / "imp_clipped.wav", clipped(), subtype="PCM_16"),
        "imp_head": write(d / "imp_head.wav", head_silence()),
        "imp_cut": write(d / "imp_cut.wav", cut_tail()),
        "imp_slow": write(d / "imp_slow.wav", slow_attack()),
        "imp_dc": write(d / "imp_dc.wav", with_dc()),
        "imp_44k": write(d / "imp_44k.wav", resample_44k(punchy()), sr=44100),
        "imp_stereo": write(d / "imp_stereo.wav", np.stack([punchy(), punchy(seed=5)], axis=1)),
        "imp_smeared": write(d / "imp_smeared.wav", smeared(15.0)),
        "loop_seamless": write(d / "loop_seamless.wav", loop(True)),
        "loop_broken": write(d / "loop_broken.wav", loop(False)),
    }
    (root / "cards.yaml").write_text(CARDS, encoding="utf-8")
    return files


BROKEN = {
    "imp_clipped": "clip_full_scale", "imp_head": "head_silence", "imp_cut": "tail", "imp_slow": "attack",
    "imp_dc": "dc_offset", "imp_44k": "sample_rate", "imp_stereo": "channels", "loop_broken": "loop_seam",
}
CLEAN = {"imp_weak", "imp_punchy", "imp_muddy", "imp_smeared", "loop_seamless"}
FLAGGED_ONLY = {"imp_smeared": "smeared_attack"}     # L1b flags, never blocks
