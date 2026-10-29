"""ffprobe / ffmpeg wrappers: probe a clip, decode frames to numpy, encode the preview."""
from __future__ import annotations

import json
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np


class MediaError(RuntimeError):
    pass


def _need(tool: str) -> str:
    path = shutil.which(tool)
    if path is None:
        raise MediaError(f"thiếu {tool} trong PATH")
    return path


def _rate(value: str | None) -> Fraction | None:
    if not value or value in ("0/0", "0"):
        return None
    try:
        r = Fraction(value)
    except (ValueError, ZeroDivisionError):
        return None
    return r if r > 0 else None


def probe(path: Path) -> dict:
    """Return width, height, fps, frame count, duration and colour tags of the first video stream."""
    out = subprocess.run(
        [_need("ffprobe"), "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,r_frame_rate,avg_frame_rate,nb_frames,codec_name,pix_fmt,"
         "color_range,color_space:format=duration",
         "-of", "json", str(path)],
        capture_output=True, text=True)
    if out.returncode != 0:
        raise MediaError(f"ffprobe lỗi với {path}: {out.stderr.strip()}")
    data = json.loads(out.stdout)
    if not data.get("streams"):
        raise MediaError(f"{path} không có luồng video")
    s = data["streams"][0]
    fps = _rate(s.get("avg_frame_rate")) or _rate(s.get("r_frame_rate")) or Fraction(24)
    nb = int(s.get("nb_frames") or 0)
    duration = float(data.get("format", {}).get("duration") or 0.0)
    if nb <= 0:
        cnt = subprocess.run(
            [_need("ffprobe"), "-v", "error", "-count_frames", "-select_streams", "v:0",
             "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(path)],
            capture_output=True, text=True)
        nb = int((cnt.stdout.strip() or "0").split(",")[0] or 0)
    return {
        "width": int(s["width"]), "height": int(s["height"]),
        "fps": float(fps), "fpsRational": f"{fps.numerator}/{fps.denominator}",
        "frames": nb, "duration": round(duration, 4),
        "codec": s.get("codec_name"), "pixFmt": s.get("pix_fmt"),
        "colorRange": s.get("color_range"), "colorSpace": s.get("color_space"),
    }


def _decode(path: Path | None, vf: str, w: int, h: int, source: list[str] | None = None) -> np.ndarray:
    src = source if source is not None else ["-i", str(path)]
    cmd = [_need("ffmpeg"), "-v", "error", "-nostdin", *src, "-an", "-sn",
           "-fps_mode", "passthrough", "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    out = subprocess.run(cmd, capture_output=True)
    if out.returncode != 0:
        raise MediaError(f"ffmpeg giải mã lỗi: {out.stderr.decode(errors='replace').strip()}")
    frame = w * h * 3
    n = len(out.stdout) // frame
    if n == 0:
        raise MediaError(f"ffmpeg không trả khung nào từ {path}")
    return np.frombuffer(out.stdout[: n * frame], np.uint8).reshape(n, h, w, 3)


def analysis_size(width: int, height: int, target: int = 480) -> tuple[int, int]:
    w = min(target, width)
    w -= w % 2
    h = max(2, int(round(height * w / width / 2.0)) * 2)
    return w, h


def decode_analysis(path: Path, width: int, height: int, target: int = 480, pre: str = "") -> np.ndarray:
    """All frames, area-downscaled to about `target` px wide, uint8 RGB. width/height are the
    frame size after the `pre` filters (rotate, hflip)."""
    w, h = analysis_size(width, height, target)
    pre = f"format=rgb24,{pre}," if pre else ""
    return _decode(path, f"{pre}scale={w}:{h}:flags=area,format=rgb24", w, h)


def rotate_filter(degrees: float, width: int, height: int, fill: str = "black") -> tuple[str, int, int]:
    """ffmpeg rotate (clockwise for positive degrees) onto a canvas that holds the whole frame.
    Returns (filter, new width, new height)."""
    a = np.radians(degrees)
    c, s = abs(np.cos(a)), abs(np.sin(a))
    ow = int(np.ceil((width * c + height * s) / 2)) * 2
    oh = int(np.ceil((width * s + height * c) / 2)) * 2
    return f"rotate={a:.6f}:ow={ow}:oh={oh}:c={fill}:bilinear=1", ow, oh


def _crop_chain(src_size: tuple[int, int], rect: tuple[int, int, int, int], out_w: int, out_h: int,
                pad_colour: str, pre: str) -> str:
    sw, sh = src_size
    x, y, w, h = (int(v) for v in rect)
    pl, pt = max(0, -x), max(0, -y)
    pr, pb = max(0, x + w - sw), max(0, y + h - sh)
    vf_pad = ""
    if pl or pt or pr or pb:
        vf_pad = f"pad=iw+{pl + pr}:ih+{pt + pb}:{pl}:{pt}:color={pad_colour},"
    pre = f"{pre}," if pre else ""
    return (f"format=rgb24,{pre}{vf_pad}crop={w}:{h}:{x + pl}:{y + pt},"
            f"scale={out_w}:{out_h}:flags=lanczos+accurate_rnd+full_chroma_int,format=rgb24")


def decode_crop(path: Path, src_size: tuple[int, int], rect: tuple[int, int, int, int],
                out_w: int, out_h: int, pad_colour: str = "black", pre: str = "") -> np.ndarray:
    """All frames cropped to rect=(x, y, w, h) in source pixels (the rect may leave the frame;
    the outside is padded with pad_colour) and lanczos-scaled to out_w x out_h, uint8 RGB.
    src_size is the frame size after the `pre` filters."""
    return _decode(path, _crop_chain(src_size, rect, out_w, out_h, pad_colour, pre), out_w, out_h)


def frame_mask(orig_size: tuple[int, int], src_size: tuple[int, int], rect: tuple[int, int, int, int],
               out_w: int, out_h: int, pre: str = "") -> np.ndarray:
    """Where the video frame itself lands in the cell (1 inside, 0 in padding or in the corners a
    rotation opens), by sending a white frame through the same filter chain. `pre` must fill
    with black."""
    w, h = orig_size
    src = ["-f", "lavfi", "-i", f"color=c=white:s={w}x{h}:d=1:r=1"]
    vf = _crop_chain(src_size, rect, out_w, out_h, "black", pre)
    return _decode(None, vf, out_w, out_h, source=src)[0, ..., 0].astype(np.float32) / 255.0


def encode_preview(frames: np.ndarray, fps: float, out: Path, out_fps: int = 24) -> None:
    """frames: (T, H, W, 3) uint8 with even H, W. h264, small, plays everywhere."""
    t, h, w, _ = frames.shape
    rate = Fraction(fps).limit_denominator(1000)
    cmd = [_need("ffmpeg"), "-v", "error", "-nostdin", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
           "-framerate", f"{rate.numerator}/{rate.denominator}", "-i", "-",
           "-r", str(out_fps), "-c:v", "libx264", "-preset", "medium", "-crf", "22",
           "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
    proc = subprocess.run(cmd, input=np.ascontiguousarray(frames).tobytes(), capture_output=True)
    if proc.returncode != 0:
        raise MediaError(f"ffmpeg mã hóa preview lỗi: {proc.stderr.decode(errors='replace').strip()}")
