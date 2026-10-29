# Phiếu 173 · Dragonhold · Bộ texture lửa cho đòn chữ, Sky Fire và gõ chữ (12 tấm)

**Báo cáo:** `docs/codex-queue/173-report.md`, thư mục `games/dragon-hold/art-src/_review/173/`.

## Luật chung (phiếu ảnh VFX, mức chợ từ 28/10)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`. Ảnh là media, không vào Git.
- **Vì sao có phiếu:** VFX do Claude dựng bằng shader và hạt (luật `docs/games/VFX_STANDARD.md`). Các giám khảo VFX 29/10 chê lửa, vệt, khói "phẳng như mảng màu cắt", "ống cam trơn", "củ cà rốt". Texture vẽ tay tốt (flipbook, sprite, decal) cho shader thêm chi tiết bên trong mà không tốn draw call. Chủ dự án 29/10: Codex còn nhiều hạn mức, giao thêm việc trước khi Claude hết hạn mức.
- **Mức nhận:** M ≥ 8 theo game thương mại (thang `docs/games/ART_DIRECTION_2026-10-28.md` §1.3; ảnh tham chiếu của chủ dự án `games/<id>/art-src/_refs/owner-epic-2026-10-28.webp`) và Q ≥ 8 (`docs/games/ART_ACCEPTANCE.md` §2.2). Tối đa 3 lượt sinh mỗi ảnh; mọi lượt giữ `.tryN.png` và `.tryN.prompt.txt`; bản chọn `<tên>.png`, `<tên>.prompt.txt`, `<tên>.alpha.png`.
- **Luật hậu kỳ (bắt buộc, 29/10):** `docs/games/ART_ACCEPTANCE.md` §5: tờ "bản sinh | bản hậu kỳ" cho mỗi ảnh; công cụ không được xóa, san phẳng hay phủ phần vẽ; ngưỡng số mâu thuẫn với tranh thì dừng và ghi lại; tự chấm trên bản hậu kỳ.
- **Nền:** nền phẳng `#000000` đen tuyền cho mọi tấm lửa, lóe, tia (sẽ dùng blend cộng sáng; ghi rõ trong `.json`), hoặc nền `#FF00FF` rồi tách alpha cho khói, muội, mảnh vỡ, decal (blend thường). Mỗi tấm ghi `"blend": "additive"` hay `"normal"` trong `<tên>.json`.
- **Flipbook:** lưới đều, mỗi ô cùng cỡ, vật ở cùng tâm; khung đầu và khung cuối nối được (vòng lặp) khi ghi `"loop": true`. Ghi `{ "cols", "rows", "fps", "loop", "blend" }` vào `<tên>.json`.
- **Cấm:** ghi đè, đổi tên, xóa file có sẵn; xóa `.try*`; mọi lệnh git; sửa mã hay tài liệu (trừ báo cáo); dev server, trình duyệt, mạng ngoài công cụ tạo ảnh; đụng game khác, Tu Tiên; chữ, số, logo trong ảnh.
- **KA1 md5:** `md5 -r` mọi file trong thư mục đích trước và sau; `diff` chỉ có dòng thêm.
- **Báo cáo** tiếng Việt `docs/codex-queue/173-report.md`: prompt từng lượt, bảng số đo, M và Q, đường dẫn tờ, chỗ làm khác phiếu.

## Kiểm (bắt buộc, ghi số)

1. Khổ đúng bảng; alpha sạch (ngoài dải mép 3 px quanh vật alpha 0 hay 255; px mang màu nền ≤ 0,2 %); tấm cộng sáng: nền đen thật (px nền ≤ 2/255).
2. Flipbook: IoU mặt nạ giữa hai khung kề nhau 0,55–0,95 (chuyển động mượt, không đứng yên); `loop` thì khung cuối và khung đầu cũng trong dải đó.
3. Lõi trắng ≤ 30 % bán kính vật ở khung sáng nhất (đo px có luma > 0,92); ramp màu đủ ba dải (lõi, thân, mép) theo bảng.
4. Tờ `_review/173-sheet.jpg`: mỗi tấm ở cỡ gốc và cỡ trong game; flipbook xếp thành dải khung; mỗi tấm đặt lên một ảnh chụp trận của game (lấy trong `tmp/` của game hay worktree, chỉ đọc) ở cả nền sáng và nền tối.
5. KA5: M và Q cho mỗi bản chọn.

## Phiếu

**Chỉ được ghi:** `games/dragon-hold/art-src/vfx/fire-v2/` (thư mục mới), `games/dragon-hold/art-src/_review/173*`, báo cáo.

**Phong cách:** Khối STYLE của Dragonhold, nguyên văn ở `docs/games/ART_DIRECTION_2026-10-28.md` §3.2, cộng câu `Stylized painterly game VFX texture, hand-painted fire with internal detail, not photographic.` Bảng màu lửa rồng: lõi trắng vàng, thân cam bão hòa, mép đỏ thẫm, muội than tối. Xem giám khảo: `games/.wt-dh-vfx/tmp/vfx/judge-r6/verdict.md` (chỉ đọc).

| Tên | Khổ | Nội dung (viết prompt tiếng Anh từ mô tả này) |
|---|---|---|
| `flame-tongue` | flipbook 8×4, ô 256² | một lưỡi lửa liếm lên rồi tách ngọn, mép vỡ, chi tiết xoáy bên trong; cộng sáng; loop |
| `flame-ball` | flipbook 8×4, ô 256² | một quả cầu lửa cuộn, lõi nhỏ trắng vàng, thân cam, mép đỏ thẫm vỡ thành lưỡi; cộng sáng; loop |
| `fire-burst` | flipbook 8×4, ô 512² | một cú nổ lửa khi trúng: lóe, nở, tách thành lưỡi, tàn thành than; cộng sáng; không loop |
| `smoke-puff` | flipbook 8×4, ô 256² | một cụm khói than sẫm cuộn lên rồi tan, mép mềm; blend thường; không loop |
| `soot-ring` | 1024² | một vòng muội tối hình xuyến, mép vỡ (lớp tối dưới lửa); blend thường |
| `ember-sprites` | 2048×512, lưới 8×2 | 16 đốm than cỡ khác nhau, có đuôi tối ngắn, cong nhẹ; cộng sáng |
| `flame-trail` | 2048×256, liền mép trái phải | một dải vệt lửa chạy ngang, thon hai mép, có than rụng và sợi khói tối; cộng sáng |
| `heat-ring` | 1024² | một vòng nhiệt cam mảnh, đứt đoạn như chữ rune cháy; cộng sáng |
| `scorch-decal` | 1024², 2 biến thể ghép 2048×1024 | vết xém nhìn từ trên: tâm đen nâu, khe than đỏ nguội, mép tro; blend thường |
| `cracks-glow` | 1024² | khe nứt phát sáng đỏ cam trên đá, nhìn từ trên (dùng cho dư âm Sky Fire); cộng sáng |
| `glyph-spark` | 1024×256, lưới 4×1 | 4 tia lóe hình sao cho chữ vừa gõ: lõi nhỏ trắng vàng, cánh cam; cộng sáng |
| `glyph-ember-burst` | flipbook 4×2, ô 256² | chùm than bung ra từ một chữ khi gõ xong từ; cộng sáng; không loop |

**Xong khi:** đủ 12 tấm có bản chọn, qua mục kiểm 1–4, mỗi tấm tự chấm M ≥ 8 và Q ≥ 8. **Nhận** khi Claude chấm lại; Claude hay làn VFX gắn vào shader.
