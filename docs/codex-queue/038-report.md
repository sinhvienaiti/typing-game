# Phiếu 038 · Rồng Giữ Ải · Ảnh VFX lô 1

Ngày 28/10/2026 · Công cụ sinh: **image_gen tích hợp** · Hậu kỳ: ImageMagick 7 và `tools/art-normalize` · **6/6 ảnh đạt tự chấm từ 8 điểm**, mỗi ảnh một lượt sinh. Không có flipbook.

## 1. Đầu ra và cách chấm

Bản chọn trong `games/dragon-hold/art-src/vfx/`: `fissure-a.png`, `fissure-b.png`, `fissure-c.png`, `scorch.png`, `smoke-strand.png`, `sweep-strip.png`. Mỗi bản có `.prompt.txt` cùng tên chứa nguyên prompt gửi image_gen và lệnh hậu kỳ. Các `.try1.png` là ứng viên lưu lại; **dùng sáu file không có `.try1`**. Riêng `smoke-strand.try1.png` là bản nối thử chưa qua kiểm, không phải bản giao.

Chuẩn: [ART_ACCEPTANCE §2.2](../games/ART_ACCEPTANCE.md), [VFX_STANDARD §3.5–§3.6 và §4.4](../games/VFX_STANDARD.md); phong cách từ mục Decal của [pine-river](../games/dragon-lane/art-requests/m0/04-2d-ground-decals-backdrop.md). Tham chiếu nhiều lớp của chuẩn: `tmp/vfx/owner-reference-layered-vfx.webp`; phiếu này chỉ giao các lớp mặt nạ, không tái tạo toàn bộ hiệu ứng tham chiếu.

Mục đích: vết nứt và vết cháy cho I/F của **Sky Fire** (loại chiêu); dải quét cho R/T của đòn quái; khói cho lớp tối sau đạn/chiêu ở T/F. Các pha A/R/T/I/F, màu phe, tuổi thọ và trần lớp sẽ do làn tích hợp kiểm trong game. Ảnh giao không mang màu phe.

Kịch bản chấm tĩnh: xem mặt nạ và bản ghép ở cỡ nguyên 512 px; xem thêm chiều rộng **128 px** (dải giữ đúng 128×32) trên `ground/pine-river/earth.png`, cả nền gốc và nền nhân 0,42. Màu nhân RGB: cam `#ff7a24` cho nứt/cháy, tím `#956eb8` cho khói/quét; có thêm một tờ 128 px nhân cam cho cả sáu ảnh. Ghép alpha thường, không bloom. Đã mở xem các tờ và từng ô nguyên cỡ.

Điểm theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Điểm là tự chấm mỹ thuật của Codex, không phải phép đo tự động hay nghiệm thu hiệu ứng trong game.

| Ảnh | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Độ phủ | Còn thiếu |
|---|---|---|---|---|---|---|
| `fissure-a` | 1 | Một tâm, sáu khe tỏa không đều; khe trắng, môi xám, ngoài đen; không sửa prompt. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 7.2895% | Môi khe hơi góc cạnh hơn nét đất; nhánh rất nhỏ tan khi thu 128 px, sáu khe chính vẫn rõ. |
| `fissure-b` | 1 | Tâm lệch trái, ba khe dài quét sang phải, tổng sáu hướng chính; không sửa prompt. | 2 / 2 / 1,5 / 2 / 2 | **9,5/10 · Đạt** | 7.7114% | Môi khe còn hơi sắc khối; phần nhánh phụ mất bớt ở 128 px. |
| `fissure-c` | 1 | Tâm nhỏ, bốn nhánh, ít nhánh phụ; không sửa prompt. Sửa bằng công cụ: crop giữa 348² rồi về 512². | 1,5 / 2 / 1,5 / 1,5 / 2 | **8,5/10 · Đạt** | 6.4880% | Tâm còn giống mảng đá vỡ đặc hơn một khe nhẹ; phóng để đủ độ phủ làm giảm chênh kích thước với A. Cần người duyệt chấm lại vì sát ngưỡng. |
| `scorch` | 1 | Nguồn sáng biểu thị mật độ muội; RGB đầu ra đảo và giảm còn 32%, alpha giữ độ sáng nguồn; không sửa prompt. | 2 / 2 / 1,5 / 1,5 / 2 | **9/10 · Đạt** | 35.3428% | Hạt tro chi tiết hơn nền đất; ở 128 px hạt nhỏ nhập thành rìa muội, lõi tối vẫn rõ. |
| `smoke-strand` | 1 | Một sợi xoắn mảnh, hai đến ba sợi con, tiếp diễn ngang; không sửa prompt. Nối mặt nạ trước khi tạo alpha. | 2 / 1,5 / 1,5 / 2 / 2 | **9/10 · Đạt** | 16.1972% | Nét khói mảnh nên tím khá chìm trên đất ở 128 px; phù hợp vai lớp phụ, cần xem sau lớp sáng khi tích hợp. |
| `sweep-strip` | 1 | Ba vệt cào, đầu rộng gần 3/4 dải, đuôi nối mảnh; không sửa prompt. Nối mặt nạ trước khi tạo alpha. | 2 / 1,5 / 1,5 / 2 / 2 | **9/10 · Đạt** | 18.5013% | Dáng quét rõ ở 128 px nhưng tím vẫn trầm; lực đòn còn phụ thuộc chuyển động lúc tích hợp. |

Không sinh lượt 2–3 vì bản hậu kỳ của cả sáu đã đạt ≥ 8. `fissure-c` trước phóng chỉ phủ 2,9102%, sau phóng đạt 6,4880%; đầu khe còn nguyên, không cắt cụt. Mọi ảnh cuối nằm trong khoảng độ phủ nên không có ngoại lệ.

`fissure-c` đạt 8,5 nên cần Claude/người duyệt chấm lại theo quy định ảnh sát ngưỡng. Không sửa `ART_REPLACE_LATER.md` vì ngoài các đường dẫn phiếu cho phép; ghi thiếu sót ngay tại bảng này để làn duyệt tiếp nhận. Không tự tạo hay gửi tin nhắn cho người khác.

## 2. Lệnh tách alpha và nối mép

Chạy từ repo gốc. Môi trường công cụ: `ART_MAGICK=/opt/homebrew/bin/magick`, `PYTHONDONTWRITEBYTECODE=1`. Đầu ra đều là file mới; không ghi đè. Prompt nguồn được giữ nguyên trong `vfx/<tên>.try1.prompt.txt` và `_review/038/<tên>.source.try1.prompt.txt`.

Đọc độ sáng sau đổi xám và đổi khổ, dùng `-level 1%,100%` để dọn lượng đen gần 0. Alpha = độ sáng đã chuẩn hóa, đen = 0. Viền kỹ thuật 4 px được ép alpha 0. Lệnh thực tế cho `fissure-a` (ba vết nứt dùng cùng công thức; kích thước dải là 512×128 và chỉ ép viền trên/dưới):

```sh
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.source.try1.png -alpha off -colorspace Gray -resize '512x512!' -level 1%,100% -depth 8 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.luminance.try1.png
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.luminance.try1.png -fx '(j<4 || j>=508 || i<4 || i>=508) ? 0 : u' /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.alpha.try1.png
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.luminance.try1.png /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/fissure-a.alpha.try1.png -alpha off -compose CopyOpacity -composite -colorspace sRGB -depth 8 PNG32:/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/vfx/fissure-a.try1.png
```

Vết cháy: RGB = 0,32 × (1 − L), alpha = L; vì vậy lõi có màu đậm và alpha cao, đúng quy cách. Lệnh thực tế:

```sh
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.source.try1.png -alpha off -colorspace Gray -resize '512x512!' -level 1%,100% -depth 8 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.luminance.try1.png
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.luminance.try1.png -fx '(j<4 || j>=508 || i<4 || i>=508) ? 0 : u' /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.alpha.try1.png
/opt/homebrew/bin/magick /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.luminance.try1.png -negate -evaluate Multiply 0.32 /Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/_review/038/scorch.alpha.try1.png -alpha off -compose CopyOpacity -composite -colorspace sRGB -depth 8 PNG32:/Users/toandx/htdocs/typing-game/games/dragon-hold/art-src/vfx/scorch.try1.png
```

Sửa miễn phí khung của `fissure-c`:

```sh
/opt/homebrew/bin/magick games/dragon-hold/art-src/vfx/fissure-c.try1.png -gravity center -crop 348x348+0+0 +repage -resize '512x512!' -channel A -fx '(i<4 || i>=508 || j<4 || j>=508) ? 0 : u' +channel PNG32:games/dragon-hold/art-src/_review/038/fissure-c.normalized.try1.png
```

Hai dải: nối **mặt nạ xám còn đặc** để đường cắt dựa vào mật độ hình; sau đó mới dùng chính độ sáng của kết quả làm alpha. Chuẩn hóa chiều rộng trước nối: khói 536 trừ overlap 24 = 512; quét 524 trừ overlap 12 = 512. Không co giãn sau nối. `-roll +0+0` là bước giữ nguyên, không dịch ảnh.

Các thử kỹ thuật trước đó được giữ trong `_review/038/`: `--keep-size` làm phép so tọa độ nguồn không còn khớp; nối ảnh đã có alpha còn gây sai biệt RGB ở vùng trộn. Đây là thử hậu kỳ cùng một lượt sinh, không phải ảnh sinh lại. Không sửa công cụ hay nới điều kiện `seam-check`. Các bản này không được chọn.

Lệnh đã dùng cho khói:

```sh
/opt/homebrew/bin/magick games/dragon-hold/art-src/_review/038/smoke-strand.alpha.try1.png -resize '536x128!' -roll +0+0 -alpha off PNG24:games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.before.png
bash tools/art-normalize/seamless.sh games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.before.png games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.opaque.png --axis x --blend 4.458955224%
/opt/homebrew/bin/magick games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.opaque.png '(' games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.opaque.png ')' -alpha off -compose CopyOpacity -composite PNG32:games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.png
bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.png games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.repeat.png --axis x --blend 4.458955224% --reference games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.before.png
```

Lệnh đã dùng cho quét:

```sh
/opt/homebrew/bin/magick games/dragon-hold/art-src/_review/038/sweep-strip.alpha.try1.png -resize '524x128!' -roll +0+0 -alpha off PNG24:games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.before.png
bash tools/art-normalize/seamless.sh games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.before.png games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.opaque.png --axis x --blend 2.270992366%
/opt/homebrew/bin/magick games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.opaque.png '(' games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.opaque.png ')' -alpha off -compose CopyOpacity -composite PNG32:games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.png
bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.png games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.repeat.png --axis x --blend 2.270992366% --reference games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.before.png
```

Sáu file được chọn bằng sao chép nguyên byte; nguồn chọn ghi trong `_review/038/selection.json`. Lệnh đầy đủ cho mỗi ảnh nằm cạnh bản chọn trong `.prompt.txt`; các script xử lý và nhật ký chỉ nằm trong `_review/038/`.

## 3. Đầu ra năm kiểm bắt buộc

### Kiểm 1 · MD5 trước/sau

Trước: thư mục `art-src/vfx/` **chưa tồn tại**, 0 file; không có file để gọi `md5 -r`. Đã lưu mốc đó tại `inventory-before.json` và `md5-before.txt` rỗng trước khi tạo thư mục.

Sau: chạy `md5 -r` cho **mọi file** trong `art-src/vfx/`, bao gồm prompt và ứng viên: **24 file mới, 0 file thay đổi, 0 file bị xóa**, `only_added: true`. Đầu ra đầy đủ:

```text
62f3ef9effc14d2f92804bf5672e3c43 games/dragon-hold/art-src/vfx/fissure-a.png
624b1b3dcaea5934f2cddbfb4a6c3e1a games/dragon-hold/art-src/vfx/fissure-a.prompt.txt
62f3ef9effc14d2f92804bf5672e3c43 games/dragon-hold/art-src/vfx/fissure-a.try1.png
7cda864106eadc89e922a8e41a604c0b games/dragon-hold/art-src/vfx/fissure-a.try1.prompt.txt
003efafd4534f8065a6c3a9ba58b513a games/dragon-hold/art-src/vfx/fissure-b.png
c687f55093da2ccb3ae38652b27415af games/dragon-hold/art-src/vfx/fissure-b.prompt.txt
003efafd4534f8065a6c3a9ba58b513a games/dragon-hold/art-src/vfx/fissure-b.try1.png
bd083920cdcf08cce484432a583c8970 games/dragon-hold/art-src/vfx/fissure-b.try1.prompt.txt
936fc86744dc80c41095c785a553ac7c games/dragon-hold/art-src/vfx/fissure-c.png
62def8bf293b801fc6216db36d9c0a13 games/dragon-hold/art-src/vfx/fissure-c.prompt.txt
4448809e3c8fa2cc08854ab48737a9a2 games/dragon-hold/art-src/vfx/fissure-c.try1.png
881d612b3381bf458a37b308bff6e4fc games/dragon-hold/art-src/vfx/fissure-c.try1.prompt.txt
6f92a8085010b96b3ba0135ef420421e games/dragon-hold/art-src/vfx/scorch.png
3d17b696aec19db28acddcac1c276563 games/dragon-hold/art-src/vfx/scorch.prompt.txt
6f92a8085010b96b3ba0135ef420421e games/dragon-hold/art-src/vfx/scorch.try1.png
646fc8f0b1a0454218756788ac5d4077 games/dragon-hold/art-src/vfx/scorch.try1.prompt.txt
415728955f1f405db0bd0b985b463214 games/dragon-hold/art-src/vfx/smoke-strand.png
e57d060aff846e544785570713fdefff games/dragon-hold/art-src/vfx/smoke-strand.prompt.txt
851872a9ff47cdf73ee2d831d0215c1d games/dragon-hold/art-src/vfx/smoke-strand.try1.png
84890475ab53f87febee456eb696b266 games/dragon-hold/art-src/vfx/smoke-strand.try1.prompt.txt
4c52ed7724860f0d99bf4139b775fbe4 games/dragon-hold/art-src/vfx/sweep-strip.png
3849148ae5588283c82f7223483cf34c games/dragon-hold/art-src/vfx/sweep-strip.prompt.txt
4c52ed7724860f0d99bf4139b775fbe4 games/dragon-hold/art-src/vfx/sweep-strip.try1.png
3fd77c6683504e6efc83b2f510fea81a games/dragon-hold/art-src/vfx/sweep-strip.try1.prompt.txt
```

Bằng chứng: `_review/038/md5-before.txt`, `md5-after.txt`, `md5-comparison.json`.

### Kiểm 2–4 · Khổ, kênh, độ xám, viền alpha và độ phủ

Lệnh nhận dạng: `/opt/homebrew/bin/magick identify -format '%w %h %[channels]' <ảnh>`. Độ bão hòa trung bình tính trên RGB toàn ảnh: `(max−min)/max`, đen tính 0. Độ phủ tính đúng số pixel có alpha > 0,1, không dùng alpha trung bình. Viền được đo trực tiếp toàn bộ 4 px, không chỉ bốn góc. Chi tiết số đo ở `_review/038/verification.json`.

| Ảnh | Đầu ra identify | Bão hòa TB | Alpha lớn nhất viền 4 px, thang 0–255 | Độ phủ | Khoảng yêu cầu | Kết quả |
|---|---|---|---|---|---|---|
| `fissure-a` | `512 512 srgba 4.0` | 0,000000 | Trên/dưới/trái/phải: 0 | 7.2895% | 6–25% | **Đạt** |
| `fissure-b` | `512 512 srgba 4.0` | 0,000000 | Trên/dưới/trái/phải: 0 | 7.7114% | 6–25% | **Đạt** |
| `fissure-c` | `512 512 srgba 4.0` | 0,000000 | Trên/dưới/trái/phải: 0 | 6.4880% | 6–25% | **Đạt** |
| `scorch` | `512 512 srgba 4.0` | 0,000000 | Trên/dưới/trái/phải: 0 | 35.3428% | 25–55% | **Đạt** |
| `smoke-strand` | `512 128 srgba 4.0` | 0,000000 | Trên/dưới: 0; ngang nối liên tục | 16.1972% | 15–45% | **Đạt** |
| `sweep-strip` | `512 128 srgba 4.0` | 0,000000 | Trên/dưới: 0; ngang nối liên tục | 18.5013% | 15–45% | **Đạt** |

Hai dải đã kiểm lại trên **chính file bản chọn**, với ảnh trước seamless làm reference:

```sh
bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/vfx/smoke-strand.png games/dragon-hold/art-src/_review/038/smoke-strand.selected.repeat.png --axis x --blend 4.458955224% --reference games/dragon-hold/art-src/_review/038/smoke-strand.mask-w536-r0.before.png
bash tools/art-normalize/seam-check.sh games/dragon-hold/art-src/vfx/sweep-strip.png games/dragon-hold/art-src/_review/038/sweep-strip.selected.repeat.png --axis x --blend 2.270992366% --reference games/dragon-hold/art-src/_review/038/sweep-strip.mask-w524-r0.before.png
```

| Dải | `pass` | Mép / đối xứng / chi tiết / sọc hàng / đối chiếu nguồn / liên tục đường cắt | MAE alpha hai cột biên, thang 0–255 |
|---|---|---|---|
| `smoke-strand` | **true** | Tất cả true | 1.851562 |
| `sweep-strip` | **true** | Tất cả true | 2.093750 |

Sai khác nhỏ giữa hai cột biên là biến thiên liên tiếp của sợi, không yêu cầu hai cột giống hệt nhau; mép qua phép đo liên tục của công cụ. JSON đầy đủ: `_review/038/smoke-strand.selected.seam-check.json`, `sweep-strip.selected.seam-check.json`; ảnh ghép lặp: `<tên>.selected.repeat.png`.

### Kiểm 5 · Tờ xem nhanh

- [038-sheet.jpg](../../games/dragon-hold/art-src/_review/038-sheet.jpg) · 3168x1124. Hàng 1: sáu ảnh xám trên ô bàn cờ. Hàng 2: nhân cam cho nứt/cháy, tím cho khói/quét trên earth; có nhãn.
- [038-sheet-dark.jpg](../../games/dragon-hold/art-src/_review/038-sheet-dark.jpg) · 3168x1124. Cùng bố cục; hàng 1 nền tối, hàng 2 đất tối.
- [128-orange.jpg](../../games/dragon-hold/art-src/_review/038/128-orange.jpg) · 1008x198. Sáu ảnh ở rộng 128 px trên đất, đều nhân cam.
- [128-faction.jpg](../../games/dragon-hold/art-src/_review/038/128-faction.jpg) · 1008x198. Sáu ảnh ở rộng 128 px trên đất, cam/tím theo vai.
- [128-dark.jpg](../../games/dragon-hold/art-src/_review/038/128-dark.jpg) · 1008x198. Sáu ảnh ở rộng 128 px trên đất tối.

Lệnh ghép, màu nhân, font Arial và đường dẫn ảnh đất nằm trong `_review/038/sheet-commands.txt`; quy trình nằm trong `make-sheets.py`. Các ô 512 px gốc cũng được giữ trong thư mục để soi nguyên cỡ.

## 4. Bàn giao và phần không làm

- Dùng sáu PNG không có hậu tố `.try1` và đọc `.prompt.txt` cạnh từng file. Giữ `scorch` là muội tối; alpha vẫn là mật độ, không đảo alpha. Nếu shader chỉ đọc alpha, lấy alpha đó làm coverage rồi tô màu muội bằng ramp.
- Chủ dự án/người duyệt nên xem `038-sheet.jpg`, `038-sheet-dark.jpg`, các tờ 128 px; chú ý tâm `fissure-c` và độ rõ của khói/quét tím. `fissure-c` cần lượt chấm độc lập vì 8,5 điểm.
- Không tích hợp runtime, không tạo WebP hay flipbook, không đo đủ năm pha/chuyển động/hiệu năng trong game: phiếu chỉ cho phép giao ảnh nguồn và cấm dev server, trình duyệt, build/test game.
- Không chạy Git, không ghi `public/assets`, `media.md5`, không chạy media push; không sửa công cụ, mã, tài liệu khác hay đụng Tu Tiên và game khác. Không tạo âm thanh nên Q6 âm thanh không phát sinh.
- Không sinh thêm khi đã đạt. Các bản nguồn và thử hậu kỳ được giữ lại; không ghi đè, đổi tên hay xóa file có sẵn.

## Claude duyệt (28/10/2026)

Xem tận mắt `_review/038-sheet.jpg`: hàng trên là mặt nạ trên nền ô bàn cờ, hàng dưới là ảnh nhân màu trên ô đất `pine-river`.

| Ảnh | Claude | Quyết định |
|---|---:|---|
| `fissure-a` | 9 | Nhận. Khe tỏa đều, mảnh dần, đọc rõ khi nhân màu lửa. |
| `fissure-b` | 8,5 | Nhận. Lệch một phía, hợp vết đòn quét. |
| `fissure-c` | 7,5 | **Không nhận.** Tâm thành bốn mảng như viên gạch vỡ, không giống điểm đòn đánh xuống. Chuẩn §4.4 chỉ cần 2–3 vết nứt, nên bỏ ảnh này; đòn nhẹ dùng `fissure-a` thu nhỏ. |
| `scorch` | 8,5 | Nhận. Lõi đậm, rìa vụn tro. |
| `smoke-strand` | 8 | Nhận. Hơi mảnh; dùng làm lớp tối sau lớp sáng thì đủ. |
| `sweep-strip` | 8,5 | Nhận. Đầu dày, đuôi mảnh, liền mép. |

Ảnh nằm ở `games/dragon-hold/art-src/vfx/` (media, không vào Git). Làn VFX dùng chúng thay mặt nạ sinh bằng mã khi đặt cạnh nhau thấy đẹp hơn, sau khi qua packager vào `public/assets` của Rồng.
