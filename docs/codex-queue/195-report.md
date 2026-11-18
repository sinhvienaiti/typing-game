# Phiếu 195 · Dragonhold · Bộ từ lỗi, luật chất lượng và tự tua

**Hoàn tất phần mã và kiểm ngoại tuyến của phiếu.** `pnpm check` xanh **568/568 test**, golden **10/10**, English UI **9/9**. Gói production đạt **0 lỗi**. Ước tính thời gian không chữ **52,4% → 47,8%**. Claude còn duyệt diff và đo trình duyệt 1280/1920 theo phân công; chưa xác nhận cảm giác tua hoặc âm/VFX trên trình duyệt.

## 1. Tiếp tục đúng phần dở

Làm trong `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD **`6aa593a2dce6637cccbe24a58709b86f7127f607`**, không đổi. Có [báo cáo 194](194-report.md). Đã đọc diff và giữ phần đúng của 195 theo quyền chạy lại 30/10, 10:55. Worktree đầu lượt chỉ có tập 187/194/195 được cho phép. Không dừng lại ở cảnh báo của lượt 09:20 vì điều phối đã xác nhận đó là phần dở của chính phiếu này.

Lưu trạng thái mới tại [start-status.txt](195/start-status.txt), [parent-status-before.txt](195/parent-status-before.txt), [diff đầu lượt](195/resume-start.diff). Hai trạng thái và báo cáo lượt 09:20 được giữ tại `195/resume2-start-status.txt`, `195/resume2-parent-status-before.txt`, `195/resume2-report.md`. Các bằng chứng cũ khác vẫn còn, không dùng làm kết quả của lượt này.

Phần chưa commit được giữ riêng:

- **187, 10 đường dẫn:** `README.md`, `src/app/app.ts`, `src/app/learning.ts`, `src/app/portal.ts`, `src/ui/results.ts`, `tests/app/portal.test.ts`, `tests/ui/results-screen.test.ts`, `vite.config.ts`, `docs/changelog/2026-10-29-portal-link.md`, `tests/portal-build.test.ts`. Trong hai file app/learning, giữ import và lời gọi `createPortalBridge`.
- **194, 16 đường dẫn:** `README.md`, `package.json`, `scripts/ui-art/prepare.mjs`, `src/ui/debut-card.ts`, `src/ui/hud.ts`, `src/ui/learning-frame.ts`, `src/ui/placement-ui.ts`, `src/ui/results.ts`, `src/ui/skin.ts`, `src/ui/styles/dh.css`, `src/ui/ui-art.json`, `src/ui/wave-card.ts`, `tests/assets/ui-art.test.ts`, `tests/ui/results-screen.test.ts`, `tests/ui/ui-art.test.ts`, `docs/changelog/2026-10-30-ui-art-icons.md`.

[119 kiểm hash](195/verification.json) đều giữ nguyên: toàn bộ file riêng của 187/194 trong trạng thái đầu, mọi file sim/kit và golden. Hai file dùng chung app/learning có [diff riêng app](195/app-195.diff), [diff riêng learning](195/learning-195.diff), so với snapshot chỉ có phần trước 195. Không sửa đoạn của 187 hoặc 194.

## 2. Mười một mục đã làm

| Mục | Kết quả và đường dẫn trong worktree |
| --- | --- |
| 1. Lý do lỗi bộ từ | `src/app/learning.ts`: `DeckBuildError` mang `reason` (`load-failed`, `empty`, `too-small`) và `count`. Giữ `console.warn`; lỗi không để lại deck dùng được. Bộ đủ giữ nguyên cách chọn từ. Adapter chuyển lỗi tài liệu rỗng của kit thành danh sách rỗng để phân biệt với lỗi mạng. |
| 2. Bảng báo, chặn boot | `src/app/deck-boot.ts`, `app.css`: bảng `dh-panel`, tiêu đề “Words could not load”, dòng phụ theo lý do; Retry và cổng hợp lệ với `target="_top"`. `alertdialog`, tiêu đề/mô tả ARIA, focus Retry, Enter/Tab/Shift+Tab/trái/phải. Tự nghe phím trước router và gỡ khi đóng. Không tạo world/run/router/loop hay mở thẻ tốc độ khi lỗi. |
| 3. Retry | Gọi lại `buildDeck(stage)`, vô hiệu nút và hiện “Loading words…”. Lỗi nữa dùng lại bảng; thành công đóng bảng, boot đúng một lần; dispose chặn kết quả đến muộn. Xóa cache vocabulary khi thất bại để bộ 69 từ đã tải thành công có thể được nạp lại sau khi nguồn sửa. Không sửa kit. |
| 4. Chất lượng | `src/app/quality.ts`: `allowedQualities(prod)` và `normalizeQuality`. Production chỉ Medium/High/Ultra; Low chuyển Medium, dev giữ Low; giá trị lạ trả `undefined`. Áp dụng cả URL và tùy chọn đưa thẳng vào `startApp`. |
| 5. Hàm thuần | `src/app/idle-speed.ts`: chỉ pha wave, không chữ sống; xem hiện tại và vị trí sau 90 tick bằng `pointAt`, chặn ở `stopAt`, dùng `inWordZone` nguyên bản với pace và số từ chuỗi. Dùng tốc độ gốc cả khi freeze/slow; bỏ quái chết; sky lane xét x/z như movement. Đọc cả hàng đợi sinh quái, offset, tốc độ theo difficulty/Swift, cụm và jitter. Không đổi world hay RNG. |
| 6. Nối vào khung | Latch 300 ms thời gian thật; mất điều kiện hay có chữ thì tắt ngay. Khóa hệ số tua khi mở bảng, đặt/sửa, dừng, countdown. `frameTimeScale` tính hit-stop × (tay 2, nếu không thì tự 1,75, nếu không thì 1) × speed. Chỉ đi vào accumulator sim theo đường ×2 có sẵn. |
| 7. Alt + → | Giữ nguyên `fastForwardAllowed`, `fastForwardRefusal`, chuỗi từ chối và bật/tắt; ×2 thắng ×1,75, không nhân dồn. Callback scale kiểm lại quyền tua trước bước sim. |
| 8. Dấu tua | Dùng `icon("fast-forward")` của 194 và số nhỏ ×1.75/×2, nhãn ARIA đúng đề bài, không `aria-live`. Bảng đã có mục ảnh nên không sửa `ui-art.json` hoặc media. |
| 9. Chẩn đoán | `__dh.state()` có `idleSpeed` và `timeScale` gần nhất callback scale tính, kể cả trạng thái trước khi có run. |
| 10. Ước tính | `scripts/balance/idle-estimate.mjs <samples.json>`, khai báo kiểu `idle-estimate.d.mts`. Chạy Node ngoại tuyến, chỉ đọc file qua tham số, xuất JSON ra stdout. Kết quả ở [idle-estimate.json](195/idle-estimate.json). |
| 11. Tài liệu | Repo cha: `docs/games/dragon-lane/06-other-systems.md` §10 thêm hàng tự tua, giữ hàng ×2 và thêm “thắng tự tua”; ghi chủ dự án đồng ý 28/10, MAP1 §5.3 bước 0. Changelog nằm trong worktree ở `docs/changelog/2026-10-30-deck-notice-and-idle-speed.md`. |

Toàn bộ **15 đường dẫn của 195**: [files-195.txt](195/files-195.txt); [diff riêng 195](195/task.diff). Các file test gồm `deck-app`, `deck-boot`, `idle-speed`, `idle-estimate`, `pinned-deck`, `quality` trong `tests/app/`.

### Chỗ nối trong app.ts, để gộp với dh-vfx

Số dòng trên mã bàn giao:

| Dòng | Phần 195 |
| --- | --- |
| 26–28, 40 | Import boot/quality/idle và `icon`; bỏ hằng `QUALITIES` trước `DIFFICULTIES`. |
| 104, 190 | Chuẩn hóa quality từ URL và tùy chọn. |
| 245–249 | Ảnh fast-forward và số nhỏ. |
| 281–283, 638–639 | Latch, state và reset khi chơi lại. |
| 832–836 | Chặn tua, cập nhật latch/badge sau bước sim. |
| 882–884 | Phần nối trong callback `timeScale`; giữ hit-stop trước đó. |
| 904 | Thay `.buildDeck(...).then(...)` bằng `startDeckBoot`; giữ thân boot/router có sẵn. |
| 936, 967–968 | Hai trường debug. |
| 1112 | Dispose bộ boot. |

Không sửa hàm frame loop trong `src/app/loop.ts`. Không tách `inWordZoneAt`; vì vậy không có bản sim mới cần chứng minh tương đương. Toàn bộ `src/sim/**` giữ nguyên byte.

### Quái sắp xuất hiện

[spawn-audit.json](195/spawn-audit.json) xét **36 tổ hợp** từ các thành viên đợt map 1 trên ba độ khó, dùng tốc độ gốc và biên lateral/jitter bảo thủ. Có **Thorn Ant** và **Blight Wolf** có thể vào Vùng Chữ trong 90 tick sau khi ra cổng, nên đã tính quái sắp ra trong hàm; không bỏ qua hàng đợi.

Bán kính điểm sinh nhỏ nhất theo biên bảo thủ **28,811 m** (cách vòng 26 m **2,811 m**); bán kính nhỏ nhất trong 90 tick **24,188 m**. Đây là phép bao bảo thủ, không phải đo một seed chơi thật. Bỏ qua trì hoãn gate/cap để tắt tua sớm; lateral dự báo cho quái chưa sinh lấy phía gần tâm nhất, không rút RNG.

## 3. Test trước, mã sau và bảy mục kiểm

Lượt này tái hiện lỗi sẵn có trước sửa: [resume-check-before.log](195/resume-check-before.log), mã **1**, **549/551 test xanh**, hai test đỏ và một suite không thu thập vì thiếu script. Sửa hai fixture idle-speed: thứ tự tham số `applyStatus`, và cập nhật x/z sau khi đổi along; không sửa luật để làm xanh test.

Các test mới được chạy trước sửa tương ứng:

- Script chưa có: [resume-tests-first.log](195/resume-tests-first.log), idle-estimate không thu thập được; sau thêm script xanh.
- Adapter thật rỗng/69 từ: [resume-adapter-red.log](195/resume-adapter-red.log), **2 đỏ/7 xanh**; sau sửa phân biệt rỗng và cache, xanh.
- Lateral của quái sắp sinh: [resume-queued-red.log](195/resume-queued-red.log), **1 đỏ/20 xanh**; sau dự báo phía gần vòng, xanh.
- Swift của cụm: [resume-swift-red.log](195/resume-swift-red.log), **1 đỏ/22 xanh**; sau dùng đúng trait của cụm, xanh.

| Kiểm | Kết quả mới của lượt này | Bằng chứng |
| --- | --- | --- |
| 1. `pnpm check` | Cuối **mã 0**, **65 file, 568/568 test**, kit 75 file, TypeScript và Vite xanh. Sáu file test của 195 có **42/42**. Lượt giữa đã có 567 test xanh nhưng TypeScript bắt một `.find()` có thể undefined; đã sửa assertion và chạy lại đầy đủ. Không có test thời gian đỏ nên không cần ba lần chạy riêng. | [check-final.log](195/check-final.log), [lượt giữa](195/check-after.log) |
| 2. Golden và bot | Golden **10/10 xanh**; năm file `tests/sim/bot-*.test.ts` **37/37 xanh**. M0 SHA-256 **`c0f9770cf32f033988576c0da8a17b7ae817b20c676a7ae3cd78ef2860562b82`**, giữ nguyên. | Log check, [verification.json](195/verification.json) |
| 3. Balance | Hoàn tất **1.800 lượt**, 20 seed mỗi bộ, hai bộ seed, ba mode, 15 bot. Chạy bot đầy đủ đúng một lần. CLI pnpm/tsx bị `listen EPERM` trước khi vào bot; dùng `TSX_DISABLE_CACHE=1 node --import=tsx scripts/balance/run.ts --seeds=20 --json=../../docs/codex-queue/195/balance.json`, mã **0**, cùng script/tham số, không sửa mã balance. | [CLI lỗi](195/balance.log), [lượt hoàn tất](195/balance-node.log), [balance.json](195/balance.json) |
| 4. `pnpm deploy:pack` | **Mã 0**, checker **0 lỗi**, **402 file**, **35.055.709 byte**, **0 localHost**, không vocabulary ngoài gói. Chạy checker `--json` trên chính dist vừa dựng. Vite có cảnh báo chunk lớn, không lỗi. | [deploy-pack.log](195/deploy-pack.log), [JSON gói](195/deploy-pack.json) |
| 5. English UI | **9/9 xanh** trong check. Bảng lỗi, nút, loading và nhãn tua đều tiếng Anh. | Log check |
| 6. Ước tính | Trước **52,4%**, sau **47,8%**; bảng nhạy bên dưới. Test script **4/4 xanh**. | [idle-estimate.json](195/idle-estimate.json) |
| 7. Phạm vi/Git | HEAD không đổi; worktree chỉ tập 187/194/195. 119 hash bảo toàn đều đúng; `git diff --check` xanh. Repo cha: phiếu chỉ ghi `06-other-systems.md` và `195*`; trạng thái thô còn thay đổi của các làn chạy đồng thời, liệt kê bên dưới. | [status-final.txt](195/status-final.txt), [parent-status-after.txt](195/parent-status-after.txt), [verification.json](195/verification.json) |

Test app thật giữ loader/deck/world thật, thay renderer/audio và scheduler bằng stub: ba loại lỗi không tạo world/run/router/loop, không wave-start, không mở thẻ tốc độ; Retry hồi phục chỉ tạo một world/router/loop. Test DOM riêng kiểm focus, phím, cổng có/không, lỗi lần hai, loading và dispose. Test loop thật xác nhận chỉ số bước sim nhận hệ số, `dt` trình bày giữ nguyên, có chữ thì hệ số về 1. Test idle có biên 89/90/91 tick, ring và T_a, sky lane, attack/blocked, freeze/slow, chết, chữ sống, mọi pha nghỉ/kết thúc, queue/delay/jitter/Swift và tính chỉ đọc.

Bộ ghim thật khởi đầu lạnh: **200/200 trường hợp**, cấp **1–100**, `excludeMature` tắt/bật, đều **90 từ**. Không có cấp dưới 70; không hạ ngưỡng. [200 số đếm](195/pinned-counts.json).

### G1, G3, G5, G6, G8 để so main

| Cổng | Kết quả mode balanced, 40 seed | Trạng thái |
| --- | --- | --- |
| G1 | 35 WPM: **85,0% thắng** | Đạt |
| G3 | 25 WPM: **90,0% thắng** | Đạt |
| G5 | Chỉ gõ, không mua: **0,0% thắng** | Đạt |
| G6 | Không gõ, mua tốt: **40/40 thua ở đợt 1** | Đạt |
| G8 | Bẫy/nhà/lính: **30,1% sát thương** | Đạt |

[bản gọn](195/balance-gates.json) lấy G1/G3/G5/G6 từ JSON gốc; G8 dùng `extraGates` hiện có trên chính kết quả đó, vì JSON mặc định không xuất G8. Không chạy bot lần hai. Các số bot đo bằng tick; tự tua ở app không tham gia bot.

### Ước tính thời gian không chữ

Mẫu là `[ms, phase, wave, words, visibleWords, liveFoes, hp]`; giữ cách tính “trước” của `idle-samples.mjs`: pha 2, visibleWords = 0, mỗi khoảng chặn tối đa 500 ms. Tổng wave làm tròn **521 giây**, không chữ **273,0 giây**, **154 quãng**. Với quãng dài `g`, phần sau là `min(g, L) + max(0, g − L) / tốc`; mẫu số wave cũng giảm theo phần thời gian tiết kiệm.

| Tầm nhìn L | ×1,75: không chữ | ×2: không chữ |
| --- | --- | --- |
| 0 giây | **38,6%** | 35,5% |
| 0,5 giây | 42,7% | 40,7% |
| 1,0 giây | 45,6% | 44,3% |
| 1,5 giây | **47,8%** | 46,9% |

Sau ở L = 1,5 giây, ×1,75: wave **475,0 giây**, không chữ **226,9 giây**. **Giả định:** mẫu không có vị trí quái, nên dùng chữ hiện thay cho quái vào Vùng Chữ. Chưa mô hình hóa latch 0,3 giây, bảng/placement, queue và tua tay. Vì vậy 47,8% là ước tính, không phải cam kết đo thật. Khoảng **39%** trong MAP1 §5.3 ứng với tua cả quãng (L = 0: **38,6%**). Không sửa MAP1 hoặc file mẫu nguồn; test CLI xác nhận mẫu giữ nguyên byte.

## 4. Phần để Claude/chủ dự án xem

- **Gộp với 192:** Settings ở `dh-keys` phải dùng `allowedQualities(import.meta.env.PROD)` khi liệt kê Graphics; nhánh gộp sau chịu trách nhiệm. Phiếu này chặn Low tại URL và khởi động app, không sửa nhánh đó hoặc tạo bảng Settings.
- **Gộp với dh-vfx:** xem các dòng `optionsFromUrl`/`timeScale` đã chỉ rõ bên trên. Logic mới nằm trong file mới; giữ luật hit-stop của V-dh2 khi gộp. Không sửa worktree V-dh2.
- **Đồng hồ cần đo:** `src/view/fx.ts:1334` dùng `hitStop.worldDt(info.dt, info.now)`, số sát thương dùng `info.dt`; nhạc ở `src/audio/index.ts:207` dùng `AudioContext.currentTime`. Không đổi các đường này hoặc playback rate. Có giao điểm thời gian sẵn có: `src/audio/map-events.ts:245–247` đổi durationMs của telegraph sim thành hạn/độ trễ âm theo thời gian thật; `src/view/fx.ts:1294` đổi durationMs burn thành thời lượng FX, trong khi sim có thể được tua. `src/view/telegraphs.ts:509` lại dùng `info.worldDt` như đường ×2 có sẵn. Chỉ ghi nhận theo mục Rủi ro, không tự sửa ngoài phạm vi. Cần Claude nghe/xem khi tua bật và tắt.
- **Trình duyệt:** chưa mở server, trình duyệt hoặc mạng theo lệnh cấm. Claude đo 1280/1920: lỗi tải/rỗng/thiếu, focus/Retry/cổng, dấu ảnh và cỡ chữ, phần thời gian không chữ thật, chuyển tua, âm và VFX. Chưa đưa ra nhận định cảm quan.
- **Phần ngoài phiếu:** alias nginx thuộc Claude; không sửa nginx. Không tạo ảnh/âm, không thêm media vào Git, không sửa kit hay đồng bộ kit, không đổi sim/golden hoặc chạy golden:update. Không chạm Tu Tiên, game/worktree khác, không ghi `games/dragon-hold/tmp/**`. Không chạy Git ghi, commit hoặc push.

So trạng thái repo cha đầu/cuối có thay đổi đồng thời ngoài phiếu: `infra/nginx/typing-game.local.dev.conf`, `infra/nginx/typing-game.local.play.conf`, `scripts/validate-play-mode.mjs`, test cùng tên, báo cáo/thư mục 199, 202, 215, 216, 217, `tools/audio-lab/build/tests/test_build_firefly_licence.py`, `tools/audio-lab/firefly/`. Không mở để sửa hoặc hoàn tác các phần này. [Các dòng trạng thái mới](195/parent-status-added.txt) giữ nguyên bằng chứng, không nhận trạng thái repo cha thô chỉ khác hai nhóm đường của phiếu. Phần ghi của 195 vẫn đúng hai nhóm được phép.
