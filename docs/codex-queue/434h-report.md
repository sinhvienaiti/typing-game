# Phiếu 434h — Sét nối dùng đúng ảnh C owner chọn

Ngày 17/11/2026. **Đạt các cổng kỹ thuật sau 3 vòng sửa → chụp → mở ảnh.** Tám bước ở camera chơi đều ≥14 px theo probe kế thừa; thân vẫn lấy nguyên từ ảnh C, không bóp theo bảng thân của 434g. Chưa có hai giám khảo mù chấm mỹ thuật 8,5; cần owner xem nét và nhịp trong video.

## Giao nộp

- [thunder-codex-h.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-h.jpg): ảnh C, nửa phải phân cảnh 431, hai camera ở 0,4 / 1,2 / 2,2 / 3,0 s.
- [thunder-codex-h.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/thunder-codex-h.mp4): 4 giây, 30 fps, 120 khung, H.264, 2560×720; Alt+1 và Alt+2 đặt cạnh nhau. Giữ AAC 4 giây của 434g vì lịch sự kiện không đổi.
- [Tám bước ở camera chơi](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/round-3/hop-check-sheet.jpg), [tám bước sau lưng](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/round-3/behind-hops-sheet.jpg), [khung giải mã MP4](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/round-3/video-decoded-sheet.jpg).
- [Số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/round-3/measure.json), [cổng kỹ thuật](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/final-gates.json), [neo, nhấp nháy và vòng đời tài nguyên](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/lifecycle.json).

Giữ mọi JPG/MP4 cũ, thêm dòng 434h vào `owner-review/2026-11-17/tu-tien/ABOUT.md`.

## Nguồn và cách đặt

Nguồn duy nhất của sét nối: `games/immortality-cultivation/art-src/lab/vfx/thunder/stills-55/thunder-bolt-ff.v1-try3.png`, SHA-256 `0dd6abd5cfc29927e99cfc420c407c290af6a15011bf7c2851f75eab52250e15`.

Tạo đúng các tài nguyên sau trong `games/.wt-ic-lab-all/art-src/lab/vfx/thunder/`:

| Tệp | Nội dung |
| --- | --- |
| `thunder-chain-c.png` | Cắt [48, 280, 930, 470] từ ảnh C 1024×1024; nền đen thành alpha thẳng, giữ nét và màu nguồn. |
| `thunder-chain-c-flip-y.png` | Lật dọc bản cắt. |
| `thunder-chain-c-flip-x.png` | Lật ngang bản cắt. |
| `thunder-chain-c.json` | Tọa độ hai neo bằng pixel và UV cho cả ba bản, đường dẫn nguồn, hash, phép cắt và quy ước alpha. |
| Ba tệp cùng tên `.prompt.txt` | Ghi đúng chỉ dẫn xử lý cơ học, nguồn và phép lật cạnh mỗi PNG. |

Alpha = căn bậc hai của kênh tuyến tính lớn nhất; RGB thẳng = RGB tuyến tính / alpha. Shader cộng RGB tuyến tính × alpha để khôi phục ánh sáng nguồn; chỉ tăng lõi nóng và điều khiển độ sáng. Không sinh ảnh mới.

Mỗi bước là **một quad 3D, bốn đỉnh/hai tam giác**. Hệ trục của hai neo trong ảnh ánh xạ thẳng sang đoạn nối ngực–ngực; chiều ngang ảnh kéo theo chiều dài đoạn, chiều vuông góc có sàn bề dày theo camera. Quad xoay quanh trục đoạn nối để hướng về camera, không nắn thân hoặc vẽ nhánh mới. Hai vị trí ngực cập nhật mỗi khung khi quái di chuyển. Bước đầu vẫn xuất phát từ tay nhân vật theo lịch cũ.

Ba biến thể luân phiên, bề ngang và thời điểm chớp lệch nhẹ từ hạt giống 434. Sáng đầy ngay khung sinh; có hai nhịp giảm sáng quanh 0,074–0,079 s và 0,133–0,140 s; tan hết trong 0,222–0,238 s. Không giữ sáng 0,22 s rồi cộng thêm đuôi 0,14 s như 434g.

## Phạm vi mã

Chỉ ghi bảy tệp có tiền tố `thunder-ult-` trong `games/.wt-ic-lab-all/src/lab/`:

- `thunder-ult-chain-card.ts`: quad C, neo, bám ngực, ba biến thể, hạt giống, nhấp nháy và giải phóng tài nguyên; pool 14 theo giới hạn lịch hiện có.
- `thunder-ult-nguloi.ts`: chuyển `hop()` sang lớp C. Giữ nguyên mã ribbon/fit thân 434g nhưng không phát nó cho sét nối; cột, bò đất và scar không đổi.
- `thunder-ult-chain.ts`: truyền hai hàm lấy vị trí ngực hiện tại; không đổi chọn quái hoặc lịch sự kiện.
- `thunder-ult-prepare-c.mjs`: tái tạo ba PNG, JSON neo và chỉ dẫn xử lý từ đúng ảnh C.
- `thunder-ult-review-h.mjs`: chụp hai camera, đo từng bước, quét trắng 480 khung, stress 100 quái.
- `thunder-ult-probe-h.mjs`: hủy/lặp, pool, giải phóng; kiểm cả ba phép ánh xạ neo, bám điểm chuyển động và hai nhịp nhấp nháy.
- `thunder-ult-deliver-h.mjs`: đối chiếu 434f, xuất JPG/MP4 và kiểm cổng.

## Ba vòng và số đo

Chrome headless, localhost:3148, High, DPR 1, 1280×720 mỗi camera; Alt+1/Alt+2; nền `#353a40`. Đã mở ảnh mỗi vòng, đối chiếu với nguồn C và nửa phải phân cảnh 431; mở thêm từng bước sau lưng và khung giải mã MP4 cuối.

Bề dày dưới đây là **nhỏ nhất của ba lát cắt vuông góc tại 35% / 50% / 65% đoạn chiếu**, ở 0,05 s sau mỗi bước. Mỗi lần chụp chỉ bật riêng một tia C; đối chứng tắt đúng tia đó, giữ nguyên cùng khung. Đếm dải liên tục có Rec.709 tăng ≥0,1, không cộng nhánh rời. Đây là thân sáng/quầng theo probe kế thừa, không phải bề dày riêng lõi trắng hoặc độ dày suốt pha tan.

| Vòng | Bề dày bước 1→8 (px) | Trắng tối đa | p95 (ms) | Nhận xét |
| --- | --- | --- | --- | --- |
| 1 | 159 / 71 / 69 / 111 / 68 / 155 / 45 / 57 | 0,768772% tại các mốc pha | 6,10 | Nét C đã có nhưng kéo ngang và quầng quá rộng. |
| 2 | 85 / 37 / 41 / 61 / 42 / 80 / 13 / 22 | 0,768772% tại các mốc pha | 6,10 | Giảm bề ngang; bước 7 còn 13 px, chưa đạt. |
| 3 | **97 / 44 / 46 / 69 / 46 / 94 / 26 / 31** | **0,768772% trên 480 khung** | **6,20** | Bù sàn bề dày và bám ngực động; cả tám bước đạt. |

Vòng cuối: độ phủ **100%** cả tám đoạn, hở đầu/cuối **0 px**. Độ phủ quét ít nhất 101 lát dọc đoạn, cách nhau ≤1 px; lát có dải liên tục ≥3 px, Rec.709 tăng ≥0,1 được tính có thân. Phép neo hình học sai số ≤1,12×10⁻¹⁵ m trong probe toán; điểm theo dõi dịch 0,3 m vẫn bám đúng.

## Kiểm tra và giới hạn

- `./node_modules/.bin/tsc --noEmit --incremental false` trong worktree: **0 lỗi**. Không chạy build hoặc bộ test game.
- `node --import tsx src/lab/thunder-ult-probe-h.mjs`: **PASS**; năm chu kỳ hủy/lặp, pool không rơi, hình học/vật liệu không tăng. Bộ hiệu ứng dùng 19 texture; probe ba biến thể độc lập dùng thêm 3; cả **22/22** giải phóng đúng một lần, dispose lặp an toàn.
- Sáng khung đầu = 1, hai đáy nhấp nháy được xác nhận ở bước thời gian 1 ms, kết thúc đúng 0,22–0,24 s. Clip 30 fps thể hiện số lần lóe tùy pha lấy mẫu.
- Stress **87 TargetField + 13 walker = 100 quái**, 4×240 mẫu; bỏ lượt làm nóng, gộp 720 mẫu. p95 tổng CPU + chờ GPU qua `readPixels` = **6,20 ms ≤16,7 ms**, ANGLE Metal / Apple M4.
- **480 PNG không mất dữ liệu**, 240 khung/60 Hz mỗi camera, toàn đoạn 4 giây: RGB ≥0,95 tối đa **0,768772%**, Rec.709 ≥0,95 tối đa **0,829753%**; đều ≤6%.
- JSON xác nhận giữ nguyên đường chọn quái, góc zíc zắc và mốc từng bước; dữ liệu cột Ngũ Lôi, bò đất, scar và mây ở 2,2/3,0 s giống 434f. Không exception.
- Các cảnh báo có sẵn về KTX2Loader, atlas Kim và nhiều bản Three vẫn còn; không sửa lane khác.
- [Xác nhận dọn Chrome](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/thunder-ult-434h/browser-cleanup.json): không còn tiến trình Chrome dùng profile của lượt chụp, profile tạm không còn.

Không sửa game chính, docs Tu Tiên, `cloud-volume*`, `five-thunder.ts`, nguồn C, flipbook Ngũ Lôi hoặc audio-lab. Không tạo ảnh/âm mới vì phiếu yêu cầu dùng đúng ảnh C và giữ lớp cũ. Không khởi động/dừng server; không commit/push/reset/clean/stash. Owner cần xem đoạn sét nối ngắn ở bước 7–8 và nhánh ảnh C ở cả hai camera; chưa ghi nhận nghiệm thu mỹ thuật 8,5.

## Dọn khung

Dùng `tools/capture-prune/prune.mjs` xem danh sách khô rồi áp dụng chỉ trong `captures/tu-tien/thunder-ult-434h/`; giữ các sheet, JSON, ABOUT và video. Đã xóa **736 ảnh thô, 658,771 MB**, giữ 15 sheet; chi tiết trong `prune-dry.json` và `prune-applied.json`. Không đụng capture của phiếu khác. Dựng lại mục lục review sau khi dọn.
