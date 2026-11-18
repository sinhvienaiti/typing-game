# Phiếu 409: Chuyển hết chữ người chơi đọc sang tiếng Anh (menu, kết quả, ôn tập)


Phản biện: PASS (Sonnet, 16/11)
## Bối cảnh
Luật owner 28/10/2026 (AGENTS.md, "Language, names and art level"): mọi chữ người chơi đọc là tiếng Anh, kể cả danh từ trong game; tiếng Việt chỉ còn ở nghĩa của từ đang học và chú giải trong khung học. Phiếu 394 ghi menu, kết quả và ôn tập còn tiếng Việt. Tên riêng nhân vật giữ nguyên.

## Việc (trong `games/immortality-cultivation/`)
1. Tìm mọi chuỗi người chơi thấy còn tiếng Việt trong `src/ui/` (ví dụ `menu.ts`, `results.ts`, `review-card.ts`, `wave-card.ts`, `word-book.ts`, `hud.ts`, `shop-*`) và `src/app/`. Lập bảng: file, chuỗi cũ, chuỗi tiếng Anh mới.
2. Dịch sang tiếng Anh ngắn, rõ, hợp giọng game tu tiên thương mại (ví dụ "Chân Nguyên" → "Qi", "Đợt" → "Wave", "Cửa hàng" → "Shop"). Giữ nguyên: nghĩa tiếng Việt của từ đang học, chú giải trong khung học, tên riêng (Lam, Thanh Thạch Ải nếu là địa danh riêng thì ghi "Thanh Thach Pass" theo canon nếu canon có; không có thì giữ và ghi vào báo cáo).
3. Không đổi luật, số hay bố cục; nếu chữ tiếng Anh dài hơn làm vỡ ô, rút gọn chữ chứ không đổi layout.

## Nghiệm thu
- `pnpm test` và typecheck sạch; cập nhật test chụp chuỗi nếu có.
- Báo cáo có bảng đối chiếu đầy đủ và danh sách chuỗi cố ý giữ tiếng Việt kèm lý do.
- Chỉ sửa chuỗi trong `src/ui/`, `src/app/`, `src/content/` (nhãn hiển thị) và test. Không đụng `src/sim/` logic, `src/lab/`. Không commit, không đổi nhánh.

## Giao nộp
`docs/codex-queue/409-report.md`.
