"""Repackage one existing lab entry, leaving its manifest and source media untouched."""
from __future__ import annotations

import copy
import hashlib
import json
import math
import shutil
from datetime import date
from pathlib import Path

from . import atlas, ktx2, media, motion, pipeline, video_export

COPY_FIELDS = ("role", "roles", "job", "take", "source", "mode", "alpha", "code", "design", "name", "elements",
               "use", "layer", "modesAllowed", "alphaKind", "premultiplied", "tint", "dir", "head")


def md5(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "md5").hexdigest()


def _choices(value: str, allowed: tuple[str, ...], label: str) -> list[str]:
    result = list(dict.fromkeys(s.strip() for s in value.split(",") if s.strip()))
    if any(s not in allowed for s in result):
        raise media.MediaError(f"{label} phải thuộc {', '.join(allowed)}")
    return result


def _compress(png: Path, stem: str, codecs: list[str], transfer: str,
              level: int, quality: int) -> dict:
    result = {}
    for codec in codecs:
        dest = png.parent / f"{stem}.{codec}.ktx2"
        print(f"KTX2 {dest.name} ({transfer})…", flush=True)
        info = ktx2.encode(png, dest, codec, transfer, uastc_level=level, etc1s_quality=quality)
        result[codec] = {"file": dest.name, "bytes": info["bytes"], "md5": md5(dest),
                         "encodeS": round(info["encodeMs"] / 1000, 3),
                         **({"level": level} if codec == "uastc" else {"quality": quality})}
    if result:
        result.update(yFlip=True, mipmaps=True, transfer=transfer)
    return result


def run(like: str, out: Path, cell: tuple[int, int] | list[int], fps: float, *, frames: int = 64,
        look: str | None = None, no_mv: bool = False, ktx2_codecs: str = "uastc,etc1s", videos: str = "",
        uastc_level: int = 2, etc1s_quality: int = 150, max_atlas: int = 4096,
        game: str = "immortality-cultivation", repo_root: Path | None = None,
        home: Path | None = None, table_dir: Path = pipeline.TOOL_DIR) -> dict:
    if not math.isfinite(fps) or not 6 <= fps <= 24 or (fps < 12 and no_mv):
        raise media.MediaError("fps phải từ 6 đến 24; fps dưới 12 bắt buộc có vector chuyển động (bỏ --no-mv)")
    if len(cell) != 2 or any(c < 16 or c > 1024 or int(c) != c or c % 4 for c in cell):
        raise media.MediaError("mỗi cạnh ô phải từ 16 đến 1024 và chia hết cho 4")
    if frames < 2:
        raise media.MediaError("frames phải từ 2 trở lên")
    if max_atlas < 1:
        raise media.MediaError("max-atlas phải lớn hơn 0")
    if look is not None and look not in ("cool", "neutral"):
        raise media.MediaError("look phải là cool hoặc neutral")
    if not 0 <= uastc_level <= 4 or not 1 <= etc1s_quality <= 255:
        raise media.MediaError("uastc-level phải từ 0 đến 4; etc1s-quality phải từ 1 đến 255")
    codecs = [] if ktx2_codecs == "none" else _choices(ktx2_codecs, ("uastc", "etc1s"), "ktx2")
    variants = _choices(videos, ("crf23", "720p"), "videos")
    try:
        manifest_name, cid = like.rsplit(":", 1)
    except ValueError as exc:
        raise media.MediaError("--like cần <manifest.json>:<id>") from exc
    if not cid or Path(cid).name != cid or cid in (".", ".."):
        raise media.MediaError("id không hợp lệ")
    repo_root = (repo_root or Path(__file__).resolve().parents[3]).resolve()
    manifest = repo_root / manifest_name
    try:
        original = json.loads(manifest.read_text(encoding="utf-8"))["flipbooks"][cid]
        job = original["job"]
        source = repo_root / original["source"]
    except (KeyError, TypeError, ValueError) as exc:
        raise media.MediaError(f"không đọc được mục like {like}: {exc}") from exc
    if Path(job).name != job or job in (".", ".."):
        raise media.MediaError("job không hợp lệ")
    folder = manifest.parent.name
    look = look or ("cool" if folder == "fire" else "neutral")
    params = pipeline.clip_params(pipeline.load_table(game, table_dir), job)
    params.update(cell=list(cell), frames=frames, fps=fps, look=look)
    work = (home or pipeline.lab_home()) / "out" / game / "upgrade" / cid
    report = pipeline.process(source, work, game, job, "v1", params)
    stem = f"{job}__v1"
    meta = json.loads((work / f"{stem}.json").read_text(encoding="utf-8"))
    cols, rows = atlas.grid(meta["frames"], *cell)
    width, height = cols * cell[0], rows * cell[1]
    if max(width, height) > max_atlas:
        raise media.MediaError(f"{meta['frames']} khung, lưới {cols}×{rows}, atlas {width}×{height} "
                               f"vượt --max-atlas {max_atlas}; chưa ghi file nào vào {out}")
    if variants and not meta["loop"] and not isinstance(original.get("video"), dict):
        raise media.MediaError("xuất videoVariants cần video.peakTime và video.pivot trong mục like")
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    upgrade = {"tool": "tools/vfx-flipbook upgrade", "cell": list(cell), "fps": fps,
               "look": look, "date": date.today().isoformat()}
    png, metadata_path = out / f"{cid}.atlas.png", out / f"{cid}.json"
    shutil.copyfile(work / f"{stem}.atlas.png", png)
    meta.update(id=cid, element=folder, role=original.get("role"), job=job, take=original.get("take"),
                image=png.name, upgrade=upgrade)
    video_export._write_manifest(metadata_path, meta)
    white = job.endswith("-white") or original.get("role") == "smoke"
    entry = {key: copy.deepcopy(original[key]) for key in COPY_FIELDS if key in original}
    entry.update(file=png.name, json=metadata_path.name,
                 **{key: meta[key] for key in ("cols", "rows", "frames", "fps", "loop", "blend", "cell", "pivot", "tileX")},
                 start=0, heading=0, width=width, height=height, md5=md5(png), bytes=png.stat().st_size,
                 sourceFps=meta["source"]["fps"],
                 trim={key: meta["trim"][key] for key in ("start", "end", "step", "startMode")},
                 flags=[f for f in report["flags"]
                        if not (f.startswith(("white-core", "mustard")) and folder != "fire")
                        and not (f.startswith("black-residue") and white)],
                 notes=report["warnings"],
                 checks={"whiteCore": (report["checks"].get("whiteCore") or {}).get("value"),
                         "blackResidue": (report["checks"].get("blackResidue") or {}).get("value"),
                         "loopSeam": (report["checks"].get("loopSeam") or {}).get("ratio"),
                         "tileSeam": (report["checks"].get("tileSeam") or {}).get("ratio")},
                 sourceRect={"crop": meta["source"]["crop"], "frame": [meta["source"]["width"], meta["source"]["height"]]},
                 compareWith={"folder": folder, "id": cid}, upgrade=upgrade)
    if "head" in entry and "uv" in entry["head"]:
        x, y, w, h = meta["source"]["crop"]
        sw, sh = entry["sourceRect"]["frame"]
        u, v = entry["head"]["uv"]
        entry["head"]["cellUv"] = [round((u * sw - x) / w, 4), round((v * sh - y) / h, 4)]
    if not meta["loop"]:
        energy = report["energy"]
        sm = [sum(energy[max(0, i - 1):i + 2]) / len(energy[max(0, i - 1):i + 2]) for i in range(len(energy))]
        peak = max(range(len(sm)), key=lambda i: sm[i])
        hold = max(i for i in range(len(sm)) if sm[i] >= 0.6 * sm[peak])
        entry["timing"] = {"peak": peak, "holdEnd": hold, "endsHot": bool(energy[-1] > 0.5 * sm[peak]),
                           "note": "peak: frame of peak energy (3-frame mean); holdEnd: last frame still at 60 % of it or more (the tail after it is the "
                                   "fade); endsHot: the last frame is still bright (the Firefly clip cuts to black without a fade), so the kit must erode or fade it"}
    if not no_mv:
        cells = motion.cells_from_atlas(png, cols, rows, *cell, meta["frames"])
        result = motion.flow(cells, meta["loop"])
        mv = out / f"{cid}.mv.png"
        motion.write_atlas(result["encoded"], cols, rows, mv)
        entry["motion"] = {"file": mv.name, "bytes": mv.stat().st_size, "md5": md5(mv),
                           "layout": "x-rgb-y-a", "zero": 128, "scale": 127, "strength": result["strength"],
                           "units": "cell UV per frame step, x right, y up",
                           "direction": "forward: frame n to n+1; one-shot last frame 0; loop last to first",
                           "method": "opencv DIS medium on sqrt luma, masked", "checks": result["checks"]}
        del cells, result
    if codecs:
        entry["ktx2"] = _compress(png, cid, codecs, "srgb", uastc_level, etc1s_quality)
        if not no_mv:
            entry["motion"]["ktx2"] = _compress(mv, f"{cid}.mv", codecs, "linear", uastc_level, etc1s_quality)
    if variants and meta["loop"]:
        print(f"note: {cid} là clip lặp; bỏ qua --videos")
    elif variants:
        cut = video_export.calculate_cut(original)
        entry["videoVariants"] = {}
        for name in variants:
            output = out / f"{cid}.{name}.mp4"
            video = original["video"]
            plan = video_export.ExportPlan(cid, source, output, cut, video["pivot"], original.get("take"), original["source"])
            crf = 23 if name == "crf23" else 20
            item = video_export._export_one(plan, crf=crf, height=720 if name == "720p" else None)
            item.pop("take", None)
            item.pop("source", None)
            item.update(peakTime=video["peakTime"], crf=crf,
                        ssim=video_export.variant_ssim(output, source, cut, meta["source"]["width"], meta["source"]["height"]))
            entry["videoVariants"][name] = item
    dest_manifest = out / "manifest.json"
    data = json.loads(dest_manifest.read_text(encoding="utf-8")) if dest_manifest.exists() else {
        "version": 1, "kind": "lab-hybrid", "note": "Phiếu 325/326: thử cách lai với ô lớn, vector chuyển động và KTX2.", "flipbooks": {}}
    data["flipbooks"][cid] = entry
    video_export._write_manifest(dest_manifest, data)
    print(report["summary"])
    for warning in report["warnings"]:
        print(f"    note: {warning}")
    print(f"upgrade {cid}: {dest_manifest}", flush=True)
    return entry
