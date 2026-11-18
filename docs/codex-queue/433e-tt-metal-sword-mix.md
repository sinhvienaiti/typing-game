# Phiếu 433e: Kim, kiếm nhỏ dạng năng lượng, kiếm lớn là kiếm thật có hào quang (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Agent Claude đã dựng hai kiểu kiếm, bật bằng tham số `?swordLook=aura|energy`:
- code ở `games/.wt-ic-lab-all/src/lab/metal-sword-look.ts`, có móc trong `metal-ult-rain.ts`;
- ảnh so sánh: `typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-look-AB.jpg`.

Owner chốt ngày 17/11: "tại sao không kết hợp cả 2, với những kiếm nhỏ, dạng số nhiều, thì dùng dạng kiếm năng lượng, kiếm lớn thì vẫn dùng kiếm hình thật là được".

Owner cho chạy full-access để Codex tự chụp ("Cho full-access", 17/11):
- Chrome headless, chỉ vào localhost:3148. Không dừng server.
- Được dùng ffmpeg và `tools/capture-prune/prune.mjs`.
- Cách đo p95 như `games/.wt-ic-lab-all/src/lab/metal-ult-rain-review.mjs`.

Phạm vi sửa: `games/.wt-ic-lab-all/src/lab/metal-ult-*` và `metal-sword-look.ts`. Ngoài code, chỉ được ghi `docs/codex-queue/433e-report.md` và `ABOUT.md` trong thư mục review. Không commit.

## Việc
1. Kiểu mặc định khi không có tham số là kiểu kết hợp:
   - **Mọi kiếm nhỏ:** dạng năng lượng (energy). Lưỡi vàng trong mờ, lõi sáng dọc sống, mép tan.
   - **Kiếm lớn:** kiếm thật (mô hình Tripo) có hào quang (aura). Vỏ sáng vàng, viền fresnel, hạt bay ra.
   - Kiếm lớn phải là điểm nhấn duy nhất: sáng hơn và nổi hơn kiếm nhỏ. Khi đó hệ số tăng sáng 1,5 lần của kiếm nhỏ ở bản B phải hạ xuống, để kiếm lớn nổi bật.
2. Giữ tham số `?swordLook=aura|energy` để so sánh.
3. Vùng trắng toàn khung ≤ 6 %. Kiếm cắm đất vẫn sáng nhẹ cho tới khi tan.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với hai bản A/B và phân cảnh (nửa trái của `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`) → sửa.
- Chụp ở 1,2 / 2,4 / 3,0 s, camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra: độ sáng đỉnh của kiếm lớn so với kiếm nhỏ (tỷ số ≥ 1,5) và vùng trắng.

## Nghiệm thu
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms.
- Lưu `metal-sword-mix.jpg` và một clip `.mp4` dài 4 s vào `owner-review/2026-11-17/tu-tien/`, thêm dòng vào `ABOUT.md`.
- Xoá khung thô của mình.

## Giao nộp
`docs/codex-queue/433e-report.md`.
