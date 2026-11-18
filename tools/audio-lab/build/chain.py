"""Final ("bus") chain for one rendered mix (§5.1 step 4, §4.3.1, §11 manifest v2 common level).

Order: DC/HPF -> bus filters -> saturation -> head trim -> length cap -> tail trim + fade
(or loop crossfade) -> loudness normalise -> brick-wall limiter -> true-peak safety.
DC is removed by the high-pass only; the critic measures true DC (critic.audio.dc_estimate), not
the mean of a short decaying wave, so no mean-zeroing correction is applied here (§5.5).
"""
from __future__ import annotations

import numpy as np

from build import dsp, measure

MODE_TAG = {"lufs-m-max": "lufsM", "lufs-s-max": "lufsS", "lufs-i": "lufsI", "peak": "peak"}


def _limit(x: np.ndarray, sr: int, ceiling_db: float, release_ms: float) -> np.ndarray:
    import pedalboard  # GPL, local import only

    lim = pedalboard.BrickwallLimiter(ceiling_db=ceiling_db, release_ms=release_ms, lookahead_ms=5.0, true_peak=True)
    y = lim(np.ascontiguousarray(x.T, dtype=np.float32), sr)
    return y.T.astype(np.float64)


def _normalise_and_limit(x: np.ndarray, sr: int, norm: dict, lim: dict, rep: dict) -> np.ndarray:
    mode = norm.get("mode", "lufs-m-max")
    ceiling = float(lim.get("ceilingDbtp", -1.0))
    max_gr = float(lim.get("maxGrDb", 6.0))
    release = float(lim.get("releaseMs", 60.0))
    if mode == "none" or not np.any(x):
        rep.update({"normalise": "none", "preGainDb": 0.0})
        return x
    target = float(norm.get("target", -20.0 if mode != "peak" else ceiling))
    if mode == "peak":
        target = min(target, ceiling)
    before = measure.loudness(x, sr, mode)

    def attempt(gain_db: float) -> tuple[np.ndarray, float]:
        pre = x * dsp.db_to_gain(gain_db)
        tp_pre = measure.true_peak_db(pre, sr)
        if mode != "peak" and tp_pre > ceiling - 0.3:
            out = _limit(pre, sr, ceiling - 0.3, release)
            return out, max(0.0, tp_pre - measure.true_peak_db(out, sr))
        return pre, 0.0

    g = target - before
    best = None                          # (abs error, y, gr, level, g) among attempts within maxGrDb
    for _ in range(8):
        y, gr = attempt(g)
        if gr > max_gr + 0.05:          # too much squashing: back off, accept a shortfall
            g -= gr - max_gr + 0.05
            continue
        level = measure.loudness(y, sr, mode)
        err = target - level
        if err >= -0.1 and (best is None or abs(err) < best[0]):
            best = (abs(err), y, gr, level, g)
        if abs(err) <= 0.1 or (err > 0 and gr >= max_gr - 0.25):
            break
        # Limiter engaged: each extra dB of gain mostly becomes gain reduction.
        g += err if err < 0 or gr == 0 else min(err, max(max_gr - gr, 0.05))
    if best is None:                     # fall back to plain peak-safe gain
        g = min(target - before, ceiling - 0.3 - measure.true_peak_db(x, sr))
        y, gr = attempt(g)
        level = measure.loudness(y, sr, mode)
    else:
        _, y, gr, level, g = best
    rep.update({
        "normalise": mode, "target": target, "measuredBefore": round(before, 2), "preGainDb": round(g, 2),
        "limiterGrDb": round(gr, 2), "achieved": round(level, 2), "shortfallDb": round(max(0.0, target - level), 2),
    })
    return y


def run(x: np.ndarray, sr: int, params: dict, loop: bool = False) -> tuple[np.ndarray, dict]:
    """Apply the chain; returns (audio (n, ch) float64, report)."""
    rep: dict = {"steps": []}
    y = dsp.as2d(np.asarray(x, dtype=np.float64))
    hz = max(float(params.get("dcHpfHz") or 0.0), float(params.get("hpfHz") or 0.0))
    if hz > 0:
        y = dsp.apply_filters(y, [{"type": "highpass", "hz": hz, "order": 2}], sr)
        rep["steps"].append(f"hpf{hz:g}")
    if params.get("filters"):
        y = dsp.apply_filters(y, params["filters"], sr)
        rep["steps"].append("eq" + "+".join(f["type"] for f in params["filters"]))
    sat = params.get("saturation")
    if sat and sat.get("driveDb", 0) > 0:
        y = dsp.saturate(y, float(sat["driveDb"]), float(sat.get("mix", 1.0)))
        rep["steps"].append(f"sat{sat['driveDb']:g}dB")
    head = params.get("headTrim")
    if head and not loop:
        y, cut = dsp.head_trim(y, float(head.get("thresholdDb", -50.0)), float(head.get("preRollMs", 0.5)), sr)
        rep["headCutMs"] = round(1000.0 * cut / sr, 2)
        rep["steps"].append(f"trim<{head.get('preRollMs', 0.5):g}ms")
    cap = params.get("maxLengthMs")
    capped = False
    if cap and y.shape[0] > dsp.ms_to_n(cap, sr):
        y = y[: dsp.ms_to_n(cap, sr)]
        capped = True
        rep["steps"].append(f"cap{cap:g}ms")
    tail = params.get("tail")
    if loop:
        xf = float(params.get("loopCrossfadeMs") or 0.0)
        if xf > 0:
            y = dsp.loop_crossfade(y, xf, sr)
            rep["steps"].append(f"loopxf{xf:g}ms")
    elif tail and tail.get("shape") == "exp":
        # exponential cap from the knee to floorDb at the last sample (no flat cut then fade)
        n = y.shape[0]
        pk = int(np.argmax(np.max(np.abs(y), axis=1))) if n else 0
        knee = dsp.ms_to_n(float(tail["kneeMs"]), sr) if tail.get("kneeMs") is not None else int(0.35 * n)
        knee = max(knee, pk + dsp.ms_to_n(5.0, sr))
        y, info = dsp.exp_cap_tail(y, sr, knee, float(tail.get("floorDb", -60.0)))
        rep["tailShape"] = {"shape": "exp", "capped": capped, **info}
        rep["steps"].append(f"expTail{info['knee_ms']:g}ms>{tail.get('floorDb', -60.0):g}dB")
    elif tail:
        n0 = y.shape[0]
        y = dsp.tail_trim(y, float(tail.get("floorDb", -60.0)), sr)
        y = dsp.fade(y, out_ms=float(tail.get("fadeMs", 10.0)), sr=sr)
        rep["tailCutMs"] = round(1000.0 * (n0 - y.shape[0]) / sr, 2)
        rep["steps"].append(f"tail{tail.get('floorDb', -60.0):g}dB+{tail.get('fadeMs', 10.0):g}ms")
    norm = params.get("normalise") or {"mode": "none"}
    lim = params.get("limiter") or {}
    y = _normalise_and_limit(y, sr, norm, lim, rep)
    if rep.get("normalise") not in (None, "none"):
        rep["steps"].append(f"{MODE_TAG[rep['normalise']]}{rep['target']:g}")
    # Safety: the file never exceeds the true-peak ceiling (so it never clips).
    ceiling = float(lim.get("ceilingDbtp", -1.0))
    tp = measure.true_peak_db(y, sr)
    safety = 0.0
    if tp > ceiling:
        safety = ceiling - tp - 0.02
        y = y * dsp.db_to_gain(safety)
    rep["safetyGainDb"] = round(safety, 3)
    rep["steps"].append(f"tp{ceiling:g}")
    rep["summary"] = ", ".join(rep["steps"])
    return y, rep
