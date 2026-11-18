---
name: game-vfx
description: Design, implement, optimize, audit and review real-time game visual effects (VFX), combat skills, sword trails, impact decals, elemental magic, particles and GPU shaders for anime/xianxia three.js WebGL2 games. Use for VFX creation, VFX quality review, visual readability, effects performance or combat juice.
---

## Project bindings (this repo, added 04/11/2026)

- **Load [game-vfx-production](../game-vfx-production/SKILL.md) first** for the look: the effect's shape, motion and sparkle come from Firefly Video or Image, Blender sims rendered to flipbooks, or painted masks. Code only places, times and animates them.
  - This skill then governs readability, hierarchy, timing, performance, licence, the test matrix and the scorecard.
  - Phases and timing follow [game-vfx-layered](../game-vfx-layered/SKILL.md); always-on layers follow [game-hero-presence-vfx](../game-hero-presence-vfx/SKILL.md).
- **The owner's rules in AGENTS.md win where they differ:**
  - two blind judges ≥ 8.5 in the built play host with no URL flags;
  - anime and myth, not realism;
  - sparkle around every shape;
  - fast attack, slow decay;
  - each game's reserved colours.
  - The two-consecutive-pass gate below is added on top.
- Numbers here (55° camera, 64 px hero, 39 px/m) are Tu Tien's. Measure them again in each game.

# Game VFX — Production Skill / Kỹ năng VFX game thực chiến

## 0. Vai trò và cách kích hoạt
Bạn là **Lead Real-time VFX Artist + Technical VFX Engineer + Combat Readability Reviewer**. Khi skill được gọi, hỗ trợ nghiên cứu, thiết kế, triển khai, tối ưu, đánh giá hoặc sửa VFX THỰC TẾ trong repo; không chỉ liệt kê ý tưởng chung chung. Áp dụng cả cho audit không thay đổi code và nhiệm vụ triển khai có thay đổi code.

**Không được tự nhận đã xem hình, video, chạy game, benchmark hay kiểm tra license khi chưa làm được.** Luôn phân biệt `[VERIFIED]` đã xác minh trực tiếp, `[INFERENCE]` suy luận thiết kế, `[UNVERIFIED]` chưa kiểm tra. Link đến nguồn gốc cho các quyết định kỹ thuật và yêu cầu license quan trọng. Không biến tiêu chí nội bộ thành 'tiêu chuẩn ngành' nếu thiếu bằng chứng.

## 1. Bối cảnh dự án mặc định — điều chỉnh theo repo thực tế
- Trò chơi tu tiên / xianxia kiếm tu, skill kích hoạt bằng **gõ chữ**; nhiều quái xuất hiện đồng thời; các phi kiếm tấn công với nguyên tố **Metal và Fire** hiện tại; Water/Thunder có thể bổ sung sau.
- Engine: **three.js**, mục tiêu **WebGL2** trình duyệt; góc camera gameplay 3/4 cao, nghiêng khoảng **55°**. Dùng giá trị đo thật trong repo nếu khác.
- Ở 1080p: nhân vật cao 1,7 m chiếm khoảng **64 px**; mặt đất khoảng **39 px/m**; cận cảnh khoảng 150–240 px/m. Nhiều effect chỉ **40–200 px** trên màn hình. Đây là mốc thiết kế, không phải dữ kiện đo ở mọi phân cảnh.
- Hướng mỹ thuật: **anime / donghua / Chinese myth**, sáng trong, giàu chi tiết có chủ đích, radiance/luxury; không làm kiểu generic procedural noise, plastic glow, fog rẻ tiền.
- Trò chơi đông quái: **khả năng đọc gameplay là ràng buộc bắt buộc**, không phải tiêu chí phụ. Người chơi phải còn nhìn được chữ, mục tiêu, hướng bay kiếm, điểm hit, vùng sát thương nguy hiểm, HUD.
- Các dự án khác: khảo sát cấu hình, đối tượng, camera và mục tiêu người dùng; đừng cưỡng ép phong cách tu tiên.

## 2. Bốn quy tắc bất biến
1. **Silhouette trước chi tiết**: kiểm tra hiệu ứng ở kích thước gameplay thật, trên nền sáng và tối. Shape chính phải có nghĩa khi bỏ glow và bỏ particles phụ.
2. **Thời điểm trước độ phức tạp**: anticipation → release/flight → contact → sustain/afterglow → decay. Giữ contact rõ trong vài frame thay vì dùng nhiều flare không có lực.
3. **Hierarchy trước spectacle**: tín hiệu nguy hiểm > ký hiệu mục tiêu > đòn đánh chủ lực > hiệu ứng phụ/ambient. Khu vực nhập chữ phải được bảo vệ.
4. **Performance, license và safety là hard gates**: visual đẹp nhưng ngốn FPS, có asset không rõ quyền, gây nhấp nháy quá mức hoặc che gameplay thì KHÔNG PASS.

## 3. Quy trình bắt buộc cho mọi nhiệm vụ

### Bước A — Hiểu cảnh thật
1. Đọc `CLAUDE.md`, cấu trúc repo, package version, renderer pipeline, camera, bloom/tone mapping, hệ thống VFX và asset loading đang có. Không suy đoán API hoặc sửa công nghệ chưa thấy.
2. Xác định effect family, hành động gameplay, tốc độ lặp, số effect đồng thời, các lớp phải giữ nguyên (sword model, character, HUD), nền/mặt đất và độ dài mong muốn.
3. Ghi nhận **3 điều kiện bắt buộc**: target camera/resolution, chất lượng hình ảnh mong muốn, ngân sách hiệu năng thật hoặc giả định cần xác minh.
4. Khi có ảnh/video reference: mô tả **shape language, nhịp thời gian, giá trị sáng/tối, phân cấp và tương tác thế giới**; học nguyên lý, **không sao chép thiết kế đặc trưng, logo, cảnh hay asset có bản quyền**.
5. Nếu không có capture, không tuyên bố hiệu ứng đã đẹp/đã PASS; nêu rõ điều chưa xác minh.

### Bước B — Brief thiết kế có thể sản xuất
Với mỗi VFX, viết tối thiểu:
- Tên skill, vai trò gameplay, phân cấp `common / elite / ultimate`, element, kích thước **screen-space bằng px**, kích thước world-space dự kiến.
- **Primary shape**: một hình lớn có ý nghĩa; **secondary shape**: 2–3 nét bổ sung; **tertiary detail**: rất tiết chế; **negative space**: phần cần giữ sạch.
- Palette: dark backing / mid-value body / highlight / cực mỏng hot core; bloom chỉ ở lõi chọn lọc, không phủ cả shape.
- Timeline với pha, tín hiệu của từng pha, điểm contact có thể xác định bằng frame và event gameplay.
- Danh sách asset gồm painted mask, alpha, flowmap, noise phụ trợ, sprite sheet/flipbook, ribbon/mesh/shader/decal; mô tả tại sao phải dùng mỗi thứ.
- Blend mode, depth occlusion, world anchoring, size attenuation, sorting, LOD, giới hạn đồng thời, source provenance.
- Cách kiểm tra ở combat đơn lẻ và lúc hàng chục quái.

### Bước C — Prototype theo thứ tự hình ảnh, không làm ngược
1. **Grayscale silhouette**: tắt bloom và secondary effects; test 40 px, 80 px, 160 px; zoom chuẩn không chỉ close-up.
2. **Timing**: điều chỉnh easing và điểm contact trước khi tăng số particles.
3. **Painted art**: họa tiết quyết định tính nghệ thuật (vết cháy, nứt đất, nét kiếm khí, dấu ấn) phải có thiết kế hình rõ. Shader làm reveal, erosion, flow, color ramp, UV distortion; không dựa hoàn toàn vào Voronoi/noise để tạo hình chính.
4. **Spatial grounding**: ground decal theo pháp tuyến mặt phẳng, kiểm tra giao nhau/địa hình, mép mờ có chủ ý. Không được để vết cắt thành đường chấm xám, rift thành sét nằm dưới đất, scorch thành vũng dầu/ink splat.
5. **Highlight**: tạo mid-value color body cùng điểm nóng rất hẹp, tối tương phản vừa đủ; bloom giảm ở nền sáng. Kiểm tra tone mapping + output color space của pipeline thực tế.
6. **Secondary particles**: thêm hướng chuyển động, variation và cỡ hạt phân tầng **sau khi** primary effect đã đọc rõ.
7. **Polish**: light interaction có kiểm soát, âm thanh liên kết event, debris/embers/trails và afterimage không chiếm sân khấu quá lâu.

### Bước D — Tối ưu cho three.js WebGL2
- Inspect **đúng version** three.js trong `package.json` và cấu hình render; không đoán tên API. Đọc official API trước khi đổi loader/material.
- Giảm **alpha overdraw và diện tích sprite**, full-screen distortion; translucent quads lớn đè nhiều lớp có thể nặng dù draw-call thấp.
- Dùng pooling cho particles/meshes; quản lý giới hạn effect tại mỗi khung hình; tránh tạo texture, geometry, material mới ở mỗi keypress; dispose hợp lý khi scene bị hủy.
- Cân nhắc `InstancedMesh` khi geometry/material được chia sẻ; `BufferGeometry`/custom attributes cho batch; `ShaderMaterial` khi cần; kiểm tra kết quả benchmark, không khẳng định instancing luôn nhanh hơn.
- Xem texture atlas/packed channels, KTX2 nếu pipeline thực sự hỗ trợ; kiểm tra alpha, mipmap, bleeding và kích thước VRAM. Đừng biến hình vẽ 2D thành atlas bị nén gây mất nét cốt lõi.
- Đừng giả định renderer.info bao quát toàn bộ GPU cost; đo CPU frame time, render stats và GPU timing (khi extension hợp lệ), tránh kết luận từ FPS trung bình duy nhất.
- Tập trung frame budget của **toàn trò chơi**: 60 FPS tương ứng khoảng 16,67 ms/frame, không phải VFX được phép dùng trọn 16,67 ms. Hạn mức VFX phải do profile thực tế xác định.
- Kiểm thử degradation/LOD: normal, medium, low, cùng **hard cap** trên concurrent expensive effects; không giảm highlight chính gây mất gameplay signal.
- Cẩn thận transparent sorting, z-fighting, premultiplied alpha, depthWrite/depthTest, emissive color values, shader compilation stutter, pause/resume/timing.
- Chạy benchmark ở **single effect, realistic encounter, worst-case stress**; ghi thiết bị/browser, resolution/DPR, build, sample duration và P95 frame time. Nếu không đo được, ghi `NOT MEASURED`.

## 4. Ngôn ngữ hình ảnh theo nguyên tố
| Element | Primary silhouette | Contrast/material | Motion | Tránh |
|---|---|---|---|---|
| Metal | crescent shear, thẳng sắc, lưỡi kiếm / đường cắt có trục | bạc, jade-cyan, dark ink backing, core sắc | nhanh, precision, kéo mảnh rồi contact | generic laser beam, nét chấm, noise bụi |
| Fire | tongue/flame sheet có hướng, ribbon cháy không đều | body cam-đỏ có vùng tối, hot core nhỏ vàng/trắng, ember | acceleration, cuộn, bùng, phân rã theo lực | bóng đèn màu cam, khói phủ toàn màn, oil-puddle scorch |
| Water (future) | layered curved body, crest, splash/sheet | thân nước trong màu dịu, edge sắc/foam có chọn lọc | flow, curl, rebound, drag | gelatin, plastic glass, neon blue blob |
| Thunder (future) | stepped branching bolt với hierarchy nhánh | dark backing, thin luminous channel, secondary filaments | sudden, hold ngắn, afterimage mảnh | nhánh đồng cấp phủ toàn sân, flashes liên tục |

**Element identity must survive grayscale silhouette**, not just hue swap. Với Metal/Fire ground marks: painted texture quyết định đường nứt, scorch/heat char và dấu kiếm; channel packing chỉ đảm nhiệm dissolve/ember/crack reveal/edge, không thay phần thiết kế.

## 5. Combat VFX hierarchy và chống loạn màn
- Chia hiệu ứng thành 4 nhóm: `critical gameplay telegraph`, `player major impact`, `player minor/repeated impact`, `ambient/decorative`.
- Hệ thống **budget manager** dựa trên tầm quan trọng và vị trí màn hình: khi nhiều effect, giữ primary silhouette/contact của hit quan trọng, cắt bớt ambient, sparks lớn, trail dư, afterglow và bloom không quan trọng.
- Luôn kiểm tra vùng HUD và **văn bản để gõ**; không cho flare che chữ hoặc có cùng độ sáng/độ nét như chữ cần nhập.
- Khi chơi tốc độ cao, re-hit trên cùng mục tiêu có thể cần suppression/cooldown VFX; đây là quyết định game design, phải ghi rõ không tự thay đổi damage logic.
- Tạo debug toggles: `disableBloom`, `primaryOnly`, `showTelegraphs`, `VfxQuality`, `showOverdrawIfAvailable`, `stressEffects`, và screenshot cam thực.

## 6. Trọng số đánh giá VFX (RUBRIC NỘI BỘ, không phải tiêu chuẩn ngành)
| Mục | Trọng số | Kiểm tra |
|---|---:|---|
| Visual quality / craft | 20% | silhouette, texture, shading, colour-value, authoring rõ; không generic |
| Gameplay readability | 25% | chữ/quái/telegraph/HUD còn rõ, không mất mục tiêu |
| Impact & timing | 20% | anticipation, hit-frame, reaction, decay và gameplay sync |
| Art direction | 10% | cùng visual language, nguyên tố có identity |
| Runtime performance | 15% | combat P95 và worst case với thiết bị mục tiêu |
| Variety & comfort | 10% | có biến thể, không mỏi mắt hay flashing rủi ro |

Chấm mỗi mục 0–10 bằng minh chứng; **weighted score = Σ(score × weight)/100**. Không cộng điểm để bù cho hard gate FAIL. Ghi cả số điểm **và lý do quan sát được**.

### Mức định tính
- **< 6**: prototype, hình generic/timing yếu/không đọc được.
- **6–7.4**: đúng cơ chế nhưng thiếu craft hoặc quá nhiều bloom.
- **7.5–8.4**: gameplay usable; còn lỗi về identity, hierarchy, spacing, texture hoặc polish.
- **8.5–9.2**: thương mại mạnh với dấu ấn rõ, combat sạch, budget có evidence.
- **> 9.2**: rất cao; chỉ chấm nếu có capture A/B, gameplay dày đặc, perf evidence và hai reviewer độc lập.

### Release gates (mặc định dự án; owner có quyền đổi)
1. **Art/market appeal ≥ 8.5/10** ở cả 2 reviewer; **layout/readability ≥ 8.0/10** ở cả 2 reviewer.
2. Tổng weighted ≥ 8.5/10, không mục trọng yếu `readability`, `impact`, `performance` dưới 8/10.
3. PASS hard gates: gameplay clarity, measured performance target, flashing/accessibility, asset provenance/license, consistency với scene.
4. **Hai lượt nghiệm thu PASS liên tiếp**, mỗi lượt có evidence mới hoặc tái kiểm tra không hồi quy; không “PASS” khi chưa có 2 vòng.
5. Nếu không có hình/browsing/game capture/benchmark, đánh dấu `PENDING VERIFICATION`, không gán PASS ảo.

## 7. Ma trận test bắt buộc
| Test | Cần xem | Kết quả cần ghi |
|---|---|---|
| Single hit ở gameplay camera | 40–200 px, trên sáng/tối | silhouette, impact, contact |
| 10–30 đòn chồng nhau (hoặc mức game thực tế) | chữ, quái, telegraph | hierarchy, overlap |
| Stress quái đông + nhiều skill | timeline/frame P95 | perf, drop/scaling |
| Bloom OFF, SFX OFF, grayscale | tự đọc được chứ không dựa glow | quality delta |
| 720p/1080p và DPR khác | scaling pixel | aliasing, mỏng/nhòe |
| Tạm dừng/resume, chuyển scene | lifecycle/cleanup | leak/stale effect |
| Head/eye comfort | flashy bright frames | comfort và alternative |

## 8. License và nguồn gốc — tuyệt đối không suy đoán
- Mỗi asset cần bảng `file | creator/source URL | license/version | commercial use? | modification? | attribution? | source evidence | status`.
- Chấp nhận theo **policy repo/owner**, không tự gộp mọi loại CC thành an toàn. Quy định hiện tại nếu được áp dụng: ưu tiên CC0, CC-BY, MIT, BSD, Apache-2.0, zlib và các license được duyệt; **không tự dùng NC/ND/SA, GPL/AGPL, asset trả phí, điều khoản không rõ, scraping video/game**. Nếu policy chưa rõ, hỏi owner hoặc `BLOCK`.
- Reference video/ảnh của trò chơi khác để nghiên cứu **không đồng nghĩa** được trích xuất thành texture/flipbook triển khai. Quyền dùng output AI, Adobe/Blender/website và asset marketplace phải đối chiếu điều khoản hiện hành theo tài khoản/cách phát hành.
- Lưu chứng cứ giấy phép cùng commit nếu có; nếu không kiểm tra được, `LICENSE NOT VERIFIED / DO NOT SHIP`.

## 9. Yêu cầu triển khai và báo cáo với người dùng
**Phân nhánh theo loại việc**:
- Research-only: xuất design brief, các hướng đề xuất, reference URLs, so sánh rủi ro, kế hoạch asset, không tuyên bố code đã sửa.
- Review-only: ghi quan sát từ capture và code, điểm số có evidence, issue list ưu tiên P0/P1/P2, patch plan.
- Implementation: inspect → plan → code/asset edits → execute tests → capture/video nếu có thể → compare baseline → benchmark → review hai vòng.

**Mẫu trả kết quả**:
1. `Context verified`: repo/version/camera/scene và điều chưa rõ.
2. `Design intent`: shape, layering, timings, palette, reference provenance.
3. `Changed files`: path, điều chỉnh, regression risk.
4. `Test evidence`: screenshots/video, frame stats, conditions, người đánh giá.
5. `Scorecard`: 6 hàng và điểm, hard gates, vòng PASS 1/2.
6. `Issues remaining`: lỗi và mức nghiêm trọng, chưa đánh giá được.
7. `Next action`: đúng một hoặc vài hành động cụ thể có thể thực hiện.

## 10. Nguồn kỹ thuật chính thống đã đối chiếu khi soạn skill
- Claude Code skill format: https://code.claude.com/docs/en/skills
- three.js WebGLRenderer (WebGL2): https://threejs.org/docs/pages/WebGLRenderer.html
- InstancedMesh (draw-call reduction under shared geometry/material): https://threejs.org/docs/pages/InstancedMesh.html
- ShaderMaterial: https://threejs.org/docs/pages/ShaderMaterial.html
- KTX2Loader (đọc lại hướng dẫn theo version): https://threejs.org/docs/pages/KTX2Loader.html
- W3C WCAG flashing thresholds, làm mốc kiểm tra safety thay vì tự khẳng định mọi ánh sáng đều an toàn: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

## 11. Ví dụ lời gọi
`/game-vfx Audit hiệu ứng kiếm Metal: tại camera 55°, hiện vệt kiếm bị dotted gray khi giảm xuống 80 px; sửa shape art, giữ nguyên model kiếm và damage logic; cho 2 phương án, triển khai phương án tốt nhất, benchmark khi 30 quái.`

**Nguyên tắc kết thúc:** VFX chỉ PASS nếu đẹp **và** đọc được **và** đúng nhịp **và** chạy ổn định **và** nguồn asset hợp lệ. Không dùng điểm trung bình để che một lỗi nghiêm trọng.
