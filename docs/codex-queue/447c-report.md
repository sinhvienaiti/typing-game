# Phiếu 447c: báo cáo (Claude làm thay Codex vì Codex hết lượt)

18/11/2026. Owner chọn viền **C** (`void-core-rim.v1-try3.png`). Làm 3 vòng sửa → chụp Alt+1, Alt+2 và góc 90° (`?ground=%23353a40&blackhole=1`) → mở ảnh.

## Đã sửa (chỉ `src/lab/void-blackhole-ult.ts`)
- **Viền C:** cắt sang alpha để cộng sáng: alpha = max(R,G,B), RGB chia cho alpha, không vẽ thêm. Atlas mới: `art-src/lab/vfx/void-ult/void-core-rim-c.png`, kèm `.json` và `.prompt.txt`. Lỗ tròn trong ảnh đo được bán kính ~0,243 bề ngang.
  - Đặt viền trên một quad quay theo camera, ngay sau quả cầu (lùi 1,05 R theo hướng nhìn). Quad thu phóng đều sao cho lỗ tròn khớp bóng chiếu của cầu: R/√(d²−R²) nhân với khoảng cách tới quad.
  - Tint 1,7/1,55/1,35, renderOrder 7, có kiểm tra độ sâu.
- **Vành bồi tụ:** tint (1,55; 1,3; 1,05) cho sáng hơn. Thêm một cặp vọng của cùng flipbook ở tỉ lệ 0,9, lệch 30 khung, độ mờ 0,7, để dải vành dày vào phía trong. Mép ngoài vành không đổi.
- **Lõi** nhỏ đi **20 %** (`coreShrink` 0,8).

## Số đo (vòng 3)
- Lõi tròn ở góc 90°: tỉ lệ **1,0005**. Đã qua cổng 0,9–1,1 ở cả 3 góc.
- Lề vành nhỏ nhất **4,87 %**, đạt ngưỡng ≥ 4 %. Vành ≥ 32 % vẫn đạt.
- Trắng **0,113 %**, ngưỡng ≤ 6 %. p95 **5,6 ms**. Kiểm kiểu **0 lỗi**.
- Vòng 1 thu lõi 17 %: viền khó thấy. Vòng 2 thu lõi 20 % và nâng tint viền: viền hiện rõ ở Alt+2. Vòng 3 là bản cuối.

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab-c.jpg` và `.mp4` (7 s, có âm). Đã thêm dòng vào `ABOUT.md`.
- Driver: `games/.wt-ic-lab-all/src/lab/void-blackhole-review-c.mjs`.
- Tấm ghép, ảnh 90° và số đo: `typing-game-review/captures/tu-tien/void-blackhole-447c/`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile tạm. Server 3148 vẫn chạy. Không commit.

## Owner xem
- Ở camera chơi, cầu che phần lớn viền, chỉ lộ quầng mép trên. Viền thấy rõ nhất ở Alt+2.
- Cầu vẫn có ánh nâu từ vật liệu GLB gốc. Phiếu không cho đổi vật liệu nên chưa sửa.
