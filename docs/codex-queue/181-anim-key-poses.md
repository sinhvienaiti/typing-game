# Phiếu 181 · Ba game · Tờ tư thế khóa cho animation: Hỏa Long, Lightbearer, Mộc Tinh, bóng dáng quái theo họ

**Nguồn:** thiết kế animation 29/10 (`docs/games/CHARACTER_ANIMATION.md`). Chủ dự án 29/10: animation nhân vật là hệ dùng chung, phải đạt từ 9 (`docs/games/SHARED_SYSTEMS_BAR.md`). Người làm animation cần tờ tư thế khóa vẽ tay (gồng, tung đòn, theo đà, bị đánh, chết) để dựng clip có chuẩn bị và theo đà rõ, thay vì đoán.

**Báo cáo:** `docs/codex-queue/181-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5.

## Luật chung

- Repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git. Tối đa 3 lượt sinh mỗi tờ; giữ `.tryN.*`; bản chọn `<tên>.png` và `.prompt.txt`.
- **Đây là tờ tham chiếu cho người làm animation, không phải ảnh trong game:** ưu tiên dáng rõ, đường hành động (line of action), khối lượng; nền phẳng sáng, không cảnh. Mỗi ô ghi chú bằng **hình** (mũi tên chuyển động vẽ tay), không chữ.
- **Mức nhận:** đúng nhân vật (so ảnh nguồn), dáng đọc rõ ở 256 px mỗi ô, đường hành động mạnh; tự chấm theo 5 tiêu chí `docs/games/ART_ACCEPTANCE.md` §2.2, đạt ≥ 8.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn; mọi lệnh git; sửa mã hay tài liệu; mạng ngoài công cụ tạo ảnh; Tu Tiên.
- KA1 md5 trên từng thư mục đích, trước và sau.

## Tờ (mỗi tờ 3072 × 1024, lưới 6 × 2, ô 512²)

| Tên | Thư mục | Nhân vật (ảnh nguồn đính kèm) | 12 ô |
|---|---|---|---|
| `keyposes-hoa-long` | `games/dragon-hold/art-src/anim-ref/` | Hỏa Long, rồng lửa đỏ cam (ảnh 2D gốc của rồng trong `games/dragon-hold/art-src/`, tìm `draconis`, `dragon`, `long`) | lượn nghỉ ×2; gồng phun lửa (rụt cổ, ngực phồng) ×2; tung đòn (cổ vươn, hàm mở) ×2; theo đà (đầu giật lại, cánh vỗ) ×2; bị đánh ×2; hạ cánh, cất cánh ×2 |
| `keyposes-lightbearer` | `games/typing-survival/art-src/anim-ref/` | Lightbearer (`concepts/b-lightbearer-*.png`, ảnh 156 nếu có) | đứng thủ ×2; lướt trái, lướt phải; giơ tay bắn trái, bắn phải; bị đánh ×2; quỳ; đứng dậy; thắng ×2 |
| `keyposes-moc-tinh` | `games/typing-defense/art-src/anim-ref/` | Mộc Tinh, boss cây (chân dung `portraits/moc-tinh.png`) | nghỉ ×2; gồng triệu hồi ×2; tung chiêu ×2; bị đánh ×2; nổi giận; choáng; ngã ×2 |
| `silhouettes-dh-foes` | `games/dragon-hold/art-src/anim-ref/` | quái Dragonhold theo họ: Moss Grunt, Blight Wolf, Tusk Boar, Thorn Wasp, Thorn Ant, Moss Bannerman (`art-src/enemies/*.png`) | mỗi họ hai ô: tư thế tấn công đỉnh và tư thế chết; bóng đen đặc trên nền sáng, đọc được ở 64 px |

## Kiểm (ghi số)

1. Khổ đúng; không chữ, không số.
2. Mỗi ô: bóng dáng (mặt nạ) đọc được ở 256 px; hai ô kề nhau của cùng một hành động khác dáng rõ (IoU ≤ 0,85).
3. Đúng nhân vật: tờ so `_review/181-vs-source.jpg` mỗi tờ cạnh ảnh nguồn.
4. KA5 tự chấm.

**Xong khi:** bốn tờ có bản chọn, qua mục 1–3, tự chấm ≥ 8.
