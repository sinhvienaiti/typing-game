# Phiếu 439d — Quang: tia mềm và cú hội tụ có lực

17/11/2026. **Đã làm 4 vòng sửa → chụp → mở ảnh; đạt các ngưỡng định lượng, kiểm kiểu 0 lỗi, p95 5,70 ms. Chưa có nghiệm thu mỹ thuật 8,5 của hai giám khảo mù.**

## Giao nộp

- [light-ult-codex-d.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-d.jpg): phân cảnh gốc cạnh camera chơi và sau lưng; pha va chạm ở 2,05 s để thấy quái đã lùi.
- [light-ult-codex-d.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-d.mp4): 4 giây, 120 khung, 30 fps, 1280×720, H.264 + AAC, 2.185.403 byte. Đã giải mã và mở [sheet kiểm clip](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-d-4/439d-decoded-sheet.jpg).
- Đã thêm dòng bản d vào `owner-review/2026-11-17/tu-tien/ABOUT.md`, giữ nguyên a/b/c.

Chỉ sửa `games/.wt-ic-lab-all/src/lab/light-ult-fan.ts`, `light-ult-fan-space.ts`, `light-ult-glow-probe.mjs`; thêm `light-ult-impact.ts`, `light-ult-review-d.mjs`. Các phần đất, kính và dư âm được chỉnh qua tham số trong `light-ult-fan.ts`. Import, không sửa `ult-camera-punch.ts`; không sửa `skills-main.ts` hoặc `showcase.ts`.

## Đã sửa

**Tia.** Bao quầng Gaussian, thân phình ở giữa và thuôn về hai đầu; 32% cuối chiều dài tan bằng smoothstep. Có nhiễu chảy, sợi sáng xoắn, bề rộng dao động và rung sáng nhẹ. Tia quạt vươn trong 0,18–0,23 s, tia hội tụ trong 0,15 s. Giữ 11 tia, seed 439.31, CV chiều dài **0,118684125**, ba tia chính 3/6/10, 28 hạt art/tia; thu quạt 1,45–1,80 s. Tia cuối lệch trục **0°**, quái chọn lệch **1,97856°**. Hướng giữa theo owner, thay chi tiết bắn chéo của phân cảnh gốc.

**Va chạm.** Tia cuối bắt đầu ở 1,80 s, chạm ở **1,95 s**. Một `light-big-burst` **5,8 m** cùng lớp `light-impact`, lóe thêm đúng **2 khung 60 Hz**, **48 hạt lăng kính có vệt**, **14 tia tỏa ngắn mềm**. Mọi vệt/sao dùng ngôi sao cô lập từ atlas Firefly `light-sparkle`, không vẽ sao mới. Đèn điểm vàng đặt ở đích, tan trong 0,3 s, rọi đất/quái; không thêm vòng hoặc đĩa.

**Lực và phản ứng.** 10 quái trong 4,8 m quanh đích nhận viền vàng, recoil và shove. Cú cuối gọi trực tiếp API hit/shove của đàn quái, tránh hook host cũ giữ quái 0,45 s: phản ứng diễn ra ngay, không thêm hit-stop. Độ dịch chuyển thực ở 1,9667 s **0,240–0,458 m**; ở 2,05 s **0,644–1,241 m**, gồm shove, recoil và chuyển động đàn. `UltCameraPunch` đẩy gần 4%, vào 35 ms, giữ tới 85 ms, trả trong 300 ms, giữ hướng nhìn sẵn có; rung nhẹ từ hook focus có sẵn. Camera trả về với sai số **0 m**, tỷ lệ khoảng cách 1, góc 55° như ban đầu.

**Tụ lực và dư âm.** 28 hạt art hút vào kính, lóe nhỏ trước khi phóng; quái trong quạt có viền vàng. Tăng hắt sáng nêm từ 0,065 lên 0,18; RGB phụ ≤0,9. Giữ 60 đốm dư âm có khoảng trống, tăng kích thước/độ hiện, tan trong 1,3 s. Tái dùng art/âm sẵn có theo `VFX_STANDARD`, skill `game-vfx-production`, `game-vfx-layered`, `game-vfx`; không tạo tài nguyên mới.

## Vòng tự xem

| Vòng | Tự chấm tham khảo | Phủ nêm 0,9 s | Burst 1,95 s | Nhìn thấy và sửa |
|---|---:|---:|---:|---|
| 1 | 6,5 | 45,73% | 67,74% | Tia mềm hơn, đốm rõ; camera punch hướng thẳng vào đích làm lệch khung quá nhiều. Script lưu ảnh/JSON rồi lỗi khi in mặt cắt null ở góc sau lưng. |
| 2 | 7,0 | 45,73% | 67,74% | Sửa tâm camera theo hướng nhìn hiện tại; giữ được vùng chiêu. Tăng độ rõ vệt lăng kính và làm lõi hội tụ gọn hơn. |
| 3 | 7,2 | 45,73% | 67,63% | Đo thêm mặt cắt đúng 20/50/85% chiều dài thế giới và riêng tia giữa. Phát hiện hook host giữ quái đứng 0,45 s; p95 5,60 ms. |
| 4 | 7,5 | 45,73% | 67,63% | Bỏ giữ quái ở cú cuối, quái lùi ngay cùng burst; camera trả lại đúng góc, bụi đọc được. p95 5,70 ms. |

Điểm tự chấm chỉ ghi vòng lặp, không thay owner hoặc giám khảo. So phân cảnh từng pha qua ảnh/sheet, cả camera chơi và sau lưng; vòng 3–4 thêm góc 90° ở 1,2/1,9 s.

- Vòng 1: [so phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-1/439d-comparison.jpg), [nhịp chiêu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-1/439d-transition-sheet.jpg).
- Vòng 2: [so phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-2/439d-comparison.jpg), [nhịp chiêu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-2/439d-transition-sheet.jpg).
- Vòng 3: [so phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-3/439d-comparison.jpg), [nhịp chiêu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-3/439d-transition-sheet.jpg).
- Vòng 4: [so phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-comparison.jpg), [nhịp chiêu](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-transition-sheet.jpg).

## Số đo cuối

[JSON đầy đủ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-measure.json), [ảnh các pha chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-play-inspection.jpg), [góc 90°](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-overhead-sheet.jpg).

Phép đo giữ định nghĩa của 439c: cùng thời gian/camera, bật/tắt nhóm Quang, Rec.709 trên RGB ảnh chuẩn hóa; phủ sáng ΔY≥0,15; quầng ΔY≥0,1; lõi Y≥0,95. Probe kiểm thời gian và camera khung nền giống hệt khung có chiêu. Đèn/flash của host ở ngoài nhóm Quang vẫn có trong cả hai khung, nên không cộng phần đó vào độ phủ Quang.

| Camera | Giây | Phủ nêm | Phủ ROI sau lưng | Trắng toàn khung | Số tia HDR |
|---|---:|---:|---:|---:|---:|
| Chơi | 0.3 | 0.11% | 0.11% | 0.0000% | 0 |
| Chơi | 0.9 | 45.73% | 17.26% | 0.0000% | 0 |
| Chơi | 1.6 | 55.65% | 18.20% | 0.0000% | 0 |
| Chơi | 1.9 | 24.88% | 8.20% | 0.0622% | 1 |
| Chơi | 1.95 | 52.94% | 13.76% | 0.0744% | 1 |
| Chơi | 2.05 | 47.82% | 13.28% | 0.0827% | 1 |
| Chơi | 2.6 | 2.82% | 0.77% | 0.0000% | 0 |
| Sau lưng | 0.3 | 28.49% | 2.40% | 0.0000% | 0 |
| Sau lưng | 0.9 | 99.30% | 11.45% | 0.0000% | 0 |
| Sau lưng | 1.6 | 93.70% | 17.53% | 0.0000% | 0 |
| Sau lưng | 1.9 | 90.26% | 13.39% | 0.0043% | 1 |
| Sau lưng | 1.95 | 92.49% | 17.24% | 0.0028% | 1 |
| Sau lưng | 2.05 | 90.62% | 18.64% | 0.0047% | 1 |
| Sau lưng | 2.6 | 64.21% | 5.42% | 0.0000% | 0 |

- **Burst tại 1,950 s:** tâm chiếu từ hook, tròn bán kính 120 px; **67,633% ≥45%**, trắng **0,074436% ≤6%**. Các khung 1,9667/1,9833/2,000/2,050 s cũng được ghi trong JSON. Trắng cao nhất mọi khung đo **0,084527%**.
- **Độ thuôn tia giữa ở 0,9 s:** chiếu đúng ba điểm ở 20/50/85% chiều dài thế giới; quầng bản ghép **98/24/2 px**, tỷ lệ 85/50 **0,0833≤0,6**. Tách riêng tia để loại hắt đất/hạt/tia khác: **8/13/2 px**, tỷ lệ **0,1538**. [Tia riêng bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-middle-isolated-on.png), [tia riêng tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-middle-isolated-off.png). Không đổi định nghĩa mặt cắt giữa nêm cũ.
- **Quầng quạt:** mặt cắt giữa nêm cũ **103 px**; mặt cắt giữa từng tia theo phép cũ **25/71/95/230/208/30/11/40/85/62/54 px**, đều ≥8. Đây là số đo bản ghép có hắt đất/hạt và tia lân cận; quầng riêng tia giữa là 13 px.
- **Hội tụ 1,9 s:** quầng/lõi **113/9 px**, đích ≥24/4; đúng một tia HDR. Góc 90° ở 1,9 s: **47/4 px**, một tia HDR; ở 1,2 s: không có tia HDR.
- **Kính camera chơi:** bbox chiếu nhỏ nhất khoảng **30,96×22,47 px**, bbox ảnh chỉ ẩn kính ít nhất **31×20 px**, đạt ≥18.
- **Đỉnh sáng 11 tia:** 0,7358 / 0,6703 / 0,9400 / 0,5796 / 0,7154 / 1,0000 / 0,5566 / 0,6187 / 0,5898 / 0,9800 / 0,7420. CV, số hạt/tia, seed và chiều dài từng tia được giữ/in trong JSON.

## Kiểm kiểu, hiệu năng và âm

`./node_modules/.bin/tsc --noEmit`: **0 lỗi**. `node --check` probe và scenario: 0 lỗi. Không chạy build/bộ test game.

`stress.html` 3148, 1280×720 DPR1 High; mỗi lượt kiểm đủ **87 TargetField +13 walker =100**. Bốn lượt kích chiêu, mỗi lượt 240 mẫu; bỏ lượt làm nóng, gộp 720 mẫu. `total` = CPU + chờ GPU qua `readPixels`, giữ cách `metal-ult-rain-review.mjs`.

| Lượt | p95 total | p95 CPU |
|---|---:|---:|
| Làm nóng | 5.90 ms | 1.50 ms |
| Đo 1 | 5.60 ms | 1.20 ms |
| Đo 2 | 5.90 ms | 1.30 ms |
| Đo 3 | 5.70 ms | 1.20 ms |

**p95 gộp total 5,70 ms≤16,7; CPU 1,20 ms.** GPU `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`. Không có exception JS/shader; asset Quang ready, `loadError=null`. Có cảnh báo sẵn có về nhiều KTX2Loader và atlas Metal không tải được; không sửa làn Metal.

Âm `tt-sfx-ult-light/take1.wav` từ mixer sẵn có: gather 0 / release 0,600 / focus **1,950 s**, khớp khung chạm; giữ gain/bus/reverb/đoạn nguồn. Log còn tiếng release chung 0,583 s và elite nền 3,35 s. [Log âm](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-d-4/439d-sound-takes.json). Đã kiểm stream và sheet giải mã, chưa có đánh giá nghe độc lập.

## Phần để owner xem và phần bỏ qua

Owner xem độ mềm ở đoạn 0,6–1,6 s, lực nổ/giật lùi ở 1,95–2,15 s và độ rõ bụi ở 2,6 s. Hạn chế: nền lab sáng và model Lam khác phân cảnh; góc sau lưng nén quạt thành dải ngang, burst vẫn ấm/cam hơn ảnh demo. Chưa khẳng định đạt mỹ thuật 8,5; cần hai giám khảo mù ở host chơi trước khi đưa vào production.

Không tạo ảnh/âm mới vì đã có đủ thành phần. Bỏ hit-stop theo phiếu. Không dựng lại index review vì index nằm ngoài các đường dẫn được phép ghi của phiếu. Một lane; quota lúc nhận còn 73%; Chrome chỉ headless, chỉ localhost, giữ server 3148. Không sửa production, docs Tu Tiên, script/test game, audio-lab hoặc tài nguyên; không commit/push/reset/clean/stash/đổi nhánh.

## Dọn ảnh

Chỉ dọn `round-d-1..4`, `frames-d-round-3/4`, `video-check-d-4` do lượt này tạo bằng `tools/capture-prune/prune.mjs`, dry-run trước `--apply --min-age-min 0`, giữ các sheet/ảnh có liên kết trên và JSON. Mỗi thư mục mới có `ABOUT.md`. Đã xóa **583 ảnh thô/trung gian, 615.314 MB**, giữ 13 ảnh/sheet có liên kết; từ chối 0 mục. Nhật ký: `captures/tu-tien/light-ult-439/439d-prune.log`. Không đụng các lượt a/b/c hoặc ảnh của người khác.
