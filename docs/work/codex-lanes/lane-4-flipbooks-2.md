# Làn Codex 4 · Flipbook đợt 2: clip Firefly làm xong sau làn 2

Anh (07/11 00:46): muốn thêm 2 làn Codex để làm nhanh nhưng không tốn token vô lý. Hàng video Firefly đã xong lúc 00:45. Làn 2 (`lane-2-flipbooks.md`, báo cáo `docs/codex-queue/lane2-report.md`) đã cắt 79 atlas, bỏ 46 việc vì lúc đó chưa có file. Làn này cắt **74 clip còn lại** và **cắt lại 7 mục** từng lấy nhầm clip trùng.

**Model `gpt-6.1-sol`, mức `medium`** (việc máy móc). Báo cáo duy nhất: `docs/codex-queue/lane4-report.md` (tiếng Việt, ngắn). Làm lần lượt từng việc. Xong việc nào thì tự kiểm theo "Đạt khi", ghi một đoạn vào báo cáo, rồi mới sang việc kế.

## Cách làm
Giống hệt làn 2. Đọc mục "Cách làm" và "Đạt khi" của `docs/work/codex-lanes/lane-2-flipbooks.md` và làm theo: công cụ, chế độ `fire` hay `smoke`, vòng lặp liền cho id có `-loop`, định dạng manifest, bộ kiểm manifest. Chỉ khác ba chỗ:
- `VFXLAB_HOME=/Volumes/SS990TPRO/htdocs/typing-game/.local/vfxlab-lane4`.
- Clip: dùng take hợp lệ mới nhất trong thư mục việc. **Bỏ mọi file có `wrong-dup` trong tên.**
- Không cắt `i2v-recheck-fire-comet` và `i2v-recheck2-fire-comet`. Đây chỉ là clip thử lỗi Content Credentials.

## Ranh giới
- **Được ghi:**
  - các thư mục ở bảng dưới (thêm mục mới vào manifest, giữ nguyên mục cũ);
  - riêng việc 11, thay đúng mục được nêu;
  - `tools/vfx-flipbook/immortality-cultivation.json` (thêm mục mới; việc 11 thì sửa đúng mục của clip đó);
  - `.local/vfxlab-lane4/`;
  - báo cáo.
- **Cấm:**
  - sửa mã game hay mã lab;
  - sửa file trong `firefly-sprint-2026-11-05/`;
  - ghi vào `art-src/lab/audio/`, vì làn 5 đang làm âm;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Danh sách việc
| # | Việc | Clip (id việc video) | Thư mục ra |
|---|---|---|---|
| 1 | Thú chết | `beast-dissolve-edge-noise`, `death-ape-rock-crumble`, `death-boar-iron-flakes`, `death-crow-ember-ash`, `death-rat-stone-dust`, `death-wolf-wind-wisps` | `art-src/lab/vfx/beast/` |
| 2 | Boss, đội trưởng | `boss-charge-impact-r2`, `boss-death-explosion-r2`, `boss-death-ink-smoke-ring`, `boss-iron-charge-sparks-loop`, `boss-spirit-ascend`, `captain-aura-ground-loop` | `art-src/lab/vfx/boss/` |
| 3 | Đòn quái | `foe-projectile-core-loop`, `foe-rock-impact-shatter-r2` (làn 2 đã loại bản cũ vì cụt mép) | `art-src/lab/vfx/foe/` |
| 4 | Thế giới, Thiên Kiếp | `world-cloud-sea-loop`, `world-dust-motes-loop`, `world-light-shafts-loop`, `world-mist-loop`, `tide-wave-surge`, `tribulation-phantom-wisp-loop`, `tribulation-static-fill-loop`, `formation-heart-breath-loop`, `formation-heart-restore-swell`, `sky-route-ember-stream-loop` | `art-src/lab/vfx/world/` |
| 5 | Thưởng, UI, thẻ, anh hùng | `card-glow-base-loop`, `card-glow-ascended-loop`, `card-glow-supreme-loop`, `hero-down-qi-scatter`, `hero-golden-body-shell-loop`, `hero-halo-ring-loop`, `hero-pill-heal-swell`, `hero-presence-ring-loop`, `hero-qi-motes-idle-loop`, `hero-ultimate-ready-aura-loop`, `meditation-heart-demon-smoke-loop`, `realm-up-burst`, `results-star-burst`, `results-victory-rays-loop`, `reward-drop-glow-loop`, `ui-sunburst-halo-loop`, `van-khi-motes-rise`, `wave-clear-sweep` | `art-src/lab/vfx/meta/` |
| 6 | Chất liệu cut-in | `cutin-cloud-wipe`, `cutin-ember-drift`, `cutin-gold-rays`, `cutin-ink-bloom`, `cutin-ink-wash-sweep`, `cutin-light-petals-drift`, `cutin-seal-stamp-splash`, `cutin-speed-lines-loop` | `art-src/lab/vfx/cutin-mat/` |
| 7 | Hiện hình làm lại | `i2v-mountain-crushing-imperial-seal-manifest-r2`, `i2v-yin-yang-void-mirror-manifest-r2`: **thay** mục cũ cùng chiêu (cùng vai) trong manifest, không thêm mục trùng vai | `art-src/lab/vfx/expansion-phases/` |
| 8 | Tụ lực theo hệ (mới) | `i2v-<hệ>-charge-fill` của 13 hệ: blood dark earth fire ice light metal poison star thunder void water wind wood (đủ 14 id nếu có). Vai `charge`; ghi trường `element` | `art-src/lab/vfx/charge-fill/` (mới) |
| 9 | Cơ chế (mới) | `mech-chain-lightning-arc`, `mech-seal-net-bind`, `barrier-edge-flow-strip`, `pillar-shelter-ward-loop` | `art-src/lab/vfx/mech/` (mới) |
| 10 | Rồng khí, hoa sen (mới) | `spirit-dragon-side`, `spirit-dragon-unified`, `dragon-fire-body-ribbon`, `fire-lotus-bloom-top` | `art-src/lab/vfx/spirit/` (mới) |
| 11 | Cắt lại mục lấy nhầm clip trùng | `void-wave`, `dark-big-burst`, `style-w3-fire-ribbon`, `death-crow-ember-ash`, `wave-clear-sweep`, `i2v-mountain-crushing-imperial-seal-manifest`, `i2v-yin-yang-void-mirror-manifest` | thư mục đang chứa mục đó |

**Việc 11, cách làm:**
- Với mỗi job, tìm mọi mục manifest trong `art-src/lab/vfx/*/manifest.json` có `job` bằng nó.
- Mục nào có atlas cũ hơn take hợp lệ hiện tại (so `mtime`, hoặc MD5 nguồn khác clip đã cắt) thì cắt lại từ take hợp lệ. Nếu có việc `-r2` thì dùng clip của việc `-r2`.
- Giữ nguyên khoá, vai và đường dẫn atlas.
- Mục đã mới hơn take (ví dụ `void-wave` đã cắt lại) thì bỏ qua và ghi vào báo cáo.

## Đạt khi
- Như làn 2:
  - bộ kiểm manifest báo `0 problems` trong các thư mục làn này ghi;
  - số mục tăng đúng bằng số clip của việc (việc 7 và 11: không tăng);
  - không atlas nào lớn hơn 4096 px mỗi cạnh;
  - xem `sheet` từng clip bằng `view_image`: không cụt mép hình chính, không trống. Clip lỗi thì ghi rõ và bỏ, không làm lại bằng tay.
- Báo cáo cuối có tổng: số atlas, MiB, số clip bỏ và lý do.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`). Làm xong thì không ghi.
