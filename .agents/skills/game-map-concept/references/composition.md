# Composition, light, value and colour for a play frame

All three map 1 concepts were reviewed on 01/11 and scored 7.9–8.1. In each case ChatGPT's verdict was the same: the frame was held back by hierarchy, not by asset quality, because every idea tried to be memorable at once. Wordwoven was told it "should not be redesigned. It should be edited." Write each rule below into the concept as numbers and screen boxes, not adjectives. "Word tags" and "word cards" stand for the world-anchored UI the player must read at a glance: the words to type in this repo's games, or whatever a later game puts over the world.

## 1. Read order and the hero landmark

- **Write the read order as a ranked list of 3–5 items.** Nothing lower may outshine anything higher. Typical order:
  1. the threat's source, or the hero dialogue;
  2. the lanes and the defensive line;
  3. the setting's scale (gorge, abyss, wall);
  4. secondary life.
- **One hero landmark per stage,** or one dialogue between two figures. In Dragonhold, living fire on the platform faces dead stone on the cliff.
  - Supporting landmarks (towers, cascades, gates) sit 15–25 % lower in contrast and detail.
  - Two landmarks that compete for the eye are a reject.
- **Each stage of a chapter gets one unmistakable dominant silhouette** and its own light or weather. Stages that differ only in colour read as one map. A darker or corrupted version of a region changes silhouettes, damage, particles and materials, not just the tint.
- **The landmark's brightest part sits in a free band of the frame:**
  - never under the word tags or a HUD card;
  - never right behind the foe lane;
  - never in the area round the player's eye.

## 2. What carries the scale when the camera looks down

Commercial top-down games make a field feel epic with ground that is a painting, landmarks at the field's edge, a world edge that drops away, giant shadows, raking light and life (ART_DIRECTION §1.2). With a small height budget, scale comes from:

- **Things lying on the ground,** read from above: an ink tide, a 16 m inlaid ring, river beds, terraces.
- **Things cropped by the top edge:** trunks and low boughs with crowns overhanging from beyond the frame, a spur whose top leaves the frame, a gate whose arch just fits.
- **Things below the play surface:** an abyss with structures rising from far below, seen from above. Last Line's 2.4 km ring stands 6 km out with its centre about 1 km below the deck, and only its lower arc shows.
- **Giant shadows:** one or two huge cloud shadows, never mottled patches, and the long shadow of a flying beast.
- **The wings:** a colossus or cliff just outside the play circle. Dragonhold's Warden stands 22 m tall, ten times a soldier as drawn.
- **Life:** a muster crowd at the gate, a defensive line, workers.

**Rules of scale:**
- A hero landmark is at least ten times a standard unit as drawn. Characters are usually drawn larger than true scale for readability (Dragonhold uses 1.4×). Keep that scale, and let masonry courses, narrow stairs and oversized fractures carry the size instead.
- A megastructure far away must carry its own scale. A smooth lit arc reads as a few hundred metres. It needs:
  - thickness (a section deep enough to show mass);
  - giant structural divisions;
  - asymmetric damage, with missing chunks and exposed layers;
  - hidden stretches lost in haze or shadow;
  - atmospheric falloff, with only the nearest edge crisp.
- A centrepiece that is too big turns the whole map into a model. Dragonhold's painted bastion came out 2.9× its block and the dragon almost as large, and the judges read a toy. Hold every piece to its block.
- Nothing taller than about 3 m stands in front of (below, on screen) a lane or build ground. Anything between the camera and a lane or a word tag dithers to about 35 %.

## 3. Depth bands for a frame without sky

| Band | Treatment |
|---|---|
| Foreground frame (bottom band, mostly under the HUD) | A heavy, darker band (25–35 % below the playfield): ramparts, parapets, dark crowns in the lower corners. A frame, never the subject |
| Playfield | The crispest and clearest ground. Lanes in their own materials. Within 2–4 m of a lane or the defended point the ground stays simple |
| Wings | Cliffs, colossi, forest walls, world edges. Darker toward the corners |
| Far band (top) | Darker and softer than the playfield: lower contrast, no fine detail. It reads as far because of value and softness, not because of fog |
| Below the surface (if the field stands high) | An abyss, a gorge or a sea of cloud, layered, with haze between the layers |

- No uniform fog over the map. Mist lies only in hollows, river beds and the abyss.
- Light shafts stay faint and few, never a gold field. Use broad columns and soft strata, not many thin god rays.

## 4. Light budget

- **One key light** with a named time and direction, for example "dawn, bearing 70°, elevation 24°, gold from the upper right".
  - Every cast shadow in the frame agrees with it.
  - A shadow without a caster, or a second sun, is a reject. Judges caught both in paintings.
- **A weak fill.** Shadows take the map's shadow hue (jade, pine green, navy), never black. A high sun with a strong fill gives the flat light of a toy.
- **Write a ranked light table:** rank, what, where (screen box), rule.
  - Rank 1 is the one brightest mass, where the eye must look.
  - Then the defended line, then shots and gun light (short-lived), then hero accents, then foe accents, then the environment's sources, then support lights at low contrast.
- **The reserved warm light lands on a named list of places only.** In Dragonhold that is the Warden's east planes, the bridge crowns, the platform rim and a few grass edges; the meadow stays subdued.
- **Lanterns and lamps are small cores, not pools of light.** Signal lights (lane cues, parapet lights) sit dark at rest and pulse on the event.
- **Mist, haze and plasma are never the brightest mass.** Nothing in the world reaches the brightness of the word cards.
- **Bloom only on fire, magic and thin HDR cores.** The numbers are in VFX_STANDARD.

## 5. Value hierarchy (the gameplay read)

Write a value table in grey percent for the map's surfaces. Wordwoven's, accepted by the review:

| Element | Value |
|---|---|
| Threat interior (rift, ink) | 8–15 % |
| Deep vegetation and shadow | 20–30 % |
| Meadow | 30–42 % |
| House pads | 35–50 % |
| Road | 48–58 % |
| Sunlit stone | 55–65 % |
| Word cards and VFX | above all of these |

- **Lanes are one clear value step over the ground beside them, and no more.**
  - The floor is luma ≥ grass + 0.15 (PATH_QUALITY), or a ratio of about 1.3 on stone floors.
  - A painting with roads three steps too bright failed readability just as one with roads too dark did.
- **The ground under word tags stays at luma 0.6 or below.** No snowfields, pale quarry floors or sunlit water behind tags.
- **The play zone round the player's eye is the calmest, darkest large region.**
  - Last Line's basin round the heroine sits 1–2 values below the mid lane, at most +0.02 luma over the old frame under the word line.
  - Ground round houses stays under 60 %.
- **Foes separate from the ground.**
  - Either near-black silhouettes on a mid-value lane with a warm rim on one side and a cool rim on the other, or mid-value bodies with a rim on dark ground.
  - Give them contact shadows (AO or a soft blob) so they stand on the ground and do not float or sink.
  - Never put dark foes on dark ink: lift the ground under them to a mid tone, or rim them.
  - Foes never wear our side's colour. Wordwoven's zombies in navy read as our Spearmen.
  - Foes look like monsters, not villagers or cute animals.
- **Grey blur test.** In a half-size greyscale blurred copy, the lanes, foes, our units and health bars must still read, and decorative floors such as an inlaid ring must vanish.

## 6. Reserved signal colours and the colour script

Decide at the start which colours are signals, and write them as a table: colour, what it means, the rule. Wordwoven's rule: "the world never uses saturated versions of these." Patterns from the three games:

| Signal | Typical rule |
|---|---|
| The foe faction's colour (violet, blight yellow-green) | Only on foes, their eyes, veins and cracks, and the thin haze at their gates. No pools, washes or floors of it. A rift's body stays near-black, and only the foes in it carry the colour |
| Red | Foe attacks or the boss's slam only. No red banners, lines or placeholder glows |
| Gold | Leaders, word cards, typed letters or loot, whichever the game uses. Environment gold becomes muted ochre or ivory: no glowing ore, no gold armour on the hero, no gold sun patches |
| Our side's accent (cyan, ember) | Sparse: thin cores, a few px of bloom, never a glyph run down the lane |
| Keying colours (pink, magenta, purple, if used by tools) | Not in the world |

- **A colour script with shares.** Give each colour family its share of the frame and where it lives. Last Line's was graphite and navy about 60 %, near-black 15 %, plasma 15 % (abyss only), ivory 6 %, cyan 3 % and purple 1 % (foe veins).
- **Two main families against each other:** cool shadow against warm light. The most saturated colour sits only where the action is.
- **The loudest environment colour must not match a signal.** Last Line's orange-and-black wall stripes matched the foes' cracks.

## 7. Materials

- **Give each family one language, and keep the families apart,** so stone, grass and trees do not repeat. Dragonhold used four granites:
  - large dressed cream blocks for the fortress;
  - fractured cool grey for the cliff;
  - dark damp stone for the bridge;
  - polished worn flags on the lane.
- **Two lanes can differ by material,** for example engineered flags against packed earth with stepping stones. Both stay brighter than the ground beside them.
- **Write the surface rules as numbers:**
  - ground in broad bands (short grass, damp grass, moss, trampled), never one mint green;
  - water in an irregular bed, foam only at named places;
  - roads by PATH_QUALITY.
- **The style is the game's own choice; take it from its design docs.** Dragonhold (owner choice O1) and Tu Tiên (D52) chose painterly-realistic: real material response with a painterly grade. Whatever the style, scenery is never toy plastic, ink-outlined or flat colour.

## 8. Life before polish

- **Muster ground.** The next wave waits at its gate, view only, in shade. Only eyes or veins glint, and it thickens on a surge warning. The sim never reads it.
- **Defenders on structures, not near lanes,** so nobody mistakes them for blockers. Brief moments react to waves: shields raised, braziers flare, a horn (a real audio file).
- **Ambient motion:** smoke, banners and trees in one wind field, mist drifting, spray, embers, dust under marching foes, cloud shadows. Things beside the fight move: shuttles fleeing, workers chopping, owlets carrying.
- **Only creatures with a verified source.** No birds or animals until a free, commercial-safe animated source exists. Fireflies and embers are particles. Reuse monsters before you make new ones (`MONSTER_MODEL_INVENTORY.md`).

## 9. Dressing only what the frame shows

- **Clusters, not scatter.** Boulders at grove edges and banks, never small rocks sprinkled on the lawn.
- **Thin the vegetation within 2–4 m of a lane edge and the defended point:** short grass only, from none at 1.5 m to full at 4 m.
- **Trees at uneven spacing,** varied in crown, species and lean, with dark gaps and a clear channel where the lane enters. Never an even wall of canopy.
- **Retire park furniture** (rail fences, jetties, lily ponds, round-crown trees) and anything off the game's bible. List each piece you retire in the concept.

## 10. Beats

One beat per wave, day or night: light height, colour and weather change while the key direction stays. Write the beats as a table (beat, what happens, light, weather, colour). Night uses a cold low moon, amber lamp cores and thicker mist, and the foe's colour stays the only one of its kind.
