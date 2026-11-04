# Phiếu 256 · Capture-prune nhận thư mục review và giữ tham chiếu tài liệu

> **Claude duyệt (04/11/2026, khoảng 11:55).**
> - Tự chạy lại: 26/26 test qua, `node --check` qua.
> - Một sửa sau duyệt: `defaultDocs` còn bỏ qua `games/immortality-cultivation/docs`, luật cũ từ hồi Tu Tiên tạm dừng. Nay ảnh của Tu Tiên đã ở thư mục review và dọn được, nên phải quét cả tài liệu của nó.
> - Thử thật: chạy khô `games/immortality-cultivation/tmp/shots/element-fire` giữ `adv/evidence/lotus-root-cut-before.jpg` vì `document-reference`, tổng cộng 8 ảnh được giữ vì tài liệu. Trước khi sửa, ảnh đó sẽ nằm trong danh sách xoá.
> - Giới hạn còn lại, đúng theo đặc tả: tài liệu chỉ ghi thư mục và tên file riêng thì không được tính là tham chiếu. Vì vậy với thư mục do người khác tạo, luôn chạy khô và đọc danh sách trước khi `--apply`.

Ngày 04/11/2026 · Mac mini M4, macOS. Đã triển khai đúng lời giải của phiếu, một luồng, không thiết kế lại công cụ. Bộ test tăng từ **12 lên 26**, tất cả đều qua. Chạy khô greybox thật được nhận qua symlink: **0 ảnh dự kiến xóa, giữ 3 ảnh**. Không chạy `--apply` trên dữ liệu thật.

## Các file đã làm

- `tools/capture-prune/prune.mjs`: thêm `--review-root`, tự tìm gốc anh em `<tên repo>-review` nếu tồn tại, lấy realpath và đọc `review.config.json`; thiếu config hoặc `areas` thì dùng ánh xạ rỗng. Giữ nguyên chữ ký `planPrune(options, context)`; gốc tùy chọn đi qua `options.reviewRoot`.
- `tools/capture-prune/test/prune.test.mjs`: thêm fixture repo/review tạm, cấu hình và symlink `games/g/tmp/shots`; thêm 14 test hồi quy, giữ nguyên 12 test cũ.
- `tools/capture-prune/README.md`: hướng dẫn tiếng Việt về gốc review, cờ mới, tham chiếu ảnh, hàng rào bảo vệ và ví dụ greybox-v2 qua symlink.
- `docs/codex-queue/256-report.md`: báo cáo này.

Đích trong review chỉ được nhận ở cây `captures/`, vẫn áp `FORBIDDEN`. Chính gốc review, `owner-review/` và mọi nhánh khác bên trong gốc trả `review-not-captures`. Ngoài review giữ luật `tmp`, repo/worktree như trước. Không đổi cơ chế xóa, nhật ký, nhận dạng file và từ chối symlink.

Ảnh review được so với `captures/<khu>/...` và hai dạng đường dẫn cũ lấy từ `areas`. Tham chiếu `tmp/` và `captures/` được trích riêng để một dạng nằm trong tiền tố không che khuất dạng còn lại. Ảnh trong repo vẫn giữ cách so hậu tố cũ. Bộ tài liệu mặc định chỉ thêm README của review, không quét INDEX tự sinh; ngoại lệ cũ với docs nội bộ Tu Tiên vẫn giữ nguyên theo phiếu.

## Kiểm bắt buộc

### 1. Test trước và sau

Lệnh ở cả hai mốc:

```bash
node --test tools/capture-prune/test/prune.test.mjs
```

| Mốc | Tests | Pass | Fail | Bỏ qua | Mã thoát |
|---|---:|---:|---:|---:|---:|
| Trước sửa | 12 | 12 | 0 | 0 | 0 |
| Sau sửa cuối | 26 | 26 | 0 | 0 | 0 |

Phần tổng của lần cuối:

```text
ℹ tests 26
ℹ suites 0
ℹ pass 26
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
```

Test mới kiểm: nhận captures ngoài repo và không có `tmp`; chặn review root/owner-review/tiền tố giả; giữ đủ ba dạng tham chiếu và đường dẫn có tiền tố review; ảnh không tham chiếu vẫn là ảnh thô; đích qua symlink cha cho kết quả giống đường dẫn thật; `FORBIDDEN` chặn cả đích và nhánh con; ánh xạ riêng từng khu; README được quét, INDEX không được quét; `--docs` vẫn thay thế bộ mặc định; README vẫn được quét khi repo chưa có cây games; gốc tùy chọn qua realpath và CLI; thiếu config/areas; lỗi gốc/config; tham chiếu có cả `tmp/` và `captures/`. Mọi thao tác xóa của test chỉ diễn ra trong cây tạm do test tạo rồi tự dọn.

### 2. Cú pháp

```bash
node --check tools/capture-prune/prune.mjs
```

Thoát **0**, không có thông báo lỗi.

### 3. Chạy khô greybox thật và đối chiếu tài liệu

```bash
node tools/capture-prune/prune.mjs games/immortality-cultivation/tmp/shots/dragon/greybox
```

Thoát **0**. Đầu ra của lượt cuối (tab biểu diễn bằng `\t`):

```text
Danh sách ảnh thô sẽ xóa (byte):

Thư mục / nhóm cấp 1	Số file	MB (1 MB = 1.000.000 byte)
/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/dragon/greybox [cộng]	0	0.000
Tổng: 0 file, 0.000 MB; giữ 3 ảnh, từ chối 0 mục.
```

Đã dùng `node --input-type=module` gọi `parseArgs`/`planPrune` trong bộ nhớ để đọc `kept`, không tạo JSON trên đĩa. **Danh sách giữ vì `document-reference`: rỗng (0 ảnh).** Ba ảnh được giữ như sau, đường dẫn tính từ đích greybox:

| Ảnh | Lý do thực tế |
|---|---|
| `twin-pearl-greybox-play-1280x720-sheet.jpg` | `name` |
| `twin-pearl-greybox-play-1920x1080-sheet.jpg` | `name` |
| `twin-pearl-greybox-sheet.jpg` | `name` |

Đối chiếu theo đúng lệnh yêu cầu:

```bash
grep -rn "dragon/greybox" docs games/immortality-cultivation/docs
```

Thoát **0**. Đã đọc thêm các đoạn liền sau kết quả grep:

- `docs/games/tu-tien/skills/DRAGON_SKILL.md`, mục 8.7: ghi đường dẫn thư mục, sau đó nêu riêng hai tên tấm 1280 × 720 và 1920 × 1080 ở bảng trên.
- `games/immortality-cultivation/docs/changelog/2026-11-04-lab-twin-dragons-greybox.md`, mục Bằng chứng: ghi thư mục rồi nêu riêng tên tấm còn lại.
- Các kết quả khác ở hai changelog và DRAGON_SKILL trỏ tới thư mục, kịch bản, JSON hoặc clip; không có thêm đường dẫn ảnh đầy đủ cần giữ.

Vì tài liệu ghi **thư mục và basename riêng**, chúng không tạo tham chiếu ảnh đầy đủ theo regex hiện có; ba tấm vẫn được giữ nhờ tên chứa `sheet`. Mọi ảnh được các đoạn tài liệu này nêu đều có trong `kept`, không ảnh nào vào danh sách xóa. Không mở rộng suy luận Markdown ngoài lời giải của phiếu.

Đã đối chiếu thêm bằng API chỉ đọc: kế hoạch đi qua symlink và kế hoạch dùng realpath giống hệt nhau. Khi chỉ định `--docs` gồm `docs`, `games/immortality-cultivation/docs` và README review, kết quả vẫn **0 ảnh thô, giữ 3 ảnh, 0 document-reference, 0 từ chối**. Các dạng tham chiếu đầy đủ được xác nhận bằng fixture hồi quy ở mục test.

### 4. Phạm vi Git

Đã chạy:

```bash
git diff --stat
git diff --stat -- tools/capture-prune/prune.mjs tools/capture-prune/test/prune.test.mjs tools/capture-prune/README.md docs/codex-queue/256-report.md
git status --short -- tools/capture-prune/prune.mjs tools/capture-prune/test/prune.test.mjs tools/capture-prune/README.md docs/codex-queue/256-report.md
git diff --check -- tools/capture-prune/prune.mjs tools/capture-prune/test/prune.test.mjs tools/capture-prune/README.md docs/codex-queue/256-report.md
```

`git diff --stat` toàn repo có **8 đường dẫn đã thay đổi từ đầu phiên**, ngoài phạm vi phiếu: `.claude/launch.json`, ba báo cáo 118/119/120, `docs/games/THIRD_PARTY.md`, `docs/games/dragon-lane/06-other-systems.md`, hai submodule `games/immortality-cultivation` và `games/typing-survival`. Không sửa hay dọn những thay đổi này. Vì vậy điều kiện “toàn bộ diff chỉ có file được ghi” **không đúng nguyên văn ở repo đang có làn khác**, nhưng phần thay đổi của phiếu chỉ nằm trong bốn đường dẫn được phép.

Diff giới hạn phạm vi có ba file công cụ; báo cáo mới chưa được Git theo dõi nên không xuất hiện trong `diff --stat`. `status` giới hạn phạm vi liệt kê ba file công cụ sửa và báo cáo mới. `diff --check` thoát **0**, không báo lỗi khoảng trắng. Không chạy lệnh Git có ghi.

```text
 tools/capture-prune/README.md           |  31 +++++-
 tools/capture-prune/prune.mjs           |  51 +++++++---
 tools/capture-prune/test/prune.test.mjs | 169 +++++++++++++++++++++++++++++++-
 3 files changed, 233 insertions(+), 18 deletions(-)

 M tools/capture-prune/README.md
 M tools/capture-prune/prune.mjs
 M tools/capture-prune/test/prune.test.mjs
?? docs/codex-queue/256-report.md
```

## Bỏ qua và phần chủ dự án cần xem

- Không chạy `--apply` trên thư mục thật; không xóa, di chuyển hoặc ghi bất kỳ file nào trong thư mục review thật. Không tạo capture nên không chạy lại index.
- Không chạy build/test của game; không sửa src/scripts/tests/docs của Tu Tiên hoặc file của các làn khác. Không tạo ảnh hay âm thanh vì phiếu chỉ yêu cầu code.
- Chủ dự án cần lưu ý hai giới hạn đã giữ theo đặc tả: tài liệu ghi thư mục và basename riêng không được suy ra thành `document-reference`; bộ tài liệu mặc định vẫn bỏ qua docs nội bộ Tu Tiên. Khi cần quét các docs đó, truyền đủ gốc bằng `--docs` như README.

Không gặp hạn mức hoặc bước phải chờ. Không có phần triển khai còn dang dở trong phạm vi phiếu.
