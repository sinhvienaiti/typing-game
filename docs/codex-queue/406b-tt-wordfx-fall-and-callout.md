# Phiếu 406b: Chữ phòng thủ rơi ra khỏi màn hình; câu "HOÀN HẢO" còn tiếng Việt; hạt sáng quá mờ


Phản biện: PASS (Sonnet, 16/11; 406b sau khi sửa phạm vi kit)
## Bối cảnh
Agent Claude chụp kiểm 406 (16/11): ở 1280×720 từ phòng thủ rơi quá đáy màn hình và bị cắt (`typing-game-review/owner-review/2026-11-16/tu-tien/word-fx/406-defence-1280x720-strip.jpg`); từ tấn công chỉ bay 60–75 px (dưới 70–110 px của phiếu 406) và hạt sáng gần như không thấy; câu thông báo chiến đấu "HOÀN HẢO" còn tiếng Việt (luật: chữ người chơi đọc là tiếng Anh). Chạy sau 409 trong cùng làn (đọc lại file, giữ phần dịch của 409).

## Việc (trong `games/immortality-cultivation/`)
1. Từ phòng thủ: rơi 50–80 px nhưng luôn nằm trong khung ở cả 1280×720 và 1920×1080 (kẹp theo cạnh dưới viewport, hoặc rơi ngắn hơn khi dải ở sát đáy), nảy nhẹ một lần, mờ trong 0,55–0,7 s.
2. Từ tấn công: bay 80–110 px đo được bằng test, theo đường cong; hạt sáng nhìn rõ (lớn hơn, sáng hơn, mỗi kênh ≤ 0,9) và tắt cùng chữ.
3. "HOÀN HẢO" nằm trong `src/kit/feedback/profiles.ts` (dòng 51). `src/kit/**` là bản sao của `shared/game-kit`, **không được sửa tay** (AGENTS.md của game). Ghi đè nhãn ở phía game: truyền nhãn tiếng Anh ("PERFECT") qua cấu hình hoặc profile riêng của game trong `src/ui/` hoặc `src/view/feedback-profile.ts`, không sửa kit. Nếu kit không cho ghi đè, dừng phần này và ghi rõ trong báo cáo (cần phiếu sửa kit dùng chung, chuẩn 9). Kiểm thêm bằng grep chữ có dấu tiếng Việt trong `src/ui/` ngoài nghĩa từ học.
4. Giữ ≤ 50 ms phím→phát chiêu và chế độ giảm chuyển động.

## Nghiệm thu
- `pnpm test` và typecheck sạch; test cho biên độ bay/rơi và kẹp trong viewport.
- Để lệnh chụp cho Claude. Chỉ sửa `src/ui/`, `src/view/feedback-profile.ts` và test; không sửa `src/kit/`. Không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/406b-report.md`.
