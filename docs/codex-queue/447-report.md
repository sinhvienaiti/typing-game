# Phiếu 447 — Hư Không: hố đen trong lab

Ngày 18/11/2026. Đã dựng bản lab chỉ bật bằng `?blackhole=1`, xuất ảnh và clip, hoàn tất ba vòng sửa/chụp/mở ảnh. **Đạt các số đo kỹ thuật; chưa đạt nghiệm thu toàn phần về “3D thật”: nguồn có phối cảnh đóng sẵn, đặt trên mặt phẳng cố định vẫn dẹt ở Alt+2.** Không bật mặc định, không đưa vào game chính hoặc tự chấm đạt 8,5.

## Tệp giao owner

- [void-blackhole-lab.jpg](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab.jpg): mỗi hàng là một ô storyboard, cạnh ảnh Alt+1 và Alt+2 tại 0,5 / 1,8 / 3,2 / 5,0 giây; đã mở xem.
- [void-blackhole-lab.mp4](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-18/tu-tien/void-blackhole-lab.mp4): đúng 7,000 giây, 168 khung, H.264 1280×720, 24 fps, AAC stereo. Âm `tt-sfx-ult-void/take1.wav` sẵn có; hai lần gọi trong bản trộn tại 0,800 và 2,400 giây. Đã kiểm giải mã và mở tấm chuỗi khung; chưa nghe/chấm âm độc lập.
- [Chuỗi chuyển động](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447/round-3-motion.jpg), [số đo cuối](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447/round-3-measure.json). ABOUT của thư mục owner đã thêm dòng 447.

Host có sẵn: `http://localhost:3148/stress.html?blackhole=1&ground=%23353a40`; chọn Void/key 8 trong lab. `/skills.html` không phải trang lab của host này; lần probe đầu dùng nhầm URL đó và đã sửa về `/stress.html`.

## Phần đã dựng

Tất cả mã mới ở `games/.wt-ic-lab-all/src/lab/`:

- `void-blackhole-cut.mjs`: ffmpeg đọc video, ImageMagick đóng atlas; không gọi AI.
- `void-blackhole-ult.ts`: timeline 6 giây, mặt phẳng world space khóa góc, 8 lưỡi lần lượt quét, hút và nuốt quái, hai mốc âm.
- `void-blackhole-review.mjs`: ba vòng đối chiếu, clip, vùng trắng và p95 theo phương pháp của `metal-ult-rain-review.mjs`.
- `void-blackhole-check.mjs`: kiểm hẹp atlas, mặt nạ, đoạn nối và vị trí nhánh; không gọi bộ test của game.
- `void-blackhole-probe.mjs`: kiểm chọn nhánh mặc định/video và hủy/reset.
- `skills-main.ts`: chỉ thêm import và các hook tạo/chuẩn bị, dispatch trước hai nhánh Void cũ, update, reset và API đọc trạng thái. Giữ nguyên `params.get("ultVoid") !== "video"` và `if (!voidUlt.layered) return castClip8(pick)`. Không sửa `void-ult-check.mjs`, kể cả dòng 249.

Atlas mới trong `games/.wt-ic-lab-all/art-src/lab/vfx/void-ult/`:

- `void-blackhole-ring.atlas.png`: 60 khung 384×384, atlas 3072×3072, 24 fps, lặp 2,5 giây. Đọc nguồn 0,5–3,5 giây, đầu chu kỳ tại 1,0 giây; hòa 12 khung cuối với đoạn ngay trước đầu chu kỳ.
- `void-blackhole-core.atlas.png`: cùng 60 khung; flood-fill vùng tối được viền sáng video bao kín, max-filter vuông 5 px đóng khe nén rồi mở lại 2 px. Không đĩa đen, hình tròn tự sinh hoặc shader hình tròn. RGB bằng 0; 4.801–5.123 pixel alpha 255 mỗi khung, trộn thường phía sau ánh sáng.
- `void-blackhole-crescent.atlas.png`: 53 khung nguồn 0–2,2 giây, atlas 3072×2688. Mỗi lưỡi chạy đoạn này trong 0,64 giây, giảm opacity trong 25% cuối; tám lần phát từ 2,40 đến 3,73 giây, kết thúc trước 4,4 giây.
- Mỗi atlas có JSON và `.atlas.prompt.txt` ghi phép xử lý, đường dẫn tham chiếu và prompt nguồn nguyên văn; thêm `ABOUT.md`. Không sửa manifest hoặc ảnh/video cũ.

`art-src` của worktree là symlink có sẵn sang game chính; chỉ ghi những atlas mới và ABOUT qua đường dẫn worktree được phép. Không sửa `src`, `scripts`, `tests` hoặc docs của game chính.

0–0,8 giây: lõi nguồn thu nhỏ ngang ngực quái, hạt từ atlas `aura/glint-gold-twinkle-set` chuyển về tâm. 0,8–2,4 giây: mở vành đến 11 m, nghiêng 25° so với mặt đất, nâng thấp trên cụm đông nhất; gọi `herd.pull(..., 8, 3.6)`. 2,4–4,4 giây: tám lưỡi khác góc; thu nhỏ đều thân quái rồi dùng dissolve đã có của herd. Cảnh đo có 51 quái trong vùng, khớp 51 instance và nuốt đủ 51. 4,4–6,0 giây: co về điểm ở 5,15 giây, một glint 5,05–5,40 giây, hạt vàng còn đến 6 giây. Bóng/ánh dưới đất dùng ảnh `inward-spray.png` có sẵn, không thêm vòng tròn dưới đất. Không tạo shader hiệu ứng, đèn hoặc hình vẽ mới bằng code.

## Số đo và ba vòng xem

Cảnh 100 quái = 87 TargetField + 13 walker stress; hook gameplay chỉ tác động TargetField. Chrome headless, Apple M4/ANGLE Metal, 1280×720, High, DPR 1, pipeline lab hiện hữu; nền `#353a40`. p95 là thời gian CPU cộng chờ GPU bằng readPixels 1 pixel, lấy cửa sổ 0,8–6 giây; không dùng khoảng cách rAF.

| Vòng | Vành Alt+1 tại 1,8 / 3,2 s | Vành Alt+2 tại 1,8 / 3,2 s | Nghiêng | Tổng lưỡi | Trắng tối đa | p95 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 254,9 / 295,2 px | 385,0 / 444,3 px | 25° | 8 | 0% | 4,80 ms |
| 2 | 256,7 / 295,2 px | 387,7 / 444,3 px | 25° | 8 | 0% | 5,50 ms |
| 3 | 257,8 / 295,2 px | 389,4 / 444,3 px | 25° | 8 | 0% | 5,50 ms |

Vòng 1 thấy chấm tụ lực khó đọc và dư âm còn lớn. Vòng 2 tăng chấm/hạt, co nhanh hơn và sửa sai số thời gian. Vòng 3 tăng nhẹ độ đọc pha đầu, xuất tệp cuối; không mở vòng 4. Tại 3,2 giây có 5 lưỡi đã phát, 4 lưỡi còn sống; đủ 8 lưỡi ở cuối cao trào. Sau co, đường kính chiếu tại 5,0 giây là 29,9 px / 46,0 px.

Vòng cuối: CPU p95 1,50 ms; p95 cao trào 5,50 ms; tối đa 132 draw call, 1.471.159 tam giác. Bộ nhớ ba lần dùng lại: 159 texture / 306 geometry, ổn định. 6,000 giây: inactive, không còn card sống. Vùng trắng là cả ba kênh sRGB ≥242/255; 0% trên tám ảnh pha và toàn bộ 168 khung clip.

Kiểm atlas PASS: lõi đen đặc, ngoài biên alpha 0; sai khác RGB trung bình tại mối nối là 2,159/255, so với phân vị 95 các cặp khung liền là 1,907/255. Đây là số đo nối chu kỳ, không phải chấm thẩm mỹ. `tsc --noEmit`: 0 lỗi. Không chạy build hoặc bộ test game. Không có runtime exception ở ba vòng chụp; còn cảnh báo KTX2Loader và drawImage của atlas Metal đã có, ngoài phạm vi phiếu.

Probe chọn nhánh runtime PASS, không có exception: mặc định = Void layered cũ active; `ultVoid=video` = clip cũ active 1; `blackhole=1` với mỗi giá trị của `ultVoid` = hố đen active, layered/video cũ đều inactive. Chuyển sang tuyệt kỹ khác và reset đều dọn hố đen. Chỉ kiểm dispatch của các nhánh cũ, không chấm lại art của chúng. Bằng chứng: [route-probe.json](/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/void-blackhole-447/route-probe.json).

## Phần chưa đạt và dọn dẹp

- Owner cần nhìn đặc biệt góc Alt+2: lõi/vành là mặt phẳng hai mặt có depth test, không quay theo camera, nhưng **chưa phải khối hố đen 3D thật**. Góc nghiêng đóng sẵn trong nguồn bị chiếu thêm một lần, làm lõi bẹt; lưỡi cũng cùng dạng mặt phẳng. Các phép đặt/xoay/scale đều/opacity/flipbook không bổ sung được bề mặt hoặc góc khuất thiếu trong video. Không tự dựng cầu/đĩa, kéo méo nguồn hoặc sinh model ngoài phạm vi để che vấn đề này.
- Pha đầu và hạt dư âm vẫn nhỏ so với storyboard; ánh vàng dưới đất yếu. Tấm so sánh giữ nguyên cảnh/nhân vật hiện có của host; không sửa map, caster hoặc art khác để giống storyboard.
- Không sinh hình/âm mới; nguồn đã có và đã được owner duyệt. Chưa có hai chấm mù hoặc owner chốt thẩm mỹ; không ghi PASS 8,5.
- Đã xem trước rồi prune đúng 204 PNG của phiên, khoảng 230,68 MB; giữ tấm ghép, JSON và nhật ký prune. Không xoá nguồn hoặc khung của người khác. Tệp âm/video trung gian đã xoá.
- Driver đóng Chrome do phiên tạo và xoá profile tạm. Server 3148 PID 243 giữ nguyên. Không commit, push, reset, clean hoặc stash.
- Không chạy `review-index.mjs` vì sẽ ghi INDEX ngoài danh sách đường dẫn được phiếu cho phép; người điều phối cần cập nhật chỉ mục review.

Chạy lại trên host có sẵn (chỉ đo/chụp theo phiên, không build):

```sh
ROUND=3 FINAL=1 .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/void-blackhole-review.mjs --width=1280 --height=720 --dpr=1
node games/.wt-ic-lab-all/src/lab/void-blackhole-check.mjs
node games/.wt-ic-lab-all/node_modules/typescript/bin/tsc --noEmit -p games/.wt-ic-lab-all/tsconfig.json
```
