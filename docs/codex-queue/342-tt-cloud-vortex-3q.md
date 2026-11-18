# Phiếu 342 · Tu Tiên · Ảnh 2D: xoáy mây kiếp góc ba phần tư (trắng xanh) cho Ngũ Lôi Oanh Đỉnh

Anh (12/11 01:1x): xoáy mây trong lab "nhìn nó kiểu bị lệch, cứ 2D sao sao"; lab đã dựng 3 đĩa nghiêng nhưng ảnh nhìn thẳng từ trên vẫn đọc như hình dán. Cần một ảnh **góc ba phần tư từ trên 35°** để thay. Chỉ vẽ ảnh, không sửa mã. Chạy sau phiếu 341.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 3 lần gọi `image_gen`** (1 ảnh, tối đa 2 lần vẽ lại). `view_image` tối đa 4. Báo cáo: `docs/codex-queue/342-report.md` (ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-five-cloud-vortex-3q.v2-try*.png` và `.prompt.txt`. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `S/thunder-five-cloud-vortex-top.v2-try1.png`: cùng thiết kế và bảng màu trắng xanh, chỉ đổi góc nhìn.
- `S/thunder-five-strike.v2-try9.png`: xoáy ở đỉnh ảnh này là dáng cần có khi nhìn nghiêng.

## Hình
Đĩa mây giông xoáy nhìn từ **ba phần tư, từ trên 35°**, nên thành elip có bề dày rõ: mép trước thấy thành mây cuộn dày, mép sau mỏng hơn; tâm là lỗ sáng trắng xanh hơi lõm xuống như phễu; năm mầm sét sáng ở vành trong; tia điện nhỏ chạy trong mây; vài sợi mây rủ xuống dưới đĩa. Lõi trắng nóng, thân xanh điện, quầng lam thẫm, tím chỉ ở rìa rất nhẹ. Nền đen thuần, lề ≥ 10 %, không chữ. Khổ 1:1. Phong cách donghua tiên hiệp cao cấp, nhiều lớp.

## Kiểm và tự chấm
Nền 4 góc gần đen; lề; tỉ lệ tím trong vùng sáng ≤ 15 % (đo như phiếu 338). Tự chấm theo mặt yếu nhất: có bề dày và phối cảnh rõ; cùng bộ với ảnh nhìn từ trên; nền sạch; dùng làm khung đầu video được. Dưới 8: vẽ lại một lần.

## Xong khi
Ảnh + prompt + tấm so cạnh nhau với ảnh nhìn từ trên `S/thunder-five-vortex-342-compare.jpg` + báo cáo.
