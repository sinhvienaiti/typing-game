# Phiếu 327 · Tu Tiên · Ảnh 2D: biểu tượng còn thiếu của phím 8, và 2 ảnh mẫu ấn trên đất của Hỏa

Làn ảnh của Codex (anh, 06/11 19:00: "cho codex 1 làn xử lý ảnh, 1 làn xử lý lab"). Hai việc nhỏ trong một phiếu:
- **(a)** Thanh chiêu mới trong lab (phiếu 322) còn thiếu đúng một biểu tượng: `sky-gate-open-close` (cổng trời, phím 8). Vẽ ở cả hai kiểu đã duyệt.
- **(b)** Bộ ấn Kim đã xong (phiếu 323, 324, 324b). Bây giờ vẽ 2 mẫu cho Hỏa để anh duyệt trước khi làm đủ bộ Hỏa.

**Model `gpt-6.1-sol`, mức `high`. Đúng 4 lần gọi `image_gen`, cộng tối đa 3 lần vẽ lại cho ảnh tự chấm dưới 8.** Báo cáo: `docs/codex-queue/327-report.md` (tiếng Việt, ngắn).

## Đường dẫn và luật
- `D = games/immortality-cultivation/art-src/lab/ui/skill-icons`.
- `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
- `U = games/immortality-cultivation/art-src/lab/vfx/ult`.
- **Được ghi:** chỉ thêm file mới vào `D` và `S` (`cp -n`) và báo cáo.
- **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo.

## (a) Hai biểu tượng `sky-gate-open-close`
- Làm đúng cách của phiếu 316: prompt, hai câu FRAME của phiếu 314, bản `-48` và `-32`, `.prompt.txt`, tự chấm ở 32 và 48 px.
- Mẫu đạt của mỗi kiểu: `D/ink-gold-meteor-rain-fire.v1-try1.png`, `D/jewel-crest-meteor-rain-fire.v1-try1.png`.
- Ảnh nguồn của chiêu: mục `sky-gate-open-close` trong `U/manifest.json`. Mở ảnh hay khung tiêu biểu mà mục đó trỏ tới.
- **Hình chính:** một cổng trời tròn mở ra giữa mây, ánh sáng trắng vàng rọi thẳng xuống, viền cổng có phù văn.
- **Tên tệp:** `D/ink-gold-sky-gate-open-close.v1-try1.png` và `D/jewel-crest-sky-gate-open-close.v1-try1.png`, cộng bản `-48`, `-32`.

## (b) Hai mẫu ấn Hỏa
- **Mốc dáng** (anh đã duyệt): `S/metal-sigil-hex.v1-try2.png`, `S/metal-sigil-line.v1-try1.png`. Giữ đúng dáng, chỉ đổi chất liệu và màu.
- **Mốc chất liệu Hỏa** (anh đã duyệt): `S/fire-ground-mark.v1-try1.jpg`, `S/fire-crescent-sym.v1-try1.png`. Lửa cam đỏ thật, lõi trắng vàng (canon D54).
- **Tên tệp:** `S/fire-sigil-hex.v1-try1.png` và `S/fire-sigil-line.v1-try1.png`.
- Prompt như phiếu 323, thay câu chất liệu thép bằng: "living spirit fire: white-gold core lines with vermilion and orange flame edges, tiny embers rising off the strokes, soft heat glow". Vẫn nhìn thẳng từ trên xuống, nền đen thuần, không chữ.
- Tự chấm như phiếu 323, thêm tiêu chí "cùng dáng với mốc Kim". Ghép tấm `S/fire-sigils-samples-sheet.jpg`: 2 ảnh Hỏa cạnh 2 mốc Kim.

## Xong khi
- Có 2 biểu tượng (kèm bản nhỏ), 2 ảnh ấn Hỏa và tấm ghép.
- Báo cáo có bảng điểm cho cả 4 ảnh.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
