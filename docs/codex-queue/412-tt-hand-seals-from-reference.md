# Phiếu 412: Dựng lại 10 thủ ấn theo ảnh tham chiếu 411


Phản biện: PASS (Sonnet, 16/11, vòng 3)
## Bối cảnh
Bản 403 đúng kỹ thuật nhưng chưa đạt về hình: thủ ấn như ký hiệu tay chung chung, tay buông xa thân, ngón lỏng (agent Claude chấm 16/11). Owner: làm theo ảnh tham chiếu. Ảnh đích: `games/immortality-cultivation/art-src/concept/hand-seals/seals-sheet-411.jpg` (10 ấn nửa thân trên + 10 ấn cận cảnh bàn tay; ảnh lẻ cùng thư mục, xem `411-report.md`). Rig: `human` (66 khớp), code `src/lab/anim-r2-*` trong worktree `games/.wt-ic-lab-all`.

## Việc
0. **Trước khi chỉnh tư thế:** xem ảnh 411 (bản cận cảnh tay) và viết bảng chuẩn cho từng ấn S0–S9 vào `src/lab/anim-r3-seals.json` và vào báo cáo: với mỗi bàn tay, trạng thái 5 ngón (duỗi / gập / chạm ngón khác), vùng cổ tay (bụng / ngực / mặt), lòng bàn tay hướng (trước / trong / lên / xuống), và chỗ hai tay chạm nhau nếu có. Bảng này là chuẩn để kiểm; Codex tự viết script kiểm `src/lab/anim-r3-check.ts` đọc bảng đó.
1. Với từng ấn S0–S9: chỉnh tư thế vai, khuỷu, cổ tay và **từng đốt ngón** cho khớp ảnh đích: vị trí tay so với thân (ngang ngực/bụng/mặt, sát thân), hướng lòng bàn tay, ngón nào duỗi/gập/đan. Ghi bảng góc khớp chính cho mỗi ấn.
2. Chuyển giữa các ấn mượt (0,15–0,3 s), không xuyên ngón (khoảng cách hai đốt ngón khác nhau ≥ 4 mm), không gập cổ tay quá giới hạn tự nhiên.
3. Thêm chế độ xem so sánh trong lab: góc chính diện, cùng khung hình với ảnh đích để đặt cạnh nhau.
4. Giữ nguyên Kiếm A, chưởng, kết trận và luật ≤ 50 ms.

## Nghiệm thu (số đo)
- Rig: `skills-lab.html?hero=human` (bộ xương 66 khớp đã dùng ở 403). Chạy `src/lab/anim-r2-check.ts` (hoặc bản mở rộng `anim-r3-check.ts`) như 403; kiểm kiểu strict 0 lỗi.
- Với mỗi ấn S0–S9, check tự động ghi và đạt:
  - khoảng cách hai đốt ngón của hai ngón khác nhau ≥ 4 mm ở mọi khung;
  - cả hai cổ tay nằm trong khoảng 0,05–0,30 m trước mặt phẳng thân (sát thân, không buông xa);
  - độ cao cổ tay đúng vùng của ảnh đích (bụng / ngực / mặt, ghi vùng trong bảng);
  - góc gập cổ tay ≤ 70°;
  - mỗi ngón ở đúng trạng thái duỗi (tổng gập ba đốt < 40°) hoặc gập (> 120°) như ghi cho ấn đó.
- Trễ phím→phát chiêu ≤ 50 ms ở 60 và 120 Hz cho Kiếm A, chưởng, kết trận (như 403).
- Nếu một giới hạn không đạt được vì chính ấn đòi hai tay chạm hoặc đan nhau (ví dụ S0, S9, hoặc bất kỳ ấn nào bảng chuẩn ghi "chạm ngón khác"), ghi ngoại lệ cho đúng ấn đó kèm lý do trong bảng; không nới giới hạn cho các ấn khác.
- Mắt người chấm sau: agent Claude Opus đặt cạnh ảnh đích và chỉnh.
- Lệnh chụp lưới 10 ấn chính diện và 10 cận cảnh tay, đặt cạnh ô tương ứng của ảnh đích, để Claude chụp (sandbox chặn trình duyệt). Sau đó agent Claude Opus sẽ chỉnh bằng mắt.
- Chỉ sửa trong `games/.wt-ic-lab-all`: `src/lab/anim-r1-*`, `src/lab/anim-r2-*`, file mới `src/lab/anim-r3-*`. Không đụng `*-ult-*`, `skills-main.ts` (trừ khi cần một phím mới, khi đó đọc lại và giữ phần của người khác), `src/view/`, `src/ui/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/412-report.md`.
