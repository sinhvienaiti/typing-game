"""Đóng gói PNG RGBA Blender: MP4 nền đen, tấm 6 khung và phép đo alpha.

Chạy bằng tools/vfx-flipbook/.venv/bin/python tools/blender-vfx/finish_samples.py <out>
Thêm --flipbook chỉ sau khi đã tự chấm >= 8; dùng bộ đóng atlas có sẵn.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('out', type=Path)
    p.add_argument('--flipbook', action='store_true')
    args = p.parse_args()
    out = args.out.resolve()
    out.relative_to(ROOT / '.local/blender-samples')
    meta = json.loads((out / 'render.json').read_text())
    files = sorted((out / 'rgba').glob('*.png'))
    assert len(files) == meta['frames'], (len(files), meta['frames'])
    images = [Image.open(f).convert('RGBA') for f in files]
    assert all(i.size == (512, 512) for i in images)
    frames = np.stack([np.array(i) for i in images])
    prompt = (out / 'sample.prompt.txt').read_text()
    measures = []
    for f, im, a in zip(files, images, frames):
        f.with_suffix('.prompt.txt').write_text(prompt, encoding='utf-8')
        alpha = a[..., 3]
        ys, xs = np.where(alpha > 2)
        margin = min(xs.min(), ys.min(), 511-xs.max(), 511-ys.max()) if len(xs) else 256
        border = np.concatenate([alpha[0], alpha[-1], alpha[:, 0], alpha[:, -1]])
        measures.append(dict(frame=int(f.stem), alpha_sum=int(alpha.sum()),
                             alpha_max=int(alpha.max()), margin_px=int(margin),
                             border_alpha_max=int(border.max()), sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
    # Alpha-over thật lên nền đen; không làm mất khói đen bằng luma-key.
    rgb = np.round(frames[..., :3] * (frames[..., 3:4] / 255)).astype('uint8')
    video = out / f'{out.name}.mp4'
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pixel_format', 'rgb24',
           '-video_size', '512x512', '-framerate', '24', '-i', '-', '-an',
           '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(video)]
    subprocess.run(cmd, input=rgb.tobytes(), check=True)
    video.with_suffix('.prompt.txt').write_text(prompt, encoding='utf-8')
    indices = [min(len(files)-1, int(len(files)*v)) for v in (.1,.25,.4,.55,.7,.9)]
    for bg, suffix in [((0,0,0),'sheet'), ((174,174,170),'sheet-light')]:
        sheet = Image.new('RGB', (972,648), (51,51,51))
        for j, ix in enumerate(indices):
            ground = Image.new('RGBA', (512,512), (*bg,255))
            tile = Image.alpha_composite(ground, images[ix]).convert('RGB').resize((320,320), Image.Resampling.LANCZOS)
            sheet.paste(tile, ((j%3)*324+2,(j//3)*324+2))
        path = out/f'{out.name}.{suffix}.jpg'
        sheet.save(path, quality=92)
        path.with_suffix('.prompt.txt').write_text(prompt+f'\nReview sheet: frames {[i+1 for i in indices]}, background {bg}.\n', encoding='utf-8')
    (out/'validation.json').write_text(json.dumps(dict(frames=measures, sheet_frames=[i+1 for i in indices],
        minimum_margin_px=min(m['margin_px'] for m in measures),
        border_alpha_max=max(m['border_alpha_max'] for m in measures),
        final_alpha_max=measures[-1]['alpha_max']),indent=2),encoding='utf-8')
    if args.flipbook:
        sys.path.insert(0,str(ROOT/'tools/vfx-flipbook'))
        from vfxflip import atlas
        folder = out/'flipbook'
        folder.mkdir(exist_ok=True)
        f = frames.astype(np.float32)/255
        cols, rows = atlas.grid(len(f),512,512)
        wh = atlas.write_atlas(f,cols,rows,folder/'atlas.png')
        (folder/'atlas.prompt.txt').write_text(prompt,encoding='utf-8')
        (folder/'atlas.json').write_text(json.dumps(dict(frames=len(f), fps=24, cell=[512,512],
            columns=cols,rows=rows,size=wh,blend='straight-alpha',order='row-major',loop=False),indent=2))
    print(out.name, 'khung',len(files),'lề',min(m['margin_px'] for m in measures),'alpha mép',max(m['border_alpha_max'] for m in measures))


if __name__ == '__main__':
    main()
