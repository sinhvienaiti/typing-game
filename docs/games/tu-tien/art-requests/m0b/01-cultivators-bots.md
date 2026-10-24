# Tu Tiên Thủ Ải — M0b · 01. Người chơi và bot đạo đồng (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

Kiếm tu là nhân vật chữ ký, tự rig Blender. Thổ thể tu là người hai chân chuẩn: Tripo Biped một lần 20 credit, Blender thêm chiêu còn thiếu. Bot dùng GLB trường phái còn lại và đổi màu áo (canon §21.2); BOT01 là bảng chất liệu của Thổ thể cho đội có người chơi Kiếm, không tạo model hoặc rig riêng. Khi người chơi Thổ thể, bot dùng lại Kiếm tu và đổi bảng màu tương ứng. «Đạo đồng» là vai bot, không ép hình trẻ em. Phù là trường phái sau MVP, canon chưa có bộ chiêu/hình; không tự thêm nhân vật Phù.

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
| 3 | NV01-F | `cultivators/kiem-tu.png` | 1024×1536 | `identity/kiem-tu-portrait.png` | Đã tạo · chờ duyệt/nền |
| 4 | NV01-B | `cultivators/kiem-tu-back.png` | 1024×1536 | `cultivators/kiem-tu.png` | Đã tạo · chờ duyệt/nền |
| 19 | NV02-F | `cultivators/tho-the-tu.png` | 1024×1536 | — | Đã tạo · chờ duyệt/nền |
| 20 | NV02-B | `cultivators/tho-the-tu-back.png` | 1024×1536 | `cultivators/tho-the-tu.png` | Đã tạo · chờ duyệt/nền |
| 21 | BOT01-F | `bots/bot-dao-dong-tho.png` | 1024×1536 | `cultivators/tho-the-tu.png` | Đã tạo · chờ duyệt/nền |
| 22 | BOT01-B | `bots/bot-dao-dong-tho-back.png` | 1024×1536 | `bots/bot-dao-dong-tho.png` | Đã tạo · chờ duyệt/nền |

## NV01-F · Kiếm tu

**File:** `games/immortality-cultivation/art-src/cultivators/kiem-tu.png` · **Đính kèm:** `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png`.

**3D:** face limit đề xuất 20000 · Tự rig Blender. Nhân vật chữ ký; dáng đi bộ, áo xẻ và động tác Kiếm riêng. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese woman sword cultivator, about thirty, 1.70 m tall, calm warm attentive face, dark eyes, black hair in a compact low bun with a plain ivory pin. Practical indigo Vietnamese five-panel-robe-inspired tunic with ivory inner collar, narrow sleeves, split skirt ending above the knees, separate charcoal trousers and wrapped boots, broad charcoal sash. Natural adult proportions around seven heads tall. Plain geometric woven trim, no writing. No weapon or scabbard on the body; the flying sword is a separate asset.
View and pose: Straight front view, near orthographic, camera at chest height. Neutral anatomical A pose, arms straight down and out 30 degrees from the torso, open empty hands, fingers separated, legs straight and slightly apart, feet parallel, face forward. Both sides symmetrical and unobstructed.
Reference: attach only games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png; use it as a face, hair and palette guide only; replace the portrait framing and scenery with the specified full-body A pose and flat background.
Output: one PNG, 1024x1536.
```

## NV01-B · Kiếm tu · góc phụ

**File:** `games/immortality-cultivation/art-src/cultivators/kiem-tu-back.png` · **Đính kèm:** `games/immortality-cultivation/art-src/cultivators/kiem-tu.png`.

**3D:** face limit đề xuất 20000 · Tự rig Blender. Nhân vật chữ ký; dáng đi bộ, áo xẻ và động tác Kiếm riêng. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese woman sword cultivator, about thirty, 1.70 m tall, calm warm attentive face, dark eyes, black hair in a compact low bun with a plain ivory pin. Practical indigo Vietnamese five-panel-robe-inspired tunic with ivory inner collar, narrow sleeves, split skirt ending above the knees, separate charcoal trousers and wrapped boots, broad charcoal sash. Natural adult proportions around seven heads tall. Plain geometric woven trim, no writing. No weapon or scabbard on the body; the flying sword is a separate asset.
View and pose: Straight rear view of the attached main image, near orthographic, camera at chest height. Preserve the exact identity, materials, proportions, garment construction and neutral A pose; change only the camera by 180 degrees. Arms down and out 30 degrees, hands and feet visible; do not look over the shoulder.
Reference: attach only games/immortality-cultivation/art-src/cultivators/kiem-tu.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## NV02-F · Thổ thể tu

**File:** `games/immortality-cultivation/art-src/cultivators/tho-the-tu.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 10000 · Tripo Biped · 20 credit. Người hai chân chuẩn, áo ngắn; rig cơ bản đủ, Blender thêm chiêu Thổ. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese earth-body cultivator, 1.80 m tall, sturdy broad-shouldered standard human proportions, warm calm face, short black hair under a compact charcoal cloth head wrap. Practical short stone-grey Vietnamese five-panel-robe-inspired tunic, muted ochre-grey solid forearm guards and square belt clasp, charcoal trousers, separate heavy wrapped boots. Open empty hands. Narrow sleeves, no cape, no weapon, no attached floating stones. Square material motifs imply Earth without written symbols.
View and pose: Straight front view, near orthographic, camera at chest height. Neutral anatomical A pose, arms straight down and out 30 degrees from the torso, open empty hands, fingers separated, legs straight and slightly apart, feet parallel, face forward. Both sides symmetrical and unobstructed.
Output: one PNG, 1024x1536.
```

## NV02-B · Thổ thể tu · góc phụ

**File:** `games/immortality-cultivation/art-src/cultivators/tho-the-tu-back.png` · **Đính kèm:** `games/immortality-cultivation/art-src/cultivators/tho-the-tu.png`.

**3D:** face limit đề xuất 10000 · Tripo Biped · 20 credit. Người hai chân chuẩn, áo ngắn; rig cơ bản đủ, Blender thêm chiêu Thổ. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese earth-body cultivator, 1.80 m tall, sturdy broad-shouldered standard human proportions, warm calm face, short black hair under a compact charcoal cloth head wrap. Practical short stone-grey Vietnamese five-panel-robe-inspired tunic, muted ochre-grey solid forearm guards and square belt clasp, charcoal trousers, separate heavy wrapped boots. Open empty hands. Narrow sleeves, no cape, no weapon, no attached floating stones. Square material motifs imply Earth without written symbols.
View and pose: Straight rear view of the attached main image, near orthographic, camera at chest height. Preserve the exact identity, materials, proportions, garment construction and neutral A pose; change only the camera by 180 degrees. Arms down and out 30 degrees, hands and feet visible; do not look over the shoulder.
Reference: attach only games/immortality-cultivation/art-src/cultivators/tho-the-tu.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## BOT01-F · Bot đạo đồng · Thổ thể

**File:** `games/immortality-cultivation/art-src/bots/bot-dao-dong-tho.png` · **Đính kèm:** `games/immortality-cultivation/art-src/cultivators/tho-the-tu.png`.

**3D:** face limit đề xuất 10000 · Dùng rig Thổ thể tu. Bot dùng trường phái còn lại, chỉ đổi màu áo; không dựng hoặc rig thêm. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory. **Không tạo GLB mới.**

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese earth-body cultivator, 1.80 m tall, sturdy broad-shouldered standard human proportions, warm calm face, short black hair under a compact charcoal cloth head wrap. Practical short stone-grey Vietnamese five-panel-robe-inspired tunic, muted ochre-grey solid forearm guards and square belt clasp, charcoal trousers, separate heavy wrapped boots. Open empty hands. Narrow sleeves, no cape, no weapon, no attached floating stones. Square material motifs imply Earth without written symbols. Bot material study: exactly the same adult body and clothing geometry as Tho The Tu; change the tunic to pale muted moss-grey and the collar to ivory, retain charcoal trousers and square motifs. Bot dao dong is a role label, not a child. No new accessories or geometry.
View and pose: Straight front view, near orthographic, camera at chest height. Neutral anatomical A pose, arms straight down and out 30 degrees from the torso, open empty hands, fingers separated, legs straight and slightly apart, feet parallel, face forward. Both sides symmetrical and unobstructed.
Reference: attach only games/immortality-cultivation/art-src/cultivators/tho-the-tu.png; use it as the exact body and clothing design; change only the described garment colors.
Output: one PNG, 1024x1536.
```

## BOT01-B · Bot đạo đồng · Thổ thể · góc phụ

**File:** `games/immortality-cultivation/art-src/bots/bot-dao-dong-tho-back.png` · **Đính kèm:** `games/immortality-cultivation/art-src/bots/bot-dao-dong-tho.png`.

**3D:** face limit đề xuất 10000 · Dùng rig Thổ thể tu. Bot dùng trường phái còn lại, chỉ đổi màu áo; không dựng hoặc rig thêm. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape art translated into a hand-painted 3D maquette, broad sculpted masses, restrained ink-wash value steps, matte indigo, limestone grey, ink charcoal, muted moss and warm ivory; readable from an elevated game camera, serious yet warm for teenagers. Fine do-paper character belongs to the painted material, not the background.
Framing: exactly one complete subject, centered, all extremities visible, 10 percent empty margin; one view only.
Background: perfectly uniform flat light grey #E6E6E6, no gradient, vignette, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle form shading only, no rim lighting, bloom, reflections or baked directional shadows.
Build: coherent solid volumes, broad cloth and fur clumps, strong separate limbs, opaque surfaces; small details grouped into sturdy masses suitable for reconstruction.
Color rules: vermilion belongs to UI seals; enemy red #FF4A4A, urgent orange #FFB020, reward gold #FFC83A and typing turquoise #7FF5E0 are reserved for runtime signals and absent from the asset.
Constraints: no text, letters, numbers, logos, watermarks, labels, frame, blood, wounds, gore or horror. No smoke, mist, fire, sparks, particles, aura, trails, glowing eyes, emissive light or other effects. Trọc khí is a flat ink-dark material motif, never a cloud or injury. Original designs only.
Subject: One adult Vietnamese earth-body cultivator, 1.80 m tall, sturdy broad-shouldered standard human proportions, warm calm face, short black hair under a compact charcoal cloth head wrap. Practical short stone-grey Vietnamese five-panel-robe-inspired tunic, muted ochre-grey solid forearm guards and square belt clasp, charcoal trousers, separate heavy wrapped boots. Open empty hands. Narrow sleeves, no cape, no weapon, no attached floating stones. Square material motifs imply Earth without written symbols. Bot material study: exactly the same adult body and clothing geometry as Tho The Tu; change the tunic to pale muted moss-grey and the collar to ivory, retain charcoal trousers and square motifs. Bot dao dong is a role label, not a child. No new accessories or geometry.
View and pose: Straight rear view of the attached main image, near orthographic, camera at chest height. Preserve the exact identity, materials, proportions, garment construction and neutral A pose; change only the camera by 180 degrees. Arms down and out 30 degrees, hands and feet visible; do not look over the shoulder.
Reference: attach only games/immortality-cultivation/art-src/bots/bot-dao-dong-tho.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

