# Phiếu 409 — Chữ hiển thị tiếng Anh

Ngày: 16/11/2026. Phản biện đầu vào: PASS (Sonnet).

Đã rà toàn bộ `src/ui/`, `src/app/` và nhãn trong `src/content/`. Chỉ sửa literal chuỗi và các kỳ vọng chuỗi tương ứng trong test; không đổi số, luật, cấu trúc DOM hay CSS. Những tệp đang có thay đổi của tác nhân khác được giữ nguyên ngoài các literal liệt kê dưới đây.

Điều kiện nhận phiếu: quota còn 43 % theo bản ghi rate_limits mới nhất lúc bắt đầu. Làm một luồng; không gọi trợ lý ngoài vì phiếu đã có giải pháp và PASS.

## Bảng đối chiếu đầy đủ

Đường dẫn trong bảng tính từ `games/immortality-cultivation/`. Các đoạn của chuỗi ghép được ghi nguyên literal, bao gồm khoảng trắng. Một dòng bao gồm mọi lần xuất hiện của cùng literal trong tệp.

| Tệp | Chuỗi cũ | Chuỗi mới |
| --- | --- | --- |
| `src/ui/ime-banner.ts` | `Bộ gõ tiếng Việt đang bật: chữ gõ vào không thành phím chữ cái.` | `Vietnamese input is on: keystrokes are not arriving as letters.` |
| `src/ui/ime-banner.ts` | `Chuyển nguồn nhập sang ABC (Control + Space, hoặc biểu tượng trên thanh menu) rồi gõ tiếp.` | `Switch input to ABC (Control + Space, or the menu bar icon), then keep typing.` |
| `src/ui/ime-banner.ts` | `Chuyển Unikey hoặc EVKey sang E (Ctrl + Shift, hoặc bấm biểu tượng V ở khay hệ thống) rồi gõ tiếp.` | `Switch Unikey or EVKey to E (Ctrl + Shift, or the tray's V icon), then keep typing.` |
| `src/ui/ime-banner.ts` | `Bấm để ẩn` | `Click to dismiss` |
| `src/ui/learning-frame.ts` | `Nghe từ` | `Hear word` |
| `src/ui/learning-frame.ts` | `MỚI` | `NEW` |
| `src/ui/learning-frame.ts` | `Vừa học: ` | `Just learned: ` |
| `src/ui/menu.ts` | `Tiếp tục` | `Resume` |
| `src/ui/menu.ts` | `Tốc độ gõ` | `Typing speed` |
| `src/ui/menu.ts` | `Giảm chuyển động` | `Reduce motion` |
| `src/ui/menu.ts` | `Cỡ chữ` | `Text size` |
| `src/ui/menu.ts` | `Đổi phím` | `Key bindings` |
| `src/ui/menu.ts` | `Rút lui` | `Retreat` |
| `src/ui/menu.ts` | `Theo máy` | `System` |
| `src/ui/menu.ts` | `Bật` | `On` |
| `src/ui/menu.ts` | `Tắt` | `Off` |
| `src/ui/menu.ts` | `Xóa một chữ` | `Delete letter` |
| `src/ui/menu.ts` | `Nhả khóa, đóng bảng, menu` | `Unlock, close, pause` |
| `src/ui/menu.ts` | `Bắt đầu đợt, trả lời` | `Start wave, submit` |
| `src/ui/menu.ts` | `Đan phù 1` | `Item 1` |
| `src/ui/menu.ts` | `Đan phù 2` | `Item 2` |
| `src/ui/menu.ts` | `Đan phù 3` | `Item 3` |
| `src/ui/menu.ts` | `Chế độ cửa hàng` | `Shop mode` |
| `src/ui/menu.ts` | `Đi lên` | `Move up` |
| `src/ui/menu.ts` | `Đi xuống` | `Move down` |
| `src/ui/menu.ts` | `Sang trái` | `Move left` |
| `src/ui/menu.ts` | `Sang phải` | `Move right` |
| `src/ui/menu.ts` | `Nâng cơ quan` | `Upgrade mechanism` |
| `src/ui/menu.ts` | `Bán cơ quan` | `Sell mechanism` |
| `src/ui/menu.ts` | `Phím chữ chỉ để gõ: chọn phím khác` | `Letters are for typing: choose another key` |
| `src/ui/menu.ts` | `Phím này không dùng được: chọn phím khác` | `Key unavailable: choose another` |
| `src/ui/menu.ts` | `Bấm phím mới cho ` | `Press a new key for ` |
| `src/ui/menu.ts` | ` (Esc: hủy)` | ` (Esc: cancel)` |
| `src/ui/menu.ts` | `↑ ↓ chọn, Enter đổi, Esc quay lại` | `↑ ↓ select, Enter rebind, Esc back` |
| `src/ui/menu.ts` | `Enter lần nữa để rút lui (giữ 50 % Thú Hạch, kết quả học không mất)` | `Enter again to retreat (keep 50 % Beast Cores; learning is saved)` |
| `src/ui/menu.ts` | `Tạm dừng` | `Paused` |
| `src/ui/menu.ts` | `Enter lần nữa` | `Enter again` |
| `src/ui/results.ts` | `Chớp` | `Flash` |
| `src/ui/results.ts` | `Hoàn hảo` | `Perfect` |
| `src/ui/results.ts` | `Tốt` | `Good` |
| `src/ui/results.ts` | `Vừa` | `Fair` |
| `src/ui/results.ts` | `Ẩu` | `Sloppy` |
| `src/ui/results.ts` | `Trận Lực còn` | `Core remaining` |
| `src/ui/results.ts` | `Đợt giữ được` | `Waves held` |
| `src/ui/results.ts` | `Thú đã hạ` | `Beasts slain` |
| `src/ui/results.ts` | `Thú Hạch` | `Beast Cores` |
| `src/ui/results.ts` | `Thú Hạch (giữ ` | `Beast Cores (keep ` |
| `src/ui/results.ts` | `Linh Sa còn` | `Spirit Sand left` |
| `src/ui/results.ts` | `Từ đã gõ` | `Words typed` |
| `src/ui/results.ts` | `Từ mới đã gặp` | `New words seen` |
| `src/ui/results.ts` | `Từ gõ sai` | `Mistyped words` |
| `src/ui/results.ts` | `Thu Hoạch · Giữ được ải` | `Results · Pass defended` |
| `src/ui/results.ts` | `Thu Hoạch · Ải đã vỡ` | `Results · Pass fallen` |
| `src/ui/results.ts` | `Thu Hoạch · Rút lui` | `Results · Retreated` |
| `src/ui/results.ts` | `Thu Hoạch` | `Results` |
| `src/ui/results.ts` | `Enter: chơi lại ải này` | `Enter: replay this pass` |
| `src/ui/results.ts` | `Trận` | `Battle` |
| `src/ui/results.ts` | `Học` | `Learning` |
| `src/ui/review-card.ts` | `Nghe rồi gõ từ` | `Listen, then type` |
| `src/ui/review-card.ts` | `Xem nghĩa rồi gõ từ` | `Read the meaning, then type` |
| `src/ui/review-card.ts` | `Chọn nghĩa đúng (phím 1 / 2 / 3)` | `Choose the meaning (1 / 2 / 3)` |
| `src/ui/review-card.ts` | `Thẻ Ôn` | `Review Card` |
| `src/ui/review-card.ts` | `THẺ ÔN` | `REVIEW CARD` |
| `src/ui/review-card.ts` | `Phím 1 / 2 / 3 chọn · Esc đóng thẻ` | `1 / 2 / 3 choose · Esc close` |
| `src/ui/review-card.ts` | `Enter nộp · Backspace xóa · Esc đóng thẻ` | `Enter submit · Backspace delete · Esc close` |
| `src/ui/review-card.ts` | `Đúng!` | `Correct!` |
| `src/ui/review-card.ts` | `Chưa đúng, nhớ lại nhé` | `Not quite. Remember this word.` |
| `src/ui/word-book.ts` | `Mới học` | `New words` |
| `src/ui/word-book.ts` | `Gõ sai` | `Mistyped` |
| `src/ui/word-book.ts` | `Cần ôn` | `Due for review` |
| `src/ui/word-book.ts` | `Sổ Từ` | `Word Book` |
| `src/ui/word-book.ts` | `Trận này chưa có từ để ghi vào Sổ Từ.` | `No words to record this match.` |
| `src/app/pace-card.ts` | `Tốc độ gõ` | `Typing speed` |
| `src/app/pace-card.ts` | `Bạn gõ nhanh cỡ nào?` | `How fast do you type?` |
| `src/app/pace-card.ts` | `Thú tràn vào nhanh hay chậm, từ dài hay ngắn theo tốc độ này; không ai phải gõ nhanh hơn sức mình. Chưa biết thì chọn "Chưa biết": game đo lại sau đợt 1. Hết trận, game ghi tốc độ thật của bạn.` | `Beast pace and word length match your speed. Choose "Not sure" to measure after wave 1. Your speed is recorded after each match.` |
| `src/app/pace-card.ts` | `Phím số chọn · ↑ ↓ rồi Enter · hoặc bấm chuột` | `Number keys · ↑ ↓ then Enter · or click` |
| `src/app/typing-pace.ts` | `Mới tập gõ` | `Beginner` |
| `src/app/typing-pace.ts` | `Còn nhìn phím` | `Looking at keys` |
| `src/app/typing-pace.ts` | `Gõ chậm` | `Slow` |
| `src/app/typing-pace.ts` | `Vừa, người chơi chuẩn` | `Steady, standard pace` |
| `src/app/typing-pace.ts` | `Khá nhanh` | `Fairly fast` |
| `src/app/typing-pace.ts` | `Nhanh` | `Fast` |
| `src/app/typing-pace.ts` | `Rất nhanh` | `Very fast` |
| `src/app/typing-pace.ts` | `Số đo: ` | `Measured: ` |
| `src/app/typing-pace.ts` | `Đúng ` | `Accuracy: ` |
| `src/app/typing-pace.ts` | ` % phím, đo qua ` | ` % across ` |
| `src/app/typing-pace.ts` | ` trận` | ` matches` |
| `src/app/typing-pace.ts` | `Chưa biết` | `Not sure` |
| `src/app/typing-pace.ts` | `Chơi ở ` | `Start at ` |
| `src/app/typing-pace.ts` | ` WPM, game đo lại sau đợt 1` | ` WPM; measured after wave 1` |
| `src/content/data/beasts.ts` | `Thạch Thử` | `Stone swarm` |
| `src/content/data/beasts.ts` | `Phong Lang` | `Wind wolf` |
| `src/content/data/beasts.ts` | `Hỏa Nha` | `Fire crow` |
| `src/content/data/beasts.ts` | `Nham Viên` | `Rock ape` |
| `src/content/data/beasts.ts` | `Thiết Giáp Trư` | `Armored boar` |
| `src/content/data/beasts.ts` | `Lang Đầu Đàn` | `Pack leader` |
| `src/content/data/consumables.ts` | `Hồi Xuân Đan` | `Healing pill` |
| `src/content/data/consumables.ts` | `Kim Thân Phù` | `Iron ward` |
| `src/content/data/consumables.ts` | `Lôi Hỏa Phù` | `Thunder talisman` |
| `src/content/data/elites.ts` | `Cuồng` | `Frenzied` |
| `src/content/data/elites.ts` | `Thiết Bì` | `Ironhide` |
| `src/content/data/elites.ts` | `Hồi Nguyên` | `Regenerating` |
| `src/content/data/mechanisms.ts` | `Kiếm Thung` | `Sword stakes` |
| `src/content/data/mechanisms.ts` | `Lôi Phù Trụ` | `Thunder pillar` |
| `src/content/data/mechanisms.ts` | `Phong Ấn Võng` | `Binding net` |
| `src/content/data/school-kiem.ts` | `Phi Kiếm` | `Flying Sword` |
| `src/content/data/school-kiem.ts` | `Ngự Kiếm Quyết` | `Sword Command` |
| `src/content/data/school-kiem.ts` | `Nhất Tuyến Xuyên Vân` | `Cloudpiercer` |
| `src/content/data/school-kiem.ts` | `Hồi Kiếm Hộ Thân` | `Sword Ward` |
| `src/content/data/school-kiem.ts` | `Lưu Quang Bộ` | `Radiant Step` |
| `src/content/data/school-kiem.ts` | `Lạc Kiếm Trận` | `Swordfall Formation` |
| `src/content/data/school-kiem.ts` | `Thiên Hà Kiếm Vũ` | `Celestial Sword Rain` |
| `src/content/data/school-kiem.ts` | `Kiếm Tâm` | `Sword Heart` |
| `src/content/data/school-kiem.ts` | `Tích Kiếm` | `Gathering Blades` |
| `src/content/data/trial-set.ts` | `Bộ thử dự phòng: không tải được kho từ chung` | `Fallback word set: shared vocabulary unavailable` |
| `src/content/data/trial-set.ts` | `Nhất Tuyến Xuyên Vân` | `Cloudpiercer` |
| `src/content/data/trial-set.ts` | `Lạc Kiếm Trận` | `Swordfall Formation` |
| `src/content/data/trial-set.ts` | `Thiên Hà Kiếm Vũ` | `Celestial Sword Rain` |
| `src/ui/hud.ts` | `Ironback Wolf King` | `Thiết Bối Lang Vương` |

## Kỳ vọng test đã cập nhật

| Tệp | Chuỗi cũ | Chuỗi mới |
| --- | --- | --- |
| `tests/ui/menu.test.ts` | `Tiếp tục` | `Resume` |
| `tests/ui/menu.test.ts` | `Tốc độ gõ` | `Typing speed` |
| `tests/ui/menu.test.ts` | `Giảm chuyển động` | `Reduce motion` |
| `tests/ui/menu.test.ts` | `Cỡ chữ` | `Text size` |
| `tests/ui/menu.test.ts` | `Đổi phím` | `Key bindings` |
| `tests/ui/menu.test.ts` | `Rút lui` | `Retreat` |
| `tests/ui/menu.test.ts` | `Bật` | `On` |
| `tests/ui/menu.test.ts` | `Enter lần nữa` | `Enter again` |
| `tests/ui/menu.test.ts` | `Phím chữ` | `Letters are for typing` |
| `tests/ui/results.test.ts` | `Thu Hoạch` | `Results` |
| `tests/ui/results.test.ts` | `Giữ được ải` | `Pass defended` |
| `tests/ui/results.test.ts` | `Trận Lực còn` | `Core remaining` |
| `tests/ui/results.test.ts` | `Đợt giữ được` | `Waves held` |
| `tests/ui/results.test.ts` | `Thú đã hạ` | `Beasts slain` |
| `tests/ui/results.test.ts` | `Thú Hạch` | `Beast Cores` |
| `tests/ui/results.test.ts` | `Linh Sa còn` | `Spirit Sand left` |
| `tests/ui/results.test.ts` | `Từ đã gõ` | `Words typed` |
| `tests/ui/results.test.ts` | `Chớp` | `Flash` |
| `tests/ui/results.test.ts` | `Hoàn hảo` | `Perfect` |
| `tests/ui/results.test.ts` | `Tốt` | `Good` |
| `tests/ui/results.test.ts` | `Vừa` | `Fair` |
| `tests/ui/results.test.ts` | `Ẩu` | `Sloppy` |
| `tests/ui/results.test.ts` | `Từ mới đã gặp` | `New words seen` |
| `tests/ui/results.test.ts` | `Từ gõ sai` | `Mistyped words` |
| `tests/ui/results.test.ts` | `Thú Hạch (giữ ` | `Beast Cores (keep ` |
| `tests/ui/learning-panels.test.ts` | `Mới học` | `New words` |
| `tests/ui/learning-panels.test.ts` | `Cần ôn` | `Due for review` |
| `tests/typing/typing-pace.test.ts` | `Chưa biết` | `Not sure` |
| `tests/ui/hud.test.ts` | `Ironback Wolf King` | `Thiết Bối Lang Vương` |

## Chuỗi tiếng Việt cố ý giữ

- `src/content/data/stage-m0a.ts`: `Thanh Thạch Ải` là địa danh riêng, được canon D50 nêu đích danh phải giữ. `ART_AUDIO_VFX_PLAN.md` Q3 chỉ đưa “Thanh Thach Pass” làm ví dụ tên game chưa chốt, nên không coi đó là tên canon thay thế.
- `src/content/data/boss.ts` và `src/ui/hud.ts`: `Thiết Bối Lang Vương` là tên boss riêng được D50 bảo lưu. Nhãn HUD tiếng Anh cũ được trả về tên canon để đồng nhất với dữ liệu/thẻ đợt.
- Nghĩa học từ: các trường `vi`, cột nghĩa trong `DECK_ROWS`, nghĩa đáp án câu hỏi ôn tập và chú giải `shortMeaning` được giữ nguyên. Danh sách literal nghĩa có trong phạm vi mã nguồn ở phụ lục dưới; nghĩa nạp từ kho từ dùng chung tiếp tục đi qua `gloss`, `question.vi`, `question.choices`, `entry.vi` và `item.vi` mà không dịch.
- `src/app/learning.ts`: `: Học trước without hintUsed` là thông báo kiểm tra hợp đồng sự kiện nội bộ, không phải chữ hiển thị. Giữ nguyên, cùng kỳ vọng test tương ứng.
- Chú thích mã nguồn, ID kỹ thuật không dấu (`kiem-thung`, `phong-lang`…), tên biến và tên tệp không phải chữ hiển thị; giữ nguyên. Không thấy nhãn nhân vật `Lam` trong phạm vi cần đổi.

## Kiểm tra và giới hạn

- Chưa chạy `pnpm test`, build hay bộ test game: house rules của lượt giao việc cấm chạy các lệnh này, dù mục nghiệm thu của phiếu có yêu cầu. Không tuyên bố test sạch.
- `pnpm exec tsc --noEmit`: PASS (exit 0). Kiểm tra AST trên 73 tệp đã chụp trạng thái đầu lượt xác nhận 19 tệp thay đổi và mọi phần ngoài literal chuỗi đều giữ nguyên (gồm số, biểu thức, chú thích, DOM và CSS); tệp test tốc độ còn lại chỉ đổi kỳ vọng `Chưa biết` → `Not sure`. Tổng cộng 15 tệp nguồn và 5 tệp test được sửa. Phân tích cú pháp TypeScript: 0 lỗi; quét literal tiếng Việt: 0 chuỗi hiển thị ngoài các ngoại lệ đã liệt kê. `git diff --check` trong phạm vi: PASS.
- Chưa nghiệm thu giao diện trong trình duyệt; không tạo capture hoặc video ngoài phạm vi được phép ghi. Cần coordinator kiểm tra menu, kết quả, thẻ ôn và bảng tốc độ ở các cỡ chữ trước khi chốt hiển thị.
- Không sửa `src/sim/`, `src/lab/`, `src/view/`, `src/kit/`, script, tài liệu Tu Tiên hay nhánh Git. Không commit/push/reset/clean/stash.

## Phụ lục: nghĩa học từ giữ nguyên

Dữ liệu ở `src/content/data/trial-set.ts`; gộp các cặp từ/nghĩa trùng nhau, giữ từng biến thể nghĩa khác nhau.

| Từ học | Nghĩa tiếng Việt giữ nguyên |
| --- | --- |
| `add` | `thêm vào; cộng; nói thêm` |
| `afraid` | `đáng sợ` |
| `again` | `lại, lần nữa` |
| `agenda` | `nghị trình; chương trình nghị sự` |
| `air` | `không khí` |
| `aircraft` | `phi cơ; máy bay` |
| `allergy` | `dị ứng` |
| `already` | `đã, rồi` |
| `always` | `luôn luôn; lúc nào cũng` |
| `analyze` | `phân tích` |
| `angry` | `giận; tức` |
| `answer` | `câu trả lời; lời đáp` |
| `arm` | `cánh tay; tay` |
| `art` | `nghệ thuật; mỹ thuật` |
| `artist` | `họa sĩ; nghệ sĩ` |
| `ask` | `hỏi, yêu cầu` |
| `attend` | `tham gia` |
| `audience` | `khán giả; quý vị` |
| `aunt` | `cô; dì` |
| `average` | `trung bình; bình thường` |
| `back` | `lưng; sống lưng` |
| `bad` | `tệ, xấu, tồi, dở` |
| `bake` | `nướng` |
| `balcony` | `ban công` |
| `basket` | `giỏ; rổ` |
| `bathroom` | `buồng tắm; phòng tắm` |
| `bedroom` | `phòng ngủ; buồng ngủ` |
| `better` | `tốt hơn; khá hơn` |
| `bicycle` | `xe đạp; đạp xe` |
| `big` | `to, lớn` |
| `boil` | `đun; đun sôi; luộc` |
| `book` | `sách; quyển sách` |
| `bottle` | `chai; đóng chai` |
| `brother` | `anh (em) trai` |
| `browser` | `trình duyệt; người xem qua loa` |
| `build` | `xây dựng, lắp ráp` |
| `cabinet` | `nội các; tủ` |
| `calm` | `bình tĩnh, điềm tĩnh; lặng gió, yên tĩnh; sự bình tĩnh, sự điềm tĩnh` |
| `calorie` | `ca-lo; ca-lo-ri` |
| `camera` | `máy ảnh, máy chụp hình; máy quay phim, camera truyền hình` |
| `car` | `xe hơi; ô tô` |
| `care` | `sự chăm sóc, săn sóc` |
| `carriage` | `xe ngựa; xe tải` |
| `cause` | `gây ra; tạo nên` |
| `chair` | `ghế` |
| `charger` | `bộ nạp điện` |
| `cheap` | `rẻ` |
| `child` | `đứa trẻ, đứa bé` |
| `choice` | `sự lựa chọn, sự chọn lựa` |
| `clean` | `sạch; sạch sẽ` |
| `clever` | `thông minh` |
| `climate` | `khí hậu` |
| `clothes` | `quần áo; đồ` |
| `cloud` | `mây; làm mây mù; che phủ` |
| `coffee` | `cà phê` |
| `cold` | `lạnh; rét` |
| `color` | `màu sắc` |
| `company` | `công ty, doanh nghiệp` |
| `confirm` | `xác nhận` |
| `cook` | `nấu; nấu chín; nấu ăn` |
| `cooking` | `nấu nướng; việc nấu ăn` |
| `cough` | `ho; sự ho` |
| `course` | `khóa học` |
| `crispy` | `giòn` |
| `customs` | `thuế hải quan, thuế quan` |
| `cut` | `cắt, chặt, chém` |
| `cycling` | `đi xe đạp` |
| `danger` | `nguy hiểm` |
| `database` | `cơ sở dữ liệu` |
| `daughter` | `con gái` |
| `day` | `ngày; một ngày đêm` |
| `debit` | `ghi nợ; hạch toán bên nợ` |
| `deliver` | `chuyển phát; giao` |
| `dessert` | `tráng miệng` |
| `device` | `thiết bị; dụng cụ` |
| `disagree` | `bất đồng, không đồng ý; không giống nhau, khác nhau` |
| `discuss` | `thảo luận` |
| `doctor` | `bác sĩ` |
| `door` | `cửa, cánh cửa` |
| `drink` | `uống` |
| `drive` | `lái (xe)` |
| `driver` | `người lái; tài xế` |
| `dry` | `khô; sấy; hong` |
| `dust` | `bụi; phủi` |
| `ear` | `tai; bông` |
| `early` | `sớm; trước giờ` |
| `east` | `hướng đông, phía đông` |
| `easy` | `dễ; dễ dàng` |
| `elephant` | `voi` |
| `emotion` | `cảm xúc` |
| `employee` | `nhân viên` |
| `engine` | `động cơ` |
| `enough` | `đủ` |
| `entry` | `mục từ` |
| `error` | `lỗi; sai số` |
| `evening` | `chiều tối` |
| `example` | `ví dụ; trường hợp điển hình` |
| `excited` | `bị kích thích` |
| `excuse` | `cớ; cho nghỉ` |
| `fact` | `sự thật, sự kiện` |
| `fail` | `thất bại` |
| `family` | `gia đình` |
| `far` | `xa; ở xa` |
| `father` | `cha; bố; ba` |
| `fever` | `sốt` |
| `film` | `phim; phim ảnh` |
| `folder` | `bìa hồ sơ; thư mục` |
| `follow` | `đi theo; theo sau` |
| `food` | `thức ăn, đồ ăn` |
| `foot` | `bàn chân` |
| `forest` | `rừng; trồng rừng` |
| `free` | `miễn phí` |
| `fridge` | `tủ lạnh` |
| `friend` | `bạn, người bạn thân` |
| `fry` | `thanh thiếu niên, người trẻ; chiên; rán` |
| `full` | `đầy` |
| `fun` | `niềm vui, trò vui` |
| `garbage` | `rác` |
| `garlic` | `tỏi` |
| `generous` | `rộng lượng; hào phóng` |
| `glasses` | `kính mắt; cặp kính` |
| `global` | `toàn cầu; hình cầu` |
| `good` | `tốt; hay` |
| `grill` | `lưới; nướng vĩ; nướng` |
| `guest` | `khách` |
| `hacker` | `hacker; tin tặc` |
| `hair` | `tóc; lông` |
| `hand` | `bàn tay; tay` |
| `handsome` | `đẹp trai` |
| `happy` | `vui vẻ; hạnh phúc` |
| `hard` | `khó, khó khăn` |
| `head` | `đầu` |
| `headache` | `chứng nhức đầu` |
| `healthy` | `khỏe mạnh; tốt cho sức khỏe` |
| `heart` | `tim, trái tim` |
| `heat` | `hơi nóng; đun` |
| `heater` | `bếp lò; lò` |
| `hello` | `lời chào; xin chào` |
| `hold` | `cầm, nắm, giữ` |
| `home` | `nhà, chỗ ở, nơi ở` |
| `homework` | `bài tập; bài tập về nhà` |
| `honest` | `thành thật` |
| `horse` | `ngựa; cung cấp ngựa, thắng ngựa` |
| `hot` | `nóng, nóng bức` |
| `hotel` | `khách sạn` |
| `hour` | `giờ, tiếng đồng hồ` |
| `house` | `nhà, căn nhà` |
| `idea` | `ý tưởng, ý niệm` |
| `income` | `thu nhập` |
| `injury` | `thương tích; thương tật` |
| `insect` | `sâu bọ; côn trùng` |
| `interest` | `sự quan tâm; hứng thú` |
| `internet` | `mạng internet; mạng lưới toàn cầu` |
| `issue` | `vấn đề` |
| `job` | `công việc; nghề nghiệp` |
| `juice` | `nước ép; nước` |
| `kettle` | `ấm; bình đun siêu tốc` |
| `kind` | `loại, hạng, kiểu` |
| `lake` | `hồ` |
| `lamp` | `đèn; đèn điện` |
| `landlord` | `chủ nhà; địa chủ` |
| `late` | `muộn, trễ` |
| `learn` | `học, học hỏi` |
| `less` | `ít hơn, kém hơn` |
| `lesson` | `bài; bài học` |
| `like` | `thích` |
| `limit` | `giới hạn; hạn chế` |
| `line` | `đường kẻ, vạch, nét` |
| `lion` | `sư tử` |
| `local` | `địa phương; cục bộ` |
| `love` | `yêu, thương, yêu thương` |
| `luggage` | `hành lý` |
| `major` | `quan trọng; chủ chốt` |
| `man` | `đàn ông` |
| `maybe` | `có lẽ, có thể` |
| `meal` | `bữa; bữa cơm` |
| `meat` | `thịt` |
| `medical` | `thuộc y học; y khoa` |
| `meet` | `gặp; gặp gỡ` |
| `metro` | `tàu điện ngầm; metro` |
| `milk` | `sữa; vắt sữa` |
| `mix` | `pha; hỗn hợp khô (bán sẵn); sự pha trộn` |
| `month` | `tháng` |
| `morning` | `buổi sáng` |
| `mother` | `mẹ, má` |
| `mountain` | `núi` |
| `move` | `di chuyển; chuyển động` |
| `name` | `tên; tên gọi` |
| `near` | `gần; sắp tới` |
| `neck` | `cổ; hôn hít, ôm ấp (say đắm)` |
| `nervous` | `hồi hộp` |
| `never` | `chưa bao giờ, không bao giờ` |
| `new` | `mới` |
| `news` | `tin tức, tin` |
| `night` | `đêm, ban đêm` |
| `north` | `phương bắc; hướng bắc` |
| `often` | `thường; hay; thường xuyên` |
| `old` | `già; lớn tuổi` |
| `onion` | `hành tây; hành` |
| `organic` | `hữu cơ; phân hữu cơ` |
| `organize` | `sắp xếp; tổ chức` |
| `oven` | `lò; lò nướng` |
| `paint` | `nước sơn; sơn` |
| `parking` | `bãi đỗ xe` |
| `passport` | `hộ chiếu; giấy thông hành` |
| `password` | `mật khẩu` |
| `pay` | `trả tiền, thanh toán` |
| `people` | `người, người ta` |
| `percent` | `phần trăm` |
| `permit` | `cho phép; sự cho phép` |
| `person` | `người, con người` |
| `platform` | `sân ga; nền tảng` |
| `please` | `xin; làm ơn; xin vui lòng` |
| `point` | `điểm; ý chính` |
| `polite` | `lịch sự; lễ phép` |
| `position` | `vị trí; quan điểm` |
| `possible` | `có thể (xảy ra/tồn tại)` |
| `pot` | `nồi; trồng vào chậu` |
| `prepare` | `chuẩn bị` |
| `printer` | `máy in` |
| `priority` | `sự ưu tiên` |
| `privacy` | `sự riêng tư` |
| `problem` | `vấn đề, rắc rối, khó khăn` |
| `protect` | `bảo vệ, che chở; bảo hộ (thương mại)` |
| `proud` | `tự hào; hãnh diện` |
| `prove` | `chứng minh` |
| `public` | `công cộng, công khai` |
| `quality` | `chất lượng; phẩm chất` |
| `question` | `câu hỏi` |
| `quiet` | `yên tĩnh; im lặng` |
| `rain` | `mưa` |
| `rate` | `tốc độ; tỷ lệ` |
| `read` | `đọc` |
| `really` | `thực sự, thật sự` |
| `recipe` | `công thức; công thức nấu ăn` |
| `recycle` | `tái chế` |
| `relaxed` | `thư giãn; thoải mái` |
| `religion` | `đạo; tôn giáo` |
| `replace` | `thay thế` |
| `return` | `trở về, quay lại` |
| `revenue` | `thu nhập` |
| `right` | `đúng, chính xác` |
| `river` | `sông` |
| `room` | `phòng; căn phòng` |
| `run` | `chạy; chạy bộ` |
| `runway` | `đường băng` |
| `sad` | `buồn; buồn bả; buồn rầu` |
| `safe` | `an toàn` |
| `salary` | `lương` |
| `salty` | `mặn` |
| `same` | `giống; tương tự` |
| `say` | `nói; nói ra` |
| `school` | `trường học, trường` |
| `seller` | `người bán` |
| `sheep` | `cừu` |
| `shelf` | `giá sách; giá` |
| `short` | `ngắn` |
| `shoulder` | `vai; vác` |
| `show` | `cho thấy; chỉ ra` |
| `similar` | `tương tự, giống nhau` |
| `simple` | `đơn giản, dễ dàng` |
| `sister` | `chị gái; em gái` |
| `small` | `nhỏ; bé` |
| `smile` | `cười; cười mỉm` |
| `snack` | `bữa ăn nhẹ, đồ ăn vặt; ăn nhẹ, ăn vặt` |
| `snow` | `tuyết; có tuyết rơi` |
| `son` | `con trai` |
| `south` | `hướng nam, phía nam` |
| `spicy` | `có gia vị; cay` |
| `stay` | `ở lại, lưu lại` |
| `stop` | `dừng lại; đỗ lại` |
| `store` | `cửa hàng; tiệm` |
| `story` | `truyện, câu chuyện` |
| `strategy` | `chiến lược` |
| `student` | `học sinh; sinh viên` |
| `sun` | `mặt trời; ánh nắng, ánh mặt trời; người rực rỡ như mặt trời` |
| `sure` | `chắc chắn, không nghi ngờ` |
| `symptom` | `triệu chứng; chứng trạng` |
| `system` | `hệ thống` |
| `tablet` | `phiến` |
| `talk` | `nói chuyện, trò chuyện` |
| `tall` | `cao; cỡ quần áo cho người cao` |
| `teacher` | `giáo viên, thầy giáo, cô giáo` |
| `tell` | `nói, kể` |
| `tennis` | `quần vợt; ten-nít` |
| `thank` | `cảm ơn, cám ơn` |
| `thanks` | `lời cảm ơn; sự biết ơn` |
| `theater` | `nhà hát; rạp hát` |
| `time` | `thời gian; thì giờ` |
| `tired` | `mệt mỏi; mệt nhọc` |
| `today` | `hôm nay` |
| `together` | `cùng nhau; với nhau` |
| `tomorrow` | `ngày mai; tương lai gần` |
| `topic` | `chủ đề` |
| `train` | `xe lửa; tàu hỏa` |
| `tram` | `tàu điện; đi xe điện` |
| `trip` | `chuyến đi; hành trình` |
| `upload` | `tải lên` |
| `valley` | `thung lũng` |
| `version` | `phiên bản; cách kể, cách giải thích (của một người)` |
| `view` | `quan điểm; góc nhìn` |
| `vitamin` | `sinh tố; vi ta min` |
| `wallet` | `ví; bóp` |
| `watch` | `xem, theo dõi` |
| `weak` | `yếu` |
| `weather` | `thời tiết; phía đón gió; hướng gió` |
| `wedding` | `đám cưới` |
| `week` | `tuần, tuần lễ` |
| `west` | `hướng tây` |
| `wife` | `vợ; người vợ` |
| `window` | `cửa sổ` |
| `withdraw` | `rút tiền; rút lui` |
| `woman` | `phụ nữ, đàn bà` |
| `wood` | `gỗ` |
| `word` | `từ` |
| `work` | `công việc, việc làm` |
| `worker` | `thợ; công nhân` |
| `worried` | `lo lắng` |
| `write` | `viết; sáng tác` |
| `wrong` | `sai` |
| `year` | `năm` |
| `young` | `trẻ; non; còn nhỏ` |
