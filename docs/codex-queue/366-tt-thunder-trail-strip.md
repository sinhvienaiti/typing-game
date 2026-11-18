# Phiếu 366 · Tu Tiên · Linh kiện: dải vệt đất sấm sét lặp liền (cho tám cột Ngũ Lôi)

Anh (12/11, sau bản 22): vệt của tám cột "đang kiểu vệt tự style, nhìn rất xấu, đáng lẽ nên là những vệt dạng sấm sét in dưới, hoặc nứt đất, có rực lửa 1 chút để vệt in nhìn thật hơn". Nguyên nhân: lab kéo dãn một ảnh vết tròn Lichtenberg theo chiều dài. Theo luật linh kiện (AGENTS.md "Components first"), cần **một linh kiện dải** lặp liền theo chiều dài; code nối các đoạn, không kéo dãn.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần `image_gen`**, `view_image` tối đa 10. Báo cáo `docs/codex-queue/366-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-trail-rock.v1-try*.png`, `S/thunder-trail-glow.v1-try*.png`, `S/thunder-trail-cap.v1-try*.png`, `S/thunder-trail-cap-glow.v1-try*.png`, `.prompt.txt` và tấm ghép `S/thunder-trail-366-sheet.jpg`. Cấm git ghi, sửa file có sẵn, mã.

## Tham chiếu (`view_image`)
`S/thunder-scar-crack-hot.v1-try9.png` và `S/thunder-scar-cooled.v1-try9.png` (chất đá, màu nứt rực và nguội đã dùng trong lab), `S/metal-rift-groove.v1-try1.*` (cách vẽ một dải lặp), bạch kim lôi D65 trong `docs/games/tu-tien/00-canon.md` (trắng ngà, vàng nhạt, mây mực; không xanh, tím, cam đậm).

## Bốn ảnh, nhìn thẳng từ trên xuống, cùng tỉ lệ đá
1. **`thunder-trail-rock`** 2048×256: dải đất đá vôi xám bị sét cày, giữa là một rãnh nứt chính chạy dọc, mép rãnh sém đen, các **nhánh nứt hình sét** (phân nhánh nhỏ dần) toả ra hai bên tới khoảng 80 % bề ngang; đá vỡ vụn, bụi than. Hai mép dọc mờ dần vào nền trong suốt (vẽ trên `#00FF00`, mép mềm). **Lặp liền theo trục x:** cột pixel đầu khớp cột cuối.
2. **`thunder-trail-glow`** cùng khổ, chồng khít lên ảnh 1: chỉ phần **phát sáng trong khe nứt** trên nền đen thuần: lõi trắng ngà mảnh, viền than hồng vàng nhạt ấm (không cam đậm), vài đốm than rải theo nhánh. Lặp liền theo x như ảnh 1.
3. **`thunder-trail-cap`** 512×256 và 4. **`thunder-trail-cap-glow`**: đoạn **đầu dải** (chỗ cột dừng ở mép): rãnh khép lại thành một điểm nổ nhỏ hình sao nứt; mép trái khớp liền với dải 1–2.
Không chữ, không vật khác, không bóng đổ. Lõi sáng không vượt 0,9 mỗi kênh ngoài đường lõi mảnh.

## Cách làm để chồng khít và lặp liền
- Vẽ **rock** trước. Làm **glow** bằng cách sửa chính ảnh rock đã chọn (giữ bố cục, chỉ còn ánh sáng trong khe nứt, nền đen); **cap-glow** sửa từ **cap** đã chọn. Không vẽ glow như một ảnh mới.
- `image_gen` không ra đúng cỡ: cắt và đổi cỡ về đúng 2048×256 và 512×256 bằng script, rồi làm lặp liền bằng dịch nửa chiều dài, vá đường nối (inpaint) hoặc hoà chéo, rồi dịch về. Làm y hệt cho glow để giữ chồng khít.
- Tách `#00FF00` thành kênh alpha, không viền xanh; phép so mặt nạ ở dưới dùng alpha này.
- Cap vẽ từ try dải đã chọn; mép trái cap khớp mép phải dải đó. Mỗi `.prompt.txt` ghi đường dẫn các ảnh tham chiếu và try gốc đã dùng.

## Kiểm và tự chấm
Script: hiệu cột đầu và cột cuối (lặp liền), ảnh glow chồng đúng khe nứt của ảnh rock (so mặt nạ), mép cap khớp dải. Tấm ghép: dải lặp 3 lần nối nhau + cap, bản thu về 64 px bề ngang để xem ở camera chơi, và bản rock+glow cộng sáng. Tự chấm theo mặt yếu nhất (thật như sét cày đất, đọc được nhánh sét, lặp không lộ đường nối, hợp bộ bạch kim); dưới 8 vẽ lại. Báo cáo ≤ 300 chữ.

Phản biện: PASS (Sonnet, 12/11; lỗi phản biện nêu đã sửa)
