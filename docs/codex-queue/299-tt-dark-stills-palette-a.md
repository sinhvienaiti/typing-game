# Phiếu 299 · Tu Tiên · Ảnh 2D: vẽ lại bộ Ám theo màu A (đen, viền đỏ thẫm), 3 lần gọi `image_gen`

Anh (05/11 19:12): "màu ám vì sao lại giống màu tím vậy"; 19:20 anh chọn hướng A "đen đỏ thẫm". Ảnh Ám cũ (G19–G21) màu tím bị bỏ. ChatGPT đang lỗi tải lại trang, nên Codex vẽ cùng. Phiếu ảnh ngắn, prompt đã chốt.

**Model `gpt-6.1-sol`, mức `high`. Đúng 3 lần gọi `image_gen`, không gọi thêm, không tự sửa lại.**

**Báo cáo:** `docs/codex-queue/299-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`D = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`

**Được ghi:** chỉ thêm file mới vào `D` (`cp -n`, không ghi đè) và `docs/codex-queue/299-report.md`.
**Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài làm tham chiếu.

## Việc
Mỗi ảnh: mở hai ảnh tham chiếu bằng `view_image`, gọi `image_gen` tạo mới khổ ngang 16:9 kèm hai ảnh đó, **prompt dán nguyên văn**; chép kết quả bằng `cp -n` thành `D/<tên ra>.png`; ghi `D/<tên ra>.prompt.txt` (công cụ, hai ảnh tham chiếu, prompt, khổ thật).

| Tên ra | Tham chiếu màu và bố cục (bản đổi màu anh chọn) | Tham chiếu phong cách |
|---|---|---|
| `dark-slash-arc-a.v1-try2` | `D/dark-slash-arc-colour-study-a.v1-try1.jpg` | `D/thunder-slash-arc-clean.v1-try1.jpg` |
| `dark-ground-mark-a.v1-try2` | `D/dark-ground-mark-colour-study-a.v1-try1.jpg` | `D/thunder-ground-mark-clean.v1-try1.jpg` |
| `ult-dark-a.v1-try2` | `D/ult-dark-colour-study-a.v1-try1.jpg` | `D/pillar-thunder-field-clean.v1-try1.jpg` |

Câu đầu chung của cả ba prompt (dán trước prompt riêng): `Use the first attached image only as the colour and composition reference (black with dark-crimson ember light) and the second only as the style reference for glow, sparkle and finish; do not copy the second image's shape or colour.`

Câu cuối chung: `Premium Chinese donghua xianxia skill effect, mythic and explosive, radiant energy with volumetric depth, fine luminous detail, glints and ember sparks, soft halos and thin light rays; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down unless stated. Main shape centred with a wide empty border, solid pure black background, no text or lettering. 16:9.`

Prompt riêng:
- `dark-slash-arc-a`: `A crescent slash made of deep black shadow smoke and ink, outlined by a thin blazing dark-crimson ember edge, black tendrils trailing behind it, a few red-hot sparks and tiny embers; the black body is lit only by its ember rims and a faint red under-glow. Almost no colour except black and ember red; no purple, no violet.`
- `dark-ground-mark-a`: `Top-down view: stone ground scorched black by a shadow blow, black ink stains and cracks spreading in a circle from the hit point, thin smouldering dark-crimson ember glow deep inside the cracks, wisps of black smoke and a few red sparks. Almost no colour except black and ember red; no purple, no violet.`
- `ult-dark-a`: `An eclipse: a black sun with a thin blazing dark-crimson corona rises over the battlefield, the field sinks into black shadow, and giant shadow hands of black smoke outlined in ember red rise from the ground to drag the beasts down. Almost no colour except black and ember red; no purple, no violet.`

## Xong khi
- Đủ 3 bộ `.png` và `.prompt.txt` trong `D`; báo cáo ghi khổ thật, số lần gọi `image_gen` (phải là 3), một câu nhận xét mỗi ảnh (có tím không).

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
