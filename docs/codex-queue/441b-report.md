# Phiếu 441b — Quang, cú nổ D lớn và lực va chạm

17/11/2026. Đã sửa, tự chụp và mở xem **4 vòng** ở lab 3148. Cụm nổ đạt ngưỡng kích thước màn hình; kiểm kiểu **0 lỗi**, p95 **6,20 ms**. Giới hạn cần owner xem: phần trên D bị cắt ở camera chơi; chưa có nghiệm thu mỹ thuật 8,5 ở host chơi.

## Giao nộp

- [Ảnh phân cảnh và hai camera](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-f.jpg)
- [Video camera chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-f.mp4)
- [Video sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-f-behind.mp4)

Hai video đều **4 giây, 120 khung, 30 fps, 1280×720, H.264 + AAC**, lần lượt **2.312.598** và **2.540.505 byte**. Đã giải mã toàn bộ bằng ffmpeg không lỗi và mở các sheet giải mã: [chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-f-4/441b-decoded-top-sheet.jpg), [sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-f-4/441b-decoded-behind-sheet.jpg). Giữ nguyên mọi bản cũ a–e.

## Thay đổi

- D từ 7×7 m thành **36,5 × 26,849315 m**: diện tích mặt phẳng thế giới **20 lần**. Mở rộng ngang để cú nổ trùm đàn quái; hình nguồn atlas giữ nguyên, kích thước hiển thị dùng tỷ lệ 1,36. Billboard vẫn đứng, chỉ quay Y theo camera; neo nguồn `[0,5; 0,62078125]`, chân ở **y=0,025 m**, cố định từ lần trúng đầu. Độ trôi neo trong mỗi lượt chụp: **0 m**.
- Dùng **`light-prism-burst-hi`**, cắt từ chính video Firefly D «Bản 1»: 32 ô **512²**, atlas **4096×2048**, UASTC/Zstd **2.829.480 byte**, 13 mip; alpha cuối 0. Giữ bộ 256² cũ. Có hai file prompt cạnh bộ mới; không sinh ảnh, video hay âm mới. Thử ô 768² vượt trần texel của encoder; chuyển sang 512² đúng giới hạn, không đổi công cụ/gỡ cổng chặn.
- **120** vệt lăng kính thay 48 (**2,5 lần**), tầm đạn đạo **4–15 m** thay 1,7–6,4 m; giữ 14 tia tỏa. Bộ đệm 192 chỗ, không cắt mất hạt.
- Lóe phụ **14 m**, alpha 0,55, đúng **2/60 s** tại 1,95 s. Ánh sáng điểm ấm có phạm vi **28 m**, cao 5,8 m, cường độ đỉnh 300, tan 0,42 s; không thêm vòng/đĩa. Gain D 1,35.
- Vùng phản ứng tăng bán kính **4,8→13,5 m**; đẩy gốc **0,95→1,65 m**, xung hit 1,1, shocked vàng 0,4 s. **71 quái** quanh điểm trúng được phản ứng. Ở 2,05 s độ dịch chuyển ròng **0,130–2,018 m**, đã gồm chuyển động của từng quái.
- `UltCameraPunch` chỉ import, không sửa: tỷ lệ khoảng cách **0,96→0,88**, vào 0,025 s, giữ tới 0,07 s, trả 0,25 s; ở 2,05 s đo được 0,881718, sai số trả camera 0 m. Giữ rung host hiện có.
- Không đổi tầm quạt **20 m**, thuật toán chọn điểm trúng hoặc shader tia. Tia hội tụ vẫn theo trục giữa, đầu chìm trong lõi D. Chiều dài thế giới ở 1,9 s **15,4973 m**, bản 441 ghi 15,5023 m; chênh 5 mm do vị trí quái giữa các lượt, không có thao tác rút ngắn tia. Lệch trục cuối **0°**.
- Âm `tt-sfx-ult-light/take1.wav` giữ nguyên mixer và take. Bản ghi: tụ 0, phóng 0,600, nổ **1,950 s**, khớp khung chạm; clip dùng âm từ bản ghi mixer thật.

## Bốn vòng tự xem

Đã mở sheet từng vòng và ảnh riêng hai góc, đối chiếu ô dưới trái phân cảnh cùng nhận xét owner. Điểm tự chấm chỉ mô tả tiến bộ, không thay hai giám khảo mù.

| Vòng | Tự chấm | Quan sát và quyết định |
| --- | --- | --- |
| 1 | 7,0 | D 30 m lớn rõ, rọi quá mạnh; D riêng rộng 38,28%. Giảm đèn 520→300, tăng lóe ngắn và kiểm riêng cụm nổ. |
| 2 | 7,1 | Cụm liền mạch rộng 40,16%, thiếu ngưỡng; nổ sáng hơn, sau lưng vẫn nhìn thấy cảnh. |
| 3 | 7,2 | D 35×28 m, diện tích 20 lần; cụm liền mạch rộng 44,45%, thiếu 7 px. Mở ngang thêm, giảm cao để giữ diện tích 20 lần. |
| 4 | 7,3 | Cụm liền mạch 45,47%×66,53%; D riêng rộng 46,48%. Nổ lớn, quái/đất phản ứng rõ; còn cắt mép trên và lóe quái khá mạnh. |

Ảnh đối chiếu: [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-1/441b-comparison.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-2/441b-comparison.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-3/441b-comparison.jpg), [vòng 4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-comparison.jpg). [Nhịp chuyển pha cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-transition-sheet.jpg).

## Cách đo và kết quả

High, **1280×720 DPR1**, nền **`?ground=%23353a40`**, Chrome headless/Metal. Độ sáng Rec.709 trên RGB chuẩn hóa, ngưỡng **ΔY≥0,15**. Mọi cặp bật/tắt giữ nguyên camera, thời gian và trạng thái quái. Ngắt riêng kết nối HMR của trình duyệt chụp để thay đổi ở làn khác không tải lại trang giữa cặp; không đụng server.

Tìm khung nổ bằng **luma trung bình cao nhất trong tròn 120 px quanh điểm trúng**, quét 31 khung 60 Hz từ 1,95 đến 2,45 s mỗi góc. Kết quả: **chơi 1,9666667 s**, sau lưng **1,9500000 s**. Phủ sáng tròn tương ứng **92,35%** và **99,33%**.

Đo kích thước vụ nổ bằng **D + vệt lăng kính + đèn ấm**, tắt tia hội tụ, kính và những mesh FX khác trước khi lấy cặp bật/tắt. Lóe phụ không được tính vào cặp tách cụm này. In cả bbox tất cả điểm sáng và bbox **thành phần liên thông 8 hướng lớn nhất**, để hạt lẻ không quyết định kết luận.

| Camera | Bbox tất cả điểm ΔY≥0,15 | Cụm liên thông lớn nhất | Pixel sáng liên thông / toàn khung |
| --- | --- | --- | --- |
| Chơi | 1201×717 px; 93,83%×99,58% | **582×479 px; 45,47%×66,53%** | 16,68% |
| Sau lưng | 1270×649 px; 99,22%×90,14% | **615×618 px; 48,05%×85,83%** | 30,38% |

**Phân biệt D riêng:** khi chỉ tắt mesh D, giữ các lớp khác, D đóng góp bbox **595×179 px (46,48%×24,86%)** ở camera chơi và **694×370 px (54,22%×51,39%)** sau lưng. Ngưỡng chiều cao 35% đạt cho **tổ hợp nổ có hắt sáng**, không đạt nếu chỉ tính bitmap D; phần phía trên bitmap đã ra ngoài khung do điểm trúng ở gần mép trên. Không dùng tia hội tụ để bù chiều cao. Owner cần xem và chốt giới hạn này.

Mốc trước sửa ở cùng 1,9667 s: D riêng camera chơi **85×34 px**. Bbox D mới / cũ **36,85 lần** theo ngưỡng ảnh; không gọi đây là tỷ lệ màn hình chính xác 20 lần. Tỷ lệ đúng 20 lần ở trên là diện tích mặt phẳng thế giới; ngưỡng sáng, độ cắt khung và camera punch làm tỷ lệ bbox ảnh khác đi.

Trắng toàn khung cao nhất **0,040907%≤6%**, quét hai góc và các pha cố định. Sau lưng, độ phủ ΔY≥0,15 của toàn chiêu cao nhất trong 31 khung quét là **36,10%**; không có khung che kín toàn cảnh trong đoạn nổ nguy hiểm 0,5 s. Sheet giải mã kiểm thêm 2,6 và 3,3 s: phần ngoài vụ nổ vẫn đọc được, D tắt trước 3,30 s.

Giữ các cổng cũ: nêm 0,9 s **61,12%≥25%**; ROI sau lưng ≥8%; quầng giữa từng tia ≥8 px; hội tụ 1,9 s **quầng/lõi 95/6 px≥24/4**, đúng 1 tia HDR. Mặt cắt tia giữa tách riêng 20/50/85% **12/17/2 px**, tỷ lệ **0,11765≤0,6**. Kính camera chơi 31×21 px ở 0,9 s, mọi pha ≥18 px; CV tia **0,118684**. Các cổng đều qua trong scenario cuối.

[JSON đầy đủ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-measure.json); [Bản ghi âm](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-sound-takes.json). Cặp ảnh giữ để đo lại:

- chơi, D riêng: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-D-top-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-D-top-off.png).
- chơi, cụm nổ: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-explosion-top-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-explosion-top-off.png).
- chơi, khung nổ toàn chiêu: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-scan-top-1.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-scan-top-1-off.png).
- sau lưng, D riêng: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-D-behind-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-D-behind-off.png).
- sau lưng, cụm nổ: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-explosion-behind-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-explosion-behind-off.png).
- sau lưng, khung nổ toàn chiêu: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-scan-behind-0.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-f-4/441b-scan-behind-0-off.png).
- Trước sửa, D riêng camera chơi: [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/baseline-f/441b-before-top.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/baseline-f/441b-before-top-off.png).

## Kiểm kiểu, GPU và phạm vi

`./node_modules/.bin/tsc --noEmit`: **0 lỗi** sau thay đổi cuối; `node --check` các script cắt/chụp/probe: qua. Không chạy build hay bộ test game.

`stress.html`: đủ **87 TargetField +13 walker =100** từng lượt; 240 mẫu/lượt, bỏ lượt làm nóng, gộp 720 mẫu. `total=CPU+chờ GPU qua readPixels`, khóa `.local/bin/heavy.sh --perf`, renderer **ANGLE Metal / Apple M4**, không renderer phần mềm.

| Lượt | p95 total | p95 CPU |
| --- | --- | --- |
| Làm nóng | 8,90 ms | 1,60 ms |
| 1 | 5,90 ms | 1,40 ms |
| 2 | 6,00 ms | 1,40 ms |
| 3 | 6,40 ms | 1,60 ms |

**p95 gộp 6,20 ms≤16,7; CPU 1,50 ms.** Không exception JS/shader; tài nguyên Quang ready. Có cảnh báo KTX2Loader và hai atlas Kim không tải được từ làn khác; giữ nguyên.

Mã sửa: `src/lab/light-ult-{burst,impact,fan,cut,glow-probe}`; thêm `light-ult-review-f.mjs`, đều trong `games/.wt-ic-lab-all`. Tài nguyên chỉ thêm bộ `light-prism-burst-hi` vào thư mục cho phép; cập nhật mục thư viện, ABOUT owner và báo cáo này. Không sửa `skills-main.ts`, `ult-camera-punch.ts`, audio-lab hoặc mã production. Một làn ghi; một trợ lý chỉ đọc rà giới hạn API và cách đo, không ghi file hay mở browser. Quota ban đầu còn 65%; phiếu đã có phản biện PASS, không gọi tư vấn ngoài.

Không khởi động/dừng lại server 3148; Chrome do phiếu tạo đã thoát. Không commit, push, reset, clean, stash hay đưa media vào Git. Không chạy dựng index review vì các file index nằm ngoài phạm vi ghi của phiếu.

Lệnh tái lập (từ repo cha): `ROUND=4 FINAL=1 CHROME_FLAGS='--use-angle=metal' .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review-f.mjs --width=1280 --height=720 --dpr=1`. Cắt atlas: `ART_MAGICK=/opt/homebrew/bin/magick node games/.wt-ic-lab-all/src/lab/light-ult-cut.mjs`.

## Owner cần xem và phần bỏ qua

Xem **1,95–2,3 s** trong hai clip: mức lớn của D, phần trên bị cắt ở góc chơi, đầu tia chìm vào lõi, rọi đất và phản ứng quái. Cụm nổ đáp ứng ngưỡng 45%×35%, nhưng bitmap D riêng chỉ cao 24,86% ở camera chơi. Dừng đúng 4 vòng; chưa gọi đạt mỹ thuật 8,5 hoặc nghiệm thu production. Không sinh thêm media vì đã có nguồn owner chọn; không đổi camera mặc định/model/nền hoặc thuật toán tia để né giới hạn hình.

## Dọn khung thô

Đã dọn riêng các thư mục `baseline-f`, `round-f-1..4`, `frames-f-round-4`, `frames-f-behind-round-4`, `video-check-f-4` do phiếu tạo bằng `tools/capture-prune/prune.mjs`, dry-run trước `--apply --min-age-min 0`. Giữ các sheet/cặp ảnh được báo cáo liên kết và JSON; không đụng file cũ hoặc làn khác.

Đã xóa **1.120 ảnh thô/trung gian, 1006,972 MB**, giữ **24** ảnh/sheet có ích; từ chối **0** mục. Nhật ký và kế hoạch: `captures/tu-tien/light-ult-439/441b-prune-{dry,result}.{json,log}`.
