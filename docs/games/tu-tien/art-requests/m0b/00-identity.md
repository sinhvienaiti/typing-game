# Tu Tiên Thủ Ải — M0b · 00. Hai ảnh bản sắc (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

Hai ảnh dùng duyệt bản sắc trước khi dựng 3D; không đưa cả cảnh hoặc chân dung bán thân vào Tripo. Nguồn dựng nhân vật là NV01-F/B; nguồn dựng cảnh tách từng vật ở file 06. Tên game vẫn tạm tới khi anh duyệt. Cảnh có hiệu ứng để thử giọng hình; các ảnh tái dựng phía sau bỏ toàn bộ hiệu ứng.

```text
Instructions for the image tool (Codex image_gen or ChatGPT)
- Use exactly one complete prompt block below per image, verbatim.
- Keep one view per image; never make a contact sheet or multiview collage.
- Attach only the image in the reference column when specified.
- A secondary view must preserve the main image and change only the camera.
- Save one PNG and the exact prompt beside it as <id>.prompt.txt.
- Follow README order; every output, including retries, counts toward the 40-image cap.
```

| Thứ tự | Mã | File | Khổ yêu cầu | Đính kèm duy nhất | Lượt |
|---:|---|---|---|---|---|
| 1 | BS01 | `identity/thanh-thach-ai.png` | 1536×1024 | — | Đã tạo · chờ duyệt/nền |
| 2 | BS02 | `identity/kiem-tu-portrait.png` | 1024×1536 | — | Đã tạo · chờ duyệt/nền |

## BS01 · Thanh Thạch Ải lúc thú triều

**File:** `games/immortality-cultivation/art-src/identity/thanh-thach-ai.png` · **Đính kèm:** không.

```text
Use case: stylized-concept.
Asset type: art direction approval for the original Vietnamese fantasy defense game Tu Tien Thu Ai; a visual guide for later 3D modeling, not a direct reconstruction plate.
Scene: Thanh Thach Ai, a broad limestone frontier pass, two winding entrances at the far left and far right, a circular low stone formation core near the lower center and exactly two tall stone cover pillars. A quiet Vietnamese mountain sect gateway sits far behind the core. Vertical karst cliffs and indigo mist frame the pass; sparse old pine trees.
Action: a beast tide of low stone-backed rats, lean wolves, broad armored boars, tall rock macaques and a few dark crows approaches the defenders. One adult sword cultivator in indigo and warm ivory cloth stands beside the core. A huge iron-backed wolf king can be read in the far pass. A restrained arc of physical ivory flying swords shows the large sword technique. On the ground, a defeated small beast dissolves into a soft ink stain and a few ivory motes.
Style: original Vietnamese fantastical landscape, sculptural stylized 3D forms with restrained ink wash shading, subtle do-paper grain, large readable masses, serious yet warm, suitable for teenagers. Fixed elevated three-quarter game camera around 52 degrees; legible battlefield with open paths.
Palette: indigo, limestone grey, ink charcoal, muted moss and warm ivory. Small ivory spiritual highlights. Vermilion belongs to UI seals and is absent from this scene. Enemy warning red, urgent orange, reward gold and typing turquoise are reserved for runtime signals.
Constraints: one coherent landscape, no interface, no text, letters, numbers, logos or watermarks. No blood, wounds, gore, horror, religious ceremony or borrowed game characters. No scroll-shaped character cards.
Output: one landscape PNG, 1536x1024.
```

## BS02 · Chân dung Kiếm tu

**File:** `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png` · **Đính kèm:** không.

```text
Use case: stylized-concept.
Asset type: portrait for art direction approval of the original Vietnamese fantasy game Tu Tien Thu Ai; a guide for a later 3D cultivator model.
Subject: one adult Vietnamese woman sword cultivator, around thirty, calm attentive warm expression, natural face, dark eyes, black hair gathered in a compact low bun held by a plain ivory pin. Practical indigo five-panel robe inspired by Vietnamese ao ngu than, ivory inner collar, narrow sleeves, broad charcoal waist sash. A closed charcoal scabbard with a simple ivory sword pommel is visible at her side.
Scene: waist-up portrait at a limestone frontier pass, restrained indigo atmospheric haze and a distant old pine, quiet background.
Style: sculptural stylized 3D concept art with restrained ink-wash shading and subtle do-paper grain; believable adult proportions, broad matte material masses, serious yet warm, suitable for teenagers.
Palette: indigo cloth, limestone grey, ink charcoal and warm ivory; quiet muted moss. Use ivory spiritual light very sparingly. Vermilion, warning red, urgent orange, reward gold and typing turquoise are reserved for runtime signals and absent from costume.
Lighting: broad soft daylight; readable face and garment construction.
Constraints: one original character, no UI, no text, letters, numbers, seals, logos or watermarks. No blood, injuries, horror, religious ceremony, ornamental headdress, scroll-shaped character cards or copied game designs.
Output: one portrait PNG, 1024x1536.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

