# Phiếu 188 · Ba game và kit · Kiểm giấy phép mọi thư viện mã, điền sổ THIRD_PARTY

**Vì sao:** chủ dự án 29/10 sẽ đưa các game lên site công khai và yêu cầu mọi thứ dùng phải miễn phí, không vi phạm bản quyền (`docs/games/SHARED_SYSTEMS_BAR.md` §5). Sổ `docs/games/THIRD_PARTY.md` mới có vài dòng. Chủ dự án 29/10: giao thêm việc cho Codex.

**Báo cáo:** `docs/codex-queue/188-report.md`, thư mục `docs/codex-queue/188/`.

## Luật chung

- **cwd:** repo cha. Chỉ đọc mã; **chỉ được ghi** `docs/games/THIRD_PARTY.md` (thêm dòng, giữ mọi dòng cũ), báo cáo và `docs/codex-queue/188/`.
- Được dùng git chỉ đọc. Cấm git có ghi, cấm cài hay gỡ gói, cấm sửa `package.json` hay lockfile, cấm Tu Tiên (`games/immortality-cultivation`).
- Có mạng để đọc trang giấy phép thì được; không tải gói về.

## Việc

1. Với `games/dragon-hold`, `games/typing-defense`, `games/typing-survival` và `shared/game-kit`: liệt kê **mọi gói chạy trong bản build** (dependencies, không tính devDependencies chỉ dùng lúc build, nhưng ghi riêng những gói build nhúng mã vào bundle) theo lockfile, kèm phiên bản thật.
2. Với mỗi gói: giấy phép đọc từ `node_modules/<gói>/package.json` và file LICENSE trong `node_modules` (nguồn trên máy là đủ); nếu thiếu hay mơ hồ thì đọc repo gốc trên mạng. Ghi: tên, phiên bản, giấy phép, có cần ghi công trong trang Credits không, game nào dùng.
3. Gắn cờ mọi gói có giấy phép ngoài danh sách được dùng (MIT, BSD, ISC, Apache-2.0, MPL-2.0, CC0, CC-BY): GPL, AGPL, LGPL, không có giấy phép, giấy phép tùy chỉnh. Không sửa gì; chỉ báo.
4. Điền các dòng vào `docs/games/THIRD_PARTY.md` (bảng có sẵn), nhóm theo game.
5. Viết `188/credits-<game>.md`: đoạn ghi công cần có cho trang Credits của từng game (nếu giấy phép yêu cầu giữ thông báo bản quyền, chép đúng thông báo).

## Kiểm

1. Số gói mỗi game, số gói theo từng loại giấy phép, danh sách gói bị gắn cờ.
2. `git status --short -uall`: chỉ file được ghi.

**Xong khi:** đủ năm mục việc, có số. Claude duyệt rồi commit.
