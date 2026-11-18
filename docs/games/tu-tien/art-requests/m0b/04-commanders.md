# Tu Tiên Thủ Ải — M0b · 04. Thú tướng Lang Đầu Đàn (25/10/2026)

> **Phiếu 007.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

Lang Đầu Đàn có Tru Đàn và hào quang 6 m, giữ cùng GLB Phong Lang theo canon §21.2. Hai ảnh TG01 là mẫu tỷ lệ/chất liệu để duyệt thứ bậc; khi tạo GLB chỉ gửi T02. Vì thứ tự phiếu yêu cầu tướng trước năm họ, T02 dùng TG01-S làm tham chiếu hình học rồi bỏ dấu vai cấp tướng. Không tạo thêm model tướng, không trả rig thêm.

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
| 7 | TG01-S | `commanders/lang-dau-dan.png` | 1536×1024 | — | Đã tạo · chờ duyệt/nền |
| 8 | TG01-F | `commanders/lang-dau-dan-front.png` | 1024×1024 | `commanders/lang-dau-dan.png` | Đã tạo · chờ duyệt/nền |

## TG01-S · Lang Đầu Đàn

**File:** `games/immortality-cultivation/art-src/commanders/lang-dau-dan.png` · **Đính kèm:** không.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang trong Blender. Chung GLB Phong Lang theo canon §21.2; thêm clip Tru Đàn, không dựng model mới. Clip: Idle, Move, Attack, Death, Howl_Summon, Hit, Intro, Stagger. **Không tạo GLB mới.**

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Commander material study: the same anatomy as Phong Lang at a larger runtime scale; an ivory-grey broad painted shoulder chevron identifies rank. No added geometry. Aura is runtime only.
View and pose: Exact left-side view, head pointing to the left edge, camera at body height, near orthographic. Neutral standing pose, head level, eyes open and mouth closed. Four straight legs in slightly staggered neutral positions so each paw is visible, tail held clear of legs. Do not rotate toward the viewer.
Output: one PNG, 1536x1024.
```

## TG01-F · Lang Đầu Đàn · góc phụ

**File:** `games/immortality-cultivation/art-src/commanders/lang-dau-dan-front.png` · **Đính kèm:** `games/immortality-cultivation/art-src/commanders/lang-dau-dan.png`.

**3D:** face limit đề xuất 6000 · Dùng rig Phong Lang trong Blender. Chung GLB Phong Lang theo canon §21.2; thêm clip Tru Đàn, không dựng model mới. Clip: Idle, Move, Attack, Death, Howl_Summon, Hit, Intro, Stagger.

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
Subject: One Phong Lang spirit wolf, shoulder height 0.9 m, length 1.6 m excluding tail. Low long lean body, deep chest, wedge muzzle, two erect ears, four clear muscular legs, thick paws, one bushy tail. Smoky indigo-grey fur in a few solid clumps, warm ivory throat and muzzle, charcoal broad brush-like markings along the shoulders and spine; quiet dark eyes. No armor, horns, antlers, spikes, jewelry or extra limbs. Commander material study: the same anatomy as Phong Lang at a larger runtime scale; an ivory-grey broad painted shoulder chevron identifies rank. No added geometry. Aura is runtime only.
View and pose: EXACT ORTHOGRAPHIC FRONT ELEVATION of the attached animal. Camera yaw is ZERO degrees: nose, sternum, spine and pelvis lie on the image vertical centerline. Left and right shoulders have identical apparent size; hips centered directly behind the chest, no flank or side of the torso visible. Front paws symmetric. Rear paws may be partly occluded behind the front legs. Tail stays directly behind the torso and is hidden, never swung sideways. Head faces straight at the viewer, mouth closed. Preserve the same anatomy, armor plates, colors, scale and neutral standing pose. Rotate the entire animal to the front, not just its head.
Reference: attach only games/immortality-cultivation/art-src/commanders/lang-dau-dan.png; use it as the sole design authority; preserve the same subject and change only the requested view.
Output: one PNG, 1024x1024.
```

## Kiểm trước khi gửi Tripo

- Đúng tên, số chân/cánh và tỷ lệ; không cắt mất tay, tai, chân, cánh hoặc đuôi.
- Ảnh phụ khớp ảnh chính về khối, mảng màu và tư thế. Không dùng hai góc lệch thiết kế.
- Nền nguồn phẳng `#E6E6E6`, không bóng tiếp đất, chữ hoặc hiệu ứng. Prompt không thay cho kiểm ảnh.
- Hỏng rõ: tối đa **một lần tạo lại**, vẫn tính vào trần 40 ảnh. Ghi lỗi và prompt bản loại; dừng ảnh ưu tiên thấp khi hết lượt.
- Ảnh chưa chứng minh topology, rig, chuyển động hoặc HN0/HN1 đã đạt. Hai ảnh bản sắc được đánh giá theo phong cách, không dùng trực tiếp tái dựng.

