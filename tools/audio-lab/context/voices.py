"""Spoken words for test C (plan §6.1): macOS `say` voices, cached as 48 kHz mono WAV.

These recordings only feed test renders on this machine; they are never released or sent anywhere.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

from common import env

DIR = env.WORK / "_context" / "voices"
VOICES = ("Samantha", "Daniel")                     # en_US, en_GB (plan §6.1 C: 2-3 English voices)
WORDS = ("harbor", "lantern", "meadow", "thunder", "willow", "garden", "silver", "orchard")
LUFS_M = -17.0                                       # spoken word level, swept +-6 dB in the metrics


def path_for(voice: str, word: str) -> Path:
    return DIR / f"{voice.lower()}-{word}.wav"


def record(voice: str, word: str) -> Path:
    """Record once with `say`, trim the silence, resample to 48 kHz, set the level."""
    out = path_for(voice, word)
    if out.is_file():
        return out
    if not shutil.which("say"):
        raise RuntimeError("không có lệnh `say` (cần macOS) để ghi giọng đọc")
    DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        aiff = Path(td) / "w.aiff"
        subprocess.run(["say", "-v", voice, "-o", str(aiff), word], check=True, timeout=30)
        x, sr = sf.read(str(aiff), always_2d=True, dtype="float64")
    import soxr
    from build import measure
    x = x.mean(axis=1)
    if sr != 48000:
        x = soxr.resample(x, sr, 48000, quality="VHQ")
    a = np.abs(x)
    idx = np.flatnonzero(a >= a.max() * 10 ** (-50 / 20))
    x = x[max(0, idx[0] - 48):idx[-1] + 480] if idx.size else x
    x = x * 10 ** ((LUFS_M - measure.lufs_m_max(x, 48000)) / 20)
    sf.write(str(out), x.astype(np.float32), 48000, subtype="FLOAT")
    return out


def load(voice: str, word: str) -> np.ndarray:
    x, _ = sf.read(str(record(voice, word)), dtype="float64")
    return x
