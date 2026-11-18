# Phiếu 389 — Ult băng v3 theo ảnh 386

Ngày 16/11/2026. **Đã dựng mã và cắt sprite; chưa hoàn tất nghiệm thu.** V3 là mặc định trong worktree lab. Chưa có ảnh so sánh thật, số đo p95 hoặc kết luận đạt 8,5. Âm mọc/vỡ chưa nối được vì host nằm ngoài phạm vi sửa.

## Đã làm

- `games/.wt-ic-lab-all/src/lab/ice-ult-layered.ts`: chọn v3 mặc định; `?iceVersion=v1` và `?iceVersion=v2` giữ hai bản cũ. Y và `?ultIce=video` giữ video cũ. Giữ đường chớp màn, khựng hình, sát thương, số sát thương, âm ultimate băng và clip tụ/phát/sóng/chạm cũ.
- `games/.wt-ic-lab-all/src/lab/ice-ult-sprites.ts`: 180 cụm từ đúng ảnh `ult-ice-crystal-clusters.v1-try1.png`, không có lưới tinh thể tự tạo trong v3. Cụm dựng đứng và quay quanh Y theo camera; có nhiều cỡ, lật ngang và nghiêng nhẹ. Phân bố 108 cụm ở hai vành, 40 cụm bên trong và 32 cụm quanh quái; vòng ngoài nằm khoảng 25–29 m, trong vùng phép 30 m. Mọc 0,2 s theo sóng từ người tung, tốc độ 26 m/s.
- Mặt băng lấy từ đúng ảnh nứt, bỏ khung đen, lặp đối xứng để tránh đường nối cứng; mở theo sóng, mép vùng mềm, giữ 3 s rồi tan 2,5 s. Không sửa nền của phiếu 387.
- Một bông ở tâm vùng băng, ghép sáu cánh từ cụm 3 và tâm từ cụm 2. Chỉ chi tiết sáng của bông này có HDR 4 trong 0,09 s khi trúng chính; RGB các lớp mới khác đều giới hạn ≤ 0,9.
- Hai vỏ từ đúng ảnh `round-shell`, billboard ôm quái thật, cỡ theo bán kính và chiều cao; tối đa 128 vỏ. Hết 3 s trói, mỗi vỏ vỡ thành sáu sprite mảnh và hai lớp bụi/lấp lánh từ đúng ảnh `shards-sparkle`. Huỷ vỏ và mảnh chờ nếu quái chết sớm.
- Sương thấp, bụi và tia lóe đều lấy từ ảnh `shards-sparkle`, chuyển động bằng vị trí, xoay, đường vào/ra và nhấp nháy. Không dùng thú hoặc cảnh vẽ sẵn từ ảnh đích.
- `docs/games/tu-tien/skills/VFX_LIBRARY.md`: thêm bảng thành phần, nguồn, vai, thời gian và trạng thái chưa nghiệm thu; giữ hồ sơ v2/video cũ.

## Media và script

Thư mục `games/immortality-cultivation/art-src/lab/vfx/ice-ult/` cũng được worktree dùng qua symlink `art-src` có sẵn:

- `cluster-0..3.png`, `shard-0..2.png`, `dust.png`, `sparkles.png`, `glint.png`, `shell-0..1.png`: 12 sprite 512×512, RGBA, nền đen thành alpha, giữ tỉ lệ hình nguồn.
- `ice-ult-v3.atlas.png`: 2048×2048, 4×4 ô, 12 ô có hình; `cracked-surface.png`: 1024×1024. PNG nằm trong lựa chọn xuất của phiếu; không sinh thêm KTX2.
- Mỗi ảnh có `<tên>.prompt.txt` cạnh nó, ghi phép cắt và prompt nguồn nguyên văn hoặc chỉ dẫn ghép atlas. `manifest.json` ghi ảnh nguồn, SHA-256, chỉ số ô và vùng cắt. Chỉ dùng bốn ảnh thành phần `v1-try1` được phiếu chỉ định; ảnh `moment-a.v1-try1` dùng làm đích bố cục và đối chiếu, không thành texture cảnh.
- Không gọi image_gen: phiếu yêu cầu cắt các hình đã chọn bằng script, không vẽ lại hoặc sinh thêm. Không có ảnh tham chiếu bên thứ ba.

Các file mới trong `games/.wt-ic-lab-all/src/lab/`:

| File | Vai |
| --- | --- |
| `ice-ult-cut.mjs` | Cắt lại media bằng ImageMagick 7; khử nền đen và giảm nền xám bên trong vỏ; giữ hình nguồn |
| `ice-ult-sprites.ts` | Các kho thẻ instance, vật liệu, mặt băng, bố trí và lịch v3 |
| `ice-ult-check.mjs` | Kiểm kiểu riêng hai file TypeScript và kịch bản CPU 100 mục tiêu; không chạy bộ test game |
| `ice-ult-review.mjs` | Kịch bản cho runner CDP sẵn có: chụp góc trên/sau lưng cạnh ảnh đích, ghi ABOUT, đo ba lượt 420 khung mỗi góc và cập nhật index; chưa chạy được |

Lệnh đã chạy từ repo gốc:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node games/.wt-ic-lab-all/src/lab/ice-ult-cut.mjs
node games/.wt-ic-lab-all/src/lab/ice-ult-check.mjs
```

## Kiểm tra đã đạt

- TypeScript strict và `noUncheckedIndexedAccess`: 0 chẩn đoán tại hai file thay đổi. Transpile riêng: 0 lỗi cú pháp. Hai script cắt/chụp qua `node --check`.
- Atlas thực tế 2048×2048; 12 sprite đều 512×512 RGBA, mặt băng 1024×1024. Alpha atlas có cả 0 và 1; không có khung đen đặc bao quanh sprite. Đã nhìn sprite cụm và vỏ nguồn sau cắt; việc này không thay cho kiểm hình trong lab.
- Kịch bản CPU 100 mục tiêu, một mục tiêu chết trước sóng: 99 mục tiêu còn sống đóng băng đúng một lần trong 3 s và nhận đúng một lần sát thương khi vỡ. Đúng một cú nhấn chính. Tám lần tung lại/xoá không để instance sót.
- 180 cụm; cỡ thẻ trong kịch bản là 0,760–5,588 m. Sáu lượt vẽ mới: tinh thể+bông, vỏ, mảnh, lấp lánh, sương, mặt băng. Đây là cỡ thẻ và số kho trong mã, chưa phải số đo hình hoặc GPU.
- Callback thử nhận 7 yêu cầu mọc, 1 lan nứt, 9 vỡ và 1 gió; pitch 0,96–1,04. V1/v2 chọn lại được bằng URL, video mặc định/toggle vẫn giữ.
- Không chạy build hoặc bộ test của game; không sửa `view/ground.ts`, `rules.ts`, `skills-main.ts`, mã phiếu 387 hay các game khác. Không commit, push, reset, clean, stash, đổi nhánh hoặc đưa media vào Git.

## Còn thiếu và bằng chứng chặn

| Mục | Kết quả hiện tại |
| --- | --- |
| Ảnh so sánh góc trên và sau lưng cạnh `ult-ice-moment-a` | Chưa có; không dùng ảnh dựng giả thay ảnh lab |
| `stress.html`, 100 hình quái, p95 ≤ 16,7 ms | Chưa đo, chưa có baseline v1/v2/v3; không suy FPS từ kiểm CPU |
| Âm tinh thể mọc và vỡ qua bus dùng chung | Chưa nối; không tạo AudioContext thứ hai hoặc can thiệp prototype |
| Hai giám khảo ≥ 8,5 và owner xem | Chưa thực hiện |

Các chặn thực tế:

1. Chạy Vite đã cài với cache `/private/tmp/codex-389-vite`, cổng 3019: `listen EPERM: operation not permitted 127.0.0.1:3019`. Không có server mới còn chạy. Có cổng lab cũ 3146 đang nghe, nhưng không xác minh được qua trình duyệt.
2. CUA trả `The browser access host is unavailable`. Yêu cầu dùng Chrome bị cơ chế phê duyệt tự động từ chối: `Computer Use was not approved to use Google Chrome`. Không chuyển sang CDP/driver khác để vượt chặn này; script review chỉ được bàn giao, chưa thực thi.
3. `mkdir -p /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ult-ice-v3` bị `Operation not permitted`. Chưa ghi được ảnh hoặc ABOUT tại đích. Không đặt capture vào `art-src`, `public` hoặc `docs`.
4. Đã thử `node scripts/review-index.mjs`; lỗi `EPERM: operation not permitted, open '.../typing-game-review/INDEX.md'`. Index chưa cập nhật.

Phạm vi âm thanh: instance `LabSound` dùng chung và đối tượng host tạo `IceUltLayered` nằm trong `src/lab/skills-main.ts`; đối tượng đó không truyền `sound`. File này không được phép sửa. `IceUltHost.sound` và yêu cầu mọc/vỡ đã có, nhưng trong host thật `soundWired` vẫn false. Cần một phiếu cho phép nối tại host để hoàn tất âm thư viện băng qua bus hiện có, giữ mute, headroom và ghi âm. Chưa chọn/nghe take thay owner.

## Tiếp tục khi quyền được mở

Không cần cắt lại ảnh hoặc dựng lại mã. Chạy host worktree, rồi từ `games/.wt-ic-lab-all`:

```sh
BASE=http://127.0.0.1:3146/stress.html ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/ice-ult-review.mjs --width=1920 --height=1080
```

Chỉ chạy khi quyền dùng Chrome và ghi thư mục review đã được mở. Kịch bản dùng đúng thư mục giao nộp, ảnh thật đặt cạnh tham chiếu, hai góc `top`/`behind`, DPR 1 và bộ băng tải xong. Kịch bản chụp chưa được thực thi, cần kiểm đầu ra và console. Ngoài p95 tổng có readback, phải đo thêm rAF thật, nghe âm và xem ở tốc độ thật/nửa tốc độ. Cảnh stress hiện có 87 mục tiêu thật và 13 walker trang trí; 13 walker không thuộc `TargetField`, không nhận trói/sát thương. Muốn 100 mục tiêu đều nhận phép cần phiếu mở rộng host riêng, không tự đổi workload này.

ABOUT dự kiến (cũng nằm trong script review):

```text
purpose: Đối chiếu ult băng v3 với ảnh 386, góc trên và sau lưng; đo stress 100 hình quái
made-by: Codex, phiếu 389
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/389-report.md
delete-when: Sau khi owner duyệt và không còn cần đối chiếu
```

Owner cần xem độ giống ảnh đích về mật độ, vật liệu, bông tâm và bố cục; độ ôm vỏ trên từng quái; sương/bụi có che quái hoặc chữ không; vết nối của mặt băng và độ mượt khi đổi camera. **Chưa đưa vào game hoặc công nhận nghiệm thu.**
