# Báo cáo phiếu 291 · Hai khóa bóng còn muộn của Kim

**Hoàn tất mã và kiểm tự động.** TypeScript qua; **1031/1031 test, 94/94 tệp** qua; build wrapper 274 qua, grep sạch và đã xóa đầu ra. Chưa đo lại cổng 7; Claude đo khi máy rảnh. Không commit, gộp hoặc dùng lệnh Git ghi.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD giữ `672f2e7`. Hai link `?? art-src`, `?? node_modules` giữ nguyên.

## Nguyên nhân và khóa đầy đủ

Đã đọc `recheck-merge/control/stall-ids-{fire,metal}.json`, `stall-probe-metal.json`, `first-compile-metal-1.json` và số đối chứng. Kim có đúng hai lượt link ở khung 7, sau khung trúng đầu 6. Log chỉ lưu một phần define và độ dài nguồn, **không lưu `cacheKey` đầy đủ**; các khóa dưới được dựng lại bằng chính `WebGLPrograms.getParameters/getProgramCacheKey` của Three r170, đối chiếu nguồn game và metadata GLB Lam, không phải đọc từ GPU.

| Thuộc tính | Skinned | Instanced |
| --- | --- | --- |
| Vật thể | Lam, bản đang dùng có 31 xương | Kiếm `BladeSet` có map |
| Chương trình | `MeshDepthMaterial`, shader ID `depth`, tên rỗng | Cùng loại |
| Define đặc trưng | `USE_MAP`, `MAP_UV uv`, `USE_SKINNING`, `FLIP_SIDED`, `USE_SHADOWMAP`, `SHADOWMAP_TYPE_PCF_SOFT`, `DEPTH_PACKING 3201` | Đổi `USE_SKINNING` thành `USE_INSTANCING` |
| GLSL vertex/fragment | **14842/12228** ký tự | **14844/12228** ký tự |
| Map/alpha | Map UV0; `alphaMap = null`, `alphaTest = 0`; không alpha hash/coverage | Cùng cấu hình |
| Side | Vật liệu thân `FrontSide`, `shadowSide = null` → bóng `BackSide` | Cùng cấu hình |
| Vật liệu độ sâu | Mặc định của `WebGLShadowMap`; không `customDepthMaterial`, define hoặc hook riêng | Cùng cấu hình |
| Bóng/đèn | `PCFSoftShadowMap` (2); 3 đèn hướng, 1 đèn điểm, 1 bán cầu; 1 bóng hướng, 0 bóng điểm/spot | Cùng cấu hình |
| Đích/màu | Target bóng tuyến tính, `NoToneMapping`; renderer xuất sRGB | Cùng cấu hình |
| Phần còn lại | `highp`, vertex texture bật; không sương, clipping, morph, displacement, màu đỉnh hoặc log/reverse depth | Không màu/morph theo instance |

Số xương không nằm trong khóa của r170: skinning đọc bone texture. `customProgramCacheKey` mặc định là chuỗi của `onBeforeCompile` rỗng. Toàn bộ khóa dựng lại:

```text
SKINNED
depth,highp,srgb-linear,false,,uv,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,,false,false,0,,3,1,0,0,1,0,1,0,0,0,0,2,0,0,0,3201,1,144416,srgb,onBeforeCompile( /* shaderobject, renderer */ ) {}

INSTANCED
depth,highp,srgb-linear,false,,uv,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,,false,false,0,,3,1,0,0,1,0,1,0,0,0,0,2,0,0,0,3201,3,144384,srgb,onBeforeCompile( /* shaderobject, renderer */ ) {}
```

**Điểm khác 286:** khóa chứa `numPointLights` dù vật liệu độ sâu không dùng ánh sáng. `drawActorMask()` giấu nhóm FX và ba `FlashLights`, để lại 1 đèn điểm trong trạng thái ánh sáng của scene. Three r170 gọi `shadowMap.render()` **trước** `setupLights()` ở khung kế tiếp (`WebGLRenderer.js`), nên bóng sau trúng dùng trạng thái đó. Hai lượt `compile()` trong 286 lại đặt trạng thái thành 4 đèn điểm. Khóa 286 giống các khóa trên, chỉ thay cụm số đèn `3,1,0,0,1` thành `3,4,0,0,1`; shader vẫn giống nhau. Đây là lý do bật thêm `castShadow` chưa giải quyết được.

## Tệp đã ghi

Các đường sau tính từ worktree, trừ báo cáo này ở repo cha:

| Tệp | Thay đổi |
| --- | --- |
| `src/view/renderer.ts` | Callback làm ấm sau compile, trước render; đặt lại target 64×64 sau callback. Bổ sung khôi phục background, override material, màu/alpha xóa và `autoClear` nếu host vẽ mask ném lỗi; giữ đường khôi phục mesh/bóng hiện có. |
| `src/view/skills/element-stage.ts` | Chuyển callback qua điểm vào prewarm chung. |
| `src/lab/skills-main.ts` | Upload mask trước compile; gọi `screen.prewarm()` bằng callback, dùng pass mask thật để tạo đúng trạng thái ánh sáng trước bóng. Chỉ đổi phần làm ấm. |
| `tests/view/skill-prewarm-shared.test.ts` | Thêm 3 ca so khóa đầy đủ và khôi phục khi thành công/lỗi mask/lỗi bóng. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Ghi nguyên nhân, cách sửa và kết quả kiểm. |
| `docs/codex-queue/291-report.md` ở repo cha | Báo cáo này. |

Không cần sửa `screen-fx.ts`. Không tạo mesh/vật liệu bóng thay thế trong runtime: chính Lam, các kiếm và vật liệu độ sâu thật của scene đi qua shadow pass. Giữ một lượt vẽ scene 64×64 mỗi hệ; lượt mask/impact chỉ đổi vị trí trong chuỗi làm ấm. Không đổi hình, số, nhịp, sim, RNG, art hoặc âm thanh.

## Kiểm bắt buộc

Chỉ chạy trong worktree được giao, qua `.local/bin/heavy.sh` của repo cha:

1. **PASS**, thoát 0: `node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **PASS**, thoát 0: `VITEST_MAX_THREADS=4 …/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: **1031/1031 test, 94/94 tệp**. Tệp prewarm **17/17**, thêm 3 ca so với mốc 1028.
3. Test dùng **`WebGLShadowMap` và `WebGLLights` thật**, gọi hàm tạo toàn bộ khóa của Three r170. Chỉ thay adapter render/GPU để chạy trong Node. Fixture Lam giữ các thuộc tính khóa đã đọc từ model thật; kiếm dùng lớp `BladeSet` thật và model có map. Hai khóa prewarm trùng khóa sau mask khi kiếm được phát; đối chứng thứ tự 286 tạo hai khóa khác. Kiểm ngay sau prewarm: count/ma trận, culling, đổ bóng, visibility, scene, màu/alpha xóa, `autoClear`, target và cờ cập nhật bóng được trả lại, cả khi host vẽ mask ném lỗi trước đoạn khôi phục của nó hoặc khi lỗi bóng; pool/đồng hồ không đổi.
4. **PASS build**, thoát 0: wrapper `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ đổi chuỗi thư mục trong bộ nhớ từ `/private/tmp/codex-274-dist` sang `/private/tmp/codex-291-dist`; đủ `--no-cache --configLoader runner --outDir`, cache riêng `/private/tmp/codex-291-dist/.vite-cache`, thư mục đầu ra mới. Không sửa wrapper.
5. **PASS grep**: `grep -rlE 'fxcode|stripK|prewarmReport' /private/tmp/codex-291-dist` không in gì, thoát 1 đúng nghĩa không tìm thấy. **Đã xóa** `/private/tmp/codex-291-dist`.
6. `git diff --check` sạch; chỉ sửa các đường được phép. Không đụng link có sẵn hoặc thay đổi của luồng khác.

Log tạm: `/private/tmp/codex-291-tsc.log`, `codex-291-prewarm.log`, `codex-291-vitest.log`, `codex-291-build.log`, `codex-291-bundle-scan.log` (đều trong `/private/tmp`).

## Bàn giao

Claude đo lại cổng 7 trên máy rảnh: đặc biệt Kim trúng +1 không còn hai lượt link độ sâu; xác nhận khung bấm phím và khung trúng đạt ≤ 11,5 ms, rồi xử lý commit/fast-forward theo phiếu. Kiểm tự động ở đây chứng minh khóa khớp; chưa chứng minh thời gian GPU thực tế.

Không chạy trình duyệt, mở cổng mạng hoặc tạo capture vì phiếu giao phần đo cho Claude. Không chạy build/test của game chính hay game khác. Không gặp hạn mức hoặc mốc giờ phải đợi; không có phần mã còn bỏ dở.
