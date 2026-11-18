"""Ticket 273: numeric straight-RGBA extraction and impact control masks."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys

import numpy as np
import PIL
from PIL import Image, ImageDraw, ImageFont
import scipy
from scipy import ndimage as ndi

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2"
REVIEW = ROOT.parent / "typing-game-review/captures/tu-tien/impact-k1-r2"
NAME = "fire-impact-k1-r2-v1a.a4"
OUT = ROOT / ".local/codex-runs/273-out"
CELL, BORDER, COLS, ROWS, FIRST, LAST = 384, 2, 6, 4, 53, 120
FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"


def md5(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def zero_border(a: np.ndarray) -> np.ndarray:
    a[:BORDER] = 0
    a[-BORDER:] = 0
    a[:, :BORDER] = 0
    a[:, -BORDER:] = 0
    return a


def border_nonzero(a: np.ndarray) -> int:
    mask = np.ones(a.shape[:2], bool)
    mask[BORDER:-BORDER, BORDER:-BORDER] = False
    return int(np.count_nonzero(a[mask]))


def cells(atlas: np.ndarray) -> list[np.ndarray]:
    return [atlas[(k // COLS) * CELL:(k // COLS + 1) * CELL,
                  (k % COLS) * CELL:(k % COLS + 1) * CELL].copy() for k in range(COLS * ROWS)]


def pack(frames: list[np.ndarray]) -> np.ndarray:
    out = np.zeros((ROWS * CELL, COLS * CELL, frames[0].shape[-1]), np.uint8)
    for k, frame in enumerate(frames):
        y, x = (k // COLS) * CELL, (k % COLS) * CELL
        out[y:y + CELL, x:x + CELL] = frame
    return out


def quantize(a: np.ndarray) -> np.ndarray:
    return np.rint(np.clip(a, 0, 1) * 255).astype(np.uint8)


def smoothstep(lo: float, hi: float, x: np.ndarray) -> np.ndarray:
    t = np.clip((x - lo) / (hi - lo), 0, 1)
    return t * t * (3 - 2 * t)


def straight_rgba(rgb: np.ndarray) -> tuple[np.ndarray, dict]:
    a = rgb.max(axis=-1).astype(np.float64) / 255
    color = np.divide(rgb / 255.0, a[..., None], out=np.zeros_like(rgb, dtype=float),
                      where=a[..., None] > 0)
    empty = a < 1 / 255
    if np.all(empty):
        raise ValueError("Ô hoàn toàn trống: không có màu để loang.")
    nearest = ndi.distance_transform_edt(empty, return_distances=False, return_indices=True)
    color[empty] = color[nearest[0][empty], nearest[1][empty]]
    rgba = zero_border(quantize(np.dstack((color, a))))
    reconstructed = np.rint(rgba[..., :3].astype(float) * rgba[..., 3:4] / 255).astype(int)
    delta = np.abs(reconstructed - rgb.astype(int))
    on = a >= 1 / 255
    return rgba, {"max_error_8bit": int(delta[on].max(initial=0)),
                  "pixels_over_1": int(np.count_nonzero(np.any(delta > 1, axis=-1) & on)),
                  "alpha_pixels": int(on.sum())}


def decode_alpha(video: Path, original: list[np.ndarray], magick: str) -> tuple[np.ndarray, dict]:
    # Match a4clip.py: decode at native size, then ImageMagick's sRGB Lanczos.
    probe = json.loads(subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
        "stream=width,height,nb_frames,r_frame_rate", "-of", "json", str(video)]))["streams"][0]
    if (probe["width"], probe["height"], probe["nb_frames"], probe["r_frame_rate"]) != (1080, 1080, "121", "24/1"):
        raise ValueError(f"Clip không khớp phiếu: {probe}")
    cmd = ["ffmpeg", "-v", "error", "-threads", "1", "-i", str(video), "-vf",
           f"select=between(n\\,{FIRST}\\,{LAST})", "-fps_mode", "passthrough",
           "-threads", "1", "-pix_fmt", "rgb24", "-f", "rawvideo", "pipe:1"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    alpha = []
    mismatches = []
    assert process.stdout is not None and process.stderr is not None
    try:
        for t in range(FIRST, LAST + 1):
            raw = process.stdout.read(1080 * 1080 * 3)
            if len(raw) != 1080 * 1080 * 3:
                raise ValueError(f"Thiếu dữ liệu khung f{t:03d}.")
            resized = subprocess.check_output([
                magick, "-size", "1080x1080", "-depth", "8", "rgb:-", "-colorspace", "sRGB",
                "-alpha", "off", "-filter", "Lanczos", "-resize", "384x384!", "-depth", "8", "rgb:-"], input=raw)
            rgb = zero_border(np.frombuffer(resized, np.uint8).reshape(CELL, CELL, 3).copy())
            if t < FIRST + COLS * ROWS:
                diff = np.abs(rgb.astype(int) - original[t - FIRST].astype(int))
                mismatches.append({"frame": t, "max_error_8bit": int(diff.max()),
                                   "different_pixels": int(np.any(diff != 0, axis=-1).sum())})
            alpha.append(rgb.max(axis=-1).astype(np.float32) / 255)
        if process.stdout.read(1):
            raise ValueError("Clip trả về nhiều hơn 68 khung.")
        stderr = process.stderr.read().decode()
        if process.wait() != 0:
            raise ValueError(f"ffmpeg: {stderr}")
    finally:
        if process.poll() is None:
            process.kill()
            process.wait()
        process.stdout.close()
        process.stderr.close()
    if any(r["max_error_8bit"] for r in mismatches):
        raise ValueError(f"Giải mã/đổi cỡ không khớp atlas: {mismatches}")
    return np.stack(alpha), {"probe": probe, "atlas_comparison": mismatches,
                             "decoded_frames": len(alpha), "resize": "ImageMagick sRGB Lanczos, 1080→384, no crop"}


def circle_center(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray | None:
    # Solve in coordinates relative to b to avoid cancellation.
    u, v = a - b, c - b
    m = 2 * np.stack((u, v))
    if abs(np.linalg.det(m)) < 1e-10:
        return None
    return b + np.linalg.solve(m, np.array([u @ u, v @ v]))


def geometry(strokes: dict) -> dict:
    yy, xx = np.mgrid[:CELL, :CELL]
    grid = np.stack((xx, yy), axis=-1).astype(float)
    distance2 = np.full((CELL, CELL), np.inf)
    progress = np.zeros((CELL, CELL))
    convex = np.zeros((CELL, CELL), bool)
    stroke_id = np.zeros((CELL, CELL), np.int16)
    lengths, endpoints, degenerate = [], [], []
    for sid, stroke in enumerate(strokes["strokes"]):
        pts = np.asarray(stroke["pts"], float) / 2.8125
        if not np.allclose(pts[0], np.array([331, 797]) / 2.8125):
            raise ValueError("Gốc nét không khớp (331, 797).")
        seglen = np.linalg.norm(np.diff(pts, axis=0), axis=-1)
        if np.any(seglen <= 0):
            raise ValueError("Đường tâm có đoạn dài 0.")
        s = np.r_[0, np.cumsum(seglen)]
        centers = []
        for j in range(len(pts)):
            i = min(max(j, 1), len(pts) - 2)
            center = circle_center(pts[i - 1], pts[i], pts[i + 1])
            if center is None:
                degenerate.append([sid, j])
            centers.append(center)
        for j, length in enumerate(seglen):
            d = pts[j + 1] - pts[j]
            t = np.clip(np.sum((grid - pts[j]) * d, axis=-1) / (length * length), 0, 1)
            q = pts[j] + t[..., None] * d
            d2 = np.sum((grid - q) ** 2, axis=-1)
            closer = d2 < distance2
            distance2[closer] = d2[closer]
            progress[closer] = ((s[j] + t * length) / s[-1])[closer]
            stroke_id[closer] = sid
            # Interpolate the local three-point circle centres along each segment.
            if centers[j] is None or centers[j + 1] is None:
                convex[closer] = False
            else:
                center = centers[j] + t[..., None] * (centers[j + 1] - centers[j])
                outer = np.sum((grid - q) * (q - center), axis=-1) > 0
                convex[closer] = outer[closer]
        lengths.append(float(s[-1]))
        endpoints.append({"root": pts[0].tolist(), "tip": pts[-1].tolist()})
    if degenerate:
        raise ValueError(f"Không có tâm đường tròn qua bộ ba thẳng hàng: {degenerate}")
    return {"distance": np.sqrt(distance2), "progress": progress, "convex": convex,
            "stroke_id": stroke_id, "lengths_px": lengths, "endpoints": endpoints}


def fixed_noise() -> np.ndarray:
    knots = np.random.default_rng(273).random((17, 17))
    yy, xx = np.mgrid[:CELL, :CELL] / 24
    return ndi.map_coordinates(knots, (yy, xx), order=1, mode="nearest", prefilter=False)


def life_from(alpha: np.ndarray, k: int) -> np.ndarray:
    # Count consecutive frames including the current frame; a currently dark pixel has life 0.
    alive = np.ones((CELL, CELL), bool)
    life = np.zeros((CELL, CELL), np.uint16)
    for at in alpha[k:]:
        alive &= at >= 0.08
        life += alive
    return life


def make_mask_a(alpha: np.ndarray, g: dict) -> tuple[list[np.ndarray], list[dict], dict]:
    hulls, coverages, rings = [], [], []
    for a in alpha[:24]:
        cov = smoothstep(0.03, 0.12, a)
        cov = zero_border(np.clip(ndi.gaussian_filter(ndi.maximum_filter(cov, size=5, mode="constant"),
                                                    sigma=1, mode="constant"), 0, 1))
        hull = cov > 0.5
        ring = zero_border(ndi.maximum_filter(hull, size=9, mode="constant") & ~hull)
        hulls.append(hull)
        coverages.append(cov)
        rings.append(ring)
    noise = fixed_noise()
    lower = max(float(np.quantile(noise[r], 0.22)) for r in rings)
    upper = min(float(np.quantile(noise[r], 0.28)) for r in rings)
    if lower > upper:
        raise ValueError(f"Không có một ngưỡng mực chung đạt 22–28%: [{lower}, {upper}].")
    threshold = float(np.clip(np.quantile(np.concatenate([noise[r] for r in rings]), 0.25), lower, upper))
    keep = noise >= threshold
    masks, rows = [], []
    for k, (a, cov, hull, ring) in enumerate(zip(alpha, coverages, hulls, rings)):
        lit = a > 0.1
        ink = ndi.gaussian_filter(ring.astype(float), sigma=0.8, mode="constant") * keep
        edt = ndi.distance_transform_edt(hull)
        band = hull & (edt <= 3) & g["convex"]
        candidates = np.flatnonzero(band)
        target = int(np.rint(0.04 * lit.sum()))
        if len(candidates) < target:
            raise ValueError(f"Ô {k}: dải lồi chỉ có {len(candidates)} px, cần {target} px cho vạch nóng 4%.")
        # Stable pixel order resolves equal-brightness ties without a new random sample.
        ranking = np.argsort(-a.ravel()[candidates], kind="stable")
        hot_seed = np.zeros((CELL, CELL), float)
        hot_seed.ravel()[candidates[ranking[:target]]] = 1
        hot = ndi.gaussian_filter(hot_seed, sigma=0.6, mode="constant")
        life = life_from(alpha, k)
        max_life = float(np.percentile(life[hull], 99))
        edt99 = float(np.percentile(edt[hull], 99))
        if max_life <= 0 or edt99 <= 0:
            raise ValueError(f"Ô {k}: không chuẩn hóa được life/độ dày.")
        survival = np.where(hull, 0.75 * np.clip(life / max_life, 0, 1) + 0.25 * edt / edt99, 0)
        m = zero_border(quantize(np.dstack((cov, ink, hot, survival))))
        masks.append(m)
        root = hull & (g["progress"] <= 0.2)
        tip = hull & (g["progress"] >= 0.8)
        if not root.any() or not tip.any():
            raise ValueError(f"Ô {k}: vùng gốc/mũi rỗng.")
        ma = m[..., 3] / 255
        edge = hull & ~ndi.binary_erosion(hull, border_value=0)
        gap = float((ring & ~keep).sum() / ring.sum())
        hot_ratio = float((m[..., 2].astype(float) / 255).sum() / lit.sum())
        row = {"cell": k, "source_frame": FIRST + k, "lit_area_px": int(lit.sum()),
               "hull_area_px": int(hull.sum()), "ink_ring_area_px": int(ring.sum()),
               "ink_effective_area_px": float((m[..., 1] / 255).sum()), "ink_gap_ratio": gap,
               "hot_band_candidates_px": int(len(candidates)), "hot_selected_px": target,
               "hot_effective_area_px": float((m[..., 2] / 255).sum()), "hot_to_lit_ratio": hot_ratio,
               "hot_nonzero_px": int((m[..., 2] > 0).sum()), "hot_over_half_px": int((m[..., 2] > 127).sum()),
               "life_p99_frames": max_life, "edt_p99_px": edt99,
               "root_area_px": int(root.sum()), "tip_area_px": int(tip.sum()),
               "survival_root_mean": float(ma[root].mean()), "survival_tip_mean": float(ma[tip].mean()),
               "edge_to_centerline_mean_px": float(g["distance"][edge].mean()),
               "hull_farther_than_40px": int((hull & (g["distance"] > 40)).sum()),
               "checks": {"hot": bool(0.035 <= hot_ratio <= 0.045), "ink": bool(0.22 <= gap <= 0.28),
                          "root_longer_than_tip": bool(ma[root].mean() > ma[tip].mean())}}
        rows.append(row)
    return masks, rows, {"noise_threshold": threshold, "feasible_threshold_interval": [lower, upper]}


def make_mask_b(masks: list[np.ndarray], g: dict) -> tuple[list[np.ndarray], dict]:
    # Claude's 21:03 amendment: one dilated union, one reveal map for all cells.
    union = ndi.maximum_filter(np.maximum.reduce([m[..., 0] for m in masks]) > 127,
                               size=5, mode="constant")
    zero_border(union)
    reveal = ndi.gaussian_filter(np.where(union, g["progress"], 1.0),
                                 sigma=1, mode="constant", cval=1)
    reveal[~union] = 1
    b = zero_border(quantize(np.dstack((reveal, np.zeros_like(reveal),
                                       np.zeros_like(reveal), np.ones_like(reveal)))))
    samples = []
    for sid, endpoints in enumerate(g["endpoints"]):
        for name, xy in endpoints.items():
            # Read the saved byte map at the actual fractional endpoint, bilinearly.
            value = float(ndi.map_coordinates(b[..., 0].astype(float) / 255,
                                             [[xy[1]], [xy[0]]], order=1, prefilter=False)[0])
            samples.append({"stroke": sid, "endpoint": name, "xy": xy, "value": value,
                            "pass": bool(value <= 0.05 if name == "root" else value >= 0.95)})
    return [b.copy() for _ in masks], {"union_area_px": int(union.sum()), "endpoints": samples,
                                      "endpoints_pass": all(s["pass"] for s in samples)}


def parameters() -> dict:
    return {
        "grid": [COLS, ROWS], "cell_px": CELL, "border_px": BORDER, "border_all_channels": 0,
        "source_frames": [FIRST, FIRST + COLS * ROWS - 1], "source_fps": 24,
        "rgba": {"color_space": "sRGB", "alpha": "straight", "alpha_formula": "max(r,g,b)",
                 "unpremultiply": "rgb/alpha in sRGB", "bleed_below_alpha": 1 / 255,
                 "bleed": "per-cell scipy.ndimage.distance_transform_edt(return_indices=True)",
                 "rounding": "numpy.rint; uint8, no premultiplication"},
        "mask_color_space": "linear / NoColorSpace", "mask_alpha": "straight data",
        "hull": {"smoothstep": [0.03, 0.12], "dilate_px": 2, "maximum_filter_size": 5,
                 "sigma_px": 1, "binary_threshold": 0.5},
        "ink": {"ring_dilate_px": 4, "maximum_filter_size": 9, "sigma_px": 0.8,
                "seed": 273, "rng": "numpy.random.default_rng / PCG64", "grid_spacing_px": 24,
                "grid_shape": [17, 17], "interpolation": "bilinear, scipy.map_coordinates(order=1)",
                "threshold": "single threshold for all 24 cells; pooled 25th percentile constrained to all per-cell 22–28% intervals",
                "gap_ratio_target": 0.25, "gap_ratio_range": [0.22, 0.28],
                "gap_measure": "zeroed pixels on the binary outer ring before Gaussian softening"},
        "hot": {"inside_edge_distance_px": [0, 3], "convex_test": "dot(p-q, q-local_circle_center)>0",
                "centerline_scale_divisor": 2.8125, "nearest_point": "exact projection on piecewise linear segments",
                "curvature": "circle through each consecutive vertex triple; interpolate centres along segment; endpoints use first/last triple",
                "rank": "descending source alpha, stable row-major ties", "target_lit_area_ratio": 0.04,
                "target_count_rounding": "numpy.rint", "sigma_px": 0.6,
                "area_measure": "sum of soft uint8 channel / 255; also records selected, nonzero, and >0.5 counts",
                "lit_threshold": 0.1, "gate": [0.035, 0.045]},
        "survival": {"decode_frames": [FIRST, LAST], "decode": "ffmpeg rgb24 native 1080x1080",
                     "resize": "ImageMagick sRGB, alpha off, Lanczos, resize 384x384!, no crop; matches a4clip.py",
                     "off_below_alpha": 0.08, "count": "current frame included, until first dark frame; never restart",
                     "maxLife_percentile": 99, "maxLife_region": "binary hull",
                     "life_normalization": "clamp(life/maxLife,0,1)", "life_weight": 0.75,
                     "edt_weight": 0.25, "edt_percentile": 99,
                     "edt_normalization": "edt/percentile99, then clamp final mask when quantizing",
                     "outside_hull": 0, "root_progress": [0, 0.2], "tip_progress": [0.8, 1]},
        "reveal_requested": {"distance": "arc length to nearest projected centerline point / own stroke length",
                             "farther_than_px": 40, "sigma_px": 1, "outside_hull": 1,
                             "same_B_R_in_all_cells": True, "B_G": 0, "B_B": 0, "B_A_interior": 255},
        "filters": {"mode": "constant", "cval": 0, "gaussian_truncate": 4,
                    "dilation_footprint": "square maximum_filter", "edge_measure": "binary hull minus 4-neighbour erosion"},
        "preview_requested": {"ticks": [0, 1, 3, 6, 9, 12, 18, 24, 30, 36, 42],
                              "loopMode": "none", "life_seconds": 43 / 60, "background_srgb": "#2a2c30",
                              "timingProfile": "impact-key1", "tint": [1, 1, 1], "soft": 1},
    }


def channel_sheet(rgba: list[np.ndarray], mask_a: list[np.ndarray], mask_b: list[np.ndarray] | None, out: Path) -> None:
    chosen = [0, 4, 8, 12, 16, 20]
    labels = ["RGBA", "A.R hull", "A.G ink", "A.B hot", "A.A survival", "B.R reveal"]
    w, h, label_w, label_h = 256, 256, 130, 28
    sheet = Image.new("RGB", (label_w + len(chosen) * w, label_h + len(labels) * h), "#16171a")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.truetype(FONT, 18)
    for col, k in enumerate(chosen):
        draw.text((label_w + col * w + 10, 4), f"k{k:02d} / f{FIRST + k:03d}", font=font, fill="white")
        for row, label in enumerate(labels):
            if row == 0:
                src = Image.fromarray(rgba[k])
                tile = Image.new("RGBA", src.size, "#2a2c30")
                tile.alpha_composite(src)
                tile = tile.convert("RGB")
            elif row <= 4:
                tile = Image.fromarray(mask_a[k][..., row - 1]).convert("RGB")
            elif mask_b is not None:
                tile = Image.fromarray(mask_b[k][..., 0]).convert("RGB")
            else:
                tile = Image.new("RGB", (CELL, CELL), "#2a2c30")
                ImageDraw.Draw(tile).text((20, 170), "NOT GENERATED", font=font, fill="white")
            sheet.paste(tile.resize((w, h), Image.Resampling.LANCZOS), (label_w + col * w, label_h + row * h))
    for row, label in enumerate(labels):
        draw.text((8, label_h + row * h + 12), label, font=font, fill="white")
    sheet.save(out)


def verify_preserved(result: dict, original: list[np.ndarray], rgba: list[np.ndarray],
                     masks: list[np.ndarray], g: dict) -> dict:
    excess, max_error = 0, 0
    rows = []
    noise = fixed_noise()
    keep = noise >= result["noise"]["noise_threshold"]
    for k, (rgb, color, mask) in enumerate(zip(original, rgba, masks)):
        alpha = rgb.max(axis=-1)
        if not np.array_equal(color[..., 3], alpha):
            raise ValueError(f"Ô {k}: alpha RGBA không bằng max RGB nguồn.")
        delta = np.abs(np.rint(color[..., :3].astype(float) * color[..., 3:4] / 255) - rgb)
        on = alpha > 0
        excess += int((np.any(delta > 1, axis=-1) & on).sum())
        max_error = max(max_error, int(delta[on].max(initial=0)))
        hull = mask[..., 0] > 127
        ring = zero_border(ndi.maximum_filter(hull, size=9, mode="constant") & ~hull)
        root, tip = hull & (g["progress"] <= 0.2), hull & (g["progress"] >= 0.8)
        ma = mask[..., 3] / 255
        edge = hull & ~ndi.binary_erosion(hull, border_value=0)
        row = {"cell": k, "lit_area_px": int((alpha / 255 > 0.1).sum()),
               "hull_area_px": int(hull.sum()), "ink_gap_ratio": float((ring & ~keep).sum() / ring.sum()),
               "ink_effective_area_px": float((mask[..., 1] / 255).sum()),
               "hot_to_lit_ratio": float((mask[..., 2] / 255).sum() / (alpha / 255 > 0.1).sum()),
               "survival_root_mean": float(ma[root].mean()), "survival_tip_mean": float(ma[tip].mean()),
               "edge_to_centerline_mean_px": float(g["distance"][edge].mean())}
        saved = result["cells"][k]
        if any(not np.isclose(v, saved[key], rtol=0, atol=1e-12) for key, v in row.items()):
            raise ValueError(f"Ô {k}: số đo đọc lại không khớp hồ sơ maskA đã đạt.")
        row["pass"] = bool(0.035 <= row["hot_to_lit_ratio"] <= 0.045 and
                           0.22 <= row["ink_gap_ratio"] <= 0.28 and
                           row["survival_root_mean"] > row["survival_tip_mean"])
        rows.append(row)
    print(f"Reconstruction pixels over 1: {excess}; max error: {max_error}", flush=True)
    print(" k  lit_px hull_px ink_gap% hot/lit% A.A_root A.A_tip edge_dist  result", flush=True)
    for r in rows:
        print(f"{r['cell']:2d} {r['lit_area_px']:7d} {r['hull_area_px']:7d} "
              f"{100*r['ink_gap_ratio']:8.3f} {100*r['hot_to_lit_ratio']:8.3f} "
              f"{r['survival_root_mean']:8.4f} {r['survival_tip_mean']:7.4f} "
              f"{r['edge_to_centerline_mean_px']:9.3f} " + ("PASS" if r["pass"] else "FAIL"), flush=True)
    if excess or not all(r["pass"] for r in rows):
        raise ValueError("Kiểm 1–2 đọc lại không đạt; giữ nguyên RGBA/maskA và dừng.")
    return {"reconstruction_pixels_over_1": excess, "reconstruction_max_error_8bit": max_error,
            "A_checks_24_cells": True, "reread_cells": rows}


def rank_survival(alpha: np.ndarray, masks: list[np.ndarray], g: dict) -> tuple[list[np.ndarray], list[dict]]:
    ranked, rows = [], []
    for k, mask in enumerate(masks):
        cov = mask[..., 0].astype(float) / 255
        hull = cov > 0.5
        n = int(hull.sum())
        if n < 2:
            raise ValueError(f"Ô {k}: cần ít nhất hai điểm trong vỏ để xếp hạng.")
        life = life_from(alpha, k)
        edt = ndi.distance_transform_edt(hull)
        life99, edt99 = np.percentile(life[hull], 99), np.percentile(edt[hull], 99)
        if life99 <= 0 or edt99 <= 0:
            raise ValueError(f"Ô {k}: không chuẩn hóa được life/EDT.")
        score = 0.75 * np.clip(life[hull] / life99, 0, 1) + 0.25 * edt[hull] / edt99
        # Zero-based average ranks retain exact ties in the unquantized score.
        _, inverse, counts = np.unique(score, return_inverse=True, return_counts=True)
        starts = np.cumsum(counts) - counts
        ranks = (starts + (counts - 1) / 2)[inverse]
        survival = np.zeros_like(cov)
        survival[hull] = 0.02 + 0.98 * ranks / (n - 1)
        nearest = ndi.distance_transform_edt(~hull, return_distances=False, return_indices=True)
        soft = (cov > 0) & ~hull
        survival[soft] = survival[nearest[0][soft], nearest[1][soft]] * cov[soft] / 0.5
        survival = zero_border(ndi.gaussian_filter(survival, sigma=0.6, mode="constant"))
        updated = mask.copy()
        updated[..., 3] = quantize(survival)
        root, tip = hull & (g["progress"] <= 0.2), hull & (g["progress"] >= 0.8)
        if not root.any() or not tip.any():
            raise ValueError(f"Ô {k}: vùng gốc/mũi rỗng.")
        ma = updated[..., 3] / 255
        row = {"cell": k, "hull_area_px": n, "score_unique_values": int(len(counts)),
               "tied_pixels": int(counts[counts > 1].sum()),
               "survival_root_mean": float(ma[root].mean()), "survival_tip_mean": float(ma[tip].mean()),
               "root_longer_than_tip": bool(ma[root].mean() > ma[tip].mean()),
               "rgb_identical": bool(np.array_equal(mask[..., :3], updated[..., :3]))}
        print(f"k{k:02d} A.A root={row['survival_root_mean']:.6f} tip={row['survival_tip_mean']:.6f} "
              f"RGB={'PASS' if row['rgb_identical'] else 'FAIL'} "
              f"root>tip={'PASS' if row['root_longer_than_tip'] else 'FAIL'}", flush=True)
        ranked.append(updated)
        rows.append(row)
    if not all(r["root_longer_than_tip"] and r["rgb_identical"] for r in rows):
        raise ValueError("A.A theo hạng không đạt kiểm RGB/gốc > mũi; chưa ghi art-src.")
    return ranked, rows


def update_survival_rank(meta: Path) -> int:
    apath = ART / f"{NAME}.maskA.png"
    backup_a = ART / f"{NAME}.maskA.v1.png"
    backup_meta = ART / f"{NAME}.masks.v1.json"
    if backup_a.exists() != backup_meta.exists():
        raise ValueError("Cặp bản sao v1 không đầy đủ; dừng để giữ nguyên dữ liệu.")
    result = json.loads(meta.read_text())
    baseline = json.loads((backup_meta if backup_meta.exists() else meta).read_text())
    baseline_a = backup_a if backup_a.exists() else apath
    if md5(baseline_a) != baseline["outputs"]["maskA"]["md5"]:
        raise ValueError("maskA v1 không khớp hồ sơ v1.")
    for name, entry in result["sources"].items():
        if name != "builder" and md5(Path(entry["path"])) != entry["md5"]:
            raise ValueError(f"Nguồn đã đổi: {name}")
    for name, entry in result["outputs"].items():
        if md5(Path(entry["path"])) != entry["md5"]:
            raise ValueError(f"Đầu ra không khớp hồ sơ: {name}")
    preserved = {name: {"md5": md5(Path(result["outputs"][name]["path"])),
                        "mtime_ns": Path(result["outputs"][name]["path"]).stat().st_mtime_ns}
                 for name in ("rgba", "maskB")}

    def read(path: Path, mode: str = "RGBA") -> list[np.ndarray]:
        with Image.open(path) as im:
            if im.size != (COLS * CELL, ROWS * CELL) or im.mode != mode:
                raise ValueError(f"Sai kích thước/kênh: {path}")
            return cells(np.asarray(im))

    original = read(Path(result["sources"]["atlas"]["path"]), "RGB")
    rgba = read(Path(result["outputs"]["rgba"]["path"]))
    old_masks = read(baseline_a)
    g = geometry(json.loads(Path(result["sources"]["strokes"]["path"]).read_text()))
    verify_preserved(baseline, original, rgba, old_masks, g)
    if not np.array_equal(pack(read(apath))[..., :3], pack(old_masks)[..., :3]):
        raise ValueError("RGB maskA hiện tại khác v1; dừng.")
    alpha, decode_check = decode_alpha(Path(result["sources"]["video"]["path"]), original,
                                       os.environ.get("ART_MAGICK", "/opt/homebrew/bin/magick"))
    masks, rows = rank_survival(alpha, old_masks, g)
    if any(border_nonzero(m) for m in masks):
        raise ValueError("Viền maskA khác 0.")
    # Back up both originals before the first authorized overwrite; never replace v1.
    if not backup_a.exists():
        shutil.copy2(apath, backup_a)
        shutil.copy2(meta, backup_meta)
    Image.fromarray(pack(masks)).save(apath)
    saved = read(apath)
    if not np.array_equal(pack(saved), pack(masks)) or not np.array_equal(pack(saved)[..., :3], pack(old_masks)[..., :3]):
        raise ValueError("PNG đọc lại không khớp byte đã tính hoặc RGB v1.")
    for name, before in preserved.items():
        path = Path(result["outputs"][name]["path"])
        if before != {"md5": md5(path), "mtime_ns": path.stat().st_mtime_ns}:
            raise ValueError(f"{name} đã đổi trong lúc chạy.")
    for row in rows:
        saved_row = result["cells"][row["cell"]]
        for key in ("survival_root_mean", "survival_tip_mean"):
            saved_row[key] = row[key]
        saved_row["checks"]["root_longer_than_tip"] = row["root_longer_than_tip"]
    result["parameters"]["survival"].update({
        "score": "0.75*clamp(life/p99,0,1)+0.25*edt/edt_p99; before quantization",
        "rank_region": "saved A.R > 0.5", "rank": "zero-based average ranks for exact ties",
        "rank_formula": "0.02+0.98*rank(score)/(N-1)",
        "soft_edge": "0<A.R<=0.5: nearest binary hull survival * A.R/0.5",
        "outside_support_before_blur": 0, "sigma_px": 0.6,
        "outside_hull": "nearest-hull extension on soft A.R, then Gaussian; 2px border zero"})
    verification = {"decision": "Claude 2026-11-04 21:15; ticket 273b",
                    "RGB_identical_v1": True, "root_longer_than_tip_24_cells": True,
                    "border_nonzero_values": [border_nonzero(m) for m in saved], "cells": rows,
                    "decode": decode_check, "preserved": preserved,
                    "backups": {"maskA": {"path": str(backup_a), "md5": md5(backup_a)},
                                "metadata": {"path": str(backup_meta), "md5": md5(backup_meta)}},
                    "builder": {"path": str(Path(__file__).resolve()), "md5": md5(Path(__file__))},
                    "versions": {"python": platform.python_version(), "numpy": np.__version__,
                                 "scipy": scipy.__version__, "pillow": PIL.__version__}}
    result["survival_rank"] = verification
    result["outputs"]["maskA"]["md5"] = md5(apath)
    result["checks"].pop("preserved_RGBA_maskA", None)
    result["checks"].pop("preview_tick42_less_than_2pct_tick9", None)
    result["checks"].pop("preview_area", None)
    result["checks"].update({"maskA_RGB_identical_v1": True, "root_longer_than_tip_24_cells": True,
                              "preserved_RGBA_maskB": True})
    result.pop("preview", None)
    result["status"] = "ranked_masks_complete_awaiting_CPU_preview"
    channel_sheet(rgba, saved, read(Path(result["outputs"]["maskB"]["path"])), OUT / "channels-k00-k23.png")
    write_json(OUT / "273b-survival-rank-verification.json", verification)
    write_json(OUT / "measurements.json", result)
    write_json(meta, result)
    print("273b: RGB identical to v1; root > tip 24/24; RGBA/maskB unchanged; PASS", flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true",
                        help="Cho ghi đè masks.json và 273-out; cùng --survival-rank cho đổi riêng A.A maskA.")
    parser.add_argument("--survival-rank", action="store_true",
                        help="Phiếu 273b: sao lưu v1 rồi xếp hạng A.A, giữ nguyên RGB; không tạo lại RGBA/maskB.")
    args = parser.parse_args()
    meta = ART / f"{NAME}.masks.json"
    if not args.force:
        parser.error("Lượt tiếp tục cần --force cho masks.json và 273-out; RGBA/maskA luôn chỉ đọc.")
    if args.survival_rank:
        return update_survival_rank(meta)
    # The approved retry resumes from the exact completed section 1–2 metadata.
    result = json.loads(meta.read_text())
    retained_keys = ("cells", "noise", "reconstruction", "decode", "geometry")
    retained = json.dumps({k: result[k] for k in retained_keys}, sort_keys=True)
    source_checks = {}
    for name, entry in result["sources"].items():
        if name == "builder":  # Historical hash of the first run's tool.
            continue
        source_checks[name] = md5(Path(entry["path"])) == entry["md5"]
    if not all(source_checks.values()):
        raise ValueError(f"Nguồn đã thay đổi: {source_checks}")
    preserved = {name: {"md5": md5(Path(result["outputs"][name]["path"])),
                        "mtime_ns": Path(result["outputs"][name]["path"]).stat().st_mtime_ns}
                 for name in ("rgba", "maskA")}
    if any(preserved[n]["md5"] != result["outputs"][n]["md5"] for n in preserved):
        raise ValueError("RGBA/maskA khác MD5 của lần chạy đã đạt; dừng.")
    def read_atlas(path: Path, mode: str) -> list[np.ndarray]:
        with Image.open(path) as im:
            if im.size != (COLS * CELL, ROWS * CELL) or im.mode != mode:
                raise ValueError(f"Sai kích thước/kênh: {path}")
            return cells(np.asarray(im))
    original = read_atlas(Path(result["sources"]["atlas"]["path"]), "RGB")
    rgba = read_atlas(Path(result["outputs"]["rgba"]["path"]), "RGBA")
    masks = read_atlas(Path(result["outputs"]["maskA"]["path"]), "RGBA")
    g = geometry(json.loads(Path(result["sources"]["strokes"]["path"]).read_text()))
    verification = verify_preserved(result, original, rgba, masks, g)
    mask_b, reveal_check = make_mask_b(masks, g)
    print("B.R shared-map endpoints:", json.dumps(reveal_check, ensure_ascii=False), flush=True)
    if not reveal_check["endpoints_pass"]:
        raise ValueError("Kiểm 3 không đạt; dừng, không đổi đường tâm hoặc công thức.")
    borders = {name: [border_nonzero(c) for c in frames]
               for name, frames in (("source_atlas", original), ("rgba", rgba), ("maskA", masks), ("maskB", mask_b))}
    if any(any(v) for v in borders.values()):
        raise ValueError(f"Kiểm 4 không đạt: {borders}")
    bpath = ART / f"{NAME}.maskB.png"
    packed_b = pack(mask_b)
    if bpath.exists():
        if not np.array_equal(pack(read_atlas(bpath, "RGBA")), packed_b):
            raise ValueError("maskB đã có và khác kết quả; --force không cho ghi đè PNG art-src.")
    else:
        Image.fromarray(packed_b).save(bpath)
    channel_sheet(rgba, masks, mask_b, OUT / "channels-k00-k23.png")
    verification.update({"border_nonzero_values": borders, "source_md5_unchanged": source_checks,
                         "reveal": reveal_check, "B_R_identical_24_cells": all(np.array_equal(b, mask_b[0]) for b in mask_b),
                         "preserved": preserved})
    for name, before in preserved.items():
        path = Path(result["outputs"][name]["path"])
        if before != {"md5": md5(path), "mtime_ns": path.stat().st_mtime_ns}:
            raise ValueError(f"{name} đã bị đổi trong lúc chạy; dừng.")
    if retained != json.dumps({k: result[k] for k in retained_keys}, sort_keys=True):
        raise ValueError("Hồ sơ mục 1–2 bị thay đổi; dừng.")
    result["continuation"] = {
        "decision": "Claude 2026-11-04 21:03: U=dilate(max_k(A.R_k)>0.5,2px); one shared B.R",
        "preserved_outputs": preserved, "preserved_maskA_metadata": True,
        "builder": {"path": str(Path(__file__).resolve()), "md5": md5(Path(__file__))},
        "versions": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": scipy.__version__, "pillow": PIL.__version__}}
    result["parameters"]["reveal_requested"] = {
        "distance": "arc length to nearest projected centerline point / own stroke length",
        "farther_than_px": 40, "farther_than_rule": "same nearest stroke projection, no cutoff",
        "support": "U=dilate(max_k(A.R_k)>0.5,2px), square maximum_filter 5x5",
        "sigma_px": 1, "blur_input_outside_U": 1, "blur_cval": 1, "outside_U": 1,
        "same_B_R_in_all_cells": True, "B_G": 0, "B_B": 0, "B_A_interior": 255,
        "border_all_channels": 0, "endpoint_sampling": "bilinear at scaled fractional endpoint on quantized PNG"}
    result["outputs"]["maskB"] = {"path": str(bpath), "md5": md5(bpath)}
    result["checks"].update({"reconstruction_pixels_over_1": verification["reconstruction_pixels_over_1"],
                              "border_nonzero_values": borders, "reveal": reveal_check,
                              "B_R_identical_24_cells": True, "preserved_RGBA_maskA": True,
                              "source_md5_unchanged": True})
    for key in ("stopped_at", "reason", "reveal_constraint_check"):
        result.pop(key, None)
    result["status"] = "masks_complete_awaiting_CPU_preview"
    write_json(OUT / "verification.json", verification)
    write_json(OUT / "measurements.json", result)
    write_json(meta, result)
    print("Borders: all four PNGs / 24 cells / all channels = 0; RGBA/maskA unchanged.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
