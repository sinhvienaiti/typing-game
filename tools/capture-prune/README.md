# Dọn ảnh thô của lượt chụp test

CLI Node ESM, chỉ dùng thư viện chuẩn. Mặc định **chỉ liệt kê**, không xóa ảnh và không tạo nhật ký. Chỉ dùng `--apply` cho lượt chụp do chính mình tạo, sau khi đã chấm và giữ đủ bằng chứng. Công cụ không xác định được ai sở hữu ảnh; nên truyền đúng thư mục của lượt chụp thay vì toàn bộ `tmp` đang dùng chung.

## Cách chạy

Chạy từ repo cha:

```bash
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban
node tools/capture-prune/prune.mjs games/dragon-hold/tmp games/typing-defense/tmp games/typing-survival/tmp --json tools/capture-prune/.tmp/dry-run.json
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban --min-age-min 60 --docs docs games/dragon-hold/docs
```

Khi chủ lượt chụp đã xem danh sách và muốn xóa:

```bash
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban --apply
```

| Đối số | Ý nghĩa |
|---|---|
| `<thư mục>...` | Một hoặc nhiều thư mục đích; đường dẫn tương đối tính từ thư mục đang đứng. |
| `--apply` | Xóa đúng tập ảnh được tính trong lần gọi này; không quét thêm khi xóa. |
| `--min-age-min N` | Giữ ảnh có mtime cách hiện tại không quá N phút, mặc định 30. N hữu hạn, không âm; ảnh có mtime tương lai cũng được giữ. |
| `--docs <gốc>...` | Quét đệ quy `.md` dưới các gốc, hoặc nhận trực tiếp file Markdown. Thay thế bộ gốc mặc định; phải đặt các đích trước `--docs`. Có thể lặp lại tùy chọn này. |
| `--json <file>` | Ghi kết quả JSON; cần đuôi `.json`, nằm ngoài các đích. Tạo thư mục cha nếu thiếu. Có thể ghi lại file JSON thường, không ghi qua symlink hoặc hard link. |
| `--help` | In cú pháp và thoát. |

Đầu ra gồm từng ảnh thô cùng số byte, bảng theo thư mục con cấp 1 của từng đích và dòng tổng. Nhóm `.` chứa ảnh trực tiếp ở đích. **MB = 1.000.000 byte**. Ảnh giữ lại không xuất hiện trong danh sách sẽ xóa; JSON chứa chúng trong `kept`.

## Luật giữ ảnh

Chỉ xét file thường có đuôi `.png`, `.jpg`, `.jpeg`, `.webp`, không phân biệt hoa thường. JSON, Markdown, video và các loại file khác được để nguyên.

Một ảnh được giữ nếu có ít nhất một lý do sau; JSON ghi đủ các lý do trùng nhau:

| Mã trong `kept[].reasons` | Điều kiện |
|---|---|
| `name` | Tên file chứa `sheet`, `contact` hoặc `compare`, không phân biệt hoa thường. |
| `compare-directory` | Một thư mục trong đường dẫn có tên bắt đầu bằng `compare`, không phân biệt hoa thường. |
| `document-reference` | Đường dẫn POSIX tính từ repo kết thúc bằng chuỗi ảnh `tmp/...` lấy từ Markdown. |
| `too-new` | Mtime ở trong ngưỡng tuổi, kể cả đúng mốc biên hoặc ở tương lai. |

Mặc định quét `docs`, `games/*/docs` và `games/*/*.md`. Không duyệt game `immortality-cultivation` đang tạm dừng. Bộ gốc mặc định chưa tồn tại được bỏ qua; gốc `--docs` chỉ định nhưng không đọc được gây lỗi để tránh xóa khi thiếu tham chiếu. Không đi theo symlink tài liệu. Chuỗi lấy từ Markdown khớp biểu thức `tmp/[^\s)\x60"'<>]+\.(png|jpe?g|webp)`; `\x60` biểu diễn dấu backtick. Cả `tmp/run/a.png` và `games/x/tmp/run/a.png` đều giữ ảnh tương ứng. Không giải mã URL hoặc suy diễn đường dẫn có khoảng trắng ngoài biểu thức này.

## Luật từ chối và xóa

- Kiểm tra đường dẫn thật bằng `realpath`: phải có thành phần thư mục `tmp` và nằm trong repo chứa công cụ hoặc cây anh em `../typing-game-wt/`. So ranh giới thư mục, không nhận đường dẫn chỉ trùng tiền tố repo.
- Từ chối đích có thành phần `art-src`, `public`, `docs`, `typing-game-handoff`, `immortality-cultivation`; cả biến thể nối bằng `-`/`_` cũng được bảo vệ. So theo thành phần để `htdocs` trên Mac không bị hiểu nhầm là `docs`. Không duyệt các thư mục con bảo vệ này.
- Không nhận đích là symlink, không đi theo symlink thư mục, không chọn file symlink. Symlink gãy cũng bị bỏ qua. Mục có `realpath` ra ngoài đích ghi `outside-target` vào `refused`; symlink còn lại ghi `symlink`.
- Khi `--apply`, kiểm tra lại file thường, symlink ở các thư mục cha, realpath và bộ nhận dạng `dev`, `ino`, kích thước, mtime, ctime. File đã đổi được bỏ qua và ghi vào `refused`. File xuất hiện sau lúc lập danh sách không bị xóa. Các đích trùng/chồng nhau không làm một ảnh được chọn hai lần.
- Mỗi đích có ảnh được chọn sẽ giữ chỗ nhật ký độc quyền `.pruned-YYYYMMDD-HHmm.txt` trước khi xóa. Mỗi lần xóa thành công ghi ngay `đường_dẫn_tương_đối<TAB>số_byte`. Không ghi ảnh xóa thất bại vào nhật ký. Nhật ký cùng phút đã tồn tại thì bỏ thao tác trên đích đó, không ghi đè; chọn phút khác khi chạy lại. Nếu không xóa được file nào, nhật ký đã giữ chỗ có thể rỗng.
- Không xóa thư mục rỗng, không sửa nội dung ảnh giữ lại. Không có chế độ khôi phục sau khi xóa.

JSON có `targets` (các đích hợp lệ, đường dẫn thật), `files` (danh sách dự kiến xóa), `kept` (ảnh và lý do giữ), `bytes` (tổng byte dự kiến), `refused` (đường dẫn và lý do). Mỗi ảnh có `target`, `path`, `relative`, `bytes`; ảnh được chọn còn có `identity` để kiểm lại trước khi xóa. Khi áp dụng có thêm `deleted` (đường dẫn đã xóa) và `logs`. `files`/`bytes` vẫn là kế hoạch ban đầu nếu có lỗi khi áp dụng. Đầu ra JSON được kiểm tra trước khi xóa.

Mã thoát: **0** khi hoàn tất với ít nhất một đích hợp lệ (kể cả danh sách rỗng hoặc có đích khác bị từ chối); **2** khi mọi đích bị từ chối; **1** khi sai đối số, lỗi đọc tài liệu/ghi JSON hoặc lỗi áp dụng. Vì vậy luôn xem `refused`, ngay cả khi mã thoát là 0.

## Kiểm thử

Test tự tạo cây giả bằng `fs.mkdtempSync()` dưới `os.tmpdir()`, chỉ chạy `--apply` trong cây đó và tự xóa cây của mình sau khi xong. Không cần game, mạng, trình duyệt hoặc gói ngoài.

```bash
node --test tools/capture-prune/test/*.test.mjs
```

Kết quả lệnh nguyên văn và giới hạn kiểm tra đồng thời được ghi riêng trong [báo cáo 048](../../docs/codex-queue/048-report.md).
