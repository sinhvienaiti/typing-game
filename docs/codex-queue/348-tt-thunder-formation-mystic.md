# Phiếu 348 · Tu Tiên · Ảnh 2D: trận pháp lôi huyền bí (vẽ lại theo D64), 2 phương án + lớp vành rời

Anh (12/11 09:2x) chê hai phương án của phiếu 345 là "hình vẽ cơ bản": "trận pháp nên kiểu nhìn huyền bí, chi tiết của trận pháp nên cho cảm giác tu tiên hơn, với các ngữ văn cổ hoặc các dạng hình hoặc hiệu ứng nhìn cho cảm giác thần thoại hơn". Canon D64. Chỉ vẽ ảnh, không sửa mã. Chạy sau phiếu 347.

**Model `gpt-6.1-sol`, mức `high`. Tối đa 6 lần gọi `image_gen`** (2 phương án + 1 lớp vành rời, tối đa 3 vẽ lại). `view_image` tối đa 8. Báo cáo: `docs/codex-queue/348-report.md`.

## Đường dẫn
`S = games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/stills/skills`. Chỉ thêm `S/thunder-array-*.v1-try*.png`, `.prompt.txt`, tấm ghép. Cấm git ghi, sửa file có sẵn, mở cổng, ảnh ngoài repo, sửa mã.

## Tham chiếu (`view_image`)
- `S/thunder-formation-top.v1-try2-black.png`: chỉ lấy góc nhìn thẳng từ trên; **bố cục và màu bị chê, không lặp lại**.
- `S/foe-boss-summon-sigil-top.v1-try1.png`: mức dày đặc của vành rune và cách lồng vòng (chỉ lấy mật độ, không lấy màu đỏ).
- `S/light-ground-mark-top.v1-try3.png`: độ hoàn thiện, nét khắc phát sáng.

## Màu (anh, 12/11 09:3x: "đang hướng về lôi đình màu xanh quá, nên đổi màu trận pháp để nó nhìn khác với sấm sét cho đẹp hơn")
Trận pháp **không dùng trắng xanh** của tia sét. Phương án A: **đồng cổ và hổ phách** (nét khắc như đồng thau cũ phát sáng ấm, lõi hổ phách, viền tối nâu đen), là màu vàng cũ đã dịu, **không phải vàng kim sáng** `#FFC83A` (màu tiền), không cam `#FFB020`. Phương án B: **tử lôi** (tím thẫm và bạc, lõi trắng bạc). Vành rời theo màu của phương án tự chấm cao hơn. Khi sét trắng xanh giáng xuống, trận phải nổi lên tương phản.

## Hình chung (nhìn thẳng từ trên, tròn hoàn hảo, phẳng, nền đen, lề ≥ 10 %, 1:1, không chữ thật)
Trận pháp lôi tu tiên **nhiều vòng lồng nhau**, nét như khắc trên đồng cổ (A) hoặc ngọc đen (B) phát sáng, tia điện mảnh cùng màu trận chạy theo rãnh khắc, hạt sáng li ti, quầng mềm. Bắt buộc có: (1) **vành ngoài là một dải chữ triện cổ** chạy quanh (ký hiệu trừu tượng gợi cổ văn, nét vuông gãy, không phải chữ Hán hay chữ Latinh thật); (2) một vành **lôi văn** (hoa văn sét cuộn kiểu đồ đồng cổ); (3) một vòng **cánh sen hoặc mây cuộn**; (4) **năm nút sét** ở vòng trong, nối nhau bằng cung chứ không bằng đường thẳng tạo sao; (5) **tâm** là lõi sáng nhỏ với một ấn sét trừu tượng, phần lớn tâm vẫn thoáng để tia giáng đọc rõ. Cảm giác thần thoại, cổ xưa, huyền bí; không giống bùa phương Tây, không hình học trơn.

## Ba ảnh
| Tên | Khác nhau |
|---|---|
| `S/thunder-array-a.v1-try1.png` | Bố cục **bát quái**: tám quẻ cách điệu quanh vòng giữa, chữ triện ngoài cùng, năm nút sét trong |
| `S/thunder-array-b.v1-try1.png` | Bố cục **sao chòm và long văn**: vành ngoài là bản đồ sao cổ (điểm sao nối cung), vòng giữa hai rồng sét uốn đuổi nhau, năm nút sét trong |
| `S/thunder-array-ring.v1-try1.png` | **Chỉ vành chữ triện ngoài cùng** (theo phương án tự chấm cao hơn), tâm hoàn toàn đen trong suốt, để engine quay riêng ngược chiều |

## Kiểm và tự chấm
Nền, lề, tròn (sai lệch bán kính ≤ 2 %), đo và ghi tỉ lệ vàng kim sáng (sắc 45–60°, độ bão hoà > 0,8, độ sáng > 0,85) ≤ 5 % vùng sáng ở A; vành rời có tâm đen thuần ≥ 55 % đường kính. Tự chấm theo mặt yếu nhất: huyền bí và chất tu tiên (không hình học cơ bản); đọc ngay là trận lôi; tâm đủ thoáng; khác hẳn màu tia sét trắng xanh nhưng vẫn hợp bộ; sang, cuốn hút; dùng làm khung đầu video. Dưới 8 vẽ lại một lần.

## Xong khi
3 ảnh + prompt + `S/thunder-array-348-sheet.jpg` (A, B, vành rời, có nhãn) + báo cáo có bảng.
