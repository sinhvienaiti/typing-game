"""degrade.py - make controlled bad versions of good sounds for a pairwise critic test.

For each source: <stem>__clipped / __muddy / __thin .wav
  clipped : +18 dB, hard clip at 0 dBFS
  muddy   : 45 ms fade-in (kills transient), +8 dB @ 300 Hz, low-pass 700 Hz
  thin    : high-pass 1.5 kHz (removes body) and -14 dB
A critic is "right" on a pair when it scores the source better than the degraded copy.

Usage: python -I degrade.py OUT_DIR SRC [SRC ...]
"""
import os
import sys
import numpy as np
import soundfile as sf
from scipy import signal
from pedalboard import Pedalboard, PeakFilter, LowpassFilter


def main(out, srcs):
    os.makedirs(out, exist_ok=True)
    for p in srcs:
        x, sr = sf.read(p, always_2d=True, dtype="float32")
        x = x.mean(axis=1)
        stem = os.path.splitext(os.path.basename(p))[0]
        # clipped
        c = np.clip(x * 10 ** (18 / 20), -1, 1)
        # muddy
        n = int(0.045 * sr)
        m = x.copy()
        m[:n] *= np.linspace(0, 1, n)
        m = Pedalboard([PeakFilter(cutoff_frequency_hz=300, gain_db=8, q=0.8),
                        LowpassFilter(cutoff_frequency_hz=700)])(m.astype(np.float32), sr)
        m = m / (np.max(np.abs(m)) + 1e-9) * np.max(np.abs(x))
        # thin
        sos = signal.butter(4, 1500, btype="high", fs=sr, output="sos")
        t = signal.sosfilt(sos, x) * 10 ** (-14 / 20)
        for tag, y in (("clipped", c), ("muddy", m), ("thin", t)):
            sf.write(os.path.join(out, f"{stem}__{tag}.wav"), y.astype(np.float32), sr, subtype="PCM_16")
        print(stem, "ok")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
