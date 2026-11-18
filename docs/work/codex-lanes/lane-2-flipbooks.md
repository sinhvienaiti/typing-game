# Làn Codex 2 · Video Firefly mới hôm nay → flipbook cho lab (danh sách việc, làm lần lượt)

Anh (06/11 22:00): "tăng agent của codex lên 3, đảm bảo list việc của 3 agent này k ảnh hưởng lẫn nhau… giao việc theo list vào 1 file md, kêu nó làm và kiểm tra kỹ từng việc, pass mới sang việc khác". Đây là danh sách của **làn 2**. Làm **lần lượt từng việc**; xong một việc thì tự kiểm theo mục "Đạt khi", ghi một đoạn vào báo cáo, rồi mới sang việc kế tiếp.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo duy nhất: `docs/codex-queue/lane2-report.md` (tiếng Việt, ngắn). Mỗi việc một đoạn: số clip, số atlas, cảnh báo, việc nào bỏ và vì sao.

## Ranh giới với hai làn kia (bắt buộc)
- **Làn 1** đang sửa mã sim Song Long trong `games/.wt-ic-swarm-sim`: không đụng.
- **Làn 3** vẽ ảnh vào `…/stills/skills/`: không đụng.
- **Phiên lab-flipbooks** của Claude quản các thư mục hệ `art-src/lab/vfx/<hệ>/`, `ult/`, `expansion/`, `weapon/`, `fire/`: **không ghi vào các thư mục đó**. Làn này chỉ ghi vào các **thư mục mới** liệt kê dưới đây.
- Không sửa mã game hay mã lab. Không lệnh git ghi. Không mở cổng mạng.

## Cách làm (đọc trước)
- Cách cắt clip thành atlas và viết manifest: `docs/work/tasks/lab-flipbooks.md` (mục Công cụ, Đầu ra, cách chọn khung và chế độ `fire` cho nền đen) và `tools/vfx-flipbook/README.md`.
- Công cụ: `tools/vfx-flipbook/run.sh` (`ingest`, `upgrade`). Đặt `VFXLAB_HOME=/Volumes/SS990TPRO/htdocs/typing-game/.local/vfxlab-lane2` (trong repo; sandbox không cho ghi ra ngoài).
- Cấu hình clip: thêm mục mới vào `tools/vfx-flipbook/immortality-cultivation.json`, không sửa mục cũ.
- Ý nghĩa từng clip: trường `use` của việc tương ứng trong `docs/work/tasks/firefly-sprint-video.json`.
- Video: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/video/<job>/take1.mp4` (bỏ việc chưa có file; ghi vào báo cáo).
- Định dạng manifest đúng như `art-src/lab/vfx/fire/manifest.json`; mỗi mục có `role`, `job`, `take`, `source`. Vai trò lấy theo `use`: `impact`, `burst`, `groundMark`, `aura` (vòng lặp quanh thân), `trail`, `telegraph`, `death`, `ambient`, `ui`, `cutin`; vai nào mới thì ghi rõ trong báo cáo.
- Bộ kiểm manifest: `cd games/immortality-cultivation && node_modules/.bin/tsx /Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/lab-flipbooks/validate-manifests.ts` (chỉ đọc). Ghi số mục trước và sau mỗi việc.

## Danh sách việc
| # | Việc | Clip (id việc video) | Thư mục ra (mới) |
|---|---|---|---|
| 1 | Đòn của boss và quái làm từ ảnh | 16 việc `i2v-foe-*` | `art-src/lab/vfx/foe-i2v/` |
| 2 | Đòn quái làm từ chữ (đỏ nguy hiểm) | các việc `foe-*` (telegraph, charge-gather, claw-rake, bite-snap, ground-slam, charge-dash-trail, rock, dive, roar-wave, howl-ring, summon-smoke, victim-red-flash, projectile) và `formation-heart-hit-ripple` | `art-src/lab/vfx/foe/` |
| 3 | Thú trúng đòn và chết | `beast-*`, `death-*` (rat, wolf, crow, ape, boar), `posture-break-shatter`, `stagger-stars-loop` | `art-src/lab/vfx/beast/` |
| 4 | Tinh anh, đội trưởng, boss | `elite-aura-*`, `captain-*`, `boss-*` | `art-src/lab/vfx/boss/` |
| 5 | Thế giới và Thiên Kiếp | `world-*`, `tide-*`, `tribulation-*`, `formation-heart-breath-loop`, `formation-heart-restore-swell` | `art-src/lab/vfx/world/` |
| 6 | Thưởng, UI, thẻ vật phẩm, anh hùng | `reward-*`, `results-*`, `realm-up-burst`, `wave-clear-sweep`, `van-khi-motes-rise`, `ui-*`, `card-glow-*`, `hero-*`, `meditation-*` | `art-src/lab/vfx/meta/` |
| 7 | Chất liệu cut-in | `cutin-*` của hôm nay (bỏ các bản `-w2` cũ) | `art-src/lab/vfx/cutin-mat/` |
| 8 | Hiện hình và giữ của 30 chiêu mở rộng | `i2v-*-manifest`, `i2v-*-hold` | `art-src/lab/vfx/expansion-phases/` |

Clip vòng lặp (`-loop` trong id) cắt thành vòng lặp liền (`loop: true`). Nền đen dùng chế độ `fire` (cộng sáng). Clip mực trắng trên đen (`ink`, `smoke` có chữ "white") ghi `mode: "smoke"`, `blend: "normal"` như các bản `dark-*-white` trong `lab-flipbooks.md`.

## Đạt khi (mỗi việc)
- Mọi clip có file đều ra atlas và mục manifest. Bộ kiểm manifest báo `0 problems`, số mục tăng đúng bằng số clip của việc.
- Không atlas nào lớn hơn 4096 px mỗi cạnh.
- Xem tấm ghép khung (`sheet`) của từng clip bằng `view_image`: không bị cắt mép hình chính, không trống. Clip nào lỗi thì ghi rõ và bỏ, không làm lại bằng tay.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`); làm xong thì không ghi.
