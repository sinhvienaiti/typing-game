# Vòng 3 · Bước 1 · Cột Lôi: quái nhận đòn có lực, thấy được ở góc chơi (sau `tp2=1`)

Anh (07/11 15:55): "Làm vòng 3". Nút thắt số 1 trong `docs/work/consult/r2-step4-verdict.md`: quái nhận đòn chưa đủ lực (giây 1,07–1,30); điểm sáng trắng tím nổi hơn thân quái, không đọc được dáng nhận đòn ở góc chơi. Luật: `.agents/skills/game-vfx-production/references/path-to-8.md` §7.

**Chỉ làm điểm này:**
- **Đúng khung trúng** của Cột Lôi, quái mục tiêu (và quái trong bán kính cú giáng) nhận một phản ứng thân bằng biến đổi theo instance có sẵn của bầy quái:
  - nghiêng **ra khỏi điểm giáng** 10–16° quanh chân;
  - nhún xuống rồi nảy lên trong 0,08 s;
  - về lại trong 0,25–0,35 s.
  Biên độ theo cỡ thân để quái nhỏ, quái lớn đều thấy được ở camera chơi.
- **Chớp viền** màu Lôi 0,1 s bằng hệ viền có sẵn. Giữ choáng `stagger-stars-loop` như cũ.
- Không đổi sát thương, trạng thái hay thời điểm. Không thêm model hay hoạt ảnh mới. Quái chết thì giữ cách chết hiện có.

**Ngân sách** (cả Cột Lôi khi bật `tp2`):
- +1,0 ms p95 tối đa;
- ≤ 12 draw call thêm;
- không cấp phát mỗi khung;
- bước này khoảng ≤ 250 dòng;
- không shader mới.

**Mức `high`.** Worktree `games/.wt-ic-lab-all`, nhánh `codex/lab-all`.
- **Được ghi:** `src/lab/thunder-impact-r2.ts`; `src/lab/herd.ts`, tối thiểu, chỉ phần biến đổi instance; chỗ nối trong `src/lab/skills-main.ts`; test trong `tests/lab/`; báo cáo `docs/codex-queue/laneL1-report.md`.
- **Không:** sửa media hay manifest; lệnh git ghi; mở cổng mạng; mở trình duyệt.

**Đạt khi:**
- test node: biên độ và hướng nghiêng đúng, đúng khung trúng, về lại hết, `tp2` tắt thì không đổi, không cấp phát;
- chạy riêng các file test có liên quan bằng `npx --no-install vitest run <file…>`. Claude sẽ chạy toàn bộ.
