# Làn Codex 1 (tiếp) · Song Long phím 2: phần hình (phiếu 296), chạy từ sim thật trong lab

Anh (06/11 22:45): "Làm hình Song Long". Sim phần A (đường bay, nhịp, sự kiện `SwarmCastV1`) và phần B (sát thương) đã xong trên nhánh `codex/key2-swarm-sim` (`35f3202`, `d8457d1`). Phiếu này làm **phần hình** theo `docs/games/tu-tien/skills/DRAGON_SKILL.md` §10.6. Làm **lần lượt từng việc**; xong một việc thì tự kiểm theo "Đạt khi", ghi một đoạn vào báo cáo, rồi mới sang việc kế tiếp.

**Model `gpt-6.1-sol`, mức `xhigh`.** Báo cáo duy nhất: `docs/codex-queue/lane1b-report.md` (tiếng Việt, ngắn).

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-swarm-sim`, nhánh `codex/key2-swarm-sim`. Không đụng worktree khác.
- **Chỉ đọc** module lab cũ: `git -C games/.wt-ic-dragon-swarm show HEAD:src/lab/dragon-swarm-energy.ts`, `dragon-swarm-3d.ts`, `dragon-swarm.ts` (nhánh `claude/dragon-swarm-lab`, đã có chuyển động, B-spline, làm ấm, tốc độ 1,3× của các phiếu 288–290). Đây là mẫu hình và chuyển động anh đã duyệt.
- **Model và texture** (phiếu 292, media không vào Git): `games/.wt-ic-dragon-swarm/public/assets/immortality-cultivation/models/` và `…/vfx/`. Được chép (`cp -n`) sang cùng đường dẫn trong `public/` của worktree này; không sửa bản gốc.
- **Không đổi sim**, không đổi số sát thương, không đổi băm replay. Không lệnh git ghi. Không mở cổng mạng, không mở trình duyệt (Claude quay video sau).

## Danh sách việc
### Việc 1 · Presenter
- File mới `src/view/skills/qi-dragon-swarm.ts`, dựng từ module lab:
  - nhận gói `SwarmCastV1` của sự kiện `skill-fx` giai đoạn `swarm-cast`;
  - đồng hồ là tick thế giới (dừng khi tạm dừng), vẽ thân theo **đúng đường xoắn sim gửi**, nội suy giữa hai tick;
  - đầu tới ngọc đúng tick lao; rút theo nhịp sim; nổ ngọc ở `swarm-burst`, dọn ở `swarm-end`.
- Pool 2 bầy cho hai lần tung chồng (tách theo `castId`). Làm ấm trong `newMatch`. Giảm chuyển động theo canon §24 (`docs/games/tu-tien/00-canon.md`).
- `src/view/fx.ts`: chỉ thêm nhánh gọi presenter cho ba giai đoạn `swarm-*` (phần A đã chặn chúng khỏi loạt kiếm chung).
- **Đạt khi:** test thuần trên node cho phần không cần GPU (giải mã gói, nội suy theo tick, chọn bầy trong pool, thời điểm hiện, ẩn, dọn); `tsc` sạch; vitest toàn bộ qua.

### Việc 2 · Tầng chất lượng
- **High:** 5 rồng, tối đa 3 lượt depth prepass (≤ 8 lượt vẽ skinned).
- **Medium:** 5 rồng một lượt, không prepass.
- **Low:** 5 dải hoặc bóng 2D theo đường chiếu, ngọc và nổ màn hình; không skinned, không bloom; giữ đúng nhịp và chỗ.
- Model High/Medium lấy theo manifest trong `public/assets/immortality-cultivation/`. Chọn tầng theo cài đặt chất lượng sẵn có của game.
- **Đạt khi:** test chọn tầng và số lượt vẽ theo tầng; `tsc` và vitest qua.

### Việc 3 · Lab chạy từ sim thật
- Trong `skills-lab.html` của worktree này: tham số `?key2=swarm` cho phím 2 tung bầy rồng khí từ sim thật (header `swordKey2 = "swarm"`), trên bầy quái của lab, tầng theo `?tier=high|medium|low`.
- Ghi vào báo cáo cách mở và các tham số, để Claude quay video cho anh.
- **Đạt khi:** `tsc` và vitest qua; lab mặc định (không tham số) không đổi.

## Kiểm (sau mỗi việc)
- `./node_modules/.bin/tsc --noEmit -p .`
- `./node_modules/.bin/vitest run --no-cache --configLoader runner --maxWorkers 4` (trước phiếu: 91 file, 1.048 test)
- Băm replay ghim trong `tests/sim/twin-pearl.test.ts` không đổi.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
