# Phiếu 439b — Quầng hổ phách và tia hội tụ Quang

17/11/2026. **Đạt các cổng đo của phiếu; đã tự mở từng ảnh qua 4 vòng. Chưa có nghiệm thu mỹ thuật 8,5 từ hai giám khảo mù.** Tự chấm thận trọng vòng cuối 7,0/10; điểm này không thay số đo hoặc đánh giá của Claude/chủ.

## Tệp giao và phạm vi

- [Ảnh đối chiếu mới](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-b.jpg).
- [Clip mới, 4 giây có âm](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-b.mp4).
- Đã thêm một dòng `light-ult-codex-b` vào `owner-review/2026-11-17/tu-tien/ABOUT.md`. Cặp `light-ult-codex.jpg/.mp4` cũ được giữ nguyên.

Chỉ sửa `games/.wt-ic-lab-all/src/lab/light-ult-fan.ts`, `light-ult-fan-space.ts`; thêm `light-ult-ground.ts`, `light-ult-glow-probe.mjs`, `light-ult-review-b.mjs`. Ngoại lệ hook kế thừa phiếu 439: chỉ mở rộng kiểu tham số và nhánh `window.__lab.lightUlt()` trong `skills-main.ts` để nhận `hideLight/showLight`, render lại mà không bước thời gian. Không đổi phần khác của hook/lab chung.

Một luồng, quota còn 77% khi bắt đầu. Không commit/push/reset/clean/stash, không đổi nhánh, không build hoặc chạy bộ test game. Không sửa production, tài liệu Tu Tiên, script/test game, âm thanh hoặc vật liệu nguồn; không gọi mạng ngoài localhost. Giữ nguyên server 3148, Chrome luôn headless và được runner đóng sau mỗi lượt. Không dựng lại index review vì các tệp index nằm ngoài whitelist của phiếu.

## Đã làm

- 13 tia thế giới, mỗi tia có lõi trắng ấm mảnh, quầng hổ phách mềm, nhiễu chạy dọc và **28 sprite hạt vàng trôi**. Tái dùng atlas Firefly `light-sparkle`; pool 512 giữ đủ 364 hạt trên tia và các glint khác. Hệ số bề ngang shader cho tỷ lệ FWHM quầng/lõi khoảng 9,2 lần; kênh RGB lớp phụ được chặn ở 0,9.
- Đầu tia mềm, độ dài biến thiên 17,5–20 m, cường độ quét trái sang phải. Hai mặt dải giao nhau trong thế giới, không khóa theo màn hình.
- Một tia hội tụ duy nhất có lõi HDR 12, thân/quầng phụ vẫn ≤0,9. Thu bề ngang thế giới về 1,9 m sau khi đo lõi; dùng `light-big-burst`, `light-impact` lớn và các sprite lăng kính ở đúng điểm trúng. Frame burst tính từ sự kiện hội tụ, không chạy vòng theo đồng hồ toàn chiêu.
- Decal **tam giác hình nêm**, mép và đầu mờ, hắt ấm lên nền. Không thêm vòng, đĩa, trận pháp hoặc cột trời.
- 96 cụm `gold-dust-motes-loop-w2` phủ vùng nêm, trôi nhẹ và tan dần đến 3,6 s. Chỉ tái dùng thành phần có sẵn, không tạo ảnh/âm mới.
- Sửa lỗi UV: trước đây thu hình học thành hình thang làm đường UV lõi lệch khỏi trục world. Nay mesh chữ nhật giữ UV affine, shader thu quầng quanh đúng trục. Probe đo đúng trung điểm đường nối, không dịch probe để tìm vệt sáng.

## Vòng sửa → chụp → xem → so phân cảnh

Mỗi vòng chụp 0,3 / 0,9 / 1,6 / 1,9 / 2,6 s ở Alt+1 và Alt+2, mở từng ảnh rồi xem sheet cạnh phân cảnh được chỉ định. Vòng 4 thêm hai ảnh 90°. Các số trong bảng lấy từ PNG gốc, không lấy từ JPG sheet.

| Vòng | Tự chấm | Phủ nêm chơi 0,9 s | ROI sau lưng 0,9 s | Quầng tia giữa 0,9 s | Quầng/lõi hội tụ 1,9 s | Trắng tối đa | Nhận xét sau khi xem |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | 5,5 | 92,89% | 29,46% | 281 px | 158 / 0 px | 0,009983% | Đã sáng nhưng quầng dính thành tấm, ánh hắt quá mạnh; lõi chưa nằm đúng trục probe. |
| 2 | 6,1 | 45,03% | 10,79% | 13 px | 162 / 0 px | 0,158746% | Tách được tia, giảm nền sáng; thấy lõi bị cong/lệch do UV của dải hình thang. |
| 3 | 6,6 | 49,66% | 11,43% | 32 px | 175 / 10 px | 0,176107% | Sửa trục lõi, đạt ngưỡng; tia hội tụ còn dày, điểm trúng giống búi lửa hơn chùm tia lăng kính. |
| 4 | 7,0 | **51,01%** | **11,53%** | **32 px** | **165 / 6 px** | **0,118490%** | Thu hẹp hội tụ, tăng `light-impact` và thêm lớp lăng kính; dừng sau khi xem đủ ảnh, sheet và sheet giải mã MP4. |

Sheet từng vòng: [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-1/439b-comparison.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-2/439b-comparison.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-3/439b-comparison.jpg), [vòng 4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-comparison.jpg).

Giữ [năm pha chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-top-phases.jpg), [năm pha sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-behind-phases.jpg), [hai khung 90°](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-overhead-phases.jpg), [sheet MP4 giải mã](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-video-check.jpg), [sheet vật liệu burst đã xem](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-3/439b-burst-source-sheet.jpg).

## Cách đo và kết quả mỗi khung cuối

1280×720, DPR 1, High, camera thật Alt+1/Alt+2; không đổi hậu kỳ chung. `lightUlt()` xuất `fanWorld/fanScreen` gồm đỉnh kính và hai mút ngoài cùng; `fanMidScreen` là phép chiếu trung điểm world của hai mút. `focusWorld/focusScreen` xuất hai đầu tia hội tụ. Hai ảnh on/off giữ nguyên clock, camera, pose và phản ứng quái; scenario kiểm đồng nhất clock/camera trước khi tính. `hideLight` chỉ ẩn nhóm Quang, không tiến thời gian; flash phản ứng ở host vẫn ở cả hai ảnh, nên không làm tăng chênh lệch.

`light-ult-glow-probe.mjs` đọc RGB PNG 8 bit, chuẩn hóa 0–1, tính **Y = 0,2126 R + 0,7152 G + 0,0722 B** trên RGB màn hình. Không dùng gray mặc định của ImageMagick. Phủ sáng: tâm pixel nằm trong tam giác chiếu, ΔY ≥0,15. ROI sau lưng: x=256–1023, y=216–503, đúng 768×288 px. Trắng: cả R/G/B ≥0,95 trên toàn khung.

Cắt vuông góc đoạn chiếu tại trung điểm, nội suy song tuyến tính, bước 1 px trong cửa sổ ±180 px. Quầng: ΔY ≥0,1; lõi: Y tuyệt đối ≥0,95. Bảng dùng **dải liên tục qua trục**, chặt hơn việc cộng các hạt rời/nhánh tia khác. JSON cũng giữ toàn bộ mẫu và tổng số mẫu qua ngưỡng. Khi rà lại thấy quầng hội tụ vượt cửa sổ ±80 px ban đầu, đã mở probe lên ±180 px và tính lại toàn bộ các vòng từ đúng cặp PNG cũ: quầng cuối chốt 165 px; các cổng khác không đổi. Giá trị ≥361 nghĩa dải chạm biên cửa sổ; các ngưỡng nghiệm thu bề rộng chỉ áp cho camera chơi ở mốc quy định.

| Camera | Giây | Phủ nêm | ROI giữa 60%×40% | Trắng toàn khung | Quầng giữa | Quầng hội tụ | Lõi hội tụ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Chơi | 0,3 | 0,041% | 0,034% | 0% | 0 | 0 | 0 |
| Chơi | 0,9 | 51,006% | 16,328% | 0% | 32 | 11 | 0 |
| Chơi | 1,6 | 62,252% | 19,700% | 0% | 33 | 66 | 0 |
| Chơi | 1,9 | 35,585% | 15,735% | 0,083116% | 15 | 165 | 6 |
| Chơi | 2,6 | 5,293% | 1,369% | 0% | 0 | 0 | 0 |
| Sau lưng | 0,3 | 18,745% | 1,092% | 0% | 61 | 0 | 0 |
| Sau lưng | 0,9 | 99,321% | 11,527% | 0% | 332 | 40 | 0 |
| Sau lưng | 1,6 | 99,463% | 19,883% | 0% | ≥361 | 99 | 0 |
| Sau lưng | 1,9 | 99,196% | 23,889% | 0,118490% | ≥361 | 126 | 11 |
| Sau lưng | 2,6 | 76,632% | 10,497% | 0% | 11 | 7 | 0 |
| Trên 90° | 1,2 | 38,527% | 2,649% | 0% | 8 | 4 | 0 |
| Trên 90° | 1,9 | 22,799% | 2,601% | 0,030816% | 4 | 57 | 4 |

Đo bổ sung từng tia thật tại trung điểm đoạn chiếu của chính nó, ở 0,9 s camera chơi: **135 / 31 / 59 / 67 / 95 / 14 / 11 / 16 / 9 / 15 / 14 / 13 / 10 px**, nhỏ nhất **9 px ≥8**. Nguồn world từ hook, chiều dài/góc theo đúng công thức mesh, camera tái dựng từ position/quaternion/FOV được lưu. Đây là bề rộng trong bản ghép đầy đủ, có bloom/hạt/ánh hắt, không phải đo lớp tia cô lập.

Số gốc: `round-b-1` đến `round-b-4/439b-measure.json`; [JSON cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-measure.json), [13 tia](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-all-rays.json). Giữ cặp on/off nguyên RGB, trái bật/phải tắt: [tia quạt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-probe-fan-pair.png), [hội tụ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-probe-focus-pair.png), [sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-b-4/439b-probe-behind-pair.png).

Kính chơi vẫn có bbox chiếu nhỏ nhất khoảng 20,64×14,98 px; hook xác nhận đúng **một** mesh tia HDR ở 1,9 s tại cả ba góc, các mốc ngoài hội tụ bằng 0. Không biến số đo quầng thành đánh giá mỹ thuật.

## Kiểu, hiệu năng và clip

`./node_modules/.bin/tsc --noEmit` theo nguyên tsconfig: **0 lỗi**. Hai scenario/probe MJS qua `node --check`. Không chạy build/test suite.

`stress.html`, cách của `metal-ult-rain-review.mjs`: mỗi lượt kiểm đủ **87 TargetField sống + 13 walker = 100**, kích `ult-light`, 240 mẫu. `total` là CPU cộng chờ GPU qua `readPixels`; bỏ lượt làm nóng, gộp 720 mẫu còn lại.

| Lượt | p95 total | p95 CPU | Live cuối |
|---|---:|---:|---:|
| Làm nóng | 5,90 ms | 1,60 ms | 0 |
| Đo 1 | 5,70 ms | 1,30 ms | 0 |
| Đo 2 | 5,70 ms | 1,30 ms | 0 |
| Đo 3 | 5,70 ms | 1,40 ms | 0 |

**Gộp p95 total 5,70 ms ≤16,7 ms; CPU 1,30 ms.** Renderer `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`, không phải SwiftShader. Không có exception JS/shader; Quang `assetsReady=true`, `loadError=null`. Log lab còn cảnh báo nhiều KTX2Loader và lỗi atlas Metal có sẵn, ngoài phạm vi sửa.

`ffprobe`: H.264 1280×720, 120 khung/30 fps, 4,000 giây; AAC 4,000 giây. Âm Quang giữ sự kiện gather/release/focus ở 0 / 0,6 / 1,8 s, bộ trộn giữ log runtime. Clip cũng chứa tiếng release chung ở 0,583 s và elite nền ở 3,35 s của lab; không sửa âm của làn khác.

## Chủ/Claude cần xem

Các cổng định lượng đạt, nhưng quạt còn thẳng và đều hơn phân cảnh, tia lửa cuối còn mang sắc cam; lăng kính xanh/hồng khá nhẹ. Góc sau lưng đọc được ánh quạt và hạt nhưng vẫn nén thành dải theo phối cảnh thấp. Nền/nhân vật lab khác tranh và chưa có đánh giá nghe hoặc hai giám khảo mù. Cần xem cặp JPG/MP4 mới trước khi kết luận 8,5 hoặc đưa vào game.

Khung thô riêng của phiếu được dọn bằng `tools/capture-prune/prune.mjs` sau dry-run, chỉ nhắm `round-b-*` và `frames-b-round-4`; giữ ảnh đối chiếu/sheet có liên kết ở trên cùng JSON/clip. Đã xóa **242 ảnh, 239,652 MB**, giữ 12 ảnh đối chiếu/sheet; nhật ký `captures/tu-tien/light-ult-439/439b-prune.log`. Không đụng khung của 439 hoặc người khác.

Chạy lại từ gốc repo, dùng server 3148 hiện có:

```sh
ROUND=5 FINAL=1 CHROME_FLAGS='--use-angle=metal --enable-gpu --disable-background-networking' node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review-b.mjs --width=1280 --height=720 --dpr=1
```

Scenario lưu số đo trước bước clip, tự chặn nếu cổng hình trượt. MP4 chỉ ghi tên `light-ult-codex-b.mp4`; JPG giao là bản sao `439b-comparison.jpg` của vòng cuối.
