# Rồng Giữ Ải — M0 · 05. Icon HUD và cửa hàng (20 icon) (23/10/2026)

> **Dành cho:** AI điều khiển Codex CLI; AI làm UI sau. Không gửi Tripo.
> **Lấy từ:** `../../DESIGN.md` §9 M0 (Hỏa Long, bẫy, hỗ trợ, đồ tiêu hao, trang bị), §7.1 (icon từ Codex); `../../05-presentation-audio-tech-split.md` §4 (HUD, thẻ món 64 px, cờ báo đợt có icon họ quái), §2.2 (màu); `../../02-enemies-generals-bosses.md` §1.5 (hào quang địch: vàng úa, hoa văn và icon riêng mỗi loại buff).
> **Mục lục, thứ tự làm, thiết lập Tripo, nơi lưu GLB:** [`README.md`](README.md). Mỗi khối `text` là **một ảnh**: dán nguyên văn, không rút gọn, không thêm bớt. Các dòng chung giống từng chữ ở mọi prompt (README §5).

## 1. Luật chung

- Đọc được ở 32–64 px (thẻ món 64 px, ô kỹ năng, cờ báo đợt). Mỗi icon có **dáng riêng**, không chỉ khác màu (mù màu đỏ–lục, 05 §4.3).
- Nền khóa màu G, M, B như bộ TD, để cắt alpha. Icon có lá, rêu, vàng úa dùng M.
- Phe ta: lửa Hỏa Long **cam đào** (peach-coral), không dùng cam khẩn `#FFB020`, không đỏ. Vàng kim chỉ cho icon Vàng.
- Phe Héo: icon họ quái, huy hiệu tướng, hào quang dùng **vỏ xám tro + vàng úa `#C8D24A`** (02 §1.5).
- Icon món đã có ảnh nguồn Tripo đã duyệt (I01–I05): đính kèm ảnh đó và thêm dòng `BUILDREF` dưới đây ngay trước dòng nền.
- Thiếu icon thì game vẽ icon bằng canvas (05 §4.1), nên icon không chặn việc làm mã.

```text
Reference: the attached image shows this object or character. Keep its shape, materials and colours, simplified into a chunky icon; add only what is described.
```

**Tự quyết:** 20 icon M0 = 3 bẫy, 2 hỗ trợ, Bình Máu Nhỏ, Tim Rồng, Vảy Cứng, 4 kỹ năng Hỏa Long (Phun Lửa, Thiên Hỏa, Long Hống, Long Nộ / Viêm Đế), Vàng, 3 họ quái của M0 (Yêu Rêu, Thú Mục, Bọ Gai), huy hiệu tướng địch, 2 hào quang của G01 (tốc: chân gió; đòn: kiếm), Gọi sớm (tù và). Icon nhỏ trên thẻ chữ (vương miện, tia chớp, lá, bánh răng, loa) và nút hệ thống vẽ bằng SVG, không cần ảnh.

## 2. Bảng icon

Cột file bỏ tiền tố `games/dragon-hold/art-src/`.

| Mã | Icon | File | Nền |
|---|---|---|---|
| I01 | Gai Chông | `ui/icons/spikes.png` | M |
| I02 | Bom Hạt Thông | `ui/icons/pine-bomb.png` | M |
| I03 | Lưới Phóng | `ui/icons/net-launcher.png` | M |
| I04 | Vệ Binh Rêu | `ui/icons/moss-warden.png` | M |
| I05 | Nhà Thuốc Lá | `ui/icons/herb-hut.png` | M |
| I06 | Bình Máu Nhỏ | `ui/icons/potion-small.png` | M |
| I07 | Tim Rồng (trang bị) | `ui/icons/dragon-heart.png` | G |
| I08 | Vảy Cứng (trang bị) | `ui/icons/hard-scale.png` | G |
| I09 | Phun Lửa (Alt + 1) | `ui/icons/skill-fire-breath.png` | G |
| I10 | Thiên Hỏa (Alt + 2) | `ui/icons/skill-sky-fire.png` | G |
| I11 | Long Hống (Từ Khẩn) | `ui/icons/skill-roar.png` | G |
| I12 | Long Nộ / Viêm Đế | `ui/icons/skill-ultimate.png` | G |
| I13 | Vàng | `ui/icons/gold.png` | G |
| I14 | Họ Yêu Rêu | `ui/icons/family-moss.png` | M |
| I15 | Họ Thú Mục | `ui/icons/family-beast.png` | M |
| I16 | Họ Bọ Gai | `ui/icons/family-bug.png` | M |
| I17 | Huy hiệu tướng địch | `ui/icons/enemy-general.png` | M |
| I18 | Hào quang tốc (Xung Phong) | `ui/icons/aura-speed.png` | M |
| I19 | Hào quang đòn (Cắm Cờ) | `ui/icons/aura-attack.png` | M |
| I20 | Gọi sớm (tù và) | `ui/icons/call-wave.png` | G |

## 3. Prompt

### I01 · Gai Chông

**I01** · icon · `ui/icons/spikes.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Spike Bed trap: a short low wooden plank frame seen from slightly above with three rows of sharpened wooden stakes pointing up, pale carved tips, green vine bindings on the corners.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I02 · Bom Hạt Thông

**I02** · icon · `ui/icons/pine-bomb.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Pine-Cone Bomb trap: one fat warm-brown pine cone with chunky scales and small honey-amber resin beads, a short curled green vine fuse on top, sitting in a small twig cradle.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I03 · Lưới Phóng

**I03** · icon · `ui/icons/net-launcher.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Net Launcher trap: a chunky bent-wood launcher on a short thick post, holding a tightly rolled thick rope net with round stone weights at its ends.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I04 · Vệ Binh Rêu

**I04** · icon · `ui/icons/moss-warden.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Moss Warden ally soldier: head and shoulders of a friendly stout wooden guardian with a calm carved face, dark round eyes, a fresh green moss mantle and a two-leaf sapling sprout on its head, its round woven willow shield raised in front of one shoulder, a soft pale sky-blue sash.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I05 · Nhà Thuốc Lá

**I05** · icon · `ui/icons/herb-hut.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Herb Hut healer building: a small round hut with a stone base, a domed roof of broad fresh-green leaves, a round wooden door, a bundle of dried herbs under the eaves and one small pale sky-blue window.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I06 · Bình Máu Nhỏ

**I06** · icon · `ui/icons/potion-small.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Small Health Tonic: a small round glass bottle with a cork stopper, filled with fresh leaf-green tonic, a small green leaf tied to its neck with twine.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I07 · Tim Rồng (trang bị)

**I07** · icon · `ui/icons/dragon-heart.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Dragon Heart charm (equipment): a heart-shaped polished gemstone in warm peach-coral with a cream inner highlight, set in a round carved wooden amulet frame with a pattern of small dragon scales.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I08 · Vảy Cứng (trang bị)

**I08** · icon · `ui/icons/hard-scale.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Hard Scale (equipment): one big thick dragon scale shaped like a rounded shield, warm peach-coral with a cream rim and three carved grooves, a small leather loop at the top.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I09 · Phun Lửa (Alt + 1)

**I09** · icon · `ui/icons/skill-fire-breath.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Fire Breath skill: a wide cone of rolling dragon fire bursting from the left toward the right, chunky rounded flame tongues in peach-coral and warm cream, darker coral at the edges.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I10 · Thiên Hỏa (Alt + 2)

**I10** · icon · `ui/icons/skill-sky-fire.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Sky Fire skill: a round ball of peach-coral fire with a short cream tail, falling diagonally from the upper right onto a small cracked ring of ground at the lower left.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I11 · Long Hống (Từ Khẩn)

**I11** · icon · `ui/icons/skill-roar.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Dragon Roar skill: three bold curved shock-wave arcs in cream white with peach-coral edges, spreading to the right from a small stylized open dragon mouth in profile on the left.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I12 · Long Nộ / Viêm Đế

**I12** · icon · `ui/icons/skill-ultimate.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Dragon Fury ultimate: a tall blazing peach-coral flame shaped like a rearing dragon head, with a small three-pointed cream crown of fire on top.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I13 · Vàng

**I13** · icon · `ui/icons/gold.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Gold currency: a small stack of three thick round gold coins with soft rims and a simple pine-cone emblem embossed on the top coin (no letters, no numbers).
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### I14 · Họ Yêu Rêu

**I14** · icon · `ui/icons/family-moss.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Moss-goblin enemy family: a carved bark mask with two round eye holes and a jagged mouth slit, a dry dusty-sage moss cap on top, one ash-grey shell patch on its corner with a thin bright withered yellow-green (#C8D24A) crack; the eyes are withered yellow-green.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I15 · Họ Thú Mục

**I15** · icon · `ui/icons/family-beast.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Beast enemy family: a wolf's head in three-quarter view, smoky grey-brown fur, an ash-grey shell plate on the forehead with a thin bright withered yellow-green (#C8D24A) crack, withered yellow-green eyes, mouth closed.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I16 · Họ Bọ Gai

**I16** · icon · `ui/icons/family-bug.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Bug enemy family: the round head of a thorn wasp in front view, deep pine-blue chitin, big rounded compound eyes in withered yellow-green (#C8D24A), short thick antennae and three short black thorns on top.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I17 · Huy hiệu tướng địch

**I17** · icon · `ui/icons/enemy-general.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: Enemy General badge: a rugged shield-shaped badge of ash-grey withered shell with a silver rim, one thin bright withered yellow-green (#C8D24A) crack across it and a short ragged ash-grey pennant on a stub pole rising from its top.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I18 · Hào quang tốc (Xung Phong)

**I18** · icon · `ui/icons/aura-speed.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: enemy aura of speed: a stylized running foot with three swept wind streaks behind it, painted in bright withered yellow-green (#C8D24A) on a round ash-grey stone token.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I19 · Hào quang đòn (Cắm Cờ)

**I19** · icon · `ui/icons/aura-attack.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: enemy aura of attack: a short broad stone blade pointing up, painted in bright withered yellow-green (#C8D24A) on a round ash-grey stone token.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

### I20 · Gọi sớm (tù và)

**I20** · icon · `ui/icons/call-wave.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Hand-painted game icon for the HUD and shop of a cozy storybook fantasy defense game set in a misty pine forest: one single object, centred, filling about 80% of the square, slight three-quarter front view, chunky simplified shapes with very few details, painterly brush texture, a soft dark-brown outline thick enough to survive shrinking to 32 px, two or three tones per colour plus one small soft highlight, strong value contrast so it reads on both dark carved wood and cream parchment. No background shapes, no badge or circle behind the object unless the object itself is a badge, no frame, no cast shadow, no text, no letters, no numbers. Square 1024 x 1024.
Icon: call the next wave early: a curved forest war horn of pale horn with dark wood bands and a leather strap, its wide mouth pointing up to the right.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

## 4. Kiểm ảnh

- [ ] Một vật, chiếm khoảng 80 % ô, thu còn 32 px vẫn nhận ra.
- [ ] Không vòng, khung, huy hiệu sau vật (trừ khi vật là huy hiệu hay thẻ đá); không bóng đổ.
- [ ] Nền đúng mã, phẳng; vật không chứa màu của nền.
- [ ] Không chữ, số. Không đỏ; cam đào cho lửa phe ta; vàng úa chỉ cho phe Héo.
