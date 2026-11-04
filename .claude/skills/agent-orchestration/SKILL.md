---
name: agent-orchestration
description: "Decide who does what among Claude, ChatGPT, Gemini, Firefly and the local Codex, and how they hand work over: the owner's division of labour and the double-review protocol (04/11/2026). Use before handing any research, analysis, plan, design, 2D image, code, logic or sound work to ChatGPT, Gemini, Codex, a subagent or a workflow; before writing a Codex ticket or lane; when picking Codex's model and effort; when deciding how many agents or lanes to run; and before leaving work running unattended. Applies to every game and tool in this repo."
---

# Agent orchestration: who does what, and the double review

**The owner's words (04/11/2026), the source of this skill:**

> "về codex ở local, hãy giao cho nó việc chính là cũng xử lý code, logic, âm thanh, với hình ảnh bạn cứ ưu tiên kêu chatgpt và gemini, lưu ý cách làm việc, hãy kêu chatgpt phân tích, tìm hiểu và đưa solution, và kêu nó tự review lại 2 lần liên tiếp, nếu cả 2 lần liên tiếp phần phân tích, solution của nó đều đúng, chính xác, pass thì mới đưa sang gemini để nhờ nó review lại, và cũng phải áp dụng tương tự cách review 2 lần liên tiếp này cho cả gemini, sau khi cả 2 đều pass thì bạn mới lấy về tham khảo, còn về codex ở local, hãy giao cho nó việc sau khi bạn có solution đầy đủ, về phân tích, tạo ảnh 2d thì cứ cho chatgpt và gemini phân tích trước, bạn là người chốt, còn codex chỉ là 1 đứa làm việc thay bạn xử lý code hoặc logic là được, khi nào 2 đứa chatgpt và gemini đạt giới hạn tạo ảnh thì kêu codex tạo ảnh, vì codex giới hạn quote ít, nên ưu tiên dùng 1 luồng agent, khi nào tôi kêu tạo thêm agent thì hãy tạo thêm, codex hiện tại bạn cứ kêu nó dùng model sol 6.1 medium, high, extra hoặc ultra tuỳ công việc, nếu liên quan tới logic, code thì cứ extra hoặc ultra"

This replaces older rules wherever they differ:
- "image making is always Codex's job" (28/10);
- "images only for Codex" (31/10);
- "same brief to both assistants, then a cross-fed second round" (04/11, night);
- "ultra only with the owner's OK per ticket" (27/10).

## Roles

| Who | Does | Never |
|---|---|---|
| **Claude** (the coordinator) | Decides: the owner calls Claude "người chốt". Writes briefs and tickets, runs the double review, verifies key claims at their sources, merges, reviews workers' output, commits, wires accepted work, reports to the owner | Accepts an assistant's answer unverified, or lets a worker make design decisions |
| **ChatGPT** (chatgpt.com, Chat mode, thinking High; never Work or agent mode) | First analysis, research and solution. First choice for 2D images | Has the final word |
| **Gemini** (gemini.google.com, 4 Argon, High) | Reviews ChatGPT's passed solution. 2D images next to ChatGPT, and when ChatGPT hits its image limit | Has the final word |
| **Codex** (the local CLI, `tools/codex-run`) | Code, logic and sound work (audio processing chains, Web Audio code, mixing scripts), only from a complete solution Claude hands it. Images **only** when ChatGPT and Gemini have both hit their image limits | Analysis, design or deciding. Browsing, dev servers (the sandbox refuses ports) |
| **Firefly** (Adobe models only) | Video VFX, sound effects, Adobe images and the image Upscaler, where `game-vfx-production` picks it | Partner models (Veo, Gemini, Flux and the like), the video upscaler (Topaz) |
| **Claude subagents and workflows** | Making, measuring, judging and browser work in parallel | More than the owner's current cap at once: 2 since 04/11 14:00 (3 from 03/11) |

## The double-review protocol (every analysis, plan, design and solution)

Use it before building any feature, effect, art, system or rework. Skip it only for purely mechanical work (a typo, a one-line fix, re-running a measurement, moving files), and say so when you skip.

1. **ChatGPT analyses.** One brief: the goal, the facts, the constraints, the owner's taste, and what is already decided. Ask it to research, analyse, and give a concrete solution with reasons and risks.
2. **ChatGPT reviews itself twice in a row.**
   - Ask it to re-check its own analysis and solution against the brief, the facts and the constraints.
   - It must answer **PASS** (nothing needs to change) or **FAIL** with the problems and a corrected full version.
   - It needs **two consecutive PASSes**. A FAIL resets the count; the next review starts on the corrected version.
3. **Gemini reviews.** Only after ChatGPT's two consecutive passes, give Gemini the same brief plus ChatGPT's final analysis and solution. Ask it to:
   - review it: correct, accurate, complete;
   - fix errors and fill gaps;
   - add better ideas;
   - return a full reviewed solution.
4. **Gemini reviews itself twice in a row,** by the same rule: PASS or FAIL with a corrected version, two consecutive PASSes, and a FAIL resets the count.
5. **Claude takes it as reference, not as an order.**
   - Verify the key claims at real sources.
   - Decide, and write one plan that says what each assistant contributed and where Claude disagrees.
6. **Record.** Save both conversations verbatim, with a check table of the claims, in the game's docs `source/` folder. Save the plan beside the design doc.
7. **Stop rule.** If an assistant gets no two consecutive passes within 4 review rounds, stop that run. Record where it keeps failing, then change the brief or the approach ("three tries, then discuss"). Never loop forever.
   - **Never forward a non-passing answer to Gemini.** On 04/11 an agent did, and the plan's ChatGPT side did not count.
   - **Size the workstream so it can pass.** Review one package, one layer or one ticket at a time, not a whole roadmap.
   - A roadmap from a pass that never got its two consecutive PASSes is only a draft. Each of its packages gets its own short double review right before it is built.
9. **ChatGPT and Gemini never block the work** (owner, 04/11/2026, about 14:00: "đừng để chatgpt hay gemini block bạn nữa, hãy triển khai các agent đang bị đợi đó theo cách khác, bạn tự điều tra hoặc xử lý chứ tránh chỉ vì gpt hay gemini làm block"). When an assistant is unreachable, has no free browser tab, is slow, or keeps failing:
   - **A Claude agent does the analysis itself:** it reads the code, does web research with WebSearch and WebFetch, verifies at the sources, and writes the solution.
   - **Independent Claude critics replace the review:** fresh agents that did not write the solution. It needs two consecutive PASSes with the same PASS meaning (correct and accurate); a FAIL leads to a fix and resets the count; at most 4 rounds.
   - **2D images:** when ChatGPT and Gemini cannot be reached, Codex `image_gen` paints from the decided design, run as a Codex image ticket. Firefly Image is the other choice when a tab is free.
   - Record which path was used. When an assistant becomes reachable again, its review may be added as an extra check, but nothing waits for it.
10. **PASS means "correct and accurate"** (owner: "đúng, chính xác"). It does not mean "nothing could be added". Defects fail; style and optional ideas do not (template in `references/double-review.md`).

Prompt templates and the record format: [references/double-review.md](references/double-review.md).

### Spend few tokens on the two assistants (owner, 04/11/2026)

The owner: "thảo luận xong 1 việc rồi hãy qua gemini nhờ nó đánh giá lại… tránh cứ hỏi 1 câu nhỏ bên chatgpt xong, đang thảo luận thì lại copy qua gemini". What costs Claude tokens is what Claude reads, and how many turns it takes, not what the assistants write. So:

1. **One whole workstream per chat.**
   - Send one complete brief: the goal, facts, constraints, decisions and taste, all at once.
   - Ask the assistant to put every clarifying question in one message at the start, and answer them in one message.
   - Never ping-pong small questions, and never carry half a discussion over to Gemini.
2. **Short verdicts.** A self-review that passes answers one line, `VERDICT: PASS`. Only a FAIL writes out the corrected full version. Claude reads the verdict line, not the whole answer.
3. **One handoff at the end.** After the two passes, ChatGPT writes one consolidated handoff in a single message: the final analysis, the solution, the sources and the open questions, at most about 1,500 words.
4. **Move it without reading it.**
   - Click the handoff message's own Copy button in ChatGPT, then click Gemini's input box and press Cmd+V.
   - The text goes through the browser clipboard, not through Claude's context.
   - Prefer this to downloading an `.md` and uploading it: every download needs the owner's OK under the browser rules, and the in-app browser has no upload tool.
   - If paste fails, have the page post the text to the local receiver (`game-art-pipeline` browser-ai-tools §4), then insert it into Gemini's box from that file with page JavaScript.
5. **Gemini works the same way.** In one chat: its review, two short-verdict self-reviews, then one final reviewed handoff.
6. **Claude reads once:** Gemini's final handoff, plus the verdict lines. Then Claude verifies the key claims and decides.
7. **Records cost no tokens.** Save the verbatim chats to files through the local receiver or page JavaScript that writes them out, never by reading them into Claude's context. Check that the files are complete by their size and turn count.
8. **One subagent per workstream at most.** Give the whole protocol to one agent with this skill, rather than several agents each opening chats.

**2D images** follow the same order:
1. the assistants analyse the design first, with the double review;
2. Claude decides the direction;
3. ChatGPT (then Gemini) paints it;
4. Codex paints only when both have hit their image limits.

The owner still reviews every sample, and acceptance is still two blind judges at 8.5 or more in the play build (`game-art-pipeline`).

## Codex: the worker for code, logic and sound

The owner (04/11): "với codex thì nó cũng như 1 agent của bạn, cứ sai nó thực hiện code, test, hoặc tạo ảnh nếu 2 đứa kia chạm giới hạn". Treat Codex as one of Claude's own agents for code, tests and logic. Using it saves Claude's tokens, since its quota is separate.

- **Only from a complete solution.** A ticket gives Codex the decided solution, the exact files and functions, the allowed write paths, the forbidden actions, forced checks with numbers, and a report file. Design questions never go to Codex.
- **Model and effort** (owner, 04/11): model `gpt-6.1-sol`; the effort follows the work.

  | Work | Effort |
  |---|---|
  | Chores: docs status, inventories, moving files, simple scripted edits | `medium` |
  | Sound processing chains, small specified edits, images when both assistants are limited | `high` |
  | Code and logic: features, fixes, tests, refactors with a clear spec | `xhigh` (the owner's "extra") |
  | Large multi-part code or hard logic. It splits into sub-agents and spends quota fastest | `ultra` |

  Code and logic always get `xhigh` or `ultra`. The lane line names the effort (column 4) and the model (column 6).
- **One lane.** Codex's quota is small. Add lanes only when the owner asks. Keep the lane stocked with ready tickets, but only ready ones: a ticket waits until its solution is complete.
  - **Never let Codex sit idle behind a review queue** (owner, 04/11/2026 18:40: "bạn đã giao cả việc cho codex hay chưa vậy, sao tôi không thấy nó làm gì"). Run the critic rounds of Codex's next ticket before long browser jobs, not after them. If Codex is idle and a ticket has one PASS after its FAIL rounds were all fixed, Claude may hand it over. In that case, record the call in the ticket's review line and keep the second critic running as an extra check; its defects become a follow-up ticket.
- **Its own tree.** When Claude agents edit the same game, Codex works in its own worktree on a branch (`games/.wt-<game>-codex`). Claude reviews and merges.
- **Claude owns quality.** Codex never commits. Claude:
  - re-runs the checks;
  - reads the diff;
  - checks it in the browser when it is visible;
  - commits only after review, never on Codex's self-report.
- **Limits:** `tools/codex-run/queue.sh` waits out every limit. Never kill a waiting lane unless the owner says to stop Codex. A routing change (like 04/11's) stops tickets that no longer fit, keeps their files, and moves the work to the right worker.
- **Paths:** since 03/11 the repo lives at `/Volumes/SS990TPRO/htdocs/typing-game`. Tickets name that path.

Runner usage: `tools/codex-run/README.md`.

## Claude agents and unattended work

- **Claude agents within the owner's current cap:** 2 at once since 04/11/2026 14:00 (it was 3 from 03/11). Count a workflow by its live agents. Keep it lean, and never let two agents write the same files.
  - Extra agents he grants for a time box stop at the time he set; never extend it.
  - Their leftovers go into an ordered queue in `docs/HANDOFF_CURRENT.md`; the next item starts only when a slot frees.
- **Never send messages to a live workflow agent:** it resumed a duplicate on 31/10. Relay through files or later steps.
- **Before leaving work unattended,** check:
  - the permission mode;
  - that every path in prompts is the `/Volumes/...` path (writes through the old symlink path stalled the overnight agents for 7 hours on 04/11);
  - that nothing needs a prompt.

  Have a check-in look for logs that have been idle too long.
- **Browser:** close your tabs when done (the in-app browser holds about 9). Never sign in, type credentials or click consent dialogs.
- **Check before reporting "signed out".**
  - On 04/11 an agent reported that ChatGPT, Gemini and Firefly were signed out and stopped its Firefly step. The owner said they were not, and a fresh tab showed all three still signed in.
  - Before concluding a sign-out, open a fresh tab, load the site's home page, and look for the account avatar against a "Sign in" or "Log in" button.
  - Keep one neutral tab open when cleaning up: closing the last tab closes the browser pane.
- **Agents use the in-app browser only.** Claude in Chrome is the owner's own Chrome, used only when he asks for it. On 04/11 two agents tried it when the in-app browser was full.
- **Budget browser tabs, not just agents.** The in-app browser holds about 9 tabs. On 04/11 nine agents ran at once and one image agent never got a tab (four tries in 8 minutes).
  - Before adding agents, count the tabs (`tabs_context`).
  - Give each browser agent ONE tab: ChatGPT, then the same tab navigated to Gemini after Copy.
  - Give extra agents work that needs no browser (code reading, measuring, audits, ticket drafts), or queue their browser part after another agent frees its tab.
- **Short time boxes.** An agent spends its first minutes reading.
  - When the owner asks for extra agents with a stop time less than about 20 minutes away, say so and offer a later stop time before starting them.
  - Every time-boxed agent saves its records, a draft and a `PROGRESS.md` a few minutes before the stop, so nothing is lost.
- **Files for the owner live where he can see them.** Every capture goes to `typing-game-review/captures/<game>/<topic>/` beside the source (owner, 04/11/2026). Everything sent to him also goes to `owner-review/<date>/<game>/<topic>/`. Each topic folder has an `ABOUT.md`; rebuild the index with `node scripts/review-index.mjs` (AGENTS.md "Test captures"). Brief every agent and Codex ticket with these paths.
- **Demos while the owner is remote** go out as a video (an MP4 under 30 MB, so it reaches his phone) through SendUserFile, and the file is kept in `owner-review/`.
