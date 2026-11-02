# From an accepted concept to build steps

Build only after the painting is accepted. Then judge the build against that painting, side by side at 1280×720. The concept changes the view only: lanes, slots, river paths, spawns, collisions and golden hashes stay. Muster crowds and other life are view-only, and the sim never reads them.

## 1. The kit table

List every piece the accepted painting shows, ordered by how much of the battle frame it takes:

| Rank | Item | Seen (always, per wave, at a beat) | Size at 720p | Source | New model? |
|---|---|---|---|---|---|

- **Drop what the frame cannot show.** Last Line dropped a ring's base pylon (behind the deck) and two monoliths (outside the frame). Move such pieces to the title or the intro sweep, or cut them.
- **Ask for a new model** (Tripo) only for a piece the frame shows large, and only after its source image passes 8.5 with both judges. The owner's words: "Chờ ảnh đạt 8,5". The settings, face limits, credits and dry-run steps are in `docs/games/TRIPO_TODO.md` and [game-art-pipeline tripo](../../game-art-pipeline/references/tripo.md).
- **Foes and creatures:** reuse from `MONSTER_MODEL_INVENTORY.md` first (retexture, recolour, rescale, re-rig). A ticket for a new one says why nothing in the inventory fits.
- **Name the piece ids (K1, K2, …) once in the concept**, and use those ids in tickets and changelogs.

## 2. Order of work

1. **Lock the layout** with the projection script, and grey-box it in the game.
2. **Life first:** foes, defenders, hero creatures, workers, and the gameplay objects that must be seen (Wordwoven's 36 choppable trees were not drawn at all). An empty stage with polished ground still scores as empty.
3. **Ground, water and light,** the biggest share of the frame.
   - Light first: a CC0 HDRI through PMREM gives the image-based light and the reflections, in place of `RoomEnvironment` (Tu Tien's lab does this in `games/immortality-cultivation/src/lab/look.ts`).
   - ambientCG maps add detail under the game's own shading: its ramp, palette and grade stay. The scene stays anime and mythic (owner, 02/11); scans and HDRIs are light and raw material, never a photoreal target.
   - Judge the lit scene in the play build.
4. **The landmarks** (cropped, on the wings, below the surface).
5. **Dressing:** clusters, roadside items, vegetation thinned near the lanes.
6. **Atmosphere and grade:** mist in the hollows, cloud shadows, one colour lookup per map and hour.

Judge each step in the play build before you start the next. Keep each step a small, separate change, and write the game's changelog for each update.

## 3. Rendering that decides "toy" or "commercial"

These were measured causes of the toy look on 01/11. Every map needs them before any polish:
- **Physically based materials** with normal, roughness and AO maps. No Lambert with a 3-step ramp, no sphere-normal tree crowns, no ink outlines on scenery, no milky lift in the grade.
- **Image-based light** from a CC0 HDRI or our own PMREM of the scene's environment. Never a studio `RoomEnvironment` as the world light, and never the HDRI shown as sky in a frame without sky.
- **One shadow-casting key light** (cascaded shadows on High and Ultra for long shadows), contact AO (GTAO or SSAO), and real anti-aliasing (MSAA or SMAA) on High and Ultra.
- **A filmic tone map** (Neutral, AgX or ACES, as the game decides) and a colour lookup.
- **Bloom only on thin HDR cores.** The numbers are in `VFX_STANDARD.md` and in the game's settings.
- **Models keep their detail:** keep the face counts, normal maps and roughness maps of the originals, to the floors in `MODEL_QUALITY.md`. Cutting trees and rocks by 84–91 % and stripping their maps made them plastic. Cut only when measured frame time breaks the budget, in that doc's order.
- **Texture sharpness:** reach the texel density `frame-budget.mjs` prints for the nearest row, at dpr 2 on High and Ultra. Anisotropy 8–16 on ground and scenery textures. No foliage map bias that throws away resolution.
- **The play build loads what dev loads.** Check the network requests of the shipped page for the ground, decals and models.

## 4. Surfaces

- **Ground.**
  - Tiling CC0 PBR sets (ambientCG, Poly Haven, cgbookcase) in broad bands, vertex- or splat-blended.
  - A world-space macro mask (about 40–60 m) varies tone and wear, so no tile repeat shows inside the frame.
  - Use 2–3 tile families (length, tone, wear) on one trim sheet for decks and paving.
  - Add decals for wear, scorches and cracks. Keep them out of the word-tag zones.
- **Roads and lanes:** follow `PATH_QUALITY.md`: a layered cross-section, varying width, depth and kerbs, roadside items, and UVs running along the road. Use mesh strips along the lane spline, or a shader on UVs that run along the road. Real texture and decals, never a code-drawn pattern.
- **Water.**
  - A flow-map shader (three.js `Water2`, MIT), with depth colour, Fresnel, specular from the sun, and normals from CC0 maps.
  - Foam only where a per-map mask allows it (piers, drops, stepping stones). Boulders get a dark wake, not foam.
  - Irregular banks, with stones under the water to break straight lines, and mist in the bed.
  - Falls are a mesh with scrolling foam, spray particles and mist cards, built to VFX_STANDARD.
- **Cliffs and rocks:** real height on the terrain with triplanar CC0 stone, or CC0 scanned rock faces. Never cliff blocks stretched into a face.
- **Trees:** free commercial-safe models first (§6). Trees grown in code at runtime count as code-drawn stand-ins (`FREE_ASSET_SOURCES.md` flags ez-tree); an ez-tree exported to GLB is judged like any model, and the owner decides. Impostors only far away, baked from several angles at enough resolution.

## 5. Atmosphere, effects and sound

- **Fog and mist:** height fog that pools in beds, hollows and the abyss. No uniform fog.
- **Cloud shadows:** a cloud-shadow shader on CC0 noise. Light shafts stay faint.
- **Wind:** one wind field for trees, grass, banners and cloth.
- **Particles:** CC0 packs (Kenney, Unity Labs flipbooks, JangaFX VDBs rendered to cards). Record each one in `docs/games/THIRD_PARTY.md` before use.
- **Effects:** every map effect (a rift, a fall, an ink tide, a beacon, a hazard) is built to `VFX_STANDARD.md` through [game-vfx-layered](../../game-vfx-layered/SKILL.md): five phases, the caster side first.
- **Sound:** map ambience (river, wind, horns) is a real audio file through `docs/games/AUDIO_PIPELINE.md`, never a synthesized placeholder.

## 6. Sources and licences

- The rule text is `docs/games/SHARED_SYSTEMS_BAR.md` §5 (with the owner's 01/11 extension); the checked sources are in `docs/games/FREE_ASSET_SOURCES.md`; the working summary is [game-art-pipeline licences](../../game-art-pipeline/references/licences.md). Read those, not this summary, when a case is close.
- **Allowed:** CC0 first. CC-BY with a full credit line. Free custom licences that allow commercial use and forbid only reselling the asset as a pack, such as Quaternius QAL (record the date and the licence text). Third-party CC0 or QAL models may ship (01/11). Code under MIT, BSD, ISC, Apache-2.0, MPL-2.0 or Zlib.
- **Never:** NC, ND, SA or GPL; Mixamo, Fab or Sketchfab Standard; anything tagged NoAI; anything without a clear licence. Any other custom licence waits for the owner.
- **Look:** Kenney, KayKit and Poly Pizza models are grey-box only (the toy look), even though their licences allow shipping.
- **Check each licence on the asset's own page and quote it.** Download one by one; never scrape or bulk-download. Record each asset in `THIRD_PARTY.md` with the date and version at download.
- **Media never goes into Git.** Media travels by `pnpm media:push`. Image tickets for another maker carry forced checks, and the result is reviewed before commit.

## 7. Budgets and tiers

- **Every map has a frame-time gate per tier,** measured on the real GPU bench, plus the game's limits on draw calls, triangles and media size. For example, Last Line allows ≤ 60 draw calls on High; Wordwoven allows ≤ 150 draw calls and 1.5 M triangles on High.
- **Medium drops these first:** shadows, the extra fog layers, ambient life and parallax card layers. **Low** keeps the ground, the lanes, the landmark and one card layer.
- **Scatter uses a fixed seed:** the same map always gives the same result.
- **The render loop allocates nothing per frame.**
