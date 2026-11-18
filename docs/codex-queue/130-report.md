# Phiếu 130 · Last Line · Đổi giao diện sang tiếng Anh

Ngày 29/10/2026 · Nhánh `ts-codex`, worktree `games/.wt-ts-codex`. Đã hoàn thành lượt đổi chữ người chơi thấy; chờ Claude duyệt chữ và kiểm màn hình. Báo cáo này cùng thư mục `130/` nằm ở repo cha.

## Đã làm

- Kiểm kê **266** đoạn literal/dòng HTML có chữ Việt hiển thị trong phạm vi cho sửa: [strings-before.md](130/strings-before.md).
- Dịch **278** đoạn/thuộc tính hiển thị: 270 thay đổi trực tiếp, 7 lời khuyên cục bộ và 1 nhãn PERFECT ghi đè từ kit. Bảng còn ghi đủ **8** dòng test so chữ cũ đã sửa: [strings.md](130/strings.md), dữ liệu [changes-final.json](130/changes-final.json).
- Đổi màn tựa, `<title>`, `document.title`, nhãn canvas, lỗi WebGL và trạng thái tải sang Last Line; đặt `lang="en"`. Dịch menu, gợi ý phím, chọn ải, briefing, loadout, mô tả súng/quái, HUD, banner, kết quả và hồ sơ gõ. Bốn ải là First Shift, Hunt Pack Leader, Rift Wall, Shield Glow.
- Giữ tên súng/quái theo `docs/games/NAMES_EN.md`; lấy quyết định 28/10 trong AGENTS làm chuẩn ngôn ngữ thay phần quy tắc cũ trong tài liệu tên. Nghĩa `vi`, từ dự phòng, Vanguard và Draconis giữ nguyên.
- Thêm `src/app/english.ts` để dùng lời khuyên tiếng Anh mà không sửa kit hay cách chọn id; cấu hình view đổi nhãn hoàn hảo thành PERFECT. Thêm `tests/english-ui.test.ts`; cập nhật đúng các đối chiếu chữ cũ trong `tests/small-labels.test.ts`, `tests/theme.test.ts`.
- Changelog trong worktree: `docs/changelog/2026-10-29-english-ui.md`.

Mọi đường dẫn mã phía trên tính từ worktree. Chi tiết file đổi có trong [status.txt](130/status.txt). Chỉ thay literal ở content; [structure.json](130/structure.json) xác nhận phần ngoài literal giữ nguyên ở các file content và các file view/app đổi chữ trực tiếp. Ba ngoại lệ cấu trúc là import/chọn bảng ADVICE_EN ở skill/results và ghi đè riêng nhãn FEEL; không đổi cách tính hay chọn luật.

## Kiểm bắt buộc

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| `pnpm check` trước | 20 file test, **193/193** test; kit **59/59**; TypeScript và Vite đạt | [check-before.log](130/check-before.log) |
| `pnpm check` cuối | 21 file test, **196/196** test; kit **59/59**; TypeScript và Vite đạt | [check-final.log](130/check-final.log) |
| Kiểm thời gian | Không có test thời gian đỏ nên không cần chạy riêng ba lần. Median bước sim 700 quái/2.000 đạn: **0,547 → 0,648 ms**, giới hạn median 1,5 ms; p95 **1,194 → 1,261 ms** | Hai log check |
| Luật chương không đổi | **152 dòng trước, 152 dòng sau, giống hệt từng byte** | [trước](130/chapter-hashes-before.txt), [sau](130/chapter-hashes-after.txt), [verification.json](130/verification.json) |
| Trace S0 | **18/18** test đạt ở cả hai lần check, golden không sửa | Hai log check |
| Đột biến | Thêm tạm `void "Bắt đầu";` vào `src/view/screens.ts`: **1 đỏ/2 xanh**, exit **1**. Khôi phục đúng từng byte: **3/3 xanh**, exit **0** | [đỏ](130/mutation-red.log), [xanh](130/mutation-green.log), [mutation.json](130/mutation.json) |
| Phạm vi | `git -C games/.wt-ts-codex status --short -uall`: **20 file**, tất cả thuộc danh sách cho ghi; `git diff --check` đạt | [status.txt](130/status.txt), [verification.json](130/verification.json) |

Lần check cuối vẫn chạy đủ kit verify, Vitest, TypeScript và Vite. Để giữ đầu ra build trong thư mục báo cáo, dùng shell truyền xuống cả hai lệnh pnpm lồng:

```sh
cd /Users/toandx/htdocs/typing-game/games/.wt-ts-codex
TICKET130_BUILD_DIR=/Users/toandx/htdocs/typing-game/docs/codex-queue/130/build-final \
pnpm --config.script-shell=/Users/toandx/htdocs/typing-game/docs/codex-queue/130/check-shell.py check
```

Shell chỉ thêm `--no-cache` cho Vitest, `--configLoader runner --outDir ... --emptyOutDir` cho Vite; không bỏ kiểm nào. Build tạm trong báo cáo đã được dọn, giữ log. Các lần check đầu chạy theo đầu ra mặc định `dist` vì cấu hình shell chưa được truyền xuống pnpm lồng; đó là đầu ra build bị Git bỏ qua, không phải thay đổi mã trong bảng status. Không chạy build/test của game khác. Vite còn cảnh báo chunk lớn hơn 500 kB sẵn có, không làm check đỏ.

## Độ dài và còn sót

[Kiểm độ dài](130/lengths.json) dựng trực tiếp hàm menu cũ/mới trong Node, không mở trình duyệt: **5.304 lượt, 69 biến thể khác nhau, 0 trường vượt 120%**. Đã rút gọn các ghi chú Campaign và độ khó; nhãn nhỏ dùng Rig, BGM, KO, Med, Hi, Lv, MAX, CLEAN. Bảng duyệt đánh dấu các mảnh ghép và các đoạn hướng dẫn/tiêu đề dài; độ dài ký tự không thay cho kiểm tràn chữ khi render.

[remaining.md](130/remaining.md) ghi toàn bộ kết quả sau sửa, gồm kit và chú thích. Test không miễn nguyên các file hiện nghĩa từ; chỉ miễn đúng hằng FALLBACK trong `src/app/vocab.ts`. `src/view/hud.ts`, `strip.ts`, `screens.ts`, `src/app/results.ts` vẫn quét literal bình thường. Test còn kiểm template lồng, dấu Unicode tách rời và CSS.

**Ngoại lệ so với yêu cầu quét source tuyệt đối:** `src/content/stage-rules.ts:149` còn diagnostic `: more Rèn levels than bays`. Đây là chữ nội bộ của `validateChapter`, không hiển thị cho người chơi. Phiếu chỉ cho sửa chuỗi hiển thị trong content nên giữ nguyên, miễn đúng file + literal + lời gọi `problems.push` trong guard và ghi rõ ở bảng còn sót. Vì thế không khẳng định danh sách literal thô chỉ còn nghĩa từ, kit và chú thích. Claude cần chốt ngoại lệ này hoặc mở quyền cho một lượt sửa diagnostic; không lén sửa ngoài phạm vi.

## Đã bỏ qua và việc Claude cần xem

Không sửa `src/kit/**`, sim, script, golden, id, khóa lưu trữ, event, số cân bằng, package metadata hoặc tài liệu ngoài danh sách. Không động cây game chính, worktree khác, game khác, Tu Tiên, media hay audio-lab. Không chạy git có ghi, không commit/gộp/push.

Kit còn ADVICE_VI và HOÀN HẢO nhưng Last Line đã dùng bản dịch cục bộ; thông báo thiếu giọng đọc trong kit chưa có callback hiển thị ở game này. Các literal kit khác để Claude sửa tại nguồn kit, đầy đủ trong remaining.md.

Claude còn duyệt từng dòng bảng chữ, các cách gọi Hull/armor, Black Hole Horde, Rig/BGM/KO/Med/Hi/Lv và kiểm từng màn tại **1280×720, 1920×1080**. Chưa có bằng chứng render và chưa nghiệm thu tràn chữ vì phiếu cấm dev server/trình duyệt.
