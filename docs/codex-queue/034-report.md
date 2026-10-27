# Phiếu 034 · Báo cáo cập nhật trạng thái model

Ngày cập nhật: 28/10/2026. Tổng cộng 143 dòng model trong §3.

## Đếm trước và sau

| Game | Trước cập nhật | Sau cập nhật |
|---|---|---|
| Rồng Giữ Ải | 13 `chờ ảnh`; 1 `chờ ảnh` có ghi chú Front/Back; 7 `có`; 3 dòng có ghi chú 015 | 24 `có GLB`; các trạng thái ảnh/đợt 2/chờ ảnh: 0 |
| Lời Gọi | 115 `chờ ảnh`; 2 dòng có ghi chú 015 | 31 `có GLB`; 86 `có ảnh · đợt 2 Tripo (chủ dự án đang dựng)`; `có ảnh`: 0; `chờ ảnh`: 0 |
| Tuyến Cuối | 2 `Có`, đều có ghi chú 015 | 1 `có GLB`; 1 dùng chung model `rainbow-tank`; trạng thái ảnh/đợt 2/chờ ảnh: 0 |
| **Tổng** | **143** | **143** |

Sổ model 025 đối chiếu: `tools/map-factory/registry/out/assets.<game>.json`, mục `assets` với `source: "original"`. Tất cả GLB được tính trong bảng đều tồn tại tại đường dẫn ghi ở cột GLB và khớp registry.

## Ghi chú cũ được giữ

- `thorn-wasp`: ghi chú 015 về ảnh Left chưa đạt; giữ Front, không yêu cầu tạo lại.
- `moss-grunt`: có Front, thiếu Back.
- `moss-warden`: ghi chú 015 về hai lượt Front chưa đạt và không sinh Back mới.
- `rainbow-scout`, `rainbow-tank`: ghi chú 015 giữ nguyên nguồn chung Space.
- `moss-banner`: ghi chú 015 về góc ảnh chưa đạt và không sinh Back/model trùng.
- `barracks`: ghi chú 015 về `barracks-v2.png`, prompt và rig cổng Blender.
- `draconis`: ghi chú 015 xác nhận đủ Front/Left/Back, prompt và nguồn `guides/draconis-v4`.

## Kết quả bốn lệnh kiểm

1. Chạy lại Node đối chiếu từng trạng thái: **143 dòng; lệch 0**. Đếm ra Rồng 24 GLB; Lời Gọi 31 GLB + 86 đợt 2; Tuyến Cuối 1 GLB + 1 dùng chung.
2. Bảng đếm: **tổng 143**, các mốc theo game khớp đúng yêu cầu.
3. `git diff --word-diff -- docs/games/3D_REQUESTS.md`: thay đổi chỉ nằm ở ô trạng thái cuối của §3 và đoạn trạng thái mới §1. Node so từng ô ngoài cột cuối giữa bản đầu và bản mới: **vi phạm 0** (143 dòng).
4. `git status --short`: so với trạng thái đầu phiên, chỉ phát sinh `M docs/games/3D_REQUESTS.md` và `?? docs/codex-queue/034-report.md`. Các thay đổi khác đã có từ trước được giữ nguyên.

## Claude duyệt (28/10/2026)

- **Tính lại độc lập bằng script riêng:** 143 dòng; 0 dòng lệch trạng thái.
  - Rồng: 24 có GLB.
  - Lời Gọi: 31 có GLB, 86 đợt 2.
  - Tuyến Cuối: 1 có GLB, 1 dùng chung.
- **Mọi ô ngoài cột cuối giữ nguyên:** 0 vi phạm trên 147 dòng bảng.
- **Model:** phiếu chạy bằng `gpt-6-luna` medium trong 2 phút, đúng ngay lần đầu. Lần thử đầu tiên của model này trên tài khoản cho thấy nó dùng được cho việc vặt có kiểm rõ.
