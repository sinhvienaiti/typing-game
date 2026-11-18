# Phiếu 050 · Lời Gọi · Đổi tên tiếng Anh cho danh từ trong game (lượt đổi tên của game)

**Luật:** `AGENTS.md` của repo cha, mục "In-game names" (chủ dự án 27/10).
- Người chơi thấy danh từ trong game bằng tiếng Anh: tháp, bẫy, nhà, lính, loài quái, vật phẩm, súng.
- Câu, gợi ý và menu vẫn tiếng Việt.
- Nhân vật độc nhất giữ tên riêng.

Bảng tên đã chốt nằm ở `docs/games/NAMES_EN.md`:
- mục "Lời Gọi", "Bảng đề xuất";
- mục "Quyết định của Claude (27/10/2026)": các dòng chốt ở đây **thay** đề xuất của Codex 026, ví dụ Fort chứ không phải Keep;
- dòng "cả ba | các dòng còn lại | giữ tiếng Việt": mọi dòng ở "Cần Claude xem" giữ nguyên tiếng Việt.

**Thư mục làm việc:** repo cha (`.`). Mọi sửa mã chỉ diễn ra trong worktree `games/.wt-td-names` (nhánh `td-names`, cắt từ `a2-days`, đã `pnpm install`, `public/assets` là symlink).

**Chỉ được ghi:**
- `games/.wt-td-names/src/**`, `games/.wt-td-names/tests/**`, `games/.wt-td-names/scripts/**`, chỉ ở các file mà `NAMES_EN.md` liệt kê cho Lời Gọi;
- `games/.wt-td-names/docs/changelog/2026-10-28-english-names.md` (file mới);
- `docs/codex-queue/050-report.md`.

**Cấm:**
- đổi id, khóa dữ liệu, tên file, đường dẫn asset;
- đổi từ người chơi phải gõ (`shared/vocabulary/**`, danh sách từ của ải);
- chạy `pnpm dh:golden:update` hay lệnh cập nhật golden nào. Golden đổi thì dừng và ghi vào báo cáo;
- lệnh git có ghi; đụng `games/typing-defense` (cây chính), game khác, Tu Tiên;
- dev server, trình duyệt; sửa `public/assets`.

## Việc

1. Với từng dòng "phải đổi" của Lời Gọi trong `NAMES_EN.md` (28 tên, 59 dòng mã theo phiếu 026), thay literal hiển thị bằng tên tiếng Anh đã chốt. Giữ đúng kiểu chữ của tên tiếng Anh, ví dụ "Archer Tower", "Hopping Zombie".
2. Câu tiếng Việt chứa tên: chỉ thay phần tên và giữ câu. Ví dụ "Xây Tháp Cung" thành "Xây Archer Tower". Nếu câu thành sai ngữ pháp rõ, sửa tối thiểu và ghi vào báo cáo.
3. **Lần đầu tên hiện** (thẻ ra mắt, chú thích ô xây): nếu chỗ đó đã có dòng mô tả tiếng Việt, mở đầu dòng mô tả bằng nghĩa Việt ngắn trong ngoặc, ví dụ "(Tháp Cung) Bắn …". Không thêm thành phần giao diện mới.
4. Test và fixture: sửa assert hay fixture phụ thuộc chuỗi hiển thị. **Không** sửa logic test.
5. Ghi changelog ngắn: tên nào đổi, chỗ nào, test nào sửa.

## Kiểm (bắt buộc)

1. `cd games/.wt-td-names && pnpm check`: đạt. Ghi số test.
2. **Golden:** `pnpm check` gồm kiểm golden; golden phải giữ nguyên hàm băm. Golden lệch thì dừng việc và báo cáo.
3. **Không sót:**
   - một lệnh `node` (không lưu vào repo) đọc danh sách tên Việt phải đổi từ `NAMES_EN.md` và tìm từng tên trong các file của mục "File có literal tên đề xuất đổi";
   - bỏ qua chú thích và nghĩa Việt trong ngoặc ở việc 3;
   - in số chỗ còn sót, phải bằng 0.
4. **Không đổi id:**
   - `git -C games/.wt-td-names diff -U0` chỉ đổi literal chuỗi;
   - một lệnh `node` so tập id (`id:`, khóa object) trước và sau trong `src/content/**`; in số id khác, phải bằng 0.
5. **Độ dài:** liệt kê mọi tên tiếng Anh dài hơn tên Việt cũ quá 4 ký tự, kèm file và chỗ hiển thị (thẻ, nút, thanh đội), để Claude kiểm bố cục bằng trình duyệt.
6. `git -C games/.wt-td-names status --short`: chỉ file trong danh sách được ghi. `git status --short` ở repo cha: chỉ thêm `docs/codex-queue/050-report.md`.

## Báo cáo `docs/codex-queue/050-report.md`

- Bảng `| Tên Việt | Tên tiếng Anh | Số chỗ đổi | File |`.
- Câu đã sửa ngữ pháp.
- Test đã sửa.
- Kết quả sáu kiểm, kèm danh sách độ dài cho Claude.

**Xong khi:** sáu kiểm đạt. Claude kiểm trong trình duyệt rồi mới commit.
