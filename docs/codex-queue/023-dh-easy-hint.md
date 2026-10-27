# Phiếu 023 · Rồng Giữ Ải · Thẻ tốc độ gợi ý mức Dễ cho người mới tập (chỉ mã, không trình duyệt)

**Bối cảnh:** chủ dự án chốt ngày 27/10 (canon `docs/games/dragon-lane/00-canon.md` D33 mục 6). Ở đợt 1–2, người mới tập 15 WPM thua gần nửa số lượt ở mức mặc định. Thẻ tốc độ hiện trước ải lại không gợi ý mức Dễ (phát hiện 15, `games/dragon-hold/docs/changelog/2026-10-27-test-pass.md`). Đã có sẵn: thua 2 lần liền thì màn thua mời chơi lại mức Dễ (00 §4.10: gợi ý, không ép). Chưa làm Lều Chuẩn Bị ở M0.

Sandbox của Codex **không mở được cổng**, nên phiếu này **không có bước trình duyệt**. Claude chạy trình duyệt sau khi đọc diff.

**Thư mục làm việc: `games/.wt-dh-codex`** (worktree của Rồng Giữ Ải, nhánh `codex-023-easy-hint`, tách từ `main` 83da970). Mọi lệnh dưới đây chạy ở đó. **Không đụng `games/dragon-hold`**: làn luật và cân bằng của Claude đang sửa cây đó.

**Cấm:**
- lệnh git có ghi (chỉ được `status`, `diff`, `log`, `show`); Claude commit;
- sửa `src/sim/**`, `src/content/**`, golden, `src/kit/**`;
- đụng media, game khác, Tu Tiên;
- mở dev server hay Chrome.

## Việc

1. **Luật gợi ý, hàm thuần.** Trong `src/app/typing-pace.ts`:
   - thêm hằng `EASY_HINT_WPM = 20`, chú thích một dòng trỏ 00 D33 (6);
   - thêm hàm thuần `offerEasy(wpm: number, difficulty: Difficulty, fromMenu: boolean): boolean`, trả đúng khi `wpm <= EASY_HINT_WPM`, `difficulty === "normal"` và thẻ không mở từ menu tạm dừng.
2. **Thẻ tốc độ** (`src/app/pace-card.ts`):
   - `open(...)` nhận thêm tham số cuối, tùy chọn: `easy?: (wpm: number) => boolean`. Có tham số này và hàng đang chọn có `header.typistWpm` mà hàm trả đúng thì `noteNode` hiện dòng: "Mới tập gõ: nên chơi mức Dễ, quái thưa và chậm hơn. ⇧↵ chọn tốc độ này và chơi mức Dễ." Kèm một nút nhỏ "Chơi mức Dễ" (dùng `uiButton` như các nút khác).
   - Dòng gợi ý cập nhật mỗi lần đổi hàng (↑ ↓, phím số, rê chuột nếu thẻ đang đổi hàng theo chuột). Hàng trên 20 WPM thì ẩn dòng gợi ý và giữ `note` cũ nếu có.
   - `onPick` nhận thêm tham số thứ hai, tùy chọn: `{ easy: boolean }`.
     - Enter, bấm phím số, bấm chuột vào hàng: chọn như cũ với `easy: false`.
     - `handleAction("call-early")` (⇧↵, `src/content/rules.ts` KEYS) và nút "Chơi mức Dễ": chọn hàng đang chọn với `easy: true`, chỉ khi dòng gợi ý đang hiện. Không hiện thì `call-early` trả `false` như cũ.
3. **App** (`src/app/app.ts`):
   - `askPace` chuyển tham số `easy` cho thẻ chỉ khi mở trước ải (không có `back`), bằng `offerEasy(wpm, difficulty, false)`.
   - Ở chỗ gọi `askPace` trước ải (khoảng dòng 902): `easy: true` thì đặt `difficulty = "easy"` trước khi dựng trận.
   - Hai chỗ khác không đổi hành vi: menu tạm dừng (dòng 393) và màn thua với lời mời "⇧↵ Thua 2 lần: chơi lại mức Dễ".
   - `?difficulty=` trên đường dẫn vẫn thắng: đã có `difficulty` khác `normal` thì không gợi ý.
4. **Test** (vitest, `tests/app/typing-pace.test.ts` hoặc file mới cạnh đó):
   - `offerEasy` ở 15, 20, 25 WPM; với `normal`, `easy`, `hard`; với `fromMenu` đúng và sai.
   - Nếu môi trường test có DOM (xem các test `tests/ui/*` dựng DOM thế nào): mở thẻ với `easy`, chọn hàng 15 WPM. Dòng gợi ý phải hiện; `call-early` gọi `onPick` với `easy: true`; Enter gọi với `easy: false`; hàng 35 WPM thì dòng ẩn và `call-early` trả `false`.
5. **Changelog** mới: `docs/changelog/2026-10-27-easy-hint.md`, tiếng Việt có dấu, theo kiểu các file cạnh đó. Ghi: việc gì, vì sao (D33 mục 6, phát hiện 15), file nào, kết quả kiểm.

## Kiểm (bắt buộc)

1. `../../.local/bin/heavy.sh pnpm check`, chạy trong `games/.wt-dh-codex`. Ghi số test; tsc và build phải xanh.
2. Golden: lệnh golden trong `package.json` (hoặc `pnpm exec tsx scripts/balance/golden.ts`), cũng dưới `heavy.sh`. Mọi ca giữ nguyên mã băm: phiếu này không đổi sim.
3. `git -C games/.wt-dh-codex diff --stat` và `git -C games/.wt-dh-codex diff` đầy đủ, dán vào báo cáo.

## Báo cáo `docs/codex-queue/023-report.md` (repo cha)

Bảng `| # | Việc | File:dòng | Kiểm (lệnh, kết quả) | Còn cần Claude kiểm trên trình duyệt |`. Cột cuối ghi rõ cho Claude, ở 1280×720 và 1920×1080, mở trang không có `?wpm` và đã xóa `localStorage`:
- chọn hàng 15, rồi 20: dòng gợi ý và nút hiện, không tràn thẻ;
- chọn hàng 25: dòng ẩn;
- ⇧↵ ở hàng 15: trận chạy ở mức Dễ (`__dh` hay HUD cho thấy mức);
- Enter ở hàng 15: mức Thường;
- mở thẻ từ menu tạm dừng: không có dòng gợi ý.

**Xong khi:** 5 việc có kết quả; `pnpm check` và golden đạt trên cây cuối.
