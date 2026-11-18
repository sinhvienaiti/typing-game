# Common failures, and how to catch them

Every row happened in one of our games between 26/10 and 01/11/2026. Check a concept, a prompt, a painting and a build against this list before you send it for judging.

## Layout and camera

| Failure | What we saw | Fix | Check |
|---|---|---|---|
| The epic is where the camera cannot look | Concepts with a sky band, far mountains, a cliff and a guardian statue above the top edge. Title art full of mountains, while the fight showed a lawn | Compute the frame first. Put sky and distant scenery on the title, results and intro cameras. In play, build the epic inside the frame (§2 of `composition.md`) | `frame-budget.mjs`: sky line, points outside the frame |
| Landmarks out of frame | "300 m to the side, 400 m tall, filling the upper corner" was at screen x 3,112 | Place every landmark with the script, far and low, or on the wings | Every landmark has a screen box in the legend |
| Tall things over the play or the HUD | A 16 m gatehouse covering the south pads; masts and pylons leaning into the gun cards | Respect the height budget and the lean-out. Design low and wide, or change the view's headroom | Project the top and the foot of every tall piece |
| A miniature or diorama read | Cliffs 8–9 m high (a 1:100 model); a centrepiece painted 2.9× its block; nothing ten times a soldier | Hold pieces to their blocks. Make the hero landmark at least ten times a unit. Let masonry, stairs and fractures carry the scale | Judge: "does it look like a miniature?" |
| The fight shows another world | The stage card showed a ring and the heroine on a causeway; the fight showed a loading dock with hazard stripes | The battle frame shows the world the key art promises | The stage card and the fight frame side by side |
| Every stage looks the same | No stage had its own landmark, light or weather | One dominant silhouette and one light script per stage. Corrupted versions change silhouettes and materials, not just the tint | A contact sheet of all the stages |

## Ground, water, roads

| Failure | What we saw | Fix | Check |
|---|---|---|---|
| Empty field | A football-pitch lawn in one mint green; the centre of a road loop empty; the top band bare; the east half flat mid-tone | Broad ground bands, clusters, a low-contrast floor feature, cropped edges, cloud shadows, life | Half-size view: is any large area one flat value? |
| Repeated tiles | One deck plate repeated down the lane; a single ground tile | 2–3 tile families, a world-space macro mask, decals, a seam layout that does not repeat in the frame | Look at a half-size frame for a visible grid |
| Flat water | A uniform blue ribbon; a straight grey "concrete gutter"; posterized foam drawn with `step()`; a garden pond with lily pads | A flow-map shader with depth colour, Fresnel, sun specular and normals; a foam mask; irregular banks; stones under the water | Crops of fords, bridges and drops beside the painting |
| Finger-smear roads | Even-width beige ribbons with soft even edges, pasted flat on the grass. Owner, 29/10: "đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu" | `PATH_QUALITY.md`: three layers, varying width, depth and kerbs, roadside items every 2–6 m, material running along the road | The judge answers "does the road look like a smear?" with no |
| Road value wrong | Roads three steps brighter than the grass; an S-bend darker than the grass in shadow | One clear step: luma ≥ grass + 0.15, not more | Luma probes along every lane |
| Blurred ground | A 2048 bake at 5.1 cm per texel where the screen needs 1.4–2.8 cm; no anisotropy; a foliage map bias of 2.7 | Meet the texel need; anisotropy 8–16; no map bias | 1:1 crops at 1080p on Ultra |

## Light, colour, focus

| Failure | What we saw | Fix | Check |
|---|---|---|---|
| Too many focal points | Ring, disk, falls, cyan lights, glyphs, shuttles and dust all asking for the eye; a road, a ring, a dragon and water competing with the gameplay | A read order, one hero landmark, a light-budget table, supporting pieces 15–25 % lower | Squint test: the first two things you see are ranks 1–2 |
| Gold glowing everywhere | Gold sun patches on the meadow, glowing ore veins, a "pale gold" ring and "white-gold" armour, when gold was the Leaders' signal | Reserve gold for its signal. Make the rest muted ochre or ivory | A hue mask of gold over the frame |
| Signal colours in the world | Orange-and-black wall stripes that matched the foes' cracks; a red line; violet clouds that clashed with the foes' violet; red banners | A signal-colour table from the start; the environment uses none of them at high intensity | Hue masks per signal colour |
| Flat light | A sun at 50° with sky fill nearly equal to the sun; no AO; no long shadows; a milky grade | A low key light, a weak fill in the map's shadow hue, AO, cascaded shadows, a filmic tone map | Lit and shadowed luma on the ground |
| Light that does not agree | Shadows with no caster; light shafts disagreeing with the shadows; mist as the brightest mass; a white glow at the top centre suggesting a horizon | One sun, every shadow cast. Mist stays below the landmark's light | Arrows drawn on the painting from each shadow |
| Bloom milk | Bloom spread over the deck; a beam 78–84 px wide whitening the lane; additive smoke turning to milk | Bloom only on thin HDR cores (VFX_STANDARD); smoke darkens instead of adding light | Before and after frames at 720p and 1080p |
| An abyss or side area as wallpaper | 37 % of the screen was a camera-facing poster with a swirl | Real layers below and beside the play: structures, haze, parallax, darker toward the player's eye | Intro sweep and play frames |

## Units and life

| Failure | What we saw | Fix | Check |
|---|---|---|---|
| Foes sinking into the ground | Grey foes on black ink; foes in shade with no rim on a dark lane; a beam's colour matching the foes and the floor; feet with no contact shadow | Value separation (near-black on mid ground, or rim light), contact AO or a blob shadow, ground lifted under the foes, a distinct foe colour family | Half-size grey copy: every foe reads |
| Foes misread | Painted foes looked like villagers or a cute raccoon, or wore our Spearmen's navy | Name each foe kind and its silhouette in the prompt; keep the foe colour family | Judge: "which side is each figure on?" |
| No life | The map empty between waves; foes appearing from nowhere at the lane end; 36 gameplay trees never drawn | Muster grounds, defenders on structures, ambient motion, every gameplay object drawn | A between-wave frame |
| Creatures with no source | Crows, a hawk, deer and mantas planned with no verified asset | Only what has a verified source; particles for fireflies and embers | The concept's sources table |

## Process

| Failure | What we saw | Fix |
|---|---|---|
| Built before an idea | Knobs tuned with no picture of "done" | Concept, base, review, painting at 8.5, then the build |
| Judged on our own scale | A pilot scored 7.1 on our scale and 4 on the market's | Market references, blind judges |
| Judged the wrong build | The dev build with URL flags looked better than what players got | Judge the play host only |
| Toy rendering by construction | Lambert ramps, stripped maps, meshes cut by 84–91 %, ink outlines | `build-from-concept.md` §3 before any polish |
| Painted without the base | Layout scores of 5.5–7.5 | The owner attaches the base, every time |
