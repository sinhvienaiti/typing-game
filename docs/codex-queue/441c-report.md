# Phiếu 441c — Quang, giữ cỡ nổ và sửa ba lỗi

17/11/2026. Đã tự chụp, mở xem **3 vòng** tại lab 3148, nền `?ground=%23353a40`. Cỡ D riêng vượt **45% × 35%**; tại khung nổ, toàn cụm có lề **≥3%** ở cả hai camera. Quái hết đốm trắng, đuôi D hết vòng. Kiểm kiểu **0 lỗi**; p95 **5,90 ms**.

## Giao nộp

- [Ảnh light-ult-codex-g.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-g.jpg).
- [Video camera chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-g.mp4), [video sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-g-behind.mp4).
- Hai clip: **4 s, 120 khung, 30 fps, 1280×720, H.264 + AAC**; lần lượt **2.298.518** và **2.426.411 byte**. ffmpeg giải mã toàn bộ không lỗi; đã mở xem [sheet chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-g-3/441c-decoded-top-sheet.jpg) và [sheet sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-g-3/441c-decoded-behind-sheet.jpg). Giữ nguyên mọi bản cũ a–f.

## Đã sửa

- Giữ ngang D **36,5 m**, cao **28 m**: diện tích mặt phẳng **20,857 lần** bản 441, lớn hơn nhẹ so với 441b. Hạ **neo hiển thị** dọc mặt đất tối đa **6,5 m** về phía camera theo độ cao góc nhìn; camera chơi dùng đủ, góc sau lưng giữ neo cũ. Không đổi điểm chọn mục tiêu, trục hoặc độ dài tia; đầu tia vẫn chìm trong hình D. Neo hiển thị đứng y=0,025 m, đóng băng trong một lượt, không trượt theo camera punch. Đây là hạ neo ảnh như phiếu cho phép, không di chuyển điểm trúng của tia.
- Tia lửa theo cùng neo hiển thị; giữ **120 vệt**, 14 tia tỏa, tầm đạn đạo 4–15 m. Hắt sáng mềm giảm 300→4 để ánh sáng không tràn sát mép hoặc tẩy màu quái; gain chính D vẫn 1,35, lóe phụ vẫn 2 khung, camera punch và âm giữ nguyên.
- Phản ứng nổ ở lab dùng shove **1,65 m**, giữ ngắn 0,16 s và status viền vàng **0x49320e** trong 0,24 s. Bỏ lần gọi `TargetField.hit` chung ở vụ nổ này vì nó thêm lóe HDR, đổi màu cả thân và có thể làm quái tan sáng. Điều này cũng bỏ trừ máu từ lần gọi hit chung đó trong **lab**, không thay gameplay production. Phản ứng quét giữ hook cũ, status vàng cũng giảm sáng.
- Trong bán kính 13,5 m, vật liệu quái giới hạn `outgoingLight≤0,65` khi nổ; bật từ 1,95 tới 2,7 s, tắt khi clear. Kênh viền vàng đầu vào cũng dưới 0,9. Hook shader nằm trong file Quang, không sửa `herd.ts` hay vật liệu gốc trong file khác.
- Không cắt lại tài nguyên: chỉ lấy các frame atlas **0–5**, nội suy trong đoạn này, gain tan từ age 0,10→0,40 s. Không bao giờ lấy frame 6 trở đi; nguồn bắt đầu lộ hình vòng ở khoảng frame 8. D tắt tại **2,35 s**. Đã đối chiếu [sheet nguồn](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-1/source-sheet.jpg), [chuyển pha](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-transition-sheet.jpg) và các sheet giải mã; đoạn D không còn vòng đuôi. Thấu kính cầm tay theo 439 vẫn được giữ.

## Ba vòng tự xem và đo

| Vòng | Tự chấm | Lề tối thiểu chơi / sau lưng | D riêng chơi | Trắng toàn khung | Thân quái | Kết quả |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 7,5 | 1,67% / 0% | 52,03% × 35,00% | 0,058919% | Kênh tối đa 0,969, đo mọi quái | Hình D hết cắt, đuôi hết vòng; hạt và hắt sáng chưa đủ lề, kênh thân còn cao. |
| 2 | 7,7 | 11,25% / 3,19% | 52,50% × 37,50% | 0,066298% | Chưa hợp lệ | Hình đạt; probe bị Vite tải hai module có/không `?t`, nên ảnh mask không phải mask. Không dùng số này nghiệm thu. |
| 3 | 7,7 | **11,25% / 3,19%** | **52,50% × 37,50%** | **0,066298%** | **Kênh và Y tối đa 0,686275; 0 pixel trắng** | Sửa registry probe, đo lại thành công, quay clip và đo GPU. |

Đã mở xem [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-1/441c-comparison.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-2/441c-comparison.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-comparison.jpg). Tự chấm mô tả kết quả sửa lỗi, **không thay nghiệm thu hai giám khảo mù ≥8,5 ở host chơi**.

## Số đo cuối

Chrome headless, High, DPR1, 1280×720. Độ sáng Rec.709 trên RGB chuẩn hóa; bbox lấy **mọi pixel ΔY≥0,15**. Mỗi cặp bật/tắt cùng thời gian, camera và trạng thái quái. Tách riêng cụm D + vệt lăng kính + đèn ấm để tia hội tụ, bụi quạt có sẵn không làm sai cỡ và lề của cú nổ. Không dùng bbox thành phần liên thông để bỏ hạt lẻ khi kiểm lề.

Khung nổ: tìm mean Y cao nhất trong tròn 120 px quanh neo hiển thị trong 31 mẫu 60 Hz, 1,95–2,45 s. Chơi **1,983333 s**, sau lưng **1,966667 s**; phủ sáng quanh neo **91,74% / 89,05%**. Lề dưới đây chỉ báo tại khung nổ xác định theo phép đo này.

| Camera | Bbox mọi pixel của cụm nổ | Cỡ cụm | Lề trái / phải / trên / dưới | D riêng |
| --- | --- | --- | --- | --- |
| Chơi | [293,81,672,305] px | 52,50% × 42,36% | 22,89 / 24,61 / **11,25** / 46,39% | 672×270 px = **52,50% × 37,50%** |
| Sau lưng | [243,23,765,502] px | 59,77% × 69,72% | 18,98 / 21,25 / **3,19** / 27,08% | 765×511 px = 59,77% × 70,97% |

Cụm liên thông lớn nhất cũng đạt: chơi **49,06% × 42,36%**, sau lưng **53,28% × 61,39%**. Trắng toàn khung cao nhất **0,066298%≤6%**; lấy max cả các pha và toàn bộ 31 khung quét mỗi camera, không chỉ khung có mean Y cao nhất. Các cổng cũ về nêm, độ thuôn, kính, ROI sau lưng, quầng/lõi tia đều qua. Trục hội tụ sai số **0,00000121°**, do số chấm động; không sửa thuật toán tia.

Thân quái: sáu thời điểm **1,95 / 1,9667 / 2,00 / 2,05 / 2,15 / 2,30 s**, hai camera. Chụp riêng mesh quái với ánh sáng hiện tại, tạm ẩn các mesh khác; mặt nạ trắng lọc đúng bán kính **13,5 m**, phục hồi toàn bộ ngay sau chụp, không bước đồng hồ. Đọc max từng kênh và max Y trên mặt nạ; **không tính hình D phủ trước thân** là màu vật liệu của quái. Kết quả mọi mẫu: max kênh **175/255=0,686275**, max Y **0,686275**, không pixel có ba kênh ≥0,95.

Bằng chứng giữ để đo lại:

- D riêng chơi: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-D-top-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-D-top-off.png); sau lưng: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-D-behind-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-D-behind-off.png).
- Cụm nổ chơi: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-explosion-top-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-explosion-top-off.png); sau lưng: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-explosion-behind-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-explosion-behind-off.png).
- Thân quái chơi: [màu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-body-top-1.967.png) / [mask](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-body-top-1.967-mask.png); sau lưng: [màu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-body-behind-1.967.png) / [mask](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-body-behind-1.967-mask.png).
- Khung trắng cao nhất behind 2.266667 s: [ảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-scan-behind-19.png) / [nền](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-scan-behind-19-off.png).
- JSON [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-1/441c-measure.json), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-2/441c-measure.json), [vòng cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-measure.json); [âm thực](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-g-3/441c-sound-takes.json), [kiểm video](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-g-3/441c-video-check.json). Âm `tt-sfx-ult-light` tại 0 / 0,600 / **1,950 s**, khớp nổ.

## Kiểm kiểu, hiệu năng và phạm vi

`./node_modules/.bin/tsc --noEmit`: **0 lỗi** sau thay đổi cuối. `node --check light-ult-review-g.mjs`: qua. Không chạy build hoặc bộ test game.

`stress.html`: **87 TargetField + 13 walker = 100** mỗi lượt, 240 mẫu/lượt; bỏ một lượt làm nóng, gộp **720 mẫu**. `total=CPU+GPU readPixels`, khóa `heavy.sh --perf`. Renderer **ANGLE Metal / Apple M4**, không phần mềm. p95 ba lượt **6,10 / 5,60 / 6,00 ms**, gộp **5,90 ms**, CPU gộp **1,40 ms**. Không exception JS/shader. Cảnh báo KTX2Loader và atlas Kim ở làn khác giữ nguyên.

Chỉ sửa trong `games/.wt-ic-lab-all/src/lab/`: `light-ult-burst.ts`, `light-ult-impact.ts`, `light-ult-fan.ts`; thêm `light-ult-body-probe.ts`, `light-ult-review-g.mjs`. Ngoài ra chỉ ghi capture, g.jpg/g.mp4/g-behind.mp4, thêm một dòng ABOUT owner và báo cáo này. Không sửa `skills-main.ts`, `herd.ts`, `UltCameraPunch`, audio-lab hoặc production. Không tạo ảnh/âm/video AI mới, không sửa atlas hay VFX_LIBRARY vì dùng nguồn D đã duyệt.

Tái lập từ repo cha: `ROUND=3 FINAL=1 CHROME_FLAGS='--use-angle=metal' .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review-g.mjs --width=1280 --height=720 --dpr=1`.

Không khởi động/dừng lại server 3148; các Chrome do phiếu tạo đã thoát. Không commit, push, reset, clean, stash. Không dựng lại index review vì các file index nằm ngoài phạm vi ghi cho phép.

## Dọn và owner cần xem

Dọn riêng `round-g-1..3`, `frames-g-round-3`, `frames-g-behind-round-3`, `video-check-g-3` bằng công cụ prune, dry-run trước apply; giữ sheet, cặp đo được liên kết và JSON. Đã xóa **1039 ảnh thô/trung gian, 854.083 MB**, giữ **23 ảnh/sheet**, từ chối **0** mục. Nhật ký: `captures/tu-tien/light-ult-439/441c-prune-{dry,result}.{json,log}`.

Owner xem **1,95–2,6 s** của hai clip: cỡ D vẫn lớn, toàn hình nổ nằm trong khung ở mốc nổ, quái còn màu vật liệu với viền vàng và đoạn đuôi D đã tắt. Dừng đúng ba vòng; chưa gọi đạt mỹ thuật 8,5 hoặc nghiệm thu production.
