# Da nhân vật: độ bóng và tán xạ dưới da (nghiên cứu 18/11/2026)

Chủ dự án, 18/11/2026: "về da của nhân vật, việc trắng hồng là chưa đủ, nó phải kèm 1 chút bóng để cho giống da thật".
Mô hình thử: `games/immortality-cultivation/art-src/heroine/models3d/base-body.v5B.tripo-try1.glb` (không sửa hình khối, không ghi đè GLB).
Ảnh so sánh: `typing-game-review/owner-review/2026-11-18/tu-tien/tripo-v5b-mirror/skin-shading-ABC.png` (hiện tại | A | B | C).

## 1. Da thật trông "thật" nhờ bốn lớp

1. **Tán xạ dưới da (SSS).** Ánh sáng đi vào da, đỏ đi xa hơn xanh lá và xanh lam, nên vùng chuyển sáng tối ấm và mềm, tai, mũi, ngón tay ửng đỏ khi ngược sáng. Thiếu lớp này da trông như nhựa hoặc sáp khô.
2. **Phản xạ gương thấp nhưng có.** Da là điện môi, IOR khoảng 1,4, tức F0 khoảng 0,028 (2,8 %), thấp hơn mức mặc định 0,04 của PBR. Unreal đặt Specular của da 0,35 thay vì 0,5.
3. **Hai thùy bóng (dual lobe).** Lớp dầu mỏng trên biểu bì cho một vệt bóng hẹp, bề mặt da cho một vệt rộng. Unreal và Unity đều trộn hai độ nhám.
4. **Độ bóng thay đổi theo vùng.** Môi và mũi bóng hơn (Weyrich 2006 đo 10 vùng trên 149 khuôn mặt; GPU Gems 3 ch.14 dùng kết quả đó). Trong làm nghề, vùng chữ T (trán, sống mũi, đầu mũi), gò má, cằm và môi bóng hơn má ngoài, cổ và thân. Bản đồ độ nhám gắn theo vật thể (không lặp ô) là cách Epic khuyên.

Thêm: chi tiết vi mô (lỗ chân lông, nếp) trong normal map làm vệt bóng vỡ ra tự nhiên; khi ở xa, độ nhám phải tăng (mip sáng hơn) để không lấp lánh.

## 2. Nguồn (đã đọc tận nơi, 18/11/2026)

| Nguồn | Điều đã kiểm |
| --- | --- |
| [GPU Gems 3, ch.14 Advanced Techniques for Realistic Real-Time Skin Rendering](https://developer.nvidia.com/gpugems/gpugems3/part-iii-rendering/chapter-14-advanced-techniques-realistic-real-time-skin) | F0 = 0,028 từ IOR 1,4; BRDF Kelemen/Szirmay-Kalos; môi và mũi bóng hơn theo số đo Weyrich; đỏ tán xạ xa hơn xanh |
| [Epic: Creating Human Skin in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/creating-human-skin-in-unreal-engine) | Specular da 0,35 (từ số đo thật); bắt đầu Roughness hằng khoảng 0,4; dùng texture độ nhám không lặp; mip nhỏ sáng hơn |
| [Epic: Subsurface Profile shading model](https://dev.epicgames.com/documentation/unreal-engine/subsurface-profile-shading-model-in-unreal-engine?lang=en-US) | Dual specular: Roughness 0 (thùy mềm), Roughness 1 (thùy hẹp), Lobe Mix |
| [UE5 Python API, SubsurfaceProfileStruct](https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/SubsurfaceProfileStruct.html) | Mặc định roughness0 = 0,75, roughness1 = 1,3 (hệ số nhân), lobe_mix = 0,85 (theo kết quả tìm kiếm, chưa mở trang) |
| [Unity HDRP roadmap: Skin dual lobe and diffuse power](https://activation.unity3d.com/roadmap/2120-skin-dual-lobe-and-diffuse-power) | Hai thùy bóng vì lớp dầu mỏng trên biểu bì |
| [Penner, Pre-integrated Skin Shading, SIGGRAPH 2011](https://www.slideshare.net/slideshow/penner-preintegrated-skin-rendering-siggraph-2011-advances-in-realtime-rendering-course/13966747) | SSS rẻ: tra bảng theo N·L và độ cong, không cần làm mờ màn hình; hợp với WebGL |
| [Jimenez et al., Separable Subsurface Scattering](https://graphics.unizar.es/papers/Separable-Subsurface-Scattering.pdf) | SSS màn hình hai lượt tích chập 1D; dùng trong engine game; đắt hơn cho trình duyệt |
| [Blender manual, Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) | Subsurface Weight, Radius (R,G,B), Scale, IOR, phương pháp Random Walk (Skin); Sheen = sợi mảnh (lông tơ) |
| [three.js MeshPhysicalMaterial](https://threejs.org/docs/pages/MeshPhysicalMaterial.html) | sheen, sheenRoughness, sheenColor, clearcoat, specularIntensity (0–1), ior (mặc định 1,5), thickness, transmission |
| [three.js SubsurfaceScatteringShader](https://threejs.org/docs/pages/module-SubsurfaceScatteringShader.html) | Xuyên sáng rẻ theo GDC 2011 (Approximating Translucency) |
| [three.js forum: Skin shading with SSSSS](https://discourse.threejs.org/t/skin-shading-with-screen-space-sub-surface-scattering/83939) | Có người làm SSS màn hình trong three.js, đắt |

## 3. Tripo cho gì, ta thêm gì

Đo trên GLB v5B (một material, texture 4096):
- **baseColor**: tốt, giữ nguyên (đo trước: da L* 74,8 so với nguồn 76,9).
- **ORM**: R = 1 (không có AO), G = độ nhám, B = kim loại. Trên vùng da: độ nhám p5/p50/p95 = 0,34 / 0,37 / 0,58; kim loại trung vị 0,03, p95 0,08. Độ nhám gần như đều, không có vùng chữ T hay môi; kim loại khác 0 trên da là sai (da là điện môi).
- **Normal (GL)**: có chi tiết khối, gần như không có lỗ chân lông.
- **Không có**: SSS, IOR da, bản đồ vùng bóng, thùy bóng thứ hai, lông tơ.

Ta thêm (file mới cạnh GLB, GLB không đổi):
- `base-body.v5B.tripo-try1.skin-mask.png` (2048, 1 = da, tính từ màu baseColor; còn lẫn vài đốm ở tóc sáng).
- `base-body.v5B.tripo-try1.skin-shine-mask.png` (2048, vùng chữ T, gò má, cằm; bake từ vị trí 3D quanh đầu mũi).
- `base-body.v5B.tripo-try1.skin-lips-mask.png` (2048, môi).

## 4. Ba mức đã render (Blender Cycles, Random Walk Skin)

Chung: Subsurface Weight = mặt nạ da (A 0,8; B, C 1,0), Radius (1,0; 0,35; 0,2), Scale 0,004 (mô hình cao 1 m), IOR 1,4, kim loại trên da = 0, độ nhám da = nền + (ORM.G − 0,43) × 0,5 để giữ biến thiên vi mô của Tripo.

| Mức | Nhám thân/má | Nhám chữ T, gò má, cằm | Nhám môi | Coat (thùy hẹp) | Sheen (lông tơ) |
| --- | --- | --- | --- | --- | --- |
| A nhẹ | 0,55 | 0,42 | 0,36 | 0 | 0 |
| **B vừa (đề xuất)** | **0,48** | **0,34** | **0,27** | **0,08, nhám 0,35** | **0,12, nhám 0,35, màu ấm** |
| C căng bóng | 0,40 | 0,24 | 0,18 | 0,25, nhám 0,18 | 0,15 |

## 5. Đưa vào three.js (game)

`MeshPhysicalMaterial` cho riêng da (tách bằng skin-mask hoặc tách material):
- `ior: 1.4` (F0 ≈ 0,028), `specularIntensity: 1`, `metalness: 0` trên da (hoặc nhân kênh B của ORM với 1 − skinMask).
- `roughnessMap`: ORM mới, kênh G = công thức mức B ở trên (nướng sẵn bằng script, không tính trong shader).
- Thùy hẹp: `clearcoat: 0.08`, `clearcoatRoughness: 0.35`, `clearcoatMap` = skin-mask (để quần áo không bóng).
- Lông tơ: `sheen: 0.12`, `sheenRoughness: 0.35`, `sheenColor: #ffd9cc`.
- SSS: **không** dùng `transmission`/`thickness` (đắt, làm da trong như thạch). Thay bằng wrap lighting qua `onBeforeCompile` (diffuse = max(0, (N·L + w)/(1 + w)), w ≈ 0,3 cho kênh đỏ, 0,15 xanh lá, 0,1 xanh lam), hoặc bảng tra Penner theo N·L và độ cong. Nhớ đặt `customProgramCacheKey`.
- Ở camera chơi (khoảng 55°, nhân vật nhỏ), chỉ thùy rộng và wrap là thấy; coat và sheen chỉ đáng giữ ở cận cảnh, cut-in và màn chọn nhân vật.
- Tone mapping và môi trường quyết định nhiều như material: cần envMap (PMREM) ấm để da có vệt bóng; không có môi trường thì độ nhám nào cũng trông khô.

## 6. Việc còn mở

- Mặt nạ da lấy từ màu nên lẫn đốm ở tóc sáng; nên tô tay lại trong Blender hoặc tách theo đảo UV.
- Mặt nạ vùng mặt đặt theo tỉ lệ từ đầu mũi; vùng môi hơi thấp và rộng, vùng chữ T chạm mí mắt.
- Chưa thử trong three.js; cần một bản lab và chấm mù 8.5 trong play host như luật.
