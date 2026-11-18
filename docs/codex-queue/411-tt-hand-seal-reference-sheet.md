# Phiếu 411: Ảnh tham chiếu 10 thủ ấn tu tiên (để dựng tư thế tay theo ảnh)


Phản biện: PASS (Sonnet, 16/11; 406b sau khi sửa phạm vi kit)
## Bối cảnh
Hoạt ảnh đợt 2 (`403-report.md`) có 10 thủ ấn đúng kỹ thuật nhưng agent Claude chấm "chưa đạt": trên ma-nơ-canh chúng chỉ như ký hiệu tay chung chung, tay buông lỏng xa thân, không có ấn đan ngón, ngón tay lỏng ở S1, S8, S9 (`typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r2/run-IpDPoU/403-seals-front-10-sheet.jpg`). Owner: mọi việc tạo hình phải có ảnh tham chiếu trước, rồi làm theo ảnh. Bảng 10 ấn và tên trong `393-report.md` §4.

## Việc
`image_gen`, tối đa 8 lần, 1536×1024, lưu `games/immortality-cultivation/art-src/concept/hand-seals/seals-<tên>.v1-try<k>.png`, prompt thật trong `.prompt.txt`.
Ảnh tham chiếu bắt buộc mọi lần tạo, ghi đường dẫn trong prompt: ảnh 403 ở trên (chỉ để biết tư thế đang có và lỗi), và `393-report.md` §4 (mô tả từng ấn: ngón nào duỗi/gập, tay ở đâu so với thân).
Vẽ:
1. Hai tấm "bảng thủ ấn" chính diện, mỗi tấm 5 ô, tổng 10 ấn theo §4: nửa thân trên một tu sĩ trung tính (không phải nhân vật cụ thể, mặc áo tu tiên đơn giản), hai bàn tay rõ ràng ở ngang ngực/mặt, ngón tay rõ khớp, dáng thanh thoát, tay gần thân, đan ngón đúng kiểu ấn Đạo/Phật (kiếm chỉ, liên hoa ấn, ngoại phược, nội phược…). Nền xám trơn, ánh sáng đều. Ghi tên ấn tiếng Anh nhỏ dưới mỗi ô.
2. Một tấm cận cảnh 10 bàn tay (chỉ hai bàn tay mỗi ô, nhìn chính diện) để dựng ngón.
Phong cách: tranh minh họa nhân vật game thương mại, sạch, dễ đọc tư thế.

## Ràng buộc
Không sửa code, không video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh.

## Giao nộp
Ảnh ghép `seals-sheet-411.jpg` trong `art-src/concept/hand-seals/` và `docs/codex-queue/411-report.md`.
