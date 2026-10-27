#!/usr/bin/env python3
"""Ghi báo cáo sau khi kiểm ảnh lô 012b; mọi số đo lấy từ biên bản đã chạy."""
import json
import math
from pathlib import Path
from rebuild_012b import ART, JOB, digest, json_new, require, tool_hashes, verify_originals, write_new


def link(path):
    return f"[`{path}`](../{path})"


def margins(record):
    return "/".join(str(min(v)) for v in record["margins_ltrb_alpha_gt_0"])


def main():
    raise SystemExit("Báo cáo 012b đã khóa; dùng report-012d.sh. Nội dung dưới đây là mẫu lịch sử đã bị phản biện.")
    manifest_path = ART / "_review/normalize-metrics.json"
    obj = json.loads(manifest_path.read_text(encoding="utf-8"))
    require(obj["tool_sha256"] == tool_hashes(), "Hash công cụ không khớp lô.")
    verify_originals(obj)
    for path, sha in obj["artifacts_sha256"].items():
        require(digest(ART / path) == sha, f"Đầu ra đã đổi: {path}")
    for old, archived in obj["archived_012"].items():
        require(digest(ART / archived) == obj["before_sha256"][old], f"Bản 012 lưu sai hash: {archived}")
    records = obj["records"]
    decals = [r for r in records if r["kind"] == "decal"]
    tripo = [r for r in records if r["kind"] == "tripo"]
    icons = [r for r in records if r["kind"] == "icon"]
    backdrop = next(r for r in records if r["kind"] == "backdrop")
    failed = [r["output"] for r in tripo if not r["after"]["pocket_gate"]]
    b, a = backdrop["before"]["seams"]["x"], backdrop["after"]["seams"]["x"]
    lines = [
        "# Rồng Giữ Ải — Phiếu 012b · sửa công cụ và làm lại ảnh chuẩn hóa", "",
        "Ngày 25/10/2026. Đã đọc đủ 33 phát hiện trong phản biện 012 (mã, an toàn, chất lượng ảnh). "
        "Đã sửa công cụ, chạy bộ hồi quy mở rộng và dựng lại 81 ảnh: 8 atlas decal, 1 phông, 40 icon, 32 nguồn Tripo. "
        "Công cụ dùng chung ở `tools/art-normalize/`; đối chiếu từng phát hiện ở `tools/art-normalize/REVIEW-012b.md`.", "",
        f"**File gốc:** giữ nguyên SHA-256 của {len(obj['original_sha256'])} file trong manifest 012. "
        f"**File dẫn xuất cũ:** {len(obj['archived_012'])} file chuyển hậu tố `.rejected-012`, gồm ảnh, sidecar, JSON và báo cáo cũ; "
        "hash bản lưu được đối chiếu với snapshot trước lô. Không dùng bản `.clean.alpha`/`.soft.seamless` cũ làm bản chọn.", "",
        "**Tên dùng cho lô sửa:** `decals/pine-river/<tên>.alpha.png`, `backdrops/pine-river-far.seamless.png`, "
        "`_review/pine-river-far.seam.png`, `icons/normalized/<tên>.256.png`/`.64.png`, các file `.tripo.png` như bảng bên dưới. "
        "Mức đạt kỹ thuật không thay duyệt hình, tư thế rig hoặc thiết kế nguồn.", "",
        "## 1. Cách đo và khả năng tái tạo", "",
        "- Số đo **trước** của decal/icon/Tripo được đo lại từ bản 012 ở tên bàn giao, không lấy từ báo cáo cũ. "
        "Riêng mép phông so với **ảnh nguồn** để tránh chỉ số 0 do thuật toán gương/ép biên cũ.",
        "- Lề bàn giao dùng mọi pixel alpha >0; công cụ trim với alpha >8 để bỏ đốm rất nhạt. Tripo đo hộp pixel khác đúng `#E6E6E6`. "
        "Lề atlas 9,375% của ô 512 =48 px, thực tế có dự trữ lọc. Kích thước giữ theo danh sách 012.",
        "- Màu khóa dư: pixel còn nhìn thấy và chênh màu khóa >25. Với xanh lá/xanh lam dùng kênh khóa trừ max hai kênh kia; "
        "magenta dùng min(R,B)−G. Đây là phép đo rộng hơn định nghĩa deep-blue của phản biện, nên số trước có thể khác. "
        "Cũng đếm pixel gần màu nền còn nhìn thấy/đục trong manifest.",
        "- Nền Tripo: đếm pixel trung tính (max−min ≤6), cách màu nền nguồn ≤6%×255×√3 nhưng chưa đúng E6. "
        "Số này có thể gồm mép khử răng cưa và phần thân xám. Chốt túi nền đo thành phần trung tính gần nền **không nối biên**: "
        "phải còn ≥64 pixel sai E6 và phần sai chiếm trên 5% thành phần. Túi đã có ≥95% E6 được coi là nền đúng với viền khử răng cưa; "
        "không coi tổng pixel gần nền là bằng chứng mọi pixel đó đều là nền.",
        "- Mép phông: MAE cột đầu/cuối so trung vị MAE cột kề, mirror-MAE của 30 cặp gần mép so các cặp đối chứng giữa ảnh "
        "và so nguồn; chi tiết là trung bình trị tuyệt đối sai phân bậc hai theo trục x ở dải mép so phần trong. Không dùng chốt MAE=0.", "",
        "Manifest mới: [lệnh, số đo, hash và danh sách lưu 012](../_review/normalize-metrics.json). "
        "Mỗi mục ghi argv thực tế trong vùng dựng và `replay` từ gốc repo; các lệnh hai bước dùng `\"$WORK/...\"`. "
        "Tạo `WORK` trong vùng tạm được phép và dùng đích mới khi chạy thử. SHA-256 `normalize.py`: "
        f"`{obj['tool_sha256']['tools/art-normalize/normalize.py']}`. "
        "Các JSON `.rejected-012` chỉ là hồ sơ thuật toán cũ đã loại, không tái tạo bằng mã hiện tại.", "",
        "Mỗi ảnh mới có `.prompt.txt` cạnh ảnh: đầu đề dẫn xuất, nguồn, lệnh, hash công cụ rồi prompt sinh ảnh nguồn nguyên văn khi có. "
        "Bản `.v1` thiếu prompt riêng được ghi rõ; không gán prompt của bản khác. Đây là hậu kỳ xác định, không gửi prompt sinh hình mới.", "",
        "## 2. Tám atlas decal", "",
        "Tất cả đầu ra 1024×1024, alpha góc 0/0/0/0, bốn ô có lề ≥48 px. "
        "Tách nền toàn ảnh ở fuzz 12%, alpha mềm, không ăn mòn; unmix và khử màu khóa trên cả pixel đục. "
        "Bộ lọc Triangle tránh tái tạo màu khóa khi resize. Nét 1/2 px được kiểm bằng ảnh hồi quy riêng.", "",
        "| File ra | Màu khóa dư trước → sau | Lề ô nhỏ nhất trước → sau (px) | Kết quả |",
        "|---|---|---|---|",
    ]
    for r in decals:
        before, after = r["before"], r["after"]
        lines.append(f"| {link(r['output'])} | {before['residue']['key_dominance_gt_25']} → {after['residue']['key_dominance_gt_25']} "
                     f"| {margins(before)} → {margins(after)} | Đạt chốt màu/alpha/khổ/lề; thiết kế nguồn xem §6. |")
    lines += ["", "Các sheet **1:1**, mỗi atlas hiển thị 1024 px, có nhãn và không thu nhỏ:", "",
              "- Bản hiện tại: [trắng](../_review/decals-012b.white.png), [caro](../_review/decals-012b.checker.png), [tối](../_review/decals-012b.dark.png).",
              "- Bản lưu nguồn `.v1`: [trắng](../_review/decals-archive-012b.white.png), [caro](../_review/decals-archive-012b.checker.png), [tối](../_review/decals-archive-012b.dark.png).", "",
              "## 3. Phông xa B1", "",
              f"{link(backdrop['output'])}: 1536×1024 RGB đục; ghép 2×1 ở {link('_review/pine-river-far.seam.png')} (3072×1024). "
              "Dải overlap 12% chồng cùng chiều, bỏ phần chồng và trả lại chiều rộng nguồn; không gập gương/ép biên. "
              "[Nguồn ghép để đối chiếu](../_review/pine-river-far.before.seam.png).", "",
              "| Chỉ số trục x | Trước (nguồn) | Sau (012b) |", "|---|---|---|",
              f"| MAE cột đầu–cuối | {b['edge_mae']:.6f} | {a['edge_mae']:.6f} |",
              f"| Trung vị MAE hai cột kề | {b['adjacent_median']:.6f} | {a['adjacent_median']:.6f} |",
              f"| Mép / trung vị | {b['edge_ratio']:.6f} | {a['edge_ratio']:.6f} |",
              f"| Mirror-MAE (30 cặp) | {b['mirror_mae']:.6f} | {a['mirror_mae']:.6f} |",
              f"| Mirror / đối chứng | {b['mirror_ratio']:.6f} | {a['mirror_ratio']:.6f} |",
              f"| Chi tiết dải mép / trong ảnh | {b['band_detail_ratio']:.6f} | {a['band_detail_ratio']:.6f} |", "",
              f"Chốt mép/mirror: **{'đạt' if a['pass'] else 'chưa đạt'}**; mirror sau/nguồn = {a['mirror_mae'] / b['mirror_mae']:.3f}, "
              "không suy giảm dưới 50%. Chi tiết dải mép trên 90% phần trong. "
              "Đã xem crop ghép nguyên cỡ; việc chồng cảnh vẫn có thể tạo bóng đôi ở phần overlap. "
              "Bố cục nhiều cây và tỷ lệ sống núi 62% còn cần duyệt mỹ thuật; không ghi nhận phông đã được chủ dự án phê duyệt.", "",
              "## 4. Bốn mươi icon", "",
              "Xuất lại đủ 20 icon ở 256×256 và 64×64; alpha góc 0, lề tối thiểu 23/8 px. "
              "Riêng herb-hut dùng `--despill off` để giữ màu lavender thật; nền vẫn khóa theo khoảng cách màu. "
              "Sheet 32 lấy nguồn 64 và ghi rõ **32 px** trên nhãn; đây là cỡ hiển thị, không thêm bộ asset 32 ngoài danh sách.", "",
              "| Nguồn | File 256 / 64 | Lề nhỏ nhất trước → sau (256 / 64) |", "|---|---|---|",
    ]
    for r in icons[::2]:
        other = next(v for v in icons if v["input"] == r["input"] and v["after"]["size"][0] == 64)
        lines.append(f"| {link(r['input'])} | {link(r['output'])} / {link(other['output'])} "
                     f"| {margins(r['before'])}/{margins(other['before'])} → {margins(r['after'])}/{margins(other['after'])} |")
    lines += ["", "Sheet đủ chín tấm: `icons-{256,64,32}.{dark,light,checker}.png` trong `_review/`. "
              "Ưu tiên duyệt [32 px nền tối](../_review/icons-32.dark.png), [32 px nền kem](../_review/icons-32.light.png), "
              "[32 px caro](../_review/icons-32.checker.png). I03/I12, I14, I17 và cặp I18/I19 còn cần chủ dự án đánh giá khả năng đọc.", "",
              "## 5. Ba mươi hai ảnh Tripo", "",
              "Tách nền bao gồm túi trung tính kín; giữ khổ theo bảng 012, đặt giữa, lề ≥8%, bốn góc E6 và PNG24 đục. "
              "Không đổi tư thế, góc nhìn hoặc thiết kế. Cột ‘gần nền ≠E6’ báo đầy đủ, gồm cả chi tiết thân/mép mềm; "
              "cột ‘túi lớn’ là tổng pixel sai E6 trong các thành phần kín qua điều kiện ≥64 px và >5% nêu ở §1, quyết định chốt nền.", "",
              "| File ra | Khổ | Lề trước → sau (px) | Gần nền ≠E6 trước → sau | Túi lớn trước → sau | Kết quả |",
              "|---|---|---|---|---|---|",
    ]
    for r in tripo:
        before, after = r["before"], r["after"]
        br, ar = before["residue"], after["residue"]
        status = "Đạt chốt nền/khổ/lề; chưa duyệt hình/rig." if after["pocket_gate"] else "Chưa đạt chốt túi nền; cần xem màu thân/lỗ kín."
        lines.append(f"| {link(r['output'])} | {'×'.join(map(str, after['size']))} | {margins(before)} → {margins(after)} "
                     f"| {br['near_bg_not_E6']} → {ar['near_bg_not_E6']} "
                     f"| {br['enclosed_neutral_ge_64_pixels']} → {ar['enclosed_neutral_ge_64_pixels']} | {status} |")
    lines += ["", f"**Chốt túi nền:** {len(tripo) - len(failed)}/32 ảnh đạt. " +
              ("Ảnh chưa đạt: " + ", ".join(link(p) for p in failed) + ". Không gọi các ảnh này là đã đạt hậu kỳ." if failed else
               "Không còn túi xám qua chốt ≥64 pixel sai E6 và >5% thành phần. Túi nhỏ hơn ngưỡng, viền và các vùng không trung tính vẫn cần xem nguyên cỡ."), "",
              "Ở các vùng bị gắn cờ còn lại, crop kiểm tra cho thấy phần lớn lõi lỗ đã đúng E6, phần sai màu nằm dọc mép vật. "
              "Giữ số đo và trạng thái chưa đạt để Claude duyệt nguyên cỡ; không ép toàn bộ pixel gần nền thành E6 vì có thể xóa mép nhạt thật. "
              "Giới hạn phân biệt nền và vật gần màu này chưa giải quyết hoàn toàn bằng khóa màu tự động.", "",
              "Sheet đầu ra: `tripo-{enemies,generals,units,houses,traps,props}.output.png`. "
              "Các sheet đầu vào cũ lưu `.rejected-012` vẫn dùng được để đối chiếu vì nguồn giữ nguyên hash. "
              "Đã kiểm nguyên cỡ cung–dây và khung tán cây; số đo từng file có trong manifest.", "",
              "## 6. Ảnh còn chưa đạt thiết kế nguồn và phần chủ dự án cần xem", "",
              "| Ảnh / nhóm | Phần chưa đạt hoặc chưa được duyệt |", "|---|---|",
              "| E01-S · thorn-wasp-side | Góc cánh vẫn thấy toàn mặt, không đúng góc Left; cần sinh lại hình trước Multiview. |",
              "| G01-F/B · moss-banner | Khuỷu tay cầm cờ gập; cần sửa tư thế rig rồi đồng bộ hai góc. |",
              "| U1-F/B · moss-warden | Tay khiên gập/khuất, bản sau còn mặt trang trí ngoài; chưa duyệt rig. |",
              "| E25-S/F · thorn-ant | Cần duyệt góc ngang xiên, mắt có đồng tử dọc và độ khớp hai góc. |",
              "| D1–D4 | D2 còn cuống/đá/rêu và cảm giác nổi; D4 còn cây/đá; D1 mảnh đất rời, D3 chi tiết mảnh. Khử nền không sửa thiết kế này. |",
              "| Icon I03/I12 | Lưới/đầu rồng khó đọc ở 32 px. |",
              "| Icon I14/I17/I18–I19 | I14 thành mảng nhỏ; I17 khiên xám tương phản thấp; I18/I19 dáng đĩa gần nhau, phân biệt bằng glyph nhỏ. |",
              "| Icon màu và moss-warden | Coral I07–I12 còn đỏ; I14 còn lá, I20 có vòng nhỏ. Nguồn moss-warden vốn sát/cụt khung phải/dưới; hậu kỳ không phục hồi phần bị thiếu. |",
              "| B1 | Chưa duyệt mật độ cây, bố cục và sống núi 62%; xem cả overlap ở nguyên cỡ trước dùng runtime. |", "",
              "**Bỏ qua và lý do:** không sửa/sinh lại ảnh gốc, không tạo âm thanh/model, không gọi Tripo, không sửa runtime hoặc T1–T8 ngoài danh sách 012. "
              "Các lỗi thiết kế ở bảng trên cần phiếu sinh hình riêng. Không chạy Git; quyền executable của `.sh` trong Git index để chủ dự án đặt khi staging. "
              "Ảnh và báo cáo này ở art-src trên Drive, không nằm trong clone chỉ lấy mã.", "",
              "**Kiểm tra:** `test.sh` đạt với các ca mới; kiểm cú pháp toàn bộ Python/bash đạt. "
              "Manifest và kiểm bàn giao xác nhận hash nguồn/bản lưu, hash công cụ và ảnh cuối. "
              "Chủ dự án/Claude cần xem D2/D3 trên sheet trắng/caro 1:1, phông ghép nguyên cỡ, cung–dây/cành cây và nhóm icon 32 px trước commit.", "",
    ]
    report = ART / "2d/README-normalize.md"
    require(not report.exists() and not report.is_symlink(), "Báo cáo đã có; từ chối ghi đè.")
    verification_path = ART / "_review/normalize-verification.json"
    require(not verification_path.exists() and not verification_path.is_symlink(),
            "Biên bản kiểm bàn giao đã có; từ chối ghi đè.")
    write_new(report, "\n".join(lines))
    verification = {"ticket": "012b", "original_file_count": len(obj["original_sha256"]),
                    "original_sha256_unchanged": True, "record_count": len(records),
                    "tool_sha256": obj["tool_sha256"], "decal_key_residue_gate": "8/8, 0 pixel >25",
                    "tripo_pocket_gate": {"passed": 32 - len(failed), "failed": failed},
                    "test": "Đạt test.sh và verify-code.sh", "new_files_sha256": {
                        **obj["artifacts_sha256"], "2d/README-normalize.md": digest(report),
                        "_review/normalize-metrics.json": digest(manifest_path)},
                    "archived_sha256": {archived: obj["before_sha256"][old] for old, archived in obj["archived_012"].items()}}
    json_new(verification_path, verification)
    print(f"Đã ghi báo cáo 012b: {len(records)} ảnh; túi nền đạt {32 - len(failed)}/32; nguồn và bản lưu đúng hash.")


if __name__ == "__main__":
    main()
