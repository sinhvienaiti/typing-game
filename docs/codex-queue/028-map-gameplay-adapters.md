# Phiếu 028 · Map Factory · Bộ đọc lớp chơi ở commit ghim: Lời Gọi `w1-silverfall`, Rồng `L2-cau` (chỉ mã, không trình duyệt)

**Bối cảnh:** kế hoạch [`docs/tools/MAP_FACTORY.md`](../tools/MAP_FACTORY.md), duyệt ngày 27/10/2026.
- Lớp chơi là sự thật và nằm trong nội dung game: đường quái, ô, nước, cầu, cây luật, nhà đặt sẵn (§3.1 nguyên tắc 1). Bộ sinh chỉ đọc, không ghi.
- Ở giai đoạn 1–2, bộ đọc ở repo cha lấy nội dung game ở một **commit ghim** bằng `git archive`. Nó không bao giờ đọc cây làm việc của game, vì các làn đang sửa ở đó hằng ngày (§2, §8.2).
- Kết quả là một **bản trích** JSON, mọi số là số nguyên cm (§8.3), kèm băm sha256 của nó. Phiếu 029 và các phiếu 031–032 dùng hai bản trích này làm fixture.

**Commit ghim** (Claude kiểm ngày 27/10, kiểm lại 28/10 lúc 02:30, cùng kết quả):
- **Lời Gọi** (`games/typing-defense`): `10ce627ff4e1c91f29e808cb658c086f51bd97d6`. Commit này chỉ đổi đợt quái và boss trong `src/content/slice-1a.ts` (cùng hai file golden), không đổi bản đồ. Vì vậy bản trích ở commit cha `10ce627^` (`84d0ac116b396df2b341ed4330461653a05fd8b2`) phải ra **cùng băm**.
- **Rồng** (`games/dragon-hold`): `83da970eacbf85ea64da89f62a4d1b6622bc5c7b`, đỉnh `origin/main` ngày 27/10 (đã đẩy, nằm trong `main`). M0b không đổi nội dung: `src/content` và `src/sim` ở `3f3390d6bddf404a2dee508c80973181bd31795f` (đỉnh nhánh `m0b-models`, gốc của spike) giống hệt. Vì vậy bản trích ở `3f3390d` phải ra **cùng băm**.
- **Đã đẩy hay chưa** (kiểm bằng `git branch -a --contains` và `git rev-list --count`, không fetch):
  - `83da970` là `origin/main` của Rồng;
  - `10ce627` nằm trên `main` cục bộ của Lời Gọi, chưa lên `origin/main` (lần fetch cuối lúc 12:50: `e3c2d7f`, `10ce627` đứng sau nó 4 commit);
  - `3f3390d` chỉ nằm trên hai nhánh cục bộ `m0b-models` và `map-spike`.
- Vì vậy test 3 (mục 7) là kiểm của giai đoạn 1–2. Commit so sánh (`10ce627^`, `3f3390d`) mất khỏi repo (rebase, gộp nén, gc) thì subtest của nó bỏ qua có lý do, không hỏng. Commit ghim mất thì test hỏng: điều phối viên ghim lại và làm lại fixture.
- `main` của hai game đã đi tiếp (Lời Gọi thêm 2 commit tài liệu, Rồng thêm 4 commit), nhưng `src/content` và `src/sim` không đổi so với commit ghim. Không ghim lại.

**Thư mục làm việc:** worktree của repo cha `/Users/toandx/htdocs/typing-game-wt/map-codex` (nhánh `map-factory`), cwd `.`. Mọi đường dẫn tương đối tính từ đây.
- Phiếu 027 đã chạy và đã commit trên nhánh `map-factory` (`db65b753`). `shared/game-kit/map/**` và `docs/codex-queue/027-report.md` là file đã commit, không thuộc phiếu này: không sửa, không xóa.
- Worktree có thể có file chưa commit từ trước, ví dụ chính các file phiếu. Chúng cũng không thuộc phiếu này.
- Trước khi ghi gì, chạy `git status --short --untracked-files=all` và giữ kết quả cho Kiểm 8.

**Repo của game:** các thư mục `games/*` trong worktree **rỗng** (submodule chưa khởi tạo). Gọi git trong đó là gọi trên repo cha, nên tuyệt đối không dùng chúng. Repo thật của hai game nằm ở bản checkout chính: `/Users/toandx/htdocs/typing-game/games/typing-defense` và `/Users/toandx/htdocs/typing-game/games/dragon-hold`. Chỉ đọc chúng bằng lệnh git (mục 2).

**Chỉ được ghi:**
- `tools/map-factory/lib/ts-hook.mjs`;
- `tools/map-factory/adapters/extract.mjs`, `typing-defense.mjs`, `dragon-hold.mjs`;
- `tools/map-factory/test/adapters.test.mjs`;
- `tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json`, `dragon-hold.L2-cau.json`;
- `tools/map-factory/.gitignore`;
- `tools/map-factory/.cache/**`: bản trích từ `git archive`, ngoài Git;
- `docs/codex-queue/028-report.md`: tiếng Việt có dấu.

**Cấm:**
- ghi vào `games/**` (của worktree hay của bản checkout chính), hay bất cứ đâu trong `/Users/toandx/htdocs/typing-game`;
- import hay đọc file trong cây làm việc của game: chỉ đọc từ `.cache`;
- lệnh git có ghi. Với repo game chỉ được: `archive`, `rev-parse`, `--no-optional-locks status --porcelain=v1`, `log`, `show`, `ls-tree`, `cat-file`. Ở worktree chỉ được: `status`, `diff`, `log`, `rev-parse`, `check-ignore`;
- chạy build, test hay script của game;
- sửa `shared/game-kit/**` (thuộc phiếu 027, 029) và `tools/map-factory/registry/**` (phiếu 025);
- cài gói, mạng, cổng, dev server, trình duyệt;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Mã là Node ESM thuần (`.mjs`), chỉ thư viện chuẩn của Node 24. Chú thích trong mã viết bằng tiếng Anh. Mọi lệnh ngoài gọi bằng `execFileSync` với mảng tham số, không qua shell.

## Việc

### 1. `lib/ts-hook.mjs`

Node 24.22 tự bỏ kiểu của file `.ts` (đã thử 27/10 với đúng các file của phiếu này, không cần cờ). Nhưng mã game import không có đuôi (`from "./fixed"`). Hook này thêm đuôi:
- dùng `registerHooks` của `node:module` (hook đồng bộ), đăng ký lúc import file;
- trong `resolve`: gọi `nextResolve` như thường. Nếu lỗi, và specifier bắt đầu bằng `./` hay `../`, không có đuôi, và file gọi kết thúc bằng `.ts`, thì thử lại với `specifier + ".ts"`;
- không dịch TypeScript, không dùng gói ngoài; khoảng 15–30 dòng.

### 2. `adapters/extract.mjs`: phần dùng chung

| Tên | Làm gì |
|---|---|
| `REPO_ROOT` | `path.resolve(<thư mục file này>, "../../..")` |
| `CACHE_DIR` | `<REPO_ROOT>/tools/map-factory/.cache` |
| `FIXTURE_DIR` | `<REPO_ROOT>/tools/map-factory/test/fixtures/gameplay` |
| `gamesDir()` | Biến môi trường `MAP_FACTORY_GAMES_DIR` nếu có. Nếu không: `git -C <REPO_ROOT> rev-parse --path-format=absolute --git-common-dir`, lấy thư mục cha của kết quả, nối `games`. Trong worktree này ra `/Users/toandx/htdocs/typing-game/games` |
| `gameRepo(id)` | `path.join(gamesDir(), id)`. Bắt buộc kiểm: `git -C <repo> rev-parse --show-toplevel` phải bằng `realpath(<repo>)`. Sai thì ném lỗi: thư mục đó không phải repo riêng của game (ví dụ thư mục rỗng trong worktree) |
| `resolveCommit(repo, rev)` | `git -C <repo> rev-parse --verify --end-of-options <rev>^{commit}` → 40 ký tự hex |
| `extractTree(game, repo, sha)` | Thư mục đích `<CACHE_DIR>/<game>/<sha>`. Kiểm đường dẫn nằm trong `CACHE_DIR`, xóa thư mục đó nếu có, tạo lại. Rồi `git -C <repo> archive --format=tar <sha> -- package.json src/content src/sim` (lấy stdout dạng Buffer, `maxBuffer: 64 * 1024 * 1024`; hôm nay khoảng 0,3–0,4 MB, sát trần mặc định 1 MB của `execFileSync`) và `tar -x -C <thư mục đích>` với Buffer đó làm stdin. Mỗi lần chạy trích lại từ đầu, nên không bao giờ đọc phải bản cũ. `package.json` của game có `"type": "module"`, nên Node coi các file `.ts` là ESM |
| `canonicalJson(v)` | Mục 5 |
| `gameplayHash(extract)` | sha256, dạng hex chữ thường, của byte UTF-8 của `canonicalJson(bản trích bỏ hai khóa commit và hash)` |
| `fixtureText(extract)` | Mục 5 |
| `exactCm(m, what)` | `c = Math.round(m * 100)`. Nếu `Math.abs(m * 100 - c) > 1e-6` thì ném lỗi có `what`. Trả `c + 0` (đổi `-0` thành `0`) |
| `gitStatus(repo)` | stdout của `git --no-optional-locks -C <repo> status --porcelain=v1` |

**Lệnh chạy** (khối `main`, chỉ chạy khi file được gọi trực tiếp; nạp hai bộ đọc bằng `import()` động để không có vòng import):

```text
node tools/map-factory/adapters/extract.mjs <typing-defense|dragon-hold|all> [rev] [--write]
```
- Không có `--write`: in `fixtureText` ra stdout (với `all`: Lời Gọi trước, rồi Rồng). `rev` mặc định là commit ghim.
- Có `--write`: ghi `<FIXTURE_DIR>/<game>.<map>.json`, in đường dẫn và băm. Có `--write` mà `rev` khác commit ghim thì thoát 2: fixture chỉ được làm từ commit ghim.
- Với `all`: không nhận `rev`, vì một rev không thể đúng cho hai repo. Mỗi game dùng `PIN` của mình. Có `rev` thì thoát 2.
- Tên game lạ, hay thừa tham số, cũng thoát 2.

### 3. `adapters/typing-defense.mjs`

Xuất `ADAPTER = "typing-defense@1"`, `GAME = "typing-defense"`, `PIN = "10ce627ff4e1c91f29e808cb658c086f51bd97d6"`, và ba hàm:
- `load(dir)`: import (qua `pathToFileURL`) `src/content/slice-1a.ts` lấy `SLICE_1A`; `src/content/rules.ts` lấy `BUILD`, `TREE`, `RALLY`; `src/sim/lanes.ts` lấy `groundLanes`;
- `toGameplay(mods, sha)`: hàm thuần, trả bản trích theo bảng ở mục 5, đã có trường `hash`;
- `extract(rev = PIN)`: `gameRepo` → `resolveCommit` → `extractTree` → `load` → `toGameplay`. Trả `{ extract, mods }`.

Tuyến đường lấy từ chính hàm của game: `groundLanes(SLICE_1A.map.routes)`. Hàm này dùng đường Hermite có tiếp tuyến lấy trung bình ở nút chung. Một Catmull-Rom tự viết sẽ lệch chỗ quái đi thật (§4.1), nên không được tự tính lại. Mỗi `Lane` đã lấy mẫu đều sẵn (`xs`, `zs`, bước bằng `length / (count − 1)`, khoảng 25 cm). Bản trích giữ đúng các mẫu đó, làm tròn tới cm.

### 4. `adapters/dragon-hold.mjs`

Xuất `ADAPTER = "dragon-hold@1"`, `GAME = "dragon-hold"`, `PIN = "83da970eacbf85ea64da89f62a4d1b6622bc5c7b"`, và:
- `load(dir)`: import `src/content/data/maps.ts` lấy `MAP_L2_CAU`; `src/content/data/stages.ts` lấy `STAGE_M0`; `src/sim/lanes.ts` lấy `compileLanes`; `src/sim/fixed.ts` lấy `mToU` và `U_PER_M`;
- `toGameplay(mods, sha)`: trả `{ extract, stats }`, với `stats = { laneValues, checked, notDivisible }` (mục 5);
- `extract(rev = PIN)`: như Lời Gọi; trả `{ extract, stats, mods }`.

Đơn vị của Rồng là u, 1 m = 60 000 u (`fixed.ts`), nên 1 cm = 600 u. Kiểm `U_PER_M === 60000`.
- Làn lấy từ chính hàm của game: `compileLanes(MAP_L2_CAU, ids)`, với `ids` là id các làn đất rồi id các làn trời: `["cau", "suoi", "troi"]`. Kiểm `ids` bằng đúng `STAGE_M0.lanes`.
- Mọi độ dài khác đổi bằng `mToU` của game.
- Hàm `uToCm(u, what)`: tăng `checked`; nếu `u % 600 !== 0` thì tăng `notDivisible` rồi ném lỗi có `what`; trả `u / 600 + 0`.
- `laneValues` là số lần gọi `uToCm` cho phần làn. Với mỗi làn từ `compileLanes`: mọi `xs` và `zs`, `halfWidth`, `altitude`, mỗi cầu (`from`, `to`, `halfWidth`), mỗi chỗ lội (`from`, `to`). Ở commit ghim: 13 điểm (5 + 5 + 3) × 2 + 3 + 3 + 3 + 2 = **37**.

### 5. Bản trích: định dạng chính xác

**`canonicalJson(v)`:**
- số: phải là `Number.isSafeInteger`, sai thì ném lỗi; viết bằng `String(v)`, và `-0` viết là `0`;
- chuỗi, `true`, `false`, `null`: `JSON.stringify`;
- mảng: `"[" + các phần tử nối bằng "," + "]"`, giữ thứ tự;
- object: khóa sắp bằng `Object.keys(o).sort()` (thứ tự đơn vị mã UTF-16), mỗi cặp `JSON.stringify(khóa) + ":" + giá trị`, nối bằng `","`, trong `{}`. Giá trị `undefined` thì ném lỗi;
- không có khoảng trắng.

**`fixtureText(extract)`:** `"{\n"` + các khóa cấp đầu (sắp như trên), mỗi khóa một dòng `JSON.stringify(khóa) + ":" + canonicalJson(giá trị)`, nối bằng `",\n"` + `"\n}\n"`. Đây là JSON hợp lệ; `JSON.parse` của nó bằng đúng bản trích.

**Băm:** `hash = gameplayHash(extract)`. Băm bỏ `commit` và `hash`, nên hai commit có cùng lớp chơi ra cùng băm.

**Lời Gọi** (`typing-defense@1`). Nguồn: `map = SLICE_1A.map`. "cm" là `exactCm`, trừ hai chỗ ghi "làm tròn".

| Khóa | Giá trị | Nguồn |
|---|---|---|
| `format` | `"map-gameplay/0"` | |
| `adapter` | `"typing-defense@1"` | |
| `game` | `"typing-defense"` | |
| `map` | `"w1-silverfall"` | `SLICE_1A.id` |
| `contentMapId` | `"td-sandbox"` | `map.id` |
| `commit` | 40 ký tự hex | `resolveCommit` |
| `hash` | sha256 hex | `gameplayHash` |
| `unit` | `"cm"` | |
| `field` | `{ halfCm, buildHalfCm }` | `map.halfM`, `map.buildHalfM` |
| `rules` | `{ roadHalfCm, roadClearCm, keepClearCm, gapCm, snapCm, nodeSnapCm, treeRadiusCm, footprintCm: { S, M, L, XL }, rallyRadiusCm, rallyRoadMaxCm }` | `map.roadHalfM`; `BUILD.roadClearM`, `keepClearM`, `gapM`, `snapM`, `nodeSnapM`, `footprintR`; `TREE.radiusM`; `RALLY.radiusM`, `roadMaxM` |
| `gate` | `[x, z]` | `map.gate` |
| `keep` | `{ at: [x, z], footprintCm }` | `map.keep`; `footprintCm[cỡ của nhà "keep"]` |
| `routeKnots` | mảng tuyến, mỗi tuyến mảng `[x, z]` | `map.routes` |
| `routes` | mảng `{ lengthCm, points }` | `groundLanes(map.routes)`: `lengthCm = Math.round(lane.length * 100) + 0`; `points[i] = [Math.round(xs[i] * 100) + 0, Math.round(zs[i] * 100) + 0]` (làm tròn) |
| `fly` | `{ points, heightCm }` | `map.flyRoute`, `map.flyHeightM` |
| `water` | mảng `{ x0, x1, z0, z1 }` | `map.water` |
| `bridges` | mảng `{ x0, x1, z0, z1 }` | `map.bridges` |
| `nodes` | mảng `{ at: [x, z], richness }` | `map.nodes` (`richness` giữ nguyên) |
| `trees` | mảng `[x, z]`, chỉ số là id cây | `map.trees` |
| `preset` | mảng `{ kind, at: [x, z], footprint, footprintCm }` | `map.preset` (`[id, x, z]`); `footprint` là cỡ của nhà có id đó trong `SLICE_1A.buildings`; `footprintCm[cỡ]` |

Bản trích đúng ở commit ghim, trừ hai mảng `points` dài của `routes`:

```json
{
"adapter":"typing-defense@1",
"bridges":[{"x0":-2550,"x1":-2250,"z0":-1550,"z1":-1250},{"x0":-2550,"x1":-2250,"z0":2450,"z1":2750}],
"commit":"10ce627ff4e1c91f29e808cb658c086f51bd97d6",
"contentMapId":"td-sandbox",
"field":{"buildHalfCm":4600,"halfCm":4800},
"fly":{"heightCm":300,"points":[[-1000,-4600],[2000,-2000],[0,4000]]},
"format":"map-gameplay/0",
"game":"typing-defense",
"gate":[-1000,-4600],
"hash":"7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23",
"keep":{"at":[0,4000],"footprintCm":350},
"map":"w1-silverfall",
"nodes":[{"at":[2600,-3000],"richness":3},{"at":[-1200,3200],"richness":1},{"at":[-3400,800],"richness":2}],
"preset":[{"at":[-800,1200],"footprint":"S","footprintCm":200,"kind":"archer"},{"at":[700,1200],"footprint":"M","footprintCm":230,"kind":"cannon"},{"at":[300,1800],"footprint":"M","footprintCm":230,"kind":"barracks"},{"at":[2600,-3000],"footprint":"L","footprintCm":270,"kind":"gold-mine"},{"at":[-1700,4000],"footprint":"L","footprintCm":270,"kind":"farm"}],
"routeKnots":[[[-1000,-4600],[-400,-4000],[600,-3400],[-1200,-2000],[-1000,0],[0,1200],[-600,2000],[600,3000],[0,4000]],[[-1000,-4600],[-400,-4000],[600,-3400],[1600,-2000],[1200,200],[0,1200],[-600,2000],[600,3000],[0,4000]]],
"routes":[{"lengthCm":11880,"points":[…476 điểm…]},{"lengthCm":11472,"points":[…459 điểm…]}],
"rules":{"footprintCm":{"L":270,"M":230,"S":200,"XL":350},"gapCm":100,"keepClearCm":1100,"nodeSnapCm":150,"rallyRadiusCm":1200,"rallyRoadMaxCm":300,"roadClearCm":190,"roadHalfCm":190,"snapCm":25,"treeRadiusCm":150},
"trees":[[-2100,-4400],[-1750,-4450],[-1450,-4250],[-2000,-4050],[-1650,-3950],[-1900,-3700],[-150,-4400],[250,-4450],[600,-4400],[950,-4300],[500,-4100],[1250,-4100],[-2900,-3500],[-2850,-3050],[-2950,-2600],[-2800,-2150],[-3150,-3250],[-1950,-3100],[-2000,-2700],[-1850,-2300],[-1650,-2900],[-1950,-1900],[3300,-4300],[3700,-4400],[4100,-4200],[3500,-3900],[3900,-3750],[4300,-3800],[4250,-3350],[1500,3600],[1800,3950],[1600,4350],[2000,3500],[1950,4300],[2250,3950],[1350,3150]],
"unit":"cm",
"water":[{"x0":-2550,"x1":-2250,"z0":-4800,"z1":4800}]
}
```

Hai tuyến: tuyến 0 có 476 điểm, tuyến 1 có 459 điểm. Ba điểm đầu của cả hai là `[-1000,-4600],[-983,-4582],[-966,-4564]`; ba điểm cuối của cả hai là `[29,3959],[14,3979],[0,4000]`.

**Rồng** (`dragon-hold@1`). Nguồn: `map = MAP_L2_CAU`; `lanes = compileLanes(map, ids)`. "cm" là `uToCm(mToU(m))`, hoặc `uToCm(u)` khi số đã ở u.

| Khóa | Giá trị | Nguồn |
|---|---|---|
| `format`, `adapter`, `game`, `commit`, `hash`, `unit` | như Lời Gọi, với `"dragon-hold@1"`, `"dragon-hold"` | |
| `map` | `"L2-cau"` | `map.id` |
| `dais` | `{ at, radiusCm, heroHoverCm, guideAt }` | `map.dais.center`, `radiusM`, `heroHoverM`, `guideAt` |
| `lanes` | các làn có `sky === false`, theo thứ tự `compileLanes`: `{ id, halfWidthCm, points, bridges: [{ fromCm, toCm, halfWidthCm }], fords: [{ fromCm, toCm }] }` | `xs`/`zs`, `halfWidth`, `bridges`, `fords` của `LaneRuntime` (đã ở u) |
| `sky` | các làn có `sky === true`: `{ id, altitudeCm, points }` | `xs`/`zs`, `altitude` |
| `slots` | theo thứ tự `map.slots`. Ô làn: `{ id, kind, lane, atCm, at }`. Ô nhà: `{ id, kind, ring, at }` | `id`, `kind`, `lane`, `atM`, `ring`, `pos` |
| `river` | `{ points, widthsCm, depthCm, bankCm, shallows: [{ at, radiusCm }] }` | `map.river` |
| `terrain` | `{ seed, sizeCm, playRadiusCm, reliefCm, kit }` | `map.terrain` (`seed`, `kit` giữ nguyên) |

Bản trích đúng ở commit ghim, nguyên văn từng byte (đây cũng là nội dung file fixture):

```json
{
"adapter":"dragon-hold@1",
"commit":"83da970eacbf85ea64da89f62a4d1b6622bc5c7b",
"dais":{"at":[0,0],"guideAt":[-260,200],"heroHoverCm":250,"radiusCm":400},
"format":"map-gameplay/0",
"game":"dragon-hold",
"hash":"c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a",
"lanes":[{"bridges":[{"fromCm":1050,"halfWidthCm":170,"toCm":1840}],"fords":[],"halfWidthCm":150,"id":"cau","points":[[850,-2900],[500,-2250],[220,-1540],[120,-1000],[40,-600]]},{"bridges":[],"fords":[{"fromCm":690,"toCm":1400}],"halfWidthCm":130,"id":"suoi","points":[[-3000,700],[-2400,420],[-1800,140],[-1200,100],[-600,40]]}],
"map":"L2-cau",
"river":{"bankCm":40,"depthCm":120,"points":[[7000,-3300],[3800,-2500],[2400,-2100],[1200,-1750],[100,-1550],[-800,-1350],[-1450,-850],[-1850,-100],[-2300,700],[-3000,1500],[-3800,2200],[-7000,4000]],"shallows":[{"at":[-2050,260],"radiusCm":350}],"widthsCm":[800,750,700,650,600,550,500,450,400,400,400,400]},
"sky":[{"altitudeCm":300,"id":"troi","points":[[3050,-850],[2000,-700],[730,-180]]}],
"slots":[{"at":[660,-2548],"atCm":400,"id":"cau-t1","kind":"trap","lane":"cau"},{"at":[404,-2006],"atCm":1000,"id":"cau-t2","kind":"trap","lane":"cau"},{"at":[211,-1492],"atCm":1550,"id":"cau-t3","kind":"trap","lane":"cau"},{"at":[95,-873],"atCm":2180,"id":"cau-t4","kind":"trap","lane":"cau"},{"at":[441,-2100],"atCm":900,"id":"cau-b1","kind":"block","lane":"cau"},{"at":[147,-1148],"atCm":1900,"id":"cau-b2","kind":"block","lane":"cau"},{"at":[-2502,467],"atCm":550,"id":"suoi-t1","kind":"trap","lane":"suoi"},{"at":[-1575,125],"atCm":1550,"id":"suoi-t2","kind":"trap","lane":"suoi"},{"at":[-977,78],"atCm":2150,"id":"suoi-t3","kind":"trap","lane":"suoi"},{"at":[-1525,122],"atCm":1600,"id":"suoi-b1","kind":"block","lane":"suoi"},{"at":[-1026,83],"atCm":2100,"id":"suoi-b2","kind":"block","lane":"suoi"},{"at":[-550,-650],"id":"h-nw","kind":"house","ring":"inner"},{"at":[650,-500],"id":"h-ne","kind":"house","ring":"inner"},{"at":[550,600],"id":"h-se","kind":"house","ring":"inner"},{"at":[-500,650],"id":"h-sw","kind":"house","ring":"inner"},{"at":[950,-1100],"id":"h-e","kind":"house","ring":"outer"},{"at":[-1400,650],"id":"h-w","kind":"house","ring":"outer"}],
"terrain":{"kit":"pine-river","playRadiusCm":3200,"reliefCm":160,"seed":20261023,"sizeCm":14400},
"unit":"cm"
}
```

Đếm: `laneValues` = 37; `checked` = 132 (37 của làn; `dais` 6; `slots` 17 × 2 + 11 `atCm` = 45; `river` 12 × 2 + 12 + 1 + 1 + 3 = 41; `terrain` 3); `notDivisible` = 0.

Claude đã cài thử đúng định dạng trên ở một thư mục nháp, chạy hai lần, ra cùng từng byte và cùng các băm trong phiếu. Bản trích của bạn phải ra đúng như vậy. Nếu lệch: in bản trích, so từng khóa với hai khối trên, sửa chỗ làm sai phiếu. Nếu mọi khóa đã đúng như phiếu mà băm vẫn lệch, ghi rõ vào báo cáo. Không sửa số cho khớp.

### 6. `.gitignore` và fixture

- `tools/map-factory/.gitignore`, đúng ba dòng: `# Map Factory: extracted game trees and build output, never in Git`, `/.cache/`, `/out/`. Mẫu có `/` đầu nên `registry/out/` (sổ model của phiếu 025, đã vào Git) không bị bỏ qua.
- Hai fixture tạo bằng `node tools/map-factory/adapters/extract.mjs all --write`, không viết tay.

### 7. `test/adapters.test.mjs` (`node:test`)

1. **Lời Gọi ở commit ghim:**
   - `trees` có 36 cây, đúng từng tọa độ và thứ tự như khối JSON ở mục 5;
   - `preset` có 5 nhà, đúng `kind`, `at`, `footprint`, `footprintCm`;
   - `rules.treeRadiusCm` 150 (`TREE.radiusM` 1,5), `roadClearCm` 190, `keepClearCm` 1100, `gapCm` 100 (`BUILD.roadClearM` 1,9, `keepClearM` 11, `gapM` 1), `footprintCm` S 200, M 230, L 270, XL 350;
   - `water` 1 rect, `bridges` 2 rect, `nodes` 3, đúng như khối JSON;
   - `routes`: 2 tuyến, 476 và 459 điểm, `lengthCm` 11880 và 11472, ba điểm đầu và ba điểm cuối như mục 5;
   - với mọi mẫu `i` của mọi tuyến, `|points[i][0] − xs[i] × 100| ≤ 1` và `|points[i][1] − zs[i] × 100| ≤ 1`, so với `Lane` mà test tự tạo bằng `mods.groundLanes(mods.SLICE_1A.map.routes)`. Số điểm bằng `xs.length`. In độ lệch lớn nhất (cm), phải ≤ 0,5.
2. **Rồng ở commit ghim:** bản trích bằng đúng khối JSON ở mục 5; `stats.laneValues` 37, `stats.checked` 132, `stats.notDivisible` 0 (in ra); 17 ô: 7 `trap`, 4 `block` (11 ô làn), 6 `house`; `STAGE_M0.lanes` là `["cau","suoi","troi"]`.
3. **Băm vàng:** bốn subtest, mỗi subtest gọi `extract(rev)` một lần.
   - Lời Gọi ở `PIN` và ở `10ce627^`: `hash` là `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23`. `commit` của bản trích ở `10ce627^` là `84d0ac116b396df2b341ed4330461653a05fd8b2`.
   - Rồng ở `PIN` và ở `3f3390d`: `hash` là `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a`.
   - Ở hai subtest của commit so sánh (`10ce627^`, `3f3390d`), kiểm trước bằng `git -C <repo> rev-parse --verify --quiet --end-of-options <rev>^{commit}`. Lệnh thoát khác 0 (commit không có trong repo) thì gọi `t.skip("<rev> is not in <repo>")` rồi dừng subtest.
   - Hai subtest `PIN` không có lối bỏ qua: thiếu commit ghim thì hỏng.
4. **Băm đổi khi sửa một cây trong RAM:** sao sâu `mods.SLICE_1A` (`structuredClone`); cộng 0,01 m vào x của cây số 7; gọi `toGameplay` với bản sao. `trees[7]` đổi từ `[250,-4450]` thành `[251,-4450]`; `hash` khác băm vàng; mọi khóa khác (trừ `trees`, `hash`) giống hệt bản gốc.
5. **Cùng byte:** chạy `node tools/map-factory/adapters/extract.mjs typing-defense` hai lần, mỗi lần một tiến trình con. Hai stdout giống hệt từng byte, và bằng file fixture. Làm như vậy với `dragon-hold`.
6. **Không ghi vào repo game:** với mỗi game, `s0 = gitStatus(repo)`, chạy tiến trình con trích game đó, `s1 = gitStatus(repo)`. Phải `s0 === s1`. Làn khác có thể đang sửa cây làm việc của game, nên lệch thì thử lại tối đa 2 lần nữa. Đạt khi có một lần bằng nhau. In các dòng khác nhau của lần lệch.
7. **Chặn thư mục không phải repo game:** tạo thư mục rỗng `<CACHE_DIR>/empty-games/dragon-hold` (giống thư mục submodule rỗng trong worktree: git ở đó sẽ chạy trên repo cha). Đặt `MAP_FACTORY_GAMES_DIR=<CACHE_DIR>/empty-games` thì `gameRepo("dragon-hold")` ném lỗi, và `extract()` của Rồng bị từ chối. Trả lại biến môi trường sau test. Test này phải đạt cả ở worktree lẫn ở bản checkout chính, nên không dùng `<REPO_ROOT>/games`.
8. **`canonicalJson`:** khóa sắp đúng; `-0` ra `0`; `1.5`, `NaN`, `undefined` ném lỗi.

## Kiểm (bắt buộc)

Chạy từ cwd `.` của worktree. Dán lệnh và dòng kết quả vào báo cáo.

1. `node --test tools/map-factory/test/*.test.mjs` đạt. In số test.
2. Chạy `node tools/map-factory/adapters/extract.mjs all --write` hai lần. Sau mỗi lần, `shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json` ra đúng:
   - `ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37  …/dragon-hold.L2-cau.json`
   - `71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428  …/typing-defense.w1-silverfall.json`
3. Băm bản trích: Lời Gọi `7faeaa7c…4b23` ở `10ce627` và ở `10ce627^`; Rồng `c852b4d7…659a` ở `83da970` và ở `3f3390d` (test 3). Hôm nay cả bốn commit đều có, nên không subtest nào được bỏ qua: dòng tổng của lệnh 1 phải ghi `skipped 0`.
4. Sự thật về lớp chơi (test 1, 2): 36 cây đúng thứ tự; 5 nhà đặt sẵn có bán kính nền; `TREE.radiusM`, `BUILD.roadClearM`, `keepClearM`, `gapM`; tuyến lệch ≤ 1 cm so với `Lane.xs/zs` (in số lớn nhất); Rồng 37 giá trị làn và 132 giá trị tất cả, 0 giá trị không chia hết cho 600; 6 ô nhà, 11 ô làn.
5. Sửa một cây trong RAM thì băm đổi (test 4).
6. `git --no-optional-locks -C /Users/toandx/htdocs/typing-game/games/<id> status --porcelain=v1` trước và sau lệnh 2 giống hệt, với cả hai game. Test 6 làm việc này tự động. Ghi thêm kết quả lệnh tay vào báo cáo; nếu lệnh tay lệch vì một làn khác vừa sửa cây làm việc của game, ghi rõ các dòng lệch và chạy lại.
7. Ba lệnh riêng: `git check-ignore -q tools/map-factory/.cache/x` thoát 0; `git check-ignore -q tools/map-factory/out/x` thoát 0; `git check-ignore -q tools/map-factory/registry/out/assets.dragon-hold.json` thoát 1 (sổ của phiếu 025 vẫn trong Git).
8. Chạy lại `git status --short --untracked-files=all` và so với kết quả đã giữ lúc bắt đầu. Lúc cuối chỉ được có **thêm** các đường dẫn trong "Chỉ được ghi" (`.cache` không hiện, vì bị bỏ qua). Không có dòng ` M` hay ` D` mới, kể cả với file của phiếu 027. Các dòng đã có lúc bắt đầu (ví dụ file phiếu chưa commit) ghi lại vào báo cáo, nhưng không đụng.

## Báo cáo `docs/codex-queue/028-report.md`

- Các file đã viết, mỗi file một dòng.
- Kết quả tám lệnh kiểm, kèm số: số test và số bỏ qua, hai sha256 fixture, bốn băm bản trích, độ lệch tuyến lớn nhất, `laneValues`/`checked`/`notDivisible`, kết quả `git status` của hai game.
- Thời gian một lần `extract.mjs all`.
- Những chỗ phiếu chưa rõ và cách đã chọn; những chỗ lệch với phiếu, nếu có.

**Xong khi:** tám lệnh kiểm đều đạt, hai fixture đúng sha256, báo cáo đã viết.
