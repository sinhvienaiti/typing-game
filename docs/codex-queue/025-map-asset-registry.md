# Phiếu 025 · Map Factory · Sổ model 3D của ba game (chỉ đọc media, không trình duyệt)

**Bối cảnh:** chủ dự án chọn hướng "Map Factory" (27/10/2026): bản đồ được sinh từ một bản mô tả (MapSpec) và một seed, rồi đặt model lấy từ thư viện có sẵn.

Bộ sinh nào cũng cần một sổ ghi từng model: cỡ thật, số tam giác, có xương không, nguồn ở đâu. Phiếu này làm sổ đó. Phần kiến trúc còn lại Claude đang đánh giá, nhưng sổ model không phụ thuộc vào kết quả đánh giá.

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `tools/map-factory/registry/scan-assets.mjs`: Node ESM, không TypeScript.
- `tools/map-factory/registry/package.json`, chỉ khi dùng `@gltf-transform/core`. Cài bằng `pnpm install --offline`. Không cài được offline thì tự đọc GLB: header 12 byte, chunk JSON, chunk BIN.
- `tools/map-factory/registry/out/assets.dragon-hold.json`, `assets.typing-defense.json`, `assets.space-typing.json`: văn bản.
- `tools/map-factory/registry/test/*.test.mjs`: chạy bằng `node --test`.
- `tools/map-factory/registry/README.md`: tiếng Việt có dấu.
- `docs/codex-queue/025-report.md`.

**Cấm:**
- ghi bất cứ gì vào `games/**`;
- sửa, chép, xóa media (`.glb`, `.png`, `.webp`, `.bin`…);
- lệnh git có ghi;
- mạng;
- mở dev server;
- đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`).

Ba làn của Claude đang chạy trong `games/dragon-hold`, `games/typing-defense`, `games/typing-survival`, nên không chạy test hay build của game nào.

## Nguồn đọc

`public/assets` và `art-src` có thể là symlink: phải đi theo symlink.

1. **Bản chạy trong game** (đã chuẩn cỡ, giảm mặt, có thể nén meshopt), gồm manifest và GLB:
   - `games/dragon-hold/public/assets/dragon-hold/models/**`: 54 GLB. Manifest: `m0b/manifest.json` và các manifest khác nếu có.
   - `games/typing-defense/public/assets/typing-defense/models/**`: 68 GLB, `manifest.json`.
   - `games/space-typing/public/assets/space-typing/models/**`: 378 GLB, `manifest.json`. Tuyến Cuối dùng thư viện này.
2. **Bản gốc Tripo của chủ dự án:** `games/<game>/art-src/3d/**` và `SOURCES.json` (md5, ảnh 2D gốc, `usedBy`).

## Trường của mỗi mục

- **Định danh:** `id` là đường dẫn trong `models/` bỏ đuôi, ví dụ `enemies/moss-grunt`; kèm `game`, `file` (đường dẫn từ gốc repo), `bytes`.
- **Loại:**
  - `category` lấy theo thư mục đầu: `enemies`, `props`, `houses`, `buildings`, `units`, `heroes`, `bosses`…
  - `tags` đoán thô từ tên file: `tree`, `pine`, `rock`, `bush`, `bridge`, `house`, `tower`, `fence`… Ghi `"tagsSource": "auto"`. Đây chỉ là gợi ý.
- **`bounds`:**
  - `min`, `max`, `size` tính bằng mét, theo cảnh mặc định (scene 0).
  - Có tính transform của node (ma trận hoặc TRS): lấy hộp min/max của accessor POSITION, biến đổi 8 góc hộp qua ma trận thế giới.
  - Ghi thêm `footprint` (x × z) và `height` (y).
- **Trục:** giả định +Y hướng lên. Ghi `longestAxis`; với sinh vật thì cảnh báo khi cạnh dài nhất là X hoặc Z. Không sửa gì.
- **Hình khối:** `triangles` là tổng của mode TRIANGLES; strip và fan quy đổi ra tam giác; mesh dùng chung thì nhân theo số node dùng nó. Kèm `meshes`, `primitives`, `materials`, `textures`: số ảnh và cỡ ảnh đọc từ header PNG, JPEG hay WebP; KTX2 thì ghi `"ktx2"`.
- **Chuyển động:** `skinned` (có skin hay không), `animations` (tên clip, thời lượng tính bằng giây).
- **Phần mở rộng:** `extensions`, ví dụ `EXT_meshopt_compression`, `KHR_texture_basisu`, `KHR_draco_mesh_compression`.
- **Nguồn:**
  - `source` là `"runtime"` hoặc `"original"`.
  - Với bản runtime, nối tới bản gốc khi tìm được (cùng id dưới `art-src/3d` hoặc trong `SOURCES.json`) và ghi md5 bản gốc.
- **`licence`:** `"owner-tripo"` cho model trong `art-src/3d` của game, `"space-library"` cho thư viện Space, `"unknown"` khi không rõ. Không đoán thêm.
- **`manifest`:** mục manifest tương ứng nếu có, giữ nguyên các trường cỡ, scale, preset.

**GLB nén meshopt:** JSON vẫn đọc được. Số đỉnh và số tam giác lấy từ `count` của accessor, không cần giải nén. `min`/`max` của accessor POSITION bắt buộc phải có theo chuẩn glTF. Nếu thiếu thì ghi `null` và đưa vào danh sách "cần giải nén" trong báo cáo.

## Kiểm (bắt buộc)

1. `node tools/map-factory/registry/scan-assets.mjs` chạy xong cả ba game và in ra tổng số file, số lỗi.
2. `node --test tools/map-factory/registry/test` đạt. Test gồm:
   - một GLB nhỏ dựng trong bộ nhớ: một tam giác, một node có scale 2. Bounds và số tam giác phải đúng.
   - mỗi game một file thật, so số tam giác với một cách đếm thứ hai.
3. Đối chiếu bốn bản gốc với số đã biết (3D_IMPORT 26/10):

   | File | Tam giác |
   |---|---:|
   | `games/dragon-hold/art-src/3d/enemies/moss-grunt.glb` | 5.708 |
   | `games/dragon-hold/art-src/3d/enemies/blight-wolf.glb` | 5.637 |
   | `games/dragon-hold/art-src/3d/generals/moss-banner.glb` | 8.382 |
   | `games/dragon-hold/art-src/3d/houses/herb-hut.glb` | 9.858 |

   Lệch thì ghi lý do.
4. md5 của mọi GLB đã đọc, trước và sau khi chạy, không đổi. Đây là bằng chứng không ghi vào media.
5. `git status --short` chỉ có file trong `tools/map-factory/registry/` và `docs/codex-queue/025-report.md`.

## Báo cáo `docs/codex-queue/025-report.md`

- Số model của mỗi game, chia theo `category`.
- Mười model nhiều tam giác nhất của mỗi game.
- Model có cỡ lạ (cao hơn 30 m hoặc thấp hơn 0,05 m) hoặc trục lạ.
- Các lỗi khi đọc file.
- Kết quả năm lệnh kiểm, kèm số.

**Xong khi:** ba file sổ có đủ trường và năm lệnh kiểm đều đạt.
