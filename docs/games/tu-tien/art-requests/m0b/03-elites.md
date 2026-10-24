# Tu Tiên Thủ Ải — M0b · 03. Ba thuộc tính tinh anh (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

Canon §10.3: một thuộc tính mỗi tinh anh, cỡ ×1,25; Cuồng, Thiết Bì, Hồi Nguyên. Các ảnh là mẫu chất liệu trên lưới thường, không đặt Tripo tạo model mới, không thêm bộ phận. Chọn Phong Lang cho Cuồng/Hồi Nguyên và Thiết Giáp Trư cho Thiết Bì là đề xuất mỹ thuật, không khóa thuộc tính vào loài. Hào quang, Ấn và hồi phục thuộc runtime; ảnh nguồn không vẽ.

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
| 23 | TA01-S | `elites/phong-lang-cuong.png` | 1536×1024 | `beasts/phong-lang.png` | Đã tạo · chờ duyệt/nền |
| 24 | TA01-F | `elites/phong-lang-cuong-front.png` | 1024×1024 | `elites/phong-lang-cuong.png` | Đã tạo · chờ duyệt/nền |
| 25 | TA02-S | `elites/thiet-giap-tru-thiet-bi.png` | 1536×1024 | `beasts/thiet-giap-tru.png` | Đã tạo · chờ duyệt/nền |
| 26 | TA02-F | `elites/thiet-giap-tru-thiet-bi-front.png` | 1024×1024 | `elites/thiet-giap-tru-thiet-bi.png` | Đã tạo · chờ duyệt/nền |
| 27 | TA03-S | `elites/phong-lang-hoi-nguyen.png` | 1536×1024 | `beasts/phong-lang.png` | Đã tạo · chờ duyệt/nền |
| 28 | TA03-F | `elites/phong-lang-hoi-nguyen-front.png` | 1024×1024 | `elites/phong-lang-hoi-nguyen.png` | Đã tạo · chờ duyệt/nền |

## TA01-S · Tinh anh · Phong Lang Cuồng

**File:** `games/immortality-cultivation/art-src/elites/phong-lang-cuong.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/phong-lang.png`.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang. Cuồng là thuộc tính; cùng GLB, chỉ đổi chất liệu và cỡ ×1,25. Clip: Idle, Move, Attack, Death. **Không tạo GLB mới.**

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Elite Cuong material study: preserve identical Phong Lang geometry; use broad pale slate diagonal painted markings on the shoulders to distinguish speed, with no extra forms. Runtime scale is 1.25 times. Auras and status symbols are added in the game only.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Reference: attach only games/immortality-cultivation/art-src/beasts/phong-lang.png; use it as the exact unchanged mesh design, changing only painted material markings.
Output: one PNG, 1536x1024.
```

## TA01-F · Tinh anh · Phong Lang Cuồng · góc phụ

**File:** `games/immortality-cultivation/art-src/elites/phong-lang-cuong-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/elites/phong-lang-cuong.png`.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang. Cuồng là thuộc tính; cùng GLB, chỉ đổi chất liệu và cỡ ×1,25. Clip: Idle, Move, Attack, Death.

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Elite Cuong material study: preserve identical Phong Lang geometry; use broad pale slate diagonal painted markings on the shoulders to distinguish speed, with no extra forms. Runtime scale is 1.25 times. Auras and status symbols are added in the game only.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/elites/phong-lang-cuong.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## TA02-S · Tinh anh · Thiết Giáp Trư Thiết Bì

**File:** `games/immortality-cultivation/art-src/elites/thiet-giap-tru-thiet-bi.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/thiet-giap-tru.png`.

**3D:** face limit đề xuất 8000 · Dùng rig Thiết Giáp Trư. Thiết Bì là chất liệu trên lưới gốc; không thêm giáp hình học. Clip: Idle, Move, Attack, Death. **Không tạo GLB mới.**

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
Subject: One Thiet Giap Tru spirit boar, shoulder height 1.1 m, length 1.9 m. Broad low heavy torso, massive sloped shoulders, wedge head, short upturned snout, two short thick ivory tusks, two small ears, four sturdy legs with separate cloven hooves, a short thick tail. Intact overlapping dark iron-grey broad armor-like hide plates across back and shoulders, limestone-grey flanks, charcoal broad ink marks. Dark eyes, closed mouth. No saddle, harness, extra horns or weapons. Elite Thiet Bi material study: identical boar plate thickness, plate count and body geometry; existing plates painted pale iron-grey with broad charcoal rectangular edge bands. No added armor layers. Runtime scale is 1.25 times; no aura in this source plate.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Reference: attach only games/immortality-cultivation/art-src/beasts/thiet-giap-tru.png; use it as the exact unchanged mesh design, changing only painted material markings.
Output: one PNG, 1536x1024.
```

## TA02-F · Tinh anh · Thiết Giáp Trư Thiết Bì · góc phụ

**File:** `games/immortality-cultivation/art-src/elites/thiet-giap-tru-thiet-bi-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/elites/thiet-giap-tru-thiet-bi.png`.

**3D:** face limit đề xuất 8000 · Dùng rig Thiết Giáp Trư. Thiết Bì là chất liệu trên lưới gốc; không thêm giáp hình học. Clip: Idle, Move, Attack, Death.

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
Subject: One Thiet Giap Tru spirit boar, shoulder height 1.1 m, length 1.9 m. Broad low heavy torso, massive sloped shoulders, wedge head, short upturned snout, two short thick ivory tusks, two small ears, four sturdy legs with separate cloven hooves, a short thick tail. Intact overlapping dark iron-grey broad armor-like hide plates across back and shoulders, limestone-grey flanks, charcoal broad ink marks. Dark eyes, closed mouth. No saddle, harness, extra horns or weapons. Elite Thiet Bi material study: identical boar plate thickness, plate count and body geometry; existing plates painted pale iron-grey with broad charcoal rectangular edge bands. No added armor layers. Runtime scale is 1.25 times; no aura in this source plate.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/elites/thiet-giap-tru-thiet-bi.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## TA03-S · Tinh anh · Phong Lang Hồi Nguyên

**File:** `games/immortality-cultivation/art-src/elites/phong-lang-hoi-nguyen.png` · **Đính kèm:** `games/immortality-cultivation/art-src/beasts/phong-lang.png`.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang. Hồi Nguyên là thuộc tính; giữ GLB và rig gốc. Clip: Idle, Move, Attack, Death. **Không tạo GLB mới.**

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Elite Hoi Nguyen material study: identical wolf geometry; muted moss-grey shoulder planes with a broad ivory oval painted marking on each flank. Runtime scale is 1.25 times. Regeneration and aura are runtime effects, absent here; no leaves, vines or new forms.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Reference: attach only games/immortality-cultivation/art-src/beasts/phong-lang.png; use it as the exact unchanged mesh design, changing only painted material markings.
Output: one PNG, 1536x1024.
```

## TA03-F · Tinh anh · Phong Lang Hồi Nguyên · góc phụ

**File:** `games/immortality-cultivation/art-src/elites/phong-lang-hoi-nguyen-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/elites/phong-lang-hoi-nguyen.png`.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang. Hồi Nguyên là thuộc tính; giữ GLB và rig gốc. Clip: Idle, Move, Attack, Death.

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Elite Hoi Nguyen material study: identical wolf geometry; muted moss-grey shoulder planes with a broad ivory oval painted marking on each flank. Runtime scale is 1.25 times. Regeneration and aura are runtime effects, absent here; no leaves, vines or new forms.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/elites/phong-lang-hoi-nguyen.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

