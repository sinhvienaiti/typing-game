# Directions, views, sources and judging

## Directions for the owner

- **Make two or three directions that differ in idea,** not only in colour: a different signature shape, a different royal or divine source, a different radiance language.
- **Put each direction on one board:**
  - a front image;
  - a black silhouette at play size;
  - colour swatches with their shares;
  - the radiance kit list with its geometry-or-VFX split;
  - a check tile from the play camera at the real size;
  - one line that states the idea.
- **Score each direction against [the appeal checklist](appeal-checklist.md)** before showing it. Show only directions you would defend.
- **Let the owner pick.** Record the pick and his words. No turnaround, 3D source or key UI art before the pick.

## Tools

- **ChatGPT** (chatgpt.com, Chat mode, thinking High, never Work) for character views: inside one chat it keeps one design across views.
- **Gemini** (gemini.google.com) when ChatGPT's image limit is reached. Never mix tools inside one set: when you switch, redo the turnaround and every view in one Gemini chat.
- **Firefly** (Adobe models only) could not hold one character across four views. The helmet changed per view, and the "back" came out as a front. Do not use it for character views.
- **Browser:** your own tab, closed after; never sign in or type passwords.
- **Images from disk** (the owner's reference, a frame from the game) must be attached by the owner. The in-app browser cannot upload them.

## Turnaround, then views, in one chat

1. **Brief the chat.** In one chat, give the picked direction, the brief and the references.
2. **Ask for a turnaround sheet:** the same character seen from the front, left, back and right on one image. Same scale, same pose, one baseline, near-orthographic, flat even light.
3. **Check the sheet** (see Consistency below) and fix it in the same chat until the four views match.
4. **Ask for each view on its own,** still in the same chat and one view per request. For example: "the same character as the turnaround, same design and proportions, seen from directly behind".
   - Say what must show in that view and what must not.
   - The back view shows the back of the head or helmet, the back plate, the cape panels and the back core. It shows no face and no chest core.
5. **Let the 3D generator set the list of views.** Tripo multiview takes front, left, back and right; check its current docs before generating. A drone or a flyer may need a top view for the design sheet. Keep any view the generator does not take out of its input.

## Rules for 3D source images

- **Pose (humanoids):** A-pose, arms 40–50° from the body with a gap, feet flat at shoulder width, head straight. Cape and hair hang free: they do not cover the arms or legs and do not fuse to the legs.
- **Framing:** the whole figure, centred, with an even margin of at least 6–8 % (the ticket may ask for more), nothing cut off. One frame shape and size for every view (square worked for the Last Line heroine at 1254 px).
- **Background:** one flat key colour the subject does not contain, for example #00FF00 for a character with no green. No gradient, no shadow, no ground. Check for key-colour spill on the subject and remove it on the subject only.
- **Light:** flat, even and frontal. No cast shadows, no rim light, no painted glow or light rays. Emissive parts are painted as their colour; the radiance comes later, per [the pipeline decision](pipeline-decision.md).
- **One connected object.** Nothing floats, unless the pipeline decision makes it a separate part.
- **No text** of any kind: no letters, emblems with letters, signature or watermark.

## Consistency check (numbers go in the report)

- **Detail list:** write down 10–20 design details, for example:
  - the crown line, the crest, the collar;
  - the number of shoulder plates, the chest core, the light channels;
  - the cape panels and their trims;
  - hair, gloves, boots, colours.

  Tick each detail in each view. A detail that changes between views fails the set.
- **Proportions:**
  - The bounding-box heights differ by 3 % or less across views.
  - The top of the head, shoulder, hip, knee and foot sit at the same heights, within 3 % of the figure's height.
- **Palette:** sample the base, secondary and accent in every view. The hues match.
- **A back is a back:**
  - The back view shows no face, visor or chest core.
  - The cape and the back details are there.
  - Left and right are plausible mirrors, with asymmetric details on the correct side.

## Check tile at play size

- **Shoot the side the camera sees,** front or back, from the game's camera angle (for example from behind and 45° above).
- **Use the real on-screen height** at 1280×720 and at 1920×1080.
- **Place it on a frame of the real map,** next to an enemy.
- **Add a 256 px tile for the review sheet,** but grade at the real size first. Icons that passed on a 256 px sheet read as smudges at 24 px in the game.

## Judging

Two independent blind judges must both score 8.5 or more (`docs/games/ART_ACCEPTANCE.md`). Shared systems, character animation included, need 9 from both judges with no sub-score under 8.5, and the owner signs off last (`docs/games/SHARED_SYSTEMS_BAR.md`). Your own grade and a tool's self-grade do not count.

**Blind setup:**
- Labels are neutral (A, B, C), and the key stays outside the judges' folder.
- Judges never read the prompts or the reports.
- Each judge writes what it sees before it scores.
- Judges receive the views, the turnaround, the check tile and the board of commercial references.

**Criteria** (each scored, with what was seen):

1. **On brief:** the picked direction, with every required detail.
2. **Readable in game:** silhouette, focal accent and friend-or-foe read at the real size.
3. **Fits the set:** style, light and palette match the game's accepted art; reserved colours are respected.
4. **Form:** anatomy, limbs, perspective and construction are sound.
5. **Fit for the next step:** pose, framing, background, flat light, one object.
6. **Appeal:** captivating, stylish, luxurious, modern, with rich layered detail (checklist items 1–8 and 11).
7. **Market level:** it holds up next to the commercial reference board.
8. **Consistency:** the same design in every view. A multiview set with any inconsistency fails, whatever its other scores.

**Below 8.5:** name the fault and fix that fault. There is no "best of three" and no "better than before".

## Then 3D

- **Start 3D only** after both judges pass the sources at 8.5, fitness for the generator included.
- **Follow [game-art-pipeline](../../game-art-pipeline/SKILL.md)** and `docs/games/LESSONS_FROM_THREE_GAMES.md` §4:
  - the API wallet first, and a dry run before every build;
  - a face limit per model class (the living numbers are in that section and in `docs/games/MODEL_QUALITY.md`);
  - one model first, inspected (triangles, maps, a turntable) before the rest;
  - never smart low-poly, never Tripo's auto rig.
- **Rig, clips, procedural motion and VFX are ours.** Plan the bone chains for cape and hair and the VFX sockets from the design.
- **Final acceptance** happens in the built play host, at the player's settings, with no URL flags.
