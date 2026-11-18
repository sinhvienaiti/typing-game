# Phiếu 400: Hiệu ứng vòng đời chữ trên dải kỹ năng (xuất hiện, đang gõ, gõ xong)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11/2026: "từ typing sau khi typing sẽ kiểu dạng rụng xuống hoặc bay lên với hiệu ứng bị ẩn dần để nó không gây vướng cho game… khi các từ xuất hiện, nó sẽ như nào, khi typing nó sẽ ra sao, khi typing xong nó sẽ như nào". Bố cục mới đã dựng ở phiếu 394 (`394-report.md`): dải kỹ năng ở đáy, `src/ui/ban-quyet.ts`. Bản chốt: `docs/games/tu-tien/TYPING_GAMEPLAY_DECISION.md` mục 6 và "Owner chốt". Phản hồi gõ chữ là **hệ dùng chung, chuẩn 9** (`docs/games/SHARED_SYSTEMS_BAR.md`).

## Việc (trong `games/immortality-cultivation/`, nhánh hiện tại)
1. **Xuất hiện:** từ mới vào ô hiện dần trong khoảng 180–250 ms, từng chữ cái so le 1–2 khung, chữ đầu được nhấn nhẹ. Từ khác trên dải đứng yên, dễ đọc.
2. **Đang gõ (chỉ từ đang khóa chuyển động):** chữ đúng chuyển màu vàng kim và nảy nhẹ (scale ≤ 1,12, ≤ 90 ms); chữ kế tiếp có gạch dưới sáng; gõ sai thì viền lóe đỏ 150 ms và rung ngang ≤ 3 px, không đẩy layout. Từ đang hồi chiêu mờ, có vòng đếm, không gạch dưới.
3. **Gõ xong:** cả từ lóe sáng trong ≤ 50 ms (cùng khung với lúc phát chiêu, không giữ chiêu lại), rồi tách từng chữ: từ tấn công **bay lên** về hướng chiêu, từ phòng thủ **rơi xuống** nhẹ, mờ hẳn trong khoảng 0,5–0,6 s, có vài hạt sáng nhỏ (mỗi kênh ≤ 0,9). Ô hiện từ mới sau khi từ cũ đã tan. Chữ bay không được che lõi, cổng, ô trụ hay cảnh báo.
4. Chế độ giảm chuyển động (`reduced motion` của game hoặc trình duyệt): bỏ bay/rơi, chỉ mờ dần.
5. Hiệu năng: chỉ dùng `transform` và `opacity` (không đổi layout), hoặc một canvas overlay; không tạo phần tử DOM mới mỗi phím cho hạt — dùng pool. Âm gõ và âm phát chiêu giữ nguyên.

## Nghiệm thu
- `pnpm test` và typecheck sạch; test cho: thứ tự trạng thái, phím→phát chiêu không trễ thêm, chế độ giảm chuyển động.
- Clip ngắn ở 1280×720 và 1920×1080 (gõ một từ tấn công, một từ phòng thủ, một lần gõ sai) trong `typing-game-review/owner-review/2026-11-16/tu-tien/word-fx/` có `ABOUT.md`; nếu sandbox chặn trình duyệt, ghi rõ và để lệnh chụp cho Claude.
- Chỉ sửa `src/ui/ban-quyet.ts`, `src/ui/styles/`, file mới trong `src/ui/`, và test. Không đụng `src/lab/`, `src/view/ground.ts`, bản đồ. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/400-report.md`.
