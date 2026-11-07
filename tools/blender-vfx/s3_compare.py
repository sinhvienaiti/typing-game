"""S3-3: so nguồn đã có, không render Blender, không sửa hay giả lập host."""
import hashlib
import json
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / '.local/s3/compare-S3-3'
ART = ROOT / 'games/immortality-cultivation/art-src/lab'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
FRACTIONS = [0, .1, .25, .45, .7, 1]
BACKGROUNDS = {'light': (205, 204, 195), 'dark': (8, 11, 17)}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save_image(im, path, recipe):
    im.save(path, quality=94)
    path.with_suffix('.prompt.txt').write_text(recipe + '\n', encoding='utf-8')


def metrics(ims, additive=False):
    rows = []
    corners = []
    for im in ims:
        a = np.asarray(im)
        n = max(1, round(im.width*.05))
        corners.extend([a[:n, :n].reshape(-1, 4), a[:n, -n:].reshape(-1, 4), a[-n:, :n].reshape(-1, 4), a[-n:, -n:].reshape(-1, 4)])
        mask = a[..., :3].max(2) if additive else a[..., 3]
        y, x = np.where(mask > 2)
        yc, xc = np.where(mask >= 128)
        edge = np.concatenate([mask[0], mask[-1], mask[:, 0], mask[:, -1]])
        margin = lambda xx, yy: int(min(xx.min(), yy.min(), im.width-1-xx.max(), im.height-1-yy.max())) if len(xx) else None
        rows.append(dict(bbox=[int(x.min()), int(y.min()), int(x.max()+1), int(y.max()+1)] if len(x) else None,
                         margin=margin(x, y), core_margin=margin(xc, yc), edge_max=int(edge.max()), maximum=int(mask.max()),
                         pixel_sha256=hashlib.sha256(a.tobytes()).hexdigest()))
    boxes = [r['bbox'] for r in rows if r['bbox']]
    union = [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]
    return dict(frames=rows, count=len(rows), unique=len({r['pixel_sha256'] for r in rows}),
                minimum_margin=min(r['margin'] for r in rows if r['margin'] is not None),
                minimum_core_margin=min(r['core_margin'] for r in rows if r['core_margin'] is not None),
                maximum_edge=max(r['edge_max'] for r in rows), final_maximum=rows[-1]['maximum'],
                corner_5pct_p99_rgba=np.percentile(np.concatenate(corners), 99, axis=0).tolist(),
                union_bbox=union, maximum_width=max(b[2]-b[0] for b in boxes),
                mask_kind='max RGB cho additive' if additive else 'alpha thật')


def tile(im, stats, bg, additive, smoke_tint=False):
    # Cùng bề ngang cực đại 96 px; giữ nguyên tỷ lệ và chuyển động trong mỗi nguồn.
    scale = 96 / stats['maximum_width']
    box = stats['union_bbox']
    center = ((box[0]+box[2])/2, (box[1]+box[3])/2)
    size = (round(im.width*scale), round(im.height*scale))
    arr = np.array(im)
    if smoke_tint:
        # Chỉ hiển thị matte atlas với màu mực, KHÔNG gọi đây là shader smoke của host.
        arr[..., :3] = (12, 13, 17)
    resized = Image.fromarray(arr).resize(size, Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (176, 176), (0, 0, 0, 0))
    canvas.paste(resized, (round(88-center[0]*scale), round(88-center[1]*scale)))
    a = np.asarray(canvas, dtype=np.float32)
    ground = np.empty((176, 176, 3), dtype=np.float32)
    ground[:] = bg
    if additive:
        result = ground + a[..., :3] * (1 if not smoke_tint else a[..., 3:4]/255)
    else:
        result = ground*(1-a[..., 3:4]/255) + a[..., :3]*a[..., 3:4]/255
    return Image.fromarray(np.clip(np.round(result), 0, 255).astype('uint8'))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'ABOUT.md').write_text('purpose: S3-3, so hai nguồn Blender với take Firefly trong manifest\nmade-by: Codex\ndoc: docs/work/codex-lanes/lane-S3-blender.md\ndelete-when: Anh duyệt và không còn cần bằng chứng so nguồn\n', encoding='utf-8')
    font = ImageFont.truetype(FONT, 14)
    small = ImageFont.truetype(FONT, 12)
    manifest_path = ART/'vfx/beast/manifest.json'
    manifest = json.loads(manifest_path.read_text())['flipbooks']
    report = {'scope': 'So nguồn offline, không chứng minh cảnh host hoặc chất lượng tầng B', 'manifest_sha256': sha(manifest_path), 'jobs': {}}
    for job, version in [('beast-hit-spark-burst', 'v2'), ('beast-death-ink-smoke', 'v3')]:
        smoke = 'smoke' in job
        out = OUT/job
        out.mkdir(exist_ok=True)
        entry = manifest[job]
        atlas_path = ART/'vfx/beast'/entry['file']
        meta_path = ART/'vfx/beast'/entry['json']
        atlas_meta = json.loads(meta_path.read_text())
        atlas = Image.open(atlas_path).convert('RGBA')
        cw, ch = entry['cell']
        firefly = [atlas.crop((i%entry['cols']*cw, i//entry['cols']*ch, (i%entry['cols']+1)*cw, (i//entry['cols']+1)*ch)) for i in range(entry['frames'])]
        blender_dir = ART/'vfx-redo-2026-11-07/blender'/job/version
        blender = [Image.open(p).convert('RGBA') for p in sorted((blender_dir/'rgba').glob('*.png'))]
        bmeta = json.loads((blender_dir/'render.json').read_text())
        bs, fs = metrics(blender), metrics(firefly, additive=not smoke)
        recipe = (f'S3-3: ghép ảnh nguồn có sẵn, không AI generation. Blender: {blender_dir.relative_to(ROOT)}, '
                  f'Firefly take: {entry["source"]}; atlas: {atlas_path.relative_to(ROOT)}. '
                  'Hai phía cùng bề ngang hình cực đại 96 px, cùng canvas 176 px, không kéo méo, không đổi màu Blender. '
                  'Khói Firefly: alpha atlas thật, tô mực RGB(12,13,17) đúng vai trò, chưa áp shader smoke/noise/bloom/host. '
                  'Tia Firefly: cộng RGB trên nền; Blender: ghép alpha thật. Ghép sRGB để kiểm nguồn, không mô phỏng pipeline màu GPU. '
                  f'Sáu mốc tỷ lệ vòng đời {FRACTIONS}, có nhãn thời gian gốc; không phải cùng thời gian tuyệt đối. '
                  'Cỡ 96 px là chuẩn so nguồn, khói tương ứng 1,5× thân quy ước 64 px; chưa đo quái thật. '
                  'Font /System/Library/Fonts/Supplemental/Arial.ttf. Script tools/blender-vfx/s3_compare.py.')
        sources = [(blender, bs, bmeta['fps'], False, False, 'Blender '+version), (firefly, fs, entry['fps'], not smoke, smoke, 'Firefly take1 / atlas')]
        ids = [[round(f*(len(ims)-1)) for f in FRACTIONS] for ims, *_ in sources]
        for bgname, bg in BACKGROUNDS.items():
            sheet = Image.new('RGB', (1088, 462), (29, 33, 40))
            d = ImageDraw.Draw(sheet)
            d.text((8, 6), job+' · cùng bề ngang 96 px · nền '+bgname, font=font, fill='white')
            for side, (ims, stats, fps, add, tint, label) in enumerate(sources):
                d.text((8+side*544, 29), label, font=font, fill='white')
                for k, idx in enumerate(ids[side]):
                    x, y = 4+side*544+(k%3)*180, 54+(k//3)*200
                    sheet.paste(tile(ims[idx], stats, bg, add, tint), (x, y))
                    d.text((x+3, y+178), f'f{idx+1:02} · {idx/fps:.3f} s', font=small, fill='white')
            d.text((8, 451), 'So nguồn offline; chưa xác nhận cỡ và chuyển động trong host.', font=small, fill='white')
            save_image(sheet, out/f'compare-{bgname}.jpg', recipe+f' Nền {bg}. Khung {ids}.')
        # Hai đồng hồ gốc cùng chạy từ t=0, tắt sau cuối nguồn, không retime Firefly để che nhịp dài.
        video = out/'compare-real-time.mp4'
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '720x430', '-r', '48', '-i', '-', '-an', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', str(video)]
        duration = max(len(blender)/bmeta['fps'], len(firefly)/entry['fps'])+.4
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for tick in range(round(duration*48)):
            t = tick/48
            frame = Image.new('RGB', (720, 430), (29, 33, 40))
            d = ImageDraw.Draw(frame)
            d.text((8, 5), job+f' · t={t:.3f} s · tốc độ gốc', font=font, fill='white')
            for side, (ims, stats, fps, add, tint, label) in enumerate(sources):
                x = 8+side*360
                d.text((x, 28), label+f' · {fps:g} fps', font=font, fill='white')
                for row, bg in enumerate(BACKGROUNDS.values()):
                    # Giữ khung nguồn theo timestamp; không tạo thêm khung nguồn.
                    im = tile(ims[int(t*fps)], stats, bg, add, tint) if t < len(ims)/fps else Image.new('RGB', (176, 176), bg)
                    frame.paste(im, (x+84, 52+row*186))
            proc.stdin.write(frame.tobytes())
        proc.stdin.close()
        assert proc.wait() == 0
        video.with_suffix('.prompt.txt').write_text(recipe+'\nMP4 48 fps; đồng hồ tuyệt đối chung, giữ khung theo fps gốc, không nội suy, không retime; sau cuối mỗi nguồn để nền trống.\n', encoding='utf-8')
        source = ROOT/entry['source']
        # Sheet clip gốc giúp kiểm crop và nền, không dùng matte tự suy đoán.
        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(source), '-vf', 'scale=160:160', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], check=True, stdout=subprocess.PIPE)
        raw = np.frombuffer(decoded.stdout, dtype=np.uint8).reshape((-1, 160, 160, 3))
        rawids = [round(f*(len(raw)-1)) for f in FRACTIONS]
        rawsheet = Image.new('RGB', (492, 404), (29, 33, 40))
        d = ImageDraw.Draw(rawsheet)
        d.text((5, 5), 'Firefly take1 gốc · chưa matte / chưa crop', font=font, fill='white')
        for k, idx in enumerate(rawids):
            x, y = 4+(k%3)*164, 30+(k//3)*184
            rawsheet.paste(Image.fromarray(raw[idx]), (x, y))
            d.text((x+2, y+162), f'f{idx+1:03} · {idx/24:.3f} s', font=small, fill='white')
        save_image(rawsheet, out/'firefly-raw-sheet.jpg', recipe+f' Clip gốc thu toàn khung 160²; khung 0-based {rawids}; không ghép nền hay suy alpha.')
        corners = np.concatenate([raw[:, :8, :8].reshape(-1, 3), raw[:, :8, -8:].reshape(-1, 3), raw[:, -8:, :8].reshape(-1, 3), raw[:, -8:, -8:].reshape(-1, 3)])
        report['jobs'][job] = dict(blender=bs, firefly_atlas=fs, blender_fps=bmeta['fps'], firefly_fps=entry['fps'],
            blender_duration=len(blender)/bmeta['fps'], firefly_duration=len(firefly)/entry['fps'],
            selected_indices=ids, raw_indices=rawids, raw_frame_count=len(raw), raw_corner_p99=np.percentile(corners,99,axis=0).tolist(),
            source_sha256=sha(source), atlas_sha256=sha(atlas_path), atlas_meta_sha256=sha(meta_path),
            blender_render_sha256=sha(blender_dir/'render.json'), source=str(source.relative_to(ROOT)),
            manifest_use=entry['use'], packaging_notes=entry['notes'], maximum_display_width_px=96,
            real_host_size_verified=False, runtime_playback_observed=False,
            comparison_is_gpu_equivalent=False)
        print(job, 'Blender/Firefly margins', bs['minimum_margin'], fs['minimum_margin'], 'core', bs['minimum_core_margin'], fs['minimum_core_margin'], 'end', bs['final_maximum'], fs['final_maximum'], 'raw p99', report['jobs'][job]['raw_corner_p99'])
    (OUT/'metrics.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
