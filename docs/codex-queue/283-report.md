# Báo cáo phiếu 283 · Làm ấm phần chung của lab kỹ năng

**Đã hoàn tất phần mã và kiểm tự động.** TypeScript qua; **1006/1006 test, 93/93 tệp** qua; build wrapper 274 qua, không có `prewarmReport` trong bundle và đã xóa build. **Chưa xác nhận ngưỡng GPU ≤ 11,5 ms**: Claude đo lại cổng 7 cho Hỏa và Kim theo phiếu. Chưa commit hoặc gộp.

Worktree `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-fire-lot1`, nhánh `codex/fire-lot1-art`, HEAD `fe47341`. Lúc nhận chỉ có hai link `?? art-src`, `?? node_modules`; giữ nguyên.

## Tệp đã ghi

Các đường dưới tính từ worktree, trừ báo cáo này ở repo cha:

| Tệp | Thay đổi |
| --- | --- |
| `src/lab/skills-main.ts` | Giữ Promise nạp ảnh cho prewarm; đợi ảnh/font/media; gọi cùng prewarm cho Hỏa và Kim, khôi phục nguyên tố ban đầu; thêm `__lab.prewarmReport()`. |
| `src/view/screen-fx.ts` | Thêm upload mặt nạ impact trong đường prewarm. |
| `src/view/hitfx.ts` | Thêm prewarm atlas số thật và một glyph tuổi 0 bằng trường số riêng; giữ atlas để vẽ sau. |
| `src/view/renderer.ts` | Thêm `prewarmScene()`: upload sampler, compile scene và vẽ một khung 64×64; khôi phục trạng thái, giải phóng target; trả hồ sơ texture/chương trình. |
| `src/view/skills/element-stage.ts` | Thêm điểm vào prewarm có tham số kit, dùng chung cho Hỏa/Kim. |
| `tests/view/skill-prewarm-shared.test.ts` | Sáu ca với renderer giả đếm lệnh, pool và vật liệu thật, texture trong bộ nhớ. |
| `docs/changelog/2026-11-05-fire-lot1-art.md` | Ghi bổ sung 283 và kết quả kiểm. |
| `docs/codex-queue/283-report.md` ở repo cha | Báo cáo này. |

Không cần sửa `element-fire.ts`: hàm 280 đã chờ đầy đủ thư viện Hỏa, brush và dải riêng. Không sửa hoặc nới test cũ.

## Tài nguyên và cách làm ấm

- **Mặt nạ:** `skills-main.ts` tạo `burst-star-mask.png`, `slash-crescent-mask.png` và ba mặt nạ impact khác. `ScreenFx` giữ chúng; `MyriadSwordsFx` dùng mặt nạ crescent cho `QiSlash`. Nay lab giữ Promise nạp ảnh, đợi trước prewarm và gọi `initTexture` cho các mặt nạ đã nạp.
- **Bóng đổ:** các kiếm instanced được tạo ở `skills/blades.ts` với `castShadow`, nhưng count ban đầu bằng 0 nên prewarm compile cũ không chạy đường shadow map. Ngoài ra scene có depth material riêng ở `lab/hand-sword.ts` và `lab/herd.ts`. Nay các mesh tạm hiện, kiếm rỗng có một instance ma trận hữu hạn, và lượt render scene thật đi qua shadow map. Không sửa các tệp tạo kiếm/quái hoặc shader bóng đổ.
- **Số sát thương:** `IcNumberSprites` trong `hitfx.ts` tạo `CanvasTexture` 1024×256, trước đây chỉ khi `SkillNumbersImpl.draw()` gặp số đầu tiên. Nay tạo sau khi font xong; một glyph được đưa vào cùng scene prewarm, atlas được tải qua `initTexture` và dùng lại khi đánh thật.
- **Lượt vẽ:** mỗi lần `ElementStage.prewarm(kit, …)` compile scene có ánh sáng/sương thật cho cả màn hình và HDR, rồi gọi `renderer.render(scene, camera)` **đúng một lần** vào target **64×64** sao chép buffer bloom, gồm type/format/colorSpace/samples. Lab có **hai lượt**, một cho mỗi nguyên tố, trước `__lab.ready`; sau đó trả lại nguyên tố đã chọn.
- **Bảo toàn:** mẫu thẻ tuổi 0 chỉ nằm tạm trong attribute/instance GPU; không gọi cast, emit hoặc update của pool. Không đổi đồng hồ, RNG, audit hoặc sim; không yêu cầu âm thanh. Dữ liệu, count, visibility, culling, draw range, uniform và render target được trả lại bằng `finally`; mẫu số được gỡ, target được dispose. Pool vốn rỗng vẫn có count 0, không xóa thẻ đang sống nếu gọi lại.

`__lab.prewarmReport()` trả một mảng hai hồ sơ, tìm theo `element: "fire" | "metal"`. Mỗi hồ sơ có:

- `textures`: ID Three.js và tên/URL texture đã upload trong lượt đó;
- `programs`: bản chụp chương trình đang được renderer giữ sau prewarm (`id`, `name`, `cacheKey`), gồm cả chương trình đã có từ các prewarm trước;
- `objects`: tên vật thể, ID vật liệu và cờ đổ bóng;
- `target` và `renders`: định dạng/kích thước target nhỏ và một lượt render.

Đọc API trả bản sao, không render hoặc đổi trạng thái. Danh sách chương trình là hồ sơ renderer, không phải số đo thời gian GPU.

## Kiểm bắt buộc

1. **PASS**, thoát 0: `/Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh node node_modules/typescript/bin/tsc --noEmit -p .`.
2. **PASS**, thoát 0: `VITEST_MAX_THREADS=4 /Volumes/SS990TPRO/htdocs/typing-game/.local/bin/heavy.sh node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4`. **1006/1006 test, 93/93 tệp**; mốc 1000 giữ nguyên, thêm đúng 6 ca.
3. **PASS test mới:** Hỏa/Kim đều upload hai mask và atlas số, đúng một render 64×64 cùng định dạng bloom, đúng một instance cho từng pool instanced đang rỗng, tuổi GPU bằng 0 và sau đó count bằng 0. Có kiểm thứ tự upload/compile/render, khôi phục khi ba loại lỗi, thẻ sống, uniform bị cập nhật lúc render, phiên bản texture không đổi, atlas dùng lại và không upload texture của render target như texture ảnh.
4. **PASS build** bằng wrapper gốc `.local/codex-runs/274-out/build-no-cache.mjs`, chỉ thay chuỗi `/private/tmp/codex-274-dist` thành `/private/tmp/codex-283-dist` trong bộ nhớ. Giữ nguyên `--no-cache --configLoader runner --outDir`, cache riêng và điều kiện thư mục mới; không sửa wrapper. `grep -rl 'prewarmReport' /private/tmp/codex-283-dist` không in gì, thoát 1 đúng nghĩa không tìm thấy. Đã xóa thư mục build.
5. **PASS phạm vi:** `git diff --check` sạch. Worktree chỉ có các tệp được phép nêu trên và hai link có sẵn. Repo cha có thay đổi của các luồng khác; phiếu này chỉ ghi báo cáo ở repo cha.

Log tạm: `/private/tmp/codex-283-tsc.log`, `/private/tmp/codex-283-vitest.log`, `/private/tmp/codex-283-build.log`. Hai lượt kiểm test ban đầu phát hiện lỗi đếm con của scene và số lần `dispose` trong chính test mới; đã sửa phép đếm đúng vòng đời Three.js. Không có test cũ bị lỗi hoặc bị sửa để ép qua.

## Bàn giao

Claude xem `__lab.prewarmReport()` sau `ready`, đối chiếu mask/atlas/chương trình và đo lại cả khung bấm phím lẫn khung trúng đầu ≤ 11,5 ms cho **Hỏa và Kim**. Kiểm lại hình/nhịp không đổi, rồi quay video cho chủ và xử lý gộp nhánh/xung đột theo phiếu.

Không mở cổng mạng, không chạy trình duyệt hoặc đo GPU/video vì phần đó giao Claude. Không chạy build/test game chính hoặc game khác; chỉ chạy trong worktree được giao. Không tạo ảnh/âm thanh/capture, không sửa kit, sim, nội dung, art hoặc link. Không dùng lệnh Git ghi. Không gặp hạn mức hoặc mốc giờ phải đợi.
