# Phiếu 345 · Trận pháp lôi nhìn thẳng từ trên

**Đã đủ ảnh và prompt; hai bản chọn tự chấm đạt ngưỡng 8 của phiếu.** Chạy sau báo cáo kết thúc phiếu 344. Dùng image_gen tích hợp, **4/4 lượt vẽ**, mỗi phương án vẽ lại một lần; **6/6 lượt view_image**. Không gặp giới hạn dịch vụ.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

| Phương án | PNG chọn trong S | Điểm yếu nhất |
| --- | --- | --- |
| A · Ba vòng rune, năm nút sét, tâm rộng | `thunder-formation-top.v1-try2-black.png` | **8,2** |
| B · Sao năm cánh bằng sét, lỗ sáng nhỏ, mây điện ngoài vành | `thunder-formation-top-b.v1-try2-black.png` | **8,3** |

Mở **`S/thunder-formation-345-sheet.jpg`**: hàng trên là nguồn AI lượt 2, hàng dưới là hai bản chọn đã làm sạch nền. Giữ cả bốn ảnh AI `*.v1-try1.png` / `*.v1-try2.png`; không ghi đè. Mỗi PNG có prompt AI chính xác cạnh ảnh dưới tên `<tên>.prompt.txt`; tấm ghép có mô tả thao tác riêng. Tổng cộng thêm 6 PNG, 1 JPG, 7 prompt và báo cáo này.

Đã xem và đưa đúng ba tham chiếu của phiếu vào cả bốn lượt vẽ: `thunder-five-shock-ring-top.v2-try1.png` cho góc/bảng màu/tia; `thunder-five-caster-seal.v2-try9.png` cho vòng ấn; `light-ground-mark-top.v1-try3.png` chỉ cho bố cục và độ hoàn thiện, không lấy vàng. Đường dẫn tuyệt đối và vai trò từng ảnh đều có trong prompt. Áp dụng imagegen, game-vfx-production, game-art-pipeline và agent-orchestration theo phiếu ảnh đã chốt.

## Kiểm kỹ thuật

Hai lượt đầu có lề sáng chỉ khoảng 6–8%, tự chấm **7,7**, nên đã vẽ lại với trận pháp nhỏ hơn trong khung. Nguồn lượt 2 còn nhiễu nền mức RGB 1. Bản `-black` dùng ImageMagick 7 đổi **chỉ** pixel có max(R,G,B) ≤ 1 thành RGB(0,0,0); giữ nguyên mọi pixel khác, khổ và hình dạng. Không cắt, kéo giãn hoặc vẽ bổ sung.

| Bản chọn | Khổ | Lề trái / trên / phải / dưới | Tím trong vùng sáng | Sai lệch bán kính ước lượng |
| --- | --- | --- | --- | --- |
| A | 1254×1254 | 17,86 / 16,11 / 18,26 / 20,65% | 0% | 1,99% |
| B | 1254×1254 | 18,74 / 16,99 / 19,22 / 23,37% | 0% | 1,24% |

Lề tính trên mọi pixel khác đen của PNG chọn; toàn bộ dải ngoài 10% là đen thuần. Tím: hue 255–315°, saturation > 0,15, vùng sáng max(R,G,B) > 32/255. Độ tròn là ước lượng đường vòng sáng chính từ 360 hướng với tâm khớp tự do, lấy sai lệch lớn nhất; không tính tia nhánh, mây và hoa văn nhô ngoài vành. Đây là đo raster, không phải chứng nhận đường tròn vector chính xác.

## Tự chấm theo mặt yếu nhất

| Bản chọn | Nhận ra trận lôi | Tâm đủ trống theo phương án | Cùng bộ trắng xanh | Sang, cuốn hút | Làm khung nguồn video | Thấp nhất |
| --- | --- | --- | --- | --- | --- | --- |
| A | 8,8 | 9,0 | 9,0 | 8,2 | 8,5 | **8,2** |
| B | 8,7 | 8,4 | 9,0 | 8,3 | 8,4 | **8,3** |

Đếm được đúng năm nút chính ở mỗi ảnh. Cả hai phẳng, nhìn từ trên, sáng đầy đủ, không thấy chữ thật hoặc màu vàng/tím. A có tâm đen rộng; B đọc rõ sao năm cánh và lỗ sáng nhỏ. Hoa văn A còn hơi thiên trang sức; B dày tia hơn ở các giao điểm. Điểm là tự chấm ảnh nguồn, chưa xác nhận chuyển động hoặc hiệu quả trong game.

Không sửa mã, file có sẵn hoặc Git; không chạy build/test, mở cổng, tạo video hay tích hợp. Không ghi vào thư mục review ngoài phạm vi phiếu. Chủ nhân cần chọn A hoặc B trên tấm ghép; ưu tiên A nếu muốn khoảng trống lớn cho tia giáng xuống.
