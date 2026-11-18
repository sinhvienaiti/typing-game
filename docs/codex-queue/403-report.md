# Phiếu 403 — Hoạt ảnh nhân vật, đợt 2 trong lab

Ngày 16/11/2026. Đã thêm góc chính diện, **10 thủ ấn**, **chưởng** và **kết trận** trên rig `human` có sẵn; giữ họ Kiếm A. **Kiểm kiểu và probe CPU 60/120 Hz đạt các cổng bên dưới.** Chưa có ảnh/video, nghe âm, đo phím thật → màn hình hoặc chấm chuyển động: browser host không khả dụng. Đã để lệnh chụp theo phương án dự phòng của phiếu; chưa tự nhận nghiệm thu hình ảnh hoặc chuẩn hệ dùng chung 9.

## Tệp và cách làm

Mọi mã nằm trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/`:

- `src/lab/anim-r2-poses.ts`: dữ liệu S0–S9 theo bảng §4 của 393; đủ 30 xương điều khiển ngón, phân biệt tay trái/phải. Tính hướng cánh tay từ vị trí cổ tay và chiều dài thật của rig bằng `PoseAuthor` đang có. Hai họ mới có sáu dáng gồng–nhả–theo đà và thu; bước trái 0,12 m, chân sau neo. Chưởng gom ở sườn rồi mở lòng, xoay hông và đẩy; kết trận vẽ hai tay lên trước ngực rồi ấn xuống, tiếp tục hạ trọng tâm.
- `src/lab/anim-r2-hands.ts`: xem ấn bằng chính `KeyPoser` của Animator, không thêm mixer. Chuyển ấn qua mở ngón → tách cổ tay → xoay vào ấn đích → khép ngón; mỗi đoạn 0,16 s. Có thể đổi ấn giữa đường. Chuyển từ xem ấn về chiêu lấy pose đang hiện, hòa 0,18 s. Sau khi đo được đỉnh giật khi nhập dồn, thêm giới hạn tốc độ riêng cho instance này: hông 180°/s, các khớp trên thân/ngón 1.800°/s, dịch chậu trước IK tối đa 0,15 m/s. Bộ lọc tiếp tục lắng sau khi pose hết trọng số, tránh bật ở khung về idle; không sửa Animator hoặc FootLock dùng chung.
- `src/lab/anim-r2-camera.ts`: nhìn thẳng theo mặt thực của nhân vật, tâm cao 1,13 m, cách 2,15 m. Góc xem tay **tạm ẩn toàn bộ lớp FX trước khi vẽ**, để vòng ngọc, phi kiếm và thẻ sáng không che ngón; sự kiện/âm vẫn chạy. Sau mỗi lần vẽ trả lại camera và đúng trạng thái hiển thị cũ. Đây là góc cô lập tay; xem VFX ở camera chơi.
- `src/lab/anim-r2-check.ts`: kiểm kiểu và probe riêng trên GLB thật; không chạy build hoặc bộ test game, không xuất clip hoặc ghi model.
- `src/lab/anim-r2-review.ts`: kịch bản chụp lưới 10 ấn và sáu bảng 8 pha, chờ Claude chạy bằng browser có quyền.
- `src/lab/anim-r1-poses.ts`: giữ phần gồng sâu, nhả, theo đà và bước 0,15 m của Kiếm A; thay S0/đường vào bằng thế hai tay có khoảng hở và dùng chung dữ liệu ngón đã kiểm. Đã sửa giao nhau ở S7 bằng khoảng đặt cổ tay phù hợp, không đan ngón.
- `src/lab/anim-r1-controller.ts`: chọn họ/ấn, dấu thời gian và phép đo đốt ngón; giữ ba xung chữ, sửa lùi, huỷ và đổi đích. Khi quay đích 180°, vô hiệu riêng phần “cheat” xoay một mình xương đòn trái của KeyPoser cho các slot thử nghiệm: hai tay quay cùng thân, đầu/cổ vẫn hướng theo đích. Cách cũ có thể làm hai tay xuyên nhau khi đổi hướng. Marker chuyển động nay kiểm thêm thay đổi quaternion thật của hông/tay so với chữ cuối.
- `src/lab/anim-r1-lab.ts`: phím và API đợt 2, giữ API đợt 1.
- `src/lab/skills-main.ts`: so với mốc đầu phiếu, chỉ thêm lời gọi `beforeDraw()` và truyền camera/lớp FX cho module lab. Giữ phần nối Kim 402, thứ tự phím 8, Y/P/I và các callback cũ.

Không sửa `wood-ult-*`, `metal-ult-*`, `ice-ult-*`, `src/view/`, `src/ui/`, scripts/tests hoặc docs của game. Trong lúc chạy có thay đổi đồng thời ở bốn tệp Mộc/Kim được theo dõi; tôi không ghi hoặc khôi phục chúng. Không tạo model, rig, ảnh, âm hoặc clip mới; dữ liệu pose chạy trực tiếp trong lab. Không commit, staging, đổi nhánh hoặc chạy các lệnh Git bị cấm.

## Phím và API

Mở `skills-lab.html?hero=human` trên host phục vụ đúng worktree.

| Phím | Kết quả |
| --- | --- |
| **F2** | Vào/ra chế độ thử hoạt ảnh |
| **F3** | Đổi Kiếm A → Chưởng → Kết trận; cũng rời chế độ xem ấn |
| **sword / palm / array** | Từ tương ứng; từng chữ đúng nối gồng, chữ cuối phát |
| **[ / ]** | Xem ấn trước/sau trong S0–S9, tự bật góc chính diện |
| **F4** | Bật/tắt góc chính diện; dùng được lúc gõ/tung chiêu |
| **Backspace / Escape** | Sửa lùi / huỷ, không phát chiêu; Escape cũng rời xem ấn |
| **Tab** | Đổi giữa bốn đích, gồm đích sau lưng |

Các ô nhập panel vẫn nhận phím của chúng. Không nhận composition, repeat, paste hoặc tổ hợp Ctrl/Meta/Alt làm chữ đúng. Kiếm cầm tay được ẩn trong chế độ kết ấn như đợt 1, trả lại trạng thái trước đó sau khi thu; chỉ ảnh hưởng lab.

`window.__labAnimR2`: `.family("sword" | "palm" | "array")`, `.seal(0…9)`, `.front(true | false)`, `.begin(word?)`, `.text(key)`, `.cancel()`, `.retarget(x,z)`, `.stop()`, `.report()`. API R1 tiếp tục có mặt. Báo cáo có họ, ấn, trạng thái chuyển ấn, khoảng cách ngón, marker phím/thân/FX/vẽ và sai khung.

Cả ba họ dùng lại **callback k1 hiện có** để đối nhịp chuyển động: sau thân và IK, cùng khung gọi `emitRelease("k1")`, VFX k1 và âm qua bus cũ. Không thêm look mới hoặc sát thương lần hai; chưa ghép recipe chưởng/trận riêng. Impact vẫn là sự kiện trúng thật từ projectile, nhật ký k1 theo thứ tự thời gian, không gán giả cast ID.

## Kiểm tra đã chạy

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --import tsx src/lab/anim-r2-check.ts
```

TypeScript strict và `noUncheckedIndexedAccess`: **0 chẩn đoán**, gồm chín tệp ở trên và chuỗi import. Probe nạp rig 66 khớp, đúng chiều cao 1,65 m và wrapper của `human`.

Mỗi tần số: 10 ấn tĩnh; **90 cặp chuyển có thứ tự** và đổi tiếp giữa đường; ba họ × từ 3/4/5/8 chữ ở 15/45/90 WPM, nhập dồn; đổi họ giữa gồng/nhả/theo đà/thu; sai, Backspace, huỷ, đổi đích 180°, guard không khả dụng và nhả sau cập nhật `dt=0`. Tổng **45 callback nhả/tần số**, đúng một callback mỗi chữ cuối đã nhận; thân/FX/vẽ giả lập cùng khung. Kiểm phép chiếu đủ đầu ngón của 10 ấn trong khung chính diện 16:9, trả lại camera và trạng thái FX cả khi FX vốn đang ẩn.

| Chỉ số CPU theo bước cố định | 60 Hz | 120 Hz |
| --- | ---: | ---: |
| Khung quét | 15.494 | 30.563 |
| Chữ cuối → thân, tối đa | **16,667 ms** | **8,334 ms** |
| Chữ cuối → pha nhả có chuyển động khớp thật, tối đa | **16,667 ms** | **8,334 ms** |
| Sai khung thân/FX/vẽ giả lập | 0 | 0 |
| Khoảng cách nhỏ nhất giữa các đoạn đốt ngón | **16,255 mm** | **16,252 mm** |
| Khung vi phạm khe 4 mm | **0** | **0** |
| Mẫu chân trụ được đo | 26.950 | 53.230 |
| Tốc trượt chân trụ lớn nhất | **0,04066 m/s** | **0,04463 m/s** |
| Khung gần bind/T-pose theo hai cánh tay | **0** | **0** |
| Bước góc tay/cánh tay lớn nhất | **30,00°** | **15,00°** |
| Y nhỏ nhất ở khớp ball chân | +0,00750 m | +0,00749 m |

Độ trễ trong từng nhóm mười lần phát của **mỗi họ** đều tối đa 16,657 ms ở 60 Hz và 8,324 ms ở 120 Hz; bảng dùng cả những ca chuyển/ngắt và dừng đồng hồ nên cao hơn một chút. Góc tay bị giới hạn theo giây, không theo số khung.

Khoảng cách được đo trên **405 cặp đoạn mỗi khung**: ba đốt từ gốc đến khớp lá của mỗi ngón, gồm cả cặp khác bàn tay; bỏ cặp cùng một ngón. Dùng khoảng cách gần nhất giữa hai đoạn kín, không chỉ đo đầu ngón. Chân đo sau lớp/IK, lấy tốc ngang nhỏ hơn của ankle/ball để tính đúng pivot, chỉ khi khoá liên tiếp và không bước. Mọi quaternion/vị trí đều hữu hạn. Các cổng có assertion trong lệnh kiểm, không chỉ in số.

## Lệnh chụp và phần cần xem

CUA hiện trả **`Browsers: Error: The browser access host is unavailable`**, inventory không có browser. Đã kết thúc phần CUA; không mở server hoặc tìm driver khác để vượt chặn. Chưa chạy kịch bản chụp và chưa tạo thư mục review/capture.

Khi Claude có browser/quyền ghi review, phục vụ **đúng worktree**, chỉ dùng cổng 3146 nếu nó đang phục vụ worktree đó:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/skills-lab.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node --import tsx src/kit/tools/cdp-run.mjs src/lab/anim-r2-review.ts \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản kiểm API phiên bản 403, chụp 58 khung rồi ghép **một lưới 5×2 thủ ấn** và **sáu bảng 4×2 pha**: ba họ × camera chơi/chính diện. Các pha: sẵn, gồng sớm, giữa, cuộn, nhả F1, nhả F3, theo đà, thu. Dùng Arial của macOS. Có `ABOUT.md`, `403-browser.json`, console/exceptions; mỗi lượt có thư mục riêng trong `typing-game-review/captures/tu-tien/hero-anim-r2-403/run-*`. Hard link bảy bảng và JSON sang `owner-review/2026-11-16/tu-tien/hero-anim-r2/run-*`. Chạy prune xem trước rồi áp dụng cho đúng lượt vừa tạo, giữ bảng và JSON, xoá ảnh thô của mình; cuối cùng cập nhật index. Không đặt capture vào `art-src`, `public` hoặc `docs`.

**Điểm yếu/chưa xác nhận:**

- Các số trên là lịch fixed-step CPU; callback FX trong probe là stub, dấu vẽ là giả lập. Chưa đo hàng đợi OS/browser, GPU/present hoặc onset loa. Cùng khung gọi bus chưa chứng minh hình/âm đã hiện cùng lúc trên thiết bị.
- Khe đoạn xương ≥ 4 mm và phép chiếu không thay thế xem mesh da: cần xem ngón cái giữ ngoài nắm, lòng tay, khe S7, chạm gần giữa hai tay, cổ tay và skin khi đổi ấn. Mười dáng là bản dựng trên proxy, chưa được giám khảo xác nhận đúng/đẹp theo bảng nghiên cứu.
- Cần xem video tốc độ thật ở camera chơi: lực chân–hông–vai của chưởng, đường vẽ/ấn đất của kết trận, đổi họ khi nhập nhanh và quay 180°. Giới hạn tốc độ khớp có thể làm đỉnh cử chỉ đến muộn hơn; marker phát vẫn giữ ngay. Chưa khẳng định mượt về cảm nhận từ số đo.
- Góc chính diện cố ý cô lập FX; kiểm đối nhịp VFX ở camera chơi. Recipe chưởng/trận riêng, nhân vật nữ thật, rig mới, nghiệm thu âm/hình và hai giám khảo chuẩn 9 chưa thuộc phần đã hoàn thành.

Hạn mức đầu phiếu: đã dùng 47%, còn 53%; không gặp giới hạn quota hoặc giờ bắt buộc chờ. Không gọi công cụ tạo ảnh vì phiếu yêu cầu hoạt ảnh trên rig có sẵn.
