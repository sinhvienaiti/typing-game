# Lửa làm bằng Blender (Sword × Fire), đêm 04/11/2026

Lane Blender của đêm 04/11: dựng một dây chuyền chạy không giao diện **Blender 5.2.2 LTS, Mantaflow (gas, fire)** ra atlas flipbook cho `FlipbookPool` của lab, rồi làm ba món lửa, mỗi món ít nhất 3 bản. Chưa đụng mã game; nối vào lab là bước sau, của agent khác. Media không vào Git.

- **Lời anh (04/11, sau nửa đêm):** "luôn ưu tiên dùng blender hoặc fire[fly] nếu 2 thứ này làm tốt hơn bạn… ngọn lửa bạn làm ra, nhìn như rác".
- **Kiểu lửa theo:** [`FIRE_STYLE.md`](FIRE_STYLE.md) (A · Brushfire: 3 nét lửa lớn cong theo lực kiếm, nét phụ ngược, mẩu rời, mép sắc trên lót tối, dải màu theo bậc, lõi trắng ≤ 5 %, tắt bằng cách tan từ đầu lưỡi).
- **Dây chuyền và cách chạy:** `games/immortality-cultivation/art-src/lab/vfx/fire/blender/README.md` (`firesim.py` trong Blender, `stylize.py` tô kiểu bằng numpy, `gen_recipes.py` giữ đúng thiết lập từng bản, `run.sh` qua `heavy.sh --cores=8`).
- **Ứng viên:** `art-src/lab/vfx/fire/blender/atlases/` có `manifest.json` đúng dạng lab (9 bản), mỗi bản `<id>.atlas.png` (RGBA, alpha thẳng), `<id>.heat.png` (trường nhiệt cho chế độ `heat`), `<id>.json`; B1 và b2-v4 có thêm `<id>.flow.png` (vector chuyển động).
- **Ảnh và video cho anh:** `games/immortality-cultivation/tmp/shots/overnight/blender/boards/board-b1.jpg`, `board-b2.jpg`, `board-b3.jpg` (khung chính trên đá tối và đá sáng); mỗi ứng viên có `<id>/<id>.sheet.jpg`, `<id>.preview.mp4` (tốc độ thật, nền đen, đá sáng `#d6d0c2`, đá tối `#2a2c30`) và `<id>.slow.mp4` (0,25×, trộn chéo như pool).

## Cách làm

1. **Mô phỏng:** domain gas mỏng theo chiều sâu (2,5D, cho nét lửa gọn), nguồn lửa là "nét bút": quả cầu chạy theo cung, tăng tốc, thon dần, nhiên liệu ít dần về đầu lưỡi, đặt tĩnh (không mang vận tốc nguồn, để khỏi cuộn thành chuỗi hạt). Dải B2 là một lưỡi kiếm dài phát lửa theo từng mảng nhiễu, gió lưỡi kiếm thổi về sau. Lửa đất B3 là nhiều điểm cháy rải trong một hình elip, tắt lệch nhau.
2. **Chiếu:** cộng lửa dọc tia nhìn (một lần render thể tích chỉ phát sáng), nhìn thẳng cho B1, B2 và camera cúi 35° hoặc 50° cho B3 (lớp nguồn sát đất được giấu, than hồng vẽ từ vết cháy dưới đất).
3. **Tô kiểu:** dải màu theo bậc (viền rượu `#5E1220`, đỏ thẫm, son, cam, hổ phách, lõi `#FFF4D6` ≤ 4 % diện tích), mép sắc khử răng cưa, lót tối `#1E0A0C` đều bề dày quanh viền, nhiễu màu trôi bên trong, xói mép theo nhiễu khi tàn, đường thời gian B1 thiết kế sẵn (giữ tới khung 11, tàn tới khung 35). Hình dạng và chuyển động là của mô phỏng; mã chỉ tô màu, đặt ngưỡng và xói.

## Ứng viên và tự chấm

Claude tự chấm, chưa qua giám khảo mù. **Không bản nào đạt 8,5.**

| Mục | Bản tốt nhất | Hai bản khác | Atlas | Tự chấm |
|---|---|---|---|---|
| B1 lửa va chạm (1,2 s) | `blender-b1-v15`: ba nét quạt từ điểm đánh, cong sang phải, bốn nét phụ ngược, tan từ đầu lưỡi | `b1-v17` (ba vầng trăng lồng theo cung kiếm), `b1-v16` (nét quét ngang) | 6×6 ô 512, 36 khung, 30 fps | 6–6,5 |
| B2 dải lửa lặp | `blender-b2-v6`: lưỡi lửa tách mảng, nghiêng về sau, nguội dần ra đầu lưỡi | `b2-v4` (cùng bake, tô thô hơn), `b2-v3` (dải mảnh, lưỡi nhỏ) | 4×8 ô 1024×256, 32 khung, 24 fps, lát x | 6 |
| B3 lửa đất (2,33 s) | `blender-b3-v7`: mười điểm cháy thấp tắt lệch nhau, còn than hồng nhấp nháy rồi tắt | `b3-v8` (nhìn 50°, nhiều điểm nhỏ), `b3-v6t` (ngọn cao, ô 256) | 8×7 ô 512×256, 56 khung, 24 fps | 5,5–6 |

**Vì sao chọn:** v15 đọc rõ nhất kiểu "nét thư pháp" và tan rời từng mẩu khi tàn (v17 đẹp ở pha bung nhưng tàn thành cục). b2-v6 lát và lặp sạch, có nóng ở gốc, nguội ở đầu. b3-v7 đúng chữ "lửa thấp tàn thành than", không ngọn nào chạm mép ô.

**Còn thiếu so với 8,5:**
- B1: thân nét phẳng màu, ít sống bên trong; khi tàn thì co thành cục tròn; hai mẩu rời trông như que diêm; chưa có lấp lánh (phần của lớp sao, tia lửa).
- B2: đầu lưỡi tròn, độ nghiêng chưa rõ, ruột lốm đốm.
- B3: đầu clip là các cục phồng tròn, ngọn hình giọt đơn giản.
- Gốc rễ: mô phỏng ở độ phân giải M4 làm trong vài phút cho chuyển động mềm nhưng hình bo tròn; thêm nhiễu wavelet thì mép lấm tấm như bông cải (đã thử, bỏ).

## Đề xuất bước sau

1. Anh xem ba bảng và video; nếu hướng Blender đáng theo, chọn một bản mỗi món để agent nối vào lab (`make_manifest.py <id…> --into-fire <id…>` chép bản chọn vào `art-src/lab/vfx/fire/` và thêm mục vào `manifest.json` của lab; Claude chưa làm vì lab nạp mọi atlas có trong manifest, ba bản 512 thêm khoảng 100 MB bộ nhớ ảnh).
2. So với lửa Firefly Video của lane bên cạnh trên cùng bảng; giữ cái đẹp hơn cho từng món (thứ tự ưu tiên của anh).
3. Nếu theo Blender: thử 3D độ phân giải cao hơn (bake hàng chục phút mỗi bản) với render Cycles có ánh sáng, hoặc dùng hình nét từ Firefly Video làm mặt nạ và dùng dây chuyền này chỉ để tô, cắt, lặp. Bỏ mẩu rời kiểu que diêm ở B1.
4. Vector chuyển động chỉ đáng dùng cho B1 (khung sau đoán đúng hơn 36–43 %); pool hiện chỉ trộn chéo, đọc `flow.png` là việc mã.
