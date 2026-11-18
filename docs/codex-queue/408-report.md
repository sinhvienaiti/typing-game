# Phiếu 408 — Tuyệt kỹ Hư Không trong lab theo ảnh 398

Ngày 16/11/2026. **Đã dựng mã/asset, nối lab và âm sẵn có; kiểm kiểu và probe CPU 100 mục tiêu PASS. Chưa có ảnh nghiệm thu, kiểm GLSL/GPU hoặc nghe bản mix trong host do chặn trình duyệt và thư mục review.** Không tự chấm đạt 8,5.

## Đã làm

Trong `games/.wt-ic-lab-all/`:

- `src/lab/void-ult-cut.mjs`: cắt đúng `ult-void-components.v1-try2.png` của repo, khử đen thành alpha và đóng atlas. Xuất `art-src/lab/vfx/void-ult/`: bốn khe nứt `rift-0..3`, cụm kính `glass-cluster`, ba mảnh đơn `glass-0..2`, `inward-spray`, `vortex`, `ground-cracks`, `foot-ring`, `glint`, atlas `void-ult.atlas.png` và `manifest.json`. Tổng 13 PNG lẻ + atlas; mỗi ảnh có `.prompt.txt` chứa phép xử lý và prompt nguồn nguyên văn. Manifest ghi tọa độ cắt, SHA-256 nguồn và chỉ số ô. Không gọi image_gen vì phiếu yêu cầu cắt ảnh có sẵn, không vẽ lại hoặc sinh hình.
- `src/lab/void-ult-sprites.ts`: 252 cụm khe nứt, trong đó 192 cụm chồng lấn ở ba vành; mỗi cụm có hai thẻ giao nhau 60° quanh trục Y. Thêm 84 kính lơ lửng. Tâm là trung bình vị trí quái trong tầm, bán kính bố cục 7–14 m; tầm nhận phép vẫn 30 m, sóng 26 m/s. Vành phía người tung chiêu thấp hơn. Dấu đất lấy chính ô vết nứt trong bảng, lan theo sóng rồi xói/tan 2,5 s. Một xoáy hướng camera ở tâm là điểm nhấn HDR duy nhất; hạt phụ xoắn vào tâm, RGB mỗi kênh ≤ 0,9.
- Quái có một vòng nứt xoay dưới chân, bốn mảnh kính nhỏ bay ngoài bán kính thân và tám hạt lúc vỡ. Sau 3 s, mảnh co/tan và sáu mảnh nhỏ hút về tâm. Không dựng vỏ/hull bọc quái. Giữ mặt nạ chữ, có vùng bảo vệ người tung chiêu và giới hạn diện tích thẻ ≤ 14% khung bằng phép chiếu bốn góc.
- `src/lab/void-ult-tint.ts`: clone vật liệu theo batch/loài, nối hook shader gốc, dùng thuộc tính `iVoidBindClock` riêng cho tông tím lạnh nhẹ. Không đổi opacity/transparent hoặc vật liệu nguồn; gỡ tint khi chết, hết giữ hoặc xoá phép.
- `src/lab/void-ult-layered.ts`: đủ năm pha theo `VFX_STANDARD`, host giữ quái 3 s và xử lý sát thương/số, hit-stop/kick qua đường lab sẵn có. Một cú trúng/mục tiêu, một cú chính; huỷ hiệu ứng mục tiêu chết sớm hoặc đang vỡ. Có chẩn đoán tâm/bán kính, số trói/tint, phần vượt trần 128, số kho vẽ và sự kiện âm.
- `src/lab/void-ult-sound.ts`: nối nguyên liệu Hư Không có sẵn vào bus `world`: `tt-sfx-void-vortex-loop`, `tt-sfx-void-ring-burst`, `tt-sfx-void-hit-heavy`, `tt-sfx-void-tail`. Tiếng heavy-hit có prompt gốc về không gian vỡ như kính, nên không thiếu nguyên liệu kính vỡ. Đo nguồn bằng ffmpeg ebur128/true peak trước khi đặt gain; 7 WAV khác nhau, 9 đăng ký theo vai, pitch 0,96–1,04. Mỗi lớp phát một lần/cast, không phát theo từng quái. Không tạo âm mới hoặc âm tổng hợp.
- `src/lab/skills-main.ts`: chỉ thêm chỗ nối. Hư Không đứng **ngay sau Băng** trong danh sách phím 8, trước Kim/Mộc; Shift+8 chọn mục kế, 8 tung. Y đổi công thức đang chọn giữa lớp và video cũ; `?ultVoid=video` mở đường cũ. File `art-src/lab/vfx/ult/ult-void.mp4`, atlas/manifest cũ có sẵn và được giữ nguyên. Thêm `__lab.voidUlt()`, chuẩn bị atlas khi chọn, cập nhật mỗi khung và xoá khi reset/đổi chiêu.
- `src/lab/void-ult-check.mjs`: kiểm kiểu và probe riêng; `src/lab/void-ult-review.mjs`: kịch bản chụp/đo để Claude tiếp tục.

`art-src` trong worktree là symlink sẵn có tới `games/immortality-cultivation/art-src`; toàn bộ lệnh ghi qua đường `/Volumes/.../games/.wt-ic-lab-all/`. Ngoài worktree chỉ cập nhật `docs/games/tu-tien/skills/VFX_LIBRARY.md` được phép và báo cáo giao nộp này.

## Kiểm tra đã chạy

Từ worktree:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node src/lab/void-ult-cut.mjs
node src/lab/void-ult-check.mjs
node --check src/lab/void-ult-cut.mjs
node --check src/lab/void-ult-review.mjs
git diff --check -- src/lab/skills-main.ts
```

- TypeScript strict + `noUncheckedIndexedAccess`: **0 chẩn đoán**, gồm bốn file TS mới, `skills-main.ts` và các import phụ thuộc. Không chạy build hoặc bộ test game.
- 100 mục tiêu thuộc bốn batch: **100 trói, 100 instance ghép đúng tint**, không có shell. Một mục tiêu chết sớm được huỷ; 99 mục tiêu còn lại nhận đúng một cú power 1, sau trói 3 s trong sai số một bước 1/60 s; đúng một cú chính.
- Clone giữ opacity/transparent; bốn hook nguồn đều được nối. Xoá/tung lại năm lần không để lại thẻ/tint; nhóm rỗng và vượt trần 128 có xử lý. Kiểm thêm chết khi đang vỡ.
- Tâm probe `(0, -9)`, bán kính trong 7–14 m; ba vành chồng lấn theo bố trí CPU. Tám trạng thái bảo vệ người tung chiêu; 360 trường hợp phép chiếu gồm thẻ đứng, giao nhau, nằm đất và hướng camera đều trong giới hạn. Diện tích lớn nhất ở tập mẫu là 12,96% khung. **Đây là kiểm toán học, chưa chứng minh hình thật không che người/quái.**
- Lượt cuối: lập công thức khoảng **2,10 ms**, p95 cập nhật công thức CPU khoảng **0,033 ms**. Không phải chi phí toàn khung, GPU hay kết luận 60 FPS. Upload PNG, shader và chuyển động chưa được xác nhận trong renderer.
- Đủ asset/prompt và WAV được đăng ký; lịch âm tụ/xoáy/nứt/vỡ/đuôi mỗi loại một lần. Chưa nghe hoặc đo hỗn âm trong lab.

| Kho chung khi có 100 mục tiêu | Slot nộp |
| --- | ---: |
| Khe nứt, kính quanh vành và xoáy tâm | 589 |
| Dấu đất, vòng chân và vòng người thi triển | 194 |
| Kính/mảnh | 1.504 |
| Hạt hút và radiance | 1.588 |
| **Tổng** | **3.875** |

Có slot trống và thẻ chờ được shader ẩn; số này không phải số hình cùng sáng. Toàn công thức có **4 kho/lượt vẽ**, phần trói dùng chung **3 kho**, tint thêm 0. Mỗi quái đặt lịch 19 thẻ: vòng 1 + mảnh quay 4 + mảnh vỡ 6 + hạt 8. Đây là cấu trúc mã, chưa phải số draw-call đo từ renderer.

## Chặn thực tế và phần chưa nghiệm thu

1. CUA trả `Browsers: Error: The browser access host is unavailable`; inventory không có browser. Đã kết thúc phần CUA, không khởi động server hoặc dùng driver khác để vượt chặn. Chưa có ảnh góc trên/sau lưng, video chuyển động hoặc điểm chấm mù.
2. Lệnh tạo đúng thư mục bị từ chối:

   ```text
   mkdir: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ult-void: Operation not permitted
   ```

   Vì vậy chưa ghi được ảnh cạnh `ult-void-moment-b` hoặc `ABOUT.md` ở đó. Không ghi capture vào art-src/public/docs hoặc thư mục thay thế. Không có capture mới để cập nhật index hoặc dọn raw frame.
3. `stress.html` hiện có 87 mục tiêu `TargetField` và 13 walker trang trí. Probe CPU đã kiểm 100 mục tiêu thật cùng nhận phép; cần host đủ 100 mục tiêu để đo GPU tương ứng. Không sửa herd/stress ngoài phạm vi.
4. Chưa nghiệm thu mức sáng, độ dày vành nhìn thật, tâm nhìn từ trên, che quái ở góc sau lưng, độ liền dấu đất, sound mix hoặc p95 toàn khung. Không đánh dấu tạm đạt.

Không đụng file `ice-ult-*`, không đổi mã/game khác, không chạy build/bộ test game, không staging media, không commit/push/reset/clean/stash hoặc đổi nhánh. Hạn mức đọc trước khi làm: dùng 57%, còn 43%; không có rate limit.

## Tiếp tục chụp cho owner

Khi có quyền browser và thư mục review, phục vụ **đúng worktree** rồi chạy:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/void-ult-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản không mở server/build; cần xác nhận cổng 3146 phục vụ worktree này. Script chờ atlas, kiểm host có chẩn đoán 408, làm nóng đủ pha; chụp tám mốc mỗi góc (tụ, tung, sóng, giữ, cuối giữ, vỡ, dấu đất tan), tạo bảng pha và ảnh cạnh moment-b vào đúng thư mục yêu cầu. Ghi 440 mẫu CPU/tổng có readback mỗi góc, số mục tiêu nhận trói/tint thực tế, console/exceptions và cập nhật review index. `passes100BoundFoes` chỉ đúng khi có đủ 100 mục tiêu nhận phép. Script mới qua kiểm cú pháp, chưa chạy thật.

ABOUT đã để trong script:

```text
purpose: Phiếu 408: so ảnh đích với mốc tung 0,60 s, sóng 1,20/1,90 s và lúc trói 3 s; góc trên và sau lưng
made-by: Kịch bản Codex src/lab/void-ult-review.mjs, phiếu 408
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/408-report.md
delete-when: Sau khi owner duyệt và không còn cần đối chiếu
```

Owner/Claude cần nhìn: vành đủ dày và có chiều sâu; xoáy tâm đọc rõ từ trên; người tung chiêu cùng hình dáng quái còn rõ trong cả 3 s; mảnh vỡ hút/tan mềm; âm hút–nứt–kính vỡ khớp pha và nhường tiếng đọc. Sau đó mới chấm trong host.
