# Phiếu 027 · Map Factory · Lõi tất định: `hash32`, seed theo lớp và theo ô, hạng; lint tất định (chỉ mã, không trình duyệt)

**Bối cảnh:** chủ dự án duyệt kế hoạch Map Factory ngày 27/10/2026: [`docs/tools/MAP_FACTORY.md`](../tools/MAP_FACTORY.md). Bản đồ sẽ được sinh từ spec và seed, bằng một lõi TypeScript thuần trong kit chung (`shared/game-kit/map`). Lõi phải cho ra cùng từng byte ở Node và ở mọi trình duyệt (§3.1 nguyên tắc 3 và 4, §8.5).

Phiếu này làm phần nền của lõi:
- hàm băm `hash32` và bốn hàm seed (`layerSeed`, `cellSeed`, `rankOf`, `rankKept`), đúng thuật toán ở mục "Việc";
- một test lint chặn các API không tất định trong mã lõi;
- `map/tsconfig.json` có `erasableSyntaxOnly`.

Phiếu 028 và 029 chạy ngay sau phiếu này, trong cùng worktree. Phiếu 029 dùng lại `hash32` và lint của phiếu này.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/map-codex` (nhánh `map-factory`), cwd `.`. Mọi đường dẫn tương đối trong phiếu tính từ thư mục này. Bản checkout chính `/Users/toandx/htdocs/typing-game` (tên trong phần luật chung ở đầu) không được ghi.

**Chỉ được ghi:**
- `shared/game-kit/map/tsconfig.json`;
- `shared/game-kit/map/index.ts`, `hash.ts`, `seeds.ts`;
- `shared/game-kit/map/hash.test.ts`, `seeds.test.ts`, `lint.test.ts`;
- `docs/codex-queue/027-report.md`: tiếng Việt có dấu.

**Cấm:**
- ghi ngoài danh sách trên. Trong `shared/game-kit` chỉ thêm thư mục `map/`; không sửa `package.json`, `tsconfig.json`, `vitest.config.ts`, `README.md`, `DRIFT.md` của kit;
- ghi vào `games/**`, hay bất cứ đâu trong `/Users/toandx/htdocs/typing-game`;
- cài gói (`pnpm install`, `npm install`…). Chỉ dùng thư viện chuẩn của Node và `shared/game-kit/node_modules` có sẵn: TypeScript 6.0.3, vitest 3.2.7;
- lệnh git có ghi. Được dùng: `git status`, `git diff`, `git log`, `git show`;
- mạng, cổng, dev server, trình duyệt;
- để file mẫu (mã có `enum`, mã có token cấm) trên đĩa trong `map/`: mẫu chỉ nằm trong bộ nhớ của test;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Chú thích trong mã viết bằng tiếng Anh. Import trong kit dùng đường dẫn tương đối, không có đuôi (ví dụ `./hash`), như các module khác của kit.

## Việc

### 1. `map/tsconfig.json`

Đúng nội dung này:

```json
{
  "extends": "../tsconfig.json",
  "compilerOptions": { "erasableSyntaxOnly": true },
  "include": ["./**/*.ts"]
}
```

### 2. `map/hash.ts`

```ts
export type HashPart = number | string;
export function hash32(...parts: readonly HashPart[]): number;
export function fnv1a32(bytes: ArrayLike<number>): number; // plain FNV-1a over bytes, no finaliser
export function fmix32(h: number): number;                 // murmur3 finaliser, returns uint32
```

`hash32` là FNV-1a 32 bit trên một dãy byte mã hóa từ các phần, rồi qua bộ hoàn tất `fmix32` của MurmurHash3. Mọi phép nhân dùng `Math.imul`. Kết quả là uint32 (`>>> 0`).

1. **Kiểm từng phần:**
   - số: phải là số nguyên (`Number.isInteger`) trong khoảng [−2 147 483 648; 4 294 967 295], sai thì ném `RangeError`;
   - chuỗi: mọi chuỗi; mã hóa UTF-8 bằng `TextEncoder` (một đối tượng dùng chung ở cấp module), không chuẩn hóa Unicode;
   - kiểu khác: ném `TypeError`.
2. **Mã hóa**, byte theo đúng thứ tự:
   - phần số `n`: byte `0x01`, rồi 4 byte little-endian của `w = n >>> 0`: `w & 0xff`, `(w >>> 8) & 0xff`, `(w >>> 16) & 0xff`, `w >>> 24`;
   - phần chuỗi `s`: byte `0x02`, rồi 4 byte little-endian của số byte UTF-8 `L`, rồi `L` byte UTF-8;
   - không có phần nào: dãy byte rỗng.
3. **FNV-1a:** `h = 0x811c9dc5`; với mỗi byte `b`: `h = Math.imul(h ^ b, 0x01000193)`. `fnv1a32(bytes)` trả `h >>> 0` sau byte cuối.
4. **Hoàn tất** (`fmix32`):

   ```text
   h ^= h >>> 16;  h = Math.imul(h, 0x85ebca6b);
   h ^= h >>> 13;  h = Math.imul(h, 0xc2b2ae35);
   h ^= h >>> 16;  return h >>> 0;
   ```

Không cần tạo mảng byte cho phần số: đẩy thẳng từng byte vào `h`.

Hệ quả có chủ ý (ghi trong chú thích và có test):
- `hash32(-1) === hash32(4294967295)`, vì cùng một từ 32 bit;
- `hash32("1") !== hash32(1)`, vì khác byte loại;
- `hash32("ab", "c") !== hash32("a", "bc")`, vì độ dài nằm trong mã hóa.

### 3. `map/seeds.ts`

```ts
export const RANK_SCALE = 1_000_000;
export function layerSeed(mapSeed: number, layer: string, version: number): number;
export function cellSeed(seed: number, cx: number, cz: number): number;
export function rankOf(seed: number, k: number): number;
export function rankKept(rank: number, densityPermille: number): boolean;
```

| Hàm | Bằng | Kiểm đầu vào (sai thì `RangeError`) |
|---|---|---|
| `layerSeed` | `hash32(mapSeed, layer, version)` | `layer` là chuỗi khác rỗng; `version` là số nguyên an toàn ≥ 1; `mapSeed` theo luật số của `hash32` |
| `cellSeed` | `hash32(seed, cx, cz)` | `cx`, `cz` nguyên trong [−2 147 483 648; 2 147 483 647], để ô −1 không trùng ô 4 294 967 295; `seed` theo luật của `hash32` |
| `rankOf` | `hash32(seed, "rank", k) % RANK_SCALE` | `k` nguyên trong [0; 2 147 483 647] |
| `rankKept` | `rank < densityPermille * 1000` | `rank` nguyên trong [0; 999 999]; `densityPermille` nguyên trong [0; 1000] |

Ý nghĩa (ghi trong chú thích tiếng Anh, theo §3.1 nguyên tắc 4 và §8.2):
- seed của một lớp là `layerSeed(spec.seed, tênLớp, generator.layers[tênLớp])`;
- rải theo ô: mỗi ô một seed `cellSeed(seedLớp, cx, cz)`;
- `rankOf` là hạng phần triệu của ứng viên thứ `k`. Một ứng viên có mặt ở mật độ d ‰ khi `rankKept(hạng, d)`. Vì vậy tăng mật độ chỉ thêm vật, không dời vật cũ.

### 4. `map/index.ts`

Xuất lại mọi thứ ở mục 2 và 3, kể cả kiểu `HashPart`.

### 5. Test `hash.test.ts` và `seeds.test.ts`

**12 băm vàng.** Claude tính bằng hai bản cài độc lập (JavaScript và Python), mỗi bản chạy hai lần, cùng kết quả:

| # | Gọi | Thập phân | Hex |
|---|---|---:|---|
| 1 | `hash32()` | 2872998923 | `0xab3e7c0b` |
| 2 | `hash32(0)` | 3758500711 | `0xe0062b67` |
| 3 | `hash32(1)` | 2798434716 | `0xa6ccb99c` |
| 4 | `hash32(-1)` (bằng `hash32(4294967295)`) | 3872971898 | `0xe6d8dc7a` |
| 5 | `hash32("")` | 1404927536 | `0x53bd7e30` |
| 6 | `hash32("vegetation")` | 3618500123 | `0xd7adee1b` |
| 7 | `hash32("Thác Bạc")` (NFC; trong mã viết `"Thác Bạc"`) | 2036913320 | `0x7968d4a8` |
| 8 | `layerSeed(20261027, "vegetation", 1)` | 2739991112 | `0xa350f248` |
| 9 | `layerSeed(20261028, "fields", 1)` | 3301207131 | `0xc4c46c5b` |
| 10 | `cellSeed(2739991112, 0, 0)` | 578876828 | `0x2280f59c` |
| 11 | `cellSeed(2739991112, -5, -4)` | 2270686687 | `0x8757eddf` |
| 12 | `rankOf(2270686687, 0)` | 693049 | — |

**Kiểm thêm** (cùng nguồn):
- `rankOf(2270686687, 1)` = 191962; `rankOf(2270686687, 2)` = 805752.
- Với `seed = 2739991112` và `k` = 0…9 999: có đúng **3463** hạng `< 350 000` và **5519** hạng `< 550 000`. Mọi `k` giữ ở 350 ‰ cũng được giữ ở 550 ‰.
- Vector công khai: `fnv1a32` của byte ASCII `"a"` là `0xe40c292c`, của `"foobar"` là `0xbf9cf968`, của dãy rỗng là `0x811c9dc5`; `fmix32(0)` = 0; `fmix32(1)` = `0x514e28b7`.
- Mẫu dò lỗi: `hash32(1)` mã hóa thành `01 01 00 00 00`, và `fnv1a32` của dãy đó là `0x1b95c75d`. `hash32("Thác Bạc")` mã hóa thành `02 0b 00 00 00 54 68 c3 a1 63 20 42 e1 ba a1 63`, `fnv1a32` là `0xc55e45d6`.

**Ca lỗi:**
- `hash32(1.5)`, `hash32(2 ** 32)` (viết `4294967296` trong test), `hash32(-2147483649)`, `hash32(NaN)`, `hash32(Infinity)` ném `RangeError`;
- `hash32(true as never)` ném `TypeError`;
- `layerSeed(1, "", 1)`, `layerSeed(1, "x", 0)` ném `RangeError`;
- `cellSeed(1, 2147483648, 0)` ném `RangeError`;
- `rankOf(1, -1)` ném `RangeError`;
- `rankKept(0, 1001)`, `rankKept(1000000, 5)` ném `RangeError`.

### 6. Test `lint.test.ts`: lint tất định

Mọi phần của lint nằm trong file test này: lõi không được import `typescript` lúc chạy, vì kit được chép vào game.

**File được quét:** mọi file `.ts` dưới `shared/game-kit/map/` (đệ quy, sắp theo tên), trừ file có tên kết thúc bằng `.test.ts`.
- Hàm lọc `isCoreFile(đườngDẫnTươngĐối)` tách riêng để test: `hash.ts` → đúng, `layers/fields.ts` → đúng, `edt.test.ts` → sai, `lint.test.ts` → sai.
- Hệ quả: `performance` trong `*.test.ts` được phép, để test in thời gian (§8.5 quy tắc 2).

**Bộ quét:** `ts.createScanner(ts.ScriptTarget.ES2022, true, ts.LanguageVariant.Standard, text)`, gọi `scan()` tới `EndOfFileToken`.
- Chú thích (`//`, `/* */`, `/** */`) là trivia nên không thành token. Chuỗi và template là một token literal, nên chữ bên trong không bị xét.
- Không có parser, nên cần giúp bộ quét ở hai chỗ:
  - **Template có `${…}`:** giữ một ngăn xếp. `TemplateHead` thì đẩy "tpl"; `OpenBraceToken` thì đẩy "brace"; `CloseBraceToken` mà đỉnh là "tpl" thì gọi `scanner.reScanTemplateToken(false)`: ra `TemplateTail` thì bỏ "tpl", ra `TemplateMiddle` thì giữ; `CloseBraceToken` mà đỉnh là "brace" thì bỏ "brace".
  - **Regex:** gặp `SlashToken` hay `SlashEqualsToken` mà token liền trước **không** kết thúc một biểu thức thì gọi `scanner.reScanSlashToken()`. Token kết thúc biểu thức: `Identifier`, `this`, `super`, `true`, `false`, `null`, số, chuỗi, `NoSubstitutionTemplateLiteral`, `TemplateTail`, `RegularExpressionLiteral`, `)`, `]`, `}`, `++`, `--`.

**Vi phạm** (mỗi chỗ tính một lần):
1. token `**` hoặc `**=`;
2. `Identifier` là `Date` hoặc `performance`, mà token liền trước không phải `.` hay `?.` (vì vậy `item.performance` không tính);
3. `Identifier` `Math` (token trước không phải `.` hay `?.`), rồi `.` hoặc `?.`, rồi một `Identifier` trong danh sách hàm cấm;
4. `Math` rồi `[`: không biết tên hàm, nên cấm luôn.

**Hàm cấm của `Math`:** mọi hàm mà ECMAScript cho phép tính xấp xỉ, cộng `random`: `acos acosh asin asinh atan atanh atan2 cbrt cos cosh exp expm1 hypot log log1p log10 log2 pow random sin sinh tan tanh`. Danh sách của §9.2 nằm trọn trong đó. Được dùng: `sqrt floor ceil round trunc abs sign min max imul clz32 fround`.

Báo lỗi dạng `<file>:<dòng>: <token>`.

**19 mẫu phải bắt**, mỗi mẫu đúng 1 vi phạm (mỗi dòng là một mẫu):

```text
const a = Math.sin(x);
Math.cos(x)
Math.tan(x)
Math.atan2(y, x)
Math.pow(x, 2)
Math.hypot(x, y)
Math.exp(x)
Math.log(x)
Math.cbrt(x)
Math.random()
const t = Date.now();
new Date()
performance.now()
x ** 2
x **= 2
Math['sin'](x)
const s = `${Math.sin(x)}`;
const s = `a ${b} c ${Math.pow(x, 2)} d`;
if (x) { y = 1; } const z = 2 ** 3;
```

**11 mẫu phải sạch**, 0 vi phạm. Mỗi dòng là một mẫu, riêng mẫu thứ hai là hai dòng (chú thích, xuống dòng, rồi `const a = 1;`):

```text
/** Uses no Math.sin; enumerate cells. x ** 2 Date performance */ const a = 1;
// Math.sin is banned, so is Date and **⏎const a = 1;
const s = "enumerate Math.sin Date performance **";
const s = 'Math.cos';
const t = `Math.cos ${x} Date ** performance`;
const r = /[**]/;
const r = a / b / c;
const q = (a) / 2 / (b);
const v = Math.sqrt(x) + Math.floor(y) + Math.round(z) + Math.imul(a, b) + Math.max(1, 2) + Math.min(1, 2) + Math.abs(x) + Math.trunc(x) + Math.sign(x) + Math.clz32(x);
const p = item.performance + item.Date;
const t = { a: `${`${x}`}` }; const r2 = /\*\*/g;
```

(`⏎` là ký tự xuống dòng `\n`.) Claude đã chạy thử đúng cách quét trên với TypeScript 6.0.3: cả 30 mẫu ra đúng như trên.

**Quét thật:** quét mọi file lõi trong `map/`, in danh sách file (lúc này: `hash.ts`, `index.ts`, `seeds.ts`), yêu cầu ít nhất 3 file và 0 vi phạm.

**`erasableSyntaxOnly` chặn `enum`:**
- Đọc tùy chọn: `ts.readConfigFile(<map>/tsconfig.json, ts.sys.readFile)` rồi `ts.parseJsonConfigFileContent(config, ts.sys, <thư mục map>)`. Kiểm `options.erasableSyntaxOnly === true`.
- Dịch một file ảo `<thư mục map>/__virtual__/sample.ts`, không bao giờ ghi ra đĩa: `ts.createCompilerHost(options)`, thay `getSourceFile`, `fileExists`, `readFile` cho đúng đường dẫn đó; `ts.createProgram([file], options, host)`; `ts.getPreEmitDiagnostics(program)`.
- Bốn mẫu:
  - `export enum Kind { A, B }` → có lỗi mã 1294 ("This syntax is not allowed when 'erasableSyntaxOnly' is enabled.");
  - `export namespace N { export const a = 1; }` → có lỗi 1294;
  - `export class C { constructor(private readonly a: number) {} }` → có lỗi 1294;
  - mẫu đối chứng `export const a: number = 1;` → không có lỗi nào. Mẫu này chứng minh lỗi ở ba mẫu trên không đến từ cấu hình hỏng.
- Đặt thời hạn 30 000 ms cho test này: bốn lần dịch mất khoảng 3 s trên M4.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và kết quả (dòng tổng) vào báo cáo.

1. `pnpm --dir shared/game-kit exec vitest run map` đạt. In số file test và số test.
2. `pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json` thoát 0.
3. 12 băm vàng và các mục "kiểm thêm" ở mục 5 khớp từng số (nằm trong lệnh 1).
4. Lint (nằm trong lệnh 1): danh sách file đã quét có ít nhất 3 file và 0 vi phạm; 19 mẫu cấm, mỗi mẫu đúng 1 vi phạm; 11 mẫu sạch, 0 vi phạm; ba mẫu `enum`, `namespace`, tham số thuộc tính có lỗi 1294; mẫu đối chứng 0 lỗi.
5. Không hỏng phần còn lại của kit: `pnpm --dir shared/game-kit exec vitest run` đạt (trước phiếu: 36 file, 289 test, đều đạt), và `pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit` thoát 0.
6. Chạy lại lệnh 1 lần thứ hai: cùng số test, cùng kết quả.
7. `git status --short --untracked-files=all` chỉ có file trong `shared/game-kit/map/` và `docs/codex-queue/027-report.md`.

## Báo cáo `docs/codex-queue/027-report.md`

- Các file đã viết, mỗi file một dòng nói nó làm gì.
- Kết quả bảy lệnh kiểm, kèm số.
- Bảng 12 băm vàng: giá trị test nhận được, cạnh giá trị trong phiếu.
- Những chỗ phiếu chưa rõ và cách đã chọn.

**Xong khi:** bảy lệnh kiểm đều đạt và báo cáo đã viết.
