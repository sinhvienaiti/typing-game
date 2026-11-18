# Phiếu 333 · Tu Tiên · Ảnh sét kiểu "Ngũ Lôi Oanh Đỉnh" và "Huyền Lôi Kích Sát" cho Cột Lôi (chỉ vẽ ảnh)

Anh (11/11 tối) chê `thunder-bolt-barrage.v1-try2-pad.png`: "vẽ như kia nhìn quá xấu", và bảo vẽ **dạng lôi giáng sét** giống chiêu **Ngũ Lôi Oanh Đỉnh (五雷轰顶)** hoặc **Huyền Lôi Kích Sát (玄雷击杀)** của tiên hiệp. Phiếu 332 đã huỷ; phiếu này thay nó.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 4 lần gọi `image_gen`** (2 phương án × 1, cộng 1 lần vẽ lại mỗi phương án nếu tự chấm dưới 8,5). Mở tối đa 6 ảnh bằng `view_image`. Báo cáo: `docs/codex-queue/333-report.md` (tiếng Việt, ngắn).

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`.
**Được ghi:** chỉ thêm file mới vào `S` (`cp -n`) và báo cáo. **Cấm:** git ghi; sửa hay xóa file có sẵn; mở cổng mạng; ảnh ngoài repo; sửa mã.

## Hình mẫu của thể loại (đã tìm hiểu; hãy dùng thêm hiểu biết của bạn về donghua tiên hiệp và cảnh độ kiếp)
- **Nguồn sét là kiếp vân:** một xoáy mây giông đen tím cuộn tròn trên đỉnh, mắt xoáy rực sáng, sét con chạy ngoằn ngoèo trong mây. Sét **từ trời giáng xuống**, không tự mọc giữa khung.
- **Thiên lôi to như thân cây / "thùng nước":** thân sét rất dày, lõi trắng loá, gãy khúc sắc cạnh hình răng cưa, không phải sợi chỉ uốn lượn. Quanh thân có sét con quấn và tia nhánh thon nhọn.
- **Ngũ lôi:** năm đạo lôi **cùng bổ xuống một điểm** trên đỉnh đầu mục tiêu (một đạo chính giữa thẳng đứng, bốn đạo nghiêng chụm vào), không đứng song song như rèm.
- **Điểm chạm nổ tung:** quầng nổ trắng tím, sét toé ngang sát đất, tia lửa điện và mảnh sáng bắn ra.
- **Huyền lôi:** sét huyền bí, tím thẫm gần đen ở viền, lõi trắng tím, nặng nề và sát khí hơn sét thường.
- Vẫn giữ luật của anh (07/11): **không vỏ trụ, ống sáng, cột trơn** bao quanh; thân sét là tia sét gãy khúc thật.

## Hai phương án (khổ dọc 9:16)
Tham chiếu nội bộ: `S/thunder-bolt-barrage.v1-try2-pad.png` (bản bị chê: chỉ giữ nền đen và họ màu), `S/ult-thunder-nine-heavens-v2.v1-try3.png` (độ hoàn thiện, mây sét), `S/thunder-crack-star.v1-try1.png` (màu sét).

| Tên tệp | Hình |
|---|---|
| `S/thunder-five-strike.v1-try1.png` | **Ngũ Lôi Oanh Đỉnh.** Trên đỉnh khung: xoáy kiếp vân đen tím, mắt xoáy rực trắng tím, sét con chạy trong mây. Từ mắt xoáy, **năm đạo thiên lôi dày** bổ xuống và **chụm vào một điểm** ở phần dưới khung: đạo giữa to nhất, thẳng, gãy khúc răng cưa; bốn đạo bên nghiêng vào, to nhỏ khác nhau. Lõi trắng loá rộng, viền xanh điện rồi tím; sét con quấn quanh thân, nhánh thon nhọn. Điểm chạm: quầng nổ trắng tím, sét toé ngang, tia lửa điện bắn tung. |
| `S/thunder-xuan-strike.v1-try1.png` | **Huyền Lôi Kích Sát.** Trên đỉnh khung: mắt xoáy kiếp vân đen tím hẹp và sâu. **Một đạo huyền lôi khổng lồ** giáng thẳng xuống: thân rất dày, gãy khúc sắc, lõi trắng tím loá, viền tím thẫm gần đen có rìa sáng mảnh; quanh nó hàng chục tia nhánh và sét con màu tím xanh toả ra rồi thon nhọn, vài cung sét quấn xoắn quanh thân. Điểm chạm: vụ nổ sáng trắng tím hình sao, sét toé ngang rộng, hạt điện và tàn sáng bay lên. |

Khối chung đặt sau câu tả hình:
`Side view, locked camera, vertical composition. The storm vortex sits inside the top of the frame; the impact burst sits above the bottom with at least 8 % empty pure black margin below it and at least 10 % on the left and right. Uniform pure black background everywhere outside the effect: no ground, no landscape, no mountains, no characters, no text, no watermark. The lightning trunks are jagged angular bolts, never a smooth cylinder, tube, beam or pillar shell. Premium Chinese donghua xianxia game VFX source layer, heavenly tribulation thunder, overwhelming power, wide white-hot cores, electric blue and violet bodies, deep violet-black storm cloud, layered glints, sparks, fine motes and thin soft halos.`

## Cách làm
1. `view_image` tham chiếu, gọi `image_gen` 9:16, `cp -n` vào `S/` đúng tên, ghi `.prompt.txt` (công cụ, tham chiếu, prompt nguyên văn, khổ thật).
2. Đo lề bằng `magick` (ngưỡng max(R,G,B) > 3/255). Thiếu lề thì tạo bản `-pad.png` bằng `-extent`, không sửa gốc.
3. Tự chấm 0–10 theo mặt yếu nhất: đọc ra ngay là thiên lôi giáng từ kiếp vân; uy lực, cuốn hút ngang donghua và game thương mại; thân sét dày, gãy khúc, không thành trụ trơn hay rèm song song; nền đen, không chữ; dùng làm khung đầu video được. Dưới 8,5: vẽ lại một lần (`-try2`).
4. Tấm ghép `S/thunder-strike-333-sheet.jpg`: bản bị chê bên trái, hai phương án bên phải, có tên.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
