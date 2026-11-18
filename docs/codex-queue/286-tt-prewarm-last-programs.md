# Phiếu 286 · Tu Tiên · Code: làm ấm 3 chương trình shader còn biên dịch muộn

**Loại việc:** code phần nhìn (`gpt-6.1-sol`, mức `xhigh`). Phiếu rất ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/286-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `9434ac2` (đã có 283). Lúc giao chỉ có `?? art-src` và `?? node_modules` (link của Claude): không đụng.

## Vì sao
Claude đo sau 283 (05/11 11:20, số trong `typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-283/`: `gate7.json`, `stall-ids-*.json`):
- Khung bấm phím 11–15 ms, khung trúng đầu 9–14 ms. Ngưỡng là 11,5 ms; trước 283 là 235 ms và 108 ms.
- Còn 3 chương trình shader biên dịch muộn:
  1. ở khung trúng, cả Hỏa và Kim: một chương trình `ShaderMaterial`, nhiều khả năng là shader mặt nạ va chạm hoặc mặt nạ qi slash trong `src/view/screen-fx.ts` (lấy đúng id trong `stall-ids-*.json`);
  2. ở khung ngay sau đòn trúng của Kim: hai chương trình bóng đổ, `MeshDepthMaterial` hoặc `MeshDistanceMaterial` cho mesh **skinned có map** và mesh **instanced có map**.

## Việc
1. **Mở `stall-ids-*.json`** để biết đúng chương trình nào. Thêm vào hàm prewarm phần chung (283) để biên dịch đúng ba chương trình đó lúc nạp:
   - shader của `screen-fx`: hiện tạm vật thể dùng nó trong lần `compile` / vẽ ngoài màn hình của 283;
   - bóng đổ: trong lần vẽ ngoài màn hình, bật đổ bóng cho một mesh skinned có map và một `InstancedMesh` có map, để three biên dịch biến thể bóng của chúng; xong thì trả lại như cũ.
2. **Không đổi hình, số hay nhịp.** Không thẻ nào còn sống sau prewarm.

### Được ghi
`src/view/screen-fx.ts`, `src/view/renderer.ts`, `src/view/skills/element-stage.ts` (chỉ phần prewarm), `src/lab/skills-main.ts` (chỉ phần prewarm), `tests/view/skill-prewarm-shared.test.ts`, changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, và `docs/codex-queue/286-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua. Mốc là 1006.
3. Test: prewarm có bật bóng cho một mesh skinned và một mesh instanced, và trả lại trạng thái cũ sau khi xong.
4. Build bằng bộ bọc 274 (thư mục `/private/tmp/codex-286-dist`); xóa thư mục build.
5. `git status --short` chỉ có các tệp được ghi.

## Claude làm sau
Đo lại cổng 7 cho Hỏa và Kim. Đạt thì commit, rồi gộp nhánh vào main của game.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
