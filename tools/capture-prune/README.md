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
| `--review-root <thư mục>` | Chỉ định gốc review thay cho thư mục anh em mặc định; dùng đường dẫn thật của thư mục này. |
| `--docs <gốc>...` | Quét đệ quy `.md` dưới các gốc, hoặc nhận trực tiếp file Markdown. Thay thế bộ gốc mặc định; phải đặt các đích trước `--docs`. Có thể lặp lại tùy chọn này. |
| `--json <file>` | Ghi kết quả JSON; cần đuôi `.json`, nằm ngoài các đích. Tạo thư mục cha nếu thiếu. Có thể ghi lại file JSON thường, không ghi qua symlink hoặc hard link. |
| `--help` | In cú pháp và thoát. |

Đầu ra gồm từng ảnh thô cùng số byte, bảng theo thư mục con cấp 1 của từng đích và dòng tổng. Nhóm `.` chứa ảnh trực tiếp ở đích. **MB = 1.000.000 byte**. Ảnh giữ lại không xuất hiện trong danh sách sẽ xóa; JSON chứa chúng trong `kept`.

## Thư mục review cạnh source

Nếu tồn tại, gốc review mặc định là thư mục cùng cấp có tên repo cộng `-review`: với repo này là `/Volumes/SS990TPRO/htdocs/typing-game-review`. Có thể thay bằng `--review-root <thư mục>`; gốc chỉ định phải tồn tại. Công cụ lấy `realpath` rồi đọc `review.config.json` tại đó. Thiếu file cấu hình hoặc thiếu `areas` thì dùng ánh xạ rỗng; cấu hình JSON lỗi làm lệnh dừng.

Chỉ nhận đích có đường dẫn thật trong `<gốc review>/captures/`, vẫn chặn mọi đường dẫn bảo vệ. Các đích này không cần thành phần `tmp` và không cần nằm trong repo/worktree. Chính gốc review, `owner-review/` và các thư mục khác bên trong gốc bị từ chối với mã `review-not-captures`; chủ dự án tự xóa thứ đã gửi duyệt.

Đường dẫn cũ đi qua symlink thư mục cha cũng dùng được. Ví dụ chạy khô từ repo cha:

```bash
node tools/capture-prune/prune.mjs games/immortality-cultivation/tmp/shots/dragon/greybox-v2
```

Đích trên được giải thành `captures/tu-tien/dragon/greybox-v2` trong review. Bản thân đích vẫn phải là thư mục thường; không truyền chính symlink `tmp/shots` làm đích.

Với `areas["tu-tien"] = ["games/immortality-cultivation", "tmp/shots/"]`, ảnh `captures/tu-tien/dragon/a.png` được giữ vì `document-reference` khi Markdown có một trong ba dạng:

- `captures/tu-tien/dragon/a.png` (kể cả khi có tiền tố đường dẫn tới gốc review);
- `tmp/shots/dragon/a.png`;
- `games/immortality-cultivation/tmp/shots/dragon/a.png`.

Hai dạng cũ được so theo hậu tố `tmp/...` như trước. Tiền tố lấy riêng cho từng khu từ `areas`, không suy đoán khi thiếu cấu hình. Các luật giữ theo tên, thư mục compare và tuổi ảnh vẫn áp dụng. Bộ tài liệu mặc định thêm đúng `<gốc review>/README.md`, không quét `INDEX.md` tự sinh hoặc toàn bộ cây review. `--docs` vẫn thay thế toàn bộ bộ gốc mặc định này.

## Luật giữ ảnh

Chỉ xét file thường có đuôi `.png`, `.jpg`, `.jpeg`, `.webp`, không phân biệt hoa thường. JSON, Markdown, video và các loại file khác được để nguyên.

Một ảnh được giữ nếu có ít nhất một lý do sau; JSON ghi đủ các lý do trùng nhau:

| Mã trong `kept[].reasons` | Điều kiện |
|---|---|
| `name` | Tên file chứa `sheet`, `contact` hoặc `compare`, không phân biệt hoa thường. |
| `compare-directory` | Một thư mục trong đường dẫn có tên bắt đầu bằng `compare`, không phân biệt hoa thường. |
| `document-reference` | Ảnh trong repo khớp hậu tố `tmp/...` như trước; ảnh trong review khớp `captures/<khu>/...` hoặc đường dẫn cũ theo `areas` như mục trên. |
| `too-new` | Mtime ở trong ngưỡng tuổi, kể cả đúng mốc biên hoặc ở tương lai. |

Mặc định quét `docs`, `games/*/docs`, `games/*/*.md` và README của review nếu có. Giữ nguyên ngoại lệ không duyệt `games/immortality-cultivation` trong bộ gốc mặc định; dùng `--docs` để chỉ định tài liệu tại đó khi cần. Bộ gốc mặc định chưa tồn tại được bỏ qua; gốc `--docs` chỉ định nhưng không đọc được gây lỗi để tránh xóa khi thiếu tham chiếu. Không đi theo symlink tài liệu. Chuỗi lấy từ Markdown khớp biểu thức `tmp/[^\s)\x60"'<>]+\.(png|jpe?g|webp)` và biểu thức tương tự bắt đầu bằng `captures/`; `\x60` biểu diễn dấu backtick. Hai dạng được quét riêng để không che khuất nhau khi cùng xuất hiện trong một đường dẫn. Cả `tmp/run/a.png` và `games/x/tmp/run/a.png` đều giữ ảnh tương ứng. Tham chiếu review được lấy từ `captures/`, kể cả khi đường dẫn ghi đủ tới gốc review. Không giải mã URL hoặc suy diễn đường dẫn có khoảng trắng ngoài biểu thức này.

## Luật từ chối và xóa

- Kiểm tra đường dẫn thật bằng `realpath`: ngoài gốc review, phải có thành phần thư mục `tmp` và nằm trong repo chứa công cụ hoặc cây anh em `../typing-game-wt/`. Trong gốc review chỉ nhận cây `captures/` như mục trên. So ranh giới thư mục, không nhận đường dẫn chỉ trùng tiền tố repo hoặc `captures`.
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

Kết quả lệnh nguyên văn và giới hạn kiểm tra đồng thời được ghi riêng trong [báo cáo 048](../../docs/codex-queue/048-report.md). Kiểm hồi quy cho thư mục review và lượt chạy khô greybox được ghi trong [báo cáo 256](../../docs/codex-queue/256-report.md).
