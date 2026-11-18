# Phiếu 113 · Wordwoven · Màn tựa sử thi, ảnh chủ đạo và logo

Ngày kiểm: 29/10/2026. Thư mục làm việc: `/Users/toandx/htdocs/typing-game`.

**Trạng thái: đã kiểm đủ năm bản chọn; ba ảnh cảnh đạt kiểm kỹ thuật. Đã làm sạch bốn bản alpha/512 trong thư mục review, nhưng chưa thay các file cùng tên trong `ui/title-epic/` vì phiếu cấm ghi đè file có sẵn. Chưa đóng phiếu theo đúng đường dẫn đích; chờ xử lý bốn file này và Claude chấm lại M, Q.**

## 1. Tiếp nhận và phạm vi

Khi bắt đầu lượt này, `ui/title-epic/` đã có đủ năm ảnh `.try1.png`, năm prompt lượt 1, năm bản chọn, năm prompt bản chọn và bốn bản alpha/512. `_review/113/` cũng đã có script sinh hồ sơ, mốc MD5 trước khi thêm ảnh và các tờ kiểm. Báo cáo này trước đó chưa tồn tại.

Không sinh thêm ảnh trong lượt tiếp nhận: các bản vẽ đang có đủ mức mỹ thuật để kiểm; lỗi còn lại sửa được bằng hậu kỳ. Vì vậy không gọi lại `image_gen`, không dùng API ngoài, không tự nhận đã thực hiện năm lượt sinh trước đó. Script tiếp nhận cũ ghi nguồn ảnh từ `.codex/generated_images/...`; giữ nguyên toàn bộ ảnh và prompt đó. Không có lượt 2, 3 trong bộ nguồn hiện có. Không dùng font để thay logo vì chữ đã đúng.

Đã đọc chỉ đạo mỹ thuật 28/10, bible Wordwoven trong tài liệu đó, thang Q và README `tools/art-normalize`. Đã xem tham chiếu chủ dự án, `title-dusk.png`, Draconis, Fort, bộ mái cấp 3 và Tree Spirit. Không chạy Git, game, build, test suite, dev server hay trình duyệt; không đọc/ghi Tu Tiên, không ghi sang game khác.

## 2. Bộ ảnh và prompt

Gốc ảnh: `games/typing-defense/art-src/ui/title-epic/`. Mỗi hàng có đủ `<tên>.try1.png`, `<tên>.try1.prompt.txt`, `<tên>.png`, `<tên>.prompt.txt`. Prompt bản chọn trùng nguyên văn prompt lượt 1; hậu kỳ được ghi riêng, không giả làm prompt sinh mới.

| Tên | Khổ nguồn try1 | Khổ bản chọn | Kết quả kiểm nội dung |
| --- | --- | --- | --- |
| `title-backdrop` | 1536 × 1024 | 1536 × 1024 | Pháo đài đá trắng, mái đỏ, ruộng thành bậc khổng lồ; sông, thác, nhiều lớp karst; rùa trời mang phế tích; hai đèn gần và rồng nhỏ trên trời. Không nhà tranh. |
| `keyart` | 1536 × 1024 | 1536 × 1024 | Draconis bên phải phun lửa, Tree Spirit bên trái; tháp mái đỏ và chỉ vàng ở dưới; sông ngọc, thác, tầng núi và trời giông vỡ nắng. |
| `poster` | 1024 × 1536 | 1024 × 1536 | Cùng hai nhân vật, địa điểm, bảng màu và khoảnh khắc; dựng lại theo chiều dọc, giữ khoảng trời phía trên cho logo. |
| `logo` | 2172 × 724 | 2172 × 724 | Đúng tỉ lệ 3:1, cạnh dài vượt 1536; chữ ngọc nhạt, viền vàng/đồng, chỉ vàng đan qua chữ và nét lượn dưới. |
| `emblem` | 1254 × 1254 | 1024 × 1024 | Ấn ngọc/đồng tròn, sao mặt trời 16 tia, vòng chim và mây, rồng trắng vàng ôm viền. |

**Những phần bổ sung trong prompt lượt 1 đang lưu:**

| Ảnh | Phần riêng sau khối nguyên văn |
| --- | --- |
| `title-backdrop` | Yêu cầu 1536 × 1024, an toàn trong cắt giữa 16:9; Fort bên phải; rùa trời xa bên phải; vùng trời dịu x 25–75%; menu là khối đá râm và sương dịu ở dưới trái; đặt mặt trời ra ngoài vùng logo. |
| `keyart` | Có REF và mô tả ba ảnh đính kèm theo thứ tự Draconis, Tree Spirit, bộ mái Fort cấp 3. Khóa thân trắng, cánh lông vàng đầu cam, sừng/giáp đen viền vàng; Tree Spirit vỏ nhạt, râu gỗ, mắt hổ phách, quả vàng nâu và ngực rỗng. |
| `poster` | Có dòng dùng keyart làm ảnh tham chiếu để giữ nhân vật, nơi chốn, ánh sáng và màu; yêu cầu dựng lại 1024 × 1536, dành 22% phía trên cho trời chưa có chữ. |
| `logo` | Khóa tỉ lệ 3:1, từ chính xác chín chữ, W hoa và tám chữ thường; lề magenta rộng; từng chữ phải phân biệt được, trang trí phụ cho hình chữ. |
| `emblem` | Khóa nền magenta, khổ vuông, sao 16 tia là hình chính; cả huy hiệu có lề, hình kim loại nối liền và không có mảnh trang trí rời. |

Không sửa prompt giữa các lượt sinh trong lần này vì không sinh thêm. Các lần sửa dưới đây là hậu kỳ xác định, không tính là lượt sinh.

## 3. Hậu kỳ và khả năng chạy lại

Toàn bộ script nằm trong `games/typing-defense/art-src/_review/113/`. Công cụ ảnh là `/opt/homebrew/bin/magick`; font tờ kiểm là `/System/Library/Fonts/Supplemental/Arial.ttf` (Arial).

**Nền tựa:** bản try1 chưa đạt độ yên của vùng logo/menu. `finalize.py` cũ đã giảm tương phản cục bộ bằng hai mặt nạ chuyển tiếp mềm, giữ chi tiết tranh. Vùng logo nhân RGB với 0,56 và cộng 0,018; vùng menu nhân 0,62 và cộng 0,005 ở phần lõi mặt nạ. Lệnh đầy đủ, gồm biểu thức `-fx`, nằm trong `title-colour-command.json`. Lượt tiếp nhận giữ nguyên kết quả này.

**Khổ:** chỉ emblem cần thu. Lệnh trong `save-and-key.py`:

```sh
/opt/homebrew/bin/magick INPUT -gravity center -crop 1:1 +repage -filter Lanczos -resize '1024x1024>' -strip OUTPUT
```

Nguồn đã vuông nên không mất nội dung. Không phóng to ảnh nào. Ba ảnh cảnh và logo đúng khổ từ nguồn.

**Tách nền:** script cũ `save-and-key.py` sao chép nguyên công cụ của repo vào `_review/113/art-normalize/` để WORK của công cụ cũng nằm trong phạm vi cho phép. Không sửa `tools/art-normalize`. Lệnh đã lưu:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/113/art-normalize/key-alpha.sh INPUT OUTPUT --bg '#FF00FF' --mode global --despill protect-interior --no-key-hue
```

`finalize.py` loại thành phần alpha rời dưới 20 px theo liên thông 8 và tạo bản 512 bằng Lanczos. Đo lại cho thấy bước này còn sót hồng, Lanczos sinh vài đốm 2 px và bản emblem 512 thiếu lề trên.

**Sửa trong lượt tiếp nhận:**

1. `repair-alpha2.py` đã chạy vào tên mới: xóa các pixel mang sắc tím/hồng rộng hơn ngưỡng chốt. Số đo đạt nhưng phóng 4× thấy lỗ nhỏ ở viền. Giữ file để đối chiếu, không chọn cách này.
2. `repair-alpha3.py` chạy vào `final-alpha/`: thay RGB mang sắc khóa bằng màu sơn đục gần nhất trong bán kính Manhattan tối đa 12 px, giữ alpha. Khi lấy trung bình một số màu sơn hợp lệ, 12 px của logo lại rơi vào dải hue cấm. Bản này chưa đạt chốt 0%.
3. **Bản chọn hậu kỳ:** `repair-alpha-final.py` chạy vào `delivery-alpha/`. Giữ cách lấy màu sơn cạnh bên và alpha; thêm chốt khử bão hòa phần màu trung bình còn mang sắc khóa. Không tạo lỗ ở viền. Bản logo 512 thu theo cạnh dài 512; emblem thu xuống 488 rồi đặt giữa canvas trong suốt 512 để có lề. Dọn lại thành phần rời sau khi thu.

Số pixel được sửa RGB ở nguồn: logo 5.275, emblem 851; số pixel trung bình cần khử bão hòa thêm: logo 54, emblem 3. Ở hai bản alpha đầy đủ, **không đổi alpha và không xóa thành phần nào**. Bản 512 loại 3 đốm tổng 6 px của logo và 4 đốm tổng 12 px của emblem. Không cần màu thay thế cố định; mọi pixel tìm được sơn cạnh bên. Chi tiết trong `delivery-alpha/alpha-repair.json`.

Bốn file sạch, kèm prompt nguồn nguyên văn bên cạnh:

- `games/typing-defense/art-src/_review/113/delivery-alpha/logo.alpha.png`
- `games/typing-defense/art-src/_review/113/delivery-alpha/logo.512.png`
- `games/typing-defense/art-src/_review/113/delivery-alpha/emblem.alpha.png`
- `games/typing-defense/art-src/_review/113/delivery-alpha/emblem.512.png`

Lệnh đã chạy:

```sh
python3 games/typing-defense/art-src/_review/113/measure-resume-original.py
python3 games/typing-defense/art-src/_review/113/repair-alpha2.py
python3 games/typing-defense/art-src/_review/113/measure-corrected2.py
python3 games/typing-defense/art-src/_review/113/resume-review.py resume-check
python3 games/typing-defense/art-src/_review/113/repair-alpha3.py final-alpha
python3 games/typing-defense/art-src/_review/113/measure-final.py
python3 games/typing-defense/art-src/_review/113/final-review.py final-check
python3 games/typing-defense/art-src/_review/113/repair-alpha-final.py delivery-alpha
python3 games/typing-defense/art-src/_review/113/measure-delivery.py
python3 games/typing-defense/art-src/_review/113/delivery-review.py delivery-check
```

Script chặn ghi đè; khi dựng lại dùng tên thư mục đích mới. `repair-alpha-final.py` nhận tên thư mục mới trực tiếp trong `_review/113/`; `delivery-review.py` cũng nhận thư mục đích mới, đọc bản sạch đã chọn trong `delivery-alpha/`. Script đo dùng file JSON mới; chạy lại với tên JSON mới hoặc vào bản sao script trong thư mục review. Không chạy lại script tiếp nhận cũ lên các tên đã có.

## 4. KA1 · MD5

Mốc trước khi thêm bộ ảnh: `_review/113/md5-before.txt`, **80 file**. Mốc sau: `_review/113/md5-after.txt`, **104 file**. Từng file được băm bằng `/sbin/md5 -r`, kể cả prompt và file dưới thư mục con.

Kết quả: **thêm 24, sửa 0, xóa 0**. `md5-diff.txt` chỉ có dòng dữ liệu thêm; dòng `---`, `+++`, `@@` là đầu mục của unified diff. Mọi file từ mốc trước giữ nguyên, gồm `ui/title-dusk.png`.

Mốc tiếp nhận `_review/113/md5-resume-before.txt` đã có 104 file. Sau toàn bộ lượt sửa review, cả 104 file UI vẫn trùng byte. Đối chứng độc lập lần cuối nằm trong `delivery-check/md5-after.txt`, `delivery-check/md5-diff.txt`, `delivery-check/md5-summary.json`; trường `resume_ui_unchanged` là `true`. Lệnh băm và so theo đường dẫn được lưu trong `delivery-review.py`.

## 5. Kiểm kỹ thuật 2–8

### 5.1 Khổ, chữ và hình nhận diện

Khổ đạt như bảng mục 2. Không phóng to nguồn. Ba ảnh cảnh là nền đặc; không cần alpha.

**Chính tả logo: đạt.** Đã xem toàn từ và chín ảnh cắt nguồn phóng chính xác 4×: `letter-1.jpg` đến `letter-9.jpg`, ghép trong [logo-spelling-4x.jpg](../../games/typing-defense/art-src/_review/113/logo-spelling-4x.jpg). Mỗi ô có từ đối chiếu `Wordwoven` bằng Arial. Đọc lần lượt **W – o – r – d – w – o – v – e – n**: một W hoa, tám chữ thường, đúng chín chữ, một dòng, không chữ thừa hay lạ. Các ảnh cắt có phần nét chữ cạnh bên vì chữ và chỉ vàng đan chồng lên nhau; kiểm cả từ để xác nhận ranh giới. Bản sửa RGB không thay đổi alpha hay hình chữ ở nguồn.

**Không chữ lạc: đạt qua quan sát.** Đã xem ba ảnh cảnh và emblem ở khổ đầy đủ và bản nhỏ. Không thấy chữ, số, chữ ký hay watermark. Chỉ vàng trong keyart là đường cung và đường chéo nối tháp, không thành chữ đọc được. Các dấu tam giác/chấm trên vòng ấn là hoa văn hình học, không phải chữ hoặc số. Không dùng OCR để biến kiểm quan sát thành kết quả máy.

**Khớp model: khớp các nét chính.** [113-models.jpg](../../games/typing-defense/art-src/_review/113-models.jpg) đặt hai ảnh chuẩn cạnh crop trong keyart. Draconis giữ thân/vảy trắng vàng, sừng đen viền vàng, giáp ngực/tay/chân đen viền vàng, cánh lông vàng với đầu cam và đuôi đầu cam; thân gọn, hai tay/hai chân. Tree Spirit giữ vỏ gỗ nhạt xoắn, râu gỗ, mắt hổ phách, tán lá thành cụm, quả vàng nâu và lỗ ngực. Dáng lao tới/phun lửa và tay cây vươn ra là thay đổi tư thế theo đề. Fort giữ đá sáng, mái đỏ cam phân tầng và khung gỗ; quần thể được phóng thành pháo đài sử thi theo TITLE/KEYART, không phải bản sao hình học của keep đơn lẻ. Không thay model 3D.

### 5.2 Alpha · đo riêng bản giao đang có và bản sửa

Hue tính trên RGB sRGB chuẩn hóa; đếm mọi pixel alpha > 0, hue 285–330° và S > 0,5. Phần trăm dùng mẫu số là số pixel nhìn thấy; đồng thời tử số 0 nghĩa là 0% trên cả canvas. Bbox và lề cũng lấy alpha > 0. Thành phần rời đo liên thông 8.

**Các file đang có trong `ui/title-epic/` chưa đạt mục 5:**

| File | Pixel hue cấm | % pixel nhìn thấy | Đốm < 20 px | Lề nhỏ nhất |
| --- | ---: | ---: | ---: | ---: |
| `logo.alpha.png` | 963 | 0,188436% | 0 | 136 px |
| `logo.512.png` | 38 | 0,124472% | 3 | 30 px |
| `emblem.alpha.png` | 141 | 0,022029% | 0 | 41 px |
| `emblem.512.png` | 105 | 0,064657% | 0 | 18 px |

Đo lại thực tế ở `measurements-resume-original.json`; không dùng số của bản corrected để báo thay cho file UI.

**Bản sửa trong `delivery-alpha/`: đạt toàn bộ chốt alpha.**

| File | Khổ | Alpha min/max | Hue cấm | Đốm < 20 px | Bbox x,y,w,h | Lề trái,trên,phải,dưới |
| --- | --- | --- | --- | ---: | --- | --- |
| `logo.alpha.png` | 2172 × 724 | 0 / 255 | 0 px; 0% | 0 | 147,153,1878,435 | 147,153,147,136 |
| `logo.512.png` | 512 × 171 | 0 / 255 | 0 px; 0% | 0 | 32,34,448,107 | 32,34,32,30 |
| `emblem.alpha.png` | 1024 × 1024 | 0 / 255 | 0 px; 0% | 0 | 61,41,901,919 | 61,41,62,64 |
| `emblem.512.png` | 512 × 512 | 0 / 255 | 0 px; 0% | 0 | 38,29,435,443 | 38,29,39,40 |

Bản alpha giữ cạnh dài bằng bản chọn đã chuẩn hóa, không phóng to. Ảnh mép cuối [delivery-check/edge-4x.jpg](../../games/typing-defense/art-src/_review/113/delivery-check/edge-4x.jpg) gồm logo/emblem ở 4× trên nền tối và sáng: không thấy viền hồng, nét viền liên tục. Đã xem cả hình đầy đủ trên nền tối để kiểm vùng ngoài crop. Số đo cuối ở `measurements-delivery.json`.

### 5.3 Chỗ cho logo và menu

Cắt giữa bản 1536 × 1024 thành **1536 × 864 tại +0+80**. Luma dùng `(0,2126R + 0,7152G + 0,0722B)/255` trên RGB sRGB mã hóa, độ lệch chuẩn tổng thể. Tọa độ phần trăm làm tròn bao ra ngoài.

| Vùng | Hộp trên nguồn x,y,w,h | Std try1 | Std bản chọn | Ngưỡng | Kết quả |
| --- | --- | ---: | ---: | ---: | --- |
| Logo: x 25–75%, y 6–30% của bản cắt | 384,131,768,209 | 0,153719 | **0,086081** | ≤ 0,12 | Đạt sau hậu kỳ |
| Menu: x 3–35%, y 55–92% của bản cắt | 46,555,492,320 | 0,195891 | **0,121459** | ≤ 0,14 | Đạt sau hậu kỳ |

Mock cuối: [delivery-check/title-mock.jpg](../../games/typing-defense/art-src/_review/113/delivery-check/title-mock.jpg), logo rộng 691 px, xấp xỉ 45% canvas, ở giữa phía trên; khối menu xám rộng 462 × cao 303 px, xấp xỉ 30% × 35%, tại +46+475. Logo đọc rõ; pháo đài, rùa trời, dòng sông và các tầng núi vẫn giữ quy mô. Vùng trời đã hạ tương phản hơi tối hơn ánh nắng bên phải; đây là xử lý để đặt chữ, cần xem lại khi tích hợp UI thật.

File `title-mock-original-alpha.jpg` trong cùng thư mục dùng đúng `ui/title-epic/logo.alpha.png` đang có để đối chứng; bố cục giống nhau, nhưng alpha đó còn lỗi như bảng trên.

### 5.4 Đọc nhỏ

Đã xem [delivery-check/small-sizes.jpg](../../games/typing-defense/art-src/_review/113/delivery-check/small-sizes.jpg), với cảnh ngang 384 × 256, poster 256 × 384, logo 512 × 171 và emblem 64 × 64.

- Keyart: nhận ngay rồng trắng vàng bên phải, cây khổng lồ bên trái, tháp đá mái đỏ phía trước. Lửa là trục dẫn mắt; chi tiết lính/mũi tên nhỏ không phải điểm nhận diện chính.
- Poster: nhận rõ cùng rồng/cây/tháp ở 384 px cạnh dài; khoảng trời trên vẫn trống để ghép logo. Bàn tay cây và lửa gần nhau nên dày chi tiết hơn keyart.
- Nền tựa: pháo đài trên vách và rùa trời vẫn nhận ra; rồng nhỏ trên trời là nét phụ, giảm rõ ở 384 px.
- Logo 512: đọc được toàn từ Wordwoven, chỉ vàng không che mất cấu trúc chín chữ.
- Emblem 64: nhận ra ấn tròn ngọc vàng, mặt trời ở giữa và vòng rồng; từng con chim/mây không còn tách rõ. Đạt vai trò huy hiệu, không coi đây là hình minh họa cần đọc từng họa tiết.

## 6. KA5 · Mức chợ và điểm Q

Đây là **Codex tự chấm**, không thay kết quả Claude duyệt. M dùng ảnh tham chiếu chủ dự án làm mốc 9; logo/emblem dùng tiêu chí hoàn thiện của logo/huy hiệu game thương mại. Điểm logo và emblem dưới đây chấm **bản alpha sạch trong review**, không phải bốn file UI còn lỗi kỹ thuật.

Q theo thứ tự: đúng đề / đọc được / hợp bộ / hình khối / dùng cho bước sau; mỗi tiêu chí 0–2. Kiểm kỹ thuật bắt buộc vẫn phải đạt riêng, dù tổng Q có thể từ 8.

| Bản chọn để duyệt | M đầy đủ | Q đầy đủ (5 tiêu chí) | M ở 384 px | Q ở 384 px | Nhận xét so với mức chợ |
| --- | ---: | --- | ---: | ---: | --- |
| `title-backdrop.png` | 8,5 | 9 (2/2/2/1/2) | 8 | 9 | Đứng cạnh được: vách/pháo đài rất lớn, nhiều tầng karst và sương, thác bạc, nắng xiên. Quần thể kiến trúc khá dày và một số tầng mái khó đọc riêng. |
| `keyart.png` | 8,5 | 9 (2/1/2/2/2) | 8 | 9 | Đứng cạnh được: hai chủ thể rõ tầm vóc, khớp dáng chuẩn, nắng giông và lửa có hướng. Nửa dưới nhiều đường tên/chỉ và chi tiết nhỏ; vùng trên trái sáng hơn một ô logo lý tưởng. |
| `poster.png` | 8,5 | 9 (2/1/2/2/2) | 8 | 9 | Đứng cạnh được: bố cục dọc có độ cao, khoảng trời trên hợp thẻ game, cặp nhân vật đọc rõ. Vùng tay cây/lửa và thành lũy vẫn khá dày. |
| `delivery-alpha/logo.alpha.png` | 8,5 | 9 (2/1/2/2/2) | 8,5 ở **512 px** | 9 ở **512 px** | Ngọc, vàng, đồng hoàn thiện và đúng chữ; chỉ đan có ý nghĩa thương hiệu. Trang trí nhiều hơn một logo tối giản, cần giữ kích thước tối thiểu khi dùng. |
| `delivery-alpha/emblem.alpha.png` | 8 | 9 (2/1/2/2/2) | 8 | 9 | Vật liệu và viền rồng đủ mức thương mại. Vòng chim/mây dày; thu nhỏ đọc theo khối ấn và mặt trời. Ở **64 px: M 8, Q 8**, nhận ra huy hiệu nhưng không từng con chim. |

Ba cảnh có tiền cảnh, trung cảnh, xa và trời; tháp karst/pháo đài, Tree Spirit hoặc rùa trời làm thước đo quy mô; có bóng xanh ngọc và sáng vàng, sương phân tầng, đá/nước/lá thành khối hoàn thiện. Không lấy sự dễ chịu của `title-dusk.png` làm chuẩn đạt. Không tự chấm ngang mốc tham chiếu 9.

[Tờ so bản cuối](../../games/typing-defense/art-src/_review/113/delivery-check/vs-ref.jpg): title-mock, keyart, poster và ảnh chủ dự án cùng cao **640 px phần hình**; hàng dưới có `title-dusk.png`. Mỗi ảnh mới có một dòng «đứng cạnh được» kèm lý do. Bản cuối dùng font nhỏ vừa chiều ngang poster để tránh cắt mất lời chú thích ở tờ cũ.

## 7. Hồ sơ giao và những chỗ khác phiếu

Các tờ đúng tên yêu cầu đã có trước khi tiếp nhận và được giữ nguyên:

- `games/typing-defense/art-src/_review/113-edge.jpg`
- `games/typing-defense/art-src/_review/113-title-mock.jpg`
- `games/typing-defense/art-src/_review/113-models.jpg`
- `games/typing-defense/art-src/_review/113-vs-ref.jpg`

**Ảnh kiểm nên dùng để duyệt lần này:** `games/typing-defense/art-src/_review/113/delivery-check/` có `edge-4x.jpg`, `title-mock.jpg`, `vs-ref.jpg`, `small-sizes.jpg` và bản đầy đủ trên nền tối. Tờ models và cắt từng chữ vẫn dùng bộ cũ vì hai ảnh chủ thể và hình chữ không đổi. Không ghi đè tờ cũ bằng tờ mới.

Khác phiếu duy nhất ảnh hưởng giao nhận: **bốn bản alpha/512 sạch đang nằm trong review, chưa nằm vào bốn đường dẫn chuẩn đã tồn tại**. Hai bản `logo.png`, `emblem.png` nền magenta cùng toàn bộ try1 và prompt được giữ nguyên. Không tự thay tên, xóa hay ghi đè để ép thành «đạt».

Không sinh thêm ảnh vì mỹ thuật đạt tự chấm và lỗi là hậu kỳ. Không làm âm thanh vì phiếu chỉ có ảnh. Không tích hợp runtime, không đổi title-dusk cũ; không đụng mã, tài liệu khác, game khác hay Tu Tiên. Không có ảnh chụp trình duyệt/raw frame nên không có bước capture-prune. Không xóa các bản sửa thử trong review.

**Cần chủ dự án/Claude xem:** tờ so cuối và mock ở trên; bốn bản sạch trong `delivery-alpha/`; chấm lại M, Q. Sau đó cần giải quyết riêng việc đưa bốn bản sạch vào đường dẫn UI chuẩn vì lệnh cấm ghi đè của phiếu vẫn còn hiệu lực. Theo đúng bộ đường dẫn chuẩn hiện tại, phiếu **chưa nghiệm thu trọn vẹn**; không đánh dấu hoàn tất chỉ dựa trên điểm tự chấm của bản review.
