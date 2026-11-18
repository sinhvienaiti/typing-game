# Phiếu 439 — Tuyệt kỹ Quang từ thấu kính

Ngày 17/11/2026. **Đã chạy đủ vòng sửa → chụp → mở từng ảnh → chấm → sửa, dừng ở vòng 5, tự chấm 7,2/10. Các cổng đo của phiếu đạt; chưa nghiệm thu 8,5 bởi hai giám khảo mù của Claude.**

## Phạm vi và tệp giao

Chỉ viết qua `/Volumes/SS990TPRO/htdocs/typing-game` và thư mục review được phiếu cho phép. Một làn, không gọi trợ lý ngoài, không tạo server hoặc khởi động lại host 3148; Chrome luôn headless, chỉ truy cập localhost. Không build/bộ test game, không cài gói, không đổi nhánh, stage, commit, push hoặc lệnh Git phá hủy. Quota đọc đầu phiếu: còn 85%.

Trong `games/.wt-ic-lab-all/src/lab/`:

- `light-ult-fan.ts`: timeline và recipe các thành phần, hit/recoil, âm theo sự kiện, báo cáo pool/tia.
- `light-ult-fan-space.ts`: mesh tia trong thế giới, shader lõi/viền/nhiễu chảy; kính và viền vàng bám đầu, hai tay giải IK vào giá cầm. Không đổi chiều dài xương.
- `light-ult-review.mjs`: chụp từng pha, đo trắng, ghép sheet, ghi 120 khung/30 fps, trộn âm và đo stress.
- `light-ult-lens-check.mjs`: đo phần kính thật sự nhìn thấy bằng cặp render bật/tắt kính cùng thời điểm và camera.
- `light-ult-camera-check.mjs`: chụp bổ sung 90°, khoảng cách 100 m để toàn bộ quạt nằm trong khung.
- `light-ult-pose-probe.mjs`: kiểm vị trí xương và sai số tay cầm trong Chrome.
- `skills-main.ts`: chỉ thêm import, khởi tạo, nối cast `ult-light`, update/reset và hook `window.__lab.lightUlt()`, theo đường ThunderUltChain; hook nhận `hideLens`/`showLens` chỉ để đo. Giữ nguyên các phần của làn khác.

Giao chủ: [light-ult-codex.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex.jpg) và [light-ult-codex.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex.mp4). Đã thêm một dòng riêng vào `owner-review/2026-11-17/tu-tien/ABOUT.md`.

## Cách dựng

Theo `VFX_STANDARD` và phiếu Sonnet PASS; dùng `game-vfx-production`, `game-vfx-layered`, `game-character-animation`, `agent-orchestration`. Đã mở phân cảnh `light-storyboard.v1-try1.png`, đọc prompt, dòng Quang của `ULT_CHOREOGRAPHY.md`, xem `ult-light-moment-a.v1-try1.png` và `ult-light-components.v1-try2.png`. Không gửi ảnh tham chiếu cho công cụ ngoài.

Tái dùng `light-charge`, `light-release`, `light-sparkle`, `gold-dust-motes-loop-w2`, `light-impact`, `light-big-burst` trong thư viện Quang. Không tạo media mới; mesh/shader tia và kính là phương án phiếu yêu cầu rõ ràng.

| Pha | Hành vi cuối |
|---|---|
| 0–0,6 s | Nâng kính đường kính 0,64 m, viền kim loại vàng/kính trong; mặt kính gần đứng, nghiêng 17°, gắn theo đầu. Hai tay nắm phần giá vàng bên dưới; charge và glints cục bộ. |
| 0,6–1,6 s | 13 dải tia mảnh từ một đỉnh ở kính, góc 60°, lõi trắng/viền hổ phách/nhiễu trượt. Hai mặt dải cắt nhau trong thế giới giúp thấy ở camera chơi, sau lưng và trên thẳng; không dựng theo trục màn hình. Nhịp sáng quét trái → phải, giữ bóng tia mờ. |
| 1,6–2,3 s | Từ 1,8 s, đúng một dải có lõi HDR hội tụ vào một quái bên phải; burst, glints lăng kính và recoil. Tia quạt trước đó chỉ còn bóng mờ ≤0,9/kênh. |
| 2,3–3,6 s | Hạt vàng trong vùng nêm tan dần, kính hạ và giảm sáng. Hết 3,6 s trả pool về 0. |

Các lớp phụ có tint/cường độ ≤0,9; riêng lõi hội tụ có uniform HDR 4,4. Không dựng vòng đất, trận pháp, cột trời hoặc đĩa nằm ngang. Nhóm hiện diện nền của lab và vũ khí cầm tay được ẩn trong lúc Quang chạy, trả lại sau khi hết/hủy chiêu.

Âm duy nhất là `tt-sfx-ult-light/take1.wav` có sẵn, cắt ba cửa sổ gather/release/focus; log của clip xác nhận sự kiện ở 0,000 / 0,600 / 1,800 s. Bộ trộn dùng `tsx` có sẵn để đọc import TypeScript, giữ bus/gain/pan/reverb theo log runtime. MP4 có H.264 1280×720, **120 khung, 30 fps, 4,000 s**, AAC 4,000 s; đã kiểm ffprobe và [sheet giải mã từ clip](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/439-video-check.jpg). Chưa có đánh giá nghe độc lập.

## Các vòng tự nhìn và sửa

Mỗi vòng đều chụp 0,3 / 0,9 / 1,6 / 1,9 / 2,6 s tại camera chơi và sau lưng, mở **từng ảnh**, ghép/xem cạnh phân cảnh rồi mới quyết định sửa. Vòng cuối mở thêm hai khung 90°. Điểm là tự chấm theo phân cảnh, không thay hai giám khảo mù.

| Vòng | Điểm | Lỗi nhìn thấy và hướng sửa | Bằng chứng giữ lại |
|---|---|---|---|
| 1 | 5,5/10 | Tia đứt nét do lõi dưới một pixel; charge/dư âm quá nhỏ; banner và vòng hiện diện nền lọt khung. | [So phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-1/439-comparison.jpg) · [5 khung chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-1/439-top-phases.jpg) · [5 khung sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-1/439-behind-phases.jpg) |
| 2 | 6,3/10 | Tia và hạt đã rõ, banner/vòng nền được ẩn; tay còn cách kính khoảng 0,6 m, hạt xa tràn ra trên sân. | [So phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-2/439-comparison.jpg) · [5 khung chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-2/439-top-phases.jpg) · [5 khung sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-2/439-behind-phases.jpg) |
| 3 | 6,8/10 | Sửa đúng phía trái/phải của rig, điểm cầm xuống dưới kính; sai số còn 6–15 mm ở mốc 0,3 s. Tia/hạt gọn hơn nhưng kính bị đầu Lam che, cú cuối ít tia lửa. | [So phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-3/439-comparison.jpg) · [5 khung chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-3/439-top-phases.jpg) · [5 khung sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-3/439-behind-phases.jpg) |
| 4 | 7,1/10 | Thêm giá cầm vàng ngắn để kính cao hơn đầu, ẩn vũ khí; thêm burst/lửa lăng kính và bóng tia cũ. Probe ảnh bật/tắt phát hiện chiều cao nhìn thấy chỉ 11 px ở vài khung: chưa đạt cổng bbox theo cách hiểu cả hai chiều. | [So phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-4/439-comparison.jpg) · [5 khung chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-4/439-top-phases.jpg) · [5 khung sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-4/439-behind-phases.jpg) |
| 5 | 7,2/10 | Nghiêng kính 17° so với phương đứng, tính điểm nắm theo cùng phép xoay; bbox nhìn thấy tối thiểu 20 × 12 px. Dừng sau khi mở từng khung và xem sheet. Nhìn sau lưng vẫn nén hình quạt theo phối cảnh thật. | [So phân cảnh](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-5/439-comparison.jpg) · [5 khung chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-5/439-top-phases.jpg) · [5 khung sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-5/439-behind-phases.jpg) |

Vòng 3 tạo đủ ảnh và clip im lặng nhưng runner dừng ở bước trộn âm: Node không giải được import extensionless `foe-levels` từ `sound-tiers.ts`. Bbox/HDR vòng này chưa kịp ghi JSON; không bịa số còn thiếu. Đã khôi phục trắng từ PNG gốc vào `round-3/439-white-recovered.json`; vòng 4–5 đo lại đầy đủ. Runner nay lưu checkpoint trước bước clip và gọi bộ trộn qua `tsx`.

## Số đo mỗi khung cuối

`q=high`, DPR 1, viewport 1280×720. Trắng là tỷ lệ pixel có **cả R/G/B ≥0,95**, đo trên PNG chụp thật. Bbox hình học được chiếu từ kính; bbox nhìn thấy đo từ hai render cùng camera/thời gian, chỉ bật/tắt kính/giá cầm, lấy chênh lệch gray >3%. Bbox chênh lệch bao gồm vành, kính, giá cầm và bloom do chúng tạo; không tính charge/glints riêng.

| Camera | Giây | Trắng (%) | Bbox kính chiếu (px) | Bbox nhìn thấy (px) | Tia HDR |
|---|---|---|---|---|---|
| Chơi / Alt+1 | 0.3 | 0.000000 | 20.67 × 15.01 | 20 × 12 | 0 |
| Chơi / Alt+1 | 0.9 | 0.000000 | 20.64 × 15.04 | 21 × 13 | 0 |
| Chơi / Alt+1 | 1.6 | 0.000000 | 20.68 × 15.02 | 20 × 13 | 0 |
| Chơi / Alt+1 | 1.9 | 0.009657 | 20.68 × 15.02 | 20 × 13 | 1 |
| Chơi / Alt+1 | 2.6 | 0.000000 | 20.65 × 14.98 | 20 × 12 | 0 |
| Sau lưng / Alt+2 | 0.3 | 0.000000 | 74.80 × 72.97 | 75 × 55 | 0 |
| Sau lưng / Alt+2 | 0.9 | 0.000000 | 72.69 × 70.73 | 77 × 63 | 0 |
| Sau lưng / Alt+2 | 1.6 | 0.000000 | 74.78 × 72.88 | 81 × 56 | 0 |
| Sau lưng / Alt+2 | 1.9 | 0.019857 | 74.75 × 72.86 | 78 × 55 | 1 |
| Sau lưng / Alt+2 | 2.6 | 0.000000 | 74.83 × 73.17 | 75 × 55 | 0 |
| Trên thẳng 90° | 1.2 | 0.000000 | 9.97 × 2.93 | — (cổng chỉ yêu cầu camera chơi) | 0 |
| Trên thẳng 90° | 1.9 | 0.004340 | 9.97 × 2.93 | — (cổng chỉ yêu cầu camera chơi) | 1 |

**Trắng tối đa 0.019857% ≤6%; kính chơi nhỏ nhất 20×12 px; đúng một tia HDR ở 1,9 s tại cả ba góc.** Đếm HDR bằng probe các mesh tia đang hiện và uniform >1, không suy từ số vệt trắng trong ảnh. [Sheet 90°](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-5/439-overhead-phases.jpg) giữ trọn hình quạt; kính nhìn cạnh ở góc này là phối cảnh thật.

Số liệu gốc: [439-measure.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/round-5/439-measure.json), [439-lens-visibility.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/light-ult-439/439-lens-visibility.json). Các vòng 1/2/4 còn JSON riêng; dữ liệu vòng 3 thiếu probe như nêu trên.

## p95 thật trong Chrome

Host `http://localhost:3148/stress.html`, Chrome headless với `--use-angle=metal --enable-gpu`. Renderer WebGL: **`ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`**, GPU thật, không phải SwiftShader.

Dùng nguyên `window.__lab.perf(1)` như `metal-ult-rain-review.mjs`: `total` từ đầu `frame(dt)` tới sau `gl.readPixels(0,0,1,1,...)`, tức CPU + chờ GPU, không phải rAF. Kiểm đủ **87 TargetField còn sống + 13 walker = 100** ở đầu từng lượt, kích lại `ult-light`; 240 khung/lượt. Một lượt làm nóng, ba lượt đo = 720 mẫu.

| Lượt | Quái đầu lượt | Số mẫu | p95 total (ms) | p95 CPU (ms) | Live cuối |
|---|---|---|---|---|---|
| 1 (làm nóng) | 87 + 13 = 100 | 240 | 5.70 | 1.50 | 0 |
| 2 | 87 + 13 = 100 | 240 | 5.60 | 1.40 | 0 |
| 3 | 87 + 13 = 100 | 240 | 5.80 | 1.50 | 0 |
| 4 | 87 + 13 = 100 | 240 | 5.30 | 1.10 | 0 |

**Gộp ba lượt đo: p95 total 5.60 ms ≤16,7 ms; p95 CPU 1.40 ms.** Tất cả lượt hết chiêu `active=false`, `live=0`. Cảnh nền có tải decor và walker thật; không thay bằng fixture CPU.

Kiểm kiểu nguyên `tsconfig.json` bằng `tsc --noEmit`: **0 lỗi**. Scenario JS kiểm cú pháp riêng; không chạy build hoặc bộ test game. Không có exception JS/shader trong các lượt cuối. Log còn cảnh báo loader KTX2 và lỗi tải atlas Metal `metal-crescent-sym` (một số lượt có `metal-slash-arc`) từ lab hiện có; atlas Quang sẵn sàng, `loadError=null`. Không sửa cảnh báo của làn khác.

## Còn lệch và việc để Claude/chủ xem

- Nhân vật lab hiện tại là Lam đầu lớn, tay ngắn; thao tác nắm giá dưới kính còn kém rõ và kém thanh thoát so với người áo trắng giơ hai tay trong phân cảnh. Thêm giá cầm ngắn là khác biệt có chủ ý để kính cao hơn đầu mà giữ chiều dài xương; không đổi model/animation dùng chung ngoài phạm vi phiếu.
- Tia còn thẳng và đều hơn tranh; recoil của đàn quái, chiều sâu kính và hào quang cục bộ chưa đạt mức mỹ thuật 8,5. Nhìn sau lưng ở độ cao mắt nén quạt theo phối cảnh, mặc dù cùng mesh thế giới và góc 60° vẫn đúng ở ảnh 90°.
- Tự chấm 7,2 chỉ dừng vòng lặp. **Claude cần hai giám khảo mù ≥8,5 trước khi nhận hình/âm hoặc đưa vào game.**
- Không tạo ảnh/âm mới, không sửa production `games/immortality-cultivation/src`, tài liệu Tu Tiên, `showcase.ts`, hạ tầng hay công cụ âm thanh. Không dựng lại index review vì các tệp index nằm ngoài whitelist ghi của phiếu này.

Khung thô của riêng phiếu được dọn bằng `node tools/capture-prune/prune.mjs ... --min-age-min 0` sau lượt xem trước, rồi `--apply`; giữ sheet có liên kết ở báo cáo, JSON và clip cần đối chiếu. Đã xóa 446 ảnh thô/trung gian, giải phóng 509,806 MB; giữ 17 sheet có liên kết. Nhật ký dọn ở `captures/tu-tien/light-ult-439/439-prune.log`.

## Chạy lại

Từ gốc repo, giữ server 3148 đang chạy:

```sh
ROUND=6 FINAL=1 CHROME_FLAGS='--use-angle=metal --enable-gpu --disable-background-networking' node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-review.mjs --width=1280 --height=720 --dpr=1
CHROME_FLAGS='--use-angle=metal --enable-gpu --disable-background-networking' node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/light-ult-lens-check.mjs --width=1280 --height=720 --dpr=1
```

Lượt chạy lại tạo thư mục vòng riêng và MP4 ở tên giao đã chỉ định. Nếu đổi vòng cuối, copy sheet `439-comparison.jpg` của vòng đó sang tên JPG giao chủ; scenario kính chỉ đo, không thay đổi timeline giữa hai ảnh.
