# Kiểm toán VFX vẽ bằng code: Kim, Lôi, Quang (ult lab)

Ngày 17/11/2026. Chỉ đọc, không sửa code. Thư mục nguồn: `games/.wt-ic-lab-all/src/lab/` (gọi tắt `src/`); kho art: `games/.wt-ic-lab-all/art-src/lab/vfx/` (gọi tắt `vfx/`).

Quy tắc (chủ game, AGENTS.md và 17/11): hình dạng nhìn thấy phải đến từ art đã duyệt (ảnh, video Firefly/Blender, flipbook, model Tripo). Code chỉ đặt, canh thời gian, nhuộm màu, làm chuyển động. Shader chỉ được là chất liệu phủ lên art (ví dụ dissolve), không được tự tạo hình (vệt, tia, ruy băng, vỏ hào quang, tia sét, vòng, vệt sáng, dấu trên đất).

## Tóm tắt

| Kỹ năng | Lớp vẽ bằng code (vi phạm rõ) | Lớp ở vùng xám (cần chủ game quyết) |
| --- | --- | --- |
| Kim (metal) | 2 | 3 |
| Lôi (thunder) | 1 (dùng ở 2 chỗ) | 2 |
| Quang (light) | 3 | 1 |
| Tổng | 6 | 6 |

Nặng nhất:
1. **Lôi: `ChainArcs`** (`thunder-ult-chain-space.ts:183-297`). Toàn bộ tia sét và nhánh là polyline ngẫu nhiên, dải ruy băng hướng camera, hình từ `exp(-x²)` trong shader. Không có art nào.
2. **Quang: `FanBeams`** (`light-ult-fan-space.ts:11-72`), 16 dải tia có hình từ sin/noise/gaussian trong shader. Đây là lớp chính của skill, và comment đầu file ghi rõ "Mesh/shader rays are explicitly requested by the ticket", tức là ticket trái quy tắc 17/11.
3. **Kim: `SwordLookLayer` chế độ aura** (`metal-sword-look.ts:23-30,51-52,75-78`), vỏ fresnel phình 0.03 theo normal quanh thanh kiếm khổng lồ, đúng dạng "fresnel shell" bị cấm.
4. **Quang: `HeldLens`** (`light-ult-fan-space.ts:74-100`) là vật thể 3D dựng bằng `TorusGeometry`, `SphereGeometry`, `CylinderGeometry`. Và **`LightWedgeSpill`** (`light-ult-ground.ts:4-31`), tam giác sáng trên đất với alpha thuần procedural.

Ghi chú phương pháp: "vùng xám" là lớp có art thật làm nguồn nhưng bị shader làm mờ, kéo giãn, lọc kênh hoặc nhân bản đến mức hình cuối do code quyết định. Quy tắc hiện tại không nói rõ ngưỡng, nên liệt kê riêng. Đèn `PointLight` (chiếu sáng thật lên cảnh, không phải hình) không tính là lớp vẽ bằng code.

## KIM (metal)

Nguồn: `metal-ult-rain.ts`, `metal-sword-look.ts`, `metal-ult-3d.ts`, `metal-ult-sprites.ts`, `metal-ult-layered.ts`, `metal-ult-tint.ts`. Chế độ mặc định là mưa kiếm (`MetalUltRain`); chế độ `?metalUlt=ring` dùng `MetalSpriteField`.

| # | Lớp | File:dòng | Nguồn hình | Phân loại | Thay thế đề xuất |
| --- | --- | --- | --- | --- | --- |
| K1 | Kiếm Tripo (thân kiếm rơi, kiếm khổng lồ) | `metal-ult-rain.ts:354` (`loadSword`), `metal-ult-3d.ts:114` | `vfx/metal-ult/models3d/tripo/ult-metal-sword.tripo.v1.glb` | ART (Tripo). Shader dissolve/grow là chất liệu. | Giữ nguyên. |
| K2 | **Vỏ aura fresnel quanh kiếm** (chế độ aura, dùng cho kiếm khổng lồ ở chế độ mặc định `mix`) | `metal-sword-look.ts:23-30` (vertex phình `normal*0.03`), `:51-52` (`pow(1-facing,2)`), tạo ở `:75-78`, gắn ở `metal-ult-rain.ts:422` | Không có art, chỉ hình học của kiếm và công thức fresnel | **CODE-DRAWN** (fresnel shell) | `vfx/aura/aura-metal-feather-mantle`, `aura-metal-windsilk` hoặc `aura-metal-featherplates` (flipbook) gắn quanh kiếm khổng lồ; thêm `vfx/metal/metal-sword-light-streak-w2` cho vệt. |
| K3 | **Lớp "energy" phủ lên kiếm nhỏ** (cột sống sáng `core`, dòng chảy `flow`, rim) | `metal-sword-look.ts:53-61` (`flow` ở `:54`) | Hình lấy từ geometry Tripo, nhưng toàn bộ phát sáng/đường sống do công thức sin và fresnel | **CODE-DRAWN** nhẹ (hình dạng vẫn là Tripo; phần sáng nhìn thấy là vẽ bằng shader). Có thể coi là "chất liệu trên art" nếu chủ game đồng ý. | Dùng `vfx/aura/tip-star-glint` cho mũi và `qi-streak-1..4.png` làm vệt khí; hoặc chỉ giữ emissive map của GLB. |
| K4 | Ấn trời (sky seal), mặc định `formation-simple-a/b/c` | `metal-ult-rain.ts:290`; atlas nạp `:331` | `vfx/metal-ult/formation-simple-a.atlas.png` (b, c cùng thư mục) | ART. Shader xoay vành ngoài (`:115-129`) và cộng halo 4 mẫu là chất liệu/chuyển động trên art. | Giữ. |
| K5 | Vệt kiếm rơi (trails, plane 2) | `metal-ult-rain.ts:293`, shader `:136-141`, crop `:79` | Cắt ô lưỡi kiếm của `vfx/metal-ult/metal-ult.atlas.png` (nạp `:335`), làm mờ 7 mẫu, kéo thành 2 dải chéo nhau | VÙNG XÁM: art thật nhưng là ảnh lưỡi kiếm bị blur và kéo giãn thành vệt. | `vfx/metal/metal-sword-light-streak-w2` (flipbook vệt sáng kiếm) thay cho crop-blur. |
| K6 | Tia sáng từ ấn (seal-rays, plane 4) | `metal-ult-rain.ts:292`, shader `:136-141`, crop `:79` | Cùng cách với K5, cùng ô lưỡi kiếm | VÙNG XÁM | `vfx/metal-ult/rays.png` (đã có trong thư mục metal-ult) thay cho crop-blur. |
| K7 | Vệt sáng đất (ground wash, plane 5) | `metal-ult-rain.ts:291`, shader `:130-135`, crop `:83` | Làm mờ tâm một flare có sẵn trong `metal-ult.atlas.png`, mask tròn `smoothstep(0.08,0.49)` | VÙNG XÁM (hình cuối do mask tròn và blur quyết định) | `vfx/metal/metal-ground-impact` hoặc `vfx/metal-ult/slash-ground.png`. |
| K8 | Tác động (impacts) | `metal-ult-rain.ts:294`; atlas `:331` | `vfx/metal/metal-impact-v2.atlas.png` | ART | Giữ. |
| K9 | Dấu đất (ground marks, plane 3) | `metal-ult-rain.ts:295`; atlas `:332` | `vfx/metal/metal-ground-mark.atlas.png` | ART | Giữ. |
| K10 | Bùng nổ cao trào (climax) | `metal-ult-rain.ts:296`; atlas `:332` | `vfx/metal/metal-big-burst-v2.atlas.png` | ART | Giữ. |
| K11 | Bụi và tia lửa tiếp xúc | `metal-ult-rain.ts:297-298`; atlas `:335` | `vfx/metal-ult/metal-ult.atlas.png` (ô gold-dust, glint) | ART | Giữ. |
| K12 | Chế độ vòng (`?metalUlt=ring`): rừng kiếm, dấu đất, mảnh vỡ, bụi/tia | `metal-ult-sprites.ts:176-179` (`Cards`), shader `:20-103`; Tripo `metal-ult-3d.ts` | `vfx/metal-ult/metal-ult.atlas.png` (`metal-ult-sprites.ts:187`) và GLB ở K1 | ART. Shader chỉ xói mòn nét sơn bằng hash (comment ghi "supplies no new artwork"). | Giữ. |
| K13 | `metal-ult-tint.ts` (nhuộm quái bị trói) | `metal-ult-tint.ts:11` | Chỉ nhuộm màu mesh quái | Không vẽ hình | Giữ. |

Đếm Kim: vi phạm rõ 2 (K2, K3; K3 có thể chuyển sang vùng xám nếu chủ game coi là chất liệu trên art); vùng xám 3 (K5, K6, K7).

## LÔI (thunder)

Nguồn: `thunder-ult-chain.ts` (hiệu ứng chính `ThunderUltChain`), `thunder-ult-chain-space.ts`, `thunder-ult-chain-card.ts`, `thunder-ult-nguloi.ts`, `thunder-ult-bolt-profile.ts`, `cloud-volume.ts`. Các file `thunder-{caster,travel,impact,aftermath}-r2.ts` dùng `FlipbookPool` với atlas có sẵn, không có shader tự vẽ hình.

| # | Lớp | File:dòng | Nguồn hình | Phân loại | Thay thế đề xuất |
| --- | --- | --- | --- | --- | --- |
| L1 | **Tia sét tự do và nhánh (`ChainArcs`)**, dùng cho "gân" trong tầng mây (`thunder-ult-chain.ts:344-354`) và hồ quang dư của quái sống sót (`:362-368`) | `thunder-ult-chain-space.ts:183-297` (tạo ở `thunder-ult-chain.ts:114`, vẽ `:402`) | Không có. Polyline ngẫu nhiên `spawn()` (`:218-251`), dải ruy băng hướng camera (`:198-214`), hình từ `exp(-x2*220)` và `exp(-x2*3.8)` (`:221-232`) | **CODE-DRAWN** (tia sét, ruy băng, nhánh) | `vfx/thunder/thunder-single-bolt-a-wg-hi` hoặc `thunder-five-lingering-arcs-wg` (đã dùng ở `thunder-ult-chain.ts:57` cho phần khác); còn có `thunder-chain-c*.png` (4 biến thể, flip x/y). Gân trong mây: đặt các thẻ thunder-chain-c nhỏ, xoay ngẫu nhiên. |
| L2 | Thân và nhánh sét giữa các quái (hop) và 7 cột sét | `thunder-ult-chain-card.ts:7-66` (thẻ hop, 24 thẻ), `thunder-ult-nguloi.ts:70-206` (cột, vết cháy, nổ) | `vfx/thunder/thunder-chain-c.png` (+ `-flip-x/-flip-y/-flip-xy`, `thunder-chain-c.json`), flipbook Ngũ Lôi (`THUNDER_FLIPBOOKS = "/art-src/lab/vfx/"`, `five-thunder.ts:20`), cột `thunder-column-{a,b,c}-i2v5` | ART. Shader chỉ đặt hai đầu vào hai điểm thế giới, cộng ánh sáng, không có hình mới (`thunder-ult-chain-card.ts:35-52`). `thunder-ult-bolt-profile.ts` chỉ là dữ liệu đo vị trí. | Giữ. |
| L3 | Thân mây bão (7 lát) | `thunder-ult-chain-space.ts:97-160` (`StormCloud.body`, kind 0, `:10-91`) | Atlas `thunder-five-cloud-ink-wg` (`thunder-ult-chain.ts:54`) | ART (độ sáng của art làm mật độ). Màu tím là hằng số trong shader (`:55`). | Giữ. |
| L4 | Ánh sáng mây chiếu xuống đất (`StormCloud.wash`, kind 1) | `thunder-ult-chain-space.ts:98-99,128-133` (shader `:57-60`), đặt `:128` | Cùng atlas mây, nhưng chỉ dùng độ sáng làm mật độ, màu tím cố định, mask rim hình chữ nhật mềm `smoothstep(0.16)` | VÙNG XÁM (hình cuối là hình chữ nhật mềm nhân mật độ mây, màu hằng) | `vfx/thunder/thunder-caster-seal` hoặc một vệt sáng dẹt từ `vfx/world/` nếu có; nếu không: "cần still mới" (vệt sáng tím trải đất). |
| L5 | Vết cháy sét trên đất (`StormScorch`, kind 2) | `thunder-ult-chain-space.ts:164-181` (shader `:61-64`) | Atlas nguồn, tách kênh `art.b - art.r` để lấy vết nứt xanh | ART (lọc kênh từ art) | Giữ. |
| L6 | Đám mây "deck" bão (`CloudVolume`) | `thunder-ult-chain.ts:120` (`CLOUD_PRESETS.thunder`, `lightningIntensity: 0`); `cloud-volume.ts` | `/art-src/lab/vfx/cloud-puffs/cloud01.png` (CC0 Unity Labs, `cloud-volume.ts:103`; cloud02-04 cũng có trong thư mục) | ART (CC0, không phải art do Firefly/Tripo tạo, cần chủ game xác nhận nguồn). **Lưu ý:** khi chưa có texture, shader rơi về blob tròn procedural (`cloud-volume.ts:77-78`, `smoothstep(0.5,0.15,length(vUv-0.5))`), và `uFlash` vẽ vầng sáng trong mây bằng khoảng cách (`:86-92`), đang tắt vì `lightningIntensity: 0` trong Lôi nhưng bật mặc định (0.85) ở các nơi khác. | Fallback và flash: VÙNG XÁM | Xóa fallback blob (báo lỗi thay vì vẽ). Flash: thay bằng thẻ `thunder-sparkle` hoặc `thunder-release` đặt trong mây. |
| L7 | Đèn spill hai `PointLight` | `thunder-ult-chain.ts:89,117` | Ánh sáng thật | Không phải hình | Giữ. |
| L8 | Giai đoạn r2: caster, travel, impact, aftermath | `thunder-caster-r2.ts`, `thunder-travel-r2.ts`, `thunder-impact-r2.ts`, `thunder-aftermath-r2.ts` | `thunder-ribbon-loop`, `thunder-sparkle`, `thunder-charge` và atlas dấu đất (`thunder-travel-r2.ts:12`); `FlipbookPool` | ART | Giữ. |

Đếm Lôi: vi phạm rõ 1 lớp (L1, dùng ở 2 chỗ); vùng xám 2 (L4, L6 phần fallback/flash).

## QUANG (light)

Nguồn: `light-ult-fan.ts` (điều phối), `light-ult-fan-space.ts`, `light-ult-ground.ts`, `light-ult-impact.ts`, `light-ult-burst.ts`, `light-ult-twinkles.ts`. Các `light-ult-*.mjs`, `light-ult-body-probe.ts` là công cụ chụp/đo, không dựng hình.

| # | Lớp | File:dòng | Nguồn hình | Phân loại | Thay thế đề xuất |
| --- | --- | --- | --- | --- | --- |
| Q1 | **13 tia sáng hình quạt (`FanBeams`, 16 dải, 2 mặt phẳng chéo)**, cả tia HDR | `light-ult-fan-space.ts:11-72` (FRAG `:11-34`, tạo `:46-52`), dùng ở `light-ult-fan.ts:102,172-190` | Không có. Hình từ `sin`, noise `flow`, `exp(-y*y)`, filament (`:16-31`) | **CODE-DRAWN** (tia, beam, vệt sáng) | `vfx/light/light-ribbon-loop`, `light-column-loop-w2`, `light-column-strike-w2` hoặc `light-pillar` (nhuộm vàng, kéo thành tia). Có thể ghép với `vfx/metal/metal-sword-light-streak-w2` nếu cần dải mảnh. Nếu không vừa: "cần still mới" (một tia sáng dẹt có đầu nhọn). |
| Q2 | **Vệt sáng tam giác trên đất (`LightWedgeSpill`)** | `light-ult-ground.ts:4-31`, tạo `light-ult-fan.ts:103` | Không có. Alpha từ `vUv`, `smoothstep`, `sin(a*38...)` (`:15-20`) | **CODE-DRAWN** (vệt sáng/dấu trên đất) | `vfx/light/light-ground-mark-side-i2v3` hoặc `light-ground-mark` (đã có, có bản mp4); hoặc `light-wave` kéo dẹt. |
| Q3 | **Thấu kính cầm tay (`HeldLens`)**: vành `TorusGeometry`, kính `SphereGeometry` trong suốt, hai cán `CylinderGeometry` | `light-ult-fan-space.ts:74-100` (tạo `:89-99`), dựng `light-ult-fan.ts:102` | Không có. 3 primitive + `MeshStandardMaterial`/`MeshPhysicalMaterial` | **CODE-DRAWN** (vật thể hiển thị là hình học thủ tục) | Model Tripo (thấu kính vàng có vành) sau khi still đạt 8.5; tạm thời `vfx/light/light-orb-loop` làm lõi sáng. Cần still mới cho thấu kính. |
| Q4 | Vệt lăng kính khi nổ (`LightImpactSparks`, 120 vệt, 14 tia ngắn) và tụ năng lượng (28 vệt) | `light-ult-impact.ts:7-77` (shader `:25-30`) | Cắt một ô sao 50 px của `light-sparkle.atlas.png` (frame 8, `:27`), kéo giãn theo hướng thành vệt dài | VÙNG XÁM (art thật nhưng kéo giãn từ ảnh nhỏ thành vệt; comment ghi "no drawn star") | `vfx/light/light-slash-arc` hoặc `light-comet` (`.mp4`/atlas) cho vệt, hoặc `vfx/aura/glint-starburst-set` cho tia ngắn. |
| Q5 | Lấp lánh sau nổ (`LightAfterglow`, 60 sao) | `light-ult-twinkles.ts:4-36` | Cùng ô sao 50 px của `light-sparkle.atlas.png` (`:19-22`) | ART (không kéo giãn, chỉ nhân bản) | Giữ. |
| Q6 | Bùng nổ lăng kính (`LightPrismBurst`) | `light-ult-burst.ts:12-62` | `vfx/light/light-prism-burst-hi.atlas.png` | ART (shader chỉ giải mã độ sáng từ alpha) | Giữ. |
| Q7 | Sạc, thả, lấp lánh, bụi, tác động | `light-ult-fan.ts:43,98-124` (`PARTS`) | `light-charge`, `light-release`, `light-sparkle`, `gold-dust-motes-loop-w2`, `light-impact`, `light-prism-burst-hi` (đều có trong `vfx/light/`) | ART | Giữ. |
| Q8 | Đèn `PointLight` chiếu nổ | `light-ult-impact.ts:9` | Ánh sáng thật | Không phải hình | Giữ. |

Đếm Quang: vi phạm rõ 3 (Q1, Q2, Q3); vùng xám 1 (Q4).

## Việc tiếp theo nên làm (gợi ý, chưa thực hiện)

1. Quang: thay Q1 trước tiên (là lớp chính của skill), rồi Q2. Ticket 439 phải sửa lại vì trích dẫn "mesh/shader rays are explicitly requested".
2. Lôi: thay `ChainArcs` (L1) bằng thẻ `thunder-chain-c` và `thunder-five-lingering-arcs-wg`, rồi bỏ fallback blob của `CloudVolume`.
3. Kim: bỏ vỏ fresnel (K2) và lớp energy (K3) khi đã có aura flipbook; xem K5-K7 như một mục chủ game quyết.
4. Chủ game cần quyết ngưỡng vùng xám: "art bị blur/kéo giãn/lọc kênh" có tính là "code vẽ hình" hay không (K5, K6, K7, L4, Q4).
