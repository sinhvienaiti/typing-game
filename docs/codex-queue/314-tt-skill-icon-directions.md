# Phiếu 314 · Tu Tiên · Ảnh 2D: 3 hướng biểu tượng kỹ năng cho thanh chiêu, 6 lần gọi `image_gen`, có tự chấm ở cỡ thật

Anh (06/11): "Vẽ mẫu biểu tượng". Đây là biểu tượng cho các ô chiêu trên thanh Bàn Quyết. Anh sẽ chọn một hướng rồi mới vẽ cả bộ. Luật đã học: biểu tượng duyệt trên tấm 256 px từng chỉ được 6,2 điểm khi hiện thật ở 16–24 px. Vì vậy chấm ở cỡ thật, dáng đậm, một hình chính rõ.

**Model `gpt-6.1-sol`, mức `high`. Đúng 6 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại cho mẫu tự chấm dưới 8.** Báo cáo: `docs/codex-queue/314-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/ui/skill-icons` (tạo mới). `S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. `U = games/immortality-cultivation/art-src/lab/ui/streak-counter`.

**Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Hai chiêu mẫu (hình chính bên trong biểu tượng)
- **meteor-rain-fire:** mưa thiên thạch lửa. Hình chính là một thiên thạch lửa lớn rơi chéo, đầu sáng, đuôi lửa. Tham chiếu chất liệu: `S/fire-comet.v1-try1.png`.
- **crescent-metal:** kiếm khí lưỡi liềm đối xứng bay thẳng, ánh thép bạc. Tham chiếu chất liệu: `S/metal-crescent-sym.v1-try1.png`.

## Ba hướng (khung và nền của biểu tượng)
- **ink-gold** (cùng ngôn ngữ với bộ đếm chuỗi anh đã chọn; tham chiếu thêm `U/streak-ink-edict.v1-try1.png`): huy hiệu tròn, nền vệt mực khô đen, viền vàng lá mảnh kiểu filigree, hình chính sáng rực ở giữa.
- **jewel-crest:** khối bo góc như đá quý cắt mặt, trong suốt tối màu, viền vàng hoàng gia nhiều lớp, hình chính phát sáng bên trong như nằm trong ngọc.
- **bronze-seal:** ấn đồng vuông cổ, mép chạm khắc vân mây, hình chính nổi lên như phù điêu và phát sáng theo hệ.

## Cách làm mỗi ảnh (6 ảnh: 3 hướng × 2 chiêu)
1. Mở các ảnh tham chiếu bằng `view_image`: chất liệu của chiêu, và với ink-gold thêm ảnh bộ đếm. Chỉ lấy chất liệu, ánh sáng và độ hoàn thiện.
2. Gọi `image_gen`, khổ vuông, nền trong suốt nếu công cụ cho phép (không thì nền đen thuần). Prompt:
   ```text
   A premium game skill icon for a Chinese xianxia action game, one icon centred, square, <FRAME>. Inside it: <MOTIF>. Bold, simple, instantly readable silhouette that still reads at 32 pixels: one large central shape, strong contrast between the bright motif and the dark ground, crisp outline, a soft glow and a few glints; luxurious, stylish, modern Chinese donghua game UI, rich detail at full size. No text, no letters, no numbers, no watermark.
   ```
   - `<FRAME>`, theo hướng:
     - ink-gold: "a round medallion: a dry-brush black ink wash disc with a hairline mineral-gold filigree rim";
     - jewel-crest: "a rounded-square faceted dark jewel crest with layered royal gold rims, the motif glowing inside the gem";
     - bronze-seal: "an ancient square bronze seal with carved cloud-pattern edges, the motif raised in relief and glowing".
   - `<MOTIF>`, theo chiêu:
     - meteor-rain-fire: "a huge blazing fire meteor falling diagonally with a white-gold head and a vermilion flame tail";
     - crescent-metal: "a symmetric crescent of razor-sharp silver sword light flying straight up, with a white blazing edge".
3. Chép `cp -n` thành `D/<hướng>-<chiêu>.v1-try1.png`; ghi `.prompt.txt` (công cụ, ảnh tham chiếu, prompt, khổ thật).
4. Tạo bản thu nhỏ 32 px và 48 px (`sips -Z` hoặc ImageMagick), đặt tên `…-32.png` và `…-48.png`. Ghép một tấm `D/icon-directions-sheet.png`: mỗi hàng một hướng; mỗi ô gồm bản 256, 48 và 32 px, trên nền tối giống thanh chiêu (#15171c).
5. **Tự chấm ở cỡ 32 và 48 px** (mở tấm ghép bằng `view_image`), thang 0–10:
   - đọc ra chiêu gì khi nhỏ;
   - độ cuốn hút và sang trọng;
   - khung và hình có tách bạch không;
   - sạch.

   Dưới 8 thì vẽ lại một lần (`-try2`), chọn bản điểm cao hơn.

## Xong khi
- Có đủ 6 biểu tượng (cộng bản thu nhỏ) và tấm ghép.
- Báo cáo có bảng: ảnh, điểm ở 32 px, điểm ở 48 px, một câu nhận xét. Kèm đề xuất hướng nào đọc rõ nhất khi nhỏ.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
