# Phiếu 190 · Danh mục tiếng phím và nghe thử khi rê chuột

Ngày 29/10/2026 · Mac mini M4. **Đã hoàn thành mã kit và Lab, 840/840 test xanh, hai typecheck sạch. Chưa đồng bộ vào game; chờ Claude duyệt hiển thị và nghe thực tế theo thứ tự của phiếu.**

## Phần đã làm

- `shared/game-kit/feedback/typing-fx/audio.ts`: thêm `loadKeyboardCatalog()`, đọc manifest gốc phiếu 189, trả **Off đầu tiên**, sau đó các bộ theo `order` (giữ thứ tự gốc khi bằng nhau). Id trùng giữ bản hợp lệ đầu tiên; bỏ từng mục sai, không làm hỏng cả danh sách. URL manifest và preview được giải theo base, không ép thư mục bằng id. `extra` cho game thêm/ghi đè lựa chọn riêng như Relay. Thiếu/sai manifest gốc trả trạng thái và danh sách dự phòng, không ném lỗi ra UI.
- Cùng file: `KeyboardSoundPreview` dùng **một voice**, chờ **150 ms** khi hover/focus, phát đoạn **1,000 s**, tắt dần **30 ms** khi rời/chuyển/đóng; bản kế tiếp bắt đầu sau đuôi cũ. Fetch preview lười, cache promise và `AudioBuffer`; kiểm phiên yêu cầu sau fetch/decode để không phát muộn. File thiếu được thử lại ở thao tác sau. Node được ngắt kết nối khi kết thúc.
- Preview nối vào destination của context với mức **Master × Keyboard**, không qua Effects để tránh nhân đôi mức. Mute hoặc Master bằng 0 chặn phát; đổi slider/mute cập nhật ngay. Mở Sound từ click/phím khởi động context trong cử chỉ người dùng; trường hợp trình duyệt còn chặn audio vẫn im lặng, có thể thử lại bằng thao tác nghe/chọn.
- Chọn tên/click/Enter/Space gọi `onChange` đồng bộ để game lưu, hủy preview focus còn chờ, tải đủ các file bộ chọn vào **instance `TypingSounds` gameplay được truyền qua `keyboardSounds`**, và phát một preview. Tải bộ cũ hoàn tất muộn không thay bộ chọn sau hoặc Off. Giữ hành vi tự kích hoạt của API cũ `loadKeyboard()`; API manifest mới dành cho controller không tự kích hoạt.
- `shared/game-kit/ui/quick-settings/keyboard-choices.ts`: thành phần `KeyboardSoundChoices`, listbox có nút lựa chọn, roving Tab, ArrowUp/ArrowDown/Home/End; focus chỉ nghe, Enter/Space mới chọn. Nút Listen là phần tử cạnh listbox, không nhét nút tương tác vào `role=option`. Pointer touch không kích hoạt hover; chạm tên chọn, chạm loa chỉ nghe.
- `quick-settings.ts`, `types.ts`, `rows.ts`, `logic.ts`, `index.ts`: nối controller và thành phần trên vào riêng hàng Keyboard sound; hàng khác giữ điều khiển cũ. Bản lưu trỏ tới bộ đã mất chuyển về bộ đầu tiên còn khả dụng và phát thay đổi để game lưu; Off được giữ nguyên. Dừng preview khi đóng, đổi bảng hoặc hủy kit.
- `feedback/typing-fx/settings.ts`, `index.ts`: sửa chú thích id danh mục, xuất API mới. Không sửa định dạng save `typingFx`; kit tiếp tục để game sở hữu thao tác ghi save.
- `tools/typing-feedback-lab/`: thay select cố định bằng đúng thành phần kit, thêm Master/Mute để kiểm mức nhân, lưu id lựa chọn trong `localStorage`. Chỉ tải bộ đang dùng/chọn, không tải cả danh mục. Gỡ nhánh phát synth thử nghiệm khỏi Lab để các bộ hiện ra lấy âm thật từ staging. Tham số `keysBase` chọn base URL; `LAB_KEYS` chọn thư mục staging chỉ đọc qua Vite. Mount chỉ phục vụ GET/HEAD, chặn đường dẫn/symlink ra ngoài gốc. [README](../../tools/typing-feedback-lab/README.md) có lệnh chạy, quy ước và mẫu tích hợp game.

CSS danh sách nằm trong **file mới `keyboard-choices.ts`**, không ghi vào `quick-settings/css.ts` của TF2. Khung tối đa **306 px = 9 × 34 px** ở desktop, có cuộn riêng; các hàng cảm ứng cao **44 px**. Panel tiếp tục dùng giới hạn chiều cao viewport hiện có. Đây là số từ mã và test, **chưa phải nghiệm thu render 1280 × 720**.

## Quyết định dự phòng và ảnh loa

**Giữ `DEFAULT_KEYBOARD_PROFILES` và `KEYBOARD_PROFILES` làm dự phòng tương thích.** Đã đọc `games/.wt-ts-typefx/src/app/quick.ts`: Last Line còn nhập `DEFAULT_KEYBOARD_PROFILES` để ghép Relay và các bộ đang pending. Không sửa game, không thay mặc định save chung bằng một id Firefly chưa được game đóng gói. Khi truyền danh mục, hàng Keyboard sound dùng hoàn toàn lựa chọn từ danh mục, không thêm năm id cũ. Lab truyền `fallback: []`, nên thiếu danh mục thì chỉ hiện Off kèm thông báo.

Đã đọc [báo cáo 180](180-report.md); ảnh loa phù hợp là **`hud-sound.64.png`**, thuộc bộ icon 180, đã xác nhận file tồn tại. Kit nhận ảnh qua `icons["hud-sound"]`; Lab mount chỉ đọc `games/dragon-hold/art-src/ui/quick-settings/selected/hud-sound.64.png` tại `/lab-keyboard-icon/`. **Không thiếu ảnh cho nút nghe.** Không sửa, chép hay sinh lại ảnh; không vẽ CSS/SVG/emoji. Nếu caller chưa cấp ảnh hoặc ảnh tải lỗi thì dùng chữ Listen có nhãn truy cập, ghi rõ đây là trạng thái thiếu art khi tích hợp. Báo cáo 180 còn việc nhận bộ icon của Claude; phiếu này không tự nhận thay.

Không tạo âm/ảnh mới hoặc prompt mới; dùng nguyên âm Firefly phiếu 189 và ảnh phiếu 180. Không thêm thư viện, không phát sinh việc sửa `THIRD_PARTY.md`.

## Kiểm tra và số đo

| Kiểm | Trước | Sau |
|---|---:|---:|
| File test kit | 53 qua | **54 qua** |
| Test kit | 806 qua | **840 qua** |
| Lỗi / bỏ qua | 0 / 0 | **0 / 0** |
| Typecheck kit | — | **0 lỗi**, exit 0 |
| Typecheck Lab | — | **0 lỗi**, exit 0 |
| Cú pháp cấu hình Vite | — | **0 lỗi**, exit 0 |

Log: [test trước](190/tests-before.txt), [test sau](190/tests-after.txt), [typecheck kit](190/typecheck-kit.txt), [typecheck Lab](190/typecheck-lab.txt), [kiểm cú pháp Vite](190/check-vite.txt). Log typecheck Lab/cú pháp Vite rỗng là lệnh thành công không có thông báo.

Lệnh đã chạy, không chạy build/test game:

```bash
pnpm --dir shared/game-kit test
pnpm --dir shared/game-kit typecheck
shared/game-kit/node_modules/.bin/tsc -p tools/typing-feedback-lab/tsconfig.json --noEmit
node --check tools/typing-feedback-lab/vite.config.mjs
node docs/codex-queue/190/verify-catalog.mjs
```

**34 test mới**, tại `shared/game-kit/ui/quick-settings/keyboard-sound.test.ts`; cập nhật helper và assertion của test radio cũ để theo listbox mới, không giảm số test cũ:

| Nhóm | Số | Trường hợp được chứng minh |
|---|---:|---|
| Danh mục | 6 | Off/thứ tự/URL, thiếu file/dự phòng rỗng, manifest gốc sai, id trùng/mục sai, thêm/ghi đè Relay, bộ lưu cũ mất và giữ Off |
| Voice và tải | 19 | Trễ 150 ms và dài 1 s; rời trước dwell; rời khi fetch/decode; chuyển có fade 30 ms và không chồng; tải đảo thứ tự; cache/concurrent fetch; mức nhân và cập nhật sống; Master mute/0; mute lúc chờ; lỗi rồi thử lại; Off/disabled; chọn tải đủ 13 file và preview một lần; tải cũ không thay Off; API cũ; ngắt node; bộ lỗi tải lại; chọn khi mute vẫn tải đủ file |
| Thành phần và vòng đời | 9 | Hover chuột/cảm ứng; focus và mũi tên/Home/End; Enter/Space/click (3 test) chọn một lần; nút Listen cảm ứng không chọn và ảnh 180; khung cuộn; `onChange` lưu và close/switch/destroy dừng; đóng khi fetch không phát muộn |

[Kiểm staging thật bằng mã kit](190/verify-catalog.mjs) dùng TypeScript đã có để nạp nguyên mã audio/intensity, inject fetch JSON bằng đọc filesystem; không gọi mạng. [Kết quả](190/catalog-staging.json): **8 lựa chọn = Off + 7 bộ** Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack; **91/91 sample và 7/7 preview tồn tại**, loader danh mục chỉ đọc **1 manifest gốc**, không tự lấy sample/preview.

Đường dẫn `~/AudioLab/review/staging/keys-firefly/` hiện chưa có. Theo báo cáo 189, sandbox không ghi được ngoài workspace; lần kiểm dùng bản giao thật tại `tmp/keys-firefly/staging/keys-firefly/`, không chuyển hoặc sửa staging. README có cả lệnh cho vị trí ngoài repo sau khi chủ dự án chép bộ, và lệnh trỏ vào bản tạm hiện có.

## Giữ TF2 và phạm vi

**Không ghi vào cả ba file TF2; số chỗ thêm chung file: 0.** Lưu diff đầy đủ, stat và SHA-256 trước/sau trong thư mục phiếu:

- [Stat trước](190/tf2-before.stat.txt), [stat sau](190/tf2-after.stat.txt): đều **3 file, 14 dòng thêm, 4 dòng xóa**.
- [Diff trước](190/tf2-before.diff), [diff sau](190/tf2-after.diff): giống hệt byte.
- [Hash trước](190/tf2-before.sha256.json), [hash sau](190/tf2-after.sha256.json): **3/3 file giống hệt byte**, gồm `typing-fx/css.ts`, `typing-fx/draw.ts`, `quick-settings/css.ts`.

[Status trước](190/status-before.txt), [status sau](190/status-after.txt) là nguyên đầu ra `git status --short -uall`; [đối chiếu phạm vi](190/scope.json) tách file phiếu và dữ liệu có sẵn. Workspace vốn có sửa game/docs và các WAV `typing-mp3/` chưa theo dõi của tác vụ khác, nên **status toàn repo không thể chỉ còn file phiếu 190**. Không giấu hay dọn chúng. Các file mã của phiếu chỉ ở đúng ba khu vực được cho phép; báo cáo/chứng cứ chỉ trong `docs/codex-queue/190*`.

## Chưa làm và việc cần Claude/chủ dự án xem

- Không dev server, trình duyệt, mạng, đồng bộ kit, lệnh Git có ghi, build/test game; không sửa `games/**`, `tools/audio-lab/**` hoặc Tu Tiên, đúng giới hạn phiếu.
- Không chụp render/ghi khung thô nên không có dữ liệu capture cần prune. Test DOM/Web Audio giả không thay nghiệm thu hình/âm thanh.
- Claude cần duyệt listbox và thanh cuộn ở **1280 × 720**, focus/Tab/Enter/Space trên trình duyệt thật, nút Listen trên cảm ứng, chất lượng tiếng và tắt đuôi khi rê nhanh. Chưa tự chấm nhận 9+ hay xin chủ dự án ký thay bước duyệt.
- Khi đồng bộ ở phiếu sau, game phải truyền **cùng instance `TypingSounds` đang phát gameplay**, cấp ảnh loa 180 của game, và nối `onChange("keyboard", id)` vào save. Relay dùng `extra`/`onKeyboardUse`; có preview riêng thì cấp trường `preview`. Mẫu ở README; không thực hiện tích hợp game trong phiếu 190.
