# Phiếu 029 · Map Factory · Trường: tô hình lên lưới và biến đổi khoảng cách số nguyên (Meijster) (chỉ mã, không trình duyệt)

**Bối cảnh:** kế hoạch [`docs/tools/MAP_FACTORY.md`](../tools/MAP_FACTORY.md), duyệt ngày 27/10/2026.
- Lớp L1 của lõi là một lưới 50 cm cộng **biến đổi khoảng cách** cho đường, nước, đất xây (§3).
- Một bộ trường dùng chung cho san đất, sơn đất và chỗ lùi của cây (§4.1, dòng "Khoảng cách").
- Phiếu này làm hai phép toán nền: **tô hình lên lưới** (`raster.ts`) và **EDT bình phương chính xác** (`edt.ts`).
- Lớp L1 thật (`layers/fields.ts`) để phiếu 032. Ở đây chỉ có một **bộ trường mẫu** trong test, để băm và đo thời gian trên hai bản đồ thật.

**Phụ thuộc:**
- Phiếu 027 (lõi, lint, `map/tsconfig.json`) đã commit trên nhánh `map-factory` (`db65b753`). API thật: `hash32(...parts: (number | string)[])` trong `./hash`; `RngStream` (`new RngStream(seed)`, `next()`, `int(min, max)` gồm cả hai đầu) trong `../platform/rng`.
- Phiếu 028 (hai fixture) chạy ngay trước trong cùng worktree, có thể chưa commit.

Kiểm trước khi làm:
- `pnpm --dir shared/game-kit exec vitest run map` đạt;
- `tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json` có trường `hash` = `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a`, và sha256 của cả file (`shasum -a 256`) = `ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37`;
- `tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json` có `hash` = `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23`, và sha256 của cả file = `71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428`.
- Hai sha256 này là Kiểm 2 của phiếu 028. Số vàng ở mục 6 tính từ đúng hai file có các sha256 đó.

Thiếu hay sai thì dừng, ghi lý do vào báo cáo.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/map-codex` (nhánh `map-factory`), cwd `.`. Mọi đường dẫn tương đối tính từ đây.
- File của 027 đã commit. File của 028 và các file phiếu có thể chưa commit. Chúng không thuộc phiếu này: không sửa, không xóa.
- Trước khi ghi gì, chạy `git status --short --untracked-files=all` và giữ kết quả cho Kiểm 8.

**Chỉ được ghi:**
- `shared/game-kit/map/raster.ts`, `edt.ts`;
- `shared/game-kit/map/index.ts`: chỉ thêm dòng `export`;
- `shared/game-kit/map/raster.test.ts`, `edt.test.ts`, `fields-sample.test.ts`;
- `docs/codex-queue/029-report.md`: tiếng Việt có dấu.

**Cấm:**
- sửa file của phiếu 027 (`hash.ts`, `seeds.ts`, `lint.test.ts`, `map/tsconfig.json`, các test của 027) và của phiếu 028 (`tools/map-factory/**`, kể cả fixture). Thấy lỗi ở đó thì ghi vào báo cáo;
- sửa phần khác của kit (`package.json`, `tsconfig.json`, `vitest.config.ts`, module khác);
- ghi vào `games/**`, hay bất cứ đâu trong `/Users/toandx/htdocs/typing-game`;
- cài gói, lệnh git có ghi (được dùng: `status`, `diff`, `log`, `show`), mạng, cổng, dev server, trình duyệt;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Mã lõi theo §8.5: số nguyên, chỉ `+ - * /`, `Math.floor`, `Math.ceil`, `Math.round`, `Math.sqrt`, `Math.min`, `Math.max`, `Math.abs`. Không `**`, không trig, không `Date`, không `performance` (lint của 027 sẽ bắt). Không `BigInt` trong mã lõi. Test được dùng `BigInt`, `node:crypto`, `node:fs`, `performance`. Chú thích trong mã viết bằng tiếng Anh. Import trong kit dùng đường dẫn tương đối, không đuôi (`../platform/rng`, `./hash`).

## Việc

### 1. `map/raster.ts`

```ts
export interface RasterGrid {
  readonly originX: number; // cm, west edge of cell column 0
  readonly originZ: number; // cm, north edge of cell row 0
  readonly cellCm: number;  // even, >= 2
  readonly w: number;       // cells along x
  readonly h: number;       // cells along z
}
export type RasterPoint = readonly [number, number]; // [x, z] in cm
export const RASTER_LIMIT_CM = 16384;
export const RASTER_MAX_HALF_WIDTH_CM = 2000;
export function makeMask(grid: RasterGrid): Uint8Array;            // w * h zeros
export function cellCenterX(grid: RasterGrid, i: number): number;  // originX + i * cellCm + cellCm / 2
export function cellCenterZ(grid: RasterGrid, j: number): number;  // originZ + j * cellCm + cellCm / 2
export function rasterDisc(grid: RasterGrid, mask: Uint8Array, x: number, z: number, r: number): void;
export function rasterRect(grid: RasterGrid, mask: Uint8Array, x0: number, z0: number, x1: number, z1: number): void;
export function rasterPolyline(grid: RasterGrid, mask: Uint8Array, points: readonly RasterPoint[], halfWidth: number): void;
export function rasterPolygon(grid: RasterGrid, mask: Uint8Array, points: readonly RasterPoint[]): void;
```

**Lưới.** Ô `(i, j)` có chỉ số `k = j * w + i`. Tâm ô là `(cx, cz) = (originX + i·cellCm + cellCm/2, originZ + j·cellCm + cellCm/2)`. Vì `cellCm` chẵn nên tâm ô luôn là số nguyên.

**Luật tâm ô.** Một ô thuộc hình khi và chỉ khi **tâm** của nó thuộc hình. Mọi hình là **tập đóng**: điểm nằm đúng trên biên thì thuộc hình. Gọi `P = (cx, cz)`:

| Hình | Ô thuộc hình khi |
|---|---|
| Đĩa `(x, z, r)` | `(cx − x)² + (cz − z)² ≤ r²` |
| Rect `(x0, z0, x1, z1)` | `x0 ≤ cx ≤ x1` và `z0 ≤ cz ≤ z1` |
| Đường có bề rộng `(points, hw)` | Có một đoạn `A→B` (các điểm liền nhau; chỉ 1 điểm thì `A = B`) với khoảng cách từ `P` tới đoạn thẳng `AB` ≤ `hw`. Tính bằng số nguyên: `d = B − A`, `u = P − A`, `len2 = d·d`, `t = u·d`. Nếu `len2 = 0` hoặc `t ≤ 0`: `u·u ≤ hw²`. Nếu `t ≥ len2`: `|P − B|² ≤ hw²`. Còn lại: `c = u.x·d.z − u.z·d.x`, và `c·c ≤ hw²·len2` |
| Đa giác `(points)` | Luật chẵn lẻ, biên tính là trong (xem dưới) |

**Đa giác.** Các cạnh là `points[k] → points[(k + 1) % n]`. Với mỗi cạnh `A→B`:
1. Nếu `(B.x − A.x)·(P.z − A.z) − (B.z − A.z)·(P.x − A.x) = 0` và `min(A.x, B.x) ≤ P.x ≤ max(A.x, B.x)` và `min(A.z, B.z) ≤ P.z ≤ max(A.z, B.z)`: `P` nằm trên biên, ô thuộc hình, dừng.
2. Nếu `(A.z > P.z) !== (B.z > P.z)`: đặt `den = B.z − A.z`, `num = (P.z − A.z)·(B.x − A.x)`, `lhs = (P.x − A.x)·den`. Cạnh cắt tia về phía +x khi `den > 0 ? lhs < num : lhs > num`; khi đó đảo cờ "trong".
3. Hết các cạnh: ô thuộc hình khi cờ "trong" đang bật.

**Vì sao `Number` là đủ** (chép ý này vào chú thích tiếng Anh): mọi tọa độ, kể cả tâm ô, nằm trong [−16 384; 16 384], và `hw ≤ 2000`.
- Mọi hiệu ≤ 32 768. Mọi tích hai hiệu ≤ 2^30, mọi tổng hai tích < 2^32: chính xác.
- `hw²·len2 ≤ 2000² · 2 · 32 768² ≈ 8,6·10^15 < 2^53`: chính xác.
- Riêng `c·c` có thể vượt 2^53. Khi đó nó chắc chắn lớn hơn `hw²·len2`, và phép làm tròn đơn điệu nên phép so vẫn đúng.

**Kiểm đầu vào** (sai thì ném `RangeError`):
- lưới: mọi trường là số nguyên an toàn; `cellCm` chẵn và ≥ 2; `1 ≤ w, h ≤ 4096`; `originX ≥ −16384`, `originZ ≥ −16384`, `originX + w·cellCm ≤ 16384`, `originZ + h·cellCm ≤ 16384`;
- `mask.length === w·h`;
- mọi tọa độ hình là số nguyên an toàn trong [−16384; 16384];
- đĩa: `r` nguyên trong [0; 32768];
- rect: `x0 ≤ x1` và `z0 ≤ z1`;
- đường: ít nhất 1 điểm; `halfWidth` nguyên trong [0; 2000];
- đa giác: ít nhất 3 điểm.

**Ghi:** ô thuộc hình thì gán `mask[k] = 1`. Không bao giờ xóa ô đã có; ô khác giữ nguyên. Nhiều lần gọi trên một mask cho ra hợp của các hình.

**Hiệu năng:** chỉ duyệt các ô có tâm nằm trong hộp bao của hình (đĩa: nới `r`; đường: từng đoạn, nới `hw`), cắt theo lưới. Không duyệt cả lưới cho mỗi hình. Kết quả phải đúng như luật tâm ô trên cả lưới.

### 2. `map/edt.ts`

```ts
export const EDT_INF = 2147483647;
export function edtSquared(mask: Uint8Array, w: number, h: number): Int32Array;
```

- **Kết quả:** `out[j·w + i] = min((i − i')² + (j − j')²)` trên mọi ô `(i', j')` có `mask ≠ 0`. Đơn vị là ô (khoảng cách cm = √out × cellCm, việc của lớp sau). Ô trong mask cho 0. Mask toàn 0 thì mọi ô là `EDT_INF`.
- **Kiểm đầu vào:** `w`, `h` nguyên trong [1; 4096]; `mask.length === w·h`; sai thì `RangeError`.
- **Thuật toán:** Meijster, Roerdink, Hesselink (2000), hai pha, O(w·h), chỉ số nguyên:
  - pha 1, từng cột `i`: `G[i][j]` là số ô theo trục z tới ô mask gần nhất trong cùng cột; cột không có ô mask thì `G = w + h`. Một lượt xuôi, một lượt ngược;
  - pha 2, từng hàng `j`: đường bao dưới của `f(x, i) = (x − i)² + G[i][j]²`, với `Sep(i, u) = Math.floor((u² − i² + G[u][j]² − G[i][j]²) / (2·(u − i)))`, dùng hai mảng `s`, `t` như bài báo;
  - `(w + h)² > (w − 1)² + (h − 1)²`, nên cột không có ô mask không bao giờ thắng. Xét riêng mask rỗng trước pha 2.
- Kết quả là duy nhất, nên mọi bản cài đúng đều cho cùng từng số.
- Bộ nhớ đệm bên trong được dùng lại giữa các lần gọi; kết quả luôn là một `Int32Array` mới.

### 3. `map/index.ts`

Thêm `export` cho mọi tên ở mục 1 và 2. Không đổi các dòng đã có.

### 4. Test `raster.test.ts`

**a. Ca tính tay** trên lưới `G0 = { originX: 0, originZ: 0, cellCm: 2, w: 5, h: 5 }`. Tâm ô có x, z thuộc {1, 3, 5, 7, 9}; chỉ số `k = j·5 + i`. Mỗi ca dùng một mask mới:

| Gọi | Số ô | Chỉ số các ô bằng 1 |
|---|---:|---|
| `rasterDisc(G0, m, 5, 5, 2)` | 5 | 7, 11, 12, 13, 17 |
| `rasterDisc(G0, m, 4, 4, 0)` | 0 | (không có) |
| `rasterDisc(G0, m, 5, 5, 0)` | 1 | 12 |
| `rasterRect(G0, m, 3, 3, 7, 5)` | 6 | 6, 7, 8, 11, 12, 13 |
| `rasterRect(G0, m, 4, 0, 4, 10)` | 0 | (không có) |
| `rasterRect(G0, m, 5, 0, 5, 10)` | 5 | 2, 7, 12, 17, 22 |
| `rasterPolyline(G0, m, [[1, 1], [9, 1]], 0)` | 5 | 0, 1, 2, 3, 4 |
| `rasterPolyline(G0, m, [[1, 1], [9, 9]], 1)` | 5 | 0, 6, 12, 18, 24 |
| `rasterPolyline(G0, m, [[1, 1], [9, 9]], 2)` | 13 | 0, 1, 5, 6, 7, 11, 12, 13, 17, 18, 19, 23, 24 |
| `rasterPolyline(G0, m, [[5, 5]], 2)` | 5 | 7, 11, 12, 13, 17 |
| `rasterPolygon(G0, m, [[0, 0], [10, 0], [0, 10]])` | 15 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 15, 16, 20 |
| `rasterPolygon(G0, m, [[1, 1], [5, 1], [5, 5], [1, 5]])` | 9 | 0, 1, 2, 5, 6, 7, 10, 11, 12 |
| `rasterPolygon(G0, m, [[0, 0], [10, 10], [10, 0], [0, 10]])` (hình nơ tự cắt) | 17 | 0, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 24 |

**b. 200 ca có seed, so với cách tính vét cạn bằng `BigInt`.**
- Ca `k` = 1…200 dùng `new RngStream(hash32("raster", k))` (`RngStream` ở `../platform/rng`). Loại hình theo `k % 4`: 0 đĩa, 1 rect, 2 đường, 3 đa giác.
- `cellCm` chọn trong {2, 50, 200}; `w`, `h` trong [1; 64]; lưới nằm trong giới hạn.
- Tọa độ phần lớn là bội của `cellCm / 2`, để tâm ô hay rơi đúng trên biên; một phần lệch thêm ±1…3 cm.
- Phải có đủ các ca suy biến: `r = 0`; rect có `x0 = x1`; đường 1 điểm; đường có hai điểm liền nhau trùng nhau; đa giác tự cắt; hình nằm ngoài hẳn lưới; hình phủ cả lưới; `hw` từ 0 tới mức phủ cả lưới (≤ 2000).
- Vét cạn: xét **mọi** ô của lưới bằng `BigInt`. Với đường, dùng công thức khác với mã lõi: ở trường hợp giữa đoạn, so `(u·u)·len2 − t² ≤ hw²·len2`. Kết quả phải bằng mask từng ô.
- Trước khi tô, đặt sẵn vài ô bằng 1. Sau khi tô, các ô đó vẫn là 1.
- In số ca và tổng số ô đã so.
- Đặt thời hạn 60 000 ms cho test vét cạn (mặc định 5 s của vitest có thể không đủ khi máy bận). Bản nháp của Claude chạy 200 ca tô hình và 200 lưới EDT trong khoảng 2,5 s.

**c. Ca lỗi** ném `RangeError`: `cellCm` lẻ; `cellCm = 0`; `w = 0`; lưới vượt 16 384; `mask` sai cỡ; `r = -1`; rect có `x0 > x1`; đường 0 điểm; `halfWidth = 2001`; đa giác 2 điểm; tọa độ 1,5; tọa độ 16 385.

### 5. Test `edt.test.ts`

**a. Ca tính tay:**
- mask là kết quả của `rasterDisc(G0, m, 5, 5, 2)` (ô 7, 11, 12, 13, 17), `w = h = 5`. Kết quả theo hàng:

  ```text
  5 2 1 2 5
  2 1 0 1 2
  1 0 0 0 1
  2 1 0 1 2
  5 2 1 2 5
  ```
- mask 5 × 5 chỉ có ô 0: kết quả là `i² + j²`, tức `0,1,4,9,16, 1,2,5,10,17, 4,5,8,13,20, 9,10,13,18,25, 16,17,20,25,32`;
- mask 3 × 2 toàn 0: sáu ô `EDT_INF`.

**b. 200 lưới có seed, so với vét cạn.** Lưới `k` = 1…200 dùng `new RngStream(hash32("edt", k))`:
- `k = 1`: 1 × 64; `k = 2`: 64 × 1; `k = 3`: mask rỗng; `k = 4`: mask đầy; `k = 5`: đúng một ô ngẫu nhiên;
- các `k` khác: `w`, `h` trong [1; 64], mỗi ô là 1 với xác suất `p` ‰, `p` chọn trong [1; 600].

Vét cạn: với mỗi ô, lấy min trên mọi ô mask (mask rỗng thì `EDT_INF`). Phải bằng `edtSquared` ở mọi ô. In số lưới và tổng số ô đã so. Thời hạn 60 000 ms như mục 4b.

**c. Ca lỗi:** `w = 0`, `h = 4097`, `mask` sai cỡ ném `RangeError`.

### 6. Test `fields-sample.test.ts`: bộ trường mẫu

Đọc hai fixture của 028 (đường dẫn tương đối từ `map/`: `../../../tools/map-factory/test/fixtures/gameplay/…`). Trước hết kiểm sha256 của cả file (`node:crypto`, trên byte đọc từ đĩa) và trường `hash` của chúng bằng các giá trị ở mục "Phụ thuộc"; sai thì test hỏng với lời nhắn "chạy lại phiếu 028".

**Rồng** (`dragon-hold.L2-cau.json`): lưới `{ originX: −7200, originZ: −7200, cellCm: 50, w: 288, h: 288 }` (đúng `terrain.sizeCm` 14 400). Bốn trường, theo thứ tự:
1. `lanes`: với mỗi phần tử của `lanes`: `rasterPolyline(points, halfWidthCm)`. Làn trời (`sky`) không vào;
2. `river`: với `k` = 0 … n − 2: `rasterPolyline([points[k], points[k + 1]], Math.floor((widthsCm[k] + widthsCm[k + 1]) / 4))`;
3. `dais`: `rasterDisc(dais.at[0], dais.at[1], dais.radiusCm)`;
4. `slots`: với mỗi ô: `rasterDisc(at[0], at[1], 150)`.

**Lời Gọi** (`typing-defense.w1-silverfall.json`): lưới `{ originX: −4800, originZ: −4800, cellCm: 50, w: 192, h: 192 }` (sân 96 m). Bốn trường, theo thứ tự:
1. `roads`: với mỗi tuyến của `routes`: `rasterPolyline(points, rules.roadHalfCm)`;
2. `water`: với mỗi rect của `water`: `rasterRect(x0, z0, x1, z1)`;
3. `keep`: `rasterDisc(keep.at[0], keep.at[1], rules.keepClearCm)`;
4. `blockers`: mỗi cây của `trees`: `rasterDisc(x, z, rules.treeRadiusCm)`; mỗi nhà của `preset`: `rasterDisc(at[0], at[1], footprintCm)`; mỗi mỏ của `nodes`: `rasterDisc(at[0], at[1], rules.footprintCm.L)`.

Mỗi trường: tô vào một mask mới, rồi `edtSquared(mask, w, h)`.

**Byte của một bộ trường** (để băm): với từng trường theo thứ tự: byte UTF-8 của tên, một byte `0x00`, `w` dạng uint32 little-endian, `h` dạng uint32 little-endian, rồi `w·h` giá trị của `edtSquared` dạng int32 little-endian theo thứ tự chỉ số. Viết little-endian tường minh (`DataView` hay `Buffer.writeInt32LE`), không dựa vào thứ tự byte của máy. Băm là sha256 hex chữ thường của toàn bộ dãy byte (`node:crypto`).

Test làm:
- dựng hai bộ trường, in mỗi bộ một dòng: `field-set <tên fixture> <sha256> <số byte>`; với từng trường in số ô mask bằng 1 và giá trị lớn nhất của `edtSquared`;
- **so với số vàng** ở hai bảng dưới (khẳng định: lệch thì test hỏng): băm và số byte của từng bộ; số ô mask và giá trị lớn nhất của từng trường;
- dựng lại lần hai trong cùng tiến trình: dãy byte giống hệt lần một;
- **đo thời gian** bộ trường của Rồng (4 trường ở 288², gồm tô và EDT): chạy 1 lần làm nóng, rồi 5 lần đo bằng `performance.now()`; in trung vị và cả 5 số. Test chỉ hỏng khi trung vị > 250 ms (dấu hiệu thuật toán sai bậc). Đích thật là ≤ 60 ms trên M4, ghi ở mục Kiểm.

**Băm vàng của bộ trường:**

| Fixture | sha256 của bộ trường | Số byte |
|---|---|---:|
| `dragon-hold.L2-cau.json` | `ca039deb73b5dc47e0a90ba7cd354719fed12419de77c7602a44e04cae2542b4` | 1327159 |
| `typing-defense.w1-silverfall.json` | `885278a7f3e1547fee5d7c0c04fde305d54cec8c4cc6cf35f6717c2090f30507` | 589882 |

Số byte: Rồng `4 · 288 · 288 · 4 + 55`, vì bốn tên dài 5, 5, 4, 5 byte, và mỗi tên kèm 9 byte (`0x00`, rồi 8 byte của `w`, `h`). Lời Gọi `4 · 192 · 192 · 4 + 58`, với tên dài 5, 5, 4, 8 byte.

**Số vàng của từng trường:**

| Fixture | Trường | Số ô mask bằng 1 | Giá trị lớn nhất của `edtSquared` |
|---|---|---:|---:|
| Rồng | `lanes` | 613 | 43573 |
| Rồng | `river` | 3794 | 38597 |
| Rồng | `dais` | 208 | 38088 |
| Rồng | `slots` | 445 | 33800 |
| Lời Gọi | `roads` | 2632 | 8689 |
| Lời Gọi | `water` | 1152 | 19881 |
| Lời Gọi | `keep` | 1402 | 31705 |
| Lời Gọi | `blockers` | 1692 | 5941 |

Claude tính các số này bằng một bản cài riêng, chạy hai lần, cùng kết quả. Một người phản biện cài lại độc lập chỉ từ chữ trong phiếu, trên hai fixture do chính họ làm theo phiếu 028, ra đúng từng số.

Nếu lệch: so số ô mask và giá trị lớn nhất của từng trường với bảng để biết trường nào sai. Rồi tìm chỗ làm sai phiếu: thứ tự trường, luật tâm ô, bán kính, thứ tự byte. Không sửa số cho khớp. Nếu mọi số đếm đã đúng mà băm vẫn lệch, ghi rõ vào báo cáo.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và dòng kết quả vào báo cáo.

1. `pnpm --dir shared/game-kit exec vitest run map` đạt. In số file và số test (trước phiếu: 3 file, 122 test; sau phiếu: 6 file).
2. `pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json` thoát 0.
3. Lint của 027 (trong lệnh 1) đạt: danh sách file đã quét là 5 file `edt.ts`, `hash.ts`, `index.ts`, `raster.ts`, `seeds.ts`, 0 vi phạm.
4. Vét cạn: 200 ca tô hình và 200 lưới EDT đều bằng nhau ở mọi ô. In số ca và số ô đã so. 13 ca tính tay của tô hình và 3 ca của EDT đúng như bảng.
5. Chạy lệnh 1 hai lần. Hai dòng `field-set` của mỗi fixture giống hệt nhau giữa hai lần, và bằng băm vàng ở mục 6 (`ca039deb…42b4`, 1327159 byte; `885278a7…0507`, 589882 byte). Ghi hai băm, số ô mask và giá trị lớn nhất của từng trường vào báo cáo, cạnh số vàng.
6. Thời gian: trung vị của bộ trường Rồng (4 trường ở 288²). Đích ≤ 60 ms trên M4, đo lúc máy không chạy việc nặng khác. Quá 60 ms thì ghi rõ trong báo cáo, kèm phần tốn nhất (tô hay EDT); không ghi "đạt".
7. Không hỏng phần còn lại của kit: `pnpm --dir shared/game-kit exec vitest run` đạt (trước phiếu: 39 file, 411 test), `pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit` thoát 0.
   - Chạy hai lệnh này lần lượt, không song song.
   - Khi máy bận, một test cũ ngoài `map/` có thể quá thời hạn 5 s (phiếu 027 gặp ở `typing/session.test.ts`). Khi đó chạy lại cả lệnh một mình. Đạt khi lần chạy lại đạt; ghi cả hai lần vào báo cáo. Không sửa test ngoài phạm vi.
8. Chạy lại `git status --short --untracked-files=all` và so với kết quả đã giữ lúc bắt đầu. Lúc cuối chỉ được có **thêm** các file trong "Chỉ được ghi", cộng một dòng ` M shared/game-kit/map/index.ts`. Không có dòng ` M` hay ` D` mới nào khác, kể cả với file của 027 và 028. Các dòng đã có lúc bắt đầu (ví dụ file của 028 và file phiếu chưa commit) ghi lại vào báo cáo, nhưng không đụng.

## Báo cáo `docs/codex-queue/029-report.md`

- Các file đã viết, mỗi file một dòng.
- Kết quả tám lệnh kiểm, kèm số.
- Bảng bộ trường mẫu: fixture, trường, số ô mask, giá trị lớn nhất; băm của hai bộ trường; thời gian (trung vị và 5 số).
- Những chỗ phiếu chưa rõ và cách đã chọn.

**Xong khi:** tám lệnh kiểm đều đạt (mục 6: đạt, hoặc đã ghi rõ vì sao chưa đạt) và báo cáo đã viết.
