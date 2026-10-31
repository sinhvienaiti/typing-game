# Phiếu 249 · Last Line · Tranh súng, ô băng đạn và bốn icon menu đọc sai ở cỡ thật

**Nguồn:**
- **Luật chung của đợt: mục "Luật chung của đợt 242–246" trong `docs/codex-queue/242-ts-icons-real-size.md`** (khối SMALL-SIZE, tên `.r2`, Kiểm 1–10, giới hạn ảnh, cấm, nhận). Phiếu này chỉ ghi chỗ khác.
- Lượt chấm thứ ba (31/10, khoảng 18:40, workflow `ts-ui-pass-3`): hai giám khảo độc lập chấm UI Last Line **7,4 và 7,3** trong game, ở 1280×720 và 1920×1080. Các ảnh dưới đây vẫn đọc sai ở cỡ vẽ thật.
- Phiếu gốc: tranh súng ở `ui/icons/gun-*.png` (bản `.v2` và `.norm` là bản đang dùng tuỳ súng; xem `scripts/ui-art/selection.json` để biết bản nào đang gắn), ô băng đạn ở `ui/parts/mag-full.png`, `mag-empty.png` (153, 240), icon menu ở `ui/icons/` (151, 239).

**Báo cáo:** `docs/codex-queue/249-report.md` (tiếng Việt) và thư mục `docs/codex-queue/249/`. Model `gpt-6.1-sol`, mức `high`.

## Việc A · Ba tranh súng (vẽ lại, tên `.r2`)

Tranh súng không phải icon nhỏ: giữ chất liệu và độ chi tiết của bộ súng đã nhận (`gun-xung` đọc tốt, dùng làm tham chiếu chính), nhưng **dáng ngoài phải đọc ra súng** ở 44 px (thẻ súng trên đầu bến), 64 px (Armory) và 96 px (Loadout), ở 720p. Nhìn ngang, nòng chĩa sang phải, có báng hoặc tay cầm rõ.

| Tên | Đang đọc thành | Ý mới (EN) |
|---|---|---|
| `gun-tia` (Heat Beam) | cái loa, cọc giao thông | a heavy beam cannon seen from the side: a long straight barrel ending in a glowing orange lens, three thick cooling rings along the barrel, a chunky body with a pistol grip and a short stock; reads as a gun, not a cone |
| `gun-ray` (Rail Gun) | lưỡi kiếm, ngọn giáo | a rail gun seen from the side: two long parallel rails with cyan charge sparks between them, mounted on a thick boxy body with a grip and a stock; clearly a firearm |
| `gun-phao-sao` (Star Mortar) | đèn bàn, cần cẩu | a squat mortar seen from the side: a short fat tube angled up at 45 degrees on a heavy base plate with two braces, a glowing star-shaped shell at the muzzle |

- Kiểm 3 dùng ba cỡ 44 / 64 / 96 (720p) và 66 / 96 / 144 (1080p), trên `ui/frames-epic/bay-card.png` (thẻ bến) và `button.png`.
- Ô so sánh: ba súng mới cạnh `gun-xung` và `gun-tan` đã nhận, cùng cỡ 44 px; năm súng phải khác dáng từng đôi (IoU ≤ 0,80 ở 44 px).

## Việc B · Ô băng đạn (vẽ lại, tên `.r2`)

Hai ô đứng cạnh nhau trên đầu bến đọc thành ký hiệu tạm dừng ‖. Đổi sang **viên đạn nằm ngang**:

| Tên | Ý mới (EN) |
|---|---|
| `mag-full` | one brass rifle round lying horizontally, a bright cyan-white glowing tip pointing right, thick dark outline |
| `mag-empty` | the same round's empty slot: a dark recessed horizontal capsule outline with a faint cyan edge, same size and pose as `mag-full` |

- Cỡ trong game: cao 10 px, dài khoảng 24 px ở 720p (15 × 36 ở 1080p). Khổ nguồn 1024 × 512, vật nằm giữa.
- Cặp đầy/rỗng cùng dáng (IoU ≥ 0,90) và khác nhau ngay ở 720p trên nền tối. Ô so sánh: ba ô đầy và hai ô rỗng xếp một hàng như đầu bến.

## Việc C · Bốn icon menu (vẽ lại, tên `.r2`)

| Tên | Nhãn | Cỡ 720p / 1080p | Đang đọc thành | Ý mới (EN) | So với |
|---|---|---|---|---|---|
| `menu-profile` | Profile | 28 / 40 | bàn tay in trên tấm biển | a pilot helmet seen from the front with a glowing cyan visor, chunky and round | `menu-armory`, `station-crest` |
| `menu-play` | Play / Resume | 28 / 40 | chevron mảnh (next) | a bold solid play triangle on a round metal button | `next-stage.r2`, `streak` |
| `menu-mode` | Mode | 28 / 40 | mũ, vương miện có cung | a round selector dial knob with three thick notches and a bright pointer | `pace-director.r3` nếu đã có, `clock.r2` |
| `new-badge` | (cạnh từ mới, không nhãn) | 20 / 28 | mặt trời, bánh răng | a small ribbon tag with a notched tail and a bright star on it, no text | `star-lit` |

## Chỉ được ghi

- `games/typing-survival/art-src/ui/icons/{gun-tia,gun-ray,gun-phao-sao,menu-profile,menu-play,menu-mode,new-badge}.r2-try*.*`, `.r2.*` (mới).
- `games/typing-survival/art-src/ui/parts/{mag-full,mag-empty}.r2-try*.*`, `.r2.*` (mới).
- `games/typing-survival/art-src/_review/249*`.
- `docs/codex-queue/249-report.md`, `docs/codex-queue/249/`.
