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

## Sửa lớp đè và kiểm nguồn · 07/11/2026
- Tái hiện bằng test hai lỗ hổng: thư viện nạp trước không nhận lớp đè đăng ký sau; sao băng giữ đầu đã cache hoặc chọn atlas hybrid thay nguồn pilot. Sửa `src/lab/{pilot-overrides,comet-head,skills-main}.ts` và tối thiểu `src/view/skills/flipbook.ts` để đổi nguồn, gắn lại pool, giữ atlas không liên quan.
- Thêm `__lab.pilotStatus()` cho đủ 4 id: `override`, `atlasUrl`, `textureUrl` PNG/KTX2 thực dùng, `loaded`, `plays`; không tính texture trống hay sprite bị bỏ, thẻ ONE_FRAME tính mỗi lần gửi khung. Kiểm cả nạp, giải phóng và phát trong `tests/lab/pilot-overrides.test.ts` (38 ca, có 4 manifest thật; bộ giải mã/texture được mô phỏng).
- `scripts/visual/scenarios/lab-pilot-ab.mjs`: cả A/B có `video=0`; kiểm nguồn bằng trạng thái và số lần phát tăng sau warm-up, lưu trạng thái vào bằng chứng, bỏ dò performance. Giữ trigger P1 vì `addBoss()` → `spawnBeast()` đặt đúng cờ boss; P2 vẫn bỏ vì chưa có chiêu nối nguồn.
- Kiểm cuối: `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4` PASS **126 file / 1.556 test**; `node --check scripts/visual/scenarios/lab-pilot-ab.mjs` và `git diff --check` PASS.
- Chạy lại ngoài sandbox, dùng thư mục mới: `cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all && URL=http://127.0.0.1:3146/skills-lab.html OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab-fix SEED=711 ART_MAGICK=/opt/homebrew/bin/magick FFMPEG=ffmpeg node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-pilot-ab.mjs --width=1920 --height=1080 --dpr=1`.
- Chưa mở trình duyệt/quay A/B theo ranh giới phiếu, nên chưa khẳng định nguyên nhân duy nhất của dấu vết P1/P4 trên host; Claude cần xem trạng thái và clip mới. Không sửa media, build, cổng mạng hay Git ghi; chưa xác định vị trí gây feedback loop/B9.

## Căn camera và kiểm pixel · 07/11/2026
- Sửa `games/.wt-ic-lab-all/scripts/visual/scenarios/lab-pilot-ab.mjs`; thêm tối thiểu `__lab.captureCamera/fxInstances` trong `src/lab/skills-main.ts`: lấy vị trí nguồn đang vẽ (P1 cổng boss, P3 sao băng, P4 quái trúng đòn), xuất hai góc `play/close`, căn cận cảnh bằng pixel vào 35–60% chiều cao; X/Y dùng nguyên cùng tư thế, khóa rung camera khi chụp.
- `_private/evidence.json` lưu camera, số pixel chênh độ sáng > 8/255 từng khung so ảnh ngay trước kích và đỉnh; giao với chênh ảnh cùng thời điểm khi ẩn nguồn để loại nền/chớp sáng. Đỉnh < 0,5% ném lỗi; vẫn đo các góc/bản còn lại, giữ ảnh trước/đỉnh và dọn khung thô cả khi lỗi. Đã bỏ hẳn bước ghép X|Y.
- Kiểm tra PASS: `node --check scripts/visual/scenarios/lab-pilot-ab.mjs`; `node scripts/visual/scenarios/lab-pilot-ab.mjs --self-test` (ảnh tổng hợp: ngưỡng >8, 0,49% trượt/0,50% đạt, hộp bao, nền chuyển động, ảnh tối, sai kích thước); `npx --no-install tsc --noEmit`; `npx --no-install vitest run --maxWorkers=4` (126 file / 1.556 test); `git diff --check`.
- Chạy lại ngoài sandbox khi host 3146 đã có: `cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all && URL=http://127.0.0.1:3146/skills-lab.html OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/pilot-ab-v3 SEED=711 ART_MAGICK=/opt/homebrew/bin/magick FFMPEG=ffmpeg node src/kit/tools/cdp-run.mjs scripts/visual/scenarios/lab-pilot-ab.mjs --width=1920 --height=1080 --dpr=1`.
- Chưa quay/nhận xét hình thực vì phiếu cấm trình duyệt và mở cổng; người điều phối cần xem `{P1,P3,P4}/{play,close}/{X,Y}-sheet.jpg`, clip và số đo mới. P2 giữ bỏ qua vì chưa có chiêu nối nguồn; không sửa media, build hay Git ghi.
