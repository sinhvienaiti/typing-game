# Phiếu 159 · Wordwoven · Làm lại vòng trời và phông xa (114)

**Nguồn:** chấm nhận ảnh 29/10 của Claude (`docs/codex-queue/accept-29-10/verdict.md`): ảnh của phiếu gốc chưa đạt M ≥ 8 theo mức chợ. Phiếu này sửa đúng các ảnh bị trả.

**Báo cáo:** `docs/codex-queue/159-report.md`.

## Luật chung (phiếu làm lại)

- **Luật gốc:** theo nguyên văn mục "Luật chung" của phiếu gốc (`docs/codex-queue/114-td-sky-backdrops.md`), trừ những điểm ghi dưới đây. Đọc phiếu gốc và báo cáo gốc (`docs/codex-queue/114-report.md`) trước.
- **Chỉ dẫn sửa:** `docs/codex-queue/accept-29-10/verdict.md`, mục "114, bảy ô vòng". Prompt tiếng Anh ở đó dán nguyên văn vào lượt sinh. Tờ so của người chấm: `docs/codex-queue/accept-29-10/114-ring-vs-ref.jpg`.
- **Không ghi đè:** bản mới ghi thành `<tên>.v2.png` (và các bản thu, `.v2.alpha.png`, `.v2.tryN.*`) cạnh bản cũ. Claude đổi sang khi nhận.
- **Hậu kỳ không được phá tranh (luật mới 29/10, người chấm nhận ảnh):** ở 4/6 phiếu vừa chấm, lượt sinh đã đạt nhưng bước công cụ làm hỏng nó (hộp tối nung vào trời, mép núi san phẳng, khung bị bỏ phần vẽ, gamma làm phai), và bản tự chấm vẫn ghi 8. Từ nay:
  - mỗi ảnh giao có một tờ **"bản sinh | bản hậu kỳ"** cạnh nhau, cùng cỡ, ở `_review/159/raw-vs-final/`;
  - bước công cụ chỉ được cắt, tách nền, đổi cỡ, sửa mép, làm liền mép, chỉnh sáng nhẹ toàn ảnh (±10 %); không được xóa, san phẳng, phủ mảng màu hay thay phần vẽ;
  - khi một ngưỡng số trong phiếu mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh), **dừng lại**, giữ tranh đẹp, ghi rõ mâu thuẫn trong báo cáo để Claude quyết;
  - tự chấm M trên bản hậu kỳ, không trên bản sinh.
- **Bố cục (Wordwoven):** tránh "dày kiểu AI". Mỗi tranh có một trọng tâm và khoảng 40 % khung là vùng yên (trời rộng, sương, mặt nước). Ruộng bậc thang không vàng chanh rực: xanh ngọc và vàng lúa chín trầm.

## Việc

1. **Bảy ô vòng** `sky-day-a`, `sky-day-b`, `sky-night`, `layer-320`, `layer-220`, `layer-140-a`, `layer-140-b`: làm lại **hậu kỳ** từ các lượt đã sinh (người chấm: tranh gốc tốt, hậu kỳ làm hỏng):
   - không san mép núi thành vai phẳng, không ép phẳng mép trời, không cắt dải kem phẳng ở đáy;
   - luật ghép như phiếu 114: ô `-a` một lần, ô `-b` lật ngang xen kẽ, nên chỗ nối đã trùng pixel; chỉ nối `a` với `b` bằng sửa ảnh ở dải giữa;
   - khử vệt cột tím ở mép trái `layer-140-a` (dải 2–3 px).
2. **`sky-night-b`** (ảnh thứ mười, mới): như `sky-night` nhưng **không có trăng**, để vòng đêm không lặp bốn mặt trăng. Đính kèm `sky-night` làm tham chiếu màu.
3. **Kiểm vòng ghép:** dựng vòng 360° như trong game (a | b lật | b | b lật) cho ngày, đêm, 320, 220, 140, xem ở cỡ đầy đủ. Nếu vòng vẫn đọc thành những "đảo" rời cách nhau bởi dải phẳng, thì với lớp đó **sinh một toàn cảnh liền 360°** (khổ 4:1, liền mép trái phải, đường chân núi chạy liên tục) thay cho các ô; ghi rõ lớp nào đổi cách làm. Tối đa 3 lượt sinh mỗi ảnh như luật.

**Kiểm:** như phiếu 114, cộng tờ `raw-vs-final`, cộng `_review/159-ring.jpg`: năm vòng ghép mới chồng lớp như trong game, đặt cạnh ảnh tham chiếu của chủ dự án. Ghi một câu cho mỗi vòng: "liền như một dãy núi" hay "còn thành đảo".
