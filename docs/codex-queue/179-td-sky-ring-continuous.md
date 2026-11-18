# Phiếu 179 · Wordwoven · Vòng trời và phông xa vẽ liền, bỏ lật gương (làm lại 159)

**Nguồn:** chấm nhận ảnh 29/10, lượt b (`docs/codex-queue/accept-29-10b/verdict.md`).

**Báo cáo:** `docs/codex-queue/179-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Luật chung (phiếu làm lại)

- **Luật gốc:** theo nguyên văn mục "Luật chung" của phiếu gốc (`docs/codex-queue/114-td-sky-backdrops.md` và `docs/codex-queue/159-td-sky-redo.md`), trừ những điểm dưới đây.
- **Chỉ dẫn sửa:** `docs/codex-queue/accept-29-10b/verdict.md`, mục "159, năm vòng: bỏ lật gương, vẽ vòng liền". Prompt tiếng Anh và các bước ở đó làm theo nguyên văn; tờ so của người chấm ở cùng thư mục (`159-ring.jpg`).
- **Không ghi đè:** bản mới ghi `.v3` cạnh bản cũ (`<tên>.v3.png`, `.v3.tryN.*`, các bản thu). Claude đổi sang khi nhận.
- **Không chờ phiếu nào khác.** Gặp điều không rõ thì chọn cách giữ tranh đẹp và ghi lại trong báo cáo; không dừng để hỏi.

## Việc

Làm đúng mục "159, năm vòng: bỏ lật gương, vẽ vòng liền" của bản chấm:
- trời ngày, trời đêm và vòng 140 dùng **bốn ô khác nhau** vẽ nối tiếp; vòng 320 và 220 dùng `L | L2 | L | L2`, không lật;
- giữ làm ô đầu: `layer-140-a.v2`, `layer-140-b.v2` (lật), `sky-day-a.v2`, `sky-day-b.v2`; với 320 và 220, bản `.v2` làm `L`;
- mỗi ô mới sinh bằng sửa ảnh nối tiếp từ 25 % mép phải của ô trước; khép vòng bằng sửa ảnh ở dải nối như 159 đã làm;
- trời đêm vẽ lại ô 2–4 nối tiếp từ ô có trăng; bỏ `sky-night-b.v2`;
- hòa màu sương ở dải nối bằng dốc ngang ≥ 200 px (lỗi cạnh đứng của 159 ở vòng 140);
- khoảng 9 ô mới và 5 dải nối.

**Kiểm mới (thay các ngưỡng cũ của 114 và 159):** ghép từng vòng như game; cắt góc nhìn 90° tại cả bốn mối; không trục gương nào, không mối nào thấy được ở 1 : 1. Bỏ các ngưỡng mép 8 % lặng, ≤ 6/255, ≤ 5 % cột alpha mềm, nền magenta bốn mép. Tờ `_review/179-ring.jpg`: năm vòng ghép chồng lớp như game, cạnh ảnh tham chiếu; mỗi vòng một câu "liền như một dãy núi" hay chỉ chỗ lỗi.
