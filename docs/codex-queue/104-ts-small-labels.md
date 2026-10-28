# Phiếu 104 · Tuyến Cuối · Ba nhãn nhỏ

**Nguồn:** lô Codex 1 của bản kiểm kê map 1 (`docs/games/map1/CODEX_BATCH.md`, phiếu 104). Phiếu 100 của lô (từ vựng Rồng) là phiếu **094** trong hàng; mọi chỗ ghi "phiếu 100" ở đây đã đổi thành 094.

**Báo cáo:** `docs/codex-queue/104-report.md`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game` (để ghi báo cáo). Mã nằm trong worktree nêu ở từng phiếu; mọi đường dẫn mã tính từ worktree đó.
- **Được dùng git chỉ đọc:** `show`, `log`, `diff`, `status`, `ls-tree`. **Cấm** mọi lệnh git có ghi (`add`, `commit`, `checkout`, `reset`, `stash`, `worktree`…).
- **Cấm:**
  - sửa `src/kit/**` của game (bản chép từ kit, có kiểm sha256);
  - sửa file golden hay chạy lệnh cập nhật golden (`dh:golden:update`, `td:golden:update`…);
  - ghi vào cây chính của game (`games/<id>`), worktree khác, game khác; đụng Tu Tiên;
  - sửa file ở repo cha (nginx, `scripts/`, `shared/`), trừ khi phiếu cho phép;
  - dev server, trình duyệt (sandbox không mở được cổng); media (ảnh, âm, GLB).
- **Cách làm:** test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn. Chuỗi người chơi thấy: câu tiếng Việt, danh từ game tiếng Anh (`docs/games/NAMES_EN.md`).
- **Mỗi phiếu có changelog** `docs/changelog/2026-10-29-<tên>.md` trong worktree, tiếng Việt: làm gì, vì sao, số đo.
- **Báo cáo** `docs/codex-queue/<số>-report.md` và thư mục `docs/codex-queue/<số>/` (log, số đo): file đã đổi; đầu ra của từng mục Kiểm, có số; chỗ nào làm khác phiếu và vì sao.
- **Nhận** khi Claude chạy lại kiểm, đọc diff, kiểm trên trình duyệt ở 1280 và 1920 khi phiếu đụng giao diện, rồi commit trên nhánh của worktree và gộp.

## Phiếu

**Vì sao:** kiểm kê map 1 (TS-M1-18, P2, cổng G5). Phiếu làm ba việc nhỏ, cộng hai việc chủ dự án đã quyết ngày 28/10 (câu 7 của `MAP1_PRODUCTION.md` §4.4): tên ải 2 là "ẢI 2 · SĂN PACK LEADER", và biển mục tiêu viết hoa cả câu, ví dụ "SWARM RÚT LUI!".

**Nơi làm:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`), **sau phiếu 090 và 092**. Giữ nguyên thay đổi của hai phiếu đó.

**Chỉ được ghi:**
- `src/view/hud.ts`;
- `src/view/screens-journey.ts`, `src/view/screens.ts`;
- file định nghĩa `ruleDetail` và `LEARN_RULES` nếu nằm ở file khác (ghi tên vào báo cáo; chỉ sửa chuỗi);
- test mới hoặc sửa trong `tests/`;
- `src/content/chapter-1.ts`: **chỉ** chuỗi `name` của ải 2 (dòng 59, hôm nay là `"Đầu Đàn"`);
- chuỗi trong `scripts/visual/scenarios/*.mjs` đang khớp hai chuỗi cũ (ví dụ `survival-s1-stage.mjs:88`, `huntPlateCounts`); chỉ sửa chuỗi so khớp, không đổi kịch bản;
- `docs/changelog/2026-10-29-small-labels.md` (mới);
- `docs/codex-queue/104-report.md`.

**Cấm thêm:** sửa `src/sim/**`, `src/content/**` (trừ chuỗi `ruleDetail` nếu nằm ở đó, và chuỗi `name` của ải 2); đổi luật, số, thứ tự màn.

**Việc:**
1. **Bến 3:** bản R1 chưa có Mốc, nên bỏ chữ "MỞ Ở MỐC" ở `hud.ts:161`. Bến 3 khóa hiện cùng dấu khóa như bến 4. Sửa chú thích ở `hud.ts:18` cho đúng.
2. **Esc ở thẻ ải:** hôm nay không làm gì. Cho Esc quay về màn nạp súng, giữ bộ súng đã chọn. Theo cách các màn khác đang xử lý Esc.
3. **Câu Luật học** (`screens-journey.ts:67`, phần `ruleDetail(stage)`): viết lại mỗi câu tối đa 14 từ, câu tiếng Việt thường, danh từ game tiếng Anh, bỏ thuật ngữ nội bộ. Ghi bảng câu cũ và câu mới vào báo cáo để Claude duyệt chữ.
4. **Tên ải 2** (chủ dự án 28/10): `name: "Đầu Đàn"` → `name: "Săn Pack Leader"` ở `src/content/chapter-1.ts`. Thẻ ải tự viết hoa (`screens-journey.ts:62`, `toUpperCase()`), nên sẽ hiện "ẢI 2 · SĂN PACK LEADER". Tìm mọi chỗ khác hiện tên ải (Hành trình, bảng tin, thẻ kết) và ghi vào báo cáo cách mỗi chỗ hiện tên mới.
5. **Biển mục tiêu viết hoa cả câu** (chủ dự án 28/10): ở `hud.ts` (khoảng dòng 362–365), "Swarm RÚT LUI" → "SWARM RÚT LUI", banner "Swarm RÚT LUI!" → "SWARM RÚT LUI!", "Pack Leader 2/3 · LỌT 1/2" → "PACK LEADER 2/3 · LỌT 1/2". Tìm các biển và banner khác trong `hud.ts` có danh từ game tiếng Anh viết hoa chữ đầu đứng cạnh chữ Việt viết hoa, và viết hoa cả câu theo cùng luật. Ghi bảng chuỗi cũ và mới vào báo cáo. Chỉ đổi chữ hiện ra, không đổi tên trong dữ liệu (`foes.ts` giữ "Pack Leader").

**Kiểm (bắt buộc):**
1. `pnpm check` xanh; ghi số test trước và sau.
2. **Băm chương giữ:** `node --import tsx scripts/chapter-hashes.ts` trước và sau, `diff` rỗng (152 dòng). Nếu riêng việc đổi tên ải 2 làm băm đổi (tên nằm trong dữ liệu được băm), thì trả tên cũ, ghi rõ vào báo cáo và làm tiếp các việc khác: Claude sẽ đổi tên ở chỗ hiện ra.
3. `grep -rn "MỞ Ở MỐC" src`: rỗng. `grep -rn "Swarm RÚT LUI\|\"Đầu Đàn\"" src scripts`: rỗng.
4. Test cho Esc ở thẻ ải nếu màn có bộ test DOM; nếu không, ghi rõ để Claude kiểm bằng `survival-s1-loadout`.
5. `git -C games/.wt-ts-codex status --short -uall`: chỉ các file trong "Chỉ được ghi" và file của 090, 092.

**Xong khi:** năm mục đạt. Claude kiểm thẻ ải 1 và 2, nạp súng, đầu bến, biển mục tiêu của ải 2 ở 1280 và 1920 (chữ viết hoa dài hơn, không được tràn).
