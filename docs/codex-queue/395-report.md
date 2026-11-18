# Phiếu 395 — Tuyệt kỹ Mộc trong lab theo ảnh 391

Ngày 16/11/2026. Đã dựng công thức Mộc trong worktree `games/.wt-ic-lab-all`, cắt ảnh được chỉ định, nối phím 8 và âm Mộc sẵn có. Kiểm kiểu và probe CPU 100 quái **PASS**. **Chưa nghiệm thu hình ảnh, GPU hoặc âm thanh trong host**: công cụ trình duyệt không truy cập được browser host; sandbox từ chối ghi thư mục review.

## Tệp giao nộp

Trong `games/.wt-ic-lab-all/`:

- `src/lab/wood-ult-cut.mjs`: cắt bảng thành phần try3 và mặt đất của phiếu 391, khử nền đen thành straight alpha, lưu vùng cắt/SHA-256/prompt nguồn nguyên văn. Không sinh ảnh hoặc vẽ hình bằng code.
- `src/lab/wood-ult-sprites.ts`: ba kho thẻ instance chung và một decal đất; 180 cụm rễ/gai billboard trục Y, 108 cụm dày ở hai vành và 72 cụm thấp bên trong. Sóng 26 m/s, bán kính 30 m; mặt đất tan trong 2,5 s. Mầm tâm ghép một cụm rễ và ba lá có sẵn; chỉ mạch sáng trên ba lá tâm được HDR.
- `src/lab/wood-ult-tint.ts`: vật liệu clone có tông xanh nhẹ theo từng instance; nối hook gốc và dùng tên thuộc tính/uniform riêng, không đổi opacity. Không có vỏ ôm thân.
- `src/lab/wood-ult-layered.ts`: tụ/phát/sóng/trói/vỡ theo đồng hồ lab; trói 3 s, mỗi mục tiêu sống nhận một cú tại lúc vỡ; huỷ phần trói khi chết sớm; gom sự kiện âm.
- `src/lab/wood-ult-sound.ts`: dùng lại 8 WAV Mộc qua `LabSound`, preload, mức nguồn đo bằng ffmpeg, pitch 0,96–1,04, gom mọc/vỡ tối thiểu 0,24 s; không tạo AudioContext thứ hai.
- `src/lab/wood-ult-check.mjs`: kiểm kiểu các file mới và `skills-main.ts`, probe instance/vật liệu/lịch với 100 mục tiêu, chết sớm, xoá/tung lại, cảnh rỗng, vượt trần hình và adapter âm.
- `src/lab/wood-ult-review.mjs`: kịch bản chụp góc trên/sau lưng cạnh moment-b và đo khung của host; mới kiểm cú pháp, chưa chạy.
- `src/lab/skills-main.ts`: chỉ nối công thức, thứ tự chọn, phím, reset/update, bus âm và API chẩn đoán; giữ các thay đổi có sẵn khi nhận phiếu.
- `art-src/lab/vfx/wood-ult/`: **12 PNG + 12 prompt + `manifest.json`**. Có `root-0..3.png`, `leaf.png`, `spore.png`, `wood-chip.png`, `foot-vine.png`, `sprout-leaf.png`, `light-dust.png` (hai tên cuối dùng lại lá/bào tử), `wood-ult.atlas.png` 2048×2048 và `root-ground.png` 1024×1024. `art-src` là symlink sẵn có về `games/immortality-cultivation/art-src`; chỉ ghi đúng thư mục `wood-ult/` được phiếu cho phép.

Trong repo chính: thêm mục phiếu 395 vào `docs/games/tu-tien/skills/VFX_LIBRARY.md`, cùng báo cáo được yêu cầu này.

## Công thức và điều khiển

Chuẩn `docs/games/VFX_STANDARD.md`, lớp hành động **ultimate**, đích bố cục `ult-wood-moment-b.v1-try1.png`. Ảnh bố cục chỉ làm đích; không lấy nền sàn hoặc dây leo phía sau vào mầm. Mầm được ghép bằng lá và rễ trong bảng thành phần, nên không trùng từng pixel với mầm trong tranh. Đã xem nguồn và atlas sau cắt; lần thử cắt mầm từ tranh bị loại vì dính nền, hai tệp thử do phiếu tạo đã được xoá.

| Pha | Hình và lịch |
| --- | --- |
| Tụ | 16 lá/bào tử hội về tay, vòng dây leo phẳng dưới caster, 0–0,6 s |
| Phát | Caster ra đòn tại 0,6 s cùng 16 lá/bào tử bay ra từ tay và vòng chân thứ hai |
| Sóng | Rễ/gai mọc 0,2 s theo khoảng cách/26 m/s; rễ phủ đất mở cùng sóng tới 30 m |
| Trói | Một vòng dây leo tại Y=0,065 m quay 0,24 rad/s; 4 lá + 4 bào tử quanh hông ngoài thân; vật liệu clone xanh nhẹ; host giữ quái 3 s |
| Vỡ và dư âm | Sáu mảnh gỗ + sáu bụi từ chân/quái khi hết trói; mảnh rơi/tan 0,8 s, bụi tan 1,1 s; đất tan 2,5 s. Lớp phụ RGB ≤ 0,9; HDR chỉ thuộc mầm tâm |

**8** tung Mộc khi được chọn; **Shift+8** chọn mục kế, Mộc ngay sau Băng. **Y** đổi layered/video cho Băng hoặc Mộc đang chọn. **U** bật video Mộc cũ trực tiếp (bật đường video của lab để đối chiếu). `?ultWood=video` khởi đầu ở bản video. API: `__lab.woodUlt("layered" | "video")`, `__lab.showcase("ult-wood-primordial-tree")`.

## Kiểm tra đã chạy

Từ `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all`:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node src/lab/wood-ult-cut.mjs
node src/lab/wood-ult-check.mjs
node --check src/lab/wood-ult-cut.mjs
node --check src/lab/wood-ult-check.mjs
node --check src/lab/wood-ult-review.mjs
```

- **TypeScript strict + `noUncheckedIndexedAccess`: 0 chẩn đoán**, gồm bốn file TS mới, `skills-main.ts` và các phụ thuộc được kéo vào. Không chạy build/bộ test của game.
- **100 mục tiêu, bốn loài instance:** đủ 100 lần trói, 100 tint đúng instance; không có hull bọc thân, không đổi opacity/transparent, hook vật liệu nguồn được gọi tiếp đủ bốn lần.
- Một quái chết giữa lúc trói: vòng, 20 thẻ hạt/mảnh chờ và tint bị huỷ; **99 quái còn lại nhận đúng một cú**, power 1, sau 3 s trong sai số một bước 1/60 s; đúng một nhấn chính.
- Năm lượt xoá/tung lại không còn thẻ hoặc tint hoạt động; cảnh rỗng kết thúc sạch; cảnh vượt trần báo đúng số thiếu hình. Trần ảnh 128 không thay đường trói/sát thương của host.
- Các sự kiện âm của một lượt: tụ 1, mọc 5, nứt 1, vỡ 6, đuôi 1; adapter đăng ký đủ 8 file thật. Chỉ kiểm đường gọi và mức file nguồn, **chưa nghe hoặc đo bản mix sau khi cắt đuôi và ghép**.
- Probe đo riêng hàm cập nhật công thức trên CPU: p95 khoảng **0,026 ms** ở lượt đầu. Đây không phải thời gian khung game hoặc GPU; không suy ra đạt 60 FPS.
- So SHA-256 tám file `ice-ult-*` trước/sau: nguyên vẹn.

Số cấu trúc khi 100 mục tiêu đang trói:

| Kho | Số phần tử nộp |
| --- | ---: |
| Rễ và mầm | 184 |
| Vòng chân | 130 (gồm hai vòng caster, 28 slot trống có shader ẩn) |
| Lá, bào tử, mảnh, bụi | 3.112 (gồm phần chờ tới lịch vỡ) |
| Mặt đất | 1 |
| Tổng | **3.427** |

Toàn công thức có **4 lượt vẽ** theo cấu trúc; riêng trói 21 thẻ/quái trong **2 kho/lượt vẽ chung**, tint thêm 0. Số này chưa gồm renderer, bóng, hậu xử lý, phản ứng trúng và các VFX cũ của host; không phải tất cả thẻ cùng sáng.

## Chặn và phần còn thiếu

1. CUA trả `Browsers: Error: The browser access host is unavailable`, inventory không có browser. Đã kết thúc phần CUA; không dùng driver khác để vượt chặn. **Chưa biên dịch GLSL trên GPU, xem hình/chuyển động hai góc, đo p95 khung hoặc chấm 8,5.**
2. Tạo đúng thư mục ảnh bị từ chối:

   ```text
   mkdir: /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ult-wood: Operation not permitted
   ```

   Vì vậy **chưa có ảnh so sánh hoặc `ABOUT.md` trong thư mục review**. Nội dung ABOUT và phép ghép ảnh nằm sẵn trong `wood-ult-review.mjs`. Không ghi capture sang `art-src`, `public` hoặc `docs`; không có capture để cập nhật index hoặc dọn raw frame.
3. `stress.html` hiện có 87 mục tiêu `TargetField` và 13 walker trang trí. Giữ nguyên host ngoài phạm vi; CPU probe có đủ 100 mục tiêu nhận phép, nhưng chưa có benchmark GPU 100 quái cùng trói. Kịch bản chụp ghi số thật, không tự báo đạt khi thiếu.
4. Âm dùng lại: `tt-sfx-el-wood-charge` take 1/3, `wood-cast` take 1/3, `wood-ring-burst` take 3, `wood-hit-heavy` take 1, `wood-tail` take 1/2. Tiếng vỡ lấy tiếng nứt rễ của heavy hit; **chưa có nguyên liệu tiếng mảnh gỗ văng riêng**. Không sinh âm thay thế. Mức nguồn có đo bằng `ffmpeg -af ebur128=peak=true`; độ khớp hành động, đuôi thực tế và chất lượng nghe vẫn chờ owner.

## Tiếp tục khi có quyền

Phục vụ đúng worktree hiện tại, sau đó chạy kịch bản sẵn có; chỉ dùng cổng 3146 khi nó thực sự phục vụ worktree này:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/wood-ult-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản không mở server/build. Nó tạo `ABOUT.md`, năm khung pha mỗi góc, tờ pha, hai ảnh ghép cạnh moment-b và `395-measure.json` ở đúng thư mục yêu cầu; cập nhật index sau khi ghi. Mới kiểm cú pháp; cần xem ảnh thật, console và lỗi shader sau khi chạy.

Owner cần xem mầm tâm có đẹp và nổi bật; quái còn rõ trong cả 3 s; vòng chân đủ nhẹ; rễ và nhịp lặp mặt đất có lộ thẻ/ô; mảnh/bụi rời ở đúng lúc; nghe âm mọc/nứt/vỡ so với chuyển động. Sau đó mới chấm hiệu ứng tổng hợp và xác nhận ngân sách.

Không sửa game chính `src/scripts/tests`, file `ice-ult-*`, mã 387/394 hoặc game khác. Không staging media, đổi nhánh, commit, push, reset, clean hoặc stash. Hạn mức lúc nhận phiếu: dùng 22%, còn 78%; không có lỗi giới hạn sinh ảnh/âm hoặc yêu cầu chờ theo giờ.
