"""Checks on the finished flipbook frames (float, what the atlas holds)."""
from __future__ import annotations

import numpy as np
from scipy import ndimage

from . import grade

LIMITS = {
    "firstFramePeak": 0.95,   # VFX_STANDARD §5.6: first frame of a flash >= 95 % of its peak
    "whiteCore": 0.30,        # FIREFLY_VFX_LIST §4: white core <= 30 % of the radius
    "blackResidue": 2 / 255,  # p99 left in the background, away from the effect
    "edge": 0.04,             # max in the outer 2 px ring of a cell (effect cut by the cell)
    "loopSeam": 1.0,          # join diff / mean neighbour diff
    "tileSeam": 1.0,          # wrap column diff / mean neighbour column diff
    "mustard": 0.25,          # share of the fire's light in dull yellow pixels, any frame
}


def visible(img: np.ndarray) -> np.ndarray:
    """What counts as the effect: alpha for RGBA, max(R,G,B) for additive RGB."""
    return img[..., 3] if img.shape[-1] == 4 else img.max(-1)


def energy(img: np.ndarray) -> float:
    return float(img[..., 3].sum()) if img.shape[-1] == 4 else float(grade.luma(img).sum())


def hot_energy(img: np.ndarray) -> float:
    if img.shape[-1] == 4:
        return float(img[..., 3].sum())
    lum = grade.luma(img)
    return float(lum[lum > 0.5].sum())


def first_frame_peak(frames: np.ndarray, flash_out: int) -> tuple[float, float]:
    """(first frame / flash peak, first frame / whole-flipbook peak), by hot energy."""
    hot = np.array([hot_energy(f) for f in frames])
    pk = float(hot[: flash_out + 2].max()) if hot.size else 0.0
    gpk = float(hot.max()) if hot.size else 0.0
    return (float(hot[0] / pk) if pk > 0 else 0.0), (float(hot[0] / gpk) if gpk > 0 else 0.0)


def white_core(frames: np.ndarray, min_area: float = 0.01) -> tuple[float, int]:
    """Largest white-core radius ratio over frames whose fire covers >= min_area of the cell."""
    worst, at = 0.0, -1
    cell = frames.shape[1] * frames.shape[2]
    for i, f in enumerate(frames):
        r, _, nf = grade.white_core_ratio(f)
        if nf >= min_area * cell and r > worst:
            worst, at = r, i
    return worst, at


def black_residue(frames: np.ndarray, dilate: int | None = None, min_peak: float = 0.25) -> float:
    """p99 of what is left away from the effect (outside its mask dilated by `dilate` px, default
    4 % of the cell's short side so a fire's own glow halo is not counted), over frames that
    still show the effect (a fading frame is all faint effect, not background)."""
    if dilate is None:
        dilate = max(6, int(round(0.04 * min(frames.shape[1], frames.shape[2]))))
    worst = 0.0
    for f in frames:
        v = visible(f)
        if float(v.max()) < min_peak:
            continue
        mask = ndimage.binary_dilation(v > 0.01, iterations=dilate)
        out = v[~mask]
        if out.size:
            worst = max(worst, float(np.percentile(out, 99)))
    return worst


def edge_max(frames: np.ndarray, ring: int = 2, skip: tuple[str, ...] = ()) -> dict:
    v = np.stack([visible(f) for f in frames])
    sides = {"top": v[:, :ring], "bottom": v[:, -ring:], "left": v[:, :, :ring], "right": v[:, :, -ring:]}
    return {k: round(float(s.max()), 4) for k, s in sides.items() if k not in skip}


def _diff(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a.astype(np.float32) - b.astype(np.float32)).mean())


def loop_seam(frames: np.ndarray) -> tuple[float, float, float]:
    """(ratio, join diff, mean neighbour diff) for a cyclic flipbook."""
    nd = [_diff(frames[i + 1], frames[i]) for i in range(len(frames) - 1)]
    mean = float(np.mean(nd)) if nd else 0.0
    seam = _diff(frames[0], frames[-1])
    return (seam / mean if mean > 0 else 0.0), seam, mean


def tile_seam(frames: np.ndarray) -> float:
    """Wrap-around column diff over the mean neighbour column diff (horizontal tiling)."""
    ratios = []
    for f in frames:
        d = np.abs(np.diff(f, axis=1)).mean()
        wrap = np.abs(f[:, 0] - f[:, -1]).mean()
        if d > 0:
            ratios.append(wrap / d)
    return float(np.mean(ratios)) if ratios else 0.0


def hsv(rgb: np.ndarray) -> np.ndarray:
    """(..., 3) RGB -> (..., 3) HSV with hue in degrees."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    mx = rgb.max(-1)
    mn = rgb.min(-1)
    d = mx - mn
    safe = np.where(d > 1e-6, d, 1.0)
    h = np.where(mx == r, ((g - b) / safe) % 6.0,
                 np.where(mx == g, (b - r) / safe + 2.0, (r - g) / safe + 4.0)) * 60.0
    h = np.where(d > 1e-6, h, 0.0)
    s = np.where(mx > 1e-6, d / np.maximum(mx, 1e-6), 0.0)
    return np.stack([h, s, mx], -1)


def mustard_mask(rgb: np.ndarray) -> np.ndarray:
    """Dull yellow: hue 40-65 deg, saturated, dim (a fade that keeps yellow while losing light)."""
    x = hsv(rgb)
    return (x[..., 0] >= 40) & (x[..., 0] <= 65) & (x[..., 1] >= 0.4) & (x[..., 2] >= 0.2) & (x[..., 2] <= 0.75)


def colour_ramp(frames: np.ndarray, min_area: float = 0.01) -> tuple[list[dict], float, list[int]]:
    """Light-weighted mean colour of the fire per frame, the share of its light in mustard pixels,
    and the frames that fail (mustard share above the limit or a mustard mean colour)."""
    ramp, worst, bad = [], 0.0, []
    cell = frames.shape[1] * frames.shape[2]
    for i, f in enumerate(frames):
        rgb = f[..., :3]
        fire = rgb.max(-1) > 0.1
        lum = grade.luma(rgb) * fire
        tot = float(lum.sum())
        if tot <= 0:
            ramp.append({"i": i, "hex": "#000000", "hue": None, "sat": 0.0, "val": 0.0, "mustard": 0.0})
            continue
        mean = (rgb * lum[..., None]).reshape(-1, 3).sum(0) / tot
        h, s, v = (float(x) for x in hsv(mean))
        frac = float((lum * mustard_mask(rgb)).sum() / tot)
        hexc = "#" + "".join(f"{int(round(c * 255)):02x}" for c in np.clip(mean, 0, 1))
        ramp.append({"i": i, "hex": hexc, "hue": round(h, 1), "sat": round(s, 3), "val": round(v, 3),
                     "mustard": round(frac, 3)})
        if fire.sum() >= min_area * cell:
            worst = max(worst, frac)
            mean_mustard = 40 <= h <= 65 and s >= 0.4 and v <= 0.75
            if frac > LIMITS["mustard"] or mean_mustard:
                bad.append(i)
    return ramp, worst, bad
