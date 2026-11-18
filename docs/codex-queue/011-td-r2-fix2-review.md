# Phiếu 011 · Lời Gọi (typing-defense) · phản biện độc lập lượt sửa 2 của 1B R2

**Bối cảnh:**
- Lượt sửa 2 của 1B R2 đã commit và push trên `main` của repo `games/typing-defense`, từ `c9a8edd` tới `266e39d`.
- Bước phản biện độc lập của lượt này chưa chạy, vì Claude bị giới hạn phiên.
- Phiếu này giao bước đó cho Codex. **Chỉ đọc, đo và viết báo cáo. Không sửa mã.**

**Thư mục làm việc:** `D:\typing-game\games\typing-defense`. Chỉ được ghi vào `tmp/dell-2026-10-25/review3/`: báo cáo, log, script, ảnh chụp. Thư mục `tmp/` không vào Git.

Không sửa file nào khác. Không chạy git commit, push, reset, checkout, stash, clean. Được chạy `git log`, `git show`, `git diff`.

## Cách chạy lệnh (máy Dell)

- git, node 24.11, pnpm 11 **chỉ có trong WSL**.
  1. Viết script `.sh` vào `tmp/dell-2026-10-25/review3/`.
  2. Chạy: `wsl -e bash /mnt/d/typing-game/games/typing-defense/tmp/dell-2026-10-25/review3/<x>.sh`.
- Đầu mỗi script:
  - `source /mnt/d/typing-game/scripts/local-env.sh`, để nạp nvm, Chrome và PATH;
  - `cd` vào repo game.
- **Việc nặng** (test, build, balance) bọc trong `flock /tmp/tg-heavy.lock …`, đặt `VITEST_MAX_THREADS=4`, `--threads=4`. Máy chỉ có 7 GB RAM cho WSL và có thể đang chạy việc khác.
- `git -c core.filemode=false --no-optional-locks …`: bỏ nhiễu quyền file khi ổ `D:` gắn vào WSL.
- Vite trong WSL không thấy file sửa từ Windows, nhưng phiếu này không sửa mã nên không ảnh hưởng.

## Nguồn

- `AGENTS.md` của repo game: bố cục, lệnh, luật.
- `docs/changelog/2026-10-25-td-1b-r2-fix2.md`: những gì lượt sửa 2 khẳng định đã làm.
- `docs/td/BUILD_NOTES.md` §7.5: số đo.
- `docs/td/BUILD_1B.md` §6.5, §17, §18, §20.
- Bằng chứng của lượt sửa 2: `tmp/dell-2026-10-25/r2fix2/`. Bằng chứng của phản biện lần 2: `tmp/dell-2026-10-25/review2/`.
- Luật cân bằng chung: `../../docs/games/BALANCE.md` §3, §9.2.
  - Không bao giờ chấm cổng chung chỉ bằng dải riêng của game.
  - In cả kết quả theo dải chung.

## Việc

1. **Đọc diff `c9a8edd^..266e39d`.**
   - Với mỗi khẳng định trong changelog sửa 2, ghi: đúng, sai, hay chưa chứng minh. Kèm `file:dòng` hoặc log làm bằng chứng.
   - Soi kỹ:
     - `src/app/chunks.ts` và các chỗ gọi trong `main.ts`: thử lại 3 lần, đường dự phòng, hỏi lại sau 15 s. Tìm rò timer, gọi trùng, trạng thái kẹt khi chunk tải được ở lần thử lại muộn.
     - `scripts/bundle-budget.mjs`: đọc manifest có đúng phần khởi động của "/" không; trang khác có bị bỏ sót không.
     - Phần chấm G3, G8 trong báo cáo `td:balance`: theo từng bộ và gộp; ngưỡng đúng §18.
     - `td-1b-perf` nhịp 60 Hz (`PERF_HZ`), và kịch bản `td-1b-chunks`.
     - Tài liệu `BUILD_1B` §17, §18, §20 có khớp mã không.
2. **Chạy lại để kiểm số:**
   - `pnpm check`;
   - `pnpm td:golden:check`.
   - So số test (292), kích cỡ gói "/" (82,56 kB gzip) và mã băm file vàng với changelog.
3. **Chạy một lượt cân bằng nhanh** để kiểm báo cáo in đúng dòng G3, G8 và bảng gộp. Lượt đầy đủ mất khoảng 15 phút; chỉ chạy khi máy rảnh.
   - Lệnh: `pnpm td:balance --modes=balanced --bots=standard,sloppy --stage-seeds=40 --threads=4` (`sloppy` là bot Ẩu).
   - Không cần khớp số đầy đủ; chỉ kiểm cách chấm và cách in.
4. **Kịch bản trình duyệt** bằng Chrome trong WSL, theo `AGENTS.md` (Vite cổng 3046 `--strictPort`; tắt Vite và Chrome khi xong):
   - `td-1b-chunks` ở 1280 × 720;
   - `td-theme` ở 1280 × 720.
   - Xem ảnh chụp trước khi khẳng định điều gì về hình.
   - **Không đo hiệu năng:** Chrome trong WSL chỉ vẽ bằng phần mềm. Ghi rõ là chưa kiểm.
5. **Viết báo cáo** `tmp/dell-2026-10-25/review3/REPORT.md` bằng tiếng Việt:
   - kết luận chung: đạt / đạt có điều kiện / chưa đạt;
   - danh sách phát hiện, lớn trước, mỗi phát hiện gồm:
     - mức (lớn / nhỏ);
     - `file:dòng`;
     - tình huống hỏng cụ thể;
     - bằng chứng;
     - cách sửa đề xuất;
   - bảng đối chiếu từng khẳng định của changelog;
   - các mục "đề xuất của vòng này, chờ chủ dự án xác nhận": có đúng là quyết định của chủ dự án không, hay nên tự quyết theo đề xuất;
   - những gì chưa kiểm được và vì sao.

**Xong khi:** `REPORT.md` có đủ các phần trên; mọi tiến trình Vite và Chrome đã tắt; không file nào ngoài `review3/` bị sửa (`git status` sạch như lúc đầu).
