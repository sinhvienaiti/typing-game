# Flipbooks: sources, render, atlas, budget

Use a flipbook only when a still texture with noise erosion is not enough (VFX_STANDARD §4.4): fire bodies, explosions, smoke, big bursts of energy. The free packs checked on 31/10 (`docs/games/vfx/PACKS.md`) read as soft procedural blobs, so a pack is a candidate, never a pass.

## 1. Sources

- **Unity Labs** "Free VFX image sequences and flipbooks": CC0. 28 sequences (smoke, clouds, explosions, fireballs, flames) as sheets, HDR EXR and TGA. They are 2016 renders: check the frame size before using one in a close-up.
- **JangaFX free VDB volumes:** CC0. Render them yourself (§2). Files run from about 60 MB to 5.5 GB, so check the free disk first.
- **Firefly Video,** Adobe models only (never a partner model), cut with `tools/vfx-flipbook`.
- The licence quotes and dates are in `docs/games/FREE_ASSET_SOURCES.md` §7. Every item gets its own row in `docs/games/THIRD_PARTY.md`.

## 2. Render

- **In Blender, at the play camera:** the game's tilt and distance, with the key light from the scene's direction.
- **Push it to anime and mythic:** a colour ramp or posterize on emission and density, a thin bright core and a bold silhouette. A photoreal sim is raw material, never the target (owner, 02/11).
- **Length:** keep the frames to the phase's length in VFX_STANDARD §3.4. Render on black for additive layers, or with alpha for normal-blended smoke.
- **Run heavy jobs through `.local/bin/heavy.sh`:** a render with `--cores=N`, a browser capture with `--gpu` (it also waits until 10 GB of disk is free).

## 3. Atlas

- 4×4 to 8×8 frames at 1024² to 2048². VFX_STANDARD §4.4 starts loops and bursts at 4×4 or 6×6 on 1024².
- `tools/vfx-flipbook` writes the atlas PNG, JSON, contact sheet, preview and metrics. It handles centred, pivoted and strip layouts, black crush, and a matte from an alpha video.
  - It takes video today. Encode a Blender sequence as a colour clip and an alpha clip (`<id>__vN.rgb.mp4` and `<id>__vN.alpha.mp4`), or add a frame-folder input to the tool.
- **Checks:** centre drift, coverage and the loop seam (VFX_STANDARD §4.4), and an alpha-0 margin round each cell.
- **Erosion alpha:** dissolve the frame with a noise threshold over its life (two thresholds give a hot rim), instead of fading the whole card. Blend neighbouring frames in time.

## 4. Budget

- **VRAM:** an RGBA8 atlas of 2048² takes about 16 MB, plus a third with mipmaps; 1024² takes about 4 MB. VFX textures per tier are capped at 8, 16, 32 and 48 MB (Low to Ultra, VFX_STANDARD §3.7). Count every atlas live at the same time.
- **Format:** WebP at runtime. Use KTX2 only when a measured tier breaks the cap; enabling it adds the Basis decoder's THIRD_PARTY row and Credits notice ([licences](../../game-art-pipeline/references/licences.md) §3).
- **Overdraw:** big cards cost layers × pixels. Stay inside the §3.7 overlap caps, and count overdraw in the lab when headroom is tight.
- **Warm at load:** build each pool with its final blend state at load; an atlas that arrives later only uploads a texture (`games/dragon-hold/src/view/flipbook.ts`).

## 5. Judge

- In the lab first, then in the built play host at the player's settings with no URL flags. Two blind judges both at 8.5 or more; Dragonhold's dragon fire aims at 9.
- Use a stop rule, for example a day. Send the owner the clip and sheets before wiring the flipbook into the game.
