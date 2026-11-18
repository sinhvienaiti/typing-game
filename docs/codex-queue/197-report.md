# Phiếu 197 · Dragonhold · Màn tựa kiêm màn tải (DH-13)

**Hoàn tất mã và kiểm ngoại tuyến của 197.** `pnpm check` trước **568/568**, sau **593/593**; golden **10/10**, English UI **9/9**; `pnpm deploy:pack` **0 lỗi**. Màn tựa đã đứng trước thẻ tốc độ, nhận phím trong lúc tải, chặn Start theo bốn nguồn và báo lỗi bộ từ ngay trên màn tựa. **Chưa nghiệm thu hiển thị trên trình duyệt**, theo lệnh cấm của phiếu; Claude kiểm 1280/1920, nhận tranh 119 rồi commit.

## 1. Điều kiện chạy và phạm vi

Lượt 30/10, 11:42 áp dụng xác nhận điều phối rằng 194 và 195 đã xong; cổng vào là `pnpm check` mới trên worktree. Cổng này **mã 0, 65 file, 568/568 test**, kit 75 file, TypeScript và Vite xanh. Không dừng theo kết luận cũ trong báo cáo 194 hoặc báo cáo 197 trước đó. Giữ [báo cáo dừng cũ](197/previous-report.md), [điều kiện lượt này](197/prerequisites.json), [log trước](197/check-before.log).

Worktree `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD giữ **`6aa593a2dce6637cccbe24a58709b86f7127f607`**. Trạng thái đầu **36 đường dẫn**, đúng tập 187/194/195; **0 file lạ**. [Status đầu](197/resume2-start-status.txt), [diff đầu](197/resume2-start.diff), [hash đầu](197/resume2-before.json).

| Phiếu có sẵn | Đường dẫn chưa commit, tương đối với worktree |
| --- | --- |
| 187 | `README.md`, `src/app/app.ts`, `src/app/learning.ts`, `src/app/portal.ts`, `src/ui/results.ts`, `tests/app/portal.test.ts`, `tests/ui/results-screen.test.ts`, `vite.config.ts`, `docs/changelog/2026-10-29-portal-link.md`, `tests/portal-build.test.ts` |
| 194 | `README.md`, `package.json`, `scripts/ui-art/prepare.mjs`, `src/ui/debut-card.ts`, `src/ui/hud.ts`, `src/ui/learning-frame.ts`, `src/ui/placement-ui.ts`, `src/ui/results.ts`, `src/ui/skin.ts`, `src/ui/styles/dh.css`, `src/ui/ui-art.json`, `src/ui/wave-card.ts`, `tests/assets/ui-art.test.ts`, `tests/ui/results-screen.test.ts`, `tests/ui/ui-art.test.ts`, `docs/changelog/2026-10-30-ui-art-icons.md` |
| 195 | `src/app/app.css`, `src/app/app.ts`, `src/app/learning.ts`, `src/app/deck-boot.ts`, `src/app/idle-speed.ts`, `src/app/quality.ts`, `scripts/balance/idle-estimate.mjs`, `scripts/balance/idle-estimate.d.mts`, `tests/app/deck-app.test.ts`, `tests/app/deck-boot.test.ts`, `tests/app/idle-estimate.test.ts`, `tests/app/idle-speed.test.ts`, `tests/app/pinned-deck.test.ts`, `tests/app/quality.test.ts`, `docs/changelog/2026-10-30-deck-notice-and-idle-speed.md` |

Chỉ mở rộng bốn file trong tập có sẵn: `app.ts` để nối title/router; `prepare.mjs` và `ui-art.json` theo mục 1; `deck-app.test.ts` để kiểm hợp đồng router khởi tạo sớm và giữ kiểm Retry của 195 qua `title: false`. **32 file có sẵn còn lại giữ nguyên byte**. `learning.ts`, `deck-boot.ts`, chất lượng, tự tua, portal, CSS cũ và phần kết quả không sửa.

[19 đường dẫn của 197](197/files-197.txt) gồm mã, test, bảy file kịch bản và changelog. Status cuối **51 đường dẫn = 36 có sẵn + 15 đường dẫn mới xuất hiện trong status**; không có đường dẫn lạ. [Status cuối](197/status-final.txt), [kiểm bảo toàn](197/verification.json). Repo cha chỉ ghi báo cáo/thư mục `197`; trạng thái đồng thời của các làn khác không bị sửa hoặc hoàn tác.

## 2. Mười mục việc

| Mục | Kết quả |
| --- | --- |
| 1. Danh sách và xuất ảnh | `src/ui/ui-art.json` có `art` cạnh `icons`: `title-backdrop` 1536, `logo` 1024, `emblem` 512; nguồn đúng `ui/title-epic/*`, alt tiếng Anh, cả ba `accepted: null`. `scripts/ui-art/prepare.mjs` chỉ xuất mục đã nhận ra `ui/title/<name>.webp`, Lanczos, không phóng to, quality 90/alpha 100; ghi `art` vào manifest hiện có ở `ui/icons/manifest.json`. Có số đo, mã băm nguồn/đích và kiểm `--check`; stage dùng tên riêng, xuất manifest sau cùng, giữ rollback cho cả hai thư mục. |
| 2. Màn tựa | `src/ui/title.ts`, `src/ui/styles/title.css`: nền cover/cắt giữa, logo trong vùng 25–75% × 6–30%, menu 3–35% × 55–92%, huy hiệu nhỏ, Start, tiến độ/gợi ý, ba câu hướng dẫn. Bỏ dòng nạp `.dh-boot` cũ khỏi app; chỉ giữ một phần tử rời làm neo tương thích cho đường lỗi `title=0`. Start → thẻ tốc độ → begin; có WPM thì Start → begin. |
| 3. Cổng và cài đặt | Back to portal chỉ tạo khi `portalHome(VITE_PORTAL_URL)` khác null, `target="_top"`; biến trống không tạo nút hoặc ô trống. **Chưa có `src/app/quick.ts` của 192 trong worktree này**: chừa `.dh-title__quick`/`title.quickSlot`, rỗng thì ẩn, không đặt icon thay thế. |
| 4. Phím/chuột | Chuyển `createInputRouter` ra khỏi callback bộ từ, tạo trước `learning.buildDeck` ở `app.ts:921`. Title đi qua intercept có sẵn; không thêm listener keydown. Chỉ Enter, Esc, bốn action mũi tên hiện có; mũi tên đi vòng Start/cổng, Enter bấm đúng focus. Rê chuột/focus đổi cùng chỉ mục; chữ bị intercept nuốt; Esc giữ màn tựa. Start tắt vẫn giữ viền focus mặc định. |
| 5. Tiến độ | Đọc bốn promise có sẵn: bộ từ, `models.ready`, `map.groundBaked`, `heroes.ready`. Dòng status và progress 0–4; từng nguồn chỉ tính một lần. Ba nguồn đồ họa reject thì warn một lần/nguồn và vẫn hoàn tất; lỗi bộ từ dùng nguyên tiêu đề/dòng phụ của 195, Start giữ tắt, cổng vẫn hoạt động. Đường `title=0` giữ bảng lỗi/Retry của 195. |
| 6. Thiếu ảnh | Mục vắng/null không tạo yêu cầu ảnh. Error cũng về cùng cách xử lý: nền phẳng `#17130f`, chữ Dragonhold bằng Cormorant Garamond, huy hiệu ẩn; warn một lần/tên/màn. Không vẽ cảnh hoặc icon thay thế. Nút dùng da `.dh-btn` hiện có, chỉ đặt kích thước/bố cục và viền focus; **chờ phiếu gắn khung 162**. Không có mục loading từ 184 ở bảng hiện tại; nếu sau này có mục đã nhận, title dùng nó trong lúc tải. |
| 7. Móc R2 | Có `onShow`, `onHide` trả hàm gỡ; `isOpen`, `setBackdrop` nhận `art` hoặc `live`, mặc định art. Live ẩn tranh và bỏ nền đặc để thấy map. `app.ts:918` chỉ chừa chú thích cho R2, chưa gắn camera. `handle.state().title` có loading/ready/blocked/started. |
| 8. Bỏ qua cho kịch bản | `optionsFromUrl` đọc `?title=0`; thêm cờ vào boot chung và mọi URL `page.goto` viết thẳng. Không chạy kịch bản. Danh sách bên dưới. |
| 9. Tách file | Máy trạng thái thuần ở `src/ui/title-state.ts`; DOM ở `title.ts`; CSS mới được nạp từ `title.ts`. Không sửa `dh.css`, input-router, rules, sim, view hoặc kit. `app.ts` riêng 197 **+46/−26 dòng**, tổng 72 dòng thêm/xóa so với trạng thái đầu đã có 187/195; [diff riêng](197/app-197.diff). |
| 10. Test trước mã | Viết bốn file test mới trước triển khai; [lượt đỏ](197/tests-first.log): hai suite chưa có module, hai test URL/xuất ảnh đỏ. Sau triển khai **19/19 xanh**. Thêm sáu test tích hợp app trên loader/deck/world thật, renderer/audio giả: chặn lỗi bộ từ, chờ đủ bốn promise, hai luồng WPM, reject đồ họa và dispose. Sửa stub click thiếu preventDefault/stopPropagation được phát hiện ở lượt tích hợp; không sửa luật game. [Kiểm tập trung cuối](197/focused-final.log) **33/33**, gồm 4 test script 194 giữ nguyên. |

## 3. Tám mục kiểm

| Kiểm | Số và bằng chứng |
| --- | --- |
| 1. `pnpm check` | Trước **568/568**, 65 file; sau **593/593**, 69 file, **mã 0**; kit 75 file, TypeScript và Vite đạt. Tăng **25 test**. Không có test thời gian đỏ, không áp dụng ba lượt chạy riêng. [Trước](197/check-before.log), [sau](197/check-after.log), [mã thoát sau](197/check-after-run.json). |
| 2. Golden | **10/10 xanh** trong check; `tests/golden/m0.json` giữ SHA-256 `c0f9770cf32f033988576c0da8a17b7ae817b20c676a7ae3cd78ef2860562b82`. Cả bộ golden không đổi. |
| 3. English UI | **9/9 xanh** trong check. Mọi chuỗi mới liệt kê ở mục 4; chỉ proper name Hỏa Long giữ dấu. |
| 4. Gói production | `pnpm deploy:pack` **mã 0**, checker **0 lỗi**, **402 file**, **35.061.724 byte**, **0 localHost**, vocabulary ngoài gói **0**. [Log](197/deploy-pack.log), [mã thoát](197/deploy-pack-run.json), [JSON checker trên chính dist vừa dựng](197/deploy-pack.json). Vite còn cảnh báo chunk lớn như trước, không lỗi. |
| 5. Phạm vi/status | **51 đường dẫn** trong status được phân nhóm đầy đủ ở mục 1; `git diff --check` sạch. **32/32 file có sẵn không thuộc điểm nối giữ nguyên**; **7.540 file** bảo vệ (kit, sim, view, golden và ảnh/prompt nguồn) không đổi so với mốc kiểm. HEAD không đổi. Không có ảnh title trong public; không chép ảnh vào Git. |
| 6. Quét title | `grep -nE '<svg\|canvas\|gradient'` trên ba file title: **0 kết quả**, mã 1. Quét pictograph/emoji/FE0F: **0 kết quả**. [grep.txt](197/grep.txt). |
| 7. Dòng app/kịch bản | App **+46/−26**; dời router từ callback sau buildDeck lên trước lời gọi buildDeck. **7 file kịch bản** có thay đổi; Node kiểm cú pháp **7/7**, không thực thi scenario. |
| 8. Bàn giao trình duyệt | Có [hướng dẫn đầy đủ](197/browser-handoff.md): 1280×720 và 1920×1080, chuột/phím, có/không cổng, art null/119/error, ba loại lỗi bộ từ, state, điểm gắn 192/R2. **Chưa chạy và chưa nhận cảm quan**, đúng phân công Claude. |

Lượt chuẩn bị thật và `--check` đều mã **0**: [prepare.log](197/prepare.log), [prepare-check.log](197/prepare-check.log). **159/159 WebP icon giữ nguyên byte/mã MD5 so với inventory 194**. Manifest chỉ thêm `art: {}`; **0 mục art nhận, 0 WebP title, không tạo thư mục public title**. Fixture ảnh chỉ nằm trong `tmp/title-art-test/` và `tmp/ui-art-test/`, tự dọn sau test; không sửa ảnh nguồn. Không có frame/capture nên không cần prune.

Bảy file kịch bản (tương đối với worktree):

- `scripts/visual/scenarios/lib/dh.mjs`: boot chung thêm `title=0`.
- `scripts/visual/scenarios/dh-bench.mjs`: hai URL fx/crowd.
- `scripts/visual/scenarios/dh-camera.mjs`: URL terrain.
- `scripts/visual/scenarios/dh-map-shots.mjs`: URL terrain.
- `scripts/visual/scenarios/dh-models.mjs`: hai URL models.
- `scripts/visual/scenarios/dh-pace.mjs`: ba URL mở trực tiếp.
- `scripts/visual/scenarios/ui-preview.mjs`: URL UI.

Có **10 URL viết thẳng** được thêm cờ, cộng boot chung. `dh-map-bench.mjs` chỉ bọc goto rồi dùng boot chung nên không cần sửa. Claude chạy lại các kịch bản trên và các kịch bản dùng boot sau khi gộp; Codex không chạy.

## 4. Chuỗi người chơi thấy

- `Dragonhold`; `Start`; `Back to portal`; `Press Enter to start`.
- `Loading N of 4 · words`, `Loading N of 4 · models`, `Loading N of 4 · ground`, `Loading N of 4 · dragons` (N từ 0 đến 3; đủ bốn nguồn chuyển sang gợi ý Start).
- `Type the word over a foe and Hỏa Long breathes fire on it.`
- `Place traps, units and houses on the lanes during breaks.`
- `Keep Hỏa Long standing until the last wave ends.`
- Dùng lại ba chuỗi của 195: `Words could not load`; `Check your connection and try again.`; `Not enough words arrived for this stage.`
- Nhãn truy cập/alt: `Loading progress`; `Dragonhold`; `Dragonhold mountain stronghold at dawn`; `Dragonhold emblem`. Hai alt tranh chỉ được dùng khi ảnh được nhận.

Viền focus **3 px**, màu `#fff3ce`, có vòng nền đặc `#17130f` quanh viền; tỷ lệ tính từ màu khai báo **16,686:1**. Đây là số tương phản của viền với vòng nền, không phải nghiệm thu bằng ảnh chụp. Chữ/bố cục trên tranh và viền khi Start tắt còn cần Claude xem ở hai viewport.

## 5. Phần bỏ qua và chủ dự án/Claude cần xem

Không nhận 119 thay Claude; logo/huy hiệu còn ngoại lệ sắc khóa theo 119 §5. Ba cờ vẫn null. Không chờ 184, không sinh/chép/cắt/sửa tranh, không âm mới, không gắn icon giả, không camera tự quay hoặc bảng Settings mới. Không chạm game/worktree khác, Tu Tiên, kit, sim, view, rules, `dh.css`; không server, trình duyệt, mạng, build/test game khác, kit sync hoặc Git có ghi.

Claude duyệt [diff app riêng](197/app-197.diff), bốn điểm nối file có sẵn, rồi làm [kiểm trình duyệt](197/browser-handoff.md). Khi gộp 192, đặt xử lý bảng Settings/Sound trước nhánh intercept title để Esc đóng bảng, gắn hai nút vào quickSlot. R2 gắn camera qua móc. Sau quyết định nhận 119, đổi accepted và chạy lại prepare/--check. Nút chờ khung 162. Chỉ sau nghiệm thu trình duyệt và ảnh, Claude commit theo phân công; phiên này không commit hoặc push.
