# Phiếu 320 · Tu Tiên · Ảnh 2D: 2 ảnh mẫu đòn của boss và quái (làm khung đầu cho video Firefly), có tự chấm

Anh (06/11 18:35): "Vẽ ảnh quái, boss". Hàng video Firefly đang có đòn quái dạng vệt sáng chung chung (`foe-claw-rake`, `foe-bite-snap`…), vì chưa có ảnh nào để làm video đúng hình. Phiếu này vẽ **2 ảnh mẫu**; anh duyệt rồi mới vẽ cả bộ (danh sách ở cuối). Ảnh xong sẽ là khung đầu cho video image-to-video trên Firefly.

**Model `gpt-6.1-sol`, mức `high`. Đúng 2 lần gọi `image_gen`, cộng tối đa 2 lần vẽ lại cho mẫu tự chấm dưới 8.** Báo cáo: `docs/codex-queue/320-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`A = games/immortality-cultivation/art-src`. `S = A/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu.

## Bối cảnh (đọc nhanh)
- `docs/games/tu-tien/00-canon.md` §10.5 (Thú Vương Thiết Bối Lang Vương: sói khổng lồ hệ Kim, lưng bọc thép; đòn Vồ Xé là nón 6 m) và §10.9 (thú trúng đòn ra vệt mực, chết tan thành khói mực, không có máu).
- Camera trò chơi nhìn xuống chéo khoảng 55°.
- **Bảng màu nguy hiểm của quái** (luật): đỏ tươi `#FF4A4A` và đỏ thẫm, đen mực, xám thép cho Thú Vương hệ Kim. **Không cam, không vàng** (cam là lửa của người chơi, vàng là tiền).
- Phong cách: hoạt hình donghua tiên hiệp, huyền thoại, rực rỡ, nhiều lớp chi tiết, không tả thực.

## Hai mẫu
| Tên tệp | Ảnh tham chiếu (mở bằng `view_image`) | Hình |
|---|---|---|
| `S/foe-boss-rend-claw.v1-try1.png` | dáng: `A/kings/thiet-boi-lang-vuong.png`; độ hoàn thiện và ánh sáng: `S/blood-crescent-sym.v1-try1.png` | **Vồ Xé** ở khung đỉnh: bốn vết vuốt cong khổng lồ bằng ánh sáng đỏ tươi, mép trắng nóng, quét chéo qua một vùng hình nón mở về phía trước. Ở gốc nón là bóng mờ của một bàn vuốt sói bọc thép xám (năng lượng trong suốt, không phải con vật thật). Tia lửa thép xám và đỏ, mảnh đá văng, khói mực đen cuộn theo mép vết. |
| `S/foe-boss-entrance-wolf-head.v1-try1.png` | dáng: `A/kings/thiet-boi-lang-vuong-front.png` (nếu không có thì `A/kings/thiet-boi-lang-vuong.png`); độ hoàn thiện: `S/blood-comet.v1-try1.png` | **Thú Vương xuất hiện**: đầu sói vua khổng lồ bằng khói mực đen và năng lượng đỏ thẫm, trong suốt, nhìn thẳng xuống từ trên cao, mắt đỏ tươi rực, bờm như tấm giáp thép xám có vân, hàm hé lộ ánh đỏ bên trong. Quanh đầu là vòng xoáy năng lượng đỏ đen và tia lửa đỏ; phía dưới tan dần thành khói. |

## Cách làm mỗi ảnh
1. Mở các ảnh tham chiếu bằng `view_image`. Lấy dáng sói vua từ ảnh trong `kings/`, và độ hoàn thiện, ánh sáng, độ trong suốt từ ảnh trong `S/`. **Không lấy màu** của ảnh `S/`: màu theo bảng nguy hiểm ở trên.
2. Gọi `image_gen`, khổ ngang 16:9. Prompt:
   ```text
   A premium Chinese donghua xianxia game VFX still: <SUBJECT>. The beast is made of translucent energy and ink smoke, mythic and menacing, not a realistic animal. Danger palette only: vivid scarlet red (#FF4A4A), deep crimson, ink black and cold steel grey; no orange, no gold, no purple. Radiant core light, crisp bright edges, layered glints, sparks and soft halos; anime-mythic, not realistic. Seen from a high three-quarter game camera about 55 degrees down. Centred with a wide empty border, solid pure black background, no ground, no text, no letters, no watermark.
   ```
   `<SUBJECT>` là câu ở cột "Hình", dịch sang tiếng Anh, giữ đủ chi tiết.
3. Chép `cp -n` vào `S/` đúng tên ở bảng. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu, prompt nguyên văn, khổ thật.
4. **Tự chấm** (mở ảnh bằng `view_image`, thang 0–10), ghi theo mặt yếu nhất:
   - đọc ra ngay là đòn gì hoặc ai;
   - cuốn hút, uy lực, sang trọng ngang game thương mại;
   - đúng bảng màu nguy hiểm, nền đen thuần, không chữ;
   - dùng làm khung đầu video được: hình ở giữa, viền trống rộng, không bị cắt.

   Dưới 8 thì vẽ lại một lần (`-try2`) và chọn bản điểm cao hơn.

## Xong khi
- Có đủ 2 ảnh (cùng `.prompt.txt`), và tấm ghép `S/foe-boss-samples-sheet.jpg` đặt 2 ảnh cạnh nhau trên nền đen.
- Báo cáo có bảng: ảnh, điểm từng tiêu chí, một câu nhận xét, ghi rõ có vẽ lại không.

## Sau khi anh duyệt (không làm trong phiếu này)
Cả bộ: Thiết Bối Xung (đầu sói thép năng lượng ở mũi cú húc), gầm chuyển pha, Tru Gọi Đàn (ấn sói trên đất), Hỏa Nha bổ nhào, Nham Viên ném đá, Thiết Giáp Trư húc, Ấn trên tinh anh và Thú Vương, ba hào quang tinh anh (Cuồng, Thiết Bì, Hồi Nguyên), thú tướng Lang Đầu Đàn.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
