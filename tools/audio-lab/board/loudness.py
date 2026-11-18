"""Loudness matching for blind listening (§7: louder must never win).

Per file: the critic's LUFS-M max when every file of an item has the same critic key,
else the board's own BS.1770 momentary max (K-weighted, 400 ms, padded like the critic),
else windowed RMS. Gains bring all files of an item to one level, capped so that no file
goes over the true-peak ceiling.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import threading
from pathlib import Path

MEASURE_VERSION = 2        # 2: adds lufs_100ms_max
TARGET_LUFS = -23.0        # level every candidate is matched to (before the cap)
SPREAD_MAX_DB = 2.0        # ours: 100 ms loudness may differ this much after matching on LUFS-M
QUIET_NOTE_DB = 3.0        # an item played this far under the target gets a note on its card
CEILING_DBTP = -1.0        # no file may exceed this after its gain
MAX_BOOST_DB = 36.0        # most a file is turned up (16-bit noise floor stays under about -60 dBFS)
MIN_GOAL_LUFS = -32.0      # an item may play this quiet so its quietest file still matches
# Critic keys, best first (plan §4.3.3 / §7 normalise on LUFS-M max; short-term as second choice).
CRITIC_KEYS = ("lufs_momentary_max", "lufs_m_max", "lufsM_max", "lufs_short_term_max", "lufs_s_max")

_lock = threading.Lock()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _db(x: float) -> float:
    return 20.0 * math.log10(x) if x > 0 else float("-inf")


def measure(path: Path) -> dict:
    """Board measurement of one file (numpy/scipy/soundfile live in the venv)."""
    import numpy as np
    import soundfile as sf
    from scipy import signal

    data, sr = sf.read(str(path), always_2d=True, dtype="float64")
    n, ch = data.shape
    out = {"v": MEASURE_VERSION, "sr": int(sr), "channels": int(ch),
           "duration_ms": round(1000.0 * n / sr, 2) if sr else 0.0}
    if n == 0:
        out.update(peak_db=None, true_peak_db=None, lufs_m_max=None, rms_max_db=None, silent=True)
        return out
    peak = float(np.max(np.abs(data)))
    out["peak_db"] = round(_db(peak), 2) if peak > 0 else None
    # True peak: 4x oversampling (BS.1770 annex 2 style), only for clips up to 60 s.
    tp = peak
    if n <= sr * 60:
        up = signal.resample_poly(data, 4, 1, axis=0)
        tp = max(peak, float(np.max(np.abs(up))))
    out["true_peak_db"] = round(_db(tp), 2) if tp > 0 else None

    win = int(0.4 * sr)
    hop = max(1, int(0.01 * sr))
    pad = np.zeros((win, ch))

    def sliding_max(x: np.ndarray, weights: np.ndarray) -> float:
        xp = np.vstack([pad, x, pad])
        csum = np.vstack([np.zeros((1, ch)), np.cumsum(xp ** 2, axis=0)])
        starts = np.arange(0, xp.shape[0] - win, hop)
        ms = (csum[starts + win] - csum[starts]) / win
        return float(np.max((ms * weights).sum(axis=1)))

    def sliding_max_win(x: np.ndarray, weights: np.ndarray, w: int) -> float:
        p0 = np.zeros((w, ch))
        xp = np.vstack([p0, x, p0])
        csum = np.vstack([np.zeros((1, ch)), np.cumsum(xp ** 2, axis=0)])
        starts = np.arange(0, xp.shape[0] - w, max(1, int(0.005 * sr)))
        ms = (csum[starts + w] - csum[starts]) / w
        return float(np.max((ms * weights).sum(axis=1)))

    # RMS fallback (400 ms window, unweighted, dBFS).
    rms_ms = sliding_max(data, np.full(ch, 1.0 / ch))
    out["rms_max_db"] = round(10 * math.log10(rms_ms), 2) if rms_ms > 0 else None
    try:
        import pyloudnorm as pyln

        meter = pyln.Meter(sr)
        z = data.copy()
        for stage in meter._filters.values():   # same K-weighting as the critic and the PoC
            z = signal.lfilter(stage.b, stage.a, z, axis=0)
        g = np.array([1.0, 1.0, 1.0, 1.41, 1.41][:ch] + [1.0] * max(0, ch - 5))
        m = sliding_max(z, g)
        out["lufs_m_max"] = round(-0.691 + 10 * math.log10(m), 2) if m > 0 else None
        m100 = sliding_max_win(z, g, max(1, int(0.1 * sr)))      # the attack the ear compares first
        out["lufs_100ms_max"] = round(-0.691 + 10 * math.log10(m100), 2) if m100 > 0 else None
    except Exception as exc:  # pragma: no cover - venv always has pyloudnorm
        out["lufs_m_max"] = out["lufs_100ms_max"] = None
        out["lufs_error"] = str(exc)[:200]
    out["silent"] = out["lufs_m_max"] is None and out["rms_max_db"] is None
    return out


class MeasureCache:
    """sha256 -> measurement, persisted as one JSON file (outside the repo)."""

    def __init__(self, path: Path | None):
        self.path = path
        self.data: dict[str, dict] = {}
        if path and path.is_file():
            try:
                self.data = json.loads(path.read_text("utf-8"))
            except (OSError, ValueError):
                self.data = {}
        self.dirty = False

    def get(self, sha: str, path: Path) -> dict:
        with _lock:
            hit = self.data.get(sha)
            if hit and hit.get("v") == MEASURE_VERSION:
                return hit
        m = measure(path)
        with _lock:
            self.data[sha] = m
            self.dirty = True
        return m

    def save(self) -> None:
        if not (self.path and self.dirty):
            return
        with _lock:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            tmp = self.path.with_suffix(".tmp")
            tmp.write_text(json.dumps(self.data, ensure_ascii=False, sort_keys=True), "utf-8")
            os.replace(tmp, self.path)
            self.dirty = False


def critic_value(critic_json: Path | None, sha: str) -> tuple[str, float] | None:
    """(key, LUFS) from a critic JSON next to the file, if it describes this exact file."""
    if not critic_json or not critic_json.is_file():
        return None
    try:
        doc = json.loads(critic_json.read_text("utf-8"))
    except (OSError, ValueError):
        return None
    if isinstance(doc, list):
        doc = doc[0] if len(doc) == 1 and isinstance(doc[0], dict) else None
    if not isinstance(doc, dict):
        return None
    file_sha = doc.get("sha256")
    if not file_sha and isinstance(doc.get("file"), dict):
        file_sha = doc["file"].get("sha256")
    if isinstance(file_sha, str) and len(file_sha) == 64 and file_sha != sha:
        return None
    # Top level first, then common nested blocks; "raw" last (the file played is the stored one).
    scopes = [doc] + [doc[k] for k in ("fixed", "measures", "metrics", "loudness", "l1", "l2", "raw")
                      if isinstance(doc.get(k), dict)]
    for key in CRITIC_KEYS:
        for scope in scopes:
            v = scope.get(key)
            if isinstance(v, (int, float)) and math.isfinite(v):
                return key, float(v)
    return None


def item_gains(files: list[dict], target: float = TARGET_LUFS,
               ceiling: float = CEILING_DBTP) -> tuple[str, list[float], float]:
    """files: [{"measure": {...}, "critic": (key, value) | None}] -> (source, gain_db per file, short_db).

    One goal level for the item: the target, lowered so no file passes the true-peak ceiling and
    (down to MIN_GOAL_LUFS) so the quietest file needs at most MAX_BOOST_DB. short_db > 0 means
    that file still plays that much under the others (it is near silent)."""
    if not files:
        return "none", [], 0.0
    critic = [f.get("critic") for f in files]
    keys = {c[0] for c in critic if c}
    if all(critic) and len(keys) == 1:
        source = "critic:" + keys.pop()
        levels = [c[1] for c in critic]
    elif all(f["measure"].get("lufs_m_max") is not None for f in files):
        source = "board:lufs_m_max"
        levels = [f["measure"]["lufs_m_max"] for f in files]
    else:
        source = "board:rms_max_db"
        levels = [f["measure"].get("rms_max_db") for f in files]
    finite = [(lv, f["measure"].get("true_peak_db")) for lv, f in zip(levels, files) if lv is not None]
    if not finite:
        return source, [0.0] * len(files), 0.0
    level_at_ceiling = [lv + (ceiling - tp) for lv, tp in finite if tp is not None]
    goal = min([target] + level_at_ceiling)
    boost_goal = min(lv for lv, _ in finite) + MAX_BOOST_DB
    if boost_goal < goal:
        goal = max(boost_goal, min(goal, MIN_GOAL_LUFS))
    gains = []
    for lv in levels:
        if lv is None:
            gains.append(0.0)
        else:
            gains.append(round(max(-60.0, min(MAX_BOOST_DB, goal - lv)), 2))
    short = max([0.0] + [goal - lv - g for lv, g in zip(levels, gains) if lv is not None])
    return source, gains, round(short, 2)


def _spread(l100: list, gains: list[float]) -> float | None:
    vals = [lv + g for lv, g in zip(l100, gains) if isinstance(lv, (int, float))]
    return round(max(vals) - min(vals), 2) if len(vals) >= 2 else None


def balance(files: list[dict], target: float = TARGET_LUFS, ceiling: float = CEILING_DBTP) -> dict:
    """item_gains plus a check on the 100 ms loudness (the attack): when LUFS-M matching still leaves
    the files more than SPREAD_MAX_DB apart over 100 ms (a gong against a clang), match on the mean of
    LUFS-M and LUFS 100 ms instead, so the brighter attack does not win by loudness (§7). The spread
    that remains is returned for the rating line (`loudness_spread_100ms_db`)."""
    source, gains, short = item_gains(files, target, ceiling)
    l100 = [f["measure"].get("lufs_100ms_max") for f in files]
    spread = _spread(l100, gains)
    out = {"source": source, "gains": gains, "short_db": short, "spread_100ms_db": spread, "spread_before_db": None}
    if spread is not None and spread > SPREAD_MAX_DB and all(isinstance(v, (int, float)) for v in l100):
        mid = []
        for f, l1 in zip(files, l100):
            lm = f["critic"][1] if f.get("critic") else f["measure"].get("lufs_m_max")
            if not isinstance(lm, (int, float)):
                break
            mid.append({"measure": {**f["measure"], "lufs_m_max": (lm + l1) / 2.0}, "critic": None})
        else:
            _, g2, s2 = item_gains(mid, target, ceiling)
            out.update(source=source + "+100ms", gains=g2, short_db=s2, spread_100ms_db=_spread(l100, g2),
                       spread_before_db=spread)
    levels = []
    for f, g in zip(files, out["gains"]):
        lv = f["critic"][1] if f.get("critic") and "+100ms" not in out["source"] else f["measure"].get("lufs_m_max")
        if isinstance(lv, (int, float)):
            levels.append(lv + g)
    out["played_lufs_m"] = round(float(sorted(levels)[len(levels) // 2]), 2) if levels else None
    return out
