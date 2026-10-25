# Phiếu 010a · Tu Tiên Thủ Ải · ảnh môi trường và kết cấu VFX (41 ảnh)

**Bối cảnh:** chủ dự án muốn có đủ mọi ảnh game cần. Danh sách tổng: `docs/games/tu-tien/art-requests/IMAGE_LIST.md`; phiếu này làm lô **E** (23 ảnh) và lô **V** (18 ảnh). Các ảnh này dùng thẳng trong game (2D), không gửi Tripo.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/08-environment.md` và `09-vfx.md` (file prompt mới);
- `games/immortality-cultivation/art-src/ground/`, `decals/`, `backdrops/`, `foliage/`, `vfx/` (ảnh);
- `games/immortality-cultivation/art-src/README-010a.md`.

Không chạy git. Không sửa mã, canon hay file prompt cũ.

## Nguồn phải đọc trước

- `docs/games/tu-tien/00-canon.md`:
  - §8.1: sân Thanh Thạch Ải;
  - §8.3: cơ quan;
  - §21.1: lớp hình, màu ngữ nghĩa, "chữ thành chiêu", vẻ thủy mặc;
  - D47, D48: chuẩn phong cách và camera thấy trọn sân.
- `docs/games/tu-tien/art-requests/m0b/README.md` và `00-identity.md`: khối phong cách chung. Giữ đúng khối này trong mọi prompt.
- Ảnh chuẩn phong cách: `games/immortality-cultivation/art-src/identity/` (chân dung A và cảnh 55°, xem `README-m0b.md`). Đính kèm cảnh 55° khi tạo ô đất và phông để giữ cùng bảng màu.

## Việc

1. **Viết hai file prompt** theo cách viết của bộ `m0b/`:
   - mỗi ảnh một khối `text`;
   - có id, công dụng, khổ, nền, cách dùng trong game;
   - viết khẳng định, không liệt kê điều cấm trong prompt.
2. **Tạo ảnh bằng `image_gen`.**
   - Ảnh nào đã có thì bỏ qua (chạy lại được).
   - Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
   - Bản sinh ra lưu `<id>.raw.png`; bản đã xử lý lưu `<id>.png`; prompt lưu `<id>.prompt.txt`.

### Lô E · môi trường (23)

| Id | Món | Khổ cuối | Xử lý |
|---|---|---|---|
| `ground/thanh-thach/da-lat-co`, `da-lat-reu`, `dat-soi`, `co-nui`, `da-voi-lo`, `bac-da` | 6 ô đất | 1024², liền mép bốn phía | Nhìn thẳng từ trên, ánh sáng phẳng, không bóng đổ dài. Làm liền mép bằng ImageMagick (offset nửa ô rồi hòa mép, hoặc cách tốt hơn). Kiểm bằng ảnh ghép 2×2 |
| `decals/thanh-thach/muc-loang`, `vet-nut`, `reu-dom`, `la-tung`, `vong-tran-khac`, `vet-cao-thu`, `hoa-dai`, `suong-dong` | 8 decal | 1024², PNG trong suốt, lề ≥ 8 % mỗi phía | Nếu `image_gen` không ra nền trong suốt: sinh trên nền phẳng một màu tách xa màu vật, rồi tách alpha và đặt lề bằng ImageMagick |
| `backdrops/thanh-thach-xa`, `-giua`, `-gan` | 3 lớp phông: núi đá vôi xa (đục), rừng tùng giữa (trên trong suốt), mây sương gần (trong suốt) | rộng ≥ 3072 px, tỉ lệ khoảng 4:1, liền mép trái–phải | Sinh 1536×1024 rồi nối và hòa mép bằng ImageMagick. Kiểm bằng ảnh ghép 2 bản kề nhau |
| `foliage/co-nui`, `duong-xi`, `bui-truc`, `hoa-dai`, `tung-non`, `reu-da` | 6 thẻ cỏ bụi | 512², trong suốt | Dùng cho tiền cảnh thưa |

### Lô V · kết cấu VFX (18)

- Phần lớn vẽ **trắng và xám trên nền đen** để game tô màu khi chạy (hòa cộng).
- Mực và khói mực là màu tối, không hòa cộng được: các ảnh đó làm **PNG trong suốt**.
- Ghi rõ trong README ảnh nào hòa cộng, ảnh nào trong suốt.

| Id (`vfx/…`) | Món | Khổ | Kiểu |
|---|---|---|---|
| `vet-phi-kiem` | Vệt sáng đuôi phi kiếm, dài, mảnh | 1024 × 256 | cộng |
| `quang-kiem` | Quầng sáng quanh lưỡi kiếm | 512² | cộng |
| `la-kiem-van-kiem` | Một thanh kiếm nhìn từ trên, thẳng đứng giữa ảnh, cho "vạn kiếm" (instancing) | 256 × 1024 | trong suốt |
| `vet-chem-cung` | Vết chém hình cung | 1024² | cộng |
| `khoi-muc-tan` | Khói mực tan (thú chết) | 1024² | trong suốt |
| `muc-ban` | Mực bắn lúc trúng đòn | 512² | trong suốt |
| `tia-lua-trung` | Tia lửa lúc trúng đòn | 512² | cộng |
| `bui-dat` | Bụi đất bốc lên | 512² | trong suốt |
| `set-xich` | Sét xích của Lôi Phù Trụ | 1024 × 256, lặp ngang | cộng |
| `vong-phong-an` | Vòng phong ấn của Phong Ấn Võng | 1024² | cộng |
| `suong-me` | Sương mê của Mê Vụ Trận | 1024², liền mép | trong suốt |
| `vong-ket-gioi` | Vòng Kết Giới quanh Trận Tâm | 1024² | cộng |
| `vong-ho-than` | Vòng Hộ thân (`ward`) | 1024² | cộng |
| `vach-bao-don` | Vạch báo đòn có sọc chéo. Vẽ xám, game tô đỏ `#FF4A4A` | 512², lặp ngang | cộng |
| `net-thu-phap` | Nét thư pháp "chữ thành chiêu". Vẽ trắng, game tô xanh ngọc `#7FF5E0` | 1024 × 256 | cộng |
| `xoay-chan-nguyen` | Xoáy Chân Nguyên | 1024² | cộng |
| `set-thien-kiep` | Sét Thiên Kiếp đánh từ trời xuống | 512 × 1024 | cộng |
| `hao-quang-tinh-anh` | Hào quang tinh anh dưới chân thú | 1024² | cộng |

Không làm flipbook: game tạo chuyển động bằng shader.

3. **Xử lý bằng ImageMagick trong WSL.** `magick` ở `~/.local/bin/magick`; đường dẫn Windows `D:\…` là `/mnt/d/…` trong WSL.
   - Gọi: `wsl -e bash -lc "<lệnh>"`, hoặc viết script `.sh` vào `games/immortality-cultivation/art-src/_tools/` rồi chạy `wsl -e bash /mnt/d/.../x.sh`.
   - Chỉ dùng `tools/art-normalize/` (phiếu 012) khi `docs/CODEX_QUEUE.md` ghi phiếu 012 "Claude đã duyệt"; không thì tự gọi `magick`.
4. **Làm ảnh xem nhanh** `art-src/_review/010a-environment.png` và `010a-vfx.png` bằng `magick montage`:
   - ảnh VFX hòa cộng: đặt trên nền tối;
   - ảnh trong suốt: đặt trên nền ca rô;
   - kèm các ảnh ghép kiểm liền mép.
5. **Viết `README-010a.md`.**
   - Bảng mỗi ảnh: id, khổ thật, kiểu (cộng hoặc trong suốt), số lượt sinh, đạt hay chưa, lỗi còn lại.
   - Cách xử lý đã dùng.
   - Những gì chủ dự án nên xem.

**Xong khi:**
- 2 file prompt viết xong;
- 41 ảnh đủ, hoặc ghi lý do cho ảnh thiếu;
- ảnh xem nhanh và README đã có.
