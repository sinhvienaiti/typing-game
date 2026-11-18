# Phiếu 291 · Tu Tiên · Code: làm ấm đúng 2 chương trình bóng còn biên dịch muộn của Kim

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Phiếu rất ngắn theo luật làm gọn 05/11, không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/291-report.md`.

**Worktree:** `games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `672f2e7` (đã gộp main). `?? art-src`, `?? node_modules` là link của Claude: không đụng. **Không lệnh git ghi** (Claude commit sau).

## Vì sao
Đo 05/11 15:30 (`typing-game-review/captures/tu-tien/code-drawn/lot1/recheck-merge/`, số trong `docs/work/tasks/key1-fire.md`): Hỏa không còn biên dịch muộn. Kim còn **2 chương trình `MeshDepthMaterial`** ở khung ngay sau khung trúng: `USE_MAP + USE_SKINNING` và `USE_MAP + USE_INSTANCING`. Phiếu 286 đã thử làm ấm bóng cho một mesh skinned có map và một `InstancedMesh` có map, nhưng khóa chương trình **không khớp** với cái game dùng thật.

## Việc
1. Mở các tệp `stall-ids-*.json` (và số liệu liên quan) trong thư mục đo trên, xác định **khóa chương trình đầy đủ** của hai chương trình bóng (các define, kiểu bóng, `alphaTest`, `side`, số xương, `customDepthMaterial`, kiểu đèn/bóng…), và so với cái lượt làm ấm 286 đang tạo ra.
2. Sửa phần làm ấm chung (283/286) để tạo **đúng** hai biến thể đó lúc nạp (dùng chính vật liệu/mesh mà Kim dùng khi trúng, hoặc bản sao đủ thuộc tính khóa), rồi trả lại trạng thái cũ.
3. Thêm test: lượt làm ấm tạo ra hai khóa chương trình bóng trùng với khóa của mesh Kim thật (so `renderer.properties`/`programCache` hay hàm khóa tương đương trong môi trường test), và trạng thái được trả lại.

### Được ghi
`src/view/screen-fx.ts`, `src/view/renderer.ts`, `src/view/skills/element-stage.ts` (chỉ phần làm ấm), `src/lab/skills-main.ts` (chỉ phần làm ấm), `tests/view/skill-prewarm-shared.test.ts`, changelog `docs/changelog/2026-11-05-fire-lot1-art.md`, và `docs/codex-queue/291-report.md` ở repo cha.

### Cấm
Mọi lệnh git ghi; đổi hình, số, nhịp; sửa tệp khác; mở cổng mạng.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua (mốc 1028).
3. Build bằng bộ bọc 274 (thư mục `/private/tmp/codex-291-dist`); grep không thấy `fxcode`, `stripK`, `prewarmReport`; xóa thư mục build.

## Claude làm sau
Đo lại cổng 7 khi máy rảnh. Đạt thì commit và fast-forward `main` của game.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
