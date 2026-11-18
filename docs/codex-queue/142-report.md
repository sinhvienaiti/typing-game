# Phiếu 142 · Wordwoven · Chế độ và số kết quả

Ngày hoàn tất bộ giao: **29/10/2026**, macOS, repo cha.

**Đủ 8 ảnh × 4 cỡ = 32 PNG, prompt cạnh từng ảnh, 8 nguồn try1 nguyên vẹn, tờ xem và 8 tờ “bản sinh | bản hậu kỳ”. Kiểm 1–5 đạt. Tự chấm trên bản hậu kỳ: M từ 8, Q từ 9 ở cỡ 720p. Chưa có điểm chấm nhận của Claude.**

## 1. Bộ giao và tiếp nhận

- Ảnh giao ở [ui/icons/](../../games/typing-defense/art-src/ui/icons/), đúng tám tên của phiếu: `mode-relax`, `mode-learn`, `mode-balanced`, `mode-challenge`, `stat-nights`, `stat-foes`, `stat-words`, `record-ribbon`.
- Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png` và `.prompt.txt` tương ứng. Gốc 1024², sRGB/RGBA 8 bit; bản thu 256², 128², 64², đều `srgba`.
- Khi tiếp nhận đã có bốn PNG try1 chế độ, tám prompt try1, script và mốc MD5. Giữ nguyên mọi file này. Lượt này tạo thêm bốn PNG try1 kết quả bằng **image_gen tích hợp**, hoàn tất hậu kỳ và giao. Không tự nhận đã sinh bốn nguồn có trước.
- Bộ 115 thực tế ở `ui/frames-epic/`; `ui/frames/` ghi trong phiếu trống. Đã xem và đính kèm `panel-large.png`, `crest.png` của 115 và `ui/title-epic/keyart.png` của 113 khi sinh bốn ảnh mới. Đã xem ảnh tham chiếu chủ dự án và bốn icon có sẵn.

## 2. Prompt và các lượt sinh

Mỗi ảnh chỉ có **try1**, tổng tám nguồn; không có try2/try3, không sửa hoặc ghi đè prompt có trước. Cả tám nguồn try1 trùng SHA-256 với nguồn image_gen ghi trong `<tên>-generation.json`; xem `generation-audit.json`.

Khối STYLE-UI dùng nguyên văn khối mới của AD/115, tiếp theo ICON của tài liệu định dạng. Phần bổ sung xử lý chỗ mâu thuẫn với ICON cũ: ưu tiên chất liệu có khối, bevel và bóng vẽ của STYLE-UI; bỏ yêu cầu tô phẳng/viền mực; cạnh dài 70% thay cho 80%. Dòng nền M khóa `#FF00FF` nằm cuối prompt. Khóa dáng lớn, không chữ/số/ký hiệu, không khung bao quanh. Prompt nguyên văn đầy đủ ở file cạnh ảnh và `prompts.json`.

| Ảnh | Lượt / chọn | Phần riêng của prompt và kết quả |
| --- | --- | --- |
| `mode-relax` | 1 / try1 | Hoa sen trắng, tâm vàng, gợn nước ngọc thấp và rộng. Không cần sửa prompt lần hai. |
| `mode-learn` | 1 / try1 | Cuộn giấy trống, hai đầu cuộn lớn và bút ngọc chéo. Không cần sửa prompt lần hai. |
| `mode-balanced` | 1 / try1 | Một kiếm bạc và một bút ngọc tạo dáng chữ X. Không cần sửa prompt lần hai. |
| `mode-challenge` | 1 / try1 | Mũi giáo đồng sáng, ngọn lửa hổ phách lệch phải, chuôi ngọc ngắn. Không cần sửa prompt lần hai. |
| `stat-nights` | 1 / try1 | Trăng lưỡi liềm trên tường đá có ba răng thành và cổng ngọc. Không cần sửa prompt lần hai. |
| `stat-foes` | 1 / try1 | Mặt nạ chiến binh đá vôi/ngọc, một sừng đồng và mảng vỡ ở phía phải. Không cần sửa prompt lần hai. |
| `stat-words` | 1 / try1 | Ba thẻ trống xòe quạt, viền vật liệu ngọc và góc vàng. Không cần sửa prompt lần hai. |
| `record-ribbon` | 1 / try1 | Hoa thị vàng lá, tâm ngọc nổi và hai đuôi dải gấp. Không cần sửa prompt lần hai. |

## 3. Hậu kỳ giữ tranh

Nguồn image_gen là **1254 × 1254**; giữ nguyên byte trong `.try1.png`. Hậu kỳ chỉ tách nền M, khử nhiễm khóa ở mép, trim vùng trong suốt, Lanczos giữ tỷ lệ và thêm lề vào canvas 1024². Không cắt vào vật, không đổi gamma/độ sáng, không san phẳng chất liệu, không thêm mảng phủ. Cánh sen, gợn nước, họa tiết vàng, sợi bút, vết vỡ và xếp nếp đều được giữ. Không gặp ngưỡng số buộc phải làm hỏng tranh.

Dùng bản công cụ `art-normalize` đã nằm trong hồ sơ phiếu để WORK nằm trong vùng được phép; không chạy công cụ từ thư mục repo với WORK mặc định ở ngoài phạm vi. Lệnh thực tế ghi ở `resume-v1/<tên>/commands.json`:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/142/art-normalize/key-alpha.sh   SOURCE.try1.png KEYED.png --bg '#FF00FF' --mode global   --despill protect-interior --no-key-hue
/opt/homebrew/bin/magick KEYED.png -trim +repage -filter Lanczos   -resize 716x716 -gravity center -background none -extent 1024x1024   -colorspace sRGB -depth 8 -strip PNG32:FINAL.png
```

Lanczos để lại vài giá trị alpha rất nhỏ ngoài dải mép 3 px. Sửa **chỉ alpha**, không đổi RGB: gốc sen 2 pixel, cuộn 2, kiếm/bút 4, giáo 2; bốn gốc khác 0. Sau thu trực tiếp từ gốc, bản 256 của cuộn sửa thêm 1 pixel alpha và kiếm/bút 4; mọi bản thu khác 0. Tổng **15 pixel alpha**, tọa độ và giá trị trước/sau nằm trong `resume-delivery/<tên>/edge-repairs.json`. Không co mặt nạ cả vật, không xóa phần vẽ.

Ba cỡ thu đều Lanczos **trực tiếp từ gốc giao 1024**, không nối chuỗi. Không làm nét bất kỳ cỡ nào. Audit RGB xác nhận mọi bản thu trùng RGB của phép Lanczos trực tiếp; chỉ năm pixel alpha nói trên khác ở hai bản 256.

## 4. KA1 · Không sửa hoặc xóa file có trước

Đã dùng `/sbin/md5 -r` đệ quy mọi file trong thư mục đích `ui/icons/`:

| Mốc | Số file | Thêm so với mốc | Sửa | Xóa |
| --- | ---: | ---: | ---: | ---: |
| `md5-before.txt` đã có từ đầu phiếu | 438 | — | — | — |
| `md5-after.txt` sau giao | 518 | 80 | 0 | 0 |
| `md5-resume-before.txt` chụp lúc tiếp nhận | 450 | — | — | — |
| Sau giao so với mốc tiếp nhận | 518 | 68 | 0 | 0 |

Diff chỉ có dòng nội dung thêm, không có dòng nội dung xóa (bỏ qua hai dòng tiêu đề chuẩn của unified diff). 80 file của toàn phiếu gồm 8 nguồn + 8 prompt try1 + 32 PNG giao + 32 prompt giao. Lượt tiếp nhận thêm 4 nguồn và 64 file giao. Hồ sơ: `md5-diff.txt`, `md5-summary.json`, `published-check/resume-md5.diff.txt`. Cả **64 file giao trùng byte** với bộ đã đo, xem `published-check/published-match.json`.

## 5. Khổ, lề và alpha

Lệnh identify chạy trên **đúng 32 PNG trong ui/icons**, kết quả đầy đủ: [published-check/identify.txt](../../games/typing-defense/art-src/_review/142/published-check/identify.txt). Tất cả đúng khổ và `srgba`; alpha có min 0, max 255. Cạnh dài alpha >16 là **716/1024 = 69,921875%** cho cả tám ảnh.

Đo sắc khóa: pixel alpha >0, hue cách 300° không quá 15°, S >0,5; tỷ lệ chia cho tổng pixel alpha >0. Dải mép 3 px dùng dilation/erosion Square:3 của mask alpha >127. Cột cuối là giá trị tệ nhất trong cả bốn cỡ. Đều đạt ≤0,2%; pixel alpha bán trong suốt ngoài dải mép **bằng 0 ở cả bốn cỡ**.

| Ảnh | Bbox gốc x/y/w/h | Lệch tâm lớn nhất (%) | Alpha ngoài dải mép (px) | Sắc khóa gốc: px / px thấy | Sắc khóa gốc (%) | Sắc khóa max 4 cỡ (%) |
| --- | --- | ---: | ---: | --- | ---: | ---: |
| `mode-relax` | 154 / 235 / 716 / 553 | 0.04883 | 0 | 218 / 273281 | 0.07977 | 0.07977 |
| `mode-learn` | 154 / 198 / 716 / 627 | 0.04883 | 0 | 161 / 273155 | 0.05894 | 0.08364 |
| `mode-balanced` | 154 / 179 / 716 / 666 | 0.00000 | 0 | 260 / 176866 | 0.14700 | 0.14700 |
| `mode-challenge` | 348 / 154 / 327 / 716 | 0.04883 | 0 | 73 / 121719 | 0.05997 | 0.06083 |
| `stat-nights` | 154 / 175 / 716 / 674 | 0.00000 | 0 | 213 / 273440 | 0.07790 | 0.07790 |
| `stat-foes` | 215 / 154 / 594 / 716 | 0.00000 | 0 | 444 / 243794 | 0.18212 | 0.18212 |
| `stat-words` | 154 / 230 / 716 / 564 | 0.00000 | 0 | 272 / 287772 | 0.09452 | 0.09452 |
| `record-ribbon` | 189 / 154 / 645 / 716 | 0.04883 | 0 | 242 / 310687 | 0.07789 | 0.07789 |

## 6. Cỡ thật, tương phản và dáng riêng

Nền ngọc **#061e16** lấy từ lòng `panel-large` 115: trung bình vùng giữa 256² xấp xỉ RGB (5,6; 30,0; 21,6), làm tròn thành (6; 30; 22). Nền đá vôi **#e8e1cf** theo bảng phiếu. Hai nền đều có trên tờ xem. Luma dùng Y′ = 0,2126R′ + 0,7152G′ + 0,0722B′ trên sRGB 0–1; luma vật là trung bình có trọng số alpha. Tương phản là trị tuyệt đối chênh luma, không phải tỷ số WCAG.

| Ảnh | Cỡ 720p / 1080p | ΔY′ ngọc gốc | ΔY′ đá vôi gốc | ΔY′ ngọc 720p | ΔY′ ngọc 1080p | IoU lớn nhất ở 32 px | Ảnh cùng cặp |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `mode-relax` | 20 / 24 | 0.4761 | 0.3117 | 0.4746 | 0.4745 | 0.76081 | `stat-words` |
| `mode-learn` | 20 / 24 | 0.4772 | 0.3105 | 0.4755 | 0.4758 | 0.68889 | `mode-relax` |
| `mode-balanced` | 20 / 24 | 0.4299 | 0.3578 | 0.4274 | 0.4296 | 0.47396 | `record-ribbon` |
| `mode-challenge` | 20 / 24 | 0.4838 | 0.3039 | 0.4840 | 0.4847 | 0.48399 | `stat-foes` |
| `stat-nights` | 20 / 24 | 0.4219 | 0.3658 | 0.4219 | 0.4226 | 0.57039 | `record-ribbon` |
| `stat-foes` | 20 / 24 | 0.3992 | 0.3885 | 0.3995 | 0.3996 | 0.69706 | `stat-words` |
| `stat-words` | 20 / 24 | 0.5911 | 0.1966 | 0.5869 | 0.5882 | 0.76081 | `mode-relax` |
| `record-ribbon` | 32 / 40 | 0.3782 | 0.4095 | 0.3788 | 0.3790 | 0.69010 | `stat-words` |

Tất cả qua ΔY′ ≥0,25 trên nền ngọc, cả gốc và cỡ thật. Riêng thẻ từ có ΔY′ trên nền đá vôi dưới 0,25; nền ngọc đạt rõ. Không sửa tối tranh để ép cả hai nền cùng đạt vì phiếu chỉ yêu cầu ít nhất một nền. Ở 32 px, mask alpha >16 cho mọi cặp có IoU ≤0,80; lớn nhất **0,76081**, sen/thẻ. Không có cặp sáng/tắt trong phiếu này nên điều kiện IoU ≥0,95 không áp dụng. Ma trận đầy đủ ở `delivery-checks/iou-matrix.json`; tất cả chốt số ở `delivery-checks/pass.json`.

## 7. KA5 · Tự chấm bản hậu kỳ

Đã xem từng bản hậu kỳ đủ 1024² và tờ cỡ thật 720p/1080p; không lấy điểm của bản sinh. Q theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” nhận 2 sau khi mọi kiểm số đạt. M so mức hoàn thiện của HUD thương mại trong ảnh tham chiếu, không so với phong cách cũ.

| Ảnh | Q gốc: năm tiêu chí / tổng | Q 720p: năm tiêu chí / tổng | M gốc | M 720p | Nhận xét ở cỡ dùng |
| --- | --- | --- | ---: | ---: | --- |
| `mode-relax` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ở 20 px, cánh hoa còn rõ; các nét mây chỉ còn thành chất liệu. |
| `mode-learn` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ở 20 px, nhận ra cuộn và bút; hoa văn đầu cuộn khá dày. |
| `mode-balanced` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ở 20 px, X rõ; cần màu sáng của lưỡi kiếm để phân biệt hai nhánh. |
| `mode-challenge` | 2/2/2/2/2 = **10** | 2/2/2/2/2 = **10** | 8.5 | 8.5 | Dáng cao hẹp và lửa vàng cam đọc tốt; nét chạm không còn đọc riêng. |
| `stat-nights` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ở 20 px, trăng và khối thành còn tách được; cổng nhỏ và nhiều trang trí. |
| `stat-foes` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ở 20 px, đọc ra mặt nạ; mảng vỡ nhỏ và hốc mắt mất một phần sắc nét. |
| `stat-words` | 2/2/2/2/2 = **10** | 2/1/2/2/2 = **9** | 8.5 | 8 | Ba mặt thẻ sáng rõ trên ngọc; trên đá vôi nhạt, mặt thẻ chìm hơn. |
| `record-ribbon` | 2/2/2/2/2 = **10** | 2/2/2/2/2 = **10** | 9 | 8.5 | Ở 32 px, vòng xếp nếp, tâm ngọc và hai đuôi đều rõ. |

**Đứng cạnh được ở mức phát hành M = 8.** Bevel, vân đá/ngọc và ánh kim giữ chất lượng khi tách nền; dáng riêng đọc được. Nét chạm dày ở cuộn, mặt nạ và tường là giới hạn còn lại ở 20 px. Không coi bộ này đã được Claude nghiệm thu.

## 8. Tờ xem và đối chiếu hậu kỳ

Tờ chính: [142-sheet.jpg](../../games/typing-defense/art-src/_review/142-sheet.jpg), **2048 × 688**: hàng 1 bản gốc thu về 256; hàng 2 cỡ 1080p trên hai nền; hàng 3 cỡ 720p trên hai nền; hàng 4 bốn icon có sẵn và mảnh HUD chủ dự án, cùng cao 128 px. Nhãn đặt dưới từng ảnh. [Tờ cỡ nhỏ](../../games/typing-defense/art-src/_review/142/final-sheets/142-small.jpg) giữ đúng kích thước dùng, không phóng nét.

Tám tờ cùng cỡ canvas 512² mỗi bên, trái bản sinh, phải bản hậu kỳ; việc thêm lề làm vật phía hậu kỳ nhỏ hơn, không phải cắt mất tranh:

- [mode-relax · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/mode-relax-before-after.jpg).
- [mode-learn · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/mode-learn-before-after.jpg).
- [mode-balanced · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/mode-balanced-before-after.jpg).
- [mode-challenge · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/mode-challenge-before-after.jpg).
- [stat-nights · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/stat-nights-before-after.jpg).
- [stat-foes · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/stat-foes-before-after.jpg).
- [stat-words · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/stat-words-before-after.jpg).
- [record-ribbon · bản sinh | bản hậu kỳ](../../games/typing-defense/art-src/_review/142/final-sheets/record-ribbon-before-after.jpg).

## 9. Script và chạy lại

Mã và dữ liệu ở [_review/142/](../../games/typing-defense/art-src/_review/142/):

- `intake-resume.py`: lưu nguồn mới nguyên byte, kiểm prompt và tạo nhật ký nguồn.
- `pipeline.py`: script đã có khi tiếp nhận, giữ nguyên. `pipeline-resume.py`: bản mới dùng nền ngọc 115; build, đo, dựng thử, chép giao và MD5.
- `delivery-resume.py`: tạo bộ cuối, sửa riêng alpha ngoài dải mép và thu trực tiếp ba cỡ; nhật ký từng pixel.
- `check-delivery.py`: kiểm toàn bộ chốt số; `render-final-sheets.py`: tờ chính và tám tờ đối chiếu, nhãn rời khỏi tranh.
- `audit-published.py`: đối chiếu file giao, nguồn thu trực tiếp và mốc MD5 tiếp nhận. `write-report.py`: tạo báo cáo từ số cuối, không ghi đè.

Kiểm lại bộ giao vào **tên hồ sơ mới**, không sinh ảnh, không sửa file giao:

```sh
PYTHONDONTWRITEBYTECODE=1 python3   games/typing-defense/art-src/_review/142/audit-published.py recheck-owner-01
PYTHONDONTWRITEBYTECODE=1 python3   games/typing-defense/art-src/_review/142/pipeline-resume.py verify   --run resume-delivery --out recheck-metrics-01
```

Mọi script writer từ chối ghi đè. Các thư mục thử `resume-final`, `six-checks`, `six-sheets`, `delivery-sheets` giữ lại để truy vết, **không phải bộ cần lấy**; bộ giao chuẩn là tám tên trực tiếp trong `ui/icons/`, trùng byte với `resume-delivery`.

## 10. Khác phiếu, việc bỏ qua và cần xem

- Dùng đường dẫn thật `ui/frames-epic/` của 115 thay cho `ui/frames/` rỗng; không bỏ qua tham chiếu 115 hoặc 113.
- Tiếp nhận bốn ảnh thử đã có, chỉ tạo bốn ảnh thiếu. Không sinh lại ảnh đạt; không có vòng sửa prompt thứ hai.
- Thêm sửa alpha đơn lẻ sau Lanczos ở hai bản 256; RGB vẫn đúng phép thu trực tiếp. Đây là sửa mép được §5 cho phép, không thay phần vẽ. Không làm nét bản 64.
- Không ghi `public/`, không gắn runtime: Claude chép khi gắn theo phiếu. Không làm âm thanh vì ngoài phạm vi ảnh. Không chạy Git, build/test game, server, trình duyệt hay mạng ngoài image_gen; không đọc/ghi cây Tu Tiên, không đụng worktree.
- Không có frame trình duyệt/raw render mới nên không có capture cần prune. Không xóa bất kỳ `.try*` hoặc file có trước nào.

**Chủ dự án/Claude cần xem:** tờ chính, tám tờ trước/sau và trực tiếp tám PNG ở 1024² cùng cỡ 720p; chú ý độ dày trang trí của cuộn/mặt nạ/tường và mặt thẻ trên nền sáng. Chấm nhận độc lập từ 8 trở lên trước khi gắn. Phiếu đã đủ phần giao và tự kiểm của Codex; **chưa ghi nhận nghiệm thu Claude**.
