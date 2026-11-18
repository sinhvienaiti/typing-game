# Phiếu 384 — mẫu 1 map một đường, camera B 42°

Ngày: 15/11/2026. Trạng thái: **đã làm mẫu nắng sớm; dừng chờ anh xem; chưa đạt bố cục, chưa chấp nhận**.

## Đã làm

Trong `games/immortality-cultivation/art-src/concept/`:
- `map1-lane.v1-try1.png` và `map1-lane.v1-try1.prompt.txt`: bản nắng sớm đầu; bỏ qua khi chọn mẫu vì sinh tám ổ cơ quan và Trận Trụ quá xa.
- `map1-lane.v1-try2.png` và `map1-lane.v1-try2.prompt.txt`: lượt sửa bố cục của mẫu 1; còn đúng sáu ổ, không người/quái/chữ/UI, một đường.
- `map1-lane-384-sheet.jpg`: **greybox | try2 | chồng 50 %**, 2880 × 582 px, mỗi ô 960 × 540 px cộng nhãn. Chồng hai ảnh trên cùng hệ quy chiếu 1920 × 1080 trước khi thu nhỏ.

Hai PNG giữ nguyên đầu ra công cụ **1672 × 941 px**, không nắn hình hoặc sửa tranh bằng mã. Chỉ tấm so sánh quy đổi về khung chuẩn. Công cụ không trả kích thước 1920 × 1080 như prompt yêu cầu; đây là một điểm chưa đạt.

Đã đọc MAP1_WIDE §13, MAP1_CONCEPT §3–6, skill game-map-concept và game-art-pipeline; đã xem đủ sáu ảnh tham chiếu bắt buộc. Chỉ dùng ảnh của repo, qua image_gen tích hợp. Tất cả đường dẫn ảnh nằm trong prompt đi kèm.

Công cụ chỉ nhận tối đa năm đường dẫn: lần gọi đầu bị từ chối trước khi sinh vì đưa sáu ảnh. Sau đó đóng bốn ô đất vào một tấm 2 × 2 tại chính đường dẫn sheet được phép, dùng cùng greybox và try6. Khi hoàn tất, thay tấm vật liệu tự tạo bằng sheet so sánh được yêu cầu; không sửa ảnh tham chiếu có sẵn. Có thể dựng lại đầu vào vật liệu từ bốn ảnh gốc được ghi trong prompt.

**Số lượt:** hai lần sinh thành công, một lần bị từ chối tham số trước khi sinh; chín lần view_image. Không gặp giới hạn chờ/429.

## Tự chấm try2 — không thay cho hai giám khảo mù

| Tiêu chí | Tự chấm /10 | Nhận xét |
|---|---:|---|
| Camera khớp | 5,5 | Có góc nhìn xuống và không thấy trời; bố cục vẫn trôi quá 20 px, vòng quá rộng. Không thể xác nhận camera 42° chỉ từ tranh. |
| Đọc đường | 8,4 | Một đường đá sáng rõ, có phiến lát và mép rêu; sáng hơn sân ở ba mẫu đo. |
| Hùng vĩ/hấp dẫn | 8,1 | Vực, biển mây, tùng và ánh xiên có chiều sâu; sân vẫn khá đều, họa tiết mây hơi lặp. |
| Tiên hiệp Việt | 8,0 | Đá xanh xám, ngói chàm, gỗ sẫm, ngọc ngà; nét riêng Việt chưa đủ mạnh để chốt. |
| Không che đường | 9,0 | Không vật cản trên đường; bóng dài có phủ một phần lối vào vòng. |
| Yếu nhất | — | Giữ tọa độ: H4, cụm tùng–đá và bề rộng vòng. Dải y ≥ 930 vẫn có vòng/hoa văn khá rõ, chưa đủ đơn giản. |

## Đối chiếu tọa độ

Hệ 1920 × 1080, gốc trên trái. Tọa độ đích được chiếu lại từ **makeCamera của skill hiện hành**, đúng thông số trong script lane-final.mjs, không chạy script tạo greybox và không sửa capture. Tọa độ tranh được chọn thủ công trên try2 rồi quy đổi về khung chuẩn; sai số đọc khoảng ±10 px. Độ lệch Euclid được tính từ hai điểm. Đây là số kiểm sơ bộ, Claude cần đo lại.

| Mốc / điểm neo | Greybox (px) | Try2 xấp xỉ (px) | Lệch (px) | ≤ 20 px |
|---|---|---|---:|---|
| H1, tâm mặt ổ | (715; 240) | (766; 248) | 52 | Không |
| H2, tâm mặt ổ | (1129; 183) | (1140; 186) | 11 | Có, sơ bộ |
| H3, tâm mặt ổ | (616; 392) | (596; 379) | 24 | Không |
| H4, tâm mặt ổ | (1251; 302) | (1348; 311) | 97 | Không |
| H5, tâm mặt ổ | (483; 633) | (466; 642) | 19 | Sát ngưỡng, cần đo lại |
| H6, tâm mặt ổ | (1437; 633) | (1463; 642) | 28 | Không |
| Trận Trụ trái, tâm chân | (698; 536) | (692; 520) | 17 | Có, sơ bộ |
| Trận Trụ phải, tâm chân | (1222; 536) | (1240; 520) | 24 | Không |
| Trận Trụ trái, tâm nắp | (682; 390) | (690; 352) | 39 | Không |
| Trận Trụ phải, tâm nắp | (1238; 390) | (1238; 352) | 38 | Không |
| Vọng lâu D, tâm chân | (443; 230) | (419; 266) | 43 | Không |
| Cụm F, tâm chân đá | (1454; 155) | (1550; 235) | 125 | Không |

Các mốc khác:
- **Trận Tâm A:** bao chiếu của khối A trong greybox x ≈ 813–1107, y ≈ 636–880; đĩa vẽ x ≈ 810–1113, y ≈ 700–914. Mép trên lệch khoảng +64 px, mép dưới +34 px. Đây là đối chiếu bao hình, không phải phép đo cùng một tâm 3D; hình đĩa và khối hộp khác nhau.
- **Kết Giới:** tiếp điểm phía bắc đích (960; 501), tranh khoảng (960; 497), lệch ~4 px. Ở hàng y = 772, viền trái/phải đích x ≈ 547/1373, tranh x ≈ 436/1468: lệch ngang khoảng 111/95 px; vòng quá rộng.
- **Đường:** ở hàng y ≈ 390, trục đích khoảng x1060, tranh khoảng x1025, lệch ~35 px; chưa thể xác nhận toàn bộ mép đường ≤20 px.
- **Tâm nhãn:** không vẽ người, giữ nền trống; vị trí quy chiếu (960; 880). Không có vật thể để đo tâm.
- **Cổng ải:** không có cổng trong khung; không đo tọa độ ngoài khung.

## Độ sáng

Đo trực tiếp RGB bằng ImageMagick, không sửa PNG. Luma Rec.709 trên RGB mã hóa, trung bình ô 20 × 20 px ở hệ quy chiếu 1920 × 1080; chỉ là kiểm mẫu, không bảo đảm mọi đoạn đường.

| Điểm đường / sân quanh (px) | Luma đường | Luma sân | Tỉ lệ |
|---|---:|---:|---:|
| (760;130) / (1000;130) | 0,731 | 0,343 | 2,13× |
| (815;240) / (1055;240) | 0,700 | 0,401 | 1,74× |
| (1025;390) / (1360;390) | 0,740 | 0,390 | 1,90× |

Ba mẫu đều vượt 1,3×. Luma ≥0,95 chiếm khoảng 0,068 % toàn ảnh; không phải phép đo riêng diện tích sân. Ánh sáng đi từ trên phải, vật liệu đường/sân phân biệt được; chưa kiểm màu tín hiệu bằng mặt nạ màu.

## Dừng và bàn giao

**Không làm bản chiều hoặc bản cuối:** phiếu yêu cầu “làm 1 mẫu trước, dừng chờ anh duyệt rồi mới làm tiếp”; đã dùng đủ hai lượt sinh cho mẫu 1. Không kết luận PASS hay đạt 8,5. Chưa chạy hai giám khảo mù, chưa dựng/wire vào game.

Anh cần xem sheet và try2, nhất là vòng quá rộng, cụm tùng–đá trôi phải, H4 và độ cao Trận Trụ. Claude kiểm chồng 50 %, đo lại các điểm neo, lấy ý kiến anh rồi mới chốt bước tiếp. Không làm thêm lượt sinh để vượt mức của mẫu.

Chỉ thêm các đầu ra và báo cáo được phiếu cho phép; không sửa mã, tài liệu Tu Tiên, ảnh gốc, không chạy build/test game hay lệnh Git ghi.

