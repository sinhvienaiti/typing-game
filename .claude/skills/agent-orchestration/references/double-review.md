# Double review: prompt templates and the record

Use these with the protocol in [SKILL.md](../SKILL.md). Write prompts in English or Vietnamese; ask for answers in the language of the doc they feed.

## 1. ChatGPT: analysis and solution

```text
Role: you are the analyst for a game project. Research, analyse and propose a concrete solution.
Goal: <one paragraph>
Facts and current state: <measured numbers, what exists, file or tool names>
Constraints: <owner rules, budgets, tools allowed and banned, licences>
Already decided by the owner (do not reopen): <list>
Taste: <for visual work: anime/donghua and myth, radiant, luxurious, captivating; never realism as the goal; never plain>
Deliver: 1) analysis of the problem and its causes, 2) the solution as ordered steps with the reason for each, 3) risks and how to check each, 4) what you are not sure about. Cite a source for every factual claim.
```

Add to the first brief: `If you need clarifications, ask all of them in one message before you start.`

## 2. Self-review (ChatGPT, later Gemini): ask twice in a row, or more after a FAIL

```text
Review your latest full answer above against the brief, the facts and the constraints. Check: wrong facts or sources, steps that would not work, missing steps, contradictions with the constraints or the owner's decisions, vague parts that a worker could not execute.
If nothing at all needs to change, answer with exactly one line: VERDICT: PASS
Otherwise answer: VERDICT: FAIL, then list each problem, then give the corrected FULL analysis and solution (not a diff).
```

## 2b. Handoff (after the two passes, once per assistant)

```text
Write the final handoff in one message, at most about 1,500 words: 1) the final analysis, 2) the solution as ordered steps, 3) sources, 4) open questions and risks. No preamble.
```

Move ChatGPT's handoff to Gemini with the message's Copy button and Cmd+V into Gemini's box (SKILL.md "Spend few tokens"). Claude reads only Gemini's final handoff and the verdict lines.

Count the verdicts:
- PASS, then PASS: the run is done.
- FAIL, then PASS, then PASS: done; the version reviewed is the corrected one.
- No two consecutive passes within 4 reviews: stop (SKILL.md step 7).

A PASS that still changes something counts as a FAIL.

## 3. Gemini: review of ChatGPT's passed solution

```text
Role: you are an independent reviewer for a game project.
Brief: <the same brief as step 1>
Another assistant's final analysis and solution (it passed two self-reviews): <pasted from ChatGPT's handoff with Cmd+V>
Review it: is it correct, accurate and complete for the brief? Correct errors, fill gaps, replace weak parts with better ideas, and cite a source for every factual claim.
Deliver: 1) what you agree with, 2) each error or gap with the fix, 3) your full reviewed solution, 4) what you are not sure about.
```

Then run the self-review of §2 on Gemini, with the same counting.

## 4. What Claude does with it

- **Verify** each key claim at a real source (official docs, Adobe helpx, three.js docs, GDC or the maker's own article, the original text for myths). Mark each claim verified, wrong or unverified.
- **Decide.** Take what holds, reject what does not, and say why.
- **Brief workers from the decision**, never from the raw answers. Codex tickets carry the decided solution.

## 5. The record

`docs/games/<game>/…/source/<topic>-chatgpt-<date>.md` and `<topic>-gemini-<date>.md`, each with:
1. the brief, verbatim;
2. every turn, verbatim: the answer, each review prompt and each verdict;
3. the review count, for example "FAIL, PASS, PASS";
4. a check table:

   | Claim | Source | Status | Note |
   |---|---|---|---|

The plan or design doc links both files and states what each assistant contributed and where Claude disagrees.

## 6. Practical notes

- **ChatGPT:** Chat mode with thinking High only. Work mode spends the scarce quota.
- **Gemini:** its first long answer sometimes breaks off. Ask it to continue or to resend in parts, and save the complete version.
- **Long answers:** read them with `get_page_text` or `javascript_tool`. Some pages block form posts to a local receiver.
- **Never** sign in, type credentials or click consent dialogs. If a site is signed out or asks for consent, stop and tell the owner.
- **Never paste third-party reference images** (boards made from commercial games) into either assistant. The repo's own art is fine.
