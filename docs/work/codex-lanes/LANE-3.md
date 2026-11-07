# LANE-3 · Media: KTX2 bộ hệ, giữ-chỉnh từng clip, Blender (sau duyệt)

Chạy bằng `lane-runner.md`. **Cổng:** A = anh duyệt.

| # | Việc | Phiếu | Mức | Cần xong trước | Cổng | Trạng thái | Đầu ra |
|---|---|---|---|---|---|---|---|
| 1 | A5 KTX2 cho bộ 14 hệ và thư mục chiêu | `lane-A5-ktx2-element-kits.md` | medium | — | | doing | |
| 2 | Giữ-chỉnh: lặp mỗi lần một dòng `todo` của `stream-1-keep.md` | `lane-S1-step.md` | high | 1 | | todo (lặp) | |
| 3 | KTX2 cho các bản dẫn xuất `vfx-redo-2026-11-07/keep/` (lặp khi có thêm) | `lane-A5-ktx2-element-kits.md` (áp cho thư mục keep) | medium | 2 | | todo (lặp) | |
| 4 | Anh duyệt mẫu Blender (tia có hướng, khói có sợi; `laneS3-report.md`) | — | — | — | A | todo (anh) | |
| 5 | Blender: lặp mỗi lần một dòng `todo` của `stream-3-blender.md` | `lane-S3b-blender-row.md` | high | 4 | A | todo (lặp) | |

**Ghi chú cho runner:** việc lặp giữ `todo (lặp)` cho tới khi danh sách nguồn hết dòng `todo`, rồi đổi thành `done`. Giữa hai việc lặp, ưu tiên việc số nhỏ hơn.
