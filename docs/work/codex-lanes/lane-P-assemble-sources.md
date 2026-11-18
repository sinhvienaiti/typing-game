# Phiếu làm thử · Lắp 4 nguồn mới vào thư mục đè `vfx-pilot-2026-11-07`

Bối cảnh: `docs/work/tasks/vfx-pilot-0711.md`. Lab đọc thư mục đè khi bật `?pilot=1` (phiếu `lane-P-lab-pilot-flag.md`). Quy trình: `.agents/skills/game-vfx-production/references/path-to-8.md` §1 (tầng A), §2.

**Model `gpt-6.1-sol`, mức `high`.** Báo cáo: `docs/codex-queue/lanePilot-report.md` (thêm đoạn ≤ 8 dòng). **Tối đa 14 ảnh** xem trong lần chạy; dùng tấm ghép.

## Việc
Đầu ra ở `games/immortality-cultivation/art-src/lab/vfx-pilot-2026-11-07/<kit>/`:
- atlas PNG và KTX2 (`tools/vfx-flipbook/run.sh`, rồi `run.sh ktx2`, `VFXLAB_HOME=.local/vfxlab-pilot`);
- `manifest.json` cùng lược đồ manifest kit, **cùng id** với mục cần đè, kèm `envelope` (lược đồ trong phiếu cờ).

1. **P1 · `boss/boss-entrance-vortex`.** Nguồn: `firefly-sprint-2026-11-05/video/boss-entrance-vortex-i2v/take1.mp4` và `take2.mp4`, làm từ ảnh try2 anh duyệt.
   - Kiểm tầng A cả 2 take, chọn 1 take, chọn đoạn lặp hoặc giữ ổn định nhất. Hình cổng giữ đúng; nhịp do engine làm.
   - `envelope`: mở trong 0,25 s (scale 0,6 → 1,0, alpha 0 → 1); giữ và xoay theo clip; cuối 0,4 s sụp vào tâm (scale 1,0 → 0,2, alpha → 0, ăn mòn từ ngoài vào). Tổng khoảng 1,6 s.
2. **P2 · `blood/blood-ring-burst`.** Nguồn: `blood-ring-burst-i2v/take1.mp4` và `take2.mp4`. Vòng giữ hình nhưng không tự nở.
   - Chọn 1 take, lấy đoạn sáng đều.
   - `envelope`: nở nhanh 0,45 s (scale 0,35 → 1,15, ease-out); alpha 1 tới 0,55 s; ăn mòn từ mép ngoài tới 1,1 s.
3. **P3 · `fire/i2v-fire-comet`.** Nguồn: bản dẫn xuất của luồng 1 ở `art-src/lab/vfx-redo-2026-11-07/keep/i2v-fire-comet/v1/` và `recipe.md` của nó.
   - Chép atlas và recipe sang thư mục đè, `envelope` theo recipe.
   - Chưa có bản dẫn xuất thì ghi "chờ S1" và bỏ qua mục này.
4. **P4 · `beast/beast-hit-spark-burst`.** Nguồn: mẫu Blender tốt nhất của luồng 3 ở `art-src/lab/vfx-redo-2026-11-07/blender/beast-hit-spark-burst/v*/` (RGBA).
   - Cắt flipbook từ chuỗi PNG RGBA (nền trong suốt, chế độ cộng sáng theo vai trò cũ). Giữ ≥ 24 khung.
   - Chưa có mẫu thì ghi "chờ S3" và bỏ qua mục này.

**Mỗi mục:**
- kiểm tầng A (5 ô) trên bản đóng gói, ghi số đo;
- dựng tấm so bản cũ và bản mới, 6 khung mỗi bên, cùng cỡ, vào `.local/pilot/<id>-compare.jpg`.

## Ranh giới
- **Chỉ ghi:**
  - `art-src/lab/vfx-pilot-2026-11-07/`;
  - `.local/vfxlab-pilot/`, `.local/pilot/`;
  - báo cáo.
- **Không:** sửa nguồn, manifest đang dùng hay mã; lệnh git ghi; mở cổng mạng; mở trình duyệt.

## Hết hạn mức
Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
