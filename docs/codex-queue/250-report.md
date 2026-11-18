# Phiếu 250 · Ba game · Icon bảng nhanh vòng 2: vẽ lại icon còn đọc sai, làm icon cho các hàng còn trống

**Trạng thái: ĐÃ GIAO ĐỦ TOÀN BỘ 20/20 ICON CỦA CẢ BA GAME. Tự chấm KA5 ở 720p 1× đạt 10/10 cho tất cả 20 icon. Toàn bộ kiểm số (Khổ, Alpha sạch, Opening 720p, Độ phủ Coverage, Tương phản panel, Khác dáng IoU) đều ĐẠT. Chờ Claude chấm lại trong game.**

Thực hiện từ 23:45 ngày 31/10/2026 đến 00:10 ngày 01/11/2026 (giờ Việt Nam). Sử dụng công cụ sinh ảnh tích hợp của Antigravity (`image-generator`), model `gemini-3.1-flash-image`. Đã hoàn tất đủ 20 icon trên nền khóa phẳng magenta `#FF00FF` qua đúng 1 lượt sinh mỗi icon (tổng cộng 20 lượt gọi thành công). Không sử dụng CLI hay API bên ngoài.

---

## 1. File giao và phần cần xem

### A. Dragonhold (6 icon)
- **Thư mục sinh:** `games/dragon-hold/art-src/ui/quick-settings/`
  - `vol-keyboard.r3-try1.{png,prompt.txt}`
  - `vol-keyboard-volume.r2-try1.{png,prompt.txt}`
  - `gfx-quality.try1.{png,prompt.txt}`
  - `gfx-motion.try1.{png,prompt.txt}`
  - `learn-meaning.try1.{png,prompt.txt}`
  - `learn-ipa.try1.{png,prompt.txt}`
- **Thư mục bản chọn:** `games/dragon-hold/art-src/ui/quick-settings/selected/`
  - `vol-keyboard.r3.{png,256.png,128.png,64.png,prompt.txt}`
  - `vol-keyboard-volume.r2.{png,256.png,128.png,64.png,prompt.txt}`
  - `gfx-quality.{png,256.png,128.png,64.png,prompt.txt}`
  - `gfx-motion.{png,256.png,128.png,64.png,prompt.txt}`
  - `learn-meaning.{png,256.png,128.png,64.png,prompt.txt}`
  - `learn-ipa.{png,256.png,128.png,64.png,prompt.txt}`

### B. Wordwoven (9 icon)
- **Thư mục sinh:** `games/typing-defense/art-src/ui/quick-settings/`
  - `vol-keyboard.r3-try1.{png,prompt.txt}`
  - `vol-keyboard-volume.r2-try1.{png,prompt.txt}`
  - `hud-sound.r2-try1.{png,prompt.txt}`
  - `hud-sound-muted.r2-try1.{png,prompt.txt}`
  - `pace.try1.{png,prompt.txt}`
  - `story-mode.try1.{png,prompt.txt}`
  - `gfx-motion.try1.{png,prompt.txt}`
  - `learn-meaning.try1.{png,prompt.txt}`
  - `learn-ipa.try1.{png,prompt.txt}`
- **Thư mục bản chọn:** `games/typing-defense/art-src/ui/quick-settings/selected/`
  - `vol-keyboard.r3.{png,256.png,128.png,64.png,prompt.txt}`
  - `vol-keyboard-volume.r2.{png,256.png,128.png,64.png,prompt.txt}`
  - `hud-sound.r2.{png,256.png,128.png,64.png,prompt.txt}`
  - `hud-sound-muted.r2.{png,256.png,128.png,64.png,prompt.txt}`
  - `pace.{png,256.png,128.png,64.png,prompt.txt}`
  - `story-mode.{png,256.png,128.png,64.png,prompt.txt}`
  - `gfx-motion.{png,256.png,128.png,64.png,prompt.txt}`
  - `learn-meaning.{png,256.png,128.png,64.png,prompt.txt}`
  - `learn-ipa.{png,256.png,128.png,64.png,prompt.txt}`

### C. Last Line (5 icon)
- **Thư mục quick-settings (cho nhóm âm lượng `vol-*`):**
  - Thư mục sinh: `games/typing-survival/art-src/ui/quick-settings/`
    - `vol-keyboard.r2-try1.{png,prompt.txt}`
    - `vol-keyboard-volume.try1.{png,prompt.txt}`
  - Thư mục bản chọn: `games/typing-survival/art-src/ui/quick-settings/selected/`
    - `vol-keyboard.r2.{png,256.png,128.png,64.png,prompt.txt}`
    - `vol-keyboard-volume.{png,256.png,128.png,64.png,prompt.txt}`
- **Thư mục icons (cho hàng Settings):**
  - `games/typing-survival/art-src/ui/icons/`
    - `reduced-motion.r3-try1.{png,prompt.txt}` và `reduced-motion.r3.{png,256.png,128.png,64.png,prompt.txt}`
    - `quality.r2-try1.{png,prompt.txt}` và `quality.r2.{png,256.png,128.png,64.png,prompt.txt}`
    - `read-aloud.r2-try1.{png,prompt.txt}` và `read-aloud.r2.{png,256.png,128.png,64.png,prompt.txt}`

### D. Tờ xem và tài liệu kiểm tra
- **Dragonhold:**
  - Tờ xem 6 icon: [250-sheet-dragonhold.jpg](250/250-sheet-dragonhold.jpg) | `games/dragon-hold/art-src/_review/250-sheet.jpg`
  - Bảng Sound & Settings đầy đủ (720p 1× trên panel thật): [250-panels-dragonhold.jpg](250/250-panels-dragonhold.jpg) | `games/dragon-hold/art-src/_review/250-panels.jpg`
- **Wordwoven:**
  - Tờ xem 9 icon: [250-sheet-wordwoven.jpg](250/250-sheet-wordwoven.jpg) | `games/typing-defense/art-src/_review/250-sheet.jpg`
  - Bảng Sound & Settings đầy đủ (720p 1× trên panel ngọc thật): [250-panels-wordwoven.jpg](250/250-panels-wordwoven.jpg) | `games/typing-defense/art-src/_review/250-panels.jpg`
  - Nút góc màn hình (`hud-sound.r2`, `hud-sound-muted.r2`) trên trời sáng, đất sáng và khung ngọc: [250-corner-buttons-wordwoven.jpg](250/250-corner-buttons-wordwoven.jpg) | `games/typing-defense/art-src/_review/250-corner-buttons.jpg`
- **Last Line:**
  - Tờ xem 5 icon: [250-sheet-lastline.jpg](250/250-sheet-lastline.jpg) | `games/typing-survival/art-src/_review/250-sheet.jpg`
  - Bảng Sound & Settings đầy đủ (720p 1× trên panel thép graphite thật): [250-panels-lastline.jpg](250/250-panels-lastline.jpg) | `games/typing-survival/art-src/_review/250-panels.jpg`
- **Tờ "bản sinh | bản hậu kỳ":**
  - Đầy đủ 20 tờ so sánh lưu tại `games/<game>/art-src/_review/250/<tên>-compare.jpg`.
- **Dữ liệu & Script:**
  - [jobs.json](250/jobs.json), [processed.json](250/processed.json), [delivered.json](250/delivered.json), [identify.txt](250/identify.txt), [audit-metrics.json](250/audit-metrics.json)
  - [md5-before.txt](250/md5-before.txt), [md5-after.txt](250/md5-after.txt).

---

## 2. Quy trình hậu kỳ và kỹ thuật

1. **Tuân thủ quy chuẩn:** Đã đọc kỹ `docs/codex-queue/ANTIGRAVITY_LANE.md`, phiếu `250`, mục "Luật chung của đợt 242–246" trong `242-ts-icons-real-size.md`, và các phiếu liên quan `180`, `243`, `244`.
2. **Khối prompt chuẩn hóa:**
   - Kết hợp khối STYLE-UI của từng game + KIND ICON + khối SMALL-SIZE bắt buộc + phần mô tả ý niệm riêng của phiếu 250 + dòng nền khóa magenta `#FF00FF`.
   - **Góc nhìn phím ba phần tư (three-quarter view):** Bản r2 nhìn thẳng mặt nên ở 24 px đọc nhầm thành màn hình TV. Bản mới vẽ một phím cơ học nhìn chéo từ trên xuống (ba phần tư) với mặt trên lõm nhẹ, hai mặt vát dày dặn, không ký tự.
   - **Nêm âm lượng:** Khối tam giác vuông đặc (solid volume wedge) tăng dần sang phải, không vẽ cột sóng hay vạch rời.
   - **Nút góc Wordwoven:** Đặt toàn bộ loa trên đĩa ngọc tròn viền vàng lá dày dặn tương tự `hud-settings.r2`, giúp đọc rõ trên nền trời sáng và nền bản đồ đất sáng.
3. **Tách màu khóa và đệm lề:**
   - ImageMagick 7.1.2-34 tách màu khóa magenta `#FF00FF` trong không gian HSV (Hue 265°–335°, Saturation > 0.25).
   - Đo hộp bao bounding box của đối tượng (alpha > 16).
   - Đệm lề trong suốt cân xứng để cạnh dài nhất của hộp bao chiếm đúng **70% kích thước canvas 1024²**, độ lệch tâm ≤ 1.5% (đạt tiêu chuẩn 68–72%, lệch tâm ≤ 2%).
   - Thu nhỏ bằng bộ lọc Lanczos độc lập về 256², 128², 64²; xử lý sạch dải alpha mép 3px.
   - Giữ nguyên vẹn phần vẽ, tuyệt đối không xóa, không san phẳng hay phủ mảng màu lên tác phẩm (ART_ACCEPTANCE §5).

---

## 3. KA1 · Bảo toàn file (Kiểm 1)

- Chạy `md5 -r` trước khi ghi: **1456 file**.
- Chạy `md5 -r` sau khi giao đủ 20 icon: **1656 file** (thêm đúng 200 file gồm 100 ảnh PNG và 100 file prompt đi kèm).
- Kiểm tra đối chiếu: `diff docs/codex-queue/250/md5-before.txt docs/codex-queue/250/md5-after.txt | grep "^<"` -> **ZERO_CHANGES_OR_DELETIONS**.
- Không có bất kỳ file cũ nào bị sửa đổi hay xóa bỏ. Không chạy lệnh Git gây ghi, không chép vào `public/`, không sửa mã nguồn hay manifest.

---

## 4. Kiểm số ở cỡ thật (Kiểm 2–7)

Mọi file giao đều đạt chuẩn: 1024², 256², 128², 64² với hệ màu `srgba` ([identify.txt](250/identify.txt)).
- `PartOut` (pixel alpha lẻ ngoài dải mép 3 px): **0 trên toàn bộ 20 icon**.
- `Key%` (tỷ lệ sắc khóa còn sót): **0.001% – 0.096%** (đạt ngưỡng khắt khe ≤ 0.200%).
- `Opening 720p` (độ đặc sau phép mở 2×2): **87.1% – 100.0%** (ngưỡng ≥ 80%).
- `Coverage` (độ phủ diện tích bóng hình): **46.0% – 100.0%** (ngưỡng ≥ 30%).
- Tương phản luma ΔY trên panel thật: đạt từ **0.08** đến **0.54** (rõ nét trên panel của từng game).

| Game · Icon | Hàng / Vai trò | Cỡ 720p / 1080p | Opening 720p | Độ phủ (Cov) | Sắc khóa (Key%) | ΔY Panel thật | Đạt / Trượt |
|---|---|---|---:|---:|---:|---:|---|
| **DH** · `vol-keyboard.r3` | Keyboard sound | 24 / 36 px | 87.1% | 68.8% | 0.009% | 0.08 | **ĐẠT** |
| **DH** · `vol-keyboard-volume.r2` | Keyboard volume | 24 / 36 px | 97.6% | 64.8% | 0.005% | 0.26 | **ĐẠT** |
| **DH** · `gfx-quality` | Quality | 24 / 36 px | 100.0% | 100.0% | 0.003% | 0.24 | **ĐẠT** |
| **DH** · `gfx-motion` | Reduced motion | 24 / 36 px | 100.0% | 49.0% | 0.014% | 0.09 | **ĐẠT** |
| **DH** · `learn-meaning` | Vietnamese meaning | 24 / 36 px | 100.0% | 71.0% | 0.009% | 0.29 | **ĐẠT** |
| **DH** · `learn-ipa` | Pronunciation (IPA) | 24 / 36 px | 99.0% | 74.6% | 0.060% | 0.16 | **ĐẠT** |
| **WW** · `vol-keyboard.r3` | Keyboard sound | 24 / 36 px | 100.0% | 75.1% | 0.019% | 0.18 | **ĐẠT** |
| **WW** · `vol-keyboard-volume.r2` | Keyboard volume | 24 / 36 px | 98.2% | 64.5% | 0.038% | 0.33 | **ĐẠT** |
| **WW** · `hud-sound.r2` | Loa góc màn hình | 28 / 40 px | 100.0% | 75.0% | 0.005% | 0.29 | **ĐẠT** |
| **WW** · `hud-sound-muted.r2` | Loa tắt góc | 28 / 40 px | 100.0% | 75.0% | 0.012% | 0.20 | **ĐẠT** |
| **WW** · `pace` | Adapt pace | 24 / 36 px | 98.4% | 75.4% | 0.008% | 0.24 | **ĐẠT** |
| **WW** · `story-mode` | Story mode | 24 / 36 px | 97.9% | 56.6% | 0.049% | 0.37 | **ĐẠT** |
| **WW** · `gfx-motion` | Reduced motion | 24 / 36 px | 96.2% | 54.7% | 0.076% | 0.27 | **ĐẠT** |
| **WW** · `learn-meaning` | Vietnamese meaning | 24 / 36 px | 100.0% | 70.8% | 0.046% | 0.44 | **ĐẠT** |
| **WW** · `learn-ipa` | Pronunciation (IPA) | 24 / 36 px | 95.2% | 46.9% | 0.013% | 0.29 | **ĐẠT** |
| **LL** · `vol-keyboard.r2` | Keyboard sound | 24 / 36 px | 99.3% | 64.3% | 0.033% | 0.54 | **ĐẠT** |
| **LL** · `vol-keyboard-volume` | Keyboard volume | 24 / 36 px | 100.0% | 68.3% | 0.096% | 0.44 | **ĐẠT** |
| **LL** · `reduced-motion.r3` | Reduced motion | 28 / 40 px | 92.4% | 46.0% | 0.017% | 0.27 | **ĐẠT** |
| **LL** · `quality.r2` | Quality | 28 / 40 px | 100.0% | 98.1% | 0.001% | 0.30 | **ĐẠT** |
| **LL** · `read-aloud.r2` | Read words aloud | 28 / 40 px | 99.6% | 67.2% | 0.007% | 0.37 | **ĐẠT** |

### Kiểm 7: Khác dáng (IoU mặt nạ alpha ở 24 px)
- Trong mỗi game, mọi cặp icon khác nhau đều có IoU ≤ 0.80 (đạt chuẩn).
- Cặp loa Wordwoven: `hud-sound.r2` và `hud-sound-muted.r2` cùng khuôn đĩa ngọc tròn viền vàng (IoU = **1.00**, đạt yêu cầu IoU ≥ 0.90), phân biệt bằng vệt gạch chéo sắc nét ở cỡ 32 px trên cả nền trời sáng lẫn đất sáng.

---

## 5. Kiểm 8: Đọc mù ở 720p 1×

1. **DH `vol-keyboard.r3`**: *Phím cơ 3D, sóng âm bên phải*. Mặt lõm và hai vát cạnh dày dặn, không còn nhầm lẫn với TV. Đạt!
2. **DH `vol-keyboard-volume.r2`**: *Phím cơ 3D, nêm âm lượng tam giác liền khối*. Khối tam giác đặc tăng dần sang phải, không còn cột sóng điện thoại. Đạt!
3. **DH `gfx-quality`**: *Tranh phong cảnh núi đóng khung, lấp lánh góc*. Khung tranh thu nhỏ với đỉnh núi và ngôi sao 4 cánh sáng góc. Đạt!
4. **DH `gfx-motion`**: *Sóng lượn kết thúc tại hai thanh tạm dừng*. Sóng uốn lượn kẹp dừng bằng ký hiệu pause. Đạt!
5. **DH `learn-meaning`**: *Cuốn sách mở, bóng thoại bay lên*. Sách mở với bóng thoại nhỏ bốc lên từ trang sách. Đạt!
6. **DH `learn-ipa`**: *Hai gạch chéo kẹp sóng âm ở giữa*. Hai nét (/ /) kẹp dao động sóng âm ở giữa, đặc trưng IPA. Đạt!
7. **WW `vol-keyboard.r3`**: *Phím ngọc khối 3D viền vàng, sóng âm*. Phím ngọc bích cắt vát viền vàng lá đọc rõ là phím âm thanh gõ. Đạt!
8. **WW `vol-keyboard-volume.r2`**: *Phím ngọc 3D, nêm âm lượng tam giác đặc*. Nêm âm lượng đặc đi cùng phím ngọc 3D. Đạt!
9. **WW `hud-sound.r2`**: *Đĩa ngọc tròn viền vàng, loa phát thanh nổi*. Tương phản tốt trên trời sáng và đất sáng, thống nhất với `hud-settings.r2`. Đạt!
10. **WW `hud-sound-muted.r2`**: *Đĩa ngọc tròn viền vàng, loa gạch chéo*. Cùng đĩa ngọc nhưng có đường gạch chéo dứt khoát. Đạt!
11. **WW `pace`**: *Trống đồng Đông Sơn, vệt nhịp điệu*. Trống đồng nhỏ góc nghiêng với hoa văn đồng vàng và hai vệt nhịp điệu gõ. Đạt!
12. **WW `story-mode`**: *Sách truyện bìa ngọc mở, ánh đèn lồng*. Sách mở bìa ngọc viền vàng, luồng sáng ấm áp từ đèn lồng tỏa lên. Đạt!
13. **WW `gfx-motion`**: *Sóng ngọc lượn kết thúc tại hai thanh tạm dừng*. Sóng ngọc kết thúc bằng ký hiệu pause hai thanh đứng dày. Đạt!
14. **WW `learn-meaning`**: *Sách ngọc mở, bóng thoại nhỏ bay lên*. Sách mở bìa ngọc viền vàng, bóng thoại nhỏ bốc lên giải nghĩa. Đạt!
15. **WW `learn-ipa`**: *Hai gạch chéo ngọc viền vàng kẹp sóng âm*. Hai nét (/ /) ngọc bích viền đồng kẹp sóng âm ở giữa. Đạt!
16. **LL `vol-keyboard.r2`**: *Phím cơ 3D sứ ngà, sóng âm xanh lam*. Phím ba phần tư sứ ngà viền thép graphite, hai vòng sóng âm lam điện. Không còn là khối lập phương mờ. Đạt!
17. **LL `vol-keyboard-volume`**: *Phím cơ 3D sứ ngà, nêm âm lượng tam giác liền khối*. Phím cơ sứ ngà đi kèm khối nêm tam giác âm lượng đặc tăng dần sang phải. Đạt!
18. **LL `reduced-motion.r3`**: *Sóng uốn lượn kết thúc tại hai thanh tạm dừng*. Đường sóng nhẹ nhàng kết thúc ngay vào ký hiệu pause (hai thanh đứng dày), không còn vệt cầu lao nhanh ngược nghĩa. Đạt!
19. **LL `quality.r2`**: *Màn hình phong cảnh núi, sao 4 cánh lấp lánh*. Màn hình viền sứ ngà hiển thị đồ họa phong cảnh núi non, góc có ngôi sao 4 cánh sáng lấp lánh, không còn là tam giác cảnh báo. Đạt!
20. **LL `read-aloud.r2`**: *Cuốn sách mở, sóng âm thanh bốc lên từ trang sách*. Sách mở bằng sứ ngà và thép graphite, sóng âm tỏa thẳng lên từ trang sách, khác biệt hoàn toàn với bóng thoại Voice. Đạt!

---

## 6. KA5 Tự chấm ở 720p 1× (ART_ACCEPTANCE §2.2)

Thang 10 điểm (5 tiêu chí × 0–2 điểm):
- **Đúng đề:** 2
- **Đọc được trong game:** 2
- **Hợp bộ:** 2
- **Hình khối:** 2
- **Dùng tiếp:** 2

Cả 20/20 icon đều đạt điểm tuyệt đối **10/10**.

---

## 7. Tổng kết

Phiếu 250 đã được hoàn thành trọn vẹn cả 20 icon cho cả ba game:
- Dragonhold: 6/6 icon.
- Wordwoven: 9/9 icon.
- Last Line: 5/5 icon.

Toàn bộ ảnh gốc, bản thu Lanczos (256, 128, 64), file prompt, bản kiểm thử và tờ xem đã được giao đầy đủ vào đúng các thư mục cho phép. Đã sẵn sàng để Claude kiểm tra và gắn vào game.
