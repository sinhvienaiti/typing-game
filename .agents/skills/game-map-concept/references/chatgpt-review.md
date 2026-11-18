# Review and concept painting with ChatGPT

The owner's rule (01/11/2026): write the concept first, have ChatGPT review it and paint it, redo weak results, and only then plan the build.

## 1. Tools and limits

- **ChatGPT at chatgpt.com, Chat mode, thinking effort High,** on the owner's signed-in account but in your own tab, never the owner's or another session's tab. Never Work mode: the "1 % usage left" meter belongs to Work, and Chat mode is free to use.
- **When ChatGPT hits its limit,** use Gemini (the owner is signed in). Or use Adobe Firefly Image 5 with the base image as the composition reference, Adobe's own model only.
- **Never sign in or type a password.** If a tool shows signed out, stop and tell the owner.
- Tabs, getting images out and the other browser rules are in [game-art-pipeline browser tools](../../game-art-pipeline/references/browser-ai-tools.md).
- **The in-app browser could not attach a local image to ChatGPT** (01/11): mixed content blocked it, and pasted images did not arrive. So the owner attaches the base image to the chat.
  - Check whether this still holds before asking.
  - Never send the painting request without the base. Without it ChatGPT invents its own layout: layout scored 5.5–7.5 without a base and 8.3–8.5 with one.
- **ChatGPT is a second opinion, not an authority.**
  - Check its claims against the frame numbers and the game's rules.
  - Where it is wrong, say so in the doc. Dragonhold kept its 1.4× character scale against the review's "tiny defenders", and gave the reason.

## 2. The review message (paste as one message)

Keep it in `<game>-CHATGPT_MESSAGE.md` beside the concept, with a line on top saying which image to attach. Structure:

1. **(a) What to do.**
   - Review map N as a senior art director of commercial top-down games.
   - Score it 0–10 (9 is a top commercial key frame, and 8.5 is our bar).
   - List the gaps: scale, depth, light, colour script, focal points, readability, life.
   - Propose concrete changes that keep the layout and camera exactly, each with its screen position.
   - Then paint over the attached base, score your own painting, and repaint if it is below 8.5, at most three tries in that chat.
   - Give the other maps a one- or two-line idea review, and name the weakest idea at this camera.
2. **(b) Hard constraints.**
   - The commercial bar, described in words: the owner's reference and the accepted key art.
   - The camera, with the no-sky line and the height-budget table.
   - The readability rules (word cards are the brightest things, the ground under them is calm, roads one step brighter).
   - The reserved colours, the content rules (English, no text, the game's banned motifs).
   - Buildability: our models, free CC0 assets and MIT shaders; a bespoke model only if it is clearly worth one.
3. **(c) The map concept, condensed.**
   - The story, what the frame shows (with screen positions) and the moment to paint.
   - The legend table (block colour, element, screen box).
   - Light and mood, materials, and what carries the scale.
   - "Today's frame, for honesty": what it looks like now, plainly.
4. **(d) The other maps,** one paragraph each.
5. **(e) The attachment:** the base image's path and what it is.

**If the base cannot be attached at all,** ask ChatGPT for the review and for the image prompt only. Paint later, with the base, in a chat or tool that accepts it.

## 3. Folding the review into the concept

- Save the reply as `<game>-CHATGPT_REVIEW.md`. Include the model, the mode, the chat URL, the input file, the score, the gaps table, the changes by screen region, its prompt verbatim, and its notes on the other maps.
- Raise the concept's version. Where the review and the draft disagree, **the review wins** unless it moves gameplay, the camera or a HUD zone. Mark each change inline, for example: "*v1.1 had gold sun patches on the meadow; the review wins.*"
- **The painting prompt is the reviewer's own text, verbatim.** It replaces your draft prompt, which may still carry colours or ideas the review removed.
- Apply the review's colour fixes everywhere they reach: hero briefs, Tripo prompts, other stages. Last Line's "ivory, not gold" changed the heroine's source prompts before any image was made.

## 4. Painting and retries

- **Over the base,** same camera, same 1280×720 framing, the HUD boxes flat grey, no text, sky, horizon or UI.
- **ChatGPT returned 1672×941** (16:9). Scale it to 1280×720 before you measure anything.
- **Score each try blind** (`judging.md`), then send a retry message in the same chat. A retry message:
  1. Gives the judges' numbers for each criterion, with the pass mark ("market level 7.4 / 7.5, layout 8.3 / 8.5, readability 6.8 / 7.5; the pass is 8.5 on each").
  2. Says what is right and must be kept ("the layout matches the base, so keep it").
  3. Asks to "regenerate the whole painting with your image tool over the base frame": same layout, camera and scale, every element on its block.
  4. Gives numbered fixes, each with an exact pixel box in the 1280×720 frame and the target ("Archer Tower centred at (378, 504), within x 308–425, y 380–530").
  5. Restates every HUD box exactly, as flat mid grey with nothing inside.
  6. Ends with "No text, no sky, no horizon, no word cards or UI labels. I will save it as <file>."
- **Watch for the drifts ChatGPT made on 01/11.** Name each one in the retry if it shows:
  - the lower half drifted up 45–85 px, and pieces moved right 50–60 px;
  - the centrepiece grew 2.9× and the hero creature almost as large (the toy read);
  - a road loop closed, or an extra footpath appeared that reads as a third lane;
  - a black pit or a structure was invented where the threat should stay off-screen;
  - foes looked like villagers or cute animals, or wore our side's colour;
  - dark foes sat on dark ink;
  - shadows had no caster, light shafts disagreed with the shadows, or there were two suns;
  - roads came out three value steps too bright, or darker than the grass in shadow;
  - mist became the brightest mass, or a footpath and wall were added to fill a quiet area;
  - glowing gold veins and ore, pink-purple flower dots, red banners;
  - a rampart drawn front-on instead of from the high camera, or a tower cut by the frame edge;
  - HUD boxes shifted, shrunk or missing.
- **At most three tries per round in one chat.** Still below the bar? Change something real: a fresh chat with the base, Firefly Image 5 with the base as the composition reference, a reduced brief, or a fix to the concept itself. Never pass the best of three (owner, 01/11: "tôi không muốn dùng tạm được nữa, tôi muốn phải đạt trên 8.5 trở lên").

## 5. Records

For every message, write a sidecar `<painting>.prompt.txt` next to the image with:
- the time sent, the mode and effort, and the chat URL;
- the result's file name, pixel size and the image it revises;
- the judges' scores it answers;
- the exact message. For a long message, also note its length and SHA-256 after checking that the composer matched it.

This is how the next try, and the next agent, know what was asked.
