# Rồng Giữ Ải — M0 · 04. Ảnh 2D dùng thẳng: 8 ô đất, 4 tấm decal, phông xa (23/10/2026)

> **Dành cho:** AI điều khiển Codex CLI; AI viết `prepare-ground.mjs`, `prepare-decals.mjs` sau. Không gửi Tripo.
> **Lấy từ:** `../../research/art-pipeline.md` §2.2–2.3 (đất trộn rồi nướng, luật ô đất và decal), §9 (thành phần kit); `../../05-presentation-audio-tech-split.md` §2 (bậc nổi: đường sáng hơn đất một bậc, cảnh giảm tương phản).
> **Mục lục, thứ tự làm, thiết lập Tripo, nơi lưu GLB:** [`README.md`](README.md). Mỗi khối `text` là **một ảnh**: dán nguyên văn, không rút gọn, không thêm bớt. Các dòng chung giống từng chữ ở mọi prompt (README §5).

## 1. Luật chung

- **Ô đất:** nhìn thẳng từ trên, trực giao, ánh sáng phẳng, không bóng, nét cọ to, lặp liền mép, không vật đứng, không lối đi, 1024² (art-pipeline §2.3). Không có dòng nền: hoa văn phủ kín ảnh.
- **Decal:** mỗi ảnh là một tấm 2 × 2 (4 decal), nhìn từ trên, nền khóa màu (G, M, B như bộ TD), mép đặc. Script nở màu viền 8 px.
- **Phông xa:** dải núi rừng rất xa, chân trời ngang; hai mép 8 % yên để ghép và lật gương; sống núi gần nhất chạm hai mép ở 62 % chiều cao.
- Đất **giảm bão hòa, tương phản thấp** để quái và thẻ chữ nổi (bậc nổi 05 §2.1). Không đỏ, cam, vàng kim, xanh ngọc, **không vàng úa** (màu phe Héo).
- Sau khi tạo: `prepare-ground.mjs` (việc mới) đo lệch mép, sửa mép, kéo màu về bảng kit, xuất ảnh 2 × 2 cho chủ dự án xem.

## 2. Bảng ảnh

Cột file bỏ tiền tố `games/dragon-hold/art-src/`.

| Mã | Ảnh | File | Khổ |
|---|---|---|---|
| T1 | Cỏ xuân A (chính) | `ground/pine-river/grass-a.png` | 1024×1024 |
| T2 | Cỏ xuân B (trộn với A) | `ground/pine-river/grass-b.png` | 1024×1024 |
| T3 | Rêu dưới tán | `ground/pine-river/moss.png` | 1024×1024 |
| T4 | Lối mòn (đường quái, sáng hơn cỏ một bậc) | `ground/pine-river/path.png` | 1024×1024 |
| T5 | Đất nện (quanh Bệ Rồng, ô xây) | `ground/pine-river/earth.png` | 1024×1024 |
| T6 | Cát ven suối | `ground/pine-river/river-sand.png` | 1024×1024 |
| T7 | Đá rêu (dốc > 35°, chiếu ba mặt) | `ground/pine-river/rock.png` | 1024×1024 |
| T8 | Lá thông rụng (rìa rừng) | `ground/pine-river/pine-litter.png` | 1024×1024 |
| D1 | Decal vết đất (G) | `decals/pine-river/dirt-patches.png` | 1024×1024 |
| D2 | Decal cụm hoa (B) | `decals/pine-river/flower-clusters.png` | 1024×1024 |
| D3 | Decal sỏi, lá, kim thông, cành (G) | `decals/pine-river/forest-litter.png` | 1024×1024 |
| D4 | Decal rêu, vũng nước (M) | `decals/pine-river/moss-puddles.png` | 1024×1024 |
| B1 | Phông xa rừng thông | `backdrops/pine-river-far.png` | 1536×1024 |

## 3. Ô đất

### T1 · Cỏ xuân A (chính)

**T1** · ô lặp · `ground/pine-river/grass-a.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Spring Grass A, the main grass of the pine-forest meadows: short fresh moss-green grass painted as soft overlapping brush-stroke tufts in two or three close greens, with a few lighter sage-green strokes.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T2 · Cỏ xuân B (trộn với A)

**T2** · ô lặp · `ground/pine-river/grass-b.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Spring Grass B, a variation that mixes with grass A: slightly deeper and cooler blue-green grass with a few small round clover clumps painted flat, in the same brush style.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T3 · Rêu dưới tán

**T3** · ô lặp · `ground/pine-river/moss.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Forest Moss, the floor under the pine crowns: thick deep-green cushion moss painted as soft rounded blobs of different sizes, with darker pine-blue-green between them.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T4 · Lối mòn (đường quái, sáng hơn cỏ một bậc)

**T4** · ô lặp · `ground/pine-river/path.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Worn Path, the dirt of the enemy paths, one step lighter than the grass: warm light sandy-brown packed soil with soft footworn streaks, a few tiny pale pebbles and faint darker patches; no wheel ruts, no footprints.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T5 · Đất nện (quanh Bệ Rồng, ô xây)

**T5** · ô lặp · `ground/pine-river/earth.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Packed Earth, the bare ground around the Dragon's dais and the building plots: darker warm loam brown with soft clumps and a few tiny grey pebbles.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T6 · Cát ven suối

**T6** · ô lặp · `ground/pine-river/river-sand.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: River Sand, the stream banks: pale cream-grey sand with soft rippled bands and small scattered blue-grey pebbles; dry, no water.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T7 · Đá rêu (dốc > 35°, chiếu ba mặt)

**T7** · ô lặp · `ground/pine-river/rock.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Mossy Stone, for steep slopes and cliff faces: flat layered blue-grey slate slabs with soft seams between them and small patches of moss in the seams, painted flat with no depth shading.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

### T8 · Lá thông rụng (rìa rừng)

**T8** · ô lặp · `ground/pine-river/pine-litter.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Seamless tileable ground texture for a painterly 3D game terrain, seen straight from above, orthographic, filling the whole square edge to edge; the pattern continues cleanly across all four edges, with no visible seam when tiled. Flat, even, shadowless light: no sun direction, no cast shadows, no highlights. Big soft hand-painted brush strokes, low contrast and medium-low detail so characters and word labels on top stay readable. No standing objects, no paths, no stones bigger than a fist, no border, no vignette, no text, no letters, no watermark. Square 1024 x 1024.
Tile: Pine Litter, the forest floor at the edges of the map: a soft carpet of fallen warm-brown pine needles painted as short grouped strokes, with patches of dark soil and a few small dull-green moss spots; no whole pine cones, no branches.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

## 4. Decal

### D1 · Decal vết đất (G)

**D1** · tấm 2 × 2 · `decals/pine-river/dirt-patches.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Ground decal atlas for a painterly 3D game, seen straight from above, orthographic: exactly 4 separate decals in a 2 x 2 grid on a square 1024 x 1024 image, each centred in its own 512 x 512 quarter with at least 48 px of empty background around it; no decal touches another or a quarter border; no grid lines. Each decal is a flat painted patch lying on the ground with an irregular organic outline and a crisp solid edge; softness is painted inside the shape as two or three tone bands, never blurred into the background. Flat shadowless light, no cast shadows, no highlights. Hand-painted storybook brush strokes. No text, letters, numbers or labels.
Decals: Dirt Patches: four different irregular patches of bare warm-brown earth, one round, one long and narrow, one kidney-shaped and one ragged, each with a slightly darker centre and a few tiny pebbles inside.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### D2 · Decal cụm hoa (B)

**D2** · tấm 2 × 2 · `decals/pine-river/flower-clusters.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Ground decal atlas for a painterly 3D game, seen straight from above, orthographic: exactly 4 separate decals in a 2 x 2 grid on a square 1024 x 1024 image, each centred in its own 512 x 512 quarter with at least 48 px of empty background around it; no decal touches another or a quarter border; no grid lines. Each decal is a flat painted patch lying on the ground with an irregular organic outline and a crisp solid edge; softness is painted inside the shape as two or three tone bands, never blurred into the background. Flat shadowless light, no cast shadows, no highlights. Hand-painted storybook brush strokes. No text, letters, numbers or labels.
Decals: Wildflower Clusters seen from above: four different low clusters of small flowers among a few broad leaves: cream-white daisies, pale violet bellflowers, a mix of both, and tiny cream star flowers; the flowers are grouped in chunky clumps, not single tiny petals.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
Flat pure #0000FF blue background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no blue at all.
```

### D3 · Decal sỏi, lá, kim thông, cành (G)

**D3** · tấm 2 × 2 · `decals/pine-river/forest-litter.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Ground decal atlas for a painterly 3D game, seen straight from above, orthographic: exactly 4 separate decals in a 2 x 2 grid on a square 1024 x 1024 image, each centred in its own 512 x 512 quarter with at least 48 px of empty background around it; no decal touches another or a quarter border; no grid lines. Each decal is a flat painted patch lying on the ground with an irregular organic outline and a crisp solid edge; softness is painted inside the shape as two or three tone bands, never blurred into the background. Flat shadowless light, no cast shadows, no highlights. Hand-painted storybook brush strokes. No text, letters, numbers or labels.
Decals: Forest Litter: four scatter groups lying flat on the ground: a loose ring of small grey pebbles, a drift of fallen warm-brown leaves, a small heap of brown pine needles with two small pine cones, and a few short broken twigs.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
Flat pure #00FF00 green background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no green at all.
```

### D4 · Decal rêu, vũng nước (M)

**D4** · tấm 2 × 2 · `decals/pine-river/moss-puddles.png` · 1024×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Ground decal atlas for a painterly 3D game, seen straight from above, orthographic: exactly 4 separate decals in a 2 x 2 grid on a square 1024 x 1024 image, each centred in its own 512 x 512 quarter with at least 48 px of empty background around it; no decal touches another or a quarter border; no grid lines. Each decal is a flat painted patch lying on the ground with an irregular organic outline and a crisp solid edge; softness is painted inside the shape as two or three tone bands, never blurred into the background. Flat shadowless light, no cast shadows, no highlights. Hand-painted storybook brush strokes. No text, letters, numbers or labels.
Decals: Moss and Puddles: two different soft patches of deep-green moss and two shallow muddy puddles with calm muted blue-grey water and a darker wet-earth rim; no reflections, no turquoise.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
Flat pure #FF00FF magenta background, perfectly uniform, no gradient, no shadow, no glow on it; the subject contains no pink, magenta or bright purple at all.
```

## 5. Phông xa

**B1** · dải phông · `backdrops/pine-river-far.png` · 1536×1024

```text
House style: hand-painted storybook fantasy art for a cozy defense game set in a misty pine forest; painterly brush strokes, chunky rounded shapes, soft forest palette of moss green, pine blue, muted violet and warm cream light; matte, calm and readable.
Backdrop strip for a 3D game: one wide band of very distant scenery that wraps around the play area, seen straight ahead at a level horizon: no tilt, no fisheye, no perspective lines. Soft even morning light, no strong shadows, no sun disc. Atmospheric haze: farther ridges are paler, bluer and softer. Large calm shapes, no small busy detail, no people, no animals, no buildings. The left 8% and the right 8% of the image are calm and plain, and the nearest ridge line meets both side edges at exactly 62% of the image height from the top, so tiles join side by side and also when mirrored. Landscape 1536 x 1024.
Scene: the far edge of the Great Misty Forest: three or four layers of rolling mountain ridges covered in rounded pine forest, the nearest ridge pine blue with muted violet shadows, the farther ridges paler lavender-blue fading into soft haze; above them a calm pale cream morning sky with a faint warm glow near the horizon and two or three soft flat cream clouds high up.
Colour rules: no bright red, orange, gold, turquoise or bright yellow-green anywhere; those colours are reserved for game signals.
```

## 6. Kiểm ảnh

- [ ] Ô đất: phủ kín, không viền, không vật đứng, không bóng; ghép 2 × 2 không thấy mép (script đo).
- [ ] Lối mòn sáng hơn cỏ một bậc; cỏ và rêu không quá bão hòa.
- [ ] Decal: đúng 4 mảnh, không chạm nhau, không chạm mép ô, mép đặc; nền đúng mã.
- [ ] Phông: chân trời ngang, hai mép yên, sống núi gần chạm mép ở cùng độ cao; không người, nhà, mặt trời.
- [ ] Không chữ, không màu giữ riêng, không vàng úa.
