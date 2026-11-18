# Phiếu 331 · Tu Tiên · Ảnh 2D: 2 dấu đất nhìn thẳng từ trên + 2 ảnh gốc mới cho Cột Lôi, có tự chấm

Anh (11/11): Codex có lại hạn mức, **chỉ tập trung tạo ảnh**. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`** (4 ảnh × 1, cộng tối đa 1 lần vẽ lại cho ảnh tự chấm dưới 8). Mở tối đa 8 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/331-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Bối cảnh
- Các ảnh này là **khung đầu cho video Firefly**, rồi thành thẻ dán phẳng trên mặt đất trong game (dấu đất) hoặc lớp tia sét. Thẻ dán phẳng phải được vẽ **nhìn thẳng từ trên xuống** (hình tròn thật, không phải elip), vì engine tự nghiêng nó theo camera.
- Mẫu đã đạt về góc nhìn và lề: `S/light-ground-mark-top.v1-try2.png`, `S/dark-ground-mark-top.v1-try2.png` (xem 1 trong 2 để biết chuẩn).
- Phong cách: donghua tiên hiệp, rực rỡ, nhiều lớp chi tiết, lõi sáng mảnh, thân màu trong suốt, không tả thực.
- Bảng màu nguy hiểm của quái: đỏ tươi `#FF4A4A`, đỏ thẫm, đen mực. Không cam, không vàng, không tím.
- Luật anh giao cho sét (07/11): chỉ là **tia sét đánh xuống**, phân nhánh, **không có vỏ trụ hay ống sáng** bao quanh; uy lực là **nhiều tia** trên vùng rộng; mặt đất **nứt và cháy đen thật** (đá cháy than, khe nứt còn rực rồi nguội), **không** là một vết màu tím phẳng.

## Bốn ảnh
| Tên tệp | Tham chiếu (`view_image`) | Hình (dịch đủ sang tiếng Anh trong prompt) | Khổ |
|---|---|---|---|
| `S/foe-boss-summon-sigil-top.v1-try1.png` | `S/foe-boss-summon-sigil.v1-try2.png` (giữ thiết kế, đổi góc nhìn) | Ấn triệu hồi của Thú Vương: các vòng rune đồng tâm và huy hiệu đầu sói ở giữa, nét đỏ tươi rực, nền ấn đen mực, tàn tro đỏ. **Nhìn thẳng từ trên, tròn đều.** | 1:1 |
| `S/foe-commander-howl-ring-top.v1-try1.png` | `S/foe-commander-howl-ring.v1-try1.png` (giữ thiết kế, đổi góc nhìn) | Vòng sóng hú của sói tướng: các vòng đỏ đồng tâm lan trên mặt đất, mép rách như khói mực, tia lửa đỏ. **Nhìn thẳng từ trên, tròn đều.** | 1:1 |
| `S/thunder-scorch-crack-top.v1-try1.png` | `S/dark-ground-mark-top.v1-try2.png` (chỉ lấy độ hoàn thiện và góc nhìn, **không lấy màu**); `S/thunder-crack-star.v1-try1.png` (màu sét) | Dấu sét đánh trên đất: đá nứt toác hình sao không đều, cháy than đen, khe nứt còn rực trắng xanh điện và tím nhạt ở đáy khe, vài tia điện nhỏ còn nhảy giữa các mảnh đá, khói mỏng. Phải đọc ra là **đất bị sét đánh nứt và cháy**, không phải vòng phép hay vết màu. **Nhìn thẳng từ trên.** | 1:1 |
| `S/thunder-bolt-barrage.v1-try1.png` | `S/pillar-thunder-field.v1-try1.jpg` (màu và năng lượng; **bỏ hẳn vỏ trụ, ống sáng**); `S/ult-thunder-nine-heavens-v2.v1-try3.png` (độ hoàn thiện) | Loạt sét giáng: 5–7 tia sét dày, phân nhánh, đánh thẳng từ mép trên khung xuống một vùng rộng ở dưới, tia giữa to nhất, lõi trắng nóng, thân xanh điện và tím, nhánh nhỏ toả ra, tia lửa điện và quầng sáng mảnh ở điểm chạm. Không có cột, trụ, ống, vòng tròn hay mặt đất. Nhìn ngang (thẻ dựng đứng). | 9:16 dọc |

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`. Khối chung đặt sau câu tả hình:
   - Ba ảnh dấu đất: `Seen straight from above, orthographic top-down, no perspective, a perfect circle not an ellipse, centred, the whole effect inside wide pure black margins (at least 10 % empty on every side), uniform pure black background, no characters, no text, no watermark. Premium Chinese donghua xianxia game VFX source layer, rich layered detail, thin bright cores with coloured translucent bodies, glints, fine motes and soft halos.`
   - Ảnh loạt sét: `Side view, locked camera, the bolts fill the height of the frame with empty pure black margins left and right (at least 10 %), uniform pure black background, no ground, no sky, no clouds, no cylinder, no tube, no pillar shell, no characters, no text, no watermark. Premium Chinese donghua xianxia game VFX source layer, thin white-hot cores, electric blue and violet bodies, layered glints and sparks.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; lề trống mỗi cạnh ≥ 6 % (dấu đất). Lề thiếu thì đệm viền đen bằng `magick -extent` vào file mới `-pad.png`, không sửa file gốc.
5. **Tự chấm** 0–10 (mở ảnh bằng `view_image`), ghi theo mặt yếu nhất: đọc ra ngay là gì; cuốn hút, sang, ngang game thương mại; đúng góc nhìn và bảng màu, nền đen, không chữ; dùng làm khung đầu video được (ở giữa, lề rộng, không bị cắt). Dưới 8: vẽ lại một lần (`-try2`), chọn bản cao hơn.

## Xong khi
- Đủ 4 ảnh cùng `.prompt.txt`, và tấm ghép `S/top-down-331-sheet.jpg` (4 ảnh trên nền đen, có tên).
- Báo cáo có bảng: ảnh, điểm từng tiêu chí, lề đo được, một câu nhận xét, có vẽ lại không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
