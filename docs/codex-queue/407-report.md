# Phiếu 407 — Ảnh tham chiếu Thiên Thạch Hỏa và Thẩm Phán Quang

Ngày làm: 16/11/2026. Đã dùng **8/8 lượt `image_gen` tích hợp**, mỗi chiêu 4 ảnh. Không gặp giới hạn dịch vụ. Đây là phương án tham chiếu để owner/Claude chọn, chưa phải nguồn đã nghiệm thu hoặc hiệu ứng đã dựng.

## File giao

Thư mục gốc: `games/immortality-cultivation/art-src/concept/`.

| Chiêu | Thư mục | Ảnh ghép A/B |
| --- | --- | --- |
| Thiên Thạch Hỏa | `pillar-meteor/` | `pillar-meteor/pillar-meteor-sheet-407.jpg` |
| Thẩm Phán Quang | `pillar-judgement/` | `pillar-judgement/pillar-judgement-sheet-407.jpg` |

Trong **mỗi** thư mục có đủ bốn PNG và bốn prompt thật, nguyên văn đã gửi công cụ:

- `pillar-moment-a.v1-try1.png` và `pillar-moment-a.v1-try1.prompt.txt`;
- `pillar-components-a.v1-try2.png` và `pillar-components-a.v1-try2.prompt.txt`;
- `pillar-moment-b.v1-try3.png` và `pillar-moment-b.v1-try3.prompt.txt`;
- `pillar-components-b.v1-try4.png` và `pillar-components-b.v1-try4.prompt.txt`.

Ảnh ghép: hàng trên là A, hàng dưới là B; cột trái là khoảnh khắc, cột phải là bảng thành phần. PNG nguồn không có chữ; nhãn chỉ nằm ngoài ảnh trong JPG ghép.

## Tham chiếu đã nạp vào mọi lượt

Không thiếu ảnh tham chiếu. Mỗi lượt nạp đúng ba file; đường dẫn đầy đủ và vai trò từng ảnh đều có trong prompt.

1. Bố cục/camera/nền sân/mức chi tiết: `games/immortality-cultivation/art-src/concept/ult-ice/ult-ice-moment-a.v1-try1.png`.
2. Chất liệu và ánh sáng, không lấy bố cục cảnh cũ:
   - Hỏa: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__pillar-fire-meteor.jpg`;
   - Quang: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/clip-content-audit/ult__pillar-light-judgement.jpg`.
3. Atlas hình chính cùng hệ:
   - `games/immortality-cultivation/art-src/lab/vfx/fire/fire-comet.atlas.png`;
   - `games/immortality-cultivation/art-src/lab/vfx/light/light-column-strike.atlas.png` (prompt chuyển cyan sang vàng champagne/trắng ấm).

Chỉ dùng ảnh của dự án, không gửi ảnh bên thứ ba. Công cụ tự lưu bản gốc trong thư mục generated_images; đã sao chép toàn bộ kết quả về đường dẫn SSD của phiếu, giữ nguyên PNG.

## Gợi ý để owner/Claude chọn

**Thiên Thạch Hỏa:** ưu tiên xem **khoảnh khắc B / try3** cùng **bảng B / try4**. B giữ trọn đuôi lửa, có khoảng sân quanh vùng va chạm và một điểm sáng chính; đá đen rạn nóng chảy đọc rõ. A mạnh và lớn hơn nhưng đuôi bị cắt ở góc trên trái. Phần hố trong cả hai bản còn nông, đọc giống nền đá nứt cháy hơn một lòng hố sâu; cần owner chọn mức độ lõm trước bước dựng. Bảng B có bốn dáng khác nhau: khối dẹt, mảnh nhọn, cụm đá tròn và mảnh dài.

**Thẩm Phán Quang:** ưu tiên xem **khoảnh khắc B / try3** cùng **bảng B / try4**. B thấy được đầu cột tan thành bụi, vòng ấn nằm trên nền lát và khoảng sân xung quanh. A dày, rực và nhiều chi tiết hơn nhưng cột bị cắt ở mép trên. Bảng B có cột mảnh, rèm sáng xòe, cột thuôn và cột rộng; các đầu cột vẫn cần kiểm lề khi tách nguồn.

Cả hai bảng đều có bốn biến thể hình chính nhìn ngang ở hàng trên; hàng dưới lần lượt là mảnh/tia nhỏ, hạt/glint, vết đất nhìn trên và vòng ấn decal nhìn trên có tâm rỗng. Không thấy người, sinh vật, watermark hoặc cảnh nền ngoài sân đá trong các PNG.

Ảnh khoảnh khắc là **tham chiếu bố cục**, không dùng nguyên ảnh làm hiệu ứng. Bảng thành phần là **bản thiết kế nguyên liệu**, chưa phải atlas hay nguồn đã tách. Dựng tiếp theo công thức thành phần: hình chính + đuôi/rèm sáng + va chạm + sóng/vòng + vết đất + hạt; tái dùng thư viện trước khi tạo thêm nguồn. Phiếu này không dựng lab hoặc tạo video.

## Kiểm tra và điểm chưa đạt

Đã kiểm đủ **8 PNG đúng 1536×1024**, đủ tám prompt cạnh ảnh, đủ ba đường dẫn tham chiếu trong từng prompt. Đã xem tám kết quả công cụ và mở kiểm cả hai ảnh ghép. ImageMagick chỉ đọc kích thước/pixel và ghép JPG; không tô lại, cắt, chỉnh nền hoặc sửa PNG nguồn.

**Lề bảng thành phần chưa đạt đồng đều 8%.** Đo theo lưới 4×2 ô bằng nhau, mỗi ô 384×512; hộp bao lấy pixel có kênh RGB lớn hơn 8/255 để bỏ nhiễu rất tối. Lề nhỏ nhất của từng ô B / try4, theo thứ tự trái sang phải, trên xuống dưới:

| Chiêu | Ô 1 | Ô 2 | Ô 3 | Ô 4 | Ô 5 | Ô 6 | Ô 7 | Ô 8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hỏa | 1,04% | 3,12% | 8,85% | 4,95% | 10,94% | 18,49% | 7,81% | 0,00% |
| Quang | 5,86% | 5,66% | 5,66% | 5,66% | 11,72% | 21,68% | 14,06% | 5,21% |

Công cụ bố trí lệch tâm so với lưới yêu cầu; các con số trên kiểm khả năng cắt theo lưới cố định, không khẳng định hình bị cắt ở mép ngoài PNG. A còn sát hoặc vượt ranh ô hơn B. Không đánh dấu PASS cho yêu cầu lề.

**Nền đen tuyệt đối chưa đạt.** Trong 16 hàng pixel trên cùng của bảng B, Hỏa có 12,415% pixel khác đen và Quang có 11,845%; mức kênh lớn nhất đều là 1/255. Nền nhìn đen nhưng còn nhiễu gần đen. Giữ nguyên ảnh và ghi nhận lỗi, không gọi là RGB(0,0,0) tuyệt đối.

**Vết đất mới là các cụm decal rời để bố trí lặp**, không phải chất liệu liên tục đã kiểm seamless. Đo ô 7 của bảng B (`x=768..1151, y=512..1023`), sai khác RGB trung bình giữa mép đối diện, đơn vị /255:

| Chiêu | Trái–phải | Trên–dưới | Sai khác lớn nhất |
| --- | --- | --- | --- |
| Hỏa | 0,2624 | 0,0877 | 8/255 |
| Quang | 0,1296 | 0,1137 | 1/255 |

Chưa đạt trùng mép tuyệt đối; Hỏa còn tín hiệu ở biên ô. Chưa xuất tile riêng hoặc thử nhịp lặp trong engine. Camera 50° và đường kính 6 m là chỉ dẫn đã gửi công cụ; không xác nhận bằng đo hình học từ tranh.

## Phạm vi và phần bỏ qua

Chỉ ghi hai thư mục concept được phép và báo cáo này. Không ghi đè hoặc xóa ảnh có sẵn, không sửa code/atlas/tham chiếu/tài liệu Tu Tiên, không tạo âm thanh/video, không chạy build hoặc test game, không đổi nhánh và không commit/push/reset/clean/stash. Không tạo capture hoặc sửa thư mục review ngoài phạm vi phiếu.

Không tạo thêm sau 8 lượt theo trần phiếu. Chưa tách thành phần, chưa chuẩn hóa nền, chưa dựng lab hoặc chấm trong play host vì nằm ngoài nhiệm vụ ảnh tham chiếu. Owner/Claude cần chọn A/B và xem các lỗi lề, nền đen, vết đất trước khi dùng làm nguồn dựng; gợi ý B không phải nghiệm thu hiệu ứng.
