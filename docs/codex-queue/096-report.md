# Phiếu 096 · Rồng Giữ Ải · Huy hiệu và chữ logo màn tựa

**Ngày:** 28/10/2026. **Người làm:** Codex. **Trạng thái:** đã tạo đủ hai phần,
qua kiểm kỹ thuật và tự chấm; chờ Claude chấm lại ≥ 8 trước khi tích hợp.

## 1. Bản giao

Thư mục: [`games/dragon-hold/art-src/ui/title/`](../../games/dragon-hold/art-src/ui/title/).
Mỗi tên dưới đây có đủ sáu file:

| Tên | Ảnh thử và prompt | Bản chọn và prompt | Bản tách nền |
|---|---|---|---|
| `title-emblem` | `.try1.png`, `.try1.prompt.txt` | `.png`, `.prompt.txt` | `.alpha.png`, `.256.png` |
| `title-logo` | `.try1.png`, `.try1.prompt.txt` | `.png`, `.prompt.txt` | `.alpha.png`, `.256.png` |

- [Huy hiệu alpha 1024](../../games/dragon-hold/art-src/ui/title/title-emblem.alpha.png):
  Hỏa Long đỏ cam, bụng kem, sừng và gai sẫm, đậu trên cổng đá cũ; hai cây
  thông hai bên và một lọn lửa nhỏ. Không chữ, số, khung hay viền bao huy hiệu.
- [Chữ logo alpha 1024](../../games/dragon-hold/art-src/ui/title/title-logo.alpha.png):
  **Rồng Giữ Ải**, kem ấm, viền xanh thông sẫm, ánh cam than hồng nhẹ.

Các `.png` không hậu tố và `.try1.png` giữ nguyên ảnh nền magenta từ công cụ.
Claude dùng `.alpha.png` hoặc `.256.png` để ghép màn tựa.

## 2. Sinh ảnh và prompt

Dùng công cụ tích hợp **image_gen**, hai lời gọi riêng, mỗi ảnh **1/3 lượt**;
không dùng API, CLI hay mạng khác. Prompt nguyên văn được lưu cạnh ảnh thử;
prompt của bản chọn giống nguyên văn prompt lượt 1.

| Ảnh | Kích thước nguồn | Diễn giải prompt lượt 1 | Sửa prompt ở lượt sau |
|---|---|---|---|
| Huy hiệu | 1448 × 1086 | Giữ nguyên câu phong cách nhà; khối rộng khoảng 4:3, thân rồng liền, bụng kem, sừng và gai nâu sẫm, cổng vòm mở rõ ở nửa dưới, hai cây thông, một lọn lửa nhỏ; nền magenta phẳng, vật không hồng/tím sáng | Không cần lượt 2–3; lỗi nền và mép sửa được bằng công cụ |
| Chữ logo | 2172 × 724 | Một dòng `Rồng Giữ Ải`; đánh vần từng chữ và mô tả riêng mũ + huyền của `ồ`, móc + ngã của `ữ`, hỏi trên `Ả`; nét cọ có chân, kem ấm và viền xanh thông | Không cần lượt 2–3; chữ và dấu đúng ngay lượt 1 |

Tham chiếu đã xem: dòng đầu `backdrops/pine-river-far.prompt.txt` và ba icon
`skill-fire-breath.png`, `skill-sky-fire.png`, `dragon-heart.png`.

## 3. Hậu kỳ và các chỗ làm khác

Python 3 thư viện chuẩn và **ImageMagick 7.1.2-34**; không cài thêm thư viện.
Script, công thức, tham số lệnh và cách chạy lại ở
[`_review/096/commands.md`](../../games/dragon-hold/art-src/_review/096/commands.md),
[`process.py`](../../games/dragon-hold/art-src/_review/096/process.py),
[`fix-resample.py`](../../games/dragon-hold/art-src/_review/096/fix-resample.py),
[`bootstrap.py`](../../games/dragon-hold/art-src/_review/096/bootstrap.py).

Nền sinh thực tế hơi lệch `#FF00FF`, có biến thiên nhẹ. Trung vị RGB ở mép
nguồn là huy hiệu `(247,4,249)`, chữ `(250,5,249)`. Giữ nguyên nguồn, tách bằng
ước lượng lượng magenta rồi khử màu nền khỏi RGB, cắt khối và thêm lề trong
khung trong suốt. Không cần sinh lại để sửa lỗi này.

Lần hậu kỳ đầu phát hiện Lanczos sinh lại pixel magenta ở mép. Đã giữ nguyên
bốn bản hậu kỳ đầu dưới `_review/096/*.before-resample-fix.png`, rồi sửa
**bốn file hậu kỳ vừa tạo trong phiên này** bằng cách trừ dư magenta khỏi R/B,
giữ alpha. Số pixel sửa: huy hiệu 1024 **177**, huy hiệu 256 **47**, chữ 1024
**232**, chữ 256 **11**. Không ghi đè file có trước phiên; ảnh thử và nguồn
chọn không thay đổi. Đây là bước sửa bằng công cụ, không phải lượt sinh mới.

Không sửa mã, tài liệu khác hay `public/`; không chạy lệnh Git, dev server,
trình duyệt, build hoặc bộ test game. Không đọc/ghi Tu Tiên. Không có phần
nào của phiếu bị bỏ. Việc tích hợp và quyết định nhận thuộc Claude.

## 4. KA1 · Bảo toàn file

Đã chạy `/sbin/md5 -r` **mọi file** trong `games/dragon-hold/art-src/ui/`,
sắp theo đường dẫn, trước khi ghi file đầu tiên và sau khi hoàn tất ảnh.

| Chỉ số | Kết quả |
|---|---:|
| File trước khi làm | 41 |
| File sau khi giao | 53 |
| File cũ giữ nguyên MD5 | 41/41 |
| File thêm | 12 |
| File đổi / mất | 0 / 0 |
| `diff` | Chỉ thêm dòng; không có dòng `<` |

Bằng chứng: [`md5-before.txt`](../../games/dragon-hold/art-src/_review/096/md5-before.txt),
[`md5-after.txt`](../../games/dragon-hold/art-src/_review/096/md5-after.txt),
[`md5-diff.txt`](../../games/dragon-hold/art-src/_review/096/md5-diff.txt),
[`md5-summary.json`](../../games/dragon-hold/art-src/_review/096/md5-summary.json).

## 5. Kiểm số đo và ảnh kiểm

Bbox dùng mọi pixel **alpha > 0**; tọa độ phải/dưới là cận ngoài.
Lề ghi theo thứ tự **trái / trên / phải / dưới**. Pixel hồng bị cấm là
alpha > 0, hue **285–330°**, S > **0,5**, tính từ RGB sRGB của PNG sau mã hóa.

| Bản giao | Kích thước | Bbox `(x0,y0,x1,y1)` | Lề, px | Pixel alpha > 0 | Pixel hồng / % |
|---|---|---|---|---:|---:|
| Huy hiệu `.alpha.png` | 1024 × 768 | 51, 48, 972, 720 | 51 / 48 / 52 / 48 | 315.900 | 0 / 0% |
| Huy hiệu `.256.png` | 256 × 192 | 12, 10, 243, 180 | 12 / 10 / 13 / 12 | 21.019 | 0 / 0% |
| Chữ `.alpha.png` | 1024 × 352 | 62, 48, 962, 304 | 62 / 48 / 62 / 48 | 97.670 | 0 / 0% |
| Chữ `.256.png` | 256 × 88 | 23, 9, 235, 67 | 23 / 9 / 21 / 21 | 6.899 | 0 / 0% |

Tỉ lệ khung huy hiệu **4:3**; bbox khối khoảng **1,37:1**. Hai bản 1024 đều
có lề tối thiểu **48 px**, vượt yêu cầu 32 px. Tỉ lệ pixel hồng bằng 0 cả
trên toàn khung lẫn trong tập pixel alpha > 0.

Số máy đọc được ở [`measurements-final.json`](../../games/dragon-hold/art-src/_review/096/measurements-final.json).
`measurements.json` lưu số trước sửa dư màu để đối chiếu, không phải số giao.

- [096-proof.jpg](../../games/dragon-hold/art-src/_review/096-proof.jpg):
  cả hai bản chọn trên nền tối **#14201a** và sáng **#efe6d2**, cạnh dài
  1024, 256, 64 px. Đã xem ảnh. **Ở 64 px còn nhận ra rồng đỏ cam phía trên
  và cổng đá vòm mở phía dưới** trên cả hai nền; chi tiết vảy và lá mất là
  bình thường ở cỡ này. Logo 256 px đọc rõ; ở 64 px chữ quá nhỏ để dùng
  làm cỡ tựa chính, không coi đây là bằng chứng đọc đủ dấu.
- [096-edge.jpg](../../games/dragon-hold/art-src/_review/096-edge.jpg):
  crop sừng/đầu, lòng cổng, dấu huyền/mũ và dấu ngã/móc, phóng **4×** bằng
  nearest-neighbour trên hai nền. Đã xem; không thấy viền hồng. Có nét cọ
  và bậc pixel ở độ phóng, không phải mảng màu nền sót.
- [096-spelling.jpg](../../games/dragon-hold/art-src/_review/096-spelling.jpg):
  từng chữ có dấu cắt từ ảnh nguồn, phóng đúng **4×**, đặt cạnh cùng chữ
  in bằng **Arial**, file `/System/Library/Fonts/Supplemental/Arial.ttf`.
  Các ảnh kiểm chỉ chứa kết quả cần cho báo cáo; không tạo chuỗi khung thô.

### Chính tả phần B

| Thành phần | Quan sát đối chiếu với Arial | Kết quả |
|---|---|---|
| `R-ồ-n-g` | Đúng thứ tự chữ; `ồ` có thân o, mũ và nét huyền nghiêng từ trái trên xuống phải dưới | Đạt |
| `G-i-ữ` | `ữ` có thân u, móc bên phải gắn thân và dấu ngã riêng bên trên | Đạt |
| `Ả-i` | A hoa có dấu hỏi phía trên, không có chấm dưới; sau đó là i thường | Đạt |
| Toàn dòng | `Rồng Giữ Ải`, đúng hoa/thường và hai khoảng cách từ | Đạt lượt 1 |

Không dùng font để sửa hay thay chữ trong ảnh logo; Arial chỉ làm mẫu kiểm.

## 6. KA5 · Tự chấm

Mỗi tiêu chí 0–2 theo ART_ACCEPTANCE §2.2. “Dùng tiếp” chỉ chấm 2 sau khi
toàn bộ kiểm bắt buộc của từng phần đã đạt. Cỡ bảng là cạnh dài.

| Ảnh / cỡ | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Tổng / mức |
|---|---:|---:|---:|---:|---:|---|
| Huy hiệu 1024 | 2 | 2 | 1,5 | 1,5 | 2 | **9/10 · Đạt tự chấm** |
| Huy hiệu 256 | 2 | 2 | 1,5 | 1,5 | 2 | **9/10 · Đạt tự chấm** |
| Chữ 1024 | 2 | 2 | 1,5 | 2 | 2 | **9,5/10 · Đạt tự chấm** |
| Chữ 256 | 2 | 2 | 1,5 | 2 | 2 | **9,5/10 · Đạt tự chấm** |

Trừ nhẹ huy hiệu vì nhiều chi tiết lá/đá hơn bộ icon nét lớn, phần thân và
cánh sau có chỗ chồng khối; không thấy lỗi giải phẫu lớn cản dùng. Chữ có
bề mặt hơi vàng và nổi khối hơn nét mờ lì của phông, nên Hợp bộ giữ 1,5.

**Chủ dự án/Claude cần xem:** ảnh proof để xét độ nổi của huy hiệu trên
màn tựa, ảnh chính tả để chấm độc lập ba dấu, rồi chấm lại trước khi chép
sang `public/`. Chưa có nghiệm thu hay tích hợp trong game.
