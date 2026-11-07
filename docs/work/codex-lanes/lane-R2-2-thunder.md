# Vòng 2 · Bước 2 · Cột Lôi: chỉ pha bay (đường dẫn từ người tung lên trời tới vùng giáng) và thân cột giáng xuống, sau cờ `tp2=1`

Tiếp sau bước 1, đã được Claude đo và mở cổng trong `LANE-1.md`. Thiết kế lớp và nhịp: `docs/work/consult/codex-pilot-verdict.md` §4.2–4.3, hàng của pha này. Luật: `.agents/skills/game-vfx-production/references/path-to-8.md` §7 (bước nhỏ, ngân sách hiệu năng).

**Lớp của bước này:** `thunder-ribbon-loop` làm dải đường dẫn có texture (đầu và cuối đúng socket và đích, hạt nhỏ chạy theo); thân cột `vfx/ult/pillar-thunder-single` (chọn đoạn hữu ích, canh pivot đáy và cỡ, một instance, không mảng trắng; halo và sparkle phụ từ nguồn Lôi).

**Làm gì:**
- Chồng lên bước trước sau cùng cờ `tp2=1`. Tắt cờ thì B8 giữ nguyên từng khung.
- Không đổi thời gian, sát thương, sự kiện hay trạng thái. Phím đến lúc phóng ≤ 50 ms.

**Ngân sách cho cả Cột Lôi khi bật `tp2`:**
- +1,0 ms p95 tối đa;
- ≤ 12 draw call thêm, tính tổng các bước;
- không cấp phát mỗi khung;
- ≤ 64 MB texture thêm;
- bước này khoảng ≤ 250 dòng mã;
- không thêm shader mới.

**Mức `high`.** Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:** `src/lab/thunder-caster-r2.ts` hoặc một file nhỏ cùng mẫu, `src/lab/five-phase-clip.ts`, chỗ nối trong `src/lab/skills-main.ts`, test trong `tests/lab/`, báo cáo.
- **Không:** sửa media hay manifest.

**Đạt khi:**
- test node cho đúng khung bật và tắt từng lớp, `tp2` tắt thì không đổi, không cấp phát, tổng draw call;
- `npx --no-install tsc --noEmit` sạch;
- `npx --no-install vitest run --maxWorkers=4` qua toàn bộ;
- báo cáo ghi số dòng thêm và điều Claude cần quay. Cảnh `TP` của `lab-pilot-ab.mjs` dùng lại được; thêm mốc khung của pha này nếu cần.
