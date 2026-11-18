# Phiếu 432b — giữ đủ chân khói độc

Ngày 17/11/2026. **Đã hạ pivot và bật `-v5b` trong lab. Đo PNG/KTX2, probe module thật và kiểm kiểu PASS; chưa chụp lại hình trên host/GPU.** Phiếu có PASS Sonnet và miễn hạn mức của owner; làm một luồng.

## Chẩn đoán và sửa

Đã mở atlas `poison-big-burst-v5.atlas.png` và ảnh owner `typing-game-review/owner-review/2026-11-17/tu-tien/poison-v5.jpg`. Atlas còn nguyên khói phía dưới: pixel sáng cuối cùng ở hàng **223/256**; pivot cũ **0,65873**, khoảng hàng 169, nằm giữa khối khói. Ground-card gập phần dưới pivot xuống **y=0**, đồng phẳng với nền có depth-test. Cơ chế này phù hợp với đường cắt thẳng tại pivot trong ảnh owner; không phải thiếu phần dưới trong crop.

- `games/.wt-ic-lab-all/src/lab/burst-v2.ts`: **chỉ đổi hậu tố của dòng `poison-big-burst`, `-v5` → `-v5b`**. Giữ ground=true, scale=1,4, intensity=1.
- JSON `-v5b` hạ pivot xuống **[0.5, 0.9]**, trong dải trống dưới toàn bộ khói. Phần ground-card nằm trên mặt đất nay chỉ chứa nền đen; toàn bộ pixel phát sáng nằm trên nhánh upright.
- Giữ fade đáy **15%** có sẵn: `smoothstep(0.0, 0.15, vUv.y)` nhân cả RGB/alpha. Không thêm fade lần hai.
- **Không cắt lại video** vì atlas đủ phần dưới. PNG và KTX2 `-v5b` là bản sao **đồng nhất từng byte** của `-v5`. Cần tên media mới vì parser kiểm tra chặt `id`/`image` theo hậu tố. Không nén lại hoặc thay đổi khung, màu, kích thước, thời gian.

## Tệp mới

Trong `games/immortality-cultivation/art-src/lab/vfx/poison/`:

- `poison-big-burst-v5b.atlas.png`
- `poison-big-burst-v5b.json`
- `poison-big-burst-v5b.uastc.ktx2`
- `poison-big-burst-v5b.prompt.txt` — công thức sửa, nguồn, tham chiếu và prompt Firefly gốc.
- `poison-big-burst-v5b.verify.py` — script đo và probe module lab, không chạy game.
- `poison-big-burst-v5b.validation.json` — kết quả chi tiết từng khung và probe.

Không tạo nội dung AI mới. SHA-256 xác nhận video nguồn và bốn tệp `-v5` không đổi. Khôi phục duy nhất hậu tố trong bộ nhớ cho ra đúng SHA-256 toàn tệp `burst-v2.ts` trước sửa: không thay dòng nào khác.

## Nghiệm thu kỹ thuật

Chạy từ `/Volumes/SS990TPRO/htdocs/typing-game`:

```sh
PYTHONDONTWRITEBYTECODE=1 tools/vfx-flipbook/.venv/bin/python games/immortality-cultivation/art-src/lab/vfx/poison/poison-big-burst-v5b.verify.py
node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json
```

Cả hai lệnh **exit 0**; kiểm kiểu **0 lỗi**. Đo đủ **32 khung PNG + 32 khung KTX2 giải mã mức 0**, trả Y về hướng PNG:

| Phép đo | PNG | KTX2 |
| --- | --- | --- |
| Lề nhỏ nhất trái/phải/trên/dưới, tính mọi pixel RGB > 0 | 36/35/29/32 px | 36/35/29/32 px |
| Lề tối thiểu, yêu cầu ≥10% | **11,33%** | **11,33%** |
| Bước nhảy alpha từng pixel giữa hai hàng liền kề ở vùng giữa ô | **0** | **0** |
| Bước nhảy alpha sau fade đáy 15%, yêu cầu ≤0,3 | **0,032607** | **0,032607** |
| Bước nhảy trung bình năng lượng sáng giữa hai hàng | **0,035294** | **0,035890** |
| RGB lớn nhất trong phần gập dưới pivot mới | **0** | **0** |

Vùng giữa ô là x,y=26…229, bỏ lề 10%. Asset **RGB additive** có alpha lưu trữ ngầm bằng 1; shader fire với occlude=0 xuất alpha bằng 0. Vì vậy alpha đơn thuần không bắt được đường cắt ánh sáng: script kiểm thêm trung bình maxRGB từng hàng và xác nhận toàn bộ phần gập dưới pivot bằng đen. Bước nhảy RGB của từng pixel trong chi tiết ngọn lửa có thể >0,3; đó không phải bước nhảy alpha hay một mép cắt ngang toàn khối.

Probe dùng parser, `FlipbookPool`, `installBurstV2Pools` và hook shader thật qua symlink `art-src` của lab: nạp đúng JSON/PNG/KTX2 `-v5b`, pivot shader y=0,1 và hàng gập UV=0,1, ground soft-clip tắt (-100000), occlude=0, fade đáy 0,15, scale=1,4; **0 cảnh báo**. Đây là fetch đọc tệp, chưa phải HTTP hoặc render GPU.

## Phần cần owner/coordinator xem

Chụp lại `poison-big-burst` ở cùng camera và mốc đỉnh khoảng **2,1 s**, xem đủ chân khói và vị trí tiếp đất sau khi hạ pivot. Chưa có video/ảnh mới trên host nên không tuyên bố nghiệm thu thị giác. Giới hạn khói mảnh chạm mép trên video nguồn đã ghi ở phiếu 432 vẫn giữ nguyên, ngoài lỗi chân khói của phiếu này.

Không chạy build hoặc bộ test game; không sửa thư viện VFX, mã runtime khác hoặc tài liệu Tu Tiên. Không commit, push, đổi nhánh hay đưa media vào Git.
