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
| 005a | [Ảnh 2D bậc VS: nhân vật, quái, đồ cầm](codex-queue/005a-td-vs-images-characters.md), để dựng 3D sau | Lời Gọi | Ảnh | Dừng lúc 06:10 vì hết hạn mức ChatGPT. Xếp lại trong `.local/codex-run-after-limit.ps1`, sau 007b (bỏ qua ảnh đã có) |
| 005b | [Ảnh 2D bậc VS: công trình, prop](codex-queue/005b-td-vs-images-buildings.md), khoảng 70 món, 2 lần chạy × 45 | Lời Gọi | Ảnh | Sau 005a, cùng hàng chờ |
| 007 | [Bộ prompt ảnh M0b và ảnh 2D nguồn để dựng 3D](codex-queue/007-tu-tien-art-pack-and-images.md): 2 ảnh bản sắc, Kiếm tu, 5 họ thú, tinh anh, thú tướng, Thú Vương, trận pháp, kiếm bay; mục Tu Tiên trong 3D_REQUESTS | Tu Tiên Thủ Ải | Prompt + ảnh | **Xong** 25/10: bộ prompt `docs/games/tu-tien/art-requests/m0b/` (44 prompt); 38 ảnh trong `games/immortality-cultivation/art-src/` (2 ảnh bản sắc, Kiếm tu, Thổ thể tu, bot, 5 họ thú, tinh anh, thú tướng, Thú Vương, cơ quan, trận, kiếm Thanh Phong); bảng 3D Tu Tiên 19 GLB trong `3D_REQUESTS.md`. Cần duyệt: 2 ảnh bản sắc và 3 mẫu chính; nền chưa đúng `#E6E6E6` |
| 007b | [Làm nốt ảnh M0b còn thiếu](codex-queue/007b-tu-tien-images-rest.md): Hậu Thổ Ấn, góc cạnh kiếm, Đằng Thử/Khê Viên, Hỏa Nha ngang | Tu Tiên Thủ Ải | Ảnh | Dừng lúc 06:10 vì hết hạn mức ChatGPT. Xếp lại sau 009 |
| 008 | [Làm lại ảnh bản sắc theo nhận xét của chủ dự án](codex-queue/008-tu-tien-identity-redo.md): nữ Kiếm tu quý phái, hoàng tộc (D47); cảnh ải đúng camera game, thấy trọn sân và triều thú (D48); ảnh nguồn kiem-tu mới | Tu Tiên Thủ Ải | Ảnh (ưu tiên) | **Xong** 25/10: 6 ảnh mới, bản cũ giữ `.v1.png`. **Chủ dự án duyệt:** chân dung A (miện ngọc) là chuẩn phong cách; cảnh 55° là góc camera mặc định. Còn: nền nguồn chưa đúng `#E6E6E6`, tay cần mở thêm trước Tripo |
| 009 | [Chân dung concept cho cả danh sách nhân vật](codex-queue/009-tu-tien-character-roster.md): 5 trường phái × nam/nữ (D49) cộng ảnh đội hình | Tu Tiên Thủ Ải | Ảnh | Đang chạy từ 09:23 25/10 (4/11 ảnh lúc 09:35) |
| 010a | [Môi trường và kết cấu VFX](codex-queue/010a-tu-tien-environment-vfx.md): 6 ô đất, 8 decal, 3 lớp phông, 6 cỏ bụi, 18 VFX | Tu Tiên Thủ Ải | Ảnh + hậu kỳ | Làn A: tự chạy sau hàng chờ hiện tại (`queue.ps1`, `.local/codex-lane-a.txt`) |
| 010b | [Biểu tượng](codex-queue/010b-tu-tien-icons.md): 35 cái (chiêu Kiếm, Thổ thể, đan phù, cơ quan, tiền, Đạo Quả, cảnh giới) | Tu Tiên Thủ Ải | Ảnh + hậu kỳ | Làn A, sau 010a |
| 010c | [Màn tựa, Sơn Môn, khung giao diện, Tĩnh Tu](codex-queue/010c-tu-tien-ui-hub-tinh-tu.md): 25 ảnh, có số cắt 9-slice | Tu Tiên Thủ Ải | Ảnh + hậu kỳ | Làn A, sau 010b |
| 012 | [Công cụ hậu kỳ ảnh `tools/art-normalize`](codex-queue/012-art-normalize-tool.md) và xử lý ảnh Rồng Giữ Ải còn lỗi (lề decal, mép phông, icon, nền ảnh nguồn Tripo) | Mọi game, Rồng Giữ Ải | Công cụ + hậu kỳ | Làn B: đang chạy từ 09:38 25/10 |
| 011 | [Phản biện độc lập lượt sửa 2 của 1B R2](codex-queue/011-td-r2-fix2-review.md): đối chiếu changelog với diff, chạy lại `check`, `golden`, balance nhanh, kịch bản chunk | Lời Gọi | Phản biện (chỉ đọc) | Làn B, sau 012 |
| 004 | [Đưa Tu Tiên Thủ Ải vào portal, nginx, script Play](codex-queue/004-portal-tu-tien-integration.md) | Repo cha | Tích hợp | **Xong** 25/10. Claude kiểm trong WSL: `bash -n`, `node --check`, JSON, test portal 11/11, `validate-play-mode`, `validate-space-integration` đều đạt |

**Danh sách toàn bộ ảnh Tu Tiên** (159 ảnh, chia lô, có trạng thái): [`docs/games/tu-tien/art-requests/IMAGE_LIST.md`](games/tu-tien/art-requests/IMAGE_LIST.md).

**Hai làn chạy song song** (từ 25/10):
- **Làn A** là ảnh: hàng chờ cũ `.local/codex-run-after-limit.ps1` (009 → 007b → 005a → 005b), rồi `.local/codex-lane-a.txt` (010a → 010b → 010c).
- **Làn B** là việc khác: `.local/codex-lane-b.txt` (012 → 011).
- `tools/codex-run/queue.ps1` chạy từng danh sách. Khi gặp hạn mức ChatGPT, nó tự chờ tới giờ Codex báo rồi chạy lại phiếu đó.
- Phiếu nào cần gọi WSL (ImageMagick, git, pnpm) thì chạy với `-Sandbox danger-full-access`.

Mỗi lần chạy:
- Log nằm ở `.local/codex-runs/<id>/`.
- Ảnh là media, không vào Git. Chủ dự án sao lưu bằng `pnpm media:push`, sau khi chạy `pnpm media:setup` trên máy.
- Claude xem báo cáo `last.md`, nhìn thử một số ảnh, rồi cập nhật bảng này.
