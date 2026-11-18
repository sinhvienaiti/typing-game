# Phiếu 298 · Tu Tiên · Ảnh 2D: vẽ lại tuyệt kỹ Thủy và Lôi, 4 lần gọi `image_gen`

Anh (05/11 18:10) loại ảnh tuyệt kỹ Thủy (có đôi mắt khổng lồ) và Lôi (có cuộn chiếu chỉ dài): "nó k hợp tý nào". Gemini hết lượt ảnh; anh cho Codex vẽ cùng (18:20). ChatGPT đang vẽ bản `try1`; Codex vẽ `try2` và `try3` để anh có lựa chọn. Phiếu ảnh ngắn, prompt đã chốt, không cần phản biện.

**Model `gpt-6.1-sol`, mức `high`. Đúng 4 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/298-report.md` (tiếng Việt, ngắn).

## Đường dẫn

`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`

**Được ghi:** chỉ thêm file mới vào `D` (không ghi đè, dùng `cp -n`) và `docs/codex-queue/298-report.md`.

**Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; dùng ảnh ngoài làm tham chiếu.

## Ảnh tham chiếu (của mình, anh đã duyệt)

Mở từng ảnh bằng `view_image` trước khi gọi `image_gen`. Chỉ dùng làm tham chiếu phong cách (ánh sáng, độ trong, phát sáng, lấp lánh, độ hoàn thiện), không chép dáng hay bố cục.

| Ảnh | Tham chiếu |
|---|---|
| Thủy | `D/water-slash-arc-clean.v1-try1.jpg`, `D/water-ground-mark-clean.v1-try1.jpg` |
| Lôi | `D/thunder-slash-arc-clean.v1-try1.jpg`, `D/pillar-thunder-field-clean.v1-try1.jpg` |

## Việc: 4 ảnh, khổ ngang 16:9 (hoặc khổ ngang gần nhất)

| Tên ra | Prompt |
|---|---|
| `ult-water-profound-sea-v2.v1-try2` | Prompt Thủy |
| `ult-water-profound-sea-v2.v1-try3` | Prompt Thủy |
| `ult-thunder-nine-heavens-v2.v1-try2` | Prompt Lôi |
| `ult-thunder-nine-heavens-v2.v1-try3` | Prompt Lôi |

Mỗi ảnh:
1. Gọi `image_gen` ở chế độ tạo mới, kèm hai ảnh tham chiếu của hệ đó. **Prompt dán nguyên văn**, không thêm, không bớt.
2. Chép ảnh trả về từ `~/.codex/generated_images/...` bằng `cp -n` thành `D/<tên ra>.png`, giữ nguyên khổ thật.
3. Ghi `D/<tên ra>.prompt.txt`: công cụ (Codex `image_gen`, model, mức), hai đường dẫn ảnh tham chiếu, prompt nguyên văn, khổ thật.

### Prompt Thủy (nguyên văn)

```text
Use the attached images only as the style reference for light, translucency, glow, sparkle and finish; do not copy their shapes. The battlefield ground opens into a colossal whirlpool of deep translucent spirit water: a spiralling abyss of clear blue and deep indigo water with bright white foam rims and shimmering caustic light; towering spiral water columns erupt around its rim and a huge ring-shaped tidal wave crashes inward, spray and droplets glittering. Premium Chinese donghua xianxia skill effect, mythic and explosive, radiant translucent energy with volumetric depth, fine luminous detail, glints and star twinkles, soft halos and thin light rays; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Main shape centred with a wide empty border, solid pure black background. Water and light only: no creature, no face, no eyes, no text.
```

### Prompt Lôi (nguyên văn)

```text
Use the attached images only as the style reference for light, translucency, glow, sparkle and finish; do not copy their shapes. Above the battlefield nine stacked rings of violet storm clouds form a colossal spiralling vortex; at its centre a huge glowing violet-white thunder seal, a circular rune disk of light, blazes; a downpour of violet-white lightning bolts strikes straight down onto the ground at many points at once, each strike bursting into a ring of electric light. Premium Chinese donghua xianxia skill effect, mythic and explosive, radiant translucent energy with volumetric depth, fine luminous detail, glints and star twinkles, soft halos and thin light rays; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Main shape centred with a wide empty border, solid pure black background. No scroll, no paper, no text, no letters.
```

## Xong khi
- Có đủ 4 bộ `.png` và `.prompt.txt` trong `D`.
- Báo cáo ghi khổ thật mỗi ảnh, số lần gọi `image_gen` (phải là 4) và một câu nhận xét mỗi ảnh (có mắt, mặt, sinh vật hay cuộn giấy không).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
