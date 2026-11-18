# Phiếu 222 · Kiểm độc lập phần chưa commit của Dragonhold

**Chưa đủ điều kiện để Claude chấp thuận commit.** Có **1 blocker về chuẩn ảnh kế thừa**, **3 major** (CSS màn tựa tràn sang giao diện cũ; mất Retry ở màn tựa mặc định; test phụ thuộc mẫu ngoài repo), **0 minor**, **1 note về đồng hồ âm/VFX**. Không tìm thấy thay đổi luật sim, kit hoặc golden; kiểm ngoại tuyến tương đương `check` xanh **69 file / 593 test**, kit **75 file**, TypeScript và build xanh. Gói phát hành đúng số 197: **402 file, 35.061.724 byte, 0 lỗi, 0 localHost**. Ba test dò chạy riêng đỏ đúng ba vấn đề đã nêu; không cộng chúng vào 593 test gốc. Đây là báo cáo kiểm, không sửa mã và không nghiệm thu cảm quan.

## 1. Mốc và cách chạy

- Nhánh `dh-codex`; HEAD trước/sau yêu cầu: `6aa593a2dce6637cccbe24a58709b86f7127f607`.
- Đủ bốn báo cáo 187, 194, 195, 197. Báo cáo 194 kết thúc với kiểm chung đỏ vì phần 195 còn dở; 195 và 197 có xác nhận xanh sau đó. Không dùng kết luận của lượt bị ngắt làm trạng thái cuối.
- Đầu lượt: **51 đường dẫn = 24 M + 27 mới**, danh sách chép **473 file**; đúng số phiếu 222. `df -g .`: **48 GB trống**, vượt ngưỡng 2 GB.
- Khi bắt đầu, `codex-222/` đã có bản dựng chép và marker 30/10/2026 14:19. Không dựng đè: xác minh lại từng SHA-256, status, danh sách file, `node_modules` chép thật, liên kết tuyệt đối `public/assets` và mẫu đúng chỗ; tất cả khớp trước lệnh kiểm đầu tiên. Ghi rõ xuất xứ ở `222/setup-provenance.txt`. Không coi bản chép có sẵn là bằng chứng đã chạy test.
- Mọi lệnh Git đặt `GIT_OPTIONAL_LOCKS=0`; chỉ dùng lệnh đọc. Mọi lệnh kiểm chạy với cwd trong `games/dragon-hold/tmp/codex-222/tree`, `TMPDIR` tuyệt đối là `.../codex-222/tmpdir`, `ART_MAGICK=/opt/homebrew/bin/magick`.
- `pnpm check` đầu tiên **mã 1**, trước khi chạy mã kiểm: pnpm tự gọi `install`, bị chặn vì không TTY. Không cho cài lại, không thêm CI để chấp nhận xóa modules. Chạy đúng bốn bước dự phòng trực tiếp. Lượt đầu Vitest **585 đạt / 8 đỏ** vì tám test `deploy-pack` gọi pnpm con và vướng cùng cơ chế tự cài; không phải lỗi game.
- Đọc mã pnpm cục bộ, xác định biến `pnpm_config_verify_deps_before_run=` rỗng tắt cơ chế đó ở tiến trình con. Giữ nguyên mã và assertion, chạy lại bốn bước trực tiếp: kit **0 / 0,035 s**; Vitest **0 / 6,650 s**, **69/69 file, 593/593 test**; tsc **0 / 1,966 s**; Vite **0 / 1,320 s**. Không có test thời gian đỏ cần chạy ba lần. Log đầu vẫn giữ, log chính `222/check.log` chứa cả lý do và lượt cuối; lệnh/môi trường ở `fallback-final.json`.
- Các lệnh `pnpm exec`, `deploy:pack` và `prepare-ui-art --check` được thực hiện bằng chương trình cục bộ tương đương, theo nhánh dự phòng. Build local trước, production sau; checker JSON đọc đúng dist vừa dựng. Không gọi pnpm cài gói.
- Balance dùng `TSX_DISABLE_CACHE=1 node --import=tsx scripts/balance/run.ts --seeds=20 --bots=b35 --jobs=4 --json=<C>/logs/balance-b35.json`. Không dùng CLI tsx mở IPC server. `uptime` ngay trước: tải 1 phút **6,03**, nên jobs **4**; thời gian cả lệnh **4,685 s**.
- Mẫu `samples.json` gốc trước/sau cùng SHA-256 **`d9e4220369c0f6131db82c2ed41073ff108b58e5f40a79b86abc79246ce1f0f7`**. Không ghi cạnh mẫu hoặc vào media thật.

Các file bằng chứng bên dưới tương đối với `docs/codex-queue/222/`. Các đường mã không có tiền tố được tính từ worktree `games/.wt-dh-codex/`.

## 2. Quy file và kiểm phạm vi

[attribution.json](222/attribution.json) là bản đầy đủ cho 223: **51/51 đường dẫn**, **0 chưa gán**, **0 dòng thêm trong diff hiện tại chưa gán**. Đọc lại diff thật từ HEAD và mọi file mới; dùng snapshot cũ để phân biệt tác giả, kiểm SHA-256 snapshot trước 197 khớp trước khi quy khối. File JSON chứa số dòng bản cuối, cả dòng neo cho phần xóa; dòng 954 app có cả phần 195 và 197.

| Nhóm | Số đường dẫn có phần sở hữu | Phần chung |
|---|---:|---|
| 187 | 10 | README, app, learning, results, results-screen test |
| 194 | 16 | README, results, results-screen test, prepare, ui-art |
| 195 | 15 | app, learning, deck-app test |
| 197 | 19 | app, prepare, ui-art, deck-app test |

Có **43 file chỉ một phiếu** và **8 file chung**; tổng số sở hữu 60 do chồng phần chung. Các khoảng trong JSON chính xác hơn bảng tóm tắt sau.

| File chung | Khối chính theo dòng bản cuối |
|---|---|
| `README.md` | 187: 4–40; 194: 41–44 |
| `src/app/app.ts` | 187: 25, 227; 195: 26–28, 40, 81 (xóa QUALITIES), 107, 194, 249–252, 285–287, 642–643, 837–841, 887–889, 954 (trường idle), 986–987, 1131; 197: 41, 56, 76–77, 95, 114, 211–212, 746, 909–945, 954 (title), 957, 1132 |
| `src/app/learning.ts` | 187: 12, 18, 265; 195: 15, 121–132, 247–255, 340–350, 373–380 |
| `src/ui/results.ts` | 187: 254–266, 371, 433; 194: 239, 299–301, 320–343, 348, 356, 365 |
| `tests/ui/results-screen.test.ts` | 187: import beforeEach, 114, 118–138, 147; 194: 18, 56, 58–96 |
| `scripts/ui-art/prepare.mjs` | 194 dựng script; 197 mở rộng import dirname, art validation/check, xuất title, stage/rollback nhiều thư mục, help; từng đoạn ở JSON |
| `src/ui/ui-art.json` | 194: 1–717, 741–742; 197: 718–740 |
| `tests/app/deck-app.test.ts` | 195 dựng test lỗi/Retry; 197 sửa stub và hợp đồng router sớm, thêm test title 101–147; từng dòng ở JSON |

**Không có sửa ngoài phạm vi được quy cho phiếu sở hữu.** Không có phần 194 trong `src/app/**`; không có phần 197 trong `dh.css`, rules, sim, view hoặc kit. Các cấm sửa file của một phiếu không được dùng để nhận nhầm phần hợp lệ của phiếu khác: ví dụ app thuộc 187/195/197, còn `dh.css` chỉ thuộc 194. Không có đường dẫn thay đổi ở `src/sim/**`, `src/kit/**`, `src/view/**` hoặc golden.

**File repo cha riêng của 195, không vào `paths`:** `docs/games/dragon-lane/06-other-systems.md:288–289`. Diff thật **+2/−1**: nhìn trước 1,5 giây, chốt 0,3 giây, khóa khi bảng/đặt/sửa/dừng/countdown, Alt + → thắng tự tua. Khớp `idle-speed.ts:10–88`, `app.ts:837–889`; ký hiệu » trong tài liệu mô tả dấu ảnh fast-forward, không phải ký tự được đưa lên HUD.

## 3. Đối chiếu từng phiếu

“Đạt” dưới đây là kết luận mã/kiểm ngoại tuyến trong phạm vi; không thay thế duyệt hình trên trình duyệt. Các dòng không thể dựng lại lịch sử được ghi rõ. Các nợ ảnh được phiếu cũ cho giữ lại vẫn được tách khỏi hồi quy mới; mức blocker ở §5 theo quy tắc của 222.

### 187

| Mục | Yêu cầu / số báo cáo cũ | Đọc hoặc đo lại trên trạng thái cuối | Kết quả, bằng chứng |
|---|---|---|---|
| Việc 1 | Hai nguồn nhà của 169 | Đã đối chiếu báo cáo 187 và khai báo kit / helper cổng cũ; không build lại mốc cũ | Đạt về truy vết; `src/kit/learning/contract.ts:22`, `src/app/portal.ts:6` |
| Việc 2 | Biến build, mặc định trống, nút cổng có điều kiện, README | Vite loadEnv; plugin chỉ transform đúng file và đúng 1 khai báo; URL HTTP(S) tuyệt đối, từ chối credentials; host parent null khi trống | Đạt; `vite.config.ts:11–25`, `portal.ts:5–33`, `results.ts:256–266`, `README.md:6–36` |
| Việc 3 | Pack production và local đều 0 lỗi | Tương đương build+checker trực tiếp đều mã 0; prod 0 localHost, local 5 tham chiếu cho phép | Đạt; `pack-prod.json`, `pack-local.json` |
| Việc 4 | Test nút và không nguồn nhà | Portal/results/build tests xanh; quét mọi file dist thấy 0 file chứa nguồn nhà | Đạt; `tests/app/portal.test.ts:8–114`, `tests/portal-build.test.ts:12–64`, `prod-local-host-scan.json` |
| Luật: Git/kit | Không Git ghi, sửa kit, sync | Không diff kit, verifier 75/75; 222 không thực hiện lệnh ghi | Đạt về trạng thái; không suy ra toàn bộ lịch sử shell của 187 |
| Luật: server/mạng/phạm vi | Không server, trình duyệt, mạng, game/worktree khác, Tu Tiên | 222 không chạy; diff 187 có 10 đường đúng việc | Đạt về diff; lịch sử hành động cũ không kiểm lại được |
| Luật: test trước, chú thích, luật/golden, tiếng Anh | Test trước mã; không đổi sim/golden | Lịch sử test-first chỉ có log cũ; source/comments và English UI đạt; golden đúng MD5 | Đạt mã/golden; không kiểm được thứ tự biên tập lịch sử |
| Kiểm 1 | 57 file / 509 test; kit 75; golden 10 | 69 file / 593 test; kit 75; golden 10; tsc/build mã 0 | Lệch có lý do: 194/195/197 thêm 84 test; không lỗi thời gian |
| Kiểm 2 | Trước: 1 lỗi; sau: 240 file, 33.654.248 B, local 0; demo 33.654.591 B, local 3 | Prod 402 file, 35.061.724 B, local 0; local 402 file, 35.062.123 B, local 5; problems đều 0 | Lệch có lý do: 194 thêm icon/media/manifest; 195/197 thêm UI và chỗ cổng; mốc trước giữ ở 187/pack-before.json |
| Kiểm 3 | Status 10 file của 187 | 10 đường được quy, giữ riêng phần các phiếu sau; không file lạ | Đạt; `attribution.json` |

### 194

| Mục | Yêu cầu / số báo cáo cũ | Đọc hoặc đo lại trên trạng thái cuối | Kết quả, bằng chứng |
|---|---|---|---|
| Việc 1 | 53 icon, 36 nhận, 17 tạm, version 1, tên/key duy nhất | Đúng 53/36/17; 66 tên+key, 66 duy nhất; art của 197 tách riêng | Đạt; `src/ui/ui-art.json:1–742`, test `tests/ui/ui-art.test.ts:30–55` |
| Việc 2 | Script chuyển cỡ/alpha/PSNR/manifest, atomic, --check không ghi | Đọc sourceSet/check/publish; fixture exact/downsizing/alpha/hash/nguồn lỗi xanh; --check thật mã 0. Không chạy lệnh prepare ghi vào assets thật | Đạt ngoại tuyến; `scripts/ui-art/prepare.mjs:34–184`, `tests/assets/ui-art.test.ts:45–113` |
| Việc 3 | img, cỡ, chỉ còn 3 SVG, aria-label | 20→64, 46→128, 120→256; 53 mục + alias ra img. Ba SVG được phiếu cho giữ vẫn còn | Đạt phạm vi 194; nợ chuẩn ảnh F1; `skin.ts:131–165`, `hud.ts:260–270`, `results.ts:355–357` |
| Việc 4 | Capture error, warn một lần/URL, hidden | Hàm xử lý đúng; installSkin gắn một lần/document | Đạt; `skin.ts:25–39,177–185`; listener sống cùng document, xem §4 |
| Việc 5A/B/C | Thay hình A; thêm ảnh B; chuẩn bị 6 mục C | Đối chiếu 36 dòng integration và diff thật: 30 đã gắn, 6 giữ chuẩn bị. shop-strip dùng alias không cần sửa; fast-forward do 195 gắn sau | Đạt; `hud.ts:244–443`, `wave-card.ts:249–367`, `debut-card.ts:116`, `placement-ui.ts:531–537`, `learning-frame.ts:182–190,629`, `results.ts:239–365` |
| Việc 6 | Bỏ rêu trước/sau; giữ moss tokens | Đã xóa cả hai pseudo và chú thích. app.css:115 còn quy tắc bottom chết, không có content nên không cần pseudo để hoạt động | Đạt; `dh.css:67–95`, `app.css:114–117`; không tính quy tắc chết này là lỗi chức năng |
| Việc 7 | Ô 20/25/46/18/22; không recolour mới | Markup/cỡ đúng; không thêm filter/blend/opacity đổi màu ảnh; trạng thái mờ cũ giữ nguyên | Đạt mã; kích thước hiển thị thực tế cần trình duyệt; `skin.ts:149–153`, `dh.css:125–153` |
| Việc 8 | README và changelog | Đủ hướng dẫn prepare/check và giới hạn | Đạt; `README.md:42–44`, `docs/changelog/2026-10-30-ui-art-icons.md:1–13` |
| Test 1–7 | Bảng, callers, cỡ, fixture, lỗi ảnh, emoji, learning/results | Các ca tương ứng đều trong 593 xanh; so khớp integration, alias, byte media | Đạt; `tests/ui/ui-art.test.ts:30–164`, `tests/assets/ui-art.test.ts:45–113`, `tests/ui/results-screen.test.ts:58–96` |
| Cấm 1 | Git ghi | Không có thao tác ghi Git trong 222; không chứng thực lại lịch sử shell 194 | Đạt trạng thái; `status-before.txt` |
| Cấm 2 | Kit/view/app/sim/content/tags; sync kit | Không khối 194 ở các vùng này; file chung app/learning thuộc 187/195/197 | Đạt; `attribution.json`, kit 75 |
| Cấm 3 | Server/trình duyệt/mạng | 222 không chạy; lịch sử cũ không thể suy từ diff | Đạt lượt kiểm |
| Cấm 4 | Checkout chính trừ icons; worktree/game khác; Tu Tiên | Media kiểm MD5 ở đúng icons; source worktree không có file ngoài tập sở hữu | Đạt về diff/media; không kiểm lại lịch sử thao tác ngoài Git |
| Cấm 5 | Ảnh vào Git / ghi ngoài repo | Không file media trong 51 đường; fixture chỉ trong bản chép | Đạt trạng thái |
| Cấm 6 | Icon mã, sửa nguồn, sinh ảnh | Không thêm icon SVG/CSS mới trong 194; nguồn check hash đúng. Còn 3+11 SVG và panel CSS được phiếu cũ giữ | Đạt phạm vi sửa; không đạt chuẩn ảnh chung, F1 |
| Cấm 7 | Settings/Sound 192 | Không gắn nút cài đặt hay Sound trong trận | Đạt; speaker chỉ phục vụ nghe từ/khung học |
| Kiểm 1 | 549/551 xanh, 2 đỏ + 1 suite không thu thập; build chưa chạy | 593/593, 69 file, kit 75; tsc/build xanh | Lệch có lý do: 195 hoàn tất, 197 thêm 25 test; không dùng 526 lịch sử |
| Kiểm 2 | Golden 10/10, MD5 75f749…940e | 10/10 riêng; MD5 đúng nguyên chuỗi yêu cầu | Khớp; `golden.log`, `golden-md5.txt` |
| Kiểm 3 | English UI 9/9, không emoji UI | 9/9 riêng; quét pictograph/check trong UI của test 194 xanh | Khớp; `english-ui.log` |
| Kiểm 4 | 159 WebP + manifest; 142 PNG; byte 64/128/256: 142184/350914/706946; min PSNR 35.1794/35.0822/35.2564; lossless 13/6/0 | 159 WebP MD5/byte khớp; số cỡ và PSNR/lossless đọc lại từ manifest đã kiểm nguồn/output. Không tái encode để đo PSNR độc lập | Khớp inventory; giới hạn đo nêu rõ; `icon-metrics.json`, `media-compare.json` |
| Kiểm 5 | --check mã 0 | --check mã 0, 53 icons; nguồn/output hợp lệ | Khớp; `prepare-check.log` |
| Kiểm 6 | deploy mã 2 ở 195, dist cũ có 159 icon | Build+checker mã 0, prod 402 file; 159 WebP UI trong dist; manifest mới 62562 B | Lệch có lý do 195 hoàn tất; không nhận dist cũ làm bằng chứng |
| Kiểm 7 | Tờ xem 337218 B dưới 1 MB, 53 cặp | Không tạo hay xem lại tờ xem, không nghiệm thu cảm quan trong 222 | Không kiểm lại; bàn giao Claude; không phải lệch số chưa giải thích |
| Kiểm 8 | 30 gắn / 6 chuẩn bị; 3 SVG skin + 11 tags | Đúng số; sau 195 có fast-forward gắn thêm ngoài phần 194 | Khớp; F1 là nợ chuẩn chung |
| Kiểm 9 | Tập file 187/194/195, ignore media | Quy đúng 16 đường 194; không có ảnh trong file list Git; tập cuối thêm 197 | Lệch có lý do 197; `attribution.json` |
| Kiểm 10 | 160 dòng media: 159 WebP + manifest 62549 B MD5 040d543c… | 159 WebP khớp; manifest 62562 B MD5 686bbb8e…; bỏ duy nhất art:{} khôi phục JSON đúng 62549 B / MD5 040d543c8d679c3c44a6e20adfb49b33 | Khớp sau giải thích 197; `manifest-compare.json` |

### 195

| Mục | Yêu cầu / số báo cáo cũ | Đọc hoặc đo lại trên trạng thái cuối | Kết quả, bằng chứng |
|---|---|---|---|
| Việc 1 | load-failed / empty / too-small <70; đủ từ giữ chọn cũ | Phân biệt đúng, mang count, warn, xóa cache lỗi/thiếu; >=70 giữ đường chọn cũ | Đạt; `learning.ts:243–257,332–386` |
| Việc 2 | Bảng lỗi, không run/loop/pace; phím/ARIA; cổng có điều kiện | title=0 giữ bảng và Retry; mặc định 197 dùng title blocked, không run/loop/pace nhưng không còn Retry. Router sớm là thay đổi được 197 yêu cầu | Đạt luồng bypass; không đạt tích hợp mặc định F3; `deck-boot.ts:17–89`, `app.ts:917–944`, `title.ts:58–80` |
| Việc 3 | Retry tải lại, loading, một boot, lỗi nữa/dispose | busy/closed chặn double click và late success; test thật app xanh. Chỉ còn truy cập được ở title=0 | Đạt hàm Retry; F3 ở luồng mặc định; `deck-boot.ts:73–89`, `tests/app/deck-app.test.ts:91–100` |
| Việc 4 | Production không Low, URL/direct options; dev giữ Low | normalizeQuality dùng ở cả URL và startApp; unknown undefined; API allowedQualities prod không low | Đạt; `quality.ts:4–12`, `app.ts:107,194`; Settings 192 chưa gộp |
| Việc 5 | wave, không chữ, lookahead 90 tick, ring/T_a, flyers, attack/blocked, freeze/dead/queue | Hàm chỉ đọc world/RNG, gọi inWordZone nguyên bản và pointAt; dự báo queue gồm Swift/cluster/lateral. Boundary 89/90/91 và các trạng thái đều có test xanh | Đạt; `idle-speed.ts:10–65`, `tests/app/idle-speed.test.ts:27–121`; không tách hàm sim |
| Việc 6 | Latch 0,3 s; khóa bảng/đặt/sửa/pause/countdown; chỉ số bước sim | Latch 300 ms; paused gồm menu/pace/focus/countdown/prelearn/review; placement khóa riêng. dt trình bày giữ nguyên, worldDt/accumulator nhận scale | Đạt mã; note F5 âm/VFX; `idle-speed.ts:68–88`, `app.ts:766,837–889`, `loop.ts:52–68` |
| Việc 7 | Alt+→ ×2 thắng, không nhân dồn | fastForwardAllowed/refusal giữ nguyên; frameTimeScale chọn manual trước idle | Đạt; `app.ts:712–741,889`, `idle-speed.ts:87–88` |
| Việc 8 | Ảnh fast-forward + số / ARIA đúng, không live | Đúng ảnh 194, ×1.75/×2, hai aria-label đúng, không aria-live trên badge | Đạt; `app.ts:249–252,839–841` |
| Việc 9 | state idleSpeed/timeScale | Có cả trước run và sau run | Đạt; `app.ts:954,986–987` |
| Việc 10 | Estimate CLI, before52.4, after,8 nhạy, giả định, không ghi nguồn | Before 52.4; after47.8; 8 hàng đúng; source hash giữ nguyên; test lại dựa file ngoài repo | Đạt script, lỗi fixture F4; `scripts/balance/idle-estimate.mjs:9–50`, `tests/app/idle-estimate.test.ts:16–23` |
| Việc 11 | Tài liệu repo cha §10 | Đúng +2/−1; 1,5 s / 0,3 s / Alt+→ thắng, không đổi sim/nhạc/VFX | Đạt; `docs/games/dragon-lane/06-other-systems.md:288–289` ở repo cha |
| Test | Các loại lỗi, Retry/cổng, 200 bộ ghim, quality, idle, scale | Các test gốc đều xanh; pinned 200/200, đều90 từ; không tách inWordZone nên test tương đương không áp dụng | Đạt ngoại tuyến; `tests-final.log`; thứ tự test-first lịch sử không thể kiểm lại |
| Cấm 1 | Git ghi / kit / sync | Không diff kit; verifier75; không lệnh ghi Git trong 222 | Đạt trạng thái |
| Cấm 2 | Server/browser/mạng/ngoài repo | 222 không chạy; mọi đầu ra trong C hoặc 222 | Đạt lượt kiểm; lịch sử phiếu cũ không kiểm được |
| Cấm 3 | Đổi sim / golden:update / golden | Không diff sim/golden; MD5 đúng; bot theo tick khớp | Đạt; golden.log, attribution |
| Cấm 4 | Worktree/game khác, Tu Tiên | Không file thuộc195 bên ngoài tập đã quy | Đạt về diff |
| Cấm 5 | Ghi tmp checkout chính | 222 chỉ ghi C theo quyền222; 195 đọc mẫu, không có đổi mẫu trong lượt kiểm | Đạt lượt kiểm; không suy ra lịch sử195 |
| Cấm 6 | infra/nginx | Không nhận thay đổi nginx ở repo cha là của 195 | Đạt phạm vi; thay đổi đồng thời ghi riêng |
| Cấm 7 | Sinh ảnh/media vào Git | Không media trong51 đường; chỉ code gọi ảnh đã có | Đạt trạng thái |
| Cấm 8 | Tiếng Việt người chơi thấy trừ hai tên | English UI9/9; chuỗi mới đều English, nghĩa học được giữ | Đạt; `english-ui.log` |
| Kiểm 1 | 65 file /568 test, kit75 | 69 file /593 test, kit75; tsc/build0 | Lệch có lý do197 thêm25 test; pnpm dự phòng như§1 |
| Kiểm 2 | Golden10; bot sim37; hash M0 c0f977… | Golden10 riêng; bot sim37 trong suite; MD5 75f74947dac170d05fd659f99417940e và SHA-256 c0f9770cf32f033988576c0da8a17b7ae817b20c676a7ae3cd78ef2860562b82 | Khớp; không sửa golden |
| Kiểm 3 | 1.800 lượt/all bots; G1 85%, G3 90%, G5 0%, G6 40/40 thua wave1, G8 30.1% | Theo222 chỉ b35:120 lượt, relax100%, balanced85%, challenge65%, 40 seed/mode; G1 khớp. Không đo lại G3/G5/G6/G8 vì cần bot khác | Khớp phần b35; các cổng còn lại không kiểm lại, không đánh tráo subset thành all-bot |
| Kiểm 4 | Prod402 file,35055709 B,0 lỗi/local | Prod402 file,35061724 B,0 lỗi/local | Lệch có lý do197 thêm6015 B; `pack-prod.json` |
| Kiểm 5 | English9 | English9 riêng | Khớp |
| Kiểm 6 | Before52.4%, after47.8%, nhạy38.6…46.9 | Đúng toàn bộ JSON đo lại, xem§4 | Khớp; `idle-estimate.json` |
| Kiểm 7 | 15 đường của 195 +187/194; parent chỉ doc§10 +195* (có làn đồng thời) | Quy đủ15 đường; parentdoc§10 tách riêng; 197 thêm phần sau. 222 không sửa báo cáo cũ | Khớp phạm vi; status cuối của222 kiểm riêng§7 |

### 197

| Mục | Yêu cầu / số báo cáo cũ | Đọc hoặc đo lại trên trạng thái cuối | Kết quả, bằng chứng |
|---|---|---|---|
| Việc 1 | Art 3 mục/null, xuất accepted, check, alpha/width, không public title | Đúng 3 null, width 1536/1024/512, nguồn đúng; 0 request khi null; fixture export/check xanh; thật không có title output | Đạt; `ui-art.json:719–740`, `prepare.mjs:69–84,170–180`, `tests/assets/title-art.test.ts:11–50` |
| Việc 2 | Title→Start→pace→begin; wpm skip pace; bố cục/vùng; bỏ boot | Thứ tự đúng; không boot text cũ; CSS có vùng yêu cầu nhưng lớp .dh-title trùng lớp typography cũ | Đạt thứ tự; không đạt CSS F2; `app.ts:909–938`, `title.css:1–65` |
| Việc 3 | Portal có điều kiện/target_top; quick 192 hoặc chừa slot | Không quick.ts trong worktree; slot rỗng và ẩn đúng; portal đúng biến build | Đạt trong phạm vi; `title.ts:76–82`, `title.css:64–65`; không nhận đã xong Settings 192 |
| Việc 4 | Router sớm, action cũ, Enter/arrows/Esc/mouse, chặn chữ, focus rõ | Router tạo ở 921 trước buildDeck tại 933; không keydown mới trong title; state/pointer/wrap đúng. Viền 3 px có khai báo, cảm quan chưa kiểm | Đạt mã; F2 ảnh hưởng hiển thị các màn sau; `title-state.ts:21–29`, `title.ts:101–121`, `input-router.ts:102–140` |
| Việc 5 | Bốn nguồn, status/progress, optional fail vẫn settle, từ lỗi block/cổng | Đủ bốn promise và guard dispose; Start tắt khi từ lỗi, cổng vẫn có nếu cấu hình; thiếu Retry so với 195 | Đạt hợp đồng chờ; F3 tích hợp phục hồi; `app.ts:932–944`, `title.ts:88–99` |
| Việc 6 | Thiếu art→nền phẳng/chữ/ẩn, warn, không vẽ giả, nút cũ | Null không tạo img, error hidden, warn 1/tên; nền #17130f, logo font cũ, không SVG/canvas/gradient/emoji ở title | Đạt ngoại tuyến; `title.ts:33–57`, `title.css:7,32–35`; khung 162 chưa nhận như phiếu cho phép |
| Việc 7 | Show/hide subscriptions, live/art, debug.title; không camera | Đủ API và hàm gỡ, state loading/ready/blocked/started, chừa R2, chưa gắn camera | Đạt; `title.ts:117–125`, `app.ts:918,954–957`; show sau started bị chặn, cần xem khi 192 thêm Quit to title |
| Việc 8 | title=0 và 7 scenario, không chạy | URL parse đúng; 10 URL trực tiếp + boot chung; 7/7 node --check mã 0, không thực thi | Đạt; `app.ts:114`, các diff scenario trong `current.diff`, `syntax-*.log` |
| Việc 9 | Tách state/DOM/CSS, app nhỏ, không dh.css | Ba file đúng chỗ; riêng 197 app +46/−26; không sửa dh.css nhưng CSS toàn cục gây va lớp | Đạt cấu trúc; F2; `197/app-197.diff`, `title.css:1` |
| Việc 10 | Test trước mã, state/DOM/URL, thiếu ảnh, hooks | 25 test mới đều xanh, giữ 6 test app 195; không xác minh lại được thứ tự biên tập. DOM stub không áp cascade CSS nên bỏ sót F2 | Đạt ca gốc; thiếu kiểm tích hợp CSS/Retry được probe 222 phát hiện |
| Cấm 1 | Git ghi / kit / sync | Không diff kit; verifier 75; 222 không lệnh ghi Git | Đạt trạng thái |
| Cấm 2 | View/sim/rules/dh.css | 0 khối của 197 ở các path này | Đạt; attribution |
| Cấm 3 | Server/browser/mạng | Không chạy trong 222; chưa nghiệm thu hiển thị | Đạt lượt kiểm |
| Cấm 4 | Chép/cắt/sửa ảnh; media Git/public | 0 art nhận; 159 WebP khớp; manifest chỉ thêm art:{}; không ảnh trong status | Đạt trạng thái media |
| Cấm 5 | Âm/nhạc mới/tính năng ngoài việc | Không file âm hoặc chức năng ngoài title/options/art/scripts trong diff 197 | Đạt phạm vi |
| Cấm 6 | Game/worktree khác/Tu Tiên | Chỉ 19 đường quy cho 197 ở dh-codex | Đạt về diff |
| Cấm 7 | Ghi ngoài repo | 222 chỉ C và 222; không xác minh toàn bộ lịch sử 197 | Đạt lượt kiểm |
| Cấm 8 | English; chỉ Hỏa Long/Bạch Long giữ dấu | English UI 9/9; ba câu hướng dẫn chỉ tên Hỏa Long có dấu | Đạt; title.ts:68–72 |
| Kiểm 1 | Trước 568/65 file; sau 593/69 file; kit 75; build xanh | 593/69 file; kit 75; tsc/build 0 | Khớp số sau; không chạy lại trạng thái trước 197 |
| Kiểm 2 | Golden 10/10, SHA-256 c0f977… | 10/10 riêng; SHA-256/MD5 nguyên | Khớp |
| Kiểm 3 | English 9/9, danh sách chuỗi mới | 9/9 riêng; đã so chuỗi trong title/state và bảng art | Khớp; English UI không kiểm CSS cascade |
| Kiểm 4 | Prod 402 file, 35061724 B, 0 lỗi/local | Đúng 402/35061724/0/0; ba host thông tin như 187 | Khớp nguyên số |
| Kiểm 5 | Status 51, 19 đường 197; 32 file cũ không đổi; 7540 file bảo vệ | Status 51, quy 19 đường 197; 473 file bản chép khớp. Không dựng lại 7540 hash lịch sử trước sửa | Khớp phần đo lại cuối; không xác nhận lại chỉ số lịch sử 7540 |
| Kiểm 6 | 0 SVG/canvas/emoji/gradient ở title | 0 kết quả trong ba file title | Khớp; art-source-scan.json |
| Kiểm 7 | App +46/−26; 7 scenario; node check 7/7 | Hash mốc trước 197 khớp; diff app đúng +46/−26; 7 cú pháp mã 0 | Khớp; current.diff và syntax logs |
| Kiểm 8 | Bàn giao trình duyệt 1280/1920, chưa chạy | Đã hợp nhất danh sách và rủi ro mới ở §6; không mở browser | Đạt bàn giao; chưa nghiệm thu hiển thị |


## 4. Số đo lại và rà tích hợp chung

| Kiểm | Mã / số đo lại | Bằng chứng |
|---|---|---|
| Kit → tests → tsc → build trực tiếp | 0 → 0 → 0 → 0; 75 file kit; 69 file test; 593 đạt, 0 đỏ | `check.log`, `fallback-final.json` |
| Golden riêng | 0; 1 file / 10 test đạt, 0 đỏ; MD5 `75f74947dac170d05fd659f99417940e` | `golden.log`, `golden-md5.txt` |
| English riêng | 0; 1 file / 9 test đạt, 0 đỏ | `english-ui.log` |
| UI art --check | 0; 53 icon | `prepare-check.log` |
| Local build + checker | tsc 0, Vite 0, checker 0; ok true; problems **[]** (0 ở mọi loại); files **402**; bytes **35062123**; localHost **5**; vocabularyNotShipped.count **0** | `pack-local.json`, các log build local |
| Production build + checker, sau local | tsc 0, Vite 0, checker 0; ok true; problems **[]** (0 ở mọi loại); files **402**; bytes **35061724**; localHost **0**; vocabularyNotShipped.count **0**; **0 file** chứa `typing-game.local` | `pack-prod.json`, `prod-local-host-scan.json` |
| External cả hai gói | `catlikecoding.com`:1; `developer.download.nvidia.com`:1; `kit.invalid`:1; chỉ nguồn thông tin, không bị checker tính thành problems | Hai JSON gói |
| Balance b35 | 120 lượt; relax **40/40 =100%**; balanced **34/40 =85%**, G1 đạt dải75–90%; challenge **26/40 =65%** | `balance-b35.json`, `.md` |
| Hai bộ seed | **20261023–20261042** và **21261026–21261045**, mỗi mode 20+20 seed; jobs4; 4,685s cả lệnh | `commands.json`, `uptime.txt` |
| Bảng cổng chung B1–B9 của balance subset | Các cổng cần bot khác ghi skip/blocked; không diễn giải subset b35 thành đạt toàn bộ cân bằng | `balance-b35.json` |
| Cú pháp kịch bản | **7/7 mã0**: lib/dh, dh-bench, dh-camera, dh-map-shots, dh-models, dh-pace, ui-preview; chỉ node --check | `syntax-*.log`, `commands.json` |
| Test dò, sau toàn bộ mục3 | **1 file / 3 đỏ**, mã1, đúng ba giả thuyết F2/F3/F4; không sửa mã để làm xanh | `probes/`, `probes.log` |

Không có lệch số cuối nào chưa giải thích được. PSNR trong bảng 194 là metadata của đầu ra đã xác minh MD5/bytes, không được gọi là phép nén hay phép đo PSNR mới. Số 593 chỉ được nhận sau khi xử lý cơ chế pnpm của máy bằng biến môi trường, không bỏ tám test đỏ khỏi tập chạy.

Ước tính idle: **before wave521,0 s, idle273,0 s, 52,4%, 154 quãng**; **after L=1,5, ×1,75: wave475,0 s, idle 226,9 s, 47,8%**. Không có vị trí quái trong mẫu nên chữ hiện thay cho vào Vùng Chữ; chưa mô hình hóa latch 0,3 s, bảng/placement hay ×2 tay. Đây là ước tính, chưa phải phép đo thời gian chơi thật.

| Nhìn trước (s) | Tốc | Wave (s) | Không chữ (s) | Không chữ (%) |
|---:|---:|---:|---:|---:|
|0|1,75|404,1|156,0|38,6|
|0|2|384,6|136,5|35,5|
|0,5|1,75|433,4|185,2|42,7|
|0,5|2|418,7|170,6|40,7|
|1,0|1,75|456,5|208,4|45,6|
|1,0|2|445,7|197,6|44,3|
|1,5|1,75|475,0|226,9|47,8|
|1,5|2|467,4|219,2|46,9|

Rà vòng đời/input: router `input-router.ts:134–140` gỡ capture keydown ở dispose; bảng lỗi `deck-boot.ts:29–32,64,88` gỡ listener khi thành công/dispose; title không thêm keydown host. Các pointer/blur/visibility của app được gỡ ở `app.ts:1144–1148`; listener nằm trên node title bị tháo khỏi DOM và không giữ thêm host reference. `installSkin` có một capture error và một resize sống cùng document (`skin.ts:25–39`); cờ dataset ngăn nhân listener qua các lần startApp/restart. Không coi singleton document đó là rò theo từng ván, nhưng app.dispose không có hàm teardown skin.

Guard `disposed` ở `app.ts:934–943`, `closed/busy` ở `deck-boot.ts:73–89` ngăn late boot; reset tự tua ở `app.ts:637–651`. Router đổi vị trí khởi tạo nhưng dùng cùng intercept/panel/fallback; pace/menu/Thẻ Ôn giữ mã xử lý cũ. Màn tựa chỉ khởi động một lần; API show sau started hiện không mở lại được (`title.ts:118`), nên khi 192 thêm Quit to title phải có hợp đồng tạo/reset title riêng. Chưa có luồng Quit to title trong bốn phiếu để kiểm thực tế.

## 5. Danh sách lỗi và rủi ro

### F1 · blocker · 194 / chuẩn chung · nợ kế thừa được phiếu cũ cho giữ

**File:dòng:** `src/ui/skin.ts:131–137`; `src/ui/tags.ts:472–488`; `src/ui/styles/dh.css:67–82`.

**Ca hỏng:** mở HUD/ô giáp/hình hai rồng hoặc tag còn dùng `icon("armour")`, `icon("dragon")`, `icon("white-dragon")` và `svgIcon`: vẫn tạo SVG bằng mã; panel còn tranh gỗ bằng CSS gradient/shadow. Có **3 SVG skin + 11 đường icon tags**, **19 dòng có gradient trong dh.css**. Đây là nội dung còn hiện trong trạng thái cuối, không phải asset thật theo luật chủ dự án. 194 đã bỏ các hình trong phạm vi và rêu, không tạo mới các phần này; chính phiếu 194 cho phép giữ ba SVG, cấm sửa tags, và giữ bảng gỗ chờ162. **Không kết luận 194 vượt phạm vi hay phải tự sửa vùng cấm**. Xếp blocker phát hành theo quy định 222 “hình vẽ bằng mã”, tách rõ khỏi hồi quy mới.

**Đề xuất:** Claude quy phần ảnh còn lại cho làn được phép và thay bằng ảnh đã nhận (161/UIC-DH-6/tags/162), hoặc xin quyết định phạm vi nghiệm thu rõ từ chủ dự án trước khi coi G5 hoàn tất. Không dùng sửa rộng ngoài quyền của 194 làm cách đóng lỗi.

### F2 · major · 197 · lớp màn tựa ghi đè mọi tiêu đề giao diện

**File:dòng:** `src/ui/styles/title.css:1–9`; `src/ui/title.ts:37`; điểm chịu tác động `src/ui/hud.ts:291`, `src/ui/shop-strip.ts:177`, `src/ui/wave-card.ts:145,161`, `src/ui/results.ts:232,249`.

**Ca hỏng:** Start vào game (kể cả `?title=0`, vì app luôn import title CSS), hoặc mở cửa hàng/kết quả. Lớp `.dh-title` vốn là typography (`dh.css:87–95`) cũng được dùng cho section màn tựa. Quy tắc mới áp `position:absolute; inset:0; z-index:40; background:#17130f; pointer-events:auto; overflow:auto` lên tất cả tiêu đề cũ. Chúng chiếm toàn khối chứa, có nền tối và chặn pointer; lỗi tồn tại từ selector, không phụ thuộc tranh đã nhận. Test DOM cũ không đọc CSS nên 593 test vẫn xanh. Probe1 đọc cả hai CSS và ba consumer thật, xác nhận cả các heading cũ nhận nguyên bộ thuộc tính phủ màn. Chưa đo hình dạng pixel do cấm trình duyệt.

**Đề xuất:** dùng lớp gốc riêng cho màn tựa (ví dụ `.dh-title-screen`), đổi các selector của màn đó, và kiểm lại HUD/shop/wave/results ở hai viewport trước khi duyệt.

### F3 · major · 197 tích hợp 195 · lỗi từ vựng mặc định mất đường Retry

**File:dòng:** `src/app/app.ts:927–938`; `src/ui/title.ts:58–80`; `src/ui/title-state.ts:15–19,25–27`; đối chiếu đường phục hồi `src/app/deck-boot.ts:73–89`.

**Ca hỏng:** URL thường, không `title=0`, cổng build trống; lần nạp từ đầu lỗi mạng/rỗng/69 từ. `deckBoot` là hàm dispose rỗng, app gọi buildDeck một lần; title chỉ có Start đang disabled, không có Retry. Đợi mạng phục hồi rồi Enter/Esc/arrows/click đều không thể gọi buildDeck lại; chỉ tải lại cả trang mới thử được. Với cổng cấu hình thì có thể đi cổng nhưng vẫn không có Retry. Dòng “Check your connection and try again.” không có thao tác thử lại. Probe2 xác nhận title blocked, Start tắt, **0 nút Retry**. 197 giữ chặn game đúng yêu cầu nhưng đánh mất phục hồi của 195; browser-handoff cũ đã tự ghi “không thêm Retry”, không phải một quyết định của chủ dự án trong phiếu gốc. Xếp major cho đường phục hồi bị mất, không gọi trạng thái Start tắt hợp lệ là lỗi kẹt phím của router.

**Đề xuất:** giữ đường Retry của 195 trên title, chỉ reset/settle lại nguồn words và chặn busy/disposed/double boot như hiện có; giữ cổng hoạt động.

### F4 · major · 195 · test thường phụ thuộc dữ liệu ngoài repo, Git bỏ qua

**File:dòng:** `tests/app/idle-estimate.test.ts:16–23`; quy tắc độc lập `docs/games/DEPLOY_INDEPENDENCE.md:20` (xem §1, điều2).

**Ca hỏng:** clone độc lập game hoặc CI không có `../dragon-hold/tmp/map1-audit/feel-35-1280/samples.json`; `readFileSync` ném ENOENT và suite thường đỏ trước assertion. 222 chỉ xanh vì làm đúng bước chép mẫu được chỉ định, không chứng minh clone sạch xanh. Probe3 xác nhận path bắt buộc thoát ngoài game root. Lỗi đã có trong nguồn 195; không phải số hash mẫu bị lệch. Xếp major về tính tái lập: check của bản chép có fixture vẫn xanh, chưa tự nhận đã chạy check trên clone sạch.

**Đề xuất:** đưa fixture ổn định nhỏ vào tests/fixtures hoặc tách phép đối chiếu mẫu audit thành lệnh kiểm tùy chọn có tham số; unit test thường dùng dữ liệu nằm trong repo.

### F5 · note · 195 / đường ×2 kế thừa · giao điểm đồng hồ âm/VFX

**File:dòng:** `src/audio/map-events.ts:245–247`; `src/view/fx.ts:1294,1334–1339`; `src/view/telegraphs.ts:509`; `src/sim/combat.ts:424–470`.

**Ca rủi ro:** khi hệ số sim đổi lúc còn một sự kiện trình bày đang sống, âm skill/giới hạn warning được hẹn theo durationMs thời gian thật, telegraph tiến theo worldDt, burn FX lại tiến theo đồng hồ hit-stop không nhân tua. Ví dụ duration 2 s ở ×1,75 tương ứng 1,143 s sim nhưng lịch âm vẫn 2 s, có khả năng lệch 0,857 s nếu hệ số giữ xuyên sự kiện. Đây là suy luận về hợp đồng đồng hồ, **chưa chứng minh ca auto tái hiện**: auto tắt khi có quái trong Vùng Chữ; Héo lan chỉ tính quái inWordZone nên không có nguồn Héo mới trong trạng thái auto hợp lệ. ×2 tay vẫn là đường cũ. Không thấy sửa sim hoặc nhân tốc nhạc.

**Đề xuất:** Claude nghe/xem chuyển ×1/×1,75/×2 qua telegraph, burn, Héo lan và lúc mở/đóng bảng; chỉ giao sửa đồng hồ nếu bắt được lệch, không sửa view/audio ngoài phiếu 195 trong lượt này.

## 6. Việc Claude cần kiểm trên trình duyệt

Thực hiện từng dòng ở **cả 1280×720 và 1920×1080**, sau khi xử lý F2 và thống nhất F3. Danh sách kế thừa `197/browser-handoff.md` và thêm rủi ro của222; **Codex chưa chạy**.

| Thao tác | Điều cần thấy |
|---|---|
| Mở URL thường không wpm, làm chậm từng nguồn | Loading N of 4 đúng, Start tắt và focus rõ trước đủ 4; đủ 4 mới có Press Enter to start; không có từ/sim chạy nền |
| Bấm/Enter Start, giữ Enter, bấm đúp; lặp với wpm=35 | Không wpm: pace trước begin; có wpm: begin thẳng; một ván/router/loop; giữ Enter không bỏ qua lựa chọn ngoài ý muốn |
| Dùng bốn mũi tên, rê chuột Start/cổng, Enter, Esc, gõ chữ | Focus đi vòng đúng, Enter theo focus, Esc ở title; chữ không vào sim; không focus mờ khó đọc |
| Đi hết Start→prep→wave→break→shop/edit→debut→victory/defeat | Hỏa Long, Loadout, Wave, Wordbook và tiêu đề các bảng không phủ nền tối toàn panel hoặc chặn nút sau sửa F2 |
| Build cổng trống rồi có URL hợp lệ; dùng chuột/Enter khi tải và blocked | Trống không nút/ô thừa; có đúng href + target_top, cổng vẫn dùng trong khi tải/lỗi |
| Giả lập lỗi mạng, rỗng,69 từ rồi phục hồi; thử Retry nhanh nhiều lần | Thông báo đúng lý do; Start tắt; đường Retry mặc định sau sửa F3 tải lại words một lần, không mất các nguồn đã xong; thành công chỉ boot một lần; title=0 vẫn phục hồi |
| Giữ cả 3 art null; kiểm Network/console | 0 request ui/title; nền phẳng #17130f, chữ logo, không huy hiệu; warn một lần mỗi tên |
| Sau chủ dự án/Claude nhận 119, đặt accepted="119" và chuẩn bị theo quyền riêng | Nền cover/cắt giữa, logo vùng 25–75%×6–30%, menu 3–35%×55–92%; alpha/alt/cỡ chữ/focus rõ; không tự nhận tranh trong 222 |
| Chặn từng URL backdrop/logo/emblem/loading đã nhận | Nền phẳng/chữ logo/ẩn huy hiệu đúng, warn 1/tên; loading chỉ trong lúc tải |
| Chạy lại với title=0; pause→speed→resume/countdown; mở Thẻ Ôn | Phím pace/menu/review giữ hợp đồng cũ; sim đứng khi bảng mở, chữ không mất; không nhân listener qua replay |
| Đợi quãng trống dài, chạm biên có chữ, thử Alt+→, mở bảng/đặt/sửa | Auto bật sau0,3 s, hủy sớm trước vùng chữ, warning/break không auto; ×2 tay thắng; bảng/placement/pause/countdown không tua |
| Quan sát/nghe telegraph, burn, Héo lan khi đổi tua và pause | Dấu báo/âm/đòn/FX khớp sự kiện; không đổi cao độ nhạc; ghi hệ số và mốc nếu có lệch F5 |
| Replay/Retry nhiều lần, dispose khi từng promise còn pending rồi mở app mới | Không late boot, không thêm listener, không state tua rò sang ván mới; handle.title/state phản ánh đúng |
| Khi gộp 192/R2, mở Settings/Sound trên title và trong trận, Quit to title | F1/F2/Esc ưu tiên bảng trước intercept title; quickSlot đúng góc; camera hooks chạy; có hợp đồng reset title vì show hiện từ chối started |
| Chạy lại7 scenario đã thêm title=0 và các scenario dùng boot chung | Tất cả bỏ qua title đúng, không timeout chờ ready, không thay đổi các luồng scenario ngoài cờ |

Không đánh dấu đã xong nút Settings/Sound, camera R2, tranh 119 hay khung 162 chỉ từ việc chừa móc trong 197.

## 7. Bảo toàn và dọn

Kết quả cuối được điền từ lần kiểm bảo toàn sau khi hoàn tất báo cáo và test dò; xem [verification-final.json](222/verification-final.json). SHA kiểm toàn bộ danh sách Git-listed chứ không gồm dist/tmp/node_modules; probe là file riêng dưới tests/_probe-222 nên cũng không nằm trong danh sách gốc473.

| Hạng mục cuối | Số / kết quả |
|---|---|
| cmp status trước/sau | **Giống từng byte**, 51 dòng =24 sửa +27 mới |
| Danh sách Git-listed trước/sau | **473/473**, giống từng byte, 0 thêm/bớt |
| SHA-256 nguồn trước/sau | **473/473 khớp**, 0 khác |
| HEAD trước/sau | **Giống nhau**, 6aa593a2dce6637cccbe24a58709b86f7127f607 |
| find worktree -newer marker, trước khi xóa | **0 đường dẫn** |
| Bản chép ban đầu / sau các lệnh kiểm | **473/473 khớp nguồn**, 0 khác ở cả hai lần |
| SHA-256 của bốn manifest checksum | Cùng **3dd0b867c9685ec6e6253d2a53a0902c40c886f4d6e0fc161e366298e9e2d4aa** |
| Mẫu nguồn | SHA-256 trước/sau trùng d9e4220369c0f6131db82c2ed41073ff108b58e5f40a79b86abc79246ce1f0f7 |
| Dọn C | **Đã gỡ symlink public/assets trước, rồi xóa toàn bộ C**; công cụ chặn rm -rf, dùng API xóa đúng cây tạm có kiểm đường dẫn và không theo symlink |
| Media thật sau dọn | **160/160 file**, danh sách giống đầu lượt; không mất icon/manifest |
| Phần ghi của 222 ở repo cha | Chỉ thêm **222-report.md** và **222/**; không sửa nguồn hoặc báo cáo khác |
| Thay đổi làn khác trong status | Mốc after theo thứ tự yêu cầu: **11 dòng thêm**, 0 bớt. Mốc end sau dọn: **9 dòng thêm**, 0 bớt so với before; phần ghi riêng của 222 vẫn đúng 2 dòng |

Thay đổi đồng thời ngoài phần ghi của 222 (không suy đoán làn sở hữu từ tên file):

- `?? docs/changelog/2026-10-30-fix-227.md`
- `?? docs/codex-queue/203-report.md`
- `?? docs/codex-queue/224-report.md`
- `?? docs/codex-queue/225-report.md`
- `?? docs/codex-queue/225/`
- `?? docs/codex-queue/228-report.md`
- `?? docs/codex-queue/228/`
- `?? docs/codex-queue/229-report.md`
- `?? docs/codex-queue/229/`
- `?? docs/codex-queue/230-ts-recheck-206-220.md`
- `?? docs/codex-queue/231-td-recheck-199-202.md`

Sau bước chép log và dọn, `parent-status-end.txt` ghi hai dòng `230-ts-recheck-206-220.md` và `231-td-recheck-199-202.md` không còn xuất hiện so với mốc after. Đây là biến động đồng thời của làn khác; 222 không xóa hoặc sửa hai file đó. Vì hai dòng chưa có ở before, so end với before còn **9 dòng ngoài 222 được thêm**, không có dòng bị bớt. Chi tiết ba mốc trong `verification-final.json`.

Parent status chỉ mô tả đường dẫn/trạng thái; file vốn đã dirty và được làn khác sửa thêm nhưng giữ cùng mã status không thể phát hiện bằng phép so này. 222 không nhận đã chứng minh mọi byte của repo cha bất biến, chỉ chứng minh các đường ghi của mình và toàn bộ worktree được kiểm.


## 8. File đã đọc và bằng chứng

Bảng sau ghi tổng số dòng của **mọi đường nguồn thay đổi** đã đọc bằng diff/nội dung mới và các ngữ cảnh liên quan. Không dùng số dòng để nhận đã nghiệm thu hiển thị; file cũ dài được rà diff và các vùng chức năng được trích ở trên. Danh sách và SHA riêng ở `changed-files-read.tsv`.

| Đường trong worktree | Dòng | Phiếu |
|---|---:|---|

| `README.md` | 44 | 187, 194 |
| `package.json` | 37 | 194 |
| `scripts/visual/scenarios/dh-bench.mjs` | 100 | 197 |
| `scripts/visual/scenarios/dh-camera.mjs` | 33 | 197 |
| `scripts/visual/scenarios/dh-map-shots.mjs` | 50 | 197 |
| `scripts/visual/scenarios/dh-models.mjs` | 254 | 197 |
| `scripts/visual/scenarios/dh-pace.mjs` | 296 | 197 |
| `scripts/visual/scenarios/lib/dh.mjs` | 270 | 197 |
| `scripts/visual/scenarios/ui-preview.mjs` | 134 | 197 |
| `src/app/app.css` | 296 | 195 |
| `src/app/app.ts` | 1154 | 187, 195, 197 |
| `src/app/learning.ts` | 510 | 187, 195 |
| `src/app/portal.ts` | 34 | 187 |
| `src/ui/debut-card.ts` | 165 | 194 |
| `src/ui/hud.ts` | 582 | 194 |
| `src/ui/learning-frame.ts` | 713 | 194 |
| `src/ui/placement-ui.ts` | 775 | 194 |
| `src/ui/results.ts` | 454 | 187, 194 |
| `src/ui/skin.ts` | 186 | 194 |
| `src/ui/styles/dh.css` | 1710 | 194 |
| `src/ui/wave-card.ts` | 415 | 194 |
| `tests/app/portal.test.ts` | 92 | 187 |
| `tests/ui/results-screen.test.ts` | 242 | 187, 194 |
| `vite.config.ts` | 53 | 187 |
| `docs/changelog/2026-10-29-portal-link.md` | 41 | 187 |
| `docs/changelog/2026-10-30-deck-notice-and-idle-speed.md` | 9 | 195 |
| `docs/changelog/2026-10-30-title-screen.md` | 7 | 197 |
| `docs/changelog/2026-10-30-ui-art-icons.md` | 13 | 194 |
| `scripts/balance/idle-estimate.d.mts` | 13 | 195 |
| `scripts/balance/idle-estimate.mjs` | 43 | 195 |
| `scripts/ui-art/prepare.mjs` | 213 | 194, 197 |
| `src/app/deck-boot.ts` | 93 | 195 |
| `src/app/idle-speed.ts` | 77 | 195 |
| `src/app/quality.ts` | 12 | 195 |
| `src/ui/styles/title.css` | 65 | 197 |
| `src/ui/title-state.ts` | 30 | 197 |
| `src/ui/title.ts` | 127 | 197 |
| `src/ui/ui-art.json` | 742 | 194, 197 |
| `tests/app/deck-app.test.ts` | 147 | 195, 197 |
| `tests/app/deck-boot.test.ts` | 110 | 195 |
| `tests/app/idle-estimate.test.ts` | 37 | 195 |
| `tests/app/idle-speed.test.ts` | 162 | 195 |
| `tests/app/pinned-deck.test.ts` | 24 | 195 |
| `tests/app/quality.test.ts` | 12 | 195 |
| `tests/app/title-options.test.ts` | 8 | 197 |
| `tests/assets/title-art.test.ts` | 40 | 197 |
| `tests/assets/ui-art.test.ts` | 95 | 194 |
| `tests/portal-build.test.ts` | 60 | 187 |
| `tests/ui/title-state.test.ts` | 45 | 197 |
| `tests/ui/title.test.ts` | 101 | 197 |
| `tests/ui/ui-art.test.ts` | 139 | 194 |

Các tài liệu/phụ trợ đã đọc (đoạn liên quan của tài liệu dài, toàn bộ bốn phiếu/báo cáo và snapshot đối chiếu):

| Đường repo cha | Dòng |
|---|---:|

| `AGENTS.md` | 75 |
| `docs/HANDOFF_CURRENT.md` | 333 |
| `tools/codex-run/README.md` | 68 |
| `docs/games/IN_GAME_SETTINGS.md` | 53 |
| `docs/games/DEPLOY_INDEPENDENCE.md` | 335 |
| `docs/games/dragon-lane/06-other-systems.md` | 317 |
| `docs/codex-queue/187-dh-portal-link.md` | 26 |
| `docs/codex-queue/194-dh-ui-art-icons.md` | 169 |
| `docs/codex-queue/195-dh-deck-notice-and-idle-speed.md` | 143 |
| `docs/codex-queue/197-dh-title-screen.md` | 129 |
| `docs/codex-queue/187-report.md` | 110 |
| `docs/codex-queue/194-report.md` | 78 |
| `docs/codex-queue/195-report.md` | 118 |
| `docs/codex-queue/197-report.md` | 79 |
| `docs/codex-queue/187/status-final.txt` | 10 |
| `docs/codex-queue/194/files-194.txt` | 16 |
| `docs/codex-queue/195/files-195.txt` | 15 |
| `docs/codex-queue/197/files-197.txt` | 19 |
| `docs/codex-queue/194/task.diff` | 1796 |
| `docs/codex-queue/195/task.diff` | 966 |
| `docs/codex-queue/195/app-195.diff` | 137 |
| `docs/codex-queue/195/learning-195.diff` | 78 |
| `docs/codex-queue/197/app-197.diff` | 149 |
| `docs/codex-queue/197/browser-handoff.md` | 14 |
| `docs/codex-queue/194/media-files.txt` | 160 |
| `docs/codex-queue/194/integration.md` | 42 |
| `docs/codex-queue/194/remaining-svg.md` | 22 |
| `docs/codex-queue/194/start.diff` | 434 |
| `docs/codex-queue/197/resume2-start.diff` | 1302 |
| `docs/codex-queue/197/resume2-before.json` | 38 |
| `docs/codex-queue/187/pack-final.json` | 27 |
| `docs/codex-queue/187/pack-local.json` | 27 |
| `docs/codex-queue/195/deploy-pack.json` | 27 |
| `docs/codex-queue/197/deploy-pack.json` | 27 |
| `.agents/skills/game-ci-resumable/SKILL.md` | 30 |
| `.agents/skills/game-ci-resumable/references/ci-map.md` | 38 |

Nguồn phụ trợ trong worktree đã đọc/tra cứu vùng liên quan:

| Đường | Dòng |
|---|---:|

| `AGENTS.md` | 136 |
| `src/app/input-router.ts` | 143 |
| `src/app/loop.ts` | 101 |
| `src/sim/words.ts` | 879 |
| `src/sim/movement.ts` | 425 |
| `src/sim/spawn.ts` | 287 |
| `src/sim/combat.ts` | 940 |
| `src/sim/world.ts` | 520 |
| `src/audio/map-events.ts` | 473 |
| `src/view/fx.ts` | 1372 |
| `src/view/telegraphs.ts` | 523 |
| `src/view/models.ts` | 278 |
| `src/view/stage.ts` | 570 |
| `src/view/heroes.ts` | 481 |
| `tests/english-ui.test.ts` | 118 |
| `tests/deploy-pack.test.ts` | 76 |
| `vitest.config.ts` | 9 |
| `pnpm-workspace.yaml` | 2 |
| `src/kit/learning/contract.ts` | 44 |

Ngoài ra đọc manifest media thật (53 mục), từng byte 159 WebP để MD5/bytes, samples để hash/ước tính; skill QA `/Users/toandx/.agents/skills/threejs-qa-release/SKILL.md`; mã pnpm cục bộ ở `~/.cache/node/corepack/v1/pnpm/11.21.0/dist/pnpm.mjs` quanh `runDepsStatusCheck` và biến môi trường. Không đọc bí mật hoặc token.

Log chính: `check.log`, `pnpm-check-initial.log`, `check-fallback.log`, `check-final.log`, `golden.log`, `english-ui.log`, `prepare-check.log`, `pack-local.json`, `pack-prod.json`, `balance-b35.json`, `balance-b35.md`, `idle-estimate.json`, `commands.json`, `fallback-final.json`, `probes.log`, các status/hash và `verification-final.json`. Test dò và log riêng ở `probes/`; không chạy chung với suite gốc. `current.diff`/`current-numstat.txt` là diff thật đọc lại; `attribution.json` dùng cho 223.

Bỏ qua theo phiếu: không sửa bất kỳ lỗi nào; không server/trình duyệt/mạng; không chạy prepare ghi ảnh thật; không build/test ở worktree gốc hoặc game khác; không kit sync/golden update; không tạo ảnh/âm; không commit/push/reset/clean/stash. Claude còn xử lý danh sách lỗi, nghiệm thu hai cỡ và quyết định nhận ảnh trước commit. Không có frame chụp mới cần prune.
