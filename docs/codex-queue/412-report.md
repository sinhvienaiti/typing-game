# Phiếu 412 — Dựng 10 thủ ấn theo ảnh 411

Ngày 16/11/2026. **Đã dựng lại S0–S9, kiểm kiểu strict 0 lỗi và probe CPU 60/120 Hz PASS.** Chưa chụp hoặc chấm bằng mắt; phần này để Claude Opus thực hiện theo phiếu. Bảng dưới được viết sau khi xem ảnh ghép và ảnh cận try3, **trước khi sửa tư thế**. Trái/phải là của nhân vật.

## Chuẩn S0–S9

Thứ tự ngón trong bảng: **cái, trỏ, giữa, áp út, út**. D = duỗi (<40° tổng gập), G = gập (>120°), C = chạm ngón khác (đo vị trí tiếp xúc, không áp ngưỡng D/G). S4/S8 gập mở gần đầu thấp ngưỡng G để giữ hình C. Các mặt khuất là diễn giải, chờ Claude Opus so ảnh.

| Ấn | Phải: ngón; vùng; lòng | Trái: ngón; vùng; lòng | Tiếp xúc / ngoại lệ |
|---|---|---|---|
| S0 Origin Rest | C, D, D, D, D; bụng; lên | C, D, D, D, D; bụng; lên | Hai đầu ngón cái chạm; tay phải đặt trên lòng tay trái. Không đan ngón. |
| S1 Sword Fingers | C, D, D, G, G; ngực; trước | C, D, D, G, G; bụng; trong | Mỗi ngón cái giữ hai ngón áp út/út của cùng bàn tay; hai tay tách. |
| S2 Sprouting Branches | D, D, D, G, G; ngực; trong | D, D, D, G, G; ngực; trong | Không tiếp xúc giữa hai tay, không đan; trỏ/giữa dựng cong mềm. |
| S3 Guiding Flow | D, D, D, D, D; ngực; lên | D, D, D, D, D; bụng; xuống | Tay phải trên ngửa, tay trái dưới úp; không tiếp xúc. |
| S4 Hidden Ember | D, G, G, G, G; ngực; trước | D, G, G, G, G; bụng; lên | Hai bàn tay tạo hai nửa bầu khí rời nhau; cong từng đốt, không nắm kín. |
| S5 Mountain Ward | D, D, D, D, D; ngực; trước | C, G, G, G, G; bụng; lên | Tay phải dựng mở; trái nắm ở eo, ngón cái phủ ngoài ngón trỏ. Hai tay tách. |
| S6 Thunder Command | C, G, G, G, G; mặt; trong | D, D, D, D, D; ngực; trong | Tay trái đỡ phía dưới cổ tay phải; cái phải phủ ngoài trỏ/giữa của nắm. |
| S7 Crystal Closure | D, D, D, D, D; ngực; trong | D, D, D, D, D; ngực; trong | Hai lòng tay đối nhau, khe 4–8 cm; không áp lòng, không đan. |
| S8 Guiding Wind | D, D, D, G, G; ngực; xuống | D, D, D, D, D; bụng; lên | Trỏ/giữa phải dẫn ngang, áp út/út gập; trái đỡ thấp, không chạm. |
| S9 Opening Heaven | C, D, D, G, G; mặt; trước | D, D, D, D, D; ngực; lên | Tay trái đỡ cổ tay phải; cái phải giữ áp út/út; trỏ/giữa hướng lên bên mặt. |

Nguồn máy đọc: `games/.wt-ic-lab-all/src/lab/anim-r3-seals.json`. Vùng cổ tay theo rig 1,65 m: bụng 0,78–1,06 m; ngực 1,06–1,32 m; mặt 1,32–1,52 m. Giới hạn độ sâu tính trước mặt phẳng thân tại spine_03, theo hướng thân; không lấy khoảng cách tới camera. Ngoại lệ khe chỉ áp đúng cặp trong JSON: S0 cái–cái; S1/S9 cái–áp út/út; S5 trái cái–trỏ/giữa; S6 phải cái–trỏ/giữa. S6/S9 đỡ cổ tay không miễn các cặp ngón khác.

## Thực hiện

Mã trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/`:

- `src/lab/anim-r3-seals.json`: chuẩn từng ngón, vùng cổ tay, hướng lòng, tiếp xúc và ngoại lệ có tên cặp. Script đọc trực tiếp tệp này; không suy ngược trạng thái mong muốn từ góc đã dựng.
- `src/lab/anim-r3-poses.ts`: kế hoạch cổ tay/hướng tay của 10 ấn, IK vai–khuỷu–cổ tay theo chiều dài thật; đủ **30 xương ngón**, mỗi ngón ba đốt. Các ngón cái giữ ngón gập được khớp trên bản sao bàn tay bằng tìm kiếm tọa độ xác định, lưu cache; không sửa rig/mesh. S0 khớp hai ngón cái tới cùng điểm. S3 phải trên ngửa/trái dưới úp; S6/S9 tay trái tới cổ tay phải; S7 không đan, không ép hai lòng.
- `src/lab/anim-r2-hands.ts`: giữ đường KeyPoser đang có và bộ hòa khi thoát; thêm driver R3 **chỉ khi xem ấn**. Chuyển 280 ms: tách theo chiều sâu, mở đường hai cổ tay, đổi vùng/hướng/ngón, khép cổ tay, trả chiều sâu. Nội suy quintic; khi ngắt lấy đúng tư thế đang hiện. Bộ giới hạn khi thoát cũng lưu lại quaternion R3 thực sự đã vẽ, tránh lấy nhầm pose R2 bên dưới. Nội suy khung khuỷu đã chụp thay vì tính lại một pole ngắn nhất mỗi khung, để tránh lật khuỷu tại điểm suy biến. Giới hạn gập cổ tay 68°, khoảng đệm độ sâu 0,055–0,295 m; không đổi chiều dài xương.
- `src/lab/anim-r3-geometry.ts`: chuyển nguyên phép khoảng cách đoạn kín từ R2 sang tệp dùng chung; R2 vẫn export API cũ, tránh import vòng với driver R3.
- `src/lab/anim-r2-camera.ts`: thêm khung nửa thân so ảnh 411 và góc cận lấy bounds hai bàn tay; giữ camera 403 khi không bật so sánh. Mỗi lần vẽ trả lại vị trí, quaternion và đúng trạng thái FX cũ.
- `src/lab/anim-r1-lab.ts`: API `window.__labAnimR3` phiên bản **412**, `.seal(0…9)`, `.compare("front" | "hands")`, `.report()`, `.stop()`; API R1/R2 còn nguyên. `[ / ]` xem ấn và bật khung nửa thân; **Shift+F4** đổi nửa thân/cận tay; F4 bật/tắt camera. Không cần sửa `skills-main.ts`.
- `src/lab/anim-r1-controller.ts`: chỉ đổi nhãn tên ấn theo 411 và thêm hướng dẫn Shift+F4. Không đổi luật gõ, phát chiêu, marker hoặc lớp chuyển động của ba họ.
- `src/lab/anim-r3-check.ts`: probe độc lập và kiểm kiểu có assert; `anim-r3-measurements.json` lưu kết quả thật đầy đủ.
- `src/lab/anim-r3-review.ts`: lệnh chụp hai lưới đối chiếu và 20 cặp chi tiết, chờ Claude chạy.

Dữ liệu Kiếm A trong `anim-r1-poses.ts` và dữ liệu chưởng/kết trận trong `anim-r2-poses.ts` **không sửa**. Driver R3 dừng khi rời xem ấn; không thêm mixer, sự kiện phát, VFX hoặc âm mới. Không đụng `*-ult-*`, `skills-main.ts`, `src/view/`, `src/ui/`, scripts/tests hoặc docs của game.

## Bảng góc khớp chính

Số đo ở pose cuối, 60 Hz. Bộ ba là Euler **[x, y, z]**, độ, thứ tự YZX, của thay đổi quaternion cục bộ so với rest; không dùng độ lớn Euler để thay cho góc gập cổ tay. Cột gập đo trực tiếp giữa trục bàn tay và cẳng tay. JSON giữ cả số đo 120 Hz và ba đốt của từng ngón.

| Ấn / tay | Vai (upperarm) | Khuỷu (lowerarm) | Cổ tay (hand) | Gập cổ tay |
|---|---|---|---|---:|
| S0 phải | [-33.7, -17.6, 43.0] | [-76.0, 116.4, 52.8] | [-38.3, 11.2, 31.7] | 41.98° |
| S0 trái | [-38.3, 19.8, -43.8] | [-54.8, -95.2, -52.7] | [-43.3, -15.5, -37.9] | 49.26° |
| S1 phải | [-39.1, -19.1, 49.0] | [171.5, 105.6, -59.2] | [-7.9, -1.8, -25.5] | 25.68° |
| S1 trái | [-40.9, 24.9, -22.8] | [120.6, -8.0, 62.0] | [24.1, -13.2, 57.1] | 63.05° |
| S2 phải | [-56.5, -27.9, 48.6] | [138.6, 49.2, -52.3] | [8.9, 2.8, -35.2] | 39.10° |
| S2 trái | [-56.9, 27.8, -49.5] | [139.8, -49.7, 53.7] | [7.7, -2.5, 35.6] | 38.95° |
| S3 phải | [-14.5, -7.4, 30.4] | [-116.9, 165.3, 26.4] | [-41.6, 6.1, 15.8] | 35.90° |
| S3 trái | [-28.8, 15.3, -39.9] | [67.8, 67.8, 46.2] | [25.3, -8.0, 34.6] | 47.21° |
| S4 phải | [-56.8, -28.2, 48.5] | [-177.7, 108.4, -57.3] | [-12.9, -4.1, -35.2] | 35.54° |
| S4 trái | [-37.0, 20.0, -39.5] | [-75.0, -125.1, -50.0] | [-56.5, -21.6, -39.0] | 58.30° |
| S5 phải | [-51.7, -20.1, 60.1] | [163.9, 113.0, -56.3] | [-5.7, -1.1, -22.5] | 22.86° |
| S5 trái | [-66.4, 43.7, -19.7] | [-11.3, -94.5, -77.9] | [-10.6, -2.2, -23.9] | 23.77° |
| S6 phải | [-51.2, 4.9, 82.4] | [120.9, 79.7, -41.7] | [-3.5, -0.2, -5.6] | 7.95° |
| S6 trái | [-72.0, 2.4, -77.0] | [84.5, 6.1, -46.8] | [16.0, 3.7, -26.0] | 35.25° |
| S7 phải | [-67.5, -29.4, 55.8] | [113.2, 8.1, -27.7] | [32.0, 6.4, -22.1] | 45.63° |
| S7 trái | [-68.0, 29.0, -56.6] | [112.5, -7.3, 29.1] | [31.9, -6.7, 23.2] | 45.95° |
| S8 phải | [2.1, 3.7, 22.6] | [120.5, 3.4, 6.1] | [27.2, -1.1, 4.7] | 36.29° |
| S8 trái | [-32.0, 17.1, -40.0] | [-68.4, -110.5, -52.1] | [-46.4, -16.4, -37.2] | 50.66° |
| S9 phải | [-32.0, -8.3, 73.6] | [176.8, 132.6, -66.1] | [-8.9, -0.6, -7.7] | 7.88° |
| S9 trái | [-35.4, 12.3, -66.1] | [-109.3, 177.5, -24.2] | [-24.2, -1.5, -7.1] | 16.78° |

Ngón duỗi thông thường: **6°/10°/6°**; cái duỗi **6°/9°/6°**. Ngón gập: **52°/58°/35°** (145°); gập mở S4/S8: **35°/52°/36°** (123°). S7 cái mở nhẹ **−8°/−6°/−4°**, tổng trị tuyệt đối 18°; thêm góc mở/đối ngón ở đốt gốc để hai tay không cắt nhau. Các ngón cái C dùng góc fit riêng, đầy đủ trong JSON, không bị ép về một nắm tay chung. Ở ảnh, S4/S8 cong nửa; bản này chọn 123° để đồng thời giữ hình C và đúng ngưỡng >120° của phiếu; cần Claude so bằng mắt trước khi chấp nhận.

## Kiểm tra đã chạy

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node --import tsx src/lab/anim-r3-check.ts
```

Chạy probe R3 thay cho R2 cũ vì R2 không biết ngoại lệ tiếp xúc mới. Không chạy build hoặc bộ test game. Strict, `noUncheckedIndexedAccess`, chuỗi import của mã lab và kịch bản chụp: **0 chẩn đoán**. Nạp GLB thật, đúng rig **66 khớp**, wrapper/chiều cao 1,65 m như 403.

Mỗi Hz: 10 pose cuối; **90 cặp có thứ tự**, thêm **270 ca ngắt** ở 0,05/0,125/0,20 s; đo **405 cặp đoạn đốt ngón mỗi khung**. Độ sâu theo pháp tuyến mặt phẳng thân tại spine_03, đã loại hướng rest của xương; không tính khoảng cách tới camera. Vùng, hướng lòng và trạng thái ngón là cổng pose cuối; trong chuyển động, độ sâu/khe/gập cổ tay vẫn kiểm mọi khung. Không thể yêu cầu một ngón đồng thời gập và duỗi trong khung đang chuyển hai trạng thái.

| Chỉ số | 60 Hz | 120 Hz |
|---|---:|---:|
| Khung đo ấn/chuyển ấn | 6490 | 12880 |
| Khe nhỏ nhất sau ngoại lệ đúng cặp | 15.5449 mm | 15.5449 mm |
| Độ sâu nhỏ nhất khi chuyển | 0.0974 m | 0.0974 m |
| Độ sâu lớn nhất khi chuyển | 0.2934 m | 0.2934 m |
| Gập cổ tay lớn nhất khi chuyển | 68° | 68° |
| Thời gian chuyển, lấy mẫu tới đích | 283.3 ms | 283.3 ms |
| Bước quaternion khớp lớn nhất | 57.3625° | 30.1779° |

Bước khớp lớn nhất nằm ở cẳng tay trái khi ngắt S7→S0; số này được công khai để Claude xem video tốc độ thật, không coi nội suy toán học là bằng chứng cảm nhận đã mượt. Không đổi hoặc tự hạ chuẩn nghiệm thu bằng mắt.

Khe chưa loại ngoại lệ xuống dưới 4 mm chỉ ở các cặp tiếp xúc có tên trong bảng; không miễn toàn ấn hoặc toàn bàn tay. Hai đầu cái S0 cách **4,81 mm**; đầu cái tới ngón được giữ khoảng **14,08–20,04 mm** (cổng tiếp cận 25 mm); tay đỡ S6 cách cổ tay phải khoảng **4,76 mm**, S9 **13,43 mm**. Đây là tâm xương/đầu xương; chưa chứng minh mesh da chạm tự nhiên hoặc không xuyên. Không có ngoại lệ vùng, độ sâu hoặc gập cổ tay.

Tất cả 10 ấn đạt trạng thái từng ngón và đúng vùng cả hai cổ tay; khoảng độ sâu pose cuối và bảng góc chi tiết nằm trong JSON. Đã kiểm hình chiếu các đầu ngón trong cả khung nửa thân và cận tay, cùng việc khôi phục camera/FX; chưa có ảnh render.

| Họ / 10 lần phát mỗi Hz | Phím → thân / chuyển động, 60 Hz | 120 Hz |
|---|---:|---:|
| sword | 16.6567 ms | 8.3233 ms |
| palm | 16.6567 ms | 8.3233 ms |
| array | 16.6567 ms | 8.3233 ms |

Mỗi họ được gõ ở 15/45/90 WPM, từ 3/4/5/8 chữ tùy họ, cùng một lượt nhập dồn; mỗi chữ cuối hợp lệ đúng một phát, thân/FX/vẽ giả lập cùng khung, thân có thay đổi quaternion thật. Đã kiểm thêm **30 lần phát ngay khi rời ấn mỗi Hz** (10 ấn × 3 họ), mỗi lần đúng một callback và vẫn ≤50 ms. Cả ba họ giữ cổng ≤50 ms. Đây là lịch CPU fixed-step; chưa đo hàng đợi OS/browser, GPU/present hoặc onset âm thanh.

## Lệnh chụp cho Claude Opus

Sandbox của phiếu không cho mở browser; **không thử mở server hoặc tìm đường vượt chặn**, không tạo capture/review ngoài phạm vi ghi. Claude cần phục vụ đúng worktree này; cổng 3146 chỉ là ví dụ đã dùng ở 403:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/skills-lab.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node --import tsx src/kit/tools/cdp-run.mjs src/lab/anim-r3-review.ts \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản đợi đúng API 412/human rồi mới tạo thư mục. Chụp **10 nửa thân + 10 cận tay**, cắt đúng ô nguồn 411, đặt **tham chiếu trái / human phải**; xuất:

- `412-seals-front-10-compare-sheet.jpg`: lưới 5×2 cặp nửa thân.
- `412-seals-hands-10-compare-sheet.jpg`: lưới 5×2 cặp cận tay.
- 20 tệp `412-{front|hands}-S<n>-pair-compare.jpg` để xem đầy đủ độ phân giải, và `412-browser.json`.

Đích: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/hero-anim-r3-412/run-*`; hard link bảng/cặp/JSON sang `owner-review/2026-11-16/tu-tien/hero-anim-r3/run-*`. Có `ABOUT.md`; giữ ảnh đối chiếu, chạy prune xem trước rồi áp dụng để xóa đúng ảnh thô của lượt vừa tạo; cuối cùng chạy `node scripts/review-index.mjs`. Arial macOS. Đã kiểm kiểu kịch bản; **chưa thực thi browser/ImageMagick hoặc xác nhận crop bằng mắt**.

**Claude cần xem:** độ giống từng ngón, da ở ngón cái/nắm, bàn tay đỡ S6/S9, khoảng S7; độ cong mở S4/S8; cổ tay khi đổi hướng và cẳng tay khi ngắt giữa đường. Xem 20 cặp cạnh ảnh 411 và video chuyển tốc độ thật rồi chỉnh; chưa tuyên bố đạt 8,5 hoặc chuẩn chuyển động dùng chung 9.

## Phần không làm

Không tạo ảnh, model, âm thanh hoặc video mới; không dùng ảnh bên thứ ba hoặc image_gen vì phiếu này chỉ dựng rig theo nguồn đã có. Không chụp/chấm bằng mắt trong sandbox theo phân công. Không sửa `docs/work`, cây docs/src/scripts/tests của bản chính `games/immortality-cultivation` hoặc các đường ngoài phiếu. Không staging, commit, push, reset, clean, stash hoặc đổi nhánh. Không gặp hạn mức công cụ hay giờ bắt buộc chờ.
