# Làn 6 · Quái chết, trúng đòn, choáng và trói

Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`, gốc `c97d2aa`. Chỉ sửa phạm vi phiếu; không lệnh Git ghi, không build, không mở trình duyệt/cổng mạng.

1. **Bảng ghép:** tạo `src/lab/foe-flipbook-fx.ts`, tái dùng 15 atlas đã chốt qua `FlipbookPlayer`/`FlipbookLibrary`/`FlipbookPool`. Đúng loài, dự phòng khói mực, ba lớp boss ở 0 / 0,15 / 0,4 giây, ba mức trúng, hướng đòn, pivot và fps manifest. Chiều rộng bằng 1,5 lần bề ngang thân; khói trộn thường, màu mực tối. Choáng theo đầu, trói theo thân; huỷ khi hết hạn/chết/đổi serial. Phá thế một lần cho tinh anh/boss. Kiểm việc 1: 12 test qua trước khi làm tiếp.

2. **Đám đông và lớp cũ:** xô 50 ms chọn tối đa 10 cái chết, 8 hình trúng, ưu tiên bậc rồi khoảng cách chiếu tới giữa màn hình; tối đa 12 trạng thái. Boss dành chỗ và phát ngay khung chết; những cái chết thường được chọn khi xô đóng. `death-fx.ts` chỉ bỏ mảnh sáng/vỡ, mực và sợi khí khi flipbook sẵn sàng; giữ chớp, vòng sốc, vết đất, quầng đất và đốm linh khí của đường tan Kiếm 7. Vượt xô hoặc atlas còn lạnh/tải lỗi dùng đủ lớp cũ cho lần chết đó. `?deathfx=old` giữ đường chết cũ và tắt toàn bộ flipbook quái mới. Kiểm việc 2: 18 test qua; kiểm tải đông tái dùng snapshot, vector và bộ đệm, không tạo thêm mảng Float32 hay bể sau khi ấm.

3. **Bộ nhớ:** chỉ nạp atlas cần dùng; giữ bể và giải phóng texture sau 20 giây kể từ mốc muộn hơn giữa lần dùng cuối và lúc sprite cuối hết hạn. Kiểm nạp lại, hết hạn chính xác và KTX2 lỗi quay về PNG đã qua. Toàn bộ 15 atlas: khoảng **223,5 MiB RGBA mức gốc; 298 MiB gồm mipmap**, chưa gồm model/bể dựng hình. Không tạo KTX2: `tools/vfx-flipbook/run.sh` hiện chỉ có `upgrade` dựng lại atlas từ nguồn, chưa có lệnh chỉ nén atlas hiện hữu; giữ nguyên PNG và manifest. Bộ kiểm giới hạn `beast/`, `boss/`, `mech/`: **32 task entries, 0 problems**.

4. **Kiểm cuối:** `npx --no-install tsc --noEmit` sạch; `npx --no-install vitest run --maxWorkers=4`: **115 → 116 file, 1.328 → 1.351 test**, tất cả qua; `git diff --check` sạch. Bộ mới có 23 test, gồm manifest thực và vòng đời texture.

**File:** trong worktree, thêm `src/lab/foe-flipbook-fx.ts`, `tests/lab/foe-flipbook-fx.test.ts`; sửa `src/lab/death-fx.ts`, `src/lab/events.ts`, `src/lab/skills-main.ts`. Báo cáo duy nhất ở `docs/codex-queue/lane6-report.md` của repo cha. Không sửa flipbook chung, sim/content, sound, PNG hay tạo media mới.

**Claude cần xem ở lab 3146:** quay từng loài và boss, so A/B `?deathfx=old`; kiểm cỡ/pivot ở camera chơi, khói mực trên nền sáng, ba nhịp boss, hướng vệt trúng, choáng/trói theo thân và tắt đúng lúc; tải đông 10/8/12; lần đầu atlas còn lạnh và nạp lại sau 20 giây. Chưa có video, đo GPU thực hay phán quyết 8,5 vì phiếu cấm trình duyệt/cổng mạng.

**Điểm nối cần giữ đồng bộ:** herd chưa có getter loài, greybox chưa công khai cỡ thân và callback chết giữ chưa trả target. `skills-main.ts` đọc chỉ đọc `herd["sp"]` theo thứ tự SPECIES hiện hữu, `greybox["beastSize"]` và `victims["deathRgb"]`, giữ target qua `herd.onDie`; không đoán loài từ bậc. Nếu các API nội bộ này đổi, phải cập nhật điểm nối. Greybox/swarm đọc loài và serial thật từ world.
