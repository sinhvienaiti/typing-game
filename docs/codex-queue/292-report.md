# Phiếu 292 · Bản chơi High / Medium cho rồng khí

**Trạng thái:** xong script, media và kiểm tự động, 05/11/2026. TypeScript qua; **1105/1105 test, 91/91 tệp qua** (1095 ca nền + 10 ca mới, không bỏ qua ca nào trong lượt cuối). Chờ Claude so hình Medium trong lab.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`; HEAD bắt đầu và kết thúc `6b9f26c`. Các đường dẫn tương đối dưới đây tính từ worktree, trừ báo cáo ở repo cha.

## Đã làm

- `scripts/models/qi-dragon-tiers.mjs`: lấy glTF Transform, meshoptimizer và sharp từ `node_modules` của Space Typing, chỉ khi chạy công cụ; đọc nguồn trong `art-src`, chỉ xuất vào `public/assets/immortality-cultivation/`. Chạy từ mọi thư mục làm việc vì đường dẫn tính từ chính script.
- Hai GLB giữ **25.990 tam giác, 17.607 đỉnh, 1 mesh, 1 skin, 40 khớp theo thứ tự `bone_00`…`bone_39`**. Không simplify, weld hay cắt mặt. Meshopt chỉ sắp lại dữ liệu; vị trí, gán khớp, trọng số float và inverse bind matrices được giữ nguyên. Quantize NORMAL 12 bit và UV 16 bit; không quantize POSITION hoặc WEIGHTS. Tư thế nghỉ được kiểm với sai số đọc/ghi TRS của NodeIO dưới `5e-7` mỗi thành phần; cây khớp và tên khớp khớp chính xác.
- Mỗi GLB chỉ còn **1 baseColor WebP**, High 2048² / Medium 1024², chất lượng 90. Bỏ normal, metallicRoughness và các texture thừa. Khai báo bắt buộc `EXT_meshopt_compression`, `KHR_mesh_quantization`, `EXT_texture_webp`; test giải mã bằng đúng MeshoptDecoder của Three.js mà kit dùng.
- `models/manifest.json`: version 1, mục `skills/qi-dragon` đúng `ModelManifestEntry`, URL trong `/assets/immortality-cultivation/` có khóa MD5, bytes, triangles, sockets, clips và size. Giữ các mục model khác nếu chạy lại. High/Ultra chọn High; Medium chọn Medium; Low không có tầng và `pickModelTier` trả `null`.
- `vfx/qi-dragon/qi-scales.webp`: xám, 1024², WebP lossless; test so MD5 toàn bộ mẫu ảnh giải mã với PNG gốc, nên giữ nguyên cả các biên lặp. Manifest đi kèm có URL, md5, bytes và kích thước.
- `tests/models/qi-dragon-tiers.test.ts`: 10 ca kiểm skin, cây khớp, bind matrices, texture, số mặt và từng tam giác kèm trọng số sau sắp đỉnh, extension, manifest/chọn tầng, mẫu vảy. Khi thiếu media/nguồn, cả nhóm bỏ qua kèm thông báo liệt kê tệp thiếu và lệnh tạo lại; không nạp dependency tạo model lúc đó.
- Báo cáo này: `docs/codex-queue/292-report.md` ở repo cha.

## Tệp đã sinh

Tiền tố: `public/assets/immortality-cultivation/`.

| Tệp | Bytes | MD5 |
| --- | ---: | --- |
| `models/skills/qi-dragon/qi-dragon.high.glb` | 1.293.268 | `3102c31927e96667ade92c250d31a8e3` |
| `models/skills/qi-dragon/qi-dragon.medium.glb` | 823.104 | `30091770006e12f185a4e2690661bb32` |
| `models/manifest.json` | 739 | `2f40ff4d662ba1dc2e188636d4825c01` |
| `vfx/qi-dragon/qi-scales.webp` | 307.618 | `0dfc6c900fd5890acf6be21d9d1c7e61` |
| `vfx/qi-dragon/manifest.json` | 368 | `1811d96374d1bdec4814128110aae46f` |

Nguồn chỉ đọc: `art-src/lab/models/qi-dragon/qi-dragon.rig.glb` = 15.513.892 bytes, MD5 `3086fd56e41c4207959fcd22b379ee16`; `qi-scales.png` = 370.672 bytes, MD5 `45075d924f4994f81a163eed4e4f8bcb`.

## Bộ nhớ texture GPU ước tính

Tính bảo thủ RGBA8, đủ chuỗi mipmap đến 1²: tổng `4 × cạnh²` ở từng mức mip. WebP giảm tệp tải, không giảm số byte texture đã giải mã trên GPU. Một texture dùng chung cho các bản sao rồng, không nhân theo số con.

| Tầng | BaseColor + mipmap | Vảy + mipmap | Tổng phần texture của rồng | Ngân sách toàn game theo phiếu |
| --- | ---: | ---: | ---: | ---: |
| Low | 0 | 0 khi không nạp nhánh rồng 3D | 0 | 64 MB |
| Medium | 5.592.404 bytes (5,33 MiB) | 5.592.404 bytes (5,33 MiB) | **11.184.808 bytes (10,67 MiB)** | 128 MB |
| High / Ultra | 22.369.620 bytes (21,33 MiB) | 5.592.404 bytes (5,33 MiB) | **27.962.024 bytes (26,67 MiB)** | 192 MB cho High |

Đây là phần texture tăng thêm của rồng; không tính các asset khác, geometry, bone texture hoặc render target. Nếu bên gọi vẫn nạp vảy ở Low thì riêng vảy thêm 5,33 MiB; script và manifest không tự điều khiển việc nạp VFX của presenter.

## Kiểm đã chạy

Các lệnh chạy tại worktree, qua `.local/bin/heavy.sh` ở repo cha (`--cores=2` cho script/tsc, `--cores=4` cho Vitest):

```sh
node scripts/models/qi-dragon-tiers.mjs --inspect
node node_modules/typescript/bin/tsc --noEmit -p .
VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4 --reporter=dot
```

- Script: exit 0, đã ghi đủ 5 tệp; đọc lại hai GLB qua NodeIO sau nén để kiểm số mặt, skin, bind matrices và kích thước texture.
- TypeScript: exit 0, không lỗi.
- Vitest: exit 0; **91 tệp, 1105 ca qua**, 15,06 giây. Nhóm mới gồm 10 ca đều chạy với media thật; 1095 ca nền vẫn qua.
- `git diff --check`: qua. Không đổi HEAD, không lệnh Git ghi, không commit/push hay đồng bộ media. Không chạy build hoặc mở cổng mạng.

Lượt kiểm đầu bắt thiếu `KHR_mesh_quantization`: glTF Transform 4.5.1 dò extension theo POSITION, trong khi script giữ POSITION float. Đã khai báo extension tường minh rồi tạo lại cả hai GLB. So khớp cây khớp kiểm chính xác tên/quan hệ; ma trận TRS dùng ngưỡng sai số float nêu trên, còn inverse binds và trọng số giữ chính xác.

## Tóm tắt glTF Transform inspect · Medium

Môi trường không có `@gltf-transform/cli`. Cờ `--inspect` gọi trực tiếp **`inspect(document)` của `@gltf-transform/functions` 4.5.1**, sau khi NodeIO mở lại `qi-dragon.medium.glb`; không cài thêm package. Dưới đây là phần tóm tắt dữ liệu API, không phải đầu ra lệnh CLI:

```json
{
  "scenes": { "properties": [{
    "name": "Scene", "rootName": "DragonRig",
    "bboxMin": [-0.24359, -0.21508, -0.496],
    "bboxMax": [0.22705, 0.13438, 0.50068],
    "renderVertexCount": 77970,
    "uploadVertexCount": 17607,
    "uploadNaiveVertexCount": 17607
  }] },
  "meshes": { "properties": [{
    "name": "tripo_mesh_10ae70bb-9f4b-40c5-8da2-d58dc5ba5e9d",
    "mode": ["TRIANGLES"], "meshPrimitives": 1,
    "glPrimitives": 25990, "vertices": 17607, "indices": ["u16"],
    "attributes": ["JOINTS_0:u8", "NORMAL:i16_norm", "POSITION:f32", "TEXCOORD_0:u16_norm", "WEIGHTS_0:f32"],
    "instances": 1, "size": 895434
  }] },
  "materials": { "properties": [{
    "name": "tripo_material_10ae70bb-9f4b-40c5-8da2-d58dc5ba5e9d",
    "instances": 1, "textures": ["baseColorTexture"],
    "alphaMode": "OPAQUE", "doubleSided": false
  }] },
  "textures": { "properties": [{
    "name": "Color_10ae70bb-9f4b-40c5-8da2-d58dc5ba5e9d",
    "uri": "", "slots": ["baseColorTexture"], "instances": 1,
    "mimeType": "image/webp", "compression": "",
    "resolution": "1024x1024", "size": 334924, "gpuSize": 5592404
  }] },
  "animations": { "properties": [] }
}
```

## Bỏ qua và phần Claude kiểm tiếp

- Không sửa game, presenter hay lab; không so hình/browser/video vì phiếu giao bước đó cho Claude. Claude nạp Medium qua manifest, so chi tiết với nguồn và thử bơi/uốn đủ góc trước khi nối phím 2.
- Không ghi `art-src`, không đổi liên kết `art-src`/`node_modules`, không cài thêm dependency. Lần thử `pnpm exec` gặp kiểm kho tự động gọi install rồi dừng vì `ERR_SQLITE_ERROR: unable to open database file`; đã chuyển sang executable hiện có bằng `node`, các kiểm bắt buộc đều hoàn tất.
- Script có cảnh báo native từ hai bản libvips sẵn trong cây dependency của Space Typing; exit vẫn 0 và cả hai GLB được decoder của kit đọc qua test. Không chỉnh dependency ngoài phạm vi phiếu.
- Không dùng ảnh sinh mới hay công cụ tạo ảnh; vảy chỉ được chuyển định dạng lossless từ PNG được chỉ định. Không có giới hạn chặn việc hoặc thời điểm cần chờ.
