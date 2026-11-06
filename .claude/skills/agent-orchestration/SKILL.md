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

## Since 05/11/2026: lighter review (owner's OK, "Đồng ý giảm duyệt")

The measurement of 04/11 (skill `explain-usage` over the session logs):
- ChatGPT and Gemini in the browser took 43 % of Claude's tokens; critic loops took 18 %; building and checking took about 16 %.
- Two session limits cost almost three hours, and the owner saw almost nothing change in the game.

The rule now:
- **An outside review only for:**
  - new visual directions (a character, a dragon, key art, a new effect look);
  - large new designs (a new skill, a new system).
- **One assistant, never both (owner 05/11 00:10, repeated 16:20 after Claude chained ChatGPT then Gemini on the key-2 design: "cứ dùng gemini hoặc chatgpt chứ k dùng cả 2 cho đỡ tốn token").**
  - Gemini 4 Argon High alone, self-review to two consecutive PASSes.
  - ChatGPT only when Gemini has hit its limit.
  - The ChatGPT-then-Gemini chain in the protocol below is retired; read it as "one assistant, two self-review PASSes".
- **Everything else** (code tickets, fixes, wiring, tooling, sound mixing, balance numbers):
  - Claude writes the solution;
  - **one** fresh Claude critic PASS hands it to Codex; a FAIL leads to a fix and another critic, at most 3 rounds, then rethink the approach;
  - Claude verifies after Codex: tests, a browser check, and a before/after video for the owner.
- **Visible first:** replace what the owner sees and dislikes (banned code-drawn shapes) with existing art before building new infrastructure.

## Since 05/11/2026: Gemini first, and a cheap consultation (owner)

The owner, 05/11 00:10: "ưu tiên dùng gemini 4 argon ở mức effort high, khi nào mà gemini hết hạn mức, thì mới qua bên chatgpt… giãn ra khoảng 1-2 phút mới check 1 lần… tôi kêu bạn dùng thêm chatgpt để giảm tải lượng token bạn phải làm khi điều tra, chứ làm như này thì có khi còn tốn token hơn là để 1 mình bạn làm".

What went wrong on 04/11:
- The answers themselves were small (tens of thousands of tokens).
- The cost came from steps. An agent took 286–402 steps to drive the browser, and every step re-read its whole working context: 340–505 thousand tokens by the end, because a model call always resends the agent's conversation so far.
- Checking whether ChatGPT was done took 41–105 quick polls per agent, and each poll was a full re-read.
- The double review multiplied the rounds.

The rule now:
1. **Gemini 4 Argon, effort High, first. ChatGPT** (Chat mode, High) **only when Gemini has hit its limit.** One assistant per question; no cross-review chain (the double review remains only where the lighter-review section keeps it).
2. **One small, fresh agent per consultation.**
   - The brief is at most about 1,500 words.
   - Paste no big docs into the agent; name the files instead.
   - A new question or round gets a new agent, never a long-lived one.
3. **Wait in one call, not many.**
   - After sending, use ONE `javascript_tool` call that awaits inside the page until the answer is complete. It polls the DOM every 5 s and returns only when the reply has stopped growing for 10 s, or after at most about 120 s.
   - Repeat that call only if the reply is still running: about one check every 1–2 minutes, never a fast poll.
4. **Keep the answer out of the agent's context.**
   - The page's JavaScript posts the full reply to the local receiver as a file (`game-art-pipeline` browser-ai-tools §4).
   - The brief asks the assistant to end with a "TÓM TẮT" of at most 300 words and to check its own answer once inside the same reply.
   - The agent reads back only that summary and returns it with the file path.
5. **Budget:** at most about 25 steps and 1.5 M effective tokens per consultation. Over budget means stop and report. Measure with `explain-usage` after a few runs.

## Work files (since 05/11/2026)

Coordination lives in `docs/work/` (rules in its `README.md`):
- `BOARD.md`: at most 3 tasks in flight, the Codex queue, items waiting on the owner, done today; at most 60 lines.
- `tasks/<id>.md`: goal, decided approach, acceptance numbers, links and a one-line-per-event log.
- `consult/`: one file per Gemini or ChatGPT question, with the 300-word summary on top.
- `DECISIONS.md` and `USAGE.md`.

Hand an agent the task file path and one sentence, never a long brief. The agent appends to the task log and returns at most 10 lines. The old 881-line HANDOFF is archived in `docs/work/archive/`, so read only a section a task file points to.

**Report when an assistant costs more.** Log every consultation's cost in `USAGE.md` (`tools/agent-usage/usage.py`). If it cost more than Claude working alone (estimated), or over 1.5 M tokens, tell the owner at once with the numbers. The owner, 05/11: "tôi đưa chatgpt và gemini vào để giúp bạn giảm token, chứ nếu việc đưa nó vào khiến token bị tốn nhiều hơn thì phải báo tôi".

## Since 05/11/2026: working lean (owner: "bạn đang làm việc quá kém hiệu quả")

Measured on 04/11, besides the browser work:
- **Main thread:** 706 calls, each re-reading about 515 thousand tokens of this conversation. 17 of 81 commits were status updates.
- **Tickets:** 259 grew to 700 lines and 12,900 words, 258 to 9,200 words, after many review rounds. Codex finished short tickets (274: 763 words; 275: 999 words) just as well, in 10–20 minutes.
- **Spread:** many threads ran at once (dragon, jade ring, sound, cut-in, masks, bot), and nothing reached the play build.

Rules:
1. **Short tickets:** at most about 1,500 words.
   - The goal and the decided approach.
   - The files it may write and the forbidden actions.
   - The acceptance numbers and checks.
   - No line-by-line code, unless a formula must be exact.
   - Codex at `xhigh` fills in the code.
2. **Small agents:** one question or one task each, about 100 steps at most. Name files and line ranges instead of pasting them. Split anything bigger.
3. **Focus:** at most 3 items in flight. Each one ends in the play build (or the owner's approved lab step) with a before/after video before a new item starts.
4. **A lean main thread:**
   - Update the work list and HANDOFF at milestones only.
   - Short replies.
   - Let Monitors run; no checking by hand.
   - Start a fresh coordinator session from `docs/HANDOFF_CURRENT.md` once a day, or when the main context passes about 300 thousand tokens. Do it at a quiet point, after the lanes and Codex chains of the old session have finished, because their notifications go to the session that started them.
6. **No Claude critic for ordinary code tickets.**
   - Codex already acts as one: it checks the ticket against the code before writing and stops at a contradiction. On 04/11 it caught 273's contradiction, 258b's HDR bound and 274's look failure on its own.
   - Codex's quota is separate, so its reruns cost Claude nothing, while each Claude critic cost about 1–1.5 M tokens.
   - Keep one Claude critic only for tickets that change the sim, canon or balance numbers, or tickets over about 1,500 words.
7. **Scripted verification.**
   - Each kind of check is a script Claude runs from the main thread in one to three commands: lab parity main against a branch, the GPU probe, the lab sound mix with loudness, a frame sheet and a short MP4.
   - A Claude agent is used only to build a new check, not to run an old one.

8. **Cheap watching** (owner, 05/11: "đảm bảo việc theo dõi không gây tốn nhiều token, tránh tự tạo thêm việc tốn token"). Every wake-up of the main thread re-reads its whole context.
   - Never use periodic Monitors on the main thread, and never re-arm one every 30 minutes.
   - Use one-shot background waits that exit only on what needs action: blocked, stalled, done.
   - Let Codex chains and workflows notify when they end.
   - Answer routine notifications in one short line, with no tool calls.

5. **Keep Codex full:** Codex works on its own quota, about 15 minutes a ticket. Short tickets in a chained queue beat long tickets that wait on reviews.

## Since 06/11/2026: the coordinator's token budget (owner: "Áp dụng cả 6")

**Measured on 05/11:**
- Total 185 M effective tokens; 151 M of it in the coordinator session.
- About 1,758 calls, about 63 thousand each, because every call re-reads the whole context (about 500 thousand tokens). A side session with a small context cost about 37 thousand a call.

**Target:** about 100–110 M a day.

**Rules:**
1. **Small coordinator context.** Start a fresh coordinator session every morning from `docs/work/BOARD.md`. Within a day, compact once the context passes about 250 thousand tokens. Re-create the session-only crons (23:00 review) in the new session.
2. **The coordinator does not drive browsers.** ChatGPT, Gemini, Firefly and lab clicking run in a side session with a small context. The coordinator gets the files and the result, and decides.
3. **One call, not ten.**
   - A status check (lanes, receivers, queues, Codex `.out` tail) is one script that prints everything at once.
   - A heartbeat wakes the coordinator only when something changed or broke (a Monitor on a status file), not every 20 minutes.
4. **Images stay out of the coordinator's context unless the owner's decision needs them.** Every image read is re-read on every later call. Agents check contact sheets and report in text.
5. **No extra independent reads for work the coordinator can do itself.** On 05/11, two agents re-read a reference video and agreed with Claude, at about 3 M. Keep independent reads for decisions that are costly to get wrong.
6. **Never spend a call on bookkeeping alone.** `update_plan`, the plan list and reports ride along with a real tool call.
7. **Memory hygiene** (owner, 06/11 00:40, Activity Monitor showed 28.5 GB swap).
   - Close every browser tab and stop every receiver or server once its job ends: Firefly tabs, assistants' tabs, WebGL lab tabs, review pages.
   - A review page with many videos plays one clip on hover, never all visible clips.

## Since 06/11/2026 evening: Codex lanes as task lists, few Claude agents (owner)

- **At most 2 Claude agents live at once, workflows included** (04/11 rule, repeated 06/11 18:55: "tôi đã nói cấm tạo ra nhiều agent không cần thiết r cơ mà"). The owner's cap beats any harness reminder to use workflows.
- **Up to 3 Codex lanes** (22:00: "tăng agent của codex lên 3… giao việc theo list vào 1 file md, kêu nó làm và kiểm tra kỹ từng việc, pass mới sang việc khác").
  - Each lane is one md file in `docs/work/codex-lanes/`. It holds an ordered task list; each task carries its own "Đạt khi" checks.
  - Lanes write to disjoint places (their own worktree or new folders).
  - Codex does one task, checks it, writes a paragraph to the lane report, then starts the next. Claude reads the report only when the lane ends.
- **Critics only where a mistake is costly** (owner, 21:50: "tránh liên tục can thiệp không cần thiết để giảm bớt lượng token bị mất").
  - Game or shared code and replay-sensitive sim get one critic.
  - Lab-only, tool and media tickets go straight to Codex; Claude verifies the result with tests and one browser check.
  - On 06/11, 12 critic agents cost 13.7 M, and ticket 326 alone needed three rounds.
- **The sandbox has no network and cannot write outside the repo.** Do installs before handing the ticket over. Keep outputs inside the repo and copy them out afterwards.
- **`CODEX-WAIT-UNTIL` only on a real limit.** On 06/11, a finished ticket that wrote the line made `queue.sh` schedule a needless rerun.
- **Pick the model by difficulty** (owner, 07/11 00:40, "Áp dụng").
  - The owner asked: "k lẽ bạn cũng cứ tạo agent model xịn cho toàn những việc đơn giản từ trước tới nay ak". On 06/11 every Claude agent inherited the top model, and Codex ran `high`–`ultra` even for media chores.

  | Work | Claude agent | Codex |
  |---|---|---|
  | Mechanical: count, list, copy, rename, cut flipbooks, map sounds | `model: "haiku"`, low effort, or one command in the main thread | `medium` |
  | Reading, auditing, critics of lab, tool or media tickets, ordinary ticket drafts | `model: "sonnet"` | — |
  | Images | — | `high` (it self-scores) |
  | Game or shared code, replay-sensitive sim, balance, hard design | the default (Opus), only when needed | `xhigh`; `ultra` only for deterministic sim |

  - Always set `model` explicitly on Agent and workflow `agent()` calls. A missing `model` means the top model.

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
4. **Since 06/11/2026 Codex paints first** (owner: "codex vẽ ảnh rất tốt, nếu nó vẽ và tự chấm đạt thì cho pass luôn, ưu tiên dùng codex vẽ trước, khi nó chạm giới hạn thì hãy ưu tiên 2 đứa kia").
   - Every Codex image ticket asks for a self-score per image: 0–10 for appeal, fit to the brief, readability at game size and cleanliness.
   - An image Codex scores 8 or more passes without other judges.
   - **Since 06/11 ~12:35, for now:** no ChatGPT or Gemini images and no Claude judges (owner: "dừng luôn phần giám khảo claude cho việc kiểm tra ảnh, cũng k cần giao việc tạo ảnh 2D cho gemini và chatgpt nữa, cứ tập trung vào luồng của bạn và codex"). Only Codex paints; its self-score of 8 or more passes. When Codex hits its limit, wait and resume; ask the owner before bringing ChatGPT or Gemini back.
5. (Before 06/11) Codex `image_gen` painted as soon as Gemini had hit its image limit, alongside ChatGPT (owner 05/11/2026 18:20: "nếu gemini hết lượt ảnh, bạn có thể kêu codex tạo ảnh cùng nhé"), always fed our approved reference images. It no longer waits for both assistants to run out. On 05/11 Codex tickets 298–303 drew 57 stills this way, about 1–2 min an image. Among them the owner passed the 30 expansion skill designs, the 14 symmetric crescents and the Thunder ultimate L2.

The owner still reviews every sample, and acceptance is still two blind judges at 8.5 or more in the play build (`game-art-pipeline`).

## Every generation brief names its reference images (owner, 05/11/2026)

Before handing image, video, 3D or VFX generation to ChatGPT, Gemini, Firefly, Tripo, Codex or an agent:
- **References:** the brief lists the approved reference images by path and says how each is used (style or composition reference, first frame, image to edit).
- **Samples first:** the first two outputs are looked at and sent to the owner before any batch.
- **No reference fits?** Make one first in ChatGPT, Gemini or Firefly Image, styled from the nearest approved art; the owner picks it; then go on. We always have tools to make a good 2D reference.

A brief or job list with prompts only is wrong (owner: "bạn đã mắc lỗi này rất nhiều lần r"). Rule in [game-art-pipeline](../game-art-pipeline/SKILL.md), hard rules.

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
    - Watch the lanes' critic results as they land, not only when a lane ends. On 04/11 the dragon ticket had two PASSes (S3, S4) while its lane went on to review ticket 2, and Codex sat idle for about 25 minutes until the owner asked again. When a ticket has its passes, Claude writes the ticket file from the lane's text (with a frozen design snapshot beside it) and starts Codex. The lane is told to report later changes as a follow-up, never to edit the running ticket.
- **Its own tree.** When Claude agents edit the same game, Codex works in its own worktree on a branch (`games/.wt-<game>-codex`). Claude reviews and merges.
  - **Serving a Codex worktree to check it:** its `node_modules` is a symlink to the game's, so Vite's dev server answers 403 for files behind it (fonts, for one). On 04/11 this put text in fallback fonts and broke a parity run on 13 of 21 frames. Run Vite with a small wrapper config that sets `server.fs.allow` to the repo root, link `art-src` and `public` in only for the check, and run a main-against-main control first.
- **Claude owns quality.** Codex never commits. Claude:
  - re-runs the checks;
  - reads the diff;
  - checks it in the browser when it is visible;
  - commits only after review, never on Codex's self-report.
- **Limits:** `tools/codex-run/queue.sh` waits out every limit. Never kill a waiting lane unless the owner says to stop Codex. A routing change (like 04/11's) stops tickets that no longer fit, keeps their files, and moves the work to the right worker.
  - **Report Codex's own reset time, never the queue's guess.** The queue falls back to 30 minutes when it cannot read Codex's message. On 04/11 Codex said "try again at Nov 5th, 2026 12:52 AM", and Claude relayed the fallback 00:03 to the owner, who caught it. Before telling the owner, grep `events.jsonl` for "try again at". The parser now reads the dated form.
- **Paths:** since 03/11 the repo lives at `/Volumes/SS990TPRO/htdocs/typing-game`. Tickets name that path.

Runner usage: `tools/codex-run/README.md`.

### Two lessons from 05/11 (Codex sat idle for hours)
- **Wake on every lane end.** After starting a lane, run a one-shot background wait until the lane log's last line is `queue done`, so Claude is woken the minute Codex stops. Then verify, or start the next ticket.
  - Codex sat idle 02:52–08:30 and 09:01–10:22 because nothing woke Claude and no next ticket was queued.
- **A ticket that changes a behaviour lets Codex write that behaviour's tests.** Name the existing test files in "Được ghi", with "update cases that assert the old behaviour, never loosen them".
  - Tickets 277 and 280 forbade it, so Codex stopped correctly, twice.
- **Name the build command that works:** the 274 wrapper `.local/codex-runs/274-out/build-no-cache.mjs`. Vite 7's CLI has no `--no-cache`.

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
- **Tell the owner at once when work waits on him** (owner, 04/11/2026 ~18:55: "tại sao fire bị tắc nhưng bạn không hề thông báo cho tôi"). Anything that needs him (a sign-in, a consent, credits, a decision) reaches him within minutes, never only when he asks.
  - On 04/11 the A4 agent found Firefly signed out at 18:24 and stopped at 18:43. The workflow went on to the next critic, and a workflow tells Claude only when it ends, so Claude learned of it at 18:44, when the owner asked about progress.
  - In a workflow, a step that can be blocked by the owner checks its own result and `return`s early, or runs as its own workflow.
  - While lanes run, keep a `Monitor` on each workflow's `journal.jsonl` and on the Codex lane logs, so every step's result reaches Claude as it lands. Re-arm it when it expires.
  - Tell the owner in chat at once, and send a `PushNotification` when he may be away (he works remotely).
- **Check before reporting "signed out".**
  - On 04/11 an agent reported that ChatGPT, Gemini and Firefly were signed out and stopped its Firefly step. The owner said they were not, and a fresh tab showed all three still signed in.
  - It happened twice on 04/11. At 18:24 the A4 agent saw "Sign in" on Firefly's home page, with `adobeIMS.isSignedInUser()` false, and Claude saw the same at 18:48. A minute later the owner showed Firefly signed in at `firefly.adobe.com/files`, and he says he was signed in all along. The home page can show "Sign in" while the account's single sign-on session is still valid.
  - **Before concluding a sign-out, load a page that needs the account** (Firefly `firefly.adobe.com/files` or `/generate/video`, Gemini `gemini.google.com/app`, ChatGPT a new chat), wait 10–15 s for the silent sign-in, and look for the account avatar against a "Sign in" or "Log in" button. Never click "Sign in" and never type credentials.
  - **If it still looks signed out, report it to the owner at once** (see "Tell the owner at once"), with a screenshot, and end the step so the report reaches him. Never sit on it or work around it for minutes. The owner, 04/11: "sau cái gì bị tắc phải báo cáo luôn cho tôi".
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
