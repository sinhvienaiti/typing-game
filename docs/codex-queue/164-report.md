# Phiếu 164 · Dragonhold · Vẽ lại 10 icon kiểu cũ, đợt 2

Ngày giao: **29/10/2026**, Mac mini M4, repo cha. Dùng **image_gen tích hợp**, một lời gọi cho mỗi ảnh/lượt; không dùng API ngoài.

**Đủ 10/10 bản chọn `.v2`, 40 PNG giao, 13 nguồn sinh và toàn bộ prompt. Các kiểm 1–5 đạt theo phương pháp ghi dưới đây; KA5 tự chấm từ 8 trở lên ở cả gốc và 720p. Chờ Claude chấm độc lập ≥8 để nhận và chép vào `public/`.** Chưa gắn vào game.

## 1. Tệp giao và tham chiếu

Thư mục [icon](../../games/dragon-hold/art-src/ui/icons/): mỗi tên trong bảng dưới có `.v2.png` 1024², `.v2.256.png`, `.v2.128.png`, `.v2.64.png`; mỗi PNG giao có prompt bên cạnh. Mọi nguồn `.v2.tryN.png` và `.v2.tryN.prompt.txt` được giữ nguyên. Không có lượt 3.

Đã xem `skill-fire-breath.png`, `gold.png`, cả 10 ảnh cũ, các tờ nhận 137–139, `emblem.png`/`emblem.alpha.png` của 119 và HUD trong ảnh chủ dự án `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`. Mỗi lời gọi đính kèm đúng ảnh cũ cùng tên trước, tiếp theo ba tờ 137–139 và ảnh 119. Lấy mức hoàn thiện thương mại, không chép nội dung HUD tham chiếu.

Mỗi prompt bắt đầu bằng **nguyên văn STYLE-UI của 119 / AD Dragonhold**, tiếp theo KIND–ICON tự soạn theo yêu cầu một vật, khối lớn, nét rõ, không khung UI hoặc chữ; rồi mô tả riêng và dòng nền **M #FF00FF**. Có nguyên văn câu bắt buộc: `Keep the same object identity as the attached image. Repaint it in the new style as described.` Thẻ đá trong hai hào quang là chính đồ vật cũ, không phải khung UI thêm vào.

| Ảnh | Lượt dùng / chọn | Prompt và sửa từng lượt |
|---|---|---|
| [`skill-fire-breath`](../../games/dragon-hold/art-src/ui/icons/skill-fire-breath.v2.png) | 1 / 1 | Giữ nón lửa từ trái sang phải; lõi trắng kem, lớp lửa cam có nếp sâu, bỏ viền mực. |
| [`skill-sky-fire`](../../games/dragon-hold/art-src/ui/icons/skill-sky-fire.v2.png) | 1 / 1 | Giữ quả cầu, đuôi chéo và vòng đất vỡ; đổi đất thành granite có khe nóng, gom sáng ở quả cầu. |
| [`skill-roar`](../../games/dragon-hold/art-src/ui/icons/skill-roar.v2.png) | 1 / 1 | Giữ đầu rồng há miệng và ba cung; vảy trưởng thành, cung kem có khối nổi và mép vàng. |
| [`skill-ultimate`](../../games/dragon-hold/art-src/ui/icons/skill-ultimate.v2.png) | 1 / 1 | Giữ cột lửa thành đầu rồng và ba chóp lửa; khối sáng/tối sâu hơn, miệng và cổ tách rõ. |
| [`family-moss`](../../games/dragon-hold/art-src/ui/icons/family-moss.v2.png) | 1 / 1 | Giữ mặt nạ vỏ cây, mũ rêu lệch, hai mắt và mảng vỏ nứt; tả rêu, thớ gỗ và ánh sáng có hướng. |
| [`family-beast`](../../games/dragon-hold/art-src/ui/icons/family-beast.v2.png) | 2 / 2 | Lượt 1 giữ đầu sói ba phần tư, mắt vàng úa và vỏ trán nứt. Lượt 2 kéo dáng cao, tai dài, má gọn và mõm thuôn để thoát bóng tròn; giữ đúng con sói. |
| [`family-bug`](../../games/dragon-hold/art-src/ui/icons/family-bug.v2.png) | 1 / 1 | Giữ đầu bọ lam, hai mắt kép, ba gai và râu móc; chất chitin rõ. Hậu kỳ tăng RGB toàn ảnh 8%, không sinh lại. |
| [`aura-speed`](../../games/dragon-hold/art-src/ui/icons/aura-speed.v2.png) | 2 / 2 | Lượt 1 còn đĩa lớn. Lượt 2 yêu cầu chân chạy và ba vệt gió kéo ngang, đĩa đá nhỏ sau cổ chân; giữ đủ ba thành phần cũ. |
| [`aura-attack`](../../games/dragon-hold/art-src/ui/icons/aura-attack.v2.png) | 2 / 2 | Lượt 1 còn đĩa lớn. Lượt 2 kéo kiếm lên trên đĩa nhỏ ở chuôi, dáng dọc, lưỡi và chắn tay lớn; giữ kiếm đá vàng úa và thẻ đá tròn. |
| [`hard-scale.warm`](../../games/dragon-hold/art-src/ui/icons/hard-scale.warm.v2.png) | 1 / 1 | Giữ một vảy cam đào ấm, ba rãnh, mép kem và vòng da; chuyển sang bề mặt sừng/vảy có khối và ánh vàng ấm. |

Prompt chính xác và đường dẫn nguồn công cụ: [lượt 1](../../games/dragon-hold/art-src/_review/164/generation-record.json), [ba lượt 2](../../games/dragon-hold/art-src/_review/164/generation-record-3.json). Kiểm **13/13 nguồn khớp byte với file công cụ**, **13/13 prompt lượt sinh khớp nội dung gửi**, **10/10 prompt bản chọn khớp lượt được chọn**. Prompt các bản thu giữ nguyên prompt nguồn và thêm dòng mô tả hậu kỳ.

## 2. Hậu kỳ không phá tranh

`process.py` dùng `tools/art-normalize/normalize.py` ở chế độ `global`, nền M, `protect-interior`, **không bật `no-key-hue`**. WORK chuyển vào `_review/164/scratch/`; tắt bytecode Python. Tách nền trước, lấy bbox alpha >16 cùng dải dư 3 px, giữ tỉ lệ bằng Lanczos trong ô 720², căn giữa trên canvas RGBA 1024². Cạnh vật thực tế 70,020–70,117%. Không xóa thành phần rời, không san phẳng, không phủ màu và không sửa dáng bằng mã.

Chỉ `family-bug` tăng đồng loạt RGB bằng **Multiply 1,08**, trong giới hạn ±10% của ART_ACCEPTANCE §5; alpha master không đổi. [Hồ sơ tăng sáng](../../games/dragon-hold/art-src/_review/164/family-bug-brightness.json) và bản candidate trước tăng sáng được giữ. Các ảnh khác giữ RGB sáng 1,00. Sắc khóa còn lại đều dưới ngưỡng 0,2%, nên không ép sửa màu vào phần tranh để lấy số 0.

Ba bản thu lấy **trực tiếp từ master 1024 bằng Lanczos**, không thu nối tiếp, không làm nét 64. Sau nội suy chỉ dọn ringing alpha: dải mép 3 px quanh alpha >127 được giữ antialias; ngoài dải đưa về 0 hoặc 255; RGB của pixel còn nhìn thấy không được sửa ở bước này. Có ghi số pixel alpha sửa cho từng kích thước trong các `*.post.json` và hồ sơ tăng sáng. Giữ cả các candidate chưa chọn của lượt 1.

Mỗi ảnh có tờ “bản sinh | bản hậu kỳ”, hai ô cùng cỡ, không kéo méo tỉ lệ. Chênh cỡ vật là căn lề giao 70%; nguồn sinh được giữ nguyên:

- [skill-fire-breath](../../games/dragon-hold/art-src/_review/164-skill-fire-breath-before-after.jpg).
- [skill-sky-fire](../../games/dragon-hold/art-src/_review/164-skill-sky-fire-before-after.jpg).
- [skill-roar](../../games/dragon-hold/art-src/_review/164-skill-roar-before-after.jpg).
- [skill-ultimate](../../games/dragon-hold/art-src/_review/164-skill-ultimate-before-after.jpg).
- [family-moss](../../games/dragon-hold/art-src/_review/164-family-moss-before-after.jpg).
- [family-beast](../../games/dragon-hold/art-src/_review/164-family-beast-before-after.jpg).
- [family-bug](../../games/dragon-hold/art-src/_review/164-family-bug-before-after.jpg).
- [aura-speed](../../games/dragon-hold/art-src/_review/164-aura-speed-before-after.jpg).
- [aura-attack](../../games/dragon-hold/art-src/_review/164-aura-attack-before-after.jpg).
- [hard-scale.warm](../../games/dragon-hold/art-src/_review/164-hard-scale.warm-before-after.jpg).

Đã xem riêng cả 10 PNG hậu kỳ 1024², 10 tờ trước/sau, tờ cũ–mới, tờ hợp bộ và cỡ 720p. Phần lửa, rêu, tai, râu, vòng da và ba vệt gió vẫn có sau tách nền/căn lề. Không có mâu thuẫn ngưỡng số cần phá tranh để giải quyết; chỗ trùng dáng đã sửa bằng prompt lượt 2.

## 3. KA1 và khổ

KA1 dùng `md5 -r` đệ quy toàn bộ thư mục icon: **685 → 791 tệp; 106 thêm / 0 đổi / 0 mất**. Trước phiên chưa có tên `.v2` của 10 icon hoặc `_review/164*`. Diff chỉ có dòng thêm dữ liệu, ngoài tiêu đề/hunk của unified diff. [106 tệp thêm](../../games/dragon-hold/art-src/_review/164/ka1-after.json), [trước](../../games/dragon-hold/art-src/_review/164/md5-before.txt), [sau](../../games/dragon-hold/art-src/_review/164/md5-after.txt), [diff](../../games/dragon-hold/art-src/_review/164/md5-diff-after.txt). Không ghi đè ảnh cũ hay tệp `.try`.

Lệnh khổ bắt buộc đã chạy: `magick identify -format '%f %wx%h %[channels]\n'` cho **40/40 PNG giao**. [Kết quả đầy đủ](../../games/dragon-hold/art-src/_review/164/identify.txt): 10 ảnh 1024×1024, 10 ảnh 256×256, 10 ảnh 128×128, 10 ảnh 64×64; tất cả **`srgba 4.0`**, 8 bit, sRGB + alpha. [Kiểm độc lập tệp giao](../../games/dragon-hold/art-src/_review/164/verification-final-v2.json) xác nhận **40/40** đúng khổ/kênh và khớp pixel candidate; **30/30** bản thu khớp Lanczos trực tiếp + đúng bước dọn alpha, không có sharpen.

## 4. Số đo alpha, lề, tương phản và dáng

[Số đo trên tệp giao](../../games/dragon-hold/art-src/_review/164/metrics-delivery.json), gồm từng file ở cả bốn kích thước và đủ **45 cặp IoU**.

- Bbox: alpha >16; lệch tâm là trị lớn nhất giữa hai trục, tính theo cạnh 1024.
- Alpha: ngoài dải giãn/co **Disk:3** quanh alpha >127, pixel chỉ có alpha 0 hoặc 255. Sắc khóa M: hue cách 300° ≤15°, S >0,5, alpha >0; mẫu số là tổng pixel alpha >0. Bảng lấy giá trị xấu nhất của bốn file giao mỗi ảnh.
- Luma: Rec.709 trên kênh sRGB mã hóa, `Y=(0,2126R+0,7152G+0,0722B)/255`. Trung bình màu vật có trọng số alpha ở đúng kích thước rồi so với nền; đây là cách đo vật–nền của các phiếu 137–139. Ngưỡng giữ nguyên **0,25** trên nền vỏ cây #2b2118; nền kem #f1e3c4 cũng được đo và ghép để xem.
- `metrics-initial.json` từng dùng thêm trung bình **sau ghép** trên footprint alpha >16 làm điều kiện thử nghiệm. Đây là đại lượng khác vì trộn thêm màu nền vào pixel mép. Hồ sơ cuối giữ cả `object_delta` và `composited_delta`, nhưng chốt theo **trung bình màu vật–nền** như định nghĩa trên. Không dùng số sau ghép để thay số vật–nền trong bảng, không thay ngưỡng hoặc sửa gamma để che khác biệt. Chẳng hạn đầu bọ sau ghép ở 22 px còn khoảng 0,207, dù vật–nền đạt 0,262; Claude có thể xem cả hai và cỡ thật.
- IoU: thu Lanczos từ master về đúng 32², mặt nạ alpha >16, không dịch, xoay hoặc co riêng để giảm trùng. Phiếu này không có cặp sáng/tắt.

| Ảnh | Cỡ 720/1080 px | Cạnh bbox % | Lệch tâm % | Alpha lẻ ngoài mép (px) | Sắc khóa % | Δ vỏ cây 720/1080 | Δ kem 720/1080 |
|---|---|---:|---:|---:|---:|---|---|
| `skill-fire-breath` | 21/31 | 70.117 | 0.049 | 0 | 0.0191 | 0.4515 / 0.4520 | 0.3064 / 0.3059 |
| `skill-sky-fire` | 21/31 | 70.020 | 0.049 | 0 | 0.0389 | 0.4104 / 0.4121 | 0.3475 / 0.3458 |
| `skill-roar` | 21/31 | 70.117 | 0.000 | 0 | 0.0803 | 0.3216 / 0.3184 | 0.4363 / 0.4395 |
| `skill-ultimate` | 21/31 | 70.117 | 0.049 | 0 | 0.0447 | 0.4021 / 0.4039 | 0.3558 / 0.3540 |
| `family-moss` | 22/34 | 70.020 | 0.049 | 0 | 0.0560 | 0.2812 / 0.2814 | 0.4767 / 0.4765 |
| `family-beast` | 22/34 | 70.117 | 0.049 | 0 | 0.0596 | 0.3139 / 0.3157 | 0.4440 / 0.4422 |
| `family-bug` | 22/34 | 70.020 | 0.098 | 0 | 0.1059 | 0.2617 / 0.2628 | 0.4962 / 0.4951 |
| `aura-speed` | 18/22 | 70.117 | 0.000 | 0 | 0.1730 | 0.4582 / 0.4573 | 0.2997 / 0.3006 |
| `aura-attack` | 18/22 | 70.020 | 0.049 | 0 | 0.1217 | 0.4379 / 0.4387 | 0.3200 / 0.3192 |
| `hard-scale.warm` | 32/48 | 70.117 | 0.000 | 0 | 0.0233 | 0.3864 / 0.3863 | 0.3715 / 0.3716 |

Cỡ bốn kỹ năng lấy từ DH-21/22/25: 21/31; ba họ quái từ DH-30: 22/34; vảy từ DH-37: 32/48. Phiếu R2 không có bảng riêng cho hào quang; dùng **18/22** theo nhóm icon thẻ DH-47 làm giả định kiểm, không nhận là phép đo runtime. Kiểm bổ sung `skill-roar` 18/22 và `hard-scale.warm` 16/24 đều qua luma. Ảnh được thu cả canvas gồm lề, không phóng riêng vật ở các cỡ này.

| Ảnh | IoU lớn nhất | Cặp gần nhất |
|---|---:|---|
| `skill-fire-breath` | 0.6410 | `family-moss` |
| `skill-sky-fire` | 0.6223 | `skill-ultimate` |
| `skill-roar` | 0.5947 | `family-bug` |
| `skill-ultimate` | 0.7534 | `family-moss` |
| `family-moss` | 0.7618 | `hard-scale.warm` |
| `family-beast` | 0.7329 | `hard-scale.warm` |
| `family-bug` | 0.7417 | `hard-scale.warm` |
| `aura-speed` | 0.5065 | `skill-fire-breath` |
| `aura-attack` | 0.5914 | `family-beast` |
| `hard-scale.warm` | 0.7618 | `family-moss` |

IoU cao nhất toàn bộ **0,761773 ≤0,80**. Lượt 1 có bảy cặp vượt 0,80, cao nhất 0,835196; đã giữ lại nguồn/candidate và sửa ba prompt sói, tốc, đòn. Không cắt khuyết hoặc dịch mặt nạ để qua chốt.

## 5. Tờ xem và KA5 trên bản hậu kỳ

- [Tờ bốn hàng](../../games/dragon-hold/art-src/_review/164-sheet.jpg): master thu 256; đúng cỡ 1080p trên vỏ cây/kem; đúng cỡ 720p trên hai nền; bốn icon có sẵn, mảnh HUD chủ dự án và huy hiệu 119 ở cùng khổ hiển thị.
- [Cũ–mới, hai hàng 64 và 32 px](../../games/dragon-hold/art-src/_review/164-old-new.jpg). Chỉ để so công bằng: ảnh cũ được tách nền trong hồ sơ và căn vật về cùng lề 70%; không sửa file cũ.
- [Mỗi icon mới cạnh bốn icon đã nhận](../../games/dragon-hold/art-src/_review/164-set-match.jpg): `wave-horn` (137), `check`/`speaker` (138), `lane-bridge` (139), cùng khổ 192.
- [Cỡ 720p thật và phóng nearest 4×](../../games/dragon-hold/art-src/_review/164/native-final-v2.jpg). Phóng chỉ giúp soi cấu trúc, không dùng làm cỡ chấm. Tờ `native-final` đầu được giữ trong hồ sơ; bản v2 sửa bố trí nhãn/nền tờ, không đổi PNG giao.

Tự chấm theo mức UI game thương mại / HUD chủ dự án, **không lấy bộ cũ làm chuẩn điểm**. Khối ánh sáng và vật liệu đứng cạnh được bộ 137–139; mức chợ M ở gốc khoảng 8,5, chưa tự chấm ngang mẫu 9. Ở 720p nhiều chi tiết chỉ còn khối, vì vậy hạ điểm đọc/hình khối; không suy điểm cỡ nhỏ từ tranh lớn.

Thứ tự năm điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” chỉ là 2 sau khi đủ kiểm số. M là điểm mức chợ bổ sung, Q là tổng KA5.

| Ảnh | Năm điểm gốc | Q gốc | Năm điểm 720p | Q 720p | M gốc / 720p |
|---|---|---:|---|---:|---|
| `skill-fire-breath` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 1,5 / 2 | 9 | 8,5 / 8,5 |
| `skill-sky-fire` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `skill-roar` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `skill-ultimate` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `family-moss` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `family-beast` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `family-bug` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `aura-speed` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1 / 1,5 / 1,5 / 2 | 8 | 8,5 / 8 |
| `aura-attack` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8,5 / 8 |
| `hard-scale.warm` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 8,5 / 8,5 |

**Cần Claude/chủ dự án nhìn kỹ:** `aura-speed` ở 18 px là dáng chuyển động ngang rất nhỏ, ba vệt nhập bớt; “Đọc được” chỉ 1 và Q sát ngưỡng 8. `skill-roar` ở 21 px còn đầu rồng và nhịp cung, nhưng không thấy hoa văn; `family-moss` ở 22 px còn mũ rêu/mặt gỗ, mắt không nổi bằng ảnh lớn. Đầu bọ có luma gần ngưỡng hơn phần còn lại. Ở 32–64 px cả 10 dáng nhận diện được; chân chạy và kiếm hiện đã phân biệt bằng dáng, không chỉ bằng màu đỏ–lục. Đây là tự chấm, chưa có điểm nhận độc lập của Claude.

## 6. Tái lập, phần khác phiếu và phần bỏ qua

Script đã dùng lưu ngay trong [_review/164/](../../games/dragon-hold/art-src/_review/164/): `process.py`, `sheets.py`, `verify.py`, `make-report.py`, `handoff.py`; kế hoạch và nhật ký giữ prompt chính xác. Mọi writer từ chối ghi đè. `ART_MAGICK=/opt/homebrew/bin/magick`; font Arial `/System/Library/Fonts/Supplemental/Arial.ttf`. Không sửa công cụ normalize.

[Kiểm chốt bàn giao](../../games/dragon-hold/art-src/_review/164/handoff-final.json): đủ 791 tệp icon vẫn khớp MD5 sau giao, 0 tệp cũ đổi/mất, 0 liên kết báo cáo bị thiếu; đủ 40 PNG giao, 13 nguồn sinh và 10 tờ trước/sau. Tờ cỡ thật v2 đã sửa nhãn/nền và được xem lại.

Kiểm lại bằng nhãn hồ sơ **mới**:

```bash
python3 -B games/dragon-hold/art-src/_review/164/verify.py owner-check-1
python3 -B games/dragon-hold/art-src/_review/164/process.py measure owner-check-1 published
```

Tái lập từ `.try` đã lưu vào thư mục con mới, không gọi tạo ảnh, không đụng file giao:

```bash
python3 -B games/dragon-hold/art-src/_review/164/process.py replay owner-replay-1
```

Lệnh replay có bước tăng sáng 8% của đầu bọ và so RGBA đủ 40 file; đây là đường chạy lại được cung cấp, chưa chạy lại toàn lô thêm một lần vì các kiểm direct-Lanczos và khớp candidate đã đạt.

Khác chi tiết phiếu:

- Nguồn công cụ thường 1254²; riêng `aura-speed.try2` là **1774×887**. Giữ nguyên `.try`, chỉ master giao mới là 1024²; fit giữ tỉ lệ, không kéo méo hoặc cắt phần vẽ.
- Không có nguyên văn KIND ICON riêng trong R2, nên soạn theo ràng buộc phiếu; STYLE-UI vẫn nguyên văn. Nền chọn M cho cả bộ, tránh xanh vàng trong quái/hào quang.
- Lượt 2 đổi tỷ lệ và đĩa đỡ của ba icon để có dáng riêng, giữ đồ vật nhận diện. Không dùng công cụ làm khuyết đĩa của lượt 1.
- Các bản thu có bước dọn alpha sau Lanczos để cùng đạt alpha sạch; bước này được ghi rõ, không gọi là Lanczos nguyên byte và không làm nét.
- Cỡ hào quang là giả định nêu ở mục 4 vì phiếu không cung cấp cỡ riêng; tờ so cũ–mới 32/64 vẫn đầy đủ. Nên kiểm lại cỡ cuối khi Claude gắn.

**Không bỏ ảnh nào.** Không làm âm thanh vì phiếu chỉ giao icon. Không chạy Git, build/test game, dev server hoặc trình duyệt. Chỉ thêm icon `.v2*`, hồ sơ `_review/164*` và báo cáo này; không ghi vào game khác, mã game, `public/`, tài liệu khác hoặc khu vực đang tạm dừng. Phần chấm nhận và tích hợp `public/` thuộc Claude theo phiếu.
