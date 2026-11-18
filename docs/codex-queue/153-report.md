# Phiếu 153 · Last Line · Mảnh UI nhỏ · Đã giao, chờ Claude chấm nhận

Ngày **31/10/2026**, Codex. Đã tiếp tục từ báo cáo và bảy prompt cũ: **đủ 7/7 ảnh gốc, 21/21 bản thu**, prompt và lượt sinh được giữ đầy đủ. Công cụ tích hợp `image_gen.imagegen` hoạt động trở lại; mỗi ảnh chỉ cần **một lượt sinh có PNG**, không có lượt 2 hoặc 3. Các lần HTTP 429 trước được giữ trong hồ sơ, không tính thành một lượt ảnh.

**Kiểm 1–5 đạt. KA5 trên bản hậu kỳ: gốc 9,5/10; cỡ 720p từ 8,5 đến 9,5/10.** Đây là tự chấm so với mức hoàn thiện của UI game thương mại, chưa phải kết luận nhận của Claude. Chưa chép vào `public/`.

## Bản giao và căn cứ

Thư mục `games/typing-survival/art-src/ui/parts/` có đủ `keycap`, `keycap-active`, `led-on`, `led-off`, `mag-empty`, `mag-full`, `arrow`. Mỗi tên có:

- `.try1.png` và `.try1.prompt.txt`: bản sinh nguyên trạng và prompt đã gọi;
- `.png` và `.prompt.txt`: bản chọn sau hậu kỳ 1024 × 1024;
- `.256.png`, `.128.png`, `.64.png`: Lanczos trực tiếp từ bản 1024, mỗi bản có sidecar prompt tương ứng. Không làm nét bản 64.

Đã đọc AD §4.3, ART_ACCEPTANCE §2.2 và §5, định dạng 015, UI_IMAGERY và UIC-LL-5. Đã xem icon `gun-xung.norm.256.png`, khung 127, nền chọn 121 và ảnh tham chiếu chủ dự án. Hướng **B · Lightbearer** theo quyết định 29/10; không coi việc dùng tham chiếu 121/127 là một lần nhận thay cho Claude.

[Tờ xem chính, bốn hàng](../../games/typing-survival/art-src/_review/153-sheet.jpg); [tờ phụ cỡ thật và phóng nearest 4×](../../games/typing-survival/art-src/_review/153/ui-detail.jpg). Tờ chính gồm bản 256; cỡ 1080p trên hai nền; cỡ 720p trên hai nền; bốn icon hiện có cạnh mảnh HUD của chủ dự án, cùng khung 127 và nền 121.

## Prompt và lượt sinh

Mỗi prompt cũ mở bằng STYLE-UI nguyên văn của AD, rồi KIND PART, mô tả riêng và dòng nền alpha. Không sửa prompt trong lượt tiếp tục này; không tăng số lượt khi công cụ chưa trả ảnh. Ba cặp trạng thái dùng ảnh gốc làm đích chỉnh trong `referenced_image_paths`, sau khi đã xem ảnh đó.

| Ảnh | Lượt 1 và nội dung riêng | Lượt sửa prompt |
|---|---|---|
| `keycap` | Phím giáp mặt kính khói trống, bevel vàng trắng, hai góc có chỉ mảnh; rãnh lam tắt. | Không; chọn try1. |
| `keycap-active` | Chỉnh từ keycap: bật rãnh viền lam, giữ mặt trống, vỏ và dáng. | Không; chọn try1. |
| `led-on` | Chỉnh từ led-off: kính đèn lam sáng, lõi sáng nằm trong vỏ. | Không; chọn try1. |
| `led-off` | Đèn tròn tắt, kính xanh xám, vòng kim loại vàng trắng. | Không; chọn try1. |
| `mag-empty` | Ô đạn dọc hẹp, cửa kính rỗng tối, hai đầu và cạnh kim loại. | Không; chọn try1. |
| `mag-full` | Chỉnh từ mag-empty: cửa kính có năng lượng trắng lam, giữ vỏ và dáng. | Không; chọn try1. |
| `arrow` | Chevron liền khối hướng phải, hai nhánh rộng, mặt vàng trắng và rãnh lam. | Không; chọn try1. |

[Chỉ mục công cụ, đầu vào và đường dẫn bản sinh](../../games/typing-survival/art-src/_review/153/resume-20261031/generation-index.json). Các tên và chữ UI do game đặt khi tích hợp; bitmap không có chữ, số, logo hay khung ngoài độc lập.

## Hậu kỳ không phá tranh

Công cụ trả bảy bản **1254² sRGBA**, dù prompt xin 1024². Giữ nguyên `.try1.png`; bản giao được cắt lề alpha, đổi cỡ Lanczos và đặt lại trên canvas 1024². Không kéo méo. Alpha bản sinh có nhiễu ở vùng vốn đục (phổ biến 252–253/255): chốt vùng trong thân về 255 và vùng ngoài dải mép về 0, giữ antialias trong dải 3 px. Không tô, xóa hay thay phần vẽ RGB khi làm alpha.

Ứng viên hậu kỳ đầu đo chênh luma ô đạn ở 10 px là **0,279084**, chưa đạt 0,30. Bản chọn tăng sáng **toàn ảnh `mag-full` 6%** bằng phép nhân RGB 1,06; các ảnh khác giữ độ sáng. Đây là chỉnh sáng nhẹ trong giới hạn ±10% của §5. Đã xem tờ so: cửa năng lượng, vân, vát cạnh và vỏ vẫn nguyên. Chênh luma sau chỉnh **0,302188**. Không có ngưỡng nào buộc xóa hoặc phủ tranh; không cần sinh lại.

Mỗi ảnh có tờ cùng khổ “bản sinh | bản hậu kỳ”, ở `_review/153/<tên>-before-after.jpg`. Bản sinh và bản hậu kỳ được đặt trên cùng nền than chì; thay đổi tỷ lệ vật là kết quả sửa lề, không phải cắt bỏ vỏ.

 | Ảnh | Tờ đối chiếu |
|---|---|
| `keycap` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/keycap-before-after.jpg) |
| `keycap-active` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/keycap-active-before-after.jpg) |
| `led-on` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/led-on-before-after.jpg) |
| `led-off` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/led-off-before-after.jpg) |
| `mag-empty` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/mag-empty-before-after.jpg) |
| `mag-full` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/mag-full-before-after.jpg) |
| `arrow` | [bản sinh ∣ bản hậu kỳ](../../games/typing-survival/art-src/_review/153/arrow-before-after.jpg) |

## Kiểm số

### KA1 · Giữ nguyên file có sẵn

Chụp bằng `/sbin/md5 -r` trước lần ghi đầu của lượt này; chạy lại sau giao rồi dùng `/usr/bin/diff -u`: **21 file trước, 211 file sau; 190 thêm, 0 đổi nội dung, 0 mất; 0 dòng nội dung bị trừ trong diff**. Phạm vi là `ui/parts/`, `_review/153/` và tờ `_review/153-*.jpg` (không có tờ dạng này ở baseline). Ba file kết quả audit được tạo sau thời điểm lấy danh sách; báo cáo nằm ngoài phạm vi snapshot. Snapshot cũ của ngày 30/10 không bị ghi đè.

[MD5 trước](../../games/typing-survival/art-src/_review/153/resume-20261031/md5-before.txt) · [MD5 sau](../../games/typing-survival/art-src/_review/153/resume-20261031/md5-after.txt) · [diff](../../games/typing-survival/art-src/_review/153/resume-20261031/md5-diff.txt) · [tổng hợp](../../games/typing-survival/art-src/_review/153/resume-20261031/md5-summary.json)

### Khổ, alpha, lề

`magick identify -format '%f %wx%h %[channels]\n'` kiểm đủ **28/28**: bảy bản 1024² và mỗi nhóm bảy bản 256², 128², 64², tất cả **srgba**. Kiểm lại pixel chứng minh 21/21 bản thu bằng Lanczos trực tiếp từ bản giao gốc. 28/28 sidecar khớp prompt try1.

Không dùng nền khóa màu vì công cụ đã trả alpha thật. Vẫn đo bảo thủ cả M (300° ±15°) và G (120° ±15°), S >0,5; tỷ lệ tính trên các pixel alpha >0. Dải mép là vùng trong/ngoài 3 px quanh biên alpha ≥128, dùng kernel Disk:3. Bảng dưới là bản gốc giao; cả 28 bản cũng có **0 pixel alpha bán trong suốt ngoài dải mép**, tỷ lệ M/G đều ≤0,2%.

| Ảnh | Hộp bao alpha >16 (x0,y0 → x1,y1) | Cạnh dài % | Lệch tâm tối đa % | Alpha sai ngoài 3 px | M % | G % |
|---|---|---:|---:|---:|---:|---:|
| `keycap` | 154,349 → 870,675 | 69.922 | 0.000 | 0 | 0.0193 | 0.0220 |
| `keycap-active` | 154,347 → 870,676 | 69.922 | 0.049 | 0 | 0.0050 | 0.0036 |
| `led-on` | 155,154 → 869,870 | 69.922 | 0.000 | 0 | 0.0142 | 0.0045 |
| `led-off` | 154,154 → 869,870 | 69.922 | 0.049 | 0 | 0.0182 | 0.0127 |
| `mag-empty` | 396,154 → 628,870 | 69.922 | 0.000 | 0 | 0.0094 | 0.0012 |
| `mag-full` | 395,154 → 628,870 | 69.922 | 0.049 | 0 | 0.0255 | 0.0068 |
| `arrow` | 235,154 → 788,870 | 69.922 | 0.049 | 0 | 0.0042 | 0.0074 |

[identify đủ 28 PNG](../../games/typing-survival/art-src/_review/153/identify-final.txt); [kiểm trực tiếp bản giao và bản thu](../../games/typing-survival/art-src/_review/153/resume-20261031/verification-final.json).

### Luma và cỡ trong game

Thu trực tiếp **toàn canvas gốc, gồm lề alpha**, về cạnh/cỡ bảng phiếu; không cắt sát vật trước khi đo. Cách này giữ đúng ảnh mà runtime nhận. Luma Y′ = 0,2126 R′ + 0,7152 G′ + 0,0722 B′ trên sRGB, trung bình theo trọng số alpha của vật; Δ là độ lệch tuyệt đối với luma nền. Hai nền là `#14181f` và `#8c96a3`. Đây là luma hình ảnh, không phải tỷ số tương phản WCAG.

| Ảnh | Cỡ 720p / 1080p | Luma vật 720 / 1080 | Δ than chì 720 / 1080 | Δ thép sáng 720 / 1080 |
|---|---|---|---|---|
| `keycap` | 16 / 24 px | 0.352276 / 0.346424 | 0.259511 / 0.253659 | 0.231303 / 0.237155 |
| `keycap-active` | 16 / 24 px | 0.373647 / 0.368024 | 0.280882 / 0.275259 | 0.209932 / 0.215555 |
| `led-on` | 8 / 12 px | 0.527699 / 0.521918 | 0.434934 / 0.429153 | 0.055880 / 0.061661 |
| `led-off` | 8 / 12 px | 0.384504 / 0.375949 | 0.291739 / 0.283184 | 0.199075 / 0.207630 |
| `mag-empty` | 10 / 15 px | 0.345145 / 0.344162 | 0.252381 / 0.251397 | 0.238434 / 0.239417 |
| `mag-full` | 10 / 15 px | 0.647333 / 0.643226 | 0.554568 / 0.550461 | 0.063754 / 0.059647 |
| `arrow` | 12 / 18 px | 0.575711 / 0.571580 | 0.482947 / 0.478815 | 0.007867 / 0.011999 |

Tất cả đạt Δ ≥0,25 trên nền than chì ở cả hai cỡ. `mag-full − mag-empty` tại 10 px = **0,647333 − 0,345145 = 0,302188 ≥0,30**. Các ô hẹp và đèn tắt vẫn cần Claude xem ở cỡ thật; tờ phóng nearest chỉ giúp kiểm biên, không thay việc chấm ở cỡ thật.

### IoU ở 32 px

Resize Lanczos trực tiếp về 32², mặt nạ alpha >16. Cột “khác vật” loại trừ đúng ảnh cùng cặp sáng/tắt. Tất cả cặp khác vật ≤0,80; ba cặp trạng thái ≥0,95.

| Ảnh | IoU lớn nhất với vật khác | Vật đối chiếu | IoU cùng cặp |
|---|---:|---|---:|
| `keycap` | 0.571759 | `led-on` | 0.980315 |
| `keycap-active` | 0.576037 | `led-on` | 0.980315 |
| `led-on` | 0.576037 | `keycap-active` | 0.995370 |
| `led-off` | 0.573394 | `keycap-active` | 0.995370 |
| `mag-empty` | 0.450355 | `arrow` | 1.000000 |
| `mag-full` | 0.450355 | `arrow` | 1.000000 |
| `arrow` | 0.450355 | `mag-empty` | — |

[Số đo đầy đủ, gồm toàn bộ ma trận IoU](../../games/typing-survival/art-src/_review/153/metrics-final.json).

## KA5 · Tự chấm trên bản hậu kỳ

Thứ tự bộ điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. Hợp bộ 1,5 vì các icon súng cũ thiên về thép kỹ thuật trong khi bộ mới dùng kính và vàng trắng Lightbearer; khung 127 khớp rõ hơn. “Dùng tiếp” được 2 sau khi mọi kiểm số ở trên đã đạt. Đã xem cả bảy bản 1024, tờ đối chiếu và cỡ thật trên hai nền.

| Ảnh | Gốc: 5 tiêu chí | Tổng gốc | 720p: 5 tiêu chí | Tổng 720p | Nhận xét ở cỡ nhỏ |
|---|---|---:|---|---:|---|
| `keycap` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9,0 | Mặt phím và vát cạnh rõ; chỉ góc thu thành nét nhỏ. |
| `keycap-active` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1,5 / 1,5 / 2 / 2 | 9,0 | Viền lam phân biệt được, chi tiết mảnh giảm. |
| `led-on` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 2 / 1,5 / 2 / 2 | 9,5 | Tâm lam sáng, đọc trạng thái tức thời. |
| `led-off` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1 / 1,5 / 2 / 2 | 8,5 | Vòng kim loại còn rõ; kính tắt rất nhỏ ở 8 px. |
| `mag-empty` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 1 / 1,5 / 2 / 2 | 8,5 | Ô rỗng nhận ra nhờ dáng dọc, viền mảnh trên nền sáng. |
| `mag-full` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 2 / 1,5 / 2 / 2 | 9,5 | Trắng lam và ô rỗng tách nhau rõ. |
| `arrow` | 2 / 2 / 1,5 / 2 / 2 | 9,5 | 2 / 2 / 1,5 / 2 / 2 | 9,5 | Chevron hướng phải rõ, vát cạnh gọn. |

Mức tự chấm: **đạt ≥8 cho cả bảy ảnh**. Hai ảnh 8,5 có điểm cần nâng được ghi ngay trong báo cáo; không sửa ART_REPLACE_LATER vì ngoài phạm vi ghi của phiếu này.

## Script, hồ sơ và sai khác

Tất cả trong `_review/153/resume-20261031/`:

- `process.py` và `candidate-1/`: giữ nguyên hậu kỳ đầu, đo được chênh ô đạn chưa đạt; tờ xem nháp thiếu mảnh tham chiếu vì gravity ảnh hưởng crop.
- `process-v2.py` và `candidate-2/`: bản chọn, thêm chỉnh sáng toàn ảnh +6% cho mag-full. Script nhận tag đầu ra mới, từ chối ghi đè. Có thể tái lập từ `.try1.png` bằng `python3 games/typing-survival/art-src/_review/153/resume-20261031/process-v2.py replay-1`. Tờ nháp trong candidate-2 vẫn bị gravity ảnh hưởng crop; không dùng để giao.
- `owner-hud-crop.png`: mảnh tham chiếu cắt riêng đúng vùng HUD; `deliver.py` dùng ảnh này làm tờ chính cuối cùng, đã xem và có đủ tham chiếu. Script giao từ chối ghi đè media để giữ an toàn.
- `verify-final.py`: kiểm trực tiếp 28 bản giao, alpha/màu khóa, prompt và Lanczos; không sửa ảnh.
- `report-and-audit.py`: MD5 bằng công cụ Mac, diff và báo cáo. Muốn audit lại, truyền tag mới; mọi snapshot cũ giữ nguyên.
- `generation-index.json`: chỉ mục bảy lời gọi công cụ và ảnh đích chỉnh. `153-report-before-resume.md`: nguyên văn báo cáo trước lượt tiếp tục.

Sai khác có giải thích: nguồn công cụ 1254² được chuẩn hóa về 1024²; chỉ mag-full tăng sáng 6%; tờ phụ phóng nearest bổ sung ngoài tờ bắt buộc. Không sửa prompt cũ. Không có ảnh bị bỏ, không xóa `.try*`, không ghi đè media hay hồ sơ đã tồn tại trước lượt này. Chỉ báo cáo được cập nhật theo yêu cầu.

Không chạy lệnh Git, mạng ngoài công cụ sinh ảnh, trình duyệt, dev server, build hoặc bộ kiểm thử game. Không sửa mã, không đọc/ghi Tu Tiên, không chạm `.wt-*`, âm thanh hay thư mục game khác ngoài đọc ảnh tham chiếu được chỉ định. Không có capture trình duyệt/render hoặc chuỗi raw frame để phải prune.

## Phần để lại và việc chủ dự án cần xem

Không thiếu ảnh hoặc kiểm bắt buộc nào. **Chờ Claude chấm lại ≥8**; Claude là người chép vào `public/` khi gắn. Chủ dự án/Claude xem tờ chính, bảy tờ so và tờ cỡ thật, ưu tiên `led-off` 8 px, `mag-empty` 10 px và viền bật của phím 16 px. Chênh luma ô đạn đạt khá sát ngưỡng (0,302188); thay cách resize khi tích hợp thì cần đo lại cùng cỡ.

Hồ sơ lỗi hạn mức ngày 30/10 vẫn còn trong `_review/153/generation-error.json` và `_review/153/resume-20261030/`; lần này không gặp lỗi hạn mức, không có phần việc phải đợi giờ mở lại.
