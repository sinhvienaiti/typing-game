# Phiếu 154 · Kit mặc định tiếng Anh

Ngày 29/10/2026 · Trạng thái: **đạt đủ 5 mục kiểm; chờ Claude duyệt chữ và đồng bộ**.

## Đã làm

- Kiểm kê 79 file nguồn, 2.155 literal/đoạn tĩnh của template bằng AST TypeScript, bỏ test và chú thích; rà thêm các literal ASCII. Tìm được **87 vị trí tiếng Việt**: 9 người chơi thấy, 71 báo cáo dev, 7 bộ ký tự nhận diện IME. Các chuỗi không dấu thực tế có `cao`, `Nhanh`. Bảng đủ file, dòng, chuỗi và người đọc: [154/strings-before.md](154/strings-before.md).
- Đổi **80 vị trí tiếng Việt** sang tiếng Anh và **6 vị trí chỉ định dạng phần trăm** trong sáu file runtime: `shared/game-kit/feedback/profiles.ts`, `balance/{bands,gates,pace,typist}.ts`, `speech/speech.ts`. Bảng đủ **86 vị trí trước → sau**: [154/strings.md](154/strings.md). Đã đối chiếu luật hiện hành trong `docs/games/NAMES_EN.md`; không có tên riêng hoặc danh từ game cần quyết định thêm.
- Nhãn `SHIP.numbers.label` là `PERFECT`; các hồ sơ kế thừa nhận cùng nhãn. `ADVICE_EN` được xuất qua `balance/index.ts`; `ADVICE_VI` là alias cùng bảng, có `@deprecated`, vẫn dùng được với import cũ và trả tiếng Anh.
- Phần trăm viết liền (`80%`, `2.5%`); giữ dấu chấm thập phân. Không đổi giá trị số, id, khóa lưu, tên sự kiện hay trường nghĩa từ. Đối chiếu AST ngoài chuỗi của sáu file runtime không thấy thay đổi khác, ngoại trừ API lời khuyên đã nêu: [structure-check.json](154/structure-check.json).
- Thêm `shared/game-kit/english-strings.test.ts`: quét literal bằng AST, gồm chuỗi có escape, Unicode tách dấu và mọi đoạn tĩnh của template; chặn chữ Việt có dấu và danh sách từ/cụm không dấu. Cho qua test, chú thích, các trường nghĩa từ và đúng bảy literal IME trong binding `VIETNAMESE_LETTERS` của `input/keys.ts`. Danh sách không dấu là phép chặn theo từ/cụm, không phải bộ nhận diện ngôn ngữ tổng quát.
- Sửa `vitest.config.ts` để chạy test ở gốc kit; cập nhật các khẳng định nhãn, báo cáo, phần trăm và thông báo giọng đọc. Thêm ca kiểm bảng lời khuyên và alias xuất công khai. Thêm đúng một mục vào `shared/game-kit/DRIFT.md`, giữ các mục cũ.

## Năm mục kiểm bắt buộc

| Mục | Kết quả | Bằng chứng |
|---|---|---|
| 1. Test kit trước và sau | Trước: **46 file, 713 ca xanh**. Sau: **47 file, 719 ca xanh**. Lệnh `pnpm --dir shared/game-kit test`, mã thoát 0 ở cả hai lượt | [Trước](154/tests-before.log), [sau](154/tests-after.log) |
| 2. Kiểm kiểu kit | `pnpm --dir shared/game-kit typecheck` chạy `tsc -p tsconfig.json --noEmit`, **mã thoát 0** | [Log](154/typecheck.log) |
| 3. Đột biến đỏ rồi xanh | Chèn tạm `const englishStringMutation154 = "Bắt đầu";` vào `balance/pace.ts:133`: **1 file đỏ, 1 ca đỏ / 4 ca xanh**, mã thoát 1; bộ quét thấy đúng 1 vi phạm. Gỡ ra: **1 file, 5 ca xanh**, mã thoát 0. SHA-256 trước và sau phục hồi trùng nhau | [Đỏ](154/mutation-red.log), [xanh](154/mutation-green.log), [mã thoát và SHA-256](154/mutation.json) |
| 4. Bảng trước → sau | Đủ **86 vị trí literal runtime**, kèm thay đổi test/cấu hình | [Bảng chuỗi](154/strings.md), [dữ liệu đối chiếu](154/strings-changed.json) |
| 5. Phạm vi git | `git status --short -uall -- shared/game-kit`: **16 file thay đổi, 0 file ngoài danh sách được ghi**; `git diff --check -- shared/game-kit` đạt | [Trạng thái git](154/git-status-kit.log), [kiểm phạm vi](154/scope-check.json) |

Đúng thứ tự **test trước, mã sau**: sau khi thêm test và đổi kỳ vọng, chạy trên mã cũ được **7 file đỏ / 40 file xanh; 14 ca đỏ / 705 ca xanh**. Riêng bộ quét tìm đủ **80 vi phạm** cần dịch; bốn ca tự kiểm của bộ quét xanh. Sau khi sửa mã, số vi phạm còn **0 trên 79 file nguồn**. Log: [tests-red-before-code.log](154/tests-red-before-code.log).

## Giữ nguyên và chưa làm

- Giữ bảy literal IME vì đây là dữ liệu nhận diện bàn phím. Không có literal nghĩa từ tiếng Việt trong nguồn ngoài test; giữ nguyên đường dữ liệu `vi`, `meaningVi` và các trường nghĩa tương tự.
- Giữ fixture đo mực chữ `HOÀN HẢO` cũ trong test hồi quy atlas; nhãn runtime và khẳng định chữ được vẽ đã là `PERFECT`. Giữ hai nhãn đầu vào tự do tiếng Việt trong test B9 để bảo toàn kiểm API nhận nhãn từ bên gọi.
- Không sửa bản chép kit trong game, không chạy đồng bộ, build/test game, dev server, trình duyệt hay mạng; không đụng Tu Tiên. Không dùng lệnh git có ghi.

## Claude/chủ dự án cần xem

Duyệt cách diễn đạt trong [bảng chuỗi](154/strings.md), nhất là bảy lời khuyên cuối ải và các nhãn báo cáo cân bằng. Sau đó Claude đồng bộ kit vào ba game, bỏ phần đè tương ứng ở **Last Line `src/app/english.ts`** và **Dragonhold `src/view/fx.ts` (`NUMBER_FEEL`)** như mục mới trong `DRIFT.md`.
