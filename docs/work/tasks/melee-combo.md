# Đánh thường liên hoàn: chém nhiều góc và phi kiếm liên tục (theo vũ khí × hệ)

**Mục tiêu (≤ 3 dòng):** lối đánh gần như không hồi chiêu, gõ liên tục là đánh liên tục. Có hai dạng: (1) chém cận chiến liên hoàn, mỗi nhát một góc, có động tác và vệt chém theo góc đó; (2) phi kiếm phóng liên tục. Mỗi nhát mang hình của vũ khí, chất liệu và hào quang của hệ, trúng quái thì để lại hiệu ứng của hệ.
**Cách đã chốt:** anh, 06/11 ~13:00: "đã nghĩ tới việc cận chiến chưa... chém liên tục, và skill bắn ra phi kiếm liên tục... chém theo nhiều góc, vệt chém cũng phải theo đổi theo nhiều góc... mỗi vệt chém sẽ phụ thuộc vào vũ khí và hệ... hoả thì vệt chém màu lửa, sẽ có hiệu ứng của hệ hoả xung quanh và khi chạm quái thì sẽ gây hiệu ứng hoả lên". Canon: đòn thường `auto{seat, beast, origin}` theo nhịp của phái. Lưỡi liềm đối xứng chỉ cho chiêu bắn ra từ kiếm; vệt lệch (vung) dùng cho chém cận chiến.
**Nghiệm thu (số):**
- Từ phím tới nhát chém ≤ 50 ms.
- Không có 2 nhát liền nhau cùng góc.
- Vệt chém khớp mặt phẳng nhát vung (lệch ≤ 10°).
- Trúng quái thì có hiệu ứng hệ (cháy, đóng băng…) trong ≤ 1 khung.
- Chữ trên quái ≥ 7:1.
- Anh chấm trong lab.

## Danh sách việc
1. **Dáng vệt chém** (ảnh Codex, tự chấm ≥ 8). Có 3 dáng mới cho mỗi hệ, ngoài vệt lệch hiện có:
   - chém nhanh mảnh (Kiếm);
   - quét rộng nặng (Đao);
   - đâm thẳng và vòng xoáy (Thương).

   Làm mẫu Hỏa trước (phiếu 315), anh duyệt rồi mới làm 14 hệ.
2. **Chuỗi động tác** (mã, hệ động tác của lab `src/lab/anim/`, khung khoá tạo bằng mã): 6–8 nhát mỗi vũ khí.
   - Các nhát: ngang trái sang phải, phải sang trái, chéo xuống trái, chéo lên phải, bổ dọc, đâm, xoay vòng.
   - Nhát kế tiếp chọn sao cho tay chuyển tự nhiên.
   - Từ Chớp hoặc Hoàn hảo cho nhát kết mạnh hơn.
   - Thuộc hệ thống dùng chung (động tác nhân vật, chuẩn 9).
3. **Vệt theo lưỡi:**
   - Một dải đi theo mũi kiếm suốt nhát vung, chất liệu là `ribbon` hoặc `sheath` của hệ, mép mềm, tàn bằng erosion.
   - Ảnh vệt chém xoay và lật đặt đúng mặt phẳng của nhát.
   - Tia và hạt của hệ rơi dọc vệt.
4. **Hiệu ứng hệ:**
   - Lưỡi kiếm luôn có `sheath` của hệ khi đang liên hoàn.
   - Cú trúng: `impact` + `hit-affliction` (video đang làm) bám lên quái 1–2 s.
   - Nhát kết: `burst` nhỏ + vết trên đất.
5. **Phi kiếm liên tục:**
   - Mỗi từ gõ xong phóng một kiếm bay (mô hình kiếm có `sheath` của hệ và vệt `ribbon`), tự tìm quái gần.
   - Trúng thì `impact` + `hit-affliction`.
   - Gõ liên tục thì kiếm bay thành chuỗi, lệch góc nhẹ cho khỏi trùng.
6. **Âm:** dùng tiếng vung và trúng sẵn có theo vũ khí và hệ (`tt-sfx-<hệ>-sword-swing`, `-sword-hit`, `-sabre-hit`, `-spear-hit`), đổi cao độ ±3 %, không lặp bản liền nhau.
7. **Lab:** phím mới cho "liên hoàn"; gõ từ thật hoặc WPM giả để thấy nhịp; đổi vũ khí bằng W, đổi hệ bằng E.

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 06/11 13:05 · Claude · lập danh sách; phiếu Codex 315 (3 mẫu dáng vệt chém Hỏa) xếp sau 314 (biểu tượng)
- 06/11 14:00 · Codex · phiếu 317 xong: 39/39 vệt chém (13 hệ × 3 dáng), tự chấm đều ≥ 8, không vẽ lại. Tấm ghép 14×3: `owner-review/2026-11-06/tu-tien/melee-slash/melee-slash-14x3.jpg`. Lưu ý: Ám nền đen chỉ còn viền đỏ, dễ lẫn Huyết; cần bản nền trắng cho thân khói như sao băng Ám.
