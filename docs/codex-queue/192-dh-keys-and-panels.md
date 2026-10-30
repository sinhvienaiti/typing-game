# Phiếu 192 · Dragonhold · Nút Settings, nút loa và bộ tiếng phím Firefly trong trận

**Nguồn:** chủ dự án 29/10/2026:
- "mỗi game đều phải có icon setting … và icon loa …" (`docs/games/IN_GAME_SETTINGS.md`);
- tối cùng ngày: "phần âm typing, triển khai nó luôn … khi hover vào thì phát ra âm 1 s".

Bộ âm do phiếu 189 dựng; danh sách chọn và nghe thử do phiếu 190 làm trong kit. Last Line đã gắn mẫu ở nhánh `ts-typefx` (phiếu 191).

**Báo cáo:** `docs/codex-queue/192-report.md`, thư mục `docs/codex-queue/192/`.

**Chỉ chạy khi** Claude đã duyệt 189 và 190, tạo worktree dưới đây và đồng bộ kit mới vào đó (module `ui` có quick-settings; `feedback` có typing-fx audio). Chưa có thì dừng, ghi vào báo cáo.

> **Chạy lại 30/10 sáng (điều phối):** lượt đầu của chính phiếu này (29/10 khoảng 23:35) bị cắt giữa chừng vì hết hạn mức, nên worktree **không sạch**: các thay đổi chưa commit trong đó là việc dở của chính phiếu này, không phải của ai khác. Đừng dừng ở bước "git status phải sạch". Đọc `git status` và `git diff`, giữ phần đúng, làm tiếp cho đủ phiếu, rồi kiểm như thường. Báo cáo lượt trước (chỉ ghi "dừng vì worktree không sạch") nằm ở thư mục `docs/codex-queue/` của worktree; ghi đè bằng báo cáo mới.

## Nơi làm

- Worktree `games/.wt-dh-keys`, nhánh `dh-keys`, cắt từ `main` Dragonhold. `git status` phải sạch.
- Mẫu tham khảo, chỉ đọc: `games/.wt-ts-typefx/src/app/quick.ts`, `settings.ts`, `main.ts`.

## Việc

1. **Hai nút trong trận** theo `docs/games/IN_GAME_SETTINGS.md` §1:
   - Settings (bánh răng) và Sound (loa, đổi sang loa gạch chéo khi tắt hết tiếng);
   - góc trên phải, có ở màn tựa và trong trận; không che thẻ chữ hay HUD;
   - phím tắt `F1`, `F2`, `Esc`;
   - bảng mở thì trận tạm dừng và phím chữ không vào ô gõ; đóng thì đếm 3-2-1 rồi chơi tiếp.
   - Icon là ảnh thật của phiếu 180 (`docs/codex-queue/180-report.md`); thiếu thì ghi lại, không vẽ bằng CSS, SVG hay emoji.
2. **Bảng Sound** (`IN_GAME_SETTINGS.md` §2):
   - Master, Music, Effects, Keyboard sound, Keyboard volume, Voice, Interface;
   - nối vào các kênh âm đang có của game (đọc `src/audio/` hay nơi game phát âm); kênh nào game chưa có thì ẩn hàng đó, ghi lại.
   - Hàng "Keyboard sound" lấy từ danh mục bộ Firefly (hàm kit 190): Off rồi các bộ. Rê chuột hay focus thì nghe thử 1 s.
3. **Bảng Settings** (`IN_GAME_SETTINGS.md` §3): những mục game đã có thật (mức đồ họa Low, Medium, High, Ultra nếu game đã có tầng; giảm chuyển động nếu có), cùng Resume và Quit to title. Mục chưa có thì không thêm hàng giả.
4. **Gõ chữ phát bộ đã chọn:**
   - mỗi phím một biến thể `key-*`, phím cách `space-*`;
   - theo Master × Keyboard volume; lưu vào save.
   - Nếu game đang có tiếng gõ riêng, giữ nó thành một lựa chọn (như "Relay" của Last Line) để Off còn hoàn tác được.
5. **Media:**
   - chép `~/AudioLab/review/staging/keys-firefly/` (không `.wav`) vào `public/assets/dragon-hold/audio/keys/`;
   - cập nhật danh sách media theo cách repo làm; JSON danh mục theo luật `.gitignore` (`docs/games/AUDIO_PIPELINE.md` §11). Claude chạy `media:push`.
6. **Test:**
   - mở và đóng bằng chuột, `F1`, `F2`, `Esc`;
   - tạm dừng và chặn phím chữ;
   - đổi giá trị lưu được;
   - danh mục bộ phím, phát đúng file bộ đã chọn, không phát khi Off hay Master tắt tiếng;
   - ván vàng và mã băm trận không đổi.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy đồng bộ kit.
- Dev server, trình duyệt, mạng.
- Đụng game khác, worktree khác (nhất là `.wt-dh-vfx`, `.wt-dh-models`, `.wt-dh-codex`), Tu Tiên.
- Chữ người chơi thấy phải là tiếng Anh.

## Kiểm (ghi số)

1. `pnpm check` xanh (số test). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. `git status --short -uall`: chỉ file của việc này, cộng `docs/changelog/<ngày>-settings-and-keyboard-sounds.md`.
3. Liệt kê hàng nào bị ẩn vì game chưa có kênh hay tính năng tương ứng.
