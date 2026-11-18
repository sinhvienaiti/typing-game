# Phiếu 447b — Hư Không: lõi cầu 3D và hố đen lớn hơn

Ngày 18/11/2026. Hoàn tất đúng ba vòng sửa → chụp → mở ảnh. **Đạt các ngưỡng kỹ thuật của phiếu:** lõi tròn ở ba góc, vành ≥ 32% bề ngang tại pha mở/cao trào, lề ≥ 4%, vùng trắng ≤ 6%, p95 ≤ 16,7 ms, kiểm kiểu 0 lỗi. Bản này chỉ bật bằng `?blackhole=1`; chờ owner xem hình, không tự gán điểm thẩm mỹ 8,5.

## Tệp gửi owner

- [Ảnh đối chiếu bốn ô phân cảnh, Alt+1 và Alt+2](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab-b.jpg).
- [Video 7 giây có âm](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab-b.mp4): H.264, 1280×720, 24 fps, 168 khung; AAC stereo 48 kHz, 2,76 MB. ffprobe xác nhận 7,000 s; ffmpeg giải mã toàn bộ không lỗi.
- [Góc thẳng từ trên xuống 90° tại 3,2 s](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447b/round-3-overhead.jpg), [chuỗi chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447b/round-3-motion.jpg), [số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447b/round-3-measure.json). Đã mở xem cả ba tấm cuối.

Đã giữ nguyên `void-blackhole-lab.jpg` và `.mp4` của 447, thêm dòng 447b vào ABOUT của thư mục owner.

## Thay đổi trong phạm vi

Trong `games/.wt-ic-lab-all/src/lab/`:

- `void-blackhole-ult.ts`: nạp `void-blackhole-core.v1.glb` bằng GLTFLoader; dùng nguyên vật liệu đen, không đổi shader hoặc thuộc tính vật liệu. Cầu bán kính nguồn 1, 3.968 tam giác, thu phóng đều. Cầu opaque, depthWrite/depthTest đều bật, renderOrder 8; vành trong lượt transparent, renderOrder 12, depthTest bật. Phần vành khuất sau cầu bị chiều sâu che. Hai hàm mặt nạ phẳng của 447 vẫn giữ để tra, không gọi và không nạp atlas lõi phẳng.
- Vành cố định trong không gian, nghiêng **22°** so với mặt đất, không quay theo camera. Quad và các lưỡi xoáy phóng đều **1,5 lần**. Đường kính hình nguồn trung bình 0,806 đơn vị quad; lúc mở đủ, vành khoảng 18,74 m, cầu đường kính 8,52 m, tỷ lệ 2,2. Đường kính viền video dao động theo khung nên tỷ lệ thực khoảng 2,14–2,25. Giữ cầu phía trên mặt đất để không bị cắt mất chân cầu.
- Thêm ba lưỡi có sẵn, quay −60°, đặt nối dọc trục ngang, mỗi lưỡi thu phóng đều 13,5 m; phát 2,82–3,66 s. Mặt phẳng dải chém quay về camera và nằm trước bán cầu gần để đường quét cắt qua lõi ở các góc; không đổi hướng vành hoặc hình học cầu. Dải này vẫn kiểm tra độ sâu. Giữ đủ tám lưỡi xoáy 2,40–4,37 s.
- `skills-main.ts`: chỉ mở rộng hook `blackhole("overhead")` và kiểu tương ứng để chụp góc 90° sau khi tua tới 3,2 s. Không đổi dispatch mặc định/video của 447 hoặc tham số `ultVoid` cũ.
- `void-blackhole-review-b.mjs`: cảnh chụp/đo riêng 447b, giới hạn ba vòng; có cổng kiểm tỷ lệ lõi, kích thước vành, lề, ba lưỡi ngang, p95 và vùng trắng.
- `void-blackhole-support.mjs`: đọc atlas có sẵn để tạo bao lồi biên sáng; không sinh hoặc sửa ảnh.

Trong `games/.wt-ic-lab-all/art-src/lab/vfx/void-ult/`: thêm `void-blackhole-ring-b.json` trỏ đúng atlas vành cũ, kèm dữ liệu bao lồi cho đo; thêm ghi chú 447b vào `ABOUT.md`. Không ghi lại GLB, video, atlas hoặc manifest cũ. `art-src` của worktree là symlink có sẵn; mọi lệnh ghi dùng đường dẫn `/Volumes/…` được phép.

Giữ timeline 0–0,8 / 0,8–2,4 / 2,4–4,4 / 4,4–6,0 s; giữ hook kéo bán kính 8 m trong 3,6 s và quy trình thu nhỏ/nuốt quái. Cảnh cuối vẫn 51 mục tiêu khớp 51 thân quái, nuốt đủ 51; kết thúc 6,000 s, inactive. Hai mốc âm sẵn có vẫn 0,800 và 2,400 s; không tạo âm mới.

## Ba vòng và số đo

Chrome headless, Apple M4/ANGLE Metal, High, 1280×720, DPR 1; host có sẵn `http://localhost:3148/stress.html?ground=%23353a40&blackhole=1`. Cảnh 100 quái = 87 TargetField + 13 walker; camera đẩy vào tắt khi đo để giữ Alt+1/Alt+2. Mỗi vòng chụp 0,5 / 1,8 / 3,2 / 5,0 s ở hai góc, cùng một ảnh 90° tại 3,2 s.

| Vòng | Vành Alt+1 tại 1,8 / 3,2 s | Lõi cao/rộng tại 3,2 s: Alt+1 / Alt+2 / 90° | Trắng tối đa | p95 |
| --- | --- | --- | --- | --- |
| 1 | 37.52 / 43.20% | 1.0092 / 1.0165 / 1.0002 | 0.14724% | 5.80 ms |
| 2 | 32.98 / 38.57% | 1.0087 / 1.0137 / 1.0000 | 0.16233% | 5.30 ms |
| 3 | 32.89 / 38.45% | 1.0082 / 1.0117 / 1.0007 | 0.16482% | 5.30 ms |

Vòng 1 còn cắt mép trên và dải ngang nằm thấp; vòng 2 đưa dải qua lõi, còn thiếu khoảng 1 px lề trên. Vòng 3 hạ tâm 0,2 m và giảm nghiêng từ 25° về 22°; không mở vòng thứ tư. Số đường kính vòng 1 dùng phép ước lượng bốn điểm kế thừa 447; từ vòng 2 dùng bao lồi của pixel nguồn, tính cả hai khung flipbook đang hòa.

Vòng cuối:

- Vành Alt+1: **420,98 px (32,89%)** tại 1,8 s; **492,11 px (38,45%)** tại 3,2 s. Alt+2 tương ứng 49,75% và 56,75%.
- Lề nhỏ nhất của vành trong mọi mẫu 0,8–5,15 s ở camera chơi: **4,868%**; mép trên gần nhất 35,05 px. Hai ảnh Alt+2 cũng nằm trong khung.
- Lõi tại 3,2 s: **1,0082 / 1,0117 / 1,0007**, đo bằng chiếu toàn bộ đỉnh mô hình GLB qua camera thật; mọi ảnh pha cuối đều trong 0,9–1,1. Ảnh 90° có trục nhìn đúng thẳng xuống.
- Trắng tối đa **0,16482%** ở Alt+2; riêng toàn bộ 168 khung clip Alt+1 là **0,00304%**. Ngưỡng trắng: cả ba kênh sRGB ≥ 242/255.
- p95 **5,30 ms**, CPU p95 **1,40 ms**, p95 cao trào **5,20 ms**. Dùng `__lab.perf(1)` cộng CPU và chờ GPU qua readPixels 1 pixel, như `metal-ult-rain-review.mjs`; không dùng khoảng cách rAF. Tối đa 143 draw call, 1.475.147 tam giác cả cảnh.
- Ba lần dùng lại đều 158 texture / 305 geometry. Không runtime exception hoặc lỗi nạp lõi/vành/lưỡi của phiếu.

Kiểm hẹp `void-blackhole-check.mjs` PASS, giữ nguyên kiểm tra ở `void-ult-check.mjs:249`; TypeScript `tsc --noEmit` **0 lỗi**. Còn cảnh báo KTX2Loader và drawImage các atlas Metal có từ trước, ngoài phạm vi.

## Để owner xem và phần bỏ qua

Owner nên xem ô 2 ở Alt+2 để đánh giá cảm giác vành ôm cầu, ô 3 để chọn mức độ dải chém ngang; ảnh 90° xác nhận lõi không còn dẹt. Vành vẫn là flipbook trên mặt phẳng 3D theo phiếu; khối lõi là cầu GLB thật. Không sinh thêm hình/âm vì toàn bộ thành phần được phiếu cung cấp. Không chấm lại thẩm mỹ bằng hai giám khảo trong phiếu sửa kỹ thuật này.

Không chạy build hoặc bộ test game theo lệnh giới hạn phạm vi. Không cập nhật `INDEX.md` vì tệp đó ngoài danh sách được ghi; người điều phối cần chạy `node scripts/review-index.mjs` sau khi nhận bàn giao. Không sửa docs/game chính, src/scripts/tests của game chính hoặc công việc của agent khác.

Đã xem trước danh sách rồi prune đúng **207 PNG** của ba lượt, giải phóng **233.39 MB**; không còn khung thô. Giữ tấm ghép, ảnh 90°, số đo JSON và nhật ký prune. Không xoá khung hay tài nguyên của phiên khác.

Driver đã đóng Chrome của từng lượt và xoá profile tạm; không còn profile do ba lượt 447b tạo. Giữ server 3148 PID 243. Không commit, push, reset, clean hoặc stash.
