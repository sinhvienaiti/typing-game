# Phiếu 433m: báo cáo (Claude làm thay Codex vì Codex hết lượt)

18/11/2026. Owner chọn "Trận mờ/nhỏ hơn + bụi vàng". Làm 3 vòng sửa → chụp Alt+1 và Alt+2 (`?ground=%23353a40`, 100 quái) → mở ảnh.

## Đã sửa (chỉ `src/lab/metal-ult-rain.ts`)
- **Trận:** độ mờ 0,74 → **0,45**; đường kính 22 → **16 m**. Bóng trận dưới đất dùng cùng đường kính nên thu theo. Vùng kiếm rơi lấy theo bán kính trận nên vẫn nằm trong hình chiếu: điểm cắm xa nhất **0,94 R**. Ở camera chơi, quái và phần đầu đường rơi đã nhìn xuyên qua trận.
- **Bụi nổ kiếm lớn** (`Explosion01` flipbook): chỉ đổi tint (1,15; 1,0; 0,68) → **(3,0; 1,85; 0,42)**. Bụi giờ có màu vàng ấm sáng, không còn xám đục. Lõi khói vẫn tối hơn vì đó là bóng đổ có sẵn trong ảnh nguồn.
- Không vẽ thêm lớp nào bằng code.

## Số đo (vòng 3)
- Cổng quãng rơi của 433f: **48/48** kiếm đạt, trung vị 0,95 s và 22,8 % chiều cao khung.
- Lề trận trong camera chơi: **26,0 %**, trước đây 20,9 %.
- Vùng trắng **0,0001 %**, ngưỡng ≤ 6 %. p95 **5,8 ms**; đã dùng tối đa 212 draw call.
- Kiểm kiểu **0 lỗi**.
- Vòng 1 dùng tint (1,75; 1,22; 0,48): bụi còn màu ô liu. Vòng 2 dùng (2,6; 1,8; 0,62): bụi màu kaki. Vòng 3 ra màu vàng ấm.

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-m.jpg` và `.mp4` (6,875 s, có âm). Đã thêm dòng vào `ABOUT.md`.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-m-review.mjs` (chép từ bản l).
- Tấm ghép và số đo: `typing-game-review/captures/tu-tien/metal-rain-433m/`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile tạm. Server 3148 vẫn chạy. Không commit.

## Owner xem
Ở Alt+2 trận vẫn vượt mép trên khung (chủ ý từ 433l). Vùng kiếm rơi nhỏ lại theo trận nên bao ít quái hơn.
