"""Generate copyright-free synthetic test sounds for the critic PoC.

Each sound is a deliberate archetype so we can check whether a critic
separates them: weak / punchy / clipped / muddy impacts, plus a seamless
loop and a broken loop, plus a sci-fi zap and a fire whoosh for CLAP
prompt-match tests.

Usage: python -I gen_samples.py <out_dir>
"""
import sys
import os
import numpy as np
import soundfile as sf
from scipy import signal
from pedalboard import (Pedalboard, Compressor, LowpassFilter, HighpassFilter,
                        PeakFilter, Reverb, Distortion, Gain)

SR = 48000
rng = np.random.default_rng(7)


def t_axis(sec):
    return np.arange(int(SR * sec)) / SR


def env_exp(sec, decay_s):
    t = t_axis(sec)
    return np.exp(-t / decay_s)


def norm_peak(x, db):
    p = np.max(np.abs(x)) + 1e-12
    return x * (10 ** (db / 20) / p)


def bandpass(x, lo, hi, order=4):
    sos = signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def lowpass(x, fc, order=4):
    sos = signal.butter(order, fc, btype="low", fs=SR, output="sos")
    return signal.sosfilt(sos, x)


def fade(x, fin_ms=0.0, fout_ms=5.0):
    y = x.copy()
    ni = int(SR * fin_ms / 1000)
    no = int(SR * fout_ms / 1000)
    if ni > 0:
        y[:ni] *= np.linspace(0, 1, ni)
    if no > 0:
        y[-no:] *= np.linspace(1, 0, no)
    return y


def weak_click():
    """Thin, quiet, 3 ms high-passed blip: the 'placeholder' sound."""
    dur = 0.15
    x = np.zeros(int(SR * dur))
    n = int(SR * 0.003)
    blip = np.sin(2 * np.pi * 3200 * t_axis(0.003)) * np.hanning(n)
    x[:n] = blip
    return norm_peak(x, -24)


def punchy_impact():
    """Layered impact: noise transient + pitch-dropping sine body + filtered tail."""
    dur = 1.2
    t = t_axis(dur)
    # 1) transient: 6 ms band-passed noise burst
    tr = np.zeros_like(t)
    n = int(SR * 0.006)
    tr[:n] = bandpass(rng.standard_normal(n), 1500, 9000) * np.linspace(1, 0, n) ** 2
    tr = norm_peak(tr, -3)
    # 2) body: sine sweeping 140 -> 48 Hz with ~120 ms decay
    f = 48 + (140 - 48) * np.exp(-t / 0.05)
    phase = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(phase) * np.exp(-t / 0.09)
    body[: int(SR * 0.002)] *= np.linspace(0, 1, int(SR * 0.002))
    body = norm_peak(body, -4)
    # 3) tail: low-passed noise with ~350 ms decay (debris / room)
    tail = lowpass(rng.standard_normal(len(t)), 2500) * np.exp(-t / 0.35)
    tail = norm_peak(tail, -14)
    # 4) mid crunch: 300 Hz-2.5 kHz noise, 45 ms decay (what survives laptop speakers)
    crunch = bandpass(rng.standard_normal(len(t)), 300, 2500) * np.exp(-t / 0.045)
    crunch = norm_peak(crunch, -4)
    mix = tr + body + tail + crunch
    board = Pedalboard([Compressor(threshold_db=-12, ratio=3, attack_ms=3, release_ms=120),
                        Reverb(room_size=0.25, wet_level=0.08, dry_level=1.0)])
    y = board(mix.astype(np.float32), SR)
    return fade(norm_peak(y, -1.0), 0, 30)


def clipped_harsh(base):
    """Same impact, slammed +18 dB into a hard clipper and a fuzz: broken mastering."""
    y = base * 10 ** (18 / 20)
    y = Pedalboard([Distortion(drive_db=12)])(y.astype(np.float32), SR)
    y = np.clip(y * 3.0, -1.0, 1.0)
    return y


def muddy_low():
    """Soft-attack, boomy, low-passed thump with 200-500 Hz build-up and long boom."""
    dur = 1.6
    t = t_axis(dur)
    f = 70 + 30 * np.exp(-t / 0.2)
    phase = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(phase) * np.exp(-t / 0.6)
    body *= np.minimum(1, t / 0.045)  # 45 ms fade-in: no transient
    noise = lowpass(rng.standard_normal(len(t)), 450) * np.exp(-t / 0.7) * np.minimum(1, t / 0.06)
    mix = norm_peak(body, -3) + norm_peak(noise, -8)
    board = Pedalboard([PeakFilter(cutoff_frequency_hz=300, gain_db=9, q=0.8),
                        LowpassFilter(cutoff_frequency_hz=600),
                        Reverb(room_size=0.8, damping=0.9, wet_level=0.35, dry_level=0.8)])
    y = board(mix.astype(np.float32), SR)
    return fade(norm_peak(y, -1.5), 0, 40)


def industrial_loop(seamless=True):
    """2 s industrial drone/hum loop. Seamless = whole number of cycles + matched ends."""
    dur = 2.0
    t = t_axis(dur)
    # 55 Hz and harmonics complete an integer number of cycles in 2 s -> seamless
    base = 55.0 if seamless else 55.37
    x = (np.sin(2 * np.pi * base * t) + 0.5 * np.sin(2 * np.pi * base * 2 * t)
         + 0.25 * np.sign(np.sin(2 * np.pi * base * 3 * t)) * 0.3)
    # 4 Hz amplitude pulse (8 cycles in 2 s)
    lfo = 0.75 + 0.25 * np.sin(2 * np.pi * (4.0 if seamless else 3.7) * t)
    x *= lfo
    # circular noise: generate in frequency domain so it wraps around
    spec = np.fft.rfft(rng.standard_normal(len(t)))
    freqs = np.fft.rfftfreq(len(t), 1 / SR)
    spec *= (freqs > 800) & (freqs < 5000)
    noise = np.fft.irfft(spec, n=len(t))
    x = x + 0.6 * noise / (np.max(np.abs(noise)) + 1e-9)
    if not seamless:
        x *= np.linspace(1.0, 0.55, len(t))  # level drift -> jump at the seam
    return norm_peak(x, -6)


def scifi_zap():
    dur = 0.35
    t = t_axis(dur)
    f = 2400 * np.exp(-t / 0.06) + 180
    phase = 2 * np.pi * np.cumsum(f) / SR
    x = signal.sawtooth(phase) * np.exp(-t / 0.09)
    x = Pedalboard([LowpassFilter(cutoff_frequency_hz=7000),
                    Reverb(room_size=0.2, wet_level=0.1)])(x.astype(np.float32), SR)
    return fade(norm_peak(x, -2), 1, 10)


def fire_whoosh():
    dur = 1.8
    t = t_axis(dur)
    n = rng.standard_normal(len(t))
    # sweeping band-pass via short-block filtering
    out = np.zeros_like(n)
    blk = 1024
    for i in range(0, len(n), blk):
        c = 300 + 2200 * np.sin(np.pi * min(1, i / len(n)))
        sos = signal.butter(2, [c * 0.5, c * 1.8], btype="band", fs=SR, output="sos")
        out[i:i + blk] = signal.sosfilt(sos, n[i:i + blk])
    envl = np.sin(np.pi * t / dur) ** 1.5
    crackle = (rng.random(len(t)) > 0.9993) * rng.standard_normal(len(t)) * 3
    crackle = bandpass(crackle, 2000, 8000)
    x = out * envl + crackle * envl
    x = Pedalboard([Reverb(room_size=0.5, wet_level=0.2)])(x.astype(np.float32), SR)
    return fade(norm_peak(x, -3), 20, 50)


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    punch = punchy_impact()
    sounds = {
        "syn_weak_click": weak_click(),
        "syn_punchy_impact": punch,
        "syn_clipped_harsh": clipped_harsh(punch),
        "syn_muddy_low": muddy_low(),
        "syn_loop_seamless": industrial_loop(True),
        "syn_loop_broken": industrial_loop(False),
        "syn_scifi_zap": scifi_zap(),
        "syn_fire_whoosh": fire_whoosh(),
    }
    for name, x in sounds.items():
        x = np.asarray(x, dtype=np.float64)
        sf.write(os.path.join(out_dir, name + ".wav"), x, SR, subtype="FLOAT" if "clipped" not in name else "PCM_16")
        print(name, f"{len(x)/SR:.2f}s peak={20*np.log10(np.max(np.abs(x))+1e-12):.1f}dBFS")


if __name__ == "__main__":
    main(sys.argv[1])
