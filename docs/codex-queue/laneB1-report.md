# Làn B1 · Hào quang tinh anh và boss trong lab

Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Chỉ sửa phạm vi phiếu; không lệnh Git ghi, không build, không mở trình duyệt/cổng mạng, không sửa media hay manifest của làn A.

1. **Đã nối:** `elite-aura-ironhide-loop` cho `thiet-giap-tru` bậc 2; chọn tối đa 8 theo khoảng cách chiếu tới tâm màn hình. Boss `thiet-boi-lang-vuong` có `captain-aura-ground-loop` riêng, không tranh chỗ với tinh anh. Máu ≤ 50% bật `boss-frenzy-aura-loop`; lần đầu đi từ trên xuống mốc này mở đúng một timeline `boss-phase-roar-shockwave` + `boss-phase-aura-flare`. Hồi máu rồi qua lại mốc không phát lại; đổi đời/serial cho phép lần mới.

2. **Vòng đời và bộ nhớ:** boss mới xuất hiện phát vortex + fog một lần ở vị trí sinh, kể cả boss gọi bằng V trong greybox. Hủy ngay khi chết/dừng; hủy khi mất khỏi nguồn hoặc đổi serial, không chuyển hiệu ứng cũ sang model mới. Cái chết chờ xô 50 ms chỉ hủy đúng serial. Đổi chế độ bầy/reset xóa trạng thái cũ. Tái dùng `FoeFlipbookFx`, library/player/pool hiện hữu, nạp lười, giữ snapshot/bộ đệm sau khi ấm, giải phóng atlas sau 20 giây không cần dùng. Giữ sẵn atlas chuyển pha khi boss còn trên 50% để boss sống lâu vẫn chuyển ngay khung qua mốc; one-shot hết hạn không tự nạp lại.

3. **Lớp và công tắc:** `?foeaura=0` tắt cả 7 lớp của B1, không nạp atlas hào quang; các phản ứng quái trước đó vẫn dùng được. Art giữ pivot/fps/mode từ manifest, depth lùi sau model, giữ tag mask hiện hữu. Hệ số sáng: tinh anh 0,45; frenzy 0,30; các lớp boss khác 0,12, kể cả chồng entrance và chuyển pha vẫn dưới 0,9/kênh cho một boss. Swarm mặc áo trên herd đang hiển thị, không vẽ trùng thêm bản sim.

4. **Kiểm:** trước **116 file / 1.351 test**; sau **117 file / 1.368 test**, tất cả qua. Thêm **17 test** trong `tests/lab/foe-aura.test.ts`, cập nhật kiểm manifest từ 15 lên 22 clip. Hai file kiểm hiệu ứng: **40/40 qua**. `npx --no-install tsc --noEmit` và `git diff --check` sạch. `npx --no-install vitest run --maxWorkers=4`: lượt cuối **mã 0, 51,81 giây**. Một lượt trước đó qua mọi test nhưng worker timeout `onTaskUpdate`; chạy lại nguyên lệnh, không đổi mã/cấu hình, đã sạch.

**File đã sửa/thêm:** trong worktree: `src/lab/foe-flipbook-fx.ts`, `src/lab/skills-main.ts`, `tests/lab/foe-aura.test.ts`, `tests/lab/foe-flipbook-fx.test.ts`; báo cáo này ở repo cha. Không cần sửa `events.ts`. Điểm nối herd đọc `hp` nội bộ với HP tối đa 60 của boss stand-in hiện tại; greybox đọc `hp/hpMax` và serial thật.

**Chờ tính năng:** `elite-aura-frenzy-loop`, `elite-aura-regen-loop`, `captain-aura-loop`: lab hiện không cung cấp đúng trạng thái cuồng nộ, hồi máu hoặc đội trưởng cho các quái này. Không gán suy đoán.

**Chủ repo cần xem:** A/B `?foeaura=0` ở camera chơi; 8 tinh anh gần tâm, boss luôn có lớp dưới chân; gọi boss bằng V trong greybox, đánh qua 50%, giết và sinh lại. Kiểm cỡ/pivot, độ sáng trên nền sáng, mặt và chữ trên đầu không bị che. Atlas lạnh giữ thời điểm gốc: khi tải xong chỉ hiện phần thời gian còn lại, không phát lại từ đầu. Chưa có video, đo GPU hay phán quyết hình ảnh 8,5 vì phiếu cấm trình duyệt/cổng mạng.
