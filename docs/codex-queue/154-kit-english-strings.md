# Phiếu 154 · Kit · Chữ người chơi thấy trong kit chung sang tiếng Anh

**Vì sao:** chủ dự án 28/10 tối: ba game là game tiếng Anh, mọi chữ người chơi đọc là tiếng Anh, tiếng Việt chỉ ở nghĩa của từ đang học (`AGENTS.md`, mục "Language, names and art level"). Lượt duyệt phiếu 130 và 131 thấy kit chung vẫn mang chữ Việt mà người chơi thấy:
- `HOÀN HẢO` trong nhãn số của `SHIP.numbers.label` (`feedback/profiles.ts`);
- lời khuyên tốc độ gõ `ADVICE_VI` (`balance/pace.ts`);
- chữ Việt trong `balance/typist.ts`, `balance/gates.ts` (báo cáo dev).

Hiện Last Line và Dragonhold tự đè bằng bản tiếng Anh trong game. Phiếu này sửa tại nguồn, để Claude bỏ phần đè khi đồng bộ kit sau.

**Báo cáo:** `docs/codex-queue/154-report.md`, thư mục `docs/codex-queue/154/`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`, thư mục `shared/game-kit/`.
- Được dùng git chỉ đọc. **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa bản chép kit trong game (`games/*/src/kit/**`, `games/.wt-*/src/kit/**`);
  - chạy `kit:sync` hay `scripts/sync-game-kit.mjs`;
  - dev server, trình duyệt, mạng;
  - đụng Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*`).
- Test trước, mã sau. Chú thích tiếng Anh, ngắn.

**Chỉ được ghi:** `shared/game-kit/**/*.ts` (trừ `node_modules`), `shared/game-kit/DRIFT.md` (thêm một mục, giữ mọi mục cũ), báo cáo và `docs/codex-queue/154/`.

## Việc

1. **Kiểm kê:** liệt kê mọi literal chuỗi có chữ Việt (có dấu, và cả không dấu như "trong", "sau", "Thiếu") trong `shared/game-kit/**/*.ts`, trừ test và chú thích. Ghi bảng `154/strings-before.md`: file, dòng, chuỗi, ai thấy (người chơi, báo cáo dev, nghĩa từ).
2. **Đổi:**
   - chuỗi người chơi thấy và chuỗi báo cáo dev: sang tiếng Anh, ngắn, giọng game thương mại. Theo `docs/games/NAMES_EN.md` cho danh từ game;
   - `HOÀN HẢO` → `PERFECT`;
   - `ADVICE_VI` → thêm `ADVICE_EN` làm mặc định; giữ `ADVICE_VI` như alias cũ, đánh dấu `@deprecated`, để game chưa đồng bộ vẫn build được;
   - **giữ nguyên:** nghĩa từ (`vi`, `meaningVi` và các trường cùng loại), id, khóa lưu, tên sự kiện, số.
   - Số kiểu Mỹ: dấu thập phân là dấu chấm, phần trăm viết liền (`95%`).
3. **Test:**
   - thêm `shared/game-kit/english-strings.test.ts`: quét literal chuỗi trong kit, đỏ khi gặp chữ Việt ngoài danh sách được phép (chú thích, trường nghĩa từ, test);
   - cập nhật test cũ so chữ Việt;
   - đột biến: thêm tạm `"Bắt đầu"` vào một file kit thì test mới đỏ; trả lại thì xanh.
4. **DRIFT.md:** một mục ngắn: kit nay mặc định tiếng Anh; các game đang đè (Last Line `src/app/english.ts`, Dragonhold `src/view/fx.ts` `NUMBER_FEEL`) bỏ phần đè ở lần đồng bộ tới.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. Test của kit xanh, ghi số file và số ca, trước và sau.
2. `npx tsc --noEmit -p shared/game-kit` (hoặc lệnh kiểm kiểu của kit trong `package.json`) đạt.
3. Đột biến ở mục 3: đỏ rồi xanh, ghi log.
4. Bảng `154/strings.md`: trước → sau, cho mọi chuỗi đã đổi.
5. `git status --short -uall -- shared/game-kit`: chỉ file trong "Chỉ được ghi".

**Xong khi:** năm mục đạt. Claude duyệt chữ, rồi đồng bộ kit vào ba game và bỏ phần đè.
