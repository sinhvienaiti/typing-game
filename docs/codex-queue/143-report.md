# Phiếu 143 · Wordwoven · Người làng, lính, ruộng, trạng thái

Ngày báo cáo: 30/10/2026. Làm tại repo cha trên macOS, bằng **`image_gen` tích hợp**.

**Chưa hoàn tất phiếu.** Đã giao đủ 10 bản tốt nhất hiện có, mỗi bản có PNG 1024² RGBA, ba bản thu 256/128/64 và prompt. Cả 10 qua kiểm số. **Năm chân dung chưa đạt kiểm mắt ở 24 px**, M tại cỡ 720p chỉ 7,5; chưa được coi là ảnh đã duyệt. Năm icon tự chấm M/Q từ 8, chờ Claude chấm lại. Không chép ảnh vào `public/`.

Đã chuẩn bị prompt sửa bố cục mặt cho cả năm chân dung. Lệnh sinh `farmer` lượt 2 bị công cụ từ chối **HTTP 429 · `usage_limit_reached`**, không trả ảnh. Không gọi tiếp bốn chân dung còn lại và không chuyển sang CLI/API ngoài. Công cụ báo mốc mở lại **19:47:25 ngày 30/10/2026, giờ Việt Nam**; đây là thời điểm do công cụ trả về, không phải cam kết lượt sinh sau sẽ thành công. Hồ sơ: `generation-limit.json`.

## 1. File giao và phạm vi

- Năm chân dung: [portraits/units/](../../games/typing-defense/art-src/portraits/units/): `farmer`, `villager`, `builder`, `miner`, `soldier` — bản tốt nhất để xem, **còn lỗi mắt ở cỡ nhỏ**.
- Năm icon: [ui/icons/](../../games/typing-defense/art-src/ui/icons/): `rice-ripe`, `rice-growing`, `rice-empty`, `status-burn`, `status-stun`.
- Mỗi tên có `<tên>.png`, `.256.png`, `.128.png`, `.64.png`; từng PNG có `.prompt.txt` cùng tên. Danh sách 80 file giao ở [published-files.json](../../games/typing-defense/art-src/_review/143/published-files.json).
- Mọi bản sinh và prompt lượt thử giữ nguyên. Tổng **12 ảnh sinh thành công**: 10 lượt 1, thêm lượt 2 cho `rice-growing` và `status-burn`. SHA-256 của 12 bản thử trùng nguyên byte nguồn công cụ; xem `source-audit.json`.
- Năm `.try2.prompt.txt` của chân dung là **prompt dự kiến sửa, chưa có ảnh tương ứng**. Chỉ `farmer` được gọi rồi thất bại do hạn mức; bốn prompt còn lại chưa được gọi. Không đếm các prompt này là năm lượt sinh thành công.

Không chạy lệnh Git, build/test game, dev server, trình duyệt, mạng ngoài `image_gen`; không đọc/ghi Tu Tiên hoặc `.wt-*`; không sửa runtime, tài liệu khác, âm thanh hay game khác. Không có capture trình duyệt cần dọn. Không sửa/xóa tài nguyên có trước phiếu.

## 2. Tham chiếu và prompt

Đã đọc `ART_ACCEPTANCE.md` §2.2, §5, chỉ đạo mỹ thuật 28/10, phiếu 115, định dạng ICON/PORTRAIT và README `tools/art-normalize`. Đã xem ảnh mẫu HUD thương mại của chủ dự án.

Đường dẫn `ui/frames/` trong phiếu không tồn tại; bộ 115 thực tế nằm ở **`ui/frames-epic/`**. Đã đính kèm `panel-large.v2.png` và ảnh chủ đạo `ui/title-epic/keyart.png` của 113 vào mọi lượt sinh thành công. Vì bộ 115 đã có nên không cần chờ.

Mỗi prompt bắt đầu bằng STYLE-UI nguyên văn của 115, tiếp theo KIND nguyên văn, nội dung riêng và dòng nền M `#FF00FF`. Có chỉ dẫn hiện hành ghi rõ việc bỏ viền mực của KIND cũ, giữ nét vẽ tự nhiên, vật chiếm 70% canvas, lề 15%, không chữ/khung/nền cảnh. Không dùng STYLE “storybook” cũ. Prompt nguyên văn nằm cạnh ảnh; `prompts.json` là danh mục lượt 1. Prompt được sửa ở lượt 2 nằm ở đúng file `.try2.prompt.txt`, không gán lại prompt lượt 1 cho ảnh lượt 2.

| Tên | Ảnh nguồn model đính kèm thêm | Lượt giữ / chọn và sửa prompt |
| --- | --- | --- |
| `farmer` | `workers/worker-base.png`, `worker-kit-ma-head.png` | try1; giữ nón, dây buộc, bím tóc, áo kem; thêm liềm theo đề. Prompt try2 dự kiến phóng lớn mặt, giảm vai và nón, giữ liềm nhỏ; lệnh sinh bị 429, không có try2 PNG. |
| `villager` | `workers/worker-base.png` | try1; áo kem, tóc và mặt theo base, đòn gánh theo đề. Prompt try2 đã soạn, chưa gọi do hạn mức. |
| `builder` | `workers/worker-base.png` | try1; băng đầu son, búa và tạp dề theo đề, không tự nhận là bộ dụng cụ model đã có. Prompt try2 đã soạn, chưa gọi. |
| `miner` | base, `worker-kit-miner-head.png`, `worker-kit-miner-pickaxe.png` | try1; giữ mũ nâu, đèn đồng, cuốc. Prompt try2 đã soạn, chưa gọi. |
| `soldier` | `units/linh-giao.png`, `linh-giao-spear.png`, `linh-khien-shield.png` | try1; giữ nón nhọn, áo chàm, dải lam và đĩa đồng; thêm khiên tròn theo đề. Prompt try2 đã soạn, chưa gọi. |
| `rice-ripe` | 115 + 113 | try1; một cây lúa vàng trĩu. Hạt cách điệu lớn, ghi hạn chế ở bảng điểm. |
| `rice-growing` | 115 + 113 | try1 lá quá rộng; **chọn try2**, sửa thành Oryza sativa với năm lá dài hẹp ít nhất 8:1, gốc/rễ gọn. |
| `rice-empty` | 115 + 113 | try1; ô ruộng ngập nước, bờ đất, lỗ gieo giữa. |
| `status-burn` | 115 + 113 | try1 sai đề: công cụ chép rồng từ key art. **Chọn try2**, nhấn mạnh chỉ một ngọn lửa, tham chiếu chỉ dùng màu, loại toàn bộ nhân vật/rồng/giáp/cánh. |
| `status-stun` | 115 + 113 | try1; ba sao vàng, ba vệt chuyển động, tâm rỗng. |

## 3. Hậu kỳ và bảo toàn tranh

Nguồn công cụ là **1254 × 1254**; `.try*.png` giữ nguyên. Bản chọn được tách M bằng bản sao nguyên trạng của `key-alpha.sh`, `common.sh`, `normalize.py`, `seam_analysis.py` nằm trong review, để WORK không ghi ra ngoài phạm vi phiếu. Các băm công cụ được lưu trong nhật ký phiên; không sửa công cụ gốc.

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
bash games/typing-defense/art-src/_review/143/art-normalize/key-alpha.sh   SOURCE.tryN.png KEY.png --bg '#FF00FF' --mode global --despill protect-interior
magick KEY.png -trim +repage -filter Lanczos -resize 716x716   -gravity center -background none -extent 1024x1024   -colorspace sRGB -alpha on -depth 8 -define png:color-type=6 MASTER.png
```

Các bản 256/128/64 đều thu Lanczos **trực tiếp từ master**. Không làm nét bản 64. Không thay phần vẽ, không phủ màu phẳng, không cắt bỏ thành phần alpha có nội dung, không dùng chỉnh gamma/độ sáng để ép tương phản. Ảnh chân dung được giữ dạng bust có sẵn; không vẽ thêm vòng và không cắt bỏ vai/dụng cụ để giả tăng cỡ mặt.

`polish.py` sửa riêng alpha phân số ngoài dải mép Disk:3 quanh alpha 50%: sai số ≤5/255 ở nền trống về 0; phần có sơn còn lại về 255 để giữ nét mảnh, không xóa nó. RGB phần có sơn giữ nguyên. Số pixel và toàn bộ tọa độ nằm trong `*-alpha-polish*.json`; các thay đổi alpha lớn hơn 5 được công khai ở bảng dưới. Đây là sửa matte, không san phẳng màu hoặc chi tiết tranh.

Lượt thử đầu `finish.py` dùng mép alpha>16 bị dừng bởi guard; không xuất ảnh kết quả. Giữ `farmer-alpha-unresolved.json` để truy vết; script đó không phải bước giao cuối.

Riêng lúa non try2 có **0,251266%** pixel sắc M sau tách lần đầu, vượt 0,2%. Chạy lại key với `--no-key-hue` theo hướng dẫn công cụ, alpha không đổi: 14.837 pixel RGB nhìn thấy thay đổi, 3.416 pixel trong số đó có alpha 255; delta RGB trung bình trên pixel đổi 9,794/255, cực đại 255 ở viền có alpha thấp. Đây là khử sắc khóa, không phủ màu vật. Tờ raw/post cuối giữ được vân lá, rễ và độ sáng; số cuối **0,112943%**, đạt. Có `despill-audit.json`, `rice-growing-despill-delta.json` và bản trước sửa để so. Không coi số 0,251266% là đã đạt.

| Tên | Pixel sửa alpha | Pixel nét mảnh khôi phục alpha >5 và <250 | Sai số alpha lớn nhất /255 |
| --- | ---: | ---: | ---: |
| `farmer` | 29 | 2 | 232 |
| `villager` | 72 | 0 | 5 |
| `builder` | 102 | 12 | 236 |
| `miner` | 10 | 0 | 2 |
| `soldier` | 14 | 0 | 1 |
| `rice-ripe` | 107 | 4 | 70 |
| `rice-growing` | 68 | 9 | 249 |
| `rice-empty` | 1 | 0 | 1 |
| `status-burn` | 5 | 0 | 1 |
| `status-stun` | 28 | 0 | 1 |

## 4. KA1 · Băm trước/sau

Phạm vi: mọi file đệ quy trong hai thư mục đích tài nguyên `portraits/units/` và `ui/icons/`; thư mục chân dung chưa tồn tại khi bắt đầu. Hồ sơ review và báo cáo tự sinh không nằm trong hai thư mục băm này.

| Mục | Số |
| --- | ---: |
| File trước | 518 |
| File sau | 627 |
| Dòng thêm | 109 |
| Dòng cũ bị mất/thay đổi | 0 |
| Dòng `<` trong diff | 0 |

109 file thêm gồm 24 file ảnh/prompt của 12 lượt thành công, 5 prompt chân dung lượt 2 chưa có ảnh và 80 file giao. Chạy `/sbin/md5 -r` từng file, sắp đường dẫn, `diff` chỉ thêm dòng. Hồ sơ: `md5-before.txt`, `md5-after.txt`, `md5.diff.txt`, `md5-audit.json`. `publish.py` kiểm bản giao trùng SHA-256 với đúng ứng viên đã đo.

## 5. Khổ, alpha, lề và dáng

Đủ **40 PNG giao**: 10 master **1024²**, 10 bản **256²**, 10 bản **128²**, 10 bản **64²**; tất cả sRGB RGBA 8-bit. ImageMagick 7 hiện in kênh là `srgba 4.0`; phần `4.0` là thông tin số kênh, không phải sai định dạng. Đầu ra nguyên văn của lệnh `identify -format '%f %wx%h %[channels]\n'` nằm ở `metrics-final-v2-identify.txt`.

Dải mép: Disk:3 quanh mặt nạ alpha>127; ngoài dải này, đếm mọi pixel 0<alpha<255. Tỷ lệ sắc M: hue cách 300° không quá 15°, S>0,5, trên mọi pixel alpha>0. Hộp bao dùng alpha>16. IoU dùng master thu Lanczos 32², alpha>16; JSON có thêm kết quả alpha>127 để kiểm độ nhạy, không chỉ báo ngưỡng có lợi.

| Tên | Alpha min/max | Alpha phân số ngoài mép 3 px | Pixel sắc M (%) | Cạnh dài hộp bao (%) | Lệch tâm max (%) | IoU lớn nhất / ảnh kia |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `farmer` | 0/255 | 0 | 0.029323 | 69.9219 | 0.0488 | 0.779661 / `miner` |
| `villager` | 0/255 | 0 | 0.027484 | 69.9219 | 0.0488 | 0.793103 / `builder` |
| `builder` | 0/255 | 0 | 0.032622 | 69.9219 | 0.0000 | 0.793103 / `villager` |
| `miner` | 0/255 | 0 | 0.017438 | 69.9219 | 0.0488 | 0.779661 / `farmer` |
| `soldier` | 0/255 | 0 | 0.031632 | 69.9219 | 0.0488 | 0.730047 / `builder` |
| `rice-ripe` | 0/255 | 0 | 0.136751 | 69.9219 | 0.0000 | 0.587678 / `farmer` |
| `rice-growing` | 0/255 | 0 | 0.112943 | 69.9219 | 0.0000 | 0.437229 / `status-burn` |
| `rice-empty` | 0/255 | 0 | 0.084025 | 69.9219 | 0.0000 | 0.514493 / `status-burn` |
| `status-burn` | 0/255 | 0 | 0.013770 | 69.9219 | 0.0000 | 0.514493 / `rice-empty` |
| `status-stun` | 0/255 | 0 | 0.091270 | 69.9219 | 0.0000 | 0.471698 / `farmer` |

Tất cả đạt ngưỡng alpha, sắc khóa ≤0,2%, hộp bao 68–72%, lệch tâm ≤2%, IoU ≤0,80. Không có cặp bật/tắt cùng vật trong phiếu này. Cặp sát nhất `villager`–`builder` = 0,793103; cần Claude xem thêm dáng ở cỡ nhỏ, không chỉ dựa số.

## 6. Tương phản và kiểm chân dung

Hai nền lấy trực tiếp từ `panel-large.v2.png` của 115: **ngọc `#051e15`**, **đá vôi `#b6a68c`**. Lấy trung vị R/G/B trong vùng ngọc `(491,476,200,200)` và dải đá `(550,60,80,40)` theo `(x,y,w,h)`; không dùng màu tạm khi đã có bộ 115. Định nghĩa luma: Rec.709 trên giá trị sRGB chuẩn hóa 0–1, trung bình có trọng số alpha trong vật, sau đó lấy trị tuyệt đối so với nền phẳng. Đây là luma hiển thị, không gọi là WCAG hoặc luminance tuyến tính.

| Tên | Cỡ 720 / 1080 | Δ luma ngọc 720 / 1080 | Δ luma đá 720 / 1080 |
| --- | --- | --- | --- |
| `farmer` | 24 / 29 | 0.3894 / 0.3891 | 0.1733 / 0.1736 |
| `villager` | 24 / 29 | 0.4243 / 0.4243 | 0.1384 / 0.1384 |
| `builder` | 24 / 29 | 0.3791 / 0.3793 | 0.1836 / 0.1834 |
| `miner` | 24 / 29 | 0.3931 / 0.3930 | 0.1696 / 0.1697 |
| `soldier` | 24 / 29 | 0.3033 / 0.3028 | 0.2594 / 0.2599 |
| `rice-ripe` | 20 / 24 | 0.4259 / 0.4251 | 0.1368 / 0.1376 |
| `rice-growing` | 20 / 24 | 0.4687 / 0.4700 | 0.0940 / 0.0927 |
| `rice-empty` | 20 / 24 | 0.4042 / 0.4060 | 0.1585 / 0.1567 |
| `status-burn` | 16 / 20 | 0.4883 / 0.4888 | 0.0744 / 0.0739 |
| `status-stun` | 16 / 20 | 0.5131 / 0.5159 | 0.0496 / 0.0468 |

Cả 10 đạt Δ luma ≥0,25 trên nền ngọc ở cả hai cỡ; nhỏ nhất là soldier 1080p = 0,3028. Có dựng thêm năm chân dung ở **20/24 px trong thẻ**, không bỏ cỡ này khỏi hồ sơ.

Vùng mặt được đánh dấu tay trên nguồn, biến đổi bằng đúng phép trim/fit vào master; kiểm bốn góc ROI nằm trong vòng r=0,45 cạnh ảnh. Đây là kiểm ROI thủ công, không giả nhận diện khuôn mặt tự động. Số ở `face-check.json`.

| Chân dung | Bán kính xa nhất của góc ROI mặt | Mặt trong r=0,45 | Mắt rõ ở 24 px | Đồ nghề ở 24 px |
| --- | ---: | --- | --- | --- |
| `farmer` | 0.2780 | Có | **Không đủ rõ** | Có |
| `villager` | 0.2771 | Có | **Không đủ rõ** | Có |
| `builder` | 0.2834 | Có | **Không đủ rõ** | Có |
| `miner` | 0.1776 | Có | **Không đủ rõ** | Có |
| `soldier` | 0.2512 | Có | **Không đủ rõ** | Có |

Đây là điểm **chưa đạt**, không được dùng độ rõ ở 54 px hay bản lớn để thay kết luận ở 24 px. Năm chân dung đặt cạnh `portraits/draconis.png` đúng 54 px cho thấy ánh vàng, khối mặt và chất liệu cùng hướng; Draconis có quy mô khuôn mặt lớn hơn vì ảnh cũ phủ gần đầy canvas. Bản xem Draconis chỉ tách G tạm trong bộ dựng tờ, không sửa file gốc.

## 7. KA5 trên bản hậu kỳ và điểm M

Thứ tự Q: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Chấm trên PNG hậu kỳ và cỡ 720p thật. “Dùng tiếp” của chân dung chỉ 1 vì kiểm mắt chưa đạt; không tự cộng thành 2 nhờ các kiểm số đã đạt. M so với mức hoàn thiện HUD thương mại của ảnh chủ dự án, không chấm theo tranh nguồn nội bộ.

| Ảnh | M 1024 / 720p | Q 1024 | Q 720p | Kết luận và thiếu gì |
| --- | --- | --- | --- | --- |
| `farmer` | 8.5 / 7.5 | 9 = 2/2/2/2/1 | 8 = 2/1/2/2/1 | **Chưa đạt**. Mặt tốt ở cỡ lớn; mắt không đủ rõ ở 24 px. |
| `villager` | 8.5 / 7.5 | 9 = 2/2/2/2/1 | 8 = 2/1/2/2/1 | **Chưa đạt**. Đòn gánh rõ; mắt không đủ rõ ở 24 px. |
| `builder` | 8.5 / 7.5 | 9 = 2/2/2/2/1 | 8 = 2/1/2/2/1 | **Chưa đạt**. Búa và băng đầu rõ; mắt không đủ rõ ở 24 px. |
| `miner` | 8.5 / 7.5 | 9 = 2/2/2/2/1 | 8 = 2/1/2/2/1 | **Chưa đạt**. Cuốc và đèn nhận ra; mắt không đủ rõ ở 24 px. |
| `soldier` | 8.5 / 7.5 | 9 = 2/2/2/2/1 | 8 = 2/1/2/2/1 | **Chưa đạt**. Giáo, khiên và áo chàm rõ; mặt nhỏ nhất bộ. |
| `rice-ripe` | 8 / 8 | 9 = 1/2/2/2/2 | 9 = 1/2/2/2/2 | Tự chấm đạt, chờ Claude. Hạt được phóng đại, hơi giống ngũ cốc chung; dáng trĩu vẫn rõ. |
| `rice-growing` | 8 / 8 | 9 = 2/2/1/2/2 | 8 = 2/1/1/2/2 | Tự chấm đạt, chờ Claude. Lá hẹp đúng lúa; ở 20 px chi tiết rễ mất, phong cách hơi sáng. |
| `rice-empty` | 8 / 8 | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | Tự chấm đạt, chờ Claude. Đọc được ô ruộng ướt; lỗ gieo hạt rất nhỏ ở 20 px. |
| `status-burn` | 8 / 8 | 9 = 2/2/1/2/2 | 9 = 2/2/1/2/2 | Tự chấm đạt, chờ Claude. Lửa rõ ở 16 px; mức vẽ đơn giản hơn nhóm ngọc/đồng. |
| `status-stun` | 8.5 / 8 | 10 = 2/2/2/2/2 | 9 = 2/1/2/2/2 | Tự chấm đạt, chờ Claude. Ba điểm sao còn đọc được; cạnh sao nhỏ không tách rõ ở 16 px. |

**So với tham chiếu:** năm icon đứng cạnh được ở mức M=8; năm chân dung đứng cạnh được ở 54 px và cỡ lớn, **chưa** ở cỡ 24 px. Không tuyên bố toàn phiếu đạt hoặc đã được Claude nhận. Không có người chấm độc lập trong lượt này.

## 8. Tờ xem và bản sinh | bản hậu kỳ

**Dùng bộ có hậu tố `-final` để duyệt.** Tờ không hậu tố đã được dựng trong lần kiểm sơ bộ trước khi khử viền lúa non; giữ lại để không ghi đè file đã tạo. Đây là sai khác tên tờ cuối so với phiếu, được ghi rõ thay vì coi tờ sơ bộ là bằng chứng cuối.

- [Tờ bốn hàng cuối — 143-sheet-final.jpg](../../games/typing-defense/art-src/_review/143-sheet-final.jpg): master ở 256 px; 1080p trên hai nền; 720p trên hai nền; bốn icon `build`, `upgrade`, `hire-villager`, `seeds` có sẵn và mảnh HUD chủ dự án cùng cao 64 px. Tờ tên yêu cầu [143-sheet.jpg](../../games/typing-defense/art-src/_review/143-sheet.jpg) được giữ như hồ sơ sơ bộ.
- [Tờ contact cuối](../../games/typing-defense/art-src/_review/143-contact-final.jpg).
- [Cỡ 720p phóng nearest ×6](../../games/typing-defense/art-src/_review/143-tiny-final.jpg): chỉ để thấy lưới pixel; ảnh native thật vẫn có trong tờ bốn hàng.
- [Cỡ thẻ 20/24 px](../../games/typing-defense/art-src/_review/143-cards-final.jpg).
- [Năm chân dung + Draconis ở 54 px](../../games/typing-defense/art-src/_review/143-portraits-54-final.jpg).
- [Mười cặp bản sinh | bản hậu kỳ cuối](../../games/typing-defense/art-src/_review/143-raw-post-final.jpg).
- Từng cặp **512 px mỗi phía**: [final-review/](../../games/typing-defense/art-src/_review/143/final-review/), các file `<tên>-raw-post.jpg`; prompt nguồn nguyên văn ở cạnh từng cặp. Không chỉ xem tờ gộp thu nhỏ để duyệt bảo toàn tranh.

## 9. Script và chạy lại

Mọi script đã dùng nằm trong [_review/143/](../../games/typing-defense/art-src/_review/143/), dùng Python chuẩn và ImageMagick 7, không cần thư viện cài thêm:

- `prepare.py`: trích nguyên văn STYLE/KIND và ghi prompt/danh mục lượt 1.
- `process.py`: key, trim, Lanczos, thêm lề; hỗ trợ `process(name, trial)`.
- `measure.py`: phép đo ban đầu; `verify.py`: kiểm bộ cuối với màu thật lấy từ 115.
- `finish.py`: phép thử có guard đã dừng, giữ để truy vết; **không dùng kết quả của bước này để giao**.
- `polish.py`: sửa matte, ghi từng pixel alpha sửa; `rekey-rice-growing.py`: bước khử viền bổ sung, giữ cả bản trước sửa.
- `sheets.py`, `render-final.py`: tờ cỡ thật, raw/post, thẻ, tham chiếu thương mại; dùng font Arial hệ thống đúng phiếu.
- `face-check.py`: ROI mặt và kết luận kiểm mắt/dụng cụ.
- `publish.py`: công bố tên mới độc quyền, kiểm SHA-256, băm MD5 trước/sau, kiểm bản sinh.
- `write-report.py`: báo cáo này từ JSON và đánh giá nhìn trực tiếp.

Chạy lại **kiểm đọc**, ghi vào tên JSON mới, không sinh ảnh, không ghi đè hồ sơ:

```sh
PYTHONDONTWRITEBYTECODE=1 python3   games/typing-defense/art-src/_review/143/verify.py   recheck-owner-01.json games/typing-defense/art-src/_review/143/final-v2
```

Các bước sinh dẫn xuất từ đầu từ chối thư mục/tên đã có; muốn dựng lại toàn bộ phải dùng một thư mục review mới, không xóa/bỏ bản thử. Nguồn công cụ được ghi ở `generation-records*.json`. Không dùng script kiểm để gọi lại dịch vụ sinh ảnh.

## 10. Phần còn lại và việc chủ dự án cần xem

1. **Sửa năm chân dung cho mắt rõ ở 24 px**. Đã soạn prompt đầu to, vai gọn, hai mắt lớn; chưa có ảnh mới do hạn mức công cụ. Không thể giải quyết bằng thu/phóng toàn ảnh vì lề 68–72% đã khóa; cắt bỏ nón/dụng cụ hay vẽ mắt bằng mã sẽ phá đề và trái luật hậu kỳ. Vì vậy dừng phần sửa này, giữ tranh đẹp và ghi mâu thuẫn giữa cỡ mặt hiện có với cỡ dùng thật.
2. **Claude chấm lại năm icon**, nhất là `rice-ripe` (hạt hơi giống ngũ cốc chung), `rice-growing` ở 20 px và ba sao của `status-stun` ở 16 px. Chưa có nghiệm thu hay gắn vào `public/`.
3. Chủ dự án nên xem [tờ tiny cuối](../../games/typing-defense/art-src/_review/143-tiny-final.jpg) và các raw/post đầy đủ. Không dùng điểm bản lớn để bỏ qua lỗi mắt ở 24 px.

Không tuyên bố đạt điều kiện “xong khi” của toàn phiếu. Phần chờ là chất lượng chân dung ở cỡ thật và chấm nhận độc lập, không phải build/test game hoặc quyền ghi file.
