# Phiếu 194 · Dragonhold · Gắn ảnh icon UI

**Hoàn tất phần mã và mười mục kiểm tự động.** Đã chuẩn bị 53 icon (36 đã nhận, 17 tạm), gắn 30/36 icon đã nhận vào những chỗ được phép, thay SVG/emoji trong phạm vi và bỏ hai mảng rêu CSS. Sáu icon còn lại chỉ chuẩn bị đúng đề bài. Chưa kiểm trình duyệt; bước đó giao Claude sau duyệt diff.

## 1. Điều kiện đầu, phạm vi và công việc 187

Làm tại `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD trước/sau `6aa593a2dce6637cccbe24a58709b86f7127f607`. Có `187-report.md`; worktree ban đầu có đúng 10 file của 187 được liệt kê trong phiếu, không có file lạ. Repo cha có công việc đồng thời của các làn khác; không dùng trạng thái repo cha để kết luận worktree bẩn.

Đã lưu [trạng thái ban đầu](194/start-status.txt), [diff ban đầu](194/start.diff), [mốc và golden](194/before.json). [Diff riêng của 194](194/task.diff) tính từ trạng thái đó, để Claude tách hai phiếu khi duyệt. [Xác minh phần 187 giữ nguyên](194/187-preserved.json).

Trong các file dùng chung:

- `README.md:42–44`: 194 chỉ thêm đoạn “Ảnh icon UI”; hướng dẫn portal của 187 giữ nguyên.
- `src/ui/results.ts`: 194 đổi sao (`239`, `320–323`), năm ô số (`299–303`, `327–331`), viên trạng thái (`340–350`), ảnh/nhãn nghe từ (`356–357`), ảnh Replay/Retry (`365`). Khối portal có điều kiện và gợi ý bàn phím của 187 giữ nguyên.
- `tests/ui/results-screen.test.ts`: 194 thêm `ariaLabel` vào stub, ghi rõ kiểu trả về của fixture `assigned` tại dòng 56 và thêm hai test “results UI art (194)” tại dòng 60–96. Các test portal của 187 giữ nguyên.
- Năm file tracked chỉ thuộc 187 (`src/app/app.ts`, `src/app/learning.ts`, `src/app/portal.ts`, `tests/app/portal.test.ts`, `vite.config.ts`) được đối chiếu byte với trạng thái đầu và không thay đổi. Hai file untracked của 187 (`tests/portal-build.test.ts`, changelog portal) không sửa.

Không chạy lệnh Git ghi, không đồng bộ kit, không server/trình duyệt/mạng, không sinh ảnh nguồn. Chỉ chạy check/build/test được phiếu này yêu cầu trong worktree Dragonhold; không chạy game khác. Không chạm Tu Tiên, `src/kit`, `src/view`, `src/sim`, `src/content`, `src/app`, `src/ui/tags.ts`, nút Settings/Sound trong trận.

## 2. Đã làm

| Nhóm | Đường dẫn trong worktree | Kết quả |
| --- | --- | --- |
| Bảng chọn | `src/ui/ui-art.json` | Version 1; 53 mục; 36 mục nhận đúng 137–140; 17 mục tạm; tên/key duy nhất. Roar lấy `icons/normalized/015-skill-roar`. Không lấy bản thử hoặc bản chưa nhận. |
| Đóng gói | `scripts/ui-art/prepare.mjs`, `package.json` | Lệnh chuẩn bị, `--out`, `--check`, `--help`; giữ alpha, strip metadata, quality 90/alpha 100, Lanczos khi thiếu cỡ, không phóng to. PSNR dưới 35 chuyển lossless. Chuyển hết trước khi xuất; manifest đổi sau cùng qua rename; lỗi xuất thì hoàn lại file đã thay. Scratch nằm trong `tmp/ui-art/` của worktree. |
| Runtime | `src/ui/skin.ts`, `src/ui/styles/dh.css` | Bảng URL tên/key, cỡ ảnh, alt trang trí hoặc có nhãn, listener lỗi capture một lần/document; cảnh báo một lần/URL và `hidden`. Không hình thay thế. Bỏ SVG đã thay, bóng quái SVG, rêu bảng và quy tắc tô sao SVG. |
| Gắn HUD/thẻ/ô đặt | `src/ui/hud.ts`, `wave-card.ts`, `debut-card.ts`, `placement-ui.ts` | Icon A/B, ảnh family theo `family`; chỉ toast `rejected` thêm `deny`; nút pause/camera có `aria-label` bằng title. Shop-strip dùng key cũ nên tự nhận ảnh qua bảng, không cần sửa file. |
| Học/kết quả | `src/ui/learning-frame.ts`, `results.ts` | Hàm markup thuần cho từ đã gõ và Thẻ Ôn; ảnh loa/dấu đúng/NEW; sao sáng/tắt, năm ô số, Wordbook và Retry/Replay. Nút nghe từ có nhãn tiếng Anh. |
| Test trước mã | `tests/ui/ui-art.test.ts`, `tests/assets/ui-art.test.ts` | Bảng, mọi tên/key, chọn cỡ, các chỗ gọi cố định/dữ liệu, ảnh lỗi, listener capture, không emoji trong chuỗi/template/CSS content, markup khung học. Fixture script nằm trong `tmp/ui-art-test/`, tự dọn; kiểm alpha, kích thước, MD5/byte, check chỉ đọc, lỗi nguồn, manifest thừa và giữ đầu ra cũ. |
| Test kết quả/hướng dẫn | `tests/ui/results-screen.test.ts`, `README.md`, `docs/changelog/2026-10-30-ui-art-icons.md` | Kiểm sao, năm ô số, năm trạng thái và nhãn nghe; hướng dẫn lệnh và số đo. |

Ô mặc định 20; Retry/trạng thái/ô số 25; sao 46; loa/dấu đúng khung học 18; loa Thẻ Ôn 22. Nút nghe Wordbook có ô 28 với padding 4 để chứa ảnh 20. Ảnh có `object-fit: contain`; không thêm filter, blend hay opacity để sửa màu. `star-unlit` giữ nguyên ảnh, không dựng ổ sao; chờ 196.

Đã giữ các trạng thái có sẵn làm mờ ảnh cùng điều khiển: `dh-btn:disabled/is-off` (saturate 0,55), ô potion rỗng (opacity 0,22, grayscale), kỹ năng đã dùng (0,55), lane tối (0,45), ô mang theo tắt/thiếu tiền, marker mờ và menu thiếu tiền; khung học idle (0,55). Hoạt ảnh sao xuất hiện vốn có giữ nguyên. Không đổi những quy tắc này để chỉnh màu ảnh.

Biến `--dh-moss`, `--dh-moss-hi` giữ nguyên cho `app.css`. Tìm toàn bộ nguồn chỉ còn một quy tắc ngoài phạm vi `src/app/app.css:115` đặt `bottom: 0` cho `.dh-panel.dh-pacecard::after`; nó không khai báo `content`, nên sau khi xóa rêu không tạo giả phần tử và không có chức năng nào phụ thuộc. Không sửa `app.css`.

## 3. Test và mười mục kiểm

| Mục | Kết quả, số đo | Bằng chứng |
| --- | --- | --- |
| 1. `pnpm check` trước/sau | Trước: mã 0, **57 file, 509/509 test**. Cuối: mã 0, **59 file, 526/526 test**, kit hash/TypeScript/Vite xanh. Không có test thời gian đỏ nên không cần chạy riêng ba lần. | [Trước](194/check-before.log), [cuối](194/check-final.log) |
| Test trước mã | Hai file đỏ khi bảng/API/script chưa tồn tại: 4 test script đỏ và lỗi thu thập test runtime. Lượt đầu sau mã phát hiện chữ `False` của ImageMagick khác chữ thường trong test; đã sửa chuẩn hóa. Lượt check đầu phát hiện thiếu trường/kiểu sự kiện trong fixture kết quả; đã sửa fixture đúng hợp đồng, không nới kiểm. Test tập trung sau sửa: **29/29**. | [Đỏ](194/test-red.log), [lượt đầu](194/test-first.log), [tập trung](194/test-focused.log), [check có lỗi fixture](194/check-after.log), [cuối](194/check-final.log) |
| 2. Ván vàng | **10/10 xanh**. MD5 `tests/golden/m0.json` trước/sau cùng **`75f74947dac170d05fd659f99417940e`**. | [Golden và English](194/golden-english.log), [số đo](194/verification.json) |
| 3. English UI | **9/9 xanh**; test mới quét chuỗi/template bằng AST TypeScript và CSS `content` không còn pictograph, FE0F hoặc dấu đúng bằng ký tự. | [Log](194/golden-english.log), [check cuối](194/check-final.log) |
| 4. Chuẩn bị thật | Mã 0: **159 WebP + 1 manifest**, từ **142 PNG nguồn**. Tổng **1.262.593 byte**, gồm manifest **62.549 byte**. | [prepare.log](194/prepare.log), [số đo](194/verification.json) |
| 5. Check ảnh thật | `pnpm prepare-ui-art --check --art-src ../dragon-hold/art-src`: mã **0**, 53 icon, check OK. Không ghi file. | [check.log](194/check.log) |
| 6. Gói triển khai | `pnpm deploy:pack`: mã **0**, **0 lỗi**, 0 local-host. Kiểm JSON trên gói đó: `ok: true`; **159 ảnh UI trong dist**, toàn gói 402 file. Vite có cảnh báo chunk lớn vốn có, không phải lỗi. | [Log](194/deploy-pack.log), [JSON](194/deploy-pack.json), [inventory](194/verification.json) |
| 7. Tờ xem | `games/.wt-dh-codex/tmp/ui-art/194-sheet.jpg`, **337.218 byte**. 53 mục, PNG/WebP cạnh nhau ở 64 px trên vỏ cây `#2b2118` và kem `#f1e3c4`, đủ tên. Chỉ giữ tại tmp cho Claude; không chép vào docs/public. Đã xem tờ cuối và dọn 53 ảnh ghép thô do mình tạo bằng capture-prune, giữ tờ xem. | [Prune thử](194/prune-dry-run.txt), [đã dọn](194/prune-apply.txt) |
| 8. Bảng gắn/SVG | **30 icon nhận đã gắn, 6 chỉ chuẩn bị**. `skin.ts` còn đúng ba SVG; `tags.ts` có 11 đường icon giữ nguyên theo lệnh cấm sửa. | [36 dòng gắn](194/integration.md), [JSON](194/integration.json), [SVG còn lại và lý do](194/remaining-svg.md) |
| 9. Git/ignore | Trạng thái cuối chỉ có file 194 và 187 đã ghi riêng. WebP và manifest đều bị bỏ qua ở checkout chính bởi `.git/info/exclude:7:public/assets`; bảng JSON không bị bỏ qua (exit 1). HEAD không đổi. | [Status](194/status-final.txt), [ignore](194/check-ignore.txt), [diff riêng](194/task.diff) |
| 10. Danh sách media | **160 dòng** đường, byte, MD5 của toàn bộ thư mục icon đầu ra; sẵn cho Claude media:push. | [media-files.txt](194/media-files.txt) |

| Cỡ | WebP | Tổng byte | PSNR nhỏ nhất sau chọn kiểu nén | File lossless |
| --- | --- | --- | --- | --- |
| 64 | 53 | 142.184 | 35,1794 dB | 13 |
| 128 | 53 | 350.914 | 35,0822 dB | 6 |
| 256 | 53 | 706.946 | 35,2564 dB | 0 |

Lossless 64: `dragon-rage`, `camera-reset`, `deny`, `lock`, `upgrade`, `seal-lit`, `edge-arrow`, `stat-accuracy`, `stat-new-words`, `retry`, `status-learned`, `status-new`, `gold`. Lossless 128: `dragon-rage`, `seal-lit`, `status-learned`, `gold`, `skill-ultimate`, `herb-hut`. Tên đủ đuôi file có trong prepare.log và verification.json.

## 4. Chưa gắn và việc Claude cần xem

- `fast-forward`, `keyboard`: chỉ chuẩn bị, chỗ gọi ở `src/app` ngoài phiếu. `seal-lit`, `seal-unlit`, `edge-arrow`: chỉ chuẩn bị vì `src/ui/tags.ts` bị cấm sửa. `lock`: chưa có chỗ khóa. `easier` và mọi tên/bản chưa nhận không được chọn.
- 17 icon cũ tiếp tục là ảnh tạm theo phiếu; khi 163/164 được nhận, sửa nguồn và cờ interim trong bảng, không cần đổi mã runtime. Tăng version khi cần phá cache URL. Giữ `015-skill-roar` cho lượt này.
- Không đổi bảng gỗ CSS (chờ 162), ổ sao (196), chân dung rồng (UIC-DH-6), armour (161), hoặc Settings/Sound (192/180). Danh sách SVG tags chưa có số phiếu gắn trong đề bài; không tự đoán số.
- Claude duyệt `194/task.diff` cùng `194/start.diff`, đặc biệt `hud.ts`, `dh.css`, rồi xử lý thứ tự map-pilot → dh-vfx → dh-codex và xung đột với 192. Chưa có bằng chứng bố cục trình duyệt; xem 1280 và 1920, nhất là hàng Wave/Chain thêm ảnh, Wordbook 25 px và sao tối chưa có ổ.
- Sau khi gộp main, Claude chạy lại `pnpm prepare-ui-art` ở checkout chính với nguồn phù hợp, rồi `media:push` theo `194/media-files.txt`. Phiếu này không commit, push hoặc tải media lên.
