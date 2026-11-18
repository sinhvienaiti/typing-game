# The concept doc: skeleton

Write one concept doc per game, in English so it can be pasted to a reviewer.
- **Map 1**, or the next stage to build, gets the full treatment.
- **Other stages** get a short card each, and their own base image when their grey box exists.
- **Where it lives:** the three split games keep theirs at `docs/games/maps/<game>-MAP_CONCEPTS.md`. A new or split-out game keeps it in its own `docs/`.
- **Header:**
  - a version line that says what each review changed;
  - the sources you read, including code paths;
  - the projection script;
  - the art bar.

## 0. How to use this file with the reviewer
- What is done (review score, date), what comes next (the painting over the base), and the files: the message, the review, the base image, the legend.
- The reject list for paintings (see `judging.md` §3), with this game's specifics: its reserved colours, its forbidden motifs, and the hero's size in px.

## 1. Fixed rules for every map
1. **The field.** The sim facts that do not change: the size, the lanes, where foes enter, the defended point, the hazards and objectives that need room.
2. **The camera.** The numbers and the frame tables from `frame-budget.mjs`:
   - the sky decision;
   - the row table;
   - heights on screen of the standard unit, the hero and the boss;
   - the vertical budget at the places that matter;
   - what leans into the HUD.
3. **HUD zones** in px, and the free bands where a landmark's bright part may sit.
4. **Screen map.** An ASCII sketch of the 1280×720 frame, with the HUD boxes, the lanes, the defended line and the landmark zones at their y values.
5. **Rules that follow.** Where the brightest region may sit, what stays dark under the word line, height limits along the lane, and the budgets (draw calls, triangles, media).
6. **Reserved signal colours.** A table of colour, meaning and rule.
7. **Hero group and foes.** The look, the scale in px, the models (reused first), and what is still open for the owner.

## 2. One idea for the chapter, and its shared kit
- The chapter's single setting idea, and how stages progress through it (light, damage, weather).
- An intro sweep or title camera for everything the battle frame cannot show.
- **Kit table:** id (K1…), piece, how it is seen in the battle frame, its source.
  - Mark sources that need the owner's licence decision.
  - List what was dropped and why ("out of frame", "leans into the gun cards", "no verified source").
- Quality tiers: what Medium and Low drop.

## 3. Map N in full
1. Story beat and gameplay: the rules of the stage, its waves, its hazards.
2. The battle frame and its base image: a table of element, world position, screen box and block colour. Say once that block colours are labels, not paint.
3. The hero landmark: what it is, what part of it the frame shows, how it carries its scale, and its brightest box.
4. Depth layers: foreground, playfield, top band, wings, far, below the surface.
5. Light, value and colour:
   - key, fill and bloom;
   - the light-budget table;
   - the value plan by region;
   - the read order;
   - the colour script with shares;
   - the colour reservations in this frame.
6. Look by screen region: a table of area, box and look.
7. Kept out of the frame: each thing that would break the read.
8. Life: foes first, then defenders, then what happens beside the fight. Note any creatures removed for lack of a source.
9. Sources and build notes: a table of element, source, licence and state, plus the notes the build needs (deck rhythm, foam mask, shader masks, signal lights at rest).
10. What is wrong today: evidence from a play-build capture, with file names.
11. The concept painting prompt: the attachment, the tool and the prompt (the reviewer's own words, verbatim).

## 4. The other maps (short)
For each stage:
- gameplay;
- the landmark, placed by the script, with its screen box and the px per 100 m there;
- light and weather;
- life;
- sources.

Write no prompts until map 1's painting is accepted. Fold in the reviewer's notes, and replace the weakest idea it names.

## 5. Why the current maps fail
A numbered list of causes, not symptoms: "we built a system, not places", "the epic is where the camera cannot look", "toy rendering by construction", "the shipped build differed from dev", "we scored ourselves on our own scale". Then "what fixes it, in order".

## 6. What needs the owner
Only the blocking decisions: attaching the base image, licences outside the allowed list, Tripo spending, camera trials, retiring old models.
