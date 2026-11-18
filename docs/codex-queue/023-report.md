# Phiếu 023 · Thẻ tốc độ gợi ý mức Dễ cho người mới tập

Đã xong 5 việc trên `games/.wt-dh-codex`, nhánh `codex-023-easy-hint`, nền `83da970`. Thẻ trước ải gợi ý mức Dễ khi chọn ≤ 20 WPM ở mức Thường; người chơi nhận bằng ⇧↵ hoặc nút “Chơi mức Dễ”. Enter, phím số, bấm hàng giữ mức hiện tại. Không có gợi ý trong menu tạm dừng hoặc khi mức khó đã khác `normal`.

Các đường dẫn trong bảng tính từ `games/.wt-dh-codex`. Cột trình duyệt dành cho **Claude**, chạy ở **cả 1280×720 và 1920×1080**, trang **không có `?wpm`**, **xóa `localStorage` trước mỗi lượt độc lập**. Chọn hàng bằng ↑/↓ hoặc rê chuột để xem gợi ý; phím số và bấm hàng sẽ chọn ngay như trước.

| # | Việc | File:dòng | Kiểm (lệnh, kết quả) | Còn cần Claude kiểm trên trình duyệt |
|---|---|---|---|---|
| 1 | Luật gợi ý thuần, ngưỡng 20 WPM, trỏ 00 D33 (6) | `src/app/typing-pace.ts:26` | `../../.local/bin/heavy.sh pnpm check`: đạt 18 ca mới cho 15/20/25 × `normal/easy/hard` × `fromMenu` đúng/sai | Chọn hàng 15 rồi 20: dòng gợi ý và nút hiện; chọn hàng 25: dòng ẩn |
| 2 | Thẻ cập nhật gợi ý theo hàng, nút `uiButton`, lựa chọn `{ easy }` | `src/app/pace-card.ts:15`, `:33`, `:49`, `:65`, `:115` | Cùng `pnpm check`: 10/10 ca DOM giả đạt; ⇧↵/nút chọn Dễ, Enter/số/click giữ mức, hàng 35 trả `false` cho `call-early`, khôi phục ghi chú cũ | Hàng 15 và 20: dòng và nút không tràn thẻ; đổi bằng ↑/↓ và rê chuột; thử nút “Chơi mức Dễ” |
| 3 | App chỉ gợi ý trước ải, đổi mức trước dựng trận khi người chơi nhận | `src/app/app.ts:373`, `:381`, `:902` | Cùng `pnpm check`: tsc và build xanh. Đọc diff: menu không nhận hàm gợi ý; `offerEasy` đọc mức hiện tại; màn thua không sửa | ⇧↵ hàng 15 → Dễ (`__dh.state().difficulty` hoặc HUD); lượt mới Enter hàng 15 → Thường. Mở thẻ từ menu tạm dừng → không gợi ý. Thử thêm `?difficulty=easy/hard`: không gợi ý; lời mời sau hai lần thua còn nguyên |
| 4 | Test luật và thẻ tốc độ | `tests/app/typing-pace.test.ts:26`, `tests/app/pace-card.test.ts:67` | `../../.local/bin/heavy.sh pnpm check`: **433/433 test, 48/48 file**, gồm 28 ca mới; kit 73 file khớp manifest, tsc và Vite build xanh | DOM giả chỉ kiểm trạng thái và callback; Claude kiểm thao tác thật và bố cục theo các hàng trên |
| 5 | Changelog tiếng Việt, lý do và kết quả kiểm | `docs/changelog/2026-10-27-easy-hint.md:1` | Đã ghi D33 mục 6, phát hiện 15, file sửa, kiểm cuối và phần trình duyệt còn chờ; `git diff --check` đạt | Đọc diff rồi ghi bằng chứng trình duyệt trước khi xác nhận bố cục |

## Kết quả kiểm trên cây cuối

Chạy trong `games/.wt-dh-codex`, Mac mini M4, macOS, Node 24.22.0. `pnpm check` kết thúc mã 0:

```text
src/kit OK: 73 files match kit-manifest.json (kit 0.1.0, modules platform, input, vocab, learning, speech, audio, ui, tools, typing, three, feedback, balance)
 ✓ tests/app/pace-card.test.ts (10 tests) 6ms
 ✓ tests/app/typing-pace.test.ts (25 tests) 9ms
 Test Files  48 passed (48)
      Tests  433 passed (433)
$ tsc --noEmit && vite build
✓ built in 999ms
```

Lệnh bắt buộc `../../.local/bin/heavy.sh pnpm exec tsx scripts/balance/golden.ts` đã chạy nhưng CLI `tsx` bị sandbox chặn khi tạo IPC pipe: `listen EPERM`, mã thoát 1, chưa chạy script golden. Dùng cùng script với loader, vẫn dưới `heavy.sh`:

```sh
../../.local/bin/heavy.sh node --import tsx scripts/balance/golden.ts
```

Kết thúc mã 0, **4/4 ca giữ nguyên**; mọi hash định kỳ, hash cuối, số tick và log lệnh khớp. Không cập nhật golden:

```json
{
 "same": true,
 "deckChanged": false,
 "cases": [
  {
   "name": "idle",
   "change": "giữ nguyên",
   "firstMovedAtTick": null,
   "final": "61222e57 → 61222e57",
   "log": "giữ nguyên"
  },
  {
   "name": "b35-seed1",
   "change": "giữ nguyên",
   "firstMovedAtTick": null,
   "final": "8b16e8be → 8b16e8be",
   "log": "giữ nguyên"
  },
  {
   "name": "noTyping-seed2",
   "change": "giữ nguyên",
   "firstMovedAtTick": null,
   "final": "59192d7b → 59192d7b",
   "log": "giữ nguyên"
  },
  {
   "name": "sloppy-hard-off-seed3",
   "change": "giữ nguyên",
   "firstMovedAtTick": null,
   "final": "4d27a14a → 4d27a14a",
   "log": "giữ nguyên"
  }
 ]
}
```

## Phạm vi và phần bỏ qua

- Không mở dev server hoặc Chrome theo phiếu; chưa xác nhận trực quan và thao tác thật. Claude cần kiểm đủ các bước ở cột cuối.
- Chưa làm Lều Chuẩn Bị ở M0 theo D33 mục 6; không thay cân bằng hay luật mô phỏng.
- Không sửa `src/sim/**`, `src/content/**`, `src/kit/**`, golden, media, cây `games/dragon-hold`, game khác hoặc Tu Tiên.
- Không chạy lệnh Git ghi, commit, push, reset, clean hoặc stash. Hai file mới vẫn chưa được Git theo dõi; diff bổ sung bên dưới giúp Claude đọc đủ mà không cần stage.

## Diff đầy đủ

Lệnh dưới đây dùng đường dẫn từ repo cha; đầu ra được chép nguyên văn. `git diff` thường không gồm file chưa được theo dõi, nên phần sau bổ sung cả test mới và changelog bằng `git diff --no-index`.

`git -C games/.wt-dh-codex diff --stat`:

```text
 src/app/app.ts                | 13 +++++++------
 src/app/pace-card.ts          | 43 ++++++++++++++++++++++++++++++++-----------
 src/app/typing-pace.ts        |  8 +++++++-
 tests/app/typing-pace.test.ts | 12 ++++++++++--
 4 files changed, 56 insertions(+), 20 deletions(-)
```

`git -C games/.wt-dh-codex diff`:

```diff
diff --git a/src/app/app.ts b/src/app/app.ts
index 76e3da1..0a221d5 100644
--- a/src/app/app.ts
+++ b/src/app/app.ts
@@ -51,7 +51,7 @@ import { createInputRouter, type InputRouter, type KeyPanel } from "./input-rout
 import { createLearningClient, type LearningClient } from "./learning";
 import { createLoop, type Loop } from "./loop";
 import { createPaceCard } from "./pace-card";
-import { PaceMeter, clampWpm, measuredHeader, paceLabel, paceOptions, readPaceMemory, recordStage, rememberPick, sameSpeed, type PaceHeader } from "./typing-pace";
+import { PaceMeter, clampWpm, measuredHeader, offerEasy, paceLabel, paceOptions, readPaceMemory, recordStage, rememberPick, sameSpeed, type PaceHeader } from "./typing-pace";
 
 export interface App {
   dispose(): void;
@@ -370,15 +370,15 @@ export function startApp(doc: Document = document, given?: AppOptions): App {
    * From the menu the speed in use is preselected (its own row when no
    * preset has it), so Enter on the card goes back to the game.
    */
-  function askPace(onPick: (picked: PaceHeader) => void, back?: () => void): void {
+  function askPace(onPick: (picked: PaceHeader, choice?: { easy: boolean }) => void, back?: () => void): void {
     const current = back ? run?.header : undefined;
     const { options: rows, selected } = paceOptions(readPaceMemory(safeLocalStorage), current);
     const note = current ? "Chọn tốc độ khác thì ải chơi lại từ đầu." : undefined;
-    paceCard.open(rows, selected, (picked) => {
+    paceCard.open(rows, selected, (picked, choice) => {
       // Keeping the speed in use keeps its source: a ?wpm= stays the portal's.
       if (!(current && sameSpeed(picked, current))) rememberPick(safeLocalStorage, picked);
-      onPick(picked);
-    }, back, run?.header, note);
+      onPick(picked, choice);
+    }, back, run?.header, note, back ? undefined : (wpm) => offerEasy(wpm, difficulty, false));
   }
   /**
    * Pause menu → speed card: another WPM replays the stage with it; the same
@@ -899,8 +899,9 @@ export function startApp(doc: Document = document, given?: AppOptions): App {
     });
     if (header !== null) begin();
     else
-      askPace((picked) => {
+      askPace((picked, choice) => {
         header = picked;
+        if (choice?.easy) difficulty = "easy";
         begin();
       });
   });
diff --git a/src/app/pace-card.ts b/src/app/pace-card.ts
index cbfd978..dc2f5a0 100644
--- a/src/app/pace-card.ts
+++ b/src/app/pace-card.ts
@@ -12,7 +12,7 @@ import { PACE_CURRENT_KEY, type PaceHeader, type PaceOption } from "./typing-pac
 export interface PaceCard {
   readonly isOpen: boolean;
   /** Shows the rows; `onPick` gets the chosen header, `onBack` (if given) makes Esc close the card. */
-  open(options: readonly PaceOption[], selected: number, onPick: (header: PaceHeader) => void, onBack?: () => void, current?: PaceHeader, note?: string): void;
+  open(options: readonly PaceOption[], selected: number, onPick: (header: PaceHeader, choice?: { easy: boolean }) => void, onBack?: () => void, current?: PaceHeader, note?: string, easy?: (wpm: number) => boolean): void;
   /** Keyboard actions (rules.ts KEYS names); true when the card took it. */
   handleAction(action: string | null): boolean;
   close(): void;
@@ -30,6 +30,8 @@ export function createPaceCard(root: HTMLElement): PaceCard {
   const list = el(doc, "div", "dh-pacecard__list");
   const keys = el(doc, "div", "dh-pacecard__keys", "");
   const noteNode = el(doc, "div", "dh-pacecard__note", "");
+  const easyButton = uiButton(doc, "dh-pacecard__easy", () => choose(index, true));
+  easyButton.textContent = "Chơi mức Dễ";
   card.append(title, lead, list, noteNode, keys);
   setShown(card, false);
   root.append(card);
@@ -38,27 +40,43 @@ export function createPaceCard(root: HTMLElement): PaceCard {
   let items: readonly PaceOption[] = [];
   let index = 0;
   let open = false;
-  let pick: ((header: PaceHeader) => void) | null = null;
+  let pick: ((header: PaceHeader, choice?: { easy: boolean }) => void) | null = null;
   let back: (() => void) | null = null;
+  let easy: ((wpm: number) => boolean) | null = null;
+  let originalNote = "";
+  let easyShown = false;
+
+  const updateNote = (): void => {
+    const wpm = items[index]?.header.typistWpm;
+    easyShown = wpm !== undefined && (easy?.(wpm) ?? false);
+    noteNode.textContent = easyShown
+      ? "Mới tập gõ: nên chơi mức Dễ, quái thưa và chậm hơn. ⇧↵ chọn tốc độ này và chơi mức Dễ."
+      : originalNote;
+    if (easyShown) noteNode.append(" ", easyButton);
+    setShown(noteNode, easyShown || Boolean(originalNote));
+  };
 
   const select = (next: number): void => {
-    if (rows.length === 0) return;
-    index = (next + rows.length) % rows.length;
+    index = rows.length === 0 ? 0 : (next + rows.length) % rows.length;
     rows.forEach((row, k) => row.classList.toggle("is-on", k === index));
+    updateNote();
   };
 
-  const choose = (k: number): void => {
+  const choose = (k: number, useEasy = false): void => {
     const item = items[k];
-    if (!open || item === undefined) return;
+    if (!open || item === undefined || (useEasy && !easyShown)) return;
+    select(k);
     const done = pick;
     close();
-    done?.(item.header);
+    done?.(item.header, { easy: useEasy });
   };
 
   function close(): void {
     open = false;
     pick = null;
     back = null;
+    easy = null;
+    easyShown = false;
     setShown(card, false);
   }
 
@@ -66,10 +84,12 @@ export function createPaceCard(root: HTMLElement): PaceCard {
     get isOpen() {
       return open;
     },
-    open(options, selected, onPick, onBack, current, note) {
+    open(options, selected, onPick, onBack, current, note, offer) {
       items = options;
       pick = onPick;
       back = onBack ?? null;
+      easy = offer ?? null;
+      originalNote = note ?? "";
       rows = options.map((option, k) => {
         const row = uiButton(doc, "dh-pacecard__row", () => choose(k));
         row.dataset.wpm = String(option.header.typistWpm);
@@ -86,8 +106,6 @@ export function createPaceCard(root: HTMLElement): PaceCard {
         return row;
       });
       list.replaceChildren(...rows);
-      noteNode.textContent = note ?? "";
-      setShown(noteNode, Boolean(note));
       const digits = options.map((option) => option.key);
       keys.textContent = "Phím " + Math.min(...digits) + "–" + Math.max(...digits) + " chọn · ↑ ↓ rồi Enter" + (back ? " · Esc quay lại" : "");
       open = true;
@@ -99,7 +117,10 @@ export function createPaceCard(root: HTMLElement): PaceCard {
       if (action === "tilt-up") select(index - 1);
       else if (action === "tilt-down") select(index + 1);
       else if (action === "enter") choose(index);
-      else if (action === "escape") {
+      else if (action === "call-early") {
+        if (!easyShown) return false;
+        choose(index, true);
+      } else if (action === "escape") {
         if (back) {
           const done = back;
           close();
diff --git a/src/app/typing-pace.ts b/src/app/typing-pace.ts
index 13f09e7..df6e97c 100644
--- a/src/app/typing-pace.ts
+++ b/src/app/typing-pace.ts
@@ -15,7 +15,7 @@
  */
 import { blendSkill, parseSkill, serializeSkill, skillStorageKey, updateSkill, type SkillSample } from "../kit/balance";
 import { GRADE, TEMPO } from "../content/rules";
-import type { SimEvent, WordGroup } from "../content/types";
+import type { Difficulty, SimEvent, WordGroup } from "../content/types";
 
 export const PACE_GAME_ID = "dragon-hold";
 /** The last speed picked on the card. */
@@ -23,6 +23,12 @@ export const PACE_PICK_KEY = "dragon-hold.pace";
 /** Speeds the world accepts from the card or the URL (WPM, integers). */
 export const WPM_MIN = 10;
 export const WPM_MAX = 120;
+/** 00-canon.md D33 (6): suggest Easy to beginners before the stage. */
+export const EASY_HINT_WPM = 20;
+
+export function offerEasy(wpm: number, difficulty: Difficulty, fromMenu: boolean): boolean {
+  return wpm <= EASY_HINT_WPM && difficulty === "normal" && !fromMenu;
+}
 
 /** What a world is built with: E, and a and CV in permille when they were measured. */
 export interface PaceHeader {
diff --git a/tests/app/typing-pace.test.ts b/tests/app/typing-pace.test.ts
index de32101..7136d4e 100644
--- a/tests/app/typing-pace.test.ts
+++ b/tests/app/typing-pace.test.ts
@@ -1,6 +1,6 @@
 import { describe, expect, it } from "vitest";
-import { PACE_CURRENT_KEY, PACE_PICK_KEY, PACE_PRESETS, PaceMeter, clampWpm, measuredHeader, paceLabel, paceOptions, readPaceMemory, recordStage, rememberPick, sameSpeed, type PaceStorage } from "../../src/app/typing-pace";
-import type { SimEvent, WordGroup } from "../../src/content/types";
+import { PACE_CURRENT_KEY, PACE_PICK_KEY, PACE_PRESETS, PaceMeter, clampWpm, measuredHeader, offerEasy, paceLabel, paceOptions, readPaceMemory, recordStage, rememberPick, sameSpeed, type PaceStorage } from "../../src/app/typing-pace";
+import type { Difficulty, SimEvent, WordGroup } from "../../src/content/types";
 
 /** A storage over a Map, as kit/platform's SafeStorage answers. */
 function memoryStorage(): PaceStorage & { map: Map<string, string> } {
@@ -23,6 +23,14 @@ function typedWords(wpm: number, words: number, groups: readonly WordGroup[] = [
 }
 
 describe("typing pace", () => {
+  it.each([15, 20, 25].flatMap((wpm) =>
+    (["normal", "easy", "hard"] as const).flatMap((difficulty: Difficulty) =>
+      [false, true].map((fromMenu) => ({ wpm, difficulty, fromMenu })),
+    ),
+  ))("offers Easy at $wpm WPM, $difficulty, fromMenu=$fromMenu only for beginners before a Normal stage", ({ wpm, difficulty, fromMenu }) => {
+    expect(offerEasy(wpm, difficulty, fromMenu)).toBe(wpm <= 20 && difficulty === "normal" && !fromMenu);
+  });
+
   it("keeps the world's speed a whole WPM in 10–120", () => {
     expect(clampWpm(undefined)).toBeUndefined();
     expect(clampWpm(Number.NaN)).toBeUndefined();
```

`git diff --no-index --stat /dev/null tests/app/pace-card.test.ts` và `git diff --no-index /dev/null tests/app/pace-card.test.ts` (mã thoát 1: có khác biệt):

```text
 /dev/null => tests/app/pace-card.test.ts | 140 +++++++++++++++++++++++++++++++
 1 file changed, 140 insertions(+)
```

```diff
diff --git a/tests/app/pace-card.test.ts b/tests/app/pace-card.test.ts
new file mode 100644
index 0000000..02e34b7
--- /dev/null
+++ b/tests/app/pace-card.test.ts
@@ -0,0 +1,140 @@
+import { describe, expect, it, vi } from "vitest";
+import { createPaceCard } from "../../src/app/pace-card";
+import { offerEasy, paceOptions } from "../../src/app/typing-pace";
+
+// Source: tests/ui/tags-animation.test.ts. Node DOM stub; layout stays with browser QA.
+class ElementStub {
+  className = "";
+  hidden = false;
+  disabled = false;
+  dataset: Record<string, string> = {};
+  children: (ElementStub | string)[] = [];
+  private text = "";
+  private listeners = new Map<string, (() => void)[]>();
+  classList = {
+    toggle: (name: string, on: boolean) => {
+      const classes = new Set(this.className.split(" "));
+      if (on) classes.add(name); else classes.delete(name);
+      this.className = [...classes].join(" ");
+    },
+  };
+
+  constructor(readonly ownerDocument: DocumentStub) {}
+  get textContent(): string {
+    return this.text + this.children.map((child) => typeof child === "string" ? child : child.textContent).join("");
+  }
+  set textContent(value: string) { this.text = value; this.children = []; }
+  append(...nodes: (ElementStub | string)[]): void { this.children.push(...nodes); }
+  replaceChildren(...nodes: ElementStub[]): void { this.text = ""; this.children = nodes; }
+  setAttribute(): void {}
+  remove(): void {}
+  addEventListener(type: string, listener: () => void): void {
+    this.listeners.set(type, [...(this.listeners.get(type) ?? []), listener]);
+  }
+  fire(type: string): void {
+    const event = { preventDefault() {}, stopPropagation() {} };
+    for (const listener of this.listeners.get(type) ?? []) (listener as (event: unknown) => void)(event);
+  }
+}
+
+class DocumentStub {
+  elements: ElementStub[] = [];
+  createElement(): ElementStub {
+    const node = new ElementStub(this);
+    this.elements.push(node);
+    return node;
+  }
+}
+
+const hint = "Mới tập gõ: nên chơi mức Dễ, quái thưa và chậm hơn. ⇧↵ chọn tốc độ này và chơi mức Dễ.";
+
+function fixture() {
+  const doc = new DocumentStub();
+  const card = createPaceCard(new ElementStub(doc) as unknown as HTMLElement);
+  const { options } = paceOptions({ measured: null, lastPick: null });
+  const onPick = vi.fn();
+  const rowIndex = (wpm: number) => options.findIndex((option) => option.header.typistWpm === wpm);
+  const node = (name: string) => doc.elements.find((el) => el.className.split(" ").includes(name))!;
+  const note = node("dh-pacecard__note");
+  const button = node("dh-pacecard__easy");
+  const row = (wpm: number) => doc.elements.find((el) => el.dataset.wpm === String(wpm))!;
+  const open = (wpm = 15, easy: ((wpm: number) => boolean) | undefined = (speed) => offerEasy(speed, "normal", false), note?: string) =>
+    card.open(options, rowIndex(wpm), onPick, undefined, undefined, note, easy);
+  return { card, options, onPick, rowIndex, note, button, row, open };
+}
+
+describe("speed card Easy suggestion (00 D33 (6))", () => {
+  it("shows the exact hint and button at 15 and 20, hides at 25 and 35, and updates on arrows and hover", () => {
+    const f = fixture();
+    f.open();
+    expect(f.note.hidden).toBe(false);
+    expect(f.note.textContent).toBe(hint + " Chơi mức Dễ");
+    expect(f.note.children).toContain(f.button);
+    f.card.handleAction("tilt-down");
+    expect(f.note.hidden).toBe(false);
+    f.card.handleAction("tilt-down");
+    expect(f.note.hidden).toBe(true);
+    expect(f.note.children).not.toContain(f.button);
+    expect(f.card.handleAction("call-early")).toBe(false);
+    expect(f.onPick).not.toHaveBeenCalled();
+    f.row(15).fire("pointerenter");
+    expect(f.note.hidden).toBe(false);
+    f.row(35).fire("pointerenter");
+    expect(f.note.hidden).toBe(true);
+    expect(f.card.handleAction("call-early")).toBe(false);
+    f.card.handleAction("tilt-up");
+    expect(f.note.hidden).toBe(true);
+  });
+
+  it.each(["call-early", "button"])("accepts Easy explicitly through %s and closes the card", (action) => {
+    const f = fixture();
+    f.open();
+    if (action === "button") f.button.fire("click"); else expect(f.card.handleAction(action)).toBe(true);
+    expect(f.onPick).toHaveBeenCalledExactlyOnceWith(f.options[f.rowIndex(15)]!.header, { easy: true });
+    expect(f.card.isOpen).toBe(false);
+    expect(f.card.handleAction("call-early")).toBe(false);
+  });
+
+  it.each(["enter", "carry-1", "click"])("keeps the level for %s even with the hint visible", (action) => {
+    const f = fixture();
+    f.open();
+    if (action === "click") f.row(15).fire("click"); else f.card.handleAction(action);
+    expect(f.onPick).toHaveBeenCalledExactlyOnceWith(f.options[f.rowIndex(15)]!.header, { easy: false });
+  });
+
+  it("chooses the digit's row with the old level and restores the original note above 20 WPM", () => {
+    const f = fixture();
+    f.open(15, (wpm) => offerEasy(wpm, "normal", false), "Ghi chú cũ");
+    f.row(35).fire("pointerenter");
+    expect(f.note.hidden).toBe(false);
+    expect(f.note.textContent).toBe("Ghi chú cũ");
+    expect(f.card.handleAction("call-early")).toBe(false);
+    f.card.handleAction("carry-2");
+    expect(f.onPick).toHaveBeenCalledExactlyOnceWith(f.options[f.rowIndex(20)]!.header, { easy: false });
+    expect(f.note.textContent).toContain(hint);
+  });
+
+  it("reopens without a suggestion or stale Easy action from the pause menu", () => {
+    const f = fixture();
+    f.open();
+    f.card.close();
+    const onBack = vi.fn();
+    f.card.open(f.options, f.rowIndex(15), f.onPick, onBack, undefined, "Chọn tốc độ khác thì ải chơi lại từ đầu.");
+    expect(f.note.textContent).toBe("Chọn tốc độ khác thì ải chơi lại từ đầu.");
+    expect(f.note.children).not.toContain(f.button);
+    expect(f.card.handleAction("call-early")).toBe(false);
+    f.button.fire("click");
+    expect(f.onPick).not.toHaveBeenCalled();
+    expect(f.card.isOpen).toBe(true);
+    f.card.handleAction("escape");
+    expect(onBack).toHaveBeenCalledOnce();
+  });
+
+  it.each(["easy", "hard"] as const)("does not suggest when the URL already chose %s", (difficulty) => {
+    const f = fixture();
+    f.open(15, (wpm) => offerEasy(wpm, difficulty, false));
+    expect(f.note.hidden).toBe(true);
+    expect(f.card.handleAction("call-early")).toBe(false);
+    expect(f.onPick).not.toHaveBeenCalled();
+  });
+});
```

`git diff --no-index --stat /dev/null docs/changelog/2026-10-27-easy-hint.md` và `git diff --no-index /dev/null docs/changelog/2026-10-27-easy-hint.md` (mã thoát 1: có khác biệt):

```text
 .../null => docs/changelog/2026-10-27-easy-hint.md | 37 ++++++++++++++++++++++
 1 file changed, 37 insertions(+)
```

```diff
diff --git a/docs/changelog/2026-10-27-easy-hint.md b/docs/changelog/2026-10-27-easy-hint.md
new file mode 100644
index 0000000..037d8a9
--- /dev/null
+++ b/docs/changelog/2026-10-27-easy-hint.md
@@ -0,0 +1,37 @@
+# 27/10/2026 · Thẻ tốc độ gợi ý mức Dễ cho người mới tập (phiếu 023)
+
+Theo `docs/games/dragon-lane/00-canon.md` D33 mục 6 (repo cha) và phát hiện 15 trong `2026-10-27-test-pass.md`: người mới tập 15 WPM thua gần nửa số lượt ở đợt 1–2, nhưng thẻ tốc độ trước ải chưa gợi ý mức Dễ. Đây là lời mời, người chơi tự chọn (00 §4.10).
+
+## 1. Đã làm
+
+| File | Thay đổi |
+|---|---|
+| `src/app/typing-pace.ts` | Hằng `EASY_HINT_WPM = 20`, hàm thuần `offerEasy`: chỉ gợi ý khi WPM ≤ 20, mức hiện tại là `normal`, không mở từ menu tạm dừng |
+| `src/app/pace-card.ts` | `open` nhận hàm gợi ý tùy chọn; hàng đủ điều kiện hiện đúng dòng hướng dẫn và nút nhỏ “Chơi mức Dễ” bằng `uiButton`. Cập nhật khi đổi hàng bằng ↑/↓, rê chuột, phím số hoặc bấm hàng; trên 20 WPM trả về ghi chú cũ nếu có |
+| `src/app/pace-card.ts` | ⇧↵ (`call-early`) hoặc nút gợi ý chọn hàng hiện tại với `{ easy: true }`; chỉ nhận khi có gợi ý. Enter, phím số, bấm hàng vẫn trả `{ easy: false }` |
+| `src/app/app.ts` | Chỉ truyền hàm gợi ý trước ải; nhận lựa chọn Dễ thì đặt mức khó trước khi dựng trận. `?difficulty=easy` hoặc `hard` không bị gợi ý đổi mức. Menu tạm dừng và lời mời sau hai lần thua giữ hành vi cũ |
+| `tests/app/typing-pace.test.ts`, `tests/app/pace-card.test.ts` | Thêm 18 ca luật thuần (15/20/25 × ba mức × hai nguồn mở thẻ) và 10 ca thẻ với DOM giả theo cách của `tests/ui`; có ẩn ở 25/35, khôi phục ghi chú, nút, phím, rê chuột và mở lại từ menu |
+
+## 2. Kiểm trên Mac mini M4
+
+Chạy trong `games/.wt-dh-codex`, nhánh `codex-023-easy-hint`, nền `83da970`. Không mở dev server hay trình duyệt.
+
+| Lệnh | Kết quả |
+|---|---|
+| `../../.local/bin/heavy.sh pnpm check` | Đạt: kit 73 file khớp manifest; Vitest **433/433 test, 48/48 file**; `tsc --noEmit` và Vite build xanh. Hai file tốc độ/thẻ có 25 + 10 test, trong đó 28 ca mới |
+| `../../.local/bin/heavy.sh pnpm exec tsx scripts/balance/golden.ts` | CLI `tsx` bị sandbox chặn IPC pipe (`listen EPERM`), chưa vào script golden |
+| `../../.local/bin/heavy.sh node --import tsx scripts/balance/golden.ts` | Chạy cùng script bằng loader TypeScript, không cần IPC của CLI; đạt, `same: true`, `deckChanged: false`, **4/4 ca giữ nguyên** toàn bộ hash và log lệnh |
+
+Hash cuối giữ nguyên: `idle` = `61222e57`; `b35-seed1` = `8b16e8be`; `noTyping-seed2` = `59192d7b`; `sloppy-hard-off-seed3` = `4d27a14a`. Không sửa sim, content, kit hay golden.
+
+## 3. Còn Claude kiểm
+
+Ở **1280×720 và 1920×1080**, mở trang **không có `?wpm`**, xóa `localStorage` trước từng lượt độc lập:
+
+- Mức Thường mặc định: dùng ↑/↓ hoặc rê chuột chọn hàng 15 rồi 20; dòng gợi ý và nút hiện, không tràn thẻ. Hàng 25 ẩn gợi ý.
+- ⇧↵ ở hàng 15: trận chạy mức Dễ, xác nhận bằng `__dh.state().difficulty` hoặc HUD. Thử thêm nút “Chơi mức Dễ”.
+- Lượt mới, Enter ở hàng 15: trận chạy mức Thường; phím số và bấm hàng cũng giữ mức hiện tại.
+- Mở thẻ từ menu tạm dừng: không có dòng gợi ý; ghi chú đổi tốc độ còn nguyên, Enter cùng tốc độ trở lại trận.
+- Thử thêm `?difficulty=easy` và `?difficulty=hard` (không `?wpm`): không có gợi ý; màn thua vẫn mời hạ một mức sau hai lần thua như trước.
+
+Chưa xác nhận bố cục hay thao tác trong trình duyệt: phiếu chỉ mã, sandbox không mở được cổng. Chưa làm Lều Chuẩn Bị ở M0 theo D33 mục 6. Không sửa media, game khác hay cây `games/dragon-hold`.
```

Trạng thái worktree cuối:

```text
## codex-023-easy-hint
 M src/app/app.ts
 M src/app/pace-card.ts
 M src/app/typing-pace.ts
 M tests/app/typing-pace.test.ts
?? docs/changelog/2026-10-27-easy-hint.md
?? tests/app/pace-card.test.ts
```
