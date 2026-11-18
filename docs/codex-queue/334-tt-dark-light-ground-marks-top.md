# Phiếu 334 · Tu Tiên · Ảnh 2D: dấu đất Ám và Quang nhìn thẳng từ trên, có tự chấm

Anh (11/11 tối): "dấu đất của gemini bạn kêu codex làm luôn cho". Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần gọi `image_gen`** (2 ảnh × 1, cộng tối đa 1 lần vẽ lại cho ảnh tự chấm dưới 8). Mở tối đa 6 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/334-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Bối cảnh
- Hai ảnh này là **khung đầu cho video Firefly**, rồi thành thẻ dán phẳng trên mặt đất trong game. Phải vẽ **nhìn thẳng từ trên xuống** (hình tròn thật, không phải elip), vì engine tự nghiêng thẻ theo camera.
- Chuẩn góc nhìn, lề và độ hoàn thiện đã đạt ở phiếu 331: `S/foe-boss-summon-sigil-top.v1-try1.png` (xem để biết chuẩn).
- Phong cách: donghua tiên hiệp, rực rỡ, sang, nhiều lớp chi tiết, lõi sáng mảnh, thân màu trong suốt, có lấp lánh và hạt sáng mịn, không tả thực.

## Hai ảnh
| Tên tệp | Tham chiếu (`view_image`) | Hình (dịch đủ sang tiếng Anh trong prompt) | Khổ |
|---|---|---|---|
| `S/dark-ground-mark-top.v1-try3.png` | `S/dark-ground-mark.v1-try1.jpg` (giữ thiết kế và màu, đổi góc nhìn); `S/dark-ground-mark-top.v1-try1.png` (bản Gemini, chỉ để biết bố cục nhìn từ trên) | Dấu đất hệ Ám: giữ đúng các vòng, hoa văn và bảng màu của ảnh tham chiếu thứ nhất (tím thẫm, đen mực, viền tím sáng mảnh), khói mực cuộn ở mép, hạt sáng tím li ti. **Nhìn thẳng từ trên, tròn đều.** | 1:1 |
| `S/light-ground-mark-top.v1-try3.png` | `S/light-ground-mark.v1-try1.jpg` (giữ thiết kế và màu, đổi góc nhìn); `S/light-ground-mark-top.v1-try2.png` (bản Gemini, chỉ để biết bố cục nhìn từ trên) | Dấu đất hệ Quang: giữ đúng các vòng, hoa văn và bảng màu của ảnh tham chiếu thứ nhất (vàng kim nhạt và trắng ngà), tia sáng mảnh toả đều, hạt sáng và ánh lấp lánh. **Nhìn thẳng từ trên, tròn đều.** | 1:1 |

Nếu ảnh tham chiếu thứ nhất khác với mô tả màu ở trên thì **ảnh tham chiếu thắng**; ghi điều đó vào báo cáo.

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`. Khối chung đặt sau câu tả hình:
   `Seen straight from above, orthographic top-down, no perspective, a perfect circle not an ellipse, centred, the whole effect inside wide pure black margins (at least 10 % empty on every side), uniform pure black background, no characters, no text, no watermark. Premium Chinese donghua xianxia game VFX source layer, rich layered detail, thin bright cores with coloured translucent bodies, glints, fine motes and soft halos.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; lề trống mỗi cạnh ≥ 6 %. Lề thiếu thì đệm viền đen bằng `magick -extent` vào file mới `-pad.png`, không sửa file gốc.
5. **Tự chấm** 0–10 (mở ảnh bằng `view_image`), ghi theo mặt yếu nhất: đọc ra ngay là gì; cuốn hút, sang, ngang game thương mại; đúng góc nhìn và bảng màu, nền đen, không chữ; dùng làm khung đầu video được. Dưới 8: vẽ lại một lần (`-try4`), chọn bản cao hơn.

## Xong khi
- Đủ 2 ảnh cùng `.prompt.txt`, và tấm ghép `S/top-down-334-sheet.jpg`: mỗi hệ một hàng gồm ảnh gốc cũ, bản Gemini, bản mới, có tên.
- Báo cáo có bảng: ảnh, điểm từng tiêu chí, lề đo được, một câu nhận xét, có vẽ lại không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
