# Phiếu 311 · Tu Tiên · Ảnh 2D: vòng phù văn dưới chân và hiệu ứng bám trên quái cho 14 hệ, 28 lần gọi `image_gen`

Anh (06/11 ~12:10): "phải tập trung việc tạo ảnh, tạo video, âm thanh... firefly chỉ còn hạn 2 tiếng, phải tăng tốc độ tạo media lên". Trước đó anh nhấn mạnh 5 pha của chiêu (tung, bay, vào quái ra sao, xung quanh chiêu). Phiếu này vẽ hai phần đang thiếu cho cả 14 hệ, song song với mẫu ChatGPT và Gemini (`docs/work/tasks/images-0611.md`); anh chọn bộ đẹp hơn. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 28 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.** Báo cáo: `docs/codex-queue/311-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu bằng `view_image`: lưỡi liềm của hệ anh đã duyệt. Chỉ lấy chất liệu, ánh sáng, độ phát sáng, độ hoàn thiện; không lấy dáng lưỡi liềm.
2. Gọi `image_gen` tạo mới, khổ ngang, nền đen (không bật nền trong suốt), kèm ảnh đó. Prompt = câu của cột "Loại" (thay `<MATTER>` bằng cột chất liệu) + đuôi chung, dán nguyên văn.
3. Chép bằng `cp -n` thành `D/<tên ra>.png`; ghi `D/<tên ra>.prompt.txt` (công cụ, ảnh tham chiếu, prompt, khổ thật).

**Seal (nguyên văn):**
```text
A circular cultivation formation seal glowing on the ground beneath a cultivator (the cultivator is not shown), seen at the play camera angle: concentric rings of fine runes and trigram marks made of <MATTER>, a bright thin inner ring, small particles lifting from the rings, the centre left empty.
```
**Affliction (nguyên văn):**
```text
An affliction that clings to a struck beast, shown alone without the beast: a ring-shaped crown of <MATTER> wrapping an empty upright oval where the body would be, small pieces and particles of it drifting off.
```
**Đuôi chung (nguyên văn):**
```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its crescent shape. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, fine luminous detail, glints and star twinkles, soft halos; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Centred with a wide empty border, solid pure black background, no text, no letters, no watermark.
```

| Tên ra | Ảnh tham chiếu | Loại | `<MATTER>` |
|---|---|---|---|
| `metal-caster-seal.v1-try1` | `D/metal-crescent-sym.v1-try1.png` | Seal | razor-sharp white-silver metal light with pale jade edges and star glints |
| `metal-hit-affliction.v1-try1` | `D/metal-crescent-sym.v1-try1.png` | Affliction | razor-sharp white-silver metal light with pale jade edges and star glints |
| `fire-caster-seal.v1-try1` | `D/fire-crescent-sym.v1-try1.png` | Seal | dense white-gold, amber and vermilion flame with embers and sparks |
| `fire-hit-affliction.v1-try1` | `D/fire-crescent-sym.v1-try1.png` | Affliction | dense white-gold, amber and vermilion flame with embers and sparks |
| `water-caster-seal.v1-try1` | `D/water-crescent-sym.v1-try1.png` | Seal | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |
| `water-hit-affliction.v1-try1` | `D/water-crescent-sym.v1-try1.png` | Affliction | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |
| `thunder-caster-seal.v1-try1` | `D/thunder-crescent-sym.v1-try1.png` | Seal | violet-white lightning with a blinding white core line and crackling branching arcs |
| `thunder-hit-affliction.v1-try1` | `D/thunder-crescent-sym.v1-try1.png` | Affliction | violet-white lightning with a blinding white core line and crackling branching arcs |
| `wind-caster-seal.v1-try1` | `D/wind-crescent-sym.v1-try1.png` | Seal | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| `wind-hit-affliction.v1-try1` | `D/wind-crescent-sym.v1-try1.png` | Affliction | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| `ice-caster-seal.v1-try1` | `D/ice-crescent-sym.v1-try1.png` | Seal | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| `ice-hit-affliction.v1-try1` | `D/ice-crescent-sym.v1-try1.png` | Affliction | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| `earth-caster-seal.v1-try1` | `D/earth-crescent-sym.v1-try1.png` | Seal | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| `earth-hit-affliction.v1-try1` | `D/earth-crescent-sym.v1-try1.png` | Affliction | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| `wood-caster-seal.v1-try1` | `D/wood-crescent-sym.v1-try1.png` | Seal | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| `wood-hit-affliction.v1-try1` | `D/wood-crescent-sym.v1-try1.png` | Affliction | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| `dark-caster-seal.v1-try1` | `D/dark-crescent-sym.v1-try1.png` | Seal | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| `dark-hit-affliction.v1-try1` | `D/dark-crescent-sym.v1-try1.png` | Affliction | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| `light-caster-seal.v1-try1` | `D/light-crescent-sym.v1-try1.png` | Seal | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| `light-hit-affliction.v1-try1` | `D/light-crescent-sym.v1-try1.png` | Affliction | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| `poison-caster-seal.v1-try1` | `D/poison-crescent-sym.v1-try1.png` | Seal | luminous toxic green and violet miasma with acid droplets and spores |
| `poison-hit-affliction.v1-try1` | `D/poison-crescent-sym.v1-try1.png` | Affliction | luminous toxic green and violet miasma with acid droplets and spores |
| `blood-caster-seal.v1-try1` | `D/blood-crescent-sym.v1-try1.png` | Seal | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| `blood-hit-affliction.v1-try1` | `D/blood-crescent-sym.v1-try1.png` | Affliction | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| `void-caster-seal.v1-try1` | `D/void-crescent-sym.v1-try1.png` | Seal | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| `void-hit-affliction.v1-try1` | `D/void-crescent-sym.v1-try1.png` | Affliction | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| `star-caster-seal.v1-try1` | `D/star-crescent-sym.v1-try1.png` | Seal | cosmic star energy, constellation lines of white-blue light and glittering star dust |
| `star-hit-affliction.v1-try1` | `D/star-crescent-sym.v1-try1.png` | Affliction | cosmic star energy, constellation lines of white-blue light and glittering star dust |

## Xong khi
Có đủ 28 bộ `.png` và `.prompt.txt`. Báo cáo ghi số lần gọi (phải là 28), khổ thật, và một câu mỗi ảnh: đúng dáng không (vòng ấn tròn có tâm trống; vòng bám quanh hình bầu dục trống), nền có đen không, có chữ lọt vào không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
