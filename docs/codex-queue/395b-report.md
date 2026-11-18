# Phiếu 395b — Dựng lại bố cục tuyệt kỹ Mộc

Ngày 16/11/2026, sau phiếu 397 trong cùng làn. **Đã sửa công thức; kiểm kiểu và probe CPU 100 quái PASS. Chưa nghiệm thu hình ảnh trong host** vì trình duyệt không khả dụng và sandbox chặn ghi thư mục review.

## Tệp và thay đổi

Chỉ sửa bốn tệp trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/src/lab/`:

- `wood-ult-sprites.ts`: tăng phần vành từ 108 lên **144 cụm**, chia hai hàng so le tại khoảng 25,4 và 28,1 m. Thẻ rễ ở vành tăng cả rộng/cao **2,8 lần** so công thức cũ; chiều cao thẻ trước giới hạn màn hình khoảng **7,92–15,65 m**. Probe xác nhận các cụm kề nhau chồng lấn. Giảm phần trong từ 72 xuống **36 đoạn rễ nằm phẳng**, tạo sáu nhánh liên tục từ tâm ra vành. Giảm độ đậm lớp đất lặp từ 0,60 xuống 0,32 để phần trong thoáng hơn.
- Mầm vẫn ở **đúng tâm vùng tung chiêu**, dùng lại một cụm rễ và ba lá đã cắt. Tăng đế từ 2×1 lên 7,5×4,8 m; lá từ 1,8–2,2 lên 4–4,8 m, hướng theo camera để đọc rõ ở góc trên. Chỉ mạch sáng của ba lá tâm được vượt HDR; các thành phần Mộc còn lại giữ trần 0,9 mỗi kênh. Không đổi bloom toàn cảnh.
- Thêm giới hạn theo hình chiếu cho các thẻ instance: hộp bao tối đa **14% diện tích khung**, dưới yêu cầu 15%; riêng lá/hạt tối đa 14% mỗi chiều. Giới hạn tính cả góc xoay, độ sâu phối cảnh và thẻ sát camera. Vùng bảo vệ caster làm alpha thẻ dựng/lá bằng 0 trên hộp thân, với mép mềm bên ngoài; vòng chân và rễ nằm đất vẫn ở dưới thân.
- `wood-ult-layered.ts`: cập nhật vị trí caster hiện tại cho vùng bảo vệ và thêm `clock` vào báo cáo để chụp đúng thời gian công thức. Không đổi đường trói, sát thương hoặc lịch âm.
- `wood-ult-check.mjs`: giữ probe 395, thêm kiểm bố cục, nhánh hướng ra vành, tâm mầm, hộp bảo vệ và giới hạn hình chiếu.
- `wood-ult-review.mjs`: lấy đúng **0,600 / 0,720 / 0,840 s** theo `clock`, cộng tụ/trói/cuối trói/vỡ/tan. Ghép ảnh đích cạnh mốc 0,840 s và lúc trói; thêm bảng đối chiếu cả cửa sổ 0,60–0,84 s. Giữ tên đầu ra `395-*` để ghi đè bản cũ; nội dung `ABOUT.md` trỏ về báo cáo này.

Tái dùng nguyên ảnh riêng của repo trong `art-src/lab/vfx/wood-ult/`, không sinh hoặc sửa media. SHA-256 của **16 tệp bảo vệ** nguyên vẹn: `skills-main.ts`, năm tệp `anim-r1-*`, tám tệp `ice-ult-*`, âm và tint Mộc. Phần nối của 397 được giữ nguyên.

## Kiểm tra

Đã chạy từ worktree:

```sh
node src/lab/wood-ult-check.mjs
node --check src/lab/wood-ult-review.mjs
```

- TypeScript strict, `noUncheckedIndexedAccess`: **0 chẩn đoán**, gồm `skills-main.ts` hiện có và các phụ thuộc; không chạy build hoặc bộ test game.
- **100 lần trói, 100 tint**; một quái chết sớm được huỷ hình/tint, **99 quái còn lại nhận đúng một cú** sau 3 s, sai số dưới một bước 60 Hz. Ca xoá/tung lại, cảnh rỗng và vượt trần giữ PASS.
- Số sự kiện âm giữ như 395: tụ 1, mọc 5, nứt 1, vỡ 6, đuôi 1; tám file âm thật. Không đổi nguồn, adapter hoặc mức âm.
- Vẫn **4 kho/lượt vẽ cấu trúc**, riêng trói 2; khi 100 mục tiêu trói: 184 thẻ rễ/mầm, 130 vòng chân, 3.112 lá/hạt/mảnh/bụi và một mặt đất.
- Kiểm toán học: **12 trường hợp bảo vệ** (hai góc, ba tỷ lệ khung, hai vị trí caster), **180 trường hợp chiếu thẻ** ở nhiều khoảng cách/góc xoay. Diện tích hộp bao lớn nhất trong mẫu khoảng 7%; đây không phải số đo pixel từ GPU.
- CPU p95 riêng `wood.update`: khoảng **0,0243 ms** ở lượt chốt; không phải thời gian khung game hoặc bằng chứng FPS.

## Phần chụp chuyển Claude

CUA trả `Browsers: Error: The browser access host is unavailable`. Mở ghi `typing-game-review/owner-review/2026-11-16/tu-tien/ult-wood/ABOUT.md` bị `Operation not permitted`. Vì vậy **chưa ghi đè ảnh 395, chưa cập nhật ABOUT/index**, không có capture mới cần dọn. Không dùng cách khác để vượt chặn.

Khi Claude có browser và quyền ghi, phục vụ **đúng worktree đã sửa**, rồi chạy; thay cổng nếu host thực tế khác 3148:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3148/stress.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/wood-ult-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Script không mở server/build; từ chối host thiếu `clock` của 395b. Nó ghi hai bảng pha, hai bảng cạnh ảnh đích, hai bảng cửa sổ trúng, số liệu và ABOUT trong đúng thư mục yêu cầu rồi cập nhật index. Script mới qua kiểm cú pháp, chưa chạy browser; cần xem ảnh và lỗi shader/console sau khi chạy.

**Owner cần xem:** vành có thực sự dày/liền và đạt bố cục ảnh đích; mầm có đọc rõ ở góc trên; vùng bảo vệ caster có tạo khoảng hở dễ thấy; lá còn chắn tay/đầu ở góc sau lưng; độ nặng GPU do tăng diện tích chồng lớp. Sóng vẫn 26 m/s từ 0,6 s: ở mốc 0,84 s vành 30 m chưa mọc đủ; bảng lúc trói dùng để đối chiếu toàn vòng. Cú vỡ gây sát thương vẫn sau 3 s trói như 395. Host stress hiện chỉ có 87 mục tiêu thật và 13 walker trang trí; không gọi đó là phép đo GPU 100 quái trói.

Chưa xác minh GLSL/GPU, nghe âm, chuyển động hoặc chấm 8,5 trong host. Không sửa `skills-main.ts`, mã hoạt ảnh 397, game chính, scripts/tests hay docs game. Không staging media, đổi nhánh, commit, push, reset, clean hoặc stash. Hạn mức lúc nhận còn 62%, không gặp giới hạn quota hoặc giờ bắt buộc chờ.
