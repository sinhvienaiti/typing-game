# Phiếu 433c — Kim mưa kiếm: kích thước và camera chơi

Ngày **17/11/2026**. Đã hoàn tất mã trong worktree `games/.wt-ic-lab-all`, kiểm kiểu **0 lỗi** và hai probe CPU đạt. **Chưa nghiệm thu toàn bộ: còn p95 GPU `stress.html` 100 quái, console và hình chụp thật cho owner.** Công cụ trình duyệt hiện báo `The browser access host is unavailable`; sandbox cũng không kết nối được host `127.0.0.1:3146`. Không lấy số CPU để kết luận đạt 16,7 ms hoặc chất lượng 8,5.

## Tệp giao

Trong `games/.wt-ic-lab-all/`:

- `src/lab/metal-ult-rain.ts`: kích thước, đặt trận trong khung, số đo probe.
- `src/lab/metal-ult-layered.ts`: nối nhịp camera vào lượt tung mưa kiếm.
- `src/lab/ult-camera-punch.ts`: camera dùng chung, tham số tâm, tỉ lệ khoảng cách, hạ góc, thời gian vào/giữ/trả và FOV tùy chọn; tắt bằng `?ultCam=0`.
- `src/lab/metal-ult-rain-check.mjs`: kiểm kiểu tập trung, GLB thật, lịch mưa kiếm, pool và camera.
- `src/lab/metal-ult-camera-check.mjs`: probe camera độc lập, hình chiếu và vòng đời adapter.
- `src/lab/metal-ult-rain-review.mjs`: lệnh chụp/đo cho Claude; mặc định góc chơi `top`, bốn mốc 0,4 / 1,2 / 2,4 / 3,2 s; có `METRICS_ONLY=1` để chỉ in số, không ghi capture.

Báo cáo: `docs/codex-queue/433c-report.md` ở repo cha. Chỉ ghi các đường dẫn được phiếu cho phép; giữ nguyên thay đổi có sẵn của tác nhân khác. Không chạy build hoặc bộ test game, không tạo media, không commit/push/reset/clean/stash, không đổi nhánh. Áp dụng miễn hạn mức owner ghi trong phiếu.

## Kết quả mã

| Phần | Giá trị |
| --- | --- |
| Kiếm thường, chiều cao phần nhìn thấy của GLB | **5,010–5,929 m** |
| Kiếm cuối | **16 m** |
| Trận pháp | Cao **6 m**, đường kính **14 m** |
| Vệt sau kiếm | Dài **5,029–8 m**; rộng **1,52 m**, kiếm cuối **3,4 m**, đúng hai lần bản 433b |
| Tia rủ dưới trận | Rộng **0,16–0,32 m**, hai lần bản 433b |
| Ground mark | **7,25 m**, kiếm cuối **22,5 m**: hai chiều tăng **2,5 lần** |
| Camera | Vào trong **0,5 s** bằng đường cong quintic ease in/out; khoảng cách còn **65%**, góc **55° → 49°**; giữ tới **2,6 s**; trả trong **0,6 s**, kết thúc **3,2 s** |

Giữ art/GLB/atlas hiện có. Trận pháp được đặt bằng hình chiếu của toàn bộ hình tròn, có khoảng đệm mép trên 12% + 2 px và cách đáy thẻ tên ít nhất 12 px. Mask mềm ở góc thẻ giới hạn art vào đúng đường tròn để phần kiểm khung khớp phần vẽ, kể cả khi trận xoay và camera có yaw. Chỉ dịch tâm hiển thị của trận và tia rủ; vị trí mục tiêu và điểm chạm kiếm giữ nguyên.

**Chi tiết cần owner xem:** FOV chuyển **28° → 34° → 28°**, cùng đường cong camera. Ở FOV 28° cố định, hình tròn 14 m trên mặt phẳng cao 6 m không đủ chỗ dưới thẻ tên trong tư thế camera gần; khoảng mở 6° giúp giữ cả trận và người chơi. Tỉ lệ khoảng cách vẫn là 65%, hạ góc vẫn là 6°. FOV là tham số tùy chọn của helper và được phục hồi cùng vị trí/quaternion gốc.

Host vẫn sở hữu sát thương, số và âm thanh. Giữ 49 kiếm, ba đợt **0,6 / 1,05 / 1,5 s**, kiếm cuối chạm **2,4 s**, 36 kiếm nhắm mục tiêu + 12 kiếm rải. Không đổi power, số sát thương, đường gọi `blow`/`strike`, tệp âm hay lịch âm. Nhánh `?metalUlt=ring` giữ nguyên hành vi.

## Đã kiểm

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node node_modules/typescript/bin/tsc --noEmit
node src/lab/metal-ult-rain-check.mjs
node src/lab/metal-ult-camera-check.mjs
node --check src/lab/metal-ult-rain-review.mjs
```

- Kiểm kiểu toàn worktree: **0 lỗi**. Kiểm cú pháp kịch bản chụp: **đạt**.
- 240 bước ở 60 Hz: trận và caster cao 2,4 m đều trong khung, không giao thẻ tên; kiểm lại ở yaw **0° / 20,05°**, có/không có thẻ tên. Probe độc lập chiếu 360 điểm trên biên để đối chiếu hộp bao tính toán.
- Không có thẻ tên: mép trên thấp nhất **88,4 px = 12,278%**. Với thẻ tên kết thúc ở y = 154 px: mép trên **166 px = 23,056%**, khoảng hở **12 px**.
- Camera ở **15 / 60 / 120 Hz**, có/không có parent: đạt; nhiều lượt cập nhật ma trận cùng thời điểm không cộng dồn chuyển động; hủy, tung lại và bước thời gian lớn đều trả camera. Sai số trả vị trí **0 m**; quaternion và FOV phục hồi. Camera thấp nhất trong fixture **26,487 m**, không xuyên đất.
- `?ultCam=0`: vị trí/quaternion/FOV giữ nguyên qua 240 bước. Cờ chỉ tắt phần chuyển động của helper; hiệu ứng camera khác vẫn thuộc host hiện có.
- Hook giữ lời gọi stress hiện có, tháo đúng khi dispose và không sửa prototype Three.js. Một lượt rà soát nguồn độc lập không còn phát hiện lỗi cụ thể; chưa phải duyệt hình.
- **49/49** điểm chạm và slot trả ở 4 s; năm vòng tung/xóa, nạp chậm rồi clear/dispose, nhánh vành cũ: đạt. Không tạo lại tài nguyên sau mỗi lượt tung. Tối đa vẫn **272.930 tam giác kiếm**.
- Lượt probe cuối: lập kế hoạch **0,980 ms**, p95 vòng cập nhật CPU có kiểm camera **0,170 ms**. Đây là số CPU fixture, không đo giải mã ảnh trình duyệt, GLSL hoặc GPU toàn cảnh.

Đường cong camera của fixture, khoảng cách tính tới tâm shot cố định:

| Thời điểm (s) | Khoảng cách (m) | Tỉ lệ | Góc nhìn xuống | FOV |
| --- | --- | --- | --- | --- |
| 0 | 47,878 | 1,0000 | 55° | 28° |
| 0,25 | 39,369 | 0,8223 | 52° | 31° |
| 0,4 | 32,056 | 0,6695 | 49,348° | 33,652° |
| 0,5–2,6 | 31,121 | 0,6500 | 49° | 34° |
| 2,75 | 32,797 | 0,6850 | 49,621° | 33,379° |
| 2,9 | 39,369 | 0,8223 | 52° | 31° |
| 3,1 | 47,268 | 0,9873 | 54,787° | 28,213° |
| 3,2 | 47,878 | 1,0000 | 55° | 28° |

Hộp bao trận ở **1280×720**, fixture thẻ tên tới y = 154 px; tọa độ `[trái, trên, phải, dưới]`:

| Thời điểm | Hộp bao (px) |
| --- | --- |
| 0,4 s | `[342,48; 166,00; 937,52; 622,59]` |
| 1,2 / 2,4 s | `[331,28; 166,00; 948,72; 639,79]` |
| 3,2 s | `[424,00; 166,00; 856,00; 515,26]` — trận đã mờ hết trước mốc này |

Probe in thêm đầy đủ mẫu camera ở 0,1 / 0,25 / 0,4 / 0,5 / 1,2 / 2,4 / 2,6 / 2,75 / 2,9 / 3,1 / 3,2 s. Tọa độ trên là phép chiếu CPU, không thay kết quả chụp host thật.

## Claude chạy tiếp

Cần host đang phục vụ **đúng worktree này**; kịch bản từ chối nếu chưa có trường của 433c. Không chạy build. Từ worktree:

```sh
BASE=http://127.0.0.1:3146/stress.html \
VIEWS=top \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-ult-rain-433c \
ART_MAGICK=/opt/homebrew/bin/magick \
../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs \
  src/lab/metal-ult-rain-review.mjs --width=1280 --height=720 --dpr=1
```

Kịch bản chụp bốn mốc đúng giờ ở góc chơi; in/lưu tọa độ trận, caster và đường cong camera; đo toàn khung qua `readPixels` đợi GPU trong cảnh khởi đầu **87 TargetField + 13 walker = 100 quái**, rồi kiểm tài nguyên qua năm lượt tung. Cổng **p95 ≤ 16,7 ms** vẫn là bắt buộc. Capture chỉ tạo khi Claude chạy: bốn ảnh, một sheet, `433c-measure.json`, `ABOUT.md`; tự cập nhật chỉ mục review.

Đối chiếu cờ tắt bằng cùng lệnh, đổi `BASE` thành `'http://127.0.0.1:3146/stress.html?ultCam=0'` và `OUT` sang thư mục `metal-ult-rain-433c-no-camera`. Nếu chỉ muốn số, thêm `METRICS_ONLY=1`; không tạo capture hoặc cập nhật chỉ mục.

Owner cần xem sheet bật/tắt camera, mức phóng kiếm cuối, vệt sáng và ground mark so với bản 433b/phân cảnh. Chưa có ảnh hoặc video 433c, chưa chấm đạt 8,5; p95 GPU và console còn chờ công cụ trình duyệt hoạt động.
