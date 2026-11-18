# Briefs, set standards and post-checks

## 1. Appeal language for every visual brief

The owner, 01/11/2026 evening: "phần hình ảnh chúng ta phải làm nó thật đẹp, nhìn cuốn hút, phong cách, sang trọng, thời trang, hiện đại… đừng làm hình ảnh của game trở nên nhàm chán, đơn giản, thiếu đi sự hấp dẫn".

Put the goal into the prompt in concrete words:

- **Core line:** captivating, stylish, luxurious, fashionable, modern; rich detail through layered forms, premium materials, light accents and a strong silhouette.
- **Key art, backgrounds, title screens, skies:** epic scale, dramatic sky, depth, grand landmarks, cinematic light, painterly-realistic detail. Never "cozy rustic village" unless the game asks for it. The owner rejected a countryside look as "xấu đến thậm tệ" and asked for "đẹp và hùng vĩ".
- **Characters, companions and bosses:** follow [game-character-design](../../game-character-design/SKILL.md). That skill covers the research lenses, the appeal checklist, the radiance kit and which parts are geometry and which are engine VFX.
  - Short version for a hero or companion: royal and radiant, yet clearly a warrior.
  - A hero carries no villain cues: no full-face dark mask, no horn-like fins at the ears, no smooth toy-shell armour. Bosses and foes follow their own design brief.
- **Creatures:** design a creature with its own identity. A real animal with "corrupted veins" painted on it is not a design.
- **Icons:** bold, chunky silhouettes designed for 24–32 px, in the game's bright accent colour.
  - Avoid thin dark lines on dark panels and sound arcs that vanish when small.
  - Check that the meaning cannot be misread. Real misreads we shipped: settings read as a virus, accuracy as a snowflake, kills as a quill, next stage as a no-entry sign.
  - Brief the panel frames and buttons in the same art pass; they are not CSS.
- **Maps and scenes:** follow [game-map-concept](../../game-map-concept/SKILL.md).
  - Write for the real game camera. Can it see the sky? Which heights get cut at the top? What must never cover a road or a build spot?
  - Keep a brightness hierarchy (road clearly brighter than grass; foes lifted by foot shadows and rim light; a calm, darker play zone so word tags read) and one key light.
- **Signal colours are reserved per game.** Decide early which colours belong only to foes, foe attacks, elite foes and our side. Environment and UI art never use them at high intensity. Example: Last Line keeps gold for Pack Leaders, so the hero uses platinum and pearl.

Phrases that changed the result:

- **"AAA game concept sheet"** pushed Firefly to a comic, cel-shaded look.
- **"Photorealistic 3D render, Unreal Engine 5 look, studio product shot"** moved it to realistic rendering. Add "Not cartoon, not anime".
- **No style reference** lets Firefly drift to a flat mobile-cartoon look. Attach accepted pieces of the same family as a style reference ([browser-ai-tools.md](browser-ai-tools.md) §5), then check the result at play size, because references can add clutter.
- **Video:** describe the effect in time steps ("0–0.3 s a white flash, then…") and keep the subject centred.

**When generated material sheets stall, define materials in the game's own renderer.** Build a lookdev page with the game camera and post-processing, real CC0 PBR materials and a real HDRI, an 18 % grey ball and a chrome ball. Judge a capture of it. Once it passes, prompts point at that capture. Generated images stay concepts and shape sources; they no longer define the material.

## 2. Set standard: one block in every prompt of a set

A set that is not made against one standard comes out as several styles. Six landmarks once came back with five render styles, five stone colours, four dragon-head designs and five key greens. Before the first image, write one standard block and paste it, unchanged, into every prompt:

| Part | Rule |
|---|---|
| Render phrase | One phrase for the whole set (§1). |
| Material sentence | One per object. Split shared sentences: "iron and wood" pulled iron into a stone statue. Name the material concretely, for example "weathered sandstone in large irregular blocks, chipped edges, soot around carvings". |
| Motif | One design for a recurring motif (one dragon-head design, one crest), described the same way each time. |
| Light | One key-light direction and fill, the same in every image. |
| Background | Best: a transparent PNG (ChatGPT can deliver one). Otherwise a flat neutral mid-grey. Avoid `#00FF00` in Firefly: it drifts to a mottled `#4ae261` and spills green onto the object. For small icons, magenta works when the subject has no purple; use green when it does. |
| View | Three-quarter view about 30–35° around and about 30° from above, unless the game needs another view. Keep the same view for every object of the set. |
| Frame | One object, centred, with at least 6–8 % empty margin on every side. Tall objects (towers, standing figures) use a 3:4 frame: a tower in a square frame touched the top edge. |
| Clean | No cast shadow, no ground plane, no platform, no props, no text, no particles. |
| Make | Generate the set in one session, or one chat, using the same block. |

Template (fill the brackets, keep the rest word for word across the set):

```text
<render phrase>: <SUBJECT, with its own material sentence>. <view sentence>. One key light from <direction>, soft cool fill, no cast shadow, no ground plane, no platform. Single solid object, centered, 8 percent empty margin on every side, <background>. No text, no logo, no effects, no particles, no extra objects.
```

## 3. Four consistent views of one design

- **Firefly cannot hold one design across views.** The helmet changed between angles, and the "back" image was another front.
- **ChatGPT can, inside one chat:**
  1. Agree the design first. Show the owner options before the four-view step.
  2. Ask for a turnaround sheet of that design (front, three-quarter, side, back).
  3. Then ask for each view as its own image in the same chat: "same character, same outfit, only the camera changes", with the same aspect ratio and scale for each.
- Add a check panel at play size (for example 68 px tall) to see how it reads in game.
- Views feed Tripo multiview. See [tripo.md](tripo.md) and [game-character-design](../../game-character-design/SKILL.md).

## 4. Post-checks before any judge

Scripts live in `.local/ff-bridge/` (outside Git). Copy them to your scratchpad and run them with `python3 -I`; they need ImageMagick at `/opt/homebrew/bin/magick`.

- **`framecheck.py <png> [green|magenta]`** prints the margin per side (%), the bounding-box aspect, the share of the largest connected piece and any other piece of 0.1 % of the frame or more.
  - The script passes margins at 3 %. The brief asks for 6–8 %, so read the numbers, not only PASS.
  - CONNECTED passes when the largest piece holds at least 98 % of the foreground and there are no other pieces.
- **`shadowcheck.py <png>`** counts key-coloured pixels clearly darker than the border median, away from the object. More than 0.5 % of the background is a cast shadow, and the check fails.
- **The scripts only read a key colour:** `framecheck.py` takes green or magenta, `shadowcheck.py` green only. On any other background every pixel counts as object and the margins read 0.
  - **Transparent PNGs:** flatten onto the key first, then run both checks: `magick in.png -background '#00FF00' -flatten <scratch>/in.green.png`.
  - **Flat grey backgrounds:** flood the background to green from a corner first: `magick in.png -fuzz 6% -fill '#00FF00' -draw 'color 0,0 floodfill' <scratch>/in.green.png`. A cast shadow on grey is darker than the fuzz, so it survives the flood: framecheck shows it as an extra piece or a skirt at the base, and shadowcheck cannot see it. Look for it on the sheet.
- **When a check fails:**
  - **Margin too small:** regenerate with the margin sentence, or pad the canvas by extending the background. Never crop into the object.
  - **Not connected:** regenerate. Floating parts also break Tripo.
  - **Shadow:** regenerate with "no cast shadow, no ground plane". A soft contact shadow cleaned off a flat key is a fix only when the object's edge is untouched.
- **Set check:** put the whole set on one contact sheet at the same scale. Check render style, material, block size, motif and light side by side before you spend judge time.

## 5. What post-processing may and may not do

From the 29/10 acceptance round: four of six tickets had a good generation that the tool step damaged. Dark boxes were burned into a sky, mountain edges were flattened, painted frames were dropped, and gamma washed out icons.

- **Allowed:** crop, remove the background, resize, fix and seam edges, and change global light by up to ±10 %.
- **Key removal:**
  - flood from the border;
  - turn enclosed key pockets into dark glass;
  - un-mix the key colour on the edge and de-spill about 4 px;
  - drop small stray pieces (such as text the generator added);
  - centre the object.
  - De-spill only the object's edge, never the whole image.
- **Not allowed:** erase, flatten, fill with flat colour, or replace painted parts.
- **When a numeric threshold fights the painting** (passing the number would make the art dirty), keep the painting and report the conflict for a decision.
- **Record every change** after generation in the piece's `.prompt.txt`.
- **Deliver a "generated | processed" pair** at the same size for every piece. Self-grades and judges look at the processed file.
