# Phiếu 336 · Bốn tia sét đơn cho Ngũ Lôi Oanh Đỉnh

Đã tạo đủ 4 ảnh bằng `image_gen`, cùng tham chiếu `thunder-five-strike.v1-try1.png`. Dùng 4/8 lượt tạo ảnh và 5/10 lượt `view_image`; không cần vẽ lại.

## Tệp bàn giao

Trong `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`:

- `thunder-single-bolt-a.v1-try1.png`: thân rất dày, năm đoạn gãy lớn, ít nhánh.
- `thunder-single-bolt-b.v1-try1.png`: chẻ đôi nửa dưới, nhiều nhánh nhỏ dạng rễ.
- `thunder-single-bolt-c.v1-try1.png`: xiên từ trên trái xuống giữa dưới, ba nhánh phụ dài.
- `thunder-single-bolt-d.v1-try1.png`: thân mảnh, nhiều khúc gấp nhanh, hai tia vệ tinh.
- Mỗi ảnh có tệp `.prompt.txt` cùng tên gốc, ghi công cụ, đường dẫn tham chiếu, prompt nguyên văn và khổ thật.
- `thunder-single-bolt-336-sheet.jpg`: bốn ảnh cạnh nhau có tên, 1776 × 805 px.

## Kiểm tra và tự chấm

Cả bốn ảnh là 941 × 1672 px, xấp xỉ 9:16 (sai lệch tỷ lệ 0,05%). ImageMagick đo lề theo điểm ảnh có kênh RGB lớn nhất > 8/255; đo nền ở ô 24 × 24 px tại mỗi góc.

| Ảnh | Lề trái / phải | Kênh lớn nhất ở bốn góc |
| --- | --- | --- |
| A | 17,11% / 21,68% | 1 / 1 / 2 / 1 |
| B | 6,59% / 7,12% | 1 / 1 / 2 / 1 |
| C | 7,97% / 8,71% | 1 / 1 / 2 / 1 |
| D | 29,01% / 29,12% | 1 / 1 / 1 / 1 |

Điểm tổng lấy mặt yếu nhất, theo thang tự chấm của phiếu; đây là đánh giá ảnh nguồn, chưa phải duyệt hiệu ứng trong game.

| Ảnh | Đọc hình sét | Đồng bộ ảnh gốc | Khác hình trong bộ | Nền, không chữ | Khung đầu video | Tổng |
| --- | --- | --- | --- | --- | --- | --- |
| A | 8,6 | 8,3 | 8,6 | 9,5 | 8,4 | **8,3** |
| B | 8,5 | 8,5 | 8,8 | 9,5 | 8,2 | **8,2** |
| C | 8,5 | 8,6 | 8,7 | 9,5 | 8,4 | **8,4** |
| D | 8,2 | 8,4 | 9,0 | 9,5 | 8,4 | **8,2** |

Anh xem tấm ghép để duyệt: lõi A rộng hơn ảnh gốc; hai ngọn B hội lại ở điểm chạm nên khi làm video cần giữ khoảng rỗng giữa chúng; D nhẹ hơn rõ rệt, đúng vai trò nhát phụ. Cả bộ giữ thân gãy khúc, ánh trắng–xanh điện–tím, không mây, mặt đất, chữ hay vỏ trụ.

Không đệm vì mọi lề đều đạt ≥ 6%; không vẽ lại vì không ảnh nào dưới 8. Không làm video, sửa mã, chạy build/test hay thao tác Git ghi. Không sửa tệp đã có trước phiếu.
