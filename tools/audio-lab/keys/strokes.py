"""Model takes -> single keystrokes (press, then the key's release when the take has one).

A Stable Audio 3 take (a 1 s single stroke or a 10 s typing passage) is folded to mono (plan §5.1 rule),
high-passed at 30 Hz and resampled to 48 kHz (soxr VHQ). Its sound components are runs of the 5 ms
level above (file peak - 45 dB); each has a true onset (first 1 ms frame within 30 dB of its own peak)
and an end (5 ms level 40 dB under its peak).

A stroke is a press with quiet before it (30..1 ms before the onset >= 35 dB under the press; a file
start only with evidence, as gen/process.py) and, when the take has one, its release: the next
component 35..240 ms later, quieter than the press, starting after the press has decayed 20 dB, and
followed by >= 30 ms of quiet. A press with >= 80 ms of quiet after it and no release is a press-only
stroke. Anything else (overlapping keys, a release that runs into the next key) is skipped with its
reason.

Window: from 1 ms before the onset (faded in over that 1 ms, so the attack starts inside the first
2 ms), to the end of the release (or press) + 5 ms. When that is longer than the part's cap
(keys 180 ms, spacebar 260 ms) the silent gap between press and release is shortened (only where the
5 ms level is 40 dB under the press, never under 50 ms from press to release, 2 ms crossfade): the
hold time of a real finger varies, the two sounds stay whole. If it still does not fit, the stroke
is skipped. The tail gets the shared exponential cap (build.dsp.exp_cap_tail) to -60 dB.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field

import numpy as np
from scipy import signal

from build import dsp
from gen.process import envelope

SR = 48000
CAP_MS = {"key": 180.0, "space": 260.0}
MIN_MS = {"key": 40.0, "space": 60.0}


@dataclass
class Comp:
    onset: int
    peak: int
    peak_db: float
    end: int


@dataclass
class Stroke:
    take: str
    index: int
    onset: int                 # sample in the 48 kHz take
    press_peak_db: float
    press_end: int
    release_onset: int | None = None
    release_peak_db: float | None = None
    release_end: int | None = None
    kind: str = "press+release"
    start_kind: str = "quiet"  # quiet | file-start
    notes: list[str] = field(default_factory=list)

    @property
    def gap_ms(self) -> float | None:
        return None if self.release_onset is None else (self.release_onset - self.onset) / SR * 1000

    @property
    def release_rel_db(self) -> float | None:
        return None if self.release_peak_db is None else self.release_peak_db - self.press_peak_db


def prepare(x: np.ndarray, sr: int) -> tuple[np.ndarray, dict]:
    """Take (n, ch) float -> mono 48 kHz float64, HPF 30 Hz (zero phase)."""
    x2 = dsp.as2d(np.asarray(x, dtype=np.float64))
    corr = None
    if x2.shape[1] == 2 and np.std(x2[:, 0]) > 0 and np.std(x2[:, 1]) > 0:
        corr = float(np.corrcoef(x2[:, 0], x2[:, 1])[0, 1])
    mono, how = dsp.to_channels(x2, 1)
    m = mono[:, 0]
    m = signal.sosfiltfilt(signal.butter(2, 30.0, "high", fs=sr, output="sos"), m)
    m = dsp.resample(m, sr, SR)[:, 0]
    return m, {"stereo_corr": None if corr is None else round(corr, 4), "mono": how, "hpf_hz": 30, "sr_in": sr}


def components(m: np.ndarray, span_db: float = 35.0, prominence_db: float = 15.0) -> tuple[list[Comp], float]:
    """Sound components: peaks of the 5 ms level (prominence >= 15 dB, >= 15 ms apart, within 35 dB of the
    file peak), split at the valley between two peaks. A finger touching the cap 5-15 ms before the
    bottom-out is part of the press (no 15 dB valley); a press and its release are two components."""
    st1, e1 = envelope(m, SR, 1.0, 0.25)
    st5, e5 = envelope(m, SR, 5.0, 1.0)
    G = float(e1.max())
    pk5, _ = signal.find_peaks(e5, prominence=prominence_db, distance=15)
    pk5 = [int(p) for p in pk5 if e5[p] >= float(e5.max()) - span_db]
    bounds = [0]
    for p, q in zip(pk5, pk5[1:]):
        bounds.append(p + int(np.argmin(e5[p:q + 1])))
    bounds.append(len(e5))
    out: list[Comp] = []
    for k, p in enumerate(pk5):
        a5, b5 = bounds[k], bounds[k + 1]
        lo, hi = int(st5[a5]), int(st5[min(b5, len(st5) - 1)]) + int(0.005 * SR)
        f0 = int(np.searchsorted(st1, lo))
        f1 = max(int(np.searchsorted(st1, int(st5[p]) + int(0.006 * SR))), f0 + 1)
        pk = f0 + int(np.argmax(e1[f0:f1]))
        pk_db = float(e1[pk])
        above = np.flatnonzero(e1[f0:pk + 1] > pk_db - 30.0)
        on = int(st1[f0 + int(above[0])]) if above.size else int(st1[f0])
        below = np.flatnonzero(e5[p:b5] < float(e5[p]) - 40.0)
        end = int(st5[p + below[0]]) + int(0.005 * SR) if below.size else min(len(m), hi)
        out.append(Comp(onset=on, peak=int(st1[pk]), peak_db=pk_db, end=min(len(m), end)))
    return out, G


def _level_db(m: np.ndarray, a: int, b: int) -> float:
    a, b = max(0, a), max(0, b)
    if b <= a:
        return -200.0
    return float(10 * np.log10(np.mean(m[a:b] ** 2) + 1e-20))


def _file_start_ok(m: np.ndarray, on: int, pk_db: float) -> bool:
    """gen/process.py review 2: a stroke at the file start counts only with evidence."""
    head = 10 * np.log10(np.mean(m[:max(1, int(0.0015 * SR))] ** 2) + 1e-20) - pk_db
    if head <= -30.0:
        return True
    seg = m[on:on + int(0.050 * SR)]
    if len(seg) < int(0.006 * SR):
        return False
    hp = signal.sosfilt(signal.butter(4, 2000, "high", fs=SR, output="sos"), seg)
    _, eh = envelope(hp, SR, 1.0, 0.25)
    return float(np.argmax(eh)) * 0.25 <= 5.0


PRESS_SPAN_DB = 18.0       # a press is within 18 dB of the take's loudest component
QUIET_DB = 40.0            # "quiet": 5 ms level 40 dB under the press peak
ISOLATION_MS = 150.0       # a stroke needs 150 ms to the presses before and after it
TAIL_CAP_MAX_MS = 40.0     # a release tail may be capped by up to 40 ms when it is already 20 dB down


def find_strokes(m: np.ndarray, take: str, part: str) -> tuple[list[Stroke], list[dict]]:
    """Presses (loud, quiet before, not the release of the key before) and everything up to the next press."""
    comps, G = components(m)
    strokes, skipped = [], []
    presses: list[tuple[Comp, str]] = []
    cur: Comp | None = None                  # the press the components now belong to
    for i, c in enumerate(comps):
        if c.peak_db < G - PRESS_SPAN_DB:
            continue                         # a release, a rattle or a far key: part of a stroke, never its start
        if cur is not None and c.onset - cur.onset < int(0.260 * SR) and cur.peak_db - c.peak_db >= 3.0:
            continue                         # the release (or a rattle) of the current press
        why, start_kind = None, "quiet"
        if c.onset < int(0.0015 * SR):
            start_kind = "file-start"
            if not _file_start_ok(m, c.onset, c.peak_db):
                why = "kêu ngay từ mẫu đầu, đầu tiếng chưa xác minh"
        elif c.onset < int(0.031 * SR):
            start_kind = "near-file-start"   # what there is before the onset must be quiet (file-start rule level)
            pre = _level_db(m, 0, c.onset - int(0.0005 * SR)) - c.peak_db
            if pre > -30.0:
                why = f"không có lặng trước đầu tiếng ({pre:.0f} dB)"
        else:
            pre = _level_db(m, c.onset - int(0.030 * SR), c.onset - int(0.001 * SR)) - c.peak_db
            if pre > -35.0:
                why = f"không có lặng trước đầu tiếng ({pre:.0f} dB)"
        cur = c
        if why:
            skipped.append({"take": take, "onset_ms": round(c.onset / SR * 1000, 1), "why": why})
            presses.append((c, "blocker"))   # a key landing on another's tail still ends that stroke
            continue
        presses.append((c, start_kind))
    _, e5 = envelope(m, SR, 5.0, 1.0)
    hop = int(0.001 * SR)
    for k, (c, kind) in enumerate(presses):
        if kind == "blocker":
            continue
        nxt = presses[k + 1][0].onset if k + 1 < len(presses) else len(m)
        prv = presses[k - 1][0].onset if k > 0 else None
        if nxt - c.onset < int(ISOLATION_MS / 1000 * SR) or (prv is not None and c.onset - prv < int(ISOLATION_MS / 1000 * SR)):
            # fast typing: whose release is whose cannot be told apart
            skipped.append({"take": take, "onset_ms": round(c.onset / SR * 1000, 1),
                            "why": f"phím khác cách dưới {ISOLATION_MS:.0f} ms, không rõ nhả phím của ai"})
            continue
        f0, f1 = c.onset // hop, max(c.onset // hop + 1, (nxt - int(0.006 * SR)) // hop)
        loud = np.flatnonzero(e5[f0:f1] >= c.peak_db - QUIET_DB)
        end = (f0 + int(loud[-1])) * hop + int(0.010 * SR) if loud.size else c.end
        if end > nxt - int(0.002 * SR):
            skipped.append({"take": take, "onset_ms": round(c.onset / SR * 1000, 1),
                            "why": f"phím sau đến sớm ({(nxt - c.onset) / SR * 1000:.0f} ms), chưa tắt"})
            continue
        inner = [d for d in comps if c.onset < d.onset < end]
        st = Stroke(take=take, index=len(strokes), onset=c.onset, press_peak_db=c.peak_db, press_end=end,
                    start_kind=kind, kind="press+release" if inner else "press")
        if inner:
            rel = max(inner, key=lambda d: d.peak_db)
            st.release_onset, st.release_peak_db, st.release_end = rel.onset, rel.peak_db, end
            st.notes.append(f"{len(inner)} thành phần sau tiếng nhấn")
        strokes.append(st)
    return strokes, skipped


def render(m: np.ndarray, st: Stroke, part: str) -> tuple[np.ndarray | None, dict]:
    """The stroke as a float mono 48 kHz clip (not level-normalised). Too long: shorten the longest
    quiet gap after the press (the finger's hold time), never under 50 ms from the press onset."""
    cap_n = int(CAP_MS[part] / 1000 * SR)
    a = max(0, st.onset - int(0.001 * SR))
    end = st.press_end
    info: dict = {"pre_roll_ms": round((st.onset - a) / SR * 1000, 2), "tightened_ms": 0.0}
    need = (end - a) - (cap_n - int(0.002 * SR))
    y = m[a:end].copy()
    if need > 0:
        _, e5 = envelope(y, SR, 5.0, 1.0)
        hop = int(0.001 * SR)
        quiet = e5 < st.press_peak_db - QUIET_DB
        start_f = int(0.030 * SR) // hop
        best = (0, 0)
        d = np.diff(np.concatenate([[0], quiet[start_f:].astype(np.int8), [0]]))
        for r0, r1 in zip(np.where(d == 1)[0], np.where(d == -1)[0]):
            r0, r1 = r0 + start_f, r1 + start_f
            if r1 * hop + int(0.005 * SR) >= len(y):
                continue                     # the closing silence is not a gap
            if r1 - r0 > best[1] - best[0]:
                best = (r0, r1)
        g0 = best[0] * hop + int(0.004 * SR)
        g1 = best[1] * hop
        room = g1 - g0
        after = g1                           # the sound after the gap must start >= 50 ms after the press
        room = min(room, after - int(0.050 * SR))
        cut = max(0, min(room, need))
        over = need - cut
        if over > int(TAIL_CAP_MAX_MS / 1000 * SR):
            return None, {**info, "why": f"không vừa {CAP_MS[part]:.0f} ms (thiếu {over / SR * 1000:.0f} ms)"}
        if cut > int(0.002 * SR):
            xf = int(0.002 * SR)
            head = y[:g0 + xf].copy()
            tail = y[g0 + cut:].copy()
            r = np.linspace(0.0, 1.0, xf)
            head[-xf:] = head[-xf:] * (1 - r) + tail[:xf] * r
            y = np.concatenate([head, tail[xf:]])
            info["tightened_ms"] = round(cut / SR * 1000, 1)
        if over > 0:
            # what is left over: the release's own tail, capped exponentially (only when already 20 dB down)
            _, e5b = envelope(y, SR, 5.0, 1.0)
            at = min(len(e5b) - 1, (cap_n - int(0.025 * SR)) // hop)
            if e5b[at] > st.press_peak_db - 20.0:
                return None, {**info, "why": f"không vừa {CAP_MS[part]:.0f} ms, đuôi nhả phím còn to"}
            info["release_tail_capped_ms"] = round(over / SR * 1000, 1)
    if len(y) > cap_n:
        y = y[:cap_n]
        info["capped"] = True
    if len(y) < int(MIN_MS[part] / 1000 * SR):
        return None, {**info, "why": "quá ngắn"}
    n = st.onset - a
    if n > 1:
        y[:n] *= np.sin(0.5 * np.pi * np.linspace(0.0, 1.0, n)) ** 2
    pk = int(np.argmax(np.abs(y)))
    knee = min(max(pk + int(0.005 * SR), int((0.55 if info.get("release_tail_capped_ms") else 0.7) * len(y))), len(y) - 2)
    out, tail = dsp.exp_cap_tail(y, SR, knee, -60.0)
    info["tail"] = tail
    info["duration_ms"] = round(len(y) / SR * 1000, 2)
    return out[:, 0], info


def to_dict(st: Stroke) -> dict:
    d = asdict(st)
    d["onset_ms"] = round(st.onset / SR * 1000, 2)
    d["gap_ms"] = None if st.gap_ms is None else round(st.gap_ms, 1)
    d["release_rel_db"] = None if st.release_rel_db is None else round(st.release_rel_db, 1)
    return d
