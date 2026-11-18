# 2026-10-25 — Audio Lab: phiên nghe lô 1c (Q6) trên Mac mini M4

Yêu cầu: dựng bản trong bối cảnh và phiên nghe cho lô 1c, như lô 1 đã làm: cấu hình Bảng Nghe và `SESSION_1C_<GAME>.md` tiếng Việt. Tu Tiên tạm dừng, không đụng tới.

Chi tiết và số đo: `tools/audio-lab/Q6_REWRITE_2026-10-24.md` §12 và `DECISIONS.md` "Q6: phiên nghe lô 1c". Âm và bản dựng chỉ nằm ở `~/AudioLab` (không vào Git). Mọi số thời gian là số Apple M4.

## Mục đã làm

| Mục | Việc |
|---|---|
| `Q6_REWRITE` §11.6 #1, `DECISIONS` "Việc còn lại" mục 5 ý 1 | `common/batch1c.py` có bước `context` và `session`. Danh sách nghe tối đa 4 bản mỗi id; 72 bản dựng trong 8 kịch bản (`dh-cast-chain`, `dh-pack`, `dh-trap`, `td-wordhit-chain`, `td-night`, `ts-xung-3s`, `ts-xung-3s-kills`, `ts-breach`); 3 phiên `1c-dh` (26 bản), `1c-td` (20), `1c-ts` (26), lô `1c` |
| `Q6_REWRITE` §7, `dh-cast-chain` dựng lại với 750 ms | Bản dựng dùng `fire.cast` 600–900 ms của lô 1c. `context/scenes.py` thêm chỗ `impact.multi` (từ thứ 2 và 5, mức theo `map-events.ts:175`); thiếu chỗ đó thì giống hệt lô 1 |
| `Q6_REWRITE` §7, `gun.xung` I, J, K cạnh lô 1 | Một item "Liên thanh 3 s": hướng 2 lô 1, bộ I, bộ K (bộ B nhỏ hơn 5 dB, `B_db` mới ở `context/ts_scenes.py`), cách game đang phát. J: 0/6 bản nghe được |
| `Q6_REWRITE` §11.6, `wordshot-fire` ở nhịp 1,5 s | "Lặp" của họ lửa và Phát Chữ: mỗi 1,5 s, 8 lần |
| `Q6_REWRITE` 11.3 #2, đưa bản bị luật chặn vào phiên kèm nhãn | 15 bản có nhãn "bị luật chặn"; thêm xếp hạng raw cho bom và `arrow-fire` |
| `DECISIONS` "Việc còn lại" mục 3 | Tai nghe, Lặp, cặp mốc (3–4 mỗi phiên, tối đa 10 mục), bản anh đã chấm nằm lẫn không nhãn, nhắc "rè/lỗi", súng tổng hợp và Stable Audio 3 cùng phiên |
| `DECISIONS` "Việc còn lại" mục 4 | Đã chọn theo đề xuất (luật §2 của process): các đề xuất vòng 25/10 giữ như trong thẻ |
| `DECISIONS` "Việc còn lại" mục 6 (mới) | Bảng id còn chờ điểm của lô 1 (S1–S6 chưa chấm), id nào lô 1c đã thay |
| `REPORT.md` của lô | Thêm số đo trong bối cảnh (giọng đọc, 1–4 kHz sau 100 ms, loa nhỏ, liên thanh) |

## Lỗi tìm ra và cách sửa

- **Thẻ thứ năm tràn màn hình.** Lượt đầu cho tới 6 bản mỗi id. Ở 1280×720, thẻ thứ năm đẩy hàng nhãn xuống dưới mép (đo 147 px ở `gun.xung`). Đã giới hạn 4 bản, xếp theo ưu tiên (máy xếp đầu, loại kia, bản bị luật chặn, bản đã chấm, bản dò, prompt khác). Chụp lại: 7 màn hình, không tràn.
- **Lỗi tiềm ẩn ở lần chấm raw:** bản đã chấm nằm trong thư mục `masters` (bom 0a v3) sẽ được chấm mà không kèm `SOURCES.json`, vì mã lấy nhầm thư mục cha. Các lần chấm raw trước chưa gặp (bản tru nằm ở `processed`). Đã sửa trước lần chấm raw của bom, theo cách bước `critic` cuối vẫn làm.

## Phát hiện (máy, trước khi chủ dự án nghe)

- `gun.xung` nguyên khối hổng ở 10 viên mỗi giây: I 20,4 %, K 17,1 % (hướng 2 lô 1: 0,2 %; ngưỡng 10 %).
- Giọng đọc trượt bài C ở mọi bản dựng, như lô 1.
- Mọi `fire.cast` theo Q6 trượt luật "âm xong từ" vì tiếng gầm tới sau phần khè.

## Kiểm

- `AUDIOLAB_HOME=$HOME/AudioLab ~/AudioLab/.venv/bin/python -m pytest -q specs/tests gen/tests common/tests` trong `tools/audio-lab`: 255 qua (trước: 249).
- `… pytest -q board/tests context/tests`: 42 qua, 1 bỏ qua (thử Chrome của bảng).
- Chrome 1280×720 (khóa `--gpu`): 7 màn hình của 3 phiên, không tràn sau khi giới hạn 4 bản; ảnh ở `~/AudioLab/work/_batch1c/b1c/board-check/`.
- `run.sh board check`: 3 phiên mới ĐẠT. Bảng Nghe phục vụ 3 phiên trên bản sao thư mục review: âm và bản dựng 200, thẻ 403 trước khi chấm, trang không lộ tên file.

## Còn lại

- Chủ dự án nghe `1c-dh`, `1c-td`, `1c-ts`, rồi các phiên lô 1 có id chỉ còn ở lô 1.
- Sau phiên: `critic agreement --batch 1c`, lớp đầu tiếng cho id bị luật chặn (§4.3.1), chốt bản, bù `gainDb`.
- Người điều phối: thêm dòng vào `docs/changelog/README.md` và dòng làn âm trong `docs/CLAUDE_PROCESS_2026-10-24.md`.

## Sửa sau phản biện

Phản biện độc lập (26/10): **chưa đạt**, 2 lỗi lớn (thân `fire.impact.b`, `.a` không cân mức; đuôi hàm mũ cắt vào tiếng chính của id tụ lực), 11 lỗi nhỏ (phiên quá 20 phút, `gun.xung` 0a v2 có nhãn nên không mù, `fire.cast` thiếu hướng G và H, điểm của hai lần chấm trong một item, đường xuất trùng của `hurt.breach`, còi trước tiếng nổ ở `hurt.breach-v4`, `step_recipes` ghi file trước khi dựng, chữ "đề xuất" của Q3, "16 phiên cũ", thứ tự bằng chứng, `tmp/` không gitignore). Cả 13 mục và cách sửa: [`2026-10-26-audio-lab-batch-1c-review-fix.md`](2026-10-26-audio-lab-batch-1c-review-fix.md); số đo ở `tools/audio-lab/Q6_REWRITE_2026-10-24.md` §13. Ba phiên `1c-dh`, `1c-td`, `1c-ts` ở trên đã được thay bằng năm phiên `1c-dh-1`, `1c-dh-2`, `1c-td`, `1c-ts-1`, `1c-ts-2`; phiên cũ cất vào `sessions/_superseded/`.
