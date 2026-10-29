"""A/B sheet: our frames beside Typing Break's at the same moments (docs/games/SHARED_SYSTEMS_BAR.md §3).

    ~/AudioLab/.venv/bin/python -I tools/typing-feedback-lab/scripts/ab_sheet.py <style frames dir> <out.jpg>

<style frames dir> is <frames>/<W>x<H>/<style>/ from capture.mjs (key-, wrong-, word-<ms>.jpg). Typing Break
frames are cut from typing_break.mov (parent repo root) at the study's events (TYPING_BREAK_STUDY.md):
a key = letter-2 f4121 ('c' of "cost": T1 on the plate, T2 in the input bar); a word = skill-1 f1651
(FLAME's rim pop, T3). Typing Break has no wrong-key feedback (study §2.3): that row is ours alone.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
VIDEO = ROOT / "typing_break.mov"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
MOMENTS = [0, 17, 33, 50, 67, 83, 100, 133, 167, 200, 300]
# Full-resolution crops (2034 x 1140): the left plates (T1, T3) and the input bar (T2).
PLATES = (20, 690, 640, 1010)
WORD_PLATES = (20, 560, 640, 880)
INPUT = (780, 930, 1260, 1140)
# Ours at the same pixel scale as Typing Break's crop (our Large cap height ~ their ~55 px letters).
SAME = (620, 320)
TILE_W = 270
PAD = 8


def tb_frames(event: int, tmp: Path) -> list[Image.Image]:
    out = tmp / f"tb-{event}"
    out.mkdir(exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{event / 60 + 0.002:.4f}", "-i", str(VIDEO), "-frames:v", "61", str(out / "f%03d.png")], check=True)
    return [Image.open(out / f"f{round(ms * 0.06) + 1:03d}.png").convert("RGB") for ms in MOMENTS]


def row(images: list[Image.Image], label: str, font_l, font_s) -> Image.Image:
    h = round(images[0].height * TILE_W / images[0].width)
    sheet = Image.new("RGB", (PAD + len(images) * (TILE_W + PAD), 40 + h + 30), (16, 16, 22))
    draw = ImageDraw.Draw(sheet)
    draw.text((PAD, 8), label, fill=(240, 236, 226), font=font_l)
    for k, (img, ms) in enumerate(zip(images, MOMENTS)):
        x = PAD + k * (TILE_W + PAD)
        sheet.paste(img.resize((TILE_W, h), Image.LANCZOS), (x, 40))
        draw.text((x + 3, 40 + h + 4), f"+{ms} ms", fill=(170, 200, 255), font=font_s)
    return sheet


def same_size(img: Image.Image, cx: float, cy: float, scale: float) -> Image.Image:
    """A SAME-sized full-resolution window around (cx, cy) of a frame captured at `scale`."""
    w, h = SAME[0] * scale, SAME[1] * scale
    box = (round(cx - w / 2), round(cy - h * 0.52), round(cx + w / 2), round(cy + h * 0.48))
    return img.crop(box).resize(SAME, Image.LANCZOS)


def main(style_dir: str, out: str) -> None:
    d = Path(style_dir)
    import json
    view = json.loads((d.parent / "capture.json").read_text())["view"]
    size, vw, vh = view["size"], view["w"], view["h"]
    # Strip crops start at 0.2 h - 1.7 size and are 14 size wide; the row's centre is ~0.6 size under the anchor.
    strip_cx, strip_cy = 7 * size, 2.3 * size
    full_scale = 960 / vw
    row_y = (0.2 * vh + 0.6 * size) * full_scale
    font_l = ImageFont.truetype(FONT, 22)
    font_s = ImageFont.truetype(FONT, 16)
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        key = tb_frames(4121, tmp)
        word = tb_frames(1651, tmp)
        load = lambda kind: [Image.open(d / f"{kind}-{ms:04d}.jpg").convert("RGB") for ms in MOMENTS]
        ours = lambda kind: [same_size(f, strip_cx, strip_cy, 1) for f in load(kind)]
        ours_word = [same_size(f, 480, row_y, full_scale) for f in load("word")]
        rows = [
            row([f.crop(PLATES) for f in key], "Typing Break · key 'c' (f4121): T1 stamp on the matching plate", font_l, font_s),
            row([f.crop(INPUT) for f in key], "Typing Break · same key in the input bar: T2 two-tone smash", font_l, font_s),
            row(ours("key"), f"Ours · {d.name} · key 'a' of 'thank' ({d.parent.name})", font_l, font_s),
            row(ours("wrong"), "Ours · wrong key 'x' while 'n' is due (Typing Break shows nothing, study §2.3)", font_l, font_s),
            row([f.crop(WORD_PLATES) for f in word], "Typing Break · word done (FLAME, f1651): T3 rim pop", font_l, font_s),
            row(ours_word, "Ours · word done: rim pop, seal, letters lift off to fly to the dragon", font_l, font_s),
        ]
    width = max(r.width for r in rows)
    sheet = Image.new("RGB", (width, sum(r.height for r in rows) + 60), (8, 8, 12))
    ImageDraw.Draw(sheet).text((PAD, 14), f"A/B at the same moments · {d.name} · {d.parent.name}", fill=(255, 255, 255), font=ImageFont.truetype(FONT, 30))
    y = 60
    for r in rows:
        sheet.paste(r, (0, y))
        y += r.height
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=86)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
