# Phiếu 004 · Đưa Tu Tiên Thủ Ải (`immortality-cultivation`) vào portal, nginx và script Play

**Mục tiêu:** game thứ 9 hiện trên menu portal và mở được ở Play mode và dev mode, đúng cách các game trước đã làm. Mẫu là commit `039842a9` ("three new games on the portal menu…") và mọi chỗ đang nhắc `typing-survival`.

**Thông số:**

| Mục | Giá trị |
|---|---|
| id | `immortality-cultivation` |
| Thư mục | `games/immortality-cultivation` (submodule, hiện mới có README; mã khung đến ở M0a) |
| Cổng dev | **3008** (strict) |
| Host | `tutien.typing-game.local` |
| Tên menu | `Tu Tiên Thủ Ải` |
| Nhóm | `battle` |
| Icon | 🗡️ |
| Mô tả (tiếng Việt, một câu, kiểu các game khác) | "Tu sĩ giữ ải trước thú triều: gõ khẩu quyết tiếng Anh để xuất chiêu, lập trận, đột phá cảnh giới." |

**Thư mục làm việc:** gốc repo `D:\typing-game`.

## File phải sửa

Thêm `immortality-cultivation` vào mọi nơi `typing-survival` đang có mặt, theo đúng kiểu đó:
- `portal/public/games.json`
- `portal/tests/learning-bridge.test.mjs` (gameId mới trong danh sách được phép, nếu file có danh sách)
- `infra/nginx/typing-game.local.dev.conf` (proxy tới 127.0.0.1:3008)
- `infra/nginx/typing-game.local.play.conf` (phục vụ `games/immortality-cultivation/dist`)
- `scripts/setup-nginx.sh` (`HOSTS`)
- `dev.sh`, `play.sh` (`build_if_needed` có kiểm thư mục)
- `scripts/game-dir.sh`, `scripts/bootstrap.sh` (`require_new_game`/`update_new_game` với nhãn "Tu Tiên Thủ Ải"; tên target ngắn `tutien`)
- `scripts/play.sh`, `scripts/validate-play-mode.mjs`
- `package.json` (các lệnh `dev:*`, `build:*` kiểu `build:survival`; tên `build:tutien`)
- `media/media.config.json` (mục game mới, kiểu `typing-survival`)
- `AGENTS.md` (thêm hàng vào bảng "Skills by game"; nguồn thiết kế `docs/games/tu-tien`)
- `docs/AGENT_SKILLS_SETUP.md`
- `.github/workflows/ci.yml` (chỉ khi `typing-survival` có trong đó)
- `scripts/validate-space-integration.mjs` (chỉ khi danh sách game ở đó cần game mới)

## Luật

- Game chưa có `package.json`, nên script phải **bỏ qua** game này như đang bỏ qua game chưa checkout ("not checked out yet; skipped"), không được báo lỗi.
- Giữ định dạng, thứ tự và chú thích của từng file. Không đổi gì của các game khác.
- Không chạy git. Không sửa file ngoài danh sách. Không động vào `games/**`.
- Không cài gì.
- Chạy được thì kiểm cú pháp:
  - `node --check` cho file `.mjs`;
  - `powershell` không dùng được cho `bash`: bỏ qua, Claude sẽ chạy `bash -n` và test trong WSL.

**Xong khi:** mọi file trên có mục mới; báo cáo liệt kê từng file đã sửa và đoạn thêm vào; ghi rõ chỗ nào chưa chắc.
