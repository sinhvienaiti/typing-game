# Media và model của các game (23/10/2026)

> Bước S2 của [SPLIT_PLAN.md](SPLIT_PLAN.md) (mục 5). Hướng dẫn chung về kho media: [MEDIA_STORAGE.md](../MEDIA_STORAGE.md).

## 1. Tóm tắt

- Ảnh, âm thanh, model không vào Git ở repo nào. Chúng nằm trên Google Drive, đẩy và tải bằng `pnpm media:*`.
- Mỗi game có media riêng, danh sách md5 riêng (`media.md5` trong repo của game) và thư mục riêng trên Drive.
- Space Typing giữ nguyên mọi đường dẫn cũ. Không file nào của Space phải đẩy lại.
- Công cụ model nằm ở `scripts/models/` của repo cha. Không cờ thì chạy y như script của Space. Có cờ thì chạy cho game khác.
- Game chưa có thư mục trên máy thì lệnh bỏ qua, in một dòng báo, không lỗi.

## 2. Media của từng game ở đâu

Cấu hình: `media/media.config.json`, mảng `games[]`. Space đứng đầu.

| Game | Thư mục | `originals` | `runtime` | Danh sách md5 | Trên Drive |
|---|---|---|---|---|---|
| Space Typing | `games/space-typing` | `art-src/**` | media chưa vào Git trong game, chủ yếu `public/assets/space-typing/**` | `games/space-typing/media.md5` | `repo/games/space-typing/` |
| Rồng Giữ Ải | `games/dragon-hold` | `art-src/**` | chủ yếu `public/assets/dragon-hold/**` | `games/dragon-hold/media.md5` | `repo/games/dragon-hold/` |
| Lời Gọi | `games/typing-defense` | `art-src/**` | chủ yếu `public/assets/typing-defense/**` | `games/typing-defense/media.md5` | `repo/games/typing-defense/` |
| Tuyến Cuối | `games/typing-survival` | `art-src/**` | chủ yếu `public/assets/typing-survival/**` | `games/typing-survival/media.md5` | `repo/games/typing-survival/` |

- `runtime` là **mọi** file media trong thư mục game mà Git không theo dõi. `.gitignore` không quyết định gì. Bỏ qua `node_modules`, `dist`, `.git`, `.visual`, `art-src`, `coverage`.
- Nhóm `private` (nhạc, âm thanh riêng) dùng chung, như cũ: `media/private.md5`, Drive `private/`.
- Bản sao danh sách trên Drive: `_locks/<thời điểm>/<id>.media.md5` cho từng game. Space vẫn là `space-typing.media.md5`.
- Model của mỗi game nằm ở `public/assets/<id>/models/`, manifest `public/assets/<id>/models/manifest.json`. URL: `/assets/<id>/models/<loại>/<tên>/<tên>.<high|medium>.glb?v=<mã>`.
- Mỗi game mới cần `.gitignore` chặn media: `art-src/*` (trừ `art-src/3d/SOURCES.json`, README), file media trong `public/assets/<id>/`. Manifest JSON thì vào Git.

## 3. Lệnh media

Chạy trong thư mục `typing-game`. Một lệnh làm cho mọi game có thư mục trên máy.

```bash
pnpm media:status                 # không cần mạng; in theo từng game, rồi nhóm dùng chung
pnpm media:push --dry-run         # xem trước, không đụng Drive
pnpm media:push                   # đẩy; ghi media.md5 của từng game có thay đổi
pnpm media:pull                   # tải file còn thiếu của mọi game
pnpm media:check --remote         # kiểm tra cả Drive
pnpm media:test                   # test của kho media (không cần Drive thật)
```

- Một lần đẩy dùng một thời điểm chung cho mọi game. Mọi câu hỏi và mọi kiểm tra chạy trước khi đẩy file nào.
- Sau khi đẩy, script in lệnh commit cho từng game có `media.md5` mới. Commit trong repo của game đó, rồi cập nhật con trỏ ở repo cha.
- `--forget` và `--readd` nhận đường dẫn tính từ repo cha, ví dụ `games/dragon-hold/art-src/units/a.png`.
- `pnpm media:pull` chạm `games/<id>/.media-pulled` của game vừa có file mới. Hiện `./play.sh` chỉ theo dõi file này của Space. Ba game mới cần thêm nó vào đầu vào build của mình (làn hạ tầng S3).

## 4. Lưu GLB Tripo cho từng game

Quy tắc giống Space: `art-src/3d` soi gương cây ảnh 2D.

| Ảnh 2D (bản gốc) | GLB Tripo lưu ở |
|---|---|
| `games/<id>/art-src/<đường dẫn>/<tên>.png` | `games/<id>/art-src/3d/<đường dẫn>/<tên>.glb` |
| Không có ảnh (Text to 3D) | `games/<id>/art-src/3d/skills/<tên>.glb` hoặc `art-src/3d/items/<tên>.glb` |

Ví dụ cho Rồng Giữ Ải: ảnh `games/dragon-hold/art-src/enemies/withered-wolf.png`, GLB `games/dragon-hold/art-src/3d/enemies/withered-wolf.glb`.

Các bước sau khi tải GLB từ Tripo:

1. Đặt tên GLB theo ảnh 2D, lưu vào `art-src/3d/...` như bảng trên. Không sửa file gốc này.
2. Ghi chỉ mục: `pnpm models:index --root games/dragon-hold`. Lệnh ghi `games/dragon-hold/art-src/3d/SOURCES.json` (md5, cỡ, ảnh 2D, ai đọc file).
3. Commit `SOURCES.json` trong repo của game.
4. Đẩy bản gốc: `pnpm media:push --only originals`.

Space giữ cách cũ: `node games/space-typing/scripts/models/index-3d-sources.mjs`, hoặc `pnpm models:index` (không cờ). Hai lệnh cho ra cùng một file.

## 5. Đóng gói model

| Lệnh (repo cha) | Làm gì |
|---|---|
| `pnpm models:blender --root games/<id>` | Đọc preset, cho từng GLB Tripo qua Blender (xoay, đặt kích cỡ, giảm tam giác, ổ cắm `FX_`, clip), ghi `art-src/models/<loại>/<tên>.glb`, rồi gọi `models:prepare` với cùng cờ |
| `pnpm models:prepare --root games/<id>` | Đóng gói `art-src/models/<loại>/<tên>.glb` thành bản High và Medium, ghi manifest |
| `pnpm models:prepare --root games/<id> --manifest-only` | Không đóng gói; tính lại `?v=` của mọi file và ghi lại manifest |
| `pnpm models:prepare --root games/<id> --import <manifest khác> --only <khoá>` | Chép bản đã đóng gói từ game khác, đổi URL sang game này |
| `pnpm models:index --root games/<id>` | Ghi `art-src/3d/SOURCES.json` |
| `pnpm models:test` | Test của công cụ model |

Cờ chung:

| Cờ | Mặc định | Ý nghĩa |
|---|---|---|
| `--root <thư mục game>` | `games/space-typing` | Game cần làm |
| `--out <thư mục model public>` | `<root>/public/assets/<id>/models` | Nơi ghi GLB và `manifest.json` |
| `--url-base </assets/<id>/models/>` | `/assets/<id>/models/` | Đầu URL trong manifest |
| `--art-src <thư mục>` | `<root>/art-src` | Nơi có `3d/` và `models/` |

- `<id>` là tên thư mục game. Chỉ cần `--root`, ba cờ còn lại tự suy ra.
- Không cờ nào: chạy y như script của Space.
- Cờ riêng: `--only <loại>/<tên>[,…]`, `--force`, `--contracts <file>`, `--generated-at <thời điểm ISO>` (cho `models:prepare`); `--preset`, `--kind`, `--kinds`, `--blender`, `--dry-run`, `--no-package` (cho `models:blender`).
- Preset mặc định: `<root>/scripts/models/presets/campaign3d-models.json`. Mẫu khoá: `"enemies/withered-wolf": { "source": "enemies/withered-wolf.glb", "triangles": 6000, "reviewed": false }`.
- Hợp đồng model của game: `src/render3d/model-contracts.ts`, hoặc `src/kit/three/model-contracts.ts` (bản chép từ kit). Khác chỗ thì dùng `--contracts`.
- Thư viện đóng gói (gltf-transform, sharp, meshoptimizer) lấy từ `node_modules` của game. Game chưa cài thì mượn của Space.

## 6. Ba GLB Rồng cho Rồng Giữ Ải

Rồng Giữ Ải có **bản riêng** của ba model Rồng trong media của mình (quyết định D22). Không đọc chung file của Space.

| Model | Lấy tầng | Nguồn trong Space | Đích trong Rồng Giữ Ải |
|---|---|---|---|
| `heroes/draconis-v2` | High, Medium | `public/assets/space-typing/models/heroes/draconis-v2/` | `public/assets/dragon-hold/models/heroes/draconis-v2/` |
| `heroes/draconis-v3` | Medium | `public/assets/space-typing/models/heroes/draconis-v3/` | `public/assets/dragon-hold/models/heroes/draconis-v3/` |
| `guides/draconis-v4` | High, Medium | `public/assets/space-typing/models/guides/draconis-v4/` | `public/assets/dragon-hold/models/guides/draconis-v4/` |

Lệnh chép (chạy một lần, khi `games/dragon-hold` đã có):

```bash
SPACE_MANIFEST=games/space-typing/public/assets/space-typing/models/manifest.json
pnpm models:prepare --root games/dragon-hold --import $SPACE_MANIFEST --only heroes/draconis-v2,guides/draconis-v4
pnpm models:prepare --root games/dragon-hold --import $SPACE_MANIFEST --only heroes/draconis-v3 --tiers medium
pnpm media:push --only runtime
```

- Lệnh chép file GLB, rồi ghi vào `games/dragon-hold/public/assets/dragon-hold/models/manifest.json` với URL `/assets/dragon-hold/models/...` và `?v=` mới. Không cần Blender.
- Sau đó commit `manifest.json` và `media.md5` trong repo `dragon-hold`. GLB không vào Git; nó lên Drive ở `repo/games/dragon-hold/public/...`.
- Bản gốc Meshy của bốn model Draconis đã mất (`noOriginalOnThisMachine` trong `SOURCES.json` của Space). Chỉ còn bản đã đóng gói. Nếu tìm lại được, lưu ở `games/space-typing/art-src/3d/heroes/<tên>.glb`.
- Bước S2 không chép file nhị phân nào. Việc chép làm ở M0 của Rồng Giữ Ải.

## 7. Giới hạn cần biết

- Bộ Blender (`scripts/models/blender/space_typing_model_tools.py`) giống hệt file của Space. Nó chỉ nhận loại `ships`, `enemies`, `bosses`, `skills`, `items`, `heroes`, `guides`. Loại mới (ví dụ `units`, `props`) cần sửa bộ Blender trước.
- `models:blender` ghi vào `<root>/art-src`, nên không nhận `--art-src`.
- Chạy `models:blender` cho Space sẽ build lại mọi model: khoá cache tính cả file đóng gói của repo cha. Kết quả giống hệt, chỉ tốn thời gian. Space cứ dùng script của mình.
- Tàu của Space (`ships:models:prepare`) chưa chuyển lên repo cha.
- Tuyến Cuối đọc model của Space qua URL `/assets/space-typing/models/`, không chép (SPLIT_PLAN mục 5).

## 8. Đã kiểm chứng (23/10)

- Danh sách file của Space (originals 1.084, runtime 423, private 208), đường dẫn danh sách md5 và thư mục Drive: code cũ và code mới cho kết quả giống hệt trên máy này.
- Đẩy thử trên Drive giả (thư mục cục bộ): code cũ và code mới tạo cùng cây file, cùng `media.md5`, cùng `private.md5`.
- `pnpm models:index` (không cờ, ghi ra thư mục tạm) giống từng byte `games/space-typing/art-src/3d/SOURCES.json`.
- `pnpm models:prepare --manifest-only` trên các file model của Space giống từng byte `manifest.json` của Space (189 model).
- Đóng gói hai model bằng script của Space và bằng `scripts/models`: bốn GLB và manifest giống từng byte.
