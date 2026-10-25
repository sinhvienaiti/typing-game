# Tu Tiên Thủ Ải — Danh sách toàn bộ ảnh cần dùng (25/10/2026)

> **Nguồn:** canon `../00-canon.md` §21.3 (danh sách asset M0b), §8.3 (cơ quan), §10 (thú), §12 (trường phái, đan phù), §14 (tiền), §15 (cảnh giới, Đạo Quả), §16 (Tĩnh Tu), D47–D49 (phong cách, camera, danh sách nhân vật).
> **Chuẩn phong cách** (chủ dự án duyệt 25/10): chân dung A `art-src/identity/kiem-tu-portrait.png`. Sơn thủy huyền ảo chất Việt, lụa nhiều lớp, viền thêu, hạc, mây, ngọc; khuôn mặt đẹp, quý phái; không máu (vệt mực); không chép QCBH (không cầu chữ Hán, không cuộn giấy nhân vật, không bố cục HUD của họ).
> **Ai làm:** Codex tạo ảnh 2D bằng `image_gen` theo phiếu trong `docs/codex-queue/`. Ảnh nguồn 3D gửi Tripo do chủ dự án dựng, theo bảng 3D trong `docs/games/3D_REQUESTS.md`. Claude rig, nướng VAT và impostor.
> **Nơi lưu:** `games/immortality-cultivation/art-src/<nhóm>/<id>.png` (media, không vào Git), mỗi ảnh có `<id>.prompt.txt` bên cạnh.
> **Trạng thái:** "có" là file đã có trên máy (chưa phải đã duyệt); "chờ" là chưa tạo. Cập nhật khi mỗi lô xong.

## Tổng quan

| Lô | Nhóm | Số ảnh | Đã có | Phiếu Codex |
|---|---|---:|---:|---|
| A | Ảnh nguồn 3D (GLB): thú, cơ quan, prop, pháp bảo | 47 | 42 | 007, 007b, 008 |
| A2 | Ảnh nguồn 3D nhân vật theo danh sách đã duyệt: 4 MVP + pháp khí | 11 | 0 | 013 |
| A3 | Ảnh nguồn 3D 6 nhân vật sau MVP, 2 linh thú, 6 pháp khí | ≈ 22 | 0 | 013b |
| R | Danh sách nhân vật (concept) | 11 | 11, **chủ dự án duyệt 25/10** | 009 |
| E | Môi trường: đất, decal, phông, cỏ bụi | 23 | 0 | 010a |
| V | Kết cấu VFX | 18 | 0 | 010a |
| I | Biểu tượng | 35 | 0 | 010b |
| U | Giao diện, Sơn Môn, màn tựa | 15 | 0 | 010c |
| T | Tĩnh Tu | 10 | 0 | 010c |
| **Cộng** | | **≈ 192** | **53** | |

Âm thanh và nhạc không nằm trong danh sách này. Danh sách âm làm ở M0b (canon §22), sinh âm bằng audio-lab trên Mac.

## A. Ảnh nguồn 3D (gửi Tripo; luật ảnh: nền `#E6E6E6`, tư thế A, không hiệu ứng)

| Id | Món | Góc | Trạng thái |
|---|---|---|---|
| `cultivators/kiem-tu` | Nữ Kiếm tu (D47, chuẩn phong cách) | trước, sau | có (008); tay cần mở thêm trước Tripo |
| `cultivators/tho-the-tu` | Thổ thể tu | trước, sau | có (007); **vẽ lại theo chuẩn D47** sau khi duyệt danh sách D49 |
| `bots/bot-dao-dong-tho` | Bot Đạo Đồng | trước, sau | có; vẽ lại theo D47 cùng đợt |
| `beasts/thach-thu` | Thạch Thử (bầy) | ngang, trước | có |
| `beasts/phong-lang` | Phong Lang | ngang, trước | có |
| `beasts/hoa-nha` | Hỏa Nha (bay) | trước, ngang | có; góc ngang chưa đạt (007b làm lại) |
| `beasts/nham-vien` | Nham Viên | trước, sau | có |
| `beasts/thiet-giap-tru` | Thiết Giáp Trư | ngang, trước | có |
| `beasts/dang-thu`, `beasts/khe-vien` | Biến chủng hệ dạy khắc (D23) | 2 góc mỗi con | chờ (007b) |
| `elites/*` | Tinh anh: Phong Lang Cuồng, Phong Lang Hồi Nguyên, Thiết Giáp Trư Thiết Bì | 2 góc mỗi con | có |
| `commanders/lang-dau-dan` | Thú tướng Lang Đầu Đàn | ngang, trước | có |
| `kings/thiet-boi-lang-vuong` | Thú Vương Thiết Bối Lang Vương | ngang, trước | có |
| `mechanisms/*` | Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng, Mê Vụ Trận | 1 | có |
| `props/*` | Cổng ải, Trận Tâm, Trận Trụ, đá vôi, tùng cổ | 1 | có |
| `treasures/thanh-phong-kiem` | Phi kiếm Thanh Phong (ô 1, "vạn kiếm") | trên, cạnh | trên: có; cạnh: chờ (007b) |
| `treasures/hau-tho-an` | Hậu Thổ Ấn (pháp bảo Thổ thể) | 1 | chờ (007b) |

## R. Danh sách nhân vật (D49; concept)

- **Gồm:** 5 trường phái × nam/nữ cộng ảnh đội hình. Kiếm nữ dùng chân dung A.
  - Kiếm (nữ, nam), Thổ thể (nam, nữ), Phù (nam, nữ), Hỏa (nam, nữ), Ngự thú (nam, nữ, kèm linh thú nhỏ);
  - ảnh đội hình `roster/doi-hinh.png`.
  - Phiếu 009.
- **Chủ dự án duyệt cả 10 ngày 25/10** ("10 ảnh kia đạt").
- **Ảnh nguồn 3D theo bộ này:**
  - phiếu 013: Kiếm nam/nữ, Thổ thể nam/nữ, trượng đá;
  - phiếu 013b: 6 nhân vật sau MVP, linh lộc, linh cáo, 6 pháp khí.
- **Thay thế:**
  - `cultivators/kiem-tu.*` thay bằng `kiem-nu.*`;
  - `tho-the-tu.*` thay bằng `tho-the-nam.*`, `tho-the-nu.*`.
  - Bot không có ảnh nguồn riêng: dùng model trường phái còn lại, đổi màu áo.

## E. Môi trường (2D dùng thẳng: nướng lên đất, lặp liền mép)

| Id | Món | Số | Ghi chú |
|---|---|---:|---|
| `ground/thanh-thach/*` | Ô đất lặp 1024², liền mép bốn phía: đá lát cổ, đá lát rêu, đất sỏi, cỏ núi, đá vôi lộ, bậc đá | 6 | Nhìn thẳng từ trên, ánh sáng phẳng |
| `decals/thanh-thach/*` | Decal mực trên đất 1024², nền trong suốt, lề ≥ 8 %: vết mực loang, vết nứt, rêu đốm, lá tùng rụng, vòng trận khắc, vết cào thú, hoa dại, sương đọng | 8 | Dùng để phá lặp đất |
| `backdrops/thanh-thach-{xa,giua,gan}` | Phông 3 lớp: núi đá vôi xa, rừng tùng giữa, mây sương gần | 3 | Ngang 4096 × 1024, liền mép trái và phải |
| `foliage/*` | Thẻ cỏ bụi nền trong suốt: cỏ núi, dương xỉ, bụi trúc, hoa dại, khóm tùng non, rêu đá | 6 | Cho tiền cảnh thưa |

## V. Kết cấu VFX (nền đen hoặc trong suốt, có alpha, 512² hoặc 1024²)

Vệt phi kiếm · quầng sáng kiếm · lá kiếm cho "vạn kiếm" (sprite) · vết chém cung · khói mực tan · bắn mực (trúng) · tia lửa trúng · bụi đất · sét xích (Lôi Phù Trụ) · vòng phong ấn (Phong Ấn Võng) · sương mê (Mê Vụ Trận) · vòng Kết Giới · vòng Hộ thân (`ward`) · vạch báo đòn có sọc (đỏ `#FF4A4A`) · nét thư pháp xanh ngọc "chữ thành chiêu" · xoáy Chân Nguyên · sét Thiên Kiếp · hào quang tinh anh. **Cộng 18.**

## I. Biểu tượng (256², nền trong suốt, đọc được ở 32 px)

| Nhóm | Món | Số |
|---|---|---:|
| Kiếm | Phi Kiếm, Ngự Kiếm Quyết, Nhất Tuyến Xuyên Vân, Hồi Kiếm Hộ Thân, Lưu Quang Bộ, Lạc Kiếm Trận, Thiên Hà Kiếm Vũ, Kiếm Tâm, Tích Kiếm | 9 |
| Thổ thể | Trấn Quyền, Chấn Địa Quyền, Phá Sơn Chưởng, Kim Cương Thân, Thạch Bích, Sơn Hà Trấn, Hậu Thổ · Bàn Thạch | 7 |
| Đan, phù | Hồi Xuân Đan, Kim Thân Phù, Lôi Hỏa Phù, Định Thân Phù | 4 |
| Cơ quan | Kiếm Thung, Lôi Phù Trụ, Phong Ấn Võng, Mê Vụ Trận | 4 |
| Tiền | Linh Sa, Văn Khí, Thú Hạch | 3 |
| Đạo Quả | Kiếm Ý Bất Tán, Kim Cương Bất Hoại, Lưu Quang, Trận Linh, Tụ Nguyên, Hữu Duyên | 6 |
| Cảnh giới | Luyện Khí, Trúc Cơ (MVP) | 2 |

**Cộng 35.** Màu ngữ nghĩa giữ theo canon §21.1: vàng kim chỉ cho tiền, đỏ chỉ cho nguy hiểm.

## U. Giao diện, Sơn Môn, màn tựa

- **Màn tựa:** tranh chính 1920 × 1080, theo chuẩn phong cách, không chữ (logo làm bằng CSS).
- **Màn chờ:** 1 ảnh.
- **Sơn Môn** (canon §4.2):
  - nền một màn tĩnh 1920 × 1080;
  - 4 tranh điểm: 1 Trận Đài, 2 Tĩnh Thất, 3 Thư Lâu, 4 Bảo Khí Lò.
- **Khung DOM** (9-slice, có alpha):
  - ô Bàn Quyết;
  - bộ thanh Sinh lực / Chân Nguyên / Trận Lực;
  - thanh Thế của Thú Vương;
  - thẻ triều (báo đợt);
  - bảng cửa hàng lúc nghỉ;
  - bảng Thu Hoạch;
  - khung học;
  - bộ nút và tab.
- **Cộng 15.**

## T. Tĩnh Tu (canon §16)

- **Nền:** người tu ngồi trên mặt nước tĩnh, núi và sương phía sau. Không có cầu tròn chữ Hán.
- **Lá phù giấy dó** chở chữ, mỗi loại nhận bằng viền và biểu tượng, không chỉ bằng màu:
  - Minh: viền trắng ngà có tia;
  - Thường: giấy trơn;
  - Thường khác nhóm: viền nhạt;
  - Tâm ma: khói mực tím than.
- **3 biểu tượng:** mặt trời (Minh), giọt mực (Thường khác nhóm), mắt nứt (Tâm ma).
- **Thẻ Khẩu Quyết** (thẻ học 6 từ trước phiên).
- **Hiệu ứng lĩnh ngộ** khi đủ 100 điểm.
- **Cộng 10.**

## Thứ tự làm

1. Phiếu 009 (danh sách nhân vật) và 007b (ảnh nguồn 3D còn thiếu).
2. Phiếu 010a: môi trường và VFX.
3. Phiếu 010b: biểu tượng.
4. Phiếu 010c: giao diện, Sơn Môn, màn tựa, Tĩnh Tu.
5. Sau khi chủ dự án duyệt danh sách nhân vật: vẽ lại ảnh nguồn 3D Thổ thể và bot theo chuẩn D47; thêm ảnh nguồn 3D cho nhân vật được duyệt.
