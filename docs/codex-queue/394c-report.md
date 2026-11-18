# Phiếu 394c — Cấp từ Ultimate khi đầy giới hạn từ sống

Ngày: 16/11/2026. Phản biện của phiếu: PASS (Sonnet). Làm một luồng; quota đọc từ phiên Codex mới nhất lúc bắt đầu còn 52%.

**Đã hoàn tất phần sim và kiểm thử của phiếu.** Lệnh tái hiện 394b nay cấp được từ Ultimate, giữ nguyên giới hạn 5 từ sống.

## Đã sửa

- `games/immortality-cultivation/src/sim/words.ts`: trong `allocate()`, Ultimate đang chờ và có năng lượng đầy được thay một từ kỹ năng đang sống, `typed === 0`, không phải từ đang khóa. Duyệt ngược danh sách ưu tiên sẵn có để chọn từ có ưu tiên thấp nhất; không thêm lần rút RNG để chọn từ bị thay. Xét cả các kỹ năng đứng trước Ultimate trong danh sách, nên hoạt động cả với preset `learn`.
- Ultimate không lấy chỗ của bất kỳ Seal/Cleanse nào. Không có ứng viên thì tiếp tục chờ; các đường cấp lại và `stepWords()` hiện có sẽ thử tiếp ngay khi có chỗ hoặc khi người chơi nhả khóa.
- Giữ nguyên ledger, `liveCap`, nghỉ chữ cái đầu và bộ chọn từ `tryDeal()`: luật chữ đầu khác nhau và không tiền tố vẫn do kit hiện có kiểm soát. Không cần sửa file sim khác. Giữ nguyên các thay đổi Ultimate gõ rồi Space có sẵn từ 394.

## Test và kết quả

Thêm `games/immortality-cultivation/tests/sim/ultimate-allocation.test.ts`, **9 test**, dùng sim thật, không mock:

- Đầy 5 từ với Seal, ở cả `relax` và `learn`: Ultimate thay ô 4, Seal giữ nguyên; view model ô 5 chứa đúng từ được cấp.
- Ô 4 đang gõ, kể cả gõ hai chữ rồi Backspace về một chữ: giữ nguyên từ và khóa; Ultimate thay ô 2 là ứng viên kế tiếp.
- Bộ từ nhỏ tạo giới hạn thật `A − 3 = 1`: nếu chỉ còn Seal hoặc Cleanse cấp bách thì Ultimate chờ; giải phóng từ cấp bách cấp được Ultimate ngay trong cùng lời gọi.
- Nếu từ duy nhất đang gõ dở thì Ultimate chờ; sau Esc, bước cấp từ kế tiếp cấp được Ultimate.
- Ba lần đầy năng lượng, gõ từ và Space liên tiếp: mỗi lượt đúng một lần hoàn thành/một Cast; trạng thái sẵn sàng không tự sinh thêm từ. Chạy hai lần với từng seed 7, 19, 99 cho toàn bộ sự kiện và hash thế giới giống nhau. Mọi lượt kiểm tra ledger, cap, chữ đầu và tiền tố.
- Ultimate đã sẵn sàng bị xóa khi vào `break`; năng lượng còn nguyên. Sang warning phải gõ lại, Space chưa gõ không tung chiêu. Test có sẵn trong `ultimate-space.test.ts` tiếp tục kiểm cả chết và hết đợt cuối khi còn ở live lull.

Cập nhật kỳ vọng trong `tests/typing/words-sim.test.ts`: ở cap 5, khi có Cleanse + Seal đầu tiên + ô 2 đang gõ, ô 3 và Ultimate giữ chỗ; **ô 1 và 4 chờ**, thay cho kỳ vọng cũ là ô 4 và Ultimate chờ. Đây là thay đổi hành vi có chủ đích theo phiếu 394c.

| Lệnh, chạy từ thư mục game | Kết quả |
| --- | --- |
| `../../.local/bin/heavy.sh --cores=2 pnpm test tests/sim/ultimate-allocation.test.ts tests/typing/words-sim.test.ts tests/sim/ultimate-space.test.ts --maxWorkers=2` | 3 file, 36 test PASS |
| `../../.local/bin/heavy.sh --cores=2 pnpm test --maxWorkers=2` | **101 file, 1.037 test PASS**, 20,62 s |
| `../../.local/bin/heavy.sh --cores=2 pnpm exec tsc --noEmit` | **PASS**, không lỗi |
| `git diff --check -- src/sim/words.ts tests/typing/words-sim.test.ts tests/sim/ultimate-allocation.test.ts` | PASS |

Trước sửa sim, lượt chạy hồi quy mới đã tái hiện Ultimate không có chỗ. Sau sửa, toàn bộ test PASS. Các kiểm tra `runLog`/hash trong `combat-real-lanes`, `core-world`, `match-runner` và golden 387c trong `twin-pearl.test.ts` đều PASS; **không đổi golden/hash kỳ vọng nào**. Không chạy script cập nhật golden.

## Đối chiếu lệnh 394b

Chạy lại nguyên lệnh trong mục “Ultimate còn lỗi trong phạm vi mô phỏng” của `394b-report.md`:

```text
cap = 5
live = 5
ultimate.kitSlot = 3
ultimate.state = ready
ultimate.text = drum
cell.label = Ultimate
cell.text = drum
cell.state = ready
```

Đây là đầu ra API sim và `banQuyetView()` thật, không phải ảnh chụp DOM.

## Phạm vi và việc owner/Claude cần xem

Chỉ sửa `src/sim/words.ts`, test mới, kỳ vọng test nêu trên và báo cáo này. Không sửa UI, lab, docs Tu Tiên, scripts, media hay file của worker khác; không build, mở server, đổi nhánh, commit, push, reset, clean hoặc stash.

Không bỏ hạng mục sim/test nào của 394c. Chưa chạy browser/capture: các phép đo DOM và nghiệm thu hình ảnh còn mở của **394b** vẫn cần Claude chạy kịch bản `tests/ui/ui-layout394b-capture.mjs`; nay đường tái hiện cấp từ Ultimate đã được sửa để đối chiếu trong lượt đó.
