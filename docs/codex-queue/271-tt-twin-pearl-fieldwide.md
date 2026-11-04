# Phiếu 271 · Tu Tiên · Code: Song Long toàn sân, phiếu 1 (nội dung, sim, lab, test)

Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/271/section9-design.md` §9.0–§9.11. Đây là bản chụp §9 của `docs/games/tu-tien/skills/DRAGON_SKILL.md` lúc giao (04/11/2026 19:55, md5 `48f97024a99c11ef3f8cca8d2ddd8a29`). Mọi §9.x trong phiếu là của file này.

**Đường duyệt:**
- Claude tự phân tích (làn 1), theo bước 9 của skill `agent-orchestration`.
- Thiết kế: phản biện A1–A3. Phiếu: B1–B3, rồi tách làm hai phiếu.
- Phiếu 1: S1 FAIL, S2 FAIL (đều đã sửa), **S3 PASS, S4 PASS**: đủ hai lượt PASS liên tiếp.
- Sau S4 chỉ thêm các quyết định của anh lúc 19:40:
  - `pool.sideW100` 250 → 200;
  - chữ người chơi thấy bằng tiếng Anh;
  - ghi rõ phần nào thuộc phiếu 1.

**Báo cáo:** tin nhắn cuối của Codex (`run.sh` lưu ở `.local/codex-runs/271-tt-twin-pearl-fieldwide/last.md`). Claude chép vào `docs/codex-queue/271-report.md`.

**Claude đã chuẩn bị** (mục "Claude chuẩn bị trước khi giao" bên dưới, bước 1–3):
- worktree `games/.wt-ic-twin-fieldwide`, nhánh `codex/twin-pearl-fieldwide` từ `main` của game, `be7cfa0`; `main` này gồm các phiếu 258, 258b và việc đổi mặt C3, đều không đụng file của phiếu này;
- symlink `node_modules`;
- bản chép `tmp/skill-reach/`;
- golden cờ tắt có sẵn ở đường tuyệt đối đã ghi.

Bỏ qua bước 4 (Claude đã ghi phiếu này). Phần F (bot) là phiếu 2, giao sau khi Claude merge phiếu này.

### 9.12 Ticket Codex: lời giải đầy đủ

**Thợ:** Codex `gpt-6.1-sol`, effort `xhigh` (code và logic), một lane, **hai phiếu nối nhau**: phiếu 1 là A–E (nội dung, sim, lab, test); phiếu 2 là F (bot và số đo), giao sau khi Claude đã duyệt và merge phiếu 1. Sandbox `workspace-write`, thư mục làm việc là cây riêng `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide` trên nhánh `codex/twin-pearl-fieldwide` (không dùng `games/.wt-immortality-cultivation-codex`: cây đó đang giữ việc chưa duyệt của phiếu 258 và đã được phiếu 259 đặt chỗ). Mọi đường dẫn dưới đây tính từ thư mục đó. Báo cáo của Codex là tin nhắn cuối (`run.sh` lưu ở `.local/codex-runs/<id>/last.md`); Claude chép nó vào `docs/codex-queue/` của repo cha. Codex không commit; Claude chạy lại kiểm tra, đọc diff, rồi mới merge.

**Claude chuẩn bị trước khi giao** (Codex không tự làm):
1. `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-twin-fieldwide -b codex/twin-pearl-fieldwide main`, rồi `ln -s ../immortality-cultivation/node_modules /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/node_modules` (liên kết như phiếu 255). Phiếu 2 dùng lại đúng cây và nhánh này sau khi Claude đã merge phiếu 1 (cây vẫn giữ bản chép `tmp/skill-reach/` của bước 2). Vì liên kết đó, mọi lệnh test và build ở E.1 dùng đúng dạng của báo cáo 255 (không ghi gì vào `node_modules` của cây chính).
2. Chép `tmp/skill-reach/` của cây chính vào cây mới (bot nhập `../../src/...` theo thư mục của chính nó, nên phải chạy bản trong cây mới).
3. Golden cờ tắt để so nằm ở đường tuyệt đối `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`.
4. Ghi hai phiếu ở `docs/codex-queue/` của repo cha. **Phiếu 1** `<n>-tt-twin-pearl-fieldwide.md`: dòng đầu "Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md` §9.0–§9.11; mọi §9.x trong phiếu là của file này", rồi phần đầu §9.12 và A–E. **Phiếu 2** `<n+1>-tt-twin-pearl-fieldwide-bot.md`: cùng dòng đầu, phần đầu §9.12, B.1, B.3, B.6, dòng "Sân tổng hợp cho test" của D, và F. Trước khi chạy phiếu 2: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide merge --ff-only main` để cây có đúng bản phiếu 1 đã merge. Chạy lần lượt (phiếu 2 sau khi phiếu 1 đã merge): `tools/codex-run/run.sh <n>-tt-twin-pearl-fieldwide docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md games/.wt-ic-twin-fieldwide xhigh workspace-write`, và tương tự cho phiếu 2.

**Được ghi:**
- `src/content/data/twin-pearl.ts` (chỉ phiếu 1)
- `src/sim/twin-pearl.ts` (chỉ phiếu 1)
- `src/sim/combat.ts` (chỉ thêm một hàm xuất, §B.7; chỉ phiếu 1)
- `tests/sim/twin-pearl.test.ts` (chỉ phiếu 1)
- `src/lab/twin-pearl-greybox.ts`, `src/lab/skills-main.ts` (chỉ phần hộp xám; chỉ phiếu 1)
- `tmp/skill-reach/**` (ngoài Git; chỉ phiếu 2)
- thư mục build tạm `/private/tmp/codex-twin-fieldwide-dist` (xóa sau khi kiểm; chỉ phiếu 1)

**Chữ:** mọi chữ người chơi thấy, và mọi nhãn mới trong lab, bằng tiếng Anh (luật chữ của game; §9.11).

**Luật chung của `run.sh`** cấm chạy build và bộ test của game và cấm sửa `src`, `tests`: phiếu này ghi đè luật đó, chỉ trong cây của Codex và chỉ cho các file ở danh sách "Được ghi" và các lệnh ở E và F.

**Cấm:**
- sửa canon, `rules.ts`, `school-kiem.ts`, `field.ts`, `spawn.ts`, `src/kit/**`, game khác;
- đổi bất kỳ hành vi nào khi cờ tắt;
- đổi `hit()`, `mayHit()`, `falloffPm()`, `postureOf()`, `twinPearlPool()` ngoài phần ghi ở dưới;
- số thực trong trạng thái sim; mở cổng mạng; commit.

#### A. Nội dung: `src/content/data/twin-pearl.ts`

Đổi `pool.sideW100` từ 250 thành **200** (2,0 W mỗi bên, anh duyệt, §9.11); `pool.skyW100` giữ 80. Giữ `SwordKey2`, `SWORD_KEY2_VARIANTS`, `id`, `name`, `sharesPct`, `maxHits`, `rehitTicks`, `bossCapW100`, `trailTicks`, `groundTopMm`. Thay phần hình học:

```ts
hold:   { tick: 0, radiusMm: 4500 },                       // F0 ground disc round the formation centre
touch:  { fromTick: 1, toTick: 2, radiusMm: 2200 },        // F1–F2 one disc per side, centre fixed at F1
pearl:  { pullPm: 600, maxMm: 12_000, insetMm: 2000, emptyMm: 9000, fromTick: 3, arriveTick: 48 },
anchors:{ max: 3, minGapMm: 3000 },
wingMm: 9000,
heads:  { fromTick: 3, toTick: 48, radiusMm: 1400, amplitudeMm: 900, halfWaveMm: 4000, sampleMm: 500, maxSamples: 256, maxSegmentMm: 32_000 },
sky:    { fromTick: 30, toTick: 56, radiusMm: 3000, bottomMm: 2500, topMm: 6000 },
roar:   { fromTick: 49, toTick: 56 },                      // view only
lotus:  { fromTick: 57, toTick: 77, radiusMm: 9000, coreMm: 4000, petalLengthMm: 13_000, petalHalfWidthMm: 2200, outsidePm: 500 },
```

Bỏ `meetFallbackMm` và hộp `hold.halfWidthMm/depthMm`, `touch.halfLengthMm/halfWidthMm`, `heads` cũ, `sky` cũ, `lotus` cũ. `TWIN_PEARL_END_TICK` vẫn là `max(heads.toTick + trailTicks, lotus.toTick, sky.toTick)` = 102. Sửa lời chú thích đầu file theo §9 (không còn hành lang hay cổng). `rulesHash` tự phủ bảng mới vì `matchRulesHash` đã đẩy `TWIN_PEARL` khi có cờ: không sửa `app.ts`.

#### B. Sim: `src/sim/twin-pearl.ts`

**B.1 Bỏ:** `TwinLane`, `TwinGeometry`, `TwinTouch`, `geometryCache`, `laneRoute`, `lastBend`, `buildLane`, `twinPearlGeometry`, `inHold` (hộp), `inTouch` (hộp), `routeDirection`, `pickTouches`, các hằng mô-đun đọc trường đã bỏ (`HOLD_HALF`, `HOLD_DEPTH`, `TOUCH_HALF_LEN`, `TOUCH_HALF_W`), `skyFront`, `inSky`, `inPetal` và `lotusRegion` bản theo hành lang, `sideOf` theo cổng.

**B.2 Giữ nguyên:** `TwinKind`, `KIND_BIT`, `KIND_ORDER`, các `POOL_*`, `TwinVictim`, `createTwinPearlState`, `swordKey2Of`, `falloffPm`, `postureOf`, `twinPearlPool`, `bookOf`, `mayHit`, `hit` (trừ dòng lấy bên, B.5), `stepTwinPearl`, phần `declare module`.

**B.3 Bản ghi lần tung** (`TwinPearlCast`, thêm, toàn số nguyên; giữ mọi trường cũ trừ `touch`):

```ts
readonly hx: number; readonly hz: number;            // H (u)
readonly fx: number; readonly fz: number;            // F (‰)
readonly rx: number; readonly rz: number;            // R (‰)
readonly cut2: number;
readonly px: number; readonly pz: number;            // the pearl P (u)
readonly sideSlot: number[];                         // by beast slot: 0 none, 1 side 0, 2 side 1 (grow with push(0), like bookAt: no holes)
readonly sideSerial: number[];                       // by beast slot: the serial the side belongs to
readonly dragons: readonly [TwinDragon, TwinDragon];
readonly disc: [TwinDisc, TwinDisc];                 // F1 discs, set at t = 1
readonly snapshot: number[];                         // [slot, serial] pairs of the F0 snapshot (F1 targets come only from it)

interface TwinDragon {
  readonly nodes: number[];                          // control points x0, z0, x1, z1 … (C, anchors…, P) after merging duplicates (before the long-segment split)
  readonly sx: number[]; readonly sz: number[];      // samples (u), clamped into the field
  readonly arc: number[];                            // cumulative arc on the clamped samples (u)
  readonly pass: number[];                           // tick offset the head passes each sample (3…48)
  readonly petalFrom: number;                        // first sample index with arc[last] − arc[i] ≤ petalLength
  readonly sky: number[];                            // sky anchors x, z … (this side's snapshot flyers at F0)
}
interface TwinDisc { on: number; x: number; z: number; sky: number }   // sky: 0 ground disc, 1 sky disc
```

**B.4 Dựng hình học ở F0** (xuất `buildCastGeometry(world, cast)` cho test và bot; gọi trong `resolveTwinPearl` trước khi đẩy bản ghi; trả các trường B.3):
1. **Ảnh chụp:** duyệt `world.beasts.list` theo thứ tự mảng: `alive && !damageImmune(world, beast)`.
2. **Trục và bên:**
   - F, R theo §9.3, cộng `+ 0` vào mỗi thành phần để không có −0 (ví dụ R = (−F.z + 0, F.x + 0)); "fieldCentre" = (mulDivSym(minX + maxX, 1, 2); mulDivSym(minZ + maxZ, 1, 2)) của `world.stage.field` đổi sang u.
   - Sắp bằng so sánh (v, u, serial). Ghi `sideSlot` và `sideSerial` cho từng con.
   - `cut2` như §9.3.
3. **Ngọc:** §9.4. Độ dài |P − H| = `isqrt(dist2)`. Kẹp: x vào [minX + inset; maxX − inset], nếu minX + inset > maxX − inset thì x = mulDivSym(minX + maxX, 1, 2); z tương tự.
4. **Neo:** §9.4, so bằng `dist2` (số nguyên, không căn).
5. **Thứ tự:**
   - Sinh hoán vị theo thứ tự từ điển; độ dài = Σ `isqrt(dist2)`; giữ hoán vị đầu tiên có độ dài nhỏ hơn hẳn.
   - Không neo: nút C, W, P (W kẹp như P).
   - Bỏ nút trùng nút trước. Lưu các nút này vào `nodes` (việc chia đoạn dài nằm trong `sampleRoute`, bước 6).
6. **Mẫu** (xuất `sampleRoute(nodes, sideSign, field)` trả `{ sx, sz, arc, pass, step }`, và `splitLong(nodes, maxSegU): number[]`; cả hai dùng cho test 4):
   - `sampleRoute` gọi `splitLong` trước: mỗi đoạn A → B dài L > `maxSegmentMm` thành k = ceil(L / maxSeg) đoạn, nút chèn ở A + mulDivSym(B − A, j, k), j = 1…k−1.
   - `sPath(nodes, side 0 ? +1 : −1, step)`: thêm tham số `step` (u) vào `sPath` hiện có, và đổi hai dòng độ lệch thành `x = bx + mulDivSym(-unit.z * off, 1, 1000)`, `z = bz + mulDivSym(unit.x * off, 1, 1000)` (làm tròn đối xứng theo dấu của tích, để ảnh gương trùng tới 0 u; bản cũ lệch 1 u ở các tích tận cùng …500). Không đổi gì khác.
   - `step = max(U(sampleMm), ceil(Σ độ dài đoạn / maxSamples))`.
   - Kẹp từng mẫu vào khung sân. Tính lại `arc`.
   - `pass[i] = heads.fromTick + mulDiv(arc[i], heads.toTick − heads.fromTick, arcTổng)` (arcTổng = 0: mọi `pass = fromTick`).
   - Nếu chỉ có 1 nút: một mẫu ở C, `arc = [0]`, `pass = [3]`.
7. **Cánh hoa sen:** `petalFrom` = chỉ số nhỏ nhất i có arc[last] − arc[i] ≤ petalLength.
8. **Neo trời:** các con ảnh chụp ở dải trời, theo bên của chúng, thứ tự ảnh chụp.

**H** là `heartPoint()` (gốc tọa độ hôm nay); không có trường nào khác giữ nó.

**B.5 Bên của thú khi vào sổ** (thay `sideOf(beast)` trong `hit()`): `sideFor(cast, beast)`:
- `sideSlot[slot] ≠ 0` và `sideSerial[slot] = serial`: lấy bên đã lưu.
- Ngược lại: v = mulDivSym((x − hx)·rx + (z − hz)·rz, 1, 1000); bên 0 nếu 2v < cut2, bên 1 nếu 2v > cut2, ngược lại `serial % 2`. Ghi lại vào `sideSlot` và `sideSerial`.

**B.6 Khối trúng** (hàm thuần, xuất ra cho test, lab và bot):
- `inHoldDisc(cast, x, z)`: `within(x, z, hx, hz, hold.r)`.
- `inDisc(disc, x, z)`: `disc.on && within(x, z, disc.x, disc.z, touch.r)`.
- `liveSamples(dragon, t, out)`: như hôm nay, trên `dragon.pass`.
- `inSpan(dragon, first, last, x, z, r)`: thêm tham số bán kính.
- `headIndex(dragon, t)`: mẫu cuối có `pass ≤ min(t, heads.toTick)`.
- `inSkyReach(cast, x, z, t)`: t ∈ [30; 56] và có ít nhất một rồng thỏa một trong hai:
  - `distSegment2(x, z, head, anchor) ≤ (3 m)²` với một neo trời của rồng đó;
  - `inSpan(dragon, span, 3 m)`.
- `distSegment2`: chiếu nguyên như `inPetal` cũ. `along` dùng `floor(dot / len)` và kẹp vào [0; len]; điểm gần nhất bằng `mulDivSym`. Đoạn dài 0 (đầu rồng trùng neo): khoảng cách tới điểm đó.
- `inBody(dragon, x, z, t)`: viết lại trên `liveSamples` và `inSpan` với r 1,4 m. `inGroundBand`, `inSkyBand` giữ nguyên.
- `staticCoverage(cast, points)`: nhận vị trí F0 của các thú ảnh chụp (x, z, y), trả số con nằm trong ít nhất một khối đúng dải ở một tick nào đó F0–F102, bỏ qua máu, ngân sách, trần và khoảng trúng lại; đĩa F1 lấy từ bản ghi (sau t = 1). Dùng cho test và bot.
- `lotusRegion(cast, x, z)`:
  - 2 (đầy) nếu một trong các điều: `within(P, coreMm)`, `inHoldDisc`, hoặc trong `petalHalfWidth` của một đoạn [k; k+1] với k ≥ max(0, petalFrom − 1) của một rồng (đoạn đầu có thể vươn quá 13 m tối đa một bước mẫu: chấp nhận);
  - 1 (nửa) nếu không đầy nhưng `within(P, radiusMm)`;
  - 0 nếu không.
- `volumesAt(cast, x, y, z, t)`: bit như hôm nay (1 đĩa F0, 2 đĩa F1 đất hay trời theo dải của đĩa, 4 thân, 8 trời F30–F56, 16 hoa sen đầy, 32 hoa sen nửa), nay nhận `cast` thay `geo`.

**B.7 Đĩa F1** (`pickDiscs(world, cast)` ở t = 1):
- Với mỗi bên s, duyệt các cặp của `snapshot` có bên s; lấy con bằng `beastByRef(world, { slot, serial })` (`src/sim/combat.ts`; thêm `beastByRef` vào dòng import từ `./combat`), bỏ cặp trả `null` (đã chết hoặc slot đã dùng lại).
- Một con hợp lệ khi:
  - sống, `!damageImmune`;
  - ở dải đất (loại chạm, phần chạm) hoặc dải trời (loại hành lang, phần trời);
  - `mayHit(cast, beast, loại, 1)`;
  - `cast.pool[s·4 + phần] > 0`;
  - không phải Vương, hoặc `bossDealt < bossCap`;
  - nếu thuộc cụm bầy: `areaClusterLeft(world, cast.area, cluster) > 0`.
- Chọn con hợp lệ có dist2 tới H nhỏ nhất (hòa: serial nhỏ). Đặt `disc[s] = { on: 1, x, z, sky }` theo dải của nó.
- **`combat.ts`:** xuất thêm `areaClusterLeft(world, area, cluster)`. Nó trả `area.left[at]` nếu cụm đã có, ngược lại `floor(hp cụm × clusterCapPct / 100)`, **không** đẩy vào `area` (cùng công thức `clusterLeft`). Không đổi gì khác.

**B.8 Mỗi tick** (`stepCast`, thay phần gom ứng viên; giữ cách gom một lượt rồi sắp):
```text
geo đọc từ cast; t = world.tick − startTick
t = 1: pickDiscs
với mỗi thú sống, !damageImmune:
  g = inGroundBand(y), s = inSkyBand(y)
  nếu g và ((t = 0 và inHoldDisc) hoặc (1 ≤ t ≤ 2 và một đĩa F1 đất chứa nó)) và mayHit(chạm)      → chạm, POOL_TOUCH
  ngược lại nếu s và 1 ≤ t ≤ 2 và một đĩa F1 trời chứa nó và mayHit(hành lang)                       → hành lang, POOL_SKY
  ngược lại nếu g và thân một rồng đang sống chứa nó (r 1,4 m) và mayHit(hành lang)                   → hành lang, POOL_CORRIDOR
  ngược lại nếu s và inSkyReach và mayHit(hành lang)                                                   → hành lang, POOL_SKY
  ngược lại nếu g và 57 ≤ t ≤ 77 và lotusRegion ≠ 0 và mayHit(hoa sen)                                 → hoa sen, POOL_LOTUS, nửa nếu vùng = 1
  d = dist2(x, z, hx, hz)                                                                              // thay heartDistance
sắp (KIND_ORDER, d, serial); đánh lần lượt bằng hit() như hôm nay
```
Thoát sớm khi không khối nào sống ở tick t (như hôm nay). Bên của thú trong `hit()` lấy từ `sideFor` (B.5).

**B.9 `resolveTwinPearl`:** điều kiện giải không đổi (có thú nhận được sát thương). Gọi `buildCastGeometry` rồi đẩy bản ghi. Ngân sách vẫn từ `twinPearlPool`.

**Số khung trong mã:** mọi tick ở B.6–B.8 (1–2, 30–56, 48, 57–77, 102) đọc từ `TWIN_PEARL` (`touch`, `sky`, `heads`, `lotus`, `TWIN_PEARL_END_TICK`); không viết số tick trần trong mã, để đổi khung chỉ là đổi bảng (§9.11).

**B.10 Dọn chú thích đầu file** theo §9: không còn hành lang, cổng, góc trời, điểm gặp.

#### C. Lab: `src/lab/twin-pearl-greybox.ts`, `skills-main.ts`

- **Triều thú của lab** (bỏ mọi chỗ dùng `twinPearlGeometry`, `skyFront`, `TwinGeometry`, `along()` theo hành lang):
  - khi dựng lại (R) và lúc mở: đổ bố cục hai cổng của §9.8;
  - phím `L`: đổ bố cục kế tiếp: hai cổng, một cổng, ba cổng, vòng quanh (tám hướng × bán kính 5, 8, 11, 14, 17 m theo thứ tự §9.8, bỏ những điểm ngoài sân hôm nay), sau lưng; lab bỏ thêm những điểm rơi vào ô bị chặn (hai Trận Trụ, kể cả khoảng đệm), vì trong lab thú đi lại;
  - **bỏ hẳn** `refill()` và phần tự bơm cũ ở đầu mỗi `stepWorld()`; phím `N` đổ lại bố cục đang chọn;
  - thú đất đổ bằng `spawnBeast` với nhãn cổng "A" (nhãn không ảnh hưởng hình học); quạ luôn với nhãn "sky" ở y = 4 m;
  - phím `V` thả Vương ở `gatePoint(stage, "A")`;
  - thú đi như thường; bấm phím 2 ngay sau `L` hoặc `N` để tung lúc bố cục còn nguyên. Không sửa sim để giữ thú đứng yên.
- **Vẽ từ bản ghi lần tung đang sống:**
  - đĩa F0, hai đĩa F1 (đất hay trời) và hai sợi sáng từ kiếm;
  - nút và mẫu của hai rồng, đầu rồng ở `headIndex`, vệt theo `liveSamples`. Lưới instanced của thân đủ cho mọi mẫu: tối thiểu 320 thực thể mỗi rồng (`maxSamples` + 1 + số đoạn), hoặc vẽ từ `range.last` lùi về khi vượt;
  - con nhộng trời tới từng neo trời;
  - ngọc bay từ kiếm tới P trong F3–F48;
  - hoa sen: đĩa lõi, cánh và vòng 9 m.
- **Băng tên pha** theo khung mới. **Ô số:** tây/đông thay bằng bên 0 / bên 1 lấy từ `cast.book[].side`; thêm `coverageStatic` của lần tung: ghi vị trí F0 của các thú ảnh chụp ngay sau lệnh `stepWorld()` chạy F0 trong `cast()`, rồi tính một lần khi lần tung tới t ≥ 1 (không tính mỗi khung).
- Thêm `L` vào danh sách nút của bảng, như `N` và `V`.
- Không đổi gì khi không có `?key2=twin-pearl`.

#### D. Test: `tests/sim/twin-pearl.test.ts` (viết lại phần hình học; giữ phần luật sát thương)

Giữ, sửa cho khung mới:
- cờ tắt: header không có `swordKey2`, ô 2 vẫn là đường thẳng, **các băm ghim của `1a78a82` giữ nguyên**;
- `rulesHash` phủ bảng chỉ khi có cờ;
- 3 đòn mỗi thú, mỗi loại 1, cách ≥ 20 tick; phần 15/45/40;
- hệ số giảm dần mỗi bên, sàn 40 %; ngân sách mỗi bên và mỗi phần (nay 2,0 W mỗi bên chia 15/45/40, cộng 0,8 W trời), không phần nào vượt;
- một trần cụm cho cả lần tung; trần Vương theo mã lần tung; chia Thế 3/9/8;
- chỉ giải khi có thú nhận được sát thương; tất định và không số thực (`hashedFloats`).

Thêm (bố cục ở §9.8; thú đứng yên: chỉ gọi `stepSkills` qua `advance`, trừ khi test ghi khác; **mọi lần tung dùng `castOf(world, 2, { origin: at(0, 3) })`**, trừ phần kẹp của test 2 và C xoay của test 9, vì `castOf` mặc định đặt origin ở Trận Tâm):

| # | Test | Kiểm |
|---|---|---|
| 1 | Bên theo trục ngang | Hai cổng: 20/20, mọi con x < 0 bên 0. n = 0, 1, 2 cho đúng `cut2`. Thú đến sau theo `cut2`, hòa theo `serial % 2`, giữ bên tới hết lần tung |
| 2 | Ngọc | Hai cổng: P cách (0; −5,9) ≤ 0,15 m. Mười Phong Lang quanh (−15; −16) (tâm khối cách H khoảng 22 m): \|P − H\| = 12 m ± 2 u. Sân trống (gọi `buildCastGeometry` trực tiếp, origin (0; 3)): P = (0; −9). Kẹp mép: sân trống, `buildCastGeometry(world, castOf(world, 2, { origin: at(0, −3) }))` trên THANH_THACH_AI cho F = (0; 1000) và P = (0; 6 m) (9 m kẹp về maxZ − 2 m) |
| 3 | Neo và đường | Hai cổng: mỗi rồng 3 neo (5 nút: C, 3 neo, P); con xa H nhất của mỗi bên là một nút. Σ isqrt các đoạn nút (C → neo → P, trước sóng S) 45,1 / 43,9 m ± 1 m (nguyên mẫu); `arc` cuối 50,3 / 49,2 m ± 1 m. Đường bắt đầu ở C, kết thúc ở P. Một thú: rồng không có thú đất bay vòng cánh qua H ± 9 m·R |
| 4 | Mẫu | Mọi mẫu trong khung sân. `pass` không giảm, đầu 3, cuối 48. Số mẫu ≤ 257 + số đoạn (sau khi chia). `splitLong` biến một đoạn nút 40 m thành 2 đoạn, mỗi đoạn ≤ `maxSegmentMm` (u). Gọi thẳng `sampleRoute` với một danh sách nút dài ≥ 200 m (đường gấp khúc) trong khung 60 × 60 m (−30 000…30 000 mm): bước > 0,5 m và số mẫu ≤ 257 + số đoạn. (Không dựng world trên sân lớn hơn khoảng 64 × 63,5 m: `field.ts` từ chối từ 16 384 ô) |
| 5 | Đĩa F0 và F1 | Con trong r 4,5 m quanh H nhận chạm ở F0. Với `cast.pool.fill(10 ** 9)` ngay sau khi giải (như các test đám đông hiện có): mỗi bên, con gần H nhất ngoài đĩa F0 nhận chạm ở F1. Không bơm ngân sách, bố cục hai cổng **bỏ hai quạ**: bên có con bị chạm ở F0 đã cạn phần chạm, nên `disc[s].on === 0`. Cùng bố cục **có quạ**: đĩa của bên đó là đĩa trời ở quạ của bên đó (`disc[s].sky === 1`), quạ nhận hành lang từ phần trời ở F1. Con gần nhất bị trần cụm chặn (cụm 1 máu): bỏ qua, chọn con kế |
| 6 | Thân, trời, hoa sen theo khung | Chạy với `cast.pool.fill(10 ** 9)` sau khi giải, để quạ không là mục tiêu F1. Con trên đường rồng nhận hành lang khi đầu qua và tới 54 tick sau. Quạ không nằm trên đường nhận hành lang qua con nhộng, đúng ở F30 (nó nằm ở đầu con nhộng của chính nó). Thú đất dưới con nhộng không bị trời trúng. Hoa sen đầy trong lõi, đĩa H và cánh; nửa trong 9 m quanh P; không gì ngoài 9 m quanh P trừ cánh và đĩa H r 4,5 m. Không đòn nào sau F102 |
| 7 | Bảy bố cục | Mỗi bố cục có thú: đòn dương đầu tiên ở F0 hoặc F1. `coverageStatic` ≥ 95 % (hai cổng, ba cổng), ≥ 85 % (một cổng, sau lưng), ≥ 75 % (đấu trường). Số con bị trúng ≤ tổng con và mọi phần ngân sách ≥ 0. Sân trống: dựng hình học không lỗi, không đòn |
| 8 | Gương | Hai cổng lật x → −x, giữ serial; C = (0; 3) không đổi: bên 0 ↔ 1. Mọi đòn (serial, tick, loại, máu) trùng, dung sai 0. Nút, mẫu và `pass` là ảnh gương, dung sai 0 u |
| 9 | Xoay | Đấu trường trên sân 40 × 40 m, xoay 90° (x, z) → (−z + 0, x) (cộng `+ 0` để không có −0, như test gương hiện có), cả C: (0; 3) thành (−3; 0). Mọi đòn trùng, dung sai 0. Mẫu xoay đúng, dung sai 0 u |
| 10 | Không đọc cổng | Cùng vị trí, đổi nhãn cổng A ↔ B của mọi thú đất: mọi đòn trùng |
| 11 | Tất định | Hai lần chạy một seed, có thú di chuyển và hai lần tung chồng nhau: cùng băm mỗi tick. Bản ghi lần tung chỉ có số nguyên |
| 12 | Hiệu năng (khói) | 60 thú, hai lần tung chồng nhau, 102 tick, chạy nóng máy 3 lần trước: in thời gian dựng hình học và µs mỗi tick mỗi lần tung. Chỉ làm hỏng test khi trung vị vượt 4 lần đích (0,8 ms; 200 µs) |

**Sân tổng hợp cho test:** `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }` qua `makeWorld({ stage })`. Kiểm trước rằng `createWorld` chạy được với nó; nếu không, dừng và ghi vào báo cáo, không sửa `field.ts`.

#### E. Kiểm của phiếu 1 (Codex chạy, Claude chạy lại)

1. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` xanh, gồm test băm ghim cờ tắt `1a78a82`. `node node_modules/typescript/bin/tsc --noEmit -p .` xanh. Build không ghi vào cây: `IC_VITE_CACHE_DIR=/private/tmp/codex-twin-fieldwide-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-twin-fieldwide-dist --configLoader runner` xanh (như phiếu 255), rồi xóa thư mục đó. `node src/kit/verify-kit.mjs` xanh.
2. Hiệu năng (test 12, 60 thú, sau 3 lần chạy nóng máy): đạt nếu trung vị dựng hình học ≤ 0,2 ms và trung vị ≤ 50 µs mỗi tick mỗi lần tung; trượt thì báo số, không tối ưu bằng cách đổi luật.
3. Phiếu 1 không chạy bot: sau phiếu 1, các script ở `tmp/skill-reach/` còn nhập tên đã bỏ; phiếu 2 sửa chúng.
4. `grep -n "heartDistance" src/sim/twin-pearl.ts` không ra gì, kể cả trong chú thích (thứ tự đánh dùng `dist2` tới H, §9.6; đừng chép chú thích `// thay heartDistance` của B.8 vào mã).
5. **Báo cáo:** file đã đổi, kết quả từng lệnh, số của test 12, mọi chỗ làm khác phiếu và lý do.
