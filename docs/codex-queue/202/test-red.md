# Nhật ký test trước mã: lỗi thiếu module như dự kiến

```text

 RUN  v3.2.7 /Users/toandx/htdocs/typing-game/games/.wt-td-scenery


⎯⎯⎯⎯⎯⎯ Failed Suites 1 ⎯⎯⎯⎯⎯⎯⎯

 FAIL  tests/td-scenery-layout.test.ts [ tests/td-scenery-layout.test.ts ]
Error: Cannot find module '../src/view/3d/scenery-layout' imported from '/Users/toandx/htdocs/typing-game/games/.wt-td-scenery/tests/td-scenery-layout.test.ts'
 ❯ tests/td-scenery-layout.test.ts:8:1
      6| import { BORDER_M, heightAt } from "../src/view/3d/ground";
      7| import { roadField } from "../src/view/3d/road";
      8| import { buildableAt, sceneryLayout, SCENERY_BUDGET, type SceneryEntry…
       | ^
      9| import { inspectLayout } from "../scripts/td/scenery-layout-sheet";
     10| 

Caused by: Error: Failed to load url ../src/view/3d/scenery-layout (resolved id: ../src/view/3d/scenery-layout) in /Users/toandx/htdocs/typing-game/games/.wt-td-scenery/tests/td-scenery-layout.test.ts. Does the file exist?
 ❯ loadAndTransform node_modules/.pnpm/vite@7.3.7_@types+node@24.19.2_tsx@4.23.15/node_modules/vite/dist/node/chunks/config.js:22907:33

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯[1/1]⎯


 Test Files  1 failed (1)
      Tests  no tests
   Start at  11:33:19
   Duration  288ms (transform 67ms, setup 0ms, collect 0ms, tests 0ms, environment 0ms, prepare 37ms)

```
