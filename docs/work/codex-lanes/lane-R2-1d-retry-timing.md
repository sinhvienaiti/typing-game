# Vòng 2 · Bước 1d · Thử lại bước 1 một lần: chỉ đổi nhịp vòng ấn Lôi

Kết quả chấm mù bước 1: `docs/work/consult/r2-step1-verdict.md`, **TRƯỢT**. "Nhịp và lực" cùng "tương tác" chỉ tăng 0,5. Lỗi lớn nhất: vòng ấn nở sau tia phóng (R0+0,03–0,20 s), nên không đọc được nhịp "tụ rồi bật".

**Chỉ đổi một điều** (theo mục "Một thay đổi cụ thể" của bản chấm):
- đoạn tăng sáng của vòng ấn Lôi (`thunder-caster-seal`, bước 1) dời vào **150 ms cuối của pha tụ lực**, đạt đỉnh **đúng khung phóng**, rồi bắt đầu tan;
- giữ nguyên nguồn, cỡ, số lớp và các lớp khác, để lần thử chỉ đo nhịp;
- không dời sự kiện gameplay. Nếu pha tụ lực ngắn hơn 150 ms thì tăng sáng suốt pha tụ lực.

**Mức `high`.** Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:** `src/lab/thunder-caster-r2.ts` và test của nó; báo cáo `docs/codex-queue/laneR2-report.md` (≤ 5 dòng).
- **Ngân sách:** như bước 1 (`path-to-8.md` §7).

**Đạt khi:**
- test: vòng đạt đỉnh đúng khung phóng, bắt đầu tăng 150 ms trước đó, `tp2` tắt thì không đổi;
- `npx --no-install tsc --noEmit` sạch;
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ.

## Chốt của Claude (07/11 12:35, sau khi lượt trước báo blocked)
- Phím 8 trong lab tung chiêu tức thì, nên không có "trước lúc phóng". Trong game thật chiêu được tung bằng cách **gõ từ**. Vì vậy: khi lab ở chế độ gõ (`typed=1`, có từ cho chiêu phím 8), vòng ấn **sáng theo tiến độ gõ của từ** (ký tự đúng / độ dài từ, như `charge-fill-fx` của phím 2–7) và đạt đỉnh đúng ký tự cuối (khung phóng). Khi tung tức thì không có từ, vòng hiện ở đỉnh ngay khung phóng rồi tan; không thêm độ trễ.
- **Được sửa thêm:** `src/lab/five-phase-clip.ts` (chỗ nối nhận tiến độ gõ trước khi phóng) và chỗ đọc tiến độ gõ trong `src/lab/skills-main.ts`, tối thiểu. Không đổi sự kiện hay thời điểm gameplay.
- **Kịch bản quay:** cảnh `TP` trong `scripts/visual/scenarios/lab-pilot-ab.mjs` thêm `typed=1` cùng `wpm` như các cảnh khác, để có pha tụ lực theo gõ. Ghi vào báo cáo.
- Tự chạy `npx --no-install vitest run --maxWorkers=4` toàn bộ.
