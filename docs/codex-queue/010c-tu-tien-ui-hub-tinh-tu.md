# Phiếu 010c · Tu Tiên Thủ Ải · màn tựa, Sơn Môn, khung giao diện, Tĩnh Tu (25 ảnh)

**Bối cảnh:** lô **U** (15) và **T** (10) của `docs/games/tu-tien/art-requests/IMAGE_LIST.md`.

**Thư mục làm việc:** gốc repo `D:\typing-game`. Chỉ được ghi vào:
- `docs/games/tu-tien/art-requests/m0b/11-ui-hub-title.md` và `12-tinh-tu.md`;
- `games/immortality-cultivation/art-src/ui/`, `hub/`, `title/`, `tinh-tu/`;
- `games/immortality-cultivation/art-src/README-010c.md`.

Không chạy git, không sửa mã.

## Nguồn phải đọc trước

- `docs/games/tu-tien/00-canon.md`:
  - §4.1, §4.2: trận, Sơn Môn 4 điểm, Thu Hoạch;
  - §5: bảng phím, để biết Bàn Quyết có những ô nào;
  - §6.3: ô và loại từ;
  - §14.3: cửa hàng lúc nghỉ;
  - §16: Tĩnh Tu, đọc kỹ bảng Minh / Thường / Tâm ma;
  - §21.1: lớp DOM, màu ngữ nghĩa;
  - §21.3: dòng "không giống QCBH";
  - §24: tiếp cận, độ tương phản chữ.
- `docs/games/tu-tien/art-requests/m0b/README.md`, `00-identity.md`.
- Ảnh chuẩn phong cách `games/immortality-cultivation/art-src/identity/`. Màn tựa và Sơn Môn đính kèm chân dung A và cảnh 55°.

## Lô U (15)

| Id | Món | Khổ cuối | Ghi chú |
|---|---|---|---|
| `title/key-art` | Tranh màn tựa: nữ Kiếm tu (chân dung A) trên cổng Thanh Thạch Ải, triều thú xa dưới thung, núi đá vôi, mây | 1920 × 1080 | Chừa khoảng trống bên trái cho tên game và menu (làm bằng CSS). Không chữ |
| `title/loading` | Màn chờ: phi kiếm bay qua mây núi, tĩnh | 1920 × 1080 | Không chữ |
| `hub/son-mon` | Nền Sơn Môn: sân tông môn trên núi, 4 công trình đứng rõ | 1920 × 1080 | 4 công trình phải tách nhau để đặt điểm bấm. Ghi tọa độ tâm từng công trình vào README |
| `hub/tran-dai`, `hub/tinh-that`, `hub/thu-lau`, `hub/bao-khi-lo` | 4 tranh điểm Sơn Môn | 1024 × 768 | Hiện khi rê chuột hoặc chọn phím 1–4 |
| `ui/ban-quyet` | Khung ô Bàn Quyết | 9-slice, PNG trong suốt | Vùng chữ ở giữa phải phẳng, tối hoặc sáng đều, để chữ gõ đọc rõ |
| `ui/thanh-chi-so` | Bộ khung thanh Sinh lực / Chân Nguyên / Trận Lực | 9-slice | Một tấm chứa 3 khung |
| `ui/thanh-the` | Khung thanh Thế của Thú Vương | 9-slice | Rộng, uy |
| `ui/the-trieu` | Thẻ triều (báo đợt) | 9-slice | |
| `ui/bang-cua-hang` | Bảng cửa hàng lúc nghỉ | 9-slice | |
| `ui/bang-thu-hoach` | Bảng Thu Hoạch (màn kết) | 9-slice | Hai cột: học và RPG |
| `ui/khung-hoc` | Khung học (nghĩa, IPA) | 9-slice | |
| `ui/nut-tab` | Bộ nút và tab: thường, rê, chọn, tắt | một tấm | |

- **Khung 9-slice:**
  - sinh trên nền phẳng, tách alpha bằng ImageMagick (`~/.local/bin/magick` trong WSL, `D:` là `/mnt/d`);
  - giữa khung phải trơn để kéo giãn được;
  - ghi số cắt (trên, phải, dưới, trái, theo px) của mỗi khung vào `art-src/ui/slices.json`.
- **Ảnh 1920 × 1080:** `image_gen` sinh tối đa 1536 × 1024. Cắt về 16:9 rồi phóng bằng Lanczos; ghi khổ gốc vào README.
- Nếu đã có `tools/art-normalize/` (phiếu 012) thì dùng nó.

## Lô T · Tĩnh Tu (10)

| Id (`tinh-tu/…`) | Món | Khổ |
|---|---|---|
| `nen-mat-nuoc` | Mặt nước tĩnh, núi và sương phía sau; chỗ giữa cho người tu ngồi (model 3D đặt vào sau, nên không vẽ người). Không cầu tròn chữ Hán | 1920 × 1080 |
| `la-phu-minh` | Lá phù giấy dó, viền trắng ngà có tia | 512 × 256, trong suốt |
| `la-phu-thuong` | Lá phù giấy trơn | 512 × 256, trong suốt |
| `la-phu-thuong-khac-nhom` | Lá phù viền nhạt | 512 × 256, trong suốt |
| `la-phu-tam-ma` | Lá phù trong khói mực tím than | 512 × 256, trong suốt |
| `icon-mat-troi`, `icon-giot-muc`, `icon-mat-nut` | 3 biểu tượng: Minh, Thường khác nhóm, Tâm ma | 128², trong suốt |
| `the-khau-quyet` | Khung thẻ Khẩu Quyết (6 từ, IPA, nghĩa) | 9-slice; thêm số cắt vào `ui/slices.json` |
| `linh-ngo` | Ánh lĩnh ngộ khi đủ 100 điểm: vòng sáng tỏa trên mặt nước | 1024², hòa cộng trên nền đen |

**Ba loại lá phù** phải phân biệt được bằng viền và biểu tượng, không chỉ màu (canon §16). Vùng chữ giữa lá phải trơn: chữ gõ vẽ bằng DOM.

## Chung

- Ảnh đã có thì bỏ qua. Ảnh hỏng rõ thì tạo lại tối đa 1 lần.
- Bản sinh giữ là `<id>.raw.png` khi có xử lý; bản cuối là `<id>.png`; prompt là `<id>.prompt.txt`.
- **Ảnh xem nhanh:** `art-src/_review/010c-ui.png` và `010c-tinh-tu.png` (ảnh trong suốt đặt trên nền ca rô). Thêm một ảnh thử: khung Bàn Quyết kéo giãn 3 cỡ.
- **`README-010c.md`:** bảng từng ảnh (khổ, lượt sinh, đạt hay chưa); tọa độ 4 công trình Sơn Môn; những gì chủ dự án nên xem.

**Xong khi:**
- 2 file prompt viết xong;
- 25 ảnh đủ, hoặc ghi lý do cho ảnh thiếu;
- `slices.json`, ảnh xem nhanh và README đã có.
