# Phiếu 433h: Kim, gắn vệt sáng kiếm D thay vệt crop-blur (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11)

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png

## Bối cảnh
Ngày 18/11 owner chọn vệt sáng mẫu **D** của phiếu 444: lõi mảnh, đuôi thành chuỗi hạt sáng thưa dần. Tờ ghép ở `typing-game-review/owner-review/2026-11-17/tu-tien/sword-trail-444/sword-trail-444.jpg`.

Phiếu này thay lớp K5 trong `docs/work/tasks/vfx-code-drawn-audit.md`. K5 hiện là vệt kiếm rơi làm bằng cách crop ảnh lưỡi kiếm, làm mờ rồi kéo giãn. Theo owner, cách này tính là vẽ bằng code.

**Chỉ chạy sau khi phiếu 433g xong**, vì hai phiếu sửa chung file.

Giữ nguyên các mục sau của `docs/codex-queue/433g-tt-metal-replace-code-vfx.md`: luật "chỉ đặt, xoay, thu phóng đều, nhuộm màu, chỉnh độ mờ", quyền chạy, server 3148, ffmpeg, prune, phạm vi sửa (`games/.wt-ic-lab-all/src/lab/metal-ult-*`, `metal-sword-look.ts`) và cách đo.

Được ghi:
- atlas hoặc texture mới vào `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/`;
- `docs/codex-queue/433h-report.md`;
- `ABOUT.md`.

Khi xong, tắt Chrome và xoá thư mục profile tạm.

## Việc
1. Cắt ảnh D: nền đen thành alpha, cộng sáng, giữ nguyên hình. Ghi vào `.json` vị trí đầu vệt (khoảng 85 % chiều cao ảnh) làm điểm neo.
2. Mỗi kiếm nhỏ có một quad vệt D. Đầu vệt neo đúng mũi chuôi kiếm, vệt hướng ngược chiều rơi.
   - Quad quay mặt về camera quanh trục rơi.
   - Thu phóng **đều**: độ dài vệt tỉ lệ với tốc độ rơi, nhưng chiều ngang thay đổi theo đúng tỉ lệ gốc của ảnh. Không kéo giãn một chiều.
   - Độ dài vệt trên màn hình bằng khoảng 0,8–1,4 lần thân kiếm.
3. Khi kiếm cắm đất, vệt mờ dần trong 0,15–0,25 s.
4. Bỏ lớp K5 cũ (crop-blur). Không xoá code, chỉ ngừng dùng.
5. Kiếm lớn dùng cùng vệt D, cỡ to hơn theo tỉ lệ đều.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với ảnh D và với bản 433g → sửa tiếp.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- In ra: bề ngang vệt trên màn hình so với thân kiếm, vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `metal-rain-h.jpg` và `metal-rain-h.mp4` mới (giữ file cũ), thêm dòng vào `ABOUT.md`.
- Xoá khung thô của mình. Không commit.
