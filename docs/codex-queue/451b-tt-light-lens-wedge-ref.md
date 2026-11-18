# Phiếu 451b: Thấu kính và vệt quạt trên đất của chiêu Ánh Sáng, vẽ lại có ảnh tham chiếu

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Bảng `typing-game-review/owner-review/2026-11-18/tu-tien/light-art-parts/sheet-light-art-parts.jpg` có các ô B1 (thấu kính viền ngọc chạm bạc), B2 (thấu kính gương mặt trời) và C1 (vệt quạt sáng trên đất). Các ô này được vẽ bằng Firefly chỉ từ chữ, không có ảnh tham chiếu, nên sai luật. Owner chưa chọn ô nào, nên phải vẽ lại có tham chiếu để owner chọn.

Thấu kính sẽ thay vật thể `HeldLens` đang dựng bằng khối hình học trong code (xem `docs/work/tasks/vfx-code-drawn-audit.md`, mục Q3). Sau khi owner chọn, ảnh thấu kính sẽ dùng làm nguồn cho Tripo.

## Việc
Dùng công cụ `image_gen`, tối đa 5 lần.

Ảnh tham chiếu, chỉ dùng ảnh của dự án và ghi đường dẫn vào mỗi prompt:
- `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png`: thấu kính và quạt tia.
- `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png`: màu và chất liệu.

1. **Thấu kính, 2 ảnh (`light-lens-b1`, `light-lens-b2`).**
   - Kích thước 1024×1024. Nền xám trơn, ánh sáng đều, không đổ bóng. Góc nhìn 3/4 từ trước. Vật nằm trọn trong khung, lề ≥ 8 %.
   - Thấu kính tròn cầm tay có vành dày và một cán.
   - B1: vành ngọc bích chạm bạc.
   - B2: vành vàng hình mặt trời có tia.
   - Mặt kính đặc màu hổ phách nhạt, không trong suốt (để Tripo dựng được khối).
   - Không hào quang, không tia sáng, không chữ.
2. **Vệt quạt trên đất, 3 ảnh (`light-ground-wedge`, try1 đến try3).**
   - Kích thước 1024×1024, nền đen tuyền, nhìn thẳng từ trên xuống 90° (đây là mặt phẳng đặt trên đất).
   - Một hình quạt sáng mở khoảng 60°, đỉnh quạt ở giữa mép dưới. Sáng nhất gần đỉnh, mờ dần ra mép cong.
   - Màu vàng ấm và hổ phách. Bên trong có vân chữ cổ hoặc hoa văn sen rất mờ.
   - Mép tan mềm, không có viền cứng, lề ≥ 6 %.
   - Ba biến thể: A trơn, B có vân sen, C có tia mảnh tỏa ra từ đỉnh quạt.

Lưu ảnh ở `games/immortality-cultivation/art-src/lab/vfx/light/stills/<tên>.v1-try<k>.png`, mỗi ảnh kèm `.prompt.txt`. Ghép tất cả thành một tờ `light-lens-wedge-451b.jpg`; nếu không ghi được thư mục review thì để ở `/private/tmp/typing-game-451b/`.

## Ràng buộc
Không sửa code, không làm video, không xoá hay ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh của game khác.

## Giao nộp
`docs/codex-queue/451b-report.md`.
