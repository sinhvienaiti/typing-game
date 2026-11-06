# Phiếu 326 · Tu Tiên · Lab: flipbook lai (KTX2, vector chuyển động, sao băng lệch pha) và cảnh A/B cho anh xem

**Vì sao:** anh đồng ý thử cách lai ngày 06/11 và cần xem demo A/B trước khi chốt ("tôi cần xem demo trước khi chốt chắc chắn 1 trong 2 cách") (`.agents/skills/game-vfx-production/references/runtime-packaging.md`; số đo ở `docs/games/tu-tien/skills/SKILL_TECH_OVERVIEW_2026-11-06.md`, mục 3 và 6). 19:27 anh nhắn: "kêu codex tạo tôi xem thử demo giữa 2 bản". Phiếu này cho lab:
- nạp atlas KTX2;
- trộn khung bằng vector chuyển động;
- mỗi sao băng một pha flipbook riêng;
- **cảnh A/B chia đôi màn hình**: trái là cách hiện tại, phải là cách lai, cùng seed và cùng đồng hồ;
- kịch bản quay và đo.

Cảnh A/B thay cho "ba thẻ cạnh nhau"; muốn so mức nén video thì dùng `&left=crf23|720p`.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/326-report.md` (tiếng Việt, ngắn).

## Nơi làm
- **Worktree:** `W = games/.wt-ic-lab-hybrid`, nhánh `codex/lab-hybrid-flipbook`, tách từ `codex/lab-skill-bar` (`1b9461e` = `b8ebd51` + thanh chiêu của phiếu 322). **Số dòng trong phiếu này tính theo `b8ebd51`;** trên nhánh này `skills-main.ts` đã có thêm khoảng 63 dòng của phiếu 322 (thanh chiêu, `let bar`, `refreshClipSlots`, phím I), nên tìm chỗ sửa theo nội dung được trích, không theo số dòng. Claude tạo sẵn, kèm liên kết `W/art-src` và `W/node_modules` sang `games/immortality-cultivation/` như các worktree lab khác. Chưa có W thì dừng và ghi báo cáo.
- **Được ghi:**
  - `W/src/view/skills/flipbook.ts`, `W/src/lab/{comet-head,meteor-rain,skills-main}.ts`;
  - file mới `W/src/lab/hybrid-ab.ts`, `W/tests/lab/hybrid-flipbook.test.ts`, `W/scripts/visual/scenarios/lab-hybrid-ab.mjs`;
  - `W/tests/view/flipbook-v2.test.ts`: **chỉ** đổi `FRAGMENT_SHA` và số `7272` sang giá trị của FRAGMENT mới (in từ `unwrapTagMask(new FlipbookPool("c", "rgba", 1, 12, new THREE.Texture()).mesh.material.fragmentShader)`); `VERTEX_SHA` và `1823` giữ nguyên; báo cáo ghi giá trị cũ và mới;
  - thư mục `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/hybrid-ab/`, `typing-game-review/INDEX.md` (do `review-index.mjs` ghi) và báo cáo.
- **Cấm:** lệnh git ghi; sửa file khác (kể cả `vite.config.ts`, `package.json`); ghi vào `art-src`; cài gói; tự làm media thay phiếu 325; mở trình duyệt ngoài kịch bản ở mục 7.

## Đầu vào từ phiếu 325
- `art-src/lab/vfx/hybrid/manifest.json`, mục `azure-cloud-dragon`:
  - file `.atlas.png`, `.uastc.ktx2`, `.etc1s.ktx2`, `.mv.png`, `.mv.uastc.ktx2`, `.mv.etc1s.ktx2`, `.crf23.mp4`, `.720p.mp4`;
  - `compareWith` trỏ về `expansion/azure-cloud-dragon` (video hiện tại: `expansion/azure-cloud-dragon.mp4`).
- Mục `fire-comet`: atlas, KTX2, vector, không có video; `compareWith` trỏ về `fire/fire-comet` (video dùng chung: `fire/fire-comet.mp4`).
- Các trường `ktx2`, `motion`, `videoVariants`, `compareWith`, `sourceRect`: như phiếu 325 mục 4.
- **Thiếu file:** vẫn làm hết mã và test (manifest viết sẵn trong test; test đọc manifest thật dùng `it.skipIf`); bỏ bước trình duyệt và ghi "chờ 325".

## Lời giải đã chốt
1. **`flipbook.ts`, manifest.**
   - **Kiểu xuất:** `Ktx2File {url, bytes}`, `Ktx2Set {uastc?, etc1s?}`, `FlipbookMotion {url, bytes, strength, ktx2?}`.
   - **`FlipbookMeta`** thêm các trường tuỳ chọn `ktx2`, `motion`, `videoVariants: Record<string, FlipbookVideo>`, `compareWith {folder, id}`, `sourceRect {crop: [x,y,w,h], frame: [w,h]}`. **`FlipbookVideo`** thêm `bytes?` (`videoOf` đọc `video.bytes` khi là số ≥ 0).
   - **Luật đọc:**
     - `ktx2`: chỉ khi `yFlip === true`; file khớp `/^[a-z0-9][a-z0-9._-]*\.ktx2$/i`; URL = `base + file`, thêm `"?v=" + md5` khi md5 đủ 32 ký tự hex.
     - `motion`: cần `frames ≥ 2`, `file` khớp `FILE`, `layout === "x-rgb-y-a"`, `zero === 128`, `scale === 127`, `0 < strength ≤ 1`.
     - `videoVariants`: từng mục đọc qua `videoOf`. `compareWith`: hai giá trị khớp `ID`. `sourceRect`: số hữu hạn, cạnh lớn hơn 0.
   - **`bytes`** (số nguyên ≥ 0) chỉ ghi vào meta khi mục có `ktx2` hoặc `motion` hợp lệ. Mục cũ có `bytes` (như `GLINT` trong `tests/view/flipbook-v2.test.ts`) vẫn giữ đúng 12 khoá cũ `OLD_KEYS`.
   - **Trường mới hỏng thì bỏ trường đó, không ném lỗi.** Manifest cũ và bộ đọc cũ giữ nguyên.
2. **`flipbook.ts`, nạp KTX2.** Không import `KTX2Loader` vào file này (test chạy trên node).
   - **Xuất:**
     - `setFlipbookKtx2(c: {loader: {loadAsync(url): Promise<THREE.Texture>}, variant: "uastc" | "etc1s"} | null)`;
     - `FLIPBOOK_MOTION = {blend: true}`;
     - `ktx2Pick(set, variant)` = `set?.[variant] ?? null` (không đổi sang variant kia).
   - **`loadClip(meta: FlipbookMeta, anisotropy: number, bitmap: boolean, png: THREE.TextureLoader | null)` (mới)** trả `{texture, mv?, source: "png" | "ktx2"}`. Loader KTX2 **luôn** lấy từ cấu hình `setFlipbookKtx2` (biến cấp module), không qua tham số. `png` chỉ dùng cho đường PNG khi `bitmap` là false (`loadAtlas(png ?? new THREE.TextureLoader(), …)`).
     - **Màu:** nếu đã có cấu hình KTX2 và `ktx2Pick` ra file thì `loadAsync`, đặt `anisotropy`, wrap clamp, giữ colorSpace và filter của loader. Lỗi thì `console.warn` rồi dùng PNG như cũ (`bitmap ? fetchBitmapAtlas : loadAtlas`).
     - **Vector:** dùng KTX2 cùng variant (`NoColorSpace`). Không có KTX2 thì đọc PNG qua `fetchDataBitmap` (mới):
       - `ImageBitmapLoader` với `{imageOrientation: "flipY", premultiplyAlpha: "none", colorSpaceConversion: "none"}`;
       - `flipY = false`, `NoColorSpace`, mipmap `LinearMipmapLinearFilter`, wrap clamp, `premultiplyAlpha = false`;
       - **không dùng `TextureLoader` cho vector:** `<img>` nhân sẵn alpha, mà trục y nằm trong alpha;
       - thiếu `createImageBitmap` hoặc nạp lỗi thì bỏ vector (vẫn trộn chồng như cũ) và cảnh báo.
   - **`FlipbookLibrary`:**
     - `load()` dùng `loadClip(meta, anisotropy, false, loader)`, với `loader` là `TextureLoader` sẵn có của `load()` (chỉ cho đường PNG); `controls = {a, b, mv}`, truyền khi có ít nhất một trong ba (hiện nay chỉ truyền khi có a hoặc b);
     - `fetchAtlas()` gọi `loadClip(meta, this.anisotropy, true, null)` rồi `this.add(meta, r.texture, r.mv ? { mv: r.mv } : null, r.source)` (mục hoãn như rồng vẫn có KTX2 và vector);
     - `FlipbookControls` thêm `mv?`; `release()` và `reset()` giải phóng cả `mv`;
     - `add()` nhận thêm `source` (tuỳ chọn, mặc định `"png"`); thêm `source(id)` để thăm dò.
3. **`flipbook.ts`, shader và pool.**
   - Sau `uniform vec2 uSharpen;` (dòng 601) thêm `uniform sampler2D uMv; uniform float uMvOn; uniform float uMvStrength; uniform float uClipSide; uniform float uSplitX;`.
   - Sau `  if (vAlpha <= 0.0) discard;` (dòng 619) thêm `  if (uClipSide != 0.0 && (gl_FragCoord.x - uSplitX) * uClipSide < 0.0) discard;`.
   - Thay dòng 627–628 (`vec4 t0 = …`, `vec4 t1 = …`) bằng:
     ```glsl
       vec2 uv0 = uv;
       vec2 uv1 = uv;
       if (uMvOn > 0.5 && w > 0.0) {
         // Motion vectors (tools/vfx-flipbook upgrade): frame f0's flow to f0 + 1 in cell UV (x right, y up); R = x, A = y; 128 = 0, ±127 = ±uMvStrength.
         vec4 m = texture2D(uMv, vxCell(f0, uv));
         vec2 d = (vec2(m.r, m.a) * 255.0 - 128.0) / 127.0 * uMvStrength;
         uv0 = clamp(uv - d * w, 0.004, 0.996);
         uv1 = clamp(uv + d * (1.0 - w), 0.004, 0.996);
       }
       vec4 t0 = texture2D(uMap, vxCell(f0, uv0), uBlur);
       vec4 t1 = texture2D(uMap, vxCell(f1, uv1), uBlur);
     ```
   - **Giữ nguyên các mốc mà mã khác dò theo chuỗi:**
     - `uniform vec4 uGrade;\n`, `varying vec4 vAge;\n`, `void main() {\n`, khối `PICK_V1`, `  if (uMode < 0.5) {\n` (shader v2 lấy thay đổi qua `replaceOnce`);
     - `  vec2 uv = clamp(vUv, 0.004, 0.996);` (`element-clips.ts`);
     - `  border *= …` (`comet-head.ts`, `meteor-rain.ts`).
   - **Uniform của pool:** `uMv` (mặc định `blank`), `uMvOn` 0, `uMvStrength` 0, `uClipSide` 0. `uSplitX` là một object dùng chung cho mọi pool, `SPLIT_X = {value: 0}`; xuất `setFlipbookSplitX(px)`.
   - **`attach()`**, trước `if (!isFlipbookV2(meta))`: đặt `uMv`; `uMvStrength = meta.motion?.strength ?? 0`; `hasMotion = controls?.mv !== undefined && meta.motion !== undefined`; gọi `syncMotion()`, hàm này đặt `uMvOn = hasMotion && FLIPBOOK_MOTION.blend && this.motionBlend ? 1 : 0`.
   - **Setter mới:** `motionBlend` (mặc định true), `clipSide: -1 | 0 | 1`.
   - **Hàm thuần cho test:** `MV_ZERO = 128`, `MV_SCALE = 127`, `motionDecode(byte, strength)`, `motionSampleUv(u, v, du, dv, w, out)` (kẹp 0,004–0,996 như GLSL).
4. **Sao băng (`comet-head.ts`, `meteor-rain.ts`).** Thêm `export type CometMode = "video" | "flipbook" | "ab"`; thay `videoOn` bằng `mode: CometMode = "video"` (mặc định như hôm nay).
   - **Ba chế độ:**
     - `"video"`: cách hôm nay. Mọi quả dùng một video chung; video chưa hiện thì dùng atlas của hệ.
     - `"flipbook"`: không nạp video. Dùng atlas bản lai khi thư viện upgrade có cùng id, role `comet` và trục `comet`; không có thì dùng atlas của hệ.
     - `"ab"`: vẽ cả hai. Thẻ video (`videoPool`, `headVideo`) có `clipSide = -1`; thẻ atlas lai (`rim.pool`, `headAtlas`) có `clipSide = 1`; lớp `body` (Ám) không cắt; không nhả video sau `IDLE_S`.
   - **`use(folder, lib, upgrade = null)`:**
     - video luôn lấy từ `meta.video` của mục trong thư mục hệ;
     - `attach` truyền thêm `e.controls`;
     - luật `drop()` rồi lấy lại chỉ áp dụng khi `mode !== "video"`: rim đang lấy từ hệ mà upgrade nạp sau có cùng id thì `drop()` rồi lấy lại. Ở `"video"`, rim luôn của hệ;
     - video (trong `load()` và chỗ nạp lại `src` trong `update()`, hiện đọc `this.rim.meta.video`) lấy từ `video` của mục hệ, giữ trong một trường riêng, để rim lai không làm mất video;
     - thêm getter `upgraded` (rim đang lấy từ thư viện lai);
     - chỉ gọi `load()` khi mode khác `"flipbook"`.
   - **Pha:**
     - `export function cometPhase(n)` = `(n·0.6180339887498949) % 1`;
     - `export function cometFrame(clock, phase, fps, frames)` = `(clock·fps + phase·frames) % frames`;
     - tham số `phase` của `draw` đổi nghĩa thành phần của vòng lặp (0–1), sửa chú thích; rim và body đều tính khung bằng `cometFrame`.
   - **Getter mới:** `videoEl`, `videoReady` (= `showing`).
   - **`meteor-rain.ts`:**
     - `MeteorHost` thêm `readonly upgrade?: FlipbookLibrary`;
     - `hasComet()` gọi `use(folder, library(folder), this.host.upgrade ?? null)`;
     - dòng 363: `phase: n * 0.37` → `phase: cometPhase(n)`; sửa chú thích ở dòng 247.
5. **`src/lab/hybrid-ab.ts` (mới).** Lớp `HybridAB(host, opts)` với `load()`, `start()`, `update(dt)`, `settle(): Promise<boolean>`, `state()`.
   - **Host:** `camera`, `layer`, `renderer`, `player` (`stage.flipbooks`), `hybrid` (thư viện lai), `labelHost`, `castMeteor()`, `prepareComet(): boolean` (= `meteor.hasComet()`), `comet()`.
   - **Opts:** `scene` (`"meteor"` hoặc một id của `hybrid`), `only` (`"left" | "right" | null`), `left` (`"video" | "crf23" | "720p"`), `prewarm`, `autostart`, `driven`.
   - **Đồng hồ:** `AB_CYCLE_S = 8`; **một** đồng hồ cho hai nửa; `start()` đưa chu kỳ về 0. `start()` của cảnh clip gọi `clear()` cả hai pool, dừng video và tua về 0, rồi mới sinh thẻ (pool chỉ có một ô; thẻ cũ còn sống thì `spawn()` bỏ thẻ mới).
   - **Chia đôi:** mỗi `update` gọi `setFlipbookSplitX(renderer.getDrawingBufferSize(v).x / 2)`; một vạch DOM 2 px ở `left: 50%`. Quái, đất, vệt, nổ vẽ chung; chỉ các thẻ cắt theo `gl_FragCoord` là khác nhau.
   - **Nhãn:**
     - hai góc trên, cách cạnh 24 px, cách đỉnh 16 px, `z-index: 8`, nền `rgba(8,10,16,.72)`, chữ `#f2f4f8`;
     - dòng 1 đậm 20 px: **"Hiện tại: video"** / **"Cách lai: flipbook"**; với `left=crf23|720p` nhãn trái là "Video CRF 23" / "Video 720p";
     - dòng 2, 13 px: thông số (cỡ, fps, MB tải, có vector không, KTX2 UASTC hay ETC1S);
     - có `only` thì một nhãn, không vạch, `clipSide = 0`.
   - **Cảnh `meteor` (hệ Hỏa):**
     - `load()` chờ `player.ready("hybrid")` và `player.ready("fire")`; sau đó mỗi `update` gọi `prepareComet()` tới khi có `comet().upgraded`. Với `only=left`, mỗi `update` vẫn gọi `prepareComet()` cho tới khi `comet().id` bắt đầu bằng `fire-comet` (chỉ để nạp video, không chờ `upgraded`). Video chỉ nạp qua `prepareComet()`;
     - sẵn sàng khi `comet().id` bắt đầu bằng `fire-comet` (hệ được đặt bất đồng bộ lúc khởi động), `comet().videoReady` (trừ `only=right`), `comet().upgraded` (trừ `only=left`) và có mục `fire-comet` lai; `ready` đã true thì giữ true;
     - nếu `prewarm`: `renderer.initTexture` texture màu và texture vector lai;
     - mỗi chu kỳ gọi `castMeteor()`. Hai nửa vẽ cùng một trận mưa, nên cùng seed và cùng đồng hồ.
   - **Cảnh clip (`azure-cloud-dragon`):**
     - `load()` chờ `player.ready("hybrid")` và `player.ready(compareWith.folder)` rồi mới đọc mục. Sẵn sàng khi pool phải đã có atlas thật (`!hybrid.deferred(id)`, trừ `only=left`) và video trái có `readyState ≥ 2` (trừ `only=right`); `ready` đã true thì giữ true;
     - nếu `prewarm`: `renderer.initTexture` texture màu và texture vector lai ngay ở lần `attach` đó, và cộng thời gian vào `uploadMs`;
     - chỉ `attach` texture lai vào pool phải và chỉ thêm mesh của hai pool vào `layer` ở `update` đầu tiên sau khi atlas về (vòng rAF chỉ chạy sau bước prewarm của lab), như sao chổi, để đo được giật lần đầu khi `prewarm=0`;
     - mục đang hoãn thì `hybrid.fetchAtlas(id)`;
     - **trái:** `video` của mục `compareWith` (lấy qua `player.library(folder).declares()`), hoặc `videoVariants[left]` của mục lai. Phát trên `<video>` riêng (muted, playsInline, preload auto, crossOrigin anonymous) với `VideoTexture` SRGB, đặt lên một `FlipbookPool` một ô (mode fire, capacity 1, order 15, vignette 0.35) như `VideoBank.make`;
     - **phải:** flipbook trên pool riêng `new FlipbookPool(id + "#ab", "fire", 1, 15, blank)`, `vignette = 0.35` như pool trái, `attach(meta, texture, controls)`;
     - **vị trí chung:** đất dưới tâm màn hình (cách tính của `Showcase.centre`); cỡ `2·d·tan(fov/2)·0.9`, `lift d·0.6`, `occlude 0.12`, `alpha 1`, `fadeOut 0.3`, `life = AB_CYCLE_S − 0.5`;
     - **thẻ video:** pivot `video.pivot`, `rate 0`. **Thẻ flipbook:** pivot `(video.pivot·frame − crop.xy) / crop.wh` (với đầu ra 325 thì bằng `meta.pivot`), cỡ nhân `abCardScale(meta.sourceRect)` (= `crop[3]/frame[1]`, mặc định 1) để hai nửa khớp ở vạch, `rate 1` từ khung 0;
     - **chạy thật:** chờ `seeked` rồi `play()`, sinh flipbook cùng khung. **`driven`** (`?fixed=1`): video dừng, tua theo đồng hồ khi lệch quá 0,5/24 s (như `VideoBank.update`).
   - **`settle()`:** true khi mọi video của A/B `!seeking`, `readyState ≥ 2` và đã nhận một `requestVideoFrameCallback` (nếu có); quá 500 ms trả false.
   - **`state()`:** `{scene, ready, error, only, left, right, cycle, cycleS, clock, splitX, uploadMs, glError}`; `uploadMs` là tổng ms của các lệnh `initTexture` lúc prewarm, 0 khi không prewarm.
     - Mỗi bên: `{label, kind, source: "mp4" | "png" | "ktx2-uastc" | "ktx2-etc1s", downloadBytes, gpuBytes, format, motion, ready}`.
     - `glError`: `renderer.getContext().getError()` đọc sau prewarm.
     - Mục lai chưa có: `error` = "hybrid/manifest.json chưa có <id> (phiếu 325)", hiện ở nhãn phải.
   - **Hàm thuần xuất:**
     - `abCardScale`;
     - `textureGpuBytes`: `CompressedTexture` = tổng `mipmaps[i].data.byteLength`; `VideoTexture` = `videoWidth·videoHeight·4`; còn lại `w·h·4`, nhân 4/3 khi có mipmap;
     - `textureFormatName`: tên của `RGBA_ASTC_4x4_Format`, `RGBA_BPTC_Format`, `RGB_ETC1_Format`, `RGB_ETC2_Format`, `RGBA_ETC2_EAC_Format`, `RGB_S3TC_DXT1_Format`, `RGBA_S3TC_DXT5_Format`, `RGBAFormat`; còn lại trả số.
6. **`skills-main.ts`.**
   - **Import:** `KTX2Loader` (`three/examples/jsm/loaders/KTX2Loader.js`); `basisWasmUrl` (`three/examples/jsm/libs/basis/basis_transcoder.wasm?url`); `basisJsUrl` (`three/examples/jsm/libs/basis/basis_transcoder.js?url`), để file `.js` cũng vào `safeModulePaths` của Vite (không thì Vite trả 403 vì `node_modules` là liên kết ra ngoài W). Thư mục transcoder vẫn lấy từ `basisWasmUrl`; nếu thư mục của `basisJsUrl` khác thì `console.warn`.
   - **Sau `const stage = …` (dòng 942):**
     - `AB_SCENE = params.get("ab")`; `AB_ONLY` lấy từ `?only=left|right`, khác thì `null`;
     - khi `?ktx2` khác `"0"`: `setFlipbookKtx2({loader: new KTX2Loader().setTranscoderPath(<thư mục của basisWasmUrl, có "/" cuối>).detectSupport(view.stage.renderer), variant: ?ktx2 === "etc1s" ? "etc1s" : "uastc"})`;
     - `FLIPBOOK_MOTION.blend = params.get("mv") !== "0"`;
     - `const hybridLib = AB_SCENE !== null || params.get("cometFlip") === "1" || params.get("video") === "0" ? stage.flipbooks.library("hybrid", (m) => m.role !== "comet") : undefined;`. Phải là lần gọi `library("hybrid")` đầu tiên, vì lần gọi đầu đặt `defer`. **Lab không tham số không tải thư mục `hybrid/`** và không khởi động transcoder: chỉ gọi `setFlipbookKtx2(...)` khi `hybridLib !== undefined`.
   - **Host `MeteorRain` (dòng 1193):** thêm `upgrade: hybridLib`.
   - **Thay dòng `meteor.comet.videoOn = params.get("video") !== "0";`** (khoảng dòng 1305 theo `b8ebd51`; giữ nguyên dòng `meteor.comet.driven = fixed;` ngay trên) bằng: `meteor.comet.mode = AB_SCENE === "meteor" ? (AB_ONLY === "left" ? "video" : AB_ONLY === "right" ? "flipbook" : "ab") : params.get("cometFlip") === "1" || params.get("video") === "0" ? "flipbook" : "video";`
     **Mặc định vẫn là video như hiện nay:** anh chưa chọn cách nào (06/11 19:28: "tôi cần xem demo trước khi chốt chắc chắn 1 trong 2 cách"). Flipbook từng quả chỉ bật bằng `?cometFlip=1` hoặc trong cảnh A/B. Không có tham số `cometVideo`.
   - **Ngay sau đó:** `ab = AB_SCENE === null ? null : new HybridAB(…)`, với `left` từ `?left=` (mặc định `"video"`), `prewarm: ?prewarm !== "0"`, `autostart: ?autostart !== "0"`, `driven: fixed`; rồi `void ab?.load()`.
   - **Dòng 1708:** điều kiện thành `params.get("ui") !== "0" && AB_SCENE === null` (panel không che nửa trái).
   - **Dòng 1932:** sau `meteor.update(world);` thêm `ab?.update(dt);`.
   - **`__lab`:**
     - kiểu (khoảng dòng 2040) và literal (khoảng dòng 2328) thêm `ab(): AbState | null`, `abStart(): void`, `abSettle(): Promise<boolean>`;
     - `abSettle` là `async`: `const ok = (await ab?.settle()) ?? false; view.render(0); return ok;`;
     - `memory()` (khoảng dòng 2814) tính `CompressedTexture` bằng `textureGpuBytes`.
7. **Kịch bản `scripts/visual/scenarios/lab-hybrid-ab.mjs`** (theo mẫu `lab-power-clip.mjs`, `lab-perf-memory.mjs`).
   - **Biến môi trường:** `BASE` (mặc định `http://127.0.0.1:3126/skills-lab.html`), `OUT_DIR` (mặc định thư mục `hybrid-ab` ở trên), `PART=capture|perf|hitch|all`, `SCENES=meteor,azure-cloud-dragon`.
   - **Mỗi lần mở:** URL `?ab=<cảnh>&ui=0&bar=0&dpr=1&element=fire`; chờ `__lab.ready && __lab.ab()?.ready` (tối đa 100 s); gọi `__lab.camera('play')`. Khi URL có `fixed=1`: sau khi `__lab.ready`, mỗi vòng chờ (100 ms) gọi `__lab.step(1, 1/30)`, vì lab không tự chạy khung.
   - **`capture`:**
     - URL thêm `&fixed=1&autostart=0`;
     - làm nóng: `abStart()`, `step(60, 1/30)`, `__lab.reset()`, rồi `abStart()` (để MP4 không có hai trận mưa chồng nhau);
     - 240 khung, mỗi khung: `step(1, 1/30)`, `await abSettle()`, `page.shot` JPEG;
     - ffmpeg `-framerate 30`, `libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart` → `<OUT_DIR>/<cảnh>-ab.mp4` (8 s, 1920×1080);
     - tấm ghép `<cảnh>-ab-sheet.jpg` bằng `select='not(mod(n,40))',scale=640:-2,tile=3x2`, có `-frames:v 1`;
     - có MP4 rồi thì xoá thư mục JPEG của mình.
   - **`perf`:**
     - chạy thời gian thật, lần lượt chia đôi, `only=left`, `only=right`; URL thêm `&autostart=0` (để chỉ có trận mưa do `abStart()` bắn);
     - mỗi lần: `abStart()`, chờ 0,5 s, đo khoảng rAF trong 8 s → `{frames, mean, p50, p95, p99, max, over20, over33}`, kèm `__lab.ab()` và `__lab.memory()`;
     - hai nửa vẽ chung một lượt, nên **thời gian khung của từng nửa** lấy từ lần chỉ vẽ một cách trên cả màn hình.
   - **`hitch`:** ba lần `only=right&prewarm=0`, `only=right&prewarm=1`, `only=left&prewarm=0`, đều có `autostart=0`. Mỗi lần: bật đo, chờ 1 s, `abStart()`, đo tiếp 1,5 s; ghi khoảng rAF dài nhất trước và sau khi bắt đầu.
   - **Kiểm transcoder:** sau khi lần mở đầu tiên đã sẵn sàng, đọc `performance.getEntriesByType("resource")`; lấy các mục có tên chứa `basis_transcoder.` và không chứa `?import`, ghi `name` và `responseStatus` vào `hybrid-ab.json`. Phải có đúng 2 mục, cả hai là 200; khác thì ghi vào báo cáo.
   - **Đầu ra:** `<OUT_DIR>/hybrid-ab.json`.
   - **Chạy:**
     - server nền: `cd W && npx vite --host 127.0.0.1 --port 3126 --strictPort` (cổng bận thì 3127);
     - kịch bản: `cd W && ../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-hybrid-ab.mjs --width=1920 --height=1080`;
     - xong thì tắt server, viết `ABOUT.md` (`purpose`, `made-by: codex 326`, `doc`, `delete-when`), rồi chạy `node scripts/review-index.mjs` từ gốc repo.

## Test (`tests/lab/hybrid-flipbook.test.ts`, môi trường node, không cài gói)
- **Manifest:** đọc đủ trường mới, URL có md5. Trường hỏng thì bỏ, không ném lỗi (`yFlip` false, layout lạ, `strength` 0 hoặc lớn hơn 1, file có `/`). Mục cũ không có `ktx2` hay `motion`.
- **Vector:**
  - `motionDecode(128) = 0`, `(255) = +s`, `(1) = −s`;
  - `motionSampleUv(0.5, 0.5, 0.1, −0.05, 0.25)` → uv0 = (0.475, 0.5125), uv1 = (0.575, 0.4625), cộng một ca bị kẹp;
  - `ktx2Pick` không đổi sang variant kia.
- **Pha:** `cometPhase(n)` nằm trong [0, 1); `floor(phase·32)` của n = 0–7 khác nhau từng đôi; hai n liền nhau (n = 0–23) cách nhau ít nhất 4 khung theo vòng; `cometFrame(0, 0.5, 24, 32) = 16`.
- **`FlipbookPool`:**
  - shader có dòng `discard` của `uClipSide` và dòng `vec4 m = texture2D(uMv`;
  - `attach` có `{mv}` và `meta.motion` → `uMvOn = 1`; `FLIPBOOK_MOTION.blend = false` → 0 (đặt lại sau test); không có `mv` → 0;
  - `clipSide` đặt đúng uniform;
  - mục v2 (`loopMode: "stepped"`) vẫn `attach` được và vẫn có khối vector.
- **`FlipbookLibrary` với loader KTX2 giả:** gọi đúng URL `uastc`, không gọi `TextureLoader` cho mục đó. Thêm một ca: mục hoãn qua `fetchAtlas` gọi đúng URL `uastc` và có `controls.mv`. Loader từ chối thì quay về `TextureLoader` (spy) và có cảnh báo. `afterEach` gọi `setFlipbookKtx2(null)`.
- **Hàm thuần:** `textureGpuBytes` (mipmap 1000 + 250 byte → 1250; ảnh 4×2 có mipmap → 4·2·4·4/3); `abCardScale` với crop `[-67,-37,2050,1154]`, frame `[1920,1080]` → 1.0685 (±1e-4).
- **Manifest thật** (`it.skipIf` khi chưa có): hai id đều có `ktx2.uastc`, `ktx2.etc1s`, `motion`; rồng có `videoVariants` `crf23` và `720p`, `compareWith` trỏ về expansion; sao chổi có trục `comet`.

## Kiểm
- `cd W && npx tsc --noEmit` sạch.
- `cd W && npx vitest run tests/lab tests/view` qua. Trước phiếu: `tests/lab` 14 file / 79 test, `tests/view` 30 file / 421 test.
- Khi đã có file của phiếu 325: chạy mục 7 với `PART=all`.

## Xong khi
Các lệnh kiểm qua. Báo cáo ghi:
- file đã sửa, số dòng thêm, kết quả test;
- mỗi cảnh:
  - format nén được chọn (`state().right.format`) và nguồn (`ktx2-uastc` hay `png`);
  - MB tải và MB GPU từng bên;
  - thời gian khung: chia đôi, chỉ trái, chỉ phải;
  - giật lần đầu khi có và không có prewarm, và khi video phát lần đầu;
  - `glError`;
  - đường dẫn và dung lượng hai MP4;
- mọi cảnh báo trong console.

Nếu KTX2 không nạp được (nguồn vẫn là `png`): chép lỗi console vào báo cáo; không đổi cấu hình hay đường dẫn transcoder.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`). **Chỉ ghi dòng này khi thật sự hết hạn mức;** làm xong phiếu thì không ghi (bộ hàng đợi đọc dòng này là "chờ rồi chạy lại").

## Ghi chú từ phản biện vòng 1
- Crop của sao chổi khoảng 1094/1080: thẻ lai to hơn video khoảng 1,3 %. Nhân `abCardScale(meta.sourceRect)` cho rim lai trong cảnh A/B để hai nửa khớp.

## Ghi chú từ phản biện vòng 2
- Với `only=left` (mode video), `CometHead` nhả video khi `idle` vượt 1,5 s: chỉ đếm `idle` sau lần vẽ đầu tiên kể từ `load()`; mặc định của lab không đổi.
- `settle()`: đăng ký `requestVideoFrameCallback` ngay sau mỗi lần tua, không đợi tới lúc gọi `settle()`.

## Vòng 3 và giao việc
Phản biện vòng 3 (`326-critic-r3.md`) còn 4 lỗi cụ thể, đã sửa đúng câu chữ ở trên. Theo luật, không có vòng 4: Claude giao phiếu và tự kiểm kết quả sau khi Codex xong (test, transcoder trả 200, hai cảnh A/B lên đúng trong lab).
