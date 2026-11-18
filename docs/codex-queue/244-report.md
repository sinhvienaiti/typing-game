# Phiếu 244 · Icon bảng Sound và phần đầy thanh trượt

**Trạng thái: giao đủ file của 8 icon và 4 ảnh rãnh; 9/12 ảnh đạt tự chấm. Ba ảnh rãnh Wordwoven/Last Line CHƯA ĐẠT kiểm vị trí hai đầu sau đủ 3 lượt. Không coi phiếu đã được nhận.**

Thực hiện ngày 31/10/2026, khoảng 17:15–17:45, giờ Việt Nam. Dùng công cụ tích hợp `image_gen`: **26 lời gọi thành công**, không gặp 429 hay lời yêu cầu thử lại sau. Không dùng CLI/API sinh ảnh khác. Mỗi ảnh tối đa 3 lượt, không có lượt thứ tư.

## File giao và phần cần xem

- Icon Dragonhold: `games/dragon-hold/art-src/ui/quick-settings/selected/{vol-keyboard,vol-voice,vol-interface}.r2.*`, `selected/vol-keyboard-volume.*`.
- Icon Wordwoven: `games/typing-defense/art-src/ui/quick-settings/selected/{vol-keyboard,vol-interface,hud-settings}.r2.*`, `selected/vol-keyboard-volume.*`.
- Mỗi icon có PNG 1024², 256², 128², 64²; mỗi PNG có prompt chính xác cạnh ảnh.
- Rãnh: Dragonhold `sliders/slider-fill.*`; Wordwoven `sliders/{slider-fill,slider-empty}.*`; Last Line `sliders/slider-fill.*`. Mỗi ảnh có 1024×64, `.512.png` 512×32 và prompt cạnh từng bản. Ba ảnh chưa đạt vẫn giữ bản tốt nhất theo luật sau 3 lượt; tên bản chọn không có nghĩa đã được nhận.
- Danh sách từng PNG và nguồn được chọn: [delivered.json](244/delivered.json). Mọi lượt sinh giữ trong thư mục quy định, kèm `.prompt.txt`.
- Tờ icon: [Dragonhold](../../games/dragon-hold/art-src/_review/244-sheet.jpg), [Wordwoven](../../games/typing-defense/art-src/_review/244-sheet.jpg). Có 256 px, 1080p/720p **1×**, bản ×4 point, cặp so sánh và cũ/mới.
- Bảy hàng Sound xếp dọc như bảng thật: [Dragonhold](../../games/dragon-hold/art-src/_review/244-sound-dragon-hold.jpg), [Wordwoven](../../games/typing-defense/art-src/_review/244-sound-typing-defense.jpg). Phiếu gọi là “sáu” nhưng liệt kê bảy hàng; tờ kiểm dùng đủ bảy.
- Thanh 0/25/50/100%, 720p/1080p 1× và 720p ×4: [Dragonhold](../../games/dragon-hold/art-src/_review/244-slider-dragon-hold.jpg), [Wordwoven](../../games/typing-defense/art-src/_review/244-slider-typing-defense.jpg), [Last Line](../../games/typing-survival/art-src/_review/244-slider-typing-survival.jpg).
- Tờ kéo giãn: `games/<game>/art-src/_review/244-slider-stretch-<game>.jpg`. Tờ bản sinh | bản hậu kỳ: `games/<game>/art-src/_review/244/<tên>-compare.jpg`. Hai ô đặt vật cùng cỡ để kiểm việc giữ tranh.

## Phạm vi, nguồn và hậu kỳ

Đã đọc luật chung 242–246, phiếu 180, 225, 241 và báo cáo 241; khối STYLE-UI/KIND từ prompt bộ 180 của từng game, thêm SMALL-SIZE nguyên văn. Đính kèm `selected/vol-master.png` và `selected/hud-sound.png` của đúng game cho từng icon. Đã xem ảnh tham chiếu thương mại `owner-epic-2026-10-28.webp`, không đính kèm vào lượt sinh. Mảnh bảng thật: Dragonhold `ui/frames/panel-large.png`; Wordwoven `ui/frames-epic/panel-large.v2.png`; Last Line `ui/frames-epic/panel-large.png`.

Ảnh rãnh được sinh ở chế độ sửa ảnh, đính kèm `slider-track.png` hiện tại. Lượt cuối Wordwoven và Last Line thêm bản đích chỉ đệm trong suốt 1536×1024, giữ nguyên rãnh, nhằm giữ vị trí; công cụ lại thêm quầng sáng ngoài vật nên loại cả ba lượt cuối. Không xoá quầng sáng bằng hậu kỳ để ép qua kiểm.

Icon: tách màu khóa magenta, cắt hộp bao, thêm lề trong suốt để cạnh dài xấp xỉ 70%, thu Lanczos độc lập từ nguồn đã đệm. Rãnh: cắt hộp bao alpha >16, đệm trong suốt về 16:1, thu đều; mọi hệ số x = y. Không co không đều, không làm nét bản 64. Chỉ kẹp alpha gần 0/255 và sửa alpha lẻ ngoài dải mép 3 px; không tô, thay vật liệu hay san phẳng phần vẽ bằng mã.

Chỉnh sáng nhẹ toàn ảnh: `vol-keyboard` Dragonhold lượt 3 ×1,10 và `vol-keyboard-volume` Dragonhold lượt 2 ×1,06, trong giới hạn ±10%. Các ảnh khác ×1,00. Hộp bao, khung đệm, hệ số và số pixel sửa alpha ở [processed.json](244/processed.json). Dùng ImageMagick 7.1.2-34, font Arial của macOS; đặt một luồng cho hậu kỳ.

Lưu ý nguồn: báo cáo 241 ghi rãnh Dragonhold chưa đạt đầu trái 69 px. Phiếu 244 chỉ định rãnh hiện tại làm khuôn; đã dùng đúng file hiện tại và không thay `slider-track.*` hay `slider-thumb.*`. Kiểm riêng của 244 thay Kiểm 3–8 cho phần rãnh; không tuyên bố đã giải quyết nợ của 241.

## KA1 · Bảo toàn file

Đã ghi MD5 trước/sau cho toàn bộ quick-settings của ba game: **598 → 730 file**, thêm **132** file, **0 đổi, 0 mất**. Kiểm cuối [final-check.json](244/final-check.json) xác nhận 40 PNG giao đủ prompt chính xác, 26 nguồn giữ đủ, không có đường dẫn mới ngoài danh sách và tối đa 3 lượt/ảnh. Danh sách trong [md5-before.txt](244/md5-before.txt), [md5-after.txt](244/md5-after.txt), [verification.json](244/verification.json). MD5 tính bằng thư viện chuẩn, cùng kết quả băm với `md5 -r`.

| Game | Trước | Sau | Đổi / mất |
| --- | ---: | ---: | --- |
| Dragonhold | 202 | 258 | 0 / 0 |
| Wordwoven | 184 | 250 | 0 / 0 |
| Last Line | 212 | 222 | 0 / 0 |

Toàn bộ file thêm nằm đúng các tên/lượt cho phép. Ngoài quick-settings chỉ ghi `art-src/_review/244*`, báo cáo này và thư mục `244/`. Không dùng Git; không sửa mã, manifest, CSS, âm thanh, public, Tu Tiên hay `.wt-*`; không chạy build, test game, dev server hoặc trình duyệt. Không có raw frame/capture trình duyệt cần prune.

## Icon · Kiểm số ở cỡ thật

Mọi bản giao đúng khổ sRGBA, cạnh dài hộp bao khoảng 70%, lệch tâm dưới 2%. Tất cả các bản thu có **0 pixel alpha lẻ ngoài mép 3 px**, sắc khóa dưới 0,2%. Bảng dưới ghi bản 1024; số đủ từng cỡ ở [metrics.json](244/metrics.json) và [identify.txt](244/identify.txt).

| Game · icon | Lượt chọn / gọi | Opening 720p | Độ phủ | Sắc khóa 1024 | ΔY vùng trên / dưới bảng thật |
| --- | --- | ---: | ---: | ---: | --- |
| Dragonhold · `vol-keyboard` | 3 / 3 | 0.9939 | 0.8594 | 0.0153% | 0.2433 / 0.2976 |
| Dragonhold · `vol-voice` | 2 / 2 | 0.9931 | 0.7552 | 0.0179% | 0.3318 / 0.3858 |
| Dragonhold · `vol-interface` | 1 / 1 | 0.9695 | 0.5848 | 0.0156% | 0.3238 / 0.3843 |
| Dragonhold · `vol-keyboard-volume` | 2 / 2 | 1.0000 | 0.7875 | 0.0124% | 0.2720 / 0.3313 |
| Wordwoven · `vol-keyboard` | 2 / 2 | 0.9939 | 0.8542 | 0.0344% | 0.2603 / 0.2994 |
| Wordwoven · `vol-interface` | 1 / 1 | 0.9511 | 0.7188 | 0.0139% | 0.3643 / 0.4036 |
| Wordwoven · `vol-keyboard-volume` | 2 / 2 | 0.9918 | 0.7625 | 0.0100% | 0.3746 / 0.4160 |
| Wordwoven · `hud-settings` | 2 / 2 | 1.0000 | 0.7425 | 0.0091% | 0.3722 / 0.4116 |

Opening ≥0,80 và độ phủ ≥0,30: đạt cả tám. Tương phản ≥0,25 trên ít nhất một vùng bảng tối thật: đạt cả tám. **Phím Dragonhold còn ΔY 0,2433 ở vùng bảng phía trên**, dưới ngưỡng ở vùng đó; vùng dưới đạt 0,2976. Giữ cả hai số, không che điểm yếu. Tờ [Dragonhold vùng sáng/tối](../../games/dragon-hold/art-src/_review/244-panel-contrast-dragon-hold.jpg) và [Wordwoven](../../games/typing-defense/art-src/_review/244-panel-contrast-typing-defense.jpg) dùng cùng các mảnh cho mọi icon, không đổi nền theo từng ảnh. Vùng nền cắt tại (200,200) và (200,700), icon đặt (8,8); phép đo lấy đúng vùng dưới icon. Chi tiết: [contrast-panels.json](244/contrast-panels.json).

| Cặp ở 24 px | Dragonhold IoU | Wordwoven IoU |
| --- | ---: | ---: |
| `vol-keyboard` / `vol-keyboard-volume` | 0.7206 | 0.7277 |
| `vol-keyboard` / `vol-master` | 0.6552 | 0.7273 |
| `vol-keyboard-volume` / `vol-master` | 0.6789 | 0.6911 |

Ba cặp riêng mỗi game đều ≤0,80. Mọi cặp được đo ở 32 px đều ≤0,80; bảng đủ nằm trong metrics. Có cặp phím/voice Dragonhold IoU 0,8060 ở 24 px; hai ảnh vẫn tách nghĩa nhờ ô vuông và đuôi thoại, nhưng Claude nên xem cạnh nhau.

Tự đọc ở ô 720p 1× trước khi đọc lại ý mới; đây là tự chấm của người đã biết brief, **không phải phép đọc mù độc lập**:

| Game · icon | Cụm tự đọc 3–5 chữ |
| --- | --- |
| Dragonhold · `vol-keyboard` | Phím phát sóng âm |
| Dragonhold · `vol-voice` | Bong bóng đang nói |
| Dragonhold · `vol-interface` | Con trỏ nhấn nút |
| Dragonhold · `vol-keyboard-volume` | Phím kèm cột âm |
| Wordwoven · `vol-keyboard` | Phím ngọc phát âm |
| Wordwoven · `vol-interface` | Con trỏ bấm nút |
| Wordwoven · `vol-keyboard-volume` | Phím và cột âm |
| Wordwoven · `hud-settings` | Bánh răng tâm tối |

## Rãnh · Chồng khuôn, luma và kéo giãn

Mặt nạ alpha >16, đo tại 1024×64. Luma sRGB theo 0,2126R + 0,7152G + 0,0722B; lòng rãnh lấy x=103…920, y=20…43, bỏ viền và hai đầu. Wordwoven so phần đầy với phần rỗng mới.

| Game · ảnh chọn | Lượt chọn / gọi | IoU với track | Lệch đầu trái / phải | Y lòng rãnh | Kết luận |
| --- | --- | ---: | --- | ---: | --- |
| Dragonhold · `slider-fill` | 2 / 2 | 0.976177 | 0 / 0 px | 0.513551 | Đạt |
| Wordwoven · `slider-fill` | 1 / 3 | 0.982164 | 8 / 8 px | 0.635151 | **Chưa đạt hai đầu** |
| Wordwoven · `slider-empty` | 2 / 3 | 0.982133 | 8 / 8 px | 0.165584 | **Chưa đạt hai đầu** |
| Last Line · `slider-fill` | 1 / 3 | 0.976025 | 12 / 12 px | 0.715276 | **Chưa đạt hai đầu** |

| Game | ΔY đầy − rỗng | IoU đầy / rỗng |
| --- | ---: | ---: |
| Dragonhold | 0.315622 | 0.976177 |
| Wordwoven | 0.469567 | 0.999589 |
| Last Line | 0.400604 | 0.976025 |

Mọi ΔY ≥0,15; mọi IoU mới/track ≥0,97. Cặp đầy/rỗng Wordwoven khớp nhau 0,999589 nhưng **cả hai ngắn hơn khuôn đã nhận 8 px mỗi đầu**, nên vẫn trượt yêu cầu ≤2 px. Last Line ngắn hơn 12 px mỗi đầu. Không co ngang riêng để ép khớp, không cắt/đắp phần vẽ. Sau 3 lượt, giữ bản tốt nhất để Claude quyết theo ART_ACCEPTANCE §5.

Các bản 90×10, 210×10, 290×10, 135×15, 315×15, 435×15 đã dựng. Hình đầu rãnh giữ kiểu gốc, không biến thành móc hoặc vòng; nguồn hậu kỳ không co không đều. Bảng độ lệch chuẩn luma cột trong 80% giữa (tham khảo 225):

| Game · ảnh | 90×10 | 210×10 | 290×10 | 135×15 | 315×15 | 435×15 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Dragonhold · slider-fill | 0.01964 | 0.02018 | 0.02034 | 0.02020 | 0.02049 | 0.02069 |
| Wordwoven · slider-fill | 0.03314 | 0.03339 | 0.03339 | 0.03355 | 0.03367 | 0.03371 |
| Wordwoven · slider-empty | 0.01267 | 0.01269 | 0.01275 | 0.01181 | 0.01188 | 0.01194 |
| Last Line · slider-fill | 0.01124 | 0.01126 | 0.01128 | 0.01066 | 0.01078 | 0.01080 |

Mọi số ≤0,05. Tờ mức đầy dựng bằng phần rỗng nguyên thanh, cắt phần đầy tại tâm núm cho mức trung gian; 0% không vẽ phần đầy, 100% vẽ toàn bộ. Tâm núm chạy từ nửa ô núm tới chiều rộng trừ nửa ô núm. Kích thước rail/thumb 210×10 / 22 px và 315×15 / 33 px; không cắt lại lề núm đã nhận. Bảng nền rộng được ghép bằng các mảnh lòng bảng thật 500 px, tránh lẫn mép magenta của ảnh nguồn.

## Lượt sinh và sửa prompt

Prompt đầy đủ chính xác của từng lượt ở [prompts.json](244/prompts.json) và cạnh từng PNG nguồn; thời điểm, đường dẫn nguồn công cụ và lượt ở [calls.json](244/calls.json). Không bỏ các lượt trượt.

| Game · ảnh | Số gọi | Bản chọn | Diễn biến |
| --- | ---: | --- | --- |
| Dragonhold · `vol-keyboard` | 3 | 3 | 1: mặt đá sáng giống hộp; 2: đổi phím mặt tối; 3: tăng khối vàng để nổi ở cỡ nhỏ, hậu kỳ sáng +10%. |
| Dragonhold · `vol-voice` | 2 | 2 | 1: lòng tối quá lớn; 2: vành vàng và đuôi thoại rộng hơn. |
| Dragonhold · `vol-interface` | 1 | 1 | Lượt 1: con trỏ, nút tròn và tia click; giữ, chi tiết nút còn nhiều ở bản lớn. |
| Dragonhold · `vol-keyboard-volume` | 2 | 2 | 1: công cụ chép loa tham chiếu, loại; 2: khóa chủ thể phím + ba cột thẳng, sáng +6%. |
| Wordwoven · `vol-keyboard` | 2 | 2 | 1: mặt ngà và dáng hộp; 2: mặt ngọc trơn, mặt trước có bậc phím. |
| Wordwoven · `vol-interface` | 1 | 1 | Lượt 1: con trỏ bấm ngọc; giữ, hoa văn chỉ còn là texture ở cỡ nhỏ. |
| Wordwoven · `vol-keyboard-volume` | 2 | 2 | 1: cặp phím/âm lượng IoU 0,8020; 2: thu phím, tăng ba cột và khoảng trống, IoU về 0,7277. |
| Wordwoven · `hud-settings` | 2 | 2 | 1: tâm có mặt trời; 2: tâm ngọc tối, trơn, răng liền thân. |
| Dragonhold · `slider-fill` | 2 | 2 | 1: IoU 0,9407; 2: giữ tỉ lệ sát hơn, IoU 0,9762 và đầu 0/0 px. |
| Wordwoven · `slider-fill` | 3 | 1 | 1: bản tốt nhất, đầu 8/8; 2: đầu 19/19, bỏ; 3: thêm quầng sáng ngoài khuôn, bỏ. |
| Wordwoven · `slider-empty` | 3 | 2 | 1: đầu 12/12; 2: bản tốt nhất, đầu 8/8; 3: thêm quầng sáng ngoài khuôn, bỏ. |
| Last Line · `slider-fill` | 3 | 1 | 1: bản tốt nhất, đầu 12/12; 2: vẫn 12/12, IoU/luma thấp hơn; 3: thêm quầng sáng ngoài khuôn, bỏ. |

## KA5 · Tự chấm trên tờ 720p 1×

Thứ tự tiêu chí: Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp, mỗi tiêu chí 0–2. Đã xem tờ 1× và bản phóng; điểm không phải chấm nhận trong game.

| Game · ảnh | Năm điểm | Tổng | Mức |
| --- | --- | ---: | --- |
| Dragonhold · `vol-keyboard` | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | đạt tự chấm, chờ Claude duyệt |
| Dragonhold · `vol-voice` | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | đạt tự chấm, chờ Claude duyệt |
| Dragonhold · `vol-interface` | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | đạt tự chấm, chờ Claude duyệt |
| Dragonhold · `vol-keyboard-volume` | 2 / 1,5 / 2 / 1,5 / 2 | 9.0 | đạt tự chấm, chờ Claude duyệt |
| Wordwoven · `vol-keyboard` | 2 / 1,5 / 2 / 1,5 / 2 | 9.0 | đạt tự chấm, chờ Claude duyệt |
| Wordwoven · `vol-interface` | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | đạt tự chấm, chờ Claude duyệt |
| Wordwoven · `vol-keyboard-volume` | 2 / 1,5 / 2 / 1,5 / 2 | 9.0 | đạt tự chấm, chờ Claude duyệt |
| Wordwoven · `hud-settings` | 2 / 2 / 1,5 / 1,5 / 2 | 9.0 | đạt tự chấm, chờ Claude duyệt |
| Dragonhold · `slider-fill` | 2 / 1,5 / 1,5 / 1,5 / 2 | 8.5 | đạt tự chấm, chờ Claude duyệt |
| Wordwoven · `slider-fill` | 2 / 2 / 1,5 / 1,5 / 0,5 | 7.5 | chưa đạt — giữ bản tốt nhất sau 3 lượt |
| Wordwoven · `slider-empty` | 2 / 2 / 1,5 / 1,5 / 0,5 | 7.5 | chưa đạt — giữ bản tốt nhất sau 3 lượt |
| Last Line · `slider-fill` | 2 / 2 / 1,5 / 1,5 / 0,5 | 7.5 | chưa đạt — giữ bản tốt nhất sau 3 lượt |

Không cho “Dùng tiếp” 2 điểm với ba ảnh rãnh trượt vị trí hai đầu. Điểm 7,5 chỉ để giữ bản tốt nhất, **chưa đạt nhận**. Icon phím và con trỏ vẫn cần Claude đọc độc lập ở cỡ thật; đặc biệt phím Dragonhold trên vùng bảng sáng hơn và con trỏ Wordwoven còn nhiều khối vàng.

## Việc chưa làm và việc của Claude/chủ dự án

- **Chưa hoàn tất kiểm hai đầu của ba ảnh rãnh Wordwoven/Last Line**: đã đủ 3 lượt, không gọi tiếp trong phiếu này. Xin quyết định hướng xử lý khuôn; không xem tên bản chọn là đã nhận. Có thể ưu tiên xem cặp Wordwoven vì chúng khớp nhau rất sát, nhưng tiêu chuẩn đối chiếu track cũ vẫn đang trượt.
- Chấm lại 8 icon và Dragonhold fill, rồi kiểm trong game ở 1280×720 và 1920×1080 theo thẩm quyền gắn của Claude. Chủ dự án xem tờ Sound và các tờ slider đã liên kết ở đầu báo cáo.
- Chưa gắn manifest/CSS, chưa chép public, chưa sao lưu media bằng lệnh mạng; các việc đó ngoài phạm vi được ghi. Không sửa các ảnh track/thumb đã nhận.
- Không tạo âm thanh vì phiếu này chỉ yêu cầu ảnh. Không mở hay sửa Tu Tiên.

## Tái hiện

Từ repo cha, chạy `node docs/codex-queue/244/audit.mjs` và `node docs/codex-queue/244/contrast.mjs` để kiểm; `node docs/codex-queue/244/review.mjs` để dựng tờ xem. `process.mjs` lưu phép hậu kỳ của các bản được chọn, `deliver.mjs` chỉ chép nếu file chưa có hoặc đã trùng nội dung. Lệnh ghép cụ thể ở [review-commands.json](244/review-commands.json); số các lượt trước giữ ở `metrics-pass1.json`, `metrics-pass2.json`. Không chạy lại các script chuẩn bị/sửa prompt để sinh thêm ảnh sau giới hạn.
