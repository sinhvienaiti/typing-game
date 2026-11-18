# Phiếu 434g — Sét nối quái dày và phủ đủ đoạn

Ngày 17/11/2026. **Đạt các cổng kỹ thuật của phiếu sau đúng 3 vòng sửa.** Ở camera chơi, cả 8 bước đạt ≥14 px theo probe kế thừa; đoạn nối phủ 100%, hai đầu không hở. Chưa có hai giám khảo mù chấm mỹ thuật 8,5; không ghi nhận nghiệm thu mỹ thuật.

## Giao nộp

- [thunder-codex-g.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-g.jpg): phân cảnh 431 cạnh Alt+1 và Alt+2, các mốc 0,4 / 1,2 / 2,2 / 3,0 s.
- [thunder-codex-g.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-g.mp4): 4 giây, 30 fps, 120 khung, H.264; hai camera 1280×720 đặt cạnh nhau thành 2560×720. Giữ nguyên AAC 4 giây của bản 434f và mốc đánh 2,0 s.
- [Từng bước ở camera chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/round-3/hop-check-sheet.jpg), [từng bước sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/round-3/behind-hops-sheet.jpg), [khung giải mã MP4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/round-3/video-decoded-sheet.jpg).
- [Số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/round-3/measure.json), [các cổng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/final-gates.json), [vòng đời tài nguyên](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/lifecycle.json).

Đã thêm dòng 434g vào `owner-review/2026-11-17/tu-tien/ABOUT.md`. Giữ toàn bộ bản cũ.

## Thay đổi

Chỉ ghi sáu file có tiền tố `thunder-ult-` trong `games/.wt-ic-lab-all/src/lab/`:

| File | Nội dung |
| --- | --- |
| `thunder-ult-nguloi.ts` | Neo hai đầu card theo ngực hai quái; dùng cùng chuẩn thân nguồn 22 px cho mọi bước, bù khoảng cách camera, không có hệ số giảm theo chỉ số bước. Ánh sét nối hiển thị trên thân quái để đoạn cực ngắn không bị che. Giữ hold 0,22 s và fade 0,14 s. |
| `thunder-ult-bolt-profile.ts` | Bảng vị trí tâm và bề ngang thân lấy từ pixel thật của ô 0 atlas `boltA`, dải hàng 0,23–0,73. Dùng để đặt và kéo giãn nguồn, tách độ dày thân khỏi độ lượn ngang và phần đệm. |
| `thunder-ult-chain.ts` | Truyền camera cho lớp art và trả đúng bề rộng card vào báo cáo. Không đổi thuật toán chọn quái hay lịch sự kiện. |
| `thunder-ult-review-g.mjs` | Chụp hai camera, đo từng bước, quét độ phủ dọc đoạn nối và toàn bộ 480 khung; đo p95 ở stress 100 quái. |
| `thunder-ult-probe-g.mjs` | Kiểm nguồn thật, hủy/lặp, pool và giải phóng tài nguyên. |
| `thunder-ult-deliver-g.mjs` | Ghép tấm xem, xuất MP4, kiểm cổng và đối chiếu dữ liệu 434f. |

Công cụ hình ảnh là **art Ngũ Lôi có sẵn**, theo `game-vfx-production` và `game-vfx-layered`. Mọi pixel thân sét vẫn lấy từ atlas thật; bảng chỉ điều khiển cách lấy mẫu và đặt hình. Không tạo ảnh, âm hoặc atlas mới. Các bước đều dùng thân gãy `boltA` ô 0 để tránh đổi sang ô có thân/phần đệm khác nhau. Nguồn vẫn import từ `five-thunder.ts`; không sửa file đó hoặc flipbook. `crawlA`–`crawlD`, scar, burst, cột chính và mây không đổi.

## Ba vòng

Chrome headless, localhost:3148, High, DPR 1, 1280×720 mỗi camera, nền `#353a40`; camera chơi Alt+1 và góc sau lưng Alt+2.

Bề dày là **giá trị nhỏ nhất của ba lát cắt vuông góc tại 35% / 50% / 65%**, ở 0,05 s sau mỗi bước. Đếm dải liên tục dài nhất có Rec.709 tăng ≥0,1 so ảnh đối chứng cùng thời điểm, không cộng các nhánh rời. Không dùng tham số card thay số đo pixel, không khẳng định độ rộng này trong giai đoạn tan.

Độ phủ: quét dọc 0–100% đoạn chiếu giữa hai ngực, tối thiểu 101 lát và khoảng cách không quá 1 px; lát có dải liên tục ≥3 px tăng Rec.709 ≥0,1 được tính có thân art. Kiểm riêng khoảng hở ở đầu/cuối. Đây là độ phủ theo trục đoạn nối, không phải tỷ lệ diện tích hình chữ nhật.

| Vòng | Bề dày bước 1→8 (px) | Độ phủ bước 1→8 (%) | Trắng tối đa | p95 (ms) |
| --- | --- | --- | --- | --- |
| 1 | 112 / 35 / 36 / 71 / 30 / 93 / 0 / 14 | 100 / 100 / 100 / 100 / 100 / 100 / 0 / 100 | 0,768772% tại mốc pha | 6,20 |
| 2 | 95 / 37 / 33 / 60 / 33 / 73 / 1 / 14 | 100 / 100 / 100 / 100 / 100 / 93,18 / 50,50 / 100 | 0,768772% tại mốc pha | 6,10 |
| 3 | **112 / 47 / 52 / 71 / 50 / 109 / 19 / 23** | **100 / 100 / 100 / 100 / 100 / 100 / 100 / 100** | **0,768772% trên 480 khung** | **6,00** |

Vòng 1: sửa probe dùng chung trạng thái giữa các bản mô-đun Vite rồi đo lại cùng cấu hình; số 0 đồng loạt từ probe lỗi đã bị loại. Phép đo chính thức vòng 1 tắt riêng từng tia nhưng các tia còn lại vẫn sáng, nên bước 7 còn bị chồng sáng. Vòng 2–3 chụp riêng một tia trên đúng nền cùng khung, tắt các tia nối khác ở cả ảnh bật và tắt để loại chồng sáng. Vòng 3 còn sửa che khuất bởi thân quái và giới hạn độ lượn để giữ thân trong card. Không làm vòng sửa thứ tư.

Bước cuối vòng 3 ở 1,25 / 1,35 s đạt **19 / 23 px**; khoảng hở đầu và cuối của cả tám bước đều **0 px**. Cùng một chuẩn thân nguồn được dùng cho mọi bước. Độ rộng sau bloom còn phụ thuộc chiều dài, góc chiếu và quầng nguồn, nên số đo không bằng nhau tuyệt đối. Quét dọc bổ sung: ≥14 px trên 100% lát của bảy bước; riêng bước 7 đạt trên 98,02% lát, hai lát sát đầu có 12 px. Ba lát cắt nghiệm thu của bước 7 đều ≥19 px; toàn đoạn vẫn có thân liên tục.

## Kiểm tra

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**. Không chạy build hoặc bộ test game.
- `node --import tsx src/lab/thunder-ult-probe-g.mjs`: **PASS**; hủy/lặp 5 lần, không rơi pool, không tăng số hình học/vật liệu; 16 texture giải phóng đúng một lần, dispose lặp an toàn.
- Stress đúng **87 TargetField + 13 walker = 100 quái**, 4×240 mẫu; bỏ lượt làm nóng, gộp 720 mẫu. p95 tổng CPU + chờ GPU qua `readPixels`: **6,00 ms ≤16,7 ms**, ANGLE Metal / Apple M4.
- Quét **480 PNG không mất dữ liệu**, 240 khung/60 Hz mỗi camera, cả 4 giây. Trắng RGB ≥0,95 tối đa **0,768772%**; Rec.709 ≥0,95 tối đa **0,829753%**, đều ≤6%.
- Cột chính vẫn **74–183 px** theo probe pha. Mây đặc ở dải **15,56–22,78%** từ mép trên camera chơi, phủ tâm quái **0**; góc sau lưng giữ như 434f.
- Đối chiếu JSON với 434f: **đúng nguyên đường chọn quái, đầu–cuối và mốc từng bước**; dữ liệu cột, crawl, vết đất và mây ở 2,2 / 3,0 s giống hệt.
- Góc đổi hướng giữ nguyên: +52,40 / −63,71 / +45,47 / −52,31 / +76,49 / −64,54 / +48,10°.
- Không exception. Còn các cảnh báo sẵn có của host về KTX2Loader, atlas Kim và nhiều bản Three trong probe; không sửa lane khác.
- Đã mở tấm xem của cả ba vòng, hai camera cuối, nguồn và khung giải mã MP4. Video có 120 khung/4 giây và âm 4 giây.
- Chrome của lượt chạy đã tắt, profile tạm đã xóa; [xác nhận dọn trình duyệt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434g/browser-cleanup.json).

Không sửa game chính, tài liệu Tu Tiên, `cloud-volume*`, `five-thunder.ts`, ảnh/flipbook hoặc audio-lab. Không khởi động/dừng server, không commit/push/reset/clean/stash. Không tạo ảnh/âm mới vì phiếu yêu cầu tái dùng Ngũ Lôi. Owner cần xem đoạn nối cuối trong video và độ gãy của thân tia sau khi kéo giãn; chưa có chấm mù mỹ thuật.

## Dọn khung

Đã xem danh sách capture-prune khô: chỉ 738 file của riêng 434g, 653,571 MB; giữ các sheet, số đo, MP4 và ABOUT; không đụng bản 434f hoặc ảnh của lane khác. Kết quả áp dụng được lưu cùng thư mục capture và mục lục review được dựng lại sau khi dọn.
