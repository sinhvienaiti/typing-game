# Phiếu 329 · Panel lab gọn

- Đã sửa `games/.wt-ic-lab-panel/src/lab/skills-main.ts` trên nhánh `codex/lab-compact-panel`: thêm 63 dòng, bỏ 11 dòng.
- Panel mở rộng **240 px**, cuộn dọc theo chiều cao màn hình; các nút dùng tên ngắn tiếng Anh và giữ câu đầy đủ trong tooltip. Giữ nguyên mô tả của thanh chiêu.
- H hoặc bấm `Lab panel · H` để thu gọn/mở lại; lưu trạng thái tại `lab.panel.collapsed`, cập nhật vùng tránh của thanh chiêu.
- `npx tsc --noEmit`: PASS.
- `npx vitest run tests/lab tests/view --maxWorkers=4`: PASS, **45 file / 530 test**, 3,61 giây. Có cảnh báo fixture `fire-impact-k1-r2` chưa tải; các test liên quan vẫn qua.
- `git diff --check`: sạch. `git diff --stat` trong worktree chỉ có `src/lab/skills-main.ts`; hai liên kết chưa theo dõi `art-src`, `node_modules` có sẵn từ đầu.
- Không mở trình duyệt/cổng mạng, không chạy build hoặc suite khác theo phạm vi phiếu. Claude cần kiểm trực quan panel, tooltip, phím H và thanh chiêu sau khi thu gọn/mở lại.
