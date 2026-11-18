# Phiếu 336 · Tu Tiên · Ảnh 2D: 4 tia sét đơn khác hình cho Ngũ Lôi Oanh Đỉnh (để engine bắn dồn dập), có tự chấm

Anh (11/11): chọn hướng **Ngũ Lôi Oanh Đỉnh** cho Cột Lôi; ảnh do Codex phụ trách. Phiếu này chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 8 lần gọi `image_gen`** (4 ảnh × 1, cộng tối đa 1 lần vẽ lại cho ảnh tự chấm dưới 8). Mở tối đa 10 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/336-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`), đúng tên ở dưới, và báo cáo. **Cấm:** mọi lệnh git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo làm tham chiếu; sửa mã.

## Bối cảnh
- Ảnh gốc anh đã chọn: `S/thunder-five-strike.v1-try1.png` (xoáy mây kiếp ở trên, năm tia sét thân dày, gãy khúc, cùng giáng vào một điểm). **Mọi ảnh trong phiếu phải cùng bảng màu, cùng kiểu tia sét và cùng độ hoàn thiện với ảnh này.**
- Dấu đất đã có: `S/thunder-scorch-crack-top.v1-try1.png` (đất nứt cháy, nhìn từ trên).
- Các ảnh là **khung đầu cho video Firefly**, mỗi ảnh một pha của chiêu: tụ lực, phóng, đường bay đã có (ảnh gốc), chạm, dư âm.
- Luật anh giao cho sét (07/11): chỉ là **tia sét đánh xuống**, thân dày, gãy khúc, phân nhánh; **không có vỏ trụ, ống sáng hay cột trơn**; uy lực là nhiều tia. Bảng màu: trắng nóng, xanh điện, tím; không cam, không vàng.
- Phong cách: donghua tiên hiệp, rực rỡ, sang, nhiều lớp, lõi trắng mảnh, thân màu trong suốt, lấp lánh, hạt sáng mịn, quầng mềm.

## Vì sao (anh, 11/11 21:1x)
"hiệu ứng vfx đẹp khi có nhiều hiệu ứng chồng lên nhau… ngũ lôi thì phải dồn dập nhiều tia sét đánh lực mạnh mẽ". Một video năm tia không đủ. Engine sẽ bắn **nhiều tia đơn** lệch nhịp trong 3–5 giây, nên cần các tia đơn **khác hình nhau** để không lặp.

## Bốn ảnh
Tham chiếu của cả bốn: `S/thunder-five-strike.v1-try1.png` (lấy đúng kiểu thân tia, màu, độ hoàn thiện; **chỉ vẽ một tia**, không vẽ mây).
| Tên tệp | Hình (dịch đủ sang tiếng Anh trong prompt) |
|---|---|
| `S/thunder-single-bolt-a.v1-try1.png` | Một tia sét chính thân rất dày, gãy khúc mạnh 4–5 đoạn, đánh thẳng từ mép trên xuống gần mép dưới, ít nhánh, lõi trắng nóng, viền xanh điện, quầng tím |
| `S/thunder-single-bolt-b.v1-try1.png` | Một tia sét chẻ đôi ở nửa dưới thành hai ngọn cùng giáng xuống, nhiều nhánh nhỏ toả hai bên như rễ cây |
| `S/thunder-single-bolt-c.v1-try1.png` | Một tia sét xiên nhẹ từ góc trên trái xuống giữa dưới, thân dày vừa, có ba nhánh phụ dài, tia lửa điện dọc thân |
| `S/thunder-single-bolt-d.v1-try1.png` | Một tia sét mảnh, rất sáng, zíc zắc gấp khúc nhanh, kèm hai tia vệ tinh mảnh hơn chạy song song không đều (dùng cho các nhát phụ dồn dập) |

Cả bốn: khổ **9:16 dọc**, nhìn ngang, tia chiếm chiều cao khung, đầu dưới kết thúc bằng một điểm chạm sáng nhỏ (không có mặt đất).

## Cách làm mỗi ảnh
1. Mở ảnh tham chiếu bằng `view_image`.
2. Gọi `image_gen`. Khối chung đặt sau câu tả hình:
   `Side view, locked camera, a single lightning bolt filling the height of the frame, empty pure black margins left and right (at least 15 %), uniform pure black background, no clouds, no ground, no sky, no cylinder, no tube, no smooth pillar, no characters, no text, no watermark. Palette: white-hot core, electric blue and violet body only, no orange, no gold. Premium Chinese donghua xianxia game VFX source layer, thick jagged lightning, layered glints, sparks, fine motes and a soft halo.`
3. Chép `cp -n` vào `S/` đúng tên. Ghi `.prompt.txt` cùng tên: công cụ, ảnh tham chiếu (đường dẫn), prompt nguyên văn, khổ thật.
4. Kiểm bằng `magick`: nền 4 góc gần đen thuần; lề trái phải ≥ 6 %. Thiếu thì đệm bằng `magick -extent` vào file mới `-pad.png`.
5. **Tự chấm** 0–10 theo mặt yếu nhất: đọc ra ngay là một tia sét mạnh; cùng bộ với ảnh gốc; **bốn tia khác hình nhau rõ**; nền đen, không chữ; dùng làm khung đầu video được. Dưới 8: vẽ lại một lần (`-try2`).

## Xong khi
- Đủ 4 ảnh cùng `.prompt.txt`, tấm ghép `S/thunder-single-bolt-336-sheet.jpg` (4 tia cạnh nhau, có tên), và báo cáo có bảng điểm.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
