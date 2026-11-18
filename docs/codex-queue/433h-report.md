# Phiếu 433h — Kim, thay K5 bằng vệt kiếm D

Ngày 18/11/2026. Xác nhận 433g đã xong trước khi sửa. **Đạt các cổng số sau ba vòng chụp và tự mở ảnh: kiểm kiểu 0 lỗi, p95 8,90 ms, chiều dài vệt 0,80–1,40 lần thân kiếm, tan 0,20 s.** Chưa có chấm mù 8,5 hoặc owner duyệt thẩm mỹ.

## Nguồn và cách gắn

- Dùng duy nhất `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png`, đối chiếu tờ mẫu 444 đã chọn D và ảnh 433g.
- Texture mới: `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/sword-trail-d.png`, kèm `.json` và `.prompt.txt`. Cắt lề ngang x=448, rộng=128, giữ nguyên chiều cao 1024; không thu nhỏ, làm mờ hoặc vẽ thêm. `.json` ghi điểm neo (63; 850), tương đương (511; 850) ảnh gốc, tại 83,01% chiều cao, gần mốc 85% của phiếu.
- Alpha thẳng lấy từ độ sáng cực đại sRGB; RGB được bù trong ánh sáng tuyến tính để cộng sáng tái tạo màu nguồn. Bỏ nhiễu nền ≤2/255. Đối chiếu tái tạo trên nền đen: sai số kênh tối đa 2/255, trung bình 0,095/255.
- Mỗi kiếm nhỏ và kiếm lớn dùng đúng một quad, chung hình học và texture D. Vật liệu `MeshBasicMaterial` chuẩn, `AdditiveBlending`, `SRGBColorSpace`, không shader tùy biến; màu nhân đều (1,8; 1,8; 1,8). Giữ nguyên hình nguồn, không crop/blur/mask ở runtime.
- Gốc hình học nằm ngay đầu sáng D. Gắn vào điểm local y=1 của kiếm, tức đầu trên của chuôi, dùng đúng biến đổi kiếm từng khung. Trục dọc ngược chiều rơi; quad quay quanh trục ấy để hướng về camera hiện tại.
- Tỷ lệ dài tăng theo tốc độ rơi chuẩn hóa, chặn trong khoảng đọc được 0,8–1,4. Bù phép chiếu phối cảnh bằng **một hệ số chung cho x/y/z**, không kéo riêng chiều dài hoặc ngang. Kiếm lớn cùng công thức và art, tăng theo kích thước thân.
- Khi cắm, alpha giảm bằng smoothstep từ 0,9 xuống 0 trong 0,20 s. Đo kiếm lớn ở 4,90 / 4,95 / 5,00 / 5,05 / 5,10 s: 0,900 / 0,759375 / 0,450 / 0,140625 / 0; giống nhau ở cả hai góc.
- K5 cũ còn nguyên đoạn crop-blur và lời gọi được lưu trong `if (false)`; mesh cũ `visible=false`, số instance đang vẽ đo tại runtime bằng 0. Không xóa code cũ. K2/K3/K6/K7 và nhịp mưa của 433g giữ nguyên.

## Số đo ở camera thật

Chrome headless, localhost:3148 có sẵn, High mặc định, 1280×720, DPR 1; ANGLE Metal Renderer Apple M4, 100 quái. Alt+1 và Alt+2, nền `?ground=%23353a40`. Mỗi vòng mở ảnh và so với D/433g; vòng 1 chưa đạt khoảng chiều dài, vòng 2 sửa bù phối cảnh, vòng 3 tăng sáng đều cho D và xuất media. Lần khởi động trước vòng 1 gặp đệ quy camera; đã sửa bằng đọc matrixWorld trực tiếp, chưa chụp ảnh ở lần lỗi ấy.

| Vòng | p95 mưa dày (ms) | Trắng tối đa (%) | Dài nhỏ, min–max / thân | Kết luận |
| --- | ---: | ---: | ---: | --- |
| 1 | 11.90 | 0.00010851 | 0.184–1.794 | Cần sửa chiều dài |
| 2 | 9.00 | 0.00010851 | 0.800–1.400 | Đạt cổng số |
| 3 | 8.90 | 0.00010851 | 0.800–1.400 | Đạt cổng số |

Bề ngang dưới đây là bao hình D ở ngưỡng nguồn khoảng 1%, gồm quầng/hạt mờ, chiếu theo hướng vuông góc trục thân; không phải riêng lõi sáng. Thân kiếm đo từ đỉnh thật của model trong local y=0…1, bỏ phần đế sẵn có ở y<0. Chỉ lấy đầu chuôi trong khung, alpha ≥0,5.

| Góc / kiếm | Mẫu | Ngang vệt / thân, trung vị (min–max) | Dài vệt / thân, trung vị (min–max) |
| --- | ---: | ---: | ---: |
| Alt+1 / nhỏ | 117 | 0.717 (0.400–2.288) | 1.047 (0.800–1.400) |
| Alt+1 / lớn | 3 | 0.810 (0.779–0.819) | 1.400 (1.384–1.400) |
| Alt+2 / nhỏ | 176 | 0.648 (0.433–1.819) | 0.820 (0.800–1.400) |
| Alt+2 / lớn | 4 | 1.497 (0.928–1.513) | 1.400 (1.011–1.400) |

293 mẫu kiếm nhỏ và 7 mẫu kiếm lớn. Sai số neo lớn nhất **0,0000008443 m**, do ma trận instance Float32; chênh lệch scale x/y/z bằng **0**. Mọi vật liệu D đều dùng shader chuẩn. Sai số tỷ lệ dài do số thực dưới 0,000002.
Vùng trắng: cả ba kênh sRGB ≥242/255; tối đa **0,00010851%**, tức một pixel/921.600 pixel, trên cả ảnh pha và 165 khung clip. p95 mưa dày **8,90 ms**, CPU p95 **4,10 ms**, 42 mẫu có kiếm rơi và số kiếm sống ≥80% đỉnh. Đo CPU rồi readPixels một pixel chờ GPU theo driver 433f/433g, không phải khoảng cách rAF. p95 toàn chiêu **8,80 ms**; đỉnh 428 draw call, 1.807.817 tam giác. Không suy ra tăng tốc từ chênh lệch giữa các lượt lịch sử.
Giữ 102 kiếm nhỏ + 1 kiếm lớn, tối đa 60 kiếm sống, sáu đợt 12/14/16/18/20/22, mưa 4,088344 s, hết chiêu 6,80 s, trả đủ 103 ô. Quãng rơi trung vị 39,69% khung; thấy rõ trung vị 0,767 s; 99,03% kiếm đạt cả hai ngưỡng 433f. Độ sáng kiếm lớn/nhỏ đo nhóm thân và khí/hào quang của 433g là 2,930×; phép đo này không cộng nhóm vệt D.
`node node_modules/typescript/bin/tsc --noEmit`: **0 lỗi**. Không chạy build hoặc bộ test của game. Runtime không có exception cuối; còn cảnh báo sẵn có về nhiều KTX2Loader và drawImage của metal-crescent-sym ngoài phạm vi. Video giải mã hết bằng ffmpeg không báo lỗi.

## Tệp giao nộp

- [metal-rain-h.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-h.jpg): 10 ô, Alt+1 và Alt+2, các mốc 1,05 / 2,35 / 3,90 / 4,916667 / 5,90 s.
- [metal-rain-h.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-h.mp4): H.264 + AAC, 1280×720, 24 fps, 165 khung, 6,875 s; 5.637.832 byte. Âm Kim cũ: 54 sự kiện, từ 0 đến 4,883333 s; không tạo âm mới.
- [Tấm chi tiết](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/round-3-trail-detail.jpg): 1,35 / 3,75 / 4,89 s, hai góc; [tấm chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/motion-contact.jpg), [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/round-1-trail-d-sheet.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/round-2-trail-d-sheet.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/round-3-trail-d-sheet.jpg), [nguồn D trên nền xám](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433h/source-preview.jpg).
- Đã sửa `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`; thêm `metal-ult-trail-d.ts`, `metal-ult-trail-d-normalize.mjs`, `metal-ult-rain-h-review.mjs` cùng thư mục. Không sửa `metal-sword-look.ts`.
- Đã thêm dòng vào ABOUT của owner và tạo ABOUT cho các thư mục capture của phiên. `art-src` của worktree là symlink có sẵn sang art-src game chính; chỉ thêm đúng ba tệp D qua đường dẫn worktree được phép. Không sửa ảnh gốc.
- Giữ nguyên mọi ảnh/video cũ. Đã mở ảnh giao nộp, tấm chi tiết, tấm chuyển động và so với D cùng 433g.

## Dọn dẹp và phần chưa làm

- Đã đóng Chrome của từng lần chạy và xóa profile tạm bằng driver; sau lượt cuối không còn tiến trình Chrome dùng st-cdp. Không tắt Chrome của người khác. Server 3148 PID 243 vẫn chạy.
- Đã xem trước rồi prune toàn bộ 201 khung thô (263.129.725 byte) do phiên này tạo; giữ các tấm ghép. Video/âm trung gian đã xóa. Số byte xóa ghi trong nhật ký `.pruned-*.txt` ở từng thư mục lượt.
- Không chạy review-index vì công cụ sẽ ghi chỉ mục ngoài phạm vi tệp được phiếu cho phép; người điều phối cập nhật sau. Không commit, push, reset, clean hoặc stash.
- Không sinh art/âm mới: dùng D đã được owner chọn và âm Kim của 433g. Không sửa model/đế Tripo hoặc các lớp khác. Không mở vòng thứ tư.
- Owner cần xem độ đọc của lõi/hạt D ở camera chơi; phần đế Tripo và trận sáng ở góc sau lưng đã có từ 433g vẫn còn. Chưa có hai chấm mù độc lập hoặc owner chốt thẩm mỹ, nên không tuyên bố đạt 8,5.

Chạy lại trên server có sẵn (FINAL=1 ghi lại media h; không dùng để mở vòng sửa thứ tư):

```sh
ROUND=3 FINAL=1 ART_MAGICK=/opt/homebrew/bin/magick .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/metal-ult-rain-h-review.mjs --width=1280 --height=720 --dpr=1
```
