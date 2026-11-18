# Phiếu 353 · Tu Tiên · Ảnh 2D: bộ Lôi vẽ lại theo D65 (bạch kim lôi, kiểu thuỷ mặc), 10 ảnh

Anh (12/11 10:5x): bộ sét hiện tại sai ở **cách vẽ** (ống plasma dày, phủ xanh đặc) và **phối màu** (xanh điện bão hoà). Anh muốn kiểu tranh thuỷ mặc "thiên kiếp": tia sét **trắng ngà có quầng vàng kim nhạt**, mảnh, dài, phân nhánh rất nhiều, như nét bút, trên nền mây mực tối; "phối giữa lôi trắng và hoàng kim, nhìn rất đẹp và sang". Canon D65. Chỉ vẽ ảnh, không sửa mã. **Không dùng ảnh ngoài repo**; tranh tham khảo của anh chỉ được tả bằng lời ở trên.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 13 lần gọi `image_gen`** (10 ảnh + 3 vẽ lại). `view_image` tối đa 16. Báo cáo: `docs/codex-queue/353-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/*.v3-try*.png` theo tên dưới, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`, chỉ lấy bố cục và góc nhìn, **không lấy màu, không lấy kiểu thân dày**)
`S/thunder-five-strike.v2-try9.png`, `S/thunder-single-bolt-a.v2-try1.png`, `S/thunder-five-impact-burst.v2-try9.png`, `S/thunder-five-shock-ring-top.v2-try1.png`, `S/thunder-five-lingering-arcs.v2-try1.png`, `S/thunder-five-caster-seal.v2-try9.png`.

## Kiểu và màu chung (bắt buộc, đặt vào mọi prompt)
- **Màu:** lõi tia trắng ngà (`#FFF6E0`), quầng sát lõi vàng kim nhạt ít bão hoà (`#E8CC8A` tới `#D9B86A`), quầng ngoài mờ ấm rất nhẹ; **không** vàng kim sáng bão hoà (`#FFC83A`), không cam, không xanh, không tím. Tỉ lệ: lõi trắng 60 %, vàng nhạt 35 %, ấm mờ 5 %.
- **Nét:** như nét bút mực: vài thân chính độ dày vừa (không phải ống plasma), gãy khúc tự nhiên, **rất nhiều nhánh mảnh dài** toả ra, nhánh con li ti ở đầu; cạnh tia hơi khô kiểu mực chứ không mềm neon; có hạt sáng vàng nhạt thưa quanh tia.
- **Nền:** đen thuần (engine ghép), lề ≥ 10 %; nơi hình cần "mây mực" (đòn kết) thì mây là **khói mực xám đen mờ**, thấp, không chiếm lề.
- Phong cách: tranh thuỷ mặc tiên hiệp cao cấp, sang, tinh tế, lấp lánh nhẹ; không chữ.

## Mười ảnh
| Tên | Hình | Khổ |
|---|---|---|
| `S/thunder-five-strike.v3-try1.png` | Đòn kết: từ một dải **mây mực tối** mỏng ở mép trên, năm tia bạch kim giáng hội tụ một điểm dưới, tia giữa to nhất; nhánh mảnh toả dày; điểm chạm toé tia nhỏ | 9:16 dọc |
| `S/thunder-single-bolt-a.v3-try1.png` | Một tia chính dày vừa, gãy 4–5 khúc, ít nhánh | 9:16 |
| `S/thunder-single-bolt-b.v3-try1.png` | Một tia chẻ đôi nửa dưới, nhánh rễ dày | 9:16 |
| `S/thunder-single-bolt-c.v3-try1.png` | Một tia xiên nhẹ, ba nhánh phụ dài | 9:16 |
| `S/thunder-single-bolt-d.v3-try1.png` | Một tia mảnh zíc zắc nhanh, hai tia vệ tinh | 9:16 |
| `S/thunder-five-impact-burst.v3-try1.png` | Vụ nổ tại điểm giáng: lõi trắng ngà, năm nhánh toé ngang và chéo, mảnh đá văng, vành sốc mảnh vàng nhạt | 1:1, nhìn ngang |
| `S/thunder-five-shock-ring-top.v3-try1.png` | Vành sốc trên đất: vòng mảnh trắng ngà, tia rễ vàng nhạt toả, tâm trống | 1:1, nhìn từ trên |
| `S/thunder-five-lingering-arcs.v3-try1.png` | Tia sót: vài cung điện mảnh vàng nhạt nhảy thấp, khói mực mỏng | 16:9 |
| `S/thunder-five-caster-seal.v3-try1.png` | Ấn lôi ở tay: vòng ấn nhỏ với năm nét sét mảnh, lõi trắng ngà | 1:1 |
| `S/thunder-five-cloud-ink.v3-try1.png` | **Lớp mây mực** riêng: dải mây giông thuỷ mặc xám đen, mờ dần hai đầu, vài tia nhỏ vàng nhạt lóe trong mây (để engine đặt sau đòn kết) | 16:9 |

## Kiểm và tự chấm
Nền 4 góc đen; lề; **đo màu:** trong vùng sáng (V > 0,35) tỉ lệ điểm có sắc 190–300° (xanh, tím) ≤ 2 %; tỉ lệ vàng kim sáng (sắc 45–60°, S > 0,8, V > 0,85) ≤ 5 %; ghi số. Tự chấm theo mặt yếu nhất: đúng kiểu nét mực mảnh nhiều nhánh (không ống plasma); đúng bảng trắng ngà và vàng nhạt; sang, cuốn hút; cùng bộ 10 ảnh; dùng làm khung đầu video được. Dưới 8 vẽ lại một lần.

## Xong khi
10 ảnh + prompt + `S/thunder-v3-353-sheet.jpg` (10 ảnh có nhãn, kèm cột so với bản v2 cho đòn kết và tia A) + báo cáo có bảng số.
