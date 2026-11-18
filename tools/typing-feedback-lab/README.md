# Typing Feedback Lab

Lab dùng focus strip của kit và **cùng thành phần `KeyboardSoundChoices`** với bảng Sound trong `QuickSettings`. Phiếu 219 chuyển mặc định sang danh mục v2 của phiếu 218, có `family`, `score` và bộ nhiều biến thể. Danh mục cũ của phiếu 190 vẫn đọc được; Lab chỉ tải sample của bộ đang chọn.

## Chạy

Từ thư mục gốc repo, sau khi có phụ thuộc sẵn của kit:

```bash
LAB_KEYS="$PWD/tmp/keys-firefly/staging-v2/keys-firefly" \
  shared/game-kit/node_modules/.bin/vite --config tools/typing-feedback-lab/vite.config.mjs
```

Mở `http://127.0.0.1:4192/`. `LAB_KEYS` là **đường dẫn thư mục**, mặc định là thư mục v2 trong lệnh trên; Vite phục vụ tại `/lab-keys/` bằng GET/HEAD chỉ đọc. Có thể trỏ `LAB_KEYS` sang thư mục giao nhận khác, kể cả ngoài repo. Bên trong cần có `keys-manifest.json` gốc chứa `profiles[]` (`id`, `name`, `manifest`, `preview`, `order`, thêm `family` và `score` ở v2), cùng manifest/preview/sample tương ứng.

Có thể đổi base URL bằng `http://127.0.0.1:4192/?keysBase=/lab-keys/`. Một base HTTP khác cần tự cho phép CORS; không dùng đường dẫn filesystem làm URL. Không có danh mục thì Lab chỉ hiện **Off** và thông báo thiếu staging. Không chép âm hoặc ghi ngược staging. Muốn thử bản cũ, đặt `LAB_KEYS="$PWD/tmp/keys-firefly/staging/keys-firefly"`.

Danh mục được đọc nguyên thứ tự `order`, không lọc theo `score` hoặc giới hạn số bộ. **Tại lúc làm phiếu 219, v2 mới có 32 bộ/7 họ**, chưa đạt đầu vào hơn 80 bộ của phiếu 218. Vitest dùng thêm danh mục giả lập 84 bộ; khi phiếu 218 bổ sung, tải lại trang để đọc đủ danh mục mới.

## Thử bộ phím

- **Off** đứng đầu; lựa chọn riêng của game như **Relay** đứng ngay sau Off. Các bộ có `family` nằm dưới tiêu đề họ tương ứng (Deep, Warm, …); tiêu đề là nhãn nhóm ARIA, không chọn được. Danh mục không có họ vẫn là danh sách phẳng.
- Rê chuột lên tên hoặc dùng Tab/mũi tên lên xuống/Home/End để focus: sau **150 ms** nghe **1 giây**. Focus không đổi lựa chọn. Mũi tên bỏ qua tiêu đề và bộ bị vô hiệu hóa; **PageUp/PageDown** chuyển tới bộ đầu tiên có thể chọn của họ trước/sau.
- Rời tên, chuyển focus, đổi bộ hay ẩn bảng: dừng preview, tắt dần **30 ms**; bản kế tiếp chờ hết đuôi cũ. Preview được fetch/giải mã lần đầu cần nghe và cache trong phiên. Kết quả tải đến sau khi đã rời không được phát.
- Click tên, Enter hoặc Space: chọn, lưu id vào `localStorage` với khóa `typing-feedback-lab.keyboard`, tải đủ file bộ đó và phát một preview. Bộ lưu cũ đã mất chuyển về bộ đầu tiên; Off được giữ nguyên. Khôi phục bộ đã lưu dùng cùng bộ tải nhưng không tự phát preview.
- Sample giải mã tối đa **16 file/lô**, nhường một lượt cho luồng giao diện giữa các lô. Những sample đầu đã giải mã dùng được ngay khi gõ. Bộ 70–100 biến thể xoay hết một lượt trước khi xoay lại, không lặp trong **8 cú gần nhất** khi có đủ biến thể; số biến thể ít hơn dùng cửa sổ tối đa `n − 1`.
- Đổi bộ hoặc chọn Off hủy việc công bố sample đang tải của bộ cũ, nhả buffer/sample và voice của bộ đó. Chọn lại bộ đã rời sẽ tải lại sample; preview 1 giây vẫn được cache riêng. `TypingSounds.release(id)` cho caller chủ động nhả bộ; `use(id)` chuyển giữa hai bộ đã tải cũng nhả bộ trước. API cũ `use("off")` vẫn chỉ làm im tiếng; luồng chọn danh mục chịu trách nhiệm nhả bộ khi chọn Off.
- Nút ảnh loa riêng: nghe mà không chọn, dùng được trên cảm ứng. Ảnh là `hud-sound.64.png` bộ Dragonhold của phiếu 180, qua mount `/lab-keyboard-icon/`; không có ảnh thì hiện chữ **Listen**. Danh sách có khung cuộn riêng tối đa **306 px** ở desktop; hàng cảm ứng cao **44 px**, tiêu đề họ cao **28 px**. Mở bảng tự cuộn tới bộ đã chọn, không cuộn trang/bảng ngoài.
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

`DEFAULT_KEYBOARD_PROFILES` chỉ dùng dự phòng cho game chưa có danh mục. Bộ có manifest được tải từ URL manifest thật trong danh mục, không suy ra bắt buộc `<id>/`. Game vẫn phải tải bộ đã lưu khi khởi động gameplay; mở bảng không tự thay phần khởi tạo âm của game.

## Kiểm tra không mở trình duyệt

```bash
pnpm --dir shared/game-kit test
pnpm --dir shared/game-kit typecheck
shared/game-kit/node_modules/.bin/tsc -p tools/typing-feedback-lab/tsconfig.json --noEmit
node --check tools/typing-feedback-lab/vite.config.mjs
```

Phiếu 219 không chạy dev server, trình duyệt, mạng hoặc build/test game. Vitest kiểm hành vi bằng đồng hồ giả, DOM giả và Web Audio giả; hiển thị thật ở 1280 × 720, thao tác thiết bị cảm ứng và nghe thực tế vẫn cần Claude duyệt trước khi đồng bộ vào game.
