# Typing Feedback Lab

Lab dùng focus strip của kit và **cùng thành phần `KeyboardSoundChoices`** với bảng Sound trong `QuickSettings`. Danh sách lấy từ manifest gốc phiếu 189; không còn liệt kê cố định năm hồ sơ cũ, không tải trước mọi bộ.

## Chạy

Từ thư mục gốc repo, sau khi có phụ thuộc sẵn của kit:

```bash
LAB_KEYS="$HOME/AudioLab/review/staging/keys-firefly" \
  shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs
```

Mở `http://127.0.0.1:4192/`. Biến `LAB_KEYS` là **đường dẫn thư mục**, mặc định chính đường dẫn AudioLab trên; Vite phục vụ tại `/lab-keys/` bằng GET/HEAD chỉ đọc. Bên trong cần có `keys-manifest.json` gốc chứa `profiles[]` (`id`, `name`, `manifest`, `preview`, `order`) và các đường dẫn tương đối tới manifest/preview từng bộ.

Nếu bản giao 189 vẫn ở vị trí tạm trong repo, dùng:

```bash
LAB_KEYS="$PWD/tmp/keys-firefly/staging/keys-firefly" \
  shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs
```

Có thể đổi base URL bằng `http://127.0.0.1:4192/?keysBase=/lab-keys/`. Một base HTTP khác cần tự cho phép CORS; không dùng đường dẫn filesystem làm URL. Không có danh mục thì Lab chỉ hiện **Off** và thông báo thiếu staging. Không chép âm vào repo, không ghi ngược staging.

## Thử bộ phím

- Rê chuột lên tên hoặc dùng Tab/mũi tên lên xuống/Home/End để focus: sau **150 ms** nghe **1 giây**. Focus không đổi lựa chọn.
- Rời tên, chuyển focus, đổi bộ hay ẩn bảng: dừng, tắt dần **30 ms**; bản kế tiếp chờ hết đuôi cũ. Preview được fetch/giải mã lần đầu cần nghe và cache trong phiên. Kết quả tải đến sau khi đã rời không được phát.
- Click tên, Enter hoặc Space: chọn, lưu id vào `localStorage` với khóa `typing-feedback-lab.keyboard`, tải đủ file bộ đó và phát một preview. Bộ lưu cũ đã mất chuyển về bộ đầu tiên; Off được giữ nguyên.
- Nút ảnh loa riêng: nghe mà không chọn, dùng được trên cảm ứng. Ảnh là `hud-sound.64.png` bộ Dragonhold của phiếu 180, qua mount `/lab-keyboard-icon/`; không có ảnh thì hiện chữ **Listen**, không vẽ icon thay thế. Danh sách có khung cuộn riêng, tối đa 9 dòng ở desktop; trên cảm ứng hàng cao 44 px.
- Preview theo **Master × Keyboard volume**, bỏ qua Effects; Mute Master hoặc Master bằng 0 thì không phát. Hai thanh âm lượng và Mute áp dụng ngay cả khi đang nghe.

Kit không sở hữu save của game. Khi tích hợp, game đọc danh mục trước lúc dựng QuickSettings, truyền `keyboardProfiles: catalogue.options`, `keyboardSounds: sounds` (đúng instance gameplay) và lưu `onChange("keyboard", id)` vào `typingFx.soundProfile` của save. Lựa chọn riêng như Relay được truyền qua `extra`; bộ không có manifest do game xử lý bằng `onKeyboardUse` hoặc callback preview cũ.

```ts
const catalogue = await loadKeyboardCatalog(keysBase, {
  extra: [{ value: "relay", label: "Relay" }],
});
const quick = new QuickSettings({
  keyboardProfiles: catalogue.options,
  keyboardSounds: sounds,
  getValues,
  onChange, // game áp dụng và ghi save ngay tại đây
});
```

`DEFAULT_KEYBOARD_PROFILES` chỉ dùng dự phòng cho game chưa có danh mục. Bộ có manifest được tải từ URL manifest thật trong danh mục, không suy ra bắt buộc `<id>/`. Game vẫn phải tải bộ đã lưu khi khởi động gameplay, như trước; mở bảng không tự thay phần khởi tạo âm của game.

## Kiểm tra không mở trình duyệt

```bash
pnpm --dir shared/game-kit test
pnpm --dir shared/game-kit typecheck
shared/game-kit/node_modules/.bin/tsc -p tools/typing-feedback-lab/tsconfig.json --noEmit
```

Phiếu 190 không chạy dev server, trình duyệt, mạng hoặc build/test game. Vitest kiểm hành vi bằng đồng hồ giả, DOM giả và Web Audio giả; hiển thị thật ở 1280 × 720, thao tác thiết bị cảm ứng và nghe thực tế vẫn cần Claude duyệt trước khi đồng bộ vào game.
