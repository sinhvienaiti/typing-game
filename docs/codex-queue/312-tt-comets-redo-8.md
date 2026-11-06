# Phiếu 312 · Tu Tiên · Ảnh 2D: vẽ lại 7 sao băng chưa đạt (2 giám khảo mù < 8), 8 lần gọi `image_gen`

Anh (06/11 12:15): ảnh 2D phải đạt trên 8. Hai giám khảo mù chấm 14 sao băng; 8 ảnh chưa đạt. Phiếu này vẽ lại 7 ảnh đó (Mộc đã vẽ lại qua Gemini) theo lời sửa của giám khảo. Riêng Ám vẫn giữ bảng màu A anh đã chốt (đen, viền đỏ thẫm). Mẫu đã đạt để tham khảo độ hoàn thiện: `D/fire-comet.v1-try1.png`, `D/star-comet.v1-try1.png`. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 7 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.** Báo cáo: `docs/codex-queue/312-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. **Được ghi:** chỉ thêm file mới vào `D` (`cp -n`) và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Cách làm mỗi ảnh
1. Mở bằng `view_image` ảnh lưỡi liềm của hệ (chất liệu) và `D/fire-comet.v1-try1.png` (dáng và độ hoàn thiện đã đạt). Đó là ảnh anh đã duyệt; chỉ lấy chất liệu, ánh sáng, độ phát sáng và độ hoàn thiện, **không lấy dáng lưỡi liềm**.
2. Gọi `image_gen` tạo mới, khổ ngang, kèm hai ảnh đó, **nền đen** (không bật nền trong suốt). Prompt dán nguyên văn, thay `<MATTER>` bằng cột chất liệu.
3. Chép bằng `cp -n` thành `D/<tên ra>.png`.
4. Ghi `D/<tên ra>.prompt.txt`: công cụ, ảnh tham chiếu, prompt đã gửi, khổ thật.

```text
Use the attached image only as the reference for material, light, glow and finish; do not copy its crescent shape. A meteor of <MATTER> falling diagonally from the upper left toward the lower right, about 20 degrees from vertical: a dense blazing rounded head with a white-hot core and a bright shimmering rim, followed by a long tapering tail of the same matter that streams back up toward the upper left, thins and breaks into sparks, embers and glints, with soft halos around the head. Seen from a high three-quarter game camera about 55 degrees down. Premium Chinese donghua xianxia skill effect, mythic and radiant, translucent energy, anime-mythic, not realistic. The whole meteor inside the frame with a wide empty border, solid pure black background, no ground, no crescent, no sword, no text.
```

| Tên ra | Ảnh tham chiếu | `<MATTER>` |
|---|---|---|
| `metal-comet.v1-try2` | `D/metal-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably METAL: a dense head of polished steel and sword-blade shards with hard white specular edges and warm gold highlights, a cool steel-silver palette (not teal, not ice), the tail made of streaming blade shards and metal sparks |
| `earth-comet.v1-try2` | `D/earth-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably EARTH: a dense head of dark jagged boulders and rock shards glowing through amber crack-light, an ochre, brown and jade palette with a gold glow, the tail made of rock fragments, gravel and dust, no flames |
| `dark-comet.v1-try2` | `D/dark-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | black shadow smoke and ink with a thin blazing dark-crimson ember edge: a LARGE, dense head of churning black smoke with a bright crimson-ember rim and a hot core, strong contrast, the tail of black smoke and ink wisps breaking into crimson embers; black and dark-crimson only, no purple, no violet |
| `wind-comet.v1-try2` | `D/wind-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably WIND: a dense, bright rounded head of compressed spiralling air with strong mint-white pressure rims, thick bold spiral air bands and cut-air arcs, cloud wisps and dust in the tail, high contrast; no leaves |
| `poison-comet.v1-try2` | `D/poison-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably POISON: a dense bubbling head of viscous toxic green fluid with dripping venom forms and popping bubbles, green dominant with a little violet, the tail of dripping viscous streams and toxic droplets |
| `blood-comet.v1-try2` | `D/blood-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably BLOOD: a dense head of thick viscous arterial-crimson blood with dark clots and glossy highlights, drip and splatter forms, the tail of thick streaming blood and droplets, few crystal facets |
| `void-comet.v1-try2` | `D/void-crescent-sym.v1-try1.png`, `D/fire-comet.v1-try1.png` | unmistakably VOID: a dense head with a dark swallowing vortex centre and a thin bright rim of distorted space, broken-glass spatial cracks with indigo-white edges, darker body than star or ice, the tail of floating shards of space |

## Xong khi
Có đủ 7 bộ `.png` và `.prompt.txt`. Báo cáo ghi khổ thật, số lần gọi (phải là 7), và một câu mỗi ảnh: đầu sao băng có rõ không, đuôi có thon dần không, có dáng lưỡi liềm hay chữ lọt vào không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
