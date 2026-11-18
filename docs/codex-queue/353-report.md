# Phiếu 353 · Bộ Lôi D65 vẽ lại

Ngày thực hiện: 12/11/2026. Công cụ: image_gen tích hợp. Đã dùng **13/13 lượt** (10 ảnh đầu + 3 lượt vẽ lại), **7/16 lượt view_image** (6 tham chiếu + tấm ghép).

Đã tạo đủ 10 hình chủ đề, 3 bản vẽ lại, 13 prompt nguyên văn và tấm ghép. **Chưa đạt trọn bộ điều kiện kỹ thuật:** cả 10 bản chọn còn nhiễu 1/255 tại ít nhất một góc; tia A có lề phần mờ 9,81%, dưới 10%. Không ghi PASS tuyệt đối và không sửa ảnh bằng mã. Ba lượt vẽ lại đã dùng cho các lỗi lề lớn nhất ở đòn kết, B và C; giữ nguyên mọi bản đầu.

## Tệp bàn giao

Thư mục S: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

- [Tấm ghép 10 hình + cột đối chiếu v2](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-v3-353-sheet.jpg), 2040 × 1168; cột phải là đòn kết v2 và tia A v2, giữ nguyên màu để so sánh.
- Các bản chọn nằm trong bảng bên dưới. Mỗi PNG có prompt cùng tên gốc, đuôi `.prompt.txt`, ghi đúng đường dẫn và vai trò của ảnh tham chiếu.
- Ba bản đầu không chọn: `thunder-five-strike.v3-try1.png`, `thunder-single-bolt-b.v3-try1.png`, `thunder-single-bolt-c.v3-try1.png`, cùng prompt. Không xoá hay ghi đè.

Chỉ dùng sáu ảnh v2 của phiếu làm tham chiếu bố cục/góc nhìn. Ba lượt sửa dùng thêm chính bản v3 vừa tạo làm tham chiếu nét và màu. Không dùng ảnh ngoài repo. D65 được thực hiện theo mô tả trong phiếu: trắng ngà, quầng vàng nhạt ít bão hoà, nét mực khô nhiều nhánh; không kế thừa ống plasma xanh của v2. Hai mẫu đầu đã hiển thị cho chủ nhân trước khi tiếp tục bộ.

## Phép đo

Đọc PNG gốc bằng ImageMagick 7 thành RGB 8-bit, tính HSV bằng `colorsys.rgb_to_hsv`; không thay đổi ảnh. V = max(R,G,B)/255.

- Mẫu số của hai tỷ lệ màu: toàn bộ điểm ảnh có **V > 0,35**; không thêm ngưỡng S cho màu xanh/tím.
- Xanh/tím: H trong **190–300°**, yêu cầu ≤ 2%.
- Vàng sáng bão hoà: H trong **45–60°**, S > 0,8 và V > 0,85, yêu cầu ≤ 5%.
- Lề là khoảng cách của hộp bao mọi điểm có max(R,G,B) > 8 đến từng mép, theo thứ tự **trái / trên / phải / dưới**. Ngưỡng 8 loại nhiễu nền 1 mức nhưng vẫn bắt phần khói/nhánh mờ. Ghi thêm lề theo vùng sáng V > 0,35 ở cột kế.
- Bốn góc là bốn pixel ngoài cùng theo thứ tự **trên trái / trên phải / dưới trái / dưới phải**. Ký hiệu **B = (0,0,0)**, **G = (0,1,0)**, **Y = (1,1,0)**. Kiểm tra thêm bốn ô góc 10% kích thước: mọi ảnh có max kênh = **1/255**, không phải đen tuyệt đối.
- Các tỷ lệ 60/35/5 là mục tiêu trong mọi prompt, không phải số đo xác nhận phân bố màu của đầu ra.

| Bản chọn trong S | Kích thước | Điểm sáng | Xanh/tím % | Vàng bão hoà % | Lề >8, % (T/Tr/P/D) | Lề vùng sáng, % | Góc |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| `thunder-five-strike.v3-try2.png` | 941 × 1672 | 32519 | 0.0215 | 0.0000 | 21.36 / 29.49 / 23.17 / 30.44 | 24.87 / 29.61 / 24.97 / 31.52 | BBGG |
| `thunder-single-bolt-a.v3-try1.png` | 941 × 1671 | 45350 | 0.0375 | 0.0000 | 21.47 / 9.81 / 19.87 / 13.17 | 22.32 / 10.23 / 20.4 / 14.18 | BBGG |
| `thunder-single-bolt-b.v3-try2.png` | 941 × 1672 | 12384 | 0.0161 | 0.0000 | 32.62 / 27.09 / 33.16 / 27.45 | 33.79 / 27.57 / 34.43 / 28.17 | YBGG |
| `thunder-single-bolt-c.v3-try2.png` | 941 × 1672 | 11112 | 0.0810 | 0.0000 | 27.52 / 29.25 / 28.16 / 31.76 | 29.01 / 29.84 / 29.01 / 32.54 | YBGG |
| `thunder-single-bolt-d.v3-try1.png` | 941 × 1672 | 15734 | 0.5021 | 0.0000 | 28.8 / 21.89 / 29.54 / 25.36 | 29.97 / 22.91 / 31.03 / 26.2 | YBGG |
| `thunder-five-impact-burst.v3-try1.png` | 1254 × 1254 | 76984 | 0.2936 | 0.0000 | 10.93 / 17.46 / 10.77 / 22.81 | 12.28 / 17.78 / 12.04 / 23.68 | BBGG |
| `thunder-five-shock-ring-top.v3-try1.png` | 1254 × 1254 | 40473 | 0.1779 | 0.0000 | 13.72 / 11.8 / 14.04 / 17.22 | 13.8 / 13 / 15.47 / 18.18 | BBBG |
| `thunder-five-lingering-arcs.v3-try1.png` | 1672 × 941 | 26377 | 0.0531 | 0.0000 | 12.86 / 25.19 / 13.4 / 30.39 | 13.88 / 29.44 / 14.83 / 31.56 | BBBG |
| `thunder-five-caster-seal.v3-try1.png` | 1254 × 1254 | 56525 | 0.0265 | 0.0000 | 21.85 / 18.98 / 23.13 / 27.59 | 22.49 / 19.54 / 23.68 / 28.55 | BBGG |
| `thunder-five-cloud-ink.v3-try1.png` | 1672 × 941 | 2513 | 0.0000 | 0.0000 | 14.65 / 40.7 / 14.83 / 38.89 | 26.44 / 43.68 / 30.74 / 41.76 | BBGG |

**Kết quả:** 10/10 đạt hai ngưỡng màu. 9/10 đạt lề 10% ở ngưỡng >8; tia A chỉ đạt lề ở phần sáng (trên 10,23%) và **không đạt** khi tính phần mờ (9,81%). 0/10 đạt đen tuyệt đối ở đủ bốn pixel góc; mức sai lệch tối đa chỉ 1/255 nhưng vẫn phải ghi lỗi.

## Tự chấm mỹ thuật

Điểm là tự chấm nguồn ảnh, không phải nghiệm thu hiệu ứng chuyển động trong game. Thứ tự tiêu chí: nét mực mảnh/nhiều nhánh; bảng màu; sang và cuốn hút; đồng bộ cả bộ; dùng làm khung đầu video. Điểm cuối là **giá trị thấp nhất**. Các lỗi kỹ thuật phía trên vẫn giữ trạng thái không đạt dù điểm mỹ thuật ≥ 8.

| Hình | Nét | Màu | Hấp dẫn | Đồng bộ | Khung đầu | Thấp nhất | Nhận xét |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| thunder-five-strike | 8.5 | 8.8 | 8.5 | 8.6 | 8.5 | 8.5 | Năm tia riêng, nhánh dài dày, dải mây thấp; bố cục try2 nhỏ hơn để giữ lề. |
| thunder-single-bolt-a | 8.2 | 8.7 | 8.3 | 8.5 | 8.2 | 8.2 | Bốn–năm khúc gãy, ít nhánh chính; vài gối tia còn khá rộng. Lề mờ phía trên 9,81%. |
| thunder-single-bolt-b | 8.5 | 8.7 | 8.4 | 8.5 | 8.4 | 8.4 | Chẻ đôi rõ nửa dưới, rễ dài; try2 đã làm thân gọn hơn. |
| thunder-single-bolt-c | 8.3 | 8.7 | 8.4 | 8.5 | 8.4 | 8.3 | Trục xiên nhẹ, ba nhánh phụ dài; try2 giảm tính lặp zíc zắc. |
| thunder-single-bolt-d | 8.5 | 8.6 | 8.4 | 8.5 | 8.4 | 8.4 | Tia chính mảnh, hai tia vệ tinh tách rời; đủ khoảng đen. |
| thunder-five-impact-burst | 8.5 | 8.7 | 8.5 | 8.5 | 8.5 | 8.5 | Năm nhánh toé, mảnh đá, vòng sốc elip nhìn ngang đọc được. |
| thunder-five-shock-ring-top | 8.5 | 8.7 | 8.5 | 8.6 | 8.5 | 8.5 | Vòng nhìn thẳng từ trên, tâm trống; rễ mảnh ra ngoài. |
| thunder-five-lingering-arcs | 8.4 | 8.6 | 8.4 | 8.5 | 8.3 | 8.3 | Cung thấp và khói mực mỏng; vài đuôi vẫn hơi vươn cao, cần chủ nhân xem. |
| thunder-five-caster-seal | 8.5 | 8.6 | 8.5 | 8.6 | 8.5 | 8.5 | Vòng nhỏ, năm nét nối lõi với vành; không chữ, không bàn tay. |
| thunder-five-cloud-ink | 8.4 | 8.6 | 8.4 | 8.5 | 8.5 | 8.4 | Mây xám đen riêng, hai đầu tan; chỉ vài tia nhỏ bên trong. |

Ba bản đầu dưới 8 được vẽ lại đúng một lần:

| Bản đầu | Điểm yếu nhất | Lỗi chính | Bản vẽ lại |
| --- | ---: | --- | --- |
| thunder-five-strike.v3-try1 | 7,6 | Lề trái/phải 6,59% / 7,33% | v3-try2; lề nhỏ nhất 21,36% |
| thunder-single-bolt-b.v3-try1 | 7,5 | Lề trên/dưới 5,32% / 6,04% | v3-try2; lề nhỏ nhất 27,09% |
| thunder-single-bolt-c.v3-try1 | 7,7 | Lề trên 6,34%; trục còn quá lặp | v3-try2; lề nhỏ nhất 27,52% |

## Phần không làm và việc chủ nhân cần xem

- Không sửa mã, không tích hợp runtime, không mở cổng, không chạy build/test, không thao tác ghi Git. Không sửa các tệp đã có trước phiếu. Không tạo âm thanh hay video.
- Không hậu kỳ đổi màu, thêm lề hay xoá nhiễu trên PNG; mọi PNG bàn giao là bản sao nguyên vẹn từ image_gen. Chỉ tấm ghép được thu nhỏ và thêm nhãn bằng ImageMagick, font Arial đúng đường dẫn máy Mac.
- Đã hết hạn mức 13 lượt của phiếu; không tự mở lượt 14 hay xoá ảnh để làm lại. Không có HTTP 429 hoặc giờ reset do công cụ cung cấp.
- Chủ nhân xem nét tia A (một số gối còn rộng), độ thấp của tia sót, dải mây đòn kết và độ mảnh/lấp lánh toàn bộ trên tấm ghép. Bộ mới sáng tinh tế hơn, không còn mảng xanh điện phủ đặc.
- Còn cần xử lý nền 1/255 và lề A trước khi tuyên bố đáp ứng toàn bộ yêu cầu kỹ thuật. Không coi các giới hạn này là đã được chủ nhân chấp thuận.

