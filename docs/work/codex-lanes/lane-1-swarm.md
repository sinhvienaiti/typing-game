# Làn Codex 1 · Song Long phím 2: sát thương rồi đo cân bằng (danh sách việc, làm lần lượt)

Anh (06/11 22:00): "tăng agent của codex lên 3… giao việc theo list vào 1 file md, kêu nó làm và kiểm tra kỹ từng việc, pass mới sang việc khác". Phần A (phiếu 293, đường bay, nhịp, sự kiện) đã xong và đã commit (`35f3202`, nhánh `codex/key2-swarm-sim`). Đây là danh sách tiếp theo của **làn 1**. Làm **lần lượt**; xong một việc thì tự kiểm theo "Đạt khi", ghi một đoạn vào báo cáo, rồi mới sang việc kế tiếp.

**Model `gpt-6.1-sol`, mức `ultra`.** Báo cáo duy nhất: `docs/codex-queue/lane1-report.md` (tiếng Việt, ngắn).

## Nơi làm và ranh giới
- Worktree `games/.wt-ic-swarm-sim`, nhánh `codex/key2-swarm-sim` (đã có phần A). Không đụng worktree khác, không đụng `art-src`.
- Không lệnh git ghi (Claude commit). Không mở cổng mạng. Không float, `Math.sin/cos/atan2/random` trong sim.
- Biến thể vẫn sau cờ header `swordKey2 = "swarm"`. **Cờ tắt hoặc `"twin-pearl"`: hành vi và băm replay không đổi** (bốn dãy băm ghim trong `tests/sim/twin-pearl.test.ts` phải còn xanh).

## Nguồn thiết kế (anh đã duyệt, là nguồn duy nhất về luật và số)
`docs/games/tu-tien/skills/DRAGON_SKILL.md` §10.4 (sát thương), §10.5 (sự kiện), §10.7 (thứ tự), cộng phần "Vòng 3" cuối `docs/codex-queue/293-tt-key2-swarm-sim-routes.md`. Theo Vòng 3, **nổ ngọc không còn ở F260 cố định**: dùng tick nổ đã tính ở phần A (max(tick lao) + 32), và tick hết = tick nổ + 40. Ở mọi chỗ §10.4–10.5 ghi F260 hay F300, hiểu là tick nổ và tick hết của lần tung đó.

## Danh sách việc
### Việc 1 · Phiếu 294: sát thương ba kênh
- **Sóng thả, chạm thân, nổ ngọc** đúng số khởi điểm §10.4 (0,5 W bán kính 6 m ở F1; 0,15 W mỗi quái một lần mỗi tung; quỹ 2,5 W chia theo trọng số khoảng cách với 1 đơn vị sàn, dư lớn nhất, hòa theo id).
- **Va chạm chạm thân** trên đoạn đường xoắn mà thân đang chiếm (≤ 0,85 m + hurtbox), lưới ô cho pha rộng, thứ tự tick → rồng → id quái.
- **Đòn đầu** như §10.4 (đã có phần chọn đích ở phần A; giờ thêm sát thương).
- **Trần** quái thường 2,5 W, boss 1,5 W mỗi tung; ba kênh chung một danh tính đòn diện rộng cho trần cụm 60 %; không chia lại phần bị cắt.
- **Sự kiện `hit`** thêm `castId`, `phase` (release/touch/burst), `dragon` (khi chạm). Phiên bản va chạm và sát thương vào `rulesHash` của biến thể.
- **Test mới:** bảo toàn quỹ (tổng chia đúng quỹ trước trần), thứ tự tất định, trần quái thường và boss, sóng thả đúng bán kính, mỗi quái chỉ bị chạm thân một lần mỗi tung, hai lần tung chồng tách riêng theo `castId`, nổ chụp đúng quái sống ở tick nổ.
- **Đạt khi:** `./node_modules/.bin/tsc --noEmit -p .` sạch; `./node_modules/.bin/vitest run --no-cache --configLoader runner --maxWorkers 4` toàn bộ qua (trước việc này: 90 file, 1.026 test); băm ghim không đổi.

### Việc 2 · Phiếu 295: đo cân bằng bằng bot (chỉ đo và chọn trong khoảng quét của §10.4)
- Dùng khung bot hiện có của game (`scripts/balance/run.ts`, `pnpm ic:balance`; đọc `docs/games/tu-tien/BALANCE.md` nếu có) để chạy bot Chuẩn với `swordKey2 = "swarm"`.
- Quét ba kênh trong khoảng §10.4 (sóng thả 0,3–0,7 W; chạm 0,10–0,20 W; nổ 2,0–3,5 W), ghi theo lần tung: độ dài đường, số đám phủ, tick đòn đầu, số quái bị chạm, sát thương từng kênh, phần bị trần cắt.
- Chọn bộ số đạt cả hai: phím 2 ≤ 45 % sát thương của bot Chuẩn, và bot Chuẩn thắng rõ hơn 15 %. Ghi bộ số vào `src/content/data/swarm.ts`.
- Không bộ số nào đạt: **không** sửa chiêu khác, chỉ ghi báo cáo đầy đủ để Claude và anh quyết.
- **Đạt khi:** tsc và vitest như việc 1 đều qua; báo cáo có bảng quét và bộ số chọn.

## Hết hạn mức
Giữ file, ghi báo cáo phần đã xong. Chỉ khi thật sự hết hạn mức mới ghi dòng cuối `CODEX-WAIT-UNTIL: HH:MM` (hoặc `unknown`).

## Cập nhật 06/11 22:30 (Claude)
- **Việc 1 đã xong và đã commit** (`d8457d1`). Không làm lại.
- **Việc 2 chạy tiếp:** Claude đã chép mã bộ bot của phiếu 272 (chỉ mã, không có kết quả cũ) vào `tmp/skill-reach/` của worktree này (thư mục `tmp` bị git bỏ qua). Cách dùng và bot Chuẩn: `docs/codex-queue/272-tt-twin-pearl-fieldwide-bot.md`, `docs/codex-queue/272-report.md` và báo cáo chi tiết (chỉ đọc) `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/tmp/skill-reach/key2-fieldwide/report.md`. `scripts/balance/run.ts` chỉ là chỗ giữ chỗ, không dùng.
- Kết quả quét ghi vào `tmp/skill-reach/swarm/` của worktree này, bảng tóm tắt vào báo cáo làn 1.
