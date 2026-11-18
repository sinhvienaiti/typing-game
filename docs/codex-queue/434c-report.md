# Phiếu 434c — Lôi và mây bão

Ngày 17/11/2026. Đã chạy 4 vòng sửa → chụp → mở ảnh → đối chiếu nửa phải phân cảnh 431. Các cổng số đo đạt; tự chấm hình cuối **7,4/10**, chưa phải nghiệm thu mỹ thuật 8,5 của hai giám khảo mù.

## Giao nộp

- [Sét, phân cảnh cạnh hai camera](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-c.jpg).
- [Clip sét 4 giây, 1280×720, 30 fps, có âm](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-c.mp4).
- [Mây riêng, camera chơi và sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/clouds-codex-c.jpg).
- [Số đo, từng khung và các lượt stress](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/round-4/measure.json).
- [Phép đo lóe cục bộ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/locality/measure.json).

Giữ nguyên các file cũ. Đã thêm dòng vào `owner-review/2026-11-17/tu-tien/ABOUT.md`, dọn 593 ảnh thô của riêng phiếu (514,084 MB) bằng capture-prune và dựng lại chỉ mục review.

## Đã sửa

Chỉ sửa/tạo file đúng hai tiền tố được phép trong `games/.wt-ic-lab-all/src/lab/`:

| File | Thay đổi |
| --- | --- |
| `thunder-ult-chain.ts` | Chọn đường có nhìn trước, không lặp quái; góc rẽ luân phiên; ghi từng góc; hạ gốc sét vào mây; bỏ lớp phủ tím cũ và lóe tự phát không gắn với tia. |
| `thunder-ult-chain-space.ts` | Tách lõi mảnh/quầng tím xanh; chỉ thân chính có mức sáng cao; làm mềm đầu quầng tại khớp, giữ lõi liên tục. |
| `cloud-volume.ts` | Bố trí mây bão riêng bằng 170 puff CC0; lớp đáy dày, giữa cao hơn mép; ánh chớp có biên cứng 4 m và suy giảm mềm bên trong. |
| `cloud-volume-lab.ts` | Preset Thunder: đáy 6,2 m, bề dày cấu hình 7,8 m, màu đáy xanh đen, đỉnh xám xanh; không cộng tím toàn khối. |
| `cloud-volume-probe.ts` | Thêm chiều cao alpha thật vào kết quả probe. |
| `thunder-ult-chain-probe.mjs`, `cloud-volume-check.ts` | Cập nhật kiểm tra cũ; kiểm góc độc lập từ tọa độ, vòng đời, hủy/lặp và thời gian xuất hiện theo tham số. |
| `thunder-ult-review-c.mjs`, `thunder-ult-pixel-c.mjs`, `cloud-volume-locality-c.mjs` | Kịch bản chụp, đo pixel toàn chuỗi và kiểm lóe tại cùng thời điểm/camera. |

Dùng lại `art-src/lab/vfx/cloud-puffs/cloud01.png` cùng các flipbook sét, va chạm, hạt và vết cháy hiện có. Công cụ làm hình của lượt này là CC0/flipbook sẵn có; mã chỉ đặt, đổi màu và định thời. Không tạo ảnh, video nguồn hay âm thanh mới. Clip lấy âm từ các take thật mà lab ghi lại, ghép bằng mixer có sẵn; không sửa âm hoặc mixer.

## Các vòng

Điểm là tự chấm khi mở ảnh, không phải điểm giám khảo độc lập. Cột trắng của bảng này lấy cả ba kênh ≥ 0,95 ở các khung chụp pha; phép quét toàn chuỗi nằm bên dưới.

| Vòng | Bước nhảy; góc rẽ hợp lệ | Trắng lớn nhất | Lõi gần trắng, lát cắt lớn nhất | Mây sau lưng, nhỏ nhất | Tự chấm | Nhận xét nhìn thấy |
| --- | --- | --- | --- | --- | --- | --- |
| [1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/round-1/comparison.jpg) | 5; 38,42–67,79° | 0% | 0 px | 35,56% | 6,4 | Khối mây rõ hơn nhưng che quái; lõi sét chưa đạt ngưỡng gần trắng. Banner còn lọt vào ảnh, đã sửa ở vòng 2. |
| [2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/round-2/comparison.jpg) | 8; 45,47–76,49° | 0% | 0 px | 35,56% | 6,8 | Đường nhảy dài hơn, màu mây có tầng; thân chính vẫn thiếu lõi sáng. |
| [3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/round-3/comparison.jpg) | 8; 45,47–76,49° | 0,00489% | 3 px | 35,14% | 7,1 | Lõi mảnh, mây bớt lấn phía trước; quầng còn lộ mép tại khớp. |
| [4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/round-4/comparison.jpg) | 8; 45,47–76,49° | 0,00934% | 4 px | 35,14% | 7,4 | Khớp mềm hơn, lóe giữ cục bộ, thân lớn vẫn là điểm nhấn. |

## 1. Góc từng bước

Đo trên mặt phẳng XZ bằng `atan2(cross, dot)` của hai hướng liên tiếp. Bước đầu từ tay tới quái chưa có hướng nhảy trước để so. Chọn góc 38–77° để có khoảng đệm trong cổng 35–80°. Trong cảnh thật có 8 bước hợp lệ; không ép đủ trần 14 bằng cách chèn bước thẳng hoặc sai phía.

| Bước | Mốc | Quái | Góc có dấu | Phía |
| --- | --- | --- | --- | --- |
| 1 | 0,6 s | 58 | — | Khởi đầu |
| 2 | 0,7 s | 24 | +52,41° | Phải |
| 3 | 0,8 s | 25 | −63,71° | Trái |
| 4 | 0,9 s | 39 | +45,47° | Phải |
| 5 | 1,0 s | 41 | −52,31° | Trái |
| 6 | 1,1 s | 69 | +76,49° | Phải |
| 7 | 1,2 s | 71 | −64,54° | Trái |
| 8 | 1,3 s | 70 | +48,10° | Phải |

Console in từng dòng `[thunder-434c-hop]`. ID quái chính xác và tọa độ từng đoạn lưu trong `measure.json → hops`; bảng trên phải đối chiếu với JSON khi đổi cảnh.

## 2. Lõi và vùng trắng

Đã chụp đủ 0,4 / 1,2 / 2,2 / 3,0 s ở Alt+1 và Alt+2, thêm 2,0 và 2,0167 s. Nền `ground=%23353a40`, High, 1280×720, DPR 1. Sau đó kiểm **480 khung PNG không mất dữ liệu**: 240 khung ở 60 Hz cho mỗi camera, từ 0 đến 3,9833 s.

| Số đo cuối | Kết quả | Cổng |
| --- | --- | --- |
| Đo ngang bảo thủ trên mọi hàng của toàn khung sau lưng, Rec.709 ≥ 0,95 | **5 px = 0,390625%** chiều rộng | ≤ 25,6 px = 2% |
| Lát cắt vuông góc thân chính, 5 vị trí dọc thân, mọi khung sau lưng | 4 px lớn nhất | ≤ 2% |
| Trắng cả ba kênh ≥ 0,95, lớn nhất trong chuỗi và ảnh pha | **0,00934%** | ≤ 6% |
| Rec.709 ≥ 0,95, lớn nhất trong chuỗi và ảnh pha | **0,17806%** | ≤ 6% |

Độ rộng 5 px là đoạn liên tục sáng nhất ở bất kỳ vị trí nào trong khung, nên không bỏ sót phần thân lệch khỏi trục lý tưởng. Đây là phép đo ở độ phân giải/cài đặt trên, không suy rộng sang DPR hoặc camera khác.

## 3. Lóe trong mây

Bán kính runtime **4 m**, nằm trong cổng 3–5 m. Shader bằng không ngoài bán kính; bên trong suy giảm theo khoảng cách rồi bình phương. Trong tuyệt kỹ, chỉ các sự kiện tia thực phát lóe; không có cộng tím nền toàn khối.

Phép đối chứng đóng băng camera/thời gian, bật/tắt duy nhất một lóe ở `(0, 9, 0)`, tắt lóe ngẫu nhiên. Ngưỡng khác biệt ≥ 3/255 ở một kênh:

| Camera | Điểm ảnh đổi màu | Ngoài hình chiếu hộp bao bán kính 4 m |
| --- | --- | --- |
| [Chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/locality/top-locality-sheet.jpg) | 2,6862% khung | **0 px** |
| [Sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434c/locality/behind-locality-sheet.jpg) | 0,9037% khung | **0 px** |

Hộp chiếu là cận bao bảo thủ; giới hạn hình cầu 4 m được thực thi trong shader theo tọa độ thế giới.

## 4. Mây bão

Đáy tối với các gờ cuộn từ atlas CC0, trộn thường và xếp xa → gần. Dùng 170 puff trong **1 draw**. Nhánh `storm` giữ bố trí riêng của Thunder; không đổi bố trí Poison/Dark.

| Số đo | Kết quả |
| --- | --- |
| Mây riêng `?cloud=thunder`, góc sau lưng; alpha ≥ 8/255 | **228/720 px = 31,67%** chiều cao; phủ 25,53% diện tích khung |
| Mây trong tuyệt kỹ, sau lưng; ảnh bật/tắt mây, khác biệt ≥ 8/255 | **35,14–37,36%** chiều cao ở các khung pha |
| Bao hình học của puff ở giữa, r < 0,4 | **13,52 m** theo chiều đứng |
| Bao hình học của puff ngoài mép, r > 0,75 | **10,73 m** theo chiều đứng |
| Tâm puff cao nhất tính từ đáy: giữa / mép | 6,89 / 4,83 m |

Bao hình học chỉ chứng minh tầng giữa dày hơn; không dùng nó thay phép đo alpha. Trong ảnh chơi vẫn có phần đàn quái bị mây che. Đáy mây sau lưng đọc dày và tối nhưng còn mềm, chưa có mức chi tiết/ánh sáng của phân cảnh.

## Kiểm tra và giới hạn

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**.
- `node --import tsx src/lab/thunder-ult-chain-probe.mjs`: **PASS**; góc tính lại từ tọa độ, không lặp mục tiêu, hủy/lặp 5 lần, cảnh rỗng/cảnh ít quái, giải phóng tài nguyên.
- `node --import tsx src/lab/cloud-volume-check.ts`: **PASS**; vòng đời 15/30/60/120 Hz, ngắt chuyển mờ, adapter không tăng tuổi hai lần trên cùng khung, teardown.
- Stress đúng **87 TargetField + 13 walker = 100** ở cả 4 lượt. Mỗi lượt 240 mẫu; loại lượt làm nóng đầu, gộp 720 mẫu còn lại. `total = CPU + chờ GPU qua readPixels`: **p95 5,5 ms**, CPU p95 1,0 ms, cổng 16,7 ms. GPU: `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`. P95 từng lượt: 6,4 / 5,5 / 5,3 / 5,8 ms.
- Các lượt kết thúc `active=false`, `live=0`, `dropped=0`. Hai lượt cuối cùng có cùng 161 texture / 292 geometry; tài nguyên khác của host còn nạp trong các lượt đầu, không coi cả bốn lượt là đã ổn định bộ nhớ.
- Không có exception hoặc lỗi nạp tài nguyên Thunder. Host có cảnh báo cũ KTX2 nhiều loader và hai atlas Metal không nạp; ghi nguyên trong JSON, không sửa ngoài phạm vi.
- Clip có 120 khung / 30 fps, dài đúng 4,000 s, âm AAC từ take hiện có. Không đánh giá lại chất lượng âm.
- Không chạy build hoặc bộ test game; không dừng/khởi động server, không commit, không chạm mã game hay tài liệu Tu Tiên khác.

**Owner cần xem:** độ dày và độ che quái của mây ở Alt+1; gờ cuộn ở Alt+2; độ quét ngang của đường sét. Tự chấm 7,4 còn dưới 8,5: hình mây vẫn mềm, đường sét nhỏ chưa có độ phong phú của phân cảnh. Chưa gắn nhãn nghiệm thu mỹ thuật hoặc đưa thay đổi vào game chính.
