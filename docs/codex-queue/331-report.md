# Phiếu 331 · Bốn ảnh nguồn 2D Tu Tiên

Hoàn tất ngày 11/11/2026. Dùng **5/8 lần gọi `image_gen`**, **8/8 lần mở `view_image`** (6 tham chiếu, loạt sét bản đầu, tấm ghép cuối). Chỉ dùng ảnh nội bộ được phiếu chỉ định. Tự chấm ảnh nguồn; chưa đánh giá hiệu ứng trong game hay chuyển động Firefly.

`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.

Đã thêm 4 ảnh `try1` đúng tên phiếu, 1 ảnh loạt sét `try2`, 4 bản `-pad.png`; mỗi ảnh có `.prompt.txt` ghi công cụ, đường dẫn tham chiếu, prompt nguyên văn và khổ thật. Bản gốc đều chép bằng `cp -n`. Tấm ghép: [top-down-331-sheet.jpg](../../games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills/top-down-331-sheet.jpg), kèm hồ sơ lệnh ghép `.prompt.txt`.

## Bản chọn và tự chấm

Điểm chung lấy **tiêu chí thấp nhất**, không lấy trung bình. Cột “Đúng hình” gồm góc nhìn, bảng màu, nền đen và không có chữ đọc được. Lề theo thứ tự **trái / phải / trên / dưới**, đơn vị %.

| Ảnh chọn trong S | Đọc ra ngay | Cuốn hút, mức thương mại | Đúng hình | Khung đầu video | Chung | Lề đo được | Vẽ lại | Nhận xét |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| `foe-boss-summon-sigil-top.v1-try1-pad.png` | 9,0 | 8,7 | 8,8 | 9,0 | **8,7** | 13,19 / 13,82 / 12,15 / 15,76 | Không | Huy hiệu đầu sói phẳng rõ, vòng rune tròn đều, đỏ rực trên nền đen mực. |
| `foe-commander-howl-ring-top.v1-try1-pad.png` | 8,7 | 8,5 | 8,7 | 8,8 | **8,5** | 13,54 / 13,75 / 13,26 / 15,62 | Không | Sóng đỏ nhiều lớp, mép khói rách; các điểm sáng đối xứng hơi thiên về trang trí. |
| `thunder-scorch-crack-top.v1-try1-pad.png` | 9,0 | 8,7 | 8,6 | 8,8 | **8,6** | 12,85 / 13,26 / 10,76 / 13,61 | Không | Đá cháy than nứt sâu, điện còn nối giữa mảnh đá, khói mỏng; không thành vòng phép. |
| `thunder-bolt-barrage.v1-try2-pad.png` | 9,0 | 8,6 | 8,2 | 8,4 | **8,2** | 15,87 / 15,98 / 0 / 5,77 | Có, 1 lần | Năm tia chính phân nhánh, tia giữa lớn nhất; vài nhánh ngoài kết thúc hơi đột ngột, cần anh nhìn kỹ. |

## Kiểm tra kỹ thuật

- ImageMagick đo hộp bao mọi pixel có `max(R,G,B) > 3/255`; bỏ qua nhiễu gần đen 0–3. Đây là lề gần đen, không coi mọi pixel trong lề gốc đều bằng 0 tuyệt đối.
- Lề gốc trước đệm: ấn sói **7,74 / 8,45 / 6,54 / 10,69**; vòng hú **8,13 / 8,37 / 7,81 / 10,53**; đất sét **7,34 / 7,81 / 4,94 / 8,21**. Đệm cả ba để đạt lề 10% theo khối prompt, giữ nguyên ảnh gốc.
- Loạt sét `try1`: lề **1,70 / 2,55 / 0 / 9,69**; điểm đọc hình / cuốn hút / đúng hình / video = **9,0 / 8,6 / 7,8 / 7,2**, chung **7,2**. Vẽ lại vì nhánh điện quá sát hai bên; chọn `try2` cao hơn.
- Ảnh gốc vuông **1254×1254**; bản đệm **1440×1440**. Hai bản sét công cụ trả **941×1672** (gần 9:16); bản chọn đệm thành **945×1680**, đúng **9:16**, neo trên để tia tiếp tục đi vào từ mép trên.
- Bốn góc của cả bốn bản chọn đều **RGB(0,0,0)**. Ba dấu đất có lề mỗi cạnh trên 6%; sét có lề trái/phải trên 10%, mép trên 0% đúng yêu cầu tia đánh từ mép khung xuống.
- So sánh vùng ảnh gốc trong mỗi bản đệm: **AE = 0 pixel khác biệt**. Không cắt, co giãn hay tô lại ảnh bằng mã. Tấm ghép đen **2000×2082**, có đủ tên bốn bản chọn.

Không bỏ ảnh nào. Không tạo video, sửa mã, chạy build/test hay ghi Git vì ngoài phạm vi phiếu. Anh xem tấm ghép, ưu tiên kiểm đầu nhánh ngoài của loạt sét và độ đọc của đá cháy trước khi dùng làm khung đầu Firefly.
