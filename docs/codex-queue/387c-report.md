# Báo cáo phiếu 387c · 16/11/2026

**Mã đã xong; 997/997 test và TypeScript xanh. Đo GPU và ảnh N = 90 còn bị sandbox chặn; chưa thể đóng phiếu hoặc chốt N tối đa.** Không ghi Git, không chạy build.

## Phạm vi và điều kiện đầu vào

- Phiếu có dòng phản biện Claude PASS. Một làn, không giao agent phụ. Kiểm tra hạn mức trước khi làm: còn 90%.
- Đã kiểm tra mã 387a: lane 12 m, 51 điểm, camera 42°, 52,8 m, look z −7,55 đã có. Báo cáo `387a-report.md` xác nhận mã/kiểm tự động xong; nghiệm thu ảnh host của 387a vẫn chờ sandbox. Không coi đó là nghiệm thu hình ảnh đã hoàn tất.
- Giữ nguyên `waves.ts`, canon, preset `liveCap`, `liveCapM1`, fixture `tests/typing/world-fixture.ts` có `liveCap: 60`, `HERD_MIX`, `BENCH_COUNTS`, `BENCH_CASE_IDS` và mọi thứ Ngũ Lôi.

## Đã làm

- Chỉ đổi trường `STAGE_M0A.liveCap` từ 60 → 90 trong rules; sửa test stage tương ứng. Test `liveRoom` sau khi sinh 7 Thạch Thử đổi 53 → 83; tên test cap cũng đổi thành 90.
- `BenchCase.map?: "lane"`, đọc `?map=lane`; mặc định không bật. Hàm URL hiện có tên `benchUrl` ghi lại cờ này. `?count=90` dùng giới hạn 1–600 hiện có.
- Camera bench khi khởi tạo và khi gọi `__icBenchCamera('default')` dùng `placeCamera(camera, CAMERA.defaultTiltDeg, VIEW.distanceM, 0, VIEW.lookZM)` cho lane. Hai góc `close`/`heart` giữ nguyên.
- Herd lấy điểm từ `THANH_THACH_AI.field.lane.pointsMm`, đổi mm → m; chọn khoảng cách ngẫu nhiên đều theo chiều dài polyline bằng PRNG hiện có, rồi tiếp tục vào tim. Vị trí sinh/tái sinh chỉ nằm trên phần lane được tác giả định nghĩa, không trên đoạn nối vào tim. Lệch ngang tối đa ±5,5 m; tâm cụm chừa 0,8 m cho thành viên ngoài cùng. Trong chế độ lane, thành viên Thạch Thử tái sinh rải lại cả cụm để giữ đội hình. Lối vào và chuyển động Hỏa Nha vẫn dùng `FIELD.skyEntries` như trước.
- Kịch bản bench nhận env `EXTRA`, ví dụ `map=lane`, lưu vào báo cáo JSON cùng env. Không thêm ca hoặc N mặc định.
- Test mới kiểm khoảng cách mọi điểm sinh quái đất tới lane ≤6 m, rải theo chiều dài, tái sinh, tới tim, lối trời, tính lặp theo seed, đọc cờ/seed mặc định và URL đi-về, truyền `EXTRA`.

## Kiểm

Chạy trong `games/immortality-cultivation`, qua bộ khóa tài nguyên hiện có:

| Kiểm | Kết quả |
| --- | --- |
| `npm run typecheck` | Package không có script này; không thêm script ngoài phạm vi |
| `node node_modules/typescript/bin/tsc --noEmit` | Xanh, exit 0 |
| `npm test -- --maxWorkers=4` | **91 tệp, 997 test xanh**, 12,73 s |
| `git diff --check` trong game | Xanh |

## Golden đổi có chủ ý

`tests/sim/core-hash.test.ts` không cần đổi. Golden trận đang được kiểm trong `tests/sim/twin-pearl.test.ts` đổi vì `world.liveCap` là một trường được hash. Số thú sống tại các mốc này giữ nguyên và đều dưới 60; cap có thể làm hash đổi ngay cả khi chưa tác động giới hạn sinh quái. Không đổi kịch bản hoặc nới phép so sánh golden.

Các mốc lấy mỗi 300 tick; hậu tố `@N` là số thú sống:

| Seed | Tick | Cũ (sau 387a) | Mới (387c) |
| --- | --- | --- | --- |
| 5 | 300 | `2231db6c@23` | `5dd0a95e@23` |
| 5 | 600 | `96141749@35` | `faa53ba7@35` |
| 5 | 900 | `9a5257a5@55` | `9cb2fe5f@55` |
| 5 | 1200 | `28755f54@43` | `c0da7c8e@43` |
| 9 | 300 | `a82ff7c4@21` | `350025e6@21` |
| 9 | 600 | `73c2b707@34` | `4a1fb061@34` |
| 9 | 900 | `578f0f34@52` | `233af216@52` |
| 9 | 1200 | `2b8c358d@35` | `2d6a48cf@35` |

## Đo tải và ảnh: chưa có kết quả hợp lệ

Đã thử mở Vite mới bằng `npm run dev`, cache trỏ `/private/tmp/typing-game-387c-vite`; lỗi **`listen EPERM: operation not permitted 127.0.0.1:3008`**. Host HTTPS hiện có cũng không kết nối được từ shell của phiên này. Hai lượt runner dưới đây, High rồi Medium, đều kết thúc với **`DevTools endpoint did not come up`** trước khi chạy kịch bản. Không có số đo GPU được tạo; không dùng build cũ hoặc số headless thay cho đo GPU.

| N | Chất lượng | p95 (ms), trung vị 3 lượt | Mesh / impostor đo được | So với trần High 12 ms |
| --- | --- | --- | --- | --- |
| 60 | High | Chưa đo | Chưa đo | Chưa xác định |
| 90 | High | Chưa đo | Chưa đo | Chưa xác định |
| 120 | High | Chưa đo | Chưa đo | Chưa xác định |
| 60 | Medium | Chưa đo | Chưa đo | — |
| 90 | Medium | Chưa đo | Chưa đo | — |
| 120 | Medium | Chưa đo | Chưa đo | — |

**Chưa đề xuất N tối đa đạt ≤12 ms ở High** vì chưa có mẫu GPU hợp lệ. `liveCap = 90` là thay đổi đã duyệt, chưa phải bằng chứng máy đạt trần hiệu năng. Không hạ chất lượng hay bật ladder để vượt qua phép đo.

Tạo thư mục `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/map1-lane-build/387c/` cũng trả **`Operation not permitted`** (nằm ngoài writable roots). Vì vậy chưa tạo được `ABOUT.md`, JSON và ảnh N = 90 tại đích; không phát sinh khung thô cần xóa. Không có tệp được thêm/xóa trong review folder nên chưa chạy lại index. Không tìm cách vượt sandbox.

### Chạy tiếp khi môi trường cho phép

Từ game, chạy Vite bằng `IC_VITE_CACHE_DIR=/private/tmp/typing-game-387c-vite npm run dev`. Dùng host đã phục vụ đúng mã hiện tại; không chạy game build hoặc dùng `dist` cũ của agent khác làm chứng cứ. Câu lệnh đo đã thử, lặp lại lần lượt `Q=high` và `Q=medium`:

```sh
URL=http://127.0.0.1:3008 \
OUT_DIR=/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/map1-lane-build/387c \
CASE=crowd-proc COUNT=60,90,120 Q=high RUNS=3 EXTRA=map=lane \
CHROME_FLAGS='--disable-gpu-vsync --disable-frame-rate-limit --enable-precise-memory-info --js-flags=--expose-gc' \
../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs \
  scripts/visual/scenarios/ic-bench.mjs --width=1920 --height=1080
```

Giữ timing mặc định warmup 2 s, đo 10 s, 1920 × 1080, DPR 1; ghi GPU thực tế và xác nhận `valid`. Lấy p95 từ `medians`, số mesh/impostor từ `runs[].instances`. Giữ một ảnh High N = 90 góc mặc định để xem; các ảnh phụ do chính lượt này tạo phải được prune theo quy định rồi dựng lại index của review folder. Bộ runner đã tự đóng Chrome và dọn profile khi lỗi; Vite cũng đã thoát, không để máy chủ của phiếu chạy nền.

Nội dung `ABOUT.md` cần tạo ở thư mục capture khi có quyền ghi:

```text
purpose: Đo bench Map 1 lane 12 m, N 60/90/120, phiếu 387c
made-by: Codex · 16/11/2026
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/387c-report.md
delete-when: Chủ dự án đã xem và phép đo 387c được thay bằng đợt đo mới
```

## Tệp thay đổi trong phiếu

Trong `games/immortality-cultivation/`:

- `src/content/rules.ts`.
- `src/view/bench/{cases,main,herd}.ts`.
- `scripts/visual/scenarios/ic-bench.mjs`.
- `tests/content/{rules,stage}.test.ts`.
- `tests/sim/{core-world,twin-pearl}.test.ts`.
- `tests/view/{crowd-herd,renderer-bench}.test.ts`.

Ngoài game: chỉ báo cáo `docs/codex-queue/387c-report.md`. Thay đổi từ trước của 387a, `media.md5` và agent khác được giữ nguyên. Chủ dự án cần xem kết quả GPU và ảnh N = 90 sau khi có môi trường chạy/ghi capture hợp lệ; phiếu còn mở ở phần này.

## Đo tải của Claude (16/11, Mac mini M4, 1920 × 1080, Chrome có cửa sổ, không vsync, tắt throttle nền)

`ic-bench.mjs`, `CASE=crowd-proc`, `EXTRA=map=lane`, `RUNS=3` (trung vị), renderer ANGLE Metal Apple M4, hợp lệ:

| N | High p95 (ms) | High TB | Medium p95 | Medium TB | Draw |
|---|---|---|---|---|---|
| 60 | 4,1 | 2,97 | 3,8 | 2,89 | 33 |
| 90 | 4,4 | 3,09 | 4,1 | 2,96 | 33 |
| 120 | 4,3 | 3,17 | 4,2 | 3,06 | 33 |

Xa dưới trần High 12 ms; N = 90 an toàn (120 cũng vậy, chỉ đám đông, chưa gồm VFX chiêu và nền ảnh 387b). Số liệu: `typing-game-review/captures/tu-tien/map1-lane-build/387c/{high,medium}/`. **387c nghiệm thu kỹ thuật: ĐẠT.**
