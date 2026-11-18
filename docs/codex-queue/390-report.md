# Phiếu 390 — Thay vỏ băng bằng trói chuyển động

Ngày 16/11/2026. **Đã sửa mã, kiểm kiểu và kịch bản CPU riêng đạt; chưa hoàn tất ảnh nghiệm thu và phép đo GPU.** Bản v3 mặc định trong worktree `games/.wt-ic-lab-all` đã bỏ billboard `round-shell`. Không sinh ảnh, không đổi asset, không commit hoặc đổi nhánh.

## Đã làm

- `games/.wt-ic-lab-all/src/lab/ice-ult-sprites.ts`: thay kho vỏ bằng vòng sương chân nằm trên đất, dùng khung 24 cố định của `ice/ice-ground-mark.atlas.png`. Vòng quay 0,2 rad/s, nhịp alpha nhẹ, giữ 3 s rồi tách theo khe alpha, giãn và tan trong 0,7 s. Code chỉ cắt alpha hình có sẵn, không tự vẽ vòng hoặc tinh thể.
- Mỗi quái có **6 mảnh nhỏ** từ ba sprite `shard-0..2.png`, bay quanh ngang hông với bán kính lớn hơn bán kính quái và có khoảng hở theo cỡ mảnh. Hai nhóm bay ngược chiều, tốc độ 0,65–0,83 rad/s. Sau 3 s, chính các mảnh đó bay tiếp ra ngoài, co và tan trong 0,55 s; 6 lớp bụi/lấp lánh đi theo quỹ đạo, hết tại 3,85 s.
- Mỗi quái có **8 hạt rơi** từ `glint.png` / `sparkles.png`, cỡ 0,06–0,13 m, rơi 0,42 m/s; mờ vào/ra từng chu kỳ. Alpha vòng/mảnh/hạt/bụi lần lượt 0,24 / 0,46 / 0,32 / 0,22; RGB sprite phụ tiếp tục giới hạn mỗi kênh ≤ 0,9. Không thêm nguồn HDR.
- `games/.wt-ic-lab-all/src/lab/ice-ult-frost.ts`: clone vật liệu theo loài, nối tiếp hook dissolve/burn và mặt nạ chữ của vật liệu cũ. Thuộc tính instance riêng điều khiển tông lạnh và Fresnel nhỏ trên mô hình thật, không thay opacity, không phủ mesh mới. Ghép mục tiêu với instance bằng transform công khai lúc bắt đầu trói; không đọc các mảng species/slot riêng của `LabHerd`. Tông lạnh tự hết ở 3 s và xoá ngay khi quái chết sớm hoặc xoá phép. Vật liệu nguồn không bị sửa.
- `games/.wt-ic-lab-all/src/lab/ice-ult-layered.ts`: giữ host đóng băng/đứng hình và đường sát thương/số sát thương cũ. Chạm đầu trói của v3 được thu nhỏ, giảm alpha và đặt sát chân để tránh che thân ngay ở khung đầu. Thêm chẩn đoán `bindDraws`, `bindInstancesPerFoe`, `tintedFoes`, `truncatedBinds`. V1, v2 và video đối chiếu giữ nguyên.
- Rừng 180 cụm, mặt băng nứt và bông tâm giữ nguyên bố trí/nguồn/lịch. Bông tâm vẫn là điểm nhấn HDR duy nhất của các lớp v3.
- `docs/games/tu-tien/skills/VFX_LIBRARY.md`: đánh dấu **không dùng** hai sprite vỏ `shell-0..1.png` từ phiếu 390 và ghi công thức thay thế. PNG, prompt nguồn, manifest và ô atlas 10–11 được giữ nguyên; không xoá asset.

Tất cả ảnh bắt buộc đều có đủ: ba mảnh, glint, sparkles, dust, atlas ground-mark và caster-seal, atlas v3, hai vỏ lưu kho, cùng ảnh đích `ult-ice-moment-a.v1-try1.png`. Đã xem atlas thành phần và atlas ground-mark; việc xem nguồn không thay cho nghiệm thu trong lab.

## Kiểm tra đã chạy

Từ `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all`:

```sh
node src/lab/ice-ult-frost-check.mjs
node src/lab/ice-ult-check.mjs
node --check src/lab/ice-ult-frost-review.mjs
node --check src/lab/ice-ult-frost-check.mjs
```

Kết quả:

- TypeScript strict và `noUncheckedIndexedAccess`: **0 chẩn đoán** tại cả ba file TypeScript của phiếu. Không chạy build hoặc bộ test của game.
- Probe mới với 100 mục tiêu và bốn loài instance: 100 mục tiêu nhận trói, **100 instance ghép đúng tông lạnh**, không có đối tượng `fx-ice-ult-v3-round-shells`. Vật liệu được clone, không đổi opacity/transparent, hook gốc được gọi tiếp đủ bốn lần. Khoảng hở của mảnh lớn hơn bán kính quái cộng nửa chiều cao thẻ.
- Một mục tiêu chết giữa lúc trói: vòng, mảnh chờ, hạt và tint của nó bị huỷ; 99 mục tiêu còn lại nhận đúng một cú sát thương, power 1, cách lúc trói 3 s trong sai số tối đa một bước 1/60 s. Đúng một cú trúng chính. Xoá/tung lại năm lần không để instance hoặc tint còn sót.
- Probe cũ phiếu 389 vẫn PASS: một mục tiêu chết trước sóng, 99 mục tiêu còn sống trói 3 s và nhận đúng một cú; 180 cụm, một bông, lịch sự kiện âm cũ không đổi, v1/v2 và lựa chọn video còn dùng được.
- Hai script mới qua kiểm cú pháp Node. **Chưa biên dịch shader bằng GPU hoặc quan sát chuyển động trong trình duyệt**; kiểm CPU không chứng minh quái nhìn rõ, mức sáng thực tế hoặc tốc độ khung.

## Số instance và lượt vẽ

Đây là số cấu trúc mã và số nộp instance trong probe CPU, **không phải số đo renderer**.

| Kho khi có 100 mục tiêu trói | Số thẻ nộp | Gồm |
| --- | ---: | --- |
| Tinh thể và bông | 187 | 180 cụm + 7 thẻ bông cũ |
| Vòng chân | 100 | 1/quái |
| Mảnh | 960 | 360 mảnh vỡ rừng chờ + 600 mảnh quỹ đạo |
| Lấp lánh | 1.760 | 360 lóe rừng + 800 hạt rơi + 600 bụi tan chờ |
| Sương thấp cũ | 24 | Giữ nguyên |
| Mặt băng | 1 | Mesh mặt đất cũ |
| **Tổng** | **3.032** | Thẻ chờ được shader ẩn, không sáng đồng thời |

Trói riêng là **21 thẻ/quái, 2.100 thẻ cho 100 quái**, chung **3 lượt vẽ**: vòng chân, mảnh và lấp lánh. Tint trên mô hình thật thêm **0 lượt vẽ**. Tối đa 128 quái; vượt trần có `truncatedBinds`.

Tổng lớp v3 vẫn **6 lượt vẽ**, so với 6 ở phiếu 389: một kho vòng thay một kho vỏ, hai kho mảnh/lấp lánh được mở rộng. Mức tăng số lượt vẽ của lần thay này là **0**. Số này tính cho một lượt render cảnh, chưa gồm flipbook cũ, shadow hay hậu xử lý. Các clip chạm/vỡ cũ vẫn dùng pool chung.

## Chặn thực tế và phần chưa làm

1. CUA trả `Browsers: Error: The browser access host is unavailable`; không có browser trong inventory. Đã kết thúc phần CUA, không dùng driver khác để vượt chặn. Vì vậy **chưa có ảnh góc trên/sau lưng, chưa xem đủ 3 s trói, chưa đo p95 ≤ 16,7 ms**.
2. Lệnh tạo đúng thư mục giao nộp bị từ chối:

   ```text
   mkdir: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ult-ice-v3: Operation not permitted
   ```

   Vì vậy chưa ghi được ảnh hoặc `ABOUT.md` ở `.../frost-motion/`; không ghi capture sang `art-src`, `public`, `docs` hay một chỗ khác. Không có capture mới để cập nhật index hoặc dọn raw frame. Nội dung ABOUT đã nằm sẵn trong script chụp.
3. `stress.html` hiện dùng 87 mục tiêu `TargetField` và 13 walker trang trí: tổng 100 hình quái, tối đa 87 nhận phép. Không sửa `herd.ts`, `stress.ts` hoặc host ngoài phạm vi để đổi workload. Probe CPU của phiếu có 100 mục tiêu cùng nhận trói, nhưng không thay cho benchmark GPU 100 quái. Script chụp/đo ghi rõ số đóng băng/tint thực tế và chỉ đặt `passes100BoundFoes=true` khi đủ 100.
4. Chưa có điểm 8,5 hay owner duyệt. Không tự công nhận nghiệm thu hình ảnh. Không thay âm thanh; phần âm mọc/vỡ chưa nối bus từ phiếu 389 vẫn nằm ngoài phạm vi phiếu này.

## Lệnh tiếp tục cho Claude

Đã để lại **file mới** `games/.wt-ic-lab-all/src/lab/ice-ult-frost-review.mjs`; chưa chạy vì các chặn trên. Khi quyền trình duyệt và ghi review được mở, phục vụ đúng worktree hiện tại rồi chạy:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/ice-ult-frost-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Chỉ dùng cổng 3146 khi nó đang phục vụ đúng worktree; script dừng nếu host không có `bindDraws=3` của phiếu 390. Script không mở server hoặc build game. Nó sẽ:

- Ghi `ABOUT.md`, 5 ảnh mỗi góc (`bind-start`, `bind-middle`, `bind-end`, `release`, `dust-end`), bảng pha và so sánh với ảnh đích vào đúng `typing-game-review/owner-review/2026-11-16/tu-tien/ult-ice-v3/frost-motion/`.
- Làm nóng đủ các pha, ghi 420 mẫu công việc CPU/tổng có `readPixels` đồng bộ và 360 mẫu rAF cho mỗi góc. `frameP95WithReadbackMs` tính trên khung đang trói; `rafP95Ms` được lưu riêng, không đánh đồng với thời gian GPU thuần. Lưu GPU, pipeline, số quái thật, console và exceptions trong `measure.json`.
- Cập nhật index bằng `node scripts/review-index.mjs` sau khi ghi ảnh. Script mới chỉ qua kiểm cú pháp, cần kiểm đầu ra, lỗi console và shader khi chạy thật.

ABOUT dự kiến:

```text
purpose: Kiểm hình trói băng chuyển động, góc trên và sau lưng, cùng chi phí stress
made-by: Codex, phiếu 390
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/390-report.md
delete-when: Sau khi owner duyệt và không còn cần đối chiếu
```

Owner cần xem: hình dáng từng loài trong cả 3 s; mảnh ở ngoài thân khi quay camera; vòng chân đủ nhẹ; hạt và bụi có che quái/chữ không; chuyển tiếp bay rời tại giây thứ 3; bông tâm còn là điểm nhấn duy nhất. Sau đó cần phép đo host với 100 mục tiêu thực sự nhận trói để chốt ngân sách.

## Phạm vi

Chỉ sửa hai file `ice-ult-*.ts` đã nêu, thêm `ice-ult-frost.ts`, `ice-ult-frost-check.mjs`, `ice-ult-frost-review.mjs` trong `src/lab/`, cập nhật `VFX_LIBRARY.md` được chỉ định và báo cáo này. Không sửa mã bản đồ 387, `view/ground.ts`, `rules.ts`, src/scripts/tests của checkout chính hoặc game khác. Không chạy build/bộ test game, không staging media, không commit/push/reset/clean/stash/đổi nhánh. Hạn mức đọc trước khi làm: `primary.used_percent=14`, còn 86%; hạn mức Codex không phải nguyên nhân chặn.
