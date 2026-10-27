# Rồng Giữ Ải — M0 · 02. Phe ta: bẫy, lính chặn, nhà phép gửi Tripo (23/10/2026)

> **Dành cho:** chủ dự án (Tripo); AI điều khiển Codex CLI; AI ghép file sau.
> **Lấy từ:** `../../DESIGN.md` §7.2, §9 M0 (3 bẫy, 2 hỗ trợ); `../../03-our-side-shop-traps-support.md` §7.2 (Gai Chông, Lưới Phóng, Bom Hạt Thông), §8.2 (Lều Thuốc Nam), §9.2 (Vệ Binh Rêu); `../../05-presentation-audio-tech-split.md` §2.2 (màu phe ta), §6.5–6.6 (hình bẫy, nhà, lính).
> **Mục lục, thứ tự làm, thiết lập Tripo, nơi lưu GLB:** [`README.md`](README.md). Mỗi khối `text` là **một ảnh**: dán nguyên văn, không rút gọn, không thêm bớt. Các dòng chung giống từng chữ ở mọi prompt (README §5).

## 1. Luật chung

- Phe ta **không có dấu Héo**: khỏe, sáng, không vỏ xám, không nứt vàng úa (dòng `Our side` trong prompt).
- Màu phe ta (05 §2.2): bẫy gỗ nâu, dây leo lục; nhà và lính có điểm **lam trời nhạt** (thanh máu lính là lam). Không dùng xanh ngọc `#7FF5E0` (màu sức gõ).
- Đồ đứng yên (bẫy, nhà): nhìn 3/4, xoay 30°, cao 30°, đáy cắt phẳng như đồ chơi đặt trên bàn. Một ảnh, Tripo Image to 3D, không rig.
- Vệ Binh Rêu có rig hai chân: như quái hai chân (ảnh chính nhìn thẳng tư thế A + ảnh nhìn sau).
- Mọi chuyển động của bẫy (gai trồi, quả thông thở, bắn lưới), giọt sáng của nhà, vòng tầm: **shader và VFX trong mã**, không cần thêm model.

**Tự quyết:**

- Vệ Binh Rêu là **thần gỗ bạch dương phủ rêu tươi**, mầm cây trên đầu: khác hẳn Yêu Rêu (mặt nạ vỏ cây, rêu khô) để người chơi không nhầm phe. Khi ngã thành nụ cây (05 §6.6): mầm trên đầu là chỗ VFX nụ mọc.
- Lưới Phóng là **trụ gỗ ba chân** đỡ một cuộn lưới cuộn chặt: lưới bung khi bắn là VFX.
- Bom Hạt Thông: hạt nhựa màu mật ong sẫm, không dùng vàng kim (tiền) hay cam (khẩn).

## 2. Bảng ảnh

Cột file bỏ tiền tố `games/dragon-hold/art-src/`.

| Mã | Món | Vai (03) | File | Khổ | Đính kèm |
|---|---|---|---|---|---|
| TR1 | Gai Chông `spikes` | Sàn, liên tục: dải 4 m, chậm 25 %, 8 VL/s | `traps/spikes.png` | 1536×1024 | — |
| TR2 | Bom Hạt Thông `pine-bomb` | Sàn: nổ 3 m, 120 VL, đẩy 2 m, hồi 22 s | `traps/pine-bomb.png` | 1024×1024 | — |
| TR3 | Lưới Phóng `net-launcher` | Trụ: bắn lưới quái bay thấp trong 10 m, Hạ Cánh 3 s | `traps/net-launcher.png` | 1024×1536 | — |
| U1-F | Vệ Binh Rêu `moss-warden` · ảnh chính | Lính chặn: suất chặn 2, máu 450, G1 | `units/moss-warden.png` | 1024×1536 | — |
| U1-B | Vệ Binh Rêu · nhìn sau | — | `units/moss-warden-back.png` | 1024×1536 | U1-F |
| H1 | Lều Thuốc Nam `herb-hut` | Nhà phép: hồi 1,5 % máu/s trong 7 m | `houses/herb-hut.png` | 1024×1024 | — |

## 3. Bẫy

### TR1 · Gai Chông (`spikes`)

| Mục | Giá trị |
|---|---|
| Chờ / kích | Gai nhú; gai trồi theo nhịp (05 §6.5). Mã nâng cả khối gai hoặc rung đỉnh bằng shader |
| Cỡ trong game | Dải 4 m ngang đường, cao tới gối; bẫy 30–50 px |
| Nhánh cấp 3 | Gai Độc, Gai Sắt: đổi màu đầu gai bằng vật liệu, không cần model mới |

**TR1** · ảnh chính · `traps/spikes.png` · 1536×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally trap: Spike Bed, a floor trap that lies across a forest path: a long low rectangular frame of thick dark-brown wooden planks, about four times as long as it is wide and knee-high, filled with three neat rows of short thick sharpened wooden stakes pointing straight up, their tips pale and freshly carved; thick green vine bindings wrap the four corners. Colours: dark wood brown, pale cut-wood tips, fresh vine green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### TR2 · Bom Hạt Thông (`pine-bomb`)

| Mục | Giá trị |
|---|---|
| Chờ / kích | Quả thông "thở" (co giãn bằng shader); nổ lóe, cột lửa hoặc nhựa, sóng tròn 3 m (05 §6.5) |
| Nạp lại | Vỏ rỗng (shader tối màu) + vòng đồng hồ |
| Cỡ trong game | Cao khoảng 1 m |

**TR2** · ảnh chính · `traps/pine-bomb.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally trap: Pine-Cone Bomb, a floor trap: one giant pine cone the size of a barrel standing upright, with thick chunky overlapping scales in warm brown with darker tips and small deep honey-amber resin beads between the scales (painted, not glowing); it sits in a low round cradle of woven twigs and green vine, pinned to the ground by three short wooden pegs; a short thick green vine fuse curls from the top of the cone. Colours: warm brown, dark brown, deep honey-amber, fresh vine green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

### TR3 · Lưới Phóng (`net-launcher`)

| Mục | Giá trị |
|---|---|
| Chờ / kích | Trụ có cuộn lưới; khi bắn, lưới bung và kéo quái bay xuống (VFX + Hạ Cánh) |
| Cỡ trong game | Cao 2,5 m, đứng bên đường |
| Ghi chú Blender | Cần socket ở đầu cuộn lưới (`FX_MUZZLE`) để VFX bắn ra đúng chỗ; trụ có thể xoay theo quái bằng mã (cả model) |

**TR3** · ảnh chính · `traps/net-launcher.png` · 1024×1536

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally trap: Net Launcher, a post trap that stands beside a path and shoots nets at low-flying enemies, about 2.5 m tall: a thick dark-wood post on a wide, sturdy three-legged base; on top, a short swivelling launcher of bent wood like a big chunky crossbow without a string, pointing up and forward; resting in it, one big net rolled up tight into a single solid cylinder of thick rope (no loose strands) with four round stone weights tied at its ends; thick green vine bindings around the joints. Colours: dark wood brown, rope tan, stone grey, fresh vine green.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 4. Lính chặn: Vệ Binh Rêu (`moss-warden`)

| Mục | Giá trị |
|---|---|
| Là gì | Lính chặn của phe ta, đánh 12 VL / 1,2 s, hồi sinh 14 s (03 §9.2) |
| Cao thật | 1,7 m (lính 34–46 px) |
| Nhìn từ trên | Áo rêu tươi, mầm hai lá trên đầu, khiên tròn đan liễu, dải lam nhạt |
| Clip | Idle, Walk, Attack (đỡ khiên, quét chày), Death (ngã thành nụ cây: clip ngã + VFX nụ) |

**U1-F** · ảnh chính, nhìn thẳng · `units/moss-warden.png` · 1024×1536

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View and pose for 3D rigging: straight front view at chest height, near-orthographic, no perspective distortion, no tilt. Neutral A-pose: standing upright and facing the viewer, arms straight down and out 30 to 45 degrees from the body, elbows almost straight, legs straight and slightly apart, both feet flat on an invisible floor; a clear gap of empty background separates each arm from the body from the armpit down, and nothing touches an arm below the shoulder except an object gripped in that hand. Calm neutral expression, eyes open, mouth closed.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally: Moss Warden, a friendly blocker soldier of the Dragon's side, about 1.7 m tall, stout and sturdy, about 3 heads tall: a barrel body of living pale birch-like wood, short thick legs with rounded root-like feet, thick arms; a calm round face carved into the wood with two dark round painted eyes and a small kind mouth; a thick mantle of fresh green moss over the shoulders; a small fresh sapling sprout with two bright leaves on top of the head. In its left hand (on the viewer's right in a front view) it grips a big round shield of woven willow and bark with a pale cream rim, held by a side handle out to the side with the shield face toward the viewer, clear of the body; in its right hand (on the viewer's left in a front view) it grips a short thick wooden club pointing down. Colours: fresh moss green, pale birch cream, warm wood brown, and a soft pale sky-blue cloth sash across the chest (the colour of the Dragon's allies).
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

**U1-B** · ảnh phụ, nhìn sau · `units/moss-warden-back.png` · 1024×1536 · đính kèm: `units/moss-warden.png` (U1-F)

```text
Image-to-3D source picture of ONE character or creature for a stylized 3D defense game; it will be auto-rigged and animated later.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
Framing: exactly one character, the whole body from the top of the head to the soles of the feet, centred, with a small even empty margin on every side; nothing cut off.
View: this is an extra view of the same character as the attached front image (the approved main image of this item): identical design, colours, shell patches, proportions, A-pose and scale. Seen straight from behind, near-orthographic, camera at chest height; the character faces straight away from the camera, the head is not turned and the face does not show. Left and right are swapped compared with the front image: a part on the viewer's right in the front image is on the viewer's left here; every part stays on the same side of the character's own body.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally: Moss Warden, a friendly blocker soldier of the Dragon's side, about 1.7 m tall, stout and sturdy, about 3 heads tall: a barrel body of living pale birch-like wood, short thick legs with rounded root-like feet, thick arms; a calm round face carved into the wood with two dark round painted eyes and a small kind mouth; a thick mantle of fresh green moss over the shoulders; a small fresh sapling sprout with two bright leaves on top of the head. In its left hand (on the viewer's right in a front view) it grips a big round shield of woven willow and bark with a pale cream rim, held by a side handle out to the side with the shield face toward the viewer, clear of the body; in its right hand (on the viewer's left in a front view) it grips a short thick wooden club pointing down. Colours: fresh moss green, pale birch cream, warm wood brown, and a soft pale sky-blue cloth sash across the chest (the colour of the Dragon's allies).
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no floor shadow, no strong highlights, no rim light. Build: fur, moss, leaves, feathers and cloth grouped into a few big solid masses; no thin strands, wires, strings or gaps; nothing floating, every part touches the body; wings and cloth are solid and opaque, never see-through.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow or aura effects, motion lines, text, letters, numbers, logos, watermark, a frame, ground, grass, props lying around, a second view or a second character.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 5. Nhà phép: Lều Thuốc Nam (`herb-hut`)

| Mục | Giá trị |
|---|---|
| Là gì | Nhà hồi máu cho đồng minh và Rồng trong 7 m; Xung hồi 10 % (03 §8.2). Máu nhà 600 |
| Cỡ trong game | Rộng 4 m, cao 4 m (nhà 70–100 px) |
| Hoạt động | Giọt sáng lơ lửng bay tới đồng minh; hỏng thì nứt, khói, ánh tắt dần (05 §6.6) — đều là VFX |

**H1** · ảnh chính · `houses/herb-hut.png` · 1024×1024

```text
Image-to-3D source picture of ONE object for a stylized 3D defense game; it will become a static 3D model.
House style: stylized painterly 3D game art for a cozy storybook fantasy defense game set in a misty pine forest, like a hand-painted 3D figurine; hand-painted textures with soft visible brush strokes, chunky rounded shapes, a few large details instead of many small ones, and a chunky readable silhouette that still reads from a high top-down camera; soft forest palette of moss green, pine blue, muted violet and warm cream light; matte surfaces, no glossy shine.
View: three-quarter view, the object turned about 30 degrees so its front and its right side both show, looking down from about 30 degrees above, near-orthographic, no perspective distortion. Framing: the whole object from base to top, centred, with a small even empty margin on every side; nothing cut off. Its base is cut flat like a toy standing on a table: no ground, soil, grass, loose rocks or props around it, and no shadow under it.
Our side: this belongs to the Dragon's forest allies, healthy and bright; it has no ash-grey withered shell and no yellow-green cracks.
Ally building: Herb Hut, a small round healer's hut of the Dragon's side, about 4 m wide and 4 m tall: a low round wall of stacked rounded river stones at the bottom and woven willow above; a big domed roof of overlapping broad fresh-green leaves with pale cream midribs, laid in three big layers, with a small curled leaf tip on top; a round wooden door with a simple leaf carving; three thick bundles of dried herbs hanging close under the eaves; a big round clay pot with a lid beside the door; one round window with a pale sky-blue painted pane (paint, not glow). Colours: warm wood brown, river-stone grey, fresh moss green, cream, small pale sky-blue accents.
Colour rules: no large areas of bright red, orange, gold or turquoise anywhere; those colours are reserved for game signals.
Light: flat, even and frontal; no cast shadows, no strong highlights, no rim light. Build: one connected solid object; every part touches the main body and nothing floats; foliage, moss, thatch and cloth grouped into a few big rounded solid masses, each a little darker underneath; posts, ropes and branches thick and sturdy; no thin wires, strings, single needles, tiny scattered leaves or gaps.
Never draw: black outlines, fire, smoke, mist, sparks, particles, glow, light rays, motion lines, people, animals or creatures, text, letters, numbers, logos, watermark, a frame, a second view or a second object.
Background: plain flat very light neutral grey (#E6E6E6), perfectly uniform, no gradient, no vignette, no floor, no shadow.
```

## 6. Kiểm ảnh

- [ ] Một vật, thấy trọn, đáy cắt phẳng, không đất, không bóng; nền xám nhạt phẳng.
- [ ] Không dấu Héo (không vỏ xám tro, không nứt vàng úa).
- [ ] Lưới, dây leo, cọc dày và đặc; không sợi mảnh, không phần lơ lửng.
- [ ] Không lửa, khói, quầng sáng; cửa sổ lam là màu sơn.
- [ ] Không chữ, số, logo. Không màu giữ riêng thành mảng lớn.
