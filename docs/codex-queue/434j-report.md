# Phiếu 434j — Sét lan rộng và bảy điểm Ngũ Lôi

Ngày 17/11/2026. **Đạt các cổng kỹ thuật của phiếu.** Sét lan phủ **67,73%** bề ngang camera chơi; bốn tầng **4 / 10 / 16 / 20 tia**, cùng lúc tối đa **20 tia**, góc thực nhỏ nhất **61,23°**. Bảy điểm đánh cách nhau tối thiểu **5,69 m**, tối đa **3 cột** chồng nhau. Trắng tối đa **2,194227%** trên 840 khung; p95 pha cột sét **6,60 ms** với đủ 100 quái. Chưa có nghiệm thu mỹ thuật mù 8,5 hoặc đánh giá nghe chủ quan.

## Giao nộp

- [thunder-codex-j.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-j.jpg): phân cảnh 431 cạnh sáu mốc ở Alt+1 và Alt+2.
- [thunder-codex-j.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-j.mp4): **7,000 giây, 210 khung, 30 fps**, H.264 2560×720, hai camera đặt cạnh nhau, có AAC.
- [Bảy điểm đánh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/round-3/top-seven-landings-sheet.jpg), [bảy điểm ở góc sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/round-3/behind-seven-landings-sheet.jpg), [khung giải mã video](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/round-3/video-decoded-sheet.jpg).
- [Số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/round-3/measure.json), [cổng kỹ thuật và âm thanh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/final-gates.json), [vòng đời tài nguyên](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/lifecycle.json).

Đã thêm dòng 434j vào `owner-review/2026-11-17/tu-tien/ABOUT.md`; giữ nguyên mọi JPG/MP4 cũ.

## Thay đổi

Tâm lan là quái gần người tung chiêu nhất. Bán kính tìm mỗi tầng **10,5 m**; ưu tiên đường dài ra rìa đàn và các nguồn cách nhau ít nhất 3 m. Bốn đợt phát ở **0,72 / 1,10 / 1,54 / 1,98 s**, mỗi tia vẫn dùng ảnh C đã chọn, neo ngực–ngực, biến thể có hạt giống và tắt trong 0,22–0,24 s. Góc chọn có dự phòng cho chuyển động; phép đo dùng góc thực của các đoạn đang sáng, gồm cả khoảng góc khép vòng. Khi thiếu quái ở một hướng, giữ đoạn hụt kết thúc bằng sparkle của thư viện.

Độ phủ đo bằng chênh lệch ảnh bình thường và ảnh ẩn riêng lớp C, ngưỡng chênh tối thiểu 24/255 ở một kênh; tính cả thân, nhánh và quầng nhìn thấy. Alt+1 đạt **64,61% tại 1,2 s**, **67,73% tại 2,0 s**; Alt+2 phủ hết ngang khung. Độ phủ giữa các điểm neo lớn nhất riêng là 57,03%, không dùng số này thay cho độ phủ ánh sét. Dành ngân sách cho chớp mây và dư điện; phép đếm bảo thủ cộng thêm tám flipbook dư điện bám quái vẫn không vượt 24.

Bảy điểm được chốt ở 2,4 s, ưu tiên mật độ trong bán kính 4,5 m và độ trải ra sân, giữ khoảng cách tối thiểu 5,4 m. Dành cụm đông nhất trong vùng đánh an toàn cách nhân vật trên 8 m cho cột cuối. Mật độ tại điểm cuối là **34 quái**, sáu điểm trước là **16 / 7 / 7 / 12 / 11 / 7**.

| Cột | Bắt đầu (s) | Sống (s) | Bề ngang đặt (m) |
| --- | --- | --- | --- |
| 1 | 2,40 | 0,86 | 3,4 |
| 2 | 2,88 | 0,84 | 3,4 |
| 3 | 3,36 | 0,88 | 3,4 |
| 4 | 3,84 | 0,86 | 3,4 |
| 5 | 4,32 | 0,90 | 3,4 |
| 6 | 4,80 | 0,88 | 3,4 |
| 7 | 5,14 | 0,86 | **5,6** |

Mỗi cột đổi ô nguồn mỗi **0,09 s**, có seed riêng, burst chân, bốn nhánh bò đất, `scarHot`, `scarCold` và `lichtenberg` riêng. Cột cuối mới có nhịp lóe hai khung mạnh nhất và hook rung màn hình. Các vết nguội còn đến pha 6–7 s, tan hết tại 7 s. Hook giật quái có sẵn được gọi tại từng chân cột và mỗi 0,16 s khi cột còn sống; ghi nhận **504 lần giật**. Hook finisher hiện có chạy tại 6 s, mỗi quái tối đa một lần trên hợp các vùng đánh.

Mỗi cột gọi đúng một tiếng `tt-sfx-pillar-thunder/take1.wav`; tốc độ **0,965–1,02559**, độ trễ **0,50–16,17 ms**. Sáu tiếng đầu có gain ×0,7, tiếng cuối ×1; pan theo điểm đánh. Cầu nối trong `thunder-ult-sound.ts` chỉ trang trí đồng bộ lời gọi take Lôi của hook cũ để truyền rate/delay/gain, khôi phục phương thức bằng `finally`; giữ bus, mute, voice cap và log của `LabSound`. Không sửa `skills-main.ts` hoặc `sound.ts`. Probe kiểm cả khôi phục khi hook ném lỗi và giữ nguyên cue khác.

Video dựng từ log âm thật, **7/7 cue cột khớp**, `missing = 0`; bù một khung theo quy ước log và lượng tử hóa sự kiện lên khung 60 Hz kế tiếp. AAC đo **−16,5 LUFS**, true peak **−1,0 dBFS**. Chưa nghe chấm chất âm.

## Ba vòng kiểm tra

Chrome headless trên server 3148 có sẵn, High, DPR 1, 1280×720 mỗi camera, nền `#353a40`. Đủ các mốc **1,2 / 2,0 / 3,0 / 4,2 / 5,5 / 6,5 s** ở Alt+1 và Alt+2. Đã mở ảnh cả ba vòng, đối chiếu phân cảnh và mở tấm bảy điểm đánh, tấm giải mã clip.

| Vòng | Phủ ngang | Tầng / tia cùng lúc / góc nhỏ nhất | Cột / chồng / cách nhỏ nhất | Trắng lớn nhất | p95 |
| --- | --- | --- | --- | --- | --- |
| 1 | 67,73% | 4 / 20 / 61,23° | 7 / 3 / 5,69 m | 1,111762% tại mốc chụp | 7,20 ms |
| 2 | 67,73% | 4 / 20 / 61,23° | 7 / 3 / 5,69 m | 1,111762% tại mốc chụp | 6,40 ms |
| 3 | 67,73% | 4 / 20 / 61,23° | 7 / 3 / 5,69 m | **2,194227% / 840 khung** | **6,60 ms** |

Vòng 1 có ba lượt impact nhỏ rơi pool ở tầng 4. Đã tăng pool impact 16→24, sparkle 24→32; vòng 2–3 không rơi lượt nào. Vòng 3 quét đủ 420 khung/60 Hz mỗi camera: RGB ≥0,95 tối đa 2,194227%, Rec.709 ≥0,95 tối đa **2,353950%**, cùng tại Alt+2 **5,15 s**. Mây giữ nguyên dải trên khung, không sửa `cloud-volume*`.

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**. Không chạy build hoặc bộ test game.
- p95 CPU + chờ GPU qua `readPixels`: **6,60 ms**, ANGLE Metal / Apple M4. Bốn lượt, bỏ lượt làm nóng; **630 mẫu** trong 2,4167–5,9000 s. Mỗi lượt đủ **87 quái giữ vị trí + 13 walker** ở đầu và cuối; quái vẫn giật và walker vẫn bước.
- Probe riêng: năm chu kỳ phát/hủy/phát lại, lịch/biến thể tái lập, góc ≥40°, bán kính tìm ≤10,5 m, bảy điểm cách ≥5 m, thời gian sống hợp lệ, bước lớn 7 s, hủy giữa pha. Hình học/vật liệu ổn định; **20/20 texture** được giải phóng đúng một lần, dispose lặp an toàn. Đổi hình đo từng mili giây: **90 ms**.
- Không exception. Cảnh báo KTX2Loader và atlas Kim có sẵn vẫn xuất hiện; không sửa làn khác.

## Phạm vi, phần bỏ qua và dọn dẹp

Chỉ sửa/thêm trong `games/.wt-ic-lab-all/src/lab/`: `thunder-ult-chain.ts`, `thunder-ult-nguloi.ts`, `thunder-ult-sound.ts`, `thunder-ult-review-j.mjs`, `thunder-ult-probe-j.mjs`, `thunder-ult-deliver-j.mjs`; báo cáo này và các tệp review/ABOUT được phép. Không sửa game chính, `five-thunder.ts`, flipbook, logic quái hoặc audio-lab.

Không sinh ảnh/âm mới vì bộ C, cột Ngũ Lôi, bò đất, vết cháy và take Lôi hiện có đủ cho công thức này. Không đưa vào game chính; phiếu chỉ yêu cầu lab. Chưa chạy chấm mù mỹ thuật hoặc nghe chủ quan, nên không ghi nhận nghiệm thu 8,5.

Chrome của các lượt chụp đã đóng; profile tạm đã được driver xóa, xác minh trong [browser-cleanup.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434j/browser-cleanup.json). Đã xem danh sách prune khô rồi xóa **897 ảnh thô, 804,499 MB**, chỉ các tệp của phiếu này; giữ **14 tấm xem**, số đo và bản dựng âm. Đã dựng lại mục lục review. Giữ server 3148. Không commit/push/reset/clean/stash.

Owner cần xem độ phủ ở 1,2–2,0 s, bảy điểm đánh so le và điểm nhấn cuối 5,14 s; nghe bảy tiếng sét trong clip.
