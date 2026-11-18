# Phiếu 258 · Tu Tiên · Code: `FlipbookPool` bản 2 (gói CX-B)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`: shader, manifest và tương thích ngược). Lời giải đã chốt ở mục "Việc"; Codex không thiết kế lại. Chỗ nào không làm được đúng như viết thì dừng chỗ đó, ghi vào báo cáo, không tự chọn cách khác.

**Báo cáo:** `docs/codex-queue/258-report.md` (tiếng Việt).

**Đường duyệt:** Claude tự phân tích; ChatGPT duyệt lượt 1 (FAIL, các lỗi đã xử lý). Agent phản biện Claude: lượt 1–3 FAIL (mỗi lỗi đã kiểm ở mã và sửa, ghi ở "Phản biện"), lượt 4 PASS (tự tính lại mọi băm, mốc, số thử). Đường phản biện Claude theo bước 9 của skill `agent-orchestration`; ChatGPT và Gemini vẫn đăng nhập, lúc 14:10 một agent kết luận nhầm. **Claude (người chốt) giao Codex lúc 18:42 ngày 04/11, khi mới có một PASS,** vì làn Codex đang rỗi. Lượt phản biện thứ hai vẫn chạy song song như một bước kiểm thêm; lỗi nào nó tìm ra sẽ thành phiếu sửa nối tiếp. Không gộp gì trước khi Claude duyệt diff và kiểm trong lab.

## Bối cảnh
- Kế hoạch: `docs/games/tu-tien/skills/INTEGRATION_PLAN_2026-11-04.md` §2.2–2.6, §3 hàng CX-B, §7. Kế hoạch là bản nháp lộ trình; lời giải của gói này do Claude chốt trong phiếu, sau khi kiểm từng điểm ở mã và ở three r170.
  - Hồ sơ ChatGPT (bản trả lời đầu và lượt tự duyệt 1, FAIL): `docs/games/tu-tien/skills/source/flipbook-v2-chatgpt-2026-11-04.md`. Không có hồ sơ Gemini: phiếu đi đường phản biện Claude theo bước 9 của skill `agent-orchestration` (hai trợ lý vẫn đăng nhập; lúc 14:10 một agent kết luận nhầm).
  - Bảng xử lý 12 lỗi ChatGPT nêu và các chỗ Claude không theo ChatGPT: `docs/codex-queue/258/PROGRESS.md`.
- Số phiếu: kế hoạch §7 ghi `257-tt-flipbook-v2`; ghi chú đầu kế hoạch dời số lên một bậc, nên CX-B là **258**.
- **Mã hiện tại** (`games/immortality-cultivation`, `main` ở `bc94110`, Claude đã đọc toàn bộ `src/view/skills/flipbook.ts`, 907 dòng):
  - `parseFlipbookManifest(value, base)` trả `Map<string, FlipbookMeta>`; `FlipbookMeta` có đúng 12 khóa theo thứ tự `id, url, cols, rows, frames, fps, loop, mode, aspect, pivot, start, heading`; trường lạ bị bỏ qua.
  - `FlipbookLibrary.load` nạp atlas bằng `THREE.TextureLoader`: `SRGBColorSpace`, mipmap, `LinearMipmapLinearFilter`, `premultiplyAlpha = false`. `add(meta, texture)`, `reset()`, `get(id)` trả `Entry { meta, texture }`.
  - `FlipbookPool(id, mode, capacity, renderOrder, blank)`: một `InstancedBufferGeometry`, một `ShaderMaterial` (`VERTEX`, `FRAGMENT`), một lệnh vẽ; trộn `CustomBlending` ONE / ONE_MINUS_SRC_ALPHA (alpha ZERO / ONE). Thuộc tính instance `iPos`(3), `iData`(4: size, angle, frame, alpha), `iColor`(4), `iDir`(4), `iAge`(4: x tuổi/đời, y mốc `cool`, z seed, w `erode`), `iLift`(2); mảng trạng thái `STRIDE = 35`; `update` nén các sprite sống về chỉ số `n`.
  - Fragment hôm nay: `f = uLoop>0.5 ? mod(vFrame,uFrames) : clamp(...)`, `f1 = uLoop>0.5 ? mod(f0+1,uFrames) : min(...)`, `w = uStep>0.5 ? 0 : f-f0`. **Clip lặp hòa chéo khung cuối vào khung đầu (bóng chồng).** `burn` (từ `cool`) và `erode` (từ `iAge.w`) là ngưỡng trên độ phủ màu cộng nhiễu, không có trường vẽ tay.
  - Người dùng: `element-fire.ts` (6 pool, `setSoot`, `setHeatRamp`, `taper`, `blur`, `softM`, `setSharpen`, `setGrade`), `element-stage.ts` (`FlipbookPlayer`, `clip()` trả `{ texture, meta }`), `sword-skills.ts` (`flameOf` đọc `cols, rows, frames, fps`), `src/lab/skills-main.ts` (`FlipbookMode`, `flipbooks.pool`). Test: `tests/view/element-layer.test.ts` (dựng `FlipbookMeta` bằng tay với 12 khóa; đọc `fragmentShader` của pool mới và so chuỗi đoạn `if (uSharpen.y > 0.0)`).
  - `tsconfig.json` gồm `tests/` và `types: ["node", "vite/client"]`, nên mọi trường mới của `FlipbookMeta` và `FlipOptions` **phải là tùy chọn**, và test được dùng `node:crypto`. `vitest` 3.2.7 môi trường `node`, không WebGL. TypeScript 6.0.3.
  - Mốc test: **793 test, 84 tệp, đều qua** (Claude chạy ở `bc94110` lúc 14:50 ngày 04/11, cùng lệnh ở Kiểm 2).
- **Đã kiểm trong three r170** (`node_modules/three/build/three.module.js`, bản 0.170.0):
  - dòng 25018–25025: `UNPACK_FLIP_Y_WEBGL = texture.flipY`, `UNPACK_PREMULTIPLY_ALPHA_WEBGL = texture.premultiplyAlpha`, `UNPACK_COLORSPACE_CONVERSION_WEBGL = NONE` khi `colorSpace === NoColorSpace`;
  - dòng 19579–19595 (`generateDefines`): mỗi khóa `defines` thành `#define TÊN giá_trị`, giá trị `false` bị bỏ, nên `FB_LOOP: 0` vẫn được định nghĩa;
  - dòng 20978–21016 (`getProgramCacheKey`): khóa chương trình gồm mã nguồn shader và `defines`; dòng 9722: `material.needsUpdate = true` tăng `version`, dòng 30702 dựng lại chương trình;
  - dòng 15387–15430 (`WebGLBindingStates.needsUpdate`): chỉ thuộc tính mà chương trình khai báo mới được gắn; dòng 17640 (`WebGLGeometries.update`): **mọi** thuộc tính của geometry đều được tải lên GPU. Vì vậy `iCtl`, `iVar` chỉ được thêm vào geometry khi pool sang đường v2.
- `art-src/` không nằm trong Git, nên worktree không có atlas thật: test chỉ dùng manifest và `THREE.Texture` dựng sẵn trong test.

## Làm ở đâu
- **Claude tạo trước khi chạy:** `git -C games/immortality-cultivation worktree add ../.wt-immortality-cultivation-codex -b codex/flipbook-v2 <HEAD của main>`, rồi symlink `node_modules` như phiếu 255. Nếu `main` đã đi quá `bc94110`, Claude kiểm `git -C games/immortality-cultivation diff bc94110 HEAD -- src/view/skills/flipbook.ts tests/view/element-layer.test.ts` rỗng và chạy lại để lấy số test mốc mới trước khi giao.
- Không ghi gì trong `games/immortality-cultivation/` (agent khác đang làm ở đó).

### Được ghi
- `games/.wt-immortality-cultivation-codex/src/view/skills/flipbook.ts`;
- `games/.wt-immortality-cultivation-codex/tests/view/flipbook-v2.test.ts` (tạo mới);
- `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-flipbook-v2.md` (tạo mới);
- `docs/codex-queue/258-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa file khác những file trên, nhất là `element-fire.ts`, `element-stage.ts`, `element-*.ts`, `sword-skills.ts`, `src/lab/**`, `tests/view/element-layer.test.ts` (phải qua mà không sửa), manifest và ảnh trong `art-src/`.
- Đổi một ký tự nào của hằng `VERTEX` và `FRAGMENT` (Test 1 so SHA-256 với `bc94110`), hay đổi `STRIDE = 35`.
- Đổi ý nghĩa của bất kỳ export, phương thức, setter hay trường `FlipOptions` đang có. Chỉ được **thêm** tham số tùy chọn ở cuối.
- Chạy dev server, mở trình duyệt, tải gói hay ảnh, sinh ảnh.

## Việc (lời giải đã chốt)

### 0. Hai đường shader
- **Đường cũ.** Meta không có trường kích hoạt v2 (dưới đây) thì pool dùng nguyên `VERTEX` và `FRAGMENT`, `defines` rỗng, không thêm thuộc tính vào geometry, không đặt `needsUpdate`. Clip cũ `loop: true` vẫn hòa chéo bọc vòng như hôm nay. Đây là **ngoại lệ tương thích có chủ đích**: điều kiện nhận "atlas cũ y nguyên từng điểm ảnh" thắng luật "không hòa chéo bọc vòng" đối với manifest chưa đổi. Bỏ ngoại lệ là việc của phiếu lắp (CX-D, CX-G), khi từng clip được ghi `loopMode` và đo R_seam.
- **Đường v2.** Hai chuỗi `VERTEX_V2`, `FRAGMENT_V2` dựng **một lần lúc nạp module** từ `VERTEX` và `FRAGMENT` bằng `replaceOnce` (mục 3), cộng `defines` `FB_LOOP`, `FB_CTRL_A`, `FB_CTRL_B`. Không chọn đường bằng `if` trên uniform.
- **Trường kích hoạt v2:** `loopMode`, `frameRange`, `controlA`, `controlB`, `timingProfile` ("mục v2" = mục manifest có ít nhất một trường này khác `undefined`). `variants`, `anchor`, `sourceFps` không kích hoạt v2; `variants` chỉ có hiệu lực ở mục v2.
- **`variants` đã có trong manifest cũ (ngoại lệ tương thích thứ hai, có chủ đích).** Ba mục hiện có mang `"variants": 8`: `fire-twinkle-set` (`art-src/lab/vfx/fire/manifest.json`), `glint-gold-twinkle-set` và `glint-starburst-set` (`art-src/lab/vfx/aura/manifest.json`); cả ba `cols 16, rows 8, frames 16`, `"order": "one element per row (variant), its frames left to right"`, json đi kèm ghi `"playback": "one-shot per row (pick a row at random)"`. Nghĩa của `variants` trong phiếu này **là nghĩa ba tệp đó đang dùng**: `frames` là số khung của **một** biến thể, biến thể v chiếm các ô `v·frames … v·frames + frames − 1` (một hàng khi `frames = cols`), `variants · frames ≤ cols · rows`. Ba mục đó không có trường kích hoạt v2, nên **ở lại đường cũ**: parser bỏ qua `variants` của chúng như trường lạ hôm nay (không kiểm, không đặt khóa), meta đúng 12 khóa, pool phát 16 khung của hàng 0, `playLife` 16/24 s, y như hôm nay ("Claude kiểm sau" mục 2 đòi `fire` và `aura` chênh 0). Bật biến thể cho chúng là việc của phiếu lắp (CX-D, CX-G): chỉ cần thêm `"loopMode": "none"` vào mục, khi đó clip thành 8 biến thể × 16 khung (hàng v), spawn lần lượt hàng 0…7, đời vẫn 16/24 s. Phiếu này không sửa manifest nào.

### 1. Kiểu và manifest
Kiểu mới (export):
```ts
export type FlipbookLoopMode = "none" | "stepped" | "holderode";
export interface FlipbookTiming {
  readonly revealTicks: number; // ngưỡng hiện T(tick) = clamp((tick + 1) / revealTicks, 0, 1)
  readonly holdEnd: number;     // tick cuối của pha giữ (e = -width tới đây)
  readonly tearEnd: number;     // tick cuối của pha xé (e tới tearE)
  readonly tearE: number;       // e ở tearEnd
  readonly erodeEnd: number;    // tick e chạm 1 (hết)
  readonly width: number;       // bề rộng dải xói
  readonly rampTicks: number;   // số tick dải màu bậc trộn vào sau holdEnd
}
export const FLIPBOOK_TIMING = {
  // TRIAL (INTEGRATION_PLAN §2.6): hiện 0–3, giữ 4–9, xé 10–20, than và bụi 20–42.
  "impact-key1": { revealTicks: 4, holdEnd: 9, tearEnd: 20, tearE: 0.85, erodeEnd: 42, width: 0.08, rampTicks: 4 },
} as const satisfies Readonly<Record<string, FlipbookTiming>>;
export type FlipbookTimingName = keyof typeof FLIPBOOK_TIMING;
export const FLIPBOOK_ERODE_WIDTH = 0.08; // bề rộng dải xói khi không có lịch
```

`FlipbookMeta` thêm các trường **tùy chọn**, giữ nguyên 12 trường cũ:
```ts
  /** v2: cách phát khung (thắng `loop`). */
  readonly loopMode?: FlipbookLoopMode;
  /** v2: đoạn khung phát [đầu, cuối], bao hai đầu, tính trong một biến thể (0 … frames − 1). */
  readonly frameRange?: readonly [number, number];
  /** v2: số biến thể (chỉ có ở meta v2: parser bỏ qua `variants` của mục không có trường kích hoạt v2). `frames` là số khung của MỘT biến thể; biến thể v chiếm các ô v·frames … v·frames + frames − 1 (một hàng khi frames = cols, như các atlas glint hiện có); variants · frames ≤ cols · rows. */
  readonly variants?: number;
  /** v2: URL mặt nạ A (R bao, G ink, B vạch nóng, A thứ tự sống sót) và mặt nạ B (R thứ tự hiện, G ảnh hưởng chuyển động). */
  readonly controlA?: string;
  readonly controlB?: string;
  /** Điểm gốc của hiệu ứng trong ô (0–1 từ góc trên trái); khi có thì `pivot` lấy giá trị này. */
  readonly anchor?: readonly [number, number];
  /** fps của clip nguồn (chỉ là dữ liệu cho công cụ và cổng đo; không đổi tốc độ phát, tốc độ phát vẫn là `fps`). */
  readonly sourceFps?: number;
  /** Lịch hiện và xói mặc định (khóa của FLIPBOOK_TIMING); cần mặt nạ A. */
  readonly timingProfile?: FlipbookTimingName;
```

`parseFlipbookManifest`: giữ nguyên mọi bước kiểm và mọi giá trị cũ (kể cả `frames ≤ cols · rows` và `start < frames`). Sau khi đã có `cols, rows, frames, cw, ch, mode, md5` của mục, đọc trường mới. **Trường nào vắng thì không đặt khóa đó** (meta của manifest cũ có đúng 12 khóa như hôm nay, cùng thứ tự; kể cả mục cũ mang `variants` mà không có trường kích hoạt v2, §0). Mỗi trường mới, khi có mặt mà sai, ném `Error("Invalid flipbook <tên trường>: " + id)`:
- `variants`: **chỉ đọc ở mục v2** (§0); mục không phải v2 bỏ qua hoàn toàn (không kiểm, không đặt khóa, kể cả giá trị sai như `0` hay `"x"`). Ở mục v2: số nguyên, `variants ≥ 1`, `variants · frames ≤ cols · rows` (`frames` là số khung của một biến thể, đã lấy mặc định `cols · rows` khi vắng, nên `frames` vắng chỉ nhận `variants: 1`). Không đổi `frames`: meta lưu `frames` của manifest (khung của một biến thể).
- `frameRange`: mảng đúng 2 số nguyên `[a, b]`, `0 ≤ a ≤ b < frames` (trong một biến thể; không phụ thuộc `variants`).
- `loopMode`: đúng một trong `"none"`, `"stepped"`, `"holderode"`.
- `controlA`, `controlB`: chuỗi khớp regex `FILE` có sẵn; URL lưu trong meta = `base + tên + md5` (cùng hậu tố `?v=<md5>` như `url`, rỗng khi mục không có `md5`). `controlB` mà thiếu `controlA`: ném. Có mặt nạ mà `mode` đã giải ra khác `"rgba"`: ném.
- `anchor`: mảng 2 số hữu hạn ≥ 0; nếu một trong hai > 1 thì đọc theo pixel ô (`[x / cw, y / ch]`, như `pivot`); sau đó cả hai phải ≤ 1. Có `anchor` thì `pivot` của meta = giá trị này (thay đọc `pivot`), và `anchor` lưu cùng giá trị.
- `sourceFps`: số hữu hạn, `0 < sourceFps ≤ 240`.
- `timingProfile`: chuỗi là khóa riêng của `FLIPBOOK_TIMING` (`Object.prototype.hasOwnProperty.call`); thiếu `controlA` thì ném.
- Khi có ít nhất một trường kích hoạt v2: nếu có `loopMode` thì `loop = loopMode !== "none"` (thắng `loop` cũ); nếu thiếu `loopMode` thì đặt `loopMode = loop ? "stepped" : "none"`.

Hàm export mới:
```ts
export function isFlipbookV2(meta: FlipbookMeta): boolean; // loopMode | frameRange | controlA | controlB | timingProfile (không xét variants)
export function flipbookLoopMode(meta: FlipbookMeta): FlipbookLoopMode; // meta.loopMode ?? (meta.loop ? "stepped" : "none")
```

Hai hàm nội bộ dùng chung cho `spawn`, `playLife`, `slowFromOf`, `clipS` (không cấp phát; với meta cũ cho đúng số cũ):
```ts
/** Khung cuối + 1 trong một biến thể (`frames` là số khung của một biến thể). Meta cũ: frames. */
function frameEnd(meta: FlipbookMeta): number {
  return meta.frameRange !== undefined ? meta.frameRange[1] + 1 : meta.frames;
}
/** Khung đầu. Meta cũ: o.frame ?? (loop ? 0 : start), y như hôm nay. */
function firstOf(meta: FlipbookMeta, o: FlipOptions): number {
  if (o.frame !== undefined) return o.frame;
  const lo = meta.frameRange?.[0] ?? 0;
  if (meta.loop) return lo;
  return Math.min(frameEnd(meta) - 1, Math.max(lo, meta.start));
}
```
- `spawn`: `first = firstOf(meta, options)` thay biểu thức cũ.
- `slowFromOf`: `first = firstOf(meta, o)`, `last = Math.min(frameEnd(meta), o.until !== undefined ? o.until + 1 : frameEnd(meta))`.
- `playLife`: sau `if (o.life !== undefined) return o.life;` thêm `const timing = flipbookTimingOf(meta, o); if (timing !== null) return (timing.erodeEnd + 1) / 60;`; các dòng sau dùng `firstOf` và `frameEnd` như `slowFromOf`. `playLife` chỉ thấy meta và `o`, không thấy pool: clip có `controlA` và lịch lấy đời theo lịch ở **mọi** pool, kể cả pool không có mặt nạ A (chế độ khác `rgba`, hay `attach` không kèm `controls.a`). Đây là lựa chọn đã chốt (giữ `playLife` bằng đời `spawn` dùng); JSDoc `FlipOptions.timing` (§4) và JSDoc của `playLife` ghi đúng như vậy.
- `clipS(rate)`: meta cũ giữ nguyên biểu thức; meta v2: `(frameEnd(meta) − firstOf(meta, EMPTY_OPTIONS)) / (meta.fps · max(0.05, rate))`, `EMPTY_OPTIONS` là hằng `{}` của module.

### 2. Nạp mặt nạ
- Kiểu export mới:
  ```ts
  export interface FlipbookControls {
    readonly a?: THREE.Texture; // mặt nạ A
    readonly b?: THREE.Texture; // mặt nạ B
  }
  ```
- `Entry` thêm `controls: FlipbookControls | null`. `FlipbookLibrary.add(meta, texture, controls: FlipbookControls | null = null)`. `reset()` gọi `dispose()` cả atlas lẫn `controls?.a`, `controls?.b`.
- `FlipbookLibrary.load`, với mỗi meta: nạp atlas như hôm nay (không đổi một thiết lập nào); rồi nếu có `meta.controlA` thì nạp, rồi `meta.controlB`, cùng `loader`. Mỗi mặt nạ đặt **trước khi** `add`:
  - `colorSpace = THREE.NoColorSpace`, `premultiplyAlpha = false`;
  - `generateMipmaps = true`, `minFilter = THREE.LinearMipmapLinearFilter`, `magFilter = THREE.LinearFilter`, `anisotropy` như atlas (giữ mặt nạ khớp atlas ở mọi mức mip);
  - `wrapS = wrapT = THREE.ClampToEdgeWrapping`;
  - **không** đổi `flipY` (mặc định `true`, giống atlas: cùng hướng ô, `vxCell` dùng chung).
- Một tệp hỏng (atlas hay mặt nạ khai trong manifest): `console.warn`, `dispose()` các texture của clip đó đã nạp, và **không** `add` clip đó (giống atlas hỏng hôm nay: kit vẽ không có clip). Không bao giờ chạy một clip v2 thiếu mặt nạ đã khai.
- `FlipbookPlayer`: hai chỗ gọi `pool.attach(entry.meta, entry.texture)` (trong `library()` và `pool()`) thành `pool.attach(entry.meta, entry.texture, entry.controls)`.
- Pool không bao giờ `dispose` texture: thư viện sở hữu atlas và mặt nạ.

### 3. Shader v2
**Dựng chuỗi** (hằng module, một lần lúc nạp):
```ts
function replaceOnce(src: string, anchor: string, text: string): string {
  const at = src.indexOf(anchor);
  if (at < 0 || src.indexOf(anchor, at + 1) >= 0) throw new Error("[flipbook] v2 shader anchor not found once: " + anchor.trim().slice(0, 48));
  return src.slice(0, at) + text + src.slice(at + anchor.length);
}
```
(Claude đã kiểm trên chuỗi thật của `bc94110`: mỗi neo dưới đây xuất hiện đúng một lần.)

`VERTEX_V2` = `VERTEX` sau ba lần `replaceOnce`:
1. neo `"attribute vec2 iLift;\n"` → thêm sau nó `"attribute vec4 iCtl;\nattribute float iVar;\n"`;
2. neo `"varying vec4 vAge;\n"` → thêm sau nó `"varying vec4 vCtl;\nvarying float vVar;\n"`;
3. neo `"  vAge = iAge;\n"` → thêm sau nó `"  vCtl = iCtl;\n  vVar = iVar;\n"`.

`FRAGMENT_V2` = `FRAGMENT` sau năm lần `replaceOnce`:
1. neo `"uniform vec4 uGrade;\n"` → thêm sau nó khối uniform:
   ```glsl
   uniform vec2 uRange;
   uniform sampler2D uCtlA;
   uniform sampler2D uCtlB;
   uniform vec2 uInsetA;
   uniform vec2 uInsetB;
   uniform vec4 uInk;
   uniform float uBodyCap;
   uniform vec4 uHot;
   uniform float uHotLead;
   uniform vec3 uRamp0;
   uniform vec3 uRamp1;
   uniform vec3 uRamp2;
   ```
2. neo `"varying vec4 vAge;\n"` → thêm sau nó `"varying vec4 vCtl;\nvarying float vVar;\n"`;
3. neo `"void main() {\n"` → chèn **trước** nó hằng `FB_COMPOSE_GLSL` (export):
   ```glsl
   // FlipbookPool v2, mask A (R hull, G ink, B hot line, A survival order): its survival order recoloured through the
   // stepped ramp (uRamp0 white-gold, uRamp1 orange, uRamp2 crimson, uSoot soot).
   vec3 fbRamp(float r) {
     vec3 c = uSoot;
     c = mix(c, uRamp2, smoothstep(0.23, 0.27, r));
     c = mix(c, uRamp1, smoothstep(0.48, 0.52, r));
     return mix(c, uRamp0, smoothstep(0.73, 0.77, r));
   }
   // Ink under the body under the hot core in one fragment (INTEGRATION_PLAN §2.3), premultiplied; `soft` once at the end.
   // ctl = iCtl: x reveal threshold T, y erosion threshold e, z band width, w ramp mix.
   vec4 fbComposeMasked(vec4 t0, vec4 t1, vec4 m0, vec4 m1, float b0, float b1, float w, vec4 ctl, vec3 tint, float soft) {
     vec3 pm = mix(t0.rgb * t0.a, t1.rgb * t1.a, w);
     float aAt = mix(t0.a, t1.a, w);
     vec3 cAt = aAt > 1e-4 ? pm / aAt : mix(t0.rgb, t1.rgb, w);
     if (uSharpen.y > 0.0) aAt = smoothstep(uSharpen.x, uSharpen.y, aAt);
     if (uGrade.w > 0.0) {
       float mxc = max(cAt.r, max(cAt.g, cAt.b));
       float wht = min(cAt.r, min(cAt.g, cAt.b)) / max(mxc, 1e-4);
       float heart = smoothstep(uGrade.w, 1.0, wht) * smoothstep(0.93, 1.0, mxc);
       cAt = mix(cAt, uGrade.rgb * mix(0.8, 1.0, mxc), smoothstep(0.1, 0.5, wht) * (1.0 - heart));
     }
     vec4 m = mix(m0, m1, w);
     float rev = step(mix(b0, b1, w), ctl.x + 0.002);
     float e = ctl.y;
     float wd = max(ctl.z, 1e-4);
     float eh = e + uHotLead * ctl.w;
     float live = smoothstep(e, e + wd, m.a);
     float liveH = smoothstep(eh, eh + wd, m.a);
     float ai = m.g * uInk.a * rev * live;
     float ab = min(aAt, m.r) * rev * live;
     float ah = m.b * rev * liveH;
     float r = clamp((m.a - e) / max(1.0 - e, 1e-4), 0.0, 1.0);
     vec3 ci = uInk.rgb;
     vec3 cb = min(mix(cAt, fbRamp(r), ctl.w) * tint, vec3(uBodyCap));
     vec3 ch = uHot.rgb * uHot.a * tint;
     float alpha = 1.0 - (1.0 - ai) * (1.0 - ab) * (1.0 - ah);
     vec3 rgb = ci * ai * (1.0 - ab) * (1.0 - ah) + cb * ab * (1.0 - ah) + ch * ah;
     return vec4(rgb * soft, alpha * soft);
   }
   ```
4. neo là đúng năm dòng chọn khung cũ (hằng `PICK_V1`, chuỗi nguyên văn như trong `FRAGMENT`: mỗi dòng bắt đầu bằng đúng hai dấu cách và kết thúc bằng `\n`; các khối mã trong danh sách này thụt thêm ba dấu cách chỉ vì định dạng markdown, không chép phần thụt đó):
   ```
     // Frames blend in time (uStep: held cels); a loop wraps to its first frame.
     float f = uLoop > 0.5 ? mod(vFrame, uFrames) : clamp(vFrame, 0.0, uFrames - 1.0);
     float f0 = floor(f);
     float f1 = uLoop > 0.5 ? mod(f0 + 1.0, uFrames) : min(f0 + 1.0, uFrames - 1.0);
     float w = uStep > 0.5 ? 0.0 : f - f0;
   ```
   → **thay** bằng hằng `FB_PICK_GLSL` (export):
   ```glsl
     // FlipbookPool v2: the frame pair inside the clip's segment [uRange.x, uRange.x + uRange.y - 1] (frames of its
     // variant; vVar: the variant's first cell). No loop mode crossfades the segment's last frame into its first.
     float fbVar = floor(vVar + 0.5);
     float fbN = max(uRange.y, 1.0);
     float fbLast = uRange.x + fbN - 1.0;
   #if FB_LOOP == 0
     float f = clamp(vFrame, uRange.x, fbLast);
     float f0 = floor(f);
     float f1 = min(f0 + 1.0, fbLast);
     float w = uStep > 0.5 ? 0.0 : f - f0;
   #else
     float f = uRange.x + mod(vFrame - uRange.x, fbN);
     float f0 = clamp(floor(f), uRange.x, fbLast);
   #if FB_LOOP == 1
     float f1 = f0;
     float w = 0.0;
   #else
     float f1 = f0 + 1.0 > fbLast ? uRange.x : f0 + 1.0;
     float w = uStep > 0.5 ? 0.0 : clamp(f - f0, 0.0, 1.0);
   #endif
   #endif
   #if FB_LOOP == 2 || defined(FB_CTRL_A)
     // Hold and erode between two frames: each pixel switches from f0 to f1 at its own moment (its survival order in
     // mask A, else the clip's noise through a logistic), never a see-through crossfade. Always in "holderode"; with
     // mask A also when the pool sharpens (setSharpen).
   #if FB_LOOP == 2
     bool fbSwitch = true;
   #else
     bool fbSwitch = uSharpen.y > 0.0;
   #endif
     if (fbSwitch && w > 0.0) {
   #ifdef FB_CTRL_A
       float order = texture2D(uCtlA, vxCell(f0 + fbVar, clamp(vUv, uInsetA, 1.0 - uInsetA))).a;
   #else
       float nO = vxNoise(vUv * 6.0 + vec2(vAge.z * 13.1, vAge.z * 7.3)) * 0.65 + vxNoise(vUv * 15.0 - vec2(vAge.z * 5.7, 0.0)) * 0.35;
       float order = 1.0 / (1.0 + exp(-8.0 * (nO - 0.5)));
   #endif
       w = smoothstep(-0.08, 0.08, w - mix(0.08, 0.92, order));
     }
   #endif
     f0 += fbVar;
     f1 += fbVar;
   ```
   (`fbVar` làm tròn vì một varying hằng có thể nội suy thành 7,9999995: `vxCell` sẽ lấy sai ô.)
5. neo `"  if (uMode < 0.5) {\n"` → thêm sau nó hằng `FB_MASKED_GLSL` (export):
   ```glsl
   #ifdef FB_CTRL_A
       vec2 uvA = clamp(vUv, uInsetA, 1.0 - uInsetA);
       vec4 m0 = texture2D(uCtlA, vxCell(f0, uvA));
       vec4 m1 = texture2D(uCtlA, vxCell(f1, uvA));
   #ifdef FB_CTRL_B
       vec2 uvB = clamp(vUv, uInsetB, 1.0 - uInsetB);
       float b0 = texture2D(uCtlB, vxCell(f0, uvB)).r;
       float b1 = texture2D(uCtlB, vxCell(f1, uvB)).r;
   #else
       float b0 = 0.0;
       float b1 = 0.0;
   #endif
       gl_FragColor = fbComposeMasked(t0, t1, m0, m1, b0, b1, w, vCtl, vTint, soft);
       return;
   #endif
   ```

**Hệ quả, viết ra để Codex không phải đoán:**
- Mọi phần khác của `FRAGMENT_V2` là chữ của `FRAGMENT`: `uv = clamp(vUv, 0.004, 0.996)` và hai lần lấy mẫu atlas (với `uBlur`), `border`, `vignette`, `soft`, `burn`, `n`, toàn bộ nhánh `rgba` cũ (sharpen, grade, erode, burn), và ba nhánh `fire`, `smoke`, `heat` (`vec4 t = mix(t0, t1, w)`). Vì vậy ở đường v2 **không mặt nạ**, bốn chế độ chạy y như hôm nay, chỉ khác cặp khung `f0, f1, w` (và `w` đã là trọng số chuyển từng điểm ảnh khi `holderode`).
- `none`: chạy một lần trong đoạn, giữ khung cuối; hòa chéo hai khung kề nhau trong đoạn (như clip cũ không lặp), `stepped` (setter `uStep`) tắt hòa chéo; `setSharpen` giữ nguyên cách cũ ở đường không mặt nạ, và ở đường có mặt nạ thì đổi khung từng điểm ảnh theo `A.a` cộng nén độ phủ atlas qua `smoothstep(lo, hi, ·)`.
- `stepped`: lặp đoạn, khung giữ, không bao giờ trộn hai khung.
- `holderode`: lặp đoạn; giữa hai khung mỗi điểm ảnh đổi khung ở thời điểm riêng (cùng hằng `±0.08`, `mix(0.08, 0.92, ·)` như sharpen hiện nay), kể cả ở chỗ bọc từ khung cuối về khung đầu đoạn. Không bao giờ là một ảnh chồng nửa trong suốt.
- Đường có mặt nạ không đọc `vAge.x`, `vAge.y`, `vAge.w`: `cool` và `erode` đi vào `iCtl.y` (mục 4), nên không bị áp hai lần.
- Lề nửa texel: atlas giữ `0.004` của đường cũ; `uInsetA`, `uInsetB` riêng cho từng mặt nạ (mục 4). Tổng thuộc tính đỉnh v2: `position, uv, iPos, iData, iColor, iDir, iAge, iLift, iCtl, iVar` = 10 (≤ 16). Sampler: 3.

### 4. Pool
**Hằng mặc định** (export), constructor lấy giá trị đầu từ đây:
```ts
export interface FlipbookMaskedLook {
  readonly ink: FlipbookVec4;        // uInk: màu ink tuyến tính, alpha ink
  readonly bodyCap: number;          // uBodyCap: trần thân mỗi kênh
  readonly hot: FlipbookVec4;        // uHot: màu lõi tuyến tính, độ lợi HDR
  readonly hotLead: number;          // uHotLead: lõi tắt sớm hơn thân bao nhiêu (× ramp mix)
  readonly ramp: readonly [FlipbookVec3, FlipbookVec3, FlipbookVec3]; // uRamp0..2
  readonly soot: FlipbookVec3;       // = uSoot mặc định (setSoot)
  readonly sharpen: readonly [number, number]; // = uSharpen mặc định (setSharpen)
  readonly grade: FlipbookVec4;      // = uGrade mặc định (setGrade)
}
export const FLIPBOOK_MASKED_LOOK: FlipbookMaskedLook = {
  ink: [0.03, 0.022, 0.02, 0.55],
  bodyCap: 0.88,
  hot: [1, 0.982, 0.871, 2.2],
  hotLead: 0.1,
  ramp: [[1, 0.982, 0.871], [1, 0.473, 0.001], [0.693, 0.04, 0]], // #FFFDF0, #FFB703, #D93800 tuyến tính (như uHeat*)
  soot: [0.03, 0.022, 0.02],
  sharpen: [0, 0],
  grade: [0, 0, 0, 0],
};
```
`FlipbookVec3 = readonly [number, number, number]`, `FlipbookVec4 = readonly [number, number, number, number]` (export).

**Constructor** (thêm, không bỏ gì):
- lưu `blank` vào trường riêng `private readonly blank`;
- thêm vào `uniforms`: `uRange` (`Vector2(0, 1)`), `uCtlA`, `uCtlB` (`blank`), `uInsetA`, `uInsetB` (`Vector2(0.004, 0.004)`), `uInk` (`Vector4` từ `ink`), `uBodyCap`, `uHot` (`Vector4`), `uHotLead`, `uRamp0..2` (`Vector3`). Uniform thừa không đổi chương trình cũ (three chỉ tải uniform mà chương trình khai báo);
- cấp một lần: `iCtl = new Float32Array(capacity * 4)`, `iVar = new Float32Array(capacity)`, hai `InstancedBufferAttribute` (`DynamicDrawUsage`) **chưa gắn** vào geometry; `varCell = new Float32Array(capacity)`; `timings: (FlipbookTiming | null)[] = new Array(capacity).fill(null)`; `private v2Key: string | null = null`; `private masked = false`; `private variantTurn = 0`.

**Setter mới** (chỉ ghi uniform, gọi được trước `attach`): `setInk(r, g, b, alpha)`, `setHot(r, g, b, gain)`, `setRamp(hot, mid, low: readonly number[])`, `set bodyCap(v)`, `set hotLead(v)`.

**`attach(meta, texture, controls: FlipbookControls | null = null)`:**
1. Tám dòng hiện có giữ nguyên, cùng thứ tự (`meta`, `uMap`, `uGrid`, `uFrames`, `uLoop`, `uPivot`, `uAspect`, `uHeading`).
2. Nếu `!isFlipbookV2(meta)`: nếu `v2Key !== null` thì trả pool về đường cũ (`vertexShader = VERTEX`, `fragmentShader = FRAGMENT`, `defines = {}`, `geometry.deleteAttribute("iCtl")`, `deleteAttribute("iVar")`, `uCtlA = uCtlB = blank`, `masked = false`, `v2Key = null`, `needsUpdate = true`); rồi `return`. Pool chưa từng v2 thì không làm gì thêm.
3. V2:
   - `loop = flipbookLoopMode(meta)`; `masked = this.mode === "rgba" && controls?.a !== undefined`; `reveal = masked && controls?.b !== undefined`. (Pool không phải `rgba` bỏ qua mặt nạ.)
   - `[lo, hi] = meta.frameRange ?? [0, meta.frames − 1]` (`frames` là số khung của một biến thể); `uRange = (lo, hi − lo + 1)`.
   - `uCtlA = masked ? controls.a : blank`; `uCtlB = reveal ? controls.b : blank`.
   - `uInsetA` từ `controls.a.image`, `uInsetB` từ `controls.b.image` (mỗi mặt nạ theo độ phân giải của chính nó; B là nửa độ phân giải nên lề của nó lớn hơn): nếu `image` có `width`, `height` là số > 0 thì `(max(0.004, 0.5·cols / width), max(0.004, 0.5·rows / height))`, không thì `(0.004, 0.004)`.
   - `key = loop + "|" + masked + "|" + reveal`. Nếu `key !== v2Key`: `vertexShader = VERTEX_V2`, `fragmentShader = FRAGMENT_V2`, `defines = { FB_LOOP: 0 | 1 | 2 (none, stepped, holderode), FB_CTRL_A: 1 nếu masked, FB_CTRL_B: 1 nếu reveal }` (khóa vắng thì không đặt), gắn `iCtl`, `iVar` vào geometry nếu chưa có, `needsUpdate = true`, `v2Key = key`. Gọi lại `attach` với cùng meta (watch và `pool()` đều gọi) thì `version` không tăng.

**`flipbookTimingOf(meta, o)`** (export): `null` nếu `meta.controlA === undefined`; không thì `t = o.timing ?? meta.timingProfile`; chuỗi tra `FLIPBOOK_TIMING` (khóa lạ → `null`), đối tượng dùng thẳng. Hàm chỉ xét meta, không xét pool có mặt nạ hay không: `spawn` tự lọc bằng `this.masked`, còn `playLife` dùng thẳng (§1).

**`spawn`** (thêm, phần cũ giữ nguyên):
- `first = firstOf(meta, options)`;
- `timing = this.masked ? flipbookTimingOf(meta, options) : null`;
- `life = playLife(meta, options)` như cũ (có lịch thì mặc định `(erodeEnd + 1) / 60`; `options.life` của người gọi vẫn thắng, kể cả khi cắt lịch sớm). Trên pool không có mặt nạ A, `timing` ở đây là `null` nhưng `life` vẫn theo lịch (§1 `playLife`); hiện, xói, bỏ `cool` và `fadeOut` 0 thì không áp;
- `fadeOut` mặc định: `options.fadeOut ?? (timing !== null || (this.mode === "rgba" && (options.cool ?? 0) > 0) ? 0 : Math.min(0.12, life * 0.3))`;
- biến thể: `vars = this.v2Key !== null ? meta.variants ?? 1 : 1` (pool ở đường cũ không đọc `variants`, kể cả meta dựng tay); `v = 0`; nếu `vars > 1`: `options.variant` hữu hạn thì `v = min(vars − 1, max(0, floor(variant)))`, không thì `v = variantTurn % vars` và `variantTurn += 1`;
- **mỗi** `spawn` thành công ghi `this.timings[i] = timing` và `this.varCell[i] = v · meta.frames` (ô đầu của biến thể v; `frames` là số khung của một biến thể): slot tái dùng không giữ lịch hay biến thể cũ.

**`flipbookControl`** (export, `update` gọi, không cấp phát):
```ts
export function flipbookControl(age: number, life: number, cool: number, erode: number, timing: FlipbookTiming | null, out: { [i: number]: number }, at = 0): void {
  let T = 1, wd = FLIPBOOK_ERODE_WIDTH, e = -wd, mix = 0;
  if (timing !== null) {
    const tick = flipbookTick(age);
    T = revealThreshold(tick, timing.revealTicks); wd = timing.width; e = erodeThreshold(tick, timing); mix = rampMixAt(tick, timing);
  } else if (cool > 0) {
    // `cool` giữ nghĩa cũ (từ phần đời này cháy tàn), nay đi theo thứ tự sống sót của mặt nạ A.
    const burn = Math.min(1, Math.max(0, (age / life - cool) / Math.max(0.05, 1 - cool)));
    e = -wd + burn * (1 + wd); mix = Math.min(1, burn * 4);
  }
  // `erode` giữ nghĩa cũ (0 nguyên … 1 hết, phần mỏng trước): phần "mỏng" nay là A.a thấp.
  if (erode > 0) e = Math.max(e, -wd + erode * (1 + wd));
  out[at] = T; out[at + 1] = e; out[at + 2] = wd; out[at + 3] = mix;
}
```
Có lịch thì `cool` bị bỏ qua (lịch lo phần tàn); `erode` vẫn áp (kit dùng để hiện dần).

**`update(dt)`**: phần cũ giữ nguyên. Nếu `v2Key !== null`, trong vòng lặp, ngay sau khi ghi `iLift` ở chỉ số nén `n`: `flipbookControl(age, life, st[o + 28], st[o + 32], this.timings[i], this.iCtl, n * 4)` và `this.iVar[n] = this.varCell[i]` (`age` là tuổi lúc vẽ, trước khi cộng `dt`; khung đầu tick 0; lúc `delay` chưa hết thì sprite chưa vẽ và tuổi chưa chạy). Cuối hàm, sau vòng `ATTRS`, nếu `v2Key !== null` thì đặt `needsUpdate = true` cho hai thuộc tính v2. `ATTRS` giữ nguyên.

**`clear()`**: thêm `variantTurn = 0`.

**`FlipOptions`** thêm hai trường tùy chọn:
```ts
  /** Clip có `controlA` trong manifest: lịch hiện và xói (tên trong FLIPBOOK_TIMING hoặc một bảng); thắng `timingProfile` của manifest; clip không có `controlA` thì bỏ qua. Có lịch thì `life` mặc định (erodeEnd + 1) / 60 s ở mọi pool, kể cả pool không có mặt nạ A (qua `playLife`, nên `playLife` luôn bằng đời `spawn` dùng). Chỉ trên pool có mặt nạ A (pool `rgba` được `attach` kèm `controls.a`) lịch mới bật hiện và xói, bỏ qua `cool` và đặt `fadeOut` mặc định 0; pool khác giữ `cool`, `erode`, `fadeOut` như cũ. */
  timing?: FlipbookTimingName | FlipbookTiming;
  /** Clip v2 có `variants`: biến thể (0 …, kẹp vào khoảng; biến thể v bắt đầu ở ô v·frames); vắng thì pool lần lượt 0, 1, … (về 0 khi clear). Clip ở đường cũ bỏ qua. */
  variant?: number;
```

### 5. Hàm CPU (export, chạy được trong node, cùng phép tính như GPU)
- `flipbookTick(ageS) = Math.max(0, Math.floor(ageS * 60 + 1e-3))`. Epsilon `1e-3` tick vì tuổi lưu trong `Float32Array`: Claude đã chạy cộng dồn `Math.fround` với `dt` = 1/30, 1/60, 1/75, 1/120, 1/144 qua 400 bước, không lệch tick nào so với tuổi chính xác.
- `revealThreshold(tick, revealTicks = 4) = clamp((tick + 1) / revealTicks, 0, 1)`.
- `erodeThreshold(tick, t)`: `tick ≤ holdEnd` → `−width`; `tick ≤ tearEnd` → `−width + (tearE + width)·(1 − (1 − x)²)`, `x = (tick − holdEnd)/(tearEnd − holdEnd)`; `tick < erodeEnd` → `tearE + (1 − tearE)·(tick − tearEnd)/(erodeEnd − tearEnd)`; còn lại `1`.
- `rampMixAt(tick, t) = clamp((tick − holdEnd) / rampTicks, 0, 1)`.
- `srgbToLinear(c)`: `c ≤ 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4`. Atlas giữ `SRGBColorSpace` (GPU giải mã trước khi lọc), nên mẫu atlas đưa vào hàm CPU là giá trị đã giải mã: `srgbToLinear(byte / 255)`; mặt nạ là `byte / 255`.
- `flipbookFramePair(vFrame, lo, count, loop, step, out: { f0; f1; w })`: đúng khối `#if FB_LOOP` của `FB_PICK_GLSL` (trước bước chuyển từng điểm ảnh, trước khi cộng biến thể). `mod(x, y)` của GLSL viết là `x − y·Math.floor(x / y)`, không dùng `%`.
- `flipbookSwitch(w, order) = w > 0 ? smoothstep(−0.08, 0.08, w − mix(0.08, 0.92, order)) : w`. Áp khi `loop === "holderode"`, hoặc khi pool có mặt nạ A và sharpen bật.
- `composeLayers(ai, ab, ah, ci, cb, ch, out)`: công thức §2.3 (`out` = RGB premultiplied, alpha).
- `composeFlipbookMasked(s: FlipbookMaskedSample, look: FlipbookMaskedLook, out)`: chép `fbComposeMasked` **từng phép, cùng thứ tự** (`step(edge, x)` là `x < edge ? 0 : 1`; `smoothstep` của GLSL), với
  ```ts
  export interface FlipbookMaskedSample {
    readonly t0: FlipbookVec4; readonly t1: FlipbookVec4; // atlas như shader đọc: RGB tuyến tính, alpha thẳng
    readonly m0: FlipbookVec4; readonly m1: FlipbookVec4; // mặt nạ A ở f0, f1
    readonly b0: number; readonly b1: number;             // R của mặt nạ B ở f0, f1 (0 khi không có B)
    readonly w: number;                                   // trọng số sau flipbookFramePair và flipbookSwitch
    readonly ctl: FlipbookVec4;                           // iCtl
    readonly tint: FlipbookVec3;                          // vTint (tint × intensity)
    readonly soft: number;                                // soft của shader (đất × viền × vAlpha)
  }
  ```
- `blendPremultiplied(src: FlipbookVec4, dst: FlipbookVec3, out)`: `out.rgb = src.rgb + dst·(1 − src.a)` (đúng phép trộn ONE, ONE_MINUS_SRC_ALPHA của pool).

### 6. Test mới `tests/view/flipbook-v2.test.ts` (số cụ thể)
Sai số mặc định ±1e-6 trừ khi ghi khác. `t` là `FLIPBOOK_TIMING["impact-key1"]`; "nhìn mặc định" là `FLIPBOOK_MASKED_LOOK`.
1. **Đường cũ y nguyên.**
   - Pool mới ở cả bốn chế độ: SHA-256 (`node:crypto`) của `vertexShader` = `c2f64aa0e39d46ec17b4f60ecd3932e42178f933784a72ee8fec1d38cc25a9c7`, của `fragmentShader` = `3b5524bd2c052ed97c6261586915f9b218deb5756d0477d634e3605d05b93abd` (Claude tính trên `flipbook.ts` của `bc94110`, 1823 và 7272 ký tự).
   - Manifest cũ (`loop: true` và `loop: false`, kèm `md5`, `blend`, `alphaKind`, `modesAllowed`): `Object.keys(meta)` đúng 12 khóa cũ theo thứ tự; `isFlipbookV2` sai.
   - `attach` hai meta đó: hai hash không đổi, `Object.keys(material.defines)` rỗng, `material.version === 0`, `geometry.hasAttribute("iCtl")` sai; `uLoop` = 1 với `loop: true` (ngoại lệ tương thích).
   - **Mục glint thật mang `variants` (ngoại lệ thứ hai, §0)**: mục `fire-twinkle-set` của `art-src/lab/vfx/fire/manifest.json` chép nguyên văn, chỉ bỏ bốn trường văn xuôi dài `use`, `source`, `checks`, `modeNote` (parser không đọc), `base "/v/"`:
     ```json
     { "version": 1, "flipbooks": { "fire-twinkle-set": { "file": "fire-twinkle-set.atlas.png", "json": "fire-twinkle-set.json", "cols": 16, "rows": 8, "frames": 16, "fps": 24, "loop": false, "blend": "additive", "mode": "fire", "alpha": false, "alphaKind": "none (rgb on black; black means no energy)", "premultiplied": false, "tint": false, "modesAllowed": ["additive", "heat"], "cell": [128, 128], "pivot": [0.5, 0.5], "start": 0, "heading": 0, "tileX": false, "width": 2048, "height": 1024, "md5": "67106d17c24f841c3807a96aa7e92886", "bytes": 725605, "roles": ["glint"], "status": "candidate (owner review pending; not judged)", "variants": 8, "order": "one element per row (variant), its frames left to right" } } }
     ```
     → `Object.keys(meta)` đúng 12 khóa cũ theo thứ tự (không có `variants`, không có `loopMode`); `url === "/v/fire-twinkle-set.atlas.png?v=67106d17c24f841c3807a96aa7e92886"`; `frames === 16`; `isFlipbookV2` sai; `playLife(meta, {}) = 16/24 = 0.666667`. Cùng mục với `"variants": 0` và với `"variants": "x"`: không ném, meta `toEqual` meta trên (bỏ qua như hôm nay). Pool `"fire"` `attach` meta đó: hai hash không đổi, `defines` rỗng, `version === 0`, không có `iCtl`, `iVar`; spawn `{ variant: 3 }` rồi `update(1/60)`: `iData.z` = 0 ở lần vẽ tuổi 0 (khung 0 của hàng 0, như hôm nay).
2. **Manifest v2.**
   - `loopMode` `"none" / "stepped" / "holderode"` → `loop` sai / đúng / đúng; `"crossfade"` ném. `frameRange` có mà thiếu `loopMode`: `loop: true` → `"stepped"`, không có `loop` → `"none"`. `loop: true, loopMode: "none"` → `loop` sai.
   - 16 khung lưới 4×4, không `variants`: `frameRange [2, 5]` nhận; `[5, 2]`, `[0, 16]`, `[0.5, 3]` ném.
   - `variants` (mọi ca dưới đây có `loopMode: "none"` để mục là v2; lưới 4×4 = 16 ô; `frames` là khung của một biến thể): `frames: 8, variants: 2` nhận, meta `frames === 8`, `variants === 2`; `frames: 4, variants: 4` nhận; `frames: 8, variants: 3` ném (24 > 16); `frames: 16, variants: 2` ném (32 > 16); `frames` vắng (= 16) với `variants: 2` ném, với `variants: 1` nhận; `variants: 0`, `1.5`, `"2"` ném; `frames: 8, variants: 2, frameRange: [0, 7]` nhận, `[0, 8]` ném (đoạn tính trong một biến thể, `b < frames = 8`).
   - Mục glint thật của Test 1 thêm `"loopMode": "none"`: nhận; `isFlipbookV2` đúng; `loop` sai; `frames === 16`, `variants === 8`; `Object.keys(meta)` = 12 khóa cũ theo thứ tự rồi đúng hai khóa `loopMode`, `variants` (thứ tự hai khóa này không kiểm); `playLife(meta, {}) = 16/24 = 0.666667` (không phải 2/24).
   - `controlA: "a.png"` với `base "/v/"` và `md5` 32 hex → `"/v/a.png?v=<md5>"`; `"../a.png"` ném; `controlB` thiếu `controlA` ném; mặt nạ trên `mode: "fire"` ném.
   - `timingProfile: "impact-key1"` có `controlA` nhận; thiếu `controlA` ném; `"nope"` ném.
   - `sourceFps: 24` lưu 24; `0`, `NaN`, `"24"`, `300` ném.
   - `anchor [0.25, 0.75]` → `pivot` và `anchor` = `[0.25, 0.75]`; `anchor [64, 192]` với `cell 256` → `[0.25, 0.75]`; `[300, 10]` với `cell 256` ném; manifest chỉ thêm `anchor` → `isFlipbookV2` sai.
3. **Cặp khung** (`lo = 2`, `count = 4`, trả `(f0, f1, w)`):
   - `none`: `3.25` → `(3, 4, 0.25)`, có `step` → `(3, 4, 0)`; `5.5` → `(5, 5, 0)`; `1` → `(2, 3, 0)`.
   - `stepped`: `5.5` → `(5, 5, 0)`; `6.25` → `(2, 2, 0)`; `1` → `(5, 5, 0)`.
   - `holderode`: `5.5` → `(5, 2, 0.5)` (bọc về đầu đoạn, không về 0); `3.75` → `(3, 4, 0.75)`; `1` → `(5, 2, 0)`.
   - `flipbookSwitch`: với `order` ∈ {0; 0,25; 0,5; 0,75; 1}: `(0, order) = 0`, `(1, order) = 1`; với `w` cách `mix(0.08, 0.92, order)` ≥ 0,08 kết quả chỉ là 0 hoặc 1; không giảm theo `w` (bước 0,01).
   - `fragmentShader` của pool v2 (mọi `loopMode`) không chứa `mod(f0 + 1.0, uFrames)`, chứa `FB_PICK_GLSL`, `FB_COMPOSE_GLSL`, `FB_MASKED_GLSL`; `vertexShader` chứa `attribute vec4 iCtl;`.
4. **Ghép.**
   - `composeLayers` so với ba phép "over" nối tiếp (ink, rồi thân, rồi lõi) trên lưới độ phủ {0; 0,25; 0,5; 0,75; 1}³ với ba bộ màu (`ci, cb, ch`): `(0.03, 0.022, 0.02), (0.88, 0.5, 0.2), (2.2, 2.1604, 1.9162)`; `(0.1, 0.1, 0.1), (0.8, 0.4, 0.2), (2, 1, 0.5)`; `(0, 0, 0), (0.88, 0.88, 0.88), (1, 1, 1)`: lệch ≤ 1e-9.
   - Mốc: `(0.25, 0.5, 0.1)` với bộ màu thứ hai → `(0.57125, 0.29125, 0.15125, 0.6625)`; `blendPremultiplied` lên đá sáng `#d6d0c2` (qua `srgbToLinear`: `0.672443, 0.630757, 0.539479`) → `(0.798200, 0.504131, 0.333324)`; lên đá tối `#2a2c30` → `(0.579064, 0.299751, 0.161225)`.
   - `composeFlipbookMasked`, nhìn mặc định; mẫu gốc `t0 = t1 = (0.9, 0.5, 0.2, 1)`, `m0 = m1 = (1, 0, 0, 1)`, `b = 0`, `w = 0`, `ctl = (1, −0.08, 0.08, 0)`, `tint = (1, 1, 1)`, `soft = 1`; mỗi dòng chỉ ghi chỗ khác mẫu gốc:
     - `m = (0, 0, 0, 1)` → `(0, 0, 0, 0)`;
     - mẫu gốc → `(0.88, 0.5, 0.2, 1)` (trần thân);
     - `t.a = 0`, `m = (1, 1, 0, 1)` → `(0.0165, 0.0121, 0.011, 0.55)` (ink);
     - `t = (0, 0, 0, 0)`, `m = (0, 0, 1, 1)` → `(2.2, 2.1604, 1.9162, 1)` (lõi HDR, không bị trần);
     - `b = 128/255`: `ctl.x = 0.25` → `(0, 0, 0, 0)`, `ctl.x = 0.5` → như mẫu gốc; `b = 64/255`, `ctl.x = 0.25` → như mẫu gốc; `b = 1`: `ctl.x = 0.75` → 0, `ctl.x = 1` → như mẫu gốc;
     - `ctl = (1, 0.819256, 0.08, 1)`: `m.a = 0.5` → `(0, 0, 0, 0)`; `m.a = 1` → `(0.88, 0.88, 0.871, 1)` (dải màu, trần);
     - `soft = 0.5` → `(0.44, 0.25, 0.1, 0.5)` (`soft` nhân một lần);
     - `t0 = (1, 0, 0, 1)`, `t1 = (0, 0, 1, 0)`, `w = 0.5` → `(0.44, 0, 0, 0.5)` (nội suy premultiplied, không ra tím);
     - `t.a = 0.2`, `sharpen (0.06, 0.4)` → `(0.324738, 0.18451, 0.073804, 0.369021)`; không sharpen → `(0.176, 0.1, 0.04, 0.2)`;
     - `t = (0.95, 0.9, 0.8, 1)`, `grade (0.9, 0.55, 0.12, 0.9)` → `(0.88, 0.5445, 0.1188, 1)`;
     - `t = (0, 0, 0, 0)`, `m = (0, 0, 1, 0.65)`: `ctl = (1, 0.5, 0.08, 1)` → `(1.503906, 1.476836, 1.309902, 0.683594)`; `ctl.w = 0` → `(2.2, 2.1604, 1.9162, 1)` (lõi chỉ tắt sớm khi dải màu đã vào);
     - `t.a = 0.5`, `m = (0.8, 0.5, 0.25, 1)` → `(0.883094, 0.729869, 0.556113, 0.728125)`.
   - `FB_COMPOSE_GLSL` chứa nguyên văn ba dòng `float alpha = 1.0 - (1.0 - ai) * (1.0 - ab) * (1.0 - ah);`, `vec3 rgb = ci * ai * (1.0 - ab) * (1.0 - ah) + cb * ab * (1.0 - ah) + ch * ah;`, `return vec4(rgb * soft, alpha * soft);`.
5. **Tick.** `flipbookTick`: `0` → 0, `1/60` → 1, `0.5` → 30, `42/60` → 42, `−0.1` → 0. Pool có mặt nạ, `timing: "impact-key1"`: lần `update` vẽ ở tuổi 0,5 s (sau 15 bước 1/30, 30 bước 1/60, 72 bước 1/144) ghi `iCtl.y = 0.918182` (tick 30) cả ba trường hợp.
6. **Hiện.** `revealThreshold(0..4)` = `0.25, 0.5, 0.75, 1, 1`; `revealThreshold(10) = 1`.
7. **Xói `impact-key1`.** `e(0..9) = −0.08`; `e(10) = 0.081405`, `e(12) = 0.358099`, `e(18) = 0.819256`, `e(20) = 0.85`, `e(31) = 0.925`, `e(42) = 1`, `e(60) = 1`; không giảm trên 0–60; `erodeEnd − holdEnd ≥ 3 · revealTicks`. `rampMixAt`: `9` → 0, `11` → 0.5, `13` → 1.
8. **Thân sáng.** 1000 mẫu `S = (k + 0.5)/1000`; mẫu gốc của Test 4 với `m = (1, 0, 0, S)`; `ctl` = `flipbookControl(tick/60, 43/60, 0, 0, t)`; `B(tick)` = tổng độ sáng `0.2126R + 0.7152G + 0.0722B` của đầu ra. `B(0..9) = 559.128 ± 0.01` (đỉnh, giữ đủ ở 4–9); `B(18) / max B ≤ 0.15` (Claude tính được 0,1269); `B(42) = 0`.
9. **Pool ghi `iCtl`.** Pool `rgba` sức chứa 2, meta có `controlA`, `controlB`, `timingProfile: "impact-key1"`, `attach(meta, new THREE.Texture(), { a: new THREE.Texture(), b: new THREE.Texture() })`:
   - spawn rồi `update(1/60)`: `iCtl[0..3] = (0.25, −0.08, 0.08, 0)`; lần `update` vẽ ở tick 12: `(1, 0.358099, 0.08, 0.75)`; `iData.w` (alpha) = 1 ở lần vẽ tick 42; đúng 43 lần vẽ (tick 0–42), lần `update` thứ 44 cho `live = 0` (Claude đã mô phỏng cộng dồn `Float32Array`).
   - spawn với `timing: undefined` trên meta có `controlA` mà không `timingProfile` → `(1, −0.08, 0.08, 0)`; `cool: 0.5, life: 1`, lần vẽ ở tuổi 0,75 → `(1, 0.46, 0.08, 1)`; `erode: 0.6` → `(1, 0.568, 0.08, 0)`.
   - Tái dùng slot: pool sức chứa 1, sprite có lịch chết rồi spawn sprite không lịch vào cùng slot → `(1, −0.08, 0.08, 0)`.
   - `timing: "impact-key1"` trên pool có meta cũ → không có thuộc tính `iCtl`, `life` bằng `playLife` cũ.
   - Lịch trên pool không có mặt nạ A: cùng meta (`controlA`, `controlB`, `timingProfile: "impact-key1"`), (i) pool `rgba` gọi `attach(meta, new THREE.Texture())` không kèm `controls`, (ii) pool `"fire"` gọi `attach(meta, tex, { a, b })`. Mỗi ca spawn không `life` rồi `update(1/60)` lặp: `playLife(meta, {}) = 43/60`; đúng 43 lần vẽ (tick 0–42); mọi lần vẽ `iCtl = (1, −0.08, 0.08, 0)`; `iData.w` ở lần vẽ tick 42 = `0.138889 ± 1e-4` (`fadeOut` mặc định `min(0.12, life · 0.3) = 0.12` vẫn áp, khác ca có mặt nạ ở trên là 1). Claude đã mô phỏng cộng dồn `Float32Array`.
10. **Biến thể** (`iVar` đọc ở lần `update` vẽ tuổi 0, tại chỉ số nén của sprite).
    - Lưới 4×4, `frames: 8` (khung của một biến thể), `variants: 2`, `loopMode: "none"`, pool `rgba` mới: `uRange = (0, 8)`; spawn `{ variant: 1 }` → `iVar = 8`, `iData.z = 0` ở tuổi 0; hai spawn không `variant` → `iVar` 0 rồi 8; sau `clear()` spawn không `variant` → 0; `variant: 5` → 8 (kẹp về 1).
    - Mục glint thật của Test 1 thêm `"loopMode": "none"` (lưới 16×8, `frames: 16`, `variants: 8`), pool `"fire"` mới sức chứa 4: `uRange = (0, 16)`; spawn `{ variant: 3 }` → `iVar = 48` (ô đầu hàng 3), `iData.z = 0`; tiếp hai spawn không `variant` → `iVar` 0 rồi 16 (hàng 0, hàng 1); `variant: 9` → 112 (kẹp về 7, ô đầu hàng 7).
11. **`attach` v2.** Meta `loopMode: "holderode"` không mặt nạ → `defines` đúng `{ FB_LOOP: 2 }`, `version === 1`, `iCtl.itemSize === 4`, `iVar.itemSize === 1`, geometry có 10 thuộc tính; `attach` lại cùng meta → `version` vẫn 1. Meta có mặt nạ trên pool `rgba` với `{ a, b }` → `{ FB_LOOP: 0, FB_CTRL_A: 1, FB_CTRL_B: 1 }`, `uCtlA.value === a`; chỉ `{ a }` → không có `FB_CTRL_B`; cùng meta trên pool `"fire"` → không có `FB_CTRL_*`. Sau đó `attach` meta cũ → hai hash về như Test 1, `defines` rỗng, không còn `iCtl`, `iVar`.
12. **Thư viện và player.** `player.pool("fx", "c", { mode: "rgba" })` rồi `player.library("fx").add(meta, tex, { a, b })` → pool có `FB_CTRL_A`, `FB_CTRL_B`; `library.reset()` gọi `dispose` của atlas, A và B, mỗi texture đúng một lần. Pool mới có `uInk`, `uHot`, `uBodyCap`, `uHotLead`, `uRamp0..2`, `uSoot`, `uSharpen`, `uGrade` bằng `FLIPBOOK_MASKED_LOOK`.

### 7. Chú thích và changelog
- Khối JSDoc đầu `flipbook.ts`: thêm các trường v2 của manifest (nói rõ `frames` là số khung của một biến thể và biến thể v bắt đầu ở ô v·frames), hai đường shader, ba `loopMode`, hai ngoại lệ tương thích (`loop: true` cũ hòa chéo bọc vòng; `variants` ở mục không phải v2 bị bỏ qua), và mặt nạ A/B. Không sửa dòng `// Source: …`.
- Changelog `docs/changelog/2026-11-04-flipbook-v2.md` (tiếng Việt): làm gì, trường manifest mới, API mới, test, và "chưa nối vào kit hay lab (CX-G, CX-H); kiểm GPU do Claude chạy".

## Kiểm bắt buộc (trong `games/.wt-immortality-cultivation-codex`; ghi lệnh và kết quả vào báo cáo)
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua; trước **793 test, 84 tệp** (mốc `bc94110`), sau = 793 + số test của `flipbook-v2.test.ts`, 85 tệp; `tests/view/element-layer.test.ts` qua mà không sửa.
3. Xóa `/private/tmp/codex-258-dist` nếu còn, rồi `IC_VITE_CACHE_DIR=/private/tmp/codex-258-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-258-dist --configLoader runner`: thoát 0. `--configLoader runner` và `IC_VITE_CACHE_DIR` là bắt buộc: Vite 7.3.7 mặc định nạp cấu hình kiểu `bundle`, ghi tệp tạm vào `node_modules/.vite-temp/`, mà `node_modules` của worktree là symlink sang game (báo cáo 255 dòng 57, 64). Sau đó `grep -rl "fbComposeMasked\|uSharpen" /private/tmp/codex-258-dist` **không in đường dẫn nào** (thoát 1 là đúng): bản dựng chỉ gồm `index.html`, `bench.html`, `tinh-tu.html`, và `flipbook.ts` chỉ tới được từ lab (`src/lab/skills-main.ts`), nên phiếu này không được kéo flipbook vào bản dựng. Hai chuỗi grep là chữ trong shader nên không bị minify đổi tên. Shader v2 được chứng minh bằng Test 3, Test 11 và phần "Claude kiểm sau", không qua bản dựng. Cuối cùng xóa `/private/tmp/codex-258-dist`.
4. `git -C games/.wt-immortality-cultivation-codex diff --stat` và `status --short`: chỉ các file được ghi (cộng symlink `node_modules` có sẵn).

## Claude kiểm sau (trình duyệt, không phải việc của Codex)
1. **Biên dịch:** trong lab, `attach` meta tổng hợp cho `FB_LOOP` 0/1/2 × {không mặt nạ, A, A+B} ở `rgba` và `FB_LOOP` 0/1/2 không mặt nạ ở `fire`, `smoke`, `heat`: 18 pool, 9 chương trình khác nhau (bản không mặt nạ dùng chung chương trình giữa bốn chế độ vì `uMode` là uniform: three r170 `getProgramCacheKey`, dòng 20978–21016, ghép `customVertexShaderID`, `customFragmentShaderID`, `defines` và cờ vật liệu, mà mọi pool cùng chữ shader, cùng `defines` theo `FB_LOOP` và cùng cờ). Đo: số `renderer.properties.get(pool.mesh.material).currentProgram` khác nhau trên 18 pool = 9, và `renderer.info.programs.length` tăng đúng 9 so với trước khi vẽ 18 pool; không lỗi biên dịch, không lỗi GL, mỗi pool một lệnh vẽ.
2. **Atlas cũ y nguyên từng điểm ảnh:** chụp các clip của `fire` và `aura` trước và sau, chênh 0 (kể cả ba clip glint mang `"variants": 8`, vẫn ở đường cũ theo §0).
3. **GPU so CPU ±1/255:** camera trực giao, một instance, atlas tổng hợp `SRGBColorSpace` và mặt nạ `NoColorSpace` với mỗi ô một màu phẳng (cùng `flipY`); vẽ vào `WebGLRenderTarget` `HalfFloatType`; lượt 1 tắt trộn (đọc RGBA premultiplied của nguồn), lượt 2 trộn như pool lên nền đá sáng và đá tối đã xóa bằng màu tuyến tính (đọc RGB); `readRenderTargetPixels` vào `Uint16Array`, đổi bằng `THREE.DataUtils.fromHalfFloat`; so với `composeFlipbookMasked` và `blendPremultiplied` (mẫu atlas = `srgbToLinear(byte/255)`, mặt nạ = `byte/255`) cho các ca của Test 4 và tick 0, 1, 3, 9, 12, 18, 20, 42 của `impact-key1`. Không so ảnh chụp đã qua bloom hay tone mapping.
4. **Mặt nạ không bị premultiply khi giải mã:** PNG RGB (200, 100, 50), A = 1, 3, 8 /255, nạp đúng thiết lập ở mục 2; vẽ texel ra target float, so `byte/255` ±1/255. Nếu trượt: phiếu sau đổi cách nạp mặt nạ sang `ImageBitmapLoader` (`premultiplyAlpha: "none"`, `colorSpaceConversion: "none"`, `imageOrientation: "flipY"`); CX-B không đổi.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Thay đổi trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–4, làm phần "Claude kiểm sau", rồi mới commit và gộp.
- Báo cáo ghi: từng mục 1–7 đã làm ở hàm nào; chỗ phải làm khác và vì sao; kết quả Kiểm 1–4 (số test trước và sau).

## Phản biện
Lượt phản biện Claude (04/11) nêu hai lỗi ở Kiểm 3; Claude kiểm cả hai ở mã, cả hai đúng, đã sửa Kiểm 3. Không bác lỗi nào.

| Lỗi | Claude kiểm | Xử lý |
|---|---|---|
| Đòi grep `fbComposeMasked` ra trong bản dựng là không thể đạt | `vite.config.ts` chỉ dựng `index.html`, `bench.html`, `tinh-tu.html` (skills-lab.html không dựng); duyệt import (bỏ `import type`) từ `src/main.ts`, `src/view/bench/main.ts`, `src/tinh-tu/main.ts` tới 162 module, không module nào ở `src/view/skills/` hay `src/lab/`; người nhập `flipbook.ts` chỉ là `skills-main.ts`, `element-fire.ts`, `element-stage.ts`; `dist/` lúc 09:52 không có `uSharpen`, `vxSoftGround`, `vxCell` | Đổi thành kiểm phủ định như phiếu 255: grep `fbComposeMasked\|uSharpen` không ra gì. Không grep tên lớp (`FlipbookPool`) vì minify đổi tên |
| Lệnh build ghi vào game qua symlink `node_modules` | Vite 7.3.7, `config.js` dòng 36005 (`configLoader = "bundle"` mặc định), 36158–36164 (ghi `node_modules/.vite-temp/`); báo cáo 255 dòng 57, 64 đã thêm cờ | Thêm `--configLoader runner` và `IC_VITE_CACHE_DIR` trong thư mục dựng tạm, như lệnh 255 đã chạy |

Lượt phản biện Claude thứ hai (04/11) nêu hai lỗi; Claude kiểm cả hai ở mã của `bc94110` và ở three r170, cả hai đúng, đã sửa. Không bác lỗi nào.

| Lỗi | Claude kiểm | Xử lý |
|---|---|---|
| "Claude kiểm sau" mục 1 ghi 15 chương trình; đúng là 18 pool, 9 chương trình | `flipbook.ts` dòng 270, 548: `uMode` là uniform; dòng 542–577: mọi pool cùng cờ vật liệu (`transparent`, `depthWrite: false`, `DoubleSide`, `toneMapped: false`, cùng trộn), không `onBeforeCompile`, không `customProgramCacheKey`; three r170 dòng 20978–21016: khóa = `customVertexShaderID`, `customFragmentShaderID`, `defines`, tham số và cờ vật liệu, `outputColorSpace`, không có uniform. Rgba: 3 × 3 = 9 pool; `fire`, `smoke`, `heat` không mặt nạ: 9 pool; chương trình: 3 không mặt nạ (dùng chung bốn chế độ) + 3 chỉ A + 3 A+B = 9 | Sửa mục 1: 18 pool, 9 chương trình khác nhau, lý do `uMode` là uniform; đo bằng số `currentProgram` khác nhau = 9 và `renderer.info.programs.length` tăng 9 |
| JSDoc `FlipOptions.timing` (§4) nói lịch "nơi khác bị bỏ qua", trái với `playLife` (§1) đặt `life` theo lịch trên cả pool không có mặt nạ A | `playLife` là hàm module export (dòng 480), chỉ nhận `(meta, o)`, được `tests/view/element-layer.test.ts` dòng 785, 796 gọi thẳng; `flipbookTimingOf` chỉ xét `meta.controlA`; `spawn` đặt `timing = this.masked ? … : null`. Vậy trên pool `fire` hay `rgba` không `controls.a`, đời = 43/60 s, `fadeOut` cũ 0,12, không hiện/xói: lịch không bị "bỏ qua" | Chọn cách (a): giữ mã như phiếu (đời là thuộc tính của clip, `playLife` bằng đời `spawn` dùng, không cần biết pool). Sửa JSDoc `FlipOptions.timing`; ghi rõ ở §1 `playLife`, §4 `flipbookTimingOf` và `spawn`; thêm ca vào Test 9 (pool `rgba` không `controls`, pool `fire` có `{ a, b }`: 43 lần vẽ, `iCtl = (1, −0.08, 0.08, 0)`, `iData.w` tick 42 = 0,138889) |

Lượt phản biện Claude thứ ba (04/11) nêu một lỗi: nghĩa mới của `variants` đụng ba manifest đang dùng trường này. Claude kiểm ở `art-src/lab/vfx/fire/manifest.json`, `art-src/lab/vfx/aura/manifest.json`, json đi kèm và `flipbook.ts` của `bc94110`: đúng, đã sửa. Không bác phần nào; chỉ chọn một trong hai cách critic đưa cho (b) và làm chặt thêm một chỗ (ghi ở cột cuối).

| Lỗi | Claude kiểm | Xử lý |
|---|---|---|
| `variants` của phiếu (`F = frames / variants`, biến thể v ở ô `v·F`) trái nghĩa với ba mục hiện có (`frames` = khung của một biến thể, mỗi biến thể một hàng); parser mới sẽ nhận chúng thành 8 biến thể × 2 khung trong hàng 0, sang v2 (14 khóa), `playLife` 16/24 → 2/24 s, `variantTurn` ra ô 0, 2, 4…; trái §1 (12 khóa), kế hoạch §2.2, nhận CX-B và "Claude kiểm sau" mục 2; Codex không thấy được vì `art-src` không có trong worktree | Ba mục `fire-twinkle-set`, `glint-gold-twinkle-set`, `glint-starburst-set`: `cols 16, rows 8, frames 16, variants 8`, `order` "one element per row (variant), its frames left to right", json đi kèm `playback` "one-shot per row (pick a row at random)", `atlas [2048, 1024]`. Không mục nào khác trong `art-src/lab/vfx/*/manifest.json` mang trường mới. `bc94110`: parser bỏ qua `variants` (dòng 84–118), `playLife` dùng `meta.frames` (dòng 485), không mã nào trong `src/` nhắc ba id này. Tính lại theo phiếu cũ: `16 % 8 = 0`, `F = 2`, v2 với `loopMode: "none"`, 14 khóa, `playLife = 2/24`: đúng như critic nói | (a) Lấy nghĩa của tệp: `frames` là số khung của một biến thể, biến thể v ở ô `v·frames … v·frames + frames − 1`, kiểm `variants · frames ≤ cols · rows`; `frameEnd`, kiểm `frameRange` (`b < frames`), `uRange` trong `attach` và `varCell` đều dùng `frames` (§1, §4, JSDoc `FlipOptions.variant`, §7). (b) `variants` không còn là trường kích hoạt v2 và chỉ có hiệu lực ở mục v2; ở mục không phải v2 parser bỏ qua hoàn toàn, không kiểm, không đặt khóa (làm chặt hơn đề xuất: nếu kiểm ở cả mục cũ thì một giá trị sai trong tệp cũ sẽ làm hỏng cả manifest, hôm nay vẫn nạp được); `spawn` chỉ đọc `variants` khi `v2Key !== null`. Ba mục glint ở lại đường cũ (12 khóa, hàng 0, 16/24 s); bật biến thể cho chúng là việc của CX-D/CX-G bằng `"loopMode": "none"` (§0). (c) Test 1 thêm mục `fire-twinkle-set` thật (khóa, `url`, `playLife`, `attach`, giá trị `variants` sai bị bỏ qua); Test 2 tính lại (`frames: 8, variants: 2` trên lưới 4×4; 3, 0, 1,5, `"2"`, `frames: 16` hay vắng với `variants: 2` ném; `frameRange [0, 7]` nhận, `[0, 8]` ném; mục thật thêm `loopMode` ra 14 khóa và 16/24 s); Test 10 tính lại (`frames: 8`, `iVar` 8; mục thật `iVar` 48, 0, 16, 112); "Claude kiểm sau" mục 2 nêu ba clip glint |
