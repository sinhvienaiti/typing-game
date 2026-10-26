#!/usr/bin/env python3
# HỒ SƠ 012 ĐÃ KHÓA: không dùng để tái tạo ảnh bằng công cụ 012b.
import sys
import math
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

def write_text_new(path, text, encoding='utf-8'):
    with open(path, 'x', encoding=encoding) as output:
        output.write(text)

def write_bytes_new(path, data):
    with open(path, 'xb') as output:
        output.write(data)

"""Reproducible, append-only batch for ticket 012; no runtime integration."""
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import tempfile
from normalize import ROOT, bounds, dimensions, im, key, metrics, output_guard, rgba
REPO = ROOT.parent.parent
ART = REPO / 'games/dragon-hold/art-src'
REVIEW = ART / '_review'
MANIFEST = REVIEW / 'normalize-metrics.json'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rel(path):
    return str(path.relative_to(ART))

def run(command, *args):
    argv = ['bash', str(ROOT / f'{command}.sh'), *map(str, args)]
    result = subprocess.run(argv, check=True, stdout=subprocess.PIPE)
    return shlex.join(['bash', f'tools/art-normalize/{command}.sh', *[str(a.relative_to(REPO)) if isinstance(a, Path) and a.is_relative_to(REPO) else str(a) for a in args]])

def provenance(out, src, commands):
    prompt = out.with_suffix('.prompt.txt')
    if prompt.exists():
        raise ValueError(f'Từ chối ghi đè: {prompt}')
    original = src.with_suffix('.prompt.txt') if src else None
    if original and original.exists() and (not src.stem.endswith('.v1')):
        write_bytes_new(prompt, ('Dẫn xuất từ ' + str(src) + ' bằng ' + '\n'.join(commands) + '\nPrompt nguồn:\n').encode('utf-8') + original.read_bytes())
    else:
        write_text_new(prompt, 'Ảnh hậu kỳ bằng ImageMagick, không gọi image_gen.\n' + ('Prompt chính xác của bản .v1 chưa được lưu riêng; giữ tham chiếu ảnh gốc.\n' if src else '') + '\n'.join(commands) + '\n', encoding='utf-8')

def foreground_flat(path):
    w, h, data = rgba(path)
    for i in range(0, len(data), 4):
        data[i + 3] = 0 if data[i:i + 3] == bytes([230, 230, 230]) else 255
    x, y, bw, bh = bounds(w, h, data)
    return [x, y, w - x - bw, h - y - bh]

def main():
    if MANIFEST.exists():
        raise SystemExit('Đã có manifest; từ chối chạy đè. Dùng từng lệnh với tên ra mới.')
    REVIEW.mkdir(exist_ok=True)
    originals = {rel(p): digest(p) for p in ART.rglob('*') if p.is_file()}
    records = []
    review_records = []
    work = ROOT / '.tmp'
    work.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='dragon-', dir=work) as directory:
        tmp = Path(directory)
        decals = sorted((ART / 'decals/pine-river').glob('*.png'))
        decal_out = []
        for index, src in enumerate(decals):
            out = src.with_name(src.stem + '.alpha.png')
            cut = tmp / f'decal-{index}.png'
            commands = [run('key-alpha', src, cut), run('pad-margin', cut, out, '--size', '1024', '--margin', '9.375%', '--grid', '2x2')]
            before = metrics(src)
            before['foreground'] = metrics(cut, '2x2')['margins_ltrb']
            records.append({'kind': 'decal', 'input': rel(src), 'output': rel(out), 'commands': commands, 'before': before, 'after': metrics(out, '2x2')})
            provenance(out, src, commands)
            decal_out.append(out)
            print(f'Decal: {rel(out)}', flush=True)
        src = ART / 'backdrops/pine-river-far.png'
        out = src.with_name(src.stem + '.seamless.png')
        commands = [run('seamless', src, out, '--axis', 'x')]
        records.append({'kind': 'backdrop', 'input': rel(src), 'output': rel(out), 'commands': commands, 'before': metrics(src), 'after': metrics(out)})
        provenance(out, src, commands)
        for image, name in ((src, 'pine-river-far.before.seam.png'), (out, 'pine-river-far.seam.png')):
            review = REVIEW / name
            command = run('seam-check', image, review, '--axis', 'x')
            provenance(review, None, [command])
            review_records.append({'output': rel(review), 'commands': [command]})
        icons = sorted((ART / 'ui/icons').glob('*.png'))
        if not len(icons) == 20:
            raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
        for src in icons:
            outdir = ART / 'icons/normalized'
            command = run('icon', src, outdir, '--sizes', '256,64')
            cut = tmp / 'icon.png'
            key(src, cut)
            before = metrics(src)
            before['foreground'] = metrics(cut)['margins_ltrb']
            for s in (256, 64):
                out = outdir / f'{src.stem}.{s}.png'
                records.append({'kind': 'icon', 'input': rel(src), 'output': rel(out), 'commands': [command], 'before': before, 'after': metrics(out)})
                provenance(out, src, [command])
            print(f'Icon: {src.stem}', flush=True)
        specifications = {}
        for name in ('01-creatures.md', '02-allies-traps.md', '03-pine-river-props.md'):
            text = (REPO / 'docs/games/dragon-lane/art-requests/m0' / name).read_text(encoding='utf-8')
            for filename, width, height in re.findall('`([^`]+\\.png)`\\s*[·|]\\s*(\\d+)×(\\d+)', text):
                specifications[filename] = f'{width}x{height}'
        sources = sorted((p for group in ('enemies', 'generals', 'units', 'houses', 'traps', 'props') for p in (ART / group).rglob('*.png') if '.v1.' not in p.name))
        if not len(sources) == 32:
            raise ValueError(len(sources))
        for index, src in enumerate(sources):
            out = src.with_name(src.stem + '.tripo.png')
            requested = specifications[rel(src)]
            command = run('flat-bg', src, out, '--bg', '#E6E6E6', '--size', requested)
            cut = tmp / 'tripo-key.png'
            key(src, cut, fuzz=0.06)
            before = metrics(src)
            before['foreground'] = metrics(cut)['margins_ltrb']
            after = metrics(out)
            after['foreground'] = [foreground_flat(out)]
            records.append({'kind': 'tripo', 'input': rel(src), 'output': rel(out), 'commands': [command], 'requested_size': requested, 'before': before, 'after': after})
            provenance(out, src, [command])
            print(f'Tripo {index + 1}/32: {rel(out)}', flush=True)
        sheets = [('decals-current.checker.png', [p for p in decal_out if '.v1.' not in p.name], 'checker', 512), ('decals-archive.checker.png', [p for p in decal_out if '.v1.' in p.name], 'checker', 512), ('decals-current.dark.png', [p for p in decal_out if '.v1.' not in p.name], 'dark', 512)]
        for s in (256, 64, 32):
            for bg in ('dark', 'light', 'checker'):
                files = [ART / 'icons/normalized' / f'{p.stem}.{(256 if s == 256 else 64)}.png' for p in icons]
                sheets.append((f'icons-{s}.{bg}.png', files, bg, s))
        for group in ('enemies', 'generals', 'units', 'houses', 'traps', 'props'):
            groupfiles = [r for r in records if r['kind'] == 'tripo' and r['input'].startswith(group + '/')]
            for phase in ('input', 'output'):
                sheets.append((f'tripo-{group}.{phase}.png', [ART / r[phase] for r in groupfiles], 'light', 256))
        for name, files, bg, tile in sheets:
            out = REVIEW / name
            command = run('sheet', out, *files, '--bg', bg, '--tile', str(tile))
            provenance(out, None, [command])
            review_records.append({'output': rel(out), 'commands': [command]})
            print(f'Xem nhanh: {name}', flush=True)
        unchanged = all(((ART / p).exists() and digest(ART / p) == sha for p, sha in originals.items()))
        if not unchanged:
            raise ValueError('Ảnh hoặc tài liệu gốc bị thay đổi.')
        for r in records:
            r['commands'] = [c.replace(str(tmp.relative_to(REPO)), '"$WORK"') for c in r['commands']]
        write_text_new(MANIFEST, json.dumps({'original_sha256': originals, 'originals_unchanged': unchanged, 'records': records, 'review': review_records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Đã giữ nguyên {len(originals)} file gốc. Manifest: {MANIFEST}', flush=True)
if __name__ == '__main__':
    raise SystemExit('Hồ sơ Phiếu 012 đã khóa; dùng rebuild-012b.sh cho lô sửa.')
