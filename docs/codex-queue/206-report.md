# Phiếu 206 · Last Line · Đường ảnh UI

Ngày 30/10/2026. Phần mã và kiểm bằng Node đã làm tại `games/.wt-ts-art`, nhánh `ts-art`, từ `79db62851e00eadeca7bfd44c10c0c682a9cec8d`. Lúc bắt đầu `git status --short -uall` sạch, có `node_modules/.bin/vitest`. Chưa commit, chưa gộp, chưa đẩy media. Claude còn phải duyệt diff và kiểm trình duyệt theo phiếu.

## Đã làm

- `scripts/ui-art/selection.json`: 37 mục, đúng 15 mục nhận và 22 mục chờ; đủ tên tiếng Anh, phiếu, nguồn và chỗ ghi nhận. `gun-phao` trỏ nguồn `gun-phao-sao`, kể cả bản v2 thực tế trên đĩa.
- `scripts/ui-art/prepare.mjs`, lệnh `ui-art:prepare`: chọn đúng nguồn theo cỡ, không phóng to media; cắt nền theo crop; chuyển WebP, đo PSNR, nâng lossless/q92 theo luật. Dựng trong `tmp/`, chuyển sau khi đủ, manifest và bảng chạy ghi cuối; có hoàn tác khi chuyển thất bại. Kiểm md5/byte/bảng và WebP lạ; lần chạy lại không ghi lại file. Chỉ xóa đầu ra thuộc manifest cũ khi vai hết được nhận.
- `src/view/ui-art.json` được sinh; `src/view/ui-art.ts` chứa ánh xạ vai, `BOX`, chọn mật độ, HTML/thuộc tính DOM và listener lỗi dùng chung. Không có ảnh thay khi thiếu; cảnh báo một lần mỗi vai hoặc URL. `BOX` và các cỡ CSS được test đối chiếu để không thêm biến vào theme.
- Thêm ảnh vào các màn và HUD, sẵn điểm gắn sáu nền chờ. README, dòng Layout trong AGENTS và changelog `docs/changelog/2026-10-30-ui-art.md` đã cập nhật.
- Viết test trước phần triển khai; `tests/golden/ui-text-206.json` sinh đúng một lần từ mã cũ, không sinh lại sau khi sửa. Có 19 test mới, gồm test thuần, HTML, media thật và fixture chuyển ảnh/alpha/không ghi lại/ảnh hỏng/lỗi chuyển giữa chừng.
- Viết `scripts/visual/scenarios/survival-ui-art.mjs`, chỉ kiểm cú pháp. Đặt khóa `survival.guide` ngay sau xóa `survival.stages` như phiếu; lấy cỡ từ chính `BOX`, kiểm ảnh, khổ, tràn, thẻ, bến, dòng chữ và byte từ Resource Timing. Không sửa kịch bản cũ.

## Bảng gắn

Đường mã trong bảng tính từ `games/.wt-ts-art/`. Cỡ là CSS ở 720p; 1080p nhân 1,5. Hai chỗ dùng chung `item()` cho Hành trình và kết quả.

| Mã | File:dòng sau sửa | Vai | Ô 720p |
|---|---|---|---|
| LL-15 | `src/view/screens.ts:91` | `gun-xung/tia/tan/ray/phao` | 64 × 64 |
| LL-17 | `src/app/journey.ts:127`, `src/view/screens.ts:48` | `stage-c1-s1…c1-s4`, gồm hàng khóa | 96 × 54 |
| LL-18 | `src/view/screens-journey.ts:69` | `stage-<id>` | 760 × 120 |
| LL-20 | `src/view/screens-journey.ts:78` | Chân dung từng quái trong danh sách | 40 × 40 |
| LL-21 | `src/view/screens-journey.ts:80` | `foe-brute/pack-leader/shield-guard/splitter` theo mục dạy | 32 × 32 |
| LL-25 | `src/view/screens-journey.ts:99` | Năm vai súng | 72 × 72 |
| LL-26 | `src/view/screens-journey.ts:103` và dòng kế | Vai quái theo `goodRows`, `poorRows`, giữ dấu phẩy | 20 × 20 |
| LL-27 | `src/view/screens-journey.ts:109` | Vai quái theo `ThreatView.row` | 16 × 16 |
| LL-29 | `src/view/screens.ts:122` và dòng kế; `src/app/main.ts:306` | `stage-<id>` trừ s0; súng theo kit | 384 × 216; súng 48 × 48 |
| LL-35 | `src/view/hud.ts:411` | Chân dung quái được dạy | 48 × 48 |
| LL-39 | `src/view/hud.ts:174` | Súng của bến; 1/3 bên trái, 2/4 bên phải | 40 × 40 |
| LL-53 | `src/app/main.ts:262`, `src/view/screens.ts:48` | Ảnh ải kế | 96 × 54 |
| LL-12 | `src/view/screens.ts:65` | `bg-menu` | Phủ overlay |
| LL-16 | `src/view/screens-journey.ts:58` | `bg-journey` | Phủ overlay |
| LL-23 | `src/view/screens-journey.ts:68` | `bg-briefing` | Phủ overlay |
| LL-24 | `src/view/screens-journey.ts:90` | `bg-loadout` | Phủ overlay |
| LL-49 | `src/view/screens.ts:130` | `bg-results-win/lose` | Phủ overlay |

Các nền chưa nhận đều trả chuỗi rỗng. Khi có nền, ảnh nằm dưới màn che dùng `--veil`, `--veil-edge` và dưới thẻ. Khi ảnh lỗi bị `hidden`, quy tắc `:not([hidden])` nhường lại bố cục cũ. Băng thẻ ải dùng lề âm theo padding hiện có để giữ đúng ô 760 px; cần Claude nhìn mép thẻ thực tế.

## Vai chờ và cách bật

| Phiếu | Các mục chờ | Cách Claude bật sau khi nhận |
|---|---|---|
| 157 | `gun-xung`, `gun-tia`, `gun-tan`, `gun-ray`, `gun-phao` (bản v2) | Với từng vai nhận, tắt mục 108 tương ứng rồi bật mục 157; ghi verdict |
| 157 | `foe-swarm`, `foe-scout`, `foe-brute`, `foe-pack-leader`, `foe-shield-guard`, `foe-splitter` (bản v2) | Tắt mục 089 tương ứng rồi bật mục 157; có thể nhận riêng từng vai |
| 126 | `stage-c1-s1`, `stage-c1-s2`, `stage-c1-s3`, `stage-c1-s4` (bản v2) | Tắt mục 109 tương ứng rồi bật mục 126 |
| 121 | `bg-menu`, `bg-journey`, `bg-briefing`, `bg-loadout`, `bg-results-win`, `bg-results-lose` | Bật từng mục 121 đã nhận; giữ crop `1536x864+0+80` |
| 150 | `foe-shard` | Chưa có nguồn: điền nguồn đã nhận rồi bật; không bật mục `source: null` |

Sau khi đổi cờ, chạy `pnpm ui-art:prepare --art-src ../typing-survival/art-src` và cùng lệnh thêm `--check`. Không sửa mã hay bảng chạy bằng tay. Mỗi vai tối đa một mục nhận. Sau khi gộp `ts-art` vào `main`, Claude dựng lại ở checkout chính với `--art-src art-src`, rồi `media:push` theo quy trình repo cha. Lượt này không ghi vào checkout chính.

## Kết quả kiểm

1. `pnpm check`: trước **22 file / 206 test**, sau **24 file / 225 test**, xanh; log `206/check-before.log`, `206/check-after.log`. Có hai lỗi trong lúc phát triển đã sửa: biến kích thước chưa được theme cho phép; chữ hoa `False` của ImageMagick trong assertion alpha. Không có test thời gian đỏ, nên không cần chạy riêng ba lần.
2. Ván vàng md5 trước/sau **`eeaf27679681c136c79badd7669ec83f`**. **152** hash chương trùng byte, diff rỗng (`chapter-hashes-before.txt`, `chapter-hashes-after.txt`). Không sửa `src/content`, `src/sim` hoặc ván vàng.
3. Bốn test bắt buộc English/theme/boundary/small-labels xanh, cùng các test mới. `node --check` cho script chuẩn bị và kịch bản mới trả 0. Các bài test chạy môi trường Node, không thêm thư viện DOM.
4. Dựng **49 WebP + manifest**, tổng WebP **2.769.208 B**. `prepare.log`, số theo từng cỡ và các file lossless/q92 ở `media-summary.json`. Lần hai **0 file ghi**, **0,639 s**, mã 0 (`prepare-repeat.log`, `.json`); kiểm cuối vẫn 0 file, **0,627 s** (`prepare-repeat-final.json`).
5. `pnpm ui-art:prepare --check --art-src ../typing-survival/art-src`: mã **0**, `check.log`. Thử không chỉ `--art-src` trong worktree không có media nguồn: mã **2**, thông báo chỉ rõ đường cần truyền. Test hỏng byte/nguồn/bảng/WebP lạ đều bắt được.
6. `--pending` xuất **61 WebP** của **21 vai có nguồn**, chỉ vào `tmp/ui-art/pending/`. Tổng **8.625.740 B** nếu nhận cả 157, 126, 121; đây là bộ thay thế, không cộng bản cũ cùng vai. `foe-shard` không dựng. Byte/khổ/PSNR từng file trong `pending.json`, log `pending.log`.
7. Byte ảnh từng màn ở DPR 1/2 nằm trong `bytes-per-screen.json`, bảng dưới. Không màn nào quá 1 MB ở DPR 2 với bộ đang nhận. Đây là tính theo URL duy nhất của ảnh thuộc màn, không phải số đo trình duyệt; không gồm HUD đang bị overlay che hoặc header HTTP/cache. Kịch bản sẽ ghi số Resource Timing thực tế cho Claude.
8. `pnpm deploy:pack`: trước và sau đều thoát **1**, **hai lỗi**, cùng mã `foreign-asset` và `local-host`; số lỗi không tăng. Gói vẫn tham chiếu thư viện model Space Typing và miền local, đã ghi trong README trước phiếu. Không sửa ngoài phạm vi để chữa hai lỗi này. JSON trước/sau và log có trong `206/`; `dist/` có **49 WebP UI và manifest**.
9. **84 file PNG nguồn** đã kiểm md5 trước/sau, tất cả trùng (`sources-md5.json`). Không sinh ảnh mới, không sửa nguồn. Chỉ đổi định dạng/thu nhỏ media và cắt nền theo phiếu.
10. Chuỗi `/assets/typing-survival/ui/` trong `src/` chỉ xuất hiện ở `src/view/ui-art.json`; `ui-art.ts` ghép URL từ trường `base`. Không tăng `<svg`, `url(` hay ký tự Extended Pictographic; các ký tự có sẵn giữ nguyên (`source-audit.json`). Không thêm màu hoặc sửa theme.
11. `git diff --numstat`: `main.ts` **+2/-2 = 4** dòng; `hud.ts` **+13/-1 = 14** dòng. Không sắp lại mã cũ.
12. `status.log` chỉ có các file được phép. WebP và manifest bị `.gitignore:11 public/assets/**` bỏ qua; `src/view/ui-art.json` không bị bỏ qua (`ignore.json`). Chỉ dùng Git đọc, không commit/push/reset/clean/stash.
13. `media-files.txt`: **50 dòng**, đủ đường/byte/md5 của 49 WebP và manifest, để Claude đẩy media sau duyệt.

| Cỡ ra | Tổng byte đang nhận |
|---|---:|
| 64 | 30.474 |
| 128 | 77.584 |
| 192 | 45.044 |
| 256 | 186.954 |
| 384 | 156.988 |
| 768 | 553.240 |
| 1536 | 1.718.924 |

PSNR nhỏ nhất: icon **35,126 dB**; portrait **35,2698 dB**; stage **26,7384 dB**. File lossless: `foe-shield-guard.{64,128,256}`, `gun-ray.64`, `gun-tan.{64,128}`. Cả **16 file stage** đã tăng q92 và vẫn dưới 35 dB; danh sách và số cụ thể được giữ trong manifest và JSON, theo luật của phiếu, chưa coi là đã duyệt bằng mắt.

| Màn | DPR 1 (B) | DPR 2 (B) |
|---|---:|---:|
| Chính | 0 | 0 |
| Kho súng | 30.436 | 62.170 |
| Hành trình | 45.044 | 156.988 |
| Thẻ ải 1 | 393.220 | 403.446 |
| Nạp súng ải 1 | 47.924 | 79.658 |
| Trước trận ải 1 | 133.940 | 408.154 |
| Trận ải 1, hai bến | 3.680 | 8.608 |
| Thắng ải 1, nút ải kế | 11.456 | 40.330 |

## Tờ xem và việc còn lại cho Claude

Tờ xem chỉ ở worktree, không vào Git hay thư mục media:

- `games/.wt-ts-art/tmp/206/sheet.jpg`: **867.111 B**, 7680×3264; đủ 15 vai nhận và 49 cỡ xuất, PNG/WebP cạnh nhau trên hai nền, ở cỡ gắn đại diện 720p/1080p. Chân dung dùng ô 40/48, súng 40/72 tùy cỡ xuất; ảnh ải dùng ô menu/intro/băng tương ứng. JPEG nén để dưới 1 MB; dùng PSNR trong JSON khi so chất lượng file gốc.
- `games/.wt-ts-art/tmp/206/pending-sheet.jpg`: **736.459 B**, 7680×3584; đủ 21 vai chờ có nguồn và 61 cỡ xuất. Icon/chân dung/ải ở cỡ đại diện; sáu nền toàn màn dùng bản xem thu nhỏ để tờ tổng quan không thành ảnh hàng trăm megapixel. Nền cần xem toàn màn sau khi bật, không chấm nhận qua tờ JPEG này.

Đã dùng `tools/capture-prune/prune.mjs` xem danh sách rồi áp dụng để xóa ảnh trung gian do lượt này tạo, giữ hai tờ; dọn `tmp/ui-art/` và `tmp/os-tmp/` sau kiểm. Không xóa file của làn khác.

Claude chạy `survival-ui-art` tại **1280×720** và **1920×1080**, xem tay thêm **thẻ ra mắt quái** và **kết quả**. Cần nhìn kỹ icon bến cạnh mũi súng và vạch đáy, không chồng `.sv-strip`; băng ảnh thẻ ải và mép thẻ; chiều cao năm thẻ nạp súng ở 720p; chân dung và chữ thẻ ra mắt; lớp màn che trên nền khi bật 121. Codex không mở trình duyệt, chưa xác nhận bố cục hay 0 lỗi console thực tế. Nếu còn chớp ảnh do `innerHTML`, để làn sau giữ nút ảnh theo rủi ro đã nêu trong phiếu.

Kịch bản cũ `survival-s1-loadout.mjs` còn `Hành trình`, `Trận thử`, `khắc: Rail Gun`, `ẢI 1`, `Trận thử: 24 viên`; giữ nguyên theo phạm vi, nên không dùng các assertion chữ cũ để kết luận lỗi của phiếu 206.

Không làm phần 191/TF2, 149–153, đổi ngôn ngữ, logo/tàu/khung, âm thanh, hoặc game khác; không chạy dev server, trình duyệt, mạng hay cài gói. Khi gộp 191/TF2 và 210, Claude giải tay `main.ts`, `hud.ts` và giữ cả phần ảnh trong `screens-journey.ts`, `journey.ts`, CSS. Chưa đủ điều kiện ký duyệt hình ảnh cuối cùng cho tới khi Claude hoàn thành lượt trình duyệt.
