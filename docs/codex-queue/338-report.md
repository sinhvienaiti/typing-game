# Phiếu 338 · Ngũ Lôi Oanh Đỉnh trắng xanh · 11/11/2026

Đã vẽ đủ **10/10 ảnh** bằng `image_gen`, dùng **10/13 lần gọi**, không vẽ lại. Đã mở **11/24 ảnh bằng `view_image`**: 10 nguồn và tấm ghép; các đầu ra được xem trực tiếp khi công cụ trả ảnh. Mỗi ảnh dùng đúng nguồn trong phiếu, chép bằng `cp -n`, kèm `.prompt.txt` ghi công cụ, đường dẫn tham chiếu, prompt tiếng Anh nguyên văn và khổ thật. Không dùng ảnh ngoài repo, không sửa tệp có sẵn.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`.

Tệp mới: 10 PNG `.v2-try1.png` trong bảng, 10 prompt cùng gốc tên; thêm 4 PNG `-pad.png` cùng prompt thao tác đệm; tấm ghép **`S/thunder-five-338-compare.jpg`** (2016 × 2910). Tấm ghép có đủ 10 cặp: tím bên trái, trắng xanh bên phải, dùng ảnh chưa đệm để so bố cục ở cùng khung.

## Tự chấm và kiểm tra

Điểm cuối là **tiêu chí thấp nhất**, không lấy trung bình. Màu = bảng trắng xanh; Thiết kế = giữ nguồn, riêng vòng ấn sửa năm ký hiệu theo phiếu; Đẹp/lực = cuốn hút, sang và có lực đúng vai trò; Sạch = nền đen, không chữ; Video = phù hợp làm khung đầu. Tất cả đạt từ 8 nên không dùng 3 lượt vẽ lại dự phòng. Đây là tự chấm ảnh nguồn, chưa phải chấm hiệu ứng ghép trong game.

| Ảnh mới trong S | Tím đo được | Màu | Thiết kế | Đẹp/lực | Sạch | Video | Điểm cuối | Lề nhỏ nhất trước → sau | Nhận xét | Vẽ lại |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `thunder-five-strike.v2-try1.png` | 1,0756% | 9,2 | 8,8 | 9,0 | 9,7 | 8,6 | **8,6** | 0,00% → 6,55% (đệm) | Giữ xoáy mây và năm đường sét hội tụ; lõi trắng rất mạnh. | Không |
| `thunder-five-cloud-vortex-top.v2-try1.png` | 0,3009% | 9,3 | 9,2 | 9,1 | 9,7 | 9,1 | **9,1** | 9,97% → 9,97% | Tâm đen, năm nút và mây xoắn nhiều lớp rõ; giữ góc nhìn thẳng từ trên. | Không |
| `thunder-five-caster-seal.v2-try1.png` | 0,2863% | 9,3 | 8,7 | 8,7 | 9,7 | 8,8 | **8,7** | 4,94% → 6,61% (đệm) | Năm ký hiệu đã thành nhánh sét mảnh, gãy, sắc; vòng ấn và vị trí được giữ. | Không |
| `thunder-five-impact-burst.v2-try1.png` | 0,4660% | 9,2 | 9,2 | 9,0 | 9,7 | 8,8 | **8,8** | 1,91% → 6,55% (đệm) | Giữ quạt tia, tâm nổ và các mảnh đá; lực bùng nổ rõ. | Không |
| `thunder-five-shock-ring-top.v2-try1.png` | 0,2104% | 9,2 | 9,3 | 8,7 | 9,7 | 8,9 | **8,7** | 8,45% → 8,45% | Giữ vòng tròn mảnh, năm nút, khói và vụn ngoài rìa. | Không |
| `thunder-five-lingering-arcs.v2-try1.png` | 0,2294% | 9,2 | 9,1 | 8,5 | 9,7 | 8,7 | **8,5** | 8,55% → 8,55% | Giữ lớp dư thấp và ba dải khói chính; hợp vai trò hậu dư nên nhẹ hơn ảnh chính. | Không |
| `thunder-single-bolt-a.v2-try1.png` | 0,7680% | 9,2 | 9,1 | 8,7 | 9,7 | 8,8 | **8,7** | 16,79% → 16,79% | Giữ năm góc gãy lớn, áo điện nhiều lớp; lõi trắng rộng. | Không |
| `thunder-single-bolt-b.v2-try1.png` | 0,9573% | 9,2 | 9,1 | 9,0 | 9,6 | 8,9 | **8,9** | 5,42% → 6,62% (đệm) | Giữ nhánh đôi mở rồi hội tụ; đầu ra thấp hơn nguồn 1 px. | Không |
| `thunder-single-bolt-c.v2-try1.png` | 2,8380% | 9,1 | 9,3 | 8,8 | 9,7 | 8,8 | **8,8** | 7,55% → 7,55% | Giữ đường chéo lệch trái và ba nhánh phụ dài; còn chút tím ở rìa tối. | Không |
| `thunder-single-bolt-d.v2-try1.png` | 2,0576% | 9,1 | 9,2 | 8,6 | 9,7 | 8,7 | **8,6** | 28,69% → 28,69% | Giữ dáng mảnh, nhiều góc gãy nhỏ và khoảng đen rộng; lõi trắng rõ hơn. | Không |

Đo bằng `/opt/homebrew/bin/magick` (ImageMagick 7), trực tiếp trên PNG: đổi HSB; điểm sáng có `B > 0,35`; tỉ lệ tím = số điểm sáng có `255° ≤ H ≤ 330°` / tổng điểm sáng. Không lọc thêm độ bão hòa. Cả 10 ảnh ≤ 15%, thực tế **0,2104–2,8380%**. Đệm đen không thay đổi tỉ lệ này.

Lề đo tới hộp bao các điểm có `max(R,G,B) > 2%`; ảnh dọc kiểm trái/phải, ảnh khác kiểm cả bốn phía. Bảng ghi lề nhỏ nhất trong các phía phải kiểm. Kiểm bốn vùng góc, mỗi vùng rộng/cao 6% khung: cực đại RGB **0–3/255**, nền gần đen thuần. Ảnh không có chữ, nhân vật, watermark hay tàn lửa; màu cam/vàng/hồng không thấy khi kiểm ảnh.

Khổ gốc đầu ra: ảnh 1, A, C, D **941 × 1672**; ảnh 2–5 **1254 × 1254**; ảnh 6 **1672 × 941**; B **941 × 1671** (chênh 1 px so nguồn, vẫn khổ dọc xấp xỉ 9:16).

## Bản đệm để dùng bước tiếp theo

Chỉ thêm nền đen bằng `magick -extent`, không co giãn hay vẽ lại. Đã so phần bên trong với PNG sinh gốc: sai khác điểm ảnh bằng **0** cho cả bốn bản.

- `S/thunder-five-strike.v2-try1-pad.png`: **1084 × 1924**.
- `S/thunder-five-caster-seal.v2-try1-pad.png`: **1301 × 1301**.
- `S/thunder-five-impact-burst.v2-try1-pad.png`: **1389 × 1389**.
- `S/thunder-single-bolt-b.v2-try1-pad.png`: **967 × 1715**.

Các ảnh còn lại dùng nguyên `.v2-try1.png`. Prompt cạnh từng bản đệm giữ prompt sinh gốc và ghi thêm lệnh đệm, khổ sau đệm.

**Anh xem:** tấm ghép `thunder-five-338-compare.jpg`, đặc biệt vòng ấn số 3 (năm ký hiệu thành sét thật), độ rộng lõi trắng ở 1/A/B và độ mảnh của D. Không bỏ ảnh nào; không gặp giới hạn công cụ. Không tích hợp, sửa mã, âm thanh, chạy build/test, mở cổng mạng hay dùng lệnh Git ghi vì ngoài phạm vi.
