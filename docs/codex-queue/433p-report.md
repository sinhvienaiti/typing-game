# Phiếu 433p: báo cáo (Claude làm thay Codex)

18/11/2026. Owner góp ý: kiếm hiện quá ngắn, cần ở lại thêm 3 s; mưa kiếm cần dài hơn; thêm sấm sét trong lớp bụi.

## Đã sửa
- **Mưa dài hơn** (`metal-ult-rain.ts`): đổi từ 6 đợt sang **10 đợt**, cách nhau 0,55 s, số kiếm mỗi đợt tăng dần 6→9. Tổng 83 kiếm con, rơi liên tục **6,3 s** (trước khoảng 3,7 s).
- **Kiếm con cắm lại 4,5 s** rồi mờ trong 0,5 s (`SMALL_PLANT_HOLD` 1,5 → 4,5 trong `metal-ult-energy-a.ts`). Lúc đông nhất có 83 kiếm hiện cùng lúc (17 đang rơi, 78 đã cắm), dưới mức trần 110.
- **Kiếm lớn ra sau đợt mưa cuối:** sinh ở 6,8 s, chạm đất 7,6 s, bắt đầu tan ở 11,05 s (ở lại lâu hơn 3 s), kết thúc chiêu 12,6 s. Hào quang C và màn tối theo các mốc mới. Ánh nứt dung nham giữ 4,1 s rồi nguội 1,2 s; đường nứt còn đến khoảng 5,9 s. Bụi vẫn lên trễ 0,25 s sau khi chạm, cỡ 17 m, độ đậm 0,51.
- **Sấm trong bụi:** dùng flipbook đã duyệt `thunder/thunder-single-bolt-a-wg-lo` (chỉ đọc, không sửa). Lớp này là thẻ quay mặt về camera, đặt cao hơn bụi một bậc vẽ, nhuộm vàng trắng (0,9; 0,78; 0,5), nên mỗi kênh ≤ 0,9.
  - Quanh bụi kiếm lớn: 4–7 tia nhỏ cao 2,6–4,2 m, mỗi tia sống 0,08–0,15 s. Vị trí, góc xoay và khung hình lấy theo chuỗi băm có seed. Các tia chớp suốt thời gian bụi tồn tại.
  - Bụi kiếm con: 1–2 tia rất nhỏ (0,9 m) mỗi lần chạm đất, chỉ khi kiếm chạm trong khoảng 3,4–6,6 s, là đoạn mưa dày nhất.
- Chỉ đặt vị trí, xoay, phóng đều, nhuộm màu và làm mờ. Không vẽ hình nào bằng code.

## Số đo (vòng cuối)
- p95 lúc mưa dày nhất **8,5 ms**, ngưỡng 16,7 ms. Dùng tối đa 275 draw call.
- Vùng trắng **0,0004 %**, ngưỡng ≤ 6 %.
- Cổng quãng rơi: **83/83** kiếm đạt, trung vị 0,95 s và 22 % chiều cao khung.
- Kiểm kiểu 0 lỗi.

## Tệp
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-p.jpg` và `.mp4`. Clip dài 12,7 s, đủ cả chiêu, có âm.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-p-review.mjs`.
- Đã xoá khung thô. Chrome headless đã đóng và đã xoá profile. Server 3148 vẫn chạy. Không commit.

## Owner xem
Ở camera chơi, tia sấm khá nhỏ và mảnh. Nếu owner muốn rõ hơn, có thể tăng cỡ lên khoảng 1,3×.
