# CX-B `FlipbookPool` bản 2: hồ sơ ChatGPT (04/11/2026)

- Phiếu: `docs/codex-queue/258-tt-flipbook-v2.md`. Chat: https://chatgpt.com/c/6aead1a6-ca44-83ec-ba92-891611be57cb (Chat mode, thinking High).
- Brief gửi 13:33; trả lời đầy đủ xong 13:47; tự duyệt lần 1 gửi 13:47.
- **Đếm lượt duyệt:** lượt 1: FAIL (8+ lỗi, đang viết bản sửa đầy đủ lúc lưu 13:51); chưa có hai PASS liền nhau. Văn bản dưới dừng giữa lượt 1.
- Phần dưới là văn bản trang lấy bằng JavaScript (`main.innerText`), nguyên văn, gồm brief, câu trả lời, lời nhắc duyệt và phán quyết. Dòng "Thought for…", tóm tắt suy nghĩ và chữ giao diện cũng nằm trong đó.

## Bảng kiểm (Claude)

| Khẳng định | Nguồn | Trạng thái | Ghi chú |
|---|---|---|---|
| Manifest cũ `loop: true` đang hòa chéo bọc vòng; bỏ nó đổi điểm ảnh của manifest cũ, nên giữ đường cũ cho manifest không có trường v2 | `src/view/skills/flipbook.ts`, fragment (`f1 = uLoop>0.5 ? mod(f0+1,uFrames)`) | đã kiểm | Claude nhận |
| Có trường v2 mà thiếu `loopMode`: `loop: true` → `stepped`, `false` → `none` | quy ước đề xuất | Claude nhận | đường v2 không còn hòa chéo bọc vòng |
| Tick = `Math.floor(ageSeconds * 60 + 1e-6)` | quy ước | Claude nhận | trùng lời giải sơ bộ của Claude |
| three r170: `NoColorSpace` → `UNPACK_COLORSPACE_CONVERSION_WEBGL = NONE`; `UNPACK_PREMULTIPLY_ALPHA_WEBGL` theo `texture.premultiplyAlpha` | `node_modules/three/build/three.module.js` dòng ~25020–25025 | đã kiểm | |
| `Texture.flipY` và `premultiplyAlpha` không tác dụng với `ImageBitmap`; phải đặt khi tạo bitmap | tài liệu three.js `Texture` | chưa kiểm tại nguồn trong phiên này | thư viện hiện dùng `TextureLoader` (ảnh thường), nên không đổi loader |
| Không chuyển màu đầu ra trước khi trộn premultiplied trong target HDR tuyến tính | ColorManagement của three.js | chưa kiểm tại nguồn trong phiên này | kế hoạch §2.3 đã ghi `EffectComposer` r170 dùng HalfFloat |

## Văn bản chat

````text
Share
You said:
Role: you are the analyst for a game project. Research, analyse and propose a concrete, exact code solution that a coding agent (Codex, no browser, no network, no GPU) will implement as written.

Goal: package CX-B "FlipbookPool v2" for the browser game "Tu Tien Thu Ai" (TypeScript, three.js 0.170.0, WebGL2, ShaderMaterial). Extend the existing sprite-flipbook system in src/view/skills/flipbook.ts so that: (1) a clip has loopMode "none" | "stepped" | "holderode", and NO mode ever crossfades the last frame into the first (wrap-around crossfade ghosts); (2) manifests stay backward compatible: an old manifest with none of the new fields renders pixel-identical to today; (3) a clip may carry two control masks A and B; (4) the RGBA mode can compose ink, body and hot core with the contract formula below, matching a CPU reference within +-1/255; (5) reveal and erode thresholds are driven per 60 Hz tick from the masks (fast attack, slow decay).

Facts (current code, verified by me):
- parseFlipbookManifest(value: unknown, base: string): Map<string, FlipbookMeta>. Accepts version undefined or 1, "flipbooks" or "clips" (object or array with id), "file" or "atlas", "grid":[c,r] or cols/rows. Unknown fields are ignored; a bad entry throws. FlipbookMeta = { id, url, cols, rows, frames, fps, loop: boolean, mode: "rgba"|"fire"|"smoke"|"heat", aspect, pivot, start, heading }. Real manifests (art-src/lab/vfx/<element>/manifest.json) carry many extra fields (blend, alphaKind, json, modesAllowed, md5...) and 9 clips have "loop": true (aura sheaths/ribbons, fire-trail, dragonhold clips).
- FlipbookLibrary loads atlases with texture.premultiplyAlpha = false (straight alpha stored; the shader premultiplies once).
- class FlipbookPool(id, mode, capacity, renderOrder, blankTexture): one InstancedBufferGeometry + one ShaderMaterial per clip, one draw call. Blending CustomBlending, AddEquation, src ONE, dst ONE_MINUS_SRC_ALPHA, srcAlpha ZERO, dstAlpha ONE; toneMapped false; depthWrite false. Instance attributes: iPos(3), iData(4: size, angle, frame, alpha), iColor(4: tint rgb, ground), iDir(4: dir xyz, occlude), iAge(4: x = age/life, y = cool start fraction, z = seed, w = erode), iLift(2). CPU state Float32Array stride 35. update(dt) advances age; frame = frameAt(first, fps, slowFrom, slowFps, age) (a two-rate time map). attach(meta, texture) sets uMap, uGrid, uFrames, uLoop = meta.loop?1:0, uPivot, uAspect, uHeading. Setters/methods: stepped (uStep), setSharpen(lo,hi), setSoot, setHeatRamp, setGrade, blur, taper, vignette, softM, spawn(at, size, FlipOptions), clipS, clear, dispose. Exported helpers: frameAt, playLife, ONE_FRAME, MODE_INDEX.
- Fragment today: f = uLoop>0.5 ? mod(vFrame,uFrames) : clamp(vFrame,0,uFrames-1); f0 = floor(f); f1 = uLoop>0.5 ? mod(f0+1,uFrames) : min(f0+1,uFrames-1); w = uStep>0.5 ? 0 : f-f0. So a loop crossfades frame N-1 into frame 0 (the ghost). Mode "rgba": pm = mix(t0.rgb*t0.a, t1.rgb*t1.a, w), a = mix(t0.a,t1.a,w); optional sharpen (per-pixel noise-staggered switch between frames); optional grade; erode-in by vAge.w (threshold on a + noise); burn from vAge.y (threshold rising through a + noise, rgb toward uSoot*0.85). Output gl_FragColor = vec4(pm*vTint*soft, a*soft). The thresholds today use colour coverage + value noise, not an authored field. Other modes: "fire" (rgb on black, added), "smoke", "heat".
- Users: src/view/skills/element-fire.ts (spawn, setSharpen, stepped, setSoot...). tests/view/element-layer.test.ts tests parseFlipbookManifest, frameAt, playLife, pool spawn. vitest 3.2 with environment "node" (no WebGL, no DOM canvas). Typecheck: tsc --noEmit.

Contract (owner-approved plan, do not reopen):
- Manifest gains optional fields, backward compatible: rows/variants, frameRange, controlA, controlB, anchor, sourceFps, loopMode, timingProfile. A file without them runs exactly as before.
- Control mask A (RGBA, data, NoColorSpace, same grid as the atlas): R = hull (max coverage, hand painted), G = ink, B = hot line, A = survival order (thin tips and loose bits low, roots high).
- Control mask B (half resolution, data): R = reveal order (0 at the slash root, 1 at the tip, secondary strokes 0.35-0.85), G = motion influence.
- Shader contract, ink/body/core in one fragment, coverages a_i, a_b, a_h, linear colours C_i, C_b, C_h (C_h HDR, only on hot lines):
  alpha = 1 - (1-a_i)(1-a_b)(1-a_h)
  RGB = C_i*a_i*(1-a_b)(1-a_h) + C_b*a_b*(1-a_h) + C_h*a_h
  blend ONE, ONE_MINUS_SRC_ALPHA (premultiplied, no second alpha multiply). Caps: body <= 0.85-0.9 per channel; core <= 5% of the bright area; ink alpha Metal 0.35, Fire 0.45-0.7, broken 20-35%. Check: sample cells (none, partial, full coverage) on light and dark stone, GPU vs CPU, error <= 1/255.
- Frame loops: a segment is chosen offline with R_seam <= 1.2; play "stepped" or "hold and erode", never a wrap-around crossfade; else play once.
- Fast attack: body revealed by mask B.R with threshold T(tick) = clamp((tick+1)/4, 0, 1) at 60 Hz (tick 0: 25% from the root, inside the flash; 1: 50%; 2: 75% and secondary strokes; 3: full). A revealed stroke is already at full colour and brightness, never fading in.
- Slow decay: a pixel lives while smoothstep(e(t), e(t)+w, A) with A = mask A.A, w = 0.06-0.12 (trial). The surviving part is recoloured by a stepped ramp r = clamp((A-e)/(1-e)): white-gold -> orange -> crimson -> soot; never a uniform fade of the card. This extends the pool's existing cool/erode. Key-1 impact timeline (60 Hz ticks, trial): 0 flash + root; 1-3 body reveals; 4-9 hold; 10-20 tips and secondary strokes tear first, big bright parts nearly gone; 20-42 only embers and sparse gold dust. At tick 18 the bright body is <= 15% of its peak. Decay lasts at least 3x the reveal.

Constraints: only src/view/skills/flipbook.ts and a new tests/view/flipbook-v2.test.ts change in this package (wiring into the lab and element kits is a later package); every existing export, method and FlipOptions field keeps its meaning; no per-frame allocation; one draw call per pool; at most 16 vertex attributes; masks are separate textures (NoColorSpace, no premultiply, same flipY as the atlas); old pools should compile the old path (for example via defines) so they stay pixel-identical; tests run in node without WebGL, so the GPU-vs-CPU check needs a design that tsc/vitest can enforce now plus a small browser probe that the coordinator runs later.

Deliver, in Vietnamese, keeping every code name, field and GLSL as is: 1) analysis of the problem and its causes; 2) the solution as ordered steps with the reason for each: exact TypeScript types and manifest field validation (names, types, defaults, how loopMode relates to the old loop boolean), the exact frame-index logic per loopMode, how a_i, a_b, a_h, C_i, C_b, C_h are derived from the atlas and mask A, the exact GLSL and the matching CPU reference function (names, signatures), how tick is computed from age (frame-rate independent, deterministic), how e(t) and T(tick) are scheduled (new FlipOptions fields or a timingProfile), where new per-instance data goes, and the exact vitest cases with numeric expectations; 3) risks and how to check each; 4) what you are not sure about. Cite a source for every factual claim about three.js or WebGL. Do not ask clarifying questions in a separate turn: state any assumption inside the answer and proceed.
…
Show more
Worked for 11m 51s
Analyzed
Analyzed
ChatGPT said:
CX-B — FlipbookPool v2
Phân tích kỹ thuật và đặc tả triển khai cho Codex

Phạm vi: src/view/skills/flipbook.ts và tests/view/flipbook-v2.test.ts.

Nền tảng: TypeScript, three.js 0.170.0, WebGL2, ShaderMaterial, Vitest 3.2.

Mục tiêu: bổ sung điều khiển frame, hai control mask, compositing RGBA và reveal/erosion 60 Hz mà không thay đổi hình ảnh của manifest cũ.

1. Phân tích nguyên nhân và các quyết định nền tảng
1.1. Wrap-around ghosting

Shader hiện tại tính:

glsl
float f = uLoop > 0.5
  ? mod(vFrame, uFrames)
  : clamp(vFrame, 0.0, uFrames - 1.0);

float f0 = floor(f);
float f1 = uLoop > 0.5
  ? mod(f0 + 1.0, uFrames)
  : min(f0 + 1.0, uFrames - 1.0);

float w = uStep > 0.5 ? 0.0 : f - f0;

Khi f0 = N - 1, f1 = 0, w > 0, hai pose không liền nhau bị trộn thành một ảnh. Đây là nguyên nhân trực tiếp của wrap-around ghosting.

Quyết định: stepped không nội suy frame; none chỉ được nội suy giữa hai frame kề nhau trong đoạn hợp lệ; holderode phát các frame rời rạc rồi giữ frame cuối để erosion.

1.2. Có một mâu thuẫn bắt buộc phải xử lý

Hai yêu cầu sau không thể đồng thời đúng theo nghĩa tuyệt đối:

Manifest cũ phải pixel-identical.

Không chế độ nào được crossfade frame cuối sang frame đầu.

Một manifest cũ có loop: true, uStep = 0 đang thực hiện wrap-around crossfade. Xóa hành vi đó sẽ làm thay đổi pixel của chính manifest cũ.

Giải pháp tương thích được chốt:

Legacy path: manifest không chứa trường mới giữ nguyên toàn bộ hành vi cũ, kể cả wrap-around crossfade đã tồn tại.

V2 path: mọi loopMode tường minh đều cấm wrap-around crossfade.

Không âm thầm sửa asset cũ trong CX-B. Một lần chuyển đổi manifest sang V2 sau này sẽ giải quyết ghosting cho asset đó.

Đây là ngoại lệ tương thích, không phải thêm một giá trị loopMode thứ tư.

1.3. Premultiplied alpha và công thức compositing

Contract hiện tại đã xác định đúng phép hợp nhất ba lớp:

𝛼
=
1
−
(
1
−
𝑎
𝑖
)
(
1
−
𝑎
𝑏
)
(
1
−
𝑎
ℎ
)
α=1−(1−a
i
	​

)(1−a
b
	​

)(1−a
h
	​

)
𝑅
𝐺
𝐵
=
𝐶
𝑖
𝑎
𝑖
(
1
−
𝑎
𝑏
)
(
1
−
𝑎
ℎ
)
+
𝐶
𝑏
𝑎
𝑏
(
1
−
𝑎
ℎ
)
+
𝐶
ℎ
𝑎
ℎ
RGB=C
i
	​

a
i
	​

(1−a
b
	​

)(1−a
h
	​

)+C
b
	​

a
b
	​

(1−a
h
	​

)+C
h
	​

a
h
	​


Điểm quan trọng là RGB đã premultiplied. Không được tiếp tục nhân RGB với alpha.

Với blending ONE, ONE_MINUS_SRC_ALPHA, màu đích được tính:

𝑅
𝐺
𝐵
𝑜
𝑢
𝑡
=
𝑅
𝐺
𝐵
𝑠
𝑟
𝑐
+
𝑅
𝐺
𝐵
𝑑
𝑠
𝑡
(
1
−
𝛼
𝑠
𝑟
𝑐
)
RGB
out
	​

=RGB
src
	​

+RGB
dst
	​

(1−α
src
	​

)

Đây là phép tính tương ứng với blending factors được định nghĩa trong WebGL. 
MDN
+1

Một lưu ý khác: trạng thái alpha hiện tại (srcAlpha ZERO, dstAlpha ONE) giữ nguyên alpha của destination. Vì vậy, phép kiểm tra phải so sánh RGB compositing với background và kiểm tra alpha của shader riêng; không được giả định đọc alpha của framebuffer đã blend sẽ trả về alpha của sprite.

1.4. Tách đường shader cũ và mới tại compile time

Dùng ShaderMaterial.defines, không dùng if (uV2 > 0.5) cho mọi fragment.

TypeScript
material.defines = v2Enabled
  ? { FLIPBOOK_V2: 1 }
  : {};

three.js hỗ trợ đưa các định nghĩa này vào source shader khi compile. 
Three.js Docs

Bắt buộc:

Giữ nguyên biểu thức, thứ tự thao tác và texture settings ở legacy path.

Không chuyển đổi color space của texture cũ.

Không thay đổi thời điểm cập nhật frame, age, alpha trong legacy path.

Chỉ V2 mới sử dụng control masks và các tham số bổ sung.

Không cần thêm draw call: mỗi pool vẫn dùng một geometry, một material và một draw call cho các instance của clip đó.

1.5. Nguyên nhân của erosion thiếu kiểm soát

Erosion hiện tại dựa vào:

Plain text
atlas alpha + procedural noise

Điều này khiến shader không phân biệt được phần nào là đầu nét, phần nào là chân nét, hoặc phần nào phải tồn tại lâu hơn.

V2 phải chuyển sang dữ liệu được tác giả kiểm soát:

controlB.R: thứ tự xuất hiện của nét.

controlA.A: thứ tự biến mất.

controlA.G: vùng ink.

controlA.B: vùng hot core.

controlA.R: coverage hull.

Shader chỉ giải mã và hiển thị dữ liệu đó, không tự tạo hình học procedural thay thế.

2. Giải pháp triển khai theo thứ tự
Bước 1 — Mở rộng FlipbookMeta và định dạng manifest

Giữ nguyên toàn bộ trường hiện tại. Chỉ bổ sung các trường optional sau:

TypeScript

export type FlipbookLoopMode =
  | "none"
  | "stepped"
  | "holderode";

export type FlipbookTimingProfile =
  | "off"
  | "key1-impact-60";

export type FlipbookFrameRange =
  readonly [first: number, last: number];

export interface FlipbookVariant {
  row: number;
  frameRange?: FlipbookFrameRange;
}

// Append to the existing FlipbookMeta interface.
// Do not remove or change existing fields.
export interface FlipbookV2Fields {
  variants?: Record<string, FlipbookVariant>;
  frameRange?: FlipbookFrameRange;
  controlA?: string;
  controlB?: string;
  anchor?: readonly [number, number];
  sourceFps?: number;
  loopMode?: FlipbookLoopMode;
  timingProfile?: FlipbookTimingProfile;
}


FlipbookMeta phải tiếp tục chứa tất cả các trường cũ và bổ sung những trường của FlipbookV2Fields. Không thay loop: boolean thành kiểu mới.

Quy tắc định dạng

Trường

	

Quy tắc




rows

	

Vẫn là số hàng atlas kiểu cũ, không đổi ý nghĩa




variants

	

Object có key là variant ID, value là { row, frameRange? }




frameRange

	

[first,last], 0-based, inclusive




controlA

	

URL string của mask A




controlB

	

URL string của mask B




anchor

	

[x,y], normalized từ 0 đến 1




sourceFps

	

FPS nguồn, số hữu hạn lớn hơn 0 và không quá 240




loopMode

	

Một trong ba giá trị được duyệt




timingProfile

	

"off" hoặc "key1-impact-60"

frameRange ở clip là chỉ số frame tuyệt đối trong atlas. Riêng variants[id].frameRange là khoảng cột tương đối trong hàng được chọn.

Ví dụ:

JSON
{
  "file": "fire-impact.webp",
  "grid": [8, 4],
  "frames": 32,
  "fps": 12,
  "loop": false,
  "mode": "rgba",
  "frameRange": [0, 7],
  "variants": {
    "slash-a": {
      "row": 0,
      "frameRange": [0, 7]
    },
    "slash-b": {
      "row": 1,
      "frameRange": [1, 6]
    },
    "slash-c": {
      "row": 2,
      "frameRange": [0, 7]
    }
  },
  "controlA": "fire-impact-control-a.png",
  "controlB": "fire-impact-control-b.png",
  "sourceFps": 12,
  "loopMode": "holderode",
  "timingProfile": "key1-impact-60",
  "anchor": [0.5, 0.5]
}

Giả sử variant = "slash-b", khoảng frame cuối cùng là [9,14].

Nếu không chọn variant, dùng frameRange cấp clip, hoặc [0, frames - 1] nếu không khai báo.

Validation trong parseFlipbookManifest

Không thay cơ chế chấp nhận manifest version undefined hoặc 1, cấu trúc flipbooks/clips, file/atlas và grid/cols/rows.

Sau validation cũ, thực hiện:

Kiểm tra chính xác kiểu của từng trường mới, nếu có.

frameRange: hai số nguyên, 0 <= first <= last < frames.

variants: object không phải array; ID không rỗng; row nguyên trong [0,rows-1]; các cột trong [0,cols-1]; frame tuyệt đối cuối cùng phải nhỏ hơn frames.

controlA và controlB: string khác rỗng, resolve URL với base bằng cùng quy tắc mà file đang dùng.

Hai control masks phải cùng xuất hiện nếu muốn bật compositing bằng mask. Trường hợp chỉ có một mask phải báo lỗi; không tự tạo mask giả.

Chỉ chấp nhận control masks trên clip có mode === "rgba".

anchor: đúng hai số hữu hạn trong [0,1].

sourceFps: số hữu hạn thuộc (0,240].

loopMode, timingProfile: reject mọi giá trị ngoài union được duyệt.

timingProfile === "key1-impact-60" yêu cầu cả hai control masks.

Các unknown fields khác vẫn bị bỏ qua như parser hiện tại.

Quan trọng: không thêm các property với giá trị undefined vào kết quả parse của manifest cũ nếu parser hiện tại không tạo chúng. Điều này giữ nguyên cả hình dạng object cho các test cũ.

Xác định Legacy và V2
TypeScript
const V2_FIELD_NAMES = [
  "variants",
  "frameRange",
  "controlA",
  "controlB",
  "anchor",
  "sourceFps",
  "loopMode",
  "timingProfile"
] as const;

export function hasFlipbookV2Fields(
  value: object
): boolean {
  return V2_FIELD_NAMES.some(
    key => Object.prototype.hasOwnProperty.call(
      value,
      key
    )
  );
}

export function effectiveLoopMode(
  meta: FlipbookMeta
): FlipbookLoopMode {
  return meta.loopMode ??
    (meta.loop ? "stepped" : "none");
}

hasFlipbookV2Fields chỉ dùng khi chuẩn bị pool, không gọi mỗi frame. rows không được dùng để phát hiện V2 vì đây vốn là trường legacy.

Nếu manifest cũ không có trường mới, dùng nguyên legacy shader. Nếu có trường mới nhưng thiếu loopMode, quy ước V2 là loop: true → stepped, loop: false → none.

loopMode tường minh luôn ưu tiên hơn loop; bản thân loop không được sửa.

Bước 2 — Chốt ngữ nghĩa frame cho ba loopMode

Mode

	

Tiến frame

	

Kết thúc đoạn

	

Nội suy




none

	

Một lần từ first đến last

	

Clamp tại last, instance vẫn theo lifetime hiện có

	

Chỉ giữa frame kề nhau, không wrap




stepped

	

Loop [first,last]

	

Quay về first sau frame cuối

	

Không nội suy




holderode

	

Một lần từ first đến last

	

Giữ nguyên last, để timing profile xóa nét

	

Không nội suy

none không tự xóa instance khi đến frame cuối; lifetime vẫn theo cơ chế cũ. holderode khác none ở chính sách giữ frame và mặc định timing profile.

Hàm tính frame V2, export để test:

TypeScript

export function v2FrameAt(
  rawFrame: number,
  first: number,
  last: number,
  loopMode: FlipbookLoopMode
): number {
  const count = last - first + 1;
  const local = Math.max(0, rawFrame - first);

  if (loopMode === "stepped") {
    const whole = Math.floor(local);
    return first + (
      ((whole % count) + count) % count
    );
  }

  if (loopMode === "holderode") {
    return first + Math.min(
      count - 1,
      Math.floor(local)
    );
  }

  return first + Math.min(
    count - 1,
    local
  );
}


rawFrame phải là kết quả của bộ ánh xạ thời gian hai tốc độ hiện tại:

TypeScript
const rawFrame = frameAt(
  first,
  meta.sourceFps ?? meta.fps,
  slowFrom,
  slowFps,
  ageSeconds
);

const frame = v2FrameAt(
  rawFrame,
  first,
  last,
  effectiveLoopMode(meta)
);

Đây là điểm nối đề xuất: giữ nguyên công thức frameAt, chỉ đưa kết quả qua v2FrameAt. Nếu tên first trong implementation thực tế không phải offset frame, Codex phải giữ biểu thức gọi frameAt cũ và chuyển sang hệ local-frame trước khi áp dụng v2FrameAt; không được sửa thuật toán hai tốc độ.

Không được áp dụng mod cho vFrame lần thứ hai trong shader V2. Frame đã được xử lý trên CPU.

Shader V2:

glsl
float f0 = floor(vFrame);
float f1 = min(f0 + 1.0, vV2Last);

float w = (
  uV2LoopMode == 0 &&
  uStep < 0.5
) ? fract(vFrame) : 0.0;

Quy ước uV2LoopMode: 0 = none, 1 = stepped, 2 = holderode.

Dù none nội suy, tại frame cuối f1 = f0, nên không thể sample nhầm frame tiếp theo. stepped và holderode luôn có w = 0.

Không cần thay đổi frameAt, playLife, ONE_FRAME hoặc MODE_INDEX.

Bước 3 — Load và quản lý texture

Bổ sung optional arguments vào attach, không thay ý nghĩa hai arguments cũ:

TypeScript
attach(
  meta: FlipbookMeta,
  texture: THREE.Texture,
  controlA?: THREE.Texture,
  controlB?: THREE.Texture
): void

FlipbookLibrary có trách nhiệm load mask URLs sau khi đã parse manifest và trước attach. Dùng loader đang được project sử dụng, giữ cache theo resolved URL.

Các texture settings V2:

Property

	

Atlas V2

	

Control A

	

Control B




colorSpace

	

NoColorSpace + explicit shader decode

	

NoColorSpace

	

NoColorSpace




premultiplyAlpha

	

false

	

false

	

false




flipY

	

Theo atlas hiện tại

	

Bằng atlas

	

Bằng atlas




magFilter

	

LinearFilter

	

NearestFilter

	

NearestFilter




minFilter

	

LinearFilter

	

NearestFilter

	

NearestFilter




generateMipmaps

	

false

	

false

	

false




wrapS, wrapT

	

ClampToEdgeWrapping

	

Tương tự

	

Tương tự

Đây là cấu hình được chọn cho CX-B, không phải mặc định của mọi Texture. three.js ghi nhận Texture mặc định có NoColorSpace, premultiplyAlpha = false, và các tùy chọn filter/flip khác nhau; DataTexture còn có flipY = false mặc định. 
Three.js Docs
+2

Dùng NearestFilter cho mask để CPU reference và GPU probe không bị sai khác bởi nội suy texel. Khi asset production cần đường reveal mềm hơn ở độ phân giải lớn, việc chuyển sang filtered masks phải đi kèm một probe có CPU bilinear reference.

Để giữ pixel-identical:

Nếu atlas V2 có thể chia sẻ đối tượng Texture với legacy, clone đối tượng texture trước khi thay filter.

Không thay settings của object legacy đã load.

Mask là tài nguyên riêng; khi load thất bại phải báo lỗi và không âm thầm chuyển sang đường render không mask.

Chỉ dispose texture do pool sở hữu, không dispose shared texture của library.

Validation kích thước

Khi texture đã load:

Plain text
A.width  = atlas.width
A.height = atlas.height

B.width  = atlas.width / 2
B.height = atlas.height / 2

Mọi kích thước phải nguyên, chia hết cho cols và rows, và cell dimensions phải lớn hơn 0.

Cả ba texture phải dùng cùng thứ tự frame và cùng orientation.

Chú ý ImageBitmap: three.js ghi rõ Texture.flipY và Texture.premultiplyAlpha không điều khiển lại dữ liệu ImageBitmap sau khi đã decode; orientation và premultiply phải được thiết lập ở bước tạo bitmap. 
Three.js Docs

Trong CX-B, nếu library hiện tại không dùng ImageBitmap, không cần chuyển loader.

Bước 4 — Bố trí instance attributes và bộ nhớ

Không thêm dữ liệu vào state stride 35 của legacy.

Thêm đúng một attribute V2:

TypeScript
const v2AttributeData =
  new Float32Array(capacity * 2);

const iV2 = new THREE.InstancedBufferAttribute(
  v2AttributeData,
  2
);

Layout:

Plain text
iV2.x = last allowed frame
iV2.y = current 60 Hz tick

Trên CPU, cấp phát một lần trong constructor:

TypeScript
private readonly v2Time: Float64Array;
private readonly v2First: Int32Array;
private readonly v2Last: Int32Array;

Nếu dùng legacy-only pool, không cấp phát các arrays bổ sung.

Khi spawn:

Plain text
resolve variant
resolve frameRange
v2Time[slot] = 0
v2First[slot] = first
v2Last[slot] = last
iV2.x = last
iV2.y = 0

Khi update(dt):

Plain text
v2Time[slot] += dt
tick = tickAtAge(v2Time[slot])
iV2.y = tick

rawFrame = existing two-rate frameAt(...)
iData.frame = v2FrameAt(
  rawFrame,
  v2First[slot],
  v2Last[slot],
  loopMode
)

Giữ nguyên toàn bộ nhánh update cũ khi pool không phải V2.

Các buffer mới được ghi đè tại chỗ và đánh dấu dirty một lần sau update. Không tạo array, object hoặc closure mới trong vòng lặp instance.

Ba.js InstancedBufferAttribute hỗ trợ mỗi instance một bộ dữ liệu, trong khi giới hạn số attribute phụ thuộc thiết bị. 
Three.js Docs
+1

Với hai vertex attributes thông thường (position, uv) và sáu instance attributes đã nêu, V2 tăng từ khoảng 8 lên 9 attribute locations. Codex phải đếm các attribute thực tế trong vertex shader trước khi kết luận; điều kiện acceptance là:

TypeScript
activeAttributeCount <= 16

Kiểm tra thêm bằng renderer.capabilities.maxAttributes trong browser probe. 
Three.js Docs

Bước 5 — Chốt tick 60 Hz và thời gian của hiệu ứng

Export helper thuần:

TypeScript

export const V2_TICK_RATE = 60;
export const V2_ERODE_WIDTH = 0.09;

export function tickAtAge(
  ageSeconds: number
): number {
  if (!Number.isFinite(ageSeconds)) {
    throw new RangeError("Invalid ageSeconds");
  }

  return Math.max(
    0,
    Math.floor(ageSeconds * 60 + 1e-6)
  );
}

export function revealThreshold(
  tick: number
): number {
  return Math.min(
    1,
    Math.max(0, (tick + 1) / 4)
  );
}

export function erodeThreshold(
  tick: number,
  width = V2_ERODE_WIDTH
): number {
  if (tick <= 9) return -width;

  if (tick <= 18) {
    return -width +
      (0.85 + width) * (tick - 9) / 9;
  }

  if (tick <= 20) {
    return 0.85 +
      0.07 * (tick - 18) / 2;
  }

  if (tick <= 42) {
    return 0.92 +
      0.08 * (tick - 20) / 22;
  }

  return 1;
}

export function smoothstepCpu(
  edge0: number,
  edge1: number,
  x: number
): number {
  const t = Math.max(
    0,
    Math.min(1, (x - edge0) / (edge1 - edge0))
  );

  return t * t * (3 - 2 * t);
}


tickAtAge được gọi trên CPU, không suy ra tick từ vAge.x = age/life. Như vậy lifetime khác nhau không làm thay đổi nhịp reveal.

Để tránh sai khác do tích lũy thời gian Float32Array, v2Time dùng Float64Array. Epsilon xử lý sai số nhỏ quanh biên tick trong các test với dt = 1/60.

Điều này cho phép tốc độ render thay đổi mà lịch hiệu ứng vẫn dựa trên thời gian đã trôi qua. Tuy nhiên, nếu engine yêu cầu deterministic tuyệt đối giữa những lịch dt có tổng số thực khác nhau, nên cung cấp simulation tick nguyên ở tầng tích hợp sau này; cộng số thực không phải một bảo đảm lockstep tuyệt đối.

Reveal schedule

Tick

	

T(tick)

	

Kết quả




0

	

0.25

	

Root và 25% đầu dải order




1

	

0.50

	

50% order




2

	

0.75

	

75%, gồm nhiều secondary strokes




3

	

1.00

	

Toàn bộ stroke




4+

	

1.00

	

Giữ nguyên reveal

Mask B.R biểu diễn thứ tự, không trực tiếp biểu diễn opacity.

glsl
float revealed = step(maskB.r, T);

Nét được tiết lộ phải đạt ngay full coverage của nó. Không dùng smoothstep trên reveal threshold.

Erosion schedule
-0.1
0.175
0.45
0.725
1
0
3
9
10
15
18
20
31
42
0: Erosion threshold -0.09
3: Erosion threshold -0.09
9: Erosion threshold -0.09
10: Erosion threshold 0.01444
15: Erosion threshold 0.53667
18: Erosion threshold 0.85
20: Erosion threshold 0.92
31: Erosion threshold 0.96
42: Erosion threshold 1

Giá trị e(t) được đề xuất để thử nghiệm; hiệu quả diện tích phải đo từ control mask thật.

Trong attack/hold, e = -width là lựa chọn có chủ đích. Nếu dùng e = 0 từ đầu, một pixel có survival order A = 0 sẽ bị xóa ngay cả trước khi decay bắt đầu.

glsl
float surviving = smoothstep(
  e,
  e + uV2ErodeWidth,
  maskA.a
);

Sau đó:

glsl
float r = clamp(
  (maskA.a - e) / max(1.0 - e, 0.00001),
  0.0,
  1.0
);

Với lịch này, reveal hoàn thành ở tick 3; decay bắt đầu tick 10 và có thể kéo dài đến tick 42. Khoảng decay dài hơn ba lần khoảng reveal.

Điều kiện tick 18: không thể bảo đảm diện tích bright body còn dưới 15% chỉ bằng một giá trị e = 0.85. Điều đó còn phụ thuộc phân bố A.A của asset. Đây phải là một acceptance test dùng mask thật, không được khẳng định đạt khi chỉ có unit test.

Bước 6 — Định nghĩa chính xác màu và coverage của RGBA V2

Tôi chọn cách ánh xạ sau để Codex không phải tự quyết định quan hệ giữa atlas và control masks.

Đầu vào tại mỗi pixel:

Plain text
atlas.rgb = straight sRGB colour
atlas.a   = authored body opacity

maskA.r = hull
maskA.g = ink
maskA.b = hot
maskA.a = survival

maskB.r = reveal order
maskB.g = motion influence

maskB.g được sample nhưng chưa dùng để dịch chuyển UV hoặc geometry trong CX-B. Contract mới xác định ý nghĩa kênh này nhưng chưa xác định motion law. Tự thêm motion sẽ làm khó so sánh CPU/GPU và vượt mục tiêu package.

Coverage equations

Đặt:

Plain text
T = revealThreshold(tick)
e = erodeThreshold(tick)

revealed = step(maskB.r, T)
surviving = smoothstep(e, e + width, maskA.a)

q = clamp(
  maskA.r * revealed * surviving * soft,
  0,
  1
)

soft ở đây chính là multiplier cuối cùng của shader hiện có, bao gồm những hiệu ứng opacity/edge attenuation mà fragment cũ đã xử lý. Không được nhân multiplier đó thêm một lần sau khi compositing.

Sau đó:

Plain text
a_i = q * maskA.g * inkOpacity

a_b = q * atlas.a * (1 - maskA.g)

a_h = q * atlas.a * maskA.b

Mỗi coverage được clamp trong [0,1].

Lý do chọn:

Ink là vùng độc lập do mask vẽ, không yêu cầu atlas.a > 0.

Body nằm trong hull và lấy chi tiết opacity từ atlas.

Body giảm ở nơi ink chiếm ưu thế, giúp giữ được viền mực.

Hot line nằm trên body; compositing formula tự xử lý độ che phủ.

Erosion áp dụng lên từng coverage trước khi chúng được hợp nhất.

Color equations

Vì atlas V2 giữ NoColorSpace, shader thực hiện decode sRGB sang linear. Với RGB của atlas đã decode:

Plain text
C_i = uV2InkColor

C_b = min(
  atlasLinear.rgb * vTint,
  vec3(0.88)
)

C_h = uV2CoreColor * vTint

Giá trị thử ban đầu:

TypeScript
const V2_DEFAULTS = {
  inkColor: [0.04, 0.03, 0.02],
  inkOpacity: 0.45,
  bodyCap: 0.88,
  coreColor: [2.0, 1.6, 0.85],
  erodeWidth: 0.09
} as const;

Trong giai đoạn erosion từ tick 10, thay C_b bằng ramp:

Giá trị r

	

Màu linear RGB

	

Diễn giải




r >= 0.75

	

[0.88,0.82,0.65]

	

white-gold




r >= 0.45

	

[0.88,0.28,0.04]

	

orange




r >= 0.20

	

[0.44,0.018,0.012]

	

crimson




r < 0.20

	

min(uSoot * 0.85, 0.88)

	

soot

Các màu này là điểm khởi đầu của thử nghiệm, không phải màu đã được owner duyệt từng giá trị.

Với tick >= 20, đặt a_h = 0 để hot HDR không tồn tại trong giai đoạn chỉ còn ember và dust. Đây là quy tắc tắt riêng core, không phải fade đồng đều toàn bộ card. Đối với sprite có profile "off", không thực hiện ramp và không tắt core theo tick.

setSoot hiện tại tiếp tục điều khiển màu soot. setGrade, blur, taper, vignette và các setter cũ vẫn giữ ý nghĩa; đường compositing V2 phải lấy giá trị đã được các bước xử lý tương ứng tạo ra, không mặc định bỏ qua chúng.

Giá trị inkOpacity cần thử:

Metal: 0.35.

Fire: bắt đầu 0.55, giới hạn tuning 0.45–0.70.

Do CX-B chưa sửa element kits, các giá trị theo nguyên tố chưa được kết nối tự động. Thêm setter V2:

TypeScript
setV2Ink(
  color: readonly [number, number, number],
  opacity: number
): void;

setV2Core(
  color: readonly [number, number, number]
): void;

setV2ErodeWidth(width: number): void;

Các setter này tác động lên uniform theo pool, không thay đổi các setter cũ. Validation opacity ∈ [0,1], width ∈ [0.06,0.12], colors hữu hạn và không âm.

Giới hạn hot core tối đa 5% diện tích sáng và ink broken 20–35% là điều kiện kiểm định asset, không thể suy ra từ một texel riêng lẻ. Không được clamp maskA.b xuống 0.05, vì 5% là diện tích chứ không phải độ mờ.

Bước 7 — GLSL V2

Bổ sung các khai báo bên ngoài main() trong nhánh compile V2:

glsl

#ifdef FLIPBOOK_V2

attribute vec2 iV2;

varying float vV2Last;
varying float vV2Tick;

uniform int uV2LoopMode;

#ifdef FLIPBOOK_MASKED_RGBA

uniform sampler2D uControlA;
uniform sampler2D uControlB;

uniform vec2 uV2LocalInset;

uniform vec3 uV2InkColor;
uniform vec3 uV2CoreColor;
uniform float uV2InkOpacity;
uniform float uV2ErodeWidth;
uniform float uV2BodyCap;

// 0 = off, 1 = key1-impact-60
uniform int uV2Profile;

#endif
#endif


Trong vertex shader V2:

glsl
vV2Last = iV2.x;
vV2Tick = iV2.y;

iV2 không được khai báo trong legacy shader.

Các function GLSL cho masked RGBA:

glsl

#ifdef FLIPBOOK_MASKED_RGBA

vec3 v2SrgbToLinear(vec3 c) {
  vec3 lo = c / 12.92;
  vec3 hi = pow(
    (c + 0.055) / 1.055,
    vec3(2.4)
  );

  return mix(
    lo,
    hi,
    step(vec3(0.04045), c)
  );
}

float v2Smoothstep(
  float a,
  float b,
  float x
) {
  float t = clamp((x - a) / (b - a), 0.0, 1.0);
  return t * t * (3.0 - 2.0 * t);
}

float v2RevealThreshold(float tick) {
  return clamp((tick + 1.0) / 4.0, 0.0, 1.0);
}

float v2ErodeThreshold(
  float tick,
  float width
) {
  if (tick <= 9.0) return -width;

  if (tick <= 18.0) {
    return -width +
      (0.85 + width) * (tick - 9.0) / 9.0;
  }

  if (tick <= 20.0) {
    return 0.85 + 0.07 * (tick - 18.0) / 2.0;
  }

  if (tick <= 42.0) {
    return 0.92 + 0.08 * (tick - 20.0) / 22.0;
  }

  return 1.0;
}

vec3 v2Ramp(float r, vec3 soot) {
  if (r >= 0.75) {
    return vec3(0.88, 0.82, 0.65);
  }

  if (r >= 0.45) {
    return vec3(0.88, 0.28, 0.04);
  }

  if (r >= 0.20) {
    return vec3(0.44, 0.018, 0.012);
  }

  return min(soot * 0.85, vec3(0.88));
}

vec4 v2Composite(
  vec4 atlas,
  vec3 atlasLinear,
  vec4 maskA,
  vec4 maskB,
  vec3 tint,
  float soft,
  float tick,
  vec3 soot
) {
  float revealed = 1.0;
  float surviving = 1.0;
  float e = -uV2ErodeWidth;

  if (uV2Profile == 1) {
    float T = v2RevealThreshold(tick);
    e = v2ErodeThreshold(
      tick,
      uV2ErodeWidth
    );

    revealed = step(maskB.r, T);

    surviving = v2Smoothstep(
      e,
      e + uV2ErodeWidth,
      maskA.a
    );
  }

  float q = clamp(
    maskA.r * revealed * surviving * soft,
    0.0,
    1.0
  );

  float ai = clamp(
    q * maskA.g * uV2InkOpacity,
    0.0,
    1.0
  );

  float ab = clamp(
    q * atlas.a * (1.0 - maskA.g),
    0.0,
    1.0
  );

  float ah = clamp(
    q * atlas.a * maskA.b,
    0.0,
    1.0
  );

  vec3 Ci = uV2InkColor;

  vec3 Cb = min(
    atlasLinear * tint,
    vec3(uV2BodyCap)
  );

  vec3 Ch = uV2CoreColor * tint;

  if (uV2Profile == 1 && tick >= 10.0) {
    float r = clamp(
      (maskA.a - e) / max(1.0 - e, 0.00001),
      0.0,
      1.0
    );

    Cb = min(
      v2Ramp(r, soot) * tint,
      vec3(uV2BodyCap)
    );
  }

  if (uV2Profile == 1 && tick >= 20.0) {
    ah = 0.0;
  }

  float alpha =
    1.0 -
    (1.0 - ai) *
    (1.0 - ab) *
    (1.0 - ah);

  vec3 rgb =
    Ci * ai * (1.0 - ab) * (1.0 - ah) +
    Cb * ab * (1.0 - ah) +
    Ch * ah;

  return vec4(rgb, alpha);
}

#endif

Sampling atlas và hai masks

Dùng cùng một hàm UV cho cả ba texture. Với asset atlas được đóng gói theo thứ tự từ trái sang phải, từ trên xuống dưới:

glsl
vec2 v2FrameUV(
  float frame,
  vec2 localUV
) {
  float col = mod(frame, uGrid.x);
  float row = floor(frame / uGrid.x);

  vec2 uv = clamp(
    localUV,
    uV2LocalInset,
    vec2(1.0) - uV2LocalInset
  );

  return (
    vec2(col, uGrid.y - 1.0 - row) + uv
  ) / uGrid;
}

uV2LocalInset được chuẩn bị một lần từ cell size của mask B:

TypeScript
const bCellWidth = controlB.image.width / meta.cols;
const bCellHeight = controlB.image.height / meta.rows;

uV2LocalInset.set(
  0.5 / bCellWidth,
  0.5 / bCellHeight
);

Nếu hệ UV hiện tại đã đảo trục Y theo cách khác, Codex phải dùng lại mapping đúng của atlas legacy cho cả ba texture, không được đảo Y hai lần.

Trong fragment, tại vị trí hiện tại của đường RGBA:

glsl

#ifdef FLIPBOOK_MASKED_RGBA

float f0 = floor(vFrame);
float f1 = min(f0 + 1.0, vV2Last);

float w = (
  uV2LoopMode == 0 &&
  uStep < 0.5
) ? fract(vFrame) : 0.0;

vec2 uv0 = v2FrameUV(f0, vUv);
vec2 uv1 = v2FrameUV(f1, vUv);

vec4 t0 = texture2D(uMap, uv0);
vec4 t1 = texture2D(uMap, uv1);

vec4 a0 = texture2D(uControlA, uv0);
vec4 a1 = texture2D(uControlA, uv1);

vec4 b0 = texture2D(uControlB, uv0);
vec4 b1 = texture2D(uControlB, uv1);

vec4 maskA = mix(a0, a1, w);
vec4 maskB = mix(b0, b1, w);

float atlasAlpha = mix(t0.a, t1.a, w);

// Interpolate premultiplied linear source,
// then recover straight linear body colour.
vec3 pm0 = v2SrgbToLinear(t0.rgb) * t0.a;
vec3 pm1 = v2SrgbToLinear(t1.rgb) * t1.a;

vec3 atlasLinear =
  mix(pm0, pm1, w) /
  max(atlasAlpha, 0.000001);

vec4 atlas = vec4(
  mix(t0.rgb, t1.rgb, w),
  atlasAlpha
);

// soft, vTint, uSoot are the existing
// shader's values after their normal processing.
gl_FragColor = v2Composite(
  atlas,
  atlasLinear,
  maskA,
  maskB,
  vTint,
  soft,
  vV2Tick,
  uSoot
);

#endif


Bảo đảm vUv trong ví dụ được nối với quad-local UV mà shader hiện tại dùng. uGrid, uMap, uStep, soft, vTint và uSoot phải tương ứng với những biến thực có trong source; không tạo thêm một lớp xử lý các giá trị này nếu source đã xử lý.

Đoạn code trên là nhánh thay thế RGBA cuối cùng. Không giữ lại phần erode-in procedural, burn procedural hoặc pm * soft của RGBA cũ trong nhánh masked V2.

Không chèn thêm output-color conversion trước khi premultiplied alpha được blend trong HDR linear render target. three.js sử dụng Linear-sRGB làm working color space, còn việc chuyển sang output space phụ thuộc render pipeline. Đối với custom ShaderMaterial, chuyển đổi output phải được cấu hình tường minh ở đúng giai đoạn. 
Three.js

Bước 8 — CPU reference cùng công thức shader

Thêm một pure reference function vào flipbook.ts. Hàm này dành cho test và probe, không gọi trong vòng lặp render.

TypeScript

export type V2RGB = readonly [
  number, number, number
];

export type V2RGBA = readonly [
  number, number, number, number
];

export interface V2PixelInput {
  atlas: V2RGBA;       // straight sRGB
  controlA: V2RGBA;    // hull, ink, hot, survival
  controlB: V2RGBA;    // reveal, motion, unused, unused
  tint: V2RGB;         // linear
  inkColor: V2RGB;     // linear
  coreColor: V2RGB;    // linear HDR
  sootColor: V2RGB;    // linear
  inkOpacity: number;
  bodyCap: number;
  soft: number;
  tick: number;
  erodeWidth: number;
  profile: "off" | "key1-impact-60";
}

const v2Clamp = (x: number) =>
  Math.max(0, Math.min(1, x));

export function v2SrgbToLinearCpu(
  c: number
): number {
  return c <= 0.04045
    ? c / 12.92
    : Math.pow((c + 0.055) / 1.055, 2.4);
}

export function composeV2Coverages(
  ai: number,
  ab: number,
  ah: number,
  ci: V2RGB,
  cb: V2RGB,
  ch: V2RGB
): [number, number, number, number] {
  const alpha =
    1 - (1 - ai) * (1 - ab) * (1 - ah);

  const rgb = [0, 1, 2].map(k =>
    ci[k] * ai * (1 - ab) * (1 - ah) +
    cb[k] * ab * (1 - ah) +
    ch[k] * ah
  );

  return [rgb[0], rgb[1], rgb[2], alpha];
}

export function composeV2Pixel(
  p: V2PixelInput
): [number, number, number, number] {
  const A = p.controlA;
  const B = p.controlB;
  const t = p.tick;
  const active = p.profile === "key1-impact-60";

  const T = active ? revealThreshold(t) : 1;
  const e = active
    ? erodeThreshold(t, p.erodeWidth)
    : -p.erodeWidth;

  const revealed = active
    ? Number(T >= B[0])
    : 1;

  const surviving = active
    ? smoothstepCpu(e, e + p.erodeWidth, A[3])
    : 1;

  const q = v2Clamp(
    A[0] * revealed * surviving * p.soft
  );

  const ai = v2Clamp(
    q * A[1] * p.inkOpacity
  );
  const ab = v2Clamp(
    q * p.atlas[3] * (1 - A[1])
  );
  let ah = v2Clamp(
    q * p.atlas[3] * A[2]
  );

  const ci: V2RGB = p.inkColor;

  const cb: [number, number, number] = [0, 0, 0];
  const ch: [number, number, number] = [0, 0, 0];

  let rampIndex = -1;

  if (active && t >= 10) {
    const r = v2Clamp(
      (A[3] - e) / Math.max(1 - e, 0.00001)
    );

    rampIndex =
      r >= 0.75 ? 0 :
      r >= 0.45 ? 1 :
      r >= 0.20 ? 2 : 3;
  }

  const ramps: readonly V2RGB[] = [
    [0.88, 0.82, 0.65],
    [0.88, 0.28, 0.04],
    [0.44, 0.018, 0.012],
    [
      Math.min(p.sootColor[0] * 0.85, 0.88),
      Math.min(p.sootColor[1] * 0.85, 0.88),
      Math.min(p.sootColor[2] * 0.85, 0.88)
    ]
  ];

  for (let k = 0; k < 3; k++) {
    const base = rampIndex >= 0
      ? ramps[rampIndex][k]
      : v2SrgbToLinearCpu(p.atlas[k]);

    cb[k] = Math.min(
      base * p.tint[k],
      p.bodyCap
    );

    ch[k] = p.coreColor[k] * p.tint[k];
  }

  if (active && t >= 20) {
    ah = 0;
  }

  return composeV2Coverages(
    ai, ab, ah, ci, cb, ch
  );
}


composeV2Pixel cố ý nhận một sample atlas đã xác định. Trong none khi w > 0, CPU probe phải nội suy atlasAlpha, premultiplied linear RGB, controlA và controlB giống shader trước khi gọi compositing. Không được nội suy sRGB trực tiếp rồi mới decode khi so sánh.

Các temporary arrays và .map() trong CPU reference chấp nhận được vì đây là hàm kiểm thử. Không gọi hàm này trong FlipbookPool.update() hoặc quá trình render.

Khi triển khai production, có thể đưa ramps thành constant ngoài hàm để tránh allocations ngay cả trong benchmark CPU. Việc đó không thay kết quả.

Bước 9 — Hoàn thiện API, lifecycle và shader variants

Thêm vào FlipOptions mà không sửa các field cũ:

TypeScript
export interface FlipbookV2Options {
  variant?: string;
}

Cho phép FlipOptions kế thừa hoặc chứa FlipbookV2Options.

Khi spawn:

Resolve variant thành khoảng [first,last]. Variant không tồn tại phải báo lỗi.

Khởi tạo v2Time[slot] = 0.

Khởi tạo iV2 = [last,0].

Chọn timingProfile theo quy tắc dưới đây.

Khởi tạo các thuộc tính cũ theo đúng logic hiện có.

Quy tắc timing mặc định:

Điều kiện

	

Profile




Legacy

	

Không dùng




V2 không có hai masks

	

"off"




V2 masked stepped

	

"off"




V2 masked none

	

"key1-impact-60"




V2 masked holderode

	

"key1-impact-60"




Có timingProfile tường minh

	

Dùng giá trị khai báo

Với "key1-impact-60", nếu lifetime không được chỉ định, dùng tối thiểu 43/60 giây để có thể hiển thị hết tick 42. Nếu caller truyền lifetime ngắn hơn, giữ nguyên ý nghĩa lifetime của caller, nhưng hiệu ứng sẽ kết thúc sớm; không kéo dài âm thầm.

holderode không được tự động tăng tuổi thọ của instance sau khi hết life.

Shader variants cần compile

Shader variant

	

Defines




Legacy

	

Không có define V2




V2, không masked RGBA

	

FLIPBOOK_V2




V2, masked RGBA

	

FLIPBOOK_V2, FLIPBOOK_MASKED_RGBA

Ở biến thể V2 không có masks, shader phải giữ nguyên các mode rgba, fire, smoke, heat hiện có, chỉ thay bước chọn frame.

Khi setSharpen hoặc stepped được gọi, giữ nguyên thiết lập cũ. Trong V2 none, uStep vẫn có thể buộc nội suy về 0. Trong stepped và holderode, không cho phép nội suy bất kể uStep.

Một pool luôn chỉ có một loopMode và một timingProfile. Không tạo shader variant riêng cho từng instance hoặc từng variant.

3. Test plan — tests/view/flipbook-v2.test.ts

Vitest trong Node có thể test toàn bộ helper thuần, parsing, texture metadata và construction của pool mà không tạo WebGL context.

3.1. Test matrix bắt buộc

Test

	

Input

	

Expected




Legacy manifest

	

Không có field V2

	

Không có define V2; metadata cũ giữ nguyên




Legacy loop

	

loop:true

	

Shader legacy giữ uLoop=1




Explicit stepped

	

loop:true, loopMode:"stepped"

	

Shader V2; không wrap interpolation




Explicit none

	

loop:true, loopMode:"none"

	

loopMode ưu tiên




Range clamp

	

[9,14], raw frame 15

	

none=14




Range loop

	

[9,14], raw frame 15

	

stepped=9




Hold

	

[9,14], raw frame 15

	

holderode=14




Inside range

	

[9,14], raw frame 10.5

	

none=10.5, stepped=10, holderode=10




Reveal tick 0

	

Tick 0

	

0.25




Reveal tick 3

	

Tick 3

	

1.0




Hold tick 9

	

Tick 9

	

e=-0.09




Erode tick 18

	

Tick 18

	

e=0.85




Erode tick 20

	

Tick 20

	

e=0.92




End tick 42

	

Tick 42

	

e=1

3.2. Test frame logic
TypeScript

import {
  describe,
  expect,
  it
} from "vitest";

import {
  v2FrameAt,
  tickAtAge,
  revealThreshold,
  erodeThreshold,
  smoothstepCpu,
  composeV2Coverages,
  composeV2Pixel
} from "../../src/view/skills/flipbook";

describe("FlipbookPool v2 frames", () => {
  it("does not wrap a nonlooping range", () => {
    expect(v2FrameAt(15, 9, 14, "none"))
      .toBe(14);

    expect(v2FrameAt(10.5, 9, 14, "none"))
      .toBe(10.5);
  });

  it("loops only by stepping", () => {
    expect(v2FrameAt(14.75, 9, 14, "stepped"))
      .toBe(14);

    expect(v2FrameAt(15, 9, 14, "stepped"))
      .toBe(9);

    expect(v2FrameAt(16.5, 9, 14, "stepped"))
      .toBe(10);
  });

  it("holds the final frame", () => {
    expect(v2FrameAt(10.5, 9, 14, "holderode"))
      .toBe(10);

    expect(v2FrameAt(15, 9, 14, "holderode"))
      .toBe(14);
  });
});

describe("FlipbookPool v2 timing", () => {
  it("reveals over four ticks", () => {
    expect(
      [0, 1, 2, 3, 4].map(revealThreshold)
    ).toEqual([0.25, 0.5, 0.75, 1, 1]);
  });

  it("uses the approved erosion schedule", () => {
    expect(erodeThreshold(0)).toBe(-0.09);
    expect(erodeThreshold(9)).toBe(-0.09);
    expect(erodeThreshold(18)).toBeCloseTo(0.85);
    expect(erodeThreshold(20)).toBeCloseTo(0.92);
    expect(erodeThreshold(42)).toBeCloseTo(1);
  });

  it("preserves low-order tips before decay", () => {
    expect(
      smoothstepCpu(-0.09, 0, 0)
    ).toBe(1);

    expect(
      smoothstepCpu(
        erodeThreshold(18),
        erodeThreshold(18) + 0.09,
        0.7
      )
    ).toBe(0);

    expect(
      smoothstepCpu(0.85, 0.94, 0.9)
    ).toBeCloseTo(0.5829904, 6);
  });

  it("quantizes elapsed time consistently", () => {
    expect(tickAtAge(0)).toBe(0);
    expect(tickAtAge(1 / 60)).toBe(1);
    expect(tickAtAge(3 / 60)).toBe(3);
    expect(tickAtAge(18 / 60)).toBe(18);
    expect(tickAtAge(42 / 60)).toBe(42);
  });
});


Thêm test update theo ba lịch dt khác nhau, có cùng tổng thời gian:

Plain text
18 x (1/60)
6 x (3/60)
1 x (18/60)

Cả ba phải tạo tick=18, cùng frame và cùng threshold.

Test cần thực hiện cả trên slot 0 và slot được tái sử dụng sau clear/despawn, để tránh lỗi không reset timer khi pooling.

3.3. Test compositing với numeric expectations

Một sample coverage cụ thể:

Plain text
a_i = 0.25
a_b = 0.50
a_h = 0.10

C_i = [0.1, 0.1, 0.1]
C_b = [0.8, 0.4, 0.2]
C_h = [2.0, 1.0, 0.5]

Kết quả chính xác:

Plain text
alpha = 0.6625
RGB   = [0.57125, 0.29125, 0.15125]
TypeScript

describe("FlipbookPool v2 compositing", () => {
  it("returns transparent black for no coverage", () => {
    expect(
      composeV2Coverages(
        0, 0, 0,
        [0.1, 0.1, 0.1],
        [0.8, 0.4, 0.2],
        [2, 1, 0.5]
      )
    ).toEqual([0, 0, 0, 0]);
  });

  it("composes partial coverage", () => {
    const result = composeV2Coverages(
      0.25, 0.5, 0.1,
      [0.1, 0.1, 0.1],
      [0.8, 0.4, 0.2],
      [2, 1, 0.5]
    );

    const expected = [
      0.57125,
      0.29125,
      0.15125,
      0.6625
    ];

    result.forEach((v, i) => {
      expect(v).toBeCloseTo(expected[i], 7);
    });
  });

  it("lets full hot core cover lower layers", () => {
    expect(
      composeV2Coverages(
        1, 1, 1,
        [0.1, 0.1, 0.1],
        [0.8, 0.4, 0.2],
        [2, 1, 0.5]
      )
    ).toEqual([2, 1, 0.5, 1]);
  });
});


Ngoài ra test composeV2Pixel với các cases:

maskA=[1,0,0,1], maskB.R=0, atlas trắng alpha 1, tick 0, tint trắng, soft 1: RGB=[0.88,0.88,0.88], alpha 1.

maskA=[1,1,0,1], inkOpacity=0.45, ink [0.04,0.03,0.02]: RGB [0.018,0.0135,0.009], alpha 0.45.

maskB.R=0.5, tick 0: toàn bộ output bằng 0; tick 1: revealed.

maskA.A=0, tick 0: chưa bị erosion; tick 18: bị xóa.

maskA.A=0.9, tick 18: survival xấp xỉ 0.5829904.

Profile "off", tick 42: không tự erosion hoặc tắt hot core.

Dùng toBeCloseTo cho floating point, không dùng so sánh equality trực tiếp với giá trị thập phân tính toán.

3.4. Kiểm tra blend trên light/dark stone

Với sample partial ở trên:

Background linear

	

Expected RGB sau blend




Light stone #d6d0c2

	

[0.798200, 0.504131, 0.333324]




Dark stone #2a2c30

	

[0.579064, 0.299751, 0.161225]

Các giá trị đã chuyển background từ sRGB sang Linear-sRGB trước khi áp dụng src + dst*(1-alpha).

Đây là golden values để so sánh RGB của framebuffer tuyến tính, không phải RGB của screenshot đã tone-map/bloom/output-transform.

3.5. Parser và compatibility tests

Tạo fixtures trực tiếp trong file test, không cần file fixture thứ ba.

Các trường hợp phải reject:

loopMode: "crossfade".

sourceFps: 0, NaN, âm hoặc string.

frameRange vượt frames.

Variant row vượt rows, frame range có cột không hợp lệ.

anchor ngoài [0,1].

Chỉ có controlA mà thiếu controlB.

Hai masks trên clip fire.

timingProfile: "key1-impact-60" nhưng không có masks.

Các trường hợp phải accept:

Manifest version undefined và 1.

clips dạng object và dạng array có id.

file hoặc atlas.

grid hoặc cols/rows.

Các unknown fields như md5, blend, alphaKind.

loop:true legacy, không có field V2.

Nên kiểm tra baseline shader thật trước khi sửa: Codex dùng phiên bản đầu trong Git để lưu hash của đoạn legacy fragment, và sau khi sửa so sánh lại nhánh shader legacy được trích ra. Không tự tạo hash golden từ source đã sửa, vì như vậy test có thể chứng minh nhầm một regression là đúng.

3.6. Node-side construction tests

Dùng THREE.DataTexture với pixel bytes tự tạo, không dùng TextureLoader hoặc DOM canvas.

Test:

attach legacy chỉ có hai arguments vẫn hoạt động.

V2 attach có đủ ba textures và masks.

Uniforms trỏ đúng texture objects.

Defines chính xác cho ba shader variants.

iV2.itemSize === 2.

iV2.array.length === capacity * 2.

Không thay đổi stride 35 của CPU state cũ.

Material vẫn sử dụng cùng blending factors.

clear reset V2 timers và slot state.

dispose giải phóng đúng tài nguyên sở hữu.

node không có WebGL context nên không thể xác nhận shader link thành công bằng các test này.

4. Browser probe cho coordinator

Đây là acceptance gate độc lập, phải chạy khi có GPU. Không thêm file trong package CX-B.

4.1. Cấu hình probe

Dùng một trang lab hiện có hoặc đoạn script trong browser console.

Tạo WebGLRenderer WebGL2, tắt tone mapping của material dưới test.

Tạo atlas synthetic với các frame có màu và alpha biết trước; tạo A/B synthetic cùng grid, B ở half resolution.

Render một quad hoặc pool có một instance vào một linear floating-point render target.

Probe lần đầu với blending disabled để lấy source premultiplied RGBA.

Probe lần hai với blending production trên hai background.

Đọc pixel và so sánh với composeV2Pixel cùng dữ liệu.

Render-target floating point cần kiểm tra extension trên thiết bị. EXT_color_buffer_float cung cấp khả năng render vào các format float gồm RGBA16F; float32 blending còn có giới hạn bổ sung, vì vậy ưu tiên RGBA16F cho probe HDR. 
MDN
+2

Kiểm tra tối thiểu các frame:

Plain text
none:
  first
  middle
  last
  last + fractional time

stepped:
  last
  last + 0.99 frame
  first after wrap

holderode:
  first
  last
  long hold at last

Kiểm tra timeline:

Plain text
tick 0, 1, 2, 3, 9, 10, 18, 20, 31, 42

Và ba vùng synthetic:

Plain text
No coverage:
  hull = 0

Partial coverage:
  ai = 0.25
  ab = 0.50
  ah = 0.10

Full hot coverage:
  ah = 1
Sai số acceptance
TypeScript
const tolerance = 1 / 255;

for (let c = 0; c < 4; c++) {
  if (Math.abs(gpu[c] - cpu[c]) > tolerance) {
    throw new Error(
      `V2 mismatch channel=${c}: ` +
      `gpu=${gpu[c]} cpu=${cpu[c]}`
    );
  }
}

Với test background đã blend, kiểm RGB. Với test source không blend, kiểm đủ RGBA.

Không so sánh screenshot PNG sau bloom hoặc tone mapping với CPU linear value. Khi dùng RGBA16F, cần đọc và chuyển đổi giá trị half-float đúng cách trước khi so sánh.

Kiểm tra runtime

Ghi nhận renderer.info.render.calls, số attributes và số textures sử dụng. WebGLRenderer cung cấp các thống kê draw calls và capabilities cho những kiểm tra này. 
Three.js Docs

Acceptance:

Plain text
1 pool = 1 draw call
active vertex attributes <= 16
no shader compile/link errors
no GL errors
no per-frame allocations attributable to V2

Để đánh giá ghosting, so sánh trực quan giữa frame cuối và frame đầu tại boundary, đồng thời đọc frame indices thực tế. Đây là kiểm tra bên ngoài unit test.

5. Rủi ro và phương pháp kiểm tra

Rủi ro

	

Mức độ

	

Cách kiểm tra / xử lý




Legacy thay đổi pixel

	

Critical

	

Baseline shader hash, parser regression, old clips visual comparison




Atlas/mask lệch Y

	

Critical

	

Synthetic atlas có marker khác nhau ở bốn góc




Source alpha bị premultiply hai lần

	

Critical

	

CPU/GPU partial coverage + transparent RGB probe




Sai color space

	

High

	

Linear readback, HDR probe, kiểm Texture.colorSpace




Mask bleed sang cell kế bên

	

High

	

Cell-border probe, tắt mipmaps, inset theo cell B




Body không còn dưới 15% ở tick 18

	

High

	

Đo bright-pixel ratio trên mask thật




Hot core chiếm quá 5%

	

High

	

Histogram/area check từ mask A.B




holderode không đến frame cuối kịp hold

	

Medium

	

So sánh sourceFps, frameRange và thời điểm tick 10




Frame-rate-dependent tick

	

Medium

	

Nhiều lịch dt, cùng elapsed time




Quá nhiều GPU attributes

	

Medium

	

Kiểm active attributes trên browser




none bị nội suy với frame ngoài range

	

High

	

Test end-frame bằng synthetic atlas




Color clamp làm core mất HDR

	

High

	

Kiểm C_h không bị clamp theo bodyCap

Với trường hợp sourceFps quá thấp hoặc frameRange dài, holderode có thể vẫn đang chạy animation khi erosion bắt đầu. Quy tắc giữ frame cuối là chính xác, nhưng asset đó chưa đạt timeline key-1 mong muốn. CX-B không nên tự tăng FPS hoặc rút ngắn đoạn frame ngầm; coordinator cần chọn đoạn và FPS hợp lý khi chuyển manifest.

6. Những điểm chưa thể xác nhận

Có bốn điểm cần kiểm chứng trong source thực hoặc browser; đây không phải lý do để mở rộng phạm vi package.

1. Hình dạng cụ thể của FlipOptions và cách frameAt nhận offset. Brief mô tả ý nghĩa nhưng không cung cấp toàn bộ TypeScript source. Những đoạn ghép vào spawn, update và vertex shader vì vậy là đặc tả triển khai chính xác về hành vi, chưa phải một diff được xác nhận compile against repository. Codex cần đọc chữ ký gốc trước khi áp dụng, tuyệt đối không thay đổi ý nghĩa tham số cũ.

2. Các biến soft, vTint, uSoot và UV mapping thực tế. Contract compositing mới đã xác định, nhưng vị trí tính các biến này trong fragment cũ cần được giữ đúng. Đặc biệt, phải chắc chắn opacity không được nhân hai lần và grade không bị bỏ qua.

3. Các đặc tính pixel thật của atlas. Tôi giả định RGB atlas V2 là sRGB và alpha là straight alpha. Nếu atlas được xuất bằng linear RGB hoặc chứa dữ liệu premultiplied từ công cụ tạo asset, loader/shader cần nhận diện đúng nguồn trước khi đạt acceptance. Không thay đổi interpretation của atlas legacy.

4. Khả năng đạt chỉ tiêu thẩm mỹ và hiệu năng với asset thật. R_seam <= 1.2, hot area không quá 5%, ink broken 20–35%, bright body còn không quá 15% ở tick 18 và chất lượng VFX 8.5 đều phụ thuộc asset và renderer thật. Chúng chưa thể được chứng minh bằng synthetic CPU tests.

7. Quyết định handoff cuối cùng

Chốt kiến trúc: Legacy shader bất biến; V2 dùng compile-time defines.

Chốt frame: none nội suy nội đoạn; stepped loop rời rạc; holderode giữ frame cuối.

Chốt compositing: Mask A/B riêng, ba coverage, một fragment, một lần premultiplied compositing.

Chốt timeline: Tick 60 Hz, reveal 0–3, hold 4–9, erosion 10–42.

Chốt kiểm thử: Vitest CPU là gate thứ nhất; browser GPU tolerance ±1/255 là gate thứ hai.

Tiêu chí hoàn thành CX-B: tsc --noEmit và toàn bộ Vitest cũ/mới phải pass; không thay đổi API cũ; shader legacy phải giữ hành vi cũ; V2 không wrap-crossfade; mỗi pool vẫn một draw call. Chỉ được tuyên bố đạt toàn bộ contract compositing sau khi browser probe vượt sai số ±1/255.

Nguồn kỹ thuật chính

three.js r170 — ShaderMaterial source và ShaderMaterial documentation.

three.js r170 — Texture source; Texture settings.

three.js — Color management.

InstancedBufferAttribute và WebGLRenderer capabilities.

MDN — WebGL blending equations.

MDN — EXT_color_buffer_float và MDN — EXT_float_blend.

Các lịch tick, bảng màu, API V2 và quy tắc fallback là đề xuất thiết kế cho CX-B dựa trên contract của owner, không phải những hành vi được tài liệu three.js quy định.

You said:
Review your latest full answer above against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff).
Worked for 3m 27s
Analyzed
ChatGPT said:

VERDICT: FAIL

Bản trước có những lỗi thực sự ảnh hưởng đến khả năng triển khai hoặc kiểm chứng. Dưới đây là các lỗi cần sửa, tiếp theo là bản phân tích và giải pháp đầy đủ, không phải diff.

I. Các lỗi phát hiện

1. CPU reference không tương đương shader khi nội suy frame. Shader decode sRGB, nội suy premultiplied linear RGB rồi phục hồi màu straight-linear. composeV2Pixel lại nhận một atlas sample straight-sRGB và decode lần nữa. Không có hàm CPU được định nghĩa chính xác để xử lý hai frame và cùng trọng số nội suy. Vì vậy chưa thể kiểm chứng ±1/255 cho none.

2. GLSL không tích hợp đầy đủ setSharpen. Shader V2 chỉ xét uStep và fract(vFrame), bỏ qua cơ chế chuyển frame bằng noise-stagger hiện có. Điều này làm một setter cũ mất tác dụng.

3. anchor được parse nhưng không được sử dụng. Thiếu quy tắc ưu tiên giữa anchor và pivot, cũng như vị trí nối vào uPivot.

4. timingProfile chưa đủ chặt chẽ ở runtime. Bản trước mô tả default trong bảng nhưng không chốt đầy đủ thời điểm kích hoạt, cách giữ ý nghĩa các điều khiển iAge/FlipOptions hiện có, và việc reset timer cho slot tái sử dụng.

5. Quy tắc áp dụng soft thay đổi ý nghĩa fade cũ. Shader cũ nhân soft một lần lên RGB premultiplied và alpha cuối cùng. Bản trước nhân soft vào từng coverage trước khi hợp nhất, cho kết quả opacity khác. Cần giữ phép nhân cuối cùng, đồng thời không nhân thêm alpha.

6. uV2LocalInset không xử lý đúng cả hai độ phân giải. Dùng half-texel inset của mask B cho atlas và mask A có thể cắt các texel biên. Cần inset riêng cho atlas/A và B, với cùng mapping frame.

7. Thiếu GLSL hoàn chỉnh cho V2 không có masks. Bản trước khai báo shader variant nhưng chưa xác định chính xác việc lấy f0, f1, w cho cả rgba, fire, smoke, heat. Worker vẫn phải tự thiết kế phần này.

8. Chưa phân định rõ dữ liệu iAge cũ và erosion mới. Đặc biệt iAge.w và cool-start có thể bị bỏ qua hoặc bị áp dụng thêm lần thứ hai. Điều này vi phạm yêu cầu giữ ý nghĩa các điều khiển cũ.

9. Một số test không chứng minh điều chúng được dùng để chứng minh. v2FrameAt chỉ chứng minh frame index, không chứng minh shader không crossfade. Test partial compositing mới kiểm công thức đại số, chưa kiểm toàn bộ pipeline từ RGBA/masks đến output. Không có test bắt buộc cho interpolation weight, mask sampling, setSharpen và profile resolution.

10. Browser probe chưa đủ chính xác. Cần kiểm tra chế độ readback thực sự được hỗ trợ, đối chiếu source RGBA trước blending và RGB sau blending, tránh so sánh dữ liệu HDR linear với framebuffer đã qua color conversion.

11. Có mâu thuẫn literal giữa hai yêu cầu của brief. Legacy loop:true đang crossfade cuối→đầu. Không thể đồng thời giữ hình ảnh pixel-identical và cấm hành vi đó trên chính clip cũ. Bản trước nhận diện mâu thuẫn này nhưng chưa trình bày ngoại lệ legacy thành một điều kiện acceptance rõ ràng.

12. Validation và lifecycle chưa đủ để worker triển khai không phải đoán. Đặc biệt việc resolve variant, fallback frameRange, ownership của mask textures, xử lý attach thiếu texture và việc giữ nguyên API FlipbookLibrary.

Không cần thay đổi công thức compositing đã duyệt, bốn mốc reveal, chiến lược giữ legacy shader hay mô hình một draw call. Các phần đó là hướng đúng.

II. CX-B FlipbookPool v2 — Bản
ChatGPT can make mistakes. Check important info.
Latest response




Thinking effort
High
````
