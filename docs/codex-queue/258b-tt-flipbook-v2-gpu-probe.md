# Phiếu 258b · Tu Tiên · Code: công cụ đo GPU cho `FlipbookPool` bản 2

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Đây là công cụ kiểm, không phải tính năng. Đặc tả lấy từ mục "Claude kiểm sau" của phiếu 258, mục đó đã qua phản biện. Codex không thiết kế lại. Chỗ nào không làm được đúng như viết thì dừng ở đó và ghi vào báo cáo.

**Báo cáo:** `docs/codex-queue/258b-report.md` (tiếng Việt).

**Đường duyệt:** Claude viết lúc 19:05 ngày 04/11, rút thẳng từ mục "Claude kiểm sau" (1, 3, 4) của phiếu 258. Bỏ bước duyệt hai lần vì đây là công cụ đo cho một đặc tả đã duyệt: chạy sai thì nó tự báo trượt khi so với số CPU. Claude chạy công cụ trong trình duyệt và đọc kết quả.

## Bối cảnh
- Phiếu 258 đã xong và đã commit trên nhánh `codex/flipbook-v2` (`bf18505`) trong `games/.wt-immortality-cultivation-codex`. Claude đã chạy lại tsc (0 lỗi), 907/907 test, và grep bản build (sạch).
- Trước khi gộp vào `main`, còn phải kiểm trên GPU theo mục "Claude kiểm sau" của `docs/codex-queue/258-tt-flipbook-v2.md`. Đọc kỹ mục đó: phiếu này hiện thực mục 1, 3 và 4. Mục 2 (atlas cũ giữ nguyên) Claude kiểm bằng `scripts/visual/scenarios/lab-element-parity.mjs` có sẵn.
- Codex không chạy được trình duyệt hay dev server. Codex chỉ viết công cụ cùng test Node cho các phần thuần. Claude chạy bằng `src/kit/tools/cdp-run.mjs`, giống mẫu `scripts/visual/scenarios/lab-element-parity.mjs`.
- Mã liên quan: `src/view/skills/flipbook.ts` (đã có `FlipbookPool`, `parseFlipbookManifest`, `composeFlipbookMasked`, `blendPremultiplied`, `srgbToLinear`, `flipbookControl`, `FLIPBOOK_TIMING`, `FLIPBOOK_MASKED_LOOK`) và `src/lab/skills-main.ts` (`window.__lab`; renderer là `view.stage.renderer`, dòng khoảng 1874).
  - Pool dựng một lần với texture trắng `blank` (xem `FlipbookPlayer`, dòng khoảng 1424, nơi dựng `DataTexture` 1×1).
  - Thuộc tính instance là thuộc tính công khai của `pool.mesh.geometry`: `iPos`, `iData` (size, angle, frame, alpha), `iColor`, `iDir` (w: occlude), `iAge`, `iLift`, và trên đường v2 thêm `iCtl`, `iVar`. Công cụ ghi đè các mảng này qua `geometry.getAttribute(name).array` rồi đặt `needsUpdate`, **không sửa `flipbook.ts`**.

## Làm ở đâu
Cùng worktree `games/.wt-immortality-cultivation-codex`, nhánh `codex/flipbook-v2` (HEAD `bf18505`). Không ghi gì trong `games/immortality-cultivation/`.

### Được ghi
- `src/lab/flipbook-probe.ts` (tạo mới);
- `src/lab/skills-main.ts`, **chỉ ba chỗ**: một dòng import; một phương thức `flipbookProbe(): Promise<FlipbookProbeReport>` có JSDoc trong kiểu của `__lab`; và phần thân phương thức gọi `runFlipbookProbe(view.stage.renderer)`;
- `scripts/visual/scenarios/lab-flipbook-v2-probe.mjs` (tạo mới);
- `tests/view/flipbook-probe.test.ts` (tạo mới);
- `docs/changelog/2026-11-04-flipbook-v2.md` (chỉ thêm một mục "Công cụ đo GPU (258b)" ở cuối);
- `docs/codex-queue/258b-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa `src/view/skills/flipbook.ts` hay bất kỳ file nào khác ngoài danh sách trên.
- Chạy dev server, mở trình duyệt, tải gói, sinh ảnh.

## Việc (lời giải đã chốt)

### 1. `src/lab/flipbook-probe.ts`
Export:
- `interface FlipbookProbeReport { programs; gpuVsCpu; maskDecode; pass: boolean }`. Dạng chi tiết ở mục 5.
- `async function runFlipbookProbe(renderer: THREE.WebGLRenderer): Promise<FlipbookProbeReport>`.
- Các hàm thuần để test Node dùng:
  - `probeCases(): ProbeCase[]` (mục 3);
  - `cpuExpected(c: ProbeCase): { premul: [r,g,b,a]; light: [r,g,b]; dark: [r,g,b] }`;
  - `encodePngRgba(width, height, rgba: Uint8Array, deflate: (raw: Uint8Array) => Promise<Uint8Array>): Promise<Uint8Array>`;
  - `crc32(bytes): number`.

Quy tắc chung của `runFlipbookProbe`:
- Dựng `THREE.Scene` riêng, `OrthographicCamera(-1, 1, 1, -1, 0.1, 10)` đặt ở z = 5 nhìn về gốc, và `WebGLRenderTarget` kiểu `HalfFloatType`, `RGBAFormat`, không MSAA, không depth buffer nếu không cần.
- Đầu hàm lưu rồi cuối hàm trả lại: render target đang dùng, clear color và alpha, `renderer.debug.checkShaderErrors`, `renderer.debug.onShaderError`, `renderer.info.autoReset`, `renderer.autoClear`.
- Bắt lỗi biên dịch bằng `renderer.debug.checkShaderErrors = true` và một `onShaderError` ghi vào danh sách. Sau mỗi lần vẽ, gọi `gl.getError()` đến khi ra `NO_ERROR` và ghi mọi mã khác 0.
- Mọi texture, pool, material và target do công cụ dựng đều được `dispose` ở cuối, kể cả khi có lỗi (`try/finally`). Giữa các mục, công cụ không đợi khung hình nào của lab.

### 2. Mục 1: biên dịch, 18 pool và 9 chương trình
- Atlas tổng hợp: `DataTexture` RGBA8, 2 ô × 1 hàng, mỗi ô 32×32 px một màu phẳng, `SRGBColorSpace`, `premultiplyAlpha = false`, mipmap bật, bộ lọc giống `FlipbookLibrary.load`. Mặt nạ A và B: `DataTexture` RGBA8 cùng kích thước, `NoColorSpace`, `premultiplyAlpha = false`.
- Meta lấy qua **`parseFlipbookManifest`** từ một manifest tổng hợp, để các trường v2 đi qua đúng parser: `cols 2, rows 1, frames 2, fps 24`, `loopMode` lần lượt `none | stepped | holderode`, cộng `controlA` hoặc `controlA` với `controlB` (tên tệp hợp lệ theo regex `FILE` của parser; tệp không cần có thật vì texture được đưa thẳng vào `attach`).
- 18 pool:
  - `rgba`: 3 `loopMode` × {không mặt nạ, A, A+B} = 9;
  - `fire`, `smoke`, `heat`: 3 `loopMode`, không mặt nạ = 9.
- Ghi `p0 = renderer.info.programs.length` trước. Với từng pool: `attach`, `spawn` một sprite ở gốc (size 2, `ground` −1e5), `update(1/60)`, vẽ cảnh chỉ chứa `pool.mesh` vào target. Ghi:
  - số draw call của lần vẽ đó (lấy hiệu `renderer.info.render.calls` trước và sau, với `autoReset = false` trong lúc đo);
  - `renderer.properties.get(pool.mesh.material).currentProgram`.
- Kết quả: `programs = { pools: 18, distinct, added: p1 − p0, callsPerPool: number[], shaderErrors: string[], glErrors: number[] }`. **Đạt** khi `distinct === 9`, `added === 9`, mọi `callsPerPool` bằng 1, và cả hai danh sách lỗi rỗng.

### 3. Mục 3: GPU so CPU, sai số ≤ 1/255
**Bảng ca (`probeCases`)** có hai nhóm, mỗi ca có tên. Mọi số đều là **byte**, để GPU và CPU đọc đúng cùng một giá trị:
- Nhóm "test4": mỗi ca của Test 4 trong `tests/view/flipbook-v2.test.ts` đổi sang byte gần nhất:
  - atlas: kênh RGB qua sRGB, `round(linearToSrgb(v)·255)`; alpha `round(a·255)`;
  - mặt nạ: `round(v·255)`;
  - `w` đổi sang số gần nhất trong {0, 0.25, 0.5, 0.75};
  - `ctl` và `tint` giữ nguyên số thực.

  Phía CPU tính lại từ chính các byte đó, không từ số thực của Test 4. Ca nào của Test 4 không biểu diễn được bằng một sprite (ví dụ cần hai mẫu khác nhau trong cùng một ô) thì bỏ, và ghi tên ca vào báo cáo.
- Nhóm "impact-key1": dùng một mẫu cố định:
  - atlas ô 0 = (255, 150, 60, 230), ô 1 = (240, 90, 30, 200);
  - mặt nạ A ô 0 = (230, 120, 200, 140), ô 1 = (200, 90, 160, 110);
  - mặt nạ B kênh R: ô 0 = 40, ô 1 = 90;
  - `w = 0.25`, tint (1, 1, 1);
  - `loopMode: "none"`, mặt nạ A+B;
  - `ctl` lấy từ `flipbookControl(tick/60, 43/60, 0, 0, FLIPBOOK_TIMING["impact-key1"], out)` với tick ∈ {0, 1, 3, 9, 12, 18, 20, 42}.

**Phía CPU (`cpuExpected`):**
- mẫu atlas = `[srgbToLinear(r/255), srgbToLinear(g/255), srgbToLinear(b/255), a/255]`; mẫu mặt nạ = `byte/255`;
- `premul = composeFlipbookMasked({... , soft: 1}, FLIPBOOK_MASKED_LOOK, out)`;
- `light` và `dark` = `blendPremultiplied(premul, dst)`. Ở đây `dst` là màu đá sáng `#d6d0c2` và đá tối `#2a2c30` đổi sang tuyến tính bằng `srgbToLinear` (nhưng xem lượt 2 bên dưới: lúc chạy, `dst` lấy theo giá trị đọc lại).

**Phía GPU:** với mỗi ca:
1. Dựng atlas và mặt nạ của ca, như ở mục 2.
2. Một pool `rgba`, `attach(meta, atlas, controls)`.
3. `spawn` một sprite: size 2 ở gốc (lấp kín khung trực giao), `life` 10, `fadeIn` 0, `fadeOut` 0, `ground` −1e5, `tint` của ca, `intensity` 1.
4. `update(0)`, rồi ghi đè instance 0:
   - `iData.z` = `w` (khung 0 + phần lẻ w), `iData.w` = 1;
   - `iCtl` = `ctl` của ca;
   - `iColor.rgb` = tint;
   - đặt `needsUpdate` cho các thuộc tính đó.
5. **Trung hòa mọi hệ số khác.** Đọc `VERTEX`, `FRAGMENT` và `FB_MASKED_GLSL` rồi xác định mọi hệ số nhân vào kết quả ngoài các đầu vào của `fbComposeMasked`: `soft` gồm `vxSoftGround`, `border`, `uVignette`, `vAlpha`; ngoài ra `iLift` và độ nâng sâu. Đặt các giá trị để ở **điểm ảnh giữa** (32, 32) mỗi hệ số đúng bằng 1, và ghi trong báo cáo từng hệ số được trung hòa bằng cách nào.
   - Nếu một hệ số không thể bằng 1 mà không sửa `flipbook.ts`, thì đo nó (so với lượt 1 của một ca đã biết), ghi vào báo cáo, và đánh dấu mục 3 là "không kết luận". Không được tự sửa shader.
6. **Lượt 1:** tạm đặt `material.blending = THREE.NoBlending`, xóa target về (0, 0, 0, 0), vẽ, đọc RGBA tại (32, 32) bằng `readRenderTargetPixels` vào `Uint16Array`, đổi bằng `THREE.DataUtils.fromHalfFloat`. So với `premul`.
7. **Lượt 2:** trả `blending` về như cũ.
   - Xóa target bằng màu đá sáng (`THREE.Color.setRGB(..., THREE.LinearSRGBColorSpace)` từ giá trị tuyến tính).
   - **Đọc lại giá trị đã xóa** tại (32, 32) trước khi vẽ, và dùng đúng giá trị đọc được làm `dst` cho phía CPU (không dùng số lý thuyết).
   - Vẽ, đọc RGB, so với `blendPremultiplied(premul, dstĐọcĐược)`.
   - Làm lại với màu đá tối.

Kết quả:
```
gpuVsCpu = {
  cases: [{ name, premul: {gpu, cpu, err}, light: {...}, dark: {...} }],
  maxErr,
  skipped: string[],
  neutralised: string[],
  inconclusive: boolean,
}
```
**Đạt** khi `maxErr ≤ 1/255` trên mọi kênh của mọi ca và `inconclusive === false`.

### 4. Mục 4: mặt nạ không bị premultiply khi giải mã PNG
- Dựng ba ảnh PNG 4×4 RGBA, mỗi ảnh một màu (200, 100, 50) với A lần lượt 1, 3 và 8.
  - Mã hóa bằng `encodePngRgba`: chữ ký PNG, IHDR (8 bit, kiểu màu 6, không interlace), một IDAT (mỗi hàng có byte lọc 0, nén zlib), IEND, CRC32 đúng chuẩn.
  - Trong trình duyệt, `deflate` dùng `new CompressionStream("deflate")` (định dạng zlib).
  - **Không dùng canvas 2D**: canvas lưu màu premultiplied, làm hỏng RGB khi A nhỏ.
- `Blob` sang `URL.createObjectURL`, rồi `new THREE.TextureLoader().loadAsync(url)`. Đặt **đúng các thiết lập mặt nạ** của `FlipbookLibrary.load` sau phiếu 258: `NoColorSpace`, `premultiplyAlpha = false`, mipmap, `LinearMipmapLinearFilter`/`LinearFilter`, `ClampToEdge`, `flipY` mặc định của loader.
- Vẽ texel ra target float 4×4 bằng một `ShaderMaterial` nhỏ (quad lấp kín, mẫu 1:1 nên ở LOD 0, xuất thẳng `texture2D(...)`, `NoBlending`). Đọc 4×4 điểm ảnh rồi lấy điểm (1, 1).
- So RGBA với `(200, 100, 50, A)/255`. Kết quả: `maskDecode = { alphas: [1, 3, 8], read: [[r,g,b,a]…], maxErr }`. **Đạt** khi `maxErr ≤ 1/255`.
- Thu hồi URL bằng `URL.revokeObjectURL`.

### 5. `__lab.flipbookProbe` và kịch bản
- Trong `skills-main.ts`, thêm vào kiểu `__lab`:

  ```ts
  /** Ticket 258b: GPU checks of FlipbookPool v2 (programs, GPU vs CPU, mask decode); off-screen, no time passes. */
  flipbookProbe(): Promise<FlipbookProbeReport>;
  ```

  Thân phương thức: `flipbookProbe: () => runFlipbookProbe(view.stage.renderer)`. Phương thức không đổi gì của lab ngoài phần công cụ tự dựng rồi tự dọn.
- Tạo `scripts/visual/scenarios/lab-flipbook-v2-probe.mjs`, theo mẫu `lab-element-parity.mjs`:
  1. `BASE` mặc định `http://127.0.0.1:3061/skills-lab.html`; mở `${BASE}?fixed=1&ui=0&dpr=1&probe=0`.
  2. Chờ `window.__lab.ready`.
  3. `const r = await page.eval("window.__lab.flipbookProbe()")`. Nếu `cdp-run`'s `page.eval` không chờ Promise, dùng cùng cách các kịch bản khác chờ kết quả bất đồng bộ (đọc `src/kit/tools/cdp-run.mjs` và ghi cách đã dùng).
  4. Ghi JSON đẹp vào `${OUT_DIR ?? "tmp/shots/flipbook-v2"}/probe-${PHASE ?? "after"}.json`.
  5. Trả `{ pass, programs: {distinct, added}, maxErr, maskMaxErr }`.

  Đầu tệp ghi chú cách chạy, giống `lab-element-parity.mjs`.

### 6. Test Node `tests/view/flipbook-probe.test.ts`
- `encodePngRgba` với `deflate` từ `node:zlib` `deflateSync` trên ảnh 4×4, A = 1, 3, 8:
  - tách các chunk;
  - kiểm CRC của từng chunk bằng `crc32`, và `crc32` của chuỗi "IEND" = `0xAE426082`;
  - `inflateSync` IDAT rồi so từng byte với đầu vào (mỗi hàng có byte lọc 0 phía trước).
- `probeCases()`:
  - nhóm impact có đúng 8 ca, tick đúng thứ tự;
  - mọi byte nằm trong 0–255;
  - mọi `w` thuộc {0, 0.25, 0.5, 0.75};
  - số ca test4 bằng số ca Test 4 trừ số ca bỏ (in ra).
- `cpuExpected` cho ba ca impact tick 0, 12, 42: ghi số mong đợi (4 chữ số thập phân) vào báo cáo; test kiểm chúng là số hữu hạn trong [0, 1], và với tick 42 thì `premul` của thân bằng 0 ± 1e-6 (e = 1).
- Không test gì cần WebGL.

## Kiểm bắt buộc (chạy trong worktree)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua; ghi số test và số tệp trước và sau (mốc trước: 907 test, 85 tệp).
3. Xóa `/private/tmp/codex-258b-dist` nếu có, rồi `IC_VITE_CACHE_DIR=/private/tmp/codex-258b-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-258b-dist --configLoader runner`: thoát 0. `grep -rl "flipbookProbe\|fbComposeMasked\|encodePngRgba" /private/tmp/codex-258b-dist` không in gì (lab không vào bản dựng). Xóa thư mục build sau khi kiểm.
4. `node --check scripts/visual/scenarios/lab-flipbook-v2-probe.mjs`: thoát 0.
5. `git -C games/.wt-immortality-cultivation-codex diff --stat` và `status --short`: chỉ các file được ghi.

## Claude làm sau (trình duyệt)
- Dev server của worktree.
- `BASE=http://127.0.0.1:<port>/skills-lab.html OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/flipbook-v2 node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-flipbook-v2-probe.mjs`.
- Đọc JSON. Chạy mục 2 bằng `lab-element-parity.mjs` (`ELEMENT=fire` và kịch bản aura) trên `main` và trên nhánh, so từng điểm ảnh.
- Nếu đạt: gộp `codex/flipbook-v2` vào `main`.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
Thay đổi trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–5, chạy công cụ trong trình duyệt, rồi mới commit.
