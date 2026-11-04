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
| **Claude subagents and workflows** | Making, measuring, judging and browser work in parallel | More than 3 at once (owner, 03/11) |

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

- **At most 3 Claude agents at once:** lean, with no two writing the same files.
- **Never send messages to a live workflow agent:** it resumed a duplicate on 31/10. Relay through files or later steps.
- **Before leaving work unattended,** check:
  - the permission mode;
  - that every path in prompts is the `/Volumes/...` path (writes through the old symlink path stalled the overnight agents for 7 hours on 04/11);
  - that nothing needs a prompt.

  Have a check-in look for logs that have been idle too long.
- **Browser:** close your tabs when done (the in-app browser holds about 9). Never sign in, type credentials or click consent dialogs.
