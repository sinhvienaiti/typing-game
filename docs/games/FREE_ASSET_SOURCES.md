# Free asset sources for Dragonhold, Wordwoven and Last Line

Researched 01/11/2026 by Claude (free-asset researcher), after the owner's message about the maps of all three games. Every licence below was read on the source page or in the repo's LICENSE file on 01/11/2026 unless the row says otherwise. Nothing was downloaded (one HEAD request checked that a Unity Labs link still answers).

Read with: `docs/games/THIRD_PARTY.md` (what is in use), `docs/games/vfx/PACKS.md` (VFX packs already evaluated), `docs/games/SHARED_SYSTEMS_BAR.md` §5 (allowed licences), `docs/tools/MAP_FACTORY.md` §4.5 (current rule on third-party models).

## Tóm tắt (tiếng Việt)

1. **Vì sao cảnh trông như đồ chơi, phần nguồn miễn phí sửa được.** Cả ba game chiếu sáng bằng `RoomEnvironment` (một phòng studio giả, `shared/game-kit/three/stage.ts` dòng 98–99, Dragonhold thêm ở `src/view/heroes.ts` dòng 353–354). Không game nào nạp HDRI, `Sky`, `Water`, `CSM`, SMAA hay TAA, dù three 0.170 đã có sẵn tất cả (MIT). Ảnh tham chiếu của chủ dự án là cảnh gần như ảnh thật: vách đá thật, mây tích, nắng gắt, vật liệu PBR dày chi tiết. Muốn tới đó cần ánh sáng HDRI, vật liệu quét thật và mây, lửa render thật, không phải thêm model low-poly.
2. **Gần mức tham chiếu nhất (CC0, dùng thương mại, không cần ghi công):** Poly Haven (HDRI, đá, vách, cây quét thật), ambientCG và cgbookcase (vật liệu PBR), flipbook Unity Labs (28 chuỗi khói, lửa, nổ render HDR, CC0) và VDB JangaFX (CC0, render bằng Blender ra flipbook). Cho Last Line: ảnh ESA/Webb và ESA/Hubble (CC BY 4.0, phải ghi công từng ảnh).
3. **Hướng vẽ tay:** Quaternius Stylized Nature MegaKit (kiểu Ghibli), texture màu nước Voxel Core Lab (CC0), texture vẽ tay của rubberduck trên OpenGameArt (CC0). **Quaternius có giấy phép không nhất quán:** trang gói ghi CC0, trang giấy phép (cập nhật 28/8/2026) ghi Quaternius Asset License v1.0. Phải coi như QAL: dùng trong game thương mại được, không cần ghi công, cấm phát lại thành gói tài sản.
4. **Kenney, KayKit, Poly Pizza là low-poly màu phẳng**, đúng cái chủ dự án chê là đồ chơi. Chỉ dùng để dựng thô bố cục, không ship làm nền chính.
5. **Mã:** dùng ngay được three r170 (`Sky`, `Water2`, `GroundedSkybox`, `CSM`, `GTAOPass`, `SMAAPass`, `TAARenderPass`, `LUTPass`, `RGBELoader`/`EXRLoader`/`UltraHDRLoader`, `KTX2Loader`); `three-custom-shader-material` (MIT, gió cho cây cỏ, trộn đất); `@pmndrs/vanilla` (MIT: sàn phản chiếu, nón sáng thể tích, mây, sprite flipbook); Quick_Grass của SimonDev (MIT, cỏ kiểu Ghost of Tsushima); `three.terrain.js` (MIT). **pmndrs `postprocessing` là Zlib**, nằm ngoài danh sách §5, và N8AO, `three-good-godrays`, mây/khí quyển Takram đều cần nó: chủ dự án quyết.
6. **Luật cần chủ dự án xác nhận:** (a) ship model bên thứ ba hiện đang trái luật (`MAP_FACTORY.md` §4.5; `games/dragon-hold/AGENTS.md`: "Real models come from the owner as GLB"). Lời chủ dự án ngày 01/11 ("có thể dùng các loại tài nguyên, thư viện, source có sẵn…") có thể là đổi luật này, nhưng cần xác nhận rõ. (b) §5 chỉ cho tài sản CC0 hoặc CC-BY. QAL, ShareTextures "Custom CC0", CMU, Fab Standard, Sketchfab Standard và Mixamo đều là giấy phép riêng, nằm ngoài danh sách. (c) Mỗi gói tải về cần chủ dự án đồng ý (tên, nguồn, giấy phép, dung lượng).
7. **AI:** không đưa vào ChatGPT hay Tripo các model gắn NoAI hoặc theo giấy phép Standard (Sketchfab, Fab), file Mixamo, hay thứ lấy từ dịch vụ Poly Pizza (điều khoản cấm dùng dịch vụ để huấn luyện AI). Ảnh chụp tài sản CC0 thì gửi làm tham chiếu được.
8. Mười nguồn nên thử trước cho từng game ở §11.

## 0. Rules this list is checked against

| Rule | Where | What it means here |
|---|---|---|
| Allowed licences | `SHARED_SYSTEMS_BAR.md` §5 | Code: MIT, BSD, ISC, Apache-2.0, MPL-2.0. Assets: CC0; CC-BY only with full credit on the game's Credits page. Not allowed: NC, ND, GPL family when modified/linked statically, "free"/"royalty-free" without a clear licence. Custom licences (QAL, Fab Standard, CMU, Mixamo, ShareTextures) are **outside the list**: the owner must accept each one explicitly. |
| Download approval | `SHARED_SYSTEMS_BAR.md` §5 | Each asset pack needs the owner's OK before download (name, source, licence, size). Code packages via pnpm are routine. |
| Third-party models in shipped games | `docs/tools/MAP_FACTORY.md` §4.5, §5; `games/dragon-hold/AGENTS.md` | Currently not allowed ("Real models come from the owner as GLB"; Poly Haven/Kenney/Quaternius in a shipped game "Khi chủ dự án đổi luật model"). The owner's 01/11 message may change this; confirm before shipping any model below. Textures, HDRIs, flipbooks and code are not blocked by this rule. |
| No code-drawn stand-ins | `AGENTS.md` (owner, 28/10) | Procedural trees (ez-tree) are props built in code: flagged. Grass, water, sky and terrain shaders are in the allowed list (shaders, instancing, procedural terrain) as long as they reach the art bar. |
| No media in Git | memory, game AGENTS | Downloaded packs live outside the repos (as `~/VFXLab/packs/` does today), with a `media.md5` pointer. |
| Licence version date | `MAP_FACTORY.md` §4 (QAL §7) | Record the download date and pack version in `THIRD_PARTY.md`; QAL says the version in force when you obtained the asset applies. |

## 1. Already in use or already reviewed (not repeated below)

| Item | Status | Source of record |
|---|---|---|
| three.js 0.170.0 (MIT) | All three games. Add-ons used: `EffectComposer`, `RenderPass`, `UnrealBloomPass`, `OutputPass`, `RoomEnvironment`; Dragonhold and Wordwoven add `FXAAShader`; Wordwoven adds `GTAOPass`; Last Line adds `BufferGeometryUtils`. No HDRI, `Sky`, `Water`, `CSM`, SMAA or TAA anywhere. | `THIRD_PARTY.md`; grep of `src/` 01/11 |
| Kenney Particle Pack, Kenney Smoke Particles (CC0) | In Dragonhold fire C (`main` `e1ed394`) | `THIRD_PARTY.md`, `vfx/PACKS.md` |
| SEAMPROOF Pyroclast free sample, SCORCH free sampler, AD_FX FREE 01, Taproot decals | Downloaded 31/10 for evaluation; judged procedural blobs, not used | `vfx/PACKS.md` |
| Mesh2Motion rigs and clips (CC0; app MIT) | Wordwoven Blender rig pipeline; dragon/fox/horse/spider/kaiju rigs await download approval | `THIRD_PARTY.md` |
| Quaternius UAL 1 and 2 (Standard) | Proposed, awaiting download approval; see the QAL note in §3 | `THIRD_PARTY.md` |
| Mixamo | Not default (raw-file and ML clauses; official FAQ still 403 on 01/11) | `THIRD_PARTY.md` |
| `@three.ez/instanced-mesh`, Kenney Animated Characters, OpenVAT | Reviewed, not used | `THIRD_PARTY.md` |
| pmndrs `postprocessing` (Zlib) | Flagged "outside §5" by TF2 on 29/10 | `THIRD_PARTY.md` |
| Poly Haven, Kenney, Quaternius, KayKit, ambientCG, Styloo | Reviewed for the Map Factory: "dựng thô", "không ship" under the current model rule | `MAP_FACTORY.md` §4.5 |

## 2. Style fit against the owner's reference

The reference (`games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp`) is a near-photoreal fantasy MMO frame: sun-lit sandstone mesas with real erosion detail, volumetric cumulus over a deep blue sky, warm key light with cool sky fill, dense PBR props (water wheel, tents, scaffolds), a highly detailed creature. Three style tiers among free sources:

| Tier | Sources | Fit to the reference | Where it belongs |
|---|---|---|---|
| Realistic, scanned PBR | Poly Haven models, textures and HDRIs; ambientCG; cgbookcase; Sketchfab photogrammetry (CC0/CC-BY); Unity Labs and JangaFX rendered fire/smoke; ESA/Webb/Hubble photos | **Closest.** Gives real rock, ground, sky light and fire. | Terrain, cliffs, rocks, ground, sky, IBL, water, VFX, Last Line space vistas. Risk: Tripo models are painterly with 1024² textures; next to scans they show two texel densities (`MAP_FACTORY.md` §4.5). Unify with the same HDRI, a shared LUT grade, and by keeping scans mostly at mid and far range. |
| Painterly / stylized-detailed | Quaternius Stylized Nature MegaKit (Ghibli-inspired, textured); Voxel Core Lab watercolor textures; rubberduck hand-painted textures (OGA) | Medium. Charming, not "epic"; closer to the Tripo look. | Wordwoven meadow and village if the art direction stays stylized; flowers, bushes, understory. |
| Low-poly, flat colour, gradient atlas | Kenney kits, KayKit, Poly Pizza (Google Poly) | **Poor.** This is the "toy" look the owner rejected. | Grey-box layout only, never in the shipped view. |

## 3. 3D models

| Source | Licence | Verified on source page (01/11) | Good for | Style fit | Risks |
|---|---|---|---|---|---|
| **Poly Haven models** | CC0 | https://polyhaven.com/license: "Our assets are all licensed as CC0"; "You can use our assets for any purpose"; "You do not need to give credit". Example https://polyhaven.com/a/rock_face_01: CC0, 20K tris, textures 1K–8K, glTF/Blend/FBX, category Nature > Rocks & Stone > Cliffs & Rock Faces. | **DH:** cliffs, boulders, rock faces, river stones, pine forest pieces (Collections page lists a Pine Forest collection). **WW:** rocks, logs, ferns for the meadow edge. **LL:** a few industrial props. | Realistic scanned | Heavy: 20K–866K tris per asset (coastal cliff 866K per the asset page in search); decimate in Blender, meshopt, KTX2. Terms forbid "Web scraping or data mining without express permission": download by hand, never script the API. Mixed style next to Tripo models. Shipping models needs the owner's rule change (§0). |
| **Quaternius** (Stylized Nature MegaKit, Modular Sci-Fi MegaKit, UAL) | **Conflict:** pack pages say CC0; site licence says Quaternius Asset License (QAL) v1.0 | https://quaternius.com/license.html: "Quaternius Asset License (QAL) v1.0", "Last updated: 8/28/2026"; "You can use these assets, free of charge, in personal, educational, and commercial games"; "No attribution is required."; §3(a) no redistribution "as a standalone asset, asset pack, stock file, template, or similar product", "This restriction applies regardless of how much the Assets have been modified."; §7 "Changes will not apply retroactively to Assets you've already obtained under an earlier version." https://quaternius.com/packs/stylizednaturemegakit.html: licence "CC0", "Free to use in personal, educational and commercial projects.", 116 models (40 trees, 35 plants and flowers, 27 rocks), "Ghibli-inspired", Standard tier "60-70% of my pack is completely free"; the wind grass and stylized leaf shaders are only in the paid Source tier. https://quaternius.com/packs/modularscifimegakit.html: "CC0", 277 modular sci-fi pieces (walls, floors, columns, doors, props, aliens). | **WW:** trees, flowers, bushes, rocks in one painterly family. **LL:** modular corridor blockout and props. **DH:** stylized trees if DH goes painterly. | Painterly-stylized (nature); stylized textured (sci-fi) | Treat as QAL (the stricter reading): fine inside the game; QAL is a custom licence, outside §5, so the owner must accept it. Record download date and page text. Not "epic" enough alone for DH. |
| **KayKit** (Kay Lousberg): Forest Nature Pack, Space Base Bits, Medieval Hexagon, Adventurers, Character Animations | CC0 | https://kaylousberg.itch.io/kaykit-forest: "Creative Commons Zero v1.0 Universal"; "Free for personal and commercial use, no attribution required. (CC0 Licensed)"; "But please don't resell unmodified copies or claim them as your own."; "Textured using a single gradient atlas texture (1024x1024)"; free tier "100+" models; "No generative AI was used". https://kaylousberg.itch.io/space-base-bits: CC0, "48+ Low poly optimized models", gradient atlas. | Grey-box for all three (DH lanes, WW village layout, LL base). | Low-poly toy | Gradient-atlas look is exactly the rejected toy style. The "don't resell unmodified copies" line is a request beside CC0; harmless for us. |
| **Kenney**: Nature Kit, Space Station Kit, Space Kit | CC0 | https://kenney.nl/support: "Yes, all game assets on the asset pages are public domain licensed (CC0)."; "You're free to use them, even in commercial projects."; "Attribution is not required". https://kenney.nl/assets/nature-kit: CC0, 330 files, v1.0 2020. https://kenney.nl/assets/space-station-kit: CC0, 90 files, v1.0 2024 (sci-fi station interiors). https://kenney.nl/assets/space-kit: CC0, 150 files, 2020. | Grey-box (LL station layout from Space Station Kit). | Low-poly toy | Same as KayKit. The Kenney logo is reserved for the studio. |
| **Poly Pizza** | Per model: CC0 or CC-BY (Google Poly imports) | https://poly.pizza/docs/tos: "you agree to adhere to the terms of the Creative Commons license that applies at the time of download"; users are "expressly forbidden from using any part of the service" for "machine learning or artificial intelligence training without explicit written permission from us." FAQ page returned 502 on 01/11. | Grey-box only. | Low-poly toy | CC-BY models need credit. The AI clause means: do not feed models taken from the service into ChatGPT/Tripo pipelines. |
| **Sketchfab** (downloadable, CC0 or CC-BY only) | Per model | https://help.sketchfab.com/en/articles/16152217 ("Downloading 3D models"): CC BY: "they must give you credit for the original work"; CC0: "No Rights Reserved"; CC BY-NC: "others cannot use your model commercially"; Standard: "you may use the 3D asset worldwide, in all types of media, for all types of use". NoAI: Sketchfab blog https://sketchfab.com/blogs/community/restricting-generative-ai-use-of-free-models (via search): NoAI stays enforceable on Standard-licensed downloads; NoAI can no longer be set on new CC uploads. | Hero props that Tripo struggles with: **WW** stone lanterns, torii, temple details from photogrammetry; **DH** ruins, carved stones; **LL** realistic machinery. | Realistic (scans) or anything | Quality and licence vary per model; check each page. Only CC0 and CC BY (not SA, NC, ND). Standard-licence free models are outside §5 and may carry NoAI (never use with AI tools). Platform future uncertain: CC BY and Standard migrate to Fab, other CC licences do not (Epic docs, via search). Scans are heavy and need retopology/decimation. |
| **OpenGameArt** | Per asset (CC0, CC-BY, OGA-BY, CC-BY-SA, GPL) | https://opengameart.org/content/faq (read with curl; WebFetch got 403): "Yes, you can use any of the art submitted to this site. Even in commercial projects. Just be sure to adhere to the license terms."; for CC-BY 3.0: the work "may not be not used on distribution networks that use some form of Digital Rights Management (DRM)." | Textures (see §4); few 3D models at our bar. | Mostly low-poly or pixel | Use only CC0 or CC-BY/OGA-BY with credit; avoid SA and GPL (§5). A public web game has no DRM, so the CC-BY 3.0 DRM clause is fine. |
| **Fab** (Epic) free listings, Megascans | Fab Standard (custom) or CC BY | Fab EULA page returned 403. https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab: "Standard (Free or For Sale)"; "you cannot offer an asset with the NoAI meta tag under the Creative Commons Attribution license." Megascans: free only to the end of 2024, paid on Fab from 2025 (CG Channel, 80.lv, via search). | Only Fab listings marked **Creative Commons Attribution** fit §5. | Realistic | Standard listings are a custom licence, outside §5; Epic terms bar use in AI datasets/training (Mixer supplemental terms, via search). If the owner claimed Megascans on Fab in 2024, that is a Fab Standard licence, still outside §5: owner decision. |

## 4. PBR textures, HDRIs and skies

| Source | Licence | Verified on source page (01/11) | Good for | Style fit | Risks |
|---|---|---|---|---|---|
| **Poly Haven textures and HDRIs** | CC0 | As §3 (https://polyhaven.com/license). | **All three:** replace `RoomEnvironment` with a real HDRI for IBL (PMREM) and, for outdoor maps, as the visible sky through r170 `GroundedSkybox`. **DH:** sunny mountain and cloud HDRIs, rock/cliff/ground materials. **WW:** meadow, sunrise, overcast HDRIs; grass, mud, path materials. **LL:** industrial interior HDRIs for metal reflections. | Realistic | 8K–16K HDR files are huge; ship 1K–2K EXR/HDR for lighting plus a separate sky image; convert large ones to Ultra HDR JPEG (`UltraHDRLoader` in r170). Do not script downloads (terms §3.2). |
| **ambientCG** | CC0 | https://docs.ambientcg.com/license/: "All ambientCG assets are provided under the Creative Commons CC0 1.0 Universal License."; "You can include the raw files in your project, for example a video game."; "You don't need to give credit but I would of course appreciate it". Catalogue checked by search on 01/11 (counts are search hits): "roof" 22 (RoofingTiles…), "paving" 165, "metal" 214, "plate" 21 (DiamondPlate…), "ground" 169, "rock" 76; ids RoofingTiles001, PavingStones001, MetalPlates001, DiamondPlate001, PaintedMetal001 exist. | **DH:** ground, gravel, rock, cliff, moss materials for terrain splat. **WW:** roof tiles, planks, plaster, paving stones, mud. **LL:** metal plates, painted metal, concrete, diamond plate, panels. | Realistic | None found in the licence. Keep texture sets at 1K–2K and pack ORM channels for the web. |
| **cgbookcase** | CC0 | https://www.cgbookcase.com/textures/: "The textures are published under the CC0 1.0 license, which means means you can use them for free without giving credit." (sic). Home page: "100% free, no restrictions." | Second source for bark, rock, ground, wood, metals (all three games). | Realistic | Separate licence page returned 404; the statement above is on the textures index. Fewer sets than ambientCG. |
| **ShareTextures** | "Custom CC0" (custom terms) | https://www.sharetextures.com/p/license: "Free to use for personal, educational, or commercial projects."; "No attribution required (but appreciated!)."; "No asset redistribution on other websites, in plugins, or as part of collections without our written permission."; "No automated downloads, hotlinking, or embedding direct downloads in third-party apps". | Extra realistic materials and some models. | Realistic | Not plain CC0 despite the name: outside §5. Use only if ambientCG, Poly Haven and cgbookcase lack a material and the owner accepts. |
| **Voxel Core Lab, Hand-Painted Watercolor Terrain Textures** | CC0 | https://voxelcorelab.itch.io/watercolor-terrain-textures: "This pack is released under the CC0 1.0 Universal license (Creative Commons Zero)"; 16 seamless PNGs at 1024² (4 grass, 4 stone, 4 water, 4 dirt); name your own price; "No generative AI was used". | **WW** painterly ground and water if the map goes stylized. | Painterly (watercolor) | Albedo only (no normal/roughness). Small set; tiling will show without blending. |
| **OpenGameArt, rubberduck hand-painted textures** | CC0 | https://opengameart.org/content/handpainted-rock-textures: "License(s): CC0", author rubberduck. https://opengameart.org/content/8-handpainted-style-textures-2: "License(s): CC0". (Search also lists "handpainted-style-textures-3" and a hand-painted grass pack by the same author as CC0; not opened.) | **WW** and **DH** if stylized: rock, grass, ground with normal/height/roughness maps. | Painterly | Older assets; check resolution and seams per set. |
| **ESA/Webb, ESA/Hubble images** | CC BY 4.0 | https://esawebb.org/copyright/: "ESA/Webb images, videos and web texts are released under the Creative Commons Attribution 4.0 International license"; "Each image or video has its own credit line that is required."; logos excluded. https://esahubble.org/copyright/: same licence, credit "clearly and visibly", "may not be used to state or imply the endorsement by ESA/Hubble", identifiable people need separate permission. | **LL:** real nebulae and star fields through station windows, title backdrop, briefing screens. Real photography, commercial-grade. | Realistic | Every image needs its exact credit line on the Credits page. Some images on these sites have other credits (NASA, CSA, STScI); copy the line per image. |
| **NASA images** | US public domain (with limits) | https://www.nasa.gov/nasa-brand-center/images-and-media/: images "generally are not subject to copyright in the United States."; use "must not explicitly or implicitly convey NASA's endorsement"; "The NASA Insignia, Logotype, identifiers, and imagery are not in the public domain." | **LL:** planets, Earth limb, deep-field star backgrounds. | Realistic | Not a CC licence; §5 lists CC0/CC-BY only, so record it as public domain and get the owner's OK. Avoid images with logos, people, or third-party credits. |

## 5. Foliage, rocks and terrain (realistic or painterly enough)

| Source | Licence | Verified (01/11) | Good for | Style fit | Risks |
|---|---|---|---|---|---|
| Poly Haven rocks, cliffs, trees | CC0 | §3 | **DH** cliffs and rock walls along the pass, river boulders; **WW** meadow rocks | Realistic | Decimate; shared HDRI and grade to sit next to Tripo models. |
| Quaternius Stylized Nature MegaKit | CC0 on page / QAL site-wide | §3 | **WW** trees, flowers, bushes, rocks | Painterly | QAL; Source-tier shaders are paid (we write our own wind with CSM). |
| KayKit Forest Nature Pack | CC0 | §3 | Grey-box only | Low-poly | Toy look. |
| Kenney Nature Kit | CC0 | §3 | Grey-box only | Low-poly | Toy look. |
| **Quick_Grass** (SimonDev) | MIT (code) | https://github.com/simondevyoutube/Quick_Grass `LICENSE`: "MIT License, Copyright (c) 2023 simondevyoutube"; README: "this is released under the MIT license, so do whatever you want." Based on the Ghost of Tsushima grass GDC talk. | **WW** meadow, **DH** grass on the slopes: dense instanced blades with wind | Realistic-stylized (shader) | Demo code, not a package: port into our kit. Bundled textures/models not inventoried (GitHub API rate limit); take code only unless their source is checked. Counts as shader/instancing under the allowed list; owner should still see it against the bar. |
| **`@dgreenheck/ez-tree`** 1.1.0 | MIT | `LICENSE`: "MIT License, Copyright (c) 2024 Daniel Greenheck"; npm peer `three >=0.167`; published 2026-01-15 | Varied pines and broadleaf trees with bark and leaf textures | Realistic-ish | **Rule flag:** trees built in code are "prop models in code" (DH AGENTS). Possible route: generate in its app, export GLB, judge like any model, owner decides. Bark/leaf texture sources not checked. |
| **`three.terrain.js`** 3.1.1 | MIT | `LICENSE.txt`: "The MIT License, Copyright (C) 2010-2014 Isaac Sukin"; npm peer `three >=0.160.0`; published 2026-08-27 | **DH** backdrop mountains and terrain shaping beyond the playfield | (geometry) | Heightmap terrain needs real materials (ambientCG/Poly Haven) and a splat or triplanar shader to look real. |
| `@mapbox/martini` 0.2.0 | ISC | `LICENSE`: "ISC License, Copyright (c) 2019, Mapbox" | Turns a heightmap into an efficient mesh (RTIN) for far terrain | (geometry) | Last release 2020; small and stable. |
| Gaea 2 Community | Not allowed | QuadSpinner download page (via search): Community Edition is "for evaluation and non-commercial use"; export capped at 1024² | — | — | Non-commercial: do not use its output. |

## 6. three.js add-ons and shaders

| Package | Version, date | Licence (LICENSE file) | three 0.170 | Use | Risks |
|---|---|---|---|---|---|
| **three r170 built-ins** (`examples/jsm`) | 0.170.0, in `node_modules` | MIT ("The MIT License, Copyright © 2010-2024 three.js authors", r170 `LICENSE`) | Yes | `objects/Sky.js` and `SkyMesh` (Preetham sky), `Water.js`, `Water2.js` (flow-map river), `GroundedSkybox.js` (HDRI as ground-projected sky), `Lensflare.js`; `loaders/RGBELoader`, `EXRLoader`, `UltraHDRLoader`, `KTX2Loader`; `csm/CSM.js` (cascaded shadows for long views); `postprocessing/GTAOPass`, `SMAAPass`, `TAARenderPass`, `SSRPass`, `BokehPass`, `LUTPass`; `shaders/GodRaysShader`. | Already a dependency; no new licence. `Water`/`Water2` need normal and flow maps: the ones in the three.js repo `examples/textures/water/` have no separate licence file, so use a CC0 normal map (ambientCG/Poly Haven) or bake our own. |
| **`three-custom-shader-material`** | 6.4.0, 2025-10-12 | MIT ("MIT License, Copyright (c) 2024 Faraz Shaikh") | Peer `three >=0.159`; React optional; vanilla entry `three-custom-shader-material/vanilla` | Extend `MeshStandardMaterial`/`MeshPhysicalMaterial` with our own vertex/fragment code while keeping PBR lighting: wind sway for trees and grass, terrain splat and triplanar blending, moss/snow on top faces, burn/scorch on hit | None found. |
| **`@pmndrs/vanilla`** (drei-vanilla) | 1.25.0, 2025-09-17 | MIT ("MIT License, Copyright (c) 2023 Poimandres") | Peer `three >=0.137` | `MeshReflectorMaterial` (LL polished/wet floors, WW pond), `SpotLight` (volumetric cones for LL), `Cloud`, `Sparkles`, `Stars`, `Sprite Animator` (flipbooks), `pcss` soft shadows, `Caustics`, `Outlines` | `Cloud` uses a cloud texture: check its source before shipping. |
| `three-stdlib` | 2.36.1, 2025-11-10 | MIT ("MIT License, Copyright (c) 2021-2023 Poimandres") | Peer `three >=0.128` | Older copies of three examples; little we need beyond r170 | Prefer r170's own `examples/jsm`. |
| **pmndrs `postprocessing`** | 6.39.5, 2026-09-09 | **Zlib** (`LICENSE.md`: "Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to" three conditions) | Peer `three >=0.168.0 <0.187.0` | Faster merged effect passes; prerequisite for N8AO, godrays, Takram clouds and atmosphere | Zlib is permissive (no attribution in binaries; keep the notice in source copies) but **not in the §5 list**: needs the owner's OK. |
| `n8ao` | 2.0.1, 2026-08-10 | npm says ISC; repo `LICENSE` is CC0 1.0 | Peer `three >=0.137`, needs `postprocessing` installed even for `N8AOPass` (README) | High-quality AO that grounds props in the scene (removes the floating, toy look) | Licence metadata disagrees (both permissive). Depends on the Zlib package. r170 `GTAOPass` (MIT) is the in-list alternative. |
| `three-good-godrays` | 0.12.1, 2026-08-06 | Zlib-style text ("Copyright © 2022 Casey Primozic… This software is provided 'as-is'"); npm has no licence field | Peer `three <=0.182`, `postprocessing ^6.33.4` | Screen-space god rays through DH dust and WW trees | Zlib, outside §5; needs postprocessing. |
| `@takram/three-clouds`, `@takram/three-atmosphere` | 0.7.6 and 0.19.1, 2026-05-06 | MIT ("The MIT License (MIT), Copyright (c) 2024 Shota Matsuda", three-geospatial repo) | Peer `three >=0.170.0`; React optional; `postprocessing >=6.36.7` required | Physically based sky and volumetric clouds: the closest free match to the reference's cumulus | Built for geospatial scale; GPU cost unmeasured on our target machines; needs the Zlib package. Try on Dragonhold only after the cheaper HDRI sky. |
| `three-mesh-bvh` | 0.9.17, 2026-10-28 | MIT ("MIT License, Copyright (c) 2018 Garrett Johnson") | Peer `three >=0.159` | Fast raycasts for scattering on scanned terrain and picking | None. |
| `realism-effects` | 1.1.2, 2023-05-12 | MIT (`LICENSE.md`, "Copyright (c) 2023 0beqz") | Peer `three >=0.148`, needs `postprocessing` | SSGI, motion blur, TRAA | No release since 2023; Zlib dependency. Not recommended. |
| `three-landscape` | 0.9.2 | MIT (npm) | React-only peers | — | We do not use React. Skip. |

## 7. VFX sprites and flipbooks (beyond the Kenney packs in use)

| Source | Licence | Verified (01/11) | Good for | Style fit | Risks |
|---|---|---|---|---|---|
| **Unity Labs "Free VFX image sequences and flipbooks"** (Thomas Iché, 2016) | CC0 | https://unity.com/blog/engine-platform/free-vfx-image-sequences-flipbooks: "we release some of these sequences under CC0 license"; 28 sequences: smoke (CandleSmoke01, DiscSmoke01, WispySmoke01–03b), clouds (Cloud01–04), explosions (Explosion00, 01 with light/nofire variants, 02, 02HD), fireballs (FireBall01–04), flames (Flame02, Flame03, Flame03-hollow, SmallFlame01 variants); each as flipbook sheets, HDR linear EXR and TGA. HEAD check: `Explosion01-flipbooks.zip` answers 200, 3,001,400 bytes. | **DH:** dragon fire body (Flame02/03), fireball travel, impact explosions, smoke after hits. **LL:** explosions, muzzle smoke, burning wreckage. **WW:** spell smoke, clouds. | Realistic rendered (offline sim) | 2016 render resolution; check frame size before relying on close-ups. EXR versions allow re-grading colour in our pipeline. Brackeys' CC0 bundle repackages these flipbooks. |
| **JangaFX free VDB volumes** (EmberGen) | CC0 | https://jangafx.com/software/embergen/download/free-vdb-animations: "These free VDB simulations are licensed as CC0 (Public Domain) so you are free to use them however you want!" Sizes: Simple Fire 64.7 MB, Small Camp Fire 59 MB, Cloud Pack 104 MB (10 clouds), Ground Explosion 661 MB, Gasoline Explosion 751 MB, Mid-Air Explosion 1.14 GB, Fire Plume 5.5 GB, Dust Shockwave 5.0 GB, Grenade Dust Impact 3.45 GB, others. | Render in Blender (free) from our own camera angles into flipbooks: **DH** dragon breath and Sky Fire impacts, ground scorch smoke; **LL** explosions, dust shockwave; **DH/WW** Cloud Pack as sky cards. | Realistic (volumetric sims) | Very large downloads; rendering is our work (time, GPU). Their CC0 flipbook pack is on the roadmap as "Delayed" (https://jangafx.com/roadmap/jangafx, via search). |
| Brackeys VFX Bundle | CC0 | https://brackeysgames.itch.io/brackeys-vfx-bundle: "These assets are released under a Creative Commons Zero (CC0) license."; "Attribution is not required."; "This pack is a combination of repackaged and remixed assets" (particle textures from Picster and Kenney, flipbooks by Thomas Iché, spritesheets by CodeManu) | Ready-to-use mix | Mixed | Mostly Kenney and Unity Labs content we can take from the originals; check CodeManu sheets' origin before use. |
| OpenGameArt CC0 explosion sheets (Sinestesia, "more explosions", AIM Studios on itch) | CC0 per page (via search) | Not opened | — | Pixel art / cartoon | Below the bar for a 3D commercial look. Skip. |
| SEAMPROOF, SCORCH, AD_FX | Already evaluated | `vfx/PACKS.md` | `cinder-drift`, Ember Puff as secondary layers | Procedural blobs | Custom licences ("royalty-free"), outside §5. |

Not used: Unity Asset Store and Fab VFX packs (custom EULAs), ansimuz and similar itch packs (licence not stated as CC0/CC-BY).

## 8. Characters and animations

| Source | Licence | Verified (01/11) | Good for | Risks |
|---|---|---|---|---|
| Mesh2Motion | CC0 assets, MIT app | `THIRD_PARTY.md` (29/10) | Already in WW's rig pipeline; creature rigs await download approval | — |
| **Quaternius Universal Animation Library** 1 and 2 | CC0 on the pack page; QAL site-wide | https://quaternius.com/packs/universalanimationlibrary.html: licence CC0, "Free to use in personal, educational and commercial projects.", 120+ animations, universal humanoid rig "ready for retargeting"; Standard tier free | Villagers, soldiers, bipedal foes (WW needs visible characters and foes on map 1), Lightbearer in LL | Same QAL ambiguity as §3. |
| **KayKit Character Animations** | CC0 | https://kaylousberg.itch.io/kaykit-character-animations: "Creative Commons Zero v1.0 Universal"; "161 Humanoid animations"; built for KayKit Rig_Medium and Rig_Large; the page warns animations "may not look good" on other humanoids | Backup clip source for crowds (walk, work, cheer) | Retarget quality on Tripo rigs unproven. |
| Mixamo | Adobe terms | Official FAQ (helpx.adobe.com) still 403 on 01/11 | — | As `THIRD_PARTY.md`: not default (no raw-file redistribution, no ML training, Adobe upload). |
| CMU Motion Capture Database | Custom | http://mocap.cs.cmu.edu/: "This dataset of motions is free for all uses."; FAQ: "You may include this data in commercially-sold products, but you may not resell this data directly, even in converted form." | Large human mocap library | Custom licence, outside §5; raw BVH needs heavy cleanup. Not default. |

## 9. Clause check (attribution, pack redistribution, AI, NFT)

| Source | Credit needed | "No redistribution as assets/pack" | AI clause | NFT clause |
|---|---|---|---|---|
| Poly Haven | No | No (CC0) | No AI clause; terms forbid scraping/data mining without permission | None found |
| ambientCG | No (suggested line on the page) | No | None found | None found |
| cgbookcase | No | No | None found | None found |
| ShareTextures | No | **Yes**: no redistribution on other sites, plugins, collections; no automated downloads | None found | None found |
| Quaternius (QAL) | No | **Yes** (§3a), even when modified | None in QAL | None |
| KayKit | No | Request: don't resell unmodified copies | None (page states "No generative AI was used" about its making) | None found |
| Kenney | No | No | None found | None found |
| Poly Pizza | Per model (CC-BY needs it) | Per CC licence | **Yes**: no ML/AI training via the service without written permission | None found |
| Sketchfab | CC-BY: yes | Per CC licence | **NoAI** tag binding on Standard licence; not on CC uploads | None found |
| Fab Standard | Per listing | Standard EULA (not read, 403) | Epic terms bar AI datasets/training (secondary source) | Not read |
| OpenGameArt | Per asset | Per licence; CC-BY 3.0 forbids DRM distribution | None found | None found |
| Voxel Core Lab | No | No | None found | None found |
| ESA/Webb, ESA/Hubble | **Yes**, exact line per image | No | None found | None found |
| NASA | No (no endorsement, no logos) | No | None found | None found |
| Unity Labs flipbooks, JangaFX VDBs, Brackeys | No | No | None found | None found |
| CMU mocap | Citation appreciated | **Yes**: no direct resale, even converted | None found | None found |

Shipping inside a web game is fine for every "no pack redistribution" clause above: the files ship only as part of the game. Packing assets into our own merged GLBs and KTX2 atlases keeps them from looking like a loose asset pack.

## 10. Checked and not usable, or not verified this round

- **Not usable:** Gaea Community (non-commercial), Megascans after 2024 (paid; Fab Standard), any CC BY-NC, BY-ND or BY-SA model, Unity Asset Store content (custom EULA), GSAP (already rejected in `THIRD_PARTY.md`).
- **Not verified (page blocked or empty on 01/11):** Smithsonian Open Access 3D (CC0 per awesome-cc0 list; site behind Cloudflare), USGS elevation data (policy page empty), Fab EULA (403), Poly Pizza FAQ (502), Mixamo FAQ (403), Quick_Grass bundled assets, ez-tree texture sources, drei `Cloud` texture. Check these before any use.

## 11. Best 10 to try first, per game

Order = expected gain per hour. Each asset pack still needs the owner's download OK (§0). Code packages are routine.

### Dragonhold (fantasy mountain pass)

1. **Poly Haven HDRIs** (CC0): replace `RoomEnvironment` with a sunny mountain or cumulus HDRI for IBL, and show it through r170 `GroundedSkybox`. Directly targets the toy-like trees, rocks, water and ground.
2. **Poly Haven rocks and cliffs** (CC0, e.g. Rock Face 01, 20K tris): pass walls, river boulders, backdrop crags, decimated and meshopt-compressed. Needs the model-rule change.
3. **ambientCG ground, gravel, rock and moss materials** (CC0) with a splat/triplanar terrain shader via **`three-custom-shader-material`** (MIT).
4. **r170 `Water2`** (MIT) with a CC0 normal map for the river, plus foam and wet-bank decals.
5. **Unity Labs flipbooks** (CC0): Flame02/03, FireBall, Explosion01/02 as the body of dragon fire and impacts, layered over the Kenney sprites already in use.
6. **JangaFX CC0 VDBs** rendered in Blender: Simple Fire (64.7 MB), Ground Explosion (661 MB), Cloud Pack (104 MB) for a hero breath, hit bursts and sky cards.
7. **r170 `CSM` + `GTAOPass` + `SMAAPass` + `LUTPass`** (MIT): long sun shadows, contact shadows, clean edges, one cinematic grade across scans and Tripo models.
8. **Quick_Grass** (MIT, code only) for wind-blown grass on the slopes.
9. **cgbookcase bark, rock and ground sets** (CC0) as a second texture source when ambientCG lacks a match.
10. **`@takram/three-clouds`** (MIT, needs Zlib `postprocessing`) for volumetric cumulus like the reference: only after the owner accepts Zlib and after the HDRI sky is in.

### Wordwoven (East Asian fantasy meadow and villages)

1. **Poly Haven meadow and sunrise HDRIs** (CC0) for IBL and sky: the scene stops looking like a studio.
2. **Quick_Grass** (MIT) + `three-custom-shader-material` wind: a living meadow on map 1.
3. **Quaternius Stylized Nature MegaKit** (CC0 page / QAL): trees, flowers, bushes and rocks in one painterly family close to the Tripo look. Needs the model-rule change and QAL acceptance.
4. **ambientCG roof tiles, planks, plaster, paving stones and mud** (CC0) for village surfaces and paths.
5. **Quaternius UAL 1 and 2** (CC0 page / QAL) on villagers and foes, plus the Mesh2Motion creature rigs already proposed: map 1 needs visible characters and monsters.
6. **Voxel Core Lab watercolor terrain textures** (CC0) as a painterly ground option if the art direction stays stylized.
7. **rubberduck hand-painted rock and grass textures** (OpenGameArt, CC0) for stylized rocks and ground with normals.
8. **Sketchfab CC0 / CC BY photogrammetry hero props** (stone lanterns, torii, shrine pieces), checked one by one, credited, never NoAI, never fed to AI tools.
9. **Unity Labs smoke and cloud flipbooks** (CC0) + `@pmndrs/vanilla` `Sparkles` and `Sprite Animator` (MIT) for spell smoke, mist and fireflies.
10. **KayKit Character Animations** (CC0) as a backup clip set for village crowds (work, walk, cheer), if retargeting holds up.

### Last Line (sci-fi space station)

1. **ESA/Webb and ESA/Hubble images** (CC BY 4.0, exact credit per image): real nebulae and star fields through windows and on the title screen.
2. **ambientCG metal plates, painted metal, diamond plate and concrete** (CC0) re-applied to corridor walls and floors.
3. **Poly Haven industrial interior HDRIs** (CC0) for reflections, replacing `RoomEnvironment`.
4. **`@pmndrs/vanilla` `MeshReflectorMaterial` and `SpotLight`** (MIT): polished and wet floors, volumetric light cones.
5. **r170 `SMAAPass` or `TAARenderPass`** (MIT): if part of the "blurry shots" complaint comes from anti-aliasing or a low render scale, measure, then replace or add to the current bloom chain.
6. **Unity Labs explosion, fireball and smoke flipbooks** (CC0) for hits and deaths.
7. **JangaFX CC0 VDBs** (Dust Shockwave, Ground Explosion, Gasoline Explosion) rendered as big set-piece explosions.
8. **Quaternius Modular Sci-Fi MegaKit** (CC0 page / QAL, 277 pieces): modular corridor geometry, re-textured with item 2 where UVs allow.
9. **NASA images** (US public domain, no logos, no endorsement) for planets and Earth-limb views.
10. **Kenney Space Station Kit** (CC0, 90 files, 2024): grey-box layout only, to test corridor shapes before Tripo or Quaternius pieces.

## Sources

Licence and product pages read on 01/11/2026:
- https://polyhaven.com/license, https://polyhaven.com/a/rock_face_01
- https://docs.ambientcg.com/license/
- https://www.cgbookcase.com/, https://www.cgbookcase.com/textures/
- https://www.sharetextures.com/p/license
- https://quaternius.com/license.html, https://quaternius.com/packs/stylizednaturemegakit.html, https://quaternius.com/packs/modularscifimegakit.html, https://quaternius.com/packs/universalanimationlibrary.html
- https://kaylousberg.itch.io/, https://kaylousberg.itch.io/kaykit-forest, https://kaylousberg.itch.io/space-base-bits, https://kaylousberg.itch.io/kaykit-character-animations
- https://kenney.nl/support, https://kenney.nl/assets/nature-kit, https://www.kenney.nl/assets/space-station-kit, https://www.kenney.nl/assets/space-kit
- https://poly.pizza/, https://poly.pizza/docs/tos
- https://help.sketchfab.com/en/articles/16152217, https://sketchfab.com/licenses
- https://opengameart.org/content/faq, https://opengameart.org/content/handpainted-rock-textures, https://opengameart.org/content/8-handpainted-style-textures-2
- https://voxelcorelab.itch.io/watercolor-terrain-textures
- https://esawebb.org/copyright/, https://esahubble.org/copyright/
- https://www.nasa.gov/nasa-brand-center/images-and-media/
- https://jangafx.com/software/embergen/download/free-vdb-animations
- https://unity.com/blog/engine-platform/free-vfx-image-sequences-flipbooks
- https://brackeysgames.itch.io/brackeys-vfx-bundle
- http://mocap.cs.cmu.edu/
- https://dev.epicgames.com/documentation/en-us/fab/licenses-and-pricing-in-fab
- LICENSE files on GitHub: mrdoob/three.js@r170, pmndrs/postprocessing, FarazzShaikh/THREE-CustomShaderMaterial, pmndrs/three-stdlib, pmndrs/drei-vanilla, N8python/n8ao, ameobea/three-good-godrays, takram-design-engineering/three-geospatial, IceCreamYou/THREE.Terrain, gkjohnson/three-mesh-bvh, simondevyoutube/Quick_Grass, dgreenheck/ez-tree, mapbox/martini, 0beqz/realism-effects; versions, peers and dates from registry.npmjs.org

Secondary (search summaries, not the binding text): Sketchfab NoAI blog posts; Fab/Megascans coverage (CG Channel, 80.lv, Epic forums); Epic Mixer supplemental terms; JangaFX roadmap; Gaea download page; Sketchfab-to-Fab migration docs.
