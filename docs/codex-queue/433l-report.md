# Phiếu 433l: báo cáo (Claude làm thay Codex vì Codex hết lượt)

18/11/2026. Làm 4 vòng sửa, chụp và mở ảnh. Mỗi vòng chụp hai góc: Alt+1 (camera chơi) và Alt+2 (sau lưng), nền `?ground=%23353a40`, 100 quái. Các mốc chụp: đợt 1 (1,10 s), giữa mưa (2,00 s), mưa dày nhất (3,00 s), kiếm lớn chạm (4,92 s), bụi nổ (5,20 s) và +1,5 s (6,40 s).

- Kiểm kiểu: **0 lỗi**.
- p95 lúc mưa dày: **5,7 ms** (ngưỡng 16,7 ms).
- Vùng trắng: **0,0001 %**.

Đây là bản lab gửi owner xem, chưa có chấm mù 8,5.

## Bảng 7 lỗi (số đo vòng 4, camera chơi)

| # | Lỗi owner nêu | Đã sửa? | Số đo |
|---|---|---|---|
| 1 | Trận không hợp góc nhìn | Đã sửa | Tâm trận nằm thẳng trên tâm vùng kiếm rơi, cao **12 m**, đường kính 22 m (không phải hạ độ cao hay thu bán kính). Lề nhỏ nhất trong khung camera chơi **20,9 %**. Bóng trận dưới đất là chính ảnh `formation-simple-a`, nhuộm vàng tối, độ mờ 0,18. Tia sáng dùng `rays.png`. Bỏ cách lùi trận ra sau của 433j. |
| 2 | Kiếm nhỏ quá to | Đã sửa | Thân kiếm nhỏ cao: trung vị **22,6 px**, từ 17,7 đến 35,9 px tuỳ độ sâu và lúc kiếm ở gần camera khi đang bay. Kiếm lớn cao 385–444 px, gấp **≥ 17 lần** kiếm nhỏ (cổng ≥ 4). |
| 3 | Rơi xong là mất | Đã sửa | Kiếm cắm giữ nguyên **1,5 s** rồi tan bằng độ mờ trong **0,5 s**. Lúc nhiều kiếm hiện nhất (3,28 s): **29 kiếm cắm**, 19 đang bay, 48 kiếm hiển thị (cổng ≤ 60). Số kiếm bay cùng lúc nhiều nhất **20**, số kiếm cắm cùng lúc nhiều nhất **39**. |
| 4 | Chạm đất ảo, xấu | Đã sửa | Kiếm nhỏ không còn gọi impact, ground-mark, dust và sparks cũ; code vẫn giữ. Thay bằng: chớp bụi CC0 `DiscSmoke01_16x4` nhuộm màu đất, hoà trộn thường, sống 0,5 s; một chùm `metal-sparkle` sống 0,4 s. Không có đĩa sáng hay vòng. |
| 5 | Như đồ chơi | Đã sửa (chờ owner chấm) | Khi mưa dày, camera rung nhẹ liên tục (0,05 m). Lúc kiếm lớn chạm đất, camera giật mạnh 0,45 m rồi tắt dần. Nổ bụi `Explosion01-light-nofire_5x5` nhuộm vàng xám rộng **khoảng 27 %** bề ngang khung. Có thêm lớp âm `crack` chồng lên `break` và `tail`. Quái quanh điểm chạm bị hất qua hook `blow` có sẵn. Cả cảnh tối đi bằng một lớp đen phẳng, độ mờ **0,22**. |
| 6 | Kiếm cắm dựng đứng | Đã sửa | Góc cắm khớp góc rơi: dot ≥ **0,9999999**. Mũi kiếm ngập **20 %**. Quad kiếm cố định trong không gian thế giới từ lúc cắm, không quay theo camera. |
| 7 | Kiếm bay quá xa trận | Đã sửa | Điểm cắm xa tâm trận nhất **0,94 R** (cổng ≤ 1,05 R). Kiếm lệch khỏi phương thẳng đứng nhiều nhất **9,9°** (cổng ≤ 12°). |

Quãng rơi: 48/48 kiếm đạt cả hai mức. Trung vị **0,95 s** và **22,6 %** chiều cao khung ở camera chơi (51,6 % ở Alt+2).

## Số đo từng vòng

| Vòng | Kiếm nhỏ px (trung vị) | Lề trận | Kiếm cắm lúc dày nhất | Thay đổi |
|---|---|---|---|---|
| 1 | 49,6 | 20,9 % | 17 (đo theo số kiếm bay nhiều nhất) | Đặt lại trận, đổi nhịp mưa, kiếm cắm, bụi và tia lửa, rung camera, lớp tối |
| 2 | 22,6 | 20,9 % | 29 (đo theo số kiếm hiện nhiều nhất) | Thu kiếm nhỏ về 1,85–2,0 m; thêm mốc chụp bụi nổ |
| 3 | 22,6 | 20,9 % | 29 | Nổ bụi to hơn và sáng hơn (24 m), xuất bản cuối |
| 4 | 22,6 | 20,9 % | 29 | Nâng nổ bụi lên y 10 m, cỡ 26 m, để đất không cắt phẳng mép dưới |

p95 qua các vòng: 5,2 / 5,6 / 5,5 / 5,7 ms. Draw call nhiều nhất là 211.

## Tệp

- Sửa:
  - `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`
  - `games/.wt-ic-lab-all/src/lab/metal-ult-energy-a.ts`
- Driver mới: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-l-review.mjs`
- Atlas mới, chỉ đổi định dạng TGA sang PNG, kèm `.json` và `.prompt.txt`:
  - `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/disc-smoke-01.atlas.png`
  - `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/explosion-01-nofire.atlas.png`
- Gửi owner:
  - `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-l.jpg`
  - `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-l.mp4` (1280×720, 24 fps, 165 khung, 6,875 s, có âm)
  - Đã thêm dòng vào `ABOUT.md`.
- Tấm ghép và số đo 4 vòng: `typing-game-review/captures/tu-tien/metal-rain-433l/`.

## Dọn dẹp

- Đã xoá toàn bộ khung PNG thô.
- Chrome headless tự đóng và đã xoá profile tạm; không còn profile `st-cdp` nào của phiên này.
- Server 3148 vẫn chạy.
- Không commit.

## Owner cần xem

- Kiếm nhỏ cao 22 px nên ở camera chơi khá mảnh.
- Ở camera chơi, trận nằm ngay trên vùng đánh nên che phần đầu đường rơi của kiếm.
- Ở Alt+2, trận vượt mép trên khung. Phiếu chỉ đòi lề cho camera chơi, nên đây là chủ ý.
- Nổ bụi trông đục và tối trên nền xám.
