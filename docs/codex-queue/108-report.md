# Báo cáo 108 · Tuyến Cuối / Last Line · Chuẩn hóa sáu icon súng

Ngày 29/10/2026, thực hiện tại repo cha trên Mac mini M4 bằng Python 3 và ImageMagick 7.1.2-34; `ART_MAGICK=/opt/homebrew/bin/magick`.

**Đã tạo 24 PNG và tờ xem; chưa đạt điều kiện “Xong khi”.** KA1 và khổ đạt; KA3 không đạt 6/6 bản 1024 vì hộp alpha không vuông; KA4 đạt 8/24 file theo đúng ngưỡng alpha 255 và chênh luma ≤ 0,08. Giữ nguyên tỉ lệ, màu và alpha nguồn, chỉ cắt/co/đệm theo phiếu; không sửa hình để ép kết quả kiểm đạt.

## File đã tạo

Mỗi hàng gồm bản 1024 và ba bản thu trực tiếp từ bản 1024. Tất cả nằm trong `games/typing-survival/art-src/ui/icons/`.

| Icon | 1024 × 1024 | 256 × 256 | 128 × 128 | 64 × 64 |
| --- | --- | --- | --- | --- |
| Pulse Gun (`gun-xung`) | [gun-xung.norm.png](../../games/typing-survival/art-src/ui/icons/gun-xung.norm.png) | [gun-xung.norm.256.png](../../games/typing-survival/art-src/ui/icons/gun-xung.norm.256.png) | [gun-xung.norm.128.png](../../games/typing-survival/art-src/ui/icons/gun-xung.norm.128.png) | [gun-xung.norm.64.png](../../games/typing-survival/art-src/ui/icons/gun-xung.norm.64.png) |
| Heat Beam (`gun-tia`) | [gun-tia.norm.png](../../games/typing-survival/art-src/ui/icons/gun-tia.norm.png) | [gun-tia.norm.256.png](../../games/typing-survival/art-src/ui/icons/gun-tia.norm.256.png) | [gun-tia.norm.128.png](../../games/typing-survival/art-src/ui/icons/gun-tia.norm.128.png) | [gun-tia.norm.64.png](../../games/typing-survival/art-src/ui/icons/gun-tia.norm.64.png) |
| Scatter Gun (`gun-tan`) | [gun-tan.norm.png](../../games/typing-survival/art-src/ui/icons/gun-tan.norm.png) | [gun-tan.norm.256.png](../../games/typing-survival/art-src/ui/icons/gun-tan.norm.256.png) | [gun-tan.norm.128.png](../../games/typing-survival/art-src/ui/icons/gun-tan.norm.128.png) | [gun-tan.norm.64.png](../../games/typing-survival/art-src/ui/icons/gun-tan.norm.64.png) |
| Rail Gun (`gun-ray`) | [gun-ray.norm.png](../../games/typing-survival/art-src/ui/icons/gun-ray.norm.png) | [gun-ray.norm.256.png](../../games/typing-survival/art-src/ui/icons/gun-ray.norm.256.png) | [gun-ray.norm.128.png](../../games/typing-survival/art-src/ui/icons/gun-ray.norm.128.png) | [gun-ray.norm.64.png](../../games/typing-survival/art-src/ui/icons/gun-ray.norm.64.png) |
| Star Mortar (`gun-phao-sao`) | [gun-phao-sao.norm.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.norm.png) | [gun-phao-sao.norm.256.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.norm.256.png) | [gun-phao-sao.norm.128.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.norm.128.png) | [gun-phao-sao.norm.64.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.norm.64.png) |
| Nova (`nova`) | [nova.norm.png](../../games/typing-survival/art-src/ui/icons/nova.norm.png) | [nova.norm.256.png](../../games/typing-survival/art-src/ui/icons/nova.norm.256.png) | [nova.norm.128.png](../../games/typing-survival/art-src/ui/icons/nova.norm.128.png) | [nova.norm.64.png](../../games/typing-survival/art-src/ui/icons/nova.norm.64.png) |

- [Tờ xem 1800 × 804](../../games/typing-survival/art-src/_review/108-sheet.jpg): đủ ba hàng; hàng cuối thử mỗi icon trên cả viền xanh `#37c9ff` và cam `#ff8c42`, dày 1 px.
- [Thư mục đo và script](../../games/typing-survival/art-src/_review/108/): `01-normalize.py`, `02-verify.py`, `03-sheet.py`, `04-integrity.py`, `05-report.py`; `normalization.json`, `commands.json`, `measurements.json`, `integrity.json`; `original-files.txt`, `md5-before.txt`, `md5-after.txt`, `md5-diff.txt`.

## Cách xử lý

Đọc đúng `<tên>.png`, không dùng `.v1.png`. Hộp bao tính trên alpha 8 bit > 16, tọa độ dưới đây theo dạng `rộng×cao+x+y`. Cắt đúng hộp đó, đặt giữa canvas trong suốt cạnh `round(cạnh dài / 0,70)`, rồi thu Lanczos về 1024. Ba cỡ nhỏ đều thu Lanczos trực tiếp từ bản 1024; PNG RGBA 8 bit. Không đổi không gian màu, không chỉnh màu, không thay alpha bằng ngưỡng mới. **Không dùng unsharp cho bất kỳ bản 64 px nào**: ở 64 px còn nhận ra hình chính; mất chi tiết ở 32 px không được giải quyết bằng làm nét bản 64.

| Nguồn | Hộp cắt alpha > 16 | Cạnh canvas trước khi thu | Cạnh dài / canvas |
| --- | --- | ---: | ---: |
| `gun-xung.png` | `1164×947+73+214` | 1663 px | 69.99399% |
| `gun-tia.png` | `1198×1052+36+86` | 1711 px | 70.01753% |
| `gun-tan.png` | `1190×965+39+144` | 1700 px | 70.00000% |
| `gun-ray.png` | `1197×1163+37+66` | 1710 px | 70.00000% |
| `gun-phao-sao.png` | `1164×1031+54+135` | 1663 px | 69.99399% |
| `nova.png` | `1156×1126+49+51` | 1651 px | 70.01817% |

Canvas nguyên pixel làm tỉ lệ 70% lệch tối đa khoảng 0,01817 điểm phần trăm trước khi thu. Không kéo giãn chiều ngắn để bù lề. Số pixel nguồn alpha > 16 nằm ngoài hộp cắt: **0 cho cả sáu ảnh**. Phần alpha ≤ 16 ngoài hộp bị bỏ theo đúng bước cắt của phiếu.

## KA1 · MD5: đạt

Chạy `md5 -r` trên mọi file trong `art-src/ui/icons/` theo danh sách đường dẫn đã sắp xếp, lưu trước khi tạo PNG và sau khi tạo đủ PNG. Trước: **20 file**; sau: **44 file**. Cả 20 hash cũ giữ nguyên; **24 file thêm, 0 file đổi, 0 file mất**. So tập tên xác nhận đúng 24 đầu ra được cho phép, không có file mới khác trong `ui/icons/`.

[MD5 trước](../../games/typing-survival/art-src/_review/108/md5-before.txt), [MD5 sau](../../games/typing-survival/art-src/_review/108/md5-after.txt), [diff](../../games/typing-survival/art-src/_review/108/md5-diff.txt). `diff` trả 1 vì có bổ sung; ngoài chỉ dẫn số dòng `a`, chỉ có 24 dòng `>` của file mới, không có dòng `<`.

## KA2 · Khổ: đạt 24/24

Mỗi icon có đúng một bản 1024 × 1024, 256 × 256, 128 × 128 và 64 × 64. Bảng KA4 ghi số đo từng file; `measurements.json` giữ toàn bộ dữ liệu.

## KA3 · Lề: 0/6 bản 1024 đạt cả bốn lề

Đếm số pixel từ mỗi mép canvas tới hộp alpha > 16. Cả sáu đạt lề trái/phải 148–160 px; cả sáu vượt 160 px ở trên/dưới.

| Icon 1024 | Trái | Trên | Phải | Dưới | Cả bốn trong 148–160 |
| --- | ---: | ---: | ---: | ---: | --- |
| `gun-xung.norm.png` | 153 | 221 | 154 | 221 | Chưa đạt |
| `gun-tia.norm.png` | 153 | 197 | 154 | 197 | Chưa đạt |
| `gun-tan.norm.png` | 153 | 221 | 154 | 222 | Chưa đạt |
| `gun-ray.norm.png` | 154 | 164 | 154 | 164 | Chưa đạt |
| `gun-phao-sao.norm.png` | 153 | 195 | 154 | 195 | Chưa đạt |
| `nova.norm.png` | 153 | 162 | 154 | 163 | Chưa đạt |

**Không thể đồng thời giữ tỉ lệ và đạt cả bốn lề theo phiếu.** Ví dụ Pulse Gun có hộp cắt 1164 × 947; khi cạnh dài bằng khoảng 717 px trong canvas 1024, cạnh ngắn còn khoảng 583 px, nên lề dọc khoảng 221 px. Hộp alpha của Rail Gun và Nova gần vuông hơn nhưng lề dọc vẫn vượt 160 px. Không cắt nội dung hay kéo giãn hình để đưa lề dọc về 15%.

Kiểm hình không bị canvas cắt: **24/24 đạt**, alpha lớn nhất trên toàn bộ bốn mép ngoài bằng **0**, hộp alpha > 16 nằm hoàn toàn bên trong canvas.

## KA4 · Alpha: cực trị đạt 24/24, chênh luma đạt 8/24

Phép đo dùng RGB thẳng, chưa ghép nền: `Y′ = (0,2126R + 0,7152G + 0,0722B) / 255` trên sRGB. `Y′ bán trong suốt` là trung bình của **mọi** pixel alpha 1–254. `Y′ đặc sát bên` là trung bình của tập pixel alpha **đúng 255** có ít nhất một pixel alpha 1–254 trong tám ô lân cận cách 1 px; mỗi pixel tham chiếu chỉ tính một lần. Δ là trị tuyệt đối chênh hai trung bình, so ngưỡng 0,08 bằng số chưa làm tròn. Không thay alpha 255 bằng 253 để làm mẫu tham chiếu dễ đạt hơn.

| File | Khổ | Alpha min–max | Y′ bán trong suốt | Y′ đặc sát bên | Δ | KA4 |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `gun-xung.norm.png` | 1024×1024 | 0–255 | 0.407401 | 0.141629 | 0.265771 | Chưa đạt |
| `gun-xung.norm.256.png` | 256×256 | 0–255 | 0.401502 | 0.369935 | 0.031567 | Đạt |
| `gun-xung.norm.128.png` | 128×128 | 0–255 | 0.387229 | 0.497018 | 0.109789 | Chưa đạt |
| `gun-xung.norm.64.png` | 64×64 | 0–255 | 0.358147 | 0.534758 | 0.176611 | Chưa đạt |
| `gun-tia.norm.png` | 1024×1024 | 0–255 | 0.441879 | 0.147207 | 0.294671 | Chưa đạt |
| `gun-tia.norm.256.png` | 256×256 | 0–255 | 0.435128 | 0.342047 | 0.093080 | Chưa đạt |
| `gun-tia.norm.128.png` | 128×128 | 0–255 | 0.434615 | 0.331295 | 0.103320 | Chưa đạt |
| `gun-tia.norm.64.png` | 64×64 | 0–255 | 0.431292 | 0.377970 | 0.053322 | Đạt |
| `gun-tan.norm.png` | 1024×1024 | 0–255 | 0.394512 | 0.066422 | 0.328090 | Chưa đạt |
| `gun-tan.norm.256.png` | 256×256 | 0–255 | 0.385532 | 0.300981 | 0.084551 | Chưa đạt |
| `gun-tan.norm.128.png` | 128×128 | 0–255 | 0.356413 | 0.433439 | 0.077026 | Đạt |
| `gun-tan.norm.64.png` | 64×64 | 0–255 | 0.330796 | 0.468656 | 0.137860 | Chưa đạt |
| `gun-ray.norm.png` | 1024×1024 | 0–255 | 0.418131 | 0.099219 | 0.318912 | Chưa đạt |
| `gun-ray.norm.256.png` | 256×256 | 0–255 | 0.409669 | 0.242964 | 0.166705 | Chưa đạt |
| `gun-ray.norm.128.png` | 128×128 | 0–255 | 0.401666 | 0.273687 | 0.127979 | Chưa đạt |
| `gun-ray.norm.64.png` | 64×64 | 0–255 | 0.386925 | 0.373014 | 0.013912 | Đạt |
| `gun-phao-sao.norm.png` | 1024×1024 | 0–255 | 0.391778 | 0.075965 | 0.315813 | Chưa đạt |
| `gun-phao-sao.norm.256.png` | 256×256 | 0–255 | 0.379373 | 0.310350 | 0.069023 | Đạt |
| `gun-phao-sao.norm.128.png` | 128×128 | 0–255 | 0.364920 | 0.402458 | 0.037538 | Đạt |
| `gun-phao-sao.norm.64.png` | 64×64 | 0–255 | 0.355335 | 0.434995 | 0.079661 | Đạt |
| `nova.norm.png` | 1024×1024 | 0–255 | 0.506380 | 0.086507 | 0.419873 | Chưa đạt |
| `nova.norm.256.png` | 256×256 | 0–255 | 0.496013 | 0.400634 | 0.095379 | Chưa đạt |
| `nova.norm.128.png` | 128×128 | 0–255 | 0.487711 | 0.490905 | 0.003194 | Đạt |
| `nova.norm.64.png` | 64×64 | 0–255 | 0.470578 | 0.557360 | 0.086782 | Chưa đạt |

Vấn đề đã có trong nguồn: phần lớn thân và vùng sáng có alpha 253, nên vẫn thuộc tập bán trong suốt theo định nghĩa của phiếu; pixel alpha 255 chỉ là số ít điểm tối. Sáu nguồn đều alpha min 0, max 255, nhưng Δ theo cùng phép đo đều vượt 0,08:

| Nguồn | Pixel alpha 253 | Pixel alpha 255 | Δ trước chuẩn hóa |
| --- | ---: | ---: | ---: |
| `gun-xung.png` | 310104 | 396 | 0.308217 |
| `gun-tia.png` | 473186 | 602 | 0.363001 |
| `gun-tan.png` | 442899 | 1590 | 0.353122 |
| `gun-ray.png` | 310748 | 985 | 0.381711 |
| `gun-phao-sao.png` | 266207 | 801 | 0.341898 |
| `nova.png` | 593725 | 292 | 0.452798 |

Phép đo này không tách riêng quầng năng lượng có chủ ý khỏi viền lỗi. Vì vậy không dùng nó để kết luận mọi điểm không đạt đều là viền sáng/tối mới. Kết quả vẫn được ghi **chưa đạt** theo phiếu; không sửa màu, nắn alpha hoặc loại quầng khỏi mẫu đo. Dữ liệu đếm pixel tham chiếu và trung bình nguồn có trong `measurements.json`.

## KA5 · Tờ xem và nhận diện

Đã mở kiểm trực tiếp [108-sheet.jpg](../../games/typing-survival/art-src/_review/108-sheet.jpg), không chạy trình duyệt. Hàng 1: sáu bản 1024 thu Lanczos về 256 trên `#0e1116`. Hàng 2: sáu cặp 64 px và 32 px trên cùng nền (32 thu từ bản 1024, không tạo file đầu ra riêng). Hàng 3: sáu cặp icon 64 px trên thẻ `#1a1f27`, mỗi cặp thử cả viền xanh và cam 1 px. Các nhãn dùng `/System/Library/Fonts/Supplemental/Arial.ttf`; JPEG 4:4:4, quality 96.

| Icon | Nhận xét ở 32 px | 64 px trên thẻ có viền |
| --- | --- | --- |
| Pulse Gun | Còn nhận ra thân súng và ba vệt xanh; chi tiết thân nhỏ. | Tách được thân và vệt xanh; không nhập vào viền. |
| Heat Beam | Quạt cam còn rất rõ; thân thép tối, ít chi tiết. | Quạt và nòng đọc rõ; cách viền cam bằng khoảng trống. |
| Scatter Gun | Khó tách/đếm đủ bảy viên; các chấm vàng và vệt sau viên tụ thành cụm. | Nhận ra quạt đạn và hai nòng; không chạm viền. |
| Rail Gun | Nhận ra đường chéo xanh, khó đọc ba tấm giáp riêng. | Ba tấm giáp dễ đọc hơn, vẫn nhỏ; không chạm viền xanh. |
| Star Mortar | Khó nhận thân cối: mảnh, tối; chủ yếu còn nét móc cam và sao. | Đọc được quỹ đạo/sao; thân cối vẫn nhỏ, không nhập viền cam. |
| Nova | Đọc như bông tuyết ngọc lam; vòng xung và kẹp thép thành chi tiết nhỏ. | Còn lõi và tám tia; cần tránh nhầm biểu tượng băng khi lắp. |

Ở hàng 3 không thấy viền sáng/tối rộng bất thường; nhận xét thị giác này không thay cho KA4. Cả sáu icon có khoảng trống rõ tới viền thẻ. Tờ xem cần được xem ở 100% để đánh giá đúng 64/32 px.

## Phần bỏ qua và việc cần chủ dự án/Claude xem

- Không sinh ảnh mới, không có prompt sinh ảnh; không dùng bản `.v1`, không ghi đè/đổi tên/xóa file cũ. Không chạy Git, dev server, trình duyệt, build hay bộ test game. Không sửa mã, tài liệu khác hoặc game khác.
- Không dùng unsharp ở 64 px; không đổi màu Pháo Sao, không sửa alpha hay kéo giãn hình vì nằm ngoài thao tác cắt/co/đệm được giao.
- Chủ dự án cần xử lý mâu thuẫn KA3: lề 15% trên trục dài có thể giữ tỉ lệ, còn cả bốn lề 15% đòi hộp hình vuông. Cần điều chỉnh tiêu chí hoặc cấp một phiếu khác nếu muốn thay hình; lượt này giữ nguyên tỉ lệ.
- Cần quyết định định nghĩa KA4 cho nguồn có phần đặc ở alpha 253 và quầng năng lượng bán trong suốt, hoặc giao một phiếu sửa alpha riêng. Lượt này giữ phép đo nguyên văn và ghi 16/24 file chưa đạt.
- Claude xem tờ ở 100%, chú ý Scatter Gun, Star Mortar, Nova và các tấm giáp Rail Gun ở 32 px. **Chưa đánh dấu cổng G2/phiếu 108 đạt** chỉ dựa vào việc đã có 24 file; báo cáo này chưa thay cho điều kiện Kiểm 1–4 của phiếu.
