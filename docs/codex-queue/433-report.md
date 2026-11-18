# Phiếu 433 — Trận pháp trời và mưa kiếm Kim, bản lab đầu

Hoàn tất phần mã và kiểm tra CPU ngày **17/11/2026**. **Chờ Claude kiểm hình, âm và GPU**; chưa kết luận đạt p95 toàn khung ≤ 16,7 ms hoặc nghiệm thu hình ảnh 8,5.

## Tệp giao

Chỉ ghi các tệp sau trong worktree `games/.wt-ic-lab-all/src/lab/` và báo cáo này:

| Tệp | Nội dung |
| --- | --- |
| `metal-ult-rain.ts` | Recipe mưa kiếm mới, kho 49 kiếm, trận pháp trên trời, vệt sáng, va chạm, kiếm lớn và tan bụi. |
| `metal-ult-layered.ts` | Nối recipe mới làm mặc định; `?metalUlt=ring` chọn nguyên đường vành đất cũ. Thêm chẩn đoán `mode` và `rain`, giữ hợp đồng host hiện tại. |
| `metal-ult-rain-check.mjs` | Strict, đọc GLB thật, kiểm lịch, hướng kiếm, sát thương qua host, seed, kho và vòng đời tài nguyên. |
| `metal-ult-rain-review.mjs` | Kịch bản cho Claude chụp tám khung đúng giờ, đo stress 100 quái và tài nguyên GPU qua năm lần tung. |

Không sửa mã game chính, `skills-main.ts`, thư viện âm, ảnh, GLB, tài liệu Tu Tiên hay cấu hình. Không tạo media, commit, đổi nhánh, chạy build hoặc bộ test game.

## Chuyển động và thành phần

Theo `VFX_STANDARD`, loại hành động ultimate, dùng lại toàn bộ hình có sẵn; mã chỉ đặt, xoay, di chuyển, nhuộm và xói:

- **0–0,6 s:** khung tĩnh số 16 trong `metal/metal-caster-seal.atlas.png`, nằm ngang ở cao **10,5 m**, sáng dần và xoay 0,18 rad/s. Đường kính bao đám mục tiêu.
- **0,6 / 1,2 / 1,8 s:** ba đợt, mỗi đợt **16 kiếm**, lệch nhau 6 ms trong đợt. Tổng **36 vị trí nhắm quái + 12 vị trí rơi lệch**, seed 433. Vị trí quái được lấy lúc từng kiếm bắt đầu rơi; kiếm rơi thẳng, gia tốc dương, chuyến rơi 0,42–0,50 s.
- **Mỗi va chạm:** kiếm cắm thấp 0,10 m rồi nghiêng nhẹ; `metal-impact-v2` chạy có trộn khung. Quái đang ở điểm chạm nhận `host.blow`, giữ đường giật lùi và số sát thương của lab; không trói quái trong recipe mới.
- **2,0–2,4 s:** kiếm lớn dài **6,6 m**, gấp ba chiều dài danh nghĩa kiếm thường 2,2 m, rơi vào giữa trận. Chạm đúng **2,4 s**, phát `metal-big-burst-v2`, rung/nhấn màn hình qua `host.strike`; cú kết vẫn đi qua đường sát thương diện rộng hiện có cho các mục tiêu sống đã chọn.
- **2,6–4 s:** kiếm xói bằng shader, mép vàng và bụi/glint từ atlas `metal-ult/metal-ult.atlas.png`; trận pháp mờ từ 2,4 s. Vệt kiếm dùng ô blade của cùng atlas, thẻ ngắn hướng dọc. RGB các lớp được chặn ≤ 0,9.
- **Âm:** dùng nguyên `metal-ult-sound.ts`: `gather` khi tụ, `grow` cho tiếng kiếm rơi, `crack` khi chạm, `break` ở kiếm lớn và `tail` cho dư âm; gom âm chạm theo cửa sổ 50 ms.

Một `InstancedMesh` dùng GLB được chỉ định, giữ texture màu/normal/ORM gốc và vật liệu PBR thép bạc, chuôi vàng. Nguồn kiếm vốn đã chĩa mũi xuống. Shader ẩn chân đá phía dưới ngưỡng 0,18 chiều cao nguồn, không sửa GLB; **Claude cần xem trực tiếp mép lưỡi tại ngưỡng này**. Tối đa 49 × 5.570 = **272.930 tam giác kiếm**, cộng năm kho thẻ. Không suy ra chi phí GPU từ số tam giác này.

## Đã kiểm

Chạy từ worktree:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
node node_modules/typescript/bin/tsc --noEmit
node src/lab/metal-ult-rain-check.mjs
node --check src/lab/metal-ult-rain-review.mjs
```

- **Strict toàn worktree: 0 lỗi.** Probe riêng cũng kiểm strict các tệp liên quan và toàn bộ cây import, gồm host `skills-main.ts`: 0 lỗi.
- **PASS:** đợt xuất hiện đúng 0,6 / 1,2 / 1,8 s ở bước 60 Hz; số kiếm **16 / 16 / 16**; tổng **49 va chạm**, kiếm lớn đúng 2,4 s.
- Ma trận kiếm đang rơi có chuôi ở trên mũi, trục thẳng đứng. 100 mục tiêu CPU sống nhận đường damage; mục tiêu chết trước lúc tung không nhận hit giả. Trường hợp ít mục tiêu có thể nhận nhiều kiếm; cú kết vẫn đánh các mục tiêu còn sống.
- **PASS tại 4 s:** clock chốt 4; phép ngừng hoạt động; 49 slot về kho; số instance, tam giác kiếm và số thẻ nộp về 0.
- **PASS năm vòng xoá/tung lại:** cùng seed cho cùng kế hoạch; giữ nguyên mesh, geometry, material, mảng ma trận và mảng thuộc tính; GLB chỉ nạp một lần, bốn atlas chỉ nạp một lần. Có cả bước 15 Hz.
- **PASS clear/dispose khi đang nạp:** không hồi sinh phép cũ; tài nguyên nguồn và texture được giải phóng. Probe giải mã hình học GLB thật; thay giải mã ảnh trình duyệt bằng `THREE.Texture` rỗng.
- **PASS nhánh vành cũ:** chọn `?metalUlt=ring`, giữ 204 cụm và lịch trói/phá cũ với 100 mục tiêu CPU.
- Lượt cuối: lập phép khoảng **0,734 ms**, p95 cập nhật riêng recipe CPU khoảng **0,0565 ms**. Đây **không phải** p95 toàn khung hoặc số đo GPU. Hook PBR được áp vào shader chuẩn r170; chưa biên dịch GLSL trên GPU.

## Lệnh chụp và đo cho Claude

Dùng host đang phục vụ đúng worktree; đổi `BASE` nếu cổng khác. Kịch bản không mở máy chủ:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-lab-all
BASE=http://127.0.0.1:3146/stress.html \
OUT=/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-ult-rain-433 \
ART_MAGICK=/opt/homebrew/bin/magick \
node src/kit/tools/cdp-run.mjs src/lab/metal-ult-rain-review.mjs \
  --width=1920 --height=1080 --dpr=1
```

Kịch bản chờ atlas/GLB, làm ấm đầy đủ pha, rồi chụp **góc trên và sau lưng** tại **0,4 / 1,2 / 2,4 / 3,2 s theo clock recipe**, tạo hai bảng JPG và `433-measure.json`. Nó ghi p95 CPU, p95 toàn khung có đồng bộ `readPixels`, tam giác, số kiếm và tài nguyên GPU qua năm lượt. Cổng **p95 ≤ 16,7 ms** lấy các khung 0,6–4 s ở cả hai góc; ghi số đo trước khi báo lỗi nếu trượt.

Host hiện tại có **87 mục tiêu TargetField + 13 walker = 100 quái trong cảnh**. Walker chỉ gây tải render, không nhận sát thương recipe. Probe CPU phía trên dùng đúng 100 mục tiêu; không đánh đồng hai phép đo.

Đối chiếu vành cũ bằng cách mở cùng host với `?metalUlt=ring`, rồi gọi `__lab.showcase('ult-metal-geng')`. Các kịch bản 402/426 cũ vẫn dành cho vành đất; dùng kịch bản 433 cho mặc định mới.

Kịch bản tạo `ABOUT.md` và xây lại chỉ mục review. Sau khi xem, giữ bảng, số đo và khung được dùng; Claude xem trước danh sách rồi dọn đúng capture của lượt này theo công cụ chuẩn:

```sh
cd /Volumes/SS990TPRO/htdocs/typing-game
node tools/capture-prune/prune.mjs /Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-17/tu-tien/metal-ult-rain-433
# Chỉ thêm --apply sau khi đối chiếu đúng các khung vừa tạo.
node scripts/review-index.mjs
```

**Còn lại:** Claude chạy kịch bản, xem GLSL/404/console, độ rõ vòng trời ở góc sau lưng, phần chân đá bị ẩn, cảm giác gia tốc, màu bạc/vàng, âm chạm và cú kết; đo p95 trên thiết lập của owner. Đây là bản chuyển động đầu để chỉnh theo phân cảnh 431, chưa chấm mù hoặc tuyên bố đạt hình ảnh 8,5. Không có công cụ bị giới hạn trong lượt này.
