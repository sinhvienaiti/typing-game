"""Where to crop: mass centroid over the whole cut, effect extent, cell-shaped crop rectangles."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import ndimage


@dataclass
class Box:
    x0: float
    y0: float
    x1: float
    y1: float

    def union(self, o: "Box") -> "Box":
        return Box(min(self.x0, o.x0), min(self.y0, o.y0), max(self.x1, o.x1), max(self.y1, o.y1))


def centroid(w: np.ndarray) -> tuple[float, float] | None:
    tot = float(w.sum())
    if tot <= 0:
        return None
    h, wd = w.shape
    xs = np.arange(wd) + 0.5
    ys = np.arange(h) + 0.5
    return float((w.sum(0) * xs).sum() / tot), float((w.sum(1) * ys).sum() / tot)


def core_centroid(lum: np.ndarray, rel: float = 0.85) -> tuple[float, float] | None:
    """Centroid of the hottest pixels (>= rel x frame max): the effect's hot core."""
    mx = float(lum.max())
    if mx <= 0:
        return None
    return centroid(np.where(lum >= rel * mx, lum, 0.0))


def extent(acc: np.ndarray, maxmap: np.ndarray, thr: float = 0.01, q: float = 0.001) -> Box:
    """Bounding box of everything visible in any frame of the cut (opened to drop single noisy
    pixels), joined with the box holding all but q of the accumulated energy on each side."""
    h, w = acc.shape
    box = None
    mask = ndimage.binary_opening(maxmap > thr, iterations=1)
    if mask.any():
        ys, xs = np.nonzero(mask)
        box = Box(float(xs.min()), float(ys.min()), float(xs.max() + 1), float(ys.max() + 1))
    tot = float(acc.sum())
    if tot > 0:
        cx = np.cumsum(acc.sum(0)) / tot
        cy = np.cumsum(acc.sum(1)) / tot
        qb = Box(float(np.searchsorted(cx, q)), float(np.searchsorted(cy, q)),
                 float(min(w, np.searchsorted(cx, 1 - q) + 1)), float(min(h, np.searchsorted(cy, 1 - q) + 1)))
        box = qb if box is None else box.union(qb)
    return box or Box(0.0, 0.0, float(w), float(h))


def touches_border(maxmap: np.ndarray, thr: float = 0.15, ring: int = 2) -> list[str]:
    strong = maxmap > thr
    sides = {"top": strong[:ring].any(), "bottom": strong[-ring:].any(),
             "left": strong[:, :ring].any(), "right": strong[:, -ring:].any()}
    return [k for k, v in sides.items() if v]


def crop_centre(c: tuple[float, float], box: Box, aspect: float, margin: float) -> tuple[float, float, float, float]:
    """Crop centred on the mass centroid, large enough for the whole extent plus margin."""
    cx, cy = c
    hx = max(cx - box.x0, box.x1 - cx)
    hy = max(cy - box.y0, box.y1 - cy)
    hh = max(hy, hx / aspect) * (1.0 + margin) + 1.0
    hw = hh * aspect
    return cx - hw, cy - hh, 2 * hw, 2 * hh


def crop_bbox(box: Box, aspect: float, margin: float) -> tuple[float, float, float, float]:
    """Crop around the effect's own extent (not symmetric about the centroid): more pixels for a
    lopsided effect such as a projectile with a long tail; the pivot then carries the anchor."""
    cx, cy = (box.x0 + box.x1) / 2, (box.y0 + box.y1) / 2
    hw = (box.x1 - box.x0) / 2 * (1.0 + margin) + 1.0
    hh = (box.y1 - box.y0) / 2 * (1.0 + margin) + 1.0
    hh = max(hh, hw / aspect)
    hw = hh * aspect
    return cx - hw, cy - hh, 2 * hw, 2 * hh


def crop_left(core: tuple[float, float], c: tuple[float, float], box: Box, aspect: float,
              margin: float) -> tuple[float, float, float, float]:
    """Directional clip (left -> right): the left edge sits just left of the flash, the axis stays
    horizontal, centred vertically on the mass centroid; widens to the right when needed."""
    span = max(box.x1 - box.x0, 1.0)
    left = min(box.x0, core[0]) - margin * span
    right = box.x1 + margin * span
    w = right - left
    cy = c[1]
    hy = max(cy - box.y0, box.y1 - cy) * (1.0 + margin) + 1.0
    h = max(w / aspect, 2 * hy)
    w = h * aspect
    return left, cy - h / 2, w, h


def strip_span(acc: np.ndarray, rel: float = 0.6) -> tuple[int, int]:
    """Widest run of columns whose energy is at least rel x the median column energy, preferring
    the run nearest the frame centre (drops vignetted frame edges of a horizontal band)."""
    col = acc.sum(0)
    pos = col[col > 0]
    if pos.size == 0:
        return 0, acc.shape[1]
    good = col >= rel * float(np.median(pos))
    runs, start = [], None
    for x, g in enumerate(list(good) + [False]):
        if g and start is None:
            start = x
        elif not g and start is not None:
            runs.append((start, x))
            start = None
    if not runs:
        return 0, acc.shape[1]
    mid = acc.shape[1] / 2
    runs.sort(key=lambda r: (-(r[1] - r[0]), abs((r[0] + r[1]) / 2 - mid)))
    return runs[0]


def crop_strip(acc: np.ndarray, c: tuple[float, float], box: Box, aspect: float, margin: float,
               max_squash: float = 1.6) -> tuple[tuple[float, float, float, float], float, bool]:
    """Horizontal strip: the even span of the band, height from the strip aspect, centred on the
    band. A band taller than that is fitted by squashing it vertically (ribbon textures are
    stretched along the ribbon anyway), up to max_squash. Returns (rect, squash, fits)."""
    x0, x1 = strip_span(acc)
    w = float(x1 - x0)
    h = w / aspect
    need = (box.y1 - box.y0) * (1.0 + 2 * margin)
    squash = 1.0
    if need > h:
        squash = min(max_squash, need / h)
        h *= squash
    cy = (box.y0 + box.y1) / 2
    return (float(x0), cy - h / 2, w, h), squash, need <= h + 1e-6


def principal_axis(w: np.ndarray) -> tuple[float, float]:
    """(angle in degrees, elongation) of the weighted mass; angle in (-90, 90], image axes
    (x right, y down), so a streak rising to the right has a negative angle."""
    c = centroid(w)
    if c is None:
        return 0.0, 1.0
    tot = float(w.sum())
    ys, xs = np.mgrid[0:w.shape[0], 0:w.shape[1]].astype(np.float64)
    dx, dy = xs + 0.5 - c[0], ys + 0.5 - c[1]
    cxx = float((w * dx * dx).sum() / tot)
    cyy = float((w * dy * dy).sum() / tot)
    cxy = float((w * dx * dy).sum() / tot)
    ang = 0.5 * np.degrees(np.arctan2(2 * cxy, cxx - cyy))
    tr, det = cxx + cyy, cxx * cyy - cxy * cxy
    disc = max(0.0, tr * tr / 4 - det) ** 0.5
    l1, l2 = tr / 2 + disc, max(1e-9, tr / 2 - disc)
    return float(ang), float((l1 / l2) ** 0.5)


def to_source(rect: tuple[float, float, float, float], sx: float, sy: float,
              aspect: float | None) -> tuple[int, int, int, int]:
    """Analysis-pixel rect -> integer source-pixel rect (even sizes). With an aspect, the rect is
    grown to exactly that aspect around its centre; with None it keeps its own shape."""
    x, y, w, h = rect
    cx, cy = (x + w / 2) * sx, (y + h / 2) * sy
    ws, hs = max(16.0, w * sx), max(2.0, h * sy)
    if aspect is not None:
        hs2 = ws / aspect
        if hs2 < hs:
            ws = hs * aspect
        else:
            hs = hs2
    wi = int(round(ws / 2)) * 2
    hi = int(round((wi / aspect if aspect is not None else hs) / 2)) * 2
    return int(round(cx - wi / 2)), int(round(cy - hi / 2)), wi, max(2, hi)
