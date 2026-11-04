# Phiếu 259 (CX-C, vòng ngọc): tiến độ

**Cập nhật:** 04/11/2026, chiều (agent viết phiếu, phiên Tu Tiên).

**Trạng thái:** phiếu `docs/codex-queue/259-tt-jade-ring-material.md` đã đủ lời giải, đã bỏ dòng "BẢN NHÁP".
- **Đường duyệt:** Claude tự phân tích; ChatGPT duyệt lượt 1 (FAIL, các lỗi đã xử lý); hai lượt PASS liên tiếp của agent phản biện Claude (ChatGPT/Gemini mất đăng nhập).
- **Chưa đưa vào làn Codex.** Phải chờ hai lượt PASS của agent phản biện. Worktree `games/.wt-immortality-cultivation-codex` (nhánh `codex/jade-ring-material`) chưa tạo.

## Đã làm sau bản nháp (13:50)
- ChatGPT và Gemini mất đăng nhập, nên không chạy tiếp lượt duyệt trong trình duyệt (luật 9 của skill `agent-orchestration`). Claude tự phân tích từ mã, GLB và texture.
- **Đo hình.** Đọc GLB trong Node bằng `tsx`, đưa về lưỡi đơn vị bằng chính `bladeFromObject`, rồi:
  - vẽ ảnh mặt trước, mặt sau, độ sâu, pháp tuyến;
  - trải vòng ra tọa độ cực;
  - cắt lát qua tâm ở 45° và 135°.
- **Kết quả hình:** đĩa ngọc là xuyến dày, lỗ `rIn` 0,0440 ở (0,0023; −0,0274). Gờ nối mỏng ở z ≈ 0, từ 0,092 tới 0,102. Vành bạc hình elip, từ 0,104 ra 0,113–0,128. Hạt, mây, chữ V và khâu nối nhô cao hơn đỉnh đĩa. Đĩa nghiêng khoảng 2°.
- **Phát hiện chính:** map màu đã là ngọc trắng (trung vị sRGB 218/215/213) và có nét vàng nhạt (216/181/142), sát màu ảnh đã duyệt. "Crôm" là do ORM:
  - độ kim loại trung vị 0,15, p90 tới 0,48, đốm 0,61;
  - độ nhám 0,22–0,26, đốm 0,10.
- **Lời giải đổi khỏi bản nháp:**
  - Bỏ dải vàng vẽ bằng hình học. Bản nháp sẽ đặt chỉ vàng lên vành bạc và tô gờ nối thành ngọc.
  - Thay bằng: vùng đổi theo hình (trong `rCut`, dưới hai mặt phẳng đỉnh cộng biên, không phải hạt), và trong vùng đó tách loại theo chính màu map. Trắng thành ngọc: điện môi, nhám 0,34. Vàng thành vàng kim: 0,85 / 0,30.
  - Impostor không đổi, vì atlas Blender đã sáng, vòng ở kiếm xa chỉ 5–21 px, và elip không có căn cứ.
- **Mô phỏng trên map thật** (model đầy đủ và LOD, mặt trước và sau): chỉ đĩa và nét vàng của nó đổi. Hạt, đế, mây, chữ V, khâu nối, vành giữ nguyên. Ảnh mô phỏng nằm ở thư mục nháp của phiên, không lưu vào repo.
- **Bản tham chiếu chạy được:** `jade-ring-reference.ts` trong thư mục này (hàm `jadeRingOf` và bộ đọc GLB).
  - Số đo của hai model ghi ở đầu tệp và trong bảng §1 của phiếu.
  - Vòng tổng hợp của test cho số đúng như thiết kế: nghiêng 2,4° ra độ dốc 0,0426 (0,0445 sau khi `rCut` dời về mép trong gờ), hạt không kéo mặt phẳng.
  - Đĩa đặc và lưỡi trơn trả `null`.
- **Đã kiểm ở nguồn:** three 0.170.0 `meshphysical.glsl.js` (thứ tự chunk), `roughnessmap_fragment` (kênh G), `metalnessmap_fragment` (kênh B), `lights_physical_fragment` (đọc `diffuseColor`, `metalnessFactor`, `roughnessFactor`).

## Phản biện lượt 1 (agent Claude độc lập): FAIL, đã sửa
- Ba lỗi, cả ba đúng sau khi Claude kiểm trên mã và số đo; chi tiết ở mục "Phản biện" cuối phiếu.
  1. Mặt nạ của Kiểm 8 thiếu kiếm cắm của nạn nhân và kiếm trời K5: thêm `__lab.swordMask(on, all)`; `MASK=1` gọi `swordMask(true, true)`.
  2. Gờ nối có độ bão hòa tuyến tính 0,52–0,59 (không phải 0,26), bị đổi thành vàng lốm đốm: `rCut` dời về mép trong gờ (`rs[a0]`); bảng số, test, tham chiếu cập nhật; thêm `ring-sim.ts` và số bắt buộc ở Kiểm 6.
  3. `jadeRingOf` thêm `fail?: (step) => void`; `modelOf` in cảnh báo có tên model.
- Đếm lại hai lượt PASS từ đầu.

## Còn lại
1. Hai lượt PASS liên tiếp của agent phản biện Claude, tối đa 4 lượt. FAIL thì sửa phiếu và đếm lại từ đầu.
2. Claude tạo worktree và nhánh, symlink `node_modules`, rồi đưa phiếu vào làn Codex (`gpt-6.1-sol`, `xhigh`).
3. Khi Codex xong: Claude chạy Kiểm 6–12 của phiếu, gửi anh ảnh trước và sau.
