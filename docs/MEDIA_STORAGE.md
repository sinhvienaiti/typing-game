# Kho media trên Google Drive

Ảnh, nhạc, mô hình 3D và height map (`.bin`) không lên Git. Chúng nằm trên Google Drive, trong một thư mục riêng tên `typing-game-media`. Git chỉ giữ danh sách md5 (`games/space-typing/media.md5`) để biết bản nào khớp với code.

Mọi lệnh chạy trong thư mục `typing-game`, giống nhau trên Mac và WSL:

```bash
pnpm media:status     # không cần mạng: Thiếu / Mới / Khác
pnpm media:push       # đẩy file mới hoặc đã đổi, so md5, cập nhật danh sách
pnpm media:pull       # tải file còn thiếu, so md5
pnpm media:check      # kiểm tra (thêm --remote để kiểm tra cả Drive)
```

Viết cờ **không có `--`** đứng trước: `pnpm media:push --dry-run`. Script cũng chấp nhận `pnpm media:push -- --dry-run`, và báo lỗi, không làm gì, khi gặp cờ lạ.

## Cái gì đi đâu

| Nhóm | Gồm | Trên Drive | Bản cũ khi bị thay |
|---|---|---|---|
| `originals` | `games/space-typing/art-src/**` (mô hình gốc `3d/`, ảnh 2D gốc, prompt, `ships/rendered`, file `.blend`) | `repo/games/space-typing/art-src/...` | Chuyển vào `_replaced/` |
| `runtime` | Mọi file media trong `games/space-typing` mà Git không theo dõi (GLB trong `public/`, hull tàu, ảnh trong `docs/`…), cộng 14 mô hình runtime đã mất bản gốc | `repo/games/space-typing/...` | Thay thẳng (tạo lại được) |
| `private` | `shared/music/**`, `art-src/Dota-Sounds/**`, `public/local-assets/**` | `private/...` | Chuyển vào `_replaced/` |

Đo ngày 21/10 trên Mac: originals 834 file (2,9 GB), runtime 423 file (371 MB), private 208 file (481 MB). Tổng khoảng 1.465 file, 3,7 GB.

Không đưa lên:

- `art-src/models/raw/**`: chỉ bỏ file trùng md5 với một file `art-src/3d` có trong `SOURCES.json` **và** có ở máy này hoặc đã có trong `media.md5`. File nào không trùng vẫn được đẩy và hiện trong `--dry-run`.
- Cache build của Blender: `.campaign3d-model-cache/`, `.ship-model-cache/` (gắn với đường dẫn của từng máy). Bản Blender đã xử lý `art-src/models/<loại>/*.glb` thì **có** đưa lên, để máy khác đóng gói lại mà không cần Blender (chủ dự án chốt 22/10).
- `**/*.zip`, `**/_out/**`, `.DS_Store`, `._*`, `Thumbs.db`, `*:Zone.Identifier` (file phụ Windows tạo khi tải về, hiện ra trong WSL).
- Tên file có ký tự Windows không cho phép (`< > : " | ? *`): bị bỏ qua, `pnpm media:status` liệt kê để đổi tên.
- File Git đã theo dõi (GitHub giữ), `node_modules`, `dist`, `.visual`.

Thư mục trên Drive:

- `README.txt`: không sửa tay, không chia sẻ `private/`.
- `repo/`, `private/`: đường dẫn giống hệt trong repo. Có thể tải tay từng file trên web Drive.
- `_replaced/<thời điểm>/`: bản cũ bị thay. Không bao giờ tự xoá.
- `_locks/<thời điểm>/`: bản sao danh sách md5 sau mỗi lần đẩy.

Danh sách nhạc riêng (`media/private.md5`) không vào Git, vì repo công khai. Nó chỉ nằm trên máy và trong `_locks/` trên Drive.

## Cài đặt (một lần mỗi máy)

Tự chạy trong **terminal của bạn**, không chạy qua AI. Không dán mã, mật khẩu hay token vào chat.

1. Cài rclone.
   - Mac: `brew install rclone`
   - WSL Ubuntu: `sudo -v ; curl https://rclone.org/install.sh | sudo bash`. Không dùng `apt` (bản quá cũ). Chỉ cài trong WSL, không cài thêm `rclone.exe` trên Windows.
2. `pnpm media:setup`
   - Trình duyệt mở. Đăng nhập **tài khoản @gmail.com cá nhân**, không dùng tài khoản công ty. Bấm Allow.
   - WSL: nếu trình duyệt không mở, chép link `http://127.0.0.1:53682/...` rclone in ra sang Chrome trên Windows.
   - Script tự tạo thư mục `typing-game-media` và khoá rclone vào thư mục đó (`root_folder_id`). rclone không thấy file nào khác trên Drive.
   - Cuối cùng script in dung lượng còn trống. Lần đẩy đầu cần khoảng 3,7 GB, cộng 2 GB dự phòng. Drive đầy thì Gmail ngừng nhận thư.
   - Kiểm tra chỗ trống chỉ làm được với tài khoản có hạn mức (Gmail cá nhân). Tài khoản Workspace dùng chung dung lượng không báo hạn mức: push cảnh báo rồi bỏ qua bước này.
3. Đăng nhập hết hạn (lâu không dùng, đổi mật khẩu): `pnpm media:setup --reconnect`.

Client OAuth riêng (tuỳ chọn, khi client có sẵn của rclone bị Google chặn hoặc chậm):

- Tạo Desktop client trong Google Cloud Console (bật Drive API, scope `.../auth/drive`, bấm **Publish app**; để Testing thì 7 ngày phải đăng nhập lại).
- `rclone config delete tgmedia` rồi `pnpm media:setup --client-id <id>`. Secret gõ ẩn, hoặc đặt biến `TGMEDIA_CLIENT_SECRET`. Secret không bao giờ nằm trên dòng lệnh.

## Hằng ngày

Thêm hoặc sửa media:

```bash
pnpm media:status
pnpm media:push --dry-run      # xem trước; danh sách đầy đủ ở .cache/media-push-dry-run.txt
pnpm media:push
```

- Mô hình 3D mới trong `art-src/3d`: chạy `node games/space-typing/scripts/models/index-3d-sources.mjs` trước. Push từ chối nếu `SOURCES.json` chưa khớp.
- Thay một file gốc (originals, private): script hỏi `y` trước. Bản cũ trên Drive chuyển vào `_replaced/`. `--yes` bỏ câu hỏi này, và chỉ câu hỏi này.
- Push chỉ cập nhật danh sách md5 sau khi Drive xác nhận md5 của mọi dòng và bản sao danh sách đã lên `_locks/`. Rồi script in sẵn lệnh commit `media.md5`. Script không tự commit.
- Đổi tên file: script nhận ra theo md5 và hỏi `y`. `--yes` không trả lời thay, vì tên cũ có thể chỉ là file máy khác vừa thêm mà máy này chưa tải. Không có terminal để trả lời: `--forget <đường dẫn cũ>`.
- Xoá file có chủ ý: push hỏi `y`, hoặc dùng `--forget <đường dẫn>`. Bản trên Drive vẫn giữ.
- File đã bị bỏ khỏi danh sách (đổi tên hoặc `--forget`, ở máy này hay máy khác) mà vẫn còn trên máy: push không đẩy lại, `status` ghi `Đã bị bỏ khỏi danh sách`. Không cần nữa thì chuyển vào `.media-old/`. Cần thêm lại: `pnpm media:push --readd <đường dẫn>`.
- Đẩy dở (mất mạng, tắt máy): chạy lại `pnpm media:push`. File đã lên được bỏ qua theo md5.

Lấy media về:

```bash
pnpm media:pull                     # tất cả nhóm
pnpm media:pull --only runtime      # chỉ để chơi (khoảng 370 MB)
```

- Pull chỉ tải file còn thiếu. Không ghi đè, không xoá file nào của bạn.
- File tải vào `.media-tmp/` trước. Khớp md5 mới chuyển vào đúng chỗ. File khác md5 chuyển vào `.media-old/<thời điểm>/mismatch/`, không vào repo, không vào `media.md5`; chạy `pnpm media:check --remote`.
- Sau khi tải, `./play.sh` tự build lại Space Typing. WSL: Vite đang chạy thì khởi động lại.
- Nhạc mới: `./dev.sh` và `./play.sh` tự chạy `pnpm music:index`.

## Hai máy (Mac và Windows/WSL)

- Trước khi làm việc trên máy kia: `git pull` (cả submodule), rồi `pnpm media:pull`.
- File ở máy này **cũ hơn** bản trên Drive (md5 trùng một bản cũ trong lịch sử `media.md5`): push từ chối, để Drive không quay về bản cũ. Chạy `pnpm media:pull --update-stale`: bản cũ chuyển vào `.media-old/<thời điểm>/`, bản mới được tải về.
- Máy khác vừa đẩy mà máy này chưa `git pull`: push từ chối và nói rõ. Script đọc các bản sao trong `_locks/` từ mới nhất về, dừng ở bản đầu tiên máy này đã biết, nên bản sửa nhiều lần trước một lần commit không làm push bị chặn.
- Đẩy từ một nhánh khác trên cùng máy (ví dụ nhánh feature): không bị từ chối. Push nhắc merge nhánh đó để `media.md5` đủ dòng (không phải `git pull`).
- Giờ hai máy lệch nhau (WSL hay chậm giờ sau khi ngủ): bản sao mới luôn có thời điểm sau bản mới nhất trên Drive, và push cảnh báo. Chỉnh giờ WSL: `wsl --shutdown` trong PowerShell rồi mở lại.
- `games/space-typing` đang ở detached HEAD: push từ chối, vì commit `media.md5` dễ mất. Chuyển về một nhánh trước.
- Máy Windows cũ: dùng `pnpm media:push --new-only`. Lệnh này chỉ thêm file mới, không thay file nào, và không tự bỏ dòng nào khỏi danh sách (chỉ `--forget` mới bỏ).
- Máy Windows cũ có thể còn bản gốc duy nhất của Draconis, auriel-hero, rainbow-scout-3d, dragon-fireball (trong `art-src\models\raw\heroes\`, `art-src\models\heroes\`, `art-src\models\blend\`). Chạy `pnpm media:status --find-unknown` để liệt kê. Chép bản gốc vào `art-src/3d`, chạy `index-3d-sources`, rồi `pnpm media:push --new-only --only originals`. **Không xoá `art-src/models` trên Windows** khi danh sách đó chưa rỗng.

## Diễn tập khôi phục

Làm sau lần đẩy đầu, rồi mỗi năm một lần.

1. `pnpm media:check --remote`. Đúng là: thiếu 0, khác 0, `art-src/3d: 204/204 khớp`.
2. `pnpm media:pull --to ~/media-restore-test`. Đúng là: `Khớp N/N`. Xong thì xoá thư mục tạm.
3. (Tuỳ chọn) Clone vào thư mục khác, `pnpm media:pull --only runtime`, `pnpm media:check --only runtime`. Không chạy `./dev.sh` hay `./play.sh` trong bản clone: nginx sẽ trỏ sang bản clone. Lỡ chạy thì chạy lại `./dev.sh` trong thư mục chính.

Chỉ sau bước 1 và 2 mới xoá bản trùng trên Mac: `games/space-typing/art-src/models/raw` và `~/Downloads/img-typing`. Không bao giờ xoá `art-src/3d`.

## Kiểm tra định kỳ

- Mỗi tháng: `pnpm media:check --remote`. Lệnh này cũng giữ đăng nhập không hết hạn (Google thu hồi token sau 6 tháng không dùng).
- Báo trùng tên trên Drive: `pnpm media:check --remote --fix-duplicates`. Chỉ xoá bản trùng giống hệt (cùng md5); bản khác nhau giữ nguyên.
- `check --remote` in dung lượng `_replaced/`. Dọn tay trên web Drive khi cần, rồi dọn thùng rác (thùng rác cũng tính vào dung lượng).
- Bản build phát hành phải làm trên máy đã `media:pull` và `media:check` sạch. Clone mới và CI không có file runtime.

## Quy tắc an toàn

- Script chỉ dùng `rclone copy`, `check`, `lsjson`, `size`… Không bao giờ dùng `sync`, `bisync`, `move`, `delete`, `purge`. Script chặn các lệnh đó bằng danh sách cho phép. Ngoại lệ duy nhất: `dedupe --dedupe-mode skip` sau `--fix-duplicates`.
- Không sửa, xoá hay chia sẻ thư mục trên Drive bằng tay. Không bao giờ chia sẻ `private/`.
- `~/.config/rclone/rclone.conf` có quyền vào toàn bộ Drive. Không đưa vào repo, không gửi ai. Không bật mã hoá rclone.conf (các lệnh chạy không hỏi mật khẩu).
- Drive và máy Mac là hai bản duy nhất. Mỗi năm chép `art-src/3d` và `shared/music` ra ổ ngoài một lần.

## Khi gặp lỗi

| Thông báo | Làm gì |
|---|---|
| `Chưa có rclone` | Cài rclone (mục Cài đặt). |
| `Máy này chưa kết nối Google Drive` | `pnpm media:setup` trong terminal của bạn. |
| `máy này thiếu N file có trong danh sách` | Chưa tải: `pnpm media:pull`. Đã xoá có chủ ý: trả lời `y` hoặc `--forget`. |
| `cũ hơn bản trên Drive` | `pnpm media:pull --update-stale`. |
| `Drive có danh sách md5 mới hơn từ máy khác` | `git pull` + `git submodule update`, `pnpm media:pull`, rồi đẩy lại. Máy kia đã mất commit `media.md5` (chưa kịp commit, hỏng máy): chép `_locks/<mới nhất>/space-typing.media.md5` trên Drive thành `games/space-typing/media.md5`, chạy `pnpm media:status`, `pnpm media:pull`, rồi commit. |
| `chưa chép được danh sách md5 vào _locks/` | File đã lên Drive; `media.md5` chưa đổi. Chạy lại `pnpm media:push`. |
| `Đã bị bỏ khỏi danh sách` | File này đã bị đổi tên hoặc `--forget`. Chuyển vào `.media-old/`, hoặc `--readd <đường dẫn>` để thêm lại. |
| `dòng nằm ngoài nhóm của nó` | Danh sách có đường dẫn không phải media của nhóm đó (ví dụ `.git/`, `scripts/`). Sửa `media.md5` (hoặc bản trên Drive) cho đúng; script không dùng danh sách đó. |
| `Drive không báo hạn mức` | Tài khoản Workspace: không kiểm tra được chỗ trống, push vẫn chạy. Tự xem dung lượng trên web Drive. |
| `Drive còn trống …` | Dọn `_replaced/` và thùng rác, hoặc nâng gói Drive. |
| `còn dấu xung đột merge` trong `media.md5` | Sửa xung đột, giữ dòng của cả hai phía, rồi `pnpm media:check --remote`. |
| Lỡ mất `media.md5` chưa commit | Lấy `_locks/<mới nhất>/space-typing.media.md5` trên Drive, chép thành `games/space-typing/media.md5`. |

## Cho người làm tiếp

- Code: `scripts/media/` (chỉ dùng thư viện có sẵn của Node). Cấu hình nhóm: `media/media.config.json`.
- Test: `pnpm media:test`. Có test chạy rclone thật với một thư mục local đóng vai Drive (bỏ qua nếu máy không có rclone).
- Cache md5: `.cache/media-hash.json` (theo kích thước và thời điểm sửa file).
- Phân tích và các phương án đã loại: [MEDIA_GOOGLE_DRIVE_PLAN_2026-10-21.md](./MEDIA_GOOGLE_DRIVE_PLAN_2026-10-21.md).
