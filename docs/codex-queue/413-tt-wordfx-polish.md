# Phiếu 413: Hoàn thiện nhỏ sau 406b (test làm tròn, hạt sáng, comment, màn kết quả/ôn tập)


Phản biện: PASS (Sonnet, 16/11; sửa phạm vi theo phản biện vòng 1)
## Bối cảnh
Agent Claude kiểm 409 + 406b (16/11):
- 23/24 test đạt; `tests/ui/word-fx.test.ts:99` hỏng vì làm tròn (4.000000000000001 > 4);
- hạt sáng khi từ tấn công bay lên vẫn nhỏ và mờ;
- hai comment còn ghi "HOÀN HẢO";
- màn kết quả và màn ôn tập chưa được xác nhận đã sang tiếng Anh;
- biên độ bay chưa có số đo trong dữ liệu chụp.

## Việc (trong `games/immortality-cultivation/`)
1. Sửa test dòng 99: so sánh có dung sai (hoặc kẹp giá trị trong code) — không nới giới hạn thật.
2. Hạt sáng: to và sáng hơn để nhìn rõ ở 1280×720 (mỗi kênh vẫn ≤ 0,9), 6–10 hạt mỗi từ, tắt cùng chữ.
3. Ghi biên độ bay/rơi thực (px) vào JSON mà script chụp `tests/ui/word-fx-capture.mjs` xuất ra, để đo được 80–110 px (tấn công) và 50–80 px (phòng thủ).
4. Đổi comment "HOÀN HẢO" ở `src/view/hitfx.ts:328` sang tiếng Anh (chỉ comment, không đổi code); nhãn trong `src/kit/feedback/profiles.ts` là kit dùng chung, không sửa. Kiểm bằng test hoặc grep rằng màn kết quả (`results.ts`) và ôn tập (`review-card.ts`) không còn chuỗi tiếng Việt ngoài nghĩa từ học.

## Nghiệm thu
- `pnpm test` toàn bộ đạt; typecheck sạch.
- Chỉ sửa `src/ui/`, `src/view/feedback-profile.ts`, comment ở `src/view/hitfx.ts:328`, `tests/ui/word-fx-capture.mjs`, test. Không sửa `src/kit/`, `src/sim/`, `src/lab/`. Không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/413-report.md`.
