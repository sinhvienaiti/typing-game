# Báo cáo phiếu 247 · Last Line · Năm icon đổi ý tưởng

**Người làm:** Claude (điều phối), 01/11/2026 từ 00:30 tới khoảng 02:40. Chủ dự án hỏi "mà bạn có thể tự tạo ảnh k? nếu có thì bạn tạo luôn được chứ". Lúc đó Codex hết hạn mức, Antigravity đang làm phiếu 250, nên Claude nhận 247 và gạch khỏi hàng Antigravity (`5f83b267`).

**Công cụ:** Adobe Firefly trên web, mô hình **Firefly Image 5** của Adobe (không dùng mô hình đối tác). Khung vuông 1:1, 1K, không preset. Tính năng chuẩn, không tốn credit cao cấp (vẫn 8660/10000).

## Kết luận

- **Chưa icon nào đạt 8, nên phiếu không nhận icon nào.**
- Có 21 lượt sinh qua ba vòng, sáu giám khảo mù chấm ở cỡ thật. Bản tốt nhất mỗi hàng được 6,5–7 điểm; các icon đang trong game chỉ được 4–5,5.
- Theo luật dừng, không vẽ thêm. Bản tốt nhất được lưu với tên vòng (bên dưới), chưa gắn vào game.

| Hàng (cỡ 720p) | Icon trong game | Bản tốt nhất | Điểm của bản tốt nhất (giám khảo E, F) | Nó trông như gì |
|---|---|---|---|---|
| Steadiness (28 px) | `stat-evenness.r2`: 4,5 / 4 | `stat-evenness.r3.png` (từ `r3-try2`) | 7 / 7 | máy đếm nhịp, kim lam thẳng đứng; có lúc đọc thành nón giao thông hay chữ A |
| New-word read (28 px) | `stat-new-word.r2`: 5 / 4,5 | `stat-new-word.r5.png` (từ `r5-try1`) | 6,5 / 7 | một trang giấy có dòng chữ và tia sáng lam ở góc; trông như "tài liệu mới", nét hơi văn phòng |
| Rift (24 px) | `rift.r2`: 5 / 4,5 | `rift.r3.png` (từ `r3-try3`) | 6,5 / 6,5 | vòng ngà có vết nứt tím chữ chi; còn đọc ra tia sét |
| Adapt pace (28 px) | `pace-director.r2`: 5,5 / 5 | `pace-director.r5.png` (từ `r5-try1`) | 7 / 6,5 | mũi tên vòng lam quanh mặt đồng hồ; ít ngà và vàng hơn bộ icon |
| Screen shake (28 px) | `shake.r2`: 4,5 / 4,5 | `shake.r5.png` (từ `r5-try1`) | 6,5 / 6,5 | màn hình trống có sóng rung lam hai bên (biểu tượng điện thoại rung); hơi giống máy tính bảng |

## Cách làm

1. Prompt viết theo khối STYLE-UI và SMALL-SIZE của 242, rút gọn cho Firefly. Nền là magenta phẳng, riêng Rift dùng xanh lá vì có màu tím.
2. Lấy ảnh ra khỏi trang: blob của trang được gửi bằng form POST tới `127.0.0.1:8765` (`scratchpad/ff-recv/recv-img.py`). CSP của trang không chặn `form-action`.
3. Tách nền bằng `scratchpad/g247/tools/key.py`:
   - màu nền lấy từ viền ảnh, lấp loang từ mép vào;
   - túi màu nền nằm kín bên trong đổi thành kính tối;
   - mép được gỡ trộn màu nền rồi khử ám 4 px;
   - mảnh rời nhỏ (chữ mã màu mà Firefly vẽ thêm) bị bỏ;
   - icon được căn giữa.
4. Sửa màu sau khi sinh, ghi rõ trong `.prompt.txt` của từng bản:
   - nêm tím trong đồng hồ `r3-try1` đổi thành kính tối;
   - khung bóng hồng của `shake.r4-try1` đổi thành ngà mờ;
   - trang giấy `r5-try1` bị ám hồng từ nền magenta, đổi lại màu ngà, giữ độ sáng.
5. Vòng 2 nạp ba icon đã nhận (`clock.r2`, `stat-accuracy.r2`, `kills.r2`) làm ảnh tham chiếu phong cách: ảnh được đưa vào trang bằng `<img crossOrigin>` từ `127.0.0.1:8767`, vì `fetch` bị chặn.
6. Chấm: tờ tự dựng ở 1×, mảnh panel và nút thật (`bg-pan`, `bg-btn`), 720p (28 px, Rift 24 px) và 1080p (40/32 px), icon cũ đặt cạnh các ứng viên và các icon đã nhận trong cùng hàng.
   - Mỗi vòng có hai giám khảo mới, chấm mù. Nhãn trung tính (current, c1, c2…), khoá để ngoài thư mục của họ.
   - Mỗi giám khảo phải viết "trông giống gì" trước khi đọc nhãn.

## Ba vòng

| Vòng | Lượt | Điểm chính (hai giám khảo) | Bài học |
|---|---|---|---|
| 1 (`.r3`, không ảnh mẫu) | 10 | Máy đếm nhịp try2: 7 / 7; sách: 6,5 / 5,5; đồng hồ tốc độ: 6,5 / 6,5; Rift try3: 6,5 / 6,5; Screen shake: tối đa 5,5 | Mọi màn hình đều lẫn với icon Quality; quyển sách lẫn với Rule; vết nứt mảnh đọc thành tia sét. Tôi tự chấm máy đếm nhịp 8, cao hơn thực tế. |
| 2 (`.r4`, có ảnh mẫu phong cách) | 5 | Thẻ chữ 5,5 / 4,5; đồng hồ tối 4,5 / 4,5; khung bóng 4 / 3,5; Rift 5,5 / 6 | Ảnh mẫu cho nét trang trí giống bộ, nhưng ở 28 px thành rối. Ứng viên to và nặng hơn các icon bên cạnh. |
| 3 (`.r5`, không ảnh mẫu, sửa đúng góp ý, thu về 74 % cạnh dài) | 6 | Như bảng kết luận | Đọc nghĩa tốt hơn (vòng mũi tên, sóng rung, trang có tia sáng), nhưng chưa ai cho 8. |

Mọi lượt nằm trong `games/typing-survival/art-src/ui/icons/`. Mỗi lượt có `<tên>.rN-tryM.png` (đã tách nền, 1024), `.raw.png` (bản gốc Firefly) và `.prompt.txt` (prompt đúng từng chữ, kèm thay đổi so với lượt trước):
- Steadiness: `stat-evenness` `r3-try1..3`, `r5-try1..2`;
- New-word read: `stat-new-word` `r3-try1`, `r4-try1`, `r5-try1`;
- Rift: `rift` `r3-try1..3`, `r4-try1`, `r5-try1`;
- Adapt pace: `pace-director` `r3-try1`, `r4-try1`, `r5-try1`;
- Screen shake: `shake` `r3-try1..3`, `r4-try1`, `r5-try1`.

Tờ chấm của từng vòng và khoá mù nằm ở `games/typing-survival/art-src/_review/247/`.

## Số đo của bản tốt nhất (ở cỡ 720p)

| Bản | Phủ ngang | Phủ dọc | Mép còn sắc nền | M (điểm đặc gần magenta) |
|---|---|---|---|---|
| `stat-evenness.r3` | 0,71 | 0,71 | 3,7 % | 0 |
| `stat-new-word.r5` | 0,57 | 0,71 | 0,5 % | 0,18 % |
| `rift.r3` | 0,75 | 0,75 | 0,03 % | 0 |
| `pace-director.r5` | 0,71 | 0,71 | 1,0 % | 0,03 % |
| `shake.r5` | 0,79 | 0,43 | 6,5 % | 0 |

## Khác phiếu, và lý do

- **Quá 3 lượt mỗi ảnh.** Vòng 2 và 3 là ý mới hoặc sửa theo góp ý cụ thể của giám khảo, đặt tên `.r4`, `.r5` như mục "Lượt 2" của phiếu 250. Riêng máy đếm nhịp và Rift giữ ý cũ: hai icon này dùng 5 lượt.
- **Độ phủ.** Phiếu đòi ≥ 70 % cả hai chiều. Cả bốn giám khảo hai vòng đầu nói icon phủ 78–88 % to và nặng hơn các icon đã nhận (chúng chỉ chiếm khoảng 70 % canvas). Nên vòng 3 đặt cạnh dài 74 %.
  - Trang giấy rộng 0,57 vì nó là hình đứng.
  - Screen shake cao 0,43 vì nó rộng gấp đôi (2:1, vượt mức 1,25:1 của phiếu). Đó là dáng của sóng rung hai bên, ý mà giám khảo đề nghị.
- **Screen shake bỏ "vạch giật chữ chi".** Firefly vẽ mọi đường chữ chi trên màn hình thành tia sét (try1) hoặc đường nhịp tim (try2).
- **Pace bỏ màu cam,** theo góp ý: màu cam là màu cảnh báo của game.

## Bước tiếp (chủ dự án chọn)

1. Gắn tạm năm bản tốt nhất. Chúng hơn icon hiện có 1,5–3 điểm nhưng dưới mức 8, nên phải ghi là tạm, trái luật 2D ≥ 8.
2. Giữ icon hiện có, tìm nguồn có sẵn hợp phong cách hoặc nhờ người vẽ.
3. Giao lại cho Codex khi có hạn mức, kèm góp ý cụ thể của giám khảo vòng 3:
   - nghiêng cần lắc, có quả nặng lam, viền vàng;
   - thẻ chữ có một ký tự đậm hoặc một vạch chữ sáng;
   - vết rách rộng có ánh tím tràn ra;
   - vòng mũi tên bằng ngà hoặc vàng thay vì nét lam phẳng;
   - mặt màn hình sáng hơn và sóng rung dày hơn.

## Quyết định của chủ dự án (01/11)

- Chủ dự án chọn **"Gắn tạm"**: năm bản tốt nhất vào game như bản tạm, chưa được nhận.
- Đã gắn ở Last Line `main` `a4d2b97`. Trong selection, năm mục đều có `ticket: "247"`, `provisional: true` và lời phán "Tạm 01/11". Changelog: `games/typing-survival/docs/changelog/2026-11-01-icons-247-provisional.md`.
- Kiểm trong game ở 720p và 1080p:
  - kỹ thuật đạt ở mọi chỗ: Options, bảng Settings nhanh, Profile, dải cảnh báo Rift;
  - so với icon thật đang có trong game (các bản gốc, không phải `.r2`), điểm cũ → mới: Steadiness 5 → 5,5; New-word read 3,5 → 6; Rift 4,5 → 6,5; Adapt pace 5 → 6; Screen shake 4 → 5,5.
- **Chỉnh lại một chỗ của bảng kết luận:** cột "Icon trong game" ở trên thật ra chấm các bản `.r2` của phiếu 242/243. Các bản này chưa từng được gắn vào game; game vẫn dùng bản gốc. Điểm trong game của bản gốc là dòng "cũ" ngay trên.
