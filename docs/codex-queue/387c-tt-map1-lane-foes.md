# Phiếu 387c · Tu Tiên · Map 1 một đường: liveCap 90 và đo tải 90 quái trên đường 12 m (sau 387a)

> Anh duyệt bề rộng 12 m (16/11: "đồng ý") để "quái nhiều hơn". Bản 387c cũ (nhân số quái trong `waves.ts`) bị ba vòng critic FAIL vì đụng bảng tải canon §13.1; **cân lại đợt là việc thiết kế riêng sau thử chơi**, không trong phiếu này. Phiếu này chỉ mở trần và đo xem máy chịu được 90 quái trên đường mới. Lời giải do Claude viết. Không ghi Git.

Phản biện: PASS (critic Claude mới, 16/11, bản 387c viết lại)

**Model `gpt-6.1-sol`, mức `high`. Một làn.** Báo cáo `docs/codex-queue/387c-report.md`. Chỉ chạy khi 387a đã xong (đường và camera mới).

`G = games/immortality-cultivation`.

## Việc
1. `STAGE_M0A.liveCap` (`G/src/content/rules.ts`) 60 → 90. Chỉ trường này; `liveCap` theo preset (~dòng 78) và `liveCapM1` giữ nguyên. Sửa có chủ ý các test cố định 60 của **stage**: `G/tests/content/rules.test.ts` (~dòng 40, `[60, 7, 6]` → `[90, 7, 6]`), `G/tests/sim/core-world.test.ts` (~dòng 73, `toBe(60)` → `toBe(90)`), và đổi tên test ở `G/tests/content/stage.test.ts` (~dòng 60) từ "live cap 60" thành "live cap 90". `G/tests/typing/world-fixture.ts:73` (`liveCap: 60`) là fixture riêng của test gõ: **giữ nguyên**. Không đổi `waves.ts`.
2. Golden: nếu `G/tests/sim/core-hash.test.ts` hay golden bộ chạy trận đổi (cap chỉ có tác dụng khi > 60 quái sống, nên có thể không đổi), ghi cũ → mới.
3. **Đo tải bằng bench có sẵn** (`G/bench.html`, `G/src/view/bench/`):
   - Thêm tham số URL `?map=lane` (đọc trong `cases.ts` như các tham số khác, mặc định tắt; ca cũ không đổi). Khi bật: (a) `main.ts` đặt camera bằng `placeCamera(renderer.camera, CAMERA.defaultTiltDeg, VIEW.distanceM, 0, VIEW.lookZM)` thay cho `fitCamera` (các hằng do 387a thêm); (b) truyền cờ vào `Herd` (`G/src/view/bench/herd.ts`): khi `map=lane`, mọi quái đi đất thay tuyến cổng → khúc → tim bằng đường gấp khúc `THANH_THACH_AI.field.lane.pointsMm` (import từ `content/data/stage-m0a.ts`, đổi mm → m bằng ÷1000), xuất phát rải đều theo độ dài đường, lệch ngang ngẫu nhiên trong ±5,5 m bằng PRNG sẵn có với `?seed=` (mặc định 20 261 025), rồi đi về tim như chuyển động hiện có; quái tan rồi sinh lại cũng rải dọc đường như lúc đầu (không về cổng). Thêm trường `map?: "lane"` vào `BenchCase` và cho `buildUrl` ghi lại nó. Quái bay (`hoa-nha`) **giữ** lối vào `FIELD.skyEntries` như cũ. `HERD_MIX` không đổi. (c) `window.__icBenchCamera`: khi `map=lane`, nhánh mặc định (không phải `close`/`heart`) cũng dùng `placeCamera(..., VIEW.distanceM, 0, VIEW.lookZM)`, không gọi `fitCamera`.
   - N = 90 dùng `?count=90` (đã cho phép 1–600); **không** sửa `BENCH_COUNTS` hay `BENCH_CASE_IDS`, nên test của chúng không đổi. Thêm test trong `G/tests/view/crowd-herd.test.ts` (đã có) cho `map=lane`: mọi điểm xuất phát của quái đất cách đường ≤ 6 m; quái bay vẫn vào từ `skyEntries`; và trong test đọc tham số bench có sẵn (`G/tests/view/renderer-bench.test.ts`) cho `?map=lane`.
   - Chạy bằng kịch bản có sẵn `G/scripts/visual/scenarios/ic-bench.mjs` (qua `src/kit/tools/cdp-run.mjs`, 1920 × 1080), env `CASE=crowd-proc`, `COUNT=60,90,120`, `Q=high` rồi `Q=medium`, `RUNS=3`; thêm env `EXTRA` (chuỗi tham số nối vào URL, ví dụ `map=lane`) vào kịch bản nếu chưa có. Ghi bảng p95 (ms) và số impostor/mesh. Trần High 12 ms. Vượt trần thì chỉ báo, **không** tự hạ chất lượng (luật 13/11: tối ưu cách vẽ trước).
4. Chụp một khung bench N = 90 ở High, 1920 × 1080, vào `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/map1-lane-build/387c/` kèm `ABOUT.md`. Xoá khung thô của mình.

## Kiểm và nộp
- `npm run typecheck`, `npm test` xanh.
- Báo cáo: file đã đổi, bảng p95 N = 60/90/120 × High/Medium, golden (nếu đổi), đề xuất N tối đa giữ ≤ 12 ms ở High.

Cấm: sửa `src/lab/five-thunder.ts` hay mọi thứ Ngũ Lôi; sửa `waves.ts` hay canon; ghi Git.
