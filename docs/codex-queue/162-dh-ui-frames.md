# Phiếu 162 · Dragonhold · Khung UI và bảng sử thi: hoa cương, sắt rèn, vàng búa (9 ảnh)

**Nguồn:** kiểm kê hình ảnh UI 29/10 (`docs/games/map1/UI_IMAGERY.md`): chỉ đạo mỹ thuật chưa có phiếu khung UI cho Dragonhold; HUD, thẻ đợt, thẻ ra mắt, cửa hàng, kết quả vẫn là bảng CSS. Chủ dự án 28/10: mọi chi tiết UI phải có hình thật; không hình vẽ bằng mã. Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc.

**Báo cáo:** `docs/codex-queue/162-report.md`.

**Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.

## Cách làm: theo phiếu 115, đổi sang Dragonhold

Đọc trước `docs/codex-queue/115-td-ui-frames.md` (phiếu khung của Wordwoven) và bản chấm nhận `docs/codex-queue/accept-29-10/verdict.md` mục 115. Làm **đúng chín món, khổ, cách cắt 9-slice, file `.json` và mục kiểm của phiếu 115**, với các điểm khác dưới đây.

1. **Thư mục:** `games/dragon-hold/art-src/ui/frames/` (mới). `_review/162*` ở `games/dragon-hold/art-src/_review/`. Chỉ được ghi ở đó và báo cáo. KA1 md5 trên `games/dragon-hold/art-src/ui/`.
2. **Phong cách:** khối **STYLE-UI** của Dragonhold, nguyên văn ở `docs/games/ART_DIRECTION_2026-10-28.md` §3.2 (hoa cương kem phong hóa, sắt rèn sẫm, viền vàng búa, men cam than hồng, chạm vảy rồng và cành thông, chút tím xám). Không dùng ngọc, đá vôi hay đồng của Wordwoven.
3. **Ảnh tham chiếu bắt buộc:** ảnh tham chiếu của chủ dự án `games/dragon-hold/art-src/_refs/owner-epic-2026-10-28.webp` (HUD: viền mảnh, icon gánh phần hình); các icon đã nhận của phiếu 137–139 (để khung hợp icon); ảnh 119 khi có.
4. **Bài học của phiếu 115 (bắt buộc):** lượt sinh đầu của 115 đã đẹp (đá chạm, góc đồng) nhưng hậu kỳ thu góc về 32 px và trải một mảng màu kín lòng, nên bản giao thành bảng phẳng như CSS (người chấm: M 4–4,5). Ở phiếu này:
   - giữ độ phân giải gốc của lượt sinh; cắt 9-slice ở mép trong của trang trí góc;
   - cạnh có hoa văn ghi `"repeat": "round"` trong `<tên>.json`;
   - lòng khung chỉ được làm tối cho chữ đọc rõ (WCAG ≥ 7 với chữ sáng), không thay bằng mảng màu phẳng;
   - `button-active` dựng từ `button` cộng ánh than hồng ở viền và lòng, không sinh mới.
5. **Mock kiểm:** `_review/162-mock.jpg`: dựng HUD và thẻ đợt của Dragonhold ở 1280 × 720 bằng các khung mới trên ảnh chụp trận (lấy một khung trong `games/dragon-hold/tmp/` hay `games/.wt-dh-mappilot/tmp/map-pilot-r2/compare-r2b/`, chỉ đọc), cạnh ảnh tham chiếu. Tự chấm M cho mock.

**Xong khi:** chín ảnh có bản chọn, qua mọi mục kiểm của phiếu 115 và tờ `raw-vs-final`, mỗi ảnh tự chấm M ≥ 8 và Q ≥ 8, mock M ≥ 8.
