# Phiếu 252 · Tu Tiên · Thí điểm: khung đầu và khung cuối cho đòn lửa phím 1 (Brushfire), để Firefly Video tạo chuyển động

**Vì sao có phiếu này:**
- Đêm 04/11 hai giám khảo mù chấm 35 ứng viên lửa và hào quang. Cao nhất là 7, đều là bản Firefly Video.
- Kế hoạch đã lập cùng ChatGPT và Gemini (`docs/games/VFX_PRODUCTION_PIPELINE.md` §10, mục 10, bản C) là: vẽ trước **hình ba nét đã thiết kế**, rồi Claude đưa hình đó vào Firefly Video làm **khung đầu** (và khung cuối) để Firefly cho chuyển động lửa.
- Bản `ff-a1-c5` làm theo cách này được 6,5 ở cả hai giám khảo. Nó trượt vì bốn chỗ, phiếu này sửa ngay ở hình vẽ:
  - cung gần khép (khoảng 300° trong clip), đọc như chữ "C";
  - nét dày đều (đo được tỉ lệ dày 0,81, gần như không thuôn);
  - không có đường nóng trắng vàng;
  - mép cắt cứng như hình dán.

**Đây là lượt thí điểm, tối đa 10 lần gọi `image_gen`.** Claude xem chất lửa của ảnh vẽ trước khi giao các món khác. Rủi ro đã biết: `ff-a1-c5` đẹp vì khung đầu là lửa thật của Firefly được uốn lại; một hình vẽ có thể mang nét "tranh vẽ" mà Firefly giữ nguyên.

Codex chỉ vẽ ảnh và đo. Không mở trình duyệt, không dùng Firefly: Claude làm bước Firefly sau khi chọn.

**Báo cáo:** `docs/codex-queue/252-report.md` (tiếng Việt). Model `gpt-6.1-sol`, mức `high`.

## Đường dẫn

### Được ghi
- `games/immortality-cultivation/art-src/lab/vfx/first-frames/fire-impact-k1/`: lượt sinh, prompt, bản chọn trong `selected/`.
- `games/immortality-cultivation/tmp/shots/codex-first-frames/`: tấm xem, mặt nạ, ảnh gỡ lỗi, ảnh tham chiếu đã cắt.
- `docs/codex-queue/252-report.md` và `docs/codex-queue/252/`. **Thư mục `252/` chỉ chứa file chữ** (`.py`, `.json`, `.md`, `.txt`): repo cha không bỏ qua ảnh ở đó, nên ảnh để ở đó sẽ lọt vào Git.

Không ghi chỗ nào khác.

**Không ghi đè file có sẵn trước lần chạy đầu của phiếu.** Nếu phiếu chạy lại sau khi chờ hạn mức, Codex được ghi lại tấm xem và JSON của chính nó. Số lượt sinh tính cả lượt của lần chạy trước.

### Cấm
- Mọi lệnh git, trừ `status`, `diff`, `log`, `show`, `ls-files`, `check-ignore`.
- Sửa `src/`, `scripts/`, `tests/`, `docs/` của game, `manifest.json` hay `public/`.
- Chạy dev server, build hoặc test của game. Tải ảnh trên mạng.
- **Đưa vào `image_gen` ảnh của game thương mại** (ảnh chụp, bảng tham chiếu, mọi thư mục `tmp/shots/*/board/`).

## Tham chiếu

**Được đọc hoặc xem để hiểu** (ảnh và bài của chính repo):
- hai bài chấm `games/immortality-cultivation/tmp/shots/overnight/judge-1.md` và `judge-2.md`;
- `games/immortality-cultivation/tmp/shots/overnight/firefly/fire-crescent-sweep.sheet.jpg` (bản `ff-a1-c5`): chất lửa mềm cần giữ, hình cần sửa;
- `docs/games/tu-tien/skills/FIRE_STYLE.md`, khối "Quyết định của anh".

**Chỉ được đính kèm vào `image_gen`:**
1. Một ô 1024×256 cắt từ `games/dragon-hold/public/assets/dragon-hold/vfx/firefly/flame-trail.webp`: vệt lửa Dragonhold chủ dự án khen, để làm mẫu chất lửa.
   - Atlas này có 2 cột × 8 hàng; cắt một ô của dải lửa, không lấy đường lưới.
   - Lưu ở `games/immortality-cultivation/tmp/shots/codex-first-frames/ref-flame-trail-strip.png`.
2. Với khung cuối: ảnh gốc của lượt khung đầu đã chọn.

Không đính kèm tấm xem, bảng hay `ff-a1-c5-first.png`, vì đó là hình chữ C cần tránh.

## Gu của chủ dự án (bắt buộc)
- Anime, donghua và thần thoại: rực rỡ, cuốn hút, sang, có chi tiết. Không lấy tả thực làm đích, không đơn điệu.
- Lửa giữ tông đỏ cam: rượu `#5E1220` → đỏ thẫm `#A8221A` → son `#DC461C` → cam `#FF7E2A` → hổ phách `#FFB43A` → trắng vàng `#FFF4D6` ở đường nóng.
- Không máu, không mực, không vết bẩn.
- Có lấp lánh, nhưng là vài điểm lóe nhỏ có tia ngắn. Không sao clip-art, không lóa ống kính, không bokeh.

## Việc: `fire-impact-k1`

Đây là thân lửa của nhát chém phím 1, hệ Fire, kiểu Brushfire Calligraphy mà chủ dự án đã chọn: ba nét bút lửa cong lớn. Khung đầu là lúc nhát chém **đã bung đủ hình**: shader trong game lo pha bùng, Firefly lo cho lửa cuộn và tách.

### A. Khung đầu: 3 biến thể, tối đa 2 lượt mỗi biến thể

Mọi biến thể đều có:
- **3 nét không đều nhau:** một nét dài chủ đạo, một nét vừa, một nét ngắn, cách nhau không đều, có khe tối giữa các nét;
- mỗi nét **dày ở gốc, thuôn thành mũi kim**;
- **cung mở, không khép thành vòng**;
- **một đường nóng trắng vàng mảnh chạy dọc mép trước, mép ngoài** của mỗi nét; lưỡi lửa bong ra ở phía trong, phía sau.

| Biến thể | Bố cục | Ý (EN) cho prompt |
|---|---|---|
| `v1` | Ba vầng trăng lồng nhau, đi lên sang phải từ điểm chém ở dưới trái | three nested crescent brushstrokes of fire sweeping up and to the right from a strike point at the lower left, like a sword cut drawn in three calligraphy strokes, the fan open like half a circle and never closing |
| `v2` | Ba nét bung từ một gốc như ba nét phẩy bút | three flame brushstrokes flicked out from one shared root like a calligrapher's three fast strokes, fanning apart, each curving and tapering to a fine needle |
| `v3` | Hai nét dài cùng chiều và một nét ngắn ngược chiều | two long sweeping crescent strokes of fire and one short counter-stroke curling the opposite way at their root, like a sword cut followed by a flick of the wrist |

Câu chung thêm vào cuối mọi prompt, giữ nguyên chữ:

> The strokes are clearly unequal: one dominant long stroke, one medium, one short, unevenly spaced with dark gaps between them. Each stroke is thick and heavy at its base and tapers to a fine needle tip. Soft, flowing, living fire with natural flame texture (not photographic), in the style of premium anime xianxia game effects: radiant, elegant, luxurious. Colour from deep wine-red at the trailing edges through crimson, vermilion and orange to amber, with a thin white-gold hot line along the leading outer edge of each stroke; flame tongues peel off the inner trailing side. Two or three pin-point glints with very short thin cross rays at the hottest points, and three or four small ember sparks flying outward along the swing; no star icons, no lens flare, no bokeh. Keep the entire effect inside the middle 55 % of the image width and the middle 70 % of the image height; everything outside stays pure black. Pure black background, no ground, no sword, no character, no text, no frame.

### B. Khung cuối: cho 2 biến thể tốt nhất, tối đa 2 lượt mỗi khung

Khung cuối cho Firefly biết lửa "tắt chậm" ra sao (luật của chủ dự án: bùng nhanh, tắt chậm).

- **Vẽ bằng chế độ sửa ảnh của `image_gen`.** Đính kèm đúng ảnh gốc của lượt khung đầu đã chọn làm ảnh cần sửa, không đính kèm ảnh nào khác. Prompt mở đầu bằng: `Edit the attached image. Keep every stroke exactly where it is; do not move, add or extend anything.` Sau đó tả: `the same three strokes after they have burned down: thin glowing ember lines tracing exactly the same paths, scattered dying embers along the swing, a few faint dark-wine smoke wisps`.
- Cắt khung cuối bằng **đúng hộp cắt của khung đầu** (ghi trong JSON). Nếu ảnh trả về khác khổ, thu về khổ gốc trước khi cắt.
- Tên: `fire-impact-k1-v<k>-end`.

## Định dạng

1. **Sinh ảnh.** Xin 1536×1024 và ghi khổ thật nhận được (công cụ từng trả 1586×992, 1774×887, 1254×1254). Ảnh hẹp hơn 1400 px thì loại.
2. **`<tên>.master.png`:** cắt hình chữ nhật 16:9 lớn nhất ở giữa, thu (Lanczos) về 1536×864. Ảnh RGB đục trên nền đen.
3. **`<tên>.square.png`:** hình vuông lớn nhất ở giữa, thu về 1080×1080. **Đây là khung đầu chính cho Firefly**, cùng chế độ đã chạy được với `ff-a1-c5`: nền đen, 1080p, 1:1. Hình phải nằm gọn trong hình vuông giữa.
   - Ghi hai hộp cắt vào `docs/codex-queue/252/<tên>.crop.json`.
4. **`<tên>.alpha.png`** (1080×1080, RGBA thẳng, không premultiplied), dùng làm mặt nạ trong game:
   - m = max(R, G, B) / 255;
   - alpha = smoothstep(0,03; hi; m), hi trong khoảng 0,20–0,40 (ghi số dùng);
   - màu = RGB / (255 · max(alpha, m));
   - chỗ alpha < 2/255 lấy màu của điểm có alpha ≥ 0,5 gần nhất.
5. **Tên lượt sinh:** `fire-impact-k1-v<k>.try<n>.png`, prompt nguyên văn cạnh nó: `.try<n>.prompt.txt`. Bản chọn chép vào `selected/` cùng ba file `.master.png`, `.square.png`, `.alpha.png`.

## Công cụ đo
- `python3` của máy không có numpy hay Pillow, và không được cài thêm.
- Đo bằng Python của Blender, có numpy 2.3, không có scipy hay Pillow: `/Applications/Blender.app/Contents/Resources/5.2/python/bin/python3.13 -I docs/codex-queue/252/measure.py`.
- **Một script tự chứa:** `-I` bỏ thư mục của script khỏi `sys.path`, nên không import file bên cạnh.
- **Đọc ảnh:** `magick in.png -depth 8 rgba:-` rồi `numpy.frombuffer`; ghi ảnh theo chiều ngược lại.
- **Thành phần liên thông và nở mặt nạ:** dùng ImageMagick 7 (`-connected-components 8`, `-morphology Dilate Disk:N`).
- **luma** = Rec.709 trên giá trị sRGB 8 bit / 255.

## Kiểm (ghi số vào báo cáo cho từng bản chọn; đo trên `.square.png` trừ khi ghi khác)

1. **Khổ và nền:**
   - đúng 1536×864 và 1080×1080;
   - mức đen đo ở bốn góc 32×32 ≤ 8/255 (ghi số); nếu > 3/255 thì trừ mức đen đó ra trước khi lưu.
2. **Lề:** khung bao các điểm luma > 8/255 nằm trong lề 8 % mỗi cạnh của cả hai bản cắt. Bỏ qua thành phần nhỏ hơn 0,05 % diện tích sáng.
3. **Một bố cục:** ngoài ba nét chỉ được 2–3 mẩu rời, mỗi mẩu ≤ 2 % diện tích sáng. "Ngoài" là nằm ngoài mặt nạ ba nét nở 24 px.
4. **Đường nóng:** điểm luma ≥ 0,85 chiếm 2–6 % diện tích sáng (luma > 0,1).
5. **Alpha:**
   - ở các điểm alpha ≥ 0,5, ghép lên nền đen sai số trung bình ≤ 2/255;
   - phần nhạt (alpha 0,05–0,5 trên tổng số điểm alpha > 0,05) < 15 %;
   - 4 px ngoài cùng có alpha = 0.
6. **Tấm xem** `games/immortality-cultivation/tmp/shots/codex-first-frames/fire-impact-k1-sheet.jpg`. Mỗi bản chọn có:
   - `.square.png` trên nền đen ở bề ngang 80, 150 và 400 px;
   - `.alpha.png` ghép thường lên đá tối `#2a2c30` và đá sáng `#d6d0c2` ở 150 và 400 px;
   - đường tâm của Kiểm 7 vẽ chồng lên ở ô 400 px.

   Ghi tên dưới từng ô (font `/System/Library/Fonts/Supplemental/Arial.ttf`).
7. **Độ mở của cung.** Codex tự đặt đường tâm của nét dài nhất bằng tay: ≥ 10 điểm từ gốc tới mũi, tọa độ pixel ở 1080×1080, ghi vào `docs/codex-queue/252/<tên>.strokes.json`. Khớp đường tròn Kåsa với các điểm đó.
   - **v1, v3:** góc quét từ đầu tới cuối đường tâm quanh tâm khớp phải từ 120° tới 180°.
   - **v2:** góc giữa hai nét ngoài cùng tại gốc chung, lấy theo hướng của 15 % đầu mỗi đường tâm, từ 140° tới 180°.
   - Không ghi tâm cung vào prompt.
8. **Nét thuôn.** Dùng đường tâm của Kiểm 7.
   - Bề dày = độ dài đoạn liền luma > 0,1 dọc pháp tuyến, lấy trung vị trong ±3 % chiều dài.
   - Đo ở 20 % và 80 % chiều dài tính từ đầu dày. Tỉ lệ phải ≥ 3. (`ff-a1-c5` chỉ được 0,81.)
9. **Khung cuối:**
   - diện tích sáng bằng 15–35 % diện tích sáng của khung đầu;
   - ít nhất 70 % điểm sáng nằm trong mặt nạ khung đầu đã nở 12 px;
   - độ lệch tốt nhất giữa hai mặt nạ (tương quan chéo trong ±24 px) ≤ 4 px.
10. **Tự chấm ở 150 px** theo thang của hai bài chấm (mốc: `ff-a1-c5` = 6,5; vệt Dragonhold = 7), kèm một dòng lý do. Đây chỉ là điểm tự chấm: Claude, hai giám khảo mù và chủ dự án mới quyết định.

## Hết hạn mức
Nếu `image_gen` báo 429 hay bảo chờ:
- giữ mọi file và viết báo cáo phần đã xong;
- **dòng cuối của tin nhắn cuối cùng** ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`);
- lần chạy sau làm tiếp từ chỗ đã có.

## Nhận
- `fire-impact-k1/selected/` có 3 khung đầu và 2 khung cuối, mỗi khung đủ ba file.
- Tấm xem `games/immortality-cultivation/tmp/shots/codex-first-frames/fire-impact-k1-sheet.jpg`.
- `docs/codex-queue/252/measure.py` cùng các file `.crop.json` và `.strokes.json`.
- Báo cáo có:
  - số Kiểm 1–10 cho từng bản;
  - khổ thật và hộp cắt của từng lượt;
  - prompt mỗi lượt và chỗ đổi giữa các lượt;
  - tổng số lần gọi `image_gen` (≤ 10);
  - điểm tự chấm;
  - hai biến thể Codex đề nghị đưa vào Firefly trước, kèm lý do.
