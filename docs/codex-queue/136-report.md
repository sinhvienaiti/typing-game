# Phiếu 136 · Wordwoven · Nút và thẻ nhà

Ngày làm: 29/10/2026, macOS, repo cha.

**Đã giao đủ 10 ảnh, 30 bản thu và prompt; các phép kiểm số đạt theo cách xét tương phản trên ít nhất một trong hai nền được chỉ định. Tự chấm KA5 từ 9 điểm trên bản hậu kỳ. Chưa nghiệm thu: cần Claude chấm lại từ 8 điểm rồi mới chép vào `public/`.**

## 1. Nơi giao và tờ xem

- Ảnh: [ui/icons/](../../games/typing-defense/art-src/ui/icons/). Mỗi tên có `.try1.png`, `.try1.prompt.txt`, `.png`, `.prompt.txt`, `.256.png`, `.128.png`, `.64.png`; ba bản thu cũng có prompt và ghi phép thu cạnh ảnh.
- [Tờ bốn hàng bắt buộc](../../games/typing-defense/art-src/_review/136-sheet.jpg): bản gốc ở 256 px; đúng cỡ 1080p trên hai nền; đúng cỡ 720p trên hai nền; năm icon mới cạnh bốn icon có sẵn và mảnh HUD tham chiếu, cùng cao 64 px. Mỗi ô có tên.
- [Tờ cỡ 720p nguyên pixel](../../games/typing-defense/art-src/_review/136-native.jpg).
- [Tờ tổng bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/136-before-after.jpg). Mười tờ riêng, cùng cỡ 512 px mỗi bên: [final-sheets/](../../games/typing-defense/art-src/_review/136/final-sheets/), tên `<tên>.before-after.jpg`; ảnh hậu kỳ đầy đủ trên ngọc là `<tên>.full.jpg`.
- Số đo cuối: [final-check/metrics.json](../../games/typing-defense/art-src/_review/136/final-check/metrics.json). Bằng chứng khổ và thu: [files-verification-v2.json](../../games/typing-defense/art-src/_review/136/files-verification-v2.json), [identify-delivery-v2.txt](../../games/typing-defense/art-src/_review/136/identify-delivery-v2.txt).

Ảnh được tạo bằng công cụ tích hợp **`image_gen.imagegen`**, không gọi dịch vụ ngoài. Chỉ ghi vào `ui/icons/`, `_review/136*` và báo cáo này. Không sửa mã, không chạy Git, game, build, test suite hay trình duyệt; không đọc/ghi Tu Tiên hoặc `.wt-*`. Không có lượt chụp trình duyệt, không có khung hình thô cần dọn. Không tạo âm vì phiếu này chỉ yêu cầu ảnh.

## 2. Tham chiếu và prompt từng lượt

`ui/frames/` trong phiếu chưa tồn tại; ảnh 115 thực tế nằm ở **`ui/frames-epic/`**. Đã xem và đính kèm `panel-large.v2.png` của 115 cùng `ui/title-epic/keyart.png` của 113 cho mọi lượt. Đã xem HUD ảnh chủ dự án `art-src/_refs/owner-epic-2026-10-28.webp`; lấy mức hoàn thiện của chất liệu và độ rõ của icon, không chép nội dung. Pip tắt đính kèm thêm chính ảnh nguồn pip sáng.

Mỗi prompt bắt đầu bằng **STYLE-UI mới nguyên văn của AD**, tiếp đến **ICON nguyên văn §3.5**, nội dung riêng, ràng buộc giao và dòng nền M nguyên văn. Ràng buộc giao ghi rõ ưu tiên lề 15% (thay câu 80% cũ của ICON), dáng 70%, khối vật liệu hoàn thiện và mép vật thật, không thêm đường viền vẽ, khung hoặc nền huy hiệu. Không dùng STYLE storybook cũ. Toàn bộ prompt tiếng Anh ở [prompts.json](../../games/typing-defense/art-src/_review/136/prompts.json) và cạnh từng ảnh; [generation-manifest.json](../../games/typing-defense/art-src/_review/136/generation-manifest.json) ghi nguồn, công cụ và tham chiếu.

| Tên | Lượt giữ / chọn | Nội dung khóa ở lượt 1; sửa prompt ở lượt sau |
| --- | --- | --- |
| `build` | 1 / 1 | Búa đầu đá vôi trên cuộn bản vẽ ngọc, nét kiến trúc trừu tượng; búa là khối chính. Không có lượt sau. |
| `hire-villager` | 1 / 1 | Nón rộng, dấu cộng ngọc vật lý ở mép phải; không đầu người. Không có lượt sau. |
| `ultimate` | 1 / 1 | Một lông rồng trắng/vàng, ba dải lửa hổ phách chảy xuống; mép lửa gọn. Không có lượt sau. |
| `sell` | 1 / 1 | Ba đồng vàng trượt trên một bàn tay mở, khối ngang; đồng không có chữ. Không có lượt sau. |
| `upgrade` | 1 / 1 | Bậc đá vôi đi lên, chevron vàng lớn, mặt đứng bóng ngọc. Không có lượt sau. |
| `send` | 1 / 1 | Tên ngọc chéo bay khỏi bàn tay nhỏ, đầu tên lớn, không vệt tốc độ. Không có lượt sau. |
| `undo` | 1 / 1 | Mũi tên đồng cuộn hở, đầu quay trái, lòng trống. Không có lượt sau. |
| `lock` | 1 / 1 | Khóa đồng thân vuông, quai cao, lỗ khóa ngọc lớn. Không có lượt sau. |
| `level-pip-lit` | 1 / 1 | Hình thoi đứng rộng 65% chiều cao, lõi vàng sáng, ánh sáng nằm trong vật. Không có lượt sau. |
| `level-pip-unlit` | 1 / 1 | Cùng hình thoi của ảnh đính kèm; chỉ đổi thành đồng tối, bỏ tự phát sáng. Không có lượt sau. |

Tổng **10 lượt sinh**, không dùng lượt 2 hoặc 3. Không xóa hoặc sửa ảnh `.try1`. Nguồn công cụ là **1254 × 1254**; giữ nguyên byte ở `.try1.png`, chuẩn hóa bản giao về **1024 × 1024**.

## 3. Hậu kỳ giữ tranh

Sao chép nguyên trạng bốn file công cụ `normalize.py`, `seam_analysis.py`, `common.sh`, `key-alpha.sh` vào `_review/136/art-normalize/` để mọi file làm việc nằm trong phạm vi phiếu. Lệnh tách nền dùng `ART_MAGICK=/opt/homebrew/bin/magick`, nền `#FF00FF`, `--mode global --despill protect-interior --no-key-hue`.

Sau tách nền: trim alpha, thu Lanczos giữ tỷ lệ vào hộp 717 × 717, đặt giữa canvas trong suốt 1024². Không cắt phần vẽ. Chỉ chốt alpha lửng ngoài dải mép 3 px về 0 hoặc 255; giữ toàn bộ RGB ở bước này. Sau đó khử riêng phần đỏ/xanh lam dư của sắc magenta **trong dải mép 3 px**, không đổi alpha hoặc RGB bên trong vật. Không phủ mảng màu, thay vật liệu, san phẳng chi tiết, tăng nét hay chỉnh gamma/độ sáng.

| Ảnh | Pixel chốt alpha ngoài mép | Pixel khử sắc khóa ở mép | RGB trong vật bị đổi ở bước sửa mép |
| --- | ---: | ---: | ---: |
| `build` | 438 | 635 | 0 |
| `hire-villager` | 173 | 37 | 0 |
| `ultimate` | 1180 | 80 | 0 |
| `sell` | 326 | 68 | 0 |
| `upgrade` | 587 | 48 | 0 |
| `send` | 573 | 109 | 0 |
| `undo` | 396 | 90 | 0 |
| `lock` | 597 | 242 | 0 |
| `level-pip-lit` | 117 | 52 | 0 |
| `level-pip-unlit` | 136 | 329 | 0 |

Tờ đối chiếu cuối được dựng từ chính PNG giao, không lấy bản nguồn đẹp hơn để tự chấm. Các bản trung gian và nhật ký được giữ để truy vết. Ba bản thu lấy **trực tiếp** từ bản 1024 bằng Lanczos, không thu nối tiếp và không làm nét bản 64.

## 4. KA1 và khổ

Đã chạy `/sbin/md5 -r` trước khi ghi vào icon. Thư mục review 136 và báo cáo chưa tồn tại ở mốc trước. Trong `ui/icons/`: **218 file trước → 318 file sau, thêm 100; sửa 0; xóa 0**. Băm sau giao còn bao gồm toàn bộ review 136, tờ xem ở ngoài thư mục con và báo cáo. [md5-before.txt](../../games/typing-defense/art-src/_review/136/md5-before.txt), [md5-after.txt](../../games/typing-defense/art-src/_review/136/md5-after.txt), [md5.diff.txt](../../games/typing-defense/art-src/_review/136/md5.diff.txt), [md5-summary.json](../../games/typing-defense/art-src/_review/136/md5-summary.json). Phần nội dung diff chỉ có dòng thêm. Chỉ loại chính `md5-after.txt` và diff phụ thuộc vào nó khỏi tự băm.

Đã chạy `magick identify -format '%f %wx%h %[channels]\n'` cho đủ **40 PNG giao**: 10 bản **1024²**, 10 bản **256²**, 10 bản **128²**, 10 bản **64²**, tất cả **srgba**. ImageMagick 7.1.2-34 in kèm `4.0` sau `srgba`, nghĩa là số kênh; bộ kiểm đầu hiểu nhầm trường này và báo trượt. Đã sửa bộ đọc, giữ hồ sơ đầu, kiểm v2 đạt. Không sửa ảnh để xử lý lỗi bộ đọc. Đối chiếu pixel xác nhận đủ 30 bản thu trùng phép Lanczos trực tiếp; SHA-256 xác nhận đủ 10 `.try1.png` trùng nguồn công cụ và 10 bản giao trùng ứng viên đã kiểm.

## 5. Alpha, lề và dáng

Đo alpha mép quanh mặt nạ `alpha > 16`, dải Disk bán kính 3 px. Sắc khóa: hue 285–315°, S > 0,5, mẫu số là mọi pixel alpha > 0. Mặt nạ IoU thu Lanczos thẳng về 32² rồi lấy alpha > 16; không căn lại từng ảnh để cải thiện kết quả. Với pip, cột lớn nhất loại riêng pip còn lại, được xét theo ngưỡng cặp trạng thái ở dưới.

| Ảnh | Cạnh dài hộp bao / cạnh ảnh | Lệch tâm lớn nhất | Alpha lửng ngoài mép | Sắc khóa / pixel hiện | Sắc khóa % | IoU lớn nhất với vật khác | Cặp |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `build` | 70.020% | 0.049% | 0 | 11/306959 | 0.00358% | 0.6552 | `hire-villager` |
| `hire-villager` | 70.020% | 0.049% | 0 | 5/215823 | 0.00232% | 0.6875 | `sell` |
| `ultimate` | 70.020% | 0.049% | 0 | 1/219342 | 0.00046% | 0.6376 | `upgrade` |
| `sell` | 70.020% | 0.049% | 0 | 0/195830 | 0.00000% | 0.6875 | `hire-villager` |
| `upgrade` | 70.020% | 0.049% | 0 | 4/296835 | 0.00135% | 0.6376 | `ultimate` |
| `send` | 70.020% | 0.049% | 0 | 4/151292 | 0.00264% | 0.4215 | `ultimate` |
| `undo` | 70.020% | 0.049% | 0 | 1/214806 | 0.00047% | 0.4423 | `build` |
| `lock` | 70.020% | 0.049% | 0 | 15/313766 | 0.00478% | 0.5632 | `upgrade` |
| `level-pip-lit` | 70.020% | 0.049% | 0 | 0/166501 | 0.00000% | 0.5789 | `hire-villager` |
| `level-pip-unlit` | 70.020% | 0.049% | 0 | 0/166992 | 0.00000% | 0.5827 | `hire-villager` |

Tất cả đạt lề **68–72%**, tâm **≤ 2%**, alpha ngoài mép **0 pixel lửng**, sắc khóa **≤ 0,2%**, IoU vật khác **≤ 0,80**. Cặp pip có **IoU = 0.994536 ≥ 0,95**; không ép mặt nạ hai ảnh thành một bằng công cụ.

## 6. Tương phản và đọc được

Hai nền lấy từ ảnh 115 thực tế, không dùng màu tạm: `panel-large.v2.png`, trung bình RGB vùng `64x64+560+560` cho ngọc **#051e16**, vùng `80x20+360+35` cho đá vôi **#bdae99**. Luma dùng hệ số Rec.709 trên sRGB chuẩn hóa 0–1, trung bình vật có trọng số alpha; cùng một cách đo cho cả bộ và cặp pip.

| Ảnh | Cỡ 720 / 1080 | Δ luma ngọc / đá vôi tại 720 | Δ luma ngọc / đá vôi tại 1080 | Quan sát ở cỡ 720p |
| --- | --- | --- | --- | --- |
| `build` | 24 / 29 | 0.2806 / 0.3138 | 0.2795 / 0.3149 | Đọc được búa chéo và cuộn giấy; nét bản vẽ thành chất liệu. |
| `hire-villager` | 24 / 29 | 0.3691 / 0.2252 | 0.3677 / 0.2267 | Dáng nón và dấu cộng tách được; khắc nhỏ không còn đọc. |
| `ultimate` | 24 / 29 | 0.5491 / 0.0453 | 0.5492 / 0.0451 | Nhận ra lông và lửa rơi; sợi lông nhỏ nhập thành khối sáng. |
| `sell` | 16 / 20 | 0.4786 / 0.1157 | 0.4790 / 0.1154 | Nhận ra đồng trên lòng bàn tay; không phân biệt từng ngón. |
| `upgrade` | 16 / 20 | 0.4010 / 0.1934 | 0.4023 / 0.1921 | Đọc được bước đi lên và chevron; hoa văn bậc nhập lại. |
| `send` | 16 / 20 | 0.3794 / 0.2150 | 0.3786 / 0.2158 | Mũi tên chỉ hướng rõ; bàn tay thành khối phụ, không đọc từng ngón. |
| `undo` | 16 / 20 | 0.3919 / 0.2024 | 0.3924 / 0.2020 | Đầu trái, lòng hở và đường cuộn rõ. |
| `lock` | 16 / 20 | 0.2865 / 0.3079 | 0.2864 / 0.3080 | Dáng quai và thân khóa rõ; lỗ khóa giảm thành mảng ngọc nhỏ. |
| `level-pip-lit` | 8 / 10 | 0.6079 / 0.0136 | 0.6049 / 0.0105 | Điểm thoi vàng sáng rõ ở 8 px. |
| `level-pip-unlit` | 8 / 10 | 0.1935 / 0.4009 | 0.1936 / 0.4008 | Điểm thoi đồng tối phân biệt rõ với pip sáng; đọc tốt hơn trên đá vôi. |

Mỗi ảnh đạt Δ luma **≥ 0,25 trên ít nhất một trong hai nền**, ở cả hai cỡ. Pip tại 8 px: sáng **0.702478**, tắt **0.288044**, chênh **0.414434 ≥ 0,30**.

**Cách hiểu cần ghi rõ:** câu “ít nhất một trong hai nền tối” của phiếu liệt kê một nền ngọc tối và một nền đá vôi sáng. Phép kiểm ở đây xét ít nhất một trong **hai nền được liệt kê**. Pip tắt đạt trên đá vôi, không đạt 0,25 trên ngọc; không nâng sáng pip tắt để ép nó nổi như trạng thái bật. Claude cần xác nhận cách hiểu này khi chấm nhận. Các con số riêng từng nền ở bảng trên được giữ nguyên.

## 7. KA5 · Tự chấm bản hậu kỳ

So với độ hoàn thiện của HUD game thương mại trong ảnh chủ dự án. Đã xem cả mười PNG sau hậu kỳ ở 1024², tờ cỡ thật 720p và tờ bản sinh/hậu kỳ. Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” chỉ chấm 2 sau khi phép kiểm số của bản giao đạt.

| Ảnh | 1024²: năm điểm | Tổng | 720p: năm điểm | Tổng | Điểm còn hạn chế |
| --- | --- | ---: | --- | ---: |
| `build` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; đọc được búa chéo và cuộn giấy; nét bản vẽ thành chất liệu. |
| `hire-villager` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; dáng nón và dấu cộng tách được; khắc nhỏ không còn đọc. |
| `ultimate` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; nhận ra lông và lửa rơi; sợi lông nhỏ nhập thành khối sáng. |
| `sell` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; nhận ra đồng trên lòng bàn tay; không phân biệt từng ngón. |
| `upgrade` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; đọc được bước đi lên và chevron; hoa văn bậc nhập lại. |
| `send` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; mũi tên chỉ hướng rõ; bàn tay thành khối phụ, không đọc từng ngón. |
| `undo` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 2 / 2 / 2 / 2 | 10 | Còn nhiễu mép rất nhỏ khi xem bản lớn; đầu trái, lòng hở và đường cuộn rõ. |
| `lock` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 1 / 2 / 2 / 2 | 9 | Còn nhiễu mép rất nhỏ khi xem bản lớn; dáng quai và thân khóa rõ; lỗ khóa giảm thành mảng ngọc nhỏ. |
| `level-pip-lit` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 2 / 2 / 2 / 2 | 10 | Còn nhiễu mép rất nhỏ khi xem bản lớn; điểm thoi vàng sáng rõ ở 8 px. |
| `level-pip-unlit` | 2 / 2 / 2 / 2 / 1 | 9 | 2 / 2 / 2 / 2 / 2 | 10 | Còn nhiễu mép rất nhỏ khi xem bản lớn; điểm thoi đồng tối phân biệt rõ với pip sáng; đọc tốt hơn trên đá vôi. |

Giữ nguyên phần vẽ, không chấm lại trên ảnh nguồn để che hạn chế của mép hậu kỳ. **Chưa có điểm độc lập của Claude**; điểm trên là tự chấm, không phải quyết định nghiệm thu.

## 8. Script, chạy lại và việc để lại

Toàn bộ script ở [_review/136/](../../games/typing-defense/art-src/_review/136/):

- `workflow.py`: lưu nguồn, tách nền, chuẩn hóa, thu và đo; `finish-clean.py`: chốt alpha ngoài mép; `finish-edge.py`: khử sắc khóa ở mép.
- `review-delivery.py`: bảng số, IoU, tương phản, tờ cỡ thật và bản sinh/hậu kỳ; `verify-files.py`: khổ, nguồn và thu trực tiếp.
- `provenance.py`: prompt nguồn cho ảnh kiểm; `md5-audit.py`: băm và diff; `make-report.py`: báo cáo này từ số đo cuối.
- `replay.py`: chạy lại toàn bộ hậu kỳ và kiểm vào **thư mục con mới**, dùng thư viện chuẩn Python và ImageMagick, không gọi sinh ảnh và không ghi bộ icon.

Ví dụ chạy lại, từ repo cha (đổi tên đích nếu đã có):

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 python3 \
  games/typing-defense/art-src/_review/136/replay.py \
  games/typing-defense/art-src/_review/136/recheck-owner-01
```

Không sinh lại ảnh vì cả mười ảnh đã đủ nội dung và qua kiểm; chỉ dùng một lượt mỗi ảnh. Không sao chép vào `public/` hoặc gắn runtime vì đó là việc của Claude sau khi chấm nhận. Không thêm dòng vào tài liệu thay ảnh hay tài liệu khác vì ngoài phạm vi cho phép. Chủ dự án/Claude nên xem **bản cỡ thật**, nhất là `send`, `sell` ở 16 px, và xác nhận cách xét tương phản pip tắt trên hai nền nêu ở §6.

