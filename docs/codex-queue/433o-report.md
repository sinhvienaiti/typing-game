# Phiếu 433o: báo cáo (Claude làm thay Codex)

18/11/2026. Owner chọn "Cho sóng lên trên bụi".

## Đã sửa (`src/lab/metal-ult-rain.ts`)
- **Bụi nổ lên trễ 0,25 s.** Mình chọn cách này thay vì vẽ sóng đè lên bụi. Khi vẽ đè, sóng vàng cộng sáng nằm trên khói trông như dán lên mặt khói, trái với cảm giác vật nằm dưới đất. Còn khi bụi lên trễ, sóng A phóng ra trên nền đất trống trong 0,25 s đầu, sau đó bụi mới cuộn lên che. Sóng vẫn nằm phẳng dưới đất. Bụi giữ cỡ 17 m và độ đậm 0,51.
- **Ánh nứt dung nham B** giữ sáng 1,1 s (trước là 0,8 s), rồi nguội trong 1,2 s. Đường nứt sẫm còn đến khoảng 2,9 s.
- Không vẽ thêm gì bằng code.

## Số đo
- Kiểm kiểu 0 lỗi. Vùng trắng khoảng 0 %, ngưỡng ≤ 6 %. p95 7,5 ms ở vòng cuối (ngưỡng 16,7 ms), dùng 212 draw call.
- Làm 2 vòng. Vòng 1 chụp thêm mốc +0,2 s: sóng A thấy rõ ở chỗ chạm, trước khi bụi lên.

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-o.jpg` và `.mp4`. Đã thêm dòng vào `ABOUT.md`.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-o-review.mjs`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile. Server 3148 vẫn chạy. Không commit.
