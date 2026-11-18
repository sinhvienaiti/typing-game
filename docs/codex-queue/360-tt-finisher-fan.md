# Phiếu 360 · Tu Tiên · Ảnh 2D: đòn kết Ngũ Lôi vẽ lại (năm tia toả quạt xuống năm điểm) + khung thu năng lượng, bộ bạch kim D65

Hai giám khảo mù (v16: 7,0/7,0; v19: 7,2/6,7) đều nói đòn kết "không đọc được năm thân tia và năm điểm chạm" và "thiếu nhịp thu năng lượng trước đòn cuối". Ghép từ tia đơn không giải quyết được, nên vẽ lại đòn kết từ nguồn. Chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần gọi `image_gen`** (2 ảnh + 4 vẽ lại). `view_image` tối đa 8. Báo cáo: `docs/codex-queue/360-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-five-fan.v1-try*.png`, `S/thunder-five-gather.v1-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
`S/thunder-five-strike.v4-try1.png` (màu, kiểu nét mực; **không lấy bố cục hội tụ**), `S/thunder-five-cloud-ink.v4-try2.png` (mây mực), `S/thunder-array-silver-a.v1-try2.png` (trận bạc ở dưới, chỉ để biết).

## Hai ảnh
| Tên | Hình | Khổ |
|---|---|---|
| `S/thunder-five-fan.v1-try1.png` | **Đòn kết:** nhìn ngang hơi từ trên (camera 30° từ trên), một dải mây mực tối ở mép trên; **năm tia sét bạch kim toả hình quạt**, mỗi tia giáng xuống **một điểm chạm riêng** trên một đường ngang, năm điểm cách đều, tia giữa dày nhất, hai tia ngoài xiên rõ; **giữa các tia có khoảng tối rõ**, không chồng; mỗi điểm chạm có vụ nổ nhỏ riêng và mảnh đá; lõi trắng nóng, quầng vàng nhạt mỏng, nhiều nhánh mảnh. Nền đen, không đất. | 16:9 ngang |
| `S/thunder-five-gather.v1-try1.png` | **Thu năng lượng (0,4 s trước đòn kết):** nhìn ngang hơi từ trên; từ năm điểm trên mặt đất, **năm luồng sáng mảnh vàng nhạt bị hút lên trời** tụ vào một điểm sáng trong dải mây mực ở mép trên, các hạt sáng bay lên theo luồng, mây bắt đầu rực ở tâm; không có tia giáng. Nền đen. | 16:9 ngang |
Chung: bạch kim D65 (trắng ngà, vàng nhạt, mây mực xám đen), kiểu nét mực, không xanh tím cam, không vàng kim sáng, lề ≥ 8 %, không chữ. Đọc được ở cỡ nhỏ: **đếm được 5 tia và 5 điểm chạm khi thu ảnh xuống cao 120 px** (tự thu nhỏ rồi mở xem).

## Kiểm và tự chấm
Nền, lề, màu như phiếu 353; **ô 120 px**: đếm tia và điểm chạm (phải 5 và 5). Tự chấm theo mặt yếu nhất: đếm được 5 tia và 5 điểm ở 120 px; có khoảng tối giữa tia; cùng bộ bạch kim; lực; khung đầu video. Dưới 8 vẽ lại.

## Xong khi
2 ảnh + prompt + `S/thunder-fan-360-sheet.jpg` (2 ảnh + ô 120 px) + báo cáo.
