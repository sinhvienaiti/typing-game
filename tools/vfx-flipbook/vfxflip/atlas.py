"""Atlas PNG, contact sheet over a light and a dark ground, preview frames."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

DARK = np.array([0.06, 0.07, 0.09], np.float32)
LIGHT = np.array([0.70, 0.70, 0.68], np.float32)


def grid(n: int, cw: int, ch: int) -> tuple[int, int]:
    """Power-of-two cols x rows (so the atlas is power-of-two too): smallest area, then the
    squarest atlas, then the wider one."""
    best = None
    for c in (1, 2, 4, 8, 16, 32, 64):
        for r in (1, 2, 4, 8, 16, 32, 64):
            if c * r < n:
                continue
            w, h = c * cw, r * ch
            key = (w * h, max(w, h) / min(w, h), -w)
            if best is None or key < best[0]:
                best = (key, c, r)
    return best[1], best[2]


def to_uint8(frames: np.ndarray) -> np.ndarray:
    return np.clip(np.round(frames * 255.0), 0, 255).astype(np.uint8)


def write_atlas(frames: np.ndarray, cols: int, rows: int, path: Path) -> tuple[int, int]:
    """frames (N, h, w, C) float -> PNG, row-major from the top-left cell. RGB for additive,
    RGBA (straight alpha) for normal blending."""
    n, h, w, c = frames.shape
    atlas = np.zeros((rows * h, cols * w, c), np.uint8)
    if c == 4:
        atlas[..., :3] = to_uint8(frames[0, ..., :3]).reshape(-1, 3)[0]  # unused cells: charcoal, alpha 0
    q = to_uint8(frames)
    for i in range(n):
        r, k = divmod(i, cols)
        atlas[r * h:(r + 1) * h, k * w:(k + 1) * w] = q[i]
    Image.fromarray(atlas, "RGBA" if c == 4 else "RGB").save(path, compress_level=7)
    return cols * w, rows * h


def composite(frame: np.ndarray, ground: np.ndarray) -> np.ndarray:
    """How the frame looks in game: additive on the ground, or alpha-over for RGBA."""
    if frame.shape[-1] == 4:
        a = frame[..., 3:4]
        return ground * (1 - a) + frame[..., :3] * a
    return np.clip(ground + frame, 0.0, 1.0)


def _resize(img: np.ndarray, w: int, h: int) -> np.ndarray:
    if img.shape[1] == w and img.shape[0] == h:
        return img
    return np.asarray(Image.fromarray(img).resize((w, h), Image.Resampling.LANCZOS))


def display_frame(frame: np.ndarray, ground: np.ndarray, tile_x: bool, max_side: int = 256) -> np.ndarray:
    """uint8 view of one frame on a ground; tileable strips show two copies side by side."""
    img = composite(frame, ground)
    if tile_x:
        img = np.concatenate([img, img], axis=1)
        max_side = 2 * max_side if max_side else 0
    h, w = img.shape[:2]
    s = min(1.0, max_side / max(h, w)) if max_side else 1.0
    if tile_x:
        s = min(1.0, 1024 / w)
    dw, dh = max(2, int(round(w * s / 2)) * 2), max(2, int(round(h * s / 2)) * 2)
    return _resize(to_uint8(img), dw, dh)


def _font(size: int):
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # older Pillow
        return ImageFont.load_default()


def write_sheet(frames: np.ndarray, path: Path, title: str, lines: list[str], tile_x: bool,
                indices: list[int] | None = None) -> None:
    """Every frame over the dark ground, then every frame over the light ground."""
    views = {name: [display_frame(f, g, tile_x) for f in frames] for name, g in (("dark", DARK), ("light", LIGHT))}
    dh, dw = views["dark"][0].shape[:2]
    cols = max(1, min(len(frames), 2048 // dw))
    rows = -(-len(frames) // cols)
    gap, head = 4, 26 + 18 * len(lines)
    label_h = 20
    block_h = label_h + rows * (dh + gap)
    W = cols * (dw + gap) + gap
    H = head + 2 * block_h + gap
    sheet = Image.new("RGB", (W, H), (28, 28, 30))
    draw = ImageDraw.Draw(sheet)
    big, small = _font(18), _font(12)
    draw.text((gap + 2, 4), title, fill=(240, 240, 240), font=big)
    for j, line in enumerate(lines):
        colour = (255, 140, 120) if line.startswith("FLAG") else (200, 200, 200)
        draw.text((gap + 2, 26 + 18 * j), line, fill=colour, font=small)
    y = head
    for name in ("dark", "light"):
        draw.text((gap + 2, y + 3), f"{name} ground", fill=(180, 180, 180), font=small)
        y += label_h
        for i, v in enumerate(views[name]):
            r, k = divmod(i, cols)
            x0, y0 = gap + k * (dw + gap), y + r * (dh + gap)
            sheet.paste(Image.fromarray(v), (x0, y0))
            tag = f"{i}" if indices is None else f"{i}·{indices[i]}"
            ink = (230, 230, 230) if name == "dark" else (20, 20, 20)
            draw.text((x0 + 3, y0 + 2), tag, fill=ink, font=small)
        y += rows * (dh + gap)
    sheet.save(path, quality=88, subsampling=0)


def preview_frames(frames: np.ndarray, loop: bool, tile_x: bool, fps: float) -> np.ndarray:
    """Dark | light side by side; loops play three cycles, one-shots play twice with a short gap."""
    pairs = [np.concatenate([display_frame(f, DARK, tile_x), display_frame(f, LIGHT, tile_x)], axis=1)
             for f in frames]
    blank = np.concatenate([display_frame(np.zeros_like(frames[0]), DARK, tile_x),
                            display_frame(np.zeros_like(frames[0]), LIGHT, tile_x)], axis=1)
    if loop:
        seq = pairs * 3
    else:
        gap = [blank] * max(2, int(round(0.3 * fps)))
        seq = pairs + gap + pairs + gap
    return np.stack(seq)
