# Phiếu 439: Tuyệt kỹ Quang (tia quạt từ thấu kính), Codex tự nhìn và lặp

Phản biện: PASS (Sonnet, 17/11, vòng 3)

## Vì sao phiếu này khác
Ngày 17/11 owner cho phép chạy phiếu này ở chế độ **full-access**, để Codex tự mở Chrome headless và chụp lab giống Claude. Câu trả lời của owner: "Cho full-access". Đây là phép thử: so với agent Claude đang làm Kim/Lôi bằng mắt. Vì vậy phiếu này **bắt buộc vòng lặp sửa → chụp → xem ảnh → chấm → sửa**. Chưa xem ảnh tự chụp thì không được báo xong.

Giới hạn quyền (bắt buộc):
- Chỉ sửa file trong `games/.wt-ic-lab-all/src/lab/` có tiền tố `light-ult-`; được sửa `skills-main.ts` chỉ để thêm import, khởi tạo và hook `window.__lab` cho `light-ult-*`, theo đúng mẫu `ThunderUltChain` (dòng 129 và ~1396), kích khi chạy `ult-light`; không sửa phần khác của `skills-main.ts` hay `showcase.ts`.
- Được ghi `docs/codex-queue/439-report.md`.
- Chỉ ghi ảnh vào `typing-game-review/captures/tu-tien/light-ult-439/` và `owner-review/2026-11-17/tu-tien/`.
- Được chạy ffmpeg để ghép clip, và `node tools/capture-prune/prune.mjs` từ gốc repo. Chrome chỉ chạy headless. Không mở Blender, không cài gói, không đụng mạng ngoài localhost.
- Không dừng hoặc khởi động lại server lab đang chạy ở http://localhost:3148.
- Không commit, không đổi nhánh, không xoá file không phải của mình.

## Đích
Phân cảnh: `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png` (2×2, đọc theo thứ tự trên trái, trên phải, dưới trái, dưới phải). Prompt ở file `.prompt.txt` cùng tên. Dòng Quang trong `docs/games/tu-tien/ULT_CHOREOGRAPHY.md`.
1. **Tụ lực (0–0,6 s):** người tung giơ thấu kính tròn nhỏ (đường kính ~0,5 m, viền vàng) bằng hai tay, ngay trên và trước đầu, mặt kính hướng về đám quái (đứng, không nằm ngang), ánh sáng ấm tụ trong thấu kính.
2. **Phóng và bay (0,6–1,6 s):** từ một đỉnh sát người tung, nhiều tia vàng trắng mảnh xòe thành hình quạt về phía đám quái, cao ngang ngực quái, quét từ trái sang phải để lại bóng mờ.
3. **Va chạm (1,6–2,3 s):** cuối đợt quét, thấu kính hội tụ thành **một** tia trắng hẹp, rất sáng, bắn chéo ra trước vào một quái bên phải. Tia lửa lăng kính và quái giật lùi dọc vùng quạt đã quét. Đây là **điểm nhấn duy nhất**.
4. **Dư âm (2,3–3,6 s):** hạt sáng vàng lơ lửng dọc vùng hình nêm (góc quạt ~60°) đã quét rồi tan. Thấu kính còn sáng nhẹ.

Cấm (theo owner): vòng tròn dưới đất, vòng phép, cột sáng thẳng đứng từ trời, đĩa nằm ngang lơ lửng trên trời. Thấu kính cầm tay ở mục 1 thì được.

## Vật liệu
- **Flipbook có sẵn trong `games/.wt-ic-lab-all/art-src/lab/vfx/light/`:** `light-charge`, `light-big-burst`, `gold-dust-motes-loop-w2`, `light-column-*` (chỉ dùng làm chất liệu tia, không dựng thành cột đứng), cùng những file khác trong thư mục.
- **Tham chiếu màu và chất liệu:** `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png` và `ult-light-components.v1-try2.png`.
- **Tia:** dải mesh 3D trong không gian thế giới, có shader chất liệu (lõi trắng mảnh, viền hổ phách, nhiễu chảy), không vẽ cố định theo màn hình.
- **Thấu kính:** mesh nhỏ với vật liệu kính và viền kim loại vàng, theo vị trí ở mục 1, bám xương đầu/tay người tung.
- Không vẽ hình bằng canvas/SVG.

## Luật hình (owner)
- Kênh lớp phụ ≤ 0,9, chỉ tia hội tụ cuối được sáng HDR. Vùng trắng toàn khung ≤ 6 %.
- Nhìn đúng ở camera chơi, góc trên (phím 1 hoặc Alt+1) và góc sau lưng (phím 2 hoặc Alt+2), không bị lệch phối cảnh.
- Mỗi pha có lớp lấp lánh (hạt, vành sáng mảnh) quanh hình chính.
- Âm thanh dùng `tt-sfx-ult-light` có sẵn, khớp khung phóng và khung hội tụ.

## Vòng lặp (bắt buộc, tối đa 8 vòng, dừng sớm khi đạt ≥ 7/10)
Mỗi vòng:
1. Sửa code.
2. Chụp bằng Chrome headless vào lab đang chạy (`http://localhost:3148/skills-lab.html`, ẩn banner tiêu đề DOM) ở 0,3 / 0,9 / 1,6 / 1,9 / 2,6 s, ở camera chơi (Alt+1) và góc sau lưng (Alt+2). Vòng cuối chụp thêm góc nhìn thẳng từ trên (90°, đặt camera bằng hook như probe trong `metal-ult-camera-check.mjs`) ở 1,2 và 1,9 s.
3. **Mở xem từng ảnh** và ghép cạnh phân cảnh thành một sheet.
4. Chấm 1–10 theo phân cảnh, ghi lỗi nhìn thấy cụ thể, rồi sửa đúng lỗi đó ở vòng sau.

Ghi bảng điểm từng vòng vào báo cáo. Kịch bản mẫu để học cách chụp: `src/lab/metal-ult-rain-review.mjs`, `thunder-ult-chain-capture.mjs`.

## Nghiệm thu
- Mục tiêu tự chấm ≥ 7/10 chỉ là điều kiện dừng vòng lặp; nghiệm thu thật 8,5 do hai giám khảo mù của Claude chấm sau. Kèm số đo mỗi khung chụp: % điểm ảnh trắng (≥ 0,95 cả 3 kênh) ≤ 6 %; thấu kính thấy được ở camera chơi (bbox ≥ 12 px); khung 1,9 s có đúng một tia HDR (đếm bằng probe).
- p95: dùng y nguyên cách của `metal-ult-rain-review.mjs` (100 quái = 87 TargetField + 13 walker, kiểm đủ 100, kích chiêu lặp, số `total` = CPU + chờ GPU qua readPixels, p95 của `total` ≤ 16,7 ms). Ghi renderer WebGL vào báo cáo; nếu là renderer phần mềm (SwiftShader) thì chạy lại Chrome với `--use-angle=metal` hoặc `--enable-gpu`, vẫn phần mềm thì ghi rõ và để Claude đo.
- Clip 4 s quay 0–4 s sau khi kích chiêu, 30 fps.
- Kiểm kiểu 0 lỗi.
- p95 trên `stress.html` với 100 quái ≤ 16,7 ms (đo thật trong Chrome).
- Giao nộp:
  - `owner-review/2026-11-17/tu-tien/light-ult-codex.jpg` (phân cảnh cạnh khung cuối, camera chơi và góc sau lưng);
  - `light-ult-codex.mp4` (4 s, camera chơi);
  - thêm một dòng vào `ABOUT.md`.
- Xoá khung thô của mình bằng `node tools/capture-prune/prune.mjs <thư mục> --apply`.

## Giao nộp
Báo cáo `docs/codex-queue/439-report.md`, gồm:
- bảng điểm theo vòng;
- những gì đã sửa;
- chỗ còn lệch so với phân cảnh;
- p95.
