# Phiếu 355 · Tu Tiên · Ảnh 2D: bộ Lôi D65 vòng 2 (giữ kiểu, tăng lực và cỡ)

Vòng 1 (phiếu 353) đúng bảng màu trắng ngà và vàng nhạt, đúng kiểu nét mực nhiều nhánh, nhưng **yếu**: đòn kết chỉ chiếm khoảng 40 % chiều cao khung (lề 21–30 %), tia mảnh và mờ, lõi chưa trắng nóng, nhìn như sét xa; lớp mây mực chỉ là vệt khói mờ. Vòng 2 giữ kiểu và màu, sửa lực. Chỉ vẽ ảnh, không sửa mã. Chạy sau phiếu 354.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 12 lần gọi `image_gen`** (9 ảnh + 3 vẽ lại; ấn tay và vành sốc v3 giữ, không vẽ lại). `view_image` tối đa 14. Báo cáo: `docs/codex-queue/355-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/*.v4-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
Bản v3 cùng tên (màu và kiểu nét: **giữ**), và `S/thunder-five-strike.v2-try9.png` chỉ để lấy **cỡ trong khung và độ mạnh của lõi** (không lấy màu xanh, không lấy ống plasma).

## Sửa bắt buộc so với v3
1. **Cỡ:** tia và đòn kết **chiếm 80–90 % chiều cao khung**, lề mỗi cạnh 6–10 % (không hơn 12 %). Tia đơn: đỉnh sát mép trên, chân sát mép dưới.
2. **Lực:** lõi tia **trắng nóng rõ** (`#FFFFFF` tới `#FFF6E0`) chiếm 1,5–2 lần bề rộng lõi v3; sát lõi là vàng nhạt ấm; thân chính của đòn kết dày hơn v3 khoảng 2 lần nhưng vẫn là nét bút, không ống plasma; nhánh mảnh dài **nhiều hơn** và toả rộng hơn; điểm chạm toé tia và hạt sáng mạnh.
3. **Đòn kết:** năm thân rõ, hội tụ một điểm; **dải mây mực tối dày hơn** ở mép trên (xám đen, có khối), từ đó tia giáng.
4. **Mây mực riêng** (`thunder-five-cloud-ink.v4`): dải mây giông thuỷ mặc **đậm, có khối cuộn**, xám đen tới đen, chiếm 70 % bề ngang và 40 % chiều cao khung, mờ dần hai đầu, vài tia vàng nhạt lóe trong mây; không phải vệt khói mờ.
5. Vụ nổ, tia sót: cùng luật cỡ và lực; vụ nổ có mảnh đá văng và vành sốc rõ.
6. Giữ: bảng màu D65 (không xanh, tím, cam, vàng kim sáng), kiểu nét mực nhiều nhánh, nền đen thuần, khổ như v3.

## Chín ảnh
`S/thunder-five-strike.v4-try1.png` (9:16), `S/thunder-single-bolt-{a,b,c,d}.v4-try1.png` (9:16), `S/thunder-five-impact-burst.v4-try1.png` (1:1), `S/thunder-five-lingering-arcs.v4-try1.png` (16:9), `S/thunder-five-cloud-ink.v4-try1.png` (16:9), và `S/thunder-five-shock-ring-top.v4-try1.png` chỉ khi v3 nhỏ hơn 60 % khung (nếu đủ thì bỏ qua và ghi rõ).

## Kiểm và tự chấm
Nền; **lề mỗi cạnh 6–12 %** (đo hộp bao các điểm V > 0,12); màu như phiếu 353 (xanh tím ≤ 2 %, vàng kim sáng ≤ 5 %); **độ sáng:** tỉ lệ điểm V > 0,9 trong hộp bao ≥ 4 % (lõi trắng nóng có thật). Tự chấm theo mặt yếu nhất: có lực và cỡ; đúng kiểu và màu; sang; cùng bộ; khung đầu video. Dưới 8 vẽ lại một lần.

## Xong khi
Ảnh + prompt + `S/thunder-v4-355-sheet.jpg` (v4 trên, v3 dưới, có nhãn) + báo cáo có bảng số.
