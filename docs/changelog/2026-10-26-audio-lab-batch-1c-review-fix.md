# 2026-10-26 — Audio Lab: lô 1c sửa sau phản biện (Mac mini M4)

Yêu cầu: sửa mọi lỗi mà hai người kiểm độc lập tìm ra ở làn âm lô 1c (base `e322a375` tới `b6830f5b`), chạy lại các bước bị ảnh hưởng, dựng lại phiên nghe trước khi chủ dự án mở. Kết luận phản biện: **chưa đạt**, 2 lỗi lớn, 11 lỗi nhỏ. Chưa có file trạng thái 1c nào, nên ghi đè phiên an toàn. Tu Tiên tạm dừng, không đụng tới.

Chi tiết và số đo: `tools/audio-lab/Q6_REWRITE_2026-10-24.md` §13; `DECISIONS.md` "Q6: sửa sau phản biện lô 1c". Âm, bản dựng và bằng chứng chỉ nằm ở `~/AudioLab` (bằng chứng: `~/AudioLab/work/_batch1c/b1c/review-fix/`). Mọi số đo là số **Apple M4**.

## Sửa sau phản biện

| # | Lỗi (phản biện) | Đã làm |
|---|---|---|
| 1 (lớn) | `fire.impact.b-v3`, bản máy xếp đầu của `1c-dh`, gần như không có thân và đuôi: thân lấy theo đỉnh 5 ms, không cân mức, lệch tới 22 dB; `fire.impact.a` cùng kiểu | Thân của mọi công thức lô 1c được cân mức (`gainDb` của nguồn, mới ở `build/sources.py` và schema) theo LUFS-M max của cửa sổ qua bộ lọc của lớp, **sau 40 ms đầu** (phần tiếng đánh do lớp đầu tiếng lo), về trung vị của bể; bản nhỏ hơn bản to nhất quá 10 dB bị loại (`common/batch1c.py` › `level_match`, `body_level`). `fire.impact.b`: mức thô các biến thể lệch 1,1 dB (trước 11,5 dB), mẫu dưới −90 dBFS tối đa 4,3 % (trước 53,9 %), 410–500 ms trong 30 dB dưới đỉnh (trước 50 ms ở v3). `fire.impact.a`: 390–420 ms ở mọi biến thể (trước 50–70 ms ở v2, v6). Cả hai nay đạt −20,0 LUFS-M, không cần bù `gainDb` (trước −24,2 và −24,9) |
| 2 (lớn) | Đuôi hàm mũ bắt đầu ở 35 % cửa sổ, nên ở id có phần tụ lực nó hạ cả tiếng chính; số đo đuôi Q6 ở §11.3 #4 là đuôi tổng hợp | `gen/process.py`: đường tắt dần bắt đầu sau **thân** của cửa sổ (khung cuối còn trong 6 dB dưới khung to nhất; khung dài 10 % cửa sổ, 10–50 ms) và sau tiếng chính 100 ms ở id tụ lực. Cửa sổ bị cắt mà còn dưới 20 % độ dài cho đuôi, khi âm còn trên −30 dB, bị loại kèm lý do "không còn chỗ cho đuôi". Bản có thân bị cắt quá 3 dB: `fire.cast` 21/23 → 1/13, `hurt.breach` 13/18 → 3/12, `impact.multi` 19/22 → 6/22, `kill.elite` 18/24 → 0/24, `ink-puff` 6/17 → 0/7. Luật đuôi Q6 đọc đuôi gốc trên cửa sổ thô (`natural_tail`); bản tụ lực bị cắt khi còn trên −30 dB mang nhãn "đuôi rút vừa thẻ". §11.3 #4 và DECISIONS đã sửa |
| 3 | `gun.xung` 0a v2 có nhãn "Cách game đang phát", nên không mù, cả ở vai bản đo độ nhất quán lẫn ở cặp mốc | `board/server.py` › `pick_anchors`: cặp mốc nào có file mà một phiên cùng lô đang đưa ra thì bị bỏ; bảng đọc mọi file phiên của game trên đĩa; phiên mở sau không lấy lại cặp mà phiên cùng lô đã giữ (lượt thử đầu, `1c-dh-1` và `1c-dh-2` cùng lấy một cặp 0a). §12.1 và DECISIONS ghi rõ bản này không dùng được làm mốc mù |
| 4 | `fire.cast` không đưa hướng G và H vào phiên | Danh sách nghe đưa bản tốt nhất của **mọi** prompt chưa có mặt trước bản khác nhất; `fire.cast` không còn bản dò. Phiên mới có E, G, H; F không còn bản nào (5 bản gầm dài quá thẻ 900 ms, 1 bản không có đầu tiếng thật) |
| 5 | `1c-dh`, `1c-ts` ước 20–25 phút, vượt giới hạn 20 phút | Rồng Giữ Ải và Tuyến Cuối tách làm hai phiên mỗi game, 2 cặp mốc mỗi phiên; mỗi phiên tối đa 10 mục và 20 phút (ước 40 s một thẻ, có test). Phiên cũ `1c-dh`, `1c-ts` được cất vào `sessions/_superseded/` |
| 6 | `critic agreement --batch 1c` sẽ so điểm z của hai lần chấm khác nhau trong một item | Lần chấm raw của một id nay chấm mọi file mà item của id có thể chứa; item nào có bản từ lần chấm raw thì lấy mọi điểm từ lần đó (tìm theo đường dẫn). `critic/agreement.py` bỏ cặp khác thư mục chấm (`cross_run_pairs`), item lẫn hai lần chấm không có `top_pick` |
| 7 | `hurt.breach` và `hurt.breach.b2` cùng đường xuất runtime | `hurt.breach.b2` xuất ra `sfx/alerts/hurt-breach-b2`; `build/release.py` từ chối khi công thức thứ hai trùng đường xuất (có test) |
| 8 | `hurt.breach-v4`, `.b2-v4` đặt còi và cú đập trước tiếng nổ tới muộn | Thân `hurt.breach` lấy theo đỉnh tiếng nổ (`PEAK_POOLS`, 900 ms từ 4 ms trước đỉnh), như `kill.elite`: khung to nhất của v4 nay ở 10 ms và 20 ms (trước 390 và 400 ms) |
| 9 | `step_recipes` ghi đè `.b1c.json` trước khi kiểm bản dựng | File công thức chỉ được ghi khi dựng; bản dựng đã có mà nguồn khác thì báo, không ghi. Dựng lại thì lần trước chuyển sang `.prev` (thư mục mới sạch, không còn master cũ thừa) |
| 10 | `SESSION_1C_DH` gọi Q3 là "đề xuất" | Sửa: Q3 đã quyết nới tới 150 ms; cổng L1 chưa đổi vì §4.3.1 chưa sửa |
| 11 | §12.4 ghi "16 phiên cũ" | Sửa thành 15 |
| 12 | Ảnh Bảng Nghe và log pytest có trước lần ghi phiên cuối | Lần này test và ảnh chụp chạy sau lần ghi phiên cuối (thứ tự ở §13.5) |
| 13 | `tmp/mac-2026-10-25/` của repo cha không bị gitignore | Việc của người điều phối (không phải mã của làn); làn này chỉ add đường dẫn cụ thể |

## Lỗi tìm ra thêm khi sửa

- **Chữ ký bản dựng chỉ theo đường dẫn.** Bản xử lý lại giữ tên cũ, nên `context` sẽ dùng lại bản dựng cũ. Chữ ký nay gồm mã băm nội dung.
- **Bộ chấm không xóa JSON của file đã mất.** Bản bị loại ở lượt xử lý lại vẫn giữ điểm cũ trong `critic-final`. Mỗi lần chấm lại nay vào thư mục trống (lần trước sang `.prev`); lần chấm raw của id không còn cần cũng được cất.
- **Đo trên hai tần số mẫu.** Thước đo đầu của lượt này so khung 50 ms của bản thô 44,1 kHz với bản xử lý 48 kHz theo số mẫu, nên lệch dần. Mọi số ở trên đo lại theo thời gian.

## Kiểm

Chạy trên mã cuối, sau lần ghi phiên cuối:

- `AUDIOLAB_HOME=$HOME/AudioLab ~/AudioLab/.venv/bin/python -m pytest -q specs/tests gen/tests` trong `tools/audio-lab`: 234 qua (HEAD trước lượt này: 229).
- `… pytest -q common/tests build/tests critic/tests board/tests context/tests`: 287 qua, 3 bỏ qua (Chrome của bảng, test cần mô hình).
- `run.sh board check`: 20 file phiên ĐẠT (5 phiên 1c mới, 15 phiên cũ). `session` không `--force` khi file đã có: mã 1, mã băm không đổi.
- Bảng Nghe trên bản sao thư mục review: cặp mốc 2, 2, 4, 2, 0 (Tuyến Cuối hết cặp mù cho phiên thứ hai); thẻ và số đo 403 trước khi chấm; trang không lộ tên file, vai trò, đường dẫn.
- Chrome 1280×720 (khóa `--gpu`): 29 màn hình, mọi mục của 5 phiên; tràn 0 px; nhãn dài nhất xuống hai dòng, đọc được. Ảnh ở `~/AudioLab/work/_batch1c/b1c/review-fix/board-check/`.
- `licence-check` trên cây thử dựng lại: mã 0 ở 3 game. L1 bản thô: 426 bản, 0 clip.
- Phiên mới: `1c-dh-1` (4 id, 16 bản, khoảng 13 phút), `1c-dh-2` (3 id, 11 bản, 10 phút), `1c-td` (5 id, 20 bản, 19 phút), `1c-ts-1` (4 id, 16 bản, 13 phút), `1c-ts-2` (3 id, 10 bản, 9 phút).

## Còn lại

- Chủ dự án nghe 5 phiên 1c (`pnpm audio:board --game <game> --batch 1c --open`).
- Làn Specs: thẻ `fire.cast` 900 ms, `hurt.breach` 960 ms, `ink-puff` 240 ms có thể quá ngắn cho Q6 (26 bản bị loại vì không còn chỗ cho đuôi).
- Cắt đuôi còn sót ở `impact.multi` 6/22 và `hurt.breach` 3/12 (đã dùng 4/6 vòng đo); đòn kế: ngưỡng thân riêng cho id tụ lực.
- Bù `gainDb`: bom −24,4 LUFS-M, `wordshot-fire.mix` −22,5.
- Người điều phối: thêm dòng 26/10 vào `docs/changelog/README.md`, dòng làn âm trong `docs/CLAUDE_PROCESS_2026-10-24.md`, và `/tmp/` vào `.gitignore` của repo cha nếu muốn.
