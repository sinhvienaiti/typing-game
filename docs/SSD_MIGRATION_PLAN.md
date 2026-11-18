# Chuyển dự án sang ổ SSD rời (03/11/2026)

Anh hỏi: "hiện tại tôi có lắp thêm ổ ssd rời… nếu ổn thì đưa cả dự án sang ổ đó, để tránh việc bị đầy ổ… bạn kiểm tra nếu đạt thì lên plan di chuyển source sang đó, và sửa lại đầy đủ các cấu hình để có thể phát triển tiếp".

## 1. Kết quả kiểm tra: đạt

**Ổ SSD rời**

| Mục | Kết quả |
|---|---|
| Ổ | Samsung SSD 990 PRO 2 TB (NVMe), hộp ACASIS TBU405Pro |
| Kết nối | Thunderbolt / USB4, 40 Gb/s, giao thức PCI-Express |
| Định dạng | APFS, không phân biệt hoa thường (giống ổ trong), không mã hóa |
| Sức khỏe | SMART: Verified |
| Còn trống | 1,8 TiB; trên ổ chỉ có thư mục `manga` của anh, không đụng tới |
| Ghi | 2 GB tuần tự trong 0,73 s, khoảng 2,9 GB/s (có cache) |
| File nhỏ | 5.000 file trong 0,24 s; `stat` khoảng 2 µs mỗi file |
| Sở hữu | "Owners: Disabled": macOS coi mọi file là của người đang dùng. Git và Node vẫn chạy bình thường. Bật lại được nếu muốn (bước 5) |

Với code, Node, Vite, Git và trình duyệt chụp ảnh, ổ này nhanh hơn mức cần.

**Ổ trong của máy:** còn 7,3 GB trống trên 228 GB (97 % đã dùng). Đây là việc gấp:
- `heavy.sh --gpu` dừng các lượt chụp khi trống dưới 10 GB;
- các agent đang chụp ảnh nên dễ bị kẹt.

**Dung lượng cần chuyển:**
- `~/htdocs/typing-game`: 66 GB, gồm các game, worktree `.wt-*`, `tmp/`, `art-src`, `node_modules`;
- `~/htdocs/typing-game-wt`: 149 MB.

## 2. Cách làm: chuyển rồi để một liên kết tại đường dẫn cũ

- Thư mục dự án chuyển sang `/Volumes/SS990TPRO/htdocs/typing-game`.
- Ở đường dẫn cũ `/Users/toandx/htdocs/typing-game` đặt một symlink trỏ sang đó. Làm tương tự cho `typing-game-wt`.

Mọi đường dẫn tuyệt đối đang có vì thế vẫn đúng, không phải sửa từng chỗ:
- `.claude/launch.json`, cấu hình nginx, các script trong `scripts/` và `.local/bin`;
- cron heartbeat;
- đường dẫn worktree mà Git ghi trong `.git/worktrees`;
- bộ nhớ của Claude (gắn với đường dẫn dự án `-Users-toandx-htdocs-typing-game`).

Cách sửa từng đường dẫn sang `/Volumes/...` rủi ro hơn nhiều: dễ sót, và làm mất bộ nhớ của Claude.

## 3. Các bước

0. **Sao chép trước (đang chạy, không đụng bản gốc):** `rsync -aHAX --numeric-ids`, giữ symlink, hard link, quyền và thuộc tính mở rộng. Bản gốc vẫn dùng bình thường trong lúc chép.
1. **Chọn lúc rảnh:** không agent nào đang chạy. Dừng mọi dev server của dự án:
   - của Claude: 3160, 3162, 3018 và các server tạm của agent;
   - các server cũ từ 01–02/11 trong các worktree `.wt-*`, cổng 3027–3028, 3341–3344, 4191–4196. Chúng thuộc các phiên khác; Claude chỉ dừng khi anh đồng ý.
2. **Chép lần cuối:** chạy lại rsync với `--delete`. Chỉ phần đổi từ lần trước được chép, mất vài phút.
3. **Kiểm bản chép:**
   - số file và dung lượng khớp;
   - `git status` trùng với bản gốc ở repo cha, mọi repo game và các worktree;
   - `git fsck --connectivity-only` ở từng repo.
4. **Đổi chỗ:**
   - `mv ~/htdocs/typing-game ~/htdocs/typing-game.pre-ssd` (giữ lại làm bản dự phòng);
   - `ln -s /Volumes/SS990TPRO/htdocs/typing-game ~/htdocs/typing-game`;
   - làm tương tự với `typing-game-wt`.
5. **Cấu hình sau khi chuyển:**
   - pnpm: đặt kho package lên SSD (`pnpm config set store-dir /Volumes/SS990TPRO/.pnpm-store`), vì hard link không đi qua hai ổ khác nhau. Không đổi thì lần cài sau vẫn chạy, chỉ chậm hơn;
   - `heavy.sh` đo chỗ trống bằng `df` của thư mục đang chạy, nên sau khi đổi chỗ nó tự đo trên SSD;
   - Vite và Node chạy qua symlink bình thường (đã có tiền lệ: các bản lab cố định cho anh đều dùng `node_modules` qua symlink).
6. **Chạy thử:**
   - `pnpm test` và `pnpm build` ở game Tu Tiên;
   - mở lại bản lab cho anh (3160, 3162) và trang chơi;
   - một lượt chụp nhỏ qua `heavy.sh`;
   - `git status` không có thay đổi lạ.
7. **Khởi động lại** các phiên Claude và cửa sổ Terminal đang mở. Một tiến trình đang "đứng" trong thư mục cũ sẽ vẫn trỏ vào bản `.pre-ssd` cho tới khi mở lại.
8. **Sau 1–2 ngày dùng ổn:** anh đồng ý thì xóa `typing-game.pre-ssd`, giải phóng khoảng 66 GB trên ổ trong.

## 4. Việc anh tự làm (cần mật khẩu hoặc bấm cho phép)

- **Nên làm:**
  - Không cho ổ ngủ để tránh bị ngắt giữa chừng: `sudo pmset -a disksleep 0`.
  - Luôn cắm ổ khi làm việc. Nếu ổ bị rút, đường dẫn dự án sẽ tạm hỏng cho tới khi cắm lại.
- **Nếu macOS hỏi** cho Terminal, Claude hoặc Node truy cập "Removable Volumes": bấm Allow.
- **Không bắt buộc:**
  - bật quyền sở hữu trên ổ: `sudo diskutil enableOwnership /Volumes/SS990TPRO`;
  - thêm thư mục dự án vào Spotlight Privacy, để máy không lập chỉ mục hàng trăm nghìn file `node_modules`.

## 5. Rủi ro và cách lùi lại

| Rủi ro | Cách xử lý |
|---|---|
| Ổ bị ngắt khi đang ghi | Cắm lại; Git tự kiểm khi chạy lệnh. Bước 4 của mục trên giảm khả năng này |
| Công cụ đọc đường dẫn thật (`/Volumes/...`) thay vì đường dẫn symlink | Không làm hỏng gì, vì cả hai cùng trỏ một chỗ |
| Muốn quay lại | `rm ~/htdocs/typing-game && mv ~/htdocs/typing-game.pre-ssd ~/htdocs/typing-game` |

**Thời gian:** sao chép trước khoảng 15–30 phút. Đổi chỗ cộng kiểm tra khoảng 15–20 phút, cần lúc không agent nào chạy.
