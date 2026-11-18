# Phiếu 422: Sửa các lỗi của 17 bùng nổ -v2 trong lab


Phản biện: PASS (Sonnet, 16/11; tách sau 3 vòng)
## Bối cảnh
Agent Claude chụp 421 trong lab ở camera chơi (`typing-game-review/owner-review/2026-11-16/tu-tien/burst-v2/burst-v2-grid.jpg`): mới tốt hơn 7, ngang 7, kém 3. Lỗi:
- **Kém hơn bản cũ:** `fire-big-burst` (nhỏ, tối, ngả đỏ), `void-big-burst` (rất mờ), `water-ring-burst` (nhỏ hơn nhiều so với vòng cũ); `metal-impact` mờ.
- **Sọc ngang cứng** chỗ chạm đất ở `dark-big-burst-white`, `dark-ground-impact-white`, `wind-ring-burst`, `poison-ring-burst`: phần nằm phẳng dưới điểm chạm đọc thành mép cắt.
- **`fire-impact` hiện trễ** ~1,2 s (từ tick ~72).
- `earth-ring-burst` dựng đứng thành đĩa gai quanh quái thay vì đọc là vòng trên đất.
Chạy sau 421 trong làn B (đọc lại `src/lab/burst-v2.ts`).

## Việc (worktree `games/.wt-ic-lab-all`, chỉ `src/lab/burst-v2.ts` và json `-v2` trong `art-src/lab/vfx/<hệ>/`)
1. Cỡ và độ sáng theo bản cũ: mỗi clip -v2 có hệ số scale và intensity riêng trong bảng của `burst-v2.ts`, chỉnh để đỉnh của bản mới chiếm diện tích màn hình trong khoảng 90–130 % của bản cũ ở camera chơi (đo bằng số pixel có độ sáng luma > 0,15 trên nền đen ở khung đỉnh, cùng camera chơi 55°, cùng độ phân giải 1280×720 cho cả hai bản), độ sáng đỉnh ≥ bản cũ.
2. Bỏ sọc chạm đất: phần dưới điểm chạm mờ dần theo chiều cao (height fade ở đáy thẻ, 10–20 % chiều cao), không cắt cứng; hoặc nâng điểm cắt alpha. Không có hàng pixel nào ở đáy thẻ có alpha > 0,1.
3. `fire-impact`: bắt đầu từ khung đầu có năng lượng (cắt bỏ đoạn đen đầu) để hiện ≤ 2 tick sau va chạm.
4. (Màu `fire-big-burst` và hướng `earth-ring-burst` tách sang phiếu 422b.)

## Nghiệm thu
- Kiểm kiểu 0 lỗi; script đo in cho từng clip: tỉ lệ diện tích đỉnh mới/cũ (90–130 %), độ sáng đỉnh mới ≥ cũ (độ sáng đỉnh = luma trung bình của 1 % pixel sáng nhất ở khung đỉnh), alpha hàng đáy ≤ 0,1, độ trễ hiện của `fire-impact` ≤ 2 tick.
- Để lệnh chụp lưới cũ | mới cho Claude. Không đụng file khác, không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/422-report.md`.
