# Phiếu 415b — Cong ngón mềm cho rig `human`

Ngày 16/11/2026. **PASS nghiệm thu số ở 60/120 Hz; TypeScript strict + `noUncheckedIndexedAccess`: 0 chẩn đoán.** Giữ phần điều khiển ngón, pole khuỷu, IK và các cổng của 415. Chưa chụp browser hoặc chấm mắt; Claude Opus thực hiện phần đó sau theo phiếu.

## Đã sửa

Chỉ bảy tệp trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/src/lab/` và báo cáo này:

- `anim-r3-fingers.ts`: `FingerSetting.curl` là một số 0–1. Nhân toàn bộ tỉ lệ với cùng một hệ số, lấy hệ số lớn nhất còn nằm trong giới hạn của cả ba đốt; không cắt riêng từng góc làm lệch tỉ lệ.
- `anim-r3-seals.json`: thêm hợp đồng tỉ lệ/giới hạn và một curl cho từng ngón ở cả hai tay, đủ S0–S9. Giữ các trạng thái, vùng cổ tay, hướng lòng và ngoại lệ tiếp xúc đã có.
- `anim-r3-poses.ts`: đọc curl từ JSON. Bộ fit tiếp xúc ngón cái chỉ tìm xoè/xoắn, giữ nguyên curl đã soạn; không còn ba biến gập độc lập. Giữ bảng xoè và cơ chế pole/cache của 415.
- `anim-r1-lab.ts`: giữ API `version:415`, thêm `curlVersion:'415b'`; `.finger(...)` nhận thêm `curl`. Từ chối curl không hữu hạn hoặc ngoài 0–1.
- `anim-r3-check.ts`: đo góc gập thật từ quaternion xương, bỏ rest fan rồi tách xoè/xoắn trong hệ lòng tay. In bảng đủ 100 ngón mỗi Hz: trạng thái, curl JSON/thực đo, ba góc, sai số tỉ lệ và PASS. Giữ các cổng cũ.
- `anim-r3-measurements.json`: kết quả cuối, `ticket:'415b'`, `baseTicket:415`, `pass:true`, `errors:[]`.
- `anim-r3-review.ts`: nhận diện đúng API 415b/human và dùng tên/thư mục capture riêng của 415b, giữ cách so ảnh 411 của 415.

| Loại ngón | Tỉ lệ gốc : giữa : ngọn | Góc tại curl=1 | Giới hạn từng đốt |
|---|---|---|---|
| Trỏ–út | 1 : 1,1 : 0,8 | 85° : 93,5° : 68° | 85° : 100° : 75° |
| Cái | 1 : 1,2 : 1,4 | 50° : 60° : 70° | 50° : 60° : 70° |

Ngón duỗi dùng 0,08 (trỏ–út) hoặc 0,12 (cái). Ngón gập dùng 0,75 hoặc 0,82. Cụ thể S4 hai tay, S8 phải và nắm S5 trái/S6 phải dùng 0,75; các ngón gập còn lại dùng 0,82. Ngón cái tiếp xúc: S0 phải/trái 0,16/0,36; S1 hai tay và S9 phải 0,67; S5 trái/S6 phải 1. Trạng thái tiếp xúc vẫn riêng với gập/duỗi như JSON gốc.

Ví dụ sau khi chọn ấn:

```js
window.__labAnimR3.seal(3);
window.__labAnimR3.finger('r', 'index', { curl: 0.12 });
```

## Kiểm chứng

Chạy riêng checker của lab, không chạy build hoặc bộ test game:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --import tsx src/lab/anim-r3-check.ts
node --import tsx src/lab/anim-r3-check.ts --json > src/lab/anim-r3-measurements.json
```

| Cổng / số đo | 60 Hz | 120 Hz |
|---|---:|---:|
| Ngón đúng curl, tỉ lệ, giới hạn và trạng thái JSON | 100/100 | 100/100 |
| Sai số tỉ lệ lớn nhất, làm tròn 4 chữ số (%) | 0,0000 | 0,0000 |
| Ca rig thật tại curl 0 / 0,15 / 0,75 / 1 | 40/40 | 40/40 |
| Khe tâm đoạn nhỏ nhất toàn chuyển, sau ngoại lệ đúng cặp | 5,3130 mm | 5,3130 mm |
| Khung ấn/chuyển ấn | 6.490 | 12.880 |
| Phím→thân và phím→chuyển động lớn nhất | 16,6567 ms | 8,3233 ms |
| Rời ấn→phát ngay, đúng một lần | 30/30 | 30/30 |
| Độ sâu cổ tay khi chuyển | 0,1143–0,2950 m | 0,1142–0,2950 m |
| Gập cổ tay lớn nhất | 68° | 68° |
| Khe da đầu ngón khi xoè/curl/xoắn=0, lớn nhất | 6,9153 mm | 6,9153 mm |

Mỗi Hz vẫn kiểm 90 chuyển ấn có thứ tự, 270 ca ngắt giữa chuyển, 405 cặp đoạn mỗi khung; ba họ sword/palm/array đều 10/10 lần phát, đúng frame thân/FX/vẽ. Các cổng vùng cổ tay, khuỷu, hướng lòng, camera và API chỉnh thật của 415 đều đạt. Quét curl trên rig thật kết hợp xoè 10°/xoắn 20°; sai số góc so với công thức <0,001°. API curl=0,12 đưa trỏ phải tới `[10,2°; 11,22°; 8,16°]`, giữ các ngón khác; giá trị -0,1/1,1/NaN đều bị từ chối.

## Lệnh chụp cho Claude Opus

Claude phục vụ **đúng worktree này**, rồi chạy (3146 là cổng ví dụ):

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/skills-lab.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node --import tsx src/kit/tools/cdp-run.mjs src/lab/anim-r3-review.ts \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản xuất lưới cận tay `415b-seals-hands-10-compare-sheet.jpg`, 10 cặp `415b-hands-S<n>-pair-compare.jpg`; có thêm lưới/cặp nửa thân và `415b-browser.json`. Đích: `typing-game-review/captures/tu-tien/hero-anim-r3-415b/run-*`, hard link sang `owner-review/2026-11-16/tu-tien/hero-anim-r3-415b/run-*`; có `ABOUT.md`, prune ảnh thô của lượt chụp và dựng lại index. Script đã qua kiểm kiểu; chưa thực thi capture.

## Claude/owner cần xem

So từng ngón với ảnh 411, nhất là nắm S5 trái/S6 phải khi ngón cái đạt curl=1. Khe đầu xương cái–trỏ ở hai trường hợp này là 24,9083/24,9078 mm, đạt cổng tiếp cận <25 mm nhưng chưa chứng minh da chạm. S0 hai đầu cái cách 19,3168/19,3309 mm (60/120 Hz). Đo khoảng cách xương không thay thế kiểm va chạm bề mặt da hoặc chấm độ cong bằng mắt.

Giữ lưu ý từ 415: chuyển S7→S8 vẫn có bước quaternion cẳng tay trái lớn nhất 63,6141° tại 60 Hz, 33,2558° tại 120 Hz; cần xem chuyển động ở tốc độ thật. Phiếu này không sửa đường chuyển khuỷu.

Không tạo ảnh/model/âm thanh/video mới, không chạy server/browser và không tự chấm thị giác vì phần này giao Claude Opus sau nghiệm thu Codex. Không sửa bản chính Tu Tiên, scripts/tests/docs game hoặc đường dẫn lane khác. Không staging, commit, push, reset, clean, stash hay đổi nhánh. Không gặp hạn mức hoặc giờ bắt buộc chờ.
