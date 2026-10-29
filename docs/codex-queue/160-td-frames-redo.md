# Phiếu 160 · Wordwoven · Làm lại năm khung UI (115)

**Nguồn:** chấm nhận ảnh 29/10 của Claude (`docs/codex-queue/accept-29-10/verdict.md`): ảnh của phiếu gốc chưa đạt M ≥ 8 theo mức chợ. Phiếu này sửa đúng các ảnh bị trả.

**Báo cáo:** `docs/codex-queue/160-report.md`.

## Luật chung (phiếu làm lại)

- **Luật gốc:** theo nguyên văn mục "Luật chung" của phiếu gốc (`docs/codex-queue/115-td-ui-frames.md`), trừ những điểm ghi dưới đây. Đọc phiếu gốc và báo cáo gốc (`docs/codex-queue/115-report.md`) trước.
- **Chỉ dẫn sửa:** `docs/codex-queue/accept-29-10/verdict.md`, mục "115, năm khung". Prompt tiếng Anh ở đó dán nguyên văn vào lượt sinh. Tờ so của người chấm: `docs/codex-queue/accept-29-10/115-frames-vs-ref.jpg`.
- **Không ghi đè:** bản mới ghi thành `<tên>.v2.png` (và các bản thu, `.v2.alpha.png`, `.v2.tryN.*`) cạnh bản cũ. Claude đổi sang khi nhận.
- **Hậu kỳ không được phá tranh (luật mới 29/10, người chấm nhận ảnh):** ở 4/6 phiếu vừa chấm, lượt sinh đã đạt nhưng bước công cụ làm hỏng nó (hộp tối nung vào trời, mép núi san phẳng, khung bị bỏ phần vẽ, gamma làm phai), và bản tự chấm vẫn ghi 8. Từ nay:
  - mỗi ảnh giao có một tờ **"bản sinh | bản hậu kỳ"** cạnh nhau, cùng cỡ, ở `_review/160/raw-vs-final/`;
  - bước công cụ chỉ được cắt, tách nền, đổi cỡ, sửa mép, làm liền mép, chỉnh sáng nhẹ toàn ảnh (±10 %); không được xóa, san phẳng, phủ mảng màu hay thay phần vẽ;
  - khi một ngưỡng số trong phiếu mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh), **dừng lại**, giữ tranh đẹp, ghi rõ mâu thuẫn trong báo cáo để Claude quyết;
  - tự chấm M trên bản hậu kỳ, không trên bản sinh.
- **Bố cục (Wordwoven):** tránh "dày kiểu AI". Mỗi tranh có một trọng tâm và khoảng 40 % khung là vùng yên (trời rộng, sương, mặt nước). Ruộng bậc thang không vàng chanh rực: xanh ngọc và vàng lúa chín trầm.

## Việc

**Năm khung** `panel-large`, `plate-long`, `button`, `button-active`, `tooltip`: làm lại hậu kỳ **từ try1** (người chấm: try1 khoảng 8, đá vôi chạm, góc đồng mặt trời; bản giao chỉ còn tấm ngọc phẳng như bảng CSS):
- giữ độ phân giải gốc của try1, không thu góc về 32 px;
- cắt 9-slice ở mép trong của trang trí góc (panel khoảng 11 % cạnh); cạnh có hoa văn ghi `"repeat": "round"` trong `<tên>.v2.json` để CSS dùng `border-image-repeat: round`;
- lòng chữ chỉ được làm tối để chữ đọc rõ (WCAG ≥ 7 với chữ sáng), không thay lòng bằng mảng ngọc phẳng;
- `tooltip` cũng từ try1;
- `button-active` dựng từ `button.v2` cộng ánh hổ phách ở viền và lòng (không sinh mới).
- **Ba mẫu ngọc:** người chấm thấy ba thứ ngọc khác nhau (huy hiệu lục bảo bão hòa, logo ngọc nhạt, khung ngọc gần đen). Lấy ngọc của `crest` (đã nhận) làm chuẩn; ghi mã màu ba sắc ngọc (sáng, giữa, tối) vào báo cáo để các phiếu sau dùng.

**Kiểm:** như phiếu 115, cộng tờ `raw-vs-final`, cộng `_review/160-mock.jpg`: dựng lại mock HUD và menu Tạm dừng ở 1280 × 720 với khung mới, cạnh ảnh tham chiếu. Tự chấm M cho mock.
