# Tu Tiên Thủ Ải — Kế hoạch M0a (hộp xám) và bản thử Tĩnh Tu (25/10/2026)

> **Vai:** kế hoạch xây theo khuôn `games/dragon-hold/LANES.md`: ai làm gì, ghi vào đâu, theo thứ tự nào, nghiệm thu bằng gì. Mọi luật và số ở [`00-canon.md`](00-canon.md); tệp này không có số riêng. Khi lệch, canon thắng.
> **Trạng thái:** kế hoạch, chưa có mã. `games/immortality-cultivation` (repo `sinhvienaiti/immortality-cultivation`) mới chỉ có `README.md`.
> **Hộp xám đúng nghĩa:** không hình thật, không âm phát ra (móc âm im lặng, không viết âm tổng hợp mới, Q6), không nhạc. Khối tạm một màu mỗi họ; đất, đường, decal, hạt, shader, instancing được làm bằng mã.
> **Lượt sửa 25/10** theo [`analysis/09-phan-bien-canon.md`](analysis/09-phan-bien-canon.md): ranh giới `local`/thế giới (`ward`, ví, đan phù), khởi đầu lạnh, sổ cái từ mới thuần, HN0 lùi theo phần vượt và đo ở N = 60/120/300, nối repo cha "đã có, chỉ kiểm", không sửa kit ở M0a, mốc 1a/1b của Làn 1, mọi trường `World` khai ở bước 0. Mã `PB-xx` trỏ về mục của tệp phản biện; luật ở canon D32–D46.

## 0. Đích và giới hạn

**Đích:** ải Thanh Thạch Ải (6 đợt + Thú Vương) chơi được từ thẻ tốc độ tới Thu Hoạch với đủ luật lõi của canon; bench 3D **HN0** có phán quyết trước mọi việc hình; bản thử Tĩnh Tu chạy ở trang riêng; bot và cổng in báo cáo.

| Có ở M0a | Không có ở M0a (mốc sau) |
|---|---|
| Sim số nguyên 60 Hz chép từ Rồng Giữ Ải (có `// Source:` và vé nợ đồng bộ); trường hướng cho 2 cổng + đường trời; trần thú sống 60; máu nguyên | Sơn Môn, Thư Lâu, Bảo Khí Lò, pháp bảo, lưu tiến trình (M1) |
| Người chơi cục bộ: chuột phải, mũi tên, Sinh lực, khiên, gục 8 s; đánh nền phát lệnh có `origin`; tác dụng đan phù lên mình; đỡ bằng `ward` (canon §9.1) | Cơ Duyên, Đạo Quả, Thiên Kiếp, Đại Triều, công pháp, Ngộ Chiêu (M1) |
| Trường phái Kiếm đủ 5 ô, tâm pháp 1 trong 2, Hộ thân hoặc thân pháp | Thổ thể, bot đạo đồng, Tam Tài, Hợp Trận (M1) |
| Trận Tâm, Kết Giới, Tâm nhãn, Trận Trụ, chiếm nhãn + Tẩy | Biến chủng hệ (khắc dạy ở trận 4 của M1); thú ở M0a vô hệ |
| 5 họ thú, 3 thuộc tính tinh anh, Lang Đầu Đàn, Thiết Bối Lang Vương 3 pha, Thế, phá thế | Mê Vụ Trận, Định Thân Phù (M1) |
| 3 cơ quan, cửa hàng lúc nghỉ (chuột và chế độ cửa hàng `` ` ``), 3 đan phù (phím 1/2/3) | Hình thật, VFX thật, âm, nhạc (M0b) |
| Bàn Quyết DOM, hợp đồng Cast, Chớp theo hồ sơ, khởi đầu lạnh (từ nền), Học trước, Thẻ Ôn, Sổ Từ, sự kiện học (nháp cho bot), sổ cái từ mới, dò IME, thẻ tốc độ | Voice, Hybrid (M4); đội online (M3) |
| Bench HN0 (ca nền + thú 3D instanced ở N = 60, 120, 300; "vạn kiếm" 150/300/500 kiếm; VFX; số; `SkinnedMesh` đi bộ), giảm chuyển động | Hồ sơ phản hồi `tutien` trong kit, nhân vật đi bộ trong kit (M0b, việc của repo cha) |
| Bản thử Tĩnh Tu (`tinh-tu.html`): Khẩu Quyết, phiên 60 s, Nhập Môn + Tham Ngộ, bot | Minh Tâm (sau MVP) |

## 1. Thứ tự và phụ thuộc

```text
Bước 0  Khung repo + kiểm nối repo cha + hợp đồng kiểu + mọi trường World (người dựng khung)   2 ngày
   │
   ├─▶ Làn 1  Mốc 1a: renderer, Projector, đám đông "procedural" (cho Làn 6) ─────▶ 2 ngày
   │          Mốc 1b: VAT, impostor, kiếm, VFX, walker-rig, bench, ma trận GPU ───▶ phán quyết canon §20.4   6–8 ngày
   ├─▶ Làn 2  Sim lõi + người chơi cục bộ ──┐
   ├─▶ Làn 8  Tĩnh Tu thử (độc lập) ────────┼──────────────────▶ cổng HC4–HC7, HC4b, HC6b   1–2 tuần
   │                                         ▼ khi `createWorld`, `step`, `emit` chạy (2–3 ngày)
   ├─▶ Làn 3  Bàn Quyết, gõ, học
   ├─▶ Làn 4  Kiếm, combat, trận pháp, cơ quan, kinh tế
   ├─▶ Làn 5  Thú, tinh anh, Thú Vương, báo trước
   ├─▶ Làn 6  View hộp xám, HUD, móc âm   (dùng renderer, đám đông, kiếm của Làn 1)
   └─▶ Làn 7  Bot, cân bằng, golden, kịch bản  (khung chạy bot từ ngày đầu, cổng ở cuối)
            ▼                                                                         1,5–2 tuần
Tích hợp (người dựng khung quay lại) → vòng cổng M0a → phản biện độc lập → sửa → chốt   3–5 ngày
```

- Làn 3–7 bắt đầu trên các stub có sẵn chữ ký của bước 0 (`TODO(<làn>)`), không chờ Làn 2 làm xong, chỉ chờ `createWorld`, `step`, `emit` chạy. Bước 0 khai sẵn **mọi trường trạng thái** của `World` theo canon §23.3 (thú, chữ, Cast, `ward`, nhãn, cơ quan, ví theo ghế, kho đan phù, Thế, báo đòn, `newWordAllowance`); mỗi làn chỉ viết hàm khởi tạo và băm của phần mình, không thêm trường vào `world.ts` của làn khác (PB-36).
- Làn 1 chỉ cần bước 0. **Mốc 1a** (2 ngày) giao `createRenderer`, `Projector`, `createCrowd(…, "procedural")` để Làn 6 dựng cảnh; **mốc 1b** (6–8 ngày) làm phần còn lại và chạy ma trận GPU (PB-36). **Phán quyết HN0 chặn việc hình của M0b**, không chặn lối chơi M0a. Tới khi có VAT, Làn 6 vẽ đám đông ở chế độ `procedural`.
- Làn 8 chỉ phụ thuộc kit, `src/typing/new-word-ledger.ts` của Làn 3 và `src/app/storage.ts` của bước 0 (chữ ký có từ bước 0).
- **Thứ tự sửa theo phản biện** (09 §11) đã xong ở canon và tệp này trước bước 0; phần còn lại là mã.
- Tổng: hộp xám chơi được sau 2–3 tuần (canon D02; tệp đánh giá §6). Giờ của anh: chỉ buổi chơi thử B9, sau khi Rồng Giữ Ải qua B9.

## 2. Bước 0: khung repo

### 2.1 Tệp trong `games/immortality-cultivation`

| Tệp | Chép từ | Đổi |
|---|---|---|
| `package.json` | `games/dragon-hold/package.json` | `name` `immortality-cultivation`; mô tả; cổng **3008** ở `dev`, `preview` (`--host 127.0.0.1 --port 3008 --strictPort`; cờ cổng **chỉ** đặt ở đây, repo cha gọi `pnpm dev` trơn, PB-22); lệnh `ic:balance`, `ic:golden:update`, `ic:calibrate`, `tt:bots`, `visual` (`node src/kit/tools/cdp-run.mjs`); phụ thuộc như Rồng (`three` **0.170.0** ghim, `@types/three` 0.170.0, `@fontsource/be-vietnam-pro`, `@fontsource/noto-sans`); `packageManager` `pnpm@11.21.0` |
| `pnpm-workspace.yaml`, `tsconfig.json`, `vitest.config.ts` | Rồng | Giữ nguyên |
| `kit.config.json` | Rồng | `{ "modules": ["platform", "input", "vocab", "learning", "speech", "audio", "ui", "tools", "typing", "three", "feedback", "balance"] }` |
| `vite.config.ts` | Rồng | Cổng 3008; `allowedHosts` mặc định `tutien.typing-game.local`; `serveSharedFolders` của kit; `manualChunks: { three: ["three"] }`; **nhiều trang**: `index.html`, `bench.html`, `tinh-tu.html` (`build.rollupOptions.input`); `server.watch.usePolling` khi `CHOKIDAR_USEPOLLING=1` (Vite trong WSL không thấy sửa từ Windows) |
| `index.html` | Rồng | `lang="vi"`; `#ic-app`, `#ic-canvas`, `#ic-overlay`, `#ic-quyet` (Bàn Quyết, **ngoài** canvas) |
| `bench.html`, `tinh-tu.html` | mới | Trỏ `src/view/bench/main.ts`, `src/tinh-tu/main.ts` |
| `.gitignore` | Rồng | Giữ nguyên khối chặn media (`public/assets/**`, `art-src/*`, `*.glb`, `*.png`, `*.wav`…), `tmp/` |
| `AGENTS.md` | Rồng | Cùng luật cứng (mục 11); trỏ canon và tệp này; bảng lệnh |
| `LANES.md` | mới | Bản tiếng Anh của mục 3–6 tệp này (đường dẫn sở hữu, hợp đồng, sự kiện, lệnh) |
| `docs/README.md`, `docs/SYNC_DEBT.md`, `docs/changelog/<ngày>-m0a-scaffold.md` | mới | Tiếng Việt |
| `src/main.ts` | mới | Trang "Đang dựng" tới khi tích hợp |
| `src/app/contracts.ts` | Rồng | `Presenter { onEvents, frame, dispose }`, `CommandSink`, `Projector`, `ActionHandler`, `Quality` |
| `src/app/storage.ts` | mới | Bọc kit `safe-storage` cho 4 khóa của canon §23.1 (`.save`, `.skill`, `.newwords`, `.settings`), mỗi khóa một hàm đọc, ghi, chuyển đổi; nơi duy nhất chạm `localStorage` |
| `src/content/types.ts`, `src/content/rules.ts` | mới (khung) | Theo **hợp đồng dữ liệu canon §23.3**: id, `SimCommand`, `SimEvent`, `Cast`, `BeastDef`, `SkillDef`, `WaveDef`, `TelegraphDef`, `Ward`, đầu replay (canon §23.2), **mọi trường của `World`**; mọi khóa số của canon (gồm `TT_TIERS`, `TT_BUDGETS`, `REF_OUTPUT`), mỗi khóa ghi `// canon §x`. Bàn giao cho Làn 2 |
| Stub mọi tệp của các làn | mới | Chữ ký xuất khẩu + `TODO(<làn>)` |
| `tests/boundary.test.ts` | Rồng | Nhóm thuần: `src/sim`, `src/local`, `src/typing`, `src/content`, `src/tinh-tu/sim` (không `Date`, `localStorage`, `window`…, kể cả qua chuỗi import tới `kit/platform/safe-storage`). **Thêm** (PB-20, canon D44): mọi tệp của game ngoài `src/kit/**` không import `kit/feedback/audio-cues` và `kit/audio/dragon-voice`, không có `OscillatorNode`, `createOscillator` |

Không chép `scripts/visual/cdp-run.mjs`: dùng `src/kit/tools/cdp-run.mjs` của kit (như Tuyến Cuối).

### 2.2 Kit

- Ở repo cha (WSL): `pnpm kit:sync --target games/immortality-cultivation`, rồi `node games/immortality-cultivation/src/kit/verify-kit.mjs` và `pnpm kit:check` (xanh cho cả 4 game).
- Repo cha commit trước, repo game commit `src/kit/` sau (bài học `parentDirty` của Rồng). Lỗi kit sửa ở `shared/game-kit` rồi sync lại; không ai sửa `src/kit/**`.
- **M0a không sửa `shared/game-kit`** (canon D44): hồ sơ phản hồi, nhân vật đi bộ, hợp đồng model để cục bộ trong game, ghi vào `SYNC_DEBT.md`; đưa lên kit ở M0b như một việc riêng của repo cha (chạy `kit:sync` lại cho mọi game và commit).

### 2.3 Nối repo cha: **đã có, chỉ kiểm** (PB-22)

Phần nối đã làm ở commit `6c44135b` của repo cha (25/10). Bước 0 **kiểm** từng dòng, không thêm lại:

| Tệp | Trạng thái |
|---|---|
| `.gitmodules` | Đã có `games/immortality-cultivation` (`branch = main`) |
| `portal/public/games.json` | Đã có mục `immortality-cultivation` (`appUrl` `https://tutien.typing-game.local`, `group` `battle`) |
| `portal/tests/learning-bridge.test.mjs` | Đã nhận `gameId` `immortality-cultivation`; origin sai bị từ chối (`SPLIT_PLAN.md` §9.2) |
| `infra/nginx/typing-game.local.dev.conf`, `.play.conf` | Đã có khối `tutien.typing-game.local` (dev proxy 3008 có HMR; play `root …/games/immortality-cultivation/dist`, alias `/vocabulary/`, `/typing-texts/`, `/assets/immortality-cultivation/`) |
| `scripts/setup-nginx.sh` | Đã có host trong `HOSTS`. **Anh chạy `pnpm setup:play` (sudo) và thêm host vào hosts của Windows**; agent không chạy |
| `package.json` cha | Đã có `dev:tutien`, `dev:tutien:app`, `build:tutien`, mục trong `dev` và `build:local` |
| `dev.sh`, `play.sh`, `scripts/play.sh`, `scripts/game-dir.sh`, `scripts/bootstrap.sh` | Đã có |
| `scripts/validate-play-mode.mjs`, `scripts/validate-space-integration.mjs` | Đã có mục game mới |
| `media/media.config.json` | Đã có mục `games[]` |
| `AGENTS.md` cha, `docs/AGENT_SKILLS_SETUP.md` | Đã có dòng game mới |

**Việc còn lại ở repo cha** (bước 0 làm, commit riêng ở repo cha trước khi commit repo game):

1. `scripts/media/test/unit.test.mjs` dòng 464: thêm `'immortality-cultivation'` vào danh sách id (đang **đỏ** vì `media.config.json` có 5 game); vòng lặp dòng 479 thêm id mới. Chạy lại `node --test scripts/media/test/unit.test.mjs`.
2. `docs/games/SPLIT_PLAN.md` §10: thêm 3008 vào dòng "Cổng đang dùng" và một mục ngắn "Game thứ tư: Tu Tiên Thủ Ải" (id, cổng 3008, host, nơi tài liệu `docs/games/tu-tien/`).
3. `package.json` cha, `dev:tutien:app`: bỏ `--host 127.0.0.1 --port 3008 --strictPort` cho giống `dev:dragon:app` (cờ chỉ ở `dev` của game; cờ lặp làm Vite nhận mảng cho `--port`).
4. `docs/games/tu-tien/README.md`: trạng thái "đang dựng M0a".

### 2.4 Nghiệm thu bước 0

- `pnpm --dir games/immortality-cultivation check` xanh (sha256 kit, test, build); test ranh giới xanh.
- `pnpm kit:check` ở repo cha xanh cho 4 game.
- `http://127.0.0.1:3008/` hiện "Đang dựng"; `bench.html`, `tinh-tu.html` mở được (khung trống); 0 lỗi console.
- Sau khi anh chạy `setup:play`: `https://tutien.typing-game.local` mở qua portal; một sự kiện học thử với `gameId` mới tới được portal.
- `node scripts/validate-play-mode.mjs` qua **không còn** cảnh báo "games/immortality-cultivation is not checked out yet"; `validate-space-integration.mjs` qua; `node --test scripts/media/test/unit.test.mjs` xanh (PB-22).
- Test ranh giới xanh, gồm luật cấm import âm tổng hợp của kit (mục 2.1).

## 3. Bố cục mã và quy ước

```text
src/
  main.ts        định tuyến trang (tích hợp)
  kit/           chép từ shared/game-kit, kiểm sha256, không sửa tay
  content/       types.ts, rules.ts, data/*.ts                       thuần, tất định
  sim/           thế giới chung, 60 Hz, số nguyên                    thuần, tất định
  local/         người chơi của máy này: vị trí, Sinh lực, khiên, gục, đi, đỡ `ward`, đan phù lên mình,
                 phát lệnh                                             thuần, tất định, có trong replay (`hashLocal`)
  typing/        bộ từ (khởi đầu lạnh), ô, độ dài, lùi khi thiếu từ, chấm, sổ cái từ mới (nhận `nowMs`)   thuần
  view/          three: renderer, đám đông, kiếm, VFX, walker-rig, hồ sơ phản hồi, cảnh hộp xám; bench/
  ui/            DOM: Bàn Quyết, HUD, khung học, thẻ, cửa hàng (chuột, chế độ phím), Thu Hoạch
  audio/         móc âm im lặng
  app/           vòng khung, định tuyến phím, học, lưu (`storage.ts` là nơi duy nhất chạm localStorage), tốc độ gõ
  tinh-tu/       bản thử Tĩnh Tu (sim/ thuần, ui/, main.ts)
scripts/  balance/  tinh-tu/  models/blender/  visual/scenarios/
tests/    boundary  app/  content/  sim/  local/  typing/  ui/  view/  audio/  golden/  tinh-tu/
```

### 3.1 Quy ước (nguồn: Rồng `LANES.md` "Units and conventions")

- Tick 60 Hz. **Dữ liệu** (`rules.ts`, `data/*.ts`): ms (`…Ms`), mm (`…Mm`), phần trăm (`…Pct`), phần nghìn (`…Pm`), W × 100 (`w100`). **Trạng thái** (canon §7.1, D38): tick, u, phần nghìn, **máu nguyên**; `w100` chỉ ở dữ liệu, đổi sang máu lúc nạp. Không lưu số thực trong trạng thái có băm.
- Không gian sim: u, 1 m = 60.000 u (canon ghi mm ở dữ liệu; `origin` lượng tử 100 mm = 6.000 u). x đông, z nam, y lên; **Trận Tâm ở gốc**; cổng A, B ở (∓15 m; −18 m), đường trời từ (±20 m; −18 m) (canon §8.1); camera nhìn về bắc từ phía nam.
- Sát thương: thứ tự và làm tròn nửa lên theo canon §7.2 (`mulDiv` mỗi bước); sổ phần cộng sát thương hiệu dụng.
- Ngẫu nhiên chỉ từ `world.rng.<luồng>`: `spawn`, `combat`, `words`, `ai`, `loot`, `props`. **Không có luồng `crit`** (canon D09).
- `src/sim`, `src/local`, `src/typing`, `src/content`, `src/tinh-tu/sim`: không `three`, `window`, `document`, `Date`, `performance`, `localStorage`, `Math.random`, lượng giác, `pow`, `hypot`, `**`. Hướng dùng bảng tra; độ dài dùng `isqrt`. Giờ tường (sổ cái từ mới) do người gọi đưa vào (`nowMs`). Test ranh giới giữ luật này.
- `hashWorld` đi cả thế giới trừ `HASH_SKIP` (cấu hình tĩnh, `wall`, sự kiện); `hashLocal` đi cả lớp `local`. Tạo object với trường theo thứ tự cố định. Replay ghi cả hai mỗi 600 tick và cuối trận (canon §23.2).
- Số luật chỉ đọc từ `src/content/rules.ts`, không viết số trong hệ.
- `SimEvent` là kênh duy nhất từ sim ra ngoài. Làn cần sự kiện mới ghi `// WANT EVENT: …` trong tệp của mình và báo lại.
- Làn cần đổi kiểu dùng chung thì khai kiểu mới **trong tệp của mình**, dùng ở đó, rồi báo; Làn 2 gộp vào `types.ts`. Không sửa tệp của làn khác.
- Tệp chép: một dòng `// Source: games/<repo>/<đường dẫn> @<commit> (adapted: …)`, liệt kê trong `docs/SYNC_DEBT.md`.
- Chú thích mã tiếng Anh, ngắn. Tài liệu và changelog tiếng Việt có dấu; mỗi làn một tệp `docs/changelog/<ngày>-m0a-<làn>.md`.

### 3.2 Bước của thế giới (thứ tự cố định)

```text
lệnh → stepWords → stepWaves → stepSpawn → stepDirector → stepBeasts → stepCasts → stepSkills
     → stepWards → stepConsumables → stepAutoHits → stepMechanisms → stepBeastAttacks → stepBoss
     → stepPosture → stepFormation → stepEconomy
     → dọn (mỗi thú chết: words.onBeastGone, combat.onBeastKilled, economy.onBeastKilled,
       waves.onBeastGone; rồi kiểm hết đợt, thua) → tick + 1
```

- Lớp `local` chạy trước mỗi tick thế giới: đầu vào đi, di chuyển, đọc đòn đã chạm của tick trước để trừ Sinh lực, khiên của mình (đỡ bằng `ward` khi đứng trong vòng, phát `ward-use`), áp tác dụng đan phù lên mình khi có sự kiện `consumable` của ghế mình, gục, phát lệnh `auto`; lệnh đi vào tick kế với `origin`. Replay ghi cả đầu vào cục bộ (`move-to`, `arrows`) và lệnh. Bảng tách quyền: canon §9.1 (D34).
- Dừng hình chỉ làm chậm thế giới, không bao giờ làm chậm phím.

### 3.3 Lệnh (`SimCommand`)

`key{seat, letter 0–25, ms, origin, aim}` (`ms` đồng hồ tường chỉ cho học, không vào băm; `aim` là điểm con trỏ trên đất cho chiêu đặt đất) · `backspace` · `release` · `soft-target{beast}` · `auto{seat, beast, origin}` · `down{seat, origin}` · `ward-use{seat, wardId}` · `consumable{seat, slot, origin, aim}` · `buy` · `place{slot, mech}` · `upgrade` · `sell` · `loadout{guard | dash, tamPhap}` · `start` · `continue` · `learn-ahead` · `review-card` · `pace-update{seat, kPm}` (trận đầu hồ sơ "chưa biết", sau đợt 1; canon §6.5).

Phím chữ chỉ thành lệnh `key` khi **Bàn Quyết sống** (từ báo đợt tới hết đợt, pha Vương; canon §6.1, D42); lúc bày trận, nghỉ, gục thì vào bảng đang mở hoặc bị bỏ.

Đầu vào chỉ của lớp `local` (ghi vào replay, không vào thế giới): `move-to{point}`, `arrows{mask}`.

### 3.4 Sự kiện (`SimEvent`, app rút một lần mỗi khung)

| Sự kiện | Phát bởi | Đọc bởi |
|---|---|---|
| `phase`, `wave-start`, `wave-end`, `victory`, `defeat` | waves, world | ui (thẻ đợt, Thu Hoạch), móc âm |
| `spawn`, `death` (cờ cụm, bậc phản hồi) | spawn, dọn | view đám đông, fx, Bàn Quyết (Ấn) |
| `hit` (lượng, loại, bucket, chất lượng, bậc T0–T5) | combat | fx, số sát thương, móc âm |
| `cast` (`held`, `resolved`, `fizzled`; ô, `actionId`, `wordId`, `origin`) | cast | Bàn Quyết, fx, `local` (lướt) |
| `skill-fx` (bắn băng, tuyến, vùng mở/đóng, loạt tuyệt kỹ) | skills | view kiếm, fx |
| `telegraph` (`start`, `strike`, `cancel`; hình, đáp án, số tick) | telegraph | view báo đòn, `local` (trúng vùng), HUD |
| `posture` (`change`, `break`, `recover`) | posture | thanh Thế, fx |
| `formation` (Trận Lực, nhãn tắt/sáng, Linh Dịch) · `pillar` (`hit`, `crack`) | formation | HUD, view |
| `mechanism` (`trigger`, `built`, `upgraded`, `sold`) | mechanisms | view, cửa hàng, HUD |
| `consumable{seat, kind}` | consumables (sim) | `local/consumables.ts` (tác dụng lên mình), view, HUD |
| `ward` (`start`, `block`, `end`; `wardId`, `origin`, còn lần) | wards | `local` (đỡ cho mình), view |
| `linh-sa` | economy | HUD, hạt nhặt |
| `word-assigned`, `word-progress`, `word-complete`, `word-released`, `grade`, `word-first-seen` (từ mới gặp lần đầu, để app gọi `take` của sổ cái) | words | Bàn Quyết, khung học, `app/learning` |
| `pace` · `pace-update` | director · pace | gỡ lỗi, báo cáo, Bàn Quyết |
| `rejected` | mọi xử lý lệnh | ui (báo nhẹ) |
| `player-hit`, `player-down`, `player-up` (của `local`) | local | HUD, view người chơi |

- Vị trí thú: view đọc thẳng `world.beasts` mỗi khung, không qua sự kiện (luật 60 thú ở M0a; đường này phải chịu được 300 như bench).

## 4. Làn và đường dẫn sở hữu

Mỗi làn chỉ ghi vào đường dẫn của mình. Không ai sửa `src/kit/**`.

| Làn | Sở hữu |
|---|---|
| **Bước 0 / Tích hợp** | Khung repo (mục 2.1); sau đó `src/main.ts`, `src/app/{app,loop,input-router,contracts,save,storage}.ts`, `tests/app/save-migrate.test.ts`, `vite.config.ts`, `index.html`, `bench.html`, `tinh-tu.html`, `AGENTS.md`, `LANES.md`, `docs/README.md`; việc còn lại ở repo cha (mục 2.3) |
| **1 Bench 3D (HN0)** | `src/view/{renderer,crowd,vat,impostor,swords,trails,hitfx,walker-rig}.ts`, `src/view/bench/**`, `src/content/model-contracts.ts`, `scripts/visual/scenarios/ic-bench.mjs` (tự chứa, không import `lib/**`), `scripts/models/**`, `tests/view/{renderer,crowd,vat,impostor,swords,hitfx,walker-rig}*.test.ts`; bảng phán quyết canon §20.4 |
| **2 Sim lõi + người chơi cục bộ** | `src/content/{types,rules}.ts` (từ sau bước 0), `src/content/data/{stage-m0a,waves}.ts`, `src/sim/{fixed,hash,events,world,waves,spawn,director,pace,field}.ts`, `src/local/**` (gồm `local/consumables.ts`, `local/zones.ts`), `tests/content/**`, `tests/sim/core-*.test.ts`, `tests/local/**`, `docs/SYNC_DEBT.md` |
| **3 Bàn Quyết, gõ, học** | `src/typing/**` (gồm `new-word-ledger.ts`, `deck.ts`, `slots.ts`, `fallback.ts`), `src/sim/{words,cast}.ts`, `src/ui/{ban-quyet,learning-frame,ime-banner,learn-ahead,review-card,word-book}.ts`, `src/app/{learning,typing-pace,pace-card}.ts`, `tests/typing/**`, `tests/ui/{ban-quyet,learning}*.test.ts` |
| **4 Kiếm, combat, trận pháp, cơ quan, kinh tế** | `src/sim/{combat,shares,skills,wards,chan-nguyen,formation,mechanisms,economy,shop,consumables}.ts`, `src/content/data/{school-kiem,mechanisms,consumables,economy}.ts`, `tests/sim/{combat,combat-kill-invariants,skills,wards,formation,mechanisms,economy,shop,consumables}*.test.ts` |
| **5 Thú, tinh anh, Thú Vương, báo trước** | `src/sim/{beasts,targeting,elites,posture,telegraph,boss,pressure}.ts`, `src/content/data/{beasts,elites,boss,telegraphs}.ts`, `tests/sim/{beasts,targeting,elites,posture,telegraph,telegraph-floor,boss,pressure}*.test.ts` |
| **6 View hộp xám, HUD, móc âm** | `src/view/{stage,ground,actors,player-view,telegraphs,fx,pickups,feedback-profile}.ts`, `src/ui/{hud,wave-card,shop-strip,shop-mode,results,menu,skin,screen-zones}.ts`, `src/ui/styles/**`, `src/audio/**`, `tests/ui/{hud,wave-card,shop,results,menu,screen-zones}*.test.ts`, `tests/view/{stage,actors,telegraphs,fx}*.test.ts`, `tests/audio/**` |
| **7 Bot, cân bằng, golden, kịch bản** | `scripts/balance/**`, `tests/golden/**`, `tests/sim/bot-*.test.ts`, `scripts/visual/scenarios/ic-*.mjs` trừ `ic-bench.mjs` (gồm `ic-hitstop-keys.mjs`), `scripts/visual/scenarios/lib/**` |
| **8 Tĩnh Tu thử** | `src/tinh-tu/**`, `tests/tinh-tu/**`, `scripts/tinh-tu/**`, `scripts/visual/scenarios/tt-*.mjs` |

## 5. Hợp đồng giữa các làn

| Gọi | Chủ | Ai gọi |
|---|---|---|
| `createWorld(stage, seed, header)`, `step(world, cmds)`, `applyCommand`, `hashWorld`, `hashLocal(local)`, `runLog(header, log, untilTick)` (dựng cả `world` và `local` từ đầu replay canon §23.2), `emit(world, event)`, `allocBeast`, `beastAt({slot, serial})` | 2 `world.ts`, `events.ts` | mọi làn, bot |
| `scheduleWave`, `spawnGroup`, `liveCount`, `liveRoom`, `onBeastGone`, `isWaveOver` (mọi toán đã sinh và 0 thú sống, canon §4.1) | 2 `waves.ts`, `spawn.ts` | 5 (Tru Đàn, Gọi Đàn: chỉ gọi khi `liveRoom` đủ), dọn |
| `fieldStep(world, beast)`, `fieldDistance(gate, cell)` | 2 `field.ts` | 5 (di chuyển, "gần Trận Tâm nhất"), 7 (đo quãng Q) |
| `paceFor(profile)`, `kForSeat(world, seat)`, `scaleTicks`, `applyPaceUpdate` | 2 `pace.ts` (kit `paceK`, `effectiveE`) | 5 (nạp đòn), 2 (khoảng sinh), 4 (Chân Nguyên, Dưỡng × 1/k) |
| `createLocal(seat)`, `stepLocal(local, world, input)`, `drainLocalCommands(local)`, `playerPos(local)` | 2 `local/**` | tích hợp, 6, 7 |
| `dealSlotWord(world, seat, slot)`, `dealSeal(world, seat, beast)`, `dealCleanse(world, seat, node)`, `releaseWord(world, slot, reason)` (theo luật chữ và thứ tự lùi canon §6.2) | 3 `words.ts` | 4 (ô hồi xong), 5 (tinh anh, Vương), 4 (chiếm nhãn) |
| `emitCast(world, cast)` → `resolveCast(world, cast)` | 3 `cast.ts` → 4 `skills.ts` | 3 |
| `createNewWordLedger(snapshot)`: `remaining(nowMs)`, `take(wordId, nowMs, channel)` (thuần) | 3 `typing/new-word-ledger.ts` | tích hợp (`storage.ts` đọc, ghi), 3, 8 |
| `buildDeck(records, level, allowance, rng)` (khởi đầu lạnh, sàn 40 từ; canon §17.1) | 3 `typing/deck.ts` | tích hợp (lúc nạp trận), 7 |
| `damageBeast(world, beast, amount, type, source, by)` (máu nguyên, thứ tự canon §7.2) | 4 `combat.ts` | 4, 5 (Thạch Bích sau này), cơ quan, đan phù |
| `damageFormation(world, amount, source)`, `inBarrier(x, z)`, `nodeState(world)`, `occupyNode`, `pillarOnSegment(world, a, b)`, `hitPillar` | 4 `formation.ts` | 5 |
| `wardAt(world, seat)` → `{ wardId, origin, radius, charges }` hoặc rỗng; `wardCrosses(world, seat, a, b)` | 4 `wards.ts` | 5 (đỡ một nửa Thiết Bối Xung, đỡ cho bot, nhãn), `local` (đỡ cho mình) |
| `addChanNguyen(world, seat, grade, isSeal)` (chỉ Cast `resolved`, × 1/k) | 4 `chan-nguyen.ts` | 3 |
| `earn`, `spend`, `payWaveEnd`, `payLearning`, `payKill` (ĐĐ, canon §14.2) | 4 `economy.ts` | 2 (hết đợt), 3 (Học trước, Thẻ Ôn), 4 |
| `bucketAdd(world, bucket, amount)`, `shares(world)` | 4 `shares.ts` | 4, 7 |
| `chooseTarget(world, beast)` (chỉ đích hợp lệ của canon §10.1) | 5 `targeting.ts` | 5 |
| `postureHit(world, beast, delta, source)`, `isBroken(beast)` | 5 `posture.ts` | 3 (Ấn), 4 (chiêu), cơ quan |
| `telegraph(world, def)`, `chargeTicks(def, preset, k)` (kẹp `max(T, nạp / k)`), `T(preset, ℓ, tKênh)` | 5 `telegraph.ts` | 5, Làn 7 (`ic-telegraphs`), CB5 |
| `createRenderer(host, quality)`, `Projector`, `createCrowd(renderer, mode)`, `createSwords(pool)`, `createHitFx`, `createDamageNumbers`, `createInkSmoke`, `createWalker(rig)` | 1 `view/**` | 6 |
| `Presenter { onEvents(events, world); frame(world, info); dispose() }` | bước 0 `contracts.ts` | 1, 3, 6 |
| `loadKey`, `saveKey`, `migrate` cho `.save`, `.skill`, `.newwords`, `.settings` | bước 0 `app/storage.ts` | tích hợp, 3, 8 |

- **Cast:** chữ cuối đúng trong `words.ts` → `emitCast` (một lần cho mỗi `wordId`, `actionId` riêng ghế) → `resolveCast` của Làn 4 tìm đích. Không có đích: trạng thái `held` 3 s, không tốn hồi; hết giờ `fizzled`, ô nhận từ kế (canon §6.1). Chân Nguyên, Dưỡng, điểm luyện chỉ cho `resolved`.
- **Chiêu đất:** điểm đặt là `aim` của lệnh phím cuối; không có `aim` trên sân thì Làn 4 chọn cụm đông nhất trong tầm (hòa: canon §23.3).
- **Hộ thân:** Làn 4 tạo `ward` khi Cast ô 3 `resolved` (canon §9.1); Làn 5 hỏi `wardCrosses` ở tick chạm của Thiết Bối Xung và đòn vào bot, nhãn; `local` (Làn 2) đọc `ward` từ thế giới và phát `ward-use` khi tự đỡ.
- **Đan phù:** Làn 4 kiểm số, hồi chung, Linh Sa, phát `consumable{seat, kind}` và áp tác dụng lên thế giới; Làn 2 (`local/consumables.ts`) áp tác dụng lên mình.

## 6. Từng làn

### 6.1 Làn 1 — Bench 3D (HN0), làm đầu tiên

**Mốc 1a (2 ngày, giao cho Làn 6 trước; PB-36)**
1. `renderer.ts`: `Stage3D` của kit với bảng `TT_TIERS` đủ 4 khóa `low | medium | high | ultra` (ultra = high ở MVP; kiểu `StageTier`: DPR, hạt, bloom, `tipsPerSide`, `trail`); số kiếm, tam giác LOD, trần draw call, ngân sách con đọc từ `TT_BUDGETS` của `rules.ts` (canon §20.2); đặt `stage.renderer.toneMapping = THREE.NeutralToneMapping` **sau khi dựng** (kit cố định ACES; PB-35); camera 3/4 cố định theo canon §21.1 (nghiêng 50–55°, FOV 25–30°, khung đủ 40 × 26 m ở 16:9); `Projector`; đọc `renderer.info` (draw call **gồm** lượt hậu kỳ, tam giác); dọn tài nguyên khi hủy.
2. `crowd.ts` (Source: `games/dragon-hold/src/view/crowd.ts`, adapted): một `InstancedMesh` mỗi loài mỗi kiểu vẽ; kiểu `procedural` (có sẵn) giao ở mốc 1a; API giữ như Rồng (`add`, `remove`, `set`, `update`); thuộc tính mỗi instance: clip, thời điểm clip, lóe, nén, tan, tint, cỡ; bóng blob; viền mực vỏ lật bật được. Khe `bones` giữ kiểu, không làm (canon §20.3).

**Mốc 1b (6–8 ngày)**
3. `crowd.ts` thêm kiểu **`vat`** và **`impostor`**; đổi kiểu một thú giữa VAT và impostor có trễ 1 s và trộn 0,2 s (canon §20.3).
4. `vat.ts`: định dạng VAT (vị trí + pháp tuyến RGBA16F; **texel = `khung × số đỉnh + đỉnh`, quấn dòng trong kết cấu rộng 1.024 hoặc 2.048**, PB-34; bảng clip); đoạn shader đọc 2 khung và nội suy, trộn 2 clip trong 0,15 s; nạp tệp nướng (`.vat.bin` + JSON, trong `public/assets/`, không vào Git); **bộ nướng trong trang** cho khối tạm: chia lưới khối tới đúng số tam giác của bậc (≤ 1.000 / 1.800 / 3.000), nướng biến dạng dáng đi thủ tục thành VAT.
5. `impostor.ts`: atlas **16 hướng × 8 pha** (ô 192 px ở High, 128 px ở Low), trộn mờ hai pha kề; bộ nướng trong trang bằng render-to-texture cho khối tạm; nạp kết quả `bake_impostor.py`; shader quad instanced chọn ô theo góc nhìn và pha.
6. `swords.ts`, `trails.ts`: cảnh "vạn kiếm" (canon §12.1, §20.3): kiếm sinh sau lưng người tung, bay theo cung, 3 loạt hội về vùng đích, thu gọn; thân kiếm là `InstancedMesh` khối tạm ít tam giác; vệt là dải instanced đọc vị trí cũ từ một `DataTexture` vòng (1 draw call); quầng sáng là quad cộng sáng instanced (1 draw call); **một bể kiếm chung** theo bậc 150 / 300 / 500 (đồng đội lấy từ bể, canon §20.2); không cấp phát mỗi khung.
7. `hitfx.ts`: tia trúng (quad instanced kiểu `Glows` của Tuyến Cuối hoặc `ParticlePool` của kit); **`createDamageNumbers`** bằng `NumberField` của kit qua lớp bọc có sửa hộp vẽ của Rồng (Source: `games/dragon-hold/src/view/number-field.ts`; gộp số nhỏ mỗi mục tiêu mỗi 0,25 s); **`createInkSmoke`** khói mực tạm khi chết. Số sát thương và khói mực **chỉ ở làn này**; Làn 6 chỉ nối (PB-36).
8. `walker-rig.ts` (Source: `kit/three/hero.ts`, chỉ lấy trộn clip và ổ cắm; locomotion `idle | run | dash`, không độ chúi bay) và `src/content/model-contracts.ts` (`cultivators`, `beasts`, `beast-kings`; `props` dùng của kit) theo canon §21.2 (D44, PB-21). Khối tạm có xương cho ca E: người 15.000 tam giác, Vương 45.000; ghi số xương.
9. `bench/{main,cases,meter}.ts`: ca **0, A–E** của canon §20.3; ca B, C, D, E nhận `COUNT` ∈ {60, 120, 300}; ca E dùng số `SkinnedMesh` bằng trần của bậc (Low, Medium 6; High 8; thêm lượt High 10). Bộ đo: khoảng rAF, thời gian CPU quanh cập nhật + vẽ, `renderer.info`, bộ nhớ kết cấu ước, `performance.memory.usedJSHeapSize`, chuỗi `renderer` qua `WEBGL_debug_renderer_info`, giá trị `prefers-reduced-motion`; kết quả ở `window.__icBench`; `__icBenchStop`, `__icBenchCamera`. Trang đặt `?motion=full` khi đo.
10. `ic-bench.mjs` (Source: `games/dragon-hold/scripts/visual/scenarios/dh-bench.mjs`, adapted; **tự chứa, không import `scripts/visual/scenarios/lib/**`** của Làn 7): biến môi trường `Q`, `CASE` (`base`, `crowd-proc`, `crowd-vat`, `vankiem`, `impostor`, `skinned`), `COUNT` (60, 120, 300), `SWORDS`, `SKINNED`, `SECONDS` (10), `WARMUP` (2), `RUNS` (3), `SHOTS`; ghi JSON và ảnh vào `tmp/shots/bench/`; đánh dấu lượt **không hợp lệ** khi chuỗi `renderer` là SwiftShader, llvmpipe hay vẽ phần mềm; tính **hiệu từng phần** (nền, đám đông, kiếm và VFX, có xương) theo canon §20.3 và in cột "phần vượt".
11. `scripts/models/blender/bake_vat.py` (mới; khung theo `bake_impostor.py` của Space): GLB có xương, danh sách clip, fps, `--lod-tris`, `--width 1024|2048` → `.vat.bin` + JSON. `scripts/models/blender/bake_impostor.py`: chép (Source: `games/space-typing/scripts/models/blender/bake_impostor.py`), thêm tham số 8 pha. Chạy bằng Blender Linux trong WSL (`~/.local/blender/blender-5.2.3-linux-x64/blender -b --factory-startup -P …`).
12. Chạy ma trận trên Dell (mục 9): ca 0 và A một lần mỗi bậc; B, C, D, E × N 60/120/300; × Low, Medium, High × 3 lượt. Nếu trên máy có sẵn một GLB có xương của anh (ví dụ Draconis v3 medium trong media của Rồng), chạy thêm lượt xác nhận B, C bằng VAT nướng từ GLB đó (không commit tệp nướng). **Phán quyết theo N của luật** (60; và 120 cho đề xuất M1): bậc đạt ở ca E thì 3D đầy đủ, **không lùi gì**; bậc trượt thì lùi **theo phần vượt** (canon §20.3, D36), đo lại sau mỗi nấc. Ghi phán quyết vào canon §20.4 (cột "N đạt 3D đầy đủ", "phần vượt") và `docs/changelog/<ngày>-m0a-hn0-bench.md` (bảng số, chuỗi `renderer`, ảnh đã xem). Lượt Apple M4 chạy khi có máy Mac.

**Nghiệm thu**
- Mốc 1a: Làn 6 dựng được cảnh hộp xám trên `createRenderer` và `createCrowd(…, "procedural")`; `pnpm test` xanh.
- `pnpm test` xanh: chỉ số texel VAT (`khung × số đỉnh + đỉnh`, quấn dòng, không vượt 2.048 ở mesh 3.000 tam giác), nội suy khung, trọng số trộn clip, chọn ô impostor đúng 16 hướng × 8 pha (hướng 0 là chính diện), pool kiếm không tạo object sau khởi động, bảng bậc khớp canon §20.2 (`TT_TIERS` đủ 4 khóa; số kiếm, tam giác LOD, trần draw call, ngân sách con trong `TT_BUDGETS`), `walker-rig` trộn idle/run/dash.
- Bench chạy đủ ma trận trên GPU thật của Dell; JSON đủ trường (gồm hiệu từng phần); 0 lỗi console; ảnh đã xem (đám đông đọc được ở cả 3 kiểu vẽ).
- Không cấp phát mỗi khung: `performance.memory.usedJSHeapSize` tăng ≤ 2 MB trong 10 s đo (Chrome chạy với `--enable-precise-memory-info`, mục 9; PB-35).
- Phán quyết, N đạt 3D đầy đủ, phần vượt và nấc lùi (nếu có) đã ghi ở canon §20.4.

### 6.2 Làn 2 — Sim lõi và người chơi cục bộ

**Việc**
1. Chép (thường là "viết lại có tham chiếu", vì sim của Rồng đi theo làn còn game này đi theo trường hướng và có lớp `local`) từ Rồng Giữ Ải, mỗi tệp có `// Source: … @<commit>`: `fixed.ts`, `hash.ts` (`hashWorld`, `hashLocal`), `events.ts`, `world.ts` (thứ tự bước mục 3.2, `HASH_SKIP`; trường của `World` đã khai ở bước 0), `waves.ts` (pha: bày trận 20 s, báo 5 s, đợt, nghỉ theo preset (Đại Triều 15 s ở Cân bằng), lặng 8 s, Vương; **hết đợt khi mọi toán đã sinh và 0 thú sống**, lặng trước Vương bắt đầu khi đợt cuối sinh hết toán, canon §4.1; phân tích kế hoạch đợt), `spawn.ts` (toán, luật cổng 1,5 s / 0,6 s chỉ giãn, **trần thú sống 60** với toán chờ ở cổng, đồng hồ đợt không dừng; `liveRoom` cho triệu hồi), `director.ts` (nối `PaceDirector` của kit, bậc của canon §13.2, Linh Dịch).
2. `pace.ts`: k theo ghế (`paceK`, `effectiveE` của kit), kẹp 0,75–1,30; k chỉ đổi thời gian; `applyPaceUpdate` cho lệnh `pace-update` sau đợt 1 ở trận đầu của hồ sơ "chưa biết" (canon §6.5).
3. `field.ts` (mới): trường hướng mỗi cổng trên lưới 0,5 m (80 × 52 ô) về Trận Tâm, tránh Trận Trụ; BFS số nguyên; đường trời là tuyến thẳng có điểm bổ nhào; tính lại chỉ khi vật cản đổi.
4. `data/stage-m0a.ts` theo tọa độ canon §8.1 (Trận Tâm ở gốc; cổng A, B ở (∓15 m; −18 m); đường trời từ (±20 m; −18 m); Trận Trụ, 6 ô cơ quan, Tâm nhãn, khung camera) và `data/waves.ts` (bảng canon §13.3 theo hình dạng `WaveDef` của canon §23.3, gồm `summonMaxW`; máu đợt `L × D_ref × phút` **gồm W gọi tối đa**, đọc `REF_OUTPUT` của `rules.ts`; lọc giải tích tính cả phần gọi).
5. `src/local/**`: `player.ts` (vị trí u, Sinh lực 600 × g(K), khiên, tốc 5 m/s, va chạm địa hình và Trận Trụ, **không va chạm thú**), `nav.ts` (Source: `games/typing-defense/src/sim/nav/{grid,astar,connectivity}.ts`), `input.ts` (`move-to`, `arrows`; mũi tên không đi khi chế độ cửa hàng mở), `zones.ts` (đọc `telegraph strike` của thế giới, trừ Sinh lực, khiên của mình nếu đứng trong vùng; **đỡ bằng `ward`** khi đứng trong vòng và `ward` còn lần, rồi phát `ward-use`; Kết Giới −10 % với đệm 1,5 s và phai 3 s), `consumables.ts` (**tác dụng lên mình** khi có `consumable{seat, kind}` của ghế mình: Hồi Xuân Đan, Kim Thân Phù; canon §12.3), `down.ts` (gục 8 s, dậy ở Trận Tâm, phát `down`; lúc gục không đánh nền, không đan phù), `auto.ts` (phát `auto` theo nhịp trường phái: mục tiêu mềm, không thì thú gần Trận Tâm nhất trong tầm; chỉ đọc thế giới), `dash.ts` (áp Lưu Quang Bộ khi `cast resolved` của chính mình).
6. Replay: `runLog(header, log, untilTick)` dựng `world` và `local` từ đầu replay canon §23.2 (seed, `rulesHash`, preset, ghế và `kPm`, bộ từ, `newWordAllowance`, loadout); thân gồm lệnh và đầu vào cục bộ; đuôi `hashWorld`, `hashLocal` mỗi 600 tick.
7. `docs/SYNC_DEBT.md` (mục 10).

**Nghiệm thu**
- Tất định: hai lượt cùng đầu replay, cùng nhật ký ra cùng `hashWorld` **và** `hashLocal`, qua cả ải M0a; không số thực trong trạng thái có băm.
- Test ranh giới xanh.
- Một bước sim ≤ 0,3 ms ở 300 thú (headless); cả trận ≥ 200 lần thời gian thực.
- Trần thú sống 60 giữ ở mọi tick; luật cổng không dưới 1,5 s / 0,6 s; đợt chỉ hết khi mọi toán đã sinh và 0 thú sống.
- **Thời gian tới mép Kết Giới theo từng loài** ở k = 1, Cân bằng (test, PB-08): Phong Lang và Hỏa Nha 8–12 s (10,7 s; 9,0 s); Thạch Thử 8–12 s; Phong Lang Cuồng, trong hào quang tướng, hoặc cả hai: ≥ 6 s (ngoại lệ có chủ ý, canon §8.1).
- Đổi k chỉ đổi thời gian: máu, thành phần, danh sách toán giữ nguyên (test); `pace-update` chỉ đổi thời gian từ đợt 2.
- `local`: chuột phải tránh Trận Trụ; mũi tên; đi xuyên thú; chỉ mất Sinh lực khi đứng trong vùng đúng tick chạm; đứng trong `ward` thì đỡ và phát `ward-use`; Hồi Xuân Đan, Kim Thân Phù áp lên mình khi nhận sự kiện; Sinh lực 0 → lệnh `down` → Trận Lực −5 %.

### 6.3 Làn 3 — Bàn Quyết, gõ, học

**Việc**
1. `typing/deck.ts` (Source: `games/dragon-hold/src/typing/deck.ts`, **có sửa cố ý**, canon §17.1, D35, PB-02): bộ từ trận 70–100 từ qua `kit/vocab` và truy vấn `query`/`lookup` của lõi học; lọc `sensitive` (và `mature` cho hồ sơ trẻ em); loại từ (đã thuộc, đang học, đến hạn, mới, yếu) theo **bản ghi học**. **Bỏ** nhánh hồ sơ trống gắn "known" cho 50 từ đầu (dòng 89–92 của Rồng) và nhánh lấp chỗ `candidate.isNew ? "learning"` (dòng 101–105). **Khởi đầu lạnh:** ≤ 40 từ nền (cấp thấp hơn một bậc, cờ `assumed: true`) + từ mới trong `newWordAllowance`; nhóm thiếu thì **thu nhỏ bộ từ** (sàn 40), không đổi nhãn. Ghi chỗ khác Rồng vào `SYNC_DEBT.md`.
2. `typing/slots.ts`: loại từ và dải độ dài mỗi ô theo canon §6.3, theo E và preset (Ấn ở Học = Thư giãn 3–5); ô gấp không bao giờ nhận từ mới; ô 4 nhận từ mới chỉ ở đợt 1–2; ô 2 chỉ nhận từ mới của trận ở lần gặp thứ hai trở đi; từ nền dùng thẳng ở ô 1, ô 3, Tẩy.
3. `typing/fallback.ts`: trần chữ sống = min(trần preset; A − 3) với `BudgetLedger` của kit; thứ tự lùi khi không có từ thỏa luật (nới độ dài ±1 → nới loại về phía quen hơn, từ nền tính là đã thuộc → ô chờ mờ, ghi "nghẽn"); **không bao giờ lấy từ mới để lấp** (canon §6.2, PB-26).
4. `typing/new-word-ledger.ts` (canon §6.4, D39, PB-10): `NewWordLedger` **thuần**, `createNewWordLedger(snapshot)`, `remaining(nowMs)`, `take(wordId, nowMs, channel)`; cửa sổ trượt 20 phút theo `firstSeenMs`; một từ tính một lần mọi kênh. Không đọc đồng hồ, không lưu: `src/app/storage.ts` (bước 0) đọc, ghi khóa `.newwords`. Lúc nạp trận app chụp `remaining` thành `newWordAllowance` vào đầu replay (`min(remaining; 4)` khi > 80 từ đến hạn).
5. **Gặp lại từ mới** (canon §6.4, PB-11): `WordPicker` ưu tiên trả từ mới của trận cho ô 2, ô 4 tới khi mỗi từ gặp ≥ 3 lần (≥ 45 s giữa hai lần, xong trước đợt 4).
6. `typing/grading.ts` (Source: Rồng `src/typing/grading.ts`): bảng chất lượng; Chớp theo hồ sơ (`t_kỳ_vọng` từ `SkillProfile`, sàn theo 5 phiên); **trần đổi 10 % mỗi phiên chỉ chiều giảm và chỉ khi độ tin ≥ 60 từ qua ≥ 3 phiên**, còn lại `blendSkill` không trần (canon §6.5, D41).
7. `sim/words.ts`: trên `kit/typing/session` — chữ đầu bậc 1, luật tiền tố và khoảng sửa, trần chữ sống và thứ tự ưu tiên theo preset (Học: ô 4 trước ô 5), không đổi từ khi đang gõ dở, chữ nghỉ 1 s, Esc giữ số phím sai (`unlockErrors: "keep"`), ân hạn khóa; **Bàn Quyết chỉ sống từ báo đợt tới hết đợt và pha Vương** (D42); cấp từ ô, Ấn (`dealSeal`), Tẩy (`dealCleanse`); nhả từ khi thú chết và khi gục; phát `word-first-seen` cho từ mới.
8. `sim/cast.ts`: giao dịch Cast (canon §6.1); `held` 3 s, `resolved`, `fizzled`; gọi `addChanNguyen` **chỉ** cho `resolved`.
9. UI: `ban-quyet.ts` (dải DOM ngoài canvas: 5 ô + 3 ô đan phù chỉ hiện số đếm và hồi; từ 28–32 px, chữ đầu gạch chân, vòng hồi, từ kế mờ 50 %, tên chiêu tách khỏi từ, trạng thái `held`, viền hệ; cả dải mờ khi Bàn Quyết không sống; không rung); `learning-frame.ts` (Source: Rồng `src/ui/learning-frame.ts`: IPA, nghĩa, nút nghe; nghĩa hiện theo số lần nhớ đúng và preset); `ime-banner.ts`; `learn-ahead.ts` (Học trước, Linh Sa mỗi từ theo canon §14.2); `review-card.ts` (Thẻ Ôn 3 câu, phím 1/2/3, đồng hồ nghỉ dừng, ẩn lớp chữ chiến đấu, Linh Sa mỗi câu theo canon §14.2); `word-book.ts` (Sổ Từ cho Thu Hoạch).
10. `app/learning.ts` (Source: Rồng `src/app/learning.ts`): sự kiện học theo canon §17, `gameId` `immortality-cultivation`, trường `channel`, hàng đợi cục bộ, `isRightRecall`; Học trước luôn `hintUsed: true`; **chế độ nháp** `dryRun: true` cho bot (không bao giờ gửi; hàng đợi chặn và ghi lỗi nếu gặp sự kiện của bot, canon §17.2); gọi `take` của sổ cái khi có `word-first-seen`.
11. `app/typing-pace.ts`, `app/pace-card.ts` (Source: Rồng): thẻ tốc độ (D18), `?wpm=`, cập nhật hồ sơ `immortality-cultivation.skill` sau trận; trận đầu hồ sơ "chưa biết" phát `pace-update` sau đợt 1.

**Nghiệm thu**
- Test: HC1 ở mức đơn vị **theo bản ghi** (hồ sơ trống: 0 từ không có bản ghi và không thuộc từ nền lên ô gấp); HC2; một Cast cho mỗi `wordId` (phím lặp, Esc, tạm dừng, dừng hình); `held` 3 s và `fizzled` không tốn hồi, `fizzled` không cho Chân Nguyên; phím chữ lúc nghỉ không tạo Cast; không đổi từ khi đang gõ dở; luật tiền tố, khoảng sửa; thứ tự lùi không bao giờ ra từ mới; Esc giữ số phím sai; sổ cái từ mới: cửa sổ trượt, một từ một lần, `take` lặp không trừ, không đụng `Date`; bộ từ lạnh ≥ 40 từ, không nhãn đổi; từ mới gặp ≥ 3 lần; bảng `activityType`, luật `hintUsed` (kể cả ngoại lệ), `channel`; Học trước không bao giờ là lần nhớ; sự kiện nháp không vào hàng đợi.
- Kịch bản của Làn 7 (`ic-words`, `ic-ime`, `ic-keyboard-only`) qua.

### 6.4 Làn 4 — Kiếm, combat, trận pháp, cơ quan, kinh tế

**Việc**
1. `combat.ts` (Source: phần sát thương của Rồng `src/sim/combat.ts`): `damageBeast` trên **máu nguyên**; thứ tự `P → M_q → M_hệ → bucket → dễ tổn thương → giáp/kháng → trần cụm → trần máu còn` với `mulDiv` làm tròn nửa lên mỗi bước (canon §7.2, D38); giáp `G/(G+100)` trần 75 %; đòn gõ bỏ qua giáp; khắc hệ (luật có sẵn dù M0a vô hệ); phá thế ×1,5; trần cụm 60 %; rẽ đòn 4 m 50 %; chồng chậm (khác nguồn nhân, trần 60 %).
2. `shares.ts`: sổ phần sát thương theo nguồn (gõ theo từng ô, đánh nền, cơ quan, đan phù, trận pháp) cộng **sát thương hiệu dụng** cho CB2, CB3.
3. `skills.ts` + `data/school-kiem.ts`: bảng canon §12.1 — đánh nền (từ lệnh `auto`, kiểm tầm theo `origin`), ô 1 (**sát thương tính một lần mỗi từ rồi chia 3 kiếm, dư vào kiếm cuối**; băng 3 kiếm, chờ ≤ 2 băng, xuyên), ô 2 (tuyến, 2,5 W thú đầu), ô 3 (Hộ thân: tạo `ward` qua `wards.ts`; hoặc thân pháp: sự kiện cho `local`), ô 4 (vùng, **trần 4 W mỗi lần tung cộng mọi thú**), ô 5 (3 loạt; số kiếm hình chỉ ở view), tâm pháp Kiếm Tâm, Tích Kiếm; **tick chạm** +6/+36/+66, +12, +12 rồi mỗi 30 tick, +30/+75/+120, +18 (canon §12.1); luật đích và hòa điểm (canon §23.3).
4. `wards.ts` (canon §9.1, D34, PB-01): `ward{seat, origin, r 2 m, đến tick, còn 3 lần}` đứng yên 5 s; đỡ đòn vào bot, điểm nhãn trong vòng; `wardAt`, `wardCrosses`; nhận `ward-use` từ `local` (kẹp ở 0); phát sự kiện `ward`.
5. `chan-nguyen.ts`: +5 / +3 / +2 **× 1 / k_ghế** (phần nghìn, nửa lên), chỉ Cast `resolved`, đầy 100, xin từ ô 5 (canon §6.6).
6. `formation.ts`: Trận Tâm và Trận Lực 1.000; Kết Giới (thú chậm 15 %); Tâm nhãn (Công +8 %, Thủ −15 %, **Dưỡng 0,1 %/s khi có Cast `resolved` trong 3 s / k_ghế**, trần 15 %, tắt khi gục và khi Bàn Quyết không sống); chiếm nhãn 3 s + Tẩy; Trận Trụ (2 cú húc rồi nứt; chặn đá ném, chặn húc); Linh Dịch.
7. `mechanisms.ts` + `data/mechanisms.ts`: 3 cơ quan canon §8.3, cấp 1–3, trần khống chế cứng 35 %, 6 ô.
8. `economy.ts` (Source: Rồng `src/sim/economy.ts`): **ví theo ghế trong thế giới**; quỹ Linh Sa 60 / 25 / 15; hạ thú trả theo **ĐĐ** (`round(0,60 × 900 × f × ĐĐ / ΣĐĐ_trận)`, ΣĐĐ từ `WaveDef` gồm phần gọi tối đa ở 50 %, không gồm Vương), ghi sổ ngay tick chết, cụm trả một lần; hết đợt +10 % mỗi đợt; **thưởng học tính từ quỹ** (Thẻ Ôn mỗi câu = round(0,15 × 900 × f × 0,8 / (3 × số lần nghỉ)), Học trước mỗi từ = round(0,15 × 900 × f × 0,2 / 8); canon §14.2, PB-07); Linh Sa dư → Thú Hạch chỉ ghi (M0a chưa có tiến trình).
9. `shop.ts` (Source: Rồng `src/sim/shop.ts`): mua, đặt, nâng, bán lúc bày trận và nghỉ; hoàn 70 % / 100 %.
10. `consumables.ts` + `data/consumables.ts`: 3 món M0a, 2 ô × 3, phím 1/2/3, hồi chung 8 s; **sim giữ số viên, hồi chung, Linh Sa**, phát `consumable{seat, kind}`, áp Lôi Hỏa Phù lên thế giới; Hồi Xuân Đan, Kim Thân Phù để `local/consumables.ts` của Làn 2 áp (canon §12.3). Không dùng được khi gục.

**Nghiệm thu**
- Test từng luật: thứ tự và làm tròn sát thương; giáp và đòn gõ; trần cụm; trần bucket; sổ phần cộng sát thương hiệu dụng; băng ô 1 không quá 2; tuyến giảm 15 % sàn 40 %; vùng ô 4 trần 4 W mỗi lần tung; tuyệt kỹ ≤ 2,5 W mỗi thú; tick chạm đúng; `ward` đỡ 3 lần, đỡ bot và nhãn trong vòng, `wardCrosses` khi vòng cắt vạch; Trận Trụ đếm cú húc; Tâm nhãn đúng trần; Chân Nguyên và Dưỡng chỉ cho `resolved`, × 1/k; hoàn tiền đúng; hồi chung đan 8 s; tác dụng lên mình không nằm trong sim.
- **`tests/sim/combat-kill-invariants.test.ts`** (canon §10.2, PB-06): ở Thư giãn, Cân bằng, Thử thách, Học, không Tích Kiếm, không khắc ×0,80: một kiếm ô 1 không Ẩu hạ Thạch Thử (30 máu); một từ ô 1 không Ẩu hạ Phong Lang (90 máu) khi cả 3 kiếm trúng; kiểm cả K0, K1.
- **Linh Sa** ải M0a tối đa (bot làm đủ học) = **1.325 ± 3**; Thẻ Ôn 9, Học trước 4 mỗi lần; trận dạy một cổng: 5 và 2; bot làm đủ học hơn bot bỏ qua **≤ 15 %** (KT4 đúng theo cấu tạo; PB-07).
- Một lượt bot Chuẩn có kịch bản in phần gõ, phần ô 1 (để Làn 7 so CB2, CB3).

### 6.5 Làn 5 — Thú, tinh anh, Thú Vương, báo trước

**Việc**
1. `beasts.ts` + `data/beasts.ts`: 5 họ canon §10.2 (W, tốc, vai, đòn; máu nguyên = round(W × 90 × g(K) × hệ số preset)); khối tạm một màu mỗi họ (hai chân cao, bốn chân thấp dài, bay lơ lửng, bầy nhỏ đi cụm) với cỡ cho view; đi theo `field.ts`; chậm trong Kết Giới; **Nham Viên dừng cách đích 11 m** (PB-17).
2. `targeting.ts`: chỉ đích hợp lệ của canon §10.1; "gần Trận Tâm nhất" theo khoảng cách trường hướng (thú đất) hoặc thẳng (thú bay), hòa thì `beastId` nhỏ hơn (canon §23.3).
3. `elites.ts` + `data/elites.ts`: 3 thuộc tính, W × 1,6, Thế 40, xin Ấn.
4. `posture.ts`: Thế, mức giảm, phá thế 6 s ×1,5, miễn 15 s, đầy lại; −35 / √(số ghế) cho Ấn.
5. `telegraph.ts` + `data/telegraphs.ts`: **một công thức T** (canon §10.6), hàm runtime `chargeTicks(def, preset, k)` kẹp `max(T, nạp / k)` (không dùng `telegraphScale` ở M0a); `TelegraphDef` theo canon §23.3; hình tròn, nón, tuyến, ô; danh sách đáp án mỗi đòn; sự kiện `start`, `strike`, `cancel`. Đòn không có đáp án gõ: báo ≥ 1,2 s + nửa bề rộng ÷ 5 m/s (**Nham Viên 1,6 s; Thiết Giáp Trư 1,2 s + thời gian ra khỏi vạch**; PB-27).
6. `boss.ts` + `data/boss.ts` (khuôn từ Rồng `src/sim/boss.ts`): Lang Đầu Đàn (hào quang, Tru Đàn **tối đa 2 lần mỗi đợt**, chỉ gọi khi `liveRoom` đủ, không thì bỏ lượt); Thiết Bối Lang Vương **W 64, t đích 120 s**, 3 pha (Vồ Xé; **Gọi Đàn P1 mỗi 30 s, P2 không gọi, P3 mỗi 18 s**, tải phụ ≤ 30 % W_Vương; Thiết Bối Xung với 4 cách giải; P3); gầm chuyển pha 2,5 s, hủy Ấn cũ; đâm Trận Trụ qua `pillarOnSegment`; đỡ một nửa khi **vòng `ward` cắt vạch ở tick chạm** (`wardCrosses`, canon §10.5).
7. `pressure.ts`: cắn mép Trận Tâm; Nham Viên ném (Trận Trụ chặn, kiểm đoạn thẳng số nguyên); Hỏa Nha bổ nhào; Thiết Giáp Trư húc và chiếm nhãn; đòn vào bot, nhãn trong vòng `ward` bị đỡ; × g(K) × hệ số preset.

**Nghiệm thu**
- **CB5** (test dữ liệu, PB-28): gọi `chargeTicks(def, preset, k)` với k ∈ {0,75; 1; 1,30}, ℓ lớn nhất của dải đáp án, 4 preset: kết quả ≥ T.
- **`tests/sim/telegraph-floor.test.ts`**: mọi `TelegraphDef` không có đáp án gõ đạt sàn 1,2 s + nửa bề rộng ÷ 5 m/s.
- Test dữ liệu: mọi đòn lớn có ≥ 2 đáp án, ≥ 1 không cần gõ.
- Test tính chất: 20 seed × mọi bot, **0** thú chọn đích là người thật.
- Test triệu hồi: Tru Đàn ≤ 2 lần mỗi đợt; Gọi Đàn ≤ 30 % W_Vương qua 20 seed; không gọi khi trần thú sống đầy; P2 không gọi.
- Test Thế (giảm, phá, miễn 15 s, đầy lại); mỗi cách giải Thiết Bối Xung cho đúng kết quả của canon (gồm `ward` cắt vạch); Hỏa Nha bỏ qua cơ quan đất; Phong Ấn Võng kéo thú bay xuống.

### 6.6 Làn 6 — View hộp xám, HUD, móc âm

**Việc**
1. `stage.ts`, `ground.ts`: cảnh hộp xám trên renderer của Làn 1: đất phẳng 40 × 26 m tô màu có lưới và hành lang, cổng, Trận Trụ (khối), Trận Tâm (đĩa), vòng Kết Giới, điểm Tâm nhãn, 6 dấu ô cơ quan (chỉ lúc bày trận và nghỉ), gợi ý đường trời; shading ramp và viền mực tạm.
2. `actors.ts`, `player-view.ts`: thú qua `crowd` (kiểu vẽ theo bậc lấy từ phán quyết HN0 trong `rules.ts`; `procedural` tới khi VAT sẵn); tinh anh × 1,25 + vòng hào quang; thú tướng × 1,4; Thú Vương khối tạm lớn (đường `SkinnedMesh` qua `walker-rig` chỉ đo ở bench, hình thật ở M0b); người chơi là khối tạm đọc từ `local`; vòng `ward` (r 2 m) vẽ từ sự kiện `ward`.
3. `telegraphs.ts` (Source: Rồng `src/view/telegraphs.ts`): đỏ `#FF4A4A` đầy dần, có sọc và biểu tượng; tròn, nón, tuyến, ô.
4. `fx.ts`, `pickups.ts`: **nối** sự kiện vào `createHitFx`, `createDamageNumbers`, `createInkSmoke`, `createSwords` của Làn 1 (không viết lại số sát thương hay khói mực; PB-36): chiêu Kiếm (tuyệt kỹ đúng số kiếm của bậc, lấy từ bể chung), vùng Lạc Kiếm Trận, tuyến Xuyên Vân; hạt Linh Sa bay về HUD (chỉ hình).
5. `feedback-profile.ts` (canon §21.1, D44, PB-20): hồ sơ phản hồi **cục bộ** (khung `FeedbackProfile` của kit với `id: "dragon"`, đè số T0–T5, dừng hình, rung); chỉ dùng phần số và nhịp của `kit/feedback`, **không** `AudioCues`; ghi vào `SYNC_DEBT.md`.
6. UI: `hud.ts` (Sinh lực, khiên, Chân Nguyên, Trận Lực, thanh Thế của tinh anh gần nhất hoặc Vương, thông báo); `wave-card.ts` (mỗi cổng: biểu tượng họ, số con, dấu: cánh = bay, búa = chiếm nhãn, vương miện = thú tướng, sừng = Thú Vương; dải nhịp đỉnh); `shop-strip.ts` (bày trận và nghỉ: cơ quan, đan phù; chuột) và **`shop-mode.ts`** (chế độ cửa hàng bằng phím, canon §5.1, D45: `` ` `` mở, ← → chọn món, ↑ ↓ chọn ô, Enter mua hoặc đặt, `=` nâng và `-` bán bấm hai lần, Esc thoát); `results.ts` (Thu Hoạch: học và RPG tách dòng; nhúng Sổ Từ); `menu.ts` (tiếp tục, tốc độ gõ, giảm chuyển động, rút lui, đổi phím); `skin.ts` + `styles/**` (Be Vietnam Pro, Noto Sans cho IPA; token của `kit/ui`); `screen-zones.ts` (Source: Rồng).
7. Giảm chuyển động: theo media query và cài đặt; `?motion=full|reduce` để kiểm; không rung camera khi bật.
8. `audio/**`: danh mục id theo thẻ canon §22, mọi id `silent: true`; ánh xạ sự kiện → id; bộ trộn bus không phát gì. **Không viết âm tổng hợp**; test chặn `OscillatorNode`, `createOscillator` và mọi nguồn phát trong `src/audio`, cộng luật cấm import `kit/feedback/audio-cues`, `kit/audio/dragon-voice` của test ranh giới (mục 2.1).

**Nghiệm thu**
- Test: HUD đọc đúng giá trị; dấu thẻ đợt; luồng phím chế độ cửa hàng (mua, đặt, nâng hai lần, bán hai lần, Esc; mũi tên không làm người chơi đi khi chế độ mở); vùng màn; mọi id âm im lặng; không tệp nào import `AudioCues`.
- Kịch bản của Làn 7: cỡ px đạt canon §21.1 (`ic-scale`); Bàn Quyết không bị che; 0 lỗi console; `ic-perf` ở High trên Dell TB ≤ 8 ms, p95 ≤ 12 ms.
- **`ic-camera-frame` (canon D48, chủ dự án 25/10).** Ở 1280 × 720 và 1920 × 1080, khung camera chứa đủ:
  - 4 góc sân 40 × 26 m, có lề;
  - 2 cổng, đường trời, Trận Tâm;
  - mọi thú đang trên sân ở đợt đông nhất.
  Phép kiểm chiếu các điểm đó qua `Projector` và chụp ảnh để xem. Không zoom vào trong trận.

### 6.7 Làn 7 — Bot, cân bằng, golden, kịch bản

**Việc**
1. Bot (Source: Rồng `scripts/balance/{bot,typist,policy,hands,meter,report,run,golden*,load}.ts`, adapted): `HumanTypist` và `STANDARD_BOTS` của kit + bot Đứng yên, Cơ động (canon §18.3); **chính sách đi mặc định Đứng yên** cho 9 bot đầu (D46); **chính sách chọn ô** Tẩy → Ấn → ô 5 → ô 2 → ô 4 → ô 3 → ô 1 (Học: ô 4 trước ô 5; "Vừa" bỏ ô sẵn 1–2 s theo seed, "Tốt" không bỏ, "Kém" chọn ngẫu nhiên; PB-05); mua (Kém / Vừa / Tốt) qua lệnh cửa hàng; Học trước, Thẻ Ôn; chạy trận headless bằng `createWorld`, `step`, `local`; bot dựng **sự kiện học nháp** (`dryRun: true`) qua `app/learning.ts` của Làn 3, không bao giờ gửi (D43).
2. `calibrate.ts`: đo **D_ref, D_đơn** trên sân thử trộn (canon §7.4) **trước** khi chỉnh đợt; in số để Làn 2 ghi vào `rules.ts` `REF_OUTPUT`; in phần gõ theo ô để so với ước ô 1 ~10, ô 2 ~18, ô 4 ~11, tuyệt kỹ ~8.
3. `meter.ts`: mẫu mỗi tick cho `FlowMeter` theo định nghĩa của game (canon §18.2: P; **I = (a) ∧ (b tính từ Trận Tâm và tầm ô 1) ∧ không P**; O, S, Q).
4. `report.ts`: B1–B9 bằng `runGates` của kit với **dải chung**; CB1–CB6, **CB9**; HC1–HC3, **HC7 (trận M0a, bot Chuẩn × 20 seed), HC8** trên sự kiện nháp; phần sát thương, **phần ô 1 theo từng bot ngay vòng đầu** (CB3 ở Khá, Nhanh), số Ấn, chữ sống tối đa, nghẽn chữ đầu, "nghẽn" của bước lùi, số lần dùng từ nền theo ô, thời lượng trận (không tính bảng mở), sự kiện `pace`; P, I, O thêm của bot Chuẩn Cơ động (chỉ so); bot × preset × 20 seed; Markdown + JSON. Không bao giờ chỉ in dải riêng (D15).
5. Golden: `tests/golden/m0a.json` — 20 seed bot Chuẩn, Cân bằng + 3 ca (Thư giãn, Thử thách, bộ điều nhịp tắt); so `hashWorld` **và** `hashLocal` mỗi 600 tick và cuối trận; `pnpm ic:golden:update` chỉ sau một đổi luật có chủ ý.
6. Kịch bản trình duyệt (Source: Rồng `scripts/visual/scenarios/dh-*.mjs`, `lib/dh.mjs`): `ic-smoke`; `ic-words` (không chữ nào bị che, 720p và 1080p, chữ 100 % và 150 %); `ic-keyboard-only` (chơi cả ải chỉ bằng bàn phím theo bảng canon §5.1, gồm **chế độ cửa hàng** `` ` ``; bố cục Mac và Linux); `ic-ime` (soạn chữ → dải báo); `ic-telegraphs` (nạp ≥ T ở `?wpm=15`, `25`, `70`); `ic-focus` (mất focus, tạm dừng: 0 tick); `ic-scale` (cỡ px); `ic-perf` (game thật, High và Low, GPU Dell); **`ic-hitstop-keys`** (Source: `games/dragon-hold/scripts/visual/scenarios/dh-hitstop-keys.mjs`; phím tới đòn ≤ 50 ms theo định nghĩa canon §20.2; PB-35); `ic-replay` (`__ic.replayCheck()`, so cả `hashLocal`). Mọi kịch bản: 0 lỗi console; ảnh vào `tmp/shots/<làn>/` và **phải được xem** trước khi kết luận điều gì về hình.

**Nghiệm thu**
- Báo cáo đủ ma trận; cổng chấm đúng; ma trận đầy đủ chạy ≤ 45 phút với `--jobs=4`.
- Golden xanh; replay khớp cả hai mã băm.
- 0 sự kiện có nguồn là bot vào hàng đợi học.

### 6.8 Làn 8 — Tĩnh Tu thử (trang `tinh-tu.html`)

**Việc**
1. `src/tinh-tu/sim/*` (thuần, tất định): phiên 60 s; 3–4 điểm đọc; lịch sinh chữ (mỗi Minh ≥ 2 lần, lần đầu hiện nghĩa); thời gian sống L / 1,5 L / 2 L theo **E_eff của hồ sơ** (`typeSeconds` của `kit/typing/tempo`); bộ xếp lịch bảo đảm **không hai Minh hết hạn trong cùng cửa sổ 1,5 s**; chữ đầu bậc 1; ân hạn 1,2 s và tha phím lạc (`kit/typing/session`); **chấm** (canon §16, D40, PB-12): phiên **hoàn thành** (gõ xong mỗi từ Minh ít nhất một lần) = `clamp(40 + 5 Minh + 2 Thường − 3 nhầm; 40; 100)`, phiên chưa hoàn thành = `max(0; 5 Minh + 2 Thường − 3 nhầm)`, cộng dồn tới 100; Nhập Môn và Tham Ngộ.
2. **Tham Ngộ** (D40, PB-13): màn hiện tên nhóm chủ đề của bài; 1/3 Tâm ma không nhãn; Thường không nhãn chỉ lấy từ đến hạn **cùng nhóm**, Thường khác nhóm giữ dấu riêng (viền nhạt, giọt mực); Tâm ma từ nhóm **cách ≥ 3 bậc** (bảng khoảng cách 15 nhóm ở `src/tinh-tu/sim/topics.ts`), độ thuộc ≥ 70; bỏ từ đa nghĩa và mọi từ thuộc ≥ 2 nhóm khỏi cả Thường và Tâm ma.
3. Dữ liệu: bài 6 từ từ `shared/vocabulary/topics`; bộ thử dự phòng khi không có portal.
4. UI DOM hộp xám: thẻ Khẩu Quyết (không tính giờ, gõ lại mỗi từ một lần); màn phiên (mặt nước tạm bằng gradient, lá phù có viền và biểu tượng riêng mỗi loại); màn kết (điểm, từ đã gặp, danh sách "chọn nhầm" kèm nghĩa); giảm chuyển động; chỉ bàn phím chơi được. Tĩnh Thất mở bài mới **chỉ khi sổ cái còn ≥ 6 từ**; không thì hiện "còn N phút nữa đủ 6 từ" và cho phiên ôn (chỉ Thường).
5. Sự kiện học theo canon §16, §17 qua `kit/learning` (`gameId` `immortality-cultivation`): Minh và Khẩu Quyết **luôn** `review-card` kèm `hintUsed: true`, mọi lần (PB-31); bot chỉ dựng nháp. Sổ cái: `typing/new-word-ledger.ts` của Làn 3 (chỉ import) qua `src/app/storage.ts`, giờ từ `Date.now()` ở tầng UI của trang (không ở `src/tinh-tu/sim`).
6. `scripts/tinh-tu/bots.ts`: `HumanTypist` 15 / 25 / 35 / 60 / 90 WPM × 20 seed × 2 bậc, cộng bot Không gõ và bot gõ mọi chữ; bot Chuẩn ở Tham Ngộ đoán theo nhóm chủ đề, có lỗi đọc; báo cáo HC4, HC4b, HC5, HC6, HC6b, HC7.

**Nghiệm thu:** HC4, HC4b, HC5, HC6, HC6b, HC7 (mục 8); test đơn vị (gồm phiên chưa hoàn thành không có sàn; không mở bài mới khi sổ < 6); kịch bản `tt-session.mjs` 0 lỗi console, chỉ bàn phím.

### 6.9 Tích hợp

- `src/app/app.ts` (`startApp`): thẻ tốc độ → bày trận → thế giới, `local`, vòng khung, định tuyến phím, mọi presenter. Thứ tự khung (nguồn: Rồng `LANES.md` "Integration"): rút sự kiện → `learning.onEvents` → luồng app (Thẻ Ôn, xả hàng đợi) → `onEvents` của mọi presenter → cập nhật stage (camera trước khi chiếu DOM) → `frame` của mọi presenter → vẽ.
- **Nạp trận:** đọc hồ sơ (`.skill`), sổ cái (`.newwords`) và bản ghi học (lõi học, hoặc trống → khởi đầu lạnh); dựng bộ từ bằng `buildDeck`; chụp `remaining` thành `newWordAllowance`; ghi **đầu replay** canon §23.2 trước tick 0. Khi sim phát `word-first-seen`, gọi `take(wordId, Date.now(), channel)` rồi lưu `.newwords`.
- `src/app/input-router.ts`: một listener `keydown` trên `window`, pha capture. Chữ (kit `typedLetter`) → bảng đang mở, không thì lệnh `key` kèm `origin`, `aim` **chỉ khi Bàn Quyết sống** (từ báo đợt tới hết đợt, pha Vương; canon §6.1), còn lại bỏ. Thứ tự: chặn (menu, màn focus, 3-2-1) → bảng đang mở (gồm **chế độ cửa hàng**, mở bằng `` ` `` lúc bày trận và nghỉ; mũi tên, Enter, `=`, `-` thuộc chế độ này) → Esc nhả khóa → Backspace → 1/2/3 (bảng nếu mở, không thì đan phù) → Enter bắt đầu đợt → mũi tên cho `local` → dự phòng (menu dừng). Chuột phải → `move-to`; chuột trái lên thú → `soft-target`.
- Sim đứng yên khi bảng học mở (đồng hồ nghỉ dừng), ở menu dừng, dưới màn focus, trong 3-2-1 sau tạm dừng.
- **Bậc hình mặc định** (canon §20.1): lần đầu High nếu GPU rời, Medium nếu Apple, Low nếu khác; sau 10 s đầu trận, p95 vượt ngân sách thì chỉ **gợi ý** hạ bậc.
- Cờ URL: `?q=low|medium|high`, `?seed=`, `?preset=`, `?wpm=`, `?motion=`, `?prelearn=0`, `?speed=N` (chỉ bản dev, luật không đổi), `?debug=1` → `window.__ic` (`state`, `send`, `replayCheck`, `foeSizes`).
- `src/app/save.ts` trên `storage.ts`: lưu v1 tối thiểu ở M0a (`.skill`, `.newwords`, `.settings` theo canon §23.1) có số phiên bản, hàm chuyển đổi và tệp mẫu trong `tests/app/save-migrate.test.ts`; `.save` (tiến trình) để M1.

## 7. Cổng M0a

| Mảng | Cổng | Ngưỡng | Ai |
|---|---|---|---|
| Test | `pnpm check` xanh; test ranh giới (gồm cấm import âm tổng hợp của kit); golden 20 seed + 3 ca; `combat-kill-invariants`, `telegraph-floor`, `save-migrate` (test tu vi theo biến thể của canon §15.2 để M1, khi có tiến trình) | Khớp `hashWorld` và `hashLocal` | Mọi làn; Làn 7 |
| Bot | **B1–B8** (9 bot đầu, đi Đứng yên; B8 chấm trên sự kiện nháp) | `BALANCE.md` §7, dải chung §3 | Làn 7 |
| Bot | **CB1–CB6, CB9** (CB9 ở M0a: ải M0a 9–10,5 phút với bot Chuẩn) | canon §18.4 | Làn 7 (CB5 của Làn 5) |
| Học | **HC1–HC3, HC7 (trận M0a), HC8** trên sự kiện nháp | canon §18.4 | Làn 7 |
| Hiệu năng | **HN0** | canon §20.2–20.4; phán quyết theo N của luật, cột "N đạt 3D đầy đủ" và "phần vượt" đã ghi | Làn 1 |
| Hiệu năng game | `ic-perf` High trên Dell: TB ≤ 8 ms, p95 ≤ 12 ms; `ic-hitstop-keys` ≤ 50 ms; sim ≤ 0,3 ms mỗi bước ở 300 thú | | Làn 7 |
| Trình duyệt | `ic-smoke`, `ic-words`, `ic-keyboard-only` (gồm chế độ cửa hàng), `ic-ime`, `ic-telegraphs`, `ic-focus`, `ic-scale`, `ic-hitstop-keys`, `ic-replay`: đạt; 0 lỗi console; ảnh đã xem | | Làn 7 |
| Âm | 0 âm phát ra; mọi id `silent: true`; không mã âm tổng hợp; không import `AudioCues`, `dragon-voice` | | Làn 6 |
| Người | **B9**: anh chơi ải M0a một lượt (sau khi Rồng qua B9); game xuất nhật ký (replay canon §23.2); bot cùng hồ sơ lệch ≤ 15 %. **M0a chốt có điều kiện, B9 mở** tới khi chạy được (canon §25, PB-37) | | Anh, Làn 7 |
| Phản biện | Một vòng phản biện độc lập (chỉ đọc) đối chiếu canon, mã, báo cáo trước khi chốt; lỗi đã sửa hoặc ghi vào changelog | | Agent phản biện |

- Trận không đạt cổng bot: chỉnh hệ số trong dữ liệu (±10 %) hoặc thành phần; không sửa mã để qua cổng. Mọi số đổi ghi vào changelog và, nếu là số của canon, sửa canon cùng lượt.
- Một cổng trượt sau 3 vòng chỉnh: dừng, ghi các lần thử và số đo, nêu đề xuất cho anh (như vòng 3 của Rồng); không tự đổi dải chung.

## 8. Cổng bản thử Tĩnh Tu

| Cổng | Ngưỡng |
|---|---|
| HC4 | Bot 15 / 25 / 35 / 60 / 90 WPM, Nhập Môn và Tham Ngộ, 20 seed: đạt 100 điểm trong ≤ 2 phiên ở mọi ô |
| HC4b | Bot Không gõ không lĩnh ngộ sau 10 phiên; báo cáo điểm phiên của bot gõ mọi chữ so với bot Chuẩn |
| HC5 | 0 lần hai Minh hết hạn trong cùng cửa sổ 1,5 s |
| HC6 | 0 sự kiện học âm từ Tâm ma |
| HC6b | Bot Chuẩn ở Tham Ngộ: tỉ lệ "chọn nhầm" ≤ 10 % |
| HC7 | ≥ 90 % sự kiện học đúng luật (đích 100 %; mọi sự kiện sai được in); cứng: 0 `hintUsed: false` khi nghĩa đang hiện, Minh luôn `hintUsed: true`, 0 sự kiện của bot vào hàng đợi |
| Trình duyệt | `tt-session.mjs`: chỉ bàn phím, 0 lỗi console, lá phù phân biệt được khi tắt màu (ảnh thang xám đã xem) |
| Người | Anh thử ~0,5 giờ (sau Rồng B9) |

## 9. Đo GPU

**Máy Dell** (Windows 11, WSL Ubuntu 24.04, RTX 3050 Ti). Chrome trong WSL chỉ vẽ phần mềm, nên số đo của nó **không hợp lệ**.

1. Trong WSL (git, node, pnpm chỉ có ở WSL; chạy bằng một tệp script bash, vì chuỗi PowerShell làm hỏng `$`):

   ```bash
   cd /mnt/d/typing-game && source scripts/local-env.sh
   cd games/immortality-cultivation
   setsid nohup pnpm dev > tmp/vite.log 2>&1 < /dev/null &
   ```

   Vite trong WSL không thấy tệp sửa từ Windows: khởi động lại sau mỗi lần sửa mã, hoặc chạy với `CHOKIDAR_USEPOLLING=1`.
2. Từ Windows, chờ `http://127.0.0.1:3008/` trả lời. **Chỉ một lượt đo GPU một lúc**: có `D:\_tools\gpu.lock` thì chờ; không có thì tạo, đo, xóa.
3. PowerShell:

   ```powershell
   $env:URL = "http://127.0.0.1:3008/"
   $env:OUT_DIR = "D:\typing-game\games\immortality-cultivation\tmp\shots\bench"
   $env:CHROME_FLAGS = "--disable-gpu-vsync --disable-frame-rate-limit --enable-precise-memory-info"
   $env:Q = "high"; $env:CASE = "vankiem"; $env:COUNT = "60"; $env:RUNS = "3"
   & D:\_tools\node-v24.11.0-win-x64\node.exe `
     D:\typing-game\games\immortality-cultivation\src\kit\tools\cdp-run.mjs `
     D:\typing-game\games\immortality-cultivation\scripts\visual\scenarios\ic-bench.mjs `
     --width=1920 --height=1080
   ```

   Low: `--width=1280 --height=720`; Medium: `--width=1600 --height=900`. Ca `base` và `crowd-proc` một lần mỗi bậc; `crowd-vat`, `vankiem`, `impostor`, `skinned` × `COUNT` 60, 120, 300 × mỗi bậc (`--enable-precise-memory-info` để số bộ nhớ JS tin được; PB-35).
4. Kiểm hợp lệ: chuỗi `renderer` chứa "NVIDIA" (ANGLE D3D11). Nếu chế độ headless rơi về SwiftShader, chạy lại với `--headful`. Ghi rằng Windows của máy Dell báo `prefers-reduced-motion: reduce` (trang đo đặt `?motion=full`).
5. Máy đang chạy việc nặng của làn khác (build, bot) làm khung dài hơn: ghi tải máy lúc đo; số trượt thì đo lại khi máy rảnh trước khi kết luận.
6. Bậc Low trên GPU tích hợp: chỉ khi anh tự chuyển Chrome sang GPU tích hợp trong Cài đặt đồ họa Windows (agent không đổi cài đặt hệ thống); không có thì dùng luật dư ×2 của canon §20.2.

**Apple M4:** `pnpm dev`, rồi `CHROME_FLAGS="--disable-gpu-vsync --disable-frame-rate-limit --enable-precise-memory-info" URL=http://127.0.0.1:3008/ Q=high CASE=vankiem COUNT=60 node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/ic-bench.mjs --width=1920 --height=1080`; ngân sách con nhân theo tỉ lệ tổng của bậc (canon §20.2). Chuỗi `renderer` chứa "Apple"; bỏ số GPU timer (ANGLE trên Metal đọc sai, nguồn: Rồng `bench.ts`), dùng khoảng giữa hai khung.

## 10. Vé nợ đồng bộ (`docs/SYNC_DEBT.md`)

- Bảng: tệp của game · tệp nguồn · commit nguồn · đổi gì khi chép.
- **Chỗ cố ý khác nguồn** (ghi rõ để không ai "đồng bộ" ngược): `src/typing/deck.ts` bỏ nhánh hồ sơ trống gắn "known" và nhánh lấp chỗ `isNew ? "learning"` của Rồng (canon §17.1, D35); `src/view/feedback-profile.ts` là hồ sơ phản hồi cục bộ thay cho hồ sơ `tutien` trong kit (D44); `src/view/walker-rig.ts` lấy phần trộn clip của `kit/three/hero.ts`, bỏ locomotion bay; `src/content/model-contracts.ts` thay `MODEL_CONTRACTS` của kit cho nhân vật và thú; `waves.ts` giữ luật hết đợt của Rồng (mọi toán đã sinh và 0 thú sống), lặng trước Vương 8 s thay 12 s của Rồng (canon §4.1).
- Sửa đang mở ở Rồng Giữ Ải lúc chép (theo `games/dragon-hold/LANES.md`, changelog 25/10): B1, B7 trượt Nhàn I (cả hai dải); D27 (dải I ≤ 20 % ở Cân bằng, chờ anh); phần luật cổng của D29 (chờ anh); hộp `box()` và `settle()` một lượt của `kit/feedback/numbers.ts` (trôi so với kit).
- Luật: đầu mỗi vòng của M0a và M1, làn 2 so commit nguồn với `games/dragon-hold` hiện tại (`git log` các tệp nguồn), ghi sửa nào cần đem sang và sửa nào không áp (game này đo Nhàn I khác, canon D14). Không tự kéo sửa mà không chạy lại golden và bot.
- Khi cả hai game dùng ổn định cùng một phần (đợt, sinh quái, báo trước, cơ quan, đám đông VAT), đề xuất đưa phần đó lên `shared/game-kit` (kit chỉ chứa thứ ≥ 2 game dùng). Hồ sơ phản hồi `tutien` lên kit ở M0b; nhân vật đi bộ và hợp đồng model lên kit khi game thứ hai cần (canon D44).

## 11. Luật làm việc (vào `AGENTS.md` của repo game)

- Không sửa `games/space-typing`, `games/.wt-*` hay game khác; chép mã dùng lại kèm `// Source:`; không import chéo repo.
- **Không media trong Git**, bao giờ cũng vậy. Không dựng sinh vật, nhân vật, công trình bằng mã ngoài khối tạm.
- Không git phá (`reset --hard`, `checkout -- .`, `clean -f`, `stash` trần, force push). Không push. Không `sudo`, không `scripts/setup-nginx.sh`, không `pnpm media:push/pull`, không `pnpm bootstrap` khi còn việc chưa commit.
- TypeScript strict. Chú thích mã tiếng Anh; tài liệu, changelog tiếng Việt có dấu.
- Tắt mọi tiến trình nền mình mở (Vite, Chrome). Việc nặng chạy tuần tự dưới `flock /tmp/tg-heavy.lock`, `VITEST_MAX_THREADS=4`, bot `--jobs=4` (WSL chỉ có 7 GB RAM).
- Kiểm trình duyệt: Vite ở cổng của mình với `--strictPort`; kịch bản chạy bằng `cdp-run.mjs` của kit; ảnh vào `tmp/shots/<làn>/` và phải xem trước khi kết luận về hình.
- Cổng chung (`BALANCE.md`) không bao giờ chấm bằng dải riêng (canon D15).
- M0a không sửa `shared/game-kit`; thứ cần cho kit để cục bộ và ghi `SYNC_DEBT.md` (canon D44). Không import `kit/feedback/audio-cues`, `kit/audio/dragon-voice`.
- Bot không bao giờ gửi sự kiện học; chỉ dựng nháp `dryRun` (canon D43).

## 12. Rủi ro của M0a

| Rủi ro | Giảm bằng |
|---|---|
| Quá dễ như Rồng M0a vòng đầu (mọi bot thắng 100 %) | Áp lực liên tục từ đầu (ném, bổ nhào, cắn); D_ref đo trước khi chỉnh đợt; cổng B1, B2 ngay hộp xám |
| Gõ không là sức chính (đánh nền, cơ quan quá mạnh) | CB1–CB3 ngay vòng đầu; giảm phần không do gõ trước khi tăng tải |
| Nhàn I trượt như Rồng | Định nghĩa nhàn quyết định tính từ Trận Tâm, không trùng P (canon D14, D46); bot chuẩn đi Đứng yên; thời gian thú đi tới Kết Giới 8–12 s nhờ sân mới (canon §8.1); không đổi dải chung |
| VAT hay vạn kiếm trượt ngân sách | Đo theo N của luật (60), quy chi phí từng phần, chỉ phần vượt mới lùi theo thang của nó (canon §20.3, D36); kiếm cắt cuối cùng; phán quyết chỉ đổi kiểu vẽ, không đổi luật |
| CB3 trượt ở bot Khá, Nhanh (ô 1 nhận mọi từ dư) | In phần ô 1 theo từng bot ngay vòng đầu; tăng sức ô 2, ô 4 trước khi hạ ô 1 (canon §7.3, câu hỏi mở 10) |
| Trận lạnh thiếu từ cho ô 2, ô 5, Ấn (M0a không có lõi học) | Bước lùi về từ nền (canon §17.1); báo cáo in "nghẽn" và số lần dùng từ nền theo ô |
| Kiến trúc `local` (vị trí ngoài sim) làm khó bot và replay | Bảng tách quyền canon §9.1 (`ward`, đan phù, ví); replay ghi đầu vào cục bộ; bot chạy cùng `local`; golden băm cả `hashWorld` và `hashLocal` |
| Làn chồng tệp | Bảng sở hữu mục 4; bước 0 khai sẵn mọi trường `World`; số sát thương và khói mực chỉ ở Làn 1; đổi kiểu đi qua Làn 2; sự kiện mới qua `// WANT EVENT` |
| Giờ của anh | M0a không cần Tripo hay Bảng Nghe; chỉ một buổi B9 sau Rồng |
