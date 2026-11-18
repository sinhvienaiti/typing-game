# Bản nháp changelog · Phiếu 216 · 30/10/2026

Claude chép mục này vào file duy nhất `docs/changelog/2026-10-30.md` khi duyệt và commit; không tạo thêm changelog ngày khác cho cùng lượt.

## Nginx: ba game tự phục vụ bản từ vựng ghim

- Bỏ alias dữ liệu dùng chung khỏi các khối HTTPS `dragon.`, `td.`, `survival.` trong cả cấu hình play và dev. Trước đó nginx đè bản ghim của game bằng `shared/` của repo cha; sau thay đổi, Play đọc `dist/vocabulary/`, dev chuyển tới Vite phục vụ `public/vocabulary/`.
- Bỏ **16 location**: mỗi cấu hình Dragonhold −2, Wordwoven −3, Last Line −3. Các location dữ liệu bị cấm ở ba host: **16 → 0**; alias/root vào `__ROOT_DIR__/shared/` ở ba host: **16 → 0**.
- Bộ kiểm `validate-play-mode.mjs` import được mà không đọc file; nhận `--play-conf` và `--dev-conf`; chặn alias quay lại kể cả đổi tên đường, modifier, tab và `root`; kiểm ngoặc cùng số khối host. Giữ mọi kiểm cũ, chỉ bỏ yêu cầu hai route dùng chung của ba game đã tự phục vụ. Tu Tiên vẫn giữ yêu cầu cũ.
- Last Line giữ alias model Space cùng chú thích phiếu 205; sau khi 205 gộp, Claude bỏ block alias và yêu cầu tương ứng trong bộ kiểm.
- Kiểm: **94 đỏ trước → 94 xanh sau**, hai validator exit **0** trước và sau; mỗi cấu hình vẫn **11 server**; **16/16 khối ngoài phạm vi** giữ nguyên byte/SHA-256. Ba game khớp pin `18338405eebd9cfdbd6d6bf666ea79361c00a564`; public/dist khớp **103 / 8 / 6 file**, kể cả manifest; **0** chuỗi `typing-texts` trong nguồn ngoài kit và JS build.
- Chủ dự án chạy `pnpm setup:play` sau commit để áp dụng trên máy nhà; đang dev thì `pnpm setup:dev`. Không chạy cả script bằng sudo trên macOS. Lượt này chưa cài/reload nginx, chưa chứng minh G7 qua HTTP; thiếu file vẫn có nguy cơ nhận SPA index mã 200.

Báo cáo và số đo: `docs/codex-queue/216-report.md`, `docs/codex-queue/216/`.
