# Thư viện và tài sản bên thứ ba

Sổ ghi mọi thư viện mã và tài sản (âm thanh, animation, texture, phông) không do dự án tự làm, dùng trong các game công khai. Luật chọn: `docs/games/SHARED_SYSTEMS_BAR.md` §5. Mỗi dòng phải kiểm giấy phép tại nguồn trước khi dùng.

| Tên | Phiên bản | Loại | Nguồn | Giấy phép | Dùng ở đâu | Ghi công cần có | Người kiểm, ngày |
|---|---|---|---|---|---|---|---|
| three.js | theo `package.json` từng game (0.170.0 ở cả ba, 29/10) | mã | https://github.com/mrdoob/three.js | MIT (`node_modules/three/LICENSE`) | cả ba game; animation dùng `AnimationMixer`, `AnimationUtils.makeClipAdditive`, `SkeletonUtils.clone`/`retargetClip`, `CCDIKSolver` (`examples/jsm`, cùng giấy phép) | không bắt buộc | animation: Claude, 29/10 |
| Mesh2Motion rig và clip (người base, người addon, chim, rắn) | bản tải 24/10/2026 | animation | https://github.com/mesh2motion/mesh2motion-app (`static/rigs`, `static/animations`) | CC0 1.0 (`LICENSE-CC0.MD`: "All 3d models, blend files, rigs, animations"); mã của app MIT (`LICENSE-MIT.MD`) | đã dùng từ 24/10 trong đường ống rig Blender của Wordwoven (`games/typing-defense/art-src/anim/mesh2motion/`, chưa ghi sổ trước đây); đề xuất cho cả ba game (`CHARACTER_ANIMATION.md` §5.2). **Không dùng** `human-mocap-animations.glb` và `CarnegieMellonAnimations/` (dữ liệu CMU, nguồn trỏ tới gói itch.io, giấy phép chưa kiểm) | không bắt buộc (CC0); ghi "Mesh2Motion" trong Credits là lịch sự | Claude, 29/10 |
| Mesh2Motion rig và clip rồng, cáo, ngựa, nhện, kaiju | chưa tải | animation | như trên | CC0 1.0 (như trên) | đề xuất (`CHARACTER_ANIMATION.md` §5.2): cáo → Blight Wolf, ngựa → Tusk Boar, nhện → Thorn Ant, kaiju → Troll, Mộc Tinh, rồng → thử cho Hỏa Long. ~4,3 MB. **Chờ chủ dự án đồng ý tải** | không bắt buộc | Claude, 29/10 |
| Quaternius Universal Animation Library (Standard) | chưa tải | animation | https://quaternius.com/packs/universalanimationlibrary.html | CC0 (trang gói) | đề xuất: Lightbearer, lính, người làng, quái hai chân. **Chờ chủ dự án đồng ý tải**; bản Source trả phí, không cần | không bắt buộc (CC0) | Claude, 29/10 |
| Quaternius Universal Animation Library 2 (Standard) | chưa tải | animation | https://quaternius.com/packs/universalanimationlibrary2.html | CC0 (trang gói) | đề xuất: combo cận chiến của lính, nông trại cho người làng, đi kiểu xác sống cho Moss Grunt. **Chờ chủ dự án đồng ý tải** | không bắt buộc (CC0) | Claude, 29/10 |
| `@pixiv/three-vrm-springbone` | 3.5.5 (npm, 29/10) | mã | https://github.com/pixiv/three-vrm | MIT (`LICENSE` của repo, `package.json`) | đề xuất: lò xo phụ (đuôi, áo choàng, cánh, cờ, tán lá) cho nhân vật chính; peer `three >= 0.137` | không bắt buộc | Claude, 29/10 |
| glTF-Transform (`@gltf-transform/core`, `functions`) | 4.5.1 (npm, 29/10) | mã (chỉ script, không vào bản chơi) | https://github.com/donmccurdy/glTF-Transform | MIT (`LICENSE.md`) | đề xuất: lấy mẫu lại, bỏ khóa thừa, lượng tử hóa clip sau Blender | không bắt buộc | Claude, 29/10 |

## Đã xét, chưa dùng hay không dùng

| Tên | Giấy phép, điều khoản (kiểm tại nguồn) | Kết luận | Người kiểm, ngày |
|---|---|---|---|
| Mixamo (Adobe) | Bài FAQ của nhân viên Adobe trên cộng đồng Adobe (29/09/2022): miễn phí, không phí bản quyền cho game, cấm phân phối file nhân vật và clip thô, không bắt buộc ghi công, cấm dùng huấn luyện máy học. Trang FAQ chính thức (helpx.adobe.com) trả 403, chưa kiểm được bản hiện hành | Không dùng mặc định. Game web phát GLB công khai, gần với "file thô"; phải tải model lên Adobe. Chỉ khi CC0 thiếu clip, chủ dự án đọc điều khoản trong tài khoản rồi quyết | Claude, 29/10 |
| `@three.ez/instanced-mesh` 0.3.16 | MIT (repo `agargaro/instanced-mesh`), peer `three >= 0.159` | Chưa chọn: skin từng con bằng mixer CPU, đắt hơn texture xương của ta khi trên 200 con; xem lại nếu cần cull hay LOD trên 400 con | Claude, 29/10 |
| OpenVAT (add-on Blender) | GPL-3.0 cho add-on (tác giả nói đầu ra tự do), MIT cho shader engine; theo trang của tác giả và trang tiện ích Blender, chưa đọc `LICENSE` của repo `sharpen3d/openvat` | Không dùng: ta tự nướng texture xương | Claude, 29/10 |
| Kenney Animated Characters 1–3 | CC0 (trang Kenney) | Không dùng: clip gắn với nhân vật của Kenney, ít giá trị cho model Tripo | Claude, 29/10 |
