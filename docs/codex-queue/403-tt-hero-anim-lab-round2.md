# Phiếu 403: Hoạt ảnh nhân vật, đợt 2 trong lab (chính diện, thêm thủ ấn và hai họ chiêu)


Phản biện: PASS (Sonnet, 16/11; đã thêm số khoảng cách ngón và đưa vào hàng làn B)
## Bối cảnh
Đợt 1 (`397-report.md`) đạt kỹ thuật: phím→phát chiêu ~23 ms, tay/khuỷu không méo, không về bind pose. Nhưng ảnh chụp từ sau vai nên thủ ấn hai tay không thấy, đạo cụ (vòng ngọc, kiếm) che 2/8 khung. Owner 16/11 chọn: "Quay lại chính diện rồi làm đợt 2". Nghiên cứu nền: `393-report.md` §3, §4 (10 thủ ấn), §5.2 (họ chiêu), §6. Vẫn chỉ dùng rig `human` có sẵn (owner 16/11: nhân vật phải đạt chất lượng 2D trước khi làm 3D và rig thật). Chạy sau 402 trong cùng làn B: đọc lại `skills-main.ts`, giữ phần nối của 402.

## Việc (worktree `games/.wt-ic-lab-all`, file `src/lab/anim-r1-*` hoặc `src/lab/anim-r2-*`)
1. **Camera xem chính diện:** thêm một góc quay lab nhìn nhân vật từ trước mặt, ngang ngực, thấy rõ hai bàn tay; ẩn đạo cụ che tay trong góc này (chỉ ở chế độ xem tay, không đổi game).
2. **Thủ ấn:** thêm đủ 10 thủ ấn theo bảng §4 (từng ngón duỗi/gập, vị trí tay so với thân), chuyển giữa các ấn mượt, không xuyên ngón. Phím lab để duyệt lần lượt từng ấn.
3. **Hai họ chiêu mới** theo §5.2: **chưởng** (đẩy lòng bàn tay, hông xoay, chân trụ) và **kết trận** (hai tay vẽ ấn rồi ấn xuống đất). Mỗi chiêu đủ tụ lực theo chữ → phát ≤ 50 ms → thu thế; sự kiện release cùng khung VFX/âm có sẵn.
4. Giữ Kiếm A của đợt 1; chuyển qua lại giữa ba họ chiêu không bật, không trượt chân.

## Nghiệm thu
- Kiểm kiểu sạch; probe trễ phím→phát chiêu ≤ 50 ms cho cả ba chiêu ở 60 và 120 Hz; kiểm không xuyên ngón (khoảng cách giữa hai đốt ngón bất kỳ của hai ngón khác nhau ≥ 4 mm ở mọi khung) và không về bind pose.
- Lệnh chụp có sẵn cho: góc chính diện từng thủ ấn (lưới 10 ô), mỗi chiêu 8 pha ở camera chơi và góc chính diện. Nếu sandbox chặn trình duyệt, để lệnh cho Claude chụp.
- Chỉ sửa trong `games/.wt-ic-lab-all`: `src/lab/anim-r1-*`, file mới `src/lab/anim-r2-*`, chỗ nối phím trong `src/lab/skills-main.ts`, `art-src/lab/anim/`. Không đụng `wood-ult-*`, `metal-ult-*`, `ice-ult-*`, `src/view/`, `src/ui/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/403-report.md`: phím lab, lệnh chụp, số đo, điểm yếu tự thấy.
