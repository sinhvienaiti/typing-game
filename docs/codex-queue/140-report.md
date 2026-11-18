# Phiếu 140 · Dragonhold · Kết quả

**Ngày:** 29/10/2026. **Trạng thái:** đã giao đủ ảnh và hồ sơ; **chưa đủ điều kiện đóng phiếu** vì `star-unlit` thiếu tương phản trung bình trên nền tối. Giữ tranh theo ART_ACCEPTANCE §5, chờ Claude quyết ngoại lệ và chấm lại. Không tự nhận thay Claude.

## 1. Đã làm

- 10 icon mới trong `games/dragon-hold/art-src/ui/icons/`: `star-lit`, `star-unlit`, `stat-accuracy`, `stat-new-words`, `stat-words-seen`, `retry`, `easier`, `status-learned`, `status-review`, `status-new`.
- Mỗi tên có bản chọn `.png` 1024 × 1024 sRGBA, ba bản Lanczos trực tiếp `.256.png`, `.128.png`, `.64.png`; không làm nét. Tổng 40 PNG giao.
- Giữ đủ 10 `.try1.png` và 10 `.try1.prompt.txt`; bản chọn và từng bản thu có prompt cạnh ảnh. Tổng 100 file mới ở thư mục icon. Không có lượt 2 hoặc 3.
- Công cụ sinh: **image_gen tích hợp**, mỗi ảnh một lời gọi. `star-unlit` là lượt sửa riêng lấy `star-lit.try1.png` làm ảnh nguồn. Không dùng API hay mạng ngoài công cụ này.
- Tờ xem: [140-sheet.jpg](../../games/dragon-hold/art-src/_review/140-sheet.jpg). Mười tờ so [bản sinh | bản hậu kỳ](../../games/dragon-hold/art-src/_review/140/delivery/) ở cùng cỡ 512 px; bản hậu kỳ là bản giao cuối.
- Script, prompt nguyên văn, nguồn sinh và bằng chứng nằm trong [_review/140/](../../games/dragon-hold/art-src/_review/140/).

## 2. Prompt và các lượt

Mỗi prompt mở đầu bằng **STYLE-UI nguyên văn** ở ART_DIRECTION_2026-10-28 §3.2 / phiếu 119. Khối ICON lấy yêu cầu một vật, dáng rõ, tương phản và cấm chữ của định dạng Dragonhold, cập nhật lề 70%, chính diện và mỹ thuật sử thi theo phiếu này. Không dùng câu phong cách sách tranh cũ. Nền khóa M `#FF00FF` cho cả bộ; không có sắc M được chủ đích vẽ trong vật.

Đã xem `skill-fire-breath.png`, `gold.png` và HUD của ảnh chủ dự án trong Wordwoven. Không có ảnh chọn 119 tại thời điểm đọc; dùng khối STYLE-UI đã ban hành, không chờ phiếu khác. Tham chiếu chỉ lấy mức chất liệu và độ hoàn thiện.

| Ảnh | Lượt 1: phần riêng, mục tiêu hình dáng | Sửa prompt lượt sau |
|---|---|---|
| star-lit | Sao năm cánh vàng búa, mặt vát lớn, lõm cam, đúng năm mũi và rãnh chữ V | Không; giữ lượt 1 |
| star-unlit | Sửa từ sao vàng, giữ đúng đường bao và mặt vát; sắt tối, tắt lửa, gờ thép | Không; giữ lượt 1 |
| stat-accuracy | Bia đá kem, tâm tối, cán tên chẻ thành hai nhánh có lông; tên nhô chéo khỏi bia | Không; giữ lượt 1 |
| stat-new-words | Sách mở rộng, rãnh gáy tối, ánh than trong giấy, rãnh góc cạnh phi ngôn ngữ | Không; giữ lượt 1 |
| stat-words-seen | Ba bia đá dày xếp lệch bậc, rãnh đục không thành chữ, đai sắt và cạnh vàng | Không; giữ lượt 1 |
| retry | Mũi tên than dạng C, đầu tên lớn, khoảng rỗng rộng quanh một vảy rồng | Không; giữ lượt 1 |
| easier | Bậc đá hạ từ trái sang phải, lông mềm lớn nằm chéo theo hướng xuống | Không; giữ lượt 1 |
| status-learned | Dấu kiểm vàng nổi lớn trên dấu sáp vàng có mép bất quy tắc và đuôi ngắn | Không; giữ lượt 1 |
| status-review | Trang giấy đứng, góc gấp, dải đánh dấu đuôi V và ngọn lửa nhỏ nhô lên | Không; giữ lượt 1 |
| status-new | Mầm than hai lá lửa, thân sắt cong, hạt than nhọn và khoảng rỗng chữ Y | Không; giữ lượt 1 |

Prompt thực gửi: [prompts.json](../../games/dragon-hold/art-src/_review/140/prompts.json); đường dẫn bản sinh và ảnh sửa: [sources.json](../../games/dragon-hold/art-src/_review/140/sources.json). Không gán prompt sinh mới cho bước công cụ.

## 3. Hậu kỳ không phá tranh

Tách M bằng `tools/art-normalize`, chế độ global, khử loang protect-interior, WORK đặt riêng dưới 140. Cắt theo alpha, giữ tỉ lệ, căn giữa và lề bằng Triangle; sau đó các bản thu dùng Lanczos trực tiếp từ bản 1024. Nguồn do công cụ trả về 1254² được giữ nguyên trong `.try1.png`; bản chọn sau tách/căn là 1024² theo phiếu.

- `star-unlit`: lượt đầu có 467 pixel sắc khóa / 192.392 pixel hiện, tức 0,24273%. Bật sửa sắc khóa ở viền (`no_key_hue`), còn 78 pixel / 192.392, tức 0,04054%. Không tăng sáng thân sao.
- `stat-accuracy`: phục hồi alpha thành 255 cho **6 pixel** vốn có alpha 171–253 ở trong lông tên, ngoài dải mép 3 px; giữ nguyên RGB. Không xóa nét lông.
- `status-new`: thử tăng sáng RGB toàn ảnh 1% thì khổ gốc đạt, nhưng cỡ 14/20 px chỉ đạt 0,24249/0,24438 trên nền tối. Đo lại đúng cỡ game rồi tăng **tổng cộng 4% từ bản hậu kỳ đầu**, được 0,25264/0,25461. Alpha giữ nguyên. Không phải cộng dồn thêm 4% lên lượt 1%.
- Ba ảnh được sửa công cụ có byte bản hậu kỳ đầu giữ trong `first-pass/`; lượt mầm +1% giữ trong `second-pass/`. Mọi `.try1` giữ nguyên. Chỉ các file **mới do phiếu tạo** được cập nhật; không file nào trong kiểm kê trước phiếu bị sửa.
- Không san phẳng, phủ mảng màu, vẽ lại hay bỏ phần vẽ. Không xóa tệp hoặc nguồn sinh. Các tờ kiểm đầu vẫn giữ; chỉ dùng `delivery/` và `metrics-delivery-final.json` để chấm nhận.

## 4. Kiểm số

### KA1 · Giữ nguyên file có sẵn

`md5 -r` toàn bộ file trong thư mục icon trước và sau: **327 file cũ → 427 file**, **100 dòng thêm**, **0 dòng cũ đổi/mất**. `diff` chỉ thêm dòng dữ liệu (ngoài đầu mục diff). Thư mục 140, tờ xem và báo cáo chưa có trước phiếu; không có file cũ ở các đích ấy để băm. Không có file khác trong thư mục icon bị thay đổi trong thời gian làm.

Bằng chứng: [md5-before.txt](../../games/dragon-hold/art-src/_review/140/md5-before.txt), [md5-after.txt](../../games/dragon-hold/art-src/_review/140/md5-after.txt), [md5.diff](../../games/dragon-hold/art-src/_review/140/md5.diff), [md5-audit.json](../../games/dragon-hold/art-src/_review/140/md5-audit.json).

### Khổ, alpha và căn lề

40/40 bản giao đúng **1024² / 256² / 128² / 64², srgba**. Lệnh đo và đủ 40 dòng: [identify-final.txt](../../games/dragon-hold/art-src/_review/140/identify-final.txt). Hộp bao đo trên alpha >16; cạnh dài **69,921875% ở cả 10 ảnh**, lệch tâm lớn nhất **0,048828125%**, đều trong 68–72% và ≤2%.

Dải mép dùng mặt nạ alpha ≥128, lấy hiệu giãn/co vuông bán kính 3 px; đếm alpha không phải 0/255 ở ngoài dải. Pixel sắc khóa đếm trên mọi pixel alpha >0, hue cách M ≤15°, S >0,5; phần trăm chia cho số pixel alpha >0.

| Ảnh | Alpha mềm ngoài mép 3 px | Pixel sắc M / pixel hiện | Sắc M (%) | Lệch tâm lớn nhất (%) |
|---|---:|---:|---:|---:|
| star-lit | 0 | 0 / 192039 | 0.00000 | 0.04883 |
| star-unlit | 0 | 78 / 192392 | 0.04054 | 0.04883 |
| stat-accuracy | 0 | 133 / 261741 | 0.05081 | 0.00000 |
| stat-new-words | 0 | 41 / 263699 | 0.01555 | 0.00000 |
| stat-words-seen | 0 | 79 / 312201 | 0.02530 | 0.00000 |
| retry | 0 | 16 / 199903 | 0.00800 | 0.00000 |
| easier | 0 | 336 / 276062 | 0.12171 | 0.04883 |
| status-learned | 0 | 0 / 334214 | 0.00000 | 0.00000 |
| status-review | 0 | 83 / 201277 | 0.04124 | 0.00000 |
| status-new | 0 | 22 / 145733 | 0.01510 | 0.04883 |

**Kết quả:** 10/10 đạt alpha sạch và căn lề.

### Cỡ thật, tương phản và dáng

Luma là Rec.709 trên RGB sRGB chuẩn hóa: `0,2126R + 0,7152G + 0,0722B`. Luma vật là trung bình có trọng số alpha sau thu trực tiếp từ bản gốc bằng Lanczos ở **đúng cỡ game**. Hai nền có luma 0,13520 và 0,89309. Không đếm RGB của pixel trong suốt. Tờ xem ghép thật lên hai màu nền; không chỉ đặt ô màu bên cạnh.

| Ảnh | Cỡ 720 / 1080 | ΔY vỏ cây 720 / 1080 | ΔY kem 720 / 1080 | IoU lớn nhất với vật khác | Cặp |
|---|---:|---:|---:|---:|---|
| star-lit | 37 / 55 | 0.43808 / 0.43765 | 0.31981 / 0.32024 | 0.56032 | status-learned |
| star-unlit | 37 / 55 | 0.17482 / 0.17404 | 0.58307 / 0.58385 | 0.56032 | status-learned |
| stat-accuracy | 20 / 30 | 0.34443 / 0.34596 | 0.41346 / 0.41193 | 0.65903 | status-learned |
| stat-new-words | 20 / 30 | 0.40310 / 0.40355 | 0.35479 / 0.35434 | 0.77778 | stat-words-seen |
| stat-words-seen | 20 / 30 | 0.37253 / 0.37311 | 0.38536 / 0.38478 | 0.77778 | stat-new-words |
| retry | 16 / 24 | 0.27657 / 0.27801 | 0.48132 / 0.47988 | 0.51724 | status-learned |
| easier | 16 / 24 | 0.32319 / 0.32425 | 0.43470 / 0.43364 | 0.74795 | stat-words-seen |
| status-learned | 14 / 20 | 0.35267 / 0.35253 | 0.40522 / 0.40536 | 0.76131 | stat-words-seen |
| status-review | 14 / 20 | 0.50984 / 0.51023 | 0.24805 / 0.24766 | 0.58708 | stat-words-seen |
| status-new | 14 / 20 | 0.25264 / 0.25461 | 0.50525 / 0.50328 | 0.46739 | status-review |

Mặt nạ 32 px dùng Lanczos từ bản 1024 rồi alpha >16. Cặp sao cùng vật **IoU = 1,00000 ≥0,95**; các cặp còn lại lớn nhất **0,77778 ≤0,80**. Đủ 45 cặp nằm trong [metrics-delivery-final.json](../../games/dragon-hold/art-src/_review/140/metrics-delivery-final.json).

**Ngoại lệ giữ tranh:** sao sắt không đạt ΔY ≥0,25 trên nền vỏ cây (0,17482 / 0,17404), nhưng đạt trên kem (0,58307 / 0,58385). Nguyên văn phiếu nói “một trong hai nền tối” trong khi đưa một nền tối và một nền kem. Báo cáo dùng cách hiểu chặt: phải đạt trên nền vỏ cây. Vì vật bắt buộc là sắt tối và trạng thái tắt, không nâng sáng vượt ±10% để ép số; không đổi nó thành sao bạc sáng. Giữ ảnh và dừng sửa điểm này theo ART_ACCEPTANCE §5; Claude quyết dùng trên kem hay nhận ngoại lệ. Vì thế không tuyên bố toàn bộ kiểm 1–5 đã đạt.

## 5. KA5 · Tự chấm trên bản hậu kỳ

Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. M chấm theo mức hoàn thiện HUD của ảnh thương mại tham chiếu, không lấy điểm từ số đo. Ảnh mới có chất liệu, mặt vát, ánh sáng và khối rõ hơn bốn icon cũ; đứng cạnh được về độ hoàn thiện, nhưng chi tiết mảnh mất khi xuống 14–20 px.

| Ảnh | 1024 px: 5 tiêu chí → Q | 720p: 5 tiêu chí → Q | M gốc / 720p | Hạn chế nhìn thấy |
|---|---|---|---:|---|
| star-lit | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 2 / 2 / 2 / 2 → 10 | 8,5 / 8,5 | Lửa chủ yếu nằm trong mặt sao; không có quầng ngoài. |
| star-unlit | 2 / 2 / 2 / 2 / 1 → 9 | 2 / 1,5 / 2 / 2 / 1 → 8,5 | 8,5 / 8 | Nền tối thiếu ΔY; Dùng tiếp chỉ 1 vì kiểm số còn ngoại lệ. |
| stat-accuracy | 2 / 2 / 1,5 / 2 / 2 → 9,5 | 2 / 1,5 / 1,5 / 2 / 2 → 9 | 8,5 / 8 | Ở 20 px đọc được bia và tên; đường chẻ chỉ còn gợi dáng. |
| stat-new-words | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 1,5 / 2 / 2 / 2 → 9,5 | 8,5 / 8 | Rãnh phi ngôn ngữ mất ở 20 px, sách mở vẫn rõ. |
| stat-words-seen | 2 / 2 / 1,5 / 2 / 2 → 9,5 | 2 / 1,5 / 1,5 / 2 / 2 → 9 | 8 / 8 | Độ xiên làm dày bia dễ đọc, khác yêu cầu chính diện tuyệt đối của STYLE-UI. |
| retry | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 1,5 / 2 / 2 / 2 → 9,5 | 8,5 / 8 | Mũi tên C còn rõ; vảy giữa rất nhỏ ở 16 px. |
| easier | 2 / 2 / 1,5 / 2 / 2 → 9,5 | 2 / 1 / 1,5 / 2 / 2 → 8,5 | 8 / 8 | Ở 16 px chỉ còn bậc hạ và vệt lông sáng; các gân lông mất. |
| status-learned | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 1 / 2 / 2 / 2 → 9 | 8,5 / 8 | Ở 14 px dấu kiểm nổi khó hơn dáng dấu vàng. |
| status-review | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 1,5 / 2 / 2 / 2 → 9,5 | 8,5 / 8 | Ở 14 px trang, đuôi và đốm lửa phân biệt được; hoa văn đai mất. |
| status-new | 2 / 2 / 2 / 2 / 2 → 10 | 2 / 1,5 / 2 / 2 / 2 → 9,5 | 8,5 / 8 | Mầm hai nhánh còn đọc được, thân dưới chìm hơn lá trên nền tối. |

Tất cả tự chấm Q và M ≥8. Đây không phải điểm nhận; các ảnh M=8–8,5 cần Claude chấm lại độc lập. Dùng tiếp =2 chỉ cho chín ảnh đã đạt toàn bộ kiểm số của riêng ảnh; sao sắt giữ 1.

## 6. Tờ xem, khác phiếu và phần chờ

- [Tờ xem bốn hàng](../../games/dragon-hold/art-src/_review/140-sheet.jpg): hàng 1 bản giao 256 px; hàng 2 đúng cỡ 1080p trên vỏ cây/kem; hàng 3 đúng cỡ 720p trên hai nền; hàng 4 bốn icon cũ và một mảnh HUD tham chiếu, đều cao 160 px. Dưới ảnh có tên. Không dùng ảnh chụp trình duyệt.
- [Mười tờ bản sinh | bản hậu kỳ cuối](../../games/dragon-hold/art-src/_review/140/delivery/): `<tên>-before-after.jpg`. Bản sinh giữ nền M; bản hậu kỳ đặt trên nền tối trung tính để thấy alpha và lề, cùng cỡ hiển thị. Các ảnh trung gian/kiểm đầu giữ nguyên, không dùng thay ảnh cuối.
- Khác phiếu: nguồn sinh 1254² được giữ nguyên; bản chọn đúng 1024². Tám vật ngoài sao có độ dày nổi; bia và bậc hơi xiên để thể hiện lớp, đã trừ Hợp bộ. Các rãnh sách/bia là nét góc cạnh không thành chữ, để tuân thủ cấm chữ. Không có ảnh chọn 119 để so trực tiếp.
- Không làm âm thanh vì phiếu chỉ có ảnh. Không ghi `public/`, không tích hợp UI, không sửa mã game, tài liệu mỹ thuật, công cụ dùng chung, game khác hay Tu Tiên. Không chạy Git, dev server, trình duyệt, build hoặc test game.
- Chủ dự án/Claude cần xem **sao sắt trên nền tối** và các dấu 14 px ở hàng 3; quyết ngoại lệ tương phản, sau đó chấm lại M/Q. Claude là người chép vào `public/` khi nhận, không phải Codex của phiếu này.

## 7. Chạy lại

Hướng dẫn và phạm vi ghi: [README.md](../../games/dragon-hold/art-src/_review/140/README.md). Từ repo cha:

```bash
export ART_MAGICK=/opt/homebrew/bin/magick
python3 games/dragon-hold/art-src/_review/140/reproduce.py games/dragon-hold/art-src/_review/140/replay-moi
```

Dùng thư mục đích mới. Script dựng lại từ `.try1.png` đã giữ, không gọi AI và không ghi vào icon đang giao. `pipeline.py` giữ toàn bộ công thức và thao tác; `refine.py` ghi rõ ba sửa hậu kỳ. Không cần thư viện Python ngoài thư viện chuẩn và ImageMagick 7.
