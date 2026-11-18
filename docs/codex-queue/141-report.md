# Phiếu 141 · Wordwoven · Menu, âm lượng, hồ sơ

Ngày làm: 29/10/2026, repo cha trên Mac mini M4.

**Đã giao đủ 12 icon, 48 PNG ở bốn cỡ, 12 lượt sinh nguyên byte và prompt đi kèm. Kiểm kỹ thuật cuối đạt; tự chấm Q từ 9 ở 720p, M từ 8. Chờ Claude chấm lại từ 8 để nhận; chưa đưa vào `public/` hoặc gắn mã.**

## 1. Nơi giao và tham chiếu

- Ảnh và prompt: [ui/icons/](../../games/typing-defense/art-src/ui/icons/), đúng 12 tên trong bảng phiếu; mỗi tên có `.png`, `.256.png`, `.128.png`, `.64.png`, `.try1.png` và prompt tương ứng. Không sinh lượt 2, 3.
- Tờ xem bốn hàng: [141-sheet.jpg](../../games/typing-defense/art-src/_review/141-sheet.jpg), 4032 × 686. Hàng 1 là bản alpha ở 256 px; hàng 2 là 1080p trên hai nền; hàng 3 là 720p trên hai nền; hàng 4 có icon mới, bốn icon cũ và mảnh HUD chủ dự án, cùng khổ 40 px.
- Từng ảnh có [`<tên>-final-before-after.jpg`](../../games/typing-defense/art-src/_review/141/) và `<tên>-final-sizes.jpg`; tờ cỡ nhỏ giữ nguyên kích thước thật, không phóng giả 20–36 px. Tờ tổng rộng nên cần mở ở 100%, hoặc xem tờ riêng.
- Hồ sơ, script và số đo: [_review/141/](../../games/typing-defense/art-src/_review/141/).

Đã đính kèm trong **cả 12 lời gọi `image_gen`**: khung 115 `ui/frames-epic/panel-large.v2.alpha.png`, ảnh chủ đạo 113 `ui/title-epic/keyart.png`, tham chiếu chủ dự án `_refs/owner-epic-2026-10-28.webp`. Thư mục `ui/frames/` ghi trong phiếu không tồn tại; bộ 115 thực tế nằm ở `ui/frames-epic/`, vì vậy dùng đúng bộ đang có. Không sửa các ảnh tham chiếu.

Đối chiếu mức hoàn thiện HUD thương mại của ảnh chủ dự án: chất liệu, bevel, điểm sáng và nhận diện nhỏ **đứng cạnh được ở mức M 8–8,5**; không tự nhận ngang chất lượng ảnh mẫu M 9. Ở 20 px, cần Claude xem kỹ sáo, chiêng và cân.

## 2. Lượt sinh và hậu kỳ

Mọi prompt viết bằng tiếng Anh, bắt đầu bằng **STYLE-UI mới nguyên văn** trong chỉ đạo 28/10, rồi khối **ICON** của tài liệu định dạng. Phần bổ sung ghi rõ STYLE-UI mới thay nét mực/màu phẳng của ICON cũ và lề mới 70% thay 80%; không chép khối STYLE “storybook”. Nền M `#FF00FF`. Không có chữ, số, logo, huy hiệu nền hay khung UI bao ngoài; hoa văn khắc thuộc vật thể.

| Tên | Lượt chọn | Phần riêng đã khóa trong prompt lượt 1 | Sửa giữa các lượt |
| --- | --- | --- | --- |
| menu-start | try1 | Cổng đá vôi, mái son, hai cửa ngọc mở, đường bình minh trong vòm | Không có lượt sau |
| menu-continue | try1 | Sách trống mở, dải đánh dấu son lớn ở bên phải | Không |
| menu-settings | try1 | Tám răng đồng, mảng ngọc, lỗ trục lớn | Không |
| menu-learn | try1 | Sách trống, đèn đồng sáng hổ phách và sợi sáng trừu tượng | Không |
| menu-profile | try1 | Thẻ trống, bút ngọc chéo, ấn son hoa văn mây | Không |
| vol-master | try1 | Chiêng đồng tròn, núm giữa, quai ngọc và tia Đông Sơn | Không |
| vol-music | try1 | Sáo tre chéo, ba lỗ lớn, đúng hai nốt sáng | Không |
| vol-effects | try1 | Trống cầm tay thân son, mặt sáng và dùi chéo | Không |
| stat-speed | try1 | Ngựa chạy nghiêng phải, bốn chân và đuôi tách dáng | Không |
| stat-accuracy | try1 | Bia ngọc có vòng sáng, một tên vào đúng tâm từ trên phải | Không |
| stat-new-word | try1 | Mầm hai lá ngọc từ gáy sách mở | Không |
| stat-evenness | try1 | Cân đồng cân bằng, hai đĩa cùng cao, chân ngọc | Không |

Nguồn công cụ là 1254 × 1254; giữ nguyên byte ở `.try1.png`, không giả thành bản hậu kỳ. SHA-256 đối chiếu đủ **12/12 nguồn** trong `final-audit-v7.json`. Prompt chính xác nằm cạnh bản thử và cả bốn bản giao; có bản tổng `prompts.json`.

Hậu kỳ cuối chỉ làm các bước cho phép:

1. Loại họ màu khóa magenta; sửa RGB trong dải mép 3 px của nguồn bằng màu phần đặc gần nhất. Không phủ mảng hay thay chất liệu trong lòng tranh.
2. Cắt phần nền trống, thu Lanczos cho cạnh dài hộp alpha bằng 716 px, canh giữa canvas 1024². Không cắt mất bộ phận của vật.
3. Riêng **menu-settings và vol-master tăng RGB toàn ảnh 8%**, giữ alpha: tương phản nền ngọc ban đầu lần lượt khoảng 0,229 và 0,241, sau sửa vượt 0,25. Mười ảnh khác không chỉnh sáng. Không đổi gamma, không san phẳng hay thêm tranh bằng mã.
4. Thu từng cỡ 256, 128, 64 **trực tiếp từ bản 1024 bằng Lanczos**, không qua cỡ trung gian, không làm nét. Sau thu, kẹp alpha về 0/255 chỉ ở pixel ngoài dải mép 3 px; giữ nguyên RGB của phép thu. Kiểm đầu phát hiện tổng 209 pixel như vậy, chủ yếu alpha 1/254; đã sửa trên các tệp mới của phiếu rồi kiểm lại đủ 48 PNG.

Các thử nghiệm công cụ `process.py`, `process-v2.py` … `process-v6.py`, các bản ứng viên cũ và các kiểm đầu vẫn giữ để truy vết; **không phải bản nhận**. Pipeline cuối là `process-v7.py`, bộ đã đo là `candidates-v7/`; ảnh được xem và chấm là PNG cuối trong `ui/icons/`. Hoàn thiện lại chỉ các tệp do phiếu này vừa tạo; `finish-own-deliveries.py` khóa mọi tên trong MD5 trước và xác nhận bản đang có vẫn là bản ứng viên của phiếu trước khi viết. Không sửa tệp có trước mốc KA1, không xóa/đổi tên bản thử. `own-delivery-finalization.json` ghi từng đường dẫn và SHA-256.

Không gặp ngưỡng buộc phải phá phần vẽ. Vòng thử tách nền đầu của riêng menu-start để lại nền nhiễu; đã bỏ khỏi lựa chọn, giữ lại trong review để đối chiếu. Tờ xem nháp được lưu ở `141-sheet-draft.jpg`; `141-sheet.jpg` và `141-sheet-final.jpg` là tờ đã hoàn thiện.

## 3. Kiểm số cuối

`identify-final.txt` chứa đúng lệnh `magick identify -format '%f %wx%h %[channels]\n'` cho đủ 48 PNG. **12 bản 1024², 12 bản 256², 12 bản 128² và 12 bản 64², tất cả srgba.** `final-audit-v7.json`: 48/48 qua kiểm khổ, alpha, sót màu, ứng viên đã đo, prompt và phép thu trực tiếp kèm sửa mép alpha.

Định nghĩa đo: luma Y′ = 0,2126 R + 0,7152 G + 0,0722 B trên mã sRGB chuẩn hóa, trung bình theo alpha, không đổi màu ảnh để tính. Nền ngọc `#1f3b33`, đá vôi `#e8e1cf` theo phương án tạm trong phiếu; dùng cùng hai nền ở mọi tờ cỡ thật. Dải mép lấy từ mặt nạ alpha ≥ 128 bằng `morphology Edge Disk:3`; đây là kiểm chặt, bao gồm cả nhiễu alpha rất thấp. IoU thu 32² bằng Lanczos, ngưỡng alpha > 16, giữ nguyên canh giữa, kiểm đủ 66 cặp.

### 3.1 Hộp alpha và mép ở 1024²

| Ảnh | Cạnh dài (%) | Lệch tâm X/Y (%) | Alpha ngoài dải 3 px | Sót khóa / pixel alpha > 0 | Sót khóa (%) |
| --- | ---: | ---: | ---: | ---: | ---: |
| menu-start | 69.9219 | 0.0000 / 0.0000 | 0 | 0 / 368914 | 0.00000 |
| menu-continue | 69.9219 | 0.0000 / 0.0488 | 0 | 4 / 289290 | 0.00138 |
| menu-settings | 69.9219 | 0.0488 / 0.0000 | 0 | 44 / 332636 | 0.01323 |
| menu-learn | 69.9219 | 0.0000 / 0.0488 | 0 | 13 / 256691 | 0.00506 |
| menu-profile | 69.9219 | 0.0000 / 0.0488 | 0 | 22 / 282364 | 0.00779 |
| vol-master | 69.9219 | 0.0000 / 0.0000 | 0 | 0 / 328248 | 0.00000 |
| vol-music | 69.9219 | 0.0000 / 0.0488 | 0 | 4 / 139559 | 0.00287 |
| vol-effects | 69.9219 | 0.0000 / 0.0000 | 0 | 28 / 297367 | 0.00942 |
| stat-speed | 69.9219 | 0.0000 / 0.0488 | 0 | 13 / 178421 | 0.00729 |
| stat-accuracy | 69.9219 | 0.0000 / 0.0488 | 0 | 1 / 286037 | 0.00035 |
| stat-new-word | 69.9219 | 0.0000 / 0.0000 | 0 | 0 / 253317 | 0.00000 |
| stat-evenness | 69.9219 | 0.0000 / 0.0000 | 0 | 32 / 163267 | 0.01960 |

Ở **cả 48 PNG** sau sửa, alpha bán trong suốt ngoài dải 3 px = **0**. Sót khóa cao nhất kể cả bản thu là **0,06138%**, dưới 0,2%; bảng chi tiết từng tệp ở `final-audit-v7.json`.

### 3.2 Tương phản ở cỡ thật và dáng riêng

Mỗi ô tương phản là **ngọc tối / đá vôi sáng**. Cả 12 ảnh đạt ≥ 0,25 trên nền tối ở cả hai cỡ; không cần dựa vào nền sáng để qua.

| Ảnh | Cỡ 720p / 1080p | ΔY′ 720p (tối / sáng) | ΔY′ 1080p (tối / sáng) | IoU lớn nhất | So với |
| --- | --- | ---: | ---: | ---: | --- |
| menu-start | 24 / 36 | 0.3117 / 0.3656 | 0.3105 / 0.3668 | 0.7453 | vol-master |
| menu-continue | 24 / 36 | 0.3854 / 0.2919 | 0.3855 / 0.2918 | 0.6640 | vol-effects |
| menu-settings | 24 / 36 | 0.2610 / 0.4164 | 0.2605 / 0.4169 | 0.7930 | vol-master |
| menu-learn | 24 / 36 | 0.3723 / 0.3050 | 0.3732 / 0.3041 | 0.7893 | vol-master |
| menu-profile | 24 / 36 | 0.4057 / 0.2716 | 0.4062 / 0.2711 | 0.6991 | menu-start |
| vol-master | 20 / 24 | 0.2725 / 0.4048 | 0.2724 / 0.4049 | 0.7930 | menu-settings |
| vol-music | 20 / 24 | 0.2914 / 0.3859 | 0.2939 / 0.3834 | 0.4252 | menu-profile |
| vol-effects | 20 / 24 | 0.2837 / 0.3936 | 0.2837 / 0.3936 | 0.7242 | vol-master |
| stat-speed | 20 / 24 | 0.3520 / 0.3254 | 0.3515 / 0.3259 | 0.6341 | menu-continue |
| stat-accuracy | 20 / 24 | 0.3235 / 0.3539 | 0.3242 / 0.3531 | 0.6917 | menu-profile |
| stat-new-word | 20 / 24 | 0.3345 / 0.3428 | 0.3354 / 0.3420 | 0.6861 | menu-start |
| stat-evenness | 20 / 24 | 0.2574 / 0.4200 | 0.2574 / 0.4199 | 0.6099 | vol-master |

IoU lớn nhất **0.793017** (bánh răng / chiêng), dưới 0,80; bánh răng có lỗ trục, chiêng có mặt đặc. Không có cặp sáng/tắt trong phiếu. `metrics-v7.json` giữ đủ 66 cặp và số luma chưa làm tròn.

### 3.3 KA1

Đã chạy `md5 -r` trước khi ghi ảnh, lưu `md5-before.txt`, và chạy lại sau khi giao ở `md5-after.txt`; `md5-diff.txt` là diff 0 dòng ngữ cảnh. **318 tệp có trước giữ nguyên, 0 tệp mất hoặc đổi**. Bộ kê sau gồm 1247 tệp, tăng 929; `ka1-audit.json` xác nhận diff không có dòng nội dung bị bỏ. Ba tệp chính bảng kê sau, diff và kết quả audit không tự băm để tránh vòng tự tham chiếu. Cả ba tờ tổng và báo cáo này cũng có trong bảng kê sau.

## 4. KA5 và điểm M trên bản hậu kỳ

Thứ tự năm số: **Đúng đề · Đọc được · Hợp bộ · Hình khối · Dùng tiếp**, mỗi tiêu chí 0–2. Điểm “Dùng tiếp” = 2 chỉ sau khi kiểm cuối đạt. Đây là tự chấm; không thay điểm nhận của Claude.

| Ảnh | Năm điểm gốc | Q gốc | Năm điểm 720p | Q 720p | M gốc / 720p |
| --- | --- | ---: | --- | ---: | ---: |
| menu-start | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| menu-continue | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| menu-settings | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 2 / 2 / 2 / 2 | 10 | 8.5 / 8.5 |
| menu-learn | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| menu-profile | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1 / 2 / 2 / 2 | 9 | 8.5 / 8 |
| vol-master | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| vol-music | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1 / 2 / 2 / 2 | 9 | 8.5 / 8 |
| vol-effects | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| stat-speed | 1.5 / 2 / 2 / 2 / 2 | 9.5 | 1.5 / 1.5 / 2 / 2 / 2 | 9 | 8 / 8 |
| stat-accuracy | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| stat-new-word | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.5 / 8 |
| stat-evenness | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1 / 2 / 2 / 2 | 9 | 8.5 / 8 |

Các điểm còn hạn chế, ghi để Claude xem đúng chỗ:

- **menu-start:** Cổng và lối sáng rõ; phong cảnh trong vòm mất chi tiết ở 24 px.
- **menu-continue:** Sách mở và dải son tách nhau; hoa văn nhỏ chỉ còn thành mảng.
- **menu-settings:** Tám răng và lỗ trục vẫn rõ ở 24 px.
- **menu-learn:** Đèn sáng trên sách nhận ra; sợi sáng trong đèn không đọc riêng ở 24 px.
- **menu-profile:** Bút chéo và thẻ rõ; dấu son nhỏ cần xem trên nền sáng.
- **vol-master:** Mặt chiêng có núm và quai; ở 20 px dễ gần một huy chương, cần Claude xem.
- **vol-music:** Ống sáo chéo tách dáng; hai nốt sáng rất nhỏ ở 20 px.
- **vol-effects:** Mặt trống sáng, thân son và dùi chéo; trang trí đồng mất ở cỡ nhỏ.
- **stat-speed:** Ngựa đủ bốn chân; bản vẽ thêm mảng ngà và yên ngọc so với phù điêu vàng thuần trong đề.
- **stat-accuracy:** Bia, vòng sáng và tên vào tâm rõ; đuôi tên chỉ còn mảng ở 20 px.
- **stat-new-word:** Hai lá lớn và sách mở đọc được; gân lá mất khi thu.
- **stat-evenness:** Hai đĩa cùng cao và trụ giữa rõ; dây xích mảnh ở 20 px.

## 5. Chạy lại, khác phiếu và việc chờ

Script dùng Python chuẩn và ImageMagick 7, hỗ trợ `ART_MAGICK=/opt/homebrew/bin/magick`; font tờ xem là `/System/Library/Fonts/Supplemental/Arial.ttf`. Không cài thêm gói. Các script tạo mới từ chối ghi đè đầu ra để bảo vệ hồ sơ; muốn tái lập hậu kỳ, dùng một bản sao trống của bộ đầu ra trong phạm vi review, giữ nguồn và prompt. Không chạy lại bước hoàn thiện giao vào cây đã hoàn thiện.

Kiểm lại **chỉ đọc** ngay trong repo:

```sh
python3 games/typing-defense/art-src/_review/141/verify-live.py
python3 games/typing-defense/art-src/_review/141/process-v7.py measure
```

Pipeline: `save-generated.py` giữ nguồn và prompt; `process-v7.py prepare <tên> 1` tách nền, canh lề, thu; `process-v7.py measure` đo; `check-final-v7.py` kiểm trực tiếp bộ giao; `build-final-sheets.py` tạo tờ xem; `process-v7.py audit` lập MD5. Các script cũ giữ nguyên để truy vết, không dùng kết quả “pass” của bản cũ thay kết quả cuối.

Khác phiếu có chủ đích: dùng đường dẫn thực tế `frames-epic/` cho 115; nguồn sinh 1254² được chuẩn hóa thành 1024²; khối ICON cũ được ghi đè về **chỉ dẫn mỹ thuật** bằng STYLE-UI mới và lề 70%; thu Lanczos có sửa alpha mép sau thu. Nền kiểm dùng hai mã tạm mà phiếu đã cho, chưa tự lấy màu bất kỳ từ panel. Ngựa có mảng ngà/yên ngọc ngoài phù điêu vàng đã yêu cầu, nên trừ điểm Đúng đề và ghi riêng để Claude quyết. Không sửa prompt/sinh lại chỉ vì chi tiết phụ khi điểm vẫn đạt.

Không làm mã, âm thanh, public hoặc ảnh ngoài 12 tên vì ngoài phạm vi. Không sửa tài liệu nào ngoài báo cáo này; không chạy Git, build/test suite, game, dev server, trình duyệt, mạng ngoài `image_gen`; không đụng `.wt-*`, Tu Tiên hoặc game khác. Không có capture trình duyệt hay khung raw mới cần dọn.

**Chủ dự án cần xem:** tờ `141-sheet.jpg`, đặc biệt `vol-master`, `vol-music`, `stat-evenness` ở 20 px và bản ngựa. **Chờ Claude chấm lại M/Q từ 8; Claude mới chép vào `public/` khi gắn.**
