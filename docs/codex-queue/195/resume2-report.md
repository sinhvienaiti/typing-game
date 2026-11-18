# Phiếu 195 · Dragonhold · Dừng ở điều kiện đầu

Chưa hoàn tất phiếu. Phiên này dừng trước khi sửa mã, theo yêu cầu: “Chỉ được có file của 187 hay 194 mà Claude chưa commit. … Có file lạ thì dừng.”

## Trạng thái đã xác minh

- Worktree đúng `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD `6aa593a2dce6637cccbe24a58709b86f7127f607`. Có [báo cáo 194](194-report.md).
- Đã có bằng chứng của một lượt 195 trước đó trong `195/`, nhưng chưa có báo cáo 195. Không xác nhận được tác giả hoặc quyền tiếp tục phần mã đang dở chỉ từ các file này.
- Đã lưu trạng thái của phiên này tại [start-status.txt](195/start-status.txt) và [parent-status-before.txt](195/parent-status-before.txt). Hai bản có sẵn được giữ nguyên nội dung tại [previous-start-status.txt](195/previous-start-status.txt) và [previous-parent-status-before.txt](195/previous-parent-status-before.txt). Các log và snapshot cũ khác được giữ nguyên.

## File ngoài trạng thái 187/194

Đối chiếu trạng thái hiện tại với `195/start-files.json` có sẵn (snapshot khi chỉ có 187/194):

| Nhóm | Đường dẫn trong worktree |
| --- | --- |
| File đã có nhưng nội dung khác snapshot | `src/app/app.ts` |
| File đã có nhưng nội dung khác snapshot | `src/app/learning.ts` |
| File không có trong snapshot | `src/app/app.css` |
| File không có trong snapshot | `src/app/deck-boot.ts` |
| File không có trong snapshot | `src/app/idle-speed.ts` |
| File không có trong snapshot | `src/app/quality.ts` |
| File không có trong snapshot | `tests/app/deck-boot.test.ts` |
| File không có trong snapshot | `tests/app/idle-estimate.test.ts` |
| File không có trong snapshot | `tests/app/idle-speed.test.ts` |
| File không có trong snapshot | `tests/app/pinned-deck.test.ts` |
| File không có trong snapshot | `tests/app/quality.test.ts` |

Các file này có nội dung tương ứng việc đang dở của 195, nhưng nằm ngoài hai phiếu được phép có ở điều kiện đầu. Không sửa, xóa hoặc hoàn tác chúng. Các file còn lại của 187/194 trong snapshot được giữ nguyên. Danh sách đầy đủ nằm trong trạng thái đã lưu.

## Phiên này đã làm và chưa làm

Chỉ đọc Git, báo cáo 187/194, snapshot cũ và hai file mã có sẵn để xác minh điều kiện đầu. Chỉ ghi báo cáo này và các file trạng thái/backup nêu trên. Không sửa dòng nào trong `app.ts`, mã game, test, script, changelog hoặc `06-other-systems.md`.

Chưa thực hiện hoặc xác nhận lại 11 mục việc và 7 mục kiểm. Không chạy `pnpm check`, golden, bot, balance, deploy:pack, English UI hoặc script ước tính; vì vậy không có số test trước/sau, G1/G3/G5/G6/G8 hay phần trăm mới được xác nhận trong phiên này. Các log có sẵn không được coi là kết quả của phiên này. Không chạy server, trình duyệt, mạng hoặc Git ghi. Không chạm worktree khác, kit, Tu Tiên hay media.

## Chủ dự án và Claude cần xem

Xác định phần mã 195 đang dở có được phép tiếp tục hay không, hoặc bàn giao lại worktree chỉ có phần 187/194 như điều kiện đề bài. Phiên này chưa đủ điều kiện để gửi duyệt hoàn tất. Kiểm trình duyệt vẫn thuộc Claude theo phiếu.
