# Smoke library candidates (17/11/2026)

Owner approved 17/11: a shared neutral grey smoke library, tinted per element in code. Needed kinds: **puff**, **plume** (rising), **ground roll**, **dust burst**, **wisp**, **explosion smoke**. Licences read on the pack's own page (rules: `.agents/skills/game-art-pipeline/references/licences.md`). Nobody signed in, nothing accepted. Contact sheet: `typing-game-review/owner-review/2026-11-17/tu-tien/smoke-library/smoke-candidates.jpg`.

## Downloaded

Folder `games/immortality-cultivation/art-src/third-party/smoke/unity-labs-vfx/` (zips in `zips/`, .tga sheets in `flipbooks/`, `LICENSE-SOURCE.md`). Licence for all: **CC0 1.0**, https://creativecommons.org/publicdomain/zero/1.0/, stated on https://unity.com/blog/engine-platform/free-vfx-image-sequences-flipbooks . All are 8-bit RGBA TGA, pure greyscale (saturation 0) with real alpha, except Explosion02 (coloured fire). Frame order is row-major.

| Flipbook | Sheet / grid / frame | Frames | Grade | Covers |
|---|---|---|---|---|
| DiscSmoke01 | 2048x1024, 16x4, 128x256 | 64 | A | plume (best), wisp support |
| Cloud01 | 1024x1024, 8x8, 128x128 | 64 | A | puff, dust-burst support |
| Cloud02 | same | 64 | A (twin of Cloud01, lighter) | puff |
| Cloud04 | same | 64 | A | soft puff, dust base |
| Cloud03 | same | 64 | B | dust burst support (dim, soft) |
| WispySmoke01 / 02 | same | 64 | B | wisp, ground-roll support (billowy, not wide) |
| WispySmoke03 / 03b | same | 64 | B | wisp (03b thinnest) |
| CandleSmoke01 | 1024x512, 20x4, 51x128 | 80 | B | thin wisp (tiny frames, upscale blurs) |
| Explosion01-light-nofire | 1024x1024, 5x5, 204x204 | 25 | A | explosion smoke (fades to grey, tint-friendly) |
| Explosion01-nofire | same | 25 | B | explosion smoke, near-black (needs lift when tinted) |
| Explosion02 | same | 25 | C for this job | coloured fire plus smoke, not neutral (keep for fire work) |

Resolution caveat: the 128 px frames are small; fine as layers up to about 256 px on screen, soft when large. Realistic volumetric look is real (EmberGen-style render), so no cartoon C grades.

## Pack table

| Pack | Licence + URL | Flipbooks | Grade | Kinds covered |
|---|---|---|---|---|
| Unity Labs free VFX flipbooks (downloaded) | CC0 1.0, page above | 13 smoke, cloud and explosion sheets (table above) | A/B | puff A, plume A, wisp B, explosion A, dust burst B (support only), ground roll B (support only) |
| JangaFX free VDB volumes (EmberGen) | CC0 per https://jangafx.com/software/embergen/download/free-vdb-animations (search summary of the page, not downloaded) | none: .vdb volumes, 59 MB to 6.6 GB each (fire plume, dust devil, cloud pack, aerial explosion, tornado) | not graded | no flipbook; the Blender bake source for dust burst, ground roll and shockwave |
| JangaFX flipbook pack | none exists; the JangaFX roadmap lists a CC0 flipbook pack as delayed | n/a | n/a | n/a |
| Kenney Smoke Particles | CC0 per https://www.kenney.nl/assets/smoke-particles (page says CC0, 70 files); direct zip link not exposed to a plain fetch, so not downloaded | single sprites, not flipbooks | likely C/B, not seen | puff stills only |
| OpenGameArt "smoke aura" | CC0 per search result https://opengameart.org/content/smoke-aura ; page returned 403 so licence not verified on the page | one sheet, 256 px frames | not seen | not verified, skip |
| ActionVFX free smoke plume and dust wave clips | "licensed for use in commercial projects" only (CGChannel 2016); custom licence, needs their site | video clips, 2K | rejected: custom terms, not CC0 | none |
| Ardes Particle Pack 1 (Gumroad) | listed CC0, pay-what-you-want checkout | sprite sheets | not checked | stopped: Gumroad checkout, no click-through accepted |
| itch.io packs (Fellor, RagnaPixel, GoVFX, Kalponic) | Fellor: not CC0 and no redistribution; RagnaPixel: credit required; others no licence statement seen | n/a | rejected or unverified | none |
| Summer Engine "Smoke Particles" | third-party listing, appears to mirror Kenney | n/a | unverified | none |

## Coverage and gaps

- **A:** puff (Cloud01, 02, 04), plume (DiscSmoke01), explosion smoke (Explosion01-light-nofire).
- **B only:** wisp (WispySmoke, CandleSmoke), dust burst (Cloud03 as a soft support), ground roll (WispySmoke as a support).
- **Gaps needing Blender:** a true dust burst with a shockwave ring and ground-hugging spread; a wide ground-rolling smoke (side view, low and long); a thin high-resolution wisp (256 px or more). Plan: bake from the CC0 JangaFX dust, fire-plume and cloud VDBs in Blender and render grey flipbooks with alpha; those VDB files are huge and are not yet downloaded.
- Not yet done: no blind-judge scoring, no engine test. Grades are the author's, from contact sheets only. Explosion00 returned no file.
