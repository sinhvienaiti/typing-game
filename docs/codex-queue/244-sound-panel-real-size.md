# Phiếu 244 · Ba game · Bảng Sound: icon hàng của Dragonhold và Wordwoven, phần đầy của thanh trượt

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`.** Phiếu này chỉ ghi chỗ khác.
- Phiếu gốc: `180-quick-settings-icons.md` (icon `vol-*`, `hud-*`, bản chọn ở `ui/quick-settings/selected/`) và `225-settings-slider-art.md` (rãnh và núm; rãnh Dragonhold làm lại ở 241).
- Lượt chấm thứ hai (31/10, khoảng 16:00), giám khảo bảng Settings/Sound của Dragonhold và Wordwoven chấm **6,5**:
  - năm icon hàng đọc sai ở khoảng 24 px (ô 24 px, mực khoảng 18 px ở 1280×720);
  - hàng Keyboard volume chưa có icon;
  - rãnh thanh trượt không có phần đầy: 0 % và 100 % chỉ khác ở vị trí núm. Rãnh ngọc sáng của Wordwoven trông như đầy cả khi ở 0.
- Giám khảo Last Line cũng ghi: rãnh hiện cùng một vạch lam ở 50 % và 100 %.

**Báo cáo:** `docs/codex-queue/244-report.md` (tiếng Việt) và thư mục `docs/codex-queue/244/`. Model `gpt-6.1-sol`, mức `high`.

## Việc A · Icon hàng (tên `.r2`, hoặc tên mới)

- Khối STYLE-UI và tham chiếu bộ theo phiếu 180 của từng game. Dragonhold: sắt rèn và vàng ấm, lõi than hồng. Wordwoven: đồng, vàng lá và ngọc.
- Tham chiếu bộ đính kèm: `ui/quick-settings/selected/vol-master.png` và `selected/hud-sound.png` của cùng game (hai icon đã đọc đúng).
- Lượt sinh ở `ui/quick-settings/`, bản chọn ở `ui/quick-settings/selected/`.
- Mảnh UI thật cho Kiểm 3: Dragonhold `ui/frames/panel-large.png`; Wordwoven `ui/frames-epic/panel-large.v2.png`.

| Game · tên | Nhãn | Cỡ 720p / 1080p | Đang đọc thành | Ý mới (EN) |
|---|---|---|---|---|
| Dragonhold · `vol-keyboard` | Keyboard sound | 24 / 36 | hộp vàng, rương, miếng phô mai | one front-facing keycap (a square with a bevelled top and a dark letter-free face) with two curved sound arcs to its right, ember gold with a dark outline |
| Dragonhold · `vol-voice` | Voice | 24 / 36 | viên thuốc, cái nhẫn, đôi môi | a speech bubble with a clear pointed tail and two sound arcs, thick gold outline, dark filled centre |
| Dragonhold · `vol-interface` | Interface | 24 / 36 | cuốc chim, búa | a bold upright mouse-pointer arrow pressing a small round button, with a tiny click star, one gold silhouette |
| Dragonhold · `vol-keyboard-volume` (mới) | Keyboard volume | 24 / 36 | (ô trống) | a keycap on the left with three rising volume bars on the right, ember gold |
| Wordwoven · `vol-keyboard` | Keyboard sound | 24 / 36 | thỏi vàng, hộp, phô mai | one front-facing jade keycap in a gold rim, letter-free face, with two sound arcs to its right |
| Wordwoven · `vol-interface` | Interface | 24 / 36 | tù và, kèn, dụng cụ cầm tay | an upright pointer arrow tapping a round jade button, with a small click spark, gold silhouette with a dark outline |
| Wordwoven · `vol-keyboard-volume` (mới) | Keyboard volume | 24 / 36 | (ô trống) | a jade keycap with three rising gold volume bars |
| Wordwoven · `hud-settings` | (nút góc, không nhãn) | 28 / 40 | hoa hướng dương, mặt trời (răng là cánh rời quanh vòng mảnh) | a gear with solid teeth joined to a thick gold body and a dark hub, set on a round jade plate |

**Kiểm riêng:**
- Ở 24 px, `vol-keyboard` và `vol-keyboard-volume` của cùng game phải khác nhau ngay (IoU ≤ 0,80), và cùng khác `vol-master`.
- Ô so sánh sáu icon hàng của bảng Sound của mỗi game (master, music, effects, keyboard, keyboard volume, voice, interface) xếp dọc như bảng thật, ở 720p 1×.

## Việc B · Phần đầy của thanh trượt (ba game)

Kit sẽ vẽ phần **đầy** (bên trái núm) và phần **rỗng** (bên phải núm) bằng hai ảnh cùng khuôn. Hai ảnh phải chồng khít nhau.

| Game · tên | Vai | Ý (EN) |
|---|---|---|
| Dragonhold · `slider-fill` | phần đầy; rãnh đã nhận (241) là phần rỗng | the same groove, its channel filled with a molten ember-gold core that glows warm orange, the gold rims and end caps unchanged |
| Wordwoven · `slider-fill` | phần đầy | the same groove, its channel filled with bright polished jade lit from within, gold-leaf rims unchanged |
| Wordwoven · `slider-empty` | phần rỗng (thay rãnh hiện tại vì nó sáng như đầy) | the same groove, its channel dark unpolished stone with a faint bronze tint, clearly darker than the jade fill, rims and caps unchanged |
| Last Line · `slider-fill` | phần đầy; rãnh đã nhận là phần rỗng | the same groove, the smoked glass filled with bright electric-cyan energy, white-gold rims and caps unchanged |

- **Cách sinh:** dùng chế độ sửa ảnh của công cụ, đính kèm **rãnh đã nhận** của game đó (`ui/quick-settings/sliders/slider-track.png`, bản trước khi thu nếu còn) làm ảnh đích, và chỉ xin đổi chất liệu lòng rãnh. Khổ, hậu kỳ và thu nhỏ theo 225 (bản 1024×64 và 512×32, cùng cách đệm trong suốt như 241, không co không đều).
- Lượt sinh: `sliders/<tên>.tryN.png` và `.tryN.prompt.txt`. Bản chọn: `sliders/<tên>.png`, `.512.png`, `.prompt.txt`.

**Kiểm riêng (thay Kiểm 3–8 của 242 cho phần này):**
1. **Chồng khít:** ở 1024×64, IoU mặt nạ alpha > 16 giữa ảnh mới và rãnh đã nhận ≥ 0,97; hai đầu lệch nhau ≤ 2 px.
2. **Khác mức:** luma trung bình của lòng rãnh (bỏ viền) ở phần đầy cao hơn phần rỗng ít nhất **0,15**. Wordwoven: so `slider-fill` với `slider-empty`.
3. **Kéo giãn:** kéo ngang 90–435 px như 241 mà không méo đầu.
4. **Tờ xem** `art-src/_review/244-slider-<game>.jpg`: ghép phần đầy bên trái, phần rỗng bên phải, núm đã nhận ở mép, tại 0 %, 25 %, 50 %, 100 %, ở 720p và 1080p 1×, trên mảnh bảng thật của game. Thêm bản phóng ×4 của hàng 720p.
5. KA5 tự chấm ở tờ 720p 1×.

## Chỉ được ghi

- `games/{dragon-hold,typing-defense}/art-src/ui/quick-settings/<tên>.r2-try*.*` và `selected/<tên>.r2.*` cho các tên vẽ lại ở bảng Việc A; `<tên>.try*.*` và `selected/<tên>.*` cho `vol-keyboard-volume` (mới).
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/ui/quick-settings/sliders/{slider-fill,slider-empty}.*` (mới, đúng tên theo bảng Việc B).
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/_review/244*`.
- `docs/codex-queue/244-report.md`, `docs/codex-queue/244/`.

Không động tới `slider-track.*`, `slider-thumb.*` đã nhận.
