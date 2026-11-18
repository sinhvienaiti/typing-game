# Phiếu 139 · Dragonhold · Bản đồ và thẻ chữ

Ngày 29/10/2026. **Đã giao đủ 11 ảnh, 44 PNG thành phẩm và prompt kèm theo.** Toàn bộ kiểm số đo đạt; KA5 tự chấm thấp nhất **8,5/10** ở cỡ 720p, M thấp nhất **8/10**. **Chờ Claude chấm lại để nhận**, chưa chép vào `public/`.

## 1. File giao và phạm vi

- Nguồn và thành phẩm: `games/dragon-hold/art-src/ui/icons/`, đúng 11 tên của phiếu. Mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png` và prompt cạnh từng ảnh.
- 13 lượt sinh bằng **công cụ tích hợp `image_gen.imagegen`**: cầu và kéo cờ có hai lượt; chín ảnh còn lại một lượt. Giữ đủ 13 `.tryN.png` và 13 `.tryN.prompt.txt`; không xóa lượt nào.
- Hồ sơ, script và số đo: `games/dragon-hold/art-src/_review/139/`.
- Tờ xem: [139-sheet.jpg](../../games/dragon-hold/art-src/_review/139-sheet.jpg).
- Kiểm nền đất: [139-ground-v2.jpg](../../games/dragon-hold/art-src/_review/139-ground-v2.jpg). Bản đầu `139-ground.jpg` vẫn giữ, nhưng ô cắt thứ ba chạm HUD nên dùng bản v2.
- Báo cáo này là tài liệu duy nhất được ghi ngoài thư mục art của phiếu. Không chạy Git, build, bộ kiểm game, server, trình duyệt hoặc mạng ngoài công cụ sinh ảnh. Không đụng Tu Tiên, `.wt-*`, mã game, `public/` hay game khác.

## 2. Hướng mỹ thuật và lịch sử prompt

Mỗi prompt bắt đầu bằng **nguyên văn STYLE-UI Dragonhold** trong `ART_DIRECTION_2026-10-28.md` §3.2 / phiếu 119; sau đó là KIND–ICON, nội dung riêng và dòng nền G `#00FF00`. KIND bỏ hướng sách tranh cũ, dùng khối lớn, vật liệu có thể tích, cạnh rõ, lề 70%, không khung trang trí, chữ hay bóng đổ. Bệ đá, khung bẫy và lá cờ là chính vật được yêu cầu, không phải khung UI thêm sau vật.

Đã xem ảnh chủ dự án `games/typing-defense/art-src/_refs/owner-epic-2026-10-28.webp`, nhất là cụm kỹ năng và icon hệ thống; lấy mức hoàn thiện kim loại, độ sắc và ánh sáng, không chép nội dung. Đã xem `skill-fire-breath.png`, `gold.png`; hàng 4 tờ xem còn có `skill-sky-fire.png`, `dragon-heart.png`. Không có ảnh chọn 119 trong thư mục art lúc kiểm, nên chỉ dùng khối STYLE-UI đã có; không bỏ qua ảnh tham chiếu hiện hữu nào của 119.

| Ảnh | Lượt 1 | Sửa ở lượt 2 | Chọn |
|---|---|---|---|
| lane-bridge | Cầu đá cổ nhìn ngang, một vòm, granite kem và kim loại; quá dài và nhiều trang trí khi về 16 px. | Nhấn cầu cao, vòm mở lớn, năm khối đá lớn; bỏ đầu rồng, cột, cờ, lan can, huy hiệu. Không sửa màu để che vấn đề dáng. | 2 |
| lane-stream | Dòng nước trắng bạc chữ S, hai đá chéo nhau; dáng cao hẹp. | Không cần sinh lại. | 1 |
| lane-sky | Một cánh da tím đá phiến, ba thùy lõm lớn và xương bạc; không thân. | Không cần sinh lại. | 1 |
| slot-trap | Khung bẫy sắt vuông trên đất, bốn chốt góc, lòng đất tối. | Không cần sinh lại; sửa sáng bằng công cụ. | 1 |
| slot-house | Bệ móng granite tròn đặc, ba phiến lớn, một chốt sắt nhỏ. | Không cần sinh lại. | 1 |
| slot-hold | Cột cờ đứng trên chân đá nhỏ, cờ than hồng đuôi én. | Không cần sinh lại; sửa sáng bằng công cụ. | 1 |
| seal-lit | Một mảnh ấn tím, nứt phân nhánh phát sáng trong lòng, mép đá rõ; không hào quang ngoài. | Không cần sinh lại. | 1 |
| seal-unlit | Chỉnh trực tiếp từ `seal-lit.try1.png`: khóa dáng, mặt đá và vết nứt; tắt sáng, đổi lõi sang tím đá phiến xám, khe nứt tối. | Không cần sinh lại; đây là ảnh riêng với một lượt, không tính thành lượt 2 của ấn sáng. | 1 |
| flag-pull | Bàn tay kéo cán cờ Héo chéo khỏi đất; nắm tay còn nhỏ khi về 18 px. | Nắm tay chiếm nửa khối chính, khớp ngón sáng lớn; cờ và đất nhỏ lại, giữ hướng kéo chéo. | 2 |
| swarm | Đúng ba kiến gai thành cụm tam giác, giáp bạc xám, thân và chân tách bằng khoảng trống. | Không cần sinh lại; sửa sáng bằng công cụ. | 1 |
| edge-arrow | Đầu tên ngắn hướng phải, lõm chữ V bên trái, men than hồng và mặt sáng kem, không cán. | Không cần sinh lại. | 1 |

Prompt đầy đủ ở các `.tryN.prompt.txt`, bản chọn sao chép đúng prompt của lượt được chọn. `generation-manifest.json` ghi 13 lần gọi, đường dẫn nguồn công cụ và ảnh tham chiếu của bản ấn tắt.

## 3. Hậu kỳ và khổ

Nguồn tích hợp trả ảnh vuông 1254 px; giữ nguyên nguồn trong `.tryN.png`. Dùng thư viện chuẩn của `tools/art-normalize/normalize.py`, đặt **WORK vào `_review/139/scratch/`**, không ghi vào thư mục công cụ. Đã đặt `ART_MAGICK=/opt/homebrew/bin/magick`.

Quy trình: khóa G, chế độ global, despill bảo vệ lòng vật, bỏ sắc khóa; cắt theo alpha >16 có dự trữ mép, Lanczos về cạnh vật khoảng 717 px, căn giữa canvas 1024², xuất PNG32 8-bit sRGB. Alpha ≤8 về 0, ≥247 về 255; phần ngoài dải mép Euclid 3 px được đưa về 0/255. Pixel ngả xanh còn sót được trung hòa kênh G, không thay alpha.

Sửa sáng RGB của bản chọn: `slot-trap` gamma **1,30**, `slot-hold` **1,08**, `swarm` **1,30**. Các bản chọn khác gamma **1,00**. `flag-pull.try1` từng thử gamma 1,23 nhưng không được chọn; bản lượt 2 đủ sáng nên giữ 1,00. Chi tiết từng giai đoạn ở `corrections*.json`, `*.post.json`, `metrics-before-correction.json`, `metrics-final.json`.

Ba bản thu đều **Lanczos trực tiếp từ bản gốc 1024**, không qua chuỗi 256 →128 →64 và không làm nét. Kiểm thêm tất cả bản thu phát hiện ringing alpha và sắc xanh do nội suy: bản `swarm.256` trước sửa có 0,4800% pixel màu khóa. Đã làm sạch matte và despill sau phép thu, không đổi hình dáng hay làm nét. Giữ các bản xuất đầu và prompt trong `*.initial-delivery.*`; `reduction-repairs.json` ghi số pixel sửa. Chỉ sửa các bản thu mới do phiên này tạo, không sửa nguồn `.try` hoặc 213 file có sẵn trước phiếu.

`identify.txt` lưu nguyên kết quả lệnh `magick identify -format '%f %wx%h %[channels]\n'` cho 44 file. **11 bản 1024², 11 bản 256², 11 bản 128², 11 bản 64²; tất cả sRGBA, alpha 0–255**. ImageMagick 7.1.2 thêm trường số kênh `4.0` sau `srgba`; đây vẫn là RGBA bốn kênh. `delivery-verification-final.json` xác nhận khớp nguồn chọn hoặc đúng phép Lanczos trực tiếp + làm sạch matte, 44/44 đạt.

## 4. Số đo bắt buộc

KA1: `md5-before.txt` ghi 213 file icon có sẵn, trước lần ghi ảnh đầu tiên. Thư mục `_review/139/`, các JPG 139 và báo cáo chưa tồn tại khi bắt đầu. `md5-after.txt` bao gồm icon và toàn bộ hồ sơ mới, kể cả báo cáo; chỉ bỏ chính manifest sau và diff để tránh tự tham chiếu. `md5.diff` là kết quả `diff -u`; **không có dòng dữ liệu bị xóa hoặc đổi**, chỉ thêm. Có 114 file icon mới: 44 PNG giao, 44 prompt thành phẩm và 26 file của 13 lượt sinh. `ka1.json` ghi số lượng và xác nhận 213 file cũ giữ nguyên.

Luma dùng trọng số Rec.709 trên kênh sRGB chuẩn hóa (0,2126 R + 0,7152 G + 0,0722 B), trung bình vật có trọng số alpha tại đúng cỡ. Δ là trị tuyệt đối giữa luma vật và nền. Nền vỏ cây `#2b2118` có luma 0,1352; nền kem `#f1e3c4` có luma 0,8931. Mọi ảnh đạt Δ ≥0,25 trên **nền vỏ cây ở cả hai cỡ**.

| Ảnh | Cỡ 720/1080 | Cạnh dài bbox % | Lệch tâm % | Alpha lẻ ngoài mép 3 px¹ | Màu khóa %¹ | Δ vỏ cây 720/1080 | Δ kem 720/1080 |
|---|---|---:|---:|---:|---:|---|---|
| `lane-bridge` | 16/24 | 70.020 | 0.049 | 0 | 0.0000 | 0.3661/0.3756 | 0.3918/0.3823 |
| `lane-stream` | 16/24 | 70.117 | 0.098 | 0 | 0.0000 | 0.4763/0.4768 | 0.2815/0.2811 |
| `lane-sky` | 16/24 | 70.117 | 0.049 | 0 | 0.0000 | 0.2726/0.2743 | 0.4853/0.4836 |
| `slot-trap` | 24/36 | 69.922 | 0.000 | 0 | 0.0000 | 0.2778/0.2775 | 0.4801/0.4804 |
| `slot-house` | 24/36 | 70.020 | 0.049 | 0 | 0.0000 | 0.4997/0.5003 | 0.2582/0.2576 |
| `slot-hold` | 24/36 | 70.020 | 0.049 | 0 | 0.0000 | 0.2670/0.2659 | 0.4909/0.4920 |
| `seal-lit` | 10/14 | 70.020 | 0.098 | 0 | 0.0000 | 0.2702/0.2681 | 0.4877/0.4898 |
| `seal-unlit` | 10/14 | 70.020 | 0.049 | 0 | 0.0000 | 0.2612/0.2593 | 0.4967/0.4986 |
| `flag-pull` | 18/22 | 70.020 | 0.049 | 0 | 0.0000 | 0.2771/0.2765 | 0.4808/0.4814 |
| `swarm` | 18/22 | 70.020 | 0.049 | 0 | 0.0000 | 0.2595/0.2596 | 0.4984/0.4983 |
| `edge-arrow` | 10/14 | 69.922 | 0.000 | 0 | 0.0000 | 0.2698/0.2709 | 0.4881/0.4870 |

¹ Giá trị xấu nhất trong cả bốn file giao của từng ảnh: mọi pixel bán trong nằm trong dải mép 3 px; hue cách G ≤15°, S >0,5 và alpha >0 bằng 0 pixel. Không chỉ kiểm bản gốc. Dải mép được đo quanh mặt nạ alpha >127 bằng giãn/co Disk:3. Bbox dùng alpha >16, cạnh dài phải 68–72%, lệch tâm mỗi trục ≤2%.

IoU đo sau Lanczos từ gốc về **32×32**, mặt nạ alpha >16; không dịch, xoay hoặc co riêng để làm giảm trùng dáng. Bảng loại trừ cặp cùng vật sáng/tắt; 55 cặp đầy đủ nằm trong `metrics-final.json`.

| Ảnh | IoU lớn nhất với vật khác | Cặp gần nhất |
|---|---:|---|
| `lane-bridge` | 0.4851 | `slot-house` |
| `lane-stream` | 0.7293 | `seal-unlit` |
| `lane-sky` | 0.5437 | `swarm` |
| `slot-trap` | 0.7760 | `slot-house` |
| `slot-house` | 0.7760 | `slot-trap` |
| `slot-hold` | 0.4907 | `edge-arrow` |
| `seal-lit` | 0.7266 | `lane-stream` |
| `seal-unlit` | 0.7293 | `lane-stream` |
| `flag-pull` | 0.5240 | `swarm` |
| `swarm` | 0.6294 | `seal-unlit` |
| `edge-arrow` | 0.5112 | `seal-unlit` |

Cặp **seal-lit / seal-unlit = 0.996016**, đạt ≥0,95. IoU khác vật cao nhất **0,776000**, đạt ≤0,80.

Kiểm riêng trên mặt đất: `slot-trap`, `slot-house`, `slot-hold` được ghép đúng **24×24 px** lên ba mảnh 72×72 từ `sheet-04-words-crowd.jpg`, không phóng to nền; tọa độ ở `ground-crops.json`. Khung vuông, đĩa tròn và cột cờ phân biệt được; cả ba đọc được trên cỏ, cỏ có bóng và mép đường. Không phải ảnh chạy game mới.

Tờ xem bốn hàng: (1) bản gốc thu 256; (2) đúng cỡ 1080p trên vỏ cây và kem; (3) đúng cỡ 720p trên hai nền; (4) bốn icon cũ, mảnh HUD ảnh chủ dự án và sáu ảnh mới cùng khổ hiển thị 192 px để so chất liệu. Nhãn nằm ngoài ảnh, font Arial theo phiếu. Khoảng trống 70% của texture vẫn được giữ khi thu về cỡ game, không phóng riêng vật cho dễ đọc.

## 5. KA5 và điểm mức chợ

Tự chấm sau khi xem ảnh gốc, tờ xem và ảnh nền đất, theo mức hoàn thiện UI game thương mại cùng cụm HUD ảnh chủ dự án. **Đứng cạnh được ở mức phát hành 8–8,5**, chưa chấm ngang mức tham chiếu 9. Chất liệu và ánh sáng mới cao hơn bộ icon cũ; “Hợp bộ” 1,5 do phần art cũ của game còn giản lược hơn. Tại 10–18 px, chi tiết khắc mất đi; giữ điểm “Đọc được”/“Hình khối” thận trọng, không lấy ảnh phóng lớn thay cỡ thật.

Thứ tự năm số: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” chỉ nhận 2 sau khi toàn bộ kiểm số đo trên 44 file đạt.

| Ảnh | Năm điểm ở gốc | Q gốc | Năm điểm ở 720p | Q 720p | M gốc/720p |
|---|---|---:|---|---:|---|
| `lane-bridge` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `lane-stream` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 1,5 / 2 | 9 | 8.5/8.5 |
| `lane-sky` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `slot-trap` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 1,5 / 2 | 9 | 8.5/8 |
| `slot-house` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 8.5/8.5 |
| `slot-hold` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 1,5 / 2 | 9 | 8.5/8 |
| `seal-lit` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `seal-unlit` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `flag-pull` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `swarm` | 2 / 1,5 / 1,5 / 2 / 2 | 9 | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | 8.5/8 |
| `edge-arrow` | 2 / 2 / 1,5 / 2 / 2 | 9.5 | 2 / 2 / 1,5 / 1,5 / 2 | 9 | 8.5/8.5 |

Cần Claude xem kỹ độ đọc của `seal-lit`/`seal-unlit` ở 10 px và ba kiến ở 18 px; ở cỡ đó chỉ nhận khối/nhóm và trạng thái, không đọc được từng vết nứt hay từng chân. Cầu lượt 2 giữ vòm mở rõ hơn lượt 1; kéo cờ lượt 2 giữ nắm tay lớn hơn.

## 6. Tái lập và chỗ khác phiếu

Script đã dùng: `process.py`, `repair-reductions.py`, `verify.py`, `make-report.py`. Công cụ normalize chỉ được import, không sửa; bytecode Python bị tắt để không phát sinh file ngoài phạm vi. Script hậu kỳ có chặn tên tồn tại. `repair-reductions.py` là thao tác một lần, bảo vệ bằng baseline và SHA-256 của các bản mới trước sửa, giữ bản trước sửa trong hồ sơ.

Kiểm lại file giao, dùng một nhãn mới để không ghi đè bằng chứng:

```bash
python3 games/dragon-hold/art-src/_review/139/verify.py check-2
```

Tái lập toàn bộ từ các `.try` đã chọn vào thư mục con mới, không gọi sinh ảnh và không ghi lại file giao:

```bash
python3 games/dragon-hold/art-src/_review/139/replay.py replay-owner-1
```

`replay.py` dùng đúng hậu kỳ cuối, đo lại và so khớp RGBA với 11 bản gốc đã giao. Các bước tạo/đo/xuất/kiểm đã chạy trong phiên; không chạy thêm một bản replay toàn bộ chỉ để lặp lại cùng phép hậu kỳ.

Khác chi tiết phiếu và lý do:

- Công cụ sinh trả nguồn 1254², nên `.try` giữ nguyên nguồn; bản gốc **giao** được chuẩn hóa 1024² theo yêu cầu.
- Các bản thu có bước làm sạch alpha/despill **sau** Lanczos để cùng đạt chốt alpha sạch; không làm nét, không thu nối tiếp, không dùng sửa hình bằng mã để thay ảnh sinh.
- Không có ảnh chọn 119 để xem; đã dùng nguyên STYLE-UI của 119 và đầy đủ ảnh tham chiếu hiện có mà phiếu nêu.
- Giữ cả ảnh kiểm nền đất ban đầu và bản v2; bản v2 tránh HUD. Đây là ghép lên ảnh chụp có sẵn, không mở game.

Không bỏ ảnh nào. Chưa gắn vào runtime và chưa chép vào `public/` vì phần này thuộc Claude sau khi chấm lại ≥8. Không coi điểm tự chấm là quyết định nhận của Claude.
