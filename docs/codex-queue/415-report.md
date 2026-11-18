# Phiếu 415 — Điều khiển ngón và pole khuỷu cho `human`

Ngày 16/11/2026. **PASS các cổng số của phiếu tại 60/120 Hz; strict + `noUncheckedIndexedAccess`: 0 chẩn đoán.** Chưa chụp browser hoặc chấm mắt. Claude Opus tiếp tục so từng ấn với ảnh 411, mục tiêu ≥7/10 theo phân công của phiếu.

## Đã làm

Trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/`:

- `src/lab/anim-r3-fingers.ts` — mới: đo `rig.restQ/restP` thật; lấy trục gốc→đầu mỗi ngón, bù độ xoè/nghiêng của rest về trục dọc bàn tay trước khi áp góc. `abduction` quanh pháp tuyến lòng tay và `twist` quanh trục dọc là hai góc riêng ở đốt gốc của cả năm ngón, hai tay. Đổi về quaternion cục bộ qua parent/rest đã đo. Không đổi vị trí, chiều dài, scale xương hoặc mesh.
- `src/lab/anim-r3-poses.ts` — dùng điều khiển đã hiệu chuẩn cho toàn bộ S0–S9; bảng góc xoè riêng cho mười ấn. S1/S9 giữ trỏ–giữa song song; S2 mở nhẹ cặp này và đặt cổ tay x=±0,12 m để hai ngón cái không cắt nhau. S1 trái sửa hướng lòng vào trong. S5 trái chuyển từ `[-0,15; 0,90; +0,22]` sang `[-0,06; 0,94; +0,23]` theo hệ soạn (phải, cao, trước).
- Cùng tệp: IK hai xương lấy **điểm pole độc lập với hướng ngón/lòng tay**. Mặc định phải `[+0,12; 0,85; +0,06]`, trái `[-0,12; 0,85; +0,06]` m, kéo xuống và sát thân. Có pole riêng từng tay/từng ấn; giữ nội suy khung khuỷu, thêm hướng dự phòng khi pole thẳng hàng với trục vai–cổ tay. Cache ngón bị hủy đúng tay khi chỉnh.
- `src/lab/anim-r3-seals.json` — giữ nguyên vùng cổ tay, trạng thái ngón, hướng lòng và các cặp ngoại lệ của 412; thêm ngưỡng 415, metadata `ticket:415/baseTicket:412`. Dữ liệu gập ba đốt vẫn là của 412; cong mềm và tỉ lệ ngón cái để phiếu 415b.
- `src/lab/anim-r3-check.ts` — giữ cổng 412, thêm kiểm xoè=0, phản ứng xoè/xoắn độc lập cả mười ngón, vị trí khuỷu, S5 và API chỉnh thật qua cache. Mặc định in bảng S0–S9 cho từng Hz; `--json` xuất đầy đủ số đo.
- `src/lab/anim-r3-measurements.json` — kết quả thật của lượt cuối, `pass:true`, `errors:[]`.
- `src/lab/anim-r1-lab.ts` — API R3 phiên bản **415**, thêm `.finger(...)` và `.pole(...)`; không đổi luật gõ hoặc phát chiêu.
- `src/lab/anim-r3-review.ts` — nhận diện đúng host/API 415, tên ảnh và thư mục 415 riêng; giữ cách chụp cặp tham chiếu trái / human phải.

Ví dụ chỉnh trong lab, sau khi chọn ấn (góc tính bằng độ; điểm pole theo hệ phải/cao/trước):

```js
window.__labAnimR3.seal(3);
window.__labAnimR3.finger('r', 'index', { abduction: 0, twist: 0 });
window.__labAnimR3.pole('r', [0.12, 0.85, 0.06]);
```

Giá trị chỉnh được giữ riêng từng ấn trong phiên lab. Chỉnh thủ công ngón cái ưu tiên góc yêu cầu, không bị bộ fit tiếp xúc ghi đè. Tải lại trang trả về dữ liệu mặc định.

## Phép đo và kết quả

GLB thật `human-base-animations.glb`, 66 khớp; kiểm chiều cao **1,65 m trong world**. Khoảng cách lấy từ `getWorldPosition`; tọa độ trình bày trong hệ rig có scale 1, tương đương mét thế giới sau bỏ phép quay/tịnh tiến root. Mặt phẳng giữa thân đi qua `spine_03`, pháp tuyến ngang theo chuyển động thật của thân so với rest. Khuỷu=`lowerarm`, vai=`upperarm`.

**Diễn giải khe ≤8 mm:** khe ngang giữa **bề mặt đầu ngón**, không phải khoảng cách Euclid giữa hai đầu xương dài/ngắn khác nhau. Đặt curl/xoè/xoắn=0; kiểm ba cặp trỏ–giữa, giữa–áp út, áp út–út trên mỗi tay. Lấy vertex da thật có trọng số ngón ≥0,5, chỉ **10% cuối chiều dài ngón**, chiếu lên trục ngang lòng tay, đo khe giữa hai silhouette. Bản 35% cuối cũng được lưu để đối chiếu, không dùng phần gốc rộng đó để cho cổng đầu ngón PASS. Đây không phải khoảng cách tối đa của mọi lát cắt trên chóp tròn. Ngón cái là ngón đối, kiểm điều khiển riêng, không gộp cái–trỏ vào ba cặp song song.

| Cặp, cả hai tay | Khe da đầu ngón khi xoè=0 | Góc giữa hai trục |
|---|---:|---:|
| Trỏ–giữa | 6,9153 mm | <0,01° |
| Giữa–áp út | 5,5596 mm | <0,01° |
| Áp út–út | 6,9014 mm | <0,01° |

Trục là gốc→đầu ngón; số làm tròn góc trong JSON là 0°. Khoảng cách tâm ngang vẫn 23,37–24,98 mm, được công khai riêng. Không trừ bán kính giả định, không đổi cổng tâm xương của 412. Mỗi đầu ngón có 22–25 vertex trong dải 10% cuối.

Xoè +10° làm trục ngón đổi 10°; xoắn +10° giữ trục và đổi quaternion 10°, kiểm từng ngón kể cả cái. Không đổi quaternion khớp khác. API thật chỉnh trỏ cho thay đổi 14,1331° khi xoè/xoắn cùng +10°; đổi pole dịch khuỷu **0,0392 m**, dịch cổ tay **0 m**, và dữ liệu chỉnh vẫn giữ sau đổi ấn rồi trở lại.

| Ấn | Khe tâm đốt nhỏ nhất, 60 / 120 Hz (mm) | Lệch ngang khuỷu phải / trái (m, 60 Hz) | Vai cao hơn khuỷu phải / trái (m, 60 Hz) | Cao cổ tay trái (m) |
|---|---:|---:|---:|---:|
| S0 | 7.8791 / 7.8725 | 0.1533 / 0.1512 | 0.2467 / 0.2465 | 0.900 |
| S1 | 23.4302 / 23.4302 | 0.1420 / 0.1303 | 0.2197 / 0.2435 | 1.020 |
| S2 | 23.4302 / 23.4302 | 0.1437 / 0.1392 | 0.2344 / 0.2338 | 1.100 |
| S3 | 22.1292 / 22.1292 | 0.1432 / 0.1383 | 0.2342 / 0.2278 | 0.900 |
| S4 | 23.3916 / 23.3916 | 0.1435 / 0.1393 | 0.2344 / 0.2340 | 0.920 |
| S5 | 22.1292 / 22.1292 | 0.1458 / 0.1392 | 0.2222 / 0.2320 | 0.940 |
| S6 | 22.8275 / 22.8275 | 0.1343 / 0.0916 | 0.1220 / 0.1866 | 1.170 |
| S7 | 18.5062 / 18.5062 | 0.1374 / 0.1322 | 0.2256 / 0.2245 | 1.120 |
| S8 | 22.8275 / 22.8275 | 0.1451 / 0.1382 | 0.2123 / 0.2337 | 0.910 |
| S9 | 22.8275 / 22.8275 | 0.1247 / 0.1141 | 0.1258 / 0.2005 | 1.195 |

Mỗi ấn đều đạt hướng lòng, trạng thái ngón, vùng JSON với dung sai ±0,03 m và tiếp xúc theo đúng cặp. Cả hai Hz: lệch ngang khuỷu lớn nhất **0,1533 m <0,25 m**; khuỷu thấp hơn vai ít nhất **0,1220 m**. S5 trái: cổ tay hệ rig `[-0,06; 0,94; -0,23]` m, độ sâu trước thân **0,2641 m**; cao 0,94 m nằm trong vùng bụng gốc **0,78–1,06 m**, không cần dùng dung sai.

| Cổng / số đo | 60 Hz | 120 Hz |
|---|---:|---:|
| Khung ấn/chuyển ấn | 6.490 | 12.880 |
| Khe tâm đoạn nhỏ nhất toàn chuyển, sau ngoại lệ đúng cặp | 5,9897 mm | 5,9909 mm |
| Độ sâu cổ tay khi chuyển | 0,1143–0,2950 m | 0,1142–0,2950 m |
| Gập cổ tay lớn nhất | 68° | 68° |
| Phím→thân và phím→chuyển động lớn nhất | 16,6567 ms | 8,3233 ms |
| Phát ngay khi rời ấn, đúng một lần | 30/30 | 30/30 |

Mỗi Hz giữ 90 chuyển ấn có thứ tự, 270 ca ngắt ở 0,05/0,125/0,20 s, 405 cặp đoạn đốt khác ngón mỗi khung. Chỉ miễn đúng các cặp tiếp xúc trong JSON. Ba họ sword/palm/array đều 10/10 lần phát, đúng frame thân/FX/vẽ, có chuyển động thật, ≤50 ms; thêm 30 ca rời ấn→phát ngay. Kiểm camera không cắt đầu ngón và phục hồi camera/FX vẫn đạt.

## Lệnh kiểm và chụp

Đã chạy cả chế độ bảng và JSON, cùng cách kiểm strict cô lập của 412; không chạy build hoặc bộ test game:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --import tsx src/lab/anim-r3-check.ts
node --import tsx src/lab/anim-r3-check.ts --json > src/lab/anim-r3-measurements.json
```

Claude Opus phục vụ đúng worktree này rồi chạy (3146 là cổng ví dụ; Codex không mở server/browser):

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/skills-lab.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node --import tsx src/kit/tools/cdp-run.mjs src/lab/anim-r3-review.ts \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản chờ API 415/human trước khi tạo thư mục, xuất hai lưới `415-seals-{front|hands}-10-compare-sheet.jpg`, 20 cặp `415-{front|hands}-S<n>-pair-compare.jpg` và `415-browser.json`. Nguồn là ảnh riêng của repo thuộc bộ 411. Đích `typing-game-review/captures/tu-tien/hero-anim-r3-415/run-*`, hard link sang `owner-review/2026-11-16/tu-tien/hero-anim-r3-415/run-*`; có `ABOUT.md`, prune ảnh thô của lượt đó và dựng lại index. **Chỉ kiểm kiểu kịch bản; chưa thực thi capture.**

## Claude/owner cần xem

So mười ấn với ảnh 411, nhất là da ngón cái, nắm S5 trước bụng, dáng khuỷu S3/S4/S8 và tay đỡ S6/S9. S0 đầu cái cách 23,93–23,94 mm, đạt cổng tiếp cận <25 mm của 412 nhưng chưa chứng minh da chạm như ảnh. Tay đỡ S6 cách cổ tay phải 6,775 mm, S9 16,168 mm. Cần xem video tốc độ thật S7→S8: bước quaternion cẳng tay trái lớn nhất 63,6141° tại 60 Hz, 33,2558° tại 120 Hz; không coi số đo CPU là bằng chứng mượt bằng mắt.

Không làm phần cong mềm/tỉ lệ ngón cái của 415b, không tạo ảnh/model/âm thanh/video mới, không chấm thị giác hoặc tuyên bố đạt 7/10. Chỉ ghi bảy tệp `src/lab/anim-r*` nêu trên và báo cáo này; không sửa `*-ult-*`, `src/view`, `src/ui`, bản chính Tu Tiên, scripts/tests/docs game hoặc file của lane khác. Không staging, commit, push, reset, clean, stash hay đổi nhánh. Không gặp hạn mức hoặc giờ bắt buộc chờ.
