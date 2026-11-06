# Làn Codex 5 · Gắn âm Firefly còn thiếu vào những chỗ lab đã có hình mà chưa có tiếng riêng

Anh (07/11 00:46): muốn thêm 2 làn Codex để làm nhanh nhưng không tốn token vô lý. Firefly đã làm xong 659 việc âm. Lab mới dùng khoảng 180 việc, gồm 122 sự kiện theo hệ của phiếu 330 và khoảng 57 âm gắn thẳng trong `sound.ts`, `clip-skills.ts`, `showcase.ts`. Còn khoảng 480 việc chưa gắn, gồm Song Long (`twin`), quái theo loài (`beast`), `elite`, `enemy`, `captain`, `boss`, chuỗi, luồng, `ult`, `cutin`, `trib`, `world`, UI và các chỗ khác. Làn này gắn chúng vào **những chỗ lab đã có sự kiện**. Không thêm tính năng mới.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo duy nhất: `docs/codex-queue/lane5-report.md` (tiếng Việt, ngắn). Làm lần lượt từng việc; xong việc nào tự kiểm theo "Đạt khi" rồi mới sang việc kế.

## Nơi làm
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Lab chung có panel gọn, thanh chiêu, A/B, ấn 13 hệ, Song Long, phím 8/9, sao băng M, luồng C, bộ đếm chuỗi.
- **Cơ chế âm có sẵn, dùng đúng nó, không làm cơ chế mới:**
  - `src/lab/sound.ts`: bảng âm Firefly gắn thẳng `FIREFLY_SOUND`, nhóm giọng, gộp cú theo xô, hậu tố hệ.
  - `src/lab/sound-tiers.ts`: `FIREFLY_LEVELS`, mức đo bằng ebur128 theo bậc. Âm chiến đấu to, nổ, vang; UI khô, bậc T1.
  - Cách đo và số đã đo: `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-sounds/measure-2026-11-06.md`, chỉ đọc.
- **Nguồn:**
  - `docs/work/tasks/firefly-sprint-sound.json`: trường `group` và `why` của từng việc nói âm đó dành cho chỗ nào.
  - File: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/sound/<id>/take<N>.wav` và `take<N>.prompt.txt`.

## Ranh giới
- **Được ghi:**
  - `src/lab/sound.ts`, `src/lab/sound-tiers.ts`;
  - chỗ gọi âm trong `src/lab/*.ts`, chỉ thêm dòng gọi tại sự kiện đã có; liệt kê từng chỗ trong báo cáo;
  - test trong `tests/lab/`;
  - số đo vào `.local/lane5-sounds/`;
  - báo cáo.
- **Cấm:**
  - sửa `src/view/skills/*`, `src/sim/*`, `src/content/*`;
  - sửa hay xoá file trong `firefly-sprint-2026-11-05/`;
  - ghi vào `art-src/lab/vfx/` và `tools/vfx-flipbook/`, vì làn 4 đang cắt flipbook;
  - đổi âm đã gắn mà anh đã nghe (122 sự kiện hệ, các mục sẵn có trong bảng);
  - tổng hợp âm bằng mã;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Danh sách việc (theo thứ tự)
1. **Kiểm kê.**
   - Liệt kê việc âm chưa gắn: id không có trong mã lab và không có trong `art-src/lab/audio/SOURCES.json`. Nhóm theo `group`.
   - Với từng nhóm, tìm sự kiện lab tương ứng (grep mã lab: Song Long, quái chết hay trúng theo loài, boss, chuỗi D60, luồng D61, sao băng M, phím 8/9, showcase, panel).
   - Ghi bảng vào báo cáo với các cột: nhóm · số việc · sự kiện lab · gắn được hay "chờ tính năng".
   - **Đạt khi:** mọi việc chưa gắn đều có trong bảng.
2. **Song Long (phím 2)**, các việc `tt-sfx-twin-*`: gắn vào lúc thả, lượn, bổ nhào, chạm, nổ ngọc, tan, theo `why` của từng việc và sự kiện có sẵn trong lab Song Long.
3. **Quái:** `beast-*`, `enemy-*`, `elite-*`, `captain-*`, `boss-*`.
   - Chết, trúng đòn, gào hay lao, theo loài mà lab đang sinh.
   - Loài nào lab không sinh thì ghi "chờ tính năng".
   - Vẫn giữ luật gộp cú theo xô của `sound.ts`, để bầy quái không vỡ tiếng.
4. **Chiêu và bộ đếm:**
   - `streak-*` (mốc chuỗi), `channel-*` (mở, nhịp, đứt), `meteor`;
   - các việc `x-*` của phím 9 chưa gắn hoặc đang mượn âm tạm (D6, D7, D8 trong `clip-skills.ts`);
   - `ult-*`, `cutin-*`, `trib-*`, `world-*`, nơi showcase hay phím 8/9 đã có sự kiện.
5. **UI lab:** `ui-*`, `confirm-*`, `reward-*`, chỉ nơi panel lab đã có thao tác tương ứng (bấm, chọn, đổi hệ). Bậc UI khô, không vang.

**Cách chọn take (việc 2–5):**
- Đo bằng `ffmpeg` ebur128: momentary max, true peak, khoảng lặng đầu, độ dài.
- Chọn take theo số đo cộng với prompt khớp `why`. Ghi một dòng lý do mỗi việc.
- Đặt mức trong `FIREFLY_LEVELS` theo bậc như các mục sẵn có, không quá −1 dBTP.
- Âm có đoạn lặng đầu thì đặt điểm bắt đầu như các mục sẵn có, để tiếng rơi đúng khung sự kiện.
- Agent không nghe được: số đo chỉ để loại take lỗi. Anh nghe và quyết cuối.

## Đạt khi (mỗi việc 2–5)
- Mỗi file được gắn đều có thật. Mỗi mục đều có mức trong `FIREFLY_LEVELS`.
- Có test node thuần: bảng âm mới không trỏ tới file thiếu, mỗi sự kiện gắn mới gọi đúng id.
- `npx --no-install tsc --noEmit` sạch.
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ (trước làn này khoảng 1.311 test). Ghi số test trước và sau.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
