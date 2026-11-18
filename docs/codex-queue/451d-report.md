# Phiếu 451d — Bảo kính Nhật Luân, tông Quang

Ngày: 18/11/2026. Phản biện đầu vào: PASS (Sonnet, theo phiếu). Đã dùng `image_gen` tích hợp **2/3 lượt**; đề xuất owner xem **v2-try2**.

## Ảnh và prompt đã tạo

Các đường dẫn dưới đây tính từ `/Volumes/SS990TPRO/htdocs/typing-game/`:

| Ảnh | Prompt nguyên văn | Ghi chú |
| --- | --- | --- |
| `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try1.png` | `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try1.prompt.txt` | Bản đầu chuyển tông và bổ sung ba góc; lề ngang chưa đạt, giữ lại để đối chiếu. |
| `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try2.png` | `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-relic-mirror-a.v2-try2.prompt.txt` | Bản đề xuất: thu nhỏ bố cục, gom lông vũ thành mảng dày hơn. |

Hai ảnh gốc tham chiếu đúng theo phiếu: `light-relic-mirror-a.v1-try1.png` cho dáng phượng, vành và ngọc đỉnh; `light-ray-a2.v1-try2.png` cho lõi trắng ấm và vàng champagne. Lượt hai nhận thêm v2-try1 để sửa có định hướng. Mọi đường dẫn tham chiếu đều ghi trong prompt; không dùng ảnh ngoài dự án hoặc game khác.

## Kết quả kiểm tra

- Cả hai PNG đúng **1536×1024**, giữ nguyên ảnh do công cụ sinh; không chỉnh màu, biến dạng hay vẽ bù.
- Ba góc: trước 3/4 nhẹ, nghiêng thấy thân và vành dày, sau thấy hoa văn lớn và một núm giữa. Phượng ôm vành và ngọc đỉnh được giữ; mặt kính đổi thành đá trắng ngà đặc, vân mềm, ngọc trắng ấm.
- V2-try2 có lông vũ và hoa văn thành mảng lớn hơn, tông vàng nhạt/champagne, không còn đá đỏ hoặc mặt kính cam dung nham. Quan sát không thấy chữ, watermark, tia, hào quang hoặc bóng đổ xuống nền.
- Đo vùng vật thể bằng ngưỡng sắc độ trên nền xám với ImageMagick: try1 có hộp bao `1430×685+52+131`, lề trái/phải khoảng **3,39% / 3,52%**; try2 có hộp bao `1272×613+130+173`, lề trái/trên/phải/dưới khoảng **8,46% / 16,89% / 8,72% / 23,24%**. Đây là phép đo xấp xỉ vùng có màu; đã xem toàn ảnh để kiểm tra các cạnh sáng.
- Tự đánh giá để owner chọn, không phải chấm mù hay nghiệm thu trong game: try1 — sức hút 8,3; bám phiếu 7,5 (lỗi lề); đọc hình thu nhỏ 8,2; độ sạch 8,4. Try2 — sức hút 8,4; bám phiếu 8,5; đọc hình thu nhỏ 8,3; độ sạch 8,5.

## Tờ so sánh

`/private/tmp/typing-game-451d/light-relic-mirror-451d.jpg` — **1600×680**, v1 bên trái, v2-try2 đủ ba góc bên phải; đã mở kiểm tra. Có `ABOUT.md` bên cạnh.

Dùng thư mục dự phòng được phiếu cho phép vì sandbox của phiên chỉ cho ghi trong repo và thư mục tạm, không bao gồm `/Volumes/SS990TPRO/htdocs/typing-game-review/`. Không ghi vào thư mục review hoặc sửa chỉ mục ngoài phạm vi cho phép.

## Owner cần xem

Xem v2-try2 và tờ so sánh để quyết định tông Quang, độ dày các cụm lông vũ và thiết kế mặt sau. Một số đầu mút lông vẫn nhọn nhưng gốc đã gom thành khối; khi dựng 3D cần kiểm tra độ liền và độ bền hình học. Tỷ lệ vành 12–15% là yêu cầu đã đưa vào prompt và được kiểm tra bằng mắt, chưa phải số đo của mô hình. Bảng ba góc là nguồn thiết kế, chưa chứng minh độ khớp hình học tuyệt đối giữa các mặt.

Không dùng lượt ba vì lượt hai đã sửa lỗi lề và các mảng mảnh thấy ở lượt đầu. Không chạy chấm mù mới, Tripo, video, build hoặc test suite vì ngoài phạm vi phiếu. Không sửa code, không xóa hay ghi đè ảnh có sẵn, không thao tác commit/push/reset/clean/stash hoặc đổi nhánh.
