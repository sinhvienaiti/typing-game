# Antigravity lane: image tickets while Codex is out of quota

Owner, 31/10/2026 about 23:45: "tạm thời hãy kêu antigravity tạo ảnh cho bạn, codex khả năng chắc phải 2 ngày nữa mới có hạn mức". Codex lanes s29/s30 are paused; the coordinator (Claude) grades every delivery at real size and wires it. Antigravity has no command line the coordinator can call, so the owner pastes one prompt per ticket into Antigravity's agent with this repo open.

## Rules for the Antigravity agent (read before every ticket)

1. Open the ticket file named in the prompt and do exactly what it says. Read every file it names first: earlier tickets and reports, style blocks, reference images, `docs/games/ART_ACCEPTANCE.md`, and for tickets 245–250 the section "Luật chung của đợt 242–246" in `docs/codex-queue/242-ts-icons-real-size.md`.
2. The tickets were written for Codex. Read them with these changes:
   - Where a ticket says `image_gen` or "công cụ ảnh", use **your own built-in image generation tool**. Use no other image service. In the report, give the tool's and model's name.
   - **Transparent background:** if your tool cannot output real alpha, paint on a flat key colour: magenta `#FF00FF`, or green `#00FF00` when the subject contains magenta or pink. Remove the key with ImageMagick as the ticket's post-processing rules say (`docs/games/ART_ACCEPTANCE.md` §5). No key colour may remain at the edges (Kiểm 2–3).
   - `CODEX-WAIT-UNTIL`: if your image tool refuses, rate-limits or asks you to wait, stop, keep every file, write the report for what is done, and end the report with the line `ANTIGRAVITY-WAIT-UNTIL: HH:MM` (or `unknown`). The owner will run the ticket again later and you continue from what exists.
3. Write only the paths the ticket's "Chỉ được ghi" section allows, plus its report `docs/codex-queue/<n>-report.md` (in Vietnamese) and folder `docs/codex-queue/<n>/`. Never overwrite or delete an existing file. Keep every try (`.tryN` / `.rN-tryN`) with its exact prompt next to it.
4. Forbidden:
   - any git command that writes (commit, add, checkout, stash, reset, push);
   - copying anything into `public/`;
   - editing code, manifests, `selection.json` or docs other than your report;
   - starting dev servers;
   - touching Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`) or any `games/.wt-*` folder;
   - downloading images from the web.
5. Grade at real size, as the tickets require: the 720p and 1080p cells at 1×, on the real UI crop of the game, before any big sheet.
6. The ticket's limit applies: at most **3 tries per image**.
7. Finish with the report. It lists:
   - every file you made;
   - the prompt changes per try;
   - the numbers each check asks for;
   - your self-grade at 720p 1×;
   - anything you did differently from the ticket, and why.

## Order (most visible first)

| # | Ticket | What |
|---|---|---|
| 1 | `docs/codex-queue/250-quick-panel-icons-round2.md` | Quick-panel icons in all three games: three-quarter keycap, keyboard volume, empty Settings rows, Wordwoven corner speaker, Last Line reduced-motion, quality, read-aloud |
| 2 | `docs/codex-queue/249-ts-guns-menu-parts.md` | Last Line gun art at 44–96 px, horizontal magazine rounds, four menu icons |
| 3 | ~~`docs/codex-queue/247-ts-icons-new-concepts.md`~~ | **Taken by Claude with Adobe Firefly Image 5 on 01/11 (00:30). Do not run it.** |
| 4 | `docs/codex-queue/246-ts-hud-chrome-parts.md` | Last Line: hazard strip, hull bar, sealed bay plate |
| 5 | `docs/codex-queue/248-ts-victory-bg.md` | Last Line: a victory background that reads as victory |

Ticket 245 (list rows, Close buttons, foe silhouettes) was already delivered by Codex; do not redo it.

## Prompt to paste (one ticket per Antigravity conversation)

```text
You are making game UI art for this repo. First read docs/codex-queue/ANTIGRAVITY_LANE.md (rules for you) and follow it exactly. Then do the ticket docs/codex-queue/250-quick-panel-icons-round2.md completely: read every file it names, generate the images with your built-in image tool, post-process and check them as the ticket says, and write the Vietnamese report docs/codex-queue/250-report.md. Do not run any git command that writes, do not copy anything into public/, and never overwrite or delete existing files. Work until every image in the ticket is delivered or your image tool stops you.
```

For the next tickets, change both `250-...` file names to the ticket in the order table above (for example `249-ts-guns-menu-parts.md` and `249-report.md`).
