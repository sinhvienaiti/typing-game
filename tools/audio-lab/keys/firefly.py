"""Survey of the owner's Adobe Firefly keyboard takes (stage 1 of the Firefly keyboard lane, 29/10/2026).

The owner made 408 WAVs with Adobe Firefly "Generate Sound Effects" (Adobe model, commercially safe):
9 folders "Adobe_2026-10-29", "Adobe_2026-10-29 (1)" ... "(7)", "(8) (1)", 12 s each (a few 1 s),
48 kHz stereo 16-bit. This module only reads them (never writes, moves or deletes a source file) and
measures them without imposing the rejected five-profile list. Ticket 189 builds one
keyboard per folder, merging only near duplicates and a compatible small folder.

  run.sh keys firefly survey [--src DIR] [--out DIR] [--folders 0,3] [--limit N] [--no-sheets] [--no-export]
  run.sh keys.firefly survey ...            # same, module form

Per take: the shared stroke finder (keys/strokes.py: components, presses, press+release, isolation)
finds every press. A press that strokes.find_strokes keeps is "clean" (extractable as one stroke); a
press it skips (crowded, no quiet before) is still measured, in a window that ends 1 ms before the next
press, and flagged. Per stroke: peak, attack, main hit time, length to -40 dB, centroid, six band
energies, hiss ratio (4-8 kHz vs 150-400 Hz), floors before / inside / after the stroke, the floor the
stroke would have once mastered to -27 LUFS-M, stereo correlation (all, < 400 Hz, > 2 kHz) and the
mono fold loss, clipping, a reverb-tail estimate (decay slope, T60, late energy) and a spacebar score.
Per take: stroke count, rhythm regularity, gap floor, gap activity (rustle), stray events and a 0-10
cleanliness score. Per folder: medians, ranks across folders, heuristic tags, best takes, the mean
stroke spectrum.

Outputs (git-ignored): <out>/features.json, <out>/summary.json, <out>/sheets/<slug>.png (contact sheet),
<out>/sheets/spectra-overlay.png (folders against the rejected Codex 182 and Stable Audio 3 sets),
<out>/strokes/<slug>/{key,space}/*.wav + index.json (representative single strokes, 48 kHz mono 24-bit,
not level-normalised; index.json carries the gain to -27 LUFS-M).

The tags and the cleanliness score are measurement heuristics, not listening verdicts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import struct
import sys
from pathlib import Path

import numpy as np
from scipy import ndimage, signal

from keys import strokes

SR = strokes.SR
REPO = Path(__file__).resolve().parents[3]
SRC = Path.home() / "Downloads" / "typing-mp3"
OUT = REPO / "tmp" / "keys-firefly" / "survey"
CODEX_SETS = REPO / "tmp" / "keys-codex"
SA3_SETS = Path.home() / "AudioLab" / "work" / "_keys"
SCHEMA = "keys-firefly-survey/1"

BANDS = (("b80_150", 80, 150), ("b150_400", 150, 400), ("b400_2k", 400, 2000),
         ("b2k_4k", 2000, 4000), ("b4k_8k", 4000, 8000), ("b8k_up", 8000, 24000))
TARGET_LUFS_M = -27.0      # per-file master level of the deliverable
FLOOR_GATE_DBFS = -70.0    # deliverable: floor between / after strokes once mastered
WELCH = {"nperseg": 2048, "nfft": 8192}


# ---------------------------------------------------------------- small helpers

def _db(p: float) -> float:
    return float(10 * np.log10(max(float(p), 1e-20)))


def _lvl(x: np.ndarray) -> float:
    """Mean power in dBFS (-200 for an empty slice)."""
    return _db(np.mean(np.asarray(x, dtype=np.float64) ** 2)) if len(x) else -200.0


def _r(v, n: int = 2):
    if v is None:
        return None
    v = float(v)
    return round(v, n) if np.isfinite(v) else None


def slug(folder: str) -> str:
    """'Adobe_2026-10-29 (8) (1)' -> 'adobe-2026-10-29-8-1'."""
    s = re.sub(r"[^a-z0-9]+", "-", folder.lower()).strip("-")
    return s


def file_id(name: str) -> str:
    """'An edited Foley sequence of isol 111746 jTN.wav' -> '111746-jTN'."""
    m = re.search(r"(\d+) (\w+)\.wav$", name)
    return f"{m.group(1)}-{m.group(2)}" if m else Path(name).stem.replace(" ", "_")


def provenance(path: Path) -> dict:
    """The take's C2PA provenance link from its XMP chunk (read only, never fetched) and SHA-256."""
    b = path.read_bytes()
    out = {"sha256": hashlib.sha256(b).hexdigest(), "c2pa_manifest": None, "chunks": []}
    i = 12
    while i + 8 <= len(b):
        cid = b[i:i + 4].decode("latin-1")
        n = struct.unpack("<I", b[i + 4:i + 8])[0]
        out["chunks"].append(cid)
        if cid == "XMP ":
            m = re.search(rb'dcterms:provenance="([^"]+)"', b[i + 8:i + 8 + n])
            if m:
                out["c2pa_manifest"] = m.group(1).decode("utf-8", "replace")
        i += 8 + n + (n & 1)
    return out


# ---------------------------------------------------------------- loading and detection

def load(path: Path) -> tuple[np.ndarray, np.ndarray, dict]:
    """-> (mono 48 kHz HPF 30 Hz, stereo 48 kHz HPF 30 Hz (n, 2), info incl. clip count on the raw samples)."""
    import soundfile as sf
    x, sr = sf.read(str(path), always_2d=True, dtype="float64")
    clip_idx = np.flatnonzero(np.any(np.abs(x) >= 32766 / 32768, axis=1))
    m, info = strokes.prepare(x, sr)
    lr = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, axis=1)
    lr = signal.sosfiltfilt(signal.butter(2, 30.0, "high", fs=sr, output="sos"), lr, axis=0)
    if sr != SR:
        from build import dsp
        lr = dsp.resample(lr, sr, SR)
    info.update({"sr": int(sr), "channels": int(x.shape[1]), "duration_s": round(len(x) / sr, 3),
                 "clip_samples": int(clip_idx.size), "clip_idx": clip_idx, "peak_dbfs": _r(20 * np.log10(np.abs(x).max() + 1e-12))})
    return m, lr[:len(m)], info


COMP_SPAN_DB = 45.0       # components down to 45 dB under the take's peak (Firefly releases sit 30-37 dB down;
                          # at the shared 35 dB a release and the next key merge into one component)
PRESS_SPAN_DB = 20.0      # a press is within 20 dB of the take's loudest component
MERGE_MS = 30.0           # a second press candidate this soon is the same press (finger touch, chatter)
RELEASE_DROP_DB = 6.0     # a loud follow-up is a release when >= 6 dB quieter ...
RELEASE_LOWER_DB = 6.0    # ... and >= 6 dB thinner below 400 Hz than its press (an upstroke has no bottom-out body)
PRE_QUIET_DB = 30.0       # clean: 5 ms level 30..2 ms before the onset >= 30 dB under the press
DECAY_DB = 40.0           # clean: the stroke falls 40 dB under its press before the next press
SEARCH_MS = 400.0         # longest press-to-end span searched for a release and the decay
SINGLE_TAKE_S = 3.0       # shorter takes are single keystrokes: a follow-up within 260 ms is the release


def _low_share_db(m: np.ndarray, on: int) -> float:
    """Energy share below 400 Hz in the first 12 ms of a component, dB."""
    seg = m[on:on + int(0.012 * SR)]
    if len(seg) < 64:
        return 0.0
    f, P = signal.welch(seg, SR, nperseg=len(seg), nfft=4096)
    return _db(P[(f >= 60) & (f < 400)].sum() / (P[f >= 60].sum() + 1e-30))


def detect(m: np.ndarray, take: str = "t") -> tuple[list[dict], list, float]:
    """Every press of a take, in time order, with its window and release.

    Reuses strokes.components (sound components of the 5 ms level, here down to COMP_SPAN_DB) and strokes'
    file-start rule, but not
    find_strokes' press rule: there a component 3 dB quieter within 260 ms of a press is its release,
    which in Firefly's fast passages (keys 90-130 ms apart, levels varying 3-15 dB) swallows real presses.
    Here a press is a component within PRESS_SPAN_DB of the loudest, not within MERGE_MS of the press
    before, and not an upstroke (RELEASE_DROP_DB quieter and RELEASE_LOWER_DB thinner below 400 Hz than
    the press it follows within 260 ms; in a take under SINGLE_TAKE_S, any follow-up within 260 ms
    that is not 3 dB louder). Every other component belongs to the press before it; the
    loudest of them 25 ms or more after the press is its release.

    Window: 1 ms before the onset to the end (last 5 ms frame within DECAY_DB of the press + 5 ms),
    searched up to SEARCH_MS and never past 1 ms before the next press. Clean = quiet before
    (PRE_QUIET_DB, or the file-start evidence rule) and decayed before the next press; a clean press
    carries a strokes.Stroke so strokes.render can cut it."""
    comps, G = strokes.components(m, span_db=COMP_SPAN_DB)
    single = len(m) < int(SINGLE_TAKE_S * SR)
    presses: list[dict] = []
    for c in comps:
        if c.peak_db < G - PRESS_SPAN_DB:
            continue
        if presses:
            q = presses[-1]
            dt = c.onset - q["onset"]
            if dt < int(MERGE_MS / 1000 * SR):
                if c.peak_db > q["peak_db"]:
                    q["peak_db"] = c.peak_db
                continue
            if (dt < int(0.260 * SR) and q["peak_db"] - c.peak_db >= RELEASE_DROP_DB
                    and q["low_db"] - _low_share_db(m, c.onset) >= RELEASE_LOWER_DB):
                continue
            if single and dt < int(0.260 * SR) and c.peak_db <= q["peak_db"] + 3.0:
                continue                     # a 1 s single-keystroke take: the loud follow-up is the release
        presses.append({"onset": c.onset, "peak_db": c.peak_db, "low_db": _low_share_db(m, c.onset)})
    _, e5 = strokes.envelope(m, SR, 5.0, 1.0)
    hop = int(0.001 * SR)
    for i, p in enumerate(presses):
        on = p["onset"]
        nxt = presses[i + 1]["onset"] if i + 1 < len(presses) else len(m)
        p["next"] = nxt
        p["a"] = max(0, on - hop)
        limit = min(len(m), nxt - hop, on + int(SEARCH_MS / 1000 * SR))
        f0, f1 = on // hop, max(on // hop + 1, limit // hop - 4)
        loud = np.flatnonzero(e5[f0:f1] >= p["peak_db"] - DECAY_DB)
        end = (f0 + int(loud[-1])) * hop + 5 * hop if loud.size else on + 10 * hop
        decayed = bool(loud.size == 0 or f0 + int(loud[-1]) < f1 - 2)
        p["end"] = min(end, limit)
        p["b"] = max(p["end"], p["a"] + 10 * hop)
        inner = [d for d in comps if on + int(0.025 * SR) <= d.onset < p["end"] and d.onset != on]
        rel = max(inner, key=lambda d: d.peak_db) if inner else None
        p["release"] = rel.onset if rel else None
        p["release_peak_db"] = rel.peak_db if rel else None
        why = None
        if on < int(0.0015 * SR):
            start_kind = "file-start"
            if not strokes._file_start_ok(m, on, p["peak_db"]):
                why = "sounds from the first sample, onset not verified"
        else:
            start_kind = "quiet"
            pa = max(0, on - int(0.030 * SR))
            pre = e5[pa // hop:max(pa // hop + 1, (on - 2 * hop) // hop - 4)]
            if i > 0 and on - presses[i - 1]["end"] < 2 * hop:
                why = "the key before has not decayed"
            elif pre.size and float(pre.max()) > p["peak_db"] - PRE_QUIET_DB:
                why = f"no quiet before the onset ({float(pre.max()) - p['peak_db']:.0f} dB)"
        if why is None and p["end"] >= len(m) - int(0.030 * SR):
            why = "cut by the end of the take"
        if why is None and not decayed:
            why = (f"next key {(nxt - on) / SR * 1000:.0f} ms later, not decayed {DECAY_DB:.0f} dB"
                   if nxt - hop <= on + int(SEARCH_MS / 1000 * SR) else f"not decayed {DECAY_DB:.0f} dB in {SEARCH_MS:.0f} ms")
        p["clean"] = why is None
        p["why"] = why
        p["stroke"] = None
        if p["clean"]:
            p["stroke"] = strokes.Stroke(take=take, index=i, onset=on, press_peak_db=p["peak_db"], press_end=p["end"],
                                         release_onset=p["release"], release_peak_db=p["release_peak_db"],
                                         release_end=p["end"] if rel else None,
                                         kind="press+release" if rel else "press", start_kind=start_kind)
    return presses, comps, G


# ---------------------------------------------------------------- per-stroke numbers

def psd(y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = len(y)
    nper = min(WELCH["nperseg"], n)
    return signal.welch(y, SR, nperseg=nper, nfft=max(WELCH["nfft"], nper))


def bands(f: np.ndarray, P: np.ndarray) -> dict:
    tot = float(P[(f >= 20)].sum()) + 1e-30
    out = {}
    for name, lo, hi in BANDS:
        out[name] = _r(_db(P[(f >= lo) & (f < hi)].sum() / tot), 1)
    return out


def hiss_ratio(f: np.ndarray, P: np.ndarray) -> float:
    """4-8 kHz energy against the 150-400 Hz body, dB (codex182 definition)."""
    return _db(P[(f >= 4000) & (f < 8000)].sum()) - _db(P[(f >= 150) & (f < 400)].sum())


def centroid(f: np.ndarray, P: np.ndarray) -> float:
    s = P[f >= 20]
    return float(np.sum(f[f >= 20] * s) / (s.sum() + 1e-30))


def flatness(f: np.ndarray, P: np.ndarray, lo: float = 400.0, hi: float = 8000.0) -> float:
    """Wiener entropy 400-8 kHz (0 = tonal, 1 = white noise)."""
    s = P[(f >= lo) & (f < hi)] + 1e-30
    return float(np.exp(np.mean(np.log(s))) / np.mean(s))


def stereo(lr: np.ndarray) -> dict:
    """Correlation of L and R (whole band, < 400 Hz, > 2 kHz) and what folding to mono loses, dB."""
    L, R = lr[:, 0], lr[:, 1]

    def corr(a, b):
        if np.std(a) < 1e-12 or np.std(b) < 1e-12:
            return None
        return float(np.corrcoef(a, b)[0, 1])

    out = {"corr": _r(corr(L, R), 3)}
    if len(lr) > 64:
        lo = signal.sosfilt(signal.butter(4, 400, "low", fs=SR, output="sos"), lr, axis=0)
        hi = signal.sosfilt(signal.butter(4, 2000, "high", fs=SR, output="sos"), lr, axis=0)
        out["corr_lo"] = _r(corr(lo[:, 0], lo[:, 1]), 3)
        out["corr_hi"] = _r(corr(hi[:, 0], hi[:, 1]), 3)
    e_lr = float(np.mean(np.sum(lr ** 2, axis=0)))
    e_mid = float(np.sum(lr.mean(axis=1) ** 2))
    out["mono_loss_db"] = _r(_db(e_lr) - _db(e_mid), 2)
    return out


def tail(m: np.ndarray, from_s: int, limit: int, ref_db: float) -> dict:
    """Reverb-tail estimate after the stroke's last component peak: the 5 ms level's decay slope between
    6 and 36 dB down (or 6 dB over the floor of the span), T60 from that slope, and the late energy
    40-120 ms after the peak against the first 20 ms (only when nothing else sounds in that span)."""
    seg = m[from_s:limit]
    out = {"slope_db_ms": None, "t60_ms": None, "late_db": None, "span_ms": _r(len(seg) / SR * 1000, 1)}
    if len(seg) < int(0.030 * SR):
        return out
    st5, e5 = strokes.envelope(seg, SR, 5.0, 1.0)
    p = int(np.argmax(e5[:12]))
    top = float(e5[p])
    floor = float(np.min(e5[p:])) if len(e5) > p + 1 else top - 60
    lo_db = max(top - 36.0, floor + 6.0)
    after = e5[p:]
    i0 = np.flatnonzero(after <= top - 6.0)
    i1 = np.flatnonzero(after <= lo_db)
    if i0.size and i1.size:
        if i1[0] - i0[0] >= 3:
            xs = np.arange(i0[0], i1[0] + 1)
            slope = float(np.polyfit(xs, after[i0[0]:i1[0] + 1], 1)[0])   # dB per 1 ms hop
        else:                                # falls faster than a fit can follow: very dry
            slope = float(after[i1[0]] - top) / max(1, int(i1[0]))
        out["slope_db_ms"] = _r(slope, 3)
        out["t60_ms"] = _r(min(5000.0, 60.0 / -slope), 1) if slope < -1e-3 else 5000.0
    pk = from_s + int(st5[p])
    if pk + int(0.120 * SR) <= limit:
        early = _lvl(m[pk:pk + int(0.020 * SR)])
        late = _lvl(m[pk + int(0.040 * SR):pk + int(0.120 * SR)])
        out["late_db"] = _r(late - early, 1)
    return out


def _band_decay_ms(y: np.ndarray, lo: float, hi: float, drop_db: float = 30.0) -> float | None:
    """Time from a band's 1 ms peak (first 20 ms) until its 1 ms level falls drop_db under it."""
    if len(y) < int(0.012 * SR):
        return None
    z = signal.sosfilt(signal.butter(4, [lo, hi], "band", fs=SR, output="sos"), y)
    _, e = strokes.envelope(z, SR, 1.0, 0.25)
    k = int(np.argmax(e[:80]))
    below = np.flatnonzero(e[k:] < e[k] - drop_db)
    return float(below[0]) * 0.25 if below.size else None


def ring(f: np.ndarray, P: np.ndarray, lo: float = 400.0, hi: float = 6000.0) -> tuple[float, float]:
    """A narrow tonal line in the press decay: the largest prominence (dB) of the spectrum over its own
    running median (+-150 Hz), 400-6000 Hz, and its frequency. A natural decay stays under ~10 dB; a
    sustained ping or ring stands 15-25 dB over its neighbourhood."""
    d = 10 * np.log10(P + 1e-30)
    k = int(150.0 / (f[1] - f[0])) * 2 + 1
    base = ndimage.median_filter(d, size=k, mode="nearest")
    band = (f >= lo) & (f <= hi)
    prom = (d - base)[band]
    i = int(np.argmax(prom))
    return float(prom[i]), float(f[band][i])


def stroke_features(m: np.ndarray, lr: np.ndarray, p: dict, prev_end: int | None = None) -> dict:
    """All numbers of one press (dict p from detect): window [a, b) = 1 ms before the onset to the end."""
    from build import measure
    a, b, on = p["a"], p["b"], p["onset"]
    hop = int(0.001 * SR)
    y = m[a:b]
    st1, e1 = strokes.envelope(y, SR, 1.0, 0.25)
    pk = int(np.argmax(e1))
    pk_db = float(e1[pk])
    on_rel = on - a
    attack = max(0.0, (int(st1[pk]) - on_rel) / SR * 1000)
    main_i = int(np.flatnonzero(e1 >= pk_db - 3.0)[0])
    main_ms = max(0.0, (int(st1[main_i]) - on_rel) / SR * 1000)
    st5, e5 = strokes.envelope(y, SR, 5.0, 1.0)
    pk5 = float(e5.max())
    loud = np.flatnonzero(e5 >= pk5 - 40.0)
    len40 = (int(st5[loud[-1]]) + 5 * hop - on_rel) / SR * 1000 if loud.size else 0.0
    rel = p.get("release")
    press_b = (rel - a) if rel is not None and rel > on + 10 * hop else len(y)
    pe = e5[:max(1, press_b // hop)]
    dk = np.flatnonzero(pe < pk5 - 40.0)
    press_decay = float(dk[0]) if dk.size else None
    f, P = psd(y)
    fp, Pp = psd(m[on:on + min(30 * hop, max(5 * hop, press_b - on_rel))])
    press_y = y[on_rel:press_b]
    hiss_tail = None
    if press_b - on_rel - 15 * hop >= 10 * hop:
        ft, Pt = psd(y[on_rel + 15 * hop:press_b])
        hiss_tail = hiss_ratio(ft, Pt)
    ring_db, ring_hz, low_sus, low_edge, hold_lv = None, None, None, None, None
    body_b = min(press_b, on_rel + 120 * hop)
    if body_b - (on_rel + 20 * hop) >= 20 * hop:
        seg = y[on_rel + 20 * hop:body_b]
        fr, Pr = signal.welch(seg, SR, nperseg=min(len(seg), 2048), nfft=16384)
        ring_db, ring_hz = ring(fr, Pr)
    if body_b - (on_rel + 30 * hop) >= 15 * hop:
        lo_now = signal.sosfiltfilt(signal.butter(4, [60, 450], "band", fs=SR, output="sos"), y)
        low_sus = _lvl(lo_now[on_rel + 30 * hop:body_b]) - _lvl(lo_now[on_rel:on_rel + 10 * hop])
        fs_, Ps_ = signal.welch(y[on_rel + 30 * hop:body_b], SR, nperseg=min(body_b - on_rel - 30 * hop, 2048), nfft=8192)
        low_edge = _db(Ps_[(fs_ >= 300) & (fs_ < 450)].mean()) - _db(Ps_[(fs_ >= 550) & (fs_ < 750)].mean())
    if rel is not None and rel - on > 60 * hop:
        hold_lv = float(np.median(e5[(on_rel + 40 * hop) // hop:max((on_rel + 41 * hop) // hop, (rel - a) // hop - 6)]))
    feat = {
        "t_ms": _r(on / SR * 1000, 1), "clean": p["clean"], "why": p["why"],
        "kind": "press+release" if rel is not None else "press",
        "release_gap_ms": _r((rel - on) / SR * 1000, 1) if rel is not None else None,
        "window_ms": _r((b - a) / SR * 1000, 1), "next_press_ms": _r((p["next"] - on) / SR * 1000, 1),
        "peak_dbfs": _r(20 * np.log10(np.abs(y).max() + 1e-12), 1),
        "attack_ms": _r(attack, 2), "main_ms": _r(main_ms, 2),
        "len40_ms": _r(len40, 1), "len40_hits_window": not p["clean"] and bool(loud.size and loud[-1] >= len(e5) - 2),
        "press_decay40_ms": _r(press_decay, 1),
        "hf_decay30_ms": _r(_band_decay_ms(press_y, 4000, 8000), 2),
        "body_decay30_ms": _r(_band_decay_ms(press_y, 150, 400), 2),
        "centroid_hz": _r(centroid(f, P), 0), "centroid_press_hz": _r(centroid(fp, Pp), 0),
        "bands_db": bands(f, P), "hiss_db": _r(hiss_ratio(f, P), 1), "hiss_tail_db": _r(hiss_tail, 1),
        "flatness": _r(flatness(f, P), 3),
        "ring_db": _r(ring_db, 1), "ring_hz": _r(ring_hz, 0),
        "low_sustain_db": _r(low_sus, 1), "low_edge_db": _r(low_edge, 1),
        "peak_hz": _r(f[(f >= 100) & (f <= 8000)][int(np.argmax(P[(f >= 100) & (f <= 8000)]))], 0),
    }
    if rel is not None:
        feat["release_rel_db"] = _r(_lvl(m[rel:rel + 5 * hop]) - _lvl(m[on:on + 5 * hop]), 1)
    # floors in dBFS: before the onset (after the key before has ended), inside the hold (press decayed,
    # release not yet), after the end (10th percentile of the 5 ms level until the next key, <= 150 ms)
    pre_a = max(0 if prev_end is None else prev_end, on - 30 * hop)
    pre = _lvl(m[pre_a:on - 2 * hop]) if on - 2 * hop - pre_a >= 5 * hop else None
    post = None
    post_a, post_b = p["b"], min(len(m), p["next"] - 3 * hop, p["b"] + 150 * hop)
    if post_b - post_a >= 15 * hop:
        _, ep = strokes.envelope(m[post_a:post_b], SR, 5.0, 1.0)
        post = float(np.percentile(ep, 10))
    gap = None
    if rel is not None and rel - on > 30 * hop:
        mid = e5[12:max(0, (rel - a) // hop - 6)]
        gap = float(np.min(mid)) if mid.size else None
    lm = measure.lufs_m_max(y, SR)
    gain = TARGET_LUFS_M - lm
    worst = max([v for v in (post, gap) if v is not None], default=None)   # pre is often the key before's tail
    feat["floor"] = {"pre_dbfs": _r(pre, 1), "hold_gap_dbfs": _r(gap, 1), "post_dbfs": _r(post, 1),
                     "pre_rel_db": _r(None if pre is None else pre - pk_db, 1),
                     "post_rel_db": _r(None if post is None else post - pk_db, 1)}
    feat["lufs_m"] = _r(lm, 2)
    feat["gain_to_master_db"] = _r(gain, 2)
    feat["floor_at_master_dbfs"] = _r(None if worst is None else worst + gain, 1)
    feat["hold_level_at_master_dbfs"] = _r(None if hold_lv is None else hold_lv + gain, 1)
    feat["true_peak_at_master_dbtp"] = _r(measure.true_peak_db(y, SR) + gain, 2)
    feat["stereo"] = stereo(lr[a:b])
    last = max(on, rel or on)
    feat["tail"] = tail(m, last, min(len(m), p["next"] - 2 * hop, last + 250 * hop), pk_db)
    return feat


def space_flags(feats: list[dict], ref: list[dict] | None = None) -> None:
    """Spacebar-like = lower, longer, heavier than the take's other strokes (robust z within the take, or
    within `ref` when the take has under 6 strokes): score >= 2, centroid z <= -0.5 and length z >= 0.
    Writes space_score and space_like in place."""
    base = ref if ref is not None and len(feats) < 6 else feats
    if len(base) < 3:
        for f in feats:
            f["space_score"], f["space_like"] = None, False
        return

    def vec(fs, key):
        return np.array([key(f) for f in fs], dtype=float)

    keys = {
        "lc": lambda f: np.log2(max(f["centroid_hz"] or 1.0, 1.0)),
        "len": lambda f: f["len40_ms"] or 0.0,
        "low": lambda f: max(f["bands_db"]["b80_150"] or -60, f["bands_db"]["b150_400"] or -60),
        "pk": lambda f: f["peak_dbfs"] or -60.0,
    }
    z = {}
    for k, fn in keys.items():
        v0 = vec(base, fn)
        med = float(np.median(v0))
        mad = float(np.median(np.abs(v0 - med))) * 1.4826 + 1e-6
        z[k] = (vec(feats, fn) - med) / mad
    score = -z["lc"] + 0.6 * np.clip(z["len"], -3, 3) + 0.6 * np.clip(z["low"], -3, 3) + 0.3 * np.clip(z["pk"], -3, 3)
    for i, f in enumerate(feats):
        f["space_score"] = _r(score[i], 2)
        f["space_like"] = bool(score[i] >= 2.0 and z["lc"][i] <= -0.5 and z["len"][i] >= 0.0)


# ---------------------------------------------------------------- per-take numbers

def take_numbers(m: np.ndarray, presses: list[dict], comps: list, G: float, feats: list[dict]) -> dict:
    """Gap = 20 ms frames clear of every stroke (1 ms before the onset .. 50 ms after its end). Gap floor =
    10th percentile of their level; activity = share of gap frames that would sit over -60 dBFS once the
    take's strokes are mastered to -27 LUFS-M (rustle, ghost keys, tails that never settle)."""
    n20 = int(0.020 * SR)
    nf = len(m) // n20
    busy = np.zeros(len(m), bool)
    for p in presses:
        busy[max(0, p["a"] - int(0.005 * SR)):min(len(m), p["end"] + int(0.050 * SR))] = True
    lv = np.array([_lvl(m[i * n20:(i + 1) * n20]) for i in range(nf)])
    free = np.array([not busy[i * n20:(i + 1) * n20].any() for i in range(nf)], dtype=bool)
    sel = free if free.sum() >= 5 else (lv <= np.percentile(lv, 10))
    gap_lv = lv[sel]
    floor = float(np.percentile(gap_lv, 10)) if gap_lv.size else None
    hs = signal.sosfilt(signal.butter(4, [4000, 8000], "band", fs=SR, output="sos"), m)
    q = np.flatnonzero(sel)
    hiss_gap = _db(np.mean([np.mean(hs[i * n20:(i + 1) * n20] ** 2) for i in q])) if q.size else None
    clean = [f for f in feats if f["clean"]] or feats
    gains = [f["gain_to_master_db"] for f in clean if f["gain_to_master_db"] is not None]
    med_gain = float(np.median(gains)) if gains else None
    activity = None
    if gap_lv.size and med_gain is not None and free.sum() >= 5:
        activity = float(np.mean(gap_lv + med_gain > -60.0))
    on = np.array([p["onset"] for p in presses]) / SR
    ioi = np.diff(on) if len(on) > 1 else np.array([])
    ioi_k = ioi[ioi < 1.0]                                   # a pause between phrases is not the rhythm
    cv = float(np.std(ioi_k) / np.mean(ioi_k)) if len(ioi_k) >= 3 else None
    # hard edits: a 1 ms frame that drops from audible (> -90 dBFS) straight to digital zero (< -140 dBFS)
    n1 = int(0.001 * SR)
    lv1 = 10 * np.log10(np.mean(m[:len(m) // n1 * n1].reshape(-1, n1) ** 2, axis=1) + 1e-20)
    hard_cuts = int(np.sum((lv1[:-1] > -90.0) & (lv1[1:] < -140.0)))
    digital = float(np.mean(gap_lv < -150.0)) if gap_lv.size else None
    attached = set()
    for p in presses:
        for d in comps:
            if p["onset"] - int(0.002 * SR) <= d.onset < max(p["end"], p["onset"] + int(0.260 * SR)):
                attached.add(d.onset)
    stray = sum(1 for d in comps if d.onset not in attached)
    return {
        "presses": len(presses), "clean": sum(1 for f in feats if f["clean"]),
        "space_like": sum(1 for f in feats if f.get("space_like")),
        "rhythm": {"ioi_median_ms": _r(np.median(ioi_k) * 1000, 1) if len(ioi_k) else None,
                   "ioi_cv": _r(cv, 3), "regularity": _r(None if cv is None else max(0.0, 1.0 - cv), 3),
                   "presses_per_s": _r(len(presses) / max(1e-3, len(m) / SR), 2)},
        "hard_cuts_to_digital_zero": hard_cuts,
        "gap": {"floor_dbfs": _r(floor, 1), "hiss_4k8k_dbfs": _r(hiss_gap, 1), "activity": _r(activity, 3),
                "digital_silence_share": _r(digital, 3),
                "frames": int(free.sum()), "median_gain_to_master_db": _r(med_gain, 2),
                "floor_at_master_dbfs": _r(None if floor is None or med_gain is None else floor + med_gain, 1)},
        "stray_events": stray, "components": len(comps), "loudest_component_db": _r(G, 1),
    }


def med(vals, n: int = 1):
    v = [x for x in vals if x is not None and np.isfinite(x)]
    return _r(np.median(v), n) if v else None


def stroke_medians(fs: list[dict]) -> dict:
    return {
        "n": len(fs),
        "centroid_hz": med([f["centroid_hz"] for f in fs], 0),
        "centroid_press_hz": med([f["centroid_press_hz"] for f in fs], 0),
        "hiss_db": med([f["hiss_db"] for f in fs]),
        "hiss_tail_db": med([f["hiss_tail_db"] for f in fs]),
        "hf_decay30_ms": med([f["hf_decay30_ms"] for f in fs], 2),
        "body_decay30_ms": med([f["body_decay30_ms"] for f in fs], 2),
        "bands_db": {k: med([f["bands_db"][k] for f in fs]) for k, _, _ in BANDS},
        "len40_ms": med([f["len40_ms"] for f in fs]),
        "press_decay40_ms": med([f["press_decay40_ms"] for f in fs]),
        "release_gap_ms": med([f["release_gap_ms"] for f in fs]),
        "release_rel_db": med([f.get("release_rel_db") for f in fs]),
        "attack_ms": med([f["attack_ms"] for f in fs], 2),
        "main_ms": med([f["main_ms"] for f in fs], 2),
        "t60_ms": med([f["tail"]["t60_ms"] for f in fs]),
        "late_db": med([f["tail"]["late_db"] for f in fs]),
        "floor_at_master_dbfs": med([f["floor_at_master_dbfs"] for f in fs]),
        "stereo_corr": med([f["stereo"]["corr"] for f in fs], 3),
        "corr_hi": med([f["stereo"].get("corr_hi") for f in fs], 3),
        "mono_loss_db": med([f["stereo"]["mono_loss_db"] for f in fs], 2),
        "flatness": med([f["flatness"] for f in fs], 3),
        "ring_db": med([f["ring_db"] for f in fs]),
        "ring_hz": med([f["ring_hz"] for f in fs], 0),
        "low_sustain_db": med([f["low_sustain_db"] for f in fs]),
        "low_edge_db": med([f["low_edge_db"] for f in fs]),
        "hold_level_at_master_dbfs": med([f["hold_level_at_master_dbfs"] for f in fs]),
        "peak_hz": med([f["peak_hz"] for f in fs], 0),
    }


def cleanliness(take: dict, ms: dict) -> tuple[float, dict]:
    """0-10, a measurement heuristic: 10 minus penalties for a floor that would sit over -70 dBFS once
    mastered (gap floor, hold gap, after the stroke), hiss (4-8 kHz vs 150-400 Hz over -5 dB for the whole
    stroke, over -20 dB in its decay after 15 ms), a tail (T60 over 80 ms, late energy over -35 dB),
    clipping, mono fold loss over 1.5 dB, gap activity over -60 dBFS once mastered (rustle, ghost keys),
    stray events, under 3 clean strokes."""
    pen = {}
    fl = take["gap"]["floor_at_master_dbfs"]
    fm = ms.get("floor_at_master_dbfs")
    worst = max([v for v in (fl, fm) if v is not None], default=None)
    pen["floor"] = 0.0 if worst is None else min(3.0, max(0.0, (worst - FLOOR_GATE_DBFS) / 5.0))
    h, ht = ms.get("hiss_db"), ms.get("hiss_tail_db")
    pen["hiss"] = min(2.0, (0.0 if h is None else 0.5 * max(0.0, (h + 5.0) / 5.0))
                      + (0.0 if ht is None else max(0.0, (ht + 20.0) / 5.0)))
    t60 = ms.get("t60_ms")
    late = ms.get("late_db")
    pen["tail"] = min(2.0, (0.0 if t60 is None else max(0.0, (t60 - 80.0) / 60.0))
                      + (0.0 if late is None else max(0.0, (late + 35.0) / 10.0)))
    pen["clip"] = 1.5 if take.get("clip_samples") else 0.0
    ml = ms.get("mono_loss_db")
    pen["mono"] = 0.0 if ml is None else min(1.0, max(0.0, (ml - 1.5) / 2.0))
    act = take["gap"]["activity"]
    pen["rustle"] = 0.0 if act is None else min(1.0, act * 3.0)
    pen["stray"] = min(1.0, take["stray_events"] / max(4, take["presses"]) * 2.0)
    pen["few_clean"] = 1.0 if take["clean"] < 3 else 0.0
    score = max(0.0, 10.0 - sum(pen.values()))
    return round(score, 2), {k: round(v, 2) for k, v in pen.items()}


# ---------------------------------------------------------------- survey

def list_sources(src: Path, folders: list[int] | None = None) -> list[tuple[str, list[Path]]]:
    dirs = sorted([d for d in src.iterdir() if d.is_dir() and not d.name.startswith(".")], key=_folder_key)
    if folders is not None:
        dirs = [d for i, d in enumerate(dirs) if i in folders]
    return [(d.name, sorted(d.glob("*.wav"))) for d in dirs]


def _folder_key(d: Path) -> tuple:
    nums = [int(n) for n in re.findall(r"\((\d+)\)", d.name)]
    return (len(nums) > 0, nums)


def survey_take(path: Path, folder: str) -> tuple[dict, np.ndarray, list[dict]]:
    m, lr, info = load(path)
    presses, comps, G = detect(m, path.name)
    feats = []
    prev_end = None
    for p in presses:
        f = stroke_features(m, lr, p, prev_end)
        ci = info["clip_idx"]
        f["clip_samples"] = int(np.sum((ci >= p["a"]) & (ci < p["b"])))
        feats.append(f)
        prev_end = p["end"]
    space_flags(feats)
    take = {"folder": folder, "slug": slug(folder), "file": path.name, "id": file_id(path.name),
            "path": str(path), **{k: info[k] for k in ("sr", "channels", "duration_s", "clip_samples", "peak_dbfs")},
            "mono_fold": info["mono"], "stereo_corr_file": info["stereo_corr"]}
    take.update(take_numbers(m, presses, comps, G, feats))
    take["find_strokes_kept"] = len(strokes.find_strokes(m, path.name, "key")[0])   # the shared finder, for comparison
    take["provenance"] = provenance(path)
    clean = [f for f in feats if f["clean"]]
    take["medians_clean"] = stroke_medians(clean)
    take["medians_all"] = stroke_medians(feats)
    take["cleanliness"], take["penalties"] = cleanliness(take, take["medians_clean"] if clean else take["medians_all"])
    take["strokes"] = feats
    return take, m, presses


def refine_space(takes: list[dict]) -> None:
    """Takes with under 6 strokes: spacebar score against the folder's strokes."""
    ref = [f for t in takes for f in t["strokes"]]
    for t in takes:
        if 0 < len(t["strokes"]) < 6:
            space_flags(t["strokes"], ref)
            t["space_like"] = sum(1 for f in t["strokes"] if f.get("space_like"))


FEAT_VEC = ("lc", "b150_400", "b2k_4k", "b4k_8k", "len40", "t60")


def fvec(f: dict) -> np.ndarray:
    b = f["bands_db"]
    return np.array([np.log2(max(f["centroid_hz"] or 1, 1)), b["b150_400"] or -60, b["b2k_4k"] or -60,
                     b["b4k_8k"] or -60, (f["len40_ms"] or 0) / 20.0, min(f["tail"]["t60_ms"] or 30, 400) / 40.0])


def stroke_quality(f: dict) -> float:
    """Ranking for export: clean extraction, quiet floors once mastered, little hiss, a dry tail, mono-safe."""
    q = 0.0
    fm = f["floor_at_master_dbfs"]
    q -= 0.0 if fm is None else max(0.0, fm - FLOOR_GATE_DBFS) / 5.0
    q -= max(0.0, (f["hiss_db"] or 0) + 15.0) / 5.0
    t60 = f["tail"]["t60_ms"]
    q -= 0.0 if t60 is None else max(0.0, t60 - 80.0) / 60.0
    q -= max(0.0, (f["stereo"]["mono_loss_db"] or 0) - 1.5) / 2.0
    q -= 1.5 if f.get("clip_samples") else 0.0
    q -= 1.0 if f["kind"] != "press+release" else 0.0
    q -= 2.0 if f["len40_hits_window"] else 0.0
    q -= max(0.0, (f["main_ms"] or 0) - 15.0) / 5.0
    return q


def representative(takes: list[dict], n_key: int, n_space: int, per_take: int, clean_only: bool = True,
                   by: str = "typical", keep=None) -> list[tuple[dict, dict]]:
    """(take, stroke) pairs: key-like and space-like apart; 'typical' = nearest the folder median in
    feature space; 'best' = stroke_quality first, then nearness. At most per_take per take; `keep`
    filters strokes (e.g. one brightness band)."""
    pool = [(t, f) for t in takes for f in t["strokes"] if (f["clean"] or not clean_only) and (keep is None or keep(f))]
    if not pool and clean_only:
        return representative(takes, n_key, n_space, per_take, False, by, keep)
    out = []
    for want_space, n in ((False, n_key), (True, n_space)):
        cand = [(t, f) for t, f in pool if bool(f.get("space_like")) == want_space]
        if not cand:
            continue
        V = np.array([fvec(f) for _, f in cand])
        mu = np.median(V, axis=0)
        sd = np.std(V, axis=0) + 1e-6
        d = np.sqrt(np.mean(((V - mu) / sd) ** 2, axis=1))
        if by == "best":
            order = sorted(range(len(cand)), key=lambda i: (-round(stroke_quality(cand[i][1]), 1), d[i]))
        else:
            order = sorted(range(len(cand)), key=lambda i: d[i] - 0.15 * stroke_quality(cand[i][1]))
        used: dict[str, int] = {}
        for i in order:
            t, f = cand[i]
            if used.get(t["id"], 0) >= per_take:
                continue
            used[t["id"]] = used.get(t["id"], 0) + 1
            out.append((t, f))
            if sum(1 for _, g in out if bool(g.get("space_like")) == want_space) >= n:
                break
    return out


def folder_summary(folder: str, takes: list[dict]) -> dict:
    allf = [f for t in takes for f in t["strokes"]]
    clean = [f for f in allf if f["clean"]]
    keys_ = [f for f in clean if not f.get("space_like")]
    spaces = [f for f in clean if f.get("space_like")]
    ranked = sorted(takes, key=lambda t: (-(t["cleanliness"] + min(2.0, t["clean"] / 10.0)), t["id"]))
    return {
        "folder": folder, "slug": slug(folder), "files": len(takes),
        "durations_s": sorted({t["duration_s"] for t in takes}),
        "presses": len(allf), "clean": len(clean), "space_like_clean": len(spaces),
        "presses_per_take_median": med([t["presses"] for t in takes]),
        "clean_per_take_median": med([t["clean"] for t in takes]),
        "rhythm_cv_median": med([t["rhythm"]["ioi_cv"] for t in takes], 3),
        "ioi_median_ms": med([t["rhythm"]["ioi_median_ms"] for t in takes]),
        "gap_floor_dbfs_median": med([t["gap"]["floor_dbfs"] for t in takes]),
        "gap_floor_at_master_dbfs_median": med([t["gap"]["floor_at_master_dbfs"] for t in takes]),
        "gap_hiss_dbfs_median": med([t["gap"]["hiss_4k8k_dbfs"] for t in takes]),
        "gap_activity_median": med([t["gap"]["activity"] for t in takes], 3),
        "stray_events_median": med([t["stray_events"] for t in takes]),
        "takes_with_clipping": sum(1 for t in takes if t["clip_samples"]),
        "takes_with_digital_silence_gaps": sum(1 for t in takes if (t["gap"]["digital_silence_share"] or 0) > 0.2),
        "takes_with_hard_cuts": sum(1 for t in takes if t["hard_cuts_to_digital_zero"]),
        "take_centroid_hz_p10_p50_p90": [med([np.percentile([t["medians_clean"]["centroid_hz"] for t in takes
                                                             if t["medians_clean"]["centroid_hz"]], q)], 0) for q in (10, 50, 90)],
        "takes_by_brightness": {
            "dark_lt_450hz": sum(1 for t in takes if (t["medians_clean"]["centroid_hz"] or 0) and t["medians_clean"]["centroid_hz"] < 450),
            "mid_450_900hz": sum(1 for t in takes if t["medians_clean"]["centroid_hz"] and 450 <= t["medians_clean"]["centroid_hz"] < 900),
            "bright_ge_900hz": sum(1 for t in takes if t["medians_clean"]["centroid_hz"] and t["medians_clean"]["centroid_hz"] >= 900)},
        "stereo_corr_file_median": med([t["stereo_corr_file"] for t in takes], 3),
        "cleanliness_median": med([t["cleanliness"] for t in takes], 2),
        "cleanliness_min_max": [min(t["cleanliness"] for t in takes), max(t["cleanliness"] for t in takes)],
        "key_like": stroke_medians(keys_), "space_like": stroke_medians(spaces),
        "all_presses": stroke_medians(allf),
        "best_files": [{"file": t["file"], "id": t["id"], "cleanliness": t["cleanliness"], "clean": t["clean"],
                        "presses": t["presses"], "space_like": t["space_like"],
                        "hiss_db": t["medians_clean"]["hiss_db"], "centroid_hz": t["medians_clean"]["centroid_hz"],
                        "t60_ms": t["medians_clean"]["t60_ms"],
                        "floor_at_master_dbfs": t["gap"]["floor_at_master_dbfs"]} for t in ranked[:6]],
        "worst_files": [{"file": t["file"], "id": t["id"], "cleanliness": t["cleanliness"],
                         "penalties": t["penalties"]} for t in ranked[-3:]],
        "takes": [_take_row(t) for t in ranked],
    }


def _take_row(t: dict) -> dict:
    """One line per take for the judges (medians of its clean strokes)."""
    mc = t["medians_clean"] if t["clean"] else t["medians_all"]
    return {"id": t["id"], "file": t["file"], "duration_s": t["duration_s"], "cleanliness": t["cleanliness"],
            "presses": t["presses"], "clean": t["clean"], "space_like": t["space_like"],
            "ioi_median_ms": t["rhythm"]["ioi_median_ms"], "centroid_hz": mc["centroid_hz"],
            "b80_150": mc["bands_db"]["b80_150"], "b150_400": mc["bands_db"]["b150_400"],
            "b2k_4k": mc["bands_db"]["b2k_4k"], "hiss_db": mc["hiss_db"], "hiss_tail_db": mc["hiss_tail_db"],
            "len40_ms": mc["len40_ms"], "t60_ms": mc["t60_ms"], "late_db": mc["late_db"], "ring_db": mc["ring_db"],
            "ring_hz": mc["ring_hz"], "low_sustain_db": mc["low_sustain_db"], "release_rel_db": mc["release_rel_db"],
            "stereo_corr": mc["stereo_corr"], "gap_floor_at_master_dbfs": t["gap"]["floor_at_master_dbfs"],
            "digital_silence_share": t["gap"]["digital_silence_share"], "hard_cuts": t["hard_cuts_to_digital_zero"]}


RANKED = (("centroid_hz", "key_like", "centroid_hz"), ("hiss_db", "key_like", "hiss_db"),
          ("hiss_tail_db", "key_like", "hiss_tail_db"),
          ("body_150_400_db", "key_like", ("bands_db", "b150_400")),
          ("low_80_150_db", "key_like", ("bands_db", "b80_150")),
          ("presence_2k_4k_db", "key_like", ("bands_db", "b2k_4k")),
          ("len40_ms", "key_like", "len40_ms"), ("t60_ms", "key_like", "t60_ms"), ("late_db", "key_like", "late_db"),
          ("ring_db", "key_like", "ring_db"), ("low_sustain_db", "key_like", "low_sustain_db"),
          ("release_rel_db", "key_like", "release_rel_db"), ("mono_loss_db", "key_like", "mono_loss_db"),
          ("cleanliness", None, "cleanliness_median"))


def _get(d: dict, sec, key):
    v = d[sec] if sec else d
    if isinstance(key, tuple):
        for k in key:
            v = v.get(k) if isinstance(v, dict) else None
        return v
    return v.get(key)


def rank_and_tag(folders: list[dict], ref: dict) -> None:
    """Ranks across folders (1 = lowest value) and heuristic tags. Character tags compare a folder with the
    other folders (top or bottom two); defect tags use the deliverable's gates or the rejected sets."""
    n = len(folders)
    for name, sec, key in RANKED:
        ok = sorted([(_get(f, sec, key), i) for i, f in enumerate(folders) if _get(f, sec, key) is not None])
        for r, (_, i) in enumerate(ok):
            folders[i].setdefault("ranks_low_to_high", {})[name] = r + 1
    rc = ref.get("codex182", {}).get("key_like", {})
    for f in folders:
        k = f["key_like"]
        rk = f.get("ranks_low_to_high", {})
        if k.get("centroid_hz") is None:
            f["tags"] = ["no clean key-like strokes"]
            continue
        lo2 = lambda name: n >= 4 and rk.get(name, 99) <= 2          # noqa: E731  (ranks need >= 4 folders)
        hi2 = lambda name: n >= 4 and rk.get(name, -99) >= n - 1     # noqa: E731
        tags = []
        if lo2("centroid_hz"):
            tags.append("darkest of the set (lowest centroid)")
        if hi2("centroid_hz"):
            tags.append("brightest of the set (highest centroid)")
        if hi2("low_80_150_db"):
            tags.append("most sub-thump 80-150 Hz")
        if hi2("body_150_400_db"):
            tags.append("most 150-400 Hz body")
        if hi2("presence_2k_4k_db"):
            tags.append("most 2-4 kHz presence (clack side)")
        if hi2("t60_ms") or hi2("late_db"):
            tags.append("longest tails of the set")
        if lo2("t60_ms") and not hi2("late_db"):
            tags.append("shortest tails of the set")
        if hi2("ring_db"):
            tags.append("strongest tonal ring of the set")
        if hi2("low_sustain_db"):
            tags.append("longest low (< 450 Hz) sustain under the press")
        if hi2("release_rel_db"):
            tags.append("loudest releases of the set")
        if (k.get("hiss_tail_db") or -99) > -20:
            tags.append("HF left in the decay (hiss risk)")
        if rc.get("hiss_tail_db") is not None and (k.get("hiss_tail_db") or 99) < rc["hiss_tail_db"] - 10:
            tags.append(f"decay far cleaner above 4 kHz than Codex 182 ({k['hiss_tail_db']} vs {rc['hiss_tail_db']} dB)")
        if (k.get("t60_ms") or 0) > 100:
            tags.append(f"tail T60 {k['t60_ms']:.0f} ms, late {k.get('late_db')} dB (longer than a dry key)")
        if (k.get("ring_db") or 0) >= 15:
            tags.append(f"tonal ring near {k.get('ring_hz'):.0f} Hz ({k['ring_db']} dB over its neighbourhood)")
        if (f.get("gap_floor_at_master_dbfs_median") or -999) > FLOOR_GATE_DBFS:
            tags.append("floor between strokes over -70 dBFS once mastered (needs gating)")
        elif (f.get("gap_floor_at_master_dbfs_median") or 0) <= -80:
            tags.append(f"near-silent gaps ({f['gap_floor_at_master_dbfs_median']} dBFS once mastered)")
        if (f.get("gap_activity_median") or 0) > 0.2:
            tags.append("activity between strokes (rustle / ghost events)")
        if (k.get("mono_loss_db") or 0) > 0.8:
            tags.append(f"widest stereo ({k['mono_loss_db']} dB lost in mono)")
        if f.get("takes_with_clipping"):
            tags.append(f"clipping in {f['takes_with_clipping']} takes")
        if f.get("takes_with_digital_silence_gaps", 0) >= max(2, f["files"] // 5):
            tags.append(f"{f['takes_with_digital_silence_gaps']} takes gated to digital zero between strokes (edited)")
        if f.get("takes_with_hard_cuts", 0) >= max(2, f["files"] // 5):
            tags.append(f"{f['takes_with_hard_cuts']} takes with hard cuts to digital zero (check tails)")
        tb = f.get("takes_by_brightness", {})
        if tb and min(tb.values()) >= max(2, f["files"] // 8):
            tags.append("mixed brightness across takes (dark, mid and bright takes all present)")
        if (f.get("rhythm_cv_median") or 0) > 0.6:
            tags.append("irregular rhythm")
        f["tags"] = tags


# ---------------------------------------------------------------- reference (rejected) sets

def reference_sets() -> dict:
    """Rejected sets measured with the same code: Codex 182 (tmp/keys-codex/<id>/) and the Stable Audio 3 set
    (~/AudioLab/work/_keys/<id>/sets/top/masters/). Each file is one stroke; window = the whole file."""
    import soundfile as sf
    out = {}
    groups = {"codex182": sorted(CODEX_SETS.glob("*/key-*.wav")) + sorted(CODEX_SETS.glob("*/space-*.wav")),
              "sa3": sorted(SA3_SETS.glob("*/sets/top/masters/key-*.wav")) + sorted(SA3_SETS.glob("*/sets/top/masters/space-*.wav"))}
    for name, paths in groups.items():
        feats, spectra = [], {"key": [], "space": []}
        for path in paths:
            x, sr = sf.read(str(path), always_2d=True, dtype="float64")
            if sr != SR:
                continue
            m = x.mean(axis=1)
            lr = x if x.shape[1] == 2 else np.repeat(x[:, :1], 2, axis=1)
            on = int(np.flatnonzero(np.abs(m) >= np.abs(m).max() * 10 ** (-30 / 20))[0])
            p = {"onset": on, "a": max(0, on - int(0.001 * SR)), "b": len(m), "end": len(m), "clean": True,
                 "why": None, "release": None, "next": len(m) + int(0.003 * SR), "peak_db": None}
            f = stroke_features(m, lr, p)
            part = "space" if path.name.startswith("space") else "key"
            f.update({"file": str(path), "profile": path.parts[-2] if name == "codex182" else path.parts[-5],
                      "part": part, "space_like": part == "space"})
            feats.append(f)
            spectra[part].append(norm_psd(m[p["a"]:]))
        if feats:
            out[name] = {"files": len(feats),
                         "key_like": stroke_medians([f for f in feats if f["part"] == "key"]),
                         "space_like": stroke_medians([f for f in feats if f["part"] == "space"]),
                         "by_profile": {pid: stroke_medians([f for f in feats if f["profile"] == pid and f["part"] == "key"])
                                        for pid in sorted({f["profile"] for f in feats})},
                         "strokes": feats, "_spectra": spectra}
    return out


def norm_psd(y: np.ndarray) -> np.ndarray:
    """PSD of a stroke after pure gain to -27 LUFS-M (so every curve compares at the deliverable level)."""
    from build import measure
    g = 10 ** ((TARGET_LUFS_M - measure.lufs_m_max(y, SR)) / 20)
    f, P = signal.welch(y * g, SR, nperseg=min(1024, len(y)), nfft=4096)
    return P


SPEC_F = np.fft.rfftfreq(4096, 1 / SR)


def smooth_oct(P: np.ndarray, frac: float = 6.0) -> tuple[np.ndarray, np.ndarray]:
    """1/frac-octave smoothing on a log grid 50 Hz - 20 kHz -> (hz, dB)."""
    centres = np.geomspace(50, 20000, 140)
    out = []
    for c in centres:
        lo, hi = c * 2 ** (-0.5 / frac), c * 2 ** (0.5 / frac)
        sel = (SPEC_F >= lo) & (SPEC_F < hi)
        out.append(_db(P[sel].mean()) if sel.any() else np.nan)
    return centres, np.array(out)


# ---------------------------------------------------------------- pictures

def _spec_img(ax, y, fmax=20000, vmin=-80):
    f, t, S = signal.spectrogram(y, SR, window="hann", nperseg=256, noverlap=256 - 24, nfft=1024, mode="psd")
    Sd = 10 * np.log10(S + 1e-20)
    Sd -= Sd.max()
    sel = (f >= 40) & (f <= fmax)
    ax.pcolormesh(t * 1000, f[sel], Sd[sel], vmin=vmin, vmax=0, cmap="magma", shading="auto", rasterized=True)
    ax.set_yscale("log")
    ax.set_ylim(40, fmax)
    ax.set_yticks([100, 300, 1000, 3000, 10000])
    ax.set_yticklabels(["100", "300", "1k", "3k", "10k"], fontsize=6)
    ax.tick_params(axis="x", labelsize=6)


def contact_sheet(fs: dict, takes: list[dict], audio: dict, picks: list[tuple[dict, dict]], path: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(17, 12.5), dpi=100)
    gs = fig.add_gridspec(6, 4, height_ratios=[0.55, 1.0, 0.55, 1.0, 0.55, 1.0], hspace=0.55, wspace=0.18,
                          left=0.04, right=0.99, top=0.885, bottom=0.04)
    k = fs["key_like"]
    sp = fs["space_like"]
    title = (f"{fs['folder']}  ({fs['slug']})  -  {fs['files']} takes, {fs['presses']} presses, "
             f"{fs['clean']} clean, {fs['space_like_clean']} spacebar-like")
    lines = [
        f"key-like median: centroid {k['centroid_hz']} Hz (press {k['centroid_press_hz']}), hiss(4-8k vs 150-400) {k['hiss_db']} dB, "
        f"bands 80-150/150-400/400-2k/2-4k/4-8k/8k+ = " + "/".join(str(k['bands_db'][b]) for b, _, _ in BANDS) + " dB re total",
        f"len to -40 dB {k['len40_ms']} ms, press decay {k['press_decay40_ms']} ms, release +{k['release_gap_ms']} ms at {k['release_rel_db']} dB, "
        f"T60 {k['t60_ms']} ms, late {k['late_db']} dB, floor once mastered {k['floor_at_master_dbfs']} dBFS, "
        f"L/R corr {k['stereo_corr']} (hi {k['corr_hi']}), mono loss {k['mono_loss_db']} dB",
        f"space-like median: centroid {sp['centroid_hz']} Hz, hiss {sp['hiss_db']} dB, len {sp['len40_ms']} ms   |   "
        f"takes: cleanliness median {fs['cleanliness_median']} (range {fs['cleanliness_min_max']}), gap floor {fs['gap_floor_dbfs_median']} dBFS "
        f"(at master {fs['gap_floor_at_master_dbfs_median']}), gap activity {fs['gap_activity_median']}, rhythm CV {fs['rhythm_cv_median']}, "
        f"clipping takes {fs['takes_with_clipping']}",
        "tags (measurement heuristics): " + "; ".join(fs.get("tags", [])),
    ]
    fig.text(0.04, 0.985, title, fontsize=12, weight="bold", va="top")
    fig.text(0.04, 0.962, "\n".join(lines), fontsize=7.6, va="top", family="monospace")
    # row 0-1: full take of the best file (waveform + spectrogram)
    best = fs["best_files"][0]["id"] if fs["best_files"] else takes[0]["id"]
    t = next(t for t in takes if t["id"] == best)
    m = audio[best]
    axw = fig.add_subplot(gs[0, :])
    tt = np.arange(len(m)) / SR
    step = max(1, len(m) // 6000)
    seg = m[:len(m) // step * step].reshape(-1, step)
    axw.fill_between(tt[::step][:len(seg)], seg.min(axis=1), seg.max(axis=1), color="#333", lw=0)
    for f in t["strokes"]:
        c = "#1b9e77" if f["clean"] and not f.get("space_like") else ("#d95f02" if f.get("space_like") else "#bbbbbb")
        axw.axvline(f["t_ms"] / 1000, color=c, lw=0.8, alpha=0.8)
    axw.set_xlim(0, len(m) / SR)
    axw.set_title(f"best take by measurement: {t['file']}  (cleanliness {t['cleanliness']}, {t['presses']} presses, "
                  f"{t['clean']} clean; green = clean key, orange = spacebar-like, grey = not isolatable)", fontsize=8)
    axw.tick_params(labelsize=6)
    axs = fig.add_subplot(gs[1, :])
    f_, t_, S = signal.spectrogram(m, SR, window="hann", nperseg=1024, noverlap=768, mode="psd")
    Sd = 10 * np.log10(S + 1e-20)
    Sd -= Sd.max()
    sel = (f_ >= 40)
    axs.pcolormesh(t_, f_[sel], Sd[sel], vmin=-90, vmax=0, cmap="magma", shading="auto", rasterized=True)
    axs.set_yscale("log")
    axs.set_ylim(40, 22000)
    axs.set_yticks([100, 300, 1000, 3000, 10000])
    axs.set_yticklabels(["100", "300", "1k", "3k", "10k"], fontsize=6)
    axs.tick_params(labelsize=6)
    axs.set_xlabel("s (full take, dB re max, floor -90)", fontsize=7)
    # rows 2-5: 8 strokes
    for j, (tk, f) in enumerate(picks[:8]):
        r, c = 2 + 2 * (j // 4), j % 4
        mm = audio[tk["id"]]
        a = max(0, int(f["t_ms"] / 1000 * SR) - int(0.002 * SR))
        b = min(len(mm), a + int(0.262 * SR))
        nxt = [g["t_ms"] for g in tk["strokes"] if g["t_ms"] > f["t_ms"]]
        y = mm[a:b]
        ax1 = fig.add_subplot(gs[r, c])
        ty = np.arange(len(y)) / SR * 1000
        pk = np.abs(y).max() + 1e-12
        ax1.plot(ty, y / pk, lw=0.5, color="#222")
        env = 20 * np.log10(np.sqrt(np.convolve(y ** 2, np.ones(48) / 48, "same")) / pk + 1e-9)
        ax1b = ax1.twinx()
        ax1b.plot(ty, env, lw=0.6, color="#1f78b4")
        ax1b.set_ylim(-80, 0)
        ax1b.axhline(-40, color="#1f78b4", lw=0.4, ls=":")
        ax1b.tick_params(labelsize=5)
        if nxt and nxt[0] - f["t_ms"] < 262:
            ax1.axvline(nxt[0] - f["t_ms"] + 2, color="red", lw=0.8)
        ax1.set_xlim(0, 262)
        ax1.set_ylim(-1.05, 1.05)
        ax1.tick_params(labelsize=5)
        kind = "SPACE-like" if f.get("space_like") else "key"
        ax1.set_title(f"{kind} {tk['id']} @{f['t_ms'] / 1000:.2f}s {'clean' if f['clean'] else 'crowded'} | "
                      f"cen {f['centroid_hz']:.0f} hiss {f['hiss_db']} T60 {f['tail']['t60_ms']} "
                      f"fl@M {f['floor_at_master_dbfs']} corr {f['stereo']['corr']}", fontsize=6.3)
        ax2 = fig.add_subplot(gs[r + 1, c])
        _spec_img(ax2, y)
        ax2.set_xlim(0, 262)
    fig.suptitle("")
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=100)
    plt.close(fig)


def overlay(folders: list[dict], spectra: dict, ref: dict, path: Path) -> dict:
    """Mean key-like stroke spectrum (each stroke at -27 LUFS-M, Welch 1024/4096, 1/6-octave smoothing) of every
    folder against the rejected Codex 182 and Stable Audio 3 sets."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    curves = {}
    for f in folders:
        if spectra.get(f["slug"], {}).get("key"):
            curves[f["slug"]] = smooth_oct(np.mean(spectra[f["slug"]]["key"], axis=0))
    refc = {}
    for name in ("codex182", "sa3"):
        if name in ref and ref[name]["_spectra"]["key"]:
            refc[name] = smooth_oct(np.mean(ref[name]["_spectra"]["key"], axis=0))
    n = len(folders)
    cols = 4
    rows = int(np.ceil((n + 1) / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(17, 3.6 * rows), dpi=100, sharex=True, sharey=True)
    axes = np.atleast_2d(axes)
    cmap = plt.get_cmap("tab10")
    ax0 = axes[0, 0]
    for i, (s, (hz, d)) in enumerate(curves.items()):
        ax0.semilogx(hz, d, lw=1.1, color=cmap(i % 10), label=s.replace("adobe-2026-10-29", "f") or s)
    for name, (hz, d) in refc.items():
        ax0.semilogx(hz, d, lw=2.0, ls="--" if name == "codex182" else ":", color="k" if name == "codex182" else "#c0392b",
                     label=f"rejected {name}")
    ax0.set_title("all folders (key-like, mean)", fontsize=9)
    ax0.legend(fontsize=6, ncol=2)
    for i, f in enumerate(folders):
        ax = axes.flat[i + 1]
        if f["slug"] in curves:
            hz, d = curves[f["slug"]]
            ax.semilogx(hz, d, lw=1.6, color=cmap(i % 10), label=f"{f['slug']} key ({f['key_like']['n']})")
            if spectra[f["slug"]].get("space"):
                hz2, d2 = smooth_oct(np.mean(spectra[f["slug"]]["space"], axis=0))
                ax.semilogx(hz2, d2, lw=1.0, color=cmap(i % 10), ls="-.", label=f"space-like ({f['space_like']['n']})")
        for name, (hz, d) in refc.items():
            ax.semilogx(hz, d, lw=1.2, ls="--" if name == "codex182" else ":", color="k" if name == "codex182" else "#c0392b",
                        label=f"rejected {name}")
        ax.set_title(f"{f['folder']}  hiss {f['key_like']['hiss_db']} dB, cen {f['key_like']['centroid_hz']} Hz", fontsize=8)
        ax.legend(fontsize=6)
    for ax in axes.flat:
        ax.axvspan(150, 400, color="#3aa66c", alpha=0.10)
        ax.axvspan(4000, 8000, color="#eaa03d", alpha=0.13)
        ax.grid(alpha=0.25, which="both")
        ax.set_xlim(50, 20000)
        ax.set_ylim(-125, -45)
        ax.tick_params(labelsize=7)
    for ax in axes.flat[n + 1:]:
        ax.axis("off")
    fig.suptitle("Mean stroke spectrum per folder, each stroke at -27 LUFS-M (PSD dB/Hz, Welch 1024/4096, 1/6 oct). "
                 "Green = 150-400 Hz body, orange = 4-8 kHz hiss band. Dashed black = Codex 182 (rejected), dotted red = Stable Audio 3 (rejected)",
                 fontsize=9)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=100)
    plt.close(fig)
    data = {s: {"hz": [round(float(v), 1) for v in hz], "db": [None if not np.isfinite(v) else round(float(v), 2) for v in d]}
            for s, (hz, d) in {**curves, **{f"rejected-{k}": v for k, v in refc.items()}}.items()}
    return data


# ---------------------------------------------------------------- export

def export(fs: dict, takes: list[dict], audio: dict, presses: dict, out: Path, n_total: int = 16) -> list[dict]:
    """~16 representative single strokes per folder, at most 3 per take: 12 key-like as 4 dark + 4 mid + 4
    bright (tertiles of the folder's clean key-like centroids, best by measurement inside each band, so
    the export spans the folder instead of piling on its darkest, least hissy strokes; a band short of
    clean strokes is filled with the folder's next best) and 4 spacebar-like (keys fill when there are fewer). Rendered with strokes.render (pre-roll 1 ms, hold
    shortened in its silence when over the cap, exponential tail cap), 48 kHz mono PCM 24, not normalised."""
    import soundfile as sf
    from build import measure
    d = out / fs["slug"]
    for sub in ("key", "space"):
        (d / sub).mkdir(parents=True, exist_ok=True)
        for old in (d / sub).glob("*.wav"):
            old.unlink()                     # only files this command wrote on an earlier run
    n_space = min(4, fs["space_like_clean"])
    n_key = n_total - n_space
    cen = [f["centroid_hz"] for t in takes for f in t["strokes"] if f["clean"] and not f.get("space_like") and f["centroid_hz"]]
    edges = np.percentile(cen, [100 / 3, 200 / 3]) if len(cen) >= 6 else [np.inf, np.inf]
    band_of = lambda f: ("dark" if (f["centroid_hz"] or 0) < edges[0] else "mid" if (f["centroid_hz"] or 0) < edges[1]  # noqa: E731
                         else "bright")
    picks: list[tuple[str, dict, dict]] = []          # (quota group, take, stroke)
    for band in ("dark", "mid", "bright"):
        picks += [(band, t, f) for t, f in representative(
            takes, n_key // 3 + 3, 0, per_take=2, by="best",
            keep=lambda f, band=band: not f.get("space_like") and band_of(f) == band)]
    picks += [("space", t, f) for t, f in representative(takes, 0, n_space + 2, per_take=2, by="best",
                                                         keep=lambda f: bool(f.get("space_like")))]
    picks += [("fill", t, f) for t, f in representative(takes, n_key + 4, 0, per_take=2, by="best",
                                                        keep=lambda f: not f.get("space_like"))]
    quota = {"dark": n_key // 3, "mid": n_key // 3, "bright": n_key // 3, "space": n_space, "fill": n_key}
    rows, counts, used, seen, per_src = [], {"key": 0, "space": 0}, {}, set(), {}
    for group, t, f in picks:
        part = "space" if group == "space" else "key"
        band = band_of(f) if part == "key" else "space"
        if (counts[part] >= (n_key if part == "key" else n_space) or used.get(group, 0) >= quota[group]
                or (t["id"], f["t_ms"]) in seen or per_src.get(t["id"], 0) >= 3):
            continue
        p = next(p for p in presses[t["id"]] if round(p["onset"] / SR * 1000, 1) == f["t_ms"])
        if p["stroke"] is None:
            continue
        y, info = strokes.render(audio[t["id"]], p["stroke"], part)
        if y is None:
            continue
        counts[part] += 1
        used[group] = used.get(group, 0) + 1
        seen.add((t["id"], f["t_ms"]))
        per_src[t["id"]] = per_src.get(t["id"], 0) + 1
        name = f"{part}-{counts[part]:02d}_{band}_{t['id']}_{int(round(f['t_ms']))}ms.wav"
        sf.write(str(d / part / name), y, SR, subtype="PCM_24")
        lm = measure.lufs_m_max(y, SR)
        rows.append({"file": f"{part}/{name}", "part": part, "band": band, "source": t["path"], "source_sha256": t["provenance"]["sha256"],
                     "c2pa_manifest": t["provenance"]["c2pa_manifest"], "onset_ms": f["t_ms"], "render": info,
                     "lufs_m_max": round(lm, 2), "gain_to_master_db": round(TARGET_LUFS_M - lm, 2),
                     "true_peak_dbtp": round(measure.true_peak_db(y, SR), 2), "quality": round(stroke_quality(f), 2),
                     "features": {k: f[k] for k in ("centroid_hz", "hiss_db", "bands_db", "len40_ms", "release_gap_ms",
                                                    "floor_at_master_dbfs", "stereo", "tail", "space_score")}})
    (d / "index.json").write_text(json.dumps({
        "schema": SCHEMA, "folder": fs["folder"], "note": "Firefly (Adobe model) strokes cut by keys/strokes.py; not normalised, "
        "not cleaned. Licence: owner-generated with Adobe Firefly Generate Sound Effects (commercially safe per Adobe); "
        "C2PA manifest link per file, not fetched.", "centroid_band_edges_hz": [_r(e, 0) for e in edges],
        "strokes": rows}, indent=1, ensure_ascii=False), "utf-8")
    return rows


# ---------------------------------------------------------------- driver

def _strip(d):
    if isinstance(d, dict):
        return {k: _strip(v) for k, v in d.items() if not k.startswith("_")}
    if isinstance(d, list):
        return [_strip(v) for v in d]
    return d


def survey(src: Path = SRC, out: Path = OUT, folders: list[int] | None = None, limit: int | None = None,
           sheets: bool = True, do_export: bool = True, quiet: bool = False) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    groups = list_sources(src, folders)
    all_takes, fsums, spectra = [], [], {}
    started = dt.datetime.now()
    for folder, paths in groups:
        paths = paths[:limit] if limit else paths
        takes, audio, presses = [], {}, {}
        for i, path in enumerate(paths):
            t, m, pr = survey_take(path, folder)
            takes.append(t)
            audio[t["id"]] = m
            presses[t["id"]] = pr
            if not quiet:
                print(f"[{folder}] {i + 1}/{len(paths)} {t['id']}: {t['presses']} presses, {t['clean']} clean, "
                      f"{t['space_like']} space-like, cleanliness {t['cleanliness']}", flush=True)
        refine_space(takes)
        fs = folder_summary(folder, takes)
        sp = {"key": [], "space": []}
        for t in takes:
            for f in t["strokes"]:
                if f["clean"]:
                    p = next(p for p in presses[t["id"]] if round(p["onset"] / SR * 1000, 1) == f["t_ms"])
                    sp["space" if f.get("space_like") else "key"].append(norm_psd(audio[t["id"]][p["a"]:p["b"]]))
        spectra[fs["slug"]] = sp
        fsums.append((fs, takes, audio, presses))
        all_takes += takes
    ref = reference_sets()
    folders_out = [fs for fs, *_ in fsums]
    rank_and_tag(folders_out, ref)
    for fs, takes, audio, presses in fsums:
        if sheets:
            picks = representative(takes, 6, 2, per_take=1)
            if len(picks) < 8:
                picks = (picks + [p for p in representative(takes, 8, 0, per_take=2) if p not in picks])[:8]
            fs["sheet"] = str(out / "sheets" / f"{fs['slug']}.png")
            fs["sheet_strokes"] = [{"id": t["id"], "t_ms": f["t_ms"], "space_like": f.get("space_like")} for t, f in picks[:8]]
            contact_sheet(fs, takes, audio, picks, Path(fs["sheet"]))
        if do_export:
            rows = export(fs, takes, audio, presses, out / "strokes")
            fs["exported"] = {"dir": str(out / "strokes" / fs["slug"]), "key": sum(r["part"] == "key" for r in rows),
                              "space": sum(r["part"] == "space" for r in rows)}
        if not quiet:
            print(f"== {fs['folder']}: {fs['presses']} presses, {fs['clean']} clean, tags {fs.get('tags')}", flush=True)
    spec_data = overlay(folders_out, spectra, ref, out / "sheets" / "spectra-overlay.png") if sheets else {}
    params = {"stroke_finder": detect.__doc__.strip(),
              "press_span_db": PRESS_SPAN_DB, "merge_ms": MERGE_MS, "release_drop_db": RELEASE_DROP_DB,
              "release_lower_db": RELEASE_LOWER_DB, "pre_quiet_db": PRE_QUIET_DB, "decay_db": DECAY_DB, "search_ms": SEARCH_MS, "welch": WELCH, "bands": BANDS, "target_lufs_m": TARGET_LUFS_M,
              "floor_gate_dbfs": FLOOR_GATE_DBFS, "hiss": "10log10(P[4-8k]) - 10log10(P[150-400])",
              "space_like": "-z(log centroid) + 0.6 z(len40) + 0.6 z(low band) + 0.3 z(peak) >= 2 and z(log centroid) <= -0.5, "
                            "robust z within the take (folder when < 6 strokes)",
              "cleanliness": cleanliness.__doc__.strip()}
    meta = {"schema": SCHEMA, "generated": started.isoformat(timespec="seconds"), "source": str(src),
            "source_rule": "read only; never modified, moved or deleted", "params": params}
    (out / "features.json").write_text(json.dumps(_strip({**meta, "files": all_takes,
                                                          "rejected_sets": {k: v["strokes"] for k, v in ref.items()}}),
                                                  ensure_ascii=False, allow_nan=False), "utf-8")
    summary = {**meta, "folders": folders_out,
               "rejected_sets": {k: {kk: vv for kk, vv in v.items() if kk not in ("strokes", "_spectra")} for k, v in ref.items()},
               "overlay": str(out / "sheets" / "spectra-overlay.png") if sheets else None,
               "mean_spectra_db_at_minus27_lufs_m": spec_data}
    (out / "summary.json").write_text(json.dumps(_strip(summary), indent=1, ensure_ascii=False, allow_nan=False), "utf-8")
    if not quiet:
        print(f"features {out / 'features.json'}\nsummary {out / 'summary.json'}", flush=True)
    return summary


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="keys firefly", description="Khảo sát và dựng bộ phím Firefly của chủ dự án.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("survey", help="measure every take, contact sheets, overlay, representative strokes")
    s.add_argument("--src", default=str(SRC))
    s.add_argument("--out", default=str(OUT))
    s.add_argument("--folders", help="folder indexes in sorted order, e.g. 0,3 (default all)")
    s.add_argument("--limit", type=int, help="first N takes per folder (smoke runs)")
    s.add_argument("--no-sheets", action="store_true")
    s.add_argument("--no-export", action="store_true")
    from keys import firefly_build
    b = sub.add_parser("build", help="mỗi thư mục một bộ 10+3, preview 1 giây và hồ sơ đo (phiếu 189)")
    b.add_argument("--src", type=Path, default=SRC)
    b.add_argument("--survey", type=Path, default=OUT)
    b.add_argument("--out", type=Path, default=firefly_build.STAGING)
    b.add_argument("--work", type=Path, default=firefly_build.WORK)
    b.add_argument("--evidence", type=Path, default=firefly_build.EVIDENCE)
    from keys import firefly_v2
    v = sub.add_parser("build-v2", help="bộ 70–100 phím và 6–10 cách theo âm sắc (phiếu 218)")
    v.add_argument("--src", type=Path, default=SRC)
    v.add_argument("--survey", type=Path, default=OUT)
    v.add_argument("--out", type=Path, default=firefly_v2.STAGING)
    v.add_argument("--work", type=Path, default=firefly_v2.WORK)
    v.add_argument("--evidence", type=Path, default=firefly_v2.EVIDENCE)
    v.add_argument("--prepare-only", action="store_true", help="chỉ chuẩn bị ứng viên và đo nguồn")
    a = ap.parse_args(argv)
    if a.cmd == "survey":
        fl = [int(v) for v in a.folders.split(",")] if a.folders else None
        survey(Path(a.src), Path(a.out), fl, a.limit, not a.no_sheets, not a.no_export)
    elif a.cmd == "build":
        firefly_build.build(a.src, a.survey, a.out, a.work, a.evidence)
    elif a.cmd == "build-v2":
        firefly_v2.build(a.src, a.survey, a.out, a.work, a.evidence, a.prepare_only)
    return 0


if __name__ == "__main__":
    sys.exit(main())
