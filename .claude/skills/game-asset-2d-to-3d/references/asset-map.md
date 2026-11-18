# Asset modes and contracts

| Target | Source/consumer | Guidance |
| --- | --- | --- |
| Painted/procedural 2D ships | [Character renderer](../../../../games/space-typing/src/characters/renderer.ts), [Ship media runtime](../../../../games/space-typing/src/characters/ship-media-runtime.ts) | Exact-version imagery has bundled/procedural fallback; preserve typing readability |
| Duel relief bundle | [Relief loader](../../../../games/space-typing/src/duel/relief-model.ts), [version resolver](../../../../games/space-typing/src/duel/relief-media-runtime.ts), [Ship3D](../../../../games/space-typing/src/duel/ship3d.ts) | Relief components and authored GLB are distinct paths; inspect current selection/lifecycle |
| Authored/bundled GLB | [Model contracts](../../../../games/space-typing/src/render3d/model-contracts.ts), [loader](../../../../games/space-typing/src/render3d/model-loader.ts), [Ship model](../../../../games/space-typing/src/render3d/ship-model.ts) | Required sockets/clips, manifest keys and quality URLs; verify destination consumes the entry |
| Campaign 3D | [Mode](../../../../games/space-typing/src/campaign3d/), [3D engine](../../../../games/space-typing/src/scene3d/), [isolation tests](../../../../games/space-typing/tests/mode-isolation.test.ts) | Separate entry, engine and storage; do not import it into the 2D game merely to render a model |
| Admin assignment | [Capability matrix](../../../../games/space-typing/src/admin/asset-tuning-capabilities.ts) | Bundled GLB loading does not prove arbitrary GLB/semantic-clip Admin editing is supported |

Older [asset-source notes](../../../../games/space-typing/docs/ASSET_SOURCES.md) contain historical procedural-only descriptions. Use them for provenance expectations; resolve implementation questions against current loaders/manifests/consumers.

## Vanguard and Fleet pipeline

For ship work, start with the [Vanguard reference](../../../../games/space-typing/docs/VANGUARD_MESHY_INTEGRATION_2026-10-17.md) and [Fleet integration](../../../../games/space-typing/docs/FLEET_12_MESHY_INTEGRATION_2026-10-20.md), then inspect their current consumers. Recorded host paths, measurements and completion claims are historical evidence, not proof of the present checkout or tool installation.

- [Visual catalog](../../../../games/space-typing/src/characters/ship-visual-catalog.json) and [cosmetic selection](../../../../games/space-typing/src/characters/ship-visual.ts) separate gameplay CharacterId from visual ID: `aegis` defaults to `razorwing`; `eternal-sovereign` is a cosmetic with no legacy character. Resolve model IDs through the catalog/selection; preserve gameplay saves, unlocks and separate cosmetic storage.
- [Source discovery](../../../../games/space-typing/scripts/ships/ship-sources.mjs) validates numbered filenames and uses catalog priority for aliases. Reuse it; preserve original art and approved Vanguard outputs.
- [Ship preparation](../../../../games/space-typing/scripts/models/prepare-ship-models.mjs) sends raw catalog sources through the Blender helper into normalized GLB, then packages High/Medium tiers and the runtime manifest. [Reviewed presets](../../../../games/space-typing/scripts/models/presets/ships-meshy.json) carry per-model orientation/socket settings; a prior model's raw nose axis is not universal.
- [Top projection](../../../../games/space-typing/scripts/models/blender/render_ship_top.py) derives transparent orthographic images and socket metadata from normalized GLB. The separate [relief preparation](../../../../games/space-typing/scripts/bg-art/prepare-ship-3d.mjs) uses suitable source imagery or a validated projection, producing color/emissive/height/model metadata. Projection sidecars bind to the GLB hash; do not reuse stale sidecars or treat studio-gray angled concepts as clean top-down cutouts.

Owner GLB originals live in `art-src/3d/`, mirroring their 2D art (`art-src/<path>/<name>.png` -> `art-src/3d/<path>/<name>.glb`); see `art-src/README.md`. [Campaign 3D preparation](../../../../games/space-typing/scripts/models/prepare-campaign3d-models.mjs) builds enemies, bosses, ship shots and Defense items from there, with a preset `placeholder` used until an image's own model exists.

Production branches (paths below are relative to the game root):

```text
art-src/3d/ships/<catalog-filename>      (ship-NN-<id>.glb, owner original)
  -> art-src/models/ships/<visual-id>.glb
  -> public/assets/space-typing/models/ships/<visual-id>/<visual-id>.{high,medium}.glb
     + public/assets/space-typing/models/manifest.json

normalized GLB -> art-src/ships/rendered/<visual-id>-top.png + <visual-id>-top.json
suitable source image or validated projection -> relief preparation
  -> public/assets/space-typing/ships/3d/<visual-id>/
     color.webp + emissive.webp + height.bin + model.json
     + public/assets/space-typing/ships/3d/manifest.json
```

## Preparation

Read [model prompt pack](../../../../games/space-typing/docs/art-requests/3D_MODELS_PROMPT_PACK_2026-10-16.md) for authored exports, [hero references](../../../../games/space-typing/docs/art-requests/HERO_2D_TO_3D_PROMPTS_2026-10-17.md) for character view consistency, and [ship top-view references](../../../../games/space-typing/docs/art-requests/ship-top-hd/SHIP_TOP_HD_PROMPTS.md) for that art direction. A 2D top view differs from the rear/above view useful in Duel.

[Model contracts](../../../../games/space-typing/src/render3d/model-contracts.ts) specify metres, +Y up, forward -Z and a visually centered origin. Read the applicable kind's current sockets/clips, triangle range and texture limits directly instead of copying numeric budgets into a new source of truth. Rigged heroes/guides and static ships differ.

Inspect script arguments/outputs before preparation. Safe scope inspection from repo root:

```bash
pnpm --dir games/space-typing ships:models:prepare --dry-run
```

- [Ship preparation](../../../../games/space-typing/scripts/models/prepare-ship-models.mjs) discovers raw ship sources and supports dry-run and explicit Blender selection. Review per-model orientation/socket presets; preserve existing output when sources/tools are absent.
- [Model preparation](../../../../games/space-typing/scripts/models/prepare-models.ts) packages `art-src/models/<kind>/<id>.glb`, validates contracts and emits tiers/manifest using meshopt/texture conversion. Its CLI currently accepts `--only` and `--force`; it has no read-only `--help` or dry-run and ignores unknown flags. Read source rather than probing `--help`, which can perform generation.
- [Blender helper](../../../../games/space-typing/scripts/models/blender/space_typing_model_tools.py) is reusable local authoring logic, not proof Blender is installed.
- [Local assets policy](../../../../games/space-typing/docs/LOCAL_ASSETS_README.md) distinguishes source/licensed material from distributable output. Do not automatically add local-only art/audio to Git.

Before using Blender recipes, resolve the executable in the preparation script's order: explicit `--blender`, `BLENDER_BIN`, standard macOS app location, then PATH. Read that executable's `--version` and the relevant helper before generating. The local helper documents Blender 4.x/5.x compatibility; Fleet records a 4.5.7 run, while external skill packs may require 5.2. Neither a historical path nor a successful preparation dry-run proves the executable/version works. Finish independent inspection when tools are absent; install or upgrade only when the task calls for it. For Three.js/API compatibility, use the [engine compatibility check](../../space-typing-director/references/project-map.md#compatibility-before-reusing-recipes).

## Acceptance evidence

Inspect multiple camera angles for symmetry, rear/underside completeness, normals, transparent/material artifacts, silhouette, socket alignment and scale. For animation check clip transitions, deformation and repeated playback. Test fallback when manifest entries or media versions are unavailable.

The generic loader skips models at Low, prefers Medium at Medium and High at High/Ultra, with available-tier fallback. Consumers can override that preference: ordinary 2D Campaign/Recall [ShipModel3D](../../../../games/space-typing/src/render3d/ship-model.ts) requests Medium for every non-Low level; this is distinct from the separate Campaign 3D mode. [Duel Ship3D](../../../../games/space-typing/src/duel/ship3d.ts) forces rival Medium while self/title follow selected quality through the authored loader. Recheck current consumers when changing tiers. Preserve exact Admin image/relief assignments instead of overriding them with a bundled cosmetic model. Check decoded memory, GPU disposal and repeated screen entry; use LOD when measured complexity justifies it.

Focused Vitest regressions include [ship-model pipeline](../../../../games/space-typing/tests/ship-model-pipeline.test.mjs), [runtime](../../../../games/space-typing/tests/ship-model-runtime.test.ts), [manifest retry](../../../../games/space-typing/tests/model-manifest-retry.test.ts), [authored shot origin](../../../../games/space-typing/tests/authored-ship-shot-origin.test.ts) and [Ship3D lifecycle](../../../../games/space-typing/tests/ship3d-lifecycle.test.ts). These protect contracts; actual rendering still needs browser evidence.
