# Phiếu 439c — Quang hội tụ giữa quạt

17/11/2026. **Đạt các cổng định lượng của phiếu, kiểm kiểu 0 lỗi; đã tự mở ảnh qua 4 vòng. Chưa có nghiệm thu mỹ thuật 8,5 của hai giám khảo mù.** Tự chấm cuối 7,0/10 chỉ để ghi nhận vòng lặp, không thay đánh giá owner.

## Giao nộp và phạm vi

- [light-ult-codex-c.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-c.jpg) — phân cảnh cạnh camera chơi và sau lưng.
- [light-ult-codex-c.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-c.mp4) — 4 giây, 120 khung, 30 fps, 1280×720, H.264 + AAC; có âm Quang sẵn có.
- Đã thêm dòng `light-ult-codex-c` vào `owner-review/2026-11-17/tu-tien/ABOUT.md`; giữ nguyên các bản `light-ult-codex` và `light-ult-codex-b`.

Trong `games/.wt-ic-lab-all/src/lab/`, chỉ sửa `light-ult-fan.ts`, `light-ult-fan-space.ts`, `light-ult-glow-probe.mjs`; thêm `light-ult-twinkles.ts`, `light-ult-review-c.mjs`. Không sửa `skills-main.ts` hoặc `showcase.ts`. Tái dùng hook `lightUlt()` và `hideLight/showLight/hideLens/showLens` có sẵn.

Một lane; quota còn 75% theo bản ghi mới nhất khi bắt đầu. Giữ server 3148, Chrome luôn headless và được runner đóng sau mỗi lượt; không gọi mạng ngoài localhost. Không commit/push/reset/clean/stash, không đổi nhánh, không chạy build hoặc bộ test game. Không sửa production, tài liệu Tu Tiên, script/test game, audio-lab hoặc tài nguyên nguồn.

## Đã sửa

**Trục và nhịp hội tụ.** Bỏ cách chọn quái ở góc 26° bên phải. Trục lấy từ đỉnh kính qua trung điểm hai đầu tia biên thật. Hai tia biên có chiều dài bằng nhau và góc đối xứng để trục ổn định; các tia trong có độ dài/góc so le. Thu toàn bộ tia từ hai phía vào trục trong **1,45–1,80 s (0,35 s)**; chỉ sau đó xuất hiện một tia HDR. Chọn lại quái sống gần trục nhất tại 1,8 s, trong tầm 20 m và lệch không quá 5°; điểm tiếp xúc là hình chiếu vị trí quái lên trục, không bẻ tia về phía quái. Không có quái phù hợp thì điểm cuối ở 20 m trên trục. Số đo final: **tia lệch 0.000000°**, quái số 46 lệch **1.9786°**.

**Quạt 11 tia.** Seed **439.31**, độ dài ngang bằng 65–100% tầm theo công thức seed, mẫu đang dùng thực tế **66,30–100%**, CV **0.118684125 ≥0,1**. Góc lệch lưới đều tối đa 2,577°; ba tia chính số **3, 6, 10** có đỉnh sáng 0,94 / 1,00 / 0,98. Giữ nguyên **28 sprite hạt vàng trôi trên mỗi tia**, lõi ấm, quầng hổ phách và nhiễu chảy của 439b. Mỗi tia vẫn là dải thế giới, không vẽ cố định lên màn hình.

**Dư âm.** Lớp bụi rộng của pha trước tan hết ở 2,3 s. Riêng dư âm dùng **60 đốm**: 42 đốm theo các cụm trên ba tia chính, 18 đốm thưa trong nêm; có các khoảng trống. Mỗi đốm lấy một ngôi sao cô lập từ atlas Firefly **`art-src/lab/vfx/light/light-sparkle.atlas.png`, frame 8, tâm (43,56), vùng 50×50 px**, không vẽ sao bằng shader và không sinh art mới. Shader chỉ lấy mẫu art, đặt billboard, nhuộm màu và nhấp nháy; RGB phụ chặn ≤0,9. Chuyển vào nhẹ từ 2,25 s, dư âm tan trong **2,3–3,6 s (1,3 s)**. Giữ nguyên `gold-dust-motes-loop-w2` trong pha quét/hội tụ, không giữ lớp phủ đều sang dư âm.

**Thấu kính.** Bán kính 0,32→0,48 m, viền 0,024→0,036 m: **×1,5**, vàng phát sáng nhẹ ≤0,9. Ở camera chơi, bbox chiếu nhỏ nhất qua năm mốc **30,96×22,51 px**; cặp ảnh chỉ ẩn kính đo bbox thật **31×20 px** trở lên, đạt cả hai chiều ≥18 px.

Công cụ được chọn: tái dùng art Firefly đã có; code chỉ đổi bố cục, chuyển động, thời điểm và màu theo phiếu Sonnet PASS. Không cần tạo ảnh/âm mới hoặc gọi tham vấn ngoài cho hướng đã chốt. Hướng giữa mới của owner thay chi tiết bắn chéo bên phải trong phân cảnh 439 gốc.

## Vòng sửa → chụp → mở ảnh

Mỗi vòng chụp và tự mở riêng 0,3 / 0,9 / 1,6 / 1,9 / 2,6 s ở Alt+1 và Alt+2; xem sheet cạnh phân cảnh. Vòng 3–4 thêm 90° ở 1,2 / 1,9 s. Có sheet chuyển pha từ 1,45 tới 3,55 s và sheet giải mã MP4 cuối.

| Vòng | Tự chấm | Phủ nêm 0,9 s | Quầng/lõi 1,9 s | Nhận xét khi mở ảnh và sửa |
|---|---:|---:|---:|---|
| 1 | 5,0 | 39,22% | Không đo được: đoạn co về 0 | Quạt đã so le, kính rõ; phép tính khoảng cách bị dùng sau khi copy nguồn khiến cú cuối nổ sát người. Đốm dư âm chưa hiện do UV lấy vùng trống của atlas. Scenario in tóm tắt gặp null, JSON và ảnh vẫn được lưu. |
| 2 | 6,2 | 39,21% | 118 / 6 px | Giữ riêng khoảng cách hội tụ: cú cuối đúng giữa, đích quái gần trục; dư âm còn trống. Rà UV theo quy ước của FlipbookPool. |
| 3 | 6,6 | 39,22% | 118 / 6 px | Sửa UV, 60 đốm đã hiện và có khoảng trống; camera chơi còn hơi chìm trên nền sáng. p95 5,80 ms. |
| 4 | 7,0 | 39,22% | 118 / 6 px | Nâng màu sprite trong giới hạn 0,9; camera chơi đọc được cụm vàng, góc sau lưng rõ đốm nhấp nháy. Giữ tia cuối giữa; p95 5,70 ms. |

Sheet từng vòng: [439c-comparison.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-1/439c-comparison.jpg), [439c-comparison.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-2/439c-comparison.jpg), [439c-comparison.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-3/439c-comparison.jpg), [439c-comparison.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-comparison.jpg).

Sheet cuối: [439c-top-phases.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-top-phases.jpg), [439c-behind-phases.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-behind-phases.jpg), [439c-transition-sheet.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-transition-sheet.jpg), [439c-overhead-phases.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-overhead-phases.jpg), [439c-video-check.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-video-check.jpg).

## Số đo cuối

Đúng phương pháp 439b: 1280×720, DPR 1, High, Alt+1/Alt+2; ảnh bật/tắt chiêu cùng clock/camera, scenario so đồng nhất trước khi đo. Nêm là tam giác chiếu từ đỉnh kính và hai mút ngoài thật; không chọn ROI dễ đạt. Rec.709 trên RGB ảnh: Y=0,2126R+0,7152G+0,0722B. Phủ nêm: ΔY≥0,15; quầng: ΔY≥0,1; lõi: Y≥0,95; trắng: cả ba kênh ≥0,95. Cắt vuông góc đúng trung điểm đoạn chiếu, đếm dải liên tục qua trục, cửa sổ ±180 px; ≥361 là chạm biên cửa sổ. Ngưỡng bề rộng áp cho camera chơi ở mốc quy định.

| Camera | Giây | Phủ nêm | ROI sau lưng 60%×40% | Trắng toàn khung | Quầng giữa | Quầng hội tụ | Lõi hội tụ | Tia HDR |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Chơi | 0.3 | 0.104% | 0.086% | 0.000000% | 0 | 0 | 0 | 0 |
| Chơi | 0.9 | 39.219% | 13.296% | 0.000000% | 12 | 13 | 0 | 0 |
| Chơi | 1.6 | 52.818% | 14.846% | 0.000000% | 90 | 123 | 0 | 0 |
| Chơi | 1.9 | 40.401% | 11.051% | 0.100586% | 126 | 118 | 6 | 1 |
| Chơi | 2.6 | 0.778% | 0.231% | 0.000000% | 0 | 0 | 0 | 0 |
| Sau lưng | 0.3 | 28.168% | 2.101% | 0.000000% | 85 | 85 | 0 | 0 |
| Sau lưng | 0.9 | 99.240% | 11.065% | 0.000000% | 333 | 185 | 0 | 0 |
| Sau lưng | 1.6 | 93.915% | 16.837% | 0.000000% | ≥361 | 184 | 0 | 0 |
| Sau lưng | 1.9 | 92.230% | 16.162% | 0.004232% | ≥361 | ≥361 | 8 | 1 |
| Sau lưng | 2.6 | 38.080% | 2.902% | 0.000000% | 82 | 82 | 0 | 0 |
| 90° | 1.2 | 32.525% | 2.403% | 0.000000% | 7 | 8 | 0 | 0 |
| 90° | 1.9 | 33.424% | 2.239% | 0.035699% | 69 | 69 | 4 | 1 |

Cổng chính: phủ nêm chơi **39,219%≥18%**; ROI sau lưng **11,065%≥8%** ở 0,9 s; quầng giữa **12 px≥8**; hội tụ **118/6 px≥24/4**; trắng cao nhất trong các khung đo **0,100586%≤6%**. Một tia HDR ở 1,9 s tại cả ba góc, các mốc ngoài hội tụ bằng 0. Góc trục do hook in ra ở khung cuối bằng 0° tại cả ba camera.

Đỉnh sáng là hệ số 0–1 của từng tia trong hook `rayPeakBrightness`, trước envelope quét/thu quạt; không phải độ chói pixel sau bloom. Độ dài dưới đây là tầm ngang dùng để đặt tia, CV tính trên cùng đại lượng. Hai đầu tia biên dùng cùng mẫu seed để giữ trục giữa, tia giữa đạt 100% để làm trục chính.

| Tia | Góc gốc | Độ dài / tầm 20 m | Đỉnh sáng | Quầng giữa tia ở 0,9 s |
|---|---:|---:|---:|---:|
| 1 | -29.200° | 93.276% | 0.735815 | 13 px |
| 2 | -22.832° | 79.061% | 0.670289 | 50 px |
| 3 (chính) | -19.461° | 82.426% | 0.940000 | 49 px |
| 4 | -13.226° | 66.304% | 0.579570 | 14 px |
| 5 | -8.125° | 73.362% | 0.715398 | 32 px |
| 6 (chính) | 0.000° | 100.000% | 1.000000 | 13 px |
| 7 | 6.646° | 87.488% | 0.556639 | 11 px |
| 8 | 11.027° | 79.897% | 0.618728 | 11 px |
| 9 | 20.577° | 71.919% | 0.589804 | 27 px |
| 10 (chính) | 24.075° | 88.889% | 0.980000 | 28 px |
| 11 | 29.200° | 93.276% | 0.741975 | 13 px |

Quầng từng tia nhỏ nhất **11 px≥8**; đo tại trung điểm đoạn chiếu của từng tia thật xuất từ hook, trên bản ghép đầy đủ có hạt/bloom/ánh hắt.

Số gốc: [439c-measure.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-measure.json); cặp on/off nguyên RGB (trái bật, phải tắt): [439c-probe-fan-pair.png](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-probe-fan-pair.png), [439c-probe-focus-pair.png](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-probe-focus-pair.png), [439c-probe-behind-pair.png](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-c-4/439c-probe-behind-pair.png). JSON giữ nguồn/trục/đích thế giới, góc lệch trục và quái, danh sách độ dài/góc/đỉnh sáng, 28 hạt/tia, 60 đốm và thời gian tan.

## Kiểu, hiệu năng và âm

`./node_modules/.bin/tsc --noEmit` theo nguyên tsconfig: **0 lỗi**. `node --check` hai MJS đã sửa/thêm: 0 lỗi. Không chạy build/test suite.

`stress.html` trên server 3148, cách của `metal-ult-rain-review.mjs`: kiểm đủ **87 TargetField sống +13 walker =100** ở đầu từng lượt, kích lại `ult-light`, 240 mẫu/lượt. `total` là CPU cộng chờ GPU qua `readPixels`; bỏ một lượt làm nóng, gộp ba lượt còn lại (720 mẫu).

| Lượt | p95 total | p95 CPU | Kết thúc |
|---|---:|---:|---|
| Làm nóng | 5.50 ms | 1.30 ms | active=false, live=0 |
| Đo 1 | 6.00 ms | 1.40 ms | active=false, live=0 |
| Đo 2 | 5.40 ms | 1.10 ms | active=false, live=0 |
| Đo 3 | 5.60 ms | 1.20 ms | active=false, live=0 |

**p95 gộp total 5.70 ms≤16,7; CPU 1.30 ms.** GPU thật `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`, không phải SwiftShader. Không có exception JS/shader; Quang sẵn sàng, `loadError=null`. Lab còn cảnh báo nhiều KTX2Loader và atlas Metal `metal-crescent-sym` không nạp được như các phiếu trước; không sửa làn khác.

Âm giữ tệp `tt-sfx-ult-light/take1.wav` và mixer runtime có sẵn: gather/release/focus ở 0 /0,6 /1,8 s. Log runtime và gain/bus/reverb được trộn vào clip, không tạo âm hoặc sửa audio-lab. Clip còn tiếng release chung 0,583 s và elite nền 3,35 s của lab. Đã kiểm thông số stream bằng ffprobe và mở sheet giải mã MP4; chưa có đánh giá nghe độc lập.

## Còn để owner/Claude xem

- Xem nhịp thu quạt rồi bắn giữa, độ so le của tia, độ rõ đốm dư âm ở camera chơi. Góc sau lưng vẫn nén quạt thành dải do phối cảnh thấp; dư âm trên nền sáng nhẹ hơn phân cảnh tối.
- Cú nổ vẫn hơi cam, chất liệu nền và model Lam của lab khác phân cảnh. Không nâng tự chấm thành nghiệm thu thương mại: cần hai giám khảo mù ≥8,5 ở host chơi trước khi đưa vào production.
- Không tạo art/âm mới vì đủ thành phần sẵn có; không mở Blender hoặc gọi công cụ ảnh. Không dựng lại index review vì tệp index nằm ngoài whitelist ghi của phiếu (như 439/439b). Không sửa tài liệu hoặc hạ tầng của làn khác.

## Lưu và dọn

Ảnh/chỉ số chỉ nằm trong `captures/tu-tien/light-ult-439/round-c-*`, `frames-c-round-3/4`, `video-check-c-4`; các thư mục mới có `ABOUT.md`. Sau khi giữ sheet, cặp on/off cần đối chiếu và JSON, dọn khung thô **chỉ các thư mục do 439c tạo** bằng `tools/capture-prune/prune.mjs`, xem dry-run trước `--apply --min-age-min 0`. Không đụng `round-b-*` hoặc khung người khác. Đã xóa **433 ảnh thô/trung gian, 479,184 MB**, giữ 15 ảnh đối chiếu/sheet có liên kết; JSON/clip được giữ. Nhật ký dọn: `captures/tu-tien/light-ult-439/439c-prune.log`.

Chạy lại từ gốc repo, giữ server 3148; chọn ROUND mới, tối đa 5 vòng theo phiếu:

```sh
ROUND=5 FINAL=1 CHROME_FLAGS='--use-angle=metal --enable-gpu --disable-background-networking' node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review-c.mjs --width=1280 --height=720 --dpr=1
```

Scenario tự chặn cổng hình trước khi xuất clip và chặn p95/GPU phần mềm/exception sau phép đo. JPG giao là bản sao sheet `439c-comparison.jpg` của vòng cuối. Các số đo phục vụ phiếu này, không thay phán xét mỹ thuật.
