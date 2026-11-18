# Phiếu 397 — Hoạt ảnh nhân vật, đợt 1 trong lab

Ngày 16/11/2026. Đã làm lát thử **Kiếm A trên `human` 66 khớp**, nối gõ thật trong lab và xuất clip. **Kiểm kiểu và probe CPU 60/120 Hz đạt các cổng đã đo**. Chưa có ảnh/video, phép đo phím thật → màn hình, nghe âm hoặc chấm chuyển động: browser host không khả dụng và sandbox chặn thư mục review. Đây chưa phải nghiệm thu hệ dùng chung chuẩn 9.

## Cách làm và tệp

Chọn **key pose bằng code trong lab**, dùng `PoseAuthor`, `KeyPoser`, chuyển tiếp quán tính và `FootLock` đang có. Không dùng Blender, Mixamo, Tripo, model mới hoặc rig Lam. Idle và bộ xương nguồn giữ nguyên. Phiếu 395 đã có báo cáo và dòng `[x]` trong `docs/work/LANES.md` trước khi nối phím.

Trong `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all/`:

- `src/lab/anim-r1-poses.ts`: sáu dáng khóa cho S0 → mở khoảng tay → S1 → gồng → nhả → theo đà. S0 dùng bàn tay khum mở, S1 gập áp út/út và giữ trỏ/giữa; chân trái bước trước 0,15 m trong gồng. Nhả rồi giữ, theo đà, lắng và thu.
- `src/lab/anim-r1-controller.ts`: tiến độ chữ, ba xung luân phiên cổ tay/khuỷu/ngực có cộng năng lượng và chặn trần; phản ứng sai nhỏ; sửa lùi, huỷ, đổi đích; marker riêng cho pose đã áp dụng, pha nhả bắt đầu chuyển động, VFX và khung vẽ. Thở 0,25 Hz và nghiêng hông theo đích được áp sau pose, trước IK; nhìn đích dùng đường `poseTarget` hiện có.
- `src/lab/anim-r1-lab.ts`: cổng `human`, F2 và các phím của lát thử, trạng thái tiếng Anh, API `window.__labAnimR1`.
- `src/lab/anim-r1-check.ts`: kiểm kiểu có kéo theo `skills-main.ts`, nạp rig thật, probe FK/IK, kiểm chuyển trạng thái và xuất/đọc lại clip. Chạy riêng, không chạy build hoặc bộ test game.
- `src/lab/anim-r1-review.ts`: kịch bản chụp góc chơi và cận tay, bảng pha, số liệu cùng `ABOUT.md` khi Claude có browser/quyền ghi review. Chưa chạy được phần chụp.
- `src/lab/skills-main.ts`: nối module, phím, reset, điểm sau cập nhật thân/sau render, VFX/âm/camera và bus impact. Giữ phần nối Mộc của 395.
- `art-src/lab/anim/round1/sword-a.clip.json`: một `THREE.AnimationClip` hoàn chỉnh, **1,8 s, 60 Hz, 109 mẫu, 132 track**; có `extras.events`. Khoảng 1,30 MB.
- `art-src/lab/anim/round1/s0.clip.json`, `s1.clip.json`: hai pose tĩnh trên cùng rig, khoảng 19 KB mỗi file.
- `art-src/lab/anim/round1/manifest.json`: nguồn, hệ tọa độ, mặt nạ xương, cách làm và marker. Marker của bản bake: `windup_end` **0,7833 s**, `release` **0,9 s**, `recover` **1,35 s**, lấy từ khung thực.

`art-src` là symlink có sẵn về game chính; chỉ ghi thư mục `lab/anim/round1/` được phiếu cho phép. Lab diễn trực tiếp từ cùng dữ liệu pose dùng để bake; không fetch/phát chồng thêm clip JSON hay mixer thứ hai. Clip JSON là đầu ra tái sử dụng, đọc bằng `THREE.AnimationClip.parse`; không phải GLB model mới.

## Cách thử

Mở `skills-lab.html?hero=human` trên host phục vụ đúng worktree:

| Phím | Kết quả |
| --- | --- |
| **F2** | Vào/ra chế độ Kiếm A |
| **s w o r d** | Gõ từ `sword`; mỗi chữ đúng tăng thế gồng, chữ cuối nhả |
| Chữ khác chữ đang chờ | Xung sai ở cổ tay/ngón; không tăng tiến độ, không diễn như bị đánh |
| **Backspace** | Lùi một chữ và giảm thế gồng qua chuyển tiếp |
| **Escape** | Huỷ từ và thu tay; không phát VFX nhả |
| **Tab** | Luân phiên bốn đích, gồm đích phía sau; mắt/thân/chân quay theo đường có sẵn |

Hai tay kết ấn trống: tạm ẩn prop kiếm cầm trong chế độ này để S0 không xuyên cán kiếm; dùng **kiếm khí/VFX k1 đã có**. Khi thoát, prop trở lại sau khi tay thu; giữ đúng trạng thái ẩn/hiện trước khi vào. F2 đợi authored skill khác thu xong; từ chối vào lúc cut-in hoặc lab đang pause. Không nhận composition, repeat, paste hoặc tổ hợp Ctrl/Meta/Alt làm chữ đúng; các ô nhập của panel giữ quyền gõ của chúng. Đây là bộ nhập Latin thử nghiệm riêng, chưa nối IME/tầng nhập game.

API thử thêm: `__labAnimR1.begin("art" | "sword" | "cultivar")`, `.text("s")`, `.cancel()`, `.retarget(x,z)`, `.stop()`, `.report()`. Từ được phép dài 3–12 chữ Latin.

Thân cập nhật và giải IK trước, rồi cùng khung gọi `emitRelease("k1")`, VFX k1, âm qua bus cũ và camera kick. Impact đi qua đường trúng thật của projectile; marker `hit` là **sự kiện ngoài clip**, không hẹn theo thời gian clip và không phát sát thương lần hai. Nhật ký contact ghi thứ tự sự kiện k1, **không gán giả cast ID** khi các projectile chồng nhau. Chưa đo onset loa hoặc chứng minh VFX thực sự lên màn hình đúng khung.

## Số đo và kiểm tra

Lệnh đã chạy từ worktree:

```sh
node --import tsx src/lab/anim-r1-check.ts
```

Không chạy build/bộ test game. TypeScript strict, `noUncheckedIndexedAccess`: **0 chẩn đoán** cho năm file mới, `skills-main.ts` và phụ thuộc.

Mỗi tần số thử 3/5/8 chữ (`art`, `sword`, `cultivar`) ở 15/45/90 WPM, cộng một lần nhập dồn; tổng **10 callback nhả đúng một lần**. Có sai, Backspace, huỷ, đổi đích 180°, từ mới ngắt hành động đang diễn, cập nhật `dt=0`, xung luân phiên, guard pause và chuỗi fanSweep → vào F2 sau khi thu. Quaternion/vị trí hữu hạn, không cộng dồn lớp khi dừng đồng hồ. Clip xuất đọc lại qua sampler khớp toàn bộ 109 mẫu: sai góc < 0,001 rad, vị trí < 0,00001 đơn vị model.

| Chỉ số CPU theo bước cố định | 60 Hz | 120 Hz |
| --- | ---: | ---: |
| Số khung trong phần đo chính | 1.997 | 3.944 |
| Dấu chữ cuối → marker sau thân, p95/max | 16,657 ms | 8,323 ms |
| Dấu chữ cuối → pha nhả có trọng số và chuyển động, max | **16,667 ms** | **8,333 ms** |
| Sai khung callback nhả/VFX/khung vẽ giả lập | 0 | 0 |
| Mẫu chân khóa được đo | 2.334 | 4.769 |
| Trượt chân trụ lớn nhất | **0,03534 m/s** | **0,04097 m/s** |
| Khung gần T/bind theo hai cánh tay | **0** | **0** |
| Y nhỏ nhất tại khớp ball chân | +0,00880 m | +0,00892 m |
| Bước góc tay/cánh tay lớn nhất | 32,85° | 17,41° |
| Đỉnh tương ứng của clip nguồn `Sword_Regular_A` | 38,68° | 19,34° |
| Tỷ lệ đỉnh mới/nguồn | 0,849 | 0,900 |
| CPU p95 lượt chốt, một human + adapter/probe | 0,0728 ms | 0,0467 ms |

Trượt đo trên world transform sau lớp và IK: lấy tốc ngang nhỏ hơn giữa ankle/ball để tính đúng pivot gót/mũi, chỉ khi khóa liên tiếp và không bước. Cổng ≤ 0,05 m/s đạt trong các ca đã đo. Kiểm góc ≤ 1,5 lần đỉnh kiếm nguồn đạt, nhưng không thay được xem diễn xuất thực. Y khớp ball không phải phép kiểm mọi đỉnh mesh đế chân.

**Giới hạn phép đo trễ:** đây là đồng hồ input được đưa vào probe Node với bước cố định, không có hàng đợi OS/browser, GPU hoặc present màn hình. Bộ đo xác nhận pose thực đã áp dụng và pha có chuyển động; callback VFX trong CPU là stub. Bản browser đã lấy dấu từ `KeyboardEvent.timeStamp` và ghi `performance.now()` sau render, nhưng chưa chạy được; ngay cả dấu sau render cũng chưa phải photon/present. Vì vậy chưa xác nhận toàn tuyến phím thật → hình ≤ 50 ms.

Hai lỗi cơ chế đã xử lý trong module mới: KeyPoser giữ mục tiêu gồng tăng dần nên Backspace cần vào lại từ pose đang hiển thị; huỷ gốc 120 ms nâng hông trước bước chân thu 200 ms nên riêng recovery huỷ của R1 chạy **267 ms**, IK vẫn nhận dt đầy đủ. Không đổi tốc nhả hoặc sửa Animator/FootLock dùng chung. Guard khi đổi authored skill tránh trạng thái spacing cũ của fanSweep.

SHA-256 **15 file Băng/Mộc** có sẵn lúc nhận phiếu giống trước/sau. Không sửa `ice-ult-*`, `wood-ult-*`, `src/view/`, `src/ui/`, scripts/tests hoặc docs của game.

## Chặn, điểm yếu và phần owner cần xem

- CUA trả `Browsers: Error: The browser access host is unavailable`; đã kết thúc phiên kiểm CUA. Không dùng driver khác để vượt chặn.
- Tạo `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r1/` bị **`Operation not permitted`**. Chưa có ảnh/video hoặc `ABOUT.md` tại đó. Không ghi capture sang `art-src`, `public` hoặc `docs`; chưa có capture để rebuild index/prune. Nội dung ABOUT và lệnh index nằm trong script review.
- Cần xem S0 có đúng lòng ngửa/tay phải trên tay trái, S1 có đủ khe ngón, cái giữ đúng chỗ và không xuyên; hiện là dáng khóa có ngón thật, **chưa xác minh tiếp xúc/skin bằng hình**.
- Cần xem lực chân–hông–vai và độ tách dáng từ camera chơi, nhất là nhập 90 WPM, nhả khi chưa đủ gồng, huỷ và đổi đích 180°. Không tự chấm vẻ đẹp hoặc khẳng định không giật cảm nhận từ số góc.
- Chưa kiểm GPU, FPS cảnh nặng, viewport 720p/1080p, onset/mix âm, Hit_Chest ngắt giữa chiêu trên bản chốt, hai giám khảo mù hoặc chuẩn 9. Không gọi đây là nghiệm thu nhân vật/hệ hoạt ảnh.

Khi Claude có quyền, phục vụ **đúng worktree** trước; chỉ dùng cổng 3146 nếu nó thực sự đang phục vụ worktree này. Kịch bản không mở server hoặc build:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/skills-lab.html \
ART_MAGICK=/opt/homebrew/bin/magick \
node --import tsx src/kit/tools/cdp-run.mjs src/lab/anim-r1-review.ts \
  --width=1920 --height=1080 --dpr=1
```

Script tạo ABOUT, 16 khung hai góc, hai bảng pha và `397-browser.json` trong đúng folder yêu cầu rồi cập nhật index. Cần xem ảnh và lỗi console sau khi chạy; script mới qua kiểm kiểu, chưa được chạy với browser. Sau đó đo phím thật ở rAF 60 Hz, nghe nhả/trúng và quay video thời gian thực để owner xem; số fixed-step không thay bước này.

Không sinh ảnh/âm/look mới; không làm model hoặc rig mới. Không staging media, đổi nhánh, commit, push, reset, clean hay stash. Hạn mức lúc nhận: dùng 31%, còn 69%; không gặp hạn mức sinh media hoặc giờ bắt buộc chờ.
