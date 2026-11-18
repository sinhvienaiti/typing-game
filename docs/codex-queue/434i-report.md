# Phiếu 434i — Sét lan ba tầng, cột Ngũ Lôi kéo dài 3,6 giây

Ngày 17/11/2026. **Đạt các cổng kỹ thuật.** Sét C lan ba tầng **4 / 8 / 16 tia**; góc tỏa thực nhỏ nhất **65,91°** trên cả hai camera. Cột đánh từ **2,4 đến 6,0 s**, đổi hình mỗi **0,09 s**, có ba nhịp lóe dài hai khung. p95 với đủ 100 quái trong pha cột sét là **6,10 ms**; trắng tối đa **0,844944%** trên 840 khung. Chưa có hai giám khảo mù nghiệm thu mỹ thuật 8,5; âm chưa được nghe đánh giá chủ quan.

## Giao nộp

- [thunder-codex-i.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-i.jpg): nửa phải phân cảnh 431 và đủ sáu mốc ở hai camera.
- [thunder-codex-i.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-i.mp4): **7,000 s, 210 khung, 30 fps**, H.264 2560×720, Alt+1/Alt+2 đặt cạnh nhau, có AAC từ âm đang dùng trong lab.
- [Khung giải mã video](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/round-3/video-decoded-sheet.jpg), [chuỗi đổi hình cột](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/round-3/top-column-motion-sheet.jpg).
- [Số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/round-3/measure.json), [cổng kỹ thuật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/final-gates.json), [kiểm số tia](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/ray-cap-audit.json), [vòng đời tài nguyên](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/lifecycle.json).

Đã thêm dòng 434i vào `owner-review/2026-11-17/tu-tien/ABOUT.md`. Giữ nguyên mọi JPG/MP4 cũ.

## Cách làm

Dùng lại đúng ảnh C owner chọn: `games/immortality-cultivation/art-src/lab/vfx/thunder/stills-55/thunder-bolt-ff.v1-try3.png`. Giữ ba bản đã có, thêm **lật ngang và dọc** thành biến thể thứ tư; tệp `thunder-chain-c-flip-xy.png` có chỉ dẫn xử lý cơ học cạnh nó trong `.prompt.txt`. Cập nhật JSON neo. Không sinh ảnh AI mới, không đổi nguồn C.

Mỗi quái nguồn tỏa 2–4 quad C với biến thể khác nhau trong cùng cụm; chọn quái chưa bị chạm trong bán kính 6 m. Hướng trống kết thúc bằng đoạn ngắn và sparkle có sẵn. Đầu đoạn hụt bám theo quái nguồn, tránh góc bị ép lại khi đàn quái di chuyển. Góc chọn có khoảng dự phòng; phép đo dùng góc phương vị thế giới của các đoạn đang sáng, bao gồm khoảng góc khép vòng. Các tia vẫn neo vào ngực quái.

Giới hạn ba tầng truyền; tầng cuối dừng phát triển mạng. Khi thiếu ngân sách, tầng sau giảm còn hai tia mỗi nguồn rồi bỏ nguồn xa nhân vật nhất. Pool 24 quad tái sử dụng theo tuổi tia; dành bốn suất cho thân và nhánh chớp mây. Mức đo lớn nhất là **16 tia đặt riêng** gồm C, cột, bò đất và các nhánh mây/dư điện. Đếm bảo thủ thêm tối đa tám flipbook dư điện bám quái cho tổng **24**, vẫn đạt trần. Nhánh vẽ sẵn trong cùng texture C không được đếm thành quad mới.

| Pha | Mốc cố định |
| --- | --- |
| Mây tụ | 0–0,6 s |
| Sét lan | 0,6–2,4 s; phát các tầng ở 0,72 / 1,32 / 2,12 s, chớp lại tầng 1–2 tại 1,06 / 1,82 s |
| Cột Ngũ Lôi | 2,4–6,0 s; dùng một cột liên tục, chọn khung từ atlas trộn 72 ô đã có |
| Mây tan và dư điện | 6,0–7,0 s; hết sạch hiệu ứng tại 7,0 s |

Ba nhịp bùng tại **2,4 / 3,6 / 4,8 s**, mỗi nhịp **2/60 s**. Tám nhánh bò đất đổi hướng, khung và độ sáng có hạt giống suốt pha cột; sparkle tái phát tại chân. Quái quanh chân cột gọi hook `host.stun` hiện có mỗi 0,16 s; ghi nhận **861 lần giật**. Giữ quái để xem giật trong pha cột, dời hook finisher hiện có tới 6,0 s. Không sửa `skills-main.ts` hoặc logic quái.

Âm gọi lại `host.sound("climax")` ở **2,4 / 3,2 / 4,0 / 4,8 / 5,6 s**: dùng `tt-sfx-pillar-thunder/take1.wav`, thân 0,7 s và đuôi 0,4 s nên các lần nối chồng 0,3 s. Mây tụ và đuôi dùng `tt-sfx-ult-thunder-edict/take1.wav` như trước. Không sửa/thêm tài nguyên âm. `capture-mix.wav` chỉ là bản dựng âm của video trong thư mục review, từ log sự kiện thật qua bộ mix sẵn có; **missing = 0**. Bù 1/60 s theo quy ước log trước bước khung. Đo AAC: **−17,1 LUFS tích hợp, true peak −1,1 dBFS**; chưa nghe chủ quan.

## Ba vòng và xác minh

Chrome headless, localhost:3148, High, DPR 1, 1280×720 mỗi camera; nền `#353a40`. Đã mở ảnh cả ba vòng và đối chiếu phân cảnh. Các mốc: **1,2 / 2,0 / 2,5 / 4,2 / 5,8 / 6,5 s**, đủ Alt+1 và Alt+2.

| Vòng | Tia tầng 1 / 2 / 3 | Góc thực nhỏ nhất | Cột | Trắng lớn nhất | p95 |
| --- | --- | --- | --- | --- | --- |
| 1 | 4 / 11 / 14 | 39,09° — chưa đạt | 3,6 s | 0,744900% tại các mốc chụp | 6,30 ms |
| 2 | 4 / 8 / 16 | 65,91° | 3,6 s | 0,766385% tại các mốc chụp | 6,40 ms |
| 3 | 4 / 8 / 16 | 65,91° | 3,6 s | **0,844944% / 840 khung** | **6,10 ms / đủ 100 quái** |

Trong vòng cuối, kiểm tra độc lập phát hiện nhánh dư điện có thể vượt trần nếu cộng cả nhánh phụ. Đã bỏ nhánh phụ của các đoạn dư điện, giữ flipbook bám quái và chụp lại riêng 6–7 s; 0–6 s giữ nguyên. Số đo cuối và video dùng cùng bản sửa này.

- `./node_modules/.bin/tsc --noEmit --incremental false` trong worktree: **0 lỗi**. Không chạy build hoặc bộ test game.
- Probe riêng: năm chu kỳ hủy/phát lại, lịch và biến thể có hạt giống tái lập, các góc kế hoạch ≥40°, khoảng cách ≤6 m, không rơi pool, hình học/vật liệu ổn định. Kiểm bước lớn 7 s và hủy giữa pha. **20/20 texture** được giải phóng đúng một lần; dispose lặp an toàn.
- Kiểm từng mili giây: đổi khung đúng **90 ms**, dùng 40 ô khác nhau trong 3,6 s; ba đỉnh đo 34 ms do bước lấy mẫu 1 ms, tương ứng hợp đồng hai khung 60 Hz.
- Quét ảnh không mất dữ liệu **420 khung/60 Hz mỗi camera**: RGB ≥0,95 tối đa **0,844944%**, Rec.709 ≥0,95 tối đa **0,884115%**, đều dưới 6%. Quét hình học 842 mẫu ở hai góc xác nhận góc tỏa và giới hạn số tia.
- Đo cột riêng: **87 TargetField + 13 walker = 100 quái**, đủ ở đầu và cuối mỗi lượt; bốn lượt ×210 mẫu trong **2,4167–5,9000 s**, bỏ lượt làm nóng, còn **630 mẫu**. p95 CPU + chờ GPU qua `readPixels` **6,10 ms**, p95 CPU **1,40 ms**, ANGLE Metal / Apple M4. Giữ 87 quái tại vị trí để chúng không rời sân; 13 walker vẫn bước và quái vẫn giật. Lượt march thường có một quái đang rời sân ở đầu cột nên lưu riêng, không dùng làm bằng chứng “đủ 100 quái”.
- Không exception. Cảnh báo KTX2Loader và atlas Kim có sẵn vẫn xuất hiện; không sửa lane khác.

## Phạm vi và dọn dẹp

Chỉ sửa/thêm trong `games/.wt-ic-lab-all/src/lab/` các tệp:

- `thunder-ult-chain.ts`, `thunder-ult-chain-card.ts`, `thunder-ult-nguloi.ts`;
- `thunder-ult-prepare-c.mjs`;
- `thunder-ult-review-i.mjs`, `thunder-ult-probe-i.mjs`, `thunder-ult-perf-i.mjs`, `thunder-ult-deliver-i.mjs`.

Tài nguyên chỉ trong `art-src/lab/vfx/thunder/`: JSON neo, bốn biến thể C và các chỉ dẫn cạnh PNG. Không sửa game chính, `five-thunder.ts`, flipbook Ngũ Lôi, cloud-volume, docs Tu Tiên hoặc audio-lab. Không tạo ảnh/âm nguồn mới vì thư viện đã đủ. Không khởi động/dừng server; không commit/push/reset/clean/stash.

Đã xem danh sách prune khô rồi xóa **885 ảnh thô, 785,295 MB**, chỉ trong ba thư mục vòng của phiếu này; giữ 13 sheet, số đo và bản dựng âm. Chrome của các lượt chụp đã đóng và profile tạm đã được driver xóa. Một Chrome do lane khác mở giữa hai lượt được giữ nguyên; chi tiết trong [browser-cleanup.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434i/browser-cleanup.json). Đã dựng lại mục lục review.

Owner cần xem độ lan ở 1,2–2,4 s, nhịp đổi hình và âm lặp trong 2,4–6,0 s. Chưa ghi nhận nghiệm thu mỹ thuật 8,5 hoặc đánh giá nghe của owner.
