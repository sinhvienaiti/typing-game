# Phiếu 192 · Settings, Sound và tiếng phím Firefly

Ngày 30/10/2026 · Mac mini M4 · worktree `games/.wt-dh-keys`, nhánh `dh-keys`. Đã tiếp tục phần làm dở theo lệnh điều phối. **Kiểm mã đạt; chưa nghiệm thu hình và nghe trong trình duyệt** vì phiếu cấm dev server, trình duyệt và mạng.

## Điều kiện đầu vào

Claude đã duyệt 189 ở commit repo cha `9f7cac0f` (thông điệp “Codex 189, reviewed”, đồng tác giả Claude Opus 5.5), duyệt 190 ở `7b677b5a` (“reviewed in the Lab at 1280x720”, cùng đồng tác giả). Báo cáo cũ của 190 chưa cập nhật kết quả duyệt; lịch sử commit là bằng chứng mới hơn.

Kit được đồng bộ ở `d7717ac`, ghim parent `7b677b5a`, `parentDirty: false`; có quick-settings, danh mục và preview. Không sửa hoặc đồng bộ lại kit. Đầu lượt có **31 mục thay đổi**, gồm triển khai dở và báo cáo dừng cũ; giữ phần đúng, hoàn tất test còn dở. [Kiểm đầu vào](192/preflight.json), [status đầu lượt](192/status-before.txt).

## Phần đã làm

- `src/app/{quick,app,input-router}.ts`, `app.css`: gắn bảng kit và hai nút Settings/Sound góc trên phải; chuột, F1, F2, Esc. Mở bảng dừng loop ngay, chặn chữ và lệnh từ giao diện; đóng đếm **3–2–1, mỗi số một giây**, giữ các lý do tạm dừng khác. Có vùng tránh cho thẻ chữ/số sát thương; dời cụm HUD hệ thống sang trái. Quit to title trả về màn Dragonhold có Play và cả hai nút; Play mở thẻ tốc độ và ván mới.
- `src/app/settings.ts`: lưu ngay vào `dragon-hold:settings:v1`, kiểm dữ liệu khi đọc lại. Đủ **Master, Music, Effects, Keyboard sound, Keyboard volume, Voice, Interface**. Mute hoặc Master = 0 đổi sang ảnh loa gạch chéo.
- `src/audio/{index,mix,music}.ts`: nối mức vào bus thật, Keyboard độc lập Effects; giọng đọc qua Master × Voice; Interface điều khiển tiếng giao diện và học. Slider có mẫu theo nhóm; Music có đoạn nghe ngắn qua bus nhạc.
- `src/app/keyboard.ts`: danh mục kit 190 theo thứ tự **Off, Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack, Dragonhold**. Dragonhold giữ tiếng gõ cũ để hoàn tác. Deep là mặc định tạm theo 189, không gán là mặc định đã được chủ dự án chốt.
- Firefly phát `key-*` cho chữ, `space-*` cho phím cách, đổi biến thể bằng kit, mức **Master × Keyboard volume**. Không phát phím khi Off, mute, Master = 0 hoặc Keyboard volume = 0. Hover/focus dùng preview kit **một giây**, chờ 150 ms; rời/chuyển/đóng tắt dần 30 ms. Tải trước riêng bộ đã lưu, cùng player với bảng; bảo vệ lượt tải cũ khi chuyển Off hoặc hủy ứng dụng.
- `tests/app/{quick-settings.test,settings-and-keyboard.test,keyboard-audio-fixture}.ts`, package/lockfile: DOM bằng happy-dom và WebAudio giả lập, dùng bảng/player kit thật. Sửa selector Quit còn dở và chờ tải đang chạy kết thúc trước khi khôi phục fetch trong dọn test. Bỏ qua `.pnpm-store/`, không xóa cơ sở dữ liệu cục bộ.

## Media

`public/assets/dragon-hold/audio/keys/`: **107 file không phải WAV** khớp từng byte nguồn `~/AudioLab/review/staging/keys-firefly/`, gồm **98 OGG** (91 biến thể + 7 preview), **8 keys-manifest.json** và dấu nguồn builder; **0 WAV**.

`public/assets/dragon-hold/ui/quick-settings/`: dùng lại **9 icon 180** bản 64 px cùng prompt, khung `panel-large.alpha.png` và nút `button.alpha.png` cùng prompt. Không thiếu icon, không sinh hoặc vẽ icon mới. [Hồ sơ chép media](192/media-copy.json) có **118 mục**, đối chiếu nguồn/mã băm đạt 118/118.

`.gitignore` mở đúng manifest phím để JSON đi qua Git; OGG/PNG và store vẫn bị bỏ qua. `media.md5` bổ sung **129 dòng** cho file chép, cả prompt; đối chiếu không sai mã băm nào. [Kiểm media và ván vàng](192/media-and-golden-audit.json). Không tạo âm mới, không sửa nguồn Firefly hoặc chuỗi xử lý 189. Claude thực hiện media:push.

## Hàng ẩn và giới hạn

**Không ẩn hàng âm thanh nào:** đủ kênh tương ứng. Settings có bốn tầng thật **Low, Medium, High, Ultra**, Resume và Quit to title.

Ẩn **Letter style, Effect strength, Word size và Preview** vì chưa có bộ hiệu ứng chữ tùy chỉnh tương ứng; **Reduced motion** vì chưa có cờ giảm chuyển động; **Show Vietnamese meaning, Show pronunciation** vì đang dùng quy tắc học tập, chưa có hai công tắc độc lập. Không thêm hàng giả.

**Quality áp dụng khi tải game lần tiếp theo**, nhãn `Quality (next launch)`. Map, terrain, model tier và renderer được dựng một lần ở khởi động; không dựng lại giữa ván hoặc bỏ tiến trình đang tạm dừng. Các mức âm, mute và lựa chọn phím áp dụng ngay.

## Kết quả kiểm

Lệnh đạt: `pnpm_config_verify_deps_before_run=false pnpm check`. Biến môi trường chỉ tắt bước pnpm tự kiểm/cài dependency trước script; script check giữ nguyên, không tải mạng. Lệnh pnpm check đầu tiên bị pnpm chặn trước kiểm vì muốn thay thư mục dependency trong môi trường không TTY; không cho phép cài lại.

| Kiểm | Kết quả |
|---|---|
| Kit | **92/92 file** khớp mã băm |
| Vitest | **58/58 file, 513/513 test**, 6,30 giây; 21 test mới |
| TypeScript strict, Vite build | Đạt; còn cảnh báo chunk trên 600 kB |
| Ván vàng | **10/10 test**; bốn ca giữ log và toàn bộ mã băm |
| Media nguồn, media.md5 | Không sai file nào; manifest được theo dõi, OGG/PNG bị bỏ qua |
| git diff --check | Sạch |

Ván vàng: `idle` **61222e57**, `b35-seed1` **8b16e8be**, `noTyping-seed2` **59192d7b**, `sloppy-hard-off-seed3` **4d27a14a**. Không đổi `src/sim`, `src/typing`, `src/content`, `tests/golden`, `src/kit`.

Lượt đầy đủ đầu tiên 512/513 do selector test Quit sai; sau sửa, chạy riêng 8/8 rồi toàn bộ đạt. Không có test thời gian đỏ ở lượt đạt, không cần chạy riêng ba lần. [Log check](192/check.txt), [log test bảng](192/quick-tests.txt).

Test bảng kiểm chuột/phím, pause/chặn chữ, 3–2–1, save/khởi động lại, danh mục/preview, đúng file key/space, Off/mute/zero và quit/play. Đây là **DOM và âm giả lập, không phải kiểm nhìn/nghe thật**. Lượt đầu lộ tải âm tiếp tục sau khi test khôi phục fetch, gây yêu cầu localhost bị sandbox chặn; đã sửa dọn test, lượt đạt không còn yêu cầu đó.

[Status cuối](192/status-after.txt) chỉ có mã, dependency test, manifest, danh sách media và tài liệu của phiếu. Không chạy lệnh Git có ghi, server, trình duyệt, đồng bộ kit hoặc media:push.

## Chủ dự án và Claude cần xem

Kiểm trình duyệt ở **1280×720 và 1920×1080**, màn tựa và trong trận: vị trí nút so với HUD/thẻ chữ, khung/nút, tương phản và tiếng preview/gameplay thực. Phiếu 180 còn ghi ngoại lệ loa bật/tắt chờ duyệt, nên dùng đúng ảnh không thay thế nghiệm thu mỹ thuật. Xem giới hạn Quality, nghe các bộ và chốt mặc định nếu cần; sau đó Claude chạy media:push.
