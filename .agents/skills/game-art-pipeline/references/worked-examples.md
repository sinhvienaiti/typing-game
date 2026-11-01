# Worked examples

These are real cases from the split games, kept as examples only. The rules they produced are in SKILL.md and the other reference files. For each case, read what happened and then the rule. Numbers are blind-judge scores unless the case says otherwise.

## Last Line HUD icons (31/10–01/11)

- **What happened:**
  - Icons were accepted from 256 px sheets.
  - Wired at 16–24 px, the UI scored 6.2 and 6.3. Settings read as a virus, accuracy as a snowflake, kills as a quill, next stage as a no-entry sign.
  - Brass-filigree icons clashed with the CSS hazard-stripe chrome.
- **A later round, made in Firefly Image 5 by Claude:**
  - Claude graded the best icon 8; the judges gave it 7 and 7.
  - A style reference made the icons busier at 28 px.
  - Antigravity graded its own 20 icons 10/10; at 24 px only 4 reached 8.
- **Rules:**
  - Grade at real size, in the UI spot.
  - Brief bold silhouettes for 24–32 px.
  - Treat panels and buttons as part of the same art pass.
  - Never accept a self-grade, yours or a tool's.

## Dragonhold landmarks as Tripo sources (01/11)

- **Round 1** (old sources) scored 5–7.5. The judges saw a mobile-game look, stubby towers and near-frontal views.
- **Round v2b** (Firefly Image 5): the dragon statue came close at 8.0 and 8.3, with Tripo fitness 8.5 and 8.5.
  - The six pieces were not a set: five render styles, five stone colours, four dragon-head designs, five key greens.
  - The watchtower touched the top edge of a square frame.
  - A shared "iron and wood" sentence put iron into stone.
- **Round v3:** one set standard (one material, one dragon-head design, one light, no shadow, margins of 6–8 %, the tower in 3:4).
- **Free-model route, tried in parallel:** 58 licence-checked candidates; the best scored 7, and they did not match each other.
- **Moving the set to ChatGPT in one chat:**
  - It delivered transparent PNGs.
  - Five of six first tries failed the margin check; the second tries passed.
- **Tripo credits spent below 8.5:** none.
- **Rules:**
  - Write the set standard before the first image.
  - Split material sentences per object.
  - Put tall objects in 3:4.
  - Run the mechanical checks before judging.
  - Spend no credit below the bar.

## Last Line heroine and drone (01/11 evening)

- **What happened:**
  - Two designs came out plain and villain-like: a dark full-face mask, two horn-like fins at the ears, smooth plain plates.
  - A third design painted a halo ring into the picture, and the owner asked whether that was the right way to build it.
  - Firefly could not hold the design across four views. ChatGPT could, in one chat: first the turnaround sheet, then each view.
  - Gold was already reserved for elite foes, so the hero moved to pearl, platinum and cyan.
- **Rules:**
  - Research before designing ([game-character-design](../../game-character-design/SKILL.md)).
  - Halos are attached geometry, and the glow is VFX.
  - Make four views in one ChatGPT chat.
  - Respect the signal colours.
  - Show the owner options first.

## Tu Tien source images (01/11)

- **What happened:**
  - "AAA game concept sheet" gave a comic, cel-shaded look. "Photorealistic 3D render, Unreal Engine 5 look" fixed the rendering.
  - The `#00FF00` background came back as a mottled `#4ae261` that spilled onto the subject, so we moved to a flat neutral grey.
  - A realistic wolf with painted "corrupted veins" scored 5.8–6.9: rendered well, but with no identity. The next brief described a designed creature.
  - Generated material sheets stalled: 5.0, then 5.7.
- **Rules:**
  - Watch the render phrase.
  - Use a neutral or transparent background.
  - Design creatures; do not decorate real animals.
  - Define materials on a lookdev page in the game's renderer once generated sheets stall.

## Wordwoven map 1 concept (01/11)

- **What happened:**
  - Without a base frame, ChatGPT's layout scored 5.5–7.5.
  - With the owner attaching the real-camera base frame, the layout scored 8.3 and 8.5 (beauty 7.4 and 7.5).
  - The next repaint drifted the lower half up by 45–85 px, and layout fell to 6.4 and 6.5.
- **Rules:**
  - Base frames come from the owner, because ChatGPT's page blocks local files.
  - Give coordinates in the base frame's pixels and ask it to keep every position.
  - Re-check layout on every repaint ([game-map-concept](../../game-map-concept/SKILL.md)).

## Dragonhold dragon fire (29–31/10)

- **What happened:** code-drawn and generated fire went 11 rounds plus two tests and still scored about 6 (test A: 5.0 and 6.0).
- **The owner asked** why we insisted on making it ourselves, and what guaranteed that more rounds would pass.
- **Rules:**
  - After two rounds without a real gain, offer the sourcing route with a search brief.
  - Test packs on the bench with blind judges and a stop rule.

## The play build looked like toys (01/11)

- **What happened:**
  - Wordwoven defaulted to Low and showed its code-drawn 2D board; the 3D map needed `?view=3d`.
  - Dragonhold's build had no ground tiles, because a loader read them from `/art-src` in dev only.
  - Pieces had passed in dev and on sheets.
- **Rules:**
  - Grade the built play host at the owner's setting with no URL flags.
  - A dev-only gap is a P0 bug.

## Plastic-looking models (29/10)

- **What happened:** our processing step cut foes by about 58 % and trees by 84–91 %, stripped the normal, roughness and AO maps, and set a flat roughness. The Tripo originals were fine.
- **Rules:** follow MODEL_QUALITY.md: floors, keep the maps, and cut only on measured frame time ([tripo.md](tripo.md) §5).

## Post-processing that broke good art (29/10)

- **What happened:** four of six tickets had a passing generation that the tool step damaged: dark boxes in the sky, flattened mountain edges, dropped painted frames, washed-out icons. The self-grade still said 8.
- **Rules:**
  - Post-processing only crops, keys, resizes, fixes edges and adjusts global light by ±10 %.
  - Deliver a "generated | processed" pair for every piece ([briefs-and-sets.md](briefs-and-sets.md) §5).
