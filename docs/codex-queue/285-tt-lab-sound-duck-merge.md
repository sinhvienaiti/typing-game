# Phiếu 285 · Tu Tiên · Âm: gộp tiếng trúng hàng loạt, ép bus khi cao trào và khi tiếng hô (sau 269)

**Loại việc:** âm và code lab (`gpt-6.1-sol`, mức `xhigh`). Phiếu ngắn theo luật làm gọn 05/11, không đụng sim, canon hay cân bằng, nên không cần phản biện. Làm ngay.

**Báo cáo:** `docs/codex-queue/285-report.md`.

**Worktree:** `games/.wt-ic-sound-mix`, nhánh `codex/sound-mix-duck`, nền `bbb46d8` (main của game, đã có 269). Lúc giao `git status --short` chỉ có `?? node_modules`.

## Vì sao
- Ba việc anh đã duyệt, đang đỗ trên `docs/work/BOARD.md`: "lớp gộp tiếng trúng hàng loạt, giới hạn số tiếng; tiếng hô hạ các âm khác".
- Báo cáo 269 (dòng 191) ghi chưa có limiter sống hay duck bus. Bản trộn đủ có đỉnh cao hơn cao trào, vì tiếng trúng, chết và bay qua cộng dồn.
- Âm chiến đấu phải mạnh và có tầng to nhỏ (`.agents/skills/game-art-pipeline/references/audio.md` §5): cao trào phải là đỉnh to nhất.

## Việc (trong `src/lab/sound.ts`, `src/lab/sound-tiers.ts`)
1. **Gộp tiếng hàng loạt:**
   - Với các nhóm `impact-*`, `death`, `flyby`: trong cửa sổ 120 ms, mỗi nhóm phát tối đa N tiếng (`impact` 4, `death` 3, `flyby` 2).
   - Sự kiện thứ N+1 trở đi trong cửa sổ **không phát tiếng mới**. Thay vào đó cộng vào tiếng đầu của cửa sổ một lần tăng mức, tối đa +1,5 dB tổng, qua GainNode riêng của tiếng đó; không vượt trần true peak của tầng (`sound-tiers.ts`).
   - Ghi số tiếng bị gộp vào bản ghi offline.
2. **Ép bus khi cao trào:**
   - Khi `world-climax` hoặc `world-climax-<element>` phát, bus `combat` hạ −6 dB: tấn công 20 ms, giữ suốt độ dài take, nhả 300 ms.
   - Bus `world` và `voice` không bị ép.
3. **Ép khi tiếng hô:**
   - Khi một take bus `voice` (callout) phát, bus `combat` và `world` hạ −4 dB: tấn công 30 ms, giữ suốt độ dài take, nhả 250 ms.
   - Nếu đang có ép cao trào thì lấy mức hạ sâu hơn, không cộng hai lần.
4. **Bản trộn offline:** bản ghi (`recording`) và bộ trộn offline (`scripts/audio/…`, nơi 269 đã viết) áp đúng ba luật trên, để video thử ra cùng mức với chơi sống.
5. **Không đổi:** trim từng tiếng, nhánh vang chung, nhịp `hush` (duck 8 % có sẵn).

### Được ghi
`src/lab/sound.ts`, `src/lab/sound-tiers.ts`, các script trộn offline của 269 trong `scripts/audio/`, các test hiện có của âm lab (cập nhật ca kiểm hành vi cũ, không nới), test mới `tests/lab/sound-duck-merge.test.ts` (hoặc đúng thư mục test âm lab đang dùng), changelog `docs/changelog/2026-11-05-lab-sound-duck-merge.md`, và `docs/codex-queue/285-report.md` ở repo cha.

### Cấm
Lệnh git ghi; sửa sim, nội dung, kit, `art-src` (không sửa hay tạo file âm); mở cổng mạng; chạy model AI.

## Kiểm bắt buộc
1. `tsc --noEmit -p .` không lỗi.
2. Vitest đủ (`--no-cache --configLoader runner --maxWorkers 4`): mọi test qua.
3. Test mới, trên đồng hồ giả và AudioContext giả:
   - 20 `impact` trong 100 ms tạo đúng 4 nguồn phát;
   - tổng tăng mức ≤ +1,5 dB;
   - lúc cao trào, gain bus `combat` xuống −6 dB ±0,2 trong 20 ms và về lại sau khi nhả;
   - tiếng hô chồng lên cao trào thì lấy mức hạ sâu hơn, không cộng hai lần.
4. Bản trộn offline của kịch bản đủ mà 269 dùng (cao trào phím 5 giữa bầy):
   - đỉnh ngắn hạn (LUFS-S 400 ms) của cao trào cao hơn đỉnh của đợt trúng hàng loạt ít nhất 3 LU;
   - in bảng trước và sau.
5. `git status --short` chỉ có các tệp được ghi.

## Claude làm sau
Quay video trước/sau (chiêu phím 5 và phím 7 giữa bầy), gửi anh nghe; anh duyệt thì gộp.

## Hết hạn mức
Giữ file, viết báo cáo phần đã xong. Dòng cuối ghi `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).
