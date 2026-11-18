# Phiếu 259 (CX-C, vòng ngọc): tiến độ

**Cập nhật:** 04/11/2026, tối (sau phản biện lượt 4).

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

## Phản biện lượt 2 (agent Claude độc lập): FAIL, đã sửa
- Một lỗi, đúng sau khi Claude kiểm `UnrealBloomPass` và `LuminosityHighPassShader` của three 0.170.0 và `look.ts` của lab; chi tiết ở mục "Phản biện", lượt 2, cuối phiếu.
  - Kiểm 8 với bloom mặc định đòi "0 điểm ảnh khác ở xa hơn 16 px": bản đúng không đạt được. Bloom 5 mip lan khoảng 516 px; bỏ điểm lóe trên ngưỡng 1 của vòng cũ (đúng ý phiếu) làm điểm ảnh xa lật làm tròn.
  - Sửa: bloom 0 giữ "0 điểm ảnh khác ngoài mặt nạ giãn 3 px"; bloom mặc định chỉ ghi số điểm ảnh xa để tham khảo, thay bằng `__lab.bright()` cả khung có `pixels` và `sum` sau ≤ trước ở mọi khung. `MASK=1` ghi `bright` vào `shots-<PHASE>.json`, `ring-parity.mjs` ghép và ghi `bright.ok`, `box`. Mỗi cặp chạy một `OUT_DIR`.
- Đếm lại hai lượt PASS từ đầu; còn lượt 3 và 4, cả hai phải PASS.

## Phản biện lượt 3 (agent Claude độc lập): FAIL, đã sửa
- Hai lỗi về lệnh kiểm của Codex (cờ bắt buộc của Vitest và Vite qua symlink `node_modules`; Kiểm 4 với `?? node_modules`); chi tiết ở mục "Phản biện", lượt 3, cuối phiếu.

## Phản biện lượt 4 (agent Claude độc lập): FAIL, đã sửa
- Hai lỗi, cả hai đúng sau khi Claude kiểm mã của game và three 0.170.0; Claude thêm một chỗ tự thấy. Chi tiết ở mục "Phản biện", lượt 4, cuối phiếu.
  1. Cổng `bright.ok` cả khung của Kiểm 8 có thể đánh trượt bản làm đúng: lớp trong suốt đè lên đĩa (cổng "Chồng lớp" cho tới 2 lớp) mà đĩa cố ý sáng hơn, và bộ đệm sáng của bloom ở nửa độ phân giải trung bình 2 × 2. Sửa: `bright` chỉ còn để ghi; cổng mới `__lab.ringCap()` (mã đầy đủ ở §4) vẽ riêng kiếm ba lần (vòng tắt, bật, trọng số qua `uSwRingOn` = 2), đòi `over` = 0 với điểm ảnh nắp áp trọn trên độ sáng 0,96; mép mềm ghi riêng. `MASK=1` và `ring-parity.mjs` ghi `ringCap`.
  2. Nắp ăn cả ánh mép tan, nên mép tan trên đĩa không bloom trong khi trên lưỡi có. Sửa: ánh mép tan (`swRingDe`) nằm ngoài nắp; test kiểm dòng này.
  3. (Claude thêm) Nắp đo bằng hệ số 601, bloom đo bằng 709; viền k4 xanh ngọc qua ngưỡng. Sửa: nắp dùng (0,2126; 0,7152; 0,0722).
- Đếm lại hai lượt PASS từ đầu; lượt 5 và 6 đều phải PASS.

## Còn lại
1. Hai lượt PASS liên tiếp của agent phản biện Claude. Đã dùng 4 lượt, cả bốn FAIL và đã sửa, nên mức "tối đa 4 lượt" ghi trước đây đã hết: Claude chính quyết định chạy lượt 5 và 6 hay đi đường khác. FAIL thì sửa phiếu và đếm lại từ đầu.
2. Claude tạo worktree và nhánh, symlink `node_modules`, rồi đưa phiếu vào làn Codex (`gpt-6.1-sol`, `xhigh`).
3. Khi Codex xong: Claude chạy Kiểm 6–12 của phiếu, gửi anh ảnh trước và sau.
