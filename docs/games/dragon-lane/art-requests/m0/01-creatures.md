# Rồng Giữ Ải — M0 · 01. Ảnh 2D sinh vật địch gửi Tripo (23/10/2026)

> **Dành cho:** chủ dự án (dựng model bằng Tripo); AI điều khiển Codex CLI tạo ảnh 2D trên máy (đăng nhập ChatGPT, không dùng API key); AI ghép file sau (Blender, manifest).
> **Lấy từ:** `../../DESIGN.md` §7 (ai làm gì, danh sách lát M0), §9 M0; `../../02-enemies-generals-bosses.md` §1.1 (Bầy Héo, dấu Héo), §1.5 (màu VFX), §2.1–2.2 (E01, E09, E11, E18, E19, E25), §3.2, §3.4 (G01), §7.2 (rig, clip); `../../05-presentation-audio-tech-split.md` §2 (phong cách, màu, tỉ lệ); `../../research/art-pipeline.md` §7 (ảnh gửi Tripo theo dáng).
> **Mục lục, thứ tự làm, thiết lập Tripo, nơi lưu GLB:** [`README.md`](README.md). Mỗi khối `text` là **một ảnh**: dán nguyên văn, không rút gọn, không thêm bớt. Các dòng chung giống từng chữ ở mọi prompt (README §5).

## 1. Luật chung

- **Dấu Héo chặn mọi ảnh quái khác** (02 §1.1, 00 D02). Làm HT-A và HT-B trước. Chủ dự án chọn A hoặc B, rồi mới làm các ảnh còn lại. Mọi prompt trong file này viết theo **A** (đúng câu thiết kế "phủ một phần thân"). Chọn B thì đổi hai câu theo mục 11.
- **Mẫu duyệt** (DESIGN §7.2): HT-A, HT-B, E09-F, E18-S, E18-F, E01-F. Ảnh phụ còn lại của E09, E01 làm sau khi chủ dự án duyệt dáng.
- **Góc nhìn theo dáng** (art-pipeline §7): hai chân: ảnh chính nhìn thẳng, tư thế A; ảnh phụ nhìn sau (`-back`). Bốn chân và bò: ảnh chính nhìn ngang bên trái, đầu quay trái; ảnh phụ nhìn thẳng (`-front`). Bay: ảnh chính nhìn thẳng, cánh dang chữ V; ảnh phụ nhìn ngang (`-side`). Ảnh phụ luôn đính kèm ảnh chính đã duyệt.
- **Nền** xám nhạt phẳng `#E6E6E6` (Tripo tách nền). Không bóng đổ, không viền đen, không lửa, khói, sương, hạt, chữ.
- **Không máu** (02 §1.1). Vàng úa `#C8D24A` chỉ ở khe nứt và mắt, là **màu sơn**, không phải quầng sáng: quầng sáng sẽ dính vào texture. Ánh sáng thật của khe nứt do shader làm. Hắc Vụ là VFX, không vẽ.
- **Màu giữ riêng** (05 §2.2): không tô mảng lớn đỏ, cam, vàng kim, xanh ngọc lên quái.
- **Cỡ:** ghi "cao thật". Game phóng nhân vật 1,4 lần so với cảnh (05 §2.3). Quái thường 32–44 px, bầy ≥ 26 px, tướng ≥ 60 px ở 1080p.
- **Clip:** quái thường chỉ cần 4 clip Idle, Move, Attack, Death; trúng đòn là phản ứng instanced. Tướng có đủ bộ (02 §7.2). Chọn clip ở README §3.

**Tự quyết** (thiết kế chưa ghi):

- Rêu của Yêu Rêu là **rêu khô xám lục** (dusty sage), không phải lục tươi: đúng chữ "Héo", và không chìm vào cỏ khi nhìn từ trên.
- Ong Gai **không sọc vàng đen**: vàng dễ lẫn với vàng úa (dấu Héo) và vàng kim (tiền). Thân lam thông và than, dải kem.
- Ảnh thử Héo nhìn **xiên 45° từ trên** như camera game, trên nền phẳng: chủ dự án duyệt độ đọc của dấu Héo ở góc thật. Ảnh E09 gửi Tripo vẫn nhìn thẳng, tư thế A.
- HT-B đính kèm HT-A để hai ảnh chỉ khác độ phủ vỏ. E09-F đính kèm ảnh thử đã chọn để giữ cùng một con. Không có ảnh đính kèm thì bỏ dòng `Reference:` của prompt.
- Hai chân lấy ảnh phụ **nhìn sau**, không nhìn ngang: lưng mang mảng vỏ, ống tên, cờ, và camera 55° thấy lưng quái nhiều.
- G01: cờ dính liền model. "Cờ cắm" của kỹ năng Cắm Cờ dùng bản tách phần cờ từ chính model này trong Blender (tách, không dựng lưới). Cần model cờ riêng thì thêm một ảnh ở M1.

## 2. Bảng ảnh

Cột ảnh bỏ tiền tố `games/dragon-hold/art-src/`. Model 3D: thêm `3d/` sau `art-src/`, đuôi `.glb`, chỉ ảnh chính có GLB (README §3).

| Mã | Ảnh | File | Khổ | Đính kèm | Lát |
|---|---|---|---|---|---|
| HT-A | Ảnh thử dấu Héo A (vỏ ít) | `refs/heo-test-a.png` | 1024×1536 | — | Mẫu duyệt |
| HT-B | Ảnh thử dấu Héo B (vỏ nhiều) | `refs/heo-test-b.png` | 1024×1536 | HT-A | Mẫu duyệt |
| E09-F | E09 Yêu Rêu Lính · ảnh chính, nhìn thẳng | `enemies/moss-grunt.png` | 1024×1536 | HT-A | Mẫu duyệt |
| E09-B | E09 · nhìn sau | `enemies/moss-grunt-back.png` | 1024×1536 | E09-F | Sau khi duyệt mẫu |
| E18-S | E18 Sói Mục · ảnh chính, nhìn ngang | `enemies/blight-wolf.png` | 1536×1024 | — | Mẫu duyệt |
| E18-F | E18 · nhìn thẳng | `enemies/blight-wolf-front.png` | 1024×1024 | E18-S | Mẫu duyệt |
| E01-F | E01 Ong Gai · ảnh chính, nhìn thẳng | `enemies/thorn-wasp.png` | 1536×1024 | — | Mẫu duyệt |
| E01-S | E01 · nhìn ngang | `enemies/thorn-wasp-side.png` | 1024×1024 | E01-F | Sau khi duyệt mẫu |
| E11-F | E11 Yêu Rêu Cung · ảnh chính | `enemies/moss-archer.png` | 1024×1536 | — | M0 |
| E11-B | E11 · nhìn sau | `enemies/moss-archer-back.png` | 1024×1536 | E11-F | M0 |
| E19-S | E19 Heo Nanh Đá · ảnh chính, nhìn ngang | `enemies/tusk-boar.png` | 1536×1024 | — | M0 |
| E19-F | E19 · nhìn thẳng | `enemies/tusk-boar-front.png` | 1024×1024 | E19-S | M0 |
| E25-S | E25 Kiến Gai · ảnh chính, nhìn ngang | `enemies/thorn-ant.png` | 1536×1024 | — | M0 |
| E25-F | E25 · nhìn thẳng | `enemies/thorn-ant-front.png` | 1024×1024 | E25-S | M0 |
| G01-F | G01 Yêu Rêu Cầm Cờ · ảnh chính | `generals/moss-banner.png` | 1024×1536 | — | M0 |
| G01-B | G01 · nhìn sau | `generals/moss-banner-back.png` | 1024×1536 | G01-F | M0 |

## 3. Ảnh thử dấu Héo (HT-A, HT-B)

| Mục | Giá trị |
|---|---|
| Mục đích | Cổng của 02 §1.1: chủ dự án chọn độ phủ vỏ Héo trước khi làm ảnh quái hàng loạt |
| Con mẫu | E09 Yêu Rêu Lính, cùng một con ở hai ảnh |
| A | Vỏ phủ khoảng 1/4 thân: vai trái và bắp tay, góc mặt nạ, gối phải. Giữ nhiều màu loài |
| B | Vỏ phủ khoảng 1/2–2/3 thân: hai vai, gần hết mặt nạ, lưng và ngực áo rêu, hai ống chân. Đọc phe rõ hơn, mất bớt màu loài |
| Góc | Xiên 45° từ trên, như camera game; nền phẳng. Không gửi Tripo |
| Cách xem | Xem cỡ thật trong game: thu ảnh còn cao 40 px, đặt trên nền cỏ (bài nheo mắt TD 23.1). Tấm `review-sheet.png` có sẵn dải này |

**HT-A** · ảnh thử A · `refs/heo-test-a.png` · 1024×1536

```text
Look-test picture of ONE enemy creature for a stylized 3D defense game; it is not sent to the 3D tool, it shows the art director how the enemy faction mark reads from the game camera.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: three-quarter view from the front and a little to one side, looking down from about 45 degrees above like the game's top-down camera, near-orthographic; the whole creature is visible, including the top of its head, its shoulders and part of its back. Pose: its in-game stance, slightly hunched with the knees a little bent, the stone knife held low in its right hand, head up, eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Grunt, a small foot soldier of the moss goblins, about 1.6 m tall, chibi proportions about 3 heads tall: a stocky round body, short bowed legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a small jagged mouth slit; a shaggy hooded cape of thick dry moss hangs in a few big clumps down to the hips; a round moss cap with two big leaves sits on top of the head; a belt of twisted root holds a muted violet cloth wrap at the waist. In its right hand (on the viewer's left in a front view) it grips a chunky flint stone knife with a short wooden handle, blade pointing down and away from the leg. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a few cream fungus spots on the cape, muted violet waist cloth.
Shell placement (look A): ash-grey shell covers the left shoulder and upper arm, the upper left corner of the bark mask and the right knee; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**HT-B** · ảnh thử B · `refs/heo-test-b.png` · 1024×1536 · đính kèm: `refs/heo-test-a.png` (HT-A)

```text
Look-test picture of ONE enemy creature for a stylized 3D defense game; it is not sent to the 3D tool, it shows the art director how the enemy faction mark reads from the game camera.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: three-quarter view from the front and a little to one side, looking down from about 45 degrees above like the game's top-down camera, near-orthographic; the whole creature is visible, including the top of its head, its shoulders and part of its back. Pose: its in-game stance, slightly hunched with the knees a little bent, the stone knife held low in its right hand, head up, eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look B, heavy): the ash-grey shell covers about half to two thirds of the body, only where the species text below says.
Species: Moss Grunt, a small foot soldier of the moss goblins, about 1.6 m tall, chibi proportions about 3 heads tall: a stocky round body, short bowed legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a small jagged mouth slit; a shaggy hooded cape of thick dry moss hangs in a few big clumps down to the hips; a round moss cap with two big leaves sits on top of the head; a belt of twisted root holds a muted violet cloth wrap at the waist. In its right hand (on the viewer's left in a front view) it grips a chunky flint stone knife with a short wooden handle, blade pointing down and away from the leg. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a few cream fungus spots on the cape, muted violet waist cloth.
Shell placement (look B): ash-grey shell covers both shoulders and upper arms like rough pauldrons, most of the bark mask except the eye holes and the mouth slit, the back and chest of the moss cape, and both shins; withered yellow-green cracks run across every patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Reference: the attached image is look A of this same creature; keep the same character, camera, pose and colours, and change only the shell, which now covers much more of the body as described here.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 4. E09 · `moss-grunt` · Yêu Rêu Lính

| Mục | Giá trị |
|---|---|
| Là gì | Họ Yêu Rêu (`moss`), hai chân, chém cận chiến. Bậc Nhỏ 1 W, G1/K0, tốc S2 2,0. Mở C1 (02 §2.1) |
| Cao thật | 1,6 m |
| Nhìn từ trên | Mũ rêu khô hai lá, mảng vỏ xám tro trên vai, mắt vàng úa trong mặt nạ vỏ cây, dao đá |
| Clip | Idle, Walk (lom khom, lắc lư), Attack (giơ dao 0,5 s rồi chém), Death (ngã ngửa, thân tan thành rêu khô) |

**E09-F** · ảnh chính, nhìn thẳng · `enemies/moss-grunt.png` · 1024×1536 · đính kèm: `refs/heo-test-a.png` (HT-A)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: straight front view at chest height, near-orthographic, no perspective distortion, no tilt. Neutral A-pose: standing upright and facing the viewer, arms straight down and out 30 to 45 degrees from the body, elbows almost straight, legs straight and slightly apart, both feet flat on an invisible floor; a clear gap of empty background separates each arm from the body from the armpit down, and nothing touches an arm below the shoulder except an object gripped in that hand. Calm neutral expression, eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Grunt, a small foot soldier of the moss goblins, about 1.6 m tall, chibi proportions about 3 heads tall: a stocky round body, short bowed legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a small jagged mouth slit; a shaggy hooded cape of thick dry moss hangs in a few big clumps down to the hips; a round moss cap with two big leaves sits on top of the head; a belt of twisted root holds a muted violet cloth wrap at the waist. In its right hand (on the viewer's left in a front view) it grips a chunky flint stone knife with a short wooden handle, blade pointing down and away from the leg. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a few cream fungus spots on the cape, muted violet waist cloth.
Shell placement (look A): ash-grey shell covers the left shoulder and upper arm, the upper left corner of the bark mask and the right knee; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Reference: the attached image is the look test of this same creature; keep its design, colours, shell patches and proportions identical, and change only the camera and pose as described here.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E09-B** · ảnh phụ, nhìn sau · `enemies/moss-grunt-back.png` · 1024×1536 · đính kèm: `enemies/moss-grunt.png` (E09-F)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same character as the attached front image (the approved main image of this item): identical design, colours, shell patches, proportions, A-pose and scale. Seen straight from behind, near-orthographic, camera at chest height; the character faces straight away from the camera, the head is not turned and the face does not show. Left and right are swapped compared with the front image: a part on the viewer's right in the front image is on the viewer's left here; every part stays on the same side of the character's own body.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Grunt, a small foot soldier of the moss goblins, about 1.6 m tall, chibi proportions about 3 heads tall: a stocky round body, short bowed legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a small jagged mouth slit; a shaggy hooded cape of thick dry moss hangs in a few big clumps down to the hips; a round moss cap with two big leaves sits on top of the head; a belt of twisted root holds a muted violet cloth wrap at the waist. In its right hand (on the viewer's left in a front view) it grips a chunky flint stone knife with a short wooden handle, blade pointing down and away from the leg. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a few cream fungus spots on the cape, muted violet waist cloth.
Shell placement (look A): ash-grey shell covers the left shoulder and upper arm, the upper left corner of the bark mask and the right knee; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 5. E18 · `blight-wolf` · Sói Mục

| Mục | Giá trị |
|---|---|
| Là gì | Họ Thú Mục (`beast`), bốn chân, lao theo bầy 3–5 con, vồ qua 1 lính chặn. Bậc Nhỏ 1,2 W, tốc S4 3,6. Mở C3, có ở M0 |
| Cao thật | 0,8 m ở vai, dài 1,4 m |
| Nhìn từ trên | Dải vỏ xám dọc sống lưng, vết nứt vàng úa lan ra lông (dấu họ Thú Mục), đuôi rậm |
| Clip | Idle, Run, Attack (cắn; vồ báo 0,5 s), Death (lăn nghiêng, khói tan từ vết nứt) |

**E18-S** · ảnh chính, nhìn ngang · `enemies/blight-wolf.png` · 1536×1024

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body from nose to tail tip, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: exact side view of the creature's left side, head pointing to the left edge of the image, camera at body height, near-orthographic, no perspective distortion; do not turn the body toward the viewer. Neutral standing pose: all legs straight, separate and visible, feet flat on an invisible floor; head level; tail (if any) held out behind, clear of the legs. Eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Blight Wolf, a forest wolf that hunts in small packs, about 1.4 m from nose to tail tip and 0.8 m at the shoulder, chunky storybook proportions: a big head with a broad muzzle and big pointed ears (one with a small notch), a deep chest, short sturdy legs with big paws, a thick bushy tail. Its fur is grouped into a few big shaggy solid masses: smoky grey-brown flanks, a darker pine-blue-grey back, a cream muzzle, throat and chest. Mouth closed, the tips of two small fangs showing.
Shell placement (look A): a row of ash-grey shell plates runs along the spine from the back of the neck to the hips, and one larger plate covers the near shoulder; withered yellow-green cracks run across the plates and on into the fur around them (the beast-family mark), and the eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E18-F** · ảnh phụ, nhìn thẳng · `enemies/blight-wolf-front.png` · 1024×1024 · đính kèm: `enemies/blight-wolf.png` (E18-S)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body seen from the front, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same creature as the attached side image (the approved main image of this item): identical design, colours, shell patches, proportions, pose and scale. Seen straight from the front with the head facing the viewer, near-orthographic, camera at body height; all legs straight, separate and visible, feet flat on an invisible floor; the body and tail stay hidden behind the head and chest, not bent to the side.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Blight Wolf, a forest wolf that hunts in small packs, about 1.4 m from nose to tail tip and 0.8 m at the shoulder, chunky storybook proportions: a big head with a broad muzzle and big pointed ears (one with a small notch), a deep chest, short sturdy legs with big paws, a thick bushy tail. Its fur is grouped into a few big shaggy solid masses: smoky grey-brown flanks, a darker pine-blue-grey back, a cream muzzle, throat and chest. Mouth closed, the tips of two small fangs showing.
Shell placement (look A): a row of ash-grey shell plates runs along the spine from the back of the neck to the hips, and one larger plate covers the near shoulder; withered yellow-green cracks run across the plates and on into the fur around them (the beast-family mark), and the eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 6. E01 · `thorn-wasp` · Ong Gai

| Mục | Giá trị |
|---|---|
| Là gì | Họ Bọ Gai (`bug`), bay cao 3–4 m, bắn ngòi gai 10 m. Bậc Nhỏ 1 W, tốc S3 2,6. Mở C1 |
| Cỡ thật | To cỡ con mèo, sải cánh 1,2 m |
| Nhìn từ trên | Hai cánh lá tím khói, vỏ xám trên lưng ngực, gai đen (dấu họ Bọ Gai) |
| Clip | Fly, Attack (chổng bụng 0,4 s, bắn ngòi), Death (rơi xoáy). Blender `make_flight_clips` nếu Tripo không có |

**E01-F** · ảnh chính, nhìn thẳng · `enemies/thorn-wasp.png` · 1536×1024

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body and both wings from tip to tip, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: straight front view at body height, near-orthographic, no perspective distortion; the creature hovers level and faces the viewer; wings raised and spread wide to the left and right in a shallow V, fully visible and not covering the body; legs hang relaxed below the body, clear of each other. Eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Thorn Wasp, a big forest wasp about the size of a cat with a wingspan of about 1.2 m, chunky and round rather than spindly: a round head with two big rounded compound eyes, two short thick antennae and small closed mandibles; a round fuzzy thorax; a big rounded abdomen with broad bands, ending in one thick blunt black stinger pointing down; one pair of broad rounded wings like stiff solid leaves, smoky lilac with a few darker veins, opaque, not see-through; six short thick legs. A few short thick black thorns stick out of the thorax and the abdomen bands (the bug-family mark). Natural colours: deep pine-blue and charcoal chitin with dusty cream bands; no yellow-and-black warning stripes, no orange.
Shell placement (look A): ash-grey shell plates cover the top of the thorax and the first abdomen band; withered yellow-green cracks run across them, and both big compound eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E01-S** · ảnh phụ, nhìn ngang · `enemies/thorn-wasp-side.png` · 1024×1024 · đính kèm: `enemies/thorn-wasp.png` (E01-F)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body from nose to tail tip, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same creature as the attached front image (the approved main image of this item): identical design, colours, shell patches, proportions, pose and scale. Exact side view of the creature's left side, head pointing to the left edge of the image, camera at body height, near-orthographic; the wings stay raised exactly as in the front image and are only seen from the side, so the near wing shows its edge and hides the far wing; do not swing the wings forward or back.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Thorn Wasp, a big forest wasp about the size of a cat with a wingspan of about 1.2 m, chunky and round rather than spindly: a round head with two big rounded compound eyes, two short thick antennae and small closed mandibles; a round fuzzy thorax; a big rounded abdomen with broad bands, ending in one thick blunt black stinger pointing down; one pair of broad rounded wings like stiff solid leaves, smoky lilac with a few darker veins, opaque, not see-through; six short thick legs. A few short thick black thorns stick out of the thorax and the abdomen bands (the bug-family mark). Natural colours: deep pine-blue and charcoal chitin with dusty cream bands; no yellow-and-black warning stripes, no orange.
Shell placement (look A): ash-grey shell plates cover the top of the thorax and the first abdomen band; withered yellow-green cracks run across them, and both big compound eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 7. E11 · `moss-archer` · Yêu Rêu Cung

| Mục | Giá trị |
|---|---|
| Là gì | Họ Yêu Rêu, hai chân, bắn xa 12 m, bị áp sát thì lùi. Bậc Nhỏ 1,2 W, tốc S2. Mở C2, có ở M0 |
| Cao thật | 1,6 m |
| Nhìn từ trên | Mũ trùm rêu nhọn, ống tên sau lưng, cung gỗ rễ |
| Clip | Idle, Walk, Attack (kéo dây 0,6 s rồi bắn), Death (quỳ xuống, cung gãy) |

**E11-F** · ảnh chính, nhìn thẳng · `enemies/moss-archer.png` · 1024×1536

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: straight front view at chest height, near-orthographic, no perspective distortion, no tilt. Neutral A-pose: standing upright and facing the viewer, arms straight down and out 30 to 45 degrees from the body, elbows almost straight, legs straight and slightly apart, both feet flat on an invisible floor; a clear gap of empty background separates each arm from the body from the armpit down, and nothing touches an arm below the shoulder except an object gripped in that hand. Calm neutral expression, eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Archer, a moss goblin who shoots from range, about 1.6 m tall, chibi proportions about 3 heads tall, a little slimmer than a Moss Grunt: a round body, short legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a short pointed beak-like nose; a long pointed hood of thick dry moss falls to the shoulders in a few big clumps; a short moss cape; a bark quiver strapped flat on its back holds four thick arrows with solid leaf-shaped fletching, the fletching just showing above the right shoulder. In its left hand (on the viewer's right in a front view) it grips a short chunky bow of bent root wood with a thick solid bowstring, held upright beside the leg and clear of it. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a muted violet scarf, pale cream leaf fletching.
Shell placement (look A): ash-grey shell covers the right shoulder and upper arm, the tip of the hood and the left forearm; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E11-B** · ảnh phụ, nhìn sau · `enemies/moss-archer-back.png` · 1024×1536 · đính kèm: `enemies/moss-archer.png` (E11-F)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same character as the attached front image (the approved main image of this item): identical design, colours, shell patches, proportions, A-pose and scale. Seen straight from behind, near-orthographic, camera at chest height; the character faces straight away from the camera, the head is not turned and the face does not show. Left and right are swapped compared with the front image: a part on the viewer's right in the front image is on the viewer's left here; every part stays on the same side of the character's own body.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Archer, a moss goblin who shoots from range, about 1.6 m tall, chibi proportions about 3 heads tall, a little slimmer than a Moss Grunt: a round body, short legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a carved bark mask (the moss-goblin family mark) with two round eye holes and a short pointed beak-like nose; a long pointed hood of thick dry moss falls to the shoulders in a few big clumps; a short moss cape; a bark quiver strapped flat on its back holds four thick arrows with solid leaf-shaped fletching, the fletching just showing above the right shoulder. In its left hand (on the viewer's right in a front view) it grips a short chunky bow of bent root wood with a thick solid bowstring, held upright beside the leg and clear of it. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a muted violet scarf, pale cream leaf fletching.
Shell placement (look A): ash-grey shell covers the right shoulder and upper arm, the tip of the hood and the left forearm; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 8. E19 · `tusk-boar` · Heo Nanh Đá

| Mục | Giá trị |
|---|---|
| Là gì | Họ Thú Mục, bốn chân, húc thẳng 8 m hất lính. Bậc Vừa 3 W, G1, tốc S2. Mở C4, có ở M0 |
| Cao thật | 1,1 m ở vai, dài 1,8 m |
| Nhìn từ trên | Bướu vai phủ vỏ, bờm gai, cặp nanh đá cong |
| Clip | Idle, Walk, Attack (cào đất rồi húc, vạch đỏ 1 s), Death (trượt dài theo đà) |

**E19-S** · ảnh chính, nhìn ngang · `enemies/tusk-boar.png` · 1536×1024

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body from nose to tail tip, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: exact side view of the creature's left side, head pointing to the left edge of the image, camera at body height, near-orthographic, no perspective distortion; do not turn the body toward the viewer. Neutral standing pose: all legs straight, separate and visible, feet flat on an invisible floor; head level; tail (if any) held out behind, clear of the legs. Eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Stone-Tusk Boar, a heavy forest boar that charges, about 1.1 m at the shoulder and 1.8 m long, chunky storybook proportions: a big wedge-shaped head with a wide flat snout and small ears, a high muscular shoulder hump, a barrel body, short thick legs with neat hooves, a short tail with a tuft. Two big curved tusks of grey granite with moss in their grooves sweep up from the lower jaw. A stiff mane of dark bristles is grouped into one big solid ridge along the spine. Natural colours: dark umber-brown hide, lighter tan snout and belly, mossy granite tusks.
Shell placement (look A): ash-grey shell covers the forehead like a rough helmet and the shoulder hump like a saddle plate; withered yellow-green cracks run across both patches, and the small eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E19-F** · ảnh phụ, nhìn thẳng · `enemies/tusk-boar-front.png` · 1024×1024 · đính kèm: `enemies/tusk-boar.png` (E19-S)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body seen from the front, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same creature as the attached side image (the approved main image of this item): identical design, colours, shell patches, proportions, pose and scale. Seen straight from the front with the head facing the viewer, near-orthographic, camera at body height; all legs straight, separate and visible, feet flat on an invisible floor; the body and tail stay hidden behind the head and chest, not bent to the side.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Stone-Tusk Boar, a heavy forest boar that charges, about 1.1 m at the shoulder and 1.8 m long, chunky storybook proportions: a big wedge-shaped head with a wide flat snout and small ears, a high muscular shoulder hump, a barrel body, short thick legs with neat hooves, a short tail with a tuft. Two big curved tusks of grey granite with moss in their grooves sweep up from the lower jaw. A stiff mane of dark bristles is grouped into one big solid ridge along the spine. Natural colours: dark umber-brown hide, lighter tan snout and belly, mossy granite tusks.
Shell placement (look A): ash-grey shell covers the forehead like a rough helmet and the shoulder hump like a saddle plate; withered yellow-green cracks run across both patches, and the small eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 9. E25 · `thorn-ant` · Kiến Gai

| Mục | Giá trị |
|---|---|
| Là gì | Họ Bọ Gai, bò, bầy 6–10 con dùng chung một từ cụm. Bậc Bầy 0,4 W, tốc S3. Mở C1 |
| Cỡ thật | Dài 0,6 m (bầy ≥ 26 px) |
| Nhìn từ trên | Bụng tròn có mảng vỏ xám, hàng gai đen dọc lưng |
| Clip | Crawl, Attack (cắn), Death (lật bụng). Đám đông có xương: Blender giảm còn 1.500–3.000 tam giác |

**E25-S** · ảnh chính, nhìn ngang · `enemies/thorn-ant.png` · 1536×1024

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body from nose to tail tip, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: exact side view of the creature's left side, head pointing to the left edge of the image, camera at body height, near-orthographic, no perspective distortion; do not turn the body toward the viewer. Neutral standing pose: all legs straight, separate and visible, feet flat on an invisible floor; head level; tail (if any) held out behind, clear of the legs. Eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Thorn Ant, a swarm ant about the size of a small dog (0.6 m long), chunky and rounded rather than spindly: a big round head with closed mandibles and two short thick elbowed antennae, a round thorax, a big round abdomen, six short thick legs, three on each side, all touching the invisible floor. A row of short thick black thorns runs along its back (the bug-family mark). Natural colours: dark bark-brown and charcoal chitin with a warm umber tint, painted matte.
Shell placement (look A): one ash-grey shell plate covers the top of the abdomen; withered yellow-green cracks run across it, and the eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**E25-F** · ảnh phụ, nhìn thẳng · `enemies/thorn-ant-front.png` · 1024×1024 · đính kèm: `enemies/thorn-ant.png` (E25-S)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one creature, the whole body seen from the front, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same creature as the attached side image (the approved main image of this item): identical design, colours, shell patches, proportions, pose and scale. Seen straight from the front with the head facing the viewer, near-orthographic, camera at body height; all legs straight, separate and visible, feet flat on an invisible floor; the body and tail stay hidden behind the head and chest, not bent to the side.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Thorn Ant, a swarm ant about the size of a small dog (0.6 m long), chunky and rounded rather than spindly: a big round head with closed mandibles and two short thick elbowed antennae, a round thorax, a big round abdomen, six short thick legs, three on each side, all touching the invisible floor. A row of short thick black thorns runs along its back (the bug-family mark). Natural colours: dark bark-brown and charcoal chitin with a warm umber tint, painted matte.
Shell placement (look A): one ash-grey shell plate covers the top of the abdomen; withered yellow-green cracks run across it, and the eyes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 10. G01 · `moss-banner` · Yêu Rêu Cầm Cờ

| Mục | Giá trị |
|---|---|
| Là gì | Đội trưởng, hai chân. 6 W, G1. Hào quang Xung Phong (+15 % tốc), kỹ năng Cắm Cờ, Ấn Phá. Mở C1 ải 5; ra ở đợt 5 và 10 của M0 (02 §3.2) |
| Cao thật | 2,2 m (tướng ≥ 60 px) |
| Nhìn từ trên | Lá cờ vải xám tro có hình lá vàng úa, giáp vai bằng vỏ Héo, mặt nạ cao có ba nhánh cành |
| Clip | Bộ tướng: Idle, Walk (cờ phất theo bước), Attack (đâm cán cờ, giơ cờ 0,5 s), Cast (cắm cờ), Hit, Death (cờ gãy đổ), Intro (phất cờ, hô) |

**G01-F** · ảnh chính, nhìn thẳng · `generals/moss-banner.png` · 1024×1536

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: straight front view at chest height, near-orthographic, no perspective distortion, no tilt. Neutral A-pose: standing upright and facing the viewer, arms straight down and out 30 to 45 degrees from the body, elbows almost straight, legs straight and slightly apart, both feet flat on an invisible floor; a clear gap of empty background separates each arm from the body from the armpit down, and nothing touches an arm below the shoulder except an object gripped in that hand. Calm neutral expression, eyes open, mouth closed.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Banner-Bearer, a captain of the moss goblins and a minor enemy general, about 2.2 m tall, sturdier and taller than a Moss Grunt, chibi proportions about 3.5 heads tall: a broad round body, short strong legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a tall carved bark mask (the moss-goblin family mark) with two round eye holes and three short antler-like twig points on top; a heavy mantle of thick dry moss covers the shoulders; a wide belt of twisted root carries a curved wooden war horn hanging flat against the left hip. In its right hand (on the viewer's left in a front view) it grips a tall thick wooden banner pole that stands straight up beside it, the foot of the pole resting on the invisible floor next to the right foot and its top above the head; from a short crossbar at the top hangs a stiff rectangular banner of rough ash-grey cloth with a ragged bottom edge and one simple withered yellow-green leaf shape painted in the middle (no letters, no symbols), hanging still and clear of the body. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a muted violet cloth sash across the chest.
Shell placement (look A): ash-grey shell covers both shoulders like rough pauldrons and the centre of the chest like a breastplate; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**G01-B** · ảnh phụ, nhìn sau · `generals/moss-banner-back.png` · 1024×1536 · đính kèm: `generals/moss-banner.png` (G01-F)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same character as the attached front image (the approved main image of this item): identical design, colours, shell patches, proportions, A-pose and scale. Seen straight from behind, near-orthographic, camera at chest height; the character faces straight away from the camera, the head is not turned and the face does not show. Left and right are swapped compared with the front image: a part on the viewer's right in the front image is on the viewer's left here; every part stays on the same side of the character's own body.
Héo mark (enemy faction signature): this forest creature breathed the Hắc Vụ, a cursed violet-grey mist, and became withered and wild. Thick patches of ash-grey withered shell, like cooled charcoal with a dry, cracked, bark-like surface, have grown over part of its body; the rest of the creature keeps its natural species colours. Thin cracks across the shell and both eyes are painted a bright withered yellow-green (#C8D24A) as flat painted colour, with no halo, no light spill and no bloom. No blood, no wounds, no gore, no bones; a little menacing, but suitable for children.
Shell coverage (look A, light): the ash-grey shell covers about a quarter of the body, only where the species text below says.
Species: Moss Banner-Bearer, a captain of the moss goblins and a minor enemy general, about 2.2 m tall, sturdier and taller than a Moss Grunt, chibi proportions about 3.5 heads tall: a broad round body, short strong legs with big flat bare feet, long arms with big three-fingered hands. Its face is hidden behind a tall carved bark mask (the moss-goblin family mark) with two round eye holes and three short antler-like twig points on top; a heavy mantle of thick dry moss covers the shoulders; a wide belt of twisted root carries a curved wooden war horn hanging flat against the left hip. In its right hand (on the viewer's left in a front view) it grips a tall thick wooden banner pole that stands straight up beside it, the foot of the pole resting on the invisible floor next to the right foot and its top above the head; from a short crossbar at the top hangs a stiff rectangular banner of rough ash-grey cloth with a ragged bottom edge and one simple withered yellow-green leaf shape painted in the middle (no letters, no symbols), hanging still and clear of the body. Natural colours: dusty sage and olive moss, warm bark-brown mask and skin, a muted violet cloth sash across the chest.
Shell placement (look A): ash-grey shell covers both shoulders like rough pauldrons and the centre of the chest like a breastplate; withered yellow-green cracks run across each patch, and the eyes inside the mask holes are withered yellow-green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 11. Đổi sang dấu B (nếu chủ dự án chọn B)

Trong mọi prompt của file này: thay dòng `Shell coverage (look A, light)` bằng dòng dưới, và thay câu `Shell placement (look A): …` của loài bằng câu B của loài đó. E09-F đính kèm HT-B thay cho HT-A. Không đổi gì khác.

```text
Shell coverage (look B, heavy): the ash-grey shell covers about half to two thirds of the body, only where the species text below says.
```

**E09** (B)

```text
Shell placement (look B): ash-grey shell covers both shoulders and upper arms like rough pauldrons, most of the bark mask except the eye holes and the mouth slit, the back and chest of the moss cape, and both shins; withered yellow-green cracks run across every patch, and the eyes inside the mask holes are withered yellow-green.
```

**E18** (B)

```text
Shell placement (look B): ash-grey shell covers the whole back and neck like a rough saddle, both shoulders, the top of the head between the ears and the upper half of the tail; withered yellow-green cracks run across every plate and on into the fur around them (the beast-family mark), and the eyes are withered yellow-green.
```

**E01** (B)

```text
Shell placement (look B): ash-grey shell covers the whole thorax, the top of the head and the upper half of the abdomen; withered yellow-green cracks run across every plate, and both big compound eyes are withered yellow-green.
```

**E11** (B)

```text
Shell placement (look B): ash-grey shell covers both shoulders, the whole hood around the mask, the back of the cape around the quiver, both forearms and both shins; withered yellow-green cracks run across every patch, and the eyes inside the mask holes are withered yellow-green.
```

**E19** (B)

```text
Shell placement (look B): ash-grey shell covers the whole head except the snout and the eyes, the shoulder hump and the whole back to the hips, and the front of both front legs; withered yellow-green cracks run across every plate, and the small eyes are withered yellow-green.
```

**E25** (B)

```text
Shell placement (look B): ash-grey shell covers the whole abdomen, the top of the thorax and the top of the head; withered yellow-green cracks run across every plate, and the eyes are withered yellow-green.
```

**G01** (B)

```text
Shell placement (look B): ash-grey shell covers both shoulders and upper arms, the whole chest and belly, most of the bark mask except the eye holes, and both shins; withered yellow-green cracks run across every patch, and the eyes inside the mask holes are withered yellow-green.
```

## 12. Kiểm ảnh trước khi gửi Tripo

- [ ] Một con duy nhất, thấy trọn, không bị cắt, lề đều. Nền xám nhạt phẳng, không đất, không bóng.
- [ ] Đúng góc theo dáng (mục 1). Hai chân: có khe nền giữa tay và thân; đồ cầm không chạm thân. Bốn chân: thấy đủ chân, đầu quay trái.
- [ ] Dấu Héo đúng: vỏ xám tro nứt khô ở đúng chỗ prompt ghi, khe nứt và mắt vàng úa; phần còn lại giữ màu loài. Không máu, không vết thương.
- [ ] Vàng úa là màu sơn phẳng, không quầng sáng, không tia, không hạt.
- [ ] Phong cách tranh vẽ 3D: khối to, nét cọ mềm trên texture, không bóng loáng, không viền đen.
- [ ] Lông, rêu, lá thành mảng to; cánh đặc, không trong suốt; không sợi mảnh, không phần lơ lửng.
- [ ] Không chữ, số, logo, dấu nước, khung. Không màu giữ riêng thành mảng lớn.
- [ ] Ảnh phụ cùng con, cùng màu, cùng mảng vỏ, cùng cỡ. Ảnh `-back`: đồ lệch một bên đổi phía, đầu không ngoái lại.

Ảnh lỗi: tạo lại cùng prompt, thêm một câu nói rõ lỗi, ví dụ `Redo it: same creature, full body, nothing cropped, plain flat light-grey background, no cast shadow.`
