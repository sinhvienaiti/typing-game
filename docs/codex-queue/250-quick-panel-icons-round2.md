# Phiếu 250 · Ba game · Icon bảng nhanh vòng 2: vẽ lại icon còn đọc sai, làm icon cho các hàng còn trống

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`** (khối SMALL-SIZE, tên `.rN`, Kiểm 1–10, giới hạn ảnh, cấm, nhận). Phiếu này chỉ ghi chỗ khác.
- Phiếu gốc: `180-quick-settings-icons.md` (khối STYLE-UI, nền và bộ icon của từng game), `243`, `244`.
- Lượt chấm bảng nhanh 31/10 khoảng 22:10 (workflow `panels-art-wiring`): Dragonhold 7,1, Wordwoven 6,8, Last Line Settings 7 và Sound 7,3. Hai giám khảo đọc icon ở đúng cỡ vẽ (24 px ở 720p, 36 px ở 1080p) và ghi các icon dưới đây là đọc sai hoặc ô còn trống.

**Báo cáo:** `docs/codex-queue/250-report.md` (tiếng Việt) và thư mục `docs/codex-queue/250/`. Model `gpt-6.1-sol`, mức `high`.

## Ý chung cho bàn phím

`vol-keyboard` bản r2 nhìn thẳng mặt nên ở 24 px đọc thành **màn hình TV có sóng âm**. Bản mới vẽ **một phím cơ học nhìn chéo từ trên xuống (ba phần tư)**: thấy rõ mặt trên lõm nhẹ và hai mặt bên vát, thân phím dày. Không vẽ chữ trên phím.

| Vai | Ý (EN) |
|---|---|
| Keyboard sound | one chunky mechanical keycap seen from three-quarter view above, its slightly dished top face and two bevelled sides clearly visible, with two bold sound arcs to its right |
| Keyboard volume | the same three-quarter keycap with a solid volume wedge (a right triangle growing from left to right) beside it; no bar graph, no signal bars |

Hai icon phải khác nhau ngay ở 24 px (IoU ≤ 0,80), và cùng khác `vol-master`.

## Việc theo từng game

Lượt sinh ở `ui/quick-settings/`, bản chọn ở `ui/quick-settings/selected/`, tên `<tên>.r3` nếu vẽ lại bản r2, `<tên>.r2` nếu vẽ lại bản gốc, tên mới nếu chưa có. Khối STYLE-UI và tham chiếu bộ theo phiếu 180 của đúng game.

### Dragonhold (sắt rèn, vàng ấm, than hồng)

| Tên | Hàng | Đang đọc thành | Ý (EN) |
|---|---|---|---|
| `vol-keyboard.r3` | Keyboard sound | TV hay màn hình có sóng âm | xem "Ý chung" |
| `vol-keyboard-volume.r2` | Keyboard volume | cột sóng điện thoại | xem "Ý chung" |
| `gfx-quality` (mới) | Quality | ô trống | a small framed painting of a mountain landscape with a bright four-point sparkle at its corner |
| `gfx-motion` (mới) | Reduced motion | ô trống | a single gentle wave line ending in a bold pause sign (two thick upright bars) |
| `learn-meaning` (mới) | Vietnamese meaning | ô trống | an open book with a small speech bubble rising from its pages |
| `learn-ipa` (mới) | Pronunciation (IPA) | ô trống | two bold slanted slashes enclosing a short sound wave |

### Wordwoven (đồng, vàng lá, ngọc)

| Tên | Hàng | Đang đọc thành | Ý (EN) |
|---|---|---|---|
| `vol-keyboard.r3` | Keyboard sound | TV màn xanh có sóng âm | xem "Ý chung", phím ngọc viền vàng |
| `vol-keyboard-volume.r2` | Keyboard volume | cột sóng cạnh khối xanh | xem "Ý chung" |
| `hud-sound.r2`, `hud-sound-muted.r2` | nút loa góc màn hình | vệt vàng nhạt trên trời sáng và bản đồ màu đất | the same speaker (muted: with a clean slash) set on a round jade plate with a gold rim, like the accepted `hud-settings.r2`, so it reads on light backgrounds |
| `pace` (mới) | Pace adapts to your typing | ô trống | a small bronze drum with two motion ticks above it, beating in rhythm |
| `story-mode` (mới) | Story mode | ô trống | an open storybook with a small lantern glow rising from its pages |
| `gfx-motion` (mới) | Reduced motion | ô trống | như Dragonhold, chất liệu Wordwoven |
| `learn-meaning` (mới) | Vietnamese meaning | ô trống | như Dragonhold, chất liệu Wordwoven |
| `learn-ipa` (mới) | Pronunciation (IPA) | ô trống | như Dragonhold, chất liệu Wordwoven |

- `hud-sound.r2` và `hud-sound-muted.r2`: cùng tư thế (IoU ≥ 0,90), khác nhau rõ ở 32 px. Kiểm 3 thêm ô trên trời sáng của màn tựa và trên nền đất sáng của bản đồ.

### Last Line (sứ ngà, thép, lõi lam)

Thư mục `ui/quick-settings/` cho icon `vol-*`, `ui/icons/` cho icon hàng Settings.

| Tên | Hàng | Đang đọc thành | Ý (EN) |
|---|---|---|---|
| `vol-keyboard.r2` | Keyboard sound | hộp trắng, khối lập phương (28 px) | xem "Ý chung" |
| `vol-keyboard-volume` (mới) | Keyboard volume | đang mượn icon bàn phím | xem "Ý chung" |
| `reduced-motion.r3` | Reduced motion | quả cầu lao nhanh có vệt tốc độ (ngược nghĩa) | a single gentle wave line ending in a bold pause sign (two thick upright bars) |
| `quality.r2` | Quality | kim tự tháp pha lê, tam giác cảnh báo | a small screen showing a mountain landscape with a bright four-point sparkle at its corner |
| `read-aloud.r2` | Read words aloud | đôi môi có sóng, lẫn với Voice | an open book with bold sound arcs rising from its pages (reading aloud), clearly different from the Voice speech bubble |

## Kiểm riêng

- Ô so sánh của mỗi game: toàn bộ icon hàng của bảng Settings và bảng Sound xếp dọc như bảng thật, ở 720p 1×, trên mảnh `panel-large` thật của game.
- Ô 32 px của các nút góc trên nền sáng (Wordwoven).
- Ở 24 px, mọi cặp icon trong cùng một bảng khác dáng (IoU ≤ 0,80), trừ cặp loa/loa tắt.

## Chỉ được ghi

- `games/{dragon-hold,typing-defense,typing-survival}/art-src/ui/quick-settings/` và `selected/`, đúng các tên ở bảng trên (mới hoặc hậu tố mới; không ghi đè).
- `games/typing-survival/art-src/ui/icons/{reduced-motion.r3,quality.r2,read-aloud.r2}*`.
- `games/{dragon-hold,typing-defense,typing-survival}/art-src/_review/250*`.
- `docs/codex-queue/250-report.md`, `docs/codex-queue/250/`.
