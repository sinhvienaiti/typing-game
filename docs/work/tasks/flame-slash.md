# Bỏ lửa gai nhọn ở nhát chém kết phím 7 (Hỏa)

**Mục tiêu:** bỏ hàng lưỡi lửa tam giác do mã vẽ trong `games/immortality-cultivation/src/view/skills/flame-slash.ts`, thay bằng dải lửa Firefly anh đã chọn.
**Cách đã chốt:** dải `art-src/lab/vfx/aura/strips/strip-fire-sheath.rgba.png` cuộn dọc nhát chém, đi qua cùng ramp và nhịp xói. Đường cũ chỉ còn sau cờ `?slash=tongues`. (DECISIONS: 04/11 23:50)
**Nghiệm thu:** không còn răng cưa; hệ Kim trùng 100 % khi so ảnh; các khung không có nhát chém của hệ Hỏa trùng 100 %; video trước/sau cho anh.
**Phiếu:** `docs/codex-queue/275-tt-flame-slash-strip.md` · worktree `games/.wt-ic-flame-slash`.

## Nhật ký
- 04/11 23:50 · anh · chê lửa gai nhọn (ảnh từ video âm 269).
- 04/11 23:56 · Claude · viết phiếu 275, tạo worktree.
- 05/11 00:20 · Claude · bỏ khâu phản biện (luật làm gọn); 275 READY, chạy sau 274b.
- 05/11 02:15 · Claude · Codex 275 xong (01:05), chưa commit, ở worktree `games/.wt-ic-flame-slash`. **Việc kế (agent kiểm):**
  - làm đúng mục "Claude làm sau" của `docs/codex-queue/275-*.md`, theo `docs/codex-queue/275-report.md`;
  - dựng dev server riêng cho worktree: wrapper Vite có `server.fs.allow` là gốc repo, link `art-src` từ game chính (không commit link), cổng 3068;
  - quay video trước/sau nhát chém kết phím 7 Hỏa ở camera chơi, so mặc định với `?slash=tongues`; kiểm Kim trùng khít;
  - đạt thì commit trong worktree (chỉ các tệp phiếu cho ghi), báo Claude để gộp;
  - ghi nhật ký ở đây. Video vào `typing-game-review/owner-review/2026-11-05/tu-tien/flame-slash/` kèm `ABOUT.md`.
- 05/11 02:32 · agent kiểm · **ĐẠT** theo mục nghiệm thu. tsc đạt, Vitest 979/979. Lab của worktree (cổng 3068) so với bản xuất `git archive 5de0d22` (cổng 3069), camera chơi, 60 Hz cố định:
  - không còn răng cưa: dải lửa liền, cuộn dọc nhát chém;
  - hệ Kim: 28/28 khung trùng tuyệt đối (nền giữa và nền sáng);
  - hệ Hỏa 1080p, nền sáng và tối: 71/148 khung trùng tuyệt đối; chỉ khung 196–272 khác, đúng đời nhát chém;
  - `?slash=tongues` so với bản gốc: 19–20 khung trong nhát chém lệch ≤ 1/255 ở khoảng 1 điểm ảnh (làm tròn khi biên dịch lại shader), ngoài ra trùng.
  - Video: `typing-game-review/owner-review/2026-11-05/tu-tien/flame-slash/flame-slash-before-after.mp4` (25,9 giây, 26,6 MB, kèm ảnh tĩnh và `ABOUT.md`). Số liệu: `captures/tu-tien/flame-slash/parity.json`.
  - Commit `f3e7029` trên `codex/flame-slash-strip` (5 tệp của phiếu). Chưa gộp, chưa push. Đã xóa ảnh thô, link `art-src`/`public`, server, bản xuất tạm.
  - **Cho Claude xem (chưa chấm 8,5):** (1) lúc quét có một mép cắt dọc thẳng ở đầu chạy (khung khoảng 200–215, do `behind` là hàm bậc). Mép này có từ trước nhưng dải rộng làm nó lộ hơn. (2) Với `k = 3`, dải trông bị kéo dài gấp khoảng 1,5–2 lần so với tỉ lệ 2:1, nên lửa giống mảng dung nham hơn là lưỡi liếm. Ước từ khung hình: `k` khoảng 5 sẽ gần tỉ lệ 2:1 hơn.
  - **Việc kế (Claude):** gộp `f3e7029`, gửi video cho anh, quyết hai điểm trên.
- 05/11 08:53 · Claude · Codex 279 xong (08:38): `uStripK` tính theo tỉ lệ 2:1 (dự phòng 5, cờ `?stripK=`), mép đầu mềm và rách theo nhiễu. Chưa commit trong `games/.wt-ic-flame-slash` (HEAD `f3e7029`). **Việc kế (agent kiểm):**
  - quay lại video trước/sau như lần 02:32: trước là main `5de0d22`, sau là worktree; nhát chém kết phím 7 Hỏa, camera chơi, nền sáng và tối, kèm vài khung cận ở khoảng 200–260;
  - kiểm Kim trùng khít; xem dải hết kéo dài, đầu hết mép thẳng;
  - đạt thì commit các tệp của 279 (đọc `docs/codex-queue/279-report.md`);
  - dev server riêng cổng 3068, link `art-src`/`public` rồi gỡ;
  - video vào `typing-game-review/owner-review/2026-11-05/tu-tien/flame-slash/flame-slash-v2-before-after.mp4`.
- 05/11 08:55 · agent kiểm 279 · bắt đầu: tsc đạt, Vitest 985/985 (89 tệp). Ba server Vite riêng: worktree 3068, `git archive 5de0d22` 3069, `git archive f3e7029` 3070 (bản xuất trong scratchpad); link `art-src`/`public` tạm vào worktree.
- 05/11 09:12 · agent kiểm 279 · **ĐẠT** theo mục nghiệm thu. Camera chơi, 60 Hz cố định, 1080p và 720p, nền sáng/tối, worktree so với `git archive 5de0d22` (và `f3e7029` để so với 275):
  - hệ Kim: 148/148 khung trùng tuyệt đối, cả nền giữa và nền sáng;
  - hệ Hỏa: 71/148 khung trùng tuyệt đối trên mỗi nền; chỉ khung 196–272 khác, đúng đời nhát chém;
  - `?slash=tongues` so với bản gốc: 19/19 khung trùng (AE 0);
  - dải hết kéo dài: `uStripK` đo được 5,71 khi nhát chém ổn định (275 là 3), giống nhau ở 720p và 1080p; lửa thành các lưỡi liếm nhỏ, hết mảng dung nham;
  - đầu hết mép thẳng: khung 205–215 đầu dải tan mềm, rách theo nhiễu (`head-edge-v2-215.jpg`).
  - Video: `typing-game-review/owner-review/2026-11-05/tu-tien/flame-slash/flame-slash-v2-before-after.mp4` (31,1 giây, 27,9 MB; 2×2 sáng/tối, cận ×1,5, đoạn cận ba cột gốc/275/279, 720p) và hai ảnh tĩnh `close-frames-v2-205-260.jpg`, `head-edge-v2-215.jpg`. Số liệu: `captures/tu-tien/flame-slash/parity-v2.json`.
  - Commit `180db0b` trên `codex/flame-slash-strip` (5 tệp của phiếu 279). Chưa gộp, chưa push. Đã xóa ảnh thô (2.544 tệp), server, link `art-src`/`public`, bản xuất tạm; đã dựng lại INDEX.
  - **Cho Claude xem (chưa chấm 8,5):** (1) `uStripK` đổi theo khung lúc quét: khung 196 là 5 (dự phòng, metadata chưa về), 197 là 5,12, rồi tăng dần đến 5,71 ở khung 219 (+11 %). Đo theo phép chiếu từng khung nên vân dải trôi nhẹ trong lúc quét, nhanh hơn tốc độ cuộn 0,5 chu kỳ/giây; nếu thấy trôi thì chốt `k` khi nhát chém bắt đầu. (2) Ở cận ×1,5 khung 240–260, biên dải vẫn có các mảng đỏ sẫm răng nhỏ; phải chấm mù mới biết có đạt 8,5. (3) Đường nối chéo mờ trong dải cam phía trước đầu chạy có cả ở bản gốc, không do dải.
  - **Việc kế (Claude):** gửi video v2 cho anh, gộp `180db0b` khi anh duyệt.
- 05/11 09:22 · Claude · Anh duyệt ("Gộp"). Đã gộp `codex/flame-slash-strip` (275 `f3e7029`, 279 `180db0b`) vào main của game: `bbb46d8`. tsc sạch, 989/989 test trên main. Lưu ý: nhánh lô 1 (`codex/fire-lot1-art`, có 264, 277, 278, 280) cũng sửa `element-fire.ts`; lúc gộp phải xử lý xung đột với 275.
