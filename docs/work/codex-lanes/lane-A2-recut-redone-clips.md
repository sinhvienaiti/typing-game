# Làn Codex A · Việc A2 · Cắt lại flipbook cho 12 clip Firefly vừa làm lại

Bối cảnh (07/11 01:50):
- 14 clip lưu từ 23:55 đến 00:30 bị lưu nhầm, đều là biến thể của `i2v-nether-samsara-monarch-avatar-manifest`.
- Claude đã gạt chúng thành `take1.wrong-ref.mp4`. Atlas làn 4 cắt từ chúng đã chuyển vào `<thư mục>/.wrong-ref-2026-11-07/` và gỡ khỏi manifest.
- Firefly đã làm lại cả 14 (01:14–01:40). Claude đã xem tấm ghép: đúng prompt, không clip nào trùng.
- `void-wave` và `dark-big-burst` thuộc bộ hệ, phiên lab-flipbooks đã tự xử lý: **không đụng**.

**Model `gpt-6.1-sol`, mức `medium`** (việc máy móc). Báo cáo: `docs/codex-queue/laneA2-report.md` (tiếng Việt, ngắn).

## Cách làm
Giống hệt làn 4 (`docs/work/codex-lanes/lane-4-flipbooks-2.md`, mục "Cách làm" và "Đạt khi"):
- `VFXLAB_HOME=/Volumes/SS990TPRO/htdocs/typing-game/.local/vfxlab-laneA2`;
- clip là `take1.mp4` hiện tại. Bỏ mọi file có `wrong-` trong tên;
- thêm mục mới vào manifest. Cấu hình trong `tools/vfx-flipbook/immortality-cultivation.json` đã có từ làn 4 thì dùng lại, chỉ cập nhật `source` hoặc MD5 nếu cần;
- nếu lệnh `run.sh ktx2` của việc A1 đã có và chạy được, nén KTX2 luôn cho các atlas mới (`--only` đúng các id này).

## Danh sách việc
| # | Clip | Thư mục ra |
|---|---|---|
| 1 | `realm-up-burst`, `ui-sunburst-halo-loop`, `hero-down-qi-scatter`, `hero-halo-ring-loop`, `van-khi-motes-rise` | `art-src/lab/vfx/meta/` |
| 2 | `cutin-ink-wash-sweep`, `cutin-gold-rays`, `cutin-ember-drift`, `cutin-seal-stamp-splash`, `cutin-speed-lines-loop` | `art-src/lab/vfx/cutin-mat/` |
| 3 | `sky-route-ember-stream-loop`, `formation-heart-restore-swell` | `art-src/lab/vfx/world/` |
| 4 | `i2v-mountain-crushing-imperial-seal-manifest-r2`, thêm mới cùng vai với các mục `-manifest` khác. Làn 4 đã cắt bản này trong `.local/vfxlab-lane4/`, ấn đủ khung. **Không** thêm `i2v-yin-yang-void-mirror-manifest-r2`, vì vành dưới cụt biên lúc nở; ghi vào báo cáo | `art-src/lab/vfx/expansion-phases/` |

## Ranh giới
- **Được ghi:**
  - 4 thư mục trên, chỉ thêm mục mới hoặc thay mục cùng id;
  - cấu hình flipbook;
  - `.local/vfxlab-laneA2/`;
  - báo cáo.
- **Cấm:**
  - đụng `.wrong-ref-2026-11-07/` và mọi thư mục `vfx` khác (các thư mục hệ, `beast/`, `boss/`, `foe/`, `mech/`);
  - sửa mã lab hay game, sửa video gốc;
  - lệnh git ghi, mở cổng mạng, mở trình duyệt.

## Đạt khi
- Bộ kiểm manifest `0 problems` cho 4 thư mục. Số mục tăng đúng số atlas giữ lại.
- Mỗi cạnh ≤ 4096 px. Vòng lặp (`-loop`) nối liền, chỉ số nối ≤ 1,0.
- Xem `sheet` từng clip bằng `view_image`: không cụt mép hình chính, không trống. Clip lỗi thì ghi rõ và bỏ.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
