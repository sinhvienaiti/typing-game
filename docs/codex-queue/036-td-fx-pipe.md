# Phiếu 036 · Lời Gọi · Ống sự kiện bắn và trúng cho view 2D: `FX.fire`, `FX.hit` (chỉ mã, không trình duyệt)

**Bối cảnh:** chủ dự án duyệt chuẩn VFX nhiều lớp ngày 28/10/2026: [`docs/games/VFX_STANDARD.md`](../games/VFX_STANDARD.md) (§1.2 ý 4, §2.3, §5.4 làn V4a).

Ở Lời Gọi (`games/typing-defense`), tháp và Draconis bắn mà không có hình:
- `FX.fire` chỉ phần âm thanh đọc (`src/view/audio-min.ts:227-230`).
- `FX.hit` không ai đọc (`src/sim/systems/projectile.ts:64`).

Phiếu này làm phần **đọc**: một bộ đọc ở view, biến mỗi sự kiện thành đúng một lời gọi trên một giao diện vẽ nhỏ. Phần **vẽ** là việc của Claude ở V4a, sau phiếu này.

**Ngoại lệ có chủ ý:** điều phối viên dặn V4 chỉ đụng view. Phiếu này sửa thêm `src/main.ts` (≤ 10 dòng, đúng các chỗ ở mục 4) và biểu thức `LAZY` của `vite.config.ts`, vì chunk lười giữ trần byte (bên dưới) phải được nối ở `main.ts` và khai trong `LAZY`. `main.ts` là file hay đụng nhau khi gộp, nên không sửa gì khác trong đó.

**Sau phiếu, Claude làm (không thuộc phiếu; Codex không được ghi các chỗ này):**
1. Xem trên trình duyệt (mục Báo cáo).
2. Sửa các chú thích và tài liệu còn nói `FxView` ở `fx-2d.ts`:
   - `src/view/debug-2d.ts:767`: "(its shadow: fx-2d.ts)" thành `fx-pipe.ts`;
   - `src/view/boss-2d.ts:40`: "fx-2d.ts's FxView emits into it too";
   - `AGENTS.md` của game, dòng 161 (`FxView` in `src/view/fx-2d.ts`) và 175 (outcomes in `view/fx-2d.ts`).

   `boss-2d.ts:13` ("the fixed pool of fx-2d.ts") vẫn đúng, vì `Particles` ở lại `fx-2d.ts`.
3. Ghi byte và số dòng vào `BUILD_NOTES.md` §7, viết changelog, rồi commit kết quả phiếu.
4. Sau commit đó mới làm phần vẽ V4a trên giao diện `FxDraw`.

**Sự kiện trong vòng `CombatRing`** (`src/sim/events.ts`):
- Vòng có 8.192 ô. `written` là tổng số sự kiện đã đẩy. Mỗi ô có `kind`, `x`, `z`, `value`, `tick`.
- **`FX.fire`** (`combat.ts:86`, trong `launch`):
  - `x`, `z`: chỗ người bắn.
  - `value`: loại đạn `PROJECTILE`, gồm:
    - `arrow` 0: Archer Tower;
    - `shell` 1: Cannon Tower;
    - `bolt` 2: Lũy (Fort, ô 0) hoặc nỏ của một lời gọi;
    - `fireball` 3: Draconis, đứng ở `A.x[0]`, `A.z[0]`;
    - `wordShot` 4: Word Shot.
  - `feather` 5 không bao giờ phát `FX.fire`, vì lông lửa được thêm thẳng bằng `P.add` (`ult.ts:107`).
- **`FX.hit`** (`projectile.ts:64`):
  - `x`, `z`: chỗ mục tiêu lúc trúng.
  - `value`: 1 nếu chí mạng, 0 nếu không.
  - Chỉ có ở đòn một mục tiêu. Đòn nổ phát `FX.burst`, đã được `debug-2d.ts` vẽ.

**Hai trần phải giữ** (Claude đo ngày 28/10 trên `e49189a`, bằng một bản cài thử của chính phiếu này; `ad4df6f` có cùng `src`, `tests`, `scripts`):
1. **Gói khởi động "/"** (`scripts/bundle-budget.mjs`, ≤ 85.000 byte gzip):
   - Đang dùng 84.975 byte, còn 25 byte. BUILD_NOTES §7.10 ở `ad4df6f` ghi đúng số này.
   - Nối một chunk lười trong `main.ts` tốn khoảng 72 byte, nên vượt trần.
   - **Cách giải:** chuyển nguyên lớp `FxView` (hình của Tối Thượng, vòng của lời gọi trực tiếp, Word Shot trúng; R2) từ `fx-2d.ts` vào cùng chunk lười.
   - Bản cài thử cho:
     - "/" 83.847 byte (giảm 1.128);
     - "/?title=0" 82.396 byte;
     - chunk mới 1.947 byte.
   - Không cảnh nào của `FxView` xảy ra trước khi chunk về: Tối Thượng cần nạp đầy, lời gọi trực tiếp và Word Shot cần một đêm. `ready()` của `__td` cũng chờ chunk này.
2. **Trần dòng TypeScript** (`tests/boundary.test.ts:247-263`):
   - `src` trừ `src/kit` đang có 10.499 dòng, trần 10.500 (`BUILD_1B.md` §16, `BUILD_NOTES.md` §1.2).
   - Bản cài thử thêm 55 dòng.
   - Phiếu chỉ chạy được sau khi điều phối viên commit quyết định nới trần (mục "Điều kiện chạy").

**Thư mục làm việc:** cwd `.` là repo cha `/Users/toandx/htdocs/typing-game`, để ghi được báo cáo. Mã của phiếu nằm trong worktree `games/.wt-td-vfx` (nhánh `td-vfx`), do điều phối viên tạo trước khi chạy.
- **Nền:** nhánh `td-vfx` tách từ `main` của Lời Gọi. Lúc kiểm lại (28/10, 07:32), `main` = `a2-days` = `ad4df6f`, tức `e49189a` cộng một commit chỉ sửa tài liệu (`AGENTS.md`, changelog, `BUILD_NOTES.md` §7.10). Bản checkout chính sạch.
- **Làn `a2-days`** làm trong bản checkout chính và có thể sửa lại `src/sim`, `src/content`, `tests` ở đó bất cứ lúc nào. Phiếu này chỉ đụng view, `src/main.ts`, `vite.config.ts` và **một file test mới của riêng nó**.
- **Một mình trong worktree:** trong lúc phiếu chạy, không agent nào khác ghi vào `games/.wt-td-vfx`. Làn V4 của Claude (`VFX_STANDARD.md` §5.4) chỉ bắt đầu ở đó sau khi Claude commit kết quả phiếu.
- **Điều kiện kiểm:** mọi số trong phiếu tính trên `src`, `tests`, `scripts` của `e49189a`. Kiểm 0 lấy `e49189a` làm mốc so; mọi HEAD là `e49189a` cộng các commit chỉ sửa tài liệu (như `ad4df6f` và commit nới trần) đều đạt.
- **`node_modules`:** điều phối viên đã cài sẵn. Thiếu thì dừng; không cài.
- **Chạy lệnh của game:**
  - trong worktree: `cd games/.wt-td-vfx && <lệnh>`;
  - khóa máy: `../../.local/bin/heavy.sh`;
  - `pnpm` qua `env pnpm_config_verify_deps_before_run=warn`;
  - `tsx` qua `node --import tsx` (`pnpm exec tsx` bị sandbox chặn, phiếu 023).
- **Ngoại lệ luật chung:** luật chung cấm chạy build và test của game. Phiếu này cho phép **chỉ** các lệnh ở mục Kiểm, **chỉ** trong `games/.wt-td-vfx`.

**Điều kiện chạy (điều phối viên làm trước; Codex chỉ kiểm ở Kiểm 0):** một commit chỉ sửa tài liệu trên `td-vfx`, nới trần dòng lên ít nhất 10.574 (10.499 + 75, phần tối đa của phiếu này). Claude đề xuất đoạn sau. Đã áp lên bản `ad4df6f` của hai file: lệnh một dòng ở Kiểm 0 in `1B.V4 10900 10900`, và `tests/boundary.test.ts` đạt 17/17 với `src` của bản cài thử (10.554 dòng).
- `docs/td/BUILD_NOTES.md` §1.2:
  - đổi `Mốc đang làm: **1B.R3**.` thành `Mốc đang làm: **1B.V4**.`;
  - cùng dòng đó, đổi `từ 1B là \`BUILD_1B.md\` §16, 10.500)` thành `từ 1B là \`BUILD_1B.md\` §16: 10.500 tới hết R3, 10.900 từ 1B.V4)`;
  - thêm sau dòng `| 1B.R3 Học và dạy …`: `| 1B.V4 VFX 2D (V4a của \`docs/games/VFX_STANDARD.md\` §5.4: ống \`FX.fire\`/\`FX.hit\` của phiếu Codex 036, lóe ở tháp và Draconis, cầu lửa, trúng đòn) | 10.499 trước V4; phiếu 036 ≤ +75 | 400 | 10.900 |`.
- `docs/td/BUILD_1B.md` §16:
  - `Trần cứng 1B: **10.500**` thành `Trần cứng 1B: **10.900** (10.500 tới hết R3; +400 cho VFX 2D V4a, điều phối viên 28/10)`;
  - cuối cùng đoạn đó, `trần 1B giữ 10.500.` thành `trần 1B khi đó giữ 10.500.`.

Test chỉ đọc `Trần cứng 1B: **…**`, dòng `Mốc đang làm` và hàng của mốc, nên hai cụm sửa thêm không đổi kết quả của `boundary`.

**Chỉ được ghi:**
- `games/.wt-td-vfx/src/view/fx-pipe.ts` (mới);
- `games/.wt-td-vfx/src/view/fx-2d.ts`: chỉ bỏ khối `FxView` (dòng 113–245 ở `e49189a`) và các import chỉ khối đó dùng; sửa chú thích đầu file tối đa 3 dòng;
- `games/.wt-td-vfx/src/view/debug-2d.ts`: đúng 6 dòng: 28, 93, 157, 163, 175, 784 ở `e49189a` (mục 3);
- `games/.wt-td-vfx/src/main.ts`: phần nối chunk (mục 4), thêm tối đa 10 dòng;
- `games/.wt-td-vfx/vite.config.ts`: chỉ biểu thức `LAZY` và chú thích của nó;
- `games/.wt-td-vfx/tests/td-fx-pipe.test.ts` (mới);
- `games/.wt-td-vfx/tmp/036/**`: bằng chứng (`.gitignore` của game đã bỏ qua `tmp/`);
- `docs/codex-queue/036-report.md` ở repo cha: tiếng Việt có dấu.

**Cấm:**
- ghi ngoài danh sách trên. Trong worktree, không đụng `src/sim`, `src/content`, `src/kit`, `src/typing`, `src/ui`, `src/app`, `scripts`, các test khác, `docs`, `AGENTS.md`;
- sửa mã của `FxView`: chỉ chuyển nguyên văn. Không vẽ thêm gì: phần vẽ là của V4a;
- ghi vào bản checkout chính `games/typing-defense` (làn `a2-days` đang làm ở đó), hay vào worktree khác;
- lệnh git có ghi. Được dùng: `status`, `diff`, `log`, `show`, `branch --show-current`, `rev-parse`, `merge-base --is-ancestor`. Khi trỏ vào bản checkout chính, luôn kèm `--no-optional-locks`;
- cài gói, mạng, mở cổng, dev server, trình duyệt;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Chú thích trong mã viết bằng tiếng Anh, ngắn, theo giọng của file.

## Việc

### 1. `src/view/fx-pipe.ts` (mới, chunk lười)

```ts
/** What the pipe calls; kind: PROJECTILE of the shot (arrow, shell, bolt, fireball, wordShot); crit: 0 or 1; tick: the sim's. */
export interface FxDraw {
  muzzle(x: number, z: number, kind: number, tick: number): void; // a shot leaves its shooter at (x, z) m
  hit(x: number, z: number, crit: number, tick: number): void; // a single-target shot lands on its target at (x, z) m
}
export type FxStats = { read: number; fire: number; hit: number; lost: number };
export class FxPipe {
  constructor(ring: CombatRing, draw?: FxDraw);
  read(ring: CombatRing): void;
  stats(): FxStats;
}
```

1. **`constructor`:**
   - con trỏ riêng bắt đầu ở `ring.written`. Một bộ đọc tạo giữa trận không phát lại sự kiện cũ;
   - `draw` mặc định là một hằng cấp module, không làm gì.
2. **`read(ring)`:**
   - nếu `ring.written − con trỏ > ring.size`: cộng phần bị ghi đè (`ring.written − ring.size − con trỏ`) vào `lost`, rồi đưa con trỏ tới `ring.written − ring.size`;
   - đọc từng ô từ con trỏ tới `ring.written`. Mỗi ô: `read` + 1;
     - `FX.fire`: `fire` + 1 và **đúng một** lời gọi `draw.muzzle(x, z, value, tick)`;
     - `FX.hit`: `hit` + 1 và **đúng một** lời gọi `draw.hit(x, z, value, tick)`;
     - loại khác: không gọi gì.
3. **`stats()`:** trả **một bản sao mới** `{ read, fire, hit, lost }`, đếm từ lúc tạo. Cấp phát chỉ xảy ra khi có người hỏi.
4. **Không cấp phát mỗi khung.** Thân `read` không có: object literal, array literal, `new`, hàm mũi tên, hàm vô danh, spread, template literal, regex, hay lời gọi `map`, `filter`, `slice`, `concat`, `splice`, `push`, `unshift`, `flat`, `flatMap`, `join`, `split`, `from`, `of`, `assign`, `keys`, `values`, `entries`, `bind`, `toFixed`, `toString`.

### 2. Chuyển `FxView` vào `fx-pipe.ts`

- Chép **nguyên văn** khối từ dòng `/** A heal ring (0), a drum broken into letters (1), …` tới hết file `fx-2d.ts` của `e49189a` (dòng 113–245: kiểu `Mark`, `SCRAPS`, `ease`, `FALL_M`, lớp `FxView`), đặt sau `FxPipe`.
- Thêm các import khối đó cần vào `fx-pipe.ts`:
  - `ULT` từ `../content/rules`;
  - `RareEvent`, `CombatRing`, `FX` từ `../sim/events`;
  - `PROJECTILE` từ `../sim/stores/projectiles`;
  - `World` từ `../sim/world`;
  - `Pen` từ `./boss-2d`, và `Particles` từ `./fx-2d`, đều dạng `import type`.
- `fx-2d.ts` giữ `Particles` và `Kind` y nguyên, bỏ các import không còn dùng.

### 3. `src/view/debug-2d.ts` (đúng 6 dòng)

- Dòng 28: `import type { FxView } from "./fx-pipe";`.
- Dòng 93: `fx: FxView | null = null;`, bỏ `readonly` vì `main.ts` gán sau.
- Dòng 157, 163, 175, 784: `this.fx.` thành `this.fx?.`. Bốn lời gọi là `under`, `over`, `portrait`, `wordHit`. Ở dòng 784, lời gọi nằm trong biểu thức dấu phẩy và vẫn đúng.

### 4. `src/main.ts`

Bản cài thử của Claude (vị trí ở `e49189a`):

```ts
import type { FxPipe } from "./view/fx-pipe"; // cạnh import type của audio-min (dòng 44)
// sau `const world = session.world;` (dòng 149):
/** Shots and hits for the 2D view (ticket 036) and FxView, a chunk once the page is usable. */
const fxChunk = new Chunk("fx", () => import("./view/fx-pipe"));
let fx: FxPipe | null = null;
// trong prefetch(), sau wantSound(false):
  void fxChunk.get().then((m) => m && ((view.fx = new m.FxView(view.boss.fx)), (fx = new m.FxPipe(world.events.ring))));
// trong installDevTools: ready thêm `fxChunk.settled &&` sau `sound.settled &&`; chunks thêm `fx: fx !== null,` sau `sound: audio !== null,`
// vòng update (dòng 359):
      view.fx?.read(fresh, world, now);
      fx?.read(world.events.ring);
```

### 5. `vite.config.ts`

Trong `LAZY`, đổi `view[\\/](audio-min|folk|music)` thành `view[\\/](audio-min|folk|music|fx-pipe)`. `tests/td-chunks.test.ts` đối chiếu mọi `import()` của `main.ts` với `LAZY`.

### 6. `tests/td-fx-pipe.test.ts` (mới, vitest)

Năm ca bắt buộc:
1. **Thứ tự và loại.** Một `CombatRing` mới và một bộ ghi lời gọi. Đẩy lần lượt:
   - `FX.fire` (3,5; −2,25; arrow; tick 10);
   - `FX.spawn`;
   - `FX.fire` (−7; 4; fireball; 11);
   - `FX.hit` (4; −1; 1; 12);
   - mỗi loại `burst`, `death`, `leak`, `coin`, `block`, `soldierDown`, `fizzle`, `bossHit` một lần;
   - `FX.hit` (5,5; 6; 0; 14).

   `read` một lần. Kết quả:
   - lời gọi đúng `[muzzle 3.5 −2.25 0 10]`, `[muzzle −7 4 3 11]`, `[hit 4 −1 1 12]`, `[hit 5.5 6 0 14]`;
   - `stats()` = `{ read: 13, fire: 2, hit: 2, lost: 0 }`;
   - `read` lần hai không thêm lời gọi nào.
2. **Tạo giữa trận và tràn vòng.**
   - Đẩy 5 sự kiện, rồi mới tạo pipe; `read` cho 0 lời gọi.
   - Đẩy thêm `8192 + 100` `FX.hit` (x = i, tick = i). `read` cho `stats()` = `{ read: 8192, fire: 0, hit: 8192, lost: 100 }`.
   - Lời gọi đầu là `hit 100 0 0 100`; lời gọi cuối là `hit 8291 0 0 8291`.
3. **`stats()` là bản sao:** sửa object trả về không đổi lần hỏi sau; hai lần hỏi là hai object khác nhau.
4. **Không cấp phát trong `read`.**
   - Dùng `typescript` (devDependency có sẵn): `ts.createSourceFile` trên `src/view/fx-pipe.ts`. Tìm đúng một thân phương thức `read` của lớp `FxPipe`, duyệt cây con.
   - Cấm các nút `NewExpression`, `ObjectLiteralExpression`, `ArrayLiteralExpression`, `ArrowFunction`, `FunctionExpression`, `ClassExpression`, `SpreadElement`, `TemplateExpression`, `RegularExpressionLiteral`, và các lời gọi thuộc tính có tên trong danh sách ở mục 1.4.
   - Kết quả trên `fx-pipe.ts`: `[]`.
   - **Mẫu đối chứng**, chỉ trong bộ nhớ, không ghi ra đĩa: `class FxPipe { read(r: R) { const a = { x: 1 }; const b = [1]; r.list.push(1); for (const c of r) f(() => c); } }`. Phải ra đúng `["ObjectLiteralExpression", "ArrayLiteralExpression", "call push", "ArrowFunction"]`.
5. **Ván vàng.**
   - Chạy `runBot({ ...goldenSpec(goldenDeck(readGolden().words)), check: false, onTick })` (`tests/td/bot.ts`, `tests/td/golden.ts`).
   - Ở `onTick` đầu tiên: tạo pipe với một bộ ghi, và một con trỏ quét độc lập, đặt ở `ring.written` lúc đó.
   - Mỗi tick: con trỏ quét gom mọi `FX.fire`, `FX.hit` mới thành danh sách `seen`, cùng dạng với lời gọi.
   - Tick chia hết cho 3: gọi `pipe.read`. Sau ván: `read` thêm một lần trên `run.world.events.ring`.
   - Kết quả: danh sách lời gọi **bằng đúng** `seen`, cả thứ tự; `lost` 0; có ít nhất một `fireball`, một `arrow`, một `hit`.
   - In các số đếm bằng `console.log("036 golden counts " + JSON.stringify(…))`.
   - Bản cài thử của Claude, chạy hai lần, cùng số:

   | Mục | Số |
   |---|---|
   | `ticks` | 19.660 |
   | `muzzle` (tổng) | 133 |
   | `arrow` | 90 |
   | `shell` | 1 |
   | `bolt` | 11 |
   | `fireball` | 23 |
   | `wordShot` | 8 |
   | `feather` | 0 |
   | `hit` | 102, trong đó 12 chí mạng |
   | `stats()` | `{ read: 489, fire: 133, hit: 102, lost: 0 }` |

   File test chỉ khẳng định các bất biến trên. Các số trong bảng được so ở Kiểm 5, để test không gãy khi làn `a2-days` đổi ván vàng sau này.

## Kiểm (bắt buộc)

Chạy từ cwd `.` (repo cha), trừ khi ghi khác. Dán lệnh và dòng kết quả vào báo cáo. Script đo byte dưới đây ghi vào `games/.wt-td-vfx/tmp/036/budget-bytes.mjs` và chạy trong worktree sau mỗi lần build. Nó dùng đúng cách gom chunk của `scripts/bundle-budget.mjs`:

```js
import { readFileSync } from "node:fs";
import { gzipSync } from "node:zlib";
const PAGES = { "/": ["index.html", "src/ui/title.ts"], "/?title=0": ["index.html", "src/app/learn.ts"] };
const m = JSON.parse(readFileSync("dist/.vite/manifest.json", "utf8"));
const gz = (f) => gzipSync(readFileSync("dist/" + f)).length;
const closure = (keys) => { const seen = new Set(); const walk = (k) => { if (seen.has(k)) return; seen.add(k); for (const n of m[k].imports ?? []) walk(n); }; keys.forEach(walk); return [...new Set([...seen].map((k) => m[k].file))].filter((f) => f.endsWith(".js")); };
const out = {};
for (const [p, keys] of Object.entries(PAGES)) out[p] = closure(keys).reduce((s, f) => s + gz(f), 0);
out.fxChunk = m["src/view/fx-pipe.ts"] ? gz(m["src/view/fx-pipe.ts"].file) : null;
const text = (f) => readFileSync("dist/" + f, "utf8").split("Tối Thượng!").length - 1;
out.portraitInEntry = text(m["index.html"].file);
out.portraitInFx = m["src/view/fx-pipe.ts"] ? text(m["src/view/fx-pipe.ts"].file) : null;
console.log(JSON.stringify(out));
```

0. **Điều kiện đầu**, trước khi ghi gì vào `src`. Một điều không đạt thì dừng, ghi báo cáo, không sửa mã.
   - `git -C games/.wt-td-vfx branch --show-current` in `td-vfx`.
   - `git -C games/.wt-td-vfx merge-base --is-ancestor e49189a HEAD` thoát 0.
   - `git -C games/.wt-td-vfx diff --quiet e49189a HEAD -- src tests scripts package.json pnpm-lock.yaml tsconfig.json vite.config.ts vitest.config.ts kit.config.json` thoát 0.
   - `test -e games/.wt-td-vfx/node_modules/.bin/vitest` thoát 0.
   - **Số dòng:** `cd games/.wt-td-vfx && find src -name '*.ts' -not -path 'src/kit/*' -print0 | xargs -0 cat | wc -l` in **10499**.
   - **Trần đã nới:** lệnh sau, chạy trong worktree, in tên mốc và hai trần; cả hai trần ≥ 10.574. Với đoạn đề xuất: `1B.V4 10900 10900`. Ở `e49189a` và `ad4df6f` chưa nới: `1B.R3 10500 10500`, khi đó dừng.

     ```sh
     node -e 'const fs=require("fs");const h=/Trần cứng 1B: \*\*(\d+)\.(\d{3})\*\*/.exec(fs.readFileSync("docs/td/BUILD_1B.md","utf8"));const n=fs.readFileSync("docs/td/BUILD_NOTES.md","utf8");const m=/Mốc đang làm: \*\*(1[AB]\.\w+)\*\*/.exec(n)[1];const r=new RegExp("^\\| "+m.replace(".","\\.")+" [^|]*\\|[^|]*\\|[^|]*\\| (\\d+)\\.(\\d{3}) \\|","m").exec(n);console.log(m,h[1]+h[2],r&&r[1]+r[2])'
     ```

   - **Byte trước khi sửa:**
     - lệnh: `cd games/.wt-td-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm build && node tmp/036/budget-bytes.mjs > tmp/036/base-bytes.json`;
     - phải ra `"/":84975` và `"/?title=0":83525`, `fxChunk` null, `portraitInEntry` 1.
   - Giữ kết quả để so ở Kiểm 9:
     - `git -C games/.wt-td-vfx status --short --untracked-files=all`;
     - `git --no-optional-locks -C games/typing-defense status --short`;
     - `git status --short --untracked-files=all -- docs/codex-queue/`.
1. **`pnpm check`.** Lệnh: `cd games/.wt-td-vfx && env pnpm_config_verify_deps_before_run=warn ../../.local/bin/heavy.sh pnpm check`, thoát 0. Phải thấy:
   - `src/kit OK: 31 files match kit-manifest.json`;
   - `Test Files  33 passed (33)`;
   - `Tests` ≥ 355 passed: trước phiếu 350 trong 32 file, bản cài thử thêm 5;
   - `tsc`, `vite build` và hai dòng `bundle budget` không lỗi.

   Ba test đo thời gian có thể hỏng khi máy tải nặng (ba phiếu và các làn khác chạy cùng lúc): `tests/td-sim-perf.test.ts` (median ≤ 2 ms), ca A* của `tests/td-nav.test.ts` (median ≤ 0,5 ms), ca "lays out 20 cards" của `tests/td-lanes.test.ts` (≤ 0,3 ms). Nếu chỉ chúng hỏng, chạy lại `pnpm check` một lần và ghi cả hai kết quả.
2. **Byte sau khi sửa:** `node tmp/036/budget-bytes.mjs` trong worktree, ghi `tmp/036/after-bytes.json`.
   - `"/"` ≤ 84.975: không tăng so với nền. Bản cài thử: 83.847.
   - `"/?title=0"` ≤ 83.525. Bản cài thử: 82.396.
   - `fxChunk` là một số. Bản cài thử: 1.947.
   - `portraitInEntry` 0 và `portraitInFx` 1: `FxView` đã rời gói khởi động.
3. **Số dòng:** lệnh `find … | wc -l` ở Kiểm 0 in ≤ **10574**. Bản cài thử: 10.554. Hai test trần dòng của `tests/boundary.test.ts` đạt (nằm trong Kiểm 1).
4. **Ván vàng không đổi**, chạy trong worktree:
   - `../../.local/bin/heavy.sh node --import tsx scripts/td/golden.ts --check`;
   - `../../.local/bin/heavy.sh node --import tsx scripts/td/golden.ts --boss --check`.

   Cả hai in `"same":true` và `"content":"f2a21037"`, với `"ticks"` lần lượt 19660 và 5695.
5. **Số đếm ván vàng:** dòng `036 golden counts` (Kiểm 1, hay chạy riêng file test) khớp bảng ở mục 6.5. Nếu lệch: nền đã khác `e49189a` (Kiểm 0 đã chặn), hoặc ca 5 làm khác phiếu. Ghi rõ, không sửa số cho khớp.
6. **`FxView` chuyển nguyên văn.** Chạy trong worktree:

   ```sh
   node -e 'const {execFileSync}=require("child_process");const fs=require("fs");const old=execFileSync("git",["show","e49189a:src/view/fx-2d.ts"],{encoding:"utf8"});const block=old.slice(old.indexOf("/** A heal ring (0)")).trimEnd();console.log(block.length,fs.readFileSync("src/view/fx-pipe.ts","utf8").includes(block))'
   ```

   Lệnh in `7095 true` (độ dài khối ở `e49189a`, rồi `true`; Claude đã chạy trên bản cài thử).

   `git -C games/.wt-td-vfx diff --numstat e49189a -- src/view/fx-2d.ts src/view/debug-2d.ts vite.config.ts src/main.ts` phải cho:
   - `fx-2d.ts`: thêm ≤ 3 dòng;
   - `debug-2d.ts`: thêm 6, bỏ 6;
   - `vite.config.ts`: thêm ≤ 2, bỏ ≤ 2;
   - `main.ts`: thêm ≤ 10.

   Bản cài thử: `fx-2d.ts` 0/138, `debug-2d.ts` 6/6, `vite.config.ts` 1/1, `main.ts` 9/3.
7. **Đột biến, để chứng minh test bắt được lỗi.** Chép bản đã sửa của `fx-pipe.ts` sang `tmp/036/`. Làm lần lượt hai đột biến; sau mỗi đột biến, chạy lại file test mới và ghi tên các ca hỏng:
   - (a) `read` bỏ qua `FX.hit`. **Đạt khi ca 1, 2, 5 đều hỏng.** Bản cài thử: đúng ca 1, 2, 5 hỏng;
   - (b) thêm `const probe = { n: 1 };` làm câu đầu trong thân vòng của `read` (không đọc biến nào, nên không ném lỗi khi chạy). **Đạt khi ca 4 hỏng.** Bản cài thử: chỉ ca 4 hỏng.

   Số ca hỏng của bản cài thử chỉ để so. Nếu thêm ca khác hỏng, ghi tên và lý do vào báo cáo; đột biến vẫn đạt.

   Sau đó trả lại file, rồi `cmp` với bản đã chép: không in gì.
8. **Sim và phần khác không đổi:** `git -C games/.wt-td-vfx status --porcelain -- src/sim src/content src/kit src/typing src/ui src/app scripts tests/golden tests/td docs` không in gì.
9. **`git status` so với lúc bắt đầu:**
   - Worktree: chỉ **thêm** ` M src/main.ts`, ` M src/view/debug-2d.ts`, ` M src/view/fx-2d.ts`, ` M vite.config.ts`, `?? src/view/fx-pipe.ts`, `?? tests/td-fx-pipe.test.ts`. `tmp/` và `dist/` bị bỏ qua.
   - `games/typing-defense`: so với lúc đầu. Làn `a2-days` có thể đổi nó trong lúc chạy; chép các dòng khác vào báo cáo, phiếu này không ghi ở đó.
   - `docs/codex-queue/` ở repo cha: chỉ thêm `?? docs/codex-queue/036-report.md`. Báo cáo của phiếu khác chạy cùng lúc thì ghi tên, không tính.

## Báo cáo `docs/codex-queue/036-report.md`

- Nền thật của worktree (`git log --oneline -3`) và kết quả Kiểm 0, gồm dòng in hai trần.
- Các file đã viết hay sửa, mỗi file một dòng.
- Kết quả 10 mục kiểm (Kiểm 0–9), kèm số; với hai đột biến, tên các ca hỏng.
- Bảng byte trước và sau ("/", "/?title=0", chunk mới), số dòng trước và sau.
- Số đếm ván vàng, kết quả hai đột biến.
- Những chú thích và tài liệu còn nói `FxView` ở `fx-2d.ts` mà phiếu không cho sửa (ít nhất `debug-2d.ts:767`, `boss-2d.ts:40`, `AGENTS.md` dòng 161 và 175), kèm chỗ khác nếu thấy, để Claude sửa.
- Những chỗ phiếu chưa rõ và cách đã chọn.
- Những gì Claude phải xem trên trình duyệt:
  - `td-1b-chunks` với chunk mới;
  - chân dung "Tối Thượng!" và mưa lông lửa (`td-1b-ult`);
  - Word Shot trúng, vòng của lời gọi trực tiếp;
  - không lỗi console.

**Xong khi:** Kiểm 0–9 đạt, báo cáo đã viết. Codex không commit. Claude xem trên trình duyệt, sửa các chú thích cũ, rồi mới commit; phần vẽ V4a làm sau commit đó.
