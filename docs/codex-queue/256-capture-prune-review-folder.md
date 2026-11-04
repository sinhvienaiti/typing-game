# Phiếu 256 · Repo cha · Code: cho `tools/capture-prune` dọn được thư mục review, và giữ đúng ảnh tài liệu đang trỏ tới

**Loại việc:** code (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã đủ ở mục "Việc". Không thiết kế lại công cụ.

**Báo cáo:** `docs/codex-queue/256-report.md` (tiếng Việt).

## Bối cảnh
- Ngày 04/11/2026 chủ dự án yêu cầu gom mọi ảnh chụp test và video review vào **một thư mục cạnh source**: `/Volumes/SS990TPRO/htdocs/typing-game-review/`.
  - Ảnh chụp làm việc nằm ở `captures/<khu>/<việc>/`; thứ đã gửi chủ dự án nằm ở `owner-review/<ngày>/<khu>/<việc>/`.
  - Cấu hình nằm trong `typing-game-review/review.config.json`. Mục `areas` ánh xạ `<khu>` sang `[<thư mục game trong repo>, <tiền tố cũ mà tài liệu dùng>]`, ví dụ `"tu-tien": ["games/immortality-cultivation", "tmp/shots/"]` và `"dragonhold": ["games/dragon-hold", "tmp/"]`.
  - Các đường dẫn cũ trong repo giờ là symlink tới đó: `games/immortality-cultivation/tmp/shots`, `games/dragon-hold/tmp`, `games/typing-survival/tmp`, `games/typing-defense/tmp`.
- `tools/capture-prune/prune.mjs` hiện có hai vấn đề:
  1. **Từ chối mọi đích trong thư mục review.** `targetRefusal` đòi đường dẫn thật có `/tmp/` (lý do `not-tmp`) và nằm trong repo hoặc `../typing-game-wt` (lý do `outside-roots`).
  2. **Không giữ được ảnh tài liệu đang trỏ tới,** nếu sau này có cho phép thư mục review. Hàm `referenced` so `path.relative(repoRoot, real)` với các tham chiếu bắt đầu bằng `tmp/`. Đường dẫn thật trong thư mục review lại là `../typing-game-review/captures/tu-tien/...`, không có `tmp/`, nên ảnh tài liệu trỏ tới bằng `games/immortality-cultivation/tmp/shots/x.png` sẽ bị coi là ảnh thô và **bị xoá**. Đây là lỗi phải chặn.

## Làm ở đâu
Thư mục gốc repo cha (`.`).

### Được ghi
- `tools/capture-prune/prune.mjs`
- `tools/capture-prune/test/prune.test.mjs`
- `tools/capture-prune/README.md`
- `docs/codex-queue/256-report.md`

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`.
- Sửa file khác.
- **Chạy `--apply` trên thư mục thật nào.** Mọi phép thử chỉ chạy trên thư mục tạm do test tạo ra.
- Xoá hay di chuyển bất cứ thứ gì trong `typing-game-review/`.

## Việc

1. **Gốc review.**
   - Thêm `--review-root <thư mục>`. Mặc định là `path.resolve(repoRoot, '..', path.basename(repoRoot) + '-review')`, nếu thư mục đó tồn tại. Lấy đường dẫn thật bằng `realpathSync`.
   - Đọc `review.config.json` ở gốc review, nếu có; thiếu thì coi `areas` là rỗng.
   - Truyền gốc review vào `planPrune` qua `options`. Giữ nguyên chữ ký hiện có, thêm tham số dạng tùy chọn.
2. **`targetRefusal(real, repoRoot, worktreeRoot, reviewRoot)`:**
   - Đích hợp lệ khi đường dẫn thật nằm trong `<reviewRoot>/captures/`. Khi đó bỏ qua hai kiểm `not-tmp` và `outside-roots`, nhưng **vẫn** áp `FORBIDDEN`.
   - Đích nằm trong `<reviewRoot>` mà ngoài `captures/` (ví dụ `owner-review/`, hay chính gốc review) bị từ chối với lý do mới `review-not-captures`. Thứ đã gửi chủ dự án do chủ dự án tự xoá.
   - Mọi đích khác giữ đúng luật cũ.
3. **Giữ ảnh tài liệu trỏ tới.**
   - `readReferences` bắt thêm tham chiếu có dạng `captures/<khu>/...(png|jpg|jpeg|webp)`, ngoài dạng `tmp/...` đang có. Chuẩn hoá về chuỗi bắt đầu từ `captures/`.
   - `referenced` nhận thêm `reviewRoot` và `areas`. Với một ảnh có đường dẫn thật là `<reviewRoot>/captures/<khu>/<phần còn lại>`, ảnh được giữ nếu tài liệu có một trong các tham chiếu:
     - `captures/<khu>/<phần còn lại>`;
     - `<tiền tố cũ><phần còn lại>`, lấy từ `areas[<khu>][1]`, ví dụ `tmp/shots/dragon/a.png`, so khớp đúng như cách so các tham chiếu `tmp/` hiện nay;
     - `<thư mục game>/<tiền tố cũ><phần còn lại>`.
   - Ảnh nằm trong repo, như trước, giữ đúng luật cũ.
4. **Tài liệu mặc định để quét** (`defaultDocs`): giữ nguyên các gốc cũ, cộng thêm `<reviewRoot>/README.md`. Không quét `INDEX.md`, vì đó là mục lục tự sinh và liệt kê mọi thư mục.
5. **Test** (`node --test tools/capture-prune/test/prune.test.mjs`), dựng một repo giả và một thư mục review giả trong thư mục tạm, có `review.config.json` và một symlink `games/g/tmp/shots → review/captures/g/`. Phải có:
   - một đích trong `review/captures/g/run` được nhận;
   - đích `review/owner-review/...` và chính gốc review bị từ chối (`review-not-captures`);
   - ảnh `review/captures/g/run/a.png` được giữ khi tài liệu có `games/g/tmp/shots/run/a.png`; được giữ khi tài liệu có `captures/g/run/a.png`; bị liệt kê là ảnh thô khi không tài liệu nào nhắc;
   - đích đưa vào qua đường dẫn symlink (`games/g/tmp/shots/run`) cho cùng kết quả;
   - `FORBIDDEN` vẫn chặn (ví dụ `review/captures/g/art-src/...`);
   - mọi test cũ vẫn qua.
6. **README** (tiếng Việt): thêm mục thư mục review: đích nào được nhận, cờ `--review-root`, ảnh nào được giữ, và lệnh ví dụ `node tools/capture-prune/prune.mjs games/immortality-cultivation/tmp/shots/dragon/greybox-v2` (đi qua symlink).

## Kiểm bắt buộc (ghi lệnh và kết quả vào báo cáo)
1. `node --test tools/capture-prune/test/prune.test.mjs`: mọi test qua; ghi số test trước và sau.
2. `node --check tools/capture-prune/prune.mjs`.
3. **Chạy khô** (không `--apply`) trên thư mục thật `games/immortality-cultivation/tmp/shots/dragon/greybox` và chép phần tổng vào báo cáo. Liệt kê các ảnh được giữ vì `document-reference`. Đối chiếu bằng `grep -rn "dragon/greybox" docs games/immortality-cultivation/docs` để chắc mọi ảnh tài liệu trỏ tới đều được giữ.
4. `git diff --stat`: chỉ có các file được ghi.

## Hết hạn mức
Giữ mọi file, viết báo cáo phần đã xong. Dòng cuối của tin nhắn cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
