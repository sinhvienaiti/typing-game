"""Loop checks for beds (ours, batch 0b review): long-term average spectrum (LTAS), decoder comb
lines, and the "loop signature": short events that make a 6 s loop recognisable on repeat.

The seam itself is features.seam (§4.3.1). These measures only flag (L1b) and draw (L6):
  - LTAS over the whole loop with the per-second spread (P10-P90), 1/3-octave levels, tilt;
  - comb: Stable Audio 3's decoder leaves lines at k x 44100/256 Hz (172.27 Hz) above 10 kHz;
  - signature: knocks (short bumps over the local background, full band, above 100 Hz and in
    20-200 Hz, so a low wind-mic thump under a bright bed counts too), chirps (narrow tonal events in
    1.5-9 kHz, bird-like: a far-standing bin, or a 4096-point bin that stands over its neighbours and
    its own past while its band rises) and bands (a narrow 1/6-octave band in 1.5-12 kHz that comes
    and goes within the loop: a whistle or an insect-like hiss that stops mid-loop). A loop is read
    circularly, so an event at the seam counts.
"""
from __future__ import annotations

import numpy as np
from scipy import signal

from .audio import EPS, fnum, pdb
from .thresholds import L1B

COMB_F0 = 44100.0 / 256.0


def _mono(data: np.ndarray) -> np.ndarray:
    return data.mean(axis=1) if data.ndim == 2 else data


def ltas(data: np.ndarray, sr: int, nperseg: int = 8192) -> dict:
    """Mean PSD of the loop plus the P10/P90 of 1 s Welch spectra (how much the colour moves)."""
    x = _mono(data)
    nper = int(min(nperseg, 2 ** int(np.floor(np.log2(max(256, len(x)))))))
    f, p = signal.welch(x, sr, nperseg=nper)
    seg = int(sr)
    parts = [signal.welch(x[i:i + seg], sr, nperseg=min(nper, 4096))[1] for i in range(0, len(x) - seg + 1, seg // 2)]
    if parts:
        f1 = signal.welch(x[:seg], sr, nperseg=min(nper, 4096))[0]
        stack = np.array(parts)
        lo = np.interp(f, f1, np.percentile(stack, 10, axis=0))
        hi = np.interp(f, f1, np.percentile(stack, 90, axis=0))
    else:
        lo = hi = p
    return {"f": f, "psd": p, "p10": lo, "p90": hi}


def third_octaves(f: np.ndarray, psd: np.ndarray, lo: float = 50.0, hi: float = 20000.0) -> list[tuple[float, float]]:
    out = []
    k = np.arange(np.ceil(3 * np.log2(lo / 1000)), np.floor(3 * np.log2(hi / 1000)) + 1)
    for fc in 1000 * 2 ** (k / 3):
        sel = (f >= fc * 2 ** (-1 / 6)) & (f < fc * 2 ** (1 / 6))
        if sel.any():
            out.append((float(fc), float(pdb(psd[sel].sum()))))
    return out


def comb(f: np.ndarray, psd: np.ndarray, f0: float = COMB_F0, fmin: float = 10000.0, fmax: float | None = None) -> dict:
    """Prominence of the lines at k*f0 over the neighbouring bins (median of +-3..12 bins)."""
    fmax = min(fmax or 20000.0, f[-1] - 15 * (f[1] - f[0]))
    d = pdb(psd)
    ref = float(d.max())
    proms, levels, freqs = [], [], []
    for k in range(int(np.ceil(fmin / f0)), int(fmax // f0) + 1):
        i = int(np.argmin(np.abs(f - k * f0)))
        nb = np.r_[d[max(0, i - 12): i - 3], d[i + 4: i + 13]]
        if nb.size < 6:
            continue
        top = float(d[i - 1: i + 2].max())
        proms.append(top - float(np.median(nb)))
        levels.append(top - ref)
        freqs.append(k * f0)
    if not proms:
        return {"n_lines": 0, "median_prom_db": None, "n_prom6": 0, "line_level_db": None}
    proms = np.array(proms)
    return {"n_lines": len(proms), "median_prom_db": fnum(np.median(proms), 1),
            "p90_prom_db": fnum(np.percentile(proms, 90), 1), "n_prom6": int((proms >= 6).sum()),
            "line_level_db": fnum(np.median(levels), 1), "freqs": [round(x, 2) for x in freqs],
            "prom_db": [fnum(x, 1) for x in proms]}


def summary(data: np.ndarray, sr: int) -> tuple[dict, dict]:
    """(metrics, drawing context) of the long-term spectrum."""
    L = ltas(data, sr)
    f, p = L["f"], L["psd"]
    tot = float(p[f >= 20].sum()) + EPS

    def share(a, b):
        return float(p[(f >= a) & (f < b)].sum()) / tot

    bands = third_octaves(f, p)
    sel = [(fc, lv) for fc, lv in bands if 100 <= fc <= 16000]
    tilt = None
    if len(sel) >= 4:
        tilt = float(np.polyfit(np.log2([b[0] for b in sel]), [b[1] for b in sel], 1)[0])
    c = comb(f, p)
    var = pdb(L["p90"]) - pdb(L["p10"])
    m = {"ltas_share_below_150": fnum(share(20, 150), 4), "ltas_share_4k_10k": fnum(share(4000, 10000), 4),
         "ltas_share_above_8k": fnum(share(8000, 1e9), 4), "ltas_tilt_db_oct": fnum(tilt, 2),
         "ltas_spread_db_1k_8k": fnum(float(np.median(var[(f >= 1000) & (f < 8000)])), 1) if np.any((f >= 1000) & (f < 8000)) else None,
         "comb_median_prom_db": c["median_prom_db"], "comb_n_prom6": c["n_prom6"], "comb_n_lines": c["n_lines"],
         "comb_line_level_db": c["line_level_db"],
         "third_octaves": [[round(fc, 1), fnum(lv, 1)] for fc, lv in bands]}
    return m, {"ltas": L, "comb": c}


# ---------------------------------------------------------------- loop signature

def _wrap(x: np.ndarray, pad: int, loop: bool) -> np.ndarray:
    if not loop or len(x) <= 2 * pad:
        return np.pad(x, (pad, pad), mode="reflect") if len(x) > pad else x
    return np.concatenate([x[-pad:], x, x[:pad]])


def _runs(mask: np.ndarray) -> list[tuple[int, int]]:
    d = np.diff(np.concatenate([[0], mask.astype(np.int8), [0]]))
    return list(zip(np.where(d == 1)[0], np.where(d == -1)[0]))


def signature(data: np.ndarray, sr: int, loop: bool = True) -> dict:
    """Knocks and chirps that stand out of a bed (times in s from the loop start)."""
    x = _mono(data).astype(np.float64)
    n = len(x)
    if n < sr:
        return {"applies": False, "events": [], "knocks": 0, "chirps": 0}
    hop = int(0.005 * sr)
    pad = int(1.0 * sr)
    # knocks: 10 ms RMS against the 1 s running median (circular for loops), on the full band (a low
    # thump) and above 100 Hz (a knock under a loud rumble); the same bump found twice counts once
    events = []
    lo_hz, hi_hz = L1B["loop_knock_low_band"]
    knock_bands = ((signal.butter(2, 20, "high", fs=sr, output="sos"), "full", 0.0),
                   (signal.butter(2, 100, "high", fs=sr, output="sos"), "above-100", 0.0),
                   # review 2: a < 200 Hz thump 10.8 dB over its median, invisible in the full band
                   (signal.butter(4, [lo_hz, hi_hz], "bandpass", fs=sr, output="sos"), "below-200",
                    L1B["loop_knock_low_min_s"]))
    for sos, band, min_s in knock_bands:
        hp = signal.sosfilt(sos, _wrap(x, pad, loop))
        w = int(0.010 * sr)
        c = np.concatenate([[0.0], np.cumsum(hp ** 2)])
        starts = np.arange(0, len(hp) - w, hop)
        env = pdb((c[starts + w] - c[starts]) / w)
        med = signal.medfilt(env, kernel_size=int(1.0 * sr / hop) // 2 * 2 + 1)
        exc = env - med
        for a, b in _runs(exc >= L1B["loop_knock_db"] - 4):
            dur = (b - a) * hop / sr
            k = a + int(np.argmax(exc[a:b]))
            t = (starts[k] - pad) / sr
            if exc[k] >= L1B["loop_knock_db"] and min_s <= dur <= L1B["loop_knock_max_s"] and 0 <= t < n / sr:
                ev = {"t": round(float(t), 3), "kind": "knock", "db": round(float(exc[k]), 1),
                      "dur_ms": round(dur * 1000), "band": band}
                twin = next((e for e in events if abs(e["t"] - ev["t"]) <= 0.03), None)
                if twin is None:
                    events.append(ev)
                elif ev["db"] > twin["db"]:
                    twin.update(ev)
    # chirps: one narrow spectral peak in 1.5-9 kHz far over the band's median, rising over the bed
    xx = _wrap(x, pad, loop)
    nfft = 1024
    f, t_, Z = signal.stft(xx, sr, nperseg=nfft, noverlap=nfft - hop, boundary=None, padded=False)
    band = (f >= 1500) & (f <= 9000)
    S = pdb(np.abs(Z[band]) ** 2)
    prom = S.max(axis=0) - np.median(S, axis=0)
    lvl = pdb((np.abs(Z[band]) ** 2).sum(axis=0))
    lmed = signal.medfilt(lvl, kernel_size=int(1.0 * sr / hop) // 2 * 2 + 1)
    tonal = (prom >= L1B["loop_chirp_prom_db"]) & (lvl - lmed >= L1B["loop_chirp_rise_db"])
    for a, b in _runs(tonal):
        dur = (b - a) * hop / sr
        if not (0.015 <= dur <= 0.6):
            continue
        k = a + int(np.argmax(prom[a:b]))
        t = (t_[k] - pad / sr)
        if 0 <= t < n / sr:
            fpk = float(f[band][int(np.argmax(S[:, k]))])
            events.append({"t": round(float(t), 3), "kind": "chirp", "db": round(float(prom[k]), 1),
                           "dur_ms": round(dur * 1000), "hz": round(fpk)})
    for e in tones(x, sr, loop):            # the same chirp found by both tests counts once
        if not any(o["kind"] == "chirp" and abs(o["t"] - e["t"]) <= 0.1 for o in events):
            events.append(e)
    events += band_steps(x, sr)
    events.sort(key=lambda e: e["t"])
    knocks = [e for e in events if e["kind"] == "knock"]
    chirps = [e for e in events if e["kind"] == "chirp"]
    bands = [e for e in events if e["kind"] == "band"]
    return {"applies": True, "events": events[:40], "knocks": len(knocks), "chirps": len(chirps),
            "bands": len(bands), "max_knock_db": max((e["db"] for e in knocks), default=None),
            "max_chirp_db": max((e["db"] for e in chirps), default=None),
            "max_band_db": max((e["db"] for e in bands), default=None)}


def tones(x: np.ndarray, sr: int, loop: bool = True, nfft: int = 4096, hop_s: float = 0.010) -> list[dict]:
    """Near-tonal events in 1.5-9 kHz that the 24 dB chirp test misses (review 2: a 3.93 kHz tone in
    H s2001, 18.4 dB over its own median, 12.8 dB over +-500 Hz, its 3-5 kHz band up ~5-9 dB).
    A 4096-point bin (11.7 Hz) must stand >= loop_tone_rise_db over its own 1 s running median,
    >= loop_tone_prom_db over the median of its +-500 Hz neighbours (+-100 Hz left out), while the
    +-1 kHz band around it rises >= loop_tone_band_rise_db. Frames within 30 ms are one event."""
    from scipy.ndimage import median_filter, uniform_filter1d

    pad = int(1.0 * sr)
    if len(x) < max(nfft, sr):
        return []
    hop = int(hop_s * sr)
    xx = _wrap(x, pad, loop)
    f, t, Z = signal.stft(xx, sr, nperseg=nfft, noverlap=nfft - hop, boundary=None, padded=False)
    P = np.abs(Z) ** 2
    S = pdb(P)
    df = float(f[1] - f[0])
    k_med = int(1.0 * sr / hop) // 2 * 2 + 1
    mode = "wrap" if loop else "nearest"
    rise = S - median_filter(S, size=(1, k_med), mode=mode)
    nbb = int(1000 / df)
    Lb = pdb(uniform_filter1d(P, 2 * nbb + 1, axis=0, mode="nearest"))
    brise = Lb - median_filter(Lb, size=(1, k_med), mode=mode)
    nb, ex = int(500 / df), int(100 / df)
    tt = t - pad / sr
    cols = np.where((tt >= 0) & (tt < len(x) / sr))[0]
    rows = np.where((f >= 1500) & (f <= 9000))[0]
    rows = rows[(rows - nb >= 0) & (rows + nb < len(f))]
    cand = (rise[rows][:, cols] >= L1B["loop_tone_rise_db"]) & (brise[rows][:, cols] >= L1B["loop_tone_band_rise_db"])
    hits: list[tuple[int, int, float]] = []
    for ri, ci in zip(*np.nonzero(cand)):
        i, j = int(rows[ri]), int(cols[ci])
        nbh = np.r_[S[i - nb:i - ex, j], S[i + ex + 1:i + nb + 1, j]]
        prom = float(S[i, j] - np.median(nbh))
        if prom >= L1B["loop_tone_prom_db"]:
            hits.append((j, i, prom))
    out: list[dict] = []
    for j, i, prom in sorted(hits):
        tj = float(tt[j])
        if out and tj - out[-1]["_t_end"] <= 0.03:
            if prom > out[-1]["db"]:
                out[-1].update({"t": round(tj, 3), "db": round(prom, 1), "hz": round(float(f[i]))})
            out[-1]["_t_end"] = tj
            continue
        out.append({"t": round(tj, 3), "kind": "chirp", "db": round(prom, 1), "dur_ms": 0,
                    "hz": round(float(f[i])), "rule": "tone", "_t0": tj, "_t_end": tj})
    for e in out:
        e["dur_ms"] = round((e.pop("_t_end") - e.pop("_t0")) * 1000 + hop_s * 1000)
    return out


def band_steps(x: np.ndarray, sr: int, seg_s: float = 0.5) -> list[dict]:
    """Narrow bands that come and go: per 0.5 s segment, each 1/6-octave band in 1.5-12 kHz relative
    to the 1-12 kHz level; a band whose P95-P5 range over the loop is >= loop_band_range_db and
    stands >= loop_band_over_db over the median band's range is one event (t: its loudest segment).
    Batch 0b r2: a 4.2 kHz hiss band on for 3.6 s, off for 2.4 s, that the chirp test missed."""
    f, t, S = signal.spectrogram(x, sr, nperseg=2048, noverlap=1024)
    if len(t) < 2:
        return []
    per = max(1, int(round(seg_s / (t[1] - t[0]))))
    nseg = S.shape[1] // per
    if nseg < 6:
        return []
    G = np.stack([S[:, i * per:(i + 1) * per].mean(axis=1) for i in range(nseg)], axis=1)
    edges = 1000.0 * 2 ** (np.arange(0, 22) / 6.0)          # 1 to 12.7 kHz in 1/6 octaves
    lv, fcs = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (f >= lo) & (f < hi)
        if sel.any() and hi <= sr / 2:
            lv.append(pdb(G[sel].sum(axis=0)))
            fcs.append(float(np.sqrt(lo * hi)))
    if len(lv) < 6:
        return []
    bb = pdb(G[(f >= 1000) & (f < 12000)].sum(axis=0))
    R = np.array(lv) - bb
    rng = np.percentile(R, 95, axis=1) - np.percentile(R, 5, axis=1)
    med = float(np.median(rng))
    out = []
    for k, fc in enumerate(fcs):
        if fc < 1500 or rng[k] < L1B["loop_band_range_db"] or rng[k] - med < L1B["loop_band_over_db"]:
            continue
        j = int(np.argmax(R[k]))
        out.append({"t": round(float((j + 0.5) * per * (t[1] - t[0])), 3), "kind": "band", "db": round(float(rng[k]), 1),
                    "hz": round(fc), "dur_ms": round(seg_s * 1000)})
    # neighbouring bands of one event count once (the strongest)
    out.sort(key=lambda e: e["hz"])
    merged: list[dict] = []
    for e in out:
        if merged and e["hz"] <= merged[-1]["hz"] * 2 ** (2.5 / 6):
            if e["db"] > merged[-1]["db"]:
                merged[-1] = e
            continue
        merged.append(e)
    return merged
