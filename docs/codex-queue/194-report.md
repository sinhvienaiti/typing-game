# Phiếu 194 · Dragonhold · Đường ảnh icon UI

**Đã hoàn tất phần gắn ảnh trong phạm vi 194; chưa đạt điều kiện kiểm chung vì phần dở 195.** Có bảng 53 icon, 159 WebP và manifest; gắn 30/36 icon đã nhận, sáu icon chỉ chuẩn bị theo phiếu; bỏ rêu CSS. Kiểm riêng **48/48 xanh**, golden giữ nguyên. `pnpm check` trước/sau đều đỏ tại 195; `deploy:pack` dừng ở TypeScript của 195. Không dùng số xanh lịch sử để nhận lượt này đã đạt toàn bộ mười mục kiểm.

## 1. Tiếp tục phần dở và giữ phạm vi

Có báo cáo 187. Làm tại `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD giữ nguyên `6aa593a2dce6637cccbe24a58709b86f7127f607`. Trạng thái đầu gồm đúng các file của 187, 194 và 195 được điều phối cho phép; không có file lạ. Không sửa hoặc hoàn tác 195.

Giữ mốc đầu tiên [start-status.txt](194/start-status.txt), [start.diff](194/start.diff). Lượt chạy lại lần 3 lưu [trạng thái](194/resume3-start-status.txt), [diff](194/resume3-start.diff), [hash trước](194/resume3-before.json). [Hash sau](194/resume3-preserved.json) xác nhận toàn bộ 16 file được theo dõi của 187/195 và golden giữ nguyên byte. Không có file mới ngoài tập cho phép trong worktree.

Các phần dùng chung được tách rõ:

- **`src/app/app.ts`: không có đoạn nào của 194.** Import `createPortalBridge` dòng 25 và lời gọi dòng 223 thuộc 187. Import boot/quality/idle dòng 26–28, import `icon`, ảnh `fast-forward` dòng 245–248, xử lý tăng tốc, boot lại bộ từ và state tương ứng thuộc 195.
- **`src/app/learning.ts`: không có đoạn nào của 194.** Import `createPortalBridge` dòng 18 và lời gọi dòng 257 thuộc 187. `DeckBuildError` dòng 123–131, xử lý lỗi tải/rỗng/thiếu bộ từ dòng 329–370 thuộc 195. Cả hai file giữ nguyên byte so với đầu lượt này.
- **`src/ui/results.ts`:** 194 đổi sao dòng 239 và 320–323, ô số dòng 299–303 và 327–331, ảnh trạng thái dòng 340–343, ảnh/nhãn nghe dòng 355–357, Retry/Replay dòng 365. Khối cổng có điều kiện dòng 255–268 và gợi ý phím dòng 371 thuộc 187, được giữ nguyên.
- **`README.md`:** chỉ mục “Ảnh icon UI” dòng 42–44 thuộc 194; phần hướng dẫn cổng trước đó thuộc 187.
- **`tests/ui/results-screen.test.ts`:** 194 thêm `ariaLabel` vào stub, kiểu sự kiện của helper `assigned`, hai test `results UI art (194)`; các test portal thuộc 187 giữ nguyên.

[Diff riêng 194](194/task.diff) được dựng từ HEAD cộng `194/start.diff` trong bộ nhớ, loại phần 187 và 195; [16 đường dẫn 194](194/files-194.txt). Không chạy lệnh Git ghi, kit sync, server, trình duyệt, mạng hoặc media:push. Chỉ chạy các lệnh kiểm Dragonhold được phiếu liệt kê trong worktree; không chạy game khác, không chạm Tu Tiên.

## 2. Mã và media đã làm

| Nhóm | Đường dẫn trong worktree | Kết quả |
| --- | --- | --- |
| Bảng chọn | `src/ui/ui-art.json` | Version 1; đúng 36 mục nhận 137–140, 17 mục tạm; tên/key duy nhất, alt tiếng Anh, không bản thử. Roar dùng `icons/normalized/015-skill-roar`. |
| Chuẩn bị ảnh | `scripts/ui-art/prepare.mjs`, `package.json` | Lệnh `prepare-ui-art`, `--out`, `--check`, `--help`. Dùng PNG đúng cỡ, thiếu thì thu Lanczos từ cỡ lớn hơn gần nhất; không phóng to. Strip metadata, quality 90/alpha 100; dưới 35 dB chuyển lossless. Chuyển hết trước khi xuất, manifest đổi sau cùng qua rename; lỗi xuất hoàn lại file đã thay. Scratch trong `tmp/ui-art/`. |
| Runtime | `src/ui/skin.ts`, `src/ui/styles/dh.css` | Tên và alias trả `img.dh-art`, URL có version; chọn 64/128/256, width/height, alt trang trí hoặc có nhãn. Listener capture trên document, warn một lần/URL, ẩn ảnh lỗi, không hình thay thế. |
| Gắn | `hud.ts`, `wave-card.ts`, `debut-card.ts`, `placement-ui.ts`, `learning-frame.ts`, `results.ts` trong `src/ui` | Các mục A/B được gắn; family thay bóng quái, toast rejected mới có deny, pause/camera/listen có nhãn tiếng Anh bằng title. `shop-strip.ts` tự dùng ảnh qua alias nên không cần sửa. |
| Test | `tests/ui/ui-art.test.ts`, `tests/assets/ui-art.test.ts`, phần 194 trong `tests/ui/results-screen.test.ts` | Đủ bảy nhóm kiểm: bảng/chỗ gọi/cỡ/script/ảnh lỗi/không emoji/markup học và kết quả. Fixture nằm trong `tmp/ui-art-test/`, tự dọn. |
| Hướng dẫn | `README.md`, `docs/changelog/2026-10-30-ui-art-icons.md` | Cách chuẩn bị/kiểm ảnh, số đo và giới hạn của lượt hiện tại. |

Phần dở của lượt trước đã được giữ và rà lại. Lượt này phát hiện NEW dùng ô 18; thêm kiểm hồi quy, chạy đỏ **1/11**, rồi sửa về mặc định 20. [Log đỏ](194/resume3-size-red.log). Bằng chứng test trước mã của lượt đầu vẫn ở [test-red.log](194/test-red.log).

Cỡ ô: mặc định/NEW 20; Retry/trạng thái/năm ô số 25; sao 46; loa/dấu đúng khung học 18; loa Thẻ Ôn 22. Ô ra mắt giữ cỡ sẵn có 28 và lấy ảnh 128. Nút nghe Wordbook có ô 28, padding 4, ảnh 20. `object-fit: contain`; sao tối dùng nguyên ảnh, không dựng ổ sao (chờ 196), không thêm filter/blend/opacity để đổi màu ảnh.

Các trạng thái mờ vốn có được giữ: `.dh-btn:disabled/.is-off` saturate 0,55; potion rỗng opacity 0,22/grayscale; kỹ năng đã dùng opacity 0,55; lane tối 0,45; ô mang theo tắt/thiếu tiền, marker và menu thiếu tiền; khung học idle 0,55. Hoạt ảnh xuất hiện sao giữ nguyên.

Bỏ đúng `.dh-panel::before` và `::after` cùng hai chú thích. Giữ biến `--dh-moss`, `--dh-moss-hi` cho `app.css`. Chỉ còn `src/app/app.css:115` đặt `bottom` cho `.dh-panel.dh-pacecard::after`; quy tắc này không khai báo `content`, không tạo phần tử sau khi rêu bị bỏ, không có chức năng khác phụ thuộc. Không sửa file đó. Bảng gỗ CSS chờ 162.

## 3. Mười mục kiểm hiện tại

| Mục | Kết quả lượt chạy lại | Bằng chứng |
| --- | --- | --- |
| 1. `pnpm check` trước/sau | Cả hai mã **1**; 64 file: **62 xanh, 2 đỏ**; **549/551 test xanh**, hai test đỏ và một suite không thu thập. Cùng ba lỗi ở 195 trước/sau, kit 75 file đạt. Chưa tới bước build. Không lỗi thời gian nên không áp dụng chạy riêng ba lần. | [Trước](194/resume3-check-before.log), [sau](194/resume3-check-after.log) |
| Test tập trung | Trước sửa: **29/29 xanh**. Sau sửa NEW: **48/48 xanh** ở năm file, gồm 29 test UI/script/kết quả + 10 golden + 9 English. | [Trước](194/resume3-focused-before.log), [sau](194/resume3-focused-after.log) |
| 2. Ván vàng | **10/10 xanh**; MD5 trước/sau `75f74947dac170d05fd659f99417940e`. | [Log](194/resume3-focused-after.log), [hash](194/resume3-preserved.json) |
| 3. English UI | **9/9 xanh**; AST chuỗi/template và CSS content trong UI không còn pictograph, FE0F hoặc dấu đúng bằng ký tự. | [Log tập trung](194/resume3-focused-after.log) |
| 4. Chuẩn bị thật | Mã **0**, 53 icon, **159 WebP + manifest**, từ **142 PNG**; tổng **1.262.593 byte**, manifest **62.549 byte**. | [prepare.log](194/prepare.log), [số đo](194/verification.json) |
| 5. Check ảnh thật | Mã **0**, `53 icons; check OK`; chỉ đọc. | [check.log](194/check.log) |
| 6. `pnpm deploy:pack` | Mã **2**, dừng tại ba lỗi TypeScript của 195. **Chưa dựng lại dist, chưa chạy checker trên mã hiện tại.** Dist cũ có 159 ảnh UI; đây chỉ là kiểm đếm file còn từ lượt trước, không phải bằng chứng gói hiện tại đạt. | [Log](194/deploy-pack.log), [JSON trạng thái thất bại](194/deploy-pack.json) |
| 7. Tờ xem | Giữ `tmp/ui-art/194-sheet.jpg`, **337.218 byte**; đã mở xem lại đủ 53 PNG/WebP cạnh nhau ở 64 px trên `#2b2118` và `#f1e3c4`, có tên. Media xuất lại khớp byte/hash inventory cũ nên tái dùng tờ này. Không tạo raw frame mới, không chép vào docs/public. | [Đối chiếu inventory](194/resume3-preserved.json) |
| 8. Bảng gắn/SVG | **30 nhận đã gắn, 6 chỉ chuẩn bị trong 194**. `skin.ts` còn ba SVG; 11 icon SVG trong `tags.ts` giữ nguyên do cấm sửa. | [36 dòng gắn](194/integration.md), [JSON](194/integration.json), [SVG còn lại](194/remaining-svg.md) |
| 9. Git/ignore | Chỉ tập 187/194/195 được phép, HEAD không đổi, `git diff --check` mã 0. WebP/manifest bị bỏ qua bởi `.git/info/exclude:7:public/assets` ở checkout chính; `src/ui/ui-art.json` không bị bỏ qua (mã 1). | [Status](194/status-final.txt), [ignore](194/check-ignore.txt), [hash bảo toàn](194/resume3-preserved.json) |
| 10. Danh sách media | **160 dòng**: đường, byte, MD5 mọi file đầu ra; ghi lại từ media vừa xuất. | [media-files.txt](194/media-files.txt) |

| Cỡ | WebP | Tổng byte | PSNR nhỏ nhất | Lossless |
| --- | --- | --- | --- | --- |
| 64 | 53 | 142.184 | 35,1794 dB | 13 |
| 128 | 53 | 350.914 | 35,0822 dB | 6 |
| 256 | 53 | 706.946 | 35,2564 dB | 0 |

Lossless 64: `dragon-rage`, `camera-reset`, `deny`, `lock`, `upgrade`, `seal-lit`, `edge-arrow`, `stat-accuracy`, `stat-new-words`, `retry`, `status-learned`, `status-new`, `gold`. Lossless 128: `dragon-rage`, `seal-lit`, `status-learned`, `gold`, `skill-ultimate`, `herb-hut`. Không file 256 cần lossless. Tên đủ đuôi trong log và JSON.

Số **526/526 test, deploy 0 lỗi** trong [báo cáo lượt trước](194/previous-report.md) là lịch sử trước 195. Giữ các log cũ để truy vết; [verification.json](194/verification.json) và báo cáo này phản ánh trạng thái hiện tại.

## 4. Phần chưa đạt và việc cần Claude/chủ dự án xem

Các lỗi có sẵn của 195, được tái hiện nguyên trạng trước/sau:

1. `tests/app/idle-estimate.test.ts:5`: thiếu `scripts/balance/idle-estimate.mjs`; Vitest không thu thập suite, TypeScript báo TS2307.
2. `tests/app/idle-speed.test.ts:43`: truyền `StatusSet` thay vì `EntityRef` vào `applyStatus`, runtime báo `set.list is not iterable`; TypeScript báo TS2345 ở dòng 43 và 44.
3. `tests/app/idle-speed.test.ts:58`: điều kiện ring/stopAt mong true nhưng nhận false.

Không sửa các lỗi này vì nằm ngoài 194 và điều phối yêu cầu giữ nguyên 195. Cần làn 195 hoàn tất rồi chạy lại `pnpm check`, `pnpm deploy:pack` và lấy JSON checker mới. Phiếu 194 **chưa được đánh dấu đạt toàn bộ điều kiện xong** khi hai cổng đó còn đỏ.

Trong 194, `fast-forward`, `keyboard` chỉ chuẩn bị vì `src/app` ngoài phạm vi; `seal-lit`, `seal-unlit`, `edge-arrow` vì `tags.ts` bị cấm sửa; `lock` chưa có giao diện khóa. Ảnh fast-forward đang gọi tại `app.ts:246` là phần 195, không tính vào phần gắn của 194. Không dùng icon easier hoặc ảnh chưa nhận. Không sinh ảnh, không sửa PNG nguồn; 17 icon cũ là ảnh tạm, chờ 163/164, khi nhận chỉ đổi nguồn/cờ trong bảng.

Claude duyệt [diff riêng](194/task.diff), đặc biệt `hud.ts` và `dh.css`; gộp theo map-pilot → dh-vfx → dh-codex, xử lý xung đột 192. Chưa kiểm bố cục hay nhận cảm quan trên trình duyệt theo lệnh cấm; cần xem 1280/1920 sau khi kiểm chung xanh, nhất là Wave/Chain, huy hiệu NEW, Wordbook 25 px và sao tối chờ ổ vẽ thật 196. Sau gộp main, chạy lại prepare ở checkout chính rồi media:push theo inventory. Không commit hoặc push trong phiên này.
