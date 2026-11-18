# Phiếu 321 · Tu Tiên · Ảnh 2D: cả bộ đòn của boss và quái (14 ảnh, khung đầu cho video Firefly), có tự chấm

Anh (06/11 18:50): "Duyệt, vẽ cả bộ", sau khi xem 2 mẫu của phiếu 320. Phiếu này vẽ 14 ảnh còn lại, **cùng phong cách với 2 mẫu đã duyệt**. Mỗi ảnh sẽ là khung đầu cho một video image-to-video trên Firefly.

**Model `gpt-6.1-sol`, mức `high`. 14 lần gọi `image_gen`, cộng tối đa 6 lần vẽ lại cho ảnh tự chấm dưới 8.** Báo cáo: `docs/codex-queue/321-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`A = games/immortality-cultivation/art-src`. `S = A/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu.

## Hai mẫu đã duyệt (mốc phong cách cho cả bộ)
- `S/foe-boss-rend-claw.v1-try2.png` (Vồ Xé)
- `S/foe-boss-entrance-wolf-head.v1-try2.png` (Thú Vương xuất hiện)

Mở cả hai bằng `view_image` trước khi vẽ ảnh đầu tiên. Cả bộ phải cùng chất liệu: năng lượng trong suốt và khói mực, mép sáng sắc, tia lửa và ánh lấp lánh, nền đen thuần.

## Màu
- **Đòn và hình của quái:** bảng màu nguy hiểm: đỏ tươi `#FF4A4A`, đỏ thẫm, đen mực; xám thép cho Thú Vương (hệ Kim) và Thiết Giáp Trư. Không cam, không vàng, không tím.
- **Ấn** (từ trên tinh anh, thú tướng, Thú Vương mà người chơi gõ để phá thế): màu **sức gõ** xanh ngọc `#7FF5E0` và trắng ngà, vì đây là cơ hội của người chơi, không phải đòn địch.
- **Thú Vương chết:** khói mực và đốm linh quang trắng ngà, ngọc nhạt (canon §10.9: chết tan thành khói mực, không có máu).

## 14 ảnh
| Tên tệp trong `S/` | Ảnh tham chiếu dáng (ngoài 2 mẫu) | Hình |
|---|---|---|
| `foe-boss-iron-charge-head.v1-try1.png` | `A/kings/thiet-boi-lang-vuong.png` | **Thiết Bối Xung**: đầu sói thép năng lượng khổng lồ lao thẳng về phía trước ở mũi cú húc, hàm khép, tai cụp, bờm giáp xám dựng; sau đầu là luồng năng lượng đỏ và khói mực kéo dài, tia lửa thép văng hai bên. |
| `foe-boss-phase-roar.v1-try1.png` | `A/kings/thiet-boi-lang-vuong-front.png` | **Gầm chuyển pha**: đầu sói vua ngửa lên gầm, hàm mở rực đỏ, ba vòng sóng xung kích đỏ tươi bung ra quanh đầu, khói mực và mảnh giáp bay. |
| `foe-boss-frenzy-aura.v1-try1.png` | `A/kings/thiet-boi-lang-vuong.png` | **Cuồng (pha 3)**: bóng sói vua toàn thân đứng nghiêng, bao trong ngọn lửa năng lượng đỏ thẫm và đen mực bốc ngược lên dữ dội, mắt đỏ rực, tia đỏ quất ra như roi. |
| `foe-boss-summon-sigil.v1-try1.png` | `A/kings/thiet-boi-lang-vuong.png` | **Tru Gọi Đàn**: ấn tròn trên đất, nhìn chéo 55°, giữa ấn là hình đầu sói tru, vòng ngoài là phù văn đỏ và ba dấu chân sói; khói mực bốc lên từ mép, giữa có ánh đỏ như cổng mở. |
| `foe-boss-death-spirit.v1-try1.png` | `A/kings/thiet-boi-lang-vuong-front.png` | **Thú Vương chết**: đầu sói vua đang tan từ dưới lên thành khói mực trắng xám và hàng nghìn đốm linh quang trắng ngà, ngọc nhạt bay lên; mắt đã tắt, các tấm giáp rời ra rồi mờ đi. |
| `foe-commander-howl-ring.v1-try1.png` | `A/commanders/lang-dau-dan.png` | **Lang Đầu Đàn tru đàn**: bóng đầu sói đầu đàn ngửa lên tru, sóng âm đỏ hình vòng tỏa ra trên đất, dưới chân là vòng hào quang đỏ thẫm rộng có hoa văn móng sói. |
| `foe-wolf-bite-jaws.v1-try1.png` | `A/beasts/phong-lang.png` | **Phong Lang cắn**: hai hàm sói năng lượng đỏ tươi đang sập lại, răng như lưỡi dao sáng trắng ở mép, vệt gió xám và tia đỏ văng ra. |
| `foe-crow-dive.v1-try1.png` | `A/beasts/hoa-nha.png` | **Hỏa Nha bổ nhào**: bóng quạ lửa năng lượng đỏ thẫm khép cánh lao chéo xuống từ góc trên, lông cánh như lưỡi lửa đỏ đen, vệt đuôi dài, tàn lửa đỏ rơi. |
| `foe-ape-boulder.v1-try1.png` | `A/beasts/nham-vien.png` | **Nham Viên ném đá**: tảng đá xám khổng lồ nứt vân đỏ tươi phát sáng bên trong, đang bay theo đường cong, vệt bụi đá và tia lửa đỏ phía sau, vài mảnh đá vỡ bay theo. |
| `foe-boar-ram-head.v1-try1.png` | `A/beasts/thiet-giap-tru.png` | **Thiết Giáp Trư húc**: đầu lợn rừng giáp sắt năng lượng lao thẳng, nanh cong sáng trắng, tấm giáp xám, luồng đỏ và bụi đất cuộn phía sau. |
| `foe-seal-an.v1-try1.png` | 2 mẫu đã duyệt (chỉ lấy độ hoàn thiện) | **Ấn**: vòng ấn tròn lơ lửng màu xanh ngọc `#7FF5E0` và trắng ngà, hai vòng phù văn mảnh xoay ngược nhau, bốn mũi nhọn như khóa ở bốn hướng, **tâm để trống** (game đặt chữ vào đó), ánh lấp lánh và vầng sáng mềm. |
| `foe-elite-crest-frenzy.v1-try1.png` | `A/beasts/phong-lang.png` | **Tinh anh Cuồng**: huy hiệu lơ lửng khung đỏ thẫm, giữa là ba vết vuốt đỏ tươi bốc lửa năng lượng, tia đỏ quất ra. |
| `foe-elite-crest-ironhide.v1-try1.png` | `A/beasts/thiet-giap-tru.png` | **Tinh anh Thiết Bì**: huy hiệu lơ lửng khung đỏ thẫm, giữa là tấm khiên giáp thép xám ghép vảy, mép đỏ sáng, bụi sắt lấp lánh. |
| `foe-elite-crest-regen.v1-try1.png` | `A/beasts/nham-vien.png` | **Tinh anh Hồi Nguyên**: huy hiệu lơ lửng khung đỏ thẫm, giữa là một hạt sống xanh lục đậm đập như tim, các đốm xanh lục nhỏ bay lên, vầng sáng xanh mờ. |

## Cách làm mỗi ảnh
1. Mở bằng `view_image` 2 mẫu đã duyệt và ảnh tham chiếu dáng của ảnh đó. Lấy dáng từ ảnh trong `A/`, lấy chất liệu, ánh sáng và độ hoàn thiện từ 2 mẫu.
2. Gọi `image_gen`, khổ ngang 16:9 như 2 mẫu. Prompt (giống phiếu 320, đổi câu màu theo mục "Màu" ở trên cho Ấn và cho Thú Vương chết):
   ```text
   A premium Chinese donghua xianxia game VFX still: <SUBJECT>. The beast is made of translucent energy and ink smoke, mythic and menacing, not a realistic animal. Danger palette only: vivid scarlet red (#FF4A4A), deep crimson, ink black and cold steel grey; no orange, no gold, no purple. Radiant core light, crisp bright edges, layered glints, sparks and soft halos; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Centred with a wide empty border, solid pure black background, no ground, no text, no letters, no watermark.
   ```
   `<SUBJECT>` là câu ở cột "Hình", dịch sang tiếng Anh, giữ đủ chi tiết.
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu, prompt nguyên văn, khổ thật.
4. **Tự chấm** như phiếu 320 (đọc ra đòn hay ai; cuốn hút, uy lực; đúng màu, nền đen, không chữ; dùng làm khung đầu video được: ở giữa, viền rộng, không bị cắt). Thêm một tiêu chí: **cùng phong cách với 2 mẫu đã duyệt**. Ghi theo mặt yếu nhất. Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản điểm cao hơn.

## Xong khi
- Có đủ 14 ảnh (kèm `.prompt.txt`).
- Có tấm ghép `S/foe-boss-set-sheet.jpg`: lưới 4 cột, các bản đã chọn, kèm tên ngắn tiếng Anh dưới mỗi ảnh, nền đen. Mở bằng `view_image` để kiểm đúng ô trước khi báo cáo.
- Báo cáo có bảng: ảnh, bản chọn, điểm từng tiêu chí, một câu nhận xét.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
