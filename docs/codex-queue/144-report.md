# Phiếu 144 · Wordwoven · Chín chân dung quái

Ngày tiếp nhận và kiểm: 30/10/2026, macOS, repo cha.

**Đã xuất đủ 9 bản chọn 1024² và 27 bản thu, mỗi PNG có prompt nguồn bên cạnh. Phiếu CHƯA XONG và CHƯA NHẬN: còn hai cặp bóng trượt IoU, phép đo hue River Serpent phụ thuộc góc nguồn, và 21/27 bản Lanczos có alpha lẻ ngoài dải mép 3 px. Công cụ image_gen hết hạn mức khi gọi lượt sửa Tanuki. Không ghi các trường hợp này là đạt, không chép vào public/.**

## 1. Tiếp nhận, phạm vi và nơi giao

Khi bắt đầu, `portraits/enemies/` có mười PNG thử cùng prompt (chín try1 và Troll try2); `_review/144/` đã có script, nguồn băm và stage-1 dở dang. Không tạo lại hay nhận là đã sinh các ảnh này trong lượt tiếp nhận. Kiểm SHA-256: cả 10 PNG thử trùng nguyên byte nguồn `image_gen` còn trên máy; xem [provenance.json](../../games/typing-defense/art-src/_review/144/resume-20261030/provenance.json).

Bộ ứng viên giao: [portraits/enemies/](../../games/typing-defense/art-src/portraits/enemies/). Chọn try1 cho tám ảnh và try2 cho Troll. Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png`; cả bốn PNG đều có `.prompt.txt` trùng nguyên văn prompt của lượt được chọn. Nguồn thử và prompt cũ giữ nguyên. Các prompt try2 Tanuki/Blob chỉ là prompt sửa đã chuẩn bị, không giả tạo file ảnh hay hồ sơ sinh thành công.

Tham chiếu 115 hiện ở `ui/frames-epic/`, không phải `ui/frames/` như đường dẫn cũ của phiếu. Đã xem `portrait-ring.png`, `panel-large.v2.png`, `ui/title-epic/keyart.png`, ảnh chuẩn từng loài và ảnh chủ dự án. Hồ sơ trước đó có [references.jpg](../../games/typing-defense/art-src/_review/144/references.jpg). Lượt sửa Tanuki đính kèm đúng nguồn Tanuki, vòng chân dung, bảng 115 và keyart 113.

Chỉ thêm file trong `art-src/portraits/enemies/`, `_review/144*` và báo cáo này. Không chạy Git, build, test suite game, dev server, trình duyệt hay mạng ngoài image_gen; không đọc/ghi Tu Tiên, `.wt-*`, game khác hay tools/audio-lab. Không có âm thanh hoặc capture trình duyệt mới cần dọn.

## 2. Prompt và các lượt

Giữ khối STYLE-UI mới của Wordwoven, khối PORTRAIT theo tài liệu định dạng, phần loài và dòng nền G/M. Phần giải thích trong prompt ưu tiên mỹ thuật mới: khối vẽ có chất liệu, không viền mực cũ, không khung hay chữ trong tranh. Nguồn sinh và prompt cũ không bị sửa.

| Tên | Lượt và thay đổi prompt |
|---|---|
| `hopping-zombie` | try1: mũ trụ đen, bùa trống, áo vàng; giữ bản đã sinh. Miệng cười nhẹ hơn vẻ buồn ngủ của nguồn. |
| `zombie-leader` | try1: dùng mũ chỉ huy có hai cánh ngang, không bùa; giữ bản đã sinh. Không nâng sáng mũ để chạy theo màu nền tạm. |
| `river-serpent` | try1: đầu và cổ chữ S, vảy lam, cổ kem, sừng vàng; giữ bản đã sinh. Hai râu dài mềm hơn râu/ngà ngắn của nguồn. |
| `raccoon-dog` | try1 được chọn. Prompt try2 bổ sung đuôi trải ngang bên trái, đầu cao bên phải, khe âm rộng giữa đuôi và tai để tách bóng. Lệnh image_gen trả HTTP 429 usage_limit_reached; không có PNG try2. |
| `split-blob` | try1 được chọn. Đã soạn prompt try2 cho tay vươn chéo cao, thân hẹp lệch phải và khe chữ V rộng cạnh má. Chưa gửi do công cụ đã hết hạn mức. |
| `little-blob` | try1: con nhỏ tròn, một nếp cằm, không tay; giữ bản đã sinh. Không bóp méo vòng tròn để giảm IoU. |
| `sapling` | try1: hai lá lớn tách chữ V, thân gỗ hình giọt nước, mắt hốc; giữ bản đã sinh. |
| `troll` | try1 cắt vai ở mép; prompt try2 đã thêm COMPOSITION CORRECTION: lùi camera, đủ hai vai và đáy bán nguyệt trên nền khóa. Chọn try2 có sẵn, giữ try1 nguyên vẹn. |
| `ghost-flame` | try1: một đốm lửa lam-trắng, lõi tím nhạt, mắt và miệng rõ, thân đặc không quầng rời; giữ bản đã sinh. Mắt có chấm sáng khác mắt đen của tấm nguồn. |

Một lệnh sinh mới đã được gửi cho Tanuki; công cụ trả `http 429`, loại `usage_limit_reached`, thời gian chờ do công cụ trả tại lúc gọi là 66.816 giây. Không trả ảnh hay đường dẫn ảnh. [generation-block.json](../../games/typing-defense/art-src/_review/144/resume-20261030/generation-block.json) giữ sự kiện này. Không gọi tiếp Blob, không thử API/CLI khác và không tiêu lượt 3.

## 3. Hậu kỳ không phá tranh

Dùng bản sao công cụ `art-normalize` đã có trong `_review/144/art-normalize/`, với `ART_MAGICK=/opt/homebrew/bin/magick`, nền khóa G/M, `key-alpha --mode global --despill protect-interior --no-key-hue`; sau đó trim nền, giữ tỷ lệ, thu Lanczos vào hộp 717 px và đặt giữa canvas 1024². Không thêm mảng vẽ, không san phẳng hay đổi màu cả nhân vật. Không tăng sáng: 0%.

Sau lần thu, đóng alpha lẻ nằm trong lòng mask và ngoài dải mép 3 px về 255. Không hạ alpha, không xóa pixel tranh, RGB không đổi. Kiểm lại từ bytes PNG xác nhận RGB trước/sau bước này giống nhau cho cả chín bản. Số pixel đóng alpha: `hopping-zombie` 13, `zombie-leader` 46, `river-serpent` 63, `raccoon-dog` 329, `split-blob` 37, `little-blob` 26, `sapling` 259, `troll` 36, `ghost-flame` 23. Hồ sơ [alpha-repair.json](../../games/typing-defense/art-src/_review/144/resume-20261030/alpha-repair.json).

Ba bản thu được tính trực tiếp từ bản 1024 cuối bằng Lanczos; không làm nét 64, không sửa tiếp bản thu. Kiểm so dữ liệu RGBA của cả 27 bản thu với phép Lanczos trực tiếp: trùng. Vì giữ đúng phép thu này, các giá trị alpha 254 và tương tự ở lòng vật vẫn còn ở một số bản thu; bảng dưới không giấu lỗi này.

Mỗi ảnh có tờ «bản sinh | bản hậu kỳ» cùng khổ hiển thị 512²:
- [hopping-zombie](../../games/typing-defense/art-src/_review/144-hopping-zombie-before-after-final.jpg).
- [zombie-leader](../../games/typing-defense/art-src/_review/144-zombie-leader-before-after-final.jpg).
- [river-serpent](../../games/typing-defense/art-src/_review/144-river-serpent-before-after-final.jpg).
- [raccoon-dog](../../games/typing-defense/art-src/_review/144-raccoon-dog-before-after-final.jpg).
- [split-blob](../../games/typing-defense/art-src/_review/144-split-blob-before-after-final.jpg).
- [little-blob](../../games/typing-defense/art-src/_review/144-little-blob-before-after-final.jpg).
- [sapling](../../games/typing-defense/art-src/_review/144-sapling-before-after-final.jpg).
- [troll](../../games/typing-defense/art-src/_review/144-troll-before-after-final.jpg).
- [ghost-flame](../../games/typing-defense/art-src/_review/144-ghost-flame-before-after-final.jpg).

## 4. KA1 · Băm và KA2 · Khổ

Mốc mới trước khi viết: [md5-before.txt](../../games/typing-defense/art-src/_review/144/resume-20261030/md5-before.txt), gồm 86 file có sẵn trong đúng hai vùng đích. Mốc cũ `_review/144/md5-before.txt` được giữ nguyên. Hồ sơ của lượt tiếp nhận nằm trong thư mục con mới để không ghi đè nhật ký cũ. Sau khi giao: [md5-after.txt](../../games/typing-defense/art-src/_review/144/resume-20261030/md5-after.txt), [md5-diff.txt](../../games/typing-defense/art-src/_review/144/resume-20261030/md5-diff.txt), [md5-summary.json](../../games/typing-defense/art-src/_review/144/resume-20261030/md5-summary.json). Dùng `md5 -r` từng file; diff phải chỉ có dòng dữ liệu thêm, không đổi/xóa 86 file cũ. Chỉ loại các file `md5-*` của lượt tiếp nhận khỏi tự băm vòng; các nhật ký cũ vẫn nằm trong phạm vi kiểm.

[identify.txt](../../games/typing-defense/art-src/_review/144/resume-20261030/identify.txt) ghi nguyên kết quả `magick identify -format "%f %wx%h %[channels]\n"` cho 36 PNG. Tất cả bản gốc 1024×1024, bản thu 256×256 / 128×128 / 64×64; kênh `srgba`, colorspace sRGB. [delivery-pixels.json](../../games/typing-defense/art-src/_review/144/resume-20261030/delivery-pixels.json) có kiểm colorspace từng file.

## 5. KA3 · Alpha, nền khóa và lề

Mask vật: alpha >16. Dải mép là vành Chebyshev 3 px quanh biên mask, tính bằng dilate trừ erode. Cột alpha lẻ đếm mọi giá trị 1–254 nằm ngoài vành; ngưỡng bắt buộc là 0. Spill đếm pixel alpha>0 có hue cách khóa ≤15° và S>0,5, chia tổng pixel alpha>0. Mọi bản 1024 đều đạt alpha, spill và lề.

| Tên | Cạnh dài % | Lệch tâm x/y % | Alpha lẻ 1024 | Spill gốc % | Alpha lẻ 256 / 128 / 64 | Spill lớn nhất cả 4 khổ % |
|---|---:|---:|---:|---:|---:|---:|
| `hopping-zombie` | 70.020 | 0.000 / 0.049 | 0 | 0.03159 | 8 / 2 / 0 | 0.03159 |
| `zombie-leader` | 70.020 | 0.049 / 0.049 | 0 | 0.08405 | 14 / 7 / 1 | 0.08405 |
| `river-serpent` | 70.020 | 0.049 / 0.049 | 0 | 0.00742 | 21 / 8 / 3 | 0.00742 |
| `raccoon-dog` | 70.020 | 0.049 / 0.049 | 0 | 0.00467 | 27 / 2 / 4 | 0.01736 |
| `split-blob` | 70.020 | 0.049 / 0.049 | 0 | 0.02240 | 1 / 0 / 0 | 0.05098 |
| `little-blob` | 70.020 | 0.049 / 0.049 | 0 | 0.01245 | 4 / 0 / 0 | 0.04996 |
| `sapling` | 70.020 | 0.000 / 0.049 | 0 | 0.01835 | 27 / 15 / 4 | 0.04312 |
| `troll` | 70.020 | 0.049 / 0.049 | 0 | 0.00210 | 5 / 3 / 0 | 0.00210 |
| `ghost-flame` | 70.020 | 0.000 / 0.049 | 0 | 0.08528 | 3 / 1 / 1 | 0.08528 |

**21/27 bản thu trượt kiểm alpha nhị phân ngoài vành 3 px**, dù toàn bộ spill ≤0,2%. Không tự nới ngưỡng, không âm thầm sửa bản thu rồi vẫn nhận là phép Lanczos nguyên byte. Giữ tranh và ghi mâu thuẫn này theo ART_ACCEPTANCE §5; Claude quyết việc cho phép đóng alpha các pixel lẻ trong bản thu sau khi lọc. Các bản 1024 không có lỗi này.

## 6. KA4 · Cỡ trong game, tương phản, bóng và màu

Màu lấy từ `panel-large.v2.png` của 115: ngọc `#061e15` (ROI `394x384+394+384`, trung vị từng kênh), đá vôi chạm `#c3b49e` (ROI `200x10+490+40`). [hud-colours.json](../../games/typing-defense/art-src/_review/144/resume-20261030/hud-colours.json) ghi nguồn/ROI; không dùng màu tạm khi đã có 115. Luma là Y′ sRGB chuẩn hóa `0,2126R + 0,7152G + 0,0722B`, bình quân vật theo trọng số alpha. Mọi bản đạt ΔY′ ≥0,25 trên nền ngọc.

Tờ cuối giữ đúng kích thước raster: 1080p là 29 px (Low) / 77 px (thẻ); 720p là 24 px / 64 px, mỗi cặp trên hai nền. IoU kiểm cả 36 cặp ở 24 và 32 px, alpha>16 sau thu Lanczos, không dịch mask để tối ưu điểm.

| Tên | ΔY′ ngọc / đá vôi | IoU max 24 px · cặp | IoU max 32 px · cặp | Hue bản giao / nguồn đầu · lệch ° | Kiểm số bản 1024 |
|---|---:|---|---|---:|---|
| `hopping-zombie` | 0.3627 / 0.2544 | 0.7526 · `river-serpent` | 0.7200 · `river-serpent` | 20 / 31 · 11 | đạt |
| `zombie-leader` | 0.3131 / 0.3040 | 0.7031 · `river-serpent` | 0.7152 · `river-serpent` | 20 / 31 · 11 | đạt |
| `river-serpent` | 0.4192 / 0.1978 | 0.7526 · `hopping-zombie` | 0.7200 · `hopping-zombie` | 22 / 212 · 170 | **chưa đạt** |
| `raccoon-dog` | 0.3970 / 0.2201 | 0.8590 · `little-blob` | 0.8452 · `little-blob` | 28 / 29 · 1 | **chưa đạt** |
| `split-blob` | 0.5535 / 0.0636 | 0.8625 · `little-blob` | 0.8738 · `little-blob` | 26 / 28 · 2 | **chưa đạt** |
| `little-blob` | 0.5714 / 0.0456 | 0.8625 · `split-blob` | 0.8738 · `split-blob` | 29 / 28 · 1 | **chưa đạt** |
| `sapling` | 0.4909 / 0.1261 | 0.5880 · `hopping-zombie` | 0.5649 · `hopping-zombie` | 40 / 37 · 3 | đạt |
| `troll` | 0.4024 / 0.2147 | 0.7937 · `little-blob` | 0.7851 · `raccoon-dog` | 28 / 27 · 1 | đạt |
| `ghost-flame` | 0.6422 / 0.0251 | 0.6099 · `river-serpent` | 0.6013 · `river-serpent` | 204 / 218 · 14 | đạt |

Số liệu đầy đủ: [final-measurements.json](../../games/typing-defense/art-src/_review/144/resume-20261030/final-measurements.json), [IoU 24](../../games/typing-defense/art-src/_review/144/resume-20261030/final-iou-24.json), [IoU 32](../../games/typing-defense/art-src/_review/144/resume-20261030/final-iou-32.json). Theo phép kiểm chặt dùng nguồn đầu tiên, **5/9 bản 1024 qua mọi ngưỡng**, bốn bản còn lại được giữ để duyệt, không coi là đã đạt.

Hai cặp lỗi bóng: Raccoon Dog/Little Blob có IoU 0,8590 ở 24 px và 0,8452 ở 32 px; Split Blob/Little Blob là 0,8625 / 0,8738, vượt 0,80. Tanuki vẫn nhận bằng mặt nạ, lá, màu nâu; hai Blob phân biệt bằng tay và nếp gấp ở thẻ 64 px, nhưng mức Low 24 px chưa đủ chắc. Không cắt mất má, tay hoặc đuôi để ép bóng.

**Mâu thuẫn hue River Serpent:** trung vị hue toàn vùng vật là 22°; nguồn nhìn ngang có thân vảy lam chiếm diện tích lớn nên 212° (lệch vòng tròn 170°), trong khi nguồn chính diện có cổ kem lớn nên 35° (lệch 13°, đạt). Đây là thay đổi tỷ trọng mảng màu do crop chân dung, không phải đề nghị xoay vảy lam sang cam. Phép đo bỏ nền khóa thật của từng nguồn, S≥0,10 và V≥0,15; trung vị vòng tròn có trọng số alpha, góc làm tròn 1°. Cả hai nguồn cùng ghi trong JSON. Giữ màu vảy/kem đang đúng mẫu; không chỉnh hue để làm đẹp con số. Claude cần quyết dùng đối chứng chính diện hay phép đo theo vùng vật liệu, hoặc yêu cầu prompt khác. Hồ sơ chặt hiện vẫn ghi lỗi theo nguồn đầu.

## 7. KA5 · Tự chấm trên bản hậu kỳ

Thứ tự năm tiêu chí: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**; mỗi mục 0–2. Cột 720p chấm cả Low 24 px và thẻ 64 px, lấy yếu hơn. Mức chợ M chấm cạnh crop HUD của chủ dự án và bốn icon thật, không dùng kỹ thuật để thay thẩm mỹ. Mỗi ảnh đều có chất liệu, khối sáng và độ hoàn thiện có thể đứng cạnh bộ tham chiếu; Blob cần sửa dáng, Troll cần đọc mặt rõ hơn ở Low.

**Dùng tiếp chỉ chấm 1 cho cả chín bộ**, vì kiểm đủ các bản thu còn lỗi alpha; không chấm 2 khi còn ngưỡng số trượt. Điểm ≥8 không thay thế các chốt bắt buộc và không có nghĩa đã nhận.

| Tên | Q gốc: 5 mục = tổng | Q 720p: 5 mục = tổng | M gốc / 720p | Nhận xét trên bản giao |
|---|---|---|---:|---|
| `hopping-zombie` | 1.5/2/2/2/1 = **8.5** | 1.5/1.5/2/2/1 = **8** | 8 / 8 | Mặt, mũ, bùa và áo rõ; nét cười hơi khác nguồn. |
| `zombie-leader` | 1.5/2/2/2/1 = **8.5** | 1.5/1.5/2/2/1 = **8** | 8.5 / 8 | Hai cánh mũ riêng, vàng có chất liệu; ở 24 px chi tiết mắt giảm. |
| `river-serpent` | 2/2/2/2/1 = **9** | 2/1.5/2/2/1 = **8.5** | 8.5 / 8 | Khối vảy và cổ tốt; chênh histogram hue do tỷ lệ cổ kem, chờ Claude quyết. |
| `raccoon-dog` | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | 8.5 / 8 | Lông, mặt nạ, lá và đuôi rõ; bóng alpha chưa tách Little Blob đủ ngưỡng. |
| `split-blob` | 2/2/2/2/1 = **9** | 2/1/2/2/1 = **8** | 8.5 / 8 | Da và nếp gấp có khối; tay chưa tạo khe âm mạnh, dễ lẫn con nhỏ ở 24 px. |
| `little-blob` | 2/2/2/2/1 = **9** | 2/1/2/2/1 = **8** | 8.5 / 8 | Đúng con nhỏ tròn; chưa tách con lớn bằng bóng ở 24 px. |
| `sapling` | 2/2/2/2/1 = **9** | 2/2/2/2/1 = **9** | 8.5 / 8.5 | Hai lá, thân gỗ và mặt hốc còn đọc rõ; chất gỗ và lá hợp bộ. |
| `troll` | 2/2/2/2/1 = **9** | 2/1/2/2/1 = **8** | 8.5 / 8 | Đá, rêu, tóc và tấm khiên có chất liệu; mặt nhỏ trong vai rộng ở 24 px. |
| `ghost-flame` | 1.5/2/2/2/1 = **8.5** | 1.5/1.5/2/2/1 = **8** | 8.5 / 8 | Lửa và mặt rõ, tương phản tốt trên ngọc; nét mắt bóng khác nguồn một chút. |

Chưa có Claude chấm lại, không giả nhận là hai giám khảo đã thông qua. Các điểm sát ngưỡng M=8–8,5 cần được Claude xem ở PNG đầy đủ và đúng cỡ trong game.

## 8. Tờ xem và script chạy lại

- **[Tờ cuối 144-sheet-final.jpg](../../games/typing-defense/art-src/_review/144-sheet-final.jpg)**: hàng 1 bản gốc ở 256 px; hàng 2 cỡ 1080p trên hai nền 115; hàng 3 cỡ 720p trên hai nền; hàng 4 là bốn icon `gold.v2`, `food.v2`, `knowledge.v2`, `lives.v2` và crop HUD chủ dự án, phần hình cùng cao 160 px. Nhãn chỉ nằm trong tờ kiểm.
- [144-sheet.jpg](../../games/typing-defense/art-src/_review/144-sheet.jpg) là tờ sơ bộ trên màu tạm. Đã tạo tờ này trước khi chốt mẫu màu 115; giữ nguyên để tránh ghi đè, dùng tờ `-final` để duyệt. Đây là sai khác tên tờ so với phiếu.
- Script/hồ sơ lượt tiếp nhận: [resume-20261030/](../../games/typing-defense/art-src/_review/144/resume-20261030/). Các file cũ ở `_review/144/` và `stage-1/` giữ nguyên.

Chạy từ repo cha, dùng Python 3 chuẩn, ImageMagick 7, Arial macOS; không cần cài thư viện hay mạng. `reproduce.py` nhận một thư mục mới để chạy lại tách nền, chuẩn hóa, alpha, bản thu, phép đo và tờ xem mà không đụng bộ giao:

```sh
ART_MAGICK=/opt/homebrew/bin/magick PYTHONDONTWRITEBYTECODE=1 python3 games/typing-defense/art-src/_review/144/resume-20261030/reproduce.py --out rerun-YYYYMMDD
```

Thư mục chạy lại phải chưa tồn tại; script cố ý từ chối ghi đè. Không chạy `prepare.py` hay `register.py` cũ vì các tên đầu ra của chúng đã tồn tại. Quy trình đã dùng trong lượt này: `finish.py process`, `finalize.py prepare`, `finalize.py measure`, `finalize.py sheets`, `finalize.py publish`, `verify-delivery.py`, `report.py`, `audit-final.py`. Script tách nền cũ được gọi bằng selection mới, không sửa nội dung.

## 9. Việc còn lại và sai khác phiếu

1. Khi image_gen mở hạn mức: chạy hai prompt try2 đã chuẩn bị cho Tanuki và Split Blob, giữ tham chiếu 115/113 và nguồn model, kiểm lại đủ 36 cặp. Chưa dùng lượt 3. Lượt sửa Tanuki hiện chỉ có lỗi công cụ, không có ảnh try2.
2. Claude quyết mâu thuẫn hue River Serpent giữa ảnh ngang và ảnh chính diện; không tô đổi màu vảy chỉ để qua histogram.
3. Claude quyết cách đóng alpha lẻ sau Lanczos đối với bản thu. Hiện giao đúng phép Lanczos trực tiếp và ghi đủ số trượt; không tự nới ngưỡng hoặc ghi đè những bản đã xuất.
4. Duyệt tờ `144-sheet-final.jpg`, các cặp trước/sau `*-before-after-final.jpg` và từng PNG; chấm lại M/Q. Chỉ Claude chép ảnh vào public khi gắn sau khi nhận.

Chưa thể đóng phiếu theo điều kiện «mọi kiểm 1–5 đạt». Lý do là lỗi số đo được giữ nguyên và hạn mức sinh ảnh thực sự đã chặn lượt sửa, không phải thiếu file bàn giao. Không có sửa mã hay âm thanh ngoài phạm vi.
