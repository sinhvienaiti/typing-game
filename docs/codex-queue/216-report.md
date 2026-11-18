# Phiếu 216 · Repo cha · Bỏ alias dữ liệu dùng chung của ba host game

Hoàn tất phần mã và kiểm tĩnh ngày 30/10/2026 trên Mac mini M4/macOS, Node `v24.22.0`. Bỏ **16 location** trong hai cấu hình nginx; bộ kiểm chặn chúng quay lại; **94/94 test đạt**. Chưa cài cấu hình vào nginx máy nhà. Claude duyệt rồi commit; phiên này không chạy lệnh Git ghi.

## Mốc đầu và phạm vi

Đúng nhánh `feat/space-typing-admin-uiux`; `git status --short -uall -- infra/nginx scripts/validate-play-mode.mjs scripts/validate-play-mode.test.mjs` ban đầu rỗng. Repo cha có sửa của làn khác; lưu nguyên [status-before.txt](216/status-before.txt).

| Repo | Nhánh | HEAD lúc bắt đầu |
| --- | --- | --- |
| Repo cha | `feat/space-typing-admin-uiux` | `b646d8550b71ddb9f39bdd77ffbbf43941cafcb9` |
| `games/dragon-hold` | `main` | `1f1de484afd5092f5967454fab5f4e6edd3189c9` |
| `games/typing-defense` | `a2-days` | `f9abfd09987dadd519233c2f38692758d35cefca` |
| `games/typing-survival` | `main` | `79db62851e00eadeca7bfd44c10c0c682a9cec8d` |

Chi tiết: [revisions-before.json](216/revisions-before.json). HEAD repo cha cuối phiên vẫn giữ nguyên. Ba repo game chỉ được đọc; không đọc/ghi worktree game hay sửa Tu Tiên.

## Thay đổi và số đo

Trong cả play và dev, bỏ `/vocabulary/`, `/typing-texts/` khỏi Dragonhold; bỏ thêm `/shared/typing-texts/` và chú thích cũ khỏi Wordwoven, Last Line. Giữ `root`, `index`, `gzip`, route assets, `location /`, mọi chỉ thị proxy. Last Line còn đúng **1** location `/assets/space-typing/models/` mỗi file, chú thích đúng phiếu **205**.

| Chế độ | Dragonhold | Wordwoven | Last Line | Server trước → sau |
| --- | ---: | ---: | ---: | ---: |
| Play, số location | 5 → 3 | 6 → 3 | 7 → 4 | 11 → 11 |
| Dev, số location | 3 → 1 | 4 → 1 | 5 → 2 | 11 → 11 |

Trong sáu khối HTTPS được sửa: location dữ liệu bị cấm **16 → 0**; alias/root vào `__ROOT_DIR__/shared/` **16 → 0**. Kiểm ngoặc độc lập: độ sâu cuối **0**, nhỏ nhất **0** ở cả hai file trước và sau. Xem [conf-static.json](216/conf-static.json).

[aliases-before.json](216/aliases-before.json) liệt kê **36** location có alias/root vào shared hoặc Space Typing trong cả hai file, đủ file, dòng, host, route và đích; sau khi bỏ 16 còn 20. [blocks-unchanged.json](216/blocks-unchanged.json) có SHA-256 trước/sau của đủ **22 server**: **16/16 khối ngoài ba host** giống nguyên byte, gồm chuyển HTTP, portal, monkeytype, shooter, recall, karaoke, space và tutien. Mỗi file chỉ ba khối được giao đổi; diff không thay dòng trống hay thụt lề nơi khác.

`validate-play-mode.mjs` đưa phần đọc file/chạy kiểm vào `main()`, chỉ gọi khi chạy trực tiếp. Export `SELF_SERVED_HOSTS`, `SHARED_DATA_ROUTES`, hàm thuần `sharedDataAliases(config, host)` và `configStructureErrors(config)`. Bộ tách directive giữ số dòng, bỏ chú thích, xử lý chuỗi trong nháy và ký tự escape; kiểm thiếu ngoặc và ngoặc đóng sớm. Mỗi host trong bốn game phải có đúng một khối `server_name <host>;`.

Trong cả play và dev, mỗi location có tiền tố route bị cấm hoặc đích alias/root vào shared đều báo host, route và dòng. Đổi tên `/words/`, modifier, thiếu slash cuối, khoảng trắng/tab và đích trong nháy vẫn bị bắt. Kiểm cũ và thông báo lỗi cũ được giữ; chỉ vòng bắt buộc route dữ liệu thu hẹp còn tutien. Survival vẫn bắt buộc alias model, kèm chú thích bỏ cùng phiếu 205. Dòng PASS bổ sung việc ba game tự phục vụ bản ghim. Tham số lạ hoặc thiếu giá trị in Usage, exit **2**.

## Bản ghim tự phục vụ

Pin chung: `18338405eebd9cfdbd6d6bf666ea79361c00a564`, khớp cả ba manifest.

| Game | File nguồn trong manifest | Public kể cả manifest | Dist kể cả manifest | Lệch hash / thiếu / thừa |
| --- | ---: | ---: | ---: | ---: |
| Dragonhold | 102 | 103 | 103 | 0 |
| Wordwoven | 7 | 8 | 8 | 0 |
| Last Line | 5 | 6 | 6 | 0 |

Từng file nguồn khớp SHA-256 manifest; mọi file dist, kể cả manifest, khớp public. Không build lại. Quét mọi file `src/` trừ `src/kit/`, cùng mọi `.js` trong `dist/`: **0 chuỗi `typing-texts`** ở cả ba game, nên không cần giữ alias dữ liệu nào. Đối chiếu cấu hình Vite: không có override `publicDir`; hai game không dùng plugin shared; Last Line truyền `routes: {}`. Đã đọc bản plugin của Last Line: `Object.entries(options.routes ?? DEFAULT_SHARED_ROUTES)` giữ bảng rỗng, chỉ thêm mount model. Vì vậy Vite phục vụ `public/vocabulary/` của chính game. Chi tiết số file đã quét và kết quả: [vocab-self-serve.json](216/vocab-self-serve.json).

## Kiểm đã chạy

| Lệnh | Trước sửa mã | Sau sửa mã |
| --- | --- | --- |
| `node scripts/validate-play-mode.mjs` | exit 0, PASS | exit 0, PASS mới |
| `node scripts/validate-space-integration.mjs` | exit 0 | exit 0 |
| `node --test scripts/validate-play-mode.test.mjs` | 94 test, 94 đỏ, exit 1 | 94 test, 94 xanh, exit 0 |
| `git diff --check -- infra/nginx/typing-game.local.play.conf infra/nginx/typing-game.local.dev.conf scripts/validate-play-mode.mjs scripts/validate-play-mode.test.mjs` | — | exit 0, 0 lỗi |

Log: [validate-before.txt](216/validate-before.txt), [tests-before.txt](216/tests-before.txt), [tests-after.txt](216/tests-after.txt), [validate-after.txt](216/validate-after.txt).

Test dùng `node:test` và `node:assert/strict`, dựng fixture từ conf thật, không ghi cứng dòng. Có đủ **18** tổ hợp 3 host × 3 route × 2 chế độ; biến thể modifier `=`, `^~`, `~`, `~*`; comment, chuỗi có ngoặc/escape, model được phép, các host khác được giữ, thiếu/thừa ngoặc, thiếu/trùng host. Test CLI kiểm mặc định PASS, hai tham số fixture bắt đúng host/route, usage exit 2, lỗi cấu trúc exit 1. Test import đổi cwd sang `/` để chứng minh module không đọc file hay tự chạy CLI. Không phụ thuộc checkout hoặc bản build game; chỉ đọc hợp đồng repo cha. Fixture CLI chỉ ghi dưới `tmp/validate-play-mode-test/`, xóa trong `after`; thư mục đã biến mất.

Bản nháp changelog: [changelog.md](216/changelog.md). Chưa sửa changelog chính thức theo luật một file mỗi ngày.

## Áp dụng sau khi Claude commit và rủi ro

Chủ dự án chạy một lần ở gốc repo bằng tài khoản thường:

```sh
pnpm setup:play
```

Đây là `bash scripts/setup-nginx.sh play` theo `package.json`. Ai đang chạy dev dùng `pnpm setup:dev` (`bash scripts/setup-nginx.sh dev`). `./play.sh` cũng tự gọi lệnh setup ở dòng **352**. Script thay `__ROOT_DIR__`, `__SSL_CERT__`, `__SSL_KEY__`, cài conf rồi tự gọi sudo để kiểm nginx và reload/khởi động; có thể hỏi mật khẩu khi cần.

`docs/games/MAP1_PRODUCTION.md` DH-03 hiện ghi `sudo bash scripts/setup-nginx.sh play` (cũng lặp ở kế hoạch cuối tài liệu). **Claude cần sửa hướng dẫn này ở lượt tài liệu khác**: chạy cả script dưới sudo sai trên macOS vì `brew --prefix` chạy bằng root. Phiếu này không sửa tài liệu đó.

- Play trên máy nhà vẫn giữ alias cũ cho tới khi chủ dự án chạy lại setup. Chưa kiểm HTTP sau khi áp dụng.
- Sau đó `/vocabulary/` đi qua `location /` của Play với `try_files $uri $uri/ /index.html`. Nếu thiếu file, nginx có thể trả `index.html` mã **200**, không phải 404. Để lượt G7 (§4.6, yêu cầu không fallback SPA) xử lý; phiếu này không đổi fallback.
- Khi phiếu **205** đã gộp, Claude bỏ alias model của survival ở hai conf cùng yêu cầu tương ứng trong validator. Tu Tiên giữ nguyên.

Không chạy setup-nginx, play, sudo, nginx (kể cả `nginx -t`), brew services, server, trình duyệt, mạng, game build/test, kit sync. Không sửa repo game, shared, các công cụ khác, tài liệu game hoặc HANDOFF/CODEX_QUEUE. Không có ảnh/âm cần tạo. Mọi file tạm riêng của phiếu trong `tmp/ticket-216/` được dọn khi kết thúc.

## Các đường đã đổi

Mỗi dòng dưới là một file của phiếu, tính từ gốc repo cha; không gồm các file có sẵn của làn khác hay file tạm đã xóa.

- `infra/nginx/typing-game.local.play.conf`
- `infra/nginx/typing-game.local.dev.conf`
- `scripts/validate-play-mode.mjs`
- `scripts/validate-play-mode.test.mjs`
- `docs/codex-queue/216-report.md`
- `docs/codex-queue/216/aliases-before.json`
- `docs/codex-queue/216/blocks-unchanged.json`
- `docs/codex-queue/216/changelog.md`
- `docs/codex-queue/216/conf-static.json`
- `docs/codex-queue/216/revisions-before.json`
- `docs/codex-queue/216/scope.json`
- `docs/codex-queue/216/status-after.txt`
- `docs/codex-queue/216/status-before.txt`
- `docs/codex-queue/216/tests-after.txt`
- `docs/codex-queue/216/tests-before.txt`
- `docs/codex-queue/216/validate-after.txt`
- `docs/codex-queue/216/validate-before.txt`
- `docs/codex-queue/216/vocab-self-serve.json`

## Trạng thái cuối và công việc đồng thời

[status-after.txt](216/status-after.txt) có **1005 dòng**, so với **975 dòng** ban đầu. [scope.json](216/scope.json) liệt kê đúng các đường của phiếu, xác nhận HEAD/nhánh giữ nguyên và hai thư mục tạm riêng đã xóa. Ngoài file của phiếu, có **13 dòng trạng thái phát sinh** từ các phiếu 195, 199, 202 và `docs/games/dragon-lane/06-other-systems.md` trong phiên; đây là kết quả làm đồng thời của làn khác, không do phiếu này ghi. Không có dòng trạng thái cũ nào biến mất. Vì vậy chênh status toàn repo còn chứa các đường đồng thời này; không xóa hoặc sửa chúng để ép status chỉ còn phiếu 216.
