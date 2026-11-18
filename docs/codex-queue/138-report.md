# Phiếu 138 · Dragonhold · Hệ thống và học

**Kết quả:** đủ 10 icon, 40 PNG chọn/thu, 40 prompt đi kèm và 10 PNG lượt sinh đầu cùng 10 prompt nguyên văn. Tự chấm KA5 từ 8,5; chờ Claude chấm lại từ 8 để nhận và gắn vào `public/`.

## 1. Nơi giao và tham chiếu

- Ảnh: `games/dragon-hold/art-src/ui/icons/{pause,camera-reset,keyboard,speaker,check,new-word,deny,lock,upgrade,sell}*`.
- [Tờ xem cuối](../../games/dragon-hold/art-src/_review/138-sheet-final.jpg): hàng 1 ô 256 px; hàng 2 cỡ 1080p trên vỏ cây/kem; hàng 3 cỡ 720p trên hai nền; hàng 4 cả bộ mới cạnh `skill-fire-breath`, `gold`, `shield`, `armour` và mảnh HUD chủ dự án, cùng chiều cao vật 96 px.
- [Tờ kiểm cỡ nhỏ và mép](../../games/dragon-hold/art-src/_review/138-detail-final.jpg): cỡ thật, phóng nearest 8× để xem cấu trúc; mép phóng nearest 4×.
- [Hồ sơ, script và số đo](../../games/dragon-hold/art-src/_review/138/).

Đã đọc AD §3.2, ART_ACCEPTANCE §2.2, định dạng `05-icons.md`, UIC-DH-2 và phiếu 119. Đã xem trực tiếp `skill-fire-breath.png`, `gold.png`, ảnh `owner-epic-2026-10-28.webp` của Wordwoven và hai tờ xem cuối. Không có ảnh chọn của 119 trong thư mục mỹ thuật Dragonhold tại lúc khảo sát. Lấy chất liệu, độ hoàn thiện và độ rõ HUD thương mại làm mốc; không chép nội dung ảnh mẫu.

## 2. Sinh ảnh và sửa prompt

Dùng công cụ tích hợp `image_gen`, một lời gọi cho mỗi icon, nền M `#FF00FF`. Mỗi prompt bắt đầu bằng nguyên văn STYLE-UI mới của AD Dragonhold, tiếp theo là KIND ICON, mô tả riêng, dòng nền. Phiếu không cung cấp nguyên văn khối KIND; đã soạn khối ICON theo các ràng buộc của phiếu: khối lớn, relief, khoảng trống rõ, đọc ở cỡ nhỏ, không chữ hay khung phụ. Prompt chính xác nằm tại `<tên>.try1.prompt.txt`; bản chọn và ba bản thu có bản sao nguyên văn bên cạnh. Lệnh hậu kỳ nằm trong script, không trộn vào prompt đã gửi.

| Icon | Lượt | Điểm nhấn riêng của prompt lượt 1 | Khổ nguồn công cụ | Gamma RGB | Pixel khử sắc khóa bổ sung |
|---|---:|---|---|---:|---:|
| `pause` | 1 | Hai thanh granite rộng, khe lớn, đĩa sắt vật lý không vòng trang trí | 1254x1254 | 1.10 | 159 |
| `camera-reset` | 1 | Mắt rồng ngang, đồng tử dọc, mũi tên quay lại mở và dày | 1254x1254 | 1.55 | 300 |
| `keyboard` | 1 | Hai hàng bốn phím trống, thanh cách lớn, dáng thấp ngang | 1774x887 | 1.10 | 99 |
| `speaker` | 1 | Kèn đồng và đúng hai cung âm tách nhau, ưu tiên đọc ở 14 px | 1254x1254 | 1.80 | 128 |
| `check` | 1 | Dáng dấu kiểm tự làm silhouette, tay phải dài, mặt đá dát vàng than hồng | 1254x1254 | 1.30 | 7 |
| `new-word` | 1 | Sao bốn cánh lớn và hai sao phụ, biên đặc, ánh sáng gói trong vật | 1254x1254 | 1.45 | 22 |
| `deny` | 1 | Hai thanh sắt chéo X, than đỏ nhỏ tại giao điểm, không đĩa nền | 1254x1254 | 1.70 | 351 |
| `lock` | 1 | Quai U có lỗ thoáng lớn, ba mảng vảy lớn, lỗ khóa rõ ở 12 px | 1254x1254 | 1.50 | 598 |
| `upgrade` | 1 | Ba bậc granite lên từ trái sang phải, chevron lớn phía trên | 1254x1254 | 1.40 | 189 |
| `sell` | 1 | Găng giáp mở, ngón gom thành khối, ba đồng tiền trơn tách nhau | 1254x1254 | 1.45 | 221 |

Không có lượt 2 hoặc 3, nên không có sửa prompt giữa lượt. Các lỗi đo được đều sửa bằng công cụ: tách nền global với despill bảo vệ lòng vật; crop theo alpha >16, fit Lanczos cạnh dài 717 px, đặt giữa canvas 1024 px; nâng trung độ RGB vừa đủ để tương phản nhỏ đạt ít nhất 0,27; khử sắc M còn sót bằng tăng G tới min(R,B), chỉ trên pixel có alpha >0, hue 285–315°, S >0,5. Không vẽ lại hình hay thêm chi tiết bằng mã.

## 3. Khổ, alpha, lề và tương phản

**40/40 file đạt** trong `delivery-verification-accepted.json`. Bản chọn 1024×1024; các bản 256×256, 128×128, 64×64 đều thu Lanczos trực tiếp từ bản chọn, không làm nét. ImageMagick báo `srgba 4.0`: bốn kênh sRGB + alpha, 8 bit. Lệnh bắt buộc và kết quả đầy đủ nằm ở `identify-accepted.txt`.

Luma dùng Rec.709 trên các kênh sRGB mã hóa: Y=(0,2126R+0,7152G+0,0722B)/255. Tương phản cỡ thật là chênh luma trung bình sau ghép alpha trên footprint alpha >16. Hai nền Dragonhold: vỏ cây #2b2118 và kem #f1e3c4. Điều kiện 0,25 đạt trên nền tối ở cả hai cỡ cho mọi ảnh; không yêu cầu đồng thời đạt trên nền kem.

Dải mép là phần giãn trừ co bán kính Chebyshev 3 px quanh mask alpha ≥128; ngoài dải, không có pixel 0<alpha<255. Sắc khóa đếm mọi pixel alpha >0, hue cách M không quá 15°, S >0,5; mẫu số là số pixel alpha >0. Bảng dưới: cột alpha áp cho cả bốn khổ; spill gốc =0% cho cả 10 ảnh; spill tối đa gồm cả ba bản thu.

| Icon | Bbox gốc x,y,w,h | Cạnh dài / ô | Lệch tâm lớn nhất | Alpha ngoài 3 px | Spill tối đa 4 khổ | Cỡ 720/1080 | ΔY tối 720/1080 | ΔY kem 720/1080 |
|---|---|---:|---:|---:|---:|---|---|---|
| `pause` | 154,153,716,717 | 70.02% | 0.049% | 0 | 0.0307% | 16/24 | 0.278/0.290 | 0.363/0.380 |
| `camera-reset` | 153,185,717,653 | 70.02% | 0.049% | 0 | 0.0643% | 16/24 | 0.273/0.297 | 0.286/0.314 |
| `keyboard` | 153,375,717,273 | 70.02% | 0.049% | 0 | 0.0170% | 24/36 | 0.277/0.318 | 0.300/0.340 |
| `speaker` | 153,231,717,561 | 70.02% | 0.049% | 0 | 0.0276% | 14/22 | 0.274/0.309 | 0.227/0.256 |
| `check` | 153,192,717,640 | 70.02% | 0.049% | 0 | 0.0000% | 14/22 | 0.276/0.319 | 0.264/0.304 |
| `new-word` | 231,153,561,717 | 70.02% | 0.049% | 0 | 0.1408% | 14/22 | 0.270/0.339 | 0.116/0.147 |
| `deny` | 153,155,717,714 | 70.02% | 0.049% | 0 | 0.0271% | 16/24 | 0.273/0.282 | 0.316/0.330 |
| `lock` | 210,153,603,717 | 70.02% | 0.049% | 0 | 0.0156% | 12/18 | 0.274/0.301 | 0.270/0.301 |
| `upgrade` | 166,153,692,717 | 70.02% | 0.049% | 0 | 0.0435% | 16/24 | 0.275/0.313 | 0.288/0.326 |
| `sell` | 205,153,614,717 | 70.02% | 0.049% | 0 | 0.0419% | 16/24 | 0.274/0.293 | 0.246/0.265 |

Ba bản thu mới có ringing ngoài dải 3 px sau Lanczos: `camera-reset.256` 1 pixel, `new-word.128` 1 pixel, `new-word.64` 4 pixel (đều alpha=1). Đã đưa alpha của sáu pixel đó về 0, giữ đầy đủ bản trước sửa và bản sửa ở `derived-alpha-repair/`. Không làm nét; không sửa nguồn hay bất kỳ file có trước phiếu. Kiểm đầu tiên còn có lỗi đọc chuỗi kênh `srgba 4.0`; bản kiểm `-accepted` sửa bộ đọc và đo lại đủ 40 file. Giữ log trung gian, không dùng chúng làm kết luận.

## 4. Dáng riêng ở 32 px

Mặt nạ alpha ≥128 sau thu Lanczos 32 px; IoU = giao/hợp. Đã đo đủ 45 cặp, không chỉ các cặp dưới đây. Không có cặp sáng/tắt của cùng vật trong phiếu. Tất cả IoU ≤0,80; bảng đầy đủ ở `metrics-ready.json`.

| Icon | IoU lớn nhất | Với icon |
|---|---:|---|
| `pause` | 0.6816 | `lock` |
| `camera-reset` | 0.6250 | `pause` |
| `keyboard` | 0.5498 | `speaker` |
| `speaker` | 0.5498 | `keyboard` |
| `check` | 0.4655 | `camera-reset` |
| `new-word` | 0.4000 | `speaker` |
| `deny` | 0.5042 | `pause` |
| `lock` | 0.6816 | `pause` |
| `upgrade` | 0.5923 | `pause` |
| `sell` | 0.4377 | `lock` |

Ở 14 px, nhận ra kèn/phát âm, dấu kiểm và sao từ mới. Hai cung của `speaker` không tách sắc nét như ở bản lớn; sao phụ của `new-word` giảm rõ trên nền kem. `lock` ở 12 px vẫn đọc được quai và thân, chi tiết vảy/lỗ khóa không giữ đầy đủ. `sell` ở 16 px giữ dáng bàn tay và đồng vàng, không còn đọc từng đốt giáp. Đã trừ điểm Đọc được tương ứng; Claude cần xem đúng cỡ, không chấm bằng bản phóng.

## 5. KA5 và mức chợ

Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**; mỗi tiêu chí 0–2. Dùng tiếp =2 chỉ sau khi mọi kiểm số đo đạt. Hình khối 1,5 ghi nhận độ nổi/phối cảnh mạnh hơn yêu cầu nhìn phẳng; đánh giá ở cỡ thật vẫn rõ. M chấm độ hoàn thiện UI thương mại: relief granite, sắt và vàng có ánh sáng, biên vật liệu rõ, dáng hệ thống đủ độc lập; không áp tiêu chí cảnh quan ba tầng/trời cho icon.

| Icon | KA5 gốc (5 tiêu chí) | Tổng | KA5 720p (5 tiêu chí) | Tổng | M gốc / 720p |
|---|---|---:|---|---:|---|
| `pause` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 8,5 / 8,5 |
| `camera-reset` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1 / 2 / 1,5 / 2 | 8,5 | 8,5 / 8 |
| `keyboard` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | 8,5 / 8,5 |
| `speaker` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1 / 2 / 1,5 / 2 | 8,5 | 8,5 / 8 |
| `check` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 8,5 / 8,5 |
| `new-word` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | 8,5 / 8,5 |
| `deny` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | 8,5 / 8,5 |
| `lock` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1 / 2 / 1,5 / 2 | 8,5 | 8,5 / 8 |
| `upgrade` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1,5 / 2 / 1,5 / 2 | 9,0 | 8,5 / 8,5 |
| `sell` | 2 / 2 / 2 / 1,5 / 2 | 9,5 | 2 / 1 / 2 / 1,5 / 2 | 8,5 | 8,5 / 8 |

**Đứng cạnh được về độ hoàn thiện chất liệu và tính nhất quán của bộ mới**, còn giới hạn cỡ 12–14 px như đã nêu. Đây là tự chấm của Codex, chưa phải quyết định nhận của Claude.

## 6. KA1 và phạm vi

Trước lần ghi đầu tiên đã chạy `/sbin/md5 -r` cho toàn bộ 113 file có sẵn trong thư mục icon, lưu `md5-before.txt`. Các nơi đích 138 và báo cáo chưa có file. Sau khi hoàn tất chạy lại cho icon, `_review/138*` và báo cáo; xem `md5-after.txt`, `md5-diff.txt`, `ka1-summary.json`. Điều kiện bắt buộc: **113/113 file cũ giữ nguyên; 0 dòng bị xóa hoặc sửa; diff chỉ thêm**. Bản chụp sau loại chính nó, diff và JSON tổng kết để tránh tự tham chiếu. Thư mục icon thêm đúng 100 file của phiếu (50 PNG gồm nguồn thử và 50 prompt).

Không chạy Git, build, test game, dev server, trình duyệt hoặc mạng ngoài công cụ ảnh. Không đọc/ghi Tu Tiên, không đụng `.wt-*`, không sửa mã hay tài liệu khác, không ghi game khác. Không có âm thanh trong phạm vi. Không có capture trình duyệt hoặc raw frame để prune.

## 7. Khác phiếu và cách chạy lại

- Dùng STYLE-UI nguyên văn thay STYLE cảnh, đúng phần chung Dragonhold; KIND ICON tự soạn vì không có nguyên văn trong phiếu.
- Công cụ trả nguồn có khổ khác 1024; giữ nguyên mọi `.try1.png`, chỉ bản chọn mới crop/thu/căn giữa thành 1024. Không sinh lại chỉ vì khổ.
- Giữ nguyên `138-sheet.jpg` và `138-detail.jpg` là tờ xem trước bước khử sắc khóa bổ sung; tờ **cuối** có hậu tố `-final` để không ghi đè tờ đã tạo. Bố cục đủ bốn hàng như phiếu. Khác biệt hình chỉ là màu mép dưới 0,21% pixel vật.
- Có thêm prompt cho cả ba bản thu, log ứng viên, tờ soi cỡ nhỏ, bản sửa alpha và số đo cả 40 file. Sáu pixel alpha đã dọn là hậu kỳ sau Lanczos, không có sharpen.

Các script ở `_review/138/`: `prepare.py`, `select.py`, `finish.py`, `publish.py`, `repair_derived.py`, `verify.py`, `audit_delivery.py`, `sheets.py`, `replay.py`, `report.py`, `ka1.py`. Đa số script tạo tên mới và chặn ghi đè; **không chạy lại publish/repair trên bộ đã giao**. `replay.py` là lối chạy lại an toàn: đọc nguồn `.try1.png` và gamma đã chốt, tạo một thư mục mới `138/replay-<UTC>/`, tái tạo bốn khổ và so toàn bộ RGBA với bộ giao; không sửa bộ giao.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
PYTHONDONTWRITEBYTECODE=1 python3 games/dragon-hold/art-src/_review/138/replay.py
# Thêm check ở cuối để chạy riêng một icon.
```

Đã chạy lại riêng `check`, yêu cầu bốn khổ trùng toàn bộ RGBA. Font tờ xem: `/System/Library/Fonts/Supplemental/Arial.ttf`.

**Cần chủ dự án/Claude xem:** tờ cuối, đặc biệt `speaker` 14 px, `lock` 12 px, `camera-reset` và `sell` 16 px; chấm lại KA5/M. Chưa chép vào `public/`, đúng phân công của phiếu.
