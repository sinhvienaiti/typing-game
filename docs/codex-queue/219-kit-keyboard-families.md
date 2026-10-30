# Phiếu 219 · Kit dùng chung · Danh sách 80 bộ tiếng phím theo họ, mỗi bộ 70–100 biến thể

**Nguồn:** chủ dự án 30/10/2026: "80 bộ trở lên, 70–100 biến thể". Phiếu 218 dựng các bộ đó. Danh sách chọn của 190 làm cho 7 bộ; với hơn 80 bộ, nó phải vẫn dễ chọn và rê chuột nghe thử 1 giây như cũ.

**Báo cáo:** `docs/codex-queue/219-report.md`, thư mục `docs/codex-queue/219/`.

**Trước:** 218 (danh mục `tmp/keys-firefly/staging-v2/keys-firefly/keys-manifest.json` có `family`, `score`). **Sau:** Claude duyệt, đồng bộ kit vào ba game và chép kit vào Monkeytype.

## Nơi làm

- Repo cha: `shared/game-kit/feedback/typing-fx/` (`audio.ts`, `index.ts`) và `shared/game-kit/ui/quick-settings/keyboard-choices.ts` cùng test; `tools/typing-feedback-lab/`.
- **Có sửa chưa commit của làn Claude TF2** trong:
  - `shared/game-kit/feedback/typing-fx/css.ts`;
  - `shared/game-kit/feedback/typing-fx/draw.ts`;
  - `shared/game-kit/ui/quick-settings/css.ts`.

  Giữ nguyên các sửa đó, không đụng các file ấy (cách làm như phiếu 190).

## Việc

1. **Danh mục có họ:**
   - `loadKeyboardCatalog()` đọc thêm `family` và `score`.
   - Lựa chọn giữ thứ tự `order`. Off luôn đứng đầu; lựa chọn riêng của game (ví dụ Relay) đứng sau Off.
   - Danh mục cũ không có `family` vẫn chạy như 190.
2. **Danh sách theo họ** trong `KeyboardSoundChoices`:
   - Đầu mỗi họ có một tiêu đề họ (Deep, Warm, …), không chọn được, đọc được bằng trình đọc màn hình (nhóm ARIA).
   - Mũi tên lên xuống chạy qua mọi bộ, bỏ qua tiêu đề. Home, End giữ như cũ.
   - Thêm `PageUp` và `PageDown` để nhảy sang họ trước hay họ sau.
   - Khung vẫn giới hạn chiều cao, cuộn bên trong, không đẩy bảng tràn màn 1280 × 720.
   - Bộ đang chọn tự cuộn vào tầm nhìn khi mở bảng.
   - Rê chuột, focus nghe thử 1 giây và nút Listen giữ nguyên hành vi của 190.
3. **Nhiều biến thể:**
   - Bộ chọn biến thể phải xoay đều với 70–100 file và không lặp lại trong khoảng 8 cú gần nhất.
   - Tải hết file của bộ được chọn: giải mã theo lô, không chặn khung hình. Có thể phát được ngay khi vài file đầu đã giải mã xong.
   - Khi đổi sang bộ khác, nhả `AudioBuffer` của bộ cũ (trừ preview đã cache).
4. **Lab:** dùng danh mục v2 (đọc base qua `LAB_KEYS`, như 190) và ghi cách chạy trong README.
5. **Test (vitest):**
   - danh mục có và không có họ;
   - tiêu đề không chọn được; mũi tên bỏ qua tiêu đề; PageUp, PageDown đổi họ;
   - tự cuộn tới bộ đang chọn;
   - xoay 100 biến thể không lặp trong 8 cú;
   - tải theo lô, phát được trước khi tải xong;
   - nhả bộ nhớ khi đổi bộ;
   - các test của 190 vẫn xanh.

## Cấm

- Mọi lệnh git có ghi; chạy đồng bộ kit; sửa `games/**`; dev server, trình duyệt, mạng; đụng Tu Tiên.
- Không sửa ba file TF2 ở trên.
- Thêm thư viện thì phải ghi `docs/games/THIRD_PARTY.md`; chỉ MIT, BSD, ISC, Apache, MPL.

## Kiểm (ghi số)

1. Test kit: số trước và sau; typecheck sạch; typecheck Lab sạch.
2. `git diff --stat` ba file TF2 trước và sau giống hệt (lưu vào `219/`).
3. `git status --short -uall`: chỉ file của việc này.

**Xong khi:** danh sách hiện đủ hơn 80 bộ theo họ, nghe thử 1 giây như cũ, bộ nhiều biến thể phát đều, test xanh.
