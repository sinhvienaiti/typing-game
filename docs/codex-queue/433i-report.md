# Phiếu 433i — Kiếm nhỏ năng lượng A, vệt D

Ngày 18/11/2026. **Đạt các cổng số sau hai lượt chụp và tự mở ảnh:** 0 mô hình kiếm nhỏ được vẽ, tỷ số sáng tối thiểu 2,008×, vùng trắng 0,00010851%, p95 cuối 6,10 ms, kiểm kiểu 0 lỗi. Chưa có chấm mù 8,5 hoặc owner duyệt thẩm mỹ.

## Thay đổi

- Dùng đúng ảnh owner chọn: `games/immortality-cultivation/art-src/lab/vfx/metal-ult/stills/energy-sword.v1-try1.png`. Cắt lề ngang x=400, rộng=224, giữ chiều cao 1024; không làm mờ, vẽ thêm hoặc kéo méo. Tạo `energy-sword-a.png`, `.json`, `.prompt.txt` trong `games/.wt-ic-lab-all/art-src/lab/vfx/metal-ult/`.
- JSON ghi mũi (111;850), đầu chuôi (111;200) trên ảnh cắt, tương ứng (511;850) và (511;200) trên ảnh gốc. Khoảng neo 650 px được chuẩn hóa thành local y=0…1. Alpha thẳng lấy từ max RGB sRGB, bù RGB trong ánh sáng tuyến tính; cộng lại trên nền đen khớp nguồn, sai số kênh lớn nhất và trung bình đều 0/255 trong khung cắt.
- Mỗi trong 102 kiếm nhỏ chỉ dựng **một quad A**, dùng `MeshBasicMaterial`, `AdditiveBlending`, `SRGBColorSpace`, shader chuẩn. Nhân màu đều 0,62 và opacity bay 0,85. Chiều dài neo bằng chiều dài kiếm cũ, thu phóng đều cả ba trục; quay quanh trục dài để hướng mặt về camera. Model Tripo ẩn còn làm carrier ma trận chung, không được render.
- Khi cắm, giữ góc nghiêng của 433h, đưa mũi xuống 15% chiều dài dọc trục kiếm, chuyển êm qua tiếp đất. Opacity giảm nhẹ 30% trong 0,08 s, rồi tan theo khoảng fade/end cũ bằng độ mờ. Không dùng emissive hoặc `qi-streak` trên kiếm nhỏ.
- Giữ mô hình Tripo nguyên bản cho **duy nhất kiếm lớn**, hào quang flipbook feather-mantle và vệt D. Code dựng kiếm nhỏ/emissive/qi-streak của 433g còn nguyên trong lớp cũ, lời gọi bị ngừng bằng `if (false)`; không tải qi-streak nữa.
- D giữ texture, màu, cách thu phóng đều, bù phối cảnh và thời gian tan 0,20 s của 433h. Neo ở đúng đầu chuôi A (local y=1), hướng ngược chiều rơi; đo ngang trong probe đã đổi từ biên Tripo sang biên A thực. Trận A, nhịp mưa và âm Kim giữ nguyên.

## Kiểm tra

Chrome headless chỉ vào server có sẵn localhost:3148, High mặc định, 1280×720, DPR 1, Apple M4/ANGLE Metal, 100 quái. Hai góc Alt+1 và Alt+2, `?ground=%23353a40`. Hai lượt cùng cách gắn A; lượt 2 xuất media cuối, không sửa hình sau lượt 1.

| Chỉ số | Lượt 1 | Lượt 2 cuối | Cổng |
| --- | ---: | ---: | ---: |
| Mô hình kiếm nhỏ được vẽ | 0 | 0 | 0 |
| Lớp qi-streak được vẽ | 0 | 0 | 0 |
| Sáng kiếm lớn / nhỏ, tối thiểu | 2,008× | 2,008× | ≥1,5× |
| Trắng toàn khung, tối đa | 0,00010851% | 0,00010851% | ≤6% |
| p95 mưa dày | 9,00 ms | 6,10 ms | ≤16,7 ms |
| CPU p95 | 3,10 ms | 1,90 ms | — |
| p95 toàn chiêu | 8,70 ms | 5,70 ms | — |

- 760 mẫu quad ở hai góc: tỷ số chiều cao màn hình A / trục kiếm cũ = 1,000000; scale x/y/z lệch 0; hướng mặt dot ≥0,9999999999999998; sai số neo A tối đa 9,94e−16 m. Tất cả dùng shader chuẩn.
- 146 mẫu đã cắm đủ 0,10 s: mũi ngập 14,9999990–15,0000011% chiều dài. Kiếm bay lẫn kiếm cắm đều dùng cùng quad A.
- 353 mẫu D trên kiếm nhỏ: dài 0,800–1,400 lần thân kiếm, trung vị 0,939; ngang/biên A trung vị 0,457. Sai số neo D tối đa 8,45e−7 m; scale lệch 0. D cũ crop-blur có 0 instance được vẽ; opacity D của kiếm lớn về 0 ở 5,10 s tại cả hai góc.
- Đo sáng tách nhóm thân A và nhóm thân Tripo + hào quang, HDR tuyến tính trước bloom, cùng định nghĩa 433g/433h; không cộng nhóm vệt D và cảnh nền. Có 3 mẫu hợp lệ tại Alt+1, 4 tại Alt+2; không nhận Infinity hoặc mẫu thiếu một nhóm. Giá trị tối thiểu tại Alt+1, 4,40 s: nhỏ 0,927755; lớn 1,862968.
- Vùng trắng đo trên PNG sau chuỗi render: cả ba kênh sRGB ≥242/255. Tối đa 1 pixel/921.600 pixel, bao gồm 165 khung clip. p95 đo riêng ở camera chơi, 42 mẫu có kiếm rơi và số kiếm sống ≥80% đỉnh; CPU rồi readPixels một pixel chờ GPU theo driver 433h, không dùng khoảng cách rAF. Không suy ra mức tăng tốc từ chênh lệch giữa hai lượt.
- Giữ 102 kiếm nhỏ + 1 lớn, sáu đợt 12/14/16/18/20/22; tối đa 60 kiếm sống; mưa 4,088344 s, chiêu 6,80 s, trả đủ 103 ô. Trung vị thấy rõ 0,767 s, quãng rơi 40,63% khung; 99,03% kiếm đạt hai cổng 433f.
- `node node_modules/typescript/bin/tsc --noEmit`: **0 lỗi** trong worktree lab. Không chạy build hoặc bộ test của game. Không có runtime exception. Còn cảnh báo sẵn có KTX2Loader và drawImage của metal-crescent-sym/metal-slash-arc ngoài phạm vi; tài nguyên mưa A/D/hào quang sẵn sàng.

## Tệp giao nộp

- [metal-rain-i.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-i.jpg): 10 ô, Alt+1 và Alt+2, 1,05 / 2,35 / 3,90 / 4,916667 / 5,90 s.
- [metal-rain-i.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/metal-rain-i.mp4): H.264 + AAC, 1280×720, 24 fps, 165 khung, 6,875 s, 5.457.344 byte; âm Kim cũ, 54 sự kiện. ffmpeg giải mã hết không báo lỗi.
- [Chi tiết hai góc](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433i/round-2-trail-detail.jpg), [tấm chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433i/motion-contact.jpg), [so sánh h/i](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433i/h-i-compare.jpg), [nguồn A trên nền xám](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433i/source-preview.jpg), [số đo đầy đủ](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/metal-rain-433i/round-2-metrics.json).
- Sửa `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`, `metal-ult-trail-d.ts`; thêm `metal-ult-energy-a.ts`, `metal-ult-energy-a-normalize.mjs`, `metal-ult-rain-i-review.mjs`. Không sửa `metal-sword-look.ts`. Ba tệp art A ghi qua đường dẫn worktree được phép; `art-src` là symlink sẵn có sang game chính.
- Đã thêm dòng vào ABOUT owner và tạo ABOUT cho chủ đề/lượt chụp. Đã tự mở tấm cuối, tấm chi tiết/chuyển động, nguồn A; đối chiếu ảnh A và 433h.

## Dọn dẹp và phần owner cần xem

- Đã xem trước rồi prune **197 khung thô**, khoảng 260,597 MB, chỉ của phiên này. Giữ tấm ghép, số đo và nhật ký prune. Không còn PNG thô; video/âm trung gian đã xóa.
- Driver đã đóng Chrome của hai lượt và xóa profile tạm; không còn tiến trình Chrome st-cdp của phiên. Giữ server 3148 PID 243. Không xóa profile cũ của phiên khác.
- Không sinh ảnh/âm AI mới vì phiếu yêu cầu giữ nguyên A/D đã chọn; không đổi các lớp khác. Không commit, push, reset, clean hoặc stash. Không chạy review-index vì INDEX.md nằm ngoài phạm vi ghi của phiếu; người điều phối cập nhật sau.
- Owner cần xem độ đọc kiếm A ở camera chơi và góc sau lưng trong ảnh/video. Hình nền, trận và phần đế Tripo của kiếm lớn đã có từ 433h, vẫn hiện trong bản này; không nhận chúng là phần đã sửa hoặc đã đạt 8,5.

Chạy lại driver sẽ ghi lại ảnh/video i khi có `FINAL=1`:

```sh
ROUND=2 FINAL=1 ART_MAGICK=/opt/homebrew/bin/magick .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/metal-ult-rain-i-review.mjs --width=1280 --height=720 --dpr=1
```
