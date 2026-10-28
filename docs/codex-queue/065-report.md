# Phiếu 065 · MF-I1 · Campfire Ring và Woodpile (pine-river)

**Ngày:** 28/10/2026. **Công cụ:** image_gen tích hợp của Codex, theo skill `imagegen`. **Kết quả:** hai ảnh chọn lượt 1, KA1–KA5 đạt; tự chấm **9/10 mỗi ảnh**. Chưa có điểm chấm lại của Claude, nên chưa coi là đã nhận.

## 1. File bàn giao

Gốc đường dẫn ảnh: `games/dragon-hold/art-src/props/pine-river/`.

| Món | Bản chọn | Prompt nguyên văn | Lượt giữ lại |
| --- | --- | --- | --- |
| Campfire Ring | `campfire-ring.png` | `campfire-ring.prompt.txt` | `campfire-ring.try1.png`, `campfire-ring.try1.prompt.txt` |
| Woodpile | `woodpile.png` | `woodpile.prompt.txt` | `woodpile.try1.png`, `woodpile.try1.prompt.txt` |

Cả hai PNG 1536×1024, RGB đục, là ảnh nguồn Tripo. Campfire Ring diễn tả vòng đá rộng 2,6 m; Woodpile diễn tả chồng củi dài 2 m, cao 1,1 m. Đây là tỉ lệ định hướng trong prompt, chưa phải kích thước model đã chuẩn hóa.

Đọc chuẩn `ART_ACCEPTANCE.md`, phiếu MF-I1, kế hoạch và bộ prompt `03-pine-river-props.md`. Đã xem `bridge-old.png`, `rock-boulder.png`, `pine-tall.png`; đối chiếu tám món phiếu 046 trên tờ tham chiếu. Giữ nguyên từng chữ các dòng chung của bộ; chỉ thay dòng `Kit prop (pine-river forest, spring): ...`, kể cả yêu cầu khổ và lề. Kiểm tự động **2/2 prompt trùng các dòng chung**. Prompt đã lưu là nội dung gửi công cụ, không rút gọn.

Bằng chứng trong `games/dragon-hold/art-src/_review/MF-I1/`:

- `contact-sheet.jpg`: hai ảnh lượt 1 cạnh nhau.
- `reference-sheet.jpg`: bridge-old và tám món phiếu 046.
- `campfire-ring-128.png`, `woodpile-128.png`: thumbnail 128×85 px, đã xem ở cỡ này.
- `measurements.json`: số đo chi tiết từng ảnh, từng mép, màu HSV.
- `identify.txt`, `selection-checks.json`: khổ ảnh, kiểm prompt và bản chọn.
- `md5-before.txt`, `md5-after.txt`, `md5-diff.txt`: bằng chứng KA1.

## 2. KA1 · Không đổi file có sẵn

Chạy `/sbin/md5 -r` cho mọi file trong thư mục đích `props/pine-river/`, theo danh sách đường dẫn đã sắp xếp, trước khi ghi prompt và sau khi chọn ảnh. **154 file trước, 162 file sau; 154/154 file cũ giữ nguyên MD5; thêm đúng 8 file bàn giao.** `diff -u` trả mã 1 vì có file mới; ngoài dòng tiêu đề/hunk, chỉ có dòng thêm, không có dòng dữ liệu bị xóa hay thay.

Bản chọn PNG và prompt được chép nguyên byte từ try1: **4/4 cặp giống hệt**. Vì vậy số đo của try1 cũng áp dụng cho bản chọn. Không ghi đè, đổi tên hoặc xóa file có sẵn; không xóa lượt thử.

## 3. KA2 · Khổ và nền

`/opt/homebrew/bin/magick identify`: **4/4 PNG nguồn và bản chọn là 1536×1024, 8-bit sRGB**. Không cần đổi khổ hay sửa nền. Nền đục theo yêu cầu ảnh nguồn Tripo; alpha sạch của sprite/decal không áp dụng.

Đọc RGB 8-bit qua ImageMagick, đo riêng mỗi dải mép 10 px. Trung bình và độ lệch chuẩn dưới đây theo thang 0–255, thứ tự R/G/B; độ lệch chuẩn dùng toàn bộ pixel của từng dải.

| Ảnh, lượt | Mép | Trung bình RGB | σ RGB (trên 255) | Kết quả |
| --- | --- | --- | --- | --- |
| campfire-ring, try1 | trên | 226.3812 / 225.9570 / 225.8339 | 0.5840 / 0.6048 / 0.5960 | Đạt |
| campfire-ring, try1 | dưới | 227.0889 / 226.6556 / 226.6218 | 0.5572 / 0.5576 / 0.5624 | Đạt |
| campfire-ring, try1 | trái | 226.1470 / 225.7267 / 225.7114 | 0.5952 / 0.6117 / 0.6154 | Đạt |
| campfire-ring, try1 | phải | 226.7675 / 226.4599 / 226.3648 | 0.5957 / 0.5758 / 0.5961 | Đạt |
| woodpile, try1 | trên | 227.4706 / 227.0779 / 226.9815 | 0.5668 / 0.5782 / 0.5852 | Đạt |
| woodpile, try1 | dưới | 227.9346 / 227.5109 / 227.4936 | 0.5658 / 0.5607 / 0.5663 | Đạt |
| woodpile, try1 | trái | 227.2163 / 226.8268 / 226.7695 | 0.5613 / 0.5775 / 0.5885 | Đạt |
| woodpile, try1 | phải | 227.7960 / 227.4901 / 227.4575 | 0.6083 / 0.6174 / 0.6378 | Đạt |

σ lớn nhất **0.6378/255 ≤ 6/255**. Sai lệch trung bình lớn nhất so với #E6E6E6 (230/230/230) là **4.2886/255 ≤ 8/255**. Cả bốn mép của hai ảnh đều đạt. Nền có nhiễu rất nhẹ từ công cụ, trong giới hạn đo.

Kiểm bằng mắt ở cỡ gốc: không thấy bóng đổ ngoài vật, ánh viền, vùng phát sáng hay vệt nắng; chuyển sắc nhẹ trên các mặt khối cùng nét cọ thuộc chất liệu của bộ. Campfire Ring có củi nguyên chưa đốt, không có lửa, khói hoặc than đỏ.

## 4. KA3 · Lề

Chạy đúng phép đo: `magick <ảnh> -fuzz 12% -trim -format '%X %Y %w %h' info:`. Lề phải = 1536 − X − w; lề dưới = 1024 − Y − h.

| Ảnh, lượt | Đầu ra X Y w h | Lề trái / trên / phải / dưới (px) | Kết quả |
| --- | --- | --- | --- |
| campfire-ring, try1 | `+105 +157 1328 674` | 105 / 157 / 103 / 193 | Đạt |
| woodpile, try1 | `+168 +61 1196 861` | 168 / 61 / 172 / 102 | Đạt |

Lề nhỏ nhất của Campfire Ring là **103 px**, Woodpile là **61 px**; đều ≥ 24 px. Không cắt mất vật.

## 5. KA4 · Màu giữ riêng

Từ RGB 8-bit của PNG, đổi từng pixel sang HSV: hue theo độ, saturation và value trong [0,1]. Đếm `(0° ≤ H ≤ 50° hoặc 165° ≤ H ≤ 190°) và S > 0,55 và V > 0,5`, mẫu số là **toàn bộ 1.572.864 px của ảnh**. Không áp dụng ngoại lệ màu.

| Ảnh, lượt | Pixel thuộc dải giữ riêng | Tỉ lệ toàn ảnh | Ngưỡng | Kết quả |
| --- | --- | --- | --- | --- |
| campfire-ring, try1 | 0 | 0.000000% | ≤ 2% | Đạt |
| woodpile, try1 | 1.394 | 0.088628% | ≤ 2% | Đạt |

Đối chiếu thêm để nền không che tỉ lệ màu trên vật: với mặt nạ `max(|R−230|,|G−230|,|B−230|) > 31`, tỉ lệ màu giữ riêng trên phần vật là **0%** ở Campfire Ring và **0,224589%** ở Woodpile. Đây chỉ là phép bổ sung; KA4 vẫn dùng mẫu số toàn ảnh. Pixel thuộc dải ở Woodpile nằm trong sắc gỗ ấm, không phải lửa hay ánh phát sáng.

## 6. KA5 · Điểm từng lượt và lựa chọn

Thứ tự điểm: **Đúng đề / Đọc được trong game / Hợp bộ / Hình khối / Dùng được cho bước sau**, mỗi tiêu chí 0–2 theo bảng năm tiêu chí của `ART_ACCEPTANCE.md`; ngưỡng ảnh 2D theo §2.2. Tổng chọn lấy mức thấp hơn giữa cỡ gốc và 128 px.

| Món | Lượt | Cỡ gốc | 128 px | Tổng chọn | Mức |
| --- | --- | --- | --- | --- | --- |
| Campfire Ring | 1 | 2 / 2 / 2 / 1,5 / 2 = 9,5 | 2 / 1,5 / 2 / 1,5 / 2 = 9 | **9/10** | Đạt |
| Woodpile | 1 | 2 / 2 / 1,5 / 2 / 2 = 9,5 | 2 / 1,5 / 1,5 / 2 / 2 = 9 | **9/10** | Đạt |

**Campfire Ring:** vòng đá xám ấm khép kín, củi nguyên xếp chéo, đúng hai ghế gỗ hai bên; mặt đáy cùng phẳng. Nét cọ, gỗ mờ và đá pha tím xám hợp bộ. Ghế gỗ cong khá rõ, hơi giống ghế được đẽo tạo dáng hơn khúc gỗ thẳng nên trừ hình khối 0,5. Ở 128 px, các thanh củi giữa vòng hơi dồn nên trừ độ đọc 0,5. Vẫn nhận rõ vòng đá và hai ghế.

**Woodpile:** củi chẻ xếp giữa đúng hai cọc, gốc cây áp sát cọc, rìu cắm lưỡi vào mặt gốc, ba mẩu gỗ ở chân; các phần chạm nhau, không thấy vật bay. Cùng kiểu vỏ gỗ và nét cọ với bridge-old; mặt gỗ cắt sáng và ấm hơn bộ cầu một chút nên trừ hợp bộ 0,5. Ở 128 px, chồng củi đọc rõ nhưng phần đầu rìu nhỏ nên trừ độ đọc 0,5.

Chọn **try1 cho cả hai** vì đúng đề, đủ KA1–KA5 và vượt ngưỡng 8 ở cả hai cỡ. Không cần lượt 2–3; không chỉnh sửa nội dung ảnh sau khi tạo.

## 7. Phạm vi và việc còn lại

Đã tạo đúng hai ảnh và prompt, giữ toàn bộ lượt thử, bằng chứng và báo cáo này. Không tạo âm thanh hoặc model 3D vì ngoài phiếu. Không chạy Git, build, test suite, dev server, trình duyệt hoặc mạng ngoài image_gen; không đọc/ghi Tu Tiên và không sửa mã hay tài liệu khác.

Chủ dự án xem `contact-sheet.jpg`, nhất là dáng cong của hai ghế và sắc sáng của mặt củi. **Claude cần chấm lại ≥ 8** trước khi nhận. Bước dựng Tripo và chuẩn hóa kích thước thật chưa nằm trong phiếu này.
