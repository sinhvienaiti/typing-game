# Phiếu 439b: Quang, tia quạt phải rực rỡ như phân cảnh (chạy full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 4)

## Bối cảnh
Phiếu 439 tự chấm 7,2. Claude xem `typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex.jpg` và chấm khoảng 4.

Lỗi ở camera chơi, so với phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`:
- tia quạt chỉ là các nét trắng mảnh 1–2 px;
- tia không có quầng vàng hổ phách, không có lớp hạt lấp lánh dày dọc tia;
- tia hội tụ là một vạch trắng mảnh, không có quầng sáng hay tia lửa lăng kính lớn ở điểm trúng;
- nhìn từ sau lưng gần như không thấy quạt.

Kết luận: tự chấm của 439 dễ hơn thực tế.

Owner cho phép chạy full-access để tự chụp (17/11, "Cho full-access"). Giới hạn quyền, ffmpeg, prune, mẫu móc vào `skills-main.ts` và cách đo p95 giữ nguyên như `docs/codex-queue/439-tt-light-ult-eyes-loop.md`. Chỉ sửa `src/lab/light-ult-*`. Không dừng hay khởi động lại server lab 3148.

## Việc (worktree `games/.wt-ic-lab-all`)
1. **Tia quạt.** Mỗi tia gồm:
   - lõi trắng ấm mảnh;
   - quầng hổ phách rộng 6–10 lần lõi, kênh ≤ 0,9, mờ dần ra mép;
   - nhiễu chảy dọc tia;
   - 20–40 hạt vàng lấp lánh trôi dọc mỗi tia.

   Ở camera chơi 1280×720, quầng mỗi tia rộng ≥ 8 px tại giữa tia.
2. **Tia hội tụ.** Đây là điểm nhấn duy nhất:
   - lõi HDR dày ≥ 4 px, quầng vàng ≥ 24 px;
   - ở điểm trúng: flipbook `light-big-burst`, tia lửa lăng kính; không thêm vòng hay đĩa dưới đất (luật cấm của 439).
3. **Ánh sáng hắt.** Vùng quạt rọi sáng ấm lên mặt đất theo hình nêm (decal hoặc đèn), để quạt đọc được cả ở góc sau lưng.
4. **Dư âm.** Hạt vàng `gold-dust-motes-loop-w2` lơ lửng dày hơn dọc vùng nêm, tan dần.

## Đo bắt buộc (không chỉ tự chấm)
Mỗi khung chụp ghi các số sau:
- **Độ phủ sáng:** chỉ đo ở camera chơi (Alt+1) 1280×720. Hình nêm = đa giác màn hình chiếu từ 3 điểm thế giới (đỉnh quạt ở thấu kính, hai mút xa nhất của tia ngoài cùng) lấy từ hook của `light-ult-fan.ts`. Khung nền = cùng thời điểm, cùng camera, chiêu tắt (`hideLight`/không kích). % điểm ảnh trong nêm có độ sáng (Rec.709) tăng ≥ 0,15. Đích ở 0,9 s: ≥ 18 %.
- **Vùng trắng:** % trắng toàn khung ≤ 6 %.
- **Bề rộng quầng:** viết probe `light-ult-glow-probe.mjs`: cắt ngang tia giữa ở trung điểm (tia giữa = từ đỉnh quạt tới trung điểm hai mút tia ngoài cùng), đếm px có độ sáng tăng ≥ 0,1 so khung nền. Probe chạy ở 0,9 s cho tia quạt giữa và ở 1,9 s cho tia hội tụ (thêm vào hook của `light-ult-fan.ts` hai điểm thế giới đầu–cuối của tia hội tụ, chiếu ra màn hình; cắt vuông góc tại trung điểm của đoạn chiếu đó. Quầng = px có độ sáng tăng ≥ 0,1, đích ≥ 24 px; lõi = px có độ sáng Rec.709 tuyệt đối ≥ 0,95, đích ≥ 4 px). Các ngưỡng px ở mục 1–2 chỉ áp cho camera chơi 1280×720; góc sau lưng chỉ cần quạt thấy được (ở 0,9 s, độ phủ ≥ 8 % trong hình chữ nhật giữa khung rộng 60 % và cao 40 % chiều khung, cùng định nghĩa độ sáng tăng ≥ 0,15 so khung nền).

Vòng lặp sửa → chụp → mở ảnh → so phân cảnh → sửa, tối đa 6 vòng. Ghi bảng điểm, có cả số đo.

## Nghiệm thu
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms.
- Giữ nguyên `light-ult-codex.jpg/.mp4` cũ; lưu bản mới `light-ult-codex-b.jpg` và `.mp4` trong `owner-review/2026-11-17/tu-tien/`, thêm dòng vào `ABOUT.md`.
- Xoá khung thô của mình.
- Không commit.

## Giao nộp
`docs/codex-queue/439b-report.md`.
