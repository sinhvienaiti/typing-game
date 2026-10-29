# Clip hiệu ứng tạo bằng Firefly Video (Dragonhold, lô 1)

Chủ dự án, 29/10/2026 tối: sau clip thử `fire-burst__v1`, lửa của Rồng "cố gắng lên 9, 8,5 vẫn chấp nhận được" (`docs/games/VFX_STANDARD.md` §5.6). Chủ dự án duyệt khoảng 25 clip (khoảng 2.500 credit) cho lô này.

## 1. Luật

- **Chỉ model Firefly Video của Adobe** (nhãn "Commercially safe"). Model đối tác (Veo, Kling, Seedance, Runway, Ray…) chỉ để tham khảo, không đưa vào game.
- Người điều phối tạo trong tab Firefly chủ dự án đã đăng nhập; không đăng nhập hộ, không mua credit. Lô mới hay vượt số clip đã duyệt thì hỏi chủ dự án trước.
- Cài đặt: 1080p, 24 fps, 5 giây; tỉ lệ theo bảng dưới.
- **Không tốn credit** (đo 29/10): tài khoản ghi "Standard features: Unlimited access", số dư đứng 8.900/10.010 sau 25 clip. Nhưng có **giới hạn tốc độ**: gửi dồn quá khoảng 10 lệnh thì báo "Something went wrong" hoặc "try again at …" (chờ vài phút). Gửi cách nhau 8–30 giây.
- **Tải về:** nút Download của trang không lưu file trong khung trình duyệt của app. Bấm từng ô ở dải lịch sử bên phải để trang nạp video, đọc `src` của thẻ video (link ký tên, hết hạn sau 4 giờ, không chia sẻ), tải bằng `curl`, so cỡ với `x-resource-length`, rồi xóa file chứa link.
- Video là media, không vào Git. Clip gốc: `~/VFXLab/inbox/firefly/dragon-hold/<id>/<id>__vN.mp4`, kèm `<id>__vN.txt` ghi model, cài đặt, prompt, ngày, credit trước và sau.
- Flipbook ra: `~/VFXLab/out/dragon-hold/<id>/` (công cụ `tools/vfx-flipbook/`), rồi chép bản chọn vào `games/dragon-hold/art-src/vfx/firefly/` khi V-dh2 dùng.

## 2. Đuôi chung của prompt

Mọi prompt mở bằng **"Game VFX element, stylized painterly fantasy fire for a dragon,"** và đóng bằng:

> Pure black background, nothing else in frame, no ground, no floor, no text. Locked-off static camera, the effect stays inside the frame. Steady exposure, no camera shake.

Riêng `smoke-roll` dùng nền trắng (khói tối trên trắng tách bằng độ sáng, chắc hơn tách màu xanh với khói nửa trong).

## 3. Danh sách

| id | Pha | Dùng cho | Tỉ lệ | Lặp | Blend | Số bản | Ô atlas |
|---|---|---|---|---|---|---:|---|
| `charge-orb` | A gồng | cầu lửa trước mõm khi gõ | 1:1 | có | additive | 3 | 256 |
| `muzzle-flash` | R tung đòn | lóe và lưỡi lửa ở miệng | 16:9 | không | additive | 3 | 256×128 |
| `fireball-head` | T bay | đầu đạn đòn chữ và Sky Fire | 1:1 | có | additive | 2 | 256 |
| `flame-trail` | T bay | vân lửa cuộn UV cho ribbon | 16:9 | có | additive | 2 | dải 1024×256 |
| `impact-burst` | I trúng | nổ đòn thường (đã có v1) | 1:1 | không | additive | 2 | 256 |
| `impact-big` | I trúng | nổ đòn mạnh, Sky Fire | 1:1 | không | additive | 3 | 512 |
| `smoke-roll` | F dư âm | khói than sau nổ | 1:1 | không | normal | 3 | 256 |
| `embers` | I, F | tàn lửa, tia lửa bay cung | 1:1 | không | additive | 2 | 256 |
| `ground-fire` | F dư âm | đám lửa cháy trên đất sau Sky Fire | 1:1 | có | additive | 2 | 256 |

Tổng 22 clip mới, cộng `fire-burst__v1` đã có. Còn khoảng 3 lượt cho bản hỏng.

**Đã tạo (29/10, khoảng 20:10–20:40):** 24 clip mới, đủ chín id; `impact-burst__v1` là bản chép của clip thử 16:9. Nhận xét nhanh của điều phối (chưa chấm):
- `muzzle-flash` v1–v3 mỏng (sao lóe kèm vệt nhỏ); v4, v5 dùng prompt mạnh hơn (dưới đây) nên ra luồng lửa dày, cuộn khói, nhưng chạy chéo từ dưới trái lên trên phải, cần xoay.
- `fireball-head` v1 vẽ tay đẹp, bay sang trái; v2 tô phẳng kiểu hoạt hình, loại.
- `impact-burst` v2, v3 và `impact-big` v1–v3 đều dùng được: lóe sao, khối lửa cuộn, vành khói tối viền đỏ.
- `charge-orb` ra xoáy lốc; `embers` ra chùm tia đầu tròn; `flame-trail` ra dải lửa có lỗ, hơi giống dung nham.
- `ground-fire` v1 là bức tường lửa thấp nhìn ngang; v2 là nêm lửa chéo, loại.
- `smoke-roll` khói xám đậm trên nền trắng, đẹp nhưng nở tràn mép khung từ giữa clip: dùng đoạn đầu và làm mờ mép.

Prompt `muzzle-flash` v4, v5 (phần giữa): a powerful cone-shaped blast of fire erupts from the left edge and fills the left half of the frame: a bright white-yellow flash at the source, then a wide cone of thick rolling orange flames with ragged tongues of uneven length bursts to the right, the flames curl, break apart and fade into embers and a little dark smoke within one second.

### Prompt (phần giữa)

- **charge-orb:** a small swirling orb of fire hovers in the centre, flame wisps spiral inward toward a white-yellow hot core, saturated orange body, deep red edges, tiny embers are drawn into it; the orb keeps the same size and brightness the whole time, a seamless continuous loop with no build-up and no fade.
- **muzzle-flash:** a short violent jet of fire bursts from the left edge toward the right: a bright star-shaped flash at the left, then three to five ragged flame tongues of uneven length shoot to the right and break apart within half a second, leaving a few embers and a thin wisp of dark smoke.
- **fireball-head:** a rolling ball of fire stays in the centre while its flames churn and lick backward to the left, as if it flies to the right; white-yellow core, orange body, deep red ragged edges; constant size and brightness, a seamless continuous loop.
- **flame-trail:** a horizontal river of fire flows steadily from left to right across the whole width of the frame, a band about one fifth of the frame tall, turbulent noisy flame texture with holes and torn edges, yellow-hot in the middle, orange and deep red at the edges; the same density all the time, a seamless continuous loop.
- **impact-burst:** a dragon fireball bursts in the centre of the frame with a small white-yellow hot core, a saturated orange body and deep red edges that break into licking flame tongues, then it rolls outward and fades into dark charcoal smoke with a few drifting embers.
- **impact-big:** a large fiery explosion erupts in the centre: a brief white-yellow flash, then a rolling ball of orange fire with inner shadows billows upward and outward, deep red edges, then it turns into dark charcoal smoke while sparks fly out.
- **smoke-roll:** thick dark charcoal grey smoke billows up from the lower centre, rolls and expands, then thins out and fades away completely; no fire, no sparks. (Đuôi: "Pure white background…" thay cho nền đen.)
- **embers:** a burst of glowing embers and hot sparks flies outward from the centre in arcs that fall with gravity, each spark a bright yellow head with a tapering orange-red tail, they cool and fade out; no flames, no smoke.
- **ground-fire:** a low patch of flames burns on an invisible floor, seen from a three-quarter top-down view, small licking flame tongues and floating embers, constant intensity, a seamless continuous loop.

## 4. Cắt thành flipbook (việc của `tools/vfx-flipbook/`)

- Một lần nổ (`impact-*`, `muzzle-flash`, `embers`, `smoke-roll`): bỏ khung đen đầu, khung đầu của lóe ≥ 95 % đỉnh (§5.6), cắt đuôi khi tắt hẳn; 24–32 khung.
- Lặp (`charge-orb`, `fireball-head`, `flame-trail`, `ground-fire`): chọn đoạn 1–2 giây đều nhất, nối vòng bằng hòa chéo; không nháy ở chỗ nối.
- Đen nền về 0 (crush), căn tâm theo khối sáng, cắt vuông hay chữ nhật theo bảng, atlas PNG lũy thừa 2, JSON `{ cols, rows, fps, loop, blend, cell, pivot, source }`, tờ xem trên nền sáng và nền tối.
- Lõi trắng ≤ 30 % bán kính (VFX_STANDARD); nếu clip quá trắng thì hạ đỉnh, không cắt màu.
