# Phiếu 345 · Tu Tiên · Ảnh 2D: trận pháp lôi trên mặt đất (nhìn thẳng từ trên) cho pha tụ lực Ngũ Lôi Oanh Đỉnh

Anh (12/11 08:5x): bỏ xoáy mây trên trời; tụ lực là "dưới mặt đất xuất hiện 1 vòng tròn trận pháp dạng của lôi hiển thị từ bé rồi to dần 1 cách nhanh chóng, sau đó sấm sét đánh ra". Chỉ vẽ ảnh, không sửa mã. Chạy sau phiếu 344.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần gọi `image_gen`** (2 phương án × 1, tối đa 2 vẽ lại). `view_image` tối đa 6. Báo cáo: `docs/codex-queue/345-report.md` (ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-formation-top.v1-try*.png` (phương án 1), `S/thunder-formation-top-b.v1-try*.png` (phương án 2), `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `S/thunder-five-shock-ring-top.v2-try1.png`: góc nhìn thẳng từ trên, bảng màu trắng xanh, kiểu tia.
- `S/thunder-five-caster-seal.v2-try9.png`: ký hiệu sét và vòng ấn.
- `S/light-ground-mark-top.v1-try3.png`: độ hoàn thiện và cách bố trí một dấu đất tròn (chỉ lấy bố cục, không lấy màu vàng).

## Hình (hai phương án khác nhau về ý)
1. **Trận lôi vòng rune:** ba vòng đồng tâm, vòng ngoài khắc ký hiệu sét và lôi văn cổ, vòng giữa có năm nút sét sáng (đúng năm tia), vòng trong là lõi trắng xanh; các tia điện mảnh chạy nối ba vòng; vài hạt sáng; **tâm phần lớn trống** để tia giáng xuống đọc rõ.
2. **Trận lôi sao năm cánh:** vòng ngoài khắc lôi văn, bên trong một hình sao năm cánh bằng tia sét gãy khúc nối năm nút sáng trên vành, tâm là lỗ sáng nhỏ; mây điện mỏng lan ngoài vành.
Chung: **nhìn thẳng từ trên, tròn hoàn hảo, phẳng**, lõi trắng nóng, thân xanh điện, quầng lam thẫm, không tím, không cam vàng; nền đen thuần; lề ≥ 10 %; không chữ thật, chỉ ký hiệu trừu tượng; khổ 1:1; donghua tiên hiệp cao cấp, nhiều lớp, lấp lánh. Vẽ ở trạng thái **sáng đầy đủ** (engine tự làm hiện từ bé tới to).

## Kiểm và tự chấm
Nền, lề, tím ≤ 15 % vùng sáng, tròn đều (sai lệch bán kính ≤ 2 %). Tự chấm theo mặt yếu nhất: đọc ngay là trận pháp lôi; tâm đủ trống; cùng bộ trắng xanh; sang, cuốn hút; dùng làm khung đầu video. Dưới 8 vẽ lại một lần.

## Xong khi
2 ảnh + prompt + `S/thunder-formation-345-sheet.jpg` + báo cáo có bảng.
