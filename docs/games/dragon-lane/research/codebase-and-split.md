# Dragon Lane: nghiên cứu mã nguồn, portal và cách tách game

Ngày: 23/10/2026. Tên "Dragon Lane" là tên tạm.
Đối chiếu tại: repo cha `e7e0e049` (nhánh `feat/td-1a6`); Space Typing `b9d9bd79` (`feat/space-typing-2026-10-18`);
worktree `games/.wt-td-1a6` (`fc5aad95`) và `games/.wt-survival` (`28e071bc`, chỉ đọc).
Tài liệu này chỉ nghiên cứu. Không sửa mã.

## 1. Tóm tắt

- Portal đọc danh sách game từ `portal/public/games.json`. Mỗi game chạy trong iframe, trên một tên miền riêng `*.typing-game.local`.
- Thêm một game mới phải sửa khoảng 12 chỗ: games.json, 2 file nginx, chứng chỉ, scripts, play.sh, dev.sh, validate. Mục 2 có danh sách.
- TD (`src/td`) đã gần độc lập: chỉ dùng 5 module của Space Typing. Tách rất rẻ.
- Survival (`src/survival` + `src/feedback`) dùng 8 module. Phần lớn mã S0 chưa commit. Nên tách ngay bây giờ, trước khi nó lớn.
- Không nên import thẳng `games/space-typing/src` từ game khác. Nên làm một bộ dùng chung `shared/game-kit` ở repo cha.
- Kho media và quy trình model hiện chỉ biết một game (Space Typing). Phải mở rộng trước khi game mới có model riêng.
- 3D dùng được ngay: 2 rồng (v2/v3 bay, v4 đứng). 122 model quái chỉ có `Enemy_Idle`, phong cách vũ trụ, không có xương: chỉ dùng tạm cho quái bay. Quái đi hai chân, bốn chân thì chưa có.

## 2. Portal và cách game được chạy

| Thành phần | File | Ghi chú |
|---|---|---|
| Danh sách game | `portal/public/games.json` | `id`, `name`, `description`, `path`, `appUrl`, `icon` (emoji). Thẻ ở trang chủ và nút trên thanh nav sinh từ đây. |
| Khung game | `portal/src/main.ts` `renderGame` | iframe tới `appUrl`; gửi `typing-game:shared-music` để game biết nhạc portal đang phát. |
| Cầu học tập | `portal/src/learning/bridge.ts` | Nhận `typing-game:learning:v1:attempt`. Kiểm `event.origin` khớp `appUrl` và `event.gameId` khớp `id` trong games.json. |
| Ôn tập Smart Review | `portal/src/review/*-adapter.ts`, `shared/learning/review-session.mjs`, `mixed-review.mjs`, `adaptive-mix.mjs` | Danh sách game cố định. Game mới vẫn ghi được sự kiện học, nhưng chưa vào Mixed Review cho tới khi có adapter. |
| Giọng nói | `portal/src/voice-bootstrap.ts` | Gắn cứng `space-typing`. Game mới muốn nhập bằng giọng phải sửa portal. |
| Nginx | `infra/nginx/typing-game.local.{dev,play}.conf` | Mỗi game một `server`. Dev: proxy tới cổng Vite. Play: phục vụ `dist`. Mỗi game tự alias `/vocabulary/` tới `shared/vocabulary/`. |
| Tên miền, chứng chỉ | `scripts/setup-nginx.sh` (mảng `HOSTS`) | Thêm tên miền thì phải tạo lại chứng chỉ và sửa `/etc/hosts` (cần sudo). |
| Lệnh | `package.json` cha | `dev:<game>:app`, `build:<game>`, `dev` (concurrently), `build:local`. |
| Chạy bản build | `play.sh` (`build_if_needed`), `scripts/play.sh` (danh sách `dist`) | Thêm từng game. |
| Dev | `dev.sh` (targets), `scripts/bootstrap.sh` (cài, submodule), `scripts/cleanup-dev-ports.sh` | Thêm target. |
| Kiểm tra | `scripts/validate-play-mode.mjs` | Danh sách `dist` và host gắn cứng. |
| Submodule | `.gitmodules` | 5 game là submodule riêng trên GitHub `sinhvienaiti/*`. |

Cổng đang dùng: 3000–3004 (game), 3100 (portal), 3199 (admin), 3014 (duel), 3016 (account), 3095–3098 (công cụ).
Cổng trống đề xuất: **3005** Dragon Lane, **3006** Typing Defense, **3007** Survival.

## 3. Module của Space Typing dùng lại được

| Module | File (số dòng) | Phụ thuộc ra ngoài | Nhận xét |
|---|---|---|---|
| Phím, IME tiếng Việt | `src/scene3d/keys.ts` (67) | không | Dùng nguyên. |
| Chuẩn hóa chữ | `src/logic.ts` `typingText` (114) | type `Enemy` từ `types.ts` | Chỉ lấy hàm `typingText`, `normalizeWord`. |
| Tải từ vựng | `src/vocabulary.ts` (730) | type từ `types.ts` | URL cố định `/vocabulary/...`. Dùng được vì nginx alias trên mọi host. |
| Chọn từ đơn giản | `src/scene3d/words.ts` `WordPicker` (65) | `logic`, `types` | Dải short/enemy/elite/boss. |
| Lõi gõ của TD | `src/td/typing/*` (bản 1A6: 6 file, ~410 dòng) | hằng số `src/td/content/rules` | Tốt nhất cho nhiều mục tiêu: chữ đầu không trùng, router phím, chấm điểm. Phải đổi hằng số thành tham số. |
| RNG, vòng khung, lưu | `src/platform/{rng,frame-loop,safe-storage,canvas-state}.ts` | không | Dùng nguyên. |
| Sự kiện học | `src/learning/shared.ts` (307) | `recall/model`, `types` | `gameId: "space-typing"` gắn cứng. Portal sẽ **từ chối** nếu game mới gửi id này. Phải thành tham số. |
| Phát âm | `src/speech.ts` (244) | `GameSettings`, `safe-storage` | Đổi tham số sang kiểu hẹp `{ enabled, rate, volume }`. |
| Nạp model | `src/render3d/model-loader.ts` (85), `model-contracts.ts` (128) | `VisualQuality` | Manifest cố định `/assets/space-typing/models/manifest.json`. `ModelKind` là union cố định. |
| Rig rồng | `src/scene3d/hero.ts` (395) | `particles`, `util` | Điều khiển clip `Hero_*`, vệt cánh theo socket. Hợp với rồng đỏ. |
| Rồng đứng | `src/ui/title-guide-scene.ts` (199) | `model-loader`, `types` | Mẫu điều khiển clip `Guide_*` của v4. |
| Hạt, vật liệu, texture | `src/scene3d/{particles,materials,textures,util}.ts` (~1.020) | `three` | Dùng nguyên. |
| Sân khấu, bloom | `src/scene3d/space.ts` (362) | `three` | Có cấp chất lượng, bloom. Phần trời sao là của vũ trụ, cần tách ra. |
| Hiệu ứng | `src/scene3d/fx.ts` (1.312) | `hero`, `space`, `sfx` | Lửa, tia, khiên. Dùng được, nhưng gắn với `SpaceStage`. |
| Âm cảnh | `src/scene3d/sfx.ts` (635) | file âm của Space | Bộ phát dùng được. Danh sách âm phải thay bằng âm riêng. |
| Phản hồi trúng đòn | `src/feedback/*` (worktree Survival, 8 file, 1.076) | `three`, `types` | hitstop, rung, số bay, mảnh vỡ, phản ứng. Rất hợp Dragon Lane. |
| Defense V4: camera, đám đông, VFX, địa hình vẽ | `src/defense/view/{camera,crowd,vfx,terrain,painter,sounds}.ts` (~2.870) | `enemies/*`, `render3d`, `scene3d` | Đám đông instanced 442 quái ≈ 3,7 ms. Theo quy tắc TD 25.1: **chép** sang, ghi nguồn, không import. |
| Ảnh giả, LOD | `scripts/models/blender/bake_impostor.py` | Blender | Cho đám đông xa. |

`src/types.ts` kéo theo `enemies/registry`, `audio/music-library`, `feedback`… chỉ qua `import type`. Một module mượn type từ đây sẽ kéo cả cây Space vào khi `tsc` kiểm tra. Bộ dùng chung phải có type riêng.

## 4. Phụ thuộc của từng phần cần tách

| Phần | Kích thước | Import ra ngoài thư mục |
|---|---|---|
| TD `src/td` (1A6) | 59 file, ~5.850 dòng | `scene3d/keys`, `logic.typingText`, `vocabulary` (2 hàm), `platform/rng`, `platform/frame-loop`. Có test `td-boundary` khóa danh sách này. |
| Survival `src/survival` | ~2.020 dòng (chưa commit) | `platform/rng`, `scene3d/keys`, `scene3d/hero`, `scene3d/textures`, `render3d/model-loader`, `vocabulary`, `feedback/reaction`. `survival.html` trỏ tới `app/main.ts` chưa có. |
| `src/feedback` | 1.076 dòng | `three`, `types` (chỉ `kill-translation`). `kill-translation.ts` đang được Space dùng (`types.ts`). |
| Defense V4 `src/defense` | ~7.575 dòng | 30 module Space: `enemies/*`, `boss/identity`, `ui/*`, `scene3d/*`, `render3d`, `learning`, `speech`, `vocabulary`. Không nên tách; chỉ chép phần hình. |
| Campaign 3D `src/campaign3d` | ~2.480 dòng | `campaign/*`, `worlds/*`, `characters/*`. Gắn chặt với Space. Giữ lại trong Space. |

Kèm theo khi tách TD: `td.html`, `tests/td-*.test.ts` + `tests/td/`, `scripts/td/` (balance, golden, replay), `docs/td/`, `art-src/td/`, khối `.gitignore` cho `public/assets/td/**`, lệnh `td:balance`, `td:golden:update`.
Kèm theo khi tách Survival: `survival.html`, `docs/survival/`, test ranh giới `survival-boundary` (theo BUILD_S0).

## 5. Ba cách dùng lại mã

| Cách | Làm thế nào | Được | Mất |
|---|---|---|---|
| A. Alias vào Space | Vite alias + tsconfig `paths` tới `../space-typing/src` | Nhanh nhất | Game khác vỡ khi Space đổi mã hay đổi nhánh. Kéo cây type của Space. `three` có thể bị nạp hai bản (cần `resolve.dedupe`). Submodule không tự build được. Trái ý chủ dự án "đừng nhồi vào Space". |
| B. Kit ở repo cha, import trực tiếp | `shared/game-kit/src`, alias `@kit` | Một nguồn duy nhất. Portal đã import `shared/learning` kiểu này. | Submodule clone riêng không build được. `three` nằm ngoài `node_modules` của game: bắt buộc alias `three` về game. |
| C. Kit ở repo cha, chép có kiểm tra | `pnpm kit:sync --target games/<g>` chép vào `src/kit/` kèm `kit-manifest.json` (sha256); `--check` chạy trong build | Giống hệt mẫu đang dùng cho giọng nói (`scripts/sync-space-voice-contract.mjs`). Mỗi game tự build. `three` lấy từ chính game. | Phải chạy sync khi kit đổi. Có bản sao trong mỗi repo. |

**Đề xuất: C.** Lý do: game là submodule riêng, đẩy riêng. Mẫu này đã chạy với `shared/voice`. Lỗi lệch bản bị build chặn.

## 6. Kiến trúc tách đề xuất

```
typing-game/
  shared/game-kit/                 nguồn chuẩn, TS, không media, có test riêng
    input/      keys.ts (IME), text.ts (typingText, normalizeWord)
    vocab/      types.ts, loader.ts (từ src/vocabulary.ts), picker.ts (WordPicker)
    typing/     letters, router, distance, picker, scorer, decks (từ src/td/typing, nhận config)
    platform/   rng, frame-loop, safe-storage, canvas-state
    learning/   event.ts (gameId là tham số), bridge.ts (postMessage, PARENT_ORIGIN, shared-music)
    speech/     speech.ts (settings hẹp)
    three/      model-loader (manifestUrl là tham số), model-contracts (kind mở rộng được),
                hero-rig (từ hero.ts), guide-rig (từ title-guide-scene.ts), particles, materials,
                textures, util, stage (bloom, cấp chất lượng, không trời sao)
    feedback/   hitstop, trauma, numbers, debris, reaction, tiers, audio-cues, kill-translation
    audio/      scene-audio (bộ phát, nhận bảng âm), mix
  scripts/sync-game-kit.mjs        chép + manifest + --check
  games/
    space-typing/   src/kit/ (bản chép); file cũ thành shim re-export, Space chạy y như cũ
    dragon-lane/    game mới (cổng 3005, dragon.typing-game.local)
    typing-defense/ src/td chuyển ra (cổng 3006, td.typing-game.local)
    typing-survival/ src/survival + feedback chuyển ra (cổng 3007, survival.typing-game.local)
```

Mỗi game mới có: `package.json` riêng (Vite 7, TS, `three@0.170.0` ghim giống Space), `index.html`, `src/kit/` (chép), `src/` của game, `public/assets/<game>/` (media, không vào Git), `docs/`, test ranh giới riêng.

**Media và model dùng chung**
- Model rồng, boss, quái có sẵn ở `games/space-typing/public/assets/space-typing/models/` (361 MB). Không chép.
- Play: thêm `location /assets/space-typing/models/` (alias tới thư mục trên) vào server nginx của game mới. URL trong manifest giữ nguyên.
- Dev: một plugin Vite nhỏ phục vụ đường dẫn đó từ thư mục của Space (giống `offlineVoskPlugin`). Không đưa vào `dist`.
- Model riêng của game: `public/assets/<game>/models/` + manifest riêng. Kit nhận `manifestUrl`, nạp được nhiều manifest.
- `media/media.config.json` chỉ có một khối `game` (`scripts/media/lib/sets.mjs` dùng `config.game.dir`). Phải đổi thành danh sách `games[]` trước lần `pnpm media:push` đầu tiên của game mới.
- `scripts/models/prepare-models.ts` ghi cứng `public/assets/space-typing/models`. Cần thêm `--root`, `--out`, `--url-base`, hoặc chuyển công cụ model (gồm `scripts/models/blender/`) lên `scripts/models/` của repo cha.

**Portal**
- Thêm 3 mục vào `games.json`. Thanh nav sẽ có 8 game, cần gom nhóm hoặc thu gọn; chạy `validate-portal-layout`.
- Sự kiện học: mỗi game gửi `gameId` của chính nó (`dragon-lane`, `typing-defense`, `typing-survival`).
- Smart Review, giọng nói: để giai đoạn sau.

## 7. Thứ tự tách

| Bước | Việc | Ghi chú |
|---|---|---|
| 0 | Chủ dự án tạo 3 repo GitHub (hoặc tạm để thư mục thường trong repo cha) | Tạo repo là việc của chủ dự án. |
| 1 | Dựng `shared/game-kit` + `sync-game-kit.mjs`; kit có test riêng | Chép từ Space, sửa `gameId`, type riêng, tham số manifest. |
| 2 | Space dùng kit qua shim | Không đổi hành vi. Chạy `pnpm check` của Space. |
| 3 | Mở rộng media tool (`games[]`) và công cụ model (`--out`) | Trước mọi media của game mới. |
| 4 | Tách TD | Lấy từ nhánh `feat/td-1a6` (mới nhất), không lấy bản cũ ở checkout chính. Thay 5 import bằng `src/kit`. Giữ test ranh giới, golden, balance. Xóa `td` khỏi `rollupOptions.input` của Space. |
| 5 | Tách Survival | Khi S0 đã commit trên `feat/survival-s0`. `feedback/` vào kit. Space giữ shim cho `kill-translation`. |
| 6 | Dựng Dragon Lane | Khung game, plugin phục vụ model của Space, game id `dragon-lane`. |
| 7 | Nối hạ tầng | games.json, nginx (2 file), `setup-nginx.sh`, `package.json`, `play.sh`, `scripts/play.sh`, `dev.sh`, `bootstrap.sh`, `validate-play-mode.mjs`, `.gitmodules`. |

Defense V4 (`src/defense`, `defense.html`) và Campaign 3D ở lại Space. Dragon Lane chép phần hình của V4, ghi nguồn.

## 8. Tài sản 3D cho Dragon Lane

**Anh hùng** (số clip đọc từ `manifest.json`)

| Model | Tam giác | Clip | Hợp với vai |
|---|---|---|---|
| `guides/draconis-v4` (rồng trắng đứng, cánh lông kem cam) | 31.226 | Guide_Idle, Wave, Flap, Hop, Bow, Talk | Đứng giữa bản đồ. **Thiếu** Attack, Cast, Hit, Death, Victory. Đã có rig JSON (`draconis-v4-rig.json`, `flight: "guide"`), nên có thể thêm clip bằng công cụ Blender có sẵn trên lưới của chủ dự án. Cần chủ dự án đồng ý. |
| `heroes/draconis-v2` (rồng đỏ vàng, cánh màng) | 22.000 | Fly, Idle_Hover, Boost, Attack_L/R/Both, Cast, Hit, Victory, Death, Intro | Đủ clip chiến đấu. Bay lượn ở giữa. Dùng ngay được. |
| `heroes/draconis-v3` (rồng bốn chân) | 60.000 | Fly, Idle_Hover, Boost, **Spit, Spit_Big**, Cast, Hit, Victory, Death, Intro | **Không có** Attack_L/R/Both (đề bài ghi nhầm). Gấp đôi trần hero 30.000: chỉ dùng bản medium. |
| `heroes/draconis` (v1) | 22.000 | như v2, thiếu Attack_Both | Dự phòng. |

**Quái thường**: 122 mục = 8 họ (angel, cosmic, devil, frost, nature, prism, rainbow, shadow) × 14 vai + 10 LOD. Mỗi model ~6.000 tam giác, chỉ có `Enemy_Idle`, không có xương. Hình dạng là tàu và biểu tượng vũ trụ nhìn từ trên. 10 model là bản sao tạm. Họ magma chỉ có ảnh 2D.
- Dùng tạm cho **quái bay** (lơ lửng, nhấp nhô, rung cánh bằng shader như `FLUTTER` ở `campaign3d/actors.ts`).
- Hợp rừng hơn cả: họ nature (lá, gỗ), sứa (`nature-healer`, `rainbow-healer`), bạch tuộc (`nature-leech`, `rainbow-leech`), `cosmic-leech`.
- **Không** model nào đi được bằng hai chân hay bốn chân.

**Boss**: 27 model (8 lieutenant, 10 tyrant, 8 warden, auriel-hero), ~30.000 tam giác, clip Boss_Idle_Hover, Hit, Death, Intro. Dáng đứng hai chân, hợp làm tướng hoặc boss đi bộ nếu gắn xương: `lieutenant-cosmic`, `tyrant-g06` (người máy), `lieutenant-devil`, `warden-devil` (quỷ), `tyrant-g04`, `warden-nature` (người cây). `lieutenant-nature` là bọ sáu chân. `tyrant-g03` là bản sao tạm.

**Khác**: `items/tower-*` (6), `defense-core`, `defense-gate`, `prop-crystal-a/b/c`: phong cách viễn tưởng, chỉ để thử. `skills/dragon-fireball`: đạn lửa của rồng. Ảnh 2D của TD: `cuong-thi` (có ảnh trước, bên, sau: đầu vào tốt cho Tripo), `thuong-luong` (thuồng luồng), cây vùng meadow.

**Còn thiếu**

| Nhóm | Thiếu gì |
|---|---|
| Quái đi bộ | Model có xương, hai chân và bốn chân, clip Walk, Run, Attack, Hit, Death, Skill. Tripo có gắn xương tự động cho dáng người, bốn chân và vài chuyển động mẫu: cần thử trước khi chốt. Công cụ Blender có sẵn cũng gắn xương theo JSON và nhận dạng bốn chân. |
| Hợp đồng model | Một `ModelKind` mới (ví dụ `units`) bắt buộc clip đi, đánh, trúng, chết. |
| Đám đông có xương | Đám đông hiện là InstancedMesh tĩnh. Quái đi bộ đông cần nướng chuyển động vào texture (VAT) hoặc giới hạn số SkinnedMesh. |
| Bản đồ rừng | Thông, bụi, đá, hoa tím xanh: model Tripo hoặc billboard vẽ. Đất và sông dựng thủ tục (được phép). |
| Phe ta | Lính chặn, bẫy, nhà phép, vật phẩm hỗ trợ, icon cửa hàng. |
| Âm thanh, nhạc, UI | Bộ âm riêng cho từng loại quái, rồng, bẫy. Âm hiện có là âm viễn tưởng (Kenney, Freesound). |

## 9. Rủi ro

| Rủi ro | Hậu quả | Cách giảm |
|---|---|---|
| `gameId` gắn cứng `space-typing` | Portal từ chối sự kiện học của game mới | Kit nhận `gameId`; test kiểm |
| Media tool chỉ một game | Model, âm của game mới không lên Drive, mất khi đổi máy | Làm bước 3 trước |
| Model dùng chung nằm trong Space | Đổi đường dẫn trong Space làm hỏng game khác | Ghi rõ hợp đồng URL `/assets/space-typing/models/`; test nạp manifest |
| Tách khi đang làm dở | Xung đột với worktree TD, Survival | Tách từ nhánh đã commit; không đụng `.wt-*` khi agent khác đang làm |
| Kit lệch giữa các game | Lỗi khó thấy | `kit:sync --check` trong build mỗi game |
| Quái đi bộ đông và có xương | Tụt khung hình | VAT, LOD, giới hạn SkinnedMesh; đo sớm |
| Phong cách quái vũ trụ | Lạc tông với rừng vẽ tay; chủ dự án đã chê hình tạm | Ưu tiên tạo quái mới bằng Tripo |
| Thêm clip cho v4 bằng script | Có thể chạm luật "AI không dựng model bằng code" | Chỉ thêm chuyển động trên lưới có sẵn; hỏi chủ dự án |
| Thêm tên miền | Cần sudo và tạo lại chứng chỉ | Gộp 3 tên miền vào một lần chạy `setup-nginx.sh` |
| Thanh nav portal chật | Vỡ bố cục | Gom nhóm; chạy kiểm tra bố cục |
