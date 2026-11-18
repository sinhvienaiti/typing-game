# Phiếu 356 · Vết sét in xuống đất · Bộ bạch kim D65

Ngày thực hiện: 12/11/2026. Công cụ: **image_gen tích hợp**, dùng **6/6 lượt**; **view_image 8/8 lượt** (4 tham chiếu, 3 ảnh kiểm tra trước khi chỉnh, 1 tấm ghép). Không dùng công cụ tạo ảnh khác.

Đã tạo đủ **3 ảnh chủ đề, 3 bản vẽ lại, 6 prompt nguyên văn và tấm ghép**. Ba ảnh chọn đạt lề ≥ 10% và hai ngưỡng màu. **Chưa đạt nền đen tuyệt đối:** mọi bản còn nhiễu nền tối đa 1/255 tại các ô góc. Lượt cuối yêu cầu xoá nhiễu bằng image_gen vẫn không khắc phục được. Không tuyên bố đạt toàn bộ yêu cầu kỹ thuật.

## Tệp bàn giao

S = `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

| Vai trò | Bản chọn trong S | Prompt trong S |
| --- | --- | --- |
| Đất nứt vừa bị sét đánh | `thunder-scar-crack-hot.v1-try2.png` | `thunder-scar-crack-hot.v1-try2.prompt.txt` |
| Vết cháy phân nhánh Lichtenberg | `thunder-scar-lichtenberg.v1-try2.png` | `thunder-scar-lichtenberg.v1-try2.prompt.txt` |
| Cùng vết nứt sau khi nguội | `thunder-scar-cooled.v1-try1.png` | `thunder-scar-cooled.v1-try1.prompt.txt` |

[Tấm ghép thunder-scar-356-sheet.jpg](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/thunder-scar-356-sheet.jpg), **1500 × 1096**: hàng trên giữ toàn khung để xem lề; hàng dưới phóng vùng giữa, cùng vùng cắt 760 × 760 tại (247,247). Nhãn dùng Arial của máy Mac. Đã sửa căn vùng cắt trên chính tấm ghép mới tạo, kiểm tra tâm vùng cắt bằng tọa độ; không vượt lượt view_image.

Giữ nguyên ba bản không chọn cùng prompt: `thunder-scar-crack-hot.v1-try1`, `thunder-scar-lichtenberg.v1-try1`, `thunder-scar-cooled.v1-try2` (mỗi tên có `.png` và `.prompt.txt`). Không xoá hoặc ghi đè ảnh nguồn hay tệp đã có trước phiếu.

## Tham chiếu và cách làm

- Chỉ đưa bốn ảnh thuộc repo mà phiếu chỉ định vào công cụ: `thunder-five-impact-burst.v4-try1.png`, `thunder-single-bolt-a.v4-try1.png` cho bảng trắng ngà/vàng nhạt và nét điện; `thunder-scorch-crack-top.v1-try1.png` cho bố cục từ trên; `dark-ground-mark-top.v1-try3.png` cho độ hoàn thiện đá. Không kế thừa màu xanh/tím, vòng ấn hoặc chữ của hai ảnh đất.
- Hai ảnh đầu đã hiển thị cho chủ nhân trước khi tiếp tục các lượt chỉnh. Hai lượt đầu của ảnh nóng và Lichtenberg thiếu lề nên mỗi hình được vẽ lại một lần.
- Ảnh nguội try1 được chỉnh trực tiếp từ ảnh nóng try2, khoá vị trí, tỷ lệ và sáu đường khe. Try2 nguội thử sửa nền, giữ thêm ảnh nóng làm tham chiếu; không chọn vì nền vẫn lỗi và một số mặt đá/nhánh nhỏ thay đổi hơn try1.
- PNG bàn giao là bản sao nguyên vẹn đầu ra công cụ; không đổi màu, thêm lề, xoá nền hoặc vẽ khe bằng mã. ImageMagick chỉ đọc số đo và tạo tấm ghép.

## Phép đo kỹ thuật

Đọc PNG bằng ImageMagick 7 thành RGB 8-bit và tính HSV bằng `colorsys.rgb_to_hsv`; không thay đổi PNG. Cách đo màu giữ đúng phiếu 353:

- Mẫu số: mọi pixel có **V > 0,35**, V = max(R,G,B)/255.
- Xanh/tím: **H từ 190–300°**, không thêm ngưỡng S; yêu cầu ≤ 2% trong vùng sáng.
- Vàng kim sáng bão hoà: **H từ 45–60°, S > 0,8, V > 0,85**; yêu cầu ≤ 5% trong vùng sáng.
- Lề: hộp bao mọi pixel có max(R,G,B) **> 8/255**, gồm đá, khói và nhánh mờ, bỏ nhiễu nền 1 mức. Thứ tự **trái / trên / phải / dưới**.
- Góc: bốn pixel ngoài cùng theo thứ tự trên trái / trên phải / dưới trái / dưới phải. **B = (0,0,0), G = (0,1,0), Y = (1,1,0)**. Kiểm thêm bốn ô góc 10%: cả sáu ảnh đều có giá trị kênh lớn nhất **1/255**, nên không được gọi là đen tuyệt đối.

Tất cả PNG đều **1254 × 1254**, đúng 1:1.

| Hình trong S | Chọn | Pixel sáng | Xanh/tím % | Vàng bão hoà % | Lề %, T/Tr/P/D | Góc |
| --- | --- | ---: | ---: | ---: | --- | --- |
| `thunder-scar-crack-hot.v1-try1.png` | Không | 205075 | 0,3038 | 0,0000 | 9,73 / 10,37 / 9,89 / 9,97 | BBGG |
| `thunder-scar-crack-hot.v1-try2.png` | **Có** | 91413 | 0,3632 | 0,0000 | 23,52 / 22,81 / 23,76 / 24,56 | BBGG |
| `thunder-scar-lichtenberg.v1-try1.png` | Không | 301875 | 0,0341 | 0,0000 | 11,00 / 8,53 / 12,20 / 11,96 | BBYG |
| `thunder-scar-lichtenberg.v1-try2.png` | **Có** | 103511 | 0,0000 | 0,0000 | 23,52 / 20,97 / 23,84 / 24,64 | BBGG |
| `thunder-scar-cooled.v1-try1.png` | **Có** | 35084 | 1,2456 | 0,0000 | 23,92 / 23,29 / 23,76 / 24,64 | BBGG |
| `thunder-scar-cooled.v1-try2.png` | Không | 60722 | 1,7852 | 0,0000 | 24,08 / 23,44 / 23,84 / 25,68 | BBGG |

**Kết quả bản chọn:** màu **3/3 đạt**, lề **3/3 đạt**, nền đen tuyệt đối **0/3 đạt**. Không thấy chữ, vòng tròn trơn hoặc ánh sáng xanh/tím bằng mắt; tỷ lệ xanh/tím ở trên vẫn tính cả sai khác rất nhỏ trong đá gần trung tính.

## Độ khớp nóng → nguội và tự chấm

Đối chiếu **nóng try2 → nguội try1**: ước lượng bằng mắt **90–95% trùng bố cục**, không phải chỉ số khớp pixel. Sáu tuyến khe chính cùng hướng, tâm và tỷ lệ gần như giữ nguyên; các mảnh đá nổi phía trên tâm, bên trái và bên phải vẫn ở vị trí tương ứng. Nhánh điện ngoài khe, khói và quầng sáng đã mất ở ảnh nguội theo yêu cầu; vài khe nhỏ và sắc độ mặt đá có thay đổi. Chưa thử chuyển mờ trong engine, vì phiếu chỉ cho vẽ ảnh.

Điểm dưới đây là tự chấm **nguồn ảnh**, không phải nghiệm thu hiệu ứng trong game hay điểm của hai giám khảo độc lập. Điểm cuối lấy mặt yếu nhất trong bốn tiêu chí mỹ thuật; lỗi nền vẫn là lỗi kỹ thuật riêng, không được điểm mỹ thuật xoá bỏ.

| Bản chọn | Đọc ra đất bị sét nứt/cháy | Có lực | Cùng bộ bạch kim | Đĩa tan mép, khả năng ghép sân | Thấp nhất |
| --- | ---: | ---: | ---: | ---: | ---: |
| Nứt rực try2 | 8,6 | 8,5 | 8,6 | 8,3 | **8,3** |
| Lichtenberg try2 | 8,5 | 8,2 | 8,6 | 8,3 | **8,2** |
| Nguội try1 | 8,5 | 8,2 | 8,5 | 8,3 | **8,2** |

- Nứt rực có sáu khe lớn lệch nhau, mép cháy, đá hơi bật và điện sót; đọc rõ hơn một vệt sáng mờ. Nét sáng ở nhánh đông bắc còn khá nổi trên khe, chủ nhân nên xem.
- Lichtenberg phân nhánh mảnh, tâm cháy nhỏ, phần ngoài tối hơn. Một số nhánh vẫn còn ánh nhạt vượt quá nửa trong; không coi độ dài phát sáng là đã khớp tuyệt đối brief.
- Nguội giữ khe tối, tro xám trắng và ít chấm đỏ rất nhỏ; sắc đá hơi lạnh hơn ảnh nóng do mất quầng vàng. Không có dải dung nham cam.
- Hai bản đầu nóng và Lichtenberg có điểm ghép sân **7,8** do thiếu lề, nên đã vẽ lại đúng một lần. Bản nguội đầu không dưới 8; dùng lượt thứ sáu để thử sửa lỗi nền còn lại. Nguội try2 không cải thiện nền, nên giữ try1 làm bản chọn.

## Phần không làm và chủ nhân cần xem

- Không sửa mã, tích hợp runtime, thay ảnh đã dùng trong game, mở cổng, chạy build/test, tạo video/âm thanh hay thao tác ghi Git. Không chỉnh tệp của tác nhân khác. Chỉ thêm tệp đúng S và báo cáo này; không mở rộng sang bảng công việc, manifest hay thư mục review ngoài phạm vi phiếu.
- Chưa xác nhận kiểu ghép nền trong engine và chưa kiểm chuyển mờ thực tế. Nền đen là ảnh RGB có nhiễu 1/255, không phải alpha. Đặc biệt ảnh nguội có khe tối nên cần xem cách ghép thực tế trên sân khi có phiếu tích hợp riêng.
- Chủ nhân xem tấm ghép để chọn độ rộng khe nóng, độ tinh của Lichtenberg và mức giữ bố cục ảnh nguội. Bộ này chưa được nghiệm thu 8,5 trong play host.
- Đã chạm giới hạn **6 lần image_gen** của phiếu; không gọi lượt thứ bảy. Không có HTTP 429 hay giờ reset do công cụ trả về. Vấn đề chưa xử lý là nền đen tuyệt đối; giữ toàn bộ ảnh và prompt để tiếp tục từ hiện trạng nếu được giao lượt xử lý tiếp theo.
