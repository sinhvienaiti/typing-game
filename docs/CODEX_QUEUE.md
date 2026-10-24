# Hàng việc giao cho Codex

Chủ dự án yêu cầu ngày 25/10/2026: hình ảnh, âm thanh và các việc phụ giao cho Codex, để Claude giảm tải.

Thứ tự ưu tiên:
1. Tạo file ảnh trước.
2. Nhạc và âm sinh trên Mac (audio-lab). Trên Dell chỉ chuẩn bị spec và prompt.
3. 3D: viết một file yêu cầu trước, tạo model sau.

Cách chạy: [`tools/codex-run/README.md`](../tools/codex-run/README.md). Dùng model `gpt-6.1-sol`, suy luận high. Phiếu nằm ở [`docs/codex-queue/`](codex-queue/).

| # | Phiếu | Game | Loại | Trạng thái |
|---|---|---|---|---|
| 001 | [Ảnh 2D M0, đợt 1 + 3](codex-queue/001-dh-m0-images-wave1-3.md): 2 ảnh phụ, 12 prop, 8 ô đất, 4 decal, phông xa | Rồng Giữ Ải | Ảnh | Đang chạy (25/10) |
| 002 | [Ảnh 2D M0, đợt 4 + 5](codex-queue/002-dh-m0-images-wave4-5.md): 4 quái/tướng ×2 góc, 6 phe ta và bẫy, 20 icon | Rồng Giữ Ải | Ảnh | Chờ 001 |
| 003 | [Danh sách ảnh 2D cần dựng 3D](codex-queue/003-3d-requests-manifest.md), nhóm theo face limit và cách rig (Tripo 20 credit / tự rig Blender / không rig) | Mọi game | Tài liệu 3D | Đang chạy (25/10) |

Mỗi lần chạy:
- Log nằm ở `.local/codex-runs/<id>/`.
- Ảnh là media, không vào Git. Chủ dự án sao lưu bằng `pnpm media:push`, sau khi chạy `pnpm media:setup` trên máy.
- Claude xem báo cáo `last.md`, nhìn thử một số ảnh, rồi cập nhật bảng này.
