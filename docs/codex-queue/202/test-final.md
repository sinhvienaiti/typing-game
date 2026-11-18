# Kết quả toàn bộ test qua pnpm check lượt hiện tại

```text
RUN  v3.2.7 /Users/toandx/htdocs/typing-game/games/.wt-td-scenery

 ✓ tests/td-pace.test.ts (12 tests) 940ms
   ✓ the run header and pace k (BALANCE.md §4.1) > keeps the attention budget at every k: the R3 typist at 35 WPM never types more than 8 s in 20 s, director on  654ms
 ✓ tests/boundary.test.ts (17 tests) 1591ms
   ✓ Lời Gọi boundary (TK 25.3, SPLIT_PLAN §3) > the rules use no clock, host global, storage, locale, Math.random, trigonometry, powers or logarithms  1240ms
 ✓ tests/td-boss.test.ts (21 tests) 821ms
 ✓ tests/td-flow.test.ts (7 tests) 2740ms
   ✓ the stage matrix and its report (BALANCE.md §3, §7) > types through the commands at the bot's own speed and accuracy, and measures every run (flow, pace, kill time, the learning gate)  1049ms
   ✓ the stage matrix and its report (BALANCE.md §3, §7) > plays Học as the page plans it (R3, BUILD_1B §18.1): the cold start deals fresh words, the 20-word book brings Từ Ôn back; B8 R3 holds (≤ 8 fresh, none in a call that runs out or on the boss night)  424ms
   ✓ the stage matrix and its report (BALANCE.md §3, §7) > folds a cell into the kit's summary and prints the §3 table and every gate (missing cells are THIẾU SỐ, never ĐẠT)  1259ms
 ✓ tests/td-calls.test.ts (20 tests) 2882ms
   ✓ invariants (§12 gate 6) and replay > random play on the real vocabulary: bright ≤ cap, one lock on a bright call, one word a bright call, distinct first letters; the log replays to the same hash  1534ms
   ✓ invariants (§12 gate 6) and replay > ignoring every call (Chữ Chiêu and direct calls too, BUILD_1B §21.3) never lowers the chain and loses nothing: gold falls only by seeds bought, food only by soldiers' meals, wood never  1149ms
 ✓ tests/td-input.test.ts (24 tests) 740ms
   ✓ the sandbox preset and the suggested spots > offers mines the free nodes, and others the places by the road canPlace allows (gold aside), nearest a bend first, both ways round  349ms
 ✓ tests/td-golden.test.ts (6 tests) 831ms
   ✓ golden run > runs the same twice, and its command log replays to the same hashes  701ms
stdout | tests/td-sim-perf.test.ts > simulation step cost > steps 300 enemies, 9 soldiers, 200 shots, 10 buildings, 4 farms, 9 villagers and 20 trees in ≤ 2 ms
td sim step (300 enemies): median 0.070 ms, p95 0.281 ms

 ✓ tests/td-sim-combat.test.ts (11 tests) 424ms
stdout | tests/td-sim-perf.test.ts > simulation step cost > steps TK 25.12's full load (640 enemies, 64 soldiers, 512 shots, 20 buildings) in ≤ 2 ms
td sim step (640 enemies, 64 soldiers, 512 shots, 20 buildings): median 0.052 ms, p95 0.185 ms

stdout | tests/td-sim-perf.test.ts > simulation step cost > steps Mộc Tinh's peak under a flood of 300 (its Mầm Gỗ among them) with Tối Thượng's rain falling (BUILD_1B §20) in ≤ 2 ms
td sim step (boss, 300 flooded, Tối Thượng): median 0.251 ms, p95 0.893 ms

stdout | tests/td-scenery-prep.test.ts > decoded atlases keep dimensions, positive z and zero unreported keyed pixels (13:28 decision)
decoded high almond-tree-v3: key=0, exempt=1 (dark=1, alpha0=0)
decoded high almond-tree-v4: key=0, exempt=0 (dark=0, alpha0=0)
decoded high bamboo-clump-v3: key=4, exempt=7 (dark=7, alpha0=0)
decoded high bamboo-clump-v4: key=3, exempt=0 (dark=0, alpha0=0)
decoded high canopy-block-v3: key=3, exempt=5 (dark=5, alpha0=0)
decoded high canopy-block-v4: key=0, exempt=1 (dark=1, alpha0=0)
decoded high mountain-pine-v3: key=0, exempt=4 (dark=4, alpha0=0)
decoded high mountain-pine-v4: key=2, exempt=8 (dark=8, alpha0=0)
decoded medium almond-tree-v3: key=0, exempt=0 (dark=0, alpha0=0)
decoded medium almond-tree-v4: key=0, exempt=0 (dark=0, alpha0=0)
decoded medium bamboo-clump-v3: key=0, exempt=3 (dark=3, alpha0=0)
decoded medium bamboo-clump-v4: key=0, exempt=0 (dark=0, alpha0=0)
decoded medium canopy-block-v3: key=0, exempt=3 (dark=3, alpha0=0)
decoded medium canopy-block-v4: key=0, exempt=0 (dark=0, alpha0=0)
decoded medium mountain-pine-v3: key=2, exempt=2 (dark=2, alpha0=0)
decoded medium mountain-pine-v4: key=0, exempt=1 (dark=1, alpha0=0)

 ✓ tests/td-scenery-prep.test.ts (10 tests) 4169ms
   ✓ decoded atlases keep dimensions, positive z and zero unreported keyed pixels (13:28 decision)  4088ms
 ✓ tests/td-sim-perf.test.ts (4 tests) 447ms
stdout | tests/td-fx-pipe.test.ts > 036 FxPipe > 5 matches an independent scan of the golden run
036 golden counts {"ticks":19660,"muzzle":133,"arrow":90,"shell":1,"bolt":11,"fireball":23,"wordShot":8,"feather":0,"hit":102,"crit":12,"stats":{"read":489,"fire":133,"hit":102,"lost":0}}

 ✓ tests/td-fx-pipe.test.ts (5 tests) 615ms
   ✓ 036 FxPipe > 5 matches an independent scan of the golden run  595ms
 ✓ tests/td-3d-road.test.ts (3 tests) 442ms
   ✓ C10: map 1's road field and dressing > dresses the edges off the roads, the water, the bridges and the yards, the same on every load  439ms
 ✓ tests/english-ui.test.ts (2 tests) 395ms
   ✓ keeps source literals and generated labels in English, preserving vocabulary meanings and proper names  393ms
 ✓ tests/td-sim-economy.test.ts (29 tests) 4477ms
   ✓ sites and builders (§4.3) > no sequence of builds, upgrades (the Bastion's too), sales at 60 %, undos and free sandbox levels makes gold or wood (property; BUILD_1B §7, G7)  3566ms
 ✓ tests/td-stage.test.ts (5 tests) 344ms
 ✓ tests/td-learn.test.ts (20 tests) 379ms
 ✓ tests/td-learn-app.test.ts (9 tests) 477ms
   ✓ the store and the plan (§11.3, §11.4) > counts a word seen up to 3 times; past 3,000 ids the oldest goes  461ms
 ✓ tests/td-b9.test.ts (3 tests) 4044ms
   ✓ the play-test file and B9 (BUILD_1B §22, BALANCE.md §7 B9) > holds the numbers B9 reads and the run in the replay's shape; replayed on Node it reaches the page's hash  407ms
   ✓ the play-test file and B9 (BUILD_1B §22, BALANCE.md §7 B9) > grades B9 against a bot typing at the owner's measured E, a and CV (an old file with the numbers alone too)  3442ms
 ✓ tests/td-placement.test.ts (12 tests) 323ms
 ✓ tests/td-chunks.test.ts (4 tests) 128ms
 ✓ tests/td-r2.test.ts (14 tests) 186ms
 ✓ tests/td-test-pass.test.ts (8 tests) 125ms
 ✓ tests/td-agents.test.ts (11 tests) 229ms
 ✓ tests/td-rewards.test.ts (7 tests) 87ms
 ✓ tests/td-hud.test.ts (13 tests) 332ms
 ✓ tests/td-tips.test.ts (6 tests) 328ms
 ✓ tests/td-view.test.ts (5 tests) 91ms
 ✓ tests/td-r3-abilities.test.ts (6 tests) 71ms
 ✓ tests/td-router.test.ts (9 tests) 106ms
 ✓ tests/td-sim-block.test.ts (9 tests) 102ms
stdout | tests/td-lanes.test.ts > the lane spreader > lays out 20 cards in ≤ 0.3 ms
td lanes: 0.0167 ms a frame for 20 cards

 ✓ tests/td-lanes.test.ts (10 tests) 71ms
stdout | tests/td-content.test.ts > 1A content > every word can be typed in its scoring clock (TK 25.4): L_w ≥ 1.2 + 12·(len + 1)/(E·d) at every E, mode and band
td life: 128 (mode, E, length) cells below 1.2 s + typing time, all in challenge; first: challenge E30 3 letters: 2.70 s, challenge E30 4 letters: 2.88 s, challenge E30 5 letters: 3.24 s

 ✓ tests/td-content.test.ts (13 tests) 94ms
 ✓ tests/td-scorer.test.ts (7 tests) 45ms
 ✓ tests/vocab-pin.test.ts (5 tests) 16ms
 ✓ tests/td-3d-camera.test.ts (5 tests) 12ms
 ✓ tests/td-sheet-cards.test.ts (8 tests) 23ms
 ✓ tests/td-letters.test.ts (7 tests) 11ms
 ✓ tests/td-sound-map.test.ts (2 tests) 4ms
 ✓ tests/td-3d-ground.test.ts (5 tests) 47ms
 ✓ tests/td-c10-r3.test.ts (2 tests) 5ms
 ✓ tests/td-settings.test.ts (6 tests) 4ms
stdout | tests/td-nav.test.ts > A* on the walking grid (TK 25.9) > one search takes ≤ 0.5 ms (TK 25.12): the longest ways on the sandbox field, across the stream
td A*: median 0.156 ms, p95 0.731 ms

 ✓ tests/td-nav.test.ts (10 tests) 5898ms
   ✓ A* on the walking grid (TK 25.9) > walks every way across the stream on the painted bridges: 400 random crossings never leave them (cells wholly on a bridge)  382ms
   ✓ A* on the walking grid (TK 25.9) > a helper built over beside the stream, by the bridge, never lands in the water and still reaches the mine  4880ms
 ✓ tests/td-scenery-layout.test.ts (73 tests) 1718ms
   ✓ 202: pure seeded scenery layout > is deterministic, seed sensitive, sorted, and preserves frozen inputs  326ms
   ✓ 202: pure seeded scenery layout > matches nine sample-only FNV-1a goldens  573ms
   ✓ 202: pure seeded scenery layout > has a conservative road fallback and never substitutes missing types  534ms
 ✓ tests/td-balance-gates.test.ts (10 tests) 3ms

 Test Files  44 passed (44)
      Tests  475 passed (475)
   Start at  13:39:59
   Duration  12.28s (transform 1.85s, setup 0ms, collect 20.95s, tests 36.82s, environment 4ms, prepare 1.86s)
```
