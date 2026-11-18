# Phiếu 433e — kiếm Kim kết hợp

Ngày 17/11/2026. Đã hoàn thành phần triển khai và các cổng kỹ thuật của phiếu trong lab `localhost:3148`. Không commit, không chạy build hoặc bộ test của game, không dừng server.

## Đã sửa

- `games/.wt-ic-lab-all/src/lab/metal-sword-look.ts`: mặc định `mix`; 48 kiếm nhỏ dùng năng lượng vàng trong mờ, lõi hẹp chạy dọc lưỡi, mép mềm và tan dần. Hệ số kiếm nhỏ của kiểu kết hợp là `0,26`, bỏ nhân tăng sáng `1,5` của bản B; alpha biến thiên `0,224–0,8`. Kiếm lớn dùng lớp aura có fresnel quanh mô hình thật.
- `games/.wt-ic-lab-all/src/lab/metal-ult-rain.ts`: loại bề mặt kim loại của các instance nhỏ trong kiểu kết hợp; giữ nguyên mô hình Tripo, vật liệu và ánh sáng của kiếm lớn; bật hạt aura cho kiếm lớn. Giữ các lớp hạt va chạm và bụi tan hiện có. Không đổi số kiếm, quỹ đạo, thời điểm, sát thương hoặc camera.
- `games/.wt-ic-lab-all/src/lab/metal-ult-mix-review.mjs`: kịch bản chụp/đo có thể chạy lại, kiểm hai tham số A/B, xuất tấm xem và clip.

`?swordLook=aura` vẫn hiện mô hình thật cùng aura trên mọi kiếm. `?swordLook=energy` vẫn thay mọi kiếm bằng năng lượng và giữ hệ số sáng của bản B để đối chiếu. Đã chụp và mở cả hai, xác nhận mô hình nền hiện ở `aura` và ẩn ở `energy`.

Kiếm đã cắm đất vẫn được vẽ ở trạng thái planted. Ánh sáng chỉ suy giảm cùng phép tan `smoothstep(2,95; 3,95)` và còn hệ số `0,4` trên những phần chưa tan; toàn bộ 49 instance trả kho tại 4 giây.

## Vòng sửa và kiểm hình

Một vòng sửa hình, nằm trong giới hạn ba vòng. Đã mở sáu ảnh tại 1,2 / 2,4 / 3,0 giây, góc chơi Alt+1 và sau lưng Alt+2, nền `#353a40`; đối chiếu với `metal-sword-look-AB.jpg` và nửa trái của `ult-storyboard-samples-431.jpg`. Kiếm lớn là trục sáng chính ở hai góc; kiếm nhỏ nhẹ và trong hơn bản B. Không tạo tài nguyên mới: tái sử dụng hình học Tripo và các atlas có sẵn theo quyết định của owner.

Đã sửa phép đo trong cùng vòng: cách lấy hiệu hai ảnh hậu kỳ bị nhiễu từ các lần render, từng báo tín hiệu giả khi kiếm lớn chưa xuất hiện nên **không dùng để nghiệm thu**. Phép đo cuối render riêng nhóm kiếm nhỏ và kiếm lớn lên GPU target RGBA half-float nền đen, giữ camera và đèn của cảnh. Lấy đỉnh độ chói tuyến tính `Y = 0,2126R + 0,7152G + 0,0722B`, **trước bloom và tone mapping**. Đây là tỷ số bức xạ của kiếm, không phải tỷ số RGB của ảnh đã nén sáng. Nhóm nhỏ gồm tất cả kiếm nhỏ, kể cả chồng lớp. Kiếm lớn tại 1,2 giây đo đúng bằng 0.

| Góc | Giây | Đỉnh nhóm nhỏ | Đỉnh kiếm lớn | Lớn/nhỏ | Trắng toàn khung |
| --- | ---: | ---: | ---: | ---: | ---: |
| Alt+1 | 1,2 | 0,7600 | 0 | Chưa xuất hiện | 0% |
| Alt+1 | 2,4 | 0,7172 | 5,9522 | **8,30×** | 0% |
| Alt+1 | 3,0 | 0,7947 | 5,1268 | **6,45×** | 0% |
| Alt+2 | 1,2 | 0,6987 | 0 | Chưa xuất hiện | 0% |
| Alt+2 | 2,4 | 0,9708 | 3,9582 | **4,08×** | 0% |
| Alt+2 | 3,0 | 1,0222 | 3,9844 | **3,90×** | 0% |

Vùng trắng được đếm trên ảnh toàn cảnh khi cả ba kênh sRGB ≥242/255. Tối đa trên cả 96 khung clip: **0%**, dưới mức 6%.

## Kiểm chứng

- Kiểm kiểu: `node node_modules/typescript/bin/tsc --noEmit` tại worktree, **0 lỗi**. Dùng trực tiếp trình biên dịch đã có vì `pnpm exec` từ chối liên kết `node_modules` sang game chính; không cài lại dependency.
- Chrome headless, 1280×720, DPR 1, chất lượng mặc định của lab là High; GPU `ANGLE Metal Renderer: Apple M4`.
- Cảnh 100 quái: 87 TargetField + 13 walker. Cách đo như `metal-ult-rain-review.mjs`: từng khung mô phỏng, CPU rồi `readPixels` một pixel chờ GPU; 208 mẫu khi đồng hồ từ 0,6 đến dưới 4 giây.
- **P95 toàn khung 6,20 ms**, P95 CPU 1,20 ms; đạt ≤16,7 ms. Tối đa 80 draw call và 2.020.127 tam giác. Đây là thời gian xử lý có chờ GPU, không phải khoảng cách rAF.
- Không có exception hoặc lỗi tải tài nguyên kiếm mưa. Có cảnh báo ngoài phạm vi về nhiều KTX2Loader và `drawImage` của `metal-slash-arc` / `metal-crescent-sym`; giữ nguyên các hệ thống đó.
- MP4: H.264, 1280×720, 24 fps, 96 khung, **4,000 giây**, không âm thanh. Đã mở tấm xem chuyển động 12 khung và ảnh giao nộp.

## Giao nộp

- [Ảnh so sánh với phân cảnh và A/B](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-mix.jpg).
- [Clip 4 giây](/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-sword-mix.mp4).
- Đã thêm dòng `metal-sword-mix` vào `owner-review/2026-11-17/tu-tien/ABOUT.md`.
- Tấm kiểm nội bộ giữ ở `captures/tu-tien/metal-sword-mix-433e/`: `round-1-sheet.jpg`, `motion-contact.jpg`, `look-parameter-contact.jpg`, kèm `ABOUT.md`.
- Đã dọn **138/138 khung thô, 166,191 MB** bằng `tools/capture-prune/prune.mjs`, xem trước rồi mới `--apply`; giữ ba tấm kiểm, không xóa ảnh A/B hoặc file của agent khác. Đã xác nhận thư mục phiếu không còn PNG thô.

Không tạo ảnh/âm thanh mới vì phiếu chỉ phối hai kiểu sẵn có. Không cập nhật chỉ mục review tự sinh vì phiếu giới hạn văn bản ngoài code vào báo cáo này và `ABOUT.md`. Chưa có chấm mù 8,5; owner cần xem ảnh và clip để chốt cảm nhận ánh sáng của kiếm lớn so với các kiếm nhỏ.

Lệnh tái kiểm: chạy từ `/Volumes/SS990TPRO/htdocs/typing-game`, chỉ dùng server đang có:

```sh
ART_MAGICK=/opt/homebrew/bin/magick ROUND=1 FINAL=1 .local/bin/heavy.sh --perf node games/.wt-ic-lab-all/src/kit/tools/cdp-run.mjs games/.wt-ic-lab-all/src/lab/metal-ult-mix-review.mjs --width=1280 --height=720 --dpr=1
```

Đặt `CHECK_LOOKS=1` thay cho `FINAL=1` để chỉ chụp hai tham số A/B. Mỗi lượt tạo thư mục khung thô riêng; prune thư mục đó sau khi xem.
