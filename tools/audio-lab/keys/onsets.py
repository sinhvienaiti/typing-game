"""Find every tap in a keyboard take and measure it (typing-feel natural-v1, TYPING_FEEL_SERVICE.md §3.9).

The detector of tmp/keys-firefly/raindrop/analyse.py (owner's raindrop and hail-stone sets, 30/10/2026) made a
module. Same numbers, same rounding: natural.py cuts the sets from these rows, so changing anything here changes
every set it formats. Read-only on the source.

  run.sh keys/onsets.py <take.wav> <hits.json>
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import numpy as np

SR = 48000

# Onset rule (analyse.py): a rise to 18 dB above the floor after at least 25 ms under floor + 10 dB.
ONSET_DB = 18.0
QUIET_DB = 10.0
QUIET_MS = 25.0
STEP_BACK_DB = 6.0          # step back to the first sample above floor + 6 dB
MIN_APART_MS = 10.0         # a step-back landing within 10 ms of the previous hit makes no new hit
HOLD_MS = 15.0              # skip 15 ms after a hit
FLOOR_PERCENTILE = 10
ENV_MS = 2.0                # onset envelope
DECAY_ENV_MS = 3.0          # per-hit envelope for decay40Ms
CLIP = 0.99                 # `clipped` = a sample above 0.99 (not a clip test, see §3.8)


class DecodeError(RuntimeError):
    pass


def ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if not exe:
        raise DecodeError("ffmpeg is not on this machine's PATH; install it (brew install ffmpeg), then run "
                          "`bash tools/audio-lab/common/setup.sh` on this machine.")
    return exe


def decode(path: str | Path, channels: int = 2, sr: int = SR) -> np.ndarray:
    """Float64 frames (n, channels) at `sr`, through ffmpeg, as the prototypes did (bit-exact for 48 kHz PCM)."""
    proc = subprocess.run([ffmpeg(), "-v", "error", "-nostdin", "-i", str(path), "-f", "f64le", "-ac", str(channels),
                           "-ar", str(sr), "pipe:1"], capture_output=True)
    if proc.returncode != 0:
        msg = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        raise DecodeError(f"ffmpeg could not decode {Path(path).name}: {msg[-1] if msg else 'unknown error'}")
    return np.frombuffer(proc.stdout, dtype="<f8").reshape(-1, channels)


def env_db(x: np.ndarray, win: int) -> np.ndarray:
    e = np.sqrt(np.convolve(x * x, np.ones(win) / win, mode="same"))
    return 20 * np.log10(np.maximum(e, 1e-9))


def find_onsets(fast: np.ndarray, floor: float, sr: int = SR) -> list[int]:
    """Sample index of every hit (analyse.py loop, unchanged)."""
    thr_on, thr_quiet = floor + ONSET_DB, floor + QUIET_DB
    quiet_need, hold, apart = round(QUIET_MS / 1000 * sr), round(HOLD_MS / 1000 * sr), round(MIN_APART_MS / 1000 * sr)
    hits: list[int] = []
    quiet_run, i, n = 0, 0, len(fast)
    vals = fast.tolist()                        # plain floats: same comparisons, faster loop
    while i < n:
        v = vals[i]
        if v < thr_quiet:
            quiet_run += 1
        elif v > thr_on:
            if quiet_run >= quiet_need:
                j = i
                while j > 0 and vals[j] > floor + STEP_BACK_DB:
                    j -= 1
                if not hits or j > hits[-1] + apart:
                    hits.append(j)
                i += hold
            quiet_run = 0
        # values between the two thresholds (the rise or the tail) keep the quiet count
        i += 1
    return hits


def measure(stereo: np.ndarray, hits: list[int], sr: int = SR) -> list[dict]:
    mono = stereo.mean(axis=1)
    peak = float(np.abs(mono).max())
    rows = []
    for n, on in enumerate(hits):
        nxt = hits[n + 1] if n + 1 < len(hits) else len(mono)
        seg = mono[on:nxt]
        pk = float(np.abs(seg).max())
        pk_db = 20 * np.log10(pk / peak)
        e = env_db(seg, round(DECAY_ENV_MS / 1000 * sr))
        top = int(np.argmax(e))
        after = np.where(e[top:] < e[top] - 40)[0]
        decay_ms = (top + after[0]) / sr * 1000 if after.size else None   # None: rings into the next hit
        w = min(len(seg), round(.06 * sr))
        spec = np.abs(np.fft.rfft(seg[:round(.06 * sr)] * np.hanning(w)))
        f = np.fft.rfftfreq(w, 1 / sr)
        centroid = float((spec * f).sum() / max(spec.sum(), 1e-9))
        bands = {k: float((spec[(f >= lo) & (f < hi)] ** 2).sum()) for k, (lo, hi) in
                 {"low": (0, 500), "mid": (500, 2000), "high": (2000, 6000), "air": (6000, 24000)}.items()}
        tot = sum(bands.values()) or 1
        rows.append({"n": n, "onsetMs": round(on / sr * 1000, 1), "gapToNextMs": round((nxt - on) / sr * 1000, 1),
                     "peakDb": round(pk_db, 1), "decay40Ms": None if decay_ms is None else round(decay_ms, 1),
                     "centroidHz": round(centroid), "bands": {k: round(v / tot, 3) for k, v in bands.items()},
                     "clipped": bool(np.abs(stereo[on:nxt]).max() > CLIP)})
    return rows


def detect(stereo: np.ndarray, sr: int = SR) -> dict:
    """{'floorDb', 'hits': [...]} exactly as analyse.py wrote hits.json."""
    if sr != SR:
        raise ValueError(f"onsets work at {SR} Hz; decode() resamples")
    mono = stereo.mean(axis=1)
    if not np.any(mono):
        return {"floorDb": -180.0, "hits": []}
    fast = env_db(mono, round(ENV_MS / 1000 * sr))
    floor = float(np.percentile(fast, FLOOR_PERCENTILE))
    rows = measure(stereo, find_onsets(fast, floor, sr), sr)
    return {"floorDb": round(floor, 1), "hits": rows}


def analyse(path: str | Path) -> dict:
    return detect(decode(path))


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print("usage: run.sh keys/onsets.py <take.wav> <hits.json>", file=sys.stderr)
        return 2
    data = analyse(argv[0])
    Path(argv[1]).write_text(json.dumps(data, indent=1))
    print(f"floor {data['floorDb']:.1f} dB, {len(data['hits'])} hits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
