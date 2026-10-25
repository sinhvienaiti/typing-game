# Tu Tiên Thủ Ải — M0b · 01. Người chơi và bot đạo đồng (25/10/2026)

> **Phiếu 007; NV01 sửa bằng Phiếu 008 theo D47.** Dành cho chủ dự án duyệt ảnh và dựng Tripo; theo [canon](../../00-canon.md) §0, §2, §8–12, §14.5, §20–21. [Thứ tự, thiết lập, rig và face limit](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

Kiếm tu là nhân vật chữ ký, tự rig Blender. Theo D47, nữ Kiếm tu chính trẻ, đẹp thanh tú, đứng thẳng, quý phái và mang khí chất hoàng tộc. Bộ mới dùng lụa nhiều lớp trắng ngọc–lam sẫm, viền thêu vàng nhạt, mây và hạc, miện nhỏ bằng ngọc, ngọc bội. Trang phục kín đáo, hợp mọi lứa tuổi; chất sơn thủy huyền ảo Việt giữ ở hình khối và chất liệu, **không thêm cảnh hoặc hiệu ứng vào nguồn Tripo**. Kiếm Thanh Phong vương giả hiện ở chân dung; khi dựng 3D vẫn là vật thể riêng, hai tay NV01 để trống.

Tạm chọn [chân dung A](00-identity.md#bs02-a--chân-dung-kiếm-tu--miện-nhỏ) cho cặp trước/sau; anh vẫn cần chọn giữa A và bản trâm hạc B. Ảnh sau đính kèm cả ảnh trước làm chuẩn hình khối và chân dung A làm chuẩn thiết kế. Mỗi ảnh NV01 tối đa hai lượt của Phiếu 008; trần 40 là lịch sử Phiếu 007. Bản cũ giữ `.v1.png` và `.v1.prompt.txt`; bản thử không chọn giữ `-rejected-1`.

Thổ thể tu là người hai chân chuẩn: Tripo Biped một lần 20 credit, Blender thêm chiêu còn thiếu. Bot dùng GLB trường phái còn lại và đổi màu áo (canon §21.2); BOT01 là bảng chất liệu của Thổ thể cho đội có người chơi Kiếm, không tạo model hoặc rig riêng. Khi người chơi Thổ thể, bot dùng lại Kiếm tu và đổi bảng màu tương ứng. «Đạo đồng» là vai bot, không ép hình trẻ em. Phần NV02/BOT01 dưới đây giữ theo Phiếu 007; không mở rộng danh sách nhân vật trong Phiếu 008.

```text
Instructions for the image tool (Codex image_gen or ChatGPT)
- Use exactly one complete prompt block below per image, verbatim.
- Keep one view per image; never make a contact sheet or multiview collage.
- Attach the images named for that block, preserving their stated roles.
- A secondary view must preserve the main image and change only the camera.
- Save one PNG and the exact prompt beside it as <name>.prompt.txt.
- NV01 belongs to ticket 008: at most two attempts per image, including the first.
- The original 40-image cap applies to the completed ticket 007 only.
```

| Thứ tự | Mã | File | Khổ yêu cầu | Đính kèm | Lượt |
|---:|---|---|---|---|---|
| 3 | NV01-F | `cultivators/kiem-tu.png` | 1024×1536 | Chân dung A + `cultivators/kiem-tu-rejected-1.png` cho lượt sửa | 2/2 · chờ duyệt/nền |
| 4 | NV01-B | `cultivators/kiem-tu-back.png` | 1024×1536 | `cultivators/kiem-tu.png` + chân dung A | 2/2 · giữ lượt 1; lượt 2 nền lệch hơn |
| 19 | NV02-F | `cultivators/tho-the-tu.png` | 1024×1536 | — | Phiếu 007 · chờ duyệt/nền |
| 20 | NV02-B | `cultivators/tho-the-tu-back.png` | 1024×1536 | `cultivators/tho-the-tu.png` | Phiếu 007 · chờ duyệt/nền |
| 21 | BOT01-F | `bots/bot-dao-dong-tho.png` | 1024×1536 | `cultivators/tho-the-tu.png` | Phiếu 007 · chờ duyệt/nền |
| 22 | BOT01-B | `bots/bot-dao-dong-tho-back.png` | 1024×1536 | `bots/bot-dao-dong-tho.png` | Phiếu 007 · chờ duyệt/nền |

## NV01-F · Kiếm tu · bản hoàng tộc D47

**File:** `games/immortality-cultivation/art-src/cultivators/kiem-tu.png`.
**Đính kèm theo thứ tự:** `identity/kiem-tu-portrait.png` (thiết kế được chọn tạm), `cultivators/kiem-tu-rejected-1.png` (bản thử trước để sửa khung, tư thế và nền).

**3D:** face limit đề xuất 20000 · Tự rig Blender. Nhân vật chữ ký; dáng đi bộ, áo xẻ và động tác Kiếm riêng. Clip: Idle, Run, Cast_Short, Cast_Heavy, Dash, Hit, Down, Victory. Yêu cầu nguồn: tư thế A, gần trực giao, nền `#E6E6E6`, không hiệu ứng; xem số đo nền và giới hạn thực ở README giao nhận.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape aesthetic translated into a sculptural hand-painted 3D maquette, broad elegant silk masses, restrained ink-wash value steps, readable from an elevated game camera. Material colour contains subtle do-paper character; the background is completely flat.
Subject: one beautiful young adult Vietnamese woman sword cultivator, about 24, 1.70 metres tall, delicate refined facial features, dark eyes, composed royal bearing, upright straight spine and natural adult proportions around seven and a half heads tall. Smooth black hair in a compact tidy updo, topped by a small pale antique-gold and white-jade royal diadem.
Costume: pearl-white layered silk robes inspired by Vietnamese ao ngu than, fully closed high inner collar and long fitted inner sleeves, deep-indigo outer shoulder and side panels, a wide deep-indigo silk belt, fine pale antique-gold embroidered borders and readable large royal cloud-and-crane motifs. One compact opaque white-jade waist pendant supported close to the belt. Split outer silk panels end at mid-calf over fully covering deep-indigo trousers and separate neat indigo boots. Neat narrow outer sleeves taper closely at the forearms and leave the hands and gaps beneath the arms unobstructed. Royal elegance with practical walkable construction; no train or loose trailing fabric.
Build: preserve the selected portrait design, consolidate crown, hair, embroidery and jade into sturdy reconstruction-friendly forms, with compact crown ornaments and no fine dangling hair tassels; embroidery is flat material detail, not floating geometry. Opaque layered clothing covers chest, shoulders and legs; dignified all-ages presentation.
Framing: exactly one complete character centred, full crown to boot soles and every fingertip visible, at least 10 percent empty margin at top AND bottom as well as both sides. The complete character, including crown and boots, occupies at most 80 percent of the total canvas height. One view only.
Background: perfectly uniform solid light grey #E6E6E6 across every background pixel, including corners and around the feet; no gradient, vignette, texture, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle local form shading only, no rim light, bloom, specular glare or baked directional shadow.
Equipment: empty open hands; no sword or scabbard attached to the body. The royal Thanh Phong sword remains a separate asset for reconstruction.
Colour rules: pearl white, deep indigo, ink charcoal, opaque white jade and restrained PALE ANTIQUE GOLD embroidery. The embroidery is matte ornament, distinct from runtime reward gold #FFC83A. Enemy red #FF4A4A, urgent orange #FFB020, typing turquoise #7FF5E0 and UI vermilion remain absent.
Constraints: one original fully clothed adult, no text, letters, numbers, logos, watermark, frame, blood or horror. No smoke, mist, fire, sparks, particles, aura, trails, emissive light, floating ornament or other effects. No sexualized proportions, cleavage, exposed midriff or bare legs.
View and pose: straight FRONT view, near orthographic, camera at chest height. Anatomical neutral A pose: straight arms visibly angle exactly 30 degrees away from the vertical torso downward, so the empty hands sit well away from the hips with a wide unobstructed grey gap under each arm, palms inward, empty relaxed hands with readable separated fingers, legs straight and slightly apart, feet parallel. Face, torso, shoulders and hips point straight forward; both sides symmetrical and unobstructed.
Input image 1: games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png is the selected royal design reference, option A. Preserve her face, crown, hair, layered costume, cloud-and-crane embroidery and palette; replace portrait framing and scenery with this full-body A pose and flat grey background.
Output: one portrait PNG, 1024x1536.
Input image 2: games/immortality-cultivation/art-src/cultivators/kiem-tu-rejected-1.png is the previous front attempt. Keep her beautiful face and royal design; correct its tight framing, too-closed arm angle and off-grey background. Reframe with the COMPLETE figure in the middle 80 percent of canvas height, widen the arms to the specified A pose, simplify the dangling crown tassels, and replace every background pixel with a single flat digital colour #E6E6E6 (RGB 230,230,230). The background must read as a solid colour card, not a photographed studio backdrop. Keep local shading ONLY inside the character silhouette.
```

## NV01-B · Kiếm tu · góc sau cùng thiết kế

**File:** `games/immortality-cultivation/art-src/cultivators/kiem-tu-back.png`.
**Đính kèm theo thứ tự:** `cultivators/kiem-tu.png` (chuẩn hình khối, tỷ lệ và tư thế), `identity/kiem-tu-portrait.png` (chuẩn phục sức hoàng tộc). Giữ ảnh lượt 1; lượt 2 chỉ sửa nền nhưng số đo kém hơn, lưu `kiem-tu-back-rejected-2.png` và prompt nguyên văn.

**3D:** face limit đề xuất 20000 · Tự rig Blender. Cùng model và bộ clip NV01-F; chỉ đổi camera 180°. Ngọc bội trước bụng khuất tự nhiên ở góc lưng, không tự sinh thêm ngọc sau lưng.

```text
Use case: stylized-concept.
Asset type: one image-to-3D source plate for the original Vietnamese fantasy defense game Tu Tien Thu Ai.
House style: original Vietnamese fantastical landscape aesthetic translated into a sculptural hand-painted 3D maquette, broad elegant silk masses, restrained ink-wash value steps, readable from an elevated game camera. Material colour contains subtle do-paper character; the background is completely flat.
Subject: one beautiful young adult Vietnamese woman sword cultivator, about 24, 1.70 metres tall, delicate refined facial features, dark eyes, composed royal bearing, upright straight spine and natural adult proportions around seven and a half heads tall. Smooth black hair in a compact tidy updo, topped by a small pale antique-gold and white-jade royal diadem.
Costume: pearl-white layered silk robes inspired by Vietnamese ao ngu than, fully closed high inner collar and long fitted inner sleeves, deep-indigo outer shoulder and side panels, a wide deep-indigo silk belt, fine pale antique-gold embroidered borders and readable large royal cloud-and-crane motifs. One compact opaque white-jade waist pendant supported close to the belt. Split outer silk panels end at mid-calf over fully covering deep-indigo trousers and separate neat indigo boots. Neat narrow outer sleeves taper closely at the forearms and leave the hands and gaps beneath the arms unobstructed. Royal elegance with practical walkable construction; no train or loose trailing fabric.
Build: preserve the selected portrait design, consolidate crown, hair, embroidery and jade into sturdy reconstruction-friendly forms, with compact crown ornaments and no fine dangling hair tassels; embroidery is flat material detail, not floating geometry. Opaque layered clothing covers chest, shoulders and legs; dignified all-ages presentation.
Framing: exactly one complete character centred, full crown to boot soles and every fingertip visible, 10 percent empty margin, one view only.
Background: perfectly uniform solid light grey #E6E6E6 across every background pixel, including corners and around the feet; no gradient, vignette, texture, scenery, floor, cast shadow or contact shadow.
Lighting: flat even neutral studio illumination; subtle local form shading only, no rim light, bloom, specular glare or baked directional shadow.
Equipment: empty open hands; no sword or scabbard attached to the body. The royal Thanh Phong sword remains a separate asset for reconstruction.
Colour rules: pearl white, deep indigo, ink charcoal, opaque white jade and restrained PALE ANTIQUE GOLD embroidery. The embroidery is matte ornament, distinct from runtime reward gold #FFC83A. Enemy red #FF4A4A, urgent orange #FFB020, typing turquoise #7FF5E0 and UI vermilion remain absent.
Constraints: one original fully clothed adult, no text, letters, numbers, logos, watermark, frame, blood or horror. No smoke, mist, fire, sparks, particles, aura, trails, emissive light, floating ornament or other effects. No sexualized proportions, cleavage, exposed midriff or bare legs.
View and pose: straight REAR view, near orthographic, camera at chest height. Preserve the exact body, garment construction, diadem, updo, belt, embroidery scale, trousers, boots and neutral A pose from input image 1; rotate ONLY the camera by 180 degrees. Straight arms angle 30 degrees away from the torso downward; hands and feet fully visible, legs slightly apart. Back of head faces viewer, no looking over shoulder. The front waist pendant is naturally hidden behind the body. Keep the same length and width of every garment panel; back embroidery follows the same cloud-and-crane visual language.
Input image 1: games/immortality-cultivation/art-src/cultivators/kiem-tu.png is the MAIN geometry, proportion and A-pose authority.
Input image 2: games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png is the selected option A royal costume design reference. Preserve this identity; use image 1 to resolve the full-body construction. These are references for one single rear-view character, not a collage.
Output: one portrait PNG, 1024x1536.
Strict flat-background requirement: use a single solid digital colour card RGB(230,230,230), hexadecimal #E6E6E6, outside the character silhouette everywhere. No photographed studio backdrop or near-grey approximation. Match the selected front image character size and A pose while leaving generous empty space around the complete crown and soles.
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

