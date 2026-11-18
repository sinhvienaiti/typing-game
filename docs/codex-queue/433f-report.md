# Phiếu 433f — mưa kiếm Kim rộng và lâu hơn

Ngày 17/11/2026. Hoàn thành ba vòng của phiếu trong lab đang chạy tại `localhost:3148`, không commit, không chạy build hoặc bộ test của game, không dừng server. **Đạt các cổng nghiệm thu số: 102/103 kiếm (99,03%) đạt đồng thời ≥0,45 giây và ≥18% chiều cao khung; p95 8,00 ms.** Có hai điểm owner cần xem ở phần cuối; không tuyên bố đã qua chấm mù 8,5.

## Cách đã chọn

Đích là quãng rơi trên màn hình theo bổ sung của owner, không giữ độ cao 14 m bằng mọi giá. Lượt có sẵn ở đầu phiên đã thử 14 m / 24 m nhưng trận A lệch khỏi khung chơi. Bản cuối đặt mặt trận ở **10 m**, đường kính **22 m**; mũi kiếm xuất hiện ở **18 m**, xuyên qua mặt trận rồi tỏa ra đàn quái. Gia tốc dùng `p(u) = 0,2u + 0,8u²`. Kiếm nhỏ bay 0,9–1,0 giây; vệt dùng atlas sẵn có, dài tối đa 8,5–13,5 m theo quãng đã đi. Điểm ngắm của camera được chỉnh để vành A nằm trọn khung Alt+1. Không sinh hình hoặc âm thanh mới.

Giữ trận pháp A mặc định và `?formation=old`; giữ `mix` mặc định, kiếm nhỏ năng lượng, kiếm lớn là mô hình Tripo có aura; `?swordLook=aura|energy` vẫn còn. Hệ số sáng kiếm nhỏ giữ 0,26. Chỉ bổ sung sàn alpha 0,65 ở phần đầu lưỡi (`local y ≤ 0,03`) để mũi kiếm đọc được khi rơi; thân trong mờ và mép mềm giữ cách phối 433e.

## Mã đã làm

- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`: lịch sáu đợt và số lượng từng đợt; quỹ đạo từ trên trận; phân bố đĩa phân tầng, xoay giữa các đợt và tỏa ngang; thời gian tan riêng từng kiếm; cập nhật capacity, mốc shader kiếm lớn, sự kiện âm Kim, camera và phép chiếu mũi kiếm phục vụ đo.
- `games/.wt-ic-lab-all/src/lab/metal-sword-look.ts`: sàn alpha ở mũi kiếm, giữ kiểu kết hợp và hệ số sáng. Tiếp tục dùng phép đo độ chói tuyến tính của 433e.
- `games/.wt-ic-lab-all/src/lab/metal-ult-layered.ts`: chú thích kích thước trận khớp cấu hình 22 m; adapter đọc các mốc từ `METAL_RAIN`.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain-f-review.mjs`: chụp Alt+1/Alt+2, đo từng kiếm ở 60 Hz, p95 có chờ GPU, phân cấp sáng, xuất MP4 có âm Kim sẵn có.

Các file trên nằm đúng phạm vi `metal-ult-*` và `metal-sword-look.ts` của worktree lab; không sửa game chính, tài nguyên, hệ gõ hoặc bộ test.

## Dòng thời gian thật

| Đợt | Bắt đầu (s) | Kiếm nhỏ | Khoảng rải (s) |
| --- | ---: | ---: | ---: |
| 1 | 0,60 | 12 | 0,60 |
| 2 | 1,28 | 14 | 0,54 |
| 3 | 1,90 | 16 | 0,48 |
| 4 | 2,46 | 18 | 0,42 |
| 5 | 2,96 | 20 | 0,36 |
| 6 | 3,40 | 22 | 0,30 |

Khoảng giữa các đợt giảm 0,68 → 0,62 → 0,56 → 0,50 → 0,44 giây, đồng thời tăng số kiếm. Tổng **102 kiếm nhỏ + 1 kiếm lớn**, capacity **103**. Lần phóng nhỏ cuối ở **3,70 s**; kiếm lớn sinh **4,10 s**, đúng sau đó **0,40 s**; chạm đất **4,90 s**. Mũi nhỏ cuối chạm đất **4,688344 s**, nên mưa từ 0,60 s kéo dài **4,088344 s**. Kiếm nhỏ bắt đầu tan sau khi cắm 0,08 s và hết sau 0,32 s; tối đa **60 kiếm sống cùng lúc**. Kiếm lớn bắt đầu tan ở **5,35 s**, hết ở **6,70 s**; hệ thống trả toàn bộ 103 ô lúc **6,80 s**.

Âm Kim phát theo sự kiện của sáu đợt và các cụm va chạm, nối luân phiên những file đã có: charge, sword-draw, qi-slash, big-burst, glint. Có **1 gather / 7 grow / 44 crack / 1 break / 1 tail**; nhóm va chạm cách tối thiểu 50 ms. Log âm có 54 lượt, từ 0 đến 4,883333 s (đồng hồ ghi ở đầu bước mô phỏng); đuôi âm tiếp tục sau va chạm. Clip trộn bằng `mix-lab-sound.mjs` hiện có, giữ gain, pitch, pan, nhóm voice và reverb của lab; không thêm file nguồn âm.

## Các vòng

| Vòng | Trận cao / đường kính | Bề ngang kiếm cắm | Mưa / đợt | Kiếm nhỏ / tổng | Sống tối đa | Trắng | p95 |
| --- | --- | ---: | --- | --- | ---: | ---: | ---: |
| 1, tệp có sẵn khi nhận phiên | 14 / 24 m | 40,66% | 4,368 s / 6 | 102 / 103 | 58 | 0% | 9,30 ms |
| 2 | 10 / 22 m | 73,12% | 4,088 s / 6 | 102 / 103 | 60 | 0% | 9,10 ms |
| 3, cuối | 10 / 22 m | **71,10%** | **4,088 s / 6** | **102 / 103** | **60** | **0%** | **8,00 ms** |

Vòng 1 chưa có phép đo quãng rơi theo bổ sung của phiếu; không dựng lại số. Vòng 2 tính cả kiếm lớn: trung vị thấy 0,950 s, nhỏ nhất 0,800 s; trung vị quãng rơi xấp xỉ 46,85%, nhỏ nhất 25,29%; 103/103 đạt cả hai. Vòng 2 vẫn tràn mép dưới khi nội suy camera, nên vòng 3 chỉnh điểm ngắm; không sửa thêm hình sau vòng 3.

Đã mở tấm vòng 1, vòng 2, vòng 3, ảnh riêng 1280×720, tấm chuyển động 14 khung và ảnh giao nộp; đối chiếu nửa trái của `ult-storyboard-samples-431.jpg` cùng nhận xét owner. Trận A và mưa phủ đàn quái rộng hơn; kiếm lớn giữ trục nhấn cuối. Hình trong phân cảnh là nguồn nội bộ của repo, không gửi tham chiếu bên thứ ba tới công cụ tạo ảnh.

## Quãng rơi — đo toàn bộ 103 kiếm

Camera chơi Alt+1, 1280×720, DPR 1. Mỗi bước 1/60 s chiếu **mũi kiếm local y=0** bằng đúng camera và công thức quỹ đạo đang vẽ; chỉ cộng thời gian trước va chạm khi x/y trong khung, độ sâu trong clip và alpha ≥0,5. Kiếm năng lượng có alpha mũi ≥0,65; kiếm lớn là vật liệu thật, alpha 1. Quãng rơi là trị tuyệt đối chênh y đầu tiên thấy rõ và y lúc cắm, chia 720. Phép đo theo định nghĩa hình học/alpha của phiếu, không kiểm occlusion bằng depth buffer của cảnh. Sai số lấy mẫu thời gian tối đa một khung 16,67 ms.

| Tập kiếm | Trung vị thấy rõ | Nhỏ nhất | Trung vị quãng rơi | Nhỏ nhất | Đạt cả hai |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tất cả 103 | **0.767 s** | **0.417 s** | **39.69%** | **20.13%** | **102/103 = 99.03%** |
| 102 kiếm nhỏ | 0.767 s | 0.500 s | 39.71% | 20.13% | 102/102 |
| Kiếm lớn | 0,417 s | 0,417 s | 38,25% | 38,25% | 0/1: thiếu thời gian |

Cổng tổng thể của phiếu (trung vị ≥0,45 s, trung vị ≥18%, ít nhất 80% đạt cả hai) **đạt**. Không tuyên bố mọi kiếm đạt 0,45 s: kiếm lớn đi vào khung muộn, thiếu khoảng 0,033 s nếu áp ngưỡng ấy riêng cho nó. Giữ kết quả và báo owner tại giới hạn ba vòng.

## Hình, sáng và hiệu năng

- Chụp hai góc tại **1,05 / 2,35 / 3,90 / 4,916667 / 5,90 s**, nền `#353a40`. Mốc 4,916667 là khung đầy đủ đầu tiên sau va chạm 4,90 s; 5,90 là đúng một giây sau va chạm.
- Ở Alt+1 trong toàn thời gian mưa: vành trận nằm trong khung, lề trên nhỏ nhất **6,87%** (≥4%). Khi camera trở về, lề trên còn khoảng 5,18%; lúc này trận đã tan. Vùng kiếm cắm sống cùng lúc rộng tối đa **71,10%**; toàn bộ vị trí cắm dự kiến trong thời gian mưa rộng tối đa **74,62%**. Phép đo 71,10% dùng các kiếm đang thực sự cắm, không lấy vệt làm bề ngang.
- Độ chói đo trước bloom/tone mapping, render riêng nhóm nhỏ và kiếm lớn vào RGBA half-float nền đen như 433e. Tỷ số nhỏ nhất khi cả hai nhóm hiện trong các mẫu kiểm **3,922×** (≥1,5). Alt+1 ở 4,20 và 4,40 s kiếm lớn còn ở trên khung nên không dùng số 0 đó làm tỷ số; Alt+2 lúc ấy đã thấy kiếm lớn.
- Vùng trắng toàn khung: cả ba kênh sRGB ≥242/255. **0%** ở các ảnh pha và tối đa trên **165 khung clip**, dưới 6%.
- Chrome headless, High mặc định, **ANGLE Metal Renderer: Apple M4**, cảnh 100 quái (**87 TargetField + 13 walker**), DPR 1.
- Đo như `metal-ult-rain-review.mjs`: từng khung CPU rồi `readPixels` một pixel để chờ GPU. Chọn các khung còn kiếm rơi và số sống ≥80% đỉnh; **42 mẫu** lúc mưa dày. **p95 tổng 8,00 ms**, p95 CPU **1,50 ms**. Trên toàn khoảng chiêu đang chạy, p95 tổng **11,50 ms**. Không đồng nhất số này với khoảng cách rAF.
- Tối đa **79 draw call**, **2.623.417 tam giác**; kết thúc không còn active, **103/103 ô đã trả**.
- `node node_modules/typescript/bin/tsc --noEmit` trong worktree: **0 lỗi**. Không chạy build hoặc bộ test.
- Không có exception hoặc lỗi tải tài nguyên mưa kiếm. Còn cảnh báo sẵn có ngoài phạm vi: nhiều KTX2Loader và `drawImage` ở atlas `metal-crescent-sym` / `metal-slash-arc`.

## Giao nộp và dọn dẹp

- [metal-rain-f.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-f.jpg): đối chiếu với nửa trái phân cảnh; năm mốc, hai góc.
- [metal-rain-f.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-rain-f.mp4): **H.264 + AAC, 1280×720, 24 fps, 165 khung, 6,875 giây**; từ kích chiêu tới khi kiếm tan hết, có âm Kim. Đã kiểm stream và thời lượng bằng ffprobe.
- [round-3-sheet.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433f/round-3-sheet.jpg), [motion-contact.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433f/motion-contact.jpg). Giữ các tấm vòng trước và toàn bộ ảnh/clip 433e cũ.
- Đã thêm một dòng `metal-rain-f` trong `owner-review/2026-11-17/tu-tien/ABOUT.md` và ghi ABOUT cho các thư mục lượt mới.
- Đã xem trước rồi prune **185/185 khung thô do phiên này tạo, 245,806 MB**; hai thư mục mới không còn PNG thô. Giữ khung thô của lượt cũ không do phiên này tạo, theo quy tắc không xóa file của agent khác. Đã xóa file âm/video trung gian của clip.
- Đã đóng Chrome headless do lượt chạy tạo và xóa profile tạm tự động bằng driver. Cũng đã đóng tiến trình Chrome headless 433f mồ côi từ lượt trước (PID 50859, đã xác minh trang lab 3148), xóa profile `st-cdp-e8ocsB`; không đóng Chrome chính của owner và không dừng server.
- Không chạy `review-index.mjs` vì phiếu chỉ cho ghi báo cáo và ABOUT ngoài các đường dẫn mã/media; công cụ đó sẽ ghi thêm file chỉ mục ngoài phạm vi.

**Owner cần xem:** cảm giác đường rơi và nhịp sáu đợt trong clip; kiếm lớn chỉ có 0,417 s thấy rõ ở Alt+1; góc Alt+2 cắt phần trên vành A do góc nhìn gần, dù Alt+1 đạt cổng khung. Chưa có chấm mù độc lập 8,5 hoặc owner chốt hình/âm. Không nhận đây là nghiệm thu thẩm mỹ cuối.

Lệnh tái kiểm (chỉ server có sẵn; `FINAL=1` xuất lại media):

```sh
ART_MAGICK=/opt/homebrew/bin/magick ROUND=3 FINAL=1 .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/metal-ult-rain-f-review.mjs --width=1280 --height=720 --dpr=1
```

## Số đo từng kiếm của vòng 3

ID bắt đầu từ 0; ID 102 là kiếm lớn. Quãng tính theo % chiều cao khung 720 px.

| ID | Thấy rõ (s) | Quãng (%) | Đạt cả hai |
| ---: | ---: | ---: | --- |
| 0 | 0.583 | 38.194 | Đạt |
| 1 | 0.600 | 45.176 | Đạt |
| 2 | 0.567 | 33.701 | Đạt |
| 3 | 0.667 | 47.904 | Đạt |
| 4 | 0.867 | 35.883 | Đạt |
| 5 | 0.767 | 32.740 | Đạt |
| 6 | 0.750 | 52.670 | Đạt |
| 7 | 0.867 | 25.520 | Đạt |
| 8 | 0.950 | 42.350 | Đạt |
| 9 | 0.900 | 41.632 | Đạt |
| 10 | 0.967 | 22.811 | Đạt |
| 11 | 0.933 | 58.622 | Đạt |
| 12 | 0.533 | 42.617 | Đạt |
| 13 | 0.600 | 37.334 | Đạt |
| 14 | 0.617 | 35.216 | Đạt |
| 15 | 0.800 | 54.017 | Đạt |
| 16 | 0.617 | 36.506 | Đạt |
| 17 | 0.867 | 42.204 | Đạt |
| 18 | 0.883 | 43.947 | Đạt |
| 19 | 0.700 | 26.159 | Đạt |
| 20 | 0.867 | 57.606 | Đạt |
| 21 | 0.950 | 26.685 | Đạt |
| 22 | 0.967 | 28.955 | Đạt |
| 23 | 0.833 | 54.695 | Đạt |
| 24 | 0.867 | 21.817 | Đạt |
| 25 | 0.967 | 48.451 | Đạt |
| 26 | 0.667 | 47.957 | Đạt |
| 27 | 0.567 | 33.297 | Đạt |
| 28 | 0.600 | 40.765 | Đạt |
| 29 | 0.667 | 42.601 | Đạt |
| 30 | 0.533 | 32.496 | Đạt |
| 31 | 0.800 | 54.259 | Đạt |
| 32 | 0.933 | 33.450 | Đạt |
| 33 | 0.950 | 34.001 | Đạt |
| 34 | 0.733 | 51.132 | Đạt |
| 35 | 0.750 | 24.782 | Đạt |
| 36 | 0.950 | 52.837 | Đạt |
| 37 | 0.950 | 36.913 | Đạt |
| 38 | 0.900 | 23.870 | Đạt |
| 39 | 0.933 | 58.238 | Đạt |
| 40 | 0.917 | 20.125 | Đạt |
| 41 | 0.983 | 31.896 | Đạt |
| 42 | 0.683 | 49.983 | Đạt |
| 43 | 0.500 | 39.731 | Đạt |
| 44 | 0.733 | 50.553 | Đạt |
| 45 | 0.583 | 40.375 | Đạt |
| 46 | 0.650 | 37.812 | Đạt |
| 47 | 0.750 | 51.781 | Đạt |
| 48 | 0.667 | 27.429 | Đạt |
| 49 | 0.767 | 44.775 | Đạt |
| 50 | 0.933 | 41.222 | Đạt |
| 51 | 0.600 | 36.814 | Đạt |
| 52 | 0.583 | 42.881 | Đạt |
| 53 | 0.917 | 31.549 | Đạt |
| 54 | 0.950 | 33.561 | Đạt |
| 55 | 0.867 | 56.781 | Đạt |
| 56 | 0.750 | 22.494 | Đạt |
| 57 | 0.917 | 53.449 | Đạt |
| 58 | 0.983 | 28.261 | Đạt |
| 59 | 1.000 | 20.721 | Đạt |
| 60 | 0.550 | 36.927 | Đạt |
| 61 | 0.550 | 35.330 | Đạt |
| 62 | 0.833 | 55.125 | Đạt |
| 63 | 0.583 | 30.955 | Đạt |
| 64 | 0.667 | 42.434 | Đạt |
| 65 | 0.767 | 41.081 | Đạt |
| 66 | 0.567 | 38.903 | Đạt |
| 67 | 0.567 | 43.726 | Đạt |
| 68 | 0.617 | 40.560 | Đạt |
| 69 | 0.750 | 45.274 | Đạt |
| 70 | 0.733 | 49.284 | Đạt |
| 71 | 0.533 | 33.882 | Đạt |
| 72 | 0.867 | 49.928 | Đạt |
| 73 | 0.933 | 32.948 | Đạt |
| 74 | 0.750 | 37.196 | Đạt |
| 75 | 0.900 | 56.777 | Đạt |
| 76 | 0.933 | 22.062 | Đạt |
| 77 | 0.917 | 38.169 | Đạt |
| 78 | 0.950 | 44.485 | Đạt |
| 79 | 0.933 | 21.509 | Đạt |
| 80 | 0.717 | 50.726 | Đạt |
| 81 | 0.600 | 40.400 | Đạt |
| 82 | 0.717 | 50.447 | Đạt |
| 83 | 0.567 | 31.336 | Đạt |
| 84 | 0.583 | 41.535 | Đạt |
| 85 | 0.617 | 43.275 | Đạt |
| 86 | 0.733 | 36.145 | Đạt |
| 87 | 0.783 | 54.286 | Đạt |
| 88 | 0.533 | 39.695 | Đạt |
| 89 | 0.767 | 47.247 | Đạt |
| 90 | 0.933 | 37.557 | Đạt |
| 91 | 0.667 | 37.295 | Đạt |
| 92 | 0.600 | 45.658 | Đạt |
| 93 | 0.933 | 26.784 | Đạt |
| 94 | 0.983 | 38.542 | Đạt |
| 95 | 0.833 | 52.836 | Đạt |
| 96 | 0.767 | 23.375 | Đạt |
| 97 | 0.817 | 55.219 | Đạt |
| 98 | 0.950 | 25.250 | Đạt |
| 99 | 0.967 | 24.556 | Đạt |
| 100 | 0.833 | 57.279 | Đạt |
| 101 | 1.000 | 20.732 | Đạt |
| 102 | 0.417 | 38.250 | Thiếu thời gian |
