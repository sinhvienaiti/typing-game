# Phiếu 157 · Last Line · Vẽ lại icon súng và chân dung quái theo hướng B (11 ảnh)

**Nguồn:** chủ dự án chọn hướng B · Lightbearer ngày 29/10/2026 sáng. Hướng B bỏ tàu: súng thành **súng canh bay** cạnh nhân vật, quái thành **Bầy Hố Đen kính đen nứt cam** (`docs/games/ART_DIRECTION_2026-10-28.md` §4.3). Năm icon súng của phiếu 108 và sáu chân dung quái của phiếu 089 vẽ theo kiểu cũ (súng gắn tàu, quái thân tối gân sáng), nên lệch hướng mới. Dàn ý gốc: `UIC-LL-R` ở `docs/games/map1/UI_IMAGERY_CODEX.md` §5.

**Báo cáo:** `docs/codex-queue/157-report.md`.

**Chạy khi:** sau phiếu 156 (ảnh nguồn súng canh), để icon súng khớp dáng súng canh đã chọn.

## Luật chung

Theo nguyên văn mục "Luật chung (phiếu ảnh)" và "Chung cho Last Line" của `docs/codex-queue/149-ts-ui-hud.md`, đọc trước khi làm, với ba điểm khác:
- số phiếu là 157 (thư mục `_review/157/`, tờ `_review/157-sheet.jpg`);
- **không ghi đè file cũ:** bản mới ghi cạnh bản cũ thành `<tên>.v2.png` (và `.v2.256.png`, `.v2.128.png`, `.v2.64.png`, `.v2.tryN.*`). Claude đổi sang khi gắn;
- mỗi ảnh đính kèm ảnh cũ cùng tên làm tham chiếu vật, với dòng `Keep the same object identity as the attached image. Repaint it in the new style as described.`

**Chỉ được ghi:** `games/typing-survival/art-src/ui/icons/gun-*.v2*`, `games/typing-survival/art-src/ui/foes/*.v2*`, `games/typing-survival/art-src/_review/157*`, báo cáo.

## Ảnh

| Tên | Tham chiếu thêm | Nội dung (EN, cho prompt) | Cỡ trong game 720p / 1080p |
|---|---|---|---|
| `icons/gun-xung.v2` | `models-src/sentinel-pulse.png` (156) | the Pulse Gun sentinel: compact floating gun with a short twin barrel and a cyan muzzle ring | 28 / 42 |
| `icons/gun-tia.v2` | `models-src/sentinel-heat.png` | the Heat Beam sentinel: long focusing lens barrel, glowing orange-gold core | như trên |
| `icons/gun-tan.v2` | `models-src/sentinel-scatter.png` | the Scatter Gun sentinel: five short barrels in a fan | như trên |
| `icons/gun-ray.v2` | `models-src/sentinel-rail.png` | the Rail Gun sentinel: two long rails with cyan coils | như trên |
| `icons/gun-phao-sao.v2` | `models-src/sentinel-mortar.png` | the Star Mortar sentinel: short wide upward barrel with star-shaped vents | như trên |
| `foes/swarm.v2` | `concepts/b-lightbearer-fight.png` | a small Hollow Swarm crawler of black glass with glowing orange cracks, bust portrait | 34 / 51 |
| `foes/scout.v2` | như trên | a fast thin Hollow scout of black glass, long legs, cyan-white eye glints, orange cracks | như trên |
| `foes/brute.v2` | như trên | a heavy Hollow brute of black glass, huge shoulders, amber cracks | như trên |
| `foes/pack-leader.v2` | như trên | a Hollow pack leader of black glass with a crown of spines and bright gold cracks | như trên |
| `foes/shield-guard.v2` | như trên | a Hollow shield guard of black glass holding a cyan energy shield | như trên |
| `foes/splitter.v2` | như trên | a Hollow splitter of black glass already cracking into three smaller shapes, orange light inside | như trên |

## Kiểm riêng

- Tờ so cũ và mới cùng cỡ 64 px, hai hàng (theo `UI_IMAGERY_CODEX.md` §5).
- Năm icon súng đọc ra đúng súng ở 28 px, và khớp dáng súng canh của 156 (đặt cạnh nhau trên tờ).
- Sáu chân dung quái khác dáng nhau từng đôi ở 34 px (IoU ≤ 0,80); Pack Leader và Shield Guard nhận ra ngay nhờ vương miện gai và khiên lam.

**Xong khi:** như luật chung của 149, và đủ 11 ảnh cùng ba bản thu.
