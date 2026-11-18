# Phiếu 433j: Kim, kiếm nhỏ to hơn và trận pháp lùi lại (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 18/11, vòng 2)

Nguồn hình: games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/energy-sword.v1-try1.png, games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/sword-trail.v1-try4.png

## Bối cảnh
Bản 433i (`typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-i.jpg`) có hai lỗi:
- ở camera chơi, kiếm nhỏ (ảnh kiếm năng lượng A cùng vệt D) quá mảnh, khó nhìn;
- ở góc sau lưng, trận pháp che mất nửa trên màn hình.

Ngày 18/11 owner chọn: "Kiếm to hơn + trận lùi lại".

Các điều sau giữ nguyên như `docs/codex-queue/433i-tt-metal-energy-sword.md`:
- luật "chỉ đặt, xoay, thu phóng đều, nhuộm, chỉnh độ mờ";
- quyền chạy, server 3148, ffmpeg, prune;
- phạm vi sửa;
- cách đo, kể cả cách đo quãng rơi của 433f.

Được ghi `docs/codex-queue/433j-report.md` và `ABOUT.md` trong `typing-game-review/owner-review/2026-11-18/tu-tien/`. Khi xong phải tắt Chrome và xoá profile tạm.

## Việc
1. **Kiếm nhỏ to hơn.** Phóng đều 1,6–2 lần cả kiếm A lẫn vệt D.
   - Ở camera chơi 1280×720, thân một kiếm nhỏ (không tính vệt) cao ≥ 34 px.
   - Kiếm lớn cao gấp ≥ 3 lần kiếm nhỏ trên màn hình.
2. **Trận pháp lùi lại.** Dời tâm trận ra phía sau đàn quái (xa camera hơn) và lên cao vừa đủ.
   - Ở góc sau lưng (Alt+2), trận chiếm ≤ 35 % chiều cao khung và không che người tung chiêu.
   - Ở camera chơi, trận vẫn nằm trong khung, lề ≥ 4 %.
   - Kiếm rơi từ trận chéo về phía đàn quái.
   - Quãng rơi vẫn đạt mức của 433f: trung vị ≥ 0,45 s và ≥ 18 % chiều cao khung, ≥ 80 % số kiếm đạt.
3. **Kiếm lớn (owner 18/11: "kiếm to đang tự dùng code để làm viền ánh sáng nhìn rất xấu, cần sửa lại k dùng code"):** gỡ hẳn lớp hào quang `aura-metal-feather-mantle` (viền lông nhọn) khỏi kiếm lớn, và gỡ mọi nhuộm màu vàng phẳng trên mô hình Tripo — kiếm lớn hiện **đúng vật liệu gốc của GLB** (màu, normal, roughness, emissive map gốc). Hào quang mới sẽ là ảnh owner chọn ở phiếu 448; phiếu này chỉ để chỗ trống, không tự thêm lớp nào. **Bỏ** chỉ tiêu tỷ số sáng kiếm lớn/nhỏ ≥ 1,5 kế thừa từ 433i cho tới khi có hào quang 448; thay bằng: in tỷ số sáng hiện có (để biết), và kiểm `grep` trong `games/.wt-ic-lab-all/src/lab/metal-*` không còn lời gọi `aura-metal-feather-mantle` hay nhuộm phẳng cho kiếm lớn (in kết quả grep vào báo cáo).
4. **Giữ nguyên:** trận A, nhịp mưa, vùng trắng ≤ 6 %.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với bản 433i → sửa.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`.
- Mỗi vòng in ra: chiều cao kiếm nhỏ và kiếm lớn (px), tỷ số sáng (chỉ để biết), % chiều cao trận ở góc sau lưng, số đo quãng rơi, vùng trắng, p95.

## Nghiệm thu
- Kiểm kiểu 0 lỗi; p95 ≤ 16,7 ms.
- Lưu `metal-rain-j.jpg` và `.mp4` vào `typing-game-review/owner-review/2026-11-18/tu-tien/`, thêm dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
