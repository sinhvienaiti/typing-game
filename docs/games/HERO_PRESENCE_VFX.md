# Hào quang nhân vật (presence VFX): thư viện, công thức, cách thử

Ngày 01/11/2026, tối · Áp dụng cho mọi game có nhân vật cần "tỏa sáng" khi không ra đòn: anh hùng, bạn đồng hành, rồng, tinh anh, boss · Bài học dùng lại được, rút từ nghiên cứu "cách người khác dựng hiệu ứng" và các ghi chú cùng tối · Đi cùng [CHARACTER_DESIGN_GUIDE.md](CHARACTER_DESIGN_GUIDE.md) (thiết kế, quyết định hình khối hay VFX ở §7, quy cách Last Line ở §5) và [VFX_STANDARD.md](VFX_STANDARD.md) (luật bloom, ngân sách, giảm chuyển động) · Skill: `game-hero-presence-vfx`.

**Đọc nhanh**
- Hào quang là các lớp hiện **mọi khung hình**: chi phí không bao giờ mất, lỗi nào cũng nằm trước mắt người chơi suốt trận. Dựng từng lớp riêng, có công tắc, chấm từng lớp rồi chấm cả bộ ở cỡ người chơi thấy.
- **Không cần thư viện ngoài** cho hào quang ở three.js 0.170. Kit và vài shader tự viết là đủ; thư viện ngoài chỉ để học ý (§2).
- **Chỉ lõi HDR mảnh được bloom.** Phần mềm vẽ sẵn trong shader, ≤ 0,9 mỗi kênh, để bậc không có bloom vẫn đẹp (§6).
- Mọi lớp bắt đầu từ một phần của model (socket); không có billboard trôi tự do.
- Số ms ở đây là **ước tính** để xếp thứ tự; nghiệm thu bằng số đo ở trang thử (§7).

---

## 1. Luật chung

1. **Hai loại độ sáng** (`VFX_STANDARD.md` §3.5, sửa 01/11):
   - **core:** lõi HDR 3–6, mảnh (≤ 1,5 px ở 720p, ≤ 2 px ở 1080p), vật liệu `toneMapped: false`. Chỉ loại này được bloom.
   - **glow:** ≤ 0,9 mỗi kênh trước tone map, không bao giờ bloom. Độ mềm vẽ sẵn trong shader, không trông vào bloom.
   - Bloom: ngưỡng 1, strength 0,4–0,5, radius 0,1–0,15; tone map Neutral hoặc AgX, không dùng ACES; MSAA ở High và Ultra.
   - **Một lớp hào quang không bao giờ chỉnh bloom, exposure hay tone map chung.** Hạ bloom chung từng làm mất dấu gõ chữ (`LESSONS_FROM_THREE_GAMES.md` §5).
2. **Lúc nghỉ thì dịu, ánh sáng phải kiếm được.** Riot tránh biến hình sáng gần như suốt trận, vì người chơi không biết đó là trạng thái hay chiêu đang bật [V25]. Độ sáng đi theo thứ tự: nghỉ < sẵn sàng < hành động < phản hồi đòn < thẻ chữ.
3. **Tối đa ba lớp tách khỏi thân khi nghỉ** ở cỡ chơi 70–100 px (ví dụ vũng sáng, hào quang, đốm). Lớp nằm trên bề mặt model (viền P1, kênh sáng P2, lõi P9) không tính, vì chúng không thêm hình mới vào bóng; nhưng chúng vẫn dịu khi nghỉ. Vệt, tia, quầng thân chỉ đến cùng hành động [V26].
4. **Luật cầu nối:** mỗi lớp neo vào một socket trên model (`FX_HALO`, `FX_CORE`, `FX_BACK_CORE`, `FX_RING`…). Thiếu socket thì xin thêm socket, không đoán độ lệch.
5. **Chấm ở cỡ thật** từ camera chơi. Lớp chỉ đẹp ở cận cảnh thì chỉ tính cho cận cảnh.
6. **Ánh sáng không bao giờ che một model yếu.**

---

## 2. Thư viện và nguồn

Giấy phép kiểm tại nguồn theo `SHARED_SYSTEMS_BAR.md` §5. Mọi thứ thật sự dùng ghi vào `docs/games/THIRD_PARTY.md`.

| Nguồn | Giấy phép | Hợp three 0.170? | Học hay dùng được gì | Quyết định |
|---|---|---|---|---|
| three.js lõi và addon [V1] | MIT | Có | `ShaderMaterial`, `onBeforeCompile`, `InstancedMesh`, `Points`, gắn vật làm con của `Bone` [V12], `UnrealBloomPass` [V2], `Lensflare` [V15], đường rộng theo điểm ảnh (`Line2`) [V16] | **Dùng.** Nền của mọi công thức ở §4 |
| Kit của ta `shared/game-kit/three/` [V27] | của ta | Có | `ParticlePool` (hạt điểm cộng sáng), `Ribbon`, `FlameTrail`, `LightTrail`; shader fresnel `SHIELD`, `PILLAR`, `ATMOSPHERE` qua `fxMaterial`; `glowSprite` | **Dùng.** Không viết lại thứ kit đã có |
| three.quarks [V4] | MIT | Chỉ bản 0.16.0; 0.17.x đòi three ≥ 0.182 | Mô hình emitter và behaviour, trail, hạt lưới, soft particle, preset JSON; trình sửa quarks.art trả phí | **Không dùng bây giờ** (`VFX_STANDARD.md` §4.3). Học mô hình dữ liệu |
| three-nebula [V5] | MIT | Peer `>=0.122 <1.0`, thử trên 0.185.1, chưa thử trên 0.170 | `RingZone`, `DiscZone`, `Vortex` (bản 13.3.0) cho đốm bay vòng | **Không dùng.** Mô phỏng CPU không hơn kho hạt của ta; học ý quỹ đạo |
| pmndrs postprocessing [V6] | Zlib | Có (6.39.5: three ≥ 0.168 < 0.187) | `SelectiveBloomEffect`, bloom mipmap, gộp nhiều hiệu ứng vào ít lượt vẽ | **Ứng viên** chỉ khi bloom của game tốn quá; đo trước |
| drei [V7] | MIT | Gắn với React Three Fiber | `Sparkles` (đốm instanced), `Trail`, `Billboard`, `Outlines` | **Học ý, viết lại** bằng three thuần |
| `@pmndrs/vanilla` (drei-vanilla) [V8] | MIT | Có: bản 1.25.0, peer three `>=0.137`; kéo theo `meshline`, `glsl-noise` | Bản three thuần của một số helper drei | Kiểm danh sách export trước khi dựa vào; học ý, không cài chỉ để lấy một shader |
| three-custom-shader-material (CSM) [V28] | MIT | Có: bản 6.4.0, peer three `>=0.159`; React và R3F là peer tùy chọn; đường `three-custom-shader-material/vanilla` | Mở rộng vật liệu có sẵn (`MeshStandardMaterial`, `MeshPhysicalMaterial`) bằng biến như `csm_Emissive` thay vì thay chuỗi `#include` | **Ứng viên** khi có từ ba lớp vá vật liệu trở lên (viền, kênh sáng, dải chạy) và `onBeforeCompile` thành khó giữ. Một lớp thì vá tay như §4.4 |
| The Library of Shaders [V9] | CC0-1.0 (repo `the-library-of-shaders.github.io`, đã kiểm 01/11) | — | Shader mẫu | Dùng được; vẫn ghi vào `THIRD_PARTY.md` khi chép |
| Shadertoy [V10] | Mặc định CC BY-NC-SA 3.0 | — | Vòng SDF, quầng, nhiễu | **Chỉ học**, trừ khi đầu file ghi giấy phép thoáng |
| The Book of Shaders [V11] | "All rights reserved", chỉ cho mục đích học (file LICENSE, đã kiểm 01/11) | — | Hình, nhiễu, easing | **Chỉ học**, viết lại; không chép mã vào game |
| TSL, `BloomNode` [V20] | MIT | Không: cần `WebGPURenderer` | Bloom chọn lọc qua MRT phát sáng | **Không dùng** khi game còn ở WebGL2 (`VFX_STANDARD.md` §4.1) |
| Unity VFX Graph samples, Unreal socket, bộ hào quang avatar trên Booth [V21–V23] | VFX Graph samples: Unity Companion License (chỉ cho dự án chạy Unity); bộ Booth: giấy phép VN3, trả phí | — | Cách chia lớp, neo vào xương đầu (bộ Booth đặt `Halo_Base` ngay dưới xương Head), nhịp thời gian | **Chỉ học** |
| Bài chia sẻ của studio [V24–V26] | — | — | League: 95 % hiệu ứng là hạt lưới chạy shader; Destiny 2: shader lưới cho hiệu ứng tồn tại lâu; Riot về độ rõ; Rocksteady về quá tải | Ý và luật kinh nghiệm, có trích dẫn |

---

## 3. Chọn gì cho từng lớp

Tên lớp P1–P10 theo skill `game-hero-presence-vfx` (`references/layers.md`).

| Lớp | Chọn | Vì sao | Không dùng |
|---|---|---|---|
| P3 Vòng hào quang | Vòng **SDF trên một ô phẳng**, khử răng cưa bằng `fwidth`, có độ rộng điểm ảnh tối thiểu (§4.1). Hai lưới chung hình học: thân glow và lõi core | Giữ nét 1–3 px không nhấp nháy [V18]; xoay theo camera nên luôn gần tròn ở góc chơi 46°; đổi trong vài phút | Vòng xuyến hình khối mảnh (dưới 1 px thì nhấp nháy); vòng vẽ vào ảnh nguồn (rơi vào albedo); billboard trôi tự do (trông như dán) |
| P4 Đốm sáng | **Một `Points`** (hay `InstancedMesh`) cho mỗi nhân vật, quỹ đạo tính trong vertex shader từ `uTime` và ma trận socket; cỡ điểm ảnh tối thiểu (§4.2) | Một draw call, CPU không làm gì theo từng đốm | Thư viện hạt CPU; đốm cùng cỡ cùng vòng đều tăm tắp |
| P5 Dải sáng, vệt | **`Ribbon`, `LightTrail` của kit** trên socket; khi đứng yên thì lái theo đường trôi thủ tục (§4.3) | Có sẵn, đã chạy ở hai game | Lõi trắng mặc định của dải (`VFX_STANDARD.md` §3.5); vải và khăn trên xương (đó là animation nhân vật) |
| P1 Viền fresnel | **Vá `MeshStandardMaterial` của chính model** bằng `onBeforeCompile` (§4.4) | Giữ normal, roughness map (`MODEL_QUALITY.md`); chỉ tốn ở điểm ảnh của nhân vật | Thay bằng vật liệu không chiếu sáng (model thành phẳng); lớp vỏ phồng to (gấp đôi skinning và vẽ chồng) |
| P2 Kênh phát sáng | **`emissiveMap` từ mặt nạ** tách sau Tripo, cộng một dải sáng chạy theo `uTime` (§4.5) | Ánh sáng theo đường thật trông như được thiết kế [V24] | Vẽ ánh sáng vào ảnh nguồn |
| P6 Nhịp sáng, quầng thân | **Vỏ fresnel** (`fxMaterial` với `PILLAR` hay `SHIELD` của kit) độ đục thấp, hay cung trên của mandorla bằng SDF; chỉ theo sự kiện (§4.6) | Rẻ, có sẵn | Quầng sáng suốt trận |
| P7 Vũng sáng dưới chân | **Ô decal** gradient tròn mềm, `polygonOffset` (§4.7) | Tách nhân vật khỏi sàn từ trên nhìn xuống, thay đèn ở bậc thấp | Viền vòng cứng (đọc thành dấu chọn hay cảnh báo vùng); màu đỏ |
| P8 Đèn nhân vật | Một đèn trong kho dựng sẵn, chỉ khi đo cho phép | Đèn tốn ở mọi điểm ảnh được chiếu gần đó, cả đám đông | Thêm, bớt đèn lúc chạy (biên dịch lại shader) |
| P9 Lõi, mắt, huy hiệu | Chấm HDR nhỏ trên nền tối của model | Điểm nhìn rõ, rẻ nhất | Lõi sáng hơn dấu chữ bay vào |
| P10 Méo không khí, tia sáng màn | Gần như không dùng cho hào quang | Lượt toàn màn đắt | — |
| Bloom chọn lọc | **Bloom theo ngưỡng 1 với lõi HDR** (một lần vẽ cảnh) | Đủ để chỉ lõi bloom | Ví dụ selective bloom của three.js (vẽ cảnh hai lần, hai composer, đổi vật liệu sang đen) [V3]; `SelectiveBloomEffect` khi chưa đo (thêm một lượt depth) |

---

## 4. Công thức

Mã dưới đây là của ta, viết từ ý của các nguồn đã kiểm; không chép mã có giấy phép hạn chế. Đây là bản khởi đầu: chưa chạy trong game nào; phải thử ở trang thử (§7) trước khi dùng.

### 4.1 Vòng hào quang SDF

**Hình:** một `PlaneGeometry(1, 1)` vuông, uv trải −1..1, vẽ vòng theo khoảng cách tới bán kính.

```glsl
// fragment, ô phẳng; vUv trong -1..1
uniform float uRadius;    // bán kính vòng, đơn vị uv (ví dụ 0,8)
uniform float uWidthPx;   // nửa bề rộng nét, điểm ảnh CSS × tỉ lệ điểm ảnh (lõi: 0,5–1 CSS; thân glow: 1,25–1,75 CSS)
uniform vec3  uColor;     // lõi: HDR 3–6; thân: ≤ 0,9
uniform float uArcs;      // số cung (3–4), 0 = vòng liền
uniform float uGap;       // độ rộng khe, phần của một cung (0,05–0,1)
uniform float uPhase;     // pha quay 0..1, CPU tính: (uPhase + uSpin * dt) % 1; uSpin ≤ 1/8 vòng/giây khi nghỉ
varying vec2 vUv;
void main() {
  float r = length(vUv);
  float px = max(fwidth(r), 1e-5);              // một điểm ảnh của bộ đệm khung, tính bằng đơn vị uv
  float d = abs(r - uRadius) / px;              // khoảng cách tới đường vòng, tính bằng điểm ảnh
  float w = max(uWidthPx, 0.5);                 // không mảnh hơn một điểm ảnh...
  float fade = uWidthPx / w;                    // ...mà mờ đi thay vì mảnh đi (kỹ thuật "dây điện thoại")
  float line = (1.0 - smoothstep(w - 0.5, w + 0.5, d)) * fade;
  float a = fract(atan(vUv.y, vUv.x) / 6.2831853 + uPhase);
  float seg = uArcs > 0.0 ? fract(a * uArcs) : 0.5;
  float arc = smoothstep(0.0, uGap, seg) * smoothstep(1.0, 1.0 - uGap, seg);
  gl_FragColor = vec4(uColor * line * arc, 1.0); // trộn cộng sáng
  #include <tonemapping_fragment>
  #include <colorspace_fragment>
}
```

**Ba chỗ dễ sai trong shader này:**
- **Hai dòng `#include` cuối là bắt buộc.** `ShaderMaterial` không tự tone map hay đổi sang sRGB. Thiếu chúng thì ở bậc vẽ thẳng ra màn (Last Line: Low, Medium) vòng ra sai màu và sai độ sáng so với High, Ultra. Shader nền của Last Line đã làm vậy (`scene.ts`, bốn shader có cả hai dòng).
- **Điểm ảnh của shader là điểm ảnh bộ đệm khung,** không phải điểm ảnh CSS. Số px trong guide là CSS ở 720p, 1080p; đặt `uWidthPx = widthCssPx * renderer.getPixelRatio()` (Last Line: 1 ở Low, Medium; 1,5 ở High; 2 ở Ultra). Đọc lại khi đổi bậc.
- **Không đưa `uTime` thô vào `fract`:** sau vài chục phút số thực mất độ chính xác và cung giật. CPU giữ `uPhase` trong 0..1.

**Hai lưới chung hình học:**
- **Thân glow:** nửa rộng 1,25 / 1,75 px CSS ở 720p / 1080p (nét 2,5 / 3,5 px, guide §5.1), màu ≤ 0,9, `toneMapped: true`.
- **Lõi core:** nửa rộng 0,5–0,75 / 0,75–1 px CSS (nét ≤ 1,5 / 2 px, đúng luật core), HDR 3–6, `toneMapped: false`.
- Cả hai: `transparent: true`, `blending: AdditiveBlending`, `depthTest: true`, `depthWrite: false`, vẽ sau thân (`renderOrder`).
- Ở bậc không có bloom, thân glow rộng thêm 1 px để bù.

**Hướng:** tâm theo socket `FX_HALO`, pháp tuyến quay về camera nhưng chỉ xoay quanh trục đứng của thân, cộng một góc nghiêng cố định. Như vậy vòng không lật ngang khi nhân vật xoay thân, và vẫn gần tròn ở camera chơi (Last Line: nghiêng khoảng 45°, vì vòng đứng chỉ còn cos 46° ≈ 0,69). Ở menu hay chân dung dùng cùng hàm với camera đó.

```ts
// mỗi khung; mọi vector dùng lại, không cấp phát
socket.getWorldPosition(p);
d.subVectors(camera.position, p);
const yaw = Math.atan2(d.x, d.z);
const pitch = Math.atan2(d.y, Math.hypot(d.x, d.z)) * tiltShare; // tiltShare 1: nhìn thẳng camera
halo.position.lerp(p, 1 - Math.exp(-dt / tau)); // trễ theo thời gian, không theo khung; tau 0,06–0,1 s
halo.rotation.set(-pitch, yaw, 0, "YXZ");
```

`lerp` với hệ số cố định mỗi khung cho độ trễ đổi theo FPS (60 Hz và 144 Hz trông khác nhau); hệ số `1 - exp(-dt / tau)` giữ cùng độ trễ ở mọi tốc độ khung. Ở chế độ giảm chuyển động, `tau` về 0 (bám cứng).

**Tia (vương miện tia):** cùng shader, thêm mặt nạ góc cho 5–7 tia rộng đầu bo tròn; tia là thân glow, chỉ đường giữa mỗi tia là lõi. Ít tia rộng đọc tốt hơn nhiều tia mảnh.

### 4.2 Đốm sáng bay vòng

- **Một `Points` cho mỗi nhân vật,** thuộc tính riêng từng đốm: bán kính, pha, tốc độ (vòng/s), góc nghiêng dải, cỡ, hạt giống.
- **Vertex shader** tính vị trí trên quỹ đạo từ `uTime` rồi nhân ma trận socket (uniform `uAnchor`). CPU chỉ cập nhật một ma trận mỗi khung. `uTime` quấn theo một chu kỳ chung (ví dụ bội chung của các tốc độ, hay 600 s với tốc độ làm tròn theo chu kỳ đó) để số thực không mất độ chính xác sau một trận dài.
- **Cỡ tối thiểu:** `gl_PointSize = max(uMinPx, sizeWorld * uScale / -mvPosition.z)`. Khi phải phóng lên cỡ tối thiểu thì giảm alpha theo tỉ lệ, để đốm ở xa không thành chấm nhấp nháy.
- **Đơn vị:** `gl_PointSize` tính bằng điểm ảnh bộ đệm khung. `uScale = drawingBufferHeight / (2 * tan(fov / 2))` và `uMinPx = minCssPx * renderer.getPixelRatio()`; cập nhật khi đổi cỡ cửa sổ hay bậc. Cỡ điểm có trần của GPU (`ALIASED_POINT_SIZE_RANGE`), nên đốm lớn hơn khoảng 60 px thì dùng `InstancedMesh` ô vuông.
- **Màu:** fragment shader của đốm cũng kết thúc bằng `#include <tonemapping_fragment>` và `#include <colorspace_fragment>` như §4.1.
- **Đa dạng:** 2–3 dải nghiêng khác nhau, bán kính và tốc độ lệch ±20 %, vài đốm lớn và nhiều đốm nhỏ. Nhấp nháy theo nhiễu với tỉ lệ bật ≤ 15 %. Vòng đều tăm tắp trông rẻ.
- **Độ sâu:** `depthTest: true` để đốm đi ra sau thân. Trộn cộng sáng, loại glow; chỉ 2–3 đốm lớn nhất có tâm HDR 3 cỡ 1 px, và chỉ khi không nghỉ (khi nghỉ mỗi nhân vật chỉ một lõi HDR, §6).
- **Hạt giống cố định** để chụp lại lần nào cũng giống nhau.
- **Tốc độ khi nghỉ:** 0,15–0,3 vòng/s. Nhanh hơn thì đọc thành côn trùng.

### 4.3 Dải sáng và vệt

- **Dùng `Ribbon` hay `LightTrail` của kit** trên socket (đầu khăn, viền áo, đầu cánh, gót, động cơ drone). `Hero` của kit đã tự tìm socket vệt.
- **Vệt theo chuyển động chết khi đứng yên.** Dải sáng khi nghỉ (như khăn bay của H3) lái theo một đường thủ tục quanh socket: sin chậm cộng nhiễu, chu kỳ 3–5 s, để dải vẫn lượn.
- **Dạng:** thon đuôi, cuộn UV, ăn mòn mép bằng nhiễu [V19]. Lõi giữa HDR 3 mảnh (≤ 1,5 px ở 720p) khi chuyển động hay hành động; dải lượn khi nghỉ giữ lõi ≤ 0,9. Thân glow. Rộng ≥ 3 px ở 720p.
- **Vệt khi di chuyển** tắt trong 0,3–0,5 s.
- Áo choàng, khăn và tóc trên xương là animation nhân vật (mức 9), không phải lớp này. Dải sáng chỉ nối dài phần vải ra ngoài mép.

### 4.4 Viền fresnel trên vật liệu của model

Ý từ thảo luận three.js về fresnel [V13]; mã dưới là của ta.

```ts
material.onBeforeCompile = (shader) => {
  shader.uniforms.uRim = rim;           // { value: 0.3 }, glow: ≤ 0,9
  shader.uniforms.uRimColor = rimColor; // { value: new THREE.Color(...) }
  shader.uniforms.uRimPow = rimPow;     // { value: 3.5 }
  shader.fragmentShader = shader.fragmentShader
    .replace("#include <common>", "#include <common>\nuniform float uRim; uniform float uRimPow; uniform vec3 uRimColor;")
    .replace("#include <emissivemap_fragment>", `#include <emissivemap_fragment>
      float rimF = pow(max(1.0 - dot(normal, normalize(vViewPosition)), 0.0), uRimPow);
      totalEmissiveRadiance += uRimColor * (uRim * rimF);`);
};
material.customProgramCacheKey = () => "presence-rim-v1";
```

- **Kẹp trước khi lũy thừa** (`max(…, 0.0)`): gọi `pow()` với số âm cho NaN, MSAA và bloom loang NaN thành chấm hay khối đen. Last Line đã gặp lỗi này ở shader dải và cột Heat Beam.
- **Mặt nạ:**
  - thân trên 1×, chân 0,3×, để giữ "chân tối, thân trên sáng" (guide §2.4, mục 3);
  - không phủ da mặt;
  - truyền chiều cao qua một varying riêng (vá vertex shader) hay dùng một kênh của texture mặt nạ.
- **Nghiêng viền về một hướng** (ví dụ từ trên và sau) thay vì viền đều quanh thân: viền điêu khắc khối.
- **Biên dịch biến thể lúc nạp** trong file warm của game (Last Line: `src/view/warm.ts`).

### 4.5 Kênh phát sáng

- **Tách mặt nạ sau Tripo.** Ảnh nguồn vẽ kênh sáng bằng màu phẳng (ví dụ cyan nhạt). Sau Tripo, tách vùng màu đó trên texture màu thành mặt nạ trong Blender hay bằng script, rồi sửa tay. Đây là cách của ta, chưa thử.
- **Không trông Tripo xuất map phát sáng:** đó không phải đầu ra chính của nó; nếu bản xuất có map phát sáng thì xem như thưởng.
- **Dải sáng chạy:** `totalEmissiveRadiance *= uBase + uGain * band(coord - uPos)`, với `coord` là chiều cao hay tọa độ dọc kênh, và `uPos` chạy hết kênh trong 0,3 s khi xong một từ.
- **Độ rộng:** kênh mảnh hơn khoảng 1,5 px ở camera chơi thì nhấp nháy hoặc biến mất. Hoặc làm rộng ra, hoặc chấp nhận nó chỉ đọc ở cận cảnh và không tính nó khi chơi.

### 4.6 Nhịp sáng và quầng thân

- **Vỏ fresnel:** dùng `fxMaterial(PILLAR_FRAGMENT, …)` hay `SHIELD_FRAGMENT` của kit trên một khối trụ hay viên nhộng bao thân, độ đục ≤ 0,25.
- **Cung mandorla:** vòng SDF ở §4.1 với mặt nạ chỉ giữ cung trên vai.
- **Chỉ theo sự kiện:** xong từ, lên bậc chuỗi gõ, sẵn sàng, thắng. Lên nhanh (1–2 khung), xuống chậm (ease-out 150–300 ms).
- **Nhịp thở khi nghỉ:** chu kỳ 2–4 s, biên độ nhỏ.
- Quầng thân là lớp làm trắng nhân vật đầu tiên: luôn kiểm bóng hình khi nó bật.

### 4.7 Vũng sáng dưới chân

- **Ô phẳng nằm sàn,** shader gradient tròn mềm (`1 - smoothstep(0.2, 1.0, r)`), không có viền vòng.
- **Cài đặt:** `polygonOffset` −1, `depthWrite: false`, trộn cộng sáng; tâm ≤ 0,35.
- **Cỡ:** khoảng 1–1,2 lần chiều cao nhân vật; thở chu kỳ 3–4 s, ±10 %.
- Trên đất gồ thì dùng lưới ôm địa hình như cảnh báo của Dragonhold.
- **Ngôn ngữ hình phải khác** vòng cảnh báo và vòng điểm rơi của game: mềm, không có viền, không đỏ.

### 4.8 Đèn nhân vật

- Lấy một đèn từ kho dựng sẵn lúc nạp; đèn rảnh để cường độ 0.
- Số đèn nằm trong khóa biên dịch shader, nên thêm hay bớt đèn lúc chạy làm biên dịch lại.
- Một đèn tốn ở mọi điểm ảnh được chiếu gần đó, cả đám đông (`VFX_STANDARD.md` §3.7). Chỉ dùng khi đo cho phép.

### 4.9 Hạt mềm

- So độ sâu của sprite với texture độ sâu của cảnh để sprite mờ dần chỗ chạm sàn [V17]. Không có thì quầng và sương trông như dán lên.
- Cần render target có `depthTexture`; chỉ đáng làm cho sương hay quầng sát sàn, ở Ultra.
- Đốm bay trên không thì không cần.

---

## 5. Chi phí

**Cách đọc:**
- "Ước tính" tính từ số draw call và số điểm ảnh trên màn; chưa đo. Dùng để xếp thứ tự, không để nghiệm thu.
- **Trần khởi đầu:** một lớp ≤ 0,25 ms; cả hào quang của một nhân vật ≤ 0,75 ms và ≤ 25 % khoảng trống VFX đo được của game, ở bậc mặc định 1080p.

| Lớp, cách làm | Draw call | Ước tính | Chi phí tăng theo |
|---|---|---|---|
| Vòng SDF (thân và lõi) | 2 | < 0,05 ms | Diện tích ô trên màn (khoảng 30×30 px ở cỡ chơi) |
| Đốm `Points`, 8–20 đốm | 1 | < 0,03 ms | Cỡ đốm × số đốm (vẽ chồng) |
| Dải sáng kit, 2 dải | 2 | 0,02–0,06 ms, phần lớn là CPU cập nhật điểm | Số điểm và chiều dài dải |
| Viền fresnel (vá vật liệu) | 0 | Gần 0 khi chạy | Số điểm ảnh của nhân vật; một biến thể shader biên dịch lúc nạp |
| Kênh phát sáng có dải chạy | 0 | Gần 0 | Như trên |
| Vỏ fresnel, cung mandorla | 1 | < 0,05 ms | Diện tích vỏ trên màn |
| Vũng sáng decal | 1 | < 0,03 ms | Diện tích decal |
| Đèn điểm | 0 | Có thể tới cỡ ms khi nhiều điểm ảnh được chiếu | Mọi điểm ảnh được chiếu gần đèn, cả đám đông |
| Bloom theo ngưỡng (đã có) | vài lượt toàn màn | **Đo được:** +2,2 ms ở Dragonhold trên sân trống (`VFX_STANDARD.md` §3.7) | Độ phân giải, số mip |
| Selective bloom kiểu ví dụ three.js | vẽ lại cả cảnh | Gần bằng một lần vẽ cảnh nữa | Toàn bộ cảnh |
| `SelectiveBloomEffect` (pmndrs) | thêm một lượt depth của vùng chọn | Chưa đo | Số vật được chọn |

Không cấp phát bộ nhớ trong mỗi khung: kiểm bằng timeline cấp phát qua 10 s nghỉ.

---

## 6. Cách theo luật bloom

| Lớp | Giá trị trước tone map | `toneMapped` | Trộn |
|---|---|---|---|
| Lõi vòng hào quang, lõi lưng, mắt drone, tâm vài đốm lớn, lõi dải sáng | HDR 3–6, rộng ≤ 1,5 px ở 720p, ≤ 2 px ở 1080p (CSS); khi nghỉ mỗi nhân vật chỉ một lõi ở 3 (nữ xạ thủ: lõi lưng; drone: mắt) | `false` | Cộng sáng |
| Thân vòng hào quang, đốm, thân dải sáng, vỏ fresnel, vũng sáng | ≤ 0,9 | `true` | Cộng sáng |
| Viền fresnel, kênh phát sáng (ngoài dải chạy) | ≤ 0,9 sau khi cộng vào bề mặt | `true` (vật liệu của model) | Phát sáng của vật liệu |

**`toneMapped` làm gì thật trong three r170:** khi vẽ vào render target, three không tone map theo vật liệu; chỉ khi vẽ thẳng ra màn mới tone map (`WebGLPrograms.js`: `toneMapping` chỉ lấy từ renderer khi `currentRenderTarget === null` hay là target XR) [V30]. Vì vậy:
- **Bậc có composer** (Last Line High, Ultra: `RenderPass` → bloom → `OutputPass`): mọi vật liệu vẽ giá trị tuyến tính vào target float; bloom lọc theo ngưỡng trên giá trị đó; `OutputPass` tone map và đổi sRGB cho cả ảnh [V29]. Cờ `toneMapped` không đổi gì ở đây; luật bloom đứng được là nhờ **giá trị** (core > 1, glow ≤ 0,9), không nhờ cờ.
- **Bậc vẽ thẳng** (Last Line Low, Medium): cờ có tác dụng. Lõi `toneMapped: false` bị cắt ở 1 thành trắng (đúng ý: lõi trắng nóng); glow `toneMapped: true` được nén bởi Neutral. `ShaderMaterial` chỉ tone map khi shader có `#include <tonemapping_fragment>` (§4.1).
- Vẫn đặt cờ như bảng trên, để hai đường vẽ cho cùng một thứ tự sáng; nhưng khi chấm bloom, đo giá trị trước `OutputPass`.

**Ba chỗ dễ vỡ luật:**
1. **Cộng chồng:** `UnrealBloomPass` lọc theo độ sáng của ảnh cảnh đã cộng xong [V14], nên mỗi lớp ≤ 0,9 nhưng đốm đè lên thân vòng đè lên viền vẫn có thể cộng quá 1 và bloom ngoài ý muốn. Đo bằng cách vẽ riêng hào quang vào một target float rồi đọc giá trị lớn nhất ngoài các điểm ảnh lõi; giữ ≤ 0,9.
2. **Giáp sáng màu tự bloom:** giáp ngà dưới đèn chính mạnh có thể vượt 1 trước tone map và bloom cả mảng. Đo độ sáng của giáp trước tone map; sửa bằng albedo, ánh sáng hay exposure của cảnh, không dời ngưỡng bloom chung.
3. **Ngưỡng của từng game khác nhau:**
   - Dragonhold không có bloom ở High: hào quang phải đẹp mà không có bloom (lõi HDR trên nền tối, độ mềm trong shader).
   - Last Line dùng ngưỡng 1. Giá trị mới (0,45 / 0,12 / Neutral / MSAA 4, `FeelBloomPass` cho dấu gõ chữ) nằm ở nhánh `ts-wave1`; `main` tối 01/11 vẫn là ACES 0,85 / 0,3. Chỉnh hào quang theo giá trị mới, trên nhánh.

---

## 7. Trang thử và cách đo

Đầy đủ ở skill `game-hero-presence-vfx` (`references/lab-and-judging.md`); đây là phần cốt lõi.

**Trang thử:**
- Mở rộng trang xem hiệu ứng có sẵn của game (Dragonhold: `runFxShowcase` ở `src/view/bench.ts`). Game chưa có thì thêm một trang chỉ cho dev, nằm trong game.
- Dùng đúng pipeline của game: hàm dựng cảnh, camera, bảng chất lượng, composer, bloom và MSAA theo bậc. Trang tự đặt tone map hay bloom riêng là đang chấm một bức hình khác.
- Không đọc file của repo cha: bản clone riêng của game phải chạy được (`VFX_STANDARD.md` §4.5).
- **Điều khiển:**
  - công tắc và cường độ cho từng lớp;
  - nút trạng thái (nghỉ, sẵn sàng, di chuyển, bắn, trúng đòn, thắng, thua);
  - giữ đồng hồ, bước ±1 khung, tốc độ 0,25× và 1×;
  - nền sáng, nền tối, map thật;
  - camera chơi, cận cảnh, menu;
  - giảm chuyển động theo cài đặt của game.
- **Số đọc ra** dạng JSON cho kịch bản chụp: `renderer.info`, số đốm, số đèn, thời gian khung, chênh lệch theo từng lớp.

**Đo chi phí:**
- Cảnh bench nặng nhất của game, camera cố định, shader đã nóng.
- Mỗi lớp ≥ 600 khung bật và 600 khung tắt, xen kẽ từng khối; báo trung vị và p95 của chênh lệch.
- Ở bậc mặc định và Ultra, dpr 1 và 2, chạy qua `.local/bin/heavy.sh --gpu`.

**Đo trước khi chấm:**

| Kiểm | Cách | Đạt |
|---|---|---|
| Loại sáng | Vẽ riêng hào quang vào target float, đọc giá trị lớn nhất ngoài điểm ảnh lõi | ≤ 0,9 |
| Độ loe bloom | Bề ngang lõi khi bật và tắt bloom, 1080p | ≤ 1,5 lần |
| Trắng xóa | Riêng hào quang, camera chơi: điểm ảnh độ sáng ≥ 0,95 | ≤ 1 % sân |
| Vùng bảo vệ | Hào quang bật so với tắt, trong mặt nạ dải chữ, khung học, cảnh báo, HUD | Thêm ≤ 10 % độ sáng |
| Thẻ chữ | Tương phản p99 khi nghỉ và khi hành động | ≥ 7 : 1 |
| Bóng hình | Tương phản mép, hào quang bật so với tắt, nền sáng và nền tối | Bật cao hơn tắt |
| Khung đầu | Chớp lúc đổi trạng thái, ở tuổi 0 | ≥ 95 % đỉnh |
| Nhấp nháy | Độ phủ điểm ảnh của vòng giữa các khung khi đứng yên | Lệch ≤ 10 % |
| Thời gian khung | Như trên | Trong trần ở §5 và cổng khung của game |

**Gõ chữ là hệ dùng chung (mức 9).** Khi có lớp nằm gần dải chữ hay chỗ chữ bay vào (lõi, tay, lõi súng), hoặc khi đổi bloom, tone map, composer hay mã kit:
- chạy lại cảnh chụp gõ chữ của game, hào quang tắt so với bật, cùng hạt giống và đồng hồ (Last Line: `survival-feel`);
- nếu đổi mã kit hay hậu kỳ chung: chạy thêm `tools/typing-feedback-lab/scripts/capture.mjs` và `perf.mjs`.
Thay đổi thấy được ở dấu gõ là đổi hệ dùng chung: hai giám khảo từ 9 và chủ dự án ký; nếu không thì bỏ nguyên nhân.

**Chụp:**
- Từng lớp riêng, rồi cả bộ.
- 1280×720 và 1920×1080; camera chơi, cận cảnh và menu; nền sáng, nền tối, map thật; bậc mặc định, Ultra, và Low một lần.
- Mỗi trạng thái ở §5.3 của guide, cả bản giảm chuyển động. Mỗi trạng thái thêm một clip thật khoảng 3 s.
- Ảnh vào `games/<id>/tmp/presence/<ngày>/`, không vào `art-src`, `public` hay `docs`.
- Xong thì giữ tờ khung và JSON, xóa khung thô của chính mình: `node tools/capture-prune/prune.mjs <thư mục>` để xem danh sách, rồi thêm `--apply`.

**Chấm:** hai giám khảo mù từ 8,5 trên bản chơi đã build, đúng cài đặt người chơi, không tham số URL; chấm mức thị trường, sức hút và độ đọc (guide §6). Chấm từng lớp ở trang thử chỉ để lọc.

---

## 8. Bẫy

| Bẫy | Trông ra sao | Cách tránh |
|---|---|---|
| Sáng suốt trận | Không biết nhân vật đang ở trạng thái nào; đỉnh mất tác dụng | Nghỉ thì dịu; bậc sáng theo chuỗi gõ và sự kiện [V25] |
| Bloom loang | Hào quang trên 1,0 thành vệt trắng béo; bloom cũ của Last Line làm đạn rộng 2,5–3,5 lần | Thân ≤ 0,9; chỉ lõi mảnh HDR; kiểm cộng chồng (§6) |
| Đốm rẻ tiền | Mép sprite cứng cắt sàn; đốm dưới 1 px nhấp nháy; một màu cộng sáng phẳng không có lõi; quỹ đạo đều tăm tắp; đốm nhanh như bầy côn trùng | Cỡ điểm ảnh tối thiểu, lệch pha và bán kính, gradient lõi ra mép, 0,15–0,3 vòng/s |
| Vòng nhấp nháy | Vòng xuyến hình khối mảnh, texture không có mipmap | Vòng SDF có `fwidth` và độ rộng tối thiểu |
| Vòng nằm trên đầu thành dấu chọn | Vòng ngang trên đầu trong game bắn súng đọc như đơn vị được chọn | Vòng sau đầu bao lấy đầu trên màn, chia cung theo dáng mào |
| Vũng sáng thành cảnh báo | Vòng đất có viền đọc như vùng đánh [V25] | Đĩa mềm, không viền, không đỏ; trận pháp chỉ ở đỉnh chuỗi gõ |
| Dấu hiệu phản diện | Quầng đỏ hay tím, tia nhọn tối, sáng từ dưới lên, mắt đỏ | Tròn, chậm, lướt; ngà, cyan sạch, vàng chỉ khi game không dành vàng cho tín hiệu (Last Line dành vàng: không vàng bão hòa trên nàng, drone, vỏ súng) |
| Trùng màu tín hiệu | Hào quang cùng hue với tường khiên của quái hay dấu gõ chữ | So ô màu của hào quang với từng màu dành riêng của game ở cỡ chơi (guide §4.1); tách bằng hình, chỗ neo và độ sáng khi hue gần nhau |
| Cỡ sai ở Ultra | Vòng và đốm mảnh đi một nửa ở dpr 2 vì cỡ đặt theo điểm ảnh bộ đệm | Nhân cỡ với `renderer.getPixelRatio()` (§4.1, §4.2) |
| Rối | Mọi lớp bật cùng lúc; đốm trôi qua chữ | Tối đa ba lớp khi nghỉ; mặt nạ vùng bảo vệ |
| Ánh sáng vẽ vào ảnh nguồn | Sơn phẳng trên albedo, không bloom, không đổi theo trạng thái | Ánh sáng chỉ ở VFX (guide §7) |
| Che dấu gõ chữ | Lõi nghỉ sáng hơn chữ bay vào | Lõi nghỉ dịu hơn; chạy lại đo gõ chữ |
| Đổi hậu kỳ chung để nhân vật đẹp | Dấu gõ, đạn và cảnh đổi theo | Lớp hào quang theo luật bloom, không dời luật |
| Phụ thuộc thư viện khóa phiên bản | three.quarks 0.17.x kéo three lên 0.182 | Đọc peer trước khi cài; ưu tiên kit |
| Chép mã Shadertoy | CC BY-NC-SA mặc định là phi thương mại | Học ý, tự viết |

---

## 9. Theo game

| Game | Ghi chú |
|---|---|
| **Last Line** (`games/typing-survival`) | Quy cách đủ ở guide §5. Bloom mới ở nhánh `ts-wave1`; Medium và Low không có bloom và vẽ thẳng ra màn (không composer). Tỉ lệ điểm ảnh: Low và Medium 1, High 1,5, Ultra 2 (`VIEW_TIERS` ở `scene.ts`): mọi cỡ px trong shader nhân với nó (§4.1). Chữ bay vào `FX_CORE` của súng thuộc bến đang nạp. Biến thể shader biên dịch ở `src/view/warm.ts`; giảm chuyển động qua `motionReduced()` ở `src/app/motion.ts`. Màu dành riêng: vàng (Pack Leader, `crit`, dấu gõ, `armour`, đạn Tán), đỏ `danger`, cam `hot`, lam `volt`, xanh ngọc `perfect` và `repair`, nhóm cyan của phe địch (`voltHi`, `shield`, `glass`); danh sách đủ và hue ở guide §4.1 |
| **Dragonhold** (`games/dragon-hold`) | Không bloom ở High trở xuống, tone map Neutral; MSAA chỉ ở Ultra. Khoảng trống VFX khoảng 2 ms khi máy rảnh, gần 0 khi máy bận: mỗi lớp phải đo. Draconis có sẵn `FX_HALO`, `FX_CORE`, socket cánh, đuôi, chân. Màu ta: lửa cam vàng, xanh ngọc cho Chớp và Hoàn hảo. Trang thử: `runFxShowcase` |
| **Wordwoven** (`games/typing-defense`, 2D Canvas) | Không bloom; lớp cộng sáng vẽ bằng `globalCompositeOperation = "lighter"`. Hào quang là các lớp sprite vẽ sẵn (art thật, không vẽ hình bằng mã); công tắc từng lớp, vùng bảo vệ và cách chấm giữ nguyên. Lên 3D thì theo các luật three.js ở trên |
| **Tu Tiên Thủ Ải** (`games/immortality-cultivation`) | Ảnh nguồn đã bỏ aura, ánh sáng phát ra, hạt, vật trang trí bay (`docs/games/tu-tien/art-requests/m0b/`); hào quang làm khi chạy. Hai họ hào quang (quái và phe ta) phải khác cả hình lẫn màu. Chữ gõ thành nét thư pháp ngọc bay vào tay: tay là điểm đáp của dấu gõ |

---

## Nguồn

### Trong repo

- `docs/games/VFX_STANDARD.md` §3.5–3.8, §4.1, §4.3, §4.5
- `docs/games/CHARACTER_DESIGN_GUIDE.md` §5, §7
- `docs/games/QUALITY_RESCUE_2026-11-01.md` §2.3, §4.4–4.7
- `docs/games/LESSONS_FROM_THREE_GAMES.md` §5, §11
- `docs/games/SHARED_SYSTEMS_BAR.md` §5, `docs/games/MODEL_QUALITY.md`
- `shared/game-kit/three/particles.ts`, `materials.ts`, `hero.ts`, `model-contracts.ts`
- `games/typing-survival/src/view/scene.ts`, `gun-rules.ts` (nhánh `ts-wave1`), `warm.ts`; `src/app/motion.ts`
- Skill `.agents/skills/game-hero-presence-vfx/` (`references/layers.md`, `lab-and-judging.md`, `recipes.md`)

### Web

- V1 https://github.com/mrdoob/three.js (MIT; r170)
- V2 https://threejs.org/docs/pages/UnrealBloomPass.html
- V3 https://threejs.org/examples/#webgl_postprocessing_unreal_bloom_selective
- V4 https://github.com/Alchemist0823/three.quarks (MIT; CHANGELOG có ghi peer three)
- V5 https://github.com/creativelifeform/three-nebula · https://registry.npmjs.org/three-nebula/latest (13.3.0, MIT, peer three `>=0.122.0 <1.0.0`; tôi đã mở kiểm ngày 01/11)
- V6 https://github.com/pmndrs/postprocessing · https://registry.npmjs.org/postprocessing/6.39.5 (Zlib, peer three `>= 0.168.0 < 0.187.0`; đã kiểm 01/11)
- V7 https://github.com/pmndrs/drei · https://drei.docs.pmnd.rs (MIT)
- V8 https://www.npmjs.com/package/@pmndrs/vanilla · https://registry.npmjs.org/@pmndrs/vanilla/latest (1.25.0, MIT, peer three `>=0.137`; đã kiểm 01/11)
- V9 https://github.com/The-Library-Of-Shaders · https://github.com/The-Library-Of-Shaders/the-library-of-shaders.github.io (CC0-1.0; đã kiểm 01/11)
- V10 https://www.shadertoy.com/terms (giấy phép mặc định CC BY-NC-SA 3.0)
- V11 https://github.com/patriciogonzalezvivo/thebookofshaders · https://github.com/patriciogonzalezvivo/thebookofshaders/blob/master/LICENSE ("All rights reserved", chỉ cho mục đích học; đã kiểm 01/11)
- V12 https://threejs.org/docs/#api/en/objects/Bone · https://threejs.org/docs/pages/InstancedMesh.html
- V13 https://discourse.threejs.org/t/fresnel-shader-or-similar-effect/9997/26
- V14 https://discourse.threejs.org/t/what-does-the-threshold-in-unrealbloompass-means-and-how-to-make-a-color-just-pass-that-threshold-a-bit-how-to-calculate-the-threshold-for-a-color/60984
- V15 https://threejs.org/examples/#webgl_lensflares
- V16 https://threejs.org/examples/#webgl_lines_fat
- V17 https://developer.download.nvidia.com/whitepapers/2007/SDK10/SoftParticles_hi.pdf
- V18 https://geeks3d.com/?p=8334 (bài giới thiệu demo "Phone-Wire AA" của Humus: giữ bán kính dây không nhỏ hơn một điểm ảnh, đi cùng MSAA)
- V19 https://realtimevfx.com/t/sig-sketch-50/19591/45 · https://realtimevfx.com/t/stylized-zelda-vfx/5234 (nhiễu cuộn, cuộn theo tọa độ cực)
- V20 https://threejs.org/docs/pages/BloomNode.html (TSL, chỉ WebGPU)
- V21 https://github.com/Unity-Technologies/VisualEffectGraph-Samples (LICENSE.md: Unity Companion License, chỉ cho dự án chạy Unity; đã kiểm 01/11; chỉ học)
- V22 https://dev.epicgames.com/documentation/en-us/unreal-engine/skeletal-mesh-sockets-in-unreal-engine
- V23 https://booth.pm/en/items/4822272 (bộ hào quang động cho avatar VRChat; hướng dẫn đặt `Halo_Base` ngay dưới xương Head; giấy phép VN3; đã kiểm 01/11)
- V24 https://80.lv/articles/constructing-vfx-worthy-of-league-of-legends/ · https://80.lv/articles/destiny-2-vfx-production-tips/ · https://playvalorant.com/en-us/news/dev/future-vision-the-glitchpop-story/
- V25 https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/ (12/03/2021; tôi đã mở kiểm)
- V26 https://gdcvault.com/play/1034360/Attention-Overload-Creating-Readable-VFX
- V27 `shared/game-kit/three/` (kit của ta)
- V28 https://github.com/FarazzShaikh/THREE-CustomShaderMaterial · https://registry.npmjs.org/three-custom-shader-material/6.4.0 (MIT; peer three `>=0.159`, React và R3F tùy chọn; đường `./vanilla`; đã kiểm 01/11)
- V29 https://threejs.org/docs/pages/OutputPass.html (tone map và đổi không gian màu ở cuối chuỗi pass, lấy cài đặt từ renderer)
- V30 https://github.com/mrdoob/three.js/blob/r170/src/renderers/webgl/WebGLPrograms.js (chỉ tone map khi vẽ ra màn hay target XR; đã đọc trong `node_modules/three` 0.170.0 của Last Line)
