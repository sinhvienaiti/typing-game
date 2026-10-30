# Phiếu 193 · Wordwoven · Nút Settings, nút loa và bộ tiếng phím Firefly trong trận

**Nguồn và việc:** như phiếu 192 (`docs/codex-queue/192-dh-keys-and-panels.md`), áp cho Wordwoven. Đọc kỹ 192 trước, rồi làm mọi mục của nó với những khác biệt dưới đây.

**Báo cáo:** `docs/codex-queue/193-report.md`, thư mục `docs/codex-queue/193/`.

**Chỉ chạy khi** Claude đã:
- duyệt 189 và 190;
- thêm module `ui`, `feedback`, `audio` vào `kit.config.json` của Wordwoven;
- tạo worktree dưới đây và đồng bộ kit mới vào đó.

Chưa có thì dừng, ghi vào báo cáo.

> **Chạy lại 30/10 sáng (điều phối):** lượt đầu của chính phiếu này (29/10 khoảng 23:35) bị cắt giữa chừng vì hết hạn mức, nên worktree **không sạch**: các thay đổi chưa commit trong đó là việc dở của chính phiếu này, không phải của ai khác. Đừng dừng ở bước "git status phải sạch". Đọc `git status` và `git diff`, giữ phần đúng, làm tiếp cho đủ phiếu, rồi kiểm như thường. Báo cáo lượt trước (chỉ ghi "dừng vì worktree không sạch") nằm ở thư mục `docs/codex-queue/` của worktree; ghi đè bằng báo cáo mới.

## Khác với 192

- **Nơi làm:** worktree `games/.wt-td-keys`, nhánh `td-keys`, cắt từ `a2-days` (nhánh chính hiện tại của Wordwoven). `git status` phải sạch.
- **Media:** `public/assets/typing-defense/audio/keys/`.
- **Âm hiện có:** Wordwoven có thể chưa có kênh nhạc hay giọng đọc. Hàng nào không có kênh thật thì ẩn, ghi lại; không thêm thanh trượt không làm gì.
- **Mục riêng của game** trong bảng Settings: chỉ thêm khi game đã có thật (ví dụ tốc độ game, gợi ý).
- **Tiếng gõ:** phát ở ô gõ của thẻ gọi (C10) và mọi chỗ người chơi gõ chữ.

## Cấm và kiểm

- Như 192.
- Changelog: `docs/changelog/<ngày>-settings-and-keyboard-sounds.md` của Wordwoven.
