# 2026-10-25 — Audio Lab: lô 1c (Q6) trên Mac mini M4

Yêu cầu: sinh lại âm hành động theo luật Q6 của chủ dự án (tụ lực, phát có lực, thân, đuôi vang trong không gian bản đồ; không "bụp, thụp"), theo danh sách và thứ tự ở `tools/audio-lab/Q6_REWRITE_2026-10-24.md` §7. Tu Tiên tạm dừng, không đụng tới.

Chi tiết, số đo và việc còn lại: `Q6_REWRITE_2026-10-24.md` §11 và `DECISIONS.md` "Q6: lô 1c đã sinh". Âm chỉ nằm ở `~/AudioLab` (không vào Git). Mọi số thời gian là số Apple M4.

## Mục đã làm

| Mục | Việc |
|---|---|
| `Q6_REWRITE` §7 (lô 1c) | `common/batch1c.py`: bảng job chỉ có khóa Q6 của 19 id, đúng thứ tự §7 và cột `pick_seconds`, seed 3001–3006 (`call-chop` 3101–3106). Sinh 426 bản trong 333 s, giữ 394 bản sau xử lý |
| `Q6_REWRITE` §7, gạch "Bảng `JOBS` … vẫn trỏ khóa cũ" | Lô 1c có bảng riêng; test không cho bộ (id, khóa, seed) nào trùng lô 0b, lô 1 |
| `Q6_REWRITE` §7, cột công thức | 10 công thức dựng lại cho độ dài Q6: `fire.impact.a/b/c`, bom Hạt Thông, `wordshot-fire.mix`, `blast.mix`, `kill.elite`, `hurt.breach`, `hurt.breach.b2`, `hit.t4`. Ghi ở `build/recipes/<game>/<rid>.b1c.json`; file `.b1` giữ nguyên vì phiên lô 1 còn mở |
| Hậu kỳ và chấm | Xử lý theo thẻ (đầu tiếng thật, đuôi hàm mũ, đỉnh −1 dBTP); bộ chấm theo game, có `critic.loop_eval` của thẻ; L1 trên 426 bản thô: 0 clip; `licence-check` cây thử ĐẠT ở 3 game |

## Lỗi tìm ra và cách sửa

- **`gen/process.py` loại đúng hình dạng Q6.** Luật "gõ hai lần" và "phát sau cắt cửa sổ" của tiếng trúng đã loại:
  - tiếng khè trước lửa của `fire.cast` (16/24);
  - nhiều quả cầu lửa của `impact.multi` (19/24);
  - ngòi trước tiếng nổ của bom (8/24);
  - phần đầu của `hurt.breach` (8/18).

  Thêm tùy chọn `--build-up` (có test) cho đúng 4 id này. Sau đó giữ 23/24, 22/24, 24/24, 18/18 bản.
- **`kill.elite`:** 21/24 bản kêu ngay từ mẫu đầu, nên đầu tiếng chưa xác minh. Thân của công thức lấy theo đỉnh tiếng nổ.

## Kiểm

- `AUDIOLAB_HOME=$HOME/AudioLab ~/AudioLab/.venv/bin/python -m pytest -q specs/tests gen/tests` trong `tools/audio-lab`: 229 qua.
- `pytest -q common/tests`: 20 qua.

## Còn lại

- Bản dựng trong bối cảnh và phiên nghe `SESSION_1C_*` (bước kế của làn).
- Đề xuất lớp đầu tiếng `other` cho `impact.multi`, `wordshot-fire`, `arrow-fire`. Luật lên 10 ms đang chặn mọi bản nguyên khối của hai id đầu và 21/24 bản của `arrow-fire`.
- Luật L2 Q6: `punch_db` đọc sai âm có phần tụ lực.
- Chủ dự án chưa nghe bản nào.
