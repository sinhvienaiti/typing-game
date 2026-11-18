# Chạy lại bằng chứng phiếu 224

Chạy từ `/Users/toandx/htdocs/typing-game`. Worktree chỉ đọc, không chạy pnpm/node với cwd worktree. Không install, không mạng/server/browser. Script chỉ ghi dưới hai đường của phiếu; log cũ được ghi đè nếu cố ý chạy lại, nên giữ báo cáo cũ trước khi tái lập. Chỉ tiếp tục khi preflight đúng nhánh, HEAD, status và mọi đầu vào; nếu trạng thái đã đổi sau Claude sửa/commit thì dừng, không dùng script để ép về mốc cũ.

```sh
python3 -B docs/codex-queue/224/preflight.py
python3 -B docs/codex-queue/224/run.py copy
python3 -B docs/codex-queue/224/run.py split
python3 -B docs/codex-queue/224/run.py builds
python3 -B docs/codex-queue/224/audit.py
python3 -B docs/codex-queue/224/mutate.py
python3 -B docs/codex-queue/224/finish.py
```

Các bước tuần tự, chờ lệnh trước kết thúc. Preflight lần đầu được chạy trong bộ nhớ trước mọi ghi và lưu nguyên stdout trong `preflight.txt`; `preflight.py` là bản chạy lại cùng các điều kiện. Khi bắt đầu lại một phiên mới được chủ dự án giao, chụp status repo cha trước ghi vào `parent-before.txt`; không lấy status cuối phiên cũ làm mốc đầu mới.

`copy` chụp `before.json` trước khi chép, tạo marker, dùng Git ls-files + rsync và chép thêm toàn public. Nó từ chối nếu thư mục tạm đã có. `split` chỉ dùng patch hệ thống. `builds` chạy nền 170 rồi cuối 208, mỗi pnpm đều có biến tắt tự install và TMPDIR trong bản chép, env portal được ghi ở từng `*-run.json`. JSON checker là stdout thuần; log build có cả stdout/stderr.

`audit` đối chiếu kit bằng Git show và import generator không gọi main; tạo fixture prune và probe Vite thật trong `tree/tmp`, dọn bằng finally. `probe.mts` được chép vào `tree/tmp/audit-probe.mts` rồi chạy bằng `node --import tsx`; không chạy bản nằm trong thư mục bằng chứng trực tiếp vì import tương đối của nó trỏ về game. Khi đã có `tree/tmp` từ test, audit dùng thư mục đó; không sinh ảnh.

`mutate` có M1–M4 bắt buộc và M5–M6 bổ sung, sửa từng file rồi trả byte gốc và chạy lại cùng test, ghi dần `mutations.json`. Nếu script bị ngắt giữa lượt, chỉ trả file tương ứng trong bản chép từ worktree; không sửa worktree. Sau đó chạy lại kiểm hash và bước bị ngắt.

`finish` lưu nguồn/diff/chunks/số test, đối chiếu 329 hash và mtime node_modules, chạy find trước dọn, rồi mới `rm -rf` đúng thư mục 224, chụp phạm vi và dựng báo cáo. Nó assert nguyên worktree trước khi xóa. Không chạy lại finish mặc định sau khi đã dọn, vì bản chép không còn. `python3 -B docs/codex-queue/224/finish.py --report-only` chỉ dựng lại báo cáo/phạm vi từ bằng chứng đã lưu và kiểm các liên kết/JSON/script; không chạy build/test hoặc dọn. Các thời gian trong log/run.json là số đo gốc; khi tái chạy phải dùng số mới thay cho các số thời gian được trình bày trong báo cáo.

`vite-probes-attempt1.*` ghi lần tsx CLI bị EPERM ở IPC pipe. `kit-generator-attempt1.*` ghi lỗi script đo thiếu biến template, đã sửa. `vite-probes-prior.*` là lượt probe trước đột biến, kết quả quyết định là `vite-probes.json` được đo tuần tự sau khi hoàn tất đột biến và trả nguồn. Đây là lỗi/lượt của công cụ đo, không phải lỗi game.

`requirements.md`, `findings.json` là phần đánh giá bằng đọc mã; `finish.py` chép hai bảng đó cùng `claims.json` vào báo cáo. Đọc lại đánh giá nếu mã đổi; chạy xanh không tự đóng phát hiện.
