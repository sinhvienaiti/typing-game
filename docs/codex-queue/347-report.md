# Phiếu 347 · Tu Tiên · Bộ bốn góc nhân vật chính, vòng 3

**Đã tạo đủ 5 tên ảnh theo phiếu và prompt đi kèm.** Có thêm `r3-view-play.v1-try2.png`, là bản góc chơi được chọn thay cho try1. Dùng image_gen tích hợp, **6/8 lần gọi**; view_image **12/14 lần**. Không sửa mã, chạy build/test, mở cổng hay ghi Git.

## Tệp bàn giao

Gốc ảnh: `games/immortality-cultivation/art-src/heroine/`.

| Tệp | Vai trò |
| --- | --- |
| `r3-turnaround.v1-try1.png` | Bốn góc trước, trái, sau, phải; 2048×1152 |
| `r3-view-front.v1-try1.png` | Ảnh trước; 1152×1536 |
| `r3-view-back.v1-try1.png` | Ảnh sau; 1152×1536 |
| `r3-view-left.v1-try1.png` | Ảnh trái; 1152×1536 |
| `r3-view-play.v1-try1.png` | Lần đầu, **loại vì camera còn thấp**; giữ để đối chiếu |
| `r3-view-play.v1-try2.png` | Góc chơi chọn bàn giao; 1152×1536 |
| `r3-347-sheet.jpg` | Toàn bộ ảnh chọn, turnaround, so mặt, cận ủng, ô 66×66 px |
| `r3-347-face-compare.jpg` | Mặt chuẩn vòng 2 bên trái, mặt vòng 3 bên phải |
| `r3-347-checks.json` | Số đo nền, lề, hộp bao và chênh chiều cao |

Mỗi ảnh sinh có prompt nguyên văn `.prompt.txt` cùng tên. Sáu bản `*-raw.png` giữ ảnh gốc từ công cụ, cũng có prompt. Hai tấm kiểm có tệp mô tả cách ghép; không gọi image_gen cho chúng.

## Tham chiếu và cách làm

Đã xem đủ năm ảnh được chỉ định: front/back/left/turnaround vòng 2 và `identity/kiem-tu-portrait.png`. Không dùng ảnh bên ngoài repo. Ảnh front vòng 2 khóa mặt, tóc, diadem; portrait chỉ dẫn độ rủ áo chàm. Các góc sau dùng ảnh vòng 3 trước đó làm đầu vào để giữ trang phục.

Thêm áo khoác chàm không tay, mở trước, dài giữa đùi, xẻ hông và sau; tà có lớp lót và mép dày. Cổ Nhật Bình đặt trên áo khoác. Tấm phượng có cạnh và dây/khuy gắn phía vai, thắt lưng. Ngọc bội giữ ở hông trái; góc phải và góc chơi bị khuất. Kiếm vẫn nằm thấp ở xương cùng, chuôi bên phải, có hai đai treo.

Hậu xử lý cơ học bằng ImageMagick 7: khóa nền xanh với `-fuzz 12% -transparent '#00FF00'`, trim, thu phóng đồng dạng và đặt giữa nền `#00FF00`. Ảnh đơn dùng khung 1152×1536, giới hạn hình 968×1228; riêng play try2 dùng 960×1228 để lề ngang vượt 8%. Turnaround dùng khung 2048×1152, giới hạn hình 1720×920. Không vẽ đè mặt, trang phục hay chi tiết bằng mã.

## Kiểm kỹ thuật

Hộp bao đo bằng cách loại pixel xanh trội: G > 150, G > 1,6R và G > 1,6B. Chênh chiều cao là chênh hộp bao trên ảnh; góc chơi có phối cảnh riêng, không phải phép đo chiều cao cơ thể thực.

| Ảnh | Khổ | Chiều cao hình | Lề nhỏ nhất |
| --- | --- | ---: | ---: |
| Trước try1 | 3:4 | 1227 px | 10,026% |
| Sau try1 | 3:4 | 1226 px | 10,091% |
| Trái try1 | 3:4 | 1227 px | 10,026% |
| Chơi try2 | 3:4 | 1211 px | 8,333% |
| Turnaround | 16:9 | 917 / 916 / 917 / 915 px | 8,789% ở mép ngoài |

- Chênh chiều cao ảnh đơn: **1,321%**, dưới 3%; bốn góc trên turnaround: **0,219%**.
- Bốn góc ảnh và toàn dải viền trống 64 px đều đúng RGB(0,255,0); không có pixel lệch trong dải này. Viền khử răng cưa sát hình có màu pha.
- Không thấy chữ, hào quang hay bóng đổ nền. Ánh sáng đọc từ trên phải; 45° là chỉ dẫn tạo ảnh, không phải thông số có thể khôi phục chính xác từ raster.
- Ô sau/chơi là **66×66 px thực**, hình nằm trong 54×54 px; bên dưới có bản phóng nearest-neighbour 4×. Ở kích thước này nhận ra tấm phượng, tóc và kiếm; chi tiết thêu, móc và đường ráp không còn đọc rõ.

## Bảng nhất quán 12 chi tiết × 4 góc

Kiểm trên turnaround, đối chiếu ba ảnh đơn. “Khuất” là che khuất đúng hình học, không phải chi tiết bị bỏ.

| Chi tiết nhận dạng | Trước | Trái | Sau | Phải |
| --- | --- | --- | --- | --- |
| 1. Mặt donghua vòng 2 | Cùng nhận diện; xem tấm so | Cùng nét nghiêng | Khuất | Cùng nét nghiêng |
| 2. Búi tóc đen, ngôi và tóc mai | Có | Có | Cùng búi | Có |
| 3. Diadem vàng cũ, hoa trắng, tua đôi | Có | Một tua che một phần | Hai tua | Một tua che một phần |
| 4. Áo trong ngà, cổ cao, tay hẹp | Có | Có | Có | Có |
| 5. Cổ Nhật Bình lõi chàm, rìa ngà | Có | Ôm vai | Cùng mảng cổ sau | Ôm vai |
| 6. Áo ngoài chàm mở, xẻ hông/sau | Hai vạt trước | Xẻ hông rõ | Tà sau tách | Xẻ hông rõ |
| 7. Tà chính dày, quần suông, hai đuôi | Tà ngà và quần | Thấy lớp mép | Hai đuôi, quần | Thấy lớp mép |
| 8. Viền mây hạc, ngà/chàm/vàng cũ | Có | Có | Có | Có |
| 9. Đai chàm, khóa hoa trắng | Khóa giữa | Khóa khuất một phần | Chi tiết đai sau | Khóa khuất một phần |
| 10. Một ngọc bội ở hông trái, tới giữa đùi | Phải ảnh | Bên gần | Một phần trái ảnh | Khuất đúng |
| 11. Tấm phượng có lót, gắn vai/đai; kiếm thấp chuôi phải | Phần lớn khuất | Cạnh tấm và đai | Mặt phượng, điểm gắn, hai đai kiếm | Cạnh dày và điểm gắn |
| 12. Cùng ủng, thêu bên, gót/đế/ráp sau | Mũi trước | Thêu bên, gót | Gót, đế và ráp sau | Thêu bên, gót |

Độ dài ngọc bội cùng kết thúc trong vùng giữa đùi; độ rủ chuỗi và chi tiết hạt có dao động nhỏ giữa ảnh sinh. Tỷ lệ 60/30/10 được kiểm bằng thị giác, chưa phân vùng vật liệu để đo diện tích chính xác.

## Kiểm riêng ủng sau và tấm lưng

| Hạng mục | Sau đơn | Sau trên turnaround |
| --- | --- | --- |
| Gót của cả hai ủng | **Có** | **Có** |
| Đế/mép sau của cả hai ủng | **Có** | **Có** |
| Đường ráp dọc sau | **Có** | **Có** |
| Hoạ tiết mũi giày quay ra sau | **Không** | **Không** |
| Hai chân cùng quay ra xa camera | **Có** | **Có** |

Tấm lưng đã có hai điểm gắn phía vai và các điểm nối xuống đai. Cạnh dày đọc được ở profile phải. Chất liệu được chỉ định là vải thêu có lót cứng; đường viền vàng và phượng nổi vẫn có thể khiến người xem đọc như phù điêu cứng. **Chưa thể chứng nhận độ dày thực 1–2 cm từ ảnh 2D.**

## Mặt và camera chơi

Tấm so mặt lấy trực tiếp từ front vòng 2 và front vòng 3, chỉ crop/resize. Giữ nhận diện mắt, mũi, môi, tóc và diadem; vẫn có sai khác nhẹ ở độ đầy má và độ mở mắt do tái sinh ảnh. **Anh cần xem tấm so để chốt yêu cầu giữ nguyên mặt; không coi đây là trùng pixel.**

Play try1 tự chấm **6,8/10**, loại vì góc nhìn còn thấp. Đã vẽ lại một lần thành try2: thấy mặt trên đầu/vai, tấm lưng bị ép mạnh theo chiều dọc, chân rút ngắn, đầu cùng hướng thân, hai tay thấy, ngọc bội trái khuất. Prompt khóa camera nhìn xuống 55° và lệch phải 30°. **Raster không có ma trận camera; chỉ xác nhận hình ảnh nhìn dốc, chưa chứng minh chính xác 55°/30°.**

## Tự chấm theo mặt yếu nhất

| Ảnh chọn | Điểm yếu nhất tự chấm | Điều còn cần xem |
| --- | ---: | --- |
| Trước try1 | 8,2 | Mặt và độ mềm của vai dưới cổ Nhật Bình |
| Sau try1 | 8,3 | Vải thêu có lót còn dễ đọc như tấm cứng |
| Trái try1 | 8,0 | Cạnh lót, độ rủ và các lớp che nhau |
| Turnaround try1 | 8,0 | Chi tiết thêu/chuỗi ngọc có dao động nhỏ |
| Chơi try2 | 8,0 | Độ chính xác camera và kích thước đầu do phối cảnh |

Bộ chọn tự chấm theo mặt yếu nhất: **8,0/10**. Ảnh dưới 8 đã được vẽ lại; không cần dùng hết ngân sách 8 lần gọi. Đây **không phải kết quả hai giám khảo mù và chưa đạt nghiệm thu 8,5**.

Không làm thêm 3D, tích hợp runtime, nghiên cứu hướng mới hay vòng giám khảo ngoài phạm vi phiếu. Không ghi sang thư mục review chung vì phiếu chỉ cho phép `H/r3-*` và báo cáo này. Không gặp giới hạn công cụ.

**Anh cần xem:** `r3-347-sheet.jpg`, đặc biệt tấm so mặt, vai áo, chất liệu tấm lưng và play try2. Không dùng play try1 cho bước tiếp theo.

