# Tu Tiên Thủ Ải — M0b · 00. Ảnh bản sắc sửa theo chủ dự án (25/10/2026)

> **Phiếu 008**, thay hai ảnh bản sắc lượt 1 của Phiếu 007; theo [canon](../../00-canon.md) **D47, D48, §8.1**. [Thiết lập Tripo và danh mục lượt đầu](README.md). Đường dẫn ảnh trong bảng tính từ `games/immortality-cultivation/art-src/`.

D47: nữ kiếm tu trẻ, đẹp thanh tú, đứng thẳng, cốt cách hoàng tộc; lụa trắng ngọc và lam sẫm, viền vàng nhạt, mây–hạc, miện nhỏ hoặc trâm ngọc, ngọc bội. Kiếm Thanh Phong mang phẩm chất vương giả. Trang phục kín đáo, hợp mọi lứa tuổi; giữ chất sơn thủy huyền ảo chất Việt.

D48: ảnh cảnh dùng camera game nghiêng 50–55°, FOV hẹp 25–30°, gần trực giao, thấy toàn sân 40 × 26 m và cả triều thú. Theo §8.1, Trận Tâm ở (0; 0), hai cổng ở (∓15; −18), đường trời từ hai góc xa, hai Trận Trụ và sáu ô cơ quan. Trận Tâm là tâm gameplay, không dịch sang trung điểm hình học của hình chữ nhật. Sáu ô được diễn tả bằng nền đá vật lý, không tự thêm dấu HUD trong đợt.

Hai chân dung để anh chọn phục sức; **tạm chọn A (miện nhỏ)** làm tham chiếu cặp NV01 trước/sau, chưa thay quyết định duyệt của anh. Cảnh và chân dung không đưa trực tiếp vào Tripo. Nguồn nhân vật ở [01-cultivators-bots.md](01-cultivators-bots.md); đồ cảnh vẫn dựng từng vật theo file 06.

Mỗi ảnh Phiếu 008 tối đa **hai lượt**, kể cả lượt đầu; trần 40 thuộc Phiếu 007 đã kết thúc, không phải ngân sách của phiếu sửa này. Bốn PNG bị thay và prompt cũ được đổi thành `<tên>.v1.png`, `<tên>.v1.prompt.txt`; bản thử không chọn giữ tên `-rejected-1`. Mỗi khối dưới là **nguyên văn prompt của bản giữ**; mô tả tham chiếu là một phần prompt.

| Mã | File | Khổ yêu cầu | Ảnh tham chiếu | Lượt |
|---|---|---|---|---|
| BS02-A | `identity/kiem-tu-portrait.png` | 1024×1536 | — | 1/2 · miện nhỏ, trắng ngọc chủ đạo |
| BS02-B | `identity/kiem-tu-portrait-ngoc-tram.png` | 1024×1536 | — | 1/2 · trâm hạc, lam sẫm chủ đạo |
| BS01-50 | `identity/thanh-thach-ai.png` | 1920×1080 | — | 2/2 · bản giữ; lượt đầu cắt mái cổng |
| BS01-55 | `identity/thanh-thach-ai-55.png` | 1920×1080 | `identity/thanh-thach-ai.png` | 1/2 · cùng bố cục, yêu cầu góc 55° và lề rộng hơn |

## BS02-A · Chân dung Kiếm tu · miện nhỏ

**File:** `games/immortality-cultivation/art-src/identity/kiem-tu-portrait.png` · **Đính kèm:** không.

```text
Use case: stylized-concept.
Asset type: royal sword-cultivator identity portrait, option A, for the original Vietnamese fantasy game Tu Tien Thu Ai.
Primary request: a strikingly beautiful young adult Vietnamese woman sword cultivator, about 24, with delicate harmonious facial features, dark almond eyes, luminous natural skin and a calm noble gaze. She stands very upright, shoulders relaxed, head held with the composed dignity of a royal heir.
Costume A: pearl-white layered silk robes inspired by the structure of Vietnamese ao ngu than, a fully closed high inner collar, long fitted inner sleeves, deep-indigo outer shoulder and side panels, a wide indigo silk waist belt, fine pale antique-gold embroidered borders and elegant large cloud-and-crane motifs. A compact low royal diadem of pale gold and white jade sits above a smooth black updo; one substantial white-jade pendant hangs neatly at the waist. Refined royal craftsmanship, restrained and graceful.
Sword: the Thanh Phong sword of a royal cultivator rests vertically at her side in a deep-indigo lacquer scabbard with pale-gold cloud fittings, a white-jade pommel and a dignified straight guard; her relaxed hand rests near its hilt. The sword is a physical crafted object.
Composition: one upright character, head to just below hips, face large enough to judge beauty and nobility, crown, collar, waist pendant and sword hilt all visible, gentle three-quarter body angle, gaze towards viewer.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, a sparse old pine and soft indigo mist stay subordinate to the woman.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty.
Lighting and palette: soft broad daylight, pearl white, deep indigo, ink charcoal, limestone grey, restrained pale antique gold and opaque white jade. Gold is muted embroidery, never bright reward-yellow or emissive.
Constraints: fully clothed, opaque layered silk covering chest, shoulders and legs; dignified all-ages presentation. One original character, one view, no text, letters, numbers, UI, logo, watermark or frame; no cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No aura, floating ornament or bright magical effect.
Output: one portrait PNG, 1024x1536.
```

## BS02-B · Chân dung Kiếm tu · trâm ngọc hình hạc

**File:** `games/immortality-cultivation/art-src/identity/kiem-tu-portrait-ngoc-tram.png` · **Đính kèm:** không.

```text
Use case: stylized-concept.
Asset type: royal sword-cultivator identity portrait, option B, for the original Vietnamese fantasy game Tu Tien Thu Ai.
Primary request: a strikingly beautiful young adult Vietnamese woman sword cultivator, about 24, with delicate harmonious facial features, dark almond eyes, luminous natural skin and a calm noble gaze. She stands very upright, shoulders relaxed, head held with the composed dignity of a royal heir.
Costume B: deep-indigo layered silk robes inspired by the structure of Vietnamese ao ngu than, broad pearl-white overlapping front panels, a fully closed high white inner collar, long neat sleeves with pearl-white cuffs, a pearl-white silk waist belt. Fine pale antique-gold borders and elegant large royal cloud-and-crane embroidery ornament the indigo shoulder panels and cuffs. Her smooth black hair is arranged in a compact low braided bun, secured by a sculpted white-jade crane hairpin with a small pale-gold setting; a substantial oval white-jade pendant sits neatly at the waist. Quiet royal refinement and practical sword-cultivator bearing.
Sword: the Thanh Phong sword of a royal cultivator rests vertically at her side in a pearl-white lacquer scabbard with deep-indigo accents, pale-gold cloud fittings and a white-jade pommel; her relaxed hand rests near its dignified straight hilt. The sword is a physical crafted object.
Composition: one upright character, head to just below hips, face large enough to judge beauty and nobility, jade hairpin, collar, waist pendant and sword hilt all visible, gentle three-quarter body angle, gaze towards viewer.
Scene: a quiet Vietnamese limestone frontier pass; distant karst silhouettes, a sparse old pine and soft indigo mist stay subordinate to the woman.
Style: original Vietnamese fantastical landscape aesthetic, sculptural stylized 3D concept art with soft ink-wash value steps and subtle do-paper material character; exquisite but readable silk masses, believable adult proportions, refined serene beauty.
Lighting and palette: soft broad daylight, deep indigo, pearl white, ink charcoal, limestone grey, restrained pale antique gold and opaque white jade. Gold is muted embroidery, never bright reward-yellow or emissive.
Constraints: fully clothed, opaque layered silk covering chest, shoulders and legs; dignified all-ages presentation. One original character, one view, no text, letters, numbers, UI, logo, watermark or frame; no cleavage, exposed midriff, high slit, sexualized pose, blood or horror. No aura, floating ornament or bright magical effect.
Output: one portrait PNG, 1024x1536.
```

## BS01-50 · Thanh Thạch Ải · camera 50°

**File:** `games/immortality-cultivation/art-src/identity/thanh-thach-ai.png` · **Đính kèm:** không.

```text
Use case: stylized-concept.
Asset type: full-battlefield game-camera identity concept for the original Vietnamese fantasy pass-defense game Tu Tien Thu Ai, Thanh Thach Ai.
Camera and framing are the primary requirement: a fixed overhead game camera looking down 50 degrees BELOW THE HORIZONTAL, facing north along the courtyard length with no dramatic camera yaw or roll, narrow 25-degree field of view with near-orthographic compression. Wide 16:9 landscape. Pull back until the ENTIRE 40-metre east-west by 26-metre north-south playable field and a generous clear margin fit inside the image. All FOUR field corners, both complete beast-entry gates, both sky-route entry points and every creature are inside the frame. FRAMING OVERRIDE: the complete court occupies only the central 75 percent of image width and 75 percent of image height. A continuous visible 10 to 12 percent environment margin runs along ALL FOUR edges. Pull the camera back farther than a normal illustration: BOTH gate rooftops, all four courtyard corners, ALL crow wingtips and the entire near Son Mon staircase must remain clear of every image edge. No architecture or creature touches the image border. Ground fills most of the central frame. No horizon. Every equally sized creature stays nearly the same screen size across the field. No foreground enlargement or strong perspective.
Map layout: one broad continuous limestone courtyard, bounds x=-20 to +20 metres and z=-18 to +8 metres. A low circular Tran Tam formation core is at world (0,0), the gameplay centre, slightly below image centre. A complete faint 9-metre-radius inlaid stone circle marks its protection area. Exactly two low single-roof Vietnamese beast-entry gates stand on the FAR edge at x=-15 and +15, z=-18. Broad open approach corridors curve from those gates toward the core and merge naturally; ample open ground between them. Exactly TWO simple freestanding monolithic stone Tran Tru cover pillars, without miniature pagoda roofs, sit left and right of the middle approach. SIX muted rectangular stone mechanism foundations: four across the upper-middle field and two flanking the lower approach; show them as physical paving, with small grounded mechanisms, no glowing interface markers. A modest Son Mon gate sits beyond the near field edge and remains entirely inside the outer margin.
Beast tide: about 45 small individually separated creatures stream from BOTH far gates toward the core; leave clear ground between silhouettes. Show all five legible families: low squat stone-backed rats with long tails, lean long-legged wolves with pointed ears and long muzzles, broad armored boars with paired tusks, tall upright rock macaques with long arms, and dark crows with clearly spread wings. The crows enter from BOTH far outer corners on distinct high diagonal sky routes toward the core, flying above the ground mechanisms. Each family has a different readable body shape and neutral material value. All beasts are small in this full-map view but still recognizable. One larger iron-backed WOLF king with a clearly long pointed canine muzzle, pointed wolf ears, lean wolf legs, long bushy wolf tail and angular back plates stands fully visible just inside the far right beast gate; still modest in screen area, never a giant foreground monster.
Defender: one SMALL upright female royal sword cultivator beside the Tran Tam, pearl-white and deep-indigo layered silk, compact pale-gold jade diadem, fine pale-gold trim; about normal human height within the 40-metre field. Her Thanh Phong sword is a small physical ivory blade beside her. The field and complete tide have visual priority.
Environment and style: original Vietnamese fantastical landscape, sculptural stylized 3D game art with restrained ink-wash values and subtle do-paper material character. Low limestone perimeter, a few sparse pines and misty karst suggestions occupy only the narrow outer border, never cover the field or dominate the frame. Keep the entire playable surface crisp, pale and readable; indigo mist stays outside the court. Soft even daylight. Palette of limestone grey, indigo, ink charcoal, muted moss, warm ivory; restrained pale-gold costume embroidery only.
Constraints: one coherent complete map, no inset, split panel, UI, text, letters, numbers, labels, logo or watermark. No cinematic close-up, wide-angle distortion, huge foreground creature, occluding foreground cliff, towering decorative architecture, bright spell trails, dense effects, glowing eyes, blood or horror. The six foundations are physical stones, not HUD slots.
Output: one landscape PNG, 1920x1080, 16:9.
```

## BS01-55 · Thanh Thạch Ải · camera 55°

**File:** `games/immortality-cultivation/art-src/identity/thanh-thach-ai-55.png` · **Đính kèm:** `identity/thanh-thach-ai.png` làm tham chiếu bố cục, không giữ nguyên khung camera.

```text
Use case: stylized-concept.
Asset type: full-battlefield game-camera identity concept for the original Vietnamese fantasy pass-defense game Tu Tien Thu Ai, Thanh Thach Ai.
Camera and framing are the primary requirement: a fixed overhead game camera looking down 55 degrees BELOW THE HORIZONTAL, facing north along the courtyard length with no dramatic camera yaw or roll, narrow 25-degree field of view with near-orthographic compression. Wide 16:9 landscape. Pull back until the ENTIRE 40-metre east-west by 26-metre north-south playable field and a generous clear margin fit inside the image. All FOUR field corners, both complete beast-entry gates, both sky-route entry points and every creature are inside the frame. FRAMING OVERRIDE: the complete court occupies only the central 70 percent of image width and 70 percent of image height. A continuous visible at least 12 percent environment margin runs along ALL FOUR edges. Pull the camera back farther than a normal illustration: BOTH gate rooftops, all four courtyard corners, ALL crow wingtips and the entire near Son Mon staircase must remain clear of every image edge. No architecture or creature touches the image border. Ground fills most of the central frame. No horizon. Every equally sized creature stays nearly the same screen size across the field. No foreground enlargement or strong perspective.
Map layout: one broad continuous limestone courtyard, bounds x=-20 to +20 metres and z=-18 to +8 metres. A low circular Tran Tam formation core is at world (0,0), the gameplay centre, slightly below image centre. A complete faint 9-metre-radius inlaid stone circle marks its protection area. Exactly two low single-roof Vietnamese beast-entry gates stand on the FAR edge at x=-15 and +15, z=-18. Broad open approach corridors curve from those gates toward the core and merge naturally; ample open ground between them. Exactly TWO simple freestanding monolithic stone Tran Tru cover pillars, without miniature pagoda roofs, sit left and right of the middle approach. SIX muted rectangular stone mechanism foundations: four across the upper-middle field and two flanking the lower approach; show them as physical paving, with small grounded mechanisms, no glowing interface markers. A modest Son Mon gate sits beyond the near field edge and remains entirely inside the outer margin.
Beast tide: about 45 small individually separated creatures stream from BOTH far gates toward the core; leave clear ground between silhouettes. Show all five legible families: low squat stone-backed rats with long tails, lean long-legged wolves with pointed ears and long muzzles, broad armored boars with paired tusks, tall upright rock macaques with long arms, and dark crows with clearly spread wings. The crows enter from BOTH far outer corners on distinct high diagonal sky routes toward the core, flying above the ground mechanisms. Each family has a different readable body shape and neutral material value. All beasts are small in this full-map view but still recognizable. One larger iron-backed WOLF king with a clearly long pointed canine muzzle, pointed wolf ears, lean wolf legs, long bushy wolf tail and angular back plates stands fully visible just inside the far right beast gate; still modest in screen area, never a giant foreground monster.
Defender: one SMALL upright female royal sword cultivator beside the Tran Tam, pearl-white and deep-indigo layered silk, compact pale-gold jade diadem, fine pale-gold trim; about normal human height within the 40-metre field. Her Thanh Phong sword is a small physical ivory blade beside her. The field and complete tide have visual priority.
Environment and style: original Vietnamese fantastical landscape, sculptural stylized 3D game art with restrained ink-wash values and subtle do-paper material character. Low limestone perimeter, a few sparse pines and misty karst suggestions occupy only the narrow outer border, never cover the field or dominate the frame. Keep the entire playable surface crisp, pale and readable; indigo mist stays outside the court. Soft even daylight. Palette of limestone grey, indigo, ink charcoal, muted moss, warm ivory; restrained pale-gold costume embroidery only.
Constraints: one coherent complete map, no inset, split panel, UI, text, letters, numbers, labels, logo or watermark. No cinematic close-up, wide-angle distortion, huge foreground creature, occluding foreground cliff, towering decorative architecture, bright spell trails, dense effects, glowing eyes, blood or horror. The six foundations are physical stones, not HUD slots.
Output: one landscape PNG, 1920x1080, 16:9.
Input image 1: games/immortality-cultivation/art-src/identity/thanh-thach-ai.png is the map-layout and art-direction reference. Retain its two-gate layout, two plain stone pillars, six mechanism foundations, small royal defender, five beast families and wolf king. Raise the camera to 55 degrees below horizontal and pull back substantially to show a wider margin on every side. Show all four corners and complete gate roofs with empty border above them. Keep the field dominant and keep all architecture and every crow strictly inside the image.
```

## Kiểm ảnh và giới hạn

- Chân dung: so sánh vẻ thanh tú, dáng đứng, khí chất hoàng tộc và hai cách phục sức; không coi việc chọn tạm A là anh đã duyệt.
- Cảnh: đủ bốn góc sân, hai cổng trọn mái, hai điểm vào đường trời, Trận Tâm, hai Trận Trụ, sáu nền cơ quan, thú nhỏ từng họ và Vương ở cổng xa; núi và sương nằm ngoài sân. Bản 50° còn sát lề trên; bản 55° thoáng hơn.
- 50° và 55° là góc **yêu cầu trong prompt**; ảnh AI không phải phép đo camera. Cổng runtime `ic-camera-frame` ở 1280×720 và 1920×1080 vẫn theo D48; không thay mã hoặc chạy game trong phiếu này.
- Nguồn NV01 giữ tư thế A, một góc mỗi ảnh, nền phẳng `#E6E6E6`, không hiệu ứng; kiểm pixel và đối chiếu trước/sau, không lấy prompt làm bằng chứng.
- Mỗi ảnh chỉ được sửa một lần. Prompt bản thử đầu nằm cạnh PNG thử; không gửi bản `.v1` hoặc `-rejected-1` vào Tripo cho thiết kế mới.

