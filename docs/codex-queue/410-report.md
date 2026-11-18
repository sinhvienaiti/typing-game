# Phiếu 410 — Ảnh tham chiếu Côn Bằng Tinh Hà

Ngày: 16/11/2026. Công cụ: `image_gen` tích hợp, **5/6 lượt**. Đã tạo hai khoảnh khắc và ba bản bảng thành phần; còn một điểm kỹ thuật chưa đạt: nền bảng chưa đen tuyệt đối ở mức pixel.

## Tệp giao

Thư mục ảnh: `games/immortality-cultivation/art-src/concept/astral-kunpeng/`.

| Tệp | Nội dung |
| --- | --- |
| `kunpeng-moment-a.v1-try1.png` | Côn Bằng thiên về dáng cá voi, lướt chéo trên sân đá, cánh-vây và đuôi bụi sao. |
| `kunpeng-moment-b.v1-try1.png` | Cánh mở rộng hơn, điểm sáng chính ở vai/ngực, thêm vệt sóng thấp trên nền. |
| `kunpeng-components.v1-try1.png` | Bảng sáu phần đầu tiên; lề hẹp, gốc cánh có nét giống mỏ. Giữ lại để đối chiếu. |
| `kunpeng-components.v1-try2.png` | Tăng lề, sửa gốc cánh thành đầu nối tù; các phần tách riêng. |
| `kunpeng-components.v1-try3.png` | Bản sửa nền bằng image_gen, giữ sáu phần; ánh sáng rõ hơn, nền vẫn có nhiễu 1/255. |
| `kunpeng-sheet-410.jpg` | Ảnh ghép 1536×1536: A trên trái, B trên phải, bảng try3 phía dưới; không thêm chữ. |

Cả năm PNG đều **1536×1024**. Mỗi PNG có prompt thật trong tệp `.prompt.txt` cùng tên. `kunpeng-sheet-410.prompt.txt` ghi lệnh ghép ImageMagick thực tế; ảnh ghép không dùng thêm lượt tạo ảnh.

## Tham chiếu

Không thiếu ảnh. Mọi lượt đều nhận đủ ba ảnh bắt buộc và ghi đường dẫn trong prompt:

- `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`: góc camera và nền sân đá.
- `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/expansion__astral-kunpeng-leviathan.jpg`: hình dáng và ánh sáng; bỏ bệ/cảnh có sẵn.
- `games/immortality-cultivation/art-src/lab/vfx/star/star-ribbon-loop.atlas.png`: chất liệu dải sao, sợi sáng và hạt bụi.

Các lượt sau còn dùng ảnh vừa tạo để giữ cùng thiết kế. Không dùng ảnh bên thứ ba.

## Gợi ý owner/Claude xem

Ưu tiên **moment-b try1** cho phân cấp ánh sáng và **components try3** cho bảng tách phần. Đây là gợi ý chọn ảnh tham chiếu, chưa phải nghiệm thu hiệu ứng trong game.

Bảng gồm thân nhìn ngang, thân nhìn trên, cánh-vây, đuôi bụi sao, bụi sao và decal sóng xung kích. Hai khoảnh khắc giữ cùng một Côn Bằng năng lượng xanh lam trên nền đá, không có bệ hay sinh vật phụ. Chênh lệch tư thế giữa A/B còn nhẹ; chuyển hoá được thể hiện chủ yếu qua độ mở cánh và ánh sáng. Owner cần xem độ trong suốt và cảm giác “cá voi hoá chim bằng” có đúng ý hay chưa.

## Kiểm tra và điểm còn thiếu

Đã mở xem ảnh nguồn và ảnh ghép, kiểm tra kích thước cùng các tệp prompt. Ở bảng try3, vùng có giá trị kênh lớn nhất >4/255 nằm trong hộp pixel `[194,136]–[1350,862]`, tương ứng lề trái/trên/phải/dưới khoảng **12,63% / 13,28% / 12,04% / 15,72%**.

**Chưa đạt riêng yêu cầu nền đen tuyệt đối:** trong dải lề 8%, có 383.067 pixel đen hoàn toàn và 80.397 pixel có kênh lớn nhất bằng 1/255. image_gen vẫn để lại nhiễu này sau lượt sửa nền. Không tuyên bố nền đạt RGB 0 tuyệt đối; cần chuẩn hoá nền trước khi dùng làm nguồn compositing. Giữ nguyên PNG công cụ trả về, không tự sửa màu/nền bằng công cụ khác.

Không dùng lượt thứ sáu vì lượt sửa nền vừa rồi không giải quyết được lỗi số học; chưa có cơ sở để lặp lại cùng cách. Không chạy giám khảo hay chấm 8,5: phiếu này giao ảnh cho owner/Claude chọn, không triển khai hiệu ứng trong play host.

## Phạm vi

Chỉ tạo tệp trong thư mục ảnh nêu trên và báo cáo này. Không sửa code, không tạo video/âm thanh, không chạy build/test game, không đổi nhánh, không commit/push; không xoá hoặc ghi đè ảnh nào.

