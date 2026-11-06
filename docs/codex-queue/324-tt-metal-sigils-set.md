# Phiếu 324 · Tu Tiên · Ảnh 2D: đủ bộ ấn trên đất của Kim (5 ảnh), thay hình đang vẽ bằng mã

Anh (06/11 19:10): "Duyệt 2 mẫu ấn Kim" (phiếu 323). Phiếu này vẽ 5 hình còn lại của hàng 2 và hàng 3 trong `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md`, **cùng phong cách với 2 mẫu đã duyệt**.

**Model `gpt-6.1-sol`, mức `high`. 5 lần gọi `image_gen`, cộng tối đa 3 lần vẽ lại cho ảnh tự chấm dưới 8.** Báo cáo: `docs/codex-queue/324-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu.

## Mốc phong cách (anh đã duyệt)
- `S/metal-sigil-hex.v1-try2.png`
- `S/metal-sigil-line.v1-try1.png`

Mở cả hai bằng `view_image` trước ảnh đầu tiên. Gửi cả hai vào mỗi lần gọi `image_gen` làm ảnh tham chiếu.

## 5 ảnh
| Tên tệp trong `S/` | Chiêu | Hình (nhìn thẳng từ trên xuống) |
|---|---|---|
| `metal-sigil-arcs.v1-try1.png` | Phím 3, Hồi Kiếm Hộ Thân (vòng 4,8 m) | Bốn cung tròn ánh thép đồng tâm, đứt quãng, quay quanh một tâm trống như vòng kiếm hộ thân, mỗi cung mang một mũi kiếm nhỏ hướng theo chiều quay, phù văn mảnh dọc cung. |
| `metal-sigil-arrow.v1-try1.png` | Phím 4, Lưu Quang Bộ (vạch 5 × 0,9 m) | Một mũi tên ấn dài nằm ngang (cao khoảng 1/6 khung) chỉ sang phải: thân là ba vệt sáng song song như dấu lướt, đầu là mũi kiếm nhọn, các vạch ngắn đánh dấu nhịp bước dọc thân. |
| `metal-sigil-spiral.v1-try1.png` | Phím 6, Thiên Hà Kiếm Vũ (trận 13,5 m) | Trận xoắn ốc lớn như dải ngân hà: ba nhánh xoắn bằng ánh thép bạc và ánh sao, các điểm sao nhỏ và mũi kiếm li ti rải dọc nhánh, vòng tròn ngoài mảnh có phù văn; tâm sáng nhỏ. |
| `metal-crack-star.v1-try1.png` | Vết nứt khi kiếm cắm đất (nứt sao 1,7–7,5 m) | Vết nứt hình sao trên đất do kiếm khí: tâm là lỗ cắm nhỏ, 6–8 đường nứt sắc tỏa ra không đều, mép nứt phát ánh thép trắng, vài nứt nhánh nhỏ và mảnh sáng li ti. Chỉ nét sáng, không vẽ đá. |
| `metal-rift-groove.v1-try1.png` | Rãnh mưa kiếm (rãnh 22 m) | Một rãnh chém dài nằm ngang hết bề rộng ảnh (cao khoảng 1/8 khung): khe sáng ánh thép ở giữa, mép rãnh nứt răng cưa phát sáng, các nứt nhánh ngắn hai bên, hai đầu thon nhọn. Chỉ nét sáng, không vẽ đá. |

## Cách làm mỗi ảnh
1. Gọi `image_gen`, khổ ngang 16:9, kèm 2 ảnh mốc. Prompt giống phiếu 323:
   ```text
   A premium Chinese donghua xianxia skill ground sigil, painted as a game decal texture seen straight from above (orthographic top-down, no perspective): <SUBJECT>. Razor-sharp white-silver steel light with a faint pale gold inner line, fine sword runes and trigram marks, crisp thin bright strokes with soft glow and a few glints, layered detail, luxurious and modern; anime-mythic, not realistic. Match the style of the attached approved sigils. Bright lines on a solid pure black background, no ground texture, no stone, no text, no letters, no watermark. Centred with an empty margin.
   ```
   `<SUBJECT>` là câu ở cột "Hình", dịch sang tiếng Anh, giữ đủ chi tiết.
2. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu, prompt nguyên văn, khổ thật.
3. **Tự chấm** như phiếu 323 (đúng dáng; đẹp, sang; nhìn thẳng từ trên xuống, nền đen thuần, không chữ; dùng làm mặt nạ được, lề trống, không cắt), thêm tiêu chí **cùng phong cách với 2 mốc**. Ghi theo mặt yếu nhất. Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản điểm cao hơn.

## Xong khi
- Có 5 ảnh (kèm `.prompt.txt`).
- Có tấm ghép `S/metal-sigils-set-sheet.jpg`: 7 bản đã chọn (2 mốc + 5 mới), lưới 4 cột, kèm tên ngắn tiếng Anh, nền đen. Mở bằng `view_image` để kiểm đúng ô.
- Báo cáo có bảng: ảnh, bản chọn, điểm từng tiêu chí, một câu nhận xét.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
