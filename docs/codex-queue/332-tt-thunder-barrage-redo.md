# Phiếu 332 · Tu Tiên · Vẽ lại ảnh "loạt sét giáng" cho Cột Lôi (chỉ vẽ ảnh)

Anh (11/11 tối) xem `thunder-bolt-barrage.v1-try2-pad.png` của phiếu 331 và bảo **vẽ lại**. Điểm yếu: 5 tia mảnh, gần giống nhau, đứng song song như rèm; nhánh ngoài cụt; lề dưới hẹp; chưa đủ uy lực.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần gọi `image_gen`** (2 phương án × 1, cộng 1 lần vẽ lại mỗi phương án nếu tự chấm dưới 8,5). Mở tối đa 6 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/332-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`) và báo cáo. **Cấm:** git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo; sửa mã.

## Luật hình của anh (07/11)
Sét là **tia đánh xuống**, phân nhánh, **không vỏ trụ, ống sáng, cột**; uy lực là **nhiều tia cộng dồn trên vùng rộng**.

## Hai phương án (khổ dọc 9:16)
Tham chiếu: `S/thunder-bolt-barrage.v1-try2-pad.png` (bản bị chê: giữ màu và nền, sửa bố cục), `S/ult-thunder-nine-heavens-v2.v1-try3.png` (độ hoàn thiện), `S/thunder-crack-star.v1-try1.png` (màu sét).

| Tên tệp | Hình |
|---|---|
| `S/thunder-bolt-barrage-b.v1-try1.png` | **Một tia chúa cực dày** ở giữa (lõi trắng nóng rộng, viền xanh điện rồi tím), ngoằn ngoèo mạnh, quanh nó 6–8 tia phụ **to nhỏ khác nhau, nghiêng nhẹ khác hướng, xa gần khác nhau** (tia xa mờ và mảnh hơn), nhiều nhánh con **thon dần tới đầu nhọn**. Các tia hội về một vùng chạm rộng ở dưới, nơi có chùm tia lửa điện bắn toé và quầng sáng mảnh. |
| `S/thunder-bolt-barrage-c.v1-try1.png` | **Cơn mưa sét**: 9–12 tia đánh xuống **lệch pha** (vài tia đã chạm đất sáng rực, vài tia mới tới giữa khung, vài tia chỉ là vệt dư ảnh mờ), độ dày rất khác nhau, toả rộng như hình quạt từ trên xuống, nhánh con thon nhọn, hạt điện li ti và tia lửa lơ lửng giữa các tia. |

Khối chung đặt sau câu tả hình:
`Side view, locked camera. The bolts enter from the top edge and end above the bottom with at least 10 % empty pure black margin at the bottom and at least 12 % on the left and right. Every branch tapers to a fine point; no branch ends abruptly. Uniform pure black background, no ground, no sky, no clouds, no cylinder, no tube, no pillar shell, no ring, no characters, no text, no watermark. Premium Chinese donghua xianxia game VFX source layer, overwhelming power, wide white-hot cores, electric blue and violet bodies, layered glints, sparks and soft thin halos.`

## Cách làm
1. `view_image` các tham chiếu, gọi `image_gen` 9:16, `cp -n` vào `S/` đúng tên, ghi `.prompt.txt` (công cụ, tham chiếu, prompt nguyên văn, khổ thật).
2. Đo lề bằng `magick` (ngưỡng max(R,G,B) > 3/255). Thiếu lề thì tạo bản `-pad.png` bằng `-extent`, không sửa gốc.
3. Tự chấm 0–10 theo mặt yếu nhất: uy lực và cuốn hút ngang game thương mại; các tia khác nhau rõ về cỡ, hướng, độ sâu; nhánh thon nhọn; đúng luật (không trụ, nền đen, không chữ); làm khung đầu video được. Dưới 8,5: vẽ lại một lần (`-try2`).
4. Tấm ghép `S/thunder-barrage-332-sheet.jpg`: bản bị chê bên trái, hai phương án bên phải, có tên.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
