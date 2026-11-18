"""Stroke features, profile fit and family consistency (AUDIO_PIPELINE §5.2, §4.3.3 as a starting point).

Family consistency is measured acoustically, never with CLAP (§5.2):
  - mel distance in the onset window 0-50 ms (RMS dB difference of 40 mel bands, level removed);
  - spread of the spectral centroid and of the peak pitch (cents);
  - correlation of the onset envelopes (1 ms RMS, first 50 ms).
The accepted range is P10-P90 of the same numbers over the 26 Kenney Impact families x 5 numbered
takes (CC0, ~/AudioLab/libraries/kenney/impact-sounds), cached in ~/AudioLab/work/_keys/_kenney-family.json.

Profile fit is a soft score (trapezoids, like critic L2 targets) on features that tell the five keyboards
apart: body share, presence share, air share, centroid, the press decay, the click, the spring ring.
Targets live in keys/specs/<profile>.yaml (`fit:`), never in the critic's groups.
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np

SR = 48000
_MEL = {}


def _melbank(sr: int, n_fft: int, n_mels: int = 40, fmin: float = 60.0, fmax: float | None = None) -> np.ndarray:
    key = (sr, n_fft, n_mels)
    if key not in _MEL:
        import librosa
        _MEL[key] = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels, fmin=fmin, fmax=fmax or min(16000.0, sr / 2))
    return _MEL[key]


def _spec(y: np.ndarray, sr: int, a_ms: float, b_ms: float, n_fft: int = 4096) -> tuple[np.ndarray, np.ndarray]:
    seg = y[int(a_ms / 1000 * sr):int(b_ms / 1000 * sr)]
    seg = seg * np.hanning(len(seg)) if len(seg) > 8 else np.zeros(8)
    S = np.abs(np.fft.rfft(seg, n=max(n_fft, len(seg)))) ** 2
    return np.fft.rfftfreq(max(n_fft, len(seg)), 1 / sr), S


def onset_index(y: np.ndarray, sr: int) -> int:
    a = np.abs(y)
    pk = a.max() if a.size else 0.0
    idx = np.flatnonzero(a >= pk * 10 ** (-30 / 20)) if pk > 0 else np.array([0])
    return int(idx[0]) if idx.size else 0


def features(y: np.ndarray, sr: int = SR, release_ms: float | None = None) -> dict:
    """Numbers of one stroke (mono float). Press part = onset .. 50 ms (or to the release)."""
    y0 = y
    on = onset_index(y, sr)
    y = y[on:]
    press_end = 50.0 if release_ms is None else max(15.0, min(50.0, release_ms - 3.0))
    f, S = _spec(y, sr, 0.0, press_end)
    tot = S.sum() + 1e-20

    def share(lo, hi):
        return float(S[(f >= lo) & (f < hi)].sum() / tot)

    cen = float((S * f).sum() / tot)
    band = (f >= 200) & (f <= 8000)
    peak_hz = float(f[band][int(np.argmax(S[band]))])
    n_fft = 4096
    seg = y[:int(0.050 * sr)]
    mel = _melbank(sr, n_fft) @ (np.abs(np.fft.rfft(np.pad(seg, (0, max(0, n_fft - len(seg))))[:n_fft])) ** 2)
    mel_db = 10 * np.log10(mel + 1e-12)
    # 1 ms RMS envelope, first 50 ms, normalised
    w = int(0.001 * sr)
    e = np.array([np.sqrt(np.mean(y[i:i + w] ** 2)) for i in range(0, int(0.050 * sr), w // 2)])
    env = e / (e.max() + 1e-12)
    # press decay: 5 ms level falls 30 dB under its peak
    w5 = int(0.005 * sr)
    l5 = np.array([np.mean(y[i:i + w5] ** 2) for i in range(0, max(1, len(y) - w5), int(0.001 * sr))])
    l5 = 10 * np.log10(l5 + 1e-20)
    k = int(np.argmax(l5[:30])) if len(l5) else 0
    lim = int(press_end) if release_ms else len(l5)
    dk = np.flatnonzero(l5[k:lim] < l5[k] - 30.0)
    decay_ms = float(dk[0] + k) if dk.size else float(min(lim, len(l5)))
    # the click: share of > 4 kHz in the first 4 ms against the whole press
    fc, Sc = _spec(y, sr, 0.0, 4.0, 1024)
    click = float(Sc[fc >= 4000].sum() / (Sc.sum() + 1e-20))
    # ring: a narrow peak 1.5-7 kHz in the press tail 12-45 ms (spring ping); dB over the band median
    fr, Sr = _spec(y, sr, 12.0, press_end if release_ms else 45.0, 8192)
    rb = (fr >= 1500) & (fr <= 7000)
    ring_db = float(10 * np.log10(Sr[rb].max() / (np.median(Sr[rb]) + 1e-20))) if rb.any() and Sr[rb].max() > 0 else 0.0
    ring_hz = float(fr[rb][int(np.argmax(Sr[rb]))]) if rb.any() else 0.0
    # the hit: first 1 ms frame within 6 dB of the loudest, from the file start (a finger touch before the
    # bottom-out is natural; a hit that lands late makes the key feel slow)
    w1 = int(0.001 * sr)
    e1 = np.array([np.mean(y0[i:i + w1] ** 2) for i in range(0, min(len(y0), int(0.060 * sr)), w1 // 4)])
    t_main = float(np.argmax(e1 >= e1.max() * 10 ** (-6 / 10)) * 0.25) if e1.size and e1.max() > 0 else 0.0
    # 10-90 % rise as the critic times it (critic/features.envelope: 1 ms RMS, to the first peak within 3 dB)
    hop = max(1, int(0.0005 * sr))
    r = np.array([np.sqrt(np.mean(y0[i:i + w1] ** 2)) for i in range(0, max(1, len(y0) - w1), hop)])
    attack = 0.0
    if r.size and r.max() > 0:
        p = int(np.argmax(r >= 0.708 * r.max()))
        while p + 1 < len(r) and r[p + 1] >= r[p]:
            p += 1
        attack = (int(np.argmax(r >= 0.9 * r[p])) - int(np.argmax(r >= 0.1 * r[p]))) * hop / sr * 1000
    # bottom-out sharpness: 10-90 % rise of the > 2 kHz band (0.25 ms RMS) into its loudest moment near the hit;
    # a real plate or case strike rises in about a millisecond, a model-smeared one takes several
    from scipy import signal as _sig
    hp = _sig.sosfilt(_sig.butter(4, 2000, "high", fs=sr, output="sos"), y0[:int(0.060 * sr)])
    q = max(1, int(0.00025 * sr))
    eh = np.array([np.sqrt(np.mean(hp[i:i + q] ** 2)) for i in range(0, max(1, len(hp) - q), q)])
    hit_rise = 0.0
    if eh.size and eh.max() > 0:
        k = int(np.argmax(eh))
        lo = max(0, k - int(0.010 * sr / q))
        seg = eh[lo:k + 1]
        below = np.flatnonzero(seg < 0.1 * eh[k])
        i10 = lo + (int(below[-1]) + 1 if below.size else 0)
        i90 = lo + int(np.argmax(seg >= 0.9 * eh[k]))
        hit_rise = max(0.0, (i90 - i10) * q / sr * 1000)
    return {
        "t_main_ms": round(t_main, 2), "attack_ms": round(max(0.0, attack), 2), "hit_rise_ms": round(hit_rise, 2),
        "centroid_hz": round(cen, 1), "peak_hz": round(peak_hz, 1),
        "share_below_250": round(share(20, 250), 4), "share_250_800": round(share(250, 800), 4),
        "share_800_2k": round(share(800, 2000), 4), "share_2k_5k": round(share(2000, 5000), 4),
        "share_5k_10k": round(share(5000, 10000), 4), "share_above_10k": round(share(10000, sr / 2), 4),
        "share_below_800": round(share(20, 800), 4), "share_above_5k": round(share(5000, sr / 2), 4),
        "decay_ms": round(decay_ms, 1), "click_share": round(click, 4), "ring_db": round(ring_db, 1),
        "ring_hz": round(ring_hz, 1), "mel_db": [round(float(v), 2) for v in mel_db], "env": [round(float(v), 4) for v in env],
    }


# ---------------------------------------------------------------- family numbers (§5.2)

def mel_dist(a: dict, b: dict) -> float:
    x, y = np.array(a["mel_db"]), np.array(b["mel_db"])
    d = (x - x.mean()) - (y - y.mean())
    return float(np.sqrt(np.mean(d ** 2)))


def env_corr(a: dict, b: dict) -> float:
    x, y = np.array(a["env"]), np.array(b["env"])
    n = min(len(x), len(y))
    if n < 3 or np.std(x[:n]) == 0 or np.std(y[:n]) == 0:
        return 0.0
    return float(np.corrcoef(x[:n], y[:n])[0, 1])


def cents_spread(vals: list[float]) -> float:
    v = np.array([x for x in vals if x > 0])
    if len(v) < 2:
        return 0.0
    c = 1200 * np.log2(v / np.exp(np.mean(np.log(v))))
    return float(np.std(c))


def family_stats(feats: list[dict]) -> dict:
    pairs = list(combinations(range(len(feats)), 2))
    md = [mel_dist(feats[i], feats[j]) for i, j in pairs]
    ec = [env_corr(feats[i], feats[j]) for i, j in pairs]
    return {
        "n": len(feats),
        "mel_dist_mean": round(float(np.mean(md)), 3) if md else 0.0,
        "mel_dist_min": round(float(np.min(md)), 3) if md else 0.0,
        "mel_dist_max": round(float(np.max(md)), 3) if md else 0.0,
        "centroid_spread_cents": round(cents_spread([f["centroid_hz"] for f in feats]), 1),
        "peak_spread_cents": round(cents_spread([f["peak_hz"] for f in feats]), 1),
        "env_corr_mean": round(float(np.mean(ec)), 3) if ec else 1.0,
    }


def kenney_reference(cache: Path, libraries: Path) -> dict:
    """P10/P50/P90 of the family numbers over the 26 Kenney Impact families (5 numbered takes each)."""
    if cache.is_file():
        return json.loads(cache.read_text("utf-8"))
    import re
    import soundfile as sf
    from build import dsp
    idx = json.loads((libraries / "index.json").read_text("utf-8"))
    fams: dict[str, list[str]] = {}
    for f in idx["files"]:
        if f.get("pack") == "Impact Sounds":
            fams.setdefault(re.sub(r"_\d+\.\w+$", "", f["file"].split("/")[-1]), []).append(f["file"])
    per, pair_md = [], []
    for name, files in sorted(fams.items()):
        feats = []
        for rel in sorted(files):
            x, sr = sf.read(str(libraries / rel), always_2d=True)
            m = dsp.resample(x.mean(axis=1), sr, SR)[:, 0]
            feats.append(features(m, SR))
        st = family_stats(feats)
        st["family"] = name
        per.append(st)
        pair_md += [mel_dist(a, b) for a, b in combinations(feats, 2)]
    keys = ["mel_dist_mean", "mel_dist_min", "centroid_spread_cents", "peak_spread_cents", "env_corr_mean"]
    ref = {k: {p: round(float(np.percentile([s[k] for s in per], q)), 3) for p, q in (("p10", 10), ("p50", 50), ("p90", 90))}
           for k in keys}
    ref["pair_mel_dist"] = {p: round(float(np.percentile(pair_md, q)), 3) for p, q in (("p10", 10), ("p50", 50), ("p90", 90))}
    ref["families"] = per
    ref["source"] = "Kenney Impact Sounds (CC0), 26 families x 5 numbered takes"
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(ref, indent=1), "utf-8")
    return ref


# ---------------------------------------------------------------- profile fit

def trap(v: float, good: tuple[float, float], bad: tuple[float, float]) -> float:
    """1 inside `good`, falling linearly to 0 at `bad` (bad[0] <= good[0] <= good[1] <= bad[1])."""
    lo, hi = good
    blo, bhi = bad
    if lo <= v <= hi:
        return 1.0
    if v < lo:
        return max(0.0, (v - blo) / (lo - blo)) if lo > blo else 0.0
    return max(0.0, (bhi - v) / (bhi - hi)) if bhi > hi else 0.0


def fit_score(feat: dict, targets: dict) -> tuple[float, dict]:
    """Weighted mean of the trapezoids of `targets` ({feature: {good: [a, b], bad: [c, d], weight: w}})."""
    parts, tw, s = {}, 0.0, 0.0
    for k, t in (targets or {}).items():
        if k not in feat or feat[k] is None:
            continue
        v = trap(float(feat[k]), tuple(t["good"]), tuple(t["bad"]))
        w = float(t.get("weight", 1.0))
        parts[k] = round(v, 3)
        s += w * v
        tw += w
    return (round(s / tw, 4) if tw else 1.0), parts
