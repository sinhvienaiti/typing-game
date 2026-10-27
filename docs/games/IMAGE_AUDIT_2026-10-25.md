# Kiểm kê ảnh 2D ba game · Phiếu 015

Tên file theo phiếu 25/10/2026; kiểm kê và bàn giao trên Mac mini M4 ngày **26/10/2026**. Đường dẫn tính từ gốc repo. Không kiểm kê hoặc sửa Tu Tiên.

## 1. Phạm vi, nguồn và cách đếm

- **Rồng Giữ Ải:** 00-canon, DESIGN §7.2, §9, tài liệu 02/03/05/06 và toàn bộ prompt M0 trong docs/games/dragon-lane. Hiện M0a thuộc M0; kế tiếp **M0b hình**, vẫn đúng bộ 67 ảnh; không mở M1/M2.
- **Lời Gọi:** BUILD_1B §13, TYPING_DEFENSE_DESIGN §8.9, §10.3, §16, §23, §26–27 và docs/art-requests/td trong game. 1B còn vẽ Canvas; P chuẩn bị 1C/bước 2, VS chuẩn bị lát dọc. Có ảnh nguồn không có nghĩa đã tích hợp.
- **Tuyến Cuối:** BUILD_S1 §1.1, §6, §12; SURVIVAL_MODE_PLAN §4.2–4.4 và bảng mốc. S1 dùng chung model Space; S2 thêm lò, mảnh chữ, Nova, Chuỗi, ô nguyên tố. Không sinh lại model dùng chung.
- Đọc README-samples, README-m0-wave1-3, README-m0-wave4-5, README-m0-redo của Rồng; README-tripo, README-vs-characters, README-vs-buildings của Lời Gọi. Đối chiếu cả last.md của 005a, 005b và **005b2** trong .local/codex-runs.
- “Đã có” chỉ xác nhận file. “Có nhưng lỗi” giữ lỗi README cũ hoặc lỗi kiểm trực tiếp. File .tripo/.alpha/.seamless của 012 chưa thay bằng chứng duyệt; **không dùng art-normalize**.
- Một góc = một ảnh; một atlas/flipbook = một ảnh. Không cộng .v1, ảnh xem nhanh hoặc ứng viên sửa 015 thành nhu cầu mới. Góc khuyến nghị đã bàn giao được liệt kê; không biến mọi góc tùy chọn chưa làm thành ảnh bắt buộc.
- Bỏ tầng td/ cũ của art-src/td/ khi đọc đường dẫn Lời Gọi đã tách. 005a/005b2 có **119 PNG = 49 + 70**, đại diện 115 model; bỏ qua phần nguồn 3D VS đó, kể cả lỗi. **200 ảnh VS dùng thẳng 2D là nhóm khác**, chưa được 005a/005b2 làm.

## 2. Rồng Giữ Ải · M0 → M0b

Đủ 67/67 đích từ trước 015: 16 sinh vật/mẫu + 6 phe ta + 12 prop + 13 đất/decal/phông + 20 icon. 015 thử 8 đích qua 12 lượt sinh, gồm 4 lần thử lại. Xem [README-015](../../games/dragon-hold/art-src/README-015.md); đủ file không có nghĩa đủ chất lượng.

| Mã | Nội dung | Trạng thái | Ảnh | Lỗi / ghi chú |
|---|---|---|---|---|
| HT-A | Ảnh thử dấu Héo A (vỏ ít) | Đã có | [games/dragon-hold/art-src/refs/heo-test-a.png](../../games/dragon-hold/art-src/refs/heo-test-a.png) | Mẫu đối chiếu; đã chọn dấu A. Không gửi Tripo. |
| HT-B | Ảnh thử dấu Héo B (vỏ nhiều) | Đã có | [games/dragon-hold/art-src/refs/heo-test-b.png](../../games/dragon-hold/art-src/refs/heo-test-b.png) | Mẫu đối chiếu; đã chọn dấu A. Không gửi Tripo. |
| E09-F | E09 Yêu Rêu Lính · ảnh chính, nhìn thẳng | Đạt 9 | [games/dragon-hold/art-src/enemies/moss-grunt.png](../../games/dragon-hold/art-src/enemies/moss-grunt.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model moss-grunt.glb. Lệch nhỏ (gối, số ngón, rêu hơi chìm trên cỏ); chưa có xương, xoay mặt khi rig. Không làm lại ảnh. |
| E09-B | E09 · nhìn sau | Đạt 9 | [games/dragon-hold/art-src/enemies/moss-grunt-back.png](../../games/dragon-hold/art-src/enemies/moss-grunt-back.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model moss-grunt.glb. Lệch nhỏ (gối, số ngón, rêu hơi chìm trên cỏ); chưa có xương, xoay mặt khi rig. Không làm lại ảnh. |
| E18-S | E18 Sói Mục · ảnh chính, nhìn ngang | Đạt 9,5 | [games/dragon-hold/art-src/enemies/blight-wolf.png](../../games/dragon-hold/art-src/enemies/blight-wolf.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model blight-wolf.glb. Tai thiếu vết khía; chưa có xương, rig bằng Blender. Không làm lại ảnh. |
| E18-F | E18 · nhìn thẳng | Đạt 9,5 | [games/dragon-hold/art-src/enemies/blight-wolf-front.png](../../games/dragon-hold/art-src/enemies/blight-wolf-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model blight-wolf.glb. Tai thiếu vết khía; chưa có xương, rig bằng Blender. Không làm lại ảnh. |
| E01-F | E01 Ong Gai · ảnh chính, nhìn thẳng | Tạm chấp nhận 7,5 | [games/dragon-hold/art-src/enemies/thorn-wasp.png](../../games/dragon-hold/art-src/enemies/thorn-wasp.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model thorn-wasp.glb. Hai cánh dựng đứng: khi rig Blender xoay mỗi cánh 80–90°. Giữ ảnh Front làm nguồn nếu dựng lại. |
| E01-S | E01 · nhìn ngang | Tạm chấp nhận 7,5 | [games/dragon-hold/art-src/enemies/thorn-wasp-side.png](../../games/dragon-hold/art-src/enemies/thorn-wasp-side.png)<br>Ứng viên: [games/dragon-hold/art-src/enemies/thorn-wasp-side-015.png](../../games/dragon-hold/art-src/enemies/thorn-wasp-side-015.png) | 015 thử thêm đúng 1 lần; vẫn lộ mặt cánh. Không dùng ô Left; dùng Front riêng nếu dựng. Chấm lại 26/10: đã chấm model thorn-wasp.glb (cánh dựng đứng, sửa khi rig). Không làm lại ảnh Side; nếu dựng lại chỉ dùng Front. |
| E11-F | E11 Yêu Rêu Cung · ảnh chính | Đạt 9 | [games/dragon-hold/art-src/enemies/moss-archer.png](../../games/dragon-hold/art-src/enemies/moss-archer.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model moss-archer.glb. Rêu hơi chìm trên cỏ, dây cung mảnh; kiểm tay cầm cung khi rig. Không làm lại ảnh. |
| E11-B | E11 · nhìn sau | Đạt 9 | [games/dragon-hold/art-src/enemies/moss-archer-back.png](../../games/dragon-hold/art-src/enemies/moss-archer-back.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model moss-archer.glb. Rêu hơi chìm trên cỏ, dây cung mảnh; kiểm tay cầm cung khi rig. Không làm lại ảnh. |
| E19-S | E19 Heo Nanh Đá · ảnh chính, nhìn ngang | Đạt 9,5 | [games/dragon-hold/art-src/enemies/tusk-boar.png](../../games/dragon-hold/art-src/enemies/tusk-boar.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model tusk-boar.glb. Chưa có xương, rig bằng Blender. Không làm lại ảnh. |
| E19-F | E19 · nhìn thẳng | Đạt 9,5 | [games/dragon-hold/art-src/enemies/tusk-boar-front.png](../../games/dragon-hold/art-src/enemies/tusk-boar-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model tusk-boar.glb. Chưa có xương, rig bằng Blender. Không làm lại ảnh. |
| E25-S | E25 Kiến Gai · ảnh chính, nhìn ngang | Đạt 9,5 | [games/dragon-hold/art-src/enemies/thorn-ant.png](../../games/dragon-hold/art-src/enemies/thorn-ant.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model thorn-ant.glb. Đủ sáu chân; chân mảnh, rig Blender cẩn thận. Không dùng bản .v1. |
| E25-F | E25 · nhìn thẳng | Đạt 9,5 | [games/dragon-hold/art-src/enemies/thorn-ant-front.png](../../games/dragon-hold/art-src/enemies/thorn-ant-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model thorn-ant.glb. Đủ sáu chân; chân mảnh, rig Blender cẩn thận. Không dùng bản .v1. |
| G01-F | G01 Yêu Rêu Cầm Cờ · ảnh chính | Đạt 9 | [games/dragon-hold/art-src/generals/moss-banner.png](../../games/dragon-hold/art-src/generals/moss-banner.png)<br>Ứng viên: [games/dragon-hold/art-src/generals/moss-banner-015.png](../../games/dragon-hold/art-src/generals/moss-banner-015.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. Chấm lại 26/10: đã chấm model moss-banner.glb. Tay cờ gập, cán dính tay: tách cán cờ khi rig Blender. Không cần ứng viên 015 hay dựng lại. |
| G01-B | G01 · nhìn sau | Đạt 9 | [games/dragon-hold/art-src/generals/moss-banner-back.png](../../games/dragon-hold/art-src/generals/moss-banner-back.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. Chấm lại 26/10: đã chấm model moss-banner.glb. Tay cờ gập, cán dính tay: tách cán cờ khi rig Blender. Không cần ứng viên 015 hay dựng lại. |
| TR1 | Gai Chông `spikes` | Đạt 9 | [games/dragon-hold/art-src/traps/spikes.png](../../games/dragon-hold/art-src/traps/spikes.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model spikes.glb. Ở 30–50 px chông thành hàng chấm; tỉ lệ 2:1 khớp hộp tạm. Không làm lại ảnh. |
| TR2 | Bom Hạt Thông `pine-bomb` | Đạt 9,5 | [games/dragon-hold/art-src/traps/pine-bomb.png](../../games/dragon-hold/art-src/traps/pine-bomb.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model pine-bomb.glb. Hạt nhựa chỉ còn đốm nhỏ; dùng ngay. |
| TR3 | Lưới Phóng `net-launcher` | Đạt 9,5 | [games/dragon-hold/art-src/traps/net-launcher.png](../../games/dragon-hold/art-src/traps/net-launcher.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model net-launcher.glb. Gỗ hơi rối ở 30–50 px; chỉnh hướng bằng preset. |
| U1-F | Vệ Binh Rêu `moss-warden` · ảnh chính | Tạm chấp nhận 8 | [games/dragon-hold/art-src/units/moss-warden.png](../../games/dragon-hold/art-src/units/moss-warden.png)<br>Ứng viên: [games/dragon-hold/art-src/units/moss-warden-015.png](../../games/dragon-hold/art-src/units/moss-warden-015.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. Chấm lại 26/10: đã chấm model moss-warden.glb. Chùy nhân đôi, khiên hai mặt: xóa phần thừa trong Blender trước khi rig. Nếu dựng lại dùng moss-warden-015.png. |
| U1-B | Vệ Binh Rêu · nhìn sau | Tạm chấp nhận 8 | [games/dragon-hold/art-src/units/moss-warden-back.png](../../games/dragon-hold/art-src/units/moss-warden-back.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. Chấm lại 26/10: đã chấm model moss-warden.glb. Chùy nhân đôi, khiên hai mặt: xóa phần thừa trong Blender trước khi rig. Nếu dựng lại dùng moss-warden-015.png. |
| H1 | Lều Thuốc Nam `herb-hut` | Đạt 9,5 | [games/dragon-hold/art-src/houses/herb-hut.png](../../games/dragon-hold/art-src/houses/herb-hut.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model herb-hut.glb. Tường mặt sau hơi nhòe. |
| K01 | Thông cao | Đạt 9,5 | [games/dragon-hold/art-src/props/pine-river/pine-tall.png](../../games/dragon-hold/art-src/props/pine-river/pine-tall.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model pine-tall.glb. Tán tối hơn ảnh, mặt sau nhạt hơn. |
| K02 | Thông dù già | Đạt 9,5 | [games/dragon-hold/art-src/props/pine-river/pine-round.png](../../games/dragon-hold/art-src/props/pine-river/pine-round.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model pine-round.glb. Dẹt theo chiều sâu; từ camera game vẫn tốt. |
| K03 | Thông non | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/props/pine-river/pine-young.png](../../games/dragon-hold/art-src/props/pine-river/pine-young.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model pine-young.glb. Tán bóng như nhựa (roughness 0,33), thân gần đen: trong Blender đặt roughness 1, tô thân nâu rồi chấm lại. |
| K04 | Cây tán tím (xa đường) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/props/pine-river/tree-violet.png](../../games/dragon-hold/art-src/props/pine-river/tree-violet.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model tree-violet.glb. Nửa trước tán chàm, thân xám: chỉnh hue về #8E7CC3, tô thân kem trong Blender. |
| K05 | Bụi rêu | Đạt 9,5 | [games/dragon-hold/art-src/props/pine-river/bush-moss.png](../../games/dragon-hold/art-src/props/pine-river/bush-moss.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model bush-moss.glb. Còn vài nhánh lá lộ. |
| K06 | Bụi hoa kem, tím | Đạt 9 | [games/dragon-hold/art-src/props/pine-river/bush-blossom.png](../../games/dragon-hold/art-src/props/pine-river/bush-blossom.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model bush-blossom.glb. Cụm hoa nhàu thành khối. |
| K07 | Đá tảng rêu | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/props/pine-river/rock-boulder.png](../../games/dragon-hold/art-src/props/pine-river/rock-boulder.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model rock-boulder.glb. Cụm khối góc cạnh, rêu xanh vàng gần màu Héo: tô lại ôliu sẫm trong Blender. |
| K08 | Gờ đá phiến | Đạt 10 | [games/dragon-hold/art-src/props/pine-river/rock-slab.png](../../games/dragon-hold/art-src/props/pine-river/rock-slab.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model rock-slab.glb. Mặt bên sẫm hơn ảnh, rêu nhạt hơn. |
| K09 | Đá kê suối | Đạt 10 | [games/dragon-hold/art-src/props/pine-river/river-stones.png](../../games/dragon-hold/art-src/props/pine-river/river-stones.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model river-stones.glb. Rêu chân đá ít hơn ảnh. |
| K10 | Gốc thông | Đạt 9,5 | [games/dragon-hold/art-src/props/pine-river/stump.png](../../games/dragon-hold/art-src/props/pine-river/stump.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model stump.glb. Rêu là lá rủ thay đệm tròn. |
| K11 | Khúc gỗ đổ | Đạt 9,5 | [games/dragon-hold/art-src/props/pine-river/log.png](../../games/dragon-hold/art-src/props/pine-river/log.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model log.glb. Đầu sau trơn, tô lại trong Blender nếu lộ. |
| K12 | Cầu gỗ cũ (mốc) | Đạt 10 | [games/dragon-hold/art-src/props/pine-river/bridge-old.png](../../games/dragon-hold/art-src/props/pine-river/bridge-old.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: đã chấm model bridge-old.glb. Không thiếu gì đáng kể. |
| T1 | Cỏ xuân A (chính) | Đạt 9,5 | [games/dragon-hold/art-src/ground/pine-river/grass-a.png](../../games/dragon-hold/art-src/ground/pine-river/grass-a.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: ghép 2×2, 3×3 không thấy nối; khổ 1254, đổi 1024 khi nhập. |
| T2 | Cỏ xuân B (trộn với A) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/ground/pine-river/grass-b.png](../../games/dragon-hold/art-src/ground/pine-river/grass-b.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: lệch lam so với A, thêm hoa tím, hơi rối; chỉnh sắc về gần A bằng công cụ; khổ 1254. |
| T3 | Rêu dưới tán | Tạm chấp nhận 7,5 | [games/dragon-hold/art-src/ground/pine-river/moss.png](../../games/dragon-hold/art-src/ground/pine-river/moss.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: rêu đổ bóng như gò, tối và rối hơn cỏ; khổ 1254. |
| T4 | Lối mòn (đường quái, sáng hơn cỏ một bậc) | Đạt 9 | [games/dragon-hold/art-src/ground/pine-river/path.png](../../games/dragon-hold/art-src/ground/pine-river/path.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: khổ 1254, mép lệch nhẹ, 3×3 lộ sọc chéo: đổi khổ, chạy prepare-ground, trộn decal. |
| T5 | Đất nện (quanh Bệ Rồng, ô xây) | Đạt 9,5 | [games/dragon-hold/art-src/ground/pine-river/earth.png](../../games/dragon-hold/art-src/ground/pine-river/earth.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: mép lệch nhẹ, không thấy nối; khổ 1254, đổi 1024 khi nhập. |
| T6 | Cát ven suối | Đạt 9 | [games/dragon-hold/art-src/ground/pine-river/river-sand.png](../../games/dragon-hold/art-src/ground/pine-river/river-sand.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: khổ 1254; ô sáng nhất bộ, kiểm nhãn chữ cạnh suối. |
| T7 | Đá rêu (dốc > 35°, chiếu ba mặt) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/ground/pine-river/rock.png](../../games/dragon-hold/art-src/ground/pine-river/rock.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: mép phiến có viền tối và chiều dày, không phẳng; khổ 1254. |
| T8 | Lá thông rụng (rìa rừng) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/ground/pine-river/pine-litter.png](../../games/dragon-hold/art-src/ground/pine-river/pine-litter.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. Chấm lại 26/10: kim thông dày, lặp lộ đốm, màu trùng earth; khổ 1254. |
| D1 | Decal vết đất (G) | Đạt 9,5 | [games/dragon-hold/art-src/decals/pine-river/dirt-patches.png](../../games/dragon-hold/art-src/decals/pine-river/dirt-patches.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/dirt-patches-015.png](../../games/dragon-hold/art-src/decals/pine-river/dirt-patches-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. Chấm lại 26/10: dùng dirt-patches.alpha.png (012d); đất hơi đỏ cam, chỉnh màu được. Bản -015 không hơn. |
| D2 | Decal cụm hoa (B) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/decals/pine-river/flower-clusters.png](../../games/dragon-hold/art-src/decals/pine-river/flower-clusters.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/flower-clusters-015.png](../../games/dragon-hold/art-src/decals/pine-river/flower-clusters-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. Chấm lại 26/10: chọn [_review/015-flower-clusters.png](../../games/dragon-hold/art-src/_review/015-flower-clusters.png); cần ghi nguồn, chạy art-normalize, kiểm tím. Trong lúc chờ dùng flower-clusters.alpha.png. |
| D3 | Decal sỏi, lá, kim thông, cành (G) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/decals/pine-river/forest-litter.png](../../games/dragon-hold/art-src/decals/pine-river/forest-litter.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/forest-litter-015.png](../../games/dragon-hold/art-src/decals/pine-river/forest-litter-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. Chấm lại 26/10: dùng forest-litter.alpha.png; sỏi, cành có bóng khối, kim thông mảnh. Bản -015 không hơn. |
| D4 | Decal rêu, vũng nước (M) | Tạm chấp nhận 8 | [games/dragon-hold/art-src/decals/pine-river/moss-puddles.png](../../games/dragon-hold/art-src/decals/pine-river/moss-puddles.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/moss-puddles-015.png](../../games/dragon-hold/art-src/decals/pine-river/moss-puddles-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. Chấm lại 26/10: dùng moss-puddles.v1.alpha.png; rêu nổi khối, hơi vàng lục. Bản -015 kém hơn. |
| B1 | Phông xa rừng thông | Đạt 9 | [games/dragon-hold/art-src/backdrops/pine-river-far.png](../../games/dragon-hold/art-src/backdrops/pine-river-far.png)<br>Ứng viên: [games/dragon-hold/art-src/backdrops/pine-river-far-015.png](../../games/dragon-hold/art-src/backdrops/pine-river-far-015.png) | 006 còn lỗi mép và chi tiết; 015 thử 2 lượt, chưa xác nhận đạt lặp. Chấm lại 26/10: dùng pine-river-far.seamless.png, ghép hai tấm không thấy mép; nửa dưới còn nhiều cây. Không cần cắt lại; bản -015 chưa liền mép. |
| I01 | Gai Chông | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/spikes.png](../../games/dragon-hold/art-src/ui/icons/spikes.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d .256/.64; ở 32 px hàng chông thành chấm. |
| I02 | Bom Hạt Thông | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/pine-bomb.png](../../games/dragon-hold/art-src/ui/icons/pine-bomb.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; ở 32 px mất hạt nhựa. |
| I03 | Lưới Phóng | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/net-launcher.png](../../games/dragon-hold/art-src/ui/icons/net-launcher.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: bản 012d 9,5 (ảnh gốc 8,5); ở 32 px mất mắt lưới. |
| I04 | Vệ Binh Rêu | Đạt 9 | [games/dragon-hold/art-src/ui/icons/moss-warden.png](../../games/dragon-hold/art-src/ui/icons/moss-warden.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; vệt rêu dưới mắt như nước mắt. |
| I05 | Lều Thuốc Nam | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/herb-hut.png](../../games/dragon-hold/art-src/ui/icons/herb-hut.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; ở 32 px mất dấu hiệu thuốc. |
| I06 | Bình Máu Nhỏ | Đạt 10 | [games/dragon-hold/art-src/ui/icons/potion-small.png](../../games/dragon-hold/art-src/ui/icons/potion-small.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; không thiếu gì đáng kể. |
| I07 | Tim Rồng (trang bị) | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/dragon-heart.png](../../games/dragon-hold/art-src/ui/icons/dragon-heart.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; vài mặt cắt đỏ đậm. Ứng viên _review/015 kém hơn. |
| I08 | Vảy Cứng (trang bị) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/ui/icons/hard-scale.png](../../games/dragon-hold/art-src/ui/icons/hard-scale.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; vảy méo, ở 32 px dễ lẫn quả, đỏ hơn Tim Rồng. |
| I09 | Phun Lửa (Alt + 1) | Đạt 9 | [games/dragon-hold/art-src/ui/icons/skill-fire-breath.png](../../games/dragon-hold/art-src/ui/icons/skill-fire-breath.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: chọn _review/015-skill-fire-breath.png (cam đào); chạy art-normalize trước khi dùng. Bản gốc mép đỏ. |
| I10 | Thiên Hỏa (Alt + 2) | Đạt 9 | [games/dragon-hold/art-src/ui/icons/skill-sky-fire.png](../../games/dragon-hold/art-src/ui/icons/skill-sky-fire.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: chọn _review/015-skill-sky-fire.png; chạy art-normalize. Bản gốc mép đỏ. |
| I11 | Long Hống (Từ Khẩn) | Tạm chấp nhận 8,5 | [games/dragon-hold/art-src/ui/icons/skill-roar.png](../../games/dragon-hold/art-src/ui/icons/skill-roar.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: chọn _review/015-skill-roar.png; ở 32 px khó nhận ra rồng; chạy art-normalize. |
| I12 | Long Nộ / Viêm Đế | Đạt 9 | [games/dragon-hold/art-src/ui/icons/skill-ultimate.png](../../games/dragon-hold/art-src/ui/icons/skill-ultimate.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: chọn _review/015-skill-ultimate.png; chạy art-normalize. Bản gốc 8,5. |
| I13 | Vàng | Đạt 10 | [games/dragon-hold/art-src/ui/icons/gold.png](../../games/dragon-hold/art-src/ui/icons/gold.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; không thiếu gì. |
| I14 | Họ Yêu Rêu | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/family-moss.png](../../games/dragon-hold/art-src/ui/icons/family-moss.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; rêu hơi tươi. Ứng viên 015 kém hơn. |
| I15 | Họ Thú Mục | Đạt 9 | [games/dragon-hold/art-src/ui/icons/family-beast.png](../../games/dragon-hold/art-src/ui/icons/family-beast.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; lông hơi tả thực, hơi chìm trên gỗ tối. |
| I16 | Họ Bọ Gai | Đạt 10 | [games/dragon-hold/art-src/ui/icons/family-bug.png](../../games/dragon-hold/art-src/ui/icons/family-bug.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; râu hơi dài. |
| I17 | Huy hiệu tướng địch | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/enemy-general.png](../../games/dragon-hold/art-src/ui/icons/enemy-general.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; khiên xám hơi chìm ở 32 px. |
| I18 | Hào quang tốc (Xung Phong) | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/aura-speed.png](../../games/dragon-hold/art-src/ui/icons/aura-speed.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; dưới 24 px giày nhòe. |
| I19 | Hào quang đòn (Cắm Cờ) | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/aura-attack.png](../../games/dragon-hold/art-src/ui/icons/aura-attack.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; lưỡi kiếm bóng như ngọc. |
| I20 | Gọi sớm (tù và) | Đạt 9,5 | [games/dragon-hold/art-src/ui/icons/call-wave.png](../../games/dragon-hold/art-src/ui/icons/call-wave.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. Chấm lại 26/10: dùng bản 012d; thân sừng hơi chìm trên giấy kem. |

| Hạng mục M0/M0b khác | Trạng thái / cách thực hiện |
|---|---|
| Hỏa Long, Bạch Long; nguồn 3D | Đã có model dùng lại theo DESIGN §9; không yêu cầu ảnh rồng mới. |
| Bệ Rồng | Khối tạm được README M0 §7 cho phép; chưa yêu cầu nguồn riêng. |
| VFX đòn gõ, Phun Lửa, Thiên Hỏa, Long Hống, Long Nộ/Viêm Đế, G01, bẫy, hồi máu | Hình học, hạt, shader và model theo 05 §6; pack M0 không định danh atlas raster mới. M0c duyệt cảm giác. |
| HUD, thẻ chữ, khung học, shop, đặt món, báo đợt, thắng/thua, màn đầu | 20 icon ở trên; khung/chữ/đường nét do UI vẽ. Không yêu cầu tranh tựa riêng ở M0b. |
| Cây billboard thử A/B, 5 prop M2 và vùng sau | Ngoài M0/M0b; không tự mở danh mục. |

## 3. Lời Gọi · P và VS

### 3.1. Nguồn 3D, texture và mẫu P

60 dòng gồm các góc khuyến nghị, texture/mẫu không gửi Tripo và Trại Lính cũ để đối chiếu. Ba mẫu Thư Đồng còn trong kho Space theo README giao nhận, không sinh lại. Draconis ba góc và Trại Lính v2 đã có, dù bảng 3D cũ còn ghi chờ ảnh.

| Nhóm / id | Trạng thái | Đường dẫn thực tế | Ghi chú |
|---|---|---|---|
| helpers/helper-owlet | Đã có | [games/typing-defense/art-src/helpers/helper-owlet.png](../../games/typing-defense/art-src/helpers/helper-owlet.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-owlet-side | Đã có | [games/typing-defense/art-src/helpers/helper-owlet-side.png](../../games/typing-defense/art-src/helpers/helper-owlet-side.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-owlet-back | Đã có | [games/typing-defense/art-src/helpers/helper-owlet-back.png](../../games/typing-defense/art-src/helpers/helper-owlet-back.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-cham-glasses | Đã có | [games/typing-defense/art-src/helpers/helper-cham-glasses.png](../../games/typing-defense/art-src/helpers/helper-cham-glasses.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-cham-scarf | Đã có | [games/typing-defense/art-src/helpers/helper-cham-scarf.png](../../games/typing-defense/art-src/helpers/helper-cham-scarf.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-cham-strap | Đã có | [games/typing-defense/art-src/helpers/helper-cham-strap.png](../../games/typing-defense/art-src/helpers/helper-cham-strap.png) | Texture dây, không gửi Tripo. |
| helpers/helper-phay-tail | Đã có | [games/typing-defense/art-src/helpers/helper-phay-tail.png](../../games/typing-defense/art-src/helpers/helper-phay-tail.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-phay-strap | Đã có | [games/typing-defense/art-src/helpers/helper-phay-strap.png](../../games/typing-defense/art-src/helpers/helper-phay-strap.png) | Texture dây, không gửi Tripo. |
| helpers/helper-gach-wingband | Đã có | [games/typing-defense/art-src/helpers/helper-gach-wingband.png](../../games/typing-defense/art-src/helpers/helper-gach-wingband.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-gach-strap | Đã có | [games/typing-defense/art-src/helpers/helper-gach-strap.png](../../games/typing-defense/art-src/helpers/helper-gach-strap.png) | Texture dây, không gửi Tripo. |
| helpers/helper-brush | Đã có | [games/typing-defense/art-src/helpers/helper-brush.png](../../games/typing-defense/art-src/helpers/helper-brush.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-drum | Đã có | [games/typing-defense/art-src/helpers/helper-drum.png](../../games/typing-defense/art-src/helpers/helper-drum.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-hammer | Đã có | [games/typing-defense/art-src/helpers/helper-hammer.png](../../games/typing-defense/art-src/helpers/helper-hammer.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| helpers/helper-cham-ref | Đã có | [games/space-typing/art-src/td/helpers/helper-cham-ref.png](../../games/space-typing/art-src/td/helpers/helper-cham-ref.png) | Mẫu mặc đủ dùng chung Space theo README-tripo; không gửi Tripo, không sinh lại. |
| helpers/helper-phay-ref | Đã có | [games/space-typing/art-src/td/helpers/helper-phay-ref.png](../../games/space-typing/art-src/td/helpers/helper-phay-ref.png) | Mẫu mặc đủ dùng chung Space theo README-tripo; không gửi Tripo, không sinh lại. |
| helpers/helper-gach-ref | Đã có | [games/space-typing/art-src/td/helpers/helper-gach-ref.png](../../games/space-typing/art-src/td/helpers/helper-gach-ref.png) | Mẫu mặc đủ dùng chung Space theo README-tripo; không gửi Tripo, không sinh lại. |
| heroes/lam | Đã có | [games/typing-defense/art-src/heroes/lam.png](../../games/typing-defense/art-src/heroes/lam.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| heroes/lam-side | Đã có | [games/typing-defense/art-src/heroes/lam-side.png](../../games/typing-defense/art-src/heroes/lam-side.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| heroes/lam-back | Đã có | [games/typing-defense/art-src/heroes/lam-back.png](../../games/typing-defense/art-src/heroes/lam-back.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| heroes/draconis | Đã có | [games/typing-defense/art-src/heroes/draconis.png](../../games/typing-defense/art-src/heroes/draconis.png) | Đã có đủ ba góc. README-tripo ghi model dùng guides/draconis-v4; không sinh trùng. |
| heroes/draconis-side | Đã có | [games/typing-defense/art-src/heroes/draconis-side.png](../../games/typing-defense/art-src/heroes/draconis-side.png) | Đã có đủ ba góc. README-tripo ghi model dùng guides/draconis-v4; không sinh trùng. |
| heroes/draconis-back | Đã có | [games/typing-defense/art-src/heroes/draconis-back.png](../../games/typing-defense/art-src/heroes/draconis-back.png) | Đã có đủ ba góc. README-tripo ghi model dùng guides/draconis-v4; không sinh trùng. |
| units/linh-giao | Đã có | [games/typing-defense/art-src/units/linh-giao.png](../../games/typing-defense/art-src/units/linh-giao.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| units/linh-giao-spear | Đã có | [games/typing-defense/art-src/units/linh-giao-spear.png](../../games/typing-defense/art-src/units/linh-giao-spear.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/cuong-thi | Đã có | [games/typing-defense/art-src/enemies/cuong-thi.png](../../games/typing-defense/art-src/enemies/cuong-thi.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/cuong-thi-lead-hat | Đã có | [games/typing-defense/art-src/enemies/cuong-thi-lead-hat.png](../../games/typing-defense/art-src/enemies/cuong-thi-lead-hat.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/nuppeppo | Đã có | [games/typing-defense/art-src/enemies/nuppeppo.png](../../games/typing-defense/art-src/enemies/nuppeppo.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/thuong-luong | Đã có | [games/typing-defense/art-src/enemies/thuong-luong.png](../../games/typing-defense/art-src/enemies/thuong-luong.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/thuong-luong-front | Đã có | [games/typing-defense/art-src/enemies/thuong-luong-front.png](../../games/typing-defense/art-src/enemies/thuong-luong-front.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/tanuki | Đã có | [games/typing-defense/art-src/enemies/tanuki.png](../../games/typing-defense/art-src/enemies/tanuki.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/troll | Đã có | [games/typing-defense/art-src/enemies/troll.png](../../games/typing-defense/art-src/enemies/troll.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/troll-back | Đã có | [games/typing-defense/art-src/enemies/troll-back.png](../../games/typing-defense/art-src/enemies/troll-back.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/alicanto | Đã có | [games/typing-defense/art-src/enemies/alicanto.png](../../games/typing-defense/art-src/enemies/alicanto.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/alicanto-front | Đã có | [games/typing-defense/art-src/enemies/alicanto-front.png](../../games/typing-defense/art-src/enemies/alicanto-front.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| enemies/mam-go | Đã có | [games/typing-defense/art-src/enemies/mam-go.png](../../games/typing-defense/art-src/enemies/mam-go.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| bosses/moc-tinh | Đã có | [games/typing-defense/art-src/bosses/moc-tinh.png](../../games/typing-defense/art-src/bosses/moc-tinh.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| bosses/moc-tinh-side | Đã có | [games/typing-defense/art-src/bosses/moc-tinh-side.png](../../games/typing-defense/art-src/bosses/moc-tinh-side.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| bosses/moc-tinh-back | Đã có | [games/typing-defense/art-src/bosses/moc-tinh-back.png](../../games/typing-defense/art-src/bosses/moc-tinh-back.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/keep | Đã có | [games/typing-defense/art-src/buildings/keep.png](../../games/typing-defense/art-src/buildings/keep.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/archer | Đã có | [games/typing-defense/art-src/buildings/archer.png](../../games/typing-defense/art-src/buildings/archer.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/cannon | Đã có | [games/typing-defense/art-src/buildings/cannon.png](../../games/typing-defense/art-src/buildings/cannon.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/cannon-barrel | Đã có | [games/typing-defense/art-src/buildings/cannon-barrel.png](../../games/typing-defense/art-src/buildings/cannon-barrel.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/barracks | Đã có | [games/typing-defense/art-src/buildings/barracks.png](../../games/typing-defense/art-src/buildings/barracks.png) | Bản cũ thấp 1,8 m, giữ đối chiếu; thay bằng barracks-v2. Chấm lại 26/10: không chấm riêng; model art-src barracks.glb đã dựng lại từ barracks-v2 (dòng dưới). SOURCES.json còn ghi nhầm ảnh này; public/ vẫn model cũ 1,8 m. |
| buildings/barracks-v2 | Đạt 9,5 | [games/typing-defense/art-src/buildings/barracks-v2.png](../../games/typing-defense/art-src/buildings/barracks-v2.png) | Đã có ảnh làm lại; bảng 3D trước 015 còn ghi chờ ảnh là thông tin cũ. Chấm lại 26/10: đã chấm model barracks.glb (art-src, dựng từ ảnh này), hợp bộ archer.glb. Còn: sửa SOURCES.json, xoay mặt trước, đặt cao ~4,5 m, xuất lại medium/high thay model cũ ở public/. Không cần credit Tripo. |
| buildings/gold-mine | Đã có | [games/typing-defense/art-src/buildings/gold-mine.png](../../games/typing-defense/art-src/buildings/gold-mine.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/farm | Đã có | [games/typing-defense/art-src/buildings/farm.png](../../games/typing-defense/art-src/buildings/farm.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| buildings/seal-dais | Đã có | [games/typing-defense/art-src/buildings/seal-dais.png](../../games/typing-defense/art-src/buildings/seal-dais.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/gold-mine-cart | Đã có | [games/typing-defense/art-src/props/gold-mine-cart.png](../../games/typing-defense/art-src/props/gold-mine-cart.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/level-pennant | Đã có | [games/typing-defense/art-src/props/level-pennant.png](../../games/typing-defense/art-src/props/level-pennant.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/gold-pile-1 | Đã có | [games/typing-defense/art-src/props/gold-pile-1.png](../../games/typing-defense/art-src/props/gold-pile-1.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/gold-pile-2 | Đã có | [games/typing-defense/art-src/props/gold-pile-2.png](../../games/typing-defense/art-src/props/gold-pile-2.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/gold-pile-3 | Đã có | [games/typing-defense/art-src/props/gold-pile-3.png](../../games/typing-defense/art-src/props/gold-pile-3.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| props/gold-pile-4 | Đã có | [games/typing-defense/art-src/props/gold-pile-4.png](../../games/typing-defense/art-src/props/gold-pile-4.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| projectiles/arrow | Đã có | [games/typing-defense/art-src/projectiles/arrow.png](../../games/typing-defense/art-src/projectiles/arrow.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| projectiles/shell | Đã có | [games/typing-defense/art-src/projectiles/shell.png](../../games/typing-defense/art-src/projectiles/shell.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| projectiles/keep-bolt | Đã có | [games/typing-defense/art-src/projectiles/keep-bolt.png](../../games/typing-defense/art-src/projectiles/keep-bolt.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| projectiles/root-burst | Đã có | [games/typing-defense/art-src/projectiles/root-burst.png](../../games/typing-defense/art-src/projectiles/root-burst.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| loot/bag-cloth | Đã có | [games/typing-defense/art-src/loot/bag-cloth.png](../../games/typing-defense/art-src/loot/bag-cloth.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| loot/bag-basket | Đã có | [games/typing-defense/art-src/loot/bag-basket.png](../../games/typing-defense/art-src/loot/bag-basket.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |
| loot/chest-boss | Đã có | [games/typing-defense/art-src/loot/chest-boss.png](../../games/typing-defense/art-src/loot/chest-boss.png) | Nguồn 3D; có file không thay duyệt mỹ thuật. |

### 3.2. Nguồn 3D VS · 005a/005b2 đã bàn giao, bỏ qua

| Mã | Trạng thái | Đường dẫn | Bàn giao / giới hạn |
|---|---|---|---|
| K04 | Đạt 9,5 | [games/typing-defense/art-src/workers/worker-kit-en-bow.png](../../games/typing-defense/art-src/workers/worker-kit-en-bow.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. Chấm lại 26/10: dây cung hơi mảnh; tách nền, cắt khung trước Tripo. |
| K10 | Đạt 9 | [games/typing-defense/art-src/workers/worker-kit-lua-shot.png](../../games/typing-defense/art-src/workers/worker-kit-lua-shot.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. Chấm lại 26/10: mặt sắt hơi thật; tách nền trước Tripo. |
| K13 | Đạt 9,5 | [games/typing-defense/art-src/workers/worker-kit-sam-drumstick.png](../../games/typing-defense/art-src/workers/worker-kit-sam-drumstick.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. Chấm lại 26/10: vân gỗ hơi chi tiết; tách nền, cắt khung trước Tripo. |
| VS2 | Đã có | [games/typing-defense/art-src/animals/chuon-chuon-tre.png](../../games/typing-defense/art-src/animals/chuon-chuon-tre.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS14a | Đã có | [games/typing-defense/art-src/helpers/helper-book.png](../../games/typing-defense/art-src/helpers/helper-book.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS1b | Đã có | [games/typing-defense/art-src/heroes/tre-mallet.png](../../games/typing-defense/art-src/heroes/tre-mallet.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS1c | Đã có | [games/typing-defense/art-src/heroes/tre-slingshot.png](../../games/typing-defense/art-src/heroes/tre-slingshot.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS3b | Đã có | [games/typing-defense/art-src/units/linh-khien-shield.png](../../games/typing-defense/art-src/units/linh-khien-shield.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS4b | Đã có | [games/typing-defense/art-src/units/linh-giao-dai-spear.png](../../games/typing-defense/art-src/units/linh-giao-dai-spear.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS6b | Đã có | [games/typing-defense/art-src/enemies/oni-club.png](../../games/typing-defense/art-src/enemies/oni-club.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS9b | Đã có | [games/typing-defense/art-src/enemies/dokkaebi-club.png](../../games/typing-defense/art-src/enemies/dokkaebi-club.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS14b | Đã có | [games/typing-defense/art-src/helpers/helper-fan.png](../../games/typing-defense/art-src/helpers/helper-fan.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K01 | Đã có | [games/typing-defense/art-src/workers/worker-kit-gatekeeper-head.png](../../games/typing-defense/art-src/workers/worker-kit-gatekeeper-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K02 | Đã có | [games/typing-defense/art-src/workers/worker-kit-gatekeeper-crossbow.png](../../games/typing-defense/art-src/workers/worker-kit-gatekeeper-crossbow.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K03 | Đã có | [games/typing-defense/art-src/workers/worker-kit-en-head.png](../../games/typing-defense/art-src/workers/worker-kit-en-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K05 | Đã có | [games/typing-defense/art-src/workers/worker-kit-se-head.png](../../games/typing-defense/art-src/workers/worker-kit-se-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K06 | Đã có | [games/typing-defense/art-src/workers/worker-kit-se-quiver.png](../../games/typing-defense/art-src/workers/worker-kit-se-quiver.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K07 | Đã có | [games/typing-defense/art-src/workers/worker-kit-dong-head.png](../../games/typing-defense/art-src/workers/worker-kit-dong-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K08 | Đã có | [games/typing-defense/art-src/workers/worker-kit-dong-rammer.png](../../games/typing-defense/art-src/workers/worker-kit-dong-rammer.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K09 | Đã có | [games/typing-defense/art-src/workers/worker-kit-lua-head.png](../../games/typing-defense/art-src/workers/worker-kit-lua-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K11 | Đã có | [games/typing-defense/art-src/workers/worker-kit-scholar-head.png](../../games/typing-defense/art-src/workers/worker-kit-scholar-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K12 | Đã có | [games/typing-defense/art-src/workers/worker-kit-sam-head.png](../../games/typing-defense/art-src/workers/worker-kit-sam-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K14 | Đã có | [games/typing-defense/art-src/workers/worker-kit-miner-head.png](../../games/typing-defense/art-src/workers/worker-kit-miner-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K15 | Đã có | [games/typing-defense/art-src/workers/worker-kit-miner-pickaxe.png](../../games/typing-defense/art-src/workers/worker-kit-miner-pickaxe.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K16 | Đã có | [games/typing-defense/art-src/workers/worker-kit-ma-head.png](../../games/typing-defense/art-src/workers/worker-kit-ma-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K17 | Đã có | [games/typing-defense/art-src/workers/worker-kit-ma-seedlings.png](../../games/typing-defense/art-src/workers/worker-kit-ma-seedlings.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K18 | Đã có | [games/typing-defense/art-src/workers/worker-kit-tieu-head.png](../../games/typing-defense/art-src/workers/worker-kit-tieu-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K19 | Đã có | [games/typing-defense/art-src/workers/worker-kit-tieu-axe.png](../../games/typing-defense/art-src/workers/worker-kit-tieu-axe.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K20 | Đã có | [games/typing-defense/art-src/workers/worker-kit-tro-head.png](../../games/typing-defense/art-src/workers/worker-kit-tro-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K21 | Đã có | [games/typing-defense/art-src/workers/worker-kit-tro-scroll.png](../../games/typing-defense/art-src/workers/worker-kit-tro-scroll.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K22 | Đã có | [games/typing-defense/art-src/workers/worker-kit-lang-head.png](../../games/typing-defense/art-src/workers/worker-kit-lang-head.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K23 | Đã có | [games/typing-defense/art-src/workers/worker-kit-lang-basket.png](../../games/typing-defense/art-src/workers/worker-kit-lang-basket.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| K24 | Đã có | [games/typing-defense/art-src/workers/worker-kit-sam-vest.png](../../games/typing-defense/art-src/workers/worker-kit-sam-vest.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS3a | Đã có | [games/typing-defense/art-src/units/linh-khien.png](../../games/typing-defense/art-src/units/linh-khien.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS4a | Đã có | [games/typing-defense/art-src/units/linh-giao-dai.png](../../games/typing-defense/art-src/units/linh-giao-dai.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS5a | Đã có | [games/typing-defense/art-src/workers/worker-base.png](../../games/typing-defense/art-src/workers/worker-base.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS7 | Đã có | [games/typing-defense/art-src/enemies/tat-phuong.png](../../games/typing-defense/art-src/enemies/tat-phuong.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS8 | Đã có | [games/typing-defense/art-src/enemies/ma-da.png](../../games/typing-defense/art-src/enemies/ma-da.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS9a | Đã có | [games/typing-defense/art-src/enemies/dokkaebi.png](../../games/typing-defense/art-src/enemies/dokkaebi.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS10 | Đã có | [games/typing-defense/art-src/enemies/kamaitachi.png](../../games/typing-defense/art-src/enemies/kamaitachi.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS12 | Đã có | [games/typing-defense/art-src/animals/trau.png](../../games/typing-defense/art-src/animals/trau.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS12 | Đã có | [games/typing-defense/art-src/animals/trau-front.png](../../games/typing-defense/art-src/animals/trau-front.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS13 | Đã có | [games/typing-defense/art-src/animals/piggy.png](../../games/typing-defense/art-src/animals/piggy.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS6a | Đã có | [games/typing-defense/art-src/enemies/oni.png](../../games/typing-defense/art-src/enemies/oni.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS1a | Đã có | [games/typing-defense/art-src/heroes/tre.png](../../games/typing-defense/art-src/heroes/tre.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS1a | Đã có | [games/typing-defense/art-src/heroes/tre-side.png](../../games/typing-defense/art-src/heroes/tre-side.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS1a | Đã có | [games/typing-defense/art-src/heroes/tre-back.png](../../games/typing-defense/art-src/heroes/tre-back.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS11 | Đã có | [games/typing-defense/art-src/bosses/dai-bang-tinh.png](../../games/typing-defense/art-src/bosses/dai-bang-tinh.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| VS11 | Đã có | [games/typing-defense/art-src/bosses/dai-bang-tinh-front.png](../../games/typing-defense/art-src/bosses/dai-bang-tinh-front.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V1 | Đã có | [games/typing-defense/art-src/buildings/scribe.png](../../games/typing-defense/art-src/buildings/scribe.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V2 | Đã có | [games/typing-defense/art-src/buildings/infirmary.png](../../games/typing-defense/art-src/buildings/infirmary.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V3 | Đã có | [games/typing-defense/art-src/buildings/lumber.png](../../games/typing-defense/art-src/buildings/lumber.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V4 | Đã có | [games/typing-defense/art-src/buildings/farm-ao-ca.png](../../games/typing-defense/art-src/buildings/farm-ao-ca.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V5 | Đã có | [games/typing-defense/art-src/buildings/farm-nuong.png](../../games/typing-defense/art-src/buildings/farm-nuong.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V6 | Đã có | [games/typing-defense/art-src/kits/keep-kit-l2.png](../../games/typing-defense/art-src/kits/keep-kit-l2.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V7 | Đã có | [games/typing-defense/art-src/kits/keep-kit-l3.png](../../games/typing-defense/art-src/kits/keep-kit-l3.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V8 | Đã có | [games/typing-defense/art-src/kits/keep-kit-l4.png](../../games/typing-defense/art-src/kits/keep-kit-l4.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V9 | Đã có | [games/typing-defense/art-src/kits/archer-kit-l2.png](../../games/typing-defense/art-src/kits/archer-kit-l2.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V10 | Đã có | [games/typing-defense/art-src/kits/archer-kit-l3.png](../../games/typing-defense/art-src/kits/archer-kit-l3.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V11 | Đã có | [games/typing-defense/art-src/kits/cannon-kit-l2.png](../../games/typing-defense/art-src/kits/cannon-kit-l2.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V12 | Đã có | [games/typing-defense/art-src/kits/cannon-kit-l3.png](../../games/typing-defense/art-src/kits/cannon-kit-l3.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V13 | Đã có | [games/typing-defense/art-src/kits/cannon-barrel-l3.png](../../games/typing-defense/art-src/kits/cannon-barrel-l3.png) | 005a/005b2 đã làm, 015 bỏ qua. Giữ nguyên; chưa duyệt lại hình trong 015. |
| V14 | Tạm chấp nhận 8 | [games/typing-defense/art-src/kits/barracks-kit-l2.png](../../games/typing-defense/art-src/kits/barracks-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10 (P2): chòi canh đúng phiếu, dựng Tripo được; nhưng sân sau phải không còn ở barracks-v2/glb, chòi lặp vai sàn canh và chìm ở cỡ game. Gửi ảnh hiện có, thu nhỏ, đặt vào dải sân phải trong Blender. |
| V15 | Tạm chấp nhận 8 | [games/typing-defense/art-src/kits/barracks-kit-l3.png](../../games/typing-defense/art-src/kits/barracks-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10 (P2, có người thứ ba): đủ mái ngói, chóp đai đồng, hai cờ đỏ; mái vẽ theo nhà dài cũ. Gửi ảnh hiện có, chỉnh tỉ lệ từng trục trong Blender cho chụp kín mái rơm barracks.glb. |
| V16 | Có nhưng lỗi | [games/typing-defense/art-src/kits/gold-mine-kit-l2.png](../../games/typing-defense/art-src/kits/gold-mine-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V17 | Có nhưng lỗi | [games/typing-defense/art-src/kits/gold-mine-kit-l3.png](../../games/typing-defense/art-src/kits/gold-mine-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V18 | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/kits/farm-kit-l2.png](../../games/typing-defense/art-src/kits/farm-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: viền cỏ xanh trên nền #00FF00 (khóa màu fuzz 25–30 % giữ được cỏ); giá gỗ thay tre. |
| V19 | Có nhưng lỗi | [games/typing-defense/art-src/kits/farm-kit-l3.png](../../games/typing-defense/art-src/kits/farm-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V20 | Có nhưng lỗi | [games/typing-defense/art-src/kits/seal-dais-kit-l2.png](../../games/typing-defense/art-src/kits/seal-dais-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V21 | Có nhưng lỗi | [games/typing-defense/art-src/kits/seal-dais-kit-l3.png](../../games/typing-defense/art-src/kits/seal-dais-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V22 | Có nhưng lỗi | [games/typing-defense/art-src/kits/scribe-kit-l2.png](../../games/typing-defense/art-src/kits/scribe-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V23 | Đạt 9,5 | [games/typing-defense/art-src/kits/scribe-kit-l3.png](../../games/typing-defense/art-src/kits/scribe-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: nền đã phẳng; cắt khung trước Tripo. |
| V24 | Có nhưng lỗi | [games/typing-defense/art-src/kits/infirmary-kit-l2.png](../../games/typing-defense/art-src/kits/infirmary-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V25 | Có nhưng lỗi | [games/typing-defense/art-src/kits/infirmary-kit-l3.png](../../games/typing-defense/art-src/kits/infirmary-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V26 | Có nhưng lỗi | [games/typing-defense/art-src/kits/lumber-kit-l2.png](../../games/typing-defense/art-src/kits/lumber-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V27 | Có nhưng lỗi | [games/typing-defense/art-src/kits/lumber-kit-l3.png](../../games/typing-defense/art-src/kits/lumber-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V28 | Có nhưng lỗi | [games/typing-defense/art-src/branches/archer-en-bao.png](../../games/typing-defense/art-src/branches/archer-en-bao.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V29 | Có nhưng lỗi | [games/typing-defense/art-src/branches/archer-than-tien.png](../../games/typing-defense/art-src/branches/archer-than-tien.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V30 | Có nhưng lỗi | [games/typing-defense/art-src/branches/cannon-coi-lon.png](../../games/typing-defense/art-src/branches/cannon-coi-lon.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V31 | Có nhưng lỗi | [games/typing-defense/art-src/branches/cannon-vac-lua.png](../../games/typing-defense/art-src/branches/cannon-vac-lua.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V32 | Đạt 9 | [games/typing-defense/art-src/branches/scribe-but-loi.png](../../games/typing-defense/art-src/branches/scribe-but-loi.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: cọ nghiêng 45°, vẫn đọc như cột thu lôi; tách nền trước Tripo. |
| V33 | Đạt 9 | [games/typing-defense/art-src/branches/scribe-muc-bang.png](../../games/typing-defense/art-src/branches/scribe-muc-bang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: thêm nhũ băng mái dưới, xóa trong Blender nếu cần. |
| V34 | Tạm chấp nhận 8 (vẽ lại 27/10, 015c; bản cũ 6,5) | [games/typing-defense/art-src/branches/barracks-khien-dong.png](../../games/typing-defense/art-src/branches/barracks-khien-dong.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10 (P2, có người thứ ba): vẽ đẹp, đủ phần lớn nét nhánh, nhưng theo nhà dài thấp cũ: cùng bề ngang chân chỉ cao khoảng nửa tháp barracks-v2/glb; luật 02 §8 cấm kéo dãn Z, nên không ghép được. Không gửi Tripo; vẽ lại 2D một lần theo barracks-v2.png (ART_FIX_QUEUE §3); giữ ảnh làm mẫu chi tiết và bản dự phòng. |
| V35 | Tạo lại (luật 2D từ 8, 27/10; bản 015c 7,5, bản cũ 5,5; Codex 020) | [games/typing-defense/art-src/branches/barracks-giao-dai.png](../../games/typing-defense/art-src/branches/barracks-giao-dai.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10 (P2, có người thứ ba): cùng lỗi gốc như V34 (nhà dài thấp, cao khoảng nửa tháp v2); thiếu rào cọc cao, giáo rời và dây mảnh, ở cỡ game gần như nhà cũ. Không gửi Tripo; vẽ lại 2D một lần theo barracks-v2.png (ART_FIX_QUEUE §3); giữ ảnh làm mẫu bố cục và bản dự phòng. |
| V36 | Tạm chấp nhận 8 | [games/typing-defense/art-src/branches/gold-mine-ham-sau.png](../../games/typing-defense/art-src/branches/gold-mine-ham-sau.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: thiếu miệng giếng; dáng gần Mỏ Vàng gốc ở 150 px. |
| V37 | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: miệng lò phát sáng: tô lại màu than trước khi dùng; mất cửa hầm và ray. |
| V38 | Có nhưng lỗi | [games/typing-defense/art-src/branches/farm-bac-thang.png](../../games/typing-defense/art-src/branches/farm-bac-thang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V39 | Có nhưng lỗi | [games/typing-defense/art-src/branches/farm-chuong-trau.png](../../games/typing-defense/art-src/branches/farm-chuong-trau.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V40 | Có nhưng lỗi | [games/typing-defense/art-src/branches/lumber-xuong-cua.png](../../games/typing-defense/art-src/branches/lumber-xuong-cua.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V41 | Có nhưng lỗi | [games/typing-defense/art-src/branches/lumber-xuong-rao.png](../../games/typing-defense/art-src/branches/lumber-xuong-rao.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V42 | Đạt 9 | [games/typing-defense/art-src/branches/seal-dais-phong-an.png](../../games/typing-defense/art-src/branches/seal-dais-phong-an.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: chưa có móc sắt, đặt socket FX_lantern ở đầu cột khi dựng. |
| V43 | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/branches/seal-dais-vang-am.png](../../games/typing-defense/art-src/branches/seal-dais-vang-am.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: bốn cột thay năm, không móc đèn: đặt đèn thứ năm trên cột khung đàn khi dựng. |
| V44 | Đạt 9 | [games/typing-defense/art-src/branches/infirmary-vuon-thao-duoc.png](../../games/typing-defense/art-src/branches/infirmary-vuon-thao-duoc.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: cụm lá tím sẫm giữ được khi tách nền; làm phẳng nền trước Tripo. |
| V45 | Có nhưng lỗi | [games/typing-defense/art-src/branches/infirmary-tram-cuu-thuong.png](../../games/typing-defense/art-src/branches/infirmary-tram-cuu-thuong.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V46 | Có nhưng lỗi | [games/typing-defense/art-src/ruins/ruin-s.png](../../games/typing-defense/art-src/ruins/ruin-s.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V47 | Có nhưng lỗi | [games/typing-defense/art-src/ruins/ruin-m.png](../../games/typing-defense/art-src/ruins/ruin-m.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V48 | Có nhưng lỗi | [games/typing-defense/art-src/ruins/ruin-l.png](../../games/typing-defense/art-src/ruins/ruin-l.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V49 | Có nhưng lỗi | [games/typing-defense/art-src/ruins/ruin-xl.png](../../games/typing-defense/art-src/ruins/ruin-xl.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V50 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/vach-thac-bac.png](../../games/typing-defense/art-src/landmarks/vach-thac-bac.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V51 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/cau-go.png](../../games/typing-defense/art-src/landmarks/cau-go.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V52 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/choi-canh-doi.png](../../games/typing-defense/art-src/landmarks/choi-canh-doi.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V53 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/hai-dang.png](../../games/typing-defense/art-src/landmarks/hai-dang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V54 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/cau-tau.png](../../games/typing-defense/art-src/landmarks/cau-tau.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V55 | Đạt 9,5 | [games/typing-defense/art-src/landmarks/nha-rai-da.png](../../games/typing-defense/art-src/landmarks/nha-rai-da.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. Chấm lại 26/10: chọn review-vs-buildings/nha-rai-da-attempt1.png (lưới thành khối); đệm vuông, đưa về 1024. Bản này khoảng 9. |
| V56 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/them-da-trang.png](../../games/typing-defense/art-src/landmarks/them-da-trang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V57 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/goc-da-rong.png](../../games/typing-defense/art-src/landmarks/goc-da-rong.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V58 | Đạt 9,5 | [games/typing-defense/art-src/landmarks/cau-do.png](../../games/typing-defense/art-src/landmarks/cau-do.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: thêm lớp đá viền vòm, hợp kết cấu; nền nhiễu nhẹ. |
| V59 | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/landmarks/da-ke.png](../../games/typing-defense/art-src/landmarks/da-ke.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: đá đầu cao như trụ, khe hẹp; hạ độ cao trong Blender được. |
| V60 | Đạt 9,5 | [games/typing-defense/art-src/landmarks/re-vom.png](../../games/typing-defense/art-src/landmarks/re-vom.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: khối liền; chỉnh nhịp vòm theo đường khi dựng. |
| V61 | Đạt 9,5 | [games/typing-defense/art-src/landmarks/thac-ho-sut.png](../../games/typing-defense/art-src/landmarks/thac-ho-sut.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: rãnh đá có vệt bóng, giữ đá mờ khi tô. |
| V62 | Có nhưng lỗi | [games/typing-defense/art-src/props/scaffold-bamboo.png](../../games/typing-defense/art-src/props/scaffold-bamboo.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V63 | Có nhưng lỗi | [games/typing-defense/art-src/props/rao-tre.png](../../games/typing-defense/art-src/props/rao-tre.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V64 | Có nhưng lỗi | [games/typing-defense/art-src/props/cau-tre.png](../../games/typing-defense/art-src/props/cau-tre.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V65 | Có nhưng lỗi | [games/typing-defense/art-src/props/go-lan.png](../../games/typing-defense/art-src/props/go-lan.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V66 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/pebble.png](../../games/typing-defense/art-src/projectiles/pebble.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V67 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/meteor.png](../../games/typing-defense/art-src/projectiles/meteor.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V68 | Đạt 9 | [games/typing-defense/art-src/projectiles/quill.png](../../games/typing-defense/art-src/projectiles/quill.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: đầu nhọn như phi tiêu; tô đai cùng màu ống lông. |
| V69 | Tạm chấp nhận 8 | [games/typing-defense/art-src/projectiles/seed-drop.png](../../games/typing-defense/art-src/projectiles/seed-drop.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Chấm lại 26/10: múi sâu, giống bí ngô hơn quả đa. |
| V70 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/fire-feather.png](../../games/typing-defense/art-src/projectiles/fire-feather.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |

### 3.3. Ảnh dùng thẳng P

83 ảnh = 26 cảnh/decal + 6 phông + 8 chân dung + 3 đèn lồng + 28 icon + 12 VFX. X12 là tham khảo tùy chọn. Trước 015 có 14/83 (3 chân dung, 11 VFX); màn tựa tính riêng. Prompt có sẵn chưa được tính là ảnh.

| Mã | Nội dung | Trạng thái | Đích / ảnh | Ghi chú |
|---|---|---|---|---|
| S1-v1 | Cây bàng · cây to, tán xếp tầng ngang | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/almond-tree-v1.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: viền mực đúng lối cảnh; nền dao động nhẹ, art-normalize tách được. |
| S1-v2 | Cây bàng · cây to, tán xếp tầng ngang | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/almond-tree-v2.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: gốc lệch phải ~120 px, neo ở gốc; nền tách được. |
| S2-v1 | Thông núi · cây cao, tán thành đệm tròn | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v1.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: thân cam đỏ hơi gắt; chỉ còn khóa nền. |
| S2-v2 | Thông núi · cây cao, tán thành đệm tròn | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v2.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: vòng quấn chỗ nhánh trái, tán sáng hơn v1; gốc lệch ~76 px. |
| S3-v1 | Khóm tre · bụi tre làng, ngọn cong | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: thân thẳng, lá thành quả cầu như cây cọ, vàng chanh gắt. |
| S3-v2 | Khóm tre · bụi tre làng, ngọn cong | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: dùng bản đầu bamboo-clump-v2.v1.png (thân cong rõ); bản cuối 8,5. |
| S4-v1 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v1.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lá nhiều chi tiết, rối ở 60 px. |
| S4-v2 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v2.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lá răng cưa nhiều gân, hơi rối. |
| S5-v1 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/tall-grass-v1.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lá mảnh, chìm vào nền cỏ. |
| S5-v2 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/tall-grass-v2.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: hơi chìm trên cỏ, viền tím mảnh; khóa màu khi nhập. |
| S6-v1 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/reed-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: vệt tím mờ trong khe lá, tràn màu viền bông: tẩy khi chạy prepare-scenery. |
| S6-v2 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: lá xanh vàng lệch v1, vệt tím trong khe lá; kéo màu về v1. |
| S7-v1 | Hoa dại trắng vàng · khóm hoa thấp | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/wildflowers-v1.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: khổ ngang, cắt sát là xong. |
| S7-v2 | Hoa dại trắng vàng · khóm hoa thấp | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/wildflowers-v2.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: vài nụ hồng cam rất nhỏ, ở cỡ game không thấy. |
| S8-v1 | Dương xỉ · khóm lá xòe bờ ẩm | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/fern-v1.png](../../games/typing-defense/art-src/scenery/meadow/fern-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lá dưới rủ thấp hơn gốc, neo mép dưới vẫn ổn. |
| S8-v2 | Dương xỉ · khóm lá xòe bờ ẩm | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/fern-v2.png](../../games/typing-defense/art-src/scenery/meadow/fern-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lá sát mép, vẫn đủ cắt sát. |
| S9-v1 | Đá xám rêu nhỏ | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/rock-small-v1.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: chỉ còn tách nền, cắt sát. |
| S9-v2 | Đá xám rêu nhỏ | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/rock-small-v2.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: chỉ còn tách nền, cắt sát. |
| S10-v1 | Đá xám rêu vừa · tảng đá to | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/rock-medium-v1.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lề nhỏ, viền hồng mảnh khi khóa thô; khóa nền bằng art-normalize. |
| S10-v2 | Đá xám rêu vừa · tảng đá to | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/rock-medium-v2.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lề trên, dưới hẹp; khóa nền khi nhập. |
| S11-v1 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Đạt 9,5 | [games/typing-defense/art-src/scenery/meadow/rotten-log-v1.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: lề phải hẹp; khóa nền khi nhập. |
| S11-v2 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Đạt 9 | [games/typing-defense/art-src/scenery/meadow/rotten-log-v2.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: gần bản sao v1, lật ngang khi đặt gần nhau. |
| S12-v1 | Khối tán · bức tường tán cây ở mép rừng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/canopy-block-v1.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. Chấm lại 26/10: xanh chanh quá bão hòa, vân lá đều, lệch bộ; chỉnh màu đỡ được. |
| S12-v2 | Khối tán · bức tường tán cây ở mép rừng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: cùng lỗi màu với v1. |
| S13-v1 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/shared/tree-stump-v1.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v1.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: hơi nghiêng, đầu rễ là mặt cưa; vật chiếm 95 % khung. |
| S13-v2 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/scenery/shared/tree-stump-v2.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v2.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: hơi nghiêng, đầu rễ là mặt cưa; khổ 1254. |
| F1 | Dải trời có cầu vồng | Đạt 10 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: cầu vồng hơi rực; hai mép khớp. |
| F2 | Dải trời mây sáng | Đạt 9,5 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: mây vụn không viền mực, bố cục giống sky-a. |
| F3 | Núi xa lam nhạt | Đạt 10 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: đường núi chạm mép ở 58,4 %. Bản .v1 sai lớp. |
| F4 | Đồi rừng xanh lam, vách đá vôi | Đạt 9,5 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: đường núi chạm mép ở 50 %, dời bằng công cụ. |
| F5 | Đồi chè có cối xay gió | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: hơi rối (hồ, đảo đá vôi), khung cánh lẫn hồng: khử loang bằng art-normalize. |
| F6 | Đồi chè trơn | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: gần chép ô a nên lặp rõ; khóm tre viền hồng. |
| C1 | Draconis, Tướng ô 1 (dáng ảnh 3.png, LOOK-DRACONIS) | Đã có | [games/typing-defense/art-src/portraits/draconis.png](../../games/typing-defense/art-src/portraits/draconis.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| C2 | Thư Đồng Chấm · vui | Đã có | [games/typing-defense/art-src/portraits/helper-cham-happy.png](../../games/typing-defense/art-src/portraits/helper-cham-happy.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| C3 | Thư Đồng Chấm · hoảng | Đạt 9,5 | [games/typing-defense/art-src/portraits/helper-cham-scared.png](../../games/typing-defense/art-src/portraits/helper-cham-scared.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: khổ 1254, cánh sát mép; khử loang xanh ở tròng kính. Không dùng .v1. |
| C4 | Thư Đồng Phẩy · vui | Đạt 9,5 | [games/typing-defense/art-src/portraits/helper-phay-happy.png](../../games/typing-defense/art-src/portraits/helper-phay-happy.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: chỉ cần đổi khổ 1024. |
| C5 | Thư Đồng Phẩy · hoảng | Đạt 9,5 | [games/typing-defense/art-src/portraits/helper-phay-scared.png](../../games/typing-defense/art-src/portraits/helper-phay-scared.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: nước mắt mất ở 64 px, vẻ hoảng vẫn rõ; đổi khổ. |
| C6 | Thư Đồng Gạch · vui | Đạt 9,5 | [games/typing-defense/art-src/portraits/helper-gach-happy.png](../../games/typing-defense/art-src/portraits/helper-gach-happy.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: dùng bản .png (lần 2); đổi khổ. Bản .v1 8 điểm. |
| C7 | Thư Đồng Gạch · hoảng | Đạt 9,5 | [games/typing-defense/art-src/portraits/helper-gach-scared.png](../../games/typing-defense/art-src/portraits/helper-gach-scared.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: có vạch rung, dấu giật mình, không phải chữ; đổi khổ. |
| C8 | Bà Cú Mực, người kể | Đã có | [games/typing-defense/art-src/portraits/narrator.png](../../games/typing-defense/art-src/portraits/narrator.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| L1 | Tắt | Đạt 9 | [games/typing-defense/art-src/ui/lanterns/lantern-unlit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-unlit.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: giấy kem sáng, lòng không tối, vẫn khác L2, L3 ở 32 px; đổi khổ, nới lề. |
| L2 | Sáng | Đạt 9,5 | [games/typing-defense/art-src/ui/lanterns/lantern-lit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-lit.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: vật cao 92 %; thêm lề, đổi khổ. |
| L3 | Cháy rực | Đạt 9,5 | [games/typing-defense/art-src/ui/lanterns/lantern-blazing.png](../../games/typing-defense/art-src/ui/lanterns/lantern-blazing.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: vật cao 92 %; thêm lề, đổi khổ. |
| U1 | Lũy Chữ | Đạt 9 | [games/typing-defense/art-src/ui/buildings/keep.png](../../games/typing-defense/art-src/ui/buildings/keep.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: chưa giản lược nhưng rõ ở 32 px; khóa nền, thêm lề, đổi khổ. |
| U2 | Tháp Cung | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/ui/buildings/archer.png](../../games/typing-defense/art-src/ui/buildings/archer.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: cây cung chìm ở 32 px, cờ ngả đỏ; chỉnh màu cờ, thêm lề, đổi khổ. |
| U3 | Tháp Pháo | Đạt 9 | [games/typing-defense/art-src/ui/buildings/cannon.png](../../games/typing-defense/art-src/ui/buildings/cannon.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10: còn cầu thang, bến gỗ nhưng nòng rõ ở 32 px; thêm lề, đổi khổ. |
| U4 | Trại Lính | Tạm chấp nhận 8,5 | [games/typing-defense/art-src/ui/buildings/barracks.png](../../games/typing-defense/art-src/ui/buildings/barracks.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10 (P1): khớp BUILDREF barracks.png và bộ U1–U3, nhưng là nhà dài thấp cũ, khác dáng tháp barracks-v2/glb; khổ 3:2, ở 48 px nhỏ hơn U1–U3. icon.sh, cắt sát trước khi đệm vuông. |
| U5 | Mỏ Vàng | Đạt 9,5 | [games/typing-defense/art-src/ui/buildings/gold-mine.png](../../games/typing-defense/art-src/ui/buildings/gold-mine.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10 (P1): đủ nét, rõ ở 48 px; khổ 1254, vật khoảng 95 %, cờ cam sáng hơn #C98A2E. icon.sh. |
| U6 | Ruộng Lúa | Đạt 9,5 | [games/typing-defense/art-src/ui/buildings/farm.png](../../games/typing-defense/art-src/ui/buildings/farm.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10 (P1): đủ nét, rõ ở 48 px; nền magenta, khổ 1254, vật khoảng 95 %. icon.sh `--src-bg auto`, kiểm viền hồng. |
| U7 | Đài Ấn (nếu kịp) | Đạt 9 | [games/typing-defense/art-src/ui/buildings/seal-dais.png](../../games/typing-defense/art-src/ui/buildings/seal-dais.png) | Còn lại 015b; prompt ở file 03. Chấm lại 26/10 (P2): đủ nét; đá kem hơi chìm trên nền giấy ở 48 px, rõ trên gỗ tối; cờ tím đậm hơn #8F72E8. icon.sh. |
| U8 | Dừng | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-0.png](../../games/typing-defense/art-src/ui/tempo/tempo-0.png) | Còn lại 015b; prompt ở file 03. |
| U9 | 6 s (8 s dùng chung) | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-6.png](../../games/typing-defense/art-src/ui/tempo/tempo-6.png) | Còn lại 015b; prompt ở file 03. |
| U10 | 4 s | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-4.png](../../games/typing-defense/art-src/ui/tempo/tempo-4.png) | Còn lại 015b; prompt ở file 03. |
| U11 | 3 s | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-3.png](../../games/typing-defense/art-src/ui/tempo/tempo-3.png) | Còn lại 015b; prompt ở file 03. |
| U12 | 2 s | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-2.png](../../games/typing-defense/art-src/ui/tempo/tempo-2.png) | Còn lại 015b; prompt ở file 03. |
| U13 | 1 s | Thiếu | [games/typing-defense/art-src/ui/tempo/tempo-1.png](../../games/typing-defense/art-src/ui/tempo/tempo-1.png) | Còn lại 015b; prompt ở file 03. |
| U14 | Bùa Sửa · sửa một nhà 50 % | Thiếu | [games/typing-defense/art-src/ui/charms/charm-mend.png](../../games/typing-defense/art-src/ui/charms/charm-mend.png) | Còn lại 015b; prompt ở file 03. |
| U15 | Bùa Băng · đóng băng quái 2 s | Thiếu | [games/typing-defense/art-src/ui/charms/charm-frost.png](../../games/typing-defense/art-src/ui/charms/charm-frost.png) | Còn lại 015b; prompt ở file 03. |
| U16 | Bùa Gió · người đi nhanh 30 % | Thiếu | [games/typing-defense/art-src/ui/charms/charm-gale.png](../../games/typing-defense/art-src/ui/charms/charm-gale.png) | Còn lại 015b; prompt ở file 03. |
| U17 | Mạng | Thiếu | [games/typing-defense/art-src/ui/resources/lives.png](../../games/typing-defense/art-src/ui/resources/lives.png) | Còn lại 015b; prompt ở file 03. |
| U18 | Vàng | Thiếu | [games/typing-defense/art-src/ui/resources/gold.png](../../games/typing-defense/art-src/ui/resources/gold.png) | Còn lại 015b; prompt ở file 03. |
| U19 | Lúa (cũng là bó lúa bay về HUD) | Thiếu | [games/typing-defense/art-src/ui/resources/food.png](../../games/typing-defense/art-src/ui/resources/food.png) | Còn lại 015b; prompt ở file 03. |
| U20 | Gỗ (cũng là khúc gỗ bay về HUD) | Thiếu | [games/typing-defense/art-src/ui/resources/wood.png](../../games/typing-defense/art-src/ui/resources/wood.png) | Còn lại 015b; prompt ở file 03. |
| U21 | Tri thức (ngoài trận) | Thiếu | [games/typing-defense/art-src/ui/resources/knowledge.png](../../games/typing-defense/art-src/ui/resources/knowledge.png) | Còn lại 015b; prompt ở file 03. |
| U22 | Đợt | Thiếu | [games/typing-defense/art-src/ui/resources/wave.png](../../games/typing-defense/art-src/ui/resources/wave.png) | Còn lại 015b; prompt ở file 03. |
| U23 | common | Thiếu | [games/typing-defense/art-src/ui/loot/coin-common.png](../../games/typing-defense/art-src/ui/loot/coin-common.png) | Còn lại 015b; prompt ở file 03. |
| U24 | refined | Thiếu | [games/typing-defense/art-src/ui/loot/coin-refined.png](../../games/typing-defense/art-src/ui/loot/coin-refined.png) | Còn lại 015b; prompt ở file 03. |
| U25 | high | Thiếu | [games/typing-defense/art-src/ui/loot/coin-high.png](../../games/typing-defense/art-src/ui/loot/coin-high.png) | Còn lại 015b; prompt ở file 03. |
| U26 | elite | Thiếu | [games/typing-defense/art-src/ui/loot/coin-elite.png](../../games/typing-defense/art-src/ui/loot/coin-elite.png) | Còn lại 015b; prompt ở file 03. |
| U27 | mini-boss | Thiếu | [games/typing-defense/art-src/ui/loot/coin-mini-boss.png](../../games/typing-defense/art-src/ui/loot/coin-mini-boss.png) | Còn lại 015b; prompt ở file 03. |
| U28 | major-boss | Thiếu | [games/typing-defense/art-src/ui/loot/coin-major-boss.png](../../games/typing-defense/art-src/ui/loot/coin-major-boss.png) | Còn lại 015b; prompt ở file 03. |
| X1 | Bụi bung · xây nhà, lính ra cổng, nổ bụi, Đổ Nát, bụi phấn; game tô màu thành bụi, phấn, khói | Đã có | [games/typing-defense/art-src/vfx/dust-puff.png](../../games/typing-defense/art-src/vfx/dust-puff.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X2 | Nổ hoạt hình · đạn Pháo, cầu lửa Draconis (có từ 1A) | Đã có | [games/typing-defense/art-src/vfx/explosion.png](../../games/typing-defense/art-src/vfx/explosion.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X3 | Lửa lặp · vũng cháy Tối Thượng Draconis (1B), cháy trên quái, lông lửa | Đã có | [games/typing-defense/art-src/vfx/flame-loop.png](../../games/typing-defense/art-src/vfx/flame-loop.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X4 | Té nước · Thuồng Luồng (1A) chết thành cột nước, phun vòng nước | Đã có | [games/typing-defense/art-src/vfx/water-splash.png](../../games/typing-defense/art-src/vfx/water-splash.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X5 | Mực bắn · Mực Câm bong khi mọi quái chết (22.6); VS tô đen ánh xanh ngọc cho Thư Pháp | Đã có | [games/typing-defense/art-src/vfx/ink-splat.png](../../games/typing-defense/art-src/vfx/ink-splat.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X6 | Giấy vụn · "vệt mực bong thành giấy vụn" khi quái chết (22.6) | Đã có | [games/typing-defense/art-src/vfx/paper-scraps.png](../../games/typing-defense/art-src/vfx/paper-scraps.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X7 | Lá rơi · cây đổ khi đặt nhà (1C), Tanuki chết (1B) | Đã có | [games/typing-defense/art-src/vfx/leaf-flakes.png](../../games/typing-defense/art-src/vfx/leaf-flakes.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X8 | Mảnh gỗ · nhà bị đánh, sửa, bán (ván bay), Mầm Gỗ, Mộc Tinh | Đã có | [games/typing-defense/art-src/vfx/wood-chips.png](../../games/typing-defense/art-src/vfx/wood-chips.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X9 | Mảnh đá · Troll hóa đá vỡ (1B), Lũy bị đánh | Đã có | [games/typing-defense/art-src/vfx/stone-chips.png](../../games/typing-defense/art-src/vfx/stone-chips.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X10 | Vết cháy · decal trên đất sau nổ Pháo, cầu lửa (23.8) | Đã có | [games/typing-defense/art-src/vfx/scorch-mark.png](../../games/typing-defense/art-src/vfx/scorch-mark.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X11 | Đốm Ma Trơi · quái Đàn Ma Trơi không có model (27.2: Ma Trơi là VFX) | Đã có | [games/typing-defense/art-src/vfx/ma-troi-wisp.png](../../games/typing-defense/art-src/vfx/ma-troi-wisp.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| X12 | Tờ tham khảo Ma Trơi · chỉ để AI tích hợp xem dáng đàn và cảnh chết; không vào game; không bắt buộc | Thiếu | [games/typing-defense/art-src/vfx/ma-troi-sheet.png](../../games/typing-defense/art-src/vfx/ma-troi-sheet.png) | Còn lại 015b; prompt ở file 03. Tham khảo tùy chọn, không vào game. |

| Mã | Nội dung | Trạng thái | Ảnh / nguồn |
|---|---|---|---|
| Tựa | Làng tre hoàng hôn | Đã có | [games/typing-defense/art-src/ui/title-dusk.png](../../games/typing-defense/art-src/ui/title-dusk.png); prompt 05-title-dusk.md, WebP runtime đã có. |

### 3.4. Ảnh dùng thẳng VS · chưa thuộc 005a/005b2

Đúng **200 ảnh**: 110 cảnh (30 meadow + 32 coast + 48 rainforest), 12 phông, 14 chân dung, 3 ảnh trượt, 6 tranh truyện, 48 Neon, 4 thú nền, 3 icon. S30 có 2 biến thể × 8 hướng; Neon 12 loại × 4 biến thể. Mỗi dòng dưới là một file riêng; làm sau P.

| Mã | Nội dung | Trạng thái | Đích theo prompt |
|---|---|---|---|
| S14-v1 | Cọc đá ruộng · cọc đá đánh dấu bờ ruộng | Thiếu | [games/typing-defense/art-src/scenery/meadow/field-marker-v1.png](../../games/typing-defense/art-src/scenery/meadow/field-marker-v1.png) |
| S14-v2 | Cọc đá ruộng · cọc đá đánh dấu bờ ruộng | Thiếu | [games/typing-defense/art-src/scenery/meadow/field-marker-v2.png](../../games/typing-defense/art-src/scenery/meadow/field-marker-v2.png) |
| S14-v3 | Cọc đá ruộng · cọc đá đánh dấu bờ ruộng | Thiếu | [games/typing-defense/art-src/scenery/meadow/field-marker-v3.png](../../games/typing-defense/art-src/scenery/meadow/field-marker-v3.png) |
| S14-v4 | Cọc đá ruộng · cọc đá đánh dấu bờ ruộng | Thiếu | [games/typing-defense/art-src/scenery/meadow/field-marker-v4.png](../../games/typing-defense/art-src/scenery/meadow/field-marker-v4.png) |
| S15-v1 | Cây ô-liu · cây già thân xoắn, tán xám bạc | Thiếu | [games/typing-defense/art-src/scenery/coast/olive-tree-v1.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v1.png) |
| S15-v2 | Cây ô-liu · cây già thân xoắn, tán xám bạc | Thiếu | [games/typing-defense/art-src/scenery/coast/olive-tree-v2.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v2.png) |
| S15-v3 | Cây ô-liu · cây già thân xoắn, tán xám bạc | Thiếu | [games/typing-defense/art-src/scenery/coast/olive-tree-v3.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v3.png) |
| S15-v4 | Cây ô-liu · cây già thân xoắn, tán xám bạc | Thiếu | [games/typing-defense/art-src/scenery/coast/olive-tree-v4.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v4.png) |
| S16-v1 | Phi lao · cây cao, tán rủ nghiêng theo gió | Thiếu | [games/typing-defense/art-src/scenery/coast/casuarina-v1.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v1.png) |
| S16-v2 | Phi lao · cây cao, tán rủ nghiêng theo gió | Thiếu | [games/typing-defense/art-src/scenery/coast/casuarina-v2.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v2.png) |
| S16-v3 | Phi lao · cây cao, tán rủ nghiêng theo gió | Thiếu | [games/typing-defense/art-src/scenery/coast/casuarina-v3.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v3.png) |
| S16-v4 | Phi lao · cây cao, tán rủ nghiêng theo gió | Thiếu | [games/typing-defense/art-src/scenery/coast/casuarina-v4.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v4.png) |
| S17-v1 | Cỏ biển · bụi cỏ cồn cát (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/coast/sea-grass-v1.png](../../games/typing-defense/art-src/scenery/coast/sea-grass-v1.png) |
| S17-v2 | Cỏ biển · bụi cỏ cồn cát (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/coast/sea-grass-v2.png](../../games/typing-defense/art-src/scenery/coast/sea-grass-v2.png) |
| S17-v3 | Cỏ biển · bụi cỏ cồn cát (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/coast/sea-grass-v3.png](../../games/typing-defense/art-src/scenery/coast/sea-grass-v3.png) |
| S17-v4 | Cỏ biển · bụi cỏ cồn cát (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/coast/sea-grass-v4.png](../../games/typing-defense/art-src/scenery/coast/sea-grass-v4.png) |
| S18-v1 | Hoa muống biển · thảm dây bò, hoa hồng | Thiếu | [games/typing-defense/art-src/scenery/coast/morning-glory-v1.png](../../games/typing-defense/art-src/scenery/coast/morning-glory-v1.png) |
| S18-v2 | Hoa muống biển · thảm dây bò, hoa hồng | Thiếu | [games/typing-defense/art-src/scenery/coast/morning-glory-v2.png](../../games/typing-defense/art-src/scenery/coast/morning-glory-v2.png) |
| S18-v3 | Hoa muống biển · thảm dây bò, hoa hồng | Thiếu | [games/typing-defense/art-src/scenery/coast/morning-glory-v3.png](../../games/typing-defense/art-src/scenery/coast/morning-glory-v3.png) |
| S18-v4 | Hoa muống biển · thảm dây bò, hoa hồng | Thiếu | [games/typing-defense/art-src/scenery/coast/morning-glory-v4.png](../../games/typing-defense/art-src/scenery/coast/morning-glory-v4.png) |
| S19-v1 | Đá vôi trắng nhỏ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-small-v1.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v1.png) |
| S19-v2 | Đá vôi trắng nhỏ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-small-v2.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v2.png) |
| S19-v3 | Đá vôi trắng nhỏ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-small-v3.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v3.png) |
| S19-v4 | Đá vôi trắng nhỏ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-small-v4.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v4.png) |
| S20-v1 | Đá vôi trắng vừa · tảng đá tròn, mặt có gờ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-medium-v1.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v1.png) |
| S20-v2 | Đá vôi trắng vừa · tảng đá tròn, mặt có gờ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-medium-v2.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v2.png) |
| S20-v3 | Đá vôi trắng vừa · tảng đá tròn, mặt có gờ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-medium-v3.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v3.png) |
| S20-v4 | Đá vôi trắng vừa · tảng đá tròn, mặt có gờ | Thiếu | [games/typing-defense/art-src/scenery/coast/limestone-medium-v4.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v4.png) |
| S21-v1 | Lưới phơi · giá tre phơi lưới cá | Thiếu | [games/typing-defense/art-src/scenery/coast/net-rack-v1.png](../../games/typing-defense/art-src/scenery/coast/net-rack-v1.png) |
| S21-v2 | Lưới phơi · giá tre phơi lưới cá | Thiếu | [games/typing-defense/art-src/scenery/coast/net-rack-v2.png](../../games/typing-defense/art-src/scenery/coast/net-rack-v2.png) |
| S21-v3 | Lưới phơi · giá tre phơi lưới cá | Thiếu | [games/typing-defense/art-src/scenery/coast/net-rack-v3.png](../../games/typing-defense/art-src/scenery/coast/net-rack-v3.png) |
| S21-v4 | Lưới phơi · giá tre phơi lưới cá | Thiếu | [games/typing-defense/art-src/scenery/coast/net-rack-v4.png](../../games/typing-defense/art-src/scenery/coast/net-rack-v4.png) |
| S22-v1 | Thuyền thúng úp | Thiếu | [games/typing-defense/art-src/scenery/coast/basket-boat-v1.png](../../games/typing-defense/art-src/scenery/coast/basket-boat-v1.png) |
| S22-v2 | Thuyền thúng úp | Thiếu | [games/typing-defense/art-src/scenery/coast/basket-boat-v2.png](../../games/typing-defense/art-src/scenery/coast/basket-boat-v2.png) |
| S22-v3 | Thuyền thúng úp | Thiếu | [games/typing-defense/art-src/scenery/coast/basket-boat-v3.png](../../games/typing-defense/art-src/scenery/coast/basket-boat-v3.png) |
| S22-v4 | Thuyền thúng úp | Thiếu | [games/typing-defense/art-src/scenery/coast/basket-boat-v4.png](../../games/typing-defense/art-src/scenery/coast/basket-boat-v4.png) |
| S23-v1 | Cây rừng to · thân xám, rễ bạnh | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v1.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v1.png) |
| S23-v2 | Cây rừng to · thân xám, rễ bạnh | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v2.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v2.png) |
| S23-v3 | Cây rừng to · thân xám, rễ bạnh | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v3.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v3.png) |
| S23-v4 | Cây rừng to · thân xám, rễ bạnh | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v4.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v4.png) |
| S24-v1 | Dây leo · gốc cây chết quấn dây leo | Thiếu | [games/typing-defense/art-src/scenery/rainforest/vine-stump-v1.png](../../games/typing-defense/art-src/scenery/rainforest/vine-stump-v1.png) |
| S24-v2 | Dây leo · gốc cây chết quấn dây leo | Thiếu | [games/typing-defense/art-src/scenery/rainforest/vine-stump-v2.png](../../games/typing-defense/art-src/scenery/rainforest/vine-stump-v2.png) |
| S24-v3 | Dây leo · gốc cây chết quấn dây leo | Thiếu | [games/typing-defense/art-src/scenery/rainforest/vine-stump-v3.png](../../games/typing-defense/art-src/scenery/rainforest/vine-stump-v3.png) |
| S24-v4 | Dây leo · gốc cây chết quấn dây leo | Thiếu | [games/typing-defense/art-src/scenery/rainforest/vine-stump-v4.png](../../games/typing-defense/art-src/scenery/rainforest/vine-stump-v4.png) |
| S25-v1 | Dương xỉ thân gỗ | Thiếu | [games/typing-defense/art-src/scenery/rainforest/tree-fern-v1.png](../../games/typing-defense/art-src/scenery/rainforest/tree-fern-v1.png) |
| S25-v2 | Dương xỉ thân gỗ | Thiếu | [games/typing-defense/art-src/scenery/rainforest/tree-fern-v2.png](../../games/typing-defense/art-src/scenery/rainforest/tree-fern-v2.png) |
| S25-v3 | Dương xỉ thân gỗ | Thiếu | [games/typing-defense/art-src/scenery/rainforest/tree-fern-v3.png](../../games/typing-defense/art-src/scenery/rainforest/tree-fern-v3.png) |
| S25-v4 | Dương xỉ thân gỗ | Thiếu | [games/typing-defense/art-src/scenery/rainforest/tree-fern-v4.png](../../games/typing-defense/art-src/scenery/rainforest/tree-fern-v4.png) |
| S26-v1 | Cụm nấm | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v1.png](../../games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v1.png) |
| S26-v2 | Cụm nấm | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v2.png](../../games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v2.png) |
| S26-v3 | Cụm nấm | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v3.png](../../games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v3.png) |
| S26-v4 | Cụm nấm | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v4.png](../../games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v4.png) |
| S27-v1 | Rễ nhỏ · đám rễ uốn vòng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/root-tangle-v1.png](../../games/typing-defense/art-src/scenery/rainforest/root-tangle-v1.png) |
| S27-v2 | Rễ nhỏ · đám rễ uốn vòng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/root-tangle-v2.png](../../games/typing-defense/art-src/scenery/rainforest/root-tangle-v2.png) |
| S27-v3 | Rễ nhỏ · đám rễ uốn vòng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/root-tangle-v3.png](../../games/typing-defense/art-src/scenery/rainforest/root-tangle-v3.png) |
| S27-v4 | Rễ nhỏ · đám rễ uốn vòng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/root-tangle-v4.png](../../games/typing-defense/art-src/scenery/rainforest/root-tangle-v4.png) |
| S28-v1 | Phong lan · khóm lan trên mẩu cành | Thiếu | [games/typing-defense/art-src/scenery/rainforest/orchid-clump-v1.png](../../games/typing-defense/art-src/scenery/rainforest/orchid-clump-v1.png) |
| S28-v2 | Phong lan · khóm lan trên mẩu cành | Thiếu | [games/typing-defense/art-src/scenery/rainforest/orchid-clump-v2.png](../../games/typing-defense/art-src/scenery/rainforest/orchid-clump-v2.png) |
| S28-v3 | Phong lan · khóm lan trên mẩu cành | Thiếu | [games/typing-defense/art-src/scenery/rainforest/orchid-clump-v3.png](../../games/typing-defense/art-src/scenery/rainforest/orchid-clump-v3.png) |
| S28-v4 | Phong lan · khóm lan trên mẩu cành | Thiếu | [games/typing-defense/art-src/scenery/rainforest/orchid-clump-v4.png](../../games/typing-defense/art-src/scenery/rainforest/orchid-clump-v4.png) |
| S29-v1 | Đá rêu rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v1.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v1.png) |
| S29-v2 | Đá rêu rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v2.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v2.png) |
| S29-v3 | Đá rêu rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v3.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v3.png) |
| S29-v4 | Đá rêu rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v4.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v4.png) |
| S30-v1-d0 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d0.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d0.png) |
| S30-v1-d1 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d1.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d1.png) |
| S30-v1-d2 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d2.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d2.png) |
| S30-v1-d3 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d3.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d3.png) |
| S30-v1-d4 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d4.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d4.png) |
| S30-v1-d5 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d5.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d5.png) |
| S30-v1-d6 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d6.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d6.png) |
| S30-v1-d7 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d7.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d7.png) |
| S30-v2-d0 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d0.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d0.png) |
| S30-v2-d1 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d1.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d1.png) |
| S30-v2-d2 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d2.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d2.png) |
| S30-v2-d3 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d3.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d3.png) |
| S30-v2-d4 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d4.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d4.png) |
| S30-v2-d5 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d5.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d5.png) |
| S30-v2-d6 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d6.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d6.png) |
| S30-v2-d7 | Nhà sàn bỏ hoang · đặt xa, ở mép bản đồ; impostor 8 hướng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d7.png](../../games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d7.png) |
| S31-v1 | Khối tán rừng mưa · tường tán ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v1.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v1.png) |
| S31-v2 | Khối tán rừng mưa · tường tán ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v2.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v2.png) |
| S31-v3 | Khối tán rừng mưa · tường tán ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v3.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v3.png) |
| S31-v4 | Khối tán rừng mưa · tường tán ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v4.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v4.png) |
| F7 | w1-whitestone / sky-a | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/sky-a.png) |
| F8 | w1-whitestone / sky-b | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/sky-b.png) |
| F9 | w1-whitestone / layer-320 | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-320.png) |
| F10 | w1-whitestone / layer-220 | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-220.png) |
| F11 | w1-whitestone / layer-140-a | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-a.png) |
| F12 | w1-whitestone / layer-140-b | Thiếu | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-b.png) |
| F13 | w1-rootwood / sky-a | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/sky-a.png) |
| F14 | w1-rootwood / sky-b | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/sky-b.png) |
| F15 | w1-rootwood / layer-320 | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-320.png) |
| F16 | w1-rootwood / layer-220 | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-220.png) |
| F17 | w1-rootwood / layer-140-a | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-a.png) |
| F18 | w1-rootwood / layer-140-b | Thiếu | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-b.png) |
| C9 | lam / Lam, Tướng chạy nhanh | Thiếu | [games/typing-defense/art-src/portraits/lam.png](../../games/typing-defense/art-src/portraits/lam.png) |
| C10 | tre / Tre, Tướng thợ | Thiếu | [games/typing-defense/art-src/portraits/tre.png](../../games/typing-defense/art-src/portraits/tre.png) |
| C11 | crew-keep / Lão Gác Cổng (Lũy Chữ) | Thiếu | [games/typing-defense/art-src/portraits/crew-keep.png](../../games/typing-defense/art-src/portraits/crew-keep.png) |
| C12 | crew-archer / Chị Én và Em Sẻ (Tháp Cung) | Thiếu | [games/typing-defense/art-src/portraits/crew-archer.png](../../games/typing-defense/art-src/portraits/crew-archer.png) |
| C13 | crew-cannon / Bác Đồng và cậu Lửa (Tháp Pháo) | Thiếu | [games/typing-defense/art-src/portraits/crew-cannon.png](../../games/typing-defense/art-src/portraits/crew-cannon.png) |
| C14 | crew-scribe / Thầy Đồ Mực (Tháp Thư Pháp) | Thiếu | [games/typing-defense/art-src/portraits/crew-scribe.png](../../games/typing-defense/art-src/portraits/crew-scribe.png) |
| C15 | crew-barracks / Đội trưởng Sấm (Trại Lính) | Thiếu | [games/typing-defense/art-src/portraits/crew-barracks.png](../../games/typing-defense/art-src/portraits/crew-barracks.png) |
| C16 | crew-gold-mine / Ba anh em thợ mỏ (Mỏ Vàng) | Thiếu | [games/typing-defense/art-src/portraits/crew-gold-mine.png](../../games/typing-defense/art-src/portraits/crew-gold-mine.png) |
| C17 | crew-farm / Cô Mạ và trâu Mộng (Ruộng Lúa) | Thiếu | [games/typing-defense/art-src/portraits/crew-farm.png](../../games/typing-defense/art-src/portraits/crew-farm.png) |
| C18 | crew-lumber / Chú Tiều (Trại Gỗ) | Thiếu | [games/typing-defense/art-src/portraits/crew-lumber.png](../../games/typing-defense/art-src/portraits/crew-lumber.png) |
| C19 | crew-seal-dais / Trò Mực (Đài Ấn) | Thiếu | [games/typing-defense/art-src/portraits/crew-seal-dais.png](../../games/typing-defense/art-src/portraits/crew-seal-dais.png) |
| C20 | crew-infirmary / Bà Lang Thơm (Nhà Thuốc) | Thiếu | [games/typing-defense/art-src/portraits/crew-infirmary.png](../../games/typing-defense/art-src/portraits/crew-infirmary.png) |
| C21 | moc-tinh / Mộc Tinh, boss bản đồ 1 và 3 | Thiếu | [games/typing-defense/art-src/portraits/moc-tinh.png](../../games/typing-defense/art-src/portraits/moc-tinh.png) |
| C22 | dai-bang-tinh / Đại Bàng Tinh, boss bản đồ 2 | Thiếu | [games/typing-defense/art-src/portraits/dai-bang-tinh.png](../../games/typing-defense/art-src/portraits/dai-bang-tinh.png) |
| C23 | draconis-ult / Mưa Lông Lửa | Thiếu | [games/typing-defense/art-src/portraits/draconis-ult.png](../../games/typing-defense/art-src/portraits/draconis-ult.png) |
| C24 | lam-ult / Hỏa Tốc | Thiếu | [games/typing-defense/art-src/portraits/lam-ult.png](../../games/typing-defense/art-src/portraits/lam-ult.png) |
| C25 | tre-ult / Giàn Giáo Thần Tốc | Thiếu | [games/typing-defense/art-src/portraits/tre-ult.png](../../games/typing-defense/art-src/portraits/tre-ult.png) |
| T1 | Draconis / 1 · chòm sao bị mực nuốt | Thiếu | [games/typing-defense/art-src/story/draconis/1.png](../../games/typing-defense/art-src/story/draconis/1.png) |
| T2 | Draconis / 2 · đậu mái kho lúa giữ làng | Thiếu | [games/typing-defense/art-src/story/draconis/2.png](../../games/typing-defense/art-src/story/draconis/2.png) |
| T3 | Lam / 1 · lá thư chưa gửi của bà | Thiếu | [games/typing-defense/art-src/story/lam/1.png](../../games/typing-defense/art-src/story/lam/1.png) |
| T4 | Lam / 2 · lửa chuyển từ cam khói sang xanh | Thiếu | [games/typing-defense/art-src/story/lam/2.png](../../games/typing-defense/art-src/story/lam/2.png) |
| T5 | Tre / 1 · cầu sập, bố kẹt bên kia sông | Thiếu | [games/typing-defense/art-src/story/tre/1.png](../../games/typing-defense/art-src/story/tre/1.png) |
| T6 | Tre / 2 · cả làng cùng dựng cầu | Thiếu | [games/typing-defense/art-src/story/tre/2.png](../../games/typing-defense/art-src/story/tre/2.png) |
| N1-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v1.png) |
| N1-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v2.png) |
| N1-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v3.png) |
| N1-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v4.png) |
| N2-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v1.png) |
| N2-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v2.png) |
| N2-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v3.png) |
| N2-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v4.png) |
| N3-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v1.png) |
| N3-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v2.png) |
| N3-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v3.png) |
| N3-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v4.png) |
| N4-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v1.png) |
| N4-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v2.png) |
| N4-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v3.png) |
| N4-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v4.png) |
| N5-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v1.png) |
| N5-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v2.png) |
| N5-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v3.png) |
| N5-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v4.png) |
| N6-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v1.png) |
| N6-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v2.png) |
| N6-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v3.png) |
| N6-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v4.png) |
| N7-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v1.png) |
| N7-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v2.png) |
| N7-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v3.png) |
| N7-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v4.png) |
| N8-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/fern-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/fern-v1.png) |
| N8-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/fern-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/fern-v2.png) |
| N8-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/fern-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/fern-v3.png) |
| N8-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/fern-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/fern-v4.png) |
| N9-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-small-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-small-v1.png) |
| N9-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-small-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-small-v2.png) |
| N9-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-small-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-small-v3.png) |
| N9-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-small-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-small-v4.png) |
| N10-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v1.png) |
| N10-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v2.png) |
| N10-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v3.png) |
| N10-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v4.png) |
| N11-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v1.png) |
| N11-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v2.png) |
| N11-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v3.png) |
| N11-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v4.png) |
| N12-v1 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v1.png](../../games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v1.png) |
| N12-v2 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v2.png) |
| N12-v3 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v3.png](../../games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v3.png) |
| N12-v4 | Atlas cảnh Neon | Thiếu | [games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v4.png](../../games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v4.png) |
| A1 | egret / Cò trắng bay · bản đồ 1 | Thiếu | [games/typing-defense/art-src/fauna/egret.png](../../games/typing-defense/art-src/fauna/egret.png) |
| A2 | gull / Hải âu bay · bản đồ 2 | Thiếu | [games/typing-defense/art-src/fauna/gull.png](../../games/typing-defense/art-src/fauna/gull.png) |
| A3 | firefly / Đom đóm nhấp nháy · bản đồ 3, đợt boss | Thiếu | [games/typing-defense/art-src/fauna/firefly.png](../../games/typing-defense/art-src/fauna/firefly.png) |
| A4 | butterfly / Bướm vỗ cánh · bản đồ 3 | Thiếu | [games/typing-defense/art-src/fauna/butterfly.png](../../games/typing-defense/art-src/fauna/butterfly.png) |
| U29 | scribe / Tháp Thư Pháp | Thiếu | [games/typing-defense/art-src/ui/buildings/scribe.png](../../games/typing-defense/art-src/ui/buildings/scribe.png) |
| U30 | lumber / Trại Gỗ | Thiếu | [games/typing-defense/art-src/ui/buildings/lumber.png](../../games/typing-defense/art-src/ui/buildings/lumber.png) |
| U31 | infirmary / Nhà Thuốc | Thiếu | [games/typing-defense/art-src/ui/buildings/infirmary.png](../../games/typing-defense/art-src/ui/buildings/infirmary.png) |
| S1-v3 | Cây bàng · cây to, tán xếp tầng ngang | Thiếu | [games/typing-defense/art-src/scenery/meadow/almond-tree-v3.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v3.png) |
| S1-v4 | Cây bàng · cây to, tán xếp tầng ngang | Thiếu | [games/typing-defense/art-src/scenery/meadow/almond-tree-v4.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v4.png) |
| S2-v3 | Thông núi · cây cao, tán thành đệm tròn | Thiếu | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v3.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v3.png) |
| S2-v4 | Thông núi · cây cao, tán thành đệm tròn | Thiếu | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v4.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v4.png) |
| S3-v3 | Khóm tre · bụi tre làng, ngọn cong | Thiếu | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v3.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v3.png) |
| S3-v4 | Khóm tre · bụi tre làng, ngọn cong | Thiếu | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v4.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v4.png) |
| S4-v3 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Thiếu | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v3.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v3.png) |
| S4-v4 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Thiếu | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v4.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v4.png) |
| S5-v3 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/meadow/tall-grass-v3.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v3.png) |
| S5-v4 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Thiếu | [games/typing-defense/art-src/scenery/meadow/tall-grass-v4.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v4.png) |
| S6-v3 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Thiếu | [games/typing-defense/art-src/scenery/meadow/reed-clump-v3.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v3.png) |
| S6-v4 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Thiếu | [games/typing-defense/art-src/scenery/meadow/reed-clump-v4.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v4.png) |
| S7-v3 | Hoa dại trắng vàng · khóm hoa thấp | Thiếu | [games/typing-defense/art-src/scenery/meadow/wildflowers-v3.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v3.png) |
| S7-v4 | Hoa dại trắng vàng · khóm hoa thấp | Thiếu | [games/typing-defense/art-src/scenery/meadow/wildflowers-v4.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v4.png) |
| S8-v3 | Dương xỉ · khóm lá xòe bờ ẩm | Thiếu | [games/typing-defense/art-src/scenery/meadow/fern-v3.png](../../games/typing-defense/art-src/scenery/meadow/fern-v3.png) |
| S8-v4 | Dương xỉ · khóm lá xòe bờ ẩm | Thiếu | [games/typing-defense/art-src/scenery/meadow/fern-v4.png](../../games/typing-defense/art-src/scenery/meadow/fern-v4.png) |
| S9-v3 | Đá xám rêu nhỏ | Thiếu | [games/typing-defense/art-src/scenery/meadow/rock-small-v3.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v3.png) |
| S9-v4 | Đá xám rêu nhỏ | Thiếu | [games/typing-defense/art-src/scenery/meadow/rock-small-v4.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v4.png) |
| S10-v3 | Đá xám rêu vừa · tảng đá to | Thiếu | [games/typing-defense/art-src/scenery/meadow/rock-medium-v3.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v3.png) |
| S10-v4 | Đá xám rêu vừa · tảng đá to | Thiếu | [games/typing-defense/art-src/scenery/meadow/rock-medium-v4.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v4.png) |
| S11-v3 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Thiếu | [games/typing-defense/art-src/scenery/meadow/rotten-log-v3.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v3.png) |
| S11-v4 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Thiếu | [games/typing-defense/art-src/scenery/meadow/rotten-log-v4.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v4.png) |
| S12-v3 | Khối tán · bức tường tán cây ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/meadow/canopy-block-v3.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v3.png) |
| S12-v4 | Khối tán · bức tường tán cây ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/meadow/canopy-block-v4.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v4.png) |
| S13-v3 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Thiếu | [games/typing-defense/art-src/scenery/shared/tree-stump-v3.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v3.png) |
| S13-v4 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Thiếu | [games/typing-defense/art-src/scenery/shared/tree-stump-v4.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v4.png) |

### 3.5. Lỗ hổng prompt được file 03 §14 ghi

Các nhóm dưới thiếu id/đích raster và prompt riêng. 1B có ký hiệu/khung vẽ bằng Canvas/DOM; cần khóa nhu cầu bitmap trước khi sinh. Không tự đặt tên hàng loạt hoặc coi đây là PNG 3D thiếu.

| Nhóm | Nội dung | Số lượng | Trạng thái |
|---|---|---|---|
| Tín hiệu nhà · 8.9 | Bị đánh; Có trộm; Cơn Gấp sắp tới; Đổ Nát; Sẵn cụm chốt; Nhà nguội; Kho đầy | 7 ký hiệu | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Trạng thái quái · 10.3, 23.8 | Chậm; Choáng; Đóng băng; Cháy; Độc; Đánh dấu; Lộ diện; Câm; Phá giáp | 9 ký hiệu | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Phép Chỉ huy · 16.1 | Mưa Đá Lửa; Viện Binh | 2 ký hiệu | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Vật phẩm · 16.2 | Bùa Sửa lớn; Bùa Băng lớn; Bom Lửa; Tù Và Viện Binh | 4 ký hiệu | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Tài nguyên ngoài trận | Sao; Xu; Bản vẽ | 3 ký hiệu | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Khung HUD sách tranh | Gỗ; giấy da | 2 chất liệu/khung | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Texture đất bản đồ 1 | Chờ khóa bố cục và ảnh khung theo file 03 §14.5 | 1 nhóm chờ bố cục | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |
| Decal tán nhìn từ trên | 23.10, file 03 §14.8; chưa chốt số loại/biến thể | 1 nhóm chờ quy cách | Thiếu prompt/đích raster; tách riêng khỏi số PNG đã định danh. |

Nhóm Sau (Thư Thành, Sảnh Tướng, Học Viện, Xưởng Bản Vẽ, Cây Chữ, Chợ, 16 tranh bách khoa, hai người đón) ngoài P/VS, không sinh trong 015. Mảnh Chữ lấy atlas glyph; tia lửa, quầng tròn, rune, số, vệt bay do runtime dựng.

## 4. Tuyến Cuối · S1 → S2

### 4.1. Nhân vật, quái, công trình/prop và nguồn 3D

| Vai | Trạng thái | Ảnh nguồn | Cách dùng |
|---|---|---|---|
| Lính Rainbow | Tạm chấp nhận 8,5 | [games/space-typing/art-src/enemies/rainbow-scout.png](../../games/space-typing/art-src/enemies/rainbow-scout.png) | Dùng chung Space; không sao chép/sinh lại. Chấm lại 26/10: đã chấm model rainbow-tank.glb; Lính dùng chung, chỉ khác cỡ, ở xa gần bằng Trâu (FAR_GROW). Chưa xem trong trận. |
| Trâu / Đầu Đàn | Tạm chấp nhận 8,5 | [games/space-typing/art-src/enemies/rainbow-tank.png](../../games/space-typing/art-src/enemies/rainbow-tank.png) | Dùng chung Space; không sao chép/sinh lại. Chấm lại 26/10: đã chấm model rainbow-tank.glb; dáng côn trùng có cánh, chưa ra Trâu nặng nề. Chưa xem trong trận. |
| Khiên | Đã có | [games/space-typing/art-src/enemies/rainbow-shield.png](../../games/space-typing/art-src/enemies/rainbow-shield.png) | Dùng chung Space; không sao chép/sinh lại. |
| Tách | Đã có | [games/space-typing/art-src/enemies/rainbow-splitter.png](../../games/space-typing/art-src/enemies/rainbow-splitter.png) | Dùng chung Space; không sao chép/sinh lại. |
| Tổ | Đã có | [games/space-typing/art-src/enemies/rainbow-carrier.png](../../games/space-typing/art-src/enemies/rainbow-carrier.png) | Dùng chung Space; không sao chép/sinh lại. |
| Bầy lao | Đã có | [games/space-typing/art-src/enemies/rainbow-mine.png](../../games/space-typing/art-src/enemies/rainbow-mine.png) | Dùng chung Space; không sao chép/sinh lại. |
| Boss Cai Ngục | Đã có | [games/space-typing/art-src/bosses/warden-rainbow.png](../../games/space-typing/art-src/bosses/warden-rainbow.png) | Dùng chung Space; không sao chép/sinh lại. |

| Hạng mục khác | Trạng thái / cách thực hiện |
|---|---|
| Tàu và đạn | Đã có thư viện Space theo BUILD_S1 §1.1; không cần nguồn mới. Scout dùng model tank chung theo quyết định chủ dự án 26/10 trong 3D_REQUESTS. |
| Đất, tường, bến, VC-7, Hố Đen | Hình học/vật liệu/shader theo BUILD_S1 §12; không có hợp đồng atlas raster đất riêng. |
| VFX năm súng, Vỏ, Khiên, Tách, Tổ, Vết nứt, Bão ion, Giếng, boss | Hạt, strips, hình học, shader và instancing theo BUILD_S1 §12; không sinh texture thay telegraph/shader. |
| S2: mảnh chữ, lò, Nova cụm từ, Chuỗi, Hoàn hảo | Glyph, UI và shader/hình học; icon Nova ở bảng dưới. |
| S2: Băng, Lửa, Ion, Hư Không | 4 ký hiệu UI chưa có hợp đồng raster; nếu chọn PNG riêng cần chốt cỡ/hình trước, không phải nguồn 3D thiếu. |
| Cửa Súng/Rèn/Lõi/Sửa, bản đồ chương, sao, thắng/thua | UI vẽ bằng DOM; S1/S2 chưa yêu cầu tranh/sprite riêng. |
| Sét và các họ/chương sau | Ngoài lát S1/S2; không sinh thêm model hoặc icon. |

### 4.2. Màn tựa và icon

| Ảnh | Trạng thái | Đường dẫn | Ghi chú |
|---|---|---|---|
| title-horizon | Tạm chấp nhận 8,5 | [games/typing-survival/art-src/ui/title-horizon.png](../../games/typing-survival/art-src/ui/title-horizon.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. Chấm lại 26/10: vẽ như ảnh chụp, lệch màn tựa 3D của game; src chưa nạp (P3). |
| gun-xung | Đạt 9 | [games/typing-survival/art-src/ui/icons/gun-xung.png](../../games/typing-survival/art-src/ui/icons/gun-xung.png) | Đã có trước, giữ nguyên; kiểm trực tiếp: 1254×1254 khác 1024×1024, lề hẹp theo README-015. Chấm lại 26/10: co về 1024, đệm lề ~15 % khi lắp. |
| gun-tia | Đạt 9 | [games/typing-survival/art-src/ui/icons/gun-tia.png](../../games/typing-survival/art-src/ui/icons/gun-tia.png) | Đã có trước, giữ nguyên; kiểm trực tiếp: 1254×1254 khác 1024×1024, lề hẹp theo README-015. Chấm lại 26/10: đầu nón sát mép; co về 1024, đệm lề. |
| gun-tan | Tạm chấp nhận 8,5 | [games/typing-survival/art-src/ui/icons/gun-tan.png](../../games/typing-survival/art-src/ui/icons/gun-tan.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. Chấm lại 26/10: ở 32 px 7 viên dính thành cụm; lề 2 %, khổ 1254. |
| gun-ray | Tạm chấp nhận 8,5 | [games/typing-survival/art-src/ui/icons/gun-ray.png](../../games/typing-survival/art-src/ui/icons/gun-ray.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. Chấm lại 26/10: giáp chẻ đôi, nhiều mảnh vụn, chìm trên nền tối. |
| gun-phao-sao | Tạm chấp nhận 8,5 | [games/typing-survival/art-src/ui/icons/gun-phao-sao.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. Chấm lại 26/10: nòng cối mảnh, tối ở 32 px; màu lệch theme. |
| nova | Tạm chấp nhận 8,5 | [games/typing-survival/art-src/ui/icons/nova.png](../../games/typing-survival/art-src/ui/icons/nova.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. Chấm lại 26/10: ở 32 px đọc như bông tuyết, dễ lẫn ô Băng; cắt alpha, thêm lề. |

## 5. Tổng thiếu theo game

| Game / nhóm | Thiếu trước 015 | Thiếu sau kiểm hiện tại | Ghi chú |
|---|---|---|---|
| Rồng · 67 ảnh M0/M0b | 0 | 0 | Đủ file; lỗi còn theo README, 8 đích được thử trong 015. |
| Lời Gọi · nguồn P và VS | 0 | 0 | Mẫu Thư Đồng dùng chung Space; bỏ qua 119 ảnh VS của 005a/005b2. |
| Lời Gọi · 83 ảnh P + màn tựa | 69 | 48 | Trong số thiếu có 1 ảnh tham khảo X12 tùy chọn. |
| Lời Gọi · 200 ảnh VS dùng thẳng | 200 | 200 | Chưa thuộc phần 3D mà 005 đã làm. |
| Tuyến Cuối · 7 ảnh tựa/icon | 5 | 0 | 2 ảnh đã có, 5 đích được sinh ở 015. |
| Chưa có quy cách raster | Chưa chốt | 27 ký hiệu/khung TD + 2 nhóm đất/tán; 4 nguyên tố S2 nếu chọn PNG | Tách khỏi số PNG đã định danh. |

Số thiếu chỉ đếm file chưa có, không bao gồm file có nhưng lỗi. Không tuyên bố ba game đã hoàn tất mỹ thuật hoặc sẵn sàng nhập trực tiếp. README-015 của từng game ghi lượt sinh và số đo. Tổng giới hạn 45 lượt gồm bản thử lại; chưa tích hợp runtime.

Ghi chú 26/10/2026: "lỗi" và "Có nhưng lỗi" trong mục này là kết luận kiểm 25/10. Điểm và mức chấm lại ở §7 thay cho kết luận đó; bảng giữ nguyên để đối chiếu. Số P còn thiếu của Lời Gọi nay là 1 (X12, P3), không phải 48: 47/48 đích P có PNG sau 015b lượt 3 (§6.2, §7.2).

## 6. Còn lại cho phiếu 015b

### 6.1. Lỗi cần xử lý trước

Rồng: E01-S vẫn sai cánh sau lần thử thêm; G01-F và U1-F chưa xác nhận tư thế/mặt khiên, nên không sinh Back mới. D1–D4 và B1 còn giới hạn lề, nền, khổ, chi tiết hoặc mép theo README-015. Đất và icon M0 còn lỗi/giới hạn ở README cũ. Không dùng 012 để kết luận đã đạt, không yêu cầu thêm model chỉ vì ảnh ứng viên chưa đạt.

Tuyến Cuối: duyệt tựa và 4 icon đã thử lại, nhất là số viên Tán, lề Ray/Pháo Sao/Nova, alpha và đọc ở 32 px. Không sinh quá một lần thử lại. Xung/Tia cũ giữ nguyên. Nếu §4.2 đã đủ file thì không còn PNG định danh bị thiếu, nhưng các giới hạn chất lượng vẫn mở.

Ghi chú 26/10/2026: các "lỗi" ở hai đoạn trên đã chấm lại theo luật 7 điểm; §7 thay cho kết luận đó. Không mục nào dưới 7, nên không tạo lại ảnh nào. Hai đoạn trên giữ nguyên làm lịch sử.

### 6.2. Lời Gọi · từng đích P còn thiếu

Ghi chú 26/10/2026: 22 dòng ghi "Đã có" là đích 015b lượt 1 đã làm và đã chấm lại; điểm và mức ở §3.3, §7. Còn thiếu 26 đích P: U4–U28 và X12. Mức cần và thứ tự làm: [015b-priority.md](../../games/typing-defense/docs/art-requests/td/015b-priority.md) (P1 rồi P2; U8–U13, X12 là P3, chờ kinh phí).

Cập nhật sau 015b lượt 3 (26/10/2026): **47/48 đích P đã có PNG**; lượt 2 thêm U4–U13, lượt 3 thêm 15 đích P1/P2. Chỉ còn X12 (P3, chờ kinh phí). U8–U13 là P3 đã lỡ sinh ở lượt 2, giữ file. Điểm/mức và lỗi sửa được của ảnh mới ở README-015b; ghi chú 22/26 đích phía trên là số lịch sử trước lượt 2–3.

| Mã | Đích còn thiếu | Lý do |
|---|---|---|
| S3-v2 | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| S6-v2 | [games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| S12-v2 | [games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| S13-v1 | [games/typing-defense/art-src/scenery/shared/tree-stump-v1.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v1.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| S13-v2 | [games/typing-defense/art-src/scenery/shared/tree-stump-v2.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v2.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F1 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F2 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F3 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F4 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F5 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| F6 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| C3 | [games/typing-defense/art-src/portraits/helper-cham-scared.png](../../games/typing-defense/art-src/portraits/helper-cham-scared.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| C4 | [games/typing-defense/art-src/portraits/helper-phay-happy.png](../../games/typing-defense/art-src/portraits/helper-phay-happy.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| C5 | [games/typing-defense/art-src/portraits/helper-phay-scared.png](../../games/typing-defense/art-src/portraits/helper-phay-scared.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| C6 | [games/typing-defense/art-src/portraits/helper-gach-happy.png](../../games/typing-defense/art-src/portraits/helper-gach-happy.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| C7 | [games/typing-defense/art-src/portraits/helper-gach-scared.png](../../games/typing-defense/art-src/portraits/helper-gach-scared.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| L1 | [games/typing-defense/art-src/ui/lanterns/lantern-unlit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-unlit.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| L2 | [games/typing-defense/art-src/ui/lanterns/lantern-lit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-lit.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| L3 | [games/typing-defense/art-src/ui/lanterns/lantern-blazing.png](../../games/typing-defense/art-src/ui/lanterns/lantern-blazing.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| U1 | [games/typing-defense/art-src/ui/buildings/keep.png](../../games/typing-defense/art-src/ui/buildings/keep.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| U2 | [games/typing-defense/art-src/ui/buildings/archer.png](../../games/typing-defense/art-src/ui/buildings/archer.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| U3 | [games/typing-defense/art-src/ui/buildings/cannon.png](../../games/typing-defense/art-src/ui/buildings/cannon.png) | Đã có (015b lượt 1), đã chấm: xem §3.3 / §7. |
| U4 | [games/typing-defense/art-src/ui/buildings/barracks.png](../../games/typing-defense/art-src/ui/buildings/barracks.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. Chấm lại 26/10: Tạm chấp nhận 8,5 (§3.3, §7). |
| U5 | [games/typing-defense/art-src/ui/buildings/gold-mine.png](../../games/typing-defense/art-src/ui/buildings/gold-mine.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. Chấm lại 26/10: Đạt 9,5 (§3.3, §7). |
| U6 | [games/typing-defense/art-src/ui/buildings/farm.png](../../games/typing-defense/art-src/ui/buildings/farm.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. Chấm lại 26/10: Đạt 9,5 (§3.3, §7). |
| U7 | [games/typing-defense/art-src/ui/buildings/seal-dais.png](../../games/typing-defense/art-src/ui/buildings/seal-dais.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. Chấm lại 26/10: Đạt 9 (§3.3, §7). |
| U8 | [games/typing-defense/art-src/ui/tempo/tempo-0.png](../../games/typing-defense/art-src/ui/tempo/tempo-0.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U9 | [games/typing-defense/art-src/ui/tempo/tempo-6.png](../../games/typing-defense/art-src/ui/tempo/tempo-6.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U10 | [games/typing-defense/art-src/ui/tempo/tempo-4.png](../../games/typing-defense/art-src/ui/tempo/tempo-4.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U11 | [games/typing-defense/art-src/ui/tempo/tempo-3.png](../../games/typing-defense/art-src/ui/tempo/tempo-3.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U12 | [games/typing-defense/art-src/ui/tempo/tempo-2.png](../../games/typing-defense/art-src/ui/tempo/tempo-2.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U13 | [games/typing-defense/art-src/ui/tempo/tempo-1.png](../../games/typing-defense/art-src/ui/tempo/tempo-1.png) | Đã có (015b lượt 2), giữ nguyên, bỏ qua khi sinh lượt 3. P3: núm nhịp đã bỏ, không sinh thêm. |
| U14 | [games/typing-defense/art-src/ui/charms/charm-mend.png](../../games/typing-defense/art-src/ui/charms/charm-mend.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U15 | [games/typing-defense/art-src/ui/charms/charm-frost.png](../../games/typing-defense/art-src/ui/charms/charm-frost.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U16 | [games/typing-defense/art-src/ui/charms/charm-gale.png](../../games/typing-defense/art-src/ui/charms/charm-gale.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U17 | [games/typing-defense/art-src/ui/resources/lives.png](../../games/typing-defense/art-src/ui/resources/lives.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U18 | [games/typing-defense/art-src/ui/resources/gold.png](../../games/typing-defense/art-src/ui/resources/gold.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U19 | [games/typing-defense/art-src/ui/resources/food.png](../../games/typing-defense/art-src/ui/resources/food.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U20 | [games/typing-defense/art-src/ui/resources/wood.png](../../games/typing-defense/art-src/ui/resources/wood.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; việc cần sửa ở README-015b. |
| U21 | [games/typing-defense/art-src/ui/resources/knowledge.png](../../games/typing-defense/art-src/ui/resources/knowledge.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U22 | [games/typing-defense/art-src/ui/resources/wave.png](../../games/typing-defense/art-src/ui/resources/wave.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U23 | [games/typing-defense/art-src/ui/loot/coin-common.png](../../games/typing-defense/art-src/ui/loot/coin-common.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; việc cần sửa ở README-015b. |
| U24 | [games/typing-defense/art-src/ui/loot/coin-refined.png](../../games/typing-defense/art-src/ui/loot/coin-refined.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U25 | [games/typing-defense/art-src/ui/loot/coin-high.png](../../games/typing-defense/art-src/ui/loot/coin-high.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U26 | [games/typing-defense/art-src/ui/loot/coin-elite.png](../../games/typing-defense/art-src/ui/loot/coin-elite.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U27 | [games/typing-defense/art-src/ui/loot/coin-mini-boss.png](../../games/typing-defense/art-src/ui/loot/coin-mini-boss.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| U28 | [games/typing-defense/art-src/ui/loot/coin-major-boss.png](../../games/typing-defense/art-src/ui/loot/coin-major-boss.png) | Đã có (015b lượt 3), 9/10 · Đạt; việc cần sửa ở README-015b. |
| X12 | [games/typing-defense/art-src/vfx/ma-troi-sheet.png](../../games/typing-defense/art-src/vfx/ma-troi-sheet.png) | Trần 45 lượt; tham khảo tùy chọn. |

### 6.3. Lời Gọi · từng đích VS còn thiếu

Toàn bộ 200 dòng còn thiếu ở §3.4 là danh sách chuyển 015b: 110 cảnh, 12 phông, 14 chân dung, 3 ảnh trượt, 6 tranh, 48 Neon, 4 thú nền và 3 icon. Làm sau P, ưu tiên cây/khối tán/đá; giữ tham chiếu biến thể và 8 hướng. Không mở lại 119 PNG của 005a/005b2; các lỗi K04/K10/K13, V18/V32/V33/V36/V37/V42/V43/V44/V55 vẫn theo README các phiếu đó.


Cập nhật sau 015b lượt 4 (26/10/2026): **41/200 đích VS đã có PNG**, đánh dấu từng đích bên dưới; còn 159 đích P3 chờ kinh phí. Lượt 4 thêm 11 P2 bằng 11 lần sinh, không tạo lại: 7 Đạt 9/10, 4 Tạm chấp nhận 8/10. Đủ 60/60 đích P1/P2 của phiếu có PNG; thứ tự chung theo `015b-priority.md`. C21 giữ ảnh 6/10, mức Sửa từ lượt 3; có file không có nghĩa đã sẵn sàng nhập runtime. Điểm và việc cần sửa: [README-015b](../../games/typing-defense/art-src/README-015b.md).

| Mã | Đích đã có | Điểm / mức |
|---|---|---|
| C23 | [games/typing-defense/art-src/portraits/draconis-ult.png](../../games/typing-defense/art-src/portraits/draconis-ult.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| C21 | [games/typing-defense/art-src/portraits/moc-tinh.png](../../games/typing-defense/art-src/portraits/moc-tinh.png) | Đã có (015b lượt 3), 6/10 · Sửa; xem README-015b. |
| C9 | [games/typing-defense/art-src/portraits/lam.png](../../games/typing-defense/art-src/portraits/lam.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| C24 | [games/typing-defense/art-src/portraits/lam-ult.png](../../games/typing-defense/art-src/portraits/lam-ult.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| C10 | [games/typing-defense/art-src/portraits/tre.png](../../games/typing-defense/art-src/portraits/tre.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| C25 | [games/typing-defense/art-src/portraits/tre-ult.png](../../games/typing-defense/art-src/portraits/tre-ult.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| C22 | [games/typing-defense/art-src/portraits/dai-bang-tinh.png](../../games/typing-defense/art-src/portraits/dai-bang-tinh.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| U29 | [games/typing-defense/art-src/ui/buildings/scribe.png](../../games/typing-defense/art-src/ui/buildings/scribe.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| U30 | [games/typing-defense/art-src/ui/buildings/lumber.png](../../games/typing-defense/art-src/ui/buildings/lumber.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| U31 | [games/typing-defense/art-src/ui/buildings/infirmary.png](../../games/typing-defense/art-src/ui/buildings/infirmary.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S15-v1 | [games/typing-defense/art-src/scenery/coast/olive-tree-v1.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v1.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S16-v1 | [games/typing-defense/art-src/scenery/coast/casuarina-v1.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v1.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S19-v1 | [games/typing-defense/art-src/scenery/coast/limestone-small-v1.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S20-v1 | [games/typing-defense/art-src/scenery/coast/limestone-medium-v1.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S17-v1 | [games/typing-defense/art-src/scenery/coast/sea-grass-v1.png](../../games/typing-defense/art-src/scenery/coast/sea-grass-v1.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S18-v1 | [games/typing-defense/art-src/scenery/coast/morning-glory-v1.png](../../games/typing-defense/art-src/scenery/coast/morning-glory-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S21-v1 | [games/typing-defense/art-src/scenery/coast/net-rack-v1.png](../../games/typing-defense/art-src/scenery/coast/net-rack-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S22-v1 | [games/typing-defense/art-src/scenery/coast/basket-boat-v1.png](../../games/typing-defense/art-src/scenery/coast/basket-boat-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S15-v2 | [games/typing-defense/art-src/scenery/coast/olive-tree-v2.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v2.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| S16-v2 | [games/typing-defense/art-src/scenery/coast/casuarina-v2.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v2.png) | Đã có (015b lượt 3), 7/10 · Tạm chấp nhận; xem README-015b. |
| S19-v2 | [games/typing-defense/art-src/scenery/coast/limestone-small-v2.png](../../games/typing-defense/art-src/scenery/coast/limestone-small-v2.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S20-v2 | [games/typing-defense/art-src/scenery/coast/limestone-medium-v2.png](../../games/typing-defense/art-src/scenery/coast/limestone-medium-v2.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| F8 | [games/typing-defense/art-src/backdrops/w1-whitestone/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/sky-b.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| F9 | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-320.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| F10 | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-220.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| F12 | [games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-b.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S23-v1 | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v1.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v1.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S31-v1 | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v1.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v1.png) | Đã có (015b lượt 3), 8/10 · Tạm chấp nhận; xem README-015b. |
| S29-v1 | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v1.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S24-v1 | [games/typing-defense/art-src/scenery/rainforest/vine-stump-v1.png](../../games/typing-defense/art-src/scenery/rainforest/vine-stump-v1.png) | Đã có (015b lượt 3), 9/10 · Đạt; xem README-015b. |
| S25-v1 | [games/typing-defense/art-src/scenery/rainforest/tree-fern-v1.png](../../games/typing-defense/art-src/scenery/rainforest/tree-fern-v1.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| S26-v1 | [games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v1.png](../../games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v1.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| S27-v1 | [games/typing-defense/art-src/scenery/rainforest/root-tangle-v1.png](../../games/typing-defense/art-src/scenery/rainforest/root-tangle-v1.png) | Đã có (015b lượt 4), 8/10 · Tạm chấp nhận; xem README-015b. |
| S28-v1 | [games/typing-defense/art-src/scenery/rainforest/orchid-clump-v1.png](../../games/typing-defense/art-src/scenery/rainforest/orchid-clump-v1.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| S23-v2 | [games/typing-defense/art-src/scenery/rainforest/jungle-tree-v2.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-tree-v2.png) | Đã có (015b lượt 4), 8/10 · Tạm chấp nhận; xem README-015b. |
| S31-v2 | [games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v2.png](../../games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v2.png) | Đã có (015b lượt 4), 8/10 · Tạm chấp nhận; xem README-015b. |
| S29-v2 | [games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v2.png](../../games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v2.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| F14 | [games/typing-defense/art-src/backdrops/w1-rootwood/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/sky-b.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| F15 | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-320.png) | Đã có (015b lượt 4), 8/10 · Tạm chấp nhận; xem README-015b. |
| F16 | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-220.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |
| F18 | [games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-b.png) | Đã có (015b lượt 4), 9/10 · Đạt; xem README-015b. |

### 6.4. Quy cách chưa khóa và chủ dự án cần xem

Chốt nhu cầu bitmap cho 27 ký hiệu/khung và 2 nhóm đất/tán ở §3.5, cùng 4 ký hiệu nguyên tố S2 nếu muốn dùng PNG. Duyệt ảnh và bảng 3D trước khi thay model/ảnh chạy. Không tạo âm, không chạy Git, build, test, game, art-normalize; không sửa mã, không nhập runtime, không tạo GLB hoặc chi credit Tripo.

### Tổng cuối phiếu theo game

| Game | PNG đã định danh còn thiếu | Chất lượng / phần chưa chốt |
|---|---|---|
| Rồng Giữ Ải | 0 | 0 ảnh thiếu mới; lỗi ảnh M0 và 8 ứng viên sửa vẫn theo README-015. |
| Lời Gọi | 160 (lúc kiểm 25/10: 248) | 1 P (X12, P3) + 159 VS (đều P3, chờ kinh phí); đã có 47 P + 41 VS sau 015b lượt 4. Đủ PNG cho 60/60 đích P1/P2; lượt 4 thêm 11 ảnh từ 8 điểm. C21 6/10 cần sửa, các giới hạn khác ở README-015b. 27 ký hiệu/khung và 2 nhóm đất/tán chưa chốt raster. |
| Tuyến Cuối | 0 | Đủ 7 PNG tựa/icon; 6 icon gồm 2 cũ còn sai khổ/lề; 4 nguyên tố S2 chưa có hợp đồng PNG. |

Bàn giao 015: **45 lượt image_gen / 34 đích ảnh** (8 Rồng, 21 Lời Gọi, 5 Tuyến Cuối), gồm 11 lần thử lại. Mỗi PNG có đúng prompt cạnh ảnh; các bản đầu được giữ .v1.png. Có 8 JPEG xem nhanh trong art-src/_review của ba game. Dừng đúng trần, không coi các lỗi còn lại là đã đạt.

## 7. Chấm lại theo luật 7 điểm (26/10/2026)

Chủ dự án, 26/10/2026: làm 2D và 3D rất đắt, nên ảnh hoặc model từ 7 điểm trở lên được nhận; chỉ tạo lại khi sai quá, không sửa được.
Ảnh tạm chấp nhận phải ghi lại để có kinh phí thì thay; làm ảnh cần thiết trước.

- Luật, thang 5 tiêu chí × 0–2 điểm, bốn mức và mức cần P1–P3: [ART_ACCEPTANCE.md](ART_ACCEPTANCE.md).
- Ảnh, model tạm chấp nhận và cách thay: [ART_REPLACE_LATER.md](ART_REPLACE_LATER.md).
- Ảnh mức Sửa và Tạo lại: [ART_FIX_QUEUE.md](ART_FIX_QUEUE.md). Lượt chấm đầu không có mục nào dưới 7. Lượt chấm thêm 8 mục Lời Gọi (V14, V15, V34, V35, U4–U7) có hai mục Tạo lại P2 (V34, V35), ghi ở §3 của file đó; không có mục Sửa.
- Thứ tự làm ảnh 015b của Lời Gọi: [015b-priority.md](../../games/typing-defense/docs/art-requests/td/015b-priority.md).

Cột trạng thái ở §2–§4 nay ghi mức và điểm, thay "Có nhưng lỗi" hoặc "Thiếu". Ghi chú cũ giữ nguyên; phần "Chấm lại 26/10" nối vào cuối ô. Mỗi mục có hai người chấm độc lập ở cỡ hiện trong game; 32 mục có thêm người chấm thứ ba (29 ở lượt đầu; V15, V34, V35 ở lượt chấm thêm). Mục đã có model thì chấm model trên ảnh render bốn góc; ảnh nguồn chỉ cần làm lại nếu model phải dựng lại.

### 7.1. Số mục theo game và mức

Một mục là một mã; mục có hai góc hoặc model dùng chung ứng với nhiều dòng.

| Game | Mục | Dòng | Đạt | Tạm chấp nhận | Sửa | Tạo lại |
|---|---:|---:|---:|---:|---:|---:|
| Rồng Giữ Ải | 57 | 65 | 43 | 14 | 0 | 0 |
| Lời Gọi | 71 | 71 | 47 | 22 | 0 | 2 |
| Tuyến Cuối | 8 | 9 | 2 | 6 | 0 | 0 |
| **Tổng** | **136** | **145** | **92** | **42** | **0** | **2** |

Lời Gọi gồm 63 mục lượt đầu và 8 mục chấm thêm 26/10: U5, U6, U7 Đạt; U4, V14, V15 Tạm chấp nhận; V34, V35 Tạo lại (cả hai P2, [ART_FIX_QUEUE.md](ART_FIX_QUEUE.md) §3).

Mục tạm chấp nhận theo mức cần:

| Game | P1 | P2 | P3 | Mục |
|---|---:|---:|---:|---|
| Rồng Giữ Ải | 14 | 0 | 0 | E01, U1, K03, K04, K07, T2, T3, T7, T8, D2, D3, D4, I08, I11 |
| Lời Gọi | 2 | 18 | 2 | P1: U2, U4. P2: S2-v2, S3-v1, S4-v1, S4-v2, S5-v1, S6-v2, S12-v1, S12-v2, S13-v1, S13-v2, F5, F6, V14, V15, V18, V36, V37, V69. P3: V43, V59 |
| Tuyến Cuối | 1 | 1 | 4 | P1: rainbow-tank (Lính, Trâu, Đầu Đàn). P2: nova. P3: title-horizon, gun-tan, gun-ray, gun-phao-sao |

Mức cần của mười hai ảnh nguồn 3D VS (K04, K10, K13, V14, V15, V18, V34, V35, V36, V37, V68, V69) là P2, khớp [INDEX đợt 2](../../typing-game-handoff-2026-10-25/tripo-upload-dot2/INDEX.md) (P2 #10, #14–16, #26, #27, #36–41): cùng nhóm tổ thợ, bộ cấp, nhánh nhà bản đồ 1, Đại Bàng Tinh, Mộc Tinh đầy đủ. Bước trước Tripo của V18, V37, V69 ([ART_FIX_QUEUE.md](ART_FIX_QUEUE.md) §5.1) phải xong trước khi gửi.

Việc không tốn kinh phí trước khi dùng ghi ở ô ghi chú từng dòng. Ví dụ: xoay cánh E01, tách cán cờ G01, xóa chùy và nửa khiên thừa U1, sửa vật liệu K03, K04, K07 trong Blender; art-normalize cho D2, I09–I12 và ảnh 2D Lời Gọi, Tuyến Cuối; tô tối miệng lò V37.

### 7.2. Thay đổi so với §5–§6

- **Rồng Giữ Ải:** 65 dòng "Có nhưng lỗi" ở §2 đều từ 7,5 điểm; không ảnh nào phải tạo lại. Ứng viên 015 được chọn: D2 và I09–I12 (bản trong `_review`). Các đích khác dùng bản gốc hoặc bản 012d (`.alpha`, `.seamless`, `icons/normalized`). Quyết định từng đích của phiếu 015: [015-m0b-fixes.md](dragon-lane/art-requests/015-m0b-fixes.md).
- **Lời Gọi:** 26 đích P ghi "Thiếu" ở §3.3 và §6.2 nay đã có và đã chấm theo luật 7 điểm: 22 ở 015b lượt 1, U4–U7 (lượt 2) chấm thêm 26/10. Sau lượt 2–3, 47/48 đích P có PNG, chỉ còn thiếu X12 (tham khảo tùy chọn, P3); 21 đích P mới khác (U8–U28) mới có điểm Codex tự chấm ở README-015b, chưa chấm lại ở đây. Ảnh VS dùng thẳng ở §3.4: 30/200 có PNG sau lượt 3 (§6.3), chưa chấm lại ở đây. Đã chấm 23 dòng nguồn 3D VS ở §3.2: K04, K10, K13, V18, V23, V32, V33, V36, V37, V42, V43, V44, V55, V58, V59, V60, V61, V68, V69, và V14, V15, V34, V35 (chấm thêm 26/10).
- **Tuyến Cuối:** màn tựa, 6 icon và model rainbow-tank đã chấm. Còn đổi khổ, đệm lề khi lắp và xem model trong trận.

### 7.3. Dòng không tìm thấy và dòng chưa chấm

- **Không tìm thấy:** không có. Mọi kết quả đều khớp dòng theo mã và đường dẫn.
- **Hai mục là model, không có dòng riêng:**
  - P5 Trại Lính: model art-src `barracks.glb` dựng lại từ `barracks-v2.png`; điểm ghi ở dòng `buildings/barracks-v2` (§3.1). Dòng `buildings/barracks` giữ "Đã có", chỉ thêm ghi chú.
  - Model `rainbow-tank.glb` trong kho Space: điểm ghi ở hai dòng Lính Rainbow và Trâu / Đầu Đàn (§4.1).
- **Chưa chấm lại, còn ghi "Có nhưng lỗi":** 37 dòng nguồn 3D VS ở §3.2: V16, V17, V19–V22, V24–V31, V38–V41, V45–V54, V56, V57, V62–V67, V70. README chỉ ghi nền chưa phẳng, sửa được bằng art-normalize; cần chấm trước khi gửi Tripo.
- **Bốn ảnh Trại Lính VS (P2, chấm thêm 26/10):** V14, V15, V34, V35 vẽ theo `barracks.png` cũ (nhà dài thấp), nên được chấm so với `barracks-v2.png` và render `barracks.glb`: hai người độc lập, thêm người thứ ba cho V15, V34, V35.
  - V14 bộ cấp 2: Tạm chấp nhận 8. V15 bộ cấp 3: Tạm chấp nhận 8. Gửi Tripo ảnh hiện có (face 4000, không rig); sau đó trong Blender đặt chòi V14 vào dải sân phải trong rào, chỉnh tỉ lệ từng trục cho mái V15 chụp kín mái rơm, render ba góc trên `barracks.glb` rồi chấm lại ([ART_FIX_QUEUE.md](ART_FIX_QUEUE.md) §5). Ghi ở [ART_REPLACE_LATER.md](ART_REPLACE_LATER.md).
  - V34 nhánh Khiên Đồng: Tạo lại 6,5. V35 nhánh Giáo Dài: Tạo lại 5,5. Cùng bề ngang chân, cả hai chỉ cao khoảng nửa tháp v2; phóng theo vòng Ø 4,6 m thì cao khoảng 2 m, mà luật 02 §8 cấm kéo dãn riêng chiều cao. Không gửi Tripo; vẽ lại 2D một lần theo `barracks-v2.png` ([ART_FIX_QUEUE.md](ART_FIX_QUEUE.md) §3). Hai ảnh hiện có giữ làm mẫu chi tiết và bản dự phòng (từ 5 điểm). **27/10, đã vẽ lại một lần (Codex 015c):** V34 bản mới 8, V35 bản mới 7,5, cả hai tạm chấp nhận, cao 79 % và 77 % tháp v2 cùng bề ngang chân; ảnh trong `tripo-upload-dot2` đã thay bằng bản mới, gửi Tripo được. Bản 26/10 giữ đuôi `.v1.png`.
- **Chưa chấm lại, ghi "Đã có":** HT-A, HT-B (§2); nguồn 3D P ở §3.1; các dòng "Đã có" ở §3.2; C1, C2, C8, X1–X11 và màn tựa ở §3.3; Khiên, Tách, Tổ, Bầy lao, Boss Cai Ngục ở §4.1.

**27/10, luật 2D từ 8 điểm (chủ dự án):** chỉ model 3D giữ luật 7 điểm. Ảnh 2D 8–8,5 ở các bảng trên là Đạt. Ảnh 2D dưới 8 (T3, C9, C10, C22, C23, C25, S15-v2, S16-v2, V35, cùng C21) phải sửa hoặc tạo lại: [ART_FIX_QUEUE.md](ART_FIX_QUEUE.md) §3b, phiếu Codex 020.
