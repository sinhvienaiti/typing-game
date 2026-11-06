# Kỹ năng Tu Tiên đang dựng thế nào, và video có phải cách tốt nhất? (06/11/2026)

Trả lời câu hỏi của anh ngày 06/11: nhiều kỹ năng đang dùng video Firefly, kể cả kỹ năng diện rộng; như vậy có tối ưu không, và game khác làm thế nào.

**Phạm vi:** game Tu Tiên Thủ Ải (`games/immortality-cultivation`).
- Lab chiêu: nhánh `claude/lab-element-kits`, commit `b8ebd51`, hơn `main` 68 commit.
- Bản chơi: `main`, commit `bbb46d8`.
- Chỉ đọc mã, đo file bằng `ffprobe`, `du` và Python, đọc nguồn ngoài. Không sửa mã.

**Cách ghi số:** "đo" là số đo hôm nay hoặc có trong changelog; "ước tính" là số tính từ công thức, chưa đo trên máy.

## 1. Tóm tắt

- **Mọi kỹ năng đẹp hiện mới chỉ chạy trong lab, chưa vào bản chơi.** Bản chơi chỉ có tia lửa khi trúng, số sát thương, khói mực khi quái chết, và một thanh kiếm tạm khoảng 32 tam giác.
- Trong lab, hình của chiêu lấy từ video Firefly (ảnh → video). Có hai cách phát:
  - cắt video thành **flipbook** (một tấm ảnh chứa nhiều khung) cho hiệu ứng nhỏ, lặp lại;
  - phát thẳng **video 1080p** cho chiêu lớn phím 8, phím 9 và thân sao băng. Đổi từ 06/11, vì atlas cũ 640×360, 6 khung/giây trông mờ và giật.
- Video 1080p đẹp nhất cho **một cảnh lớn tràn màn hình**. Trên máy M4, 2–3 video cùng lúc vẫn nhẹ (5,3–6,5 ms mỗi khung, đo).
- Nhưng video **không phải cách tối ưu cho mọi thứ**:
  - nặng tải: video phím 8 và 9 tổng 445 MB;
  - lab chỉ cho 3 video cùng lúc;
  - mọi bản sao của một video hiện cùng một khung;
  - không có kênh trong suốt;
  - khó co giãn, xoay hướng và khớp nhịp.
- Game thương mại dựng chiêu bằng **nhiều lớp**: hạt, flipbook nướng từ mô phỏng, mesh có shader, dải vệt, dấu đất, đèn, rung. Theo các nguồn công khai mình tìm được, video chủ yếu dùng cho cutscene, không dùng làm hiệu ứng chiêu.
- **Đề xuất: cách lai.**
  - Giữ video cho "cảnh lớn một lần": tuyệt kỹ, pháp tướng và cảnh tràn màn.
  - Chuyển mọi thứ lặp lại, nhiều bản cùng lúc sang flipbook nâng cấp: ô to hơn, 12–24 khung/giây, vector chuyển động, nén KTX2.
  - Hình phải theo hướng (vệt chém, luồng, vòng sóng) làm bằng dải mesh mang ảnh Firefly.
  - Hình vẫn từ Firefly hay Blender; code chỉ đặt, canh nhịp và cho chuyển động.
- Cần anh duyệt hướng. Đây là đổi đường ống lớn, nên hỏi Gemini một lượt trước khi làm.

## 2. Hiện tại mình dựng kỹ năng thế nào

### Đường đi của một hiệu ứng

1. **Ảnh tham chiếu 2D** do Codex, ChatGPT hoặc Gemini vẽ, anh duyệt.
2. **Firefly Video** biến ảnh thành video nền đen, 24 khung/giây, khoảng 5 s.
   - Hàng ngày 05/11 (đo): 494 bản trong 380 việc, tổng 2,56 GB.
   - Cỡ: 274 bản 1920×1080, 173 bản 1080×1080, 47 bản 1080×1920.
   - Tất cả là H.264 `yuv420p`, tức **không có kênh trong suốt**.
   - Một số lửa làm bằng Blender: 9 atlas trong `vfx/fire/blender/atlases`.
3. **`tools/vfx-flipbook`** cắt đoạn, tìm khung đỉnh và làm atlas PNG kèm JSON (manifest). Với chiêu lớn, công cụ xuất thêm MP4 1080p (libx264, CRF 18, 24 khung/giây).
4. **Lab** (`skills-lab.html`, chỉ chạy lúc làm, không build): code đặt thẻ đúng chỗ và quay theo camera. Code cho cú trúng rơi đúng khung đỉnh, rồi thêm số, rung, dừng hình, đèn và âm.
5. **Anh xem** ở 127.0.0.1:4310 hoặc qua video.

**Từ ngữ:**
- **Flipbook / atlas:** một tấm ảnh lớn chứa nhiều khung nhỏ của một đoạn chuyển động, phát lần lượt như lật sổ.
- **Video texture:** phát file MP4 thẳng lên một tấm phẳng trong cảnh 3D.
- **Shader:** đoạn mã nhỏ chạy trên card đồ hoạ, quyết định màu từng điểm ảnh (cuộn, ăn mòn, đổi màu một ảnh).
- **Mesh:** khung hình 3D (tấm, dải, vòng) để dán ảnh lên.
- **Hạt (particles):** hàng trăm hình nhỏ bay ra: tia, tàn, lấp lánh.
- **Cộng sáng (additive):** màu cộng vào cảnh, đen là không thấy. Đây là cách duy nhất dùng được video Firefly, vì video không có kênh trong suốt.

### Bảng theo nhóm chiêu và pha

Ký hiệu:
- **V** video 1080p;
- **F** flipbook;
- **S** mesh và shader dùng ảnh;
- **C** hình do code tự vẽ (nợ: anh đã chê dạng này);
- **H** hạt;
- **M** model 3D;
- **Â** âm Firefly.

| Nhóm | Tụ lực | Phóng | Bay | Chạm | Dư âm | Ở đâu |
|---|---|---|---|---|---|---|
| Phím 0–7 (phái Kiếm), hệ Kim mặc định | C ấn dưới chân, H | H, C tia sáng | M kiếm thật (GLB; ở xa là ảnh chụp model) | H, C tia, rung | C dấu đất | Lab |
| Phím 0–7, hệ Hỏa | F xoáy lửa, H | F, C vòng nhiệt | M, lửa bọc lưỡi | F, C điểm lửa | C vết cháy, F | Lab |
| Phím 7 Hỏa, nhát kết | | | S dải lửa Firefly (phiếu 275) | | | Mã có trên `main`, chỉ lab dùng |
| Phím 0–7, 12 hệ còn lại | F | F | F (ribbon, sheath) | F (impact, burst) | F (groundMark) | Lab |
| Phím 2 lưỡi liềm, mẫu 5 pha Hỏa | F vỏ lửa, lấp lánh, ấn | F vòng, sen lửa | F lưỡi liềm (8 khung/giây, 41 khung, ô 512×288) | F nổ, H tàn | F vết cháy từ tranh | Lab |
| Phím M, mưa thiên thạch (D62) | F (mẫu Hỏa) | F dải lên trời | **V** thân sao chổi (một video chung cho cả loạt), S quả cầu, F đuôi | F vòng, sen lửa, phun tia, sóng; H | F đất cháy, khói | Lab |
| Phím 8: 4 cột trụ, 13 tuyệt kỹ | **V** cả chiêu là một thẻ tràn màn; F 640×360, 6 khung/giây chỉ dự phòng | | | Code: số, rung, dừng hình, đèn; F ấn 0,2 s trước đòn | **V** | Lab |
| Phím 9: 30 chiêu mở rộng (A diện rộng, B pháp tướng, C thần thú, D pháp bảo) | như phím 8 | | Rồng C1, chu tước C3: thẻ **V** bay qua sân trong 1 s | như phím 8 | | Lab |
| Phím C, luồng duy trì (D61) | | F release của hệ | F ribbon từ tay tới quái | F impact mỗi nhịp | tan bằng ăn mòn 0,7 s | Lab |
| Bộ đếm chuỗi (D60) | giao diện: 5 tấm nền, 38 vảy, tia, mực, lụa, toàn ảnh đã duyệt | | | | | Lab |
| Đánh liên hoàn (melee) | chưa có mã | | | | | Mới có 39 ảnh vệt chém (13 hệ × 3 dáng, phiếu 317) |
| Song Long | | | M rồng năng lượng GLB 25.990 tam giác, 40 khớp (Codex 292) | | | Nhánh `claude/dragon-swarm-lab` |
| **Bản chơi (`main`)** | | | kiếm tạm khoảng 32 tam giác | H tia trúng, số | khói mực | Game |

**Ghi chú:**
- Âm (**Â**) có ở hầu hết chiêu lab: mỗi chiêu phím 8 và 9 có file `tt-sfx-*` riêng. D6–D8 tạm mượn âm tuyệt kỹ vì Firefly hết lượt.
- Thư mục `src/view/skills` (mọi lớp chiêu) chỉ được lab nhập. Đường chơi `app → stage → fx` chỉ dùng `hitfx.ts` và `swords.ts`. Đã kiểm hôm nay bằng grep, khớp bảng rà ngày 05/11 (`CODE_DRAWN_AUDIT_2026-11-05.md`).
- Bảng rà 05/11 còn 17 chỗ hình do code vẽ (**C**). Nhiều nhất là ấn dưới chân phím 0–7 và sigil trên đất.

## 3. Con số thật

### Dung lượng file (đo hôm nay)

| Thứ | Số file | Tổng | Mỗi file | Ghi chú |
|---|---|---|---|---|
| Video phím 8 (`vfx/ult`) | 19 | 147 MB | trung vị 8,4 MB, tới 11,1 MB | 1080p (1 file 1080×1080), 24 khung/giây, 5 s, trung vị 13,4 Mbit/s |
| Video phím 9 (`vfx/expansion`) | 30 | 298 MB | trung vị 9,6 MB, 6,4–16,3 MB | trung vị 15,2 Mbit/s |
| Video thân sao chổi | 23 (15 đang dùng) | 90 MB | trung vị 4,0 MB | 4,5 s, trung vị 7,8 Mbit/s |
| Atlas trong `art-src/lab/vfx` | 343 | 1,34 GB (PNG) | | 318 atlas RGB (cộng sáng), 25 có kênh trong suốt |
| Nguồn Firefly ngày 05/11 | 494 | 2,56 GB | khoảng 5 MB | 24 khung/giây, không trong suốt |

Video xuất ra ở CRF 18, gần như không nén mất. Vì vậy còn chỗ nén thêm (xem thử nghiệm bên dưới).

### Bộ nhớ card đồ hoạ (GPU)

**Mipmap:** các bản thu nhỏ sẵn của ảnh để nhìn xa không bị nhiễu. Chúng tốn thêm 1/3 bộ nhớ.

- **Đo trong lab** (changelog `2026-11-06-lab-perf.md`, Apple M4, Chrome):
  - Lúc mở lab đã có 2,87 GB texture. Riêng 48 atlas phím 8 và 9 (2560×2880, kèm mipmap) chiếm 1,87 GB, dù chiêu phát bằng video. Chrome dùng 9,8 GB.
  - Sau khi hoãn tải atlas: 0,99 GB texture, Chrome 2,9 GB. Sau 40 lần tung: 3,1 GB (trước là 9,65 GB).
- **Ước tính** (Python, công thức rộng × cao × 4 byte):
  - một atlas 2560×2880 kèm mipmap: 39 MB, khớp số đo (1,87 GB / 48);
  - một video 1080p: khoảng 8,3 MB, chưa tính bộ đệm giải mã của trình duyệt;
  - nạp hết 343 atlas không nén: khoảng 10,6 GB. Không thể nạp hết một lúc.

### Thời gian khung và số video cùng lúc

- **Thời gian khung (đo,** lab-perf, M4, 1920×1080, Chrome headless có GPU, bỏ giới hạn 60 Hz):
  - chỉ bầy quái: 5,1–5,7 ms;
  - 2–3 video cùng lúc: 5,3–6,5 ms trung bình, p99 ≤ 14 ms;
  - mốc 60 khung/giây là 16,7 ms.
- **Giới hạn video:** lab cho tối đa 3 video cùng lúc (`MAX_VIDEOS = 3`, `showcase.ts`).
  - Chiêu thứ tư dùng atlas. Lần đầu nạp atlas đó giật 0,45–0,7 s (đo).
  - Video không lên khung sau 1,5 s thì atlas thay vào (`VIDEO_STALL_MS`).
- **Trần của Chrome:** Chrome không tạo trình phát media thứ 76 trong một trang trên máy tính, thứ 41 trên điện thoại (thay đổi năm 2021). Đó là trần cứng; trần thực tế do bộ giải mã từng máy quyết định, mình chưa đo.
- **Độ khớp nhịp:**
  - với video, cú trúng đầu trễ 7–23 ms so với khung đỉnh (5 chiêu, đo 06/11);
  - với atlas, lệch 0–1 khung.
- **Chưa đo:** máy Windows tầm trung, máy yếu, Safari, iPhone.

### Độ đọc chữ trên quái (đo 06/11)

- 33/48 chiêu phím 8 và 9 để ≥ 50 % thẻ chữ nằm trên vùng sáng. Những chiêu đó cần nền thẻ đục ≥ 0,6.
- Bảng hạ sáng `?readable=1` giảm con số này còn 12/48.

### Thử nghiệm nhỏ hôm nay

Một clip `azure-cloud-dragon` (phím 9), đo bằng `ffmpeg` và `ktx2-encoder`. **Chưa ai chấm bằng mắt, chưa nạp vào lab.**

| Cách | Tải về | GPU (ước tính) | Ghi chú |
|---|---|---|---|
| Video 1080p hiện tại (CRF 18) | 8,94 MB | 8,3 MB | đang dùng |
| Video 1080p, CRF 23 | 4,73 MB | 8,3 MB | SSIM 0,986 so với bản gốc |
| Video 720p, CRF 20 | 3,61 MB | 3,7 MB | SSIM 0,981 |
| Atlas hiện tại 2560×2880 (31 khung 640×360, 6 khung/giây), PNG | 6,46 MB | 39 MB | bản anh chê mờ |
| Cùng atlas, nén KTX2 ETC1S | 0,72 MB | khoảng 9,8 MB | mã hoá 10,8 s |
| Cùng atlas, nén KTX2 UASTC | 3,86 MB | khoảng 9,8 MB | mã hoá 26,3 s |
| Atlas thử 3840×2592 (30 khung 768×432, 12 khung/giây, chỉ 2,5 s đầu), PNG | 14,7 MB | 53 MB | |
| Atlas thử, KTX2 ETC1S | 1,51 MB | khoảng 13,3 MB | |
| Atlas thử, KTX2 UASTC | 8,87 MB | khoảng 13,3 MB | |

**Đọc bảng:**
- **SSIM:** điểm máy đo độ giống bản gốc (1 là y hệt). Nó không thay mắt anh.
- **KTX2:** định dạng ảnh nén mà card đồ hoạ đọc thẳng, không phải giải nén ra đầy đủ.
  - GPU ước tính với 8 bit mỗi điểm ảnh (ASTC 4×4 hoặc BC7) kèm mipmap.
  - ETC1S nhỏ nhất nhưng dễ mất chi tiết; UASTC giữ chi tiết hơn.

## 4. Các game khác làm thế nào

### Khối dựng hay gặp (có nguồn)

- **Hạt và flipbook nhiều lớp.** Bài phân tích vụ nổ Star Wars Battlefront II:
  - vụ nổ gồm rất nhiều hạt riêng, không phải một flipbook trên một tấm;
  - khói và lửa là hai lớp riêng;
  - hầu hết texture hiệu ứng nằm trong một atlas lớn 12288×8192.
- **Mô phỏng nướng thành flipbook.**
  - Unreal có công cụ Niagara Flipbook Baker để nướng mô phỏng thành flipbook.
  - EmberGen (JangaFX) mô phỏng lửa khói rồi xuất flipbook.
  - Một hoạ sĩ VFX làm hiệu ứng nước gậy kiểu Wukong (không phải Game Science) dùng mô phỏng LiquiGen xuất flipbook 8×8, cộng một dải Niagara cho vệt gậy.
- **Shader trộn texture nhiễu thay cho ảnh từng khung.**
  - Diablo IV tạo sương, lửa, vũng độc bằng cách trộn các texture nhiễu lặp, không cần ảnh từng khung.
  - Vertex shader làm mặt nước gợn khi chiêu nổ.
- **Chiêu co giãn theo cấp.** Diablo IV cho kỹ năng đổi cỡ, độ mạnh và thời gian. Hoạ sĩ chỉnh tốc độ sinh hạt, vận tốc, độ phát sáng và dải màu cho từng mức.
- **Luật dễ đọc** (style guide VFX của League of Legends):
  - tách lớp chính (mang tín hiệu lối chơi) và lớp phụ;
  - cỡ và độ sáng theo độ quan trọng của chiêu;
  - để độ sáng mạnh nhất cho lúc va chạm.
- **Chuyển động mesh nướng sẵn (VAT).** Houdini có công cụ ghi chuyển động của một mesh phức tạp vào texture để engine phát lại.
- **Vector chuyển động cho flipbook.**
  - Mỗi khung kèm một ảnh chỉ hướng điểm ảnh di chuyển, nên khung giữa được nội suy mượt thay vì hoà chồng hai ảnh.
  - Hướng dẫn Unreal 5 dùng cách này để làm chậm flipbook mà không giật. Unity có node trộn khung flipbook.
  - Diễn đàn realtimevfx: vector tạo bằng Twixtor, chạy tốt khi giữa hai khung hình không đổi quá nhiều.

### Game dùng video ở đâu

- **Cutscene.** Genshin Impact lưu cutscene thành file video USM (công cụ GI-cutscenes đọc thư mục `VideoAssets`).
- **Video làm hiệu ứng chiêu thì bị khuyên tránh.** Trên diễn đàn Unreal, một nhân viên Epic nói texture phim cho hiệu ứng hạt "unnecessarily CPU taxing" và khuyên dùng flipbook.
- **Chưa tìm được nguồn kỹ thuật công khai** về cách Genshin, Star Rail, Wuthering Waves hay Black Myth: Wukong dựng chiêu trong trận. Mình không suy đoán phần này.

### Vì sao họ ít dùng video cho chiêu

Tổng hợp từ các nguồn trên và số đo của mình:
1. **Video có một góc, một nhịp cố định.** Chiêu cần đổi cỡ, hướng, độ dài và nhịp theo cấp, theo mục tiêu.
2. **Nhiều bản cùng lúc.** Flipbook dùng chung một ảnh cho hàng trăm thẻ lệch pha; lab cho bể lấp lánh tới 640 thẻ. Mỗi video cần một bộ giải mã riêng.
3. **Kênh trong suốt khác nhau từng trình duyệt.** VP9 có alpha chạy trên Chrome và Firefox; Safari cần HEVC có alpha. Một báo lỗi cho thấy Safari làm mất alpha khi đưa video vào WebGL.
4. **Tốn CPU giải mã** (nhận xét của Epic ở trên).
5. **Chiêu đẹp là nhiều lớp nhỏ có vai trò** (League of Legends). Một video là một lớp duy nhất, khó tách.

**Bù lại, video hợp với mình ở mấy điểm:**
- giữ trọn chi tiết của một cảnh lớn mà không cần hoạ sĩ VFX;
- camera chơi cố định 55°, nên một thẻ phẳng quay từ đúng góc đó trông đúng;
- nhóm mình dựa vào Firefly. Vì vậy hình từ video AI là hướng đúng cho mình. Câu hỏi là đóng gói nó thế nào và dùng ở đâu.

## 5. So sánh các cách

| Cách | Đẹp, giữ chi tiết | Mượt | Điều khiển (ngắm, co giãn, khớp nhịp) | Nhiều bản cùng lúc | Bộ nhớ và tải | Công sức | Hợp luật nhà (hình từ Firefly/Blender, code chỉ cho chuyển động) |
|---|---|---|---|---|---|---|---|
| Video texture 1080p | Cao nhất cho cảnh tràn màn | Cao (24 khung/giây gốc) | Thấp: một góc, nhịp theo đồng hồ video, bản sao cùng khung | Thấp (lab ≤ 3) | GPU nhẹ (~8 MB), tải nặng (4–16 MB mỗi clip) | Thấp | Rất hợp |
| Flipbook PNG hiện tại | Tuỳ cỡ ô: tốt ở ô 256–512 cho hiệu ứng nhỏ; ô 640×360 trên cảnh tràn màn bị chê mờ | Vừa: 6–24 khung/giây; hoà khung ở nhịp thấp gây bóng chồng | Cao: lệch pha, co giãn thời gian, ăn mòn, đổi màu | Cao (bể instanced, hàng trăm thẻ) | GPU nặng (39 MB mỗi atlas lớn) | Vừa (có `vfxflip`) | Hợp |
| Flipbook + vector chuyển động + KTX2 | Khá đến cao (ô 768 trở lên; nén cần chấm) | Cao: 12 khung/giây vẫn mượt nếu vector tốt | Cao | Cao | Nhẹ: tải 0,7–1,5 MB, GPU ~10–13 MB (đo, ước tính) | Vừa đến cao: cần công cụ vector, shader, mã hoá | Hợp |
| Mesh + shader dùng ảnh (dải, vòng, lưỡi liềm, dấu đất) | Cao nếu hình là ảnh vẽ; xấu nếu code tự vẽ hình | Rất cao (tính mỗi khung) | Rất cao: theo hướng vung, độ dài, bán kính | Cao | Rất nhẹ | Cao: mỗi dạng một shader | Hợp khi hình là ảnh, shader chỉ cuộn và ăn mòn |
| Hạt (sprite từ ảnh) | Lớp phụ: tia, tàn, lấp lánh | Rất cao | Rất cao: bay theo quái, phản ứng va chạm | Cao (coi chừng chồng lớp sáng) | Nhẹ | Vừa | Hợp nếu sprite là ảnh vẽ (không đốm tròn code) |
| Model 3D + rig | Cao cho vật có khối nhìn gần (kiếm, rồng) | Tốt nếu có clip | Cao nhất: bay theo đường, xoay mọi góc | Vừa (tam giác, xương) | Vừa | Cao (Tripo, rig, clip) | Hợp; nhưng anh muốn sinh vật trong chiêu ở dạng năng lượng trong mờ |
| **Lai (đề xuất)** | Cao: mỗi lớp dùng cách hợp nhất | Cao | Cao | Cao | Vừa, có ngân sách | Vừa: làm dần | Hợp |

## 6. Đề xuất

### Nguyên tắc

- **Video:** cảnh lớn, xuất hiện một lần, tràn màn.
- **Flipbook:** thứ nhỏ, lặp lại, nhiều bản cùng lúc.
- **Dải mesh mang ảnh:** hình phải theo hướng hay theo chiều dài.
- **Hạt từ ảnh:** lấp lánh, tàn, tia (lớp hào quang).
- **Model 3D:** vật có khối nhìn gần (kiếm thật, rồng đôi).
- **Code:** đặt, canh nhịp, rung, số, ăn mòn. Code không vẽ hình.

### Cụ thể từng nhóm

| Thứ | Cách | Cài đặt | Vì sao |
|---|---|---|---|
| Tuyệt kỹ phím 8, chiêu tràn màn phím 9 | **Giữ V** | 1080p; thử nén CRF 23 hoặc 720p rồi anh so; ≤ 2–3 video cùng lúc; chỉ tải chiêu đang trang bị; nâng atlas dự phòng như dòng flipbook dưới | Một cảnh lớn cần chi tiết; xuất hiện một lần |
| Lớp quanh video | S, F, H | Ấn đất, vòng sóng, hạt, đèn, rung; co giãn theo cấp chiêu | Để chiêu không "phẳng" và đổi được theo cấp, như Diablo IV |
| Thần thú, pháp tướng bay nhiều hướng | F nhiều bản lệch pha, hoặc M (như Song Long) | Mỗi con một thẻ hay một model, đường bay riêng | Anh muốn "nhiều con, bay nhiều hướng, loạn cả map" (DECISIONS 05/11 ~02:05); một thẻ video không làm được |
| Thân sao chổi của mưa thiên thạch | **Đổi V → F** | Ô 512–768, 24 khung/giây, lặp; mỗi quả lệch pha | 18–24 quả đang dùng chung một video, nên mọi quả cùng khung |
| Va chạm, bám quái, sen lửa, phun tia, vòng sóng, đất cháy | F (giữ, nâng) | Ô theo cỡ thật trên màn (camera chơi khoảng 38 px/m ở 1080p); 12–24 khung/giây; vector chuyển động thay hoà khung khi phát chậm; nén KTX2 | Nhiều bản, cần lệch pha và nhẹ |
| Lưỡi liềm, vệt chém liên hoàn, luồng phím C, cột sáng | S dải mesh mang ảnh | 39 ảnh vệt chém (phiếu 317) và dải ribbon của hệ làm mặt nạ; shader cuộn, ăn mòn, đổi màu theo hệ | Phải theo mặt phẳng nhát vung và độ dài |
| Ấn dưới chân, sigil, vết nứt (đang là C) | S với ảnh vẽ | Thay 17 hình code theo bảng rà 05/11, thứ thấy nhiều nhất trước | Luật nhà: hình từ tranh, code chỉ cho chuyển động |
| Lấp lánh, tàn, tia | H | Sprite từ ảnh Firefly hay ảnh vẽ, bể instanced có sẵn | Lớp hào quang bắt buộc quanh mọi chiêu |

### Giữ "chất" Firefly thế nào

- Mọi hình vẫn ra từ Firefly hay Blender (ảnh tham chiếu → video). Flipbook chỉ là cách đóng gói video Firefly cho nhẹ và điều khiển được. Code không vẽ hình.
- Vector chuyển động tính từ chính video Firefly bằng công cụ dòng chảy quang (optical flow, như Twixtor hay TFlow trong các nguồn). Đây là việc tính toán, không phải AI nặng chạy máy.
  - Rủi ro: khung AI đổi nhiều thì vector sai. Phải thử trên clip thật.
- Mỗi bản đóng gói mới được so cạnh video gốc ở camera chơi. Hai giám khảo mù chấm, anh duyệt cuối.

### Rủi ro của cách hiện tại

1. **Tải và đĩa:** video phím 8 và 9 tổng 445 MB, thêm 90 MB sao chổi. Người chơi web phải tải trước khi chiêu hiện.
2. **Trần 3 video:** chiêu thứ tư rơi về atlas, lần đầu giật 0,45–0,7 s. Trong trận đông quái, có đồng đội, chiêu chồng nhau là chuyện thường.
3. **Cùng khung:** mọi sao băng cùng hệ dùng chung một video, nên cả trận mưa trông như in một khuôn.
4. **Không trong suốt:** chỉ cộng sáng được, nên dễ chói và che chữ (33/48 chiêu cần nền thẻ đục ≥ 0,6). Khói đen phải quay nền trắng làm lớp riêng (sao băng Ám).
5. **Khó điều khiển:** không co giãn theo cấp, không đổi hướng; nhịp đánh phải theo đồng hồ video.
6. **Điện thoại và Safari chưa thử:** có báo lỗi WebKit (2020) rằng chế độ tiết kiệm pin chặn video tự phát; Chrome điện thoại có trần 40 trình phát mỗi trang; Safari xử lý video có alpha khác Chrome.
7. **Atlas PNG không nén** từng làm Chrome lên 9,8 GB (đã sửa bằng hoãn tải, nhưng gốc vẫn là ảnh không nén).
8. **Chưa đo trên máy yếu:** số 5,3–6,5 ms là máy M4.

### Bước làm

1. **Anh duyệt** nguyên tắc lai này. Đây là đổi đường ống lớn, nên trước khi làm hỏi Gemini (4 Argon, High) một lượt; Gemini tự duyệt đạt hai lần liền (theo `AGENTS.md`).
2. **Thử một clip, ba bản cạnh nhau** trong lab ở camera chơi:
   - (a) video 1080p hiện tại;
   - (b) video nén CRF 23 hoặc 720p;
   - (c) flipbook 768×432, 12 khung/giây, có vector chuyển động, nén KTX2.

   Gửi anh video so sánh; **anh chọn mức nét**.
3. **Thêm vào `tools/vfx-flipbook`:** xuất KTX2 và vector chuyển động. Làm thành phiếu Codex sau một critic PASS.
4. **Đổi thân sao chổi sang flipbook lệch pha,** đo lại, gửi anh video trước và sau.
5. **Đánh liên hoàn** dùng dải mesh theo lưỡi và 39 ảnh vệt chém (đã có trong `melee-combo.md`). **Anh duyệt mẫu Hỏa** trước khi làm 14 hệ.
6. **Trước khi đưa vào bản chơi:**
   - đo trên máy yếu hơn và Safari;
   - đặt ngân sách: số video cùng lúc, MB GPU, MB tải mỗi bộ chiêu.
7. **Thay dần hình code (C) bằng ảnh,** bắt đầu từ ấn dưới chân phím 0–7.

Mỗi loạt làm theo luật nhà: hai mẫu gửi anh trước, rồi mới làm cả loạt.

## 7. Nguồn

**Trong repo**
- Lab `games/.wt-ic-lab-elements` (`b8ebd51`): `src/lab/showcase.ts` (`MAX_VIDEOS`, `VIDEO_STALL_MS`, cách đặt thẻ), `comet-head.ts` (một video chung mỗi hệ), `clip-skills.ts`, `five-phase.ts`, `meteor-rain.ts`, `channel-skill.ts`; `src/view/skills/flipbook.ts` (hoà khung, trường `video`), `element-clips.ts` (10 vai clip, sức chứa bể), `real-swords.ts`, `flame-slash.ts`, `sword-rain.ts`.
- Changelog lab ngày 06/11 (`docs/changelog/2026-11-06-*`): `lab-perf`, `lab-castable-skills`, `five-phase-samples`, `lab-meteor-rain`, `lab-channel-skill`, `lab-streak-counter`.
- Bản chơi `games/immortality-cultivation` (`bbb46d8`): `src/view/fx.ts`, `hitfx.ts`, `swords.ts`, `vite.config.ts`. Song Long: commit `4ec6a99`.
- Media: `art-src/lab/vfx/*/manifest.json`, `art-src/lab/firefly-sprint-2026-11-05/video/`. Công cụ: `tools/vfx-flipbook/vfxflip/video_export.py`.
- Tài liệu: `docs/games/VFX_STANDARD.md`; `docs/games/tu-tien/skills/CODE_DRAWN_AUDIT_2026-11-05.md`, `SKILLS_EXPANSION_2026-11-05.md`; `docs/work/tasks/lab-flipbooks.md` (atlas 640×360, 6 khung/giây và lý do đổi sang video), `melee-combo.md`; `docs/work/DECISIONS.md` (sinh vật trong chiêu ở dạng năng lượng; chiêu diện rộng nhiều con, nhiều hướng).
- Số đo hôm nay đo lại được bằng `ffprobe` trên các thư mục trên.

**Bên ngoài**
- League of Legends VFX style guide (tóm tắt): https://www.vfxapprentice.com/blog/10-league-of-legends-vfx-design-tips
- Diablo IV, đồ hoạ và hiệu ứng: https://news.blizzard.com/en-us/article/23964183/peeling-back-the-varnish-the-graphics-of-diablo-iv
- Diablo IV, kỹ năng co giãn: https://news.blizzard.com/en-us/article/23746639/diablo-iv-quarterly-update-december-2021
- Vụ nổ Battlefront II: https://simonschreibt.de/gat/battlefront-ii-layered-explosion/
- Texture phim và flipbook (diễn đàn Unreal): https://forums.unrealengine.com/t/movie-texture-vs-flipbook-pros-and-cons/298878
- Niagara Flipbook Baker: https://dev.epicgames.com/documentation/en-us/unreal-engine/niagara-flipbook-baker-quick-start-guide-in-unreal-engine
- EmberGen: https://jangafx.com/software/embergen
- Hiệu ứng nước gậy kiểu Wukong (hoạ sĩ ngoài): https://80.lv/articles/wukong-s-spinning-staff-water-vfx-powered-by-ue5-s-niagara-liquigen
- Houdini VAT 3.0: https://www.sidefx.com/docs/houdini/nodes/out/labs--vertex_animation_textures-3.0.html
- Vector chuyển động cho flipbook: https://realtimevfx.com/t/motion-vectors-for-animated-textures-how-do-you-generate-them/575?page=2, https://forums.unrealengine.com/t/community-tutorial-level-up-your-flipbooks-with-motion-vectors-and-subuv-blending-unreal-5-tutorial/2694470, https://docs.unity3d.com/Packages/com.unity.shadergraph@17.6/manual/Particle-Flipbook-Blending-Node.html
- Ghi chú bàn tròn VFX GDC 2023 (chồng lớp sáng là nguyên nhân giật hay gặp): https://realtimevfx.com/t/gdc-2023-vfx-roundtable-discussion-notes/23367
- Cutscene Genshin dạng USM: https://github.com/ToaHartor/GI-cutscenes
- Trần trình phát media của Chrome: https://groups.google.com/a/chromium.org/g/feature-media-reviews/c/ej_x3Ovqltw
- Video có kênh trong suốt trên web: https://jakearchibald.com/2024/video-with-transparency/
- Safari mất alpha của video trong WebGL: https://forum.babylonjs.com/t/safari-hevc-h-265-video-with-transparency-has-black-background/47898
- WebKit, chế độ tiết kiệm pin chặn video tự phát: https://bugs.webkit.org/show_bug.cgi?id=216887
- three.js `VideoTexture` (r170 trong repo: không mipmap, cập nhật theo `requestVideoFrameCallback`): https://threejs.org/docs/pages/VideoTexture.html
- three.js `VideoFrameTexture` (chưa có trong r170 của mình): https://threejs.org/docs/pages/VideoFrameTexture.html
- three.js `KTX2Loader`: https://threejs.org/docs/pages/KTX2Loader.html
- Basis Universal (ETC1S, UASTC): https://github.com/BinomialLLC/basis_universal
- Cỡ texture tối đa trên máy người dùng (≥ 4096 ở 100 % báo cáo): https://web3dsurvey.com/webgl2/parameters/MAX_TEXTURE_SIZE
