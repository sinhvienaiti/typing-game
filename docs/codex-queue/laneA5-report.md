# A5 · KTX2 cho bộ hệ và thư mục chiêu

Đã chạy `tools/vfx-flipbook/run.sh ktx2 <thư mục>` cho 23 thư mục, 378 atlas: **164 nén mới, 214 bỏ qua vì MD5 khớp**. Mọi lệnh trả mã 0.

Bộ kiểm manifest theo `lane-2-flipbooks.md`, giới hạn vào đúng 23 thư mục đã chạy (kể cả thư mục con): **344 mục có job, 378 mục parse OK, 0 problems**. Dùng `node --import tsx` thay CLI `tsx` để tránh IPC bị sandbox chặn.

Đối chiếu trước/sau: PNG, JSON atlas và mọi trường manifest ngoài `ktx2` giữ nguyên. Kiểm toàn bộ KTX2: MD5 nguồn/đầu ra, byte trên đĩa, kích thước và đủ chuỗi mip đều khớp.

| Thư mục | Số atlas | MiB GPU RGBA (gồm mip) | MiB GPU KTX2 | MiB trên đĩa (KTX2) |
|---|---:|---:|---:|---:|
| aura | 9 | 274.67 | 68.67 | 42.77 |
| blood | 19 | 508.69 | 127.18 | 47.54 |
| cutin | 3 | 120.00 | 30.00 | 7.05 |
| dark | 25 | 636.85 | 159.22 | 39.27 |
| death | 1 | 6.00 | 1.50 | 0.58 |
| dragon | 1 | 21.33 | 5.33 | 1.97 |
| earth | 19 | 508.69 | 127.18 | 41.46 |
| expansion | 30 | 1125.00 | 281.26 | 137.44 |
| fire | 36 | 839.50 | 209.88 | 81.87 |
| fire/blender/atlases | 9 | 365.33 | 91.33 | 16.78 |
| fire/impact-k1-r2 | 1 | 18.00 | 4.50 | 0.79 |
| ice | 19 | 508.69 | 127.18 | 43.03 |
| light | 23 | 593.69 | 148.43 | 47.15 |
| metal | 19 | 490.50 | 122.63 | 31.18 |
| poison | 19 | 508.69 | 127.18 | 43.42 |
| star | 19 | 508.69 | 127.18 | 41.00 |
| thunder | 19 | 508.69 | 127.18 | 40.65 |
| ult | 19 | 699.00 | 174.76 | 92.32 |
| void | 19 | 508.69 | 127.18 | 38.95 |
| water | 19 | 508.69 | 127.18 | 42.41 |
| weapon | 12 | 418.50 | 104.63 | 40.28 |
| wind | 19 | 508.69 | 127.18 | 31.09 |
| wood | 19 | 508.69 | 127.18 | 35.33 |
| **Tổng** | 378 | 10695.23 | 2673.88 | 944.34 |

GPU KTX2 tính theo UASTC chuyển mã sang BC7/ASTC 4×4 (16 byte/khối), cộng từng mức mip và làm tròn khối ở mỗi mức; đây là ước tính bộ nhớ texture, không phải phép đo GPU trong trình duyệt. MiB = 1.048.576 byte. Cột đĩa chỉ cộng file KTX2 mà manifest tham chiếu, không cộng PNG giữ lại.

| File mẫu (`inspect.mjs`) | Kích thước | Mip | Kết quả |
|---|---:|---:|---|
| `fire-charge.uastc.ktx2` | 1024×1024 | 11 | PASS · Basis mở và khởi tạo chuyển mã được; UASTC, sRGB, Zstd |
| `wood-big-burst.uastc.ktx2` | 2048×1024 | 12 | PASS · Basis mở và khởi tạo chuyển mã được; UASTC, sRGB, Zstd |
| `ult-light.uastc.ktx2` | 2560×2880 | 12 | PASS · Basis mở và khởi tạo chuyển mã được; UASTC, sRGB, Zstd |

Bỏ qua theo đề bài: `sigils/`, `hybrid/`, `first-frames/`; các nhóm đã hoàn tất `beast`, `boss`, `foe`, `mech`, `meta`, `cutin-mat`, `world`, `charge-fill`, `spirit`, `expansion-phases`, `foe-i2v`. Những KTX2 hợp lệ sẵn có trong phạm vi chạy được giữ nguyên.

Tệp ghi: các `.uastc.ktx2` mới và mục `ktx2` trong manifest dưới `games/immortality-cultivation/art-src/lab/vfx/`; dữ liệu kiểm và nhật ký ở `.local/vfxlab-laneA/a5-*`; báo cáo này. Không chạy build/test game, không mở trình duyệt/cổng mạng, không lệnh Git ghi.

Chủ dự án có thể xem bảng tổng và kiểm A/B trong lab hiện có khi cần; tác vụ này không xác nhận chất lượng hình ảnh trong trình duyệt.
