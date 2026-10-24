# Lưu ảnh, nhạc, mô hình gốc trên Google Drive (phân tích 21/10/2026)

> **Dành cho:** chủ dự án và AI làm tiếp.
> **Mục tiêu:** media gốc không lên Git, nhưng máy nào cũng lấy về được bằng một lệnh.
> **Trạng thái (22/10):** đã làm xong lệnh `pnpm media:*` và test, đã sửa các lỗi từ review (hai máy, đổi tên, nhánh, pull sai md5; xem [changelog 22/10](./changelog/2026-10-22.md)). Chưa kết nối Google, chưa đẩy lần nào. Hướng dẫn dùng: [MEDIA_STORAGE.md](./MEDIA_STORAGE.md).
> Khác với bản phân tích: bắt đầu bằng client OAuth có sẵn của rclone (client riêng là tuỳ chọn, `--client-id`); Drive chia `repo/` và `private/`; danh sách nhạc riêng `media/private.md5` không vào Git (repo công khai), chỉ nằm trên Drive `_locks/`; `rclone dedupe` dùng chế độ `skip` (rclone 1.75 không có chế độ tên `identical`).

## 1. Kết luận

- Dùng **rclone** với **OAuth client riêng của chủ dự án**.
- Trên Drive có một thư mục riêng `typing-game-media/`, đường dẫn bên trong giống hệt đường dẫn trong repo.
- Git chỉ giữ một danh sách md5 nhỏ (`media.md5`), để biết bản nào khớp với code.
- Lệnh, chạy từ thư mục `typing-game`: `pnpm media:setup | status | push | pull | check`. Chạy giống nhau trên Mac và WSL.
- File đi thẳng từ ổ đĩa lên Drive. AI chỉ chạy lệnh, không tốn token theo dung lượng file.

## 2. Đo đạc (21/10)

| Nhóm | Số file | Dung lượng | Đưa lên Drive? |
|---|---|---|---|
| `art-src/3d` (mô hình gốc Tripo/Meshy) | 204 | 1,93 GB | **Có**, ưu tiên cao nhất (bản duy nhất) |
| `art-src` ảnh 2D gốc (quái, boss, icon, galaxy, fx…) | 598 | 0,95 GB | **Có** |
| `shared/music` (nhạc gốc) | 193 | 0,48 GB | **Có**, thư mục riêng tư |
| `art-src/Dota-Sounds` | 15 | 1,4 MB | **Có**, thư mục riêng tư |
| Model runtime chưa vào Git (`public/assets/.../models`, hull 11 tàu) | 393 | 0,34 GB | **Có**, để máy mới chạy được 3D mà không cần Blender |
| `art-src/models/raw` | 172 | 1,75 GB | Không: trùng y hệt `art-src/3d` |
| `art-src/models/<loại>` + cache Blender | 180 | 1,84 GB | Không: tạo lại được, cache gắn đường dẫn tuyệt đối |
| `art-src/**/*.zip` | 6 | 0,16 GB | Không: trùng file đã giải nén |
| Media đã có trong Git (trước 21/10) | — | — | Không: GitHub đã giữ |

- **Tổng cần đưa lên:** khoảng **3,7 GB**, khoảng 1.450 file. File lớn nhất 52 MB.
- **Quota Drive:** gói miễn phí 15 GB, dùng chung với Gmail và Photos. Đầy thì Gmail ngừng nhận thư. Cần kiểm tra chỗ trống trước khi đẩy. Gói 100 GB khoảng 45.000 ₫/tháng.
- **Tốc độ:** Drive cho khoảng 2 file/giây. Lần đẩy đầu mất ít nhất khoảng 12 phút, cộng thời gian tải lên.

## 3. Cách làm

### Một lần trên mỗi máy

1. Cài rclone: Mac `brew install rclone`; WSL `sudo -v ; curl https://rclone.org/install.sh | sudo bash`.
2. Tạo OAuth client riêng trên Google Cloud Console (AI soạn hướng dẫn từng màn hình bằng tiếng Việt). Phải **Publish** app, nếu để chế độ Testing thì 7 ngày phải đăng nhập lại.
3. Chạy `pnpm media:setup` **trong terminal của chủ dự án**, không qua AI, để mã bí mật không vào lịch sử chat. Trình duyệt mở, đăng nhập Google, bấm Allow.

### Hằng ngày

- `pnpm media:status`: xem file nào mới, đổi hoặc thiếu (chạy offline, dưới 1 giây).
- `pnpm media:push`: đẩy file mới và file đã đổi, rồi so md5 với Drive. Khớp hết mới cập nhật `media.md5`.
- `pnpm media:pull`: máy mới tải file còn thiếu về đúng chỗ, rồi so md5.

### Quy tắc an toàn

- Chỉ dùng `rclone copy`, **không bao giờ dùng `sync` hay `bisync`**. Hai lệnh đó có thể xóa file trên Drive khi máy bị thiếu file.
- Bản cũ bị thay trên Drive chuyển vào `_replaced/<thời điểm>/`, không tự xóa.
- Thay một file **gốc** (ảnh, model, nhạc) thì hỏi xác nhận trước.
- rclone chỉ được làm việc trong `typing-game-media/` (`root_folder_id`), không đụng file khác trên Drive.
- Mã đăng nhập nằm trong `~/.config/rclone/rclone.conf`, không bao giờ vào repo.

## 4. Những điểm phải xử lý khi làm (từ phản biện)

- Viết lệnh không có `--` (`pnpm media:push --dry-run`). pnpm 11 chuyển `--` thành tham số, làm script bỏ qua `--dry-run`.
- `rclone check` phải có `--one-way`, nếu không thì mỗi lần đẩy một phần sẽ báo lỗi.
- Hai máy: file cũ ở máy kia phải nhận ra là "cũ" (dựa vào lịch sử `media.md5`), để không đẩy đè bản mới.
- Kéo media xong phải đánh dấu để `./play.sh` build lại (file kéo về mang ngày cũ).
- Máy Windows cũ: `art-src/models/` ở đó có thể chứa file gốc duy nhất (Draconis). Không loại trừ cả thư mục, chỉ loại `models/raw` sau khi so md5.
- Nhạc và Dota-Sounds để trong `private/` trên Drive. Không bao giờ chia sẻ thư mục đó.
- 18 model đã có trong Git nhưng mất file gốc (Draconis, auriel-hero, rainbow-scout-3d, dragon-fireball): sao lưu thêm lên Drive (40 MB).
- Test đọc media phải bỏ qua file không có trong Git (đã sửa test hull Duel ngày 21/10).

## 5. Phương án đã loại

| Phương án | Lý do |
|---|---|
| Connector Google Drive của claude.ai | Dành cho tài liệu. File sẽ phải đi qua cuộc trò chuyện, không hợp để chuyển 3,7 GB. |
| Google Drive for desktop | Không có bản cho WSL. Không có lệnh so md5, khó biết khi nào tải xong. |
| Git LFS | Vẫn là Git, quota miễn phí của GitHub quá nhỏ. Trái quyết định ngày 21/10. |
| DVC | Google chặn app mặc định của DVC; vẫn cần OAuth client riêng như rclone. |
| git-annex | Thêm một lớp quản lý phiên bản, khó dùng, phụ thuộc symlink trên Windows. |
| Nén zip lên Drive | Mất kiểm tra từng file; đổi một file phải tải lại cả gói. |
| Viết lại lịch sử Git để xóa media cũ | Phải force-push, làm hỏng các bản clone. Để quyết định riêng sau. |

## 6. Việc tiếp theo

1. ~~AI viết `scripts/media/media.mjs`, `media/media.config.json`, lệnh `pnpm media:*`, test với rclone backend local.~~ Xong 22/10.
2. Chủ dự án chạy `pnpm media:setup` trong terminal của mình (đăng nhập Google một lần).
3. `pnpm media:push --dry-run`, rồi `pnpm media:push`. Commit `games/space-typing/media.md5` theo dòng lệnh script in ra.
4. Diễn tập khôi phục: `pnpm media:check --remote`, rồi `pnpm media:pull --to ~/media-restore-test` và so md5.
5. Sau khi Drive đủ và khớp md5, chủ dự án mới xóa bản trùng (`art-src/models/raw`, `~/Downloads/img-typing`).
