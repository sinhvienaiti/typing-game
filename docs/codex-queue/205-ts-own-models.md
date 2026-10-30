# Phiếu 205 · Last Line · Bộ model riêng (12 id, High và Medium), nạp theo bậc, bỏ đường sang thư viện Space (TS-M1-01, TS-M1-14)

**Nguồn:**
- `docs/games/MAP1_PRODUCTION.md` §3.2 mục 1: "TS-M1-01 · P0 · G7. Lúc chạy đọc model của Space."
- Cùng mục, mục 7: "TS-M1-14 · … Lần đầu tải 9,06 MB; Medium vẫn nạp GLB High."
- `docs/codex-queue/168-report.md` §3: lỗi `foreign-asset` là "Lỗi thật, chặn cả production/demo".
- Thiết kế: `docs/games/DEPLOY_INDEPENDENCE.md` §5.1 (bộ model riêng, lệnh nhập, không chép id dự phòng).
- Việc này từng là của làn T (phiếu 090: "việc model là TS-M1-01, Claude làm sau"). Chủ dự án giao theo khuyến nghị của Claude; hôm nay: "tăng thêm việc cho codex cho tôi".

**Báo cáo:** `docs/codex-queue/205-report.md` (tiếng Việt), thư mục `docs/codex-queue/205/`.

**Không trùng:** 090 (từ vựng), 092 (dev handle), 111 và 111b (bộ kiểm gói của kit), 168 (chỉ liệt kê chỗ trỏ sang Space), 156 (ảnh nguồn Lightbearer). Lỗi `local-host` còn lại là việc của phiếu 207.

**Sau phiếu này (Claude):** duyệt, gộp `ts-codex` vào `main`, chép GLB sang cây chính, `media:push`, bỏ alias model của Last Line trong nginx (phiếu 216 giữ alias tới lúc gộp), kiểm trình duyệt ở 1280 và 1920.

## Nơi làm và luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (thư mục làn `.`), vì `pnpm models:prepare` chạy từ repo cha (như phiếu 090, 168).
- **Mã:** worktree `games/.wt-ts-codex`, nhánh `ts-codex`, HEAD `184c90d` (cùng nội dung với `main` `79db628`). Mọi đường mã dưới đây tính từ worktree này.
- **Trước khi làm:** `git -C games/.wt-ts-codex status --short` phải rỗng và HEAD phải là `184c90d`. Khác thì dừng, ghi vào báo cáo.
- **Chỉ được ghi:**
  - `public/assets/typing-survival/models/**` (manifest và GLB; GLB không vào Git);
  - `.gitignore` (ba dòng ngoại lệ, việc 2);
  - `src/view/models.ts`, `src/view/crowd.ts`, `src/view/ship.ts`, `src/view/bolts.ts`, `src/view/combat.ts`, `src/app/main.ts` (chỉ chỗ truyền bậc và bộ súng);
  - `vite.config.ts`;
  - `tests/own-models.test.ts` (mới); test cũ chỉ khi nó đọc đúng phần đã đổi, ghi lý do;
  - `README.md` (đoạn "Models");
  - `docs/changelog/2026-10-30-own-models.md` (mới, tiếng Việt);
  - `dist/`, `tmp/` và cache trong `node_modules/` (Git bỏ qua);
  - `docs/codex-queue/205-report.md`, `docs/codex-queue/205/` (repo cha).
- **Chỉ đọc:** `games/space-typing/public/assets/space-typing/models/manifest.json` và 24 file GLB của 12 id dưới đây.
- Được dùng git chỉ đọc (`status`, `diff`, `log`, `show`, `check-ignore`).
- Test trước, mã sau. Chú thích tiếng Anh, ngắn. Chữ người chơi thấy là tiếng Anh; phiếu này không cần đổi chữ nào.
- Luật chơi, ván vàng và mã băm chương không đổi.
- **Model chép nguyên** (chủ dự án 29/10: model đang có giữ nguyên). Không nén lại, không giảm mặt, không KTX2, không đổi texture.

## Cấm

- Mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- Sửa `src/kit/**`; chạy `kit:sync`. Hằng `SPACE_MODEL_MANIFEST_URL` của kit giữ nguyên; game chỉ thôi dùng nó.
- Sửa `media/media.config.json` (đã có `modelsDir`, `modelsManifest` cho `typing-survival`; file đang có diff chưa commit của việc khác).
- Sửa `scripts/models/**`, `scripts/media/**`, nginx, `shared/`, tài liệu trong `docs/games/` của repo cha. Script có lỗi thì ghi lại, không sửa.
- Ghi vào `games/space-typing`, `games/typing-survival` (cây chính), worktree khác (`.wt-ts-typefx`, `.wt-dh-*`, `.wt-td-*`), game khác; đụng Tu Tiên.
- Chạy `media:push`, `media:pull`; dev server, trình duyệt, mạng.
- Chép id dự phòng: `rainbow-mine-lod`, `rainbow-scout-lod`, `draconis-v2`, `draconis`.
- Ghi file ra ngoài repo.

## Việc

1. **Số trước.** Lưu vào `docs/codex-queue/205/`:
   - `pnpm check` trong worktree (số test đạt, số file `verify-kit`);
   - `node --import tsx scripts/chapter-hashes.ts` chạy trong worktree, ra `205/chapter-before.txt` (đường tuyệt đối; 152 dòng);
   - sha256 của `tests/golden/s0-trace.json`;
   - `git status --short` của repo cha, ra `205/parent-status-before.txt` (cho Kiểm 9).
2. **Manifest được vào Git, GLB thì không.** Trong `.gitignore` của worktree, ngay sau dòng `public/assets/**`, thêm đúng ba dòng. Git không mở lại file nằm trong thư mục đã bị bỏ qua, nên phải mở hai thư mục cha trước (cùng cách `games/typing-defense/.gitignore`):

   ```gitignore
   !public/assets/typing-survival/
   !public/assets/typing-survival/models/
   !public/assets/typing-survival/models/manifest.json
   ```

   Thư mục con (`ships/`, `enemies/` …) và mọi `.glb` vẫn bị bỏ qua (`public/assets/**`, `*.glb`). Kiểm bằng `git check-ignore -v`: manifest không bị bỏ qua, mọi `.glb` bị bỏ qua.
3. **Nhập 12 id, hai bậc.** Chạy từ repo cha, đúng một lệnh:

   ```bash
   pnpm models:prepare --root games/.wt-ts-codex \
     --out games/.wt-ts-codex/public/assets/typing-survival/models \
     --url-base /assets/typing-survival/models/ \
     --import games/space-typing/public/assets/space-typing/models/manifest.json \
     --only ships/vanguard,heroes/draconis-v3,enemies/rainbow-mine-3d,enemies/rainbow-scout-3d,enemies/rainbow-tank-3d,enemies/rainbow-shield-3d,enemies/rainbow-splitter-3d,skills/vanguard-bolt,skills/solar-lance-bolt,skills/frost-seraph-bolt,skills/crimson-talon-bolt,skills/dragon-fireball \
     --tiers high,medium --generated-at 2026-10-30T00:00:00.000Z
   ```

   - `--out` và `--url-base` là bắt buộc. Không có chúng, script lấy tên thư mục `.wt-ts-codex` làm id game và ghi sai chỗ.
   - Mọi URL trong manifest bắt đầu bằng `/assets/typing-survival/models/`.
   - Script ghi file tạm `.tmp-<pid>` cạnh file đích. Sau lệnh, không còn file tạm nào. Thấy file mới ngoài worktree và `docs/codex-queue/205*` thì ghi đường vào báo cáo.
   - Dòng `WARN` nào của lệnh cũng chép vào báo cáo.
4. **Đường riêng.**
   - `src/view/models.ts`: xuất `MODEL_MANIFEST_URL = "/assets/typing-survival/models/manifest.json"` và dựng `ModelLibrary` với nó. Bỏ import `SPACE_MODEL_MANIFEST_URL`. Sửa chú thích đầu file cho đúng.
   - `vite.config.ts`: bỏ `spaceModels`, biến `SPACE_MODELS_DIR`, `modelsDir`, `modelsUrl`. Plugin chỉ còn `routes: {}` thì bỏ hẳn plugin và import của nó; Vite tự phục vụ `public/`. Giữ lại thì ghi lý do.
   - Sửa chú thích đầu `src/view/bolts.ts` ("from Space's library") cho đúng.
5. **Bậc model theo chất lượng (TS-M1-14).**
   - Một hàm thuần trong `models.ts`, ví dụ `modelTier(tier: Tier): "high" | "medium"`: Low → `medium`, Medium → `medium`, High → `high`, Ultra → `high`.
   - Low nạp Medium, không bỏ 3D: luật 28/10 cấm hình vẽ bằng mã trên màn. `DEPLOY_INDEPENDENCE.md` §5 dòng 2 ghi "Low bỏ 3D", mâu thuẫn với luật này. Không sửa tài liệu đó; ghi vào mục "Cần Claude quyết" của báo cáo.
   - `crowd.ts:180`: `loadMesh("enemies", ids, modelTier(tier))`.
   - `ship.ts:111`: `pickModelTier(entry, modelTier(tier))`.
   - Truyền `tier` từ `main.ts:134–135` (hàm dựng hay `load()`, chọn một cách, ghi lại).
   - `bolts.ts` dùng cùng hàm cho Medium, High, Ultra. Luật Low của đạn giữ nguyên (không đạn 3D, chỉ vệt sáng). Ghi vào "Cần Claude quyết".
6. **Đạn chỉ nạp cho súng đã chọn.**
   - Bộ súng và bậc cố định trong một trang: đổi súng hay đổi chất lượng thì trang nạp lại (`main.ts:355`, `:399`). Vậy "nạp khi chọn súng" nghĩa là: lúc dựng trận chỉ nạp đạn của súng có trong `world.header.kit.guns`.
   - Bảng: Pulse Gun (`xung`) → `vanguard-bolt` (phi công Draconis: `dragon-fireball`); Scatter Gun (`tan`) → `solar-lance-bolt`; Rail Gun (`ray`) → `frost-seraph-bolt`; Star Mortar (`phao`) → `crimson-talon-bolt`; Heat Beam (`tia`) không có đạn.
   - Súng không chọn thì không request file nào.
   - `ready` vẫn thành `true` khi không có gì để nạp.
   - `bolts.add` cho loại chưa nạp giữ hành vi cũ (trả `false`, chỉ vệt sáng).
   - Truyền bộ súng vào `Bolts` qua `combat.ts:107` và `main.ts:164`.
7. **README:** đoạn "Models" ngắn. Gồm: lệnh nhập lại ở việc 3, 12 id, bậc theo chất lượng, GLB không vào Git, `media:push` do Claude chạy.
8. **Changelog** `docs/changelog/2026-10-30-own-models.md`: TS-M1-01 và TS-M1-14 đã sửa gì, vì sao (G7, G4), số đo ở mục Kiểm.

## Test (viết trước, trong `tests/own-models.test.ts`)

Test chỉ đọc file của repo game; không cần GLB (bản clone sạch không có GLB).

1. **Manifest:** đúng tập 12 id; id nào cũng có `high` và `medium`; mọi URL bắt đầu bằng `/assets/typing-survival/models/`; không có id `-lod`, `draconis-v2`, `draconis`.
2. **URL theo bậc:** dựng `ModelLibrary({ manifests: MODEL_MANIFEST_URL, fetcher })` với fetcher giả trả manifest của game. Với cả 12 id:
   - Low và Medium ra `.medium.glb`;
   - High và Ultra ra `.high.glb`.
3. **Đạn theo súng (mock `loadMesh`):**
   - Vanguard, `[xung, tia]` → chỉ `vanguard-bolt`;
   - Draconis, `[xung, tia]` → chỉ `dragon-fireball`;
   - `[tan, ray]` → `solar-lance-bolt` và `frost-seraph-bolt`;
   - `[phao, xung]` → `crimson-talon-bolt` và `vanguard-bolt`;
   - Low → không id nào; Medium hỏi bậc `medium`, High và Ultra hỏi `high`.
4. **Đàn quái và tàu hỏi đúng bậc:** Low và Medium hỏi `medium`, High và Ultra hỏi `high`. Dựng `Crowd` hay `Ship` trong node không được (canvas, WebGL) thì tách bảng id và chọn bậc ra hàm thuần rồi test hàm đó; ghi lựa chọn.
5. **Quét mã:** `src/` (trừ `src/kit/**`), `vite.config.ts`, `index.html` không chứa chuỗi đường Space. Ghép chuỗi tìm từ hai phần (`"/assets/" + "space-typing/"`) để test không tự bắt chính nó. Fixture cố ý chứa chuỗi đó (`tests/deploy-pack.test.ts`) giữ nguyên.
6. **`dist` không có đường Space:** không viết test build trong vitest (chạy song song với test thời gian, làm đỏ giả). Kiểm bằng Kiểm 4 và 5.

## Kiểm (ghi số vào báo cáo)

1. `pnpm check` xanh: số test trước và sau, `verify-kit` 61/61. Test thời gian đỏ khi máy bận thì chạy riêng ba lần, ghi số.
2. **Ván vàng:** sha256 `tests/golden/s0-trace.json` không đổi. Chạy lại `chapter-hashes.ts` ra `205/chapter-after.txt`; `diff` với bản trước rỗng (152 dòng).
3. **Manifest:** 12 mục × 2 bậc. Mỗi GLB: byte, sha256 bằng file nguồn của Space, `?v=` bằng 10 ký tự đầu sha256. Cộng byte High, cộng byte Medium, byte manifest. Lưu `205/manifest-check.json`.
4. `pnpm build`, rồi tìm `/assets/space-typing/` trong `dist/`: **0 file**. Ghi lệnh và đầu ra. Còn sót chỉ vì hằng của kit (`SPACE_MODEL_MANIFEST_URL`) bị đóng gói thì ghi file, dòng và lý do; không sửa kit, để Claude quyết.
5. `pnpm deploy:pack`, rồi `node src/kit/tools/deploy/check-pack.mjs dist --game typing-survival --json` lưu `205/check-pack.json`: **0 lỗi `foreign-asset`**; chỉ còn `local-host` (phiếu 207). Ghi số file và byte của `dist`.
6. **Lần chơi đầu**, so với ngân sách 4 MB (`docs/HOSTING_PLAN_2026-10-25.md` §7; `DEPLOY_INDEPENDENCE.md` §5.1): một script chỉ đọc `docs/codex-queue/205/first-play.mjs` tính từ manifest và chính bảng id trong mã, không gõ tay số. Hai phi công × High và Medium, bộ súng mặc định của c1-s1 (Pulse Gun + Heat Beam), cộng cả manifest. Lưu `205/first-play.json`, đặt cạnh số cũ 9,06 MB. Bậc nào vượt 4 MB thì ghi, **không** thu nhỏ model.
7. **Còn chỗ nào trỏ sang Space:** đối chiếu 46 vị trí của `docs/codex-queue/168/space-references.json`. Ghi chỗ nào đã hết, chỗ nào còn (chú thích xuất xứ của kit, hằng trong kit) và vì sao.
8. **Danh sách media cho Claude:** 24 GLB và manifest (đường, byte, sha256). Kèm lệnh nhập cho cây chính sau khi gộp: `--root games/typing-survival`, không cần `--out` và `--url-base`, vì GLB không đi theo nhánh Git.
9. `git -C games/.wt-ts-codex status --short -uall`: chỉ file của việc này; có `manifest.json`, không có `.glb`. `git status --short` của repo cha so với `205/parent-status-before.txt`: chỉ thêm `docs/codex-queue/205*`.

**Cần Claude quyết (mục riêng trong báo cáo):** luật Low (việc 5); đạn ở Low; số High vượt ngân sách (Kiểm 6).

**Rủi ro, ghi vào báo cáo:**
- Tàu Vanguard chỉ là bản chép tạm. Hướng B thay bằng Lightbearer; model Tripo chưa dựng. Không sửa lựa chọn phi công hay socket của tàu.
- Script của repo cha có thể ghi file tạm ra ngoài worktree. Giữ chúng trong worktree; có thì báo.

**Xong khi:** tám mục việc, sáu mục test và chín mục kiểm đạt; `deploy:pack` 0 `foreign-asset`; ván vàng giữ nguyên. Claude duyệt rồi commit.
