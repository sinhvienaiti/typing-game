# Phiếu 259 (CX-C, vòng ngọc): tiến độ

**Cập nhật:** 04/11/2026, khoảng 13:50 (agent viết phiếu dừng theo hạn cứng 14:00 của anh).

**Trạng thái:** phiếu là **BẢN NHÁP, CHƯA XONG**. Chưa đủ quy trình duyệt hai lần, chưa đưa vào làn Codex.

## Đã xong
- Đọc kế hoạch (`INTEGRATION_PLAN_2026-11-04.md`: ghi chú đầu, §2.8, §3 CX-C, §4 "Vòng ngọc"), `SWORD_AURA.md` (Q4, `AuraAnchors`), mã `sword-material.ts`, `blades.ts`, `real-swords.ts`, `clear-wind-impostor.json`, kịch bản `lab-element-parity.mjs`, phiếu 255. Kiểm thứ tự chunk trong three.js 0.170 (`meshphysical.glsl.js` dòng 173–186).
- Xác định ảnh đã duyệt: `games/immortality-cultivation/art-src/weapons/clearwind-src3q.v4-try1.png` (nguồn Tripo của model). Đo màu trên vùng vòng: ngọc trắng trung vị `#DFDDDF`, vàng nhạt trung vị `#D4B793` (bảng và giá trị tuyến tính trong phiếu).
- Bản nháp phiếu đầy đủ các mục (lời giải, tệp và hàm, đường ghi, việc cấm, kiểm bắt buộc, báo cáo, model `gpt-6.1-sol` mức `xhigh`): `docs/codex-queue/259-tt-jade-ring-material.md`.
- ChatGPT (Chat, thinking High): brief đã gửi, trả lời lần đầu xong (34.365 ký tự). Chat: `https://chatgpt.com/c/6aead1ae-67e4-83ec-983f-339fe8bb6531`. Lượt tự duyệt 1 gửi lúc 13:45, kết quả `VERDICT: FAIL` (13:50); bản sửa đầy đủ đang viết dở khi dừng.
- Bản ghi ChatGPT tới lúc dừng: `docs/games/tu-tien/skills/source/jade-ring-chatgpt-2026-11-04.md` (đã lưu: brief, 4 lượt, lượt cuối chưa xong, bảng kiểm một phần). Bản ghi Gemini chưa có vì chưa bắt đầu.

## Chưa xong
1. ChatGPT: hai PASS liên tiếp (tối đa 4 lượt), rồi handoff. Mở lại đúng chat ở trên, đọc lượt tự duyệt 1 (chỉ dòng VERDICT), gửi tiếp lượt 2 theo mẫu `references/double-review.md` §2.
2. Gemini (4 Argon, High): chưa bắt đầu. Dán handoff của ChatGPT bằng nút Copy và Cmd+V, mẫu §3, hai PASS liên tiếp, handoff.
3. Lưu nguyên văn phần còn lại của hai chat bằng JS trang và bộ nhận cục bộ (form POST cùng tab; POST qua iframe ẩn bị CSP của ChatGPT chặn, `navigator.clipboard.writeText` bị từ chối).
4. Claude kiểm các ý chính, quyết ba chỗ ChatGPT khác bản nháp (cách đo vòng, bề rộng chỉ vàng và vành bạc, bán kính dọc của vòng trong impostor theo `rollWidth` hay `cos(roll)`), sửa "Lời giải đã chốt", bỏ dòng "BẢN NHÁP".
5. Trước khi chạy phiếu: Claude tạo worktree `games/.wt-immortality-cultivation-codex` nhánh `codex/jade-ring-material` từ `bc94110` (worktree của 255 đã gỡ), symlink `node_modules`.

## Ghi chú
- Codex không chạy được server hay trình duyệt, nên các kiểm có ảnh (vòng giữ ≥ 95 %, trùng khít ngoài vòng, màu, thời gian, ảnh trước và sau) là phần Claude chạy khi nhận; Codex viết công cụ `scripts/visual/ring-parity.mjs` và test không cần trình duyệt.
- Kiếm cầm tay trong lab (`src/lab/hand-sword.ts`) có vật liệu riêng, ngoài phạm vi phiếu này.
