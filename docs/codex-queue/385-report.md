# Phiếu 385 — Ult băng ghép lớp v2

Ngày 15/11/2026. **Đã dựng phần mã trong lab; chưa hoàn tất giao nộp và chưa nghiệm thu.** Sandbox chặn mở máy chủ, điều khiển Chrome và ghi thư mục review. Chưa có ảnh v2, chưa có số đo ms trước/sau, chưa thể kết luận đẹp ngang video hoặc đạt 60 FPS. Không chấm thay owner.

## Đã sửa

- `games/.wt-ic-lab-all/src/lab/ice-ult-layered.ts`: giữ runner v1 để đối chiếu, mặc định dùng v2. Rừng 64 cụm tinh thể 3D đa diện kín, bốn biến thể gồm 5 / 7 / 8 / 6 trụ mỗi cụm; phân bố trên sân và thêm mật độ quanh các nhóm quái đông. Mỗi cụm cao 1–6 m, mọc theo vòng sóng từ người tung chiêu. Đây là lưới 3D theo yêu cầu trực tiếp của phiếu, không phải thẻ hình hoặc tượng thú.
- Vật liệu băng có cạnh sáng Fresnel, lõi lam nhạt, vết bao thể và khúc xạ giả từ texture băng có sẵn. Thân giới hạn từng kênh ở 0,9. Một lần bùng lõi HDR 4 kéo dài 0,09 s, trùng cú trúng chính đầu tiên; không thêm bloom.
- Mặt băng trong liên tục trên phần nền thật của sân, texture từ `art-src/lab/vfx/ice/ice-ground-mark.atlas.png`, hiện theo sóng rồi tan 2,5 s. Ánh phản chiếu là ánh giả nhẹ theo hướng nhìn, không có bước chụp cảnh hoặc khúc xạ màn hình tốn thêm lượt render.
- Vỏ băng 3D kín, tối đa 128 quái, kích thước theo bán kính và chiều cao thật. Vỏ chỉ được tạo khi quái còn sống tại lúc đóng băng; huỷ nếu quái chết sớm. Vỏ và mảnh vỡ không sót giữa các lần tung chiêu.
- Lấp lánh tại các đỉnh tinh thể, tuyết rơi từ `ice-sparkle`, sương thấp từ `ice-wave` dùng chế độ khói. Hai pool mới dùng chung texture hiện có. Cần nhìn trong lab để xác nhận nguồn này đọc đúng vai tuyết và sương, độ ôm vỏ băng từng loài, độ trong và vết nối của nền.
- Giữ đường gọi chớp màn, khựng hình, phản ứng quái, số sát thương và âm băng của v1. Các lưới mới dùng mặt nạ chữ sẵn có để giữ vùng từ cần gõ dễ đọc.
- `docs/games/tu-tien/skills/VFX_LIBRARY.md`: ghi các thành phần mới và giữ video cũ trong danh sách dự phòng.

Không sinh ảnh, âm hoặc video mới; không xoá media, đưa media vào Git, đổi nhánh, commit hoặc push. Không sửa `skills-main.ts`, code game chính, script hoặc test của game.

## Năm pha và các số đã đặt trong mã

| Pha / phần | Thời gian / giới hạn |
| --- | --- |
| Tụ lực | 0,6 s; charge, ấn dưới chân, hạt tụ về tay của v1 |
| Phát chiêu | release và vành tinh thể quanh người tung của v1 |
| Lan | 26 m/s; đi hết 30 m trong 1,153846 s; mặt băng và tinh thể xuất hiện theo khoảng cách |
| Rừng tinh thể | 64 cụm; mọc 0,2 s, giữ đủ 3 s, vỡ 0,4 s |
| Trúng | Trói quái 3 s như v1, vỏ kín và mảnh vỡ; một cú nhấn chính duy nhất |
| Dư âm | Nền tan trong 2,5 s; sương và tuyết có đường vào/ra mềm |
| Lưới | Bảy lượt vẽ lưới mới: bốn biến thể rừng, vỏ, mảnh, nền; cộng các pool hạt và các lớp v1 còn dùng |

Vùng phép vẫn có bán kính 30 m. Rừng và mặt băng đặt trên nền sân hiện có (phần trong hình chữ nhật x = −18…18, z = −16…6), không dựng thêm cảnh hoặc nền ngoài sân. Tinh thể là các instance 3D nên cùng hình khối cho Alt+1–4; điều này chưa thay cho kiểm hình bốn góc thật.

## Âm thanh: còn thiếu nối host

Đã thêm callback tuỳ chọn `IceUltHost.sound(event, at, pitch)` với bốn sự kiện riêng: `crystal-grow`, `crack-spread`, `crystal-shatter`, `cold-wind`. Pitch 0,96–1,04; grow/shatter được gom cách nhau tối thiểu 0,16 s, không phát một tiếng cho mỗi quái. `__lab.iceUlt().last.soundEvents` đếm yêu cầu và `soundWired` cho biết có adapter hay chưa.

**Hiện `soundWired` là false trong host thật.** Instance `LabSound` dùng chung nằm kín trong `src/lab/skills-main.ts`; file đó không thuộc phạm vi được sửa. Vì vậy bốn lớp âm mới chưa phát; chỉ âm băng v1 còn hoạt động. Không tạo AudioContext thứ hai, không chặn prototype và không gọi lại toàn âm ultimate cho từng lớp. Để hoàn tất cần cho phép thêm adapter tại đối tượng host tạo `IceUltLayered` trong `skills-main.ts`, gọi thư viện băng có sẵn qua bus chung (`LabSound.on` / `playTake`) để giữ mute, headroom, ghi âm và pitch variation. Chưa chọn hoặc nghe các take mới thay owner.

## Kiểm tra đã chạy

Chỉ kiểm file nguồn và hình học / timeline bằng Node, không chạy build hoặc bộ test game:

- Transpile TypeScript: không lỗi cú pháp. Kiểm kiểu riêng file thay đổi với chế độ strict và `noUncheckedIndexedAccess`: 0 chẩn đoán ở file này.
- Bốn biến thể: 180 / 210 / 288 / 180 tam giác; kiểm ghép cạnh cho thấy mọi cạnh đều có đúng hai mặt; toạ độ và normal hữu hạn.
- Kịch bản CPU riêng với 100 mục tiêu: một mục tiêu chết trước sóng, 99 mục tiêu còn lại đóng băng và vỡ đúng một lần; đúng một sự kiện trúng chính. Có kiểm huỷ vỏ, khoảng trống instance và tung lại không giữ dữ liệu cũ.
- 64 cụm trong kịch bản trên cao **1,068–5,897 m**. Bốn loại sự kiện âm đều được phát vào callback thử; đây không phải kiểm nghe âm trong trình duyệt.
- Các vật liệu lưới có mặt nạ chữ dùng chung. Chưa biên dịch shader bằng WebGL hoặc kiểm hình / nghe âm thật.
- Kiểm tra cuối: mục tiêu chết sớm rồi hồi sinh không nhận lại vỏ trong cùng lượt; `iceVersion=v1`, mặc định v2, công tắc `ultIce=video` và cờ báo audio / asset chưa sẵn sàng đều đúng. Kiểm kiểu riêng file sau các sửa cuối vẫn 0 lỗi.

## Hiệu năng và ảnh: đang bị chặn

| Bản | CPU ms p50 / p95 | Tổng ms p50 / p95 | FPS | Kết luận |
| --- | --- | --- | --- | --- |
| V1, `stress.html`, 100 quái | Chưa đo | Chưa đo | Chưa đo | Chưa có baseline |
| V2, cùng điều kiện | Chưa đo | Chưa đo | Chưa đo | Chưa xác minh ≥ 60 FPS / p95 ≤ 16,7 ms |

Lỗi thực tế trong lượt này:

1. `pnpm exec vite` không mở được SQLite trong store. Gọi trực tiếp Vite đã cài với cache ở `/private/tmp` cũng bị sandbox chặn: `listen EPERM: operation not permitted 127.0.0.1:3008`. Không có server mới còn chạy.
2. Công cụ CUA báo browser access host không khả dụng; yêu cầu dùng Chrome tiếp theo bị từ chối: `Computer Use was not approved to use Google Chrome`. Không chuyển sang cách điều khiển khác để vượt chặn này.
3. Tạo thư mục đích `.../typing-game-review/owner-review/2026-11-15/tu-tien/ult-ice-layered/v2/` bị `Operation not permitted`. Chưa tạo được ảnh hoặc `ABOUT.md` tại đó; không đặt capture vào `docs`, `public` hoặc `art-src` thay thế.
4. Đã chạy `node scripts/review-index.mjs`; lỗi `EPERM` khi ghi `typing-game-review/INDEX.md`, nên index chưa cập nhật.

Mẫu nội dung `ABOUT.md` để ghi khi đường dẫn review được mở quyền:

```text
purpose: So sánh ult băng v1, v2 và video cũ ở góc trên và sau lưng, phiếu 385
made-by: Codex, phiếu 385
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/385-report.md
delete-when: Sau khi owner duyệt v2 và không còn cần đối chiếu
```

## Phím lab và cách tiếp tục

- Phím **8**, chọn ultimate băng mục 12: v2 mặc định. **Y** đổi bản lớp / video cũ; media video cũ giữ nguyên trong `art-src/lab/vfx/ult/`.
- **Alt+1** góc trên; **Alt+2** sau lưng; **Alt+3** sau lưng nghiêng 25°; **Alt+4** góc bên. **R** đặt lại sân.
- Thêm `iceVersion=v1` vào query của trang rồi tải lại để chạy lại bản lớp v1; bỏ query này để trở về v2. Đây chỉ là cách dựng đối chứng trong lab.
- API hiện có: `__lab.iceUlt("layered")` hoặc `__lab.iceUlt("video")`; `__lab.showcase("ult-ice-cold-silence")` để tung; `__lab.viewMode("top" | "behind" | "behind25" | "side")` để đổi góc. `__lab.iceUlt().last` có `clusters`, `clusterHeightM`, `assetsReady`, `soundEvents`, `soundWired` và `truncatedShells`.
- Đo tại `stress.html?fixed=1&ui=0&dpr=1&herd=march`, không bật `auto=1` vì nó tự tung Ngũ Lôi. Cảnh stress hiện có 87 quái của host và 13 walker trang trí; walker không thuộc `TargetField` nên không nhận trói / sát thương. Giữ nguyên workload này khi so trước/sau và ghi rõ điều đó.
- Tung một lượt để tải bộ băng, đợi `last.assetsReady === true`, đặt lại và đo các lượt sau khi GPU đã ấm. Giữ cùng trình duyệt, độ phân giải, DPR, góc, quái, mốc thời gian và các cờ mặc định giữa v1/v2. Dùng `__lab.perf(n)` cho CPU / tổng có chờ GPU, lấy p95 qua nhiều lượt; kiểm thêm vòng rAF thật cho FPS. Công cụ tham khảo: `scripts/visual/scenarios/lab-perf-stress.mjs`.
- Chụp ít nhất sáu ảnh cùng điều kiện: v1, v2, video cũ × góc trên, sau lưng. Có thể lấy mốc đứng băng khoảng 2,5 s sau phím, thêm mốc vỡ nếu cần. Ghi `ABOUT.md`, chạy lại review-index, gửi owner duyệt rồi dừng. Chưa thực hiện chấm độc lập hoặc đưa vào game.

Trạng thái bàn giao: **chờ quyền chạy lab / ghi review và phạm vi nối audio**, không có kết quả nghiệm thu thị giác hoặc hiệu năng.
