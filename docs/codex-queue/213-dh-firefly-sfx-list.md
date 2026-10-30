# Phiếu 213 · Dragonhold · Map 1 (L2-cau): danh sách âm Firefly ghép với các clip VFX lửa Firefly

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §3, làn "Âm thanh: đường Firefly". Chủ dự án tự tạo âm trong Adobe Firefly (Generate Sound Effects, model của Adobe, dùng thương mại được). Làn FF phải soạn danh sách âm theo mã sự kiện: prompt tiếng Anh, gợi ý diễn bằng giọng, nhịp VFX. Danh sách đó chưa có: `docs/games/audio/` chưa tồn tại.
- `docs/games/MAP1_PRODUCTION.md` §1.1, cổng G3 của Dragonhold: "Âm chưa ai nghe".
- Lửa Rồng nay dùng clip Firefly Video (`docs/games/vfx/FIREFLY_VFX_LIST.md`, chín id theo pha). Mỗi âm lửa phải khớp nhịp và pha của clip đi cùng nó.
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Không trùng:** 173 (texture lửa), 182 và 189–193 (tiếng phím, bảng Sound), `FIREFLY_VFX_LIST.md` (chỉ video). Phiếu này chỉ viết danh sách. Không tạo âm, không gắn vào game.

**Báo cáo:** `docs/codex-queue/213-report.md` (tiếng Việt), thư mục `docs/codex-queue/213/`.

**Chỉ chạy khi** phiếu 212 đã xong và Claude đã duyệt, commit. Kiểm bằng ba lệnh, thiếu một thì dừng, ghi vào báo cáo:
1. `git log -1 --format=%h -- docs/games/audio/firefly/schema.json docs/games/audio/firefly/README.md` ra một mã commit (Claude đã commit lược đồ của 212);
2. `docs/codex-queue/212/check.mjs` có và export hàm kiểm lược đồ (đọc file, không sửa);
3. `schema.json` có các trường `sourceCommits`, `branchOnly`, `clips`, `clipsWhy` (phiếu 212 thêm cho phiếu này).

## Nơi làm

- **cwd:** repo cha (`.`), nhánh đang có. Không đổi nhánh.
- Trước khi ghi gì, lưu `git status --short -uall` của repo cha vào `213/status-before.txt` và `git -C games/dragon-hold status --short` vào `213/game-before.txt`.
- **Chỉ được ghi** bốn chỗ:
  - `docs/games/audio/firefly/dragon-hold.md`;
  - `docs/games/audio/firefly/dragon-hold.json`;
  - thư mục `docs/codex-queue/213/`;
  - `docs/codex-queue/213-report.md`.
- Đọc Dragonhold ở checkout chính `games/dragon-hold`. `git -C games/dragon-hold branch --show-current` phải ra `main`; khác thì dừng.
- Nhánh `dh-vfx` chưa gộp. Chỉ đọc nó qua object của git, không mở worktree:
  - `git -C games/dragon-hold diff main dh-vfx -- src/audio/` (khoảng +112 dòng);
  - `git -C games/dragon-hold show dh-vfx:<đường dẫn>` cho `src/audio/catalog.ts`, `src/audio/map-events.ts`, `src/audio/index.ts`, `src/audio/engine.ts`, `src/view/fx.ts`, `src/view/skyfire.ts`, `src/view/flipbook.ts`.
- Ghi mã commit đã đọc: `git -C games/dragon-hold rev-parse --short main` và `git -C games/dragon-hold rev-parse --short dh-vfx` (hai lệnh riêng; lúc kiểm phiếu 30/10 là `1f1de48` và `be6e2dc`; `dh-vfx` còn đổi theo vòng chấm lửa 9).

## Đọc trước

- Của 212: `README.md` (tên trường, luật số lượt tạo, luật vòng lặp, cách chạy kiểm), `schema.json`, `212/check.mjs` (hàm export), `212-report.md`.
- Dragonhold `main`:
  - `src/audio/catalog.ts` (83 id; nguồn chuẩn của độ dài, bus, lặp hay không);
  - `src/audio/map-events.ts`, `src/audio/index.ts`, `src/audio/beds.ts` (id nào phát, khi nào);
  - `docs/audio/M0_SOUND_LIST.md` §5 (khi nào phát, tâm trạng).
- Map 1: `src/content/data/stages.ts` (`STAGE_M0`: map `L2-cau`, `carry`, `unlocks.heroSkills`), `waves.ts` (quái thật sự ra), `enemies.ts`, `generals.ts`, `our-side.ts`, `src/content/rules.ts` (Sky Fire `delayMs: 800`).
- Thẻ spec: 87 thẻ ở `tools/audio-lab/specs/dragon-hold/` (83 id catalog, 4 nhạc). Lấy `when`, `purpose`, `prompt.text`, `duration`, `variants.target`, `playback.mode`.
- `docs/games/AUDIO_PIPELINE.md` §8.1 (bảng âm Dragonhold: lửa thật, quái theo lớp, bẫy) và §11 (định dạng file).
- `docs/games/ART_DIRECTION_2026-10-28.md` §3 (bản sắc ải núi, để giữ giọng của prompt).
- `docs/games/VFX_STANDARD.md` §3.1 (năm pha A gồng, R tung đòn, T bay, I trúng, F dư âm) và §3.4 (thời gian theo khung 60 Hz).
- `docs/games/vfx/FIREFLY_VFX_LIST.md` và `tools/vfx-flipbook/dragon-hold.json` (pha của từng clip, có cả `fire-burst`).
- `docs/games/NAMES_EN.md`, mục Rồng Giữ Ải (Fire Breath, Sky Fire, Dragon Roar, Inferno, Spikes, Pine Bomb, Net Launcher, Grove Warden, Herb Hut, Moss Bannerman…).

## Việc

1. **Lập tập id phát ở L2-cau.**
   - Dò mọi lệnh `push(...)`, `at(...)`, `engine.bed(...)`, `engine.play(...)` trong `map-events.ts` và `index.ts`, trên `main` rồi trên `dh-vfx`.
   - Lọc theo những gì map 1 có:
     - quái trong `waves.ts`: `moss-grunt`, `moss-archer`, `tusk-boar`, `blight-wolf`, `thorn-wasp`, `thorn-ant`; tướng `moss-banner` (G01) ở đợt 5 và 10;
     - món trong `carry`: ba bẫy, Grove Warden, Herb Hut, Small Potion;
     - bốn chiêu: `breath`, `skyfire`, `roar`, `inferno`.
   - Mỗi id ghi nơi phát (file:dòng) và nhánh (`main`, `dh-vfx` hay cả hai).
   - Lưu tập này ở `213/fired-ids.json`.
2. **Mỗi id phát có một hàng** theo schema của 212.
   - Đủ các nhóm: đòn chữ (`fire.cast`, `fire.impact.a|b|c`, `impact.multi`), Fire Breath, Sky Fire, Dragon Roar, Inferno, các âm khác của Rồng, quái theo lớp, G01, bẫy, phe ta, báo nguy, mốc trận (`wave.horn`, `wave.clear`, thắng, thua), UI, học, nền.
   - `type.word`, `type.miss`, `type.back`, `type.switch` vẫn có hàng; chỉ `type.key` bị loại (bước 6).
   - Vòng lặp ghi `loop` và độ dài đích theo catalog: nền `amb.forest`, `amb.river`; bước bầy `enemy.*.march`; `move` từng quái trên `dh-vfx`. `amb.bird` là âm lẻ.
   - Prompt tiếng Anh, dựa trên `prompt.text` của thẻ spec, sửa cho hợp Firefly theo README 212.
   - Không tên riêng tiếng Việt trong prompt: Hỏa Long viết "the fire dragon".
   - Giữ số của catalog: `lengthMs` (ghi trong `basis`; `targetMs` lấy `duration.min_ms`, `max_ms` của thẻ spec, mà thẻ đã tính từ `lengthMs`), `bus`, `loop`. Mono hay stereo lấy `playback.channels` của thẻ (catalog không có trường này). Không đổi số nào.
3. **Id chỉ có trên `dh-vfx`:** id riêng từng quái của `foeSfx` và `FOE_SFX_IDS` (`enemy.<id>.spawn|move|attack|hit|death`, `general.moss-banner.*`; 7 quái của L2-cau × 5 = 35 id).
   - Vẫn có hàng, `branchOnly: "dh-vfx"`.
   - `FOE_SFX_IDS` gồm cả quái ngoài map 1: không thành hàng, chỉ ghi số lượng vào báo cáo.
   - Ghi id đó phát ở đâu, hay manifest chỉ nhận mà chưa có chỗ phát.
   - Ghi luật thay thế: có file thì phát thay âm lớp, không có thì âm lớp phát như cũ (`engine.ts` trên `dh-vfx`).
4. **Âm lửa ghép clip Firefly.** Áp cho `fire.cast`, `fire.impact.a|b|c`, `impact.multi`, `dragon.skyfire.cast`, `dragon.skyfire.impact`, `dragon.breath`, `dragon.inferno`.
   - Tìm clip được vẽ cho sự kiện đó trên `dh-vfx`: chỗ gọi `flip.pick("<id>")` và chỗ đọc `flip.pools["<id>"]` (ví dụ `flame-trail` cho dải lửa) trong `fx.ts` và `skyfire.ts`.
   - Ghi id clip và pha (A, R, T, I, F) theo `tools/vfx-flipbook/dragon-hold.json`, vào trường `clips` của hàng; không có clip thì `clips: []` và lý do ở `clipsWhy`.
   - Âm phủ nhiều pha thì ghi đủ clip theo thứ tự pha. Ví dụ `fire.cast`: R `muzzle-flash`, rồi T `fireball-head`, và `flame-trail` nếu mã thật sự dùng nó cho đòn này.
   - Mã chọn một trong vài clip (ví dụ `impact-big`, `impact-burst`, `fire-burst`) thì ghi đủ các clip có thể ra.
   - `dragon.skyfire.impact` cũng phát khi Inferno trúng: ghi cả hai.
   - Ghi nhịp mỗi cặp:
     - clip bắt đầu sau sự kiện bao nhiêu ms, hiện bao lâu (tính từ `life`, `frame`, `until`, `rate`, fps trong mã);
     - độ dài âm theo catalog;
     - điểm phải trùng, ví dụ đầu tiếng nổ trùng khung sáng đầu của `impact-big` trong 1 khung (17 ms);
     - Sky Fire: pha A nằm trong 0,8 s trễ của sim; ghi âm gồng và âm chạm khớp mốc đó thế nào.
   - Viết nhịp vào prompt và vào `syncNote` của từng clip; gợi ý diễn bằng giọng ở `voiceHint`. Ví dụ: "sharp attack at 0 ms, body to 300 ms, smoky tail to 1.1 s".
   - Âm lửa không có clip Firefly: ghi clip rỗng và lý do. Ví dụ trên `dh-vfx`, Fire Breath và Inferno vẽ bằng emitter `breath`, `inferno` của `fx.ts`. Không bịa cặp.
   - `charge-orb` lúc gõ đi với `type.key` (bị loại): ghi một dòng ghi chú.
5. **Thư mục nhận file** mỗi hàng: `~/AudioLab/inbox/firefly/dragon-hold/<id>/`. Chỉ ghi đường dẫn vào danh sách. Không tạo thư mục (nằm ngoài repo).
6. **Loại có lý do** (mục riêng, không thành hàng):
   - `type.key`: tiếng phím đã có bộ Firefly của 189–192.
   - Nhạc (`music.forest`, `music.wave`, `music.surge`, `music.general`, các lớp của `music.ts`): nhạc theo AUDIO_PIPELINE §8.1 (mẫu VSCO-2-CE, VCSL), không phải âm hiệu ứng.
   - Id catalog không phát ở L2-cau (ví dụ `enemy.quadruped.howl`, nếu đúng là không chỗ nào phát): ghi lý do.
   - Id trong `show.sounds` của content mà không thuộc catalog hay `FOE_SFX_IDS` (ví dụ `enemy.<id>.skill`, `trap.place`, `trap.spikes.stab`): liệt kê, không thành hàng.
7. **Tổng lượt tạo cho chủ dự án.**
   - Mỗi hàng có số lượt theo luật README 212. README chưa có luật thì lấy `variants.target` của thẻ spec, ghi rõ trong báo cáo.
   - Đầu `dragon-hold.md` ghi tổng, và tổng theo nhóm: lửa, Rồng (khác lửa), quái, G01, bẫy và phe ta, báo nguy và mốc trận, UI và học, nền.
8. **`dragon-hold.md` cho chủ dự án đọc.**
   - Nhóm theo buổi tạo. Lửa đứng đầu, vì đi cùng vòng chấm VFX lửa.
   - Mỗi hàng: id, tên tiếng Anh, khi nào phát, độ dài, lặp hay không, số lượt, prompt, clip và pha, thư mục nhận.
   - Phần giải thích viết tiếng Việt. Prompt và tên trong game viết tiếng Anh.
9. **`dragon-hold.json`** đúng `schema.json` của 212, cùng nội dung với `.md`. Ghi hai mã commit `main` và `dh-vfx` đã đọc vào `sourceCommits`.
10. **Script kiểm** `docs/codex-queue/213/check.mjs` (Node, không thêm thư viện):
   - import hàm kiểm lược đồ và hàm tính lượt từ `212/check.mjs`; không sửa file của 212;
   - đọc catalog `main` từ `games/dragon-hold/src/audio/catalog.ts`, catalog và `foeSfx` của `dh-vfx` qua `git -C games/dragon-hold show dh-vfx:src/audio/catalog.ts`; tập id phát từ `213/fired-ids.json`;
   - đếm thiếu, lạ, trùng, lỗi lược đồ; quét ký tự ngoài ASCII và từ cấm Q6, từ phủ định trong prompt như 212;
   - so `dragon-hold.md` với JSON: cùng tập id, cùng prompt từng chữ;
   - `--selftest`: cài sẵn ba lỗi (bỏ một hàng phát, thêm một id lạ, thêm chữ có dấu vào một prompt) và bắt đủ ba.

## Cấm

- Mọi lệnh git có ghi. Đổi nhánh của repo cha hay của `games/dragon-hold`.
- Mở, đọc hay ghi `games/.wt-dh-vfx` (làn V-dh2). Đọc `dh-vfx` chỉ qua `git -C games/dragon-hold show` và `diff`.
- Sửa file của game (`games/**`), `shared/**`, `tools/**`, thẻ spec, schema hay README của 212. Schema thiếu trường thì ghi vào báo cáo, không sửa schema.
- Ghi ra ngoài repo (kể cả `~/AudioLab`, `~/VFXLab`).
- Tạo, tải hay sửa file âm. Mạng, dev server, trình duyệt.
- Nhắc model đối tác trong prompt hay ghi chú. Danh sách này chỉ dành cho Adobe Firefly Generate Sound Effects.
- Chữ tiếng Việt trong prompt hay trong tên tiếng Anh. Đụng Tu Tiên.

## Kiểm (ghi số)

1. `node docs/codex-queue/213/check.mjs`: thoát 0, **0 thiếu, 0 lạ, 0 trùng**. Dán đầu ra vào báo cáo, lưu `213/check.txt`.
   - "Thiếu": id phát ở L2-cau (trên `main` hay `dh-vfx`) mà không có hàng hay mục loại có lý do.
   - "Lạ": hàng có id không thuộc catalog `main`, catalog `dh-vfx` hay `FOE_SFX_IDS` của `dh-vfx`.
   - `node docs/codex-queue/213/check.mjs --selftest`: bắt đủ 3/3 lỗi cài sẵn.
2. JSON hợp lệ theo `schema.json` (hàm kiểm của 212): **0 lỗi lược đồ**; ghi lệnh và kết quả.
3. Số: tổng hàng; hàng theo nhóm; hàng `dh-vfx-only`; âm lửa có clip; âm lửa không clip, kèm lý do; id bị loại; tổng lượt tạo.
4. Bảng nhịp của âm lửa: id, clip, pha, clip bắt đầu (ms), clip dài (ms), âm dài (ms), điểm phải trùng.
5. Ký tự ngoài ASCII trong mọi prompt và tên tiếng Anh của JSON: **0**. Ghi lệnh đếm.
6. Mã commit đã đọc của `main` và `dh-vfx`.
7. `git status --short -uall` sau, lưu `213/status-after.txt`: khác `213/status-before.txt` chỉ ở bốn chỗ được ghi. `git -C games/dragon-hold status --short` sau giống hệt `213/game-before.txt`; nhánh vẫn `main`.

**Xong khi:** có `dragon-hold.md`, `dragon-hold.json`, `213/fired-ids.json`, `213/check.mjs` và đầu ra của nó (0 thiếu, 0 lạ, 0 lỗi lược đồ, selftest 3/3) nằm trong báo cáo; đủ bảy mục kiểm. Claude duyệt rồi commit.

## Rủi ro

- `dh-vfx` chưa gộp. Vòng chấm 9 còn có thể đổi id hay cách chọn clip. Vì vậy phải ghi commit đã đọc; Claude chạy lại lệnh kiểm khi `dh-vfx` gộp vào `main`.
- Clip trong mã `dh-vfx` có thể khác bản chọn cuối. Ghi đúng như mã đang có, không đoán.
