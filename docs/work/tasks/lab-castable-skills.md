# Biến các mục trình diễn trong lab thành kỹ năng dùng được (phím 8, phím 9)

**Mục tiêu (≤ 3 dòng):** mỗi cột trụ, tuyệt kỹ (phím 8) và mỗi kỹ năng mới (phím 9) bấm là tung lên bầy quái của lab: chọn đích, đánh trúng đúng lúc clip chạm, ra số sát thương, quái phản ứng hoặc chết, có rung, đèn, âm. Anh thử từng đợt.
**Cách đã chốt:** anh, 06/11 00:05: "tạm thời chưa cần chấm, tôi sẽ là người chấm, bạn hãy bắt đầu triển khai từng cái vào lab để nó thành skill để tôi test là được". Anh là người chấm; không cần giám khảo mù cho các bước lab. Chỉ làm trong lab (`games/.wt-ic-lab-elements`, nhánh `claude/lab-element-kits`, trang dev, không vào bản chơi), không đổi sim của game.
**Nghiệm thu (số):** từ phím tới khung phát chiêu ≤ 50 ms; cú trúng đầu khớp khung đỉnh của clip ±1 khung; mỗi kỹ năng có số sát thương, phản ứng hoặc chết, rung và hit-stop theo bậc, âm nếu có file; 0 lỗi trong Chrome headless; test cũ vẫn qua; bản 4310 cập nhật sau mỗi đợt.
**Phiếu, báo cáo, ảnh:** bảng thông số 30 kỹ năng mới `docs/work/tasks/clip-skills-expansion.json` (agent lab-flipbooks soạn).

## Khung chung (một bảng dữ liệu, một bộ chạy; không viết mã riêng cho từng kỹ năng, trừ khi bắt buộc)

**1. Bảng `ClipSkill` (một dòng mỗi kỹ năng):**

| Trường | Ý nghĩa |
|---|---|
| `id`, `name` | Tên tiếng Anh và Hán Việt, hiện trên bảng lab |
| `element`, `clip` | Clip trong manifest |
| `shape` | Một trong: `point` (cụm quái dày nhất), `multi` (N cụm dày nhất), `field` (cả sân), `line` (từ người chơi thẳng qua đường dày nhất), `ring` (vòng quanh một tâm, nở theo thời gian), `sweep` (cung quét quanh một tâm), `path` (đường bay của thần thú qua sân), `cone` (hình quạt từ người chơi) |
| `radius` (m), `count` | Bán kính và số điểm hay số đợt |
| `strikes` | Danh sách `{ t, power }`. `t` lấy từ khung đỉnh của clip (`timing.peak / fps`), không đoán |
| `damage` | Bậc sát thương: `light`, `heavy`, `ult` |
| `status` | Tuỳ chọn: `stun`, `bind`, `slow`. Trong lab chỉ làm quái đứng hoặc chậm lại, có dấu trên quái |
| `mark` | Ấn trên đất 0,15–0,25 s trước cú từ trời (bài học video, `skills/REF_VIDEO_LESSONS_2026-11-05.md` bài 1) |
| `linger` | Dư âm trên đất 1,5–2,5 s bằng erosion (bài 3) |
| `sfx` | File `tt-sfx-*` trong `art-src/lab/firefly-sprint-2026-11-05/sound/` (bản tốt nhất); không có file thì để trống và ghi vào danh sách |

**2. Chọn đích không gắn với bản đồ** (luật 04/11): tính từ vị trí quái và biên sân, như phím 7 gộp theo ô 8 m. Không có quái thì đặt giữa sân.

**3. Đánh trúng dùng đúng đường của phím 0–7:** cùng sự kiện chạm, số sát thương (`DamageCompiler`), phản ứng và chết của bầy, hit-stop, camera kick, đèn chạm (`feel.ts`), bậc rung. Nhờ vậy cảm giác đánh giống bộ Kiếm.

**4. Nhịp:**
- Bấm là phát ngay. Clip đặt đúng chỗ, đúng góc camera (như phím 8 hiện nay).
- Cú trúng rơi đúng khung đỉnh.
- Hình và dư âm tàn chậm.
- Chữ quái luôn đọc được.

**5. Bảng lab:**
- Danh sách kỹ năng của phím 8 và 9: tên, hình đánh, bán kính, số cú, bậc sát thương.
- Shift+8 hoặc Shift+9 chọn mục, phím 8 hoặc 9 tung chiêu.
- Lab không có hồi chiêu, để anh bấm thử liên tục.

## Đợt (mỗi đợt xong: cập nhật 4310, ghi nhật ký, báo điều phối tối đa 10 dòng)

| Đợt | Nội dung | Ai |
|---|---|---|
| 1 | Khung chung + 17 mục phím 8: các cột trụ và tuyệt kỹ 14 hệ. Thông số tự soạn từ `skills/PRODUCTION_LIST_2026-11-05.md` §4, §7 | lab-element-kits |
| 2 | A1–A8 diện rộng | lab-element-kits, theo `clip-skills-expansion.json` |
| 3 | C1–C8 thần thú (`path`: thân năng lượng bay qua sân, trúng quái dọc đường) | như trên |
| 4 | D1–D8 pháp bảo (chuông nở vòng, hồ lô quạt, tháp trói…) | như trên |
| 5 | B1–B6 pháp tướng (thân khổng lồ trong suốt sau người chơi, đánh nhiều cú) | như trên |

Sau 5 đợt: D62 sao băng nghiêng (`tasks/slanted-meteor.md`), D61 chiêu duy trì (`tasks/channel-skill.md`), D60 bộ đếm chuỗi từ (`tasks/streak-counter.md`).

## Bảng 30 kỹ năng mới (`clip-skills-expansion.json`, agent lab-flipbooks)

Mỗi mục điền các trường ở mục 1:
- `clip`: id trong manifest `expansion`.
- `shape`, `radius`, `count`, `status`: lấy từ dòng lối chơi Gemini (`docs/games/tu-tien/source/gemini-skills-expansion-2026-11-05.md`, bảng ở `skills/SKILLS_EXPANSION_2026-11-05.md`).
- `strikes`: đo khung đỉnh, hoặc nhiều đỉnh, trên atlas của clip.
- `sfx`: file tốt nhất `tt-sfx-x-<id>`.

Ghi rõ chỗ nào là phỏng đoán.

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 06/11 00:08 · Claude · tạo việc; giao đợt 1 cho lab-element-kits, bảng 30 kỹ năng cho lab-flipbooks
- 06/11 00:08 · Claude (lab-flipbooks) · soạn `clip-skills-expansion.json`, 30 mục A1–D8 · hình, bán kính, số điểm, bậc, trạng thái, ấn, dư âm là quyết định từ lời Gemini và kích thước sân 40×26 m (ghi trong `guess` từng mục); mọi clip bắt đầu đã ở đủ sức nên không có khung va chạm sắc, `strikes[0].t` dùng thời gian bật của thiết kế (0,15–0,4 s) trừ D8 đo được 0,62 s; âm: 27/30 có file, thiếu D6, D7, D8
- 06/11 01:05 · Claude (lab-element-kits) · đợt 1 xong, commit `fd3f760` (nhánh claude/lab-element-kits): bảng `ClipSkill` + bộ chạy `ClipSkillRunner` (`src/lab/clip-skills.ts`), chọn đích cả 8 hình từ vị trí quái (ô 8 m), cú trúng theo khung đỉnh qua bản đồ thời gian của clip, cùng đường đánh phím 0–7 (herd.hit, impact/death, số, screen tier + hit-stop, kick, đèn), ấn `groundMark` của hệ 0,2 s trước đòn từ trời và dư âm 1,5–2,5 s, choáng/trói/chậm. 17 mục phím 8 (4 cột trụ, 13 tuyệt kỹ; dòng tuyệt kỹ Ám có sẵn, chờ clip). Phím 8 tung, Shift+8 chọn mục kế, danh sách "Kỹ năng (8)". Headless 4310: 17/17 tung được, 0 lỗi, cú đầu lệch khung đỉnh ≤ 1 khung; 1066 test qua. Phỏng đoán: các cú sau khung đỉnh (ghi `guess` trong bảng), mức W tạm của 3 bậc. Chờ `clip-skills-expansion.json` cho đợt 2.
- 06/11 00:35 · Claude · kiểm đợt 1 trên 4310: Lôi Trụ tung được, có chú thích hình đánh, bán kính, số cú, choáng; ra số sát thương (shown 3). Giao đợt 2 (A1–A8), đợt 3 (C1–C8) nối luôn
- 06/11 01:40 · Claude (lab-element-kits) · đợt 2 xong, commit `0d0dba8`: A1–A8 tung được ở phím 9 (bảng `KEY9_SKILLS` chép từ clip-skills-expansion.json, take âm theo bảng). Sửa so với bảng: cú đầu rơi đúng khung đỉnh clip thay giờ phỏng đoán 0,2–0,4 s, cú sau giữ nhịp bảng; trạng thái tạm choáng 1 s, trói 1,8 s, chậm 2 s; A2 đường chéo 40° qua giữa sân (đúng vực vẽ trong clip); A8 vòng khép từ mép vào; A5 quét cả vòng. Khung thêm: hình trải theo chỗ clip đứng, cú tick không hit-stop, số theo power, Shift+9 chọn mục kế. 4310: 8/8 tung, 0 lỗi, lệch đỉnh ≤ 1 khung; 1067 test qua.
- 06/11 02:05 · Claude (lab-element-kits) · đợt 3 xong, commit `a1759ef`: C1–C8 tung được ở phím 9. Thần thú `path` bay thật qua sân (thẻ clip bay mép này sang mép kia trong 1 s qua chỗ clip đứng: C1 trái sang phải, C3 nam lên bắc; quái trúng lúc thân bay tới, ấn dọc đường); C2 bốn vệt vuốt song song chéo 30° theo clip; C4–C8 vòng, 3 dấu móng, cả sân, vòng, quét cả vòng, trải theo chỗ clip đứng. Sửa như đợt 2 (cú đầu theo khung đỉnh, trạng thái tạm). 4310: 8/8 tung, 0 lỗi; lệch đỉnh ≤ 1 khung, riêng C3 trúng lúc thân tới (~0,5 s, đúng ý path); 1068 test qua. Đợt 4 (D1–D8) chờ điều phối.
- 06/11 02:35 · Claude (lab-element-kits) · đợt 4 xong, commit `4e9cd12`: D1–D8 tung được ở phím 9. Khung thêm `centre` (gồm mép xa), `arc`, `angles`, `perPoint`. Đặt theo clip: D1 ấn rơi xuống cụm quái dày nhất (bảng: giữa sân), cỡ 0,55; D3 hồ lô phun quạt 120° từ mép xa; D6 gương quét 140° từ mép xa; D3/D7 hệ any → Kim/Phong; D6–D8 chưa có âm Firefly, tạm âm tuyệt kỹ hệ đầu; D8 không có ấn (Ám không có groundMark). 4310: 8/8, 0 lỗi, lệch đỉnh ≤ 1 khung; 1069 test qua.
- 06/11 02:20 · Anh: phím 8 và 9 "hơi mờ, nhìn như kiểu video kém chất lượng". Gốc: atlas `ult`/`expansion` 32 ô 640×360, 6 khung/s (nguồn 1920×1080, 24 khung/s). Sửa: lab-flipbooks xuất mp4 1080p 24 khung/s + trường `video` trong manifest; lab-element-kits phát bằng VideoTexture (tối đa 2–3 video cùng lúc, giải phóng khi tắt) sau đợt 4–5.
- 06/11 03:05 · Claude (lab-element-kits) · đợt 5 xong, commit `af1a43e`: B1–B6 tung được, phím 9 đủ 30 kỹ năng. B1 sáu binh khí nện lần lượt sáu điểm, B2 bàn tay in lần lượt (13 điểm vừa khoảng cách), B3 chém cung 270° quanh người chơi, B4 vòng 14 m quanh người chơi (kiếm sao cắm dưới chân pháp tướng), B5 chữ X 50°/130° qua người chơi tới hai góc xa (đúng clip), B6 24 binh khí (19 điểm). 4310: 30/30 tung, 0 lỗi, lệch đỉnh ≤ 1 khung trừ C3 bay (trúng lúc thân tới); 1070 test qua. Máy chủ tạm 3068 đã tắt, Chrome headless đã đóng; 4310 vẫn chạy.
- 06/11 03:40 · Claude (lab-element-kits) · video 1080p xong, commit `d6399e7`: phím 8 và 9 phát `video` của manifest bằng VideoTexture trên cùng thẻ (cộng sáng, cùng chỗ và góc), tối đa 3 video, dư dùng atlas, chọn mục là nạp sẵn, hết chiêu pause + bỏ src + giải phóng texture, video kẹt 1,5 s hay không có H.264 thì về atlas; cú trúng theo thời gian video, cú đầu ở peakTime; ?video=0 để so atlas. 4310 thời gian thật: 5/5 phát video, cú đầu trễ 3–12 ms so với peakTime, 0 lỗi; 1071 test qua. Khung trước/sau: owner-review/2026-11-06/tu-tien/lab-skills-video/. Máy chủ tạm và Chrome headless đã tắt.
- 06/11 02:55 · Claude · kiểm `d6399e7`: khung trước/sau A1 cho thấy video 1080p nét hẳn (cánh sen, gân, hạt). Đợt 4 D1–D8 (`4e9cd12`), đợt 5 B1–B6 (`af1a43e`) xong; 48 video, 438 MB. Cả 47 kỹ năng phím 8, 9 đã tung được
- 06/11 09:05 · Claude · lab-element-kits đã làm xong D61 (`39f066f`, phím C) và D60 (`5312650`, góc trên trái) trước khi nhận tin đổi kế hoạch; giữ bản đó. Dừng lượt làm trùng của lab-channel và lab-streak, giao việc mới: lab-channel làm âm mới vào lab (nhánh claude/lab-sounds), lab-streak đo hiệu năng, RAM, độ đọc chữ (nhánh claude/lab-perf). Đợt clip mới: 4 ribbon-loop (Băng, Lôi, Thủy, Phong), tổng 144 mục.
- 06/11 09:25 · Claude (lab-sounds) · âm Firefly mới vào lab, commit `1ef64be` nhánh `claude/lab-sounds` (từ `5312650`): bộ đếm (tích, Chớp, lên mốc, đứt), luồng khí C (bùng, lặp, nhịp, tan), sao băng M (ngôi đầu và cuối), D6–D8 phím 9 có âm riêng; chọn bản bằng số đo (`typing-game-review/captures/tu-tien/lab-sounds/measure-2026-11-06.md`); Chrome headless: mọi âm phát, 0 lỗi; 1078 test qua · chờ lab-element-kits gộp, anh nghe chốt
- 06/11 09:40 · Claude (lab-perf) · đo hiệu năng, RAM và độ đọc chữ của lab (1920 × 1080, DPR 1, M4, không cờ URL), nhánh `claude/lab-perf` · **RAM:** lúc mở lab có 2,87 GB texture GPU, trong đó 48 atlas phím 8 và 9 chiếm 1,87 GB dù chiêu phát bằng video; Chrome 9,8 GB, sau 40 lần tung 9,65 GB. Sửa: clip có video hoãn atlas (tải khi chiêu thứ tư không còn ô video hoặc video kẹt, thả sau 10 s); sau sửa texture 0,99 GB, Chrome 2,9 GB lúc mở và 3,1 GB sau 40 lần tung. Video giải phóng đúng (bỏ src, texture về 0, heap 90–115 MB); dấu đất mỗi hệ còn giữ 50 MB/hệ (tối đa 700 MB). **Khung hình** (không giới hạn 60 Hz): bầy quái 5,1–5,7 ms, 2–3 video 5,3–6,5 ms, p99 ≤ 14 ms, trước và sau như nhau; đổi lại chiêu thứ tư cùng lúc giật 0,45–0,7 s một lần cho mỗi atlas mới tải. **Chữ:** thẻ thay trên đầu quái lúc đỉnh từng chiêu; nền thẻ đục 0,9 kiểu Dragonhold đạt ≥ 11,5:1 ở cả 48 chiêu; chữ trần trượt 7:1 cả trên sân trống (4,9:1); với nền thẻ nhạt hơn 0,6, 33/48 chiêu để ≥ 50 % thẻ trên vùng sáng (nặng nhất: B6 Taixu Sword, Earth Ink Peaks, A1 Lotus, Wood Primordial Tree, Metal Geng, Pagoda D7, Thunder Field, Fire One Spark). Bảng hạ sáng 32 chiêu `READABLE_LIGHT` chỉ bật với `?readable=1` (33 → 12), mặc định giữ nguyên để anh so. Khuyên: thẻ chữ trong game dùng nền đục ≥ 0,8. Số thô: `typing-game-review/captures/tu-tien/lab-perf/`, tấm so `owner-review/2026-11-06/tu-tien/lab-perf/readable-before-after.jpg`, changelog `docs/changelog/2026-11-06-lab-perf.md` (game)
- 06/11 10:10 · Claude (lab-element-kits) · gộp `claude/lab-sounds` (merge `71493bf`, xung đột ở `__lab.meteor`: giữ cờ dry, sao băng dry không phát âm) và `claude/lab-perf` (merge `cbf4890`, không xung đột); sửa thêm: đồng hồ video chạy tiếp giữa các lần currentTime đứng (`909ca84`), atlas dấu đất đưa lên GPU ngay khi nạp, không đợi lúc cú trúng (`0162503`; trước đó D6 trễ 88–164 ms, nay 2–14 ms). 102 tệp, 1081 test qua; 4310 = `0162503`: phím 8, 9 (video), M, C, K chạy, 0 lỗi. Còn: clip đỉnh ở 0 s tung thẳng (chưa chọn trước) có thể trúng ở khung video đầu tiên hiện ra, ~0,1 s sau khi video bắt đầu.
- 06/11 09:58 · Claude (lab-readability) · độ đọc chữ trên quái lúc đỉnh từng chiêu phím 8, 9, C, M (C và M ở cả 14 hệ), nhánh `claude/lab-readability` (từ `cbf4890`) · Lab chưa có chữ trên quái nên thêm thẻ chữ thay (`?tags=1` hoặc phím T): 24 thẻ không chồng nhau, màu thẻ Dragonhold (chữ #FFF4D6 trên nền mực, nền đục 0,6), cách đầu quái 0,3 m. Đo trên khung chỉ có canvas (nền thẻ tính đè lên điểm ảnh phân vị 90 sau mỗi thẻ), 1920 × 1080, khung cố định. **Trước:** 745/1824 thẻ dưới 7:1, cả 76 lượt chiêu đều có thẻ hỏng, tệ nhất 4,2:1; sân trống 10,1:1; với nền đục 0,9 thì mọi thẻ ≥ 11,5:1. **Sửa (chỉ hạ phần phủ sau chữ):** mặt nạ thẻ chữ `view/skills/tag-mask.ts` (độ phân giải thấp, mép mềm). Mọi flipbook, sprite, khung đồ họa lúc đánh và ánh sáng trên thân quái chỉ giữ 0,3 ánh sáng sau thẻ; phần còn lại của chiêu sáng nguyên. Thêm trường `tagKeep` trong bảng ClipSkill, đặt 0,12 cho 15 chiêu còn đè chữ; phím M dùng 0,12 khi rơi. Số sát thương giờ né thẻ (luật sẵn có `setWordTags`). **Sau:** 0/1824 thẻ dưới 7:1, tệ nhất 7,06:1; mặc định lab không bật thẻ nên không đổi gì.

  | Nhóm | Lượt chiêu | Thẻ < 7:1 trước → sau | Tệ nhất trước → sau |
  |---|---|---|---|
  | Phím 8 | 18 | 291 → 0 | 4,2 → 7,06 |
  | Phím 9 | 30 | 392 → 0 | 4,18 → 7,07 |
  | Phím C (14 hệ) | 14 | 27 → 0 | 4,53 → 8,78 |
  | Phím M (14 hệ) | 14 | 35 → 0 | 4,45 → 7,58 |

  `tagKeep` 0,12 (các chiêu khác 0,3): Thunder Field, Light Judgement, Metal Geng, Wood Primordial Tree, Fire One Spark, Earth Ink Peaks, Thunder Nine Heavens, Light, Void, A1 Lotus, B2 Bodhi Palm, B3 Titan, B6 Taixu Sword, D1 Imperial Seal, D6 Yin-Yang Mirror.

  Lưu ý: khi bật thẻ, số tổng lớn có thể mất vì luật cũ của số ("không đè thẻ: xuống dưới, không được thì lên trên, không được nữa thì bỏ"), 24 thẻ làm kín chỗ phía trên. Sát ngưỡng: Ult Poison 7,1 ở mức 0,3.

  Số thô: `typing-game-review/captures/tu-tien/lab-readability/` (`before-scored.json`, `after-scored.json`); tấm so: `owner-review/2026-11-06/tu-tien/lab-readability/tags-before-after.jpg`
- 06/11 11:05 · Claude (lab-sound-mix) · lượt trộn âm cho mọi chiêu lab (phím 0–7, 8, 9, C, M), commit trên nhánh `claude/lab-sound-mix` (từ `cbf4890`); bảng số dưới đây · chờ lab-element-kits gộp, anh nghe chốt

  **Trộn âm lab, trước/sau (06/11).** Đo bằng ffmpeg ebur128 trên bản trộn offline của bản ghi âm lab (`scripts/visual/mix-lab-sound.mjs`, đồng hồ cố định), mỗi chiêu tung riêng trên bầy đứng yên. M: LUFS tức thời tối đa (400 ms); S: LUFS ngắn hạn tối đa (3 s); đỉnh: dBTP trước bộ giới hạn (trước: lab chạy thật không có bộ giới hạn nên trên 0 là vỡ tiếng; sau: phần trên −2 do bộ giới hạn mới giữ).

  | Chiêu | Bậc | M trước → sau | S trước → sau | Đỉnh trước → sau |
  |---|---|---|---|---|
  | 0 Phi Kiếm | thường | −16,3 → −19,3 | −22,7 → −25,6 | −7,7 → −10,1 |
  | 1 Ngự Kiếm | thường | −10,2 → −15,7 | −14,8 → −18,7 | −0,5 → −6,4 |
  | 3 Hồi Kiếm | thường | −10,8 → −16,6 | −18,9 → −24,8 | −1,3 → −8,4 |
  | 4 Lưu Quang Bộ | thường | −10,6 → −16,6 | −18,7 → −24,4 | −2,4 → −7,4 |
  | C luồng khí (4 từ, rồi Ẩu) | thường | −13,8 → −15,8 | −15,7 → −17,9 | −2,2 → −5,6 |
  | 2 Nhất Tuyến | nặng | −9,7 → −12,5 | −14,5 → −17,9 | +0,6 → −2,5 |
  | 5 Lạc Kiếm Trận | nặng | −9,7 → −12,4 | −12,3 → −15,4 | +1,7 → −1,0 |
  | M sao băng | nặng | −10,2 → −11,3 | −11,3 → −12,7 | +3,2 → +0,9 |
  | 8 Lôi Trụ | nặng | −8,5 → −11,2 | −12,2 → −16,1 | +4,2 → +0,5 |
  | 9 A4 Karmic Ember Tempest | nặng | −7,8 → −9,6 | −8,9 → −11,9 | +6,4 → 0,0 |
  | 6 Thiên Hà (tuyệt kỹ) | tuyệt kỹ | −7,6 → −9,8 | −9,1 → −11,7 | +8,3 → +1,6 |
  | 7 Vạn Kiếm | tuyệt kỹ | −7,8 → −9,5 | −8,7 → −10,8 | +10,1 → +5,0 |
  | 8 Fire One Spark | tuyệt kỹ | −8,0 → −9,3 | −8,8 → −10,8 | +7,3 → +1,9 |
  | 9 B1 Asura | tuyệt kỹ | −7,3 → −10,2 | −11,1 → −15,0 | +6,5 → +0,8 |
  | Dồn: 7, 8 tuyệt kỹ, M, 9 tuyệt kỹ, 2 trong 1,3 s | | −7,5 → −8,5 | −7,9 → −9,4 | +10,5 → +4,2 |

  - **Bậc:** trước, chiêu thường (−10,5 M) to ngang chiêu nặng (−9,7). Sau: thường −15,7…−19,3, nặng −9,6…−12,5, tuyệt kỹ −9,3…−10,2. Chiêu 9 A4 (cả sân, 77 cú) sát bậc tuyệt kỹ.
  - **Đuôi dồn không thành tiếng ù:** 6–9 s sau khi dồn 5 chiêu, S −30,8, bằng đuôi của riêng phím 7 (−31,5); trước là −27,5. Giới hạn giọng: trúng 6, chết 4, âm lớn 2 (giọng cũ nhất tắt dần 0,04 / 0,05 / 0,3 s); file phím 8, 9 tắt dần từ 3,6 s.
  - **Hạ nhạc trước cú lớn (bài 11):** nhạc xuống 6 dB (nặng) hoặc 7 dB (tuyệt kỹ) từ 0,3 s trước cú. Đo trên nền thử (nhiễu hồng): −7,1 dB 0,2 s trước phím 2 và lúc phím 6 phát, −5,8 dB 0,2 s trước đỉnh phím 6, −6,8 dB 0,2 s trước nhát quét phím 7. Lab chưa có nhạc: `?music=<url>` để nghe. Kỹ năng phím 8, 9 có cú đầu ngay khung phím thì chỉ hạ được từ lúc trúng.
  - **Tiếng gõ phím:** lab chưa có tiếng phím (repo chưa có gói phím nào). Đã giữ chỗ: tiếng hô chiêu thường −6 dB, nặng −3 dB; vang và vòng lặp khoét −3 dB ở 1–4 kHz; âm UI đi sau bộ giới hạn. Chiêu thường đứng khoảng 10 LU trên mức phím (−27 LUFS-M).
  - **Sửa kèm:** phím 8, 9 trước chạy bằng thẻ `<audio>` ngoài bộ trộn, file to nhỏ lệch nhau −3,3…−17 LUFS; nay đi qua bus, mỗi file về đúng bậc. `x-immortal-sword-progenitor-avatar` take 4 gần như câm (−37 LUFS), đổi sang take 3. Độ lợi âm Firefly của `1ef64be` tính bằng một thước đo sai (pyloudnorm lọc nhầm trục) nên luồng khí và sao băng nhỏ hơn 6–7 dB; nay đo lại bằng ebur128.
  - Số thô: `typing-game-review/captures/tu-tien/lab-sound-mix/` (`before/`, `after/`, `duck/`, `before-after.json`).
- 06/11 11:50 · Claude (lab-sound-mix) · tiếng gõ phím từ gói dùng chung Typing Feel (chỉ đọc, bộ mặc định `bright-clack`), commit `bd99e28` cùng nhánh `claude/lab-sound-mix` · chờ gộp, anh nghe chốt

  **Phím so với chiêu (06/11).** Dòng gõ 60 WPM (một phím mỗi 0,2 s) trên bản trộn của từng chiêu; mỗi phím đo 30 ms đầu ở dải tiếng tách 2–8 kHz: phím cao hơn chiêu bao nhiêu dB, và bao nhiêu phím nằm dưới chiêu. Trước: gói phím ở mức file trên bản trộn cũ. Sau: bus phím +7 dB (dòng gõ ≈ −26 LUFS-M, bậc phím −28…−24 của AUDIO_PIPELINE §4.3.3), mỗi phím hạ dải 2–8 kHz của chiêu 3 dB trong 45 ms; phím không bao giờ bị hạ hay ép.

  | Chiêu | Phím − chiêu, trung vị (dB) | 10 % phím tệ nhất (dB) | Phím nằm dưới chiêu |
  |---|---|---|---|
  | 0 Phi Kiếm | 10,8 → 23,1 | −8,0 → 3,9 | 36 % → 0 % |
  | 1 Ngự Kiếm | −7,9 → 3,9 | −14,5 → −1,4 | 61 % → 22 % |
  | 3 Hồi Kiếm | 25,2 → 36,6 | −1,4 → 11,2 | 23 % → 0 % |
  | 4 Lưu Quang Bộ | 33,7 → 45,6 | −5,7 → 6,6 | 23 % → 8 % |
  | C luồng khí | −2,9 → 7,7 | −9,0 → 3,1 | 62 % → 0 % |
  | 2 Nhất Tuyến | −0,2 → 11,4 | −14,9 → −4,0 | 50 % → 21 % |
  | 5 Lạc Kiếm Trận | −6,2 → 5,9 | −10,8 → 1,0 | 71 % → 8 % |
  | M sao băng | −10,9 → 1,1 | −14,3 → −2,3 | 65 % → 35 % |
  | 8 Lôi Trụ | 2,1 → 19,6 | −13,1 → −1,8 | 43 % → 14 % |
  | 9 A4 (cả sân) | −14,2 → 0,1 | −18,9 → −3,3 | 79 % → 50 % |
  | 6 Thiên Hà | −9,7 → 2,9 | −18,9 → −2,6 | 79 % → 31 % |
  | 7 Vạn Kiếm | −14,9 → −0,7 | −19,6 → −4,0 | 84 % → 55 % |
  | 8 Fire One Spark | −9,3 → 3,6 | −17,1 → −2,7 | 76 % → 34 % |
  | 9 B1 Asura | 2,0 → 15,2 | −17,4 → −1,6 | 46 % → 21 % |
  | Dồn 5 chiêu | −16,8 → 0,4 | −21,9 → −6,4 | 80 % → 49 % |

  Chiêu thường và nặng không còn lấp tiếng phím. Lúc dày nhất của tuyệt kỹ phím 7, A4 cả sân và khi dồn chiêu, khoảng nửa số phím ngang hoặc dưới chiêu trong dải của nó (trước: 80 %); đó là lúc chiêu lớn được phép to hơn phím (audio.md §5.4), anh nghe xem có cần hạ thêm không. Số thô: `typing-game-review/captures/tu-tien/lab-sound-mix/keys-after/key-snr.json`.
