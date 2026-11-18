# Tách ba game mới khỏi Space Typing (23/10/2026)

> **Yêu cầu của chủ dự án (23/10):** Space Typing đang bị nhồi quá nhiều. Tách thành **ba game mới**, mỗi game có bối cảnh, chủ đề, UI và âm thanh riêng: (1) game rồng mới **Rồng Giữ Ải**, (2) game thủ thành **Lời Gọi** (Typing Defense, đang là `src/td` trong Space), (3) game kiểu Typing Break **Tuyến Cuối** (Sinh Tồn, đang là `src/survival` + `src/feedback` trong Space). Dùng lại những gì Space có, nhưng không viết hết vào Space. Đưa ba game lên menu chung (portal).
> **Dựa trên:** `dragon-lane/research/codebase-and-split.md`, `dragon-lane/05-presentation-audio-tech-split.md` §9, trạng thái repo đọc ngày 23/10. Quyết định đã chốt ở `dragon-lane/00-canon.md` §3 (D01, D17, D18, D22).
> **Trạng thái:** kế hoạch. Chưa sửa mã, chưa chạy lệnh git nào đổi trạng thái.

## 0. Tóm tắt

1. **Bốn game chiến đấu trên portal**, mỗi game một repo con (submodule), một cổng, một host, một vỏ UI, một bộ âm: Space Typing (giữ), **Rồng Giữ Ải** (`dragon-hold`, 3005), **Lời Gọi** (`typing-defense`, 3006), **Tuyến Cuối** (`typing-survival`, 3007).
2. Mã dùng chung nằm ở **`shared/game-kit`** của repo cha, được **chép** vào `src/kit/` của từng game có kiểm sha256. Kit chép **từ** Space; **Space giữ nguyên bản gốc**, không đổi một dòng ở giai đoạn này.
3. **Tuyến Cuối tách ngay** vì S0 đã commit trên `feat/survival-s0`. **Lời Gọi tách ở ranh giới mốc**: chờ làn TD đóng R3, gộp, đóng băng, rồi mới `filter-repo`.
4. **Rồng Giữ Ải không chờ việc tách:** bản thử dọc (DESIGN.md §9, M0) chạy song song từ ngày đầu.
5. Hạ tầng (portal, nginx, chứng chỉ, lệnh dev, play) làm **một lần cho cả ba game**, để chủ dự án chỉ chạy `setup-nginx.sh` (cần sudo) một lần.
6. Không chuyển dữ liệu lưu của TD, Sinh Tồn sang host mới: chưa có người chơi thật (D18).

## 1. Bốn game và chủ đề

### 1.1 Bảng chung

| | Space Typing (giữ) | **Rồng Giữ Ải** | **Lời Gọi** | **Tuyến Cuối** |
|---|---|---|---|---|
| id · cổng · host | `space-typing` · 3004 · `space.` | `dragon-hold` · 3005 · `dragon.` | `typing-defense` · 3006 · `td.` | `typing-survival` · 3007 · `survival.` |
| EN | Space Typing | Dragonhold | Wordwoven | Last Line |
| Thể loại | Bắn gõ chữ, chiến dịch 1.000 ải, Duel | Thủ ải gõ phím, Rồng ở giữa, 520 ải | Thủ thành trợ lực bằng chữ, làng và dân gọi | Sinh tồn đám đông, gõ là nạp đạn, 600 ải |
| Bối cảnh | Phiêu lưu 8 thế giới sao | Đại Ngàn Sương, Bầy Héo, Bệ Rồng | Miền Văn Điền (TD 22.1): ruộng bậc thang, làng tre, đèn giấy | Vành Chân Trời: trạm thép giữ hành lang ở mép hố đen (mục 1.3) |
| Góc nhìn | Ngang, cuộn | Trên xuống 55°, xoay tự do | Trên xuống 55°, kéo bản đồ | Hành lang cố định, bến súng ở đáy |
| Bảng màu | Neon vũ trụ | Lục rêu, lam thông, tím tán, kem nắng | Xanh mạ, vàng lúa, nâu tre, đỏ son | Thép tối, cam nóng, lam điện |
| Vỏ UI | Kính sci-fi | Gỗ khắc, vỏ cây sẫm, viền rêu | Giấy dó, mực, đèn lồng | Thép, sọc cảnh báo, đèn LED |
| Font tiêu đề | (hiện có) | Cormorant Garamond 700 | Baloo 2 (kiểm bộ dấu) | Chakra Petch 700 |
| Nhạc | Điện tử vũ trụ | Dân ca rừng giả tưởng: sáo gỗ, đàn hạc, cello, trống khung | Dân gian Việt: sáo trúc, đàn tranh, trống cơm | Industrial: synth trầm, trống máy, bass |
| Tiếng chiến đấu | Laser, tàu | Lửa, gió, gỗ, đá, lá | Tre, gỗ, chuông đồng, giấy | Thép, súng nặng, điện, kim loại vỡ |
| Icon portal | 🛸 | 🐉 | 🏮 | ☄️ |

- Chung cả bốn game: font chữ trong trận **Be Vietnam Pro**; 4 màu ngữ nghĩa (đỏ nguy hiểm, cam khẩn, vàng kim tiền, xanh ngọc sức gõ); luật khung học (không rung, không bị hiệu ứng đè); lõi học `shared/learning`; luật lọc từ nhạy cảm.

### 1.2 Lời Gọi (TD) — hướng chủ đề

TD đã có thiết kế hình và âm riêng (`TYPING_DEFENSE_DESIGN.md` §22–24). Phần cần làm khi tách:

| Hạng mục | Làm gì | Dùng lại | Làm mới |
|---|---|---|---|
| Màn tiêu đề | Làng tre lúc hoàng hôn, đèn lồng sáng dần, tiếng dân gọi; tên "Lời Gọi" viết bút lông | Cảnh TD 22.9 | Bố cục, chữ tên |
| Vỏ UI | Khung giấy dó, viền mực, nút như con dấu son | HUD TD 23.5 | Lớp skin CSS |
| Âm | Bus và nhường tiếng TD 24.2; bộ tiếng tre, gỗ, chuông | Mã âm TD | File âm riêng qua `media:push` |
| Nhạc | Sáo trúc, đàn tranh, trống; 3 lớp theo ngày và đêm | — | Bản nhạc |
| Học | `gameId` `typing-defense` | Mã học TD 21 | — |

### 1.3 Tuyến Cuối (Sinh Tồn) — hướng chủ đề

Kế hoạch Sinh Tồn hiện đặt trận trong "hành lang không gian" và dùng lại 112 model quái, 12 tàu của Space. Nếu giữ y nguyên, Tuyến Cuối trông như một chế độ của Space. Có hai hướng:

| | **A. Khoa học viễn tưởng riêng (mặc định)** | B. Bỏ hẳn vũ trụ |
|---|---|---|
| Bối cảnh | **Vành Chân Trời:** một trạm thép cũ giữ hành lang cuối cùng ở mép hố đen. Công nghiệp, nặng, ấm (khác hẳn neon phiêu lưu của Space) | Một bức tường thành cuối cùng (giả tưởng khác rừng và làng) |
| Quái | Dùng lại model 8 họ của Space, phủ một **lớp vật liệu chung "Bầy Hố Đen"** (vân năng lượng cam nóng, viền đen hút sáng) để thành dòng hình riêng | Cần ~60 model Tripo mới |
| Tàu, súng | Dùng lại tàu và Draconis; bến súng thép mới (prop Tripo) | Model mới |
| Sân | Hành lang có sàn thép, sọc cảnh báo, hố đen ở chân trời | Mới hoàn toàn |
| Vỏ UI, âm | Thép, LED, Chakra Petch; synth industrial, súng nặng | Mới |
| Chi phí | Thấp: vài prop, một shader, ảnh UI, âm | Cao: ngang một game mới |

- **Mặc định: A.** Hỏi chủ dự án (Câu hỏi 3). Nếu anh chọn B, Tuyến Cuối xếp sau Rồng Giữ Ải về hình.

## 2. Trạng thái repo ngày 23/10/2026 (đọc, không đổi)

| Thứ | Trạng thái |
|---|---|
| Repo cha | Commit `e7e0e049`. 5 game là submodule `sinhvienaiti/*` (`.gitmodules`) |
| Space, nhánh làm việc | `feat/space-typing-2026-10-18` tại `b9d9bd79`. `main` đi sau rất xa (1.023 commit) |
| Sinh Tồn | `feat/survival-s0` tại `eff07a3e`, **đã commit S0**: `86f007e2` (sim), `5ed6aba2` (feedback dùng chung), `d1148572` (trang S0, đám đông, kịch bản), `eff07a3e` (đánh bóng). Đi trước nhánh làm việc 5 commit, không đi sau. Worktree `games/.wt-survival` chỉ còn 3 file tài liệu changelog chưa commit |
| TD | `feat/td-1a6` tại `4913aea1` (R2 xong). `feat/td-1a6-r3` cùng commit; worktree `games/.wt-td-1a6-r3` **đang có thay đổi chưa commit** trong `tests/td/*` (R3 đang chạy). So với nhánh làm việc của Space: đi trước 6, đi sau 5 (5 commit tài liệu Sinh Tồn) |
| Worktree cũ | `games/.wt-td-1a` (`feat/td-1a`), `games/.wt-td-1a6` (`4913aea1`) |
| Portal | `portal/public/games.json` có 5 game, chưa có trường `group` |
| Hạ tầng | `setup-nginx.sh` có 6 host; `dev.sh` có 5 đích; `scripts/play.sh`, `validate-play-mode.mjs` gắn cứng danh sách `dist`; `media/media.config.json` chỉ có một khối `game` (Space) |

Kế hoạch này cập nhật `research/codebase-and-split.md` (viết lúc S0 còn chưa commit).

## 3. Bố cục repo sau khi tách

```text
typing-game/                         repo cha
  portal/  admin/  infra/nginx/  scripts/  media/
  shared/
    learning/  vocabulary/  voice/  music/  typing-texts/
    game-kit/                        MỚI: nguồn chuẩn mã dùng chung (TS, không media, có test)
  scripts/
    sync-game-kit.mjs                MỚI: chép kit, ghi kit-manifest.json, --check, --drift
    models/                          MỚI: công cụ model và bộ Blender chuyển lên từ Space (hoặc thêm cờ --root --out --url-base)
  games/
    monkeytype/ vocab-shooter/ recall-typing/ karaoke-typing/    giữ nguyên
    space-typing/                    giữ nguyên; sau bước dọn thì bỏ src/td, src/survival
    dragon-hold/                     MỚI (repo con): src/kit/ (chép), src/{app,sim,content,stages,view,ui,audio}, tests/, docs/design/
    typing-defense/                  MỚI (repo con): lịch sử của src/td qua filter-repo; src/kit/ (chép)
    typing-survival/                 MỚI (repo con): lịch sử của src/survival + src/feedback; src/kit/ (chép)
```

- Mỗi game mới có: `package.json` riêng (Vite 7, TS, `three@0.170.0` ghim như Space), `index.html`, `src/kit/` (chép), test ranh giới riêng, `public/assets/<id>/` (media, không vào Git), `docs/`, `AGENTS.md`.
- **Test ranh giới** của mỗi game: chỉ import `src/**` của chính nó, `src/kit/**`, `three`, `three/examples/jsm/*`, `@fontsource/*`; không đường dẫn `../space-typing`; mọi file trong `src/kit/` khớp sha256 của `kit-manifest.json`.

## 4. Kit chung `shared/game-kit`

### 4.1 Thứ gì vào kit

| Thư mục kit | Chép từ (nhánh · file) | Đổi gì khi chép | Dùng bởi |
|---|---|---|---|
| `input/` | Space · `src/scene3d/keys.ts`, `src/logic.ts` (`typingText`, `normalizeWord`) | Bỏ type `Enemy`; type riêng | Cả ba |
| `vocab/` | Space · `src/vocabulary.ts`, `src/scene3d/words.ts` | `baseUrl` là tham số (mặc định `/vocabulary/`); lọc cờ `sensitive`, `mature` | Cả ba |
| `typing/` | `feat/td-1a6` · `src/td/typing/*` (router, letters, picker, scorer, distance, decks) | Hằng số thành `TypingConfig`; nhận RNG | Rồng Giữ Ải; Lời Gọi chuyển sang sau khi ổn |
| `platform/` | Space · `src/platform/{rng,frame-loop,safe-storage,canvas-state}.ts` | Không | Cả ba |
| `learning/` | Space · `src/learning/shared.ts` + `shared/learning/message-contract.mjs` | **`gameId` là tham số bắt buộc**; bridge postMessage; `shared-music`; tin `request-focus`; truy vấn `lookup` | Cả ba |
| `speech/` | Space · `src/speech.ts` | Cài đặt hẹp `{ enabled, rate, volume }` | Cả ba |
| `three/` | Space · `render3d/model-loader.ts`, `model-contracts.ts`, `scene3d/{hero,particles,materials,textures,util}.ts`, phần sân khấu của `space.ts`, `ui/title-guide-scene.ts` | `manifestUrl` là tham số, nạp nhiều manifest; `ModelKind` mở rộng (`units`, `props`); bỏ trời sao | Rồng Giữ Ải, Tuyến Cuối |
| `feedback/` | `feat/survival-s0` · `src/feedback/*` (8 file) | Hồ sơ theo game (`ship`, `dragon`, `td`) | Rồng Giữ Ải, Tuyến Cuối |
| `audio/` | Space · `scene3d/sfx.ts`, `audio/mix.ts`, `audio/credit-sound.ts` | Bộ trộn nhiều bus, nhận bảng âm | Cả ba |
| `ui/` | Mới | Màu ngữ nghĩa, biến `--ui`, font chữ trận, khung học cơ bản | Cả ba |
| `tools/` | Space · `scripts/visual/cdp-run.mjs`; plugin Vite phục vụ model chung (mới) | Chỉ dùng lúc build, kiểm | Cả ba |

- **Không vào kit:** `enemies/*`, `campaign/*`, `worlds/*`, `defense/*`, `ui/*` của Space, `types.ts`.
- **Phần hình Defense V4** (`src/defense/view/{camera,crowd,vfx,terrain,painter,sounds}.ts`) chỉ một game dùng: **chép thẳng** vào `games/dragon-hold/src/view/`, ghi nguồn đầu file. Không vào kit.

### 4.2 Cách chép và kiểm

| Lệnh (repo cha) | Làm gì |
|---|---|
| `pnpm kit:test` | Test đơn vị của kit (mỗi module), `gameId` bắt buộc |
| `pnpm kit:sync --target games/<id>` | Chép các module game đó khai trong `kit.config.json` vào `src/kit/`, ghi `kit-manifest.json` (phiên bản kit, commit nguồn, sha256 từng file) |
| `pnpm kit:check` | Mọi game ở bản kit mới nhất, hoặc ở bản ghim có ghi lý do |
| `pnpm kit:drift` | So kit với bản gốc trong Space, in tóm tắt khác biệt. **Chỉ để biết**, không chặn build |

- Trong mỗi game, `pnpm check` chạy kiểm sha256 của `src/kit/`: ai sửa tay là build đỏ.
- Mẫu cơ chế giống `scripts/sync-space-voice-contract.mjs` đang chạy.
- Đổi kit: sửa ở `shared/game-kit`, chạy `kit:test`, rồi `kit:sync` từng game, mỗi game một commit riêng trong repo con. Không agent nào sửa `src/kit/` trong game.

### 4.3 Space vẫn xây như cũ

- **Không đổi Space ở giai đoạn này** (00 D17). Không shim, không đổi import, không đổi test. Space vẫn build, chạy, phát hành như hôm nay.
- Lý do: cho Space dùng kit qua shim chạm vào lõi Space (phím, học, từ vựng, model, âm) mà không giúp gì cho ba game mới, lại có rủi ro đổi hành vi ngầm.
- **Khi nào mới làm shim:** sau khi ba game mới chạy ổn ít nhất một mốc, và `kit:drift` cho thấy một lỗi đã sửa ở kit mà Space cũng cần. Khi đó làm theo 05 §9.3 (shim giữ tên export, test cũ không sửa, so ảnh trước và sau).
- Sửa lỗi ở một bên (kit hoặc Space) thì ghi một dòng vào `shared/game-kit/DRIFT.md` để bên kia biết.

## 5. Media và model

| Việc | Chi tiết | Khi nào |
|---|---|---|
| Media nhiều game | `media/media.config.json`: khối `game` thành mảng `games[]`; `scripts/media/lib/sets.mjs` đọc `games[]`. Mỗi game có `dir`, `lock`, `modelsDir`, `modelsManifest` | Trước lần `pnpm media:push` đầu tiên của game mới |
| Công cụ model | `scripts/models/prepare-models.ts` và bộ Blender nhận `--root`, `--out`, `--url-base` (hoặc chuyển lên `scripts/models/` của repo cha) | Trước model Tripo đầu tiên của Rồng Giữ Ải |
| Rồng Giữ Ải | Model riêng ở `/assets/dragon-hold/models/`. **Chép 3 GLB Rồng** (draconis v2, v3 medium, v4) vào bộ media của game (D22) | M0 |
| Tuyến Cuối | Đọc model quái và tàu của Space qua **hợp đồng URL** `/assets/space-typing/models/`: alias nginx ở play, plugin Vite ở dev (không vào `dist`). Thêm lớp vật liệu "Bầy Hố Đen" bằng mã | Khi tách |
| Lời Gọi | Media riêng `public/assets/td/**` (đã có khối `.gitignore` trong Space), chuyển sang `/assets/typing-defense/` | Khi tách |
| Thư viện model chung | Giữ trong Space tới khi có model dùng chung cho từ hai game trở lên; lúc đó tính chuyển ra `shared/models` | Sau |

- Không đưa ảnh, âm, model vào Git ở bất kỳ repo nào. Repo cha và repo con đẩy qua SSH.

## 6. Tách Tuyến Cuối (Sinh Tồn) — làm ngay

| Bước | Việc | Ai | Cổng |
|---|---|---|---|
| T1 | Làn Sinh Tồn commit 3 file changelog còn lại ở `.wt-survival`; gắn nhãn `survival-s0` trên `eff07a3e` (hoặc commit mới) | Làn Sinh Tồn | Worktree sạch |
| T2 | Chủ dự án tạo repo `sinhvienaiti/typing-survival` (hoặc đồng ý bắt đầu bằng repo cục bộ, thêm remote sau) | Chủ dự án | Repo có |
| T3 | Trên một **bản clone mới** của Space (không dùng worktree đang làm), `git filter-repo` giữ: `survival.html`, `src/survival/`, `src/feedback/` (9 file), `tests/survival-*.test.ts`, `tests/survival/`, `tests/combat-feedback.test.ts`, `tests/feedback-{motion,numbers}.test.ts`, `scripts/survival/` (balance, replay), `scripts/visual/scenarios/survival-s0-*`, `docs/survival/`, mục `docs/changelog/*survival*` | Làn tách | Lịch sử chỉ còn các đường dẫn trên |
| T4 | Thay 8 import ra ngoài bằng `src/kit`: `platform/rng`, `scene3d/keys`, `scene3d/hero`, `scene3d/textures`, `render3d/model-loader`, `vocabulary`, `feedback/*` (giờ là `kit/feedback`) | Làn tách | `tsc` xanh; test ranh giới xanh |
| T5 | `survival.html` → `index.html`; `package.json`, `vite.config.ts` (cổng 3007), `AGENTS.md`; `gameId` `typing-survival` | Làn tách | Chạy được ở `localhost:3007` |
| T6 | Thêm submodule `games/typing-survival` vào repo cha (sau khi hạ tầng S3 xong) | Làn hạ tầng | `survival.typing-game.local` mở được qua portal |
| T7 | Chủ đề Tuyến Cuối (mục 1.3): màn tiêu đề, vỏ UI thép, bộ âm, nhạc, lớp vật liệu quái | Làn Tuyến Cuối | Chủ dự án duyệt ảnh và tai |

| Cổng tách Tuyến Cuối | Ngưỡng |
|---|---|
| Sim | Cùng seed ra cùng mã băm như trên nhánh `feat/survival-s0` |
| Kịch bản | Mọi kịch bản S0 xanh ở host mới |
| Học | Portal nhận sự kiện `typing-survival`; origin sai bị từ chối |
| Chủ dự án | Chơi S0 5 phút trên `survival.typing-game.local` |

- Sau T6: **không làm thêm việc Sinh Tồn trong Space.** Trang `survival.html` trong Space giữ tới bước dọn (mục 12).
- Phần Duel kiểu bến súng (Sinh Tồn S8) là chế độ của **Space** (Duel ở lại Space); nó dùng `feedback` từ bản gốc trong Space.

## 7. Tách Lời Gọi (TD) — ở ranh giới mốc

| Bước | Việc | Ai | Cổng |
|---|---|---|---|
| D1 | Làn TD làm xong R3 và commit ở `.wt-td-1a6-r3`. **Không ai khác đụng worktree này khi R3 đang chạy** | Làn TD | R3 qua cổng của TD |
| D2 | Gộp `feat/td-1a6-r3` → `feat/td-1a6`; gộp `feat/td-1a6` với nhánh làm việc của Space (phía Space chỉ có 5 commit tài liệu Sinh Tồn, ít xung đột) | Làn TD | `pnpm check` của Space xanh; `td-boundary` xanh |
| D3 | Báo đóng băng cho mọi làn dùng `.wt-td-*`: không commit TD mới vào Space; gắn nhãn `td-1a6-final` | Người điều phối | Thông báo đã gửi |
| D4 | Trên bản clone mới: `git filter-repo` giữ `td.html`, `src/td/`, `tests/td-*.test.ts`, `tests/td/`, `scripts/td/`, `docs/td/`, `scripts/visual/scenarios/td-*`, mục changelog TD | Làn tách | Lịch sử chỉ còn các đường dẫn trên |
| D5 | Thay 5 import (`scene3d/keys`, `logic.typingText`, `vocabulary` (2 hàm), `platform/rng`, `platform/frame-loop`) bằng `src/kit`; `td.html` → `index.html`; cổng 3006; `gameId` `typing-defense`; lệnh `td:balance`, `td:golden:update` | Làn tách | `tsc` xanh; test ranh giới xanh |
| D6 | Thêm submodule `games/typing-defense` | Làn hạ tầng | `td.typing-game.local` mở được qua portal |
| D7 | Vỏ chủ đề Lời Gọi (mục 1.2) | Làn Lời Gọi | Chủ dự án duyệt |

| Cổng tách Lời Gọi | Ngưỡng |
|---|---|
| Golden | Mã băm giống hệt bản `td-1a6-final` |
| Cân bằng | Báo cáo `td:balance` giống |
| Kịch bản | `td-1a-*` xanh ở `td.typing-game.local` |
| Chủ dự án | Chơi 5 phút |

- **Lịch sử học:** sự kiện TD cũ mang `gameId` `space-typing` (TD nằm trong Space). Không viết lại. Sau khi tách, TD gửi `typing-defense`. Độ thuộc tính theo từ nên không mất gì; thống kê theo game ghi mốc đổi.
- **Lưu:** không chuyển (D18). Trang `td.html` trong Space hiện một dòng "Lời Gọi đã chuyển sang trang mới" kèm liên kết, tới bước dọn.

## 8. Dựng khung Rồng Giữ Ải

| Bước | Việc | Cổng |
|---|---|---|
| R1 | Tạo `games/dragon-hold` (repo con; chưa có repo GitHub thì repo cục bộ, thêm remote sau) với Vite, `src/kit/` (chép), bridge học `gameId` `dragon-hold`, trang "Đang dựng", test ranh giới | `localhost:3005` chạy; test ranh giới xanh |
| R2 | Nối vào portal và nginx (bước S3) | `dragon.typing-game.local` mở được qua portal; bridge nhận sự kiện |
| R3 | Bắt đầu bản thử dọc M0 (DESIGN.md §9). Không chờ R2: M0 chạy độc lập ở cổng 3005, sự kiện học xếp hàng cục bộ | — |
| R4 | Ở M1: chuyển `docs/games/dragon-lane/` vào `games/dragon-hold/docs/design/`; repo cha giữ một dòng trỏ | Liên kết trong tài liệu đúng |

## 9. Portal: menu chung

### 9.1 Ba mục mới trong `portal/public/games.json`

```jsonc
{ "id": "dragon-hold", "name": "Rồng Giữ Ải", "description": "Hai Rồng giữ rừng sương: gõ từ trên đầu quái, đặt bẫy, lính chặn, nhà phép qua 520 ải.", "path": "/dragon-hold", "appUrl": "https://dragon.typing-game.local", "icon": "🐉", "group": "battle" },
{ "id": "typing-defense", "name": "Lời Gọi", "description": "Thủ thành làng chữ Văn Điền: giúp dân khi họ gọi, giữ làng khi đêm xuống.", "path": "/typing-defense", "appUrl": "https://td.typing-game.local", "icon": "🏮", "group": "battle" },
{ "id": "typing-survival", "name": "Tuyến Cuối", "description": "Giữ hành lang cuối ở mép hố đen: gõ từ nạp đạn cho bến súng, quét biển quái.", "path": "/typing-survival", "appUrl": "https://survival.typing-game.local", "icon": "☄️", "group": "battle" }
```

### 9.2 Việc khác ở portal

| Việc | Chi tiết |
|---|---|
| Trường `group` | `practice`: Monkeytype, Recall Typing, Karaoke Typing · `battle`: Vocabulary Shooter, Space Typing, Rồng Giữ Ải, Lời Gọi, Tuyến Cuối. Thêm `group` cho 5 mục cũ |
| Thanh nav | Vẽ theo nhóm ("Luyện gõ", "Game chiến đấu"), 8 game không chật. Kiểm `validate-portal-layout` ở 1280 và 1920 |
| Cầu học | Tự nhận 3 game mới vì đọc `games.json` (kiểm origin khớp `appUrl`, `gameId` khớp `id`). Thêm test: 3 `gameId` được nhận, origin sai bị từ chối |
| Focus | Khi nạp game, portal gọi `frame.focus()`; khi nhận `typing-game:request-focus` thì focus iframe (dragon-lane 06 §2) |
| Truy vấn học | Thêm `typing-game:learning:v1:lookup` theo danh sách ≤ 200 `entityId`, trả cả `recentSamples` (dragon-lane 01 §6.8) |
| Smart Review | Adapter cho game mới làm sau (Rồng Giữ Ải ở mốc M4) |
| Giọng nói | `voice-bootstrap.ts` giữ cho Space; game mới không dùng chế độ nói ở bản đầu |

## 10. Hạ tầng: dev, play, nginx

Làm **một PR cho cả ba game** để chủ dự án chạy `setup-nginx.sh` một lần.

| File | Thêm |
|---|---|
| `infra/nginx/typing-game.local.dev.conf` | 3 khối `server`: `dragon.` → proxy 127.0.0.1:3005, `td.` → 3006, `survival.` → 3007; WebSocket HMR như các game Vite khác |
| `infra/nginx/typing-game.local.play.conf` | 3 khối `server` phục vụ `games/<id>/dist`; alias `/vocabulary/`, `/typing-texts/` tới `shared/`; `survival.` thêm alias `/assets/space-typing/models/` tới thư mục model của Space; thêm 3 host vào khối `listen 80` chuyển hướng |
| `scripts/setup-nginx.sh` | 3 host vào mảng `HOSTS`; tạo lại chứng chỉ có 3 tên mới; thêm vào `/etc/hosts`. **Chủ dự án chạy một lần (sudo)** |
| `package.json` cha | `dev:dragon`, `dev:dragon:app`, `build:dragon`; `dev:td`, `dev:td:app`, `build:td`; `dev:survival`, `dev:survival:app`, `build:survival`; thêm 3 app vào `dev` (concurrently) và `build:local`; thêm 3005–3007 vào `cleanup-dev-ports`; `kit:test`, `kit:sync`, `kit:check`, `kit:drift` |
| `dev.sh` | Đích `dragon`, `td`, `survival`; `all` gồm cả ba |
| `play.sh`, `scripts/play.sh` | `build_if_needed` cho 3 game; danh sách `dist` |
| `scripts/bootstrap.sh` | Cài phụ thuộc, `git submodule update --init` cho 3 repo mới |
| `scripts/validate-play-mode.mjs` | 3 host, 3 `dist` |
| `.gitmodules` | 3 submodule `games/dragon-hold`, `games/typing-defense`, `games/typing-survival` |
| `media/media.config.json`, `scripts/media/lib/sets.mjs` | `games[]` (mục 5) |
| `AGENTS.md`, `docs/AGENT_SKILLS_SETUP.md` | Bảng game nào dùng skill nào. Skill dự án hiện có (`.agents/skills`) viết cho Space; game mới dùng skill Game Studio, `threejs-*` và tài liệu thiết kế của chính nó |

- Cổng đang dùng: 3000–3004 (game), 3005–3007 (Rồng Giữ Ải, Lời Gọi, Tuyến Cuối), 3008 (Tu Tiên Thủ Ải), 3100 (portal), 3199 (admin), 3014 (duel), 3016 (account), 3095–3098 (công cụ).

**Game thứ tư: Tu Tiên Thủ Ải** (25/10/2026): id và `gameId` `immortality-cultivation`, repo `sinhvienaiti/immortality-cultivation` (submodule `games/immortality-cultivation`, `branch = main`), cổng dev **3008** (`--strictPort`, cờ cổng chỉ ở `pnpm dev` của game), host `tutien.typing-game.local`. Nối repo cha theo đúng bảng trên (commit `6c44135b`, `f160d4bc`). Tài liệu thiết kế ở [`docs/games/tu-tien/`](tu-tien/README.md) (canon `00-canon.md`, kế hoạch `M0A_PLAN.md`); chuyển vào repo game ở M1.

## 11. Những gì ở lại Space Typing

| Ở lại | Ghi chú |
|---|---|
| Campaign 2D, Campaign 3D, Defense V4 (`src/defense`, `defense.html`) | Gắn chặt với `enemies/*`, `campaign/*`, `worlds/*` của Space |
| Duel PvP, kể cả kiểu bến súng (Sinh Tồn S8) | Máy chủ Duel ở cổng 3014 |
| Chế độ Voice, Hybrid; `voice-bootstrap` của portal | |
| Tích hợp Admin (`/api/admin/space-typing/`), tàu, thế giới, nhân vật, trang bị Space | |
| Thư viện model chung `/assets/space-typing/models/` | Tới khi chuyển ra `shared/models` |
| Bản gốc của `keys`, `vocabulary`, `learning/shared.ts`, `speech`, `model-loader`, `hero`, `sfx`, `src/feedback/kill-translation.ts` | Space không dùng kit ở giai đoạn này |
| Sự kiện học `gameId` `space-typing` | |

| Rời Space | Sang |
|---|---|
| `src/td`, `td.html`, `tests/td*`, `scripts/td`, `docs/td` | `games/typing-defense` |
| `src/survival`, `survival.html`, `docs/survival`, phần lớn `src/feedback` | `games/typing-survival` (feedback cũng vào kit) |
| Phần hình Defense V4 | **Chép** sang `games/dragon-hold` (Space vẫn giữ bản gốc) |

## 12. Dọn Space (bước cuối)

- **Khi nào:** sau khi Lời Gọi và Tuyến Cuối qua cổng tách và chạy ổn ít nhất 2 tuần, hoặc khi chủ dự án đồng ý.
- **Làm gì:** bỏ `td`, `survival` khỏi `rollupOptions.input`; xóa `src/td`, `src/survival`, file `src/feedback/*` không còn ai dùng (giữ `kill-translation.ts`), test và script liên quan; bỏ `td-boundary`; tài liệu trỏ sang repo mới; changelog Space theo luật changelog.
- **Cổng:** `pnpm check` của Space xanh; kịch bản hình Campaign 3D và Defense chụp trước và sau không lệch; build Space không còn mã TD, Sinh Tồn.

## 13. Thứ tự và làn song song

| Bước | Việc | Bắt đầu sau | Chỉ ghi vào | Agent | Cổng |
|---|---|---|---|---|---|
| S0 | Chủ dự án duyệt tên, tạo 3 repo GitHub (hoặc cho bắt đầu cục bộ) | Ngay | — | — | Tên chốt |
| S1 | `shared/game-kit` + `sync-game-kit.mjs` + test kit | Ngay | `shared/game-kit`, `scripts/sync-game-kit.mjs` | 2 (một chép, một viết test) | `kit:test` xanh; `--check` bắt được file bị sửa |
| S2 | Media nhiều game, công cụ model | Ngay | `media/`, `scripts/media`, `scripts/models` | 1 | `media:test` xanh; manifest Space sinh lại giống từng byte |
| S3 | Hạ tầng và portal (mục 9, 10), một PR | Ngay | `infra/`, `portal/`, script repo cha | 1 | 3 host chạy dev và play; `validate-play-mode`, `validate-portal-layout` xanh |
| S4 | Khung Rồng Giữ Ải (R1) rồi M0 | Ngay (R1 cần S1 bản đầu) | `games/dragon-hold` | Theo DESIGN.md §9 (~10 agent) | Cổng M0 |
| S5 | Tách Tuyến Cuối (T1–T6) | S1 có `feedback`, `platform`, `input` | `games/typing-survival` | 2 | Cổng mục 6 |
| S6 | Tách Lời Gọi (D1–D6) | R3 của TD xong | `games/typing-defense` | 2 | Cổng mục 7 |
| S7 | Chủ đề riêng Lời Gọi, Tuyến Cuối (T7, D7) | S5, S6 | Repo con tương ứng | 1–2 mỗi game | Chủ dự án duyệt |
| S8 | Dọn Space | S5, S6 qua cổng + 2 tuần | `games/space-typing` | 1 | Mục 12 |
| — | Phản biện | Mỗi cổng | Chỉ đọc | 1 mỗi làn | — |

- S1, S2, S3, S4, S5 chạy **cùng lúc**. Chỉ S6 chờ làn TD. Không bước nào chặn bản thử dọc của Rồng Giữ Ải.
- Mỗi bước một nhánh, một PR. Không đụng `games/.wt-*` đang có người làm. Không đưa media vào Git.

## 14. Rủi ro

| Rủi ro | Giảm bằng |
|---|---|
| Kit và Space lệch nhau theo thời gian | `kit:drift` báo; `DRIFT.md`; làm shim khi lệch gây lỗi thật |
| Tách TD khi R3 đang làm dở | Chỉ tách sau D1–D3; làm trên bản clone mới |
| Tuyến Cuối trông như một chế độ của Space | Hướng A: vỏ thép, lớp vật liệu "Bầy Hố Đen", âm industrial; hoặc hướng B nếu chủ dự án muốn |
| Model chung nằm trong Space | Hợp đồng URL cố định; test nạp manifest ở mỗi game; Rồng Giữ Ải chép 3 GLB Rồng vào media riêng |
| Thêm host cần sudo, tạo lại chứng chỉ | Gộp 3 host vào một lần chạy `setup-nginx.sh` |
| Thanh nav portal chật | Trường `group`, nav theo nhóm, kiểm bố cục |
| `gameId` sai làm mất sự kiện học | Kit bắt buộc `gameId`; test bridge cho 3 game |

## 15. Câu hỏi cho chủ dự án (đã có mặc định)

| # | Câu hỏi | Mặc định |
|---|---|---|
| 1 | Tên: Rồng Giữ Ải (`dragon-hold`), Lời Gọi (`typing-defense`), Tuyến Cuối (`typing-survival`)? | Dùng đúng các tên này |
| 2 | Ba repo GitHub mới công khai hay riêng tư? Ai tạo? | Công khai như 5 repo cũ; chủ dự án tạo; trong lúc chờ, làm repo cục bộ |
| 3 | Tuyến Cuối: giữ khoa học viễn tưởng nhưng có dòng hình riêng (A), hay bỏ hẳn vũ trụ (B)? | A |
| 4 | Không cho Space dùng kit (không shim) ở giai đoạn này? | Đúng; chỉ báo độ lệch |
| 5 | Không chuyển dữ liệu lưu TD, Sinh Tồn sang host mới? | Đúng, vì chưa có người chơi thật |
| 6 | Nav portal gom thành "Luyện gõ" và "Game chiến đấu"? | Có |
| 7 | Thư viện model chung giữ trong Space? | Có; 3 GLB Rồng chép vào media của Rồng Giữ Ải |
| 8 | Dọn Space sau 2 tuần ổn định của hai game tách? | Có |
