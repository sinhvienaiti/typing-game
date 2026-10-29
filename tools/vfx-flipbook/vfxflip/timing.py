"""Which source frames go into the flipbook: one-shot trim and loop-window search."""
from __future__ import annotations

import math

import numpy as np


def block_mean(x: np.ndarray, out_h: int = 18, out_w: int = 32) -> np.ndarray:
    """(T, H, W) -> (T, out_h, out_w) by block averaging (coarse shape descriptor)."""
    t, h, w = x.shape
    hh, ww = (h // out_h) * out_h, (w // out_w) * out_w
    if hh == 0 or ww == 0:
        return x.reshape(t, h, w)
    y = x[:, :hh, :ww].reshape(t, out_h, hh // out_h, out_w, ww // out_w)
    return y.mean(axis=(2, 4))


def leading_black(energy: np.ndarray, frac: float = 0.004) -> int:
    """Number of leading frames whose energy is below frac x the clip maximum."""
    thr = frac * float(energy.max()) if energy.size else 0.0
    i = 0
    while i < len(energy) - 1 and energy[i] <= thr:
        i += 1
    return i


def even_indices(start: int, end: int, n_total: int, n_min: int = 24, n_max: int = 32,
                 may_trim: bool = False) -> tuple[list[int], float]:
    """Source indices spread evenly over [start, end). Integer steps when they give n_min..n_max
    frames (even timing, no ghosting); with may_trim (a cut that ends on a cap, not on a fade)
    the end may move in so a full n_max frames fit on an integer step; otherwise the nearest frame
    on a fractional step."""
    length = end - start
    if length <= n_max:
        if length < n_min:
            length = min(n_total, start + n_min) - start
        return list(range(start, start + length)), 1.0
    if may_trim:
        s = length // n_max
        if s >= 1 and s * n_max >= 0.85 * length:
            return [start + s * i for i in range(n_max)], float(s)
    s = math.ceil(length / n_max)
    n = math.ceil(length / s)
    if n >= n_min:
        return [start + s * i for i in range(n)], float(s)
    step = length / n_max
    return [start + min(length - 1, int(round(i * step))) for i in range(n_max)], step


def find_flash_peak(hot: np.ndarray, begin: int, min_dip: float = 0.15) -> int | None:
    """First prominent local maximum of the hot energy: at least half the clip maximum and
    followed by a dip of min_dip before anything higher. None when the effect only grows (or
    only plateaus): Firefly often grows a burst over a second or two with no flash at all."""
    hs = hot.astype(np.float64)  # no smoothing: a one-frame flash is the case that matters most
    n = len(hs)
    gmax = float(hs[begin:].max())
    for t in range(begin, n):
        v = hs[t]
        if v < 0.5 * gmax or v <= 0:
            continue
        if (t > begin and hs[t - 1] > v) or (t + 1 < n and hs[t + 1] > v):
            continue
        after = hs[t + 1:]
        higher = np.nonzero(after > v)[0]
        stretch = after[: higher[0]] if higher.size else after
        if stretch.size and stretch.min() <= (1.0 - min_dip) * v:
            return t
    return None


def plan_oneshot(energy: np.ndarray, hot: np.ndarray, fps: float, *, flash: bool = True,
                 max_sec: float = 2.5, fade_frac: float = 0.03, start_frac: float = 0.05,
                 flash_window: float = 1.5, growth_start: float = 0.35,
                 n_min: int = 24, n_max: int = 32, force_start: int | None = None,
                 force_end: int | None = None, stop: np.ndarray | None = None) -> dict:
    """Drop leading black; start on the flash (first frame >= 95 % of a flash peak that comes
    within flash_window s), or for a burst that only grows, on the frame where it reaches
    growth_start of its peak (the trigger); without a flash (smoke), on the first frame above
    start_frac. End when the effect has faded out (or at max_sec); then 24-32 even frames."""
    n = len(energy)
    begin = leading_black(energy)
    info: dict = {"droppedBlack": begin, "flashPeak": None}
    if force_start is not None:
        start, mode = int(np.clip(force_start, 0, n - 1)), "forced"
    elif flash:
        peak = find_flash_peak(hot, begin)
        if peak is not None and peak - begin <= flash_window * fps:
            lo, hi = max(begin, peak - 1), min(n, peak + 2)
            peak = lo + int(np.argmax(hot[lo:hi]))
            pv = float(hot[peak])
            start = next(t for t in range(begin, peak + 1) if hot[t] >= 0.95 * pv)
            info["flashPeak"], mode = int(peak), "flash"
        else:
            pv = float(hot[begin:].max())
            start = next(t for t in range(begin, n) if hot[t] >= growth_start * pv)
            info["growthPeak"], mode = begin + int(np.argmax(hot[begin:])), "growth"
    else:
        emax = float(energy[begin:].max())
        start = next(t for t in range(begin, n) if energy[t] >= start_frac * emax)
        mode = "rise"
    tail = energy[start:]
    epk = start + int(np.argmax(tail))
    thr = fade_frac * float(tail.max())
    end, faded = n, False
    for t in range(epk, n):
        if (energy[t:] < thr).all():
            end, faded = t + 1, True
            break
    max_len = max(n_min, int(round(max_sec * fps)))
    capped = end - start > max_len
    if capped:
        end, faded = start + max_len, False
    stopped = False
    if stop is not None and force_end is None and not stop[start]:
        hits = [t for t in range(start + 1, end) if stop[t]]
        if hits:
            end, faded, capped, stopped = hits[0], False, False, True
    if force_end is not None:
        end, capped = int(np.clip(force_end, start + 2, n)), False
        faded = bool(faded and end >= n)
    idx, step = even_indices(start, end, n, n_min, n_max, may_trim=capped)
    info.update(startMode=mode, skippedBeforeStart=int(start - begin), start=int(start), end=int(end),
                faded=faded, capped=capped, stoppedAtEdge=stopped, indices=[int(i) for i in idx], step=round(step, 4),
                frames=len(idx), crossfade=0)
    return info


def refine_start(plan: dict, hot: np.ndarray, n_min: int = 24, n_max: int = 32, rel: float = 0.95) -> dict:
    """Flash mode only: re-pick the flash peak and start on the hot energy measured on the final
    cells (crop and scale shift it by a percent or two against the analysis grid), keeping the
    cut's length."""
    fp = plan.get("flashPeak")
    if fp is None or plan.get("startMode") != "flash":
        return plan
    n = len(hot)
    begin = plan["droppedBlack"]
    lo, hi = max(begin, fp - 2), min(n, fp + 3)
    peak = lo + int(np.argmax(hot[lo:hi]))
    pv = float(hot[peak])
    start = next(t for t in range(begin, peak + 1) if hot[t] >= rel * pv)
    if start == plan["start"] and peak == fp:
        return plan
    end = plan["end"]
    if plan.get("capped") or end - start < n_min:
        end = min(n, start + (plan["end"] - plan["start"]))
    idx, step = even_indices(start, end, n, n_min, n_max, may_trim=bool(plan.get("capped")))
    out = dict(plan)
    out.update(start=int(start), end=int(end), flashPeak=int(peak), skippedBeforeStart=int(start - begin),
               indices=[int(i) for i in idx], step=round(step, 4), frames=len(idx))
    return out


def crossfade_loop(frames: np.ndarray, n: int, k: int, post=None) -> np.ndarray:
    """frames holds n + k consecutive samples. The first k output frames morph from the samples
    that follow the window end (out[0] is exactly sample n, the natural successor of the last
    frame) into the window start (out[k-1] is exactly sample k-1), so every join is a real one.
    post(img, mix) may touch up a blended frame; mix is 1 at an even blend, 0 at either end."""
    out = frames[:n].copy()
    k = min(k, len(frames) - n)
    if k <= 0:
        return out
    for i in range(k):
        w = i / (k - 1) if k > 1 else 1.0
        out[i] = (1 - w) * frames[n + i] + w * frames[i]
        if post is not None:
            out[i] = post(out[i], 4.0 * w * (1.0 - w))
    return out


def seam_ratio(frames: np.ndarray) -> float:
    """Join diff (last -> first) over the mean neighbour diff, for a cyclic sequence."""
    f = frames.reshape(len(frames), -1)
    nd = np.abs(np.diff(f, axis=0)).mean(1)
    mean = float(nd.mean()) if nd.size else 0.0
    seam = float(np.abs(f[0] - f[-1]).mean())
    return seam / mean if mean > 0 else 0.0


def plan_loop(energy: np.ndarray, shapes: np.ndarray, fps: float, *, frames: int = 32,
              step: int = 1, xfade: int = 8, top: int = 6, force_start: int | None = None) -> dict:
    """Most even window: low variation of total energy and of the coarse shape, and a crossfaded
    join that is no bigger than the mean frame-to-frame change (simulated on the descriptors).
    Returns the best window plus a few runners-up for a final pick on the real cells."""
    n = len(energy)
    begin = leading_black(energy)
    k = min(xfade, max(2, frames // 4))
    while (frames + k) * step > n - begin:
        if k > 2:
            k -= 2
        elif frames > 8:
            frames -= 4
        else:
            break
    span = frames * step
    need = (frames + k) * step
    sh = shapes.reshape(n, -1).astype(np.float64)
    scored = []
    starts = [int(force_start)] if force_start is not None else range(begin, max(begin, n - need) + 1)
    for s in starts:
        idx = s + step * np.arange(frames + k)
        if idx[-1] >= n:
            continue
        e = energy[idx].astype(np.float64)
        cv = float(e.std() / max(e.mean(), 1e-9))
        w = sh[idx]
        mw = w.mean(0)
        dev = float(np.abs(w - mw).mean() / max(mw.mean(), 1e-9))
        seam = seam_ratio(crossfade_loop(w, frames, k))
        score = cv + 0.5 * dev + 0.5 * max(0.0, seam - 0.8)
        scored.append((score, s, cv, dev, seam))
    if not scored:  # clip shorter than one window: take what there is
        scored = [(0.0, begin, 0.0, 0.0, 0.0)]
    scored.sort()
    picks: list[tuple] = []
    for c in scored:
        if all(abs(c[1] - p[1]) >= 2 for p in picks):
            picks.append(c)
        if len(picks) >= top:
            break
    score, s, cv, dev, seam = picks[0]
    return {"droppedBlack": begin, "startMode": "loop", "start": int(s), "end": int(s + span), "frames": frames,
            "step": float(step), "crossfade": k,
            "indices": [int(s + step * i) for i in range(frames + k) if s + step * i < n],
            "faded": None, "capped": False, "windowScore": round(score, 4), "windowEnergyCV": round(cv, 4),
            "windowShapeDev": round(dev, 4), "simSeam": round(seam, 3),
            "candidates": [{"start": int(c[1]), "score": round(c[0], 4)} for c in picks]}


def loop_indices(plan: dict, start: int, n_total: int) -> list[int]:
    step = int(plan["step"])
    return [start + step * i for i in range(plan["frames"] + plan["crossfade"]) if start + step * i < n_total]
