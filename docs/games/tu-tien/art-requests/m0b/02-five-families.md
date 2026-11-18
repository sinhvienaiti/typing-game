# Tu Tiên Thủ Ải — M0b · 02. Năm họ thú và biến chủng hệ (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

T01–T05 là năm họ chương 1 (canon §10.2). Hỏa Nha ở trận dạy vô hệ: tên Hỏa không cho phép thêm lửa vào ảnh. Nham Viên hai chân dùng tư thế A nhưng tỉ lệ tay dài cần Blender, không mua Biped. BT01/BT02 là chất liệu Đằng Thử (Mộc) và Khê Viên (Thủy, M1), cùng GLB gốc theo D23; bốn ảnh này nằm sau giới hạn 40 ảnh, đã có prompt để làm tiếp.

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
| 9 | T01-S | `beasts/thach-thu.png` | 1536×1024 | — | Đã tạo · chờ duyệt/nền |
| 10 | T01-F | `beasts/thach-thu-front.png` | 1024×1024 | `beasts/thach-thu.png` | Đã tạo · chờ duyệt/nền |
| 11 | T02-S | `beasts/phong-lang.png` | 1536×1024 | `commanders/lang-dau-dan.png` | Đã tạo · chờ duyệt/nền |
| 12 | T02-F | `beasts/phong-lang-front.png` | 1024×1024 | `beasts/phong-lang.png` | Đã tạo · chờ duyệt/nền |
| 13 | T03-F | `beasts/hoa-nha.png` | 1536×1024 | — | Đã tạo · chờ duyệt/nền |
| 14 | T03-S | `beasts/hoa-nha-side.png` | 1024×1024 | `beasts/hoa-nha.png` | Đã tạo/làm lại · góc phụ chưa đạt |
| 15 | T04-F | `beasts/nham-vien.png` | 1024×1536 | — | Đã tạo · chờ duyệt/nền |
| 16 | T04-B | `beasts/nham-vien-back.png` | 1024×1536 | `beasts/nham-vien.png` | Đã tạo · chờ duyệt/nền |
| 17 | T05-S | `beasts/thiet-giap-tru.png` | 1536×1024 | — | Đã tạo · chờ duyệt/nền |
| 18 | T05-F | `beasts/thiet-giap-tru-front.png` | 1024×1024 | `beasts/thiet-giap-tru.png` | Đã tạo · chờ duyệt/nền |
| 41 | BT01-S | `variants/dang-thu.png` | 1536×1024 | `beasts/thach-thu.png` | Chưa tạo · trần 40 |
| 42 | BT01-F | `variants/dang-thu-front.png` | 1024×1024 | `variants/dang-thu.png` | Chưa tạo · trần 40 |
| 43 | BT02-F | `variants/khe-vien.png` | 1024×1536 | `beasts/nham-vien.png` | Chưa tạo · trần 40 |
| 44 | BT02-B | `variants/khe-vien-back.png` | 1024×1536 | `variants/khe-vien.png` | Chưa tạo · trần 40 |

## T01-S · Thạch Thử

**File:** `games/immortality-cultivation/art-src/beasts/thach-thu.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 4000 · Tự rig Blender. Bốn chân, cắn; cần chu kỳ bầy ổn định để nướng VAT. Clip: Idle, Move, Attack, Death (Move: chạy; Attack: cắn).

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
Subject: One Thach Thu spirit rat, shoulder height 0.35 m, body length 0.65 m. Low compact rounded body, blunt muzzle, small round ears, four short stout legs with broad feet, one thick tapering curved tail kept clear of the feet. Limestone-grey pebble-like fur masses on the back, charcoal undercoat, ivory muzzle; three broad ink-dark painted marks across the back. Dark eyes. Stone quality is stylized intact surface, not broken skin.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Output: one PNG, 1536x1024.
```

## T01-F · Thạch Thử · góc phụ

**File:** `games/immortality-cultivation/art-src/beasts/thach-thu-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/thach-thu.png`.

**3D:** face limit đề xuất 4000 · Tự rig Blender. Bốn chân, cắn; cần chu kỳ bầy ổn định để nướng VAT. Clip: Idle, Move, Attack, Death (Move: chạy; Attack: cắn).

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
Subject: One Thach Thu spirit rat, shoulder height 0.35 m, body length 0.65 m. Low compact rounded body, blunt muzzle, small round ears, four short stout legs with broad feet, one thick tapering curved tail kept clear of the feet. Limestone-grey pebble-like fur masses on the back, charcoal undercoat, ivory muzzle; three broad ink-dark painted marks across the back. Dark eyes. Stone quality is stylized intact surface, not broken skin.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/beasts/thach-thu.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## T02-S · Phong Lang

**File:** `games/immortality-cultivation/art-src/beasts/phong-lang.png` · **Đính kèm:** `games/immortality-cultivation/art-src/commanders/lang-dau-dan.png`.

**3D:** face limit đề xuất 6000 · Tự rig Blender. Bốn chân, cắn và vồ; chung rig với Lang Đầu Đàn. Clip: Idle, Move, Attack, Death (Move: chạy; Attack: cắn/vồ).

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Reference: attach only games/immortality-cultivation/art-src/commanders/lang-dau-dan.png; use it as the exact wolf anatomy and fur-clump construction; retain the silhouette, replace the commander's ivory shoulder chevron with the described charcoal markings.
Output: one PNG, 1536x1024.
```

## T02-F · Phong Lang · góc phụ

**File:** `games/immortality-cultivation/art-src/beasts/phong-lang-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/phong-lang.png`.

**3D:** face limit đề xuất 6000 · Tự rig Blender. Bốn chân, cắn và vồ; chung rig với Lang Đầu Đàn. Clip: Idle, Move, Attack, Death (Move: chạy; Attack: cắn/vồ).

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/beasts/phong-lang.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## T03-F · Hỏa Nha

**File:** `games/immortality-cultivation/art-src/beasts/hoa-nha.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 5000 · Tự rig Blender. Cánh, bay và bổ nhào; không dùng Biped/Quadruped Tripo. Clip: Idle, Move, Attack, Death (Idle: lơ lửng; Move: bay; Attack: bổ nhào; Death: rơi).

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
Subject: One Hoa Nha spirit crow, body length 0.6 m, wingspan 1.4 m. Clearly avian silhouette, strong broad wings with a few solid overlapping feather groups, short thick beak, two sturdy three-toed feet, short fan tail. Matte charcoal and deep indigo plumage with warm ash-ivory feather edges on the breast and wing roots. Flat ink-dark shoulder markings. This chapter-one teaching form is elementless despite its name: no red plumage, no flames, no fire effect.
View and pose: Straight front view, near orthographic, body level, beak forward, both opaque wings raised and spread in a shallow V, each feather group a solid broad volume, two legs separated below the body. Neutral reconstruction pose, not a dive.
Output: one PNG, 1536x1024.
```

## T03-S · Hỏa Nha · góc phụ

**File:** `games/immortality-cultivation/art-src/beasts/hoa-nha-side.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/hoa-nha.png`.

**3D:** face limit đề xuất 5000 · Tự rig Blender. Cánh, bay và bổ nhào; không dùng Biped/Quadruped Tripo. Clip: Idle, Move, Attack, Death (Idle: lơ lửng; Move: bay; Attack: bổ nhào; Death: rơi).

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
Subject: One Hoa Nha spirit crow, body length 0.6 m, wingspan 1.4 m. Clearly avian silhouette, strong broad wings with a few solid overlapping feather groups, short thick beak, two sturdy three-toed feet, short fan tail. Matte charcoal and deep indigo plumage with warm ash-ivory feather edges on the breast and wing roots. Flat ink-dark shoulder markings. This chapter-one teaching form is elementless despite its name: no red plumage, no flames, no fire effect.
View and pose: EXACT LEFT ORTHOGRAPHIC SIDE ELEVATION of the attached bird, beak pointing LEFT. Camera yaw exactly 90 degrees from the front plate, with the bird's beak, sternum, pelvis and tail aligned on one horizontal sagittal plane. Preserve the FRONT plate's exact wing joint angles: both wings are spread laterally in the same shallow V, perpendicular to this side camera; therefore show the near wing mainly EDGE-ON as a narrow raised silhouette and let it occlude the far wing. Never rotate either wing to display its broad front face. Keep the body level, both feet hanging below, and preserve all plumage colors and feather groups. Change only the camera. No three-quarter view.
Reference: attach only games/immortality-cultivation/art-src/beasts/hoa-nha.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## T04-F · Nham Viên

**File:** `games/immortality-cultivation/art-src/beasts/nham-vien.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 8000 · Tự rig Blender. Tỉ lệ tay dài của Viên và clip ném riêng; không phải người chuẩn. Clip: Idle, Move, Attack, Death (Move: bước nặng; Attack: ném).

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
Subject: One Nham Vien spirit macaque, upright height 1.6 m, a tall two-legged rocky macaque with a broad chest, long strong separate arms, five-fingered hands, short sturdy legs and a thick short tail clear of the legs. Limestone-grey fur sculpted into large rock-like clumps, charcoal forearms, warm ivory face with a calm but formidable closed muzzle. Flat dark ink markings over upper back. Empty hands; thrown stone is a separate runtime projectile, not baked into the pose.
View and pose: Straight front view, near orthographic, camera at chest height. Neutral anatomical A pose, arms straight down and out 30 degrees from the torso, open empty hands, fingers separated, legs straight and slightly apart, feet parallel, face forward. Both sides symmetrical and unobstructed.
Output: one PNG, 1024x1536.
```

## T04-B · Nham Viên · góc phụ

**File:** `games/immortality-cultivation/art-src/beasts/nham-vien-back.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/nham-vien.png`.

**3D:** face limit đề xuất 8000 · Tự rig Blender. Tỉ lệ tay dài của Viên và clip ném riêng; không phải người chuẩn. Clip: Idle, Move, Attack, Death (Move: bước nặng; Attack: ném).

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
Subject: One Nham Vien spirit macaque, upright height 1.6 m, a tall two-legged rocky macaque with a broad chest, long strong separate arms, five-fingered hands, short sturdy legs and a thick short tail clear of the legs. Limestone-grey fur sculpted into large rock-like clumps, charcoal forearms, warm ivory face with a calm but formidable closed muzzle. Flat dark ink markings over upper back. Empty hands; thrown stone is a separate runtime projectile, not baked into the pose.
View and pose: Straight rear view of the attached main image, near orthographic, camera at chest height. Preserve the exact identity, materials, proportions, garment construction and neutral A pose; change only the camera by 180 degrees. Arms down and out 30 degrees, hands and feet visible; do not look over the shoulder.
Reference: attach only games/immortality-cultivation/art-src/beasts/nham-vien.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## T05-S · Thiết Giáp Trư

**File:** `games/immortality-cultivation/art-src/beasts/thiet-giap-tru.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 8000 · Tự rig Blender. Bốn chân, húc và chiếm nhãn; chuyển trọng lượng phải đúng. Clip: Idle, Move, Attack, Death (Attack: húc; chuẩn bị và lao tách nhịp).

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
Subject: One Thiet Giap Tru spirit boar, shoulder height 1.1 m, length 1.9 m. Broad low heavy torso, massive sloped shoulders, wedge head, short upturned snout, two short thick ivory tusks, two small ears, four sturdy legs with separate cloven hooves, a short thick tail. Intact overlapping dark iron-grey broad armor-like hide plates across back and shoulders, limestone-grey flanks, charcoal broad ink marks. Dark eyes, closed mouth. No saddle, harness, extra horns or weapons.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Output: one PNG, 1536x1024.
```

## T05-F · Thiết Giáp Trư · góc phụ

**File:** `games/immortality-cultivation/art-src/beasts/thiet-giap-tru-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/thiet-giap-tru.png`.

**3D:** face limit đề xuất 8000 · Tự rig Blender. Bốn chân, húc và chiếm nhãn; chuyển trọng lượng phải đúng. Clip: Idle, Move, Attack, Death (Attack: húc; chuẩn bị và lao tách nhịp).

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
Subject: One Thiet Giap Tru spirit boar, shoulder height 1.1 m, length 1.9 m. Broad low heavy torso, massive sloped shoulders, wedge head, short upturned snout, two short thick ivory tusks, two small ears, four sturdy legs with separate cloven hooves, a short thick tail. Intact overlapping dark iron-grey broad armor-like hide plates across back and shoulders, limestone-grey flanks, charcoal broad ink marks. Dark eyes, closed mouth. No saddle, harness, extra horns or weapons.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/beasts/thiet-giap-tru.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## BT01-S · Đằng Thử · biến chủng Mộc

**File:** `games/immortality-cultivation/art-src/variants/dang-thu.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/thach-thu.png`.

**3D:** face limit đề xuất 4000 · Dùng rig Thạch Thử. Cùng GLB, đổi vật liệu Mộc, từ trận 4 theo D23. Clip: Idle, Move, Attack, Death. **Không tạo GLB mới.**

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
Subject: One Thach Thu spirit rat, shoulder height 0.35 m, body length 0.65 m. Low compact rounded body, blunt muzzle, small round ears, four short stout legs with broad feet, one thick tapering curved tail kept clear of the feet. Limestone-grey pebble-like fur masses on the back, charcoal undercoat, ivory muzzle; three broad ink-dark painted marks across the back. Dark eyes. Stone quality is stylized intact surface, not broken skin. Elemental material variant: the exact same rat anatomy and pebble-clump geometry. Paint existing back masses muted moss-green with one broad ivory leaf-shaped marking. No real leaves, vines, horns or geometry changes.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Reference: attach only games/immortality-cultivation/art-src/beasts/thach-thu.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1536x1024.
```

## BT01-F · Đằng Thử · biến chủng Mộc · góc phụ

**File:** `games/immortality-cultivation/art-src/variants/dang-thu-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/variants/dang-thu.png`.

**3D:** face limit đề xuất 4000 · Dùng rig Thạch Thử. Cùng GLB, đổi vật liệu Mộc, từ trận 4 theo D23. Clip: Idle, Move, Attack, Death.

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
Subject: One Thach Thu spirit rat, shoulder height 0.35 m, body length 0.65 m. Low compact rounded body, blunt muzzle, small round ears, four short stout legs with broad feet, one thick tapering curved tail kept clear of the feet. Limestone-grey pebble-like fur masses on the back, charcoal undercoat, ivory muzzle; three broad ink-dark painted marks across the back. Dark eyes. Stone quality is stylized intact surface, not broken skin. Elemental material variant: the exact same rat anatomy and pebble-clump geometry. Paint existing back masses muted moss-green with one broad ivory leaf-shaped marking. No real leaves, vines, horns or geometry changes.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/variants/dang-thu.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## BT02-F · Khê Viên · biến chủng Thủy (M1)

**File:** `games/immortality-cultivation/art-src/variants/khe-vien.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/nham-vien.png`.

**3D:** face limit đề xuất 8000 · Dùng rig Nham Viên. Cùng GLB, đổi vật liệu Thủy; M1 theo D23. Clip: Idle, Move, Attack, Death. **Không tạo GLB mới.**

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
Subject: One Nham Vien spirit macaque, upright height 1.6 m, a tall two-legged rocky macaque with a broad chest, long strong separate arms, five-fingered hands, short sturdy legs and a thick short tail clear of the legs. Limestone-grey fur sculpted into large rock-like clumps, charcoal forearms, warm ivory face with a calm but formidable closed muzzle. Flat dark ink markings over upper back. Empty hands; thrown stone is a separate runtime projectile, not baked into the pose. Elemental material variant: identical macaque geometry. Paint existing shoulder fur masses muted slate-blue with a single broad ivory droplet-shaped marking. No real water, fins, crystals or geometry changes.
View and pose: Straight front view, near orthographic, camera at chest height. Neutral anatomical A pose, arms straight down and out 30 degrees from the torso, open empty hands, fingers separated, legs straight and slightly apart, feet parallel, face forward. Both sides symmetrical and unobstructed.
Reference: attach only games/immortality-cultivation/art-src/beasts/nham-vien.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## BT02-B · Khê Viên · biến chủng Thủy (M1) · góc phụ

**File:** `games/immortality-cultivation/art-src/variants/khe-vien-back.png` · **Đính kèm:** `games/immortality-cultivation/art-src/variants/khe-vien.png`.

**3D:** face limit đề xuất 8000 · Dùng rig Nham Viên. Cùng GLB, đổi vật liệu Thủy; M1 theo D23. Clip: Idle, Move, Attack, Death.

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
Subject: One Nham Vien spirit macaque, upright height 1.6 m, a tall two-legged rocky macaque with a broad chest, long strong separate arms, five-fingered hands, short sturdy legs and a thick short tail clear of the legs. Limestone-grey fur sculpted into large rock-like clumps, charcoal forearms, warm ivory face with a calm but formidable closed muzzle. Flat dark ink markings over upper back. Empty hands; thrown stone is a separate runtime projectile, not baked into the pose. Elemental material variant: identical macaque geometry. Paint existing shoulder fur masses muted slate-blue with a single broad ivory droplet-shaped marking. No real water, fins, crystals or geometry changes.
View and pose: Straight rear view of the attached main image, near orthographic, camera at chest height. Preserve the exact identity, materials, proportions, garment construction and neutral A pose; change only the camera by 180 degrees. Arms down and out 30 degrees, hands and feet visible; do not look over the shoulder.
Reference: attach only games/immortality-cultivation/art-src/variants/khe-vien.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

