"""MoSQITo sharpness (DIN 45692, acum) and roughness (Daniel & Weber, asper) for L2.

Run on the active part, at most 2 s, after normalising to LUFS-M max -20 (the §4.3.3 common
level) with 1.0 FS = 1 Pa, so values compare across candidates. Unavailable -> reported, not fatal.
"""
from __future__ import annotations

import contextlib
import io
import time

import numpy as np

from . import audio as A
from .audio import fnum
from .thresholds import L2

try:  # optional dependency
    import mosqito as _mq
    from mosqito import roughness_dw, sharpness_din_st
    AVAILABLE, WHY = True, ""
except Exception as e:  # pragma: no cover
    AVAILABLE, WHY = False, f"MoSQITo không dùng được: {e!r}"


def measure(mono: np.ndarray, sr: int, onset_s: float, lufs_m_max: float | None) -> dict:
    if not AVAILABLE:
        return {"available": False, "reason": WHY}
    t0 = time.time()
    x = mono[int(max(0.0, onset_s - 0.005) * sr):]
    t, r = A.frame_rms(x, sr, 10.0, 10.0)
    lv = A.pdb(r ** 2)
    act = np.where(lv >= lv.max() - 40)[0]
    end = int(min(len(x), (t[act[-1]] + 0.01) * sr if len(act) else len(x)))
    x = x[: min(end, int(L2["psycho_max_s"] * sr))]
    if lufs_m_max is not None:
        x = x * 10 ** ((L2["norm_lufs_m"] - lufs_m_max) / 20)
    x = A.resample(x, sr, 48000)
    out: dict = {"available": True, "version": getattr(_mq, "__version__", "?"),
                 "calibration": "LUFS-M max −20, 1,0 FS = 1 Pa", "seconds": fnum(len(x) / 48000, 3),
                 "roughness_seconds": fnum(min(len(x) / 48000, L2["roughness_max_s"]), 3)}
    sink = io.StringIO()
    try:
        with contextlib.redirect_stdout(sink):
            out["sharpness_acum"] = fnum(sharpness_din_st(x, 48000), 3)
    except Exception as e:
        out["sharpness_acum"] = None
        out["sharpness_error"] = repr(e)[:200]
    try:
        # roughness is slow (~1.4 s per second of audio): first 0.5 s of the active part only
        y = x[: int(L2["roughness_max_s"] * 48000)]
        y = y if len(y) >= int(0.25 * 48000) else np.pad(y, (0, int(0.25 * 48000) - len(y)))
        with contextlib.redirect_stdout(sink):
            R, _, _, _ = roughness_dw(y, 48000, overlap=0.0)
        R = np.asarray(R, dtype=float)
        out["roughness_asper"] = fnum(np.mean(R), 4)
        out["roughness_max_asper"] = fnum(np.max(R), 4)
    except Exception as e:
        out["roughness_asper"] = None
        out["roughness_error"] = repr(e)[:200]
    out["time_s"] = fnum(time.time() - t0, 3)
    return out
