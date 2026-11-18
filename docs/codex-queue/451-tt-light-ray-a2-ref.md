# Phiếu 451 — Tia quạt Ánh Sáng (hướng A2), vẽ lại có ảnh tham chiếu

Phản biện: PASS (Sonnet, 18/11)

## Bối cảnh
Owner 18/11 chọn hướng **A2 soft beam** (tia sáng mềm từ nguồn) để thay lớp `FanBeams` đang vẽ bằng code, và yêu cầu vẽ lại **có ảnh tham chiếu** (bản Firefly cũ chỉ dùng chữ, sai luật). Mẫu hướng: `typing-game-review/owner-review/2026-11-18/tu-tien/light-art-parts/sheet-light-art-parts.jpg` (ô A2).

## Việc
Dùng công cụ `image_gen`, đúng 3 lần (3 biến thể).
Ảnh tham chiếu (chỉ ảnh dự án; ghi đường dẫn vào prompt): `games/immortality-cultivation/art-src/concept/ult-storyboards/light-storyboard.v1-try1.png` (ô trên phải: quạt tia vàng từ thấu kính); `games/immortality-cultivation/art-src/concept/ult-light/ult-light-moment-a.v1-try1.png` (màu, chất liệu).
Mỗi ảnh 2048×512 (ngang), nền đen tuyền: **một** tia sáng nằm ngang, gốc sáng ở mép trái (khoảng 8 % bề ngang), thân thuôn dài sang phải và tan mềm ở 90 %; lõi trắng ấm mảnh, quầng hổ phách mềm, vài hạt lấp lánh dọc tia; không vẽ nguồn sáng, kính hay chữ; lề trên dưới ≥ 25 %.
- A: thẳng, quầng mỏng. B: quầng dày hơn, lõi sáng hơn. C: có 2 sợi sáng mảnh chạy dọc hai bên lõi.
Lưu `games/immortality-cultivation/art-src/lab/vfx/light/stills/light-ray-a2.v1-try<k>.png` + `.prompt.txt`; tờ ghép `light-ray-a2-451.jpg` (để ở `/private/tmp/typing-game-451/` nếu không ghi được thư mục review).

## Ràng buộc
Không sửa code, không video, không xoá/ghi đè ảnh có sẵn, không commit, không đổi nhánh. Không dùng ảnh game khác.

## Giao nộp
`docs/codex-queue/451-report.md`.
