# Phiếu 385: Ult băng làm bằng lớp, v2 (đạt độ hoành tráng của video cũ)

Phản biện: PASS (Sonnet, 15/11, vòng 2)

## Bối cảnh
Owner 15/11/2026, sau khi xem so sánh `typing-game-review/owner-review/2026-11-15/tu-tien/ult-ice-layered/ice-ult-compare-2x2.mp4`: bản lớp v1 "xấu hơn video rất rất nhiều… video nhiều vật thể băng giá kim cương phụ xung quanh hơn, còn hiện tại chỉ thêm lớp băng quanh quái rồi vài hình bầu dục dưới đất". Video cũ `ult-ice-cold-silence` bị loại vì có tượng thú vẽ sẵn và chỉ đúng một góc camera (`docs/games/tu-tien/source/gemini-video-vfx-approach-2026-11-15.md`).

## Việc
Trong worktree `games/.wt-ic-lab-all`, nâng cấp `src/lab/ice-ult-layered.ts` (v1, nối phím 8 mục 12, phím Y bật bản video cũ) để bản lớp **đẹp ngang hoặc hơn** video cũ ở góc trên và góc sau lưng, mà không có tượng thú hay cảnh vẽ sẵn:
1. **Rừng tinh thể băng khắp sân** (lớp hoành tráng chính): hàng chục cụm tinh thể kim cương mọc lên trên toàn vùng 30 m, dày ở chỗ quái đứng, cao và thấp xen kẽ, mọc lần lượt theo vòng sóng từ người tung chiêu, đứng trong thời gian trói 3 giây rồi vỡ vụn. Dùng **lưới 3D** (hình tinh thể nhiều mặt, vật liệu băng trong suốt: fresnel, khúc xạ giả, cạnh sáng, lõi xanh nhạt), không dùng thẻ phẳng, để đúng ở cả 4 góc nhìn (Alt+1–4).
2. **Mặt băng phủ sân:** một lớp băng trong, có vết nứt, phủ dần mặt đất thật theo vòng sóng, phản chiếu nhẹ, rồi tan.
3. **Không khí lạnh:** sương mù thấp, bông tuyết rơi, hạt lấp lánh trên các cạnh tinh thể (lớp ánh sáng theo luật "skill effects sparkle").
4. **Từng quái thật:** giữ kiểu đóng băng của v1 nhưng làm thành vỏ băng bọc kín mô hình (lưới tinh thể ôm quanh quái), không chỉ là sương phủ.
5. **Điểm nhấn duy nhất:** một khoảnh khắc tinh thể bùng sáng lúc trúng đòn. Các lớp phụ giữ nhạt.
6. Giữ chớp màn, khựng hình và âm thanh băng của v1.

## Ràng buộc
- Tái dùng bộ băng có sẵn `art-src/lab/vfx/ice/` và code v1. Không tạo video. Nếu cần ảnh tĩnh mới (ví dụ texture mặt băng nứt), tối đa 4 ảnh bằng `image_gen`, lấy tham chiếu từ `art-src/lab/vfx/ice/ice-ground-mark.atlas.png`, rồi dừng lại báo trước khi dùng.
- 100 quái (`stress.html`) phải giữ 60 fps trên Mac mini M4; báo số ms trước và sau.
- Không commit, không đưa media vào Git, không đổi nhánh.

## Giao nộp
- Ảnh so sánh v1, v2 và video cũ ở góc trên và góc sau lưng, đặt trong `typing-game-review/owner-review/2026-11-15/tu-tien/ult-ice-layered/v2/`, kèm `ABOUT.md`.
- Báo cáo `docs/codex-queue/385-report.md`: đã làm gì, phím lab, số đo hiệu năng.

## Chuẩn và số nghiệm thu (bổ sung sau phản biện 1)
- Chuẩn: `docs/games/VFX_STANDARD.md`, lớp hành động "ultimate", đủ 5 pha (tụ lực, phát chiêu, lan, trúng, dư âm). Ảnh tham chiếu bố cục: khung giữa của video cũ trong `typing-game-review/captures/tu-tien/clip-content-audit/ult__ult-ice-cold-silence.jpg`, chỉ lấy mật độ tinh thể, không lấy tượng thú.
- Thành phần (thư viện `docs/games/tu-tien/skills/VFX_LIBRARY.md`, ghi thêm các phần mới vào đó): 3–4 biến thể cụm tinh thể 3D, mảnh vỡ, ánh lấp lánh, bông tuyết, sương thấp, mặt băng nứt, vỏ băng bọc quái.
- Số đo:
  - 40–80 cụm tinh thể, cao 1–6 m;
  - vòng sóng đi hết 30 m trong 0,8–1,2 s;
  - tinh thể giữ 3 s rồi vỡ trong 0,4 s;
  - mặt băng tan trong 2,5 s;
  - 100 quái trên `stress.html` giữ ≥ 60 fps với p95 ≤ 16,7 ms (đo bằng `__lab` hoặc công cụ perf hiện có, ghi trước và sau).
- Một điểm nhấn duy nhất là khoảnh khắc tinh thể bùng sáng lúc trúng đòn (lõi HDR 3–6). Rừng tinh thể, mặt băng, sương và lấp lánh giữ nhạt, mỗi kênh ≤ 0,9, không bloom.
- Bản video cũ không xoá: vẫn bật được bằng phím Y, và clip cũ giữ trong thư viện (luật thay thế, không bỏ).
- Âm thanh: mỗi lớp mới có sự kiện âm thanh riêng (tinh thể mọc, băng nứt lan, tinh thể vỡ, gió lạnh), dùng thư viện âm thanh băng có sẵn, có biến thể pitch.
- Owner duyệt trước: dựng xong thì dừng, gửi ảnh chụp lab ở góc trên và góc sau lưng, rồi chờ owner duyệt. Không chấm thay owner.
- Thư mục `v2/` có `ABOUT.md` gồm các dòng purpose, made-by, doc, delete-when; xong chạy `node scripts/review-index.mjs`.
