# Phiếu 415: Điều khiển xoè/xoắn từng ngón và hướng khuỷu (pole) cho rig `human`, rồi đặt lại 10 thủ ấn


Phản biện: PASS (Sonnet, 16/11; tách 415 sau 3 vòng, 415b sửa tỉ lệ ngón cái)
## Bối cảnh
Sau 412 và 3 vòng chỉnh bằng mắt (agent Claude Opus, 16/11), mỗi thủ ấn chỉ 4–5/10 so với ảnh đích `games/immortality-cultivation/art-src/concept/hand-seals/seals-sheet-411.jpg`. Ảnh so: `typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r3/seals-412-vs-ref.jpg`. Nguyên nhân gốc theo agent:
- ngón duỗi luôn xoè rộng; đổi giá trị xoè không có tác dụng → độ xoè đến từ tư thế nghỉ (rest) của bàn tay rig, không qua tham số hiện có;
- khuỷu chĩa ra ngoài ở S3, S4, S8 (dáng "càng cua");
- ngón gập thành móc cụt, không cong mềm;
- S5 nắm tay trái quá xa ở hông.
Đây là lỗi điều khiển rig, không phải lỗi số liệu từng ấn.

## Việc (worktree `games/.wt-ic-lab-all`, `src/lab/anim-r*`)
1. **Xoè/khép từng ngón:** thêm điều khiển góc khép-xoè (abduction) và xoắn (twist) riêng cho đốt gốc mỗi ngón, tính **so với tư thế nghỉ thật của rig** (đo rest pose, bù về 0 trước khi áp góc). Kiểm: đặt xoè = 0 thì hai ngón kề nhau song song, khe giữa đầu ngón ≤ 8 mm.
2. (Tách sang phiếu 415b: cong ngón mềm.)
3. **Hướng khuỷu (pole):** IK hai xương cho tay với điểm pole kéo khuỷu xuống và vào sát thân (mặc định), có thể chỉnh theo từng ấn. Kiểm: ở mọi ấn, khuỷu nằm dưới vai và cách mặt phẳng thân ≤ 0,25 m sang bên.
4. **Đặt lại 10 ấn** theo `anim-r3-seals.json` dùng các điều khiển mới; sửa S5 (nắm tay trái trước bụng).
5. Giữ check 412 (≥ 4 mm, trễ ≤ 50 ms) và thêm check cho 1 và 3.

## Nghiệm thu
- TypeScript strict + `noUncheckedIndexedAccess` cho các file `src/lab/anim-r*` sửa/thêm: 0 lỗi (cùng cách kiểm như báo cáo 412).
- `src/lab/anim-r3-check.ts` mở rộng in bảng số từng ấn S0–S9 và đạt toàn bộ: khoảng cách đốt ngón ≥ 4 mm, trễ phím→phát chiêu ≤ 50 ms ở 60/120 Hz (cổng 412); khe đầu ngón kề nhau ≤ 8 mm khi xoè = 0; khuỷu dưới vai và lệch ngang ≤ 0,25 m; nắm tay S5 trước bụng (cổ tay trong vùng bụng của `anim-r3-seals.json`).
- Đơn vị: mét trong không gian thế giới của rig `human` (cao 1,65 m như báo cáo 403); mm = 0,001 m. Vùng cổ tay lấy đúng khoảng số đã ghi trong `anim-r3-seals.json` của 412, dung sai ±0,03 m; vùng bụng của S5 là vùng "bụng" trong file đó.
- **Ngoài nghiệm thu của Codex:** sau khi Codex xong, agent Claude Opus chấm mắt từng ấn so ảnh đích (mục tiêu ≥ 7/10). Codex chỉ cần đạt các số đo trên và để lệnh chụp.
- Lệnh chụp cặp so sánh với ảnh đích để Claude chụp (sandbox chặn trình duyệt); agent Claude Opus chấm sau.
- Chỉ sửa trong `games/.wt-ic-lab-all`: `src/lab/anim-r*`. Không đụng `*-ult-*`, `src/view/`, `src/ui/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/415-report.md`.
