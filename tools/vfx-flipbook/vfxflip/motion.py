"""Forward optical flow in cell UV, quantised as x-rgb-y-a for the lab shader."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image
from scipy import ndimage

from . import media


def _cv2():
    try:
        import cv2
    except ImportError as exc:
        raise media.MediaError(
            "thiếu OpenCV; chạy uv pip install --python tools/vfx-flipbook/.venv/bin/python "
            "-r tools/vfx-flipbook/requirements.txt") from exc
    return cv2


def cells_from_atlas(png: Path, cols: int, rows: int, cw: int, ch: int, n: int) -> np.ndarray:
    with Image.open(png) as image:
        pixels = np.asarray(image.convert("RGBA" if "A" in image.getbands() else "RGB"))
    if pixels.shape[:2] != (rows * ch, cols * cw) or not 1 <= n <= cols * rows:
        raise media.MediaError("kích thước atlas hoặc số ô không hợp lệ")
    return np.stack([pixels[(i // cols) * ch:(i // cols + 1) * ch,
                            (i % cols) * cw:(i % cols + 1) * cw] for i in range(n)])


def luma8(image: np.ndarray) -> np.ndarray:
    x = image[..., :3].max(-1).astype(np.float32)
    if image.shape[-1] == 4:
        x *= image[..., 3].astype(np.float32) / 255
    return np.round(255 * np.sqrt(x / 255)).astype(np.uint8)


def encode(vector: np.ndarray, strength: float) -> np.ndarray:
    return np.clip(np.round(128 + 127 * vector / strength), 1, 255).astype(np.uint8)


def decode(encoded: np.ndarray, strength: float) -> np.ndarray:
    return (encoded.astype(np.float32) - 128) / 127 * strength


def warp_blend(f0: np.ndarray, f1: np.ndarray, d_px: np.ndarray, w: float) -> np.ndarray:
    """Reference shader sampling; d_px has screen-pixel axes (x right, y down)."""
    cv2 = _cv2()
    h, width = f0.shape[:2]
    d_px = np.asarray(d_px, dtype=np.float32)
    yy, xx = np.mgrid[:h, :width].astype(np.float32)
    def sample(f, t):
        return cv2.remap(f.astype(np.float32), xx + t * d_px[..., 0], yy + t * d_px[..., 1],
                         cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return (1 - w) * sample(f0, -w) + w * sample(f1, 1 - w)


def flow(cells: np.ndarray, loop: bool) -> dict:
    cv2 = _cv2()
    n, ch, cw, _ = cells.shape
    grey = luma8(cells)
    uv = np.zeros((n, ch, cw, 2), np.float32)
    masks = np.zeros((n, ch, cw), bool)
    solver = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
    pairs = n if loop else n - 1
    for i in range(pairs):
        j = (i + 1) % n
        d = solver.calc(grey[i], grey[j], None)
        mask = cv2.dilate(((grey[i] > 8) | (grey[j] > 8)).astype(np.uint8), np.ones((9, 9), np.uint8))
        soft = ndimage.gaussian_filter(mask.astype(np.float32), sigma=2)
        d *= soft[..., None]
        uv[i, ..., 0] = d[..., 0] / cw
        uv[i, ..., 1] = -d[..., 1] / ch
        masks[i] = soft > 0
    selected = np.abs(uv[masks])
    strength = max(1e-4, float(np.percentile(selected, 99.5)) if selected.size else 0)
    strength = math.ceil(strength * 100000) / 100000
    encoded = encode(uv, strength)
    ratios = []
    for i in range(pairs):
        a, b = cells[i].astype(np.float32) / 255, cells[(i + 1) % n].astype(np.float32) / 255
        base = float(np.abs(b - a).mean())
        if base > 0.5 / 255:
            d = decode(encoded[i], strength) * np.array([cw, -ch], np.float32)
            yy, xx = np.mgrid[:ch, :cw].astype(np.float32)
            # Warp only f0 to t=1: blending at w=1 would return f1 and hide all errors.
            warped = cv2.remap(a, xx - d[..., 0], yy - d[..., 1], cv2.INTER_LINEAR,
                               borderMode=cv2.BORDER_CONSTANT, borderValue=0)
            ratios.append(float(np.abs(warped - b).mean()) / base)
    return {"uv": uv, "encoded": encoded, "strength": strength,
            "checks": {"warpRatio": float(np.median(ratios)) if ratios else None,
                       "warpRatioP90": float(np.percentile(ratios, 90)) if ratios else None}}


def write_atlas(encoded: np.ndarray, cols: int, rows: int, path: Path) -> None:
    n, ch, cw, _ = encoded.shape
    pixels = np.full((rows * ch, cols * cw, 4), 128, np.uint8)
    for i in range(n):
        rgba = np.concatenate([np.repeat(encoded[i, ..., :1], 3, axis=-1), encoded[i, ..., 1:2]], -1)
        y, x = (i // cols) * ch, (i % cols) * cw
        pixels[y:y + ch, x:x + cw] = rgba
    Image.fromarray(pixels).save(path, compress_level=7)
