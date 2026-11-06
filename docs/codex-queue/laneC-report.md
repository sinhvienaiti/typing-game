### batch-01 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung: 0 PASS, 46 REDO, 4 DROP; chọn đúng một best cho mỗi job (hai job w2 đều chọn take3, vẫn REDO).
- Lỗi thường gặp 1: cắt mép, nền/sàn hoặc vật thừa; nặng nhất là đường hầm Blood, tấm kim loại và con dấu gỗ trong splash.
- Lỗi thường gặp 2: khối nhựa, đá hoặc hình dán phẳng; thiếu chiều sâu, nội khí và lớp radiance tinh tế.
- Lỗi thường gặp 3: nở chậm, không tan đúng nhịp; sheath và aura phình lớn, nối loop bật co rõ.
- Mốc cục bộ để tham khảo: boss-death-explosion-r2 và cutin-ember-drift cùng 7/10; cả hai vẫn phải làm lại, không có mốc đạt thương mại trong đợt.
- Kết quả: .local/video-review/results/batch-01.json; 28 prompt tiếng Anh, 18 yêu cầu still do chủ chọn trước I2V; bốn DROP là take thừa của hai job w2.
- Đã đối chiếu sidecar prompt cho sáu take w2 thiếu use/prompt, xem thêm đầu/cuối của 19 clip có yêu cầu loop; điểm motion dựa trên khung trích, chưa chứng nhận phát thời gian thực hay trong game; đã xoá khung tạm.

### batch-02 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung: 0 PASS, 39 REDO, 11 DROP; 39 job, mỗi job đúng một best, chưa job nào đạt 8/10.
- Lỗi thường gặp 1: khối khói/đá phình tới cắt khung, cuối còn đặc; loop đổi lõi sáng, kích thước hoặc cấu hình vật liệu.
- Lỗi thường gặp 2: sai hình/vai trò — sàn hoặc đĩa đá, khiên tròn, đầu rồng trong strip thân, cột đá đặc, hai vách đá trong sheath.
- Lỗi thường gặp 3: hình dán/khối cao su, viền sáng đều và ít radiance; charge không tụ, release/impact thiếu nhát bung nhanh rồi tan.
- Mốc cục bộ tốt hơn: earth-orb-loop take1 đạt 7/10; dark-big-burst-v2 take1 và death-soul-threads-w2 take2 đạt 6/10; đều REDO, không phải mốc đạt thương mại.
- Kết quả: .local/video-review/results/batch-02.json; 21 prompt tiếng Anh, 18 yêu cầu still do chủ chọn trước I2V; dragon-fire-body-ribbon take2/take3 trùng SHA-256, take3 DROP.
- Đã đọc sidecar của 12 take thiếu prompt/use, xem thêm đầu/cuối của 19 clip có yêu cầu loop; nền trắng của các lớp thân được xét đúng prompt cũ. Chấm motion từ khung trích, chưa chứng nhận phát thời gian thực/trong game; JSON.parse và kiểm tra đủ key/best đã qua, đã xoá khung tạm.


### batch-03 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung: 0 PASS, 37 REDO, 13 DROP; 37 job, mỗi job đúng một best, chưa job nào đạt 8/10.
- Lỗi thường gặp 1: phình/cắt mép, mang theo sàn hoặc cảnh đá; vòng đất, aura Cuồng/Hồi Nguyên đổi kích thước hoặc mật độ rõ khi nối vòng.
- Lỗi thường gặp 2: hình dán, neon đều hoặc vật đặc — lửa biểu tượng, đĩa kim loại, đá viền truyện tranh, hoa sen sai cánh; thiếu radiance tinh tế.
- Lỗi thường gặp 3: nở kéo dài/giữ nguyên thay vì tụ–bung–tan; spark spray tự nổ lần hai, khói không tan, wave thiếu đầu sóng và hướng tiến.
- Mốc cục bộ: fire-charge-gather-w2 take1 và fire-orb-loop take1 cùng 7/10, vẫn REDO; fire-ground-burn-loop-w2 take2 đạt 6/10 là hướng chất liệu tốt hơn, chưa phải mốc đạt thương mại.
- Kết quả: .local/video-review/results/batch-03.json; 17 prompt tiếng Anh sửa chất liệu, 20 brief cần chủ chọn still trước I2V; DROP chỉ là take thừa, không yêu cầu làm lại riêng.
- Đã đọc 18 sidecar thiếu prompt/use và xem đầu/cuối của 20 clip có yêu cầu loop; nền trắng khói được xét đúng prompt nguồn. Chấm motion từ khung trích, chưa chứng nhận phát thời gian thực/trong game; JSON.parse, đủ key/best và dữ liệu REDO đã qua; đã xoá khung tạm.



### batch-04 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung và 28 still nguồn: 0 PASS, 41 REDO, 9 DROP; 43 job, mỗi job đúng một best, chưa có mốc đạt 8/10.
- Lỗi thường gặp 1: gần như giữ ảnh rồi nhấp sáng, thiếu nhát bung dứt khoát và tan đúng pha; bảy manifest đều còn hình/ring/hạt ở khung cuối.
- Lỗi thường gặp 2: đổi hình hoặc phình/cắt khung — Asura manifest mất bố cục, Kỳ Lân manifest sinh vòng/sen mới, affliction Blood mất tinh thể và thành dây neon.
- Lỗi thường gặp 3: loop không khép về cỡ/độ sáng/cấu hình ban đầu; Qi Motes, Ultimate Ready và affliction Blood có chênh rõ; hai charge chỉ quay cung sáng, không tích lũy tới đầy.
- Mốc cục bộ: i2v-blood-comet-v2 take1, i2v-astral-kunpeng-leviathan-manifest take1 và i2v-dao-guard-hold-the-pass take2 cùng 6/10, đều REDO; DROP gồm bảy take thừa và hai comet v1 đã có v2 thay thế.
- Kết quả: .local/video-review/results/batch-04.json; 34 prompt tiếng Anh giữ nguyên still I2V và bảy brief cần chủ chọn still trước I2V. Chủ cần xem still World Sever/Cross Cuts đã chạm mép và xung đột nền đen ticket với Dark comet body nền trắng/normal blend; chưa chạy tạo lại.
- Đã xem thêm đầu/cuối của 25 clip (18 loop theo metadata/prompt/use, bảy manifest), đọc ba sidecar thiếu prompt/use; chấm motion bằng khung trích, chưa chứng nhận phát thời gian thực/trong game. JSON.parse, đủ key/best và dữ liệu REDO đã qua; đã xoá toàn bộ khung tạm tự tạo.


### batch-05 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung, đối chiếu 41 still nguồn: 0 PASS, 42 REDO, 8 DROP; 43 job, mỗi job đúng một best trong đợt.
- Lỗi thường gặp 1: giữ ảnh/nhấp sáng thay vì phát lực rồi tan; ba charge quay vùng sáng thay vì tích lũy, hai manifest còn hình/hạt ở cuối nên phát ngược chưa bắt đầu từ đen.
- Lỗi thường gặp 2: biến hình và lệch loop — affliction mất chi tiết, Ấn khóa mất chốt/sinh vòng tâm, Regen phình lớn; đầu sói/heo/quạ mọc tia hoặc lửa sai hành động, có vàng sai bảng đỏ/đen.
- Lỗi thường gặp 3: radiance ít hoặc thành dây viền; Frenzy cắt hai mép, nhiều ground mark/slash và still nguồn đã có lề hẹp, cần chủ xem giới hạn bố cục trước khi tạo lại.
- Mốc cục bộ tốt hơn: i2v-earth-comet-v2 take1, i2v-fire-comet take1, i2v-ice-comet take1 cùng 7/10; đều REDO, chưa có mốc đạt thương mại 8/10.
- Kết quả: .local/video-review/results/batch-05.json; 42 prompt tiếng Anh giữ nguyên still I2V; tám DROP gồm bảy take thừa và Earth comet v1 đã có v2 thay. Dark ground mark chọn take2 thay best tạm take1 của batch-04; không sửa hồ sơ đợt cũ.
- Đã xem thêm đầu/cuối 33 clip (gồm 13 loop theo prompt/use và hai manifest); motion dựa trên khung trích, chưa chứng nhận phát thời gian thực/trong game. JSON.parse, đủ key/best và dữ liệu REDO đã qua; đã xoá các khung tạm tự tạo.


### redo-01 (làm thử)
- 10 việc sửa bằng prompt `-q1`: 0/10 đạt 8; toàn đợt xem 17/17 take của 14 việc, 0 PASS, 14 REDO, 3 DROP (take thừa).
- Trung bình cùng 10 việc: trước 5,60 → sau 5,95/10 (+0,35); `before` giữ nguyên điểm best cũ từ `batch-01.json`, mỗi mục có một dòng so sánh.
- Tăng nhiều nhất: `boss-charge-impact-r2` 4 → 6,5 (+2,5); `blood-big-burst` 5,5 → 6,5 (+1; `beast-hit-ink-streak` đồng hạng +1).
- Hai việc không tăng tiêu biểu: `beast-death-ink-smoke` 6 → 6 và `blood-impact` 6 → 6; khói/màng vẫn nở cắt mép, không tan hết (heavy ink và boss death còn giảm 0,5).
- Đổi prompt cải thiện chất liệu nhưng chưa đưa việc nào lên 8: cần still nội bộ được chủ chọn để khóa hình/bố cục; với chất liệu thuần nên thử Blender mô phỏng để kiểm soát bung–tan/lề, và dựng chu kỳ loop có kiểm soát thay vì chỉ nhắc “seamless”.
- Ngoài mẫu 10 việc: rock r3 best take1 5/10 cần still; mirror pad85 best take2 6/10 vẫn đổi hình/phình mép và chưa tan đen; victory rays r2 best take1 6,5/10 vẫn lệch nối; metal sparkle 6/10 nối từ nhiều sao về gần đen (prompt yêu cầu loop dù metadata false).
- Kết quả: `.local/video-review/results/redo-01.json`; đã xem 10 sheet cũ, 17 sheet mới, still gương và đầu/cuối đủ 17 clip; MAE nối/khung kề: rays take1 5,96×, take2 5,77×, metal 9,24×. Chấm motion bằng khung trích, chưa duyệt phát thời gian thực/trong game; kiểm JSON.parse/đủ key/best/prompt REDO và xoá khung tạm; không chạy build/test hay sửa tài sản.


### batch-06 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung, đối chiếu 33 still nguồn: 0 PASS, 38 REDO, 12 DROP; 39 job, mỗi job đúng một best.
- Lỗi thường gặp 1: giữ ảnh/nhấp sáng hoặc xoay chậm thay vì phát lực rồi tan; hai charge-fill chỉ quay vùng sáng, không tích lũy tới đầy.
- Lỗi thường gặp 2: phình/cắt khung hoặc đổi hình — Kiếm Tổ mọc vòm, Vạn Liên thành hoa có đài đặc, Đỉnh thành nồi đen, hồ ly manifest thành thú đứng; chủ cần xem lề hẹp sẵn của một số still, đợt này giữ nguyên still theo phiếu.
- Lỗi thường gặp 3: tắt/nối vòng chưa đúng — bốn trong sáu manifest còn hình/vòng/hạt ở khung cuối, hai bản còn lại dồn tắt về đoạn chót; affliction đổi cấu trúc, ground mark mất đá hoặc còn khe sáng.
- Mốc cục bộ tốt hơn: i2v-ice-crescent-sym take1, i2v-light-caster-seal take1, i2v-metal-comet-v2 take1 cùng 7/10; đều REDO, chưa có mốc đạt thương mại 8/10.
- Kết quả: .local/video-review/results/batch-06.json; 38 prompt tiếng Anh giữ nguyên still I2V, 12 DROP gồm 11 take thừa và Metal comet v1 được v2 thay theo use; không tạo ảnh/video hay sửa manifest.
- Đã xem thêm đầu/cuối cả 50 clip và 0–1,4 giây đầu của 10 chiêu lớn; motion/loop chấm bằng khung trích, chưa chứng nhận phát thời gian thực/trong game. JSON.parse, đủ key/best và dữ liệu REDO đã qua; đã xoá khung tạm tự tạo, dừng sau một đợt.


### batch-07 — 07/11/2026
- Đã xem riêng 50/50 tấm 6 khung, đối chiếu 33 still nguồn: 0 PASS, 37 REDO, 13 DROP; 38 job, mỗi job đúng một best.
- Lỗi thường gặp 1: giữ ảnh/nhấp sáng thay vì phát lực rõ rồi tan; ba charge quay vùng sáng, tắt ô cũ thay vì tích lũy tới đầy.
- Lỗi thường gặp 2: đổi hình/phình/cắt biên — Poison affliction tràn khung, chuông mất/mọc quai, tháp sinh vòng nút lớn, thương hóa dây sét; nhiều still cột và thương đã cắt mép trên, chủ cần xem lại bố cục nguồn.
- Lỗi thường gặp 3: tàn dư và nối vòng — cả ba manifest chưa về đen; ground mark mất đá hoặc còn khe sáng; Star/Thunder affliction mất dáng ôvan, MAE nối/khung kề lần lượt 12,59×/9,81× (xám 160×90, đối chiếu hai cặp kề mỗi đầu).
- Mốc cục bộ tốt hơn: i2v-poison-comet-v2 take1, i2v-star-comet take1, i2v-star-caster-seal take1 cùng 7/10; đều REDO, chưa có mốc đạt thương mại 8/10.
- Kết quả: .local/video-review/results/batch-07.json; 37 prompt tiếng Anh giữ nguyên still I2V; 13 DROP gồm 12 take thừa và Poison comet v1 được v2 thay theo use. Chỉ duyệt, chưa tạo lại ảnh/video.
- Đã xem đầu/cuối cả 50 clip, thêm 0–0,8 giây đầu của 11 clip và đo 11 loop theo prompt/use dù metadata false; motion dựa trên khung trích, chưa chứng nhận phát thực/trong game. JSON.parse/đủ key/best/REDO đã kiểm; đã xoá khung tạm tự tạo, dừng sau một đợt.
