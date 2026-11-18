# Phiếu 416 — Dải nền cut-in tuyệt kỹ cho 14 hệ

Ngày: 16/11/2026. Người làm: Codex. Phiếu có phản biện PASS (Sonnet, 16/11).

## Kết quả

Đã gọi **image_gen 16 lần, thành công 16 lần**: một ảnh cho mỗi hệ và hai lượt làm lại fire, ice. Có đủ 14 hệ theo phiếu. Không tạo video, nhân vật, sinh vật hay chữ trong các dải nền.

Thư mục giao nộp: `games/immortality-cultivation/art-src/concept/cutin-bands/`.

- 16 PNG theo mẫu `cutin-<hệ>.v1-try<k>.png`.
- 16 prompt thực tế theo mẫu `cutin-<hệ>.v1-try<k>.prompt.txt`, lưu nguyên nội dung đã gửi image_gen, có đường dẫn và vai trò của ảnh tham chiếu.
- [Ảnh ghép cutin-bands-sheet-416.jpg](../../games/immortality-cultivation/art-src/concept/cutin-bands/cutin-bands-sheet-416.jpg), 1968×2992, hai cột, tám hàng.
- `cutin-bands-sheet-416.prompt.txt`: ghi rõ ảnh ghép được tạo cơ học, kèm lệnh ImageMagick chính xác.

Bảy hàng đầu của ảnh ghép là 14 lựa chọn đề xuất. Hàng cuối giữ fire try1 và ice try1 để so sánh; không xóa hay ghi đè các bản này. Hai mẫu đầu metal và wood đã hiển thị cho owner trong hội thoại trước khi tạo phần còn lại.

## Ảnh đề xuất và kiểm tra nguồn

Đây là kiểm tra độ phù hợp của **ảnh nguồn**, không phải chấp nhận hiệu ứng hoàn chỉnh trong game. Không chấm điểm 8.5 cho một lớp nguồn và chưa tuyên bố đạt nghiệm thu trong play host.

| Hệ | Tệp đề xuất | Đặc trưng | Kiểm tra nguồn |
| --- | --- | --- | --- |
| metal | `cutin-metal.v1-try1.png` | Bạch kim, vàng champagne, lụa kim loại và bụi sáng | Phù hợp làm mẫu nguồn |
| wood | `cutin-wood.v1-try1.png` | Xanh ngọc, sợi vàng, phấn sáng | **Cần xem mép phải trước khi dùng video** |
| water | `cutin-water.v1-try1.png` | Xanh lam–cyan, caustic, giọt nước | Phù hợp làm mẫu nguồn |
| fire | `cutin-fire.v1-try2.png` | Đỏ cam, lõi nóng, lưỡi lửa và tàn than | Phù hợp làm mẫu nguồn; dùng try2 |
| earth | `cutin-earth.v1-try1.png` | Hổ phách, nâu khoáng, bụi và vảy mica | Phù hợp làm mẫu nguồn |
| ice | `cutin-ice.v1-try2.png` | Lam băng, pha lê nhỏ, sương lạnh | Phù hợp làm mẫu nguồn; dùng try2 |
| thunder | `cutin-thunder.v1-try1.png` | Sét xanh tím phân nhánh, plasma trắng | Phù hợp làm mẫu nguồn; thiếu thư mục ult cùng hệ |
| wind | `cutin-wind.v1-try1.png` | Ngọc nhạt, bạc, luồng khí mảnh | Phù hợp làm mẫu nguồn |
| light | `cutin-light.v1-try1.png` | Trắng ngà, vàng sáng, màn quang | Phù hợp làm mẫu nguồn |
| dark | `cutin-dark.v1-try1.png` | Tím mận, khói tối, viền amethyst | Phù hợp làm mẫu nguồn; thiếu thư mục ult cùng hệ |
| void | `cutin-void.v1-try1.png` | Tím lạnh, nếp khúc xạ và mảnh sáng | Phù hợp làm mẫu nguồn |
| blood | `cutin-blood.v1-try1.png` | Đỏ ruby, dải chất lỏng và sương đỏ | Phù hợp làm mẫu nguồn |
| poison | `cutin-poison.v1-try1.png` | Xanh độc–tím, giọt và hơi độc | Phù hợp làm mẫu nguồn |
| star | `cutin-star.v1-try1.png` | Bạc–vàng, bụi sao, bóng chàm | Phù hợp làm mẫu nguồn |

Các ảnh giữ năng lượng chảy ngang theo lớp, lõi sáng, sương/hạt và lấp lánh; vùng giữa-trái tối để đặt nhân vật và tên chiêu sau này. Đã xem từng đầu ra và ảnh ghép: không thấy người, sinh vật, chữ hay watermark.

**Điểm owner cần xem:** wood có phần sáng còn sát mép phải. Giá trị kênh lớn nhất ở cột ngoài cùng bên phải là 44/255; cột trái là 2/255. Vì vậy chưa kết luận wood đạt yêu cầu mờ hoàn toàn về đen để chuyển sang image-to-video. Đã dùng hết 16 lượt được giao; giữ nguyên tệp và ghi nợ rõ ràng. Các lựa chọn còn lại có giá trị kênh lớn nhất ở hai cột biên ngoài cùng không quá 5/255; phép kiểm này chỉ xác nhận cột biên, không thay cho kiểm vùng lề 8% của video tương lai.

Fire try1 sáng sát mép phải (33/255); ice try1 bị cắt cụm sáng (trái 41/255, phải 165/255). Hai lượt dự phòng dùng để cải thiện bố cục hai ảnh này: fire try2 còn 3/255, 1/255; ice try2 còn 1/255, 2/255 ở hai cột biên.

## Tham chiếu thực sự đã gửi

Mọi lần đều đính kèm atlas sở hữu trong repo:

`games/immortality-cultivation/art-src/lab/vfx/cutin/cutin-band-edge-light-loop-w2.atlas.png`

Atlas dùng cho bố cục luồng ngang và ánh sáng, không sao chép lưới atlas. Ảnh tuyệt kỹ dùng riêng cho màu và chất liệu; không lấy sẵn cảnh, vật thể hay bố cục tấm thành phần.

Các đường dẫn dưới đây tính từ `games/immortality-cultivation/art-src/concept/`:

| Hệ | Ảnh tuyệt kỹ đính kèm |
| --- | --- |
| metal | `ult-metal/ult-metal-components.v1-try2.png` |
| wood | `ult-wood/ult-wood-components.v1-try3.png` |
| water | `ult-water/ult-water-components.v1-try2.png` |
| fire, cả hai lượt | `ult-fire/ult-fire-components.v1-try2.png` |
| earth | `ult-earth/ult-earth-components.v1-try2.png` |
| ice, cả hai lượt | `ult-ice/ult-ice-moment-a.v1-try1.png` |
| wind | `ult-wind/ult-wind-components.v1-try2.png` |
| light | `ult-light/ult-light-components.v1-try2.png` |
| void | `ult-void/ult-void-components.v1-try2.png` |
| blood | `ult-blood/ult-blood-components.v1-try2.png` |
| poison | `ult-poison/ult-poison-components.v1-try2.png` |
| star | `ult-star/ult-star-components.v1-try2.png` |
| thunder, dark | Không có thư mục `ult-thunder/`, `ult-dark/` tại thời điểm kiểm tra; chỉ đính kèm atlas bắt buộc, theo điều kiện “nếu có” của phiếu |

Không dùng ảnh tham chiếu bên thứ ba.

## Kỹ thuật và phạm vi

Image_gen trả ảnh 2172×724, đúng tỷ lệ 3:1. ImageMagick 7 giảm kích thước đồng tỷ lệ xuống **1920×640** cho cả 16 PNG; không cắt khung, đổi màu, vẽ thêm hay ghép sửa hình. Ảnh gốc của công cụ được giữ nguyên tại nơi công cụ lưu mặc định. Đã kiểm tra đủ 16 PNG, đúng kích thước, mỗi PNG có prompt tương ứng, và đã xem ảnh ghép.

Môi trường python3 không có Pillow; việc kiểm tra được hoàn tất bằng ImageMagick có sẵn, không cài thêm phụ thuộc.

Chỉ ghi thư mục `art-src/concept/cutin-bands/` và báo cáo này. Ảnh ghép nằm đúng nơi phiếu yêu cầu. Không sửa code, src, scripts, tests hay docs của Tu Tiên; không chạy build hoặc bộ test của game; không làm video, không thêm nhân vật và không thực hiện thao tác Git thay đổi trạng thái. Không sửa ảnh có sẵn.

Không mở rộng nghiên cứu hay gọi thêm trợ lý vì đây là phiếu sản xuất ảnh với giải pháp và phản biện PASS đã được giao. Áp dụng imagegen, game-vfx-production, game-art-pipeline và game-video-vfx-usage; đây là lớp nền cut-in thuộc hạng SHOULD, chưa được tích hợp.

## Phần chưa làm

- Không tạo ảnh tuyệt kỹ tham chiếu riêng cho thunder/dark vì ngoài phạm vi phiếu và thư mục không có sẵn.
- Không tạo quá 16 lượt; wood được đánh dấu cần xem lại mép phải.
- Không làm video, ghép nữ chính, tích hợp hay nghiệm thu trong game theo ràng buộc.
- Owner cần xem ảnh ghép, xác nhận lựa chọn fire/ice try2, và quyết định xử lý mép phải wood trước bước image-to-video.

