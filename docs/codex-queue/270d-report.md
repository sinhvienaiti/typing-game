# Phiếu 270d · Brushfire · Khung cuối A3-R

Đã gọi `image_gen` đúng **3 lần**, dùng nguyên văn A3-R; mỗi lần chỉ đính kèm đúng khung đầu 1080 của phiếu (`v1a.try3` / `v1a.try3` / `v3.try3`). Không gọi thêm, không tự sửa kết quả.

Đã thêm **9 file** trong `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/`: mỗi tên dưới có `.src.png`, `.png`, `.prompt.txt`. Chép bằng `cp -n`, chuẩn hóa bằng đúng lệnh ImageMagick của phiếu 270, không ghi đè file cũ.

| Tên | Khổ thật trả về | Bản chuẩn hóa | Vùng sáng so với khung đầu¹ | Nhận xét |
| --- | --- | --- | --- | --- |
| `fire-impact-k1-r2-v1a.end-a.try2` | 1254×1254 | 1080×1080 | ≈22,7% | Gốc cháy cam sáng, ba thân nét vỡ thành đảo nhỏ và mất mũi kim; vẫn còn nhiều chấm sáng nhỏ dọc đường cũ. |
| `fire-impact-k1-r2-v1a.end-b.try2` | 1254×1254 | 1080×1080 | ≈23,6% | Gốc và các đảo cam đỏ còn rõ, thân đứt đoạn, mũi kim đã tắt; phần gốc vẫn khá liền. |
| `fire-impact-k1-r2-v3.end-a.try1` | 1254×1254 | 1080×1080 | ≈20,7% | Hai cung dài thành chuỗi đảo cam đỏ, gốc sáng và nét hất trái còn rõ; vẫn thấy các đốm than rời. |

¹ Luma >0,10; chia `lit_share` của ảnh cuối cho khung đầu tương ứng (`v1a.try3`: 0,0679; `v3.try3`: 0,0834), dùng số đã làm tròn của script. Cả ba nằm trong dải **15–35%** của phiếu; chưa xác nhận khóa tọa độ từng pixel.

## Đo tự động

JSON từ Python Blender chạy `docs/codex-queue/270/auto.py`:

```json
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.end-a.try2.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.0154, "hot_share_of_lit": 0.0073, "bbox": [170, 251, 811, 809], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": false}}
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.end-b.try2.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.016, "hot_share_of_lit": 0.0015, "bbox": [168, 241, 800, 808], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": false}}
{"image": "games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v3.end-a.try1.png", "size": [1080, 1080], "corner_black_max": 1.0, "lit_share": 0.0173, "hot_share_of_lit": 0.0016, "bbox": [165, 166, 772, 825], "margin_ok": true, "pass": {"size": true, "black": true, "margin": true, "hot": false}}
```

Cả ba đạt kiểm tra khổ, góc đen và lề; `hot=false` vì tỷ lệ pixel nóng dưới dải 2–6% dành cho khung đầu, trong khi A3-R yêu cầu gần như hết trắng vàng. Đây chưa phải nghiệm thu hình ảnh.

Không bỏ qua đầu việc nào. Không mở trình duyệt, chạy server, build hoặc test; không sửa code hay tài liệu Tu Tiên. Chủ sở hữu và Claude cần xem độ khớp đường nét/gốc với khung đầu và số đốm than rời trước khi chọn khung cuối.
