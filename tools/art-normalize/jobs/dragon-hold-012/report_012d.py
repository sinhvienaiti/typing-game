#!/usr/bin/env python3
"""Báo cáo số đo lô 012d; kiểm hash trước khi ghi."""
import fcntl
import os
from rebuild_012d import n, ART, STAGE, digest, require, tool_hashes, verify_originals, write_new, json_new
import json


def main():
    n.install_signal_handlers()
    lock=open(os.environ.get('ART_NORMALIZE_LOCK',n.WORK/'dragon-hold-publish.lock'),'a')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Runner đang chạy; chưa thể ghi báo cáo.')
    obj=json.loads((ART/'_review/normalize-metrics.json').read_text())
    require(obj['ticket']=='012d' and obj['tool_sha256']==tool_hashes(),'Sai lô/công cụ báo cáo.')
    verify_originals(obj)
    for name,sha in obj['artifacts_sha256'].items():require(digest(ART/name)==sha,f'Đầu ra đã đổi: {name}')
    for name,sha in obj['historical_sha256'].items():require(digest(ART/name)==sha,f'Lịch sử đã đổi: {name}')
    for name,archive in obj['archived_012c'].items():require(digest(ART/archive)==obj['before_sha256'][name],f'Sai bản lưu: {archive}')
    records=obj['records'];decals=[r for r in records if r['kind']=='decal'];tripo=[r for r in records if r['kind']=='tripo']
    lines=['# Rồng Giữ Ải · Phiếu 012d · sửa chuẩn hóa lần 3','',
           'Ngày 26/10/2026. Đã dựng lại từ ảnh gốc, không sinh ảnh AI mới. Claude cần phản biện lần 4 trước commit. Mã và bằng chứng kiểm thử: `tools/art-normalize/REVIEW-012d.md`.', '',
           f"Dựng {len(records)} ảnh xử lý: 8 decal, 1 phông, 40 icon, 32 Tripo. Giữ hash {len(obj['original_sha256'])} file gốc; lưu {len(obj['archived_012c'])} dẫn xuất 012c thành `.rejected-012c`. Không sửa nội dung lịch sử 012/012b.", '',
           '## 1. Cách đo', '',
           'Trước: đo lại dẫn xuất 012c. Sau: đo ảnh 012d. Lề theo alpha >0. Bảo vệ màu/alpha nguồn tại bước key trước resize: toàn vùng ngoài nền/khóa đậm nở 5 px; test riêng kiểm cả vành 4–10 px và ranh sơn khử răng cưa. Khóa đậm được xem là nền theo connected (túi ≥64 px) hoặc global (mọi điểm phù hợp), kể cả sơn cùng sắc khóa. Đếm riêng số điểm xa nền sáng bị xóa hoặc hạ alpha; không coi 0 khóa dư là bằng chứng giữ sơn.', '',
           'D1/D3 bật `--no-key-hue`: kẹp sắc khóa ở viền mềm và phần trong có chênh >50; số đổi hợp lệ ghi riêng. D2/D4 giữ chế độ bảo vệ phần trong. Nền trung tính chỉ nhận điểm có chênh kênh ≤6 để giữ highlight lavender. File Tripo chọn khổ chuẩn gần nhất theo log tỉ lệ vật và không phóng to.', '',
           '## 2. Decal', '',
           '| File | Khóa vừa trong lòng (>40) trước → sau | Viền khóa (>25) trước → sau | Bán trong suốt lòng (9–249) trước → sau | RGB/alpha đổi ngoài quy tắc | Đổi sắc được phép | Khóa xa nền sáng: tổng/xóa/alpha 9–249 |',
           '|---|---|---|---|---|---|---|']
    for r in decals:
        b,a=r['before']['residue'],r['after']['residue'];p=r['after']['interior_preservation']
        lines.append(f"| `{r['output']}` | {b['moderate_key_interior']} → {a['moderate_key_interior']} | {b['key_fringe']} → {a['key_fringe']} | {b['interior_semitransparent']} → {a['interior_semitransparent']} | {p['rgb_changed']}/{p['alpha_changed']} trên {p['pixels']} | {p['allowed_hue_changes']} | {p['strong_key_away_from_bright']}/{p['strong_key_removed']}/{p['strong_key_partial']} |")
    bd=next(r for r in records if r['kind']=='backdrop');b=bd['before']['seams']['x'];a=bd['after']['seams']['x']
    lines+=['','## 3. B1','',
            f"Khổ {'×'.join(map(str,bd['before']['size']))} → {'×'.join(map(str,bd['after']['size']))}; chi tiết cửa sổ so đúng cột nguồn {b['band_detail_source_ratio']} → {a['band_detail_source_ratio']}; sai số sọc so nguồn {b['row_source_residual']} → {a['row_source_residual']}; chốt đường nối {b['criteria'].get('cut_continuity')} → {a['criteria'].get('cut_continuity')}.", '',
            'Đường nối từng hàng nằm trong PNG (`art-normalize-seam`) và manifest. Ảnh 1:1 hàng 0–600: [trước](../_review/b1-cut-before-012d.png), [sau](../_review/b1-cut-after-012d.png). Ảnh xem mép: [ghép](../_review/pine-river-far.seam.png). Cần xem cả đường nối trong ô và mép lặp.', '',
            '## 4. Icon', '', 'Dựng lại đủ 40 icon vì key thay đổi. Xem sheet 256/64/32 px trên tối, sáng và caro. Giữ màu/alpha phần trong; viền sơn tối không được làm sáng bằng trung bình hàng xóm.', '',
            '## 5. Tripo', '',
            'Lõi túi: bỏ vành kề vật 1 px; túi sai E6 ≥64 px và >5% thành phần phải trượt. Đây là chốt nền, không phải duyệt thiết kế nguồn.', '',
            '| File | Khổ trước → sau | Scale trước → sau | Lõi túi sai ≥64 trước → sau | Highlight màu gần nền: nguồn/xóa ở key | Giống byte 012b / 012c |', '|---|---|---|---|---|---|']
    identical_b=[];identical_c=[]
    for r in tripo:
        out=ART/r['output'];oldb=out.with_name(out.stem+'.rejected-012b'+out.suffix);oldc=out.with_name(out.stem+'.rejected-012c'+out.suffix)
        ib=oldb.is_file() and digest(out)==digest(oldb);ic=digest(out)==digest(oldc)
        if ib:identical_b.append(r['output'])
        if ic:identical_c.append(r['output'])
        b,a=r['before'],r['after']
        hc=a['highlight_check']
        lines.append(f"| `{r['output']}` | {b['size']} → {a['size']} | {b['subject_scale']} → {a['subject_scale']} | {b['residue']['enclosed_neutral_ge_64_pixels']} → {a['residue']['enclosed_neutral_ge_64_pixels']} | {hc['near_bg_colored_source']}/{hc['removed_at_key']} | {ib} / {ic} |")
    lines+=['',f'Giống byte bản 012b: {len(identical_b)}/32; giống 012c: {len(identical_c)}/32. Các dòng True ở bảng chỉ thay nhãn do chốt/đo, không có thay đổi pixel.', '',
            '## 6. Kiểm tra và bàn giao','']
    for name,result in obj['validation'].items():lines.append(f"- `{name}`: mã thoát {result['exit_code']}; hash `{result['sha256']}`.")
    lines+=['', 'Manifest [normalize-metrics.json](../_review/normalize-metrics.json) ghi argv/hash/số đo. Sidecar `.prompt.txt` ghi phép hậu kỳ và prompt nguồn nguyên văn khi có; không thay prompt thiếu bằng prompt bản khác.', '',
            'Bỏ qua: không sửa ảnh gốc, art-src/3d, runtime, model, âm thanh, Tu Tiên, game docs khác; không chạy Git hoặc build/test game. Thiết kế nguồn/rig và khả năng đọc icon vẫn cần chủ dự án xem. Claude phản biện lần 4 trước commit.', '']
    report=ART/'2d/README-normalize.md';verification=ART/'_review/normalize-verification.json'
    write_new(report,'\n'.join(lines))
    json_new(verification,{'ticket':'012d','original_sha256_unchanged':True,'record_count':len(records),
        'new_files_sha256':{**obj['artifacts_sha256'],'2d/README-normalize.md':digest(report),'_review/normalize-metrics.json':digest(ART/'_review/normalize-metrics.json')},
        'validation':obj['validation']})


if __name__=='__main__':main()
