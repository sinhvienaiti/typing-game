# Phiếu 434e — Lôi: mây hiện vừa đủ, thay vết đất

Ngày 17/11/2026. Hoàn tất **2 vòng** sửa → chụp → mở ảnh → đối chiếu nửa phải phân cảnh 431. Các ngưỡng đo của phiếu đạt tại các mốc quy định. Chưa phải nghiệm thu mỹ thuật 8,5 của hai giám khảo mù.

## Giao nộp

- [Ảnh mới — thunder-codex-e.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-e.jpg).
- [Video mới — thunder-codex-e.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-e.mp4): 1280×720, H.264, 30 fps, 120 khung, đúng 4,000 giây. Giữ track AAC 4,000 giây của 434d, cùng mốc đánh 2,0 giây.
- [Diễn tiến mặt đất](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-2/ground-detail-sheet.jpg), [đối chứng bật/tắt vết nứt](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-2/ground-control-sheet.jpg).
- [Tấm giải mã MP4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-2/video-decoded-sheet.jpg).
- [Số đo đầy đủ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-2/measure.json), [probe vòng đời](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/chain-probe.json).

Giữ nguyên các ảnh/video cũ. Đã thêm dòng 434e vào `owner-review/2026-11-17/tu-tien/ABOUT.md`. Mỗi thư mục làm việc mới có `ABOUT.md`.

## Thay đổi

Chỉ ghi mã trong phạm vi `games/.wt-ic-lab-all/src/lab/thunder-ult-*` và `cloud-volume*`:

| File | Nội dung |
| --- | --- |
| `thunder-ult-chain-space.ts` | Đưa khối mây gần đàn quái hơn 2,5 m: tâm Z bằng tâm đàn quái −9,5 m, thay vì −12 m. Giữ chiều cao thế giới và kích thước; không ép theo màn hình/camera. Neo thân chính ở Y = 7 m, bên trong phần đáy mây thấy được. Vết nứt lấy hình từ atlas có sẵn, tách phần khe điện xanh thành mặt nạ mảnh và nhuộm xám than ấm. |
| `thunder-ult-chain.ts` | Bỏ nạp/gắn `thunder-ground-mark`; giữ file cũ trong thư viện. Nạp đúng `thunder-scorch-crack-top`. Thay 12 nhánh rơi cũ bằng **8 nhánh bò sát đất**, giữ thân chính, 3 nhánh phụ mỗi bước dây chuyền, ánh tím, burst và dư điện. Kéo thời điểm thu hồi từ 3,5 lên 4,0 s để vết nứt tan đủ 1,5 s. |
| `cloud-volume.ts` | Thêm lựa chọn đặt lại đồng hồ khi `clear(true)`; chỉ lượt cast Lôi gọi lựa chọn này để mây lặp lại đúng pha. Cách gọi mặc định giữ nguyên. |
| `cloud-volume-probe.ts` | Đo riêng footprint alpha ≥ 128/255; ghi biên, diện tích, độ phủ ngang, các hàng rộng ≥60%; lấy alpha tại tâm quái và gốc sét. |
| `thunder-ult-chain-probe.mjs` | Kiểm số nhánh, chiều dài, các đoạn mặt đất đúng Y = 0,08 m, thời gian, thành phần được nạp, hủy/lặp và giải phóng. |
| `thunder-ult-review-e.mjs`, `thunder-ult-pixel-e.mjs` | Chụp hai camera, đối chứng tắt mây/tia/vết nứt, stress và quét 480 khung; giữ mọi số đo thô dạng JSON. |

Công cụ tạo hình là **các thành phần sẵn có** theo `game-vfx-production` và `game-vfx-layered`: puff CC0 `cloud-puffs/cloud01.png`, tia đang có của 434d, burst/dư điện hiện có, atlas Firefly `thunder-scorch-crack-top`. Không tạo hình, clip nguồn hay âm thanh mới; không thêm lớp ngoài phân cảnh. Không dùng image_gen vì không thiếu thành phần cần tạo.

## Mây, quái và thân sét

1280×720, DPR 1, High, nền `#353a40`. Dải dưới đây lấy **alpha ≥ 128/255**, không dùng ngưỡng 8/255 của 434d. Mép trên footprint đều bằng 0. Độ phủ ngang là bề rộng footprint alpha thật; mép mây có gờ và khoảng lõm, không phải một hình chữ nhật đặc.

| Camera | Mốc | Dải mây từ mép trên | Phủ ngang | Tâm quái bị phủ đặc |
| --- | --- | --- | --- | --- |
| Chơi | 0.4 s | 20.14% | 93.28% | 0/87 |
| Chơi | 1.2 s | 22.78% | 99.69% | 0/85 |
| Chơi | 2.2 s | 22.22% | 99.14% | 0/72 |
| Chơi | 3.0 s | 15.56% | 79.61% | 0/72 |
| Sau lưng | 0.4 s | 31.11% | 100.00% | 0/87 |
| Sau lưng | 1.2 s | 31.11% | 100.00% | 0/85 |
| Sau lưng | 2.2 s | 31.67% | 100.00% | 0/72 |
| Sau lưng | 3.0 s | 31.53% | 100.00% | 0/72 |

Camera sau lưng giữ nguyên vị trí/FOV của 434d. Biên mây thưa cùng ngưỡng 8/255 cao 34,58–35,97% ở các mốc sau lưng, vẫn trên 30%. Mọi khung pha đã đo đều có số tâm quái bị phủ đặc bằng 0. Không khẳng định đây là phép quét alpha của mọi khung giữa các mốc; mây tiếp tục tan ở cuối chiêu.

Gốc sét chính chiếu tới khoảng **(629; 122) px** ở camera chơi khi đánh, nằm trong khung; alpha mây tại gốc ở 2,0 / 2,0167 / 2,2 s là **0,580 / 0,549 / 0,522**. Sau lưng là khoảng (624; 139) px, alpha 0,996. Các đoạn của thân chính nối chung đầu–cuối, từ gốc mây tới điểm đất Y = 0,08 m; không còn bắt đầu ngoài mép khung. Ba lát cắt thân chính lúc 2,0 s có lõi sáng 9/13/9 px, lõi + quầng 123/111/36 px. Số sát thương của host vẫn có thể che một phần gốc tia.

Dây chuyền giữ cùng 8 mục tiêu và thứ tự của 434d; góc đổi hướng xấp xỉ **+52,40 / −63,71 / +45,47 / −52,31 / +76,49 / −64,54 / +48,10°**, 3 nhánh phụ/bước, giữ sáng 0,22 s rồi mờ 0,14 s. Chỉ một thân chính là điểm nhấn. Dư điện vẫn 8 quái, 40 nhịp nhỏ trong khoảng 2,45–3,45 s.

## Điểm đánh và dư âm mặt đất

- **8 nhánh** dài **3,67–5,80 m**, mọc từ điểm đánh; toàn bộ 144 đoạn chính của chúng nằm ở **Y = 0,08 m**. Giữ sáng **0,18 s**, mờ **0,32 s**: tổng **0,50 s**, từ 2,0 tới 2,5 s.
- Vết cháy dùng đúng `art-src/lab/vfx/thunder/thunder-scorch-crack-top.atlas.png` và metadata tương ứng. Lấy khung 18 làm mặt nạ ổn định, không phát cả clip thành một kỹ năng. Kích thước 10,5×10,5 m, nằm ngang ở Y = 0,045 m. Màu RGB tuyến tính **(0,043; 0,035; 0,027)**, không phát sáng tím, không vẽ thêm sao/chấm.
- Vết nứt hiện mềm từ 2,18 tới 2,5 s dưới các nhánh điện, rồi mờ trong **1,50 s**, biến mất ở 4,0 s. Tất cả pool trả về ở 4,0 s.
- 10 đối chứng bật/tắt ở 2,5 / 2,6 / 3,0 / 3,5 / 3,95 s, hai camera: lớp vết nứt tạo **0 điểm trắng mới** (cả RGB ≥0,95), **0 điểm lóe mới** (Rec.709 ≥0,8 và tăng ≥0,1). Vết tối có 6.157 px giảm sáng ≥1/255 ở camera chơi 3,0 s. Các đốm trắng nhỏ khác của host vẫn còn trong cả ảnh bật và ảnh tắt vết nứt; chúng không do decal này tạo ra. Không sửa lớp khác ngoài phạm vi.

## Kiểm tra

- `./node_modules/.bin/tsc --noEmit --incremental false`: **0 lỗi**.
- `node --import tsx src/lab/thunder-ult-chain-probe.mjs`: **PASS**; kiểm nhánh sát đất, thời gian, không nạp decal cũ, tài nguyên ổn định, hủy/lặp 5 lần, cảnh rỗng/3 quái, giải phóng đủ 8 texture.
- Stress **87 TargetField + 13 walker = 100 quái**: 4×240 mẫu, loại lượt đầu, gộp 720 mẫu. `total = CPU + chờ GPU qua readPixels`: **p95 5,80 ms ≤16,7 ms**; CPU p95 **1,30 ms**. GPU **ANGLE Metal Renderer: Apple M4**. Mỗi lượt cuối `active=false`, `live=0`, `dropped=0`.
- Quét **480 PNG không mất dữ liệu**, 240 khung/60 Hz mỗi camera: trắng cả RGB ≥0,95 tối đa **0,023980%**, Rec.709 ≥0,95 tối đa **0,069987%**, đều dưới 6%. Dải gần trắng liên tục ngang lớn nhất sau lưng **13 px = 1,02%** khung, giữ cổng 2% của 434c.
- Không exception hay lỗi shader/GL. Host có cảnh báo atlas `metal-crescent-sym`, nhiều KTX2Loader và một cảnh báo nhiều bản Three từ phép probe; giữ trong JSON, không sửa phần của lane khác.
- Đã mở ảnh của cả hai vòng, thân sét/điểm đất ở kích thước thật, tấm diễn tiến mặt đất và tấm giải mã MP4. Hai vòng: [vòng 1](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-1/comparison.jpg), [vòng 2](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434e/round-2/comparison.jpg).

Không chạy build/bộ test game, không khởi động/dừng server 3148, không sửa mã game chính, audio-lab hay tài liệu Tu Tiên; không commit/push/reset/clean/stash. Không cần lượt thứ ba hoặc tạo thêm thành phần. Owner cần xem mức hiện diện mây Alt+1, thân sét liền từ mây xuống và hình vết nứt mới; phần chấm mỹ thuật 8,5 và các đốm trắng của lớp host khác còn dành cho owner/Claude.

## Dọn khung

Đã chạy capture-prune khô rồi áp dụng: **xóa 618 ảnh thô, 540,204 MB**, chỉ của phiếu 434e; giữ **10 sheet** cùng clip và JSON, không có mục bị từ chối. Đã dựng lại chỉ mục review. Các thư mục khung thô không còn ảnh.
