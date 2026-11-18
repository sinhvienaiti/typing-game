# Phiếu 302 · Tu Tiên · Ảnh 2D: kiếm khí lưỡi liềm đối xứng cho 14 hệ, 14 lần gọi `image_gen`

Anh (05/11 ~21:20): "chúng ta đang bắn ra kiếm, nên đáng lẽ nếu có làm dạng vết chém thì phải làm dạng lưỡi liềm đều, chứ k phải làm dạng vệt chém k cân như hiện tại, chúng ta đang bắn kiếm thẳng ra cơ mà". Phái Kiếm bắn kiếm thẳng; kiếm khí phải là lưỡi liềm **đối xứng**. Ảnh vệt chém hiện có lệch một bên (động tác vung). Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 14 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/302-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
Mở ảnh tham chiếu của hệ bằng `view_image` (ảnh anh đã duyệt, chỉ lấy chất liệu, ánh sáng, độ hoàn thiện; KHÔNG lấy dáng lệch của nó). Gọi `image_gen` tạo mới, khổ ngang 16:9, kèm ảnh đó. Prompt nguyên văn, thay `<MATTER>` bằng cột chất liệu:

```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its lopsided shape. A perfectly SYMMETRIC crescent of sword qi made of <MATTER>: both horns exactly equal in length and thickness, mirror-symmetric about the vertical centre line, the convex side facing up/forward like a crescent wave flying straight ahead, a thin blazing edge along the convex front, the element's matter trailing back toward the concave side, fine sparkles and glints shed behind; seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, radiant translucent energy, anime-mythic. Centred with a wide empty border, solid pure black background, no sword, no text.
```

Chép kết quả bằng `cp -n` thành `D/<tên ra>.png`; ghi `D/<tên ra>.prompt.txt` (công cụ, ảnh tham chiếu, prompt đã gửi, khổ thật).

| Tên ra | Ảnh tham chiếu | Chất liệu `<MATTER>` |
|---|---|---|
| `metal-crescent-sym.v1-try1` | `D/metal-slash-arc.v1-try1.jpg` | razor-sharp white-silver metal light with pale jade edges and star glints |
| `fire-crescent-sym.v1-try1` | `D/fire-slash-arc.v1-try1.jpg` | dense white-gold, amber and vermilion flame with embers and sparks |
| `water-crescent-sym.v1-try1` | `D/water-slash-arc-clean.v1-try1.jpg` | clear deep-blue spirit water with a bright white pressure edge, thin foam and caustic light |
| `thunder-crescent-sym.v1-try1` | `D/thunder-slash-arc-clean.v1-try1.jpg` | violet-white lightning with a blinding white core line and crackling branching arcs |
| `wind-crescent-sym.v1-try1` | `D/wind-slash-arc-clean.v1-try1.jpg` | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| `ice-crescent-sym.v1-try1` | `D/ice-slash-arc-clean.v1-try1.jpg` | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| `earth-crescent-sym.v1-try1` | `D/earth-slash-arc.v1-try1.jpg` | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| `wood-crescent-sym.v1-try1` | `D/wood-ground-mark.v1-try1.jpg` | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| `dark-crescent-sym.v1-try1` | `D/dark-slash-arc-a.v1-try2.png` | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| `light-crescent-sym.v1-try1` | `D/light-slash-arc-clean.v1-try1.jpg` | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| `poison-crescent-sym.v1-try1` | `D/poison-slash-arc.v1-try1.jpg` | luminous toxic green and violet miasma with acid droplets and spores |
| `blood-crescent-sym.v1-try1` | `D/blood-slash-arc.v1-try1.jpg` | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| `void-crescent-sym.v1-try1` | `D/void-slash-arc.v1-try1.jpg` | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| `star-crescent-sym.v1-try1` | `D/star-slash-arc.v1-try1.jpg` | cosmic star energy, constellation lines of white-blue light and glittering star dust |

## Xong khi
Đủ 14 bộ `.png` và `.prompt.txt`. Báo cáo ghi khổ thật, số lần gọi (phải là 14), một câu mỗi ảnh: có đối xứng hai sừng không, nền có đen không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
