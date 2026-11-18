# Phiếu 450 — Sóng năng lượng vàng và đất nứt núi lửa

Ngày thực hiện: 18/11/2026. Phiếu có phản biện PASS (Sonnet, vòng 2). Đã gọi công cụ tích hợp `image_gen` đúng **4 lần**, mỗi biến thể một lần; cả bốn đều trả ảnh thành công. Đã lưu đủ ảnh, prompt nguyên văn và tờ ghép. **Chờ owner chọn; chưa tích hợp hoặc nghiệm thu trong game.**

## Tệp đã tạo

Thư mục: `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/`.

| Mẫu | Ảnh PNG 1024×1024 | Prompt nguyên văn |
| --- | --- | --- |
| Sóng A — tỏa mọi hướng | `metal-impact-wave.v1-try1.png` | `metal-impact-wave.v1-try1.prompt.txt` |
| Sóng B — mạnh phía trước và hai bên | `metal-impact-wave.v1-try2.png` | `metal-impact-wave.v1-try2.prompt.txt` |
| Nứt A — 7 nhánh chính | `metal-impact-crack.v1-try1.png` | `metal-impact-crack.v1-try1.prompt.txt` |
| Nứt B — dày, nhiều nhánh | `metal-impact-crack.v1-try2.png` | `metal-impact-crack.v1-try2.prompt.txt` |

Tờ chọn mẫu 2×2 có nhãn: [giant-impact-450.jpg](/private/tmp/typing-game-450/giant-impact-450.jpg), 1328×1404. Có `ABOUT.md` cùng thư mục. Dùng đường dẫn dự phòng được phiếu cho phép vì thư mục review trên SSD nằm ngoài vùng sandbox được ghi; không cập nhật chỉ mục review ngoài sandbox.

## Tham chiếu và xử lý

Đã mở xem hai ảnh tham chiếu trước khi tạo. Cả bốn lần gọi đều đính kèm đúng hai ảnh của dự án và ghi đường dẫn, vai trò trong prompt:

- `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg`: chỉ lấy ngôn ngữ tạo hình cú chạm đất ở nửa trái, ô dưới trái; không lấy kiếm hoặc cảnh.
- `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/giant-sword-aura.v1-try3.png`: màu vàng ấm và chất ánh sáng của hào quang C owner đã chọn; không lấy dáng đứng của hào quang.

Chọn `image_gen` theo phiếu: mỗi lần chỉ tạo một thành phần nguồn. Công thức tổng hợp dự kiến gồm sóng vàng + vết nứt + bụi Explosion01 đã có; phiếu này chỉ bổ sung hai thành phần còn thiếu, không tạo toàn cảnh hoặc bụi mới. Không dùng ảnh bên thứ ba hay ảnh của game khác.

Công cụ trả ảnh gốc 1254×1254 dù prompt yêu cầu 1024×1024. Đã dùng ImageMagick thu đồng đều toàn bộ ảnh xuống 848×848, đặt giữa nền đen 1024×1024, rồi đưa các giá trị kênh tối ≤ 0,4% về 0 để giảm nhiễu nền. Không cắt nội dung, không bóp phối cảnh, không vẽ thêm hình. Việc thu và thêm nền bảo đảm lề đen; các khoảng đen rộng giữa luồng sáng/vết nứt được giữ, quầng sáng cục bộ vẫn còn.

Ảnh gốc được giữ nguyên tại `/Users/toandx/.codex/generated_images/01a1ed2b-1497-7c60-8a31-7a78eedc7803/`:

- Sóng A: `exec-1d1660d5-73e2-49bd-bd07-d09de8c598c8.png`.
- Sóng B: `exec-c8785046-7851-48e0-9e95-079ffe8c9f44.png`.
- Nứt A: `exec-8f213580-e4f1-475b-91cd-08500951c910.png`.
- Nứt B: `exec-97349c17-402b-4ba6-9f3f-2d3c5be72319.png`.

## Kiểm tra và điểm owner cần xem

Đã xem bốn kết quả sinh và tờ ghép cuối. Cả bốn PNG đều 1024×1024, nền đen đục; dải lề 82 px ở cả bốn cạnh có giá trị RGB tối đa bằng 0. Khoảng cách nhỏ nhất từ pixel khác đen đến cạnh là 88 px, tương đương 8,59%, vượt yêu cầu 8%. Ảnh nguồn không có kiếm, quái, nhân vật, chữ, vòng tròn đều hay mandala. Các thành phần nằm trên mặt phẳng nhìn từ trên xuống, không có đường chân trời hoặc phối cảnh cảnh nền.

| Mẫu | Nhận xét hình nguồn | Pixel gần trắng / pixel nhìn thấy |
| --- | --- | --- |
| Sóng A | Các luồng vàng xé tơi tỏa nhiều hướng, tâm trắng ấm nhỏ, có tia mảnh và hạt sáng | 1,67% |
| Sóng B | Luồng dài ưu tiên phía trên và hai bên; đuôi phía dưới ngắn hơn | 1,44% |
| Nứt A | 7 nhánh chính dài, lòng vàng cam, mép đá tối, ít nhánh phụ | 0,57% |
| Nứt B | Nhánh chính dày, nhiều nhánh phụ, còn các khoảng nền đen rộng | 1,43% |

Phép đo gần trắng dùng cả ba kênh ≥ 200, chia cho số pixel có kênh lớn nhất > 10; đây là chỉ báo kiểm tra phần trắng dưới 30%, không phải đánh giá cảm nhận độ chói trong game.

Owner cần chọn riêng **Sóng A/B** và **Nứt A/B**. Với nứt, nên xem chất lòng phát sáng có đọc đúng dung nham nóng và mép đá nhô nhẹ như mong muốn; mẫu B rực và dày hơn rõ. Các ảnh là mẫu nguồn để chọn, không chấm điểm 8,5 cho lớp đơn lẻ; chưa kiểm chứng hiệu ứng ghép với bụi và kiếm ở camera chơi. Chỉ sau lựa chọn của owner mới giao bước Firefly hoặc tích hợp lab.

## Không thực hiện

Không bỏ sót đầu ra trong phiếu. Không tạo thêm ngoài bốn lần được chỉ định. Không sửa code, không làm video hoặc âm thanh, không chạy build hay bộ test game. Không sửa src/scripts/tests hoặc tài liệu Tu Tiên, manifest và tài liệu ngoài phạm vi. Không ghi đè hoặc xóa ảnh có sẵn, không đổi nhánh; không commit, push, reset, clean hoặc stash.
