# Phiếu 350 · Tu Tiên · Bộ bốn góc nhân vật chính, vòng 4

**Đã tạo đủ năm tên ảnh yêu cầu, prompt và tấm kiểm. Bộ ảnh chưa đạt nghiệm thu 8,5.** Đã dùng **8/8 lần image_gen**, **14/14 lần view_image**; ba lần vẽ lại dành cho trước, sau và góc chơi. Chỉ thêm tệp `H/r4-*` và báo cáo này, với `H = games/immortality-cultivation/art-src/heroine`. Không sửa tệp vòng 3, mã, docs Tu Tiên, chạy build/test, mở cổng hoặc ghi Git.

## Tệp bàn giao và bản chọn

| Tệp trong H | Vai trò |
| --- | --- |
| `r4-turnaround.v1-try1.png` | Bản chọn; bốn góc trước, trái, sau, phải; 2048×1152 |
| `r4-view-front.v1-try1.png` | Giữ lần đầu theo tên yêu cầu; loại vì vai vẫn cứng, hoa văn còn bận |
| `r4-view-front.v1-try2.png` | **Bản trước được chọn**; vai dốc mềm, tay áo có nếp lớn |
| `r4-view-back.v1-try1.png` | Giữ lần đầu; đã bỏ đĩa nhưng vai chưa đồng bộ |
| `r4-view-back.v1-try2.png` | **Bản sau được chọn**; phượng thêu phẳng, lưng chàm yên |
| `r4-view-left.v1-try1.png` | **Bản trái được chọn**; mép lưng không còn đĩa nhô |
| `r4-view-play.v1-try1.png` | Giữ lần đầu; loại vì đỉnh diadem quay về phía sau |
| `r4-view-play.v1-try2.png` | **Bản chơi được chọn**; đã sửa vòng sau và đỉnh ở phía trán |
| `r4-350-sheet.jpg` | Tấm tổng hợp 1920×2358: ảnh chọn, turnaround, so mặt và ô 66 px/phóng 4× |
| `r4-350-face-compare.jpg` | So mặt trực tiếp với front vòng 3 |
| `r4-350-views.jpg`, `r4-350-pixels.jpg` | Hàng ảnh đơn và bảng đọc nhỏ riêng |
| `r4-350-back-66.png`, `r4-350-play-66.png` | Ô 66×66 px thực, nhân vật cao 66 px |
| `r4-350-back-66-4x.png`, `r4-350-play-66-4x.png` | Bản phóng nearest-neighbour 264×264, không thêm chi tiết |
| `r4-350-checks.json` | Hộp bao, lề, nền, chênh chiều cao và ghi nhận tỷ lệ phượng |

Mọi ảnh có `.prompt.txt` cùng tên. Tám ảnh `*-raw.png` giữ nguyên đầu ra công cụ và có bản prompt nguyên văn; ảnh chuẩn hóa cùng stem giữ nguyên prompt đó. Tấm ghép có mô tả thao tác cơ học riêng.

## Tham chiếu và cách làm

Đã xem đủ năm tham chiếu được chỉ định: front/back/left/play try2/turnaround vòng 3. Không dùng ảnh bên ngoài repo. Front vòng 3 khóa mặt, tóc, diadem và màu; ảnh vòng 4 trước/sau đã tạo được đưa vào các góc tiếp theo để đồng bộ trang phục. Mỗi prompt liệt kê đủ 12 chi tiết và câu “same face, hair and diadem as the reference front view”.

Đã bỏ đĩa, lót dày và móc treo tấm phượng; hình phượng nằm trên mặt vải chàm liên tục từ cổ xuống đai. Hoa văn hạc lớn gom về cổ và dải gấu; vai có độ dốc và mép rủ, bỏ lớp vai phụ dạng giáp. Giữ áo ngắn xẻ, quần, ủng, ngọc trái và kiếm thấp. Không chuyển về váy dài.

Hậu xử lý bằng ImageMagick 7 chỉ khóa nền xanh, trim và thu phóng đồng dạng rồi căn giữa; không vẽ lại mặt, áo hoặc hoa văn bằng mã. Ảnh đơn đặt trên 1152×1536, giới hạn hình 968×1228; góc chơi 960×1228. Turnaround trên 2048×1152, giới hạn hình 1720×920. Nền xanh đầu ra thô có dao động nhỏ, bản bàn giao đã khóa RGB(0,255,0).

## Kiểm nền, lề và chiều cao

Hộp bao loại pixel xanh trội: G > 150, G > 1,6R và G > 1,6B. Chênh chiều cao tính theo (lớn nhất − nhỏ nhất) / nhỏ nhất.

| Ảnh chọn | Khổ | Cao hình | Lề nhỏ nhất |
| --- | --- | ---: | ---: |
| Trước try2 | 1152×1536, 3:4 | 1227 px | 10,026% |
| Sau try2 | 1152×1536, 3:4 | 1226 px | 10,091% |
| Trái try1 | 1152×1536, 3:4 | 1227 px | 10,026% |
| Chơi try2 | 1152×1536, 3:4 | 1226 px | 8,420% |
| Turnaround try1 | 2048×1152, 16:9 | 918 / 916 / 919 / 915 px | 9,717% ở mép ngoài |

Chênh ảnh đơn **0,082%**, turnaround **0,437%**: đều dưới 3%. Bốn góc ảnh và toàn dải biên 64 px đều đúng nền xanh, không có pixel lệch trong dải này. Viền khử răng cưa sát nhân vật có màu pha tự nhiên. Không thấy chữ, hào quang hoặc bóng đổ nền.

Góc chơi thấy mặt trên đầu/vai, đầu và thân cùng hướng, hai tay rõ. 55° nhìn xuống và lệch sau 30° là chỉ dẫn tạo ảnh; ảnh raster không có ma trận camera để chứng minh chính xác. Ánh sáng 45° trên phải cũng chỉ kiểm được hướng nhìn bằng mắt.

## Bảng nhất quán 12 chi tiết × 4 góc

Đối chiếu bốn góc trên turnaround với các ảnh đơn được chọn. “Khuất” là che khuất theo góc nhìn.

| Chi tiết | Trước | Trái | Sau | Phải |
| --- | --- | --- | --- | --- |
| 1. Mặt chuẩn vòng 3 | Cùng nhận diện; xem so mặt | Cùng nét nghiêng | Khuất | Cùng nét nghiêng |
| 2. Tóc đen, búi cao gọn, tóc mai | Có | Có | Cùng búi | Có |
| 3. Một vòng diadem, đỉnh ngọc trước, hai tua bên | Có | Tua xa khuất một phần | Vòng sau, đỉnh trước ló trên búi | Tua xa khuất một phần |
| 4. Cổ cao ngà, tấm cổ Nhật Bình mỏng | Có; mép mềm | Rủ theo vai | Rủ theo vai | Rủ theo vai |
| 5. Tay trong ngà, nếp lớn ở bắp tay, bó từ khuỷu | Có | Có | Có | Có |
| 6. Áo chàm ngắn rủ dọc, xẻ hông/sau | Hai vạt trước | Xẻ hông | Xẻ sau | Xẻ hông |
| 7. Viền ngà/vàng cũ, hạc/mây ở cổ và dải gấu | Cùng vị trí | Có | Có | Có |
| 8. Một phượng thêu phẳng trên lưng chàm | Khuất | Cạnh vải phẳng; phượng khuất phần lớn | Có; không đĩa/lót | Cạnh vải phẳng |
| 9. Đai chàm, vàng cũ, khóa ngọc hoa trắng | Có | Một phần khuất | Có | Một phần khuất |
| 10. Ngọc bội tròn và tua ở hông trái | Bên phải ảnh | Bên gần | Bên trái ảnh, khuất một phần | Khuất đúng bên xa |
| 11. Hai đuôi sau, quần tối suông, ủng có gót | Quần/ủng rõ | Gót rõ | Hai đuôi/gót rõ | Gót rõ |
| 12. Kiếm thấp ở xương cùng, chuôi phải, hai đai treo | Khuất phần lớn | Chiếu ngắn | Kiếm ngang, hai đai rõ | Chiếu ngắn, chuôi bên gần |

Bố cục và vị trí ổn định; nét thêu, hạt đai và độ cong tua vẫn có sai khác nhỏ giữa các ảnh sinh. Ở play try2 đã bỏ đỉnh trang trí quay sau, còn vòng mảnh và đúng hai tua, đỉnh ngọc trước chỉ ló phía xa. Độ cong vòng và khoảng cách hoa bên chưa trùng tuyệt đối với các góc trực giao.

## Kiểm 66 px và so mặt

Ô kiểm lấy trực tiếp từ ảnh chọn, trim phần nền, thu đồng dạng vào 66×66. Bản 4× dùng nội suy điểm, không làm nét.

| Mảng mục tiêu | Sau 66 px | Chơi 66 px |
| --- | --- | --- |
| Tóc đen | Rõ, nhỏ hơn ở góc chơi | Rõ, mảng lớn |
| Vai ngà | Rõ | Rõ |
| Lưng chàm | Rõ | Rõ |
| Đốm phượng vàng tròn | Có, đọc thành vòng vàng; không đọc nét chim | Có, tròn bị ép theo phối cảnh |
| Quần tối | Rõ | Rõ; chân ngắn do phối cảnh |
| Kiếm ngang | Nhận ra nhờ thanh ngang và đầu vàng nhô hai bên | Nhận ra; gần đai, tương phản còn hạn chế |
| **Số mảng tự đọc được** | **6/6** | **6/6** |

Không tính các chấm viền/hạc vào sáu mảng chính. Ở 66 px, họa tiết gấu vẫn tạo dải sáng phụ và kiếm chưa tách thật mạnh khỏi đai. Đọc đủ sáu mảng không đồng nghĩa đạt sức hút 8,5.

Tấm so mặt dùng cùng vùng crop và tỷ lệ, không sửa hoặc ghép mặt. Mắt, mũi, môi, tóc mai và diadem giữ cùng nhận diện với vòng 3; vẫn có dao động nhỏ ở độ mở mắt và nét môi do tái sinh, **không phải giữ nguyên từng pixel**. Anh cần chốt bằng tấm so mặt.

## Điểm chưa đạt và tự chấm theo mặt yếu nhất

| Hạng mục | Kết quả |
| --- | --- |
| Phượng thêu phẳng, bỏ vật thể lạ | Đạt về cách đọc vải; không còn cạnh đĩa ở profile |
| Vai mềm và nếp tay lớn | Đã sửa; cổ có xu hướng thành khăn choàng, tính vuông Nhật Bình chưa thật sắc |
| Phượng đường kính 25% chiều cao | **Chưa đạt**: ước lượng thủ công trên back try2 khoảng 14–15%; prompt đã yêu cầu 25% cả hai lượt |
| Viền bản rộng ≥3% chiều cao | **Chưa đạt đồng đều**: cần khoảng 36,8 px trên ảnh đơn; nhiều mép dọc và gấu vẫn hẹp hơn, ước lượng khoảng 1–2% |
| Chàm yên, hoa văn tập trung | Đạt mảng chính ở lưng; vân dệt chìm và dải gấu còn nhiều nét phụ |
| Màu 60 ngà / 30 chàm / 10 vàng cũ | Giữ bảng màu; chưa xác nhận đúng tỷ lệ diện tích 60/30/10, góc sau thiên chàm |

| Ảnh | Điểm yếu nhất tự chấm | Lý do chính |
| --- | ---: | --- |
| Trước try1 | 7,4 | Vai cứng, chưa giảm đủ hoa văn; đã vẽ lại |
| Trước try2 | 8,0 | Viền còn hẹp, cổ chưa thật vuông |
| Sau try1 | 7,6 | Vai cứng, chưa đồng bộ tay; đã vẽ lại |
| Sau try2 | 7,8 | Tỷ lệ phượng và viền chưa đúng con số phiếu |
| Trái try1 | 8,0 | Viền hẹp; mặt và cấu tạo lưng giữ được |
| Chơi try1 | 7,2 | Diadem quay ngược; đã vẽ lại |
| Chơi try2 | 8,0 | Sửa được diadem; viền và độ chính xác camera còn hạn chế |
| Turnaround try1 | 8,0 | Nhất quán bố cục; còn cùng sai lệch tỷ lệ phượng/viền |

Bộ chọn theo mặt yếu nhất: **7,8/10, chưa đạt**. Đã dùng hết ba lần vẽ lại và 8 lần gọi được phép; không tạo lượt thứ chín. Đây là tự kiểm của một người, không thay cho hai giám khảo mù. Không đánh dấu chấp nhận thương mại hoặc sẵn sàng dựng mesh.

Không làm thêm nghiên cứu hướng mới, giám khảo ngoài, 3D, tích hợp runtime hoặc ghi sang thư mục review chung vì ngoài các đường dẫn phiếu cho phép. Không gặp HTTP 429 hoặc thời gian chờ do công cụ.

**Anh cần xem:** `r4-350-sheet.jpg`, nhất là mặt, tính vuông của cổ mềm, ô 66 px và hai tỷ lệ chưa đạt. Dùng front/back/play **try2** cho đối chiếu; các try1 bị loại chỉ giữ làm lịch sử.

