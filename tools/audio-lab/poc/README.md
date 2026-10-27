# Bản thử "tai AI" (tham chiếu, không sửa)

Mã của hai bản thử ngày 23/10/2026, chép nguyên từ scratchpad để không mất khi dọn scratchpad. Số liệu và cách đọc ở phụ lục A của [`docs/games/AUDIO_PIPELINE.md`](../../../docs/games/AUDIO_PIPELINE.md).

- Đây là **bản tham chiếu đóng băng**. Mã mới viết trong `critic/`, `build/`… và có thể chép từ đây. Không sửa file trong thư mục này.
- Âm thử (40 file: 8 tổng hợp, 8 Kenney CC0, 24 bản làm hỏng) nằm ngoài Git, ở `~/AudioLab/work/_fixtures/poc40/` (giấy phép trong `LICENSES.md` cạnh đó).
- `manifest.json`, `manifest_degraded.json`: đường dẫn tương đối so với thư mục âm thử.

| File | Việc |
|---|---|
| `analyze.py` | Luật đo L1/L2 và thẻ ảnh PNG (không cần ffmpeg) |
| `critics.py` | audiobox-aesthetics, CLAP (2 bản), AST |
| `listener.py` | MiDashengLM. **Không chạy trong venv chung** (cần transformers 4.57.6); kết quả kém, không dùng tiếp |
| `gen_samples.py`, `degrade.py` | Sinh 8 âm tổng hợp và 24 bản làm hỏng |
| `score_pairs.py`, `make_tables.py` | Bảng so cặp và bảng tổng (bảng tổng cần `listener.json`) |
| `run_all.orig.sh` | Script gốc, tải uv "latest" và cài thư viện không ghim. Chỉ để đối chiếu, đừng chạy |
| `try1/` | Bản thử 1 (6 âm tổng hợp): `gen.py`, `score.py`, `sem.py`, `card.py` |

Chạy lại, không cần mạng:

```bash
bash tools/audio-lab/poc/rerun.sh              # luật đo + mô hình học máy
bash tools/audio-lab/poc/rerun.sh --rules-only # chỉ luật đo và thẻ ảnh
```
