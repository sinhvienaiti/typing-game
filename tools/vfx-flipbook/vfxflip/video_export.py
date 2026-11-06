"""Export manifest one-shots at source resolution using the lab-flipbooks recipe."""
from __future__ import annotations

import json
import math
import os
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

OUTPUT_FPS = 24


class VideoExportError(RuntimeError):
    pass


@dataclass(frozen=True)
class VideoCut:
    start: int
    end: int
    peak_time: float

    @property
    def frames(self) -> int:
        return self.end - self.start

    @property
    def duration(self) -> float:
        return round(self.frames / OUTPUT_FPS, 3)


def calculate_cut(entry: dict) -> VideoCut:
    """Source-frame cut, including the entire tail; peak is an atlas-cell index."""
    trim = entry["trim"]
    start, end = int(trim["start"]), int(trim["end"])
    step = float(trim["step"])
    fps = float(entry.get("sourceFps", OUTPUT_FPS))
    peak = float(entry["timing"]["peak"])
    if (start != trim["start"] or end != trim["end"] or start < 0 or end <= start
            or not all(math.isfinite(v) for v in (step, fps, peak))
            or step <= 0 or fps <= 0 or peak < 0):
        raise ValueError("trim hoặc timing không hợp lệ")
    return VideoCut(start, end, round(peak * step / fps, 3))


def calculate_pivot(entry: dict, metadata: dict) -> list[float]:
    """Map the atlas-cell pivot back onto the full, uncropped source frame."""
    source = metadata["source"]
    x, y, w, h = source["crop"]
    sw, sh = source["width"], source["height"]
    px, py = entry["pivot"]
    if sw <= 0 or sh <= 0 or w <= 0 or h <= 0:
        raise ValueError("kích thước nguồn hoặc crop không hợp lệ")
    pivot = [(px * w + x) / sw, (py * h + y) / sh]
    if not all(math.isfinite(v) for v in pivot):
        raise ValueError("pivot không hợp lệ")
    return [round(v, 4) for v in pivot]


def skip_reason(entry: dict, repo_root: Path, *, force: bool = False) -> str | None:
    if entry.get("loop") is True:
        return "loop: true"
    video = entry.get("video")
    changed_take = isinstance(video, dict) and "take" in video and video["take"] != entry.get("take")
    if "video" in entry and not force and not changed_take:
        return "đã có video cùng take (hoặc chưa ghi video.take)"
    if not isinstance(entry.get("trim"), dict):
        return "thiếu trim"
    if not isinstance(entry.get("timing"), dict):
        return "thiếu timing"
    source = entry.get("source")
    if not isinstance(source, str) or Path(source).suffix.lower() != ".mp4":
        return "source không phải file .mp4"
    if not (repo_root / source).is_file():
        return "không tìm thấy file source .mp4"
    return None


@dataclass(frozen=True)
class ExportPlan:
    cid: str
    source: Path
    output: Path
    cut: VideoCut
    pivot: list[float]
    take: object
    source_name: str


def _probe_video(path: Path) -> dict:
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,r_frame_rate,nb_read_frames,codec_name,pix_fmt",
         "-of", "json", str(path)], capture_output=True, text=True)
    if result.returncode:
        raise VideoExportError(f"ffprobe lỗi: {result.stderr.strip()}")
    try:
        stream = json.loads(result.stdout)["streams"][0]
        return {"w": int(stream["width"]), "h": int(stream["height"]),
                "fps": float(Fraction(stream["r_frame_rate"])), "frames": int(stream["nb_read_frames"]),
                "codec": stream["codec_name"], "pixFmt": stream["pix_fmt"]}
    except (KeyError, IndexError, ValueError, ZeroDivisionError) as exc:
        raise VideoExportError(f"ffprobe không đọc được video {path}") from exc


def _export_one(plan: ExportPlan) -> dict:
    temporary = plan.output.with_suffix(".tmp.mp4")
    try:
        result = subprocess.run(
            ["ffmpeg", "-v", "error", "-nostdin", "-y", "-i", str(plan.source),
             "-vf", f"select='between(n,{plan.cut.start},{plan.cut.end - 1})',setpts=N/(24*TB)",
             "-r", "24", "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
             "-pix_fmt", "yuv420p", "-threads", "4", "-movflags", "+faststart", str(temporary)],
            capture_output=True, text=True)
        if result.returncode:
            raise VideoExportError(f"ffmpeg lỗi: {result.stderr.strip()}")
        info = _probe_video(temporary)
        if (info["frames"] != plan.cut.frames or info["fps"] != OUTPUT_FPS
                or info["codec"] != "h264" or info["pixFmt"] != "yuv420p"):
            raise VideoExportError(f"video xuất không đúng số khung/24 fps/H.264/yuv420p: {info}")
        video = {"file": plan.output.name, **{k: info[k] for k in ("w", "h", "fps", "frames")},
                 "start": 0.0, "peakTime": plan.cut.peak_time, "pivot": plan.pivot,
                 "bytes": temporary.stat().st_size, "take": plan.take, "source": plan.source_name}
        os.replace(temporary, plan.output)
        return video
    finally:
        temporary.unlink(missing_ok=True)


def _write_manifest(path: Path, data: dict) -> None:
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def export_manifest(manifest: Path, *, repo_root: Path, ids: set[str] | None = None,
                    jobs: int = 3, force: bool = False, dry_run: bool = False) -> int:
    """Plan/export selected one-shots; only the calling thread updates the manifest."""
    if jobs < 1:
        raise VideoExportError("jobs phải lớn hơn 0")
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise VideoExportError(f"không đọc được manifest {manifest}: {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("flipbooks"), dict):
        raise VideoExportError("manifest phải có bảng flipbooks")
    entries = data["flipbooks"]
    plans = []
    for cid, entry in entries.items():
        if ids is not None and cid not in ids:
            continue
        if not isinstance(entry, dict):
            print(f"skip {cid}: mục không hợp lệ")
            continue
        reason = skip_reason(entry, repo_root, force=force)
        if reason:
            print(f"skip {cid}: {reason}")
            continue
        # Both files are siblings of the manifest, independent of the current directory.
        if Path(cid).name != cid or cid in (".", ".."):
            raise VideoExportError(f"id không hợp lệ: {cid}")
        try:
            cut = calculate_cut(entry)
            metadata = json.loads((manifest.parent / f"{cid}.json").read_text(encoding="utf-8"))
            pivot = calculate_pivot(entry, metadata)
        except (OSError, ValueError, KeyError, TypeError, OverflowError) as exc:
            raise VideoExportError(f"{cid}: không đọc được trim/timing/pivot hoặc <id>.json: {exc}") from exc
        plans.append(ExportPlan(cid, repo_root / entry["source"], manifest.parent / f"{cid}.mp4",
                                cut, pivot, entry.get("take"), entry["source"]))
        if dry_run:
            print(f"plan {cid}: START={cut.start} END={cut.end} "
                  f"duration={cut.duration:.3f}s peakTime={cut.peak_time:.3f}s")
    if dry_run:
        print(f"dry-run: {len(plans)} mục cần xuất")
        return len(plans)
    if not plans:
        print("export-video: 0 mục đã xuất")
        return 0
    errors = []
    exported = 0
    total_bytes = 0
    with ThreadPoolExecutor(max_workers=jobs) as executor:
        pending = {executor.submit(_export_one, plan): plan.cid for plan in plans}
        for future in as_completed(pending):
            cid = pending[future]
            try:
                video = future.result()
            except (OSError, VideoExportError) as exc:
                errors.append(f"{cid}: {exc}")
                continue
            entries[cid]["video"] = video
            exported += 1
            total_bytes += video["bytes"]
            print(f"export {cid}: {video['frames']} khung, {video['w']}×{video['h']}, {video['bytes']} byte")
    if exported:
        _write_manifest(manifest, data)
    print(f"export-video: {exported} mục đã xuất, {total_bytes} byte, {len(errors)} lỗi")
    if errors:
        raise VideoExportError("; ".join(errors))
    return exported
