# Phiếu 241 · Dragonhold · Làm lại rãnh thanh trượt bảng Sound (ý tưởng gọn đầu)

**Nguồn:**
- Phiếu `docs/codex-queue/225-settings-slider-art.md` và báo cáo `225-report.md`. Mọi luật của 225 cho rãnh vẫn áp dụng: khổ, nền trong suốt, hậu kỳ, Kiểm 1–5, tờ xem trên nền tối và sáng, tham chiếu. Phiếu này chỉ ghi chỗ khác.
- Claude chấm tờ `games/typing-defense/art-src/_review/225-sheet.jpg` ngày 31/10:
  - **Nhận:**
    - Wordwoven: rãnh và núm;
    - Last Line: rãnh và núm;
    - Dragonhold: núm.
    - Không động tới năm ảnh này.
  - **Chưa đạt:** rãnh Dragonhold 7,5.
    - Ảnh nguồn rộng/cao 12:1, nên khi đưa về 16:1 phải co không đều, lệch 24,79%. Hai đầu bị ép dẹt.
    - Đầu rãnh rộng quá mức 61 px của Kiểm 4.
    - Đã dùng 3 lời gọi.
- Chủ dự án 31/10 05:15: Codex gần hết hạn mức, tạm chỉ giao việc tạo ảnh. Phiếu này chỉ có tạo ảnh và hậu kỳ.

**Báo cáo:** `docs/codex-queue/241-report.md` (tiếng Việt) và thư mục `docs/codex-queue/241/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

Ý tưởng mới cho rãnh Dragonhold, tối đa **3 lượt**, tên `slider-track.c2-try1..3`.
- Bảng màu và chất liệu giữ như núm Dragonhold đã nhận: vàng đồng ấm, lõi tối.
- **Đầu rãnh gọn:** mỗi đầu chỉ là một mũ tròn hay vát nhỏ, không có móc hay hoa văn lớn, để đạt Kiểm 4 (mỗi đầu ≤ 6% chiều rộng). Thân rãnh dài, đều, có thể có vân kim loại mảnh.
- Xin công cụ đúng khung ngang dài. Nếu công cụ trả khung khác 16:1 thì cắt theo hộp bao rồi đặt vào khung 16:1 **bằng đệm trong suốt**, không co không đều. Ghi hệ số co x, y; hai số phải bằng nhau.

**Kiểm (bắt buộc):** Kiểm 1–5 của 225 cho rãnh. Ghép tờ xem có rãnh mới đặt cạnh núm Dragonhold đã nhận ở 720p và 1080p, các mức 0%, 50%, 100%, trên nền tối và sáng.

**Giới hạn ảnh:** công cụ ảnh trả 429 hoặc báo thử lại sau thì dừng, giữ nguyên mọi file, và ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM`.

## Chỉ được ghi

- `games/dragon-hold/art-src/ui/quick-settings/sliders/slider-track.c2-try*.*` (mới).
- Bản chốt `slider-track.png`, `.512.png`, `.prompt.txt` của Dragonhold.
  - Được ghi đè vì chưa được nhận.
  - Trước khi ghi đè, chép bản cũ sang `games/dragon-hold/art-src/_review/241/prev/`.
- `games/dragon-hold/art-src/_review/241*`.
- `docs/codex-queue/241-report.md`, `docs/codex-queue/241/`.

## Cấm

- Sửa hay xoá năm ảnh đã nhận và mọi file `try*` cũ.
- Đụng Wordwoven hay Last Line.
- Chép vào `public/`.
- Lệnh Git ghi.
- Tu Tiên; `.wt-*`.

## Nhận

- Claude chấm lại từ 8, có xét Kiểm 4 và hình ở 720p.
