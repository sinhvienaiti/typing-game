# Phiếu 328 · Tu Tiên · Lab: ấn chiêu, sao nứt và rãnh Kim lấy từ tranh vẽ, thay hình vẽ bằng code

Anh đã chê hình vẽ bằng code: "vết nứt, vết cháy, đường may kiểu mã không đẹp". Luật nhà: hình lấy từ tranh vẽ, code chỉ đặt, canh nhịp và cho chuyển động (`.agents/skills/game-vfx-production/SKILL.md`; `references/recipes.md` §4 "Masks" và §6; `references/runtime-packaging.md`). Codex đã vẽ 7 tranh Kim, anh duyệt lúc 19:10–19:18 ngày 06/11 (phiếu 323, 324, 324b). Phiếu này thay hàng 2 và 3 của `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md` bằng các tranh đó.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo: `docs/codex-queue/328-report.md` (tiếng Việt, ngắn).

## Nơi làm
- **W** = `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-sigils`, nhánh `codex/lab-metal-sigils` tại `1b9461e` (`b8ebd51` + thanh chiêu của phiếu 322). `W/art-src` và `W/node_modules` là liên kết sang `games/immortality-cultivation/`. Chưa có W thì dừng và ghi báo cáo.
- **Được ghi:**
  - file mới: `W/src/view/skills/painted-sigils.ts`, `W/scripts/vfx/sigil-masks-lib.ts`, `W/scripts/vfx/sigil-masks.ts`, `W/tests/view/painted-sigils.test.ts`;
  - sửa, chỉ ở các chỗ nêu dưới đây: `W/src/view/skills/fxkit.ts` (`SIGIL_FRAGMENT`, `GroundSigil`), `W/src/view/skills/sword-rain.ts` (`MARK_VERTEX`, `MARK_FRAGMENT`, `GroundMarks`), `W/src/view/skills/sword-skills.ts`;
  - thư mục media mới `W/art-src/lab/vfx/sigils/` (7 PNG và `manifest.json`; media không bao giờ commit), và báo cáo.
- **Cấm:** mọi lệnh git ghi (`git status`, `git diff` để đọc thì được); sửa tranh nguồn hay ghi gì khác trong `art-src`; cài gói, mở cổng, chạy dev server hay trình duyệt; sửa file khác. **Không đụng** `src/view/skills/flipbook.ts`, `src/lab/comet-head.ts`, `src/lab/meteor-rain.ts`, `src/lab/skills-main.ts`: làn phiếu 326 đang sửa bốn file này ở worktree khác.

## Tranh nguồn và bảng mặt nạ (Claude đã đo)
`S = W/art-src/lab/firefly-sprint-2026-11-05/stills/skills/`. Mọi tranh 1672×941, nền gần đen.
- **Hộp sáng:** hộp bao các điểm có `max(R,G,B) ≥ 13`, như `magick f -alpha off -separate -evaluate-sequence max -threshold 5% -format %@ info:`.
- **Lề:** `m = max(24, round(0.04·max(w,h)))`.
- **Cách cắt:** "vuông" có cạnh `max(w,h)+2m`, tâm là tâm hộp, `x0 = Math.round(cx − cạnh/2)`; "hộp" là `x−m, y−m, w+2m, h+2m`. Phần nằm ngoài tranh là đen.
- **Cỡ ra:** `aspect = rộng/cao vùng cắt` (mọi vùng ở đây rộng ≥ cao). Cạnh ngang `long = min(ceilPow2(mét·38·2), ceilPow2(rộng vùng cắt))`; cạnh dọc `max(32, ceilPow2(long/aspect))`.

| id | Tranh trong `S` | Hộp sáng | Cắt | Vùng cắt x, y, rộng×cao | Mét | Ra px | aspect |
|---|---|---|---|---|---|---|---|
| hex | `metal-sigil-hex.v1-try2.png` | 747×791+463+60 | vuông | 409, 28, 855×855 | 7.2 | 1024×1024 | 1 |
| line | `metal-sigil-line.v1-try1.png` | 1643×185+14+371 | hộp | −52, 305, 1775×317 | 14 | 2048×512 | 5.5994 |
| arcs | `metal-sigil-arcs.v1-try2.png` | 817×863+418+29 | vuông | 360, −6, 933×933 | 4.8 | 512×512 | 1 |
| arrow | `metal-sigil-arrow.v1-try2.png` | 1596×169+42+381 | hộp | −22, 317, 1724×297 | 5 | 512×128 | 5.8047 |
| spiral | `metal-sigil-spiral.v1-try2.png` | 620×649+525+120 | vuông, **lật ngang** | 485, 94, 701×701 | 13.5 | 1024×1024 | 1 |
| crack | `metal-crack-star.v1-try1.png` | 1170×818+249+51 | hộp | 202, 4, 1264×912 | 7.5 | 1024×1024 | 1.3860 |
| rift | `metal-rift-groove.v1-try3.png` | 1521×65+76+432 | hộp | 15, 371, 1643×187 | 22 | 2048×256 | 8.7861 |

- **Mét** là cạnh dài khi vẽ trong lab: các mặt phẳng `GroundSigil` ở `sword-skills.ts` dòng 701–709; với crack là sao nứt to nhất 7.5 m (dòng 4725); với rift là `RAIN_RIFT_M = 22` (dòng 281).
- **Lật spiral:** trong tranh, tay xoắn đi ra theo chiều kim đồng hồ (Claude đã trải sang toạ độ cực). Tay giải tích `0.18·e^(0.32θ)`, nơi kiếm K5 cưỡi (`k5Belt`), đi ra ngược chiều. Lật mặt nạ thì chiều xoắn khớp; tranh gốc giữ nguyên.

## Lời giải đã chốt
1. **`src/view/skills/painted-sigils.ts` (mới)**, không chạm `window`, `document`, `location` ở cấp module. Xuất:
   - `SIGIL_MASK_IDS = ["line","arrow","arcs","hex","spiral","crack","rift"] as const`, kiểu `SigilMaskId`; `PAINTED_SIGIL_BASE = "/art-src/lab/vfx/sigils/"`; `SIGIL_PLANES: Readonly<Record<SigilMaskId, number>>` theo cột Mét.
   - `METAL_SIGIL_TINT = { body: [0.58, 0.6, 0.62], core: [1, 1, 1], inner: [1, 0.83, 0.48], innerMix: 0.3 } as const`: Kim là thân trắng bạc (≤ 0.64 một kênh, luật `SIGIL_LIGHT`) với đường trong vàng nhạt mờ.
   - `sigilModeOf(search)`: trả `"code"` chỉ khi `new URLSearchParams(search).get("sigil") === "code"`, còn lại `"painted"`. `paintedPlane(sizeX, aspect)` trả `[sizeX, sizeX / aspect]`.
   - `parseSigilManifest(json: unknown): SigilManifest | null`, với `{ version: 1; masks: ReadonlyMap<SigilMaskId, SigilMaskEntry> }` và mục `{ id, file, md5, metres, aspect, px: readonly [number, number] }`:
     - trả `null` khi gốc không phải object, `version !== 1` hay `channels` khác `{lines:"r", glow:"g", hot:"b"}`;
     - bỏ qua mục hỏng, không ném lỗi: id ngoài `SIGIL_MASK_IDS`, `file` không khớp `/^[a-z0-9][a-z0-9._-]*\.png$/i`, `md5` không đủ 32 hex, `metres` hay `aspect` không hữu hạn > 0, `px` không phải hai số nguyên ≥ 1;
     - trùng id thì giữ mục đầu; không còn mục nào thì trả `null`.
   - `sigilPaths(mode, manifest | null, loaded: ReadonlySet<SigilMaskId>)`: `Record<SigilMaskId, "painted" | "code">`. Một id là `"painted"` khi `mode` là `"painted"`, manifest khác `null`, có mục của id đó và id nằm trong `loaded`.
   - `type PaintedSigils = { masks: ReadonlyMap<SigilMaskId, { texture: THREE.Texture; aspect: number }> }`.
   - `loadPaintedSigils(base = PAINTED_SIGIL_BASE)`:
     - `fetch(base + "manifest.json", { cache: "no-cache" })`; lỗi mạng, HTTP lỗi hay manifest trả `null` thì `console.warn("[sigils] …, analytic sigils")` và trả `null`;
     - mỗi mục nạp bằng `new THREE.TextureLoader().loadAsync(base + file + "?v=" + md5)`, đặt `NoColorSpace`, wrap clamp, `LinearMipmapLinearFilter` / `LinearFilter`, `anisotropy = 8`; mục lỗi thì cảnh báo riêng;
     - id ra `"code"` theo `sigilPaths` thì `console.warn("[sigils] analytic fallback: …")`; id còn lại thì `console.info("[sigils] painted: …")`.
2. **`scripts/vfx/sigil-masks-lib.ts` (hàm thuần) và `scripts/vfx/sigil-masks.ts` (CLI, `npx tsx`).** Chỉ dùng CLI `magick` như `scripts/art/check-frame.mjs`; không thêm gói npm.
   - **Lib xuất:** `SIGIL_SOURCES` (id → `{ file, crop: "square" | "box", flop }` theo bảng); `brightBox(maxCh: Uint8Array, w, h)`; `cropOf(box, crop)`; `ceilPow2`; `maskSize(metres, cropW, cropH)` (mét lấy từ `SIGIL_PLANES` của `src`); và `packChannels(rgb, w, h, sigmaX, sigmaY)`, trả `{ data, hotT, hotShare }`, ảnh RGB với `v = max(R,G,B)/255`:
     - **R** = `clamp((v − 0.03)/0.97, 0, 1)`: các nét;
     - **G** = `min(1, 2.5·Gauss(R))`: quầng mềm. Gauss tách hai trục, bán kính `ceil(3σ)`, ngoài biên tính là 0;
     - **B** = `smoothstep(t, min(1, t + 0.2), v)`: lõi nóng. `t` bắt đầu 0.75 và tăng 0.02 chừng nào `ΣB / count(R > 0.1) > 0.05` và `t < 0.95` (lõi HDR ≤ 5 % diện tích sáng);
     - viền 2 px của mọi kênh về 0; lượng tử hoá `Math.round(x·255)`.
   - **CLI:** cờ `--src` (mặc định `art-src/lab/firefly-sprint-2026-11-05/stills/skills/`), `--out` (mặc định `art-src/lab/vfx/sigils/`), `--force`. Không có `--force` mà tệp ra đã có thì thoát mã 1, không ghi gì. Với mỗi id:
     1. Đọc tranh: `magick f -alpha off -depth 8 rgb:-` (cỡ lấy từ `-format "%w %h" info:`), rồi `brightBox`, `cropOf`, `maskSize`.
     2. Cắt và đổi cỡ: `magick f -alpha off -bordercolor black -border 1024 -crop {cw}x{ch}+{x+1024}+{y+1024} +repage [-flop] -filter Lanczos -resize {W}x{H}! -depth 8 rgb:-`.
     3. `packChannels` với `σx = 0.15·W/metres` và `σy = 0.15·H/(metres/aspect)`: quầng 0.15 m trên cả hai trục.
     4. Ghi `metal-<id>.png` bằng `magick -size {W}x{H} -depth 8 rgb:- -strip -define png:color-type=2 out`, dữ liệu vào stdin. `-strip` bỏ gAMA/iCCP để trình duyệt không đổi màu dữ liệu.
     - Ghi `manifest.json` (thụt 2 dấu cách) chỉ khi đủ 7 ảnh: `{version:1, kind:"sigil-masks", element:"metal", channels:{lines:"r",glow:"g",hot:"b"}, pxPerMetre:38, masks:[{id, file, source, md5, metres, aspect (4 số lẻ), px, crop:[x,y,w,h], flop, hotT, hotShare}]}`. Thiếu tranh nào thì thoát 1, không ghi manifest. In bảng ra stdout.
3. **`fxkit.ts`, `GroundSigil` (dòng 1908–2064) và `SIGIL_FRAGMENT` (dòng 1503–1906).**
   - **Lớp:** giữ `sizeX`, `sizeZ` của constructor trong trường private. Thêm uniform `uMask` (mặc định một `DataTexture` đen 1×1 dùng chung cấp module), `uInner` (Color 1,1,1) và `uInnerMix` (0), cả vào kiểu lẫn literal. Thêm:
     - `setPainted(mask: THREE.Texture | null, aspect = 1)`: bật/tắt define `PAINTED` như `setSolid`; gán `uMask`; `dispose()` geometry cũ rồi đặt `new THREE.PlaneGeometry(...paintedPlane(sizeX, aspect))`, hoặc `(sizeX, sizeZ)` khi `null`. Không dùng `mesh.scale`: `place()` và các hiệu ứng ghi đè scale;
     - `get painted(): boolean`.
   - **Shader:** khai `uniform sampler2D uMask; uniform vec3 uInner; uniform float uInnerMix;` trong `#ifdef PAINTED`, trước `varying vec2 vUv;` (dòng 1526). Sau `float mot = 0.0;` (dòng 1689) thêm `vec3 coreC = uCore; float fadeK = uFade;`. Đổi `#if defined(HEX)` (dòng 1691) thành `#elif defined(HEX)` và chèn trước nó:
     ```glsl
     #if defined(PAINTED)
       vec2 q = p;
     #if defined(SPIRAL)
       q = rot2(p, -uPhase);              // the painted arms turn with uPhase like the analytic ones
     #endif
       vec3 s = texture2D(uMask, q * 0.5 + 0.5).rgb;   // r lines, g glow, b hot
     #if defined(LINE) || defined(ARROW)
       float order = (p.x + 1.0) * 0.5;   // from the caster
     #elif defined(CRACK)
       float order = r;                   // from the impact
     #else
       float order = fract((atan(q.y, q.x) + PI) / (2.0 * PI));
     #endif
       float rev = revealSoft(order, uReveal, 0.05);
       float lit = 1.0;
     #if defined(ARCS)
       lit = 0.25 + 0.75 * clamp(uCount - floor(order * 3.0), 0.0, 1.0);
     #endif
       light = (s.r + s.g * 0.35) * rev * lit * (0.85 + 0.15 * n);
       core = s.b * rev * lit;
       ink = s.g * rev;
       heatL = s.r * uHeat * 0.5 * rev;
       heatC = s.b * uHeat * rev;
       ashL = s.g * 0.6 * rev;
       coreC = mix(uCore, uInner, uInnerMix);
       fadeK = smoothstep((1.0 - uFade) * 1.1 - 0.1, (1.0 - uFade) * 1.1, max(s.r, s.g * 0.6)); // erosion: faint parts go first, everything gone at uFade = 0
     ```
     - **Đuôi shader:** dòng 1869 thành `#if defined(LINE) || defined(ARROW) || defined(PAINTED)`; dòng 1876 `uCore * ca` thành `coreC * ca`; dòng 1902–1903 hai chỗ `uFade` thành `fadeK`.
     - Đường `SOLID` giữ nguyên: chỉ ấn chân dùng nó, và ấn chân chưa có tranh trong phiếu này.
     - Không có `PAINTED` thì kết quả phải giống từng điểm ảnh bản cũ.
     - Đường tranh không vẽ hoạ tiết ngọc `biRing`/`cloudCurl`: đó cũng là hình vẽ bằng code.
4. **`sword-rain.ts`, `GroundMarks` (dòng 347–530).**
   - **Vertex:** khai `uniform vec2 uAspect;` (x sao nứt, y rãnh) trong `#ifdef PAINTED`; khi có `PAINTED`, dòng 361 thành `vec2 l = position.xy * vec2(iSize.x, iSize.x / (iPos.w < 0.5 ? uAspect.x : uAspect.y));`. Các lệnh `push` không đổi.
   - **Fragment:** khai `uniform sampler2D uStarMask, uRiftMask; uniform vec3 uBody, uCoreC, uInner; uniform float uInnerMix;` trong `#ifdef PAINTED`, và đầu `main()` (dòng 385) thêm khối dưới, **bọc trong `{ … }`** ngay sau `#ifdef PAINTED` và trước `#endif` (đường cũ khai lại `rev`, `add`, `a` ở dòng 424, 443, 444 cùng tầm; GLSL cấm khai lại):
     ```glsl
     #ifdef PAINTED
     {
       vec2 uv = vec2(vL.x, -vL.y) * 0.5 + 0.5;  // local +y is world +z here: flip so the mask reads as on GroundSigil
       vec3 s = mix(texture2D(uRiftMask, uv).rgb, texture2D(uStarMask, uv).rgb, step(vKind, 0.5));
       float rev = 1.0 - smoothstep(vSize.w - 0.04, vSize.w, abs(vL.x));
       vec3 add = uBody * (s.r + s.g * 0.35) * vLook.w + mix(uCoreC, uInner, uInnerMix) * s.b * vLook.y;
       float a = clamp(s.g * vLook.z, 0.0, 1.0);
       float er = smoothstep((1.0 - vLook.x) * 1.1 - 0.1, (1.0 - vLook.x) * 1.1, max(s.r, s.g * 0.6)) * rev; // erosion reaches 0 as vLook.x -> 0 (slow decay, no pop)
       gl_FragColor = vec4((uInk * a + add) * er, a * er);
       return;
     }
     #endif
     ```
   - **Lớp** (vẫn một lệnh vẽ): thêm các uniform trên vào literal ở dòng 480 (ảnh mặc định đen 1×1, `uAspect` là (1,1)). Thêm:
     - `setPainted(star: THREE.Texture | null, starAspect, rift: THREE.Texture | null, riftAspect)`: chỉ bật `PAINTED` khi có **cả hai** ảnh;
     - `setTint(body: THREE.Color, core: THREE.Color, inner: readonly number[], innerMix: number)`, chép giá trị vào uniform; và `get painted()`.
5. **`sword-skills.ts`.**
   - Import từ `./painted-sigils` cạnh các import ở dòng 49–62. Thêm `private readonly markBody = new THREE.Color()` và `markCore` cạnh `tmpCol` (dòng 506).
   - **`setPaintedSigils(p: PaintedSigils | null): void` (public):** mỗi sigil gọi `setPainted(m?.texture ?? null, m?.aspect ?? 1)` theo cặp `line` → `sigLine`, `arrow` → `sigArrow`, `arcs` → `sigArcs`, `hex` → `sigHex`, `spiral` → `sigSpiral`, `crack` → `sigCrack` và `sigCrackS`; `rainMarks.setPainted(...)` với hai mục `crack` và `rift`; cuối cùng gọi `this.applyColours(this.weaponDef)`.
   - **Cuối constructor**, sau `this.applyColours(this.weaponDef);` (dòng 755): khi `typeof location !== "undefined"`, nếu `sigilModeOf(location.search) === "painted"` thì `void loadPaintedSigils().then((p) => this.setPaintedSigils(p))`, còn lại thì `console.info("[sigils] ?sigil=code: analytic sigils")`. Test trên node không có `location`, nên test vẫn đi đường cũ.
   - **`sigilColours` (dòng 938):** sau hai dòng hiện có, luôn đặt `uInner` từ `METAL_SIGIL_TINT.inner`. Nếu `sig.painted && this.kit.id === "metal"` thì đặt `uColor` từ `.body`, `uCore` từ `.core` và `uInnerMix = .innerMix`; ngược lại `uInnerMix = 0` (hệ khác giữ màu theo chiêu trên cùng mặt nạ).
   - **`applyColours` (dòng 913):**
     - Kim: đặt `markBody` và `markCore` từ `METAL_SIGIL_TINT`, rồi `rainMarks.setTint(markBody, markCore, .inner, .innerMix)`;
     - hệ khác: `markBody.copy(this.tmpSigil("k5", false))`, rồi `markCore.copy(this.tmpSigil("k5", true))`, rồi `setTint(…, 0)`. Gọi `tmpSigil` hai lần riêng, vì nó dùng chung `tmpCol`.
6. **Test `tests/view/painted-sigils.test.ts`** (môi trường node, không cài gói):
   - `sigilModeOf`: `""` và `"?sigil=x"` cho `painted`; `"?sigil=code"` và `"?element=fire&sigil=code"` cho `code`.
   - `parseSigilManifest` (manifest viết trong test): đủ 7 mục thì đọc đúng; `version: 2` hoặc `channels` sai thì `null`; `file` có `/`, `aspect` âm, id lạ hay md5 ngắn thì mục bị bỏ; trùng id thì giữ mục đầu; không có mục thì `null`.
   - `paintedPlane(14, 5.5994)` ≈ `[14, 2.5003]` (±1e-3).
   - `sigilPaths`: `code` thì mọi id là `code`; manifest `null` thì mọi id là `code`; thiếu `rift` trong `loaded` thì chỉ `rift` là `code`.
   - `cropOf` và `maskSize` khớp 7 hàng của bảng.
   - `packChannels`: ảnh 16×16 đen thì mọi byte là 0; một vạch `v = 1` thì R = 255 trên vạch, viền 2 px bằng 0, `hotT` dừng ở 0.95.
   - **Ảnh thật** (`it.skipIf` khi thiếu tệp): `brightBox` của 7 tranh khớp cột "Hộp sáng"; manifest thật đủ 7 id, `px` và `aspect` khớp bảng (±1e-3), mọi tệp có thật.

## Kiểm
- **Script:** `cd W && npx tsx scripts/vfx/sigil-masks.ts`. Chạy lại không có `--force` thì phải thoát 1 và không đổi tệp nào. Chạy với `--force` thì md5 phải giống lần đầu.
- **Xem bằng mắt:** mở cả 7 PNG. Hình đủ, không bị cắt, nền đen, spiral đã lật.
- **Kiểu và test:**
  - `cd W && npx tsc --noEmit` sạch;
  - `cd W && npx vitest run tests/view/painted-sigils.test.ts` qua;
  - `cd W && npx vitest run tests/lab tests/view` qua. Mốc Claude chạy lúc 20:33 ngày 06/11 trên `1b9461e`: tsc sạch, **44 tệp, 500 test qua**. Sau phiếu: 45 tệp, 500 cộng số test mới.
- **Phạm vi:** `git -C W status --short` chỉ hiện các file được ghi.
- **Không chạy trình duyệt.** Claude sẽ so A/B trong lab (mặc định là bản tranh, `?sigil=code` là bản cũ).

## Xong khi
Các lệnh kiểm qua. Báo cáo ghi:
- file đã sửa, số dòng thêm và bớt; kết quả từng lệnh kiểm;
- bảng 7 mặt nạ: vùng cắt, px, aspect, `hotT`, `hotShare`, md5, MB GPU (RGBA8 có mipmap, `W·H·4·4/3`; dự kiến tổng khoảng 27 MB); mọi chỗ lệch so với bảng của phiếu, kèm lý do.

## Hết hạn mức
Chỉ khi thật sự chạm giới hạn: giữ file, viết báo cáo phần đã xong, dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`). Không chạm giới hạn thì không ghi dòng này.

## Ghi chú từ phản biện (đã sửa 2 lỗi bắt buộc ở trên)
- Kiểm phạm vi: `git status --short` vốn đã có `?? art-src` và `?? node_modules` (hai liên kết có sẵn); ngoài hai dòng đó mới tính là file lạ.
- Đọc ảnh thô bằng `execFileSync` thì đặt `maxBuffer` lớn (mỗi tranh khoảng 4,7 MB, vượt mặc định 1 MiB).
- Test ảnh thật tự gọi `magick` (lib chỉ có hàm thuần) và bỏ qua khi máy thiếu `magick`.
- `hotT` cộng dồn ra `0.9500000000000002`: test dùng `toBeCloseTo(0.95)`.
- Bọc cả `fetch` lẫn `res.json()` trong try/catch, để manifest hỏng cũng quay về bản code.
- Claude tự kiểm trong trình duyệt sau khi Codex xong (không có vòng phản biện 2: hai lỗi trên đã sửa đúng câu chữ phản biện đưa).
