# Phiếu 022 · Rồng Giữ Ải · Báo cáo 27/10/2026

Đã sửa đủ 4 việc trên cây `games/dragon-hold`, HEAD `17b1547`. Cây game sạch lúc bắt đầu. Không commit, không chạy lệnh Git có ghi; không sửa sim, content, kit, golden, media hay game khác. Ngoài cây game, chỉ tạo báo cáo này ở repo cha.

Các lệnh kiểm dưới đây chạy từ `games/dragon-hold`.

| # | Việc | File:dòng | Kiểm (lệnh, kết quả) | Còn cần Claude kiểm trên trình duyệt |
| --- | --- | --- | --- | --- |
| 1 | Bỏ đếm ngược và gọi sớm trùng trên HUD; warning ghi “Đợt N sắp tới”; break có đồng hồ ghi “Nghỉ giữa đợt”, giữ lời báo đứng chờ khi mở thẻ và nhánh Enter khi không có đồng hồ. Khung học chỉ còn “Bày binh” hoặc “Nghỉ”. | `src/ui/hud.ts:418`; `src/ui/learning-frame.ts:315` | `../../.local/bin/heavy.sh pnpm check`: đạt 403/403 test, 46/46 file test; kit, `tsc --noEmit`, Vite build xanh. Test hiện có không khóa các câu cũ nên không phải sửa. | `ui-preview` ở **1280×720 và 1920×1080**, các cảnh **warning, break, prep**; xem cả break đang mở Thẻ Ôn và break chờ Enter. |
| 2 | `SIZE=1920` chọn 1920×1080, mặc định 1280×720; truyền W/H vào boot; cả ba tên ảnh có hậu tố `W x H` viết liền, ví dụ `focus-countdown-1920x1080.png`. | `scripts/visual/scenarios/dh-focus.mjs:13`, `:31`, `:58`, `:65`, `:97` | `node --check scripts/visual/scenarios/dh-focus.mjs`: exit 0. Sau việc 2, `../../.local/bin/heavy.sh pnpm check`: đạt 403/403 test, 46/46 file test; kit, tsc và build xanh. | **`SIZE=1920 dh-focus`**, 1920×1080; kiểm viewport và tên ảnh cùng hành vi focus/countdown/pause. |
| 3 | Tách dấu × vào span riêng dùng chung cho số quái theo đường, “Quái bay ×N” và “Tướng ×N”; cỡ 1,4 em, đậm 700 như chữ số. | `src/ui/styles/dh.css:790`; `src/ui/wave-card.ts:240`, `:264`, `:278`, `:286` | `../../.local/bin/heavy.sh pnpm check`: đạt 403/403 test, 46/46 file test; kit, tsc và build xanh. Test wave-card hiện có kiểm dữ liệu, không khóa HTML cũ. Đọc trực tiếp bảng glyph của font Be Vietnam Pro 700 đang cài: × cao 396 đơn vị, chữ số cao tối đa 760; 396 × 1,4 / 760 ≈ **73%**. | `ui-preview` ở **1280×720 và 1920×1080**, các cảnh **warning, break, prep**; kiểm dấu ×, độ đậm, khoảng cách và chiều cao hàng, gồm số quái bay và nhiều tướng. Tỷ lệ glyph chưa thay thế kiểm ảnh thật. |
| 4 | Span chữ đang nảy nhận `--dh-letter-delay` âm theo thời gian đã trôi từ `tag.tickAt`, CSS dùng biến làm animation-delay. Không đưa thời gian vào khóa render; giữ nhánh giảm chuyển động. Thêm 2 test hồi quy trong môi trường Node dùng fake-world và DOM giả chỉ ghi HTML. | `src/ui/tags.ts:539`, `:883`; **mới** `tests/ui/tags-animation.test.ts:79` | `../../.local/bin/heavy.sh pnpm check`: đạt 405/405 test, 47/47 file test; kit, tsc và build xanh. Test phím đúng ở 1000 ms rồi sai ở 1100 ms: span cũ nhận **−100 ms**, chữ kế tiếp vẫn hồng. Test còn kiểm phím đúng tiếp theo bắt đầu lượt mới ở 0 ms, và lỗi sau 170 ms không gắn lại hoạt ảnh đã hết. | **`tmp/mac-2026-10-27/test/recheck/repop.mjs` ở 1280×720**; gõ đúng rồi sai, nhất là 70 WPM; xem chữ không nảy lại, phím đúng liên tiếp vẫn nảy, và chế độ giảm chuyển động. |

## Kiểm trên cây cuối

- `../../.local/bin/heavy.sh pnpm check`: **exit 0**, **405/405 test, 47/47 file test**; kit khớp đủ 73 file, `tsc --noEmit` xanh, Vite build xanh. Đã chạy lại sau khi rà diff và giữ khoảng trắng trong nhãn quái bay/tướng.
- `node --check scripts/visual/scenarios/dh-focus.mjs`: **exit 0**.
- `git diff --check`: **exit 0**, không lỗi khoảng trắng.
- Lệnh golden yêu cầu `../../.local/bin/heavy.sh pnpm exec tsx scripts/balance/golden.ts` bị **exit 1 trước khi chạy script**: sandbox chặn socket IPC của CLI tsx, `listen EPERM …/tsx-501/49786.pipe`.
- Đã kiểm cùng script bằng **`../../.local/bin/heavy.sh pnpm exec node --import tsx scripts/balance/golden.ts`**, tránh socket của CLI: **exit 0**, `same: true`, `deckChanged: false`; cả bốn ca giữ nguyên mọi hash, hash cuối và nhật ký lệnh. Không dùng `--update`, không ghi lại golden.

| Ca golden | Hash cuối trước → sau | Kết quả |
| --- | --- | --- |
| `idle` | `61222e57 → 61222e57` | Giữ nguyên |
| `b35-seed1` | `8b16e8be → 8b16e8be` | Giữ nguyên |
| `noTyping-seed2` | `59192d7b → 59192d7b` | Giữ nguyên |
| `sloppy-hard-off-seed3` | `4d27a14a → 4d27a14a` | Giữ nguyên |

## Phần bỏ qua và bàn giao

Không bỏ việc mã nào trong 4 việc. Không mở dev server hoặc Chrome, không chạy kịch bản trình duyệt, đúng phạm vi phiếu 022. Chủ dự án/Claude cần đọc diff và kiểm các cảnh/cỡ ở cột cuối trước khi chấp nhận phần hiển thị. Test Node xác nhận HTML và thời gian, chưa xác nhận ảnh hay cảm nhận chuyển động. Không tạo ảnh hoặc âm thanh vì phiếu chỉ sửa mã.

## `git diff --stat`

Đầu ra nguyên văn trong **repo con `games/dragon-hold`**, so với HEAD `17b1547`:

```text
 scripts/visual/scenarios/dh-focus.mjs | 11 +++++++----
 src/ui/hud.ts                         | 15 ++++++---------
 src/ui/learning-frame.ts              |  2 +-
 src/ui/styles/dh.css                  | 13 +++++++++++++
 src/ui/tags.ts                        |  9 ++++++---
 src/ui/wave-card.ts                   | 13 ++++++++++---
 6 files changed, 43 insertions(+), 20 deletions(-)
```

Test mới chưa được Git theo dõi; không stage theo lệnh cấm Git có ghi. Bổ sung `git diff --no-index --stat /dev/null tests/ui/tags-animation.test.ts`:

```text
 /dev/null => tests/ui/tags-animation.test.ts | 110 +++++++++++++++++++++++++++
 1 file changed, 110 insertions(+)
```

Tổng phần game: **7 file, 153 dòng thêm, 20 dòng xóa**. Báo cáo này là file mới riêng ở repo cha; không đưa diff của báo cáo vào chính nó.

## `git diff` đầy đủ

Đầu ra nguyên văn `git diff` trong repo con:

```diff
diff --git a/scripts/visual/scenarios/dh-focus.mjs b/scripts/visual/scenarios/dh-focus.mjs
index 744d0dd..a90b3cf 100644
--- a/scripts/visual/scenarios/dh-focus.mjs
+++ b/scripts/visual/scenarios/dh-focus.mjs
@@ -5,10 +5,13 @@
 // 3-2-1, after a break pause it goes through. Esc opens the pause menu
 // (sim still), Esc closes it. The portal's nav and alt-tab are simulated with
 // blur and visibilitychange events on this page.
+// SIZE=1920 runs at 1920×1080 (default 1280×720).
 // Owner: integrator (LANES.md).
 import { join } from "node:path";
 import { badResources, boot, outDir, press, state, waitFor } from "./lib/dh.mjs";
 
+const [W, H] = process.env.SIZE === "1920" ? [1920, 1080] : [1280, 720];
+
 async function clickAt(page, selector) {
   const p = await page.locate(selector);
   if (!p || p.w === 0) return false;
@@ -25,7 +28,7 @@ const activeTag = (page) => page.eval("document.activeElement ? document.activeE
 export default async function (page) {
   const out = outDir("integrator");
   const r = {};
-  await boot(page, "prelearn=0", { width: 1280, height: 720 });
+  await boot(page, "prelearn=0", { width: W, height: H });
 
   // Clicks keep the keys: HUD skill slot, a strip cell, the wave card, the canvas.
   const clicks = [];
@@ -52,14 +55,14 @@ export default async function (page) {
   const t1 = (await state(page)).tick;
   await page.sleep(1500);
   const t2 = (await state(page)).tick;
-  await page.shot(join(out, "focus-veil-wave.png"));
+  await page.shot(join(out, `focus-veil-wave-${W}x${H}.png`));
   r.waveBlur = { veil: (await state(page)).veil, ticksWhileVeiled: t2 - t1 };
   // A key lifts it and starts 3-2-1; the key itself is used up.
   const kBefore = await keysNow(page);
   await press(page, "KeyA");
   await page.sleep(400);
   const during = await state(page);
-  await page.shot(join(out, "focus-countdown.png"));
+  await page.shot(join(out, `focus-countdown-${W}x${H}.png`));
   const tc1 = during.tick;
   await page.sleep(1200);
   const tc2 = (await state(page)).tick;
@@ -91,7 +94,7 @@ export default async function (page) {
   const m1 = s.tick;
   await page.sleep(1000);
   const m2 = (await state(page)).tick;
-  await page.shot(join(out, "focus-pause-menu.png"));
+  await page.shot(join(out, `focus-pause-menu-${W}x${H}.png`));
   await press(page, "Escape");
   await page.sleep(100);
   r.menu = { opened: s.menuOpen, ticksWhileOpen: m2 - m1, closed: !(await state(page)).menuOpen };
diff --git a/src/ui/hud.ts b/src/ui/hud.ts
index eb00064..3c69e50 100644
--- a/src/ui/hud.ts
+++ b/src/ui/hud.ts
@@ -1,6 +1,6 @@
 /**
- * In-wave HUD (05 §4.2): top-left gold, wave n/N, chain and the phase clock
- * (break timer, call-early bonus); top-right system buttons (pause, camera);
+ * In-wave HUD (05 §4.2): top-left gold, wave n/N, chain and phase;
+ * top-right system buttons (pause, camera);
  * bottom-left Hỏa Long (HP, shield, armour, level), skill slots Alt + 1/2 with
  * cooldowns, the urgent-word Long Hống, consumable slots Alt + 7/8, Long Nộ and
  * Viêm Đế (Alt + 5). Bạch Long stands by as a guide (00 D21). DOM, ≤ 10 % of
@@ -13,7 +13,6 @@ import { CONSUMABLES } from "../content/data/our-side";
 import { CHAIN, FLOW, HERO_LEVEL, HERO_SKILLS, OUR_SIDE, RAGE, URGENT } from "../content/rules";
 import type { ConsumableId, HeroSkillId, SimCommand, SimEvent } from "../content/types";
 import { TICK_HZ, msToTicks } from "../sim/fixed";
-import { callEarlyRoom } from "../sim/economy";
 import type { World } from "../sim/world";
 import { el, icon, keyLabel, setClass, setShown, setText, setVar, uiButton } from "./skin";
 
@@ -416,20 +415,18 @@ export function createHud(root: HTMLElement, sink: CommandSink, options: HudOpti
     setText(chainValue, String(w.words.chain));
     setText(chainMult, chainMultiplier(w.words.chain));
 
-    // Phase line: prep, warning, break clock with the call-early bonus.
+    // The wave card owns the countdown and call-early action.
     const left = phaseTicksLeft(w);
     let line = "";
     if (phase === "prep") line = `Bày binh · <b>${keyLabel("enter")}</b> để bắt đầu`;
-    else if (phase === "warning") line = `Đợt ${upcomingWave(w)} tới sau <b>${clockSeconds(left ?? 0)} s</b>`;
+    else if (phase === "warning") line = `Đợt ${upcomingWave(w)} sắp tới`;
     else if (phase === "break") {
       const held = options.heldBy?.() ?? null;
-      // No gold left in the stage's call-early pool: the line says only the call (test pass 27/10: "+0 vàng" in gold).
-      const bonus = left === null ? 0 : callEarlyBonus(left, callEarlyRoom(w));
       line = left === null
         ? `Nghỉ · <b>${keyLabel("enter")}</b> để vào đợt ${upcomingWave(w)}`
         : held !== null
-          ? `Nghỉ <b>${clockSeconds(left)} s</b> · đứng chờ khi mở ${held}`
-          : `Nghỉ <b>${clockSeconds(left)} s</b> · ${keyLabel("call-early")} gọi sớm` + (bonus > 0 ? ` <span class="dh-bonus">+${bonus} vàng</span>` : "");
+          ? `Nghỉ giữa đợt · đứng chờ khi mở ${held}`
+          : "Nghỉ giữa đợt";
     } else if (phase === "wave") line = `Đang giữ ải · đợt <b>${w.wave}</b>`;
     else if (phase === "victory") line = "Giữ ải thành công";
     else line = "Bệ Rồng thất thủ";
diff --git a/src/ui/learning-frame.ts b/src/ui/learning-frame.ts
index 30b9363..624949e 100644
--- a/src/ui/learning-frame.ts
+++ b/src/ui/learning-frame.ts
@@ -312,7 +312,7 @@ export function createLearningFrame(root: HTMLElement, gloss: Gloss, options: Le
         el.classList.toggle("is-idle", view === null);
         if (view === null) {
           word.innerHTML = resting
-            ? '<span class="dh-learn__idle">' + (world.phase === "prep" ? "Bày binh" : "Nghỉ") + ": phím 1–8 chọn món ở dải dưới</span>"
+            ? '<span class="dh-learn__idle">' + (world.phase === "prep" ? "Bày binh" : "Nghỉ") + "</span>"
             : anyWord
               ? '<span class="dh-learn__idle">Gõ chữ đầu của một từ để khóa</span>'
               : "";
diff --git a/src/ui/styles/dh.css b/src/ui/styles/dh.css
index 06371bc..e9d9262 100644
--- a/src/ui/styles/dh.css
+++ b/src/ui/styles/dh.css
@@ -787,6 +787,19 @@ body {
   height: calc(20px * var(--ui));
 }
 
+.dh-foe__count {
+  white-space: nowrap;
+  font-weight: 700;
+}
+
+.dh-foe__count .dh-count-times {
+  display: inline-block;
+  /* Be Vietnam Pro 700: × is 396 units high, digits up to 760; 1.4 gives 73 %. */
+  font-size: 1.4em;
+  font-weight: inherit;
+  line-height: 0.7;
+}
+
 .dh-foe.is-general .dh-foe__count {
   color: var(--dh-blight);
 }
diff --git a/src/ui/tags.ts b/src/ui/tags.ts
index e51f3fc..26c2cae 100644
--- a/src/ui/tags.ts
+++ b/src/ui/tags.ts
@@ -536,7 +536,7 @@ const CSS = `
 .dh-tag.is-shake .dh-tag__body { animation: dh-tag-shake 180ms linear; border-color: rgba(255, 140, 170, 0.95); }
 .dh-tag.is-tick .dh-tag__body { animation: dh-tag-tick 140ms ease-out; }
 .dh-tag.is-seep .dh-tag__body { border-color: #B58CFF; box-shadow: 0 0 0 2px rgba(150, 100, 220, 0.6), 0 0 12px rgba(150, 100, 220, 0.75), 0 2px 0 rgba(0, 0, 0, 0.55); }
-.dh-tag__word .j { display: inline-block; animation: dh-letter 170ms ease-out; }
+.dh-tag__word .j { display: inline-block; animation: dh-letter 170ms ease-out; animation-delay: var(--dh-letter-delay, 0ms); }
 .dh-tag.is-done .dh-tag__body { animation: dh-tag-done 160ms ease-in forwards; }
 .dh-tag.is-fold .dh-tag__body { animation: dh-tag-fold 200ms ease-in forwards; }
 .dh-tag.is-chip .dh-tag__body { border-style: solid; border-color: rgba(255, 244, 214, 0.7); }
@@ -880,8 +880,11 @@ export function createTags(root: HTMLElement, project: Projector, options: TagsO
     let html = "";
     for (let k = 0; k < word.text.length; k += 1) {
       // "j": the letter just typed pops up and glows once (05 §4.3 "nảy"; test passes 26–27/10: only its colour changed).
-      const cls = (k < word.typed ? "t " : "") + (k < word.tier ? "f " : "") + (pink && k === word.typed ? "p " : "") + (word.errors >= 3 && k === word.typed ? "h " : "") + (ticking && k === tag.tickIndex ? "j" : "");
-      html += cls === "" ? word.text[k] : '<span class="' + cls.trim() + '">' + word.text[k] + "</span>";
+      const popping = ticking && k === tag.tickIndex;
+      const cls = (k < word.typed ? "t " : "") + (k < word.tier ? "f " : "") + (pink && k === word.typed ? "p " : "") + (word.errors >= 3 && k === word.typed ? "h " : "") + (popping ? "j" : "");
+      // A pink/meaning change replaces the span: resume the same pop at its elapsed time.
+      const delay = popping ? ' style="--dh-letter-delay:' + (-Math.max(0, now - tag.tickAt)).toFixed(1) + 'ms"' : "";
+      html += cls === "" ? word.text[k] : '<span class="' + cls.trim() + '"' + delay + ">" + word.text[k] + "</span>";
     }
     tag.word.innerHTML = html;
     tag.icon.innerHTML = svgIcon(style.icon);
diff --git a/src/ui/wave-card.ts b/src/ui/wave-card.ts
index 1a02fdf..311eaaf 100644
--- a/src/ui/wave-card.ts
+++ b/src/ui/wave-card.ts
@@ -237,6 +237,12 @@ export function createWaveCard(root: HTMLElement, sink: CommandSink): Presenter
     banner.style.translate = "none";
   };
 
+  const countNode = (count: number): HTMLElement => {
+    const node = el(doc, "span", "dh-foe__count");
+    node.append(el(doc, "span", "dh-count-times", "×"), String(count));
+    return node;
+  };
+
   const render = (summary: WaveSummary): void => {
     lanesNode.replaceChildren(
       ...summary.lanes.map((lane) => {
@@ -255,7 +261,7 @@ export function createWaveCard(root: HTMLElement, sink: CommandSink): Presenter
             `<span class="dh-icon">${foeIcon(tally.gait, tally.color)}</span>` +
             (tally.flyer && !lane.sky ? `<span class="dh-icon dh-foe__mark">${icon("wing")}</span>` : "");
           // The short name beside the icon: a new player reads "Kiến ×6", not only a shape (the title keeps the full name).
-          chip.append(el(doc, "span", "dh-foe__name", shortFoeName(tally)), el(doc, "span", "dh-foe__count", "×" + tally.count));
+          chip.append(el(doc, "span", "dh-foe__name", shortFoeName(tally)), countNode(tally.count));
           foes.append(chip);
         }
         row.append(name, foes);
@@ -269,7 +275,7 @@ export function createWaveCard(root: HTMLElement, sink: CommandSink): Presenter
       warn.dataset.warn = "flyer";
       warn.title = "Quái bay ×" + summary.flyers + (skyNames.length ? " trên " + skyNames.join(", ") : "") + ": bẫy sàn không trúng, dùng Lưới Phóng";
       warn.innerHTML = `<span class="dh-icon">${icon("wing")}</span>`;
-      warn.append("Quái bay ×" + summary.flyers);
+      warn.append("Quái bay ", countNode(summary.flyers));
       warnNodes.push(warn);
     }
     if (summary.generals.length > 0) {
@@ -277,7 +283,8 @@ export function createWaveCard(root: HTMLElement, sink: CommandSink): Presenter
       warn.dataset.warn = "general";
       warn.title = "Tướng địch: " + summary.generals.map((general) => GENERALS[general].nameVi).join(", ");
       warn.innerHTML = `<span class="dh-icon">${icon("crown")}</span>`;
-      warn.append(summary.generals.length > 1 ? "Tướng ×" + summary.generals.length : "Tướng địch");
+      if (summary.generals.length > 1) warn.append("Tướng ", countNode(summary.generals.length));
+      else warn.append("Tướng địch");
       warnNodes.push(warn);
     }
     // "Đợt thở" (02 §5.1) is the design's word; on the card it read as "a breathing wave", so the player sees "Đợt nhẹ".
```

Bổ sung toàn bộ test mới bằng `git diff --no-index /dev/null tests/ui/tags-animation.test.ts` (mã thoát 1 nghĩa là có khác biệt):

```diff
diff --git a/tests/ui/tags-animation.test.ts b/tests/ui/tags-animation.test.ts
new file mode 100644
index 0000000..a8f77d5
--- /dev/null
+++ b/tests/ui/tags-animation.test.ts
@@ -0,0 +1,110 @@
+import { afterEach, describe, expect, it, vi } from "vitest";
+import type { FrameInfo } from "../../src/app/contracts";
+import type { SimEvent } from "../../src/content/types";
+import type { LiveWord } from "../../src/sim/words";
+import { createTags } from "../../src/ui/tags";
+import { fakeWorld } from "./fake-world";
+
+// Record the presenter's HTML in Node; layout and CSS animation are left to browser QA.
+class ElementStub {
+  className = "";
+  innerHTML = "";
+  textContent = "";
+  hidden = false;
+  dataset: Record<string, string> = {};
+  style = { opacity: "", display: "", visibility: "", transform: "", width: "", setProperty: vi.fn() };
+  offsetWidth = 80;
+  offsetHeight = 32;
+  children: ElementStub[] = [];
+  private selected = new Map<string, ElementStub>();
+  classList = {
+    contains: (name: string) => this.className.split(" ").includes(name),
+    add: (name: string) => { this.className = [...new Set([...this.className.split(" "), name])].join(" "); },
+    remove: (name: string) => { this.className = this.className.split(" ").filter((part) => part !== name).join(" "); },
+    toggle: (name: string, on: boolean) => { if (on) this.classList.add(name); else this.classList.remove(name); },
+  };
+
+  constructor(readonly ownerDocument: DocumentStub) {}
+  get firstElementChild(): ElementStub { return this.querySelector(".dh-tag__body"); }
+  querySelector(selector: string): ElementStub {
+    let node = this.selected.get(selector);
+    if (!node) { node = new ElementStub(this.ownerDocument); this.selected.set(selector, node); }
+    return node;
+  }
+  append(...nodes: ElementStub[]): void { this.children.push(...nodes); }
+  setAttribute(): void {}
+  remove(): void {}
+  getBoundingClientRect() { return { left: 0, top: 0, width: 1280, height: 720 }; }
+}
+
+class DocumentStub {
+  head = new ElementStub(this);
+  elements: ElementStub[] = [];
+  getElementById() { return null; }
+  createElement(): ElementStub {
+    const node = new ElementStub(this);
+    this.elements.push(node);
+    return node;
+  }
+  createElementNS(): ElementStub { return this.createElement(); }
+}
+
+function fixture() {
+  const doc = new DocumentStub();
+  const root = new ElementStub(doc);
+  const world = fakeWorld({ phase: "wave", wave: 1 });
+  const word: LiveWord = {
+    text: "cat", kind: "enemy", group: "new", index: 0, target: null, cluster: -1, source: 0,
+    tier: 1, typed: 0, errors: 0, firstKeyTick: -1, bornTick: 1, hint: false, asleep: false,
+  };
+  Object.assign(world.words, { live: [word], deck: { words: [] } });
+  Object.assign(world, { enemies: { list: [] } });
+  const tags = createTags(root as unknown as HTMLElement, (_x, _y, _z, out) => out, { avoid: () => [] });
+  const frame = (now: number) => tags.frame(world, { now, dt: 1 / 60, worldDt: 1 / 60, alpha: 0 } satisfies FrameInfo);
+  frame(900);
+  const node = doc.elements.find((el) => el.dataset.word === "cat")!;
+  const html = () => node.firstElementChild.querySelector(".dh-tag__word").innerHTML;
+  const key = (now: number, typed: number, result: "lock" | "advance" | "wrong") => {
+    vi.spyOn(performance, "now").mockReturnValue(now);
+    word.typed = typed;
+    if (result === "wrong") word.errors += 1;
+    tags.onEvents([{ tick: world.tick, type: "word-progress", word: 0, typed, key: result, letter: 0 } satisfies SimEvent], world);
+    frame(now);
+  };
+  return { tags, frame, html, key };
+}
+
+afterEach(() => vi.restoreAllMocks());
+
+describe("word tag letter animation", () => {
+  it("continues the right letter's pop when a wrong key rebuilds its span 100 ms later", () => {
+    const f = fixture();
+    try {
+      f.key(1000, 1, "lock");
+      expect(f.html()).toContain('class="t f j" style="--dh-letter-delay:0.0ms">c</span>');
+      const right = f.html();
+      f.frame(1050);
+      expect(f.html()).toBe(right);
+
+      f.key(1100, 1, "wrong");
+      expect(f.html()).toContain('class="p">a</span>');
+      const pop = f.html().match(/<span class="[^"]*\bj" style="--dh-letter-delay:([\d.-]+)ms">c<\/span>/);
+      expect(pop).not.toBeNull();
+      expect(Number(pop![1])).toBeCloseTo(-100, 1);
+    } finally { f.tags.dispose(); }
+  });
+
+  it("starts a fresh pop on the next right key and never revives it after 170 ms", () => {
+    const f = fixture();
+    try {
+      f.key(1000, 1, "lock");
+      f.key(1080, 2, "advance");
+      expect(f.html()).toContain('class="t f">c</span>');
+      expect(f.html()).toContain('class="t j" style="--dh-letter-delay:0.0ms">a</span>');
+      f.key(1251, 2, "wrong");
+      expect(f.html()).toContain('class="p">t</span>');
+      expect(f.html()).not.toContain(" j");
+      expect(f.html()).not.toContain("--dh-letter-delay");
+    } finally { f.tags.dispose(); }
+  });
+});
```
