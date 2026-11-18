# Phiếu 307 · Tu Tiên · Ảnh 2D: sao băng rơi chéo cho 12 hệ còn lại, 12 lần gọi `image_gen`

Anh duyệt 2 mẫu của phiếu 306 (06/11 10:10: "Đạt, làm 14 hệ"). Phiếu này vẽ 12 hệ còn lại, đúng cách và đúng prompt của 306 (mẫu: `D/fire-comet.v1-try1.png`, `D/water-comet.v1-try1.png`). Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 12 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.** Báo cáo: `docs/codex-queue/307-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu của hệ bằng `view_image`. Đó là ảnh anh đã duyệt; chỉ lấy chất liệu, ánh sáng, độ phát sáng và độ hoàn thiện, **không lấy dáng lưỡi liềm**.
2. Gọi `image_gen` tạo mới, khổ ngang, kèm ảnh đó, **nền đen** (không bật nền trong suốt). Prompt dán nguyên văn, thay `<MATTER>` bằng cột chất liệu.
3. Chép bằng `cp -n` thành `D/<tên ra>.png`.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, ảnh tham chiếu, prompt đã gửi, khổ thật.

```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its crescent shape. A meteor of <MATTER> falling diagonally from the upper left toward the lower right, about 20 degrees from vertical: a dense blazing rounded head with a white-hot core and a bright shimmering rim, followed by a long tapering tail of the same matter that streams back up toward the upper left, thins and breaks into sparks, embers and glints, with soft halos around the head. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, anime-mythic, not realistic. The whole meteor inside the frame with a wide empty border, solid pure black background, no ground, no crescent, no sword, no text.
```

| Tên ra | Ảnh tham chiếu | `<MATTER>` |
|---|---|---|
| `metal-comet.v1-try1` | `D/metal-crescent-sym.v1-try1.png` | razor-sharp white-silver metal light with pale jade edges and star glints |
| `thunder-comet.v1-try1` | `D/thunder-crescent-sym.v1-try1.png` | violet-white lightning with a blinding white core line and crackling branching arcs |
| `wind-comet.v1-try1` | `D/wind-crescent-sym.v1-try1.png` | almost invisible compressed air outlined by bright mint-white pressure rims and helical eddies, carrying small leaves |
| `ice-comet.v1-try1` | `D/ice-crescent-sym.v1-try1.png` | glassy faceted ice crystal with a cold-white razor edge, pale blue to cold violet, frost particles |
| `earth-comet.v1-try1` | `D/earth-crescent-sym.v1-try1.png` | heavy compressed sandstone and granite with glowing amber mineral seams and trailing dust |
| `wood-comet.v1-try1` | `D/wood-crescent-sym.v1-try1.png` | living celadon spiritwood with glowing lime sap-veins, small leaves and pollen sparkles |
| `dark-comet.v1-try1` | `D/dark-crescent-sym.v1-try1.png` | black shadow smoke and ink with a thin blazing dark-crimson ember edge; no purple, no violet |
| `light-comet.v1-try1` | `D/light-crescent-sym.v1-try1.png` | radiant holy white-gold light with warm halos, crisp rays and light feathers |
| `poison-comet.v1-try1` | `D/poison-crescent-sym.v1-try1.png` | luminous toxic green and violet miasma with acid droplets and spores |
| `blood-comet.v1-try1` | `D/blood-crescent-sym.v1-try1.png` | deep crimson liquid blood energy with glossy droplets and red crystal shards |
| `void-comet.v1-try1` | `D/void-crescent-sym.v1-try1.png` | spatial void energy, cracks like broken glass with indigo-white edges, floating shards of space |
| `star-comet.v1-try1` | `D/star-crescent-sym.v1-try1.png` | cosmic star energy, constellation lines of white-blue light and glittering star dust |

## Xong khi
Có đủ 12 bộ `.png` và `.prompt.txt`. Báo cáo ghi khổ thật, số lần gọi (phải là 12), và một câu mỗi ảnh: đầu sao băng có rõ không, đuôi có thon dần không, có dáng lưỡi liềm hay chữ lọt vào không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
