# Phiếu 170 · Wordwoven · Kit tiếng Anh, kiểm gói và tên file chơi thử

Hoàn tất phần mã được giao. `pnpm check` xanh **380/380 test**, kit **33/33 file**. Chạy thật `pnpm deploy:pack`: build qua, bộ kiểm trả mã **1** với **69 lỗi thật của gói**; kiểm local còn **68 lỗi**. Gói chưa đạt G7.

**Lượt nhận lại phiếu:** phần mã và bằng chứng bên dưới đã có sẵn khi bắt đầu lượt này. Đã đối chiếu lại hash, trạng thái worktree và chạy lại riêng bộ kiểm gói; kết quả khớp hoàn toàn. Không sửa thêm mã, không chạy lại build hay bộ test. Chi tiết ở mục 6.

## 1. Phạm vi

- Worktree: `games/.wt-td-codex`, nhánh `td-codex`, HEAD giữ nguyên `f9abfd09987dadd519233c2f38692758d35cefca`.
- Môi trường: Mac arm64, macOS 15.5, Node **24.22.0**, pnpm **11.21.0**; Vitest thực chạy **3.2.7**, Vite **7.3.7**.
- Lượt kit có sẵn: 7 file sửa, 2 file mới; manifest ghi kit cha `1b1fe6cfacdc81a55d13af202da0f42023455313`, `parentDirty: true`. **34/34 file trong `src/kit/**` giữ nguyên byte**, khớp cả bản `before.json` được bàn giao và ảnh chụp đầu phiên; 33 file được manifest kiểm, cộng chính manifest.
- Ngoài kit có đúng **10 đường dẫn** sửa/tạo, liệt kê dưới đây. [Trạng thái cuối](170/status-final.txt), [kiểm phạm vi và SHA-256](170/verification.json).

## 2. Những gì đã làm

Các đường dẫn trong bảng tính từ worktree.

| Đường dẫn | Thay đổi |
| --- | --- |
| `tests/td-flow.test.ts` | Đổi kỳ vọng chính xác thành `Balanced`, `Standard`, `Shared flow band`, `Matches human play`, `MISSING DATA`; thêm kiểm `Learning stays clear · PASS`. Giữ kiểm số, cấu trúc bảng và trạng thái `skip`. |
| `package.json` | Thêm `deploy:pack` = `pnpm build && node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense`; `deploy:pack:local` thêm `--allow-local-host`. |
| `README.md` | Một đoạn hướng dẫn tiếng Việt: dựng và kiểm `dist`, chế độ production/local, giới hạn của lệnh. |
| `src/app/retry.ts` | Tải `wordwoven-playtest-s<seed>-n<ngày>-<tick>.json`; nội dung JSON và thao tác chép bộ nhớ tạm giữ nguyên. |
| `scripts/td/b9.ts` | Đổi ví dụ và hướng dẫn tham số sang tên mới, ghi rõ nhận cả tên cũ. Bộ đọc đã nhận đường dẫn bất kỳ, không có bộ lọc tiền tố cần sửa; giữ logic này. |
| `tests/td-b9.test.ts` | Thêm 2 test: gọi thật `copyNumbers` với DOM giả để kiểm tên, Blob, click, thu hồi URL và nội dung clipboard; chạy CLI B9 thật với hai file cùng nội dung mang tên cũ/mới, kiểm cả hai chạy lại đúng hash và bảng kết quả. |
| `tests/deploy-pack.test.ts` | Thêm 8 test chạy lệnh package với build giả nhỏ và bộ kiểm kit thật: build trước kiểm, dừng khi build lỗi, chặn Space ở cả hai chế độ, chỉ bản local miễn nguồn local. Fixture trong `tmp/` được xóa sau từng test. |
| `docs/td/PLAYTEST_1B.md`, `docs/td/BUILD_1B.md` | Chỉ sửa 3 dòng có tên file: tên tải xuống, ví dụ lệnh và khả năng đọc file cũ. |
| `docs/changelog/2026-10-29-pack-and-kit.md` | Ghi thay đổi, kiểm tra và các lỗi gói còn lại. |

Quét `src/`, `scripts/`, `tests/` cho thấy không có script khác lọc `loi-goi-choi-thu-*`. Bộ đọc `tests/td/b9.ts` nhận trực tiếp đường dẫn; scenario `td-1b-tour.mjs` lấy tên tải thực tế, không ràng buộc tiền tố. `scripts/td/replay.ts` nhận đường dẫn của nhật ký ván riêng, không đọc lớp bọc file chơi thử B9. Không cần đổi các bộ đọc đó.

## 3. Test trước, mã sau và kiểm cuối

| Lượt | Số đo / kết quả | Bằng chứng |
| --- | --- | --- |
| Test luồng trước sửa | **1 đỏ, 6 xanh**; đỏ ở `Cân bằng` thay vì `Balanced` | [Kết quả](170/baseline-flow.json), [log](170/baseline-flow.log) |
| Test mới trước sửa mã | **9 đỏ, 4 xanh**; 8 lỗi thiếu lệnh deploy, 1 lỗi tên tải cũ. CLI nhận cả hai tên đã xanh | [Kết quả](170/tests-before.json), [log](170/tests-before.log) |
| `pnpm check` lần đầu | **378 xanh, 2 đỏ**: còn kỳ vọng `Chuẩn` thay vì `Standard`; test CLI mới mất **7,858 s**, vượt timeout mặc định 5 s | [Kết quả](170/check-first.json), [log](170/check-first.log) |
| Chạy riêng test CLI 3 lần, trước đổi timeout | **3/3 xanh**; riêng test **1,834 / 1,913 / 2,015 s**; cả lệnh **4,075 / 3,362 / 3,593 s** | [Số đo](170/cli-timing.json), [lần 1](170/cli-timing-1.log), [lần 2](170/cli-timing-2.log), [lần 3](170/cli-timing-3.log) |
| `pnpm check` cuối | Mã **0**, **24,422 s**; **37 file, 380/380 test xanh**, kit **33/33**, TypeScript và build qua | [Kết quả](170/check.json), [log](170/check.log) |
| Golden trong lượt check cuối | **6/6 test** của hai ván vàng qua; SHA-256 hai file golden không đổi | [Log](170/check.log), [hash](170/verification.json) |
| Hiệu năng sim trong lượt cuối | Trung vị **0,064 / 0,057 / 0,232 ms**, tương ứng tải 300 quái / tải đầy / đỉnh boss; ngưỡng mỗi test **≤ 2 ms**, giữ nguyên | [Log](170/check.log) |
| Ngân sách trang bắt đầu | `/`: **79,60 kB gzip**; `/?title=0`: **81,07 kB**; đều **≤ 85 kB** | [Log](170/check.log) |
| `git diff --check`, phạm vi và bảo toàn kit/golden | Mã **0**, không đường dẫn ngoài phạm vi; `src/sim`, `src/content`, `src/typing` sạch so với HEAD | [Kiểm cuối](170/verification.json) |

Sửa kỳ vọng `Standard` và đặt timeout **20 giây cho test CLI tích hợp mới** để chứa tiến trình Node và các lượt bot khi chạy chung; bản cuối test đó mất **9,627 s**. Không thay timeout toàn bộ bộ test, ngưỡng hiệu năng gameplay hay bất kỳ khẳng định nội dung nào. Các test hiệu năng gameplay không đỏ nên không chạy lặp thêm. Sau khi check xanh chỉ thêm tài liệu và bằng chứng.

## 4. Gói thật và phân loại từng phát hiện

`pnpm deploy:pack` chạy thật mất **4,130 s**, mã **1**: build xanh, bộ kiểm báo **69 lỗi**. Lệnh package xuất chẩn đoán chữ; sau đó gọi bộ kiểm `--json` trên **chính `dist` đó**, không build lại, để lưu JSON thuần.

- [Lệnh và mã thoát](170/deploy-pack-run.json), [log đầy đủ](170/deploy-pack.log).
- [JSON production](170/check-pack.json), [lệnh production](170/check-pack-run.json).
- [JSON local](170/check-pack-local.json), [lệnh local](170/check-pack-local-run.json): mã **1**, **68 lỗi**. Chưa chạy toàn bộ `pnpm deploy:pack:local`; lệnh này được kiểm bằng fixture, rồi kiểm trực tiếp gói thật với cùng cờ local.
- [Phân loại đủ 69 phát hiện](170/deploy-findings.json): mỗi lỗi có số thứ tự, nguyên văn chẩn đoán, kết luận và căn cứ; mỗi URL GLB có id, tier, URL, kiểm tồn tại trong `public` và `dist`.

| Phát hiện | Thật hay báo nhầm | Căn cứ và việc còn lại |
| --- | --- | --- |
| `local-host` · **1 lỗi** trong `assets/learn-BQ0vH7oH.js` | **Lỗi thật ở production** | `src/app/learning.ts:15` tạo bridge không truyền `parentOrigin`; kit dùng `PARENT_ORIGIN = https://typing-game.local` tại `contract.ts:22`, mặc định ở `bridge.ts:115`, kiểm nguồn nhận ở dòng 248, gửi `postMessage` ở dòng 292. Đây là nguồn portal được dùng thật. Bản local miễn lỗi này đúng quy định. Chưa đổi cấu hình bridge trong phiếu. |
| `missing-model` · **68 lỗi**, **34 model × 2 tier** | **Lỗi thật của gói**, không có báo nhầm về tồn tại file | Vite chép `public/assets/typing-defense/models/manifest.json` vào `dist`; toàn bộ 68 URL High/Medium trong đó không có GLB ở cả `public` lẫn `dist`. Quét `src/**/*.ts` trừ kit không thấy `ModelLibrary`, `GLTFLoader`, `/models/`, `.glb` hoặc `manifest.json`. Đây là manifest thừa có đích thiếu, **chưa phải bằng chứng game hiện tại cần 68 model khi chơi**. Theo `DEPLOY_INDEPENDENCE.md` §11, làn đóng gói sau cần loại `assets/typing-defense/models/**` khỏi gói Wordwoven; không tải hàng loạt model để làm xanh. |
| `vocabularyNotShipped: 95` | **Thông tin đúng**, không phải lỗi | Index chung có 100 level; `VOCAB_LEVELS = 5`, gói ghim level 001–005. Có 7 file ghim cùng `vocab-manifest.json`; 5 test từ vựng kiểm hash, pin, phiên bản và đủ level đều xanh. |
| `external: []` | **0 phát hiện** | Bộ kiểm không thấy host bên ngoài khác; đây là quét tĩnh, không phải bằng chứng mạng từ trình duyệt. |

Gói có **55 file, 1.205.337 byte (~1,149 MiB)**. [Inventory](170/dist-inventory.json) ghi đường dẫn, byte và SHA-256 của từng file. `title-dusk.webp` có sẵn được build chép sang `dist`; phiếu không tạo hay đưa media vào Git. Không có lỗi `foreign-asset`, đường cha, media riêng tư, cỡ file, số file, attribution hay hash từ vựng từ bộ kiểm. Không có lỗi nào trong 69 phát hiện được phân loại là báo nhầm.

## 5. Việc giữ lại và chủ dự án cần xem

1. **Gói production còn đỏ:** cần nguồn portal production và bước lọc manifest model thừa theo §11. Phiếu chỉ thêm đúng các lệnh như 168 và ghi lỗi thật; không sửa kit, media, manifest model hay kiến trúc deploy để né kiểm.
2. **G7 chưa được chứng nhận:** phiếu cấm server, trình duyệt và mạng, nên chưa kiểm HTTP, kiểu nội dung, request và chơi độc lập trên server tĩnh. Không mở dev server, không chạy trình duyệt hay tải media.
3. Các changelog cũ và `BUILD_NOTES.md` giữ nguyên tên file lịch sử của những lần chụp/chơi thử đã xảy ra; không viết lại bằng chứng cũ. Hướng dẫn chơi thử hiện hành đã đổi đúng các dòng tên file. `AGENTS.md` không sửa theo phạm vi phiếu.
4. Không chạy `kit:sync`, không sửa `shared/game-kit`, không chạm game/worktree khác hoặc Tu Tiên, không chạy lệnh Git ghi. `before.json` được bàn giao giữ nguyên. Không có ảnh hay âm thanh mới; không cần sinh hoặc dọn capture.

Báo cáo này và toàn bộ JSON/log của phiên nằm ở `docs/codex-queue/170-report.md` và `docs/codex-queue/170/` của repo cha. Thay đổi có sẵn của các tác nhân khác được giữ nguyên.

## 6. Kiểm tra khi nhận lại phiếu

- HEAD, toàn bộ trạng thái worktree, hash 6 file mã/test đã ghi, **34 file kit** và **2 file golden** khớp bằng chứng trước. `src/sim`, `src/content`, `src/typing` sạch; `git diff --check` mã **0**.
- **55/55 file trong `dist`**, tổng **1.205.337 byte**, khớp cả SHA-256 và byte của inventory đã lưu. Log `pnpm check` có sẵn ghi **37 file, 380/380 test qua**, kit **33/33**; đây là kết quả của lượt triển khai trước, không phải lượt chạy test mới.
- Chạy mới `node src/kit/tools/deploy/check-pack.mjs dist --game typing-defense --json`: mã **1**, JSON khớp bản trước; **1 lỗi local-host + 68 lỗi missing-model**. Đối chiếu đủ **69/69** dòng phân loại với chẩn đoán; xác nhận lại **68/68** URL model thiếu ở cả `public` và `dist`.
- Chỉ bổ sung ghi chú này và hai JSON trong thư mục báo cáo: [kiểm tra nhận lại](170/handoff-verification.json), [kết quả bộ kiểm mới](170/handoff-check-pack.json). Giữ nguyên mã và toàn bộ log cũ; không lặp build hay bộ test theo giới hạn của lượt giao việc.
