"""Colour work on float RGB frames in [0, 1]: black crush, luma matte, matte video, highlight shoulder, fades.

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


def neutral_fade(img, f):
    f = float(np.clip(f, 0.0, 1.0))
    out = img.copy()
    if img.shape[-1] == 4:
        out[..., 3] *= f
    else:
        out *= f
    return out.astype(np.float32)


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


def coverage_matte(rgb: np.ndarray, t: float = 0.004, k: float = 0.02, opaque_at: float = 0.25) -> np.ndarray:
    """Bright effect on black (fire, white smoke) -> coverage 0..1: the luma matte read against a black plate.

    The frames are already black-crushed, so the plate is 0: coverage rises from the black level through a soft
    knee and is opaque from `opaque_at` luma. The game colours the effect itself; this only says where it is."""
    lum = luma(rgb)
    a = knee(lum, t, k) / max(opaque_at - t - k / 2.0, 1e-3)
    return np.clip(a, 0.0, 1.0).astype(np.float32)


def widen_coverage(alpha: np.ndarray, px: float = 2.5, temporal: int = 1) -> np.ndarray:
    """Coverage (T, H, W) widened by `px` (grey dilation over a disc, then a 0.6 px blur so the new edge stays
    soft) and the max over +-`temporal` neighbouring frames, so a frame blended toward the next never thins to a
    see-through veil where the two shapes do not overlap."""
    out = alpha.astype(np.float32)
    if px > 0:
        r = int(np.ceil(px))
        yy, xx = np.mgrid[-r:r + 1, -r:r + 1]
        disc = (np.hypot(xx, yy) <= px + 0.25)[None]
        out = ndimage.grey_dilation(out, footprint=disc)
        out = ndimage.gaussian_filter(out, [0.0, 0.6, 0.6])
    if temporal > 0 and len(out) > 1:
        out = ndimage.maximum_filter1d(out, size=2 * int(temporal) + 1, axis=0, mode="nearest")
    return np.clip(out, 0.0, 1.0).astype(np.float32)


def alpha_levels(matte: np.ndarray, t0: float, k: float = 0.02, top: float = 0.97) -> np.ndarray:
    """Matte video (grey 0..1) -> alpha: codec noise up to t0 goes to exactly 0 through a soft knee, and `top` and
    above are opaque (H.264 leaves the flat interior of the matte at 0.95-1.0)."""
    a = knee(matte, t0, k) / max(top - t0 - k / 2.0, 1e-3)
    return np.clip(a, 0.0, 1.0).astype(np.float32)


def _fill(values: np.ndarray, weight: np.ndarray, sigmas: tuple[float, ...]) -> tuple[np.ndarray, np.ndarray]:
    """Normalised convolution: the weighted mean of `values` (H, W, C) around each pixel, fine scales first, each
    coarser scale filling only what the finer ones did not reach. Returns (filled, how much was reached 0..1)."""
    out = np.zeros(values.shape, np.float32)
    have = np.zeros(weight.shape, np.float32)
    vw = values * weight[..., None]
    for s in sigmas:
        den = ndimage.gaussian_filter(weight, s)
        num = ndimage.gaussian_filter(vw, [s, s, 0])
        take = smoothstep(0.02, 0.2, den) * (1.0 - have)
        out += take[..., None] * (num / np.maximum(den, 1e-6)[..., None])
        have += take
    return out, have


def clean_plate(rgb: np.ndarray, clear: np.ndarray, factor: int = 4) -> np.ndarray:
    """The backdrop the colour video was rendered on, under the effect: the colour of the clear pixels (matte 0)
    filled inward. Firefly's backdrop is a smooth gradient that brightens with the effect, so this works per frame
    at 1/`factor` resolution and is scaled back up bilinearly."""
    h, w = clear.shape
    hh, ww = -(-h // factor), -(-w // factor)
    pad = ((0, hh * factor - h), (0, ww * factor - w))
    wgt = np.pad(clear.astype(np.float32), pad, mode="edge")
    col = np.pad(rgb, pad + ((0, 0),), mode="edge") * wgt[..., None]
    den = wgt.reshape(hh, factor, ww, factor).mean((1, 3))
    num = col.reshape(hh, factor, ww, factor, 3).mean((1, 3))
    coarse = num / np.maximum(den, 1e-6)[..., None]
    plate, have = _fill(coarse, den, (1.0, 3.0, 8.0, 24.0))
    rest = (num.sum((0, 1)) / den.sum()) if den.sum() > 0 else np.zeros(3, np.float32)
    plate += (1.0 - have)[..., None] * rest
    plate = ndimage.zoom(plate, (factor, factor, 1), order=1, mode="nearest", grid_mode=True)
    return plate[:h, :w].astype(np.float32)


def decontaminate(rgb: np.ndarray, alpha: np.ndarray, plate: np.ndarray, trust: tuple[float, float] = (0.05, 0.35),
                  spread_px: float = 1.5) -> np.ndarray:
    """Colour video over its own backdrop + alpha -> RGBA, straight alpha, with the backdrop taken out of the edges.

    The colour is C = a F + (1 - a) B (measured on Firefly's transparent clips), so F = (C - (1 - a) B) / a. Where
    alpha is small that division mostly amplifies codec noise, so below `trust` the colour moves to that of the
    nearest solid pixel (alpha >= 0.5), slightly blurred; that colour also fills the clear area, so RGB is defined
    everywhere and filtering or mipmaps never pull the backdrop (or black) into the edge."""
    a = alpha[..., None]
    p = np.minimum(np.clip(rgb - (1.0 - a) * plate, 0.0, None), a)   # premultiplied foreground, F <= 1
    f = p / np.maximum(a, 1e-4)
    solid = alpha >= 0.5
    if solid.any():
        _, (iy, ix) = ndimage.distance_transform_edt(~solid, return_indices=True)
        ext = f[iy, ix]
        if spread_px > 0:
            ext = ndimage.gaussian_filter(ext, [spread_px, spread_px, 0])
    elif alpha.sum() > 0:
        ext = np.broadcast_to((p.reshape(-1, 3).sum(0) / alpha.sum()).astype(np.float32), f.shape)
    else:
        ext = np.zeros_like(f)
    w = smoothstep(trust[0], trust[1], alpha)[..., None]
    out = w * f + (1.0 - w) * ext
    return np.concatenate([np.clip(out, 0.0, 1.0), a], -1).astype(np.float32)


def matte_video_rgba(rgb: np.ndarray, matte: np.ndarray, t0: float) -> np.ndarray:
    """One frame of a transparent Firefly clip (colour frame + its matte frame, float) -> RGBA, straight alpha."""
    alpha = alpha_levels(matte, t0)
    clear = ndimage.binary_erosion(matte <= t0, iterations=2)
    return decontaminate(rgb, alpha, clean_plate(rgb, clear))


def edge_fringe(frames: np.ndarray, band: int = 4) -> dict:
    """Dark or grey fringe check for RGBA frames: the straight colour of the soft edge (0.1 < alpha < 0.6) against
    the solid colour just inside it (alpha > 0.95, within `band` px). Luma and saturation ratios near 1 mean a
    clean edge; a backdrop or black left in the edge pulls them down."""
    se = ss = sl = si = 0.0
    n_edge = 0
    for f in frames:
        a = f[..., 3]
        edge = (a > 0.1) & (a < 0.6)
        if edge.sum() < 20:
            continue
        inside = (a > 0.95) & ndimage.binary_dilation(edge, iterations=band)
        if inside.sum() < 20:
            continue
        rgb = f[..., :3]
        lum = luma(rgb)
        mx = rgb.max(-1)
        sat = np.where(mx > 1e-4, (mx - rgb.min(-1)) / np.maximum(mx, 1e-4), 0.0)
        ne, ni = int(edge.sum()), int(inside.sum())
        sl += float(lum[edge].mean()) * ne
        si += float(lum[inside].mean()) * ne
        se += float(sat[edge].mean()) * ne
        ss += float(sat[inside].mean()) * ne
        n_edge += ne
    if n_edge == 0:
        return {"edgeVsInsideLuma": None, "edgeVsInsideSat": None, "edgePixels": 0}
    return {"edgeVsInsideLuma": round(sl / max(si, 1e-6), 3), "edgeVsInsideSat": round(se / max(ss, 1e-6), 3),
            "edgePixels": n_edge}


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
