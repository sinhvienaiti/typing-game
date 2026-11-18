# Phiếu 441b: Quang, cú nổ D to gấp nhiều lần (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11)

## Bối cảnh
Đây là bản sau 441 (`typing-game-review/owner-review/2026-11-17/tu-tien/light-ult-codex-e.jpg`). Owner ngày 17/11 nhận xét: "nổ to hơn rất nhiều, chứ nổ hiện tại quá bé, vụ nổ đáng lẽ phải to gấp 10 20 lần mới đúng, còn tia thì không cần ngắn lại".

Giữ nguyên như `docs/codex-queue/441-tt-light-prism-burst-wire.md`:
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa (`games/.wt-ic-lab-all/src/lab/light-ult-*`) và các file được ghi;
- cách đo.

Được ghi `docs/codex-queue/441b-report.md`.

## Việc
1. **Phóng cú nổ D lên gấp 10–20 lần diện tích màn hình so với 441.**
   - Ở camera chơi 1280×720, khung nổ phải phủ ≥ 45 % bề rộng khung và ≥ 35 % chiều cao khung.
   - Cú nổ trùm phần lớn đàn quái quanh điểm trúng.
   - Neo đáy vẫn đặt ở điểm trúng trên mặt đất.
   - Nếu flipbook bị mờ khi phóng to, dùng atlas độ phân giải cao hơn cắt lại từ chính video D (`light-ult-cut.mjs`).
2. **Cú nổ to phải đi kèm lực tương xứng:**
   - Lóe 2 khung, vùng trắng toàn khung ≤ 6 %.
   - Ánh sáng ấm rọi rộng lên đất và quái trong vùng nổ (decal hoặc đèn mềm, không vòng hay đĩa).
   - Tia lửa lăng kính bắn xa hơn, số lượng gấp 2–3 lần.
   - Quái trong vùng nổ giật lùi và lóe viền.
   - Rung camera mạnh hơn bằng `UltCameraPunch` (chỉ import, không sửa).
   - Âm thanh `tt-sfx-ult-light` khớp đúng khung nổ.
3. **Tia hội tụ giữ nguyên độ dài như 441** (owner: không cần ngắn lại). Đầu tia vẫn chìm vào lõi nổ.
4. **Góc sau lưng:** cú nổ bùng cao, không che kín toàn khung quá 0,3 s.

## Vòng lặp và đo
- Tối đa 4 vòng: sửa → chụp → mở ảnh → so phân cảnh và nhận xét owner → sửa.
- Chụp ở camera chơi và góc sau lưng, nền `?ground=%23353a40`.
- In ra:
  - % bề rộng và % chiều cao màn hình mà cú nổ phủ ở khung nổ (bbox các điểm có độ sáng tăng ≥ 0,15 so khung nền);
  - vùng trắng;
  - p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `light-ult-codex-f.jpg` và `.mp4` mới, giữ file cũ, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.

## Giao nộp
`docs/codex-queue/441b-report.md`.
