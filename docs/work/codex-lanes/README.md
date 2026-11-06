# Các làn Codex (từ 06/11/2026 22:00)

Anh: "tăng agent của codex lên 3, đảm bảo list việc của 3 agent này k ảnh hưởng lẫn nhau… giao việc theo list vào 1 file md, kêu nó làm và kiểm tra kỹ từng việc, pass mới sang việc khác, để bạn cũng k cần phải coi nó liên tục".

Mỗi làn là một file md chứa danh sách việc làm lần lượt. Codex tự kiểm từng việc theo mục "Đạt khi", ghi báo cáo, rồi mới sang việc kế tiếp. Các làn ghi vào chỗ riêng, không đụng nhau. Claude chỉ đọc báo cáo khi một làn chạy xong.

| Làn | Việc | Nơi ghi | File | Trạng thái |
|---|---|---|---|---|
| 1 | Mã sim Song Long phím 2 (phiếu 293; sau đó 294 sát thương, 296 trình bày khi Claude viết xong) | `games/.wt-ic-swarm-sim` (nhánh `codex/key2-swarm-sim`) | `docs/codex-queue/293-tt-key2-swarm-sim-routes.md` | đang chạy từ 21:51 |
| 2 | Video Firefly mới hôm nay → flipbook cho lab (8 việc) | thư mục mới trong `art-src/lab/vfx/` (`foe-i2v`, `foe`, `beast`, `boss`, `world`, `meta`, `cutin-mat`, `expansion-phases`) | `lane-2-flipbooks.md` | đang chạy từ 22:00 |
| 3 | Ảnh: ấn đủ bộ cho Hỏa rồi 12 hệ còn lại | `…/stills/skills/<hệ>-sigil-*`, `<hệ>-crack-*`, `<hệ>-rift-*` | `lane-3-sigils.md` | đang chạy từ 22:08 (anh duyệt ấn Hỏa 22:05) |

Luật chung: không lệnh git ghi (Claude commit); không mở cổng mạng; dòng `CODEX-WAIT-UNTIL` chỉ ghi khi thật sự hết hạn mức.
