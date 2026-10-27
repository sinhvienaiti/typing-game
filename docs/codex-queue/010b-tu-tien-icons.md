# Phiếu 010b · Tu Tiên Thủ Ải · biểu tượng (35 ảnh)

**Bối cảnh:** lô **I** của `docs/games/tu-tien/art-requests/IMAGE_LIST.md`. Biểu tượng hiện trên Bàn Quyết, HUD, cửa hàng, Thư Lâu, Bảo Khí Lò và màn Đạo Quả.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/10-icons.md`;
- `games/immortality-cultivation/art-src/icons/`;
- `games/immortality-cultivation/art-src/README-010b.md`.

Không chạy git, không sửa mã.

## Nguồn phải đọc trước

- `docs/games/tu-tien/00-canon.md`, tra nghĩa từng món để biểu tượng nói đúng việc nó làm:
  - §12.1 Kiếm, §12.2 Thổ thể, §12.3 Đan, phù;
  - §8.3 Cơ quan;
  - §14.1 Ba tiền;
  - §15.1 Cảnh giới, §15.4 Đạo Quả;
  - §21.1 Màu ngữ nghĩa.
- `docs/games/tu-tien/art-requests/m0b/README.md`: khối phong cách chung.
- `games/immortality-cultivation/art-src/identity/`: ảnh chuẩn phong cách (chân dung A).

## Danh sách

| Nhóm | Id (`icons/<nhóm>/<id>`) | Số |
|---|---|---:|
| `kiem` | `phi-kiem`, `ngu-kiem-quyet`, `nhat-tuyen-xuyen-van`, `hoi-kiem-ho-than`, `luu-quang-bo`, `lac-kiem-tran`, `thien-ha-kiem-vu`, `kiem-tam`, `tich-kiem` | 9 |
| `tho-the` | `tran-quyen`, `chan-dia-quyen`, `pha-son-chuong`, `kim-cuong-than`, `thach-bich`, `son-ha-tran`, `hau-tho-ban-thach` | 7 |
| `dan-phu` | `hoi-xuan-dan`, `kim-than-phu`, `loi-hoa-phu`, `dinh-than-phu` | 4 |
| `co-quan` | `kiem-thung`, `loi-phu-tru`, `phong-an-vong`, `me-vu-tran` | 4 |
| `tien` | `linh-sa`, `van-khi`, `thu-hach` | 3 |
| `dao-qua` | `kiem-y-bat-tan`, `kim-cuong-bat-hoai`, `luu-quang`, `tran-linh`, `tu-nguyen`, `huu-duyen` | 6 |
| `canh-gioi` | `luyen-khi`, `truc-co` | 2 |

## Luật hình

- **Một gia đình hình**, mỗi nhóm có một dáng khung riêng để phân biệt nhóm ngay cả ở 32 px. Ví dụ: chiêu là ấn tròn, đan phù là lá phù dọc, cơ quan là ô vuông vát góc. Codex tự chọn rồi ghi vào prompt.
- **Hình bên trong:**
  - chỉ một hình chính, bóng rõ, tương phản cao;
  - không chữ, không số, không chữ Hán.
- **Màu ngữ nghĩa** (canon §21.1):
  - vàng kim `#FFC83A` chỉ dùng cho nhóm `tien`;
  - không dùng đỏ `#FF4A4A` làm màu chủ đạo của biểu tượng nào (đỏ dành cho nguy hiểm từ địch). Lửa của `loi-hoa-phu` dùng chu sa hoặc cam ấm.
  - Kiếm theo hệ Kim (bạc lam, trắng ngà); Thổ thể theo hệ Thổ (ngọc vàng đất, nâu đá).
- **Khổ:** sinh 1024², lưu bản cuối 256² PNG trong suốt và thêm bản 64² (`<id>@64.png`).
  - Nếu `image_gen` không ra nền trong suốt: sinh trên nền phẳng một màu, tách alpha bằng ImageMagick trong WSL (`~/.local/bin/magick`, ổ `D:` là `/mnt/d`).
  - Chỉ dùng `tools/art-normalize/` (phiếu 012) khi `docs/CODEX_QUEUE.md` ghi phiếu 012 "Claude đã duyệt"; không thì tự gọi `magick`.
  - Bản sinh giữ là `<id>.raw.png`; prompt lưu `<id>.prompt.txt`.
- Ảnh đã có thì bỏ qua. Ảnh hỏng rõ thì tạo lại tối đa 1 lần.

## Kiểm và bàn giao

1. **Ảnh xem nhanh** `art-src/_review/010b-icons.png`: mỗi biểu tượng ở 256, 64 và 32 px, trên nền tối và nền sáng.
   - Ghi trong README những biểu tượng khó đọc ở 32 px.
   - Ghi những cặp dễ nhầm nhau (ví dụ `ngu-kiem-quyet` và `phi-kiem`).
2. **Viết `README-010b.md`.**
   - Bảng mỗi biểu tượng: id, hình đã chọn, lượt sinh, đọc được ở 32 px hay không.
   - Khung từng nhóm.
   - Những gì chủ dự án nên xem.

**Xong khi:**
- file prompt viết xong;
- 35 biểu tượng (256 và 64), hoặc ghi lý do cho biểu tượng thiếu;
- ảnh xem nhanh và README đã có.
