# Phiếu 258 · Tu Tiên · Code: `FlipbookPool` bản 2 (gói CX-B)

> **BẢN NHÁP, CHƯA XONG.** Dừng 13:51 ngày 04/11 theo giờ chặn của chủ dự án. ChatGPT tự duyệt lần 1 ra **FAIL** (đang viết bản sửa); Gemini chưa chạy. Còn lại: xem `docs/codex-queue/258/PROGRESS.md` và mục "Lỗi ChatGPT nêu ở lượt duyệt 1" cuối phiếu. **Chưa giao Codex.**

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`: shader, manifest và tương thích ngược). Lời giải đã chốt ở mục "Việc"; Codex không thiết kế lại.

**Báo cáo:** `docs/codex-queue/258-report.md` (tiếng Việt).

## Bối cảnh
- Kế hoạch: `docs/games/tu-tien/skills/INTEGRATION_PLAN_2026-11-04.md` §2.2–2.6, §2.8, §3 hàng CX-B, §7. Kế hoạch đó là **bản nháp lộ trình**; gói này có lượt duyệt hai lần riêng:
  - `docs/games/tu-tien/skills/source/flipbook-v2-chatgpt-2026-11-04.md`;
  - `docs/games/tu-tien/skills/source/flipbook-v2-gemini-2026-11-04.md`.
- Số phiếu: kế hoạch §7 ghi `257-tt-flipbook-v2`; ghi chú đầu kế hoạch dời mọi số lên một bậc, nên CX-B là **258**.
- **Mã hiện tại** (`games/immortality-cultivation`, HEAD `bc94110`, Claude đã đọc):
  - `src/view/skills/flipbook.ts`: `parseFlipbookManifest(value, base)` trả `Map<string, FlipbookMeta>`; `FlipbookMeta` = `id, url, cols, rows, frames, fps, loop, mode, aspect, pivot, start, heading`; trường lạ bị bỏ qua.
  - `FlipbookLibrary.load` nạp atlas bằng `THREE.TextureLoader`, `SRGBColorSpace`, `premultiplyAlpha = false` (alpha thẳng, shader premultiply một lần).
  - `FlipbookPool(id, mode, capacity, renderOrder, blank)`: một `InstancedBufferGeometry`, một `ShaderMaterial`, một lệnh vẽ; trộn `CustomBlending` ONE / ONE_MINUS_SRC_ALPHA (alpha ZERO / ONE). Thuộc tính instance: `iPos`(3), `iData`(4: size, angle, frame, alpha), `iColor`(4), `iDir`(4), `iAge`(4: x tuổi/đời, y mốc `cool`, z seed, w `erode`), `iLift`(2). Trạng thái CPU `STRIDE = 35`.
  - `attach(meta, texture)` được gọi ở `FlipbookPlayer` (flipbook.ts dòng ~854 và ~870).
  - Fragment: `f = uLoop>0.5 ? mod(vFrame,uFrames) : clamp(...)`; `f1 = uLoop>0.5 ? mod(f0+1,uFrames) : min(...)`; `w = uStep>0.5 ? 0 : f-f0`. **Clip lặp hòa chéo khung cuối vào khung đầu: đó là bóng chồng.** Ngưỡng `burn` và `erode` hiện dựa trên độ phủ màu cộng nhiễu, không có trường vẽ tay.
  - Người dùng: `src/view/skills/element-fire.ts`. Test: `tests/view/element-layer.test.ts` (manifest, `frameAt`, `playLife`, pool). `vitest` chạy môi trường `node` (không WebGL). `tsconfig.json` gồm cả `tests/`, nên mọi trường mới của `FlipbookMeta` **phải là tùy chọn** (test cũ dựng `FlipbookMeta` bằng tay).
  - Đã kiểm trong `node_modules/three/build/three.module.js` (r170, dòng ~25020–25025): texture `NoColorSpace` được tải với `UNPACK_COLORSPACE_CONVERSION_WEBGL = NONE`, và `UNPACK_PREMULTIPLY_ALPHA_WEBGL` lấy từ `texture.premultiplyAlpha`.
- `art-src/` không nằm trong Git, nên worktree không có atlas thật: test chỉ dùng manifest dựng sẵn trong test.

## Làm ở đâu
- **Claude tạo trước khi chạy:** `git -C games/immortality-cultivation worktree add ../.wt-immortality-cultivation-codex -b codex/flipbook-v2 bc94110`, rồi symlink `node_modules` như phiếu 255.
- Không ghi gì trong `games/immortality-cultivation/` (agent khác đang làm ở đó).

### Được ghi
- `games/.wt-immortality-cultivation-codex/src/view/skills/flipbook.ts`;
- `games/.wt-immortality-cultivation-codex/tests/view/flipbook-v2.test.ts` (tạo mới);
- `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-flipbook-v2.md`;
- `docs/codex-queue/258-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa file khác những file trên, nhất là `element-fire.ts`, `element-*.ts`, `src/lab/**`, `tests/view/element-layer.test.ts` (phải qua mà không sửa), manifest và ảnh trong `art-src/`.
- Đổi ý nghĩa của bất kỳ export, phương thức, setter hay trường `FlipOptions` đang có.
- Chạy dev server, mở trình duyệt, tải gói hay ảnh, sinh ảnh.

## Việc (lời giải đã chốt)
_Đang chờ hai lượt duyệt; phần dưới là lời giải Claude chốt sơ bộ, sẽ cập nhật theo kết quả duyệt._

### 1. Manifest và `FlipbookMeta` (tương thích ngược)
- Kiểu mới: `export type FlipbookLoopMode = "none" | "stepped" | "holderode";` và `export interface FlipbookTiming { revealTicks; holdEnd; tearEnd; tearE; erodeEnd; width; rampTicks }` (mọi trường `number`, `readonly`).
- `FlipbookMeta` thêm các trường **tùy chọn**: `loopMode?`, `frameRange?: readonly [number, number]` (bao hai đầu), `variants?: number`, `controlA?: string` (URL), `controlB?: string` (URL), `anchor?: readonly [number, number]`, `sourceFps?: number`, `timingProfile?: string`.
- `parseFlipbookManifest` chỉ đặt một trường mới khi manifest có trường đó; thiếu thì không đặt (đối tượng meta của manifest cũ giữ y nguyên các khóa như hôm nay).
  - `loopMode`: chỉ nhận ba giá trị trên, sai thì ném lỗi. Có `loopMode` thì `loop = loopMode !== "none"` (thắng `loop` cũ).
  - Có trường v2 khác mà thiếu `loopMode`: `loop: true` → `stepped`, còn lại → `none` (đường v2 không bao giờ hòa chéo bọc vòng; ý của ChatGPT, Claude nhận).
  - Manifest không có trường v2 nào mà `loop: true`: **đường cũ** (hòa chéo bọc vòng như hôm nay), để atlas cũ y nguyên từng điểm ảnh. Bỏ đường này là việc của phiếu lắp (CX-D, CX-G), khi từng clip có `loopMode` và đã đo R_seam.
  - `frameRange`: hai số nguyên, `0 ≤ a ≤ b < frames`, sai thì ném lỗi.
  - `variants`: số nguyên ≥ 1, chia hết `rows`; mỗi biến thể có `frames / variants` khung (phải nguyên), khung `f` của biến thể `v` ở ô `v · (frames / variants) + f`.
  - `controlA`, `controlB`: tên tệp theo cùng regex `FILE`, URL dựng như `file` (không lấy URL từ JSON).
  - `anchor`: như `pivot` (0–1 hoặc pixel ô). `sourceFps`: số > 0, ≤ 240. `timingProfile`: phải là khóa của `FLIPBOOK_TIMING`, sai thì ném lỗi.
- Hàm mới `export function isFlipbookV2(meta: FlipbookMeta): boolean`: đúng khi có `loopMode`, `controlA`, `controlB`, `timingProfile`, `frameRange` hoặc `variants > 1`.

### 2. Nạp mặt nạ
- `FlipbookLibrary` nạp `controlA` và `controlB` bằng cùng `THREE.TextureLoader` (cùng `flipY` với atlas): `colorSpace = THREE.NoColorSpace`, `premultiplyAlpha = false`, `generateMipmaps = false`, `minFilter = magFilter = THREE.LinearFilter`, `ClampToEdgeWrapping`. Mặt nạ hỏng thì cảnh báo và clip chạy không mặt nạ.
- `Entry` thêm `controlA?: THREE.Texture`, `controlB?: THREE.Texture`. `attach(meta, texture, controls?: { a?: THREE.Texture | null; b?: THREE.Texture | null })`; hai chỗ gọi trong `FlipbookPlayer` truyền thêm `controls`.
- Mặt nạ A cùng lưới `cols × rows` và cùng kích thước atlas; mặt nạ B cùng lưới, nửa độ phân giải. Cả hai lấy mẫu bằng `vxCell` như atlas.

### 3. Shader: giữ đường cũ, thêm đường v2 bằng `defines`
- Meta cũ (`isFlipbookV2` sai): `attach` **không** đổi `material.defines`, **không** đặt `needsUpdate`; chuỗi fragment sau tiền xử lý y hệt hôm nay.
- Meta v2: `attach` đặt một lần `defines.FB_V2 = 1`, `defines.FB_LOOP = 0 | 1 | 2` (none, stepped, holderode), `defines.FB_CTRL_A = 1` nếu có mặt nạ A, `defines.FB_CTRL_B = 1` nếu có mặt nạ B; rồi `material.needsUpdate = true`.
- Uniform mới: `uRange` (vec2: khung đầu đoạn, số khung), `uVarFrames`, `uCtlA`, `uCtlB` (sampler2D), `uInk` (vec4: màu tuyến tính, alpha), `uInkBreak` (0,20–0,35, mặc định 0,25), `uBodyCap` (mặc định 0,88), `uHot` (vec4: màu HDR, độ lợi), `uHotLead` (mặc định 0,1), `uRamp0..uRamp3` (vec3 tuyến tính: trắng vàng, cam, đỏ thẫm, bồ hóng; mặc định từ bảng màu fire `#FFFDF0`, `#FFB703`, `#D93800`, `#240715` đổi sang tuyến tính).
- Thuộc tính instance mới: `iCtl` (vec4: `T`, `e`, `w`, `rampMix`) và `iVar` (float: ô đầu của biến thể). Tổng thuộc tính đỉnh: 10 (≤ 16).
- **Chỉ số khung theo `loopMode`** (mọi chế độ, trong `#ifdef FB_V2`), với `n0 = uRange.x`, `N = uRange.y`:
  - `none`: `f = clamp(vFrame, n0, n0+N-1)`, `f1 = min(f0+1, n0+N-1)`, `w = uStep>0.5 ? 0 : f-f0` (chạy một lần, như đường cũ không lặp).
  - `stepped`: `f = n0 + mod(vFrame-n0, N)`, `f1 = f0`, `w = 0`.
  - `holderode`: `f = n0 + mod(vFrame-n0, N)`, `f1 = n0 + mod(f0-n0+1, N)`; mỗi điểm ảnh đổi từ `f0` sang `f1` ở thời điểm riêng: `ws = smoothstep(-0.04, 0.04, w - mix(0.08, 0.92, order))`, `order` = `S` của mặt nạ A ở khung `f0` nếu có, không thì nhiễu qua logistic như `uSharpen`. Màu thẳng và alpha lấy theo `ws` (không trộn tuyến tính hai khung). Kể cả ở chỗ bọc vòng.
  - Ô thật: `vxCell(f + vVar, uv)`.
- **Ghép ink, thân, lõi** (chế độ `rgba`, `FB_CTRL_A`): `H, G, Hot, S` = R, G, B, A của mặt nạ A; `Rv` = R của mặt nạ B (không có B: `Rv = 0`).
  - `rev = step(Rv, iCtl.x + 0.002)` (hiện nhị phân, không mờ dần lên);
  - `live = smoothstep(e, e + w, S)`, `liveH = smoothstep(e + uHotLead, e + uHotLead + w, S)`;
  - `a_b = min(a_atlas, H) · rev · live`; `a_i = G · uInk.a · gap · rev · live`, `gap = step(uInkBreak, nhiễu)`; `a_h = Hot · rev · liveH`;
  - `C_b = min(c_atlas · vTint, uBodyCap)`, rồi `mix(C_b, ramp(r), rampMix)`, `r = clamp((S - e) / (1 - e), 0, 1)`, `ramp` theo bậc ở 0,25 / 0,5 / 0,75 (biên mềm 0,02);
  - `C_i = uInk.rgb`; `C_h = uHot.rgb · uHot.a`;
  - công thức §2.3: `α = 1 − (1 − a_i)(1 − a_b)(1 − a_h)`, `RGB = C_i·a_i·(1 − a_b)(1 − a_h) + C_b·a_b·(1 − a_h) + C_h·a_h`; xuất `vec4(RGB·soft, α·soft)`.
  - Đường v2 có mặt nạ A bỏ `burn` và `erode` cũ (thay bằng `e`); không có mặt nạ A thì giữ chúng như cũ.
- Chuỗi GLSL ghép là hằng `FB_COMPOSE_GLSL` (export), để test so chữ với bản CPU.

### 4. CPU: tick, lịch hiện và lịch xói (export, test được trong node)
- `flipbookTick(ageS) = max(0, floor(ageS · 60 + 1e-6))`.
- `revealThreshold(tick, revealTicks = 4) = clamp((tick + 1) / revealTicks, 0, 1)`.
- `erodeThreshold(tick, t: FlipbookTiming)`: `tick ≤ holdEnd` → `−width`; tới `tearEnd` → `−width + (tearE + width)·(1 − (1 − x)²)`, `x = (tick − holdEnd)/(tearEnd − holdEnd)`; tới `erodeEnd` → tuyến tính `tearE → 1`; sau đó `1`.
- `rampMixAt(tick, t) = clamp((tick − holdEnd)/rampTicks, 0, 1)`.
- `FLIPBOOK_TIMING["impact-key1"] = { revealTicks: 4, holdEnd: 9, tearEnd: 20, tearE: 0.85, erodeEnd: 42, width: 0.08, rampTicks: 4 }` (TRIAL).
- `FlipOptions` thêm `timing?: string | FlipbookTiming` (thắng `meta.timingProfile`) và `variant?: number`. Có lịch thì `life` mặc định `(erodeEnd + 1)/60`, `fadeOut` mặc định 0, `cool` bị bỏ qua. Không có lịch: `iCtl = (1, −1, 0.08, 0)`.
- Lưu trạng thái: `STRIDE` 35 → 36, ô 35 = ô đầu của biến thể; lịch của từng slot ở mảng song song `timings: (FlipbookTiming | null)[]` cấp một lần theo `capacity` trong constructor (gán ở `spawn`, không cấp phát).
- `update` ghi `iCtl` và `iVar` ở **chỉ số nén `n`** (như `iData`), từ tuổi lúc vẽ (`age`, trước khi cộng `dt`; khung đầu tick 0), không cấp phát; thêm `"iCtl"`, `"iVar"` vào `ATTRS`.
- Bản CPU của phép ghép: `composeInkBodyCore(aI, aB, aH, cI, cB, cH, out)` (premultiplied RGBA vào `out`), và `blendPremultiplied(src, dst, out)`.

### 5. Test mới `tests/view/flipbook-v2.test.ts` (số cụ thể)
1. Manifest cũ (không trường mới): `isFlipbookV2` sai; meta không có khóa mới; pool sau `attach` có `defines` không chứa khóa `FB_`, `material.version` không đổi.
2. `loopMode` hợp lệ, giá trị lạ ném lỗi; `loop: true` không `loopMode` giữ `loopMode` undefined; `frameRange`, `variants`, `timingProfile` sai ném lỗi.
3. Chỉ số khung (bản CPU `flipbookFramePair`): `stepped` ở `vFrame = N − 0,5` cho `f1 = f0`, `w = 0`; `holderode` cho `f1 = n0`, và `ws` ngoài dải ±0,04 chỉ là 0 hoặc 1.
4. Ghép: dạng đóng bằng chuỗi "over" tuần tự (ink, rồi thân, rồi lõi) sai số ≤ 1e-6 trên lưới độ phủ {0; 0,25; 0,5; 0,75; 1}³ và ba bộ màu; trên đá sáng và đá tối, sai số sau lượng tử 8 bit ≤ 1/255.
5. Tick: `flipbookTick(0) = 0`, `(1/60) = 1`, `(0,5) = 30`; cùng tuổi cho cùng tick với `dt` = 1/30, 1/60, 1/144.
6. Hiện: `T(0..3) = 0,25; 0,5; 0,75; 1`, `T(10) = 1`.
7. Xói `impact-key1`: `e(0..9) = −0,08`; đơn điệu không giảm; `e(20) = 0,85 ± 1e-6`; `e(42) = 1`; `(erodeEnd − holdEnd) ≥ 3 · revealTicks`.
8. Thân sáng: 1000 mẫu `S` đều 0–1, độ sáng thân ở tick 18 ≤ 15 % đỉnh; tick 4–9 bằng đỉnh (±1e-6).
9. Pool ghi `iCtl`: tick 0 → `(0,25; −0,08; 0,08; 0)`; tick 12 khớp `erodeThreshold(12)`; spawn không lịch → `(1, −1, 0,08, 0)`.
10. Biến thể: lưới 4×4, 16 khung, `variants: 2` → biến thể 1 có `iVar = 8`; `variants: 3` ném lỗi.

## Kiểm bắt buộc (trong `games/.wt-immortality-cultivation-codex`; ghi lệnh và kết quả vào báo cáo)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua; trước 766 (mốc `bc94110`), sau = 766 + số test mới; `tests/view/element-layer.test.ts` qua mà không sửa.
3. `git -C games/.wt-immortality-cultivation-codex diff --stat` và `status --short`: chỉ các file được ghi.

## Claude kiểm sau (trình duyệt, không phải việc của Codex)
- Atlas cũ y nguyên từng điểm ảnh: chụp các clip của `fire` và `aura` trước và sau, chênh 0.
- GPU so CPU ±1/255: ô mẫu (không phủ, phủ một phần, phủ đủ) trên đá sáng và đá tối.
- Đọc lại texel mặt nạ A có alpha thấp, so với PNG nguồn (±1/255): kiểm rằng trình duyệt không premultiply khi giải mã.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Thay đổi trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–3, làm phần "Claude kiểm sau", rồi mới commit và gộp.
- Báo cáo ghi: từng mục 1–5 đã làm ở hàm nào; chỗ phải làm khác và vì sao; kết quả Kiểm 1–3.

## Lỗi ChatGPT nêu ở lượt duyệt 1 (13:51, phải xử lý trước khi giao)
Claude chưa chốt từng lỗi; nhiều lỗi cũng đúng với lời giải sơ bộ ở trên:
1. Bản CPU phải đi đúng đường của shader: giải mã sRGB, nội suy premultiplied tuyến tính giữa hai khung, rồi lấy lại màu thẳng; thiếu hàm CPU nhận hai khung và trọng số thì không kiểm được ±1/255 cho `none`.
2. Đường v2 phải giữ `setSharpen` (chuyển khung lệch theo nhiễu), không chỉ `uStep`.
3. `anchor`: phải chốt quan hệ với `pivot` và chỗ nối vào `uPivot`, hoặc chỉ đọc và lưu.
4. Lịch thời gian: chốt lúc kích hoạt, giữ ý nghĩa `iAge` và `FlipOptions` cũ, đặt lại cho slot tái dùng.
5. `soft` nhân một lần ở cuối lên RGB premultiplied và alpha (lời giải trên đã làm vậy; giữ).
6. Lề nửa texel riêng cho atlas và mặt nạ A với mặt nạ B (độ phân giải khác nhau).
7. GLSL đầy đủ của đường v2 không mặt nạ cho cả bốn chế độ `rgba`, `fire`, `smoke`, `heat`.
8. (Danh sách bị cắt khi lưu; xem hồ sơ ChatGPT.)
