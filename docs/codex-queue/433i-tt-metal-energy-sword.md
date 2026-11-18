# Phiếu 433i: Kim, kiếm nhỏ là kiếm năng lượng A và vệt D (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11)

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/energy-sword.v1-try1.png, games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png

## Bối cảnh
Ngày 18/11 owner nhắc lại: "chỉ kiếm to là dùng hình, các kiếm con nên dùng dạng năng lượng". Owner đã chọn kiếm năng lượng mẫu **A** (`energy-sword.v1-try1.png`, xem tờ `typing-game-review/owner-review/2026-11-18/tu-tien/energy-sword-446/energy-sword-446.jpg`). Vệt D đã được gắn ở phiếu 433h.

Giữ nguyên như `docs/codex-queue/433h-tt-metal-trail-d.md`:
- luật "chỉ đặt, xoay, thu phóng đều, nhuộm, chỉnh độ mờ";
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa: `games/.wt-ic-lab-all/src/lab/metal-ult-*`, `metal-sword-look.ts`, tài nguyên mới trong `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/`.

Được ghi `docs/codex-queue/433i-report.md` và `ABOUT.md`. Tắt Chrome và xoá profile tạm khi xong.

## Việc
1. **Cắt ảnh A.** Nền đen thành alpha, cộng sáng, giữ nguyên hình. Ghi mũi kiếm và chuôi vào `.json` làm điểm neo.
2. **Mọi kiếm nhỏ** (đang bay và đã cắm đất) bỏ mô hình Tripo, thay bằng một quad ảnh A:
   - trục dài của quad theo hướng rơi; quad quay mặt về camera quanh trục đó;
   - thu phóng đều, chiều cao trên màn hình như kiếm nhỏ hiện tại.
3. **Vệt D** neo ở chuôi của kiếm A, hướng ngược chiều rơi, giữ cách làm của 433h.
4. **Kiếm cắm đất.** Quad A nghiêng theo góc cắm, mũi ngập vào đất khoảng 15 %. Kiếm sáng nhẹ, rồi tan bằng cách giảm độ mờ.
5. **Kiếm lớn giữ mô hình Tripo**, hào quang flipbook và vệt D. Tỷ số sáng kiếm lớn so với kiếm nhỏ ≥ 1,5. Vùng trắng ≤ 6 %.
6. Ngừng dùng lớp emissive và `qi-streak` trên kiếm nhỏ của 433g. Không xoá code, chỉ ngừng gọi.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với ảnh A và bản 433h → sửa.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- In ra: số kiếm nhỏ còn dùng mô hình (phải = 0), tỷ số sáng, vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `metal-rain-i.jpg` và `.mp4` vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm dòng vào `ABOUT.md` của thư mục đó.
- Xoá khung thô. Không commit.
