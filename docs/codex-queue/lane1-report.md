# Làn 1 · Song Long phím 2

Worktree: `games/.wt-ic-swarm-sim`, nhánh `codex/key2-swarm-sim`. Không commit, không mở cổng, không sửa worktree khác hoặc `art-src`.

## Việc 1 · Phiếu 294 — ĐẠT kiểm bắt buộc

Đã thêm ba kênh sau cờ `swarm`: quỹ sóng thả 0,5 W ở F1 trong 6 m; chạm 0,15 W mỗi quái một lần/tung; quỹ nổ 2,5 W chia trọng số theo tia tới biên, sàn 1 HP, dư lớn nhất rồi id. Va chạm 3D trên đường xoắn cắt đúng đuôi/đầu, pha rộng dùng lưới 4 m. Sổ theo serial và `castId`; trần mỗi quái thường 2,5 W, mỗi boss 1,5 W; ba kênh dùng chung trần cụm 60 %. Phần bị cắt, dư máu, miễn thương không chia lại. Tick nổ = max(lao) + 32, hết = nổ + 40. `hit` có `castId`, `phase`, `dragon` khi chạm; phiên bản va chạm/sát thương tăng lên 2, đã nằm trong rulesHash riêng của swarm.

- `./node_modules/.bin/tsc --noEmit -p .`: sạch.
- `./node_modules/.bin/vitest run --no-cache --configLoader runner --maxWorkers 4`: **91 file, 1.048 test PASS**, gồm 22 test sát thương mới; cả bốn dãy băm ghim của mặc định/twin-pearl giữ nguyên. `git diff --check`: sạch.
- Giữ các phép thử 200 bố cục và 200 trận replay. Ca replay phần A nay tung một lần có sát thương rồi ngừng gõ để vẫn kiểm kết trận thua; vẫn so gói, world/local hash và replay chính thức. Đo dựng 5 đường/60 quái: trung bình **0,550 ms**, bán kính nhỏ nhất **4.443 mm**, dài nhất **65.312 mm**, tối đa **263 mẫu / 11.968 byte**.

File mã: `src/content/data/swarm.ts`, `src/content/types.ts`, `src/sim/combat.ts`, `src/sim/swarm.ts`; test: `tests/sim/swarm-damage.test.ts`, `tests/sim/swarm-sim.test.ts` (đều trong worktree trên).

**Cần Claude xem:** sim chưa có trường hurtbox riêng. Phần chạm dùng kích thước thân đã có trong `speciesDef.placeholder`: tâm cao nửa chiều cao từ chân, bán kính nửa max(dài, rộng). Sóng thả chia đều quỹ, dư theo id vì §10.4 không ghi công thức chia riêng cho kênh này. Chưa đổi đường chọn đích phần A.

## Việc 2 · Phiếu 295 — Đã đo; TRƯỢT cân bằng, không đổi số

Đo trên `d8457d1`, giữ nguyên bot Chuẩn 272: 35 WPM, chính xác 95%, CV 0,25, Cân bằng, bật điều nhịp, đứng yên, cách mua và ưu tiên chiêu cũ. Bản sao chỉ thêm cờ `swarm`, điều kiện trong tầm như `twin-pearl` và bộ ghi chỉ đọc theo `castId`. Đối chứng `twin-pearl` chạy lại seed 1–20: **3/20 thắng (15%), phím 2 = 45,98892%**, tái lập đúng phiếu 272.

Quét **36 bộ × 20 seed = 720 trận**, cùng seed 1–20. Các ô dưới là **thắng % / phím 2 trên cả trận %**. Phần sát thương là trung bình tỉ lệ từng seed, cùng công thức 272; chỉ tính HP thật sau trần và dư máu. JSON có thêm tỉ lệ gộp HP.

| Sóng W | Chạm W | Nổ 2,0 W | Nổ 2,5 W | Nổ 3,0 W | Nổ 3,5 W |
|---|---|---|---|---|---|
| 0,30 | 0,10 | 0% / 37,73% | 0% / 41,13% | 0% / 43,28% | 0% / 45,98% |
| 0,30 | 0,15 | 0% / 40,61% | 0% / 42,55% | 0% / 45,18% | 10% / 46,98% |
| 0,30 | 0,20 | 0% / 41,82% | 5% / 44,22% | 5% / 47,16% | 20% / 48,20% |
| 0,50 | 0,10 | 0% / 37,71% | 0% / 41,19% | 5% / 43,15% | 5% / 46,33% |
| 0,50 | 0,15 | 0% / 40,39% | 0% / 42,84% | 0% / 45,36% | 0% / 47,44% |
| 0,50 | 0,20 | 0% / 42,34% | 5% / 44,23% | 0% / 47,36% | 30% / 47,03% |
| 0,70 | 0,10 | 0% / 37,92% | 0% / 41,31% | 5% / 43,18% | 5% / 45,85% |
| 0,70 | 0,15 | 0% / 40,32% | 0% / 43,15% | 0% / 44,89% | 5% / 46,87% |
| 0,70 | 0,20 | 0% / 42,42% | 10% / 44,66% | 0% / 47,37% | 25% / 47,65% |

**Không bộ nào trong lưới quét đạt cả hai điều kiện**, kể cả chỉ xét thắng >15%. Các bộ ≤45% thắng cao nhất **10%** (`0,7 / 0,20 / 2,5 W`, phím 2 **44,66377%**). Bộ thắng cao nhất **30%** (`0,5 / 0,20 / 3,5 W`) lại chiếm **47,03160%**. **Không chọn bộ mới; giữ `src/content/data/swarm.ts` ở 0,5 / 0,15 / 2,5 W.** Không sửa chiêu khác hay cách bot dùng chiêu. Lưới 3 × 3 × 4 này không chứng minh cho mọi số xen giữa; 20 seed/bộ chưa thay thế thử người thật.

### Số đo từng lần tung

Đã ghi **26.854 lần tung**: 26.611 có sự kiện hết, 29 đã nổ chưa có sự kiện hết, 214 chưa nổ; giữ sát thương đã xảy ra, không ngoại suy. Có 18 lượt giữ, 0 hủy; 48 lần tung không có hit dương. Mỗi dòng có 5 độ dài đường, đám chọn và đám F0 thật bị thân chạm, tick lao/nổ/hết động, đòn đầu, số quái chạm, hit từng rồng, sổ từng kênh và trạng thái kết thúc; cast chồng tách bằng `castId`.

Bộ khởi điểm: **0/20 thắng, phím 2 = 42,84409%**, 724 lần tung (716 có sự kiện hết, 8 chưa nổ). Độ dài mỗi đường trung vị **23,441 m**, khoảng **4,205–73,483 m**; trung bình **2,57** lượt chọn đám và **2,82** đám F0 thật bị thân chạm/lần. Trung bình **5,60 quái chạm/lần** (tối đa 21). Đòn đầu dương trung vị **F50**, p10–p90 **F1–F75**, xa nhất F244; 2 lần không có hit dương. Tick nổ trung vị **F224**, khoảng F152–F310; luôn `max(lao) + 32`, hết sau đó 40 tick.

| Kênh khởi điểm | HP thật/lần tung | HP bị trần cắt, tổng 20 seed | HP dư máu, tổng 20 seed |
|---|---|---|---|
| Sóng thả | 6,05 | 523 | 723 |
| Chạm thân | 90,12 | 2652 | 3385 |
| Nổ ngọc | 206,08 | 32947 | 17551 |

Trần cắt **13,05887%** sát thương tiềm năng ở bộ khởi điểm; miễn thương chặn riêng 44 HP nổ. Dư máu và miễn thương không tính là bị trần cắt. “Đám thật bị thân chạm” là ô/vùng F0 có thành viên nhận tiếp xúc trong sổ sim, kể cả bị cắt về 0; khác số đám chọn làm đích.

### Kiểm và bàn giao

- `./node_modules/.bin/tsc --noEmit -p .`: sạch. `./node_modules/.bin/vitest run --no-cache --configLoader runner --maxWorkers 4`: **91 file, 1.048 test PASS**; bốn dãy băm ghim mặc định/`twin-pearl` giữ nguyên. `git diff --check`: sạch. Không chạy build.
- 5 script đo qua strict/noEmit. 4 cặp trận gốc/bản sao (line và twin-pearl × seed 1–2), gồm snapshot, replay và hash: khớp mọi trường. Kiểm 212 đầu vào số hợp lệ chỉ đổi ba kênh; 40 đầu vào sai bị từ chối trước mutation.
- Bộ ghi qua ca cast chồng, sổ/hit/đòn đầu khớp, giữ tham chiếu sau khi cast rời mảng, thời gian động, miễn thương/trần/dư máu và hash world không đổi. Kiểm **720 JSON / 26.854 cast: 0 lỗi** về danh tính, sát thương, sổ kênh, thời gian và mẫu số.

File đo nằm trong `games/.wt-ic-swarm-sim/tmp/skill-reach/swarm/` (ngoài Git): `bot.ts`, `numbers.ts`, `recorder.ts`, các kiểm riêng, `sweep.mjs`, `aggregate.mjs`; dữ liệu thô `match/`, đối chứng `baseline/`, [bảng 36 bộ](../../games/.wt-ic-swarm-sim/tmp/skill-reach/swarm/scan-table.md), [số tổng hợp và từng seed](../../games/.wt-ic-swarm-sim/tmp/skill-reach/swarm/numbers.json), `source-manifest.json`, `tsc.log`, `vitest.log` và kết quả tự kiểm. Tái lập từ worktree: `node tmp/skill-reach/swarm/sweep.mjs` (giữ trận đã có), rồi `node tmp/skill-reach/swarm/aggregate.mjs`. Trận lẻ: `TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/swarm/bot.ts <thư-mục-mới> standard@swarm+r50t15b250 1 1`.

**Cần Claude và anh xem:** bảng trượt hai ngưỡng, mức chạm 5,60 quái và đòn đầu F50 của bộ khởi điểm để quyết bước tiếp theo theo §10.4. Không đổi mã nguồn/test game, không làm lại Việc 1 đã commit, không làm presenter hay bật biến thể cho bản chơi. Không phải hết hạn mức.
