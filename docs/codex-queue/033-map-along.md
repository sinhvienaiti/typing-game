# Phiếu 033 · Map Factory · `along.ts`: đặt vật dọc đường gấp khúc, chỉ bằng số nguyên (chỉ mã, không trình duyệt)

**Bối cảnh:** kế hoạch [`docs/tools/MAP_FACTORY.md`](../tools/MAP_FACTORY.md) §3, §8.5, §9.2, duyệt ngày 27/10/2026.
- Lớp L5 (dressing) đặt đèn, rào, cọc, mốc dọc đường cong (§3). Spec mẫu §8.1 có `dressing.along` với `everyCm`, `sideCm`, `alternate`, `skipNearCm`, `maxRun`.
- Phiếu này chỉ làm **phép hình học nền**: cho một đường gấp khúc có tọa độ cm nguyên và vài tham số, trả danh sách vị trí, góc và độ lệch ngang của từng vật.
- Lớp `dressing` thật để phiếu sau: đọc spec, chọn tuyến, đổi `skipNearCm` thành cửa sổ cung, `maxRun`, `clearOnBuild`, chọn proto. Phiếu này không làm phần nào trong số đó.

**Spike đang chạy, nên tham số là số chung.** Claude đang thử bố cục trên Rồng `L2-cau` (§6.2). Luật của spike sẽ quyết giá trị thật (đèn cách bao nhiêu, lệch bao nhiêu, có cần đồ dọc đường không).
- `along.ts` nhận mọi tham số từ lớp gọi. Không có giá trị mặc định mang nghĩa (không có "đèn cách 16 m"). Tham số chỉ được kiểm theo kiểu và khoảng.
- Số trong test chỉ là số thử, không phải luật.
- §9.2 cho phép bỏ phiếu này nếu spike thấy đồ dọc đường không giúp. Thuật toán dưới không phụ thuộc kết quả spike.

**Không `Math.sqrt`.** §8.2 và §8.5 cho phép `Math.sqrt`; phiếu này cố ý không dùng.
- Độ dài cung tính bằng căn nguyên `isqrt` (tìm nhị phân, chính xác).
- Pháp tuyến tính bằng phép chia nguyên làm tròn; góc tra bảng tan số nguyên theo bát phân.
- Mọi bước là phép tính số nguyên chính xác trong `Number`. Vì vậy hai người cài độc lập theo đúng chữ trong phiếu ra cùng từng số.

**Phụ thuộc:**
- Phiếu 027 (`hash32` trong `./hash`) và 028 (hai fixture lớp chơi) đã commit trên nhánh `map-factory` (`db65b753`, `eb74f8b6`). `RngStream` (`new RngStream(seed)`, `next()`, `int(min, max)` gồm cả hai đầu) ở `../platform/rng`.
- Không phụ thuộc phiếu 031. Nếu 031 chạy trước trong cùng làn và chưa commit, file của nó đã có sẵn; không đụng tới.
- Kiểm trước khi làm:
  - `pnpm --dir shared/game-kit exec vitest run map` đạt;
  - `shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json` ra đúng `ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37` (`dragon-hold.L2-cau.json`) và `71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428` (`typing-defense.w1-silverfall.json`).
- Thiếu hay sai thì dừng, ghi lý do vào báo cáo.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/map-codex` (nhánh `map-factory`), cwd `.`. Mọi đường dẫn tương đối tính từ đây.
- File của 027–029 đã commit. File phiếu, và file của phiếu chạy trước trong cùng làn (ví dụ 031), có thể chưa commit. Chúng không thuộc phiếu này: không sửa, không xóa.
- Trước khi ghi gì, chạy `git status --short --untracked-files=all` và giữ kết quả cho Kiểm 8.

**Chỉ được ghi:**
- `shared/game-kit/map/along.ts`;
- `shared/game-kit/map/along.test.ts`;
- `shared/game-kit/map/index.ts`: chỉ thêm dòng `export`;
- `docs/codex-queue/033-report.md`: tiếng Việt có dấu.

**Cấm:**
- sửa file khác trong `shared/game-kit/map/` (của 027, 029, 031), kể cả `lint.test.ts` và các test đã có. Thấy lỗi ở đó thì ghi vào báo cáo;
- sửa `tools/map-factory/**`, kể cả fixture;
- sửa phần khác của kit (`package.json`, `tsconfig.json`, `vitest.config.ts`, module khác);
- ghi vào `games/**`, hay bất cứ đâu trong `/Users/toandx/htdocs/typing-game`;
- cài gói; lệnh git có ghi (được dùng: `status`, `diff`, `log`, `show`); mạng, cổng, dev server, trình duyệt;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

**Quy ước mã:**
- Phép tính số trong mã lõi (`along.ts`) chỉ dùng `+ - * / %`, so sánh, `Math.abs`, `Math.min`, `Math.max`, và `hash32`. Kiểm đầu vào dùng `Number.isSafeInteger`, `Array.isArray`, `typeof`. Mọi phép chia nằm trong `floorDiv` (mục 2).
- Không `Math.sqrt`: test kiểm chuỗi `Math.sqrt` không có trong file, kể cả trong chú thích.
- Không `**`, trig, `Date`, `performance`, `BigInt` (lint của 027 bắt phần lớn).
- Test được dùng `Math.atan2`, `Math.tan`, `Math.hypot`, `BigInt`, `node:fs`, `node:crypto`.
- Import trong kit dùng đường dẫn tương đối, không đuôi (`./hash`); import chỉ để lấy kiểu viết `import type`.
- Chú thích trong mã viết bằng tiếng Anh.

## Việc

### 1. API của `map/along.ts`

```ts
export type AlongPoint = readonly [number, number]; // [x, z], integer cm
export const ALONG_Q = 1024;                          // arc-length units per cm
export const ALONG_LIMIT_CM = 16384;                  // |coordinate| bound, as in raster.ts
export const ALONG_MAX_SIDE_CM = 2000;
export const ALONG_MAX_ARC_Q = 2147483647;            // total arc length bound, in 1/1024 cm
export const TAN_SCALE = 1048576;                     // 2^20
export const TAN_HALF_DEG: readonly number[];         // 45 integers, section 4

export interface AlongArc {
  readonly lengths: readonly number[]; // lengths[i]: segment i, points[i] -> points[i + 1], in 1/1024 cm
  readonly starts: readonly number[];  // starts[i]: arc length at points[i]; starts.length === points.length
  readonly total: number;              // starts[points.length - 1]
}
export interface AlongParams {
  readonly everyCm: number;   // spacing along the arc
  readonly startCm: number;   // arc position of candidate 0
  readonly sideCm: number;    // lateral offset; > 0 is the right of travel
  readonly alternate: boolean;
  readonly jitterCm: number;  // max deterministic shift along the arc
  readonly seed: number;      // uint32, feeds hash32
  readonly skip: readonly (readonly [number, number])[]; // closed arc windows [fromCm, toCm]
}
export interface AlongItem {
  readonly k: number;        // candidate index, stable under skips
  readonly s: number;        // arc position, 1/1024 cm
  readonly seg: number;      // segment index
  readonly x: number;        // cm, after the lateral offset
  readonly z: number;
  readonly yawDeg: number;   // 0..359, direction of travel of segment seg
  readonly offsetCm: number; // signed lateral offset applied (sideCm or -sideCm)
}

export function floorDiv(a: number, b: number): number;
export function roundDiv(a: number, b: number): number;
export function isqrt(n: number): number;
export function isqrtRound(n: number): number;
export function yawDegOf(dx: number, dz: number): number;
export function polylineArc(points: readonly AlongPoint[]): AlongArc;
export function placeAlong(points: readonly AlongPoint[], params: AlongParams): AlongItem[];
export function alongHash(items: readonly AlongItem[]): number;
```

Mọi lỗi đầu vào ném `RangeError`. Không có `-0` trong đầu ra: cộng `+ 0` ở chỗ cần.

### 2. Số học nguyên

**Chia sàn, chia làm tròn** (`a`, `b` nguyên, `b > 0`, trong miền ở dòng "Kiểm đầu vào" dưới):

```text
floorDiv(a, b):  r = a % b;  if (r < 0) r += b;  return (a - r) / b;
roundDiv(a, b):  return floorDiv(2 * a + b, 2 * b);     // floor(a / b + 1/2), half rounds toward +infinity
```

- `%` của số thực là phép chính xác, `a − r` chia hết cho `b`, nên thương chính xác. Không dùng `Math.floor(a / b)`: phép chia số thực có thể làm tròn sai khi thương sát một số nguyên.
- Ví dụ: `floorDiv(7, 2)` = 3, `floorDiv(-7, 2)` = −4, `floorDiv(-8, 2)` = −4, `floorDiv(-1, 1024)` = −1; `roundDiv(5, 2)` = 3, `roundDiv(-5, 2)` = −2, `roundDiv(-7, 2)` = −3, `roundDiv(7, 3)` = 2, `roundDiv(-20480000, 512000)` = −40, `roundDiv(15360000, 512000)` = 30.
- `floorDiv(0, 5)` và `floorDiv(-0, 5)` cho `0`, không phải `-0`.
- Kiểm đầu vào (sai thì `RangeError`): `a`, `b` là số nguyên an toàn; `floorDiv` cần `|a| ≤ 2^51` và `1 ≤ b ≤ 2^51`; `roundDiv` cần `|a| ≤ 2^49` và `1 ≤ b ≤ 2^49`, để `2a + b` và `2b` vẫn trong miền của `floorDiv`.

**Căn nguyên** `isqrt(n)` = ⌊√n⌋, với `n` nguyên trong [0; 2^52] (4 503 599 627 370 496); ngoài khoảng hay không nguyên thì `RangeError`. Tìm nhị phân, đúng thứ tự này:

```text
lo = 0; hi = 67108864;                       // 2^26, and (2^26 + 1)^2 > 2^52 >= n
while (lo < hi) {
  mid = lo + floorDiv(hi - lo + 1, 2);
  if (mid * mid <= n) lo = mid; else hi = mid - 1;
}
return lo;
```

`mid ≤ 2^26` nên `mid * mid ≤ 2^52`, chính xác. Bất biến: `lo² ≤ n < (hi + 1)²`.

**Căn làm tròn** `isqrtRound(n)`: `r = isqrt(n)`; trả `r + 1` nếu `n − r·r > r`, ngược lại trả `r`. (√n ≥ r + ½ ⇔ n ≥ r² + r + ¼ ⇔ n ≥ r² + r + 1 với n nguyên; không bao giờ hòa.)

Ví dụ: `isqrt` của 0, 1, 2, 3, 4, 15, 16, 99 999 999, 100 000 000, 2^52 − 1, 2^52 là 0, 1, 1, 1, 2, 3, 4, 9999, 10 000, 67 108 863, 67 108 864. `isqrtRound` của 2, 3, 6, 7, 12, 13, 2 097 152, 262 144 000 000 là 1, 2, 2, 3, 3, 4, 1448, 512 000.

### 3. Độ dài cung: `polylineArc(points)`

- Kiểm đầu vào: `points` là mảng dài 1…100 000; mỗi điểm là mảng đúng 2 số nguyên an toàn trong [−16 384; 16 384].
- Với đoạn `i` (từ `points[i]` tới `points[i + 1]`): `dx`, `dz` là hiệu tọa độ;
  `lengths[i] = isqrtRound((dx·dx + dz·dz) · ALONG_Q · ALONG_Q)`.
  - Đơn vị là 1/1024 cm. `dx² + dz² ≤ 2^31`, nhân `2^20` thì ≤ 2^51: chính xác, nằm trong miền của `isqrt`.
  - Đoạn hai điểm trùng nhau có độ dài 0.
- `starts[0] = 0`; `starts[i + 1] = starts[i] + lengths[i]`; `total = starts[n − 1]`. Một điểm thì `lengths` rỗng và `total = 0`.
- `total > ALONG_MAX_ARC_Q` thì `RangeError`. Ví dụ hỏng: 65 điểm xen kẽ `[-16384, 0]`, `[16384, 0]` cho 64 đoạn × 33 554 432 = 2 147 483 648.

Vì sao dùng 1/1024 cm: làm tròn mỗi đoạn lệch ≤ ½ đơn vị, tức ≤ 0,0005 cm. Tuyến 0 của Lời Gọi có 475 đoạn, nên cộng dồn lệch ≤ 0,23 cm. Nếu đo bằng cm nguyên, lệch có thể tới 475 cm.

### 4. Góc: bảng tan số nguyên

**Quy ước:** `yawDeg` là góc của vectơ hướng đi `(dx, dz)` trong mặt x–z, tính từ +x (đông) quay về +z (nam), làm tròn tới độ gần nhất, trong [0; 359]. 0 là đông, 90 là nam, 180 là tây, 270 là bắc. Bằng `Math.round(atan2(dz, dx))` đổi ra độ và đưa về [0; 360), nhưng không dùng trig. Mã dựng hình của game đổi góc này sang `rotation.y` của mình; việc đó không thuộc lõi.

**Bảng** `TAN_HALF_DEG[c] = round(tan((c + 0.5)°) · 2^20)`, c = 0…44: biên giữa độ `c` và `c + 1`. Viết đúng 45 số này dạng literal trong mã:

```text
9151, 27458, 45782, 64134, 82525, 100966, 119470, 138048, 156711, 175471,
194342, 213335, 232464, 251741, 271180, 290796, 310602, 330615, 350849, 371320,
392047, 413045, 434334, 455934, 477864, 500145, 522801, 545854, 569330, 593256,
617658, 642568, 668017, 694037, 720666, 747942, 775905, 804601, 834075, 864379,
895569, 927702, 960843, 995061, 1030433
```

Claude tính bảng bằng `Math.tan` của Node và bằng `math.tan` của Python: cùng 45 số.

**Tra** `yawDegOf(dx, dz)`. `dx`, `dz` nguyên trong [−32 768; 32 768], không cùng bằng 0; sai thì `RangeError`.

```text
octant(n, d):            // 0 <= n <= d, d > 0; returns round(atan(n / d)) in degrees, 0..45
  c = 0
  while (c < 45 && n * TAN_SCALE >= TAN_HALF_DEG[c] * d) c += 1
  return c

ax = |dx|; az = |dz|
a  = (az <= ax) ? octant(az, ax) : 90 - octant(ax, az)       // angle in the first quadrant, 0..90
if (dz >= 0) t = (dx >= 0) ? a : 180 - a
else         t = (dx < 0)  ? 180 + a : 360 - a
return (t === 360) ? 0 : t
```

- Tích lớn nhất: `32768 · 2^20 = 2^35` và `1 030 433 · 32 768 < 2^36`. Chính xác.
- Biên tính bằng `>=`: tỉ số bằng đúng giá trị bảng thì sang độ trên.
- Ví dụ `(dx, dz)` → `yawDeg`: (1, 0) → 0; (1, 1) → 45; (0, 1) → 90; (−1, 1) → 135; (−1, 0) → 180; (−1, −1) → 225; (0, −1) → 270; (1, −1) → 315; (300, 400) → 53; (−1, −10000) → 270; (10000, −1) → 0; (17, 18) → 47; (100, 1) → 1; (114, 1) → 1 (0,5026°); (115, 1) → 0 (0,4982°).

### 5. `placeAlong(points, params)`

**Kiểm đầu vào** (sai thì `RangeError`): `points` như mục 3 (kể cả trần `total`), và:

| Tham số | Kiểu, khoảng |
|---|---|
| `everyCm` | nguyên [1; 100 000] |
| `startCm` | nguyên [0; 100 000] |
| `sideCm` | nguyên [−2000; 2000] |
| `alternate` | `typeof === "boolean"` |
| `jitterCm` | nguyên [0; ⌊(everyCm − 1) / 2⌋], để vật giữ đúng thứ tự |
| `seed` | nguyên [0; 4 294 967 295] |
| `skip` | mảng dài ≤ 1000; mỗi phần tử là mảng đúng 2 số nguyên `[from, to]`, 0 ≤ `from` ≤ `to` ≤ 2 097 151 |

**Thuật toán**, đúng thứ tự (`Q = ALONG_Q`):

```text
{ lengths, starts, total } = polylineArc(points)
if (total === 0) return []                      // one point, or every point the same
E  = everyCm * Q;  S0 = startCm * Q;  J = jitterCm
items = []
for (k = 0; S0 + k * E <= total; k += 1) {
  s = S0 + k * E
  if (J > 0) s += ((hash32(seed, "along", k) % (2 * J + 1)) - J) * Q
  if (s < 0 || s > total) continue
  if (some [from, to] in skip with from * Q <= s && s <= to * Q) continue
  i  = the largest segment index with lengths[i] > 0 && starts[i] <= s
  L  = lengths[i];  t = s - starts[i]           // 0 <= t <= L
  [ax, az] = points[i];  dx = points[i + 1][0] - ax;  dz = points[i + 1][1] - az
  bx = ax + roundDiv(dx * t, L)                 // base point on the polyline
  bz = az + roundDiv(dz * t, L)
  o  = (alternate && k % 2 === 1) ? 0 - sideCm : sideCm   // 0 - 0 is +0: no -0 in the output
  x  = bx + roundDiv(-dz * o * Q, L)            // right unit normal (-dz, dx) / (L / Q), times o
  z  = bz + roundDiv( dx * o * Q, L)
  items.push({ k, s, seg: i, x, z, yawDeg: yawDegOf(dx, dz), offsetCm: o })
}
return items
```

- **Ứng viên:** `k` = 0, 1, 2… chừng nào vị trí danh nghĩa `S0 + k·E` còn ≤ `total`. Ứng viên bị bỏ (rung ra ngoài `[0; total]`, hay rơi vào cửa sổ cấm) vẫn giữ chỉ số `k`. Vì vậy `k` ổn định, và chẵn lẻ của `alternate` không đổi khi một vật bị bỏ.
- **Rung** (`jitterCm`): độ lệch nguyên cm `hash32(seed, "along", k) % (2J + 1) − J`, trong [−J; J]. `hash32` của 027 với ba phần: số `seed`, chuỗi `"along"`, số `k`. `J = 0` thì không gọi `hash32`.
- **Cửa sổ cấm** `[from, to]` (cm) là đoạn đóng trên cung, so với `s` sau khi rung. Các cửa sổ được chồng nhau, không cần sắp.
- **Chọn đoạn:** đoạn có độ dài dương, bắt đầu muộn nhất mà không quá `s`. Vật nằm đúng ở đỉnh thuộc đoạn đi ra. Vật ở cuối đường (`s = total`) thuộc đoạn dương cuối cùng. Luôn tồn tại, vì đoạn dương đầu tiên có `starts = 0`. Được tìm nhị phân, miễn kết quả bằng định nghĩa này.
- **Bên phải:** `sideCm > 0` là bên phải của hướng đi (từ `points[0]` về cuối). Pháp tuyến phải của `(dx, dz)` là `(−dz, dx)`. Đi về đông (+x) thì bên phải là nam (+z); đi về bắc (−z) thì bên phải là đông (+x).
- **Góc** là góc của đoạn chứa vật (mục 4), không tính theo hướng lệch.

**Vì sao `Number` là đủ:** `|dx|, |dz| ≤ 32 768`; `L ≤ isqrtRound(2^51) < 2^26`; `t ≤ L`.
- `dx·t < 2^41`, `2·dx·t + L < 2^43`.
- `dz·o·Q ≤ 2^15 · 2000 · 2^10 < 2^37`.
- `S0 + k·E ≤ total + E < 2^32`.
- Mọi số nằm xa dưới 2^51, nên `floorDiv` chính xác.

**Sai số đã biết** (so với hình học số thực, dùng cho test, mục 8f):
- Vị trí gốc `(bx, bz)` lệch ≤ ½ cm mỗi trục so với điểm ở cung `s / Q` trên đoạn `i`.
- Độ dài số nguyên lệch ≤ ½ / 1024 cm mỗi đoạn so với `Math.hypot`. Vì vậy vị trí cung số thực của điểm gốc lệch khỏi `s / Q` không quá `0,7072 + (seg + 1) · 0,5 / 1024` cm.
- Độ dài vectơ lệch ngang `(x − bx, z − bz)` lệch khỏi `|o|` không quá `0,7072 + |o| · 0,5 / L` cm. Chỉ đoạn rất ngắn (vài cm) với `|o|` lớn mới vượt 1 cm.

### 6. `alongHash(items)`

`alongHash(items) = hash32(k₀, s₀, seg₀, x₀, z₀, yawDeg₀, offsetCm₀, k₁, s₁, …)`: một lần gọi `hash32` của 027, mỗi vật đủ 7 số theo đúng thứ tự trên, các vật theo thứ tự của mảng. Danh sách rỗng cho `hash32()` = 2872998923. Mọi số nằm trong miền của `hash32`: `s ≤ 2^31 − 1`, tọa độ trong khoảng ±18 400 (điểm gốc nằm giữa hai đầu đoạn, lệch ngang ≤ 2001 cm).

### 7. `map/index.ts`

Thêm `export` cho mọi tên ở mục 1, kể cả các kiểu. Không đổi các dòng đã có.

### 8. Test `map/along.test.ts`

**a. Số học:** mọi ví dụ ở mục 2. `isqrt` so với một bản BigInt viết trong test (Newton trên `BigInt`) ở 10 000 số có seed trong [0; 2^52] (dùng `new RngStream(hash32("isqrt", k))`, ghép hai lần `next()`), cộng các số `m² − 1`, `m²`, `m² + 1` với `m` = 1…2000 và `m` = 2^26 − 2000 … 2^26 (bỏ số > 2^52). Ca lỗi: `isqrt(-1)`, `isqrt(1.5)`, `isqrt(4503599627370497)`; `floorDiv(1, 0)`; `roundDiv(1, -2)`.

**b. Bảng và góc:**
- `TAN_HALF_DEG` có 45 số, đúng như mục 4, và bằng `Math.round(Math.tan((c + 0.5) * Math.PI / 180) * 1048576)` từng số.
- Mọi ví dụ ở mục 4.
- So với `Math.atan2` trên đúng tập này:
  - lưới `dx, dz` ∈ [−300; 300] bỏ (0, 0): 361 200 vectơ;
  - 20 000 vectơ `dx = hash32("yaw", k, 0) % 65537 − 32768`, `dz = hash32("yaw", k, 1) % 65537 − 32768`, k = 1…20 000;
  - tổng 381 200 vectơ.
- Với mỗi vectơ: `a = Math.atan2(dz, dx) · 180 / π`, đưa về [0; 360); sai số vòng `min(|y − a|, 360 − |y − a|)` phải ≤ 0,501°. Kế hoạch §9.2 cho phép 1°; thuật toán làm tròn tới độ gần nhất nên chặt hơn được.
- In sai số lớn nhất và số vectơ mà `yawDegOf` khác `Math.round(a) % 360`. Bản nháp của Claude: lớn nhất 0,499991°, 0 vectơ khác.
- Ca lỗi: `yawDegOf(0, 0)`, `yawDegOf(32769, 0)`, `yawDegOf(0.5, 1)`.

**c. Ca tính tay.** Mỗi vật viết `[k, s, seg, x, z, yawDeg, offsetCm]`. Tham số gốc `P0 = { everyCm: 250, startCm: 0, sideCm: 100, alternate: false, jitterCm: 0, seed: 0, skip: [] }`:

| Đường | Tham số | Kết quả |
|---|---|---|
| `[[0,0],[1000,0]]` | `P0` | `[0,0,0,0,100,0,100]`, `[1,256000,0,250,100,0,100]`, `[2,512000,0,500,100,0,100]`, `[3,768000,0,750,100,0,100]`, `[4,1024000,0,1000,100,0,100]` |
| `[[0,0],[1000,0]]` | `P0`, `alternate: true` | `[0,0,0,0,100,0,100]`, `[1,256000,0,250,-100,0,-100]`, `[2,512000,0,500,100,0,100]`, `[3,768000,0,750,-100,0,-100]`, `[4,1024000,0,1000,100,0,100]` |
| `[[0,0],[1000,0]]` | `P0`, `sideCm: 0`, `alternate: true` (không có `-0`: `Object.is(offsetCm, -0)` phải là `false`) | `[0,0,0,0,0,0,0]`, `[1,256000,0,250,0,0,0]`, `[2,512000,0,500,0,0,0]`, `[3,768000,0,750,0,0,0]`, `[4,1024000,0,1000,0,0,0]` |
| `[[0,0],[0,-1000]]` (đi về bắc) | `P0` | `[0,0,0,100,0,270,100]`, `[1,256000,0,100,-250,270,100]`, `[2,512000,0,100,-500,270,100]`, `[3,768000,0,100,-750,270,100]`, `[4,1024000,0,100,-1000,270,100]` |
| `[[0,0],[300,400]]` (dài đúng 500 cm) | `P0`, `everyCm: 100`, `sideCm: 50` | `[0,0,0,-40,30,53,50]`, `[1,102400,0,20,110,53,50]`, `[2,204800,0,80,190,53,50]`, `[3,307200,0,140,270,53,50]`, `[4,409600,0,200,350,53,50]`, `[5,512000,0,260,430,53,50]` |
| `[[0,0],[100,0],[100,100]]` (góc vuông) | `P0`, `everyCm: 50`, `sideCm: 10` | `[0,0,0,0,10,0,10]`, `[1,51200,0,50,10,0,10]`, `[2,102400,1,90,0,90,10]`, `[3,153600,1,90,50,90,10]`, `[4,204800,1,90,100,90,10]` |
| `[[0,0],[1000,0]]` | `P0`, `skip: [[250,250],[700,1000]]` | `[0,0,0,0,100,0,100]`, `[2,512000,0,500,100,0,100]` |
| `[[0,0],[1000,0]]` | `P0`, `startCm: 1001` | `[]` |
| `[[5,5]]` | `P0` | `[]` |
| `[[5,5],[5,5]]` | `P0` | `[]` |

Ở ca góc vuông, vật `k = 2` nằm đúng ở đỉnh (100, 0) nên thuộc đoạn đi ra (đi về nam), và bên phải của hướng nam là tây: x = 90.

**d. Ba đường vàng.** Đọc hai fixture của 028 (đường dẫn từ `map/`: `../../../tools/map-factory/test/fixtures/gameplay/…`). Trước hết kiểm sha256 của cả file và trường `hash`, như `fields-sample.test.ts`. Sai thì test hỏng với lời nhắn "chạy lại phiếu 028".

| Tên | Đường | Tham số |
|---|---|---|
| `td-route0` | `routes[0].points` của `typing-defense.w1-silverfall.json` (476 điểm, mẫu 25 cm của `groundLanes`; mở đầu `[-1000,-4600],[-983,-4582],[-966,-4564]`, kết thúc `[29,3959],[14,3979],[0,4000]`) | `everyCm: 750, startCm: 300, sideCm: 280, alternate: true, jitterCm: 0, seed: 0, skip: [[0, 800], [5000, 5600]]` |
| `dh-cau` | `lanes[0].points` của `dragon-hold.L2-cau.json`: làn `cau`, 5 điểm `[[850,-2900],[500,-2250],[220,-1540],[120,-1000],[40,-600]]` | `everyCm: 120, startCm: 60, sideCm: -200, alternate: false, jitterCm: 30, seed: 20261028, skip: [[950, 1940]]` (cầu `fromCm` 1050 … `toCm` 1840, nới 100 cm) |
| `synthetic` | `[[0,0],[0,0],[1000,0],[1000,1],[1000,700],[300,0],[300,0],[-500,-800],[-500,-800],[-1700,-800],[-1700,400],[-1000,-300],[16384,-16384]]`: hai đoạn dài 0, đoạn dài 1 cm, đủ bốn hướng trục, đoạn chéo, quay đầu gắt, chạm biên 16 384 | `everyCm: 37, startCm: 0, sideCm: 45, alternate: true, jitterCm: 18, seed: 123456789, skip: [[100, 150], [140, 200], [555, 555], [30000, 2097151]]` (`jitterCm` đúng mức trần ⌊36 / 2⌋; hai cửa sổ chồng nhau; một cửa sổ rộng 0) |

**Số vàng.** Claude tính bằng hai bản cài độc lập theo đúng chữ trong phiếu, mỗi bản chạy hai lần, cùng kết quả: JavaScript dùng `Number` và tìm nhị phân; Python dùng số nguyên lớn, `math.isqrt` và `//`.

| Tên | `total` (1/1024 cm) | Số vật | `alongHash` |
|---|---:|---:|---:|
| `td-route0` | 12163917 | 14 | 1811293709 |
| `dh-cau` | 2517567 | 12 | 1575973982 |
| `synthetic` | 31636035 | 808 | 440583006 |

Ba vật đầu và vật cuối, dạng `[k, s, seg, x, z, yawDeg, offsetCm]`:

| Tên | Vật 1 | Vật 2 | Vật 3 | Vật cuối |
|---|---|---|---|---|
| `td-route0` | `[1,1075200,41,-113,-4160,23,-280]` | `[2,1843200,71,287,-3370,37,280]` | `[3,2611200,101,422,-2801,149,-280]` | `[15,11827200,461,417,3942,133,-280]` |
| `dh-cau` | `[0,74752,0,991,-2741,118,-200]` | `[1,204800,0,931,-2629,118,-200]` | `[2,276480,0,898,-2567,118,-200]` | `[19,2373632,3,264,-699,101,-200]` |
| `synthetic` | `[1,30720,1,30,-45,0,-45]` | `[2,89088,1,87,45,0,45]` | `[6,220160,1,215,45,0,45]` | `[811,30709760,11,15689,-15803,317,-45]` |

Số để dò lỗi:
- `td-route0`: 475 đoạn; bốn độ dài đầu 25353, 25353, 26107, 25353.
- `dh-cau`: `lengths` = 755959, 781534, 562362, 417712.
- `synthetic`: `lengths` = 0, 1024000, 1024, 715776, 1013708, 0, 1158524, 0, 1228800, 1228800, 1013708, 24251695.
- Rung: `dh-cau` với k = 0…3 là 13, 20, −30, −27 cm (`hash32(20261028, "along", 0)` = 2665129022); `synthetic` với k = 0…3 là −2, −7, 13, 4 cm, nên `k = 0` rơi ra ngoài (s < 0) và vật đầu là `k = 1`.

Nếu lệch: so `total` và `lengths` trước (mục 3), rồi vật đầu (mục 5: rung, chọn đoạn, làm tròn), rồi góc (mục 4). Không sửa số cho khớp. Nếu mọi số dò lỗi đã đúng mà băm vẫn lệch, ghi rõ vào báo cáo.

**e. Bản cài lại bằng `BigInt`.** Viết trong test một bản `placeAlong` thứ hai, độc lập:
- toàn bộ bằng `BigInt`;
- căn bằng Newton trên `BigInt`, không tìm nhị phân;
- chia sàn của `BigInt` tự viết (toán tử `/` của `BigInt` cắt về 0, nên phải sửa cho số âm);
- góc bằng cùng bảng `TAN_HALF_DEG` của lõi.

Bản này phải cho **đúng cùng** danh sách vật với `placeAlong` ở ba đường vàng và ở 100 đường có seed:
- đường `k` = 1…100 dùng `new RngStream(hash32("along", k))`;
- 1…40 điểm;
- một phần ba số đường là "đường ngắn": mỗi bước đổi tọa độ trong [−3; 3], có điểm trùng, `everyCm` trong [1; 5];
- còn lại: tọa độ ngẫu nhiên trong [−16 384; 16 384], `everyCm` trong [1; 3000];
- `startCm` trong [0; 50]; `sideCm` trong [−2000; 2000]; `alternate` ngẫu nhiên; `jitterCm` trong [0; ⌊(everyCm − 1) / 2⌋]; `seed` là một `next()`;
- 0…3 cửa sổ cấm nằm trong [0; total / 1024 + 10].

In số đường và tổng số vật đã so.

**f. Tính chất** (ba đường vàng và 100 đường có seed):
- `s` tăng ngặt theo thứ tự mảng; `k` tăng ngặt.
- Với mọi vật: `s − (S0 + k·E)` là bội của `Q` và nằm trong [−J·Q; J·Q]. Khi `J = 0`, hai vật có `k` liền nhau cách nhau **đúng** `everyCm` theo cung số nguyên (`s` chênh đúng `everyCm · 1024`). Đây là dạng chính xác của "khoảng cách theo cung = `everyCm` ± 1 cm" ở §9.2.
- **Đủ và đúng cửa sổ:** test tự liệt kê mọi ứng viên `k` có `s` (sau rung) trong [0; total]. Ứng viên nằm trong một cửa sổ thì không có trong kết quả; ứng viên không nằm trong cửa sổ nào thì có.
- **Cung số thực:** gọi lại với `sideCm: 0` (tham số khác giữ nguyên) để lấy điểm gốc `(bx, bz)`; hai danh sách có cùng các `k`. Với mỗi vật, `Sf[seg] + Math.hypot(bx − Ax, bz − Az)` (Sf là tổng `Math.hypot` các đoạn trước) lệch khỏi `s / 1024` không quá `0,7072 + (seg + 1) · 0,5 / 1024`. Ở ba đường vàng, lệch ≤ 1 cm.
- **Lệch ngang:** `|Math.hypot(x − bx, z − bz) − |offsetCm||` ≤ `0,7072 + |offsetCm| · 0,5 / lengths[seg]`. Ở ba đường vàng ≤ 1 cm.
- **Góc:** sai số vòng của `yawDeg` so với `Math.atan2` của đoạn `seg` ≤ 0,501°.
- In sai số lớn nhất của ba phép đo trên. Bản nháp của Claude: cung 0,53 / 0,57 / 0,70 cm; ngang 0,43 / 0,26 / 0,28 cm ở `td-route0` / `dh-cau` / `synthetic`. Trên 3000 đường ngẫu nhiên, chưa vượt công thức lần nào.

**g. Ca lỗi** ném `RangeError`:
- `points` rỗng; điểm `[1.5, 0]`, `[16385, 0]`, `[1, 2, 3]`; 65 điểm xen kẽ `[-16384, 0]` và `[16384, 0]` (vượt `ALONG_MAX_ARC_Q`);
- `everyCm` 0; `startCm` −1; `sideCm` 2001; `alternate` `1`; `jitterCm` 5 với `everyCm` 10; `seed` −1; `seed` 4294967296;
- `skip` `[[5, 4]]`, `[[-1, 3]]`, `[[0, 2097152]]`, `[[1]]`.

**h. Không `Math.sqrt`:** đọc `along.ts` bằng `node:fs`; chuỗi `Math.sqrt` không xuất hiện ở đâu trong file.

**i. Cùng kết quả:** gọi `placeAlong` hai lần với từng đường vàng: hai mảng bằng nhau từng phần tử.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và dòng kết quả vào báo cáo.

1. `pnpm --dir shared/game-kit exec vitest run map` đạt. In số file và số test. Số file tăng đúng 1 so với lúc bắt đầu (6 nếu 031 chưa chạy, 8 nếu đã chạy).
2. `pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json` thoát 0.
3. Lint của 027 (trong lệnh 1) đạt: danh sách file đã quét có `along.ts`, cùng các file lõi đã có lúc bắt đầu (`edt.ts`, `hash.ts`, `index.ts`, `raster.ts`, `seeds.ts`, và `sha256.ts`, `spec.ts` nếu 031 đã chạy); 0 vi phạm.
4. Số vàng ở mục 8d khớp từng số: ba `total`, ba số vật, ba `alongHash`, ba vật đầu và vật cuối mỗi đường. Ghi giá trị nhận được cạnh số vàng trong báo cáo.
5. Bản BigInt (8e) bằng `placeAlong` ở 103 đường; các tính chất 8f đạt. In số vật đã so, sai số lớn nhất của cung, ngang, góc.
6. Chạy lệnh 1 lần thứ hai: cùng số test, cùng kết quả, cùng các dòng in.
7. Không hỏng phần còn lại của kit: `pnpm --dir shared/game-kit exec vitest run` đạt, rồi `pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit` thoát 0.
   - Chạy hai lệnh này lần lượt, không song song.
   - Khi máy bận, một test cũ ngoài `map/` có thể quá thời hạn 5 s. Khi đó chạy lại cả lệnh một mình. Đạt khi lần chạy lại đạt; ghi cả hai lần vào báo cáo. Không sửa test ngoài phạm vi.
8. Chạy lại `git status --short --untracked-files=all` và so với kết quả đã giữ lúc bắt đầu.
   - Lúc cuối chỉ được có **thêm** `shared/game-kit/map/along.ts`, `along.test.ts`, `docs/codex-queue/033-report.md`, cộng một dòng ` M shared/game-kit/map/index.ts` (nếu dòng này đã có từ 031 thì giữ nguyên).
   - Không có dòng ` M` hay ` D` mới nào khác.
   - Các dòng đã có lúc bắt đầu ghi lại vào báo cáo, nhưng không đụng.

## Báo cáo `docs/codex-queue/033-report.md`

- Các file đã viết, mỗi file một dòng nói nó làm gì.
- Kết quả tám lệnh kiểm, kèm số.
- Bảng số vàng: giá trị test nhận được, cạnh giá trị trong phiếu.
- Sai số lớn nhất của cung, ngang, góc; số vectơ góc khác `Math.round`.
- Những chỗ phiếu chưa rõ và cách đã chọn; những chỗ lệch với phiếu, nếu có.

**Xong khi:** tám lệnh kiểm đều đạt, số vàng khớp từng số, báo cáo đã viết.
