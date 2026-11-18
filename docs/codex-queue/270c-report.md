# Phiếu 270c · Brushfire · Khung cuối A3 và lượt sửa S4

Đã gọi `image_gen` đúng **3 lần**, dùng nguyên văn A3/A3/S4, mỗi lần chỉ đính kèm đúng ảnh nguồn của phiếu. `end-b` sửa lại từ `v1a.try3.png`, không từ `end-a`. Không gọi thêm, không tự sửa kết quả.

Đã thêm **9 file** trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`; mỗi tên dưới có `.src.png`, `.png`, `.prompt.txt`. Chép nguồn bằng `cp -n`, chuẩn hóa bằng đúng lệnh ImageMagick của phiếu 270, không ghi đè ảnh cũ.

| Tên | Khổ thật trả về | Bản chuẩn hóa | Nhận xét |
| --- | --- | --- | --- |
| `fire-impact-k1-r2-v1a.end-a.try1` | 1254×1254 | 1080×1080 | Gốc và phần nét còn lại nhìn bám đường cũ, chưa xác nhận trùng từng pixel; ba mũi kim đã tắt, thân còn khá liền ở gốc và có các đảo than đỏ phía trên. |
| `fire-impact-k1-r2-v1a.end-b.try1` | 1254×1254 | 1080×1080 | Gốc và các đảo than nhìn nằm theo ba đường cũ, chưa xác nhận trùng từng pixel; ba mũi kim đã tắt, phần giữa đứt rõ hơn `end-a`, còn vài đốm than sáng. |
| `fire-impact-k1-r2-v3.try3` | 1254×1254 | 1080×1080 | Nét trên đã mở, mũi kim hướng phải gần ngang và cao hơn hẳn mũi nét dưới; giữ nét hất trái, khe đen rộng và viền trắng vàng ở mép ngoài. |

## Đo tự động

Dòng JSON từ Python Blender chạy `docs/codex-queue/270/auto.py`:

```json
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.end-a.try1.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.0056, "hot_share_of_lit": 0.0, "bbox": [170, 243, 800, 801], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": false}}
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.end-b.try1.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.0047, "hot_share_of_lit": 0.0, "bbox": [165, 246, 808, 803], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": false}}
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v3.try3.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.0834, "hot_share_of_lit": 0.0289, "bbox": [125, 163, 902, 834], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": true}}
```

Hai khung cuối có `hot=false` vì không còn pixel đạt ngưỡng nóng; A3 yêu cầu gần như hết trắng vàng. Theo ngưỡng sáng của script, diện tích sáng còn khoảng **8,2%** (`end-a`) và **6,9%** (`end-b`) so với khung đầu (`lit_share=0.0679` trong phiếu 270b), thấp hơn mục tiêu khoảng một phần tư. Đây là số đo theo ngưỡng, không phải toàn bộ diện tích than đỏ nhìn thấy.

Không bỏ qua đầu việc nào. Không mở trình duyệt, chạy dev server, build hoặc test. Chủ sở hữu và Claude cần xem độ khớp đường nét/gốc với khung đầu, mức tắt có quá sâu không, rồi chọn `end-a` hoặc `end-b`; xem thêm độ mở của nét trên `v3.try3`. Giữ nguyên cả ba kết quả để duyệt, chưa coi là nghiệm thu hình ảnh.
