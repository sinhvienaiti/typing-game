# Phiếu 052 · Tuyến Cuối · Đổi tên tiếng Anh cho danh từ trong game (lượt đổi tên của game)

Làm **giống hệt phiếu 050** (`docs/codex-queue/050-td-english-names.md`): đọc phiếu đó trước, rồi áp dụng cho Tuyến Cuối với các thay đổi dưới đây.

- **Bảng tên:** `docs/games/NAMES_EN.md`:
  - mục "Tuyến Cuối": 12 tên phải đổi, 46 dòng mã;
  - các dòng chốt của "Quyết định của Claude (27/10/2026)", ví dụ Đầu Đàn thành **Pack Leader**, Vết nứt (hiểm họa) thành **Rift**. Tên ải "Vách nứt" giữ tiếng Việt;
  - các dòng "Cần Claude xem" giữ tiếng Việt.
- **Worktree:** `games/.wt-ts-names` (nhánh `ts-names`, cắt từ `main` ea8e0f9, đã `pnpm install`). Chỉ ghi trong `games/.wt-ts-names/src/**`, `tests/**`, `scripts/**` ở các file `NAMES_EN.md` liệt kê cho Tuyến Cuối, cộng `games/.wt-ts-names/docs/changelog/2026-10-28-english-names.md` và `docs/codex-queue/052-report.md`.
- **Không đụng** `games/typing-survival` (cây chính, làn chấm đang chạy) và `src/view/fx*`, `src/view/glows*`. Nếu một tên nằm trong các file này thì bỏ qua và ghi vào báo cáo.
- **Golden:** Tuyến Cuối có băm chương (`scripts/chapter-hashes.ts`, 152 dòng) và vết vàng Trận thử trong `pnpm check`. Phải giữ nguyên.
  - Chạy `scripts/chapter-hashes.ts` trước và sau; `diff` phải rỗng.
  - Lệch thì dừng, không cập nhật.
- **Hàm cắt hay ghép tên theo cấu trúc tiếng Việt** (như `shortFoeName()` của Rồng ở phiếu 051): được sửa tối thiểu để trả tên tiếng Anh đầy đủ, kèm test nếu có. Ghi rõ trong báo cáo.
- **Assert test có tên tài nguyên:** đổi theo tên tiếng Anh, giữ câu Việt. Ví dụ "Chưa đủ vàng" thành "Chưa đủ Gold", theo quyết định của Claude ở 051.
- Báo cáo `docs/codex-queue/052-report.md` theo mẫu của phiếu 050.

**Xong khi:** sáu kiểm của phiếu 050 đạt trên `games/.wt-ts-names`, cộng `diff` băm chương rỗng. Claude kiểm trong trình duyệt rồi mới commit.
