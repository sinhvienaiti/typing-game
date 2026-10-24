# Rồng Giữ Ải — M0 · 03. Kit rừng thông có sông (`pine-river`, xuân): 12 prop gửi Tripo (23/10/2026)

> **Dành cho:** chủ dự án (Tripo, không rig); AI điều khiển Codex CLI; AI làm Blender `--kind props` sau.
> **Lấy từ:** `../../DESIGN.md` §7.2 (M0: 12 cây, đá, bụi), §9 M0 (bản đồ `L2-cau`: một nhánh qua cầu, một nhánh lội suối); `../../04-stages-maps-progression.md` (kit `pine-river`, C1 xuân); `../../research/art-pipeline.md` §3 (công thức prop Tripo), §9 (thành phần kit); `../../05-presentation-audio-tech-split.md` §2 (tán tím `#8E7CC3`, lam `#6C8FD1` đặt xa đường).
> **Mục lục, thứ tự làm, thiết lập Tripo, nơi lưu GLB:** [`README.md`](README.md). Mỗi khối `text` là **một ảnh**: dán nguyên văn, không rút gọn, không thêm bớt. Các dòng chung giống từng chữ ở mọi prompt (README §5).

## 1. Luật chung

- Một vật mỗi ảnh, nhìn 3/4 xoay 30°, cao 30°, ánh sáng phẳng, đáy cắt phẳng, tán gom 3–6 khối tròn (art-pipeline §3). Nền xám nhạt phẳng.
- Tripo: Image to 3D, **không rig**, không clip. Blender `--kind props` (việc mới) chuẩn cỡ, gốc ở đáy, giảm còn 800–3.000 tam giác, LOD, nướng 1024².
- Lúc chạy mọi prop của kit dùng chung một vật liệu và ramp 3 bậc; gió lắc tán bằng shader. Ảnh không cần bóng, không cần ánh nắng.
- Cỏ, hoa, dương xỉ, sỏi **không** ở file này: là tranh 2D (decal, tấm cỏ hoa) ở file 04.
- Màu giữ riêng: không lá đỏ, cam, vàng kim, xanh ngọc gần đường (05 §2.2).

**Tự quyết** (DESIGN chỉ ghi "12 cây, đá, bụi"):

- 12 món = 4 cây (3 thông + 1 cây tán tím đặt xa đường), 2 bụi, 3 đá (có đá kê suối cho nhánh lội suối của `L2-cau`), 1 gốc cây, 1 khúc gỗ, 1 **cầu gỗ**. Bản đồ M0 có cầu, nên cầu vào M0 thay cho một hòn đá thứ tư; nếu chủ dự án muốn giữ đúng "cây, đá, bụi" thì cầu dùng khối tạm tới M2.
- 5 prop còn lại của kit làm ở M2 (DESIGN §7.2), ví dụ cây tán lam `#6C8FD1`, thông già đổ, mốc đá lớn, thác nhỏ, bụi dương xỉ lớn.
- **Bệ Rồng** (bệ giữa bản đồ) không có trong danh sách M0 của DESIGN §7.2. M0 dùng khối tạm; cần model thật thì thêm một ảnh (hỏi chủ dự án).
- Bài A/B cây (art-pipeline §3): ảnh ở đây cho bản **3D**. Bản 2D billboard cần ảnh nhìn ngang cao 10° riêng; chỉ làm khi chủ dự án muốn chạy A/B.

## 2. Bảng ảnh

Cột file bỏ tiền tố `games/dragon-hold/art-src/`.

| Mã | Món | Cỡ thật | File | Khổ |
|---|---|---|---|---|
| K01 | Thông cao | 9 m | `props/pine-river/pine-tall.png` | 1024×1536 |
| K02 | Thông dù già | 7 m | `props/pine-river/pine-round.png` | 1024×1536 |
| K03 | Thông non | 3,5 m | `props/pine-river/pine-young.png` | 1024×1536 |
| K04 | Cây tán tím (xa đường) | 7 m | `props/pine-river/tree-violet.png` | 1024×1536 |
| K05 | Bụi rêu | 1,2 m | `props/pine-river/bush-moss.png` | 1024×1024 |
| K06 | Bụi hoa kem, tím | 1 m | `props/pine-river/bush-blossom.png` | 1024×1024 |
| K07 | Đá tảng rêu | 2,5 m | `props/pine-river/rock-boulder.png` | 1024×1024 |
| K08 | Gờ đá phiến | 1,5 m × 3 m | `props/pine-river/rock-slab.png` | 1536×1024 |
| K09 | Đá kê suối | tới thắt lưng | `props/pine-river/river-stones.png` | 1536×1024 |
| K10 | Gốc thông | 0,8 m | `props/pine-river/stump.png` | 1024×1024 |
| K11 | Khúc gỗ đổ | dài 3 m | `props/pine-river/log.png` | 1536×1024 |
| K12 | Cầu gỗ cũ (mốc) | 8 × 3 m | `props/pine-river/bridge-old.png` | 1536×1024 |

## 3. Prompt

### K01 · Thông cao

**K01** · ảnh chính · `props/pine-river/pine-tall.png` · 1024×1536

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Tall Pine, a stylized pine tree about 9 m tall: a straight warm umber-brown trunk with chunky bark plates and three short root flares at a flat base; the crown is five stacked rounded tiers of deep pine-blue-green foliage, each tier one soft round mass a little darker underneath, getting smaller toward a rounded tip; a few short thick branch stubs show between the tiers.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K02 · Thông dù già

**K02** · ảnh chính · `props/pine-river/pine-round.png` · 1024×1536

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Old Umbrella Pine, about 7 m tall: a thick, slightly leaning umber-brown trunk that splits into two big curving limbs; the crown is four or five big flat-topped, cloud-like foliage pads in pine-blue-green with lighter moss-green tops, spread wide like an umbrella.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K03 · Thông non

**K03** · ảnh chính · `props/pine-river/pine-young.png` · 1024×1536

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Young Pine, about 3.5 m tall: a short umber-brown trunk and a cone of three rounded foliage tiers in lighter fresh moss green with pine-blue undersides.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K04 · Cây tán tím (xa đường)

**K04** · ảnh chính · `props/pine-river/tree-violet.png` · 1024×1536

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Violet Mist Tree, a broadleaf tree of the misty forest that grows far from the paths, about 7 m tall: a smooth pale grey-cream trunk with two gently curving limbs; a big round crown of five or six soft rounded masses in muted violet (#8E7CC3) with lighter lavender tops and slightly darker undersides.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K05 · Bụi rêu

**K05** · ảnh chính · `props/pine-river/bush-moss.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Moss Bush, about 1.2 m tall and 1.8 m wide: three or four big rounded leaf masses in fresh moss green with lighter tops, pressed together into one low dome.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K06 · Bụi hoa kem, tím

**K06** · ảnh chính · `props/pine-river/bush-blossom.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Blossom Bush, about 1 m tall and 1.6 m wide: a low dome of rounded deep-green leaf masses dotted with a few big soft clusters of cream-white and pale violet flowers, grouped as chunky clusters, not single petals.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K07 · Đá tảng rêu

**K07** · ảnh chính · `props/pine-river/rock-boulder.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Mossy Boulder, about 2.5 m tall: one big rounded granite boulder in cool blue-grey with soft violet-grey patches of painted colour and a thick rounded cap of moss on top as one solid mass.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K08 · Gờ đá phiến

**K08** · ảnh chính · `props/pine-river/rock-slab.png` · 1536×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Slate Ledge, about 1.5 m tall and 3 m wide: two flat-topped layered slate rocks leaning together as one connected piece, cool blue-grey with lighter edges and a little moss in the cracks.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K09 · Đá kê suối

**K09** · ảnh chính · `props/pine-river/river-stones.png` · 1536×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): River Stepping Stones: five rounded smooth river stones of different sizes, from knee-high to waist-high, touching each other in one low connected cluster, blue-grey with pale cream tops and a little moss at their bases.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K10 · Gốc thông

**K10** · ảnh chính · `props/pine-river/stump.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Old Pine Stump, about 0.8 m tall and 1.2 m wide: a thick cut stump with chunky bark and four root flares, a flat cut top showing pale cream rings, a cushion of moss on one side and two small round cream mushrooms growing from the bark.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K11 · Khúc gỗ đổ

**K11** · ảnh chính · `props/pine-river/log.png` · 1536×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring): Fallen Log, about 3 m long and 0.7 m thick, lying flat: a pine log with chunky bark, peeled to pale wood at one end, a long cushion of moss along the top and three short thick branch stubs.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### K12 · Cầu gỗ cũ (mốc)

**K12** · ảnh chính · `props/pine-river/bridge-old.png` · 1536×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Kit prop (pine-river forest, spring, landmark): Old Footbridge, about 8 m long and 3 m wide, made to span a forest stream: a gently arched deck of thick wooden planks resting at each end on a low abutment of stacked mossy stones and logs, low chunky log rails along both sides on short thick posts, green vines wrapped around two of the posts. Its length runs from the lower left to the upper right of the image so the deck and one side both show.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 4. Kiểm ảnh

- [ ] Một vật, thấy trọn, đáy cắt phẳng, không đất, không cỏ quanh gốc, không bóng.
- [ ] Tán gom thành 3–6 khối tròn, không lá rời, không kim thông từng sợi.
- [ ] Ánh sáng phẳng: không nắng xiên, không bóng đổ trên tán (ramp do shader làm).
- [ ] Cầu: thấy mặt cầu và một bên thành; một khối liền.
- [ ] Không chữ, không màu giữ riêng.
