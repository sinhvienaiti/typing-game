# Phiếu 176 · Ba game · Ảnh bìa cho cổng game (6 ảnh)

**Vì sao:** bản demo chạy ở `typing-game.local`, nơi cổng game hiện thẻ của ba game. Thẻ cần ảnh bìa ngang mức game thương mại, theo hướng mỹ thuật mới và tên tiếng Anh (Dragonhold, Wordwoven, Last Line). Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc.

**Báo cáo:** `docs/codex-queue/176-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Luật chung

- Repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git. Tối đa 3 lượt sinh mỗi ảnh; giữ `.tryN.*`; bản chọn `<tên>.png` và `.prompt.txt`.
- **Mức nhận:** M ≥ 8 theo game thương mại (`docs/games/ART_DIRECTION_2026-10-28.md` §1.3; ảnh tham chiếu `games/<id>/art-src/_refs/owner-epic-2026-10-28.webp`) và Q ≥ 8 (`docs/games/ART_ACCEPTANCE.md` §2.2).
- **Không chữ trong ảnh:** tên game do cổng đặt bằng font, hoặc dùng logo đã nhận (Wordwoven: `games/typing-defense/art-src/ui/title-epic/logo.png`). Chừa một vùng yên ở một phần ba dưới cho tên.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn; mọi lệnh git; sửa mã hay tài liệu; dev server, trình duyệt, mạng ngoài công cụ tạo ảnh; Tu Tiên.
- KA1 md5 trên từng thư mục đích, trước và sau.

## Ảnh

Mỗi game hai ảnh: `cover-wide` 1600 × 900 và `cover-square` 1024 × 1024, ở `games/<id>/art-src/ui/cover/` (thư mục mới). Đính kèm ảnh chủ đạo đã có của game làm tham chiếu nhân vật và màu, với dòng `Use the attached image only to keep the same world, hero, colours and materials. Paint a new cover as described.`

| Game | Tham chiếu | Nội dung |
|---|---|---|
| Dragonhold (`games/dragon-hold`) | ảnh 119 khi có (`art-src/` của 119), nếu chưa có thì `art-src/_refs/` và ảnh map | con rồng lửa lớn trên ải núi đá hoa cương lúc bình minh, quân Héo tràn tới cổng ải; khối STYLE §3.2 |
| Wordwoven (`games/typing-defense`) | `art-src/ui/title-epic/keyart.png` (đã nhận) | thung lũng tháp đá vôi, rùa trời, làng phòng thủ bằng chữ phát sáng; khối STYLE §2.2 |
| Last Line (`games/typing-survival`) | `art-src/concepts/b-lightbearer-keyart.png` (hướng B) | Lightbearer áo choàng nhìn từ sau, hai súng canh, bầy kính đen trên đường đắp trước hố đen; khối STYLE §4.3 |

## Kiểm (ghi số)

1. Khổ đúng; không chữ; vùng yên một phần ba dưới có độ lệch chuẩn luma thấp hơn phần còn lại.
2. Đọc được ở 320 × 180 (thẻ nhỏ trên cổng): nhận ra nhân vật chính và thế giới.
3. Tờ `games/typing-defense/art-src/_review/176-portal.jpg`: sáu ảnh xếp như một trang cổng ở 1280 × 720, kèm ảnh tham chiếu của chủ dự án.
4. KA5: M và Q cho từng ảnh.

**Xong khi:** sáu ảnh có bản chọn, qua mục 1–3, tự chấm M ≥ 8 và Q ≥ 8.
