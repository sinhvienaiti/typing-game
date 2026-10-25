# Mỗi game triển khai riêng (26/10/2026)

> **Quy tắc của chủ dự án (26/10, "lưu ý quan trọng"):** "đảm bảo sau này mỗi game đều có thể triển khai riêng mà không phải phụ thuộc vào nhau, chứ không sau này cứ phải đẩy toàn bộ code và media cùng nhau thì sẽ khiến site bị rất nặng".
>
> **Trả lời ngắn: làm được, và gói mỗi game nhẹ hơn nhiều so với kế hoạch 25/10.**
> 1. Ba game dùng kit (Rồng Giữ Ải, Lời Gọi, Tuyến Cuối) **build được một mình hôm nay**: đã clone mới từ GitHub ra ngoài repo cha, cài và build đều qua.
> 2. Không game nào tải file của game khác, **trừ Tuyến Cuối** (mượn model của Space).
> 3. Năm chỗ còn chặn: từ vựng chỉ nginx phục vụ từ repo cha; nguồn portal ghi cứng; Tuyến Cuối mượn model Space; media chỉ tải được bằng công cụ repo cha; test của Lời Gọi và Tuyến Cuối đọc `../../../../shared`.
> 4. Sau khi sửa: Rồng **14,50 MiB** (147 file), Lời Gọi **1,11 MiB** (51 file), Tuyến Cuối **12,36 MiB** (58 file, thay vì 365 MiB).
>
> **Nguồn:** audit chỉ đọc ngày 26/10 (workflow `deploy-independence-audit`): bốn agent kiểm mã, một agent clone mới từng game ra thư mục không có repo cha rồi cài, build, test và mở bằng Chrome. Số byte đo trên ổ đĩa và trong log mạng của Chrome. Không sửa, cài hay build gì trong `games/<id>` hay repo cha. Bằng chứng ở mục 16.
>
> **Ngoài phạm vi:** Tu Tiên Thủ Ải đang tạm dừng, không kiểm. Khi làm lại thì áp cùng quy tắc; alias model Space của Tu Tiên trong nginx thì bỏ.

## 1. Quy tắc

"Triển khai riêng" nghĩa là đủ cả tám điều sau:

1. **Mỗi game một gói** `.deploy/<id>/`, build từ repo của chính game đó. Gói chỉ chứa file game đó thật sự tải.
2. **Build, test, đóng gói chạy được trên bản clone riêng** của repo game. Không cần repo cha, không cần game khác.
3. **Không URL nào trỏ sang deploy khác:** không `/assets/<game khác>/`, không alias nginx chéo game, không fetch từ nguồn portal.
4. **Nội dung dùng chung (từ vựng) được chép vào repo game** ở bản ghim, chỉ phần game dùng (mục 8).
5. **Hợp đồng duy nhất giữa các deploy là postMessage với portal.** Nguồn portal là biến lúc build (mục 9).
6. **Mở game một mình, không qua portal, vẫn chơi được** (mục 10).
7. **Sửa một game thì chỉ deploy lại game đó.** `games.json` của portal chỉ đổi khi tên miền của game đổi.
8. **Repo cha chỉ cần khi cập nhật** kit (`kit:sync`) hoặc từ vựng (`vocab:sync`). Không bao giờ cần khi build hay deploy.

## 2. Hôm nay: clone riêng, không có repo cha

Clone từ GitHub ngày 26/10: Rồng `origin/main` 235a43f, Lời Gọi 7d6adf4, Tuyến Cuối 7e53835. Node 24.22.0, pnpm 11.21.0.

| Game | `pnpm install --frozen-lockfile` | `pnpm build` | `pnpm test` | `verify-kit` | Mở một mình (không `/vocabulary/`, không media) | Request sang nguồn khác |
|---|---|---|---|---|---|---|
| Rồng Giữ Ải | OK | OK: 41 file, 1,73 MiB, không media | **373/373 qua** | OK (73 file) | **Không chơi được:** 0 chữ, quái không gắn từ | 0 |
| Lời Gọi | OK | OK: 45 file, 741.889 B | **Hỏng 9 test** (ENOENT `shared/vocabulary`) | OK (31 file) | Chơi được, dùng từ dự phòng | 0 |
| Tuyến Cuối | OK | OK: 45 file, 1.385.556 B | **Hỏng 5/11 file test** (ENOENT) | OK (59 file) | Chơi được, từ dự phòng, hình thay model | 0 |
| Space Typing | chưa clone riêng | qua khi thiếu media Drive, nhưng gói kèm hình thay | hỏng (đọc `../../../shared`) | không dùng kit | Chơi được, mất học và Voice (mục 6) | 0 |

- Font lấy từ `@fontsource` của chính game, có lockfile riêng. Không file nào lấy từ `node_modules` của gói khác.
- Kit chép sẵn trong `src/kit` là ổn: `tests/boundary.test.ts` của mỗi game chặn import ra ngoài `src/**`, `three`, `@fontsource/*`.
- Cả ba game đều cần được phục vụ ở **gốc một nguồn** (subdomain): `base: "/"` (Rồng `vite.config.ts:17`, Lời Gọi `:34`, Tuyến Cuối `:23`) cộng các URL tuyệt đối `/assets/<id>/`, `/vocabulary/`.

## 3. Rồng Giữ Ải

| # | Phụ thuộc ngoài repo | Loại | Ở đâu | Byte | Sửa |
|---|---|---|---|---:|---|
| 1 | **Từ vựng `/vocabulary/`.** Không có bộ từ dự phòng: tải hỏng thì bộ bài 0 chữ, màn không chơi được, người chơi không được báo gì | runtime, **chặn chơi** | `src/kit/vocab/vocabulary.ts:9,397,505`; `src/app/learning.ts:315-322` (chỉ `console.warn`); `src/typing/deck.ts:53`; `src/app/app.ts:779-797` (không kiểm bộ rỗng). Hôm nay chỉ nginx phục vụ: `infra/nginx/typing-game.local.play.conf:152-156` | 2.666.953 (102 file) | Chép `index.json`, 100 level, `ATTRIBUTION.md` vào `public/vocabulary/` (mục 8). Thêm thông báo lỗi rõ khi bộ bài rỗng, hoặc bộ từ dự phòng như Lời Gọi |
| 2 | **Nguồn portal ghi cứng** `https://typing-game.local` | runtime, chỉ khi nhúng trong portal | `src/kit/learning/contract.ts:22`; `src/kit/learning/bridge.ts:115,248,292`; `src/app/app.ts:208` (không truyền `parentOrigin`) | 0 | Biến build (mục 9) |
| 3 | Plugin dev phục vụ `../../shared` | chỉ dev | `vite.config.ts:4,8,18`; `src/kit/tools/vite-shared-plugin.ts:78` (`apply: "serve"`) | 0 | Bỏ plugin khi đã có `public/vocabulary/`. Hôm nay `pnpm dev` ở bản clone riêng trả 404 cho `/vocabulary/` |
| 4 | **GLB Rồng:** media của chính game, đường cứng, không manifest, không `?v=` | runtime (media riêng) | `src/view/heroes.ts:37-41,83-86`; High là mặc định (`src/app/app.ts:182`) | 10.730.220 (4 file dùng) | Chỉ gói 4 file dùng. `draconis-v3` (5.928.068 B) không mã nào tải (`HERO_MODELS.fireInferno` chưa dùng): để ra ngoài tới M0c. Đổi sang tên có hash hoặc thêm `?v=` |
| 5 | **Tải media để đóng gói:** `media.md5` ở trong game, nhưng công cụ tải và cấu hình Drive ở repo cha | đóng gói | `media.md5` (420 dòng: 414 `art-src` không bao giờ deploy, 6 GLB `public/`); `scripts/media/media.mjs` và `media/media.config.json:23-32` của repo cha. `modelsManifest` trỏ tới file không có | 16.658.288 (6 file tải hôm nay) | Lệnh tải media riêng trong repo game, chỉ dòng `public/` (mục 11). Bỏ `modelsManifest` cũ hoặc tạo manifest thật |
| 6 | Gốc âm thanh có trong bundle nhưng không file nào được tải (mọi âm tổng hợp bằng mã) | không | `src/audio/catalog.ts:179`; `src/kit/audio/util.ts:3` (`/assets/audio/` dùng chung mọi game) | 0 | Không cần gì. Khi có âm thật: để ở `/assets/dragon-hold/audio/`, **không** dùng gốc mặc định `/assets/audio/` của kit |
| 7 | Hành vi chỉ nginx có: alias từ vựng, cache tách theo `/assets/`, fallback SPA, alias `/typing-texts/` | runtime | `play.conf:146-165`; `dev.conf:194-220` | 692.920 (typing-texts, không cần) | `_headers` của Worker (mục 11). **Không chép `shared/typing-texts`.** Không bật `not_found_handling` SPA |
| 8 | Công cụ dev và test giả định máy nhà | công cụ | `vite.config.ts:23` (`allowedHosts`); `scripts/visual/cdp-run.mjs:38-43` (đường Chrome) | 0 | Không cần cho deploy. `scripts/balance/deck.ts` có sẵn 100 từ, không đọc `shared/` |

**Ghi chú:**
- **Hôm nay game chỉ tải level 1 và 2** (47.613 B), vì `app.ts:209` không truyền `vocabLevel` và `saveVocabLevel` (`learning.ts:471`) chưa ai gọi. Level lưu theo người chơi (`learning.ts:315`) và bộ chọn level sau này cần bất kỳ level nào, nên chép đủ 100 level (2.651.657 B).
- **Không cần cho Rồng:** `lookup.json`, `topics/`, `grammar/`, `parts-of-speech/`, `curriculum/`, `schema.json` = 818.058 B, 14 file.
- **`_headers` của Cloudflare gộp giá trị của mọi luật khớp.** `assetsDir: "assets"` của Vite trùng tiền tố `/assets/` với media, nên luật `/assets/dragon-hold/*` phải gỡ header immutable (`! Cache-Control`) rồi mới đặt `no-cache`. Cách khác: dời đầu ra của Vite bằng `build.assetsDir`.
- **Fallback SPA che file thiếu:** với fallback (đã thấy ở `vite preview`), GLB hay file từ vựng thiếu trả về `index.html` mã 200, game báo "Unexpected token '<'".
- **Lần chơi đầu ở High: 20 request, 8.948.385 B** (8.067.219 B gzip). Ngân sách của Rồng trong HOSTING_PLAN §7 là ≤ 5 MB. Bậc Medium (3.030.508 B GLB) đưa lần đầu xuống khoảng 4,3 MB. Đây là việc làm nhẹ, không phải việc tách.

## 4. Lời Gọi

| # | Phụ thuộc ngoài repo | Loại | Ở đâu | Byte | Sửa |
|---|---|---|---|---:|---|
| 1 | **Từ vựng `/vocabulary/`** (index và level 1–5). Thiếu thì dùng khoảng 150 từ dự phòng, chỉ level 1, không nghĩa, không IPA; HUD ghi "Từ dự phòng (máy chủ không có từ vựng)" | runtime | `src/kit/vocab/vocabulary.ts:9,397,505`; `src/app/vocab.ts:12` (`VOCAB_LEVELS = 5`), `:16-21,32-37`; `src/main.ts:143,295`; nginx `play.conf:174-178` | 123.832 (7 file) | Chép `index.json` 12.195, `levels/001`–`005` (17.372 + 18.046 + 18.363 + 26.688 + 28.067), `ATTRIBUTION.md` 3.101 vào `public/vocabulary/` |
| 2 | **Test và script balance, replay đọc** `../../../../shared/vocabulary`. `pnpm check` hỏng ở bản clone riêng | công cụ | `tests/td/typing.ts:23` (dùng bởi td-boss, td-calls, td-content, td-flow, td-learn, td-pace, td-r2, td-sim-perf, td-balance-gates); `scripts/td/replay.ts:31`; qua `realDeck`: `scripts/td/balance.ts:16`, `balance-worker.ts`, `boss-tune.ts`, `retry-log.ts` | 120.731 | Đọc bản chép `public/vocabulary/`. Test, replay và trang dùng cùng byte. Hash bộ bài vào hash thế giới, nên phải ghim (mục 8) |
| 3 | Plugin dev phục vụ `../../shared` | chỉ dev | `vite.config.ts:36`; `vite-shared-plugin.ts:61,78` | 0 | Bỏ plugin; Vite tự phục vụ `public/`. Lời Gọi không bao giờ gọi `/typing-texts/` |
| 4 | **Nguồn portal ghi cứng** | runtime, chỉ khi nhúng | `src/kit/learning/contract.ts:22`; `bridge.ts:115,248,292`; `src/app/learning.ts:15`; `src/main.ts:169` (`requestFocus`) | 0 | Biến build (mục 9) |
| 5 | **Ảnh nền màn tiêu đề:** file media duy nhất game tải. Nằm ngoài Git, chỉ công cụ media của repo cha tải được. Thiếu thì giữ nền SVG | runtime (media riêng) | `src/ui/title.ts:19,180-185`; `.gitignore:26`; `media.md5:403` | 335.236 | Lệnh tải riêng một file này trong script deploy của game, kiểm md5 dòng 403. URL không phiên bản: `no-cache` hoặc tên có hash |
| 6 | **68 GLB không dùng bị Vite chép vào `dist`.** Game là canvas 2D; chạy từ màn tiêu đề tới vào trận: 0 request GLB. Chiếm 94,8 % `dist` hôm nay | đóng gói | `public/assets/typing-defense/models/**` (34 High 13.677.892 B + 34 Medium 6.067.760 B); `manifest.json` 22.968 B; `dist/.vite/manifest.json` 14.925 B (`vite.config.ts:56`) | 19.783.545 | Để `assets/typing-defense/models/**` và `.vite/` ra ngoài gói tới khi bản 3D thật sự tải model. Khi đó chỉ gói model được tải, một bậc mỗi máy |
| 7 | Hành vi chỉ nginx có | runtime | `play.conf:169-194` (alias từ vựng `:174-178`, `no-cache` `:191`, immutable `:192`, fallback `:193`) | 0 | `_headers`: `/assets/typing-defense/*` `no-cache`; JS, CSS, woff2 có hash `immutable`; `/vocabulary/*` cache ngắn. Không fallback SPA (game chỉ dùng `?title=0`, `?sandbox=`, `?untrusted=1`) |
| 8 | Phiên bản Node chỉ ghim ở repo cha (`engines.node >=24 <25`) | build | `package.json` của game có `packageManager` nhưng không `engines` | 0 | Thêm `engines.node` hoặc `.nvmrc` để CI của game dùng Node 24 |
| 9 | Công cụ Blender tìm `static_model_tools.py` của repo cha | công cụ (làm art) | `scripts/models/blender/td_rig_common.py:26-36` | 0 | Không cần cho deploy |

**Ghi chú:**
- Trang tải từ vựng với `cache: "no-store"` (`vocabulary.ts:397,505`), nên mỗi lần mở tải lại khoảng 27,6 kB gzip.
- Chunk công cụ dev (`window.__td`) vẫn được tải ở bản production (`src/main.ts:229-244`). Không phải phụ thuộc, nhưng nên tắt ở bản online.
- Giữ `td.<tên-miền>` cùng tên miền gốc với portal. Nếu không, `localStorage` trong iframe bị tách (`td.settings`, `td.campaign`, `typing-defense:learning-queue:v1`…) và hàng đợi học không tới portal.

## 5. Tuyến Cuối

| # | Phụ thuộc ngoài repo | Loại | Ở đâu | Byte | Sửa |
|---|---|---|---|---:|---|
| 1 | **Thư viện model của Space** qua URL `/assets/space-typing/models/manifest.json`. Trình duyệt tải manifest 131.018 B (189 model) rồi 6–7 GLB. Thiếu thì chạy bằng hình thay | runtime, **chéo game** | `src/view/models.ts:6-8` (hằng kit `SPACE_MODEL_MANIFEST_URL`, `src/kit/three/model-loader.ts:19`); id ở `src/view/crowd.ts:33-39`, nạp `:139-145`; `src/view/ship.ts:47-53`; nginx `play.conf:219-223`, `dev.conf:283-286` | 11.501.400 (7 GLB) | Chép riêng 7 model vào media của game (bảng dưới). Đổi `models.ts:8` sang `/assets/typing-survival/models/manifest.json`. File này là mã game, không phải kit |
| 2 | **Bậc model luôn là High**, kể cả khi chọn Low | runtime | `src/view/crowd.ts:142`, `src/view/ship.ts:50` (`pickModelTier(entry, "high")`) | 3.969.672 (thêm Medium) | Truyền bậc người chơi chọn; Low bỏ 3D như chú thích của kit |
| 3 | Plugin dev đọc thư mục model của repo Space bên cạnh | chỉ dev | `vite.config.ts:16,24`; `vite-shared-plugin.ts:21-24,66-69,78` | 0 | Bỏ `modelsDir`, `modelsUrl`, `SPACE_MODELS_DIR` sau khi chép |
| 4 | **Từ vựng `/vocabulary/`** (index, level 1–3). Thiếu thì dùng khoảng 60 từ dự phòng; hash bộ bài đổi (28a73ed5 thay vì 7f073fa2) | runtime | `src/app/vocab.ts:43-48`; `vocabulary.ts:9,397,505`; nginx `play.conf:203-207` | 69.077 (5 file) | Chép `index.json`, `levels/001`–`003`, `ATTRIBUTION.md` vào `public/vocabulary/` |
| 5 | Plugin dev phục vụ `../../shared` | chỉ dev | `vite.config.ts:10,24` (env `SHARED_DIR`) | 0 | Bỏ `sharedRoot` |
| 6 | **Test và balance đọc** `../../../../shared/vocabulary/levels/001-003.json` | công cụ | `tests/survival/typist-bot.ts:275`; `tests/survival/bot.ts:49`; `scripts/replay.ts:34` (qua `../../../shared`); gọi từ `scripts/balance.ts:155`, `scripts/s0-trace.ts:21`, `scripts/balance-lib.ts:198` | 53.781 | Đọc bản chép `public/vocabulary/`. Việc này cũng ghim `tests/golden/s0-trace.json` khỏi thay đổi của từ vựng chung |
| 7 | **Nguồn portal ghi cứng.** Chỉ dùng `sendAttempt` | runtime, chỉ khi nhúng | `src/kit/learning/contract.ts:22`; `bridge.ts:115,248,292`; `src/app/learning.ts:18` | 0 | Biến build (mục 9) |
| 8 | Hành vi chỉ nginx có; trình kiểm play mode bắt buộc alias model Space | runtime | `play.conf:196-228`; `dev.conf:260-298`; `scripts/validate-play-mode.mjs:40-46` | 0 | `_headers`: `/assets/typing-survival/*` `no-cache`. `manifest.json` phải là `application/json` (`model-loader.ts:127` từ chối kiểu khác). Sau khi chép: bỏ alias ở hai file nginx và trong trình kiểm |
| 9 | **Media chỉ tải được từ repo cha.** Game chưa có `public/`, chưa có `media.md5`; `media.config.json:45-54` đã chừa chỗ | đóng gói | `media/media.config.json:45-54`; `.gitignore:12`; `play.sh:324-334` (không theo dõi `.media-pulled` của game) | 11.501.400 | Sau khi chép và `media:push`: script deploy chỉ tải bộ `media.md5` của Tuyến Cuối, không bao giờ của Space |

**Không dùng, không gói:** `/typing-texts/`, âm thanh của Space (mọi âm tổng hợp bằng mã), texture của Space (vẽ trên canvas). Gốc `/assets/audio/` của kit có trong bundle nhưng không được tải.

### 5.1. Bộ model riêng của Tuyến Cuối

Thay cho cả thư viện của Space (379 file, 377.266.038 B = 359,8 MiB). Đo trên ổ ngày 26/10, khớp log mạng Chrome cho cả hai phi công.

| Model id | Dùng cho | High (B) | Medium (B) |
|---|---|---:|---:|
| `ships/vanguard` | phi công Vanguard (mặc định) | 2.748.648 | 881.140 |
| `heroes/draconis-v3` | phi công Draconis | 4.362.212 | 1.565.856 |
| `enemies/rainbow-mine-3d` | Mìn | 827.972 | 301.076 |
| `enemies/rainbow-scout-3d` | Trinh sát | 1.005.380 | 345.936 |
| `enemies/rainbow-tank-3d` | Trâu, Đầu Đàn | 950.164 | 347.168 |
| `enemies/rainbow-shield-3d` | Khiên | 991.376 | 311.644 |
| `enemies/rainbow-splitter-3d` | Tách và mảnh | 615.648 | 216.852 |
| **Cộng 7 model** | | **11.501.400** | **3.969.672** |
| Manifest riêng (đã dựng thử) | | 4.111 | |

```bash
SPACE_MANIFEST=games/space-typing/public/assets/space-typing/models/manifest.json
pnpm models:prepare --root games/typing-survival --import $SPACE_MANIFEST \
  --only ships/vanguard,heroes/draconis-v3,enemies/rainbow-mine-3d,enemies/rainbow-scout-3d,enemies/rainbow-tank-3d,enemies/rainbow-shield-3d,enemies/rainbow-splitter-3d \
  --tiers high            # thêm ",medium" khi bậc model theo chất lượng (dòng 2 bảng trên)
pnpm media:push --only runtime
```

- Cùng đường Rồng Giữ Ải đã làm cho Draconis (MEDIA_AND_MODELS §6, quyết định D22). Commit `manifest.json` và `media.md5` trong repo `typing-survival`. GLB không vào Git.
- `?v=` trong manifest của Space là tiền tố sha256 của nội dung file (đã kiểm `rainbow-mine-3d`, `vanguard`), nên bản chép giữ khóa cache đúng.
- **Không chép id dự phòng:** `rainbow-mine-lod` 711.832, `rainbow-scout-lod` 951.304, `draconis-v2` 4.009.564, `draconis` 3.677.336 (cộng 9.350.036 B). Chúng chỉ được hỏi khi id chính vắng mặt. Vắng trong manifest thì game bỏ qua, không request.
- **Đã dựng thử trong scratch:** bản build chỉ đổi `models.ts` chỉ request `/assets/typing-survival/...`; cả 6 cờ model đều `true` cho cả hai phi công.
- **Lần chơi đầu:** High: Vanguard 7.139.188 B GLB, Draconis 8.752.752 B. Có Medium: 2.403.816 và 3.088.532 B. Ngân sách của Tuyến Cuối (HOSTING_PLAN §7) là ≤ 4 MB, nên **nên nhập cả Medium** và cho bậc theo chất lượng.
- **Màn sau** (`docs/BUILD_S1.md:34`: 9 quái cầu vồng và 2 boss nữa): 15.780.416 B High, 5.506.456 B Medium trong thư viện Space. Chép từng model khi mã bắt đầu tải nó, không chép trước.
- Sau khi Tuyến Cuối có bản riêng, **không còn game nào đọc thư viện model của Space**. Space đổi gói, nén lại hay đổi `?v=` thoải mái mà không làm hỏng game khác. Bỏ hằng `SPACE_MODEL_MANIFEST_URL` khỏi kit (hoặc ghi rõ chỉ dùng ở dev).

## 6. Space Typing

Space là deploy riêng của chính nó (`space.<tên-miền>`, một Worker cho file tĩnh và API tài khoản). Không game nào khác đọc file của Space sau mục 5.1.

| # | Phụ thuộc ngoài repo | Loại | Ở đâu | Byte | Sửa |
|---|---|---|---|---:|---|
| 1 | **Từ vựng và bài gõ** ở `/vocabulary/`, `/shared/typing-texts/`. Chỉ nginx phục vụ. Thiếu thì chơi bằng từ có sẵn (`main.ts:11366`), bài gõ hỏng (`main.ts:1870`) | runtime | `src/vocabulary.ts:7-12`; `src/typing-text.ts:50`; `play.conf:128-137`; `dev.conf:166-175`; `scripts/dev/vite.worktree.config.ts:24` | 3.873.325 (127 file) | Chép bản ghim vào `public/` (mục 8): 106 file từ vựng 3.182.987 B, 21 file bài gõ 690.338 B. Id mục từ phải khớp portal, nếu không Smart Review báo "could not resolve every Space Smart Review item" |
| 2 | **Nguồn portal ghi cứng riêng của Space**, dùng cho học, Smart Review, hoạt động tiếng Anh, Voice | runtime | `src/learning/shared.ts:10`; `src/main.ts:1218,4818,4898,4918,4974,4998,5007`; `src/defense/main.ts:797`; lỗi Voice ghi tên portal nhà ở `src/input/voice-session.ts:131-136` | 0 | Cùng biến build và bắt tay như kit (mục 9) |
| 3 | **Mở một mình thì bỏ sự kiện học**, không có hàng đợi như game kit | runtime | `src/main.ts:4806` (`if (window.parent === window) return;`) | 0 | Chuyển sang `LearningBridge` của kit, hoặc chép hàng đợi `localStorage` |
| 4 | **Voice và Hybrid chỉ chạy trong portal** (portal giữ Vosk, mô hình, mic) | runtime | `voice-session.ts:131-136`; `portal/src/voice-bootstrap.ts:20-92`; `portal/src/voice/model-cache.ts:27-53` | 47.060.870 nếu dời vào Space | **Chủ dự án quyết:** Voice chỉ có trong portal, ẩn nút Voice/Hybrid khi Space không được nhúng (đề xuất), hay dời vào Space (+ khoảng 47 MB) |
| 5 | **API runtime của Admin** chỉ `admin/server.mjs` của repo cha phục vụ | runtime (tùy chọn) | `src/admin/*-runtime-policy.ts`, `shop-policy-contract.ts:9`, `src/liveops/runtime.ts:18`, `src/media/runtime-media.ts:1`; `play.conf:106-111`; `admin/server.mjs:48-59` | 0 | Bản online tắt các lượt gọi này (có cấu hình sẵn, `world-runtime-policy.ts:65-76`), hoặc khi Publish thì xuất JSON tĩnh vào deploy của Space. Bớt khoảng 8 request thừa mỗi lần mở |
| 6 | Địa chỉ máy chủ ghi cứng theo môi trường | runtime | `cloud/wrangler.jsonc:27` (`PUBLIC_URL`); `server/duel/ws-server.ts:92-93`; `play.conf:87-127` | 0 | `PUBLIC_URL` theo env của wrangler. Ẩn Duel online tới khi viết lại bằng Durable Objects |
| 7 | **Âm riêng và Test Lab lọt vào `dist`** khi build bằng `./play.sh` | build | `play.sh:9` (`SPACE_LOCAL_ASSETS=1 SPACE_TEST_LAB=1`); `vite.config.ts:15-16,60-72`; `media.config.json:140-144` | — | Script deploy build trong worktree sạch, không đặt hai cờ, không dùng lại `dist` của play.sh. Kiểm chặn `local-assets/`, `shared/music`, Dota-Sounds, chuỗi Test Lab |
| 8 | **323,5 MiB media chỉ tải được bằng công cụ repo cha**, công cụ không lọc theo game | đóng gói | `media.md5` (407 dòng `public/`); `scripts/media/lib/args.mjs:21-27` (`--only` chỉ nhận `originals`, `runtime`, `private`) | 339.183.994 | Lệnh tải riêng trong repo game (mục 11), hoặc tạm thêm `--game <id>` |
| 9 | Test đọc `../../../shared/vocabulary` | công cụ | `tests/game-word-variety-regression.test.ts:20`; `tests/td/typing.ts:21`; `scripts/td/replay.ts:25` | — | Đọc bản chép `public/vocabulary/` |
| 10 | Bản build công khai còn mang sandbox của game khác | build | `vite.config.ts:101-112` (`td.html` là Lời Gọi cũ; `defense.html` là Rift Defense) | 291.431 | Bỏ `td.html` (và `defense.html` khi Lời Gọi thay nó) khỏi bản công khai, sau cờ như `SPACE_BENCH` |
| 11 | Media không hash được cache immutable 30 ngày | runtime | `play.conf:140` (không có luật `no-cache` cho `/assets/space-typing/` như `:162,191,225`) | 0 | `_headers`: `/assets/space-typing/*`, `/assets/audio/*` `no-cache` tới khi có tên hash |

- **Đừng bỏ `tyrant-g01.glb` (12 MiB):** mã có tham chiếu (`src/boss/model-3d-contract.ts:20` qua `Game.ts:513`). Chỉ bỏ khi log mạng xác nhận.
- **Cỡ của Space đến từ media của chính nó**, không từ phụ thuộc: 595,0 MiB. Làm nhẹ theo HOSTING_PLAN §7 (texture 1024, WebP hoặc AVIF), không thuộc việc tách.

## 7. Portal và bốn game luyện gõ

Portal không phải game, nhưng là deploy riêng (`<tên-miền>`). Từ các game, portal chỉ cần `appUrl` mở được; ngoại lệ là Admin.

| # | Phụ thuộc | Loại | Ở đâu | Byte | Sửa |
|---|---|---|---|---:|---|
| 1 | **Build portal import mã của Space** (Admin), kéo 80 icon Space vào portal người chơi | build | `portal/src/admin/space-typing-duel-phase-b.ts:6-8`; `space-typing-sfx-phase-b.ts:4`; `admin/v2/preview/production-registry-icon.ts:4`; import tĩnh `portal/src/main.ts:2`, nav `:429`, route `:618-622` | 1.202.526 | Admin sau cờ build (`VITE_PORTAL_ADMIN=1` ở máy nhà) và `import()` động. Bản online không có mã Space |
| 2 | `vosk-browser` chỉ khai ở `package.json` của repo cha; plugin đọc `scripts/`, `shared/voice` | công cụ | `portal/vite.config.ts:2`; `scripts/offline-vosk-plugin.mjs:12-13,73` | — | Khai trong `portal/package.json`, hoặc coi repo cha là đơn vị deploy của portal (portal không phải submodule) |
| 3 | **Mô hình giọng vượt 25 MiB mỗi file** | runtime | `portal/public/assets/voice/vosk-small-en-us-0.15-space-endpoint-v1.tar.gz`; `model-cache.ts:27-53` | 41.116.554 | R2, Worker portal trả ở đúng `/assets/voice/<id>.tar.gz` (HOSTING_PLAN §6 bước 1) |
| 4 | Tìm khung Space theo **tiêu đề iframe** "Space Typing" | runtime | `portal/src/voice-bootstrap.ts:23`; tiêu đề đặt ở `main.ts:522` | 0 | So theo id game và nguồn `appUrl` trong `games.json` |
| 5 | `games.json` chỉ có địa chỉ máy nhà; là danh sách nguồn tin cậy | runtime | `portal/public/games.json:53,62,71`; `main.ts:83-86,638`; `portal/src/learning/bridge.ts:73-77`; trình kiểm `scripts/validate-space-integration.mjs:11-104` | 0 | Sinh `games.<môi-trường>.json` lúc deploy portal, chỉ liệt kê game đã deploy. Giữ nguyên file máy nhà và trình kiểm |
| 6 | Logic riêng từng game trong portal: Smart Review cho 5 game; portal từ chối tin `lookup` của Rồng | runtime | `main.ts:150-231,536-547,656-676`; `shared/learning/message-contract.mjs:37-57`; `games/dragon-hold/src/app/learning.ts:330` | 0 | Một tin review-dataset và một bộ xử lý `lookup` theo `gameId`. Thêm game không cần sửa portal |
| 7 | CSS Admin trỏ URL tuyệt đối của Space, file đã không còn | runtime | `portal/src/admin/space-typing-ui.css:54` | 0 | Bỏ URL (đang 404) |
| 8 | Nhạc portal lấy từ `shared/music` riêng tư | runtime | `portal/src/music.ts:558-560`; `play.conf:24-27` (197 file, 479.411.694 B) | 0 | Online chỉ gửi `index.json` rỗng hoặc bộ có giấy phép. Không bao giờ deploy `shared/music` |

**Bốn game luyện gõ** (Monkeytype, Vocabulary Shooter, Recall, Karaoke) fetch từ vựng và bài gõ **từ nguồn portal bằng URL tuyệt đối** `https://typing-game.local/...`, nhờ CORS `*` (`play.conf:16,21`). Ví dụ: `games/vocab-shooter/src/vocabulary/library.ts:3`, `games/recall-typing/src/vocabulary/library.ts:3`, `games/monkeytype/frontend/src/ts/custom/typing-text-library.ts:6`; mỗi game có bản `PARENT_ORIGIN` riêng (`src/learning/shared.ts:7`). Đúng quy tắc thì mỗi game chép bản từ vựng của mình (cùng `vocab:sync`). Nếu không, portal phải tiếp tục phục vụ `/vocabulary/` (3.485.011 B) và `/typing-texts/` (692.920 B) có CORS, và bốn game này còn dính deploy portal. **Đưa chúng lên hay không: chủ dự án quyết** (HOSTING_PLAN §6 bước 0).

## 8. Nội dung dùng chung: chép bản ghim, chỉ phần dùng

| Game | Chép vào `public/` | Số file | Byte | Lý do |
|---|---|---:|---:|---|
| Rồng Giữ Ải | `vocabulary/index.json`, `levels/001`–`100`, `ATTRIBUTION.md` | 102 | 2.666.953 | Level lưu theo người chơi, cần `[L, L+1]` |
| Lời Gọi | `vocabulary/index.json`, `levels/001`–`005`, `ATTRIBUTION.md` | 7 | 123.832 | `VOCAB_LEVELS = 5` (`src/app/vocab.ts:12`) |
| Tuyến Cuối | `vocabulary/index.json`, `levels/001`–`003`, `ATTRIBUTION.md` | 5 | 69.077 | `src/app/vocab.ts:44-45` |
| Space Typing | `vocabulary/`: index, `lookup.json`, `topics/index`, `parts-of-speech/index`, `grammar/index`, 100 level, `ATTRIBUTION.md`; `shared/typing-texts/`: 21 file | 127 | 3.873.325 | Học, Smart Review, bài gõ |

- **Không game kit nào chép `shared/typing-texts`** (24 file, 692.920 B): 0 lần xuất hiện trong bundle và trong log Chrome.
- **Không ai chép cả `shared/vocabulary`** (116 file, 3.485.011 B).
- **`ATTRIBUTION.md` bắt buộc** (CC BY-SA 4.0). Lời Gọi hiện chưa hiển thị nguồn ở đâu cả.
- JSON và Markdown được vào Git (quy tắc "media không vào Git" chỉ chặn ảnh, âm, GLB). Bản chép nằm trong repo game, nên dev, test, build và deploy cùng đọc một bản.

**Giữ bản chép đồng bộ** (cùng mẫu với `kit:sync`):

1. **Nguồn gốc:** `shared/vocabulary` và `shared/typing-texts` của repo cha. Lần sửa cuối của từ vựng: `56d3721d` (24/09/2026).
2. **Mỗi game có `vocab.config.json`:** danh sách file cần chép (hoặc khoảng level) và `pin` = commit repo cha.
3. **`pnpm vocab:sync --target games/<id>` ở repo cha** đọc file ở đúng commit ghim (`git show <pin>:shared/vocabulary/...`, không đọc cây làm việc), ghi `public/vocabulary/**` và `public/vocabulary/vocab-manifest.json` (pin, `version` lấy từ `index.json`, sha256 từng file).
4. **Bước build đọc bản ghim:** `verify-vocab.mjs` trong repo game (chép qua kit, như `verify-kit.mjs`) chạy ở `prebuild`, nên `pnpm build`, `pnpm check` và `deploy:pack` đều qua nó. Nó kiểm sha256 từng file khớp `vocab-manifest.json` và có `ATTRIBUTION.md`; lệch một byte là build dừng. Build chỉ đọc bản chép trong repo, không tải gì từ repo cha hay mạng, nên clone riêng vẫn build được offline (quy tắc 2).
5. **Một test trong mỗi game:** mọi level mã có thể hỏi đều có trong bản chép (Rồng 1–100, Lời Gọi 1–`VOCAB_LEVELS`, Tuyến Cuối 1–3), và `version` trong manifest khớp `index.json`. Golden giữ nguyên: Tuyến Cuối hash bộ bài 7f073fa2, Lời Gọi `td:golden:check`.
6. **`pnpm vocab:drift` ở repo cha** (như `kit:drift`): báo game nào có `pin` cũ hơn lần sửa cuối của `shared/`. Chỉ báo, không chặn. Cập nhật = chạy lại `vocab:sync`, commit trong repo game, rồi đẩy con trỏ submodule.
7. **Vì sao ghim, không đọc bản mới nhất:** hash bộ bài vào hash thế giới và golden; id mục từ phải khớp portal cho Smart Review. `version` trong manifest cho biết game đang mang bản nào.

## 9. Nguồn portal là biến build

**Hôm nay:** `PARENT_ORIGIN = "https://typing-game.local"` (`shared/game-kit/learning/contract.ts:22`, bản chép ở cả ba game; Space có bản riêng ở `src/learning/shared.ts:10`). Trong portal ở nguồn khác, trình duyệt **lặng lẽ bỏ** mọi tin: kết quả học, Smart Review, yêu cầu focus, giảm nhạc. Đã thử: portal giả ở 127.0.0.1:4320 nhúng Rồng, Chrome báo "target origin ('https://typing-game.local') does not match", portal nhận 0 tin.

| Bước | Việc | Ở đâu | Ghi chú |
|---|---|---|---|
| A | Mỗi game truyền `parentOrigin` từ `import.meta.env.VITE_PORTAL_ORIGINS` (danh sách, phân cách dấu phẩy). Không đặt thì mặc định `https://typing-game.local`: Play ở máy nhà không đổi | Rồng `src/app/app.ts:208` (và `learning.ts:246`); Lời Gọi `src/app/learning.ts:15`; Tuyến Cuối `src/app/learning.ts:18` | `createLearningBridge` đã nhận `parentOrigin` (`bridge.ts:48`), nên kit giữ nguyên byte, `verify-kit` vẫn qua. Bước A dùng nguồn đầu tiên của danh sách |
| B | **Sửa kit** (`shared/game-kit/learning/bridge.ts`, rồi `kit:sync`): chỉ coi là "đang nhúng" khi nhận tin `hello` của portal từ nguồn trong danh sách; từ đó gửi tới `event.origin`; chỉ xóa sự kiện trong hàng đợi khi nhận `ack` | `bridge.ts:122` (xả hàng đợi khi khởi tạo), `:149-157` (xả rồi `writeQueue([])` không chờ `ack`), `:131-140`, `:274` (`ack` bị bỏ qua) | **Biến build một mình chưa đủ.** Hôm nay portal sai nguồn sẽ xóa tới 500 sự kiện người chơi gom khi chơi riêng. Cần thêm tin `hello` vào `shared/learning/message-contract.mjs` và portal gửi nó (hiện chưa có) |
| C | Space dùng cùng biến và bắt tay; thêm hàng đợi; sửa câu lỗi Voice | `src/learning/shared.ts:10`; `src/main.ts:4806`; `voice-session.ts:131-136` | Lỗi nên ghi "mở từ portal", không ghi tên `typing-game.local` |
| D | Portal sinh `games.<môi-trường>.json` lúc deploy; `voice-bootstrap` so theo id | `portal/public/games.json`; `voice-bootstrap.ts:23` | Đổi tên miền một game = đổi hai chỗ: `games.json` của portal và `VITE_PORTAL_ORIGINS` của game |

- **Cùng một tên miền gốc:** portal ở `<tên-miền>`, mọi game ở `<id>.<tên-miền>`. Cookie đăng nhập của Space là `SameSite=Lax` (`cloud/src/http.ts:77`, `cloud/src/oauth.ts:79`); bản lưu và hàng đợi học nằm trong `localStorage` của nguồn game. Khác tên miền gốc thì mất đăng nhập trong portal và tách bản lưu.
- **Cách khác, chưa chọn:** file `/portal.json` trong deploy của game, đọc lúc chạy, đổi tên miền không cần build lại. Chọn biến build vì đơn giản và kiểm được lúc đóng gói.
- **Kiểm lúc đóng gói:** build cho production mà thiếu `VITE_PORTAL_ORIGINS`, hoặc bundle còn chuỗi `typing-game.local`, thì hỏng.

## 10. Mở game một mình (không portal)

| Game | Chơi được | Mất gì khi không có portal | Đã kiểm |
|---|---|---|---|
| Rồng Giữ Ải | Có, khi đã chép từ vựng | Không mất: sự kiện học chờ trong `localStorage` (tối đa 500), gửi khi vào portal đúng nguồn | Gói 147 file ở 127.0.0.1:4705 và :4317: Rồng nạp, quái có chữ (place, city, good), 0 request hỏng |
| Lời Gọi | Có (cả khi thiếu từ vựng, dùng từ dự phòng) | Như trên | :4318: `__td.flags().vocabulary = "vocabulary"`, 0 request hỏng |
| Tuyến Cuối | Có (thiếu thì từ dự phòng và hình thay) | Như trên | :47313 và :4319: `__survival.models()` đều `true` cho cả hai phi công |
| Space Typing | Có: chiến dịch, bản lưu, tài khoản cùng nguồn | Sự kiện học bị bỏ (`main.ts:4806`), Smart Review, Voice/Hybrid; Duel cần máy chủ Node | Chưa chạy gói riêng (audit mã) |

Kiểm tự động trong script deploy (mục 11): mở `.deploy/<id>/` ở **cấp cao nhất**, không portal, trên server tĩnh không fallback SPA. Đạt khi: 0 request hỏng; 0 request sang nguồn khác; từ vựng đã nạp (Rồng: số chữ > 0; Lời Gọi: `vocabulary`; Tuyến Cuối: hash 7f073fa2, không phải 28a73ed5); model nạp đủ khi gói có media.

## 11. Script deploy cho từng game

**Nằm trong repo game**, không trong repo cha. Phần chung viết một lần ở `shared/game-kit/tools/deploy/`, chép vào `src/kit/tools/deploy/` qua `kit:sync` (như `cdp-run.mjs`). Space chưa dùng kit: có script riêng, cùng các bước kiểm.

| Lệnh | Làm gì |
|---|---|
| `pnpm media:pull` | Đọc `media.md5` của chính game, chỉ giữ dòng `public/` nằm trong danh sách gói (`deploy.config.json`), tải bằng rclone từ `tgmedia:typing-game-media/repo/games/<id>/`, kiểm md5. Không cần repo cha; cần remote `tgmedia` trên máy |
| `pnpm deploy:pack` | Build production sạch (`VITE_PORTAL_ORIGINS` đặt sẵn; Space: không `SPACE_LOCAL_ASSETS`, không `SPACE_TEST_LAB`) → chép `dist` vào `.deploy/<id>/` theo danh sách gói → thêm `_headers` → chạy kiểm dưới |
| `pnpm deploy:standalone` | Clone repo game (từ GitHub hoặc `file://` của HEAD) vào thư mục trống **không có repo cha bên trên** → `pnpm install --frozen-lockfile` → `pnpm check` (`verify-kit`, `verify-vocab`, test, build) → `media:pull` → `deploy:pack` → phục vụ gói, mở bằng Chrome headless (mục 10) |
| `pnpm deploy:push` | `wrangler deploy` với `deploy/wrangler.jsonc` của game: Worker chỉ có file tĩnh, `assets.directory` = `.deploy/<id>`, không `not_found_handling` |

**Kiểm của `deploy:pack`** (hỏng một điều là dừng):

| Kiểm | Ngưỡng |
|---|---|
| Cỡ một file | Không file nào > 25 MiB |
| Số file | < 20.000 |
| Media riêng tư | Không `local-assets/`, `shared/music`, Dota-Sounds, `art-src/`, không file thuộc nhóm `private` của `media.config.json` |
| Đường ra ngoài game | Quét HTML, JS, CSS, JSON đã build: URL tuyệt đối chỉ được bắt đầu bằng `/assets/<id>/`, file có hash của Vite trong `/assets/`, `/vocabulary/` (Space thêm `/shared/typing-texts/`, `/api/account/`). Hỏng nếu có `/assets/<id khác>/`, `../`, nguồn khác, hoặc `*.typing-game.local` ở bản production |
| Đủ file | Mọi URL trên trỏ tới file có trong gói: mục trong manifest model, level từ vựng, GLB Rồng |
| Kiểu nội dung | `manifest.json` là `application/json` (`model-loader.ts:127`) |
| Giấy phép | Có `vocabulary/ATTRIBUTION.md`; giữ `LICENSE`, `NOTICE`, `SOURCE.md` |
| Báo cáo | Cỡ gói và cỡ lần chơi đầu so với ngân sách HOSTING_PLAN §7. Chỉ báo, không chặn |

**`deploy:standalone` chạy ở đâu:**
- CI của repo game (GitHub Actions): mọi bước trừ media, vì CI không có quyền vào Drive. Ở chế độ này cho phép hình thay model, nhưng từ vựng bắt buộc.
- Mac hoặc Dell, trước mỗi lần deploy: chạy đủ cả media.

**Chép thêm vào `deploy.config.json` của từng game:**
- Rồng: chỉ `draconis-v2`, `draconis-v4` (High và Medium); không `draconis-v3`.
- Lời Gọi: không `assets/typing-defense/models/**`, không `.vite/`.
- Tuyến Cuối: 7 model của mục 5.1 và manifest riêng.
- Mọi game: bỏ `.DS_Store`, README nội bộ. File `.woff` (Rồng 301.488 B, Lời Gọi 199.364 B) trình duyệt hiện đại không tải; bỏ hay giữ đều được.

## 12. Mỗi game mang theo gì: trước và sau

"Trước" là kế hoạch 25/10: `dist` hôm nay cộng cả `shared/vocabulary` (116 file) và `shared/typing-texts` (24 file); Tuyến Cuối cộng cả thư viện model Space.

| Game | Trước (kế hoạch 25/10) | Sau khi sửa | Thành phần sau khi sửa |
|---|---:|---:|---|
| Rồng Giữ Ải | 187 file, 21,60 MiB (22.647.484 B) | **147 file, 14,50 MiB** (15.208.438 B) | build 41 file 1.811.265 B (JS 1.175.211, CSS 39.914, font 595.104, HTML 1.036) + 4 GLB 10.730.220 B + từ vựng 102 file 2.666.953 B |
| Lời Gọi | 254 file, 23,84 MiB (25.000.708 B) | **51 file, 1,11 MiB** (1.163.064 B) | build 43 file 703.996 B + từ vựng 7 file 123.832 B + `title-dusk.webp` 335.236 B |
| Tuyến Cuối | 564 file, 365,09 MiB (382.829.704 B) | **58 file, 12,36 MiB** (12.960.320 B) | build 45 file 1.385.732 B + 7 GLB High 11.501.400 B + manifest 4.111 B + từ vựng 5 file 69.077 B. Thêm Medium: 65 file, khoảng 16,15 MiB |
| Space Typing | 1.871 file, 595,29 MiB (624.206.020 B) | khoảng 1.852 file, khoảng 594,7 MiB | `dist` 22/10 (1.731 file, 620.028.089 B) + từ vựng dùng 106 file + bài gõ 21 file, bớt sandbox 291.431 B. Làm nhẹ thật theo HOSTING_PLAN §7 |
| Portal | 149 file, 47,43 MiB (49.736.339 B) | khoảng 208 file, 11,06 MiB (11.595.190 B) + 1 object R2 39,21 MiB | Không Admin, mô hình giọng ở R2; con số gồm `/vocabulary/`, `/typing-texts/` cho bốn game luyện gõ |

- Ba game kit cộng lại: **từ 410,53 MiB xuống 27,97 MiB.** Mỗi game đẩy độc lập; sửa Lời Gọi chỉ đẩy 1,11 MiB.
- Số đo gói "sau" của ba game kit là gói thật đã dựng trong scratch và mở bằng Chrome, không phải ước tính. Space và portal là cộng từ số đo file.

## 13. Thứ tự làm

Các agent khác đang làm trong cả ba game (R3 balance, feel pass). Mỗi bước dưới là một PR riêng trong repo game, vào sau đợt đang chạy của làn đó.

**Bước chung V (một lần, repo cha):** `vocab:sync`, `vocab:drift`; `verify-vocab.mjs` và công cụ deploy trong `shared/game-kit/tools/`; `kit:sync` cho ba game.

| Thứ tự | Game | Việc | Xong khi |
|---|---|---|---|
| 1 | **Lời Gọi** (nhỏ nhất) | Chép 7 file từ vựng; `tests/td/typing.ts:23`, `scripts/td/replay.ts:31` đọc bản chép; bỏ plugin ở `vite.config.ts:36`; `parentOrigin` ở `src/app/learning.ts:15`; `deploy.config.json` (bỏ model, `.vite/`); tải riêng `title-dusk.webp`; `engines.node` | `deploy:standalone` xanh; gói 51 file, khoảng 1,11 MiB |
| 2 | **Tuyến Cuối** | Chép 7 model (mục 5.1), `media:push`, commit manifest và `media.md5`; `src/view/models.ts:8`; bỏ `modelsDir`, `SPACE_MODELS_DIR` ở `vite.config.ts:16,24`; bậc model theo chất lượng (`crowd.ts:142`, `ship.ts:50`); chép 5 file từ vựng; `typist-bot.ts:275`, `bot.ts:49`, `scripts/replay.ts:34` đọc bản chép; `parentOrigin` ở `src/app/learning.ts:18` | `deploy:standalone` xanh; 0 request `/assets/space-typing/`; golden s0-trace không đổi |
| 3 | **Rồng Giữ Ải** | Chép 102 file từ vựng; bỏ plugin ở `vite.config.ts:8,18`; báo lỗi hoặc bộ từ dự phòng khi bộ bài rỗng (`learning.ts:318-322`, `app.ts:779-797`); `parentOrigin` ở `app.ts:208`; tải media riêng (chỉ dòng `public/`); bỏ `draconis-v3` khỏi gói; tên GLB có hash hoặc `?v=` (`heroes.ts:83-86`) | `deploy:standalone` xanh; gói 147 file, khoảng 14,50 MiB |
| 4 | **Kit, bước B** | Bắt tay `hello` và xóa hàng đợi theo `ack` (mục 9); tin `hello` trong `shared/learning/message-contract.mjs`; portal gửi `hello`; `kit:sync` cho ba game | Portal giả sai nguồn không xóa hàng đợi; portal đúng nguồn nhận đủ sự kiện |
| 5 | **Repo cha, hạ tầng máy nhà** | Bỏ alias `/vocabulary/`, `/typing-texts/` của ba game và alias model Space của Tuyến Cuối, Tu Tiên ở `play.conf`, `dev.conf`; sửa `validate-play-mode.mjs:40-46`; bỏ `SPACE_MODEL_MANIFEST_URL` khỏi kit | `./play.sh` vẫn chạy cả ba game từ `dist` của chính chúng |
| 6 | **Space Typing** | Chép 127 file từ vựng và bài gõ; nguồn portal và hàng đợi (mục 9 bước C); ẩn Voice khi không nhúng (nếu chủ dự án chọn); build sạch không cờ riêng tư; bỏ `td.html`; tắt API runtime của Admin ở bản công khai; `PUBLIC_URL` theo env; `_headers`; tải media riêng | `deploy:standalone` của Space xanh; kiểm riêng tư xanh |
| 7 | **Portal** | Admin sau cờ và `import()` động; `vosk-browser` vào `portal/package.json`; mô hình giọng ở R2; `games.<môi-trường>.json`; `voice-bootstrap` so theo id; bỏ URL ở `space-typing-ui.css:54` | Build portal không cần `games/space-typing`; gói khoảng 11 MiB |

Bước 1–3 chạy song song được (ba repo khác nhau); bước 4 sau bước chung V.

## 14. Những gì đổi trong `docs/HOSTING_PLAN_2026-10-25.md`

Commit này **chỉ thêm tài liệu này**. Các chỗ sau trong HOSTING_PLAN sửa ở lượt sau, trỏ về đây:

| Mục | Đang ghi | Sửa thành |
|---|---|---|
| Đầu tài liệu | — | Thêm dòng: "Mỗi game triển khai riêng: xem [DEPLOY_INDEPENDENCE.md](games/DEPLOY_INDEPENDENCE.md)" |
| §1 bảng | Rồng 17,6; Lời Gọi 19,8 (110 file); Tuyến Cuối "1,3 (+ 359,8 model mượn của Space)" | Rồng 14,50 (147); Lời Gọi 1,11 (51); Tuyến Cuối 12,36 (58), model riêng (mục 12 ở đây) |
| §1 ghi chú | Tuyến Cuối nạp thư viện model của Space qua alias nginx | Tuyến Cuối mang 7 model riêng (mục 5.1) |
| §4 sơ đồ | "survival kèm bản chép thư viện model của Space"; "chép thư viện model của Space (359,8 MiB, 379 file) vào gói deploy của Tuyến Cuối… là cách không sửa mã" | Bỏ. Tuyến Cuối mang 11,5 MB model riêng; sửa một dòng `models.ts:8` |
| §4 portal | Portal phục vụ `/vocabulary/`, `/typing-texts/` | Chỉ khi bốn game luyện gõ lên mạng và chưa chép từ vựng (mục 7) |
| §6 bước 1, nguồn portal | Đổi thành biến build rồi build lại | Biến build **và** bắt tay `hello` cùng hàng đợi theo `ack` (mục 9) |
| §6 bước 1, Tuyến Cuối | Kèm bản chép thư viện model Space | Mục 5.1 |
| §6 bước 2, script đóng gói | Chép `shared/vocabulary`, `shared/typing-texts` vào mọi game | Mỗi game chép bản ghim, chỉ phần dùng (mục 8); script nằm trong repo game, có `deploy:standalone` (mục 11) |
| §1 bảng và §7 | `tyrant-g01.glb` "có vẻ không dùng", "không thấy mã nào tải" | Mã có tham chiếu (`src/boss/model-3d-contract.ts:20` qua `Game.ts:513`); chỉ bỏ khi log mạng xác nhận |
| §7 ngân sách | Rồng ≤ 5 MB; Tuyến Cuối ≤ 4 MB | Giữ. Thêm số đo lần chơi đầu: Rồng 8.948.385 B ở High; Tuyến Cuối 7.139.188 B GLB ở High (mục 3, 5.1) |
| §8 nguồn | — | Thêm tài liệu này |

Các tài liệu khác cần sửa cùng lúc với bước 2 (Tuyến Cuối): `docs/games/MEDIA_AND_MODELS.md:125` (§7, dòng cuối); `docs/games/SPLIT_PLAN.md:147,235,258` (hợp đồng URL `/assets/space-typing/models/`); `games/typing-survival/AGENTS.md:98`; chú thích ở `games/typing-survival/vite.config.ts:12-15` và `src/view/models.ts:1-5`.

## 15. Cần chủ dự án

| Việc | Vì sao |
|---|---|
| **Tên miền:** đặt nameserver ở Cloudflare; portal ở `<tên-miền>`, mọi game ở `<id>.<tên-miền>` | Cùng tên miền gốc để giữ đăng nhập và bản lưu (mục 9). Chưa có thì chỉ thử từng game trên `*.workers.dev` |
| **Thanh toán:** phương thức thanh toán để bật R2 | Mô hình giọng 39,2 MiB vượt 25 MiB mỗi file |
| **Token Cloudflare** cho `wrangler deploy` (và secret CI nếu muốn deploy từ CI) | Chỉ chủ tài khoản tạo được |
| **Quyền Drive trên máy deploy:** CI có token rclone cho `tgmedia` không, hay chỉ deploy từ Mac/Dell | Media chỉ ở Drive. Không token thì CI chỉ chạy được phần không media |
| **Voice của Space online:** chỉ trong portal (đề xuất) hay dời vào Space (+ khoảng 47 MB) | Mục 6 dòng 4 |
| **Bốn game luyện gõ:** đưa lên hay bỏ khỏi `games.json` online | Mục 7 |
| **Nhạc:** bộ có giấy phép hay tắt nhạc online | `shared/music` không được phát hành |
| **Tuyến Cuối nhập cả bậc Medium** (+ 3.969.672 B trên ổ) | Đưa lần chơi đầu về dưới ngân sách 4 MB (mục 5.1). Mặc định: có |

Còn lại là việc của Claude, có phản biện.

## 16. Bằng chứng

Thư mục scratch của phiên (ngoài repo):
`/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/157c54d6-5a15-4acc-b09d-0aae10862f93/scratchpad/deploy/`

| Thư mục | Nội dung |
|---|---|
| `dragon-hold/` | `repo/` (clone HEAD 73b265c, `dist` cộng từ vựng và 4 GLB dùng); `probe/empty-deck.ts` (thử bộ bài rỗng) |
| `typing-defense/` | `alone/typing-defense` (clone HEAD 7d6adf4); `site/` (gói ứng viên 51 file); `site-files.txt`; `escape.py` (quét đường ra ngoài) |
| `typing-survival/` | `repo/` (`dist` và `dist-own`, bản chỉ đổi `models.ts`); `serve-own/` (gói 58 file); `tools/subset.py` (manifest riêng, kiểm byte); `tools/serve.mjs`; `log-full.tsv`, `log-bare.tsv`, `log-own.tsv` |
| `portal-space-shared/` | `escape.mjs` (import ra ngoài repo), `measure.mjs`, `space-tracked.txt` |
| `verify/` | Clone mới từ GitHub của ba game; `install.log`, `build.log`, `test.log`; `out/*.json`, `*.png`; `tools/probe.mjs` (CDP) |

- Mọi server thử (4314–4320, 4705, 47311–47313) đã tắt.
- Dùng Chrome 155 headless (`/Applications/Google Chrome.app`): `CHROME_PATH` trên Mac trống, vì `scripts/local-env.sh` chỉ đặt nó trên Linux.
- `dist` của Space đo bản build 22/10 trên Mac, có media Drive. Các số còn lại đo ngày 26/10.
