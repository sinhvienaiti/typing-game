# Phiếu 366 · Dải vệt đất sấm sét

Đã tạo bằng **image_gen: 4 lượt**, kiểm hình bằng **view_image: 6 lượt**.

## Tệp bàn giao

Thư mục S: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

- `thunder-trail-rock.v1-try1.png`, `thunder-trail-glow.v1-try1.png`: 2048×256.
- `thunder-trail-cap.v1-try1.png`, `thunder-trail-cap-glow.v1-try1.png`: 512×256.
- Bốn `.prompt.txt`: prompt nguyên văn, tham chiếu, try gốc và thông số hậu kỳ.
- `thunder-trail-366-sheet.jpg`: ba đoạn nối cap ở bề ngang 64px, nền sáng/tối, bản cộng sáng phóng gần.

Tái dùng chất đá hai scar try9; groove định hướng bố cục. Glow sửa từ rock, cap theo rock, cap-glow sửa từ cap. Rock cắt đúng tỉ lệ, hoà chéo 124px; glow đăng ký trên dải đã nối. Cap và cap-glow dùng chung đoạn chuyển tiếp 112px. Sau hoà chéo, chặn dư xanh ở RGB, giữ alpha.

## Kiểm bằng script

- Mép lặp rock/glow và mép cap hai lớp: **MAE 0, max 0**, gồm alpha đá.
- Trước lọc, năng lượng mẫu glow trùng khe: **91,41%**; cap-glow **73,88%**, cần dịch (+4,+16)px.
- Sau lọc: **100%** năng lượng nằm trong khe (`max(RGB)<68, alpha>220`); không tràn alpha. Đây là kết quả ràng buộc mặt nạ, không phải độ khớp nguyên bản AI.
- Sáng tối đa **229/255**; ngoài khe đen thuần; không dư xanh.

## Tự chấm

| Lớp | Điểm yếu nhất /10 |
|---|---:|
| Rock | 8,2 |
| Glow | 8,2 |
| Cap | 8,1 |
| Cap-glow | 8,0 |

Nhánh sét đọc được ở 64px, không thấy đường cắt cứng; trắng ngà–vàng nhạt hợp D65. Cap-glow yếu nhất: vài nhánh mảnh bị mặt nạ cắt ngắn. Anh xem tấm ghép, nhất là đầu dải. Không tích hợp, chạy build/test hay đánh giá trong game vì ngoài phạm vi; đây chỉ là tự chấm linh kiện.
