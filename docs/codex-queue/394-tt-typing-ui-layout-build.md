# Phiếu 394: Dựng bố cục UI chơi gõ chữ theo bản chốt 16/11


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Owner 16/11/2026 chê UI che kín sân (ảnh `typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-research/owner-screenshot-current-ui.webp`). Bản chốt: `docs/games/tu-tien/TYPING_GAMEPLAY_DECISION.md`, **mục "Owner chốt" ở cuối file thắng mọi chỗ khác**. Phân tích nền: `392-report.md`, `392b-report.md`.

## Việc (trong `games/immortality-cultivation/`, nhánh hiện tại, không đổi nhánh)
1. **Gỡ hẳn thẻ "Học trước · Từ mới của trận"** (`src/ui/learn-ahead.ts` và chỗ gọi): không tự bật, không phím mở. Owner: "vô nghĩa, đừng có đem mấy cái không phù hợp vào game". Giữ dữ liệu hồ sơ học; từ mới chỉ gặp trên ô kỹ năng trong trận, với một dòng nghĩa nhỏ cho từ đang khóa.
2. **Chiến đấu thoáng sân:** dải kỹ năng thấp ở đáy (`ban-quyet.ts`), chữ ≥ 28 px; thanh trạng thái mỏng (máu, năng lượng, đợt) ở mép trên/cạnh; không panel nào giữa sân. Mục tiêu đo: UI che ≤ 17 % khung 1280×720 và 1920×1080 lúc đánh căng nhất, không đè lõi, cổng, ô trụ, cảnh báo. Đo bằng DOM rect, ghi số trước/sau.
3. **Cửa hàng và đặt trụ chỉ giữa các đợt** (`shop-mode.ts`, `shop-strip.ts`): ngăn kéo cạnh phải, tự đóng khi bắt đầu đợt; trong đợt không hiện.
4. **Quái:** không nhãn từ trên đầu. Quái tinh anh và boss có icon nhận biết (dùng icon art có sẵn trong game; nếu không có, ghi trong báo cáo, không vẽ bằng CSS/emoji). Thanh máu chỉ hiện khi quái đã dính sát thương, ẩn khi đầy; vẽ chung bằng một instanced mesh (≤ 2 draw call cho mọi thanh), không mỗi quái một phần tử HTML.
5. **Tuyệt kỹ:** gõ xong từ → "Ultimate ready · Space", Space để tung; không thanh/vòng canh nhịp (owner bỏ ý Audition). Không mục tiêu thì báo "No target", không mất năng lượng; mất trạng thái sẵn sàng khi hết đợt hoặc chết; không nhận Space bấm trước khi gõ xong.
6. Chữ người chơi đọc là tiếng Anh; ghi chỗ còn tiếng Việt chưa đổi.

## Nghiệm thu
- `pnpm test` và typecheck sạch; thêm test cho: không còn learn-ahead, Space tuyệt kỹ, thanh máu ẩn/hiện.
- Ảnh chụp trước/sau ở 1280×720 và 1920×1080 lúc chuẩn bị và lúc đánh, kèm % che, trong `typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-build/` có `ABOUT.md`. Nếu sandbox chặn trình duyệt, ghi rõ và để lại lệnh chụp cho Claude.
- Không đụng `src/lab/`, `view/ground.ts` và bản đồ. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/394-report.md`.
