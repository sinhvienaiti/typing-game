# Hàng việc giao cho Codex

Chủ dự án yêu cầu ngày 25/10/2026: hình ảnh, âm thanh và các việc phụ giao cho Codex, để Claude giảm tải.

Thứ tự ưu tiên:
1. Tạo file ảnh trước.
2. Nhạc và âm sinh trên Mac (audio-lab). Trên Dell chỉ chuẩn bị spec và prompt.
3. 3D: viết một file yêu cầu trước, tạo model sau.

Cách chạy: [`tools/codex-run/README.md`](../tools/codex-run/README.md). Dùng model `gpt-6.1-sol`, suy luận high. Phiếu nằm ở [`docs/codex-queue/`](codex-queue/).

| # | Phiếu | Game | Loại | Trạng thái |
|---|---|---|---|---|
| 001 | [Ảnh 2D M0, đợt 1 + 3](codex-queue/001-dh-m0-images-wave1-3.md): 2 ảnh phụ, 12 prop, 8 ô đất, 4 decal, phông xa | Rồng Giữ Ải | Ảnh | **Xong** 25/10 (lần 2; lần 1 dừng vì lỗi `run.ps1`, đã sửa): 27 ảnh mới và 6 ảnh mẫu chép về đúng chỗ. Nhận xét ở `art-src/2d/README-m0-wave1-3.md`. Cần làm lại: E01-S chưa đúng góc ngang; 4 decal thiếu lề; phông xa chưa ghép liền mép; 21 ảnh lệch khổ; nền chưa đúng mã |
| 002 | [Ảnh 2D M0, đợt 4 + 5](codex-queue/002-dh-m0-images-wave4-5.md): 4 quái/tướng ×2 góc, 6 phe ta và bẫy, 20 icon | Rồng Giữ Ải | Ảnh | **Xong** 25/10: 34/34 ảnh (42 lượt tạo), nhận xét ở `games/dragon-hold/art-src/2d/README-m0-wave4-5.md`, trang xem `review-m0-wave4-5.html`. Cần duyệt: tư thế G01 và U1 chưa đúng chữ A; E25-S chưa rõ 6 chân; 31 ảnh sai khổ; nền chưa phẳng đúng mã (Tripo tự tách nền; icon sẽ chuẩn hóa bằng ImageMagick) |
| 003 | [Danh sách ảnh 2D cần dựng 3D](codex-queue/003-3d-requests-manifest.md), nhóm theo face limit và cách rig (Tripo 20 credit / tự rig Blender / không rig) | Mọi game | Tài liệu 3D | **Xong** 25/10: [`docs/games/3D_REQUESTS.md`](games/3D_REQUESTS.md). 143 lượt; rig: Tripo 3 (60 credit), Blender 25, không rig 115; Tu Tiên ghi "chờ canon" |
| 006 | [Làm lại ảnh 2D M0 chưa đạt](codex-queue/006-dh-m0-images-redo.md): E01-S, G01-F/B, U1-F/B, E25-S/F, 4 decal, phông xa | Rồng Giữ Ải | Ảnh | **Xong** 25/10: 12 ảnh làm lại (22 lượt), bản cũ giữ dạng `.v1.png`, nhận xét ở `art-src/2d/README-m0-redo.md`. E25 đã đủ 6 chân. Còn lỗi: E01-S góc cánh; tư thế G01, U1 (tự rig Blender được); decal thiếu lề và phông xa lộ đường nối (sẽ hậu kỳ bằng ImageMagick) |
| 005a | [Ảnh 2D bậc VS: nhân vật, quái, đồ cầm](codex-queue/005a-td-vs-images-characters.md), để dựng 3D sau | Lời Gọi | Ảnh | Đang chạy; có thể dừng vì hết hạn mức ChatGPT lúc 06:10. Tự chạy lại sau 08:56 (bỏ qua ảnh đã có) |
| 005b | [Ảnh 2D bậc VS: công trình, prop](codex-queue/005b-td-vs-images-buildings.md), khoảng 70 món, 2 lần chạy × 45 | Lời Gọi | Ảnh | Tự chạy sau 08:56, sau 005a |
| 007 | [Bộ prompt ảnh M0b và ảnh 2D nguồn để dựng 3D](codex-queue/007-tu-tien-art-pack-and-images.md): 2 ảnh bản sắc, Kiếm tu, 5 họ thú, tinh anh, thú tướng, Thú Vương, trận pháp, kiếm bay; mục Tu Tiên trong 3D_REQUESTS | Tu Tiên Thủ Ải | Prompt + ảnh | **Xong** 25/10: bộ prompt `docs/games/tu-tien/art-requests/m0b/` (44 prompt); 38 ảnh trong `games/immortality-cultivation/art-src/` (2 ảnh bản sắc, Kiếm tu, Thổ thể tu, bot, 5 họ thú, tinh anh, thú tướng, Thú Vương, cơ quan, trận, kiếm Thanh Phong); bảng 3D Tu Tiên 19 GLB trong `3D_REQUESTS.md`. Cần duyệt: 2 ảnh bản sắc và 3 mẫu chính; nền chưa đúng `#E6E6E6` |
| 007b | [Làm nốt ảnh M0b còn thiếu](codex-queue/007b-tu-tien-images-rest.md): Hậu Thổ Ấn, góc cạnh kiếm, Đằng Thử/Khê Viên, Hỏa Nha ngang | Tu Tiên Thủ Ải | Ảnh | Dừng lúc 06:10 vì hết hạn mức ChatGPT (mở lại 08:54). Tự chạy lại sau 08:56 bằng `.local/codex-run-after-limit.ps1` |
| 008 | [Làm lại ảnh bản sắc theo nhận xét của chủ dự án](codex-queue/008-tu-tien-identity-redo.md): nữ Kiếm tu quý phái, hoàng tộc (D47); cảnh ải đúng camera game, thấy trọn sân và triều thú (D48); ảnh nguồn kiem-tu mới | Tu Tiên Thủ Ải | Ảnh (ưu tiên) | Chờ hạn mức ChatGPT mở lại (08:56), chạy đầu tiên |
| 009 | [Chân dung concept cho cả danh sách nhân vật](codex-queue/009-tu-tien-character-roster.md): 5 trường phái × nam/nữ (D49) cộng ảnh đội hình | Tu Tiên Thủ Ải | Ảnh | Sau 008 |
| 004 | [Đưa Tu Tiên Thủ Ải vào portal, nginx, script Play](codex-queue/004-portal-tu-tien-integration.md) | Repo cha | Tích hợp | **Xong** 25/10. Claude kiểm trong WSL: `bash -n`, `node --check`, JSON, test portal 11/11, `validate-play-mode`, `validate-space-integration` đều đạt |

Mỗi lần chạy:
- Log nằm ở `.local/codex-runs/<id>/`.
- Ảnh là media, không vào Git. Chủ dự án sao lưu bằng `pnpm media:push`, sau khi chạy `pnpm media:setup` trên máy.
- Claude xem báo cáo `last.md`, nhìn thử một số ảnh, rồi cập nhật bảng này.
