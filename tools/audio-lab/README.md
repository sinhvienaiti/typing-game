# Audio Lab

Bộ công cụ làm âm cho các game gõ chữ. Nó tạo ứng viên, chấm bằng "tai AI" nhiều lớp, dựng bản cuối kèm hồ sơ giấy phép, rồi cho chủ dự án nghe mù trên Bảng Nghe. Kế hoạch gốc: [`docs/games/AUDIO_PIPELINE.md`](../../docs/games/AUDIO_PIPELINE.md). Mục 4 (bộ phê bình), 5 (vòng tạo), 7 (Bảng Nghe), 10 (giấy phép) và 11 (bố cục) là hợp đồng của thư mục này.

Phiên nghe đầu tiên cho chủ dự án (lô 0a): xem [`SESSION_0A.md`](SESSION_0A.md). Phiên Stable Audio 3 vòng 2 (lô 0b): [`SESSION_0B.md`](SESSION_0B.md).

## Trạng thái (23/10/2026)

**Đã chạy được trên máy, offline, không tài khoản, không token:**

- Giai đoạn 0: venv chung, uv và Python riêng, cache mô hình chấm, `run.sh`, các lệnh `pnpm audio:*`.
- Giai đoạn 1: bộ phê bình L1, L1b, L2, L3 (audiobox), L4 (CLAP, AST), L5, L6 (thẻ ảnh); 147 thẻ spec cho 3 game; Bảng Nghe v1 (Một mình, Lặp 20 lần, Loa nhỏ); sổ giấy phép và `licence-check`.
- Phần của giai đoạn 2 không cần chủ dự án quyết: thư viện CC0 (Kenney, VCSL, VSCO-2-CE), bộ phát mẫu Python, bộ ghép lớp và chuỗi xử lý cuối.
- Lô 0 chạy trọn một vòng (`pnpm audio:batch0 all`): 45 âm (16 âm gốc của bản thử kèm 24 bản làm hỏng, 14 âm Kenney, 5 bản phát mẫu, 10 công thức cho id thật với 37 biến thể), tổng 96 file qua đủ các lớp chấm; phiên lô 0a cho chủ dự án. Lần chạy hiện hành: `~/AudioLab/work/_batch0/batch0-2026-10-23-r2/` (`REPORT.md`).

**Chưa cài, và vì sao:**

| Thứ | Vì sao chưa có | Khi nào |
|---|---|---|
| ACE-Step 1.5 | Chờ chủ dự án chấp nhận giấy phép (bước 1) và duyệt khoảng 10 GB ổ (bước 2) | Giai đoạn 6 (nhạc) |
| sox, rubberband, Surge XT | Chưa cần. ffmpeg 9.0.2 và uv 0.13.5 đã cài qua Homebrew (chủ dự án duyệt 23/10/2026) | Khi cần |
| Mô hình nghe L7 (Qwen2.5-Omni) | Tùy chọn, nặng 6,2 GB, kết quả bản thử yếu | Giai đoạn 7 |

**Stable Audio 3: bước 0 đã xong (23/10/2026).**

- Chủ dự án là cá nhân, không phải công ty, chưa có doanh thu. Chủ dự án đã tự đăng ký Stability AI Community License; trang xác nhận ghi "successfully activated". Bản ghi: `~/AudioLab/licences/stability-registration.txt`. Dòng chấp nhận và bản giấy phép kèm ngày: `~/AudioLab/licences/licences.jsonl` và các file `*-2026-10-23.txt` cùng thư mục.
- Mô hình (Small-SFX, Small-Music) cài ở `~/AudioLab/models/stable-audio-3/optimized/mlx` (repo ghim `77e0398c`), trọng số trong `~/AudioLab/models/hf-cache`, công cụ chạy lô ở `~/AudioLab/models/sa3-meta/tools/sa3_batch.py`. Lớp gọi `gen/sa3.py` dùng công cụ này ([`gen/README.md`](gen/README.md)).
- Bản thử 6 id: `~/AudioLab/work/<game>/<id>/sa3-trial/`, phiên nghe `~/AudioLab/review/batch-0b/`.
- Vòng 2 sau buổi soát bản thử (`bash tools/audio-lab/run.sh batch0b all`): xử lý lại 144 bản thô bằng chuỗi đã sửa (`gen/process.py`), tạo thêm 66 bản ở chỗ buổi soát đòi prompt khác, 3 công thức ghép lớp (`build/recipes/<game>/<id>.sa3-r2.json`), chấm đủ lớp, phiên lô 0b. Báo cáo `~/AudioLab/work/_batch0b/sa3-r2/REPORT.md`.
- Khi phát hành: chép bản đăng ký và dòng chấp nhận vào `art-src/audio/licences/` và `licences.jsonl` của game. `licence-check` chặn mọi lớp Stable Audio 3 cho đến khi sổ của game có hai thứ đó (mục 10.7).

## Bố cục

| Ở đâu | Có gì | Vào Git? |
|---|---|---|
| `tools/audio-lab/` | Chỉ mã, cấu hình, công thức JSON, thẻ spec YAML và văn bản | Có |
| `~/AudioLab/.venv` | Venv chung, Python 3.12.15 | Không |
| `~/AudioLab/bin/uv` | uv 0.13.5 riêng, đã kiểm SHA-256 | Không |
| `~/AudioLab/python/` | CPython 3.12.15 do uv quản lý (venv trỏ vào đây) | Không |
| `~/AudioLab/models/hf-cache/` | `HF_HOME`: trọng số audiobox, CLAP, AST | Không |
| `~/AudioLab/libraries/` | Thư viện CC0. Mỗi gói có `LICENSE-<ngày tải>.txt`, sổ `SOURCES.jsonl`, chỉ mục `index.json` | Không |
| `~/AudioLab/work/<game>/<id>/<run>/` | Bản dựng: `masters/`, `runtime/`, `render.json`, `SOURCES.json`, `licences.rows.jsonl`. Xóa sau khi chốt | Không |
| `~/AudioLab/work/_batch0/<run>/` | Lô 0: bản phát mẫu, kết quả bộ phê bình, cây phát hành thử, `REPORT.md` | Không |
| `~/AudioLab/work/_fixtures/poc40/` | 40 âm thử của bản thử (tổng hợp, Kenney CC0, bản làm hỏng) | Không |
| `~/AudioLab/review/<game>/` | Phiên nghe (`sessions/`), điểm chấm (`ratings.jsonl`, chỉ ghi thêm), trạng thái phiên | Không |
| `~/AudioLab/review/staging/<game>/` | Bản nháp của `games/<game>/art-src/audio/` và `public/assets/<game>/audio/` trong lúc `games/**` còn chỉ đọc. Chỉ để thứ chủ dự án đã duyệt | Không |
| `~/AudioLab/cache/` | Cache uv, pycache, numba, matplotlib, pytest, Bảng Nghe. Xóa được | Không |

## Cài từ đầu

Cần macOS arm64, Node và pnpm (đã có trong repo), `curl`, khoảng 10 GB ổ trống, có mạng ở bước 1, 2, 4 và 5. Không cần Homebrew, sudo, tài khoản hay token.

```bash
# 1. uv 0.13.5 riêng, kiểm SHA-256 trước khi giải nén
mkdir -p ~/AudioLab/bin/uv-0.13.5 && cd ~/AudioLab/bin/uv-0.13.5
curl -fLO https://github.com/astral-sh/uv/releases/download/0.13.5/uv-aarch64-apple-darwin.tar.gz
echo "743f85035a1996ecb350659e01cd9faea9709829be09b1b4b03c73eaf3c9cd73  uv-aarch64-apple-darwin.tar.gz" | shasum -a 256 -c
tar xzf uv-aarch64-apple-darwin.tar.gz --strip-components 1 && cp uv uvx ~/AudioLab/bin/
cd -   # về gốc repo typing-game

# 2. CPython 3.12.15 do uv quản lý, trong ~/AudioLab/python (env.sh cấm uv tự tải Python, nên mở riêng một lần)
source tools/audio-lab/common/env.sh && UV_PYTHON_DOWNLOADS=automatic "$AUDIOLAB_UV" python install 3.12.15

# 3. Venv từ file khóa có mã băm
bash tools/audio-lab/common/setup.sh

# 4. Trọng số bộ phê bình (khoảng 2,2 GB), không token, rồi kiểm offline
AUDIOLAB_ONLINE=1 bash tools/audio-lab/run.sh models --download
bash tools/audio-lab/run.sh models

# 5. Thư viện CC0 (khoảng 1,9 GB) và chỉ mục cho bộ phát mẫu
bash tools/audio-lab/run.sh libraries
bash tools/audio-lab/run.sh gen.index_library --verify-pitch

# 6. Kiểm
pnpm audio:test
```

- Bước 1: file `.sha256` tải cùng trang phát hành chỉ chứng minh file không hỏng, không chứng minh nguồn gốc. Mã băm ở trên là mã đã kiểm ngày 23/10/2026.
- Bước 4: chỉ tải đúng các file bộ phê bình đọc, **tại revision đã ghim** trong `common/fetch_models.py` (không tải `main`). Bộ chấm cũng nạp đúng revision đó, nên `main` có đổi cũng không đổi thứ bộ chấm nghe; `build mark-ai` ghi đúng revision bộ chấm đã nạp.
- Thêm gói Python: thêm dòng có ghim phiên bản vào `requirements.txt`, chạy `bash tools/audio-lab/common/lock.sh` rồi `bash tools/audio-lab/common/setup.sh`. Venv dùng chung, nên báo người điều phối.

## Lệnh

Mọi lệnh chạy từ gốc repo. `run.sh` nạp `common/env.sh` (không token, Hugging Face offline), rồi chạy Python của venv với `-I` qua `common/launch.py`. Bảng alias nằm ở `ENTRYPOINTS` trong `common/launch.py`.

| Lệnh | Việc |
|---|---|
| `pnpm audio:test` | pytest cho mọi module (`AUDIOLAB_TEST_MODELS=1` thêm L3–L5 thật; `AUDIOLAB_BROWSER=1` thêm thử Bảng Nghe bằng Chrome) |
| `pnpm audio:specs generate [--check] \| validate \| report \| list \| export` | Thẻ spec YAML cho mỗi id, sinh từ `catalog.ts` và các danh sách âm ([`specs/README.md`](specs/README.md)) |
| `pnpm audio:critic run <file\|thư mục>… --spec … [--stage raw\|final] [--sources SOURCES.json]` | Tai AI nhiều lớp: JSON, thẻ ảnh PNG, `summary.md`, danh sách nghe ([`critic/README.md`](critic/README.md)) |
| `pnpm audio:build render RECIPE.json --spec CARD.yaml` | Dựng âm theo công thức, chuỗi cuối, hồ sơ nguồn ([`build/README.md`](build/README.md)) |
| `pnpm audio:build mark-ai --run RUN_DIR --from-critic CRITIC_OUT` | Ghi các bước AI mà bộ phê bình đã chạy lên từng file, thêm dòng mô hình vào sổ (mục 10.7) |
| `pnpm audio:build release --run RUN_DIR [--variants 1,3]` | Đưa biến thể đã chọn vào cây staging |
| `pnpm audio:licence-check [--game G] [--staging] [--art-src DIR --public DIR]` | Kiểm giấy phép và nguồn gốc (mục 10.7). Game chưa có `SOURCES.json` vẫn bị quét: mọi file âm phát hành phải nằm trong danh sách file cũ được miễn (`build/legacy-audio.json`, mục 16 #9). Không game nào được kiểm thì kết quả là BỎ QUA, không phải ĐẠT |
| `pnpm audio:sampler render -i <nhạc cụ> --notes "0:C5:0.5:100" -o x.wav` | Bộ phát mẫu Python ([`sampler/README.md`](sampler/README.md)) |
| `pnpm audio:board [--game G] [--batch B]` | Bảng Nghe ở `127.0.0.1:3191` (bận thì 3192) ([`board/README.md`](board/README.md)) |
| `pnpm audio:board make-session <critic out>… --game G --batch B --session S` | Phiên nghe từ danh sách nghe của bộ phê bình (`from-critic` là tên cũ) |
| `bash tools/audio-lab/run.sh sa3 plan\|run --spec CARD.yaml [--variant E] [--seeds 2001-2006] [--seconds 1\|2\|3\|10] --run R` | Stable Audio 3 từ thẻ spec: bản float, hồ sơ từng ứng viên, dòng sổ ([`gen/README.md`](gen/README.md)) |
| `bash tools/audio-lab/run.sh process <raw>… --spec CARD.yaml --out DIR [--notch-comb] [--whole]` | Đầu ra mô hình thành ứng viên nghe: đầu tiếng thật, đuôi hàm mũ, kênh theo thẻ, cắt lược, vòng lặp có kiểm mối nối |
| `bash tools/audio-lab/run.sh batch0b all\|generate\|process\|recipes\|critic\|link\|session\|report [--force]` | Lô 0b vòng 2 (Stable Audio 3, 6 id) |
| `pnpm audio:batch0 all [--run R] [--force]` | Chạy trọn lô 0: bộ phát mẫu, dựng 10 công thức, chấm đủ lớp, ghi sổ, kiểm giấy phép, lập phiên lô 0a. File phiên đã có không bị ghi đè nếu thiếu `--force` (chủ dự án có thể đang chấm) |
| `bash tools/audio-lab/run.sh models [--download]` | Kiểm hoặc tải trọng số bộ phê bình |
| `bash tools/audio-lab/run.sh libraries [--offline]` | Tải hoặc kiểm lại thư viện CC0 ([`gen/README.md`](gen/README.md)) |
| `bash tools/audio-lab/poc/rerun.sh [--rules-only]` | Chạy lại bản thử (tham chiếu, không sửa) |

## Một vòng cho một id (mục 5.1)

```
specs/<game>/<id>.yaml ──► build/recipes/<game>/<id>.json ──► build render ──► masters/*.wav
                                  ▲ (lớp thư viện, tổng hợp,                     │
                                  │  bộ phát mẫu {"sampler": …})                ▼
sampler (VCSL, VSCO-2-CE) ────────┘                         critic run --spec --stage final --sources
                                                                                 │ _batch.json: top, distinct, probe
                         build mark-ai --from-critic ◄──────────────────────────┤
                         build release ─► licence-check                          ▼
                                                              board make-session ─► Bảng Nghe ─► ratings.jsonl
```

- **Bộ phê bình đọc thẻ spec:** `--spec specs/<game>` khớp file theo id dài nhất ở đầu tên (`gun.xung-v3.wav` → `gun.xung`); nhóm, độ dài, ngưỡng lên, nhịp chơi, nhãn AST lấy từ thẻ.
- **Bộ dựng ghi hồ sơ:** mỗi lần dựng có `SOURCES.json` (mục 10.5) và `licences.rows.jsonl` (mục 10.6). Lớp bộ phát mẫu ghi từng mẫu đã dùng, mỗi mẫu một dòng sổ.
- **Bộ phê bình không ghi sổ:** nó báo `ai_steps` trong JSON. `build mark-ai --from-critic` khớp theo SHA-256 rồi ghi bước AI và dòng mô hình (audiobox CC-BY-4.0, CLAP Apache-2.0, AST BSD-3-Clause). File có `aiInputAllowed=false` không bao giờ tới mô hình (truyền `--sources` cho bộ phê bình).
- **Danh sách nghe (mục 4.6 bước 2):** bản đứng đầu, bản khác nhất, và ở khoảng 30 % số id một bản dò rút từ nửa dưới của xếp hạng máy. Các mục ghi theo `stem` duy nhất của lần chấm. Bảng Nghe không lộ vai trò.
- **Clip trong nguồn của lớp:** `build render` kiểm clip trên từng file nguồn như đang lưu (thư viện, mẫu của bộ phát mẫu, file, đầu ra mô hình kèm cửa sổ) và dừng nếu có, trừ khi lớp ghi `allowClip`. Kết quả nằm ở `SOURCES.json` › `layers[].rawQa`; bộ phê bình (`--sources`) và `licence-check` đều đọc nó.
- **Biến thể là ứng viên:** công thức có `vary.swapMode: "cycle"` cho biến thể n dùng nguồn thứ n, để các ứng viên khác nhau có chủ đích (chọn hướng), không phụ thuộc may rủi.

## Giấy phép (mục 10)

- Chỉ dùng: CC0 (Kenney, VCSL, VSCO-2-CE, Freesound CC0 không từ chối AI), MIT, Apache-2.0, BSD-3-Clause, mã của dự án, bản ghi của chủ dự án. CC-BY phải có `CREDITS.md` (tự sinh).
- Cấm: mọi trọng số phi thương mại (mục 3.5, kể cả chỉ để so), Freesound NC và Sampling+, BBC, Pixabay, âm từ game khác, Sonniss trong bất kỳ bước AI nào.
- Mỗi thư viện giữ bản giấy phép có ngày tải. Bản dựng chép bản đó vào `art-src/audio/licences/` khi phát hành.
- `licence-check` chặn: file thiếu hồ sơ, mã băm lệch, nguồn thiếu dòng sổ, giấy phép lạ hay bị cấm, `commercial_ok=false`, nguồn cấm AI đã qua bước AI, Stable Audio 3 chưa đăng ký, bản ghi của người khác thiếu giấy đồng ý, CC-BY thiếu ghi công.
- pedalboard (GPL-3.0) chỉ được `import`. Thư mục này chưa có file `LICENSE`; khi thêm, chọn loại tương thích GPL (mục 10.9).

## Chỗ lệch so với chữ của kế hoạch (chờ chủ dự án duyệt rồi ghi vào kế hoạch)

| Chỗ | Kế hoạch | Audio Lab đang làm | Vì sao |
|---|---|---|---|
| Mối nối vòng lặp (4.3.1) | Bước nhảy mẫu < −40 dBFS; RMS, trọng tâm phổ so 50 ms | Bước nhảy tính phần vượt P95 bước mẫu của chính file; vòng nhạc chỉ chặn bởi bước nhảy (RMS, trọng tâm chỉ ghi) | Nền có nhiễu sáng luôn có bước mẫu lớn; phách mạnh ô đầu luôn to hơn đuôi ô cuối |
| Đỉnh phẳng (4.3.1) | 4 mẫu cùng độ lớn ở bất kỳ mức nào trên −20 dBFS | Chỉ tính trong 1 dB dưới đỉnh của kênh; file số thực và nén mất dữ liệu chỉ tính đoạn thật sự bằng nhau; PCM 8-bit không kiểm (cờ `low_bit_depth`); sóng vuông vẽ bằng mã không tính | Trần clip luôn là đỉnh của file kể cả sau chuẩn hóa; mẫu kèn co D2 VSCO và 17/50 file Kenney RPG bị chặn nhầm |
| Lệch DC (4.3.1) | Dưới 0,1 % FS | Đo DC thật (trung vị trung bình Hann 40 ms trên khung lặng), không lấy trung bình cả file | Tiếng trúng 120 ms ở 180 Hz không có DC vẫn có trung bình 0,26 % FS |
| Hỏi chủ dự án (4.5) | Khi L4 hay L1b gắn cờ | Cờ AST "thiếu nhãn mong đợi", "khó nhận ra" không tính; cờ L4 chỉ tính khi tách được các bản cùng id | Trước đây 28/34 bản cuối bị hỏi; giờ 4/37 |
| Bản dò (4.6 bước 2) | Nửa dưới hoặc bị cờ loại | Chỉ nửa dưới | Bản bị cờ ở nửa trên không phải bản máy xếp thấp |
| Khuôn L2 (4.3.3) | Theo nhóm | Thêm `hit_fire` (lửa trầm, không đòi lớp tách) cho `fire.impact.*`; `shot_launch` thêm sàn thân 150–800 Hz | Khuôn cũ chấm ngược mô tả thiết kế; bản mỏng đạt mọi mục |
| Lặp (7) | "Lặp 20 lần" | 8 lần với item phát cách nhau từ 1 s | Nốt thưởng 1,5 s × 20 = 30 s mỗi bản |
| Thẻ ảnh (7) | Hiện sau khi chấm | Lô 0a và phiên hiệu chỉnh: chỉ mở khi chấm xong cả phiên | Điểm máy hiện giữa các id dạy tai chủ dự án |
| Giấy phép (10.2) | Bảng không có | Cho phép BSD-3-Clause (trọng số AST, chỉ chạy trên máy) và CC-BY-3.0 (phải ghi công) | Cần cho bộ chấm; CC-BY-3.0 giống CC-BY-4.0 về ghi công |
| L3–L5 với file dài | — | File trên 2 phút: 6 đoạn 10 s cách đều | File 10 phút mất 209 s, 4,4 GB RAM |

Trọng số không dùng: `mispeech/midashenglm-0.6b-fp32` (2,6 GB) trong cache; thẻ mô hình trong cache ghi giấy phép Apache-2.0. Bộ chấm không dùng nó; xóa được (`~/AudioLab/README.md`).

## Môi trường an toàn

- Không token: `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN` luôn bị bỏ; `HF_HUB_DISABLE_IMPLICIT_TOKEN=1`, `HF_HUB_DISABLE_TELEMETRY=1`, `TOKENIZERS_PARALLELISM=false`.
- **Mặc định không mạng** với Hugging Face (`HF_HUB_OFFLINE=1`). Chỉ khi tải mô hình mới được phép mới chạy với `AUDIOLAB_ONLINE=1`, một lần.
- Mọi server chỉ nghe ở `127.0.0.1`. Bảng Nghe dùng cổng 3191; chỉ khi bận mới dùng 3192 và ghi rõ trong log.
- Máy 16 GB: mỗi lúc một mô hình nặng. Bộ phê bình nạp 4 mô hình chấm một lần mỗi tiến trình (khoảng 2–3 GB RAM). Tắt mọi server và trình duyệt mình mở.

## Module

| Thư mục | Việc | Giai đoạn | Phụ trách |
|---|---|---|---|
| `common/` | Đường dẫn, môi trường an toàn, `launch.py`, `setup.sh`, `lock.sh`, `fetch_models.py`, `batch0.py` (chạy trọn lô 0), `batch0b.py` (lô 0b vòng 2) | 0 | Làn Nền tảng; `batch0.py`, `fetch_models.py`: làn Ghép nối |
| `critic/` | L1 cổng vệ sinh, L1b dò lỗi do mô hình tạo, L2 đặc trưng, L3–L5 học máy, L6 thẻ ảnh, điểm tổng, danh sách nghe | 1 | Làn Critic |
| `specs/` | 147 thẻ spec YAML cho 3 game, sinh từ `catalog.ts` và các danh sách âm | 1 | Làn Specs |
| `board/` | Bảng Nghe v1: nghe mù, cân độ to, Một mình, Lặp 20 lần, Loa nhỏ | 1 | Làn Board |
| `build/` | Công thức, ghép lớp (thư viện, tổng hợp, bộ phát mẫu), chuỗi cuối, sổ giấy phép, `licence-check`, `critic_link.py` | 1–2 | Làn Build; `recipes/` và `critic_link.py`: làn Ghép nối |
| `sampler/` | Bộ phát mẫu Python: MIDI (mido) và mẫu CC0, dời tối đa 3 bán cung, chỉnh cao độ theo số đo | 2 | Làn Thư viện và Bộ phát mẫu |
| `gen/` | Tải thư viện CC0, chỉ mục, dòng giấy phép; lớp gọi Stable Audio 3 (`sa3.py`) và chuỗi xử lý đầu ra mô hình (`process.py`) | 2 | Làn Thư viện và Bộ phát mẫu |
| `harness/` | Nối với bộ thử của từng game (bài A–J). Không sửa mã game ở đây | 3 | (chưa giao) |
| `poc/` | Mã hai bản thử, đóng băng để tham chiếu (xem `poc/README.md`) | 0 | Làn Nền tảng |

## Quy ước cho người làm

- File phiên trong `~/AudioLab/review/<game>/sessions/` không bao giờ bị ghi đè lặng lẽ: `batch0`, `board from-critic` và `board calib-0a` đều cần `--force`.
- `games/**` **chỉ đọc**. Thứ sẽ vào `games/<game>/art-src/audio/` thì ghi vào `env.art_src_staging(game)`; người điều phối chép sang sau. Lô 0 không ghi vào staging chính thức, vì chưa có gì được chủ dự án duyệt.
- Không có media, trọng số, venv hay cache trong Git (`.gitignore` ở đây chặn âm, ảnh, video, nén, trọng số). Test tự sinh âm thử bằng numpy, không thêm file âm vào repo.
- Test đặt trong `<module>/tests/test_*.py`. pytest chạy ở chế độ `importlib`; `norecursedirs` trong `pytest.ini` đã bỏ mặc định "build", nên test của `build/` được thu.
- Ghi chú trong mã bằng tiếng Anh, ngắn. Chữ người dùng đọc (Bảng Nghe, báo cáo, README) bằng tiếng Việt có dấu.
- Không commit, không push. Tắt mọi tiến trình mình mở.
