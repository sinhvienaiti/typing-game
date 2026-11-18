# Phiếu 335 · Tu Tiên · Ảnh 2D: bộ 5 pha cho Ngũ Lôi Oanh Đỉnh, có tự chấm

Anh (11/11): chọn hướng **Ngũ Lôi Oanh Đỉnh** cho Cột Lôi; ảnh do Codex phụ trách. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 10 lần gọi `image_gen`** (5 ảnh × 1, cộng tối đa 1 lần vẽ lại cho ảnh tự chấm dưới 8). Mở tối đa 10 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/335-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Bối cảnh
- Ảnh gốc anh đã chọn: `S/thunder-five-strike.v1-try1.png` (xoáy mây kiếp ở trên, năm tia sét thân dày, gãy khúc, cùng giáng vào một điểm). **Mọi ảnh trong phiếu phải cùng bảng màu, cùng kiểu tia sét và cùng độ hoàn thiện với ảnh này.**
- Dấu đất đã có: `S/thunder-scorch-crack-top.v1-try1.png` (đất nứt cháy, nhìn từ trên).
- Các ảnh là **khung đầu cho video Firefly**, mỗi ảnh một pha của chiêu: tụ lực, phóng, đường bay đã có (ảnh gốc), chạm, dư âm.
- Luật anh giao cho sét (07/11): chỉ là **tia sét đánh xuống**, thân dày, gãy khúc, phân nhánh; **không có vỏ trụ, ống sáng hay cột trơn**; uy lực là nhiều tia. Bảng màu: trắng nóng, xanh điện, tím; không cam, không vàng.
- Phong cách: donghua tiên hiệp, rực rỡ, sang, nhiều lớp, lõi trắng mảnh, thân màu trong suốt, lấp lánh, hạt sáng mịn, quầng mềm.

## Năm ảnh
Tham chiếu của cả năm: `S/thunder-five-strike.v1-try1.png` (mở trước mỗi ảnh). Ảnh 4 thêm `S/thunder-scorch-crack-top.v1-try1.png`.
| Tên tệp | Pha | Hình (dịch đủ sang tiếng Anh trong prompt) | Góc, khổ |
|---|---|---|---|
| `S/thunder-five-cloud-vortex-top.v1-try1.png` | Tụ lực | Xoáy mây kiếp: đĩa mây giông xoáy tròn, tâm rỗng sáng trắng xanh, năm mầm sét đang tụ ở vành trong, tia điện nhỏ chạy trong mây | Nhìn thẳng từ trên (thẻ phẳng trên trời), 1:1 |
| `S/thunder-five-caster-seal.v1-try1.png` | Phóng (ở người thi triển) | Ấn lôi ở tay: vòng ấn sét nhỏ gồm năm ký hiệu sét quanh một lõi trắng, tia điện bắn ra ngắn, hạt sáng; không có bàn tay hay nhân vật | Nhìn thẳng, 1:1 |
| `S/thunder-five-impact-burst.v1-try1.png` | Chạm | Vụ nổ sét tại điểm giáng: lõi trắng nóng, năm nhánh sét toé ngang và chéo lên, mảnh đá cháy văng, vành sốc mảnh, tia lửa điện | Nhìn ngang (thẻ dựng đứng), 1:1 |
| `S/thunder-five-shock-ring-top.v1-try1.png` | Chạm (mặt đất) | Vành sốc sét lan trên đất: vòng điện xanh trắng mảnh với các tia sét nhỏ chạy toả ra như rễ, bụi cháy, tâm trống (để dấu nứt cháy nằm dưới) | Nhìn thẳng từ trên, 1:1 |
| `S/thunder-five-lingering-arcs.v1-try1.png` | Dư âm | Tia điện còn sót: vài cung điện mảnh nhảy giữa các điểm gần mặt đất, khói mỏng xám xanh bốc lên, hạt sáng nguội dần | Nhìn ngang, 16:9 |

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`. Khối chung đặt sau câu tả hình:
   - Ảnh nhìn từ trên: `Seen straight from above, orthographic top-down, no perspective, a perfect circle not an ellipse, centred, the whole effect inside wide pure black margins (at least 10 % empty on every side), uniform pure black background, no characters, no text, no watermark.`
   - Ảnh nhìn ngang hoặc nhìn thẳng: `Locked camera, centred, the whole effect inside wide pure black margins (at least 10 % empty on every side), uniform pure black background, no ground plane, no sky, no cylinder, no tube, no smooth pillar, no characters, no hands, no text, no watermark.`
   - Cả hai thêm: `Palette: white-hot cores, electric blue and violet bodies only, no orange, no gold. Premium Chinese donghua xianxia game VFX source layer, thick jagged lightning, rich layered detail, glints, fine motes and soft halos.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; lề trống mỗi cạnh ≥ 6 %. Lề thiếu thì đệm viền đen bằng `magick -extent` vào file mới `-pad.png`, không sửa file gốc.
5. **Tự chấm** 0–10 (mở ảnh bằng `view_image`), ghi theo mặt yếu nhất: đọc ra ngay là gì; cuốn hút, sang, ngang game thương mại; cùng bộ với ảnh gốc (màu, kiểu tia); đúng góc nhìn, nền đen, không chữ; dùng làm khung đầu video được. Dưới 8: vẽ lại một lần (`-try2`), chọn bản cao hơn.

## Xong khi
- Đủ 5 ảnh cùng `.prompt.txt`, và tấm ghép `S/thunder-five-335-sheet.jpg` (ảnh gốc + 5 ảnh mới, nền đen, có tên pha).
- Báo cáo có bảng: ảnh, điểm từng tiêu chí, lề đo được, một câu nhận xét, có vẽ lại không.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
