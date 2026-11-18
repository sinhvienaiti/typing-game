"""Contact sheets of the Lab's frame sequences, beside the Typing Break study sheets.

    ~/AudioLab/.venv/bin/python -I tools/typing-feedback-lab/scripts/sheets.py <frames dir> <out dir>

<frames dir> holds <W>x<H>/<style>/{key,wrong,word}-<ms>.jpg from capture.mjs. For each size and
style: one sheet with the key, the wrong key and the word complete (13 frames each, ms after the
event), then the Typing Break sheet that technique comes from (tmp/typing-break-study/, T1/T2/T3/T7).
Also one overview per size: every style at the same moments of a key.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[3]
STUDY = ROOT / "tmp" / "typing-break-study" / "moments"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
NAMES = {"stamp": "Stamp", "flare": "Flare", "smash": "Smash", "shatter": "Shatter", "rune": "Rune", "minimal": "Minimal"}
# Which study sheet each style's key effect answers to, and the word release (T3 rim pop, T7 squeeze).
KEY_REF = {
    "stamp": ("letter-1/sheet-slots-a.jpg", "Typing Break T1: the letter stamped onto every matching plate"),
    "smash": ("letter-2/sheet-input-2x.jpg", "Typing Break T2: two-tone key smash in the input bar"),
    "flare": ("letter-2/sheet-input-2x.jpg", "Typing Break T2 (closest): the input bar's per-letter flash"),
    "shatter": ("letter-2/sheet-input-2x.jpg", "Typing Break T2 (closest): white burst and dark shards per letter"),
    "rune": ("letter-2/sheet-input-2x.jpg", "Typing Break T2 (closest): ring marking the letter just typed"),
    "minimal": ("letter-1/sheet-slots-a.jpg", "Typing Break T1 (for scale): our quiet style for readers"),
}
WORD_REF = [
    ("skill-1/sheet-flame-plate-select.jpg", "Typing Break T3: the rim pops then hugs the plate"),
    ("word-2/sheet-word-cycle-love-tea.jpg", "Typing Break T7: the word squeezed flat, the next one appears"),
]
WIDTH = 3080
COLS = 7
PAD = 12


def font(size):
    return ImageFont.truetype(FONT, size)


def grid(paths, label, tile_w):
    frames = [Image.open(p).convert("RGB") for p in paths]
    tile_h = round(frames[0].height * tile_w / frames[0].width)
    rows = (len(frames) + COLS - 1) // COLS
    head = 46
    sheet = Image.new("RGB", (WIDTH, head + rows * (tile_h + 34) + PAD), (18, 18, 24))
    draw = ImageDraw.Draw(sheet)
    draw.text((PAD, 8), label, fill=(240, 236, 226), font=font(28))
    for i, (frame, path) in enumerate(zip(frames, paths)):
        r, c = divmod(i, COLS)
        x = PAD + c * (tile_w + PAD)
        y = head + r * (tile_h + 34)
        sheet.paste(frame.resize((tile_w, tile_h), Image.LANCZOS), (x, y))
        ms = int(Path(path).stem.split("-")[-1])
        draw.text((x + 4, y + tile_h + 4), f"+{ms} ms", fill=(170, 200, 255) if ms <= 100 else (160, 160, 160), font=font(22))
    return sheet


def reference(rel, label):
    path = STUDY / rel
    if not path.exists():
        return None
    img = Image.open(path).convert("RGB")
    h = round(img.height * (WIDTH - 2 * PAD) / img.width)
    sheet = Image.new("RGB", (WIDTH, h + 56), (30, 26, 22))
    draw = ImageDraw.Draw(sheet)
    draw.text((PAD, 10), label + f"  ({rel})", fill=(255, 214, 140), font=font(28))
    sheet.paste(img.resize((WIDTH - 2 * PAD, h), Image.LANCZOS), (PAD, 52))
    return sheet


def stack(parts, title):
    parts = [p for p in parts if p is not None]
    head = 70
    sheet = Image.new("RGB", (WIDTH, head + sum(p.height for p in parts) + PAD * len(parts)), (10, 10, 14))
    draw = ImageDraw.Draw(sheet)
    draw.text((PAD, 14), title, fill=(255, 255, 255), font=font(40))
    y = head
    for p in parts:
        sheet.paste(p, (0, y))
        y += p.height + PAD
    return sheet


def main(frames_dir, out_dir):
    frames_dir = Path(frames_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    made = []
    for size_dir in sorted(p for p in frames_dir.iterdir() if p.is_dir()):
        meta = json.loads((size_dir / "capture.json").read_text()) if (size_dir / "capture.json").exists() else {}
        tile = (WIDTH - PAD * (COLS + 1)) // COLS
        styles = [s for s in NAMES if (size_dir / s).is_dir()]
        for style in styles:
            d = size_dir / style
            parts = [
                grid(sorted(d.glob("key-*.jpg")), f"Key: 'a' of 'thank' typed at +0 ms ({meta.get('intensity', 'normal')}, combo {meta.get('combo', '?')})", tile),
                grid(sorted(d.glob("wrong-*.jpg")), "Wrong key: 'x' while 'n' is due, at +0 ms", tile),
                grid(sorted(d.glob("word-*.jpg")), "Word complete: 'k' at +0 ms (full frame; letters fly to the dragon)", tile),
                reference(*KEY_REF[style]),
                *[reference(*ref) for ref in WORD_REF],
            ]
            sheet = stack(parts, f"Focus strip · {NAMES[style]} · {size_dir.name} · beside Typing Break")
            path = out_dir / f"sheet-{style}-{size_dir.name}.jpg"
            sheet.save(path, quality=86)
            made.append(str(path))
        # Overview: every style at the same moments after a key.
        moments = ["0000", "0017", "0033", "0050", "0083", "0133", "0300"]
        rows = []
        for style in styles:
            rows.append(grid([size_dir / style / f"key-{m}.jpg" for m in moments], NAMES[style], tile))
        overview = stack(rows, f"All styles, one key, same moments · {size_dir.name}")
        path = out_dir / f"sheet-overview-key-{size_dir.name}.jpg"
        overview.save(path, quality=86)
        made.append(str(path))
        rows = [grid([size_dir / style / f"word-{m}.jpg" for m in ["0000", "0033", "0083", "0133", "0200", "0300", "0500"]], NAMES[style], tile) for style in styles]
        overview = stack(rows, f"All styles, word complete, same moments · {size_dir.name}")
        path = out_dir / f"sheet-overview-word-{size_dir.name}.jpg"
        overview.save(path, quality=86)
        made.append(str(path))
    print("\n".join(made))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
