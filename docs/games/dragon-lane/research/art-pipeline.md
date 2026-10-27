# Dragon Lane: quy trình hình và kỹ thuật cho bản đồ 3D tranh vẽ (23/10/2026)

> **Dành cho:** chủ dự án, AI làm hình, AI viết mã của game mới (tên tạm `dragon-lane`).
> **Câu hỏi:** làm sao có nhiều bản đồ 3D kiểu tranh vẽ nhìn từ trên (rừng thông, sông, đá, hoa, tán tím lam, nắng dịu) trên Three.js 0.170, khi AI không được dựng model 3D bằng mã.
> **Đã đọc:** `games/space-typing/docs/td/TYPING_DEFENSE_DESIGN.md` (22.9, 23.1–23.14, 25.12); cùng game: `docs/art-requests/td/01-tripo-characters-enemies.md` (mục 5) và `03-2d-scenery-ui-vfx.md`; `docs/survival/SURVIVAL_MODE_PLAN.md` (8.1); `docs/SPACE_TYPING_DEFENSE_PLAN_V4_2026-10-21.md` (số đo); mã `src/defense/view/{terrain,painter,crowd,vfx}.ts`, `src/td/sim/lanes.ts`, `src/scene3d/space.ts`, `src/render3d/*`, `scripts/models/prepare-models.ts`, `scripts/models/blender/*.py`; tài liệu Tripo cho nhà phát triển (rig, animation).
> **Đã kiểm trên máy:** `three` 0.170.0 có `BatchedMesh` (`addGeometry`, `addInstance`, cắt theo từng vật), `LUTPass`, `GTAOPass`, `OutlinePass`, `NeutralToneMapping`, `AgXToneMapping`. Blender 5.2.2 ở `/Applications/Blender.app` (không nằm trong PATH). `toktx` chưa cài, nên texture vẫn là WebP.

## 0. Tóm tắt

1. **Bản đồ = dữ liệu bố cục + kit vùng đất + seed.** Không vẽ tay từng bản đồ. Đó là cách duy nhất để có 500+ ải.
2. **Địa hình bằng mã** (lưới cao độ từ "dấu" trong dữ liệu). **Đất bằng ô vẽ tay từ Codex**, trộn theo đường, sông, dốc, nhiễu, rồi **nướng một lần** vào một ảnh lớn lúc nạp.
3. **Sông là dải lưới dọc spline** với shader riêng (màu theo độ sâu, gợn trôi, bọt ven bờ). Không dùng `Water2`.
4. **Cây lớn, đá lớn, mốc cảnh: Tripo, không rig.** Cỏ, hoa, sỏi, phông xa: tranh 2D như TD 23.10. Cần một bài kiểm A/B cho cây trước khi nhân bản (mục 3).
5. **Vẻ tranh vẽ đến từ shader chung:** ramp 3 bậc, pháp tuyến cầu cho tán, rim nhẹ, bóng có màu, sương theo bán kính, LUT theo vùng, tone map Neutral.
6. **Quái theo cách di chuyển:** hai chân dùng rig biped và preset của Tripo (có cả đánh, trúng đòn, ngã); bốn chân và bay cần Blender làm clip đánh. Đám đông vẽ bằng **texture xương instanced**; chỉ Tướng, boss, Tướng địch dùng `SkinnedMesh`.
7. **Ngân sách High:** 300 quái, ≤ 150 draw call (dự tính dùng ~65–95), khung ≤ 8 ms. **30+ vùng đất** = 8 kit gốc × 4 biến thể; biến thể chỉ đổi tham số, không cần model mới.

## 1. Ràng buộc và hệ quả

| Ràng buộc | Hệ quả cho quy trình |
|---|---|
| AI không dựng model 3D bằng mã | Mọi vật đứng (cây lớn, đá lớn, cầu, bệ, quái, boss) đến từ Tripo. Mã chỉ làm lưới địa hình, dải sông, tấm billboard, decal, hạt, model tạm đơn giản. |
| Ảnh 2D do Codex CLI tạo ở máy, Claude điều khiển | Claude viết file prompt theo kit, chạy Codex, chạy script kiểm. Ảnh chỉ có cỡ 1024², 1536 × 1024, 1024 × 1536, nên đất phải là **ô lặp**, không phải một bức tranh lớn cho mỗi bản đồ. |
| Không đưa ảnh, âm, model vào Git | `art-src/` và đầu ra media đi qua `pnpm media:push`. Mã và kịch bản kiểm phải chạy khi chỉ có manifest (như TD 23.14). |
| 500+ ải | Bố cục sinh từ mẫu + seed, có bộ kiểm tự động. |
| Máy bàn trước | Đo trên Mac Apple Silicon 1080p. Bậc Low cho laptop yếu. |
| Chủ dự án đã chê bản phẳng, bản tạm | Mỗi kit phải qua chụp 3 góc × 4 hướng xoay và bài "nheo mắt" (TD 23.1) trước khi nhân bản. |

## 2. Địa hình

### 2.1 Lưới cao độ từ dữ liệu

- Một lưới vuông, ô 0,5 m trong vùng chơi (64 m → 129² đỉnh); vòng ngoài rộng 40 m, ô 2 m.
- Cao độ = tổng các "dấu" trong dữ liệu: đồi (hình chuông), nền cao (mép mềm), lòng sông (khắc dọc spline), mặt đường (làm phẳng, hạ 5–10 cm), bệ giữa (nâng 0,4–0,8 m), nhiễu ±0,3 m theo seed. `src/defense/view/painter.ts` đã làm việc này (đường lún, ô nổi, vách); dùng lại cách làm.
- Giữ dốc thoai thoải, bậc ≤ 3 m. Lưới cao độ làm vách dựng bị kéo giãn texture. Mép vách che bằng đá Tripo; chỗ dốc > 35° dùng ô đá chiếu ba mặt (triplanar).
- Sim không đọc lưới. Đường đi, ô xây lấy từ dữ liệu (như TD).

### 2.2 Đất: trộn rồi nướng

- Mỗi kit có 6–8 ô lặp: cỏ A, cỏ B, rêu, lối mòn, đất nện, cát ven sông, đá, lá rụng hoặc cỏ phép.
- Bản trộn tính lúc nạp từ: khoảng cách tới đường, tới sông, độ dốc, độ cao, nhiễu theo seed, mặt nạ "dưới tán" (từ vị trí cây đã rải).
- Chống lặp: lấy mẫu lệch kiểu ô lục giác (hex tiling) + nhiễu màu tần thấp 30–60 m.
- **Nướng một lần:** vẽ lớp đất, decal, bóng tĩnh, AO tiếp đất bằng camera trực giao vào một render target (High 4096², Medium 2048²) phủ vùng chơi. Mỗi khung, shader đất chỉ đọc ảnh nướng + một ô chi tiết khi zoom gần. Vết cháy, hố bẫy về sau vẽ thêm vào ảnh này.
- Vòng ngoài không nướng; trộn thô, mờ dần vào sương.

### 2.3 Ô đất và decal từ Codex

- Luật prompt ô đất: nhìn thẳng từ trên, trực giao, ánh sáng phẳng, không bóng đổ, nét cọ to, "seamless tileable", không vật đứng, không lối đi, 1024².
- `prepare-ground.mjs` (sharp, việc mới): đo lệch mép (dịch 50 %), sửa mép bằng trộn chéo khi vượt ngưỡng, kéo màu về bảng kit, xuất ảnh 2 × 2 cho chủ dự án xem.
- Decal (vết đất, cụm hoa, sỏi, lá, vũng): nhìn từ trên, nền khóa màu, viền nở màu 8 px như quy trình cảnh 2D của TD.

### 2.4 Sông, suối, thác

- Dữ liệu: spline, bề rộng mỗi điểm, hướng chảy, độ sâu. Hình: dải lưới dọc spline (u ngang 0..1, v theo chiều dài).
- Shader: màu theo khoảng cách tới giữa dòng và độ sâu (ven bờ ngọc nhạt, giữa lam sẫm); 2 lớp ảnh gợn vẽ tay trôi theo v ở hai tốc độ; bọt ven bờ và quanh đá bằng nhiễu cắt 2 bậc; lấp lánh bậc thang theo hướng nắng; alpha mềm theo u, không cần depth texture.
- Thác: tấm cong theo vách, ảnh vệt nước trôi dọc, hạt bọt ở chân. Cầu, đá kê là mốc Tripo.
- Chi phí: 1–3 draw call mỗi bản đồ.

## 3. Cây, bụi, đá: Tripo 3D hay tranh 2D

| Tiêu chí | Tripo 3D, không rig | Tranh 2D billboard (TD 23.10) |
|---|---|---|
| Giống ảnh mẫu (vật khối nhìn từ trên) | Tốt | Kém ở góc > 55°: tấm đứng bị ép ngắn, phải ngả hoặc đổi sang decal tán |
| Xoay camera tự do | Tốt | Cần quay theo trục đứng và ngả; dễ lộ tấm |
| Bóng | Bóng thật, nướng vào đất | Bóng ép từ alpha |
| Công làm | 1 ảnh + 1 lần Tripo + script Blender | 1 ảnh + script sharp |
| Chi phí chạy | 800–3.000 tam giác mỗi cây | 2 tam giác |

**Đề xuất lai:**
- **Tripo:** cây lớn (3–4 biến thể), bụi lớn, đá lớn, gốc cây, khúc gỗ, mốc cảnh, bệ giữa.
- **Tranh 2D:** cỏ, hoa, dương xỉ, nấm, sỏi (thẻ chữ thập hoặc decal), thú nền, phông xa.
- **Impostor** (`bake_impostor.py`, 16 hướng): cây ở bậc Low và vòng rừng ở rìa.
- **Kiểm A/B trước khi nhân bản:** cùng một bản đồ, thông 3D và thông 2D; chụp 3 góc × 4 hướng; chủ dự án chọn. Luật 21/10 "2D khi không cần 3D" vẫn giữ cho đồ nhỏ.

**Công thức prop Tripo:** ảnh Codex (một vật, 3/4 cao 30°, ánh sáng phẳng, tán gom 3–6 khối tròn, đáy phẳng, nền khóa màu theo TD 23.11) → Tripo Image to 3D, không rig, face limit 10.000 → Blender `--kind props` (việc mới: chuẩn cỡ, gốc ở đáy, giảm còn 800–3.000 tam giác, LOD 40 %, nướng 1024², tách mặt nạ tán vào kênh phụ, ảnh xem trước) → đóng gói như `prepare-models.ts` (meshopt, WebP). Lúc chạy, mọi prop của kit chung một vật liệu, texture xếp thành mảng (`DataArrayTexture`, không loang mép), vẽ bằng **một `BatchedMesh`**.

**Shader prop:** pháp tuyến tán = trộn pháp tuyến lưới với hướng từ tâm tán (lấy từ hộp bao), nên tán sáng như một khối; gió lắc theo (y/cao)², pha theo vị trí; tuyết theo pháp tuyến hướng lên (biến thể đông); đổi sắc tán theo mặt nạ.

**Rải:** Poisson có cụm theo seed. Vùng cấm: đường + 1,5 m, sông, ô xây, bệ giữa. Cây cao che đường ở góc mặc định thì dither 35 % (TD 23.6).

## 4. Ánh sáng và hậu kỳ

| Mục | Cách làm (Three.js 0.170) | Bậc |
|---|---|---|
| Ramp | `onBeforeCompile` trên vật liệu chuẩn: lượng tử N·L bằng ảnh ramp 3 bậc mềm; dùng chung cho prop, billboard, quái | Mọi bậc |
| Môi trường | `HemisphereLight` (trời lam nhạt, đất nâu ấm) + một nắng `DirectionalLight` | Mọi bậc |
| Rim | Fresnel 10–15 % màu nắng; quái mạnh hơn 5 % để nổi trên đất | Mọi bậc |
| Bóng tĩnh | Render độ sâu từ phía nắng một lần, nướng vào ảnh đất; màu bóng theo kit | Medium+ |
| Bóng động | Shadow map PCF mềm, chỉ Tướng, boss, Tướng địch, nhà; khung bóng ôm vùng chơi | High 2048², Ultra 4096² |
| Bóng quái thường | Đốm mềm instanced (đã có trong `crowd.ts`); quái bay đốm nhỏ và nhạt dần theo độ cao | Mọi bậc |
| AO | Đốm tối tiếp đất nướng vào đất; `GTAOPass` chỉ khi đo đạt | Ultra |
| Sương | Chunk riêng: trộn theo bán kính từ tâm (vùng chơi rõ, rìa chìm) + chút theo độ cao | Mọi bậc |
| Tone map | `NeutralToneMapping` giữ sắc tranh (`space.ts` đang dùng ACES, làm nhạt màu vẽ) | Mọi bậc |
| Chỉnh màu | `LUTPass`, LUT theo kit và giờ, sinh từ tham số (bão hòa, lift/gamma/gain, tông tách) | Medium+ |
| Bloom | Ngưỡng cao, chỉ phép và lửa; 0,2–0,3 như StylePack "Sách tranh" (TD 23.12) | High+ |
| Viền | Fresnel mực cho nhân vật; viền ngoài cho thứ đang chọn và boss (`OutlinePass` hoặc vỏ lật) | Mọi bậc / High+ |
| Lọc tranh Kuwahara | Pass bán kính 3–4, chỉ giữ khi ≤ 1,5 ms; chữ phải vẽ sau pass này (DOM hoặc lớp riêng) | Ultra, thử |
| Tilt-shift | Chỉ phim mở đầu và menu; trong trận làm mờ quái ở mép | — |

- **Màu dành riêng** của TD 23.3 (đỏ nguy hiểm, cam khẩn, vàng tiền, xanh ngọc sức gõ) cấm dùng cho lá, hoa, nước gần đường. Biến thể mùa thu giữ lá đỏ cam xa đường hoặc giảm bão hòa.
- **Bậc nổi** như TD 23.1: chữ → quái, Tướng → nhà, bẫy → cảnh (giảm tương phản 10–15 %) → đất → đường sáng hơn đất một bậc.

## 5. Bản đồ là dữ liệu

```jsonc
{ "id": "c03-s12", "kit": "pine-river", "variant": "autumn", "seed": 4127, "arenaR": 30, "worldR": 70,
  "center": { "r": 6, "h": 0.6, "prop": "shrine-pine" },
  "paths": [{ "id": "N", "knots": [[0, -30], [6, -18], [-2, -8], [0, -4]] }], "air": [{ "from": [28, -24], "arc": 6 }],
  "rivers": [{ "knots": [[-40, 10], [0, 14], [40, 6]], "width": [3, 4, 3], "bridges": [[0, 14]] }],
  "stamps": [{ "type": "hill", "at": [18, 18], "r": 8, "h": 2.5 }],
  "slots": [{ "kind": "trap", "path": "N", "t": 0.55 }, { "kind": "house", "at": [8, -6] }, { "kind": "block", "path": "N", "t": 0.8 }],
  "landmarks": [{ "prop": "old-bridge", "at": [0, 14], "yaw": 90 }],
  "scatter": "pine-river/default", "light": "morning", "camera": { "pitch": 55, "yaw": 0 } }
```

- Đường dùng lại cách làm của `groundLanes` (`src/td/sim/lanes.ts`): Catmull-Rom, tách và nhập mịn. Game mới chép, không import Space Typing.
- ~16 mẫu bố cục: 1 đường (thẳng, chữ S, xoắn nửa vòng); 2 (đối nhau, chữ L, một cổng tách hai); 3 (chữ T, chữ Y, quạt); 4 (chữ thập, chữ X, chong chóng, hai cặp nhập). Mỗi mẫu rung điểm theo seed trong hành lang cho phép; 16 mẫu × 32 vùng đất × seed đủ cho 500+ ải không trùng hình.
- `validate-map` (việc mới): đường dài 24–40 m; hai đường cách ≥ 8 m trừ chỗ nhập; ô bẫy nằm trên đường; ô nhà cách đường 2–6 m; cổng trong khung camera mặc định; mốc lớn không che đường; khóa mã băm bố cục khi bot đạt (TD 22.9).
- Ảnh khung nhìn từ trên (như chế độ `guide` của `painter.ts`) cho chủ dự án duyệt. Trang sửa bản đồ cho dev (kéo điểm, đặt ô) dùng chính renderer; Admin làm sau.

## 6. Camera

| Mục | Đề xuất | Lý do |
|---|---|---|
| Kiểu | Phối cảnh, FOV dọc 30° | Như sa bàn; quái gần xa cỡ gần bằng nhau |
| Góc mặc định | 55° | Thấy dáng nhân vật và đường; trùng TD |
| Khoảng cách | Tính lúc nạp cho vừa vùng chơi (bán kính 28–32 m → ~85–95 m) | Đường tới từ 4 phía; không phải kéo khi đang gõ |
| Zoom | 0,6–1,3 lần mặc định | Xa hơn thì quái quá nhỏ |
| Nghiêng | 40–75°, bằng chuột | Ảnh mẫu gần top-down |
| Xoay | Tự do bằng chuột phải, có nút "về hướng chuẩn"; không dùng phím | Phím dành cho gõ; ý chủ dự án 21/10 |
| Kéo | Trong vùng chơi + 10 m | Không lộ rìa thế giới |
| Tự chạy | Không bao giờ giữa đợt; boss ra mắt dùng khung nhỏ (TD 23.6) | Giữ nhịp gõ |

- **Cỡ trên màn hình:** ở 90 m, quái cao 2 m chỉ còn ~20 px. Phóng nhân vật 1,3–1,5 lần so với cảnh (kiểu chibi) hoặc thu vùng chơi. Đích ở 1080p: quái thường ≥ 26 px, Tướng địch ≥ 40 px, boss ≥ 120 px.
- **Rìa thế giới:** lưới đất kéo thêm 40 m, rừng rìa dày (impostor), sương bán kính, vignette nhẹ.

## 7. Quái theo cách di chuyển

| | Bay | Hai chân | Bốn chân |
|---|---|---|---|
| Ảnh gửi Tripo (TD 23.11) | Nhìn từ trước, cánh dang vừa | Trước, tư thế A | Ngang 90° |
| Rig Tripo | Avian (bản v2.5) hoặc không rig | Biped (bản v1.0) | Quadruped (bản v2.5) |
| Clip Tripo | Bộ 16 preset chung | 90+ preset: idle, walk, run, slash, shoot, hurt, fall… | Bộ 16 preset chung |
| Blender làm thêm | `make_flight_clips` có sẵn: đập cánh, lao, trúng, rơi | Đổi tên sang `Enemy_*`, khóa gốc, cắt vòng, thêm Skill | Cắn, vồ, húc, trúng, ngã theo vai xương (việc mới) |
| Đám đông | Rung cánh trong vertex shader (như `crowd.ts`) hoặc texture xương | Texture xương | Texture xương |
| Đọc độ cao | Bay 3–6 m, đường bay riêng, đốm bóng nhỏ dần | — | — |
| Trúng đòn (thuộc tính instanced) | Lóe, giật lùi, chao cánh | Lóe, giật lùi, ngửa | Lóe, chùn, trượt chân |

- 112 model quái có sẵn chỉ có Idle, chủ đề không gian; may ra họ `nature`, `frost`, `shadow` hợp với rừng. Phần lớn quái cần đợt Tripo mới.
- Rắn, thủy quái từ sông: rig serpentine hoặc aquatic của Tripo. Tướng địch, boss: `SkinnedMesh` thật, clip theo bảng TD 23.9.
- **Tướng phe ta:** `heroes/draconis-v2`, `-v3` đủ clip chiến khi bay. `guides/draconis-v4` (31.226 tam giác) chỉ có `Guide_*`: Blender phải thêm Attack, Cast, Hit, Death, Victory (mở rộng `make_guide_clips`).
- Tripo tính phí theo lượt (API: rig 25 credit, mỗi clip 10). Kiểm bảng giá gói web chủ dự án đang dùng.

### 7.1 Hoạt ảnh cho đám đông

| Cách | Cách làm | Bộ nhớ (2.500 đỉnh, 120 khung) | Ưu | Nhược |
|---|---|---|---|---|
| `SkinnedMesh` | Mỗi con một draw call, CPU tính xương | — | Không viết shader | Chỉ 8–16 con |
| **Texture xương (đề xuất)** | Nướng ma trận xương mỗi khung vào texture; `InstancedMesh` đọc 4 xương mỗi đỉnh | ~40 xương × 120 × 4 texel ≈ 0,3 MB | Đọc thẳng GLB Tripo; trộn 2 clip; nhỏ | Shader tự viết |
| VAT | Nướng vị trí và pháp tuyến từng đỉnh | ~4,8 MB mỗi loại | Shader đơn giản; biến dạng tùy ý | Nặng bộ nhớ; không trộn clip |

- Mỗi con: thuộc tính `aClip, aTime, aSpeed, aBlend` + `aState` (lóe, băng, bùa) như `crowd.ts`. CPU chỉ ghi vài số mỗi khung.
- Bản đám đông giảm còn 1.500–3.000 tam giác (meshopt simplify đã có trong `prepare-models.ts`).
- Đo trên `defense-bench.html` (đã có sprite, instanced, lod, impostor): thêm chế độ `bones` và `vat`, 300 quái. TD 23.9 định `bake_vat.py`; kết quả đo quyết định cách nào là chính.

## 8. Ngân sách hiệu năng (Mac Apple Silicon, 1080p)

| Mục | Low | Medium | High | Ultra |
|---|---|---|---|---|
| Quái hiện cùng lúc | 100 | 200 | 300 | 450 |
| `SkinnedMesh` thật | 4 | 8 | 12 | 16 |
| Prop Tripo lớn | 400 | 800 | 1.200 | 1.800 |
| Thẻ cỏ, hoa | 0 (vẽ vào đất) | 2.000 | 5.000 | 10.000 |
| Tam giác (gồm bóng) | 0,5 M | 1 M | 2 M | 3 M |
| Ảnh đất nướng | 2048² | 2048² | 4096² | 4096² |
| Shadow map | Không | Không | 2048² | 4096² |
| Draw call | ≤ 80 | ≤ 110 | ≤ 150 | ≤ 190 |
| Bộ nhớ GPU | ≤ 300 MB | ≤ 450 MB | ≤ 700 MB | ≤ 900 MB |

- Khung High: trung bình ≤ 8 ms, p95 ≤ 12 ms (như Sinh Tồn 8.1). Nạp ải cùng kit ≤ 1 s, kit mới ≤ 5 s.
- Số đã đo: Defense V4, 442 quái instanced, 3,7 ms trung bình, 108 draw call (High).
- Bậc chỉ đổi số hiện cùng lúc và độ dày hiệu ứng, không đổi độ khó; quái thừa chờ ở cổng.
- Draw call High dự tính: đất và sông 4–5; prop `BatchedMesh` và billboard 5–8; quái thường ≤ 13 (1 mỗi loại + đốm bóng); `SkinnedMesh` và bóng 16–24; nhà, bẫy, người chặn 10–20; VFX, thanh máu, vòng bùa 11–16; hậu kỳ 3–5. **Tổng ~65–95.**

## 9. 30+ vùng đất mà rẻ

| Phần của kit gốc | Số lượng | Nguồn |
|---|---|---|
| Ô đất lặp | 6–8 | Codex |
| Decal | 1–2 tấm 4 × 4 | Codex |
| Prop | 10–14 (3 cây, 2 bụi, 3 đá, gốc, khúc gỗ, 2–3 mốc) | Codex → Tripo → Blender |
| Cỏ, hoa | 1–2 tấm 4 × 4 | Codex |
| Phông xa, trời | 1–2 | Codex |
| Nước | Bảng màu + 1 ảnh gợn | Codex + tham số |
| Ánh sáng | 2–3 giờ trong ngày + LUT | Tham số |
| Hạt môi trường, âm nền, luật rải | Lá rơi, đom đóm, tuyết, tro; 1–2 vòng âm; 1 file | Có sẵn + dữ liệu |

- **Biến thể không cần model mới:** đổi sắc tán, tuyết theo pháp tuyến, LUT và giờ, đổi 2–4 ô đất, đổi 1 tấm cỏ hoa, hạt, sương.
- 8 kit gốc: rừng thông có sông (ảnh mẫu), rừng phép tím lam, rừng mưa, đồng cỏ đồi, bờ biển đá, đầm lầy, hẻm đá đỏ, núi lửa. Mỗi kit 4 biến thể theo mùa, giờ, thời tiết, trạng thái (ví dụ thông: xuân, thu, đông tuyết, đêm trăng).
- Công ước tính: kit gốc ~40 ảnh Codex, 12 lượt Tripo không rig, ~1 ngày chạy script; biến thể ~6 ảnh + tham số. 8 kit ≈ 100 prop Tripo.

## 10. Việc mới cho bộ công cụ

| Việc | Chỗ |
|---|---|
| Blender `--kind props`: gốc đáy, giảm tam giác, LOD, mặt nạ tán, nướng 1024² | `space_typing_model_tools.py` |
| Ánh xạ xương Tripo (biped, quadruped, avian) sang vai trò; `make_enemy_clips` theo 3 dạng | Như trên (`bone_roles` hiện dựa vào socket của Draconis) |
| `bake_bone_texture.py`, `bake_vat.py` (để so) | `scripts/models/blender/` |
| `prepare-ground.mjs`, `prepare-decals.mjs`, `prepare-kit.mjs`, `validate-map.mjs`, `render-map-guide.mjs`, trang sửa bản đồ dev | Script của game mới |
| Kịch bản chụp: 3 góc × 4 hướng, nheo mắt, draw call, cỡ quái theo px | `scripts/visual/scenarios/` |
| Chuyển bộ Blender và đóng gói ra chỗ dùng chung ở repo cha để 3 game mới không import Space Typing | `shared/` hoặc gói công cụ riêng |

## 11. Thứ tự làm

| Bước | Việc | Cổng qua |
|---|---|---|
| A0 Khung xám | Schema bản đồ, lưới cao độ, trộn đất với ô tạm, mẫu 1 và 4 đường, camera, sông | Chạy 300 quái hộp, ≤ 8 ms; ảnh khung đúng dữ liệu |
| A1 Một kit thật | Rừng thông có sông: 8 ô, 12 prop Tripo, 2 tấm cỏ hoa, shader sông, ramp, LUT; A/B cây | Chủ dự án duyệt ảnh 3 góc × 4 hướng |
| A2 Quái | 1 bay, 1 hai chân, 1 bốn chân qua Tripo + Blender; bench texture xương và VAT | 300 quái có hoạt ảnh trong ngân sách High |
| A3 Nhân kit | Script kit, tham số biến thể, kit gốc thứ hai | Kit thứ hai ≤ 2 ngày công |
| A4 Quy mô | 8 kit gốc, 32 biến thể, 16 mẫu bố cục | `validate-map` đạt trên mọi ải |

## 12. Rủi ro

| Rủi ro | Cách chặn |
|---|---|
| Prop Tripo lệch phong cách nhau, texture có bóng nướng sẵn, lưới rối | Ảnh nguồn ánh sáng phẳng; kéo màu về bảng kit; ramp chung; tạo lại 2–3 lần, giữ bản đẹp |
| Billboard cây trông phẳng ở góc top-down khi xoay | Bài A/B ở A1; cây lớn dùng 3D nếu chủ dự án chọn |
| Rig Tripo hỏng với dáng chibi, có cánh, có đuôi; preset biped xuyên đầu to | Rig Check trước; dự phòng rig bằng Blender (`build_winged_rig`); clip đánh tự làm |
| Shader instanced tự viết vỡ khi nâng Three.js (tên chunk đổi) | Khóa phiên bản; test ảnh; gom chunk vào một module |
| Ô đất Codex không liền mép, lệch màu giữa các đợt | Script đo và sửa mép; dòng MATCH với ảnh mẫu; bảng màu kit |
| Đất tranh rối làm chìm quái và chữ | Bài nheo mắt; đất giảm bão hòa; rim cho quái; màu dành riêng |
| Nhiều kit làm phình bộ nhớ, nạp lâu | Nạp theo chương, giải phóng kit cũ; KTX2 khi có `toktx` |
| Quái quá nhỏ khi thấy cả vùng chơi | Phóng nhân vật 1,3–1,5 lần; đo `td-scale` kiểu mới |

## 13. Câu hỏi cho chủ dự án

1. Cây lớn: 3D Tripo hay tranh 2D? Mặc định: làm A/B ở A1 rồi anh chọn.
2. Cho phép dùng gói CC0 (Quaternius, Kenney) làm hình tạm ở A0 không? Mặc định: không, dùng hộp và ô tạm.
3. Xoay camera tự do hay chỉ 4 hướng? Mặc định: tự do, có nút về hướng chuẩn.
4. Phóng nhân vật 1,3–1,5 lần so với cảnh có được không? Mặc định: có.
5. Gói Tripo hiện tại còn bao nhiêu lượt cho rig và clip? Cần để lên lịch A2 và A4.
