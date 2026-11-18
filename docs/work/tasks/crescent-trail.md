# Vệt năng lượng mềm bay sau lưỡi liềm (phím 2, Nhất Tuyến Xuyên Vân)

**Mục tiêu (≤ 3 dòng):** sau lưỡi liềm kiếm khí đang bay có một vệt sáng năng lượng mềm, đẹp, chảy theo cho sống động, đúng chất liệu của từng hệ.
**Cách đã chốt:** anh (05/11 ~22:40): "bạn tạo ra vệt chém lưỡi liềm r, nhưng lại chưa tạo ra hiệu ứng ánh sáng dạng năng lượng mềm đẹp bay theo sau nó cho sống động".

Hiện trạng (Claude đọc mã ở `games/.wt-ic-lab-elements`, nhánh `claude/lab-element-kits`):
- `sword-skills.ts` phím 2 (khoảng dòng 3655–3690) đẩy `k.ribbon` và `k.silk` ở chuôi kiếm (`pommelBack`).
- Lưỡi liềm (`flyingCutAt` → `element-clips.ts flyingCut`) bay trước kiếm 1,2 m và chỉ là một tấm giữ nguyên khung đỉnh, nên ngay sau lưng lưỡi liềm không có gì.

Làm (chỉ ở view, không đổi sim; hình từ clip có sẵn, không vẽ hình bằng mã):
1. **Vệt đuôi mềm sau lưng lưỡi liềm (vệt chính).**
   - Một dải theo lịch sử vị trí của lưỡi liềm, nối từ mặt lõm của nó.
   - Ở đầu rộng khoảng 70–90 % sải lưỡi liềm, thon dần về 0 trong 3–5 m đường bay (khoảng 0,25–0,35 s).
   - Chất liệu lấy từ clip `ribbon` (hoặc `sheath`) của chính hệ đó, chạy dọc dải, cộng sáng.
   - **Mép mềm** (mờ dần ra hai mép, không có cạnh cứng: anh từng chê dải ribbon "khối cạnh cứng" lúc 21:20). Lõi mảnh, vầng ≤ 0,9 mỗi kênh.
   - Hệ Ám: thân khói (`layer: body`) và viền đỏ thẫm (`rim`), theo bảng màu A.
2. **Bóng mờ** (afterimage): 2–3 bản lưỡi liềm mờ dần phía sau, cách nhau khoảng 0,04–0,06 s, đục khoảng 0,45 / 0,25 / 0,12, nhỏ dần, tan bằng erosion.
3. **Hai luồng hạt lấp lánh từ hai sừng** như vệt hơi: clip `sparkle` của hệ, rơi lại và tan chậm.
4. **Tấn công nhanh, tàn chậm:** khi lưỡi liềm tới đích hay biến mất, vệt còn lại tan bằng erosion trong 0,4–0,6 s, không tắt bụp.
5. Khi video lưỡi liềm của từng hệ (`i2v-<hệ>-crescent-sym`, Firefly đang làm tối nay) vào manifest, lưỡi liềm dùng video đó thay ảnh tĩnh, để năng lượng chảy trong chính lưỡi liềm. Agent lab-flipbooks đưa video vào manifest.
6. Chữ quái luôn đọc được (≥ 7:1). Vệt nằm dưới lớp chữ, không chồng quá 2 lớp cộng sáng ở một chỗ.

**Nghiệm thu (số):** dải mở rộng ngay khung đầu lưỡi liềm xuất hiện; không cạnh cứng (mép mờ dần qua ít nhất 30 % nửa bề rộng); vầng ≤ 0,9; tan ≥ 0,4 s; đủ 14 hệ; không lỗi trong Chrome headless; khung so sánh trước/sau của 3 hệ (Kim, Hỏa, Ám) ở góc camera chơi gửi anh. Anh đang ở máy: cập nhật bản 4310 để anh tự thử, không cần quay video.
**Phiếu, báo cáo, ảnh:** khung trước/sau vào `typing-game-review/owner-review/2026-11-05/tu-tien/lab-elements/`.

## Nhật ký (mỗi dòng một sự kiện: ngày giờ · ai · việc · kết quả)
- 05/11 22:42 · Claude · tạo việc, giao agent lab-element-kits
- 05/11 23:05 · Claude (lab-element-kits) · làm xong mục 1–4 và 6, commit `baf1cb5` (nhánh claude/lab-element-kits): dải mềm từ lòng lưỡi liềm, rộng ~85 % sải, thon về 0 sau 5 m, mép mờ 45 % nửa bề rộng, vầng ≤ 0,9; 3 bóng mờ 0,04 s (0,45/0,25/0,12, mòn từ sừng); lấp lánh hai sừng; tan 0,5 s sau khi chạm. Ám: khói đen + viền đỏ thẫm từ clip ribbon; Hỏa: dải lửa; hệ chưa có ribbon: dải lụa gió theo màu hệ. 14 hệ chạy trên 4310 không lỗi; 1059 test qua; khung trước/sau `crescent-trail-{metal,fire,dark}-truoc-sau-baf1cb5.jpg`. Mục 5 (video i2v-…-crescent-sym) chưa làm: chưa có video trong manifest.
- 05/11 23:10 · Claude · kiểm khung `baf1cb5`: Hỏa, Kim thấy dải mềm và bóng mờ; Ám gần như không thấy. Vệt còn đọc như các lưỡi liềm xếp chồng, chưa thành một dòng năng lượng chảy. Firefly hết hạn lúc 23:07 (hộp mua credit), nên 11 hệ sẽ không có clip `ribbon` mới. Giao vòng 2:
  1. Lưỡi liềm dùng video `<hệ>-crescent-sym` (14 clip đã vào manifest lúc 23:05, vai `slash`, shape `crescent-sym`), phát lặp khi bay thay cho ảnh tĩnh, để năng lượng chảy trong chính lưỡi liềm.
  2. Không mượn dải lụa Phong nhuộm màu cho hệ khác. Vệt của mỗi hệ lấy chất liệu từ clip của chính hệ đó (video lưỡi liềm hoặc clip `slash`, cắt phần dải năng lượng), cho chạy dọc vệt.
  3. Vệt là một dòng năng lượng mềm liền mạch: một dải có chất liệu chảy (UV cuộn, nhiễu mềm), sáng mềm (vầng ≤ 0,9). Bóng mờ chỉ là lớp phụ, mờ hơn, để không đọc thành bậc thang lưỡi liềm.
  4. Ám phải thấy rõ: thân khói đen trộn thường (clip `layer: body`, nền trắng) dưới viền đỏ thẫm cộng sáng.
  5. Khung trước/sau của Kim, Hỏa, Ám, Thủy; cập nhật bản 4310.
- 05/11 23:25 · Claude (lab-element-kits) · mục 5 xong, commit `9c0c55c`: lưỡi liềm phím 2 (bay, bóng mờ, nhát chém cuối) dùng video `<hệ>-crescent-sym` của cả 14 hệ thay ảnh tĩnh; chạy vòng 9 khung đầu ở 3× tốc độ (vài bản tối ở giữa: Hỏa còn 0,2 khung 16–20, Độc 0,5); Thổ quay nửa vòng. 4310 đã cập nhật, 14 hệ không lỗi, 1060 test qua.
- 05/11 23:58 · Claude (lab-element-kits) · vòng 2 xong, commit `c2673bd` + `6116402`: vệt mỗi hệ là chất của chính hệ (ribbon nếu có; không thì dải năng lượng cắt giữa cung video lưỡi liềm, đo trên khung đầu), chảy liền ngược về sau (cuộn UV, soi gương, nhiễu mềm), dài 8 m (5 m bị thẻ lưỡi liềm che gần hết); không còn dải lụa gió nhuộm màu; bóng mờ thành lớp phụ 0,3/0,15/0,06; Ám: khói đen trộn thường phủ đặc dưới viền đỏ thẫm. 4310 đã cập nhật, 14 hệ không lỗi, 1060 test qua; khung `crescent-trail-v2-{metal,fire,dark,water}-truoc-sau-6116402.jpg`. Ám vẫn kín đáo hơn Kim/Hỏa/Thủy ở góc camera chơi.
