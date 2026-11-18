# Phiếu 433f: Kim, mưa kiếm cao hơn, rộng hơn và lâu hơn (full-access, tự nhìn)

Phản biện: PASS (Sonnet, 17/11, vòng 4)

## Bối cảnh
Ngày 17/11 owner đã chọn trận pháp mẫu A (vành chữ cổ, kiếm hướng tâm). Lab đã dùng mẫu này làm mặc định (`?formation=old` để quay về bản cũ). Kiếm theo kiểu 433e: kiếm nhỏ là kiếm năng lượng, kiếm lớn là kiếm thật có hào quang.

Owner nhận xét cùng ngày: "bạn nên tăng độ cao, phạm vi và thời gian mưa kiếm rơi lâu hơn, chứ hiện tại đang hơi bé và nó có thời gian ngắn quá".

Thông số hiện tại trong `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts` (`METAL_RAIN`):
- `height: 8`, `sealDiameter: 12`;
- `waves: [0.6, 1.05, 1.5]`, `perWave: 16`;
- mưa kéo dài khoảng 1,4 s.

Phần giữ nguyên như `docs/codex-queue/433e-tt-metal-sword-mix.md`:
- quyền chạy, server 3148, ffmpeg, prune, cách đo p95;
- phạm vi sửa: `games/.wt-ic-lab-all/src/lab/metal-ult-*` và `metal-sword-look.ts`.

Được ghi `docs/codex-queue/433f-report.md` và `ABOUT.md`. Khi xong phải tắt Chrome và xoá thư mục profile tạm.

## Mục đích của việc nâng cao (owner 17/11, bổ sung)
"việc tăng cao trận pháp chủ yếu để cho cảm giác mưa kiếm rơi xuống đẹp hơn, chân thật hơn, không bị kiểu vừa rơi ra đã chạm đất, nếu việc nâng cao trận pháp làm khó nhìn, thì phải tìm cách để làm được những việc kia". Đích thật là **quãng rơi nhìn thấy dài**: ở camera chơi, mỗi kiếm phải bay thấy rõ ≥ 0,45 s và đi được ≥ 18 % chiều cao khung trên màn hình trước khi cắm đất. Độ cao 13–15 m ở mục 1 chỉ là cách đầu tiên; nếu trận cao làm khó nhìn (ra mép, nhỏ, lệch), được đổi cách miễn đạt đích, ví dụ: kiếm hiện từ trên trận (ngoài mép trên khung) lao xuyên qua trận; rơi có gia tốc từ chậm tới nhanh; trận đặt lùi về sau đàn quái để đường rơi chéo về phía camera dài hơn trên màn hình; vệt kiếm dài theo tốc độ. Ghi rõ cách đã chọn và số đo trong báo cáo.

## Việc
1. **Cao hơn (một cách, không bắt buộc; khi khác với đích quãng rơi thì đích quãng rơi thắng):** thử trận pháp ở độ cao 13–15 m (gấp khoảng 1,7 lần). Kiếm rơi từ trận xuống, vệt kiếm dài hơn tương ứng. Ở camera chơi, trận không chạm mép trên, lề ≥ 4 %.
2. **Rộng hơn:**
   - Đường kính trận 20–24 m.
   - Vùng kiếm rơi phủ phần lớn đàn quái: ở camera chơi, bề rộng vùng kiếm cắm ≥ 55 % bề ngang khung.
   - Phân bố đều, có khoảng trống, không dồn cục.
3. **Lâu hơn:**
   - Mưa kéo dài 3,5–4,5 s, gồm 5–6 đợt, nhịp dồn dần (các đợt sau dày hơn).
   - Kiếm lớn rơi cuối, sau đợt cuối khoảng 0,4 s.
   - Tổng số kiếm nhỏ 90–120. Kiếm cắm dư thì tan dần sớm, để số kiếm hiện cùng lúc ≤ 60 cho nhẹ máy (số ô `METAL_RAIN_CAPACITY` có thể > 60 vì giới hạn 60 là số kiếm sống cùng lúc). Đổi `perWave` thành danh sách theo đợt; cập nhật công thức `METAL_RAIN_CAPACITY`, hằng số shader của kiếm lớn (`step(CAPACITY-0.5)`, các mốc 2,0/2,4/2,6/3,4 s), `giantBirth`/`climax`/`dissolve` và `end` theo mốc mới.
   - Cả chiêu ≤ 7 s.
   - Âm thanh mưa kiếm kéo dài theo, lặp hoặc nối lớp âm Kim có sẵn, không thêm file mới.
4. **Giữ nguyên:**
   - kiếm lớn là điểm nhấn duy nhất (tỷ số độ sáng so với kiếm nhỏ ≥ 1,5);
   - vùng trắng ≤ 6 %;
   - trận pháp A;
   - kiểu kiếm 433e.

## Vòng lặp
- Tối đa 3 vòng: sửa → chụp → mở ảnh → so với nửa trái phân cảnh `games/immortality-cultivation/art-src/concept/ult-storyboards/ult-storyboard-samples-431.jpg` và nhận xét owner → sửa.
- Chụp ở camera chơi (Alt+1) và góc sau lưng (Alt+2), nền `?ground=%23353a40`, ở các mốc tính theo dòng thời gian thật của bản đã sửa (in ra): đợt 1, giữa mưa, đợt cuối, lúc kiếm lớn chạm đất, và 1 s sau đó.
- Đo quãng rơi: với mỗi kiếm, chiếu vị trí mũi kiếm ra màn hình camera chơi 1280×720 mỗi khung; "thấy rõ" = mũi kiếm nằm trong khung và độ mờ (alpha) ≥ 0,5; thời gian thấy = tổng thời gian thấy rõ trước khi cắm; quãng = |y màn hình lúc bắt đầu thấy − y lúc cắm| / 720.
- Mỗi vòng in ra:
  - trung vị và giá trị nhỏ nhất của thời gian thấy rõ và quãng rơi màn hình mỗi kiếm;
  - độ cao trận, đường kính trận, % bề ngang vùng kiếm;
  - thời lượng mưa, số đợt;
  - tổng kiếm và số kiếm hiện cùng lúc lớn nhất;
  - vùng trắng, p95.

## Nghiệm thu
- Quãng rơi: trung vị thời gian thấy rõ ≥ 0,45 s và trung vị quãng rơi ≥ 18 % chiều cao khung; ≥ 80 % số kiếm đạt cả hai.
- Kiểm kiểu 0 lỗi.
- p95 ≤ 16,7 ms, đo lúc mưa dày nhất.
- Lưu `metal-rain-f.jpg` và clip `.mp4` từ lúc kích chiêu tới khi kiếm tan hết (≤ 7 s). Giữ file cũ. Thêm một dòng vào `ABOUT.md`.
- Xoá khung thô. Không commit.
