# Các làn Codex (từ 06/11/2026 22:00)

Anh: "tăng agent của codex lên 3, đảm bảo list việc của 3 agent này k ảnh hưởng lẫn nhau… giao việc theo list vào 1 file md, kêu nó làm và kiểm tra kỹ từng việc, pass mới sang việc khác, để bạn cũng k cần phải coi nó liên tục".

Mỗi làn là một file md chứa danh sách việc làm lần lượt. Codex tự kiểm từng việc theo mục "Đạt khi", ghi báo cáo, rồi mới sang việc kế tiếp. Các làn ghi vào chỗ riêng, không đụng nhau. Claude chỉ đọc báo cáo khi một làn chạy xong.

| Làn | Việc | Nơi ghi | File | Trạng thái |
|---|---|---|---|---|
| 1 | Song Long phím 2: phần A xong (293, `35f3202`); tiếp 294 sát thương, 295 đo cân bằng | `games/.wt-ic-swarm-sim` (nhánh `codex/key2-swarm-sim`) | `lane-1-swarm.md`, `lane-1b-swarm-view.md`, `lane-1c-lab-all-merge.md` | xong 23:24: sim, sát thương, hình, gộp vào lab chung `codex/lab-all` (cổng 3146); cân bằng trượt, chờ anh |
| 2 | Video Firefly mới hôm nay → flipbook cho lab (8 việc) | thư mục mới trong `art-src/lab/vfx/` (`foe-i2v`, `foe`, `beast`, `boss`, `world`, `meta`, `cutin-mat`, `expansion-phases`) | `lane-2-flipbooks.md` | xong 22:21: 79 flipbook; lượt 2 khi Firefly làm xong số video còn lại |
| 3 | Ảnh: ấn đủ bộ cho Hỏa rồi 12 hệ còn lại | `…/stills/skills/<hệ>-sigil-*`, `<hệ>-crack-*`, `<hệ>-rift-*` | `lane-3-sigils.md` | xong 23:31: 89 ảnh, 13 tấm ghép gửi anh; gắn vào lab chờ anh duyệt |

Luật chung: không lệnh git ghi (Claude commit); không mở cổng mạng; dòng `CODEX-WAIT-UNTIL` chỉ ghi khi thật sự hết hạn mức.
