#!/usr/bin/env python3
"""Kiểm hash bàn giao, ghi báo cáo tiếng Việt từ số đo thực của lô 012c."""
import fcntl
import json
import os
from rebuild_012c import ART, STAGE, n, digest, json_new, require, tool_hashes, verify_originals, write_new


def link(path):
    return f"[`{path}`](../{path})"


def margin(record):
    return "/".join(str(min(v)) for v in record["margins_ltrb_alpha_gt_0"])


def main():
    n.install_signal_handlers()
    lock=open(os.environ.get("ART_NORMALIZE_LOCK",n.WORK/"dragon-hold-publish.lock"),"a")
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit("Runner đang chạy; chưa thể ghi báo cáo.")
    manifest_path=ART/"_review/normalize-metrics.json"
    obj=json.loads(manifest_path.read_text())
    require(obj.get("ticket")=="012c","Chưa công bố lô 012c.")
    require(obj["tool_sha256"]==tool_hashes(),"Công cụ đã đổi sau lô.")
    verify_originals(obj)
    for path,sha in obj["artifacts_sha256"].items():require(digest(ART/path)==sha,f"Đầu ra đã đổi: {path}")
    for path,sha in obj["historical_sha256"].items():require(digest(ART/path)==sha,f"Lịch sử 012 đã đổi: {path}")
    for old,archive in obj["archived_012b"].items():require(digest(ART/archive)==obj["before_sha256"][old],f"Bản lưu 012b sai: {archive}")
    records=obj["records"]
    decals=[r for r in records if r["kind"]=="decal"]
    icons=[r for r in records if r["kind"]=="icon"]
    tripo=[r for r in records if r["kind"]=="tripo"]
    backdrop=next(r for r in records if r["kind"]=="backdrop")
    failed=[r["output"] for r in tripo if not r["after"]["pocket_gate"]]
    old_b=obj["evidence"]["backdrop_012b"]
    a=backdrop["after"]["seams"]["x"]
    counts={kind:sum(r["kind"]==kind for r in records) for kind in ("decal","icon","tripo","backdrop")}
    lines=["# Rồng Giữ Ải — Phiếu 012c · sửa chuẩn hóa lần 2", "",
           "Ngày 26/10/2026. Đối chiếu toàn bộ `merged.findings`, `merged.review012_status` và bốn bản phản biện 012b. "
           "Chi tiết sửa mã và test ở `tools/art-normalize/REVIEW-012c.md`.", "",
           f"Đã dựng lại **{len(records)} ảnh**: {counts['decal']} atlas decal, {counts['backdrop']} phông, {counts['icon']} icon và {counts['tripo']} nguồn Tripo. "
           f"Giữ nguyên SHA-256 **{len(obj['original_sha256'])} file gốc**, **{len(obj['historical_sha256'])} file lịch sử `.rejected-012`**; "
           f"lưu **{len(obj['archived_012b'])} dẫn xuất 012b** thành `.rejected-012b` và kiểm từng hash trước công bố.", "",
           "## 1. Cách đo và tái tạo", "",
           "- Số trước đo lại từ bản 012b tại tên bàn giao, số sau từ ảnh 012c. Lề dùng alpha >0; trim dùng alpha >8. "
           "Màu và alpha phần trong được so trực tiếp với nguồn ở bước key trước khi resize: vùng cách nền/khóa đậm trên 5 px. "
           "Giữ nguyên RGB và alpha 255 tại tất cả các pixel được kiểm; không dùng chốt xóa mọi màu trội khóa.",
           "- Khóa đậm: chênh kênh khóa >70% chênh nền, hoặc chênh >25% nền và >70% kênh lớn nhất (khóa bão hòa tối); alpha >8. Chỉ cho phép trong 4 px từ phần trong suốt. "
           "Màu tím nhạt/xanh rêu thật có thể trội kênh khóa; không đếm chúng là nền chỉ vì chênh >25.",
           "- Túi Tripo: thành phần gần nền trung tính, không nối biên; bỏ pixel kề vật trong 1 px trước đếm lõi sai E6. "
           "Cờ túi lớn cần lõi sai ≥64 px và trên 5% thành phần. Tổng gần nền ≠E6 vẫn được ghi để tra cứu, gồm cả viền mềm.",
           "- Chốt mép dùng cặp gương/đối chứng cùng khoảng cách 2k+1, cửa sổ trượt trên toàn dải overlap, "
           "chi tiết toàn ảnh so nguồn, độ lệch theo hàng ở hai dải mép so phần trong. Có `--reference` để phân biệt cấu trúc nguồn tự nhiên. "
           "Đây là chỉ số kiểm hỗ trợ, không thay duyệt ảnh nguyên cỡ.", "",
           f"SHA-256 `normalize.py`: `{obj['tool_sha256']['tools/art-normalize/normalize.py']}`. "
           "Manifest [normalize-metrics.json](../_review/normalize-metrics.json) chứa số đo, argv, lệnh tái tạo và hash mọi script Python/bash. "
           "Sidecar `.prompt.txt` ghi nguồn, lệnh thực tế, hash công cụ và prompt gốc nguyên văn khi có; không gán prompt bản khác cho `.v1`. "
           "Đây là hậu kỳ xác định; không sinh ảnh AI mới.", "",
           "## 2. Atlas decal", "",
           "Dùng khử loang có bảo vệ phần trong; ưu tiên matte từ màu vật lân cận, chỉ sửa vùng nền nở 3 px. "
           "Atlas giữ tên `.alpha.png`, bốn ô, khổ theo bảng dưới. Số bán trong suốt phần trong đo sau co mask vật 5 px.", "",
           "| File ra | Khổ | Khóa đậm xa mép trước → sau | Pixel bán trong suốt phần trong trước → sau | RGB/alpha nguồn bị đổi ở phần trong | Lề ô trước → sau |",
           "|---|---|---|---|---|---|"]
    for r in decals:
        b,after=r["before"],r["after"];pr=after["interior_preservation"]
        lines.append(f"| {link(r['output'])} | {'×'.join(map(str,after['size']))} | {b['residue']['strong_key_far_from_edge']} → {after['residue']['strong_key_far_from_edge']} | {b['residue']['interior_semitransparent']} → {after['residue']['interior_semitransparent']} | {pr['rgb_changed']}/{pr['alpha_changed']} trên {pr['pixels']} px | {margin(b)} → {margin(after)} |")
    lines += ["", "| Viền decal | Độ sáng / màu đục lân cận trước → sau |", "|---|---|"]
    for r in decals:
        lines.append(f"| {link(r['output'])} | {r['before']['fringe']['luminance_ratio']} → {r['after']['fringe']['luminance_ratio']} |")
    lines += ["", "Tỷ số viền dùng alpha 32–224 so trung bình pixel alpha 255 trong 7×7, bỏ điểm không có màu đục lân cận. "
              "Ngưỡng tham khảo 0,85; màu thật tối ở nét mảnh cũng có thể làm tỷ số thấp, cần đối chiếu crop nguồn.", "", "Sheet 1:1: [trắng](../_review/decals-012c.white.png), [caro](../_review/decals-012c.checker.png), "
              "[tối](../_review/decals-012c.dark.png); bộ `.v1` ở `decals-archive-012c.*.png`. "
              "Hoa tím D2, viền lá/kim D3 và lỗ nhỏ vẫn cần Claude duyệt mỹ thuật lần 3.", "",
              "## 3. Phông xa B1", "",
              f"{link(backdrop['output'])}: khổ **{'×'.join(map(str,backdrop['after']['size']))}**, overlap 12%; "
              "xuất W−B, không co giãn. Chọn đường cắt thẳng có sai số tổng nhỏ trong nửa giữa overlap, trộn quanh đường cắt tối đa 8 px. "
              f"Ảnh ghép 2×1: {link('_review/pine-river-far.seam.png')}.", "",
              "| Chỉ số x | 012b | 012c |", "|---|---|---|",
              *[f"| {label} | {old_b.get(key,'không đo')} | {a[key]} |" for label,key in
                (("MAE mép","edge_mae"),("Mép / cột kề","edge_ratio"),("Gương / đối chứng","mirror_ratio"),("Chi tiết dải thấp nhất / phần trong","band_detail_ratio"))],
              f"| Chi tiết toàn ảnh / nguồn | {obj['evidence']['backdrop_012b']['whole_detail_source_ratio']} | {a['whole_detail_source_ratio']} |",
              f"| Chi tiết cửa sổ thấp nhất / nguồn | {obj['evidence']['backdrop_012b']['band_detail_source_ratio']} | {a['band_detail_source_ratio']} |",
              f"| Độ lệch hàng cực đại | {obj['evidence']['backdrop_012b']['row_step_excess']} | {a['row_step_excess']} |", "",
              f"Kết quả chốt 012c: **{'đạt' if a['pass'] else 'chưa đạt'}**. Bản sọc `.rejected-012`: "
              f"**{'trượt' if not obj['evidence']['backdrop_rejected_012']['pass'] else 'lọt chốt'}**. "
              "Tất cả cửa sổ và từng tiêu chí có trong manifest. Mật độ cây/sống núi, đường cắt cảnh và bố cục vẫn cần duyệt nguyên cỡ.", "",
              "## 4. Icon", "",
              f"Dựng lại {len({r['input'] for r in icons})} nguồn ở các cỡ " + ", ".join(map(str,sorted({r['after']['size'][0] for r in icons},reverse=True))) +
              " px. Herb-hut dùng bảo vệ phần trong và khử loang vùng mép; không còn dùng `--despill off`. "
              "Sheet 32 px lấy nguồn 64, nhãn ghi đúng cỡ hiển thị.", "",
              "| File ra | Lề nhỏ nhất trước → sau | RGB/alpha phần trong bị đổi / pixel được kiểm |", "|---|---|---|"]
    for r in icons:
        pr=r["after"]["interior_preservation"]
        lines.append(f"| {link(r['output'])} | {margin(r['before'])} → {margin(r['after'])} | {pr['rgb_changed']}/{pr['alpha_changed']} / {pr['pixels']} |")
    lines += ["", "Duyệt [32 px tối](../_review/icons-32.dark.png), [32 px kem](../_review/icons-32.light.png), "
              "[256 px caro](../_review/icons-256.checker.png), nhất là herb-hut và I03/I12/I14/I17/I18–I19.", "",
              "## 5. Nguồn Tripo", "",
              "**Đã chọn theo đề xuất:** lấy canvas mong muốn theo hộp vật và lề 8%, chọn khổ chuẩn gần nhất trong bảng 012 "
              "(1024×1024, 1024×1536, 1536×1024), theo khoảng cách log của hai chiều để cân bằng tỷ lệ và độ phân giải. "
              "Chủ dự án có thể đổi sau. Đặt giữa, giữ lề 8%; không đổi tư thế/góc nhìn.", "",
              "| File ra | Khổ trước → sau | Tỷ lệ vật / nguồn trước → sau | Lề trước → sau | Gần nền ≠E6 trước → sau | Lõi túi sai lớn trước → sau | Chốt |", "|---|---|---|---|---|---|---|"]
    for r in tripo:
        b,after=r["before"],r["after"]
        lines.append(f"| {link(r['output'])} | {'×'.join(map(str,b['size']))} → {'×'.join(map(str,after['size']))} | {b['subject_scale']} → {after['subject_scale']} | {margin(b)} → {margin(after)} | {b['residue']['near_bg_not_E6']} → {after['residue']['near_bg_not_E6']} | {b['residue']['enclosed_neutral_ge_64_pixels']} → {after['residue']['enclosed_neutral_ge_64_pixels']} | {'Đạt' if after['pocket_gate'] else 'Chưa đạt'} |")
    lines += ["", f"Chốt túi nền: **{len(tripo)-len(failed)}/{len(tripo)} đạt**. " + ("Còn chưa đạt: "+", ".join(link(p) for p in failed) if failed else "Không có ảnh trượt chốt lõi túi lớn."),
              f"{len(obj['prior_pocket_failures'])} ảnh 012b từng bị gắn nhãn chưa đạt đã được đo lại với chốt bỏ viền mềm, không ép màu viền vào E6. "
              "Kết quả trước/sau ở bảng là phép đo mới; nhãn cũ lưu nguyên trong báo cáo `.rejected-012b`.", "",
              "## 6. Kiểm tra và phần chủ dự án cần xem", ""]
    for name,result in obj["validation"].items():lines.append(f"- `{name}`: mã thoát {result['exit_code']}; hash `{result['sha256']}`.")
    lines += ["", "Những phần chưa được duyệt thiết kế nguồn: thorn-wasp-side (góc cánh), moss-banner hai góc (tay cầm cờ), "
              "moss-warden hai góc (tay khiên, nguồn sát/cụt khung), thorn-ant (góc nhìn và độ khớp), D1–D4 (cuống/đá/rêu, cảm giác nổi), "
              "icon I03/I12/I14/I17/I18–I19 (khả năng đọc 32 px), B1 (mật độ cây và bố cục). "
              "Các ảnh này đạt hậu kỳ khi qua chốt nhưng chưa được gọi là đạt thiết kế/rig.", "",
              "**Bỏ qua và lý do:** không sinh lại/sửa ảnh gốc, không sửa runtime, model, âm thanh hoặc ô đất ngoài danh sách 012; "
              "các lỗi thiết kế cần phiếu riêng. Không chạy Git hoặc build/test game. Bản bitmap mới là dẫn xuất xác định của công cụ chuẩn hóa. "
              "Ảnh/báo cáo nằm trong art-src trên Drive; clone chỉ lấy mã không có chúng. Claude cần duyệt lần 3 trước commit.", ""]
    report=ART/"2d/README-normalize.md";verification=ART/"_review/normalize-verification.json"
    require(not report.exists() and not verification.exists(),"Báo cáo/biên bản đã có; từ chối ghi đè.")
    write_new(report,"\n".join(lines))
    json_new(verification,{"ticket":"012c","original_file_count":len(obj["original_sha256"]),
        "original_sha256_unchanged":True,"record_count":len(records),"tool_sha256":obj["tool_sha256"],
        "decal_gate":{"passed":sum(r["after"]["residue"]["strong_key_far_from_edge"]==0 for r in decals),"total":len(decals)},
        "tripo_pocket_gate":{"passed":len(tripo)-len(failed),"failed":failed},"validation":obj["validation"],
        "new_files_sha256":{**obj["artifacts_sha256"],"2d/README-normalize.md":digest(report),"_review/normalize-metrics.json":digest(manifest_path)},
        "archived_sha256":{archive:obj["before_sha256"][old] for old,archive in obj["archived_012b"].items()}})
    print(f"Đã kiểm và báo cáo {len(records)} ảnh; Tripo {len(tripo)-len(failed)}/{len(tripo)}.")


if __name__=="__main__":main()
