# Phiếu 191 · Last Line · Gắn bộ tiếng phím Firefly vào game, có nghe thử khi rê chuột

**Nguồn:** chủ dự án 29/10/2026 tối: "phần âm typing, triển khai nó luôn cho tôi đi … cho thêm tính năng khi hover vào thì phát ra âm 1 s". Bộ âm do phiếu 189 dựng; danh sách chọn và nghe thử do phiếu 190 làm trong kit.

**Báo cáo:** `docs/codex-queue/191-report.md`, thư mục `docs/codex-queue/191/`.

**Chỉ chạy khi** Claude đã duyệt 189 và 190 và đồng bộ kit mới vào worktree dưới đây. Kiểm `src/kit/kit-manifest.json` có module `ui` và `feedback` mới (có hàm đọc danh mục bộ phím của phiếu 190). Chưa có thì dừng, ghi vào báo cáo.

## Nơi làm

- Worktree `games/.wt-ts-typefx`, nhánh `ts-typefx`. Đây là nơi làn TF2 đã gắn dải chữ, bảng Settings (F1) và Sound (F2): `src/app/quick.ts`, `src/app/settings.ts`, `src/app/main.ts`, `src/view/type-fx*.ts`.
- `git status` trước khi làm: phải sạch.

## Việc

1. **Đưa bộ âm vào game** (media, không vào Git):
   - chép `~/AudioLab/review/staging/keys-firefly/` (các thư mục `<id>/` gồm `.ogg`, `preview.ogg`, `keys-manifest.json`, cùng `keys-manifest.json` gốc) vào `public/assets/typing-survival/audio/keys/`;
   - không chép `.wav`;
   - cập nhật danh sách media của game theo cách repo đang làm (`media.md5` hay manifest media; đọc README và `docs/` của game). Claude chạy `media:push`.
   - JSON danh mục phải được Git giữ hoặc có trong gói media: làm theo luật `.gitignore` của game (`docs/games/AUDIO_PIPELINE.md` §11) và ghi cách đã chọn.
2. **Hàng "Keyboard sound"** trong bảng Sound:
   - lấy từ danh mục, qua hàm kit của phiếu 190: Off, Relay (âm riêng của game), rồi các bộ Firefly;
   - bỏ năm lựa chọn "pending" cũ (`KEYBOARD_CHOICES` trong `src/app/quick.ts`).
3. **Gõ chữ phát bộ đã chọn:**
   - mỗi phím đúng một biến thể `key-*`, phím cách `space-*`, theo luật biến thể của kit;
   - theo Master × Keyboard volume; Off thì im;
   - lưu vào save; tải lại trang vẫn giữ.
4. **Nghe thử:** rê chuột hay focus lên một bộ thì phát `preview.ogg` 1 s (thành phần kit 190). Khi bảng mở, trận tạm dừng và phím chữ không vào ô gõ (luật `docs/games/IN_GAME_SETTINGS.md`).
5. **Mặc định:** bộ đứng đầu danh mục. Nếu chủ dự án đã nghe và chọn bộ nào, Claude sẽ ghi vào báo cáo 189; có thì dùng bộ đó.
6. **Test:**
   - danh mục nạp đúng, có Off và Relay;
   - chọn bộ thì phím gõ phát đúng file của bộ;
   - bộ lưu cũ đã mất thì về mặc định;
   - không phát khi Off hay Master tắt tiếng;
   - test sẵn có và ván vàng không đổi.

## Cấm

- Mọi lệnh git có ghi; sửa `src/kit/**`; chạy đồng bộ kit.
- Dev server, trình duyệt, mạng.
- Đụng game khác, worktree khác, Tu Tiên.
- Chữ người chơi thấy phải là tiếng Anh.

## Kiểm (ghi số)

1. `pnpm check` xanh (số test). Test thời gian đỏ khi máy bận thì chạy riêng ba lần.
2. Bảng file đã chép (số file, cỡ MB) và cách media đi vào gói.
3. `git status --short -uall`: chỉ file của việc này, cộng `docs/changelog/<ngày>-keyboard-sounds.md`.
