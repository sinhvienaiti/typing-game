# Phiếu 272 · Tu Tiên · Bot và số đo Song Long toàn sân (phiếu 2 của §9.12)

Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/272/section9-design.md` §9.0–§9.11. Đây là bản chụp §9 của làn 1 lúc giao (04/11/2026 21:22, md5 `32e3ffa4080d10635811f18fa274a0be`). Mọi §9.x trong phiếu là của file này.

**Đường duyệt:**
- Claude tự phân tích (làn 1), theo bước 9 của skill `agent-orchestration`.
- Phiếu 2: T1, T2, T3, U1, U2 FAIL, mỗi lỗi đã sửa; **U3 PASS, U4 PASS** (đủ hai lượt liên tiếp, U4 lúc khoảng 21:35).
- Claude (người chốt) giao khi mới có một PASS, vì làn Codex sắp trống (luật "đừng để Codex ngồi không"). Lượt phản biện kế tiếp chạy song song làm kiểm thêm; lỗi nó tìm ra sẽ thành phiếu sửa nối tiếp.

**Trạng thái mã:** phiếu 271, 271b, 271c đã gộp vào `main` của game ở `35f1b77`.
- Claude đã chạy `git -C …/games/.wt-ic-twin-fieldwide merge --ff-only main` trước khi giao, nên cây có đúng bản đã gộp.
- Riêng 271c: chiêu **chỉ giải khi có thú trong dải đất hoặc dải trời**. Lần tung không giải được (không thú nào trong dải) tính là "giữ", không phải "tung mà 0 đòn".

**Báo cáo:** tin nhắn cuối (`.local/codex-runs/272-tt-twin-pearl-fieldwide-bot/last.md`). Claude chép vào `docs/codex-queue/272-report.md`.

### 9.12 Ticket Codex: lời giải đầy đủ

**Thợ:** Codex `gpt-6.1-sol`, effort `xhigh` (code và logic), một lane, **hai phiếu nối nhau**: phiếu 1 là A–E (nội dung, sim, lab, test); phiếu 2 là F (bot và số đo), giao sau khi Claude đã duyệt và merge phiếu 1. Sandbox `workspace-write`, thư mục làm việc là cây riêng `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide` trên nhánh `codex/twin-pearl-fieldwide` (không dùng `games/.wt-immortality-cultivation-codex`: cây đó dành cho phiếu 259). Mọi đường dẫn dưới đây tính từ thư mục đó. Báo cáo của Codex là tin nhắn cuối (`run.sh` lưu ở `.local/codex-runs/<id>/last.md`); Claude chép nó vào `docs/codex-queue/` của repo cha. Codex không commit; Claude chạy lại kiểm tra, đọc diff, rồi mới merge.

**Claude chuẩn bị trước khi giao** (Codex không tự làm):
1. `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-twin-fieldwide -b codex/twin-pearl-fieldwide main`, rồi `ln -s ../immortality-cultivation/node_modules /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/node_modules` (liên kết như phiếu 255). Phiếu 2 dùng lại đúng cây và nhánh này sau khi Claude đã merge phiếu 1 (cây vẫn giữ bản chép `tmp/skill-reach/` của bước 2). Vì liên kết đó, mọi lệnh test và build ở E.1 dùng đúng dạng của báo cáo 255 (không ghi gì vào `node_modules` của cây chính).
2. Chép `tmp/skill-reach/` của cây chính vào cây mới (bot nhập `../../src/...` theo thư mục của chính nó, nên phải chạy bản trong cây mới).
3. Golden cờ tắt để so nằm ở đường tuyệt đối `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`.
4. Ghi hai phiếu ở `docs/codex-queue/` của repo cha. **Phiếu 1** `<n>-tt-twin-pearl-fieldwide.md`: dòng đầu "Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md` §9.0–§9.11; mọi §9.x trong phiếu là của file này", rồi phần đầu §9.12 và A–E. **Phiếu 2** `<n+1>-tt-twin-pearl-fieldwide-bot.md`: cùng dòng đầu nhưng "§9.0–§9.11 và §8", phần đầu §9.12, B.1, B.3, dòng tiêu đề của B.4 (`buildCastGeometry`), B.6, dòng đầu của B.7 (`pickDiscs` ở t = 1), dòng "Sân tổng hợp cho test" của D, và F. Trước khi chạy phiếu 2: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide merge --ff-only main` để cây có đúng bản phiếu 1 đã merge. Chạy lần lượt (phiếu 2 sau khi phiếu 1 đã merge): `tools/codex-run/run.sh <n>-tt-twin-pearl-fieldwide docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md games/.wt-ic-twin-fieldwide xhigh workspace-write`, và tương tự cho phiếu 2.

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

#### Trích B (đã có trong mã đã gộp, để đọc)

**B.1 Bỏ:** `TwinLane`, `TwinGeometry`, `TwinTouch`, `geometryCache`, `laneRoute`, `lastBend`, `buildLane`, `twinPearlGeometry`, `inHold` (hộp), `inTouch` (hộp), `routeDirection`, `pickTouches`, các hằng mô-đun đọc trường đã bỏ (`HOLD_HALF`, `HOLD_DEPTH`, `TOUCH_HALF_LEN`, `TOUCH_HALF_W`), `skyFront`, `inSky`, `inPetal` và `lotusRegion` bản theo hành lang, `sideOf` theo cổng.

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

#### Trích D

**Sân tổng hợp cho test:** `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }` qua `makeWorld({ stage })`. Kiểm trước rằng `createWorld` chạy được với nó; nếu không, dừng và ghi vào báo cáo, không sửa `field.ts`.

#### F. Phiếu 2: bot và số đo (`tmp/skill-reach/`, ngoài Git)

**Phạm vi:** phiếu 2 chỉ ghi `tmp/skill-reach/**`; không sửa `src/`, `tests/` hay số trong `src/content/data/twin-pearl.ts`. Cần đổi sim thì dừng và ghi vào báo cáo. Sim là bản phiếu 1 đã merge (B.1, B.3, B.6 và sân tổng hợp của D có trong phiếu này).

**Cách chạy mọi script** (CLI `tsx` bị sandbox chặn với `listen EPERM`, như phiếu 195, 223): `TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/<script>.ts …`. Thay hai chỗ `node_modules/.bin/tsx` trong `key2-matrix.sh` bằng đúng dạng đó. Mọi kết quả mới ghi vào `tmp/skill-reach/key2-fieldwide/`; không ghi vào `key2/`, `key2-fix/`, `key2-review/` (đó là nguồn của các cột so ở §8).

**Sửa script:**
1. `key2-measure.ts` (theo §9.8 bot bước 1):
   - bỏ phủ theo hành lang (`laneRoutes`, `coverage()`, `coverA/B`) và mọi chỗ nhập hay gọi các tên đã bỏ ở B.1: `TwinLane`, `TwinGeometry`, `TwinTouch`, `laneRoute`, `twinPearlGeometry`, `inHold`, `inTouch`, `skyFront`, `inSky`, `inPetal`, `sideOf`; `lotusRegion` nay nhận `cast` (B.6);
   - trận "line" (cờ tắt) cũng bỏ `coverA/B`, không thay, và giữ mọi trường cũ khác (cả `reachW/E`);
   - trận có cờ, mỗi lần tung, ghi thêm:
     - đọc ngay lúc bắt đầu ghi lần tung (`start()`: trong quét đỉnh là ngay sau `resolveCast`, trong trận là sau tick F0; trong trận vị trí có thể lệch vài cm vì một số bước sau kỹ năng cũng dời thú, chỉ ảnh hưởng số phủ của trận thật, không có ngưỡng), trước khi `sideFor` có thể ghi đè `sideSlot` cho một slot dùng lại: số thú ảnh chụp mỗi bên, tách đất và trời (đếm `snapshot` theo `sideSlot` và dải độ cao); số quạ mỗi bên;
     - vị trí F0 (x, z, y) của các thú ảnh chụp lúc tung; khi lần tung đã qua t = 1 (sau tick có `pickDiscs`), gọi `staticCoverage` mỗi lần tung hai lần, một lần với các điểm đất và một lần với các điểm trời; số chung là tổng hai số đó, chia cho mọi thú ảnh chụp (kể cả thú ở giữa hai dải);
     - số con bị trúng và sát thương mỗi bên, theo `cast.book[].side`; số thú ảnh chụp ở dải trời nhận ≥ 1 đòn dương (cho số quạ bị trúng; không dùng `crowsHit` cũ theo nhãn cổng);
     - tầm xa mỗi bên: đòn hiệu dụng xa nhất lên thú ở dải đất (≤ 1,5 m) tới H, như §8.1; và số thú đất ảnh chụp ở xa H hơn 12 m, số trong đó bị trúng;
     - phần theo loại đòn (đĩa F0, đĩa F1 đất, đĩa F1 trời, thân, trời, hoa sen đầy, hoa sen nửa): sát thương, số đòn, số con hạ. Mỗi sự kiện `hit` của lần tung xếp vào một phần theo tick so với F0, dải độ cao của thú và loại đòn vừa thêm vào `book` của nó (`kinds`): t = 0 là đĩa F0; t = 1–2, chạm là đĩa F1 đất, hành lang ở dải trời là đĩa F1 trời; hành lang ở dải đất là thân; hành lang ở dải trời từ t = 30 là trời; hoa sen đầy hay nửa theo `lotusRegion(cast, x, z)` ở vị trí lúc trúng;
     - `firstHit` (tick từ F0 tới đòn dương đầu tiên; −1 nếu không có) và, khi −1, lý do theo luật: xét các thú trong `book` của lần tung không nhận đòn dương nào; có con thuộc cụm bầy là `clusterCap`; có Vương là `bossCap`; ngược lại, nếu phần ngân sách tương ứng bằng 0 là `budget`; còn lại là `other`;
   - bộ ghi chỉ đọc: không gọi `sideFor`, `pickDiscs` hay hàm nào ghi vào bản ghi lần tung; vị trí ảnh chụp đọc từ `world.beasts.list[slot]` có kiểm `serial` (không dùng `beastByRef`, vì nó trả `null` cho con chết ngay ở F0, làm mất con đó khỏi số phủ và số đất/trời);
   - tên các phần mới bằng tiếng Anh: `f0Disc`, `f1Ground`, `f1Sky`, `body`, `sky`, `lotusFull`, `lotusHalf`;
   - sau bước này `key2-measure.ts` không còn nhập tên nào đã bỏ.
2. `key2-numbers.ts`: bỏ biến thể "narrow" (nó ghi vào các trường đã bỏ `touch.halfWidthMm`, `hold.halfWidthMm`). `+pool<N>` giữ nguyên (đổi `pool.sideW100` thành N trong bộ nhớ). Sửa luôn danh sách biến thể mặc định trong `key2-matrix.sh` và các dòng hướng dẫn trong `bot.ts`, `key2-dense.ts` còn nhắc `+narrow`.
3. `key2-aggregate.ts`, cho nhóm 35–45 và in như §8.2–8.6:
   - nhóm "35–45 thú" theo **thú đất trong ảnh chụp** (như §8.2; nhóm này quyết định đạt/trượt), in thêm nhóm theo mọi thú trong ảnh chụp để tham khảo;
   - số con bị trúng (trung vị, p10–p90, phần lần tung trong 12–20), `coverageStatic` (chung, đất, trời);
   - cân hai bên: chỉ tính lần tung mà mỗi bên có ≥ 5 thú trong ảnh chụp F0;
   - quạ bị trúng = số quạ ảnh chụp (dải trời) nhận ≥ 1 đòn dương chia số quạ ảnh chụp, tách theo phần (`f1Sky` hay `sky`), in riêng cho các lần tung có ≥ 2 quạ ở cùng một bên (đĩa F1 có thể tiêu hết ngân sách trời của bên đó cho con quạ đầu);
   - tầm xa: trung vị đòn xa nhất mỗi bên, phần thú đất > 12 m bị trúng (như §8.2);
   - phần theo loại đòn: % sát thương, đòn và hạ mỗi lần tung (như §8.3); thêm vào danh sách `PARTS` cố định của `key2-aggregate.ts` mọi phần mới (đĩa F0, đĩa F1 đất, đĩa F1 trời, thân, trời, hoa sen đầy, hoa sen nửa), để không phần nào bị bỏ sót khi in;
   - đòn đầu trong trận thật: số lần tung, số lần `firstHit > 2`, và danh sách riêng các lần `firstHit = −1` kèm lý do;
   - khối "canon" in thêm dòng ô 2/cả trận ≤ 45 % ở bot Chuẩn (đích anh duyệt) cạnh dòng ≤ 20 % cũ;
   - cột so: đọc thêm `tmp/skill-reach/key2-fix/numbers.json` (các biến thể `line`, `twin-pearl` là hai hành lang 2,5 W, `twin-pearl+pool200` là hai hành lang 2,0 W) và in cạnh số mới; không cần chạy lại các biến thể đó.
4. `key2-layouts.ts` mới (theo §9.8 bot bước 3):
   - dựng từng bố cục của §9.8 theo đúng thứ tự tạo; đấu trường trên sân tổng hợp `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }`; thế giới có cờ dựng như `twinWorld` trong `tests/sim/twin-pearl.test.ts`;
   - tung một lần với origin (0; 3), chỉ bước kỹ năng; sân trống gọi thẳng `buildCastGeometry`;
   - in: hai bên, P, độ dài đường nút, cung cuối, tốc đầu rồng (cung cuối chia (`heads.toTick` − `heads.fromTick`) / 60 s), `coverageStatic` (dạng số con / tổng), số con bị trúng, đòn đầu, chia hai bên.
5. Một script so cờ tắt nhỏ trong `tmp/skill-reach/` (kiểm 1 dưới đây).
6. **Cast không giải** (§9.2: không có thú nào ở dải đất hay dải trời): không phải một lần tung. Trong trận, bot giữ hành vi của game (Cast được giữ, không tốn hồi chiêu), `key2-measure.ts` không mở bản ghi lần tung nào, và mỗi trận ghi hai số: `key2Held` (số sự kiện `cast` của ô 2 có `state` "held") và `key2Fizzled` (số sự kiện `cast` của ô 2 có `state` "fizzled"). Trong quét đỉnh (`key2-dense.ts`), khi `resolveCast` trả `false` thì bỏ mẫu đó và lưu số "không giải" vào JSON đầu ra (trường `unresolved`). `key2-aggregate.ts` in, theo từng biến thể, tổng `key2Held`, tổng `key2Fizzled` của trận thật và tổng `unresolved` của quét đỉnh trong `aggregate.txt`; các số này không vào mẫu số của các chỉ số theo lần tung.

**Lệnh** (từ thư mục làm việc):
```text
# cờ tắt: 9 hồ sơ × seed 1–4
mkdir -p tmp/skill-reach/key2-fieldwide/golden-now
for p in w30a97 w45a97 w60a97 w80a97 w45a90 standard novice fast no-type; do
  BOT_HASHES=1 TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/bot.ts tmp/skill-reach/key2-fieldwide/golden-now $p 1 4 > tmp/skill-reach/key2-fieldwide/golden-now/$p.log 2>&1
done
# bố cục
TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/key2-layouts.ts > tmp/skill-reach/key2-fieldwide/layouts.txt
# ma trận và quét đỉnh: 2,0 W (mặc định mới) và các mức quét
KEY2_OUT=tmp/skill-reach/key2-fieldwide bash tmp/skill-reach/key2-matrix.sh twin-pearl twin-pearl+pool125 twin-pearl+pool175 twin-pearl+pool250 twin-pearl+pool375
KEY2_ROOT=tmp/skill-reach/key2-fieldwide KEY2_VARIANTS="twin-pearl twin-pearl+pool125 twin-pearl+pool175 twin-pearl+pool250 twin-pearl+pool375" TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/key2-aggregate.ts > tmp/skill-reach/key2-fieldwide/aggregate.txt
```
Cột so "hai hành lang" (2,0 W là `twin-pearl+pool200`, 2,5 W là `twin-pearl`) và "hôm nay" lấy từ `tmp/skill-reach/key2-fix/numbers.json` (bản chép ở bước chuẩn bị) và các bảng §8; không chạy lại biến thể "line" (cờ tắt không đổi).

**Kiểm và số phải đạt:**
1. **Cờ tắt:** với mỗi file JSON trong `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`, mọi trường có trong đó, ở mọi tầng (cả trong `waves[]`), bằng hệt trường cùng đường dẫn ở file cùng tên trong `golden-now`; bỏ qua khóa chỉ có ở `golden-now` (như `key2*`, `pace`, `lanePeak*`) và file `.log`, như §8.1. In số file khớp (đích 36/36).
2. **Bố cục:** `layouts.txt` khớp bảng §9.7 trong ± 1 m (độ dài các đoạn nút) và ± 1 con (trong tầm).
3. **Quét đỉnh, biến thể `twin-pearl` (2,0 W mỗi bên), nhóm 35–45 thú đất:**
   - số con bị trúng: trung vị trong 12–20 và ≥ 70 % lần tung trong 12–20 (in thêm p10–p90);
   - `coverageStatic` trung vị ≥ 75 %;
   - đòn đầu F0 hoặc F1 ở mọi lần tung có đòn dương; lần `firstHit = −1` liệt kê riêng kèm lý do, như kiểm 4;
   - quạ ≥ 90 % (in riêng nhóm ≥ 2 quạ một bên);
   - cân hai bên 40/60–60/40 ở ≥ 85 % lần tung đủ điều kiện.
4. **Trận thật, biến thể `twin-pearl`, mọi lần tung:** số lần `firstHit > 2` < 0,1 % số lần có đòn dương; các lần `firstHit = −1` đếm và liệt kê riêng kèm lý do, không gộp vào tỉ lệ này.
5. **Phần của ô 2 (anh duyệt, §9.11):** ô 2/cả trận ở bot Chuẩn (hồ sơ `standard`, 20 seed) ≤ 45 % với `twin-pearl` (2,0 W). In ô 2/cả trận của mọi bot.
6. **Báo cáo** (không có ngưỡng): ma trận 17 hồ sơ × 20 seed và quét ngân sách 1,25 / 1,75 / 2,0 / 2,5 / 3,75 W, bảng như §8.2–8.6 (tầm, phần theo loại đòn, BALANCE.md, cổng bot, quét) với cột "hai hành lang" để so.
7. Nếu một ngưỡng ở 1–5 trượt: ghi số và các lần tung trượt vào báo cáo; không đổi số trong `data/twin-pearl.ts` hay luật §9 để cho khớp.
