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
