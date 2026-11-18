# Việc: ảnh tham chiếu trước, rồi mới làm video (05/11)

**Mục tiêu.** Mỗi hiệu ứng cần giữ dáng có một ảnh tĩnh làm khung đầu: ảnh đã duyệt nếu có, nếu chưa thì vẽ mới. Anh chọn ảnh, rồi Firefly Video chỉ làm chuyển động từ ảnh đó (ảnh → video). Phải xong trước khi tài khoản Firefly hết hạn, khoảng 23:00 ngày 05/11.

**Vì sao.** Anh chê rồng và hoa sen ra kiểu clip-art phẳng (01:00). Anh nói: "tôi tưởng là chúng ta sẽ tạo ảnh để tham chiếu trước r mới tạo ra những hình animation" (`DECISIONS.md`, 05/11 01:10). Kỹ năng `game-vfx-production` cũng ghi như vậy: `references/recipes.md` §1 (sinh vật thì Firefly chỉ làm chất lửa; dáng quan trọng thì phải có khung đầu) và `references/tool-choice.md` (bảng công cụ). Đọc đúng hai phần đó, không đọc thêm.

**Đầu vào**
- Danh sách 56 việc video: `docs/work/tasks/firefly-sprint-video.full-0110.json`.
- Ảnh đã duyệt dùng được làm khung đầu (dòng anh duyệt nằm trong `docs/work/DECISIONS.md`):
  - đầu rồng hướng A: `games/immortality-cultivation/art-src/lab/vfx/dragon/head-r1/solar-ember-regent.png`. Anh dặn thêm chân trước thứ hai, không để "cụt 1 tay";
  - lửa phím 1, khung đầu v1a;
  - dải áo khí kiếm: windsilk (Kim), fire-sheath (Hỏa);
  - lô 1: `fire-halo-ring`, `fire-halo-seal-loop`, `fire-twinkle-set`.
  - Tự tìm đường dẫn trong `art-src/` (theo manifest hoặc tên file).

## Bước
1. **Phân loại** 56 việc, ghi vào `docs/work/tasks/firefly-stills.json`:
   - `material`: dòng chảy liên tục, tia lửa, tàn lửa, khói, bụi sáng, dải. Những việc này vẫn tạo video từ chữ, nhưng chờ anh chọn kiểu câu lệnh (`video/style-*`).
   - `shape`: dáng quan trọng, gồm rồng, sen, ngọc, cổng, ấn, vòng hào quang, cánh nổ, vết nứt và vết cháy, nhát chém, sao, và các yếu tố cut-in. Mỗi việc `shape` ghi: `id`, `aspect`, ảnh đã duyệt dùng được (nếu có), câu lệnh vẽ ảnh tĩnh (≤ 600 ký tự), có cần khung cuối hay không.
2. **Câu lệnh ảnh tĩnh, chung một chuẩn cả bộ** (`game-art-pipeline` → `references/briefs-and-sets.md` §2):
   - nền đen đặc, vật ở giữa, lề ≥ 8 %, không chữ;
   - phong cách: hiệu ứng huyền thoại kiểu donghua cao cấp, sáng rực, có chiều sâu thể tích, chi tiết mịn, lấp lánh;
   - **không** dùng đầu câu "Anime … game VFX element";
   - **không** viết câu phủ định kiểu "No head";
   - **không** gọi tên sinh vật khi chỉ cần chất lửa.
3. **Rồng** (thân, đuôi, bờm):
   - ảnh tĩnh phải lấy từ đầu rồng A, có hai chân trước;
   - nếu Firefly Image cho tải ảnh tham chiếu (Style hoặc Composition reference) thì dùng ảnh đầu A;
   - nếu không, ghi `needs: gemini` để Claude làm sau. **Không** vẽ rồng chỉ bằng chữ.
4. **Thử trước khi chạy hàng loạt:**
   - làm tay 2 việc trước, nhìn kết quả;
   - nếu ra kiểu clip-art phẳng như ảnh bị chê (`typing-game-review/captures/tu-tien/firefly-sprint-video-check/sheet-0110.jpg`), sửa câu lệnh rồi mới chạy cả hàng.
5. **Chạy hàng:**
   - Firefly Image, chỉ model Adobe (Firefly Image 4 hoặc 5; không dùng model đối tác);
   - bộ chạy trong trang, trong **một tab mới**. **Không chạm tab-2** (tiếng hô) và **tab-3** (video);
   - mỗi việc 1 lần tạo, tức 4 ảnh;
   - lưu vào `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/<id>/cand<N>.png`, kèm `.prompt.txt`;
   - gửi file ra qua một máy nhận local (bản sao của `.local/ff-bridge/sprint-video-recv.py`, chọn cổng trống, không ghi đè media).
6. **Credit:**
   - ghi số credit mỗi lần tạo;
   - nếu ảnh tốn credit cao cấp và tổng vượt 1.500, dừng và báo.
7. **Tấm cho anh:**
   - mỗi tấm tối đa 12 việc; mỗi hàng là một việc với 4 ứng viên, có nhãn `id` và số ứng viên;
   - lưu vào `typing-game-review/owner-review/2026-11-05/tu-tien/firefly-stills/`, kèm `ABOUT.md`;
   - kèm một dòng đề xuất ứng viên tốt nhất cho mỗi việc, có lý do ngắn.

**Gặp hộp đăng nhập, trả tiền, điều khoản hay đồng ý:** dừng ngay và báo. Không bấm gì trong hộp đó.

**Giới hạn.** Khoảng 100 bước. Trả về tối đa 10 dòng: số việc `shape` và `material`, đường dẫn các tấm, credit, việc cần Gemini.

## Nhật ký
- 01:12 Phân loại xong `firefly-stills.json`: 38 `shape`, 18 `material`; 3 việc có ảnh duyệt dùng thẳng (glint-star-twinkle, presence-ring-loop, light-ring-pulse), 2 việc rồng (bờm, đuôi) dùng chung ảnh rồng cả thân → 33 lần tạo.
- 01:12 Nhận luật mới của anh (01:20 qua điều phối): mọi ảnh tĩnh phải có ảnh tham chiếu của mình (Style, thêm Composition khi dáng quan trọng), không bao giờ chỉ bằng chữ; chưa tạo ảnh nào nên không có cand-old. Ảnh tham chiếu cắt từ ảnh đã duyệt (v1a try3, fire-halo-ring, fire-halo-seal-loop, fire-twinkle-set, windsilk, fire-sheath, đầu rồng A, mặt C3 ffup); ghi vào `refSources` mỗi việc.
- 01:12 Máy nhận 127.0.0.1:8851 (bản sao trong scratchpad), máy phát ảnh tham chiếu 127.0.0.1:8852.
- 01:16 Điều phối: 3 việc rồng (body-ribbon, mane, tail-sweep) chuyển cho Claude làm bằng Gemini; ghi `owner: claude`, bỏ khỏi hàng Firefly → 32 lần tạo.
- 01:17 Trang `firefly.adobe.com/generate/image`, tab-4 (tab nền, vẫn tạo được). Chọn Firefly Image 4 (`adobe:firefly:colligo:image4`, 2048 px): có cả ô Composition và Style reference; Image 5 chỉ có một ô. Tạo ảnh ghi "unlimited", bộ đếm credit đứng ở 6468/10000 sau mỗi lần tạo (0 credit).
- 01:18 Thử 1: `fire-lotus-bloom-top` (style v1a, độ mạnh 50) ra lửa vẽ tay có chiều sâu, không còn clip-art phẳng (cand1, cand3 tốt). `sky-gate-open-close` (style windsilk + composition seal-loop) hỏng: chép nguyên vệt ngang của windsilk, nền không đen → giữ làm `candold1-4`.
- 01:20 Thử 2: cổng với style windsilk độ mạnh 0 vẫn y như cũ (`candold5-8`); `cutin-swords-fly-out` với style C3 độ mạnh 0 đẹp, không chép mặt, nhưng in chữ "10%" (do câu "10 percent margin") → `candold1-4`. Sửa: bỏ windsilk, việc màu cyan dùng style C3 độ mạnh 0; đuôi câu lệnh đổi thành "wide empty black border … solid pure black void".
- 01:25 Claude (rồng): Firefly Image 5 + ảnh tham chiếu đầu A (bám sát), 3 ảnh toàn thân `stills/dragon-body/dragon-body.v1-try1..3.png` (1296×816; có ảnh tham chiếu thì Firefly giữ tỉ lệ của ảnh đó). Tấm so gửi anh: `owner-review/2026-11-05/tu-tien/dragon-body-stills/`. Chờ anh chọn, rồi làm video từ ảnh. Ghi chú: trang để mặc định model đối tác Gemini, phải chuyển sang Image 5; gửi form vào iframe ẩn bị trang chặn, gửi thẳng thì được.
- 01:23 Thử 3 đạt: cổng (style C3 0 + composition seal-loop 1) có vành xé cyan, chiều sâu, nền tối; kiếm cut-in hết chữ "10%". Chạy cả hàng 32 việc bằng bộ chạy trong trang (tab-4), mỗi việc 1 lần tạo = 4 ảnh, ~25–30 s/việc. Credit trước khi chạy hàng: 6468/10000.
- 01:31 Claude (rồng, lượt 2): GPT Image 2.5 Flare trong Firefly (anh cho phép 01:35) + ảnh tham chiếu đầu A; 3 ảnh toàn thân `dragon-body.v2-try1..3.png` (1536×1024, nền đen) và tấm chân vuốt `dragon-claw-study.v1-try1.png`. Mỗi lần tạo 1 ảnh, khoảng 30 s, không hiện hộp điều khoản. Chân rõ hơn hẳn Image 5. Tấm so: `owner-review/2026-11-05/tu-tien/dragon-body-stills/dragon-body-v2-sheet.jpg`.
- 01:35 Đã xong 22/32 việc bằng Image 4 (mỗi việc 4 ảnh, có ảnh tham chiếu). Credit vẫn 6468/10000 (0 credit). Tab-4 bị ai đó bấm sang `?view=edit` (có ảnh trên canvas, "References (5)"), bộ chạy kẹt ở `fire-crescent-slash`.
- 01:38 Điều phối báo anh duyệt GPT Image 2.5 Flare (ngoại lệ model đối tác). Dừng bộ chạy Image 4; trang edit mặc định model Gemini, tôi đổi ô model sang Flare nhưng không tạo ảnh và không động vào canvas hay 5 tham chiếu đang có (có thể là bài thử rồng của điều phối). 10 việc còn lại chờ làm bằng Flare: fire-crescent-slash, fire-clash-flash, metal-impact-rays, metal-qi-burst, metal-qi-crescent-wave, metal-crack-glow, sword-rain-impact, metal-seal-ignite, metal-guard-arcs, sword-rift-strip.
- 01:45 Đổi ảnh sang `cand<N>.png` (100 file, giữ đúng kích thước). Ba tấm cho anh và `ABOUT.md` kèm đề xuất từng việc nằm ở `typing-game-review/owner-review/2026-11-05/tu-tien/firefly-stills/`. Việc yếu: dragon-pearl-shatter (không có mảnh vỡ), fire-molten-seam (ra dải lửa, không ra đường nứt); cut-in kiểu C3 có nền vẽ kín khung, không phải nền đen.
- 01:46 Đã tắt máy nhận 8851 và máy phát tham chiếu 8852 (script vẫn ở scratchpad: stills-recv.py, stills-ref.py, refs/stills-driver.js).
