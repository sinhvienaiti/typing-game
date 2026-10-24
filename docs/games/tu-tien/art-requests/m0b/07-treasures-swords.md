# Tu Tiên Thủ Ải — M0b · 07. Pháp bảo và phi kiếm của Thiên Hà Kiếm Vũ (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

PB01 là một mesh phi kiếm dùng cho Phi Kiếm, Ngự Kiếm Quyết và Thiên Hà Kiếm Vũ, đồng thời là hình Thanh Phong Kiếm (§14.5). Không dựng 500 kiếm riêng. Face limit 4.000 là nguồn tạo, Blender giảm còn 300–800 tam giác (§21.3). «Vạn kiếm» là mô tả hình của Thiên Hà Kiếm Vũ, không đổi tên canon. PB02 Hậu Thổ Ấn lấy từ §14.5; không chữ triện trên mặt ấn.

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
| 38 | PB01-F | `treasures/thanh-phong-kiem.png` | 1024×1536 | — | Đã tạo · chờ duyệt/nền |
| 39 | PB01-S | `treasures/thanh-phong-kiem-side.png` | 1024×1536 | `treasures/thanh-phong-kiem.png` | Chưa tạo · trần 40 |
| 40 | PB02 | `treasures/hau-tho-an.png` | 1024×1024 | — | Chưa tạo · trần 40 |

## PB01-F · Thanh Phong Kiếm · phi kiếm

**File:** `games/immortality-cultivation/art-src/treasures/thanh-phong-kiem.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 4000 · Không rig. Đạn và pháp bảo gắn cứng; bay bằng runtime, 150/300/500 bản dùng chung mesh. Clip: —.

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
Subject: One Thanh Phong Kiem flying sword, 1.1 m long, one straight thick double-edged blade with a broad warm-ivory central plane and muted iron-grey edges, small indigo central groove, compact charcoal crossguard resembling two folded rice leaves, short wrapped indigo grip and solid ivory round pommel. Broad clean original silhouette readable when reduced to 300–800 triangles; no tassel, scabbard, gem, writing, ornament wires or effects. This one physical sword is instanced for Phi Kiem, Ngu Kiem Quyet and Thien Ha Kiem Vu, never draw a swarm here.
View and pose: Front orthographic view of the sword's broad blade face, vertical with point upward and grip below. Entire blade, guard and pommel visible.
Output: one PNG, 1024x1536.
```

## PB01-S · Thanh Phong Kiếm · nhìn cạnh

**File:** `games/immortality-cultivation/art-src/treasures/thanh-phong-kiem-side.png` · **Đính kèm:** `games/immortality-cultivation/art-src/treasures/thanh-phong-kiem.png`.

**3D:** face limit đề xuất 4000 · Không rig. Góc phụ đo độ dày; cùng GLB phi kiếm. Clip: —.

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
Subject: One Thanh Phong Kiem flying sword, 1.1 m long, one straight thick double-edged blade with a broad warm-ivory central plane and muted iron-grey edges, small indigo central groove, compact charcoal crossguard resembling two folded rice leaves, short wrapped indigo grip and solid ivory round pommel. Broad clean original silhouette readable when reduced to 300–800 triangles; no tassel, scabbard, gem, writing, ornament wires or effects. This one physical sword is instanced for Phi Kiem, Ngu Kiem Quyet and Thien Ha Kiem Vu, never draw a swarm here.
View and pose: Exact left edge orthographic view of the attached front image, point upward. Change camera by exactly 90 degrees around the vertical sword axis; preserve blade thickness, guard and grip. Show the physically thick narrow edge, not the broad face.
Reference: attach only games/immortality-cultivation/art-src/treasures/thanh-phong-kiem.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1536.
```

## PB02 · Hậu Thổ Ấn

**File:** `games/immortality-cultivation/art-src/treasures/hau-tho-an.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 4000 · Không rig. Pháp bảo tĩnh; gắn socket hoặc chuyển động cả vật. Clip: —.

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
Subject: One Hau Tho An earth-cultivator spiritual seal, 0.35 m wide: a broad square limestone-grey block with a low solid stepped mountain-shaped ivory handle fused onto the top, charcoal recessed border and a simple shallow square geometric inset on the front. Matte muted earth-grey materials, intact rounded edges. Blank underside, geometric planes only, no writing, religious symbol, stamp impression, pedestal, cloth or effects.
View and pose: Elevated three-quarter view, near orthographic, camera about 25 degrees above the subject, showing the front, left side and top. One standalone complete solid object; no plinth beyond the object's own functional base.
Output: one PNG, 1024x1024.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

