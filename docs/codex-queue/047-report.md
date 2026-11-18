# Phiếu 047 · Báo cáo trạng thái GLB đợt 2

Ngày cập nhật: 28/10/2026. Đã cập nhật 143 ô trạng thái ở §3 và tóm tắt §1 của `docs/games/3D_REQUESTS.md`.

## Đếm trước và sau

| Game | Trước cập nhật | Sau cập nhật |
|---|---|---|
| Rồng Giữ Ải | 24 `có GLB` (20 ô ghi gọn, 4 ô kèm ghi chú) | 24 `có GLB` |
| Lời Gọi | 31 `có GLB`; 86 `có ảnh · đợt 2 Tripo (chủ dự án đang dựng)` | 116 `có GLB` (31 đợt 1, 85 đợt 2); 1 thiếu GLB (`cannon-kit-l2`) |
| Tuyến Cuối | 1 `có GLB`; 1 dùng chung `rainbow-tank` | 1 `có GLB`; 1 dùng chung `rainbow-tank` |
| **Tổng** | **143** | **143** |

Trong 86 mã duy nhất ở bảng nhập có 85 GLB và `loigoi_cannon-kit-l2` thiếu GLB. Bảng nhập có thêm một dòng GLB cầu tàu dự phòng (`tripo-spares/cau-tau.alt.glb`); đây là bản trùng, không phải model thứ 86. Theo 85 GLB thuộc bộ model được nhập, mức chấm là **44 Đạt, 41 Tạm chấp nhận**. Bảng nhập có 45 dòng mang mức Đạt nếu tính cả bản cầu tàu dự phòng.

## Ghi chú cũ được giữ

- `thorn-wasp`: ghi chú 015 về Left chưa đạt; giữ Front, không yêu cầu tạo lại GLB.
- `moss-grunt`: có Front, thiếu Back.
- `moss-warden`: ghi chú 015 về hai lượt Front chưa đạt; không sinh Back mới theo ảnh chưa đạt.
- `rainbow-scout`, `rainbow-tank`: ghi chú 015 giữ nguyên nguồn Space dùng chung.
- `moss-banner`: ghi chú 015 về ảnh Front chưa đạt; giữ Blender, không sinh Back mới hoặc model trùng.
- `barracks`: ghi chú 015 về `barracks-v2.png`, prompt và rig cổng Blender.
- `draconis`: giữ ghi chú 015 xác nhận đủ Front/Left/Back, prompt và `guides/draconis-v4`; bỏ phần trạng thái đợt 2 cũ đã lỗi thời.

## Kết quả bốn lệnh kiểm

1. Chạy lại phép tính Node theo mã model, đích GLB và file có trên đĩa: **143 dòng; lệch 0**. Đếm sau: Rồng 24 GLB; Lời Gọi 116 GLB + 1 thiếu GLB; Tuyến Cuối 1 GLB + 1 dùng chung. Mức của 85 GLB đợt 2: **44 Đạt, 41 Tạm chấp nhận**.
2. Bảng đếm: **tổng 143**, Rồng 24 GLB; Lời Gọi 116 GLB (31 cũ + 85 đợt 2) và 1 thiếu `cannon-kit-l2`; Tuyến Cuối 1 GLB + 1 dùng chung. Khớp các mốc yêu cầu.
3. `git diff --word-diff -- docs/games/3D_REQUESTS.md`: thay đổi chỉ ở ô cuối của §3 và đoạn trạng thái đầu §1. Node so chín ô còn lại với bản trước: **vi phạm 0 trên 143 dòng**.
4. `git status --short`: ngoài các thay đổi có sẵn trước phiên, chỉ có `M docs/games/3D_REQUESTS.md` và `?? docs/codex-queue/047-report.md`; không có đường dẫn khác phát sinh.
