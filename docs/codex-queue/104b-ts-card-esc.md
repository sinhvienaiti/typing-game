# Phiếu 104b · Tuyến Cuối · Esc ở thẻ ải quay về màn nạp súng

**Vì sao:** phiếu 104 làm xong 4/5 việc. Việc thứ năm dừng đúng luật, vì cần sửa `src/app/main.ts` mà phiếu không cho ghi. Hôm nay, ở thẻ ải (mode `intro`), Esc không làm gì; mọi phím khác vào trận. Người chơi lỡ vào thẻ ải thì không có đường lui về màn nạp súng để đổi súng. Kiểm kê map 1: TS-M1-18, cổng G5.

**Báo cáo:** `docs/codex-queue/104b-report.md`, và thư mục `docs/codex-queue/104b/`.

## Luật chung (phiếu mã)

- **cwd:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Mã:** worktree `games/.wt-ts-codex` (nhánh `ts-codex`, head `5b4c1b5`; đã có 090, 092, 104). Mọi đường dẫn tính từ worktree.
- Được dùng git chỉ đọc (`show`, `log`, `diff`, `status`). **Cấm** mọi lệnh git có ghi.
- **Cấm:**
  - sửa `src/kit/**`, `src/sim/**`, `src/content/**`;
  - sửa golden;
  - ghi vào cây chính hay worktree khác (nhất là `.wt-ts-vfx`, của làn VFX);
  - dev server, trình duyệt; media;
  - đụng Tu Tiên.
- Test trước, mã sau. Chú thích trong mã bằng tiếng Anh, ngắn.

**Chỉ được ghi:**
- `src/app/main.ts`: chỉ phần xử lý phím của mode `intro` (hàm `act()` khoảng dòng 457–459 và listener khoảng dòng 537–542), cộng một dòng import nếu cần;
- `src/app/journey.ts`, nếu cần một hàm thuần cho quyết định phím;
- test mới trong `tests/`;
- `docs/changelog/2026-10-29-card-esc.md` (mới, tiếng Việt);
- báo cáo và `docs/codex-queue/104b/`.

## Việc

1. Đọc cách các màn khác đang xử lý Esc (Cài đặt, Kho súng, Hành trình, nạp súng), rồi làm theo cùng cách.
2. **Ở thẻ ải mở từ màn nạp súng:** Esc quay về màn nạp súng của đúng ải đó, giữ bộ súng đã chọn và thứ tự của nó. Thẻ không vào trận, không mở âm thanh, không gõ chữ nào.
3. **Ở thẻ ải mở trực tiếp** (`?card=1` từ replay hay từ Hành trình, không qua màn nạp súng): Esc quay về màn mà người chơi vừa rời (Hành trình). Nếu không có màn đó (trang mở thẳng bằng URL) thì Esc không làm gì như hôm nay. Ghi rõ vào báo cáo cách phân biệt hai trường hợp.
4. Mọi phím khác ở thẻ ải giữ nguyên hành vi hôm nay.
5. Tách quyết định phím ra hàm thuần nhỏ, ví dụ `introKey(key, from): "back" | "enter" | "none"`, rồi test nó:
   - `Escape` từ nạp súng → `"back"`;
   - `Escape` khi mở thẳng → `"none"`;
   - chữ cái, `Enter`, `Space` → `"enter"`.

## Kiểm (bắt buộc, ghi số vào báo cáo)

1. `pnpm check` xanh; ghi số test trước và sau.
2. `node --import tsx scripts/chapter-hashes.ts` trước và sau: `diff` rỗng (152 dòng).
3. **Đột biến:** cho Esc luôn trả `"enter"` thì test phải đỏ; trả lại thì xanh.
4. `git -C games/.wt-ts-codex diff --stat` và `git -C games/.wt-ts-codex status --short -uall`: chỉ các file trong "Chỉ được ghi".

**Xong khi:** bốn mục đạt. Sau đó Claude kiểm bằng `survival-s1-loadout` ở 1280 và 1920: thẻ ải → Esc → nạp súng, đúng ải, đúng bộ súng, chọn tiếp rồi vào trận không gõ nhầm.
