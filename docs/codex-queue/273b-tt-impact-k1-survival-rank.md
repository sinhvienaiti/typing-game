# Phiếu 273b · Tu Tiên · Công cụ: chuẩn hóa thứ tự sống sót (A.A) theo hạng, để lửa phím 1 tàn đều chứ không tắt vụt

**Loại việc:** sửa công cụ (`gpt-6.1-sol`, mức `xhigh`). Lời giải đã chốt.

**Báo cáo:** `docs/codex-queue/273b-report.md`.

**Đường duyệt:** Claude chốt lúc 21:15 ngày 04/11, sau khi xem `preview-ticks.png` của phiếu 273.
- Ở tick 9 quạt lửa còn đầy, tới tick 12 chỉ còn một vệt mảnh, tức gần như tắt hết cùng lúc. Luật của anh: đỉnh giữ, tàn bằng xói mòn, không bao giờ tắt vụt.
- Nguyên nhân: tấm kênh cho thấy A.A cao chỉ ở một dải hẹp phía trong nét lớn, phần còn lại của vỏ thấp. Khi ngưỡng xói `e` qua khoảng 0,25, phần lớn vỏ chết cùng lúc.
- Cách sửa: đổi A.A thành hạng phần trăm trong vỏ. Khi đó phần diện tích còn lại ≈ 1 − e, đúng đường cong của lịch `impact-key1`.

## Làm ở đâu (cwd là gốc repo cha)
### Được ghi
- `tools/vfx-masks/impact_masks.py` (thêm bước mục 1 và cờ chọn), `tools/vfx-masks/README.md`;
- `tools/vfx-masks/preview-masked.ts` (thêm video, mục 3);
- `games/immortality-cultivation/art-src/lab/vfx/fire/impact-k1-r2/fire-impact-k1-r2-v1a.a4.maskA.png` và `…a4.masks.json`: ghi đè **chỉ hai file này**, sau khi đã chép bản cũ thành `…a4.maskA.v1.png` và `…a4.masks.v1.json`;
- `.local/codex-runs/273-out/`;
- `docs/codex-queue/273b-report.md`.

### Cấm
- Sửa file khác trong art-src, sửa mã game, lệnh git ghi, cổng mạng.
- Chạy Python ngoài lệnh `uv run --offline --no-project --with numpy --with scipy --with pillow python3 …` như phiếu 273.

## Việc
1. **A.A theo hạng.**
   - Trong mỗi ô k, với các điểm có A.R > 0,5, lấy điểm số hiện tại `s = 0,75·life_norm + 0,25·edt_norm` (công thức của phiếu 273).
   - Đổi sang hạng phần trăm: `A.A = 0,02 + 0,98 · rank(s) / (N − 1)`, với N là số điểm trong vỏ. Điểm bằng điểm nhận hạng trung bình.
   - Điểm có 0 < A.R ≤ 0,5 (mép mềm) lấy A.A của điểm vỏ gần nhất nhân A.R / 0,5.
   - Ngoài vỏ: 0. Sau cùng làm mềm σ = 0,6 px.
   - RGB của maskA (hull, ink, hot) giữ y nguyên từng byte.
2. **Kiểm thứ tự còn đúng ý:** A.A trung bình vùng gốc > vùng mũi (20 % đầu và cuối dọc đường tâm) ở mọi ô, như Kiểm 2 của 273.
3. **Xem trước:**
   - Chạy lại `preview-ticks.png`, các tick như cũ.
   - Thêm `preview.mp4`: H.264, yuv420p, nền đá tối, 384×384 nhân 2.
     - Dựng mọi tick 0–42, phát 60 fps, tức tốc độ thật khoảng 0,72 s.
     - Rồi cùng chuỗi đó phát 15 fps (chậm 0,25×).
     - Lặp hai lần, nhãn tick tiếng Anh nhỏ ở góc.
   - Thêm `preview-area.json`: số điểm sáng (độ sáng > 0,1) theo từng tick, chia cho số của tick 9.

## Kiểm bắt buộc
1. Byte RGB của maskA mới trùng maskA.v1 ở mọi điểm.
2. Diện tích sáng tương đối (so với tick 9) giảm đơn điệu từ tick 9 tới 42, sai số ±2 % cho nhiễu. Ở tick 12 trong 0,50–0,80; ở tick 18 trong 0,10–0,30; ở tick 42 bằng 0. In cả chuỗi.
3. Vùng gốc > vùng mũi ở 24/24 ô.
4. `preview.mp4` dưới 5 MB, phát được (`ffprobe` ra codec h264 và đúng số khung).
5. `git status --short` chỉ có các file được ghi; `ls -la` các file art-src.

## Ghi chú cho anh (Claude sẽ hỏi, Codex không đổi)
Màu than cuối: với công thức ramp hiện tại của 258, điểm sống sau cùng mang màu trắng vàng (r gần 1), chưa thành than đỏ. Nếu anh thấy cuối đòn nên đỏ than, Claude sẽ viết phiếu shader riêng.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
