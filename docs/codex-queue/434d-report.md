# Phiếu 434d — Lôi: mây cao xa, sét dày sáng

Ngày 17/11/2026. Đã làm 4 vòng sửa → chụp → mở ảnh → đối chiếu nửa phải phân cảnh 431. Vị trí mây, vùng trắng, kiểm kiểu và p95 đạt ngưỡng phiếu. Bề rộng đạt trên các đoạn tia lộ rõ; một số lát cắt bị thân quái/số sát thương che, đã ghi cả kết quả 0 và đo bổ sung. **Chưa phải nghiệm thu mỹ thuật 8,5 của hai giám khảo mù.**

## Giao nộp

- [Tấm so phân cảnh và hai camera — thunder-codex-d.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-d.jpg).
- [Clip mới — thunder-codex-d.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-d.mp4): 1280×720, H.264, 120 khung/30 fps, đúng 4,000 giây; AAC 4,000 giây.
- [Số đo cuối, toàn bộ lát cắt và 480 khung](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-4/measure.json).
- [Đo bổ sung hai bước nhảy ngắn](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/width-check/measure.json).
- [Tấm giải mã từ MP4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-4/video-decoded-sheet.jpg).

Giữ các file 434c và file review cũ. Đã thêm dòng 434d vào `owner-review/2026-11-17/tu-tien/ABOUT.md`. Thư mục làm việc: `captures/tu-tien/thunder-ult-434d/`, có `ABOUT.md` cho từng lượt. Đã chạy capture-prune khô rồi áp dụng: xoá đúng 959 ảnh thô của riêng phiếu (883,562 MB), giữ 13 sheet; không có mục bị từ chối. Đã dựng lại chỉ mục review.

## Đã sửa

Chỉ ghi mã trong `games/.wt-ic-lab-all/src/lab/`, đúng hai tiền tố được giao:

| File | Thay đổi |
| --- | --- |
| `thunder-ult-chain-space.ts` | Bỏ phép ép mây theo khung hình; đặt một khối cố định phía sau đàn quái. Tăng quầng tím và lõi sáng, giữ nhánh/zíc zắc. Neo thân sét vào phần đáy trước của mây. Thêm xuất các đoạn thế giới thật cho probe; sửa sai số thời gian khiến tia vừa sinh đôi lúc mất đúng khung đầu. |
| `thunder-ult-chain.ts` | Mây có đáy cấu hình 10,2 m, dày 11 m, bán kính 26 m, tâm xa hơn đàn quái 12 m theo trục Z; cùng tọa độ ở cả hai camera. Đường nhảy có đường kính hình học 1,04 m; thân chính 2 m. Chớp nội mây đặt ở phần đáy phía trước. Hai đèn tím mềm hắt xuống đất/quái; không bật decal mặt đất hay thêm vòng. Giữ dư điện và chuỗi mây tan của 434c. |
| `cloud-volume.ts`, `cloud-volume-probe.ts` | Snapshot tham số/thời gian/độ mờ và phép đo alpha thật; lấy tâm quái từ hook `beast`, camera từ `captureCamera`. Không đổi bố trí/màu của Poison hoặc Dark. |
| `thunder-ult-chain-probe.mjs` | Cập nhật hợp đồng tọa độ/kích thước; giữ kiểm góc độc lập, hủy/lặp, tài nguyên và cảnh ít/rỗng. |
| `thunder-ult-review-d.mjs`, `thunder-ult-pixel-d.mjs`, `thunder-ult-width-d.mjs` | Chụp pha, đo alpha/lát cắt, stress, quét trắng toàn chuỗi và kiểm thêm phần tia bị khuất. Trang chụp bỏ qua thông báo HMR của Vite để các lane khác không làm reload giữa phép đo; không sửa server. |

Công cụ tạo hình của lượt này là các thành phần sẵn có: puff CC0 `art-src/lab/vfx/cloud-puffs/cloud01.png`, các flipbook va chạm, hạt, dư điện và vết cháy của Thunder. Mã chỉ đổi bố trí, bề rộng, màu và ánh sáng của hiệu ứng đã có. Không tạo ảnh/video nguồn, mô hình hoặc âm thanh mới. Clip giữ track âm từ 434c với cùng mốc sự kiện; không sửa mixer hoặc audio-lab.

Mỗi bước nhảy giữ 3 nhánh phụ. Chỉ một thân chính mang cờ điểm nhấn; quầng chính có kênh lớn nhất `0,9 × 0,86 × 1,15 = 0,8901`, lõi được sáng hơn. Hai đèn dùng RGB tuyến tính `(0,36; 0,16; 0,9)`, cường độ theo nhịp chớp rồi suy giảm mềm. Không bật bóng đổ cho đèn.

## Các vòng

| Vòng | Kết quả khi mở ảnh và đối chiếu |
| --- | --- |
| [1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-1/comparison.jpg) | Đẩy quá xa/cao: camera chơi mất hẳn mây; sau lưng chỉ 26,9–28,6%. Decal tím lộ hình quá rõ. Không đạt. |
| [2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-2/comparison.jpg) | Mép dưới mây ở 14,9–15,7% khung chơi; sau lưng 33,3–34,6%; phủ đặc tâm quái = 0. Bỏ decal, giữ ánh đèn mềm. Một lượt chụp bị chính cập nhật mã làm reload, đã chụp lại cùng cấu hình. |
| [3](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-3/comparison.jpg) | Lõi rõ hơn nhưng gốc thân chính còn bị cắt ở mép trên. Phép quét dài bị host dùng chung reload sau 159 khung nên không dùng để nghiệm thu số đo. |
| [4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434d/round-4/comparison.jpg) | Gốc thân chính xuất hiện trong phần mây nhìn thấy; quái lộ rõ. Hoàn tất 480 khung và stress, không sửa hiệu ứng thêm. Đo bổ sung lúc 1,25/1,35 s là phép đo trên cùng mã vòng 4. |

## Mây và vùng trắng

1280×720, DPR 1, High, nền `ground=%23353a40`. “Mép dưới”/chiều cao mây lấy alpha ≥ 8/255 của chính shader/puff tại cùng thời gian, độ mờ và camera; “phủ đặc” lấy alpha ≥ 0,5 ngay tại tâm màn hình của từng quái còn sống. Không dùng bao mesh thay alpha.

| Camera | Mốc | Mép dưới mây từ trên | Chiều cao mây trong khung | Tâm quái bị phủ đặc |
| --- | --- | --- | --- | --- |
| Chơi | 0,4 s | 17,64% | 17,64% | 0/87 |
| Chơi | 1,2 s | 17,92% | 17,92% | 0/85 |
| Chơi | 2,2 s | 18,06% | 18,06% | 0/72 |
| Chơi | 3,0 s | 17,22% | 17,22% | 0/72 |
| Sau lưng | 0,4 s | 36,39% | 36,39% | 0/87 |
| Sau lưng | 1,2 s | 36,94% | 36,94% | 0/85 |
| Sau lưng | 2,2 s | 36,53% | 36,53% | 0/72 |
| Sau lưng | 3,0 s | 37,64% | 37,64% | 0/72 |

Tính cả các mốc phụ: mép dưới lớn nhất ở camera chơi **18,19% ≤ 28%**; chiều cao nhỏ nhất sau lưng **36,25% ≥ 30%**. Cả 26 ảnh pha đều có số tâm quái bị phủ đặc bằng 0. Đây là kết quả tại các khung đã đo, không phải phép quét alpha cho mọi khung của clip.

Quét **480 PNG không mất dữ liệu**, 240 khung/60 Hz mỗi camera: trắng cả ba kênh ≥ 0,95 lớn nhất **0,022895% ≤ 6%**; Rec.709 ≥ 0,95 lớn nhất **0,065213%**. Đo ngang bảo thủ trên toàn khung sau lưng: vùng gần trắng liên tục lớn nhất **16 px = 1,25%**, dưới cổng 2% của 434c.

## Bề rộng sét

Probe cắt vuông góc đoạn thế giới thật đã chiếu qua camera, dùng hai ảnh đóng băng cùng thời gian, chỉ bật/tắt mesh sét. Quầng = dải liên tục qua trục có Rec.709 tăng ≥ 0,1. Lõi sáng = Rec.709 tuyệt đối ≥ 0,8 **và** tăng ≥ 0,1; ngưỡng tăng loại phần quái sáng sẵn. Cũng ghi lõi gần trắng ≥ 0,95 riêng, không đồng nhất hai ngưỡng này.

Bảng dưới lấy phần có lõi lộ rõ. Đã lưu mọi lát cắt 4/8/13 của 18 đoạn chính, kể cả kết quả 0; hai bước cuối đo thêm đủ 18 đoạn vì bị thân quái/số sát thương che. Quầng gồm bloom và các nhánh giao nhau, không phải đường kính lõi hình học.

| Bước | Sinh lúc | Đo lúc | Đoạn | Lõi sáng | Lõi + quầng | Tỷ lệ quầng/lõi |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0,6 s | 0,6 s | 8 | 3 px | 115 px | 38,33 |
| 2 | 0,7 s | 0,7 s | 8 | 8 px | 120 px | 15,00 |
| 3 | 0,8 s | 0,8 s | 13 | 2 px | 45 px | 22,50 |
| 4 | 0,9 s | 0,9 s | 8 | 2 px | 86 px | 43,00 |
| 5 | 1,0 s | 1,0 s | 8 | 14 px | 52 px | 3,71 |
| 6 | 1,1 s | 1,1 s | 8 | 2 px | 60 px | 30,00 |
| 7 | 1,2 s | 1,35 s | 15 | 6 px | 45 px | 7,50 |
| 8 | 1,3 s | 1,35 s | 8 | 7 px | 86 px | 12,29 |

Các phần lộ rõ trên đều ≥ 6 px, tỷ lệ ≥ 3. **Không khẳng định mọi lát cắt hoặc mọi khung đều đạt**: tại đúng 1,2/1,3 s có các đoạn hoàn toàn khuất; lõi của đường nhảy chưa đạt Rec.709 0,95 ở các lát cắt đã chọn. Owner cần xem màu lõi trắng tím bằng mắt, không dùng bảng này thay nghiệm thu hình.

Thân chính lúc 2,0 s: ba lát cắt có dải tăng sáng **96 / ≥181 / 25 px**, nhỏ nhất 25 px ≥ 10 px. Giá trị ≥181 chạm biên probe ±90 px nên chỉ là cận dưới; vùng chớp/nhánh giao làm dải đo rộng. Lõi sáng ở hai lát cắt có lõi lộ rõ là 13/16 px. Thân chính vẫn là điểm nhấn duy nhất; tổng vùng trắng đã kiểm ở mọi khung.

Góc rẽ giữ nguyên 434c, luân phiên phải/trái: **+52,41 / −63,71 / +45,47 / −52,31 / +76,49 / −64,54 / +48,10°**; không lặp quái. Dư điện vẫn bám các quái sống ở pha 3,0 s; mây giảm dần sau 2,4 s và cả nhóm kết thúc ở 3,5 s như chuỗi cũ.

## Kiểm tra và phần còn lại

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**.
- `node --import tsx src/lab/thunder-ult-chain-probe.mjs`: **PASS**, gồm hủy/lặp 5 lần, cảnh rỗng/ít quái, giải phóng tài nguyên.
- Stress: **87 TargetField + 13 walker = 100** ở từng lượt; 4 × 240 mẫu, loại lượt đầu, gộp 720 mẫu. `total = CPU + chờ GPU qua readPixels`: **p95 7,5 ms ≤ 16,7 ms**; CPU p95 1,6 ms. P95 từng lượt: 9,5 / 7,8 / 7,6 / 6,1 ms. GPU: `ANGLE (Apple, ANGLE Metal Renderer: Apple M4, Unspecified Version)`.
- Mỗi lượt kết thúc `active=false`, `live=0`, `dropped=0`. Không có exception hoặc lỗi shader/GL trong lượt cuối. Host còn cảnh báo nạp atlas `metal-crescent-sym` của làn khác; giữ trong JSON, không sửa.
- Đã mở các sheet của 4 vòng, ảnh thân chính 1280×720 và sheet giải mã MP4. Không đánh giá lại chất lượng âm hoặc gắn nhãn đạt 8,5.
- Không chạy build/bộ test game; không dừng/khởi động server; không sửa mã game chính, audio-lab hoặc tài liệu Tu Tiên; không commit.

**Owner cần xem:** độ hiện diện của mây ở dải trên Alt+1, ánh chớp tím còn khá cục bộ, các bước nhảy ngắn bị số sát thương/thân quái che, và màu lõi đường nhảy. Mây/ánh sáng chưa có độ phong phú của phân cảnh. Đã dừng sửa đúng giới hạn 4 vòng; phần duyệt mỹ thuật và hai giám khảo mù còn lại cho owner/Claude.
