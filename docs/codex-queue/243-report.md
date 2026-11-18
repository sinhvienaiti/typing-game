# Phiếu 243 · Last Line · Icon Settings, Sound và Options

**Ngày:** 31/10/2026. **Trạng thái:** đã tạo đủ 6 icon vẽ lại và 4 icon mới, giao đủ 40 PNG cùng prompt; chờ Claude chấm trong game. Các kiểm hình, kích thước, lề, độ đặc, độ phủ, tương phản, IoU và bảo toàn file cũ đạt. **Kiểm alpha tuyệt đối trên các bản thu chưa đạt hoàn toàn**: giữ Lanczos trực tiếp và ghi ngoại lệ bên dưới theo ART_ACCEPTANCE §5; không tuyên bố toàn bộ kiểm số đã qua.

## 1. Ảnh giao và lượt sinh

Dùng công cụ `image_gen` tích hợp, mỗi ảnh một lần gọi riêng. Tham chiếu vật liệu đính kèm: `streak.png`, `lock.png`, `mag-full.png`; riêng HUD Settings dùng thêm bánh răng menu vừa sinh, cùng hai icon đã nhận. Đã xem ảnh tham chiếu thương mại `owner-epic-2026-10-28.webp` để đối chiếu mức hoàn thiện, không chép nội dung.

Prompt giữ STYLE-UI, KIND ICON và SMALL-SIZE; phần ưu tiên của phiếu dùng sứ ngà, thép sáng, mép than chì dày và một màu nhấn lam. Chữ A ở hai icon được ghi rõ ngoại lệ trong prompt, không sửa nét chữ bằng tay.

| Icon | Bản chọn trong `games/typing-survival/art-src/` | Lượt chọn |
|---|---|---:|
| `menu-settings` | `ui/icons/menu-settings.r2.png` | 1 |
| `hud-settings` | `ui/quick-settings/selected/hud-settings.r2.png` | 1 |
| `pace-director` | `ui/icons/pace-director.r2.png` | 1 |
| `shake` | `ui/icons/shake.r2.png` | 1 |
| `vol-effects` | `ui/quick-settings/selected/vol-effects.r2.png` | 2 |
| `vol-interface` | `ui/quick-settings/selected/vol-interface.r2.png` | 1 |
| `ship` | `ui/icons/ship.png` | 1 |
| `letter-style` | `ui/icons/letter-style.png` | 1 |
| `effect-strength` | `ui/icons/effect-strength.png` | 1 |
| `word-size` | `ui/icons/word-size.png` | 1 |

Mỗi bản chọn có master 1024², bản 256², 128², 64²; sRGB, RGBA 8 bit. Mỗi PNG có prompt đúng của lượt sinh ở tên `.prompt.txt` bên cạnh, gồm cả bản thu. Tổng 11 lượt sinh; giữ nguyên tất cả PNG và prompt thử. Không có lượt thứ tư.

- Hai bánh răng: tám răng đầu vuông, cùng lỗ tròn; HUD có tấm thép phía sau. Giữ nguyên `hud-sound` và `hud-sound-muted`.
- Pace: mặt đồng hồ bán nguyệt và cặp mũi tên điều chỉnh. Shake: hai màn hình lệch nhau và nét chuyển động hai bên.
- Effects lượt một còn gợi bánh răng phát âm. Lượt hai sửa prompt đúng lỗi này: lõi va chạm liền, tia ngắn không đều, bỏ vành bánh răng; giữ hai cung âm. Chọn lượt hai, không sửa hình bằng công cụ.
- Interface có con trỏ và toàn bộ nút chữ nhật. Ship, Letter style, Effect strength, Word size dùng lượt đầu. Các chữ A có hai chân, khoảng rỗng và gạch ngang đọc được ở 28 px.

## 2. Hậu kỳ và bằng chứng hình

Cắt theo hộp alpha > 16, thu đều để cạnh dài đạt 717 px rồi đệm trong suốt lên 1024²; không co không đều. Ảnh công cụ có phần đặc chủ yếu alpha 253. Bước làm sạch chỉ thay alpha ngoài dải biên 3 px quanh cả ngưỡng 16 và 128; RGB từng pixel giữ nguyên. Đã kiểm bằng byte trên cả mười master. Không thêm hình vẽ, không phủ tranh, không chỉnh màu hoặc làm nét.

Các bản thu lấy thẳng từ master đã làm sạch bằng Lanczos mặc định, không qua 256 hoặc 128 trung gian, không làm nét bản 64. Kiểm so sánh byte xác nhận đủ 30/30 bản thu đúng phép này.

- [Tờ xem sáu hàng, bản đủ nhãn](../../games/typing-survival/art-src/_review/243-sheet-v2.jpg).
- [Ô 720p đúng 1× trên hai mảnh UI](243/sheets-v2/real-size-720-1x.png).
- [Letter style cạnh Word size và Effect strength ở 28 px](243/sheets-v2/letters-compare-28px.png).
- Các ô 1080p 1×, 720p 1× và 720p ×4 nearest: `243/sheets-v2/<tên>-<cỡ>-<button|panel>.png`, bản phóng `<tên>-720-panel-4x.png`.
- Tờ “bản sinh | bản hậu kỳ” riêng từng icon: `243/candidates-final/<tên>-before-after.png`.

Mảnh UI là pixel cắt nguyên từ `ui/frames-epic/button.png` và `panel-large.png`, không tô lại nền. Bản rộng cắt `560x64+220+160` và `560x64+230+230`; font Arial hệ thống, chiều cao chữ hoa xấp xỉ 60% cỡ icon. Tờ `243-sheet.jpg` đầu tiên giữ nguyên để bảo toàn file; nhãn Pace bị cắt trên bản đó. Dùng `243-sheet-v2.jpg` làm tờ duyệt chính. Hai tờ đều có hàng đối chiếu và hàng cũ/mới; icon mới ghi “New asset”.

## 3. Kiểm 1–7: số đo

[Identify](243/audit-final/identify.txt), [tóm tắt kiểm giao](243/audit-final/summary.json), [toàn bộ số đo](243/candidates-final/metrics.json), [45 cặp IoU ở 32 px](243/audit-final/all-pairs-32px.json).

**KA1:** trước có 836 file trong các thư mục đích đã tồn tại. Sau giao có 940 file, thêm 104, đổi 0, mất 0; diff chỉ thêm. Các thư mục hồ sơ và báo cáo 243 chưa có trước lượt này. Xem `243/md5-before.txt`, `243/audit-final/md5-after.txt`, `243/audit-final/md5-diff.txt`; bản băm toàn bộ hồ sơ cuối ở `243/audit-all/`.

Tất cả hộp alpha có cạnh dài **70,0195%**, lệch tâm tối đa **0,0488%**, nằm trong ngưỡng 68–72% và ≤2%. Master đều có **0 pixel alpha bán trong suốt ngoài dải mép 3 px** ở cả hai cách xác định biên. Không dùng nền khóa; vẫn đo màu magenta như kiểm nhiễm nền, tối đa trên mọi file là **0,1209%**, dưới 0,2%.

| Icon | Cỡ 720/1080 | Mở 2×2 còn (%) | Độ phủ hộp (%) | Δ luma panel 720p | IoU đối chiếu lớn nhất* |
|---|---:|---:|---:|---:|---:|
| `menu-settings` | 28/40 | 98.72 | 58.75 | 0.473 | 0.603 |
| `hud-settings` | 32/44 | 97.85 | 67.15 | 0.436 | 0.655 |
| `pace-director` | 28/40 | 99.56 | 71.56 | 0.426 | 0.729 |
| `shake` | 28/40 | 92.50 | 75.00 | 0.289 | 0.546 |
| `vol-effects` | 24/36 | 91.80 | 54.46 | 0.487 | 0.743 |
| `vol-interface` | 24/36 | 98.68 | 67.86 | 0.425 | 0.681 |
| `ship` | 28/40 | 100.00 | 43.68 | 0.411 | 0.422 |
| `letter-style` | 28/40 | 98.94 | 55.59 | 0.466 | 0.552 |
| `effect-strength` | 28/40 | 97.91 | 59.13 | 0.424 | 0.386 |
| `word-size` | 28/40 | 98.36 | 50.83 | 0.425 | 0.512 |

\* Lấy lớn hơn giữa hai ngưỡng alpha >16 và >128. Bảng chi tiết từng đối chiếu:

| Icon | Đối chiếu | IoU >16 / >128 |
|---|---|---:|
| `menu-settings` | `quality` | 0.522 / 0.481 |
| `menu-settings` | `menu-mode` | 0.603 / 0.507 |
| `hud-settings` | `hud-sound` | 0.632 / 0.504 |
| `hud-settings` | `hud-sound-muted` | 0.655 / 0.601 |
| `pace-director` | `clock.r2` | 0.723 / 0.729 |
| `pace-director` | `stat-wpm.v2` | 0.719 / 0.709 |
| `shake` | `reduced-motion` | 0.546 / 0.481 |
| `shake` | `quality` | 0.405 / 0.407 |
| `vol-effects` | `vol-master` | 0.743 / 0.625 |
| `vol-effects` | `vol-music` | 0.503 / 0.384 |
| `vol-effects` | `surge` | 0.529 / 0.359 |
| `vol-interface` | `vol-keyboard` | 0.681 / 0.629 |
| `vol-interface` | `vol-voice` | 0.379 / 0.322 |
| `ship` | `menu-play` | 0.359 / 0.335 |
| `ship` | `armour` | 0.417 / 0.422 |
| `letter-style` | `word-size` | 0.512 / 0.416 |
| `letter-style` | `effect-strength` | 0.552 / 0.511 |
| `effect-strength` | `vol-master` | 0.386 / 0.322 |
| `effect-strength` | `stat-wpm.v2` | 0.378 / 0.373 |
| `word-size` | `letter-style` | 0.512 / 0.416 |

Mọi cặp khác bánh răng đạt IoU ≤0,80 ở cả hai ngưỡng; lớn nhất **0,744565**. Hai bánh răng đạt **0,949333** (>16) và **0,923547** (>128) ngay cả khi tính tấm thép của HUD.

Kiểm bổ sung bỏ vùng tấm thép lộ giữa tám răng: dùng cùng ROI tám khe cho hai mặt nạ, được **0,955017** ở 32 px. ROI 48 pixel, tâm (16,16), bán kính 7,8–10,4 px, cách trục răng hơn 16°. Đây là loại vùng khe đã định nghĩa hình học, không phải bộ tách vật liệu tự động hoàn chỉnh; ảnh đánh dấu giúp Claude xem phạm vi loại. [Số đo](243/gear-check-final/metrics.json), [mặt nạ và ROI đỏ ×8](243/gear-check-final/masks-8x.png). Phép đo full alpha phía trên cũng vượt 0,90, không phụ thuộc loại ROI.

**Ngoại lệ alpha bản thu:** Lanczos sinh một số pixel alpha gần 0 hoặc gần 255 ngoài dải Euclid 3 px. Bảng dưới là số pixel vi phạm theo biên >16 / >128, không làm tròn thành 0. Master 1024 đều 0/0. Đã thử kiểm thêm lõi lọc hai thùy trong bộ nhớ, không giải quyết toàn bộ trường hợp, không chọn thay phép thu mặc định.

| Icon | 256 px | 128 px | 64 px |
|---|---:|---:|---:|
| `menu-settings` | 117/0 | 40/0 | 29/0 |
| `hud-settings` | 50/1 | 34/0 | 27/0 |
| `pace-director` | 24/0 | 16/0 | 8/0 |
| `shake` | 150/1 | 76/19 | 39/14 |
| `vol-effects` | 123/0 | 40/0 | 14/2 |
| `vol-interface` | 139/2 | 53/6 | 31/0 |
| `ship` | 64/0 | 38/2 | 16/2 |
| `letter-style` | 233/4 | 81/1 | 45/7 |
| `effect-strength` | 192/4 | 67/1 | 148/3 |
| `word-size` | 121/2 | 60/6 | 36/0 |

Theo [ART_ACCEPTANCE §5](../games/ART_ACCEPTANCE.md), “Khi một ngưỡng số mâu thuẫn với tranh ... giữ tranh đẹp, ghi mâu thuẫn trong báo cáo để Claude quyết.” Giữ bản thu trực tiếp, dừng can thiệp alpha sau phép thu; làm sạch lại các bản thu sẽ khiến chúng không còn đúng byte của Lanczos trực tiếp. **Kiểm alpha tuyệt đối của bản thu đang chờ Claude quyết**, không tự cho qua. Không có nhiễm nền hay thay đổi RGB để chạy theo số.

## 4. Kiểm 8–10 và tự chấm

[Đọc không nhãn bản chọn](243/blind-notes-final.md), [ảnh đọc 1× không nhãn](243/candidates-final/blind-1x.png), [ghi nhận lượt đầu](243/blind-notes-v1.md). Đây là tự kiểm của người soạn prompt, không thay hai giám khảo độc lập; người đọc đã biết đề từ trước. Không nhận là thử mù độc lập.

| Icon | Đọc ở 720p 1× | Đúng đề | Đọc được | Hợp bộ | Hình khối | Dùng tiếp | Tổng |
|---|---|---:|---:|---:|---:|---:|---:|
| `menu-settings` | Bánh răng cơ khí | 2 | 2 | 2 | 2 | 1 | **9** |
| `hud-settings` | Bánh răng lỗ tròn | 2 | 2 | 2 | 2 | 1 | **9** |
| `pace-director` | Đồng hồ tốc độ | 2 | 2 | 2 | 2 | 1 | **9** |
| `shake` | Hai màn hình rung | 2 | 2 | 2 | 2 | 1 | **9** |
| `vol-effects` | Va chạm phát âm | 2 | 2 | 2 | 2 | 1 | **9** |
| `vol-interface` | Con trỏ nhấn nút | 2 | 2 | 2 | 2 | 1 | **9** |
| `ship` | Phi thuyền mũi nhọn | 2 | 2 | 2 | 2 | 1 | **9** |
| `letter-style` | Chữ A có sao | 2 | 2 | 2 | 2 | 1 | **9** |
| `effect-strength` | Ba cột tăng sáng | 2 | 2 | 2 | 2 | 1 | **9** |
| `word-size` | Hai chữ A | 2 | 2 | 2 | 2 | 1 | **9** |

Điểm tự chấm trên bản hậu kỳ tại ô 720p 1×, đối chiếu độ gọn và vật liệu của HUD thương mại. “Dùng tiếp” chỉ 1 vì ngoại lệ alpha bản thu còn chờ quyết. Các câu đọc không trùng cách đọc sai của phiếu. Hai chữ A có chân thẳng theo trục chữ, gạch ngang rõ, không có chữ khác; chưa có kiểm nhận trong game. Tia nhỏ ở Letter style và các nét chi tiết trên Pace vẫn cần Claude xem ở màn hình thật.

## 5. Chạy lại và phần để nguyên

Không cần Pillow, mạng, trình duyệt, server, build hoặc test game. Dùng Python chuẩn và ImageMagick 7 có sẵn. Các script giữ chế độ từ chối ghi đè; đổi tên thư mục đầu ra khi chạy lại:

```sh
python3 docs/codex-queue/243/process-final.py docs/codex-queue/243/recheck-1 docs/codex-queue/243/selection.json
python3 docs/codex-queue/243/audit.py audit-recheck-1
python3 docs/codex-queue/243/gear-check.py gear-recheck-1
```

`process-final.py` là quy trình hậu kỳ/đo bản chọn; `selection.json` chọn Effects lượt 2, các ảnh còn lại lượt 1. `sheets-wide.py` tạo tờ xem rộng và ô thật. `deliver.py` ghi bản chọn mới; đã chạy, chạy lần nữa sẽ từ chối ghi đè. Các script/vùng `v1`, `v2` còn lại là lịch sử xử lý, không dùng làm kết quả cuối.

Đã bỏ qua theo phạm vi phiếu: không đổi `hud-sound`, `hud-sound-muted`, bản icon cũ, mã, manifest, `public/`, âm thanh và các game khác; không đọc/ghi Tu Tiên, không chạy Git, build hoặc test game. Không tạo capture trình duyệt hoặc khung render, nên không có raw frame cần prune. Mọi ảnh thử do công cụ tạo được giữ nguyên.

**Claude/chủ dự án cần xem:** tờ `243-sheet-v2.jpg`, ô 1× và ô ba icon chữ; quyết ngoại lệ alpha bản thu; chấm lại đủ mười icon trong game tại 1280×720 và 1920×1080 trước khi nhận và trỏ manifest. Hiện chưa có điểm nhận độc lập hoặc chấp thuận của chủ dự án.

