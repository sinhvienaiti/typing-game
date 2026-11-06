# B4 · Chất liệu cut-in · 07/11/2026

**Đã ghép mã vào đường CutIn hiện có; chưa đóng B4 cho phím 7 và nghiệm thu hình.** Làm trên `games/.wt-ic-lab-all`, nhánh `codex/lab-all`, sau B3. Giữ nguyên các thay đổi B3 có sẵn.

## Đã làm

Các đường dẫn mã dưới đây tính từ worktree:

- `src/lab/cutin-materials.ts`: chọn đúng lớp theo bảng cho 14 hệ; dùng `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer`. Nạp lười manifest và chỉ atlas được chọn; không nạp clip ấn dấu. Canvas trong khung, sau ảnh/chữ, trước nền; shader chỉ chỉnh phép ghép alpha và chặn màu lớp mới ở 0,9 mỗi kênh.
- `src/lab/cutin.ts`: khởi động/vẽ/dừng lớp theo đồng hồ hiện có; thay các chi tiết chuyển động cũ bằng clip. Mở trong 0,2 s đầu, thoát trong 0,14 s cuối; không đổi thời lượng hay các mốc âm. `?cutinmat=0` dùng nhánh cũ, không tạo renderer hoặc nạp atlas.
- `src/lab/skills-main.ts`: truyền cờ A/B và hệ hiện tại vào CutIn ở phím 5; không đổi đường thi triển phím 7.
- `tests/lab/cutin-materials.test.ts`: 35 test node cho chọn lớp/mốc, A/B, nạp lười, atlas đến muộn, huỷ/kết thúc/tái khởi động từng lớp, pivot, resize, alpha và đồng hồ âm. Qua 1.000 khung đã ấm vẫn cùng pool, bộ đệm, scene, camera và renderer; không tạo pool/nạp atlas/resize lại trong vòng vẽ. Đây không phải phép đo heap hay GPU.

## Kiểm tra

- Trước: `npx --no-install vitest run --maxWorkers=4` — **119 file / 1.393 test qua**.
- Sau: cùng lệnh — **120 file / 1.428 test qua**.
- `npx --no-install tsc --noEmit`: sạch. `git diff --check`: sạch.
- Không build, mở cổng, mở trình duyệt, tạo ảnh/âm hay sửa `art-src`; không chạy lệnh Git ghi.

## Chờ và phần anh cần xem

- **Ấn dấu: chờ clip.** Không dùng `cutin-seal-stamp-splash` vì lộ cán con dấu; âm và hình ấn cũ giữ nguyên.
- **Phím 7:** source hiện chỉ có một `new CutIn` và `cutin.start` trong `startUltimate` của phím 5. Phím 7 đi qua `MyriadSwordsFx`, chưa có cut-in chân dung để nối. Đã báo điểm lệch bối cảnh; không tự thêm một cut-in/timeline mới. Cần điều phối xác định hook phím 7 trước khi đóng B4.
- **Chưa nghiệm thu hình/GPU:** ticket cấm trình duyệt nên chưa quay video hoặc chấm 8,5. Ảnh C hiện là JPG có nền kín; canvas đặt sau ảnh đúng thứ tự được chốt sẽ chỉ lộ ở vùng mask/lúc ảnh chưa hiện hết. Cần xem A/B trong host; nếu cần chất liệu hiện quanh nhân vật trên toàn khung, cần ảnh tách nền/matte hoặc quyết định lại cách ghép. B4 không sửa nguồn ảnh.
