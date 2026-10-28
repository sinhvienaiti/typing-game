# Bàn giao điều phối (cập nhật 28/10/2026, khoảng 15:00)

File này để **một session mới** nối tiếp mà không cần đọc lại lịch sử chat.
- Mỗi lần dừng hay chuyển session, cập nhật file này.
- Luật của chủ dự án nằm ở memory (tự nạp) và `AGENTS.md`. Ở đây chỉ nhắc ý chính.

## 1. Bắt đầu session mới

1. Đọc file này, rồi `docs/CODEX_QUEUE.md` (dòng 035 trở đi).
2. Kiểm kết quả các lượt chạy ở mục 3:
   - workflow ghi file trong `/private/tmp/claude-501/-Users-toandx-htdocs-typing-game/157c54d6-5a15-4acc-b09d-0aae10862f93/tasks/<id>.output`;
   - journal của workflow ở `~/.claude/projects/-Users-toandx-htdocs-typing-game/157c54d6-5a15-4acc-b09d-0aae10862f93/subagents/workflows/<run>/journal.jsonl`;
   - Codex ghi nhật ký vào `.local/codex-runs/<tên phiếu>/` và báo cáo vào `docs/codex-queue/<số>-report.md`.
3. Nếu một lượt chạy bị ngắt khi đóng session cũ: chạy lại bằng `resumeFromRunId`, hoặc `tools/codex-run/queue.sh` với file lane (phiếu đã có báo cáo thì bỏ khỏi lane).

## 2. Luật chính (chi tiết ở memory)

- **Giao tiếp và quyết định:**
  - Trả lời chủ dự án bằng tiếng Việt.
  - Tự làm theo khuyến nghị; chỉ hỏi quyết định thật sự chặn việc.
  - Cổng nào gãy thì báo kèm số.
- **Git và media:**
  - Không media trong Git.
  - Repo game đẩy qua SSH, không force.
  - Chỉ Claude chạy `pnpm media:push`.
  - Không đụng Tu Tiên.
- **Codex:**
  - Không chạy lệnh git có ghi; Claude duyệt rồi mới commit.
  - Giao **một danh sách** việc, **ảnh trước**. Chủ dự án muốn Codex không rảnh.
- **Làn và ảnh test:**
  - Tối đa 4 workflow cùng lúc.
  - Ảnh test: giữ tờ ghép, xóa ảnh thô bằng `node tools/capture-prune/prune.mjs <thư mục> --apply`.
  - Muốn xóa thứ khác ngoài ảnh test của mình thì hỏi chủ dự án.
- **Mức nhận:**
  - Ảnh 2D nhận từ 8 điểm.
  - Model 3D nhận từ 7 điểm; 7–8,5 ghi vào `ART_REPLACE_LATER`.
  - Tên danh từ trong game bằng tiếng Anh (`docs/games/NAMES_EN.md`).

## 3. Đang chạy lúc bàn giao

| Lượt | Làm gì | Khi xong thì |
|---|---|---|
| Workflow `ts-cloud-fix` (wf_aa65bb85-96b) | Tuyến Cuối: khói sau big kill che quái 1–3 s (lỗi người chấm vòng 2 tìm ra trên `main` ea8e0f9 đã đẩy). Một agent sửa, một người chấm | Duyệt; rồi gộp nhánh `ts-names` (d96b376, đổi tên tiếng Anh đã kiểm) vào `main` Tuyến Cuối, `pnpm check`, đẩy, bump con trỏ |
| Workflow `map-pilot-a` (wf_d13ecef8-0d5) | Bản thử bản đồ Rồng L2-cau, chặng A, trong `games/.wt-dh-mappilot` (nhánh `map-pilot`). Gồm bộ giám khảo (`tools/map-factory/docs/judge.md`), người dựng, giám khảo mới | Xem điểm (cổng A: trung vị ≥ 7,5, không ảnh < 6,5, khung hình +≤ 2 ms); gửi chủ dự án tờ ảnh; sang chặng B (`docs/tools/map-factory/MAP_PLAN.md` §3) |
| **Làn VFX Rồng: đã chạy lại 16:30 trong session cũ** (`w1jp69fiq`, cùng run wf_0ab38d58-be4). Nếu nó dừng giữa chừng, session mới khởi động lại theo ghi chú ở ô này | Lượt cũ dừng lúc 13:45 khi lượt điều phối bị ngắt. Nhánh `dh-vfx` ở `games/.wt-dh-vfx` (f3fe49c): bước 1a (đòn chữ Hỏa Long) đã dựng, chưa chấm. Còn: chấm 1a; Sky Fire đủ 5 pha (VFX_STANDARD §5.3 phần 2); **VFX quái** (vệt chém, mũi tên Moss Archer, lóe và mảnh khi trúng, hiệu ứng xuất hiện; chủ dự án hỏi 28/10). Lời nhắc từng bước nằm trong `~/.claude/projects/-Users-toandx-htdocs-typing-game/157c54d6-5a15-4acc-b09d-0aae10862f93/workflows/scripts/vfx-dh-v2-wf_0ab38d58-be4.js`: chép sang workflow mới (resume chỉ chạy trong session cũ) | Gửi chủ dự án tờ trước/sau từng bước; chưa gộp vào `main` Rồng. Ước 6–9 giờ cho cả ba bước |
| Codex lane Z2 (`b52i9ktmr`) | Thư viện AL-13, AL-14, AL-15 (phiếu 085–087): ảnh nhỏ, trang `library/out/catalog.html`, cây Finder `library/browse/` song ngữ. AL-12 (Claude duyệt tên, 1.831 dòng) đã commit 98a1f0e2 | Duyệt; chạy `pnpm lib:scan` để mục lục nhận tên đã duyệt (lệnh tìm hiện còn đọc bản quét 13:17); mở `library/browse/creature (quái)/` gửi chủ dự án. Còn quyết: nâng trần 60 KB của `taxonomy.json`; luật chọn khi một nhóm con có ở hai loại (bridge, gate, wall, jetty, weapon, portrait, decal) |
| Ghi chú 16:20 | `ts-cloud-fix` và `map-pilot-a` cũng dừng lúc 13:45 vì cùng lý do; đã chạy lại (resume) trong session cũ lúc 16:20. Codex hết hạn mức ChatGPT lúc 15:32, tự chạy lại lúc 18:37 (các tiến trình hàng đợi nằm trong session cũ, đừng lưu trữ session đó) | |
| Codex chuỗi X → Y (`b8l2173ul`) | X: phiếu 065–080 (6 ảnh bản đồ đã xong 14:50; đang làm mã MF-C01…). Y: 063, 064 (AL-17, AL-18), 081–083 (MF-C06–C08), 084 (sửa đường bộ nhớ đệm của thư viện) | Duyệt từng phiếu; ảnh 065–070 chấm lại theo mức 8 |

## 4. Việc chờ, theo thứ tự

1. **Duyệt kết quả mục 3** khi từng lượt xong.
2. **Codex 035, 036, 037 (làn VFX S) chưa duyệt.** Báo cáo:
   - 035: `docs/codex-queue/035-report.md`;
   - 036: `docs/codex-queue/036-report.md`;
   - 037: `typing-game-wt/vfx/docs/codex-queue/037-report.md`.

   Mã:
   - 035: Tuyến Cuối khung đầu, `games/.wt-ts-vfx`;
   - 036: ống FX Lời Gọi, `games/.wt-td-vfx`;
   - 037: công cụ `tools/vfx-sheet`, `typing-game-wt/vfx`.

   035 và 036 cần kiểm trên trình duyệt. Sau khi 036 gộp: làn Lời Gọi b-ui rồi verify.
3. **Phiếu thư viện còn lại:**
   - AL-19 đến AL-22 (chép, kiểm) theo `docs/tools/asset-library/TICKETS.md`;
   - AL-21 cần phối hợp `kit:sync`, vì thêm file vào kit làm `kit:check` của game đỏ.
4. **Bản đồ:**
   - phiếu MF-C09 đến C19 cần Claude viết thuật toán chính xác vào phiếu (CL-02);
   - MF-C25 đến C28 cần đồ thị mẫu (CL-07).
5. **Media:** sau khi nhận ảnh Codex mới, chạy `pnpm media:push --yes`; commit `media.md5` của game; bump con trỏ.
6. **Repo cha:** nhánh `feat/space-typing-admin-uiux` hơn origin 58 commit, chưa đẩy. Lời Gọi: nhánh `a2-days` chưa đẩy.

## 5. Quyết định chờ chủ dự án

- **OW-01:** dựng 8 model đợt 3 (`typing-game-handoff-2026-10-25/tripo-upload-dot3`, khoảng 240 credit) cho chặng C của bản thử bản đồ.
- **Rồng "nhàn":** hướng cho D27/D31. Mọi bước đo ngày 27–28/10 đều gãy G1 hay trần 90 %; số ở `games/dragon-hold/docs/changelog/2026-10-27-owner-decisions.md` §8.7.
- **Tuyến Cuối, biển viết hoa:** tên tiếng Anh tạm giữ kiểu hoa đầu từ ("Pack Leader 2/3"). Anh có thể đổi sang viết hoa hết.
- **Maple Tree:** chỉ dựng nếu cây nhuộm ấm < 8 điểm ở chặng A.

## 6. Nhánh và worktree

- **Rồng** (`main` 02fe9c7, đã đẩy):
  - `.wt-dh-mappilot` (bản thử bản đồ, Claude);
  - `.wt-dh-mapcodex` (Codex);
  - `.wt-dh-vfx` (VFX);
  - `.wt-dh-mapspike` (spike vòng 1, giữ để so);
  - `.wt-dh-d27c` (D27, không giữ);
  - `.wt-dh-demo`, `.wt-play-dragon-hold`.
- **Lời Gọi** (`a2-days` a5cc147): `.wt-td-vfx` (036), `.wt-play-typing-defense`.
- **Tuyến Cuối** (`main` ea8e0f9):
  - `.wt-ts-names` (chờ gộp);
  - `.wt-ts-vfx` (035);
  - worktree tạm `tmp/mac-2026-10-28/cloud-fix/wt-base` của làn sửa khói.
- **Repo cha:**
  - `typing-game-wt/map-codex` (nhánh `map-factory`, Codex bản đồ);
  - `typing-game-wt/vfx` (037).

## 7. Tài liệu chính

- `docs/tools/map-factory/MAP_PLAN.md`, `TICKETS.md`: kế hoạch bản đồ v2, bản thử L2-cau.
- `docs/tools/ASSET_LIBRARY.md`, `docs/tools/asset-library/TICKETS.md`: thư viện tài sản.
- `docs/games/VFX_STANDARD.md`: VFX nhiều lớp. VFX quái của cả ba game nay là bước riêng.
- `docs/games/3D_IMPORT_2026-10-28.md`: Tripo đợt 2, đủ 86/86 model. `docs/games/3D_REQUESTS.md`.
- `docs/games/BALANCE.md`, `docs/games/NAMES_EN.md`, `docs/CODEX_QUEUE.md`.
