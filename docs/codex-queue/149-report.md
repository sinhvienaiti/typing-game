# Phiếu 149 · Last Line · Đủ bộ HUD, chờ Claude chấm nhận

Ngày 31/10/2026, Codex tiếp tục hồ sơ bị HTTP 429. **Đã sinh 11 ảnh thử cho 10 icon, chọn đủ 10 bản gốc 1024², 30 bản thu và 10 prompt bản chọn. Kiểm số đạt; KA5 tự chấm từ 8,5 và M từ 8,0 ở 720p. Chưa phải nghiệm thu: Claude cần chấm lại từ 8 và là người đưa vào `public/`.** Lần này công cụ tích hợp `image_gen` hoạt động, không gặp 429. Không chuyển API/CLI hay dịch vụ khác.

## Bộ giao và tờ xem cần dùng

Gốc media: `games/typing-survival/art-src/`. Mỗi tên dưới đây có `.png`, `.256.png`, `.128.png`, `.64.png` và `.prompt.txt` trong `ui/icons/`. Các `.tryN.png` và prompt nguyên văn đều giữ nguyên; không xóa bản thử hoặc hồ sơ cũ. Chỉ `repair-pod` chọn try2, chín ảnh còn lại chọn try1.

**Tờ chốt đúng bộ giao:** [149-sheet-delivery.jpg](../../games/typing-survival/art-src/_review/149-sheet-delivery.jpg). Bốn hàng: gốc thu 256 px; 1080p trên than chì/thép sáng; 720p trên hai nền đó; bốn icon súng hiện có và mảnh HUD của ảnh thương mại, cùng cao 256 px. Phần vẽ không lấy từ ảnh thương mại; chỉ đối chiếu mức hoàn thiện. Nhận xét: **đứng cạnh được** về vật liệu, bevel và ánh sáng; nhóm 16 px còn ít chi tiết hơn ảnh mẫu, đặc biệt bàn phím.

- [Cỡ thật và phóng nearest 4×](../../games/typing-survival/art-src/_review/149-small-delivery-4x.jpg).
- [Cả mười icon trên hai bến của sheet trận, 720p và 1080p](../../games/typing-survival/art-src/_review/149-bay-delivery.jpg).
- [Đúng token bay-glass trên mảnh sàn thật](../../games/typing-survival/art-src/_review/149-bay-glass-delivery.jpg).
- Mười tờ `bản sinh | bản hậu kỳ`: `_review/149/<tên>-before-after-delivery-1031.jpg`, cùng hai ô 512², nguồn giữ nguyên tỷ lệ và được đệm trong ô. Ví dụ [kills](../../games/typing-survival/art-src/_review/149/kills-before-after-delivery-1031.jpg), [repair-pod](../../games/typing-survival/art-src/_review/149/repair-pod-before-after-delivery-1031.jpg).

`149-sheet.jpg`, các tờ `*-final.jpg` và các tờ trước/sau không có hậu tố `delivery` là **mốc trung gian đã giữ lại**, không dùng để chấm bộ giao cuối. Tên tờ cuối thêm `delivery` để tuân thủ không ghi đè file đã tạo. Đây là sai khác tên tờ so với phiếu; toàn bộ tên icon giao đúng yêu cầu.

## Prompt và hậu kỳ

Đã đọc lại báo cáo cũ, ART_ACCEPTANCE §2.2/§5, STYLE-UI nguyên văn tại ART_DIRECTION §4.3, định dạng 015, báo cáo 121/127; xem concept B, `gun-xung.norm.256.png`, tờ 121/127, ảnh tham chiếu chủ dự án và sheet trận. 121/127 có chốt chưa đạt trong báo cáo của chúng: chỉ lấy hướng B và vật liệu làm tham chiếu, không tuyên bố hai phiếu đó đã nghiệm thu, không sửa chúng.

| Ảnh | Các lượt sinh, sửa prompt và chọn |
| --- | --- |
| armour | Try1 dùng nguyên prompt đã lưu: ba lớp giáp bạc/vàng trắng, hai khe lam, đầu nhọn; chọn. |
| clock | Try1 nguyên prompt: mặt đếm ngược không chữ, kim lam và cung sáng; chọn. Vòng là chính cơ cấu đồng hồ, không phải khung trình bày thêm. |
| kills | Try1 nguyên prompt: kính đen vỡ, mặt gãy cam, dáng chéo; chọn. Không sinh lại. |
| surge | Try1 nguyên prompt: ba mảnh kính dựng dưới dấu cảnh báo cam; chọn. |
| repair-pod | Try1 đẹp nhưng IoU với clock = 0,8833, không chọn. Try2 giữ nguyên STYLE-UI và ICON, đổi thân rộng/thấp thành capsule cao/hẹp, vai vát, tay cầm sát thân, giữ cờ lê lớn. IoU lớn nhất sau chọn = 0,7363. |
| keyboard | Try1 nguyên prompt, hàng phím trống và phím cách lam; chọn. Phối ngang thực tế rộng hơn 2:1, không bóp hình để ép tỷ lệ. |
| check | Try1 nguyên prompt, tấm kim loại đi theo hình dấu tích; chọn. |
| bay-full | Try1 nguyên prompt, ba ô nạp lam đầy trong máng giữ; chọn. |
| streak | Try1 nguyên prompt, đúng ba tia bốn cánh nối chéo; chọn. |
| lock | Try1 nguyên prompt, quai U, lỗ khóa và hai nan cửa bến nhỏ; chọn. |

Mười prompt try1 đã có trước phiên được giữ nguyên byte. Prompt try2 và prompt bản chọn nằm cạnh PNG. [Nhật ký 10 lượt đầu](../../games/typing-survival/art-src/_review/149/generation-log-1031.json) và [lượt pod thứ hai](../../games/typing-survival/art-src/_review/149/generation-repair-try2-1031.json) lưu prompt nguyên văn và đường dẫn nguồn của công cụ. Không ảnh nào vượt ba lượt.

Công cụ trả tám ảnh 1254², keyboard 1774×887 và bay-full 887×1774. Tất cả được **thu đều toàn vật**, giữ tỷ lệ, căn bbox alpha >16 về giữa canvas 1024², cạnh dài mục tiêu 716 px; không cắt bỏ phần vẽ. Nền trong suốt thật, không cần khóa M/G hoặc tách nền sơn. Tất cả gốc dùng sRGB, RGBA 8 bit.

Alpha nguồn đa số 252–253 ngay trên bề mặt vật được yêu cầu đục. Hậu kỳ chỉ chuẩn hóa alpha trong/ngoài dải 3 px quanh contour alpha 128; giữ alpha trong dải, giữ nguyên RGB và nét khắc. Riêng `kills` tăng RGB **toàn ảnh 8%**: mốc đầu 0%, thử hậu kỳ 2% đã đạt than chì nhưng ΔY trên token kính ở 720p chỉ 0,2401; mức 8% cho 0,2557/0,2523. Không chỉnh mảng riêng, không phủ màu, không xóa, san phẳng hay thay phần vẽ. So trước/sau không thấy mất khối hoặc làm phai nét. Các ảnh còn lại không chỉnh sáng.

Ba bản thu được Lanczos **trực tiếp từ gốc** riêng từng cỡ, không lấy 128 từ 256, không làm nét 64. Kiểm thêm trên cả bản thu phát hiện nhiễu alpha do resampling, tối đa 35 pixel trong một file. Sửa duy nhất alpha ngoài dải mép 3 px: tổng **101 pixel trên 30 bản thu**, **0 pixel RGB đổi**. Giữ mốc Lanczos trước sửa trong hồ sơ. Không có xung đột ngưỡng với phần tranh cần giữ.

## KA2–KA4 · Số đo bộ giao

Luma dùng RGB **sRGB 0–1**, `Y = 0,2126R + 0,7152G + 0,0722B`, lấy trung bình vật có trọng số alpha; loại pixel alpha 0. ΔY là trị tuyệt đối giữa luma vật và nền. Đây là quy ước số đo nêu rõ để Claude tái lập, không phải tỷ lệ tương phản WCAG. `--bay-glass` đọc từ `src/view/theme.css`: `rgba(7, 9, 11, 0.64)`.

Sheet map 1 là contact sheet 2584×1470: lấy ô đầu 640×360 tại +8+8, dựng lại 1280×720 và 1920×1080 để đặt icon đúng cỡ; đây là mock trên capture có sẵn, không phải capture mới. Tờ bến giữ nguyên chữ và art cũ của screenshot. Kiểm token kính bổ sung áp đúng rgba lên mảnh sàn thật lấy từ cùng ảnh, đo màu nền ngay dưới từng alpha. Tọa độ và số đo đầy đủ lưu JSON.

**Khổ:** 40/40 PNG đúng 1024²/256²/128²/64², `srgba`; [kết quả identify](../../games/typing-survival/art-src/_review/149/identify-delivery-1031.txt). **Alpha:** 40/40 có 0 pixel bán trong suốt ngoài dải mép 3 px; hue M lệch ≤15°, S>0,5 trong phần alpha>0 đều ≤0,2%. Cột M dưới đây là cực đại qua bốn file của từng ảnh, nên bao gồm cả bản thu. Không dùng nền khóa, nhưng vẫn đo sắc M để kiểm nhiễu.

| Ảnh | Cỡ 720/1080 | Lấp cạnh dài % | Alpha ngoài mép (4 file) | M tối đa % | ΔY than chì 720/1080 | ΔY kính 720/1080 | IoU lớn nhất (đối tượng) |
| --- | --- | ---: | ---: | ---: | --- | --- | --- |
| armour | 20 / 30 | 70.02 | 0 | 0.0100 | 0.4978 / 0.4983 | 0.5140 / 0.5145 | 0.6952 (clock) |
| clock | 20 / 30 | 69.92 | 0 | 0.0145 | 0.3959 / 0.3963 | 0.4022 / 0.4026 | 0.7560 (lock) |
| kills | 20 / 30 | 69.92 | 0 | 0.0588 | 0.2747 / 0.2714 | 0.2557 / 0.2523 | 0.3911 (check) |
| surge | 28 / 42 | 69.92 | 0 | 0.0256 | 0.2901 / 0.2892 | 0.2846 / 0.2837 | 0.5512 (clock) |
| repair-pod | 28 / 42 | 69.92 | 0 | 0.0170 | 0.3443 / 0.3435 | 0.3254 / 0.3247 | 0.7363 (bay-full) |
| keyboard | 16 / 24 | 70.02 | 0 | 0.0395 | 0.4005 / 0.3949 | 0.3463 / 0.3408 | 0.4379 (clock) |
| check | 16 / 24 | 69.92 | 0 | 0.0074 | 0.3765 / 0.3780 | 0.3687 / 0.3703 | 0.3911 (kills) |
| bay-full | 16 / 24 | 69.82 | 0 | 0.0265 | 0.3587 / 0.3675 | 0.3209 / 0.3289 | 0.7363 (repair-pod) |
| streak | 16 / 24 | 69.92 | 0 | 0.0321 | 0.5690 / 0.5729 | 0.5747 / 0.5784 | 0.3376 (kills) |
| lock | 24 / 36 | 69.92 | 0 | 0.1320 | 0.4015 / 0.4015 | 0.4196 / 0.4196 | 0.7560 (clock) |

Độ lệch tâm bbox lớn nhất **0,0977%**, dưới 2%; tỷ lệ lấp cạnh dài 69,82–70,02%, trong 68–72%. 45/45 cặp IoU alpha 32² ≤0,80, cực đại **0,7560 (clock–lock)**. Mặt nạ IoU lấy alpha ≥128 sau Lanczos trực tiếp về 32². Không có cặp sáng/tắt trong phiếu này. Hai nền HUD đã dựng là `#14181f` và `#8c96a3`; toàn bộ ảnh đạt ΔY≥0,25 trên nền than chì. Nền thép sáng vẫn có trên tờ xem và số đo, không được coi là nền đạt cho mọi icon. Cả 10 ảnh trên bến thật cũng đạt, ΔY thấp nhất **0,3133** ở kills; phép token kính riêng thấp nhất **0,2523** tại 1080p.

Dữ liệu: [gốc, tâm, tương phản hai nền và 45 cặp IoU](../../games/typing-survival/art-src/_review/149/measurements-selected-1031.json), [40 PNG giao](../../games/typing-survival/art-src/_review/149/delivery-measurements-1031.json), [bến và token kính](../../games/typing-survival/art-src/_review/149/bay-measurements-delivery-1031.json), [sửa alpha bản thu](../../games/typing-survival/art-src/_review/149/derivative-edge-measurements-1031.json). Số luma nền thép sáng và số gốc đầy đủ nằm trong JSON, không chỉ làm tròn ở bảng.

## KA5 · Tự chấm trên bản hậu kỳ

Đã xem cả mười gốc 1024², tờ trước/sau và 720p/1080p thật, đối chiếu HUD thương mại. Điểm Q theo thứ tự **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi tiêu chí 0–2. “Dùng tiếp” = 2 vì đủ khổ, prompt, alpha, lề, tương phản và IoU; điểm đó không thay cho Claude chấm nhận. M xét chất liệu và độ hoàn thiện icon theo UI thương mại, không đòi icon độc lập có ba tầng cảnh và bầu trời.

| Ảnh | 5 điểm Q gốc | Q gốc | 5 điểm Q 720p | Q 720p | M gốc / 720p | Nhận xét |
| --- | --- | ---: | --- | ---: | --- | --- |
| armour | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 2 / 2 / 2 / 2 | 10 | 8.5 / 8.2 | Giáp phân đoạn, khe lam và đầu nhọn giữ rõ. |
| clock | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.4 / 8.1 | Đọc kim và cung đếm; nét chòm sao mất ở cỡ nhỏ. |
| kills | 1.5 / 2 / 2 / 2 / 2 | 9.5 | 1.5 / 1.5 / 2 / 2 / 2 | 9 | 8.2 / 8.0 | Hai mảnh lớn trội hơn mảnh thứ ba; khe vỡ và dáng chéo còn đọc được. |
| surge | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.3 / 8.1 | Ba mảnh dựng và dấu cảnh báo rõ; hoa văn phụ thu nhỏ. |
| repair-pod | 2 / 2 / 2 / 1.5 / 2 | 9.5 | 2 / 1.5 / 2 / 1.5 / 2 | 9 | 8.2 / 8.0 | Cờ lê lớn, thân hẹp phân biệt với mặt đồng hồ; khối hơi cong. |
| keyboard | 2 / 2 / 2 / 1.5 / 2 | 9.5 | 2 / 1 / 2 / 1.5 / 2 | 8.5 | 8.1 / 8.0 | Thân rộng hơn tỷ lệ 2:1 của prompt. 16 px còn dáng bàn phím và phím cách; hàng phím rất nhỏ, cần Claude xem kỹ. |
| check | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.3 / 8.2 | Dáng tích riêng, phần khắc phụ không còn đọc ở 16 px. |
| bay-full | 2 / 2 / 2 / 1.5 / 2 | 9.5 | 2 / 1.5 / 2 / 1.5 / 2 | 9 | 8.2 / 8.0 | Ba ô nạp lam đọc thành dải đầy; thân hẹp hơn yêu cầu ban đầu. |
| streak | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.4 / 8.1 | Đúng ba tia nối, ở 16 px thiên về ba điểm sáng theo đường chéo. |
| lock | 2 / 2 / 2 / 2 / 2 | 10 | 2 / 1.5 / 2 / 2 / 2 | 9.5 | 8.4 / 8.2 | Quai và lỗ khóa rõ; cánh bến nhỏ phía sau thành mảng tối. |

**Cần chủ dự án/Claude xem kỹ:** keyboard 16 px (hàng phím nhỏ), bay-full 16 px (hẹp), kills 20 px (mảng kính đen và chi tiết vỡ nhỏ). Đây là các bản sát mức M=8; điểm tự chấm không phải lời bảo đảm Claude sẽ nhận. Nếu Claude chấm dưới 8, tiếp tục từ bản thử đã giữ, không đưa vào public.

## KA1 · Giữ nguyên hồ sơ và phạm vi

Mốc mới trước phiên băm **224 file** bằng `/sbin/md5 -r` trong `ui/icons`, `_review/149/` và các file `_review/149-*`. Mốc sau có **1426 file**, **1202 đường dẫn thêm**, **0 thay đổi**, **0 mất**; diff không có dòng nội dung bị xóa. Không quy mọi đường dẫn thêm thành sản phẩm của phiếu khi repo có agent khác cùng làm.

[Mốc trước mới](../../games/typing-survival/art-src/_review/149/md5-before-resume-1031.txt), [mốc sau mới](../../games/typing-survival/art-src/_review/149/md5-after-resume-1031.txt), [diff chỉ thêm](../../games/typing-survival/art-src/_review/149/md5-diff-resume-1031.txt), [tổng kết KA1](../../games/typing-survival/art-src/_review/149/md5-summary-resume-1031.json). Các mốc cũ `md5-before.txt`/`md5-after.txt` và hồ sơ 429 giữ nguyên. Snapshot sau được tính trước khi ghi chính nó, diff và summary để tránh tự tham chiếu. Báo cáo này nằm ngoài cây media được băm và được phép cập nhật. Bản báo cáo trước phiên giữ tại `_review/149/report-before-resume-1031.md`.

Script đã dùng đều trong `_review/149/`; không sửa công cụ dùng chung. Bộ chốt: `process-selected-1031.py` → `edge-derivatives-1031.py` → `deliver-ready-1031.py` → `proofs-delivery-1031.py`, sau cùng `audit-final-1031.py` và `write-report-1031.py`. Các writer từ chối ghi đè, hồ sơ trung gian giữ nguyên. Tái lập hậu kỳ vào **thư mục con mới** và đối chiếu 40 PNG bằng:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 games/typing-survival/art-src/_review/149/replay-ready-1031.py --out replay-owner
```

Lượt `replay-verified-1031` đã chạy, 40/40 PNG tái lập giống từng pixel RGBA với bản giao; JSON kết quả nằm trong thư mục đó. Không yêu cầu byte PNG giống nhau vì metadata thời gian có thể khác. Tái sinh nghệ thuật dùng `image_gen` tích hợp với prompt cạnh try; không có runner mạng khác.

Không còn icon thiếu. Không làm âm thanh, tích hợp game hoặc chép vào `public/` vì ngoài phạm vi và Claude là người gắn. Không chạy Git, build/test game, dev server, trình duyệt hay mạng ngoài công cụ sinh ảnh; không đọc/ghi Tu Tiên hoặc `.wt-*`. Không có capture mới hoặc raw frame cần prune; các try và proof là hồ sơ cần giữ. Sai khác đã nêu: chuẩn hóa khổ công cụ trả, alpha hậu kỳ ở các bản thu, tờ chốt mang hậu tố `delivery`, hình keyboard/bay-full khác nhẹ tỷ lệ prompt. Chưa có Claude chấm lại; chủ dự án xem tờ chốt và các icon nhỏ trước khi nhận.
