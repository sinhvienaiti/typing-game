# Phiếu 236 · Admin nhiều khu · G5

**Phần mã G5 đã triển khai; nghiệm thu trình duyệt còn thiếu do sandbox chặn mở cổng localhost (`EPERM`). Chưa thể kết luận G5 đã qua đủ cổng nghiệm thu.**

Làm tại worktree `admin-ia`, nhánh `admin-shared-ia`. Lần kiểm đầu tiên: `git status --short -uall` trống; hai cổng 3199 và 3100 không có listener. Đầu ra trạng thái sạch được lưu nguyên dạng rỗng ở `236/status-before.txt`. Không chạy lệnh Git ghi; không mở repo chính, không sửa game, media, Typing Feel hay game-kit.

## Kết quả

- Tái sử dụng Portal Admin V2, tên **Typing Game Admin**; hai khu **All games** và **Space Typing**, nút chọn khu, breadcrumb theo khu. Giữ giao diện tối và font Exo 2 / Be Vietnam Pro hiện có.
- `/admin` chuyển bằng `history.replaceState` tới `/admin/shared`. Ba URL Media, Roles và Typing Content cũ chuyển qua bảng trong `normalizedAdminPath`; query và hash được giữ. `NAV_ALIASES` chỉ còn làm sáng mục của trang con.
- All games chỉ có Overview và Learning Content. Overview đọc bốn consumer từ JSON, trạng thái hiện tại đều “Not yet · local copy”; catalogue chưa có thì hiện “Not imported yet”. Khi có manifest `typing-feel/catalogue-3`, số bộ lấy từ mảng **profiles**, revision lấy từ **revision** (§4.3).
- Learning Content dùng lại trang chỉ đọc hiện có, đọc nguồn chung. API mới có token; API cũ là bí danh. Bỏ hai nút dẫn từ trang này về History và Worlds & Stages để dùng được độc lập với Space.
- Administration có Media Library và Roles & Permissions ở cuối thanh bên của cả hai khu. Không hiện Audit và các trang G6.
- Server khởi động phần dùng chung và Media V2 trước; 13 hợp đồng, revision store, music service và bootstrap Space nằm trong khối bắt lỗi. Khi phần Space không khởi tạo được, các API Space trả 503 với mã quy định; Media V2, actor dùng chung, Overview và Learning Content tiếp tục hoạt động.
- `TYPING_GAME_ADMIN_SPACE_DIR` áp dụng cho hợp đồng, bootstrap, MusicAssetService và cả chín module xem trước đọc Space.
- Thêm `shared.publish`, đánh dấu nguy hiểm, có trong Super Admin và Publisher theo §3.13; chưa có thao tác G5 dùng quyền này. Các kiểm quyền cũ vẫn xanh.
- nginx chỉ đổi tiền tố proxy Admin và thêm location runtime Typing Feel; Vite chỉ thêm proxy tương ứng. Không thêm block host feel.

## Kiểm trước và sau

Số trong ngoặc là **mã thoát**. Toàn bộ đầu ra nằm trong các file `before-*` và `after-*` ở `236/`.

| Lệnh | Trước | Sau |
|---|---|---|
| `pnpm --dir portal build` | Xanh (0) | Xanh (0), tsc và Vite |
| `pnpm --dir portal test` | 129/129 (0) | 129/129 (0) |
| `pnpm admin:test` | 46/47 (1) | 50/51 (1); bốn ca mới xanh |
| `node scripts/validate-space-admin-alternative-modes.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-duel.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-events.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-qa.mjs` | Đỏ (1) | Đỏ (1) |
| `node scripts/validate-space-admin-phase-b.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-ranked.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-ui-assets.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-v2-design-system.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-ui.mjs` | Đỏ (1) | Xanh (0) |
| `node scripts/validate-space-admin-v2-media.mjs` | Xanh (0) | Xanh (0) |
| `node scripts/validate-space-admin-v2-shell.mjs` | Đỏ (1) | Xanh (0) |
| `node scripts/validate-play-mode.mjs` | Xanh (0) | Xanh (0) |
| `node --test scripts/validate-play-mode.test.mjs` | 94/94 (0) | 94/94 (0) |
| `pnpm admin:ia:validate` | Chưa có | Xanh (0): 2 khu, 26 mục, 39 URL cũ |
| `git diff --check` | Worktree sạch; không đo riêng | Xanh (0) |
| Khởi động Admin 3199 để chụp | Chưa chạy | Bị chặn `listen EPERM` (1) |
| Khởi động Vite 3100 để chụp | Chưa chạy | Bị chặn `listen EPERM` (1) |
| Chrome/CDP, hai kích thước, hai trạng thái Space | Chưa đo | Chưa chạy; không có mã thoát hay ảnh |
| Prune, xem trước rồi `--apply` | Chưa chạy | Cả hai (0), 0 ảnh, 0 byte bị xoá |

`admin:test` vẫn chỉ đỏ ca **pinned Space Typing runtime tree bootstraps without binary copies or duplicate versions**: thiếu media runtime trong checkout Space (11/22 bundle ship3D). Không đổi ca này để che lỗi. `qa` vẫn đỏ vì audited SHA `22a35dd2…` khác pinned Space `84777155…`; không sửa SHA ghim. Không thêm script đỏ mới: từ 8/11 lên **10/11**.

Bốn ca mới chạy trực tiếp listener HTTP thật của server qua `server.emit("request", …)`, dùng request/response trong bộ nhớ và thư mục dữ liệu tạm; không giả nội dung trả về. Chúng kiểm cả có/thiếu Space, token, Overview, catalogue chung và bí danh cũ, actor/quyền, 503 của Admin/runtime Space, Media V2 và manifest catalogue có/không có. Đây là kiểm handler và khởi tạo, **không thay thế kiểm socket/proxy hay trình duyệt**. Bộ kiểm IA thực thi registry, bảng chuyển đường và hai router thật, thay renderer DOM lá bằng stub; không chứng minh giao diện đã vẽ đúng.

## Kết luận về `ui` và `v2-shell`

Đã đọc lịch sử cả script lẫn điều hướng; bằng chứng ở `236/navigation-history.txt`.

- `37e94707` (15/10): đưa Shop và Roles trở lại điều hướng quản trị. `a67d164e` cùng ngày đã cập nhật `ui`, nhưng `v2-shell` vẫn giữ luật A2 cấm Shop và đòi Shop trong Developer Tools. **Script cũ**, không phải điều hướng cũ. Sửa nó để kiểm Shop là workflow chính, vẫn cấm các inspector kỹ thuật khác và giữ kiểm quyền Developer Tools.
- `9035d3bf` (18/10): tách Players & Live Ops, thêm Players/Mail/Chat/Feedback và đổi tên mục sự kiện thành **Events (read-only)**. `ui` vẫn đòi nhãn **Live Ops** cũ. **Script cũ**. Cập nhật theo nhãn hiện có; bảng 31 URL Phase B cũ vẫn giữ nguyên, Learning Content được kiểm tại khu chung và trong bộ kiểm IA mới.
- Sau khi bỏ chặn Shop, `v2-shell` còn bắt nhầm câu mô tả “no placeholder metrics” trong Dashboard như dữ liệu giả. Rút gọn câu mô tả Dashboard thành thông tin có ích cho người vận hành; giữ nguyên kiểm không dùng số liệu giả.
- Cập nhật cả 11 script để đọc shell và các module khu mới; giữ kiểm router, hợp đồng, quyền, media và metadata cũ. Kiểm tooltip phân biệt `document.title` với thuộc tính native `.title` trên control.

## Trình duyệt: phần còn thiếu và cách chạy tiếp

Đã thử đúng Admin 3199 với `TYPING_GAME_ADMIN_DATA_DIR=<worktree>/tmp/236-admin-data`, token mặc định, và `pnpm --dir portal dev`. Cả hai tự thoát mã 1 do sandbox từ chối `listen` trên 127.0.0.1. Chính sách phiên này không cho xin nâng quyền. Không tìm cách vượt sandbox hoặc dùng server đang chạy của repo chính. Không có tiến trình mình mở còn sống; kiểm cổng cuối vẫn trống.

Vì vậy **không có contact sheet**, ảnh thô, URL cuối, breadcrumb hay lỗi console được đo trong Chrome. `236/browser-results.json` ghi rõ từng tổ hợp URL/kích thước/trạng thái là `not-run`, các trường quan sát là `null`. Chưa quan sát trực tiếp được bố cục 1280×800/1920×1080, tương tác chọn khu, bảng lệnh, hay thông báo thiếu Space trên màn hình.

Đã chuẩn bị `236/browser-scenario.mjs` cho runner CDP hiện có. Khi môi trường cho phép:

1. Kiểm lại hai cổng trống; bật Admin với biến cổng và data dir nêu trên, bật `pnpm --dir portal dev`.
2. Từ gốc worktree, chạy `node tools/audio-lab/board/tools/cdp-run.mjs docs/codex-queue/236/browser-scenario.mjs --width=1280 --height=800`. Kịch bản tự chạy cả hai kích thước, 10 URL, chụp dưới `tmp/236/`, ghi JSON ở `236/browser-present.json`, thử chọn khu và bảng lệnh qua chuột/phím CDP.
3. Dừng riêng Admin vừa mở, bật lại cùng cổng/data dir với `TYPING_GAME_ADMIN_SPACE_DIR=<worktree>/tmp/236/absent-space`. Chạy cùng lệnh với `SPACE_MISSING=1` để ghi `236/browser-missing.json`.
4. Xem ảnh thật, ghép **một contact sheet** vào `236/` bằng ImageMagick và Arial theo phiếu; đối chiếu lỗi console/ngoại lệ. Dừng riêng hai server vừa mở. Chạy prune xem trước rồi `--apply`, giữ JSON và contact sheet. Cập nhật kết luận nghiệm thu sau khi đo đủ.

## Để lại và các lựa chọn phải suy đoán

- G6: chưa làm TypingFeelRevisionStore, Draft/Publish/Rollback, Keyboard Sounds, Typing Effects, Release & History, hay xuất bản dữ liệu. G7 Format chưa làm. Audit riêng chưa có nên không hiện.
- Catalogue thực chưa có trong worktree; dùng đúng mẫu §4.3 để đọc `profiles` và kiểm bằng fixture trong thư mục hệ thống tạm, không tạo `typing-feel/` ở repo.
- Bí danh API Typing Content cũ vẫn hoạt động khi thiếu Space: hiểu yêu cầu giữ bí danh và tách nội dung chung là ngoại lệ bổ sung có chủ đích, bên cạnh ngoại lệ Media V2.
- Thêm `/api/admin/shared/actor` để Roles và kiểm quyền dùng chung không gọi API Space đang 503. Giữ `/api/admin/space-typing/actor` cho client cũ khi có Space.
- Các trang Administration dùng breadcrumb **Administration / …**; khi mở trực tiếp, selector mặc định All games. Không tạo khu Administration thứ ba trong registry.
- Bất kỳ lỗi khởi tạo phần Space nào đều hạ riêng khu Space xuống trạng thái 503, đồng thời ghi nguyên nhân vào stderr. Không chỉ bắt ENOENT, đúng yêu cầu bọc toàn bộ phần khởi động.
- Trong G5, `consumers.json` là danh sách khai báo trạng thái hiện tại, không phải phép thăm dò trực tiếp từng game. Không truy cập host game hay mạng ngoài máy.
- Hạng mục chủ dự án cần xem: hoàn tất Chrome/CDP và contact sheet; duyệt bố cục/nút chọn khu ở hai kích thước. Chưa nhận nghiệm thu trực quan từ chủ dự án.

## File đã sửa hoặc tạo

- `admin/admin-security.mjs`: Thêm quyền shared.publish nguy hiểm, Super Admin và Publisher.
- `admin/boss-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/enemy-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/equipment-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/music-assets.mjs`: Cho phép chọn childRoot/SPACE_DIR thay vì ghim checkout Space.
- `admin/server.mjs`: Tách khởi tạo Space, guard 503, API chung, bí danh nội dung, export server để kiểm listener không mở socket.
- `admin/shared-ia.test.mjs`: Bốn ca Node cho trạng thái Space, nội dung chung, Media V2, catalogue và quyền.
- `admin/shared-overview.mjs`: Đọc consumer và catalogue Typing Feel nếu đã import.
- `admin/ship-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/shop-config-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/skill-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/stage-config-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/typing-feel/consumers.json`: Bốn game/host và trạng thái chưa đọc Typing Feel.
- `admin/world-music-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `admin/world-registry-preview.mjs`: Dùng TYPING_GAME_ADMIN_SPACE_DIR cho checkout chạy xem trước.
- `docs/codex-queue/236-report.md`: Báo cáo tiếng Việt, kết quả và giới hạn nghiệm thu.
- `docs/codex-queue/236/after-admin-ia.txt`: Đầu ra nguyên văn kiểm sau sửa: admin-ia.
- `docs/codex-queue/236/after-admin-test.txt`: Đầu ra nguyên văn kiểm sau sửa: admin-test.
- `docs/codex-queue/236/after-alternative-modes.txt`: Đầu ra nguyên văn kiểm sau sửa: alternative-modes.
- `docs/codex-queue/236/after-duel.txt`: Đầu ra nguyên văn kiểm sau sửa: duel.
- `docs/codex-queue/236/after-events.txt`: Đầu ra nguyên văn kiểm sau sửa: events.
- `docs/codex-queue/236/after-phase-b.txt`: Đầu ra nguyên văn kiểm sau sửa: phase-b.
- `docs/codex-queue/236/after-play-mode-test.txt`: Đầu ra nguyên văn kiểm sau sửa: play-mode-test.
- `docs/codex-queue/236/after-play-mode.txt`: Đầu ra nguyên văn kiểm sau sửa: play-mode.
- `docs/codex-queue/236/after-portal-build.txt`: Đầu ra nguyên văn kiểm sau sửa: portal-build.
- `docs/codex-queue/236/after-portal-test.txt`: Đầu ra nguyên văn kiểm sau sửa: portal-test.
- `docs/codex-queue/236/after-qa.txt`: Đầu ra nguyên văn kiểm sau sửa: qa.
- `docs/codex-queue/236/after-ranked.txt`: Đầu ra nguyên văn kiểm sau sửa: ranked.
- `docs/codex-queue/236/after-ui-assets.txt`: Đầu ra nguyên văn kiểm sau sửa: ui-assets.
- `docs/codex-queue/236/after-ui.txt`: Đầu ra nguyên văn kiểm sau sửa: ui.
- `docs/codex-queue/236/after-v2-design-system.txt`: Đầu ra nguyên văn kiểm sau sửa: v2-design-system.
- `docs/codex-queue/236/after-v2-media.txt`: Đầu ra nguyên văn kiểm sau sửa: v2-media.
- `docs/codex-queue/236/after-v2-shell.txt`: Đầu ra nguyên văn kiểm sau sửa: v2-shell.
- `docs/codex-queue/236/before-admin-test.txt`: Đầu ra nguyên văn kiểm trước sửa: admin-test.
- `docs/codex-queue/236/before-alternative-modes.txt`: Đầu ra nguyên văn kiểm trước sửa: alternative-modes.
- `docs/codex-queue/236/before-duel.txt`: Đầu ra nguyên văn kiểm trước sửa: duel.
- `docs/codex-queue/236/before-events.txt`: Đầu ra nguyên văn kiểm trước sửa: events.
- `docs/codex-queue/236/before-phase-b.txt`: Đầu ra nguyên văn kiểm trước sửa: phase-b.
- `docs/codex-queue/236/before-play-mode-test.txt`: Đầu ra nguyên văn kiểm trước sửa: play-mode-test.
- `docs/codex-queue/236/before-play-mode.txt`: Đầu ra nguyên văn kiểm trước sửa: play-mode.
- `docs/codex-queue/236/before-portal-build.txt`: Đầu ra nguyên văn kiểm trước sửa: portal-build.
- `docs/codex-queue/236/before-portal-test.txt`: Đầu ra nguyên văn kiểm trước sửa: portal-test.
- `docs/codex-queue/236/before-qa.txt`: Đầu ra nguyên văn kiểm trước sửa: qa.
- `docs/codex-queue/236/before-ranked.txt`: Đầu ra nguyên văn kiểm trước sửa: ranked.
- `docs/codex-queue/236/before-ui-assets.txt`: Đầu ra nguyên văn kiểm trước sửa: ui-assets.
- `docs/codex-queue/236/before-ui.txt`: Đầu ra nguyên văn kiểm trước sửa: ui.
- `docs/codex-queue/236/before-v2-design-system.txt`: Đầu ra nguyên văn kiểm trước sửa: v2-design-system.
- `docs/codex-queue/236/before-v2-media.txt`: Đầu ra nguyên văn kiểm trước sửa: v2-media.
- `docs/codex-queue/236/before-v2-shell.txt`: Đầu ra nguyên văn kiểm trước sửa: v2-shell.
- `docs/codex-queue/236/browser-admin-start.txt`: Lỗi EPERM khi mở server 3199.
- `docs/codex-queue/236/browser-results.json`: 40 tổ hợp trình duyệt chưa chạy, ghi nguyên nhân và trường quan sát null.
- `docs/codex-queue/236/browser-scenario.mjs`: Kịch bản CDP sẵn để chạy tiếp, chưa thực thi.
- `docs/codex-queue/236/browser-vite-start.txt`: Lỗi EPERM khi mở Vite 3100.
- `docs/codex-queue/236/checks-after.json`: Lệnh và mã thoát sau sửa.
- `docs/codex-queue/236/checks-before.json`: Lệnh và mã thoát trước sửa.
- `docs/codex-queue/236/diff-check.txt`: Đầu ra git diff --check, rỗng khi xanh.
- `docs/codex-queue/236/navigation-history.txt`: Lịch sử script và điều hướng dùng để quyết định bên cũ.
- `docs/codex-queue/236/ports-after.txt`: Kiểm cuối: hai cổng không có listener.
- `docs/codex-queue/236/prune-apply.txt`: Prune apply: không xoá ảnh nào.
- `docs/codex-queue/236/prune-dry-run.txt`: Prune xem trước: không có ảnh thô.
- `docs/codex-queue/236/status-after.txt`: Trạng thái worktree cuối sau kiểm diff.
- `docs/codex-queue/236/status-before.txt`: Trạng thái worktree sạch ở lần kiểm đầu, file rỗng.
- `infra/nginx/typing-game.local.play.conf`: Chỉ sửa proxy /api/admin/ và thêm /api/runtime/typing-feel/.
- `package.json`: Chỉ thêm admin:ia:validate và ca kiểm vào admin:test.
- `portal/src/admin/admin-shell.css`: Bố cục selector và bảng Overview dùng token/component hiện có.
- `portal/src/admin/admin-shell.ts`: Vỏ V2 chung, selector, breadcrumb, bảng chuyển đường và trạng thái thiếu Space.
- `portal/src/admin/api.ts`: getActor dùng API actor chung để chạy khi thiếu Space.
- `portal/src/admin/areas/registry.ts`: Registry hai khu thật và Administration dùng chung.
- `portal/src/admin/areas/shared.ts`: Chỉ đăng ký Overview và Learning Content đã có renderer.
- `portal/src/admin/areas/space-typing.ts`: Giữ nhóm Space và router V2/Phase B; dời ba mục dùng chung.
- `portal/src/admin/areas/types.ts`: Kiểu khu, nhóm điều hướng và context renderer.
- `portal/src/admin/shared-overview.ts`: Overview chỉ đọc với bảng game, catalogue và trạng thái lỗi/retry.
- `portal/src/admin/space-typing-command.ts`: Thêm lệnh All games/Administration và mở shortcut trên toàn Admin.
- `portal/src/admin/space-typing-typing-content-phase-b.ts`: Đổi Learning Content, API chung và nút quay lại khu All games.
- `portal/src/admin/space-typing.ts`: Dời mã sang admin-shell.ts và các module khu; không giữ vỏ Space thứ hai.
- `portal/src/admin/v2/dashboard.ts`: Rút gọn câu mô tả; không đổi nguồn dữ liệu Dashboard.
- `portal/src/main.ts`: Dùng shell mới, route /admin/*, nút Admin, phục hồi title Portal khi rời Admin.
- `portal/vite.config.ts`: Chỉ thêm proxy runtime Typing Feel.
- `scripts/validate-admin-shared-ia.mjs`: Kiểm thực thi registry/router, chuyển đường, Administration, 39 URL cũ và nút Portal.
- `scripts/validate-play-mode.mjs`: Chỉ đổi chuỗi location bắt buộc thành /api/admin/.
- `scripts/validate-space-admin-alternative-modes.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-duel.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-events.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-phase-b.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-qa.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-ranked.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-ui-assets.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-ui.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-v2-design-system.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-v2-media.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.
- `scripts/validate-space-admin-v2-shell.mjs`: Cập nhật nguồn shell/khu mới và giữ ý kiểm; điều chỉnh tên/đường đã dời khi cần.

## Sửa sau phản biện (Claude, 31/10)

Sửa đủ chín điểm phản biện (P2-a…d, P3-a…e) trong worktree `admin-ia`. Không chạy lệnh Git ghi; không đụng repo chính, `games/**`, `typing-feel/`, `shared/game-kit`.

- **P2-a.** Thêm `GET /api/admin/shared/status` (có token) trả `{ spaceAvailable, spaceStatus }`, không đọc file Typing Feel. Vỏ Admin chỉ gọi route này trước trang Space; route lỗi thì vẫn vẽ trang Space, để chính API của trang báo lỗi. `readSharedOverview` trả lỗi file thành dữ liệu: không có manifest → `null`; manifest hỏng → `{ status: "invalid", message }`; thiếu hoặc hỏng `consumers.json` → `consumers: []` kèm `consumersError`. Ô Overview hiện "Catalogue unreadable", bảng game hiện "Game list unreadable".
- **P2-b.** Chỉ báo "not checked out" khi không có `contracts/space-typing-admin.v1.json` dưới `TYPING_GAME_ADMIN_SPACE_DIR`. Lỗi khởi động khác thì `spaceStatus: "failed"`, 503 `{ "error": "space-typing-unavailable" }`, `console.error` kèm stack. Vỏ hiện "Space Typing failed to start — see the Admin server log".
- **P2-c.** Media Library và Roles giữ khu đang đứng. Khu cuối nằm trong trường riêng (`AdminAreaMemory`) và sessionStorage, có try/catch. Mở thẳng thì về All games. Breadcrumb vẫn là "Administration / …".
- **P2-d.** `validate-play-mode.mjs` đòi đúng block `location /api/admin/ {` và `location /api/runtime/typing-feel/ {`, cả hai đứng trước SPA fallback. Thêm 3 ca test, trong đó có ca chỉ có block hẹp `/api/admin/space-typing/` và phải đỏ. Chỉ sửa đoạn kiểm location để lúc gộp với repo chính không vướng.
- **P3-a.** Learning Content có lại nhãn phân loại "NO VISUAL PREVIEW / N/A" và cổng quyền.
- **P3-b.** Bảng lệnh tìm "Typing Content" ra Learning Content.
- **P3-c.** Nút chọn khu có `role="group"`.
- **P3-d.** Logo đổi thành "TG".
- **P3-e.** Phần chặn `listen` so sánh `realpathSync` của cả hai đường, nên chạy qua đường symlink vẫn mở cổng.

**Kiểm sau sửa:**

| Lệnh | Kết quả |
|---|---|
| `pnpm --dir portal build` | xanh, mã 0 |
| `pnpm --dir portal test` | 129/129 |
| `pnpm admin:test` | 53/54; chỉ đỏ ca bootstrap media Space đã ghim, như mốc |
| 11 script `validate-space-admin-*` | 10/11; `qa` đỏ vì SHA ghim cũ, như mốc |
| `pnpm admin:ia:validate` | xanh, có thêm kiểm nhớ khu, probe status, nhãn, bảng lệnh, `role`, logo |
| `node scripts/validate-play-mode.mjs` | xanh |
| `node --test scripts/validate-play-mode.test.mjs` | 97/97 |
| `git diff --check` | xanh |

**Trình duyệt.** Admin chạy cổng 3291, data dir `tmp/fix236-data`. Portal là `portal/dist`, phục vụ ở cổng 3292 có proxy. Đã thử sáu tình huống:
- có Space;
- thiếu Space;
- Space hỏng;
- catalogue hỏng và thiếu `consumers.json` trong một gốc nháp: trang Ships và Equipment vẫn vẽ;
- probe status lỗi;
- chạy qua đường symlink ở cổng 3293.

Media và Roles mở từ thanh bên Space vẫn giữ khu Space, kể cả sau khi tải lại. Không có lỗi console. Chi tiết ở `236/fix-browser-results.json`. Không ghi ảnh ra đĩa, nên không cần prune. Đã tắt cả ba server, các cổng đều trống.

- Claude (31/10, sau kiểm lại): mở link cũ `/admin/space-typing/media` hoặc `/roles` thì trang Administration giữ khu Space Typing (`AdminAreaMemory.remember`), vì link đó đến từ Space. Portal build xanh, 129/129 test, `admin:ia:validate`, `ui`, `v2-shell` xanh.
