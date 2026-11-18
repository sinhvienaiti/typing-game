# Phiếu 259 · Tu Tiên · Code: vòng ngọc Clear Wind thành ngọc trắng viền vàng nhạt bằng mặt nạ hình học (gói CX-C)

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`): đo đĩa ngọc lúc nạp, shader lưỡi, cờ lab, công cụ so ảnh, test. Lời giải đã chốt ở phiếu này. Codex không thiết kế lại màu, ngưỡng hay cách đo; chỗ nào không làm được thì ghi báo cáo.

**Đường duyệt:** Claude tự phân tích; ChatGPT duyệt lượt 1 (FAIL, các lỗi đã xử lý); hai lượt PASS liên tiếp của agent phản biện Claude (lúc 14:10 một agent tưởng ChatGPT/Gemini mất đăng nhập; 14:55 kiểm lại thì vẫn đăng nhập. Theo skill `agent-orchestration` bước 9, việc không chờ hai trợ lý nên đi đường phản biện Claude; ghi rõ đường này).

**Báo cáo:** `docs/codex-queue/259-report.md` (tiếng Việt).

**Nguồn:**
- Kế hoạch `docs/games/tu-tien/skills/INTEGRATION_PLAN_2026-11-04.md` (ghi chú đầu, §2.8, §3 dòng CX-C, §4 "Vòng ngọc"); `docs/games/tu-tien/skills/SWORD_AURA.md` (Q4, `AuraAnchors`).
- Bản ghi ChatGPT: `docs/games/tu-tien/skills/source/jade-ring-chatgpt-2026-11-04.md`.
- Số đo và bản tham chiếu của Claude: `docs/codex-queue/259/jade-ring-reference.ts` (hàm `jadeRingOf` chạy được, in số ở đầu tệp), `docs/codex-queue/259/PROGRESS.md`.
- Mô phỏng nghiệm thu của Claude: `docs/codex-queue/259/ring-sim.ts` (chunk `RING` trên map màu thật, theo dải bán kính; Kiểm 6). Codex không chạy.
- Số phiếu: kế hoạch §7 gọi là `258-tt-jade-ring-material`; ghi chú đầu kế hoạch dời số lên một bậc, nên CX-C là **259**.

## Bối cảnh

**Anh chốt Q4 (04/11/2026):** vòng ngọc của Clear Wind thành **ngọc trắng viền vàng nhạt, "như ảnh đã duyệt"**.
- Không vẽ lại texture. Đổi chất liệu bằng mặt nạ hình học trong shader, rồi gửi anh ảnh trước và sau.
- Chỉ khi anh chê mới nhờ AI vẽ sửa texture UV.

**Ảnh đã duyệt:** `games/immortality-cultivation/art-src/weapons/clearwind-src3q.v4-try1.png` (nguồn Tripo của model đang dùng).
- Vòng là đĩa ngọc trắng dày, lỗ tròn hở.
- Một chỉ vàng nhạt chạy ở **mép ngoài** đĩa. Mép lỗ không có chỉ vàng rõ, chỉ có bóng ấm: bản nháp đọc nhầm chỗ này.
- Quanh đĩa là khung bạc. Trên đĩa có hai hạt ngọc xanh trong đế vàng, và mây sứ trắng viền vàng.
- Màu Claude đo trên ảnh (vùng 220 × 220 quanh vòng):

  | Vai | Trung vị sRGB | Tuyến tính | Độ sáng tuyến tính |
  |---|---|---|---|
  | Ngọc trắng | `#DFDDDF` | (0,738; 0,723; 0,738) | 0,727 |
  | Vàng nhạt | `#D4B793` | (0,658; 0,474; 0,292) | 0,500 |

**Claude đo model (04/11, HEAD `bc94110`).** Cách đo: dựng bản đồ độ cao và cắt lát trên GLB đã đưa về lưỡi đơn vị, bằng `bladeFromObject`, giống hệt game. Mọi số dưới đây theo đơn vị lưỡi.
- **Hình:** ba phần tách rõ, cả ở `clear-wind.glb` (14.728 tam giác) lẫn LOD `clear-wind-swarm.glb` (3.200 tam giác).
  - **Đĩa ngọc:** một xuyến dày từ mép lỗ `rIn` 0,0440 tới khoảng 0,090.
    - Tâm lỗ ở (0,0023; −0,0274). Lỗ sạch: không tam giác nào chiếu vào lỗ, cả mặt trước lẫn mặt sau.
    - Bề dày ở đỉnh 0,052. Đỉnh mặt trước cao z ≈ +0,0245, mặt sau z ≈ −0,0275.
    - Đĩa nghiêng khoảng 2° quanh trục x: đỉnh mặt trước cao 0,022 ở phía trên và 0,0275 ở phía dưới.
  - **Gờ nối:** một gờ mỏng ở z ≈ 0, dày 0,0105–0,014, từ chân thành ngoài của đĩa tới 0,102.
    - Chân đĩa (nơi bề dày xuống dưới ngưỡng `thr` của §1 bước 4) xê dịch theo góc: 0,088–0,092, trung vị 0,091, đo ở các góc không có phần nhô. Đầu trong của đoạn mỏng theo phân vị 25 % là 0,0924 (LOD 0,0920).
    - Map màu tô gờ màu đồng nâu sẫm, không phải xám: trung vị sRGB khoảng (133; 114; 86). Độ bão hòa **tuyến tính** 0,52–0,59 ở nửa trong (r 0,092–0,097), 0,44–0,51 ở nửa ngoài. Độ sáng tuyến tính khoảng 0,18. ORM: kim loại 0,15, nhám 0,44.
  - **Vành bạc:** từ khoảng 0,104 ra tới 0,113–0,128. Vành hình elip, rộng theo chiều ngang.
  - **Phần nhô cao hơn đỉnh đĩa** (z ≥ 0,03): hai hạt ngọc với đế vàng, các cụm mây sứ, khối chữ V ở gốc lưỡi, khâu nối xuống cổ chuôi. Mây còn thò ra ngoài vành, tới r ≈ 0,15.
- **Texture đã đúng màu; lỗi nằm ở chất liệu.**
  - Trong vùng đĩa, điểm ảnh trắng của map màu có trung vị sRGB (218; 215; 213), độ sáng tuyến tính 0,684 ở mặt trước và 0,692 ở mặt sau, rất gần `#DFDDDF`.
  - Chỉ vàng vẽ sẵn ở mép ngoài đĩa có điểm sáng (216; 181; 142), rất gần `#D4B793`.
  - Cái làm vòng "bạc như crôm" là map ORM:
    - độ kim loại trung vị 0,15; ở dải r 0,055–0,06, p90 lên 0,48; có đốm tới 0,61;
    - độ nhám trung vị 0,22–0,26; có đốm 0,10.
  - Trong engine, đĩa vì thế phản chiếu nền xám nên đọc như thiếc xám. Tấm `captures/tu-tien/clearwind/final/sheets/turntable-clear-wind.jpg` cho thấy rõ.
- **Bản nháp sai chỗ này:** dải cố định 0,07 / 0,80 / 0,88 trên `[rIn; rOut]` với `rOut` ≈ 0,12 đặt "chỉ vàng ngoài" vào r 0,106–0,113, tức là lên vành bạc, và tô gờ nối thành ngọc. Vì vậy phiếu này bỏ hẳn dải vẽ bằng hình học. Màu vàng lấy từ chính nét vàng đã vẽ trên texture (đúng chỗ ảnh đã duyệt có), shader chỉ đổi chất liệu.
- **Impostor (kiếm xa, phím 7):** atlas nướng bằng Blender từ cùng GLB, dưới đèn lookdev.
  - Đĩa trong atlas đã đọc sáng: trung vị điểm ảnh trung tính sáng ở hàng 0 là sRGB (190; 186; 185), tính cả vành.
  - Vòng ở kiếm xa chỉ 5–21 px.
  - Tô lại bằng elip trong ô atlas là không có căn cứ: chính ChatGPT tự nêu ở lỗi 8–10 của lượt duyệt 1.
  - Kết luận: **phiếu này không đổi `real-swords.ts`.** Đây là chỗ lệch với dòng CX-C của kế hoạch §3, đã quyết có lý do. Kiểm 11 so chỗ chuyển giữa kiếm giữa và kiếm xa; nếu lệch thì mở phiếu nướng lại atlas.
- **Mã hiện tại** (`games/immortality-cultivation`):
  - **`src/view/skills/sword-material.ts`:** `patchSwordMaterial(material, { bladeFrom, jade })` vá vật liệu PBR của GLB qua `onBeforeCompile`, `customProgramCacheKey` là `"real-sword"`.
    - Chunk `JADE` (sau `#include <color_fragment>`) giữ `swC` (màu map, tuyến tính, trước khi `char`) và `swJade` (mặt nạ sắc của hai hạt). Ở chế độ `furnace` (Fire), nó nhân `uSwChar` vào `diffuseColor`.
    - `EMIT` (sau `#include <emissivemap_fragment>`) cộng: đường mép, viền fresnel, `swJadeE` (ở Fire bị gán lại thành than hồng), dải nhiệt, chớp `swC × flash × 0,55`, mép tan.
    - `OUTGOING` chỉ cho `swJadeE` lấp phần trống dưới độ sáng 0,95.
    - Varying `vSwP = position` là không gian lưỡi đơn vị.
  - **`src/view/skills/blades.ts`:** `guardBand()` (Clear Wind: [−0,125; 0,075]), `auraAnchorsOf()` (`guardHalf` 0,1458), `modelOf()` (gọi `patchSwordMaterial`, `look = { bladeFrom, jade }`), `overlayModel()` (vá lại một bản sao bằng `model.look`), `loadSwordModels()` (model đầy đủ và LOD; chỉ Clear Wind có `motif.ring`).
  - **three.js 0.170.0, `meshphysical.glsl.js`:** thứ tự `color_fragment` → `roughnessmap_fragment` (khai `float roughnessFactor`, nhân kênh G) → `metalnessmap_fragment` (khai `float metalnessFactor`, nhân kênh B) → `normal_fragment_begin` → … → `emissivemap_fragment` → `lights_physical_fragment`, chunk này đọc `diffuseColor`, `metalnessFactor`, `roughnessFactor`. Claude đã kiểm trong `node_modules/three`.
  - **Vật liệu glTF:** không có `baseColorFactor`, `metallicFactor`, `roughnessFactor`, nên cả ba bằng 1. Không có `occlusionTexture`.
  - **Vùng ảnh hưởng:** vòng nằm trọn dưới `bladeFrom` = 0,085, vì đỉnh của vùng đổi ở y = −0,0274 + 0,0924 = 0,065. Nên đường mép, dải nhiệt và `swOn` không chạm tới vòng. Đáy vùng đổi ở −0,1198, trên `guardFrom` −0,125, nên cả vùng nằm trong dải xanh lá của `swordMask`.

## Lời giải đã chốt

**Tóm tắt:**
- Đo đĩa ngọc một lần lúc nạp, riêng cho từng model, từ chính tam giác của nó: tâm và `rIn`; `rCut` ở mép trong gờ nối (chân thành ngoài của đĩa); hai mặt phẳng đỉnh (trước, sau); một biên an toàn.
- Trong shader, vùng đổi là phần trong `rCut`, dưới cả hai mặt phẳng đỉnh cộng biên, và không phải hạt. Vùng này gồm đĩa với nét vàng của nó, không gồm hạt, đế, mây, chữ V, khâu nối hay vành.
- Trong vùng đổi, chính màu map phân loại:
  - điểm ảnh trung tính và sáng thành ngọc trắng: điện môi, nhám 0,34;
  - điểm ảnh ấm và bão hòa thành vàng nhạt: kim loại 0,85, nhám 0,30;
  - albedo theo độ sáng của map, để giữ nét chạm.
- Vòng không bị cháy đen ở Fire, có ánh ngọc trong nhẹ, và không vượt độ sáng 0,95 (hệ số Rec. 709 của bloom). Riêng ánh mép tan lúc kiếm tan hay hiện ra nằm ngoài nắp, như trên phần còn lại của kiếm.
- Ngoài vùng đổi giữ nguyên từng bit, vì cổng bằng uniform và mọi chỗ ghi đều nằm trong `if`.

### 1. Đo đĩa ngọc lúc nạp (`blades.ts`)

- Kiểu mới khai ở **`sword-material.ts`** (để `blades.ts` import, tránh vòng import):

  ```ts
  /** One crest plane of Clear Wind's jade disc: height = a + bx·(x − ring.x) + by·(y − ring.y) (unit blade; ticket 259). */
  export interface CrestPlane { readonly a: number; readonly bx: number; readonly by: number }
  /** Clear Wind's jade disc on the unit blade, measured at load from the model's own triangles (SWORD_AURA Q4; ticket 259). */
  export interface JadeRing {
    readonly x: number; readonly y: number;   // the hole's centre
    readonly rIn: number;                      // the hole's radius
    readonly rCut: number;                     // where the disc's material ends: the flange's inner edge (the foot of the disc's outer wall)
    readonly front: CrestPlane;                // the disc's crest seen from +z (heights are z)
    readonly back: CrestPlane;                 // the disc's crest seen from −z (heights are −z)
    readonly margin: number;                   // 0.06 × the disc's crest thickness, added over both planes
  }
  ```

- Hàm mới trong `blades.ts`, xuất ra: `jadeRingOf(geometry: THREE.BufferGeometry, guard: readonly [number, number], guardHalf: number, fail?: (step: string) => void): JadeRing | null`.
  - `fail` không bắt buộc. Ngay trước mỗi `return null`, hàm gọi `fail?.(step)` **đúng một lần**, với tên bước hỏng, đúng như tệp tham chiếu:
    - `"hole-seed"`: không có hạt giống lỗ; `"hole-open"`: vùng loang chạm biên lưới;
    - `"band"`: không có `start` < `end`;
    - `"flange"`: không có thung lũng, hoặc thung lũng không đủ mỏng hay đủ sâu;
    - `"crest-front"`, `"crest-back"`: khớp mặt phẳng hỏng (dưới 24 góc, phần dư vượt, hay `a` ≤ 0). Mặt trước hỏng thì trả `null` ngay, không khớp mặt sau;
    - `"bounds"`: điều kiện hợp lệ của bước 6.
  - Hàm không tự `console.warn`, vì nó không biết tên model. Test gọi không có `fail`.
  - **Làm đúng từng bước của `docs/codex-queue/259/jade-ring-reference.ts`.** Chép logic, đổi cho hợp quy ước mã. Không đổi hằng số nào.
    1. **Bản đồ độ cao:**
       - Lưới 512 × 512 phủ hình vuông [−h; h] × [cy0 − h; cy0 + h], với h = 1,25 × `guardHalf`, cy0 = (g0 + g1) / 2.
       - Mỗi tam giác có ít nhất một đỉnh với y trong [g0 − 0,02; g1 + 0,02] được tô vào ô: lấy tâm ô, thử barycentric, chấp nhận khi mọi trọng số ≥ 0.
       - Hai mảng: `top` lấy z lớn nhất, `bot` lấy z nhỏ nhất.
    2. **Lỗ:**
       - Hạt giống là ô trống gần ô của (0; cy0) nhất, trong vòng 40 ô. Loang bốn hướng qua các ô trống.
       - Không có hạt giống, hoặc vùng loang chạm biên lưới: trả `null`.
       - Tâm lỗ là trung bình các tâm ô. `rIn` = √(số ô / π) × cạnh ô.
    3. **Bề dày quanh lỗ:**
       - Bán kính chạy từ `rIn` + 1 ô, mỗi bước một ô, tới h. Ở mỗi bán kính lấy 180 góc, góc thứ k ở (k + 0,5)/180 × 2π.
       - Ghi độ phủ: tỉ lệ góc có ô đầy.
       - Ghi bề dày `top − bot`, lấy **phân vị 25 %**: sắp tăng, chỉ số ⌊n × 0,25⌋. Phần nhô chỉ làm dày thêm, nên phân vị thấp đọc đúng mặt đĩa.
       - `start` là bán kính đầu tiên có độ phủ ≥ 0,95. `end` là bán kính đầu tiên sau `start` có độ phủ < 0,90.
    4. **Gờ nối:**
       - Chọn **thung lũng sâu nhất** của bề dày trong [start; end). Độ sâu = min(bề dày lớn nhất từ `start` tới nó, bề dày lớn nhất từ nó tới `end`) − bề dày của nó.
       - Đỉnh đĩa `crest` là chỗ dày nhất phía trong thung lũng. Đỉnh vành `rim` là chỗ dày nhất phía ngoài.
       - Đòi bề dày thung lũng ≤ 0,4 × bề dày đỉnh, và độ sâu ≥ 0,2 × bề dày đỉnh; sai thì trả `null`.
       - Đặt ngưỡng `thr` = thung lũng + 0,25 × (min(đỉnh đĩa; đỉnh vành) − thung lũng). Từ thung lũng, nới **vào trong** khi bề dày của bán kính kế trong còn < `thr`, không quá `crest`. Gọi chỉ số dừng là `a0`.
       - `rCut` = bán kính `a0` (`rs[a0]`): đầu trong của đoạn mỏng, tức chân thành ngoài của đĩa, mép trong của gờ nối. **Không** lấy trung điểm đoạn mỏng: gờ tô màu đồng bão hòa mà bộ phân loại màu ở §2 không tách được khỏi nét vàng, nên vùng đổi phải dừng trước gờ (xem "Phản biện", lỗi 2).
    5. **Hai mặt phẳng đỉnh:**
       - Đặt w = `rCut − rIn`. Lấy 120 góc; ở mỗi góc, lấy ô cao nhất trên dải bán kính `rIn + 0,30 w` … `rIn + 0,55 w`, bước nửa ô. Mặt trước tính bằng `top`, mặt sau bằng `−bot`.
       - Khớp h(θ) = a + b cos θ + c sin θ bằng bình phương nhỏ nhất (hệ 3 × 3, khử Gauss có chọn trụ).
       - Lặp 5 lần. Lần đầu dùng mọi góc có số. Sau mỗi lần khớp, chỉ giữ các góc có phần dư ≤ phân vị 40 % của phần dư mọi góc. Như vậy bám mép dưới: hạt, mây, chữ V nằm trên nên bị loại.
       - Ít hơn 24 góc có số: `null`.
       - `bx = b / rMid`, `by = c / rMid`, với `rMid = rIn + 0,425 w`.
    6. **Biên và kiểm hợp lệ:**
       - `margin = 0,06 ×` bề dày đỉnh đĩa.
       - Trả `null` khi một trong các điều kiện sau sai:
         - ở lần khớp cuối, mọi góc được giữ có phần dư ≤ 0,5 × `margin`;
         - cả hai `a` > 0;
         - 0,2 × `guardHalf` < `rIn` < 0,7 × `guardHalf`;
         - |x tâm| ≤ 0,1 × `guardHalf`;
         - y tâm nằm trong `guard`;
         - w ≥ 0,3 × `rIn`.
  - Trả `null` thì vòng giữ như hôm nay. **Không** lùi về `guardHalf`, không đoán. Lời cảnh báo do `modelOf` in, qua `fail` (xem "Nối vào model"): `console.warn` một lần mỗi model, nêu tên model và bước hỏng.
  - Số đo phải ra (bản tham chiếu, HEAD `bc94110`, `rCut` ở mép trong gờ):

    | Model | x | y | `rIn` | `rCut` | front (a; bx; by) | back (a; bx; by) | `margin` |
    |---|---|---|---|---|---|---|---|
    | `clear-wind.glb` | 0,00230 | −0,02741 | 0,04401 | 0,09243 | 0,02450; −0,01751; −0,03781 | 0,02744; −0,00356; 0,03750 | 0,00313 |
    | `clear-wind-swarm.glb` | 0,00205 | −0,02767 | 0,04409 | 0,09201 | 0,02453; −0,01954; −0,03616 | 0,02738; −0,00116; 0,03477 | 0,00309 |

    Hai mặt phẳng đỉnh đổi nhẹ so với bản trước (độ dốc lệch ≤ 0,0024), vì dải lấy mẫu của bước 5 tính theo w = `rCut − rIn`.
  - Thời gian đo trong Node: khoảng 15 ms mỗi model. Mảng tạm 2 × 1 MB chỉ dùng lúc nạp.
- **Nối vào model:**
  - `SwordModel` thêm `readonly jadeRing: JadeRing | null`.
  - `modelOf()` chỉ đo khi `ring === true`, sau `guardBand` và `auraAnchorsOf`, dùng `aura.guardHalf`. Kết quả vào `look.ring`, rồi mới gọi `patchSwordMaterial(material, look)`. Thứ tự trong `modelOf` đổi cho hợp, kết quả `aura` không đổi.
  - `modelOf()` truyền `fail` in cảnh báo bằng chính tham số `source` của nó:

    ```ts
    const jadeRing = ring ? jadeRingOf(geometry, guard, aura.guardHalf, (step) => console.warn(`[blades] ${source}: jade ring not measured (${step}); the ring keeps its old material`)) : null;
    ```

    `loadSwordModels` giữ model trong bộ đệm theo URL, nên mỗi model cảnh báo nhiều nhất một lần.
  - Mỗi model tự đo: model đầy đủ đo trên hình của nó, LOD đo trên hình của nó, cả hai ở cùng hệ lưỡi đơn vị qua `bladeMap`.
  - `standInModel()` không có vòng.
  - `overlayModel()` đã vá bằng `model.look`, nên tự có vòng.
  - **Không đổi `AuraAnchors.ring`** và mọi trường khác của `AuraAnchors`: các lớp hào quang đang đọc chúng.

### 2. Shader lưỡi (`sword-material.ts`)

- `SwordMaterialOptions` thêm `readonly ring?: JadeRing | null`.
- Bảng dùng chung, xuất ra:

  ```ts
  /**
   * Clear Wind's jade disc as white jade with a pale gold line (owner Q4, 04/11/2026; colours sampled from
   * clearwind-src3q.v4-try1.png; ticket 259). The colour map already paints the jade white and the line gold; its ORM made
   * the disc metallic and glossy (chrome). Inside the measured disc the map's own classes take these materials.
   */
  export const JADE_RING_LOOK = {
    on: { value: 1 },                                              // ?jadeRing=off → 0 (before/after); 2 only inside __lab.ringCap (the ring's weights)
    jade: { value: new THREE.Vector3(0.738, 0.723, 0.738) },       // #DFDDDF, linear
    gold: { value: new THREE.Vector3(0.658, 0.474, 0.292) },       // #D4B793, linear
    /** x: the map's jade median luminance (0.69, measured), y: the pale gold's luminance (0.50), z: the jade's inner light at rest (?jadeRingGlow), w: unused */
    tone: { value: new THREE.Vector4(0.69, 0.5, 0.06, 0) },
    /** jade metalness, jade roughness, gold metalness, gold roughness */
    pbr: { value: new THREE.Vector4(0, 0.34, 0.85, 0.3) },
  };
  ```

- **Uniform:**
  - Dùng chung, trỏ vào `JADE_RING_LOOK` như cách `SWORD_LOOK` đang làm: `uSwRingOn` (float), `uSwRingJade`, `uSwRingGold` (vec3), `uSwRingTone`, `uSwRingPbr` (vec4).
  - Riêng mỗi vật liệu, tạo một lần trong `patchSwordMaterial`, mặc định 0 khi không có `ring`:
    - `uSwRingC = vec4(ring.x, ring.y, ring.rCut, có ring ? 1 : 0)`;
    - `uSwRingF = vec4(front.a, front.bx, front.by, margin)`;
    - `uSwRingB = vec4(back.a, back.bx, back.by, margin)`.
  - Khai cả 8 uniform trong `PARS_FRAGMENT`. `customProgramCacheKey` giữ `"real-sword"`: một chương trình cho mọi vũ khí. **Không dùng `#define`, `#ifdef`.**
- **Chunk mới `RING`,** chèn ngay **sau `#include <metalnessmap_fragment>`**. Ở chỗ đó `swC`, `swJade`, `roughnessFactor`, `metalnessFactor` đều đã có. Trước khi thay chuỗi, nếu `#include <metalnessmap_fragment>` không còn trong shader thì `throw new Error("[sword-material] three's physical shader changed: the metalness hook is missing")`, như hai `throw` đang có.

  ```glsl
  // Clear Wind's jade disc (ticket 259): inside the flange, under both crest planes, not a bead; the colour map's own
  // classes pick white jade or pale gold. Nothing is written outside it.
  float swRingJ = 0.0;
  float swRingG = 0.0;
  if (uSwRingC.w * uSwRingOn > 0.5) {
    vec2 swQ = vSwP.xy - uSwRingC.xy;
    float swD = length(swQ);
    float swAr = max(fwidth(swD), 1e-5);
    float swAz = max(fwidth(vSwP.z), 1e-5);
    float swCapF = uSwRingF.x + dot(uSwRingF.yz, swQ) + uSwRingF.w;
    float swCapB = uSwRingB.x + dot(uSwRingB.yz, swQ) + uSwRingB.w;
    float swIn = (1.0 - smoothstep(uSwRingC.z - swAr, uSwRingC.z + swAr, swD))
      * (1.0 - smoothstep(swCapF - swAz, swCapF + swAz, vSwP.z))
      * (1.0 - smoothstep(swCapB - swAz, swCapB + swAz, -vSwP.z))
      * (1.0 - swJade);
    float swLum = dot(swC, vec3(0.2126, 0.7152, 0.0722));
    float swMx = max(swC.r, max(swC.g, swC.b));
    float swSat = (swMx - min(swC.r, min(swC.g, swC.b))) / max(swMx, 1e-3);
    float swGk = smoothstep(0.38, 0.52, swSat) * smoothstep(0.05, 0.12, swC.r - swC.b);
    float swJk = (1.0 - swGk) * smoothstep(0.20, 0.35, swLum) * (1.0 - smoothstep(0.18, 0.30, swSat));
    swRingJ = swIn * swJk;
    swRingG = swIn * swGk;
    float swRw = swRingJ + swRingG;
    if (swRw > 0.0) {
      vec3 swJa = uSwRingJade * clamp(swLum / uSwRingTone.x, 0.3, 1.06);
      vec3 swGa = uSwRingGold * clamp(swLum / uSwRingTone.y, 0.3, 1.1);
      // swC is the map before the furnace's char: the disc is replaced, not charred (Fire keeps Clear Wind's white jade).
      diffuseColor.rgb = mix(diffuseColor.rgb, (swJa * swRingJ + swGa * swRingG) / swRw, swRw);
      metalnessFactor = mix(metalnessFactor, (uSwRingPbr.x * swRingJ + uSwRingPbr.z * swRingG) / swRw, swRw);
      roughnessFactor = mix(roughnessFactor, (uSwRingPbr.y * swRingJ + uSwRingPbr.w * swRingG) / swRw, swRw);
    }
  }
  ```

  - Lý do các ngưỡng, Claude đã thử trên map thật bằng mô phỏng (tách điểm ảnh trong vùng đổi theo ba loại, mặt trước và sau, model đầy đủ và LOD). Mọi độ bão hòa ở đây tính trên màu **tuyến tính**, như `swC` trong shader:
    - Nét vàng vẽ trên thành ngoài đĩa (r 0,084–0,091) có độ bão hòa 0,6–0,7 với R > B, độ sáng 0,25–0,29; điểm ảnh tối của nó sát chân đĩa có độ sáng 0,10–0,15.
    - Ngọc có độ bão hòa 0,03–0,05 và độ sáng 0,48–0,72.
    - Bạc chạm xanh của chữ V và vùng tối không rơi vào loại nào, nên giữ nguyên.
    - **Gờ nối không tách được bằng màu.** Gờ là đồng nâu sẫm, độ bão hòa 0,52–0,59 ở nửa trong và 0,44–0,51 ở nửa ngoài, độ sáng khoảng 0,18; trọng số vàng `swGk` trung bình 0,55–0,75 ở nửa trong. Bản trước ghi "0,26": đó là độ bão hòa sRGB của nửa ngoài gờ, sai hệ màu. Cổng độ sáng cũng không tách được, vì điểm ảnh tối của nét vàng (0,10–0,15) tối hơn gờ (0,18). Vì vậy gờ được giữ **bằng hình**: `rCut` dừng ở mép trong gờ (§1 bước 4).
  - Kết quả mô phỏng, 2.000 px/đơn vị (`docs/codex-queue/259/ring-sim.ts`, số đo bảng §1):
    - Trong vùng đổi, model đầy đủ, mặt trước: 43.267 điểm ảnh ngọc, 6.283 vàng, 3.645 giữ nguyên (bóng tối và điểm ảnh lưng chừng). Mặt sau: 43.836 / 6.547 / 3.436. LOD: 41.594 / 7.929 / 4.002 và 42.689 / 6.977 / 4.714. Hạt, đế, mây, chữ V, khâu nối và vành bị loại trọn.
    - Theo dải bán kính quanh tâm lỗ, tỉ lệ điểm ảnh đổi (J + G > 0,05), thứ tự: đầy đủ trước, đầy đủ sau, LOD trước, LOD sau:

      | Dải | `rCut` ở mép trong gờ (phiếu này) | `rCut` giữa gờ (bản trước) |
      |---|---|---|
      | 0,084–0,092 (nét vàng; phần còn lại bị hạt, mây che hoặc tối) | 37,7 / 33,9 / 40,9 / 36,1 % | 37,8 / 33,8 / 40,8 / 36,1 % |
      | 0,092–0,102 (gờ nối) | 1,8 / 1,4 / 0,0 / 0,0 % | 18,8 / 14,4 / 19,4 / 14,0 % |

    - Nét vàng vì thế đổi như bản trước, còn gờ gần như nguyên.
    - Phần gờ còn đổi là một dải hẹp sát chân đĩa, ở những góc chân đĩa vào trong hơn `rCut` (tới 0,088). Theo bề dày đo ở từng điểm ảnh, dải này là 11–14 % điểm ảnh của gờ, so với 38–41 % ở bản trước. Mép đổi nằm ở nếp gấp giữa thành đĩa và gờ, hoặc cách nếp gấp tối đa khoảng 0,0045.
    - Không đặt `rCut` nhỏ hơn: `rCut` 0,0915 cắt nét vàng, dải 0,084–0,092 mất 2–3 điểm %.
  - Cách đổi albedo:
    - Ngọc: albedo = `#DFDDDF` × (độ sáng map / 0,69), kẹp [0,3; 1,06]. Trung vị của map ra đúng màu đích, nét chạm và bóng của map còn nguyên. Kênh lớn nhất 0,78.
    - Vàng: albedo = `#D4B793` × (độ sáng map / 0,50), kẹp [0,3; 1,1]. Điểm sáng của nét vàng ra đúng màu đích, kẽ tối giữ tối. Kênh lớn nhất 0,72.
  - Chất liệu:
    - Ngọc: kim loại 0, nhám 0,34. Bóng mềm như ngọc đánh bóng, không như gương crôm hay phấn.
    - Vàng: kim loại 0,85, nhám 0,30. Ánh vàng kim; còn 15 % khuếch tán nên không tối đen khi phản chiếu nền tối.
  - **Normal map giữ nguyên.** Bỏ ý giảm 15 %, theo lượt tự duyệt của ChatGPT.
- **Ánh ngọc trong** (giả trong mờ, không bloom), ở `EMIT`: chèn ngay **sau** khối `if (uSwMode > 0.5) { … }` và **trước** `totalEmissiveRadiance += swJadeE;`:

  ```glsl
  // The jade disc's soft inner light (ticket 259): white jade in every mode; OUTGOING lets it fill only the headroom.
  if (swRingJ > 0.0) swJadeE += uSwRingJade * swRingJ * (uSwRingTone.z + 0.10 * swGlow + 0.25 * min(swFlash, 1.0));
  ```

  Lúc nghỉ, ánh này là 0,738 × 0,06 ≈ 0,044, nên đĩa không xám đi trong bóng. Lớn nhất 0,30 / kênh. Nằm trong `swJadeE`, nên luật lấp khoảng trống dưới 0,95 của `OUTGOING` vẫn áp. Ở Fire, đĩa vẫn sáng trắng, hạt vẫn là than hồng như hôm nay.
- **Không bao giờ bloom:** nối vào cuối `OUTGOING`:

  ```glsl
  // The jade disc never blooms (ticket 259): its lit colour, inner light, flash and rim stay under luminance 0.95, by
  // the bloom's own weights (Rec. 709, as three's luminance() in LuminosityHighPassShader). The dissolve's light edge
  // (EMIT's last line) is left out of the cap: the disc melts and appears in light with the rest of the sword.
  // uSwRingOn 2 (only __lab.ringCap, ticket 259 Check 8) writes the ring's weights instead of its light.
  float swRingW = swRingJ + swRingG;
  if (swRingW > 0.0) {
    vec3 swRingDe = uSwEdge * swDe * 0.7;
    float swRl = dot(outgoingLight - swRingDe, vec3(0.2126, 0.7152, 0.0722));
    outgoingLight = (outgoingLight - swRingDe) * mix(1.0, min(1.0, 0.95 / max(swRl, 1e-4)), swRingW) + swRingDe;
    if (uSwRingOn > 1.5) outgoingLight = vec3(1.0 - swRingW, swRingJ, swRingG);
  }
  ```

  - **Ánh mép tan nằm ngoài nắp** (lượt phản biện 4, lỗi 2). `swRingDe` đúng bằng số hạng cuối của `EMIT` (`uSwEdge * swDe * 0.7`). `swDe` khai ở tầm `main` (chunk `DISSOLVE`, sau `clipping_planes_fragment`), `uSwEdge` là uniform, nên cả hai dùng được ở đây. Phần còn lại không âm: luật lấp khoảng trống ở trên chỉ bớt tối đa `swJadeE`, mà `swJadeE` đã nằm trong `outgoingLight`.
    - Lý do: với Metal, ánh này là 0,7 × `EDGE_HOT` ≈ (1,56; 2,22; 2,52), độ sáng khoảng 2,06. Nếu nắp ăn cả nó, mép tan trên đĩa bị ép xuống 0,95 và không bloom, trong khi cách một điểm ảnh, trên gờ, vành và lưỡi, nó vẫn bloom: mỗi kiếm vạn kiếm hiện ra từ ánh sáng, mỗi kiếm cắm của nạn nhân tan (`victims.ts`, `PIN_FADE_S`) và kiếm trời K5 sẽ có một vệt mờ ở `rCut`.
    - Vì vậy nắp chỉ áp cho ánh sáng của chính đĩa: màu lit, ánh ngọc trong, chớp, viền fresnel. Lúc không tan (`swDe` = 0), `swRingDe` = 0 và khối này là phép nhân của nắp cũ, chỉ khác hệ số độ sáng (gạch dưới).
  - **Hệ số độ sáng Rec. 709** (Claude thêm ở lượt 4). Bloom của three r170 đo bằng hàm `luminance()` mà `WebGLProgram` chèn vào mọi shader, với hệ số `ColorManagement` của không gian làm việc: (0,2126; 0,7152; 0,0722). Nắp đo bằng hệ số Rec. 601 (0,299; 0,587; 0,114) thì một điểm ảnh xanh lá ép tới 0,95 vẫn qua ngưỡng 1 của bloom.
    - Ví dụ có thật: viền của chiêu k4 Clear Wind (`element-metal.ts`, `CLEAR_WIND_TONE.k4`, `#35b483` qua `rimOf(…, 1,2)`) có độ sáng 709 / 601 ≈ 1,16. Điểm ảnh viền ép tới 0,95 theo 601 có độ sáng 709 tới 1,1.
    - Với 709, nắp 0,95 luôn cách ngưỡng bloom 5 %, mọi màu viền. Ngọc trắng trung tính (`#DFDDDF`) cho hai số gần bằng nhau (0,727 và 0,729), nên màu đĩa không đổi.
    - Luật lấp khoảng trống cũ của hạt ngọc ở `OUTGOING` vẫn dùng hệ số 601; nó nằm ngoài phạm vi phiếu này và trong danh sách cấm sửa.
  - **`uSwRingOn` = 2** chỉ do `__lab.ringCap()` đặt (§4), trong ba lần vẽ của nó rồi trả lại. Cổng của `RING` (`uSwRingC.w * uSwRingOn > 0.5`) vẫn mở. Khi đó điểm ảnh của vòng ghi (1 − trọng số, J, G) thay cho ánh sáng, để phép đo tách điểm ảnh nắp áp trọn với điểm ảnh ở mép mềm. Game và cờ `?jadeRing` chỉ đặt 0 hoặc 1; nhánh nằm trong `if (swRingW > 0.0)`, nên ngoài vòng vẫn giữ nguyên từng bit.

- **Các đường khác, giữ nguyên có chủ ý** (trả lời lỗi 6 và 7 của ChatGPT):
  - `char` ở Fire: đĩa thay albedo sau `char`, nên không cháy đen. Phần ngoài vùng đổi vẫn cháy như cũ.
  - Dải nhiệt, đường mép, `swOn`: chỉ có từ `bladeFrom` = 0,085 trở lên, không tới vòng (đỉnh vùng đổi ở 0,065).
  - Viền fresnel màu chiêu: giữ. Nó là quầng quanh dáng kiếm trong mọi chiêu; nắp 0,95 ở trên giữ nó không bloom trên đĩa.
  - Chớp trúng: giữ `swC × flash × 0,55`, vì `swC` của đĩa đã gần trắng ngọc. Nắp 0,95 áp.
  - Hạt ngọc: mặt nạ `swJade` và ánh của nó như hôm nay, cả Metal lẫn Fire. Vùng đổi nhân `1 − swJade`, và hạt nằm trên mặt phẳng đỉnh.
  - Mép tan (`DISSOLVE`, `discard`): giữ, không miễn cho vòng. Vòng tan cùng kiếm. Ánh mép tan (`uSwEdge * swDe * 0.7`) nằm ngoài nắp 0,95, nên trên đĩa nó sáng và bloom như trên gờ, vành và lưỡi; không có vệt mờ ở `rCut` (xem "Không bao giờ bloom").
  - Normal map, UV, hình, bóng đổ: không đổi.

### 3. Impostor (`real-swords.ts`): không đổi

Lý do ở Bối cảnh. Không thêm uniform, không đọc `ringU`, `ringR`. Kiểm 11 so chỗ chuyển; nếu lệch, mở phiếu nướng lại atlas bằng `bake_sword_impostor.py`, dùng cùng cách đổi chất liệu.

### 4. Lab (`src/lab/skills-main.ts`)

- `?jadeRing=off` đặt `JADE_RING_LOOK.on.value = 0`: vòng như cũ, để chụp trước và sau. Mặc định bật.
- `?jadeRingGlow=<số>` đặt `JADE_RING_LOOK.tone.value.z`, kẹp trong [0; 0,15]. Đây là núm để Claude chỉnh ánh ngọc khi duyệt, không đổi mặc định.
- Đặt hai cờ cạnh `BLADE_HEAT`, và ghi vào khối chú thích cờ đầu tệp.
- `__lab.jadeRing()` trả `{ hero: JadeRing | null, mid: JadeRing | null }` từ `fx.blades.models()`, để Claude so số trong trình duyệt với số đo trong Node. Khai kiểu trong interface `__lab` như các hàm khác.
- **`__lab.swordMask(on, all = false)`:** thêm tham số thứ hai. Lý do: mặt nạ hôm nay chỉ vẽ `fx.blades.mesh`, `d.lead`, `auraSolo.blade.mesh`, `fx.blades.swarm`, `d.mid` và ẩn mọi lưới khác. Nhưng hai lưới nữa cũng mang vật liệu mới, nên cũng đổi màu vòng:
  - kiếm cắm của nạn nhân (`src/lab/victims.ts`, `new BladeSet(PINS, …)`, `setSword((await loadSwordModels(def)).full)`), ở phím 7 và K5;
  - kiếm trời của K5 (`sword-skills.ts`, `this.heaven.setModel(overlayModel(models.full))`), dài khoảng 20 m, có trên màn từ release + 1,29 s tới khoảng 3,9 s, tức các khung k5-140/175/230. `overlayModel` vá lại bằng `model.look`, nên cũng có vòng.

  Thay đúng khối `swordMask` hiện có bằng:

  ```ts
  swordMask(on, all = false) {
    if (on) {
      maskRestore?.();
      const d = myriad.auraDebug;
      const a = swordAura.anchors;
      const lead: THREE.Mesh[] = [fx.blades.mesh, d.lead, auraSolo.blade.mesh];
      const mid = [fx.blades.swarm, d.mid].filter((m): m is THREE.InstancedMesh => m !== null);
      if (all) {
        // Ticket 259: every other mesh drawing a patched sword (the victims' planted swords, K5's heaven sword), as lead.
        const known = new Set<THREE.Object3D>([...lead, ...mid]);
        view.scene.traverse((o) => {
          const m = o as THREE.InstancedMesh;
          if (m.isInstancedMesh === true && !known.has(m) && !Array.isArray(m.material) && m.material.customProgramCacheKey() === "real-sword") lead.push(m);
        });
      }
      maskRestore = drawSwordMask(view.stage.renderer, view.scene, view.camera, lead, mid, a?.bladeFrom ?? 0.085, a?.guardFrom ?? -0.125);
    } else {
      maskRestore?.();
      maskRestore = null;
      view.render(0);
    }
  },
  ```

  - `known` loại lưới đã có trong danh sách: `drawSwordMask` lưu vật liệu gốc vào `Map` theo lưới, một lưới vào hai lần sẽ lưu nhầm vật liệu mặt nạ làm "gốc".
  - Duyệt cây chỉ khi gọi mặt nạ (lúc chụp), không phải mỗi khung.
  - Interface `__lab`: `swordMask(on: boolean, all?: boolean): void;`, chú thích thêm: `all` cũng vẽ mọi lưới kiếm có vật liệu `"real-sword"` (kiếm cắm của nạn nhân, kiếm trời K5), dùng cho `MASK=1` của phiếu 259.
  - `lab-sword-aura.mjs` và các cổng hào quang vẫn gọi `swordMask(true)`: không đổi gì với chúng. **Không** sửa `aura-gates.ts`.
- **`__lab.ringCap()`** (mới; lượt phản biện 4, lỗi 1): đo thẳng nắp 0,95 của đĩa trên riêng các kiếm, ở đúng khung đang có, không bước thời gian. Đây là cổng của Kiểm 8 thay cho `bright` cả khung (lý do ở Kiểm 8).
  - Vẽ mọi lưới có vật liệu `"real-sword"` (cùng tập với `swordMask(true, true)`: kiếm bay, vạn kiếm, solo, kiếm cắm của nạn nhân, kiếm trời K5) bằng chính vật liệu của nó, vào một target HalfFloat đủ cỡ khung, với đèn, bóng đổ và sương của khung. Vẽ ba lần: vòng tắt (`on` = 0), vòng bật (1), rồi trọng số của vòng (2, đẩy sương ra xa như `post({ fog: false })`). Đọc cả ba, trả mọi thứ về như cũ, rồi `view.render(0)`.
  - `SWORD_LOOK.edge` đặt về 0 trong cả ba lần vẽ rồi trả lại: ánh mép tan nằm ngoài nắp (§2), nên phải bỏ ra khỏi phép đo. Đường mép của lưỡi cũng tắt theo, nhưng nó giống nhau ở lần 0 và 1 nên không thành điểm ảnh "đổi". Đây là đặt tạm trong lab, không phải sửa `SWORD_LOOK`.
  - Không có trong suốt nào đè lên (thẻ hào quang, lửa, vệt SilkTail, tia lửa, ảnh trúng đều bị ẩn), và đo ở đủ độ phân giải, không qua phép trung bình 2 × 2 của bộ đệm sáng: đúng hợp đồng của nắp, không hơn.
  - Import thêm `JADE_RING_LOOK`, `SWORD_LOOK` vào dòng import `sword-material` đang có. Thêm vào object `__lab`, ngay sau `swordMask`:

  ```ts
  ringCap() {
    // Ticket 259, Check 8: the jade disc's cap on the swords alone, at this frame (no time passes; the frame is redrawn
    // afterwards). Every mesh with a patched sword material ("real-sword") is drawn with its own material into a
    // full-size half-float target, with the frame's lights and shadow maps: ring off (0), on (1), then its weights (2,
    // fog pushed out). The edge light is zeroed in all three: the dissolve's light edge is outside the cap on purpose.
    const renderer = view.stage.renderer;
    const scene = view.scene;
    const swords: THREE.Mesh[] = [];
    scene.traverse((o) => {
      const m = o as THREE.Mesh;
      if (m.isMesh === true && m.visible && !Array.isArray(m.material) && m.material.customProgramCacheKey() === "real-sword") swords.push(m);
    });
    const kept = new Set<THREE.Object3D>(swords);
    const hidden: THREE.Object3D[] = [];
    scene.traverse((o) => {
      if (((o as THREE.Mesh).isMesh === true || (o as THREE.Points).isPoints === true || (o as THREE.Line).isLine === true || (o as THREE.Sprite).isSprite === true) && o.visible && !kept.has(o)) {
        o.visible = false;
        hidden.push(o);
      }
    });
    const size = renderer.getDrawingBufferSize(new THREE.Vector2());
    const w = size.x;
    const h = size.y;
    const rt = new THREE.WebGLRenderTarget(w, h, { type: THREE.HalfFloatType });
    const reads = [new Uint16Array(w * h * 4), new Uint16Array(w * h * 4), new Uint16Array(w * h * 4)] as const;
    const fog = scene.fog as THREE.Fog | null;
    const near = fog?.near ?? 0;
    const far = fog?.far ?? 0;
    const on = JADE_RING_LOOK.on.value;
    const edge = SWORD_LOOK.edge.value.clone();
    const bg = scene.background;
    const shadow = renderer.shadowMap.autoUpdate;
    const clear = renderer.getClearColor(new THREE.Color());
    const clearA = renderer.getClearAlpha();
    scene.background = null;
    renderer.shadowMap.autoUpdate = false;
    SWORD_LOOK.edge.value.set(0, 0, 0);
    renderer.setRenderTarget(rt);
    renderer.setClearColor(0x000000, 0);
    for (let pass = 0; pass < 3; pass += 1) {
      JADE_RING_LOOK.on.value = pass;
      if (pass === 2 && fog !== null) {
        fog.near = 1e5;
        fog.far = 1e5 + 1;
      }
      renderer.clear();
      renderer.render(scene, view.camera);
      renderer.readRenderTargetPixels(rt, 0, 0, w, h, reads[pass]!);
    }
    renderer.setRenderTarget(null);
    renderer.setClearColor(clear, clearA);
    if (fog !== null) {
      fog.near = near;
      fog.far = far;
    }
    JADE_RING_LOOK.on.value = on;
    SWORD_LOOK.edge.value.copy(edge);
    scene.background = bg;
    renderer.shadowMap.autoUpdate = shadow;
    for (const o of hidden) o.visible = true;
    rt.dispose();
    view.render(0);
    const [a, b, wt] = reads;
    const half = THREE.DataUtils.fromHalfFloat;
    let changed = 0;
    let interior = 0;
    let over = 0;
    let soft = 0;
    let nonFinite = 0;
    let max = 0;
    let overMax = 0;
    let softMax = 0;
    for (let o = 0; o < w * h * 4; o += 4) {
      if (a[o] === b[o] && a[o + 1] === b[o + 1] && a[o + 2] === b[o + 2]) continue;
      changed += 1;
      if ((b[o]! & 0x7c00) === 0x7c00 || (b[o + 1]! & 0x7c00) === 0x7c00 || (b[o + 2]! & 0x7c00) === 0x7c00) {
        nonFinite += 1;
        continue;
      }
      // The bloom's own luminance (Rec. 709), on the ring-on pass.
      const l = 0.2126 * half(b[o]!) + 0.7152 * half(b[o + 1]!) + 0.0722 * half(b[o + 2]!);
      // Pass 2 wrote 1 − the ring's weight: ≤ 1e-4 means the cap applies in full.
      if (half(wt[o]!) <= 1e-4) {
        interior += 1;
        max = Math.max(max, l);
        if (l > 0.96) {
          over += 1;
          overMax = Math.max(overMax, l);
        }
      } else if (l > 0.96) {
        soft += 1;
        softMax = Math.max(softMax, l);
      }
    }
    return { swords: swords.length, size: [w, h], changed, interior, max, over, overMax, soft, softMax, nonFinite };
  },
  ```

  - Interface `__lab`, ngay sau `swordMask`:

  ```ts
  /**
   * Ticket 259, Check 8: the jade disc's cap measured on the swords alone at this frame (no time passes). changed: pixels
   * the ring changes (off against on); interior: those where the cap applies in full; over: interior pixels above
   * luminance 0.96 (Rec. 709; must be 0); soft: partly weighted pixels above it (a record); max: the brightest interior.
   */
  ringCap(): { swords: number; size: number[]; changed: number; interior: number; max: number; over: number; overMax: number; soft: number; softMax: number; nonFinite: number };
  ```

  - **Vì sao các số:**
    - Điểm ảnh "đổi" so bằng bit half-float của ba kênh. Ngoài vòng hai lần vẽ giống nhau từng bit (cổng uniform, mọi chỗ ghi trong `if`, Kiểm 7), nên mọi điểm ảnh đổi đều có trọng số > 0.
    - Lần 2 ghi 1 − trọng số, không ghi trọng số: half-float sát 0 mịn hơn sát 1 nhiều (số kề dưới 1 là 0,99951), nên "nắp áp trọn" đọc được bằng 1 − w ≤ 1e-4. Ở trong lòng đĩa w đúng bằng 1: ngọc có độ bão hòa 0,03–0,05, độ sáng 0,48–0,72, nên mọi `smoothstep` của `RING` bão hòa.
    - Ngưỡng 0,96, không phải 0,951: một điểm ảnh có 1 − w tới 1e-4 vẫn được cộng (1 − w) × độ sáng chưa nắp, tới 0,005 khi ánh vàng kim dưới đèn chớp tới 50; thêm sai số làm tròn half-float. Ngưỡng 0,96 vẫn dưới ngưỡng 1 của bloom 4 %, cùng hệ số. Nắp hỏng (chèn sai chỗ, số hạng cộng sau nắp, sai hệ số, thiếu `if`) lệch hàng chục phần trăm, không lọt.
    - Sương của lab là `BACKGROUND` `#b9c0c4`, tuyến tính khoảng (0,49; 0,53; 0,55), độ sáng khoảng 0,52, dưới 0,95. Sương chỉ trộn về màu đó, nên không đẩy một điểm ảnh đã nắp qua 0,96; lần 0 và 1 giữ sương như khung thật.
  - Chi phí: ba lần vẽ riêng kiếm, ba lần đọc 1920 × 1080 × 8 byte, chỉ khi kịch bản gọi (lúc chụp), không mỗi khung.

### 5. Công cụ đo cho Claude

- **`scripts/visual/scenarios/lab-element-parity.mjs`:** thêm `MASK=1`. Sau mỗi ảnh:
  - ngay sau `page.shot`, trước mặt nạ: `const b = await page.eval("window.__lab.bright()")` (cả khung), ghi `bright: { pixels: b.pixels, sum: b.sum, max: b.max, nonFinite: b.nonFinite }` vào mục của ảnh đó trong `shots` (đã ghi ra `shots-<PHASE>.json` như hôm nay). Đây là bộ đệm sáng của bloom ở đúng khung vừa chụp: **chỉ để ghi**, Kiểm 8 không đặt ngưỡng trên nó;
  - ngay sau đó: `const c = await page.eval("window.__lab.ringCap()")`, ghi nguyên `ringCap: c` vào cùng mục. Gọi sau `bright()`, vì `ringCap` vẽ lại khung và bộ đệm sáng là của lần vẽ cuối. Đây là cổng của Kiểm 8;
  - `await page.eval("window.__lab.swordMask(true, true)")` (có `all`: cả kiếm cắm của nạn nhân và kiếm trời K5, §4);
  - chụp vào `raw-<PHASE>-mask/<cùng tên>.png`;
  - `await page.eval("window.__lab.swordMask(false)")`.

  Không có `MASK` thì kịch bản chạy y như cũ, không gọi `bright()` hay `ringCap()`. Ghi một dòng chú thích ở đầu tệp.
- **`scripts/visual/ring-parity.mjs`** (mới; Node thuần):
  - Đọc PNG bằng `zlib.inflateSync`: 8 bit, kiểu màu 2 (RGB) và 6 (RGBA), không interlace, đủ 5 bộ lọc kể cả Paeth. Định dạng khác thì báo lỗi rõ. Không có `pngjs` trong `node_modules`, không cài.
  - Gọi: `node scripts/visual/ring-parity.mjs <dir>`. `<dir>` có `raw-before/`, `raw-after/`, `raw-before-mask/`, `raw-after-mask/`, và `shots-before.json`, `shots-after.json` của kịch bản. Biến môi trường `DILATE` (mặc định 3) và `NEAR` (mặc định 16).
  - Với mỗi ảnh trong `raw-before`:
    - **Mặt nạ vòng** = điểm ảnh của `raw-before-mask` có G ≥ 128 và R < 128 (dải chắn có vòng). Giãn vuông `DILATE` px. Ghi `box` = hộp bao của mặt nạ (chưa giãn) theo phần khung `[x0, y0, x1, y1]`, y xuống, như tham số của `__lab.bright`; không có điểm ảnh nào thì `null`.
    - **Ngoài mặt nạ giãn:**
      - số điểm ảnh khác nhau (bất kỳ kênh RGB nào lệch > 0) và Δ lớn nhất;
      - tách hai phần theo khoảng cách tới mặt nạ: ≤ `NEAR` px và > `NEAR` px, mỗi phần ghi số điểm ảnh và Δ lớn nhất.
    - **`bright`** (chỉ để ghi): ghép theo tên ảnh mục `bright` của `shots-before.json` và `shots-after.json`; ghi `{ before, after, ok }`, với `ok` = `after.pixels ≤ before.pixels` và `after.sum ≤ before.sum` và cả hai `nonFinite` = 0. Thiếu tệp hay thiếu mục thì `bright: null`, không báo lỗi.
    - **`ringCap`:** mục `ringCap` của ảnh đó trong `shots-after.json`, chép nguyên, thêm `ok` = `over` = 0 và `nonFinite` = 0. Thiếu thì `ringCap: null`, không báo lỗi.
    - **`keep`** = số điểm ảnh xanh của `raw-after-mask` / số điểm ảnh xanh của `raw-before-mask`.
    - **Điểm ảnh đã đổi** trong mặt nạ (Δ lớn nhất ≥ 6/255), với số đo màu OKLab (công thức Björn Ottosson; sRGB → tuyến tính → LMS → căn bậc ba):
      - nhóm **ngọc**: điểm ảnh đã đổi có độ bão hòa HSV của ảnh sau < 0,15. Ghi số điểm; trung vị L của ảnh sau và ảnh trước; trung vị độ màu C = √(a² + b²) của ảnh sau; khoảng tứ phân vị (IQR) của L ở ảnh sau và ảnh trước;
      - nhóm **vàng**: điểm ảnh đã đổi có sắc HSV 20–55° và độ bão hòa ≥ 0,2 ở ảnh sau. Ghi số điểm và trung vị sắc của ảnh sau.
  - In JSON ra màn hình và ghi `<dir>/ring-parity.json`: từng ảnh và tổng. Tổng có thêm: số ảnh `ringCap.ok` sai, số ảnh thiếu `ringCap`, tổng `soft` và `softMax` lớn nhất của `ringCap`, và số ảnh `bright.ok` sai (để ghi).
- **`scripts/visual/jade-ring-measure.ts`** (mới):
  - Đọc GLB không qua `GLTFLoader`: chép `readGlbScene` của tệp tham chiếu.
  - Dựng hình như game: `bladeFromObject` với `keepUv`; LOD dùng `bladeMap` của model đầy đủ.
  - Gọi `guardBand`, `edgeField`, `auraAnchorsOf`, `jadeRingOf`; in JSON cho cả hai model kèm thời gian đo.
  - Đường dẫn GLB mặc định: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/lab/models/weapons/clear-wind.glb` và `clear-wind-swarm.glb`. Chỉ đọc; worktree không có media vì media nằm ngoài git. Cho phép truyền đường dẫn qua tham số.
  - Phải qua `tsc` (tsconfig gồm `scripts/**/*.ts`).
  - Chạy: `node node_modules/tsx/dist/cli.mjs scripts/visual/jade-ring-measure.ts`. Lưu ý `node_modules/.bin/tsx` là shim shell, không chạy bằng `node` được.

## Làm ở đâu

- **Worktree riêng của Codex:** `games/.wt-immortality-cultivation-codex`, nhánh `codex/jade-ring-material`, gốc là `main` hiện tại của game: `ceb51c2` (merge của phiếu 258 và 258b). Số đo §1 lấy ở `bc94110`; giữa hai mốc không đổi `blades.ts`, `sword-material.ts`, chỉ thêm 4 dòng `flipbookProbe` vào `skills-main.ts`, nên số đo vẫn đúng.
  - Claude đã tạo trước khi chạy phiếu: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-immortality-cultivation-codex -b codex/jade-ring-material main`, rồi symlink `node_modules` sang thư mục của game như phiếu 255. Lúc giao phiếu, `git status --short` trong worktree chỉ in `?? node_modules`.
  - `node_modules` là symlink sang `games/immortality-cultivation/node_modules`: không sửa, không cài thêm gói. Mọi thứ ghi vào `node_modules/` là ghi vào game, nên Vitest và Vite chỉ chạy đúng lệnh ở Kiểm 2 và 3.
- **Không ghi gì trong `games/immortality-cultivation/`:** agent khác đang sửa ở đó. Chỉ đọc GLB ở `art-src` của nó cho Kiểm 5.

### Được ghi
- `games/.wt-immortality-cultivation-codex/src/view/skills/sword-material.ts`, `src/view/skills/blades.ts`;
- `games/.wt-immortality-cultivation-codex/src/lab/skills-main.ts`: chỉ hai cờ, khối chú thích, `__lab.jadeRing`, tham số `all` của `__lab.swordMask`, `__lab.ringCap` và hai tên thêm vào dòng import `sword-material` (đúng các khối ở §4, cả các dòng khai trong interface `__lab`);
- `games/.wt-immortality-cultivation-codex/scripts/visual/scenarios/lab-element-parity.mjs`: chỉ `MASK=1` (mặt nạ, mục `bright` và mục `ringCap`, §5);
- `games/.wt-immortality-cultivation-codex/scripts/visual/ring-parity.mjs`, `scripts/visual/jade-ring-measure.ts` (mới);
- `games/.wt-immortality-cultivation-codex/tests/view/jade-ring.test.ts` (mới);
- `games/.wt-immortality-cultivation-codex/docs/changelog/2026-11-04-lab-jade-ring.md`;
- `/Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/259-report.md`.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`.
- Sửa `real-swords.ts`, `hand-sword.ts`, `aura-gates.ts`, `victims.ts`, `sword-skills.ts`, các lớp hào quang (`aura-mantle.ts`, `sword-aura.ts`, `element-*.ts`), `AuraAnchors` và các trường của nó, `guardBand`, `bladeFromObject`, `edgeField`.
- Sửa đường mép, `HEAT_BAND`, `SWORD_LOOK`, `SWORD_LIGHT`, `DISSOLVE`, `JADE`, và `EMIT` hay `OUTGOING` ngoài đúng các dòng ghi ở §2.
- Thêm `discard`, `#define`, `#ifdef` hay biến thể chương trình; đổi `customProgramCacheKey`.
- Sửa texture, GLB, atlas, `art-src/**`, `public/**`, script Blender; chạy Blender.
- Sửa `src/sim/**`, `src/content/**`, `src/kit/**`, golden test, file khác ngoài danh sách được ghi, hay bất cứ thứ gì trong `games/immortality-cultivation/`.
- Chạy dev server, mở trình duyệt, tải gói hay ảnh.
- Chạy Vitest thiếu `--no-cache --configLoader runner`, hay Vite thiếu `--configLoader runner` và `IC_VITE_CACHE_DIR` (xem Kiểm 2, 3).
- Cấp phát bộ nhớ mỗi khung. Phép đo chỉ chạy lúc nạp.

## Việc

1. **`sword-material.ts`:** `CrestPlane`, `JadeRing`, `JADE_RING_LOOK`, `SwordMaterialOptions.ring`, 8 uniform, chunk `RING`, dòng ánh ngọc trong `EMIT`, nắp 0,95 trong `OUTGOING` (hệ số Rec. 709, ánh mép tan ngoài nắp, nhánh đọc trọng số khi `uSwRingOn` > 1,5), `throw` khi thiếu `metalnessmap_fragment`. Đúng §2. Cập nhật chú thích đầu tệp: thêm một gạch về đĩa ngọc.
2. **`blades.ts`:** `jadeRingOf` đúng §1 và tệp tham chiếu; `SwordModel.jadeRing`; nối vào `modelOf`.
3. **`skills-main.ts`:** đúng §4 (hai cờ, `__lab.jadeRing`, `__lab.swordMask(on, all)`, `__lab.ringCap()`).
4. **Công cụ:** `lab-element-parity.mjs` (`MASK=1`), `ring-parity.mjs`, `jade-ring-measure.ts`, đúng §5.
5. **Test `tests/view/jade-ring.test.ts`** (không cần trình duyệt):
   - **Vòng tổng hợp.** Ghép bằng `mergeGeometries(parts, false)` từ:
     - `TorusGeometry(0.067, 0.023, 24, 96).rotateX(2.4°)` (đĩa nghiêng);
     - hai `RingGeometry(0.088, 0.106, 96)` ở z = +0,004 và z = −0,004; tấm sau `rotateY(π)` trước khi dời;
     - `TorusGeometry(0.113, 0.012, 16, 96)` (vành);
     - `SphereGeometry(0.012, 16, 12)` ở (0,075 cos 30°; 0,075 sin 30°; 0,028) (hạt);
     - tất cả phần trên dời (0; −0,0274; 0);
     - `BoxGeometry(0.08, 0.92, 0.01)` ở (0; 0,54; 0) (lưỡi);
     - `CylinderGeometry(0.015, 0.015, 0.33, 12)` ở (0; −0,285; 0) (chuôi).

     Gọi `guardBand`, `edgeField`, `auraAnchorsOf(…, true)`, `jadeRingOf(g, guard, aura.guardHalf)`. Phải ra (bản tham chiếu cho x 0, y −0,0274, `rIn` 0,0440, `rCut` 0,0891, front a 0,0230 / by 0,0445, back by −0,0445, `margin` 0,00275):
     - |x| ≤ 0,001;
     - |y + 0,0274| ≤ 0,001;
     - |`rIn` − 0,044| ≤ 0,001;
     - 0,088 ≤ `rCut` ≤ 0,0905 (chân xuyến, nơi bề dày xuống dưới `thr` ≈ 0,012; không còn ở giữa gờ 0,088–0,106);
     - |front.a − 0,023| ≤ 0,0008, |back.a − 0,023| ≤ 0,0008;
     - |front.by − 0,042| ≤ 0,006, |back.by + 0,042| ≤ 0,006;
     - |bx| ≤ 0,003 cả hai;
     - |`margin` − 0,00276| ≤ 0,0002.
   - Cùng vòng nhưng bỏ hạt và độ nghiêng: front.a lệch bản có hạt ≤ 0,0003 (hạt không kéo mặt phẳng lên).
   - Thay xuyến bằng đĩa đặc `CylinderGeometry(0.09, 0.09, 0.046, 96).rotateX(π/2)`: `null`. Một lưỡi trơn `BoxGeometry(0.08, 1, 0.01)` dời lên 0,5: `null`.
   - **`fail`:** gọi lại hai ca `null` trên với `fail` ghi vào một mảng. Mỗi ca gọi `fail` đúng một lần, với tên bước trong danh sách §1 (tham chiếu: đĩa đặc `"hole-seed"`, lưỡi trơn `"hole-open"`). Vòng tổng hợp có `fail` thì không gọi lần nào.
   - `patchSwordMaterial` với một `MeshStandardMaterial`. Gọi `material.onBeforeCompile` với `{ uniforms: {}, vertexShader: THREE.ShaderLib.standard.vertexShader, fragmentShader: THREE.ShaderLib.standard.fragmentShader }`, tham số renderer là đối tượng rỗng. Kiểm:
     - chunk `RING` đứng sau `#include <metalnessmap_fragment>` và trước `#include <normal_fragment_begin>`;
     - dòng ánh ngọc đứng sau khối `if (uSwMode > 0.5)` của `EMIT` và trước `totalEmissiveRadiance += swJadeE;`;
     - nắp 0,95 đứng sau phần `OUTGOING` cũ (sau dòng `outgoingLight -= swJadeE * …`), và chứa, theo đúng thứ tự này, ba dòng `vec3 swRingDe = uSwEdge * swDe * 0.7;`, `float swRl = dot(outgoingLight - swRingDe, vec3(0.2126, 0.7152, 0.0722));`, `if (uSwRingOn > 1.5) outgoingLight = vec3(1.0 - swRingW, swRingJ, swRingG);`; shader không còn chuỗi `dot(outgoingLight, vec3(0.299, 0.587, 0.114))`;
     - `uSwRingC.value.w` bằng 0 khi không có `ring`, bằng 1 khi có;
     - shader thiếu `#include <metalnessmap_fragment>` làm `onBeforeCompile` ném lỗi.
   - `JADE_RING_LOOK` mặc định đúng các số ở §2.
6. **Changelog tiếng Việt:** làm gì và vì sao (texture đã đúng màu, ORM làm crôm), các số đo, hai cờ, `__lab.jadeRing`, các công cụ, cách thử.

## Kiểm bắt buộc

**Codex chạy** trong `games/.wt-immortality-cultivation-codex`, ghi lệnh và kết quả vào báo cáo:
1. `node node_modules/typescript/bin/tsc --noEmit -p .`: không lỗi.
2. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`: mọi test qua; trước **917 test, 86 tệp** (mốc `ceb51c2`), sau = 917 + số test của `jade-ring.test.ts`, 87 tệp; test golden không đổi. `--no-cache` và `--configLoader runner` là bắt buộc: thiếu chúng, Vitest 3.2.7 nạp cấu hình kiểu `bundle` (ghi tệp tạm vào `node_modules/.vite-temp/`) và ghi bộ đệm kết quả dưới `node_modules/.vite/`. `node_modules` của worktree là symlink sang game, nơi agent khác đang làm, nên cả hai thành ghi vào `games/immortality-cultivation/` (báo cáo 255 dòng 57; phiếu 258, Kiểm 2).
3. Xóa `/private/tmp/codex-259-dist` nếu còn, rồi `IC_VITE_CACHE_DIR=/private/tmp/codex-259-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-259-dist --configLoader runner`: thoát 0. `--configLoader runner` và `IC_VITE_CACHE_DIR` là bắt buộc: Vite 7.3.7 mặc định nạp cấu hình kiểu `bundle`, ghi tệp tạm vào `node_modules/.vite-temp/`, và `cacheDir` mặc định là `node_modules/.vite` (`vite.config.ts` chỉ đổi nó khi có `IC_VITE_CACHE_DIR`); cả hai đi qua symlink vào game (báo cáo 255 dòng 57; phiếu 258, Kiểm 3). Rồi `grep -rl "jadeRingGlow\|ring-parity" /private/tmp/codex-259-dist` **không in đường dẫn nào** (thoát 1 là đúng), vì lab và công cụ không lọt vào bản build. Cuối cùng xóa `/private/tmp/codex-259-dist`.
4. Trong worktree: `git diff --stat` và `git status --short`. (Từ gốc repo cha thì dùng `git -C games/.wt-immortality-cultivation-codex …`; trong worktree đường dẫn đó không tồn tại.) Yêu cầu: chỉ các file được ghi, cộng symlink `node_modules` có sẵn. `?? node_modules` luôn hiện, vì mẫu `node_modules/` trong `.gitignore` chỉ khớp thư mục, không khớp symlink (báo cáo 258 dòng 96); không sửa `.gitignore`. Tệp mới chưa theo dõi chỉ hiện ở `status --short`. Báo cáo `docs/codex-queue/259-report.md` nằm ở repo cha nên không hiện ở đây.
5. `node node_modules/tsx/dist/cli.mjs scripts/visual/jade-ring-measure.ts`: hai model ra khác `null`. Mọi số khớp bảng §1 trong 1e-4, vì cùng thuật toán. Lệch hơn thì ghi số và lý do. Ghi thời gian đo.

**Claude chạy khi nhận.** Codex không có server hay trình duyệt.
- Môi trường: bản cố định không HMR, High, 1920 × 1080, DPR 1, chạy qua `.local/bin/heavy.sh --gpu`.
- Mọi lần chạy `lab-element-parity.mjs` dùng cùng kế hoạch và cùng `ONLY`.
- Ảnh và JSON vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/jade-ring/` (skill `review-folder`, có `ABOUT.md`, chạy `node scripts/review-index.mjs`). Xóa khung thô sau khi đo bằng `tools/capture-prune/prune.mjs`.

6. **Đọc mã và chạy lại:** đọc diff, chạy lại Kiểm 1–5.
   - Trong lab: console không có lỗi shader hay `[sword-material]`, không có cảnh báo `[blades] … jade ring not measured`.
   - `__lab.jadeRing()` khớp số Node trong 1e-4.
   - **Gờ nối giữ nguyên, nét vàng đổi đủ:** từ thư mục game chính, `node node_modules/tsx/dist/cli.mjs ../../docs/codex-queue/259/ring-sim.ts ../.wt-immortality-cultivation-codex` (đo bằng `jadeRingOf` của Codex). Yêu cầu, ở cả bốn mặt chiếu (đầy đủ và LOD, trước và sau):
     - tỉ lệ điểm ảnh đổi ở dải r 0,092–0,102 ≤ 3 % (tham chiếu 1,8 / 1,4 / 0,0 / 0,0 %);
     - tỉ lệ đổi ở dải nét vàng 0,084–0,092 ≥ số tham chiếu − 1 điểm (tham chiếu 37,7 / 33,9 / 40,9 / 36,1 %);
     - lệnh in `PASS`, mã thoát 0.
7. **Tắt bằng cũ:** bản mới với `QS="&jadeRing=off"` so với bản cố định dựng từ `main` trước phiếu.
   - `ELEMENT=metal` rồi `ELEMENT=fire`, không `MASK`.
   - Yêu cầu: 0 điểm ảnh khác ở mọi khung.
8. **Vòng giữ và trùng khít ngoài vòng:**
   - Mỗi cặp chạy (nguyên tố × bloom) vào một `OUT_DIR` riêng dưới `captures/tu-tien/jade-ring/`: `nobloom-metal`, `nobloom-fire`, `bloom-metal`, `bloom-fire`. Tên `raw-before`, `raw-after` lặp lại giữa các cặp, chung thư mục sẽ ghi đè.
   - **Bloom 0** (chứng minh ngoài vòng giữ nguyên):
     - chạy `MASK=1 QS="&bloom=0&jadeRing=off" PHASE=before`, rồi `MASK=1 QS="&bloom=0" PHASE=after`, cho Metal và cho Fire. Chạy `ring-parity.mjs`;
     - mặt nạ của `MASK=1` gồm mọi lưới mang vật liệu `"real-sword"` (`swordMask(true, true)`, §4): kiếm bay, kiếm vạn kiếm, kiếm solo, kiếm cắm của nạn nhân (k7, K5) và kiếm trời K5 (k5-140/175/230). Trước khi đo, xem một ảnh mặt nạ k7 và một ảnh k5-175: hai loại kiếm này phải có dải xanh lá. Thiếu thì dừng, báo lại, không nới yêu cầu;
     - yêu cầu: `keep` ≥ 0,95 ở mọi khung (hình không đổi nên phải ra 1), và 0 điểm ảnh khác ngoài mặt nạ giãn 3 px.
   - **Bloom mặc định** (vòng bớt bloom): chạy `MASK=1 QS="&jadeRing=off" PHASE=before`, rồi `MASK=1 QS="" PHASE=after`, cho Metal và cho Fire. Chạy `ring-parity.mjs`. Yêu cầu:
     - `keep` ≥ 0,95 ở mọi khung;
     - `bright` cả khung (`pixels`, `sum`, `max`, `nonFinite`, và `bright.ok`): **chỉ ghi, không có ngưỡng** (lượt phản biện 4, lỗi 1). Lý do: bản làm đúng vẫn có thể làm `pixels` hay `sum` tăng, vì hai cớ:
       - (a) Nắp chỉ giới hạn mảnh của chính kiếm. Các lớp trong suốt vẽ sau và đè lên điểm ảnh kiếm: thẻ hào quang của kiếm khác ở K7, lửa và vệt SilkTail của Fire, tia lửa, ảnh trúng. Cổng "Chồng lớp" cho tới 2 lớp trong suốt mỗi điểm ảnh trong vùng kiếm (`aura-gates.ts`, `partsCoverage`) chính vì chúng đè lên kiếm. Mà phiếu cố ý làm đĩa sáng hơn: Kiểm 9 đòi L sau ≥ L trước + 0,04; ánh ngọc trong 0,044–0,30; kim loại 0,15 → 0 nâng phần khuếch tán (× 1 / (1 − kim loại)); ở Fire đĩa cũ bị `uSwChar` 0,4 nhân tối (`FIRE_BLADE`), đĩa mới thì không, sáng hơn khoảng 2,5–3 lần. Nên một điểm ảnh đĩa bị đè mà đã trên ngưỡng thì cộng thêm vào `sum`, còn điểm ảnh sát dưới ngưỡng thì vượt qua.
       - (b) `UnrealBloomPass` của three r170 dựng `renderTargetBright` ở nửa độ phân giải (`resx = Math.round(resolution.x / 2)`), lọc từ target HalfFloat của composer (mặc định `LinearFilter`). Mỗi texel sáng vì thế là trung bình 2 × 2 điểm ảnh đủ cỡ, rồi mới so ngưỡng `luminance()` ≥ 1. Một điểm ảnh đĩa sáng hơn nằm cạnh một điểm lóe không đổi đã trên ngưỡng (bạc khối chữ V, mây, hạt, vành khi kiếm nhỏ) làm texel đó sáng thêm. Khung nào đĩa cũ không có điểm lóe riêng (nhất là Fire) thì `sum` cả khung tăng.
       - Cả hai cớ không nói gì về nắp. Nắp được đo thẳng bằng `ringCap` ở dưới.
     - điểm ảnh khác ngoài mặt nạ giãn (≤ 16 px và > 16 px): **chỉ ghi số và Δ lớn nhất để tham khảo, không có ngưỡng.** Lý do: bloom của three r170 (`UnrealBloomPass`, `src/kit/three/stage.ts`; lab: strength 0,45, radius 0,12, threshold 1) lấy nguyên màu điểm ảnh trên ngưỡng, làm mờ qua 5 mip ở 1/2 tới 1/32 độ phân giải, nhân 3/5/7/9/11 (bán kính 2/4/6/8/10 texel), mip sau nạp từ mip trước. Một điểm ảnh trên ngưỡng đổi thì lan tới khoảng 4 + 16 + 48 + 128 + 320 ≈ 516 px ở 1920 × 1080; riêng mip 2 đã tới khoảng 68 px. Vòng cũ có ánh gương trên 1: kim loại trung vị 0,15, nhám 0,22–0,26 dưới mặt trời 1,4 cho đỉnh GGX ước khoảng 6 (tuyến tính, trước tone map), và mặt xuyến có đủ hướng pháp tuyến nên gần như khung nào thấy vòng cũng có điểm lóe; chớp trúng cũ cũng cộng tới 0,57. Vòng mới có nắp 0,95. Bỏ các điểm lóe đó là đúng ý phiếu, nhưng làm điểm ảnh xa đổi vài phần của một mức 8 bit, đủ lật làm tròn ở nhiều điểm ảnh.
   - **Nắp của đĩa** (`ringCap`, §4), đọc từ `ring-parity.json` của cả bốn cặp (mục `ringCap` lấy từ `shots-after.json`). Yêu cầu:
     - `ringCap.ok` đúng ở **mọi khung**: `over` = 0 (không điểm ảnh nào nắp áp trọn mà độ sáng Rec. 709 > 0,96) và `nonFinite` = 0;
     - phép đo chạy thật: ở khung k1z, Metal và Fire, `swords` ≥ 1, `changed` > 0 và `interior` ≥ 0,5 × `changed`. Không đạt thì lần đọc trọng số hỏng: dừng, báo lại, không coi `over` = 0 là đạt;
     - `soft`, `softMax` (điểm ảnh trọng số giữa 0 và 1 trên 0,96: mép hình của vùng đổi, chỗ chuyển màu của nét vàng): **chỉ ghi**, không có ngưỡng. Phần lớn chất liệu của chúng là chất liệu cũ, mà vòng cũ thì bloom không nắp. Nếu ảnh của Kiểm 12 cho thấy một đốm bloom ở mép đĩa, Claude mở một phiếu nhỏ cho nắp;
     - `max` của khung k1z, Metal và Fire, ghi vào báo cáo nhận.
   - `ringCap.ok` sai ở khung nào: dừng, không nới, không nhận phiếu. Đó là điểm ảnh nắp áp trọn mà vẫn vượt, tức là nắp sai trong mã: chèn sai chỗ, có số hạng cộng sau nắp, sai hệ số, thiếu `if`, hay `swRingDe` khác số hạng cuối của `EMIT`. Ghi khung, `over`, `overMax` và ảnh, rồi sửa theo đúng §2.
   - `bright.ok` sai ở khung nào mà `ringCap.ok` đúng: không phải lỗi, ghi vào báo cáo. Để thấy chỗ tăng nằm ở vòng, gọi `__lab.bright(x0, y0, x1, y1)` với `box` của khung đó (ring-parity) ở cả hai bản, ghi cả hai số. Chỗ tăng nằm ngoài `box` (giãn thêm 16 px) thì là chuyện khác: dừng, báo lại.
   - Ước tính đỉnh GGX ở trên là số tính tay (F0 ≈ 0,14, α² ≈ 0,0033, NL = NV ≈ 0,7), chưa đo trong trình duyệt; `bright` của bản trước ở k1z ghi luôn vào báo cáo nhận để xác nhận.
9. **Màu,** khung k1z, Metal, từ `bloom-metal/ring-parity.json` (bloom mặc định):
   - nhóm ngọc:
     - trung vị L sau ≥ 0,78, và ≥ trung vị L trước + 0,04 (trắng hơn crôm);
     - trung vị C sau ≤ 0,035 (trắng trung tính, không ngả màu);
     - IQR(L) sau ≤ 0,75 × IQR(L) trước (bớt vệt gương);
   - nhóm vàng, nếu có ≥ 20 điểm ảnh: trung vị sắc 25–50°.
   - Nếu chỉ hụt ngưỡng L tuyệt đối mà các ngưỡng tương đối đạt: thử `?jadeRingGlow` tăng từng 0,02, tối đa 0,12. Ghi giá trị đạt; nếu cần thì đổi mặc định bằng một sửa nhỏ, ghi vào changelog. Còn hụt thì báo anh kèm ảnh.
   - Fire chỉ ghi số để tham khảo, không có ngưỡng.
10. **Thời gian:** `lab-element-perf.mjs`, phím 7, High, `QS="&jadeRing=off"` và `QS=""` xen kẽ A/B/B/A.
    - Chênh p95 ≤ 0,05 ms.
    - Mọi cửa sổ ≤ 11,5 ms.
11. **Chỗ chuyển kiếm giữa và kiếm xa:** khung k7 có cả kiếm giữa (LOD) và impostor gần ngưỡng chuyển.
    - So trung vị độ sáng vùng vòng của kiếm giữa sau khi đổi với impostor: lệch ≤ 15 % thì đạt.
    - Lệch hơn thì ghi số và mở phiếu nướng lại atlas, không sửa ở phiếu này.
12. **Ảnh trước và sau cho anh:**
    - Gồm: cận cảnh phím 1 (k1z) Metal và Fire; camera chơi phím 7; từng cặp `jadeRing=off` / bật, đặt cạnh ảnh đã duyệt.
    - Ghi chú cho anh: kiếm cầm tay của nhân vật chưa đổi (ngoài phạm vi).
    - Bản gửi anh vào `owner-review/2026-11-04/tu-tien/jade-ring/`.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Nhận
- Thay đổi nằm trong worktree, chưa commit. Claude đọc diff, chạy lại Kiểm 1–5, chạy Kiểm 6–12, gửi anh ảnh trước và sau.
- Chỉ khi anh duyệt màu mới gộp vào `main`. Anh chê thì chuyển sang vẽ lại texture UV (kế hoạch §4), không chỉnh mãi shader.
- Báo cáo ghi:
  - từng việc 1–6 đã làm ở đâu (tệp và hàm);
  - bảng số đo của hai model so với bảng §1;
  - chỗ phải làm khác và vì sao;
  - kết quả Kiểm 1–5.

## Ngoài phạm vi
- **Kiếm cầm tay trong lab** (`src/lab/hand-sword.ts`): vật liệu riêng, chưa dùng `patchSwordMaterial`, nên vòng vẫn xám. Sau khi anh duyệt màu sẽ có một phiếu nhỏ dùng lại `jadeRingOf` và chunk `RING`.
- **Mây sứ và đế hạt:** giữ như hôm nay, vì nằm trên mặt phẳng đỉnh nên bị loại. Nếu anh muốn mây cũng thành sứ mờ như ngọc thì mở phiếu riêng, cùng bộ phân loại, vùng rộng hơn.
- **Atlas impostor:** không nướng lại (xem Kiểm 11). Không vẽ lại texture.

## Quyết định với các ý của ChatGPT (lượt 1 và lượt tự duyệt 1)

| Ý | Quyết | Căn cứ |
|---|---|---|
| Lỗi 1: gộp khoảng theo tia có thể lấp lỗ bằng khâu, chuôi, mây | Không dùng tia. Dùng bản đồ độ cao và loang lỗ; loang chạm biên thì `null` | Lỗ sạch trên cả hai mặt chiếu của hai model; diện tích loang ra `rIn` 0,0440 đúng hình tròn |
| Lỗi 2: tìm vành bạc theo đổi pháp tuyến chưa rõ | Không tìm vành. `rCut` ở mép trong gờ nối (đầu trong đoạn mỏng), sửa sau phản biện | Bề dày: đĩa 0,052, gờ 0,0105, vành khoảng 0,04. Gờ và vành nằm ngoài `rCut`, giữ nguyên; màu gờ không tách được khỏi nét vàng (xem "Phản biện", lỗi 2) |
| Lỗi 3: `#ifdef` không có macro | Cổng bằng uniform `uSwRingC.w × uSwRingOn` | Một chương trình, `"real-sword"` |
| Lỗi 4: mặt nạ bán kính bắt nhầm phần khác | Bán kính, cộng hai mặt phẳng đỉnh, cộng `1 − swJade`, cộng phân loại theo màu map | Mô phỏng trên map thật: chỉ đĩa và nét vàng của nó đổi |
| Lỗi 5: giảm normal map 15 % | Bỏ | Giữ nét chạm |
| Lỗi 6: đường Fire chưa đủ | Ghi đủ từng đường ở §2 | |
| Lỗi 7: miễn mép tan cho vòng | Không miễn | Vòng tan cùng kiếm; ánh mép tan nằm ngoài nắp 0,95, nên trên đĩa sáng như trên lưỡi (lượt phản biện 4) |
| Lỗi 8–10: elip impostor, alpha, nắp bloom ở impostor | Impostor không đổi | Atlas Blender đã sáng; vòng ở kiếm xa 5–21 px; Kiểm 11 |
| Lỗi 11: kiểm màu cần quy trình cố định | Ngưỡng trên cùng khung, cùng đèn, trước và sau (Kiểm 9) | |
| Đo riêng LOD | Đồng ý | Tâm, `rIn`, `rCut` và `a` của LOD lệch model đầy đủ ≤ 0,0005; độ dốc lệch ≤ 0,003 |
| Dải chỉ vàng bằng hình học (0,020 / 0,025 × `rOut`); chỉ vàng ở mép lỗ | Bỏ cả hai | Nét vàng đã vẽ trên texture đúng chỗ ảnh đã duyệt; mép lỗ trong ảnh đã duyệt không có chỉ vàng |
| Ngọc nhám 0,58; vàng kim loại 0,72, nhám 0,32 | Ngọc 0,34; vàng 0,85 / 0,30 | 0,58 ra phấn, trái yêu cầu "không như phấn"; ngọc trong ảnh đã duyệt bóng mềm |
| Ánh viền giả trong mờ 0,018 theo góc nhìn | Thay bằng ánh trong 0,06 qua `swJadeE` | Đi qua luật lấp khoảng trống sẵn có; có núm `?jadeRingGlow` |
| Kẹp kênh 0,86 trước `opaque_fragment` | Nắp độ sáng 0,95 theo trọng số vòng | Giữ màu, không làm phẳng ngọc thành 0,86; cùng ngưỡng 0,95 với `OUTGOING`, nhưng đo bằng hệ số Rec. 709 của bloom (lượt phản biện 4) |

## Phản biện

### Lượt 1

Lượt phản biện của một agent Claude độc lập (04/11/2026, chiều): **FAIL**, ba lỗi. Claude kiểm từng lỗi trên mã và số đo, cả ba đều đúng và đã sửa. Không bác lỗi nào. Sau lần sửa này đếm lại hai lượt PASS từ đầu.

| Lỗi | Kiểm lại | Đã sửa |
|---|---|---|
| 1. Kiểm 8 không thể đạt: mặt nạ thiếu kiếm cắm của nạn nhân và kiếm trời K5, hai lưới này cũng mang vật liệu mới | Đúng. `drawSwordMask` chỉ giữ các lưới truyền vào và ẩn phần còn lại (`aura-gates.ts`, `hideAllBut`). `swordMask` (`skills-main.ts`) chỉ truyền `fx.blades.mesh`, `d.lead`, `auraSolo.blade.mesh`, `fx.blades.swarm`, `d.mid`. `victims.ts` dựng `new BladeSet(PINS, 1.1, PINS)` và `setSword(…full)`; `sword-skills.ts:887` đặt kiếm trời bằng `overlayModel(models.full)`, vá lại bằng `model.look`. Cả hai mang `"real-sword"`, nên có vòng mới | §4: `__lab.swordMask(on, all = false)` với khối mã đầy đủ; `all` thêm mọi `InstancedMesh` trong `view.scene` có `customProgramCacheKey() === "real-sword"`, bỏ lưới đã có. §5: `MASK=1` gọi `swordMask(true, true)`. Phạm vi được ghi của `skills-main.ts` nới đúng chỗ này; cấm sửa `aura-gates.ts`, `victims.ts`, `sword-skills.ts`. Kiểm 8 thêm bước xem ảnh mặt nạ k7 và k5-175 trước khi đo. Chọn cách mở rộng mặt nạ, không chọn "chỉ k1/k1z, khung khác ghi tham khảo", vì Kiểm 7 và Kiểm 11 cần k7 và K5 cùng kế hoạch |
| 2. Sai số liệu gờ nối: độ bão hòa của gờ trên `swC` tuyến tính là 0,54–0,59, không phải 0,26; vùng 0,092–`rCut` không được giữ | Đúng. Claude đo lại trên map 4096² (texel trong vùng dưới hai mặt phẳng đỉnh, theo dải 0,001): gờ ở 0,092–0,097 có độ bão hòa tuyến tính 0,52–0,59, độ sáng 0,17–0,19, `swGk` trung bình 0,55–0,75; 0,26 là độ bão hòa sRGB của nửa ngoài. Mô phỏng mặt chiếu 2.000 px/đơn vị của Claude (cùng tổng số với phiếu cũ: 43.976 / 8.325) cho dải 0,092–0,097 đổi 38,5 % ở mặt trước, 29,5 % ở mặt sau. Lời phản biện đếm 6.121 điểm ảnh trên dải 0,092–`rCut`, tức đếm khác vùng, nhưng cùng kết luận. Cổng độ sáng không tách được, như lời phản biện nói | Chọn cách (a): `rCut = rs[a0]`, đầu trong của đoạn mỏng (§1 bước 4). Giữ gờ đúng như thiết kế đã chốt, và đúng ảnh đã duyệt: rãnh giữa đĩa và khung bạc tối, không phải vàng. Không chọn cách (b), đổi cả gờ thành vàng tới `rs[a1]`: trái ảnh đã duyệt, đáy vùng đổi xuống −0,128, dưới `guardFrom` −0,125, tức ra ngoài dải xanh lá của mặt nạ. Đã cập nhật: bảng số §1, số tham chiếu và khoảng chấp nhận của vòng tổng hợp (`rCut` 0,088–0,0905), lý do ngưỡng ở §2 (bỏ "0,26"), kết quả mô phỏng, đỉnh vùng đổi 0,065, tệp tham chiếu. Thêm `docs/codex-queue/259/ring-sim.ts` và số bắt buộc ở Kiểm 6: dải 0,092–0,102 đổi ≤ 3 %, dải nét vàng không hụt quá 1 điểm. Còn lại một dải gờ hẹp sát chân đĩa ở những góc chân đĩa vào trong hơn (11–14 % điểm ảnh của gờ, bản cũ 38–41 %); đã ghi ở §2 |
| 3. Mâu thuẫn ở §1: chữ ký cố định của `jadeRingOf` không biết tên model, `modelOf` không biết bước hỏng | Đúng | Tham số thứ tư không bắt buộc `fail?: (step: string) => void`, gọi đúng một lần trước mỗi `null`, với bảy tên bước; `modelOf` truyền một hàm `console.warn` có `source`. Đã thêm vào tệp tham chiếu (đĩa đặc ra `"hole-seed"`, lưỡi trơn ra `"hole-open"`) và một test cho `fail` |

### Lượt 2

Lượt phản biện thứ hai của một agent Claude độc lập (04/11/2026, chiều): **FAIL**, một lỗi. Claude kiểm trên mã của lab và của three 0.170.0 trong `node_modules`: lỗi đúng, đã sửa. Không bác lỗi nào. Một chỗ chọn khác đề xuất, ghi ở cột cuối. Đếm lại hai lượt PASS từ đầu; lượt 3 và 4 còn lại đều phải PASS.

| Lỗi | Kiểm lại | Đã sửa |
|---|---|---|
| 1. Kiểm 8, nửa sau: "0 điểm ảnh khác ở xa hơn 16 px" với bloom mặc định không đạt được với bản làm đúng | Đúng. `stage.ts` dựng `UnrealBloomPass` threshold 1; lab đặt strength 0,45, radius 0,12 (`look.ts`, `applyLook`). Trong three r170: `LuminosityHighPassShader` trả nguyên texel khi độ sáng qua `smoothstep(1; 1,01)`; `nMips` 5, `renderTargetBright` ở 1/2 độ phân giải, mỗi mip nửa mip trước; nhân `[3, 5, 7, 9, 11]`, vòng lặp `i = 1 … KERNEL_RADIUS − 1` nên bán kính 2/4/6/8/10 texel; mip `i` nạp từ `renderTargetsVertical[i − 1]`; `bloomFactors` sau `radius` 0,12 là 0,90/0,75/0,60/0,45/0,30, đều khác 0. Tầm lan cộng dồn: 4, 20, 68, 196, 516 px ở 1920 × 1080. Vòng cũ có điểm trên ngưỡng: ORM kim loại trung vị 0,15 (p90 0,48, đốm 0,61), nhám 0,22–0,26 (đốm 0,10), mặt trời 1,4; tính tay đỉnh GGX khoảng 6, và mặt xuyến có đủ hướng pháp tuyến. Chớp cũ cộng `swC × min(flash; 1,5) × 0,55`, tới 0,57. Vòng mới bị nắp 0,95. Vậy khung nào vòng cũ có điểm lóe thì điểm ảnh xa hơn 16 px đổi, đúng do thay đổi phiếu muốn. Số "lớp thép bloom" trong changelog 03/11 là của lưỡi, không phải vòng: chỉ là bằng chứng phụ, phần vòng dựa trên tính tay | Kiểm 8 tách hai nửa, mỗi cặp chạy một `OUT_DIR` (`nobloom-*`, `bloom-*`). Bloom 0 giữ đúng "0 điểm ảnh khác ngoài mặt nạ giãn 3 px". Bloom mặc định bỏ ngưỡng 16 px; điểm ảnh khác ở ≤ 16 px và > 16 px chỉ ghi số và Δ lớn nhất. Thay bằng `bright.ok` ở **mọi khung**, Metal và Fire: `pixels` và `sum` của `__lab.bright()` sau ≤ trước, `nonFinite` = 0. §5: `MASK=1` ghi `bright` (cả khung, ngay sau ảnh, trước mặt nạ) vào `shots-<PHASE>.json`; `ring-parity.mjs` ghép hai tệp đó, ghi `bright.ok`, `box` của mặt nạ, và số ảnh sai ở tổng. Dòng "Được ghi" của kịch bản ghi thêm mục `bright`. Kiểm 9 đọc `bloom-metal/ring-parity.json`. Khung nào sai: dừng, định vị bằng `__lab.bright(box)`; nếu do mép mềm của nắp thì sửa nắp, không nới. **Chọn khác đề xuất:** ngưỡng đặt trên cả khung, không trên hộp vòng, vì lượt bloom 0 đã chứng minh mọi chênh của bộ đệm sáng đến từ vòng; hộp vòng chỉ dùng để định vị |

### Lượt 3

Lượt phản biện thứ ba của một agent Claude độc lập (04/11/2026, tối): **FAIL**, hai lỗi, cả hai về lệnh kiểm của Codex. Claude kiểm trên worktree, `node_modules` của game và các báo cáo 255, 258, 258b: cả hai lỗi đúng, đã sửa. Không bác lỗi nào. Đếm lại hai lượt PASS từ đầu; lượt 4 và 5 đều phải PASS.

| Lỗi | Kiểm lại | Đã sửa |
|---|---|---|
| 1. Kiểm 2 và 3 trái lệnh cấm ghi của chính phiếu: chạy đúng như viết thì Vitest và Vite ghi vào `games/immortality-cultivation/` | Đúng. `games/.wt-immortality-cultivation-codex/node_modules` là symlink `-> ../immortality-cultivation/node_modules` (`ls -la`). Game dùng Vite 7.3.7 và Vitest 3.2.7 (`package.json` trong `node_modules`). Nạp cấu hình mặc định kiểu `bundle` ghi `node_modules/.vite-temp/`; Vitest ghi bộ đệm kết quả dưới `node_modules/.vite/`; `vite.config.ts` chỉ đổi `cacheDir` khi có `IC_VITE_CACHE_DIR`. Báo cáo 255 dòng 57 và phiếu 258 Kiểm 2, 3 đã bắt buộc các cờ vì đúng lý do này; báo cáo 258 chạy đúng các cờ. Mốc test: `main` của game là `ceb51c2` (merge 258/258b), báo cáo 258b ghi 917/917 test, 86/86 tệp; worktree đã ở `ceb51c2` | Kiểm 2 chép đúng lệnh của 258: `VITEST_MAX_THREADS=4 … run --no-cache --configLoader runner --maxWorkers 4`, mốc 917 test / 86 tệp ở `ceb51c2`, sau 87 tệp. Kiểm 3: xóa thư mục nếu còn, `IC_VITE_CACHE_DIR=/private/tmp/codex-259-dist/.vite-cache … build --outDir /private/tmp/codex-259-dist --configLoader runner`, cùng grep (thoát 1 là đúng), rồi xóa. Cả hai ghi rõ cờ là bắt buộc và vì sao. Thêm một dòng Cấm: chạy Vitest hay Vite thiếu các cờ đó. "Làm ở đâu": gốc nhánh đổi thành `ceb51c2`, ghi rằng số đo §1 lấy ở `bc94110` vẫn đúng (giữa hai mốc `blades.ts`, `sword-material.ts` không đổi; `skills-main.ts` chỉ thêm 4 dòng `flipbookProbe`), và rằng mọi ghi vào `node_modules/` là ghi vào game |
| 2. Kiểm 4 không thể đạt như viết: `status --short` luôn in `?? node_modules`; `git -C games/.wt-…` không chạy được từ trong worktree | Đúng. `git status --short` trong worktree lúc này in đúng `?? node_modules`; `.gitignore` của game có `node_modules/`, mẫu có `/` cuối chỉ khớp thư mục, không khớp symlink; báo cáo 258 dòng 96 in cùng dòng đó. Phiếu bảo Codex chạy trong worktree, mà ở đó `games/.wt-immortality-cultivation-codex` là đường dẫn tương đối không tồn tại | Kiểm 4 chạy `git diff --stat` và `git status --short` ngay trong worktree (hoặc `git -C games/.wt-…` từ gốc repo cha). Yêu cầu theo lời của 258: chỉ các file được ghi, cộng symlink `node_modules` có sẵn; ghi lý do `?? node_modules` luôn hiện, cấm sửa `.gitignore`, nói rõ tệp mới chỉ hiện ở `status --short` và báo cáo ở repo cha không hiện ở đây |

### Lượt 4

Lượt phản biện thứ tư của một agent Claude độc lập (04/11/2026, tối): **FAIL**, hai lỗi. Claude kiểm từng lỗi trên mã của game (`sword-material.ts`, `skills-main.ts`, `aura-gates.ts`, `element-fire.ts`, `element-metal.ts`, `renderer.ts`) và three 0.170.0 trong `node_modules` (`UnrealBloomPass.js`, `LuminosityHighPassShader.js`, `WebGLProgram.js`, `ColorManagement.js`, `RenderTarget.js`, `meshphysical.glsl.js`): cả hai đúng, đã sửa. Không bác lỗi nào. Claude thêm một chỗ tự thấy khi kiểm lỗi 1 (dòng 3). Đếm lại hai lượt PASS từ đầu; lượt 5 và 6 đều phải PASS.

| Lỗi | Kiểm lại | Đã sửa |
|---|---|---|
| 1. Kiểm 8, bloom mặc định: cổng `bright.ok` cả khung có thể đánh trượt bản làm đúng, và nhánh hỏng chỉ nêu mép mềm của nắp | Đúng, cả hai cớ. (a) Nắp chỉ áp cho mảnh của kiếm; `aura-gates.ts` ghi rõ cổng "Chồng lớp" cho ≤ 2 lớp trong suốt mỗi điểm ảnh trong vùng kiếm, tức là có lớp đè lên kiếm. Phiếu cố ý làm đĩa sáng hơn: Kiểm 9 đòi L + 0,04; ánh trong 0,738 × 0,06 ≈ 0,044 tới 0,738 × 0,41 ≈ 0,30; `FIRE_BLADE.char` = 0,4 (`element-fire.ts`), mà đĩa mới thay albedo sau bước `char`. (b) `UnrealBloomPass.js` dòng 43–46: `resx = Math.round(this.resolution.x / 2)`, `renderTargetBright` HalfFloat; `EffectComposer` dựng target HalfFloat, `RenderTarget` mặc định `minFilter` `LinearFilter` và texture mặc định `magFilter` `LinearFilter`: mỗi texel sáng là trung bình 2 × 2. `bright()` của lab đọc đúng bộ đệm này và cộng độ sáng 709 của texel > 0,002 | Theo đề xuất: `bright` cả khung chỉ còn để ghi; cổng mới là `__lab.ringCap()` (§4, mã đầy đủ): riêng các lưới `"real-sword"`, đủ độ phân giải, HalfFloat, ba lần vẽ (vòng tắt, bật, trọng số), trả `changed`, `interior`, `over`, `overMax`, `soft`, `softMax`, `max`, `nonFinite`. **Chọn khác đề xuất ở ba chỗ:** (1) mép mềm tách bằng chính trọng số: `uSwRingOn` = 2 cho shader ghi (1 − w, J, G) thay cho ánh sáng (một nhánh uniform trong `if (swRingW > 0.0)`), vì đoán mép bằng láng giềng điểm ảnh không bắt được chỗ chuyển màu của nét vàng ở giữa đĩa; (2) ngưỡng 0,96 thay cho 0,95 + 1e-3, vì điểm ảnh có 1 − w ≤ 1e-4 vẫn được cộng tới khoảng 0,005, cộng sai số half-float, mà 0,96 vẫn dưới ngưỡng 1 của bloom; (3) đo bằng độ sáng Rec. 709 (dòng 3). `SWORD_LOOK.edge` về 0 trong lúc đo, vì ánh mép tan ra khỏi nắp (lỗi 2). Kiểm 8 thêm yêu cầu phép đo chạy thật ở k1z (`interior` ≥ 0,5 × `changed`). Nhánh hỏng viết lại: `ringCap.ok` sai là lỗi nắp trong mã, dừng; `bright.ok` sai mà `ringCap.ok` đúng thì ghi, định vị bằng `__lab.bright(box)`, chỉ dừng khi chỗ tăng nằm ngoài hộp vòng. `MASK=1` gọi `ringCap()` sau `bright()`; `ring-parity.mjs` ghi `ringCap` và `ringCap.ok`, tổng có số khung sai |
| 2. §2 tự mâu thuẫn: nắp ăn cả ánh mép tan, nên mép tan trên đĩa không bloom trong khi trên gờ, vành, lưỡi thì có | Đúng. `EMIT` dòng cuối `totalEmissiveRadiance += uSwEdge * swDe * 0.7;` nằm trong `outgoingLight`, mà nắp nhân cả `outgoingLight`. Metal: 0,7 × `EDGE_HOT` = (1,56; 2,22; 2,52), độ sáng 601 khoảng 2,06. `swDe` khai trong `DISSOLVE`, chèn sau `#include <clipping_planes_fragment>` ở tầm `main` (`meshphysical.glsl.js` dòng 166, trước dòng 199 của `outgoingLight`), nên dùng được trong `OUTGOING` | Chọn cách thứ nhất: ánh mép tan nằm ngoài nắp, đúng công thức đề xuất (`swRingDe`), với hệ số đổi sang 709 (dòng 3). Lý do chọn: mép tan là một đường sáng chạy qua cả thanh kiếm lúc hiện và tan; giữ nó liền mạch đúng ý "vòng tan cùng kiếm", và đúng như trước phiếu. Cách thứ hai để lại một vệt mờ ở `rCut` trên kiếm trời K5 dài 20 m. Đã sửa: khối nắp và chú thích của nó, ghi chú dưới khối, gạch "Mép tan", tóm tắt đầu "Lời giải", dòng "Lỗi 7" của bảng quyết định; test kiểm ba dòng của khối nắp theo thứ tự |
| 3. (Claude thêm) Nắp đo bằng hệ số Rec. 601, bloom đo bằng Rec. 709 | Đúng. `LuminosityHighPassShader` gọi `luminance()`; `WebGLProgram.js` (`getLuminanceFunction`) chèn hàm này với hệ số của `ColorManagement` cho không gian làm việc, `REC709_LUMINANCE_COEFFICIENTS` (0,2126; 0,7152; 0,0722). Viền k4 của Clear Wind (`#35b483`, `rimOf(…, 1,2)`) có tỉ số 709 / 601 ≈ 1,16: điểm ảnh viền ép tới 0,95 theo 601 có độ sáng 709 khoảng 1,1, qua ngưỡng 1 | Nắp đo bằng `vec3(0.2126, 0.7152, 0.0722)`, cùng hệ số `RING` đang dùng cho `swLum`. Ngọc trắng trung tính không đổi (0,727 so với 0,729). Bảng quyết định ghi lại. Luật lấp khoảng trống cũ của hạt ngọc vẫn dùng 601; ngoài phạm vi và trong danh sách cấm sửa, chỉ ghi lại để Claude cân nhắc phiếu khác |
