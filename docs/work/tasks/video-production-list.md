# Danh sách video nên tạo (Tu Tiên, từ 16/11/2026)

Owner 16/11: "nếu có thể dùng video tạo các loại gì đẹp mà tối ưu thì cứ list ra mà tạo dần đi".
Luật: skill `game-video-vfx-usage` (bậc SHOULD/OPTIONAL; không làm hạng AVOID/NEVER), `game-vfx-production` (mỗi clip một thành phần, image-to-video từ ảnh tĩnh đã duyệt cho mọi thứ có hình, text-to-video chỉ cho chất liệu thuần), gửi owner 2 mẫu trước mỗi loạt. Công cụ: Firefly Video (`/video-generate`), chỉ model Adobe; ~70 clip/ngày.
Luật owner 16/11 (mọi clip): đúng góc camera chơi (~55° nhìn xuống, FOV 28°); chỉ năng lượng trên nền đen, không vẽ sẵn mặt đất/vết cháy/bụi; có điểm chạm đất rõ để code gắn decal, bụi, ánh sáng; ánh sáng và chuyển động chân thật, không như dán lên. Câu gốc: "các video phải được tạo đảm bảo chất lượng và phù hợp góc nhìn, đảm bảo để code có thể tích hợp thêm 1 số hiệu ứng khi gây ra ở mặt đất, nhìn chân thật không bị cảm giác ảo".
Người làm: agent Claude Sonnet lái Firefly; Codex cắt flipbook/KTX2; agent Claude Opus kiểm trong lab.

## Thứ tự

| # | Loại | Bậc | Số clip | Ảnh tham chiếu | Trạng thái |
|---|---|---|---|---|---|
| 1 | Bùng nổ còn thiếu: `metal-impact`, `fire-impact`, `fire-big-burst` chuẩn tên | OPTIONAL | 3 | atlas cùng hệ trong `art-src/lab/vfx/<hệ>/` | chờ kết quả kiểm `burst-audit.md` |
| 2 | Biến thể bùng nổ: thêm 2 bản cho `big-burst` và `impact` của 14 hệ | OPTIONAL | ~56 (làm theo hệ dùng nhiều trước: Lôi, Hỏa, Băng, Kim, Mộc) | clip gốc đã qua kiểm | sau mục 1, gửi mẫu trước |
| 3 | Làm lại 5 clip trượt nặng: `dark-ground-impact` (đá lát vẽ sẵn), `earth-ring-burst` (tảng đá, không phải vòng), `fire-burst` (cắt mép, chỉ một góc), `poison-ring-burst` (chữ vàng vẽ sẵn), `wind-ground-impact` (đĩa xám lạ) | OPTIONAL | 5 | clip gốc + atlas hệ | kiểm xong 16/11 |
| 3c | Làm lại nguồn 3 clip bị cắt (từ 414): `thunder-impact`, `star-ring-burst`, `metal-ring-burst` | OPTIONAL | 3 | clip gốc + atlas hệ | chờ, sau loạt 20 |
| 3b | Cứu clip chạm mép (414: `thunder-ground-impact-m`, `wood-ring-burst-m` đạt) (vòng, sét, khói dark-white): Codex thêm lề/thu nhỏ khi đóng gói atlas, không tạo lại | — | 0 | — | phiếu Codex |
| 4 | Chuyển cảnh: bắt đầu đợt, boss xuất hiện, thắng, thua (luma wipe, khung 1 đen) | SHOULD | 4 | `cutin-mat/cutin-cloud-wipe` + title key art | chờ |
| 5 | Nền tiêu đề / menu chạy vòng (từ ảnh title key art đã duyệt) | SHOULD | 1–2 | `art-src/ui/title-key-art.v1-try*.png` (bản owner duyệt) | chờ |
| 6 | Màn chờ tải chạy vòng, file nhỏ | SHOULD | 1 | title key art | chờ |
| 7 | Dải nền cut-in tuyệt kỹ theo hệ (không có nhân vật; nhân vật chờ nữ chính được duyệt) | SHOULD | 14 | `cutin/`, `cutin-mat/` + ảnh tham chiếu tuyệt kỹ từng hệ (386–407) | chờ |
| 8 | Bụi chết dùng chung theo phe (một puff, code đổi màu) | OPTIONAL | 2–3 | `death/death-soul-threads-w2` | chờ |
| 9 | Lóe phát chiêu tại người tung (1–2 thẻ, không có tay/vũ khí) theo hệ | OPTIONAL | 14 (sau khi kiểm shader flare) | atlas `*-charge` cùng hệ | sau |

Không làm bằng video: vệt bay của chiêu, decal mặt đất, sương, aura vật phẩm, tụ lực theo gõ, dư âm (bậc AVOID/NEVER).

## Nhật ký
- 16/11 · Claude Sonnet 5.5 · làm lại bùng nổ (Firefly Video 1:1 1080p, text-to-video, 30 lượt, ~1 lượt/5 phút từ 12:41, nhật ký giờ ở `typing-game-review/owner-review/2026-11-16/tu-tien/burst-remake/start-times.txt`). Điểm tự chấm, "vào lề" = khung hình (trên 120) nội dung vượt lề 12 %. Mọi take ở `art-src/lab/vfx/<hệ>/firefly-raw/<clip>.v2-try<k>.mp4`; mô hình bỏ qua chỉ dẫn góc nhìn 55° và kích thước, nên cần cắt 1-2 giây đầu hoặc thu nhỏ ~60 % khi đóng gói.
  - metal-impact · try1 · B · lưỡi kiếm khí vàng bạc, vào lề @31
  - fire-big-burst · try1 · B+ · cầu lửa khối, tia lửa, vào lề @27
  - earth-ring-burst · try1 · B+ · sóng bụi vàng và đá, vào lề @49
  - metal-big-burst · try1 · B · vào lề @22
  - void-big-burst · try1 · B · vào lề @10
  - void-ring-burst · try1 · B- · vào lề @27 (tràn khung về cuối)
  - wind-ring-burst · try1 C (mandala xám), try2 B- · xoáy gió, bắt đầu đã lớn (vào lề @0)
  - void-ground-impact · try1 · B- · vào lề @42, tâm rõ nhưng nhìn thẳng
  - dark-ground-impact · try1 · B- · vào lề @35, nhìn từ trên xuống
  - dark-impact-white · try1 · B- · phát sáng, hơi đối xứng, vào lề @39
  - dark-big-burst · try1 · B- · khói tím tia đỏ, vào lề @11
  - poison-impact · try1 · B- · vào lề @44
  - ice-ring-burst · try1 · B- · bông tuyết băng, vào lề @39
  - dark-ring-burst · try1-4 · C+ · cả 4 tràn khung; try3 vòng mảnh, try4 mandala nhìn thẳng; góc 55° không được
  - water-ring-burst · try1 C+, try2 C · giống hoa/mây hơn nước
  - dark-big-burst-white · try1 · C+ · mandala sáng, chạm mép @19
  - blood-big-burst · try1 C+ (mandala đỏ), try2 C (kín khung từ khung 0)
  - dark-ground-impact-white · try1 · C · đối xứng, chạm mép @27
  - poison-big-burst · try1, try2 · C · mandala xanh đặc
  - poison-ring-burst · try1, try2 · C · mandala xanh đặc
  - wood-big-burst · try1 · C · mandala vàng-xanh, vào lề @6
- 16/11 · agent Sonnet · kiểm 59 clip: 44 đạt, 15 trượt (`burst-audit.md`).
- 16/11 · Claude · lập danh sách; agent Sonnet đang kiểm 56 clip bùng nổ (`burst-audit.md`).

## v3 image-to-video from the 55° stills (16/11, agent Sonnet; sheets in owner-review/2026-11-16/tu-tien/burst-remake/i2v/)
- dark-ring-burst · try1 C (top-down circle, past margin) · try2 B (ellipse holds, ~68 % wide, no fade-out) · `dark/firefly-raw/dark-ring-burst.v3-try2.mp4`
- water-ring-burst · try1 A (ellipse crown splash, margins kept, fades to black; the crown cycle repeats once) · `water/firefly-raw/water-ring-burst.v3-try1.mp4`
- poison-big-burst · try1 C (top-down mandala) · try2 B (vertical plume on flat base, margin lost after ~2.5 s, no fade) · `poison/firefly-raw/poison-big-burst.v3-try2.mp4`
- poison-ring-burst · try1 B (ellipse holds, fades dim, reaches ~97 % width at the end; use 0-3 s) · `poison/firefly-raw/poison-ring-burst.v3-try1.mp4`
- blood-big-burst · try1 C (flower mandala) · try2 A (flat ground ring + vertical plume, margins kept, fades to black) · `blood/firefly-raw/blood-big-burst.v3-try2.mp4`
- wood-big-burst · try1 C (top-down mandala) · try2 B (lotus base + plume, plume leaves the top edge after ~2.5 s; use 0-2.5 s) · `wood/firefly-raw/wood-big-burst.v3-try2.mp4`
- dark-big-burst-white · try1 C (symmetric mandala) · try2 B (flat base + plume, base symmetric, margin lost after ~2 s, no fade) · `dark/firefly-raw/dark-big-burst-white.v3-try2.mp4`
- dark-ground-impact-white · try1 B (flat base + vertical column, ~78 % wide at 2.5 s, no fade; use 0-2.5 s) · `dark/firefly-raw/dark-ground-impact-white.v3-try1.mp4`
- thunder-impact · try1 B (ground arcs + bolt, 55° view holds, wide at the end, no fade; use 0-2.5 s) · `thunder/firefly-raw/thunder-impact.v3-try1.mp4`
- star-ring-burst · try1 B (gold ellipse ring holds, fades late, ~97 % wide at 3.5 s; use 0-3 s) · `star/firefly-raw/star-ring-burst.v3-try1.mp4`
- Totals: 15 generations, no limit hit. Prompt rule learned: spreading bursts become mandalas; "burns and billows in place, mostly vertical, flat base" keeps the view. Prompts beside each mp4 (`.prompt.txt`).

## v4 wide-burst remake (16/11, agent Sonnet; Firefly Video (Adobe), image-to-video from 55° stills, 1:1 1080p 5 s; sheets in owner-review/2026-11-16/tu-tien/burst-remake/wide/)
- blood-big-burst · try1 B (elliptical crown of rays on a ground ring, 55° holds, wide, fades to black; rays a little straight and ~10 % margin at peak) · `blood/firefly-raw/blood-big-burst.v4-try1.mp4` · start 19:10:00
- poison-big-burst · try1 C (gas grows into a top-down blob, margin lost, no fade) · try2 C (same mandala, even with "gas does not expand sideways") · starts 19:04:34, 19:15:50 · no usable take
- thunder-impact · try1 B (wide ellipse of arcs plus bolt, ~6 % margin mid-clip) · try2 A (compact fan from the ellipse, margin ~20 %, fades) · `thunder/firefly-raw/thunder-impact.v4-try2.mp4` · starts 18:58:41, 19:21:36
- Prompt rule: "erupts along its whole wide ground ellipse, many jets side by side" gives a crown for rays and arcs (blood, thunder) but gas (poison) still billows into a mandala; for poison try another still or a reference-style prompt.

## v5 blood-crown (16/11, agent Sonnet; Firefly Video, image-to-video, first frame `blood/stills-55/blood-crown.v2-try1.png`, 1:1 1080p 5 s; sheets in owner-review/2026-11-16/tu-tien/burst-remake/blood-crown/)
- blood-big-burst · try1 C (glossy crown for ~2 s, then flat wide ring of straight spikes, margin lost, no fade) · try2 C (same arc with the "stay compact, fade to black" prompt; first ~2 s slightly better, tendrils round-tipped) · `blood/firefly-raw/blood-big-burst.v5-try2.mp4` best (use only the first ~2 s) · starts 22:20:35, 22:25:50
