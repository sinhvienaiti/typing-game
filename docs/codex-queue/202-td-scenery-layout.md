# Phiếu 202 · Wordwoven · C9: bố cục cảnh vật map 1 thuần, theo seed (cây, bụi, đá, mép rừng) theo MAP_FACTORY §6.4

> **Chạy lại (30/10, 12:58, điều phối):** lượt 11:28 đã làm phần dữ liệu (module, test, golden, sáu tờ) nhưng bỏ `pnpm check`. Lượt này chạy ngay sau 199 trong cùng làn. Giữ phần đã làm, nối với atlas và manifest của 199 nếu phiếu cần, rồi chạy đủ mục kiểm. Các lệnh kiểm của phiếu (`pnpm check`, build, đo gói, toàn bộ test) là **bắt buộc**. Điều phối Claude cho phép thay chủ dự án; điều này thắng mọi luật chung kiểu "không chạy build hay toàn bộ test suite". Không hỏi lại, cứ chạy và ghi số.

**Nguồn:**
- Chủ dự án 29/10/2026 tối: "tăng thêm việc cho codex cho tôi".
- `docs/games/MAP1_PRODUCTION.md` C9 (P0, G2): "rải decor theo §6.4".
- `docs/tools/MAP_FACTORY.md` §6.4: "mọi decor đều `clearOnBuild`"; "Vật cố định (mốc, đá lớn, vách, rừng mép) chỉ ở vùng sim cấm xây"; "cây cảnh cách cây luật ≥ 4 m".
- TK §23.10 (`docs/td/TYPING_DEFENSE_DESIGN.md` của game): "rải Poisson có cụm, theo seed bản đồ"; "hai cây liền nhau khác biến thể"; "High 1.500 vật lớn (cây, đá, bụi, khối tán) + 4.000 cỏ và hoa chữ thập; Medium 1.000 + 1.600; Low 600 + 0"; mép rừng "xếp 2–4 hàng lệch, hàng sau cao và tối hơn 8 %".

**Không trùng:** 033 (Map Factory `along.ts`, nhánh đã dừng), 028 (bộ đọc lớp chơi của Map Factory), 116–118 (chỉ vẽ ảnh), 199 (atlas, manifest và tập ảnh).

**Phân việc:** phiếu này chỉ làm **dữ liệu**: vật nào, ở đâu, cỡ, lật, màu, cố định hay đổ khi xây. Làn Claude L3 giữ phần dựng: `src/view/3d/scenery.ts`, billboard, shader, đung đưa, cây đổ khi đặt nhà, độ cao y.

**Làn:** làn Codex duy nhất (chủ dự án 30/10: một làn). Chạy sau 199, cùng nhánh `td-scenery`.

**Báo cáo:** `docs/codex-queue/202-report.md` (tiếng Việt), thư mục `docs/codex-queue/202/` (chỉ JSON, Markdown, md5; không ảnh). Ảnh kiểm nằm ở `games/.wt-td-scenery/tmp/202/`.

**Chỉ chạy khi:**
- Worktree `games/.wt-td-scenery` (nhánh `td-scenery`, Claude cắt từ `td-1c` `2a1f61d` cho phiếu 199) đã có và đã `pnpm install --offline`. Chưa có thì dừng, ghi vào báo cáo.
- `git status --short -uall` sạch, **hoặc** chỉ có đúng các file của 199 (danh sách ở mục Kiểm 8 của phiếu 199) khi Claude chưa commit 199. Ghi rõ trường hợp nào. Có file lạ thì dừng.
- `scripts/td/scenery-set.json` của 199 có. Thiếu thì vẫn làm với tập mẫu trong test (mục Việc 1), ghi rõ; test đọc tập thật thì `skip` kèm lý do.

## Luật chung (phiếu mã)

- **Nơi làm:** worktree `games/.wt-td-scenery`. cwd của làn là repo cha (`.`), để ghi được báo cáo ở `docs/codex-queue/`; lệnh `pnpm` và script của game chạy trong worktree.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- Test trước, mã sau. Chú thích tiếng Anh. Luật chơi và ván vàng không đổi.
- Không có chữ người chơi thấy trong phiếu này.

## Đọc trước (chỉ đọc)

1. `docs/tools/MAP_FACTORY.md` §6.4 (repo cha): luật decor.
2. `docs/td/TYPING_DEFENSE_DESIGN.md` §23.10 (trong worktree): dạng, chống lặp, ngân sách, mép rừng.
3. `docs/codex-queue/199-td-prepare-scenery.md` mục Việc 1 và 6: trường của `scenery-set.json` (`id`, `type`, `variant`, `kind`, `heightM`, `accepted`) và manifest.
4. `src/content/slice-1a.ts`: `map` của map 1 (`halfM` 48, `buildHalfM` 46, `keep`, `gate`, `routes`, `water`, `bridges`, `nodes`, 36 `trees`, 5 `preset`).
5. `src/content/rules.ts`: `TREE.radiusM` 1,5; `BUILD` (`footprintR`, `gapM` 1,0, `roadClearM` 1,9, `keepClearM` 11).
6. `src/sim/placement.ts` (`canPlace`) và `src/sim/lanes.ts` (`groundLanes`).
7. `src/view/3d/road.ts` (`roadField`: `widths`, `dressing`; nửa bề rộng lượn ±14 %, +20 % ở khúc cua, +30 % ở ngã ba; lề mòn 0,3–0,8 m).
8. `src/view/3d/ground.ts`: `BORDER_M` 40, `heightAt` (đồi Cầu Vồng phía đông, vách Thác Bạc ở đầu suối), sân đá trong `groundMasks` (Lũy 7 m; mỏ 2,2 + 0,5 × `richness`; mép mềm 1,5 m).
9. `tests/td-3d-road.test.ts` và `tests/td/fixtures.ts`: cách test dựng lane, road field và world.

## Việc

1. **Test trước.** File `tests/td-scenery-layout.test.ts`.
   - Đầu vào dựng từ `SLICE_1A`: `groundLanes(map.routes)`; `roadField(map, lanes, halfM + BORDER_M)` lấy `widths` và `dressing`; `heightAt`; nhà đặt sẵn với bán kính từ `BUILD.footprintR`.
   - Test được import `road.ts`, `ground.ts`. Module thì không (mục 2).
   - Hai tập ảnh: (a) tập thật `scripts/td/scenery-set.json`; (b) tập mẫu cố định viết trong test: 13 loại × v3, v4, chiều cao cây theo 199 (bàng 18/14, thông 14/10, tre 16/16, khối tán 10/14), loại khác lấy số đề xuất của 117, 118.
   - Mã băm vàng chỉ chạy trên tập mẫu (b), để vàng chỉ đổi khi thuật toán đổi.
   - Các ca test ở mục 5.
2. **Module mới** `src/view/3d/scenery-layout.ts`. Thuần:
   - chỉ import `../../sim/lanes`, `../../content/rules` và kiểu từ `../../content/types`;
   - không import `three`, `./road`, `./ground`, `./stage`, `../../kit/**`;
   - không `Math.random`, `Date`, `performance`;
   - phép tính chỉ `+ − × ÷`, `Math.sqrt`, `floor`, `round`, `min`, `max`, `abs`, và PRNG số nguyên có seed (ví dụ mulberry32). Không `sin`, `cos`, `atan2`, `exp`, `pow`, để mã băm ổn định giữa các máy.
   - Không đọc file. Đầu vào là tham số.
3. **Hình dữ liệu** (hợp đồng với L3; được thêm trường, không đổi tên các trường dưới):

   ```ts
   export type SceneryTier = "low" | "medium" | "high";
   export type SceneryZone = "field" | "band" | "keep" | "water" | "ring";
   export type SceneryEntry = { id: string; type: string; variant: string; kind: string; heightM: number }; // a scenery-set.json entry
   export type SceneryInput = {
     map: MapDef;                                            // read only
     houses: readonly { x: number; z: number; r: number }[]; // preset footprints
     set: readonly SceneryEntry[];                           // the caller filters accepted / pending
     roadHalf?: readonly Float32Array[];                     // RoadField.widths per ground-lane point
     dressing?: readonly { x: number; z: number; r: number }[];
     heightAt?: (x: number, z: number) => number;
     seed?: number;                                          // default: FNV-1a of map.id
   };
   export type SceneryItem = {
     sprite: string;   // scenery-set id = manifest sprite id, e.g. "almond-tree-v3"
     type: string;     // "almond-tree"
     kind: string;     // tree | bamboo | canopy | bush | grass | flower | rock | log | stump
     variant: string;  // "v3"
     x: number; z: number; // m, the sim's ground plane; y is L3's
     r: number;        // footprint radius, m
     scale: number;    // jitter 0.85–1.15 × the forest row's growth; times heightM
     flip: boolean;    // mirror the quad
     tint: number;     // brightness jitter 0.96–1.04
     shade: number;    // forest row darkening: 0.92 ^ row; 1 off the edge
     row: number;      // −1 off the forest edge; 0 front … 3 back
     zone: SceneryZone;
     clearOnBuild: boolean; // true: a house over it fells it; false: fixed
     cross: boolean;   // true: a grass or flower cross; false: a large object
   };
   export type SceneryLayout = { seed: number; tier: SceneryTier; items: SceneryItem[]; counts: Record<string, number> };
   export const SCENERY_BUDGET: Record<SceneryTier, { large: number; cross: number }>; // 1500/4000, 1000/1600, 600/0
   export function sceneryLayout(input: SceneryInput, tier: SceneryTier): SceneryLayout;
   export function buildableAt(input: SceneryInput, x: number, z: number): boolean;
   ```

   - `items` sắp theo `sprite`, rồi `z`, rồi `x`, để L3 gom instance theo sprite.
   - `roadHalf` thiếu thì dùng `roadHalfM` × 1,5. Lề mòn tính thêm 0,8 m.
   - Bán kính chân `r`: bảng `FOOT` trong module, hệ số × `heightM` theo `kind`. Số khởi điểm, ghi rõ trong chú thích và báo cáo.
   - Mọi số chỉnh được (tỉ lệ loại mỗi vùng, mật độ, cỡ cụm, khoảng hàng) là hằng có tên ở đầu file.
   - Header của file mô tả hình dữ liệu, đơn vị, khung tọa độ, cách áp `scale`, `flip`, `tint`, `shade`, `row`, `clearOnBuild`.
4. **Luật rải** (§6.4, §23.10).
   - **Vùng.** Xét theo thứ tự, trúng vùng nào trước thì lấy vùng đó:
     - *Cấm mọi vật:* mặt đường (nửa bề rộng + 0,8 m + `r`); đồ trang trí đường (`dressing`; cỡ lấy từ `road.ts`, không rõ thì đá bờ 1 m, thềm 3 m nhân `scale`, ghi lại); cầu; sân đá; nền nhà đặt sẵn (`r` nhà + `gapM`); đĩa mỏ (3,7 m, hay sân đá + 1,5 m nếu lớn hơn); đĩa cây luật (`TREE.radiusM` 1,5 + `r`); ngoài [−88, 88]².
     - `water`: trong rect nước. Rect chạm mép sân thì kéo dài ra mép vòng ngoài, như `ground.ts`. Chỉ `reed-clump` và `kind` `rock`, tâm trong 0,6 m sát mép dài (bờ dốc). Cố định.
     - `keep`: trong `keepClearM` 11 quanh Lũy, ngoài sân đá. Chỉ cỏ, hoa chữ thập. Không vật lớn, để khỏi bàn vùng thẻ chữ của Lũy. Cố định.
     - `ring`: 48 < max(|x|, |z|) ≤ 88. Cố định.
     - `band`: 46 < max(|x|, |z|) ≤ 48. Cố định.
     - `field`: phần còn lại trong `buildHalfM` 46 (đất xây được). **Mọi vật `clearOnBuild: true`.** Hai đầu cầu là `field`.
   - **Vật cố định chỉ ở vùng sim cấm xây.** Vật có chân chạm đất xây được thì phải `clearOnBuild: true`.
   - **Cây cảnh** (`kind` `tree`, `bamboo`, `canopy`) cách mọi cây luật ≥ 4 m, tâm tới tâm.
   - **Hành lang cửa quái:** |x − gate.x| ≤ 6 và z ≤ −46: không vật lớn.
   - **Dốc:** có `heightAt` thì không đặt vật (trừ `kind` `rock`) nơi chênh cao trên 2 m vượt 1,4 m (dốc > 35°, vách Thác Bạc).
   - **Poisson có cụm, theo seed:**
     - trường mật độ từ nhiễu giá trị băm số nguyên, cỡ cụm 20–30 m;
     - Poisson đĩa (Bridson) có khoảng tối thiểu theo chân: tâm hai vật lớn ngoài mép rừng cách ≥ 0,8 × (rA + rB);
     - cùng seed cho cùng byte đầu ra.
   - **Biến thể:** với mỗi `type` có ≥ 2 biến thể, láng giềng gần nhất cùng `type` của mỗi vật dùng biến thể khác. Đồ thị láng giềng gần nhất không có chu trình, nên hai màu luôn đủ.
   - **Lệch:** `scale` 0,85–1,15; `flip` khoảng một nửa; `tint` 0,96–1,04.
   - **Mép rừng** ở `ring`:
     - 2–4 hàng song song mép sân, bo ở góc;
     - hàng 0 cách mép sân 2–6 m; mỗi hàng sau cách hàng trước 5–9 m;
     - chủ yếu `canopy`; hàng 0 trộn `tree`, `bamboo`;
     - hàng sau lệch nửa khoảng so với hàng trước;
     - hàng sau cao hơn: trung bình `scale` hàng r+1 ≥ 1,05 × hàng r;
     - hàng sau tối hơn 8 %: `shade` = 0,92^row;
     - tán khối được chồng nhau; luật 0,8 × (rA + rB) không áp trong mép rừng;
     - chừa khe ở hành lang cửa, ở suối và ở chỗ dốc.
   - **Dễ đọc trên `field`** (số khởi điểm, chỉ ghi số, không thành test): cây cao (`heightM` ≥ 8) ≤ 15 % số vật lớn của `field`, và cách tim đường ≥ 6 m.
   - **Bậc:** một danh sách xếp theo ưu tiên, bậc lấy phần đầu. Low ⊂ Medium ⊂ High: một vật có ở bậc thấp thì có ở bậc cao với đúng mọi trường. Bậc thấp bớt vật `field` trước. Low giữ ≥ 2 hàng mép rừng.
   - **Thiếu loại** (tập chỉ có 8 cây đã nhận): phần của loại thiếu để trống, không lấp bằng loại khác.
5. **Ca test** (trong `tests/td-scenery-layout.test.ts`):
   1. **Thuần:** đọc mã nguồn module; chỉ có các import được phép; không `three`, `Math.random`, `Date`, `sin`, `cos`.
   2. **Tất định:** cùng đầu vào cho kết quả bằng nhau sâu; seed khác cho mã băm khác. Đầu vào đóng băng sâu (`Object.freeze`) không bị đổi.
   3. **Mã băm vàng:** FNV-1a 32 bit trên JSON của `items` (x, z, r làm tròn 0,01; `scale`, `tint`, `shade` làm tròn 0,001). Ba seed (mặc định, 1, 20261030) × ba bậc, trên tập mẫu. Lưu `tests/golden/td-scenery-layout.json`.
   4. **Ngân sách:** vật lớn ≤ `large`, chữ thập ≤ `cross` mỗi bậc; Low có 0 chữ thập; Low ⊂ Medium ⊂ High.
   5. **Đất xây được:** 0 vật cố định có chân chạm đất mà `buildableAt` nhận.
   6. **Kiểm chéo với sim:** world mới có nhà đặt sẵn (`tests/td/fixtures.ts`). Trên lưới 1 m trong [−46, 46]², ở mọi điểm cách một vật cố định < 2,0 + `r`, gọi `canPlace(w, <chỉ số archer>, x / BUILD.snapM, z / BUILD.snapM, true)` (nhà S; `canPlace` nhận tọa độ theo phần tư mét; `true` bỏ kiểm giá): **0 điểm được nhận**. Ghi số điểm đã thử.
   7. **Vùng cấm:** 0 vật trên đường, đồ trang trí đường, nước (trừ ngoại lệ bờ), cầu, sân đá, nền nhà, đĩa mỏ, đĩa cây luật, ngoài [−88, 88]²; 0 vật lớn trong `keepClearM` và hành lang cửa; 0 vật (trừ đá) ở dốc > 35°.
   8. **Cây cảnh và cây luật:** khoảng cách nhỏ nhất ≥ 4 m.
   9. **Biến thể:** 0 vật có láng giềng gần nhất cùng `type` dùng cùng biến thể.
   10. **Lệch:** `scale` ngoài mép rừng trong 0,85–1,15; `tint` trong 0,96–1,04; `flip` 40–60 % ở mỗi `type` có ≥ 20 vật.
   11. **Cụm:** tỉ số phương sai trên trung bình (VMR) của số vật lớn mỗi ô 8 m trên `field` ≥ 1,5 (High, tập mẫu); khoảng cách tối thiểu 0,8 × (rA + rB) đạt.
   12. **Mép rừng:** mọi vật có `row` ≥ 0 nằm trong `ring`; mỗi cạnh 2–4 hàng; tỉ lệ `scale` giữa hàng ≥ 1,05; `shade` = 0,92^row (±0,001); khe lớn nhất ở hàng 0 ≤ 1,5 × khoảng, trừ hành lang cửa, suối, dốc; Low ≥ 2 hàng.
   13. **Tập thật:** chạy lại ca 4–12 trên `scenery-set.json`, một lần chỉ mục `accepted: true`, một lần đủ mục (trừ ca 3 và ca 11).
6. **Tờ kiểm** bằng script `scripts/td/scenery-layout-sheet.ts` (chạy `node --import tsx`). Vẽ từ dữ liệu, nhìn thẳng từ trên, không dựng cảnh. Tờ kiểm nội bộ, không phải ảnh người chơi thấy.
   - Script viết SVG, đổi sang JPG bằng `magick`. Mỗi JPG < 1 MB.
   - Lớp nền: ô vuông 46, 48, 88; đường theo `widths`; nước; cầu; sân đá; nền nhà; cây luật (đĩa 1,5 m đỏ, vòng 4 m nét đứt); hành lang cửa.
   - Mỗi vật một hình tròn bán kính `r`, màu theo `kind`. Cố định: viền liền. `clearOnBuild`: viền nét đứt. Mép rừng: đậm dần theo `shade`. Có chú giải.
   - `tmp/202/layout-high.jpg`, `layout-medium.jpg`, `layout-low.jpg`: seed mặc định, tập đủ, 10 px/m (1760 px).
   - `tmp/202/layout-accepted-high.jpg`: chỉ 8 cây đã nhận.
   - `tmp/202/field-high.jpg`: riêng [−48, 48]² ở 20 px/m.
   - `tmp/202/seeds.jpg`: ba seed cạnh nhau ở High, mỗi ô 880 px.
   - `tmp/202/layout-<bậc>-default.json`: dữ liệu thô cho L3 xem.
   - SVG trung gian: script tự xóa ngay sau khi đổi sang JPG (chỉ file nó vừa ghi), nên `tmp/202/` chỉ còn các tờ JPG và JSON trên. Không chạy `prune --apply` trên thư mục này: các tờ là sản phẩm, còn `prune` xóa JPG nào chưa được tài liệu dẫn. Chỉ chạy thử `node tools/capture-prune/prune.mjs games/.wt-td-scenery/tmp/202` và chép đầu ra vào báo cáo.
7. **Changelog** `docs/changelog/<ngày>-scenery-layout.md` trong worktree, tiếng Việt: việc gì, luật nào, số chính, việc còn cho L3.

## Cấm

- Mọi lệnh git có ghi.
- Sửa file có sẵn trong `src/**`. Chỉ được **thêm** `src/view/3d/scenery-layout.ts`.
- Viết `scenery.ts` hay bất kỳ renderer, shader, mesh nào (việc L3). Sửa `src/kit/**`; chạy đồng bộ kit.
- Import Map Factory đã dừng (`shared/game-kit/map/**`, nhánh `map-factory`, `along.ts`) hay bất kỳ gì ngoài repo game (`docs/games/DEPLOY_INDEPENDENCE.md`).
- Sửa file của 199 (`scripts/td/scenery-set.json`, `scripts/td/prepare-scenery.mjs`, manifest, test của 199) và `package.json`.
- Đổi luật chơi, `src/content/**`, `src/sim/**`, ván vàng.
- Dev server, trình duyệt, mạng, cài gói.
- Đụng worktree khác (`.wt-td-1c`, `.wt-td-keys`, `.wt-td-codex` và các worktree Dragonhold, Last Line), game khác, Tu Tiên.
- Ghi ảnh ra ngoài `games/.wt-td-scenery/tmp/202/`; đưa ảnh vào Git; ghi ra ngoài repo.

## Kiểm (ghi số)

1. `pnpm check` xanh (ghi số test). `pnpm td:golden:check` bằng (dán dòng kết quả). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. `git status --short -uall` trong worktree chỉ có:
   - `src/view/3d/scenery-layout.ts`;
   - `tests/td-scenery-layout.test.ts`, `tests/golden/td-scenery-layout.json`;
   - `scripts/td/scenery-layout-sheet.ts`;
   - `docs/changelog/<ngày>-scenery-layout.md`;
   - cộng file của 199 nếu Claude chưa commit (ghi rõ).

   `git diff --stat` trên file đã theo dõi: rỗng, hoặc chỉ file 199 như lúc bắt đầu.
3. md5 file của 199 lúc đầu và lúc cuối bằng nhau: `202/md5-199.txt`.
4. **Bảng đếm** `202/counts.json` và trong báo cáo: bậc × (tập đã nhận | tập đủ) × vùng × `kind`, cạnh ngân sách.
5. **Số luật** `202/rules.json`:
   - vật cố định trên đất xây được (0); điểm `canPlace` chạm vật cố định (0) trên số điểm đã thử;
   - vật trong mỗi vùng cấm (0 mỗi mục);
   - khoảng cách nhỏ nhất cây cảnh tới cây luật;
   - cặp láng giềng gần nhất cùng biến thể (0); số cặp chạm tán cùng sprite (chỉ ghi);
   - VMR; khoảng cách tối thiểu nhỏ nhất / (rA + rB);
   - mép rừng: số hàng mỗi cạnh, tỉ lệ `scale` và `shade` giữa hàng, khe lớn nhất hàng 0;
   - tỉ lệ cây cao trên `field`, khoảng cách nhỏ nhất tới tim đường.
6. **Thời gian:** trung vị 5 lần `sceneryLayout` High, tập đủ. Đích ≤ 50 ms. Không đặt test thời gian. Ghi `202/timing.json`.
7. **Tờ kiểm:** đường dẫn và cỡ từng file. Một dòng nhận xét mỗi tờ: thấy cụm không, mép rừng kín không, đất quanh đường có thoáng không.

## Báo cáo phải có

- **Đặc tả dữ liệu cho L3:** trường, đơn vị, khung tọa độ, thứ tự sắp, cách áp `scale × heightM`, `flip`, `tint × shade`, ý nghĩa `row`, `zone`, `clearOnBuild`, `cross`; cách gọi theo bậc. Đủ để L3 viết `scenery.ts` mà không đọc mã.
- Bảng `FOOT` và mọi hằng chỉnh được, với giá trị đang dùng.
- Chỗ làm khác phiếu và vì sao.
- Lệnh chạy lại test và tờ kiểm.

## Rủi ro (ghi vào báo cáo, không tự xử lý)

- Hình dữ liệu có thể chưa hợp L3. Ghi trường nào L3 có thể cần thêm.
- Số lượng có thể phải chỉnh sau khi Claude xem trong 3D.
- Mép rừng phía nam nằm giữa camera và sân. Ở góc thấp có thể che. L3 xử lý bằng dither.
- Mỗi loại chỉ có v3, v4. TK đòi ≥ 4 biến thể; lật ngang chỉ bù một phần.
- 117, 118 chưa được nhận. Tập đã nhận chỉ có cây, nên bản chạy thật lúc đầu chỉ có cây và mép rừng.
- Low chưa là bậc 3D (`Tier3D` chỉ có `medium`, `high`). Low giữ theo ngân sách TK.

**Xong khi:** có module thuần, test xanh với mã băm vàng, các tờ kiểm, báo cáo có đặc tả dữ liệu; bảy mục kiểm có số. Claude duyệt rồi commit; L3 gắn vào `scenery.ts`.
