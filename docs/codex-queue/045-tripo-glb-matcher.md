# Phiếu 045 · Tripo · Bộ gợi ý ghép GLB tải về với ảnh nguồn (chỉ đọc media, không trình duyệt)

**Bối cảnh:** chủ dự án đang dựng 86 model Lời Gọi trên web Tripo, từ ảnh trong `typing-game-handoff-2026-10-25/tripo-upload-dot2/`. File GLB tải về mang tên Tripo tự đặt theo mô tả ảnh, ví dụ `stylized+wolf+3d+model.glb`, `wooden+bridge+3d+model.glb`. Vì vậy phải ghép từng file với đúng model.

Đợt 1 (26/10) Claude ghép tay 55 file; bảng đáp án nằm ở `docs/games/3D_IMPORT_2026-10-26.md` (cột "File Tripo" và "Mã model"). Phiếu này viết một bộ gợi ý: với mỗi GLB, đưa ra 3 model ứng viên có điểm. Claude vẫn duyệt bằng mắt trước khi nhập.

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `tools/tripo-match/match.mjs`: Node ESM, không gói ngoài. Đọc GLB bằng cách tự đọc header, chunk JSON và BIN, giống `tools/map-factory/registry/scan-assets.mjs` (được import hàm từ file đó). Đọc cỡ ảnh bằng ImageMagick `/opt/homebrew/bin/magick` qua `child_process`.
- `tools/tripo-match/test/match.test.mjs`;
- `tools/tripo-match/README.md` (tiếng Việt);
- `docs/codex-queue/045-report.md`.

**Cấm:**
- sửa, chép, xóa media (`.glb`, `.png`…) hay bất cứ gì trong `typing-game-handoff-2026-10-25/**`, `games/**`;
- lệnh git có ghi;
- mạng;
- dev server, trình duyệt;
- đụng Tu Tiên.

## Đầu vào và đầu ra

```bash
node tools/tripo-match/match.mjs --upload <thư mục upload> [--glb <thư mục GLB>] [--out <file.json>]
```

- `--upload`: thư mục có các thư mục con `face <N> - …` chứa ảnh `<game>_<id>[_front|_back|_left][.alpha|.flat].png`, cùng `INDEX.md`.
- `--glb`: mặc định `<upload>/_GLB tải về`.
- In ra một bảng Markdown, và ghi JSON nếu có `--out`. Mỗi GLB một dòng: tên file, số tam giác, tỉ lệ hộp, 3 ứng viên kèm điểm từng thành phần.

Không ghi gì cạnh media.

## Cách chấm (ghi rõ trong README, chỉnh được bằng hằng số)

1. **Bậc face limit:**
   - Tam giác của GLB, tính như phiếu 025 (cảnh 0, nhân theo node), so với số face trong tên thư mục của ảnh ứng viên.
   - Tripo thường ra sát dưới mức face. Đo trên đợt 1 rồi đặt luật: ví dụ trong [0,55; 1,02] × face thì cộng điểm, ngoài khoảng thì trừ mạnh.
2. **Tỉ lệ hình:**
   - Hộp của vật trong ảnh: `magick <ảnh> -fuzz 15% -trim -format '%w %h' info:`, cho tỉ lệ rộng : cao.
   - So với tỉ lệ của GLB nhìn từ trước, tức (X hoặc Z, lấy cạnh lớn hơn) : Y.
   - Lấy log tỉ số. Càng gần 0 càng điểm cao.
3. **Chữ trong tên file:**
   - Tách tên Tripo thành từ, bỏ `3d`, `model` và dấu `+`.
   - So với từ của id (tách `-`), tên tiếng Anh trong `docs/games/NAMES_EN.md` nếu có, và tên Việt bỏ dấu trong `INDEX.md`.
   - Thêm một bảng đồng nghĩa nhỏ trong mã: wolf↔soi, bridge↔cau, bamboo↔tre, feather↔long, scaffold↔gian, axe↔riu, hat↔non, cliff↔vach, waterfall↔thac…
4. **Ghép một-một:** mỗi ảnh chỉ thuộc một GLB. Chạy ghép tham lam theo điểm giảm dần: gán dòng chắc nhất trước, rồi bỏ ứng viên đó khỏi các dòng khác. Vẫn in đủ 3 ứng viên gốc cho mỗi GLB.

## Kiểm (bắt buộc)

1. **Đo trên đợt 1:** chạy với `--upload typing-game-handoff-2026-10-25/tripo-upload`.
   - So với bảng đáp án trong `docs/games/3D_IMPORT_2026-10-26.md`.
   - In: độ đúng top-1, top-3, và độ đúng sau khi ghép một-một.
   - Đích: top-3 ≥ 90 %, sau ghép một-một ≥ 80 %. Không đạt thì ghi thật số đo và lý do. Không chỉnh hằng số riêng cho từng file để ăn gian.
2. **Chạy với đợt 2:** `--upload typing-game-handoff-2026-10-25/tripo-upload-dot2`. Thư mục GLB có thể còn trống hoặc mới có vài file. Lệnh phải chạy xong và in "0 GLB" hay bảng cho các file đang có, thoát 0.
3. `node --test tools/tripo-match/test`. Có:
   - test cho từng thành phần điểm, trên dữ liệu nhỏ tự tạo trong RAM;
   - test ghép một-một trên một ma trận điểm cho trước.
4. md5 của mọi GLB và ảnh đã đọc, trước và sau khi chạy, không đổi.
5. `git status --short`: so với lúc bắt đầu, chỉ **thêm** file trong `tools/tripo-match/` và `docs/codex-queue/045-report.md`.

## Báo cáo `docs/codex-queue/045-report.md`

- Ba con số độ đúng trên đợt 1.
- Bảng các dòng sai, kèm lý do.
- Hằng số đã chọn và vì sao.
- Kết quả năm kiểm.

**Xong khi:** năm kiểm chạy xong. Đích độ đúng đạt, hoặc báo cáo nói rõ vì sao chưa đạt.
