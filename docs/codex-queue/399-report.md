# Phiếu 399 — Ảnh tham chiếu tuyệt kỹ Thủy, Hỏa, Thổ

Ngày 16/11/2026. Đã dùng **12/12 lượt `image_gen`**, tạo **12 PNG 1536×1024**, mỗi hệ bốn ảnh; giữ nguyên PNG công cụ và lưu prompt thật cạnh từng ảnh. Có **ba ảnh ghép 1584×1118** để owner/Claude chọn. Phiếu có phản biện PASS (Sonnet, 16/11). Đây là phương án tham chiếu, **chưa phải nghiệm thu hiệu ứng hoặc bộ texture sẵn dùng**; nền đen tuyệt đối và đường nối texture còn hạn chế bên dưới.

## File giao nộp

Mọi tên trong bảng là liên kết tới ảnh; prompt cùng tên, đổi `.png` thành `.prompt.txt`. Mỗi thư mục có đúng bốn PNG, bốn prompt sinh ảnh và một prompt ghi lệnh ghép.

| Hệ | Khoảnh khắc chiêu | Bảng đầu | Bảng sửa lề — đề xuất | Mặt đất riêng |
| --- | --- | --- | --- | --- |
| Thủy | [moment-a.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-water/ult-water-moment-a.v1-try1.png) | [components.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-water/ult-water-components.v1-try1.png) | [components.v1-try2](../../games/immortality-cultivation/art-src/concept/ult-water/ult-water-components.v1-try2.png) | [ground-tile.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-water/ult-water-ground-tile.v1-try1.png) |
| Hỏa | [moment-a.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-fire/ult-fire-moment-a.v1-try1.png) | [components.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-fire/ult-fire-components.v1-try1.png) | [components.v1-try2](../../games/immortality-cultivation/art-src/concept/ult-fire/ult-fire-components.v1-try2.png) | [ground-tile.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-fire/ult-fire-ground-tile.v1-try1.png) |
| Thổ | [moment-a.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-earth/ult-earth-moment-a.v1-try1.png) | [components.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-earth/ult-earth-components.v1-try1.png) | [components.v1-try2](../../games/immortality-cultivation/art-src/concept/ult-earth/ult-earth-components.v1-try2.png) | [ground-tile.v1-try1](../../games/immortality-cultivation/art-src/concept/ult-earth/ult-earth-ground-tile.v1-try1.png) |

Ảnh ghép đủ mọi bản, khoảng 0,46–0,54 MB mỗi ảnh:

- [ult-water-sheet-399.jpg](../../games/immortality-cultivation/art-src/concept/ult-water/ult-water-sheet-399.jpg)
- [ult-fire-sheet-399.jpg](../../games/immortality-cultivation/art-src/concept/ult-fire/ult-fire-sheet-399.jpg)
- [ult-earth-sheet-399.jpg](../../games/immortality-cultivation/art-src/concept/ult-earth/ult-earth-sheet-399.jpg)

Thứ tự trên mỗi ảnh ghép: trên trái là khoảnh khắc, trên phải là bảng lần 2, dưới trái là bảng lần 1, dưới phải là mặt đất riêng. Chỉ ảnh ghép có nhãn tên file; PNG nguồn không có chữ. Các `.prompt.txt` của ảnh ghép ghi lệnh ImageMagick thực tế, không giả làm prompt sinh ảnh.

## Tham chiếu và quá trình

Đã xem trực tiếp và truyền đủ ba ảnh vào **mọi lượt**. Không thiếu tham chiếu nào; không dùng ảnh bên thứ ba:

1. `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`: bố cục, camera và mật độ đã duyệt; thay hoàn toàn vật liệu băng.
2. `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-water-profound-sea-v2.jpg`, `ult__ult-fire-one-spark.jpg`, `ult__ult-earth-ink-peaks.jpg`: ảnh tương ứng từng hệ, chỉ chất liệu và ánh sáng; loại mắt/sinh vật, kiến trúc và phong cảnh.
3. Dưới `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/vfx/`: `water/water-wave.atlas.png`, `fire/fire-wave.atlas.png`, `earth/earth-pillar.atlas.png`, dùng chất liệu đúng hệ, không chép bố cục atlas.

Prompt thật viết bằng tiếng Anh và ghi đường dẫn tuyệt đối, vai trò từng ảnh. Lượt sửa bảng nhận thêm PNG bảng lần 1 làm ảnh đích. Hai mẫu Thủy/Hỏa đầu được xem và hiển thị cho owner trước các lượt tiếp theo; mọi ảnh sinh tiếp cũng đã hiển thị khi công cụ trả về.

Thứ tự lượt: 1–3 khoảnh khắc Thủy/Hỏa/Thổ; 4–6 bảng thành phần lần 1; 7–9 sửa lề bảng; 10–12 mặt đất riêng để cải thiện cạnh lặp. Đã dừng ở trần 12, không gọi thêm. Hạn mức đọc trước khi làm: dùng 37%, còn 63%; không gặp lỗi giới hạn công cụ.

## Gợi ý chọn, không phải điểm duyệt

**Dùng ba `moment-a` làm phương án tổng thể và ba `components.v1-try2` làm phương án bảng để owner xem.** Bảng lần 1 giữ lại cho đối chiếu chi tiết lớn, không đạt lề ngang.

- **Thủy:** thân nước trong xanh, vòng sóng dâng, xoáy tâm gọn, đọc được đá lát qua nước; giọt và bọt sáng tách rõ. Vành ngoài khá sáng, owner nên xem liệu tâm đã nổi bật đủ ở camera chơi hay chưa.
- **Hỏa:** tia sáng tâm nhỏ, biển lửa lan rộng, các lưỡi cuộn cao thấp, có than sáng và khói mỏng. Hình mới giữ nền đá thay cho mái nhà, cảnh và vòm của clip cũ. Một số đường lửa trên sàn còn mảnh như gân sáng; cần owner chọn mức độ lửa thân dày mong muốn.
- **Thổ:** cụm đá đen nhiều tầng nhô trên sân lát, khe vàng đất, bụi và mảnh đá. Phần nứt ở đỉnh và chân cụm trung tâm đều sáng; phân cấp chưa hoàn toàn gọn thành một điểm, có thể đọc hơi giống dung nham. Owner cần xem sắc vàng đất và mức phát sáng trước khi chọn.

Mỗi bảng có tám ô: bốn biến thể hình chính góc ngang; mảnh/giọt; hạt/bọt/khói/bụi; mặt đất từ trên; vòng trói từ trên với tâm rỗng. Vòng là mẫu decal phẳng, không có vật thể hoặc cơ thể để bọc. Riêng sóng Thủy thứ tư thấy một phần mặt trên, chưa phải góc ngang tuyệt đối. Mặt đất riêng tốt hơn ô nhỏ trong bảng về cạnh nối; không lấy ô nhỏ làm texture cuối.

## Kiểm tra và giới hạn kỹ thuật

Đã kiểm đủ 12 PNG đúng 1536×1024 và 12 prompt tương ứng, mở xem ba ảnh ghép sau khi ghép. Không thấy chữ, watermark, sinh vật hoặc kiến trúc trong PNG. Không cắt, đổi màu, vẽ lại hoặc chuẩn hóa PNG nguồn. ImageMagick chỉ đọc số liệu và ghép bản xem có thu nhỏ.

Lề bảng đo theo hộp bao pixel có ít nhất một kênh RGB >8/255; đây là lề ngoài toàn bảng, không xác nhận lề riêng từng ô:

| Bảng | Trái / trên / phải / dưới | Kết quả lề ngoài |
| --- | --- | --- |
| Thủy lần 1 | 2,73 / 15,62 / 2,67 / 15,33% | Không đạt. |
| Thủy lần 2 | 14,06 / 23,44 / 13,87 / 26,17% | Đạt ngưỡng 8% theo phép đo. |
| Hỏa lần 1 | 2,93 / 11,23 / 2,86 / 15,23% | Không đạt. |
| Hỏa lần 2 | 14,52 / 19,53 / 13,93 / 24,32% | Đạt ngưỡng 8% theo phép đo. |
| Thổ lần 1 | 3,26 / 10,84 / 2,34 / 13,48% | Không đạt. |
| Thổ lần 2 | 12,43 / 18,95 / 11,46 / 22,95% | Đạt ngưỡng 8% theo phép đo. |

**Nền đen tuyệt đối chưa đạt hoàn toàn:** dải 8% quanh ba bảng lần 2 có giá trị kênh tối đa 1/255, dù nhìn như đen. Không tự sửa ngưỡng hoặc ghi đè ảnh để che sai khác này.

**Texture lặp chưa kín tuyệt đối.** Ô nhỏ trong bảng lần 2 có sai khác cạnh RGB trung bình khoảng 35–67/255 và kích thước hơi lệch vuông. Ba ảnh mặt đất riêng dùng chi tiết mờ dần về viền tối đồng màu để giảm lỗi nối. Hộp bao đo ở ngưỡng >8/255 cho các hình vuông sau:

| Mặt đất riêng | Tọa độ góc trái trên; kích thước | Sai khác RGB trung bình trái–phải / trên–dưới | Sai khác kênh lớn nhất |
| --- | --- | --- | --- |
| Thủy | (416,160); 704×704 | 0,955 / 0,829 trên 255 | 4/255 |
| Hỏa | (384,128); 768×768 | 0,738 / 0,589 trên 255 | 4/255 |
| Thổ | (448,192); 640×640 | 0,898 / 1,195 trên 255 | 4/255 |

Chỉ Thổ đúng kích thước ô 640×640 đã yêu cầu trong prompt bổ sung; cả ba canvas vẫn đúng 1536×1024. Các cạnh gần khớp hơn nhưng chưa bằng nhau; viền tối cũng có thể thành lưới khi lặp. Chưa kiểm texture lặp trong game, không tuyên bố seamless sẵn dùng. Yêu cầu góc camera 50° và sân 30 m được đưa vào prompt; hình tham chiếu không chứng minh được số đo thực trong runtime.

## Phạm vi và việc cần owner xem

Chỉ tạo file trong ba thư mục `art-src/concept/ult-water`, `ult-fire`, `ult-earth` và báo cáo này. Không sửa code, script, test, docs Tu Tiên, ảnh có sẵn hoặc nguồn audit. Không tạo video/âm thanh, chạy build/bộ test, đổi nhánh, stage, commit, push hoặc thao tác Git phá hủy. Không ghi vào thư mục review hay cập nhật chỉ mục vì ngoài phạm vi ghi của phiếu.

Owner/Claude chọn từ ba ảnh ghép: hướng nước, độ dày biển lửa, sắc vàng và điểm nhấn của Thổ; ưu tiên bảng lần 2 về bố cục. Chưa dựng tiếp từ ảnh nào. Cần xử lý nền đen tuyệt đối, góc ngang sóng thứ tư và cạnh texture trước khi coi đây là bộ thành phần hoàn chỉnh. Không chạy chấm mù hoặc công nhận đạt 8.5 trong lượt chỉ làm ảnh tham chiếu này; quyền chọn và duyệt vẫn ở owner/Claude.
