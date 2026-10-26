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
| E09-F | E09 Yêu Rêu Lính · ảnh chính, nhìn thẳng | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/moss-grunt.png](../../games/dragon-hold/art-src/enemies/moss-grunt.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E09-B | E09 · nhìn sau | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/moss-grunt-back.png](../../games/dragon-hold/art-src/enemies/moss-grunt-back.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E18-S | E18 Sói Mục · ảnh chính, nhìn ngang | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/blight-wolf.png](../../games/dragon-hold/art-src/enemies/blight-wolf.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E18-F | E18 · nhìn thẳng | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/blight-wolf-front.png](../../games/dragon-hold/art-src/enemies/blight-wolf-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E01-F | E01 Ong Gai · ảnh chính, nhìn thẳng | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/thorn-wasp.png](../../games/dragon-hold/art-src/enemies/thorn-wasp.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E01-S | E01 · nhìn ngang | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/thorn-wasp-side.png](../../games/dragon-hold/art-src/enemies/thorn-wasp-side.png)<br>Ứng viên: [games/dragon-hold/art-src/enemies/thorn-wasp-side-015.png](../../games/dragon-hold/art-src/enemies/thorn-wasp-side-015.png) | 015 thử thêm đúng 1 lần; vẫn lộ mặt cánh. Không dùng ô Left; dùng Front riêng nếu dựng. |
| E11-F | E11 Yêu Rêu Cung · ảnh chính | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/moss-archer.png](../../games/dragon-hold/art-src/enemies/moss-archer.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E11-B | E11 · nhìn sau | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/moss-archer-back.png](../../games/dragon-hold/art-src/enemies/moss-archer-back.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E19-S | E19 Heo Nanh Đá · ảnh chính, nhìn ngang | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/tusk-boar.png](../../games/dragon-hold/art-src/enemies/tusk-boar.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E19-F | E19 · nhìn thẳng | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/tusk-boar-front.png](../../games/dragon-hold/art-src/enemies/tusk-boar-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E25-S | E25 Kiến Gai · ảnh chính, nhìn ngang | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/thorn-ant.png](../../games/dragon-hold/art-src/enemies/thorn-ant.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| E25-F | E25 · nhìn thẳng | Có nhưng lỗi | [games/dragon-hold/art-src/enemies/thorn-ant-front.png](../../games/dragon-hold/art-src/enemies/thorn-ant-front.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| G01-F | G01 Yêu Rêu Cầm Cờ · ảnh chính | Có nhưng lỗi | [games/dragon-hold/art-src/generals/moss-banner.png](../../games/dragon-hold/art-src/generals/moss-banner.png)<br>Ứng viên: [games/dragon-hold/art-src/generals/moss-banner-015.png](../../games/dragon-hold/art-src/generals/moss-banner-015.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. |
| G01-B | G01 · nhìn sau | Có nhưng lỗi | [games/dragon-hold/art-src/generals/moss-banner-back.png](../../games/dragon-hold/art-src/generals/moss-banner-back.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. |
| TR1 | Gai Chông `spikes` | Có nhưng lỗi | [games/dragon-hold/art-src/traps/spikes.png](../../games/dragon-hold/art-src/traps/spikes.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| TR2 | Bom Hạt Thông `pine-bomb` | Có nhưng lỗi | [games/dragon-hold/art-src/traps/pine-bomb.png](../../games/dragon-hold/art-src/traps/pine-bomb.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| TR3 | Lưới Phóng `net-launcher` | Có nhưng lỗi | [games/dragon-hold/art-src/traps/net-launcher.png](../../games/dragon-hold/art-src/traps/net-launcher.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| U1-F | Vệ Binh Rêu `moss-warden` · ảnh chính | Có nhưng lỗi | [games/dragon-hold/art-src/units/moss-warden.png](../../games/dragon-hold/art-src/units/moss-warden.png)<br>Ứng viên: [games/dragon-hold/art-src/units/moss-warden-015.png](../../games/dragon-hold/art-src/units/moss-warden-015.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. |
| U1-B | Vệ Binh Rêu · nhìn sau | Có nhưng lỗi | [games/dragon-hold/art-src/units/moss-warden-back.png](../../games/dragon-hold/art-src/units/moss-warden-back.png) | 006 còn lỗi tay/mặt khiên; 015 thử Front 2 lượt, chưa đạt đủ. Không sinh Back mới kế thừa lỗi. |
| H1 | Lều Thuốc Nam `herb-hut` | Có nhưng lỗi | [games/dragon-hold/art-src/houses/herb-hut.png](../../games/dragon-hold/art-src/houses/herb-hut.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K01 | Thông cao | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/pine-tall.png](../../games/dragon-hold/art-src/props/pine-river/pine-tall.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K02 | Thông dù già | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/pine-round.png](../../games/dragon-hold/art-src/props/pine-river/pine-round.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K03 | Thông non | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/pine-young.png](../../games/dragon-hold/art-src/props/pine-river/pine-young.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K04 | Cây tán tím (xa đường) | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/tree-violet.png](../../games/dragon-hold/art-src/props/pine-river/tree-violet.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K05 | Bụi rêu | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/bush-moss.png](../../games/dragon-hold/art-src/props/pine-river/bush-moss.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K06 | Bụi hoa kem, tím | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/bush-blossom.png](../../games/dragon-hold/art-src/props/pine-river/bush-blossom.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K07 | Đá tảng rêu | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/rock-boulder.png](../../games/dragon-hold/art-src/props/pine-river/rock-boulder.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K08 | Gờ đá phiến | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/rock-slab.png](../../games/dragon-hold/art-src/props/pine-river/rock-slab.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K09 | Đá kê suối | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/river-stones.png](../../games/dragon-hold/art-src/props/pine-river/river-stones.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K10 | Gốc thông | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/stump.png](../../games/dragon-hold/art-src/props/pine-river/stump.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K11 | Khúc gỗ đổ | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/log.png](../../games/dragon-hold/art-src/props/pine-river/log.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| K12 | Cầu gỗ cũ (mốc) | Có nhưng lỗi | [games/dragon-hold/art-src/props/pine-river/bridge-old.png](../../games/dragon-hold/art-src/props/pine-river/bridge-old.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| T1 | Cỏ xuân A (chính) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/grass-a.png](../../games/dragon-hold/art-src/ground/pine-river/grass-a.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T2 | Cỏ xuân B (trộn với A) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/grass-b.png](../../games/dragon-hold/art-src/ground/pine-river/grass-b.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T3 | Rêu dưới tán | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/moss.png](../../games/dragon-hold/art-src/ground/pine-river/moss.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T4 | Lối mòn (đường quái, sáng hơn cỏ một bậc) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/path.png](../../games/dragon-hold/art-src/ground/pine-river/path.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T5 | Đất nện (quanh Bệ Rồng, ô xây) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/earth.png](../../games/dragon-hold/art-src/ground/pine-river/earth.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T6 | Cát ven suối | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/river-sand.png](../../games/dragon-hold/art-src/ground/pine-river/river-sand.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T7 | Đá rêu (dốc > 35°, chiếu ba mặt) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/rock.png](../../games/dragon-hold/art-src/ground/pine-river/rock.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| T8 | Lá thông rụng (rìa rừng) | Có nhưng lỗi | [games/dragon-hold/art-src/ground/pine-river/pine-litter.png](../../games/dragon-hold/art-src/ground/pine-river/pine-litter.png) | README 1–3: khổ và mép lặp chưa đạt chuẩn pixel; cần duyệt trong bản đồ. |
| D1 | Decal vết đất (G) | Có nhưng lỗi | [games/dragon-hold/art-src/decals/pine-river/dirt-patches.png](../../games/dragon-hold/art-src/decals/pine-river/dirt-patches.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/dirt-patches-015.png](../../games/dragon-hold/art-src/decals/pine-river/dirt-patches-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. |
| D2 | Decal cụm hoa (B) | Có nhưng lỗi | [games/dragon-hold/art-src/decals/pine-river/flower-clusters.png](../../games/dragon-hold/art-src/decals/pine-river/flower-clusters.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/flower-clusters-015.png](../../games/dragon-hold/art-src/decals/pine-river/flower-clusters-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. |
| D3 | Decal sỏi, lá, kim thông, cành (G) | Có nhưng lỗi | [games/dragon-hold/art-src/decals/pine-river/forest-litter.png](../../games/dragon-hold/art-src/decals/pine-river/forest-litter.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/forest-litter-015.png](../../games/dragon-hold/art-src/decals/pine-river/forest-litter-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. |
| D4 | Decal rêu, vũng nước (M) | Có nhưng lỗi | [games/dragon-hold/art-src/decals/pine-river/moss-puddles.png](../../games/dragon-hold/art-src/decals/pine-river/moss-puddles.png)<br>Ứng viên: [games/dragon-hold/art-src/decals/pine-river/moss-puddles-015.png](../../games/dragon-hold/art-src/decals/pine-river/moss-puddles-015.png) | 006 còn lỗi lề/nền; có ứng viên 015. Xem số đo và giới hạn ở README-015. |
| B1 | Phông xa rừng thông | Có nhưng lỗi | [games/dragon-hold/art-src/backdrops/pine-river-far.png](../../games/dragon-hold/art-src/backdrops/pine-river-far.png)<br>Ứng viên: [games/dragon-hold/art-src/backdrops/pine-river-far-015.png](../../games/dragon-hold/art-src/backdrops/pine-river-far-015.png) | 006 còn lỗi mép và chi tiết; 015 thử 2 lượt, chưa xác nhận đạt lặp. |
| I01 | Gai Chông | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/spikes.png](../../games/dragon-hold/art-src/ui/icons/spikes.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I02 | Bom Hạt Thông | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/pine-bomb.png](../../games/dragon-hold/art-src/ui/icons/pine-bomb.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I03 | Lưới Phóng | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/net-launcher.png](../../games/dragon-hold/art-src/ui/icons/net-launcher.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I04 | Vệ Binh Rêu | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/moss-warden.png](../../games/dragon-hold/art-src/ui/icons/moss-warden.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I05 | Lều Thuốc Nam | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/herb-hut.png](../../games/dragon-hold/art-src/ui/icons/herb-hut.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I06 | Bình Máu Nhỏ | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/potion-small.png](../../games/dragon-hold/art-src/ui/icons/potion-small.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I07 | Tim Rồng (trang bị) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/dragon-heart.png](../../games/dragon-hold/art-src/ui/icons/dragon-heart.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I08 | Vảy Cứng (trang bị) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/hard-scale.png](../../games/dragon-hold/art-src/ui/icons/hard-scale.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I09 | Phun Lửa (Alt + 1) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/skill-fire-breath.png](../../games/dragon-hold/art-src/ui/icons/skill-fire-breath.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I10 | Thiên Hỏa (Alt + 2) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/skill-sky-fire.png](../../games/dragon-hold/art-src/ui/icons/skill-sky-fire.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I11 | Long Hống (Từ Khẩn) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/skill-roar.png](../../games/dragon-hold/art-src/ui/icons/skill-roar.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I12 | Long Nộ / Viêm Đế | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/skill-ultimate.png](../../games/dragon-hold/art-src/ui/icons/skill-ultimate.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I13 | Vàng | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/gold.png](../../games/dragon-hold/art-src/ui/icons/gold.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I14 | Họ Yêu Rêu | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/family-moss.png](../../games/dragon-hold/art-src/ui/icons/family-moss.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I15 | Họ Thú Mục | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/family-beast.png](../../games/dragon-hold/art-src/ui/icons/family-beast.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I16 | Họ Bọ Gai | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/family-bug.png](../../games/dragon-hold/art-src/ui/icons/family-bug.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I17 | Huy hiệu tướng địch | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/enemy-general.png](../../games/dragon-hold/art-src/ui/icons/enemy-general.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I18 | Hào quang tốc (Xung Phong) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/aura-speed.png](../../games/dragon-hold/art-src/ui/icons/aura-speed.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I19 | Hào quang đòn (Cắm Cờ) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/aura-attack.png](../../games/dragon-hold/art-src/ui/icons/aura-attack.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |
| I20 | Gọi sớm (tù và) | Có nhưng lỗi | [games/dragon-hold/art-src/ui/icons/call-wave.png](../../games/dragon-hold/art-src/ui/icons/call-wave.png) | README cũ ghi nền/khổ hoặc chi tiết chưa đạt; không lấy bản chuẩn hóa 012 làm bằng chứng đạt. |

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
| buildings/barracks | Đã có | [games/typing-defense/art-src/buildings/barracks.png](../../games/typing-defense/art-src/buildings/barracks.png) | Bản cũ thấp 1,8 m, giữ đối chiếu; thay bằng barracks-v2. |
| buildings/barracks-v2 | Đã có | [games/typing-defense/art-src/buildings/barracks-v2.png](../../games/typing-defense/art-src/buildings/barracks-v2.png) | Đã có ảnh làm lại; bảng 3D trước 015 còn ghi chờ ảnh là thông tin cũ. |
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
| K04 | Có nhưng lỗi | [games/typing-defense/art-src/workers/worker-kit-en-bow.png](../../games/typing-defense/art-src/workers/worker-kit-en-bow.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. |
| K10 | Có nhưng lỗi | [games/typing-defense/art-src/workers/worker-kit-lua-shot.png](../../games/typing-defense/art-src/workers/worker-kit-lua-shot.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. |
| K13 | Có nhưng lỗi | [games/typing-defense/art-src/workers/worker-kit-sam-drumstick.png](../../games/typing-defense/art-src/workers/worker-kit-sam-drumstick.png) | 005a/005b2 đã làm, 015 bỏ qua. Còn lỗi ghi trong README giao nhận. |
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
| V14 | Có nhưng lỗi | [games/typing-defense/art-src/kits/barracks-kit-l2.png](../../games/typing-defense/art-src/kits/barracks-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V15 | Có nhưng lỗi | [games/typing-defense/art-src/kits/barracks-kit-l3.png](../../games/typing-defense/art-src/kits/barracks-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V16 | Có nhưng lỗi | [games/typing-defense/art-src/kits/gold-mine-kit-l2.png](../../games/typing-defense/art-src/kits/gold-mine-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V17 | Có nhưng lỗi | [games/typing-defense/art-src/kits/gold-mine-kit-l3.png](../../games/typing-defense/art-src/kits/gold-mine-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V18 | Có nhưng lỗi | [games/typing-defense/art-src/kits/farm-kit-l2.png](../../games/typing-defense/art-src/kits/farm-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V19 | Có nhưng lỗi | [games/typing-defense/art-src/kits/farm-kit-l3.png](../../games/typing-defense/art-src/kits/farm-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V20 | Có nhưng lỗi | [games/typing-defense/art-src/kits/seal-dais-kit-l2.png](../../games/typing-defense/art-src/kits/seal-dais-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V21 | Có nhưng lỗi | [games/typing-defense/art-src/kits/seal-dais-kit-l3.png](../../games/typing-defense/art-src/kits/seal-dais-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V22 | Có nhưng lỗi | [games/typing-defense/art-src/kits/scribe-kit-l2.png](../../games/typing-defense/art-src/kits/scribe-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V23 | Có nhưng lỗi | [games/typing-defense/art-src/kits/scribe-kit-l3.png](../../games/typing-defense/art-src/kits/scribe-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V24 | Có nhưng lỗi | [games/typing-defense/art-src/kits/infirmary-kit-l2.png](../../games/typing-defense/art-src/kits/infirmary-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V25 | Có nhưng lỗi | [games/typing-defense/art-src/kits/infirmary-kit-l3.png](../../games/typing-defense/art-src/kits/infirmary-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V26 | Có nhưng lỗi | [games/typing-defense/art-src/kits/lumber-kit-l2.png](../../games/typing-defense/art-src/kits/lumber-kit-l2.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V27 | Có nhưng lỗi | [games/typing-defense/art-src/kits/lumber-kit-l3.png](../../games/typing-defense/art-src/kits/lumber-kit-l3.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V28 | Có nhưng lỗi | [games/typing-defense/art-src/branches/archer-en-bao.png](../../games/typing-defense/art-src/branches/archer-en-bao.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V29 | Có nhưng lỗi | [games/typing-defense/art-src/branches/archer-than-tien.png](../../games/typing-defense/art-src/branches/archer-than-tien.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V30 | Có nhưng lỗi | [games/typing-defense/art-src/branches/cannon-coi-lon.png](../../games/typing-defense/art-src/branches/cannon-coi-lon.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V31 | Có nhưng lỗi | [games/typing-defense/art-src/branches/cannon-vac-lua.png](../../games/typing-defense/art-src/branches/cannon-vac-lua.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V32 | Có nhưng lỗi | [games/typing-defense/art-src/branches/scribe-but-loi.png](../../games/typing-defense/art-src/branches/scribe-but-loi.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V33 | Có nhưng lỗi | [games/typing-defense/art-src/branches/scribe-muc-bang.png](../../games/typing-defense/art-src/branches/scribe-muc-bang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V34 | Có nhưng lỗi | [games/typing-defense/art-src/branches/barracks-khien-dong.png](../../games/typing-defense/art-src/branches/barracks-khien-dong.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V35 | Có nhưng lỗi | [games/typing-defense/art-src/branches/barracks-giao-dai.png](../../games/typing-defense/art-src/branches/barracks-giao-dai.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V36 | Có nhưng lỗi | [games/typing-defense/art-src/branches/gold-mine-ham-sau.png](../../games/typing-defense/art-src/branches/gold-mine-ham-sau.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V37 | Có nhưng lỗi | [games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V38 | Có nhưng lỗi | [games/typing-defense/art-src/branches/farm-bac-thang.png](../../games/typing-defense/art-src/branches/farm-bac-thang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V39 | Có nhưng lỗi | [games/typing-defense/art-src/branches/farm-chuong-trau.png](../../games/typing-defense/art-src/branches/farm-chuong-trau.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V40 | Có nhưng lỗi | [games/typing-defense/art-src/branches/lumber-xuong-cua.png](../../games/typing-defense/art-src/branches/lumber-xuong-cua.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V41 | Có nhưng lỗi | [games/typing-defense/art-src/branches/lumber-xuong-rao.png](../../games/typing-defense/art-src/branches/lumber-xuong-rao.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V42 | Có nhưng lỗi | [games/typing-defense/art-src/branches/seal-dais-phong-an.png](../../games/typing-defense/art-src/branches/seal-dais-phong-an.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V43 | Có nhưng lỗi | [games/typing-defense/art-src/branches/seal-dais-vang-am.png](../../games/typing-defense/art-src/branches/seal-dais-vang-am.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V44 | Có nhưng lỗi | [games/typing-defense/art-src/branches/infirmary-vuon-thao-duoc.png](../../games/typing-defense/art-src/branches/infirmary-vuon-thao-duoc.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
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
| V55 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/nha-rai-da.png](../../games/typing-defense/art-src/landmarks/nha-rai-da.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. Còn lỗi hình. |
| V56 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/them-da-trang.png](../../games/typing-defense/art-src/landmarks/them-da-trang.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V57 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/goc-da-rong.png](../../games/typing-defense/art-src/landmarks/goc-da-rong.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V58 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/cau-do.png](../../games/typing-defense/art-src/landmarks/cau-do.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V59 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/da-ke.png](../../games/typing-defense/art-src/landmarks/da-ke.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V60 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/re-vom.png](../../games/typing-defense/art-src/landmarks/re-vom.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V61 | Có nhưng lỗi | [games/typing-defense/art-src/landmarks/thac-ho-sut.png](../../games/typing-defense/art-src/landmarks/thac-ho-sut.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V62 | Có nhưng lỗi | [games/typing-defense/art-src/props/scaffold-bamboo.png](../../games/typing-defense/art-src/props/scaffold-bamboo.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V63 | Có nhưng lỗi | [games/typing-defense/art-src/props/rao-tre.png](../../games/typing-defense/art-src/props/rao-tre.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V64 | Có nhưng lỗi | [games/typing-defense/art-src/props/cau-tre.png](../../games/typing-defense/art-src/props/cau-tre.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V65 | Có nhưng lỗi | [games/typing-defense/art-src/props/go-lan.png](../../games/typing-defense/art-src/props/go-lan.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V66 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/pebble.png](../../games/typing-defense/art-src/projectiles/pebble.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V67 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/meteor.png](../../games/typing-defense/art-src/projectiles/meteor.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V68 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/quill.png](../../games/typing-defense/art-src/projectiles/quill.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V69 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/seed-drop.png](../../games/typing-defense/art-src/projectiles/seed-drop.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |
| V70 | Có nhưng lỗi | [games/typing-defense/art-src/projectiles/fire-feather.png](../../games/typing-defense/art-src/projectiles/fire-feather.png) | README: nền nhóm ảnh mới chưa phẳng; giữ nguyên phần 005b/005b2. |

### 3.3. Ảnh dùng thẳng P

83 ảnh = 26 cảnh/decal + 6 phông + 8 chân dung + 3 đèn lồng + 28 icon + 12 VFX. X12 là tham khảo tùy chọn. Trước 015 có 14/83 (3 chân dung, 11 VFX); màn tựa tính riêng. Prompt có sẵn chưa được tính là ảnh.

| Mã | Nội dung | Trạng thái | Đích / ảnh | Ghi chú |
|---|---|---|---|---|
| S1-v1 | Cây bàng · cây to, tán xếp tầng ngang | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/almond-tree-v1.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S1-v2 | Cây bàng · cây to, tán xếp tầng ngang | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/almond-tree-v2.png](../../games/typing-defense/art-src/scenery/meadow/almond-tree-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S2-v1 | Thông núi · cây cao, tán thành đệm tròn | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v1.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S2-v2 | Thông núi · cây cao, tán thành đệm tròn | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/mountain-pine-v2.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S3-v1 | Khóm tre · bụi tre làng, ngọn cong | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S3-v2 | Khóm tre · bụi tre làng, ngọn cong | Thiếu | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png) | Còn lại 015b; prompt ở file 03. |
| S4-v1 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v1.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S4-v2 | Bụi mâm xôi · bụi tròn có quả đỏ hồng | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/raspberry-bush-v2.png](../../games/typing-defense/art-src/scenery/meadow/raspberry-bush-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S5-v1 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/tall-grass-v1.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S5-v2 | Cỏ cao · bụi cỏ gần camera (hai tấm chéo) | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/tall-grass-v2.png](../../games/typing-defense/art-src/scenery/meadow/tall-grass-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S6-v1 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/reed-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S6-v2 | Cỏ lau · bụi lau bờ suối, bông trắng bạc | Thiếu | [games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png) | Còn lại 015b; prompt ở file 03. |
| S7-v1 | Hoa dại trắng vàng · khóm hoa thấp | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/wildflowers-v1.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S7-v2 | Hoa dại trắng vàng · khóm hoa thấp | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/wildflowers-v2.png](../../games/typing-defense/art-src/scenery/meadow/wildflowers-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S8-v1 | Dương xỉ · khóm lá xòe bờ ẩm | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/fern-v1.png](../../games/typing-defense/art-src/scenery/meadow/fern-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S8-v2 | Dương xỉ · khóm lá xòe bờ ẩm | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/fern-v2.png](../../games/typing-defense/art-src/scenery/meadow/fern-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S9-v1 | Đá xám rêu nhỏ | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rock-small-v1.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S9-v2 | Đá xám rêu nhỏ | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rock-small-v2.png](../../games/typing-defense/art-src/scenery/meadow/rock-small-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S10-v1 | Đá xám rêu vừa · tảng đá to | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rock-medium-v1.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S10-v2 | Đá xám rêu vừa · tảng đá to | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rock-medium-v2.png](../../games/typing-defense/art-src/scenery/meadow/rock-medium-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S11-v1 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rotten-log-v1.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S11-v2 | Khúc gỗ mục · thân cây đổ có rêu, nấm | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/rotten-log-v2.png](../../games/typing-defense/art-src/scenery/meadow/rotten-log-v2.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S12-v1 | Khối tán · bức tường tán cây ở mép rừng | Có nhưng lỗi | [games/typing-defense/art-src/scenery/meadow/canopy-block-v1.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v1.png) | 015: nền khóa màu còn dao động; có ảnh sai khổ. Xem README-015; chưa nhập runtime. |
| S12-v2 | Khối tán · bức tường tán cây ở mép rừng | Thiếu | [games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png) | Còn lại 015b; prompt ở file 03. |
| S13-v1 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Thiếu | [games/typing-defense/art-src/scenery/shared/tree-stump-v1.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v1.png) | Còn lại 015b; prompt ở file 03. |
| S13-v2 | Gốc cây · decal nhìn từ trên, còn lại khi đặt nhà phá cây; dùng chung mọi vùng | Thiếu | [games/typing-defense/art-src/scenery/shared/tree-stump-v2.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v2.png) | Còn lại 015b; prompt ở file 03. |
| F1 | Dải trời có cầu vồng | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png) | Còn lại 015b; prompt ở file 03. |
| F2 | Dải trời mây sáng | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png) | Còn lại 015b; prompt ở file 03. |
| F3 | Núi xa lam nhạt | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png) | Còn lại 015b; prompt ở file 03. |
| F4 | Đồi rừng xanh lam, vách đá vôi | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png) | Còn lại 015b; prompt ở file 03. |
| F5 | Đồi chè có cối xay gió | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png) | Còn lại 015b; prompt ở file 03. |
| F6 | Đồi chè trơn | Thiếu | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png) | Còn lại 015b; prompt ở file 03. |
| C1 | Draconis, Tướng ô 1 (dáng ảnh 3.png, LOOK-DRACONIS) | Đã có | [games/typing-defense/art-src/portraits/draconis.png](../../games/typing-defense/art-src/portraits/draconis.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| C2 | Thư Đồng Chấm · vui | Đã có | [games/typing-defense/art-src/portraits/helper-cham-happy.png](../../games/typing-defense/art-src/portraits/helper-cham-happy.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| C3 | Thư Đồng Chấm · hoảng | Thiếu | [games/typing-defense/art-src/portraits/helper-cham-scared.png](../../games/typing-defense/art-src/portraits/helper-cham-scared.png) | Còn lại 015b; prompt ở file 03. |
| C4 | Thư Đồng Phẩy · vui | Thiếu | [games/typing-defense/art-src/portraits/helper-phay-happy.png](../../games/typing-defense/art-src/portraits/helper-phay-happy.png) | Còn lại 015b; prompt ở file 03. |
| C5 | Thư Đồng Phẩy · hoảng | Thiếu | [games/typing-defense/art-src/portraits/helper-phay-scared.png](../../games/typing-defense/art-src/portraits/helper-phay-scared.png) | Còn lại 015b; prompt ở file 03. |
| C6 | Thư Đồng Gạch · vui | Thiếu | [games/typing-defense/art-src/portraits/helper-gach-happy.png](../../games/typing-defense/art-src/portraits/helper-gach-happy.png) | Còn lại 015b; prompt ở file 03. |
| C7 | Thư Đồng Gạch · hoảng | Thiếu | [games/typing-defense/art-src/portraits/helper-gach-scared.png](../../games/typing-defense/art-src/portraits/helper-gach-scared.png) | Còn lại 015b; prompt ở file 03. |
| C8 | Bà Cú Mực, người kể | Đã có | [games/typing-defense/art-src/portraits/narrator.png](../../games/typing-defense/art-src/portraits/narrator.png) | Đã có từ trước; chưa duyệt lại toàn bộ chất lượng trong 015. |
| L1 | Tắt | Thiếu | [games/typing-defense/art-src/ui/lanterns/lantern-unlit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-unlit.png) | Còn lại 015b; prompt ở file 03. |
| L2 | Sáng | Thiếu | [games/typing-defense/art-src/ui/lanterns/lantern-lit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-lit.png) | Còn lại 015b; prompt ở file 03. |
| L3 | Cháy rực | Thiếu | [games/typing-defense/art-src/ui/lanterns/lantern-blazing.png](../../games/typing-defense/art-src/ui/lanterns/lantern-blazing.png) | Còn lại 015b; prompt ở file 03. |
| U1 | Lũy Chữ | Thiếu | [games/typing-defense/art-src/ui/buildings/keep.png](../../games/typing-defense/art-src/ui/buildings/keep.png) | Còn lại 015b; prompt ở file 03. |
| U2 | Tháp Cung | Thiếu | [games/typing-defense/art-src/ui/buildings/archer.png](../../games/typing-defense/art-src/ui/buildings/archer.png) | Còn lại 015b; prompt ở file 03. |
| U3 | Tháp Pháo | Thiếu | [games/typing-defense/art-src/ui/buildings/cannon.png](../../games/typing-defense/art-src/ui/buildings/cannon.png) | Còn lại 015b; prompt ở file 03. |
| U4 | Trại Lính | Thiếu | [games/typing-defense/art-src/ui/buildings/barracks.png](../../games/typing-defense/art-src/ui/buildings/barracks.png) | Còn lại 015b; prompt ở file 03. |
| U5 | Mỏ Vàng | Thiếu | [games/typing-defense/art-src/ui/buildings/gold-mine.png](../../games/typing-defense/art-src/ui/buildings/gold-mine.png) | Còn lại 015b; prompt ở file 03. |
| U6 | Ruộng Lúa | Thiếu | [games/typing-defense/art-src/ui/buildings/farm.png](../../games/typing-defense/art-src/ui/buildings/farm.png) | Còn lại 015b; prompt ở file 03. |
| U7 | Đài Ấn (nếu kịp) | Thiếu | [games/typing-defense/art-src/ui/buildings/seal-dais.png](../../games/typing-defense/art-src/ui/buildings/seal-dais.png) | Còn lại 015b; prompt ở file 03. |
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
| Lính Rainbow | Đã có | [games/space-typing/art-src/enemies/rainbow-scout.png](../../games/space-typing/art-src/enemies/rainbow-scout.png) | Dùng chung Space; không sao chép/sinh lại. |
| Trâu / Đầu Đàn | Đã có | [games/space-typing/art-src/enemies/rainbow-tank.png](../../games/space-typing/art-src/enemies/rainbow-tank.png) | Dùng chung Space; không sao chép/sinh lại. |
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
| title-horizon | Đã có | [games/typing-survival/art-src/ui/title-horizon.png](../../games/typing-survival/art-src/ui/title-horizon.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. |
| gun-xung | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/gun-xung.png](../../games/typing-survival/art-src/ui/icons/gun-xung.png) | Đã có trước, giữ nguyên; kiểm trực tiếp: 1254×1254 khác 1024×1024, lề hẹp theo README-015. |
| gun-tia | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/gun-tia.png](../../games/typing-survival/art-src/ui/icons/gun-tia.png) | Đã có trước, giữ nguyên; kiểm trực tiếp: 1254×1254 khác 1024×1024, lề hẹp theo README-015. |
| gun-tan | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/gun-tan.png](../../games/typing-survival/art-src/ui/icons/gun-tan.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. |
| gun-ray | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/gun-ray.png](../../games/typing-survival/art-src/ui/icons/gun-ray.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. |
| gun-phao-sao | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/gun-phao-sao.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. |
| nova | Có nhưng lỗi | [games/typing-survival/art-src/ui/icons/nova.png](../../games/typing-survival/art-src/ui/icons/nova.png) | 015: xem README-015 về khổ, alpha, lề, số lượng và giới hạn. |

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

## 6. Còn lại cho phiếu 015b

### 6.1. Lỗi cần xử lý trước

Rồng: E01-S vẫn sai cánh sau lần thử thêm; G01-F và U1-F chưa xác nhận tư thế/mặt khiên, nên không sinh Back mới. D1–D4 và B1 còn giới hạn lề, nền, khổ, chi tiết hoặc mép theo README-015. Đất và icon M0 còn lỗi/giới hạn ở README cũ. Không dùng 012 để kết luận đã đạt, không yêu cầu thêm model chỉ vì ảnh ứng viên chưa đạt.

Tuyến Cuối: duyệt tựa và 4 icon đã thử lại, nhất là số viên Tán, lề Ray/Pháo Sao/Nova, alpha và đọc ở 32 px. Không sinh quá một lần thử lại. Xung/Tia cũ giữ nguyên. Nếu §4.2 đã đủ file thì không còn PNG định danh bị thiếu, nhưng các giới hạn chất lượng vẫn mở.

### 6.2. Lời Gọi · từng đích P còn thiếu

| Mã | Đích còn thiếu | Lý do |
|---|---|---|
| S3-v2 | [games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v2.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| S6-v2 | [games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| S12-v2 | [games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| S13-v1 | [games/typing-defense/art-src/scenery/shared/tree-stump-v1.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v1.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| S13-v2 | [games/typing-defense/art-src/scenery/shared/tree-stump-v2.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v2.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F1 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-a.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F2 | [games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/sky-b.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F3 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-320.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F4 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-220.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F5 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| F6 | [games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| C3 | [games/typing-defense/art-src/portraits/helper-cham-scared.png](../../games/typing-defense/art-src/portraits/helper-cham-scared.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| C4 | [games/typing-defense/art-src/portraits/helper-phay-happy.png](../../games/typing-defense/art-src/portraits/helper-phay-happy.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| C5 | [games/typing-defense/art-src/portraits/helper-phay-scared.png](../../games/typing-defense/art-src/portraits/helper-phay-scared.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| C6 | [games/typing-defense/art-src/portraits/helper-gach-happy.png](../../games/typing-defense/art-src/portraits/helper-gach-happy.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| C7 | [games/typing-defense/art-src/portraits/helper-gach-scared.png](../../games/typing-defense/art-src/portraits/helper-gach-scared.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| L1 | [games/typing-defense/art-src/ui/lanterns/lantern-unlit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-unlit.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| L2 | [games/typing-defense/art-src/ui/lanterns/lantern-lit.png](../../games/typing-defense/art-src/ui/lanterns/lantern-lit.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| L3 | [games/typing-defense/art-src/ui/lanterns/lantern-blazing.png](../../games/typing-defense/art-src/ui/lanterns/lantern-blazing.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U1 | [games/typing-defense/art-src/ui/buildings/keep.png](../../games/typing-defense/art-src/ui/buildings/keep.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U2 | [games/typing-defense/art-src/ui/buildings/archer.png](../../games/typing-defense/art-src/ui/buildings/archer.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U3 | [games/typing-defense/art-src/ui/buildings/cannon.png](../../games/typing-defense/art-src/ui/buildings/cannon.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U4 | [games/typing-defense/art-src/ui/buildings/barracks.png](../../games/typing-defense/art-src/ui/buildings/barracks.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U5 | [games/typing-defense/art-src/ui/buildings/gold-mine.png](../../games/typing-defense/art-src/ui/buildings/gold-mine.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U6 | [games/typing-defense/art-src/ui/buildings/farm.png](../../games/typing-defense/art-src/ui/buildings/farm.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U7 | [games/typing-defense/art-src/ui/buildings/seal-dais.png](../../games/typing-defense/art-src/ui/buildings/seal-dais.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U8 | [games/typing-defense/art-src/ui/tempo/tempo-0.png](../../games/typing-defense/art-src/ui/tempo/tempo-0.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U9 | [games/typing-defense/art-src/ui/tempo/tempo-6.png](../../games/typing-defense/art-src/ui/tempo/tempo-6.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U10 | [games/typing-defense/art-src/ui/tempo/tempo-4.png](../../games/typing-defense/art-src/ui/tempo/tempo-4.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U11 | [games/typing-defense/art-src/ui/tempo/tempo-3.png](../../games/typing-defense/art-src/ui/tempo/tempo-3.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U12 | [games/typing-defense/art-src/ui/tempo/tempo-2.png](../../games/typing-defense/art-src/ui/tempo/tempo-2.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U13 | [games/typing-defense/art-src/ui/tempo/tempo-1.png](../../games/typing-defense/art-src/ui/tempo/tempo-1.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U14 | [games/typing-defense/art-src/ui/charms/charm-mend.png](../../games/typing-defense/art-src/ui/charms/charm-mend.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U15 | [games/typing-defense/art-src/ui/charms/charm-frost.png](../../games/typing-defense/art-src/ui/charms/charm-frost.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U16 | [games/typing-defense/art-src/ui/charms/charm-gale.png](../../games/typing-defense/art-src/ui/charms/charm-gale.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U17 | [games/typing-defense/art-src/ui/resources/lives.png](../../games/typing-defense/art-src/ui/resources/lives.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U18 | [games/typing-defense/art-src/ui/resources/gold.png](../../games/typing-defense/art-src/ui/resources/gold.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U19 | [games/typing-defense/art-src/ui/resources/food.png](../../games/typing-defense/art-src/ui/resources/food.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U20 | [games/typing-defense/art-src/ui/resources/wood.png](../../games/typing-defense/art-src/ui/resources/wood.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U21 | [games/typing-defense/art-src/ui/resources/knowledge.png](../../games/typing-defense/art-src/ui/resources/knowledge.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U22 | [games/typing-defense/art-src/ui/resources/wave.png](../../games/typing-defense/art-src/ui/resources/wave.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U23 | [games/typing-defense/art-src/ui/loot/coin-common.png](../../games/typing-defense/art-src/ui/loot/coin-common.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U24 | [games/typing-defense/art-src/ui/loot/coin-refined.png](../../games/typing-defense/art-src/ui/loot/coin-refined.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U25 | [games/typing-defense/art-src/ui/loot/coin-high.png](../../games/typing-defense/art-src/ui/loot/coin-high.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U26 | [games/typing-defense/art-src/ui/loot/coin-elite.png](../../games/typing-defense/art-src/ui/loot/coin-elite.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U27 | [games/typing-defense/art-src/ui/loot/coin-mini-boss.png](../../games/typing-defense/art-src/ui/loot/coin-mini-boss.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| U28 | [games/typing-defense/art-src/ui/loot/coin-major-boss.png](../../games/typing-defense/art-src/ui/loot/coin-major-boss.png) | Trần 45 lượt; sau sửa ảnh nguồn và lô cảnh S1–S12. |
| X12 | [games/typing-defense/art-src/vfx/ma-troi-sheet.png](../../games/typing-defense/art-src/vfx/ma-troi-sheet.png) | Trần 45 lượt; tham khảo tùy chọn. |

### 6.3. Lời Gọi · từng đích VS còn thiếu

Toàn bộ 200 dòng còn thiếu ở §3.4 là danh sách chuyển 015b: 110 cảnh, 12 phông, 14 chân dung, 3 ảnh trượt, 6 tranh, 48 Neon, 4 thú nền và 3 icon. Làm sau P, ưu tiên cây/khối tán/đá; giữ tham chiếu biến thể và 8 hướng. Không mở lại 119 PNG của 005a/005b2; các lỗi K04/K10/K13, V18/V32/V33/V36/V37/V42/V43/V44/V55 vẫn theo README các phiếu đó.

### 6.4. Quy cách chưa khóa và chủ dự án cần xem

Chốt nhu cầu bitmap cho 27 ký hiệu/khung và 2 nhóm đất/tán ở §3.5, cùng 4 ký hiệu nguyên tố S2 nếu muốn dùng PNG. Duyệt ảnh và bảng 3D trước khi thay model/ảnh chạy. Không tạo âm, không chạy Git, build, test, game, art-normalize; không sửa mã, không nhập runtime, không tạo GLB hoặc chi credit Tripo.

### Tổng cuối phiếu theo game

| Game | PNG đã định danh còn thiếu | Chất lượng / phần chưa chốt |
|---|---|---|
| Rồng Giữ Ải | 0 | 0 ảnh thiếu mới; lỗi ảnh M0 và 8 ứng viên sửa vẫn theo README-015. |
| Lời Gọi | 248 | 48 P (gồm 1 tham khảo tùy chọn) + 200 VS dùng thẳng; 27 ký hiệu/khung và 2 nhóm đất/tán chưa chốt raster. |
| Tuyến Cuối | 0 | Đủ 7 PNG tựa/icon; 6 icon gồm 2 cũ còn sai khổ/lề; 4 nguyên tố S2 chưa có hợp đồng PNG. |

Bàn giao 015: **45 lượt image_gen / 34 đích ảnh** (8 Rồng, 21 Lời Gọi, 5 Tuyến Cuối), gồm 11 lần thử lại. Mỗi PNG có đúng prompt cạnh ảnh; các bản đầu được giữ .v1.png. Có 8 JPEG xem nhanh trong art-src/_review của ba game. Dừng đúng trần, không coi các lỗi còn lại là đã đạt.
