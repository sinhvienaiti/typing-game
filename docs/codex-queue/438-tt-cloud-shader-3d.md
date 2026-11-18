# Phiếu 438: Shader mây 3D dùng chung (thử trên mây sét Lôi)


Phản biện: PASS (Sonnet, 17/11)
## Bối cảnh
Owner 17/11 đồng ý hướng thư viện khói/mây dùng chung: mây lớn trên trời làm bằng shader 3D để nhìn đúng ở mọi góc (owner 17/11: "những trận pháp được triệu hồi ở trên trời, nó cần được nhìn 3d để không bị lệch"), code tô màu theo hệ. Bản Lôi hiện có mây chỉ là dải mỏng ở mép xa (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-chain-r1.jpg`).

## Việc (worktree `games/.wt-ic-lab-all`, file mới `src/lab/cloud-volume.ts`)
1. Module mây dùng chung: 6–12 mặt phẳng nằm ngang xếp chồng theo chiều cao (hoặc raymarch rẻ trong một hộp), mật độ từ nhiễu fbm 3D trượt theo thời gian (cuộn, trôi), mép mềm, tối ở dưới đáy và sáng ở đỉnh (tự che sáng giả). Tham số: tâm, bán kính, độ cao đáy, độ dày, màu đáy, màu đỉnh, màu phát sáng, cường độ chớp bên trong (vị trí ngẫu nhiên, nhấp nháy), tốc độ cuộn, độ phủ (0–1), thời gian hiện/tan. Mỗi kênh màu lớp phụ ≤ 0,9.
2. Không dùng ảnh hay video; chỉ code shader (đây là chất liệu, không phải hình vẽ sẵn).
3. Thêm trang thử trong lab: một phím (ghi trong báo cáo) bật mây sét Lôi phía trên đám quái (tím đen, chớp tím trắng), mây độc (xanh lục, phát sáng nhẹ) và mây đen Ám (tím đen hút sáng), mỗi bản tách riêng bằng tham số URL `?cloud=thunder|poison|dark`.
4. Hiệu năng: tối đa 2 lượt vẽ cho một đám mây; p95 `stress.html` 100 quái ≤ 16,7 ms khi bật 1 đám mây phủ cả sân.
5. **Không** nối vào `thunder-ult-chain.ts` (phiếu 434b đang sửa file đó); chỉ xuất API để nối sau.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; probe in số lượt vẽ, thời gian khung, phạm vi phủ khung camera chơi 1280×720 của mây (≥ 60 % bề ngang khi bán kính 12 m).
- Để lệnh chụp cho Claude ở camera chơi, góc trên (phím 1), góc sau lưng (phím 2) cho cả 3 kiểu mây.
- Chỉ sửa trong worktree: file mới `src/lab/cloud-volume*.ts` và đúng chỗ đăng ký phím thử. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/438-report.md`.
