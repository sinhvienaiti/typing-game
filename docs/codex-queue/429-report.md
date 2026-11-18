# Phiếu 429 — Hai mẫu nguồn sạch cho Tripo

Ngày: 16/11/2026. Trạng thái: đã tạo đúng **2 mẫu**, dừng để Claude gửi owner duyệt. Đã dùng 2/8 lần tối đa; chưa có chỉ định làm tiếp.

## Tệp bàn giao

Các đường dẫn dưới đây tính từ `/Volumes/SS990TPRO/htdocs/typing-game`:

| Nội dung | Đường dẫn |
| --- | --- |
| Kim, mẫu 1 | `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/ult-metal-clean.v1-try1.png` |
| Prompt Kim nguyên văn | `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/ult-metal-clean.v1-try1.prompt.txt` |
| Hư Không, mẫu 1 | `games/immortality-cultivation/art-src/concept/ult-void/tripo-src/ult-void-clean.v1-try1.png` |
| Prompt Hư Không nguyên văn | `games/immortality-cultivation/art-src/concept/ult-void/tripo-src/ult-void-clean.v1-try1.prompt.txt` |
| Bảng ghép hai mẫu | `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/tripo-src-samples-429.jpg` |
| Nguồn và lệnh ghép bảng | `games/immortality-cultivation/art-src/concept/ult-metal/tripo-src/tripo-src-samples-429.prompt.txt` |

## Cách tạo

- Gọi công cụ tích hợp `image_gen` đúng hai lần, mỗi lần tạo một vật thể; không dùng CLI/API thay thế.
- Cả hai lần đều nạp ảnh tham chiếu của repo bằng `referenced_image_paths`, không chỉ ghi tên trong prompt. Kim dùng `ult-metal-blade-src.v1.png` và `ult-metal-components.v1-try2.png`; Hư Không dùng ảnh nguồn kiếm để tham chiếu bố cục cụm và `ult-void-components.v1-try2.png` để tham chiếu kính tím. Đường dẫn tuyệt đối có trong từng prompt.
- Kim giữ ba kiếm dựng đứng, thanh giữa cao nhất, mũi hướng lên theo ảnh nguồn cũ, phần dưới gắn vào đế chung; lưỡi bạc, chuôi và chắn kiếm vàng. Hư Không là bốn mảnh kính tím gắn vào đế vụn chung.
- Prompt yêu cầu chỉ có vật thể, bỏ toàn bộ vệt sáng, hạt, quầng, bloom, dây và sợi mảnh. Ánh sáng/VFX trong game không được vẽ vào nguồn.
- Công cụ trả ảnh 1254×1254 dù prompt yêu cầu 1024×1024. Xuất bằng ImageMagick: thu toàn khung về 768×768 rồi đặt giữa canvas 1024×1024; nối nền xám bằng `virtual-pixel edge`. Không cắt hay vẽ lại vật thể. Toàn bộ khung ảnh gốc nằm cách mép mới 128 px, bảo đảm lề tối thiểu 12,5%. Nền nối có thể mang sắc độ nhẹ từ mép ảnh gốc.
- Hai PNG bàn giao đều 1024×1024; bảng ghép JPEG 1072×568. Prompt được giữ nguyên văn, thao tác xuất ảnh được ghi riêng trong tệp của bảng ghép. Bản gốc do công cụ lưu trong `/Users/toandx/.codex/generated_images/01a1e509-8209-71a2-a1c9-a84496a4f659/` vẫn được giữ nguyên.

## Phần chờ và giới hạn

- Owner cần xem bảng ghép, xác nhận dáng ba kiếm, góc nhìn hơi từ trên, vật liệu bạc/vàng và độ trong của kính tím trước khi làm tiếp. Đây là mẫu chờ duyệt, chưa có kết luận đạt chuẩn 8,5 hay phù hợp sau dựng Tripo.
- Không tạo thêm biến thể, không chạy Tripo, không tạo video/âm thanh, không sửa code, không chạy build/test, không thay đổi Git. Không xóa hay ghi đè ảnh có sẵn.
- Quota đọc đầu lượt còn 14%; chỉ thực hiện phiếu tạo ảnh và tệp bàn giao kèm theo, không giao thêm việc chấm điểm hoặc đo đạc.
- Bảng ghép được để cạnh ảnh nguồn trong phạm vi đầu ra của phiếu. Thư mục `typing-game-review` nằm ngoài vùng được phép ghi của phiên này; Claude cần chuyển bảng sang `owner-review/2026-11-16/tu-tien/ult-3d-models/`, tạo/cập nhật `ABOUT.md` theo quy định và dựng lại chỉ mục khi gửi owner. Phiên này không ghi ra ngoài phạm vi hoặc chạy chỉ mục có tác dụng ghi ngoài phạm vi.
