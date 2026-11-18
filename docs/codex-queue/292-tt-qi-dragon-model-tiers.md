# Phiếu 292 · Tu Tiên · Code: script tạo bản chơi cho model rồng khí (High, Medium)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/292-report.md`.

**Worktree:** `games/.wt-ic-dragon-swarm`, nhánh `claude/dragon-swarm-lab`, HEAD `6b9f26c`. `art-src` là link của Claude (đọc được, **không ghi**). `node_modules` là link: không đụng. **Không lệnh git ghi.**

## Vì sao
Anh đã duyệt bầy rồng khí (lab, `?key2=energy`). Để đưa vào bản chơi cần model đi qua `public/assets/immortality-cultivation/` theo manifest (hiện mọi thứ nạp từ `/art-src/lab/...`, bản build không có). Model hiện tại `art-src/lab/models/qi-dragon/qi-dragon.rig.glb`: 15,5 MB, 1 mesh skinned 40 xương (`bone_00`…`bone_39`), khoảng 17,6k đỉnh, 3 texture 4096² (baseColor, normal, metallicRoughness). Shader rồng khí chỉ đọc **baseColor**. Ngân sách texture theo tầng: 64 / 128 / 192 MB (Low / Medium / High); Low không nạp 3D (`pickModelTier`).

## Việc
1. Viết `scripts/models/qi-dragon-tiers.mjs`, theo cách `games/dragon-hold/scripts/models/m0b-tiers.mjs` và `m0b-strip.mjs` lấy gltf-transform, meshoptimizer, sharp (từ `node_modules` của Space Typing, chỉ lúc build):
   - đầu vào: `art-src/lab/models/qi-dragon/qi-dragon.rig.glb`, `art-src/lab/models/qi-dragon/qi-scales.png`;
   - **High:** baseColor WebP 2048²; **Medium:** baseColor WebP 1024²; cả hai **bỏ** normal và metallicRoughness;
   - **giữ nguyên** mọi tam giác, skin, khớp và tên xương (luật chủ: chi tiết hơn nhẹ; chỉ cắt khi đo thấy chậm);
   - nén meshopt và quantize sao cho loader của kit đọc được (`src/kit/three/model-loader.ts` có `setMeshoptDecoder`); không làm sai trọng số skin;
   - ghi `public/assets/immortality-cultivation/models/skills/qi-dragon/qi-dragon.high.glb`, `qi-dragon.medium.glb`, mục manifest theo đúng kiểu `ModelManifestEntry` mà `pickModelTier` đọc (tầng high, medium; low không có);
   - chuyển `qi-scales.png` thành `public/assets/immortality-cultivation/vfx/qi-dragon/qi-scales.webp` (xám, giữ lặp liền mạch, 1024²) và `manifest.json` của thư mục đó (md5, bytes).
2. Test `tests/models/qi-dragon-tiers.test.ts` (đọc tệp đã sinh bằng gltf-transform `NodeIO`; bỏ qua có thông báo nếu tệp chưa có): 1 skin, 40 khớp đúng tên, chỉ 1 texture baseColor với cạnh 2048/1024, số tam giác bằng bản gốc, có `EXT_meshopt_compression` nếu đã dùng.

### Được ghi
`scripts/models/qi-dragon-tiers.mjs`, `tests/models/qi-dragon-tiers.test.ts`, các tệp sinh ra dưới `public/assets/immortality-cultivation/` (không commit, không push media), `docs/codex-queue/292-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; `pnpm media:push`; ghi vào `art-src`; sửa mã game hay lab; mở cổng mạng.

## Kiểm bắt buộc
1. Chạy script; ghi kích thước từng tệp và ước tính bộ nhớ texture trên GPU mỗi tầng.
2. `tsc --noEmit -p .` không lỗi; Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`) qua, mốc 1095 test.
3. Mở thử `qi-dragon.medium.glb` bằng gltf-transform `inspect` và dán phần tóm tắt vào báo cáo.

## Claude làm sau
Nạp tầng Medium trong lab, so hình với bản gốc, rồi dùng trong presenter phím 2.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
