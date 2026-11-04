# Song Long toàn sân: giám khảo Claude độc lập (04/11/2026)

Bản ghi cho [`../DRAGON_SKILL.md`](../DRAGON_SKILL.md) §9.1 và §9.10. Đường duyệt theo bước 9 của `agent-orchestration` (anh, khoảng 14:00: ChatGPT hay Gemini không được làm chặn việc): Claude tự phân tích, rồi các giám khảo Claude độc lập duyệt, mỗi lần một agent mới (`general-purpose`), chưa viết bản này, chỉ đọc, không đọc thư mục của giám khảo khác. PASS nghĩa là "đúng, chính xác"; FAIL thì Claude sửa rồi giao cho giám khảo mới; tối đa 4 lần mỗi lượt; hai PASS liên tiếp phải trên cùng một bản (Claude giữ bản đó đứng yên giữa hai lần và so md5).

Bản được duyệt là bản nháp `section9.md` (ngoài Git) mà sau đó thành §9 của tài liệu thiết kế. Phiếu 1 giao cho Codex (271) là bản sau S4 cộng các quyết định của anh lúc 19:40; phiếu 2 (272) là đúng bản U3 và U4 đã duyệt (`docs/codex-queue/272/section9-design.md`, md5 `32e3ffa4…`).

## Số lượt và kết quả

| Lượt | Phạm vi | Lần duyệt | Kết thúc |
|---|---|---|---|
| 1 | Cả §9 (thiết kế và phiếu) | critic 1: FAIL · critic 2: FAIL · critic 3: FAIL | Dừng: không thể có hai PASS liên tiếp trong 4 lần. Đổi cách: chia gói |
| 2a | Thiết kế §9.0–9.11 | A1: FAIL · A2: PASS · A3: PASS | **Qua** (A2, A3 trên cùng bản) |
| 2b | Phiếu §9.12 (một gói) | B1: FAIL · B2: FAIL · B3: FAIL | Dừng. Đổi cách: tách hai phiếu (sim; bot) |
| 3 | Phiếu 1 (header, A–E) | S1: FAIL · S2: FAIL · S3: PASS · S4: PASS | **Qua** (S3, S4 trên cùng bản) |
| 4a | Phiếu 2 (F) và việc đưa quyết định của anh vào toàn §9 | T1: FAIL · T2: FAIL · T3: FAIL | Dừng (T3 không thấy lỗi ở F, chỉ ở chỗ 2,0 W làm hỏng test giữ lại của phiếu 1) |
| 4b | Như 4a, sau khi sửa | U1: FAIL · U2: FAIL · U3: PASS · U4: PASS | **Qua** (U3, U4 trên cùng bản; bản đó giao Codex là 272) |

Mọi lỗi của các lần FAIL đã sửa trước lần duyệt kế. Các góp ý không chặn của các lần PASS và FAIL được gom ở cuối file thành việc làm sau.

## Đề bài giao giám khảo

Mỗi đề bài có cùng khung: đường dẫn bản nháp; phạm vi; bối cảnh (game, cờ, quyết định của anh nguyên văn, ràng buộc); danh sách file mã phải đọc; năm câu kiểm; định nghĩa lỗi ("A defect is: a wrong fact, … Wording, style and optional improvements are NOT defects."); và mẫu trả lời `VERDICT: PASS` hoặc `VERDICT: FAIL` kèm danh sách lỗi có chỗ, bằng chứng, cách sửa. Hai đề bài dưới đây là nguyên văn của lượt cuối mỗi loại; các lượt khác chỉ khác phạm vi, thư mục nháp của giám khảo và danh sách file.

### Đề bài A2, A3 (thiết kế)

```text
You are an independent critic. Review the DESIGN part of a game-skill document and return a verdict. You did not write it. Read-only: do not edit, create or delete any file outside your own scratch folder named below, do not use a browser, do not message other agents, do not run git commands that change anything. Use only the path /Volumes/SS990TPRO/htdocs/typing-game (never /Users/toandx/htdocs/typing-game).

THE DOCUMENT: …/scratchpad/dragon-fieldwide/section9.md (Vietnamese prose, English ids). It will become section 9 of docs/games/tu-tien/skills/DRAGON_SKILL.md.
YOUR SCOPE: §9.0 to §9.11 only (the decided design, its numbers, the prototype table, the targets and bot plan, the VFX paragraph, who contributed what, the owner question). §9.12 (the Codex ticket) is reviewed by someone else; ignore it except to read definitions it gives. Not under review: the review-result lines in §9.1 (last table row) and §9.10 ("Giám khảo Claude độc lập") and the links to source/dragon-fieldwide-*.md files; the author fills those in after the reviews.

CONTEXT
- Game: games/immortality-cultivation (Tu Tien), a deterministic integer lockstep sim at 60 Hz (1 m = 60,000 u). The skill is Sword key 2 "Twin Dragons, One Burning Pearl", today a grey box behind the header flag swordKey2: "twin-pearl".
- The owner's decision (04/11/2026, verbatim): "tôi nghĩ việc 2 rồng chạy lên cổng là k hợp lý, vì chúng ta đang build skill cố gắng dùng chung, map sau này k phải chỉ có hướng về 2 cổng, nên skill phải áp dụng được ở nhiều map chứ k phải là đi về 2 cổng, nó nên dạng skill diện rộng toàn map thì hợp lý hơn". So: field-wide, map-agnostic (no gate count, lanes, waypoints, flow fields or sky-entry points may drive the shape); keep two dragons, one pearl, the lotus climax.
- Constraints: first hit within 50 ms (by F2, canon D58 in docs/games/tu-tien/00-canon.md); fast attack, slow decay; caster side first; integer-only deterministic state; the grey box's damage machinery stays (hit kinds touch/corridor/lotus 15/45/40 %, max 3 hits per beast one per kind >= 20 ticks apart, per-side falloff and per-side budget parts, one swarm-cluster cap per cast, boss cap per cast id, one strike order per tick); canon §7.3 caps each area skill at 20 % of match damage.
- Background: docs/games/tu-tien/skills/DRAGON_SKILL.md §1-§8 (especially §3 A and the grey-box measurements in §8), docs/games/tu-tien/skills/SKILL_REACH.md, docs/games/BALANCE.md, docs/games/tu-tien/00-canon.md §7.3, §8.1, §12.1, D56, D58, D59; the code games/immortality-cultivation/src/sim/twin-pearl.ts, src/content/data/twin-pearl.ts, src/sim/combat.ts, src/sim/fixed.ts, src/content/rules.ts, src/content/data/stage-m0a.ts, src/content/data/beasts.ts.

WHAT TO CHECK (the owner's meaning of PASS: correct and accurate, not "nothing could be added")
1. Is the design correct and complete for the goal: truly map-agnostic, deterministic and integer-safe, consistent with the fixed damage machinery as the code implements it, every rule unambiguous, the first hit by F1 when an eligible damageable beast is alive at F0, the five phases with frame timing, fast attack and slow decay?
2. Are its facts accurate: numbers quoted from §8, SKILL_REACH, canon and the code; the prototype table (you may run proto.py in the parent folder or write your own integer port); the claims about the code (overflow bound, rounding, crow speeds, field data)?
3. Are the numbers consistent across §9.0-§9.11 (frames F0-F102, radii, budgets, thresholds, lengths and speeds)?
4. Is the owner question a real decision, stated correctly against the measured evidence, and are the measurable targets well defined and achievable by the design?
You may write and run throwaway scripts in …/scratchpad/dragon-fieldwide/criticA2/ (create it). Do not read other critics' folders.

A defect is: a wrong fact, a rule that would not work or is ambiguous, a missing element the goal needs, or a contradiction with the constraints or within the design. Wording, style and optional improvements are NOT defects.

ANSWER FORMAT (your final message, nothing else):
VERDICT: PASS
or
VERDICT: FAIL
then a numbered list of defects, each with: where (section), what is wrong, evidence (file:line or computation), and the exact fix.
You may add a short "Optional:" list of non-blocking suggestions after the verdict.
```

### Đề bài U3, U4 (phiếu 2 và quyết định của anh)

```text
You are an independent critic. Review ONE coding ticket inside a game-skill document, plus one consistency question, and return a verdict. You did not write it. Read-only: do not edit, create or delete any file outside your own scratch folder named below, do not use a browser, do not message other agents, do not run git commands that change anything, and do not run the bot or matrix scripts against the game's real tmp/ folders (they write output there). Do not touch games/.wt-ic-twin-fieldwide (another agent works there). Use only the path /Volumes/SS990TPRO/htdocs/typing-game (never /Users/toandx/htdocs/typing-game).

THE DOCUMENT: …/scratchpad/dragon-fieldwide/section9.md (Vietnamese prose, English ids). It will become section 9 of docs/games/tu-tien/skills/DRAGON_SKILL.md. §9.12 holds two Codex tickets run one after the other (Codex = gpt-6.1-sol at xhigh, sandboxed workspace-write, see tools/codex-run/README.md and run.sh). Ticket 1 (header, A-E) changes the sim, content, lab and tests; …

YOUR SCOPE:
(a) TICKET 2 = "#### F. Phiếu 2: bot và số đo", together with the parts of the §9.12 header that ticket 2 relies on (working directory, Claude's setup steps 1-4, the write list, the run.sh override note) and G where it concerns ticket 2. … Ticket 1's functions and fields (B.1 removed names, B.3 cast record, B.4 buildCastGeometry, B.6 exports such as lotusRegion(cast, …) and staticCoverage, B.7 pickDiscs, B.9 resolve condition, D's synthetic stage) are what ticket 2 may use.
(b) CONSISTENCY of the owner's decisions of 04/11 ~19:40, recorded in §9.11, across the whole section: key-2 budget 2.0 W per side, key-2 share ≤ 45 % now and ≤ 35 % after SKILL_REACH part 2, English callouts and player-facing text, the dragon head direction recorded but not in the tickets. Also the resolve condition in §9.2 and B.9 (a cast resolves only if some beast is alive, not immune, and in the ground or sky band; otherwise the Cast stays held …). Report any place in §9.0-§9.12 that still contradicts these, or where the 2.0 W change breaks a number, a test expectation or a threshold.
Not under review: the review-result lines in §9.1 and §9.10 and the links to source/dragon-fieldwide-*.md files.

CONTEXT … (the bot scripts, key2-fix/, key2-review/, golden-before/, DRAGON_SKILL.md §8, docs/codex-queue/195 and 223, run.sh, the sim files and tests)

WHAT TO CHECK (the owner's meaning of PASS: correct and accurate, not "nothing could be added")
1. Does ticket 2 produce every measure §9.8 asks for, with §9.8's definitions, the comparison columns, and the owner's targets?
2. Is every instruction executable as written by a sandboxed coder in the stated directory: the script edits, the new key2-layouts.ts, the handling of casts that do not resolve, the command lines (paths, env variables, variant names that key2-numbers.ts must parse, output folders), the flag-off comparison, without overwriting the old comparison sources; and Claude's steps in G?
3. Are the pass/fail thresholds unambiguous and consistent with §9.7, §9.8 and §9.11?
4. Does anything in ticket 2 contradict ticket 1 or rely on something ticket 1 does not provide?
5. The consistency question (b).
… A defect is: a wrong fact, an instruction that would not work or is ambiguous in its result, a missing step the goal needs, a contradiction with the design, ticket 1, the owner's decisions or the constraints. Wording, style and optional improvements are NOT defects.
ANSWER FORMAT: VERDICT: PASS, or VERDICT: FAIL with numbered defects (where, what, evidence, exact fix); optional "Optional:" list.
```

(Dấu "…" trong khối thứ hai là chỗ rút gọn các đoạn lặp lại y hệt khối thứ nhất hoặc danh sách file; đường dẫn đầy đủ của bản nháp là `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/section9.md`.)

## Câu trả lời nguyên văn

### Lượt 1, critic 1 (cả §9)

VERDICT: FAIL

1. **§9.12 D test 8, with B.4 step 6 ("thêm tham số step vào sPath, không đổi gì khác")**
   - **What is wrong:** test 8 asks for the mirrored nodes and samples to match at 0 u. The `sPath` that B.4 keeps unchanged cannot produce that.
   - **Evidence:**
     - The lateral offset is `mulDivSym(-unit.z, off, 1000)` and `mulDivSym(unit.x, off, 1000)` (src/sim/twin-pearl.ts:235-236).
     - `mulDivSym` is sign-symmetric only in its first argument; `mulDiv` rounds half up (src/sim/fixed.ts:31-42).
     - In the mirror, `firstSide` flips, so `off` flips sign. Whenever the product ends in exactly ...500, the mirrored sample is off by 1 u.
     - My integer port of §9.3–9.4 and B.4 (critic1/intport.py, symm.py) on the two-gate layout: nodes and `pass` mirror exactly. Mirrored dragon 1 has 8 of its 93 samples off by 1 u in z (indices 2, 6, 10, 14, …), and `arc` differs.
     - The existing grey-box lane mirror test passes only because those two lanes happen to hit no exact half.
   - **Fix:** in B.4 step 6, allow this one change to `sPath`:
     - `x = bx + mulDivSym(-unit.z * off, 1, 1000)`
     - `z = bz + mulDivSym(unit.x * off, 1, 1000)`

     I checked it in the port (critic1/fixcheck.py): the two-gate mirror and the arena rotation are then both exact at 0 u. The other option is to relax test 8 to ±1 u for samples and drop the `arc` equality.

2. **§9.12 D tests 3, 7, 9 and E.3 (`key2-layouts.ts`): the cast origin C is never given**
   - **What is wrong:** `castOf` (tests/sim/combat-fixture.ts:128) defaults `origin` to (0; 0), which is H. §9.3 then falls back to F = unitPm(fieldCentre − H). Note that §9.7's numbers assume C = (0; 3).
   - **Evidence (integer port):**
     - Two-gate with C = H: node lengths are 42.75 / 41.42 m. Test 3 expects 45.1 / 43.9 m ± 1 m, so it fails.
     - Arena with C = H: the arena centre is H, so F stays (0, −1000) in both the original and the rotated run. Sides differ and 227 samples differ, so test 9 fails.
     - With C = (0; 3 m), and C rotated to (−3 m; 0), both tests pass.
   - **Fix:** add to D and to bot step 3: every layout test and `key2-layouts.ts` casts with `origin = at(0, 3)`. Test 9 also rotates C to (−3; 0). Test 8 mirrors C to (0; 3), which is unchanged.

3. **§9.12 D test 5 contradicts the per-side budget and the B.7 rule `pool > 0`**
   - **What is wrong:** one first-victim touch hit at F0 uses up that side's whole touch part. That side then has no eligible F1 target. So "each side's nearest beast outside the F0 disc takes touch at F1" fails for the side of the F0 beast (any beast with ≥ 33 HP).
   - **Evidence:**
     - Quality `ok` with Tâm nhãn on: the touch part is mulDiv(mulDiv(mulDiv(225,900,1000),1080,1000),15,100) = 33, and the hit is mulDiv(mulDiv(mulDiv(225,15,100),900,1000),1080,1000) = 33.
     - Quality `good` with Tâm nhãn off: 34 and 34 (twin-pearl.test.ts:481).
     - §8.3 already records this effect.
   - **Fix:** in test 5:
     - call `cast.pool.fill(10 ** 9)` after resolve for the "nearest per side at F1" assertion, as the existing crowd tests do;
     - add a separate assertion that a side whose touch part was spent at F0 gets `disc[s].on === 0`.

4. **§9.12 D test 6: "không gì ngoài 9 m trừ cánh" contradicts B.6**
   - **What is wrong:** `lotusRegion` returns full (2) anywhere inside the H disc (`inHoldDisc`), and that disc can reach past 9 m from P.
   - **Evidence:** in the two-gate layout P ≈ (−0.02; −5.91). The H-disc point (0; 4.5) is 10.4 m from P and gets full lotus.
   - **Fix:** "không gì ngoài 9 m quanh P trừ cánh và đĩa H r 4,5 m".

5. **§9.12 E.7 (and §9.8 bot step 4): Codex cannot make the lab capture under its own rules**
   - **What is wrong:** capturing the lab needs a local vite server and Chrome over CDP (§8.10: `vite --port 3241`, `cdp-run.mjs`). That conflicts with the ticket's own ban on opening a network port. Codex also runs in a `workspace-write` sandbox (tools/codex-run/README.md), and the review folder sits outside the repo.
   - **Evidence for the path:** typing-game-review/review.config.json maps games/immortality-cultivation to the area `tu-tien`, and `captures/tu-tien/dragon` already exists. The ticket's `captures/immortality-cultivation/…` does not follow that.
   - **Fix:** take the capture out of E.7, since Claude records the video in §F anyway. If Codex should still capture, explicitly allow vite on 127.0.0.1 via `heavy.sh --gpu` and use `typing-game-review/captures/tu-tien/twin-pearl-fieldwide/`.

6. **§9.12 header, E.2, E.4, E.5 and bot steps 1–3: no step sets up the worktree**
   - **What is wrong:** `tmp/` is outside Git. A new `games/.wt-immortality-cultivation-codex` (it does not exist yet; `git worktree list` shows only main) would have:
     - no `tmp/skill-reach/` (`bot.ts`, `key2-dense.ts`, `key2-matrix.sh`, `key2-measure.ts`, …);
     - no `tmp/shots/dragon/greybox/golden-before/` (45 files);
     - no `node_modules`.
   - **Why it matters:** `bot.ts` imports `../../src/...` relative to its own folder. Running the main checkout's copy therefore measures the old code, and "Được ghi" only allows `key2-*.ts`.
   - **Fix:** add a setup step that Claude does before the lane starts:
     - create the worktree and give it `node_modules`;
     - copy `tmp/skill-reach/` into the worktree and allow writing `tmp/skill-reach/**` there;
     - in E.2, compare against `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/` by absolute path.

Optional:
- **Checked and correct:**
  - The first hit lands by F1 whenever an eligible damageable beast is alive at F0. A beast added after the snapshot can drain a side's part at F1, but that is itself a positive F1 hit. Beasts only exist at y = 0 or 4 m, so there is no gap-band case.
  - The 32 m split keeps `mulDiv` exact. The real bound is 2ab + c < 2^53, which is about 35 m for this term, not the 50 m fixed.ts states.
  - The rulesHash claim, the flag-off claims and all function names are accurate.
  - The frame numbers F0–F102 are consistent across the section.
  - §9.7 matches my integer port within 0.05 m on lengths and 1 beast on reach.
  - The test 7 coverage thresholds are met: integer port gives two-gate 100 %, three-gate 100 %, one-gate 100 %, behind 90 %, arena 79.5 %.
  - The sample bound "≤ 256 + segments" holds even on a 270 m path.
- **Test 12:** hard timing limits on a cold JIT can be flaky on the loaded machine. Warm up first and assert on the median, or only print the numbers.
- **B.6 `inSkyReach`:** "với mỗi rồng" can be read as "for every dragon". Write "với ít nhất một rồng".
- **B.6 `distSegment2`:** it needs a rule for len = 0, otherwise `mulDivSym(dx, along, 0)` returns NaN. Use the distance to A.
- **`coverageStatic`:** say where it lives, for example an export in sim/twin-pearl.ts, and that its F1 discs ignore the budget.
- **Unmentioned functions:** `inBody` and `inGroundBand`/`inSkyBand` are in neither B.1 nor B.2.
- **Side arrays:** grow `sideSlot`/`sideSerial` with `push(0)`, like `bookAt`, so hashed arrays have no holes.
- **H:** state H = (0; 0) explicitly; no world field holds it.
- **§9.2 empty field:** the lab can never cast on an empty field, because B.9 still needs a damageable beast. That shape is only reachable through `buildCastGeometry`.
- **§9.11:** "chỉ cần đổi heads.toTick" also needs `roar`, `lotus` and `sky.toTick` moved.
- **§9.4 "1,7 lần":** that is relative to §3 A's 26 m estimate. The built grey-box path was about 18–20 m, so the real ratio is about 2.3–2.5×.
- **§9.5 "1,9 m":** true at the crow's base speed. A Cuồng crow on the challenge preset flies 2.73 m/s and reaches about 2.6 m by F56, just outside the 2.5 m capsule.

The check scripts are in /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/critic1/ (intport.py, symm.py, fixcheck.py).

### Lượt 1, critic 2 (cả §9)

VERDICT: FAIL

1. **§9.12 E.2 (flag-off check): the "byte-identical" comparison can never pass.**
   - What is wrong: E.2 says the 36 bot runs (9 profiles × seeds 1–4, `BOT_HASHES=1`) must match `golden-before` "trùng từng byte". The current bot writes fields that `golden-before` does not have. Even a run with no sim change fails this check.
   - Evidence:
     - I byte-compared `tmp/skill-reach/key2-review/golden-now/*.json` (today's flag-off run) with `tmp/shots/dragon/greybox/golden-before/*.json`: 0 of 36 files are identical.
     - The new run adds the top-level keys `key2`, `key2Casts`, `key2Numbers`, `pace`, and `lanePeak`/`lanePeakTick` inside each `waves` entry.
     - Every field that `golden-before` does have is equal. §8.1 already describes the real check as "trùng … ở mọi trường bot cũ có ghi".
     - The `.log` files hold timings, so they are never identical either.
     - The ticket also has Codex rewrite `key2-measure.ts`, which changes the `key2*` output.
   - Fix: replace "trùng từng byte" with: "every JSON field present in the `golden-before` file is deep-equal in the new run (extra keys ignored, `.log` files ignored), plus the pinned-hash test `1a78a82` passes."

2. **§9.12 D tests 5 and 6 (and the §9.7 "Một con quạ" row) contradict B.7 in every §9.8 layout that has crows.**
   - What is wrong: B.7 makes a crow a valid F1 target whenever its side's sky part is above 0. When the F0 disc spends a side's touch part, that side's F1 disc therefore goes to its crow.
     - Test 5's "Không bơm ngân sách: … nên `disc[s].on === 0`" is false in those layouts.
     - Test 6's "quạ … nhận hành lang trong F30–F56 qua con nhộng" fails for any crow that was the F1 target, because it already took its corridor hit at F1.
   - Evidence (two gates, quality "ok", Tâm nhãn lit):
     - Two left-stream beasts are inside r 4.5 m of H: (−2.3; −2.2) at 3.18 m and (−2.03; −3.05) at 3.66 m.
     - The side's touch part is 33 HP and the first touch hit is 33 HP, so the part reaches 0.
     - At t = 1, B.7 skips the ground beasts (part = 0) and takes the crow at (−19; −17): `disc[0] = {on: 1, sky: 1}`. The crow is hit at F1, so it cannot take the capsule hit.
     - Two gates, one gate, three gates, arena and behind all have one or more crows per side. The lone-beast layout has no beast inside 4.5 m. So no §9.8 layout meets test 5's last clause.
     - In the "Một con quạ" layout the crow takes its hit from the F1 sky disc, not "qua con nhộng trời" as §9.7 says.
   - Fix:
     - Test 5: "on a layout with no crow on side s (for example two gates without the two crows), `disc[s].on === 0`; with the crows, `disc[s].sky === 1` at that side's crow."
     - Test 6: run with `cast.pool.fill(10 ** 9)`, or with a ground beast of that side nearer to H than the crow, so the crow is not the F1 target.
     - §9.7: change the "Một con quạ" note to "quạ trúng ở F1 qua đĩa trời".

3. **§9.12 D test 4: the 120 × 120 m synthetic field cannot be built.**
   - What is wrong: test 4 asks for "Đường dài 200 m trên sân tổng hợp 120 × 120 m", and the ticket forbids editing `field.ts`.
   - Evidence:
     - `src/sim/field.ts:176` throws `field: heap keys hold 14 cell bits` once a field has 16,384 cells or more.
     - I ran `makeWorld({ stage })` with ±60 m bounds: it threw "57600 cells asked".
     - The 40 × 40 m arena stage does build (80 × 80 cells).
     - The largest field `createWorld` accepts is about 64 × 63.5 m. A 200 m shortest-order route is not reachable there.
   - Fix: "Đường ≥ 130 m trên sân tổng hợp 60 × 60 m (`minXMm`/`minZMm` −30 000, `maxXMm`/`maxZMm` 30 000; dưới 16 384 ô), step > 0,5 m, số mẫu ≤ 256 + số đoạn". Or call the sampling step directly on a 200 m node list with a stub world `{ tick, stage: { field }, beasts: { list } }`.
   - Side note: my integer port of the sample cap holds on paths of 208–386 m (262–266 samples against bounds of 265–270).

4. **§9.8 vs §9.12 E.4: the pass criterion for the hit count differs.**
   - What is wrong:
     - §9.8 says "12–20 (p10 ≥ 12, p90 ≤ 20), ≥ 70 % lần tung trong dải". p10 ≥ 12 and p90 ≤ 20 already imply 80 % or more in the band, so the "≥ 70 %" is redundant and the rule is self-inconsistent. §8.2's p90 of 21 would fail it.
     - E.4 checks something else: "số con bị trúng trung vị trong 12–20, ≥ 70 % lần tung trong dải".
   - Fix: use one rule in both places, for example "trung vị trong 12–20 và ≥ 70 % lần tung trong 12–20", and drop p10/p90 from §9.8. Or state p10/p90 in both and drop "≥ 70 %".

5. **§9.8 vs §9.12 B.6: two different definitions of `coverageStatic`.**
   - What is wrong:
     - §9.8 builds the F1 disc "từ chính ảnh chụp" (ignoring budget).
     - B.6 `staticCoverage` takes the discs "từ bản ghi (sau t = 1)". Those depend on budget and on F0 hits (see defect 2: in two gates the record's disc is the crow).
     - Tests 7 and E.3/E.4 thresholds use this metric, so the result depends on which definition Codex picks.
   - Fix: in §9.8, say "đĩa F1 lấy từ bản ghi lần tung (sau t = 1), như B.6". Or give B.6 an explicit budget-free disc rule.

6. **§9.4, §9.7, §9.9, §9.11 and D test 3: lengths and head speeds use the node path, but the head flies the S arc.**
   - What is wrong: `pass` is spread over the S arc of the clamped samples, which is about 11–12 % longer than the node path. The stated speeds are therefore too low.
     - §9.4 and §9.11 say about 60 m/s on today's field; the S-arc speed is 67/66.
     - §9.7 and §9.11 say up to 90–92 m/s; the arena's arc gives 85/103 m/s.
     - §9.9 says "dài 20–70 m, 30–90 m/s".
     - Test 3 says "Độ dài đường 45,1 / 43,9 m ± 1 m" without saying which length. `arc[last]` is 50.3 / 49.2 m and would fail.
   - Evidence (my integer port of B.4, base → arc):
     - two gates 45.1/43.9 → 50.3/49.2 m
     - one gate 32.0/31.9 → 35.9/36.7 m
     - three gates 59.0/55.7 → 67.2/62.5 m
     - arena 56.9/68.8 → 63.6/77.0 m
     - behind 38.0/38.3 → 43.1/43.3 m
     - one beast 19.8/21.0 → 22.2/23.3 m
     - one crow 17.3/26.1 → 19.1/28.8 m
     - empty 22.2 → 24.4 m
   - Fix:
     - Label the §9.7 column "theo đường nút", or replace it with arc speeds: 67/66, 48/49, 90/83, 85/103, 57/58, 30/31, 25/38, 33 m/s.
     - In §9.4, §9.9 and §9.11, say "≈ 67 m/s trên sân hôm nay, tới ≈ 103 m/s".
     - Test 3: "Σ isqrt độ dài các đoạn nút (C → neo → P, trước sóng S) 45,1 / 43,9 m ± 1 m".

Checked and correct (the integer port is `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/critic2/port.py`; the mirror and rotation checks are `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/critic2/sym.py`):
- **Layout numbers:** sides and pearl positions match §9.7, and node lengths match the prototype exactly. Coverage including petals and F1 discs is within ±1 of the table, so test 7's thresholds can be met (arena 35/44, behind 36/40).
- **Mirror and rotation:** with the new symmetric rounding, the two-gate mirror and the arena 90° rotation give sides, samples and `pass` exact to 0 u. The old rounding gives 8 mismatches in two gates.
- **Overflow:** largest `2·a·b + c` with 32 m segments is 6.5e15, under 2^53. The threshold for one segment is about 35.4 m.
- **First hit by F1:** it lands by F1 whenever a valid beast exists. The target sits at distance 0 from its own disc. A rule-blocked target can only be passed over after an earlier hit in the same tick dealt positive damage.
- **Claims about the code:** `rulesHash`, flag off, `castOf` origin, the arena stage building, crow speed 2.73 m/s, and the free L key are all as stated.

Optional:
- §9.1 and §9.10 already claim "hai lần duyệt liên tiếp PASS", and they link `source/dragon-fieldwide-*.md` files that don't exist yet. The first critic returned FAIL. Update these after the reviews.
- B.1 should also list the module constants `HOLD_HALF`, `HOLD_DEPTH`, `TOUCH_HALF_LEN`, `TOUCH_HALF_W`. They read the removed content fields, so tsc fails until they are deleted.
- §9.7 "≥ 82 %": the arena is 81.8 %.

### Lượt 1, critic 3 (cả §9)

VERDICT: FAIL

1. **Where:** §9.12 D, test 2, "Kẹp mép 2 m" (section9.md:407), together with the D header rule "mọi lần tung dùng `castOf(world, 2, { origin: at(0, 3) })`" (line 402).
   **What is wrong:** No setup the ticket allows can trigger the clamp, so a test written from the ticket checks nothing.
   **Evidence:** With C = (0; 3), |P − H| ≤ 12 m. On THANH_THACH_AI the clamp box is x ∈ [−18; 18] and z ∈ [−16; 6]. P.z > 6 needs G.z > 10, but beasts stop at z ≤ 8. P.x and P.z < −16 are blocked by the 12 m cap. On the 40 × 40 arena the box is ±18, again beyond 12 m. The empty field gives P = (0; −9), also inside. My integer port never clamps P in any §9.8 layout.
   **Exact fix:** Replace "Kẹp mép 2 m" with: "Kẹp mép: sân trống, gọi `buildCastGeometry(world, castOf(world, 2, { origin: at(0, −3) }))` trên THANH_THACH_AI: F = (0; 1000), P = (0; 6 m) (9 m kẹp về maxZ − 2 m)". Add "trừ test 2 (kẹp) và test 9" to the origin rule in the D header.

2. **Where:** §9.12 D, test 4, "Một đoạn nút 40 m được chia (không đoạn nào > 32 m sau khi chia)" (line 409), with B.4 step 6 (line 312), which says `sampleRoute` returns only `{ sx, sz, arc, pass }`.
   **What is wrong:** The split cannot be seen through the specified return value, so the test cannot check it.
   **Evidence:** I ported `sampleRoute` to integers (critic3/split.py). For a 40 m segment, 32 m split versus no split gives identical samples (max difference 0 u) and identical `pass`, for both an axis segment and a diagonal (24; 32) m segment. Two halves with n = 5 have the same phase and sign as n = 10, and below 35.4 m mulDiv does not overflow.
   **Exact fix:** Export the splitter used by `sampleRoute`, e.g. `splitLong(nodes, maxSegU): number[]`, or have `sampleRoute` also return `split`. Test 4 then asserts the 40 m segment becomes 2 pieces, each ≤ `maxSegmentMm` in u.

3. **Where:** §9.12 E.4 (lines 428–433), under the heading "Kiểm và số phải đạt".
   **What is wrong:** These are gameplay thresholds Codex must meet, but nothing says what to do if one misses. E.3 says "báo, không chỉnh số"; E.4 does not. `src/content/data/twin-pearl.ts` is writable and the forbidden list does not cover its numbers. Codex could retune the budget or radii, which contradicts §9.0.7 (2.5 W kept for comparison with §8) and the sweep plan in §9.11.
   **Exact fix:** Append to E.4: "Nếu một ngưỡng trượt: ghi số và lần tung trượt vào báo cáo; không đổi số trong `data/twin-pearl.ts` hay luật §9 để khớp."

4. **Where:** §9.2 (lines 35–38) against §9.12 B.3 (line 287).
   **What is wrong:** The two contradict each other on what the cast record holds. §9.2 says the record stores the field, H and C, and "serial, slot, x, z, y" for every snapshot beast. B.3 stores only `[slot, serial]` pairs, plus hx/hz and the derived geometry: no C, no field, no F0 positions. `staticCoverage` (B.6) takes the F0 positions as a parameter instead.
   **Exact fix:** Make §9.2 match B.3: "lưu H, F, R, cut2, P, hình học và cặp [slot, serial]; vị trí F0 chỉ dùng lúc dựng, công cụ đo tự ghi để gọi `staticCoverage`". Or add the positions and C to B.3. Pick one.

5. **Where:** §9.9 (line 192), "đường nút dài 20–70 m".
   **What is wrong:** The section's own table has shorter routes: 17.3 m (lone crow, wing route) and 19.8 m (lone beast). My integer port confirms 17.29 m and 19.80 m.
   **Exact fix:** Change to "17–70 m".

Optional:
- C (lab, `L` key): "vòng quanh (tám hướng trong sân hôm nay)" gives no radii. The §9.8 arena radii up to 17 m fall outside today's field in the +z direction (maxZ 8 m). State the radii, e.g. "≤ 7 m về phía +z".
- §9.3 says a late beast takes its side "khi nó nhận đòn đầu tiên". B.5 records the side inside `sideFor` on the first attempted hit, even when that part's budget is 0 and nothing is dealt. Both are deterministic; pick one wording.
- B.6 `volumesAt`: say which bit the F1 sky disc sets (2 or 8).
- §9.11 "Nếu anh giữ 20 %: ngân sách về khoảng 1,25 W": §8.6 measured 29–36 % at 1.25 W. Say that this assumes the reach fixes for the other skills.
- Checked and correct:
  - An integer port of §9.3–9.6 reproduces the §9.7 table and the tests' numbers: P (−0.016; −5.910); node routes 45.10/43.88 m; S arcs 50.34/49.24 m; 3/3 anchors; head speeds 67/66, 48/49, 90/83, 85/103, 57/58 m/s.
  - Static reach is 40, 40, 42, 35 and 36 of 40/40/42/44/40. That meets the test 7 thresholds (arena 79.5 % ≥ 75 %, behind 90 % ≥ 85 %) and E.3's ± 2.
  - The mirror and 90° rotation are exact to 0 u with the new `sPath` rounding, and the 12 m pearl clamp gives 719 999 u (within ± 2 u).
  - The first positive hit lands at F0 or F1 whenever an eligible beast lives at F0. The exceptions are the noted fixed-rule cases, plus a beast that dies or leaves its band before F1, which the 0.1 % allowance in §9.8 covers.
  - Claims about the code are accurate: symbol names, the overflow at ~35.4 m, rulesHash, the default-origin rule, the 16 384-cell limit, and that the golden is still valid (only twin-pearl files changed since `1a78a82`).
  - The synthetic 40 × 40 stage builds and steps through `createWorld`.

### Lượt 2a, A1 (thiết kế)

VERDICT: FAIL

The core geometry in §9.2–§9.6 holds up. It is map-agnostic, integer-safe and deterministic, and it matches the damage machinery in `twin-pearl.ts` and `combat.ts`. The first positive hit does land by F1, apart from the documented cluster-cap-0 case: the F1 target is the nearest eligible beast in the snapshot, and only a positive earlier hit can drain its pool or cluster.

These claims check out:
- **Overflow:** the 35.4 m limit for `2001·len² < 2^53`, and splitting segments at 32 m keeps every segment under it.
- **Crow drift:** a crow drifts 1.87 m by F56, and a frenzied (Cuồng) crow at Challenge difficulty 2.55 m (2000 × 1.05 × 1.3 mm/s), both inside the 3 m sky capsule.
- **Old route:** the old grey-box route is 18.18 m as straight segments and 19.93 m along the S-wave (28.0 m/s), checked by running `twinPearlGeometry`.
- **§9.7 table:** every pearl P, side count, node length, S-arc length and head speed in the table, plus test 3's 50.3 / 49.2 m. I checked them with my own integer port, `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticA1/port.py`.

The defects are in the facts and in the owner question.

1. **§9.11, first bullet: wrong fact.** It says "vì không có ô 2 thì bot chỉ thắng 0–40 %".
   - Evidence: §8.4's "hôm nay" column, the source of the 0–40 % wins, is with today's key 2, the straight line Nhất Tuyến Xuyên Vân. That line takes 18–26 % of match damage (§8.4 "Ô 2/cả trận", §8.5 "ô 2 19,9 %"). The run-2 brief shows the intended meaning: "Without the dragon, bots win 0-40 %".
   - Fix: replace it with "vì với ô 2 hôm nay (đường thẳng, 18–26 % sát thương) bot chỉ thắng 0–40 %".

2. **§9.11, Claude's proposal: contradicts the evidence it cites.** It proposes "ô 2 ≤ 35 % trong lúc làm phần 2 … dự kiến 1,75–2,0 W mỗi bên".
   - Evidence: §8.6 measured 34–43 % at 1.75 W and 37–45 % at 2.0 W with the other skills' reach unchanged. At 2.5 W the Chuẩn bot is at 45.7 % (§8.5). Today only about 1.25 W gets to ≤ 35 % (29–36 %), and there Chuẩn wins 0 %.
   - So the owner would be approving a cap and budget pair that the data says breaks, and the text never says the cap depends on the reach fixes.
   - Fix: add "ở 1,75–2,0 W, §8.6 đo được 34–45 % khi tầm các chiêu khác chưa sửa; trần 35 % chỉ đạt nếu phần sửa tầm kéo phần ô 2 xuống thêm khoảng 5–10 điểm. Nếu chưa đạt thì ngân sách phải về khoảng 1,25 W (29–36 %, Chuẩn thắng 0 %)". Or state the cap as ≤ 45 % for the time before the reach fixes.

3. **§9.11, heading line: the stated reason for dropping §8.8's question 2 is wrong.** It says "câu 2 của §8.8 không còn, vì rồng không chạy về cổng nữa".
   - Evidence: the first anchor is the farthest beast (§9.4), so on today's map the route still runs "lên tới cổng" (§9.7, row 1; the node (−15,5; −17,5) is the gate end).
   - Spending is still first come (§9.6 "Không đổi"), so in a crowd the damage still stops near the heart. That was the whole of question 2 (§8.2: 15,4 / 20,2 m; 26 % of beasts beyond 12 m hit). §9.8 even keeps a "Tầm xa" metric "so với §8.2".
   - Fix: either keep the question in map-agnostic form ("Lúc đông, sát thương có cần tới thú xa nhất không, hay giữ ngân sách tới trước?"), or write "câu 2: giữ đề xuất của Claude ở §8.8 (ngân sách tới trước), đo bằng chỉ số Tầm xa §9.8; anh có thể đổi".

4. **§9.7: the reading claim is false for the design as specified, and the intro overstates the prototype.**
   - "`proto.py` dựng đúng §9.3–9.5" is not accurate. The prototype restarts the S-wave sign at every segment, whereas §9.10 keeps `sPath`'s sign carried across segments. It also leaves out the petals and the F1 discs.
   - With the specified `sPath` and every hit volume included, my port gives:

     | Layout | Table | Port |
     |---|---|---|
     | Arena | 36/44 | 35/44 (79,5 %) |
     | Behind the caster | 37/40 | 36/40 |
     | One gate | 39/40 | 40/40 |
     | Other layouts | as in table | unchanged |

   - With the sign reset I reproduce the prototype exactly (36 and 37), so the gap comes from the sign rule. The bullet "Mọi bố cục có từ 35 thú trở lên đều có ≥ 80 % (đấu trường 81,8 %)" is therefore false for the real design.
   - Fix: change the "Trong tầm" column to 40/40, 40/40, 42/42, 35/44, 36/40, 1/1, 1/1. Change the bullet to "≥ 79 % (đấu trường 79,5 %)". Reword the intro to "dựng §9.3–9.4 bằng số thực; phủ chưa tính cánh hoa sen, đĩa F1, và sóng S bắt đầu dương ở mỗi đoạn".

5. **§9.9: internal contradiction.** "vệt quá nhanh trên đường 70–90 m" clashes with "đường nút dài 17–70 m" in the same paragraph.
   - Evidence: no layout has a route that long. The longest straight-segment route is 68.8 m and the longest S-arc is 77.0 m (arena).
   - Fix: "vệt quá nhanh trên các đường dài nhất (S 63–77 m, đầu rồng 85–103 m/s)".

6. **§9.0 item 6: claims one change but there are at least two.** It says "Chỉ đổi một chỗ: khoảng cách tới Trận Tâm trong thứ tự đánh".
   - First, `hit()`'s side rule also changes, from the gate-based `sideOf` to the snapshot/`cut2` `sideFor`. §9.3, §9.6 ("'bên' nay là bên của §9.3") and B.2 ("hit (trừ dòng lấy bên)") all say so.
   - Second, F1 now adds a new path: sky beasts take a corridor-kind hit from the sky part.
   - Fix: "Đổi hai chỗ: bên của thú theo §9.3 (thay theo cổng), và khoảng cách trong thứ tự đánh là đường chim bay; F1 thêm đĩa trời (loại hành lang, phần trời)".

Optional:
- **§9.8 arena layout order:** spell out the creation order, for example "(1;0), (−1;0), (0;1), (0;−1), (0,7;0,7), (−0,7;0,7), (0,7;−0,7), (−0,7;−0,7), mỗi hướng bán kính 5…17, rồi quạ (15;0), (−15;0), (0;15), (0;−15)". Ties in distance at r = 17 and at 12.95 m are broken by serial. If the "−" variants are listed first, the routes become 67.8 / 60.2 m instead of 56.9 / 68.8, outside E.3's ±1 m.
- **§9.4 wing point W:** state the rounding, `W = H ∓ mulDivSym(9 m, R, 1000)`.
- **§9.5, aftermath row F78–F102:** the view column is empty. Add the peak hold that §3 A had ("giữ đỉnh tới F80", i.e. about F86 after the 6-tick shift) before the erosion that starts at F103, per §2 rule 10.
- **§9.4 speeds:** the old "28 m/s" is measured on the straight segments, while the new "67 m/s" follows the S-wave. The like-for-like old figure is 30.7 m/s.

### Lượt 2a, A2 (thiết kế)

VERDICT: PASS

I found no blocking defect in §9.0–§9.11. Here is what I checked:

- **The §9.7 numbers are right.** I wrote my own integer port of §9.2–§9.6. It uses the code's `mulDiv`, `mulDivSym`, `isqrt` and `unitPm`, the `sPath` with the step parameter and the sign carried across segments, the 32 m split, field clamping, `pass`, `petalFrom`, the F1 discs with the F0 touch-pool drain, and the lotus petals. Every row matches:
  - Sides 20/20, 20/20, 21/21, 22/22, 20/20, 1/0, 1/0.
  - Pearls (0;−5.9), (0;−6.2), (0;−3.4), (0;0), (−0.3;3.3), (0;−7.2), (−6.0;−7.2), (0;−9).
  - Node lengths 45.10/43.88, 31.95/31.88, 58.97/55.66, 56.89/68.85, 38.05/38.26, 19.80/21.01, 17.29/26.13 and 22.21 m.
  - Arc lengths along the S path 50.34/49.24 m and so on, giving speeds of 67/66, 48/49, 90/83, 85/103, 57/58, 30/31, 25/38 and 33 m/s.
  - In range: 40/40, 40/40, 42/42, 35/44, 36/40, 1/1, 1/1.
- **The old path facts are right.** Running `twinPearlGeometry` on the code gives a base path of 18.18 m, an S path of 19.93 m and 30.7 m/s, which supports "18–20 m, about 31 m/s" in §9.4.
- **The code claims are right.**
  - The `sPath` overflow bound is 2001·len² < 2^53, so a segment must be under about 35.4 m.
  - In the old offset, `mulDivSym(-unit.z, off, 1000)` rounds by the sign of `a` only, which is why it was off by 1 u in the mirror.
  - The time to reach F102 is 48 + 54 ticks, and the lotus holds its peak until F86, as §3 A gives (F51 to F80, 29 ticks).
  - Crows move 1.87 m by F56 at 2 m/s. At 2000 × 1.05 × 1.30 = 2730 mm/s they move 2.55 m, so a 3 m capsule covers both. Beast height is only ever 0 or 4 m, so no beast sits between the two bands.
  - `heartDistance` reads the flow field, as stated.
- **The first hit lands by F1.** The F0 disc drains a side's touch pool only through a hit that does damage. If nothing landed at F0, the pools are full at F1, so an eligible snapshot beast stays a valid F1 target. Any hit that comes earlier in the same tick does damage itself. The only exception is the documented one-HP swarm beast.
- **The rules are deterministic, integer-safe and symmetric.** All products stay under 2^53, including the head-to-anchor capsule and the pearl scaling. A 90° rotation and the x mirror both come out exact to 0 u with the symmetric offset rounding.
- **The owner question matches §8.4 and §8.6.**
  - The old grey box takes 41–50 %.
  - At 2.0 W per side key 2 takes 37–45 %, and the Mới to Nhanh bots win 45–100 %.
  - At 1.25 W it takes 29–36 % and the Chuẩn bot wins 0 %, with 11.9 beasts hit.
  - Today's straight-line key 2 takes 18–26 %, and the bots win 0–40 %.
  - The Chuẩn bot deals 43 W a minute against a D_ref of 75.
- **The crow target looks reachable.** In the 92 dense casts, 64 had two crows and the old crow hit rate was 91.6 %. With the Tâm nhãn bonus, the sky pool still covers two crows per side.

Optional:
1. **§9.5, roar beat (F49–F56).** The sim heads reach P at F48, together with the pearl. "Hai đầu quay vào ngọc, chậm lại" therefore describes a move the head cannot make while it is drawn at `headIndex`. Either say the view holds each head a little short of P from about F46, or reword the line as "hai đầu đã kề ngọc, ngẩng lên, há hàm".
2. **§9.3, player close to H.** When C is within about a metre of H, F turns sharply with small player moves. Consider using the field-centre fallback when |H − C| is under 1 m.
3. **§9.7, proto.py output.** The "speed" that proto.py prints is node length / 0.75 s (60/59 m/s on two gates). The table's speeds along the S path come from proto's `sample()`. Say so, so anyone who reruns the script is not confused.
4. **§9.0 item 5.** The F1 discs are called "hai đĩa chạm", but a disc can be a sky disc (corridor kind, sky budget).
5. **§9.9.** "25–105 m/s" could read "25–103 m/s" to match the table.
6. **Crows in the bot run.** An F1 sky disc can use a side's whole 0.8 W sky budget on its nearest crow at about 85 % falloff. At quality multiplier 1.0 or below with no bonus, a second crow on that side gets nothing. Watch "Quạ ≥ 90 %" in casts with two or more crows on one side.

My scripts are in /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticA2/: `port.py` (the integer port), `oldgeo.mts` (the old geometry) and `protoarc.py` (proto's S-path speeds).

### Lượt 2a, A3 (thiết kế)

VERDICT: PASS

I checked §9.0 to §9.11 against the code, §8, SKILL_REACH, the canon and two independent recomputations. I found no defect: no wrong fact, unworkable rule, missing element or contradiction.

**What I verified**
- **§9.7 table:** I wrote my own integer port of §9.3–9.4: `mulDiv`/`mulDivSym`/`isqrt`, `sPath` with the sign carried across segments, symmetric rounding, adaptive step, field clamp, petals, F1 discs. Every row matches:
  - sides, pearl P and node lengths: 45.1/43.9, 32.0/31.9, 59.0/55.7, 56.9/68.8, 38.0/38.3, 19.8/21.0, 17.3/26.1 and 22.2 m;
  - S-arc head speeds: 67/66, 48/49, 90/83, 85/103, 57/58, 30/31, 25/38 and 33 m/s;
  - in-range counts: 40, 40, 42, 35/44 (79.5 %), 36/40, 1 and 1.

  `proto.py` reproduces the node lengths too.
- **Mirror and rotation:** in my port both are exact to 0 u. The two-gate layout flipped x → −x swaps the sides; the arena rotated 90°, with C at (−3; 0), keeps them.
- **Overflow bound:** `mulDiv(4000·r, len − r, len²)` needs 2001·len² < 2^53, so a segment must be under 35.4 m. The 32 m split is safe. The bound "257 + number of segments" holds whether the step is computed before or after the split.
- **Old grey box:** the S path from the meeting point to the gate is 19.9 m (18.2 m straight), so the head ran at 30.7 m/s. That matches "18–20 m, about 31 m/s".
- **Crow speeds:** 2 m/s; the Cuồng crow at Thử thách is 2000 × 1.05 × 1.30 = 2.73 m/s. By F56 they move 1.87 and 2.55 m, inside the 3 m capsule. Only Hỏa Nha flies (4 m), so nothing sits between the two height bands today.
- **Frames:** F102 = 48 + 54, which is the `TWIN_PEARL_END_TICK` formula. Roar F49–F56, lotus F57–F77, sky F30–F56, lotus peak held to F86 (= 57 + 29, as in §3 A). The 60-tick example (lotus at F72) is consistent. The rule "a beast hit by the body by F57 can still take the lotus by F77" holds.
- **First hit by F1:** the F1 target rule requires a mayHit-eligible beast with budget left, Vương under cap and cluster cap above 0, and the target sits inside its own disc. Any beast in the same disc that is struck before the target is itself a positive hit, so the first positive hit at F0 or F1 follows.
- **Damage machinery:** shares, falloff, per-side budget parts, the single cluster cap, the boss cap, `limit = left` and the `min(damage, remaining)` rebuttal in §9.10 all match the code.
- **§9.11 owner question:** it is a real decision, and its numbers agree with §8.4–8.6, SKILL_REACH §5.5 (D_ref 75 against 43 W/min) and canon §7.3 (≤ 20 %, a "report" row).

Optional (non-blocking):
1. **Crow-hit target (≥ 90 %) is at risk; nothing in §9.5/§9.8 says so.** In dense casts the F0 disc usually spends the whole touch budget part, so the F1 disc goes to a crow. That crow is the side's second victim (falloff 85 %): its hit of 101 × 0.85 ≈ 86 HP caps at the crow's 72 HP and empties the 72 HP sky part when M_q × bucket = 1. A second crow on that side then gets nothing. The grey box hit crows at F30+ near the 40 % falloff floor, which left room for two crows. Suggest a sentence in §9.5/§9.8 and reporting the crow rate separately for casts with ≥ 2 crows on one side.
2. **§9.8 "35–45 thú":** §8 bins by beasts on the two lanes. State whether the new bin counts all snapshot beasts (crows included) or keeps §8's bin, so the comparison stays like-for-like.
3. **Sound cues:** §9 replaces §3 A's frames, but §3 A's sound frames (F43 silence, F47 roars, F51 bell) are not restated. They become F49, F53 and F57.
4. **§9.6 "Quét trời" row:** the values are right, but the note mentions only the shape change. The radius also went from 2.5 to 3 m and the window from F50 to F56.
5. **§9.5 F1 row:** say "nearest H at its F1 position", as B.7 does.

My scripts are in /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticA3/ (`port.py` for the table, `inv.py` for mirror and rotation).

### Lượt 2b, B1 (phiếu)

VERDICT: FAIL

The simulation part of the ticket (A, B, D) checks out. An integer port I wrote of B.4 and B.6 (`criticB1/port.ts`) reproduces every row of the §9.7 table: two gates 45.10/43.88 m of node path, final arc 50.34/49.24 m, P = (−0.02; −5.91), 40/40 in reach; three gates 58.97/55.66 m, 42/42; arena 56.89/68.85 m, 35/44; behind 38.05/38.26 m, 36/40. It also confirms these:
- the thresholds of tests 2, 3 and 7 can be met;
- the mirror and rotation tests come out exact to 0 u, and only with the new rounding in `sPath` (the old rounding gives 8 of 93 samples off);
- the sample bound holds (a 295 m zigzag gives 261 samples against a bound of 267);
- the two-gate F0 touch drains both sides, as test 5 expects;
- the synthetic 40 × 40 m arena stage builds with `createWorld`.

The defects are in what the ticket asks for around the simulation:

1. **§9.12 C: the lab's tide depends on code that B.1 removes, and C gives no replacement.**
   - **What is wrong:** C only says to draw from the cast record. Nothing in C replaces the lab's tide, refill and boss spawning, and the refill rule breaks "press 2 right after L, while the layout is intact".
   - **Evidence, removed imports:** `src/lab/twin-pearl-greybox.ts:22` imports `twinPearlGeometry`, `skyFront` and `TwinGeometry`. These are used at:
     - `:212` (`this.geo = …`);
     - `:240–252`: the lane, sky-route and meeting-point drawings;
     - `:301–303`: `along()` reads `lane.route`;
     - `:348–351`: `crow()` reads `skyFrom` and `skyTo`;
     - `:404`: `addBoss` uses `along`.
   - **Evidence, refill:** `refill()` (`:383–394`) tops the field up to 38 ground beasts and 4 crows. It runs at the start of every `stepWorld()` (`:446`), including the step `cast()` takes before F0. Every L layout has 2–3 crows, and the "vòng quanh" layout keeps 33 ground beasts after dropping the 7 points outside the field. So extra beasts appear at the gates and corners before the snapshot is taken.
   - **Evidence, side split:** `:486` splits damage west/east by gate label, while C says the labels are arbitrary.
   - **Fix:** add to C:
     - On reset, load the §9.8 two-gate layout (or keep `seedTide` with a lab-local route helper built from the flow field, plus `FIELD.skyEntries` for crows).
     - Turn auto refill off while an L layout is loaded.
     - N re-seeds the current layout.
     - V spawns the Vương at `gatePoint(stage, "A")`.
     - Crows always spawn with gate `"sky"`.
     - West/east and the coverage panel use `cast.book[].side`.

2. **§9.12 C: the lab draws at most 64 trail samples per dragon, far fewer than the new routes have.**
   - **Evidence:** `twin-pearl-greybox.ts:178` creates `InstancedMesh(bodyGeo, …, 64)`, and the loop at `:619–620` stops at 64, counting from `range.first` (the oldest sample).
     - Two gates: 93/92 samples per dragon, all of them live from F48 to F57.
     - Arena: 140 samples.
     - So the newest 29–76 samples, the part near the head and pearl, are never drawn. The owner's review video would show a trail that stops well short of the head.
   - **Fix:** size the mesh to `maxSamples + 1 + segments` (for example 320), or draw from `range.last` backwards.

3. **§9.12 has no bot step, but E.2–E.5 depend on bot changes.**
   - **Evidence:**
     - `tmp/skill-reach/key2-measure.ts:12` imports `inHold`, `inTouch`, `lotusRegion` and `twinPearlGeometry` (B.1 removes three and changes the signature of `lotusRegion`).
     - `bot.ts:10` and `:195` build a `Key2Recorder` for every match, the flag-off ones included. `start()` → `coverage()` → `laneRoutes()` calls `twinPearlGeometry` for both variants. So E.2's flag-off golden run fails at import.
     - `key2-aggregate.ts:32–33` and `:77–81` read `aliveA/aliveB`, west/east by gate, `coverA/B` and `reachW/E`, but E.4 needs `coverageStatic`, the side split with at least 5 beasts a side, and crows.
     - `key2-layouts.ts`, which E.3 runs, does not exist.
     - §9.12 never tells Codex to do §9.8 Bot steps 1–3.
   - **Fix:** add "G. Bot (`tmp/skill-reach`, outside Git)":
     - `key2-measure.ts` per §9.8 step 1:
       - drop the lane and line coverage and the `twinPearlGeometry` use;
       - classify the lotus part with `lotusRegion(cast, …)`;
       - after t ≥ 1, record `coverageStatic` (ground and sky) from the F0 positions;
       - record per-side counts and damage from `cast.book` and the reach per side.
     - `key2-aggregate.ts`: use the new fields and the "each side ≥ 5" filter.
     - New `key2-layouts.ts` per §9.8 step 3: use D's arena stage, and call `buildCastGeometry` for the empty field.
     - Say that E.2 runs only after `key2-measure.ts` no longer imports the removed names.

4. **§9.12 E.4–E.6: two §9.8 targets are not checked.**
   - **Evidence:**
     - E.6 only prints performance. §9.8 sets ≤ 0.2 ms to build the geometry and ≤ 50 µs per tick per cast with 60 beasts, and test 12 only fails at 4×.
     - §9.8's "first hit later than F2 in under 0.1 % of real-match casts" is in no check (E.4 covers the dense scan only).
   - **Fix:**
     - E.6: "pass if the median build is ≤ 0.2 ms and ≤ 50 µs per tick per cast; otherwise report".
     - E.5: add "first hit later than F2 in < 0.1 % of real-match casts that have a valid beast".

Optional:
- `sampleRoute` returns no `step`, so test 4's "step > 0.5 m" can't be checked directly. Return `step` too, or check `sx.length` against `total / U(500)`.
- State the base directory for each path and Codex's working directory.
  - The write list mixes paths relative to the game with the parent repo's `docs/codex-queue/`.
  - With `run.sh -C <worktree>` under `workspace-write`, Codex cannot write the report there.
  - `pnpm build` writes `dist/`, which is not on the write list. Ticket 255 used `vite build --outDir /private/tmp/…`.
- The petal check covers the whole segment `[petalFrom−1, petalFrom]`, so up to one step past 13 m. That is acceptable, but say so.
- Test 3's "anchor 1 is the beast farthest from H": the record keeps the anchors only in path order. Check that this beast is one of the nodes.

My scripts are in /private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticB1/: `port.ts`, `run.ts`–`run4.ts` and `arena.ts`.

### Lượt 2b, B2 (phiếu)

VERDICT: FAIL

1. **Where:** §9.12 header and setup step 1, together with E.1 ("`pnpm test` xanh").
   **What is wrong:** Setup step 1 lets Claude choose between `pnpm install --offline` and linking the worktree's `node_modules` to the main tree's. With the link, `pnpm test` (which runs `vitest run` with the default config loader) cannot work as written inside Codex's `workspace-write` sandbox. In this run's sandbox the only writable places are the worktree and /tmp. Vitest has to write its bundled config, and that write goes through the link into `games/immortality-cultivation/node_modules`. That folder is outside the sandbox, so the write is refused and Vitest stops before running any test. If the write were allowed, it would land in the main tree that another agent is using, which the house rules forbid.
   **Evidence:**
   - `tools/codex-run/run.sh` starts Codex with `-s "$sandbox" -C "$workdir"`, so the worktree is the only writable project folder.
   - `node_modules/vite/dist/node/chunks/config.js:36154-36165`: `loadConfigFromBundledFile` runs `mkdir(<nearest node_modules>/.vite-temp)` (only `EACCES` falls back), then `writeFile` of the bundled config into it.
   - `.vite-temp` and `.vite/vitest` already exist in the main game's `node_modules`, so the `mkdir` succeeds and the `writeFile` is the call that fails.
   - Ticket 255 used the same linked setup, and Codex had to change the commands (`docs/codex-queue/255-report.md` §4: "thêm `--configLoader runner` … `--no-cache` để không tạo file bundle cấu hình trong `node_modules/.vite-temp` thông qua symlink sang game"). E.1 already copies that change for the Vite build, but not for the tests.
   **Exact fix:** in E.1, replace "`pnpm test` xanh" with "`node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner` xanh (như báo cáo 255)". Alternatively, make setup step 1 require a real `pnpm install --offline` in the worktree and remove the link option.

2. **Where:** §9.12 F.1 and F.2, and the balance check in E.4 ("cân hai bên … ở ≥ 85 % lần tung đủ điều kiện").
   **What is wrong:** F.2 counts a cast for the side balance only "mà mỗi bên ≥ 5 con", but no step says which count that is. F.1 only records per-side counts taken from `cast.book[].side`, which are beasts hit. So the natural reading is "≥ 5 beasts hit per side". The design (§9.8, "Cân hai bên" row: "số thú ảnh chụp hai bên lệch ≤ 1 … khi mỗi bên ≥ 5 con") and the old rule in §8.1 ("chỉ tính lần tung có thú ở cả hai đường") point to beasts present in the F0 snapshot. The two readings select different sets of casts, especially in the low-budget sweeps where hits per side fall, so the E.4 pass/fail number depends on which one Codex picks.
   **Evidence:** F.1 bullet 4 ("số con và sát thương mỗi bên lấy từ `cast.book[].side`"), F.2 bullet 2, and the §9.8 table row.
   **Exact fix:**
   - In F.1, add: "ghi thêm số thú ảnh chụp mỗi bên (đếm `snapshot` theo `sideSlot`)".
   - In F.2, change the condition to: "cân hai bên chỉ tính lần tung mà mỗi bên có ≥ 5 thú trong ảnh chụp F0".

Optional:
- The house rules that `run.sh` puts in front of the ticket say "do not run the games' builds or test suites" and "never its src, scripts, tests". One sentence saying that E overrides this for the worktree only would remove the conflict. Ticket 255 worked, but only by inference.
- F.1: the recorder also runs for flag-off ("line") matches, where there is no cast record. Say explicitly that the per-side split and `staticCoverage` apply only when `o.cast !== null`, so E.2 does not crash on a null.
- `tmp/skill-reach/key2-numbers.ts` "narrow" variant writes to removed fields (`touch.halfWidthMm`, `hold.halfWidthMm`). No planned run uses it; it could be dropped or noted.
- C (lab): add L to the panel's button list, as N and V are now.
- No step assigns a changelog entry for this change (`docs/changelog/2026-11-04-…`); G could name it.
- What I checked and found correct:
  - I ported B.4 in integer arithmetic (B.3 / §9.3–9.4: side split, pearl, anchors, routes, long-segment split, S path with the new rounding, field clamp, `pass`, petal start, sky anchors) plus the static coverage check. It reproduces every §9.7 number: two gates 45.10/43.88 m (S-path arc 50.34/49.24 m), one gate 31.95/31.88, three gates 58.97/55.66, arena 56.89/68.85, behind the player 38.05/38.26, one beast 19.80/21.01, one crow 17.29/26.13, empty field 22.21 m. Coverage is 40/40, 40/40, 42/42, 35/44, 36/40, 1/1, 1/1, the same whether or not F0 has already spent the touch budget.
  - So the thresholds in tests 2, 3 and 7 and in E.3 can be met.
  - The pearl clamp to 12 m has at most 1.5 u of error, inside test 2's ±2 u.
  - The synthetic 40 × 40 m test stage builds a world.
  - Under the stated rounding, mirroring and 90° rotation give exact results.
  - Test 5's "touch budget spent, so `disc[s].on === 0`" holds: two beasts per side stand inside the F0 disc and the first hit already uses the whole 33 HP touch budget.
  - The scripts are at `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticB2/port.ts` and `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticB2/layouts.ts`.

### Lượt 2b, B3 (phiếu)

VERDICT: FAIL

The ticket matches the design in §9.2–§9.6, and its numbers and tests hold up. I checked them with an integer port of B.4–B.8 built on the game's own `fixed.ts`, `combat.ts`, the posture module and the test fixture (scratch folder `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticB3/`):
- **§9.7 table:** reproduced exactly: node lengths, final arcs, head speeds and the in-reach column (40/40, 40/40, 42/42, 35/44, 36/40, 1/1, 1/1).
- **Tests 2 and 3:** two-gate pearl at (−0.02; −5.91); routes 45.10 / 43.88 m, final arcs 50.34 / 49.24 m.
- **Test 5:** every case behaves as written: no F1 disc on either side without crows, sky discs at the crows with them, and ground discs at the nearest beasts with the budget filled.
- **Test 7:** the first positive hit lands on F0 or F1 in every layout, and every coverage threshold is met.
- **Tests 8 and 9:** the mirror and the rotation both give identical hits and samples, to 0 u.
- **Other checks:** the arena stage builds; µs per tick and build time are well under the test-12 limits; flag-off behaviour and tsc are not affected by the write list.

Three defects remain, all in E/F:

1. **Where:** E.2–E.5 and F (running the bot scripts).
   - **What is wrong:** every bot step runs the `tmp/skill-reach` scripts through the tsx command-line tool. In Codex's `workspace-write` sandbox that tool dies before the script starts, with `listen EPERM` on its IPC pipe. The ticket gives no command lines, so Codex will copy §8.10 or `key2-matrix.sh`, and both use that tool.
   - **Evidence:**
     - `tmp/skill-reach/key2-matrix.sh:14–15` hard-codes `node_modules/.bin/tsx`.
     - `docs/codex-queue/023-report.md:29` records the failure: "CLI `tsx` bị sandbox chặn khi tạo IPC pipe: `listen EPERM`".
     - `.local/codex-runs/195-dh-deck-notice-and-idle-speed/events.jsonl` and `076-mf-c20-map-pilot/events.jsonl` show `listen EPERM: operation not permitted …/T/tsx-501/<pid>.pipe`.
   - **Related gap:** no output folder is named. Reusing §8.10's `KEY2_OUT=tmp/skill-reach/key2-fix` would overwrite the source of the "hai hành lang" comparison column in Codex's copy (DRAGON_SKILL.md:571–578).
   - **Fix:** add to F:
     - "Run every `tmp/skill-reach` script as `TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/<script>.ts …`, and replace the two `node_modules/.bin/tsx` in `key2-matrix.sh` with that form."
     - Give the exact E.2, E.4 and E.5 command lines with fresh output folders (for example `KEY2_OUT=tmp/skill-reach/key2-fieldwide` and `tmp/skill-reach/key2-fieldwide/golden-now`).
     - Name the comparison source: `tmp/skill-reach/key2-fix/numbers.json`, or the §8 tables.

2. **Where:** F.1.
   - **What is wrong:** it says to drop `laneRoutes`, `coverA`/`coverB` and the per-gate `reachW`/`reachE`, then says flag-off ("line") matches keep exactly the old fields. Both cannot be followed.
   - **Evidence:** `key2-measure.ts` computes `coverA`/`coverB` for every variant, line included: `start()` at line 135 calls `coverage()`, which calls `laneRoutes()`, which calls `twinPearlGeometry()` (lines 209–256). B.1 removes `twinPearlGeometry` and `laneRoute`, so line cannot keep `coverA`/`coverB` without re-implementing the lane routes in the bot.
   - **Fix:** one sentence: "Line matches drop `coverA`/`coverB` as well, with no replacement, and keep every other old field, `reachW`/`reachE` included." Alternatively, tell the bot to keep its own copy of `laneRoute` for line.

3. **Where:** E.4 against F.3.
   - **What is wrong:** F.3 prints the "35–45 thú" bucket two ways: ground beasts in the snapshot (as §8) and all snapshot beasts. E.4 gives pass/fail thresholds (median 12–20, ≥ 70 % of casts in 12–20, `coverageStatic` ≥ 75 %, crows, side balance) without saying which bucket they apply to.
   - **Evidence:** the buckets hold different casts, so one threshold can pass on one and fail on the other. The result of E.4 is therefore ambiguous.
   - **Fix:** in E.4, state "The thresholds apply to the ground-beast bucket (aliveA + aliveB at the cast, as §8.2); the all-beasts bucket is printed for information." The reverse choice also works, as long as only one bucket gates.

Optional:
- In B.7, `beastByRef` from `combat.ts` (already imported) does the same as `beastAt` from `world.ts` and avoids a new import cycle (twin-pearl → world → skills → twin-pearl). The cycle works today, as `boss.ts` shows.
- The E.6 build target (≤ 0.2 ms) is tight: a plain integer port measured about 120–250 µs at 40–60 beasts. Expect a reported number there rather than a clean pass.
- Test 6: each snapshot crow lies inside its own capsule end at F30, so unless the F1 sky disc already hit it, its sky hit is exactly F30. The test can assert that tick.

### Lượt 3, S1 (phiếu 1)

VERDICT: FAIL

1. **§9.12, phần đầu và "Claude chuẩn bị trước khi giao" (bước 1–3): Codex không được chỉ chỗ đọc thiết kế, và không có bước ghi phiếu cùng lệnh chạy.**
   - **Lỗi:** Phiếu 1 dựa vào §9.3, §9.4, §9.5 và §9.8 nhưng chỉ ghi số mục, không ghi tên file. Các mục đó chứa công thức F/R/`cut2`, ngọc, điểm neo, thứ tự bay, `W`, và toạ độ bảy bố cục mà test 1–9 cần. Codex chạy trong `games/.wt-immortality-cultivation-codex`. Đây là bản checkout của repo game, không có `DRAGON_SKILL.md`.
   - **Bằng chứng:**
     - `find games/immortality-cultivation/docs -iname '*dragon*'` chỉ ra `docs/changelog/2026-11-04-lab-twin-dragons-greybox.md`. Thư mục `docs/` của game chỉ có `README.md`, `SYNC_DEBT.md` và `changelog/`.
     - `tools/codex-run/run.sh` chỉ gửi đúng nội dung file phiếu (`cat "$root/$brief"`). Nó cần `<brief.md>` và `cwd` tính từ gốc repo cha. Ba bước chuẩn bị không nói phiếu chứa gì, cũng không ghi lệnh chạy.
   - **Sửa:** thêm bước 4 vào "Claude chuẩn bị":

     "4. Ghi `docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md`. Dòng đầu: 'Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md` §9.0–§9.11; mọi §9.x trong phiếu là của file này.' Có thể chép nguyên văn §9.0–§9.11 thay cho dòng đó. Sau đó là phần đầu §9.12 và A–E, không có F. Chạy `tools/codex-run/run.sh <n>-tt-twin-pearl-fieldwide docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md games/.wt-immortality-cultivation-codex xhigh workspace-write`."

2. **§9.12 B.7: sai sự thật về import.**
   - **Lỗi:** Phiếu ghi "`beastByRef` … (`src/sim/combat.ts`, đã được nhập)". Thực tế `twin-pearl.ts` chưa nhập hàm này.
   - **Bằng chứng:** `src/sim/twin-pearl.ts:45` chỉ nhập `createAreaHit, damageBeast, scaleHit, wHpOf, type AreaHit` từ `./combat`.
   - **Sửa:** đổi thành "(`src/sim/combat.ts`; thêm `beastByRef` vào dòng import từ `./combat`)".

Optional:
- **Đã kiểm, không có lỗi.** Tôi viết lại B.4–B.8 bằng số nguyên và chạy trên module thật của game (chỉ đọc). Kết quả khớp §9.7 và các ngưỡng ở D:
  - Hai cổng: P (−0,02; −5,91). Đường nút 45,10 / 43,88 m, cung cuối 50,34 / 49,24 m, 3 neo mỗi bên. Trong tầm 40/40.
  - Đấu trường 35/44, sau lưng 36/40, ba cổng 42/42, một cổng 40/40. Đòn đầu ở F0 hoặc F1 ở mọi bố cục.
  - Test 2: P ở mép là (0; 6 m). Với mười Phong Lang, |P| = 12 m, lệch 0 u.
  - Test 5: không quạ thì cả hai đĩa tắt. Có quạ thì `1S/1S` (đĩa trời ở quạ mỗi bên). Khi bơm ngân sách, con gần H nhất ngoài đĩa F0 nhận chạm ở F1.
  - Test 6: quạ trúng đúng F30.
  - Test 8 (gương) và test 9 (xoay) trùng tới 0 u và trùng mọi đòn. Bỏ cách làm tròn mới của B.4.6 thì gương lệch, đúng như phiếu nói.
  - Hiệu năng sau khi chạy nóng: dựng hình học khoảng 0,13 ms, khoảng 13 µs mỗi tick mỗi lần tung.
  - Test hiện có `tests/sim/twin-pearl.test.ts` qua 27/27 ở HEAD `bc94110`.
  - Script ở `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticS1/` (`fw.ts`, `run.ts`, `sym.ts`, `t2.ts`, `perf.ts`).
- **B.6 và B.8 viết số tick trần (1–2, 30–56, 57–77, 48).** Nên ghi rõ: "mọi khung đọc từ `TWIN_PEARL`, không viết số tick trong mã". Không vậy thì lời hứa ở §9.11 ("chỉ cần đổi số trong bảng") không còn đúng.
- **Chưa có test nào bắt được `heartDistance` còn sót trong thứ tự đánh.** Ở M0a hai cổng dùng chung một trường dòng chảy, nên test 10 không phát hiện được. Nên thêm một test có hai thú cách H bằng nhau theo đường chim bay nhưng khác `heartDistance`.
- **Nên ghi rõ "xuất" `buildCastGeometry`**, vì test 2, test 7 và bot gọi thẳng nó.
- **Lab:** nên ghi rõ tính `staticCoverage` một lần mỗi lần tung, khi t ≥ 1. Mỗi lần gọi tốn khoảng 2–3 triệu phép tính, nếu gọi mỗi khung hình thì lab sẽ giật.
- **Bố cục hai cổng:** ba thú nằm trong bán kính 0,9 m của Trận Trụ (cách tâm 0,47 / 0,48 / 0,80 m). Test không sao vì thú đứng yên, nhưng trong lab thú đi lại.
- **Câu "tắt tự bơm thêm thú khi đang ở một bố cục"** nên đổi thành "bỏ hẳn `refill()` và phần tự bơm cũ". Lab nay luôn ở một bố cục, và `along()` đã bị bỏ.

### Lượt 3, S2 (phiếu 1)

VERDICT: FAIL

1. **Where:** §9.12, "Claude chuẩn bị" step 1. The same problem reaches the header's working directory and the `run.sh … games/.wt-immortality-cultivation-codex …` line.
   - **What is wrong:** step 1 says to create the worktree `games/.wt-immortality-cultivation-codex` on a new branch from the game's HEAD. That path is already a live worktree on branch `codex/flipbook-v2`, holding ticket 258's output. That output is uncommitted and not yet reviewed. Ticket 259 also plans to create the same path, on branch `codex/jade-ring-material`. So step 1 cannot run as written: `git worktree add` refuses a path that already exists. If Claude reuses the folder instead, ticket 258's diff ends up in this ticket's branch, in the vitest run and in Claude's diff review.
   - **Evidence:**
     - `git -C games/immortality-cultivation worktree list` shows `games/.wt-immortality-cultivation-codex bc94110 [codex/flipbook-v2]`.
     - `git -C games/.wt-immortality-cultivation-codex status --short --untracked-files=all` shows `M src/view/skills/flipbook.ts`, `?? tests/view/flipbook-v2.test.ts` and `?? docs/changelog/2026-11-04-flipbook-v2.md`.
     - `docs/codex-queue/258-report.md` line 3: "chưa commit; chờ Claude duyệt diff và kiểm GPU".
     - `docs/codex-queue/259-tt-jade-ring-material.md` lines 361–362: the same path, created with `worktree add ../.wt-immortality-cultivation-codex -b codex/jade-ring-material main`.
   - **Exact fix:** in step 1, give this ticket its own worktree and a named branch:
     - `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-twin-fieldwide -b codex/twin-pearl-fieldwide main`
     - then `ln -s ../immortality-cultivation/node_modules games/.wt-ic-twin-fieldwide/node_modules`.
     - Put `games/.wt-ic-twin-fieldwide` in the header's working directory and in the `run.sh` cwd argument.
     - Alternative: keep the old path, but add the precondition "chỉ làm sau khi phiếu 258 và 259 đã merge và `git worktree remove games/.wt-immortality-cultivation-codex` chạy sạch". Still name the branch `codex/twin-pearl-fieldwide`.

Optional (non-blocking):
- **What I checked and found correct.** I wrote my own integer port of B.4–B.8 (`/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticS2/port.mjs`, plus `sim.mjs` beside it). It reproduces §9.7 to the shown precision:
  - **Two gates:** node paths 45.10 / 43.88 m, final arc 50.34 / 49.24 m, P (−0.02; −5.91), sides 20/20, cut2 −44,000 u.
  - **Other layouts:** P, node lengths and head speeds match the table for one gate, three gates, arena, behind, one beast, one crow and the empty field.
  - **Coverage:** 40/40, 40/40, 42/42, 35/44 (arena) and 36/40 (behind), so every threshold in test 7 holds, with a margin of 2 beasts for the arena and for behind.
  - **First hit:** F0 or F1 in every layout that has beasts.
  - **Test 5:** without crows and without filling the pool, both discs are off. With crows, both discs are sky discs on the crows at (±19; −17). With the pool filled, serials 17 and 36 are touched at F1, as the test expects.
  - **Test 6:** the crows sit 3.54 m and 4.49 m off the samples and are hit at exactly F30.
  - **Tests 8 and 9:** mirroring the two-gates layout and rotating the arena give exact samples (0 u) and identical hits.
  - **Synthetic stage:** `createWorld` accepts the 40 × 40 m stage (80 × 80 cells).
  - **Speed:** a warmed geometry build with 60 beasts takes about 0.15 ms, and a tick of one cast about 17 µs.
- **Test 9 and −0.** Rotating with (x, z) → (−z, x) gives −0 where z = 0, and vitest's `toEqual` treats −0 and 0 as different. The test should write `-z + 0`, as the existing mirror test does. Likewise, for F = (1000, 0), R = (−F.z, F.x) gives rx = −0, so add `+ 0` there.
- **Lab coverage.** Section C should say where the lab gets the F0 positions for `coverageStatic`. Capture them right after the `stepWorld()` call in `cast()`, which runs F0, rather than at t ≥ 1.
- **E.4 grep.** `grep heartDistance` would also match a comment. The pseudo-code comment `// thay heartDistance` in B.8 must not be copied into the code.
- **Step 2 (scope of ticket 2).** The copy of `tmp/skill-reach/` into the worktree is lost if the worktree is created again for ticket 2 after ticket 1 is merged. State whether ticket 2 reuses the same worktree.

### Lượt 3, S3 (phiếu 1)

VERDICT: PASS

Optional:
1. **C, lab coverage timing.** The lab is told to record the "F0 positions" right after `stepWorld()` runs F0 in `cast()`. In the lab, `emitCast` settles the cast before that step: `cast.ts:102` calls `tryResolve`. `world.ts:129-131` then moves the beasts in `stepBeasts` before `stepSkills`. So the recorded positions are one tick later than the snapshot the sim built on, off by up to about 4.5 cm. If the cast was held, they are from the wrong tick altogether. Better wording: record the positions of `cast.snapshot`'s pairs right after `emitCast` returns, and only if the cast resolved. This affects the lab readout only.
2. **G, owner video.** Under `review-folder` and the AGENTS.md capture rules, a video sent to the owner also belongs in `owner-review/<yyyy-mm-dd>/tu-tien/twin-pearl-fieldwide/` (a hard link is enough). The new topic folder needs an `ABOUT.md`, and the index should be rebuilt with `node scripts/review-index.mjs`. While the owner is away from the Mac, it goes to him as an MP4 under 30 MB. §9.8 step 4 already says "theo `review-folder`"; G could say the same.
3. **D, kept damage tests.** Several kept damage tests place beasts by the old lane geometry, so they cannot stay as they are:
   - the half lotus at (0; −15.25): that beast now becomes an anchor and sits on the petal;
   - "the east keeps its whole budget" for a crowd on lane A: the new split puts half that crowd on side 1;
   - the hit ticks F51/F21.

   "Giữ, sửa cho khung mới" already covers this. Naming these tests would save the coder a round.
4. **Evidence for the PASS.** I wrote an integer port of B.4–B.8 exactly as ticket 1 words it and ran it on the game's real `makeWorld`, `spawnBeast` and `damageBeast` (`/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticS3/port.ts`, `layouts.ts`, `symm.ts`, `t6.ts`, `t24.ts`, `perf.ts`). Origin was (0; 3), quality "ok", default budget. Every threshold the tests set is met:

   | Check | Result | Test bar |
   |---|---|---|
   | §9.7 table (sides, P, node lengths, head speeds, in-reach counts, all eight layouts) | identical | — |
   | Two gates P | (−0.02; −5.91) | within 0.15 m |
   | Two gates node lengths / end arcs | 45.1/43.9 m, 50.3/49.2 m | ±1 m |
   | Static coverage: two gates, one gate, three gates | 100 % | ≥ 95 / 85 / 95 % |
   | Static coverage: arena | 79.5 % | ≥ 75 % |
   | Static coverage: behind | 90 % | ≥ 85 % |
   | First positive hit, every layout | F0 or F1 | F0 or F1 |
   | Empty field P | (0; −9) | (0; −9) |
   | Clamp case (origin (0; −3)) | F = (0; 1000), P = (0; 6 m) | same |
   | Ten beasts round (−15; −16) | \|P − H\| = 720 000 u | 12 m ± 2 u |
   | 304 m zigzag in a 60 × 60 m frame | step 1.19 m, 265 samples | ≤ 269 (257 + 12 segments) |
   | `splitLong` on 40 m | 20 m + 20 m | ≤ 32 m each |
   | Mirror (test 8) and rotation (test 9) | hits, nodes, samples and `pass` identical | tolerance 0 |
   | Test 5: discs without crows | both off | `disc[s].on === 0` |
   | Test 5: discs with crows | sky discs, crows hit at F1 from the sky budget | same |
   | Test 5: full budget | each side's nearest beast outside the F0 disc touched at F1 | same |
   | Test 6: crows | first hit at F30 in every dense layout | F30 |
   | Speed after warm-up (60 beasts, two overlapping casts) | build about 0.1 ms, about 15 µs per tick per cast | — |

   The setup steps, `beastByRef` being already exported, the E.1 commands matching the ticket 255 report, the free `L` key, `world.field.blocked`, the 16 384-cell limit and tsconfig not reaching `tmp/` all check out against the source.

### Lượt 3, S4 (phiếu 1)

VERDICT: PASS

Ticket 1 (§9.12 header through E, plus the parts of G that concern it) matches §9.2–§9.6 and can be run as written. I checked it four ways:

- **Integer port of B.4–B.6 as written.** The port is `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticS4/port.ts`, run by `run.ts` and `sym.ts` in the same folder; output is in `run.out`.
  - **Test 2:** on the two-gate layout, P comes out at (−0.02; −5.91).
  - **Test 3:** each dragon has 3 anchors and 5 nodes. Node lengths are 45.10 / 43.88 m and final arcs 50.34 / 49.24 m. The farthest beast on each side is a node.
  - **§9.7 table:** every node length and every "Trong tầm" figure matches.
  - **Test 7 coverage:** two-gate, three-gate and one-gate layouts all reach 100 %; behind the player is 90 % (bar 85 %); arena is 79.5 % (bar 75 %).
  - **Test 4:** every route stays at 257 samples plus segments or fewer.
  - **First hit:** every layout with beasts gets its first positive hit at F0 or F1.
- **Tests 5, 8 and 9 from the real game code.** The touch budget at quality "ok" is 33 HP, and the first touch hit is also 33. Each side has 2 beasts inside the F0 disc on the two-gate layout. So the touch budget is spent at F0 on both sides, and test 5 behaves as claimed:
  - without the two crows: both F1 discs are off;
  - with the crows: each side's F1 disc is a sky disc on its own crow.
  - The mirror and 90° rotation give 0 u difference in samples and `pass` with the new symmetric rounding in `sPath`.
- **Run checks.** `createWorld` works on the synthetic 40 × 40 m stage (80 × 80 cells, under the 16,384 limit). `castOf` does take an origin, and `at`, `beastByRef` and `heartPoint` all exist. `resolveCast` does not enforce the cooldown, so two overlapping casts work in tests 11 and 12. tsc does not cover `tmp/`, and vitest only includes `tests/**`.
- **Command forms and limits.** The E.1 commands are the same forms ticket 255 ran successfully. The `mulDiv` limit (about 35.4 m per segment) and the 64 × 63.5 m field limit are stated correctly. Nothing the ticket needs is on its own forbid list, and nothing changes with the flag off.

Optional:
1. **§C, lab coverage number, when to compute.** "Tính một lần khi lần tung tới t ≥ 1" can fire right after the F0 step, before `pickDiscs` has run at t = 1, so the F1 discs would be left out. Say: compute after the `stepWorld()` that ran t = 1, that is when `world.tick − startTick ≥ 2`.
2. **§C, which positions to record.** Positions read "ngay sau stepWorld() chạy F0" have already moved one tick. Recording them right after `emitCast()`, from the record's `snapshot` pairs, matches §9.2's "trước đòn F0" exactly. The difference is a few centimetres, so this is cosmetic.
3. **§B.4.6, `sampleRoute` field type.** The type of its `field` argument is not stated, and test 4 passes a 60 × 60 m frame. Naming it would avoid guesswork, for example `Pick<FieldDef, "minXMm" | "maxXMm" | "minZMm" | "maxZMm">`. It would also help to say that `nodes` (a flat array) is turned into `PointU[]` before it goes to `sPath`.
4. **Setup step 1, `node_modules` symlink.** In the worktree the symlink shows as untracked (`?? node_modules`), as ticket 255 noted, because the `node_modules/` ignore pattern does not match a symlink. Add a line to G so Claude does not commit it when merging.

### Lượt 4a, T1 (phiếu 2 và quyết định của anh)

VERDICT: FAIL

1. **G (and setup step 2): the updated bot never gets back to the main tree, so the main tree's bot breaks after the merge.**
   - What is wrong: setup step 2 copies `tmp/skill-reach/` one way only, from the main tree into the worktree. Ticket 2 then fixes the scripts and writes `key2-fieldwide/` in the worktree only. Once ticket 1 is merged, the main tree's `bot.ts` still imports the old `key2-measure.ts`, which imports names that B.1 removes. Every bot run from the main tree then fails at import, SKILL_REACH runs included. §8.10 tells people to reproduce from `games/immortality-cultivation`, so §9.13 could not be reproduced either. G has no step that copies the work back before the worktree is removed.
   - Evidence: `tmp/skill-reach/bot.ts:10` imports `./key2-measure` unconditionally. `key2-measure.ts:12` imports `inHold, inTouch, twinPearlGeometry`, all removed by B.1 (section9.md:276). Setup step 2 is at section9.md:235. G is section9.md:487–494.
   - Fix: add to G: "After reviewing ticket 2, copy the worktree's `tmp/skill-reach/{key2-measure.ts,key2-numbers.ts,key2-aggregate.ts,key2-matrix.sh,key2-layouts.ts,<the golden compare script>}` and `key2-fieldwide/` back to `games/immortality-cultivation/tmp/skill-reach/`. First check that the main copy has not changed since step 2. Then re-run one match from the main tree (`w45a97@twin-pearl 1 1`) before removing the worktree. §9.13 records the reproduce commands from the main tree."

2. **§9.12 header "Được ghi" and the `run.sh` override: ticket 2 is allowed to write `src/` and `tests/`.**
   - What is wrong: ticket 2's brief is the §9.12 header plus F (step 4). Only the `tmp/skill-reach/**` entry is scoped ("chỉ phiếu 2"). That asymmetry means the other entries (`src/sim/twin-pearl.ts`, `combat.ts`, `src/content/data/twin-pearl.ts`, the test file, the lab files, the build folder) also apply to ticket 2. The override note then lifts `run.sh`'s ban on editing `src` and `tests` "cho các file ở danh sách Được ghi". So ticket 2 may legally change the sim that Claude has already reviewed and merged. F.6 only forbids changing the numbers or the §9 rules.
   - Evidence: section9.md:239–248 and 231. F.6 is at section9.md:485.
   - Fix: mark the six src/tests/lab/build entries "(chỉ phiếu 1)". Add to F: "Phiếu 2 chỉ ghi `tmp/skill-reach/**`; không sửa `src/`, `tests/`. Nếu cần đổi sim, dừng và ghi vào báo cáo."

3. **F.3 and F.5 drop two measures §9.8 requires: "Tầm xa" and "Phần theo loại đòn".**
   - What is wrong: §9.8 asks for the median farthest hit to H on each side plus the share of beasts beyond 12 m that were hit ("so với §8.2"), and for the parts table ("như §8.3"). F.1 records the per-side reach, but F.3 never aggregates it; it only says "đọc các trường mới". F.5 asks only for "bảng như §8.4–8.6", which leaves out both the §8.2 table and the §8.3 table.
   - Evidence: section9.md:166–167 against 451–456 and 484.
   - Fix: add to F.3: "trung vị đòn xa nhất tới H mỗi bên, phần thú đất > 12 m lúc tung bị trúng, phần theo loại đòn (hold/touch/corridor/sky/lotusFull/lotusHalf: % sát thương, đòn và hạ mỗi lần tung), cho nhóm 35–45". Change F.5 to "bảng như §8.2–8.6 với cột 'hai hành lang' để so".

4. **F.1 "tầm xa (đòn xa nhất tới H) mỗi bên" does not say ground only, so the number is not comparable with §8.2.**
   - What is wrong: §8.2 and §8.1 define this measure on ground beasts. The new sky sweep hits crows at their F0 anchors, and crows enter at (∓20; −18), about 26.9 m from H. Counting sky hits would pull the median towards crow distances.
   - Evidence: DRAGON_SKILL.md:339 ("…lên thú đất mỗi bên"). The old ground-only behaviour is in `key2-measure.ts:155–158`. The sky entries are in `rules.ts:285–287`, and the sky sweep to F0 anchors is at section9.md:108.
   - Fix: change it to "đòn hiệu dụng xa nhất lên thú ở dải đất (≤ 1,5 m) tới H, mỗi bên (bên theo `cast.book[].side`), như §8.1".

5. **Check 4 and F.3 ("đòn dương đầu tiên muộn hơn F2 trong trận thật") are ambiguous in their result.**
   - What is wrong: "lần tung có thú hợp lệ" has no operational definition. It is not said whether casts with no positive hit at all (`firstHit = −1`, for example a lone 1-HP swarm beast or the Vương at his cap, §9.5) count as late or are left out. Check 3 names 2.5 W but check 4 names no variant, so it is unclear which budget levels the 0.1 % applies to.
   - Evidence: section9.md:456, 483 and 114.
   - Fix: "Biến thể `twin-pearl` (2,5 W), mọi lần tung của trận thật. Muộn = `firstHit > 2`. Lần không trúng (`firstHit = −1`) đếm và liệt kê riêng kèm lý do (trần cụm, Vương chạm trần, ngân sách), không gộp vào tỉ lệ < 0,1 %."

6. **Ticket 2's brief (setup step 4 = header + F) points to parts of ticket 1 it does not contain.**
   - What is wrong: F.1 says "tên nào đã bỏ ở B.1" and F.4 says "đấu trường trên sân tổng hợp của D". Both B.1 and D sit in ticket 1's text, and the brief's first line points Codex only at §9.0–§9.11. The arena needs D's exact stage. On today's field (z from −18 to 8 m), `spawnBeast` clamps the arena's points at z = +11, +14 and +17, and the crow at (0; 15), down to z = 8. That silently changes the layout, and check 2 compares it with §9.7's 35/44.
   - Evidence: section9.md:237, 449, 457 and 431. `rules.ts:282–283`, `spawn.ts:148`.
   - Fix: write D's stage literal into F.4 (`{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }`, and the flag-on world as `twinWorld` in `tests/sim/twin-pearl.test.ts`). Write B.1's list of removed names into F.1. Alternatively, put B.1, B.3, B.6 and D's stage line into ticket 2's brief in step 4.

Optional:
- Check 1: write "ở mọi tầng (cả `waves[]`)". A comparison of top-level keys only fails on the nested `lanePeak*` keys. A recursive check that skips keys only in `golden-now` gives 36/36 on today's `key2-review/golden-now`; I checked this with a throwaway script.
- Aggregate command: redirect stdout to `tmp/skill-reach/key2-fieldwide/aggregate.txt`, as `key2-fix` has.
- F.1: name the fields to record outright: ground and sky counts in the snapshot, and crows per side (F.3 needs them). Define the combined `coverageStatic` denominator as all snapshot beasts, mid-band beasts (1.5–2.5 m) included, as §9.8 says.
- F.4: print P, and define head speed as the last arc divided by (`heads.toTick − heads.fromTick`)/60 s.
- Before running ticket 2, bring the worktree branch up to the merged main (`git -C … merge --ff-only main`).

### Lượt 4a, T2

VERDICT: FAIL

1. **Where:** §9 intro (section9.md line 4).
   - **What is wrong:** It says the grey box's damage rules "(§8.6, `hit()`, ngân sách) giữ nguyên". §8.6 sets the budget at 2.5 W per side. That contradicts the owner's 2.0 W decision recorded in §9.0 item 7, §9.6, §9.11 and §9.12 A.
   - **Evidence:**
     - DRAGON_SKILL.md:473 says "Mỗi bên … có 2,5 W cho thú đất…".
     - section9.md:14, 126 and 265 set 200 / 2,0 W.
   - **Exact fix:** Replace the clause with "luật sát thương của hộp xám (§8.6, `hit()`, cách chia và tiêu ngân sách) giữ nguyên; riêng mức ngân sách nay là 2,0 W mỗi bên cộng 0,8 W trời (§9.0 mục 7, §9.11)".

2. **Where:** §9.12 G (section9.md line 516).
   - **What is wrong:** "Hỏi anh câu §9.11 với số mới." is left over from before the owner decided. §9.11 is now "Quyết định của anh": "anh chốt cả ba" (line 220). Its only open item is the head-speed look at the lab video (line 232). As written, Claude would ask the owner again about something he has already decided.
   - **Evidence:** In section9-before-owner.md, §9.11 was "Câu hỏi cho anh". This G line was not changed when §9.11 became the decisions.
   - **Exact fix:** Replace it with "Báo anh số đo mới so với đích anh đã duyệt ở §9.11 (ô 2/cả trận ở bot Chuẩn ≤ 45 % với 2,0 W mỗi bên), gửi kèm video lab để anh xem tốc đầu rồng (§9.11, 'Anh xem khi có video lab'); chỉ hỏi anh nếu một đích của F trượt."

Optional:
- **G copy-back list.** Copy back every file under `tmp/skill-reach/` that differs from the main tree, excluding output folders (`diff -rq`), instead of a fixed list. `key2-dense.ts` and `bot.ts` may also be touched, for example their usage comments, which still mention `+narrow`.
- **G "chưa đổi kể từ bước chuẩn bị 2".** Name the method. The copy in the worktree has mtimes of 19:52, so any main-tree script newer than the copy, or `diff -rq` on the files ticket 2 did not touch, shows a change.
- **F.1 "gọi staticCoverage một lần, tách đất và trời".** B.6 returns one count. Say "call it once per cast for the ground points and once for the sky points; the shared figure is their sum over all snapshot beasts".
- **Check 3 "đòn đầu F0 hoặc F1".** Say whether a cast with `firstHit = −1` in the 35–45 group is a fail or is listed apart, as check 4 does for real matches.
- **Ticket 2's first line.** It points only to §9.0–§9.11, but F cites §8.1–§8.6 for definitions and table layout. Add "và §8".
- **Script defaults.** The default VARIANTS in `key2-matrix.sh` still list `twin-pearl+narrow`. After F.2, a run without arguments throws "unknown key-2 number variant". Update the default.
- **Header reason for not using `.wt-immortality-cultivation-codex`.** It is out of date. Ticket 258 was reviewed and merged at 19:19 (`ceb51c2`), and that worktree is now on `codex/jade-ring-material` for ticket 259. The conclusion still holds.

### Lượt 4a, T3

VERDICT: FAIL

1. **Where:** §9.12 D (the damage-rule tests it keeps), §9.12 A, and §9.6. This is consistency question (b): the 2.0 W change.
   **What is wrong:** moving the budget to 2.0 W breaks test expectations that D keeps "as is, fixed for the new frames", and §9.12 does not say how to change them. With `pool.sideW100 = 200` each side's part budgets are smaller than the first beast's nominal hit of that kind. So the first beast on a side never gets its full 15/45/40 % of 2.5 W any more. A lone beast now takes at most 2.0 W, 80 % of today's key 2. §8.6 described the 2.5 W setting as giving a lone beast today's full key-2 damage; §9.6 marks the shares "Không đổi" without this consequence.
   **Evidence:** I ran `wHpOf` read-only on the fixture world, Tâm nhãn off.
   - At 250 the side budget is 225 HP and the parts are [34, 101, 72, 90]. At 200 the side budget is 180 HP and the parts are [27, 81, 72, 72]. A lone beast's nominal hits are [34, 101, 90].
   - `tests/sim/twin-pearl.test.ts:224-235` (the shares test, "of today's 2.5 W"): it expects [34, 101, 90]. At 2.0 W it gets [27, 81, 72], so it fails.
   - `:476-481`: the title says "each side gets 2.5 W" and the test pins `[34, 101, 72, 90]`. That becomes `[27, 81, 72, 72]`.
   - `:400-402`: the comment "34 HP, 135 HP, 225 HP" becomes 27, 108, 180. The posture values [57, 47, 38] still pass.
   - `src/content/data/twin-pearl.ts:62-69`: the pool JSDoc says "each side carries today's key-2 damage on its first beast (2.5 W)". A only asks to fix the file's header comment.
   **Exact fix:**
   - In D's keep list, add: "the shares test pumps the budget (`cast.pool.fill(10 ** 9)` right after resolve) so 15/45/40 % of today's 2.5 W land as is. Add a lone-beast case without pumping that expects [27, 81, 72] at 2.0 W. The budget test's title says 2.0 W and it pins [27, 81, 72, 72]. Update the HP comment in the Thế test to 27/108/180."
   - In A, add: "rewrite the `pool` JSDoc for 2.0 W per side (owner, 04/11). A lone beast per side takes at most 2.0 W."
   - In §9.6, row "Ngân sách mỗi bên", add: "mỗi phần (0,3 / 0,9 / 0,8 W) nhỏ hơn đòn đầu cùng loại (0,375 / 1,125 / 1,0 W), nên một con đơn độc mỗi bên nhận tối đa 2,0 W, 80 % ô 2 hôm nay (mốc 2,5 W của §8.6 không còn)".

Optional:
- **Checked, no defect found in F (ticket 2).** It produces every measure in §9.8 with §9.8's definitions, plus the comparison columns and the owner's targets.
  - Commands: `bash tmp/skill-reach/key2-matrix.sh` changes to the game root, `KEY2_OUT` and `KEY2_ROOT` resolve, and the aggregator writes to `key2-fieldwide/numbers.json`. `key2-numbers.ts` parses `twin-pearl+pool125/175/250/375`, and `twin-pearl` with no suffix is the new 200 default.
  - The flag-off run writes 36 files named like those in `golden-before`. `golden-before` has no `key2*`, `pace` or `lanePeak*` keys, and nothing in `src` has changed since `033b3f4`.
  - Nothing is written to `key2/`, `key2-fix/` or `key2-review/`, and `key2-fix/numbers.json` has `line`, `twin-pearl` and `twin-pearl+pool200`.
  - The `node --import=tsx` form works here (tested read-only).
  - A float re-implementation of §9.3–§9.4 reproduces every §9.7 sides, pearl and node-length entry (45.1/43.9, 32.0/31.9, 59.0/55.7, 56.9/68.8, 38.0/38.3, 19.8/21.0, 17.3/26.1, 22.2), so check 2 is well-founded.
  - The ≤ 45 % / ≤ 35 % shares, the English callouts and the head direction kept out of the tickets are consistent everywhere else in §9.0–§9.12.
- Add the B.4 heading (`buildCastGeometry(world, cast)` returns the B.3 fields) and B.7's one-line role of `pickDiscs` to ticket 2's copy list. F calls the first and waits on the second, but setup step 4 copies only B.1, B.3 and B.6.
- In F step 1, say when to read the F0 positions and the per-side snapshot counts: in `start()`. In the dense scan that is right after `resolveCast`; in a match it is after the F0 tick, which gives the same positions because `stepBeasts` runs before `stepCasts`. Later, `sideFor` can overwrite `sideSlot` for a slot reused within the cast.
- Define the crow numerator as snapshot crows in the sky band with at least one positive hit. Today's `crowsHit` counts alive-before beasts whose gate is "sky".
- The aggregator's `canon.areaSkill20` still tests ≤ 20 %. Add a ≤ 45 % row (Chuẩn) so the printed canon block doesn't show a fail that isn't one.
- Have `key2-layouts.ts` print `coverageStatic` as count/total, so the ±1 comparison in check 2 is direct.
- In G, record when the step-2 copy was made (or copy without preserving mtimes); otherwise the "main file newer than the copy" rule has no reference time.

### Lượt 4b, U1 (phiếu 2 và quyết định của anh)

VERDICT: FAIL

1. **Where:** §9.12 G, second bullet (the mtime baseline for copying ticket 2's bot back to the main tree), read with §9.12 setup steps 1–2.
   **What is wrong:** The baseline is taken at the wrong moment. Step 2 copies `tmp/skill-reach/` from the main tree into the worktree during setup, before ticket 1 runs. Step 1 says ticket 2 reuses that same copy ("cây vẫn giữ bản chép tmp/skill-reach/ của bước 2"). G records the main tree's mtimes only "Trước khi giao phiếu 2", after ticket 1 has been implemented, reviewed and merged. If anyone edits `games/immortality-cultivation/tmp/skill-reach/*.ts|*.sh` between the copy and that baseline, two things go wrong. Codex edits a stale copy. Then G's rule ("file nào ở cây chính đã đổi so với mốc thì gộp bằng tay; còn lại chép về") does not see the edit, because the main-tree mtime matches the later baseline. The Codex version is copied over it and the other agent's change is lost. This is a realistic case: the bot is SKILL_REACH's measurement bot, SKILL_REACH part 2 is the next planned job (§9.11), and the window covers a whole ticket-1 cycle.
   **Evidence:** §9.12 setup steps 1–2 (section9.md:239–240) against G (section9.md:515). `tmp/` is untracked (`.gitignore:3`), so Git gives no history to recover the lost edit.
   **Exact fix:**
   - In step 2, after "Chép tmp/skill-reach/ của cây chính vào cây mới", add: "Ngay lúc chép, lưu mốc của cây chính: `ls -lT /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/skill-reach/ > <scratchpad>/skill-reach-baseline.txt` và `shasum -a 256 /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/skill-reach/*.ts /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/skill-reach/*.sh >> <scratchpad>/skill-reach-baseline.txt`."
   - In G, replace "Trước khi giao phiếu 2: lưu danh sách mtime các file trong tmp/skill-reach/ của cây chính (ls -lT) làm mốc." with: "Mốc là bản lưu ở bước chuẩn bị 2 (lúc chép), không phải lúc giao phiếu 2. Trước khi giao phiếu 2, so cây chính với mốc đó. File nào đã đổi thì chép bản mới vào `tmp/skill-reach/` của cây Codex trước khi chạy phiếu 2, rồi cập nhật mốc cho file đó."

**Checked and correct.**

Ticket 2 produces every measure in §9.8, with matching definitions:
- distinct beasts hit (median, p10–p90, share of casts in 12–20);
- `coverageStatic` (overall, ground, sky; denominator includes beasts between the two bands);
- side balance (only casts where each side has ≥ 5 beasts);
- first hit, crows, reach, share by hit type;
- BALANCE.md metrics, with the "two corridors" column from `key2-fix/numbers.json` (`line`, `twin-pearl` = 2.5 W, `twin-pearl+pool200` = 2.0 W, all present);
- the 1.25 / 1.75 / 2.0 / 2.5 / 3.75 W sweep.

The commands work as written:
- The variant names parse in `key2-numbers.ts` (`/(?:^|@)twin-pearl\+([a-z0-9]+)/`; the output folders contain no `@`).
- `key2-matrix.sh` changes into the worktree root and writes under `KEY2_OUT`.
- `key2-aggregate.ts` writes `key2-fieldwide/numbers.json`, so `key2/`, `key2-fix/` and `key2-review/` are not touched.
- The flag-off check is runnable: my comparison script with the stated rules gives 36/36 between `golden-before` and today's `key2-review/golden-now`.

I re-implemented §9.3–9.4 and B.4 in integer form. It reproduces every §9.7 row:
- sides, P and node lengths (for example 45.10 / 43.88 m and 56.89 / 68.85 m);
- in-range counts 40/40, 40/40, 42/42, 35/44, 36/40, 1/1 and 1/1;
- two-gates final arc 50.34 / 49.24 m.

So check 2 (± 1 m, ± 1 beast) is consistent and reachable. The anchor stop-threshold margins are wide.

Consistency of the owner's 19:40 decisions (b) holds throughout §9.0–§9.12:
- 2.0 W per side everywhere. The "2.5 W" in §9.6 is the per-hit P, correctly unchanged.
- Key 2 ≤ 45 % now and ≤ 35 % after SKILL_REACH part 2.
- English callouts and player-facing text.
- The dragon head (Solar Ember Regent) is recorded in §9.9 and §9.11 and kept out of the tickets.

The test changes D asks for at 2.0 W are right:
- budget parts pin [27, 81, 72, 72];
- a lone beast without the budget pumped gets [27, 81, 72];
- the Thế comment becomes 27 / 108 / 180, and the posture values 57/47/38 do not change;
- the pumped 15/45/40 test still holds;
- the boss still reaches 135 = cap (36 + 99).

Optional:
- F.1 says the F0 positions are the same in a real match "vì stepBeasts chạy trước kỹ năng". That is not exact: `boss.ts:190/202`, `pressure.ts:92/101` and `formation.ts:141` move beasts after `stepSkills` in the same tick. It only affects match-side coverage, which has no threshold, so softening the wording is enough.
- F.1 should list a per-cast count of "snapshot sky-band beasts with ≥ 1 positive hit". F.3's crow measure needs it, and the existing `crowsHit` is based on gate labels.
- F.3 should also name the new F1 sky-disc part in `key2-aggregate.ts`'s hard-coded `PARTS` list, or that part will be silently dropped from the output.
- While ticket 2 runs, the main tree's bot imports names that ticket 1 removed. A one-line warning in G would help other agents.

### Lượt 4b, U2

VERDICT: FAIL

1. **Where:** §9.12 F, item 6 ("Cast không giải"), and the matching print in F.3. This is about how ticket 2 handles casts that do not resolve.
   - **What is wrong:** the item ends "Cả hai số đếm in trong aggregate.txt", but it defines only one of the two counts: the "không giải" count of the peak scan in `key2-dense.ts`. For real matches it says only that the bot keeps the game's behaviour and that `key2-measure.ts` opens no record. It never says what to count. In the game, a key-2 Cast that does not resolve emits a `cast` event with state `held` once. Later it emits either `resolved` or `fizzled`, after 3 s.
     - Counting `held` events gives one number: it includes Casts that resolved a moment later.
     - Counting `fizzled` gives another: only Casts that never resolved.
     - So two coders following the ticket would put different numbers in `aggregate.txt`.
   - **Evidence:**
     - `section9.md:484`.
     - `src/sim/cast.ts:92-109`: `emitCast` sets `held` and emits the event once.
     - `src/sim/cast.ts:112-129`: `stepCasts` retries each tick, then emits `resolved` or `fizzled`.
     - `tmp/skill-reach/bot.ts`, `onEvent` case `"cast"`: it records only `cast:<slot>` (resolved) and `fizzle:<slot>`, never `held`.
     - `key2-measure.ts` `onEvents` reads only `cast` events with state `resolved`.
   - **Exact fix:** replace the sentence "Trong trận, bot giữ hành vi của game (Cast được giữ, không tốn hồi chiêu) và `key2-measure.ts` không mở bản ghi lần tung nào;" with:

     "Trong trận, bot giữ hành vi của game (Cast được giữ, không tốn hồi chiêu), `key2-measure.ts` không mở bản ghi lần tung nào, và mỗi trận ghi hai số: `key2Held` (số sự kiện `cast` của ô 2 có `state` "held") và `key2Fizzled` (số sự kiện `cast` của ô 2 có `state` "fizzled");"

     Then replace "Cả hai số đếm in trong aggregate.txt" with:

     "`key2-dense.ts` lưu số "không giải" vào JSON đầu ra (trường `unresolved`); `key2-aggregate.ts` in, theo từng biến thể, tổng `key2Held`, tổng `key2Fizzled` của trận thật và tổng `unresolved` của quét đỉnh trong `aggregate.txt`"

Nothing else in ticket 2 or in the consistency question is a defect:
- **What I checked in the scripts and data:**
  - The variant names `+pool125/175/250/375` parse with the regex in `key2-numbers.ts`.
  - `key2-matrix.sh` runs from the working tree, and it has exactly two `tsx` call sites to replace.
  - `key2-fix/numbers.json` holds `line`, `twin-pearl` (2.5 W) and `twin-pearl+pool200`.
  - `golden-before` has 36 JSON files with no `key2*`, `pace` or `lanePeak` keys.
  - No sim, content, app or kit file changed since `033b3f4`, the last 36/36 match.
  - `tmp/` is gitignored and `tsconfig` does not include it.
- **What I checked in the design:**
  - The §9.7 rows I recomputed match the design's own formulas.
  - The 2.0 W numbers are right everywhere in §9.0–§9.12: parts 0.3 / 0.9 / 0.8 W, test parts [27, 81, 72, 72], posture comment 27 / 108 / 180, about 15 hits from §8.6, 37–45 % share from §8.6.
  - The ≤ 45 % (Standard bot) and ≤ 35 % targets, English text, the dragon head kept out of the tickets, and the resolve condition (§9.2, B.9, F.6, §9.5) agree everywhere.

Optional:
- **Reason when `firstHit = −1`:** F.1 lists the four reasons but not how to tell them apart. A rule would make it repeatable: look at the cast's book entries that took no positive hit. A beast in a swarm cluster means "trần cụm"; the Vương means "Vương chạm trần"; otherwise, if that part's `pool` is 0, "ngân sách cạn"; otherwise "khác".
- **Keep the recorder read-only:** say explicitly that the recorder must not call `sideFor` or `pickDiscs`. Both write into the cast record.
- **Read positions so F0 kills still count:** in matches, read snapshot positions from `world.beasts.list[slot]` with a serial check. `beastByRef` returns null for beasts killed at F0, so they would drop out of the coverage numerator and the ground/sky counts.
- **Name the new part ids in English:** for example `f0Disc`, `f1Ground`, `f1Sky`, `body`, `sky`, `lotusFull`, `lotusHalf`. That follows the owner's naming rule instead of leaving it to Codex.
- **Crow target at risk:** the crow target of ≥ 90 % may miss for a built-in reason. An F1 sky disc on a crow lands at falloff 85–100 % and can spend a side's whole 0.8 W sky part, so a second crow on that side gets little or nothing. Printing crow hits by part as well (F1 sky disc vs. sky sweep) would show this directly.
- **Review folder:** the review-folder README puts agents' measurement numbers ("số đo") under `typing-game-review/captures/tu-tien/<topic>/`. G could add a link or an `ABOUT.md` for `key2-fieldwide/`, or note why bot numbers stay in `tmp/skill-reach/`.

### Lượt 4b, U3

VERDICT: PASS

I found no blocking defect in ticket 2 (§9.12 F, with the header and G where they concern it) or in the consistency question (b).

**1. Every §9.8 measure is produced.**
- Ticket 2 covers: distinct beasts hit (median, p10–p90, share of casts in 12–20), coverageStatic (total, ground, sky), side balance, first hit, crows, reach, per-part damage, BALANCE.md, and the 1.25–3.75 W budget sweep.
- Performance is the one exception: ticket 1 measures it (test 12, E.2), and the bot plan in §9.8 does not ask the bot for it.
- The comparison columns map correctly onto `key2-fix/numbers.json`. I checked that file: `twin-pearl` is the two-corridor 2.5 W version (standard bot key 2 share 45.7 %), `twin-pearl+pool200` is two-corridor 2.0 W (40.7 %), and `line` is today's key 2 (19.9 %).

**2. The instructions are executable as written.**
- Exactly two `node_modules/.bin/tsx` calls exist in `key2-matrix.sh`; the `node --import=tsx` form is the one reports 195 and 223 used.
- `key2-numbers.ts` parses `twin-pearl+pool125/175/250/375` from the bot profile (`…@twin-pearl+pool125`) and from the dense scan's variant argument. The output folder paths never match its pattern.
- `KEY2_OUT` and `KEY2_ROOT` keep every new result in `key2-fieldwide/`. Nothing writes to `key2/`, `key2-fix/` or `key2-review/`.
- The `+narrow` variant does write the removed fields, as the ticket says.
- `golden-before` holds exactly 36 JSON files for the 9 profiles in the ticket's loop, and has no `key2*` keys. Since `1a78a82`, the only commits touching the simulation are the twin-pearl ones, so 36/36 is reachable.
- The game emits `cast` events with state `held` (when a cast is kept) and `fizzled` (after 3 s). `hit` events are only emitted for positive damage.
- `beastByRef` does return null for a beast killed at F0, so the instruction to read `world.beasts.list[slot]` with a serial check is right. Slots are freed at the end of the tick, so a reused slot cannot reach `start()`.
- `combat-fixture.ts` does not import vitest, so `key2-layouts.ts` can use it.
- Ticket 1 is already merged into main (`35f1b77`). I ran a throwaway copy of `key2-layouts` against that code: every number in the §9.7 table matches — the two sides, P, path lengths, head speeds, and in-range counts 40/40, 40/40, 42/42, 35/44, 36/40, 1/1, 1/1, plus the empty field (22.2 m wings, no resolve). Check 2 is reachable.

**3. The thresholds are unambiguous** and match §9.8 and §9.11: 12–20 with at least 70 %, coverage median at least 75 %, F0/F1 first hit, crows at least 90 %, balance in at least 85 % of casts, late first hits under 0.1 %, and standard-bot key 2 share at most 45 %.

**4. Nothing in ticket 2 relies on something ticket 1 does not provide.** `buildCastGeometry`, `staticCoverage`, `lotusRegion(cast, …)`, `inGroundBand`, `inSkyBand`, the `book[].side` and `kinds` fields, `snapshot`, `sideSlot`, `sideSerial`, `disc` and `dragons[].nodes/arc` all exist in the merged code.

**5. Consistency (b) holds.**
- 2.0 W per side appears consistently in the intro, §9.0.7, §9.6, §9.7, §9.8, §9.11, A, D, F and G. The "2,5 W" in the §9.6 "Loại và phần" row is the per-hit base (key 2's own 2.5 W), not the budget, so it is correct.
- The per-part arithmetic is right: 0.3 + 0.9 + 0.8 = 2.0 W, giving the pins [27, 81, 72, 72] and 27 / 108 / 180.
- The ≤ 45 % now, ≤ 35 % after SKILL_REACH part 2, then a 20 % trial, English callouts, and the dragon head direction staying out of the tickets are all consistent.
- The resolve condition matches across §9.2, B.9 and F.6, and §9.11's quoted numbers match §8.4 and §8.6.

Optional:
1. **Step 4, first line of ticket 2:** ticket 2's excerpts leave out the §9.8 layout definitions and the §9.7 table, which F.4 and check 2 need. DRAGON_SKILL.md does not contain §9 yet, and ticket 271 was given a snapshot (`docs/codex-queue/271/section9-design.md`). If §9 is still not in the file when ticket 2 is written, point the line to a snapshot the same way.
2. **F.1, the cause of the match position offset:** the offset comes mainly from `stepBeasts`, which runs between the key command (when the snapshot is taken) and the F0 skill step. The parenthetical's cause is slightly off; the effect and the no-threshold conclusion stand.
3. **Casts that end before t = 1:** if victory or defeat stops a cast before then, `pickDiscs` never runs. Record coverage as null and leave those casts out of the medians.
4. **`key2-layouts.ts` details:** step at least 103 ticks (the test uses 2 + 110). Spawn crows with gate "sky", because `spawnBeast` sets y = 4 m from the gate, not from the species.
5. **"Lệnh" block:** add the run line for the flag-off compare script.
6. **Lab video (G):** also hard-link it into `owner-review/<date>/tu-tien/twin-pearl-fieldwide/` and rerun `scripts/review-index.mjs`, as AGENTS.md requires.

My throwaway script is `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticU3/layouts.mts`. It reads the game files and writes nothing.

### Lượt 4b, U4

VERDICT: PASS

I found no blocking defect in ticket 2 (F, the §9.12 header parts it relies on, and G as it concerns ticket 2), and none in the consistency of the owner's 19:40 decisions across §9.0–§9.12.

**Ticket 2 against the code and the bot**
1. **Removed names.** Every name F.1 removes is gone from the merged `src/sim/twin-pearl.ts`. Every name ticket 2 uses exists: `buildCastGeometry`, `staticCoverage`, `lotusRegion(cast, …)`, `inGroundBand`/`inSkyBand`, `createTwinPearlState`, and the fields `snapshot`, `sideSlot`, `sideSerial`, `book[].side`/`kinds`, `disc`, `dragons[].nodes`/`arc`, `baseHp`, `startTick`, `pool`.
2. **Bot scripts.** `key2-measure.ts` still imports `inHold`, `inTouch` and `twinPearlGeometry`, so G's warning that the main tree's bot cannot run is correct. `key2-matrix.sh` has exactly two `node_modules/.bin/tsx` calls. `+narrow` is mentioned in `bot.ts` and `key2-dense.ts`. `PARTS` is fixed in `key2-aggregate.ts`. The variant names `twin-pearl+pool125/175/250/375` parse in `key2-numbers.ts` for both match ids and dense arguments; output folder paths do not match its pattern.
3. **Unresolved casts (F.6).** The game emits `cast` events with state `held` and `fizzled`, and the recorder opens a record only on `resolved`. So unresolved casts never enter the per-cast denominators. In the dense scan the cast is resolved before any step, so F0 is stepped (t = 0).
4. **Hit events are always positive.** `damageBeast` emits `hit` only when d > 0, so the victims and `firstHit` count positive hits only.
5. **Part classification is complete.** The rule (tick, height band, kind just added to `book`) covers every case. A beast's height changes only in `stepBeasts`, before `stepSkills`, so the band read after the tick is the band at hit time.
6. **Reading F0 positions from `list[slot]` with a serial check is right.** A beast killed at F0 keeps its object until the slot is reused.
7. **Comparison sources.**
   - `key2-fix/numbers.json` holds `line`, `twin-pearl` (two corridors at 2.5 W) and `twin-pearl+pool200`.
   - The golden-before folder has 36 JSON files, and its keys match what check 1 compares.
   - Nothing in src/sim, app or content changed since §8's review head except ticket 1.
   - Every output path writes only under `key2-fieldwide/`; no command writes to `key2/`, `key2-fix/` or `key2-review/`.
8. **Layouts.** I rebuilt the eight layouts on the merged sim with a throwaway script in my scratch folder. Pearl positions, node lengths, final arcs, head speeds and `staticCoverage` all match the §9.7 table exactly, so check 2 can pass.
   - Two gates: 45.1 / 43.9 m, 67 / 66 m/s, 40/40.
   - Arena: 56.9 / 68.8 m, 85 / 103 m/s, 35/44.
   - Behind the player: 36/40.
   - Empty field: 22.2 m.

**Owner's decisions and the resolve condition (b)**
- **2.0 W per side.** It is consistent everywhere it appears: intro, §9.0 item 7, §9.6, §9.8, §9.10, §9.11, A, D, F and G.
  - The 0.3 / 0.9 / 0.8 W parts and the test pins [27, 81, 72, 72] and 27 / 108 / 180 are right.
  - The figures quoted from §8.6 are right: about 15 beasts hit at 2.0 W, key 2 at 37–45 % of all damage, bots Mới → Nhanh winning 45–100 %.
  - "2,5 W" in §9.6 refers to the hit's base damage, not the budget, so it is correct.
- **Key-2 share.** It reads ≤ 45 % now and ≤ 35 % after SKILL_REACH part 2 everywhere (§9.0, §9.8, §9.11, F.3, F check 5, G).
- **English text, dragon head and resolve condition.** English callouts and player-facing text, and the dragon head direction (recorded but kept out of the tickets), are consistent. So is the resolve condition in §9.2, B.9, §9.5 and F.6.

Optional:
1. D's line "chỉ giải khi có thú nhận được sát thương" is the pre-271c wording, and so is the merged test title "only damage-immune beasts keep a cast held". They do not contradict §9.2, but are incomplete. Suggested D wording: "chỉ giải khi có thú sống, không miễn, ở dải đất hoặc trời (§9.2, B.9)".
2. F.6's parenthetical leaves out "sống, không miễn" from the §9.2 condition. Change it to "§9.2: không có thú sống, không miễn sát thương, ở dải đất hay dải trời".
3. F.3 should say that `coverageStatic` per group is printed as a median (plus p10–p90), because check 3 tests the median.
4. The reason F.1 gives for position drift in matches is incomplete. A typed cast snapshots in `applyCommand` at the start of tick F0, so `stepBeasts` of that tick also moves beasts before `start()` reads them. The conclusion (a few cm, no threshold) still holds.
5. The aggregator does not print §9.8's "side counts differ by ≤ 1" (true by construction). Adding a max |n0 − n1| line would close it.
6. F.1 hardcodes the ticks for the parts (0, 1–2, 30). Reading them from `TWIN_PEARL` would keep the bot right if the owner slows the frames (§9.11).
7. F.2 does not say what the new default variant list in `key2-matrix.sh` should be. It is harmless, because the commands pass the variants explicitly.
8. AGENTS.md lists numbers among working captures for `captures/<game>/`. G's `ABOUT.md` pointer to `tmp/skill-reach/key2-fieldwide/` covers this. Adding one line on why (the sandbox only writes inside the work tree, and the §8 comparison sources live there) would pre-empt the question.

My throwaway script is `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/0cd1bde2-f9f3-4880-8237-1e76082aeff4/scratchpad/dragon-fieldwide/criticU4/layouts.mts`.

## Bảng kiểm

Các ý then chốt của §9 và nơi chúng được kiểm. "Cổng số nguyên" là bản viết lại bằng số nguyên của từng giám khảo, chạy trên chính `fixed.ts` (và, từ S3, trên mã thật của game), ngoài Git.

| Ý | Nguồn kiểm | Kết quả | Ghi chú |
|---|---|---|---|
| Bảng §9.7: bên, ngọc, độ dài đường nút, cung cuối, tốc đầu rồng, số thú trong tầm ở tám bố cục | Cổng số nguyên của A1, A2, A3, B1, S1–S4, U1, U3, U4; U3 và U4 chạy trên main `35f1b77` sau phiếu 271 | Đúng | A1 sửa cột "trong tầm" (35/44, 36/40, 40/40) vì nguyên mẫu đặt sóng S dương ở mỗi đoạn |
| `mulDiv` trong `sPath` đúng khi đoạn ≤ khoảng 35,4 m (2001·len² < 2^53) | `src/sim/fixed.ts:31`; critic 1, A1, A2, A3 | Đúng | Chia đoạn ở 32 m |
| Ảnh gương và xoay 90° trùng tới 0 u khi `sPath` làm tròn đối xứng theo dấu của tích | critic 1 (phát hiện 8/93 mẫu lệch 1 u với cách cũ), critic 2, S1–S4 | Đúng | Sửa ở B.4 bước 6 |
| Đòn dương đầu tiên ở F0 hoặc F1 khi có thú hợp lệ ở F0 | critic 2, A2, A3, S3, S4; phiếu 272: 0 trên 13 315 lần trễ hơn F2 | Đúng | Trừ ca trần cụm làm tròn về 0 (đã ghi) |
| Quạ trôi tới F56: 1,87 m (2 m/s), 2,55 m (quạ Cuồng, Thử thách) | A1, A2, A3 | Đúng | Con nhộng trời r 3 m |
| Đường hộp xám cũ: 18,2 m đường thẳng, 19,9 m theo sóng S, khoảng 31 m/s | A1, A2 chạy `twinPearlGeometry` cũ | Đúng | |
| Ở 2,0 W, các phần [27, 81, 72, 72] máu nhỏ hơn đòn đầu [34, 101, 90] | T3 (`wHpOf` trên thế giới test), U1, U3, U4 | Đúng | Sửa test D và JSDoc `pool` (việc kiểm sau phiếu 271) |
| `key2-fix/numbers.json` có `line`, `twin-pearl` (2,5 W), `twin-pearl+pool200` | T3, U1–U4 | Đúng | Cột so của phiếu 272 |
| `golden-before` có 36 file JSON, không có khóa `key2*`, `pace`, `lanePeak*`; phép so đệ quy cho 36/36 | B2, T1, U1, U3, U4; phiếu 272: 36/36 | Đúng | |
| CLI `tsx` bị sandbox chặn (`listen EPERM`); dạng `TSX_DISABLE_CACHE=1 node --import=tsx` chạy được | B3 (phiếu 023, 195, 223); phiếu 272 đã chạy | Đúng | |
| Sân tổng hợp chỉ dựng được dưới 16 384 ô (khoảng 64 × 63,5 m) | B2 (`field.ts:176`), S3, S4 | Đúng | Test 4 gọi thẳng `sampleRoute` |
| Cây `games/.wt-immortality-cultivation-codex` đang bận | S2 (`git worktree list`) | Đúng | Dùng `games/.wt-ic-twin-fieldwide` |

## Góp ý không chặn còn mở (việc làm sau)

**Cho phiếu 271 (đã merge ở `35f1b77`), Claude kiểm lại:**
- Chú thích JSDoc của `pool` theo 2,0 W, và các test ngân sách ở 2,0 W (test phần 15/45/40 bơm ngân sách; ca một con đơn độc chờ [27, 81, 72]; test ngân sách ghim [27, 81, 72, 72]; chú thích máu của test Thế 27 / 108 / 180). Hai chỗ này được thêm vào §9.12 sau bản giao 271 (T3).
- Lab: ghi vị trí F0 cho `coverageStatic` ngay sau `emitCast` từ các cặp `snapshot`, và tính sau khi đã qua t = 1 (`world.tick − startTick ≥ 2`) (S3, S4).
- `sampleRoute`: nêu kiểu của tham số `field` (S4).
- Không commit liên kết `node_modules` của cây (S4).
- Video cho anh: thêm liên kết cứng ở `owner-review/<ngày>/tu-tien/twin-pearl-fieldwide/` và chạy lại `scripts/review-index.mjs` (S3, U3).

**Cho bot (phiếu 272, đã chạy):**
- Lần tung kết thúc trước t = 1 (thắng hay thua giữa chừng): phủ ghi `null`, không vào trung vị (U3; báo cáo 272 đã làm đúng như vậy).
- `key2-layouts.ts`: bước ít nhất 103 tick, quạ đổ với nhãn cổng "sky" (U3).
- Đọc các tick của từng phần đòn từ `TWIN_PEARL` thay vì viết số trần, để đổi khung (§9.11) không làm sai bot (U4).
- In thêm dòng lệch số thú hai bên lớn nhất `max |n0 − n1|` (U4).
- Lời trong D và F.6 về điều kiện giải nên ghi đủ "sống, không miễn, ở dải đất hoặc dải trời" (U4).
