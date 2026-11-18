# Đọc mã: nối bầy rồng khí vào chiêu phím 2 (05/11/2026 15:50)
**Tóm tắt (≤ 300 chữ)**
- Hai agent đọc mã game `main` (sim 271, view, asset). Toàn văn ở dưới.
- **Sim hôm nay:** phím 2 chỉ thành Song Long khi header có `swordKey2`; bản chơi không bao giờ bật. Sát thương từ F0 tới F102 (1,7 s): đĩa F0 4,5 m ở H, đĩa F1–F2, đĩa quanh thân 2 rồng theo đường S của sim (43,6 % sát thương), sky F30–F56, sen F57–F77. Không phát `skill-fx` nào; view chỉ có `cast` và `hit`. Cân bằng 272 trượt: cân hai bên 75 % (≥ 85 %), phím 2 chiếm 45,99 % (trần 45 %), bot Chuẩn thắng 15 %.
- **Cần đổi:** bảng nhịp chung (thả từng con, lặn từng con, nổ ngọc) do sim giữ; sát thương toàn sân chia k vùng theo góc quanh ngọc, đánh theo nhịp, không theo đường bay; giữ đòn đầu ≤ F1; nổ ngọc giữ phần 40 %; bỏ mã cứng 2 rồng; tách khỏi dữ liệu chiêu `line`; thêm sự kiện (thả, lặn, nổ, chỉ số vùng mỗi đòn); viết lại test và chạy lại cân bằng.
- **View:** chuyển module lab thành presenter `src/view/skills/qi-dragon-swarm.ts`; đồng hồ theo tick thế giới; bay đúng giờ (tốc độ = dài / (tick lặn − tick thả)); pool 2 bầy (hồi chiêu 8 s); tầng chất lượng (Medium là mặc định trên Apple, Low không 3D: cần bản 2D); 10 mesh xương vượt trần 6/8; texture 4096 quá ngân sách; giảm chuyển động; prewarm trong `newMatch`; asset qua script prepare + manifest + `pnpm media:push`; âm cue lại theo nhịp mới.
- **Quyết định cần chốt:** thời lượng chiêu và bảng nhịp; đồng hồ (tick thế giới vs thời gian thật); số rồng (5); bật `swordKey2` cho bản chơi (đổi rulesHash, cần anh duyệt).

## Toàn văn: sim
```json
{
 "summary": "Key 2 only becomes Twin Dragons when a replay header carries swordKey2: \"twin-pearl\". createSkillsState then adds world.skills.twinPearl (src/sim/skills.ts:76), and resolveCast sends slot 2 to resolveTwinPearl instead of resolveLine (skills.ts:222). The play app never sets that flag: createReplayHeader leaves it out (src/app/app.ts:153-167) and the rules hash is built without the variant (app.ts:188). So the flag only runs in the lab grey box (src/lab/twin-pearl-greybox.ts:22-26) and in the bot. The cast resolves on the tick its last letter is typed (applyCommand, then typeKey, complete and emitCast at src/sim/words.ts:881, then cast.ts tryResolve). It resolves only if a live, damageable beast sits in the ground band (up to 1.5 m) or the sky band (2.5–6 m) (twin-pearl.ts:487); otherwise the cast is held and retried every tick for up to 3 s. On resolve it takes an integer F0 snapshot and builds the cast geometry. Two axes run from the caster C to the heart H. Beasts are split into two equal sides on the lateral axis (cut2). The pearl P sits 3/5 of the way from H to the ground centroid, capped at 12 m and kept 2 m inside the field. Each side gets up to 3 farthest-first ground anchors and one S-wave path C→anchors→P sampled at least every 0.5 m, plus sky anchors (twin-pearl.ts:252-333). From that same tick, stepTwinPearl (run inside stepSkills, after strikes and zones; skills.ts:436) tests live beast positions each tick against these volumes: a 4.5 m disc at H on F0; two 2.2 m discs on F1–F2; 1.4 m discs around each dragon's sampled body, live from its pass tick until 54 ticks later (heads F3–F48); 3 m sky capsules on F30–F56; and the lotus at P on F57–F77. Damage ends at F102 (TWIN_PEARL_END_TICK). Each beast takes at most 3 hits per cast, one per kind (touch, corridor, lotus; 15/45/40 % shares of 2.5 W), at least 20 ticks apart. Each side has its own falloff (100 %, −15 % per further beast, floor 40 %) and its own budget: 2.0 W per side plus 0.8 W for sky hits, scaled by grade and the damage bonus. The whole cast is one area hit for the 60 % swarm-cluster cap, and the boss cap is 1.5 W per cast. The sim emits nothing skill-specific: no skill-fx, no pearl, no paths, no phase ticks. The view only gets the generic cast, hit, posture and death events, and the grey box reads world.skills.twinPearl.casts directly. Most of the damage is tied to the sim's own dragon paths (body 43.6 %, plus the sky capsules and the lotus petals). That is what the owner's new swarm look and his 'damage by field and beast density' rule (task file line 42) require replacing. Ticket 272 failed two targets: the two sides were balanced in only 75 % of casts (target 85 %), and key 2 took 45.99 % of all damage for the Standard bot (cap 45 %). The Standard bot won only 15 % of runs.",
 "files": [
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/content/data/twin-pearl.ts",
   "role": "Key 2 trial table (lines 14-37): F0 disc 4.5 m; F1-F2 discs 2.2 m; pearl pull 600 per mille, 12 m cap, 2 m inset, 9 m on an empty field, arrives F48; up to 3 anchors with a 3 m gap; heads F3-F48 (r 1.4 m, amplitude 0.9 m, half-wave 4 m, 0.5 m samples, at most 256, 32 m segment split); trail 54 ticks; ground band to 1.5 m; sky F30-F56 (r 3 m, 2.5-6 m); roar F49-F56 (view only); lotus F57-F77 (r 9 m, core 4 m, petals 13 m x 2.2 m, outside 500 per mille); shares 15/45/40; pool 200 + 80 (W x 100); up to 3 hits; rehit 20 ticks; boss cap 150. END_TICK = 102 (line 40)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/twin-pearl.ts",
   "role": "The whole sim of the variant: buildCastGeometry 252-333 (axes 256-261, snapshot 262-267, side split and cut2 268-279, pearl P 280-295, anchors 297-315, S path 316-331); sPath and sampleRoute 148-211; volumes 336-429; staticCoverage 432-438; falloffPm, postureOf and sideFor 443-465; twinPearlPool 468-478; resolveTwinPearl 484-511; pickDiscs 514-535; mayHit 545-550; hit 556-583; stepCast 607-661 (one hit order 600); stepTwinPearl 664-680. Two dragons are hard-coded (lines 104-105, 471-477, 502)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/skills.ts",
   "role": "Flag gate: createTwinPearlState (76); slot 2 goes to resolveTwinPearl or resolveLine (222); 8 s cooldown set on resolve (236); stepTwinPearl runs after strikes and zones (436). Today's line emits skill-fx 'line' (164); the twin variant emits none."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/cast.ts",
   "role": "Cast lifecycle: tryResolve 74-89 emits the 'cast' resolved event (86); held 103-108; retried every tick, fizzles after 3 s (112-129)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/combat.ts",
   "role": "damageBeast 173-222: scaling, falloff, cluster cap (137-161), limit, emits 'hit' (198-211); wHpOf 52-54; scaleHit 105-113; areaClusterLeft 150-156 (added in 271)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/world.ts",
   "role": "Tick order 121-145: commands (typeKey, then emitCast at F0) before stepBeasts, stepCasts, stepSkills (twin-pearl hits), then cleanup (death events)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/content/types.ts",
   "role": "SimEvent union: hit 627-640; cast 641-649; skill-fx 650-661, whose stages (654) include none for the twin or swarm variant"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/events.ts",
   "role": "Contract (lines 7-8): SimEvent is the only channel out of the sim; a lane that needs a new event writes '// WANT EVENT'"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/content/data/school-kiem.ts",
   "role": "Key 2 line data the variant borrows (60-63): 8000 ms cooldown, w100 250, falloff 15 %, floor 40 %, posture 20"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/app/app.ts",
   "role": "Play header has no swordKey2 (153-167); rulesHash is called without the variant (188); matchRulesHash adds TWIN_PEARL only for the variant (146-148)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/view/fx.ts",
   "role": "Play view event router: hit sparks and numbers (289-295); skill-fx always fires a sword volley (301-313), so new stages need a branch"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/audio/hooks.ts",
   "role": "SKILL_SOUNDS per skill-fx stage (31-38); no twin or swarm stage"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/lab/twin-pearl-greybox.ts",
   "role": "Dev-only grey box: its own world with the flag (22-26); reads world.skills.twinPearl.casts directly (250) instead of events"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tests/sim/twin-pearl.test.ts",
   "role": "37 rule and geometry tests (mirror and rotate checks at 0 u tolerance, at 444-470); flag-off world hash pinned at 1a78a82 (638-679)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tests/sim/twin-pearl-sweep.test.ts",
   "role": "Ticket 271b sweep over 200 random layouts plus the 271c band-resolve test (about 457)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm/src/lab/dragon-swarm-energy.ts",
   "role": "Approved view-only swarm: FIELD and PEARL hard-coded (28-29); FLY_S 5 s (31); FADE_S 0.9 s (35); SPEED_K (42); speed clamp(len/5, 11, 16) m/s x SPEED_K (595); end = (len+16)/speed (616); cast() 976-997 (sectors by angle around the field centre, height bands 2.6 + 0.9 i, 7 m approach point, launch delay i x 0.3 s); per-dragon sink pulses the pearl (1018-1024); burst once all dragons are done (1026-1029); burst lasts 0.7 s (433-438)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm/src/lab/skills-main.ts",
   "role": "?key2=energy dispatches key 2 to swarmE.cast with no sim (983-988); default ?dragons=6 (208)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md",
   "role": "§9: frames 706-722, volumes and budget 724-739, targets 761-776, data the view needs (798), owner decisions 824-838, sound frames (1134), results of ticket 272 (1137-1168)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/docs/work/tasks/twin-dragons.md",
   "role": "Owner direction: swarm, with damage by field and density and visuals in the view (39-43); 5 dragons in v3 (120); length 8.9 / 7.4 / 6.5 s at 1.0 / 1.3 / 1.6x speed (126); plan 1.3x, then wire into the real key 2 (129)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/272-report.md",
   "role": "Ticket 272 summary: what passed and what failed"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/tmp/skill-reach/key2-fieldwide/report.md",
   "role": "Full 272 bot report: checks (19-29), parts (50-58), side-balance failures (64-88), 20 Standard seeds (92-113), budget sweep (119-128), matrix (146-164), layouts (210-219)"
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/tmp/skill-reach/key2-fieldwide/aggregate.txt",
   "role": "Per-cast numbers; line 19 covers real matches (13317 casts)"
  }
 ],
 "events": [
  "Wind-up (while typing): 'word-progress' {seat, word, typed, result, letter} and 'word-complete' {grade, …} (types.ts:719-731). There is no key-2 charge event; the view builds the charge from these.",
  "F0 resolve: 'cast' {state:'resolved', seat, slot:2, actionId, wordId, origin (u)} at the tick of the last letter (cast.ts:69-71, 86). actionId equals TwinPearlCast.castId. This is the only release signal. It carries no P, paths, discs or phase ticks.",
  "No target: 'cast' {state:'held'} (cast.ts:107), retried every tick; 'cast' {state:'fizzled'} after CAST.heldMs 3000 ms (rules.ts:69; cast.ts:118-124). The 8 s cooldown is not spent.",
  "Hits F0–F102: one 'hit' per damaging hit {beast, amount, damageType:'typed', bucket:'typed', source:'slot2', seat, grade, tier, x, z, hpLeft} (combat.ts:198-211). Timing: F0 disc at H; F1–F2 discs; bodies from each sample's pass tick (F3–F48) plus 54 ticks; sky F30–F56; lotus F57–F77. It carries no kind, part, side or dragon index.",
  "Posture: 'posture' change or break from postureHit, with 3/9/8 Thế for touch/corridor/lotus (twin-pearl.ts:451-454, 581-582).",
  "Kills: 'death' {by:'slot2', x, z, cluster, tier} emitted in world.ts cleanup on the same tick.",
  "Missing: the variant emits no 'skill-fx' (resolveTwinPearl has no emit; the stage union at types.ts:654 has no stage for it). The play view (fx.ts) and audio (hooks.ts SKILL_SOUNDS) therefore show and play nothing for key 2 except generic hit sparks, numbers and hit sounds. The grey box gets P, nodes, samples, pass ticks, discs and sky anchors by reading world.skills.twinPearl.casts (twin-pearl-greybox.ts:250). §9.9 (DRAGON_SKILL.md:798) lists exactly this data as what the view needs from the sim.",
  "Phase ticks the view can derive today from the table (60 Hz, offsets from F0): 0 release; 1 discs; 3 heads leave; 30 sky; 48 heads reach P; 49 roar (view only); 57 lotus; 77 lotus ends; 102 last hit; view to F300 (§9.5). In the swarm lab, the dive and burst come seconds later (see risks)."
 ],
 "damageModel": "Hit selection today depends on paths and is fixed at F0, though built only from the field bounds, H, C and the F0 snapshot (no gates or lanes). (1) Touch: F0 disc r 4.5 m round H, ground band only. On F1–F2, one disc r 2.2 m per side, centred on that side's snapshot beast nearest H that can still take positive damage (pickDiscs at 514-535). The disc is a ground touch disc for a ground beast, or a sky disc that gives a corridor hit from the sky pool for a crow. (2) Corridor: discs r 1.4 m around every S-path sample of either dragon whose pass tick lies in [pass, pass+54] (liveSamples and inSpan, 349-366). Sky beasts take 3 m capsules from each dragon's head to its side's F0 sky anchors, plus 3 m discs round live samples, F30–F56 (391-402). (3) Lotus F57–F77: full damage inside the 4 m core at P, the 4.5 m H disc, or 2.2 m of the last 13 m of each path; half damage elsewhere within 9 m of P (lotusRegion 405-411). Each tick, stepCast (607-661) gives each live, not-immune beast the first kind it may still take, in the order touch, corridor, lotus. It sorts all candidates by kind, then dist2 to H, then serial (600), and applies hit(). A hit is P = baseHp (2.5 W x g(K)) x share (15/45/40 %) x the side's falloff for that beast (100 %, −15 % per further distinct victim on the side, floor 40 %; lotus outside the petals x 0.5). damageBeast then applies grade, element, bucket, the broken-posture bonus, the 60 % swarm-cluster cap for the whole cast as one AreaHit, the pool limit and HP left (556-583; combat.ts:173-222). Each side's pool is 2.0 W x M_q x bucket split 0.3/0.9/0.8 W, plus 0.8 W for the sky part (twinPearlPool 468-478). The boss cap is 1.5 W per cast. Each beast takes at most 3 hits, one per kind, at least 20 ticks apart (mayHit 545-550). Snapshot sides are fixed; late beasts are placed by cut2. Several casts may be live at once (state.casts). Measured (272, peak sweep with 35–45 ground beasts): median 14 victims (p10–p90 11–17); static coverage 97.4 % (ground 97.3 %, sky 100 %); first hit F0 62 and F1 30; crows 95.8 %. Damage by part: body 43.6, lotusFull 19.7, f1Sky 9.5, sky 7.7, f0Disc 7.6, f1Ground 6.1, lotusHalf 5.8 % (report.md:50-58). The median of the farthest ground hit is 14.95 m and 11.60 m per side; only 13.2 % of ground beasts beyond 12 m are hit. Real matches (13317 casts): median 7 victims (p10–p90 1–12), 3.6 W per cast, 7.1 W possible, 29.4 % overkill (aggregate.txt:19). The old two-corridor greybox at 2.0 W measured 3.4 W per cast (key2-fix/aggregate.txt). Performance (271): geometry 0.062 ms, 31.4 µs per tick per cast.",
 "balanceStatus": "Ticket 272 bot (1,700 real matches, 8,325 peak-sweep casts, game commit 35f1b77, 2.0 W per side + 0.8 W sky). PASS: flag off matches the baseline 36/36; layouts 8/8; median 14 victims, 83.7 % of casts in 12–20; static coverage 97.43 %; first hit F0/F1 in every peak sweep cast and 0 of 13,315 real-match casts later than F2 (2 casts had no positive hit, reason 'other'); crows 95.8 %. FAIL: (1) side balance: 69/92 = 75 % of casts within 40/60–60/40 (target at least 85 %), with 23 failing casts between 26.9 % and 70.1 % on side 0 (report.md:64-88). (2) Key 2 share of all damage for the Standard bot: 45.99 % mean over 20 seeds (cap 45 %), 14 of 20 seeds over 45 %, up to 50.2 % (report.md:92-113). Win rates: Standard 15 % (two corridors: 95 % at 2.0 W, 100 % at 2.5 W). Shared gate B1 fails: Novice 0 %, Steady 5 %, Standard 15 %, Skilled 50 %, Sloppy 0 %, Fast 85 %; pressure P 61–66 % (band 15–35 %). B4 fails; B3, B5–B9 lack data. Budget sweep (victims · balance · Standard win · key 2 share): 1.25 W 11 · 47.8 % · 0 % · 37.5 %; 1.75 W 13 · 78.3 % · 5 % · 43.7 %; 2.0 W 14 · 75 % · 15 % · 46.0 %; 2.5 W 15 · 72.8 % · 45 % · 47.6 %; 3.75 W 19 · 81.5 % · 95 % · 54.1 %. No budget meets both the 45 % cap and a decent win rate. Key 2 share across all bots: 39.2–51.3 % (child 51.3 %, type-only 51.1 %). The cause of the win-rate drop from the two-corridor version is unexplained (task file line 15, 'Cần phân tích'). Guess: per-cast damage is similar in real matches (3.6 W vs 3.4 W), so the cause is more likely where the damage lands (nearest-H-first order; far hits 13.2 % vs 20.1 %) or code drift. The two-corridor columns were read from old numbers and not re-run (report.md:130).",
 "changesForFieldWideSwarm": [
  "Make the timeline fixed ticks that the view follows, not the reverse. Add to the variant table a dragon count (5, as approved; lab default ?dragons=6), a launch tick per dragon (lab stagger 0.3 s = 18 ticks), a swarm window, a dive tick per dragon and a burst tick. The view then sets each dragon's speed to its flown length divided by (dive tick − launch tick) instead of the lab's clamp(len/5 s, 11–16 m/s) x SPEED_K (dragon-swarm-energy.ts:595). Path length must never feed the sim.",
  "Take dragon paths out of damage: drop the body sample discs (inBody, inSpan, liveSamples), the sky capsules from head to sky anchors and the sky discs on body samples (inSkyReach 391-402), and the petals along each path's last 13 m (lotusRegion 407-409). Anchors, orderedAnchors, sPath and sampleRoute (148-333) then leave the damage path. At most they survive as optional waypoint hints the sim emits for the view.",
  "Replace them with field-level selection over all live, not-immune beasts in the ground or sky band anywhere inside stage.field. Run it on fixed sweep beats across the swarm window, ordered by a density or proximity rule. Proposal: split the F0 snapshot into k = dragon-count sectors by integer angle around P or H (cross-product comparisons, equal counts, generalising cut2; late beasts placed by angle). Each beat hits each sector's next eligible beasts until that sector's pool runs out. That keeps map-agnostic inputs (bounds, H, C, snapshot, live positions) and gives each dragon a region to fly over. The order rule needs a decision: today's kind → dist2-to-H → serial (twin-pearl.ts:600) keeps threat priority but spends budget near H (13.2 % far hits), while a far-first or interleaved order shows coverage across the field.",
  "Pearl dive and burst: the sim should emit a dive event per dragon at its fixed dive tick (optionally a small pearl-pulse hit) and resolve the 40 % 'lotus' share as a burst at the burst tick after the last dive. Proposed volume: core plus H disc full, half to a radius around P, ground and sky bands both. A field-wide burst with distance falloff would also work, still budget-capped. Keep P from integer rules: today's 3/5 pull to the ground centroid, 12 m cap, 2 m inset (280-295) is map-agnostic; the alternative is the field-bounds centre. Today's two-gate P ≈ (0, −5.9) is near both the field centre (0, −5) and the lab's fixed pearl (0, 5 m high, −6).",
  "Keep the fast first hit: the F0 4.5 m H disc and the F1 nearest-H discs (one per sector instead of per side) do not depend on paths and hold the 'first hit ≤ F1' gate (§9.5 line 720).",
  "Generalise the two-dragon hard-coding: dragons [TwinDragon, TwinDragon], disc [TwinDisc, TwinDisc], sideVictims [0,0], pool [...one, ...one], sideSlot 1/2 with cut2 (twin-pearl.ts:104-105, 271-279, 457-465, 471-477, 501-503). Use k sectors or one shared pool and falloff. Decide whether per-sector pools stay; the failing 75 % two-side balance metric exists only because of the two-side split.",
  "Decouple the variant from the line data: baseHp, falloff and posture are read from kiemSkill(2) when its effect kind is 'line' (twin-pearl.ts:445-447, 452-453, 488-489, 497), and resolve returns false otherwise. To make the swarm the real key 2, move these numbers into the variant table and route slot 2 by data (skills.ts:222). Either the header carries the variant (app.ts:153-167, 188) or the default changes. Include the new table in rulesHash (app.ts:146-148) and keep the flag-off hash pin (twin-pearl.test.ts:638-679) until it becomes the default.",
  "Add events (WANT EVENT, events.ts:7-8). A release skill-fx at F0 (x,z = C; toX,toZ = P; count = dragons). Per-dragon dive skill-fx at its tick (toX,toZ = P; count = dragon index). A burst skill-fx (P; count = victims). Either a dragon or sector index on each slot-2 hit or a beat event listing each sector's targets, so the view can route each dragon over the beasts it actually hits. Also add entries in SKILL_SOUNDS (hooks.ts:31-38; §9.12 G line 1134: silence, roars, bell) and a guard in fx.ts:301-313 so new stages do not fire generic sword volleys.",
  "Keep the END tick shorter than the 8 s cooldown (school-kiem.ts:60), or support overlapping casts in the view; the sim already keeps several casts (state.casts).",
  "Rewrite the geometry tests (twin-pearl.test.ts:108-470, twin-pearl-sweep.test.ts) and the bot's coverage measure (staticCoverage and volumesAt 414-438; tmp/skill-reach key2-measure.ts and key2-layouts.ts). Re-run the 272 matrix and budget sweep against: key 2 ≤ 45 % for Standard, 12–20 victims, first hit ≤ F1, crows ≥ 90 %, and a win-rate target that still needs a decision."
 ],
 "risks": [
  "Timing gap: sim damage is all done by F102 (1.7 s), lotus F57–F77. The approved swarm dives into the pearl seconds later: the whole skill runs 8.9 / 7.4 / 6.5 s at 1.0 / 1.3 / 1.6x (task file line 126), and the burst comes only after the last dragon's tail is in plus 0.9 s fade (dragon-swarm-energy.ts:616-621, 1026). If the sim keeps its timing, the burst plays after all damage is over. If the sim stretches to the view, the payoff comes late and the END tick nears the 8 s cooldown.",
  "Readability: once damage is field-wide and not tied to paths, damage numbers can pop where no dragon is flying. Without a dragon or sector index per hit from the sim, the view cannot send dragons over their victims.",
  "Balance is already failing at 2.0 W (key 2 share 46 %, Standard bot wins 15 %, B1 fails). Spreading the same budget over the field thins damage per beast, and raising the budget pushes key 2's share up: no budget in the sweep meets both the cap and a decent win rate (report.md:119-128). Removing the two-side split removes the failing side-balance metric but changes the balance.",
  "The cause of the win-rate drop from the two-corridor version is unknown, and the comparison columns were not re-run (report.md:130). Guess: placement of damage or code drift, not per-cast power (3.6 W vs 3.4 W per cast in real matches).",
  "Determinism: any new sector or angle rule must stay integer (mulDiv is exact only below 2^53, fixed.ts; that is why sPath splits segments at 32 m). Lab floats, the LCG and Three.js curves must never feed the sim.",
  "Not reachable in the play build today: the header never sets swordKey2. Shipping needs an app or header change, a rulesHash change and a replay-compatibility decision.",
  "The two-dragon assumption runs through the types, pools, tests (mirror and rotate at 0 u) and the bot. The name 'Twin Dragons, One Burning Pearl' (data line 16) no longer fits 5 dragons.",
  "The lab hard-codes the Thanh Thach field inset by 2 m and a fixed pearl (dragon-swarm-energy.ts:28-29), and DragonSwarmEnergy.cast() restarts the one set of dragons (976-997). The real view must take bounds and P from the stage and sim and handle a recast while dragons are still flying.",
  "The owner asked not to redo the dragon image ('không sửa lại ảnh rồng, tôi thấy ổn r'), so all fixes must stay in the sim and the view's placement and timing, not the dragon art."
 ]
}
```

## Toàn văn: view
```json
{
 "summary": "In the built play host (index.html -> src/main.ts -> src/app/app.ts startApp), key 2 is drawn only as a grey box. It is still today's line skill: resolveLine emits skill-fx stage \"line\" (src/sim/skills.ts:148-166, 222), and src/view/fx.ts:301-312 answers it with 3 swords from the shared tier pool (swordsFor, fx.ts:76-92) and a pale 0.35 s ground streak (fx.ts:169, 243-252). Sound is only a request for id \"kiem-line\" sent to a SilentMixer that plays nothing (src/audio/hooks.ts:30-37, 50-51, 113-180). Nothing under src/view/skills/* (sword-skills, element-fire, flipbook and the rest) is imported by the play host; only src/lab/* imports it. skills-lab.html is a dev-only page that is not built (vite.config.ts rollupOptions.input lists only main, bench and tinh-tu), and every lab asset comes from /art-src/lab/..., which the build does not ship. The Song Long sim from ticket 271 (35f1b77) cannot be reached from the play host. createReplayHeader (app.ts:153-168) never writes swordKey2, loadMatch calls deps.rulesHash(request.stage) with no variant (app.ts:188), and optionsFromUrl has no key2 flag (app.ts:221-245). With the flag on, the sim emits no skill-fx at all: src/sim/twin-pearl.ts contains no emit call. The view would therefore draw only the per-hit sparks and numbers from `hit` events (fx.ts:290-296), and it would get the F0 trigger from the existing `cast` event (state resolved, slot 2, actionId, origin; src/sim/cast.ts:69-87). View code receives sim output in one way: once per frame the app drains the events, then calls every presenter's onEvents(events, world) and then frame(world, info) (app.ts:866-880; contract in src/app/contracts.ts:27-31). Presenters may also read world state directly, as fx.ts does with world.skills.zones and the lab grey box does with world.skills.twinPearl.casts. The new swarm should be its own Presenter module, for example src/view/skills/qi-dragon-swarm.ts plus a twin-dragons presenter. It would be built in createGreyBoxView (src/view/stage.ts:489-512) next to fx and added to renderer.layers.fx. Its clock should come from world ticks or worldDt so that pause and hit-stop stay in step with the sim's damage. It needs a prewarm called from newMatch (app.ts:681), and its media must be prepared into public/assets/immortality-cultivation/ and listed in a manifest. The biggest open issue is timing: the 271 frame table finishes all damage by F102 (1.7 s), but the approved lab swarm takes about 6.5-8.9 s to dive into the pearl (task file, 15:25 entry), so view and sim must share one beat table before wiring.",
 "files": [
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/app/app.ts",
   "role": "Play host. Builds the header with no swordKey2 (153-168, 188). Fixed camera, no zoom. reduced() comes from watchMotion (404-405). Quality is chosen by GPU, and Apple gets medium (413-416, tierForGpu 248-255). newMatch builds the scene and presenters (660-715). Frame order is drain, then onEvents, then frame, then render (866-881)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/app/contracts.ts",
   "role": "The Presenter contract (onEvents, then frame, then dispose) and FrameInfo (dt, worldDt, alpha, now)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/app/loop.ts",
   "role": "World clock: worldDt is 0 when paused (line 67), and hit-stop slows the world through hooks.worldDt."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/view/stage.ts",
   "role": "createGreyBoxView (489-512). The presenter list is [stage, actors, player, telegraphs, fx, pickups]; the new swarm presenter plugs in here."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/view/fx.ts",
   "role": "How key 2 looks in the play host today: skill-fx 'line' gives 3 pool swords plus a streak (301-312). It also owns the one hit-stop and shake per frame (blow, frame 359-393) and the reducedProfile. blow() is internal and not exported."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/view/renderer.ts",
   "role": "Renderer3D: layers.fx, the stage (composer, bloom), quality, and the fixed whole-field camera (VIEW headroomM 2.5)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/content/rules.ts",
   "role": "TT_TIERS (694-699: Low has no bloom, particles 600/1500/3000) and TT_BUDGETS (742-759: skinnedMax 6/6/8, drawCalls 80/110/150, textureMb 64/128/192, cpuP95Us 6000). DEFAULT_TIER gives medium on Apple (769)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/audio/hooks.ts",
   "role": "Maps events to sound ids. SKILL_SOUNDS has line -> kiem-line (30-37). The SilentMixer plays nothing in M0a, and no id exists yet for twin dragons."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/audio/catalog.ts",
   "role": "Sound cards, for example kiem-line (line 67). New cards for twin dragons go here."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/skills.ts",
   "role": "Key 2 dispatch: twin-pearl when world.skills.twinPearl is set, else the line (222). Only the line emits skill-fx (164)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/twin-pearl.ts",
   "role": "The 271 sim. Emits no events. Holds the per-cast record TwinPearlCast (castId, startTick, px/pz pearl, hx/hz) in world.skills.twinPearl.casts. Today its damage depends on its own two S paths (body r 1.4 m, stepCast 607-662)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/sim/cast.ts",
   "role": "Emits the 'cast' event with state resolved on the F0 tick, carrying actionId (= TwinPearlCast.castId) and origin (lines 69-87). This is the view's trigger."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/content/data/twin-pearl.ts",
   "role": "TWIN_PEARL frame table (heads F3-F48, roar F49-56, lotus F57-77). The new view beats should be read from the same table."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/lab/twin-pearl-greybox.ts",
   "role": "Lab precedent for a view that reads TwinPearlCast from a real sim world with swordKey2 (header 22-26, read casts 250-251, prewarm 487, update(dt) 295)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm/src/lab/dragon-swarm-energy.ts",
   "role": "The approved look (lab only). Contains URL knobs (19-46), /art-src URLs (14-26, 755-756), hard-coded FIELD and PEARL (28-29), speed clamp (595), per-bone posing (612-731), Pearl (400-455), Glints 1600 (770), depth-prepass SkinnedMesh (832-836), an uncommitted prewarm (902-965), cast (976-997), update (999-1033) and steerPath (1080-1144)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm/src/lab/skills-main.ts",
   "role": "Lab host. ?key2=energy builds the swarm (208-213). The key 2 branch (983-989) returns before emitRelease, so the swarm has no sound or callout events. zoom.holdWide includes swarmE.running (1359). Prewarm loop over composer.readBuffer and null (1657)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm/tests/lab/dragon-swarm-motion.test.ts",
   "role": "106 motion regression tests from Codex 288/289. They stub location because the module reads URL knobs at import time."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/src/kit/three/model-loader.ts",
   "role": "loadModel with meshopt (166-184). pickModelTier: Low loads no 3D, Medium prefers .medium (79-87). The manifest kind 'skills' exists (model-contracts.ts:15)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/dragon-hold/scripts/assets/prepare-firefly.mjs",
   "role": "Concrete art-src to play-build example (Hoa Long fire flipbooks). Copies the source cut to art-src/vfx/firefly/<id>/ and writes public/assets/dragon-hold/vfx/firefly/<id>.webp plus manifest.json."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/dragon-hold/src/view/flipbook.ts",
   "role": "Runtime side of that example: FIREFLY_BASE='/assets/dragon-hold/vfx/firefly/' (line 76); pools built and warmed at load with their final blend (header lines 1-16)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/dragon-hold/scripts/models/m0b-tiers.mjs",
   "role": "Model tiers example: Tripo original, then Blender, meshopt, WebP per tier, then public/assets/dragon-hold/models/<set>/<kind>/<id>/<id>.<tier>.glb plus manifest."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/media/media.config.json",
   "role": "Tu Tien media entry (55-65): lock media.md5, modelsDir public/assets/immortality-cultivation/models, sources art-src/3d/SOURCES.json. That SOURCES.json is missing today."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/models/qi-dragon/qi-dragon.rig.glb",
   "role": "Lab rig: 15.5 MB, 25,990 tris, 40 joints, three 4096x4096 maps (normal PNG, baseColor JPG, MR JPG). The qi shader uses only baseColor."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/sound",
   "role": "Firefly Twin Dragons SFX, all 'done' per docs/work/tasks/firefly-sprint-sound.json: twin-bronze-bell-high, sword-crack, sub-hit, fire-whoosh-a/b, flame-flutter, fire-breath, pearl-shimmer, dragon-roar-a/b/c, roar-rumble, deep-boom, bell-giant(-b), mountain-echo, ember-crackle, sparkle-ticks. callouts/callout-twin sits beside it."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md",
   "role": "Section 9 frame table (9.5), the view inputs (9.9) and the English callout decision (9.11.2)."
  },
  {
   "path": "/Volumes/SS990TPRO/htdocs/typing-game/docs/work/tasks/twin-dragons.md",
   "role": "Swarm history: 5 dragons from v3; speed measurements of 8.9/7.4/6.5 s at 1.0/1.3/1.6x; owner 15:35 asked to wire the swarm into the real key 2."
  }
 ],
 "viewHooks": [
  "Sim events: each frame the app drains world events and calls presenter.onEvents(events, world), then presenter.frame(world, info) (app.ts:866-880). FrameInfo carries dt, worldDt (0 when paused, slowed by hit-stop, loop.ts:67), alpha and now. Key 2 today arrives as skill-fx stage 'line' (skills.ts:164). The twin-pearl sim emits nothing of its own, so the swarm view should start on the 'cast' event with state 'resolved', slot 2 and seat (cast.ts:69-87). It then looks up world.skills.twinPearl.casts by castId === actionId for startTick and pearl P (px, pz), in u converted with uToM. Precedent: fx.ts reads world.skills.zones and twin-pearl-greybox.ts:250 reads twinPearl.casts. Cleaner option, a guess: a WANT EVENT such as skill-fx stage 'twin-pearl' carrying P and the beat ticks, emitted only inside resolveTwinPearl. Events are not hashed (events.ts header), so flag-off stays unchanged.",
  "Damage feedback: twin-pearl hits come through damageBeast as ordinary `hit` events with source 'slot2' (twin-pearl.ts:579). fx.ts already draws a spark and a damage number per hit and asks for one hit-stop and shake per frame (fx.ts:290-296, 359-367). A pearl-burst climax that wants a T5 blow needs fx to expose blow(tier), because it is internal; calling fx.hitStop directly would bypass the one-stop-per-frame rule.",
  "Camera / zoom hold: the play host camera is fixed and fitted to the whole field (renderer.ts header; app.ts header: 'the camera is fixed'). CameraZoom and holdWide exist only in the lab (src/view/camera-zoom.ts, used only by skills-main.ts, where swarmE.running holds wide at line 1359). No hold is needed in game. Shake is a whole-pixel projection offset in fx.ts applyShake and is off with reduced motion. Guess, needs a capture: dragons in altitude bands 2.6-7.2 m (dragon-swarm-energy.ts:988-989) and the pearl at y 5 may leave the top of the frame near the far edge, since the fit keeps only 2.5 m headroom (VIEW.headroomM).",
  "Sound cues: in the play host, hooks.ts maps skill-fx stages to ids (line -> kiem-line, 30-37) and maps 'cast' only for the dash (52-54). The mixer is the silent M0a SilentMixer, so nothing is heard in the play build today. The lab swarm emits no sound: its key 2 branch returns before emitRelease (skills-main.ts 983-989 vs 382-404). Lab files exist for release-k2 (3 takes) and callout-k2 (1) under art-src/lab/audio, plus the Firefly sprint twin set, which was cued to the old F0/F3/F47/F51 frames. Beats that only the view knows (each launch, each dive, the burst) cannot reach soundFor, which only sees sim events. They need sim beat events, or the swarm presenter must push ids to the sound hooks.",
  "Prewarm: the play host has no prewarm hook. The only prewarms are screen-fx.ts, which is lab-only, and the lab loop at skills-main.ts:1651-1663, which compiles for view.stage.composer.readBuffer and null. The worktree has an uncommitted DragonSwarmEnergy.prewarm (dragon-swarm-energy.ts:902-965) that compiles with compileAsync, uploads textures and bone textures, and draws once into its own 64x64 target, wired in skills-main.ts:212. In game, call it from newMatch after createGreyBoxView (app.ts:681), during prep or Học trước, and load the GLB once per app rather than once per match.",
  "Reduced motion: app.ts:404-405 passes reduced() into createGreyBoxView, and every view asks it each frame. fx keeps shake off and stops short. Canon §24 (00-canon.md:1216) requires no camera shake, no long freeze, short VFX and no background flash. The lab swarm has no reduced handling. It also reads ?motion=wave|swim at import (dragon-swarm-energy.ts:40), which collides with the game's own ?motion= flag read by ui/skin.ts watchMotion.",
  "Quality tiers: renderer.quality is fixed per match. TT_TIERS gives Low no bloom and no composer, and particles 600/1500/3000 (rules.ts:694-699). TT_BUDGETS caps skinnedMax at 6/6/8 and drawCalls at 80/110/150 (742-759). The kit's pickModelTier loads no 3D at Low (model-loader.ts:79-87). The lab swarm ignores all of these."
 ],
 "assetPath": "Today no skill art reaches the Tu Tien play build. Every lab skill loads from /art-src/lab/..., which the Vite dev server serves from the repo root. art-src/ is git-ignored (art-src/.gitignore is '*'), and the build has only main, bench and tinh-tu (vite.config.ts). public/ holds only assets/bench-vat locally. media.md5 lists 42 lookdev files under public/assets/immortality-cultivation/ that are not pulled on this machine.\n\nThe repo's route (docs/MEDIA_STORAGE.md; scripts/media; media/media.config.json:55-65) is:\n- Originals stay in art-src, kept on Google Drive by the 'originals' set.\n- A per-game prepare script writes runtime files under games/<id>/public/assets/<id>/ with a manifest.json. These files are not in Git.\n- `pnpm media:push` from the parent repo uploads the 'runtime' set (sets.mjs:96-122, which also picks up untracked JSON under public/assets/<id>/) and records md5s in the game's media.md5. Other machines run `pnpm media:pull`.\n- The game loads the files by manifest at /assets/<id>/... Vite copies public/ into dist/ unchanged.\n\nConcrete example, Dragonhold's Hoa Long fire (the Firefly flipbooks):\n1. games/dragon-hold/scripts/assets/prepare-firefly.mjs reads ~/VFXLab/out/dragon-hold/<id>/ cuts.\n2. It copies the chosen cut to art-src/vfx/firefly/<id>/ and writes public/assets/dragon-hold/vfx/firefly/<id>.webp (WebP q92, alpha kept), plus manifest.json with cols/rows/fps/pivot/md5/bytes.\n3. src/view/flipbook.ts:76 loads from FIREFLY_BASE='/assets/dragon-hold/vfx/firefly/' and warms each pool with its final blend at load (header lines 5-9).\n\nFor models, Dragonhold's scripts/models/m0b-tiers.mjs takes Tripo originals in art-src/3d, runs Blender, meshopt and quantize, makes WebP maps per tier, and writes public/assets/dragon-hold/models/<m0b|kit3>/<kind>/<id>/<id>.<tier>.glb plus manifests. The kit ModelLibrary then picks a tier per quality, and Low gets none.\n\nFor the qi dragon, the analogue would be a new prepare script, for example games/immortality-cultivation/scripts/assets/prepare-twin-dragons.mjs. This is a proposal, not existing code.\n- Input: art-src/lab/models/qi-dragon/qi-dragon.rig.glb, the Blender rig output of the Tripo original in art-src/3d/skills/qi-dragon/tripo-out.\n- Keep the 26k tris and 40-bone skin, since the model-detail rule says not to cut below the floor.\n- Drop the unused normal and metallicRoughness 4096 maps; the qi shader samples only baseColor (dragon-swarm-energy.ts:809-814).\n- Write the baseColor as WebP at 2048 for .high and 1024 for .medium, meshopt-compressed while keeping JOINTS/WEIGHTS.\n- Output public/assets/immortality-cultivation/models/skills/qi-dragon/qi-dragon.<high|medium>.glb with an entry of kind 'skills' in public/assets/immortality-cultivation/models/manifest.json (the path media.config.json already names).\n- Copy the textures into public/assets/immortality-cultivation/vfx/twin-dragons/ with a manifest and md5: qi-scales.png, strip-fire-sheath-v2.rgba.png, and the Kenney CC0 star_04, flare_01, light_01, circle_04, circle_05 with KENNEY-LICENSE.txt.\n- Copy chosen sound takes into public/assets/immortality-cultivation/audio/ when the real mixer lands.\n- Then run index-3d-sources (art-src/3d/SOURCES.json does not exist yet) and `pnpm media:push`.",
 "labVsGame": "The lab module (games/.wt-ic-dragon-swarm/src/lab/dragon-swarm-energy.ts, branch claude/dragon-swarm-lab, with an uncommitted prewarm) differs from what the game view needs in these ways.\n\n(1) URL knobs at import time. PARAMS is read from location.search at module scope: dragonLook, speed, minTurn, maxBend, swimWave/Side/Lift/Drift, density, glow, back, lineLo/Hi, blur, body, rim, fill, dorsal, maneCut, scaleAround/Along, pools, and motion (lines 19-46, 797-822, 880). The game must have none of these. They should become a frozen look constant: qi look only, with SPEED_K set to the agreed 1.3. ?motion= also collides with the game's reduced-motion flag. The shell/full looks and FRAG/FRAG_TEX are dead code for the game.\n\n(2) Assets. Everything loads from /art-src/lab/... (14-26, 755-756), which is not in the build. The rig is 15.5 MB with three 4096 maps.\n\n(3) Hard-coded geometry. FIELD (-18..18, -16..6) and PEARL (0,5,-6) are constants (28-29). The game must take them from world.stage.field (rules FIELD is -20..20 x -18..8) and from the sim cast's P. The waypoint ring uses only the field bounds, so it is already map-agnostic.\n\n(4) Clock. The lab advances on real dt (update(dt), 999-1001; skills-main.ts:1376). The game should use world ticks or worldDt, so pause (worldDt 0), hit-stop and dev speed freeze or slow it together with the sim damage. Flight time is also variable, because speed = clamp(len/5, 11, 16) x SPEED_K (595) and dragons are staggered by 0.3 s. Measured totals are 6.5-8.9 s, while the 271 sim finishes damage by F102 (1.7 s). The game needs time-fixed flights: speed = len / (diveTick - launchTick) from a shared beat table.\n\n(5) One swarm. cast() restarts every dragon (976-997). Key 2's cooldown is 8 s (school-kiem.ts:60), shorter than the visual plus the 0.7 s pearl burst. Overlapping casts and ally seats need a pool of two swarms, or a fade-out hand-off.\n\n(6) No quality tiers or budgets.\n- Glints are a fixed 1600 points (770), against particle caps of 600/1500/3000.\n- Each dragon has a body plus a depth-prepass SkinnedMesh (832-836). 5 dragons make 10 SkinnedMesh, over skinnedMax 6/6/8.\n- About 25 draw calls for dragons, flares and trails, plus 4 for the pearl and 1 for glints.\n- Low has no bloom, so the toneMapped:false HDR colours clip, and the kit loads no 3D at Low. Low needs a separate look, for example the earlier 2D swarm in dragon-swarm.ts.\n- The owner's Apple M4 defaults to Medium in the play host (DEFAULT_TIER), but the lab defaults to High. The look was approved at High.\n\n(7) Per-frame CPU and allocation.\n- For each of 40 bones, posing calls parent.updateWorldMatrix(true,false) and bone.updateMatrixWorld(true) (701-709). Each force-updates the rest of the chain, so roughly 820 matrix updates per dragon per frame.\n- getPointAt and getTangentAt run per bone.\n- The glint buffer is re-uploaded every frame, and emission is frame-rate dependent (8 per dragon per frame, 1007).\n- steerPath declares a class inside the function on each cast and allocates arrays (1080-1144).\n- These must be measured against cpuP95Us 6000 and frameP95.\n\n(8) Pooling and loading. The constructor loads asynchronously, and cast() does nothing until ready (977). The game needs load-once-per-app, a prewarm during prep, and a fallback if a cast comes before the load finishes.\n\n(9) No sound, callout, hit-stop or reduced-motion handling, and no damage link. The swarm is view only.\n\n(10) Lab conveniences to drop or rewire: window.__swarmE, caster.release('k2', 0, -9) (the play host player is a capsule), and zoom.holdWide.\n\nThe motion tests (tests/lab/dragon-swarm-motion.test.ts) stub location. They must move with the module and keep passing at the fixed-time speeds.",
 "plan": [
  "0. Before any code, fix the shared beat table with the sim agent and the owner. Put it in content data (for example TWIN_PEARL.view or a new swarm table) with: the F0 release, the launch stagger, each dragon's dive tick, the pearl burst tick and the aftermath end. The sim's field-wide damage pulses and the view both read it. Today the 271 frames (heads F3-F48, lotus F57-77, damage to F102) cannot match a 6.5-8.9 s flight. Also decide how swordKey2 reaches the play build: a dev-only flag first, then the default header.",
  "1. Promote the lab module into src/view/skills/qi-dragon-swarm.ts with the qi look only: Dragon, Pearl, Glints, Trail, steerPath and addFlowAttributes. Replace every URL knob with a frozen constant (speed 1.3x), keep the lab's ?key2=energy importing the view module, and move tests/lab/dragon-swarm-motion.test.ts to tests/view without the location stub.",
  "2. Change the clock to world time. Compute t = (world.tick - startTick + alpha)/60, or accumulate info.worldDt. Make each flight time-fixed: speed = path length / (dive tick - launch tick), with the 4.45 m minimum turn kept. Re-run the motion tests for turn radius, jerk and flips, and add a test that pause freezes the swarm and hit-stop slows it.",
  "3. Inputs: start the swarm on the 'cast' event (resolved, slot 2, seat) and find the TwinPearlCast by castId === actionId. Take origin and P from the cast (uToM), the field from world.stage.field, and the per-cast visual seed from actionId. Draw nothing when world.skills.twinPearl is undefined; the line path stays exactly as today. Optionally add the WANT EVENT skill-fx 'twin-pearl' with P and beats.",
  "4. Write the presenter createTwinDragonsView(renderer, {reduced, seat, quality, fx}) and register it in createGreyBoxView (stage.ts:497-499) next to fx, with its group in renderer.layers.fx. It holds a pool of 2 swarms for overlapping or ally casts (ALLY_SHARE gives fewer dragons for allies). Its dispose removes per-match objects but keeps the per-app GLB cache.",
  "5. Feedback: add a public fx.blow(tier) and call it for the pearl burst (T5) so there is still one hit-stop and shake per frame. Keep hit sparks and numbers from `hit` events. Cap the pearl flash and halo at 0.9 per channel.",
  "6. Quality tiers:\n- High: 5 dragons, .high GLB, glints capped by TT_TIERS particles.\n- Medium (Apple default): .medium GLB, about 600 glints, fewer trails.\n- Low: kit Low loads no 3D and has no bloom, so build a 2D fallback, for example the dragon-swarm.ts flipbook swarm, with its own non-HDR colours.\n- Settle the 10-SkinnedMesh overrun of skinnedMax 6/8: either ask for a named exception like TT_LIMITS.skinnedSeven, or fold the depth prepass into an onBeforeRender second draw.\n- Fix the O(n^2) bone matrix updates and the per-frame allocations.",
  "7. Reduced motion (canon §24, read reduced() each frame): no shake, short stops (fx already does this), shorter aftermath and glint life, lower swim amplitude, and no full-screen or background flash. Keep the beat times, because damage does not change with this setting.",
  "8. Assets: write scripts/assets/prepare-twin-dragons.mjs following Dragonhold's prepare-firefly.mjs and m0b-tiers.mjs. It turns the rig GLB into qi-dragon.high/medium.glb (baseColor WebP only, meshopt, skin kept) under public/assets/immortality-cultivation/models/skills/qi-dragon/ with a manifest entry of kind 'skills', and copies the textures with md5s into public/assets/immortality-cultivation/vfx/twin-dragons/manifest.json. Then create art-src/3d/SOURCES.json with index-3d-sources, run `pnpm media:push`, and load through the kit ModelLibrary and loadModel.",
  "9. Loading and prewarm: start loading at app start and cache it per app. In newMatch, after createGreyBoxView (app.ts:681), call prewarm for renderer.stage.composer.readBuffer and for null (the screen), as skills-main.ts:1657 does. Check whether the uncommitted 64x64-target prewarm compiles the same program variant as the composer target. If the swarm is not ready at F0, draw the fallback so the F0 frame is never blocked.",
  "10. Sound: add ids and catalog cards (audio/catalog.ts) re-cued to the new beats.\n- F0: bronze bell, sword crack, sub hit.\n- Each launch: whoosh a/b and flame flutter, plus a fire-breath bed while flying.\n- Each dive: pearl shimmer.\n- Before the burst: roar a/b/c and rumble.\n- Burst: deep boom, giant bell, mountain echo.\n- Aftermath: ember crackle and sparkle ticks.\n- callout-twin, in English.\nMap them through hooks.ts using sim beat events, or let the presenter push ids. Playback stays silent in the play host until the M0b real mixer replaces SilentMixer, so the lab host must carry the sound check meanwhile.",
  "11. Check in the lab first: drive the new view module from the lab's real sim world (?key2=twin-pearl grey box, twin-pearl-greybox.ts). Verify sync of P, dives and burst against the hits, map-agnostic layouts (L cycles 5 layouts), and the speed of the first strike.",
  "12. Then the play host: a dev-only path (for example optionsFromUrl key2 in dev builds that sets header swordKey2 and rulesHash variant, app.ts:188) for captures. After the sim, balance and owner sign-off, make swordKey2 the default header, so that the built play host shows the swarm without URL flags.",
  "13. Verify: vitest (motion, presenter pool, reduced, no per-frame allocation), tsc, pnpm build. Measure the built host on 3008 at Medium and High against TT_BUDGETS: draw calls, cpuP95 6000 us, frameP95, the first-cast frame without a compile stall, and textureMb. Then make a before/after video for the owner and run the blind 8.5 judging in the play build."
 ],
 "risks": [
  "Timing mismatch: the 271 sim lands all damage by F102 (1.7 s), with the lotus at F57. The approved swarm takes 6.5-8.9 s to dive (task file, 15:25). Without one shared beat table, hits will appear long before or with no relation to the dragons. The current sim damage also follows its own two S paths, which the swarm does not draw.",
  "The play build has no key 2 swarm path today. swordKey2 is never set by the app (app.ts:153-168, 188), and all view/skills code is lab-only (skills-lab.html is not built). Judging 'in the play host with no URL flags' needs both the presenter and a default header change. That changes rules and replays (rulesHash variant) and needs the owner's sign-off.",
  "The look was approved at the lab's default High, but the owner's Apple M4 gets Medium by default in the play host (DEFAULT_TIER apple: medium). Low has no bloom and the kit loads no 3D at Low. The approved look will not carry over unchanged.",
  "Budgets: 5 dragons at about 26k tris each, doubled by the depth prepass, make 10 SkinnedMesh against skinnedMax 6/8. 4096 maps would cost about 89 MB each with mips against textureMb 64/128/192. Glints are 1600 against a Low particle cap of 600.",
  "CPU: the per-bone updateWorldMatrix and updateMatrixWorld(true) chain costs O(n^2) per dragon (dragon-swarm-energy.ts:701-709), there are about 400 curve lookups per frame, and the glint buffer is re-uploaded every frame. Not measured in the play host yet.",
  "Overlapping casts: the 8 s cooldown is shorter than the visual plus the 0.7 s burst, and cast() restarts the single swarm, so a second cast would snap every dragon back to the caster.",
  "Clock choice: driving the swarm from world time keeps it synced with damage, but hit-stops will micro-freeze a 7 s glide that the owner wants smooth. Driving it from real time breaks sync and keeps it running in the pause menu (worldDt 0). This needs a decision.",
  "First-cast stall: the play host has no prewarm hook. The uncommitted lab prewarm draws into its own 64x64 target, which may not compile the composer's program variant. This is a guess and needs measurement on the first cast.",
  "Framing (guess): dragons in altitude bands up to about 7.2 m and the pearl at y 5 may leave the top of the fixed camera near the far edge (headroomM 2.5).",
  "Sound: the play host mixer is silent (M0a), so sound can only be judged in the lab until the real mixer lands. The Firefly twin SFX were cued to the old F-frames and must be re-timed.",
  "Reduced motion: canon §24 asks for short VFX and no flashes. A 7 s swarm with per-dive flashes and a burst needs a reduced variant that still shows where the skill acts.",
  "Media pipeline: art-src/3d/SOURCES.json is missing in Tu Tien. MEDIA_STORAGE says push refuses an unmatched SOURCES.json; that was stated for Space, and applying it to Tu Tien is a guess. Local public/assets/immortality-cultivation is not pulled.",
  "Dragon count is unclear: the task file says 5 (v3), the lab host defaults to 6 (skills-main.ts:208) and the class defaults to 8. Confirm what the owner approved before wiring.",
  "The worktree has uncommitted edits to dragon-swarm-energy.ts and skills-main.ts (prewarm), and the task file says not to edit dragon-swarm-energy.ts while Codex tickets run. Promote the module only after those land."
 ]
}
```
