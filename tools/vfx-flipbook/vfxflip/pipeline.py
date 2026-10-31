"""One clip in, one flipbook out: probe, analyse, cut, crop, grade, check, write."""
from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path

import numpy as np
from scipy import ndimage

from . import atlas, grade, layout, media, metrics, timing

TOOL_DIR = Path(__file__).resolve().parent.parent
TOOL_VERSION = 1
STRIP_OVERLAP = 0.15  # extra width cut for the horizontal-tiling crossfade
VERSION_RE = re.compile(r"^(?P<id>.+)__(?P<v>v\d+)\.mp4$")

DEFAULTS = {"loop": False, "blend": "additive", "background": "black", "cell": [256, 256],
            "frames": 32, "step": 1, "layout": "centre", "margin": 0.06, "greyCut": 0.15,
            "flash": True, "flashWindow": 1.5, "growthStart": 0.35, "maxSec": 2.5, "fadeFrac": 0.03,
            "tailFade": 0.3, "crossfade": 8, "startFrac": 0.05, "axis": None, "coreSide": None,
            "maxTilt": 8.0, "start": None, "end": None, "flipX": None, "rotate": None,
            "edgeFade": "auto", "stopAtEdge": None, "whiteFix": "warm",
            # "coverage": black-background clips get an alpha channel (the luma matte against black, opaque at
            # matteOpaque luma, widened matteWidenPx and maxed over +-matteTemporal frames); RGB stays as graded.
            "matte": None, "matteOpaque": 0.25, "matteWidenPx": 2.5, "matteTemporal": 1}


def lab_home() -> Path:
    return Path(os.environ.get("VFXLAB_HOME") or "~/VFXLab").expanduser()


def load_table(game: str, table_dir: Path = TOOL_DIR) -> dict:
    path = table_dir / f"{game}.json"
    if not path.is_file():
        return {"game": game, "defaults": {}, "clips": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def clip_params(table: dict, cid: str, version: str | None = None) -> dict:
    """defaults <- table defaults <- clip row <- the row's "versions": {"vN": {...}} override."""
    p = dict(DEFAULTS)
    p.update(table.get("defaults", {}))
    row = dict(table.get("clips", {}).get(cid, {}))
    per_version = row.pop("versions", {}) or {}
    p.update(row)
    if version and version in per_version:
        p.update(per_version[version])
    p["known"] = cid in table.get("clips", {})
    return p


def find_versions(inbox: Path, cid: str) -> list[tuple[str, Path]]:
    found = []
    for f in sorted((inbox / cid).glob(f"{cid}__v*.mp4")):
        m = VERSION_RE.match(f.name)
        if m and m.group("id") == cid:
            found.append((m.group("v"), f))
    found.sort(key=lambda vf: int(vf[0][1:]))
    return found


def read_note(mp4: Path) -> dict:
    """The clip's .txt (model, settings, prompt): kept as data, never run."""
    txt = mp4.with_suffix(".txt")
    if not txt.is_file():
        return {}
    text = txt.read_text(encoding="utf-8", errors="replace")
    out = {}
    for line in text.splitlines():
        if line.lower().startswith("source:"):
            out["source"] = line.split(":", 1)[1].strip()[:400]
        elif line.lower().startswith("prompt:"):
            out["prompt"] = line.split(":", 1)[1].strip()[:2000]
    return out


def _aspect_label(w: int, h: int) -> str:
    r = w / h
    for label, v in (("1:1", 1.0), ("16:9", 16 / 9), ("9:16", 9 / 16), ("4:3", 4 / 3), ("3:4", 3 / 4)):
        if abs(r - v) < 0.02:
            return label
    return f"{w}:{h}"


def _min_cut(err: np.ndarray, margin: int) -> np.ndarray:
    """Top-to-bottom path through err (H, O) with the least total error, moving at most one
    column per row and staying `margin` columns away from both sides (image-quilting seam)."""
    h, o = err.shape
    lo, hi = margin, max(margin + 1, o - margin)
    big = float(err.max()) * h + 1.0
    e = np.full_like(err, big)
    e[:, lo:hi] = err[:, lo:hi]
    cost = e.copy()
    back = np.zeros((h, o), np.int64)
    for y in range(1, h):
        prev = cost[y - 1]
        left = np.concatenate([[np.inf], prev[:-1]])
        right = np.concatenate([prev[1:], [np.inf]])
        stack = np.stack([left, prev, right])
        k = np.argmin(stack, axis=0)
        cost[y] = e[y] + stack[k, np.arange(o)]
        back[y] = np.arange(o) + k - 1
    path = np.zeros(h, np.int64)
    path[-1] = int(np.argmin(cost[-1]))
    for y in range(h - 1, 0, -1):
        path[y - 1] = back[y, path[y]]
    return path


def _strip_tile(frames: np.ndarray, out_w: int) -> np.ndarray:
    """frames are out_w + O wide. The O overhang columns (which continue the right edge) replace
    the strip's first columns up to a least-difference seam found over all frames, feathered by a
    few pixels, so the right edge runs into the left edge when the strip repeats and no wide
    double-exposed band appears."""
    o = frames.shape[2] - out_w
    out = frames[:, :, :out_w].copy()
    if o <= 0:
        return out
    over = frames[:, :, out_w:out_w + o]
    base = frames[:, :, :o]
    if o < 8:
        w = (np.arange(o) / max(1, o - 1)).astype(np.float32)[None, None, :, None]
        out[:, :, :o] = (1 - w) * over + w * base
        return out
    err = ((over - base) ** 2).sum(axis=(0, 3))
    feather = max(2, o // 12)
    path = _min_cut(err, feather + 1)
    xs = np.arange(o, dtype=np.float32)[None, :]
    keep_over = 1.0 - np.clip((xs - path[:, None] + feather) / (2.0 * feather), 0.0, 1.0)  # 1 = overhang
    keep_over[:, 0] = 1.0
    keep_over[:, -1] = 0.0
    m = keep_over[None, :, :, None].astype(np.float32)
    out[:, :, :o] = m * over + (1 - m) * base
    return out


def _quantised(frames: np.ndarray) -> np.ndarray:
    return np.round(np.clip(frames, 0.0, 1.0) * 255.0) / 255.0


def _fix_white_core(frames: np.ndarray, limit: float, mode: str = "warm") -> tuple[np.ndarray, dict | None]:
    """A white core wider than the limit (FIREFLY_VFX_LIST §4), fixed without clipping colour:
    "warm" (default) warms the core's outer part toward hot white-yellow, frame by frame, keeping
    the brightest channel; "peak" lowers the whole peak with a hue-preserving shoulder (the
    literal rule; it turns the core light grey); "off" only reports it."""
    before, at = metrics.white_core(_quantised(frames))
    if before <= limit or mode == "off":
        return frames, None
    if mode == "warm":
        target = limit - 0.02
        out = np.stack([grade.warm_core(f, target) for f in frames])
        return out, {"mode": "warm", "before": round(before, 3), "frame": at, "target": target}
    target = limit - 0.01

    def ratio(peak: float) -> float:
        return metrics.white_core(_quantised(grade.shoulder(frames, peak, knee_at=0.55)))[0]

    lo, hi = 0.82, 1.0
    if ratio(lo) > target:
        return grade.shoulder(frames, lo, knee_at=0.55), {"mode": "peak", "before": round(before, 3), "peak": lo,
                                                         "frame": at, "reached": False}
    for _ in range(12):
        mid = (lo + hi) / 2
        if ratio(mid) <= target:
            lo = mid
        else:
            hi = mid
    return grade.shoulder(frames, lo, knee_at=0.55), {"mode": "peak", "before": round(before, 3),
                                                     "peak": round(lo, 4), "frame": at, "reached": True}


class _Analysis:
    """Analysis-grid view of a clip (about 480 px wide), with any rotate/hflip pre-filters."""

    def __init__(self, mp4: Path, size: tuple[int, int], params: dict, pre: str = ""):
        self.size = size
        self.pre = pre
        an = media.decode_analysis(mp4, size[0], size[1], pre=pre)
        self.n = len(an)
        anf = grade.to_float(an)
        self.t0 = self.noise = None
        if params["background"] == "white":
            self.weight = grade.luma_matte(anf, grade.background_plate(grade.luma(anf)))[..., 3]
            self.hot = self.weight.reshape(self.n, -1).sum(1)
        else:
            self.t0, self.noise = grade.estimate_black_level(an)
            self.weight = grade.luma(grade.crush_black(anf, self.t0, grey_cut=params["greyCut"]))
            self.hot = np.where(self.weight > 0.5, self.weight, 0.0).reshape(self.n, -1).sum(1)
        self.energy = self.weight.reshape(self.n, -1).sum(1)


def _orient(mp4: Path, info: dict, params: dict, warnings: list[str], fill: str) -> tuple[_Analysis, dict]:
    """Directional clips: rotate a tilted axis to horizontal and mirror a clip that points the
    wrong way (table: axis "horizontal", coreSide "left" or "right"; per-version rotate/flipX
    override the automatic choice)."""
    size = (info["width"], info["height"])
    an = _Analysis(mp4, size, params)
    orient = {"rotate": 0.0, "flipX": False, "tiltMeasured": None}
    begin = timing.leading_black(an.energy)
    acc = an.weight[begin:].sum(0)
    if params["axis"] == "horizontal":
        ang, elong = layout.principal_axis(acc)
        orient["tiltMeasured"] = round(ang, 1)
        rot = params["rotate"]
        if rot is None and elong >= 1.4 and abs(ang) > float(params["maxTilt"]):
            rot = -ang
        if rot:
            flt, ow, oh = media.rotate_filter(float(rot), size[0], size[1], fill)
            an2 = _Analysis(mp4, (ow, oh), params, pre=flt)
            ang2, _ = layout.principal_axis(an2.weight[begin:].sum(0))
            if rot == -ang and abs(ang2) > abs(ang):  # wrong sense: turn the other way
                rot = ang
                flt, ow, oh = media.rotate_filter(float(rot), size[0], size[1], fill)
                an2 = _Analysis(mp4, (ow, oh), params, pre=flt)
                ang2, _ = layout.principal_axis(an2.weight[begin:].sum(0))
            an, size = an2, (ow, oh)
            orient["rotate"] = round(float(rot), 2)
            warnings.append(f"axis tilted {orient['tiltMeasured']:.0f} deg: rotated {rot:+.1f} deg "
                            f"(now {ang2:+.1f} deg)")
    flip = params["flipX"]
    if flip is None and params["coreSide"] in ("left", "right"):
        hot_acc = np.where(an.weight > 0.5, an.weight, 0.0)[begin:].sum(0)
        core = layout.centroid(hot_acc)
        mass = layout.centroid(an.weight[begin:].sum(0))
        if core and mass:
            side = "left" if core[0] < mass[0] else "right"
            flip = side != params["coreSide"]
            if flip:
                warnings.append(f"pointed the wrong way (hot core on the {side}): mirrored")
    if flip:
        pre = f"{an.pre},hflip" if an.pre else "hflip"
        an = _Analysis(mp4, size, params, pre=pre)
        orient["flipX"] = True
    mask_pre = []
    if orient["rotate"]:
        mask_pre.append(media.rotate_filter(orient["rotate"], info["width"], info["height"], "black")[0])
    if orient["flipX"]:
        mask_pre.append("hflip")
    orient["maskPre"] = ",".join(mask_pre)
    return an, orient


def _edge_fade(params: dict, orig: tuple[int, int], size: tuple[int, int], rect: tuple[int, int, int, int],
               out_w: int, ch: int, tile_x: bool) -> tuple[np.ndarray | None, list[str]]:
    """Soft fade where the video frame ends inside the cell (padding, rotated corners), so the
    frame edge never shows as a straight cut; plus a radial fade on request (edgeFade "radial")."""
    notes = []
    fade = np.ones((ch, out_w), np.float32)
    if params["edgeFade"] in ("auto", "radial"):
        mask = media.frame_mask(orig, size, rect, out_w, ch, pre=params.get("_maskPre", ""))
        if tile_x:
            mask = np.repeat(mask.min(axis=1, keepdims=True), out_w, axis=1)
        if float(mask.min()) < 0.98:
            dist = ndimage.distance_transform_edt(mask > 0.5)
            width = max(4.0, 0.08 * min(out_w, ch))
            fade *= grade.smoothstep(0.0, width, dist)
            notes.append(f"video frame edge inside the cell: faded over {width:.0f} px")
    if tile_x:
        yy = np.arange(ch, dtype=np.float32)[:, None] + 0.5
        band = max(3.0, 0.1 * ch)
        fade *= grade.smoothstep(0.0, band, yy) * grade.smoothstep(0.0, band, ch - yy)
        notes.append("strip: soft top/bottom fade")
    if params["edgeFade"] == "radial":
        yy, xx = np.mgrid[0:ch, 0:out_w].astype(np.float32)
        r = np.hypot((xx + 0.5) / out_w - 0.5, (yy + 0.5) / ch - 0.5) / 0.5
        fade *= 1.0 - grade.smoothstep(0.72, 1.0, r)
        notes.append("radial edge fade")
    return (None if float(fade.min()) > 0.999 else fade), notes


def process(mp4: Path, out_dir: Path, game: str, cid: str, version: str, params: dict) -> dict:
    info = media.probe(mp4)
    fps = info["fps"]
    note = read_note(mp4)
    warnings: list[str] = []
    if not params["known"]:
        warnings.append("id not in table: defaults used")
    if params.get("aspect") and params["aspect"] != _aspect_label(info["width"], info["height"]):
        warnings.append(f"aspect {_aspect_label(info['width'], info['height'])} (table says {params['aspect']})")

    additive = params["blend"] == "additive"
    white_bg = params["background"] == "white"
    fill = "white" if white_bg else "black"
    loop = bool(params["loop"])
    mode = params["layout"]
    cw, ch = (int(v) for v in params["cell"])
    tile_x = mode == "strip-x"
    out_w = int(round(cw * (1 + STRIP_OVERLAP))) if tile_x else cw

    # --- analysis pass (orientation fixed first) ---
    an, orient = _orient(mp4, info, params, warnings, fill)
    sw, sh = an.size
    n_src = an.n

    # --- timing ---
    if loop:
        plan = timing.plan_loop(an.energy, timing.block_mean(an.weight, 36, 64), fps,
                                frames=int(params["frames"]), step=int(params["step"]),
                                xfade=int(params["crossfade"]), force_start=params["start"])
        span = list(range(plan["start"], min(n_src, plan["end"] + plan["crossfade"] * int(plan["step"]))))
    else:
        stop = None
        if params["stopAtEdge"]:
            ring = 3
            wv = an.weight
            sides = {"top": wv[:, :ring], "bottom": wv[:, -ring:], "left": wv[:, :, :ring], "right": wv[:, :, -ring:]}
            stop = np.zeros(an.n, bool)
            for side in params["stopAtEdge"]:
                stop |= sides[side].reshape(an.n, -1).max(1) > 0.25
        plan = timing.plan_oneshot(an.energy, an.hot, fps, flash=bool(params["flash"]),
                                   max_sec=float(params["maxSec"]), fade_frac=float(params["fadeFrac"]),
                                   start_frac=float(params["startFrac"]), flash_window=float(params["flashWindow"]),
                                   growth_start=float(params["growthStart"]), n_max=int(params["frames"]),
                                   force_start=params["start"], force_end=params["end"], stop=stop)
        span = list(range(plan["start"], plan["end"]))
    idx = plan["indices"]

    # --- layout on the analysis grid ---
    weight = an.weight
    acc = weight[span].sum(0)
    maxmap = weight[span].max(0)
    c = layout.centroid(acc) or (weight.shape[2] / 2, weight.shape[1] / 2)
    box = layout.extent(acc, maxmap)
    edges = layout.touches_border(maxmap)
    if tile_x:
        edges = [e for e in edges if e not in ("left", "right")]
    if orient["rotate"]:
        edges = []  # the rotated canvas has new, empty borders; the source check ran before
    if edges:
        warnings.append("effect reaches the video frame edge: " + ",".join(edges))
    if white_bg:
        core = layout.centroid(weight[idx[0]]) or c
    elif loop:
        cores = [p for p in (layout.core_centroid(weight[i]) for i in idx[: plan["frames"]]) if p]
        core = (float(np.mean([p[0] for p in cores])), float(np.mean([p[1] for p in cores]))) if cores else c
    else:
        core = layout.core_centroid(weight[idx[0]]) or c
    aspect = out_w / ch
    squash = 1.0
    if mode == "left-pivot":
        rect = layout.crop_left(core, c, box, aspect, float(params["margin"]))
    elif tile_x:
        rect, squash, fits = layout.crop_strip(acc, c, box, aspect, float(params["margin"]))
        if squash > 1.0:
            warnings.append(f"band taller than the strip: squashed x{squash:.2f} vertically")
        if not fits:
            warnings.append("band still taller than the strip after squash: top/bottom cut")
    elif mode == "bbox":
        rect = layout.crop_bbox(box, aspect, float(params["margin"]))
    else:
        rect = layout.crop_centre(c, box, aspect, float(params["margin"]))
    sx, sy = sw / weight.shape[2], sh / weight.shape[1]
    src_rect = layout.to_source(rect, sx, sy, None if squash > 1.0 else aspect)
    pivot = [round((core[0] * sx - src_rect[0]) / src_rect[2], 4), round((core[1] * sy - src_rect[1]) / src_rect[3], 4)]
    if tile_x:
        pivot = [0.5, pivot[1]]
    scale = src_rect[2] / out_w
    if scale < 1.0:
        warnings.append(f"upscaled x{1 / scale:.2f} (effect smaller than the cell)")
    del weight

    # --- output pass: crop + lanczos at cell size, then grade ---
    cells = media.decode_crop(mp4, (sw, sh), src_rect, out_w, ch, fill, pre=an.pre)
    params = dict(params, _maskPre=orient["maskPre"])
    fade, fade_notes = _edge_fade(params, (info["width"], info["height"]), (sw, sh), src_rect, out_w, ch, tile_x)
    warnings += fade_notes

    def faded(img: np.ndarray) -> np.ndarray:
        if fade is None:
            return img
        if img.shape[-1] == 4:
            img = img.copy()
            img[..., 3] *= fade
            return img
        return img * fade[..., None]

    cache: dict[int, np.ndarray] = {}
    if white_bg:
        plate = grade.background_plate(grade.luma(grade.to_float(cells)), sigma=3.0)
        if float(np.median(plate)) < 0.85:
            warnings.append(f"background not white (plate median {float(np.median(plate)):.2f})")

        def graded(i: int) -> np.ndarray:
            if i not in cache:
                cache[i] = faded(grade.luma_matte(grade.to_float(cells[i]), plate))
            return cache[i]
    else:
        def graded(i: int) -> np.ndarray:
            if i not in cache:
                cache[i] = faded(grade.crush_black(grade.to_float(cells[i]), an.t0, grey_cut=params["greyCut"]))
            return cache[i]

        if not loop and plan.get("startMode") == "flash":
            hot_cells = np.array([metrics.hot_energy(graded(i)) for i in range(len(cells))])
            plan = timing.refine_start(plan, hot_cells, n_max=int(params["frames"]))
            idx = plan["indices"]

    def assemble(indices: list[int]) -> np.ndarray:
        f = np.stack([graded(i) for i in indices])
        if tile_x:
            f = _strip_tile(f[:, :, tile_shift:], cw)
        if loop:
            post = (lambda img, mix: grade.cool_dim(img, 0.8 * mix)) if additive else None
            f = timing.crossfade_loop(f, plan["frames"], plan["crossfade"], post)
        return f

    tile_shift = 0
    if tile_x:
        # where the strip wraps is free within the overlap: take the cut with the smallest jump
        probe_idx = idx[: plan["frames"]: max(1, plan["frames"] // 6)]
        sample = np.stack([graded(i) for i in probe_idx])
        o = out_w - cw
        shifts = range(0, max(1, o // 2))
        tile_shift = min(shifts, key=lambda k: metrics.tile_seam(_strip_tile(sample[:, :, k:], cw)))

    if loop and params["start"] is None and len(plan.get("candidates", [])) > 1:
        # final pick among the best windows on the real cells: evenness plus a clean join
        best = None
        for cand in plan["candidates"]:
            ci = timing.loop_indices(plan, cand["start"], len(cells))
            ratio = metrics.loop_seam(assemble(ci))[0]
            score = cand["score"] + 0.5 * max(0.0, ratio - 0.8) + (1.0 if ratio > 1.0 else 0.0)
            cand["cellSeam"] = round(ratio, 3)
            if best is None or score < best[0]:
                best = (score, cand["start"], ci)
        if best[1] != plan["start"]:
            plan = dict(plan, start=best[1], end=best[1] + plan["frames"] * int(plan["step"]), indices=best[2])
        idx = plan["indices"]
    frames = assemble(idx)
    del cells, cache
    tail_faded = 0
    if not loop and not plan["faded"]:
        tail_faded = max(2, int(math.ceil(float(params["tailFade"]) * len(frames))))
        j0 = len(frames) - tail_faded
        for j in range(j0, len(frames)):
            u = (j - j0 + 1) / tail_faded
            frames[j] = grade.cool_fade(frames[j], 1.0 - float(grade.smoothstep(0.0, 1.0, u)))
    peak_fix = None
    if additive:
        frames, peak_fix = _fix_white_core(frames, metrics.LIMITS["whiteCore"], str(params["whiteFix"]))
    frames = np.clip(frames, 0.0, 1.0)
    final = atlas.to_uint8(frames).astype(np.float32) / 255.0  # checks run on what the atlas holds
    coverage = None
    if params.get("matte") == "coverage" and not white_bg:
        cov = np.stack([grade.coverage_matte(f, opaque_at=float(params["matteOpaque"])) for f in final])
        cov = grade.widen_coverage(cov, float(params["matteWidenPx"]), int(params["matteTemporal"]))
        coverage = atlas.to_uint8(cov).astype(np.float32) / 255.0

    # --- checks ---
    flags: list[str] = []
    checks: dict = {}
    if not loop and additive and params["flash"]:
        fp = plan.get("flashPeak")
        flash_out = max((i for i, s in enumerate(idx) if fp is not None and s <= fp), default=0)
        ffp, ffg = metrics.first_frame_peak(final, flash_out)
        if plan.get("startMode") != "flash":
            ffp = ffg  # no flash peak to compare with: report against the whole flipbook
        checks["firstFramePeak"] = {"value": round(ffp, 3), "limit": metrics.LIMITS["firstFramePeak"],
                                    "vsWholeFlipbook": round(ffg, 3), "startMode": plan.get("startMode")}
        if plan.get("startMode") == "flash" and ffp < metrics.LIMITS["firstFramePeak"]:
            flags.append(f"first-frame {ffp:.2f}")
        elif plan.get("startMode") == "growth":
            grow = (plan["growthPeak"] - plan["droppedBlack"]) / fps
            warnings.append(f"no flash in the clip (the burst grows for {grow:.1f} s to its peak): started at "
                            f"{float(params['growthStart']):.0%} of that peak, first frame {ffg:.0%} of the "
                            f"flipbook peak; the flash must come from the game's flash layer")
    if additive:
        wc, wc_at = metrics.white_core(final)
        checks["whiteCore"] = {"value": round(wc, 3), "frame": wc_at, "limit": metrics.LIMITS["whiteCore"],
                               "peakFix": peak_fix}
        if wc > metrics.LIMITS["whiteCore"]:
            flags.append(f"white-core {wc:.2f}")
        if peak_fix and peak_fix["mode"] == "warm":
            warnings.append(f"white core {peak_fix['before']:.2f} of the radius: outer core warmed to "
                            f"<= {peak_fix['target']:.2f}")
        elif peak_fix:
            warnings.append(f"white core {peak_fix['before']:.2f} of the radius: peak lowered to "
                            f"{peak_fix['peak']:.3f}")
    res = metrics.black_residue(final)
    checks["blackResidue"] = {"value": round(res * 255, 2), "unit": "8-bit levels",
                              "limit": round(metrics.LIMITS["blackResidue"] * 255, 2),
                              "blackLevel": None if an.t0 is None else round(an.t0 * 255, 2),
                              "noise": None if an.noise is None else round(an.noise * 255, 2)}
    if res > metrics.LIMITS["blackResidue"]:
        flags.append(f"black-residue {res * 255:.1f}")
    em = metrics.edge_max(final, skip=("left", "right") if tile_x else ())
    checks["cellEdge"] = {"max": em, "limit": metrics.LIMITS["edge"]}
    cut = [k for k, v in em.items() if v > metrics.LIMITS["edge"]]
    if cut:
        flags.append("edge-cut " + ",".join(cut))
    if loop:
        ratio, seam, mean = metrics.loop_seam(final)
        checks["loopSeam"] = {"ratio": round(ratio, 3), "join": round(seam, 5), "meanNeighbour": round(mean, 5),
                              "limit": metrics.LIMITS["loopSeam"]}
        if ratio > metrics.LIMITS["loopSeam"]:
            flags.append(f"loop-seam {ratio:.2f}")
        en = np.array([metrics.energy(f) for f in final])
        checks["loopEnergyCV"] = round(float(en.std() / max(en.mean(), 1e-9)), 4)
    if tile_x:
        ts = metrics.tile_seam(final)
        checks["tileSeam"] = {"ratio": round(ts, 3), "limit": metrics.LIMITS["tileSeam"]}
        if ts > metrics.LIMITS["tileSeam"]:
            flags.append(f"tile-seam {ts:.2f}")
    if params["axis"] == "horizontal":
        ang, elong = layout.principal_axis(np.stack([metrics.visible(f) for f in final]).sum(0))
        checks["axis"] = {"degrees": round(ang, 1), "elongation": round(elong, 2), "limit": params["maxTilt"]}
        if elong >= 1.4 and abs(ang) > float(params["maxTilt"]):
            flags.append(f"axis {ang:+.0f} deg")
    ramp = []
    if additive:
        ramp, mworst, mbad = metrics.colour_ramp(final)
        checks["mustard"] = {"worst": round(mworst, 3), "frames": mbad, "limit": metrics.LIMITS["mustard"]}
        if mbad:
            flags.append(f"mustard x{len(mbad)}")
    if not loop and len(final) < 24:
        flags.append(f"few-frames {len(final)}")
    if not loop and plan.get("stoppedAtEdge"):
        warnings.append(f"cut ended at frame {plan['end']}, where the effect reaches the video frame edge")
    if not loop and plan.get("capped"):
        warnings.append(f"capped at maxSec {params['maxSec']} s")
    if tail_faded:
        warnings.append(f"no fade-out in the cut: cooling fade over the last {tail_faded} frames")

    if coverage is not None:
        raw = np.stack([grade.coverage_matte(f, opaque_at=float(params["matteOpaque"])) for f in final])
        checks["coverage"] = {"opaqueAt": float(params["matteOpaque"]), "widenPx": float(params["matteWidenPx"]),
                              "temporal": int(params["matteTemporal"]),
                              "meanAlpha": round(float(coverage.mean()), 4),
                              "grownShare": round(float((coverage > 0.02).sum() / max(1, (raw > 0.02).sum())), 3)}
        final = np.concatenate([final, coverage[..., None]], -1)

    # --- write ---
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{cid}__{version}"
    cols, rows = atlas.grid(len(final), cw, ch)
    aw, ah = atlas.write_atlas(final, cols, rows, out_dir / f"{stem}.atlas.png")
    if max(aw, ah) > 4096:
        warnings.append(f"atlas {aw}x{ah} is larger than 4096")
    fps_out = round(fps / float(plan["step"]), 3)
    meta = {
        "id": cid, "game": game, "version": version,
        "image": f"{stem}.atlas.png", "atlas": [aw, ah],
        "cols": cols, "rows": rows, "frames": len(final), "order": "row-major from the top-left cell",
        "fps": fps_out, "loop": loop, "blend": params["blend"],
        "channels": "rgba" if final.shape[-1] == 4 else "rgb", "premultiplied": False,
        "cell": [cw, ch], "pivot": pivot, "pivotOrigin": "top-left of the cell, 0..1",
        "tileX": tile_x,
        "source": {"file": mp4.name, "model": "Adobe Firefly Video", "note": note.get("source"),
                   "width": info["width"], "height": info["height"], "fps": fps, "frames": n_src,
                   "rotate": orient["rotate"], "flipX": orient["flipX"], "crop": list(src_rect),
                   "tileShift": tile_shift,
                   "squashY": round(squash, 3)},
        "trim": {"start": plan["start"], "end": plan["end"], "step": plan["step"], "indices": idx[: len(final)],
                 "startMode": plan.get("startMode"), "droppedBlack": plan["droppedBlack"],
                 "flashPeak": plan.get("flashPeak"), "crossfade": plan["crossfade"], "tailFade": tail_faded},
        "tool": f"tools/vfx-flipbook v{TOOL_VERSION}",
    }
    (out_dir / f"{stem}.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    status = "OK" if not flags else "FLAG " + "; ".join(flags)
    summary = (f"{cid} {version}: {len(final)}f {fps_out:g}fps cell {cw}x{ch} atlas {aw}x{ah} "
               f"src {plan['start']}-{plan['end']} step {plan['step']:g} ({plan.get('startMode')}) — {status}")
    report = {
        "id": cid, "version": version, "summary": summary, "flags": flags, "warnings": warnings,
        "frames": len(final), "fps": fps_out, "cell": [cw, ch], "loop": loop, "blend": params["blend"],
        "probe": info, "params": {k: v for k, v in params.items() if not k.startswith("_") and k != "known"},
        "orient": orient,
        "plan": {k: v for k, v in plan.items() if k != "indices"},
        "crop": {"rect": list(src_rect), "sourcePxPerCellPx": round(scale, 3), "pivot": pivot,
                 "squashY": round(squash, 3)},
        "checks": checks,
        "energy": [round(metrics.energy(f), 2) for f in final],
        "colourRamp": ramp,
        "prompt": note.get("prompt"),
    }
    (out_dir / f"{stem}.metrics.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                                                  encoding="utf-8")
    lines = [f"{len(final)} frames, {fps_out:g} fps, {'loop' if loop else 'one-shot'}, {params['blend']}, "
             f"cell {cw}x{ch}, src frames {plan['start']}-{plan['end']} step {plan['step']:g} "
             f"({plan.get('startMode')}), pivot {pivot}",
             status] + [f"note: {w}" for w in warnings]
    atlas.write_sheet(final, out_dir / f"{stem}.sheet.jpg", f"{cid} {version}", lines, tile_x, idx[: len(final)])
    media.encode_preview(atlas.preview_frames(final, loop, tile_x, fps_out), fps_out, out_dir / f"{stem}.preview.mp4")
    return report


def ingest(game: str, cid: str, version: str | None = None, home: Path | None = None,
           table_dir: Path = TOOL_DIR) -> list[dict]:
    home = home or lab_home()
    inbox = home / "inbox" / "firefly" / game
    table = load_table(game, table_dir)
    # A row with "from": another export of that id's clips under its own name (e.g. an RGBA re-cut).
    src = str(table.get("clips", {}).get(cid, {}).get("from") or cid)
    versions = find_versions(inbox, src)
    if version:
        versions = [vf for vf in versions if vf[0] == version]
    if not versions:
        raise FileNotFoundError(f"không thấy clip {inbox / src}/{src}__{version or 'vN'}.mp4")
    return [process(mp4, home / "out" / game / cid, game, cid, v, clip_params(table, cid, v))
            for v, mp4 in versions]


def ingest_all(game: str, home: Path | None = None, table_dir: Path = TOOL_DIR) -> tuple[list[dict], list[str]]:
    home = home or lab_home()
    inbox = home / "inbox" / "firefly" / game
    reports, errors = [], []
    if not inbox.is_dir():
        raise FileNotFoundError(f"không có thư mục {inbox}")
    for d in sorted(p for p in inbox.iterdir() if p.is_dir()):
        for v, _ in find_versions(inbox, d.name):
            try:
                reports += ingest(game, d.name, v, home, table_dir)
            except Exception as e:  # keep going: one bad clip must not stop the batch
                errors.append(f"{d.name} {v}: {type(e).__name__}: {e}")
    summary = {"game": game, "clips": [{"id": r["id"], "version": r["version"], "frames": r["frames"],
                                        "fps": r["fps"], "cell": r["cell"], "flags": r["flags"],
                                        "warnings": r["warnings"], "summary": r["summary"]} for r in reports],
               "errors": errors}
    out = home / "out" / game
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return reports, errors
