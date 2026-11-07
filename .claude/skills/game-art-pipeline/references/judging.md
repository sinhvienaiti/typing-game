# Judging: the acceptance protocol

Living rule text: [ART_ACCEPTANCE.md](../../../../docs/games/ART_ACCEPTANCE.md) (01/11 block) and [SHARED_SYSTEMS_BAR.md](../../../../docs/games/SHARED_SYSTEMS_BAR.md). This file is the method that has held up in practice.

## 1. The bar

- **8.5 from both judges** for everything the player sees or hears: 2D art, UI, icons, title and key art, maps, 3D models, VFX and audio.
  - Both judges must clear the bar. Do not average: 8.0 and 9.0 is a fail.
- **Shared systems need 9 from both judges**, with no sub-item under 8.5, and the owner signs off last. These are the typing feedback, the keyboard sound profiles and character animation.
- **No provisional routes.** No "best of 3 tries", no "better than the old one, so wire it", no "7 is enough for 3D".
  - The old tables in ART_ACCEPTANCE §2 are history. Read any 7 or 8 there as 8.5.
- **Appeal is scored.** The owner, 01/11 evening: "đừng làm hình ảnh của game trở nên nhàm chán, đơn giản, thiếu đi sự hấp dẫn".
  - A clean, technically correct piece that is plain, simple or generic does not pass 8.5.
- **VFX** must also meet the measured checks of [VFX_STANDARD.md](../../../../docs/games/VFX_STANDARD.md) (§5.6). The score bar is still 8.5.
  - **Two tiers** (owner, 07/11/2026). VFX source layers (clips, renders, stills, flipbooks, sprites) are judged pass or fail on fitness. The 8.5 score is for the composited effect in the play host. A lone layer never has to reach 8 by itself.
- **A piece already wired below the bar** is an open debt in `docs/games/QUALITY_RESCUE_2026-11-01.md`, not done work.
- **Checkpoint at 7: report it with a demo video** (owner, 03/11: "mọi hình ảnh, hiệu ứng từ 7 trở lên thì cứ báo cáo tôi, gửi tôi video demo để tôi đánh giá"). It extends the 02/11 rule for motion.
  - As soon as both judges score a piece (image, VFX, model, map, UI, motion) at 7 or more, send the owner a real-speed demo video, with sound where the piece has sound.
  - Add the two scores, what is done, and what still separates it from 8.5. The owner works remotely, so send a file, never a localhost link.
  - It is a checkpoint for his review, not a pass: keep going to 8.5.

## 2. Setting up a blind round

1. **Judges are fresh agents.** They are not the maker, not the lane, and not judges who saw earlier rounds of the same piece, because earlier rounds anchor them.
2. **The judge folder holds only:**
   - the candidate sheets or images;
   - the reference board;
   - a README saying what each sheet shows, for example "1080p play camera, light ground".
3. **Labels are neutral** (A/B/C, c1/c2, or "current" for the piece now in game). The key that maps labels to files sits **outside** the judges' folder.
   - When replacing a piece, include the current in-game piece as one label.
   - Never tell judges which one you prefer or which one is new.
4. **Judges are cut off from your reasoning.** They do not read reports, `.prompt.txt` files, changelogs, source code or other judges' notes, and they do not message anyone. Their crops go to their own scratch folder and are deleted at the end.
5. **The reference is the market, not our style guide.**
   - Each game's commercial reference board counts as 9. Dragonhold, Wordwoven and Last Line hold the owner's image at `games/<id>/art-src/_refs/owner-epic-2026-10-28.webp` (outside Git); a new game starts its board from that image plus commercial games of its own genre.
   - Add commercial screenshots of the same genre for UI, icons and characters.
6. **Order of the judge's answer:**
   1. What you see: one or two plain lines per piece, written before any score and before reading the key.
   2. Scores per axis (§3).
   3. The five biggest gaps to 8.5, concrete: where on screen and what it looks like.
   4. A verdict per piece: accept, fix (with the exact change) or redo (with the reason).
   5. For a set: do the pieces read as **one set** (render style, material, block size, motif, light)?
7. **Judges answer in Vietnamese** in this repo, because the owner reads the notes.

### Judge brief template

```text
You are Judge <X>, a strict, independent blind judge. Look ONLY at <judge folder> (its README says what each sheet shows) and at the reference <reference board>, which counts as 9/10 (commercial game, market level). Do not open the key file, reports, .prompt.txt files, changelogs, source code or other judges' notes; do not message anyone; your crops go under <your scratch folder> and are deleted at the end. Pass mark 8.5 on every axis.
For each piece: first write in one or two lines what it looks like. Then score M (market level: 9 = equal to the best commercial games of the genre, 8.5 = premium commercial asset, 8 = shippable but ordinary, 7 = tidy but ordinary, 5 = toy-like), A (appeal: captivating, stylish, luxurious, modern, rich detail; plain or generic cannot pass) and F (fitness for <next step>: <checklist>). Then: the five biggest gaps to 8.5, concrete (where, what it looks like); whether the set reads as one set; and a table: label, M, A, F, verdict (accept / fix: exact change / redo: why). Reply in Vietnamese.
```

## 3. Score axes

| Axis | What it asks | Notes |
|---|---|---|
| **M** market level | Does it hold up next to the commercial references? | Always scored |
| **A** appeal | Captivating, stylish, luxurious, modern, rich detail? | Always scored for visuals |
| **F** fitness | Is it usable for the next step? | Depends on the kind (below) |
| **Set** | One render style, material, motif, light and palette? | For any set of two or more |
| **Layout / readability** | Placement matches the base frame; foes, roads and word tags read at play size | For map concepts and scenes |

F checklist by kind:

- **Tripo source:** one connected solid object with a flat base; three-quarter view from about 30–35° above; whole object in frame with ≥ 6 % margin; no ground, platform, props, cast shadow or text; even light; no key-colour fringe; the back can be inferred; no floating or paper-thin parts.
- **Icon or UI part:** reads at its drawn size, no misread meaning, matches its panel's family, holds against its background.
- **Background or key art:** epic scale, depth, a clear focal point, cinematic light, and no clash with signal colours.

## 4. Where to grade

- **The built play host.** Use `*.typing-game.local` (or the game's deployed play host) at the owner's quality setting: the default or Ultra, with no URL parameters.
  - Not a dev server, a bench page or a `?view=3d` URL.
  - Capture at 1920×1080 and 1280×720, then score the whole screen against the reference.
  - A known "dev only" or "default later" gap is a P0 bug, not a note. On 01/11 the owner found games that looked like toys at Ultra while their pieces had passed in dev.
- **Icons and UI parts at real size.** Render each icon in its real UI spot, or in a mock row with the real panel and button art, at 1280×720 and 1920×1080, 1× zoom. Put it next to its neighbouring icons and the old icon.
  - Size rows at 28–32 px.
  - A grade taken on a 256 px sheet overstates the result: icons that scored about 8 on sheets scored 6.2 and 6.3 in game.
- **Pieces not yet in game** (Tripo sources, concepts). Grade them at full size and at the size the game will use. The acceptance that counts is the grade in the play build after wiring.
- **3D models:** in the play build at the play camera, plus a three-angle turntable to catch shape faults.
- **VFX:** frame sheets per VFX_STANDARD at 720p and 1080p, play camera and close-up, light and dark grounds, then the play build.
- **Post-processed images:** judge the processed file the game will load, not the raw generation. Show the "generated | processed" pair so damage is visible.
- **Audio:** see [audio.md](audio.md).

## 5. Scores you cannot trust

- **Your own grade.** It runs high: Claude read its own Firefly metronome icon as 8, and two blind judges gave it 7 and 7. Art you made goes to two blind judges like any other.
- **A tool's self-grade.** Antigravity graded all 20 of its icons 10/10; at 24 px only 4 reached 8.
- **A maker's self-grade, a Codex ticket's included.** On 29/10, four of six tickets had a good generation that the tool step then damaged, and the self-grade still said 8. The older ART_ACCEPTANCE §4 practice of counting a Codex self-grade plus a Claude re-grade as two judges does not meet the 01/11 bar of two blind, independent judges.
- **ChatGPT's critique.** It is useful input. Weigh it against the judges; do not copy it.
- **A grade taken in dev or on a sheet**, for a piece the player sees in the build.

## 6. Disagreement and re-rounds

- When the judges straddle the bar (one 8.5, one 8.0), the piece fails. Fix what the lower judge named, then re-judge with two **fresh** judges. Do not shop for a third, higher score.
- When the judges differ by 2 or more, read both "what you see" notes. One of them is looking at the wrong thing, or the piece reads differently at different sizes. Fix the sheet or the brief, then re-judge.
- Record every round: file, label, both judges' scores per axis and the verdict. Report scores and level, never just "pass" or "fail". Keep the judges' notes beside the game's judging file.
