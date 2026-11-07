# Báo cáo lanePilot · 07/11/2026

Đã làm trong `games/.wt-ic-lab-all`, nhánh `codex/lab-all`:
- Thêm `src/lab/pilot-overrides.ts`: chỉ bật với `?pilot=1`, đọc manifest đè cho `boss`, `blood`, `fire`, `beast`; thay đúng id đã có trong từng kit, giữ các mục khác và đường dẫn media riêng của mỗi nguồn. Cache yêu cầu và cảnh báo tối đa một lần mỗi kit khi thiếu hoặc sai manifest/mục.
- Đọc, kiểm tra và nội suy tuyến tính `envelope` gồm thời lượng, tỉ lệ, alpha, erosion. Không có envelope thì giữ cách phát cũ.
- Nối tại `src/lab/skills-main.ts`; thêm nhãn **Pilot sources** ở `src/lab/ab-flags.ts`. `src/lab/comet-head.ts` nối metadata video Hỏa với envelope và đồng hồ cố định để video cũng nhận đường bao.
- Chạm tối thiểu `src/view/skills/flipbook.ts` vì bộ nạp và pool dùng chung nằm ở đây: thêm điểm biến đổi metadata trước khi nạp atlas và playback tùy chọn do lab cung cấp. Parser game không đọc envelope; không sửa shader, media hay manifest hiện có.
- Thêm `tests/lab/pilot-overrides.test.ts` (29 ca) và cập nhật `tests/lab/ab-flags.test.ts`.

Kiểm tra: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` **126 file / 1.547 test PASS**; `git diff --check` sạch.

Chưa kiểm tra hình ảnh: thư mục `art-src/lab/vfx-pilot-2026-11-07/` chưa có lúc kiểm tra. Bộ nạp đã được kiểm tra bằng manifest mô phỏng qua player thật cho cả bốn kit; cần đặt nguồn rồi quay A/B cùng camera và seed. Không mở trình duyệt, cổng mạng, chạy build hay lệnh Git ghi theo ranh giới phiếu.

## Lắp nguồn pilot · 07/11/2026
- Đã đóng gói đủ P1–P4 vào `games/immortality-cultivation/art-src/lab/vfx-pilot-2026-11-07/{boss,blood,fire,beast}/`: PNG, KTX2, manifest/envelope, recipe và kiểm 5 ô tầng A; không có mục chờ S1/S3.
- P1 take1 khung 36–74 (39 khung); P2 take2 khung 45–71 (27); P3 chép nguyên atlas/recipe S1 (72); P4 v2 giữ 32 khung RGBA/48 fps, RGB nhân coverage một lần cho cộng sáng.
- KTX2 đã giải mã lại: gutter RGB/alpha=0, không khung trùng; MAE RGB vùng hiệu ứng 1,707–2,252/255. Tấm so 6 khung mỗi bản trên nền sáng/tối: `.local/pilot/*-compare.jpg`; đã xem 10/14 ảnh.
- Khóa Hỏa thực là `fire-comet` (job `i2v-fire-comet`); đè đúng khóa này và chiếu lại head/dir qua affine S1. `PILOT_IDS.fire` hiện lệch tên nên vẫn cảnh báo; cần người tích hợp kiểm.
- Tầng A toàn phần còn NOT-ENOUGH-EVIDENCE ở ô tốc độ/kích thước chơi/mip; dữ liệu và gói đạt kiểm ngoại tuyến. Chưa chấm tầng B, chưa xác nhận reveal có hướng/ăn mòn hướng tâm: schema envelope chỉ có start/end.
- Không bỏ nguồn nào; không sửa nguồn/manifest đang dùng/mã; không mở trình duyệt/cổng mạng, không build/test game hay Git ghi. Chi tiết: `vfx-pilot-2026-11-07/source-selection.md`, mỗi kit `tier-a.md`; bàn giao `.local/pilot/handoff.json`.

## Kịch bản quay mù pilot A/B · 07/11/2026
- Đã viết `games/.wt-ic-lab-all/scripts/visual/scenarios/lab-pilot-ab.mjs`; `node --check` PASS; chỉ kiểm cú pháp, chưa chạy trình duyệt/cổng/build/test game.
- Claude chạy ngoài sandbox, khi host 3146 đã có: `cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all && URL=http://127.0.0.1:3146/skills-lab.html OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab SEED=711 ART_MAGICK=/opt/homebrew/bin/magick FFMPEG=ffmpeg node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-pilot-ab.mjs --width=1920 --height=1080 --dpr=1`.
- Mỗi P1/P3/P4 xuất `{X,Y}-sheet.jpg` (12 khung, 4 × 3), `{X,Y}.mp4` (1080p, 90 khung/30 fps), `X-Y.mp4` (trái X/phải Y); chung có `ABOUT.md`, `pilot-ab.json`, `_private/key.json`, `_private/evidence.json`; không gửi `_private` cho giám khảo.
- P1: `__lab.twinPearl.boss()` với `key2=twin-pearl`; P3: hệ Fire, `__lab.type('km')`; cùng camera chơi, seed và đồng hồ 60 Hz; video P3 chỉ lấy 3 giây đầu mưa sao băng hơn 6 giây, còn các đợt sau trong khung dư âm.
- Bỏ P2: manifest có `ringBurst` nhưng `CLIP_ROLES` không nhận và không có chiêu Blood gọi nguồn; đề xuất người tích hợp nối vai trò này vào chiêu và cung cấp hàm `__lab`, chưa tự sửa. P4 dùng đòn nhẹ `__lab.channel('start')` (C, power 0,605/0,22): 0/1 đặt `directional=true` nên chọn `beast-hit-ink-streak`, không phải nguồn cần so.
- Có kiểm pool đúng nguồn/nguồn pilot, chờ giải mã video, giữ khóa riêng và tiếp tục hiệu ứng khác khi một hiệu ứng lỗi; dọn khung riêng bằng capture-prune (xem trước rồi `--apply`) và dựng lại chỉ mục review. Claude cần xem lại mốc pha/camera qua clip; OUT_DIR đã có kết quả thì dùng thư mục mới để giữ lần trước.
