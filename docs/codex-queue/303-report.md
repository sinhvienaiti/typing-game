# Phiếu 303 · Ba hướng bộ đếm chuỗi từ D60

Đã gọi `image_gen` đúng **6 lần**, mỗi lần kèm đúng hai ảnh tham chiếu của phiếu, mở bằng `view_image` trước khi gọi. Giữ nguyên prompt chung, chỉ thay `<LOOK>`. Không gọi thêm hay tự vẽ lại.

Đầu ra: `games/immortality-cultivation/art-src/lab/ui/streak-counter/` — đủ 6 PNG và 6 `.prompt.txt`, chép ảnh bằng `cp -n`; kiểm tra bản chép giống hệt ảnh gốc và prompt đúng nguyên văn.

| Ảnh PNG | Khổ thật | Kiểm tra bằng mắt trên ảnh gốc |
| --- | --- | --- |
| `streak-ink-edict.v1-try1.png` | 2172 × 724 px | Đọc rõ 7, 12, 31, 64, 128; đúng 5 trạng thái; không thấy chữ thừa. |
| `streak-ink-edict.v1-try2.png` | 2172 × 724 px | Đọc rõ 7, 12, 31, 64, 128; đúng 5 trạng thái; không thấy chữ thừa. |
| `streak-jade-seal.v1-try1.png` | 2172 × 724 px | Đọc rõ 7, 12, 31, 64, 128; đúng 5 trạng thái; không thấy chữ thừa. |
| `streak-jade-seal.v1-try2.png` | 2172 × 724 px | Đọc rõ 7, 12, 31, 64, 128; đúng 5 trạng thái; không thấy chữ thừa. |
| `streak-astrolabe.v1-try1.png` | 2172 × 724 px | Đọc được 7, 12, 31, 64, 128, nét số mảnh; đúng 5 trạng thái; không thấy chữ thừa. |
| `streak-astrolabe.v1-try2.png` | 2172 × 724 px | Đọc được 7, 12, 31, 64, 128, nét số mảnh; đúng 5 trạng thái; không thấy chữ thừa. |

**Chưa đạt khổ yêu cầu:** cả 6 ảnh là 3:1, không phải 16:9. Giao diện công cụ chỉ có prompt, tham chiếu và nền trong suốt, không có tham số khổ riêng; prompt đã chốt cũng không ghi 16:9. Giữ nguyên prompt và ảnh, không cắt, kéo giãn hoặc gọi bù.

**Đính chính:** metadata trong `streak-ink-edict.v1-try1.prompt.txt` ghi nhầm 2048 × 683 theo ảnh hiển thị. Khổ đo bằng ImageMagick là **2172 × 724**; đã thêm `streak-ink-edict.v1-try1.dimensions.txt`, giữ nguyên file đã tạo theo quy tắc chỉ thêm mới.

Không bỏ ảnh nào; không sửa code, chạy build/test hay ghi Git. Đây là sáu phương án để anh chọn hướng; chưa duyệt chất lượng trong HUD thực tế. Anh cần xem ba hướng và lưu ý sai lệch tỷ lệ ảnh.
