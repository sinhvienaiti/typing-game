"""Colour work on float RGB frames in [0, 1]: black crush, luma matte, highlight shoulder, fades.

Every curve here scales R, G and B by one factor per pixel, so hue never shifts and no channel
clips on its own (the "do not clip colour" rule of FIREFLY_VFX_LIST §4).
"""
from __future__ import annotations

import numpy as np
from scipy import ndimage

LUMA = np.array([0.2126, 0.7152, 0.0722], np.float32)
# Neutral cool charcoal for smoke-roll: the densest smoke; lighter smoke is this hue, brighter.
SMOKE_DENSE = np.array([0.125, 0.13, 0.142], np.float32)


def to_float(frames: np.ndarray) -> np.ndarray:
    return frames.astype(np.float32) / 255.0 if frames.dtype == np.uint8 else frames.astype(np.float32)


def luma(rgb: np.ndarray) -> np.ndarray:
    return rgb[..., :3] @ LUMA


def smoothstep(e0: float, e1: float, x):
    t = np.clip((np.asarray(x, np.float32) - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


def knee(x, t, k: float):
    """Soft threshold: 0 below t, a quadratic knee of width k, then slope 1 (C1 continuous)."""
    d = np.asarray(x, np.float32) - t
    return np.where(d <= 0, 0.0, np.where(d < k, d * d / (2.0 * k), d - k / 2.0)).astype(np.float32)


def estimate_black_level(frames: np.ndarray, ring: int = 6) -> tuple[float, float]:
    """Background noise of a black-background clip, read from the frame borders.

    Takes, per side, the median over frames of the 99th percentile of max(R,G,B) in a border
    strip, and uses the cleanest side (the effect may reach some borders in some frames).
    Returns (threshold, noise)."""
    m = to_float(frames).max(-1)
    n = m.shape[0]
    sides = (m[:, :ring, :], m[:, -ring:, :], m[:, :, :ring], m[:, :, -ring:])
    noise = min(float(np.median(np.percentile(s.reshape(n, -1), 99, axis=1))) for s in sides)
    return float(np.clip(noise + 0.012, 0.02, 0.12)), noise


def crush_black(rgb: np.ndarray, t0: float, k: float = 0.05, grey_cut: float = 0.0) -> np.ndarray:
    """Additive clips: near-black goes to exactly 0 through a smooth knee; 1.0 still maps to 1.0.

    grey_cut lifts the threshold for dark, unsaturated pixels only (charcoal smoke on black). In
    additive blending they add a grey veil, never smoke; saturated deep-red flame edges and the
    bright core keep the base threshold."""
    m = rgb.max(-1)
    t = t0
    if grey_cut > 0:
        mn = rgb.min(-1)
        sat = (m - mn) / np.maximum(m, 1e-6)
        grey = (1.0 - smoothstep(0.3, 0.65, sat)) * (1.0 - smoothstep(0.25, 0.5, m))
        # soften the map a little so the cut never draws a hard contour between smoke and flame
        sigma = [0.0] * (grey.ndim - 2) + [1.0, 1.0]
        grey = ndimage.gaussian_filter(grey, sigma)
        t = t0 + grey_cut * grey
    norm = 1.0 - t0 - k / 2.0
    mo = knee(m, t, k) / norm
    scale = np.where(m > 1e-6, mo / np.maximum(m, 1e-6), 0.0)
    return np.clip(rgb * scale[..., None], 0.0, 1.0).astype(np.float32)


def background_plate(lum: np.ndarray, sigma: float = 2.0) -> np.ndarray:
    """White-background clips: per-pixel max of luma over time (smoke uncovers every pixel at
    some point), blurred. Pixels never uncovered fall back to the plate median."""
    plate = lum.max(0)
    good = plate > 0.6
    fill = float(np.median(plate[good])) if good.any() else 1.0
    plate = np.where(good, plate, fill)
    if sigma > 0:
        plate = ndimage.gaussian_filter(plate, sigma)
    return plate.astype(np.float32)


def luma_matte(rgb: np.ndarray, plate: np.ndarray, t: float = 0.015, k: float = 0.03,
               opaque_at: float = 0.65) -> np.ndarray:
    """Dark smoke on white -> RGBA (straight alpha) in neutral cool charcoal.

    The raw matte a = (white - L) / (white - L_charcoal) reaches full opacity at `opaque_at`, and
    the colour is solved so that the result over the white plate reproduces the source luma
    exactly: dense smoke keeps its own light and shade (so it is not a flat grey shape on a dark
    ground) and the thin fringe settles on a lighter charcoal. RGB is defined everywhere, so
    filtering and premultiplying never pull white or black into the edges."""
    lum = luma(rgb)
    lc = float(SMOKE_DENSE @ LUMA)
    a = (plate - lum) / np.maximum(plate - lc, 1e-3)
    a = np.clip(knee(a, t, k) / (1.0 - t - k / 2.0), 0.0, 1.0)
    alpha = np.clip(a / opaque_at, 0.0, 1.0)
    fringe = plate * (1.0 - opaque_at) + lc * opaque_at          # the colour as alpha -> 0
    solved = (lum - plate * (1.0 - alpha)) / np.maximum(alpha, 1e-4)
    c = np.where(alpha > 1e-3, solved, fringe)
    c = np.clip(c, lc * 0.6, 0.55)
    tint = SMOKE_DENSE / lc                                      # luma 1, cool neutral
    colour = c[..., None] * tint
    return np.concatenate([colour, alpha[..., None]], -1).astype(np.float32)


def shoulder(rgb: np.ndarray, peak: float, knee_at: float = 0.6) -> np.ndarray:
    """Lower the peak (1.0 -> peak) with a smooth, hue-preserving shoulder above knee_at.
    Monotonic for peak >= 0.8."""
    m = rgb.max(-1)
    s = smoothstep(knee_at, 1.0, m)
    mo = m - (1.0 - peak) * s * s
    scale = np.where(m > 1e-6, mo / np.maximum(m, 1e-6), 0.0)
    return (rgb * scale[..., None]).astype(np.float32)


WARM = np.array([1.0, 0.9, 0.6], np.float32)  # hot white-yellow the over-wide core is pulled toward


def _warm_once(rgb: np.ndarray, keep_ratio: float, white: np.ndarray, nf: int, white_thr: float) -> np.ndarray:
    mn = rgb.min(-1)
    w = smoothstep(0.6, white_thr, mn) * ~white
    nw = int(white.sum())
    keep = int(keep_ratio * keep_ratio * nf)
    if nw and keep < nw:
        dist = ndimage.distance_transform_edt(white)
        vals = np.sort(dist[white])[::-1]
        d_star = float(vals[keep]) if keep > 0 else float(vals[0]) + 1.0
        band = 1.0 + 0.2 * d_star
        w = np.where(white, 1.0 - smoothstep(d_star - 2 * band, d_star, dist), w)
    elif nw:
        w = np.where(white, 0.0, w)
    w = w[..., None].astype(np.float32)
    return (rgb * (1.0 - w) + rgb * WARM * w).astype(np.float32)


def warm_core(rgb: np.ndarray, target: float = 0.28, fire_thr: float = 0.1, white_thr: float = 0.85) -> np.ndarray:
    """Shrink a white core wider than `target` of the fire's radius by warming its outer part
    toward hot white-yellow (the brightest channel stays; green and blue come down), so the
    ramp reads white -> yellow -> orange instead of a flat white blob. Near-white pixels around
    the core warm with it, so no ring appears where the mask ends. No channel is clipped."""
    white = (rgb > white_thr).all(-1)
    nf = int((rgb.max(-1) > fire_thr).sum())
    keep_ratio = target
    out = _warm_once(rgb, keep_ratio, white, nf, white_thr)
    for _ in range(10):  # the soft edge of the warm zone leaves some white: tighten until it fits
        if white_core_ratio(np.round(out * 255) / 255, fire_thr, white_thr)[0] <= target:
            break
        keep_ratio *= 0.85
        out = _warm_once(rgb, keep_ratio, white, nf, white_thr)
    return out


def cool_fade(img: np.ndarray, f: float) -> np.ndarray:
    """Fade-out that cools like fire (blue and green die first, so it ends in deep red, never in
    mustard yellow). RGBA frames fade their alpha instead."""
    f = float(np.clip(f, 0.0, 1.0))
    if img.shape[-1] == 4:
        out = img.copy()
        out[..., 3] *= f
        return out
    gains = np.array([f, f ** 1.6, f ** 2.4], np.float32)
    return (img * gains).astype(np.float32)


def cool_dim(rgb: np.ndarray, strength: float) -> np.ndarray:
    """Push dim pixels toward red, as cooling fire does (bright pixels untouched). Used where a
    crossfade halves the light of non-overlapping flames, which would otherwise read as dull
    mustard yellow."""
    if strength <= 0:
        return rgb
    v = rgb.max(-1)
    f = np.sqrt(smoothstep(0.15, 0.85, v))
    f = 1.0 - strength * (1.0 - f)
    out = rgb.copy()
    out[..., 1] *= f
    out[..., 2] *= f * f
    return out.astype(np.float32)


def white_core_ratio(rgb: np.ndarray, fire_thr: float = 0.1, white_thr: float = 0.85) -> tuple[float, int, int]:
    """sqrt(white area / fire area): the white core's radius as a share of the fire's radius."""
    fire = rgb.max(-1) > fire_thr
    white = (rgb[..., :3] > white_thr).all(-1)
    nf, nw = int(fire.sum()), int(white.sum())
    return (float(np.sqrt(nw / nf)) if nf else 0.0), nw, nf
