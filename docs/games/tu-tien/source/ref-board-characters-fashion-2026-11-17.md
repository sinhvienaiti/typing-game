# Character and fashion reference board (17/11/2026)

Owner, 17/11: "nên tham khảo các mẫu dựa trên các dạng game đang hot của tu tiên … phần thiết kế thời trang rất quan trọng, sau này sẽ có thể đổi quần áo của nhân vật".

Boards (third-party, owner review only, **never fed to any AI tool**):
`typing-game-review/owner-review/2026-11-17/tu-tien/ref-board-characters/` — `board-heroines.jpg` (H01–H12), `board-fashion-systems.jpg` (F01–F10), `board-monsters.jpg` (M01–M12).

## Summary (≤300 words)

Seven games covered: Honkai: Star Rail (Xianzhou), Genshin Impact (Liyue), Wuthering Waves (Jinzhou), Naraka: Bladepoint, Where Winds Meet, Black Myth: Wukong, plus Genshin/HSR bosses. The best heroines share four traits. (1) One strong silhouette read: long hair mass or a hair ornament plus a long trailing element (ribbon, sash, cape tail, split skirt panel) that moves. (2) Three-value colour split, roughly 60 % base (white, black, deep blue), 30 % secondary, 10 % accent (gold trim, red tassels); Jingliu, Shenhe and Jinhsi are the model. (3) Layering: fitted inner layer, open outer layer, and translucent gauze on top; detail clusters at the waist (belt, jade pendants, knots) and shoulders, which is exactly what a 55° camera sees. (4) Radiance tied to the element (Jingliu's moon frost, Fu Xuan's formation glyphs). Naraka shows the fashion model we need: one body and face, many full outfits that each change palette, hem shape and head piece but keep the same sword arm and pose — proof that skins sell on silhouette change, not tiny detail. Where Winds Meet adds realistic dyeable hanfu and a wardrobe screen next to the build. Black Myth monsters read through one giant exaggerated feature (horns, eyes, armour mass) and a strong colour key; bosses add scale, an aura and props; elites are recolour and armour-up of the base beast. Recommendation: plan the heroine as a shared skeleton with full-outfit meshes plus head-piece and back-piece slots and dye channels, not as fine per-part armour slots; at our camera the hem, sleeves, hair and back piece carry the read.

## Per-game table

| Game | What to learn | Links |
| --- | --- | --- |
| Honkai: Star Rail (Xianzhou) | Element-coded palettes, flowing hair and sashes, formation glyph radiance (Jingliu, Feixiao, Yunli, Fu Xuan); boss Phantylia | honkai-star-rail.fandom.com/wiki/Jingliu, /Feixiao, /Yunli, /Fu_Xuan, /Phantylia |
| Genshin Impact (Liyue) | Clean 60/30/10 colour, red-tassel and gold accents, outfit skins that keep the hero's read (Keqing, Ganyu, Ningguang); Azhdaha boss silhouette | genshin-impact.fandom.com/wiki/Shenhe, /Keqing, /Opulent_Splendor, /Twilight_Blossom, /Orchid%27s_Evening_Gown, /Azhdaha |
| Wuthering Waves | Modern-luxe hanfu: white plus one teal or red, gold hardware, asymmetry (Jinhsi, Changli, Jianxin) | wutheringwaves.fandom.com/wiki/Jinhsi, /Changli, /Jianxin |
| Naraka: Bladepoint | Skin economy: one hero, many full outfits with distinct palette and hem; realistic fabric (Viper Ning skins); Temulch | narakabladepoint.fandom.com/wiki/Viper_Ning, /Temulch |
| Where Winds Meet | Realistic dyeable hanfu, hair ornaments, wardrobe beside the build screen | where-winds-meet.fandom.com/wiki/File:AnLiuLi.jpg, File:BaiChuyu.jpg, File:Develop_WWM-main_interface.png |
| Black Myth: Wukong | Shan hai jing yaoguai: one exaggerated feature, strong colour key, boss scale and props | blackmythwukong.fandom.com/wiki/Yellowbrow, /Erlang_Shen, /Hundred-Eyed_Daoist_Master, /Tiger_Vanguard, /Kang-Jin_Loong, /Lingxuzi, /Black_Bear_Guai, /Yellow_Wind_Sage, /Red_Loong |

Not covered as images (no clean wiki assets reachable without sign-in): Justice Online, Moonlight Blade, Swords of Legends Online. Their known lesson (full-set fashion plus free dye channels) is folded into the slot plan.

## Proposed outfit slot system (heroine)

One shared skeleton (humanoid canonical bones per `game-character-animation`) plus spring chains for hair, sleeves, sash tails, skirt panels and back piece. Body and head are fixed; outfits swap on top.

| Slot | Kind | Notes |
| --- | --- | --- |
| Body base (skin, face) | Fixed mesh | Hidden faces under each outfit are masked out by a per-outfit body mask |
| Hair style | Separate mesh, swappable | Own spring chain; dye channel 1 |
| Head ornament (crown, pins, veil) | Separate mesh | Biggest read from 55°; carries presence glow |
| Outfit set (inner + outer robe + sleeves + skirt) | **One skinned mesh per set** | Avoids clipping between independent robe parts; 3 dye channels (base, secondary, trim) via a mask texture |
| Belt / waist ornaments (jade, tassels) | Separate mesh, socket to waist | Mix and match across sets |
| Back piece (cape, sash halo, sword sheath, mandorla) | Separate mesh or VFX | Main silhouette changer from above |
| Shoes / greaves | Part of set mesh at launch | Split later only if a shop needs it |
| Weapon (sword) | Separate mesh, hand socket | Skins plus its own presence layer |
| Aura / presence kit | Engine VFX | Per-outfit tint preset (game-hero-presence-vfx) |

Layering and clipping rules: order body → set → belt → back piece → hair → head ornament; every set mesh ships with its body mask and is tested in the motion lab with all clips; capes and skirt tails are spring chains with body colliders (pelvis, thighs); no slot may exceed the set's bounding silhouette by more than its design intends; a dye only changes the mask channels, never trim emissive.

Launch plan: 1 default plus 3 full outfit sets (one per chosen direction's palette), 3 dye presets each, 2 hair styles, 3 head ornaments, 2 back pieces, 2 sword skins; the slot code supports more without rework.

## Heroine directions (owner picks one)

1. **Moon-frost sword immortal** — white and pale blue robes with silver trim, long silver-white hair, translucent gauze outer layer, crescent hair crown, a floating sword-halo back piece. Calm, divine, high-contrast against dark maps (cf. Jingliu, Shenhe).
2. **Modern-luxe jade cultivator** — fitted white inner dress, open teal-and-black outer robe, gold hardware, jade pendants at the waist, long split sash tails, black hair in a high tied style with gold pins. Fashionable and easy to reskin (cf. Jinhsi, Jianxin, WWM).
3. **Crimson phoenix blade** — black-and-red layered hanfu, gold embroidery, red tassels, a feather-like cape and a phoenix head ornament; fiercer and warmer, strongest silhouette from above (cf. Changli, Naraka skins).

## Monster directions (owner picks one)

1. **Shan hai jing ink-myth beasts** — mythic animals (nine-tailed fox, taotie, qilin, bi fang bird) with one exaggerated feature each, ink-wash colour key with a single element glow; elites add armour plates and a ring aura, bosses grow scale, extra heads or tails and a formation under them (cf. Black Myth, Azhdaha).
2. **Demonic cultivator yaoguai** — humanoid and half-beast demons in tattered robes and bronze armour, masks, many eyes or horns, corrupted purple-red qi; reads at small size through a bright weak-point glow and big headgear; bosses carry props and phase changes (cf. Yellowbrow, Hundred-Eyed Daoist, Tiger Vanguard).
