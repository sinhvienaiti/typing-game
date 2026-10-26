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

"""Record append-only refinements and the Vietnamese delivery report after visual QA."""
import json
from pathlib import Path
import tempfile
from normalize import ROOT, key, metrics
from normalize_dragon import ART, REVIEW, MANIFEST, digest, provenance, rel

def main():
    original = json.loads(MANIFEST.read_text(encoding='utf-8'))
    extra = []
    review = []
    work = ROOT / '.tmp'
    with tempfile.TemporaryDirectory(prefix='report-', dir=work) as directory:
        tmp = Path(directory)
        for out in sorted((ART / 'decals/pine-river').glob('*.clean.alpha.png')):
            src = out.with_name(out.name.replace('.clean.alpha.png', '.png'))
            commands = [f'bash tools/art-normalize/key-alpha.sh games/dragon-hold/art-src/{rel(src)} "$WORK/key.png" --fuzz 20%', f'bash tools/art-normalize/pad-margin.sh "$WORK/key.png" games/dragon-hold/art-src/{rel(out)} --size 1024 --margin 9.375% --grid 2x2']
            cut = tmp / 'cut.png'
            key(src, cut, fuzz=0.2)
            before = metrics(src)
            before['foreground'] = metrics(cut, '2x2')['margins_ltrb']
            extra.append({'kind': 'decal', 'input': rel(src), 'output': rel(out), 'commands': commands, 'before': before, 'after': metrics(out, '2x2'), 'selected': True})
            provenance(out, src, commands)
        src = ART / 'backdrops/pine-river-far.png'
        out = src.with_name('pine-river-far.soft.seamless.png')
        commands = [f'bash tools/art-normalize/seamless.sh games/dragon-hold/art-src/{rel(src)} games/dragon-hold/art-src/{rel(out)} --axis x --blend 12%']
        extra.append({'kind': 'backdrop', 'input': rel(src), 'output': rel(out), 'commands': commands, 'before': metrics(src), 'after': metrics(out), 'selected': True, 'algorithm': 'Trộn cặp dải mép đối xứng, cosine; bản công cụ cuối.'})
        provenance(out, src, commands)
        for out in sorted(REVIEW.glob('*.png')):
            if out.with_suffix('.prompt.txt').exists():
                continue
            if out.name == 'pine-river-far.soft.seam.png':
                command = 'bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/backdrops/pine-river-far.soft.seamless.png games/dragon-hold/art-src/_review/pine-river-far.soft.seam.png --axis x'
            elif out.name.startswith('icons-'):
                tile = int(out.name.split('-')[1].split('.')[0])
                source_size = 256 if tile == 256 else 64
                sources = sorted((ART / 'icons/normalized').glob(f'*.{source_size}.png'))
                command = 'bash tools/art-normalize/sheet.sh games/dragon-hold/art-src/' + rel(out) + ' ' + ' '.join(('games/dragon-hold/art-src/' + rel(p) for p in sources)) + f' --bg checker --tile {tile}'
            else:
                selected = sorted((ART / 'decals/pine-river').glob('*.clean.alpha.png'))
                if out.name == 'decals-clean.dark.png':
                    selected = [p for p in selected if p.stem in ('flower-clusters.clean.alpha', 'forest-litter.clean.alpha')]
                elif 'archive' in out.name:
                    selected = [p for p in selected if '.v1.' in p.name]
                else:
                    selected = [p for p in selected if '.v1.' not in p.name]
                command = 'bash tools/art-normalize/sheet.sh games/dragon-hold/art-src/' + rel(out) + ' ' + ' '.join(('games/dragon-hold/art-src/' + rel(p) for p in selected)) + ' --bg dark --tile 512'
            provenance(out, None, [command])
            review.append({'output': rel(out), 'commands': [command]})
        supplementary = REVIEW / 'normalize-refinements.json'
        if not not supplementary.exists():
            raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
        write_text_new(supplementary, json.dumps({'records': extra, 'review': review, 'initial_backdrop_algorithm': 'Bù chênh lệch hai cột biên bằng cosine; đã loại vì tạo vệt ngang. Lệnh seamless hiện tại đã thay bằng trộn dải mép.'}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    records = original['records'] + extra
    if not all(((ART / p).exists() and digest(ART / p) == sha for p, sha in original['original_sha256'].items())):
        raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
    for r in records:
        a = r['after']
        if r['kind'] == 'decal':
            if not (a['size'] == [1024, 1024] and a['corner_alpha'] == [0] * 4):
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
            if not min((min(v) for v in a['margins_ltrb'])) >= 48:
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
        elif r['kind'] == 'icon':
            if not (a['size'][0] in (256, 64) and a['size'][0] == a['size'][1] and (a['corner_alpha'] == [0] * 4)):
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
        elif r['kind'] == 'tripo':
            if not 'x'.join(map(str, a['size'])) == r['requested_size']:
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
            if not (a['corners'] == ['#E6E6E6'] * 4 and a['corner_alpha'] == [255] * 4):
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
            if not all((v >= math.ceil(a['size'][i % 2] * 0.08) for i, v in enumerate(a['foreground'][0]))):
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
        elif r['kind'] == 'backdrop':
            if not a['seams']['x']['pass']:
                raise ValueError('Kiểm tra hồ sơ 012 không đạt.')

    def path(p):
        return f'[`{p}`](../{p})'

    def dims(a):
        return '×'.join(map(str, a['size']))

    def minimum(m):
        return '/'.join((str(min(v)) for v in m))

    def four(c):
        return ' / '.join(c)
    lines = ['# Rồng Giữ Ải — Phiếu 012 · chuẩn hóa ảnh bằng ImageMagick', '', 'Ngày 25/10/2026. Đã tạo công cụ dùng chung tại [`tools/art-normalize`](../../../../tools/art-normalize/README.md), chạy `test.sh` đạt và mở các tấm xem nhanh trước khi ghi nhận kết quả. Không gọi `image_gen`, không chạy Tripo, không thay ảnh runtime. Mọi ảnh nguồn, bản `.v1`, prompt và README cũ giữ nguyên SHA-256.', '', '**Bản nên dùng để xem tiếp:** 8 atlas `.clean.alpha.png` (4 hiện tại, 4 lưu đợt 1–3), phông `pine-river-far.soft.seamless.png`, 40 PNG icon tại `icons/normalized/`, 32 PNG `.tripo.png`. Các bản `.alpha.png` và `pine-river-far.seamless.png` là lượt đầu còn hạn chế, giữ riêng để đối chiếu; không ghi đè chúng sau khi phát hiện lỗi khi xem.', '', '## 1. Cách đo và lệnh', '', '- Khổ đo trực tiếp từ PNG. RGB góc theo thứ tự trên trái / trên phải / dưới trái / dưới phải; góc alpha 0 là trong suốt, 255 là đục. RGB bên dưới alpha 0 không phải màu nền nhìn thấy.', '- Lề tính trên mọi pixel alpha > 0. “Lề ô” là giá trị nhỏ nhất trong trái/trên/phải/dưới, theo thứ tự bốn phần tư. Lề trước lấy từ mask cùng ngưỡng của lần xử lý, tại khổ nguồn; không so trực tiếp với ngưỡng màu khác của báo cáo cũ. Với Tripo, lề sau là hộp mọi pixel khác đúng `#E6E6E6`, gồm cả mép khử răng cưa.', '- Lề atlas dùng **9,375% của ô 512 = 48 px**, chặt hơn 8% (= 41 px làm tròn). Công cụ còn dự trữ mép lọc nên số thực tế thường từ 50 px.', '- Sai lệch mép là MAE RGB giữa cột đầu–cuối, thang 0–255. Phông chỉ cần trục x; sai lệch trên–dưới không phải điều kiện đạt của phông ngang.', '', 'Các ký hiệu dưới đây là lệnh đã chạy, trong đó `IN` và `OUT` là file ở đúng hàng; tiền tố đường dẫn là `games/dragon-hold/art-src/`. `WORK` là thư mục tạm mới trong `tools/art-normalize/.tmp/`. Lệnh đầy đủ, số đo đủ bốn phía và hash gốc nằm trong [manifest lần đầu](../_review/normalize-metrics.json) và [manifest bản chọn](../_review/normalize-refinements.json).', '', '```bash', '# K12/P hoặc K20/P: ngưỡng 12% hoặc 20% đúng theo ký hiệu của hàng', 'bash tools/art-normalize/key-alpha.sh "$IN" "$WORK/key.png" --fuzz 12%', 'bash tools/art-normalize/key-alpha.sh "$IN" "$WORK/key.png" --fuzz 20%', 'bash tools/art-normalize/pad-margin.sh "$WORK/key.png" "$OUT" --size 1024 --margin 9.375% --grid 2x2', '# S: bản chọn dùng công thức trộn dải mép của công cụ cuối', 'bash tools/art-normalize/seamless.sh "$IN" "$OUT" --axis x --blend 12%', '# I: sinh đồng thời hai file 256 và 64', 'bash tools/art-normalize/icon.sh "$IN" games/dragon-hold/art-src/icons/normalized --sizes 256,64', '# F: SIZE lấy từ cột khổ ra của từng hàng', 'bash tools/art-normalize/flat-bg.sh "$IN" "$OUT" --bg "#E6E6E6" --size "$SIZE"', '```', '', '## 2. Decal D1–D4 và bản lưu đợt 1–3', '', 'Tất cả file ra trong bảng có khổ **1024×1024, alpha góc 0/0/0/0**. Nguồn đều 1254×1254, alpha góc 255/255/255/255. Bản `K20/P` đã xem trên nền tối: khe lá/kim/cành sạch màu khóa hơn `K12/P`; các chi tiết mảnh nhất vẫn có thể hao khoảng 1 px vì mask lùi mép. Không sửa vật phụ hay biến hoa nổi khối thành tranh phẳng.', '', '| File vào | File ra | Lệnh | Lề ô trước → sau (px) | RGB góc nguồn | Đạt hay chưa |', '|---|---|---|---|---|---|']
    for r in [r for r in records if r['kind'] == 'decal']:
        chosen = r.get('selected', False)
        status = 'Đạt alpha/khổ/lề; bản chọn.' if chosen else 'Đạt alpha/khổ/lề; bản đối chiếu, còn đốm/viền khóa ở chi tiết nhỏ.'
        lines.append(f"""| {path(r['input'])} | {path(r['output'])} | {('K20/P' if chosen else 'K12/P')} | {minimum(r['before']['foreground'])} → {minimum(r['after']['margins_ltrb'])} | {four(r['before']['corners'])} | {status} |""")
    lines += ['', '## 3. Phông xa B1', '', '| File vào | File ra | Lệnh | Khổ trước → sau | MAE mép x trước → sau | RGB góc trước → sau | Đạt hay chưa |', '|---|---|---|---|---|---|---|']
    for r in [r for r in records if r['kind'] == 'backdrop']:
        status = 'Đạt mép pixel; đã xem ghép, bản chọn. Dải trộn có bố cục gần đối xứng, cần duyệt mỹ thuật.' if r.get('selected') else 'Chưa đạt cảm quan: còn vệt ngang do công thức bù cột biên ban đầu; giữ để đối chiếu.'
        lines.append(f"""| {path(r['input'])} | {path(r['output'])} | S{(' (công thức đầu)' if not r.get('selected') else '')} | {dims(r['before'])} → {dims(r['after'])} | {r['before']['seam_rgb_mae_255']['x']:.4f} → {r['after']['seam_rgb_mae_255']['x']:.4f} | {four(r['before']['corners'])} → {four(r['after']['corners'])} | {status} |""")
    lines += ['', 'Bản ghép đúng đường dẫn yêu cầu: [lượt đầu 2×1](../_review/pine-river-far.seam.png); bản ghép để duyệt bản chọn: [bản mềm 2×1](../_review/pine-river-far.soft.seam.png), 3072×1024. [Bản nguồn ghép 2×1](../_review/pine-river-far.before.seam.png) để đối chiếu. Mỗi bản chạy `seam-check.sh IN OUT --axis x`.', '', '## 4. Hai mươi icon đợt 4–5', '', 'Nguồn 1254×1254, chưa có alpha. Mỗi hàng xuất đủ **256×256 và 64×64**, alpha bốn góc 0 ở cả hai cỡ; lệnh I. Ảnh 32 px là cỡ hiển thị trong sheet, lấy từ PNG 64 rồi thu bằng ImageMagick; không bổ sung một bộ asset 32 px ngoài yêu cầu.', '', '| File vào | File ra 256 / 64 | Lệnh | Lề trước → 256 / 64 (px) | RGB góc nguồn | Đạt hay chưa |', '|---|---|---|---|---|---|']
    icons = [r for r in records if r['kind'] == 'icon']
    for r in icons[::2]:
        other = next((v for v in icons if v['input'] == r['input'] and v['after']['size'][0] == 64))
        lines.append(f"""| {path(r['input'])} | {path(r['output'])} / {path(other['output'])} | I | {minimum(r['before']['foreground'])} → {minimum(r['after']['margins_ltrb'])} / {minimum(other['after']['margins_ltrb'])} | {four(r['before']['corners'])} | Đạt alpha/khổ/lề; hình và màu xem §7. |""")
    lines += ['', '## 5. Ba mươi hai ảnh nguồn Tripo', '', 'Khổ ra lấy từ các bảng ảnh trong `01-creatures.md`, `02-allies-traps.md`, `03-pine-river-props.md`; gồm cả hai góc của sáu sinh vật, tướng và lính, cùng bẫy, nhà và 12 prop. Không xử lý mẫu so sánh HT-A/HT-B trong `refs/` vì README nguồn ghi không gửi Tripo.', '', 'Tất cả file ra có **bốn góc đúng `#E6E6E6`, alpha góc 255**, nền ngoài vật phẳng đúng mã. Chỉ trim, đổi cỡ đồng tỉ lệ, đặt giữa, xử lý dải mép và ghép nền; không nắn tư thế, đổi màu thân hay vẽ lại vật. Đã mở các sheet trước/sau; chưa thấy hỏng mép lớn khiến phải bỏ toàn ảnh. Các nguồn nhạt màu như sừng/đá và lỗ kín giữa chi có thể còn xám gốc, cần xem nguyên cỡ trước khi gửi Tripo.', '', '| File vào | File ra | Lệnh | Khổ trước → sau | Lề nhỏ nhất trước → sau (px) | RGB bốn góc nguồn → ra | Đạt hay chưa |', '|---|---|---|---|---|---|---|']
    for r in [r for r in records if r['kind'] == 'tripo']:
        problem = any((v in r['input'] for v in ('thorn-wasp-side', 'moss-banner', 'moss-warden')))
        status = 'Đạt hậu kỳ; chưa đạt hình/rig, xem §7.' if problem else 'Đạt hậu kỳ; cần duyệt hình trước Tripo.'
        lines.append(f"""| {path(r['input'])} | {path(r['output'])} | F | {dims(r['before'])} → {dims(r['after'])} | {minimum(r['before']['foreground'])} → {minimum(r['after']['foreground'])} | {four(r['before']['corners'])} → #E6E6E6 ×4 | {status} |""")
    lines += ['', '## 6. Ảnh xem nhanh và kiểm tra', '', '- Decal hiện tại: [bản chọn trên nền tối](../_review/decals-selected.dark.png); bản lưu đợt 1–3: [bản chọn trên nền tối](../_review/decals-archive-selected.dark.png). Các sheet `decals-current.*`, `decals-archive.checker.png` giữ lượt đầu; `decals-clean.dark.png` so hai tấm D2/D3 ở ngưỡng cao.', '- Icon: đủ 9 sheet `icons-256`, `icons-64`, `icons-32`, mỗi cỡ có `.dark.png`, `.light.png`, `.checker.png`. Đã mở cả 9. Ba sheet caro đầu có nhãn thiếu tương phản, đã bổ sung `.labeled.checker.png` cho cả ba cỡ và mở lại; nên dùng ba bản có nhãn rõ này. Cỡ 32 còn đọc được các nhóm dáng, I03/I12 vẫn mất chi tiết lưới/đầu rồng và cần chủ dự án duyệt.', '- Tripo: đủ 12 sheet `tripo-{enemies,generals,units,houses,traps,props}.{input,output}.png`. Đã mở trước/sau cho cả sáu nhóm; kiểm thêm nguyên ảnh wasp-side và đá kê suối.', '- Test cuối: `wsl -e bash /mnt/d/typing-game/tools/art-normalize/test.sh` **đạt** sau khi sửa công thức trộn mép. Bộ kiểm bàn giao xác nhận khổ, alpha/lề atlas, nền/lề Tripo, MAE phông và hash mọi file gốc.', '- Mỗi PNG dẫn xuất có `.prompt.txt` cạnh ảnh. Prompt nguồn hiện tại chép nguyên văn; lệnh xử lý ở manifest. Bản `.v1` thiếu prompt riêng từ trước nên file kèm ghi đúng giới hạn này, không dùng prompt mới làm bằng chứng cho prompt cũ. Sheet có công thức ghép, không có prompt sinh ảnh.', '', '## 7. Lỗi hình còn phải sinh lại và phần chủ dự án nên xem', '', '| Ảnh / nhóm | Lỗi nằm trong hình, hậu kỳ chưa sửa | Việc tiếp theo |', '|---|---|---|', '| E01-S · `enemies/thorn-wasp-side.png` | Vẫn thấy toàn mặt cánh, cánh chéo sau; không phải cạnh cánh của góc Left. | Cần sinh lại góc cánh bằng `image_gen` theo ảnh chính trước khi dùng Multiview. |', '| G01-F/B · `generals/moss-banner*.png` | Khuỷu tay cầm cờ gập; bản sau kế thừa, còn vị trí vỏ phụ cần đối chiếu. | Cần sinh lại tư thế rig ở bản trước rồi đồng bộ bản sau. |', '| U1-F/B · `units/moss-warden*.png` | Tay khiên gập/khuất; bản sau vẫn thấy mặt trang trí bên ngoài của khiên. | Cần sinh lại tư thế và mặt trong khiên; không dùng cặp này như đã duyệt rig. |', '| E25-S/F · `thorn-ant*.png` | Đã thấy sáu chân theo Phiếu 006; góc ngang còn xiên và mắt có đồng tử dọc. | Chủ dự án xem lại góc/mắt và sự khớp hai góc trước khi quyết định sinh lại. |', '| D2/D4, D1/D3 | D2 còn cuống/đá/rêu ngoài ý đồ phẳng; D4 còn cây/đá và cảm giác nổi khối; D1 có mảnh đất rời, D3 có chi tiết rất mảnh. | Nếu cần đạt toàn prompt hình gốc, phải sinh lại hình; chuẩn hóa chỉ giải quyết nền/khổ/lề. |', '| Icon I07–I12, I14, I20 | Màu coral còn đỏ; I14 còn lá; I20 có vòng nhỏ. I03/I12 khó đọc chi tiết ở 32 px. | Duyệt màu và khả năng đọc trên gỗ tối/giấy kem; muốn đổi thiết kế phải sinh lại. |', '| B1 | Bản mềm khớp mép nhưng dải trộn gần đối xứng, cảnh vẫn nhiều cây/chi tiết; chưa xác nhận sống núi đúng 62%. | Xem ghép nguyên cỡ; phê duyệt mỹ thuật riêng trước khi dùng làm phông runtime. |', '', '**Bỏ qua và lý do:** không sinh lại ảnh trong phiếu hậu kỳ này; không tạo âm thanh/model, không chạy Tripo hoặc sửa runtime. Không xử lý ô đất T1–T8 vì danh sách chạy của mục 2 chỉ yêu cầu decal, phông, icon và nguồn Tripo; công cụ `--axis xy` đã được kiểm bằng ảnh giả để dùng cho ô đất ở phiếu sau. `refs/`, `2d/samples/` và các nguồn `.v1` sinh vật/lính giữ nguyên vì là mẫu so sánh/lưu trữ, không phải bản chọn gửi Tripo. Không có ảnh Tripo nào bị bỏ do tách nền hỏng mép lớn khi xem sheet; giới hạn mép nhạt và lỗ kín đã nêu ở §5.', '', '**Chủ dự án ưu tiên xem:** bản phông mềm ghép 2×1; D2/D3/D4 bản `.clean.alpha.png`; I03/I12 ở 32 px; cặp G01/U1 và góc cánh E01-S. Mức “đạt hậu kỳ” trong bảng không thay phê duyệt hình, rig hay chất lượng model.', '']
    report = ART / '2d/README-normalize.md'
    if not not report.exists():
        raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
    write_text_new(report, '\n'.join(lines), encoding='utf-8')
    newfiles = [p for p in ART.rglob('*') if p.is_file() and rel(p) not in original['original_sha256']]
    verification = REVIEW / 'normalize-verification.json'
    if not not verification.exists():
        raise ValueError('Kiểm tra hồ sơ 012 không đạt.')
    write_text_new(verification, json.dumps({'original_file_count': len(original['original_sha256']), 'original_sha256_unchanged': True, 'record_count': len(records), 'test': 'Đạt test.sh sau sửa seamless', 'new_files_sha256': {rel(p): digest(p) for p in newfiles}}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f"""Đạt kiểm bàn giao: {len(records)} bản xử lý; giữ nguyên {len(original['original_sha256'])} file gốc. Báo cáo: {report}""")
if __name__ == '__main__':
    raise SystemExit('Hồ sơ Phiếu 012 đã khóa; dùng rebuild-012d.sh cho lô sửa.')
