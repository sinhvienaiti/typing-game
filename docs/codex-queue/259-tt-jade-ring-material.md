# Phiếu 259 · Tu Tiên · Code: vòng ngọc Clear Wind thành ngọc trắng viền vàng nhạt bằng mặt nạ hình học (gói CX-C)

> **BẢN NHÁP, CHƯA XONG.** Trạng thái duyệt hai lần và phần còn thiếu ở cuối phiếu (mục "Trạng thái duyệt"). Không đưa vào làn Codex khi dòng này còn.

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`): shader lưỡi, shader impostor, đo vòng lúc nạp, test. Lời giải đã chốt ở phiếu này. Codex không thiết kế lại màu, dải hay cách đo; chỗ nào không làm được thì ghi báo cáo.

**Báo cáo:** `docs/codex-queue/259-report.md` (tiếng Việt).

**Nguồn:** `docs/games/tu-tien/skills/INTEGRATION_PLAN_2026-11-04.md` (ghi chú đầu, §3 dòng CX-C, §4 đoạn "Vòng ngọc", §2.8); `docs/games/tu-tien/skills/SWORD_AURA.md` (Q4, `AuraAnchors`). Bàn với trợ lý: `docs/games/tu-tien/skills/source/jade-ring-chatgpt-2026-11-04.md`, `jade-ring-gemini-2026-11-04.md`. Kế hoạch §7 gọi phiếu này là `258-tt-jade-ring-material`; ghi chú đầu kế hoạch dời số lên một bậc (CX-A → 257), nên CX-C là **259**.

## Bối cảnh

- **Anh chốt Q4 (04/11/2026):** vòng ngọc của Clear Wind thành **ngọc trắng viền vàng nhạt, "như ảnh đã duyệt"**. Không vẽ lại texture. Đổi chất liệu bằng mặt nạ hình học trong shader, rồi gửi anh ảnh trước và sau. Chỉ khi anh chê mới nhờ AI-vẽ sửa texture UV.
- **Ảnh đã duyệt:** `games/immortality-cultivation/art-src/weapons/clearwind-src3q.v4-try1.png` (nguồn Tripo của model đang dùng, changelog `2026-11-03-lab-clear-wind.md` dòng 3; thiết kế trưng bày `x5-clearwind-heirloom.v1-try1.png`). Changelog `2026-11-03-lab-real-swords.md` ghi lệch: "Vòng ngọc của model Tripo hiện ra màu bạc như crôm, còn ảnh đã duyệt là ngọc trắng viền vàng."
  - Trong ảnh: vòng là đĩa dày ngọc trắng, lỗ tròn hở; một chỉ vàng nhạt chạy ở mép lỗ và một chỉ ở mép ngoài đĩa; ngoài cùng là vành bạc bóng mảnh; trên đĩa có hai hạt ngọc xanh nhạt và mây sứ trắng viền vàng nhạt.
  - **Màu Claude đo trên ảnh** (vùng 220 × 220 quanh vòng, sRGB → tuyến tính):

    | Vai | Trung vị | p25 | p90 | Tuyến tính (trung vị) |
    |---|---|---|---|---|
    | Ngọc trắng (độ bão hòa < 0,06, sáng > 0,8) | `#DFDDDF` | `#D7D4D4` | `#F5F4F7` | (0,738; 0,723; 0,738) |
    | Vàng nhạt (sắc 30–50°, bão hòa 0,25–0,65, sáng > 0,78) | `#D4B793` | `#CEAE89` | `#EACB9D` | (0,658; 0,474; 0,292) |
    | Hạt ngọc (đã có, `CLEAR_WIND_JADE`) | `#C4E2CF` | | | (0,552; 0,761; 0,624) |

    Mẫu ngọc trắng lẫn một phần vành bạc (cũng trắng, ít bão hòa). Vàng nhạt cách xa vàng tiền `#FFC83A` (sắc 44°, bão hòa 0,77) và màu gõ `#7FF5E0`.
- **Mã hiện tại** (`games/immortality-cultivation`, HEAD `bc94110`):
  - `src/view/skills/sword-material.ts`: `patchSwordMaterial(material, { bladeFrom, jade })` vá vật liệu PBR của chính GLB qua `onBeforeCompile`. Chunk `JADE` (sau `#include <color_fragment>`) tính `swJade` theo **sắc** trên map màu: bắt hai hạt ngọc xanh, **không** bắt vòng crôm. `EMIT` cộng ánh ngọc `swJadeE`; `OUTGOING` chỉ cho `swJadeE` lấp phần trống dưới độ sáng 0,95 (không bloom). Varying `vSwP = position` là không gian lưỡi đơn vị (chắn ở y = 0, mũi y = 1, chuôi y < 0, mặt lưỡi quay ±Z).
  - `src/view/skills/blades.ts`: `guardBand()` tìm dải chắn (Clear Wind: chính là vòng). `auraAnchorsOf()` cho `AuraAnchors.ring = { y: (g0 + g1) / 2, r: guardHalf }`; `guardHalf` là |x| lớn nhất trong dải, có thể gồm cả mây sứ thò ra. Bán kính lỗ chưa đo ở đâu. `modelOf()` gọi `patchSwordMaterial`, dùng cho model đầy đủ (kiếm chủ) và LOD 3.200 tam giác (kiếm giữa); `overlayModel()` vá lại một bản sao.
  - `src/view/skills/real-swords.ts`: kiếm xa là impostor nướng từ cùng GLB (`clear-wind-impostor.json`: ô 512 × 128, 4 hàng lăn 0/30/60/90°, `ringU` 0,31109, `ringR` 0,08008, `rollWidth` [1; 0,8966; 0,5862; 0,3793]). `SwordAtlasMeta.ringU`, `ringR` đã khai báo mà chưa dùng.
  - Three.js 0.170.0. Trong `meshphysical.glsl.js`: `color_fragment` (dòng 173) → `roughnessmap_fragment` (177, khai báo `roughnessFactor`) → `metalnessmap_fragment` (178, khai báo `metalnessFactor`) → … → `emissivemap_fragment` (183) → `lights_physical_fragment` (186, đọc `diffuseColor`, `roughnessFactor`, `metalnessFactor`).

## Lời giải đã chốt

**Tóm tắt:** đo vòng ngọc một lần lúc nạp (tâm, bán kính lỗ, bán kính ngoài) từ chính hình học; trong shader lưỡi, một mặt nạ theo **khoảng cách tới tâm vòng trong mặt phẳng lưỡi** chia vòng thành bốn dải (chỉ vàng mép lỗ, đĩa ngọc trắng, chỉ vàng mép ngoài, vành bạc giữ nguyên); trong dải ngọc thì đổi `diffuseColor`, `metalnessFactor`, `roughnessFactor` sang ngọc trắng, trong dải chỉ thì sang vàng nhạt; hạt ngọc (mặt nạ sắc cũ) giữ nguyên. Impostor dùng `ringU`, `ringR` để tô lại vùng vòng trong ô atlas. Ngoài vòng, mọi phép tính giữ nguyên từng bit.

### 1. Đo vòng lúc nạp (`blades.ts`)

- Hàm mới `jadeRingOf(geometry, guard: readonly [number, number]): JadeRing | null`, kiểu mới:

  ```ts
  /** Clear Wind's jade ring on the unit blade, measured at load (SWORD_AURA Q4; ticket 259). */
  export interface JadeRing {
    readonly y: number;    // the hole's centre (unit y)
    readonly rIn: number;  // the hole's radius (unit)
    readonly rOut: number; // the disc's outer radius, silver rim included (unit)
  }
  ```

- Cách đo (chỉ dùng tam giác, không dùng texture):
  1. Lấy mọi tam giác có ít nhất một đỉnh với y trong `[guard[0] − 0,02; guard[1] + 0,02]`. Chiếu xuống mặt phẳng x–y (bỏ z).
  2. Vẽ chúng vào lưới chiếm chỗ 256 × 256 phủ hình vuông `[−h; h] × [cy0 − h; cy0 + h]`, với `cy0 = (guard[0] + guard[1]) / 2`, `h = 1,25 × guardHalf` (tô tam giác theo ô, đủ bảo thủ).
  3. **Lỗ:** loang (flood fill, 4 hướng) từ ô gần `(0; cy0)` nhất mà còn trống. Nếu ô đó không trống hoặc vùng loang chạm biên lưới thì trả `null` (không có lỗ kín: không đổi gì). Tâm `y` = trọng tâm y của vùng lỗ; `rIn = sqrt(diện tích lỗ / π)`.
  4. **Bán kính ngoài:** bắn 64 tia đều góc từ tâm lỗ ra ngoài; trên mỗi tia lấy khoảng cách tới ô chiếm chỗ **cuối cùng của đoạn liền** bắt đầu từ mép lỗ. `rOut` = **trung vị** của 64 khoảng cách đó (mây sứ, khâu nối lưỡi và cổ chuôi thò ra ở vài góc nên trung vị bỏ được chúng).
  5. Kiểm hợp lệ: `0 < rIn < rOut ≤ guardHalf + 1e-4` và `rOut − rIn ≥ 0,01`; sai thì trả `null` và `console.warn` một lần.
- `SwordModel` có thêm `readonly jadeRing: JadeRing | null`. `modelOf()` chỉ đo khi `ring === true` (chỉ Clear Wind có `motif.ring`). **Không đổi `AuraAnchors.ring`** (các lớp hào quang đang đọc nó; đổi sẽ làm lệch hào quang).
- LOD dùng chung kết quả đo của model đầy đủ (cùng hệ lưỡi đơn vị qua `bladeMap`), để kiếm chủ và kiếm giữa cùng một vòng. Thanh kiếm thay thế (`standInModel`) không có vòng.

### 2. Shader lưỡi (`sword-material.ts`)

- `SwordMaterialOptions` thêm `readonly ring?: JadeRing | null`. Uniform riêng mỗi vật liệu `uSwRing: vec4(y, rIn, rOut, có ? 1 : 0)`.
- Bảng dùng chung, xuất ra để lab bật tắt và để chỉnh sau:

  ```ts
  /** White jade with a pale gold rim (owner Q4, 04/11/2026; colours sampled from clearwind-src3q.v4-try1.png). */
  export const JADE_RING_LOOK = {
    on: { value: 1 },                                          // ?jadeRing=off → 0 (before/after)
    jade: { value: new THREE.Vector3(0.738, 0.723, 0.738) },   // white jade albedo (#DFDDDF, linear)
    gold: { value: new THREE.Vector3(0.658, 0.474, 0.292) },   // pale gold (#D4B793, linear)
    bands: { value: new THREE.Vector4(0.07, 0.80, 0.88, 0.0) },// t: gold line until .07, jade until .80, gold until .88, silver rim after
  };
  ```

- **Mặt nạ** (GLSL, một chunk mới `RING` chèn **sau `#include <metalnessmap_fragment>`**, để `roughnessFactor` và `metalnessFactor` đã có, và sau `JADE` để `swC` và `swJade` còn là màu texture gốc):

  ```glsl
  float swRing = 0.0; float swRingGold = 0.0; float swRingJade = 0.0;
  if (uSwRing.w * uSwRingOn > 0.5) {
    float swRd = length(vec2(vSwP.x, vSwP.y - uSwRing.x));
    float swRt = (swRd - uSwRing.y) / max(uSwRing.z - uSwRing.y, 1e-4);   // 0 at the hole's edge, 1 at the outer edge
    float swAa = fwidth(swRt) * 1.5 + 1e-4;
    float swIn = smoothstep(-swAa, swAa, swRt) * (1.0 - smoothstep(uSwRingBands.z - swAa, uSwRingBands.z + swAa, swRt));
    float swJd = smoothstep(uSwRingBands.x - swAa, uSwRingBands.x + swAa, swRt) * (1.0 - smoothstep(uSwRingBands.y - swAa, uSwRingBands.y + swAa, swRt));
    float swKeep = 1.0 - smoothstep(0.3, 0.6, swJade);                       // the beads keep their own jade
    swRingJade = swJd * swKeep;
    swRingGold = max(swIn - swJd, 0.0) * swKeep;
    swRing = swRingJade + swRingGold;
  }
  if (swRing > 0.0) {
    float swL = dot(swC, vec3(0.2126, 0.7152, 0.0722));
    float swDet = clamp(0.82 + 0.45 * (swL - 0.5), 0.7, 1.08);           // keep the carving, flatten the chrome's mirror swings
    vec3 swAlb = uSwRingJade * swDet * swRingJade + uSwRingGold * swDet * swRingGold;
    diffuseColor.rgb = mix(diffuseColor.rgb, swAlb / max(swRing, 1e-4), swRing);
    metalnessFactor = mix(metalnessFactor, swRingGold / max(swRing, 1e-4), swRing);   // jade 0, gold 1
    roughnessFactor = mix(roughnessFactor, mix(0.34, 0.28, swRingGold / max(swRing, 1e-4)), swRing);
  }
  ```

  Ngoài vòng `swRing = 0` và khối `if` không chạy, nên mọi giá trị khác giữ nguyên từng bit. Chế độ `furnace` (Fire) đã nhân `uSwChar` vào `diffuseColor` ở `JADE`; trong vòng, `mix` thay hẳn albedo, nên **vòng không bị cháy đen**: ngọc trắng vẫn là dấu nhận diện Clear Wind trong lửa (lửa và đèn chiêu rọi lên nó).
- **Ánh trong của ngọc** (giả trong mờ, không bloom): trong `EMIT`, sau khi tính `swJadeE`, cộng `swJadeE += uSwRingJade * swRingJade * (0.06 + 0.10 * swGlow + 0.25 * min(swFlash, 1.0));`. Vì nằm trong `swJadeE`, `OUTGOING` vẫn kẹp nó dưới độ sáng 0,95. Chế độ `furnace` giữ nguyên dòng này (ánh trắng ấm của ngọc trong lửa), không đổi thành than.
- Uniform `uSwRingOn`, `uSwRingJade`, `uSwRingGold`, `uSwRingBands` trỏ vào `JADE_RING_LOOK` (như `SWORD_LOOK`); `customProgramCacheKey` giữ `"real-sword"` (cùng một chương trình cho mọi vũ khí; vũ khí không có vòng có `uSwRing.w = 0`).

### 3. Impostor (`real-swords.ts`)

- Uniform mới trong cả `FRAGMENT` và `FRAGMENT_HALO`: `uRing: vec4(ringU, ringR, cellW / cellH, on)`; `on = 0` khi meta không có `ringU`/`ringR` (bản nướng cũ) hoặc `JADE_RING_LOOK.on = 0`. Thêm `uRingJade`, `uRingGold` trỏ vào `JADE_RING_LOOK`.
- Mặt nạ trong ô, tính **cho từng hàng** rồi trộn theo `k` như màu: hàng `row` có góc lăn `rolls[row]`; chiều cao của vòng trên ô co theo `cos(roll)` (sàn 0,12 để hàng nhìn cạnh không chia 0):

  ```glsl
  float ringMask(float row) {
    float c = max(cos(radians(uRolls[int(row)])), 0.12);
    vec2 p = vec2((vUv.x - uRing.x) / uRing.y, (vUv.y * 0.5) / (uRing.y * uRing.z) / c);
    float t = length(p);                         // 1 at the outer edge
    return 1.0 - smoothstep(0.86, 0.94, t);      // jade disc + inner gold; the silver rim stays the bake
  }
  ```

  (`vUv.y ∈ [−1; 1]` phủ cả chiều cao ô, nên nửa chiều cao ô = 0,5 đơn vị ô; `uRing.y × uRing.z` là bán kính vòng đổi sang đơn vị chiều cao ô.) Nhân với `(1.0 − m.g)` (bỏ điểm ảnh lưỡi) và `step(1e-3, m.a)`.
- Tô lại (ảnh nướng là premultiplied, nên làm trên màu chưa nhân alpha): `vec3 base = c.rgb / max(c.a, 1e-3); float L = dot(base, vec3(0.2126, 0.7152, 0.0722)); vec3 jadeLit = uRingJade * clamp(0.55 + 0.6 * L, 0.6, 1.05);` rồi `col = mix(col, jadeLit * c.a * uGain * uLight, mask)`, đặt **trước** các bước `furnace`, chớp và đường mép; trong `furnace` không nhân `uChar` vào phần vòng (như shader lưỡi). Ở kiếm xa chỉ vàng nhỏ dưới 1 px nên không vẽ; vành ngoài giữ bạc của ảnh nướng.
- `rolls` đưa vào uniform `uRolls[4]` (hoặc tính sẵn `cos` thành `vec4`), không cấp phát mỗi khung.

### 4. Lab (`src/lab/skills-main.ts`)

- Cờ `?jadeRing=off` đặt `JADE_RING_LOOK.on.value = 0` (vòng như cũ, để chụp trước và sau). Mặc định bật. Ghi vào khối chú thích cờ đầu tệp như `?bladeHeat`.

## Làm ở đâu

- **Worktree riêng của Codex:** `games/.wt-immortality-cultivation-codex`, nhánh `codex/jade-ring-material`, gốc `bc94110`. Claude tạo trước khi chạy phiếu:
  `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-immortality-cultivation-codex -b codex/jade-ring-material bc94110`, rồi symlink `node_modules` như phiếu 255.
- Không ghi gì trong `games/immortality-cultivation/` (agent khác đang sửa ở đó).

### Được ghi
- `games/.wt-immortality-cultivation-codex/src/view/skills/sword-material.ts`, `blades.ts`, `real-swords.ts`;
- `games/.wt-immortality-cultivation-codex/src/lab/skills-main.ts` (chỉ cờ `?jadeRing`);
- `games/.wt-immortality-cultivation-codex/tests/view/jade-ring.test.ts` (mới);
- `games/.wt-immortality-cultivation-codex/scripts/visual/ring-parity.mjs` (mới, công cụ so ảnh cho Claude chạy);
- `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-lab-jade-ring.md`;
- `docs/codex-queue/259-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa texture, GLB, atlas impostor, `art-src/**`, `public/**`, script Blender; chạy Blender.
- Sửa `src/sim/**`, `src/content/**`, `src/kit/**`, golden, các lớp hào quang (`aura-mantle.ts`, `sword-aura.ts`, `element-*.ts`) và `AuraAnchors.ring`.
- Đổi đường mép, `edgeField`, `HEAT_BAND`, `SWORD_LOOK`, `OUTGOING` ngoài phần ghi ở trên.
- Chạy dev server, mở trình duyệt, tải gói hay ảnh.
- Cấp phát bộ nhớ mỗi khung.

## Việc

1. `blades.ts`: `JadeRing`, `jadeRingOf()` đúng §1; `SwordModel.jadeRing`; `modelOf()` đo khi `ring`, LOD dùng kết quả của model đầy đủ; truyền vào `patchSwordMaterial` qua `look.ring` (để `overlayModel()` vá lại cũng có vòng).
2. `sword-material.ts`: `JADE_RING_LOOK`, uniform, chunk `RING` sau `metalnessmap_fragment`, dòng ánh ngọc trong `EMIT`, đúng §2. Thêm kiểm như hai `throw` sẵn có: nếu chuỗi `#include <metalnessmap_fragment>` không còn thì `throw`.
3. `real-swords.ts`: `uRing`, `uRolls`, mặt nạ và tô lại đúng §3 trong cả hai chương trình; meta thiếu `ringU`/`ringR` thì tắt.
4. `skills-main.ts`: cờ `?jadeRing=off`.
5. `scripts/visual/ring-parity.mjs`: đọc hai thư mục ảnh của `lab-element-parity.mjs` (`raw-before`, `raw-after`) và một thư mục mặt nạ vòng (ảnh `drawSwordMask`, kênh xanh; Claude chụp), giãn mặt nạ `DILATE` px (mặc định 3), in JSON: theo từng ảnh, số điểm ảnh ngoài mặt nạ khác nhau (Δ > 0 ở bất kỳ kênh nào), Δ lớn nhất, và trong mặt nạ: tỉ lệ điểm ảnh vòng còn phủ (alpha hoặc khác nền) trước và sau. Chỉ dùng Node và `pngjs` nếu đã có trong `node_modules`; không có thì đọc PNG bằng `zlib` có sẵn.
6. Test `tests/view/jade-ring.test.ts` (không cần trình duyệt):
   - một vòng tổng hợp (annulus tam giác hóa, `rIn` 0,05, `rOut` 0,09, tâm y 0, cộng một "mây" thò ra 0,13 ở một góc và một lưỡi từ y 0,1 tới 1): `jadeRingOf` trả `|y| ≤ 0,004`, `|rIn − 0,05| ≤ 0,004`, `|rOut − 0,09| ≤ 0,004`;
   - đĩa đặc không lỗ → `null`; `guardBand` mặc định `[−0,02; 0,02]` không có hình → `null`;
   - `patchSwordMaterial` với vật liệu giả: chuỗi shader sau `onBeforeCompile` chứa chunk `RING` ngay sau `metalnessmap_fragment`, và `uSwRing.w = 0` khi không có vòng;
   - `JADE_RING_LOOK` mặc định đúng các số ở §2.
7. Changelog tiếng Việt: làm gì, cờ `?jadeRing=off`, các số, cách thử.

## Kiểm bắt buộc

**Codex chạy** (trong `games/.wt-immortality-cultivation-codex`, ghi lệnh và kết quả vào báo cáo):
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `node node_modules/vitest/vitest.mjs run`: mọi test qua; ghi số test trước và sau; test golden không đổi.
3. `node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-259-dist`: build qua; xóa thư mục sau khi kiểm.
4. `git -C games/.wt-immortality-cultivation-codex diff --stat`: chỉ có các file được ghi.
5. In ra (bằng một lệnh `node` chạy hàm đo trên GLB thật nếu nạp được trong Node; không thì ghi "không đo được trong sandbox") `y`, `rIn`, `rOut` của `clear-wind.glb` và `clear-wind-swarm.glb`.

**Claude chạy khi nhận** (Codex không có server hay trình duyệt; bản cố định không HMR, High, 1920 × 1080, DPR 1, qua `.local/bin/heavy.sh --gpu`):
6. **Vòng giữ ≥ 95 % điểm ảnh** ở mọi khung của `lab-element-parity.mjs` (k1, k1z, k7, k5): số điểm ảnh của vùng vòng (mặt nạ `drawSwordMask` kênh xanh) còn phủ sau khi đổi so với trước ≥ 95 %, Metal và Fire.
7. **Metal trùng khít ngoài vùng vòng:** `PHASE=before QS="&jadeRing=off"` và `PHASE=after` (cùng `ONLY`, cùng kế hoạch), `ELEMENT=metal`; `ring-parity.mjs` với mặt nạ giãn 3 px: **0 điểm ảnh khác** ngoài mặt nạ. Nếu bloom làm lệch, ghi số điểm và Δ lớn nhất; chấp nhận chỉ khi Δ ≤ 2/255 và nằm trong 12 px quanh vòng (vầng bloom), không thì sửa. Làm lại với `ELEMENT=fire`, cùng ngưỡng.
8. **Màu vòng so với ảnh đã duyệt:** cận cảnh phím 1 (`k1z`), Metal: trung vị OKLab của điểm ảnh đĩa ngọc cách `#DFDDDF` ΔE ≤ 0,08 và độ bão hòa < 0,08; chỉ vàng (nếu ≥ 2 px) có sắc 25–45°. Không vượt độ sáng 0,95 trong vòng (không bloom mới): số điểm ảnh > 1 trong bộ đệm sáng của bloom quanh kiếm không tăng so với `jadeRing=off`.
9. **Thời gian:** `lab-element-perf.mjs`, phím 7 High p95, bật và tắt `jadeRing` xen kẽ A/B/B/A: chênh ≤ 0,05 ms; mọi cửa sổ ≤ 11,5 ms.
10. **Ảnh trước và sau cho anh** vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/jade-ring/` (skill `review-folder`, có `ABOUT.md`, chạy `node scripts/review-index.mjs`): cận cảnh phím 1 Metal và Fire, camera chơi phím 7, đặt cạnh ảnh đã duyệt. Bản gửi anh vào `owner-review/2026-11-04/tu-tien/jade-ring/`. Xóa khung thô sau khi đo.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Thay đổi trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–4, chạy Kiểm 6–10, gửi anh ảnh trước và sau. Chỉ khi anh duyệt màu mới gộp vào `main`. Anh chê thì chuyển sang vẽ lại texture UV (kế hoạch §4), không chỉnh mãi shader.
- Báo cáo ghi: từng việc 1–7 đã làm ở đâu (tệp và hàm); số đo `y`, `rIn`, `rOut`; chỗ phải làm khác và vì sao; kết quả Kiểm 1–5.

## Ngoài phạm vi
- Kiếm cầm tay trong lab (`src/lab/hand-sword.ts`) có vật liệu riêng, chưa dùng `patchSwordMaterial`; vòng của nó vẫn crôm. Claude quyết sau khi anh duyệt màu (một phiếu nhỏ dùng lại chunk `RING`).
- Vẽ lại texture, nướng lại atlas impostor.

## Trạng thái duyệt (13:50, 04/11/2026, hết giờ)

**BẢN NHÁP, CHƯA XONG.** Lời giải ở trên là bản Claude viết từ mã và ảnh đã duyệt, **trước** khi có kết quả duyệt hai lần. Chưa đủ quy trình nên chưa đưa Codex.

- **ChatGPT** (Chat, thinking High; chat `https://chatgpt.com/c/6aead1ae-67e4-83ec-983f-339fe8bb6531`): đã trả lời lần đầu (34.365 ký tự, nghĩ 6 phút 34 giây). **Lượt tự duyệt 1: `VERDICT: FAIL`** (13:50). Bản sửa đầy đủ còn đang viết khi dừng; bản ghi chỉ có phần đầu. Chưa có PASS nào. Các lỗi nó tự nêu (cần kiểm, nhiều ý cũng chạm bản nháp này):
  1. đo vòng bằng gộp khoảng theo tia có thể lấp lỗ bằng tam giác của khâu nối, chuôi hay mây (bản nháp loang trên lưới chiếm chỗ cũng có rủi ro này nếu tam giác chiếu phủ lỗ);
  2. tìm vành bạc theo đổi pháp tuyến chưa đủ cụ thể;
  3. dùng `#ifdef` mà TypeScript không định nghĩa macro (bản nháp dùng uniform `uSwRing.w`, không dính);
  4. mặt nạ bán kính có thể bắt lưỡi, chuôi, khâu, mây hay hạt nằm cùng vùng (bản nháp cũng cần thêm điều kiện ngoài mặt nạ sắc);
  5. bỏ ý giảm normal map 15 % (bản nháp không làm);
  6. đường Fire chưa ghi đủ: `char`, dải nhiệt, viền fresnel, chớp, ánh hạt, hệ số ánh sáng;
  7. không được miễn vòng khỏi dissolve (bản nháp giữ dissolve);
  8. elip impostor theo `rollWidth` chưa có căn cứ.
- **Bản ghi:** `docs/games/tu-tien/skills/source/jade-ring-chatgpt-2026-11-04.md` (brief, 4 lượt, lượt cuối chưa xong, bảng kiểm một phần).
- **Gemini:** chưa bắt đầu (chỉ làm sau khi ChatGPT PASS hai lần liên tiếp).
- **Chỗ trả lời đầu của ChatGPT khác bản nháp** (Claude chỉ mới đọc lướt đề mục, chưa kiểm; quyết sau khi có hai lượt PASS và Gemini):
  1. **Đo vòng:** ChatGPT bắn 256 tia từ các tâm thử quanh `(0; ring.y)` (lưới ±0,10 R0 theo x, ±0,15 R0 theo y, bước 0,02 R0), chỉ lấy tam giác có `|pháp tuyến mặt.z| ≥ 0,55`, gộp khoảng bán kính theo tia, chọn dải vòng lặp lại bằng trung vị lặp, chấm tâm bằng MAD của mép trong và mép ngoài cộng 2 × tỉ lệ góc hụt; đòi ≥ 90 % góc hợp lệ và MAD < 0,06 R0, sai thì **báo lỗi**, không lùi về `guardHalf`. Bản nháp dùng lưới chiếm chỗ 256² và loang lỗ. Hai cách cùng ý; cách của ChatGPT chặt hơn với mây sứ và hạt, đắt hơn lúc nạp.
  2. **Dải màu:** ChatGPT cho chỉ vàng trong `rIn → rIn + 0,020 × rOut`, chỉ vàng ngoài `silverStart − 0,025 × rOut → silverStart`, vành bạc `silverStart → rOut` (đo `silverStart`). Bản nháp dùng tỉ lệ cố định trên bề dày vòng (0,07 / 0,80 / 0,88).
  3. **Impostor:** ChatGPT lấy bán kính dọc của vòng trong ô bằng `ringR × (cellW / cellH) × rollWidth[row]` (số đo thật của từng hàng) thay cho `cos(roll)` của bản nháp, và tính mặt nạ **cho từng hàng trước khi trộn** (bản nháp cũng vậy). Cần Claude kiểm: `rollWidth` đo bề ngang lưỡi, không phải đĩa; ở hàng 90° đĩa còn bề dày riêng.
  4. **Fire:** cả hai cùng giữ vòng không bị `char` làm đen; hạt giữ ánh sẵn có.
- **Còn phải làm để phiếu thành bản chạy được:**
  1. ChatGPT: chạy tiếp các lượt tự duyệt trong cùng chat tới hai PASS liên tiếp (tối đa 4 lượt), rồi handoff ≤ 1.500 từ.
  2. Gemini (4 Argon, High): dán handoff bằng nút Copy và Cmd+V, duyệt, hai PASS liên tiếp, handoff.
  3. Claude kiểm các ý chính ở nguồn (three.js 0.170 `meshphysical.glsl.js`, `roughnessmap_fragment`, `metalnessmap_fragment` đã kiểm: thứ tự dòng 173–186 đúng như ghi ở Bối cảnh), quyết ba chỗ khác nhau ở trên, sửa mục "Lời giải đã chốt", rồi bỏ dòng "BẢN NHÁP".
  4. Lưu nguyên văn phần còn lại của hai cuộc chat vào `docs/games/tu-tien/skills/source/jade-ring-{chatgpt,gemini}-2026-11-04.md` kèm bảng kiểm.
