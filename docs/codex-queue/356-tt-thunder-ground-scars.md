# Phiếu 356 · Tu Tiên · Ảnh 2D: vết sét in xuống đất (nứt rực, vết cháy Lichtenberg, vết nguội), bộ bạch kim D65

Anh (12/11 12:1x) xem Ngũ Lôi v11: "vấn đề còn lại chỉ là các vết khi lôi sét đánh xuống in vào nền đất… đất có thể nứt ra vì sấm sét hoặc có thể tạo riêng vệt cho sấm sét khi đánh xuống để nó được đẹp và lực hơn". Vết hiện tại là sao nứt xanh trắng cũ bị nhuộm, nhìn như vệt kem mờ. Chỉ vẽ ảnh, không sửa mã.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần gọi `image_gen`** (3 ảnh + 3 vẽ lại). `view_image` tối đa 8. Báo cáo: `docs/codex-queue/356-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-scar-*.v1-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `S/thunder-five-impact-burst.v4-try1.png`, `S/thunder-single-bolt-a.v4-try1.png`: bảng màu bạch kim D65 (lõi trắng ngà, quầng vàng nhạt) và kiểu nét mực.
- `S/thunder-scorch-crack-top.v1-try1.png`: góc nhìn thẳng từ trên và cách bố trí một vết đất (chỉ lấy bố cục, **không lấy màu xanh**).
- `S/dark-ground-mark-top.v1-try3.png`: độ hoàn thiện mặt đá nứt.

## Ba ảnh (nhìn thẳng từ trên, 1:1, nền đen thuần, lề ≥ 10 %, không chữ; mặt đá là đá vôi xám xanh như sân)
| Tên | Hình |
|---|---|
| `S/thunder-scar-crack-hot.v1-try1.png` | **Đất nứt vì sét, lúc vừa đánh:** từ điểm chạm, 5–7 khe nứt lớn toả ra không đều như sao, kèm khe nhánh nhỏ; trong khe **rực trắng ngà và vàng kim nhạt** như đá nóng chảy; mép khe cháy đen, mảnh đá bật lên hơi hở; vài tia điện mảnh vàng nhạt còn nhảy trên mặt đá; khói mỏng. Phần đá ngoài khe nứt chỉ chiếm một đĩa mờ dần ra rìa (để dán lên sân). |
| `S/thunder-scar-lichtenberg.v1-try1.png` | **Vết sét in trên đá:** hình cây sét phân nhánh (Lichtenberg) khắc cháy vào mặt đá, nhánh rất mảnh và dài, lan từ tâm ra, nét cháy nâu đen với **lõi còn rực vàng nhạt** ở nửa trong; tâm là vết cháy tròn nhỏ; rất tinh, nhiều nhánh; đĩa mờ dần ra rìa. |
| `S/thunder-scar-cooled.v1-try1.png` | **Vết nguội:** cùng bố cục với ảnh 1 nhưng khe đã tắt: khe nứt tối, mép cháy đen, vài đốm than còn đỏ ngà rất nhỏ, tro trắng xám; để engine mờ dần từ ảnh 1 sang ảnh này. |
Chung: sang, có lực, chất tiên hiệp thuỷ mặc; không xanh, không tím, không cam rực; không vòng tròn trơn.

## Kiểm và tự chấm
Nền; lề; màu như phiếu 353 (xanh tím ≤ 2 %, vàng kim sáng ≤ 5 %); ảnh 1 và 3 cùng bố cục khe (ghi độ trùng khít ước lượng). Tự chấm theo mặt yếu nhất: đọc ra ngay là đất bị sét đánh nứt và cháy; có lực; cùng bộ bạch kim; dán được lên sân (đĩa mờ ra rìa). Dưới 8 vẽ lại một lần.

## Xong khi
3 ảnh + prompt + `S/thunder-scar-356-sheet.jpg` + báo cáo có bảng.
