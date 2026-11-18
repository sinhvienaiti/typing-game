# Phiếu 337 · Tu Tiên · Ảnh 2D: tấm A9 (tia lửa, tàn lửa, bụi sáng) thay đốm tròn vẽ bằng mã, có tự chấm

Anh (11/11): ảnh do Codex phụ trách; "Đồng ý cả hai" cho việc ảnh đang đỗ. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần gọi `image_gen`** (3 tấm × 1, cộng tối đa 1 lần vẽ lại cho tấm tự chấm dưới 8). Mở tối đa 8 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/337-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu (kể cả `art-src/lab/tex/*` của Kenney); sửa mã.

## Bối cảnh
- Bản rà 05/11 (`docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md`, số 7, 11, 16 và Lô 4): tàn lửa và tia lửa hệ Hỏa đang là **đốm tròn vẽ bằng mã**, thứ anh cấm. Lô 4 chờ "tấm A9": một bộ sprite rời để engine rải hàng nghìn hạt.
- Yêu cầu của A9 (kế hoạch 04/11): **ba độ dài rõ; không đốm tròn; có khoảng trống giữa các ô.**
- Mỗi tấm là **lưới 4 × 4 = 16 sprite rời**, mỗi sprite nằm giữa ô của nó, không chạm mép ô, nền đen thuần. Engine cắt từng ô và tự nhuộm màu theo hệ, nên vẽ **sáng trắng tới vàng ngà rất nhạt** (dữ liệu độ sáng), không vẽ màu cam đỏ đậm.
- Hạt hiện rất nhỏ trong game (4–15 px), nên dáng phải đọc được khi thu nhỏ: dáng rõ, lõi sáng, đuôi thon.

## Ba tấm
Tham chiếu của cả ba (chỉ lấy độ hoàn thiện và kiểu hạt lửa, không lấy bố cục): `S/karmic-ember-tempest.v1-try1.png`, `S/ult-fire-one-spark.v1-try9.png`.
| Tên tệp | Hình (dịch đủ sang tiếng Anh trong prompt) |
|---|---|
| `S/a9-spark-streaks.v1-try1.png` | 16 tia lửa dạng vệt: hàng 1 vệt ngắn, hàng 2 vệt vừa, hàng 3 vệt dài, hàng 4 vệt cong hoặc chẻ đôi. Mỗi vệt có đầu sáng nhọn, đuôi thon mờ dần, vài hạt li ti bám theo. Mỗi vệt một hướng và độ cong khác nhau |
| `S/a9-ember-flakes.v1-try1.png` | 16 tàn lửa dạng mảnh: mảnh tro dẹt méo, mảnh lá cháy quăn, mảnh vụn góc cạnh, sợi than ngắn; viền sáng, lòng hơi tối hơn, không cái nào tròn. Bốn cỡ từ nhỏ tới lớn theo hàng |
| `S/a9-dust-motes.v1-try1.png` | 16 cụm bụi sáng: mỗi ô là một cụm 5–12 hạt rất nhỏ rải không đều (hạt hình thoi, que ngắn, sao bốn cánh mảnh), có một hai hạt sáng trội; không có đĩa tròn hay quầng tròn lớn |

## Cách làm mỗi tấm
1. Mở ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`, khổ 1:1. Khối chung đặt sau câu tả hình:
   `A sprite sheet: a strict 4 by 4 grid of 16 separate sprites, each sprite centred in its own cell with clear empty black space around it, no sprite touching a cell edge or another sprite, no grid lines, no borders, no labels, no numbers, no text, no watermark. Uniform pure black background. White to very pale warm ivory luminance only (the engine tints it), bright thin cores, soft tapered falloff. No round dots, no circular blobs, no lens flares. Premium Chinese donghua xianxia game VFX particle sprites, crisp readable shapes even when tiny.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; cắt thành 16 ô đều rồi đo mỗi ô: có nội dung, và dải 4 % sát mép ô có độ sáng cực đại ≤ 12/255 (sprite không chạm mép). Ghi số ô đạt trên 16.
5. **Tự chấm** 0–10 theo mặt yếu nhất: đúng lưới 4 × 4 và ô tách rời; không có đốm tròn; ba độ dài hoặc bốn cỡ rõ; đọc được khi thu tấm xuống 256 px (tự thu nhỏ rồi mở xem); đẹp, sang, đúng chất lửa tiên hiệp. Dưới 8: vẽ lại một lần (`-try2`), chọn bản cao hơn.

## Xong khi
- Đủ 3 tấm cùng `.prompt.txt`, tấm ghép `S/a9-337-sheet.jpg` (3 tấm cạnh nhau, có tên, kèm một hàng thu nhỏ 256 px), và báo cáo có bảng: tấm, điểm từng tiêu chí, số ô đạt, nhận xét, có vẽ lại không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
