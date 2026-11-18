# Phiếu 243 · Last Line · Icon bảng Settings, Sound và Options: vẽ lại 6, làm mới 4

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`** (khối SMALL-SIZE, tên `.r2`, Kiểm 1–10, giới hạn ảnh, cấm, nhận). Phiếu này chỉ ghi chỗ khác.
- Phiếu gốc: `152-ts-ui-settings.md` (icon Options) và `180-quick-settings-icons.md` (icon bảng nhanh, bản chọn ở `ui/quick-settings/selected/`).
- Lượt chấm thứ hai (31/10, khoảng 16:00): bánh răng góc màn hình đọc thành bông hoa tám cánh; hàng Ship, Letter style, Effect strength, Word size không có icon; vài icon hàng đọc sai ở 24–28 px.

**Báo cáo:** `docs/codex-queue/243-report.md` (tiếng Việt) và thư mục `docs/codex-queue/243/`. Model `gpt-6.1-sol`, mức `high`.

## Việc

**Vẽ lại (tên `.r2`):**

| Tên | Thư mục | Nhãn | Cỡ 720p / 1080p | Đang đọc thành | Ý mới (EN) | So với |
|---|---|---|---|---|---|---|
| `menu-settings` | `ui/icons/` | Settings | 28 / 40 | bông tuyết, hoa nổ | a chunky cog with eight square teeth joined to a thick rim and a clear round hub hole; no wrench, no spokes, no separate petals | `quality`, `menu-mode` |
| `hud-settings` | `ui/quick-settings/selected/` (lượt sinh ở `ui/quick-settings/`) | (nút góc, không nhãn) | 32 / 44 | bông hoa tám cánh, mặt trời | the same cog as `menu-settings.r2`, sitting on a small round steel plate so it reads as a button | `hud-sound`, `hud-sound-muted` |
| `pace-director` | `ui/icons/` | Adapt pace to your typing | 28 / 40 | tai nghe, vòng nguồn | a half-dial speedometer on a flat base, one thick needle, a small two-way loop arrow beneath the dial | `clock.r2` (phiếu 242, nếu đã có), `stat-wpm.v2` |
| `shake` | `ui/icons/` | Screen shake | 28 / 40 | viên ngọc giữa hai ngoặc | a small screen rectangle drawn twice, the ghost copy offset to one side, with bold zigzag motion ticks on both sides | `reduced-motion`, `quality` |
| `vol-effects` | `ui/quick-settings/selected/` | Effects | 24 / 36 | phi tiêu ninja | a round impact burst with a bright core and short thick rays, with two sound arcs on its right; no speaker | `vol-master`, `vol-music`, `../../icons/surge` |
| `vol-interface` | `ui/quick-settings/selected/` | Interface | 24 / 36 | phi tiêu, máy bay giấy | a bold upright pointer arrow pressing a rectangular button, two small click ticks; the button clearly visible | `vol-keyboard`, `vol-voice` |

- Hai bánh răng phải cùng một dáng (IoU ≥ 0,90 ở 32 px, không tính tấm tròn của `hud-settings`). Bản chọn của `hud-settings` cũng có bản `.r2` ở `ui/quick-settings/selected/`; không ghi đè bản cũ.
- `hud-sound` và `hud-sound-muted` đã đọc đúng, không động tới; chỉ dùng để so.

**Làm mới (chưa có file):**

| Tên | Thư mục | Nhãn | Cỡ 720p / 1080p | Ý (EN) | So với |
|---|---|---|---|---|---|
| `ship` | `ui/icons/` | Ship | 28 / 40 | a compact top-down starfighter silhouette with swept wings and one cyan engine glow, nose pointing up | `menu-play`, `armour` |
| `letter-style` | `ui/icons/` | Letter style | 28 / 40 | a single bold capital letter A shape with a bright spark burst at its top-right corner | `word-size`, `effect-strength` |
| `effect-strength` | `ui/icons/` | Effect strength | 28 / 40 | three rising solid bars with a small burst above the tallest bar | `vol-master` (quick-settings), `stat-wpm.v2` |
| `word-size` | `ui/icons/` | Word size | 28 / 40 | a small capital letter A and a large capital letter A side by side on one baseline | `letter-style` |

- **Ngoại lệ có ghi:** `letter-style` và `word-size` được vẽ chữ A in hoa làm hình (không có từ, không có chữ khác). Chữ A phải sạch: hai chân thẳng, gạch ngang rõ, không méo. Chữ A hỏng là trượt, không sửa bằng tay.

**Kiểm riêng:** bốn icon mới và sáu icon vẽ lại khác dáng từng đôi (IoU ≤ 0,80 ở 32 px), trừ cặp bánh răng. Ô so sánh `letter-style` cạnh `word-size` và `effect-strength` ở 28 px.

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{menu-settings,pace-director,shake}.r2-try*.*`, `.r2.*`.
- `games/typing-survival/art-src/ui/icons/{ship,letter-style,effect-strength,word-size}.*` (mới).
- `games/typing-survival/art-src/ui/quick-settings/{hud-settings,vol-effects,vol-interface}.r2-try*.*` và `ui/quick-settings/selected/{hud-settings,vol-effects,vol-interface}.r2.*`.
- `games/typing-survival/art-src/_review/243*`.
- `docs/codex-queue/243-report.md`, `docs/codex-queue/243/`.
