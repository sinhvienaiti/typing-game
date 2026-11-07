# Luồng S1 · báo cáo GIỮ-CHỈNH · 07/11/2026

Kiểm tầng A theo vai trò; không chấm điểm tầng B. Nguồn và manifest đang dùng được giữ nguyên.

**i2v-fire-comet__take1 · A-PASS.** Thân Hỏa giữ đúng hướng và nội hỏa; taper chỉ bỏ tia đuôi cắt sát mép, fit/căn khung đạt ngưỡng; dùng travel một lượt, chưa duyệt loop.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-fire-comet/v1`; khung [12,84) @24. Lề 10.65 %, trôi 0.33 %, đổi cỡ 2.17, 2.68 %, p99 RGB 0.00, 0.00, 0.00. Recipe/evidence ghi nguồn, SHA-256 và năm ô; đã xóa khung trích của S1.

**i2v-ice-comet__take1 · A-PASS.** Đầu và mạng băng giữ thể tích, hai mép đọc rõ; đoạn 12–83 không có nhấp trắng kiểu bật/tắt. Chỉ dùng đầu/đuôi băng trong travel một lượt.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-ice-comet/v1`; khung [12,84) @24. Lề 15.57 %, trôi 0.21 %, đổi cỡ 0.68, 0.93 %, p99 RGB 0.00, 0.00, 0.00. Recipe/evidence ghi nguồn, SHA-256 và năm ô; đã xóa khung trích của S1.

**i2v-metal-comet-v2__take1 · A-PASS.** Giữ được lõi và sợi bạc, dòng đuôi chuyển động nội tại; đoạn 12–83 không biến dạng đầu. Chỉ dùng thân Kim cho travel một lượt.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-metal-comet-v2/v1`; khung [12,84) @24. Lề 13.23 %, trôi 0.52 %, đổi cỡ 2.92, 1.28 %, p99 RGB 0.00, 0.00, 0.00. Recipe/evidence ghi nguồn, SHA-256 và năm ô; đã xóa khung trích của S1.
Đã soi 12 tấm/72 khung; KTX2 UASTC đủ 72 khung khác nhau, gutter 0. Recipe có scale/alpha/reveal/erosion theo khung và ba id lớp phụ chuyển S3; lưu ý đường gọi lab đang loop, bản này chỉ one-shot. Chưa ghép host/chấm tầng B theo ranh giới.


**i2v-poison-comet-v2__take1 · A-PASS.** Xong đúng dòng todo đầu #5; nguồn [12,66) @24, thân Độc travel một lượt; đã soi đủ 54 khung trên đúng 12 ảnh.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-poison-comet-v2/v1/` (MP4 1080p, atlas, KTX2, recipe, evidence, so 6 khung).
Lề 13.06 %, trôi 0.13 %, đổi cỡ X/Y 1.093, 1.331 %, p99 RGB 0/255; 54 khung MP4 khác nhau, gutter KTX2=0. Recipe ghi scale/alpha/reveal/erosion bằng khung; 2 id phụ chuyển S3.
Lưu ý: seam 2,024×, không loop; đường gọi lab hiện loop nên Claude phải đổi khi ghép. Chưa kiểm host/chấm B; không sửa mã/manifest nguồn, không chạy Blender/build/test; đã xóa riêng khung thô lần này. Dừng sau một dòng.


**i2v-star-comet__take1 · A-PASS.** Xong đúng dòng todo đầu #6, [12,84) @24; soi đủ 72 khung nguồn và MP4 trên đúng 12 tấm; không có khung cũ của job này để dùng lại, SHA-256 nguồn/prompt/ảnh đầu khớp khi chốt.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-star-comet/v1/` (MP4 1080p, atlas, KTX2, recipe, evidence, so 6 khung); fit tĩnh 0,90 giữ mạng sao và xoáy đầu.
Lề 12.50 %, trôi 1.37 %, đổi cỡ X/Y 3.995/2.230 %, nền p99 0/255; 72 khung MP4 khác nhau, gutter KTX2=0. Recipe có duration/scale/alpha/reveal/erosion theo khung và hai id phụ S3.
Lưu ý: chỉ một lượt, seam 1,875× chưa duyệt loop; lab hiện loop nên Claude đổi cách phát/đo lại pivot. Chưa kiểm 1:1, tốc độ/nền thật trong host và tầng B theo ranh giới; không chạy Blender/build/test, đã xóa riêng 216 PNG thô lần này. Dừng sau một dòng.


**i2v-thunder-comet__take1 · A-PASS.** Xong đúng dòng todo đầu #7; đủ f12–65 @24 trên 12 ảnh, SHA video/prompt/ảnh đầu khớp; không có khung cũ của job Lôi để dùng lại.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-thunder-comet/v1/` (MP4 1080p, atlas/KTX2, recipe/evidence, so 6 khung); fit tĩnh 0,90, giữ sét nội bộ.
Lề 11.48 %, trôi 1.66 %, đổi cỡ X/Y 3.310/3.169 %, nền p99=0/255; 54 khung khác nhau, gutter KTX2=0. Recipe có duration/scale/alpha/reveal/erosion theo khung và 2 id phụ S3.
Lưu ý: đầu trắng mềm đã bake; gain linear đề xuất 0,75 tối/0,45 sáng, không HDR toàn đầu; một lượt, lab cũ loop nên Claude đổi khi ghép. Chưa kiểm tốc độ thật/host và tầng B; không chạy Blender/build/test; đã xóa riêng 162 PNG thô. Dừng sau một dòng.


**i2v-water-comet__take1 · A-PASS.** Xong đúng dòng todo đầu #8; đủ f12–83 @24 trên đúng 12 ảnh; SHA video/prompt/ảnh đầu khớp, không có khung cũ của job Thủy để dùng lại.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-water-comet/v1/` (MP4 1080p, atlas/KTX2, recipe/evidence, so 6 khung); căn tâm và scale đồng nhất, giữ vân nước/đầu lưới.
Lề 10.37 %, trôi 0.26 %, đổi cỡ X/Y 2.070/2.281 %, nền p99=0/255; 72 khung khác nhau, gutter KTX2=0. Recipe có duration/scale/alpha/reveal/erosion bằng khung và 2 id phụ S3.
Lưu ý: một lượt; lab hiện loop nên Claude đổi cách phát/đo lại pivot, kiểm đầu lưới ở cỡ chơi, nền sáng và rung sau căn. Chưa kiểm tốc độ thật/host hoặc tầng B; không chạy Blender/build/test; đã xóa riêng 216 PNG thô. Dừng sau một dòng.


**i2v-blood-crescent-sym__take1 · A-PASS ngoại tuyến.** Xong đúng dòng todo đầu #9; đủ f12–83 @24 trên 12 ảnh; SHA nguồn/prompt/ảnh đầu khớp, không có khung cũ của job để dùng lại.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-blood-crescent-sym/v1/` (MP4 1080p, atlas/KTX2, recipe/evidence, so 6 khung); fit cố định 0,90 giữ hai sừng/cung đỏ cân.
Lề 13.91 %, trôi 1.35 %, đổi cỡ X/Y 0.475/3.854 %, nền p99=0/255; 72 mẫu khác nhau, gutter KTX2=0. Recipe ghi đường bao engine 1 giây lấy prefix 24 mẫu và hai id phụ S3.
Lưu ý: seam 5.593×, không loop/ping-pong; Claude bỏ cách SYM_RATE=3/cửa sổ 8 mẫu khi ghép, kiểm pivot, nền sáng, nhịp cast thật và tầng B. Không chạy Blender/build/test; đã xóa riêng 216 PNG thô. Dừng sau một dòng.


**i2v-ice-crescent-sym__take1 · A-PASS ngoại tuyến.** Xong đúng một dòng todo #10; đủ f12–83 @24 trên 12 ảnh, SHA nguồn/prompt/ảnh đầu khớp.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-ice-crescent-sym/v1/`: MP4 1080p, atlas/KTX2, recipe/evidence, so 6 thời điểm; fit tĩnh 0,90 giữ mặt tinh thể/hai sừng.
Lề 15.16 %, trôi 0.46 %, đổi cỡ X/Y 0.675, 1.833 %, nền p99 0.000, 0.000, 0.000/255; 72 mẫu khác nhau; gutter KTX2 0/255. Recipe có đường bao và 2 id phụ S3.
Chưa duyệt loop/host/tầng B; Claude kiểm cách phát crescent hiện tại, pivot, nền sáng và nhịp cast. Đã xóa 216 PNG tự trích; không chạy Blender/build/test. Dừng sau một dòng.


**i2v-dark-slash-arc__take1 · A-FAIL→S2.** Đã soi nguồn f12–65, gói thử f40–63 (24 khung) sau 2 fit; đổi cỡ dọc MP4 5,246% >5%, không tích hợp.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-dark-slash-arc/v1`: MP41080p, atlas/KTX2, recipe/envelope theo khung, so6 thời điểm, SHA-256 và package-check; 7 ảnh đã xem, gutter=0, nền p99=0.
Ảnh đầu palette A giữ nguyên; thêm đúng dòng S1-11 vào S2, chưa tạo ảnh/Blender hoặc chấm tầng B; xóa 102 PNG tự trích, không sửa nguồn/manifest/mã game.

**i2v-ice-slash-arc__take1 · A-PASS ngoại tuyến.** Xong đúng một dòng todo #12; soi f12–83, chốt [36,60) @24, đủ 24 mẫu thật; tổng 9 ảnh đã xem.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-ice-slash-arc/v1/`: MP4 1080p, atlas/KTX2, recipe/evidence, so 6 cặp; fit tĩnh 0,90 và hạ nền.
Lề 7.40 %, trôi 1.60 %, đổi cỡ X/Y 0.527, 1.705 %, p99 RGB 1.000, 1.000, 1.000/255; gutter KTX2 0/255. Có đường bao theo khung và 2 id phụ S3.
Bỏ cửa sổ toàn đoạn vì trôi tâm 7,858%; chưa duyệt loop/host/tầng B. Đã xóa 264 PNG tự trích; Claude cần kiểm pivot, nhịp quét, nền sáng và bản ghép. Không chạy Blender/build/test. Dừng sau một dòng.


**i2v-water-slash-arc__take1 · A-PASS ngoại tuyến.** Xong đúng một dòng #13; soi f12–65, chốt [24,48) @24, 24 mẫu thật; 8 ảnh đã xem.
Đầu ra: `games/immortality-cultivation/art-src/lab/vfx-redo-2026-11-07/keep/i2v-water-slash-arc/v1/`: MP4 1080p, atlas/KTX2, recipe/evidence/SHA-256, so 6 cặp; fit tĩnh 0,90, hạ nền.
Lề 7.78 %, trôi 0.75 %, đổi cỡ X/Y 1.618, 2.171 %, p99 RGB 1.000, 1.000, 1.000/255; KTX2 gutter 0/255, 24/24 mẫu MP4 khác nhau. Đường bao theo khung và 2 id phụ S3 đã ghi.
Không loop (seam 3.085×); chưa tích hợp/chấm tầng B. Xóa 102 PNG tự trích. Claude cần kiểm pivot, nhịp quét, nền sáng và bản ghép trong host. Không chạy browser/Blender/build/test. Dừng sau một dòng.

