# Phiếu 219 · Danh sách tiếng phím theo họ, bộ 70–100 biến thể

Ngày 30/10/2026 · Mac mini M4. **Đã hoàn thành mã kit/Lab; 867/867 test xanh, typecheck kit và Lab sạch. Chưa đạt điều kiện dữ liệu hơn 80 bộ: danh mục v2 phiếu 218 hiện chỉ có 32 bộ/7 họ. Chưa đồng bộ game; chờ Claude duyệt hiển thị và nghe thực tế.**

## Phần đã làm

- `shared/game-kit/feedback/typing-fx/audio.ts`: `loadKeyboardCatalog()` đọc thêm `family` và `score` hữu hạn, bỏ metadata tùy chọn sai mà vẫn giữ bộ hợp lệ. **Off đầu tiên, lựa chọn riêng của game như Relay ngay sau Off**, rồi các bộ theo `order` ổn định. Giữ quy tắc id trùng, URL tương đối, dự phòng và danh mục cũ không có họ; không lọc theo điểm hoặc giới hạn số bộ.
- `shared/game-kit/ui/quick-settings/keyboard-choices.ts`: mỗi đoạn họ liên tiếp có tiêu đề và `role="group"` với `aria-labelledby`; tiêu đề không phải option, không focus/chọn/nghe được. Giữ nguyên thứ tự danh mục kể cả họ xuất hiện lại ở đoạn sau. Mũi tên bỏ qua tiêu đề và bộ bị vô hiệu hóa; Home/End chạy toàn danh sách; PageUp/PageDown nhảy tới bộ đầu tiên có thể chọn của họ trước/sau, tới biên thì dừng. Các lựa chọn Off/Relay không tạo tiêu đề họ.
- Khung danh sách vẫn tối đa **306 px**, cuộn riêng; hàng desktop **34 px**, cảm ứng **44 px**, tiêu đề họ **28 px**. Cột Listen có khoảng trống bằng tiêu đề để giữ đúng hàng. Sau khi mở Sound, bộ đã chọn tự cuộn vào tầm nhìn bằng thay đổi `scrollTop` của riêng danh sách, không cuộn bảng ngoài hoặc trang. Lab cũng gọi đồng bộ khi hiện lại bảng đã ẩn.
- `VariantPicker`: mỗi lượt dùng mỗi biến thể đúng một lần; giữa các lượt tránh **8 cú gần nhất** với bộ đủ lớn. Bộ ít biến thể dùng cửa sổ tối đa `n − 1`. Giữ lịch sử tối đa tám cú ngay cả lúc chỉ vài sample đầu sẵn sàng; sample mới gia nhập không làm mất lịch sử. Đọc thêm tên ba chữ số như **`key-100.ogg`**, vẫn đọc tên hai chữ số cũ.
- `TypingSounds`: tối đa **16 fetch/decode/lô**, nhường một macrotask giữa các lô; sample nào giải mã xong được công bố ngay, có thể gõ trước khi cả bộ xong. Tiếp tục tải mọi file; lỗi được liệt kê. Trạng thái `ready` của manifest lớn đòi đủ file đã khai báo, ngoài mức tối thiểu tương thích cũ.
- Vòng đời chọn bộ: hủy yêu cầu cũ bằng `AbortController`, chặn công bố sau fetch/decode, dừng các lô tiếp theo. Nhả buffer/picker của bộ cũ và các voice đang giữ buffer khi đổi bộ hoặc chọn Off; chọn lại bộ đã rời phải tải lại sample. `TypingSounds.release(id)` được xuất qua lớp hiện có; `use(id)` giữa hai bộ đã tải cũng nhả bộ trước. API trực tiếp cũ `use("off")` vẫn chỉ làm im tiếng để giữ tương thích; controller chọn danh mục thực hiện nhả khi chọn Off.
- Preview được cache riêng và giữ nguyên hành vi phiếu 190: chờ **150 ms**, phát **1 giây**, fade **30 ms**, một voice, Master × Keyboard, nghe qua rê chuột/focus/Listen; chọn bộ mới vẫn nghe một preview. Chọn lại đúng bộ đang tải dùng chung yêu cầu. Hủy/nhả sample không làm mất cache preview.
- `feedback/typing-fx/index.ts`: xuất `KEYBOARD_DECODE_BATCH_SIZE` để caller/test thấy giới hạn. Không thay định dạng save.
- `tools/typing-feedback-lab/`: mặc định đọc **`tmp/keys-firefly/staging-v2/keys-firefly`**, vẫn lấy thư mục qua `LAB_KEYS`, base URL qua `keysBase`. Khôi phục bộ lưu và chọn bộ dùng cùng controller tải dần; khôi phục không tự nghe preview. [README](../../tools/typing-feedback-lab/README.md) có lệnh chạy v2, cách thử v1, điều hướng và vòng đời bộ nhớ.

## Kiểm tra và số đo

| Kiểm | Trước | Sau |
|---|---:|---:|
| File test kit | 54 qua | **56 qua** |
| Test kit | 840 qua | **867 qua** |
| Lỗi / bỏ qua | 0 / 0 | **0 / 0** |
| Test mới phiếu 219 | — | **27** |
| Bộ test phiếu 190 | 34 qua | **34 qua** |
| Typecheck kit | — | **0 lỗi**, exit 0 |
| Typecheck Lab | — | **0 lỗi**, exit 0 |
| Cú pháp Vite | — | **0 lỗi**, exit 0 |

Log: [test trước](219/kit-tests-before.txt), [test sau](219/kit-tests-after.txt), [typecheck kit](219/typecheck-kit.txt), [typecheck Lab](219/typecheck-lab.txt), [cú pháp Vite](219/check-vite.txt), [diff check](219/diff-check.txt). Log rỗng là kiểm tra thành công không có thông báo. Không chạy build/test game.

**27 test mới**:

| File | Số | Phần được chứng minh |
|---|---:|---|
| `feedback/typing-fx/audio-progressive.test.ts` | 18 | Xoay 70/80/100 file qua 100 lượt, không lặp cửa sổ 8; tăng số sample giữ lịch sử; đọc file 100; tối đa 16 giải mã đồng thời và nhường giữa lô; phát khi lô đầu còn chờ; phát đều 100 file qua player; lỗi file; nhả bộ/voice; hủy/đóng khi decode còn chờ; cache preview; chọn lại bộ; đổi khi manifest còn chờ; Off; khôi phục Lab không preview |
| `ui/quick-settings/keyboard-families.test.ts` | 9 | Danh mục giả lập **84 bộ + Off + Relay = 86 lựa chọn**; metadata và danh mục cũ; 7 nhóm ARIA; tiêu đề không chọn được; mũi tên/Home/End/PageUp/PageDown; họ xuất hiện lại không đổi thứ tự; mở lại Sound tự cuộn bên trong; không cuộn sau destroy |

Test 190 chỉ sửa kỳ vọng và tên của **một test thứ tự Relay**, vì phiếu 219 yêu cầu chuyển Relay từ cuối lên ngay sau Off; không bỏ test hoặc giảm assertion hành vi. Các test còn lại của 190 giữ nguyên.

Lệnh chính:

```bash
pnpm --dir shared/game-kit test
pnpm --dir shared/game-kit typecheck
shared/game-kit/node_modules/.bin/tsc -p tools/typing-feedback-lab/tsconfig.json --noEmit
node --check tools/typing-feedback-lab/vite.config.mjs
node docs/codex-queue/219/verify-catalog.mjs
```

## Danh mục thật và phần còn thiếu của phiếu 218

[Kiểm staging](219/verify-catalog.mjs) nạp nguyên mã TypeScript kit bằng TypeScript đã có, inject đọc JSON qua filesystem; **0 yêu cầu mạng**. [Kết quả](219/catalog-staging.json):

- Danh mục v2 hiện có **32 bộ**, **7 họ**: Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack.
- Giữ đủ `family`, `score`, đúng thứ tự `order`; Off và Relay đứng trước danh mục. Loader danh mục chỉ đọc **1 manifest gốc**, không tải trước sample/preview.
- Mỗi bộ có **70–80 file key**, **78–88 file tổng** gồm space. **2.652/2.652 sample và 32/32 preview** tồn tại, kích thước lớn hơn 0.
- Điều kiện **hơn 80 bộ chưa đạt**. Mã và DOM giả đã được kiểm với 84 bộ; không tự nhân bản, tạo tên/bộ giả vào staging để làm đủ số. Bổ sung âm/danh mục thuộc phiếu 218, ngoài phạm vi ghi của 219. Khi phiếu 218 giao đủ, chỉ cần tải lại Lab; không có giới hạn 32/80 trong loader/UI.

## Giữ TF2 và phạm vi

**Không ghi vào ba file TF2.** [Stat trước](219/tf2-before.txt), [stat sau](219/tf2-after.txt) giống hệt: **3 file, 14 dòng thêm, 4 dòng xóa**. [Hash trước](219/tf2-hashes-before.json), [hash sau](219/tf2-hashes-after.json): **3/3 file giống byte**. Kết quả tự đối chiếu ở [scope.json](219/scope.json).

[Status trước](219/status-before.txt) và [status sau](219/status-after.txt) là nguyên đầu ra `git status --short -uall`. Repo đã có nhiều sửa chưa commit và file chưa theo dõi của các tác vụ khác, nên **status toàn repo không thể chỉ có file phiếu 219**. Không dọn hoặc giấu chúng; đối chiếu chỉ quy thay đổi của phiếu này vào đúng phạm vi. Mã sửa ở:

- `shared/game-kit/feedback/typing-fx/{audio.ts,index.ts,audio-progressive.test.ts}`;
- `shared/game-kit/ui/quick-settings/{keyboard-choices.ts,keyboard-sound.test.ts,keyboard-families.test.ts}`;
- `tools/typing-feedback-lab/{README.md,vite.config.mjs,src/main.ts,src/profiles.ts}`;
- báo cáo và chứng cứ trong `docs/codex-queue/219*`.

Không sửa `types.ts`, `quick-settings.ts`, file TF2, `games/**`, `tools/audio-lab/**`, Tu Tiên hoặc thư viện dùng chung khác. Không thêm thư viện, không cần sửa `THIRD_PARTY.md`. Không tạo ảnh/âm thanh mới; giữ ảnh loa phiếu 180 và âm thật phiếu 218, nên không có prompt mới.

## Việc cần Claude/chủ dự án xem

- Hoàn tất phiếu 218 để có **hơn 80 bộ thật**; hiện chưa thể đánh dấu điều kiện dữ liệu hoàn tất.
- Claude duyệt render **1280 × 720**, thanh cuộn/tiêu đề, bàn phím và trình đọc màn hình thật, Listen trên cảm ứng; nghe preview 1 giây, rê nhanh, tiếng khi đang tải dần và đổi bộ. Test DOM/Web Audio giả chưa chứng minh cảm nhận âm thanh, frame time, GC thực hoặc nghiệm thu hiển thị.
- Sau duyệt mới đồng bộ kit vào ba game và chép vào Monkeytype theo phiếu sau. Phiếu này không đồng bộ, không chạy dev server/trình duyệt/mạng, không chạy lệnh Git có ghi. Không có capture/frame thô nên không có dữ liệu cần prune.
