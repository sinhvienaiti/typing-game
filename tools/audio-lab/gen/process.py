"""Model output -> review candidate (§5.1 step 4; batch 0b round 2 fixes).

  run.sh gen.process <raw dir|record.json>... --spec CARD.yaml --out DIR [--whole] [--notch-comb]

One-shots: unclipped float copy -> 48 kHz (soxr VHQ) -> HPF 35 Hz -> sound events, each with a
TRUE onset (a quiet point before it, or the file start), checked for every window, the first one
too -> window: impacts take their natural length capped at the card's max, a creature (or --whole)
keeps the whole natural call with its slow swell -> exponential cap on a tail the window cuts
(never a flat cut then a fade) -> never across the next event (a burst keeps its first shot) ->
mono or stereo as the card says -> normalise as the card says (peak -1 dBTP or LUFS).
Loops: float copy -> 48 kHz -> HPF -> optional cut of the decoder comb (k x 44100/256 Hz above
10 kHz, each line by its prominence) -> stereo beds: L/R levelled per 1/3 octave -> loop start
search (level/colour match, no loud knock or chirp inside) -> equal-power crossfade -> seam check
with the critic's own seam measure -> LUFS-I as the card says.
A file start counts as a verified onset only with evidence (first 1.5 ms >= 30 dB under the peak,
or the >= 2 kHz peak within 5 ms); an unverified one is kept for the critic, marked
"onset_verified": false, and never offered for listening (common/batch0b.py).

Per candidate: <out>/<name>.wav (PCM 24-bit) and <name>.proc.json. <out>/SOURCES.json holds one
record per file (a `gen` layer with the raw clip test of the float copy window) for
`critic run --sources`, and <out>/licences.rows.jsonl the model and licence rows. A candidate with
no true onset, whose first shot is shorter than the card's min before the next one, or whose window
opens on a weak first hit before the main one (a flam), or whose main sound is still rising or loud where the card's
max cuts it (no room for a tail after it), goes to the rejected folder, with the reason. Raw files are never touched.
--build-up (DECISIONS Q6): an action shaped as build-up then release (a huff before the flame, a fuse before the boom,
several flare-ups of one strike) keeps its weaker first part and its later hits; the window is still capped at the card's
max, and the tail cap starts 100 ms after the window's loudest part (the main sound), never on it.
The tail cap of every window starts after its body (the last frame, 10 % of the window and 10-50 ms long, within
6 dB of its loudest frame).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 48000
COMB_F0 = 44100.0 / 256.0
TOOL = "stable-audio-3 (sa3_batch.py)"
FILE_START_HEAD_DB = -30.0     # review 2: a file start counts as a true onset only with evidence
FILE_START_HF_PEAK_MS = 5.0


# ---------------------------------------------------------------- plan from the spec card

@dataclass
class Plan:
    id: str
    game: str
    loop: bool
    channels: int
    onset_class: str
    rise_max_ms: float | None
    target_ms: float
    min_ms: float
    max_ms: float
    norm_mode: str
    norm_target: float
    whole: bool = False
    two_part: bool = False       # a lighter first hit 20-90 ms before the main one is the design (word.load 'ka-chunk')
    # DECISIONS Q6: the action's own build-up or bursts are the design (a huff before the flame, a fuse before the
    # boom, several flare-ups of one multi-target strike): a weaker first part is never a flam and a later hit never
    # ends the window; unlike `whole`, the window is still capped at the card's max
    build_up: bool = False

    @property
    def creature(self) -> bool:
        return self.onset_class == "creature"


def plan_from_card(card: dict, whole: bool | None = None, two_part: bool = False, build_up: bool = False) -> Plan:
    pb, d, o = card.get("playback") or {}, card.get("duration") or {}, card.get("onset") or {}
    lf = (card.get("loudness") or {}).get("file") or {}
    metric = str(lf.get("metric") or "peak-dbtp")
    mode = {"peak-dbtp": "peak", "peak": "peak", "lufs-i": "lufs-i", "lufs-m-max": "lufs-m-max",
            "lufs-s-max": "lufs-s-max"}.get(metric, "peak")
    target = float(lf.get("target") if lf.get("target") is not None else (-26.0 if mode == "lufs-i" else -1.0))
    loop = pb.get("mode") == "loop"
    t = float(d.get("target_ms") or 1000.0)
    cls = str(o.get("class") or "impact")
    return Plan(id=card["id"], game=card["game"], loop=loop, channels=2 if pb.get("channels") == "stereo" else 1,
                onset_class=cls, rise_max_ms=o.get("rise_max_ms"), target_ms=t,
                min_ms=float(d.get("min_ms") or t * 0.8), max_ms=float(d.get("max_ms") or t * 1.2),
                norm_mode=mode, norm_target=target, whole=bool(whole if whole is not None else cls == "creature"),
                two_part=bool(two_part), build_up=bool(build_up))


# ---------------------------------------------------------------- envelopes and events

def envelope(x: np.ndarray, sr: int, win_ms: float = 1.0, hop_ms: float = 0.25) -> tuple[np.ndarray, np.ndarray]:
    """(frame start samples, RMS level dB) of a mono signal."""
    w = max(1, int(sr * win_ms / 1000))
    h = max(1, int(sr * hop_ms / 1000))
    x = np.asarray(x, dtype=np.float64)
    if len(x) < w:
        x = np.pad(x, (0, w - len(x)))
    c = np.concatenate([[0.0], np.cumsum(x ** 2)])
    st = np.arange(0, len(x) - w + 1, h)
    return st, 10 * np.log10((c[st + w] - c[st]) / w + 1e-20)


@dataclass
class Event:
    onset: int                 # sample of the true start (or of the cut-in point)
    peak: int                  # sample of the loudest frame of the event
    first_peak: int            # first frame within 3 dB of the event's loudest
    peak_db: float
    kind: str                  # quiet | file-start | cut-in (after an earlier sound's tail)
    pre_db: float | None       # energy 30..2 ms before the onset, re the event peak
    end: int = 0               # natural end (decayed), next event, or file end
    end_kind: str = "file-end"  # decayed | next-hit | next-event | file-end
    attack_ms: float = 0.0
    head_db: float | None = None     # file-start: first 1.5 ms re the event's 1 ms peak
    hf_peak_ms: float | None = None  # file-start: >= 2 kHz peak, ms after the onset (first 50 ms)

    @property
    def true_onset(self) -> bool:
        return self.kind in ("quiet", "file-start")

    @property
    def verified(self) -> bool:
        """A quiet onset is measured; a file start only with evidence (review 2): its first 1.5 ms
        >= 30 dB under the peak, or its >= 2 kHz peak within the first 5 ms (the hit is at the start,
        not ringing on from before the file)."""
        if self.kind == "quiet":
            return True
        if self.kind != "file-start":
            return False
        return (self.head_db is not None and self.head_db <= FILE_START_HEAD_DB) or (
            self.hf_peak_ms is not None and self.hf_peak_ms <= FILE_START_HF_PEAK_MS)


def _runs(mask: np.ndarray) -> list[tuple[int, int]]:
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    return list(zip(np.where(d == 1)[0], np.where(d == -1)[0]))


def find_events(m: np.ndarray, sr: int, creature: bool = False, whole: bool = False) -> tuple[list[Event], float]:
    """Sound events of a mono signal and the global 1 ms peak level (dB).

    An event is a run of the 10 ms level above (its global peak - quiet) (quiet: 30 dB, creatures
    40 dB; dips under 5 ms bridged). Its start is the TRUE onset, found the same way for every event,
    the first one too, with no back limit (the file start counts as a start); the 1 ms level places
    it to 0.25 ms. A run whose 28 ms before it hold an earlier sound's tail (> -30 dB re its peak)
    is a cut-in, never a window start. Inside a run, a second hit at least 30 ms later, as loud as
    the first (within 6 dB) and after a dip of >= 12 dB that lasts >= 8 ms, ends a one-shot window
    at the dip (a burst keeps its first shot; the flutter of a noisy whoosh is not a second hit); a
    whole call (creatures) keeps its swells. The 10 ms level does not see
    the waveform-period ripple of a low body as dips (the 1 ms level does). Runs more than 12 dB
    (creatures 15 dB) under the global peak are not events."""
    quiet = 40.0 if creature else 30.0
    span = 15.0 if creature else 12.0
    st, e = envelope(m, sr, 1.0, 0.25)
    sT, eT = envelope(m, sr, 10.0, 1.0)
    st5, e5 = envelope(m, sr, 5.0, 1.0)
    hop = int(st[1] - st[0]) if len(st) > 1 else 1
    hT = int(sT[1] - sT[0]) if len(sT) > 1 else 1
    G, GT = float(e.max()), float(eT.max())
    active = eT > GT - quiet
    gap = max(1, int(0.005 * sr / hT))
    for a, b in _runs(~active):            # bridge short dips
        if a > 0 and b < len(active) and b - a < gap:
            active[a:b] = True
    nb = max(1, int(0.015 * sr / hT))
    events: list[Event] = []
    for a, b in _runs(active):
        pkT = a + int(np.argmax(eT[a:b]))
        if eT[pkT] < GT - span:
            continue
        # onset to 0.25 ms: first 1 ms frame of the run's span over (1 ms peak - quiet)
        lo_s, hi_s = max(0, int(sT[a]) - int(0.005 * sr)), int(sT[min(b, len(sT) - 1)]) + int(0.010 * sr)
        f0, f1 = int(np.searchsorted(st, lo_s)), int(np.searchsorted(st, hi_s))
        pk1 = f0 + int(np.argmax(e[f0:max(f0 + 1, f1)]))
        pk_db = float(e[pk1])
        above = np.flatnonzero(e[f0:pk1 + 1] > pk_db - quiet)
        on_f = f0 + int(above[0]) if above.size else f0
        on = int(st[on_f])
        kind, pre = ("file-start", None) if on_f == 0 or on < int(0.0005 * sr) else ("quiet", None)
        head = hfpk = None
        if kind == "file-start":            # evidence that the sound starts here (review 2)
            head = float(10 * np.log10(np.mean(m[:max(1, int(0.0015 * sr))] ** 2) + 1e-20) - pk_db)
            hfpk = _hf_peak_ms(m, sr, on, creature)
        if kind == "quiet":
            lo, hi = max(0, on - int(0.030 * sr)), max(0, on - int(0.002 * sr))
            pre = float(10 * np.log10(np.mean(m[lo:hi] ** 2) + 1e-20) - pk_db) if hi > lo else -90.0
            if pre > -30.0:
                kind = "cut-in"
        end_s, end_kind = None, None
        if not whole:                       # a second major hit ends a one-shot at the dip
            subs = [i for i in range(a, b) if eT[i] >= eT[pkT] - 6.0
                    and eT[i] >= eT[max(a, i - nb):min(b, i + nb + 1)].max()]
            for i, j in zip(subs, subs[1:]):
                if (sT[j] - sT[i]) < 0.030 * sr:
                    continue
                dip = i + int(np.argmin(eT[i:j + 1]))
                low = int(np.count_nonzero(eT[i:j + 1] < min(eT[i], eT[j]) - 12.0))
                if min(eT[i], eT[j]) - eT[dip] >= 12.0 and low >= max(1, int(0.008 * sr / hT)):
                    end_s, end_kind = int(sT[dip]) + int(0.005 * sr), "next-hit"
                    break
        last_f = int(np.searchsorted(st, end_s)) if end_s else f1
        peak_f = on_f + int(np.argmax(e[on_f:max(on_f + 1, last_f)]))
        ev = Event(onset=on, peak=int(st[peak_f]), first_peak=int(st[peak_f]), peak_db=float(e[peak_f]),
                   kind=kind, pre_db=pre, head_db=head, hf_peak_ms=hfpk)
        # first frame within 3 dB of the loudest (5 ms level): the critic times the attack to it
        k0, kp = int(np.searchsorted(st5, on)), int(np.searchsorted(st5, ev.peak))
        seg5 = e5[k0:kp + 1]
        if seg5.size:
            fp = k0 + int(np.argmax(seg5 >= e5[kp] - 3.0))
            while fp + 1 < len(e5) and e5[fp + 1] >= e5[fp] and (end_s is None or st5[fp + 1] < end_s):
                fp += 1
            ev.first_peak = int(st5[fp])
            seg2 = e5[k0:fp + 1]
            i10 = int(np.argmax(seg2 >= e5[fp] - 20.0))
            i90 = int(np.argmax(seg2 >= e5[fp] - 0.92))
            ev.attack_ms = max(0.0, (i90 - i10) * float(st5[1] - st5[0]) / sr * 1000)
        if end_kind == "next-hit":
            ev.end, ev.end_kind = min(len(m), end_s), "next-hit"
        else:
            k5 = int(np.searchsorted(st5, ev.peak))
            below = np.flatnonzero(e5[k5:] < float(e5[k5:k5 + 1].max() if k5 < len(e5) else -200) - (45.0 if creature else 40.0))
            ev.end = min(len(m), int(st5[k5 + below[0]]) + int(0.005 * sr)) if below.size else len(m)
            ev.end_kind = "decayed" if below.size else "file-end"
        events.append(ev)
    for k, ev in enumerate(events):        # never across the next event
        if k + 1 < len(events) and ev.end > events[k + 1].onset:
            ev.end, ev.end_kind = max(ev.onset + 1, events[k + 1].onset - int(0.001 * sr)), "next-event"
    return events, G


def _hf_peak_ms(m: np.ndarray, sr: int, on: int, creature: bool) -> float | None:
    """ms from the onset to the loudest 1 ms frame of the >= 2 kHz band in the first 50 ms; None for
    creatures (a call's highs are its voice, not a crack) or when that band is 40 dB under the sound."""
    if creature:
        return None
    from scipy import signal

    seg = m[on:on + int(0.050 * sr)]
    if len(seg) < int(0.006 * sr):
        return None
    hp = signal.sosfilt(signal.butter(4, 2000, "high", fs=sr, output="sos"), seg)
    _, eh = envelope(hp, sr, 1.0, 0.25)
    _, ef = envelope(seg, sr, 1.0, 0.25)
    if eh.max() < ef.max() - 40.0:
        return None
    return round(float(np.argmax(eh)) * 0.25, 2)


def pre_hit(m: np.ndarray, sr: int, a: int, b: int) -> dict | None:
    """A weak first hit before the main one inside a window (a flam: 'gõ hai lần').

    On the 10 ms level from a to b: an earlier peak >= 6 dB weaker than the main one, then a dip
    >= 6 dB under it and >= 12 dB under the main peak that lasts >= 8 ms, the main peak >= 20 ms
    after the first. Two near-equal puffs are the next-hit rule's case; a crack-then-boom 14-19 ms
    apart (gun takes) is not a flam; creatures are never checked (their calls swell)."""
    sT, eT = envelope(m[a:b], sr, 10.0, 1.0)
    if len(eT) < 3:
        return None
    hop = int(sT[1] - sT[0]) if len(sT) > 1 else 1
    pk = int(np.argmax(eT))
    best, top, top_k = None, -np.inf, 0
    for k in range(pk):
        if eT[k] > top:
            top, top_k = float(eT[k]), k
        if (eT[pk] - top >= 6.0 and top - eT[k] >= 6.0 and eT[pk] - eT[k] >= 12.0
                and sT[pk] - sT[top_k] >= 0.020 * sr):
            if best is None or eT[k] < best[1]:
                best = (top_k, float(eT[k]))
    if best is None:
        return None
    low = int(np.count_nonzero(eT[best[0]:pk] < eT[pk] - 12.0))
    if low < max(1, int(0.008 * sr / hop)):
        return None
    return {"first_ms": round(sT[best[0]] / sr * 1000, 1), "main_ms": round(sT[pk] / sr * 1000, 1),
            "first_db": round(float(eT[best[0]] - eT[pk]), 1), "dip_db": round(best[1] - float(eT[pk]), 1)}


# ---------------------------------------------------------------- shaping

def cap_tail(y: np.ndarray, sr: int, knee: int, end_db: float = -60.0, smooth_ms: float = 4.0) -> tuple[np.ndarray, dict]:
    """Exponential cap on a tail (build.dsp.exp_cap_tail, shared with the recipe chain's tail "exp")."""
    from build import dsp

    out, info = dsp.exp_cap_tail(y, sr, knee, end_db, smooth_ms)
    return (out if np.ndim(y) == 2 else out[:, 0]), info


def fade_in(y: np.ndarray, n: int) -> np.ndarray:
    y = y.copy()
    n = min(n, y.shape[0])
    if n > 1:
        r = np.sin(0.5 * np.pi * np.linspace(0.0, 1.0, n)) ** 2
        y[:n] *= r[:, None] if y.ndim == 2 else r
    return y


def to_channels(x: np.ndarray, channels: int) -> tuple[np.ndarray, dict]:
    """Card channels: mono by the §5.1 rule (mid if the fold-down loses <= 3 dB, else the stronger
    channel); stereo kept as is, with its correlation (a dual-mono file stays dual mono)."""
    from build import dsp

    x = x if x.ndim == 2 else x[:, None]
    info: dict = {}
    if x.shape[1] == 2:
        L, R = x[:, 0], x[:, 1]
        info["stereo_corr"] = round(float(np.corrcoef(L, R)[0, 1]), 4) if np.std(L) > 0 and np.std(R) > 0 else 1.0
        info["dual_mono"] = bool(np.array_equal(L, R))
        e_lr = float(np.mean(np.sum(x ** 2, axis=0)))
        e_mid = float(np.sum(x.mean(axis=1) ** 2))
        info["mono_loss_db"] = round(10 * np.log10(max(e_lr, 1e-20) / max(e_mid, 1e-20)), 2)
    if channels == 1:
        y, how = dsp.to_channels(x, 1)
    elif x.shape[1] == 2:
        y, how = x, "stereo-dual-mono" if info.get("dual_mono") else "stereo"
    else:
        y, how = np.repeat(x, 2, axis=1), "dual-mono-from-mono"
    info["channels"] = how
    return y, info


# ---------------------------------------------------------------- stereo balance (beds)

def lr_balance(x: np.ndarray, sr: int) -> dict:
    """L re R in dB, broadband and in the critic's four bands (critic.features.stereo_balance)."""
    from critic import features as F

    b = F.stereo_balance(x[:, 0], x[:, 1], sr)
    return {"broadband_db": b["lr_balance_db"], "bands_db": b["lr_balance_bands_db"]}


def balance_stereo(x: np.ndarray, sr: int, numtaps: int = 4097, min_db: float = 0.5) -> tuple[np.ndarray, dict]:
    """Level the two channels of a stereo bed per 1/3 octave (review 2: H s2004 leaned 5.9 dB right,
    6.6 dB under 150 Hz but 2.7 dB at 4-16 kHz, so one broadband gain would tilt the highs left).

    Long-term L/R energy ratio per 1/3 octave (Welch), smoothed over 3 bands; each channel gets half
    the difference with opposite signs through a linear-phase FIR (firwin2, applied centred: zero
    delay; beds have no attack to smear). Skipped when every band is within min_db."""
    from scipy import signal

    x = np.asarray(x, dtype=np.float64)
    if x.ndim != 2 or x.shape[1] != 2 or np.array_equal(x[:, 0], x[:, 1]):
        return x, {"applied": False, "why": "not a two-channel stereo file"}
    before = lr_balance(x, sr)
    nper = int(min(8192, 2 ** int(np.floor(np.log2(max(256, x.shape[0]))))))
    f, pl = signal.welch(x[:, 0], sr, nperseg=nper)
    _, pr = signal.welch(x[:, 1], sr, nperseg=nper)
    k = np.arange(np.ceil(3 * np.log2(25 / 1000)), np.floor(3 * np.log2(min(20000, sr / 2 * 0.95) / 1000)) + 1)
    fc = 1000 * 2 ** (k / 3)
    d = []
    for c in fc:
        sel = (f >= c * 2 ** (-1 / 6)) & (f < c * 2 ** (1 / 6))
        d.append(10 * np.log10((pl[sel].sum() + 1e-30) / (pr[sel].sum() + 1e-30)) if sel.any() else 0.0)
    d = np.convolve(np.pad(np.array(d), 1, mode="edge"), np.ones(3) / 3, mode="valid")
    if np.max(np.abs(d)) < min_db:
        return x, {"applied": False, "why": f"every 1/3 octave within {min_db:g} dB", "before": before}
    grid = np.concatenate([[0.0], fc, [sr / 2]])
    dd = np.concatenate([[d[0]], d, [d[-1]]])
    y = np.empty_like(x)
    for ch, sign in ((0, -1.0), (1, 1.0)):
        h = signal.firwin2(numtaps, grid, 10 ** (sign * dd / 40.0), fs=sr)
        y[:, ch] = signal.fftconvolve(x[:, ch], h, mode="same")
    after = lr_balance(y, sr)
    return y, {"applied": True, "mode": "per 1/3 octave, linear-phase FIR", "numtaps": numtaps,
               "before": before, "after": after, "max_band_diff_db": round(float(np.max(np.abs(d))), 2)}


# ---------------------------------------------------------------- decoder comb

def comb_lines(x: np.ndarray, sr: int, f0: float = COMB_F0, fmin: float = 10000.0) -> dict:
    from critic import loopcheck
    from scipy import signal

    m = x.mean(axis=1) if x.ndim == 2 else x
    f, p = signal.welch(m, sr, nperseg=min(8192, 2 ** int(np.floor(np.log2(max(256, len(m)))))))
    return loopcheck.comb(f, p, f0, fmin)


def _peaking_cut(fr: float, gain_db: float, bw_hz: float, sr: int) -> np.ndarray:
    """RBJ peaking biquad (one section, sos row) cutting gain_db at fr with the given bandwidth."""
    A = 10 ** (gain_db / 40.0)
    w0 = 2 * np.pi * fr / sr
    alpha = np.sin(w0) / (2 * (fr / bw_hz))
    b = np.array([1 + alpha * A, -2 * np.cos(w0), 1 - alpha * A])
    a = np.array([1 + alpha / A, -2 * np.cos(w0), 1 - alpha / A])
    return np.concatenate([b / a[0], a / a[0]])


def notch_comb(x: np.ndarray, sr: int, f0: float = COMB_F0, fmin: float = 10000.0, bw_hz: float = 24.0,
               min_prom_db: float = 3.0) -> tuple[np.ndarray, dict]:
    """Cut the decoder comb lines k*f0 above fmin that stand >= min_prom_db over their neighbours,
    each by its own prominence (a peaking cut, zero phase: beds have no attack to smear), so a
    line ends level with its neighbours instead of becoming a hole (full notches left the lines
    10 dB under the bed in round 2's first pass). Returns (audio, report)."""
    from scipy import signal

    before = comb_lines(x, sr, f0, fmin)
    cuts = [(fr, pr) for fr, pr in zip(before.get("freqs", []), before.get("prom_db", []))
            if pr is not None and pr >= min_prom_db and fr < sr / 2 - bw_hz]
    y = np.asarray(x, dtype=np.float64)
    y2 = y if y.ndim == 2 else y[:, None]
    if cuts:
        # filtfilt runs each section twice: half the cut per pass
        sos = np.vstack([_peaking_cut(fr, -pr / 2.0, bw_hz, sr) for fr, pr in cuts])
        y2 = signal.sosfiltfilt(sos, y2, axis=0)
    after = comb_lines(y2, sr, f0, fmin)
    rep = {"f0_hz": round(f0, 4), "fmin_hz": fmin, "bandwidth_hz": bw_hz, "notched": len(cuts),
           "mode": "peaking cut by line prominence",
           "median_prom_db_before": before.get("median_prom_db"), "median_prom_db_after": after.get("median_prom_db")}
    return (y2 if y.ndim == 2 else y2[:, 0]), rep


# ---------------------------------------------------------------- one-shot

def _critic_attack_ms(y: np.ndarray, sr: int) -> float:
    from critic import features as F
    e = F.envelope(y if y.ndim == 1 else y.mean(axis=1), sr)
    return float(max(0.0, (e["t"][e["i90"]] - e["t"][e["i10"]]) * 1000))


@dataclass
class Window:
    event: Event
    a: int
    b: int
    capped: bool
    reason: str
    score: float = 0.0
    critic_attack_ms: float | None = None
    shaping: dict = field(default_factory=dict)
    room_ok: bool = True


# Exponential tail cap of a window the card's max (or the next event) cuts (batch 1c review, Q6): the line starts
# after the window's MAIN sound, never before it. With a build-up (a huff, a fuse, several flare-ups) the loudest
# part comes late: a knee at 35 % of the window turned the flame or the boom down by 8-27 dB. The main sound keeps
# its own decay for TAIL_HOLD_MS (build-up ids; plain sounds 10 % of the window, at most that) and to the end of its
# body (body_end), and the window must leave the cap at least TAIL_ROOM_FRAC of its length (TAIL_ROOM_MIN_MS at least)
# after the knee; else the sound is still rising or loud where the card cuts it (a swell or a roar past the card's
# max), which no tail shape can save: refused, with the reason.
TAIL_HOLD_MS = 100.0
TAIL_ROOM_FRAC = 0.2
TAIL_ROOM_MIN_MS = 50.0
# a sound already this far under its peak where the window ends decays on its own there: no room needed
# (impact.multi A s3004 of batch 1c: a late flare-up, then -35 dB at the card's max)
TAIL_ROOM_END_DB = -30.0


def main_index(y: np.ndarray, sr: int, win_ms: float = 10.0) -> int:
    """Sample at the centre of the loudest `win_ms` of a window (the main sound)."""
    m = y if y.ndim == 1 else y.mean(axis=1)
    w = max(1, min(m.size, int(win_ms * sr / 1000)))
    c = np.concatenate([[0.0], np.cumsum(m ** 2)])
    hop = max(1, int(0.001 * sr))
    st = np.arange(0, max(1, m.size - w + 1), hop)
    return int(st[int(np.argmax(c[st + w] - c[st]))] + w // 2)


def tail_room_need(n: int, sr: int) -> int:
    return int(max(TAIL_ROOM_MIN_MS * sr / 1000, TAIL_ROOM_FRAC * n))


# The main sound is a body, not one loud instant: fire.cast E s3005 peaks at 145 ms (the flame catching) and stays
# within 1-3 dB of that until 450 ms; fire.impact.c and kill.elite carry their blast for 200-400 ms. The cap starts where
# the body ends: the centre of the last frame within BODY_DB of the window's loudest frame (a later flare-up of
# impact.multi counts too). The frame is 10 % of the window, 10 to 50 ms: a 10 ms peak sits a few dB over the body the
# ear hears, so a 10 ms frame still cut kill.elite and gun.xung bodies by up to 20 dB; a 96 ms hit needs a short one.
# Measured on batch 1c (Apple M4, Q6_REWRITE §13): a plain hit's body ends inside the 35 % knee of batch 0b, so its
# knee does not move.
BODY_DB = 6.0
BODY_WIN_MS = (10.0, 50.0)


def body_end(y: np.ndarray, sr: int, drop_db: float = BODY_DB) -> int:
    """Centre of the last frame of a window within `drop_db` of its loudest frame (frame: 10 % of the window,
    BODY_WIN_MS bounds)."""
    m = y if y.ndim == 1 else y.mean(axis=1)
    lo, hi = BODY_WIN_MS
    win_ms = float(np.clip(0.1 * m.size / sr * 1000, lo, hi))
    w = max(1, min(m.size, int(win_ms * sr / 1000)))
    c = np.concatenate([[0.0], np.cumsum(m ** 2)])
    hop = max(1, int(0.001 * sr))
    st = np.arange(0, max(1, m.size - w + 1), hop)
    e = 10 * np.log10((c[st + w] - c[st]) / w + 1e-20)
    return int(st[np.flatnonzero(e >= e.max() - drop_db)[-1]] + w // 2)


def plan_windows(m: np.ndarray, sr: int, plan: Plan, events: list[Event], G: float) -> list[Window]:
    pre_ms = 5.0 if plan.creature else 0.5 if plan.onset_class in ("impact", "key", "ui") else 1.0
    rise = float(plan.rise_max_ms or 10.0)
    out = []
    for k, ev in enumerate(events):
        nat = ev.end - ev.onset
        room = (events[k + 1].onset - int(0.001 * sr) if k + 1 < len(events) else len(m)) - ev.onset
        pre = min(ev.onset, int(pre_ms * sr / 1000))
        if plan.whole:
            L, capped, why = nat, ev.end_kind != "decayed", "whole natural sound"
        else:
            # the card's range holds the whole file, pre-roll included
            lo, hi = int(plan.min_ms * sr / 1000) - pre, int(plan.max_ms * sr / 1000) - pre
            if nat > hi:
                L, capped, why = hi, True, f"natural {nat / sr * 1000:.0f} ms > max {plan.max_ms:g} ms: capped"
            elif nat < lo and ev.end_kind in ("decayed", "file-end"):
                L, capped, why = min(lo, room), False, "natural shorter than min: decayed tail kept"
                if room < lo:
                    why += "; stops before the next event"
            else:
                L, capped, why = nat, ev.end_kind != "decayed", "natural length"
        if ev.end_kind in ("next-event", "next-hit"):
            L = min(L, ev.end - ev.onset)
            why += "; stops before the next hit" if ev.end_kind == "next-hit" else "; stops before the next event"
        a = ev.onset - pre
        b = min(len(m), ev.onset + max(1, L))
        score = (ev.peak_db - G) - 2.0 * max(0.0, ev.attack_ms - rise) / rise - (2.0 if capped and not plan.whole else 0.0) \
            - 0.002 * (ev.onset / sr * 1000)
        if plan.creature and ev.attack_ms > rise:
            score += 2.0 * max(0.0, ev.attack_ms - rise) / rise   # a creature's swell is its nature
        out.append(Window(ev, a, b, capped, why, round(float(score), 3)))
    return sorted(out, key=lambda w: -w.score)


def render_window(x: np.ndarray, sr: int, w: Window, plan: Plan) -> tuple[np.ndarray, dict]:
    y = x[w.a:w.b].copy()
    pre = w.event.onset - w.a
    y = fade_in(y, max(pre, int(0.0003 * sr)))
    n = y.shape[0]
    main = main_index(y, sr)
    # the event's first loud point can lie past the window (a sound still rising where the card cuts it)
    first = min(w.event.first_peak - w.a, main)
    knee = max(first + int(0.005 * sr), int((0.35 if w.capped else 0.6) * n))
    hold_ms = TAIL_HOLD_MS if plan.build_up else min(TAIL_HOLD_MS, 0.1 * n / sr * 1000)
    knee = max(knee, main + int(hold_ms * sr / 1000))
    body = body_end(y, sr)
    knee = max(knee, body)
    if plan.whole:
        knee = max(knee, int(0.85 * n))
    room, need = n - knee, tail_room_need(n, sr)
    y, info = cap_tail(y, sr, knee, -60.0)
    info.update({"main_ms": round(main / sr * 1000, 1),
                 "body_end_ms": round(body / sr * 1000, 1),
                 "tail_room_ms": round(max(0, room) / sr * 1000, 1),
                 "tail_room_need_ms": round(need / sr * 1000, 1),
                 # a window that ends on the sound's own decay needs no room; one the card or the next event cuts
                 # while it still sounds does
                 "tail_room_ok": bool(plan.whole or not w.capped or room >= need
                                      or info["natural_end_db"] <= TAIL_ROOM_END_DB)})
    return y, info


def process_oneshot(x: np.ndarray, sr: int, plan: Plan) -> dict:
    """x: (n, ch) float at SR after HPF. Returns {audio, window, candidates, onset_ok, ...}."""
    m = x.mean(axis=1)
    events, G = find_events(m, sr, plan.creature, plan.whole or plan.build_up)   # build_up: no next-hit cut
    wins = plan_windows(m, sr, plan, events, G)
    true = [w for w in wins if w.event.true_onset]
    rise = plan.rise_max_ms
    for w in true[:6]:
        y, sh = render_window(x, sr, w, plan)
        w.critic_attack_ms = round(_critic_attack_ms(y, sr), 2)
        w.room_ok = sh["tail_room_ok"]
    pool = true[:6]
    min_n = int(plan.min_ms * sr / 1000) - int(0.002 * sr)
    flams = {id(w): (None if plan.whole else pre_hit(m, sr, w.event.onset, w.b)) for w in pool}
    two, built = {}, {}
    if plan.build_up:            # the action's own build-up (Q6): recorded, never refused as a flam
        for k, f in list(flams.items()):
            if f:
                built[k], flams[k] = f, None
    if plan.two_part:            # the intended two-part sound: kept, recorded, never refused as a flam
        for k, f in list(flams.items()):
            if f and 20.0 <= f["main_ms"] - f["first_ms"] <= 90.0:
                two[k], flams[k] = f, None

    def long_enough(w: Window) -> bool:      # a burst cut at its next shot can be too short to use
        return plan.whole or (w.b - w.a) >= min_n or w.event.end_kind not in ("next-hit", "next-event")

    if pool:
        ok = (lambda w: rise is None or plan.whole or (w.critic_attack_ms or 0) <= rise)
        best = max(pool, key=lambda w: (long_enough(w), w.room_ok, flams[id(w)] is None, w.event.verified, ok(w),
                                        w.score))
    else:
        best = wins[0] if wins else None
    if best is None:
        return {"onset_ok": False, "reason": "không tìm thấy âm nào", "audio": None}
    y, shaping = render_window(x, sr, best, plan)
    best.shaping = shaping

    def wj(w: Window) -> dict:
        ev = w.event
        return {"onset_s": round(ev.onset / sr, 5), "onset_kind": ev.kind, "true_onset": ev.true_onset,
                "onset_verified": ev.verified,
                "head_db": None if ev.head_db is None else round(ev.head_db, 1), "hf_peak_ms": ev.hf_peak_ms,
                "pre_onset_db": None if ev.pre_db is None else round(ev.pre_db, 1),
                "peak_rel_db": round(ev.peak_db - G, 2), "attack_ms_est": round(ev.attack_ms, 2),
                "natural_ms": round((ev.end - ev.onset) / sr * 1000, 1), "end_kind": ev.end_kind,
                "window_s": [round(w.a / sr, 5), round(w.b / sr, 5)], "len_ms": round((w.b - w.a) / sr * 1000, 1),
                "capped": w.capped, "why": w.reason, "score": w.score, "critic_attack_ms": w.critic_attack_ms,
                "tail_room_ok": w.room_ok}

    reason = None
    if not best.event.true_onset:
        reason = f"không có đầu tiếng thật: mọi cửa sổ cắt vào giữa một âm (trước đầu tiếng {wj(best)['pre_onset_db']} dB)"
    elif not long_enough(best):
        reason = (f"phát đầu chỉ dài {(best.b - best.a) / sr * 1000:.0f} ms rồi tới phát sau "
                  f"({best.event.end_kind}), ngắn hơn mức tối thiểu {plan.min_ms:g} ms của thẻ")
    elif flams.get(id(best)):
        f = flams[id(best)]
        reason = (f"gõ hai lần: tiếng nhỏ ở {f['first_ms']:g} ms ({f['first_db']:g} dB) rồi tiếng chính ở "
                  f"{f['main_ms']:g} ms; cắt vào tiếng chính sẽ cắt giữa đuôi tiếng đầu")
    elif not shaping["tail_room_ok"]:
        reason = (f"không còn chỗ cho đuôi: tiếng chính ở {shaping['main_ms']:g} ms, cửa sổ {(best.b - best.a) / sr * 1000:.0f} ms "
                  f"(tối đa của thẻ {plan.max_ms:g} ms) chỉ còn {shaping['tail_room_ms']:g} ms sau tiếng chính, cần "
                  f"{shaping['tail_room_need_ms']:g} ms; âm còn đang lên hay còn to ({shaping['natural_end_db']:g} dB) "
                  f"chỗ bị cắt").replace(".", ",").replace("-", "−")
    note = None
    if reason is None and not best.event.verified:
        ev = best.event
        note = (f"đầu tiếng chưa xác minh: âm kêu ngay từ mẫu đầu (1,5 ms đầu {ev.head_db:.0f} dB so với đỉnh"
                + (f", đỉnh trên 2 kHz ở {ev.hf_peak_ms:g} ms" if ev.hf_peak_ms is not None else "")
                + "); giữ để chấm máy, không chọn vào phiên nghe").replace(".", ",").replace("-", "−")
    return {"onset_ok": best.event.true_onset, "usable": reason is None, "audio": y, "window": wj(best),
            "onset_verified": best.event.verified, "onset_note": note, "two_part": two.get(id(best)),
            "build_up": built.get(id(best)),
            "shaping": shaping, "reason": reason, "pre_hit": flams.get(id(best)),
            "n_events": len(events), "n_true": len(true), "candidates": [wj(w) for w in wins[:8]]}


# ---------------------------------------------------------------- loop

def _seam_cost(x: np.ndarray, sr: int, s: int, n_loop: int, n_xf: int) -> float:
    seg = x[s:s + n_loop + n_xf]
    head, tail = seg[:n_xf], seg[n_loop:n_loop + n_xf]

    def rms(z):
        return 10 * np.log10(np.mean(z ** 2) + 1e-20)

    def cen(z):
        S = np.abs(np.fft.rfft(z.mean(axis=1) * np.hanning(len(z))))
        f = np.fft.rfftfreq(len(z), 1 / sr)
        return float((S * f).sum() / (S.sum() + 1e-20))

    c1, c2 = cen(head), cen(tail)
    blk = int(0.1 * sr)
    lv = [rms(seg[i:i + blk]) for i in range(0, n_loop, blk)]
    return abs(rms(head) - rms(tail)) + 10 * abs(c1 - c2) / max(c1, c2, 1e-9) + 0.15 * (np.percentile(lv, 95) - np.percentile(lv, 10))


def seam_ok(seam: dict) -> bool:
    from critic.thresholds import L1
    if not seam.get("applies"):
        return False
    j = seam.get("jump_excess_dbfs")
    return ((j is None or j < L1["loop_jump_max_dbfs"]) and seam["rms_diff_db"] < L1["loop_rms_max_db"]
            and seam["centroid_diff_rel"] < L1["loop_centroid_max_rel"])


def process_loop(x: np.ndarray, sr: int, plan: Plan, xf_ms: float = 500.0, tries: int = 12) -> dict:
    """Choose a loop start, crossfade, normalise, and keep the first take whose seam passes."""
    from build import chain, dsp
    from critic import features as F, loopcheck

    n_loop = int(plan.target_ms * sr / 1000)
    n_xf = int(xf_ms * sr / 1000)
    lo, hi = int(0.5 * sr), x.shape[0] - int(0.4 * sr) - n_loop - n_xf
    if hi <= lo:
        lo, hi = 0, max(1, x.shape[0] - n_loop - n_xf)
    sig = loopcheck.signature(x, sr, loop=False)
    ev_t = [(int(e["t"] * sr), e["db"]) for e in sig["events"] if e["kind"] != "band"]   # point events only
    costs = []
    for s in range(lo, max(lo + 1, hi), int(0.025 * sr)):
        inside = sum(db for t, db in ev_t if s <= t < s + n_loop + n_xf)
        # the stitch itself, on the same 50 ms windows as the L1 seam check (level-free parts)
        st = F.seam(dsp.loop_crossfade(x[s:s + n_loop + n_xf], xf_ms, sr), sr)
        pen = max(0.0, st["rms_diff_db"] - 0.5) * 4 + max(0.0, st["centroid_diff_rel"] - 0.05) * 40 if st.get("applies") else 0.0
        costs.append((_seam_cost(x, sr, s, n_loop, n_xf) + 0.5 * inside + pen, s))
    costs.sort()
    tried = []
    best = None
    for cost, s in costs[:tries]:
        y = dsp.loop_crossfade(x[s:s + n_loop + n_xf], xf_ms, sr)
        y2, rep = chain.run(y, sr, {"normalise": {"mode": plan.norm_mode, "target": plan.norm_target},
                                    "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 3.0}}, loop=True)
        seam = F.seam(y2, sr)
        ok = seam_ok(seam)
        tried.append({"start_s": round(s / sr, 3), "cost": round(float(cost), 3), "seam_ok": ok,
                      "seam": {k: seam.get(k) for k in ("jump_excess_dbfs", "rms_diff_db", "centroid_diff_rel")}})
        if best is None or (ok and not best[0]):
            best = (ok, s, y2, rep, seam, cost)
        if ok:
            break
    ok, s, y2, rep, seam, cost = best
    return {"onset_ok": True, "audio": y2, "chain_report": rep, "seam_ok": ok,
            "loop": {"start_s": round(s / sr, 3), "length_ms": round(y2.shape[0] / sr * 1000, 1),
                     "crossfade_ms": xf_ms, "cost": round(float(cost), 3),
                     "seam": {k: seam.get(k) for k in ("jump_excess_dbfs", "rms_diff_db", "centroid_diff_rel")},
                     "seam_ok": ok, "tries": tried, "signature_events_in_source": len(ev_t)},
            "window_s": [round(s / sr, 3), round((s + n_loop + n_xf) / sr, 3)]}


# ---------------------------------------------------------------- one candidate

def _model_id(rec: dict) -> str:
    mdl = rec.get("model") or {}
    return mdl.get("id") or f"{mdl.get('repo')}@{mdl.get('revision')}"


def process_record(rec: dict, card: dict, out_dir: Path, *, whole: bool | None = None, notch: bool = False,
                   rejected: Path | None = None, run: str | None = None, two_part: bool = False,
                   build_up: bool = False) -> dict:
    """Process one candidate record (gen/sa3.py or the batch 0b trial). Returns the proc report."""
    from build import chain, dsp, measure

    plan = plan_from_card(card, whole, two_part, build_up)
    f32 = Path(rec["files"]["f32"]["path"])
    x, sr_in = sf.read(str(f32), always_2d=True, dtype="float64")
    x = dsp.resample(x, sr_in, SR)
    x = dsp.apply_filters(x, [{"type": "highpass", "hz": 35, "order": 2}], SR)
    steps = ["f32 raw", "soxr VHQ -> 48 kHz", "hpf35"]
    info: dict = {"candidate": rec["candidate"], "id": card["id"], "game": card["game"], "plan": asdict(plan),
                  "raw_record": str(rec.get("_path") or ""), "spec_card": card.get("_path"),
                  "source_f32": str(f32), "source_f32_sha256": rec["files"]["f32"]["sha256"]}
    if notch:
        x, nrep = notch_comb(x, SR)
        info["comb_notch"] = nrep
        steps.append(f"comb cut {nrep['notched']} lines (k x 172.27 Hz > 10 kHz, by prominence)")
    if plan.loop:
        x, ch = to_channels(x, plan.channels)
        if plan.channels == 2:
            x, bal = balance_stereo(x, SR)
            info["lr_balance"] = bal
            if bal.get("applied"):
                steps.append(f"L/R balance per 1/3 octave ({bal['before']['broadband_db']:+.1f} -> "
                             f"{bal['after']['broadband_db']:+.1f} dB)")
        res = process_loop(x, SR, plan)
        y = res["audio"]
        info.update({"loop": res["loop"], "window_raw_s": res["window_s"], "channels": ch})
        rep = res["chain_report"]
        steps += [f"channels {ch['channels']}", f"loop {res['loop']['length_ms']:.0f} ms from {res['loop']['start_s']:.2f} s",
                  f"equal-power crossfade {res['loop']['crossfade_ms']:g} ms", rep["summary"],
                  "seam ok" if res["seam_ok"] else "seam FAILED"]
        ok, reason = res["seam_ok"], None if res["seam_ok"] else "mối nối không đạt sau các lần thử"
    else:
        res = process_oneshot(x, SR, plan)
        if res.get("audio") is None:
            return {**info, "onset_ok": False, "reason": res["reason"]}
        y, ch = to_channels(res["audio"], plan.channels)
        y, rep = chain.run(y, SR, {"normalise": {"mode": plan.norm_mode, "target": plan.norm_target},
                                   "limiter": {"ceilingDbtp": -1.0, "maxGrDb": 6.0}})
        w = res["window"]
        info.update({"window": w, "window_raw_s": w["window_s"], "tail": res["shaping"], "channels": ch,
                     "events": res["n_events"], "true_onsets": res["n_true"], "window_candidates": res["candidates"],
                     "pre_hit": res.get("pre_hit"), "build_up": res.get("build_up")})
        steps += [f"window {w['len_ms']:.0f} ms at {w['onset_s']:.3f} s ({w['onset_kind']} onset; {w['why']})",
                  f"exp cap tail from {res['shaping']['knee_ms']:g} ms to -60 dB (cut up to {res['shaping']['max_cut_db']:g} dB)",
                  f"channels {ch['channels']}", rep["summary"]]
        ok, reason = res["onset_ok"] and res["usable"], res["reason"]
        info["true_onset"] = res["onset_ok"]
        info["onset_verified"] = res["onset_verified"]
        if res.get("onset_note"):
            info["onset_note"] = res["onset_note"]
    info["onset_ok"] = ok
    info["reason"] = reason
    info["chain"] = ", ".join(steps) + ", PCM 24-bit"
    info["normalise"] = {k: rep.get(k) for k in ("normalise", "target", "measuredBefore", "preGainDb", "limiterGrDb", "achieved")}
    rej_dir = rejected or out_dir.parent / f"{out_dir.name}-rejected"
    dest = out_dir if ok else rej_dir
    for stale in (rej_dir if ok else out_dir,):          # a re-run moves a candidate, never duplicates it
        for ext in (".wav", ".proc.json"):
            (stale / f"{rec['candidate']}{ext}").unlink(missing_ok=True)
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / f"{rec['candidate']}.wav"
    sf.write(str(out), y.astype(np.float32), SR, subtype="PCM_24")
    info["path"] = str(out)
    info["summary_after"] = measure.summary(y, SR)
    (dest / f"{rec['candidate']}.proc.json").write_text(json.dumps(info, indent=1, ensure_ascii=False, default=float), "utf-8")
    return info


def sources_record(info: dict, rec: dict, variant: int, date: str, tools: dict) -> dict:
    """SOURCES.json record of a processed candidate: one `gen` layer, raw clip test on the float copy."""
    from build import ledger, sources
    from gen import sa3

    f32 = Path(rec["files"]["f32"]["path"])
    window = info.get("window_raw_s")
    wav = Path(info["path"])
    sha = ledger.sha256_file(wav)
    mid = _model_id(rec)
    layer = {"id": "sa3", "role": "whole", "kind": "gen", "tool": TOOL, "model": mid, "licence": sa3.STABILITY,
             "licenceAccepted": "licences/stability-registration.txt", "source": f32.name,
             "sourceSha256": rec["files"]["f32"]["sha256"], "prompt": rec.get("prompt"), "seed": int(rec["seed"]),
             "cfg": float(rec.get("cfg", 1.0)), "aiSteps": ["generate"], "record": Path(str(rec.get("_path") or "")).name,
             "rawQa": sources.raw_qa([sources.clip_scan_file(f32, window)])}
    if window:
        layer["window"] = [float(v) for v in window]
    return {"id": info["id"], "game": info["game"], "variant": variant, "renderVariant": variant, "sha256": sha,
            "date": date, "run": wav.parent.parent.name, "master": wav.name, "masterSha256": sha,
            "durationMs": info["summary_after"]["durationMs"], "sampleRate": SR,
            "channels": int(info["summary_after"]["channels"]), "layers": [layer], "chain": info["chain"],
            "tools": tools, "models": [mid], "aiSteps": [], "aiInputAllowed": True,
            "rawQa": f"{wav.stem}.proc.json", "review": None}


def process_many(records: list[Path], card: dict, out_dir: Path, *, whole: bool | None = None, notch: bool = False,
                 rejected: Path | None = None, force: bool = False, two_part: bool = False,
                 build_up: bool = False) -> dict:
    """Process records into out_dir; write SOURCES.json and licences.rows.jsonl for the kept files."""
    from build import ledger, render
    from gen import sa3

    out_dir.mkdir(parents=True, exist_ok=True)
    date = ledger.today()
    tools = render.tool_versions()
    src_path = out_dir / "SOURCES.json"
    data = ledger.read_sources(src_path)
    kept, rej, skipped = [], [], 0
    rows = None
    for rp in records:
        rec = sa3.read_record(rp)
        rec["_path"] = str(rp)
        name = rec["candidate"]
        if not force and (out_dir / f"{name}.wav").is_file() and (out_dir / f"{name}.proc.json").is_file():
            skipped += 1
            continue
        info = process_record(rec, card, out_dir, whole=whole, notch=notch, rejected=rejected, two_part=two_part,
                              build_up=build_up)
        if not info.get("onset_ok"):
            rej.append({"candidate": name, "reason": info.get("reason")})
            data.pop(f"{name}.wav", None)
            continue
        data[f"{name}.wav"] = sources_record(info, rec, len(kept) + 1, date, tools)
        kept.append(name)
        if rows is None:
            rows = (rec.get("licence") or {}).get("rows") or sa3.licence_rows(sa3.load_install())[0]
    ledger.write_sources(src_path, data)
    if rows:
        ledger.append_rows(out_dir / "licences.rows.jsonl", rows)
    return {"kept": len(kept), "rejected": rej, "skipped": skipped, "sources": str(src_path)}


def collect_records(paths: list[str]) -> list[Path]:
    out = []
    for p in map(lambda s: Path(s).expanduser(), paths):
        if p.is_dir():
            out += sorted(f for f in p.glob("*.json") if not f.name.startswith("_") and not f.name.endswith(".proc.json"))
        elif p.is_file():
            out.append(p)
        else:
            raise FileNotFoundError(f"không thấy {p}")
    return out


def main(argv: list[str] | None = None) -> int:
    from common import env
    from gen import sa3

    ap = argparse.ArgumentParser(prog="gen.process", description="Xử lý đầu ra mô hình thành ứng viên nghe (mục 5.1 bước 4).")
    ap.add_argument("inputs", nargs="+", help="thư mục raw (có hồ sơ <tên>.json) hoặc file hồ sơ")
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rejected", help="nơi để bản không có đầu tiếng thật (mặc định <out>-rejected)")
    ap.add_argument("--whole", action="store_true", help="giữ trọn âm tự nhiên (mặc định với sinh vật)")
    ap.add_argument("--notch-comb", action="store_true", help="lọc khấc vạch lược của bộ giải mã (nền)")
    ap.add_argument("--two-part", action="store_true", help="âm hai nhịp có chủ ý (word.load): nhịp nhẹ 20–90 ms trước nhịp chính không bị coi là gõ hai lần")
    ap.add_argument("--build-up", action="store_true", help="âm hành động có phần tụ lực hay nhiều nhịp (Q6): phần đầu nhỏ hơn không bị coi là gõ hai lần, nhịp sau không cắt cửa sổ; vẫn cắt ở độ dài tối đa của thẻ")
    ap.add_argument("--force", action="store_true", help="xử lý lại file đã có")
    a = ap.parse_args(argv)
    env.apply()
    card = sa3.read_card(a.spec)
    res = process_many(collect_records(a.inputs), card, Path(a.out).expanduser(), whole=True if a.whole else None,
                       notch=a.notch_comb, rejected=Path(a.rejected).expanduser() if a.rejected else None, force=a.force,
                       two_part=a.two_part, build_up=a.build_up)
    print(json.dumps({**res, "rejected": len(res["rejected"])}, ensure_ascii=False))
    for r in res["rejected"]:
        print(f"  loại {r['candidate']}: {r['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
