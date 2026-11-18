# Phiếu 434j: Lôi, sét lan rộng hơn và 6–7 cột sét giật xuống (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Bản trước là 434i (`typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-i.jpg`). Trong bản đó sét lan đủ 3 tầng (4/8/16 tia) nhưng chỉ gom quanh một cụm quái. Cột sét lớn chỉ là 1–2 luồng đánh liên tục vào một chỗ.

Owner nói ngày 17/11: "tại sao không để lôi điện ra rộng hơn, tại sao chỉ có 2 luồng sét đánh mãi mà không phải 6 7 luồng giật xuống?"

Giữ nguyên theo `docs/codex-queue/434i-tt-thunder-fork-long-strike.md`:
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`games/.wt-ic-lab-all/src/lab/thunder-ult-*`, `cloud-volume*`, tài nguyên trong `art-src/lab/vfx/thunder/`);
- cách gọi hook quái và âm thanh;
- mốc thời gian lớn: sét lan 0,6–2,4 s, pha cột sét 2,4–6,0 s, tổng 7 s.

Được ghi `docs/codex-queue/434j-report.md` và `ABOUT.md`. Khi xong phải tắt Chrome và xoá profile tạm.

## Việc
1. **Sét lan rộng hơn.**
   - Tâm lan bắt đầu từ quái gần người tung chiêu nhất, rồi lan ra cả đàn.
   - Bán kính tìm quái mỗi tầng 9–11 m, lan 3–4 tầng.
   - Ở camera chơi, vùng có sét lan phủ ≥ 60 % bề ngang khung, không chỉ một cụm giữa.
   - Vẫn giữ ≤ 24 tia sáng cùng lúc và góc giữa các tia ≥ 40 °.
2. **6–7 cột sét giật xuống thay cho 1 cột đánh mãi.**
   - Trong pha 2,4–6,0 s có 6–7 cột sét Ngũ Lôi đánh xuống tại 6–7 điểm khác nhau, rải khắp vùng quái. Hai điểm cách nhau ≥ 5 m, ưu tiên cụm đông.
   - Các cột đánh so le và chồng nhau: mỗi cột sống 0,5–0,9 s, cùng lúc có 2–4 cột.
   - Mỗi cột vẫn giật và đổi hình nhanh (0,06–0,12 s), có nổ chân, sét bò đất và vết nứt cháy riêng.
   - Cột cuối cùng to nhất, đánh vào cụm đông nhất. Đó là điểm nhấn duy nhất.
   - Âm thanh: mỗi cột một tiếng sét, lệch nhẹ cao độ và thời điểm bắt đầu.
3. **Giữ:** mây ở dải trên khung, vùng trắng ≤ 6 % ở mọi khung, tổng 7 s.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với phân cảnh và nhận xét của owner → sửa.
- Chụp ở các mốc 1,2 / 2,0 / 3,0 / 4,2 / 5,5 / 6,5 s, camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra:
  - % bề ngang vùng sét lan;
  - số tầng, số tia cùng lúc, góc nhỏ nhất;
  - số cột đã đánh, số cột cùng lúc lớn nhất, khoảng cách nhỏ nhất giữa hai điểm đánh;
  - vùng trắng lớn nhất;
  - p95 trong pha cột sét.

## Nghiệm thu
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms.
- Lưu `thunder-codex-j.jpg` và một clip `.mp4` dài 7 s (giữ file cũ), thêm một dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
