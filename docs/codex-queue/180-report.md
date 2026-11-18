# Phiếu 180 · Ba bộ icon cài đặt trong trận

Ngày làm: 29/10/2026, macOS, repo cha. **Đã tạo 27 ảnh chọn và 81 bản thu, giữ đủ 28 lượt sinh cùng prompt. Chưa đóng phiếu:** ba cặp loa bật/tắt trượt IoU; kiểm mở rộng trên bản thu và cỡ hiển thị còn ngoại lệ alpha/sắc khóa. Dừng chỉnh hình để đuổi số theo ART_ACCEPTANCE §5; chờ Claude quyết các ngoại lệ và chấm nhận độc lập.

## 1. Nơi giao và bản cần xem

- **Wordwoven:** [9 ảnh gốc và 27 bản thu của bộ](../../games/typing-defense/art-src/ui/quick-settings/selected/). [Tờ xem cuối bốn hàng](../../games/typing-defense/art-src/_review/180-sheet-final.jpg).
- **Dragonhold:** [9 ảnh gốc và 27 bản thu của bộ](../../games/dragon-hold/art-src/ui/quick-settings/selected/). [Tờ xem cuối bốn hàng](../../games/dragon-hold/art-src/_review/180-sheet-final.jpg).
- **Last Line:** [9 ảnh gốc và 27 bản thu của bộ](../../games/typing-survival/art-src/ui/quick-settings/selected/). [Tờ xem cuối bốn hàng](../../games/typing-survival/art-src/_review/180-sheet-final.jpg).
- [Tờ so ba bộ cuối](../../games/typing-defense/art-src/_review/180-sets-final.jpg).
- Mỗi ảnh chọn có `.png`, `.256.png`, `.128.png`, `.64.png` và prompt cạnh từng file. Các `.tryN.png` cùng prompt nằm tại thư mục cha `ui/quick-settings/`, giữ nguyên byte nguồn công cụ. Chỉ dùng **`selected/`** để chấm bản cuối.
- Tờ bắt buộc theo tên ban đầu `180-sheet.jpg`, `180-sets.jpg` vẫn được giữ như hồ sơ sơ bộ. Tờ `*-final.jpg` mới là bản dùng để nhận, có `vol-master` Dragonhold đủ ba vòng âm.

Thêm thư mục con `selected/` và hậu tố `-final` để giữ mọi file đã xuất, tuân thủ lệnh không ghi đè/đổi tên/xóa. Đây là khác biệt đường dẫn so với phiếu. Các PNG ở ngay gốc `quick-settings/` và tờ không có `-final` là bản sơ bộ, không dùng khi tích hợp. Không có file tồn tại trước phiếu bị thay đổi.

## 2. Tham chiếu, prompt và lượt sinh

Dùng công cụ tích hợp `image_gen`, một lời gọi cho mỗi ảnh/lượt, tổng **28 lượt**; không gọi API/CLI tạo ảnh khác. Prompt mở bằng nguyên văn STYLE-UI mới tại ART_DIRECTION_2026-10-28 §2.2/§3.2/§4.3 B; tiếp theo là ICON của tài liệu định dạng Wordwoven và phần ưu tiên mới: khối vật liệu có chiều sâu, không viền mực/tô phẳng, lề 70%, hình rõ ở 20 px. Phần riêng đứng sau nên ghi đè các chỉ dẫn cũ về chi tiết, góc nhìn và lề. Kết thúc bằng nền M cho Wordwoven/Dragonhold; alpha thật cho Last Line. Prompt đầy đủ, chính xác nằm cạnh từng lượt, trong `prompts.json` và cạnh bản chọn; không gán prompt lượt 1 cho lượt 2.

Tham chiếu đính kèm từng lượt:

| Game | Ba ảnh tham chiếu bộ |
|---|---|
| Wordwoven | `ui/frames-epic/crest.png`, `ui/calls/call-build.png`, `ui/resources/gold.png` |
| Dragonhold | `ui/icons/speaker.png`, `ui/icons/keyboard.png`, `ui/icons/shield.png` |
| Last Line | `concepts/b-lightbearer-keyart.png`, `ui/icons/gun-xung.png`, `ui/icons/nova.png` |

Đường dẫn `ui/frames/crest.png` trong phiếu không có; dùng `frames-epic/crest.png` đang có. Đã xem ảnh chủ dự án `_refs/owner-epic-2026-10-28.webp`, lấy mức hoàn thiện và đưa crop HUD vào hàng 4; ảnh chủ dự án không được đính kèm vào các lời gọi sinh. Các ảnh bộ ở bảng là file hiện có, không khẳng định lại trạng thái nhận của từng file cũ. Loa tắt đính kèm thêm ảnh loa bật vừa sinh của chính game đó.

| Tên · áp dụng cho ba game | Phần riêng và thay đổi từng lượt | Bản chọn |
|---|---|---|
| `hud-settings` | Tám răng lớn và lỗ tâm rộng; đá vôi–ngọc–đồng ở Wordwoven, granite–sắt–vàng búa ở Dragonhold, ceramic trắng–vàng trắng–cyan ở Last Line. | try1 cả ba game |
| `hud-sound` | Loa quay phải, đúng hai vòng âm rời; ưu tiên thân loa lớn và khe âm rộng. | try1 cả ba game |
| `hud-sound-muted` | Đính kèm loa bật; giữ tư thế, bỏ vòng âm, thêm dấu gạch dày. Hình nhận ra được ở 32 px nhưng khung chuẩn hóa làm tỉ lệ thân lệch, IoU toàn icon trượt. | try1 cả ba game |
| `vol-master` | Wordwoven/Last Line: loa và ba vòng âm. Dragonhold try1 sai còn hai vòng; try2 nhấn rõ ngắn–vừa–dài, ba khe rời, thân loa ngắn vuông và chùm vòng chiếm hai phần ba bên phải. Đã đếm đủ ba vòng ở try2. | Dragonhold try2; hai game kia try1 |
| `vol-music` | Hai nốt nối bằng một thanh lớn, chiếm phần trên; loa nhỏ ở góc dưới phải. | try1 cả ba game |
| `vol-effects` | Tia lóe góc cạnh lớn phía trên trái, loa nhỏ ở dưới phải; hình chéo có khuyết sâu. | try1 cả ba game |
| `vol-keyboard` | Một keycap trống, nhìn ba phần tư để thấy mặt trên và hai bên, đế dày rõ. | try1 cả ba game |
| `vol-voice` | Bong bóng thoại bầu dục có đuôi lớn ở dưới trái; vòng âm bên phải, không thêm loa. | try1 cả ba game |
| `vol-interface` | Con trỏ lớn chạm nút nhỏ; hai tia báo chạm, khe lớn giữa con trỏ và nút. | try1 cả ba game |

Không ảnh nào dùng quá hai lượt. Kiểm nguồn bằng `md5 -r`: **28/28 PNG thử trùng nguồn công cụ**; mọi lượt đều còn prompt. `sources.json` của mỗi game và `vol-master.try2.source.json` giữ nguồn và tham chiếu. Không tạo âm thanh; Q6 không phát sinh trong phiếu ảnh này.

## 3. Hậu kỳ và tờ bản sinh | bản hậu kỳ

Bản thử giữ nguyên 1254² từ công cụ. Wordwoven và Dragonhold tách M bằng mặt nạ hue cách 300° tối đa 25°, saturation >0.32; không thay RGB phần vật. Last Line giữ alpha do công cụ trả. Cắt theo alpha >16, Lanczos fit 717 px, căn giữa canvas 1024² sRGB PNG32. Không chỉnh sáng/gamma hay vẽ phủ. Chốt alpha ngoài dải mép 3 px theo mặt nạ alpha ≥128; toàn bộ RGB giữ nguyên, alpha trong dải mép giữ nguyên. Last Line chủ yếu sửa 253→255 ở mặt vật liệu đặc. Nhật ký từng ảnh trong `clean/<tên>.alpha.json` ghi số pixel và độ đổi alpha lớn nhất; một số pixel Wordwoven/Dragonhold đổi alpha nhiều do lỗ mặt nạ nhỏ, nên đã xem tờ so để kiểm phần vẽ.

Bản thu cuối dùng **Lanczos hai thùy** (`-filter Lanczos -define filter:lobes=2`), thu trực tiếp từ 1024 cho từng 256/128/64. Không nối chuỗi và không làm nét. Chọn hai thùy để giảm ringing mà giữ đúng họ lọc Lanczos; vẫn có ngoại lệ nhỏ ghi ở mục 5. Cỡ hiển thị 20/28/32/44 trên tờ xem và phép đo dùng Lanczos mặc định. Không chốt lại alpha hay đổi màu sau khi thu: giữ phép thu trực tiếp và công khai số trượt.

**Wordwoven** — tờ so cùng canvas 256², nhãn “Bản sinh | Bản hậu kỳ”, trên đúng bản chọn:

[hud-settings](../../games/typing-defense/art-src/_review/180/hud-settings.compare-final.jpg) · [hud-sound](../../games/typing-defense/art-src/_review/180/hud-sound.compare-final.jpg) · [hud-sound-muted](../../games/typing-defense/art-src/_review/180/hud-sound-muted.compare-final.jpg) · [vol-master](../../games/typing-defense/art-src/_review/180/vol-master.compare-final.jpg) · [vol-music](../../games/typing-defense/art-src/_review/180/vol-music.compare-final.jpg) · [vol-effects](../../games/typing-defense/art-src/_review/180/vol-effects.compare-final.jpg) · [vol-keyboard](../../games/typing-defense/art-src/_review/180/vol-keyboard.compare-final.jpg) · [vol-voice](../../games/typing-defense/art-src/_review/180/vol-voice.compare-final.jpg) · [vol-interface](../../games/typing-defense/art-src/_review/180/vol-interface.compare-final.jpg)

**Dragonhold** — tờ so cùng canvas 256², nhãn “Bản sinh | Bản hậu kỳ”, trên đúng bản chọn:

[hud-settings](../../games/dragon-hold/art-src/_review/180/hud-settings.compare-final.jpg) · [hud-sound](../../games/dragon-hold/art-src/_review/180/hud-sound.compare-final.jpg) · [hud-sound-muted](../../games/dragon-hold/art-src/_review/180/hud-sound-muted.compare-final.jpg) · [vol-master](../../games/dragon-hold/art-src/_review/180/vol-master.compare-final.jpg) · [vol-music](../../games/dragon-hold/art-src/_review/180/vol-music.compare-final.jpg) · [vol-effects](../../games/dragon-hold/art-src/_review/180/vol-effects.compare-final.jpg) · [vol-keyboard](../../games/dragon-hold/art-src/_review/180/vol-keyboard.compare-final.jpg) · [vol-voice](../../games/dragon-hold/art-src/_review/180/vol-voice.compare-final.jpg) · [vol-interface](../../games/dragon-hold/art-src/_review/180/vol-interface.compare-final.jpg)

**Last Line** — tờ so cùng canvas 256², nhãn “Bản sinh | Bản hậu kỳ”, trên đúng bản chọn:

[hud-settings](../../games/typing-survival/art-src/_review/180/hud-settings.compare-final.jpg) · [hud-sound](../../games/typing-survival/art-src/_review/180/hud-sound.compare-final.jpg) · [hud-sound-muted](../../games/typing-survival/art-src/_review/180/hud-sound-muted.compare-final.jpg) · [vol-master](../../games/typing-survival/art-src/_review/180/vol-master.compare-final.jpg) · [vol-music](../../games/typing-survival/art-src/_review/180/vol-music.compare-final.jpg) · [vol-effects](../../games/typing-survival/art-src/_review/180/vol-effects.compare-final.jpg) · [vol-keyboard](../../games/typing-survival/art-src/_review/180/vol-keyboard.compare-final.jpg) · [vol-voice](../../games/typing-survival/art-src/_review/180/vol-voice.compare-final.jpg) · [vol-interface](../../games/typing-survival/art-src/_review/180/vol-interface.compare-final.jpg)

Các tờ `*.compare.jpg`/`*.before-after.jpg` là bước sơ bộ và vẫn được giữ. Tự chấm cuối dựa trên ảnh hậu kỳ `selected/`, đã xem đủ 27 bản 1024 và ba tờ cỡ sử dụng; không lấy bản sinh để thay điểm bản giao.

## 4. KA1, khổ và phương pháp đo

Lúc bắt đầu, cả ba thư mục quick-settings, các đường dẫn review/180* và báo cáo đều chưa tồn tại: **0 file có trước**. `md5-before.txt` của mỗi game rỗng. `snapshot.py` gọi `/sbin/md5 -r` mọi file trong quick-settings, review/180*, kèm báo cáo; lưu `md5-after.txt`, rồi `diff -u` với mốc trước. Chỉ loại hai file tự tham chiếu `md5-after.txt` và `md5.diff.txt`. Diff chỉ thêm, không có dòng dữ liệu bị sửa/xóa. Vì mốc trước rỗng, kiểm này bảo đảm phạm vi file đích được thêm mới, không thay cho kiểm toàn repo.

**108/108 PNG chọn đúng kích thước và kênh `srgba`; 81/81 bản thu khớp pixel phép Lanczos trực tiếp; 108/108 file chọn trùng bản sạch trong review.** `identify-selected.txt` của mỗi game dùng `magick identify -format '%f %wx%h %[channels]\n'`. Cả 27 ảnh gốc có cạnh dài alpha >16 bằng **717/1024 = 70.0195%**, lệch tâm lớn nhất **0.04883%**; đều trong 68–72% và ≤2%.

Alpha lẻ: 0<a<255, ở ngoài vùng lân cận Chebyshev bán kính 3 px có cả mặt nạ trong/ngoài (alpha ≥128). Sắc khóa: |hue−300°|≤15°, S>0.5, mẫu số là mọi pixel alpha >0. Luma: Rec.709 trên sRGB chuẩn hóa 0–1, trung bình trọng số alpha; bảng ghi chênh với nền tối. IoU: alpha >16 sau Lanczos về 32 px, và 20 px cho sáu nhóm âm lượng; đo đủ mọi cặp, tách riêng cặp loa bật/tắt. Đây là kiểm ảnh tĩnh, không phải playtest.

| Game | Nền tối / sáng | Δ luma tối nhỏ nhất ở 720p | IoU lớn nhất sáu vol ở 20 px | IoU lớn nhất khác cặp loa ở 32 px |
|---|---|---:|---:|---:|
| Wordwoven | `#061e16` / `#b8aa94` | 0.3310 | 0.7280 | 0.7993 |
| Dragonhold | `#2b2118` / `#f1e3c4` | 0.2710 | 0.6899 | 0.7400 |
| Last Line | `#14181f` / `#8c96a3` | 0.4671 | 0.6621 | 0.7508 |

Hai màu Wordwoven đo từ `frames-epic/panel-large.v2.png` quy về 1024²: ROI 200×200+412+412 → #061e16; ROI 200×20+412+26 → #b8aa94. Hai game còn lại dùng đúng màu phiếu. Mỗi ảnh 720p/1080p được đặt trên cả hai màu ở tờ bốn hàng; số sáng cũng có trong JSON.

### Wordwoven

| Ảnh chọn | Alpha lẻ ngoài mép · 1024 | Sắc M · 1024 (%) | Δ luma tối · 720 / 1080 | IoU max · 32 px, bỏ cặp loa | IoU max vol · 20 px |
|---|---:|---:|---|---|---|
| `hud-settings` | 0 | 0.0726 | 0.4516 / 0.4516 | 0.7933 · `vol-keyboard` | — |
| `hud-sound` | 0 | 0.1384 | 0.4390 / 0.4396 | 0.7993 · `vol-master` | — |
| `hud-sound-muted` | 0 | 0.0926 | 0.4648 / 0.4647 | 0.6771 · `vol-effects` | — |
| `vol-master` | 0 | 0.1245 | 0.4563 / 0.4568 | 0.7993 · `hud-sound` | 0.7280 |
| `vol-music` | 0 | 0.0975 | 0.4136 / 0.4139 | 0.6240 · `hud-sound-muted` | 0.6174 |
| `vol-effects` | 0 | 0.1733 | 0.4623 / 0.4626 | 0.6771 · `hud-sound-muted` | 0.6174 |
| `vol-keyboard` | 0 | 0.0495 | 0.4404 / 0.4414 | 0.7933 · `hud-settings` | 0.7055 |
| `vol-voice` | 0 | 0.0489 | 0.3310 / 0.3292 | 0.6741 · `vol-master` | 0.7280 |
| `vol-interface` | 0 | 0.1410 | 0.4552 / 0.4573 | 0.6522 · `vol-voice` | 0.6829 |

### Dragonhold

| Ảnh chọn | Alpha lẻ ngoài mép · 1024 | Sắc M · 1024 (%) | Δ luma tối · 720 / 1080 | IoU max · 32 px, bỏ cặp loa | IoU max vol · 20 px |
|---|---:|---:|---|---|---|
| `hud-settings` | 0 | 0.0539 | 0.4088 / 0.4085 | 0.6829 · `vol-keyboard` | — |
| `hud-sound` | 0 | 0.1088 | 0.3600 / 0.3598 | 0.7400 · `vol-master` | — |
| `hud-sound-muted` | 0 | 0.0870 | 0.3735 / 0.3731 | 0.6364 · `vol-master` | — |
| `vol-master` | 0 | 0.0606 | 0.3904 / 0.3859 | 0.7400 · `hud-sound` | 0.6899 |
| `vol-music` | 0 | 0.0744 | 0.3737 / 0.3757 | 0.5906 · `vol-effects` | 0.6364 |
| `vol-effects` | 0 | 0.1722 | 0.4585 / 0.4601 | 0.6045 · `hud-sound-muted` | 0.6364 |
| `vol-keyboard` | 0 | 0.0451 | 0.3946 / 0.3940 | 0.6829 · `hud-settings` | 0.6738 |
| `vol-voice` | 0 | 0.0600 | 0.2710 / 0.2692 | 0.6706 · `vol-keyboard` | 0.6899 |
| `vol-interface` | 0 | 0.1157 | 0.3915 / 0.3926 | 0.5142 · `vol-effects` | 0.5299 |

### Last Line

| Ảnh chọn | Alpha lẻ ngoài mép · 1024 | Sắc M · 1024 (%) | Δ luma tối · 720 / 1080 | IoU max · 32 px, bỏ cặp loa | IoU max vol · 20 px |
|---|---:|---:|---|---|---|
| `hud-settings` | 0 | 0.0440 | 0.4708 / 0.4700 | 0.7265 · `vol-keyboard` | — |
| `hud-sound` | 0 | 0.0158 | 0.4671 / 0.4680 | 0.7508 · `vol-master` | — |
| `hud-sound-muted` | 0 | 0.0262 | 0.4883 / 0.4894 | 0.6772 · `vol-keyboard` | — |
| `vol-master` | 0 | 0.0024 | 0.4881 / 0.4859 | 0.7508 · `hud-sound` | 0.6621 |
| `vol-music` | 0 | 0.0241 | 0.4828 / 0.4796 | 0.5360 · `vol-keyboard` | 0.5706 |
| `vol-effects` | 0 | 0.0105 | 0.5633 / 0.5631 | 0.5684 · `hud-sound-muted` | 0.5705 |
| `vol-keyboard` | 0 | 0.0072 | 0.5817 / 0.5829 | 0.7265 · `hud-settings` | 0.6621 |
| `vol-voice` | 0 | 0.0308 | 0.4741 / 0.4727 | 0.5162 · `hud-settings` | 0.5263 |
| `vol-interface` | 0 | 0.0340 | 0.4694 / 0.4686 | 0.4635 · `vol-keyboard` | 0.5000 |

## 5. Ngoại lệ số đo và điểm phải để Claude quyết

**Không đánh dấu mọi kiểm 1–5 đã đạt.** Bản gốc 1024 của cả 27 ảnh đạt alpha/sắc khóa; kiểm mở rộng 81 bản thu phát hiện **23 file có 1–27 pixel alpha lẻ ngoài dải mép**, và hai cỡ hiển thị có sắc khóa vượt ngưỡng theo phép đếm pixel không trọng số alpha. Các số không bị che bằng đổi định nghĩa sau khi kiểm.

| Game | Ảnh | Bản thu trượt alpha: cỡ → số pixel |
|---|---|---|
| Wordwoven | `hud-sound` | 256 → 6; 128 → 4 |
| Wordwoven | `hud-sound-muted` | 256 → 12; 128 → 6; 64 → 2 |
| Wordwoven | `vol-music` | 256 → 3; 128 → 3 |
| Dragonhold | `hud-settings` | 256 → 4; 128 → 3 |
| Dragonhold | `hud-sound` | 256 → 5; 128 → 4; 64 → 1 |
| Dragonhold | `hud-sound-muted` | 256 → 20; 128 → 10; 64 → 3 |
| Dragonhold | `vol-music` | 64 → 6 |
| Dragonhold | `vol-effects` | 128 → 1 |
| Dragonhold | `vol-voice` | 256 → 27; 128 → 13; 64 → 7 |
| Dragonhold | `vol-interface` | 256 → 22; 128 → 2 |
| Last Line | `hud-sound-muted` | 256 → 1 |

| Game | Ảnh, cỡ hiển thị | Sắc M / mọi pixel alpha >0 (%) |
|---|---|---:|
| Wordwoven | `vol-interface` · 20 px | 0.6494 |
| Dragonhold | `hud-sound` · 32 px | 0.5988 |

Không ép alpha các bản thu vì khi đó chúng không còn khớp pixel phép thu trực tiếp; không đổi màu phần vẽ để đuổi tỉ lệ tính cả pixel alpha rất thấp. Đây là ngoại lệ giữ lại theo §5, không phải xác nhận các ngưỡng đã đạt. Mép Last Line ở 1024 còn vài điểm màu/halo từ nguồn; không xóa phần vẽ đó bằng mặt nạ mạnh hơn.

| Cặp loa bật/tắt | IoU toàn icon 32 px | IoU ROI thân phụ | Kết luận |
|---|---:|---:|---|
| Wordwoven | 0.6419 | 0.7917 | Trượt cả ≥0.90 riêng và ≥0.95 chung |
| Dragonhold | 0.6687 | 0.8111 | Trượt cả ≥0.90 riêng và ≥0.95 chung |
| Last Line | 0.6649 | 0.7078 | Trượt cả ≥0.90 riêng và ≥0.95 chung |

ROI thân phụ là x=0..614, y=0..1024 trên canvas cuối, thu về 20×32; vẫn chứa phần dấu gạch nên chỉ để xem ảnh hưởng thay ký hiệu, không thay kiểm toàn icon. Loa giữ hướng quay phải và nhận diện vật liệu, nhưng bỏ vòng âm/thêm gạch và chuẩn hóa lại hộp bao làm mặt nạ đổi nhiều; không chứng minh được yêu cầu cùng tư thế bằng ngưỡng đã đặt. Ở 32 px vẫn phân biệt rõ bật/tắt. Giữ hai ảnh đẹp để Claude quyết cách xử lý thay vì vẽ kín khoảng trống hoặc giữ vòng âm trong icon tắt nhằm tăng IoU.

Nếu hiểu “hai ảnh bất kỳ trong phiếu” bao gồm cả **ba game**, có **11 cặp khác game** vượt 0.80 ở 32 px. Cặp lớn nhất: Wordwoven `vol-keyboard` / Last Line `vol-keyboard` = **0.9268**. Hình cùng nghĩa giữa ba bộ có chủ ý tương đồng, nhưng không dùng điều đó để tự miễn ngưỡng toàn phiếu. Bảng max từng ảnh bên dưới là số đo xuyên game; các cặp nội bộ từng game đã có ở mục 4. Danh sách đủ 243 cặp xuyên game nằm trong `final-audit-all-games.json`.

| Ảnh | IoU max xuyên game 32 px | Ảnh đối chiếu |
|---|---:|---|
| `typing-defense/hud-settings` | 0.8722 | `dragon-hold/hud-settings` |
| `typing-defense/hud-sound` | 0.8938 | `typing-survival/hud-sound` |
| `typing-defense/hud-sound-muted` | 0.7953 | `dragon-hold/hud-sound-muted` |
| `typing-defense/vol-master` | 0.8809 | `typing-survival/vol-master` |
| `typing-defense/vol-music` | 0.8222 | `dragon-hold/vol-music` |
| `typing-defense/vol-effects` | 0.6559 | `dragon-hold/hud-sound-muted` |
| `typing-defense/vol-keyboard` | 0.9268 | `typing-survival/vol-keyboard` |
| `typing-defense/vol-voice` | 0.7603 | `dragon-hold/vol-voice` |
| `typing-defense/vol-interface` | 0.7138 | `typing-survival/vol-interface` |
| `dragon-hold/hud-settings` | 0.8722 | `typing-defense/hud-settings` |
| `dragon-hold/hud-sound` | 0.8676 | `typing-defense/hud-sound` |
| `dragon-hold/hud-sound-muted` | 0.7953 | `typing-defense/hud-sound-muted` |
| `dragon-hold/vol-master` | 0.8357 | `typing-survival/vol-master` |
| `dragon-hold/vol-music` | 0.8222 | `typing-defense/vol-music` |
| `dragon-hold/vol-effects` | 0.6544 | `typing-defense/vol-effects` |
| `dragon-hold/vol-keyboard` | 0.8905 | `typing-defense/vol-keyboard` |
| `dragon-hold/vol-voice` | 0.7603 | `typing-defense/vol-voice` |
| `dragon-hold/vol-interface` | 0.5567 | `typing-survival/vol-effects` |
| `typing-survival/hud-settings` | 0.7938 | `typing-defense/hud-settings` |
| `typing-survival/hud-sound` | 0.8938 | `typing-defense/hud-sound` |
| `typing-survival/hud-sound-muted` | 0.7480 | `dragon-hold/hud-sound-muted` |
| `typing-survival/vol-master` | 0.8809 | `typing-defense/vol-master` |
| `typing-survival/vol-music` | 0.7713 | `typing-defense/vol-music` |
| `typing-survival/vol-effects` | 0.6476 | `dragon-hold/vol-effects` |
| `typing-survival/vol-keyboard` | 0.9268 | `typing-defense/vol-keyboard` |
| `typing-survival/vol-voice` | 0.6864 | `typing-defense/vol-voice` |
| `typing-survival/vol-interface` | 0.7138 | `typing-defense/vol-interface` |

## 6. KA5 trên bản hậu kỳ chọn

Thứ tự điểm: **Đúng đề / Đọc được / Hợp bộ / Hình khối / Dùng tiếp**, mỗi mục 0–2. Tất cả “Dùng tiếp” chỉ **1**, vì còn các kiểm số trượt của bộ; không dùng tổng ≥8 để coi phiếu đã xong. Điểm là tự chấm so với độ hoàn thiện HUD game thương mại trong ảnh chủ dự án; **chưa có chấm độc lập của Claude**.

| Game | Ảnh | 1024: năm điểm → tổng | 720p: năm điểm → tổng | Thiếu còn lại |
|---|---|---|---|---|
| Wordwoven | `hud-settings` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Wordwoven | `hud-sound` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Wordwoven | `hud-sound-muted` | 2 / 2 / 2 / 1.5 / 1 → **8.5** | 2 / 2 / 2 / 1.5 / 1 → **8.5** | Dấu gạch rõ; thân và hộp bao không khớp ngưỡng loa bật. |
| Wordwoven | `vol-master` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Wordwoven | `vol-music` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Wordwoven | `vol-effects` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Wordwoven | `vol-keyboard` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Wordwoven | `vol-voice` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Wordwoven | `vol-interface` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Dragonhold | `hud-settings` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Dragonhold | `hud-sound` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Dragonhold | `hud-sound-muted` | 2 / 2 / 2 / 1.5 / 1 → **8.5** | 2 / 2 / 2 / 1.5 / 1 → **8.5** | Dấu gạch rõ; thân và hộp bao không khớp ngưỡng loa bật. |
| Dragonhold | `vol-master` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Dragonhold | `vol-music` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Dragonhold | `vol-effects` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Dragonhold | `vol-keyboard` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 2 / 2 / 2 / 1 → **9** | Chi tiết chạm khắc mất khi thu; xem ngoại lệ bộ ở mục 5. |
| Dragonhold | `vol-voice` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1 / 2 / 2 / 1 → **8** | Mặt sắt tối, chênh luma 0.271 sát ngưỡng; đuôi thoại còn rõ. |
| Dragonhold | `vol-interface` | 2 / 2 / 2 / 2 / 1 → **9** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Dáng đọc được; chi tiết loa/vòng âm nhỏ ở 20 px, chưa thật thoáng. |
| Last Line | `hud-settings` | 1.5 / 2 / 1.5 / 2 / 1 → **8** | 1.5 / 1.5 / 2 / 2 / 1 → **8** | Răng nhọn thiên turbine/huy hiệu; còn nhận là bánh răng, cần Claude chấm kỹ. |
| Last Line | `hud-sound` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 2 / 2 / 2 / 1 → **9** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `hud-sound-muted` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 2 / 2 / 1.5 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-master` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-music` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-effects` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-keyboard` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 2 / 2 / 2 / 1 → **9** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-voice` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |
| Last Line | `vol-interface` | 2 / 2 / 1.5 / 2 / 1 → **8.5** | 2 / 1.5 / 2 / 2 / 1 → **8.5** | Mép nguồn còn điểm màu ở 1024; vật liệu trắng–cyan đọc tốt khi thu. |

## 7. Script, kiểm lại và việc chưa làm

Tất cả script nằm tại `games/typing-defense/art-src/_review/180/`; không sửa công cụ chung. Các script Node chỉ đọc nguồn đã giữ và ghi trong quick-settings/review/180*. Hàm ghi giữ file đã có nếu cùng byte, dừng nếu khác để không ghi đè. Chạy ở repo cha:

```sh
export ART_MAGICK=/opt/homebrew/bin/magick
node games/typing-defense/art-src/_review/180/process.mjs typing-defense
node games/typing-defense/art-src/_review/180/finish.mjs typing-defense
node games/typing-defense/art-src/_review/180/audit-selected.mjs typing-defense
node games/typing-defense/art-src/_review/180/final-audit.mjs
```

Lặp ba lệnh đầu với `dragon-hold` và `typing-survival` để kiểm từng game. `process.mjs` tái hiện bước sơ bộ; `finish.mjs` tạo ứng viên alpha sạch trong `review/180/clean`; `selection.json` chỉ đích giao `selected/`, không tự ghi đè bản trước. `sheets.mjs` và `sheets-final.mjs` dựng tờ xem; `report.py` tạo báo cáo nếu chưa có; `snapshot.py` lưu mốc sau một lần. Báo cáo số cuối: `metrics-selected.json`, `identify-selected.txt`, `final-audit.json` của từng game và `final-audit-all-games.json` trong review Wordwoven.

Không chạy Git, build, test suite game, dev server, trình duyệt hay mạng ngoài công cụ tạo ảnh; không tạo âm thanh, tích hợp runtime hoặc chép public. Không đọc/ghi Tu Tiên, không đụng `.wt-*`, không sửa file của làn khác. Không có capture trình duyệt/raw frame cần prune. Không xóa file nào. Không ghi ART_REPLACE_LATER vì ngoài phạm vi; mọi thiếu sót và điểm sát ngưỡng đã ghi ở đây để Claude xử lý khi nhận.

**Chủ dự án/Claude cần xem:** tờ `180-sets-final.jpg`, riêng bánh răng Last Line ở 32 px; ba cặp loa cùng ngưỡng IoU; các ngoại lệ alpha/sắc khóa và cách hiểu IoU xuyên game. Đủ ảnh và cỡ thu nhưng chưa đáp ứng câu “mọi kiểm 1–5 đạt”; chưa ghi nhận, chưa tích hợp.
