#!/usr/bin/env python3
"""Hậu kỳ PNG bằng ImageMagick 7; xử lý pixel bằng thư viện chuẩn Python."""
import argparse
import functools
import copy
import inspect
import signal
from array import array
from collections import deque
import json
import math
import os
from pathlib import Path
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import threading
import struct
import zlib
import seam_analysis as sa

MAGICK = os.environ.get("ART_MAGICK", shutil.which("magick") or str(Path.home() / ".local/bin/magick"))
ROOT = Path(__file__).resolve().parent
WORK = ROOT / ".tmp"
CODERS = {}


def im(*args, data=None):
    return subprocess.run(
        [MAGICK, *map(str, args)], input=data, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=True,
    ).stdout


def safe_path(path):
    value = str(Path(path).absolute())
    if "%" in value or "[" in value or re.match(r"^[A-Za-z0-9_+\-]+:", str(path)):
        raise ValueError(f"Đường dẫn có cú pháp đặc biệt bị cấm: {value}")
    # Absolute paths also prevent ImageMagick from interpreting a leading dash/@.
    return Path(path).absolute()


def validate_input(path):
    path = safe_path(path)
    if not path.is_file():
        raise ValueError(f"Không tìm thấy file vào: {path}")
    # Reject scripting formats BEFORE handing content to any ImageMagick decoder.
    with path.open("rb") as source:
        header = source.read(16)
    coder = ("PNG" if header.startswith(b"\x89PNG\r\n\x1a\n") else
             "JPEG" if header.startswith(b"\xff\xd8\xff") else
             "WEBP" if header[:4] == b"RIFF" and header[8:12] == b"WEBP" else None)
    if coder is None:
        raise ValueError("Chỉ nhận ảnh đơn PNG, JPEG hoặc WebP; cấm SVG, MSL, MVG và định dạng khác.")
    frames = im("identify", "-format", "%m %n\n", f"{coder}:{path}").splitlines()
    if len(frames) != 1 or frames[0] != f"{coder} 1".encode():
        raise ValueError("Chỉ nhận ảnh đơn PNG, JPEG hoặc WebP, không nhận ảnh động hoặc nhiều trang.")
    CODERS[str(path)] = coder
    return path


def input_image(path):
    path = safe_path(path)
    if str(path) not in CODERS:
        validate_input(path)
    return f"{CODERS[str(path)]}:{path}"


def dimensions(path):
    path = validate_input(path)
    return tuple(map(int, im(input_image(path), "-format", "%w %h", "info:").split()))


def rgba(path):
    path = validate_input(path)
    w, h = dimensions(path)
    data = bytearray(im(input_image(path), "+repage", "-colorspace", "sRGB",
                        "-alpha", "on", "-depth", "8", "rgba:-"))
    if len(data) != w * h * 4:
        raise ValueError("Chỉ nhận ảnh đơn, không nhận ảnh động hoặc nhiều trang.")
    return w, h, data


def output_guard(path, inputs=()):
    path = safe_path(path)
    if any(path.resolve() == safe_path(p).resolve() for p in inputs):
        raise ValueError("File ra trùng file vào.")
    if path.exists() or path.is_symlink():
        raise ValueError(f"Từ chối ghi đè file đã có: {path}")
    if path.suffix.lower() != ".png":
        raise ValueError("File ra phải có đuôi .png.")
    return path


def publish_file(staged, destination):
    """Atomic no-replace publication, also used for job text/JSON artifacts."""
    destination = safe_path(destination)
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(f"Từ chối ghi đè file đã có: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    stops = {signal.SIGTERM, signal.SIGHUP, signal.SIGINT}
    previous = signal.pthread_sigmask(signal.SIG_BLOCK, stops)
    partial = None
    try:
        fd, partial = tempfile.mkstemp(prefix=".normalize-", suffix=".partial", dir=destination.parent)
        os.fchmod(fd, 0o644)
        signal.pthread_sigmask(signal.SIG_SETMASK, previous)
        with os.fdopen(fd, "wb") as output, open(safe_path(staged), "rb") as source:
            shutil.copyfileobj(source, output)
            output.flush()
            os.fsync(output.fileno())
        os.link(partial, destination)
    finally:
        signal.pthread_sigmask(signal.SIG_BLOCK, stops)
        try:
            if partial is not None:
                Path(partial).unlink(missing_ok=True)
        finally:
            signal.pthread_sigmask(signal.SIG_SETMASK, previous)


def publish(staged, destination):
    publish_file(staged, output_guard(destination))


def atomic_writer(destination="dst"):
    """Public library writers share the CLI guards and atomic publication."""
    def decorate(function):
        signature = inspect.signature(function)
        @functools.wraps(function)
        def guarded(*args, **kwargs):
            bound = signature.bind(*args, **kwargs)
            target = output_guard(bound.arguments[destination])
            for name in ("src", "files"):
                if name in bound.arguments:
                    values = bound.arguments[name] if name == "files" else [bound.arguments[name]]
                    validated = [validate_input(value) for value in values]
                    bound.arguments[name] = validated if name == "files" else validated[0]
            safe_path(WORK)
            if "tmp" in bound.arguments:
                folder = safe_path(bound.arguments["tmp"])
                if not folder.resolve().is_relative_to(WORK.resolve()):
                    raise ValueError("Thư mục xử lý phải nằm trong WORK.")
            WORK.mkdir(exist_ok=True)
            with tempfile.TemporaryDirectory(prefix="writer-", dir=WORK) as folder:
                bound.arguments[destination] = Path(folder) / "result.png"
                if "tmp" in bound.arguments:
                    bound.arguments["tmp"] = Path(folder)
                result = function(*bound.args, **bound.kwargs)
                publish(bound.arguments[destination], target)
                return result
        return guarded
    return decorate


def stop_signal(signum, frame):
    raise SystemExit(f"Dừng theo tín hiệu {signum}; dọn file tạm.")


def install_signal_handlers():
    if threading.current_thread() is threading.main_thread():
        for stop in (signal.SIGTERM, signal.SIGHUP):
            if signal.getsignal(stop) != signal.SIG_IGN:
                signal.signal(stop, stop_signal)


@atomic_writer("path")

def save_rgba(w, h, data, path):
    opaque = all(a == 255 for a in data[3::4])
    im("-size", f"{w}x{h}", "-depth", "8", "rgba:-", "-strip",
       *(["-alpha", "off"] if opaque else []),
       f"{'PNG24' if opaque else 'PNG32'}:{path}", data=data)


def pct(value):
    if not re.fullmatch(r"\d+(?:\.\d+)?%", value):
        raise argparse.ArgumentTypeError("Dùng phần trăm, ví dụ 8%.")
    number = float(value[:-1]) / 100
    if not 0 <= number < .5:
        raise argparse.ArgumentTypeError("Phần trăm phải từ 0% đến dưới 50%.")
    return number


def size(value):
    if not re.fullmatch(r"[1-9]\d*(?:x[1-9]\d*)?", value):
        raise argparse.ArgumentTypeError("Khổ phải là N hoặc WxH với số nguyên dương.")
    nums = list(map(int, value.split("x")))
    return nums[0], nums[-1]


def color(value):
    if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
        raise argparse.ArgumentTypeError("Màu phải là #RRGGBB.")
    return value


def corners(w, h, pixels):
    return [tuple(pixels[i:i + 3]) for i in (0, (w - 1) * 4, (h - 1) * w * 4, (w * h - 1) * 4)]


def background_color(w, h, pixels, option="--bg"):
    n = min(8, w, h)
    patches = []
    for x0, y0 in ((0, 0), (w - n, 0), (0, h - n), (w - n, h - n)):
        patches.append(tuple(round(statistics.median(
            pixels[(y * w + x) * 4 + c]
            for y in range(y0, y0 + n) for x in range(x0, x0 + n)
        )) for c in range(3)))
    result = tuple(round(statistics.median(p[c] for p in patches)) for c in range(3))
    if max(math.dist(p, result) for p in patches) > 45:
        raise ValueError(f"Bốn mảng góc khác màu quá nhiều; chỉ định {option} hoặc kiểm tra ảnh.")
    return result


def neighbours(p, w, h):
    x = p % w
    if p >= w:
        yield p - w
    if p < w * (h - 1):
        yield p + w
    if x:
        yield p - 1
    if x < w - 1:
        yield p + 1


def connected_mask(candidate, w, h, pixels, background, minimum):
    """Keep border background, plus sufficiently large enclosed neutral pockets."""
    exterior = bytearray(w * h)
    queue = deque()
    border = list(range(w)) + list(range((h - 1) * w, h * w))
    border += list(range(0, w * h, w)) + list(range(w - 1, w * h, w))
    for p in border:
        if candidate[p] and not exterior[p]:
            exterior[p] = 1
            queue.append(p)
    while queue:
        for q in neighbours(queue.popleft(), w, h):
            if candidate[q] and not exterior[q]:
                exterior[q] = 1
                queue.append(q)
    neutral = max(background) - min(background) <= 6
    pockets = bytearray(candidate)
    if neutral:
        for p in range(w * h):
            rgb = pixels[p * 4:p * 4 + 3]
            pockets[p] = candidate[p] and max(rgb) - min(rgb) <= 6
    seen = bytearray(exterior)
    for start in range(w * h):
        if seen[start] or not pockets[start]:
            continue
        queue.append(start)
        seen[start] = 1
        component = []
        while queue:
            p = queue.popleft()
            component.append(p)
            for q in neighbours(p, w, h):
                if pockets[q] and not seen[q]:
                    seen[q] = 1
                    queue.append(q)
        if len(component) >= minimum:
            for p in component:
                exterior[p] = 1
    return exterior


def key_excess(rgb, background):
    """Colour-difference matte for saturated green, blue, red, cyan or magenta."""
    low, high = min(background), max(background)
    if high - low < 80:
        return 0, ()
    keyed = tuple(c for c in range(3) if background[c] > (low + high) / 2)
    other = tuple(c for c in range(3) if c not in keyed)
    excess = min(rgb[c] for c in keyed) - max(rgb[c] for c in other)
    return max(0, excess), keyed


def strong_key(rgb, background, absolute=.5):
    """Include dark saturated key paint; absolute excess alone misses shaded gaps."""
    bg_excess, _ = key_excess(background, background)
    excess, _ = key_excess(rgb, background)
    return bool(bg_excess and (excess > absolute * bg_excess or
                              (excess > .25 * bg_excess and excess > .7 * max(rgb))))


def edge_matte(p, w, h, source, distances, background, fallback=False):
    """Fit source = alpha*nearby paint + (1-alpha)*key near the matte only.

    Return the sampled paint as well as coverage: channel clamping cannot
    reconstruct a brown needle and produces olive/dark outlines instead.
    """
    x,y=p%w,p//w
    vector=[source[p*4+c]-background[c] for c in range(3)]
    bg_excess,_=key_excess(background,background)
    best=9
    result=None
    offsets=[(dx,dy) for radius in range(1,7) for dx,dy in
             ((radius,0),(-radius,0),(0,radius),(0,-radius),
              (radius,radius),(-radius,radius),(radius,-radius),(-radius,-radius))]
    for dx,dy in offsets:
        xx,yy=x+dx,y+dy
        if not (0<=xx<w and 0<=yy<h):continue
        q=yy*w+xx
        if distances[q]<=distances[p]*1.02:continue
        foreground=source[q*4:q*4+3]
        if key_excess(foreground,background)[0]>.25*bg_excess:continue
        paint=[foreground[c]-background[c] for c in range(3)]
        denominator=sum(v*v for v in paint)
        if not denominator:continue
        alpha=sum(a*b for a,b in zip(vector,paint))/denominator
        if not .05<alpha<.995:continue
        residual=sum((a-alpha*b)**2 for a,b in zip(vector,paint))/3
        if residual<=best:
            best=residual
            result=(alpha,foreground)
    return result


def warn_opaque_corners(w, h, alpha):
    """Report opaque pixels in corner patches that still reach the image border."""
    n = min(8, w, h)
    for x0, y0 in ((0, 0), (w-n, 0), (0, h-n), (w-n, h-n)):
        if any(alpha[y*w+x] > 8
               for y in range(y0, y0+n) for x in range(x0, x0+n)
               if x in (0, w-1) or y in (0, h-1)):
            print("Cảnh báo: mảng góc nối viền vẫn có alpha >8; kiểm màu nền nguồn hoặc --keep-alpha.", file=sys.stderr)
            return


@atomic_writer()
def key(src, dst, bg="auto", fuzz=.12, keep_alpha=False, mode="connected", shrink=0, despill="auto", bg_option="--bg", no_key_hue=False):
    w, h, pixels = rgba(src)
    alphas = pixels[3::4]
    meaningful = sum(a < 128 for a in alphas) >= math.ceil(w * h * .01)
    if keep_alpha or meaningful:
        print("Giữ alpha theo --keep-alpha." if keep_alpha else
              "Giữ alpha có ý nghĩa (≥1% pixel alpha <128).", file=sys.stderr)
        if not any(a > 8 for a in alphas):
            raise ValueError("Không tìm thấy vật trong alpha đầu vào.")
        if not keep_alpha:
            warn_opaque_corners(w, h, alphas)
        save_rgba(w, h, pixels, dst)
        return
    if any(a < 255 for a in alphas):
        print("Alpha rời rạc chưa đủ ý nghĩa; tiếp tục tách nền.", file=sys.stderr)
    background = (background_color(w, h, pixels, bg_option) if bg == "auto" else
                  tuple(int(bg[i:i + 2], 16) for i in (1, 3, 5)))
    low = fuzz * 255 * math.sqrt(3)
    high = max(low * 1.5, low + 1)
    candidate = bytearray(w * h)
    distances = array("f", [0]) * (w * h)
    for p in range(w * h):
        distances[p] = math.dist(pixels[p * 4:p * 4 + 3], background)
        candidate[p] = distances[p] < high or strong_key(pixels[p*4:p*4+3], background)
        # Neutral keys must not flood coloured petal highlights.
        if max(background)-min(background) <= 6:
            rgb = pixels[p*4:p*4+3]
            candidate[p] = candidate[p] and max(rgb)-min(rgb) <= 6
    if mode == "connected":
        candidate = connected_mask(candidate, w, h, pixels, background, 64)
    bg_excess, keyed = key_excess(background, background)
    source = bytes(pixels)
    near_background = None
    if keyed and despill != "off":
        background_mask = bytes(255 if candidate[p] and (distances[p] <= low or strong_key(pixels[p*4:p*4+3],background)) else 0 for p in range(w * h))
        near_background = im("-size", f"{w}x{h}", "-depth", "8", "gray:-", "-virtual-pixel", "edge",
                             "-morphology", "Dilate", "Diamond:3", "-depth", "8", "gray:-", data=background_mask)
    mask = bytearray(w * h)
    for p in range(w * h):
        i = p * 4
        rgb = pixels[i:i + 3]
        distance = distances[p]
        t = min(1, max(0, (distance - low) / (high - low)))
        alpha = t * t * (3 - 2 * t) if candidate[p] else 1
        excess, _ = key_excess(rgb, background) if keyed and despill != "off" else (0, ())
        # A shaded pure key is background even though it is far from the bright
        # key in RGB distance. Do not turn it into opaque grey or olive paint.
        eligible = near_background is not None and near_background[p]
        # Interior paint never enters colour-difference alpha or keyed-channel clamp.
        inferred = (edge_matte(p, w, h, source, distances, background, fallback=excess>25)
                    if alpha > 0 and eligible else None)
        if inferred is not None and not candidate[p] and (inferred[0] >= .95 or (max(rgb)<70 and excess<=20)):
            inferred = None
        if candidate[p] and strong_key(rgb, background) and excess > .7 * max(rgb) and inferred is None:
            alpha = 0
        if inferred is not None:
            alpha = inferred[0]
        elif excess>20 and eligible:
            alpha = min(alpha, max(0, 1 - excess / bg_excess))
        if alpha > 0:
            unmix_alpha = inferred[0] if inferred is not None else (
                max(alpha, 1 - excess / bg_excess) if excess and eligible else alpha)
            clean = [max(0, min(255, round((rgb[c] - (1 - unmix_alpha) * background[c]) / unmix_alpha)))
                     for c in range(3)]
            if inferred is not None:
                clean = list(inferred[1])
            if excess>20 and eligible and inferred is None:
                limit = max(clean[c] for c in range(3) if c not in keyed)
                for c in keyed:
                    clean[c] = min(clean[c], limit)
            pixels[i:i + 3] = bytes(clean)
        else:
            pixels[i:i + 3] = b"\0\0\0"
        mask[p] = round(alpha * alphas[p])
        if no_key_hue and keyed and despill != "off" and alpha>0 and (
                (eligible and mask[p]<255) or excess>50):
            limit = max(pixels[i+c] for c in range(3) if c not in keyed)
            for c in keyed:
                pixels[i+c] = min(pixels[i+c], limit)
    if shrink:
        mask = bytearray(im("-size", f"{w}x{h}", "-depth", "8", "gray:-",
                            "-virtual-pixel", "edge", "-morphology", "Erode",
                            f"Diamond:{shrink}", "-depth", "8", "gray:-", data=mask))
    if not any(a > 8 for a in mask):
        raise ValueError("Không tìm thấy vật sau khi tách nền/co mask.")
    warn_opaque_corners(w, h, mask)
    pixels[3::4] = mask
    save_rgba(w, h, pixels, dst)


def bounds(w, h, data, region=None, cutoff=8):
    x0, y0, rw, rh = region or (0, 0, w, h)
    left, top, right, bottom = rw, rh, -1, -1
    for y in range(rh):
        for x in range(rw):
            if data[((y0 + y) * w + x0 + x) * 4 + 3] > cutoff:
                left, top, right, bottom = min(left, x), min(top, y), max(right, x), max(bottom, y)
    if right < 0:
        raise ValueError("Ô không có vật; không thể trim hoặc đặt lề.")
    return left, top, right - left + 1, bottom - top + 1


def fit_area(target, margin):
    tw, th = target
    iw, ih = tw - 2 * math.ceil(tw * margin) - 4, th - 2 * math.ceil(th * margin) - 4
    if min(iw, ih) < 1:
        raise ValueError("Khổ quá nhỏ cho lề và lọc mép.")
    return iw, ih


@atomic_writer()
def fit(src, dst, target, margin, no_upscale=False):
    w, h, pixels = rgba(src)
    x, y, bw, bh = bounds(w, h, pixels)
    iw, ih = fit_area(target, margin)
    tw, th = target
    im(input_image(src), "+repage", "-crop", f"{bw}x{bh}+{x}+{y}", "+repage", "-filter", "Triangle", "-resize", f"{iw}x{ih}" + (">" if no_upscale else ""),
       "-background", "none", "-gravity", "center", "-extent", f"{tw}x{th}",
       "-strip", f"PNG32:{dst}")


@atomic_writer()
def pad(src, dst, target, margin, grid, tmp):
    if grid == "1x1":
        fit(src, dst, target, margin)
        return
    tw, th = target
    w, h, pixels = rgba(src)
    if w % 2 or h % 2 or tw % 2 or th % 2:
        raise ValueError("Atlas 2×2 cần khổ vào và ra chia hết cho 2.")
    if any(pixels[(y * w + x) * 4 + 3] > 8 for y in (h // 2 - 1, h // 2) for x in range(w)) or any(
        pixels[(y * w + x) * 4 + 3] > 8 for x in (w // 2 - 1, w // 2) for y in range(h)
    ):
        raise ValueError("Vật chạm đường chia atlas 2×2; từ chối cắt vật.")
    tiles = []
    for row in range(2):
        for col in range(2):
            crop, tile = tmp / f"crop-{row}-{col}.png", tmp / f"tile-{row}-{col}.png"
            im(input_image(src), "+repage", "-crop", f"{w // 2}x{h // 2}+{col * w // 2}+{row * h // 2}",
               "+repage", f"PNG32:{crop}")
            fit(crop, tile, (tw // 2, th // 2), margin)
            tiles.append(tile)
    im("(", tiles[0], tiles[1], "+append", ")", "(", tiles[2], tiles[3], "+append", ")",
       "-append", "-strip", f"PNG32:{dst}")


def ratio(a, b):
    return a / b if b else (1 if not a else 1e9)


def seam_metrics(w, h, pixels, blend=.12):
    return copy.deepcopy(_seam_metrics(w,h,bytes(pixels),blend))


@functools.lru_cache(maxsize=4)
def _seam_metrics(w, h, pixels, blend=.12):
    if min(w, h) < 4:
        raise ValueError("Đo mép cần cả hai cạnh ≥4 px.")
    result = {}
    for axis in ("x", "y"):
        length, lines = (w, h) if axis == "x" else (h, w)
        def value(pos, line, channel):
            p = line * w + pos if axis == "x" else pos * w + line
            return pixels[p * 4 + channel]
        def diff(a, b):
            return sum(abs(value(a, line, c) - value(b, line, c))
                       for line in range(lines) for c in range(3)) / (lines * 3)
        seam = diff(0, length - 1)
        median = statistics.median(diff(k, k+1) for k in range(length-1))
        mirror_band = min(30, max(1, (length-2)//4))
        mirror = statistics.mean(diff(k, length-1-k) for k in range(1, mirror_band+1))
        # Both pairs are separated by 2k+1 pixels.
        controls = [statistics.mean(diff(center-k-1, center+k) for k in range(1, mirror_band+1))
                    for center in (length//3, length//2, 2*length//3)
                    if center > mirror_band and center+mirror_band < length]
        control = statistics.median(controls) if controls else mirror
        band = max(1, min((length-2)//3, max(2, math.ceil(length*blend/(1-blend)))))
        lap = [sum(abs(value(k-1, line, c)-2*value(k, line, c)+value(k+1, line, c))
                   for line in range(lines) for c in range(3))/(lines*3)
               for k in range(1, length-1)]
        interior = statistics.mean(lap[band:-band]) if len(lap)>2*band else statistics.mean(lap)
        window = min(30, max(2, band//3))
        windows = []
        starts = sorted({1, length-1-window, *range(1, length-window, max(1, window//2))})
        for start in starts:
            if start <= band or start+window >= length-band:
                detail = statistics.mean(lap[start-1:start-1+window])
                windows.append({"start": start, "end": start+window, "detail": round(detail,6),
                                "ratio": round(ratio(detail,interior),6)})
        detail_ratio = min(v["ratio"] for v in windows)
        streak = sa.row_residual(sa.rows(w,h,pixels,axis), band)
        narrow = sa.narrow_mirror(sa.rows(w,h,pixels,axis))
        edge_ok = seam <= max(1, 2.5*median)
        mirror_ok = (control <= 1 or mirror >= .5*control) and all(v["control"]<=1 or v["ratio"]>=.5 for v in narrow)
        detail_ok = detail_ratio >= .9
        streak_ok = streak <= 5
        result[axis] = {
            "edge_mae": round(seam,6), "adjacent_median": round(median,6),
            "edge_ratio": round(ratio(seam,median),6),
            "mirror_mae": round(mirror,6), "mirror_control_mae": round(control,6),
            "mirror_ratio": round(ratio(mirror,control),6),
            "band_width": band, "detail_windows": windows, "mirror_scales": narrow,
            "whole_detail": round(statistics.mean(lap),6),
            "band_detail_ratio": round(detail_ratio,6), "row_step_excess": round(streak,6),
            "criteria": {"edge":edge_ok,"mirror":mirror_ok,"detail":detail_ok,"row_streak":streak_ok},
            "pass": edge_ok and mirror_ok and detail_ok and streak_ok,
        }
    return result


def reference_metrics(w, h, pixels, rw, rh, reference, blend=.12):
    report = seam_metrics(w,h,pixels,blend)
    before = seam_metrics(rw,rh,reference,blend)
    for axis in ("x","y"):
        after, source = report[axis], before[axis]
        after["whole_detail_source_ratio"] = round(ratio(after["whole_detail"],source["whole_detail"]),6)
        after["mirror_source_ratio"] = round(ratio(after["mirror_mae"],source["mirror_mae"]),6)
        exempt = not .75 <= source["mirror_ratio"] <= 1.5
        after["reference_mirror_exempt"] = exempt
        after["criteria"]["reference_mirror"] = exempt or source["mirror_mae"]<=1 or after["mirror_source_ratio"]>=.5
        after["criteria"]["reference_detail"] = after["whole_detail_source_ratio"] >= .9
        data = sa.rows(w,h,pixels,axis)
        ref = sa.rows(rw,rh,reference,axis)
        length, rlength = len(data[0])//4, len(ref[0])//4
        # For xy, apply the orthogonal overlap to the reference first. This
        # retains native source coordinates, never normalized-position windows.
        if len(data)!=len(ref):
            orthogonal = "y" if axis=="x" else "x"
            ow,oh,op,_ = overlap_pixels(rw,rh,reference,orthogonal,blend)
            ref = sa.rows(ow,oh,op,axis)
        band = rlength-length if 0<rlength-length<length//2 else after["band_width"]
        has_overlap = rlength>length
        path = sa.infer_path(data,ref,band) if has_overlap else None
        ref_laps=[]
        for k in range(1,length-1):
            samples=[]
            for y,row in enumerate(ref):
                q = k+length if has_overlap and k<path[y] else k
                if not 1<=q<rlength-1:continue
                samples.extend(abs(row[(q-1)*4+c]-2*row[q*4+c]+row[(q+1)*4+c]) for c in range(3))
            ref_laps.append(statistics.mean(samples) if samples else 0)
        for window in after["detail_windows"]:
            expected=statistics.mean(ref_laps[window["start"]-1:window["end"]-1])
            window["source_ratio"] = round(ratio(window["detail"],expected),6)
        after["band_detail_source_ratio"] = min(v["source_ratio"] for v in after["detail_windows"])
        after["criteria"]["detail"] = after["band_detail_source_ratio"] >= .9
        residual = sa.row_residual(data,band,ref,path)
        after["row_source_residual"] = round(residual,6)
        after["criteria"]["row_streak"] = residual <= 5
        if path and band>=10:
            cuts=sa.cut_metrics(data,ref,band,path)
            after["cut"]={"path":path,"radius":3,"bands":cuts}
            after["criteria"]["cut_continuity"] = all(v["pass"] for v in cuts)
        after["pass"] = all(after["criteria"].values())
    return report


def overlap_pixels(w,h,pixels,direction,blend):
    length, lines = (w, h) if direction == "x" else (h, w)
    if length < 4 or blend <= 0:
        raise ValueError("Ảnh lặp cần chiều xử lý ≥4 px và --blend >0%.")
    band = max(2, min(length // 2, math.ceil(length * blend)))
    nw, nh = (w - band, h) if direction == "x" else (w, h - band)
    path=sa.minimum_path(sa.rows(w,h,pixels,direction),band)
    radius = max(1, min(3, band//8))
    output = bytearray(nw * nh * 4)
    for line in range(lines):
        for k in range(length-band):
            dest=(line*nw+k)*4 if direction=="x" else (k*nw+line)*4
            offset=lambda pos:(line*w+pos)*4 if direction=="x" else (pos*w+line)*4
            if k>=band:
                output[dest:dest+4]=pixels[offset(k):offset(k)+4];continue
            t=min(1,max(0,(k-path[line]+radius)/(2*radius)))
            t=t*t*(3-2*t)
            a,b=offset(length-band+k),offset(k)
            alpha=pixels[a+3]*(1-t)+pixels[b+3]*t
            for c in range(3):
                output[dest+c]=round((pixels[a+c]*pixels[a+3]*(1-t)+pixels[b+c]*pixels[b+3]*t)/alpha) if alpha else 0
            output[dest+3]=round(alpha)
    return nw,nh,output,{"path":path,"radius":radius,"overlap":band,"source_size":[w,h]}


@atomic_writer()
def seamless(src, dst, axis, blend, keep_size=False):
    w, h, pixels = rgba(src)
    original_size = w, h
    seams = {}
    for direction in (("x", "y") if axis == "xy" else ("x",)):
        w,h,pixels,seams[direction] = overlap_pixels(w,h,pixels,direction,blend)
    if keep_size:
        pixels = bytearray(im("-size", f"{w}x{h}", "-depth", "8", "rgba:-",
                              "-virtual-pixel", "tile", "-filter", "Lanczos",
                              "-resize", f"{original_size[0]}x{original_size[1]}!",
                              "-depth", "8", "rgba:-", data=pixels))
        w, h = original_size
    save_rgba(w, h, pixels, dst)
    # Persist the actual path inside the PNG, including source coordinates.
    payload=b"art-normalize-seam\0"+json.dumps({"version":1,"keep_size":keep_size,"axes":seams},separators=(",",":")).encode()
    chunk=b"tEXt"+payload
    raw=Path(dst).read_bytes()
    Path(dst).write_bytes(raw[:-12]+struct.pack(">I",len(payload))+chunk+struct.pack(">I",zlib.crc32(chunk))+raw[-12:])
    return seams


def metrics(src, grid="1x1"):
    w, h, pixels = rgba(src)
    result = {
        "size": [w, h], "corners": ["#" + "".join(f"{c:02X}" for c in v) for v in corners(w, h, pixels)],
        "corner_alpha": [pixels[i + 3] for i in (0, (w - 1) * 4, (h - 1) * w * 4, (w * h - 1) * 4)],
        "seams": seam_metrics(w, h, pixels),
    }
    regions = [(0, 0, w, h)] if grid == "1x1" else [
        (x * w // 2, y * h // 2, w // 2, h // 2) for y in range(2) for x in range(2)]
    result["margins_ltrb"] = []
    for region in regions:
        x, y, bw, bh = bounds(w, h, pixels, region)
        result["margins_ltrb"].append([x, y, region[2] - x - bw, region[3] - y - bh])
    return result


@atomic_writer()
def sheet(files, dst, bg, tile, tmp):
    cells = []
    foreground = "#342C28" if bg in ("light", "white") else "#E6E6E6"
    background = {"light": "#F2E9D8", "white": "#FFFFFF"}.get(bg, "#282421")
    cellw = max(tile, 160)
    fonts = im("-list", "font").decode(errors="replace")
    names = re.findall(r"Font:\s*(\S+)", fonts)
    arial = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
    if arial.is_file():
        font = ["-font", str(arial)]
    elif "DejaVu-Sans" in names:
        font = ["-font", "DejaVu-Sans"]
    else:
        font = ["-font", names[0]] if names else []
    for index, src in enumerate(files):
        cell = tmp / f"sheet-{index}.png"
        base = (["-size", f"{cellw}x{tile}", "pattern:checkerboard", "-colorspace", "sRGB"]
                if bg == "checker" else ["-size", f"{cellw}x{tile}", f"xc:{background}"])
        # Input paths cannot contain %/[; prefixing text avoids @file expansion.
        label = "Ảnh: " + Path(src).stem.replace("%", "%%") + f" · {tile} px"
        im(*base, "(", input_image(src), "+repage", "-resize", f"{tile}x{tile}", ")", "-gravity", "center",
           "-compose", "over", "-composite", "-background", background, "-gravity", "south",
           "-splice", "0x30", "-fill", foreground, *font, "-pointsize", "11", "-annotate", "+0+9",
           label, "-strip", f"PNG24:{cell}")
        cells.append(cell)
    im("montage", *cells, "-tile", f"{min(5, len(cells))}x", "-geometry", "+4+4",
       "-background", background, "-strip", f"PNG24:{dst}")


def key_options(parser, fuzz):
    parser.add_argument("--fuzz", type=pct, default=fuzz, help=f'Ngưỡng khoảng cách màu nền; mặc định {fuzz:.0%}.'.replace('%','%%'))
    parser.add_argument("--no-key-hue", action="store_true", help='Vật không có sắc khóa: kẹp viền và chênh khóa >50 trong lòng vật.')
    parser.add_argument("--keep-alpha", action="store_true", help='Giữ rõ ràng alpha/RGB nguồn, bỏ tách nền.')
    parser.add_argument("--mode", choices=["connected", "global"], default="connected", help='Nền nối biên và túi kín, hoặc khóa toàn ảnh; mặc định connected.')
    parser.add_argument("--shrink", type=int, default=0, help='Co mask Diamond N px; mặc định 0.')
    parser.add_argument("--despill", choices=["auto", "protect-interior", "off"], default="auto", help='auto/protect-interior chỉ xử lý vùng nền nở 3 px; off bỏ khử loang.')


def main():
    install_signal_handlers()
    translations={"usage: ":"cách dùng: ","positional arguments":"tham số vị trí", "options":"tùy chọn", "show this help message and exit":"Hiện trợ giúp rồi thoát."}
    translate=argparse._
    argparse._=lambda text:translations.get(text,translate(text))
    parser = argparse.ArgumentParser(description="Chuẩn hóa ảnh bằng ImageMagick 7; từ chối ghi đè.")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("key-alpha", "pad-margin", "flat-bg", "seamless", "seam-check"):
        p = sub.add_parser(name)
        p.add_argument("src", type=Path, help="Ảnh nguồn PNG/JPEG/WebP một frame.")
        p.add_argument("dst", type=Path, help="Đường dẫn PNG mới.")
        if name == "key-alpha":
            p.add_argument("--bg", default="auto", type=lambda v: v if v == "auto" else color(v), help='Màu nền nguồn #RRGGBB; mặc định auto.')
            key_options(p, .12)
        if name == "pad-margin":
            p.add_argument("--size", type=size, required=True, help='Khổ đầu ra N hoặc WxH.')
            p.add_argument("--margin", type=pct, required=True, help='Lề tối thiểu theo phần trăm mỗi cạnh.')
            p.add_argument("--grid", choices=["1x1", "2x2"], default="1x1", help='Bố trí một ảnh hoặc atlas bốn ô; mặc định 1x1.')
        if name == "flat-bg":
            p.add_argument("--src-bg", default="auto", type=lambda v: v if v == "auto" else color(v), help="Màu nền nguồn; mặc định auto.")
            p.add_argument("--bg", type=color, required=True, help='Màu nền đích #RRGGBB.')
            p.add_argument("--size", type=size, required=True, help='Khổ đầu ra N hoặc WxH.')
            key_options(p, .06)
        if name in ("seamless", "seam-check"):
            p.add_argument("--axis", choices=["x", "xy"], required=True, help='Trục cần xử lý/kiểm: x hoặc xy.')
        if name == "seamless":
            p.add_argument("--blend", type=pct, default=.12, help="Bề rộng overlap, mặc định 12%%.")
            p.add_argument("--keep-size", action="store_true", help="Co giãn về khổ nguồn bằng Lanczos và virtual-pixel tile.")
        if name == "seam-check":
            p.add_argument("--reference", type=Path, help="Nguồn đối chiếu chi tiết, có thể khác khổ sau overlap.")
            p.add_argument("--blend", type=pct, default=.12, help="Bề rộng overlap cần kiểm, mặc định 12%%.")
    p = sub.add_parser("icon")
    p.add_argument("src", type=Path, help="Ảnh nguồn PNG/JPEG/WebP một frame.")
    p.add_argument("outdir", type=Path, help="Thư mục xuất icon.")
    p.add_argument("--sizes", default="256,64", help='Danh sách cỡ icon; mặc định 256,64.')
    p.add_argument("--src-bg", default="auto", type=lambda v: v if v == "auto" else color(v), help="Màu nền nguồn; mặc định auto.")
    key_options(p, .12)
    p = sub.add_parser("sheet")
    p.add_argument("dst", type=Path, help="Đường dẫn PNG mới.")
    p.add_argument("files", type=Path, nargs="+", help="Danh sách ảnh nguồn.")
    p.add_argument("--bg", choices=["dark", "light", "white", "checker"], default="checker", help='Nền sheet: tối, kem, trắng hoặc caro; mặc định checker.')
    p.add_argument("--tile", type=int, default=256, help='Khổ hiển thị trên sheet; mặc định 256 px.')
    p = sub.add_parser("measure")
    p.add_argument("src", type=Path, help="Ảnh nguồn PNG/JPEG/WebP một frame.")
    p.add_argument("--grid", choices=["1x1", "2x2"], default="1x1", help='Bố trí một ảnh hoặc atlas bốn ô; mặc định 1x1.')
    args = parser.parse_args()
    if getattr(args, "shrink", 0) < 0:
        raise ValueError("--shrink phải ≥0.")
    inputs = [validate_input(p) for p in args.files] if args.command == "sheet" else [validate_input(args.src)]
    if args.command == "sheet":
        args.files = inputs
    else:
        args.src = inputs[0]
    if args.command == "measure":
        print(json.dumps(metrics(args.src, args.grid), ensure_ascii=False))
        return
    if getattr(args, "reference", None):
        args.reference = validate_input(args.reference)
        inputs.append(args.reference)
    if args.command == "icon":
        safe_path(args.outdir)
        if not re.fullmatch(r"[1-9]\d*(?:,[1-9]\d*)*", args.sizes):
            raise ValueError("--sizes cần danh sách số nguyên dương, ví dụ 256,64.")
        sizes = list(dict.fromkeys(map(int, args.sizes.split(","))))
        for s in sizes:
            fit_area((s, s), .08)
        outputs = [output_guard(args.outdir / f"{args.src.stem}.{s}.png", inputs) for s in sizes]
    else:
        outputs = [output_guard(args.dst, inputs)]
    if args.command == "sheet" and args.tile < 1:
        raise ValueError("--tile phải dương.")
    WORK.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="normalize-", dir=WORK) as directory:
        tmp = Path(directory)
        staged = [tmp / f"output-{i}.png" for i in range(len(outputs))]
        dst = staged[0]
        options = {name: getattr(args, name) for name in ("fuzz", "keep_alpha", "mode", "shrink", "despill", "no_key_hue")
                   if hasattr(args, name)}
        if args.command == "key-alpha":
            key(args.src, dst, bg=args.bg, **options)
        elif args.command == "pad-margin":
            pad(args.src, dst, args.size, args.margin, args.grid, tmp)
        elif args.command == "flat-bg":
            cut, padded = tmp / "key.png", tmp / "pad.png"
            key(args.src, cut, bg=args.src_bg, bg_option="--src-bg", **options)
            fit(cut, padded, args.size, .08, no_upscale=True)
            im(padded, "-background", args.bg, "-alpha", "remove", "-alpha", "off", "-strip", f"PNG24:{dst}")
        elif args.command == "seamless":
            seamless(args.src, dst, args.axis, args.blend, args.keep_size)
        elif args.command == "seam-check":
            w, h, pixels = rgba(args.src)
            report = (reference_metrics(w,h,pixels,*rgba(args.reference),args.blend) if args.reference
                      else seam_metrics(w,h,pixels,args.blend))
            axes = ("x", "y") if args.axis == "xy" else ("x",)
            print(json.dumps({"seams": report, "pass": all(report[a]["pass"] for a in axes)}, ensure_ascii=False))
            row = tmp / "row.png"
            im(input_image(args.src), "+repage", input_image(args.src), "+repage", "+append", row)
            im(row, *([row, "-append"] if args.axis == "xy" else []), "-strip", f"PNG:{dst}")
        elif args.command == "icon":
            cut = tmp / "key.png"
            key(args.src, cut, bg=args.src_bg, bg_option="--src-bg", **options)
            for s, out in zip(sizes, staged):
                fit(cut, out, (s, s), .08)
        elif args.command == "sheet":
            sheet(args.files, dst, args.bg, args.tile, tmp)
        # Processing all sizes finishes before publishing any member of an icon set.
        for out, destination in zip(staged, outputs):
            publish(out, destination)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        raise SystemExit("ImageMagick không xử lý được ảnh: " + exc.stderr.decode(errors="replace").strip())
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
