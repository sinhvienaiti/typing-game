# Phiếu 158 · Wordwoven · Làm lại màn tựa và poster (113)

**Nguồn:** chấm nhận ảnh 29/10 của Claude (`docs/codex-queue/accept-29-10/verdict.md`): ảnh của phiếu gốc chưa đạt M ≥ 8 theo mức chợ. Phiếu này sửa đúng các ảnh bị trả.

**Báo cáo:** `docs/codex-queue/158-report.md`.

## Luật chung (phiếu làm lại)

- **Luật gốc:** theo nguyên văn mục "Luật chung" của phiếu gốc (`docs/codex-queue/113-td-title-keyart.md`), trừ những điểm ghi dưới đây. Đọc phiếu gốc và báo cáo gốc (`docs/codex-queue/113-report.md`) trước.
- **Chỉ dẫn sửa:** `docs/codex-queue/accept-29-10/verdict.md`, mục "113 `title-backdrop`" và "113 `poster`". Prompt tiếng Anh ở đó dán nguyên văn vào lượt sinh. Tờ so của người chấm: `docs/codex-queue/accept-29-10/113-vs-ref.jpg`.
- **Không ghi đè:** bản mới ghi thành `<tên>.v2.png` (và các bản thu, `.v2.alpha.png`, `.v2.tryN.*`) cạnh bản cũ. Claude đổi sang khi nhận.
- **Hậu kỳ không được phá tranh (luật mới 29/10, người chấm nhận ảnh):** ở 4/6 phiếu vừa chấm, lượt sinh đã đạt nhưng bước công cụ làm hỏng nó (hộp tối nung vào trời, mép núi san phẳng, khung bị bỏ phần vẽ, gamma làm phai), và bản tự chấm vẫn ghi 8. Từ nay:
  - mỗi ảnh giao có một tờ **"bản sinh | bản hậu kỳ"** cạnh nhau, cùng cỡ, ở `_review/158/raw-vs-final/`;
  - bước công cụ chỉ được cắt, tách nền, đổi cỡ, sửa mép, làm liền mép, chỉnh sáng nhẹ toàn ảnh (±10 %); không được xóa, san phẳng, phủ mảng màu hay thay phần vẽ;
  - khi một ngưỡng số trong phiếu mâu thuẫn với tranh (muốn đạt số phải làm bẩn tranh), **dừng lại**, giữ tranh đẹp, ghi rõ mâu thuẫn trong báo cáo để Claude quyết;
  - tự chấm M trên bản hậu kỳ, không trên bản sinh.
- **Bố cục (Wordwoven):** tránh "dày kiểu AI". Mỗi tranh có một trọng tâm và khoảng 40 % khung là vùng yên (trời rộng, sương, mặt nước). Ruộng bậc thang không vàng chanh rực: xanh ngọc và vàng lúa chín trầm.

## Việc

1. **`title-backdrop.v2`:** lấy lại `ui/title-epic/title-backdrop.try1.png` (người chấm: khoảng 8,5 trước hậu kỳ). Một lượt sửa ảnh: dời con rồng nhỏ và đỉnh tháp ra khỏi vùng logo, đặt rồng xuống thung lũng bên trái. Không nung hộp tối. Bỏ ngưỡng độ lệch chuẩn luma ≤ 0,12 của phiếu 113 (chỉ đạt được bằng cách làm bẩn tranh); logo đã đọc được nhờ viền đồng sẫm, nếu cần thì UI thêm một vệt tối mềm sau logo.
2. **`poster.v2`:** sinh lại khổ dọc (không ép từ keyart): rồng lớn, trọn cánh trong khung; cây khổng lồ cao hơn mọi vách; ít chi tiết hơn; 22 % trên là trời bão có tia nắng. Đính kèm `keyart.png` làm tham chiếu nhân vật và màu.

**Kiểm:** như phiếu 113 (trừ ngưỡng đã bỏ), cộng tờ `raw-vs-final`, cộng `_review/158-vs-ref.jpg`: hai ảnh mới cạnh ảnh tham chiếu của chủ dự án cùng cao 640 px, kèm logo đặt thử lên `title-backdrop.v2` ở 1280 × 720.
