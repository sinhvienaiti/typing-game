# Tu Tiên Thủ Ải — M0b · 06. Trận pháp, cơ quan và cảnh (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

P01–P05 là năm prop lớn ở canon §21.3. CQ01–CQ04 lấy tên và chức năng từ §8.3; bổ sung bốn nguồn 3D ngoài ước tính 14 GLB để không bỏ cơ quan. Thiết kế thân cơ quan tĩnh, hiệu ứng sét/lưới/sương và nứt Trận Trụ do shader/runtime; không có cơ cấu có khớp nên không rig. Cổng ải là cảnh, không thêm máu nhà/cổng (§8.1). Mê Vụ Trận ở M1. Mỗi vật dùng một ảnh 3/4; chọn Image to 3D, không giả điền góc thiếu.

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
| 29 | P01 | `props/tran-tam.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 30 | P02 | `props/tran-tru.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 31 | P03 | `props/cong-ai.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 32 | P04 | `props/da-voi.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 33 | P05 | `props/tung-co.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 34 | CQ01 | `mechanisms/kiem-thung.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 35 | CQ02 | `mechanisms/loi-phu-tru.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 36 | CQ03 | `mechanisms/phong-an-vong.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |
| 37 | CQ04 | `mechanisms/me-vu-tran.png` | 1024×1024 | — | Đã tạo · chờ duyệt/nền |

## P01 · Trận Tâm

**File:** `games/immortality-cultivation/art-src/props/tran-tam.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 10000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One low circular limestone formation core, diameter 4 m, height 0.65 m, a sturdy three-tier round stone dais with a single solid faceted ivory stone heart set into its center. Broad concentric shallow carved channels and three radial geometric insets imply the formation eyes without writing. Charcoal inset bands, muted moss-grey stone edges. The core is a functional low stone object, not a floating orb, throne, temple, tower or tall statue.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## P02 · Trận Trụ

**File:** `games/immortality-cultivation/art-src/props/tran-tru.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 8000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One tall solid limestone cover pillar, height 3.6 m, width 1.2 m, a rough broad square monolith with a stable wider integrated stone foot, gently tapered top, two broad horizontal structural seams and one shallow ivory geometric diamond inset. Intact surfaces, sparse muted moss in broad patches. One pillar only; later the game duplicates it twice. No carved text, roof, gate, weapon or detached rubble.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## P03 · Cổng ải

**File:** `games/immortality-cultivation/art-src/props/cong-ai.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 10000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One modest Vietnamese mountain-frontier gateway, 5 m wide and 4 m high, two heavy limestone supports joined by one thick lintel and a compact single dark tiled roof with restrained gently curved ends, old charcoal timber doorposts, a fully open central passage. Quiet indigo-grey weathering and simple geometric woven trim. No surrounding buildings, stairs, terrain, closed door, flags, lanterns, lettering or religious iconography. This is scenic architecture, not an independently damageable defense.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## P04 · Đá vôi

**File:** `games/immortality-cultivation/art-src/props/da-voi.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 6000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One vertical karst limestone boulder, 3 m high and 1.8 m wide, broad tapering silhouette, deep but solid vertical erosion folds, matte ivory-grey stone, charcoal ink-like streaks and two broad muted moss patches. Stable natural stone bottom. No caves through the rock, loose pebbles, plants, ground or detached parts.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## P05 · Tùng cổ

**File:** `games/immortality-cultivation/art-src/props/tung-co.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 10000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One old mountain pine tree, 5 m high with a broad asymmetric 4 m canopy, a thick curved charcoal-grey trunk, three sturdy connected branching limbs and four broad opaque clustered masses of dusty indigo-moss needles. Exposed thick roots belong to the tree's own base. Sculptural Vietnamese karst-landscape pine silhouette. Foliage is solid mass with broad painted needle texture, no individual thin needles, grass, stones, ground or pot.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## CQ01 · Kiếm Thung

**File:** `games/immortality-cultivation/art-src/mechanisms/kiem-thung.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 6000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One ground mechanism occupying a 4 by 2 m rectangular strip: a single low dark limestone slab with five thick short ivory-grey sword-shaped stone stakes attached along two staggered rows. Stakes tilt slightly toward the same incoming direction, broad closed solid blades with safe blunt tips. Shallow indigo inset channels connect their bases. Whole mechanism is one coherent static assembly; no moving joint, raised swords, glow, effects or scattered parts.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## CQ02 · Lôi Phù Trụ

**File:** `games/immortality-cultivation/art-src/mechanisms/loi-phu-tru.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 6000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One static lightning-talisman mechanism, 1.8 m high: a thick charcoal limestone hexagonal pillar on a broad low integral foot, capped by a solid ivory faceted stone, with three wide geometric zigzag grooves painted muted indigo and an inset rigid ivory plaque. The zigzag is abstract geometry rather than writing. No paper strips, hanging cloth, wires, electricity, arcs, glow or floating elements.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## CQ03 · Phong Ấn Võng

**File:** `games/immortality-cultivation/art-src/mechanisms/phong-an-vong.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 6000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One static binding-net mechanism, 1.6 m high: a thick limestone post on an integral broad square foot, carrying a closed vertical circular charcoal stone ring firmly attached to the post. Inside the ring a thick solid ivory lattice disk has broad intersecting rhombus grooves, all one opaque connected surface rather than thin strings. Muted indigo geometric insets. Binding tendrils are runtime effects; show only the inert mechanism with no tendrils, net projectile or moving parts.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## CQ04 · Mê Vụ Trận

**File:** `games/immortality-cultivation/art-src/mechanisms/me-vu-tran.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 5000 · Không rig. Đồ tĩnh; hiệu ứng và di chuyển cả vật do runtime, không có khớp. Clip: —.

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
Subject: One static mist-formation mechanism, a low broad limestone vessel 1 m across and 0.8 m high, stable three-lobed integrated foot, a thick closed ivory lid with a broad spiral-shaped indigo inset groove and three solid charcoal side handles connected directly to the body. Simple geometric craft, not a religious incense burner. This is the inert source prop only; emitted mist is a runtime effect. No smoke, vapor, incense sticks, flames, glow or loose lid.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

