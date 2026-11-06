# B3 · Âm cho các sự kiện B1/B2 · 07/11/2026

Đã nối đủ **5 sự kiện**, dùng **6 việc âm chưa gắn**. Đo 40 take bằng `ffmpeg ebur128`; đối chiếu `group`, `why` và prompt cạnh WAV. Giữ nguyên mọi dòng âm/mức cũ; không sửa nguồn Firefly, không tổng hợp âm.

## Take và mức

Id trong bảng có tiền tố `tt-sfx-`; file là `sound/<id>/take<N>.wav`. M/TP: LUFS-M/dBTP; đầu bỏ: giây. Đích đã tính bus/master, từng take giữ dưới −1 dBTP.

| Sự kiện / id | Take | M / TP | Đầu bỏ | Đích M | Lý do chọn |
| --- | ---: | --- | ---: | ---: | --- |
| Boss xuất hiện · `boss-entrance-roar` | 6 | −5,8 / 0,0 | 0,0094 | −13,5 (T4) | Prompt gầm Lang Vương lúc vào; duy nhất không có mẫu chạm rail trong 8 take; thân/đuôi tới 4,40 s. |
| Qua 50% · `boss-phase2-roar` | 3 | −8,1 / −0,2 | 0,0193 | −13,5 (T4) | `why` chuyển pha, gầm giận dữ; duy nhất không chạm rail trong 8 take; đuôi tới 4,18 s. |
| Cùng chuyển pha · `boss-phase-shockwave` | 1 | −5,8 / 0,0 | 0,0140 | −22 (lớp phụ) | Prompt sóng gầm lan ra; ít mẫu chạm rail nhất: 2, so với 5–9 ở các take khác; không có plateau liên tiếp. Giữ dưới tiếng gầm. |
| Tinh anh bật hào quang · `elite-reveal-aura` | 3 | −11,1 / −0,4 | 0 | −18 (T3) | Prompt tinh anh hiện ra và hào quang bật; đầu tức thì, không chạm rail, đuôi hết khoảng 1,91/2 s. |
| Tuyệt kỹ sẵn sàng · `ui-skill-ready` | 1 | −8,8 / 0,0 | 0 | −18 (T2, khô) | `why` báo chiêu sẵn sàng; đầu tức thì, không chạm rail, đuôi khoảng 0,86 s. |
| Kim thân bật · `guard-body` | 3 | −8,0 / −2,3 | 0,0096 | −18 (T2, khô) | Việc này còn chưa gắn; prompt lớp bảo vệ hình thành khớp vỏ kim thân. Crest thấp nhất trong 4 take, không chạm rail. Giữ 0,16 s rồi fade 0,25 s theo hình; đoạn thực phát đo khoảng **−27,9 LUFS-M**, nhường âm va chạm cũ. |

## Đường dẫn và hook

Trong `games/.wt-ic-lab-all/`:

- `src/lab/sound.ts`, `src/lab/sound-tiers.ts`: thêm 6 mục `SPRINT_TAKES` và `FIREFLY_LEVELS`.
- `src/lab/foe-flipbook-fx.ts`: gọi lúc kích hoạt boss/tinh anh và đúng lần vượt ngưỡng 50%; không phát theo vòng lặp hình.
- `src/lab/hero-presence-fx.ts`: gọi khi sẵn sàng chuyển tắt → bật và kim thân kích hoạt sau block thành công; kéo dài cùng lần bật không phát lại.
- `src/lab/skills-main.ts`: nối hai callback vào `sound.sprint`, giữ nguyên âm chặn cũ.
- `tests/lab/laneB3-sounds.test.ts`: 9 test node mới; `tests/lab/lane5-sounds.test.ts`: mở rộng kiểm tra bảng âm.
- `.local/laneB3-sounds/`: `inventory.json`, `measure.py`, `measurements.json`, `picks.json`, `checks.json`, log đo đoạn kim thân và log kiểm tra.

## Kiểm tra và bàn giao

- Trước: **118 file / 1.384 test qua**. Sau: **119 file / 1.393 test qua**, bằng `npx --no-install vitest run --maxWorkers=4`.
- `npx --no-install tsc --noEmit`: sạch. `git diff --check`: sạch.
- Test xác nhận WAV/prompt thật, mức đo, onset, đúng id, phát một lần, tái kích hoạt/reset; `?foeaura=0` và `?presence=0` không phát tiếng của lớp tương ứng.
- **Bỏ qua:** không có sự kiện nào. Không mở trình duyệt/build theo ranh giới ticket.
- **NOT LISTENED:** anh cần nghe xác nhận trong lab, nhất là lớp sóng xung kích có 2 mẫu rail đơn và cân âm kim thân với tiếng chặn. Số đo không thay nghiệm thu bằng tai.
