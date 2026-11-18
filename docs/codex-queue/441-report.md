# Phiếu 441 — Quang: video D tại điểm trúng

17/11/2026. **Đã đóng gói và nối D, tự chụp/xem 4 vòng; đạt các ngưỡng định lượng của phiếu.** Kiểm kiểu 0 lỗi; p95 **5,80 ms**. Chưa có nghiệm thu mỹ thuật 8,5 của hai giám khảo mù trong host chơi.

## Giao nộp

- [light-ult-codex-e.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-e.jpg): phân cảnh gốc cạnh bốn pha ở camera chơi và sau lưng; pha nổ dùng khung sáng nhất tìm được.
- [light-ult-codex-e.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-e.mp4): **4 s, 120 khung, 30 fps, 1280×720, H.264 + AAC, 2.179.732 byte**. `ffmpeg -f null -` giải mã toàn bộ không lỗi; đã mở [sheet giải mã](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/video-check-e-4/441-decoded-sheet.jpg).
- Bộ **`games/.wt-ic-lab-all/art-src/lab/vfx/light/light-prism-burst.{atlas.png,json,uastc.ktx2,prompt.txt}`**, thêm `light-prism-burst.atlas.prompt.txt`. Thư mục `art-src` là symlink tài nguyên sẵn có sang game chính. Giữ file `light-big-burst` cũ và mọi bản a/b/c/d.
- Đã ghi thành phần mới vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`, thêm dòng e trong `owner-review/2026-11-17/tu-tien/ABOUT.md`.

## Đóng gói và nối

Nguồn owner chọn «Bản 1»: `games/immortality-cultivation/art-src/lab/vfx/light/firefly-raw/light-prism-burst.v1-try1.mp4`, Adobe Firefly Video, 1080², 24 fps, 121 khung. Tham chiếu riêng của repo: `stills-55/light-prism-burst.v1-try4.png`. Không sinh ảnh, video hoặc âm mới.

`light-ult-cut.mjs` lấy **32 khung duy nhất, chỉ số 0–70** trong 0–3 s theo `round(i×72/32)`; 8×4 ô 256², atlas 2048×1024, fps metadata **10,6667**, không loop. Crop cố định **[-100,-125,1280,1280]** đệm đen, thu đồng nhất; không xoay, ép hình hoặc che mép. Đen thành **straight alpha**, RGB chuẩn hóa theo maxRGB, alpha từ maxRGB đã crush 5/255; tám khung cuối fade smoothstep 1→0. Khung cuối PNG RGBA bằng 0; KTX2 giải mã alpha bằng 0.

Điểm chạm nguồn **[540; 669,6] px** (62% chiều cao), pivot ô **[0,5; 0,62078125]**, tính từ trên trái. Lề PNG trái/phải/trên/dưới **36/33/35/40 px**, KTX2 giải mã **36/34/35/40 px**, ngưỡng alpha >12/255; tối thiểu **12,89%**. KTX2 **UASTC mức 2, sRGB, Zstd, Y-flip, 12 mip**, 766.079 byte. SHA-256 nguồn và kiểm gói nằm trong JSON. Đã xem [nguồn](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/source-e-441/441-source-sheet.jpg) và [tám khung đóng gói](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/source-e-441/441-packed-sheet.jpg).

**Trong lab:** `LightPrismBurst` dùng mặt phẳng thế giới **7 m**, dựng đứng, chỉ xoay Y về camera; dịch hình học theo pivot để chấm chạm ở **y=0,025 m**. Neo được cố định ở lần trúng đầu, không đi theo thấu kính sau đó: độ trôi đo trên các mốc hiện hình ở cả hai góc **0 m**. Chạy 32 khung trong **1,35 s** từ va chạm **1,95 s** đến **3,30 s**, giữ nhịp kết thúc 439d. Không lặp atlas hoặc bật lại khung đầu. Shader nội suy ánh sáng đã nhân alpha; đổi độ sáng alpha nguồn về gần miền tuyến tính trước khi phối, nhấn HDR theo phần nóng để giữ các mặt tinh thể.

Thay `light-big-burst` tại đích bằng D; giữ **48 vệt lăng kính, 14 tia tỏa, đèn điểm rọi đất/quái 0,3 s, rung và `UltCameraPunch`, giật lùi, âm**. Lớp `light-impact` phụ giảm alpha 0,85→0,20, lóe 2 khung giảm 0,9→0,35 để tránh lấn D. Không thêm vòng/đĩa dưới đất.

Tia hội tụ vẫn giữa trục quạt; độ lệch số học ở 1,9 s **0,00000121°**. Phần cuối quầng thu hẹp theo cả chiều rộng và alpha, không còn mặt cắt cụt. HDR thân tia 6 trước chạm, 3,5 sau chạm, dành điểm nhấn cho nổ. Giữ hạt giống **439.31**, 11 tia, ba tia chính 3/6/10, CV độ dài **0,118684125**, độ sáng đỉnh 0,55–1,0, 28 hạt/tia, thu quạt 0,35 s, 60 đốm dư âm và thời điểm âm 439d.

## Bốn vòng tự xem

Đã mở ảnh rồi đối chiếu ô dưới trái của `art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`; hướng giữa giữ theo owner, thay hướng chéo trong phân cảnh. Điểm tự chấm là tham khảo vòng lặp, không thay nghiệm thu 8,5.

| Vòng | Tự chấm | Khung nổ | Phủ điểm trúng | p95 | Quan sát và sửa |
| --- | --- | --- | --- | --- | --- |
| 1 | 6,5 | 1.9667 s | 72.56% | — | Neo đứng và đầu tia thuôn đúng; lớp lóe cũ lấn các mặt lăng kính. |
| 2 | 6,8 | 1.9667 s | 72.42% | 5.90 ms | Giảm lóe cũ, tăng hình D; ảnh tách riêng còn bị bloom làm nhạt. |
| 3 | 6,8 | 1.9667 s | 72.42% | 5.80 ms | Cố định điểm chạm, đo neo trôi 0 m; giữ hình để kiểm riêng hai góc. |
| 4 | 7,2 | 1.9667 s | 61.31% | 5.80 ms | Giữ độ sáng nguồn trong miền tuyến tính, chỉ nhấn HDR vào phần nóng; giảm lớp phụ và thân tia sau chạm. Chi tiết rõ hơn, ngưỡng phủ vẫn đạt. |

Ảnh đối chiếu [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-1/441-comparison.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-2/441-comparison.jpg), [vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-3/441-comparison.jpg), [vòng 4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-comparison.jpg). [Nhịp cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-transition-sheet.jpg); [các pha hai góc vòng 3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-3/441-phases-sheet.jpg); ảnh tách D vòng cuối [chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-prism-isolated-top.png), [sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-prism-isolated-behind.png).

## Số đo cuối

[JSON đầy đủ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-measure.json). Chrome headless, server **3148** sẵn có, High, **1280×720 DPR1**, nền **`?ground=%23353a40`**. Giữ định nghĩa 439d: Rec.709 trên RGB ảnh chuẩn hóa; phủ sáng **ΔY≥0,15**, quầng **ΔY≥0,1**, lõi **Y≥0,95**; khung nền cùng thời điểm/camera, chỉ tắt nhóm Quang. Đèn/flash host ở ngoài nhóm còn trong cả hai khung. Ngưỡng phủ điểm trúng 55% áp cho camera chơi như phép đo 439d; ngưỡng sau lưng vẫn là ROI giữa ≥8% ở 0,9 s.

**Khung nổ: 1,9666667 s**, cao nhất theo **luma trung bình tuyệt đối trong tròn bán kính 120 px quanh điểm chạm đất** trong 31 khung 60 Hz từ **1,95 đến 2,45 s**. Không chọn theo độ phủ hoặc chọn trước thời điểm. Đã in thời điểm ra log.

- Camera chơi: tâm **[640,0534; 186,1841] px**, **27.736 / 45.239 pixel sáng = 61,3099% ≥55%**; luma trung bình **0,490544**, ΔY trung bình **0,209251**.
- Sau lưng: cùng khung cực đại **1,9666667 s**, tâm **[640,0735; 405,7310]**, phủ **44,6848%**, luma trung bình **0,558679**. Đây là số đo bổ sung; ngưỡng 55% không được áp sang góc này.
- Trắng cao nhất toàn bộ khung cố định, góc 90° và 62 khung quét hai góc: **0,0249566% ≤6%**.

Giữ cặp khung cực đại để đo lại: chơi [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-scan-top-1.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-scan-top-1-off.png); sau lưng [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-scan-behind-1.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-scan-behind-1-off.png).

| Camera | Giây | Phủ nêm | Phủ ROI sau lưng | Trắng toàn khung | Tia HDR |
| --- | --- | --- | --- | --- | --- |
| Chơi | 0.3000 | 0.12% | 0.13% | 0.000000% | 0 |
| Chơi | 0.9000 | 61.24% | 22.94% | 0.000000% | 0 |
| Chơi | 1.6000 | 69.98% | 22.29% | 0.000000% | 0 |
| Chơi | 1.9000 | 32.77% | 10.17% | 0.023546% | 1 |
| Chơi | 1.9500 | 54.51% | 14.62% | 0.024957% | 1 |
| Chơi | 1.9667 | 46.16% | 12.69% | 0.000000% | 1 |
| Chơi | 2.0500 | 46.30% | 12.69% | 0.000000% | 1 |
| Chơi | 2.6000 | 5.94% | 1.08% | 0.000000% | 0 |
| Sau lưng | 0.3000 | 28.87% | 2.50% | 0.000000% | 0 |
| Sau lưng | 0.9000 | 99.24% | 12.23% | 0.000000% | 0 |
| Sau lưng | 1.6000 | 93.64% | 18.76% | 0.000000% | 0 |
| Sau lưng | 1.9000 | 89.89% | 13.52% | 0.000000% | 1 |
| Sau lưng | 1.9500 | 91.89% | 16.69% | 0.000217% | 1 |
| Sau lưng | 1.9667 | 82.99% | 15.63% | 0.000000% | 1 |
| Sau lưng | 2.0500 | 88.58% | 17.91% | 0.000000% | 1 |
| Sau lưng | 2.6000 | 70.30% | 6.95% | 0.000000% | 0 |

- Nêm 0,9 s **61,24% ≥25%**, ROI sau lưng **12,23% ≥8%**. Nền tối theo phiếu khác nền 439d; không dùng chênh lệch % giữa hai báo cáo để chấm mỹ thuật.
- Quầng giữa quạt **102 px**; quầng giữa từng tia **26/68/71/236/220/21/12/94/86/87/157 px**, đều ≥8. Đây là ảnh ghép có hạt/hắt sáng/tia lân cận.
- Tia giữa tách riêng, mặt cắt tại 20/50/85% chiều dài thế giới: **12/17/2 px**, tỷ lệ 85/50 **0,11765≤0,6**. Bản ghép **99/163/2 px**. Giữ cặp [bật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-middle-isolated-on.png) / [tắt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-middle-isolated-off.png).
- Hội tụ 1,9 s camera chơi: quầng/lõi **60/6 px**, đạt ≥24/4; đúng **1** tia HDR. Góc 90°: **45/3 px**, 1 tia HDR; 1,2 s không có tia HDR. Ngưỡng lõi 4 px của 439b áp riêng cho camera chơi.
- Kính camera chơi: bbox chiếu cạnh nhỏ nhất **22,47 px ≥18**, bbox ảnh ở 0,9 s **31×21 px**.
- 10 quái quanh điểm trúng lùi ngay: ở 1,9667 s **0,240–0,458 m**, ở 2,05 s **0,644–1,241 m**. Không đổi lực hoặc thời điểm phản ứng.

## Kiểm kiểu, GPU, âm và phạm vi

`./node_modules/.bin/tsc --noEmit`: **0 lỗi** sau bản cuối. `node --check` script cắt, scenario e và probe: 0 lỗi. Không chạy build hoặc bộ test game theo giới hạn phiếu.

`stress.html`, **87 TargetField +13 walker =100**, kiểm đủ từng lượt; 240 mẫu/lượt, bỏ lượt làm nóng, gộp **720 mẫu**. Cách `total=CPU + chờ GPU qua readPixels` giữ từ 439d; khóa GPU bằng `.local/bin/heavy.sh --perf`, Chrome `--use-angle=metal`.

| Lượt | p95 total | p95 CPU |
| --- | --- | --- |
| Làm nóng | 6.40 ms | 1.90 ms |
| Đo 1 | 5.70 ms | 1.10 ms |
| Đo 2 | 6.00 ms | 1.40 ms |
| Đo 3 | 5.70 ms | 1.20 ms |

**p95 gộp total 5,80 ms≤16,7; CPU 1,30 ms.** Renderer **ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)**. Không exception JS/shader; tài nguyên Quang ready, `loadError=null`. Còn cảnh báo sẵn có về nhiều KTX2Loader và atlas `metal-crescent-sym` không tải được; không sửa làn Kim.

Âm `tt-sfx-ult-light/take1.wav` giữ mixer/gain/bus/reverb gốc: gather **0**, release **0,600**, focus **1,950 s**, khớp khung chạm. Clip có AAC từ mixer lab sẵn có; không tạo hoặc sửa âm. [Log take](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-e-4/441-sound-takes.json). Chưa đánh giá nghe độc lập.

Mã chỉ sửa/thêm trong `games/.wt-ic-lab-all/src/lab/`: `light-ult-fan.ts`, `light-ult-fan-space.ts`, `light-ult-burst.ts`, `light-ult-cut.mjs`, `light-ult-glow-probe.mjs`, `light-ult-review-e.mjs`. Chỉ thêm bộ tài nguyên D, mục thư viện, ABOUT và báo cáo này. Không sửa `skills-main.ts`, mã production hoặc audio-lab. Một lane; quota lúc nhận còn 67%; không gọi tư vấn ngoài vì phiếu đã có phương án và phản biện PASS. Không khởi động/dừng lại server 3148; Chrome do runner tạo đã thoát. Không commit/push/reset/clean/stash; không đưa media vào Git.

Lệnh tái lập từ gốc worktree: `ART_MAGICK=/opt/homebrew/bin/magick node src/lab/light-ult-cut.mjs`; từ repo cha: `ROUND=4 FINAL=1 CHROME_FLAGS='--use-angle=metal' .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review-e.mjs --width=1280 --height=720 --dpr=1`. Scenario tạo ảnh đối chiếu trong captures; sao chép `441-comparison.jpg` sang tên owner `light-ult-codex-e.jpg` sau khi xem.

## Owner cần xem và phần bỏ qua

Owner xem độ lớn/hình lăng kính ở **1,95–2,25 s**, đầu tia tan vào lõi, chân đứng ở mặt đất và đuôi tắt trước **3,30 s**. Ở camera chơi toàn sân, hình D vẫn nhỏ hơn cảm giác cận cảnh của phân cảnh; góc sau lưng nén chiều sâu và người tung che một phần điểm trúng. Tự chấm cuối **7,2**, chưa đủ cơ sở gọi đạt thương mại 8,5; cần hai giám khảo mù ở host chơi trước production. Không sửa camera/model/nền ngoài yêu cầu để đuổi theo ảnh demo.

Không sinh ảnh/âm mới vì đã có nguồn owner duyệt; không chạy build/test suite và không dựng lại index review vì các đường dẫn ghi của index ngoài phạm vi phiếu. Dừng sau 4 vòng đúng giới hạn.

## Dọn ảnh

Chỉ dọn ảnh do phiếu này tạo trong `source-e-441`, `round-e-1..4`, `frames-e-round-2..4`, `video-check-e-4`: dry-run rồi `--apply --min-age-min 0`, giữ sheet, ảnh báo cáo liên kết và JSON. Không đụng 439a/b/c/d hoặc file người khác. Đã xóa **1,223 ảnh thô/trung gian, 1159.475 MB**, giữ **20** ảnh/sheet có ích, từ chối **0** mục. Nhật ký: `captures/tu-tien/light-ult-439/441-prune.log`; kế hoạch và kết quả trong `441-prune-dry.json`, `441-prune-result.json`.
