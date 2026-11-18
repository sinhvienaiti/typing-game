# Phiếu 088 · Tuyến Cuối · Ảnh 2D cho sân "Vành Chân Trời" (map 1)

**Vì sao:** kiểm kê map 1 ngày 28/10 (TS-M1-07, P1, cổng G2) thấy sân trận chưa từng được thiết kế. Hành lang thép 24 × 40 m trống trơn; hai bên chỉ có nền xoáy và hố đen vẽ bằng shader; 150 s không đổi cảnh. Cảnh trận vì thế chỉ được khoảng 7/10, chưa tới mức production (8). Phiếu này vẽ ảnh để Claude dựng thành lớp nền, lớp hai bên và decal sàn (TS-M1-08).

**Báo cáo:** `docs/codex-queue/088-report.md`.

## Luật chung

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh ghi vào `games/typing-survival/art-src` (media, không vào Git).
- **Luật điểm:** ảnh 2D đạt từ 8 điểm (`docs/games/ART_ACCEPTANCE.md` §2.2). Chưa đạt thì sửa prompt đúng chỗ thiếu, tối đa 3 lượt mỗi ảnh.
- **Chỉ được ghi:**
  - `games/typing-survival/art-src/arena/<tên>.tryN.png` và `<tên>.tryN.prompt.txt` (N = 1, 2, 3);
  - bản chọn chép thành `<tên>.png` và `<tên>.prompt.txt`;
  - `games/typing-survival/art-src/_review/088-*.jpg` và `games/typing-survival/art-src/_review/088/`;
  - file báo cáo.
- **Cấm:**
  - ghi đè, đổi tên, xóa file có sẵn; xóa file `.try*`;
  - mọi lệnh git;
  - sửa mã hay tài liệu;
  - dev server, trình duyệt, mạng ngoài công cụ tạo ảnh của Codex;
  - đụng game khác; đọc hay ghi Tu Tiên (`games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`);
  - chữ, số, logo, người, sinh vật, tàu bay trong ảnh.

## Phong cách

- Cùng bộ với màn tựa: xem `games/typing-survival/art-src/ui/title-horizon.png` và đọc prompt của nó, `title-horizon.prompt.txt`. Giữ nguyên các cụm: "industrial science-fiction", "old battered steel station", "matte painted cinematic science-fiction game art, strong large shapes and restrained detail", "Charcoal steel, hot orange, electric blue; clear tonal hierarchy".
- Cảnh trận hôm nay: cắt ô thứ hai của hàng đầu trong `games/typing-survival/tmp/map1-audit/sheets/sheet-c1s1-fight-1280x720.jpg`. Tờ ghép là lưới 4 × 4, mỗi ô rộng 1/4, cao 1/4. Lưu bản cắt thành `_review/088/ref-fight.png` và dùng nó làm ảnh tham chiếu.
- Camera của trận nhìn dọc hành lang, chúi xuống khoảng 36° dưới đường chân trời. Hố đen ở giữa phía trên khung hình. Hành lang chìa ra trên khoảng trống; bên dưới có một tấm thép dày.
- **Độ tối:** cảnh nằm sau dòng chữ người chơi gõ, nên ảnh hai bên và ảnh nền xa phải tối và ít chi tiết sáng. Đèn chỉ là điểm hoặc dải mảnh, thưa. Số đo ở mục Kiểm.

## Năm ảnh

| Tên file | Khổ | Nền | Nội dung |
|---|---|---|---|
| `concept-fight` | 1536×1024 | đặc | Ảnh vẽ đè lên `ref-fight.png`, cùng góc nhìn và cùng hành lang (giữ nguyên hình hành lang, dải sọc cảnh báo, cổng vòm ở cuối, hố đen). Thêm hai bên hành lang và dưới nó phần thân trạm cũ: giàn thép, khoang phóng chìm, ống dẫn, cột đèn, các khối máy lùi xa về phía hố đen. Ở xa, quanh và dưới hố đen, là bóng các mô-đun trạm ngược sáng trước vành bồi tụ. Không vẽ quái, tàu, chữ hay HUD. Đây là ảnh đích để Claude dựng theo, không dùng trực tiếp trong game |
| `hull-left` | 1024×2048 | alpha | **Nhìn thẳng từ trên xuống, chiếu trực giao, không phối cảnh, không đường chân trời.** Thân trạm nằm bên trái hành lang: phủ 20 m ngang × 40 m dọc. Mép phải là mép giáp hành lang, thẳng và đặc. Mép trái vỡ ra thành các thanh giàn thép thò vào khoảng trống, rồi trong suốt dần. Có tấm thép tán đinh, nắp khoang, ống, dải LED xanh điện mảnh, vài lò đỏ cam âm sâu. Mép trên là phía hố đen, mép dưới là phía tàu |
| `hull-right` | 1024×2048 | alpha | Như `hull-left` nhưng nằm bên phải: mép trái giáp hành lang. **Bố cục khác, không lật gương** `hull-left` |
| `far-structures` | 2048×1024 | alpha | Nhìn thẳng ngang từ xa. Bóng các mô-đun trạm, cột ăng-ten và nửa vòng một vành trạm gãy, tối gần như đen, ngược sáng với ánh cam của hố đen; viền cam mảnh ở cạnh trên. Các khối nằm ở 45 % dưới của ảnh và hai mép trái, phải. **Ô giữa phía trên rộng 40 % và cao 60 % trong suốt hoàn toàn**: hố đen hiện ở đó |
| `deck-decals` | 2048×2048 | alpha | Lưới 2 × 2, mỗi ô 1024×1024, cách nhau ít nhất 32 px trong suốt. Nhìn thẳng từ trên xuống. Bốn decal sàn thép: (1) vết cháy xém có vết nứt đỏ âm ỉ ở tâm; (2) vệt dầu hoặc nước làm mát loang; (3) mũi tên chevron sơn cảnh báo cam, mòn và tróc, chỉ về mép dưới (không chữ, không số); (4) mảng vá thép tán đinh và vết cào xước. Mép decal mờ dần, không viền cứng |

## Việc

1. Cắt `ref-fight.png`. Chạy KA1 "trước" (xem Kiểm).
2. Viết prompt cho từng ảnh từ khuôn của `title-horizon.prompt.txt` và mô tả ở bảng. Ghi `.tryN.prompt.txt` cạnh mỗi lượt.
3. Tạo `concept-fight` trước, rồi dùng nó làm tham chiếu cho bốn ảnh còn lại, để cả bộ cùng chất liệu và cùng màu.
4. Tự chấm từng lượt theo 5 tiêu chí của `ART_ACCEPTANCE.md` §2.2: ở cỡ đầy đủ, và ở cỡ nó sẽ hiện trong khung 1280×720 (thu `hull-*` còn 256 px cao, `far-structures` còn 640 px rộng). Đạt từ 8 thì dừng; chưa đạt thì sửa prompt, tối đa 3 lượt.
5. Chép bản chọn thành `<tên>.png` và `<tên>.prompt.txt`.

## Kiểm (bắt buộc, ghi số đo vào báo cáo)

1. **KA1 md5:** `md5 -r` mọi file trong `art-src/` (đệ quy) trước, lưu `_review/088/md5-before.txt`, và sau. `diff` chỉ được có dòng của file mới.
2. **Khổ:** `magick identify` đúng khổ ở bảng, cho cả năm bản chọn.
3. **Alpha** (bốn ảnh có alpha):
   - alpha min 0 và max 255;
   - không có viền nền: trên vùng alpha 1–254, màu trung bình không lệch về trắng hay xám nhạt (luma trung bình ≤ 0,35);
   - `far-structures`: ô giữa trên (x 30–70 %, y 0–60 %) có alpha ≤ 8 ở ≥ 99 % số px;
   - `deck-decals`: dải 32 px giữa các ô có alpha 0 ở 100 % số px.
4. **Độ tối** (luma Rec. 709 trên 0–1, tính trên px có alpha > 128; với `concept-fight`, tính cả ảnh):
   - `hull-left`, `hull-right`, `far-structures`: luma trung bình ≤ 0,14, và px có luma > 0,8 chiếm ≤ 2 %;
   - `concept-fight`: hình chữ nhật x 25–75 %, y 50–70 % (chỗ dòng chữ) có luma trung bình ≤ 0,20.
5. **Không chữ, không số:** xem bằng mắt cả năm ảnh ở cỡ đầy đủ; ghi "không thấy" hay chỉ chỗ.
6. **Tờ xem nhanh** `_review/088-sheet.jpg`:
   - hàng 1: `ref-fight.png` cạnh `concept-fight.png`, cùng cỡ;
   - hàng 2: `hull-left`, `hull-right`, `far-structures`, `deck-decals` trên nền `#05060A` (gần màu khoảng trống trong game) và trên nền ô vuông xám, để thấy alpha;
   - có nhãn.

## Báo cáo `docs/codex-queue/088-report.md`

- Bảng `| Ảnh | Lượt | Prompt thêm hay sửa | Điểm 5 tiêu chí | Tổng | Còn thiếu |`.
- Bản chọn của từng ảnh và lý do.
- Đầu ra của sáu mục Kiểm, có số.

**Xong khi:** cả năm ảnh có lượt tự chấm từ 8 và qua mục Kiểm 1–5. Nếu đủ 3 lượt mà vẫn chưa tới 8, ghi bản tốt nhất kèm lý do. **Nhận** khi Claude chấm lại từ 8.
