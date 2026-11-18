# Phiếu 323 · Tu Tiên · Ảnh 2D: 2 ảnh mẫu ấn trên đất (sigil) của Kim, thay hình đang vẽ bằng mã

Anh (06/11 19:00): "cho codex 1 làn xử lý ảnh, 1 làn xử lý lab". Bảng rà `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md` hàng 2: các ấn chiêu trên đất của phím 2–6 (`line`, `arcs`, `arrow`, `hex`, `spiral`, `crack`) đang do mã tự vẽ, hiện 180–530 px mỗi lần tung chiêu, và **cần art mới** (B2). Anh đã chê hình vẽ bằng mã (03/11: "vết nứt, vết cháy, đường may kiểu mã không đẹp"; luật: hình lấy từ ảnh vẽ, shader chỉ cho chuyển động). Phiếu này vẽ **2 ảnh mẫu**; anh duyệt rồi mới vẽ đủ bộ.

**Model `gpt-6.1-sol`, mức `high`. Đúng 2 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại cho mẫu tự chấm dưới 8.** Báo cáo: `docs/codex-queue/323-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu.

## Ảnh tham chiếu (anh đã duyệt; chỉ lấy chất liệu, nét và ánh sáng)
- `S/metal-ground-mark.v1-try1.jpg` (dấu trên đất của Kim)
- `S/metal-caster-seal.v1-try1.png` (ấn dưới chân của Kim)

## Hai mẫu
| Tên tệp | Chiêu | Hình |
|---|---|---|
| `S/metal-sigil-hex.v1-try1.png` | Phím 5, Lạc Kiếm Trận (trận 7,2 m) | Trận lục giác nhìn **thẳng từ trên xuống**: hai đường lục giác lồng nhau bằng ánh thép bạc trắng, sáu mũi kiếm nhỏ cắm ở sáu đỉnh, phù văn mảnh chạy dọc cạnh, vòng tròn mảnh nối các đỉnh; tâm để trống. |
| `S/metal-sigil-line.v1-try1.png` | Phím 2, Nhất Tuyến Xuyên Vân (vạch 14 × 1,8 m) | Một dải ấn dài hẹp nằm ngang **ngang hết bề rộng ảnh**, cao khoảng 1/8 khung, nhìn thẳng từ trên xuống: hai đường biên ánh thép song song, giữa là chuỗi phù văn kiếm và mũi tên mảnh chỉ về phía phải, đầu phải nhọn như mũi kiếm. Phần trên và dưới dải là nền đen trống. |

## Cách làm mỗi ảnh
1. Mở 2 ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`, khổ ngang 16:9. Prompt:
   ```text
   A premium Chinese donghua xianxia skill ground sigil, painted as a game decal texture seen straight from above (orthographic top-down, no perspective): <SUBJECT>. Razor-sharp white-silver steel light with a faint pale gold inner line, fine sword runes and trigram marks, crisp thin bright strokes with soft glow and a few glints, layered detail, luxurious and modern; anime-mythic, not realistic. Bright lines on a solid pure black background, no ground texture, no stone, no text, no letters, no watermark. Centred with an empty margin.
   ```
   `<SUBJECT>` là câu ở cột "Hình", dịch sang tiếng Anh, giữ đủ chi tiết.
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu, prompt nguyên văn, khổ thật.
4. **Tự chấm** (mở ảnh bằng `view_image`, thang 0–10), ghi theo mặt yếu nhất:
   - đúng dáng (lục giác có sáu kiếm; dải dài hẹp có mũi nhọn);
   - đẹp, sang, cuốn hút ngang game thương mại;
   - nhìn thẳng từ trên xuống, không phối cảnh; nền đen thuần, không chữ;
   - dùng làm mặt nạ được: nét sáng tách rõ khỏi nền, lề trống, không bị cắt.

   Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản điểm cao hơn.

## Xong khi
- Có 2 ảnh (kèm `.prompt.txt`) và tấm ghép `S/metal-sigils-samples-sheet.jpg` đặt 2 ảnh cạnh nhau trên nền đen.
- Báo cáo có bảng: ảnh, bản chọn, điểm từng tiêu chí, một câu nhận xét.

## Sau khi anh duyệt (không làm trong phiếu này)
Đủ bộ Kim: `arcs` (phím 3), `arrow` (phím 4), `spiral` (phím 6), `crack` (nứt sao), rãnh mưa kiếm; rồi các hệ khác nếu cần.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
