# Phiếu 394c: Ô Ultimate không được cấp từ khi đầy giới hạn từ sống


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Phiếu 394b (`394b-report.md`, mục "Ultimate còn lỗi trong phạm vi mô phỏng") tái hiện lỗi bằng API thật: preset `relax`, 4 từ kỹ năng + 1 Seal, năng lượng 100 → `liveCap = 5`, ô 5 `state = waiting`, `kitSlot = -1`, UI ghi "Waiting for slot". Nguyên nhân: `src/sim/words.ts:allocate()` chỉ cho Cleanse/Seal cấp bách thay từ khi đầy cap; Ultimate không có quyền đó. Lệnh tái hiện có trong báo cáo 394b. Luật chốt: `docs/games/tu-tien/TYPING_GAMEPLAY_DECISION.md`, mục "Owner chốt" (tuyệt kỹ: gõ từ rồi Space).

## Việc (trong `games/immortality-cultivation/`)
1. Trong bộ cấp từ (`src/sim/words.ts`), khi năng lượng đầy, Ultimate được ưu tiên: thay một từ kỹ năng **chưa gõ chữ nào và không đang khóa** (chọn từ có độ ưu tiên thấp nhất, xác định, không ngẫu nhiên ngoài RNG của sim), vẫn giữ `liveCap`, luật chữ cái đầu khác nhau và luật không tiền tố. Không bao giờ thay từ đang được gõ dở hoặc Seal/Cleanse cấp bách.
2. Nếu mọi từ đều đang khóa hoặc cấp bách, Ultimate chờ và được cấp ngay khi có chỗ.
3. Sim xác định và replay giữ nguyên (cùng seed → cùng kết quả); cập nhật golden nếu có và giải thích từng thay đổi.
4. Test hồi quy: đầy cap + Seal; đầy cap + đang khóa từ; nhiều lần đầy năng lượng liên tiếp; Ultimate ready rồi hết đợt (mất trạng thái như luật 394).

## Nghiệm thu
- `pnpm test` và typecheck sạch; lệnh tái hiện trong 394b nay cho `ultimate.kitSlot ≥ 0` và chữ hiện trên ô 5.
- Chỉ sửa `src/sim/words.ts` (và file sim liên quan trực tiếp nếu buộc phải, ghi lý do), test, golden. Không đụng `src/ui/` trừ khi test cần, không `src/lab/`. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/394c-report.md`.
