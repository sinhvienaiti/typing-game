# Lửa phím 1 có mặt nạ vào lab (rồi vào bản chơi)

**Mục tiêu:** đòn lửa phím 1 dùng clip Firefly lượt 2 với mặt nạ A/B (hiện từ gốc, giữ đỉnh, cháy rụi dần, than đỏ), thay hoa sen cũ.
**Cách đã chốt:**
- 273/273b: atlas RGBA, maskA (thứ tự sống sót theo hạng), maskB.
- 274/274b: `rampCool` giữ than ở dải son.
- 264: nối vào `element-fire.ts impact()`, sau cờ `?impact=brush|lotus` (mặc định brush).

(DECISIONS: 04/11 ~14:50, 19:40, ~22:00)
**Nghiệm thu:** khung đầu ≥ 95 % đỉnh; trắng xóa ≤ 6 %; thân sáng ≤ 15 % ở tuổi 18; Hỏa hơn Kim ≤ 0,85 ms; video.
**Phiếu:**
- `docs/codex-queue/273*`, `274*`, `264-tt-key1-brush-impact.md`.
- Tấm xem: `typing-game-review/captures/tu-tien/impact-k1-r2/masks/`.

## Nhật ký
- 04/11 21:13 · Codex · 273 xong (dừng một lần vì đặc tả mâu thuẫn, Claude chốt, chạy lại).
- 04/11 21:24 · Codex · 273b xong; nhịp cháy theo lịch (0,68 / 0,19 / 0,05 / 0).
- 04/11 ~22:00 · anh · duyệt.
- 04/11 23:31 · Codex · 274 xong: mã đạt, nhưng than chìm xuống muội (công thức của Claude sai).
- 04/11 23:35 · Claude · phiếu 274b (trần r về 0,40); Codex hết hạn mức tới 00:52, chạy lúc 00:54.
- 05/11 00:20 · Claude · 264 viết xong (phiếu dài, trước luật làm gọn), chạy sau 275 khi có `264/READY` (sau khi gộp 274).
