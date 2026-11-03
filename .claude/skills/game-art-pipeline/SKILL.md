---
name: game-art-pipeline
description: Make player-facing art and media with AI tools and accept a piece only by two blind judges, in any game of this repo (for example Dragonhold, Wordwoven, Last Line, Tu Tien, Space Typing) or a later one. Use when briefing, generating, sourcing or reviewing 2D art, UI art and icons, title or key art, backgrounds, 3D model sources or Tripo models, or audio files; when driving ChatGPT, Gemini, Firefly or Tripo in the in-app browser or CLI; when an art round stalls; and whenever you must decide whether something the player sees or hears is accepted. Characters start in game-character-design, maps in game-map-concept, combat VFX in game-vfx-layered and always-on character glow in game-hero-presence-vfx; use those first, with this skill for their tools, judging and Tripo steps. Not for runtime import, rigging, animation or audio-mixing code.
---

# Game art pipeline: make with AI, accept by blind judges

Everything the player sees or hears is accepted only when **two independent blind judges both score it 8.5 or higher** in the built play host at the player's settings, with no URL flags. Shared systems (typing feedback, keyboard sounds, character animation) need **9**. There is no provisional pass, no "best of three tries" and no "better than before". Owner, 01/11/2026: "tôi không muốn dùng tạm được nữa, tôi muốn phải đạt trên 8.5 trở lên". Living rule text: [ART_ACCEPTANCE.md](../../../docs/games/ART_ACCEPTANCE.md) (01/11 block) and [AGENTS.md](../../../AGENTS.md).

This skill is the method. Each game keeps its own data: reference board, signal colours, judging files, Tripo list. Game names in this skill are examples, not scope. Related skills: [game-character-design](../game-character-design/SKILL.md) for any character, [game-map-concept](../game-map-concept/SKILL.md) for maps and scenes, [game-vfx-layered](../game-vfx-layered/SKILL.md) for combat VFX. Space Typing's [game-asset-2d-to-3d](../game-asset-2d-to-3d/SKILL.md) covers only that game's runtime.

## Procedure

1. **Reuse before you make.**
   - Look at accepted art in every game.
   - For any foe, search [MONSTER_MODEL_INVENTORY.md](../../../docs/games/MONSTER_MODEL_INVENTORY.md) first and retexture, recolour, rescale or re-rig. A ticket for a new monster says why nothing there fits.
   - Check free, commercial-safe sources ([licences](references/licences.md)).
2. **Brief for appeal.**
   - Every visual brief asks for captivating, stylish, luxurious, modern design with rich detail ([briefs](references/briefs-and-sets.md) §1).
   - A piece that is correct but plain, simple or generic fails 8.5.
   - For taste calls (heroes, title art, key UI), research first and show the owner a few options before building on one.
   - **Spectacle, not realism** (owner, 02/11: "chúng ta k làm ra kiểu âm thanh như thật, hay hình ảnh hiệu ứng như thật… phải bùng nổ, đẹp, hào quang, thu hút của các phim anime hoặc các thần thoại, tiểu thuyết"). Images, models, VFX and sound aim at anime and mythic spectacle: explosive, radiant, haloed, luminous, captivating, as in donghua and anime films and in games like Genshin Impact, Honkai: Star Rail and Wuthering Waves. Never brief realism as the goal ("photoreal", "realistic", "museum-accurate", foley-real sound); real references only feed shape and texture. Judges score against anime and mythic commercial references.
   - **Research loved designs before any object** (owner, 02/11: "mỗi khi thiết kế một thứ gì, bạn nên kêu chatgpt tham khảo các mẫu được nhiều người yêu thích… tránh copy nhưng phải có nét đẹp riêng"). Before the first image or model of a weapon, item, relic, prop, UI frame, icon or effect shape, ask ChatGPT to research the most-loved designs of that kind with links (checked or from memory), why players love them, design principles, and three clearly different directions of our own. Make it self-review: links real, nothing too close to an existing design. Verify its key sources, then draw, judge blind and show the owner. A plain shape drawn straight from your own prompt (a box guard on a plain blade) is the failure this rule exists for.
   - **Plan the presence around every object** (owner, 03/11: "những hiệu ứng như vậy xung quanh vật phẩm, trang bị, kỹ năng là rất cần thiết, nó đem lại cái nhìn cho người chơi hứng thú hơn").
     - A brief for an item, piece of equipment, weapon or skill object names the effect that will surround it in game: an aura or sheath, motes, streamers, or a rarity glow ([game-hero-presence-vfx](../game-hero-presence-vfx/SKILL.md)).
     - The art itself stays clean: no glow painted into a 3D source.
     - A bare model or icon reads crude, however good it is.
   - **Reference images and a prompt review before generating** (owner, 02/11, after four rounds of weapon sheets: "liệu bạn đã tự review lại prompt chưa, đã nhờ chatgpt review lại prompt, cải thiện prompt chưa, đã lấy 1 số hình ảnh để tham khảo để 2 bạn có hình mẫu tạo ra prompt chưa"). Text research is not enough.
     - Have ChatGPT find and show real reference images in the chat (official game pages and wikis, via its web search) and say what makes each one captivating.
     - Then ask it to critique and rewrite your prompts against those references before any image.
     - Write prompts for an image model, not as a spec: lead with the style and the references, then the visual hooks, materials and light. Few numbers: image models ignore centimetres and percentages. Do not ban glow so hard that the image goes grey.
     - Test one piece, judge it, then make the rest.
3. **Fix one set standard before the first image of a set** ([briefs](references/briefs-and-sets.md) §2). The same block goes into every prompt of the set:
   - one render phrase and one light;
   - one material sentence per object and one motif;
   - one background;
   - margins of at least 6–8 % and no cast shadow;
   - tall objects in a 3:4 frame.
4. **Pick the tool** ([browser AI tools](references/browser-ai-tools.md)).
   - **ChatGPT**, Chat mode, thinking High, never Work or agent mode: concepts, Tripo sources, four-view sheets, paintings over a base image, web research.
   - **Gemini** when ChatGPT refuses because of its image limit. Never mix tools inside one set: redo the whole set in one Gemini chat.
   - **Adobe Firefly**, Adobe models only: transparent video VFX, sound effects, alternative images.
   - **Tripo** only from an accepted source.
   - Never sign in or type credentials. If a tool is signed out, stop and tell the owner.
   - Work in your own tab and close it at the end. The in-app browser holds about 9 tabs.
5. **Get files out and record them.**
   - Run a copy of the local receiver from `.local/ff-bridge/` and post images to it ([recipe](references/browser-ai-tools.md) §4).
   - Name each try `<id>.v<n>-try<k>.<ext>` and save the exact prompt beside it as `.prompt.txt`.
6. **Check mechanically before any judge** ([briefs](references/briefs-and-sets.md) §4). This covers frame margins, one connected object, no cast shadow, and a contact sheet of the whole set. Also make a "generated | post-processed" pair that proves the tool step did not damage the painting.
7. **Judge blind, where the player sees it** ([judging](references/judging.md)).
   - Use two fresh judges, neutral labels and a key outside their folder.
   - Each judge writes what they see before any score.
   - Score market level against the commercial reference board, appeal, and fitness for the next step.
   - Grade icons and UI at real size in their UI spot. Grade world art, models, VFX and layout in the built play host.
   - Your own grade and a tool's self-grade do not count.
   - **The owner reviews every sample and signs off last** (owner, 02/11: "hình ảnh, hiệu ứng, âm thanh, vfx, đều phải gửi tôi mẫu để tôi review"). Send each image, model render, VFX clip or sheet and sound file to the owner as soon as it exists (SendUserFile, one-line caption with the direction, try and any judge scores). Nothing is built on, sent to Tripo or wired into a game before the owner picks or approves it.
8. **Iterate with a stop rule.**
   - Fix exactly what both judges named.
   - After two rounds without a real gain, change method in the same report: ready-made free sources, a lookdev reference, another tool, or a search brief for the owner.
   - **Three tries, then discuss with ChatGPT** (owner, 02/11: "mỗi khi làm gì quá 3 lần mà không thấy cải thiện, bạn và chatgpt nên trao đổi để có phương án tốt hơn"). Count tries per problem. After the third try with no clear gain, never start a fourth of the same kind: show ChatGPT the attempts (images or clips), the judges' notes and scores and what was tried, ask why it is not improving and for different approaches, challenge the answer, pick one and tell the owner. This holds for any work, not only images.
   - **Reference first, then a batch** (owner, 02/11, after 13 Clear Wind rounds swung between 7.2 and 8.2: "sai mãi vẫn sai… kêu chatgpt đưa vài mẫu mà bạn cảm thấy trên 9 điểm, sau đó đưa tôi review"). Stop regenerating from judge notes. Have ChatGPT show 10–12 existing loved designs of that kind as pictures with source links; send the owner the ones you rate 9+; from the one he approves, have ChatGPT write a prompt that keeps its quality and rendering, improves it a little and keeps our own design identity (no copying another game's item); generate 3–5 candidates at once and send them all to the owner before any judge.
   - **Analyse each reference; one style per candidate** (owner, same evening, after five prompts gave one identical sword: "phải phân tích chi tiết của kiếm… mỗi mẫu kiếm đều mang phong cách khác"). For each reference write down its silhouette, guard or head, blade, fittings, materials, colours, light, motif and why it is beautiful, then write one prompt per reference that carries that style into an original design of ours. Do not lock every prompt to one fixed design or palette, and draw each candidate in a fresh chat: inside one chat the image model reuses the last design.
   - **Showcase art is rich, not clean** (owner, 02/11: "bạn tạo kiếm xấu thật sự, nhìn nó quá mức đơn giản… nó k kiểu mấy loại trong tiểu thuyết tu tiên"). Never write "sparse ornament", "restrained", "clean silhouette", "one material" or "generous empty space" into a showcase prompt, and do not ban the warm-metal accents the references use; readability at small size is solved later in the model and its LOD. Rule from the discussion with ChatGPT: **one dominant thesis, two secondary ornament systems, three material families, one emotionally specific aura domain**. Put the luxury at the joints (blade root, collar, guard, grip, pommel, tassel or bead), make the guard a small composition (nested rings, petal tiers, openwork, hanging ornaments, gem nodes), and make the background the item's own domain (an array answering the artefact, a forge behind a fire blade), not generic scenery. For a genre with its own grammar (xianxia), give the image model that vocabulary in words; when it is missing, the model fills gaps with generic fantasy shapes.
   - Never wire a piece below the bar. Anything already wired below it is a debt in `docs/games/QUALITY_RESCUE_2026-11-01.md`.
9. **3D** ([tripo](references/tripo.md)).
   - Generate on Tripo only after both judges give the source 8.5, including Tripo fitness.
   - Dry-run first, build one model first, set `face_limit` by class, and log credits.
   - Keep detail per [MODEL_QUALITY.md](../../../docs/games/MODEL_QUALITY.md).
   - Tripo makes the look. Rig, clips, motion and VFX are ours.
10. **Audio** ([audio](references/audio.md)).
    - Real files only, made through [AUDIO_PIPELINE.md](../../../docs/games/AUDIO_PIPELINE.md).
    - Combat sound is powerful, explosive and reverberant ([audio](references/audio.md) §5): layered ingredients, loudness tiers, a baked tail plus an in-game reverb send, priority and ducking. Never "small, quiet, faint" for combat; the keyboard rules stay with keys and UI.
    - Agents cannot hear: the Audio Lab critic gates and the owner's ears decide.
11. **Close out.**
    - Record licence rows in `docs/games/THIRD_PARTY.md`, Tripo credits in the game's Tripo log, and the update in the game's changelog.
    - Prune raw capture frames, close your tabs and stop your receivers.

## Hard rules

- **No code-drawn stand-ins** for art: no SVG or canvas scenery, no CSS-shape icons, no emoji, no fallback paintings. A missing image is a ticket, never a drawing in code. Shaders and VFX that meet [VFX_STANDARD.md](../../../docs/games/VFX_STANDARD.md) are allowed. Sound counts too: no synthesized placeholder sounds.
- **Every UI detail carries real art:** cards, buttons, bays, labels, tooltips, briefings, results and shop items. Text alone is not enough.
- **Language:** everything the player reads is English, game nouns included; unique characters keep their proper names. Vietnamese appears only where the game teaches it: the meaning of the word being learned and optional glosses in learning panels.
- **No media in Git:** no images, audio, `.glb`, `.gltf` or `.bin`. Stage explicit paths, never `git add -A`. Media travels by `pnpm media:push`.
- **Captures** go under the game's or worktree's `tmp/`, never `art-src`, `public` or `docs`.
  - When a step is scored, keep sheets, compare shots and numbers, and delete your own raw frames: `node tools/capture-prune/prune.mjs <folder>` first, then `--apply`.
  - Never delete files you did not create.
  - GPU browser runs go through `.local/bin/heavy.sh --gpu`.
- **ChatGPT is a second opinion,** never an authority. Verify each key claim at its source and say where you disagree. Weigh its art critiques; do not copy them.
- **Never feed a cloud AI** (ChatGPT, Gemini, Tripo) with NoAI-tagged assets, Sketchfab or Fab "Standard" assets, Mixamo files, Poly Pizza service assets or Sonniss audio. For Sonniss this includes Claude: touch it only through local signal measurements ([licences](references/licences.md) §4).

## References

- [judging.md](references/judging.md): bar, blind-round setup, judge brief template, where to grade, scores you cannot trust.
- [briefs-and-sets.md](references/briefs-and-sets.md): appeal language, set standard, four consistent views, post-checks, post-processing limits.
- [browser-ai-tools.md](references/browser-ai-tools.md): ChatGPT, Gemini and Firefly rules and recipes, the local receiver, tab hygiene.
- [tripo.md](references/tripo.md): wallet, dry-run, face limits, one model first, credit log, import.
- [licences.md](references/licences.md): allowed and banned licences, verifying on the page, sourcing when iteration stalls.
- [audio.md](references/audio.md): audio route, who judges sound, stop rule, banned sources; combat sound (§5): layer recipes, tiers, frequency roles, Firefly wording, the tested ffmpeg chain, reverb, the trap we fell into.
- [worked-examples.md](references/worked-examples.md): what went wrong in Dragonhold, Wordwoven, Last Line and Tu Tien, and the rule each case produced.
