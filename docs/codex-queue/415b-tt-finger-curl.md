# Phiếu 415b: Cong ngón mềm cho rig `human` (tách từ 415 sau 3 vòng phản biện)


Phản biện: PASS (Sonnet, 16/11; tách 415 sau 3 vòng, 415b sửa tỉ lệ ngón cái)
## Bối cảnh
Thủ ấn 412 có ngón gập thành móc cụt (agent Claude Opus, 16/11; ảnh `typing-game-review/owner-review/2026-11-16/tu-tien/hero-anim-r3/seals-412-vs-ref.jpg`). Ảnh đích ngón cong mềm: `games/immortality-cultivation/art-src/concept/hand-seals/seals-sheet-411.jpg`. Chạy sau 415 trong cùng làn B (đọc lại các file `src/lab/anim-r*`, giữ phần của 415).

## Việc (worktree `games/.wt-ic-lab-all`, `src/lab/anim-r*`)
1. Một tham số gập tổng `curl` (0–1) cho mỗi ngón, chia cho ba đốt theo tỉ lệ gốc : giữa : ngọn = 1 : 1,1 : 0,8 (ngón trỏ–út) và 1 : 1,2 : 1,4 (ngón cái).
2. Giới hạn góc tối đa mỗi đốt khi `curl = 1`: ngón trỏ–út gốc 85°, giữa 100°, ngọn 75°; ngón cái gốc 50°, giữa 60°, ngọn 70°.
3. Áp lại vào 10 ấn của `anim-r3-seals.json`: ngón "gập" dùng `curl` 0,75–1; ngón "duỗi" `curl` ≤ 0,15.

## Nghiệm thu (Codex tự đo)
- TypeScript strict + `noUncheckedIndexedAccess` cho các file sửa: 0 lỗi.
- `anim-r3-check` in và đạt cho mọi ngón ở mọi ấn: tỉ lệ góc ba đốt khớp tỉ lệ của loại ngón đó (mục 1) với sai số ±15 %; không đốt nào vượt giới hạn mục 2; trạng thái gập/duỗi khớp `anim-r3-seals.json`; các cổng cũ (≥ 4 mm, ≤ 50 ms) vẫn đạt.
- Để lệnh chụp cận tay 10 ấn cho Claude; agent Claude Opus chấm mắt sau (ngoài nghiệm thu Codex).
- Chỉ sửa `src/lab/anim-r*` trong worktree. Không commit, không media vào Git, không đổi nhánh.

## Giao nộp
`docs/codex-queue/415b-report.md`.
