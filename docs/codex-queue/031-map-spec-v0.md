# Phiếu 031 · Map Factory · MapSpec v0: kiểu, `validateSpec`, `specHash`, lệnh `cli validate` (chỉ mã, không trình duyệt)

**Bối cảnh:** kế hoạch [`docs/tools/MAP_FACTORY.md`](../tools/MAP_FACTORY.md) §3, §8, §9.2, duyệt ngày 27/10/2026.
- Bản đồ là **spec + seed** (§3.1 nguyên tắc 2). Người, Claude, Codex chỉ sửa chữ trong `map.spec.json`; lõi sinh bố cục từ đó.
- Phiếu này làm phần nhận spec:
  - kiểu TypeScript của MapSpec v0;
  - hàm kiểm `validateSpec`, trả danh sách lỗi `{ code, path }` với mã cố định;
  - JSON chuẩn và băm spec (`canonicalJson`, `specHash`);
  - hai spec mẫu của §8.1;
  - lệnh `node tools/map-factory/cli.mjs validate <thư mục spec>`.
- Phiếu 032 (ghép bố cục, `cli build`, `cli check`) dùng lại `validateSpec` và `specHash`.

**Spike đang chạy, nên khối lớp chỉ kiểm theo kiểu và khoảng.** Claude đang thử bố cục trên Rồng `L2-cau` (§6.2). Luật của spike sẽ đặt tham số thực vật, lối mòn, sơn đất sau này. Vì vậy:
- các khối `layers.<lớp>` được kiểm **chung**: kiểu JSON, số nguyên, khoảng theo **hậu tố tên khóa** (`…Cm`, `…Deg`, `…Ms`, `…Permille`), và ba khóa cấu trúc `id`, `proto`, `mix` (mục 3.5);
- **không** kiểm nghĩa: không bắt buộc khóa nào trong một khối, không đối chiếu `fromGameplay: "water/0"` hay `fit: "bridge/0"` với lớp chơi, không biết `groves` hay `footpaths` là gì;
- không thêm luật theo nghĩa vào các khối đó, kể cả khi thấy "hợp lý". Luật theo nghĩa thuộc các phiếu viết sau spike.

**Proto và sổ model.** Spec gọi model bằng tên `proto` (§8.2), không bằng đường dẫn file. Tên proto nằm trong file kit `registry/kits/<kit>.json`, và kit trỏ vào sổ model của phiếu 025.
- File kit đầy đủ (vai trò, cỡ, LOD, giấy phép…) để giai đoạn 4–5 (§9.2 "Để sau").
- Phiếu này chỉ tạo **file kit v0**: danh sách tên proto. Mỗi tên trỏ tới một model trong sổ 025, hoặc `null` khi chưa có model: tranh billboard của Lời Gọi, ba mốc Tripo chưa dựng, đèn và rào chưa có ảnh.
- Chuỗi kiểm: proto trong spec → có trong kit (`proto-unknown`) → model kit ghi có trong sổ 025 (CLI kiểm khi nạp kit).

**"Số lẻ" của §9.2** là số có phần thập phân (mã `not-integer`). Phiếu thêm một spec hỏng thứ bảy cho `extent.cellCm` lẻ (mã `cell-not-even`), vì lưới của phiếu 029 cần `cellCm` chẵn.

**Phụ thuộc:**
- Phiếu 027, 028, 029 đã commit trên nhánh `map-factory` (`db65b753`, `eb74f8b6`). Dùng lại:
  - `REPO_ROOT`, `FIXTURE_DIR`, `gameplayHash` trong `tools/map-factory/adapters/extract.mjs`;
  - hook `tools/map-factory/lib/ts-hook.mjs`;
  - lint tất định của 027 (`shared/game-kit/map/lint.test.ts`).
- Kiểm trước khi làm:
  - `pnpm --dir shared/game-kit exec vitest run map` đạt (6 file, 185 test);
  - `shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json` ra đúng `ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37` (`dragon-hold.L2-cau.json`) và `71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428` (`typing-defense.w1-silverfall.json`), như Kiểm 2 của phiếu 028.
- Thiếu hay sai thì dừng, ghi lý do vào báo cáo.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/map-codex` (nhánh `map-factory`), cwd `.`. Mọi đường dẫn tương đối tính từ đây.
- File của 027–029 đã commit. File phiếu, và file của phiếu chạy trước trong cùng làn, có thể chưa commit. Chúng không thuộc phiếu này: không sửa, không xóa.
- Các thư mục `games/*` trong worktree rỗng. Phiếu này không cần repo game. Riêng test của 028 (trong lệnh `node --test`) đọc repo game của bản checkout chính bằng `git archive`, chỉ đọc, như trước.
- Trước khi ghi gì, chạy `git status --short --untracked-files=all` và giữ kết quả cho Kiểm 9.

**Chỉ được ghi:**
- `shared/game-kit/map/sha256.ts`, `spec.ts`;
- `shared/game-kit/map/sha256.test.ts`, `spec.test.ts`;
- `shared/game-kit/map/index.ts`: chỉ thêm dòng `export`;
- `tools/map-factory/cli.mjs`, `tools/map-factory/lib/spec-context.mjs`;
- `tools/map-factory/registry/kits/meadow.json`, `tools/map-factory/registry/kits/pine-river.json`;
- `tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json`, `tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json`;
- `tools/map-factory/test/cli.test.mjs`;
- `tools/map-factory/test/fixtures/bad-spec/<tên>/map.spec.json`: đúng 7 thư mục ở mục 10;
- `tools/map-factory/.cache/**`: file tạm của test, ngoài Git;
- `docs/codex-queue/031-report.md`: tiếng Việt có dấu.

**Cấm:**
- sửa file của 027–029: `hash.ts`, `seeds.ts`, `raster.ts`, `edt.ts`, `map/tsconfig.json`, mọi test đã có (kể cả `lint.test.ts`), `tools/map-factory/adapters/**`, `lib/ts-hook.mjs`, `test/adapters.test.mjs`, `test/fixtures/gameplay/**`. Thấy lỗi ở đó thì ghi vào báo cáo;
- sửa sổ 025: `tools/map-factory/registry/scan-assets.mjs`, `README.md`, `out/**`, `test/**`;
- sửa phần khác của kit (`package.json`, `tsconfig.json`, `vitest.config.ts`, module khác);
- thêm luật theo nghĩa cho khối lớp (mục 3.5);
- ghi vào `games/**`, hay bất cứ đâu trong `/Users/toandx/htdocs/typing-game`;
- cài gói; lệnh git có ghi (được dùng: `status`, `diff`, `log`, `show`, `check-ignore`); mạng, cổng, dev server, trình duyệt;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

**Quy ước mã:**
- Mã lõi (`spec.ts`, `sha256.ts`) theo §8.5: không `**`, không trig, không `Date`, không `performance`, không `BigInt`, không import `node:*` hay `typescript`. Lint của 027 bắt phần lớn các chỗ này.
- Import trong kit dùng đường dẫn tương đối, không đuôi (`./sha256`).
- Import chỉ để lấy kiểu phải viết `import type`. Lý do: CLI nạp `spec.ts` bằng cách Node tự bỏ kiểu, và một import kiểu viết thường sẽ còn lại lúc chạy rồi hỏng.
- Test (`*.test.ts`, `*.test.mjs`) được dùng `node:crypto`, `node:fs`, `node:child_process`.
- `.mjs` là Node ESM thuần, chỉ thư viện chuẩn của Node 24.
- Chú thích trong mã viết bằng tiếng Anh; thông báo lỗi của CLI viết tiếng Anh.

## Việc

### 1. `map/sha256.ts`

```ts
export function sha256Hex(bytes: Uint8Array): string; // 64 lowercase hex characters
```

- SHA-256 theo FIPS 180-4, viết thuần TypeScript. Lõi chạy cả trong trình duyệt: ở đó không có `node:crypto`, còn `crypto.subtle` thì bất đồng bộ.
- Hằng `H0` (8 từ) và `K` (64 từ) viết dạng hex literal. Cộng theo modulo 2^32 bằng `| 0` hoặc `>>> 0`. Xoay phải: `(x >>> n) | (x << (32 - n))`.
- Đệm: byte `0x80`, rồi các byte `0` tới khi độ dài ≡ 56 (mod 64), rồi độ dài tính bằng **bit**, 64 bit big-endian.
  - Độ dài vào tối đa `0xffffffff` byte; dài hơn thì ném `RangeError`.
  - Nửa cao của độ dài bit là `Math.floor(len / 0x20000000)`, nửa thấp là `(len * 8) >>> 0`.
- Kết quả: 8 từ, mỗi từ `(w >>> 0).toString(16).padStart(8, "0")`, nối theo thứ tự.

### 2. `map/spec.ts`: hằng và kiểu

```ts
export const SPEC_FORMAT = "map-spec/0";
export const SPEC_LAYERS = ["fields", "height", "water", "paths", "dressing", "vegetation", "paint"] as const;
export type SpecLayerName = (typeof SPEC_LAYERS)[number];
export const SPEC_ERROR_CODES = [
  "spec-json", "type", "required", "unknown-key", "not-integer", "range", "permille-range", "pattern", "const",
  "cell-not-even", "layer-version-missing", "pin-id-format", "budget-missing", "gameplay-missing",
  "gameplay-adapter-mismatch", "gameplay-commit-mismatch", "gameplay-hash-mismatch", "kit-unknown", "proto-unknown",
] as const;
export type SpecErrorCode = (typeof SPEC_ERROR_CODES)[number];
export interface SpecError { readonly code: SpecErrorCode; readonly path: string }

export type SpecValue = number | string | boolean | readonly SpecValue[] | { readonly [key: string]: SpecValue };
export type SpecPoint = readonly [number, number]; // [x, z], integer cm
export type SpecLayerBlock = { readonly [key: string]: SpecValue };
export interface SpecRegion { readonly id: string; readonly poly: readonly SpecPoint[]; readonly reason?: string }
export type SpecPin =
  | { readonly keep: string }
  | { readonly proto: string; readonly at: SpecPoint; readonly yawDeg?: number; readonly scalePermille?: number;
      readonly variant?: string; readonly clearOnBuild?: boolean; readonly note?: string };
export interface SpecBudgetTier { readonly propTriangles: number; readonly drawCalls: number; readonly loadMs: number }
export interface MapSpec {
  readonly format: "map-spec/0";
  readonly id: string;
  readonly game: string;
  readonly title?: string;
  readonly unit: "cm";
  readonly seed: number;
  readonly generator: { readonly factory: string; readonly layers: { readonly [K in SpecLayerName]?: number } };
  readonly gameplay: { readonly adapter: string; readonly commit: string; readonly hash: string };
  readonly registry: { readonly scan: string; readonly kit: string };
  readonly extent: { readonly cellCm: number; readonly [key: string]: number };
  readonly review?: { readonly pitchesDeg: readonly number[]; readonly yawsDeg: readonly number[] };
  readonly layers: { readonly [K in SpecLayerName]?: SpecLayerBlock };
  readonly exclude?: readonly SpecRegion[];
  readonly include?: readonly SpecRegion[];
  readonly pins?: readonly SpecPin[];
  readonly budget: { readonly high: SpecBudgetTier; readonly medium?: SpecBudgetTier; readonly low?: SpecBudgetTier };
}

export interface SpecGameplayRef { readonly game: string; readonly map: string; readonly adapter: string; readonly commit: string; readonly hash: string }
export interface SpecKitRef { readonly kit: string; readonly game: string; readonly protos: readonly string[] }
export interface SpecContext { readonly gameplays?: readonly SpecGameplayRef[]; readonly kits?: readonly SpecKitRef[] }

export function validateSpec(value: unknown, context?: SpecContext): SpecError[];
export function canonicalJson(value: unknown): string;
export function specHash(spec: unknown): string;
```

`validateSpec` là hàm thuần: không đọc file, không ném lỗi với mọi giá trị JSON (kết quả của `JSON.parse`) và với mọi giá trị gốc không phải object. Spec hợp lệ thì trả mảng rỗng. Chỉ khi đó mới ép kiểu sang `MapSpec`.

### 3. `validateSpec`

#### 3.1 Đường dẫn, thứ tự, bỏ trùng

- `path` là JSON Pointer (RFC 6901). Gốc là `""`. Khóa `k` thêm `"/" + k`, sau khi thay `~` thành `~0` rồi `/` thành `~1`. Chỉ số mảng `i` thêm `"/" + i`.
  - Ví dụ: `/layers/vegetation/groves/densityPermille`, `/pins/0/keep`; khóa `"a/b~c"` trong `decals` cho `/layers/paint/decals/a~1b~0c`.
- Kết quả đã bỏ trùng (cùng `code` và `path`), rồi sắp theo `path`, hòa thì theo `code`, so bằng `<` của chuỗi (đơn vị mã UTF-16). Thứ tự duyệt vì vậy không ảnh hưởng kết quả.
- Mỗi chỗ sai báo một lỗi, không báo lỗi suy ra từ nó:
  - khóa vắng thì không kiểm giá trị của nó;
  - object chặt sai kiểu thì không xét các khóa bên trong;
  - số không nguyên thì không kiểm khoảng;
  - khóa đã báo `unknown-key` thì không kiểm giá trị của nó;
  - mảng `review.*` hay `poly` sai độ dài vẫn kiểm từng phần tử;
  - khóa `mix` sai mẫu tên vẫn kiểm trọng số của nó.

**Ba cách kiểm dùng chung** (object là `v !== null && typeof v === "object" && !Array.isArray(v)`; "có khóa" là `Object.hasOwn`):
- **Số nguyên [a; b]:** không phải `number` → `type`; không `Number.isSafeInteger` → `not-integer`; ngoài [a; b] → `range`.
- **Object chặt** với danh sách khóa cho phép và khóa bắt buộc: không phải object → `type`, dừng. Mỗi khóa ngoài danh sách → `unknown-key` ở đường dẫn khóa đó. Mỗi khóa bắt buộc vắng → `required` ở đường dẫn khóa vắng.
- **Điểm** (`at` của ghim, đỉnh của `poly`): không phải mảng đúng 2 phần tử → `type` ở đường dẫn điểm. Mỗi phần tử là số nguyên [−16 384; 16 384], giới hạn của phiếu 029.

#### 3.2 Mã lỗi

| Mã | Khi nào |
|---|---|
| `spec-json` | Chỉ CLI dùng: file không phải JSON hợp lệ. `path` là `""` |
| `type` | Sai kiểu JSON: cần object mà gặp mảng, cần chuỗi mà gặp số, gặp `null` trong khối lớp, điểm không đúng dạng. `validateSpec` nhận giá trị không phải object: `type` ở `""` |
| `required` | Thiếu khóa bắt buộc |
| `unknown-key` | Khóa không được phép ở chỗ đó |
| `not-integer` | Số không phải `Number.isSafeInteger`: có phần thập phân, `NaN`, quá lớn |
| `range` | Số nguyên ngoài khoảng; mảng có độ dài ngoài khoảng (`review.*`, `poly`) |
| `permille-range` | Khóa đuôi `Permille` không bắt đầu bằng `scale`, giá trị ngoài [0; 1000] |
| `pattern` | Chuỗi không khớp mẫu ở mục 3.3; `gameplay.adapter` không ứng với `game` |
| `const` | `format` khác `"map-spec/0"`, `unit` khác `"cm"` (kể cả khác kiểu) |
| `cell-not-even` | `extent.cellCm` là số nguyên hợp lệ nhưng lẻ |
| `layer-version-missing` | Có khối `layers.<lớp>` mà `generator.layers` không có `<lớp>` |
| `pin-id-format` | `pins[i].keep` sai dạng id ổn định |
| `budget-missing` | Thiếu `budget`, hoặc `budget` thiếu `high` |
| `gameplay-missing` | Ngữ cảnh có danh sách lớp chơi, mà không có bản trích nào cùng `game` và có `map` bằng `id` |
| `gameplay-adapter-mismatch`, `gameplay-commit-mismatch`, `gameplay-hash-mismatch` | `gameplay.adapter`, `commit`, `hash` khác bản trích |
| `kit-unknown` | Ngữ cảnh có danh sách kit, mà không có kit `registry.kit`, hoặc kit đó thuộc game khác |
| `proto-unknown` | Tên proto không có trong kit |

#### 3.3 Mẫu chuỗi

| Tên | Biểu thức chính quy | Dùng cho |
|---|---|---|
| `MAP_ID` | `^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$` | `id` (thêm: dài ≤ 64, dài hơn cũng là `pattern`); mọi khóa `id` trong khối lớp; `exclude[i].id`, `include[i].id` |
| `KEBAB` | `^[a-z0-9]+(?:-[a-z0-9]+)*$` | `game`; tên proto |
| `SEMVER` | `^(?:0\|[1-9][0-9]*)\.(?:0\|[1-9][0-9]*)\.(?:0\|[1-9][0-9]*)$` | `generator.factory` |
| `ADAPTER` | `^([a-z0-9]+(?:-[a-z0-9]+)*)@[1-9][0-9]*$`. Khi `game` là chuỗi, nhóm 1 phải bằng `game`; khác thì cũng là `pattern` | `gameplay.adapter` |
| `HEX40` | `^[0-9a-f]{40}$` | `gameplay.commit` |
| `HEX64` | `^[0-9a-f]{64}$` | `gameplay.hash` |
| `DATE` | `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` | `registry.scan` |
| `KIT` | `^[a-z0-9]+(?:-[a-z0-9]+)*@[1-9][0-9]*$` | `registry.kit` |
| `EXTENT_KEY` | `^[a-z][A-Za-z0-9]*Cm$` | khóa của `extent`; không khớp thì `unknown-key` |
| `PIN_ID` | `^[a-z]+:[a-z][A-Za-z0-9]*:c(0\|-?[1-9][0-9]*)_(0\|-?[1-9][0-9]*):(0\|[1-9][0-9]*)$`. Thêm: hai số ô (nhóm 1, 2) trong [−2 147 483 648; 2 147 483 647], `k` (nhóm 3) ≤ 2 147 483 647 | `pins[i].keep`; sai thì `pin-id-format` |

(`\|` trong bảng là dấu `|` của biểu thức.) `PIN_ID` là dạng `lớp:nguồn:c<cx>_<cz>:<k>` của §8.2 và §8.4, ví dụ `veg:groves:c-5_-4:2`. Số không có số 0 thừa ở đầu, không có `-0`.

#### 3.4 Khóa cấp đầu

Spec là object chặt. Khóa cho phép: `format`, `id`, `game`, `title`, `unit`, `seed`, `generator`, `gameplay`, `registry`, `extent`, `review`, `layers`, `exclude`, `include`, `pins`, `budget`. Khóa bắt buộc (vắng → `required`): `format`, `id`, `game`, `unit`, `seed`, `generator`, `gameplay`, `registry`, `extent`, `layers`. Vắng `budget` → `budget-missing` ở `/budget`. Khóa khác, ví dụ `locks` (định dạng để giai đoạn 5), → `unknown-key`.

| Khóa | Kiểm |
|---|---|
| `format` | khác `"map-spec/0"` → `const` |
| `id` | chuỗi (`type`), `MAP_ID` và dài ≤ 64 (`pattern`) |
| `game` | chuỗi, `KEBAB` |
| `title` | chuỗi |
| `unit` | khác `"cm"` → `const` |
| `seed` | số nguyên [0; 4 294 967 295] |
| `generator` | object chặt `{ factory, layers }`, cả hai bắt buộc. `factory`: chuỗi, `SEMVER`. `layers`: object (`type`); khóa ngoài 7 tên lớp của `SPEC_LAYERS` → `unknown-key`; giá trị nguyên [1; 1 000 000] |
| `gameplay` | object chặt `{ adapter, commit, hash }`, cả ba bắt buộc; chuỗi theo `ADAPTER`, `HEX40`, `HEX64` |
| `registry` | object chặt `{ scan, kit }`, cả hai bắt buộc; chuỗi theo `DATE`, `KIT` |
| `extent` | object (`type`), không có danh sách khóa cố định, vì hai game dùng khóa khác nhau (`fieldHalfCm`, `skirtCm` ở Lời Gọi; `playRadiusCm`, `worldHalfCm` ở Rồng). Khóa không khớp `EXTENT_KEY` → `unknown-key`. Giá trị nguyên [1; 16 384]. Vắng `cellCm` → `required` ở `/extent/cellCm`. `cellCm` nguyên trong khoảng mà lẻ → `cell-not-even` |
| `review` | object chặt `{ pitchesDeg, yawsDeg }`, cả hai bắt buộc. Mỗi khóa là mảng (`type`) dài 1…12 (sai → `range` ở đường dẫn mảng). Phần tử nguyên: `pitchesDeg` [0; 90], `yawsDeg` [0; 359] |
| `layers` | object (`type`). Với mỗi khóa `k`: ngoài 7 tên lớp → `unknown-key`, không xét tiếp. Khi `generator` và `generator.layers` là object mà `generator.layers` không có `k` → `layer-version-missing` ở `/layers/k`. Giá trị không phải object → `type`; còn lại kiểm chung (3.5) |
| `exclude`, `include` | mảng (`type`). Mỗi phần tử là object chặt `{ id, poly, reason }`, bắt buộc `id`, `poly`. `id`: chuỗi, `MAP_ID`. `poly`: mảng (`type`), ít hơn 3 điểm → `range` ở `/…/poly`; mỗi đỉnh là một điểm. `reason`: chuỗi |
| `pins` | mảng (`type`). Mỗi phần tử phải là object (`type`). **Có khóa `keep`:** object chặt `{ keep }`; `keep` là chuỗi (`type`) khớp `PIN_ID` (`pin-id-format`). **Không có `keep`:** object chặt `{ proto, at, yawDeg, scalePermille, variant, clearOnBuild, note }`, bắt buộc `proto`, `at`. `proto` là tên proto (như khóa `proto` ở 3.5); `at` là điểm; `yawDeg` nguyên [−360; 360]; `scalePermille` nguyên [1; 10 000]; `variant`, `note` là chuỗi; `clearOnBuild` là boolean (`type`) |
| `budget` | object (`type`). Khóa ngoài `high`, `medium`, `low` → `unknown-key`. Vắng `high` → `budget-missing` ở `/budget/high`. Mỗi tier là object chặt `{ propTriangles, drawCalls, loadMs }`, cả ba bắt buộc, nguyên lần lượt trong [1; 100 000 000], [1; 100 000], [1; 60 000] |

#### 3.5 Khối lớp: kiểm chung (không theo nghĩa)

Duyệt đệ quy giá trị của mỗi `layers.<lớp>`:
- `null`, hay giá trị không phải JSON → `type`.
- boolean, chuỗi: hợp lệ.
- số: không `Number.isSafeInteger` → `not-integer`. Số nguyên có **khóa đơn vị** thì kiểm khoảng theo bảng dưới; không có khóa đơn vị thì hợp lệ.
- mảng: duyệt từng phần tử, giữ khóa đơn vị của mảng.
- object: với từng khóa `k`:
  - `k === "id"`: giá trị là chuỗi (`type`) khớp `MAP_ID` (`pattern`). Không duyệt tiếp.
  - `k === "proto"`: giá trị là **tên proto**: chuỗi (`type`) khớp `KEBAB` (`pattern`). Hợp lệ thì ghi lại tên và đường dẫn, để kiểm kit (3.6).
  - `k === "mix"`: giá trị là object (`type`). Mỗi khóa của nó là một tên proto: khớp `KEBAB` (sai → `pattern` ở đường dẫn của khóa đó), hợp lệ thì ghi lại. Mỗi giá trị là trọng số nguyên [1; 1000].
  - khóa khác: duyệt giá trị. Khóa đơn vị của giá trị là `k` nếu `k` có hậu tố đơn vị, nếu không thì giữ khóa đơn vị đang có.

**Khóa đơn vị** của một số là khóa gần nhất phía trên nó có hậu tố đơn vị. Ví dụ: `"skipNearCm": { "gate": 800 }` thì 800 theo `skipNearCm`; `"radiusCm": [500, 1000]` thì cả hai số theo `radiusCm`; `"skipNearCm": { "gateMs": 70000 }` thì theo `gateMs`.

| Hậu tố (phân biệt hoa thường) | Khoảng | Mã khi ngoài khoảng |
|---|---|---|
| `Permille`, khóa bắt đầu bằng `scale` | [1; 10 000] (cỡ 1100 ‰ của ghim mẫu là hợp lệ) | `range` |
| `Permille`, khóa khác | [0; 1000] (mật độ là xác suất: §8.2, `rankKept` của 027) | `permille-range` |
| `Deg` | [−360; 360] | `range` |
| `Cm` | [−100 000; 100 000] (âm được, ví dụ đáy lòng chảo) | `range` |
| `Ms` | [0; 60 000] | `range` |

Xét hậu tố theo đúng thứ tự trong bảng.

Đây là toàn bộ luật của khối lớp. Không thêm khóa bắt buộc. Không kiểm `min ≤ max` của các cặp như `count: [6, 9]`. Không đối chiếu chuỗi trong `on`, `from`, `to`, `fit`, `under`, `fromGameplay`, `where`, `kind`.

#### 3.6 Kiểm theo ngữ cảnh

Không có `context` thì chỉ kiểm cấu trúc (3.4, 3.5). CLI đọc file và đưa ngữ cảnh vào (mục 8).

- **Lớp chơi:** chỉ xét khi có `context.gameplays`, `game` là chuỗi khớp `KEBAB`, `id` là chuỗi khớp `MAP_ID`, và `gameplay` là object. Lấy phần tử **đầu tiên** có `game === spec.game` và `map === spec.id`.
  - Không có → `gameplay-missing` ở `/gameplay`.
  - Có: so từng trường đã đạt mẫu của mình. `adapter` (đạt `ADAPTER`, nhóm 1 bằng `game`) khác → `gameplay-adapter-mismatch`. `commit` (đạt `HEX40`) khác → `gameplay-commit-mismatch`. `hash` (đạt `HEX64`) khác → `gameplay-hash-mismatch`. Đường dẫn là `/gameplay/<trường>`.
- **Kit:** chỉ xét khi có `context.kits`, `registry` là object và `registry.kit` là chuỗi đạt `KIT`. Lấy kit có `kit === registry.kit`.
  - Không có, hoặc `kit.game !== spec.game` → `kit-unknown` ở `/registry/kit`. Khi đó không kiểm proto.
  - Có: mỗi tên proto đã ghi lại (khóa `proto` trong khối lớp, khóa của `mix`, `pins[i].proto`) mà không có trong `kit.protos` → `proto-unknown` ở đường dẫn của nó.

### 4. `canonicalJson` và `specHash`

`canonicalJson(value)` theo đúng luật của phiếu 028 §5, để hai bên ra cùng byte:
- số: phải `Number.isSafeInteger`, sai thì ném `TypeError`; viết `String(v)`; `-0` viết `0`;
- chuỗi, `true`, `false`, `null`: `JSON.stringify`;
- mảng: `"[" + các phần tử nối bằng "," + "]"`, giữ thứ tự; ô trống của mảng thưa ném `TypeError`;
- object: khóa sắp bằng `Object.keys(o).sort()`, mỗi cặp `JSON.stringify(khóa) + ":" + giá trị`, nối bằng `","`, trong `{}`;
- giá trị khác (`undefined`, hàm, `bigint`…) ném `TypeError`. Không có khoảng trắng.

`specHash(spec) = sha256Hex(utf8(canonicalJson(spec)))`, với `utf8` là `TextEncoder` dùng chung ở cấp module. Không chuẩn hóa Unicode.

**Số vàng** (Claude tính bằng hai bản cài độc lập, JavaScript với `node:crypto` và Python với `hashlib`, mỗi bản chạy hai lần, cùng kết quả):

| Spec | Số byte UTF-8 của `canonicalJson` | `specHash` |
|---|---:|---|
| `w1-silverfall` | 3189 | `d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16` |
| `L2-cau` | 1145 | `e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83` |

Để dò lỗi: `canonicalJson` của `w1-silverfall` mở đầu bằng `{"budget":{"high":{"drawCalls":40,"loadMs":300,"propTriangles":550000},"medium":`; của `L2-cau` mở đầu bằng `{"budget":{"high":{"drawCalls":40,"loadMs":300,"propTriangles":550000}},"extent":{"cellCm":50,"playRadiusCm":3200,`.

**Kiểm chéo với 028:** với mỗi fixture lớp chơi, bỏ hai khóa `commit` và `hash`, rồi `sha256Hex(utf8(canonicalJson(phần còn lại)))` phải bằng trường `hash` của fixture (`7faeaa7c…4b23`, `c852b4d7…659a`). Phép này kiểm cùng lúc `canonicalJson` và `sha256Hex` của lõi với `node:crypto` của 028.

### 5. `map/index.ts`

Thêm `export` cho mọi tên ở mục 1 và 2, kể cả các kiểu (`export { …, type MapSpec, … } from "./spec"`). Không đổi các dòng đã có.

### 6. Hai spec mẫu

Chép nguyên văn hai khối JSON của §8.1 trong `docs/tools/MAP_FACTORY.md` của worktree, bằng lệnh, không gõ lại:
- `tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json`: khối đầu của §8.1, từ dòng `{` tới dòng `}` (hôm nay là dòng 489–568), cộng một `\n` cuối file. Ví dụ `sed -n '489,568p' docs/tools/MAP_FACTORY.md > …`;
- `tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json`: khối "Rồng `L2-cau`" (hôm nay là dòng 574–590), cộng một `\n` cuối file.

Kiểm bằng `shasum -a 256`:
- `w1-silverfall`: `4c60f45b2eaaf8d8b56124eb0ffad60102510f4dacfd8d033a52a60b2da799a0`;
- `L2-cau`: `2d4620366e5942352f8eee34a7e2dc853b8746e85bdfbea1964dee0f43e26030`.

Lệch thì tìm lại khối theo nội dung (tài liệu có thể đã dời dòng). Nếu khối đã đổi nội dung thì dừng và ghi vào báo cáo; không sửa số cho khớp.

Hai spec khớp với fixture của 028: `gameplay.adapter`, `commit`, `hash` của `w1-silverfall` là `typing-defense@1`, `10ce627ff4e1c91f29e808cb658c086f51bd97d6`, `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23`; của `L2-cau` là `dragon-hold@1`, `83da970eacbf85ea64da89f62a4d1b6622bc5c7b`, `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a`. CLI kiểm điều này (3.6).

### 7. Hai file kit v0

Đúng từng byte như hai khối dưới, mỗi file kết thúc bằng một `\n`. Proto của `meadow@1` là 14 tên mà spec `w1-silverfall` dùng, cộng bốn món của bộ tranh `meadow` ở §6.5 (`reed-clump`, `rock-medium`, `wildflowers`, `tree-stump`). Mọi `asset` là `null`, vì chưa có model nào. Proto của `pine-river@1` là 12 model pine-river trong sổ 025 của Rồng. `asset` không mang tiền tố `<game>:` như §8.2 của kế hoạch, vì game đã ghi ở cấp kit (`game`).

`tools/map-factory/registry/kits/meadow.json` (sha256 `ffe6a5eac17e103509f29e90615bc31e57e551c9a7f8177a644ab6dca8b954da`):

```json
{
  "format": "map-kit/0",
  "kit": "meadow@1",
  "game": "typing-defense",
  "protos": {
    "almond-tree": { "asset": null },
    "bamboo-clump": { "asset": null },
    "canopy-block": { "asset": null },
    "fence-segment": { "asset": null },
    "fern": { "asset": null },
    "lamp-post": { "asset": null },
    "mountain-pine": { "asset": null },
    "raspberry-bush": { "asset": null },
    "reed-clump": { "asset": null },
    "rock-medium": { "asset": null },
    "rock-small": { "asset": null },
    "rotten-log": { "asset": null },
    "silverfall-cliff": { "asset": null },
    "tall-grass": { "asset": null },
    "tree-stump": { "asset": null },
    "watchtower": { "asset": null },
    "wildflowers": { "asset": null },
    "wooden-bridge": { "asset": null }
  }
}
```

`tools/map-factory/registry/kits/pine-river.json` (sha256 `f8e574c5e4abc773ec3204f912af218d05f24ce13257773db974e9d8bc0ee73a`):

```json
{
  "format": "map-kit/0",
  "kit": "pine-river@1",
  "game": "dragon-hold",
  "protos": {
    "bridge-old": { "asset": "m0b/props/pine-river-bridge-old/pine-river-bridge-old" },
    "bush-blossom": { "asset": "m0b/props/pine-river-bush-blossom/pine-river-bush-blossom" },
    "bush-moss": { "asset": "m0b/props/pine-river-bush-moss/pine-river-bush-moss" },
    "log": { "asset": "m0b/props/pine-river-log/pine-river-log" },
    "pine-round": { "asset": "m0b/props/pine-river-pine-round/pine-river-pine-round" },
    "pine-tall": { "asset": "m0b/props/pine-river-pine-tall/pine-river-pine-tall" },
    "pine-young": { "asset": "m0b/props/pine-river-pine-young/pine-river-pine-young" },
    "river-stones": { "asset": "m0b/props/pine-river-river-stones/pine-river-river-stones" },
    "rock-boulder": { "asset": "m0b/props/pine-river-rock-boulder/pine-river-rock-boulder" },
    "rock-slab": { "asset": "m0b/props/pine-river-rock-slab/pine-river-rock-slab" },
    "stump": { "asset": "m0b/props/pine-river-stump/pine-river-stump" },
    "tree-violet": { "asset": "m0b/props/pine-river-tree-violet/pine-river-tree-violet" }
  }
}
```

`asset` là id runtime trong sổ 025 bỏ đuôi tier. Nó hợp lệ khi `registry/out/assets.<game>.json` có một mục `source: "runtime"` với `id` bằng `asset + ".high"`, và một mục với `id` bằng `asset + ".medium"`. Claude đã kiểm: cả 12 model đều có đủ hai tier.

### 8. `tools/map-factory/lib/spec-context.mjs`

| Tên | Làm gì |
|---|---|
| `KITS_DIR` | `<REPO_ROOT>/tools/map-factory/registry/kits` |
| `REGISTRY_OUT_DIR` | `<REPO_ROOT>/tools/map-factory/registry/out` |
| `loadGameplays(dir = FIXTURE_DIR)` | Đọc mọi `*.json` trong `dir`, sắp theo tên. Mỗi file: `JSON.parse`; `gameplayHash(bản trích)` của 028 phải bằng trường `hash`. Trả `{ gameplays, problems }`, `gameplays` là mảng `{ game, map, adapter, commit, hash }` |
| `checkKit(fileName, kit, assets)` | Hàm thuần, trả mảng lỗi (chuỗi). `assets` là mảng `assets` của sổ 025 cho `kit.game`, hoặc `null` khi không có sổ. Luật ở dưới |
| `loadKits(dir = KITS_DIR, registryDir = REGISTRY_OUT_DIR)` | Đọc mọi `*.json` trong `dir`, sắp theo tên; nạp sổ `assets.<game>.json` cho game của từng kit; gọi `checkKit`. Hai file cùng `kit` cũng là lỗi. Trả `{ kits, problems }`, `kits` là mảng `{ kit, game, protos: Object.keys(protos) }` |

Luật của `checkKit`. Mỗi lỗi là một chuỗi có tên file và lý do.
1. `format` khác `"map-kit/0"`.
2. `kit` không khớp `KIT`, hoặc `fileName` khác `<phần trước @>.json`.
3. `game` không khớp `KEBAB`, hoặc `assets` là `null`.
4. `protos` không phải object, hoặc rỗng.
5. Mỗi khóa của `protos` khớp `KEBAB`. Mỗi giá trị là object có đúng một khóa `asset`, giá trị là chuỗi hoặc `null`.
6. `asset` là chuỗi thì `assets` phải có hai mục runtime `<asset>.high` và `<asset>.medium` (mục 7). Thiếu một hay cả hai tier tính là **một** lỗi cho proto đó.

Lỗi đọc file hay `JSON.parse` cũng vào `problems`, không ném.

### 9. `tools/map-factory/cli.mjs`

```text
node tools/map-factory/cli.mjs validate <thư mục spec>
```

- Dòng đầu file: `import './lib/ts-hook.mjs';`. Nạp `spec.ts` bằng `await import(...)` động, **sau** dòng đó. Lý do: import tĩnh được phân giải trước khi hook đăng ký, nên `./sha256` không đuôi sẽ hỏng. Đây cũng là cách các bộ đọc của 028 nạp mã game.
- Tham số phải đúng là `validate` và một thư mục. Sai thì in cách dùng ra stderr, thoát **2**. Riêng `build` và `check` in "not implemented in map-spec/0 (ticket 032)", cũng thoát 2.
- `<thư mục>/map.spec.json` phải là file có thật. Không có thì stderr, thoát 2.
- `JSON.parse` lỗi: stdout đúng một dòng `error spec-json ""`, thoát **1**.
- `loadKits()` và `loadGameplays()` có lỗi: in từng lỗi ra stderr, thoát 2. Đây là môi trường hỏng, không phải spec hỏng.
- `validateSpec(spec, { gameplays, kits })` có lỗi: stdout mỗi lỗi một dòng `error <code> <JSON.stringify(path)>`, theo thứ tự hàm trả về; thoát **1**.
- Không lỗi: stdout đúng một dòng `ok <specHash>`, thoát **0**.
- Mọi dòng stdout kết thúc bằng `\n`. Dùng `process.exitCode`, không gọi `process.exit()` khi còn ghi stdout.
- Không ghi file nào.

### 10. Bảy spec hỏng

Mỗi spec hỏng là file của một spec mẫu (mục 6) với **đúng một** chỗ sửa văn bản. Chuỗi "trước" xuất hiện đúng một lần trong file gốc. Làm bằng lệnh hay script trong RAM, rồi kiểm sha256.

| Thư mục `test/fixtures/bad-spec/…` | Gốc | Sửa (trước → sau) | Lỗi duy nhất (`code`, `path`) | sha256 của file |
|---|---|---|---|---|
| `fractional-number` | w1 | `"wobbleCm": 40,` → `"wobbleCm": 40.5,` | `not-integer`, `/layers/water/streams/0/wobbleCm` | `193be3e3f5a1f460009efd4e1353c3dce9cccc7e8f4fb267354e6397e61630dd` |
| `density-over-1000` | w1 | `"densityPermille": 600,` → `"densityPermille": 1200,` | `permille-range`, `/layers/vegetation/groves/densityPermille` | `3b9eb49201b8dd62b3f65da14f9f9381ab3bb6fd18a1518dd96e4cbfef39e39a` |
| `unknown-proto` | L2 | `"densityPermille": 650 }` → `"densityPermille": 650, "mix": { "pine-tall": 3, "pine-giant": 1 } }` | `proto-unknown`, `/layers/vegetation/groves/mix/pine-giant` | `559d3eda596ff2551cdb07096c53c467dfa5a10ffb769228966e145348fc1254` |
| `gameplay-hash-mismatch` | L2 | `de45d9659a"` → `de45d9659b"` (ký tự cuối của `gameplay.hash`) | `gameplay-hash-mismatch`, `/gameplay/hash` | `7436981da69c115b957d741b40c57016481a3125b6fe6282a67645596d689090` |
| `bad-pin-id` | w1 | `"veg:groves:c-5_-4:2"` → `"veg:groves:c-5-4:2"` | `pin-id-format`, `/pins/0/keep` | `c8cd22b18ae7389ccf38846a7cfb4facdc23694f3411001024415dc5ad48705b` |
| `missing-budget` | L2 | bỏ dòng `  "budget": { "high": { "propTriangles": 550000, "drawCalls": 40, "loadMs": 300 } }` và dấu phẩy cuối dòng liền trước (`  },` thành `  }`). Chuỗi trước: `  },\n  "budget": { … } }\n}\n`; chuỗi sau: `  }\n}\n` | `budget-missing`, `/budget` | `a099fd032dae6ad16b6df644cb4e1f45532a5e13de1820eb08da7498fc45346e` |
| `odd-cell` | L2 | `"cellCm": 50,` → `"cellCm": 45,` | `cell-not-even`, `/extent/cellCm` | `ab61bbfd7da596abdc38bdc433cfade00f8d6a6850ba1ccd304e9173569355ea` |

Spec hỏng giữ `game` và `id` của gốc, nên CLI tìm đúng bản trích và đúng kit. Ở `unknown-proto`, `pine-tall` có trong kit (và trong sổ 025), còn `pine-giant` thì không.

### 11. Test vitest: `sha256.test.ts`, `spec.test.ts`

**`sha256.test.ts`:**
- vector FIPS: `""` → `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`; `"abc"` → `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`; `"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"` → `248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1`; một triệu chữ `a` → `cdc76e5c9914fb9281a1c7e284d73e67f1809a48a497200e046d39ccc7112cd0`;
- độ dài sát chỗ đệm: 55, 56, 57, 63, 64, 65, 119, 120, 128 byte, so với `node:crypto`;
- 200 dãy byte có seed: dãy `k` dùng `new RngStream(hash32("sha256", k))` (`../platform/rng`), dài 0…1000 byte. So với `node:crypto` từng dãy. In số dãy.

**`spec.test.ts`.** Đọc file bằng `node:fs`, đường dẫn tương đối từ `map/` (`../../../tools/map-factory/…`), như `fields-sample.test.ts`. Ngữ cảnh dựng trong test từ hai fixture lớp chơi và hai file kit (đọc JSON, không gọi `spec-context.mjs`).

1. **`canonicalJson`:**
   - `{ b: 1, B: 2, a: 3, _: 4 }` → `{"B":2,"_":4,"a":3,"b":1}`;
   - `{ b: 1, a: [true, null, "x"] }` → `{"a":[true,null,"x"],"b":1}`;
   - `-0` → `0`;
   - `"Thác Bạc"` → `"Thác Bạc"` (không thoát thành `\u`);
   - chuỗi `a"b` + xuống dòng → `"a\"b\n"`;
   - `1.5`, `NaN`, `Infinity`, `2 ** 53` (viết `9007199254740992`), `undefined`, `{ a: undefined }`, `[1, , 2]` ném `TypeError`.
2. **Kiểm chéo với 028** (mục 4): hai fixture.
3. **Số vàng:** `specHash` và số byte của hai spec mẫu, đọc từ `tools/map-factory/maps/…`.
4. **Mẫu sạch:** `validateSpec(mẫu, ngữ cảnh)` và `validateSpec(mẫu)` đều trả `[]`, với cả hai mẫu.
5. **Bảy spec hỏng** (đọc từ file): mỗi spec trả **đúng** một lỗi như bảng mục 10, với ngữ cảnh. Không ngữ cảnh: `gameplay-hash-mismatch` và `unknown-proto` trả `[]`; năm spec còn lại vẫn trả đúng lỗi của mình.
6. **Bảng đột biến.** Mỗi dòng: `s = structuredClone(mẫu)` (w1 hay L2), chạy câu lệnh, rồi `validateSpec(s, ngữ cảnh)` phải bằng **đúng** mảng một phần tử ở cột cuối (dòng 30: mảng rỗng).

| # | Mẫu | Đột biến | `code` | `path` |
|---|---|---|---|---|
| 1 | w1 | `delete s.format` | `required` | `/format` |
| 2 | w1 | `s.format = "map-spec/1"` | `const` | `/format` |
| 3 | w1 | `s.unit = "m"` | `const` | `/unit` |
| 4 | w1 | `s.seed = -1` | `range` | `/seed` |
| 5 | w1 | `s.seed = 1.5` | `not-integer` | `/seed` |
| 6 | w1 | `s.seed = "1"` | `type` | `/seed` |
| 7 | w1 | `s.id = "w1 silverfall"` | `pattern` | `/id` |
| 8 | w1 | `s.title = 5` | `type` | `/title` |
| 9 | w1 | `s.locks = {}` | `unknown-key` | `/locks` |
| 10 | w1 | `s.generator.layers.foliage = 1` | `unknown-key` | `/generator/layers/foliage` |
| 11 | w1 | `s.generator.layers.paint = 0` | `range` | `/generator/layers/paint` |
| 12 | w1 | `delete s.generator.layers.paint` | `layer-version-missing` | `/layers/paint` |
| 13 | w1 | `s.generator.factory = "0.1"` | `pattern` | `/generator/factory` |
| 14 | w1 | `s.gameplay.commit = s.gameplay.commit.toUpperCase()` | `pattern` | `/gameplay/commit` |
| 15 | w1 | `s.gameplay.adapter = "dragon-hold@1"` | `pattern` | `/gameplay/adapter` |
| 16 | w1 | `s.gameplay.adapter = "typing-defense@2"` | `gameplay-adapter-mismatch` | `/gameplay/adapter` |
| 17 | w1 | `s.gameplay.commit = "84d0ac116b396df2b341ed4330461653a05fd8b2"` | `gameplay-commit-mismatch` | `/gameplay/commit` |
| 18 | w1 | `s.id = "w1-silverfall-b"` | `gameplay-missing` | `/gameplay` |
| 19 | w1 | `s.registry.kit = "meadow"` | `pattern` | `/registry/kit` |
| 20 | w1 | `s.registry.kit = "meadow@2"` | `kit-unknown` | `/registry/kit` |
| 21 | w1 | `s.registry.kit = "pine-river@1"` | `kit-unknown` | `/registry/kit` |
| 22 | w1 | `s.registry.scan = "27/10/2026"` | `pattern` | `/registry/scan` |
| 23 | w1 | `delete s.extent.cellCm` | `required` | `/extent/cellCm` |
| 24 | w1 | `s.extent.skirtCm = 0` | `range` | `/extent/skirtCm` |
| 25 | w1 | `s.extent.field = 4800` | `unknown-key` | `/extent/field` |
| 26 | w1 | `s.review.yawsDeg = [0, 360]` | `range` | `/review/yawsDeg/1` |
| 27 | w1 | `s.review.pitchesDeg = []` | `range` | `/review/pitchesDeg` |
| 28 | w1 | `s.layers.water.streams[0].wobbleCm = null` | `type` | `/layers/water/streams/0/wobbleCm` |
| 29 | w1 | `s.layers.height.stamps[0].heightCm = 100001` | `range` | `/layers/height/stamps/0/heightCm` |
| 30 | w1 | `s.layers.height.stamps[0].heightCm = -300` | (không lỗi) | — |
| 31 | w1 | `s.layers.dressing.landmarks[3].yawDeg = 400` | `range` | `/layers/dressing/landmarks/3/yawDeg` |
| 32 | w1 | `s.layers.dressing.along[0].skipNearCm.gate = 100001` | `range` | `/layers/dressing/along/0/skipNearCm/gate` |
| 33 | w1 | `s.layers.dressing.along[0].skipNearCm.gateMs = 70000` | `range` | `/layers/dressing/along/0/skipNearCm/gateMs` |
| 34 | w1 | `s.layers.vegetation.edge.densityPermille = -1` | `permille-range` | `/layers/vegetation/edge/densityPermille` |
| 35 | w1 | `s.layers.vegetation.groves.radiusCm = [500, 1000.5]` | `not-integer` | `/layers/vegetation/groves/radiusCm/1` |
| 36 | w1 | `s.layers.paint.tintNoiseCm = 100001` | `range` | `/layers/paint/tintNoiseCm` |
| 37 | w1 | `s.layers.paint.decals["a/b~c"] = 1.5` | `not-integer` | `/layers/paint/decals/a~1b~0c` |
| 38 | w1 | `s.pins[1].scalePermille = 0` | `range` | `/pins/1/scalePermille` |
| 39 | w1 | `s.pins[1].scalePermille = 10001` | `range` | `/pins/1/scalePermille` |
| 40 | w1 | `s.layers.dressing.along[0].proto = "Lamp-Post"` | `pattern` | `/layers/dressing/along/0/proto` |
| 41 | w1 | `s.layers.dressing.along[0].proto = 5` | `type` | `/layers/dressing/along/0/proto` |
| 42 | w1 | `s.layers.dressing.along[0].proto = "lamp-pots"` | `proto-unknown` | `/layers/dressing/along/0/proto` |
| 43 | w1 | `s.layers.vegetation.decorTrees.mix["almond-tree"] = 0` | `range` | `/layers/vegetation/decorTrees/mix/almond-tree` |
| 44 | w1 | `s.layers.vegetation.gameplayTrees.mix["mountain-pine"] = 2.5` | `not-integer` | `/layers/vegetation/gameplayTrees/mix/mountain-pine` |
| 45 | w1 | `s.layers.vegetation.clutter.mix.Fern = 1` | `pattern` | `/layers/vegetation/clutter/mix/Fern` |
| 46 | w1 | `s.layers.vegetation.groves.mix = ["fern"]` | `type` | `/layers/vegetation/groves/mix` |
| 47 | w1 | `s.layers.height.stamps[0].id = "rainbow hill"` | `pattern` | `/layers/height/stamps/0/id` |
| 48 | w1 | `s.exclude[0].poly = s.exclude[0].poly.slice(0, 2)` | `range` | `/exclude/0/poly` |
| 49 | w1 | `s.exclude[0].poly[0] = [1, 2, 3]` | `type` | `/exclude/0/poly/0` |
| 50 | w1 | `s.exclude[0].poly[0] = [16385, 3200]` | `range` | `/exclude/0/poly/0/0` |
| 51 | w1 | `s.pins[0].keep = "veg:groves:c-0_-4:2"` | `pin-id-format` | `/pins/0/keep` |
| 52 | w1 | `s.pins[0].keep = "veg:groves:c-5_-4:2147483648"` | `pin-id-format` | `/pins/0/keep` |
| 53 | w1 | `delete s.pins[1].at` | `required` | `/pins/1/at` |
| 54 | w1 | `s.pins[1].colour = "red"` | `unknown-key` | `/pins/1/colour` |
| 55 | w1 | `s.pins[0].note = "x"` | `unknown-key` | `/pins/0/note` |
| 56 | w1 | `delete s.budget.high.drawCalls` | `required` | `/budget/high/drawCalls` |
| 57 | w1 | `s.budget.ultra = { propTriangles: 1, drawCalls: 1, loadMs: 1 }` | `unknown-key` | `/budget/ultra` |
| 58 | w1 | `delete s.budget.high` | `budget-missing` | `/budget/high` |
| 59 | w1 | `s.layers.foliage = {}` | `unknown-key` | `/layers/foliage` |
| 60 | w1 | `s.layers.paint = []` | `type` | `/layers/paint` |
| 61 | L2 | `s.layers.dressing = {}` | `layer-version-missing` | `/layers/dressing` |
| 62 | L2 | `s.gameplay.adapter = "typing-defense@1"` | `pattern` | `/gameplay/adapter` |
| 63 | L2 | `delete s.gameplay` | `required` | `/gameplay` |

7. **Nhiều lỗi, sắp và bỏ trùng.** w1 với `s.seed = 1.5; s.unit = "m"; delete s.budget; s.locks = 1; s.pins[0].keep = "veg"; s.layers.vegetation.groves.densityPermille = 1001`, không ngữ cảnh, ra đúng sáu lỗi theo thứ tự: `budget-missing /budget`, `permille-range /layers/vegetation/groves/densityPermille`, `unknown-key /locks`, `pin-id-format /pins/0/keep`, `not-integer /seed`, `const /unit`.
8. **Đầu vào không phải object:** `validateSpec([1])`, `validateSpec(null)`, `validateSpec("x")` trả `[{ code: "type", path: "" }]`, không ném.
9. **Mã lỗi:** `SPEC_ERROR_CODES` có đúng 19 mã như mục 2. Mọi mã trừ `spec-json` xuất hiện ít nhất một lần trong các ca 5–8.

Claude đã cài thử đúng luật mục 3 ở thư mục nháp, chạy hai lần: hai mẫu sạch, bảy spec hỏng và 63 dòng đột biến ra đúng như trên. Nếu lệch: in danh sách lỗi nhận được và so với luật ở mục 3. Không sửa bảng cho khớp; nếu tin bảng sai, ghi rõ vào báo cáo.

### 12. Test `tools/map-factory/test/cli.test.mjs` (`node:test`)

Chạy CLI bằng `spawnSync(process.execPath, [cli, ...args], { cwd: REPO_ROOT, encoding: "utf8" })`; xét `status` và `stdout`.
1. **Hai mẫu:** thoát 0, stdout đúng `ok d3043373…6f16\n` và `ok e77ce877…db83\n` (đủ 64 ký tự như mục 4).
2. **Bảy spec hỏng:** thoát 1, stdout đúng một dòng `error <code> "<path>"\n` như bảng mục 10. Ví dụ `error budget-missing "/budget"`.
3. **`spec-json`:** test ghi `{` vào `tools/map-factory/.cache/cli-test/broken-json/map.spec.json` (tạo thư mục nếu chưa có). CLI thoát 1, stdout đúng `error spec-json ""\n`.
4. **Cách dùng sai, thoát 2:** không tham số; chỉ `validate`; `validate <mẫu> thừa`; `build <mẫu>`; `check <mẫu>`; `validate tools/map-factory/test/fixtures` (không có `map.spec.json`).
5. **Kit:** `loadKits()` trả 0 lỗi và hai kit: `meadow@1` (18 proto, mọi `asset` là `null`), `pine-river@1` (12 proto, đủ hai tier trong sổ 025). `checkKit` với kit trong RAM:
   - kit `pine-river` mà một `asset` sửa thành `m0b/props/pine-river-pine-giant/pine-river-pine-giant` → đúng 1 lỗi;
   - `fileName` `river.json` cho kit `pine-river@1` → có lỗi;
   - `format` `"map-kit/1"` → có lỗi;
   - `protos` rỗng → có lỗi.
6. **Lớp chơi:** `loadGameplays()` trả 0 lỗi và hai mục đúng `game`, `map`, `adapter`, `commit`, `hash` như mục 6. Chép fixture Rồng sang `tools/map-factory/.cache/cli-test/gameplay/`, sửa một số trong `dais` (ví dụ `radiusCm` 400 → 401) mà giữ `hash`, rồi `loadGameplays(thư mục đó)` → đúng 1 lỗi.
7. **Cùng byte:** chạy CLI với mỗi mẫu hai lần: hai stdout giống hệt.
8. **File đúng byte:** sha256 của hai spec mẫu (mục 6), hai file kit (mục 7) và bảy spec hỏng (mục 10) đúng như phiếu.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và dòng kết quả vào báo cáo.

1. `pnpm --dir shared/game-kit exec vitest run map` đạt. In số file và số test (trước phiếu: 6 file, 185 test). Số file tăng đúng 2 so với lúc bắt đầu.
2. `pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json` thoát 0.
3. Lint của 027 (trong lệnh 1) đạt: danh sách file đã quét là đúng 7 file `edt.ts`, `hash.ts`, `index.ts`, `raster.ts`, `seeds.ts`, `sha256.ts`, `spec.ts` (thêm `along.ts` nếu phiếu 033 đã chạy trước); 0 vi phạm.
4. `node --test tools/map-factory/test/*.test.mjs` đạt, dòng tổng ghi `skipped 0`. In số test (trước phiếu: 13).
5. Lệnh tay, dán stdout và mã thoát:
   - `node tools/map-factory/cli.mjs validate tools/map-factory/maps/typing-defense/w1-silverfall` → 0, `ok d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16`;
   - `node tools/map-factory/cli.mjs validate tools/map-factory/maps/dragon-hold/L2-cau` → 0, `ok e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83`;
   - bảy spec hỏng → 1, mỗi spec đúng một dòng như bảng mục 10;
   - `node tools/map-factory/cli.mjs` → 2.
6. Chạy lại lệnh 1 và lệnh 4 lần thứ hai: cùng số test, cùng kết quả. Lệnh tay của mục 5 ra cùng từng byte.
7. Không hỏng phần còn lại của kit: `pnpm --dir shared/game-kit exec vitest run` đạt (trước phiếu: 42 file, 474 test), rồi `pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit` thoát 0.
   - Chạy hai lệnh này lần lượt, không song song.
   - Khi máy bận, một test cũ ngoài `map/` có thể quá thời hạn 5 s. Khi đó chạy lại cả lệnh một mình. Đạt khi lần chạy lại đạt; ghi cả hai lần vào báo cáo. Không sửa test ngoài phạm vi.
8. `shasum -a 256` hai spec mẫu, hai file kit, bảy spec hỏng: đúng như mục 6, 7, 10 (test 8 của mục 12 cũng kiểm).
9. Chạy lại `git status --short --untracked-files=all` và so với kết quả đã giữ lúc bắt đầu.
   - Lúc cuối chỉ được có **thêm** các file trong "Chỉ được ghi", cộng một dòng ` M shared/game-kit/map/index.ts`. `.cache` không hiện, vì bị bỏ qua.
   - Không có dòng ` M` hay ` D` mới nào khác, kể cả với file của 027–029 và sổ 025.
   - Các dòng đã có lúc bắt đầu (ví dụ file phiếu chưa commit) ghi lại vào báo cáo, nhưng không đụng.

## Báo cáo `docs/codex-queue/031-report.md`

- Các file đã viết, mỗi file một dòng nói nó làm gì.
- Kết quả chín lệnh kiểm, kèm số: số file và số test, danh sách file lint đã quét, hai `specHash` cạnh số vàng, stdout và mã thoát của các lệnh tay.
- Những chỗ phiếu chưa rõ và cách đã chọn; những chỗ lệch với phiếu, nếu có.

**Xong khi:** chín lệnh kiểm đều đạt, hai `specHash` đúng số vàng, bảy spec hỏng mỗi spec đúng một mã, báo cáo đã viết.
