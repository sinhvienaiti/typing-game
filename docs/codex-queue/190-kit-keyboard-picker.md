# Phiếu 190 · Kit dùng chung · Chọn tiếng phím từ danh mục, rê chuột nghe thử 1 giây

**Nguồn:** chủ dự án 29/10/2026 tối: "cứ tạo luôn, cho thêm tính năng khi hover vào thì phát ra âm 1 s để người nghe biết được âm đó là gì". Các bộ âm do phiếu 189 dựng từ âm Firefly của chủ dự án; không còn năm hồ sơ cố định (creamy, thock, marbly, clack, dome).

**Báo cáo:** `docs/codex-queue/190-report.md` (tiếng Việt), thư mục `docs/codex-queue/190/`.

**Trước phiếu này:** 189 (danh mục `~/AudioLab/review/staging/keys-firefly/keys-manifest.json`). **Sau:** Claude duyệt, đồng bộ kit vào game, rồi 191–193.

## Nơi làm

- Repo cha: `shared/game-kit/ui/quick-settings/`, `shared/game-kit/feedback/typing-fx/` (`audio.ts`, `settings.ts`, `index.ts`), `tools/typing-feedback-lab/`.
- **Có sửa chưa commit của làn Claude khác** (TF2, đang dừng) trong:
  - `shared/game-kit/feedback/typing-fx/css.ts`;
  - `shared/game-kit/feedback/typing-fx/draw.ts`;
  - `shared/game-kit/ui/quick-settings/css.ts`.

  Giữ nguyên các sửa đó, không revert, không định dạng lại. Đặt thay đổi của bạn ở file khác khi được. Buộc phải sửa chung file thì chỉ thêm, và ghi từng chỗ trong báo cáo.

## Việc

1. **Danh mục bộ phím.**
   - Hàm kit đọc `keys-manifest.json` gốc (định dạng phiếu 189: `profiles[]` có `id`, `name`, `manifest`, `preview`, `order`), trả danh sách lựa chọn cho hàng "Keyboard sound": `Off` ở đầu, rồi các bộ theo `order`.
   - Game vẫn thêm được lựa chọn riêng của mình. Ví dụ Last Line có "Relay" (`BUILT_IN_KEYS` trong `games/.wt-ts-typefx/src/app/quick.ts`).
   - `DEFAULT_KEYBOARD_PROFILES` với năm id cũ chỉ còn là dự phòng khi game chưa có danh mục, hoặc bỏ hẳn nếu không game nào cần; ghi quyết định.
   - Bộ đã chọn mà biến mất khỏi danh mục (lưu cũ): trở về bộ đầu tiên, không lỗi.
2. **Rê chuột nghe thử** trong bảng Sound.
   - **Khi nào phát:** con trỏ vào một lựa chọn bộ phím (`pointerenter`, chuột) hoặc focus bàn phím lên nó. Sau 150 ms, phát `preview` 1 s của bộ đó.
   - **Dừng và chuyển:**
     - rời ra hay chuyển sang lựa chọn khác thì dừng ngay, tắt dần 30 ms, rồi phát cái mới;
     - không bao giờ chồng hai bản;
     - đóng bảng thì dừng.
   - **Âm lượng:** theo Master × Keyboard volume; Master tắt tiếng thì không phát.
   - **Tải:** preview tải lười (lần rê đầu mới fetch), cache `AudioBuffer`. Chưa tải xong mà đã rời ra thì không phát.
   - **Khi chọn** (click, Enter, Space): đổi bộ, lưu vào save, tải đủ file của bộ đó, phát preview một lần.
   - **Hiển thị:** hàng choice hiện tại không bắt được hover từng lựa chọn (ví dụ dùng `<select>` gốc) thì đổi riêng hàng "Keyboard sound" sang danh sách nút (listbox theo ARIA: mũi tên lên xuống, Home, End). Giữ cỡ bảng như cũ: danh sách 8–9 dòng cuộn trong khung, không đẩy bảng tràn màn 1280 × 720.
   - **Cảm ứng** (không có hover): mỗi lựa chọn có nút nghe nhỏ; chạm nút thì nghe, chạm tên thì chọn.
     - Icon dùng ảnh thật của phiếu 180 (đọc `docs/codex-queue/180-report.md`).
     - Chưa có ảnh hợp thì ghi thiếu trong báo cáo. Không vẽ icon bằng CSS, SVG hay emoji: luật 28/10 của `AGENTS.md`.
3. **Lab** (`tools/typing-feedback-lab/`): có khu chọn bộ phím dùng đúng thành phần này. Nạp danh mục từ một base URL (tham số URL hay cấu hình Vite trỏ tới thư mục staging ngoài repo, chỉ đọc). Ghi cách chạy trong README của Lab.
4. **Test (vitest của kit):**
   - danh mục: thiếu file, trùng id, thứ tự, bộ lưu cũ đã mất;
   - hover: trễ 150 ms, rời trước 150 ms thì không phát, chuyển lựa chọn thì dừng bản cũ, không chồng;
   - âm lượng nhân đúng, Master tắt thì không phát;
   - focus bàn phím phát, chọn thì lưu và phát một lần;
   - nút nghe trên cảm ứng;
   - đóng bảng thì dừng.

## Cấm

- Mọi lệnh git có ghi; chạy đồng bộ kit (`scripts/sync-game-kit.mjs`).
- Sửa `games/**`; đụng Tu Tiên.
- Dev server, trình duyệt, mạng (vitest và typecheck thì chạy được).
- Thêm thư viện mới mà không ghi vào `docs/games/THIRD_PARTY.md` (giấy phép MIT, BSD, ISC, Apache, MPL; không GPL).

## Kiểm (ghi số)

1. Test kit xanh: số test trước và sau; typecheck sạch.
2. Test mới liệt kê theo mục 4.
3. `git status --short -uall`: chỉ file của việc này. Ba file đang sửa của TF2 ở trên vẫn còn đủ thay đổi cũ (`git diff --stat` trước và sau, lưu vào `190/`).

**Xong khi:** hàng "Keyboard sound" lấy từ danh mục, rê chuột hay focus nghe thử đúng 1 s, chọn thì đổi và lưu, test xanh.
