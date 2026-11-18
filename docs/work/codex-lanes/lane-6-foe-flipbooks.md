# Làn Codex 6 · Quái chết, trúng đòn, choáng, trói trong lab bằng flipbook vẽ

Bối cảnh (07/11 01:30):
- Làn 2 và làn 4 đã cắt flipbook từ clip Firefly cho quái: `art-src/lab/vfx/beast/`, `boss/`, `foe/`, `mech/`.
- Làn 5 (`c97d2aa`) gắn âm chết và trúng theo loài.
- Nhưng hình chết trong lab vẫn là `src/lab/death-fx.ts`, vẽ bằng mã: mảnh vỡ, vệt mực, sợi khí.
- Luật của anh: thay hình vẽ bằng mã bằng tranh vẽ có sẵn trước. Code chỉ đặt, canh giờ và làm động, không vẽ hình.

Làn này cho mỗi loài quái hình chết riêng từ flipbook, thêm hình trúng đòn theo mức sát thương, và hình choáng hoặc trói khi quái mang trạng thái đó.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo duy nhất: `docs/codex-queue/lane6-report.md` (tiếng Việt, ngắn). Làm lần lượt; xong việc nào tự kiểm theo "Đạt khi" rồi mới sang việc kế.

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`. Trước làn này: `c97d2aa`, 115 file, 1.328 test.
- **Dùng đúng cơ chế có sẵn:**
  - `src/view/skills/flipbook.ts`: `FlipbookLibrary`, `FlipbookPool`, `FlipbookPlayer`, đọc manifest, KTX2;
  - cách nạp lười và giải phóng như phím 8/9 (`src/lab/clip-skills.ts`).
  - Không viết bộ nạp hay shader flipbook mới.
- **Được ghi:**
  - file mới `src/lab/foe-flipbook-fx.ts`;
  - `src/lab/death-fx.ts`, chỉ để bỏ lớp hình vẽ bằng mã khi có flipbook (xem việc 2);
  - chỗ nối trong `src/lab/skills-main.ts` và `src/lab/events.ts`;
  - test trong `tests/lab/`;
  - nếu thêm KTX2 cho các atlas làn này dùng: file `.ktx2` và mục `ktx2` trong `manifest.json` của `beast/`, `boss/`, `mech/`, giữ nguyên mọi trường khác;
  - báo cáo.
- **Cấm:**
  - sửa `src/view/skills/flipbook.ts` (cần thì ghi lý do vào báo cáo và dừng việc đó);
  - sửa `src/sim/*`, `src/content/*`, `src/lab/sound*.ts`;
  - sửa PNG atlas có sẵn;
  - ghi vào `art-src/lab/vfx/meta/`, `cutin-mat/`, `world/`, vì các thư mục này sẽ được cắt lại sau khi Firefly làm lại 14 clip;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Bảng ghép (đã chốt)
| Sự kiện | Flipbook (thư mục `art-src/lab/vfx/`) |
|---|---|
| Chết `thach-thu` | `beast/death-rat-stone-dust` |
| Chết `phong-lang` | `beast/death-wolf-wind-wisps` |
| Chết `thiet-giap-tru` | `beast/death-boar-iron-flakes` |
| Chết `hoa-nha` | `beast/death-crow-ember-ash` |
| Chết `nham-vien` | `beast/death-ape-rock-crumble` |
| Chết loài khác, không rõ loài | `beast/beast-death-ink-smoke` |
| Chết boss `thiet-boi-lang-vuong` (bậc ≥ 4) | `boss/boss-death-explosion-r2` ngay khung chết, `boss/boss-death-ink-smoke-ring` +0,15 s, `boss/boss-spirit-ascend` +0,4 s |
| Trúng đòn nhẹ | `beast/beast-hit-spark-burst` |
| Trúng đòn có hướng (nhát chém, dải bay) | `beast/beast-hit-ink-streak`, xoay theo hướng đòn |
| Trúng đòn nặng hoặc tuyệt kỹ (`damage` `heavy` hoặc `ult`) | `beast/beast-hit-heavy-ink-burst` |
| Bắt đầu choáng (`stun`) | `beast/stagger-stars-loop` trên đầu, lặp suốt thời gian choáng; tinh anh và boss thêm `beast/posture-break-shatter` một lần lúc bắt đầu |
| Bị trói (`bind`) | `mech/mech-seal-net-bind` trên thân lúc bắt đầu trói |

Loài lấy từ quái thật (herd, greybox, swarm), giống cách `sound.ts` đọc loài (`beast(e, species)`). Không đoán theo bậc khi đã có loài.

## Danh sách việc
1. **`FoeFlipbookFx`** (`src/lab/foe-flipbook-fx.ts`):
   - chạy bảng ghép trên;
   - tâm hình ở vị trí quái, theo `pivot` của atlas;
   - cỡ theo bán kính thân quái: hình chính rộng khoảng 1,3–1,6 lần bề ngang thân ở camera chơi (khoảng 37 px một mét ở 1080p); boss lớn hơn theo thân boss;
   - pha trộn và chế độ đúng manifest (`fire` cộng sáng, `smoke` thường), tốc độ khung đúng JSON atlas;
   - chạy một lần rồi trả về bể; vòng lặp choáng tắt khi hết choáng hoặc quái chết.
   - **Đạt khi:** có test node cho chọn flipbook theo loài và sự kiện, quay về `beast-death-ink-smoke` khi thiếu loài, vòng lặp choáng bật và tắt đúng giờ.
2. **Đám đông và lớp cũ:**
   - Gộp theo xô 50 ms như âm. Mỗi xô tối đa 10 hình chết và 8 hình trúng; chọn quái bậc cao trước, rồi gần giữa màn hình. Tối đa 12 vòng lặp choáng hoặc trói cùng lúc.
   - Khi một cái chết có flipbook, `DeathFx` bỏ lớp hình vẽ bằng mã của cái chết đó: mảnh vỡ, vệt mực, sợi khí, mảnh sáng. Giữ chớp sáng, vòng sốc, vết cháy đất và tia linh khí. Cái chết vượt giới hạn xô giữ nguyên `DeathFx` cũ.
   - `?deathfx=old` trả lại `DeathFx` cũ đầy đủ, không flipbook, để anh so A/B.
   - **Đạt khi:** có test cho giới hạn xô, thứ tự ưu tiên, `?deathfx=old`, không cấp phát mỗi khung sau khi bể đã ấm.
3. **Bộ nhớ:**
   - Nạp lười atlas lần đầu dùng, giải phóng atlas không dùng sau 20 s.
   - Nếu `tools/vfx-flipbook/run.sh` có lệnh làm KTX2 cho atlas có sẵn (phiếu 325) thì tạo `.ktx2` cho các atlas bảng ghép dùng và ghi mục `ktx2` vào manifest; lab tự quay về PNG khi thiếu.
   - **Đạt khi:** báo cáo có bộ nhớ GPU ước tính (RGBA hoặc KTX2) khi mọi atlas bảng ghép cùng nạp; nếu tạo KTX2 thì bộ kiểm manifest báo `0 problems` cho `beast/`, `boss/`, `mech/`.
4. **Kiểm cuối:**
   - `npx --no-install tsc --noEmit` sạch;
   - `npx --no-install vitest run --maxWorkers=4` qua toàn bộ. Ghi số test trước và sau.
   - Báo cáo ghi rõ những gì cần xem bằng mắt (Claude sẽ chạy lab 3146 và quay video cho anh).

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
