# Phiếu 433s: báo cáo (Claude làm thay Codex)

18/11/2026. Owner chọn "Tia nứt rõ hơn": tương phản tia nứt so với bụi ≥ 2,5 ở **cả 6** khung Alt+1, không chỉ trung vị.

## Đã sửa (`games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`)
- **Số tia quanh kiếm lớn:** 4–7 → **6–8** tia cùng lúc (`ARC_GIANT` 7 → 8 để không chồng slot tia của kiếm con).
- **Cỡ tia:** 1,3× → **1,6×** (đồng đều). Tint giữ (0,8; 0,88; 0,9), opacity giữ 1,0.
- **Làm tối bụi cục bộ sau tia:** mỗi tia có một làn khói `disc-smoke-01` (ảnh bụi có sẵn, khung 12) tint đen, 1,5× rộng, 0,85× cao, opacity 0,6, NormalBlending, vẽ ngay trước tia (renderOrder 10,45), cùng thời điểm sống với tia. Không tạo hình mới, không blur, không mask.
  - Đã thử dùng chính khung tia làm bóng: atlas tia có ô nền đen đặc nên ra hình chữ nhật đen. Đã bỏ.
- Không đổi: mặt kiếm lớn, màu bụi (0,38; 0,41; 0,47), sóng A, nứt B, hào quang.

## Tương phản tia/bụi, Alt+1 (cách đo giống 433r: có/không lớp tia, điểm tia sáng lên ≥ 0,1, bụi = điểm ít màu trong 12 px quanh tia; bóng tối vẫn bật khi đo bụi vì người chơi thấy nó)

| Thời điểm | 433r | 433s | Sáng tia | Sáng bụi |
| --- | --- | --- | --- | --- |
| 7,95 s | 3,13 | **2,93** | 0,544 | 0,186 |
| 8,05 s | 2,42 | **2,73** | 0,485 | 0,178 |
| 8,20 s | 2,36 | **2,61** | 0,476 | 0,183 |
| 8,35 s | 1,86 | **2,59** | 0,548 | 0,212 |
| 8,50 s | 2,57 | **2,88** | 0,505 | 0,176 |
| 8,70 s | 2,96 | **3,15** | 0,511 | 0,162 |

Thấp nhất **2,59** (trước 1,86), trung vị 2,80. Điểm tia mỗi khung 590–2184 (trước 296–1548).

## Khác
- p95 dày nhất **6,0 ms** (toàn chiêu 5,9 ms), draw tối đa 276. Vùng trắng **0,0004 %**. Kiểm kiểu 0 lỗi. Các số đo kiếm khác như 433r.
- Gửi owner: `typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-s.jpg` và `.mp4` (12,7 s, có tiếng). Đã thêm dòng `ABOUT.md`, dựng lại index.
- Driver: `games/.wt-ic-lab-all/src/lab/metal-ult-rain-s-review.mjs`. Đã xoá khung thô, Chrome headless đã đóng. Server 3148 vẫn chạy. Không commit.
